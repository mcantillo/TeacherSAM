# Plan anual 2026–2027 — Geometría 5°

Aprobado por la docente el 2026-09-14 (reparto por trimestre e hilo del trimestre I). El
detalle por sesión se hace en la planeación de cada periodo, en `programacion.csv`.

Trimestre I pasado al calendario oficial el 2026-09-14 (9 sesiones en vez de 10): las
sesiones 001–008 quedaron como estaban; la 009 (semana 12, la de evaluación) es la
evaluación del periodo, y se perdió la situación integradora con quiz. **Pendiente de
confirmar con la docente.**

## DBA de la asignatura

Fuente: `dba/matematicas/grados/grado05.tex`. Geometría 5° cubre el componente
espacial-métrico; el numérico-variacional (DBA 1–3, 8, 9) y la estadística y probabilidad
(DBA 10–12) son de otras asignaturas.

| DBA | Enunciado (resumido) | Asignatura |
|---|---|---|
| 1, 2, 3, 8, 9 | Naturales y fraccionarios, potenciación, variación y ecuaciones | otra asignatura |
| 4 | Relaciones entre superficie y volumen; elegir unidades, instrumentos y procedimientos | **Geometría** |
| 5 | Relaciones entre perímetro y área de diferentes figuras | **Geometría** |
| 6 | Propiedades de un cuerpo en términos de bidimensionalidad y tridimensionalidad; composición y descomposición de formas | **Geometría** |
| 7 | Describir y localizar posición y trayectoria de un objeto con referencia al plano cartesiano | **Geometría** |
| 10, 11, 12 | Estadística y probabilidad | otra asignatura |

## Reparto por trimestre

| Trimestre | Semanas | Sesiones | DBA | Contenido |
|---|---|---|---|---|
| I | 02–12 | 9 | 7 | Sistemas de referencia, puntos cardinales, plano cartesiano (ejes, cuadrantes, coordenadas) y trayectorias sobre mapas y planos. |
| II | 15–26 | 12 | 5 (y 4 parcial) | Figuras planas: perímetro, área, relación entre ambos (igual perímetro no implica igual área), medición por composición, recubrimiento y cálculo; unidades de superficie. |
| III | 27–35 | 8 | 6 y 4 | Bidimensionalidad y tridimensionalidad: cuerpos y sus desarrollos planos (plantillas), composición y descomposición de formas, volumen y relación superficie–volumen. |

Criterios del reparto:

- El trimestre I continúa lo que la docente ya había iniciado en la semana 02 (ubicación en el
  espacio, plano del salón), de modo que el DBA 7 queda como el aprendizaje de entrada.
- El DBA 5 va en el II porque el trabajo con área y perímetro se apoya en las operaciones y
  fraccionarios que el estudiante trabaja en Matemáticas durante ese mismo periodo.
- Los DBA 6 y 4 cierran el año: el volumen y la relación superficie–volumen suponen resueltos
  el área de figuras planas y la composición/descomposición trabajadas en el II.

## Ritmo de evaluación

Aprobado el 2026-09-14. Una sola sesión semanal: lunes, 55 min (hora 1, 6:55).

- **Taller** o **tarea** alternados casi cada semana (una sesión de 55 min no alcanza para
  explicar y evaluar el mismo día).
- **Quiz** en la semana que cierra un bloque de subtemas (coordenadas en el plano, y el repaso
  final del periodo).
- La **última semana del trimestre** es de evaluación del periodo: sin taller ni quiz nuevo.
- La sesión 001 (semana 02) ya se dictó antes de esta planeación —introducción a la ubicación
  en el espacio: dibujar el plano del salón con la posición propia y la del profesor, según la
  bitácora de la docente—: queda registrada sin DBA por ser una introducción, no una evidencia
  del DBA todavía.

## Carga real del curso

Casi todos los festivos caen en lunes, y el receso de octubre y la Semana Santa también se
llevan un lunes cada uno. Con el calendario oficial, Geometría 5° queda con **29 sesiones en
el año** (9 + 12 + 8): es el curso más golpeado del horario. El reparto se dimensionó para 32
(calendario provisional); el trimestre III, que bajó de 10 a 8 sesiones, hay que revisarlo al
planearlo.

## Hilos conductores

| Trimestre | Hilo | Estado |
|---|---|---|
| I | Cali, mi ciudad: orientar a una visitante con planos, coordenadas y rutas (el propio ejemplo del DBA 7) | aprobado · en uso en la guía del trimestre I |
| II | por definir | — |
| III | por definir | — |

Contextos y registro del grado según `.claude/referencias/registro-grados.md` (5°: vocabulario
matemático formal introducido y explicado, procedimientos completos, problemas de varios
pasos; contextos de ciudad, viajes, naturaleza y pesos colombianos; sin diminutivos ni
mascotas).

## Estado de la planeación

El **trimestre I está planeado sesión por sesión** en `programacion.csv` (clases 001–009, DBA 7);
la clase 001 quedó registrada con lo que se dictó, según la bitácora de la docente
(`bitacora-2026-2027.md`).

La **guía del estudiante del trimestre I** está escrita:
`guia-didactica/guia-periodo-I-ubicacion.tex`, con cuatro temas (`tema:referencia`,
`tema:plano`, `tema:trayectorias`, `tema:mapas`). Compilada el 2026-09-14 (11 páginas, sin
errores de `revisar_guia.py`); falta la revisión página por página de la docente.

El paquete de la **semana 03** (clase + tarea) se construyó antes que la guía; el 2026-09-14
se enlazó a ella (`\guiadelestudiante{}` y `\refguia{tema:referencia}`). Faltan los paquetes
semanales desde la semana 04.

## Recursos principales

- `recursos/matematicas/Guías pedagógicas Matemáticas/05 - Modulo_Matematicas_Quinto.docx` y
  `Modulo_Matematicas_Geometria.docx` (texto en `texto/`): revisar qué traen sobre plano
  cartesiano, perímetro/área y cuerpos antes de adaptar ejercicios; verificar cada uno (los
  recursos tienen errores).
- `guias-anteriores/Malla_Curricular_Geometria_Grado5.docx` (texto en `texto/`): solo como
  fuente de ideas —sus campos «DBA:» no son oficiales—. Su Periodo I coincide con la ubicación
  espacial y sistemas de referencia que aquí van en el trimestre I.
