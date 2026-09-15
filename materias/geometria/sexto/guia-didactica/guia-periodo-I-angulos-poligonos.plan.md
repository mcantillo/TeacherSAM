# Plan de la guía — Geometría 6° · Trimestre I (etapas A y B)

> **Generación rápida (2026-09-14/15):** etapas A, B y C del skill `crear-guia` en una sola
> pasada, sin esperar las revisiones de la docente. El plan del trimestre (`plan-anual.md`) es
> todavía una **propuesta**: todo lo que sigue queda en borrador hasta la Revisión 1.

## Datos

| | |
|---|---|
| Asignatura | Geometría |
| Grado | 6° |
| Trimestre | I (semanas 02–12; sesiones 001–009 de la propuesta de `plan-anual.md`, lunes, 50 min) |
| Archivo | `guia-periodo-I-angulos-poligonos.tex` |
| Título | La geometría del fútbol: ángulos y polígonos |
| Hilo | **La geometría del fútbol** (opción 1 de `plan-anual.md`) |
| Registro | 6°: juvenil y respetuoso, definiciones formales y notación, citas con fuente; justificar y primeras fórmulas |
| DBA | Matemáticas grado 6 · DBA 5 y DBA 6 (y DBA 4 en la construcción) |

## Por qué este hilo (y no los otros dos)

- **Es el ejemplo del propio DBA 5**: estimar y medir ángulos de tiro al arco. El módulo casi no
  trabaja la estimación, que es la evidencia más débil.
- **Todos los datos son verificables en fuentes oficiales**: las medidas del arco y de la cancha
  (IFAB, Regla 1) y el balón Telstar de 1970 con 12 pentágonos y 20 hexágonos (adidas).
- **Conecta de verdad con la matemática, de principio a fin**: ángulo de tiro (ángulos), líneas de
  la cancha (paralelas y perpendiculares), piezas del balón (polígonos regulares) y, al cierre,
  *por qué el balón es redondo*: en cada vértice se juntan 108° + 120° + 120° = 348° < 360°, así
  que las piezas no quedan planas. Eso necesita la suma de los ángulos del triángulo y de los
  polígonos, que es el final del trimestre.
- «Euclides y los mosaicos» repetiría con 7° (teselados con Escher) y el origen babilónico de los
  360° no está documentado. «Las abejas y el hexágono» deja sin contexto los temas de ángulos.
  De esos dos se conservan pedazos verificados: las definiciones de Euclides y la prop. I.32 en
  el marco teórico, y el panal como contraejemplo plano del balón.
- **No duplica con 7°**: 7° usa a Escher y las transformaciones. Aquí los teselados solo aparecen
  como pregunta de ángulos (¿qué polígonos regulares completan 360°?), sin transformaciones.

## Decisiones provisionales (a confirmar en la Revisión 1)

1. **Triángulos 6°/8°** (`PENDIENTES.md`, sección 1, sin decidir): se sigue el reparto
   provisional del plan de 6°. Aquí van clasificación, construcción (desigualdad triangular) y
   suma de 180°; congruencia, semejanza y Pitágoras quedan en 8°. Se reutilizan
   `triangulos-6-001, 003, 005, 013, 014, 015, 017, 020` y `angulos-6-001, 002` (y
   `angulos-6-002, 003` en la guía de 7°). Si la docente
   decide que esos ejercicios se quedan en 8°, hay que reemplazarlos.
2. **Orden de los temas.** Los valores distintos de `tema`, en orden de aparición, son: Ángulos
   (001–003), Ángulos entre rectas (004), Polígonos (005 y 008), Triángulos (006–007). La suma de
   los ángulos de un polígono (sesión 008, tema «Polígonos») necesita los 180° del triángulo,
   que se ven después (007). Por eso esa parte va **al final del tema de Triángulos**, como «Del
   triángulo al polígono», y la clase 008 citará `tema:triangulos`. Alternativa: cambiar el
   `tema` de la fila 008 a «Triángulos y polígonos» (no se tocó `programacion.csv`).
3. **Sesión 001** (clasificación de ángulos, sin DBA) entra como primera parte del tema 1.

## DBA y evidencias

Fuente: `dba/matematicas/grados/grado06.tex` (texto literal).

**DBA 5** — «Propone y desarrolla estrategias de estimación, medición y cálculo de diferentes
cantidades (ángulos, longitudes, áreas, volúmenes, etc.) para resolver problemas.»

| Evidencia | Tema que la atiende |
|---|---|
| Decide acerca de las estrategias para determinar qué tan pertinente es la estimación y analiza las causas de error en procesos de medición y estimación. | 1 (errores al leer el transportador; comparar estimación y medida) |
| Estima el resultado de una medición sin realizarla, de acuerdo con un referente previo… | 1 (el ángulo recto como referente; ángulos de tiro) |
| Estima la medida de longitudes, áreas, volúmenes, masas, pesos y ángulos… y decide sobre la conveniencia de los instrumentos… | 1, 2 |

**DBA 6** — «Representa y construye formas bidimensionales y tridimensionales con el apoyo en
instrumentos de medida apropiados.»

| Evidencia | Tema que la atiende |
|---|---|
| Diferencia las propiedades geométricas de las figuras y cuerpos geométricos. | 3, 4 |
| Identifica los elementos que componen las figuras y cuerpos geométricos. | 3 (lados, vértices, ángulos, diagonales), 4 |
| Describe las congruencias y semejanzas en figuras bidimensionales y tridimensionales. | (solo mención; queda para 8°, decisión 1) |
| Construye cuerpos geométricos con el apoyo de instrumentos de medida adecuados. | 3 (hexágono con compás; el balón como cuerpo), 4 (triángulo con regla y compás) |

**DBA 4** (construcción con regla y compás): tema 3 y tema 4. Sus plantillas de cuerpos quedan
para el trimestre III.

Ejemplo oficial usado: el del DBA 5 (tiro al arco) → ejemplo resuelto y ejercicio del tema 1.
Su matemática está revisada: con los postes a 7,32 m, el ángulo desde el punto penal (11 m) es
≈ 36,8°, desde el borde del área (16,5 m) ≈ 25,0° y desde 11 m corrido 9 m al lado ≈ 23,1°.

## Frase introductoria

«La belleza de las matemáticas solo se muestra a sus seguidores más pacientes.» — Maryam
Mirzakhani, entrevista del *Clay Mathematics Institute Annual Report 2008* (trad. propia; original:
«The beauty of mathematics only shows itself to more patient followers»). Encaja con un trimestre
de medir con cuidado, estimar y comparar.

## Marco teórico (redactado)

**Dar vueltas en 360 partes.** Hacia el siglo V a. C., los astrónomos de Babilonia dividían el
recorrido aparente del Sol en el cielo en 12 partes de 30, es decir, en 360 partes, y así nació la
costumbre de medir los ángulos en grados. No dejaron escrito por qué eligieron 360: se cree que
influyeron su sistema de numeración en base 60 y que el año tiene cerca de 360 días, pero es una
suposición, no un hecho comprobado [nrich, mactutorbab].

**Euclides pone nombres.** Hacia el 300 a. C., Euclides abrió sus *Elementos* con definiciones que
todavía usamos: un ángulo es recto cuando una recta que se levanta sobre otra forma con ella dos
ángulos adyacentes iguales; obtuso, si es mayor que un recto; agudo, si es menor. También clasificó
los triángulos por sus lados (equilátero, isósceles, escaleno) y por sus ángulos (rectángulo,
obtusángulo, acutángulo), y en la proposición 32 del Libro I demostró que los tres ángulos de un
triángulo suman dos rectos, 180° [euclides].

**Un balón para la televisión.** Para el Mundial de México 1970, adidas fabricó el Telstar: 32
piezas, 12 pentágonos negros y 20 hexágonos blancos, pensadas para verse bien en los televisores
en blanco y negro; su nombre viene de *television star* [adidas]. Desde entonces ese dibujo es la
imagen de un balón de fútbol.

**Una cancha con reglas.** Las medidas del fútbol las fija la IFAB en sus Reglas de Juego: el arco
mide 7,32 m entre los postes y 2,44 m de alto, el punto penal está a 11 m, y las líneas del área
se trazan en ángulo recto con la línea de meta [ifab].

**Maryam Mirzakhani.** Nació en Teherán en 1977. En 2014 fue la primera mujer en recibir la
Medalla Fields, el premio más importante para matemáticos jóvenes, por sus estudios sobre la
geometría de superficies curvas; fue profesora de la Universidad de Stanford y murió en 2017
[mactutormirzakhani]. En la entrevista de la que viene la frase contó que de niña quería ser
escritora y que no le interesaban las matemáticas [clay2008].

## Temas

### Tema 1 — Ángulos · `tema:angulos`

Sesiones 001–003 (semanas 02–04). DBA 5.

- **Hilo:** el portero y el delantero discuten desde dónde es más fácil hacer gol. Para
  resolverlo hay que medir un ángulo: el que forman las rectas del jugador a los dos postes.
- **Explicación:** ángulo (dos rayos con un vértice común), notación ∠BAC; grado sexagesimal
  (1/360 de la vuelta); clasificación por su medida (agudo, recto, obtuso, llano, entrante,
  completo); uso del transportador (centro en el vértice, cero sobre un lado, qué escala leer);
  estimar con referentes (el recto, la mitad de un recto); complementarios, suplementarios,
  conjugados.
- **Ejemplo resuelto:** el ángulo de tiro desde el punto penal (≈ 37°) medido a escala.
- **Aplicación:** el ángulo de tiro y la posición del jugador (DBA 5).
- **Recursos:** módulo de Geometría, Tema 1 (clasificación, medición, complementarios y
  suplementarios).
- **Ejercicios planeados:** clasificar medidas (cálculo, dif. 1); ángulos de tiro, estimar y medir
  (contexto, dif. 2); dos demostraciones cortas de complementarios/conjugados (argumentación).

### Tema 2 — Ángulos entre rectas · `tema:angulosrectas`

Sesión 004 (semana 05). DBA 5 y 6.

- **Hilo:** la cancha es un dibujo de rectas: la línea de meta y la media nunca se cortan; la
  línea lateral y la de meta forman una esquina recta.
- **Explicación:** rectas paralelas, perpendiculares y secantes (oblicuas); ángulos adyacentes
  (suman 180° si son lineales) y opuestos por el vértice (son iguales, con la demostración del
  módulo); bisectriz.
- **Aplicación:** las líneas de la cancha (IFAB).
- **Ejercicios planeados:** ángulos que forman dos secantes (cálculo, dif. 1); verdadero o falso
  sobre bisectrices de adyacentes (argumentación, dif. 2).

### Tema 3 — Polígonos · `tema:poligonos`

Sesión 005 (semana 06). DBA 4 y 6.

- **Hilo:** el balón Telstar está hecho de polígonos cosidos.
- **Explicación:** polígono (y lo que no lo es), lados, vértices, ángulos internos, diagonales
  (n − 3 desde un vértice; n(n − 3)/2 en total); nombres por número de lados; equilátero,
  equiángulo, regular; convexo y cóncavo; construcción del hexágono regular con compás (lado =
  radio).
- **Aplicación:** las 32 piezas del Telstar: contar lados, costuras y vértices.
- **Ejercicios planeados:** tabla de lados, vértices y diagonales (cálculo, dif. 1); costuras y
  vértices del Telstar (contexto, dif. 3).

### Tema 4 — Triángulos · `tema:triangulos`

Sesiones 006–008 (semanas 07, 08 y 10). DBA 5 y 6.

- **Hilo:** el triángulo es el polígono más sencillo, y con triángulos se explica por qué el
  balón es redondo.
- **Explicación:** clasificación por lados y por ángulos; construcción con regla y compás dados
  los tres lados; desigualdad triangular; suma de 180° (demostración con la paralela, Euclides
  I.32); ángulo externo; **del triángulo al polígono**: triangulación desde un vértice, suma
  180°(n − 2), ángulo del polígono regular; qué polígonos regulares completan 360° alrededor de un
  punto (3, 4 y 6) y por qué el balón se cierra (348°).
- **Aplicación:** el balón y el panal: 348° se curva, 360° queda plano.
- **Ejercicios planeados:** verdadero o falso (desigualdad, ángulos recto y obtuso); ángulos de
  triángulos (rectángulo, isósceles, externo); suma de ángulos del pentágono y el hexágono; el
  vértice del balón (argumentación, dif. 3).

## Cierre del hilo

El balón resume el trimestre: cada pieza es un polígono regular, sus ángulos se calculan con
triángulos, y porque 108° + 120° + 120° no alcanzan los 360°, las piezas se curvan hasta cerrar
una esfera. Anuncio del trimestre II: medir lo que ocupan las figuras —perímetro y área— y ubicar
figuras en el plano cartesiano.

## Evaluación (borrador de la matriz)

- **Saber:** clasifica ángulos, pares de ángulos, polígonos y triángulos; sabe que los ángulos de
  un triángulo suman 180°.
- **Hacer:** estima y mide ángulos con el transportador; construye triángulos y hexágonos con regla
  y compás; calcula ángulos de triángulos y polígonos.
- **Ser:** estima antes de medir y revisa sus medidas cuando no coinciden.
- **Convivir:** explica sus estrategias de medición a sus compañeros y escucha las de ellos.

## Referencias (verificadas el 2026-09-14/15)

| Clave | Referencia | Veredicto | URL |
|---|---|---|---|
| adidas | adidas (s. f.). *How adidas has shaped the history of World Cup balls from 1970 to the present day*. | confirmada: 32 paneles, 12 pentágonos negros y 20 hexágonos blancos, para TV en blanco y negro; «television star» | https://news.adidas.com/timeline/how-adidas-has-shaped-the-history-of-world-cup-balls-from-1970-to-the-present-day/s/012334d5-aee6-4153-a1dd-0fb0085c14a5 |
| clay2008 (frase) | Clay Mathematics Institute (2008). Interview with Research Fellow Maryam Mirzakhani. *Annual Report 2008*, pp. 11–13. | confirmada, texto literal en el PDF | https://www.claymath.org/library/annual_report/ar2008/08Interview.pdf |
| euclides | Euclides. *Elementos*, Libro I (ed. electrónica de D. E. Joyce, Clark University): def. 10–12, 19–21; prop. 32. | confirmada | https://mathcs.clarku.edu/~djoyce/elements/bookI/bookI.html · https://mathcs.clarku.edu/~djoyce/elements/bookI/propI32.html |
| ifab | IFAB. *Reglas de Juego*, Regla 1: El terreno de juego. | confirmada: 7,32 m, 2,44 m, punto penal a 11 m, líneas en ángulo recto | https://www.theifab.com/laws/latest/the-field-of-play/ |
| mactutorbab | O'Connor, J. J. y Robertson, E. F. *Babylonian numerals*. MacTutor. | confirmada: las explicaciones del 60 (y del año de 360 días) son hipótesis poco convincentes | https://mathshistory.st-andrews.ac.uk/HistTopics/Babylonian_numerals/ |
| mactutormirzakhani | O'Connor, J. J. y Robertson, E. F. *Maryam Mirzakhani (1977–2017)*. MacTutor. | confirmada: Teherán 1977, Fields 2014 (primera mujer), Stanford 2008, muere en 2017 | https://mathshistory.st-andrews.ac.uk/Biographies/Mirzakhani/ |
| mendba | Ministerio de Educación Nacional (2016). *Derechos Básicos de Aprendizaje V.2: Matemáticas*. | confirmada (catálogo del MEN) | https://gblumen.mineducacion.gov.co/cgi-bin/koha/opac-detail.pl?biblionumber=4785 |
| modulo | Quintero Palomino, A. *Módulo de Matemáticas: Geometría* (Guías de Apoyo Educativo). | recurso local | recursos/matematicas/Guías pedagógicas Matemáticas/ (archivo local) |
| nrich | NRICH (University of Cambridge). *The History of Trigonometry — Part 1*. | confirmada: las observaciones babilonias dieron origen, con el tiempo, a los 360°; el origen no es seguro | https://nrich.maths.org/articles/history-trigonometry-part-1 |

Quitado o parafraseado: el «origen babilónico de los 360°» va como «se cree», no como hecho; no se
usa ninguna cita de Euclides textual (se parafrasean sus definiciones); Hales y el panal quedan
fuera (no se usan como dato, solo el panal como imagen de tres hexágonos).

## Etapa B — ejercicios (2026-09-15)

Reglas de la docente del 2026-09-15: la guía usa **solo ejercicios del banco**; si el banco no
tiene nada para un tema o una evidencia, se escribe **lo mínimo**, verificado con
`--sin-registro` y marcado como nuevo. Sin ejercicios abiertos nuevos.

| Tema | Id | Enunciado (corto) | Respuesta | Estado | Origen |
|---|---|---|---|---|---|
| 1 | angulos-medicion-6-004 | Ángulos de tiro A, B, C: estimar y medir | ≈ 37°, 25°, 23° | verificado | **nuevo**: ejemplo del DBA 5; el banco no tenía ningún ejercicio de estimar o medir ángulos |
| 1 | angulos-6-002 | Suplementarios iguales → rectos | 90° cada uno | verificado | reuso |
| 1 | angulos-6-001 | Mismo conjugado → iguales | α = β | verificado | reuso |
| 2 | triangulos-6-003 | V/F: bisectrices de adyacentes perpendiculares | falsa en general | verificado | reuso |
| 2 | triangulos-6-005 | V/F: bisectrices de suplementarios adyacentes | verdadera | verificado | reuso |
| 3 | poligonos-6-001 | Lados, vértices, diagonales (5, 6, 8 lados) | 5/2/5; 6/3/9; 8/5/20 | verificado | **nuevo**: el banco no tenía ningún ejercicio de polígonos de 6° |
| 3 | poligonos-6-005 | Telstar: lados, costuras, vértices | 180, 90, 60 | verificado | **nuevo**: ídem; aplicación del hilo |
| 4 | triangulos-6-001 | V/F desigualdad triangular | verdadera | verificado | reuso |
| 4 | triangulos-6-013, 014 | V/F: más de un recto / más de un obtuso | verdaderas | verificado | reuso |
| 4 | triangulos-6-015, 017 | Ángulos de un rectángulo (x, 2x) y de un isósceles (50°) | 30°, 60°, 90°; 65°, 65° | verificado | reuso |
| 4 | triangulos-6-020 | Ángulo externo en B | C = 80° | verificado | reuso |

Nuevos: **3** (`recursos/banco/matematicas/angulos-medicion-6.py`, `poligonos-6.py`); reusados: 10.
Pendiente de registrar: una sesión corre `python3 tools/ejercicios.py verificar` (sin
`--sin-registro`) cuando terminen los agentes en paralelo.

**Evidencias o partes de tema sin ejercicio en la guía** (pendientes; se explican en la teoría):
- Tema 1: clasificar ángulos por su medida y leer bien el transportador (DBA 5, evidencia 1).
- Tema 2: ángulos adyacentes y opuestos por el vértice con medidas; reconocer paralelas y
  perpendiculares (solo hay los V/F de bisectrices).
- Tema 3: clasificar polígonos (regular, equilátero, equiángulo, cóncavo) y construir el hexágono
  con compás (DBA 4 y 6, «Construye…»).
- Tema 4: construir triángulos con regla y compás; suma de los ángulos de un polígono,
  teselados y el vértice del balón (348°), que queda como ejemplo resuelto en la aplicación.
- DBA 6, «Describe las congruencias y semejanzas»: queda para 8° (decisión 1).

Los ejemplos resueltos de la teoría (ángulos de tiro 37° y 25°, 9 diagonales del hexágono,
120° y 348°) se comprobaron con SymPy durante la etapa B, pero ya no son entradas del banco.

**Errores encontrados en el recurso** (módulo de Geometría, Quintero Palomino):
- Tema 4, «Triangulación de polígonos»: dice «n − 2 diagonales» desde un vértice; son n − 3
  diagonales y n − 2 triángulos (anotado en `poligonos-6.py`).
- Tema 4, Suma de ángulos, Ejemplo 3: el ángulo interno del polígono regular de 20 lados da
  «160°»; es 162°.
- Tema 4, Ejemplo 6: plantea 180(n − 2) − 360 = 1800 para «los ángulos internos suman 1800°»; la
  ecuación correcta es 180(n − 2) = 1800 (la respuesta, 12, sí es correcta).
- Tema 1: «Ángulos conjugados: dos ángulos son *suplementarios* si suman un perigonal» y
  «suplementarios: … entonces los ángulos son *complementarios*» (erratas de palabra).
