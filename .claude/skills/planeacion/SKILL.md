---
name: planeacion
description: Plans the school year of María Mercedes Cantillo's courses — reads the weekly horario and the school calendar, generates and edits each course's curriculo/programacion.csv with tools/programacion.py, writes curriculo/plan-anual.md and the trimester plan (tema, subtema, DBA, quiz/taller/tarea per session). Use when the user asks about the horario, calendario, fechas, festivos, programación, plan anual, planeación del trimestre o periodo, what class or topic falls on a date, or updating the calendar.
---

# Planeación del año y del trimestre

Covers steps 1–2 of the order of work in `CLAUDE.md`. Step 1 (year program) needs nothing
else. Step 2 (period planning) also needs the DBA: load the `alinear-dba` skill there.

## Sources

- `horario-2026-2027.md` (repo root): the weekly schedule — source of truth for which courses exist and when they meet.
- `programacion-2026-2027.md`: the school calendar — trimester dates, weeks without classes and festivos on school days (**provisional**, see the notice in `CLAUDE.md`). Days listed there as festivos, recesos or vacations have no class rows.
- A course in the horario without a `materias/<asignatura>/<grado>/` folder (or a folder with no hours in the horario) is a question for the teacher, not something to fix silently.
## Step 1 — Year program (once per year)

`python3 tools/programacion.py --dry-run`, then without the flag. It generates every course's
`curriculo/programacion.csv` from horario × calendar: one row per session, numbered in order,
with dates, `semana` and `carpeta` filled and the planning columns (`tema`, `subtema`, `dba`,
`quiz`, `taller`, `tarea`) empty. Re-running it never erases planning (it keeps the planning
columns by class number and refuses to write a course if planned rows would be lost). Edit the
CSVs by hand only in the planning columns.

Period boundaries, festivos, evaluation weeks and breaks must come from the school calendar;
if they're missing, **ask** — you may propose the Colombian festivos for the teacher to
confirm, never apply them unconfirmed.

### Calendario oficial

When the teacher provides the official calendar: update the tables in
`programacion-2026-2027.md` (keep their headings and `YYYY-MM-DD` dates), run
`python3 tools/programacion.py --dry-run` and then without the flag, rename any
`clases/semana-NN` folders whose week number changed, and delete the «PENDIENTE» notices in
`CLAUDE.md` and in that file.

## `curriculo/programacion.csv`

UTF-8, comma-separated, one row per session, header exactly:

```
clase,fecha,dia,inicio,minutos,periodo,semana,tema,subtema,dba,quiz,taller,tarea,carpeta
001,2026-08-03,lunes,07:50,100,I,01,Derivadas,Definición de derivada,5,,x,x,clases/semana-01
```

- `dia`, `inicio` (HH:MM) and `minutos` come from the horario. Consecutive hours of the same course on the same day are **one session** (one row) with the minutes added up (e.g. 10° Física jueves H2–H3 → `07:50,100`); non-consecutive hours on the same day are separate rows (10° Trigonometría jueves H6 and H8). Hour 7 (1:00–1:40) lasts 40 min, hour 1 lasts 55, the rest 50.
- `fecha` is ISO `YYYY-MM-DD`; `periodo` is `I`–`III`; `dba` is the DBA number(s) for that grade (several separated by `;`), empty only if the teacher hasn't decided yet.
- `clase` numbers the course's sessions of the year in order, three digits (`001`…); a course with 4 sessions a week has ~150.
- `semana` is the school week of the year, `01`–`40`, counting only weeks with classes. All rows of a week share `carpeta` = `clases/semana-NN`.
- `quiz`, `taller`, `tarea`: `x` on the session where it's applied (quiz taken, taller worked, tarea assigned), empty otherwise. Decided in step 2 — never added on your own.
- The school year runs 2026-08-01 → 2027-06-30; flag dates outside it.
- This file is the source of truth for «which class is next / what topic is on date X».

## Step 2 — Period planning (start of each trimester)

1. **Plan anual** (once per year, before the first period): topics come from the **DBA** of the grade that belong to the subject's component (skill `alinear-dba`; there is no official plan de área, and `guias-anteriores/` is only a source of ideas). Propose how the year's DBA spread over the three trimestres, get the teacher's approval, and record it in `curriculo/plan-anual.md`, with the criteria used (e.g. Saber 11 dates) and a table of hilos conductores.
2. **The trimester's rows:** fill `tema`, `subtema` and `dba` for every session of the period; mark `quiz`/`taller`/`tarea` (e.g. a quiz when a tema closes, one tarea a week, no taller or quiz in the evaluation week). Present it as a week-by-week table and write it to the CSV only after approval.
3. Choose the DBA *evidencias* to be assessed and draft the matriz criteria: first what students must demonstrate, then how to get there.
4. Propose 2–3 *hilos conductores* suited to the grade (`.claude/referencias/registro-grados.md`) and let the teacher choose.
5. Look in `recursos/` for material on the planned temas (`recursos/CLAUDE.md`) and note what fits in `plan-anual.md`.

Rules:
- **Dates are provisional, so planning starts at session 001** in every course, as if nothing had been taught yet (teacher's decision, 2026-09-12): don't skip rows because their provisional date has passed. Once the official calendar is in place, a class whose real date passes without being planned is recorded with what was actually taught (ask the teacher, never infer it) and gets no pack.
- After approving a plan, update the «Current status» line in `CLAUDE.md`.
