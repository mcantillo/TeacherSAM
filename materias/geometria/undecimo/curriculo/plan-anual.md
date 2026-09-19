# Plan anual 2026–2027 — Geometría 11°

Aprobado por la docente el 2026-09-18: el reparto por trimestre, el ritmo de evaluación
y el hilo del trimestre I (opción **A**, «LORAN: encontrar un barco con dos hipérbolas»). El trimestre I ya está escrito
sesión a sesión en `programacion.csv` (se llenó el 2026-09-17). Quedan abiertas las
preguntas de este plan, que la docente responde una por una; ver `PENDIENTES.md`.

**Decisión del 2026-09-19:** **sí se usan las preguntas ICFES 15, 37 y 41** del cuadernillo
liberado (`recursos/matematicas/icfes/`, banco `icfes-cuadernillo-2026`) dentro de la guía del
trimestre I, con su formato original de Saber 11 y citando la fuente.

## DBA de la asignatura

Fuente: `dba/matematicas/grados/grado11.tex`. Según el reparto aprobado en Cálculo 11°
(`materias/calculo/undecimo/curriculo/plan-anual.md`), Geometría 11° tiene los DBA 4 y 6; los
demás son de Cálculo (1, 2, 3, 5, 7, 8) o de estadística (9, 10).

| DBA | Enunciado (textual) |
|---|---|
| 4 | «Interpreta y diseña técnicas para hacer mediciones con niveles crecientes de precisión (uso de diferentes instrumentos para la misma medición, revisión de escalas y rangos de medida, estimaciones, verificaciones a través de mediciones indirectas).» |
| 6 | «Modela objetos geométricos en diversos sistemas de coordenadas (cartesiano, polar, esférico) y realiza comparaciones y toma decisiones con respecto a los modelos.» |

## Criterio: Saber 11

La prueba Saber 11 de calendario B está prevista, de forma **tentativa**, para el **domingo 14 de
marzo de 2027** (ver el plan de Cálculo 11°: fecha estimada, aún sin calendario oficial del
Icfes). Cae al final del trimestre II, antes de su semana de evaluación (semana 26). La *Guía de
orientación Saber 11.º 2026* incluye en geometría: triángulos, círculos, esferas,
paralelepípedos y cilindros y sus medidas; sistemas de coordenadas cartesianas; congruencia y
semejanza; teoremas de Pitágoras y Tales; **coordenadas polares y tridimensionales**. Por eso
todo lo que evalúa la prueba (coordenadas cartesianas, polares y tridimensionales; medición de
longitudes, áreas y volúmenes) queda en los trimestres I y II, y el trimestre III profundiza
después de la prueba.

## Reparto por trimestre (propuesto)

Una sesión semanal: viernes 13:00, 40 min (hora 7). Conteo de sesiones hecho con un lector CSV
sobre `programacion.csv`.

| Trimestre | Semanas | Sesiones | DBA | Contenido |
|---|---|---|---|---|
| I | 01–12 (001–012) | 12 | 6, 4 | Coordenadas cartesianas como modelo: distancia y punto medio, lugares geométricos (circunferencia, mediatriz, hipérbola) y navegación hiperbólica (LORAN); precisión de una posición medida. |
| II | 13–26 (013–025) | 13 | 4, 6 | Medición con precisión creciente: precisión y exactitud, mediciones indirectas (semejanza, Pitágoras, razones trigonométricas), áreas y volúmenes (prismas, cilindros, esferas); coordenadas polares y tridimensionales. Sesiones 022–024 (semanas 23–25): repaso Saber 11 con preguntas liberadas del Icfes. |
| III | 27–37 (026–036) | 11 | 6, 4 | Coordenadas esféricas: latitud y longitud, distancias sobre la Tierra, del LORAN al GPS; curvas en coordenadas polares (espirales y rosas del ejemplo del DBA 6); comparar modelos. |

Semana 16 no existe (vacaciones); la semana 12 del trimestre I, la 26 del II y la 37 del III
son las de evaluación del periodo.

## Ritmo de evaluación (propuesto)

- **Tarea** y **taller** alternados cada semana (una sola sesión de 40 min).
- **Quiz** corto (~15 min) al cerrar un bloque: coordenadas y circunferencia (sesión 006) e
  hipérbola y navegación (sesión 011).
- **Semana de evaluación** (última del trimestre): evaluación del periodo, sin taller, quiz ni
  tarea nueva.

## Hilos conductores del trimestre I (elegir uno)

| Opción | Hilo | Hechos verificados (2026-09-14) / por verificar |
|---|---|---|
| **A (recomendada)** | **LORAN: encontrar un barco con dos hipérbolas.** Continúa la investigación que la docente dejó en la semana 02. Dos estaciones emiten pulsos sincronizados; el receptor mide la diferencia de tiempos, que da la diferencia de distancias: el barco está sobre una hipérbola cuyos focos son las estaciones. Un segundo par da otra hipérbola; el cruce es la posición. | **Verificados** (ETHW «Milestones: Loran, 1940–1946»; Federal Register y DVIDS 2010; Wikipedia «Gee»): Alfred Loomis propuso el sistema hiperbólico el 1 de octubre de 1940; el proyecto pasó al MIT Radiation Laboratory en 1941; primer par permanente en junio de 1942 (Montauk Point–Fenwick Island); operativo a comienzos de 1943; se inspiró en el Gee británico de Robert Dippy (RAF, 1942), que viajó a EE. UU. a ayudar; EE. UU. apagó LORAN-C el 8 de febrero de 2010. **Por verificar:** cifras de alcance y precisión de cada versión. |
| B | **Del libro de Apolonio al GPS**: Apolonio de Perga nombra la hipérbola (*Cónicas*, s. III a. C.); Descartes y Fermat la ponen en coordenadas (siglo XVII); LORAN la usa para navegar; el GPS cambia hipérbolas por esferas. | **Sin verificar:** fechas y atribuciones exactas (Apolonio, *La Géométrie* de 1637). Sirve también como hilo de todo el año (el III llega al GPS). |
| C | **Medir los Andes: la Misión Geodésica (1735–1744)**: Godin, Bouguer, La Condamine, Jorge Juan y Antonio de Ulloa triangulan entre Quito y Cuenca para decidir la forma de la Tierra. | **Verificados** (encyclopedia.pub / HandWiki «French Geodesic Mission»): fechas, integrantes, arco Quito–Cuenca y resultado (Tierra achatada). Encaja mejor con el DBA 4 (trimestre II) que con el I. |

## Propuesta del trimestre I, sesión por sesión

| Clase | Fecha | Sem. | Tema | Subtema | DBA | Quiz | Taller | Tarea |
|---|---|---|---|---|---|---|---|---|
| 001 | 2026-09-04 | 01 | Actividades de inicio de año | Actividades rompehielo y dinámicas de grupo *(dictada; según la bitácora)* | | | | |
| 002 | 2026-09-11 | 02 | Investigación: la hipérbola y LORAN | Pregunta problematizadora sobre la hipérbola y la triangulación de LORAN *(dictada; según la bitácora)* | | | | |
| 003 | 2026-09-18 | 03 | Coordenadas cartesianas | Socialización de la investigación; ubicar estaciones y barcos en el plano; distancia entre dos puntos | 6 | | | x |
| 004 | 2026-09-25 | 04 | Coordenadas cartesianas | Punto medio y distancia; comparar el mismo mapa con dos orígenes distintos | 6 | | x | |
| 005 | 2026-10-02 | 05 | Lugares geométricos | Circunferencia: puntos a igual distancia de una estación; ecuación $(x-h)^2+(y-k)^2=r^2$ | 6 | | | x |
| 006 | 2026-10-09 | 06 | Lugares geométricos | Quiz de coordenadas y circunferencia; mediatriz: puntos a igual distancia de dos estaciones | 6 | x | | |
| 007 | 2026-10-23 | 07 | La hipérbola | Lugar geométrico: diferencia de distancias constante; construcción con hilo o GeoGebra | 6 | | | x |
| 008 | 2026-10-30 | 08 | La hipérbola | Ecuación canónica con centro en el origen: focos, vértices, asíntotas ($c^2=a^2+b^2$) | 6 | | x | |
| 009 | 2026-11-06 | 09 | Navegación hiperbólica | Diferencia de tiempos × rapidez de la señal = diferencia de distancias; líneas de posición | 6; 4 | | | x |
| 010 | 2026-11-13 | 10 | Navegación hiperbólica | Cruce de dos hipérbolas: la posición; precisión (1 µs de error ≈ 300 m de diferencia de distancias) | 4; 6 | | x | |
| 011 | 2026-11-20 | 11 | Repaso | Quiz de hipérbola y navegación; pregunta 32 del cuadernillo Saber 11 (figuras en el plano cartesiano) | 6; 4 | x | | |
| 012 | 2026-11-27 | 12 | Evaluación del periodo | Evaluación del trimestre I | 6; 4 | | | |

## Recursos principales

- **No hay recurso de cónicas ni de coordenadas polares o esféricas** en `recursos/` (el módulo de
  11° es de desigualdades, valor absoluto y funciones; el de Geometría es de geometría básica).
  La hipérbola del trimestre I necesitará ejercicios nuevos, verificados con SymPy.
- `recursos/matematicas/Guías pedagógicas Matemáticas/markdown/Modulo_Matematicas_Geometria.md`:
  Tema 3 (Pitágoras) y Tema 4 (perímetros y áreas, triangulación de polígonos) para la medición
  del trimestre II.
- `recursos/matematicas/icfes/`: cuadernillo Saber 11.º 2026 y guía de orientación.
- Banco: `recursos/banco/matematicas/medicion-11.py` (11 verificados, 1 pendiente; DBA 4 y 6) e
  `icfes-cuadernillo-2026-geometria.py` (preguntas textuales del Icfes de geometría y medición;
  la 32 es de coordenadas cartesianas).

## Pendientes para la docente

1. **Cónicas en 10° y 11°:** la hipérbola es del DBA 5 de 10° («expresiones simbólicas de las
   cónicas»), y Geometría 10° tiene las cónicas en su programa. ¿Se da la hipérbola completa en
   11° (lo que sugiere la investigación de LORAN) o se supone vista en 10° y 11° solo la usa?
2. **Pitágoras 9° / 11°** (`recursos/banco/PENDIENTES.md`): `pitagoras-9-002…005` y
   `medicion-11-008…011` son los mismos problemas. Decidir en qué grado se quedan.
3. Preguntas 15, 37 y 41 de `icfes-cuadernillo-2026-geometria.py` (no encajan en los DBA 4 ni 6):
   ¿se usan como práctica Saber 11 en el repaso del trimestre II?
4. Confirmar que la sesión 001 fue de actividades de inicio (la bitácora lo dice para todos los
   cursos) y cuándo se socializa la investigación de LORAN (esta propuesta: sesión 003).
5. Aprobar el reparto, el ritmo de evaluación y el hilo del trimestre I.
