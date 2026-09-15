# Instrucciones para Claude Cowork — empieza aquí

> **Para la docente:** en Cowork, selecciona esta carpeta y pega esto en sus instrucciones
> (de la carpeta o del proyecto):
>
> «Antes de cualquier tarea, lee `INSTRUCCIONES-COWORK.md` y `CLAUDE.md` en la raíz de esta
> carpeta y síguelos.»

Esta carpeta se trabaja a veces con **Claude Code** y a veces con **Claude Cowork**. Las reglas
están escritas una sola vez, en archivos del proyecto. Claude Code carga algunas de ellas solo;
en Cowork **tienes que leerlas tú** con tus herramientas de lectura de archivos. Este archivo te
dice cuáles leer y qué cambia en tu entorno.

## 1. Al empezar cada sesión

1. Lee `CLAUDE.md` completo: qué es el proyecto, la regla de preguntar en vez de suponer, el
   orden de trabajo, el esquema de carpetas y el **estado actual**. Los **pendientes** están en
   `PENDIENTES.md` y lo ya hecho en `CHANGELOG.md`: lee la parte de `PENDIENTES.md` del curso
   con el que vas a trabajar.
2. Identifica la tarea y lee **su** archivo de reglas antes de empezar. Lee solo lo que la tarea
   necesita:

| Tarea | Lee antes de empezar |
|---|---|
| Horario, calendario, `programacion.csv`, plan anual, planear un trimestre, «qué toca el día X» | `.claude/skills/planeacion/SKILL.md` |
| Guía del estudiante (crear, ampliar, revisar) | `.claude/skills/crear-guia/SKILL.md`, y `REFERENCE.md` y `EXAMPLES.md` de esa carpeta cuando el SKILL lo indique |
| Clase semanal, quiz, taller, tarea, evaluación del periodo, claves | `.claude/skills/crear-material/SKILL.md` |
| Qué DBA aplica; revisar o dar retroalimentación de un material | `.claude/skills/alinear-dba/SKILL.md` |
| Escribir, reutilizar o verificar ejercicios; el banco de ejercicios | `.claude/skills/verificar-ejercicios/SKILL.md` |
| Cualquier material de 3° a 6° | además `.claude/referencias/registro-grados.md` |
| Usar o agregar recursos | `recursos/CLAUDE.md` |
| Cambiar las plantillas o el estilo `mmcantillo.sty` | `plantillas/CLAUDE.md` |
| Regenerar los DBA desde los PDF del MEN | `dba/CLAUDE.md` |

3. Cuando esos archivos digan «carga el skill `X`» o «usa `X`», lee
   `.claude/skills/X/SKILL.md`.

## 2. Qué cambia en el entorno de Cowork

- **Tus comandos corren en un entorno aislado, no en el Mac de la docente.** Usa rutas
  relativas a la raíz de esta carpeta; nunca rutas como `/Users/...` (aparecen en algunos
  ejemplos de los archivos de reglas: tradúcelas a rutas relativas).
- **Antes de compilar, comprueba las herramientas:**
  `command -v python3 latexmk pdflatex pdfinfo pdftoppm pdftotext`.
- **Si no hay LaTeX:** puedes intentar instalarlo solo si el entorno lo permite y es rápido (se
  necesitan, entre otros, `newpx`, `pgfplots`, `tcolorbox`, `siunitx`, `tasks`, `xr-hyper` y
  `babel-spanish`). Si no se puede:
  - escribe o edita el `.tex` igual;
  - para guías, corre `python3 .claude/skills/crear-guia/scripts/revisar_guia.py <archivo.tex>`
    **sin** `--compilar` (revisa la estructura y las referencias sin LaTeX);
  - suma a mano los puntos de quices, talleres y evaluaciones (deben dar 5);
  - dile a la docente, con claridad, que **el PDF no se compiló ni se revisó** y que falta
    compilarlo en su Mac (con Claude Code o con `latexmk -pdf archivo.tex`).
- **Nunca digas que un PDF quedó bien si no lo compilaste y miraste sus páginas.** Sin
  `pdftoppm` no hay revisión visual: dilo.
- **Solo Python:** `tools/programacion.py` y `revisar_guia.py` (sin `--compilar`) funcionan en
  cualquier entorno con Python 3.
- **Leer recursos:** lee las copias en `markdown/` junto a cada `.docx` (fórmulas en LaTeX,
  ejercicios con su numeración). Para un `.docx` nuevo:
  `python3 tools/docx_a_markdown.py <archivo>.docx` (escribe en `markdown/`; solo biblioteca
  estándar, lee también las fórmulas de Equation 3.0) y `python3 tools/docx_a_texto.py
  <archivo>.docx` (texto plano en `texto/`, con «[ecuación]» en cada fórmula; `textutil` solo
  existe en macOS). Un `<!-- alt: … -->` junto a una fórmula señala que su texto alternativo
  no coincide: revísala. Para PDF, `pdftotext -layout` si está disponible.
- **Verificar ejercicios necesita SymPy.** El `.venv/` de la carpeta es del Mac y no sirve en
  tu entorno: instala con `python3 -m pip install -r tools/requirements.txt` y usa `python3`.
  Si no se puede instalar, los ejercicios nuevos quedan **sin verificar**: dilo y no los pongas
  en ningún documento. Los ya verificados del banco sí se pueden usar.
- **No borres** los `.aux` de `materias/*/*/guia-didactica/`: las clases los leen.

## 3. Lo esencial, por si solo lees esto

- Todo el material es en **español**, para imprimir en **blanco y negro**.
- Antes de crear o archivar material debes saber **asignatura, grado y tema** (o semana). Si
  falta algo, **pregunta**; no lo deduzcas.
- Orden de trabajo: programación del año → planeación del trimestre → guía → clase semanal →
  quiz/taller/tarea. No te saltes pasos sin avisar qué falta.
- La docente aprueba cada propuesta antes de que sigas.
- Todo lo que está en `recursos/` está aprobado; úsalo para ideas, adaptado y citado.
- Las citas y referencias se verifican en internet; nunca las inventes.

## 4. Guardar lo aprendido

Cowork puede guardar instrucciones o memoria propias, pero la fuente de verdad son **los
archivos de este proyecto**, que también usa Claude Code. Cuando la docente fije una regla
nueva o cambie algo del proceso:

- escríbela en `CLAUDE.md` (si vale para todo) o en el `SKILL.md` de la tarea;
- cuando se abra o se cierre un pendiente, actualiza `PENDIENTES.md`; cuando termines un
  trabajo, agrega una línea con la fecha a `CHANGELOG.md`; y cambia el párrafo «Current status»
  de `CLAUDE.md` solo cuando un curso pase a otro paso;
- si cambia la forma de trabajar, actualiza también `GUIA-CLAUDE-CODE.md` (la guía de la
  docente) y la tabla de la sección 1 de este archivo.
