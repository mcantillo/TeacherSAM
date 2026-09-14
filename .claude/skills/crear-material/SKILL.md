---
name: crear-material
description: Creates the weekly class pack of a course — clase.tex (the teacher's lessons for every session of the week), quiz, taller, tarea and the optional material-de-estudiante — and the period exams, from the shared LaTeX templates. Use when the user asks for a clase, plan de clase, quiz, taller, tarea, material del estudiante, evaluación del periodo, answer key (clave), or the pack of a week (semana-NN).
---

# Material de clase: paquetes semanales y evaluaciones

Covers steps 4–5 of the order of work in `CLAUDE.md`. Also load `alinear-dba` (DBA comment
and evidencias) and read `.claude/referencias/registro-grados.md` for grades 3°–6°.

## Prerequisites

- The week's rows in `curriculo/programacion.csv` have `tema`, `subtema` and `dba` (if not → skill `planeacion`).
- The trimester's guía exists and is compiled with its `.aux` (if not → skill `crear-guia`).
- Say what's missing and offer to do it first (see «Order of work» in `CLAUDE.md`).

## The pack

- **The pack unit is the school week**: all the sessions a course has in a week share one pack, whatever the tema(s). `clase.tex` plans every session of that week (heading per session with its date and minutes, e.g. «Sesión 2 — jueves 10 sep., 50 min»), each timed to its row's `minutos`.
- A pack is **complete** when it has `clase.tex` (always) plus each of `quiz.tex`, `taller.tex`, `tarea.tex` that the week's rows mark with `x`. When the user asks for one piece (e.g. only the quiz), create just that file in the right pack and mention which planned files are still missing. If asked for a quiz/taller/tarea in a week whose rows don't mark it, ask whether to add the `x` to the plan.
- `material-de-estudiante.tex` is **optional**: extra practice for that class (exercises to leave in class, additional worksheets). The period's guía is the students' study material, so don't create this file by default and never report it as missing; create it only when the teacher asks, and don't repeat what's in the guía or the taller.

## Which template for each file

| File | Copy from | Data block |
|---|---|---|
| `clase.tex` | `plantillas/documento/documento.tex` | `\tipodocumento{Clase}`, `\encabezado*`, `\guiadelestudiante{…}` + `\refguia{…}` to the trimester's guía |
| `quiz.tex` | `plantillas/quiz/quiz.tex` | `\tipodocumento{Quiz}`, `\encabezado` |
| `taller.tex` | `plantillas/documento/documento.tex` | `\tipodocumento{Taller}`, `\encabezado` |
| `tarea.tex` | `plantillas/documento/documento.tex` | `\tipodocumento{Tarea}`, `\encabezado` |
| `material-de-estudiante.tex` | `plantillas/documento/documento.tex` | `\tipodocumento{Material del estudiante}`, `\encabezado` |
| `evaluaciones/periodo-*.tex` | `plantillas/evaluacion/evaluacion.tex` | `\tipodocumento{Evaluación}`, `\encabezado` |

- Always fill `\asignatura`, `\grado`, `\periodo` and `\titulo` from the grade folder and `programacion.csv`; never leave the template's sample values.
- Right under the data block: `% DBA: matematicas grado 11 · DBA 8 — <enunciado>` (skill `alinear-dba`). Each question should target at least one DBA *evidencia*.
- Relative path to the shared style (the `\input@path` line): from `clases/semana-NN/` → `{{../../../../../plantillas/estilo/}}`; from `evaluaciones/` → `{{../../../../plantillas/estilo/}}`. Compile from the file's own folder to confirm it resolves (a wrong depth fails with «File `mmcantillo.sty' not found»).

## Citing the guía from `clase.tex`

Add `\guiadelestudiante{../../guia-didactica/guia-periodo-I-<tema>}` to the preamble (path without
`.tex`) and cite with `\refguia{tema:clave}`, which prints «Guía del estudiante, Tema N (p. X)».
Compile the guía first; if a label is missing the class shows `??`. Teacher notes (timing,
questions for the group, how to run an activity) go in `clase.tex`, never in the guía.

## Assessment rules

- **Grading scale:** the school grades from **1,0 to 5,0** (desempeño Bajo < 3,0 · Básico 3,0–3,9 · Alto 4,0–4,5 · Superior 4,6–5,0; bands pending confirmation against the school's SIEE). Every quiz, taller and evaluación must add up to exactly **5 points** in its `\pregunta[...]` values (decimals like `0.5` are fine); check `\totalpuntos` = 5 after compiling.
- Quizzes, talleres and tareas include `solucion` blocks; the answer key is built with `pdflatex -jobname=<nombre>-clave "\def\clave{}\input{<nombre>}"` (run twice).
- Take ideas from `recursos/` (`recursos/CLAUDE.md`); when an exercise comes from a recurso, add `% Recurso: recursos/<ruta>` and verify it — recursos have errors.
- **Exercises go through the bank** (skill `verificar-ejercicios`): reuse verified ones (`python3 tools/ejercicios.py listar --tema … --grado …`), put new ones in `recursos/banco/` and verify them (only new or changed exercises are checked). Write `% Ejercicio: <id>` above each `\pregunta` and fill its `solucion` block from the bank's `respuesta`. Only exercises with estado `verificado` or `manual-aprobado` go into a document.

## Finish

If LaTeX is available (`command -v latexmk`): `latexmk -pdf <file>.tex` from its folder,
render the pages (`pdftoppm -png -r 70 <file>.pdf …`) and look at them, then `latexmk -c`.
If it isn't (e.g. in Cowork), follow `INSTRUCCIONES-COWORK.md`: add up the points by hand and
tell the teacher the PDFs are **not compiled or reviewed yet**. Report which planned files of
the week are still missing.
