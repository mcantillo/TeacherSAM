# Plan anual 2026–2027 — Física 10°

Aprobado por la docente el 2026-09-18: el reparto por trimestre, el ritmo de evaluación
y el hilo del trimestre I (opción **A**, «De la inercia a los *Principia*»). El trimestre I ya está escrito
sesión a sesión en `programacion.csv` (se llenó el 2026-09-17). Quedan abiertas las
preguntas de este plan, que la docente responde una por una; ver `PENDIENTES.md`.

**Decisión del 2026-09-19:** el grupo vio cinemática **a medias** en 9° (MRU sí; MUA y caída
libre no), así que no es repaso sino tema nuevo en parte: pasa de 2 a **3 sesiones** (009–011).
Para no tocar el calendario, «Tercera ley» baja de 2 sesiones a 1 (020) y «Las tres leyes» se
queda con 2 (021–022). Los quices siguen en las sesiones 010, 014, 018 y 022, y los talleres y
tareas no se mueven.

## DBA y estándares de la asignatura

Fuentes: `dba/naturales/grados/grado10.tex` (los dos DBA de física de 10°) y
`dba/naturales/estandares-fisica.md` (Estándares MEN 2004, grupo 10°–11°, entorno físico,
compartido con Física 11°).

**DBA 1:** «Comprende, que el reposo o el movimiento rectilíneo uniforme, se presentan cuando
las fuerzas aplicadas sobre el sistema se anulan entre ellas, y que en presencia de fuerzas
resultantes no nulas se producen cambios de velocidad.»
Evidencias: (1) predice el equilibrio de un cuerpo a partir de las fuerzas que actúan sobre él
(primera ley); (2) estima los cambios de velocidad a partir de la relación entre fuerza y masa
(segunda ley); (3) identifica, en interacciones directas y a distancia, la fuerza de acción y
la de reacción, con sus valores y direcciones (tercera ley).

**DBA 2:** «Comprende la conservación de la energía mecánica como un principio que permite
cuantificar y explicar diferentes fenómenos mecánicos: choques entre cuerpos, movimiento
pendular, caída libre, deformación de un sistema masa-resorte.»
Evidencias: (1) predice cualitativa y cuantitativamente el movimiento de un cuerpo con la
conservación de la energía mecánica; (2) identifica, en sistemas no conservativos (fricción,
choques no elásticos, deformación, vibraciones), las transformaciones de energía.

**Estándares 10°–11° usados para partir los DBA en temas:**

| Estándar | Tema | DBA |
|---|---|---|
| Relaciones entre las fuerzas sobre cuerpos en reposo o en MRU; condiciones para conservar la energía mecánica | Primera ley, equilibrio; energía | 1, 2 |
| Modelo matemáticamente el movimiento de objetos cotidianos a partir de las fuerzas | Segunda ley, fricción, plano inclinado, proyectiles, movimiento circular | 1 |
| Relaciono masa, distancia y fuerza de atracción gravitacional; campo gravitacional y ley de gravitación universal | Gravitación | 1 (fuerza a distancia, tercera ley) |
| Relaciones entre estabilidad y centro de masa | Centro de masa | 1 |
| Conservación del momento lineal e impulso en sistemas de objetos | Momento lineal, choques | 2 (choques) |
| Transformación de energía mecánica en térmica | Sistemas no conservativos | 2 |
| Comportamiento de fluidos en movimiento y en reposo | Fluidos | **sin DBA** |
| (columna «me aproximo… como científico-a natural»: medir, registrar datos, modelar) | Mediciones, notación científica | **sin DBA** (herramienta) |

Termodinámica no aparece en los estándares 10°–11° ni en los DBA de 10° (está en los de
8°–9°). Mediciones, fluidos y termodinámica son los temas «sin DBA» de 10° pendientes en
`recursos/banco/PENDIENTES.md`: **decisión de la docente**; esta propuesta usa mediciones
como herramienta al comienzo (ya empezó con la notación científica) y deja fluidos y
termodinámica fuera, salvo que ella diga otra cosa.

## Reparto por trimestre

Física 10° tiene **dos sesiones semanales de 100 min** (jueves y viernes, 7:50). Conteo hecho
sobre `programacion.csv` con un lector CSV:

| Trimestre | Semanas | Sesiones | Clases | DBA | Contenido |
|---|---|---|---|---|---|
| I | 01–12 | 24 | 001–024 | 1 | Inicio y notación científica (ya dictados). Medición: SI, conversión, cifras significativas, orden de magnitud. Vectores. Repaso de cinemática (MRU, MUA, caída libre). Fuerza y leyes de Newton: primera (equilibrio, diagramas de cuerpo libre), segunda (F = m·a, fricción, plano inclinado), tercera (acción y reacción). |
| II | 13–26 | 26 | 025–050 | 1 | Dinámica en dos dimensiones: proyectiles (retoma de 9°) y movimiento circular uniforme con fuerza centrípeta. Gravitación universal y leyes de Kepler (la fuerza a distancia de la tercera evidencia). Centro de masa y estabilidad. Al final: trabajo y potencia, como puente al DBA 2. |
| III | 27–37 | 22 | 051–072 | 2 | Energía cinética y potencial (gravitacional y elástica). Conservación de la energía mecánica: caída libre, péndulo, masa-resorte. Momento lineal, impulso y choques (elásticos e inelásticos). Sistemas no conservativos: fricción y energía térmica. |

Criterios:

- **Respetar lo ya dictado.** Semana 01: actividades de inicio y un proyecto sobre la primera
  ley de Newton o la presión atmosférica; semana 02: notación científica (bitácora). La
  notación científica abre un bloque corto de medición (una semana) en vez de quedar suelta.
- **Newton entero en el I.** El DBA 1 es el núcleo de 10° y el trimestre I tiene 24 sesiones
  de 100 min: alcanza para las tres leyes con problemas y un laboratorio.
- **La cinemática se repasa, no se enseña de cero:** es el DBA de 9°. Una semana de repaso
  (MRU, MUA, caída libre) antes de la segunda ley.
- **Choques con energía.** El DBA 2 nombra los choques; se ven en el III, junto con la
  conservación de la energía, para distinguir choques elásticos e inelásticos.
- **Enlace con Física 11°:** la ley de Coulomb de 11° se enseña «como la gravitación»: la
  gravitación de 10° (trimestre II) es su antecedente.

## Ritmo de evaluación (propuesto)

Dos sesiones de 100 min a la semana (jueves y viernes), sin festivos en el trimestre I:

- **Taller** en la sesión del **jueves**, casi todas las semanas.
- **Tarea** asignada el **viernes**, revisada el jueves siguiente.
- **Quiz** de unos 20 min en el **viernes** de la semana en que cierra un tema (cuatro en el
  trimestre I).
- Al menos un **laboratorio o demostración** por tema (columna «me aproximo al conocimiento
  como científico-a natural» de los estándares).
- **Última semana del trimestre:** jueves repaso, viernes evaluación del periodo; sin taller
  ni quiz.

En el trimestre I esto da 8 talleres, 8 tareas y 4 quices, más la evaluación del periodo.

## Evidencias que se evaluarían en el trimestre I

- Expresa medidas en notación científica y en unidades del SI, con las cifras significativas
  adecuadas (herramienta; sin DBA).
- Suma fuerzas como vectores y halla la fuerza neta (base de las tres evidencias del DBA 1).
- Predice el equilibrio de un cuerpo a partir de su diagrama de cuerpo libre (DBA 1, ev. 1).
- Calcula la aceleración a partir de la fuerza neta y la masa, con y sin fricción (DBA 1, ev. 2).
- Identifica pares acción-reacción, de contacto y a distancia, con valor y dirección (DBA 1,
  ev. 3; el ejemplo del DBA: adulto y niño tirando de una cuerda, el adulto sobre hielo).

## Hilos conductores del trimestre I (elegir uno)

Registro juvenil (grado 10). Solo historia real; fechas y citas se verifican contra fuente
antes de escribir la guía, como pide `crear-guia`.

| Opción | Hilo | Qué lo sostiene | Qué falta verificar |
|---|---|---|---|
| **A (recomendada)** | **«De la inercia a los *Principia*»** | Galileo y el plano inclinado (la inercia antes de Newton); Newton publica los *Philosophiæ Naturalis Principia Mathematica* en 1687, con las tres leyes, gracias a que Edmond Halley lo animó y pagó la impresión. Recorre todo el trimestre: medir (Galileo con planos y relojes de agua), primera, segunda y tercera ley. | El enunciado de las tres leyes en una traducción al español con fuente; el papel exacto de Halley; la anécdota de la manzana (viene de William Stukeley, 1752): si se usa, presentarla como anécdota, no como hecho. |
| B | «El cohete que “no podía” volar» | Tercera ley como eje: Robert Goddard lanza el primer cohete de combustible líquido (1926); un editorial del *New York Times* de 1920 se burló de que un cohete no podría avanzar en el vacío, y el diario publicó una corrección en julio de 1969, durante el Apolo 11. | Fechas y texto del editorial y de la corrección. Cubre bien la tercera ley, menos la medición y la primera. |
| C | «Medir el mundo» | Del metro de la Revolución Francesa (medición del meridiano por Delambre y Méchain, 1792–1798) a la redefinición del SI en 2019. Continúa la notación científica ya dictada. | Fechas; solo sostiene las primeras semanas (medición), no las leyes de Newton. |

## Propuesta del trimestre I, sesión por sesión

Clases 001–004 ya dictadas (registradas en `programacion.csv`). Clases 005–024: propuesta,
no se escriben en el CSV hasta que la docente las apruebe.

| Semana | Clase | Fecha | Tema | Subtema | DBA | Quiz | Taller | Tarea |
|---|---|---|---|---|---|---|---|---|
| 01 | 001 | 2026-09-03 jue | Inicio de año | Integración y proyecto de inicio (dictada) | — | | | |
| 01 | 002 | 2026-09-04 vie | Inicio de año | Integración y proyecto de inicio (dictada) | — | | | |
| 02 | 003 | 2026-09-10 jue | Herramientas de trabajo | Notación científica: explicación, ejercicios, puesta en común y video (dictada) | — | | | |
| 02 | 004 | 2026-09-11 vie | Herramientas de trabajo | Notación científica: explicación, ejercicios, puesta en común y video (dictada) | — | | | |
| 03 | 005 | 2026-09-17 jue | Medición | Magnitudes, SI, prefijos y conversión de unidades | — | | x | |
| 03 | 006 | 2026-09-18 vie | Medición | Cifras significativas, incertidumbre; orden de magnitud y estimación | — | | | x |
| 04 | 007 | 2026-09-24 jue | Vectores | Escalares y vectores; suma gráfica | 1 | | x | |
| 04 | 008 | 2026-09-25 vie | Vectores | Componentes y suma por componentes | 1 | x | | x |
| 05 | 009 | 2026-10-01 jue | Repaso de cinemática | Velocidad y aceleración; MRU y MUA con gráficas | 1 | | x | |
| 05 | 010 | 2026-10-02 vie | Repaso de cinemática | Caída libre (Galileo) | 1 | | | x |
| 06 | 011 | 2026-10-08 jue | Primera ley de Newton | Qué es una fuerza; fuerza neta; inercia | 1 | | x | |
| 06 | 012 | 2026-10-09 vie | Primera ley de Newton | Equilibrio: reposo y MRU cuando las fuerzas se anulan | 1 | x | | x |
| — | — | 12–16 oct. | *Receso de octubre* | | | | | |
| 07 | 013 | 2026-10-22 jue | Primera ley de Newton | Peso, normal y tensión; diagramas de cuerpo libre | 1 | | x | |
| 07 | 014 | 2026-10-23 vie | Primera ley de Newton | Problemas de equilibrio con diagrama de cuerpo libre | 1 | | | x |
| 08 | 015 | 2026-10-29 jue | Segunda ley de Newton | F = m·a; masa inercial; el newton | 1 | | x | |
| 08 | 016 | 2026-10-30 vie | Segunda ley de Newton | Problemas: fuerza neta y aceleración | 1 | | | x |
| 09 | 017 | 2026-11-05 jue | Segunda ley de Newton | Fricción estática y cinética | 1 | | x | |
| 09 | 018 | 2026-11-06 vie | Segunda ley de Newton | Plano inclinado; laboratorio: fuerza y aceleración de un carrito | 1 | x | | x |
| 10 | 019 | 2026-11-12 jue | Tercera ley de Newton | Acción y reacción, de contacto y a distancia (la cuerda del ejemplo del DBA) | 1 | | x | |
| 10 | 020 | 2026-11-13 vie | Tercera ley de Newton | Pares acción-reacción en situaciones cotidianas; el cohete | 1 | | | x |
| 11 | 021 | 2026-11-19 jue | Las tres leyes | Problemas integrados | 1 | | x | |
| 11 | 022 | 2026-11-20 vie | Las tres leyes | Síntesis y dudas | 1 | x | | x |
| 12 | 023 | 2026-11-26 jue | Evaluación del periodo | Repaso general | 1 | | | |
| 12 | 024 | 2026-11-27 vie | Evaluación del periodo | Evaluación del periodo I | 1 | | | |

Quices: 008 medición y vectores · 012 cinemática y primera ley (concepto) · 018 primera y
segunda ley · 022 tercera ley e integración. Las clases 005–006 quedan sin DBA (medición es
herramienta; pendiente de la docente).

## Recursos principales

- `recursos/fisica/Guías pedagógicas Física/markdown/10 - Guia_de_apoyo_cinematica_y_dinamica_grado_10_fisica.md`:
  cap. 1 (mediciones, SI, cifras significativas, notación científica, orden de magnitud),
  cap. 2 (cinemática en una dimensión, caída libre), cap. 3 (vectores, proyectiles, velocidad
  relativa), cap. 4 (leyes de Newton, peso y normal, diagramas de cuerpo libre). Cubre todo el
  trimestre I y el comienzo del II.
- `…/10 - Guia_de_Apoyo_movimiento_circular_energia_fluidos_y_termodinamica_grado_10_fisica.md`:
  cap. 1 (movimiento circular, Kepler, gravitación universal, rotación de sólidos) → II;
  cap. 2 (trabajo, energía, potencia, conservación) → II y III; caps. 3–4 (fluidos y
  termodinámica) → solo si la docente los incluye.
- **Momento lineal y choques:** ninguna guía de 10° los trae; solo aparecen, a nivel
  conceptual, en `…/05 - Guia_de_apoyo_Conceptos_de_Dinamica_leyes_de_Newton_grado_5_fisica.md`
  (cap. 2). Para el III habrá que buscar o pedir otro recurso.
- `…/08 - …Calor_y_termodinamica_grado_8_fisica.md` (presión atmosférica, hemisferios de
  Magdeburgo): relacionado con el proyecto de inicio de la semana 01.
- **Banco** (`python3 tools/ejercicios.py listar --grado 10`): `mediciones-10` (76 verificados,
  sin DBA), `cinematica-10` (51), `cinematica-2d-10` (22), `leyes-newton-10` (32),
  `movimiento-circular-10` (51), `energia-10` (43), `fluidos-10` y `termodinamica-10` (sin
  DBA), más abiertas pendientes de aprobación en cada archivo. Correcciones pendientes de
  revisar en `PENDIENTES.md` (cinemática cap. 3 problemas 5–6, movimiento circular 17–18,
  energía 6b, y movimiento circular «Desarrolla 13»).

## Estado y preguntas pendientes

- Registradas en `programacion.csv` las clases 001–004 con lo que dice la bitácora, sin DBA
  ni marcas. La bitácora no dice cómo se repartió el trabajo entre el jueves y el viernes de
  cada semana: el subtema se repitió en las dos filas.
- **Proyecto de la semana 01:** la bitácora dice «en Física de 9 y 10 se hizo proyectos de
  inicio sobre la primera ley de Newton y sobre la presión atmosférica». ¿Cuál hizo 10°?
  (Si fue la primera ley, se puede retomar en la clase 011.)
- ¿Entran mediciones (clases 005–006), fluidos y termodinámica, que no tienen DBA?
- Los estudiantes de 10° ¿vieron cinemática en 9° el año pasado? De eso depende si una semana
  de repaso alcanza.
- Momento lineal y choques no tienen recurso de 10°.
- Elegir el hilo del trimestre I.
