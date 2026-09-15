# Plan de la guía — Geometría 5° · Trimestre I (etapa A)

> Etapa A del skill `crear-guia`: estructura, teoría, hilo y fuentes, **sin enunciados de
> ejercicios**. Espera la **Revisión 1** de la docente. Rehace la guía escrita el 2026-09-14 sin
> este proceso (`guia-periodo-I-ubicacion.tex`, que se reemplaza en la etapa C); corrige lo que
> encontró la revisión de ese día.

## Datos

| | |
|---|---|
| Asignatura | Geometría |
| Grado | 5° |
| Trimestre | I (semanas 02–12; sesiones 001–009 de `programacion.csv`) |
| Archivo | `guia-periodo-I-ubicacion.tex` |
| Título | Cali, mi ciudad |
| Hilo | **Cali, mi ciudad**: orientar a Tatiana, una visitante, con planos, coordenadas y rutas (el ejemplo del propio DBA 7; aprobado el 2026-09-14) |
| Registro | 5°: vocabulario matemático formal, introducido y explicado; procedimientos completos; problemas de varios pasos; contextos de ciudad, viajes y juegos de mesa; pesos colombianos; citas cortas explicadas con palabras propias; sin diminutivos ni mascotas |

## Decisiones tomadas (2026-09-14)

1. **Orden del par.** El tema 1 conserva lo que se enseñó en la semana 03: la cuadrícula del salón
   se lee **(fila, columna)** —filas con letras A–D desde el tablero, columnas con números 1–5 de
   izquierda a derecha—, así que (B, 3) es «fila B, columna 3». El tema 2 presenta el **par
   ordenado (x, y)** como una convención nueva y universal, y explica el cambio: primero la
   distancia horizontal (hacia la derecha) y después la vertical (hacia arriba), igual que en el
   ajedrez, donde «e4» es primero la columna *e* y luego la fila *4*. Un ejercicio pide leer el
   mismo punto en las dos convenciones.
2. **Mapa.** El mapa del hilo es una **cuadrícula simplificada tipo barrio**, rotulada como
   simplificada, cuyos números crecen hacia la derecha y hacia arriba, como en el plano cartesiano.
   De Cali solo se usan nombres de lugares, no su numeración real de calles y carreras.
3. **Solo el primer cuadrante.** En 5° se trabaja únicamente con coordenadas positivas (y cero).
   Los cuatro cuadrantes se nombran porque la evidencia del DBA habla de «cuadrantes», pero se dice
   explícitamente que los otros tres necesitan números negativos, que llegan en grados posteriores.

## DBA y evidencias

Fuente: `dba/matematicas/grados/grado05.tex` (texto literal).

**DBA 7** — «Resuelve y propone situaciones en las que es necesario describir y localizar la
posición y la trayectoria de un objeto con referencia al plano cartesiano.»

| Evidencia | Tema que la atiende |
|---|---|
| Localiza puntos en un mapa a partir de coordenadas cartesianas. | 4 (mapa del barrio), 2 |
| Interpreta los elementos de un sistema de referencia (ejes, cuadrantes, coordenadas). | 1 (cuadrícula del salón), 2 (ejes, origen, cuadrantes) |
| Grafica en el plano cartesiano la posición de un objeto usando direcciones cardinales (norte, sur, oriente y occidente). | 1 (sesión 003), 2 (oriente = derecha = x; norte = arriba = y) — **reforzada**: la guía anterior le dedicaba una sola pregunta |
| Emplea el plano cartesiano al plantear y resolver situaciones de localización. | 2, 4 |
| Representa en forma gráfica y simbólica la localización y trayectoria de un objeto. | 3 (recorridos), 4 |

**Ejemplo del DBA como columna vertebral del hilo:** «Tatiana es una turista que ha venido a
visitarnos. Ayuda a Tatiana a ubicarse a partir de un plano de la ciudad, municipio o barrio»; el
DBA pide hacer un mapa a escala del barrio en papel cuadriculado, crear un sistema de referencia
con los puntos cardinales, escribirle un mensaje con el recorrido y proponer otras trayectorias.
Cada tema avanza un paso de esa tarea, y el repaso final (sesión 009, antes de la evaluación)
es el mensaje completo a Tatiana. En la guía anterior Tatiana no aparecía.

## Frase introductoria

«[La filosofía] está escrita en ese grandísimo libro que continuamente está abierto ante nuestros
ojos (digo, el universo)… Está escrito en lengua matemática, y sus caracteres son triángulos,
círculos y otras figuras geométricas.» — Galileo Galilei, *Il Saggiatore* (1623) (trad. propia;
cita de la lista aprobada en `REFERENCE.md`). Se acompaña de dos líneas que la explican con
palabras propias, como pide el registro de 5°: para entender el mundo, incluso para no perderse en
una ciudad, hace falta el idioma de la geometría.

## Marco teórico (redactado)

**¿Dónde queda?** «Al lado de la ventana», «detrás de la iglesia», «dos cuadras después del
parque»: así describimos dónde está algo. Sirve entre personas que conocen el lugar, pero no le
sirve a quien llega por primera vez, como Tatiana. Para ella hace falta un **sistema de
referencia**: un punto de partida y unas reglas que todos entiendan igual.

**Los puntos cardinales.** El sistema más antiguo usa el Sol: por el **oriente** sale y por el
**occidente** se oculta; mirando hacia el oriente, el **norte** queda a la izquierda y el **sur**
a la derecha. Los mapas se dibujan, por costumbre, con el norte hacia arriba, y por eso en un
mapa el oriente queda a la derecha. En Colombia, el Instituto Geográfico Agustín Codazzi elabora
la cartografía oficial del país, y en sus mapas cada lugar tiene coordenadas [igac].

**Descartes: ponerle números al espacio.** En 1637 el filósofo y matemático francés René
Descartes publicó *La geometría*, como uno de los ensayos que acompañaban su *Discurso del
método* [descartes1637]. Allí mostró cómo ubicar un punto con **dos números**: dos distancias
medidas a partir de rectas de referencia. Él no las dibujaba siempre perpendiculares, como
hacemos hoy: los ejes que se cortan en ángulo recto se generalizaron después, en manos de otros
matemáticos [sepdescartes]. En su honor, el sistema se llama **plano cartesiano**. Se cuenta que
tuvo la idea mirando una mosca en el techo de su cuarto; es solo una leyenda, pero explica bien
el problema: ¿cómo decir con números dónde está la mosca? [nrichmosca]

**Katherine Johnson: trayectorias que llegaron al espacio.** Más de trescientos años después, en
Estados Unidos, la matemática **Katherine Johnson** calculó en la NASA la trayectoria del primer
vuelo espacial tripulado del país (Alan Shepard, 1961). En 1962, antes de que John Glenn diera la
vuelta a la Tierra, las cuentas las hizo un computador; Glenn pidió que ella repitiera a mano los
mismos cálculos y dijo que, si ella decía que estaban bien, él estaba listo para volar [nasajohnson].
Una trayectoria es exactamente lo que dibujaremos en esta guía: una sucesión de posiciones.

## Temas

Los cuatro `tema` de las filas 002–008, en orden; la sesión 001 (introducción dictada) y la 009
(evaluación) no son temas de la guía. Las etiquetas se conservan: la semana 03 ya cita
`tema:referencia`.

### Tema 1 — Sistemas de referencia · `tema:referencia`

Sesiones 002–003 (semanas 03–04).

- **Hilo:** Tatiana llega al colegio y pregunta dónde está el salón de 5°. «Al lado de la
  cafetería» no le sirve: necesita un sistema.
- **Explicación:**
  - Posición relativa frente a sistema de referencia (punto de partida + reglas).
  - La cuadrícula del salón: filas con letras desde el tablero, columnas con números de izquierda
    a derecha; el par **(fila, columna)**, por ejemplo (B, 3). Por qué importa el orden: (B, 3) y
    (3, B) no nombran lo mismo si se cambia la regla.
  - Los puntos cardinales: cómo encontrarlos con el Sol y por qué los mapas ponen el norte arriba.
- **Aplicación:** las sillas numeradas de un teatro o de un estadio (fila y número de silla) —
  real y cercano.
- **Recursos:** clase y tarea de la semana 03 (misma cuadrícula y mismo acuerdo); `recursos/`
  no trae cuadrículas con letras para 5°.
- **Ejercicios planeados** (3–4):
  1. Leer y escribir posiciones (fila, columna) en la cuadrícula del salón (representación, dif. 1).
  2. Encontrar el error: alguien escribe la posición con el orden invertido; explicar a qué
     puesto llegaría (argumentación, dif. 2).
  3. Orientarse con los puntos cardinales en un plano del colegio (localización, dif. 1).
  4. Diseñar un sistema de referencia para otro lugar (la biblioteca, el parqueadero) y
     explicarlo por escrito (creación, dif. 2).

### Tema 2 — El plano cartesiano · `tema:plano`

Sesiones 004–006 (semanas 05–07; quiz en la 006). Cierra el bloque de coordenadas.

- **Hilo:** las letras de las filas se acaban y no dejan medir. Descartes cambió las letras por
  números: así cualquiera, en cualquier idioma, entiende la posición de Tatiana.
- **Explicación:**
  - Ejes, origen, unidades; el par ordenado **(x, y)**: primero cuántas unidades a la derecha,
    después cuántas hacia arriba.
  - **El cambio de convención, explícito:** en el salón decíamos primero la fila (vertical); en
    el plano cartesiano se dice primero la distancia horizontal. Es la regla que usa todo el
    mundo en matemáticas, igual que el ajedrez, que nombra «e4»: primero la columna, luego la
    fila [fide].
  - Puntos cardinales dentro del plano: oriente = hacia la derecha (x), norte = hacia arriba (y);
    «3 cuadras al oriente y 2 al norte» es el punto (3, 2) (ejemplo del módulo de 5°).
  - Los cuatro **cuadrantes**, solo como vocabulario; en 5° se trabaja en el primero.
  - Figuras en el plano: vértices de un rectángulo o de un triángulo como pares ordenados.
- **Aplicación:** la batalla naval (juego de mesa) y la pantalla de un videojuego o una foto
  digital, que ubican cada punto con dos números.
- **Recursos:** módulo de 5°, «Parejas ordenadas y distancias» (el banco en (3, 2) al oriente y
  al norte). **Banco:** `plano-cartesiano-5-005` (el origen) sirve tal cual; los demás de ese
  archivo usan coordenadas negativas y no sirven para 5° en este trimestre.
- **Ejercicios planeados** (4–5):
  1. Ubicar y leer puntos del primer cuadrante (cálculo, dif. 1) — `plano-cartesiano-5-005` y
     ejercicios nuevos solo con positivos.
  2. El mismo punto en las dos convenciones: una casilla del salón escrita (fila, columna) y como
     par (x, y) (argumentación, dif. 2) — decisión 1.
  3. Traducir instrucciones cardinales («4 al oriente, 1 al norte») a pares y al revés
     (representación, dif. 1).
  4. Vértices de una figura: dados tres vértices de un rectángulo, encontrar el cuarto
     (resolución, dif. 2).
  5. ¿Por qué (2, 5) y (5, 2) no son el mismo punto? (argumentación, dif. 1).

### Tema 3 — Trayectorias · `tema:trayectorias`

Sesión 007 (semana 08).

- **Hilo:** Tatiana quiere ir del hotel al zoológico. Katherine Johnson no calculaba un solo
  punto, sino una trayectoria completa: una sucesión de posiciones.
- **Explicación:**
  - Describir un recorrido por la cuadrícula con instrucciones («2 al oriente, 3 al norte») y
    con la lista de puntos por donde pasa.
  - Varios caminos, el mismo destino: **en los caminos más cortos** por las calles de la cuadrícula
    siempre se recorre la misma cantidad de unidades horizontales y verticales; un camino con
    vueltas de más es más largo.
  - Longitud de un recorrido contando unidades (sin diagonales).
- **Aplicación:** las indicaciones de una aplicación de mapas en el celular («gire a la derecha,
  siga 2 cuadras»).
- **Recursos:** no hay en el banco de 5° ejercicios de trayectorias en cuadrícula: todos serán
  nuevos (etapa B).
- **Ejercicios planeados** (3–4):
  1. Dibujar la trayectoria descrita por instrucciones y dar el punto de llegada (representación,
     dif. 1).
  2. Escribir las instrucciones de una trayectoria dibujada (representación simbólica, dif. 1).
  3. Proponer dos caminos más cortos distintos y comparar su longitud; ¿qué pasa con un camino
     que da vueltas? (argumentación, dif. 2) — el DBA pide «proponer otras trayectorias».
  4. Un obstáculo (una calle cerrada): buscar el camino más corto que lo evite (resolución, dif. 3).

### Tema 4 — Mapas y planos · `tema:mapas`

Sesión 008 (semana 10). La 009 (semana 12) es la evaluación del periodo.

- **Hilo:** el mensaje final a Tatiana: un mapa del barrio, su sistema de referencia y el
  recorrido por los mejores lugares.
- **Explicación:**
  - Un **mapa simplificado** del barrio en cuadrícula, rotulado como simplificado, con los
    números creciendo hacia la derecha (oriente) y hacia arriba (norte), y lugares con nombres
    de Cali (por ejemplo, un parque, una biblioteca, una iglesia, una estación del MIO); no se
    usa la numeración real de las calles de Cali.
  - Localizar lugares por coordenadas y describir su posición con puntos cardinales.
  - Escala sencilla: cada cuadra de la cuadrícula representa una misma distancia.
- **Aplicación:** los mapas oficiales del IGAC, que ubican cada lugar de Colombia con coordenadas
  [igac].
- **Recursos:** módulo de 5° (coordenadas en mapas); `semejanza-escala-5` del banco para la
  escala, si la docente quiere incluirla (revisar en la etapa B).
- **Ejercicios planeados** (3–4):
  1. Localizar lugares en el mapa del barrio a partir de coordenadas (localización, dif. 1).
  2. Describir la posición de un lugar respecto a otro con puntos cardinales (representación,
     dif. 1).
  3. Escribirle a Tatiana el mensaje con un recorrido por tres lugares: coordenadas,
     instrucciones y longitud (situación integradora, dif. 3) — el ejemplo del DBA.
  4. Proponer una trayectoria alternativa y explicar cuál conviene más (argumentación, dif. 2).

## Cierre del hilo

Tatiana ya puede recorrer el barrio sola: con un sistema de referencia, pares ordenados y
trayectorias escritas, cualquiera que lea el mensaje llega al mismo lugar. Es la misma idea de
Descartes hace casi cuatrocientos años y la que usó Katherine Johnson para traer de vuelta a un
astronauta. Anuncio del trimestre II: de ubicar puntos a medir figuras —perímetro y área (DBA 5)—.

## Evaluación (borrador de la matriz)

- **Saber:** reconoce los elementos de un sistema de referencia (ejes, origen, cuadrantes,
  coordenadas) y los puntos cardinales.
- **Hacer:** ubica y lee puntos del primer cuadrante; traduce entre instrucciones cardinales y
  pares ordenados; describe y dibuja trayectorias en un mapa.
- **Ser:** escribe instrucciones claras y completas, pensando en quien las va a leer.
- **Convivir:** acuerda reglas comunes con sus compañeros y las respeta, porque sin un acuerdo
  el sistema de referencia no funciona.

## Referencias

Todas verificadas el 2026-09-14. En la etapa C cada `\bibitem` lleva su `% verificado:`.

| Clave | Referencia | Veredicto | Corrección | URL |
|---|---|---|---|---|
| galileo1623 (frase) | Galilei, G. (1623). *Il Saggiatore*. Roma: Giacomo Mascardi. Pasaje del «grandissimo libro… scritto in lingua matematica, e i caratteri son triangoli, cerchi, ed altre figure geometriche» | confirmada (texto) | la URL anterior del Museo Galileo responde con error: se cambia la evidencia; se marca «trad. propia» | https://it.wikisource.org/wiki/Il_Saggiatore_(Favaro)/6 |
| descartes1637 | Descartes, R. (1637). *La géométrie*, uno de los ensayos publicados con el *Discours de la méthode*. | confirmada (año y publicación con el *Discurso*) | la URL anterior de Gallica responde 403; en la etapa C se intenta de nuevo o se usa MacTutor | https://mathshistory.st-andrews.ac.uk/Extras/Descartes_La_Geometrie/ |
| sepdescartes | Domski, M. (y otros), *Descartes' Mathematics*, *Stanford Encyclopedia of Philosophy*: en *La geometría* las incógnitas se toman como **coordenadas oblicuas** | confirmada | nueva: corrige la simplificación «dos rectas que se cruzan» | https://plato.stanford.edu/entries/descartes-mathematics/ |
| nrichmosca | NRICH / wild.maths.org, *René Descartes and the Fly on the Ceiling* (la historia contada como leyenda) | confirmada como leyenda | nueva; la guía la presenta como leyenda | https://wild.maths.org/ren%C3%A9-descartes-and-fly-ceiling |
| nasajohnson | NASA, *Katherine Johnson Biography* (Langley Research Center): trayectoria de Shepard (1961); Glenn (1962) pidió que ella verificara a mano los cálculos del computador | confirmada | «casi trescientos años» → «más de trescientos» (1637 → 1962) | https://www.nasa.gov/centers-and-facilities/langley/katherine-johnson-biography/ |
| fide | FIDE, *Laws of Chess*, Apéndice C, «Algebraic notation»: columnas con letras a–h, filas con números 1–8; «e4» | confirmada | nueva: sostiene el orden del ajedrez (columna, luego fila) | https://rcc.fide.com/appendixc/ |
| igac | Instituto Geográfico Agustín Codazzi. *Geoportal*. | confirmada (portal oficial) | — | https://geoportal.igac.gov.co/ |
| mendba | Ministerio de Educación Nacional (2016). *Derechos Básicos de Aprendizaje V.2: Matemáticas*. Bogotá: MEN. | confirmada | **ISBN corregido**: 978-958-691-913-5 (la guía anterior decía 925-8) | https://gblumen.mineducacion.gov.co/cgi-bin/koha/opac-detail.pl?biblionumber=4785 |

## Problemas encontrados en los recursos

- `plano-cartesiano-5-006` a `-014` (del módulo de 5°, «Parejas ordenadas y distancias») usan
  coordenadas negativas y distancias entre enteros negativos: el módulo trabaja los cuatro
  cuadrantes en 5°, pero este trimestre se queda en el primero (decisión 3). No es un error del
  recurso, pero no sirven aquí.
- `plano-cartesiano-5-004` sigue en estado `manual-pendiente`.

## Lo que viene

- **Etapa B** (tras la aprobación de este plan): reutilizar `plano-cartesiano-5-005`; escribir y
  verificar los nuevos (cuadrícula del salón, cambio de convención, puntos cardinales, figuras,
  trayectorias y camino más corto, mapa del barrio, mensaje a Tatiana); tabla
  id · enunciado · respuesta · estado para la Revisión 2.
- **Etapa C:** reemplazar el `.tex` actual; dibujar el mapa simplificado con TikZ (números hacia la
  derecha y hacia arriba) y rehacer las figuras del salón con el mismo acuerdo de la semana 03.
