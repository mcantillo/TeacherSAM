# Plan anual 2026–2027 — Física 9°

Aprobado por la docente el 2026-09-18: el reparto por trimestre, el ritmo de evaluación
y el hilo del trimestre I (opción **A**, «De Aristóteles a Galileo: aprender a describir el movimiento»). El trimestre I ya está escrito
sesión a sesión en `programacion.csv` (se llenó el 2026-09-17). Quedan abiertas las
preguntas de este plan, que la docente responde una por una; ver `PENDIENTES.md`.

**Decisión del 2026-09-19:** quedan **7 exposiciones** por presentar y ocupan **dos sesiones
completas**, la 002 (4 exposiciones) y la 003 (3 y cierre), a unos 12 minutos cada una. Por eso
esas dos sesiones no llevan taller; los dos talleres del trimestre pasan a las sesiones 005 y
007. Sigue pendiente quién hizo el proyecto de la semana 01 (primera ley / presión atmosférica).

## DBA y estándares de la asignatura

Fuentes: `dba/naturales/grados/grado09.tex` (el único DBA de física de 9°) y
`dba/naturales/estandares-fisica.md` (Estándares MEN 2004, grupo 8°–9°, entorno físico).

**DBA 1 (grado 9):** «Comprende que el movimiento de un cuerpo, en un marco de referencia
inercial dado, se puede describir con gráficos y predecir por medio de expresiones
matemáticas.»

Evidencias:
1. Describe el movimiento de un cuerpo (rectilíneo uniforme y uniformemente acelerado, en dos
   dimensiones – circular uniforme y parabólico) en gráficos que relacionan el desplazamiento,
   la velocidad y la aceleración en función del tiempo.
2. Predice el movimiento de un cuerpo a partir de las expresiones matemáticas con las que se
   relaciona, según el caso, la distancia recorrida, la velocidad y la aceleración en función
   del tiempo.
3. Identifica las modificaciones necesarias en la descripción del movimiento de un cuerpo,
   representada en gráficos, cuando se cambia de marco de referencia.

Ejemplo del DBA: un pasajero de un bus deja caer una pelota; para él cae en línea vertical,
para un peatón describe una parábola.

**Estándares 8°–9° (física)** — ninguno trata el movimiento; todos son de otros temas:

| Estándar | Tema | ¿DBA? |
|---|---|---|
| Relaciones entre frecuencia, amplitud, velocidad de propagación y longitud de onda en ondas mecánicas; conservación de la energía en ondas que cambian de medio | Ondas y sonido | **no** |
| Modelos para explicar la naturaleza y el comportamiento de la luz | Luz | **no** |
| Variables de estado, energía interna, trabajo y transferencia de energía térmica; gases ideales y reales; vientos | Calor y termodinámica | **no** |
| Masa, peso y densidad; sólidos, líquidos y gases | Materia (compartido con química) | **no** |

Es decir: el DBA pide cinemática y los estándares piden ondas, luz y calor. Qué entra de lo
segundo es **decisión de la docente** (pendiente también en `recursos/banco/PENDIENTES.md`,
«Física sin DBA», 9°). Esta propuesta no lo decide: deja el DBA 1 en los trimestres I y II y
ofrece dos opciones para el III.

## Reparto por trimestre

Física 9° tiene **una sola sesión semanal de 50 min** (lunes 10:10). Los festivos del 2 y 16
de noviembre y del 31 de mayo y 7 de junio caen en lunes. Conteo hecho sobre
`programacion.csv` con un lector CSV:

| Trimestre | Semanas | Sesiones | Clases | DBA | Contenido |
|---|---|---|---|---|---|
| I | 02–12 | 9 | 001–009 | 1 (evidencias 1–3, en una dimensión) | Exposiciones de científicos (ya asignadas). Describir el movimiento: marco de referencia, posición, trayectoria, distancia y desplazamiento; rapidez y velocidad media. Movimiento rectilíneo uniforme: ecuación y gráficas x–t y v–t. El mismo movimiento visto desde dos marcos. |
| II | 14–26 | 12 | 010–021 | 1 (evidencias 1–3, completas) | Aceleración y movimiento uniformemente acelerado: ecuaciones y gráficas. Caída libre. Movimiento en dos dimensiones: parabólico (la pelota del bus del DBA) y circular uniforme. |
| III | 27–35 | 8 | 022–029 | ninguno (opción A) o 1 (opción B) | **Opción A:** ondas mecánicas y sonido (estándares 8°–9°, sin DBA). **Opción B:** profundizar el DBA 1 (gráficas de movimiento con datos reales, problemas de encuentro y de proyectiles) y dejar ondas, luz y calor fuera. |

Luz y termodinámica no caben en 8 sesiones junto con ondas; si la docente las quiere, habría
que recortar el trimestre II.

Criterios:

- **Respetar lo ya dictado.** Según la bitácora, en la semana 02 (clase 001, 7 sept.) se dejó
  una investigación sobre un científico, con exposiciones por grupos «en las siguientes
  semanas»: la propuesta les da las clases 002 y 003 y enlaza su cierre con el hilo del
  trimestre.
- **El DBA completo antes que los estándares sin DBA.** Con 21 sesiones en I y II, el DBA 1
  (cuatro tipos de movimiento, gráficas, ecuaciones y marcos de referencia) necesita los dos
  trimestres.
- **Una dimensión antes que dos.** El trimestre I se queda en el MRU y el cambio de marco en
  una dimensión; el II suma la aceleración y el plano.
- **Enlace con Física 10°:** el DBA 1 de 10° (leyes de Newton) usa la aceleración como
  «cambio de velocidad»; en 10° se repasa la cinemática, así que lo de 9° es su base.

## Ritmo de evaluación (propuesto)

Una sesión de 50 min a la semana obliga a un ritmo corto:

- **Tarea** asignada en la sesión, revisada al comienzo de la siguiente, casi todas las semanas.
- **Taller** en clase, cada dos o tres semanas (ocupa casi la sesión entera).
- **Quiz** de 10–15 min al comienzo de la sesión en que cierra un tema (uno o dos por trimestre).
- **Última semana del trimestre:** evaluación del periodo, sin taller ni quiz. Como en esa
  semana solo hay una sesión de 50 min, **el repaso va en la sesión anterior**.
- **Trimestre III: no hay sesión en la semana de evaluación** (semanas 36–37: lunes 31 de mayo
  y 7 de junio son festivos). La evaluación del periodo III tendría que ir en la clase 029
  (24 de mayo, semana 35) o en otro horario: **decisión de la docente**.

En el trimestre I esto da 2 talleres, 3 tareas y 1 quiz, más la evaluación del periodo.

## Evidencias que se evaluarían en el trimestre I

- Distingue distancia recorrida de desplazamiento y rapidez de velocidad en un marco dado
  (evidencia 1).
- Construye e interpreta gráficas x–t y v–t de un MRU y lee en ellas la velocidad y el
  desplazamiento (evidencia 1).
- Predice la posición de un cuerpo con MRU usando x = x₀ + v·t (evidencia 2).
- Describe cómo cambia la velocidad y la gráfica de un movimiento al pasar a otro marco de
  referencia (evidencia 3).

## Hilos conductores del trimestre I (elegir uno)

Registro juvenil (grado 9). Solo historia real; las fechas se verifican contra fuente antes de
escribir la guía, como pide `crear-guia`.

| Opción | Hilo | Qué lo sostiene | Qué falta verificar |
|---|---|---|---|
| **A (recomendada)** | **«De Aristóteles a Galileo: aprender a describir el movimiento»** | Continúa las exposiciones de científicos que ya están en marcha. Aristóteles (movimiento «natural» y «violento»), Nicole Oresme (siglo XIV: representó la velocidad frente al tiempo con un diagrama, antecedente de la gráfica v–t) y Galileo (*Discursos y demostraciones sobre dos nuevas ciencias*, 1638: movimiento uniforme y uniformemente acelerado). | La afirmación exacta sobre el diagrama de Oresme y el año de su tratado (hacia 1350); qué dice Galileo del movimiento uniforme en la «Jornada tercera». |
| B | «¿Quién se mueve? El barco de Galileo» | El marco de referencia como eje: el experimento mental del camarote del barco en el *Diálogo sobre los dos máximos sistemas del mundo* (1632) y la pelota del bus del propio DBA. | La cita textual del barco (traducción al español con fuente). |
| C | «Cronómetros y récords» | Contexto deportivo: el 100 m de Usain Bolt (9,58 s, Berlín 2009) y atletas colombianos para comparar velocidades medias con datos reales. | Todas las marcas y fechas; es contexto, no historia de la física, y encaja peor con las exposiciones. |

## Propuesta del trimestre I, sesión por sesión

Clase 001 ya dictada (registrada en `programacion.csv`). Clases 002–009: propuesta, no se
escriben en el CSV hasta que la docente las apruebe. **La clase 002 es hoy (lunes 14 sept.):**
si ya se dictó algo distinto, se registra lo que se dio.

| Semana | Clase | Fecha | Tema | Subtema | DBA | Quiz | Taller | Tarea |
|---|---|---|---|---|---|---|---|---|
| 02 | 001 | 2026-09-07 lun | Inicio de año | Investigación asignada: un científico de todos los tiempos (dictada) | — | | | |
| 03 | 002 | 2026-09-14 lun | Científicos que cambiaron la física | Exposiciones por grupos (primera parte) | — | | | |
| 04 | 003 | 2026-09-21 lun | Científicos que cambiaron la física | Exposiciones (segunda parte) y cierre: ¿cómo describió Galileo el movimiento? | — | | | x |
| 05 | 004 | 2026-09-28 lun | Describir el movimiento | Marco de referencia, posición y trayectoria; distancia y desplazamiento | 1 | | | x |
| 06 | 005 | 2026-10-05 lun | Describir el movimiento | Rapidez media y velocidad media; conversión km/h ↔ m/s | 1 | | x | |
| — | — | 12–16 oct. | *Receso de octubre* | | | | | |
| 07 | 006 | 2026-10-19 lun | Movimiento rectilíneo uniforme | Ecuación x = x₀ + v·t y gráfica posición–tiempo | 1 | | | x |
| 08 | 007 | 2026-10-26 lun | Movimiento rectilíneo uniforme | Gráfica velocidad–tiempo; el área como desplazamiento; problemas de encuentro | 1 | x | | |
| 09 | — | 2026-11-02 | *Festivo (Todos los Santos)* | | | | | |
| 10 | 008 | 2026-11-09 lun | Marcos de referencia | Un movimiento, dos observadores (la pelota en el bus); velocidad relativa en una dimensión; repaso del periodo | 1 | | x | |
| 11 | — | 2026-11-16 | *Festivo (Independencia de Cartagena)* | | | | | |
| 12 | 009 | 2026-11-23 lun | Evaluación del periodo | Evaluación del periodo I | 1 | | | |

El quiz de la 007 evalúa «Describir el movimiento» y la ecuación del MRU. La semana 12 no
tiene taller ni quiz.

## Recursos principales

- **No hay recurso de cinemática para 9°**: la guía de 9° es de ondas, sonido y luz. La
  cinemática está en
  `recursos/fisica/Guías pedagógicas Física/markdown/10 - Guia_de_apoyo_cinematica_y_dinamica_grado_10_fisica.md`,
  cap. 2 (marcos de referencia y desplazamiento, velocidad media e instantánea, aceleración,
  aceleración constante, caída libre) y cap. 3 (movimiento de proyectiles, velocidad relativa):
  sirve para I y II, adaptada al nivel de 9°.
- `…/04 - Guia_de_apoyo_Conceptos_de_Mecanica_grado_4_fisica.md`, cap. 3 (movimiento
  rectilíneo) y «Algunas fechas importantes en la historia de la Física»: explicaciones
  conceptuales y apoyo para el hilo (verificar fechas).
- `…/05 - Guia_de_apoyo_Conceptos_de_Dinamica_leyes_de_Newton_grado_5_fisica.md`, cap. 5
  (proyectiles y satélites): trimestre II.
- `…/09 - Guia_de_Apoyo_Conceptos_ondas_de_sonido_y_de_luz_grado_9_fisica.md`, caps. 1–2
  (vibraciones y ondas, sonido): trimestre III si se elige la opción A.
- `…/08 - Guia_de_Apoyo_Conceptos_de_Calor_y_termodinamica_grado_8_fisica.md` (fluidos,
  presión atmosférica): relacionado con el proyecto de inicio de la semana 01.
- **Banco** (`python3 tools/ejercicios.py listar --grado 9`): solo hay física sin DBA
  (`ondas-9`, `sonido-9`, `luz-9`, `optica-9`, `ondas-luminosas-9`, `termodinamica-9`; muchas
  abiertas pendientes de aprobación, y `ondas-9-017` = `sonido-9-025` repetidas). **No hay
  ejercicios de cinemática para 9°**: `cinematica-10` y `cinematica-2d-10` están marcados
  `grados=[10]`; reutilizarlos en 9° es decisión de la docente.

## Estado y preguntas pendientes

- Registrada en `programacion.csv` solo la clase 001 (7 sept.), con lo que dice la bitácora,
  sin DBA ni marcas.
- **Semana 01:** la bitácora dice que 9° hizo un proyecto de inicio (primera ley de Newton o
  presión atmosférica), pero Física 9° no tiene sesión en la semana 01 (su única hora es el
  lunes y las clases empezaron el martes 1). ¿En qué hora se hizo, y cuál de los dos proyectos
  fue el de 9°?
- ¿Cuántos grupos exponen y en cuántas sesiones? (La propuesta supone dos: 002 y 003.)
- Trimestre III: ¿opción A (ondas y sonido, sin DBA) u opción B (solo DBA 1)? ¿Luz o calor en
  algún momento?
- ¿Dónde va la evaluación del periodo III, sin sesión en la semana de evaluación?
- Elegir el hilo del trimestre I.
