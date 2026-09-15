---
name: crear-guia
description: Crea o revisa la guía del estudiante trimestral (una por asignatura, grado y trimestre) de las clases de María Mercedes Cantillo, en tres etapas revisadas por la docente — plan en Markdown (DBA, hilo, marco teórico y referencias verificadas), ejercicios verificados del banco y documento LaTeX — con frase introductoria, temas con aplicación, ejercicios y resumen, y las secciones institucionales de evaluación. Use when the user asks for a «guía», «guía del estudiante», «guía trimestral» o «del periodo», to add or change temas of a guía, or to review a guía or contrast it with the material in recursos/.
---

# Crear una guía del estudiante

La guía es la referencia del estudiante para **todo un trimestre**: un `\tema` por cada tema
de las clases del periodo, y cada `clase.tex` la cita con `\refguia{tema:...}`. Este skill
tiene las reglas de la guía. Además usa: el skill `alinear-dba` (qué DBA y cómo citarlos), el
skill `verificar-ejercicios` (banco de ejercicios), `.claude/referencias/registro-grados.md`
(registro del grado) y `recursos/CLAUDE.md` (cómo usar los recursos).

## Antes de empezar: prerrequisitos

Si falta alguno, **detente**, di qué falta y ofrece hacerlo primero. No lo supongas.

- [ ] Asignatura, grado y trimestre claros (si no, pregunta).
- [ ] `curriculo/plan-anual.md` aprobado, con el reparto de los DBA por trimestre.
- [ ] Las filas del periodo en `curriculo/programacion.csv` tienen `tema`, `subtema` y `dba` aprobados.
- [ ] El **hilo conductor** del trimestre está aprobado. Si no, propón 2 o 3 opciones adecuadas al grado y pregunta.

## Tres etapas, cada una revisada por la docente

Todo vive en `materias/<a>/<g>/guia-didactica/`. Para guías cortas, la docente puede pedir
revisar las etapas A y B juntas.

### Etapa A — Plan en Markdown, sin ejercicios → `guia-periodo-<P>-<slug>.plan.md`

1. **Reunir contexto:** plan anual; las filas del periodo (los valores distintos de `tema`, en
   orden, son los `\tema`); los DBA de esas filas con su texto literal y sus evidencias (skill
   `alinear-dba`); el registro del grado; la guía del trimestre anterior (continuidad del hilo).
2. **Buscar en `recursos/`** antes de inventar (`grep -ril "<tema>" recursos/*/*/texto/`).
3. **Escribir el plan** con estas secciones: datos (asignatura, grado, trimestre, hilo); DBA y
   evidencias, con el tema que atiende cada evidencia; frase introductoria; marco teórico
   **redactado**, con sus citas; y, por cada tema: título y `\label`, paso del hilo,
   explicación (definiciones, ideas clave, ejemplos resueltos), aplicación real, recursos
   usados y **ejercicios planeados** — solo su intención (evidencia que evalúan, tipo,
   dificultad), sin enunciados. Cierra con el cierre del hilo y la tabla de referencias.
4. **Verificar referencias y citas** aquí, antes de cualquier LaTeX (ver [REFERENCE.md](REFERENCE.md),
   «Verificación de referencias»): cada obra y cada cita textual se confirma en internet; lo
   que no se confirma se quita o se parafrasea. En el plan, tabla: referencia · veredicto · URL.

→ **Revisión 1:** la docente aprueba estructura, teoría, hilo y fuentes.

### Etapa B — Ejercicios verificados (skill `verificar-ejercicios`)

1. Para cada ejercicio planeado, busca primero en el banco uno ya verificado que sirva
   (`python3 tools/ejercicios.py listar --tema … --grado …`, y también temas y grados vecinos);
   reutilízalo tal cual. **El banco es para ahorrar tiempo:** si un ejercicio aprobado cumple
   la intención del plan, ajusta el plan a él en vez de escribir uno nuevo.
2. **La guía no crea ejercicios nuevos: usa solo los del banco.** Si una evidencia del DBA no
   tiene ningún ejercicio verificado, no lo inventes: anótalo en el plan como pendiente para la
   docente, y escríbelo solo si ella (o el usuario) lo pide expresamente. **Excepción:** si el
   banco no tiene nada para ese grado o tema (p. ej. Geometría 3°–4°), la guía puede traer unos
   pocos ejercicios nuevos, los mínimos, verificados y marcados como nuevos en el plan. Lo mismo para los
   ejemplos resueltos del marco teórico: primero el banco. Ver «Reuse, don't multiply» en el
   skill `verificar-ejercicios`.
3. Anota en el plan, por tema, los ids de los ejercicios, su estado, cuáles son reusados y, para
   cada nuevo, por qué hizo falta.

→ **Revisión 2:** la docente aprueba los ejercicios (tabla id · enunciado · respuesta · estado)
y las respuestas modelo de los manuales (`python3 tools/ejercicios.py aprobar <id>`).

### Etapa C — Documento LaTeX

1. Copia `plantillas/guia-trimestral/guia-trimestral.tex` a
   `guia-periodo-<P>-<slug>.tex`, fija el `\input@path` (`{{../../../../plantillas/estilo/}}`),
   llena el bloque de datos y el comentario `% DBA: …`.
2. Escribe en el orden obligatorio (ver [REFERENCE.md](REFERENCE.md)) pasando el plan aprobado a
   los macros: frase; introducción con cajas `dba`; marco teórico con `cita`; un `\tema` por
   tema (hilo → explicación → aplicación → ejercicios → resumen); «Prepárate para Saber 11»
   solo en 9°–11°; cierre; `\matrizevaluacion`, `\autoevaluacion`, `\seguimientodocente`;
   referencias con su `% verificado:`.
3. Los ejercicios salen del banco (`python3 tools/ejercicios.py mostrar <id>`): `% Ejercicio: <id>`
   encima de cada `\pregunta`. Solo entran los de estado `verificado` o `manual-aprobado`.
4. `python3 .claude/skills/crear-guia/scripts/revisar_guia.py <archivo>.tex` revisa la
   estructura y las referencias (no necesita LaTeX). Si hay LaTeX (`command -v latexmk`),
   repítelo con `--compilar` hasta que no haya errores; luego `pdftoppm -png -r 70` y **mira
   cada página**; corrige con [EXAMPLES.md](EXAMPLES.md). Sin LaTeX (p. ej. en Cowork), di que
   la guía **no se compiló ni se revisó visualmente** (ver `INSTRUCCIONES-COWORK.md`).
   **Nunca borres el `.aux`** de la guía.

→ **Revisión 3:** la docente revisa el PDF.

**Entregar:** resumen del contenido y las fuentes, errores encontrados en los recursos,
respuestas de «Prepárate para Saber 11»; actualizar la tabla de hilos de `plan-anual.md` y la
línea de estado de `CLAUDE.md`; si cambió un `\label`, recompilar las clases que lo citan.

## Reglas que no se negocian

- Toda referencia y toda cita lleva su `% verificado:` con una URL real; sin evidencia, se quita.
- Nunca inventes una cita, una fecha o una fuente. El texto de los DBA va literal desde `dba/`.
- Ningún ejercicio entra a la guía sin estar verificado (o aprobado, si es manual) en el banco.
- Solo entran los temas del plan aprobado; un tema nuevo o cambiado se consulta primero.
- Cada `\tema` lleva `\label{tema:<slug>}`; una vez citada por las clases, la etiqueta no cambia.
- Blanco y negro (curvas por tipo de trazo, `\addplot+`). Sin notas para el docente en la guía.
