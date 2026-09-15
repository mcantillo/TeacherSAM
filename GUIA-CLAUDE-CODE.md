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
| `materias/<asignatura>/<grado>/` | Todo el material de cada curso: plan, guías, clases, evaluaciones |
| `recursos/` | Material aprobado (guías de apoyo, libros) |
| `dba/` | Los Derechos Básicos de Aprendizaje del MEN, listos para consultar |
| `plantillas/` | Los formatos de quiz, taller, guía, etc. (no hace falta tocarlos) |
| `CLAUDE.md` y `.claude/` | Las instrucciones de Claude (si cambias una regla, pídele que las actualice) |

## 8. Pendientes

- **Calendario:** el calendario oficial está en `programacion-2026-2027.md` desde el 2026-09-14.
  Si el colegio lo cambia, pásale las fechas nuevas a Claude («actualiza el calendario con estas
  fechas»); recalculará todas las fechas sin perder lo planeado.
- **Rangos del SIEE:** la escala 1,0–5,0 y los rangos de desempeño (Bajo, Básico, Alto,
  Superior) están pendientes de confirmar con el SIEE del colegio.
- **Piloto:** Cálculo 11° es el curso piloto. Los demás cursos se planean cuando apruebes cómo
  quedó el piloto. Según tu bitácora, en las semanas 01–02 de Cálculo 11° se hizo diagnóstico
  y refuerzo de factorización: falta decidir dónde se recuperan los subtemas de «Los sistemas
  numéricos» que estaban planeados ahí.
- **Material adelantado por revisar:** Álgebra 8°, Geometría 8°, Geometría 5° y Física 11° ya
  tienen plan anual y plan del trimestre I (el de Física 11°, solo propuesto); Álgebra 8°,
  Geometría 5° y Física 11° tienen además guía del trimestre I, y Álgebra 8° y Geometría 5° el
  paquete de la semana 03. Se hicieron con el calendario provisional: al pasarlos al oficial,
  la semana 13 que ya no existe se juntó con la semana 12 (repaso y evaluación), y en Física 11°
  se perdió el quiz de campo eléctrico. Revisa y confirma. Además, los hilos de los trimestres
  II y III de Cálculo 11° y Física 11° («Las leyes que se ven en una gráfica», «Faraday no sabía
  matemáticas») están propuestos, no aprobados.

## 9. Consejos

- Revisa por tandas (por ejemplo, dos semanas de clases a la vez) antes de pedir más.
- Si una regla nueva debe valer siempre («a partir de ahora, los quices de 20 minutos»), dilo
  así; Claude la guardará en las instrucciones del proyecto.
- Si algo no te gusta de cómo trabaja Claude, díselo directamente: ajustará las instrucciones
  para la próxima vez.
