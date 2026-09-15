# Plan de la guía — Geometría 11° · Trimestre I (etapas A y B)

> **Generación rápida (2026-09-14/15):** etapas A, B y C del skill `crear-guia` en una sola
> pasada, a pedido del usuario, sin esperar las revisiones de la docente. **El plan anual y el
> plan del trimestre son una propuesta pendiente de aprobación.**

## Datos

| | |
|---|---|
| Asignatura | Geometría |
| Grado | 11° |
| Trimestre | I (semanas 01–12; una sesión semanal, viernes, 40 min) |
| Archivo | `guia-periodo-I-hiperbola-navegacion.tex` (13 páginas) |
| Título | Coordenadas, lugares geométricos y la hipérbola |
| Hilo | **LORAN: encontrar un barco con dos hipérbolas** (opción A del plan anual) |
| DBA | Matemáticas grado 11 · DBA 6 y DBA 4 |

## Por qué este hilo

Continúa la investigación que la docente dejó en la sesión 002 («la hipérbola y LORAN»), así que
los estudiantes ya tienen la pregunta. Cada tema es un paso real del sistema: ubicar estaciones y
barcos en un plano (coordenadas), los puntos a igual distancia o a igual tiempo (circunferencia y
mediatriz), la diferencia de distancias constante (hipérbola) y el cruce de dos líneas de posición,
con la precisión como tema de medición (DBA 4). Es historia verificable y reciente (1940–2010), y
enlaza con el GPS del trimestre III. Científica: **Gladys West** (modelo de la forma de la Tierra
para el GPS). Hipatia se menciona con cautela: la Suda le atribuye un comentario a las
*Cónicas*, pero los historiadores lo dudan.

## Temas (propuesta del trimestre I; sin inicio, repaso ni evaluación)

| # | Tema | Sesiones | `\label` | DBA |
|---|---|---|---|---|
| — | Investigación: la hipérbola y LORAN | 002 (dictada) | — | en la Introducción, como la pregunta del trimestre |
| 1 | Coordenadas cartesianas | 003–004 | `tema:coordenadas` | 6 |
| 2 | Lugares geométricos | 005–006 | `tema:lugares` | 6 |
| 3 | La hipérbola | 007–008 | `tema:hiperbola` | 6 |
| 4 | Navegación hiperbólica | 009–010 | `tema:navegacion` | 6, 4 |

**Hipérbola 10°/11°:** se presenta completa, desde la definición, «porque la necesitamos para
LORAN», sin suponer que se vio en 10° (allí está propuesta para el trimestre III).

## DBA y evidencias (texto literal de `dba/matematicas/grados/grado11.tex`)

**DBA 6** — «Modela objetos geométricos en diversos sistemas de coordenadas (cartesiano, polar,
esférico) y realiza comparaciones y toma decisiones con respecto a los modelos.»

| Evidencia | Tema | Ejercicios |
|---|---|---|
| Reconoce y utiliza distintos sistemas de coordenadas para modelar. | 1, 4 | medicion-11-002/005, navegacion-11-003 (solo cartesianas; polares y esféricas en II y III) |
| Compara objetos geométricos, a partir de puntos de referencia diferentes. | 1 | solo el ejemplo resuelto — **pendiente** (cabe `coordenadas-11-003` cuando se registre) |
| Explora el entorno y lo representa mediante diversos sistemas de coordenadas. | 2, 4 | lugares-geometricos-11-003/004, navegacion-11-003 |

**DBA 4** — «Interpreta y diseña técnicas para hacer mediciones con niveles crecientes de
precisión (uso de diferentes instrumentos para la misma medición, revisión de escalas y rangos de
medida, estimaciones, verificaciones a través de mediciones indirectas).»

| Evidencia | Tema | Ejercicios |
|---|---|---|
| Interpreta la rapidez como una razón de cambio entre dos cantidades. | 4 | navegacion-11-005 (Δd = c·Δt), lugares-geometricos-11-003 |
| Justifica la precisión de una medición directa o indirecta… | 1, 4 | medicion-11-001, navegacion-11-005 |
| Establece conclusiones pertinentes con respecto a la precisión… en contextos específicos. | 4 | navegacion-11-005 |
| Determina las unidades e instrumentos adecuados para mejorar la precisión. | — | **pendiente** (nada en el banco) |
| Reconoce la diferencia entre la precisión y la exactitud. | 4 | navegacion-11-005 |

## Frase introductoria

Descartes, *La Géométrie* (1637), primera frase del libro I (trad. propia).

## Marco teórico (redactado en la guía)

1. Apolonio de Perga (c. 262–190 a. C.), *Cónicas* (8 libros), nombres de las cónicas. Hipatia,
   con la cautela anotada.
2. Descartes (1637): la geometría con coordenadas.
3. LORAN: Loomis (oct. 1940); MIT Radiation Laboratory; Gee británico; Montauk Point y Fenwick
   Island (jun. 1942); la Armada desde el 1 ene. 1943; ~700 millas náuticas de día y 1 400 de
   noche, errores ~1 % de la distancia; LORAN-C (años 70), errores de cientos de pies; apagado
   anunciado desde el 8 feb. 2010.
4. Gladys West (Dahlgren; geoide para el GPS; Salón de la Fama, 2018).
5. c = 299 792 458 m/s exacta → 0,3 km/µs.

## Por tema

| Tema | Paso del hilo | Explicación y ejemplo | Aplicación |
|---|---|---|---|
| 1 | Montauk y Fenwick en un mapa | distancia (Pitágoras), punto medio; ejemplo: mismo barco con dos orígenes | coordenadas del celular |
| 2 | Un pulso: circunferencia; dos pulsos a la vez: mediatriz | circunferencia, mediatriz; ejemplo: completar cuadrados | cobertura de una antena |
| 3 | Un pulso llega antes: diferencia de distancias constante | definición, ecuación canónica, c² = a² + b², asíntotas; ejemplo focos (±5, 0) y 2a = 6, con gráfica | localizar un sonido con micrófonos |
| 4 | Dos pares, dos hipérbolas, un punto | Δd = v·Δt, línea de posición; ejemplo Δt = 400 µs; precisión y exactitud | del LORAN al GPS |

Los ejemplos resueltos (no son ejercicios) se comprobaron con SymPy fuera del banco.

## Etapa B — ejercicios (regla de la docente, 2026-09-15: solo banco)

Solo ejercicios con estado `verificado`, salvo donde el banco no tenía nada (excepción aclarada por
el usuario). Nuevos: **4** (hipérbola y navegación, temas sin ningún ejercicio en el banco), y
2 de `lugares-geometricos-11.py` (escrito en esta sesión y que ya cita la guía de 10°; la
circunferencia y la mediatriz no tenían nada verificado para 11°). Todos pasan `--sin-registro`
(0 fallas); falta que una sesión corra `verificar` para registrarlos.

| Tema | Id | Enunciado (corto) | Respuesta | Estado |
|---|---|---|---|---|
| 1 | medicion-11-005 | Perímetro del terreno por coordenadas | 8 + 3√5 + √13 ≈ 18,31 m | verificado |
| 1 | medicion-11-002 | Área del pentágono por triangulación | 14 cm² | verificado |
| 1 | medicion-11-001 | Área con regla frente a exacta | 9,5125 / 9,5; 0,13 % | verificado |
| 2 | **N lugares-geometricos-11-003** | Pulso de 200 µs: circunferencia | 60 km; x² + y² = 3 600 | pasa `--sin-registro` |
| 2 | **N lugares-geometricos-11-004** | Mediatriz de (0,0)–(8,4) | y = −2x + 10 | pasa `--sin-registro` |
| 2 | icfes-cuadernillo-2026-037 | Circunferencia: P, P′, O (textual) | b | verificado |
| 3 | **N hiperbola-11-002** | Elementos de x²/16 − y²/9 = 1 | a=4, b=3, c=5 | pasa `--sin-registro` |
| 3 | **N hiperbola-11-004** | Error: c² = a² − b² | c = 5 | pasa `--sin-registro` |
| 4 | **N navegacion-11-003** | Cruce de dos hipérbolas | (12/√7, 12/√7) ≈ (454, 454) km | pasa `--sin-registro` |
| 4 | **N navegacion-11-005** | Precisión frente a exactitud | 120 km; 120 m; 1,5 km | pasa `--sin-registro` |
| S11 | icfes-cuadernillo-2026-032 | Trapecio isósceles (textual) | b | verificado |
| S11 | icfes-cuadernillo-2026-050 | Tres empaques (textual, con figura) | a | verificado |
| S11 | icfes-cuadernillo-2026-017 | Aristas de la caja (textual, con figura) | d | verificado |

No se usa `medicion-11-008…011` (decisión Pitágoras 9°/11°). No se usan los de
`geometria-analitica-10` (guía de 10°, sin registrar).

**Archivos restaurados a pedido del coordinador** (los cita la guía de Geometría 10°; se habían
borrado en esta sesión y se recrearon idénticos): `coordenadas-11.py` (ids 001–005) y
`lugares-geometricos-11.py` (ids 001–005); 10 de 10 pasan `--sin-registro`.

**Pendientes (evidencias sin ejercicio del banco):** comparar objetos desde puntos de referencia
distintos (DBA 6); unidades e instrumentos para mejorar la precisión (DBA 4).

## Referencias (verificadas 2026-09-14/15)

| Clave | Referencia | Veredicto | URL |
|---|---|---|---|
| descartes | Descartes, *La Géométrie* (1637), libro I, primera frase | confirmada (texto en Project Gutenberg) | https://www.gutenberg.org/ebooks/26400 |
| mactutorapolonio | MacTutor, *Apollonius of Perga* | confirmada: c. 262–190 a. C., 8 libros, nombres de las cónicas | https://mathshistory.st-andrews.ac.uk/Biographies/Apollonius/ |
| mactutorhipatia | MacTutor, *Hypatia of Alexandria* | confirmada: la Suda y la duda de los historiadores | https://mathshistory.st-andrews.ac.uk/Biographies/Hypatia/ |
| merrill | Merrill, J. (2006, enero). LORAN showing the way… Part I 1940–1942. *The Submarine Review* | confirmada (fechas, alcances, 1 %) | https://archive.navalsubleague.org/2006/loran-showing-the-way-long-range-navigation-land-sea-air-part-i-1940-1942 |
| noaa | Office of Coast Survey (NOAA), *Navigating waters before GPS…* | confirmada | https://nauticalcharts.noaa.gov/updates/navigating-waters-before-gps-why-some-mariners-still-refer-to-loran-c/ |
| fedreg | U.S. Coast Guard (2010, 7 ene.). *Federal Register* 75 FR 998 | confirmada | https://www.federalregister.gov/documents/2010/01/07/2010-83/terminate-long-range-aids-to-navigation-loran-c-signal |
| west | *Gladys West*, Encyclopaedia Britannica | confirmada (y Military Times, ene. 2026) | https://www.britannica.com/biography/Gladys-West |
| nist | NIST CODATA, *speed of light in vacuum* | confirmada (exacta) | https://physics.nist.gov/cgi-bin/cuu/Value?c |
| mendba, icfes2026 | como en 9° | confirmadas | — |

Corregido respecto al plan anual: «1 µs ≈ 300 m» queda como cálculo propio, no como dato
histórico; las cifras de alcance y precisión son las verificadas arriba. El ETHW no sirvió como
evidencia (bloquea la lectura automática).

## Preguntas para la docente

1. Aprobar temas, hilo y DBA; ¿se socializa la investigación en la sesión 003?
2. Hipérbola completa en 11° (como aquí) o supuesta de 10°.
3. Registrar los ejercicios nuevos (`python3 tools/ejercicios.py verificar`) y decidir si
   `coordenadas-11-003` entra para la evidencia de puntos de referencia distintos.
