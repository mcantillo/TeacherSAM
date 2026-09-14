# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

> ⚠️ **PENDIENTE — calendario provisional.** The trimester dates, recesos and evaluation weeks in `programacion-2026-2027.md` are a **provisional draft**, not the official Colegio San Alberto Magno calendar. Remind the teacher whenever you work with dates. When she provides the official calendar, follow «Calendario oficial» in the `planeacion` skill, then delete this notice.

## What this is

Teaching materials for María Mercedes Cantillo, math/physics teacher at Colegio San Alberto Magno (Cali, Colombia). Almost everything is LaTeX; all student-facing content is in **Spanish** and printed in **black & white**. Not a git repository.

It's used from **Claude Code** (the teacher's Mac: LaTeX, poppler and a Python `.venv/` with SymPy installed) and from **Claude Cowork** in the Claude app (a remote sandbox where those tools may be missing). **Every instruction must work in both:** check a tool with `command -v` before relying on it, use relative paths and `python3`, and when something is missing follow `INSTRUCCIONES-COWORK.md` — never assume the Mac. When you add or change instructions, give them the same fallback.

| Path | What | Details |
|---|---|---|
| `materias/<asignatura>/<grado>/` | all class material, in the scheme below | this file + skills |
| `horario-2026-2027.md`, `programacion-2026-2027.md` | weekly schedule; school calendar | skill `planeacion` |
| `tools/programacion.py` | generates every course's `programacion.csv` | skill `planeacion` |
| `dba/` | MEN *Derechos Básicos de Aprendizaje* extracted to LaTeX/text, plus physics estándares | skill `alinear-dba`; extraction pipeline in `dba/CLAUDE.md` |
| `recursos/` | material the teacher reviewed and approved (guides, e-books, internet resources) | `recursos/CLAUDE.md` |
| `plantillas/` | LaTeX templates and the shared style `estilo/mmcantillo.sty` | `plantillas/CLAUDE.md` (style internals); the skills say which template to use |
| `guias-anteriores/` | previous-year Word guías and mallas (Geometría 4°–6°), plain text in `texto/` | reference only — their «DBA:» fields are **not** official |
| `GUIA-CLAUDE-CODE.md` | the teacher's guide (in Spanish) to working with Claude Code and Cowork here | keep it in sync when the workflow, skills or pending items change |
| `INSTRUCCIONES-COWORK.md` | start-here file for Claude Cowork (desktop), which may not load skills or folder `CLAUDE.md` files by itself and runs commands in a remote sandbox | keep its task → file table in sync with the skills |
| `recursos/banco/`, `tools/ejercicios.py` | bank of exercises verified with Python + SymPy (each one checked once, then reused); state in `recursos/banco/verificados.json`; dependencies in `tools/requirements.txt` → `.venv/` | skill `verificar-ejercicios` |
| `tools/docx_a_markdown.py` | portable `.docx` → Markdown in `markdown/`, formulas as LaTeX (decodes Equation 3.0/MTEF and OMML; flags formulas whose alt text disagrees) — how the recursos are read | `recursos/CLAUDE.md` |
| `tools/docx_a_texto.py` | portable `.docx` → text; marks each embedded Equation 3.0 formula as «[ecuación]» (`textutil` is macOS-only and drops them silently) | `recursos/CLAUDE.md` |
| root `*.tex` | old documents with their own ad-hoc preamble | — |

## Which skill for which task

Load the skill before starting: it holds the rules for that task, so you don't need the others. (In Cowork, skills don't load by themselves: read `.claude/skills/<name>/SKILL.md` — see `INSTRUCCIONES-COWORK.md`.)

| Task | Skill |
|---|---|
| Horario, calendar, `programacion.csv`, `plan-anual.md`, planning a trimester (which tema/DBA/quiz goes when), «what's on date X» | `planeacion` |
| Guía del estudiante (one per trimester): create, extend, review, contrast with recursos | `crear-guia` |
| Weekly class pack (`clase`, `quiz`, `taller`, `tarea`, `material-de-estudiante`) and period exams | `crear-material` |
| Which DBA applies; checking or reviewing any material against the DBA | `alinear-dba` |
| Writing, reusing or checking exercises and answers; the exercise bank (`recursos/banco/`) | `verificar-ejercicios` |

Shared reference used by `crear-guia` and `crear-material`: `.claude/referencias/registro-grados.md` (tone, stories and contexts by grade, 3° to 6°).

## Ask, never assume

Before generating or filing any material you must know **asignatura**, **grado** and **tema** (and, for a class pack, which week of `programacion.csv` it belongs to). If any of these is not stated explicitly by the user or unambiguous from `programacion.csv`, **ask** — do not infer them from the topic, from earlier material, or from what "seems likely" (e.g. "derivadas" could be cálculo undécimo or física). Also ask before:
- creating a new `<asignatura>` or `<grado>` folder that doesn't exist yet;
- adding or changing a row in `programacion.csv` (dates and topics are the teacher's decision);
- overwriting a file that already exists in a pack.

## Order of work

1. **Year program** — every course's `curriculo/programacion.csv`, once per year (`planeacion`).
2. **Period planning** — `plan-anual.md` and the trimester's rows (tema, subtema, dba, quiz/taller/tarea), approved by the teacher (`planeacion`).
3. **Guía del estudiante** of the trimester (`crear-guia`).
4. **`clase.tex`** of each week (`crear-material`).
5. **quiz / taller / tarea** where the plan marks them; the period exam last (`crear-material`).

Only step 1 covers the whole year; steps 2–5 go **period by period**. **Don't skip ahead:** if asked for a later step whose prerequisite is missing (a quiz for a week that isn't planned, a `clase.tex` whose trimester has no guía, a guía without an approved plan), say what's missing and offer to do it first; if the teacher still wants to go ahead, do it and note what's pending.

**Current status (2026-09-12):** the 16 `programacion.csv` are generated (planning columns empty). The **pilot** for steps 2–5 (trimestre I from session 001) is **`calculo/undecimo`**: its `plan-anual.md`, its trimestre I plan (rows 001–036) and its trimestre I guía are done; the weekly packs go in **batches of two weeks**, each batch reviewed before the next — weeks 01–02 are done (clase, taller, tarea, and the quiz of week 02, with answer keys) and await the teacher's review; next: weeks 03–04. The other courses wait until the teacher has reviewed the pilot. **Exercise bank:** the «Practica lo aprendido» of Temas 1–2 of the 11° math module (desigualdades, intervalos, inecuaciones, valor absoluto) and its «Prepárate para el ICFES» (`saber11-desigualdades.py`; the lámparas problem was left out, pending the teacher) are in `recursos/banco/matematicas/`, plus 15 released ICFES questions copied verbatim (`icfes-cuadernillo-2026.py`, from `recursos/matematicas/icfes/`); open-ended ones await the teacher's approval. On 2026-09-13 eight parallel agents filled the bank for every course from its recursos (only the parts matching each course's asignatura and DBA): ~3 040 verified exercises and ~950 open-ended ones awaiting the teacher's approval (physics has most of them). The full checklist to trust the bank is `recursos/banco/PENDIENTES.md`. Pending teacher decisions include: which grade keeps the Geometría-module temas that landed in two grades (triángulos and ángulos 6°/8°, Pitágoras problems 9°/11°); physics temas with no DBA (`dba=[]`: ondas, luz, calor in 9°; mediciones, fluidos, termodinámica in 10°); Geometría 3°–4° and 10° (cónicas) have no recurso; the Álgebra 8° Tema 4 formulas were transcribed from images in the `.docx` and need a sample review. Update this line as the rollout advances.

## Layout of `materias/`

Every piece of class material ends up in its place in this scheme — never in the repo root or in `plantillas/`. Create missing pieces of the scheme when working in a grade.

```
materias/<asignatura>/<grado>/
├── curriculo/
│   ├── plan-anual.md           the subject's DBA distributed across the 3 trimestres (teacher-approved)
│   └── programacion.csv        one row per session of the year: date, tema, dba, quiz/taller/tarea
├── guia-didactica/
│   └── guia-periodo-<I|II|III>-<tema>.tex   one student guide per trimestre
├── evaluaciones/
│   └── periodo-<I|II|III>-<tema>.tex        period exams
└── clases/
    └── semana-NN/              one pack per school week (NN = `semana` in programacion.csv)
        ├── clase.tex           always
        ├── quiz.tex · taller.tex · tarea.tex   only where the plan marks them
        └── material-de-estudiante.tex          optional extra
```

- Names: lowercase, no accents, no spaces, words joined with `-` (`calculo`, `undecimo`, `semana-07`).
- Asignaturas: `algebra`, `calculo`, `fisica`, `geometria`, `trigonometria`. Grades spelled out: `tercero` … `undecimo`.
- The school year has **three trimestres**: `I`, `II`, `III`.
- Compiled PDFs live next to their `.tex`; run `latexmk -c` afterwards — **except in `guia-didactica/`**, whose `.aux` must stay because the classes read it.
