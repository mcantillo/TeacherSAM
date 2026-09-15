# Plan de la guía — Geometría 10° · Trimestre I (etapas A y B)

> **Generación rápida (2026-09-14):** etapas A, B y C del skill `crear-guia` en una sola pasada,
> sin esperar las revisiones de la docente. **El plan del trimestre es una propuesta pendiente
> de aprobación** (`curriculo/plan-anual.md`; en `programacion.csv` solo está llena la sesión
> 001). Todo lo de aquí se ajusta cuando la docente apruebe temas, subtemas e hilo.

## Datos

| | |
|---|---|
| Asignatura | Geometría |
| Grado | 10° |
| Trimestre | I (sesiones 001–009, semanas 02–12; una sesión semanal de 40 min) |
| Archivo | `guia-periodo-I-geometria-analitica.tex` |
| Título | El plano cartesiano y la recta |
| Hilo | **Ubicarse en la Tierra: de las coordenadas geográficas al plano cartesiano** (opción A del plan anual) |
| Registro | Juvenil (7°–11°): definiciones formales, notación, citas con fuente, justificar |
| Recurso | **No hay recurso aprobado para Geometría 10°** en `recursos/`: la teoría se redactó aquí; los ejercicios se reutilizan del banco (9°, 11°, 5° e Icfes) y solo 4 son nuevos (ver etapa B) |

## Por qué este hilo

Es el que mejor continúa lo que ya pasó en clase: la sesión 001 fue un video sobre
coordenadas geográficas. Latitud y longitud son dos números que fijan un lugar, exactamente
como $(x, y)$ en el plano; cada tema del trimestre responde una pregunta de «ubicarse»:
¿dónde está? (plano cartesiano), ¿a qué distancia y dónde nos encontramos? (distancia y punto
medio), ¿qué lugares cumplen una condición? (lugares geométricos: cobertura de una antena,
un punto a igual distancia de dos estaciones) y ¿cómo describo un camino recto? (la recta). Todos
los datos del hilo son verificables (Alcaldía de Cali, NOAA, NASA, MacTutor), sin leyendas.
Frente a la opción B (Descartes y Fermat) tiene contextos más cercanos (Cali, mapas, rutas), y
Descartes y Fermat entran igual en el marco teórico; la C (Eratóstenes) queda para
Trigonometría, cuyo hilo propuesto ya la usa.

## DBA y evidencias

Fuente: `dba/matematicas/grados/grado10.tex` (texto literal).

**DBA 5** — «Explora y describe las propiedades de los lugares geométricos y de sus
transformaciones a partir de diferentes representaciones.»

| Evidencia | Tema que la atiende |
|---|---|
| Localiza objetos geométricos en el plano cartesiano. | 1 (puntos, cuadrantes, polígonos), 2 (triángulos) |
| Identifica las propiedades de lugares geométricos a través de sus representación en un sistema de referencia. | 3 (mediatriz, circunferencia), 4 (recta; paralelas y perpendiculares) |
| Utiliza las expresiones simbólicas de las cónicas y propone los rangos de variación para obtener una gráfica requerida. | — (trimestres II y III) |
| Representa lugares geométricos en el plano cartesiano, a partir de su expresión algebraica. | 3 (ecuación de la circunferencia), 4 (graficar la recta desde su ecuación) |

**Reparto con Trigonometría 10°:** la recta (pendiente como razón, ecuaciones, paralelas y
perpendiculares) va aquí; el ángulo de inclinación y $m = \tan\theta$ se quedan en
Trigonometría y **no se enseñan** en esta guía. Tampoco se repiten semejanza ni la
demostración de Pitágoras (reforzadas en Trigonometría en la semana 02): Pitágoras se usa
como herramienta.

## Frase introductoria

«Todos los problemas de geometría pueden reducirse fácilmente a tales términos que después no
es necesario conocer más que la longitud de algunas líneas rectas para construirlos.» —
René Descartes, *La Géométrie* (1637), libro primero, primera frase (trad. propia). Original:
«Tous les Problesmes de Geometrie se peuuent facilement reduire a tels termes, qu'il n'est
besoin par aprés que de connoitre la longueur de quelques lignes droites, pour les construire.»

Por qué esta: es la primera línea del libro que fundó la geometría analítica, y dice justo lo
que hará el trimestre: convertir problemas de ubicación en longitudes (distancias) y rectas.

## Marco teórico (redactado)

**Dos números para un lugar.** Hiparco de Nicea (c. 190–120 a. C.) comenzó a usar de manera
sistemática la latitud y la longitud —que ya empleaba en su catálogo de estrellas— para fijar
lugares sobre la superficie de la Tierra [ebsco; mactutorhiparco]. La latitud dice qué tan al
norte o al sur del ecuador está un lugar; la longitud, qué tan al oriente o al occidente de un
meridiano de referencia. Hoy, por ejemplo, la Alcaldía ubica a Cali en 3°27′00″ N y
76°32′00″ O [alcaldia].

**Del globo al plano.** La Tierra es casi una esfera, pero en un mapa de una ciudad o de una
región pequeña podemos tratarla como plana, con una cuadrícula. Cada grado de latitud equivale a
unos 111 km [noaa]. Esa idea —dos rectas perpendiculares y dos números— es la del plano
cartesiano.

**Descartes y Fermat.** En 1637 René Descartes publicó en Leiden el *Discurso del método* con
tres apéndices; uno era *La Géométrie*, la parte más importante, donde aplicó el álgebra a la
geometría [mactutordescartes; descartes]. Pierre de Fermat había llegado antes, de forma
independiente, a un sistema casi idéntico: su *Introducción a los lugares planos y sólidos*
(*Ad locos planos et solidos isagoge*) ya estaba escrita en la primavera de 1636 y circuló en
manuscrito; en ella la ecuación más sencilla, $Dx = Ey$, representa una recta [mahoney]. Se
publicó después de su muerte, en 1679, en sus *Varia opera mathematica* [fermat]. De ahí viene
la expresión «lugar geométrico».

**Katherine Johnson.** Matemática de la NASA (1918–2020). En 1960 escribió con Ted Skopinski el
informe *Determination of Azimuth Angle at Burnout for Placing a Satellite Over a Selected
Earth Position*, con las ecuaciones de un vuelo orbital en el que se especifica el lugar de
aterrizaje de la nave [nasajohnson; skopinski]. Hizo el análisis de trayectoria del vuelo de
Alan Shepard (1961) y, en 1962, verificó a mano las ecuaciones orbitales del vuelo de John
Glenn; en 2015 recibió la Medalla Presidencial de la Libertad [nasajohnson]. Su trabajo fue,
literalmente, ubicar puntos sobre la Tierra con ecuaciones.

**Hipatia** (anuncio del trimestre II): hacia el año 400 enseñaba matemáticas en Alejandría;
las fuentes antiguas le atribuyen un comentario a las *Cónicas* de Apolonio [dzielska].

## Temas

Los temas vienen de la **propuesta** del plan anual (las filas del CSV aún están vacías).

### Tema 1 — Plano cartesiano · `tema:planocartesiano`

Sesiones 001–002. Evidencia 1.
- **Hilo:** Hiparco y la latitud y longitud; de la esfera a la cuadrícula del mapa.
- **Explicación:** ejes, origen, pareja ordenada, cuadrantes; puntos sobre los ejes; polígonos
  en el plano. Ejemplo resuelto: cuadrantes y ejes de cinco puntos (figura).
- **Aplicación:** las coordenadas de Cali como punto del plano (longitud → $x$, latitud → $y$).
- **Ejercicios:** distancias en una cuadrícula (diagnóstico); cambio de origen (qué cambia y qué
  no); Cali en grados decimales.

### Tema 2 — Distancia entre dos puntos · `tema:distancia`

Sesiones 003–004. Evidencia 1. Incluye el punto medio (subtema de la 004).
- **Hilo:** medir en el mapa: a qué distancia y dónde encontrarse.
- **Explicación:** fórmula de la distancia desde Pitágoras (figura); punto medio como promedio;
  clasificar triángulos por sus lados y comprobar el ángulo recto con el recíproco de Pitágoras.
- **Aplicación:** 1° de latitud ≈ 111 km; distancia norte–sur entre dos lugares del mismo meridiano.
- **Ejercicios:** distancia y punto medio (3 casos); demostrar que un triángulo es isósceles y
  rectángulo (argumentación); dron de rescate (contexto).

### Tema 3 — Lugares geométricos · `tema:lugaresgeometricos`

Sesión 005. Evidencias 2 y 4.
- **Hilo:** Fermat y los «lugares»: todos los puntos que cumplen una condición.
- **Explicación:** definición de lugar geométrico; mediatriz (ecuación desde $PA = PB$);
  circunferencia $(x - h)^2 + (y - k)^2 = r^2$ (figura).
- **Aplicación:** la zona de cobertura de una antena (idealizada como círculo).
- **Ejercicios:** pulso de radio (dónde puede estar el barco: circunferencia); encuentra el
  error (Pedro confunde circunferencia y mediatriz).

### Tema 4 — La recta · `tema:recta`

Sesiones 006–008. Evidencias 2 y 4. Sin ángulo de inclinación.
- **Hilo:** Katherine Johnson y las trayectorias; el camino más sencillo es la recta.
- **Explicación:** pendiente como razón de cambio; rectas crecientes, decrecientes, horizontales
  y verticales; formas punto-pendiente, pendiente-intercepto y general; graficar desde la
  ecuación (figura); paralelas ($m_1 = m_2$) y perpendiculares ($m_1 m_2 = -1$).
- **Aplicación:** la ruta recta de un bus en el mapa (sin cálculos: sustituir en la ecuación).
- **Ejercicios:** recta por dos puntos; paralela y perpendicular; horizontal y vertical;
  ni paralelas ni perpendiculares; encuentra el error (cociente invertido).

## Prepárate para Saber 11

Tres preguntas del Icfes transcritas **textualmente** y acreditadas (cuadernillo de marzo de
2026, preguntas 8, 20 y 32; ya verificadas en el banco). Respuestas solo en el informe: c, a, b.
No se redactaron preguntas propias (regla del 2026-09-15: reutilizar antes que escribir).

## Cierre del hilo

De Hiparco a Katherine Johnson: dos números bastan para ubicar un lugar, y con ellos medimos
distancias, describimos zonas y trazamos caminos. Anuncio del trimestre II: la circunferencia y
la parábola como lugares geométricos (Hipatia y las *Cónicas* de Apolonio).

## Evaluación (borrador de la matriz)

- **Saber:** reconoce los elementos del plano cartesiano y las fórmulas de distancia, punto
  medio, pendiente y ecuaciones de la recta y de la circunferencia.
- **Hacer:** ubica figuras, calcula distancias y puntos medios, encuentra mediatrices,
  circunferencias y rectas, y las grafica.
- **Ser:** justifica sus resultados comprobándolos en el plano.
- **Convivir:** comparte estrategias y revisa con respeto el trabajo de otros.

## Referencias (verificadas el 2026-09-14)

| Clave | Referencia | Veredicto | Corrección | URL |
|---|---|---|---|---|
| descartes (frase) | Descartes, R. (1637). *La Géométrie*, en *Discours de la méthode…* Leiden: Jan Maire, pp. 296–413 | confirmada: primera frase del libro primero | trad. propia | https://fr.wikisource.org/wiki/La_G%C3%A9om%C3%A9trie_(%C3%A9d._1637) |
| mactutordescartes | O'Connor y Robertson, *René Descartes*, MacTutor | confirmada: Leiden 1637, tres apéndices, *La Géométrie* la más importante | no menciona la mosca: la leyenda **no se usa** | https://mathshistory.st-andrews.ac.uk/Biographies/Descartes/ |
| mahoney | Mahoney, M. S. «Fermat, Pierre de», *Complete Dictionary of Scientific Biography* (Encyclopedia.com) | confirmada: *Isagoge* compuesta antes de la primavera de 1636, independiente de Descartes; $Dx = Ey$ recta | MacTutor no da las fechas; se usa esta fuente | https://www.encyclopedia.com/people/science-and-technology/mathematics-biographies/pierre-de-fermat |
| fermat | Fermat, P. de (1679). *Varia opera mathematica*. Toulouse: J. Pech | confirmada (ed. póstuma de su hijo Samuel) | — | https://archive.org/details/variaoperamathe00ferm |
| ebsco | EBSCO Research Starters, «Hipparchus» | confirmada: uso sistemático de latitud y longitud para lugares de la Tierra | «el primero en usarlas» (Britannica, 403 al abrirla) se cambia por «comenzó a usar de manera sistemática» | https://www.ebsco.com/research-starters/history/hipparchus |
| mactutorhiparco | O'Connor y Robertson, *Hipparchus*, MacTutor | confirmada: 190–120 a. C., Nicea | no habla de coordenadas terrestres: solo para las fechas | https://mathshistory.st-andrews.ac.uk/Biographies/Hipparchus/ |
| alcaldia | Alcaldía de Santiago de Cali, «Geografía de Cali» | confirmada: 3°27′00″N 76°32′00″O | el plan anual decía «aprox. 3,4° N, 76,5° O»: se usa el dato oficial (3,45°; 76,53°) | https://www.cali.gov.co/informatica/publicaciones/106104/geografia-de-cali/ |
| noaa | NOAA National Ocean Service, «What is latitude?» | confirmada: «Each degree of latitude covers about 111 kilometers» | — | https://oceanservice.noaa.gov/facts/latitude.html |
| nasajohnson | NASA, «Katherine Johnson Biography» | confirmada: 1918–2020, informe de 1960, Shepard 1961, Glenn 1962, Medalla 2015 | — | https://www.nasa.gov/centers-and-facilities/langley/katherine-johnson-biography/ |
| skopinski | Skopinski, T. H. y Johnson, K. G. (1960). NASA TN D-233 | confirmada (catálogo HathiTrust) | — | https://catalog.hathitrust.org/Record/011445470 |
| dzielska | Dzielska, M. (1995). *Hypatia of Alexandria*. Harvard UP | confirmada (ya usada en Álgebra 8°) | — | https://bmcr.brynmawr.edu/1995/1995.07.07/ · https://mathshistory.st-andrews.ac.uk/Biographies/Hypatia/ |
| icfes | Icfes (2026). *Cuadernillo de preguntas Matemáticas Saber 11.º* | archivo local | pregunta 32 textual | recursos/matematicas/icfes/09-Marzo_Cuadernillo-de-Preguntas-Matematicas-Saber-11-2026.pdf |
| mendba | MEN (2016). *DBA V.2: Matemáticas* | confirmada (ya usada) | — | https://gblumen.mineducacion.gov.co/cgi-bin/koha/opac-detail.pl?biblionumber=4785 |

**Quitado o no usado:** la anécdota de Descartes y la mosca (sin fuente contemporánea); el
valor de Eratóstenes (no hace falta en este hilo); «Hiparco fue el primero» (solo en Britannica,
que no se pudo abrir: se dice «comenzó a usar de manera sistemática»); «primera mujer con
crédito de autora en la División de Investigación de Vuelo» (de un resumen de búsqueda; la
página de la NASA consultada no lo dice).

## Etapa B — ejercicios (2026-09-14, rehecha el 2026-09-15)

Regla de la docente del 2026-09-15 («reutilizar, no multiplicar»): la guía usa sobre todo
ejercicios que ya estaban en el banco y **solo 4 nuevos**, en
`recursos/banco/matematicas/geometria-analitica-10.py` (verificados con `verificar
--sin-registro`; los otros 31 que se habían escrito el 2026-09-14 se descartaron antes de
registrarse, incluida la única abierta). La regla posterior de «ningún ejercicio nuevo» se aplica
solo a guías en curso: esta guía ya estaba terminada y se conserva así (decisión del usuario,
2026-09-15). **E** = ejemplo resuelto; **A** = aplicación; **S** = Saber 11.

| Tema | Uso | Id | Enunciado (corto) | Respuesta | Estado | Origen |
|---|---|---|---|---|---|---|
| 1 | E | geometria-analitica-10-002 | Cuadrante o eje de 5 puntos | II, IV, eje y, III, eje x | verificado | **nuevo**: no hay uno de cuadrantes con negativos para secundaria |
| 1 | 1 | plano-cartesiano-5-013 | ¿BN o AE es mayor? | BN = 6 > AE = 5 | verificado | reuso (5°, diagnóstico) |
| 1 | 2 | coordenadas-11-003 | Cambio de origen: puerto y faro | E′(−20, −10), B′(10, 30); EB = 50 en los dos | verificado* | reuso (11°) |
| 1 | 3 | geometria-analitica-10-006 | Cali en grados decimales | (−76,53; 3,45), II | verificado | **nuevo**: contexto del hilo (dato oficial) |
| 2 | E | coordenadas-11-001 | Distancia y punto medio A(−3, 2), B(5, 8) | 10; (1, 5) | verificado* | reuso (11°) |
| 2 | A | geometria-analitica-10-012 | 2°15′ N a 3°45′ N | ≈ 166,5 km | verificado | **nuevo**: contexto del hilo (NOAA) |
| 2 | 1 | coordenadas-11-002 | Distancia y punto medio, 3 casos | 5; 10; 3√2 | verificado* | reuso (11°) |
| 2 | 2 | coordenadas-11-004 | Triángulo isósceles rectángulo (argumentar) | AB = BC = 5, AC = √50 | verificado* | reuso (11°) |
| 2 | 3 | coordenadas-11-005 | Dron de rescate | 13 km; (8; 1,5); 15 min | verificado* | reuso (11°) |
| 3 | E | lugares-geometricos-11-004 | Mediatriz de A(0, 0), B(8, 4) | y = −2x + 10 | verificado* | reuso (11°) |
| 3 | E | lugares-geometricos-11-001 | Circunferencia (3, −2), r = 5 | (x − 3)² + (y + 2)² = 25 | verificado* | reuso (11°) |
| 3 | 1 | lugares-geometricos-11-003 | Pulso de radio: dónde está el barco | 60 km; x² + y² = 3 600 | verificado* | reuso (11°) |
| 3 | 2 | lugares-geometricos-11-005 | Error de Pedro: circunferencia vs. mediatriz | la mediatriz x = 3 | verificado* | reuso (11°) |
| 4 | E | funcion-lineal-9-046 | Pendiente (2, 5)–(6, 10) | 5/4 | verificado | reuso (9°) |
| 4 | E | funcion-lineal-9-060 | Recta por (5, 3) y (2, 8) | y = −5x/3 + 34/3 | verificado | reuso (9°) |
| 4 | E | funcion-lineal-9-011 | Graficar y = −2x + 4 | cortes (0, 4) y (2, 0) | verificado | reuso (9°) |
| 4 | 1 | funcion-lineal-9-061 | Recta por (4, −4) y (−8, 8) | y = −x | verificado | reuso (9°) |
| 4 | 2 | funcion-lineal-9-069 | Paralela y perpendicular a la anterior | p. ej. y = −5x/3; y = 3x/5 | verificado | reuso (9°) |
| 4 | 3 | funcion-lineal-9-094 | y = 5 y x = 4 | perpendiculares | verificado | reuso (9°) |
| 4 | 4 | funcion-lineal-9-095 | 2x + 3y = −2 y 3x − y = 4 | ninguna de las dos | verificado | reuso (9°) |
| 4 | 5 | geometria-analitica-10-030 | Error: cociente invertido | 2 | verificado | **nuevo**: el tema necesita un «encuentra el error» y el banco no lo tiene |
| S | 1 | icfes-cuadernillo-2026-008 | Montañistas: temperatura y altitud | c) | verificado | reuso (Icfes, textual) |
| S | 2 | icfes-cuadernillo-2026-020 | Publicidad y ganancia | a) | verificado | reuso (Icfes, textual) |
| S | 3 | icfes-cuadernillo-2026-032 | Trapecio isósceles simétrico | b) | verificado | reuso (Icfes, textual) |

\* `coordenadas-11` y `lugares-geometricos-11` son de la guía de Geometría 11° (otro agente,
2026-09-14) y aún no están registrados en `verificados.json`: sus comprobaciones pasan con
`verificar --sin-registro` (corrido aquí el 2026-09-15). Falta que una sesión corra `verificar`
para registrarlos, igual que los 4 nuevos. **Cruce para la docente:** Geometría 11° (DBA 6)
también trabaja distancia, punto medio, mediatriz y circunferencia en su trimestre I; conviene
decidir qué ve cada grado para no repetir los mismos ejercicios.
