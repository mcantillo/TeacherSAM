# Plan anual 2026–2027 — Trigonometría 10°

Aprobado por la docente el 2026-09-18: el reparto por trimestre, el ritmo de evaluación
y el hilo del trimestre I (opción **A**, «Medir lo inalcanzable»). El trimestre I ya está escrito
sesión a sesión en `programacion.csv` (se llenó el 2026-09-17). Quedan abiertas las
preguntas de este plan, que la docente responde una por una; ver `PENDIENTES.md`.

**Decisión del 2026-09-19:** las **leyes del seno y del coseno se quedan en el trimestre II**,
como proponía el plan. El trimestre I se cierra completo en el triángulo rectángulo (razones,
ángulos especiales, resolución, elevación y depresión) y no se toca ninguna sesión.
**Unidades:** todo el material va en el sistema métrico. Si una fuente da pies o millas (alturas
de edificios, distancias náuticas), el dato se convierte **antes** de llegar al estudiante; la
conversión de unidades inglesas no es tema de este curso.

## DBA de la asignatura

Fuente: `dba/matematicas/grados/grado10.tex` (enunciados copiados de ahí). Los DBA son del
grado, no de la asignatura: Trigonometría 10° y Geometría 10° comparten el archivo.

| DBA | Enunciado | Asignatura (propuesta) |
|---|---|---|
| 1 | «Utiliza las propiedades de los números reales para justificar procedimientos y diferentes representaciones de subconjuntos de ellos.» | ¿Trigonometría? (apoyo; ver pregunta 1) |
| 2 | «Utiliza las propiedades algebraicas de equivalencia y de orden de los números reales para comprender y crear estrategias que permitan compararlos y comparar subconjuntos de ellos (por ejemplo, intervalos).» | ¿Trigonometría? (apoyo; ver pregunta 1) |
| 3 | «Resuelve problemas que involucran el significado de medidas de magnitudes relacionales (velocidad media, aceleración media) a partir de tablas, gráficas y expresiones algebraicas.» | ¿Trigonometría / Física 10°? (ver pregunta 1) |
| **4** | «**Comprende y utiliza funciones para modelar fenómenos periódicos y justifica las soluciones.**» | **Trigonometría** (DBA central) |
| 5 | «Explora y describe las propiedades de los lugares geométricos y de sus transformaciones a partir de diferentes representaciones.» | Geometría 10° (cónicas) |
| 6 | «Comprende y usa el concepto de razón de cambio para estudiar el cambio promedio y el cambio alrededor de un punto y lo reconoce en representaciones gráficas, numéricas y algebraicas.» | ¿Trigonometría? (apoyo; ver pregunta 1) |
| 7 | «Resuelve problemas mediante el uso de las propiedades de las funciones y usa representaciones tabulares, gráficas y algebraicas para estudiar la variación, la tendencia numérica y las razones de cambio entre magnitudes.» | ¿Trigonometría? (apoyo; ver pregunta 1) |
| 8, 9, 10 | Estadística y probabilidad | otra asignatura |

Evidencias del DBA 4 (textuales), que ordenan el año:

1. «Reconoce el significado de las razones trigonométricas en un triángulo rectángulo para ángulos agudos, en particular, seno, coseno y tangente.» → trimestre I
2. «Explora, en una situación o fenómeno de variación periódica, valores, condiciones, relaciones o comportamientos, a través de diferentes representaciones.» → trimestre III
3. «Calcula algunos valores de las razones seno y coseno para ángulos no agudos, auxiliándose de ángulos de referencia inscritos en el círculo unitario.» → trimestres I (inicio) y II
4. «Reconoce algunas aplicaciones de las funciones trigonométricas en el estudio de fenómenos diversos de variación periódica, por ejemplo: movimiento circular, movimiento del péndulo, del pistón, ciclo de la respiración, entre otros.» → trimestre III
5. «Modela fenómenos periódicos a través de funciones trigonométricas.» → trimestre III

### Cruce con Geometría 10° (por señalar, no decidido)

- `materias/geometria/decimo/` tiene solo `programacion.csv` (29 sesiones de 40 min, lunes H7,
  sin planear, sin `plan-anual.md`). Su componente natural es el DBA 5 (lugares geométricos y
  cónicas); según la bitácora, en la semana 02 vio coordenadas geográficas y plano cartesiano.
- **Posibles cruces:** (a) las razones trigonométricas en el triángulo rectángulo (evidencia 1
  del DBA 4) podrían reclamarse también desde Geometría; aquí se proponen en Trigonometría;
  (b) pendiente y ángulo de inclinación de una recta (`rectas-inclinacion-10.py`, 7 ejercicios;
  el módulo lo trae en «La función tangente y la pendiente») queda entre las dos — se propone en
  Trigonometría como aplicación de la tangente (trimestre III) y Geometría 10° lo usaría para
  las rectas; (c) semejanza y Pitágoras, que se reforzaron aquí en la semana 02, no deberían
  repetirse en Geometría 10°.
- En 10° **no hay Álgebra ni Cálculo** en el horario: si Trigonometría no toma los DBA 1, 2, 3,
  6 y 7, nadie los cubre (el 3 lo toca en parte Física 10°, con sus propios DBA de naturales).

## Criterios

- **DBA 4 como eje**, en el orden natural del módulo y de sus evidencias: del triángulo
  rectángulo (estático) al ángulo como rotación y al círculo unitario, y de ahí a las
  funciones y sus gráficas.
- **Arrancar desde el diagnóstico:** la semana 02 fue refuerzo de semejanza y Pitágoras, que es
  justo la base de las razones trigonométricas (la razón no depende del tamaño del triángulo
  porque los triángulos son semejantes). El trimestre I empieza aprovechando ese refuerzo.
- **Saber 11:** estos estudiantes presentan la prueba en 11° (calendario B, hacia marzo de 2028;
  sin fecha publicada). La *Guía de orientación Saber 11.º 2026-1* (`recursos/matematicas/icfes/`)
  incluye entre los contenidos no genéricos «Representación gráfica y algebraica de funciones
  racionales, trigonométricas, … además de propiedades básicas, periodicidad, dominios y rangos»
  y, en geometría, «Relaciones de congruencia y semejanza» y «Teoremas clásicos, como el de
  Pitágoras y el de Tales». En el cuadernillo liberado de marzo de 2026, la pregunta 29 pide el
  coseno del ángulo entre una escalera y el suelo, y las preguntas 22 y 23 son de medición
  indirecta con trigonometría. Por eso el trimestre I prioriza razones y resolución de triángulos
  rectángulos, y el III, periodicidad, dominio, rango y gráficas. Estas preguntas del Icfes solo
  se usan textuales y con crédito (condiciones de uso en `recursos/CLAUDE.md`).
- **Recursos antes que invento:** el reparto sigue los temas del módulo de 10° y el banco ya
  verificado (ver «Recursos principales»).
- **Física 10°:** el movimiento circular (velocidad angular, radianes) y los fenómenos
  periódicos se cruzan con Física 10°, que dicta la misma docente; conviene sincronizarlos
  cuando se planee Física 10° (aún sin plan).

## Reparto por trimestre

Conteo hecho con `csv.DictReader` sobre `programacion.csv` (4 sesiones de 50 min por semana:
martes H6, jueves H6 y H8 —no consecutivas, dos filas— y viernes H4).

| Trimestre | Semanas | Sesiones | DBA | Contenido |
|---|---|---|---|---|
| I | 01–12 (clases 001–048) | 48 (8 ya dictadas; 36 de contenido en las semanas 03–11; semana 12 de repaso y evaluación) | 4 (evidencia 1 y comienzo de la 3); 1 como apoyo | Ángulos y sistema sexagesimal; razones trigonométricas en el triángulo rectángulo; ángulos especiales (30°, 45°, 60°, con √2 y √3); resolución de triángulos rectángulos; ángulos de elevación y depresión y medición indirecta. Ángulo como rotación, posición estándar, coterminales; radianes; longitud de arco y área del sector; primer contacto con el círculo unitario. (Módulo, Temas 1–2.) |
| II | 13–26 (clases 049–099; sin clases de este curso en la semana 16) | 51 | 4 (evidencia 3); 2 como apoyo | Seno y coseno en el círculo unitario; ángulos y números de referencia; valores para ángulos no agudos; signos por cuadrante; las otras cuatro funciones (tangente, cotangente, secante, cosecante); identidades fundamentales, pitagóricas y de cofunciones; dominio y rango expresados con intervalos. (Módulo, Temas 3 y los dos «Tema 4».) **Por decidir:** ley del seno y del coseno (triángulos oblicuángulos) — el módulo no la trae y el DBA no la nombra. |
| III | 27–37 (clases 100–143) | 44 | 4 (evidencias 2, 4 y 5); 6 y 7 como apoyo | Gráficas de seno, coseno, tangente y secante; periodo, amplitud y desplazamientos; modelado de fenómenos periódicos (rueda, péndulo, respiración, mareas, marca en un disco como en el ejemplo del DBA 4); la tangente como pendiente de una recta y razón de cambio; ecuaciones trigonométricas sencillas. (Módulo, Tema 5 y «La función tangente y la pendiente».) |

## Ritmo de evaluación (propuesto)

- **Taller** el jueves en la sesión de las 13:40 (H8), casi todas las semanas: después del
  almuerzo conviene trabajo práctico en grupo.
- **Quiz** de ~20 min el viernes de la semana en que cierra un subtema (4 en el trimestre I).
- **Tarea** asignada el viernes y revisada el martes siguiente (una por semana).
- La **última semana de cada trimestre** es de repaso y evaluación del periodo: sin taller,
  sin quiz y sin tarea nueva.
- Semanas 01–02: ya dictadas, sin DBA ni marcas (diagnóstico y refuerzo, no contenido nuevo).

## Hilos conductores del trimestre I (elegir uno)

Registro juvenil (grados 7–11). Los hechos marcados con † se verifican contra fuente antes de
escribir la guía, como pide `crear-guia`.

| | Hilo | Qué recorre | Por qué encaja |
|---|---|---|---|
| **A (recomendado)** | **Medir lo inalcanzable** | Tales y la altura de la pirámide por la sombra (anécdota que cuentan Diógenes Laercio y Plutarco siglos después †) → Eratóstenes y la circunferencia de la Tierra con el ángulo de la sombra en Siena y Alejandría (conocido por Cleómedes; el valor del estadio es incierto †) → Hiparco y la primera tabla de cuerdas (†, «padre de la trigonometría» es un título tradicional) → la Misión Geodésica Francesa (1735–1744: La Condamine, Bouguer, Godin, con Jorge Juan y Antonio de Ulloa) que midió por triangulación un arco de meridiano cerca de Quito † → la Comisión Corográfica de Agustín Codazzi en la Nueva Granada (desde 1850 †). | Cada paso es un subtema: semejanza (Tales, que conecta con el refuerzo de la semana 02) → razones → resolución de triángulos → medición indirecta → arcos y radianes (Eratóstenes). Permite un taller de medición en el patio con clinómetro casero. |
| B | **De la cuerda al seno** | La historia de la palabra «seno»: cuerdas de Hiparco y Ptolomeo (*Almagesto*) → la media cuerda *jyā/jīvā* de Aryabhata (c. 499) → *jība* en árabe, leída como *jayb* («bolsillo, pliegue») → *sinus* en las traducciones latinas del siglo XII (se suele atribuir a Gerardo de Cremona o a Roberto de Chester; atribución discutida †). | Muy buen gancho para el paso del triángulo al círculo unitario (el seno como media cuerda); algo más débil para aplicaciones. |
| C | **Navegar sin GPS** | Latitud por la altura de la estrella Polar o del Sol al mediodía, astrolabio y cuadrante náuticos †, cartas de navegación; el meridiano y los grados–minutos–segundos. Cierre: por qué el GPS no usa triangulación sino trilateración (distancias). | Motiva el sistema sexagesimal, los ángulos de elevación y la longitud de arco (millas náuticas †); se cruza con las coordenadas geográficas que vio Geometría 10°. |

**Recomendación: A.** Es el que mejor sigue el orden de los temas del trimestre, parte del
refuerzo de semejanza que ya se hizo, trae historia colombiana/latinoamericana y da pie a una
actividad de medición real.

## Recursos principales

- `recursos/matematicas/Guías pedagógicas Matemáticas/10 - Modulo_Matematicas_Decimo.docx`
  (leer en `markdown/`), de Adriana Quintero Palomino, «Conceptos de las funciones
  trigonométricas y la resolución de triángulos». Tema 1 (triángulo rectángulo, ángulos
  especiales, aplicaciones del río y el campanario) y Tema 2 (ángulos, radianes, arco, sector,
  círculo unitario) → **trimestre I**; Tema 3, Tema 4 (otras funciones) y Tema 4 (cálculo de
  valores) → **trimestre II**; Tema 5 (gráficas) → **trimestre III**. Tiene dos temas numerados
  «4» y usa millas y pies: verificar y adaptar cada ejercicio.
- Banco (`python3 tools/ejercicios.py listar --grado 10`), del mismo módulo:
  `razones-trigonometricas-10` (60), `angulos-radianes-10` (71) → trimestre I;
  `circulo-unitario-10` (95), `otras-funciones-trigonometricas-10` (86),
  `valores-trigonometricos-10` (78) → trimestre II; `graficas-trigonometricas-10` (54),
  `rectas-inclinacion-10` (7) → trimestre III.
- `recursos/matematicas/icfes/`: *Guía de orientación Saber 11.º 2026-1* y cuadernillo de
  marzo de 2026 (pregunta 29, y las 22–23 que están en `icfes-cuadernillo-2026-geometria.py`
  asignadas a Geometría 11°). Solo textuales y con crédito.

## Pendientes y preguntas para la docente

1. ¿Trigonometría 10° toma como apoyo los DBA 1, 2, 3, 6 y 7 (no hay Álgebra ni Cálculo en 10°)?
   En la tabla sesión por sesión solo aparece el DBA 1 en dos sesiones (√2, √3 y π).
2. Reparto con Geometría 10°: ¿razones trigonométricas y pendiente/ángulo de inclinación van
   aquí, como se propone?
3. ¿Entran la ley del seno y la ley del coseno (trimestre II)? No hay recurso ni ejercicios.
4. Ritmo de evaluación: ¿taller el jueves de las 13:40 y quiz el viernes?
5. Hilo del trimestre I: A, B o C.
6. De `recursos/banco/PENDIENTES.md`, lo que toca a este curso: las 29 preguntas abiertas de
   Matemáticas 10° por aprobar; las posibles erratas T2-14b «(18/13π)°» y resumen 6b
   «cos 1312» (¿radianes o grados?); y si se pasan a unidades colombianas los problemas en
   millas y pies. La pregunta 29 del cuadernillo Icfes no está en el banco.

## Semanas 01–02 (ya dictadas)

Registradas en `programacion.csv` el 2026-09-14 según `bitacora-2026-2027.md`, sin DBA ni
marcas. La bitácora no dice qué se hizo en cada sesión, así que el mismo tema y subtema se
repite en las cuatro filas de cada semana:

- 001–004 (semana 01): «Inicio de año y diagnóstico» — actividades de inicio de año, dinámicas
  de grupo y prueba diagnóstica.
- 005–008 (semana 02): «Refuerzo según el diagnóstico» — semejanza de triángulos y teorema de
  Pitágoras: conceptos, ejercicios y puesta en común.

## Propuesta del trimestre I, sesión por sesión

Sin escribir en `programacion.csv` hasta que la docente la apruebe. DBA: «4» = matemáticas
grado 10, DBA 4; «1;4» depende de la pregunta 1. Receso escolar del 12 al 16 de octubre entre
las semanas 06 y 07.

| Clase | Fecha | Tema | Subtema | DBA | Quiz | Taller | Tarea |
|---|---|---|---|---|---|---|---|
| **Semana 01** | | | | | | | |
| 001 | 2026-09-01 mar | Inicio de año y diagnóstico | (dictada) actividades de inicio y prueba diagnóstica | | | | |
| 002 | 2026-09-03 jue | Inicio de año y diagnóstico | (dictada) | | | | |
| 003 | 2026-09-03 jue | Inicio de año y diagnóstico | (dictada) | | | | |
| 004 | 2026-09-04 vie | Inicio de año y diagnóstico | (dictada) | | | | |
| **Semana 02** | | | | | | | |
| 005 | 2026-09-08 mar | Refuerzo según el diagnóstico | (dictada) semejanza de triángulos y Pitágoras | | | | |
| 006 | 2026-09-10 jue | Refuerzo según el diagnóstico | (dictada) | | | | |
| 007 | 2026-09-10 jue | Refuerzo según el diagnóstico | (dictada) | | | | |
| 008 | 2026-09-11 vie | Refuerzo según el diagnóstico | (dictada) | | | | |
| **Semana 03** | | | | | | | |
| 009 | 2026-09-15 mar | Razones trigonométricas | Ángulos: sistema sexagesimal (grados, minutos, segundos) y clasificación | 4 | | | |
| 010 | 2026-09-17 jue | Razones trigonométricas | De la semejanza a la razón: en triángulos rectángulos semejantes la razón depende solo del ángulo | 4 | | | |
| 011 | 2026-09-17 jue | Razones trigonométricas | Taller: medir lados en triángulos semejantes y comparar sus razones | 4 | | x | |
| 012 | 2026-09-18 vie | Razones trigonométricas | Definición de seno, coseno y tangente (cateto opuesto, adyacente, hipotenusa) | 4 | | | x |
| **Semana 04** | | | | | | | |
| 013 | 2026-09-22 mar | Razones trigonométricas | Cálculo de razones dados dos lados (con Pitágoras) | 4 | | | |
| 014 | 2026-09-24 jue | Razones trigonométricas | Dada una razón, hallar las otras con un triángulo auxiliar | 4 | | | |
| 015 | 2026-09-24 jue | Razones trigonométricas | Taller de cálculo de razones | 4 | | x | |
| 016 | 2026-09-25 vie | Razones trigonométricas | La calculadora científica: modo grados, razones y ángulo a partir de la razón | 4 | | | x |
| **Semana 05** | | | | | | | |
| 017 | 2026-09-29 mar | Ángulos especiales | 30° y 60° a partir del triángulo equilátero | 4 | | | |
| 018 | 2026-10-01 jue | Ángulos especiales | 45° a partir del triángulo rectángulo isósceles; √2 y √3 como irracionales | 1;4 | | | |
| 019 | 2026-10-01 jue | Ángulos especiales | Taller: tabla de valores exactos y ejercicios | 4 | | x | |
| 020 | 2026-10-02 vie | Ángulos especiales | Quiz de razones y ángulos especiales; ejercicios | 4 | x | | x |
| **Semana 06** | | | | | | | |
| 021 | 2026-10-06 mar | Resolución de triángulos rectángulos | Resolver dados dos lados | 4 | | | |
| 022 | 2026-10-08 jue | Resolución de triángulos rectángulos | Resolver dados un lado y un ángulo agudo | 4 | | | |
| 023 | 2026-10-08 jue | Resolución de triángulos rectángulos | Taller de resolución de triángulos | 4 | | x | |
| 024 | 2026-10-09 vie | Resolución de triángulos rectángulos | Ángulos de elevación y de depresión | 4 | | | x |
| **Semana 07** | | | | | | | |
| 025 | 2026-10-20 mar | Aplicaciones del triángulo rectángulo | Repaso tras el receso; medición indirecta (el ancho de un río) | 4 | | | |
| 026 | 2026-10-22 jue | Aplicaciones del triángulo rectángulo | Problemas con dos triángulos (altura de un campanario o edificio) | 4 | | | |
| 027 | 2026-10-22 jue | Aplicaciones del triángulo rectángulo | Taller de medición en el patio con clinómetro casero | 4 | | x | |
| 028 | 2026-10-23 vie | Aplicaciones del triángulo rectángulo | Quiz de resolución de triángulos y aplicaciones | 4 | x | | x |
| **Semana 08** | | | | | | | |
| 029 | 2026-10-27 mar | Ángulos como rotación | Lado inicial y terminal, sentido positivo y negativo, posición estándar y cuadrantes | 4 | | | |
| 030 | 2026-10-29 jue | Ángulos como rotación | Ángulos coterminales y ángulos mayores de 360° | 4 | | | |
| 031 | 2026-10-29 jue | Ángulos como rotación | Taller de ángulos en posición estándar | 4 | | x | |
| 032 | 2026-10-30 vie | Radianes | El radián: ángulo cuyo arco mide un radio | 4 | | | x |
| **Semana 09** | | | | | | | |
| 033 | 2026-11-03 mar | Radianes | Conversión entre grados y radianes | 4 | | | |
| 034 | 2026-11-05 jue | Radianes | Ángulos notables en radianes; π como número irracional en la recta | 1;4 | | | |
| 035 | 2026-11-05 jue | Radianes | Taller de conversión | 4 | | x | |
| 036 | 2026-11-06 vie | Radianes | Quiz de ángulos en posición estándar y radianes | 4 | x | | x |
| **Semana 10** | | | | | | | |
| 037 | 2026-11-10 mar | Arco y sector circular | Longitud de arco s = rθ | 4 | | | |
| 038 | 2026-11-12 jue | Arco y sector circular | Área del sector circular | 4 | | | |
| 039 | 2026-11-12 jue | Arco y sector circular | Taller: la medición de la Tierra de Eratóstenes y problemas de arco | 4 | | x | |
| 040 | 2026-11-13 vie | Arco y sector circular | Problemas de arco y sector (ruedas, relojes, latitudes) | 4 | | | x |
| **Semana 11** | | | | | | | |
| 041 | 2026-11-17 mar | Círculo unitario | El círculo unitario y los ángulos en posición estándar | 4 | | | |
| 042 | 2026-11-19 jue | Círculo unitario | Seno y coseno como coordenadas del punto (ángulos agudos y cuadrantales) | 4 | | | |
| 043 | 2026-11-19 jue | Círculo unitario | Taller del círculo unitario | 4 | | x | |
| 044 | 2026-11-20 vie | Círculo unitario | Quiz de arco, sector y círculo unitario; guía de repaso | 4 | x | | x |
| **Semana 12 — evaluación** | | | | | | | |
| 045 | 2026-11-24 mar | Repaso y evaluación | Repaso general del trimestre (razones y triángulos) | 4 | | | |
| 046 | 2026-11-26 jue | Repaso y evaluación | Repaso general (ángulos, radianes, arco) y dudas | 4 | | | |
| 047 | 2026-11-26 jue | Repaso y evaluación | Evaluación del periodo | 4 | | | |
| 048 | 2026-11-27 vie | Repaso y evaluación | Socialización de la evaluación y cierre del trimestre | 4 | | | |

Totales: 9 talleres, 4 quices, 9 tareas; 36 sesiones de contenido (009–044) y 4 de cierre.
