#!/usr/bin/env python3
"""Stage 4: raw grade text + figures.csv -> LaTeX.

Usage: python3 tools/build_tex.py out_dir
Writes out_dir/grados/gradoNN.tex. Figures appear in place, where the [[FIG stem]]
markers from extract_text.py put them, as \\fig{stem}{description}; the image is an
external file (figs/stem.png), never embedded.
"""
import csv, json, re, sys
from pathlib import Path

TEX_ESC = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
           "_": r"\_", "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}
END_PUNCT = tuple(".:?!;)”\"")


def esc(s):
    return "".join(TEX_ESC.get(c, c) for c in s)


def new_dba(num, page):
    return {"num": num, "page": page, "statement": [], "evid": [], "ejemplo": []}


def add_text(blocks, text, kind, fresh):
    """Append a line to the last text block, or open a new block.

    A paragraph split only by a column/page break (previous block unfinished and this
    one starting lowercase) is joined back rather than opened fresh; a figure that sat
    at that break then follows the rejoined paragraph.
    """
    last = next((b for b in reversed(blocks) if b[0] != "fig"), None)
    if not fresh and blocks and blocks[-1][0] != "fig":
        blocks[-1][1] += " " + text
    elif fresh and last and not last[1].rstrip().endswith(END_PUNCT) and text[:1].islower():
        last[1] += " " + text
    else:
        blocks.append([kind, text])


def parse(path):
    dbas, cur, section, fresh, page = [], None, None, True, None
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if line.startswith("%% page"):
            page = int(line.split()[-1])
            fresh = True
            continue
        if not line:
            fresh = True
            continue
        m = re.match(r"\[\[DBA (\d+)\]\]", line)
        if m:
            cur = new_dba(int(m.group(1)), page)
            dbas.append(cur)
            section, fresh = "statement", True
            continue
        if cur is None:
            continue
        m = re.match(r"\[\[FIG (\S+)\]\]", line)
        if m:
            # A figure inside the statement belongs with the evidence/example that follows.
            cur["evid" if section == "statement" else section].append(["fig", m.group(1)])
            fresh = True
            continue
        if re.match(r"^Evidencias? de aprendizaje$", line):
            section, fresh = "evid", True
            continue
        m = re.match(r"^Ejemplos?(?:\s+(\d+)|\s*\[\d+\])?$", line)   # "Ejemplo", "Ejemplo 2", "Ejemplo [1]"
        if m:
            section, fresh = "ejemplo", True
            if m.group(1):
                cur["ejemplo"].append(["sub", f"Ejemplo {m.group(1)}."])
            continue
        blocks = cur[section]
        if line.startswith(("- ", "* ")):
            blocks.append(["item", line[2:]])
            fresh = False
            continue
        add_text(blocks, line, "par", False if section == "statement" else fresh)
        fresh = False
    return dbas


def render_blocks(blocks, figs, placed):
    out, in_list = [], False
    for kind, text in blocks:
        if kind == "item" and not in_list:
            out.append(r"\begin{itemize}")
            in_list = True
        if kind != "item" and in_list:
            out.append(r"\end{itemize}")
            in_list = False
        if kind == "fig":
            if text in figs:          # decorative/junk crops were deleted: their markers are skipped
                out += [rf"\fig{{{text}}}{{{esc(figs[text]['description'])}}}", ""]
                placed.add(text)
            continue
        if kind == "sub":
            out += [rf"\textbf{{{esc(text)}}}", ""]
            continue
        out.append((r"  \item " if kind == "item" else "") + esc(text))
        if kind != "item":
            out.append("")
    if in_list:
        out.append(r"\end{itemize}")
    return out


def render_grade(g, dbas, figs, placed):
    out = [f"% Grado {g} -- generado por tools/build_tex.py a partir de raw/grado_{g:02d}.txt",
           rf"\section{{Grado {g}}}\label{{grado:{g}}}", ""]
    for d in dbas:
        statement = " ".join(t for k, t in d["statement"] if k == "par")
        out += [f"% PDF p. {d['page']}", rf"\dba{{{d['num']}}}{{{esc(statement)}}}", "", r"\evidencias", ""]
        out += render_blocks(d["evid"], figs, placed)
        out += ["", r"\ejemplo", ""]
        out += render_blocks(d["ejemplo"], figs, placed)
        out.append("")
    return "\n".join(out) + "\n"


def load_select(out):
    """Optional out_dir/dba_select.json: {"grado": [dba, ...]} limits output to those DBAs."""
    path = Path(out) / "dba_select.json"
    if not path.exists():
        return None
    return {int(g): set(nums) for g, nums in json.loads(path.read_text()).items()}


def main(out_dir):
    out = Path(out_dir)
    structure = json.loads((out / "structure.json").read_text())
    rows = list(csv.DictReader(open(out / "figures.csv")))
    select = load_select(out)
    if select:
        rows = [r for r in rows if r["grade"] != "intro" and r["dba"]
                and int(r["dba"]) in select.get(int(r["grade"]), ())]
    figs = {Path(r["file"]).stem: r for r in rows}
    placed = set()

    # Hand corrections: {"grado": [[regex, replacement], ...], "drop_lines": {"grado": [exact line, ...]}}
    # Regexes fix math the PDF text layer scrambles; drop_lines removes leftover figure-label text.
    fixes_path = out / "tex_fixes.json"
    fixes = json.loads(fixes_path.read_text()) if fixes_path.exists() else {}
    drops = fixes.pop("drop_lines", {})
    (out / "grados").mkdir(exist_ok=True)
    for g in sorted(select) if select else map(int, structure["grades"]):
        dbas = parse(out / "raw" / f"grado_{g:02d}.txt")
        if select:
            dbas = [d for d in dbas if d["num"] in select[g]]
        before = len(placed)
        tex = render_grade(g, dbas, figs, placed)
        for pattern, repl in fixes.get(str(g), []):
            tex, n = re.subn(pattern, lambda _m, r=repl: r, tex, flags=re.S)
            if n != 1:
                print(f"  ! grado {g}: fix matched {n} times: {pattern[:60]}")
        drop = set(drops.get(str(g), []))
        if drop:
            lines = tex.split("\n")
            kept = [ln for ln in lines if ln.strip() not in drop]
            unused = drop - {ln.strip() for ln in lines}
            if unused:
                print(f"  ! grado {g}: drop_lines not found: {sorted(unused)}")
            tex = re.sub(r"\n{3,}", "\n\n", "\n".join(kept))
        (out / "grados" / f"grado{g:02d}.tex").write_text(tex)
        print(f"grado {g:2d}: {len(dbas)} DBA, {len(placed) - before} figuras en su lugar")
    missing = sorted(s for s, r in figs.items() if s not in placed and r["grade"] != "intro")
    if missing:
        print("  ! figuras sin ubicar:", " ".join(missing))


if __name__ == "__main__":
    main(sys.argv[1])
