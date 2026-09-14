#!/usr/bin/env python3
"""Stages 1-2: detect grade page ranges and extract clean per-column text.

Usage: python3 tools/extract_text.py dba_matematicas-min.pdf out_dir
Writes out_dir/structure.json and out_dir/raw/{intro,grado_XX}.txt
"""
import html, json, re, subprocess, sys
from collections import defaultdict
from pathlib import Path

COL_SPLIT = 330      # x: left column < split <= right column
HEADER_Y = 95        # drop running header above this
FOOTER_Y = 775        # body text reaches ~765; page number sits at ~785, indd footer at ~820
LINE_TOL = 3.0       # words whose yMin differ less than this share a line
DBA_NUM = re.compile(r"^\d{1,2}\.$")
BULLET = {"m": "- ", "q": "* ", "u": "- "}  # icon-font glyphs used as bullets
NOISE = re.compile(r"(Matemáticas •|Derechos Básicos de Aprendizaje|\.indd|^\d{1,2}/\d{1,2}/\d{2})")

WORD_RE = re.compile(
    r'<page width="[\d.]+" height="[\d.]+">|</page>|'
    r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>'
)


def read_pages(pdf):
    out = subprocess.run(["pdftotext", "-bbox", pdf, "-"], capture_output=True, text=True, check=True).stdout
    pages, cur = [], None
    for m in WORD_RE.finditer(out):
        tok = m.group(0)
        if tok.startswith("<page"):
            cur = []
        elif tok == "</page>":
            pages.append(cur)
        else:
            x0, y0, x1, y1 = map(float, m.group(1, 2, 3, 4))
            cur.append((x0, y0, x1, y1, html.unescape(m.group(5))))
    return pages


def grade_of(words):
    top = [w for w in words if w[1] < HEADER_Y]
    if not any(w[4] in ("Grado", "Grad") for w in top):      # some headers split as "Grad o"
        return None
    digits = [re.match(r"\d{1,2}", w[4]) for w in top]
    found = [int(d.group(0)) for d in digits if d]
    return found[0] if found else None


def build_lines(words):
    lines = []
    for w in sorted(words, key=lambda w: (w[1], w[0])):
        if lines and abs(lines[-1]["y"] - w[1]) < LINE_TOL:
            lines[-1]["w"].append(w)
        else:
            lines.append({"y": w[1], "w": [w]})
    for ln in lines:
        ln["w"].sort(key=lambda w: w[0])
        ln["x"] = ln["w"][0][0]
        ln["text"] = " ".join(w[4] for w in ln["w"])
    return lines


def column_text(words, figs=()):
    """Reading-order text for one column; figs = (x0, y0, x1, y1, stem) boxes placed as [[FIG stem]]."""
    pending = sorted(figs, key=lambda f: (f[1] + f[3]) / 2)
    text = _column_lines(words, pending)
    return text


def _column_lines(words, pending):
    nums = [w for w in words if DBA_NUM.match(w[4])
            and (w[0] < 75 or COL_SPLIT <= w[0] < 345)]
    body = [w for w in words if w not in nums]
    lines = [l for l in build_lines(body) if not NOISE.search(l["text"])]
    if not lines:
        return "\n\n".join(f"[[FIG {f[4]}]]" for f in pending)
    gaps = sorted(b["y"] - a["y"] for a, b in zip(lines, lines[1:]))
    step = gaps[len(gaps) // 2] if gaps else 12

    # Re-anchor each floating DBA number at the first line of its statement block.
    markers = {}
    for n in nums:
        i = min(range(len(lines)), key=lambda k: abs(lines[k]["y"] - n[1]))
        while i > 0 and lines[i]["y"] - lines[i - 1]["y"] < 1.6 * step:
            i -= 1
        markers[i] = n[4].rstrip(".")

    out, prev_y = [], None
    for i, ln in enumerate(lines):
        # A figure goes before the first line below its vertical centre, so a lead-in line
        # captured at the top of its box ("Dado el siguiente circuito:") stays ahead of it.
        while pending and (pending[0][1] + pending[0][3]) / 2 < ln["y"]:
            out += ["", f"[[FIG {pending.pop(0)[4]}]]", ""]
            prev_y = None
        if prev_y is not None and ln["y"] - prev_y > 1.6 * step:
            out.append("")
        if i in markers:
            out.append(f"[[DBA {markers[i]}]]")
        t = ln["text"]
        first, _, rest = t.partition(" ")
        if first in BULLET and rest[:1].isupper():
            t = BULLET[first] + rest
        elif first[:1] in BULLET and (first[1:2].isupper() or first[1:2] == "¿"):   # glyph glued: "qPaula"
            t = BULLET[first[0]] + t[1:]
        out.append(t)
        prev_y = ln["y"]
    for f in pending:
        out += ["", f"[[FIG {f[4]}]]"]
    return "\n".join(out)


def label_words(words):
    """Words that are not running body text: axis labels, legends, table cells.

    Body text lines have >= 5 words with tight spacing; table rows are sparse.
    """
    lines = {}
    for w in words:
        lines.setdefault((int(w[0] >= COL_SPLIT), round(w[1] / 3)), []).append(w)
    out = []
    for ln in lines.values():
        ln.sort(key=lambda w: w[0])
        gaps = sorted(b[0] - a[2] for a, b in zip(ln, ln[1:]))
        if len(ln) >= 5 and gaps[len(gaps) // 2] < 8:
            continue
        out.extend(ln)
    return out


def figure_boxes(out):
    """Kept figure boxes per page, from a previous Stage 3 run (empty if none yet)."""
    path = out / "figures.csv"
    boxes = defaultdict(list)
    if path.exists():
        import csv
        for r in csv.DictReader(open(path)):
            x, y, w, h = (float(r[k]) for k in "xywh")
            boxes[int(r["page"])].append((x, y, x + w, y + h, Path(r["file"]).stem))
    return boxes


def drop_figure_labels(words, boxes):
    """Remove label words (legends, table cells) lying inside a figure; the figure keeps them."""
    inside = lambda w: any(b[0] <= (w[0] + w[2]) / 2 <= b[2] and b[1] <= (w[1] + w[3]) / 2 <= b[3] for b in boxes)
    heading = {"Ejemplo", "Ejemplos", "Evidencias", "de", "aprendizaje"}
    drop = {id(w) for w in label_words(words) if inside(w) and w[4] not in heading}
    return [w for w in words if id(w) not in drop]


def dehyphenate(text):
    return re.sub(r"(\w)-\n(\w)", r"\1\2", text)


def page_text(words, columns=2, figs=()):
    if columns == 1:
        return column_text([w for w in words if HEADER_Y <= w[1] < FOOTER_Y], figs)
    left = [w for w in words if w[0] < COL_SPLIT and HEADER_Y <= w[1] < FOOTER_Y]
    right = [w for w in words if w[0] >= COL_SPLIT and HEADER_Y <= w[1] < FOOTER_Y]
    in_right = lambda f: (f[0] + f[2]) / 2 >= COL_SPLIT
    return (column_text(left, [f for f in figs if not in_right(f)]) + "\n\n"
            + column_text(right, [f for f in figs if in_right(f)]))


def main(pdf, out_dir, keep_labels=False):
    """keep_labels: leave figure-label words in the text (complete raw text); markers are still added."""
    out = Path(out_dir)
    (out / "raw").mkdir(parents=True, exist_ok=True)
    pages = read_pages(pdf)
    grades = defaultdict(list)
    for i, words in enumerate(pages, 1):
        g = grade_of(words)
        if g:
            grades[g].append(i)
    first_grade_page = min(p for ps in grades.values() for p in ps)
    structure = {
        "pages": len(pages),
        "intro": [5, first_grade_page - 1],
        "grades": {g: [ps[0], ps[-1]] for g, ps in sorted(grades.items())},
    }
    # Last grade page lacks a header sometimes: extend it until the closing page.
    last = max(grades)
    for p in range(structure["grades"][last][1] + 1, len(pages) + 1):
        if any(DBA_NUM.match(w[4]) for w in pages[p - 1]):
            structure["grades"][last][1] = p
    (out / "structure.json").write_text(json.dumps(structure, indent=2))

    boxes = figure_boxes(out)
    intro = "\n\n".join(f"%% page {p}\n" + page_text(pages[p - 1], columns=1, figs=boxes[p])
                        for p in range(structure["intro"][0], structure["intro"][1] + 1))
    (out / "raw" / "intro.txt").write_text(dehyphenate(intro) + "\n")
    for g, (a, b) in structure["grades"].items():
        txt = "\n\n".join(f"%% page {p}\n" + page_text(pages[p - 1] if keep_labels else drop_figure_labels(pages[p - 1], boxes[p]),
                                                    figs=boxes[p])
                          for p in range(a, b + 1))
        (out / "raw" / f"grado_{g:02d}.txt").write_text(dehyphenate(txt) + "\n")
    print(json.dumps(structure))


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    main(args[0], args[1], keep_labels="--keep-labels" in sys.argv)
