#!/usr/bin/env python3
"""Stage 3: detect figure regions (raster or vector) and crop them to PNG.

Usage: python3 tools/extract_figs.py dba_matematicas-min.pdf out_dir det_dir
  det_dir holds low-res colour renders:  pdftoppm -r 30 PDF det_dir/p
Reads out_dir/structure.json, writes out_dir/figs/*.png and out_dir/figures.csv.
No third-party dependencies: detection parses PPM in pure Python, cropping uses pdftoppm.
"""
import csv, json, subprocess, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from extract_text import COL_SPLIT, DBA_NUM, FOOTER_Y, HEADER_Y, label_words, read_pages

DET_DPI = 30
CROP_DPI = 150
PT = 72 / DET_DPI          # points per detection pixel
BODY_X = (40, 575)         # ignore crop marks / margin decorations outside
DET_TOP = 140              # the green title banner ends at ~132pt
FOOTER_Y = 735             # figure search bottom; kept at 735 so crop names (and annotations) stay stable
MERGE_PT = 22              # merge ink blobs closer than this (pictogram rows, table cells)
PAD_PT = 6
MIN_W_PT, MIN_H_PT = 36, 24
MIN_INK = 30               # detection pixels


def read_ppm(path):
    data = path.read_bytes()
    parts, i = [], 0
    while len(parts) < 4:              # magic, width, height, maxval
        while data[i:i + 1].isspace():
            i += 1
        j = i
        while not data[j:j + 1].isspace():
            j += 1
        parts.append(data[i:j])
        i = j
    w, h = int(parts[1]), int(parts[2])
    return w, h, data[i + 1:]


def is_ink(r, g, b):
    lo, hi = min(r, g, b), max(r, g, b)
    return lo < 150 or (hi - lo > 90 and lo < 190)   # dark, or strongly coloured (not pastel)


def ink_mask(ppm, words):
    w, h, px = read_ppm(ppm)
    mask = [[False] * w for _ in range(h)]
    y0, y1 = int(DET_TOP / PT), int(FOOTER_Y / PT)
    x0, x1 = int(BODY_X[0] / PT), int(BODY_X[1] / PT)
    for y in range(y0, min(y1, h)):
        row = mask[y]
        base = y * w * 3
        for x in range(x0, min(x1, w)):
            k = base + 3 * x
            row[x] = is_ink(px[k], px[k + 1], px[k + 2])
    for wx0, wy0, wx1, wy1, _ in words:       # erase text: what remains is graphics
        for y in range(max(0, int(wy0 / PT) - 1), min(h, int(wy1 / PT) + 2)):
            for x in range(max(0, int(wx0 / PT) - 1), min(w, int(wx1 / PT) + 2)):
                mask[y][x] = False
    return mask


def blobs(mask):
    h, w = len(mask), len(mask[0])
    seen = [[False] * w for _ in range(h)]
    out = []
    for sy in range(h):
        for sx in range(w):
            if not mask[sy][sx] or seen[sy][sx]:
                continue
            stack, n = [(sy, sx)], 0
            seen[sy][sx] = True
            bx0 = bx1 = sx
            by0 = by1 = sy
            while stack:
                y, x = stack.pop()
                n += 1
                bx0, bx1, by0, by1 = min(bx0, x), max(bx1, x), min(by0, y), max(by1, y)
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < h and 0 <= nx < w and mask[ny][nx] and not seen[ny][nx]:
                            seen[ny][nx] = True
                            stack.append((ny, nx))
            out.append([bx0 * PT, by0 * PT, (bx1 + 1) * PT, (by1 + 1) * PT, n])
    return out


def near(a, b, gap):
    return not (a[2] + gap < b[0] or b[2] + gap < a[0] or a[3] + gap < b[1] or b[3] + gap < a[1])


def merge(boxes, gap):
    boxes = [b[:] for b in boxes]
    changed = True
    while changed:
        changed = False
        for i in range(len(boxes)):
            for j in range(i + 1, len(boxes)):
                a, b = boxes[i], boxes[j]
                if near(a, b, gap):
                    boxes[i] = [min(a[0], b[0]), min(a[1], b[1]), max(a[2], b[2]), max(a[3], b[3]), a[4] + b[4]]
                    del boxes[j]
                    changed = True
                    break
            if changed:
                break
    return boxes


def is_thin(b):
    """A long straight rule. Short specks (e.g. pieces of a broken diagonal) are not thin."""
    w, h = b[2] - b[0], b[3] - b[1]
    return (h <= 6 and w > 20) or (w <= 6 and h > 20)


def overlap_frac(t, c):
    """Share of a thin line's length that lies within core c's span along the same axis."""
    if t[2] - t[0] >= t[3] - t[1]:
        lo, hi, a, b = t[0], t[2], c[0], c[2]
    else:
        lo, hi, a, b = t[1], t[3], c[1], c[3]
    return max(0.0, min(hi, b) - max(lo, a)) / max(hi - lo, 1e-6)


def attach_thin(cores, thin, gap):
    """Grow cores with thin strokes (table rules, figure edges) that run along them.

    Ruled note lines and the wavy column divider stay out: they sit beside a figure,
    not along it.
    """
    cores = [c[:] for c in cores]
    pending = thin[:]
    changed = True
    while changed:
        changed = False
        for t in pending[:]:
            for c in cores:
                if near(c, t, gap) and overlap_frac(t, c) >= 0.5:
                    c[0], c[1], c[2], c[3] = min(c[0], t[0]), min(c[1], t[1]), max(c[2], t[2]), max(c[3], t[3])
                    c[4] += t[4]
                    pending.remove(t)
                    changed = True
                    break
    return merge(cores, 2)


def absorb_labels(box, words):
    """Grow a figure box to include label words touching it."""
    for _ in range(3):
        for wx0, wy0, wx1, wy1, _t in words:
            if near(box, (wx0, wy0, wx1, wy1), 10):
                box = [min(box[0], wx0), min(box[1], wy0), max(box[2], wx1), max(box[3], wy1), box[4]]
    return box


def dba_at(dba_marks, page, col, y):
    """Last DBA number printed before (page, column, y) in reading order."""
    key = (page, col, y)
    best = None
    for m in dba_marks:
        if m[:3] <= key:
            best = m[3]
    return best


def main(pdf, out_dir, det_dir):
    out, det = Path(out_dir), Path(det_dir)
    structure = json.loads((out / "structure.json").read_text())
    (out / "figs").mkdir(exist_ok=True)
    pages = read_pages(pdf)
    ranges = [("intro", *structure["intro"])] + [(int(g), a, b) for g, (a, b) in structure["grades"].items()]
    rows = []
    for grade, a, b in ranges:
        marks = []
        for p in range(a, b + 1):
            for w in pages[p - 1]:
                if DBA_NUM.match(w[4]) and (w[0] < 75 or COL_SPLIT <= w[0] < 345) and HEADER_Y <= w[1] < FOOTER_Y:
                    marks.append((p, int(w[0] >= COL_SPLIT), w[1], int(w[4][:-1])))
        marks.sort()
        for p in range(a, b + 1):
            words = [w for w in pages[p - 1] if HEADER_Y <= w[1] < FOOTER_Y]
            ppm = det / f"p-{p:02d}.ppm"
            labels = label_words(words)
            # Merge thick blobs first; thin strokes join only along an existing figure, so ruled
            # "notes" lines and the column divider can't chain neighbours into a page-sized box.
            raw = blobs(ink_mask(ppm, words))
            cores = merge([bx for bx in raw if not is_thin(bx)], MERGE_PT)
            found = [bx for bx in attach_thin(cores, [bx for bx in raw if is_thin(bx)], MERGE_PT)
                     if bx[4] >= MIN_INK]
            found = merge([absorb_labels(bx, labels) for bx in found], 2)
            found = [bx for bx in found if bx[2] - bx[0] >= MIN_W_PT and bx[3] - bx[1] >= MIN_H_PT]
            found.sort(key=lambda bx: (int((bx[0] + bx[2]) / 2 >= COL_SPLIT), bx[1]))
            for k, (x0, y0, x1, y1, _) in enumerate(found, 1):
                x0, y0 = max(0, x0 - PAD_PT), max(0, y0 - PAD_PT)
                x1, y1 = min(612, x1 + PAD_PT), min(793, y1 + PAD_PT)
                col = int((x0 + x1) / 2 >= COL_SPLIT)
                dba = dba_at(marks, p, col, y0) if grade != "intro" else None
                tag = "intro" if grade == "intro" else f"g{grade:02d}"
                name = f"{tag}_p{p:02d}_{k}"
                s = CROP_DPI / 72
                subprocess.run(["pdftoppm", "-r", str(CROP_DPI), "-f", str(p), "-l", str(p),
                                "-x", str(int(x0 * s)), "-y", str(int(y0 * s)),
                                "-W", str(int((x1 - x0) * s)), "-H", str(int((y1 - y0) * s)),
                                "-png", "-singlefile", pdf, str(out / "figs" / name)], check=True)
                rows.append({"file": f"figs/{name}.png", "page": p, "grade": grade, "dba": dba or "",
                             "x": round(x0), "y": round(y0), "w": round(x1 - x0), "h": round(y1 - y0),
                             "keep": "", "description": ""})
        print(grade, sum(1 for r in rows if r["grade"] == grade), file=sys.stderr)
    with open(out / "figures.csv", "w", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=list(rows[0]))
        wr.writeheader()
        wr.writerows(rows)
    print(len(rows), "figures")


if __name__ == "__main__":
    main(*sys.argv[1:4])
