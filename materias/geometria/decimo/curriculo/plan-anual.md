# Plan anual 2026–2027 — Geometría 10°

Aprobado por la docente el 2026-09-18: el reparto por trimestre, el ritmo de evaluación
y el hilo del trimestre I (opción **A**, «Ubicarse en la Tierra: de las coordenadas geográficas al plano cartesiano»). El trimestre I ya está escrito
sesión a sesión en `programacion.csv` (se llenó el 2026-09-17). Quedan abiertas las
preguntas de este plan, que la docente responde una por una; ver `PENDIENTES.md`.

## Datos del curso

- Una sesión semanal: **lunes, hora 7 (13:00), 40 minutos** (de `programacion.csv`).
- 29 sesiones en el año (calendario oficial del 2026-09-14). Varios lunes son festivos, así
  que hay semanas sin clase de Geometría 10° (ver el reparto).

## DBA de la asignatura

Fuente: `dba/matematicas/grados/grado10.tex`. En 10° los DBA de matemáticas se reparten
entre Geometría 10° y Trigonometría 10°. Geometría cubre el componente espacial y métrico,
que en 10° es un solo DBA:

> **DBA 5.** Explora y describe las propiedades de los lugares geométricos y de sus
> transformaciones a partir de diferentes representaciones.
>
> Evidencias de aprendizaje:
> 1. Localiza objetos geométricos en el plano cartesiano.
> 2. Identifica las propiedades de lugares geométricos a través de su representación en un
>    sistema de referencia.
> 3. Utiliza las expresiones simbólicas de las cónicas y propone los rangos de variación para
>    obtener una gráfica requerida.
> 4. Representa lugares geométricos en el plano cartesiano, a partir de su expresión
>    algebraica.
>
> Ejemplo del DBA: diseñar una imagen escribiendo las ecuaciones en un software de geometría
> dinámica (o en papel milimetrado) y explicar el paso a paso.

### Reparto con Trigonometría 10° (para que la docente lo concilie)

Otro agente está planeando Trigonometría 10° al mismo tiempo; este es el reparto que se
supone aquí:

| DBA | Enunciado (resumido) | Asignatura |
|---|---|---|
| 5 | Lugares geométricos y cónicas en el plano cartesiano | **Geometría 10°** |
| 4 | Funciones trigonométricas y fenómenos periódicos | Trigonometría 10° |
| 1, 2 | Propiedades de los números reales; orden e intervalos | Trigonometría 10° (componente numérico; 10° no tiene Álgebra ni Cálculo) |
| 3, 6, 7 | Razón de cambio, variación, pendiente de la tangente | Trigonometría 10° (componente variacional) |
| 8, 9, 10 | Estadística y probabilidad | otra asignatura |

**Punto de roce: la pendiente de una recta.** El módulo de 10° la trabaja en «La función
tangente y la pendiente» (Tema 4, trigonometría), y el banco guarda esos 7 ejercicios con
`dba=matematicas-10-5` (Geometría). Esta propuesta pone la recta (pendiente, ecuaciones,
paralelas y perpendiculares) en Geometría 10° como primer lugar geométrico y deja a
Trigonometría la relación `m = tan θ` (ángulo de inclinación). **La docente decide.**

## Reparto por trimestre (propuesta)

Sesiones y semanas contadas con un lector CSV sobre `programacion.csv`.

| Trimestre | Sesiones | Clases | Semanas con clase | Evidencias | Contenido |
|---|---|---|---|---|---|
| I | 9 | 001–009 | 02–08, 10, 12 | 1, 2, 4 | Sistema de referencia: plano cartesiano, distancia entre dos puntos, punto medio, idea de lugar geométrico (mediatriz, circunferencia), la recta (pendiente, ecuaciones, paralelas y perpendiculares). Evaluación del periodo en la semana 12. |
| II | 12 | 010–021 | 14–16, 18–26 | 2, 3, 4 | Circunferencia y parábola como lugares geométricos: definición, ecuación canónica y general, gráfica, rangos de variación; traslaciones (transformaciones). Evaluación en la semana 26. |
| III | 8 | 022–029 | 27–32, 34, 35 | 3, 4 | Elipse e hipérbola; proyecto de diseño con cónicas (ejemplo del DBA), en papel milimetrado o con GeoGebra si hay sala. |

Semanas del trimestre sin clase de Geometría 10° (lunes festivo o receso): 01 (empieza el
martes 1 de sept.), 09 (2 nov.), 11 (16 nov.), 17 (vacaciones; la 16 cae el 21 dic., justo
antes), 33 (10 may.), 36 (31 may.) y 37 (7 jun.).

**Aviso para la docente:** el trimestre III **no tiene sesión en su semana de evaluación**
(semana 37: el lunes 7 de junio es festivo) y su última clase es el 24 de mayo (semana 35).
Hay que decidir cuándo se hace la evaluación del periodo III (¿en la sesión 029?, ¿en otro
horario?).

### Criterios

- Un solo DBA para todo el año: el orden va de lo que ya saben (ubicar puntos, Pitágoras) a
  lo nuevo (cónicas), para que la evidencia 3 (cónicas) llegue cuando ya dominen distancia y
  ecuación de la recta, que son la base de las definiciones de cada cónica.
- La recta y la circunferencia se ven como *lugares geométricos* (conjunto de puntos que
  cumplen una condición de distancia), no solo como fórmulas: eso es lo que pide la
  evidencia 2.
- El trimestre II es el más largo (12 sesiones): ahí van circunferencia y parábola, las
  cónicas con más ejercicios de nivel de 10°.
- El trimestre III tiene solo 8 sesiones y sin semana de evaluación propia: se deja para la
  elipse, la hipérbola y un proyecto de diseño que puede servir de evaluación.
- La semana de refuerzo de Trigonometría 10° (semejanza y Pitágoras, según la bitácora)
  prepara la fórmula de la distancia.

## Ritmo de evaluación (propuesta)

Una sola sesión semanal de **40 minutos** (la hora 7, la más corta): no alcanza para
explicar un tema nuevo y además hacer un taller largo el mismo día.

- **Tarea** casi todas las semanas: es la práctica principal del curso.
- **Taller** cada dos o tres semanas, en la sesión que aplica lo visto (unos 25 minutos).
- **Quiz** corto (10–15 minutos, al comienzo de la clase) cuando cierra un bloque: uno a
  mitad del trimestre y otro en la última clase antes de la evaluación.
- La **semana de evaluación** (12 en el trimestre I) es solo la evaluación del periodo: sin
  taller, quiz ni tarea.
- La sesión 001 (semana 02) ya se dictó antes de esta planeación: queda registrada sin DBA y
  sin marcas.

## Hilo conductor del trimestre I (elegir uno)

| Opción | Hilo | Por qué |
|---|---|---|
| **A (recomendada)** | **Ubicarse en la Tierra: de las coordenadas geográficas al plano cartesiano** | Continúa directamente lo que se hizo en la sesión 001 (video de coordenadas geográficas). Latitud y longitud llevan a los ejes; la distancia entre dos puntos, al problema de medir distancias en un mapa; la recta, a los rumbos. Da pie a una aclaración importante: la Tierra es una esfera y el plano es solo una aproximación local (mapas, proyecciones). |
| B | **Descartes y Fermat: cuando el álgebra aprendió a dibujar** | Origen histórico de la geometría analítica: René Descartes publicó *La Géométrie* en 1637, como apéndice del *Discurso del método*; Pierre de Fermat llegó a ideas semejantes por la misma época (su trabajo circuló en manuscrito). Encaja con «lugar geométrico», término que ambos usaron. |
| C | **Eratóstenes mide la Tierra** | Hacia el 240 a. C. Eratóstenes estimó la circunferencia terrestre comparando las sombras del Sol en Siena y Alejandría. Une ángulos, distancias y la circunferencia (que abre el trimestre II). Menos ligado al plano cartesiano que A y B. |

Datos para verificar antes de usarlos en una guía (no verificados aquí):
- La anécdota de Descartes y la mosca en el techo es una **leyenda** sin fuente
  contemporánea: si se cuenta, presentarla como tal.
- La atribución del sistema de latitud y longitud a Hiparco (s. II a. C.) y el valor exacto
  que obtuvo Eratóstenes (depende de la longitud del *estadio*, que se discute) deben
  comprobarse en una fuente antes de ponerlos en la guía.
- Las coordenadas de Cali (aprox. 3,4° N, 76,5° O) y cualquier distancia entre ciudades
  colombianas que se use en ejercicios deben comprobarse en una fuente.
- En 11° se dejó una investigación sobre la hipérbola y LORAN (bitácora): conviene no repetir
  ese contexto en 10° cuando llegue la hipérbola (trimestre III).

| Trimestre | Hilo | Estado |
|---|---|---|
| I | Ubicarse en la Tierra: de las coordenadas geográficas al plano cartesiano | aprobado |
| II | por definir | — |
| III | por definir | — |

## Propuesta del trimestre I, sesión por sesión

Evaluación del periodo en la semana 12. No hay clase en las semanas 09 (2 nov.) y 11
(16 nov.), festivos. `x` = se aplica ese día (quiz, taller) o se deja (tarea).

| Clase | Fecha | Sem. | Tema | Subtema | DBA | Quiz | Taller | Tarea |
|---|---|---|---|---|---|---|---|---|
| 001 | 2026-09-07 | 02 | Plano cartesiano | Coordenadas geográficas (video) y su relación con las coordenadas del plano cartesiano: ubicación en el plano *(dictada; registrada según la bitácora)* | — | | | |
| 002 | 2026-09-14 | 03 | Plano cartesiano | Sistema de referencia: ejes, cuadrantes, ubicar puntos y figuras (polígonos) en el plano | 5 | | | x |
| 003 | 2026-09-21 | 04 | Distancia entre dos puntos | La fórmula de la distancia a partir del teorema de Pitágoras | 5 | | | x |
| 004 | 2026-09-28 | 05 | Distancia entre dos puntos | Punto medio de un segmento; perímetros y clasificación de triángulos en el plano | 5 | | x | |
| 005 | 2026-10-05 | 06 | Lugares geométricos | Qué es un lugar geométrico: la mediatriz y la circunferencia como puntos a igual distancia | 5 | x | | x |
| 006 | 2026-10-19 | 07 | La recta | Pendiente de una recta que pasa por dos puntos; rectas crecientes, decrecientes, horizontales y verticales | 5 | | | x |
| 007 | 2026-10-26 | 08 | La recta | Ecuación de la recta: punto-pendiente, pendiente-intercepto y forma general; graficar desde la ecuación | 5 | | x | |
| 008 | 2026-11-09 | 10 | La recta | Rectas paralelas y perpendiculares; repaso del trimestre | 5 | x | | x |
| 009 | 2026-11-23 | 12 | Evaluación del periodo | Evaluación del periodo I | 5 | | | |

Notas:
- Quiz de la 005: distancia y punto medio. Quiz de la 008: la recta. Tarea de la 008:
  repaso para la evaluación (hay dos semanas sin clase antes de la 009).
- **Hoy es 2026-09-14 (sesión 002):** si la clase ya se dictó, preguntar a la docente qué se
  vio y registrarlo así; la 002 no llevaría paquete.
- Si Trigonometría 10° se queda con la pendiente, las sesiones 006–008 se reorganizan
  (por ejemplo, ecuación de la recta + circunferencia adelantada).

## Recursos principales

- **Geometría 10° (cónicas) no tiene recurso aprobado en `recursos/`.** El módulo de
  Geometría (`recursos/matematicas/Guías pedagógicas Matemáticas/Modulo_Matematicas_Geometria`)
  llega al nivel de 6°–8° y no trae cónicas ni lugares geométricos en el plano cartesiano.
- Único material de geometría analítica para 10°: módulo de Matemáticas 10°, Tema 4, «La
  función tangente y la pendiente» (`markdown/10 - Modulo_Matematicas_Decimo.md`), y sus 7
  ejercicios verificados en `recursos/banco/matematicas/rectas-inclinacion-10.py`.
- Para la fórmula de la distancia pueden servir los ejercicios de Pitágoras del banco
  (`pitagoras-9.py`, `pitagoras-8.py`) y `plano-cartesiano-5.py` como diagnóstico, adaptados
  al nivel de 10°.
- `guias-anteriores/` solo tiene Geometría 4°–6°: nada aprovechable para 10°.
- Hace falta que la docente apruebe un recurso (libro o guía) de geometría analítica y
  cónicas antes de hacer la guía del trimestre II; para el trimestre I basta con lo anterior.

## Pendientes que decide la docente (no se decidieron aquí)

De `recursos/banco/PENDIENTES.md` y del estado en `CLAUDE.md`:
- Geometría 10°: cónicas sin recurso y sin ejercicios en el banco (solo los 7 de rectas).
- Las preguntas abiertas del banco de Matemáticas 10° (29) esperan aprobación.
- Temas del módulo de Geometría repetidos en dos grados (triángulos y ángulos 6°/8°,
  Pitágoras 9°/11°): no afecta directamente a 10°, pero decide dónde quedan los ejercicios de
  Pitágoras que se reutilicen para la distancia.
- Reparto de DBA con Trigonometría 10° (ver arriba), en especial la pendiente.
- Evaluación del periodo III sin sesión en su semana de evaluación.
