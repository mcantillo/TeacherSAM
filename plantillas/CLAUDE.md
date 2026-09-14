# Templates (`plantillas/`) — style internals

Which template to copy for each document is in the `crear-material` and `crear-guia` skills;
this file is about the templates and the shared style themselves. The teacher-facing command
reference is `plantillas/README.md`.

**Changing the style or a template requires compiling and looking at the result.** If LaTeX
isn't available (`command -v latexmk`; e.g. in Cowork), don't edit them: tell the teacher the
change has to be made where LaTeX is installed (Claude Code on her Mac).

- `estilo/mmcantillo.sty` + `estilo/logo-colegio.png` are the **single shared copy** of the design. Never copy the `.sty` into template folders — each `.tex` loads it via `\makeatletter\def\input@path{{../estilo/}}\makeatother` before `\usepackage{mmcantillo}` (graphicx finds the logo through the same `\input@path`). Documents at another depth adjust the relative path.
- `quiz/`, `evaluacion/`, `documento/`, `guia-trimestral/` each hold one template `.tex`; new documents are copies of these with the data block (`\tipodocumento`, `\asignatura`, `\titulo`, `\grado`, `\periodo`, `\tiempo`) edited.
- `guia-didactica/` is the old, self-contained FPLAN v3 form (its own `guia-didactica.sty`, replicating a `.docx`). It's superseded by `guia-trimestral/`, which keeps the FPLAN evaluation sections; use the old form only if the teacher explicitly asks for it.
- Design constraints the teacher asked for: **printed in black & white** (white page, ink + grays only; plot curves distinguished by dash style via the `mmc` pgfplots cycle list, so use `\addplot+`), logo at full opacity, small, top-left. Header = school name, «Área de Matemáticas», year. Footer = teacher name · Docente · school + page X / Y.
- Fonts are `newpxtext`/`newpxmath` — do not also load `amssymb` (clashes: «`\Bbbk` already defined»).
- babel is loaded with `es-noshorthands` so `<`/`>` in tabular/tikz/pgfplots are safe; Spanish math names (`\sen`, `\tg`, `lím`) and decimal comma (`icomma`, siunitx `output-decimal-marker={,}`) are intended.
- `\pregunta[pts]` accumulates points with `\fpeval` and writes the total to the `.aux`; the total and `\pageref{LastPage}` need a second pass.
- The guía macros (`\frase`, `dba`, `cita`, `hilo`, `aplicacion`, `resumen`, `\tema`, `referencias`, `\matrizevaluacion`, `\autoevaluacion`, `\seguimientodocente`, `\guiadelestudiante`/`\refguia` via `xr-hyper`) are documented in `.claude/skills/crear-guia/REFERENCE.md`.

## Commands

```sh
cd plantillas/quiz && latexmk -pdf quiz.tex          # build (runs twice as needed)
latexmk -c quiz.tex                                   # remove aux files, keep PDF
pdflatex -jobname=quiz-clave "\def\clave{}\input{quiz}"   # answer key (run twice); \clave shows solucion blocks
pdftoppm -png -r 80 quiz.pdf /path/to/scratch/quiz    # render pages to check layout visually
```

After changing `mmcantillo.sty`, rebuild every template (`quiz`, `evaluacion`, `documento`, both guías in `guia-trimestral/`) and the real guías in `materias/*/*/guia-didactica/`, and inspect the rendered pages — layout regressions (orphaned headings, legends overlapping axis labels, boxes split across pages) only show up visually. Also search every log for glyphs the font lacks — they print nothing and raise no error: `LC_ALL=C grep -a -c 'Missing character' archivo.log` (the logs contain non-UTF-8 bytes, so a plain `grep` silently finds nothing). To see the offending line: `pdflatex "\tracinglostchars=3\input{archivo}"`. Known case, already fixed in the style: babel-spanish's accented operators (`lím`, `máx`, `mín`) lost their «í» in pdflatex.
