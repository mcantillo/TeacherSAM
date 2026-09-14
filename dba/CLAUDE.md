# DBA extraction pipeline (`dba/`)

To *use* the DBA (which file, which DBA, reviews), load the `alinear-dba` skill. This file is
only about regenerating the extracted files from the MEN PDFs. It needs poppler and LaTeX
(installed on the teacher's Mac); in an environment without them (`command -v pdftotext
latexmk`; e.g. Cowork), don't run it — the extracted files are already in the folder.

Pure-Python (stdlib only) + poppler (`pdftotext -bbox`, `pdftoppm`). Stages, each run from `dba/` with an output dir:

```sh
python3 tools/extract_text.py dba_matematicas-min.pdf matematicas        # 1-2: structure.json, raw/*.txt
pdftoppm -r 30 dba_matematicas-min.pdf DET_DIR/p                        # low-res renders for detection
python3 tools/extract_figs.py dba_matematicas-min.pdf matematicas DET_DIR  # 3: figs/*.png, figures.csv
python3 tools/apply_annotations.py matematicas   # 3b: apply fig_annotations.json, delete decorative/junk crops
python3 tools/build_tex.py matematicas           # 4: grados/gradoNN.tex
cd matematicas && latexmk -pdf main.tex
```

- Hand-maintained inputs per output dir: `fig_annotations.json` (`{stem: [kind, description]}`, kind ∈ figure|table|decorative|junk), optional `dba_select.json` (`{"grado": [dba,...]}` — limits output to chosen DBAs; used by `naturales/`), optional `tex_fixes.json` (`drop_lines` per grade to strip extraction noise).
- Page-geometry constants (`COL_SPLIT`, `HEADER_Y`, `FOOTER_Y`, crop thresholds) are tuned to the MEN PDF layout. `extract_figs.py` deliberately keeps its own `FOOTER_Y = 735` so crop filenames — and therefore the annotation keys — stay stable; changing detection parameters can orphan existing annotations.
- Figures are external files referenced as `\fig{stem}{description}`, never embedded; `\showfigsfalse` in `main.tex` builds captions only.
- `estandares_c.naturales.pdf` is the MEN Estándares de Ciencias Naturales (2004); its physics part is transcribed by hand in `naturales/estandares-fisica.md` (not produced by this pipeline).
