#!/usr/bin/env python3
"""Stage 3b: merge hand annotations into figures.csv and keep only important images.

Usage: python3 tools/apply_annotations.py out_dir
Reads out_dir/fig_annotations.json ({stem: [kind, description]}), where kind is
figure | table | decorative | junk. Rewrites out_dir/figures.csv with kind/description,
deletes decorative and junk crops from out_dir/figs, and reports unannotated crops.
"""
import csv, json, sys
from pathlib import Path

from build_tex import load_select

KEEP = {"figure", "table"}


def main(out_dir):
    out = Path(out_dir)
    notes = json.loads((out / "fig_annotations.json").read_text())
    with open(out / "figures.csv") as f:
        rows = list(csv.DictReader(f))
    select = load_select(out)
    if select:   # crops outside the selected DBAs are discarded without needing annotations
        chosen = lambda r: r["grade"] != "intro" and r["dba"] and int(r["dba"]) in select.get(int(r["grade"]), ())
        for r in rows:
            if not chosen(r):
                (out / r["file"]).unlink(missing_ok=True)
        rows = [r for r in rows if chosen(r)]
    missing, kept = [], []
    for r in rows:
        stem = Path(r["file"]).stem
        kind, desc = notes.get(stem, ["", ""])
        if not kind:
            missing.append(stem)
            continue
        png = out / r["file"]
        if kind not in KEEP:
            png.unlink(missing_ok=True)
            continue
        r.pop("keep", None)
        r["kind"], r["description"] = kind, desc
        kept.append(r)
    stale = sorted(set(notes) - {Path(r["file"]).stem for r in rows})
    fields = ["file", "page", "grade", "dba", "kind", "description", "x", "y", "w", "h"]
    with open(out / "figures.csv", "w", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        wr.writeheader()
        wr.writerows(kept)
    print(f"kept {len(kept)} of {len(rows)} crops "
          f"({sum(r['kind'] == 'figure' for r in kept)} figures, {sum(r['kind'] == 'table' for r in kept)} tables)")
    if missing:
        print("UNANNOTATED (left in figs/, not in csv):", " ".join(missing))
    if stale:
        print("annotations with no crop:", " ".join(stale))


if __name__ == "__main__":
    main(sys.argv[1])
