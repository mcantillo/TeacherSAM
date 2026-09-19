# Cómo trabajar con Claude (Code y Cowork) en este proyecto

Guía para María Mercedes Cantillo · Área de Matemáticas · Colegio San Alberto Magno

Claude Code trabaja directamente sobre la carpeta `mercedes`: lee y escribe los archivos, compila
los PDF y sigue las reglas que ya están guardadas en el proyecto (`CLAUDE.md` y los *skills* en
`.claude/`). No tienes que repetirle las reglas; basta con pedirle la tarea.

## 0. Si usas Claude Cowork (app de escritorio)

1. En la pestaña Cowork, selecciona la carpeta `Documentos/mercedes`.
2. En las instrucciones de la carpeta (o del proyecto) pega:
   «Antes de cualquier tarea, lee `INSTRUCCIONES-COWORK.md` y `CLAUDE.md` en la raíz de esta
   carpeta y síguelos.»
3. Pide las tareas igual que en esta guía; los ejemplos de las secciones siguientes sirven igual.

Qué cambia frente a Claude Code: Cowork trabaja en un entorno aislado en los servidores de
Anthropic, que puede no tener LaTeX instalado. Si no puede compilar, escribirá los archivos
`.tex` y te avisará que **falta compilarlos y revisarlos**; en ese caso ábrelos después con
Claude Code en tu Mac y pídele «compila y revisa los archivos de la semana X».

## 1. Empezar

1. Abre la app de Claude Code y elige la carpeta del proyecto: `Documentos/mercedes`.
2. Escribe lo que necesitas en español, como se lo pedirías a un colega.
3. Usa **una conversación por tarea grande** (por ejemplo, «la guía del trimestre II de Física
   10°»). Así Claude se concentra y carga solo las reglas de esa tarea.

## 2. Di siempre asignatura, grado y tema (o semana)

Claude **no adivina**: si falta alguno de estos datos, te preguntará antes de escribir.

- Bien: «Haz el quiz de la semana 5 de Cálculo 11°».
- Incompleto: «Haz un quiz de derivadas» → te preguntará de qué curso y de qué semana.

## 3. El orden de trabajo

Cada paso necesita el anterior. Si pides algo antes de tiempo, Claude te dirá qué falta.

| Paso | Qué es | Qué escribir (ejemplos) |
|---|---|---|
| 1. Programación del año | Un calendario de clases por curso (`programacion.csv`), hecho con tu horario | «Genera la programación del año» · «Llegó el calendario oficial del colegio: [fechas]. Actualízalo» |
| 2. Planeación del trimestre | Qué tema, qué DBA, y en qué sesiones hay quiz, taller y tarea | «Planeemos el trimestre I de Geometría 3°» · «Propón el plan anual de Física 10°» |
| 3. Guía del estudiante | Una guía por trimestre, con hilo conductor, marco teórico y temas | «Crea la guía del trimestre I de Geometría 3°» · «Revisa la guía de Cálculo 11° contra los recursos» |
| 4. Clase de la semana | Tu material de docente, sesión por sesión | «Haz los paquetes de las semanas 3 y 4 de Cálculo 11°» |
| 5. Evaluación | Quiz, taller y tarea donde el plan los marca; al final, la evaluación del periodo | «Haz el quiz de la semana 5 de Cálculo 11°» · «Genera la clave del taller de la semana 2» |

En cada paso Claude te muestra una propuesta y **espera tu aprobación** («aprobado», «cambia
el tema 3 por…») antes de seguir.

## 4. Preguntas rápidas

- «¿Qué tema toca el jueves 24 de septiembre en Cálculo 11°?»
- «¿Cuántas clases le quedan al trimestre I de Física 10°?»
- «¿Qué DBA de grado 8 corresponden a Geometría?»
- «¿Este taller cumple el DBA? Dame retroalimentación.»
- «¿Qué hay en los recursos sobre movimiento circular?»
- «Verifica este ejercicio: …» · «¿Qué ejercicios de inecuaciones hay en el banco?»

**Banco de ejercicios:** cada ejercicio se verifica con un programa una sola vez y queda
guardado en `recursos/banco/`; después se reutiliza en guías, quices y talleres sin volver a revisarlo.
Los ejercicios de «explica por qué…» no se pueden verificar con un programa: Claude te mostrará
la respuesta modelo para que la apruebes.

## 5. Revisar e imprimir

- Cada PDF queda junto a su archivo `.tex`, por ejemplo
  `materias/calculo/undecimo/clases/semana-02/quiz.pdf`.
- Las claves de respuestas son los archivos que terminan en `-clave.pdf`.
- Todo está diseñado para imprimir en **blanco y negro**.
- Para pedir cambios, sé concreta: «en el quiz de la semana 2, cambia la pregunta 3 por una de
  decimales» o «la clase del lunes es muy larga, recorta la explicación».
- Claude revisa cada PDF página por página antes de entregártelo, pero tu revisión final es la
  que cuenta.

## 6. Agregar recursos

Todo lo que pongas en `recursos/` se considera **revisado y aprobado** para usar en clase.

1. Guarda el archivo (PDF, Word, libro) en la carpeta del área: `recursos/matematicas/`,
   `recursos/fisica/`, etc.
2. Dile a Claude: «Agregué [nombre] a recursos, pásalo a texto».
3. Desde ese momento lo usará para sacar ideas de ejemplos y ejercicios, siempre adaptándolos y
   citando la fuente.

Si Claude encuentra un error en un recurso, te lo avisará: aprobado no significa infalible.

## 7. Dónde está cada cosa

| Carpeta o archivo | Contenido |
|---|---|
| `horario-2026-2027.md` | Tu horario semanal |
| `programacion-2026-2027.md` | Calendario escolar (trimestres, festivos, recesos) |
| `bitacora-2026-2027.md` | Tu bitácora: lo que de verdad se dictó cada semana en cada curso |
| `PENDIENTES.md` | Todo lo que falta: tus decisiones pendientes y el trabajo que espera por ellas |
| `CHANGELOG.md` | Lo que ya se hizo, por fecha |
| `materias/<asignatura>/<grado>/` | Todo el material de cada curso: plan, guías, clases, evaluaciones |
| `recursos/` | Material aprobado (guías de apoyo, libros) |
| `dba/` | Los Derechos Básicos de Aprendizaje del MEN, listos para consultar |
| `plantillas/` | Los formatos de quiz, taller, guía, etc. (no hace falta tocarlos) |
| `CLAUDE.md` y `.claude/` | Las instrucciones de Claude (si cambias una regla, pídele que las actualice) |

## 8. Qué pedirle ahora (cola de trabajo del 2026-09-19)

Esta lista se armó en Cowork, que no tiene LaTeX ni SymPy y por eso no puede compilar ni
verificar ejercicios. **Lo de abajo se pide en Claude Code, en tu computador**, donde sí compila
los PDF, los revisa y hace el commit y el push. Pide **una cosa por conversación**.

### 8.1 Urgente: los paquetes de la semana 04 (clases del 21 al 25 de septiembre)

Faltan 11. Van en orden de fecha; el día es cuando se dicta.

| Día | Qué pedir | Ojo |
|---|---|---|
| lun 21 | «Haz el paquete de la semana 04 de Física 9°» | Sesión 003: es el **segundo día de exposiciones** (3 y cierre). El `clase.tex` es el guion del día, sin taller |
| lun 21 | «Haz el paquete de la semana 04 de Geometría 10°» | Sesión 003, con tarea |
| lun 21 | «Haz el paquete de la semana 04 de Geometría 6°» | Sesión 003, con taller. Banco: 27 ejercicios |
| mar 22 | «Haz el paquete de la semana 04 de Álgebra 9°» | Sesiones 007 y 008 (mar y vie); taller y tarea el viernes |
| mar 22 | «Haz el paquete de la semana 04 de Geometría 7°» | Sesión 004, con taller. **El banco casi no tiene traslaciones: primero el 8.2** |
| mar 22 | «Haz el paquete de la semana 04 de Trigonometría 10°» | Sesiones 013–016: **cuatro sesiones**, el paquete más grande |
| mié 23 | «Haz el paquete de la semana 04 de Geometría 4°» | Sesión 004, con taller. **Banco casi vacío: primero el 8.2** |
| jue 24 | «Haz el paquete de la semana 04 de Física 10°» | Sesiones 007 y 008; taller el jueves y tarea el viernes |
| jue 24 | «Haz el paquete de la semana 04 de Geometría 9°» | Sesión 004, con tarea. Banco: 25 ejercicios |
| vie 25 | «Haz el paquete de la semana 04 de Geometría 3°» | Sesión 004, con taller. **Banco casi vacío: primero el 8.2** |
| vie 25 | «Haz el paquete de la semana 04 de Geometría 11°» | Sesión 004, con tarea. **El banco no tiene nada de coordenadas para 11°: primero el 8.2** |

### 8.2 Llenar el banco donde está vacío

Cinco cursos no tienen con qué armar un taller. Antes de su paquete, pide:

> «Escribe y verifica ejercicios de <tema> para <curso>, y agrégalos al banco.»

| Curso | Verificados hoy | Qué falta |
|---|---|---|
| Geometría 11° | **0** | coordenadas, distancia, punto medio, lugares geométricos |
| Geometría 3° | 4 | líneas rectas y curvas, abiertas y cerradas, figuras planas |
| Geometría 4° | 6 | paralelas y perpendiculares, polígonos, cuadriláteros |
| Geometría 7° | 7 | traslaciones, rotaciones, reflexiones, vistas |
| Geometría 10° y Trigonometría 10° | 12 | y los 9 de la guía de 10° **existen pero no están verificados** |

### 8.3 Después: rehacer las 11 guías con el proceso de tres etapas

Las que hay son el borrador de la generación rápida del 2026-09-14. Ahora que los planes están
aprobados, se rehacen con `crear-guia`. Orden sugerido, por lo que ya tiene banco:

1. Álgebra 9° (127 ejercicios) · 2. Física 10° y 9° (79) · 3. Geometría 6° (27) ·
4. Geometría 9° (25) · 5. Trigonometría 10° y Geometría 10° (12, y hay 9 por verificar) ·
6. Geometría 7°, 4°, 3° y 11°, después del 8.2

> «Rehaz la guía del trimestre I de <curso> con el proceso de tres etapas.»

### 8.4 La decisión que más aprieta

**El reparto de los irracionales entre Álgebra 8° y Álgebra 9°:** hoy los dos cursos trabajan el
mismo tema con los mismos ejercicios del banco (`irracionales-8`). Si no se decide, el trimestre
se repite entero. Las demás están en `PENDIENTES.md`.

## 9. Pendientes

Todo lo que falta está en **`PENDIENTES.md`**, en la raíz: primero tus decisiones (generales y
por curso), después el trabajo de Claude que espera por ellas. Márcalas ahí o díselas a Claude
(«aprueba el plan de Geometría 6° con el hilo del fútbol») y él actualiza la lista. Lo que ya
se hizo queda en `CHANGELOG.md`.

Si el colegio cambia el calendario, pásale las fechas nuevas a Claude («actualiza el calendario
con estas fechas»); recalculará todas las fechas sin perder lo planeado.

## 10. Consejos

- Revisa por tandas (por ejemplo, dos semanas de clases a la vez) antes de pedir más.
- Si una regla nueva debe valer siempre («a partir de ahora, los quices de 20 minutos»), dilo
  así; Claude la guardará en las instrucciones del proyecto.
- Si algo no te gusta de cómo trabaja Claude, díselo directamente: ajustará las instrucciones
  para la próxima vez.
