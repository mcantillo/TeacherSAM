---
name: verificar-ejercicios
description: Verifies math and physics exercises and their answers with Python and SymPy, and keeps them in the exercise bank (recursos/banco/) so each exercise is checked only once and reused afterwards. Use when writing, reusing or reviewing exercises for guías, quices, talleres, tareas or evaluaciones, when building an answer key, when the teacher asks to check an exercise or an answer, or when working with the banco de ejercicios.
---

# Verificar ejercicios (banco de ejercicios)

Every exercise that goes into a document lives in `recursos/banco/<area>/<tema>.py` with code that
checks its answer. `tools/ejercicios.py` runs the checks **only for exercises that are new or
changed** (a hash of statement + answer + check code); verified ones are reused without
re-running or re-deriving them. State: `recursos/banco/verificados.json`.

**Pending review:** `recursos/banco/PENDIENTES.md` is the checklist of what's left to trust the
bank fully (teacher decisions, open answers to approve, corrections and invented data to confirm,
transcription samples, LaTeX compile). Check it before using an exercise, and tick or update
its boxes when you finish one of its tasks.

## Environment (same commands in Claude Code and in Cowork)

- Always run `python3 tools/ejercicios.py …`. If that Python lacks SymPy and the folder has a
  working `.venv/` (the teacher's Mac), the tool switches to it by itself.
- If it reports that SymPy is missing (e.g. in Cowork): `python3 -m pip install -r tools/requirements.txt`.
  If SymPy can't be installed, the checks can't run: say the new exercises are **not verified**
  and keep them out of documents (exercises already verified in the bank can still be used).
- Never mark or report an exercise as verified without running its check.
- **Several agents in parallel:** each runs `verificar --sin-registro <its files>` (runs every
  check, doesn't touch `verificados.json`) and names its files and ids with the grade
  (`<tema>-<grado>.py`, `<tema>-<grado>-NNN`) so they can't collide; when all are done, one
  session runs `verificar` once to record them.

## Workflow

1. **Reuse first:** `python3 tools/ejercicios.py listar --tema <tema> --grado <N>` and
   `mostrar <id>`. An exercise with estado `verificado` or `manual-aprobado` can be used as is.
2. **New exercise:** add it to the right `recursos/banco/<area>/<tema>.py` (create the file if the tema
   is new; `matematicas/` or `fisica/`). Ids: `<tema-slug>-NNN`, never reused or renamed.
3. **Run** `python3 tools/ejercicios.py verificar recursos/banco/<area>/<tema>.py`. A `falla` means the
   statement, the answer or the check is wrong: find which one and fix it — if the exercise
   came from a recurso or an official DBA example, tell the teacher about the error.
4. **Open-ended exercises** (explain, argue, draw) use `ejercicio_manual` with a model answer;
   they stay `manual-pendiente` until the teacher approves the answer, then
   `python3 tools/ejercicios.py aprobar <id>`.
5. **Report** a table: id · enunciado (short) · respuesta · estado. Only `verificado` and
   `manual-aprobado` exercises may go into a document; in the `.tex`, write
   `% Ejercicio: <id>` above each `\pregunta` and take the `solucion` from `respuesta`.

## Format

```python
from sympy import Interval, S, solveset, symbols
from ejercicios import ejercicio, ejercicio_manual
x = symbols("x", real=True)

@ejercicio(id="inecuaciones-001", tema="inecuaciones cuadráticas", grados=[11],
           dba=["matematicas-11-2"], tipo="calculo", dificultad=1, fuente="…",
           enunciado=r"Resuelve $x^2 - x - 6 \le 0$.", respuesta=r"$[-2, 3]$.")
def _():
    assert solveset(x**2 - x - 6 <= 0, x, S.Reals) == Interval(-2, 3)
```

Fields: `id`, `enunciado`, `respuesta` (LaTeX, as they'll appear in the document) are required;
`tema`, `grados`, `dba` (`<area>-<grado>-<N>`), `tipo` (calculo · contexto · argumentacion ·
encuentra-el-error · seleccion · conceptual), `dificultad` (1–3), `fuente`, `notas` optional.
Example file: `recursos/banco/matematicas/inecuaciones.py`.

**Series of inequalities, equations and intervals** (`tools/ejercicios.py`): write each
statement **once** as plain text — `desigualdad("4 - 3x > 7 + 2x")` gives its LaTeX and its
solution set, so statement and check can't disagree (chains `-1 < (3 - 7x)/4 <= 6`,
`Abs(…)`, `sqrt(2)x`, `x^2`, decimals `0.3` → `0{,}3` all work). Write the solution **by hand**
with `conjunto("(-oo, -3/5] U {2}")` (also `R`, `vacio`; decimal endpoints get `;`), and
`serie(prefijo, "Resuelve …", fuente, filas, **comun)` registers one exercise per row
`(n, literal, texto, solución, dificultad[, notas])`, checking solveset against your answer.
Examples: `recursos/banco/matematicas/inecuaciones-lineales.py`, `intervalos.py`.

## Exercises from a recurso

Read the recurso in its `markdown/` copy (formulas in LaTeX, exercises with their «5.», «b.»
labels — see `recursos/CLAUDE.md`), one bank entry per literal. `fuente`: «<recurso>, <tema>,
<sección> — <sección de ejercicios> <número><letra>», so each entry can be traced back. Fix
what's wrong (typos, impossible intervals, mixed units, misplaced bars) and write what you
changed in `notas`; a `<!-- alt: … -->` next to a formula flags a possible typo. Don't
duplicate an exercise that's already in the bank: say which id covers it in the file's
docstring. Tell the teacher the list of corrections.

## Writing good checks

- **Compute the answer independently** from the statement's data; never just restate the
  expected answer. Compare exact objects: `solveset(...) == Interval(...)`,
  `Fraction`/`Rational`, `sp.simplify(a - b) == 0` for expressions, `sp.diff`, `sp.limit`.
- **Check that the statement is well posed:** domain and denominators, the intended kind of
  answer (integer, exact fraction), realistic magnitudes and **units**
  (`sympy.physics.units`, `convert_to`).
- **Selección múltiple:** assert the correct option and that every distractor is wrong.
  **Encuentra el error:** assert the claimed result is wrong and the corrected one right.
- **Worked examples** in the guía's theory can be checked the same way.
- Answers printed from SymPy: use `latex_es(expr)` (turns `\sin`, `\tan` into `\sen`, `\tg`);
  decimals go inside `\num{…}` in the document so they print with a comma.
