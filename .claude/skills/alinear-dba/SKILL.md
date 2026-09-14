---
name: alinear-dba
description: Finds the MEN Derechos Básicos de Aprendizaje (DBA) that apply to a course from the extracted files in dba/ (and the physics estándares), and reviews materials against them. Use when choosing DBA for a plan or material, filling the dba column of programacion.csv, writing the «% DBA:» comment, or when the teacher asks whether a guía, clase, quiz, taller or tarea complies with the DBA or wants feedback on it.
---

# Alineación con los DBA

Every material must comply with the MEN *Derechos Básicos de Aprendizaje* (DBA) of its grade.
The DBAs are already extracted in `dba/` — use those files, never quote a DBA from memory.

## Where to look

Grade folder name → two-digit number: `tercero`=03 … `octavo`=08, `noveno`=09, `decimo`=10, `undecimo`=11.

| Asignatura | DBA source | Coverage |
|---|---|---|
| `algebra`, `calculo`, `geometria`, `trigonometria` | `dba/matematicas/grados/gradoNN.tex` | grades 01–11, 9–12 DBAs each |
| `fisica` | `dba/naturales/grados/gradoNN.tex` **+** `dba/naturales/estandares-fisica.md` | DBA: grado 09 → DBA 1; grado 10 → DBA 1–2; grado 11 → DBA 1–3 (all the physics DBA there are; the rest of `naturales` is chemistry/biology). The MEN Estándares de Ciencias Naturales (2004, *entorno físico*) complement them by grade band: 9° uses 8°–9°, 10° and 11° share 10°–11°. Cite a DBA as the target of each class and use the estándares to split it into topics. |

**Scope — only the teacher's components.** Each subject covers only the DBA of its own
component: `geometria` → pensamiento espacial y métrico; `algebra`, `trigonometria`, `calculo`
→ numérico y variacional (the part matching the subject); `fisica` → the physics DBA of
Ciencias Naturales. DBA of **estadística y probabilidad** (every grade) and the **numeric DBA
of grades 3°–7°** belong to other subjects/teachers: don't plan them, and don't flag them as
uncovered in reviews.

DBAs are per **grade**, not per subject: `calculo` and `trigonometria` in the same grade share
`matematicas/gradoNN.tex`, so pick the DBAs whose content matches the topic.

## Fastest way to get the context

Cheapest first — stop as soon as you have enough:
1. List the grade's DBA statements: `grep -n '\\dba{' dba/matematicas/grados/grado11.tex` — one line per DBA, `\dba{N}{statement}`.
2. Read the chosen DBA in full from the same `.tex`: from its `\dba{N}` line up to the next `\dba{` (statement, `\evidencias` list, `\ejemplo`). This is the clean, paragraph-joined version; prefer it.
3. Figures appear as `\fig{stem}{description}`; the description is usually enough. Only open `dba/<area>/figs/<stem>.png` when the image itself matters. `figures.csv` indexes all figures by `grade,dba,kind,description`.
4. `dba/<area>/raw/grado_NN.txt` is the unedited extraction (`[[DBA N]]`, `[[FIG stem]]`, `%% page N` = page in the MEN PDF). Use it only to cite the original page or when the `.tex` looks garbled. `dba/naturales/raw/` contains **all** natural-science DBAs, not just physics.

## When generating material

- Take the DBA number(s) from the session's `dba` column in `programacion.csv`. If it's empty, propose the matching DBA(s) with their statements and ask the teacher to confirm before writing, then offer to fill the column.
- Record it in every `.tex` right under the data block: `% DBA: matematicas grado 11 · DBA 8 — Encuentra derivadas de funciones…`. In guías, the verified statement(s) also go in `dba` boxes in the Introducción.
- Activities target the DBA's **evidencias de aprendizaje**: each quiz/taller/tarea question maps to at least one evidencia, at the grade's level.
- Check the math of the DBA's own examples before reusing them: some are flawed (e.g. the athlete example of grado 11 DBA 5 — a quadratic distance gives a velocity that is maximal at the start).

## When the teacher asks for feedback or a review

Report concisely against the DBA:
- which evidencias the material covers (quote them briefly) and which of the class's DBA are left uncovered;
- content that belongs to another grade's DBA (too advanced/too basic) — check the neighbouring `gradoNN.tex` before claiming this;
- concrete suggestions (a question to add, an item to cut), ideally adapted from the DBA's own `Ejemplo`.

If no DBA of the grade fits the topic, say so and ask how to proceed — don't force a match.
