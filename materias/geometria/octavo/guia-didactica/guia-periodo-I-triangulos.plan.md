# Plan de la guía — Geometría 8° · Trimestre I (etapa A)

> Etapa A del skill `crear-guia`: estructura, teoría, hilo y fuentes, **sin enunciados de
> ejercicios**. Espera la **Revisión 1** de la docente. Escrito el 2026-09-14.

## Datos

| | |
|---|---|
| Asignatura | Geometría |
| Grado | 8° |
| Trimestre | I (semanas 01–12; sesiones 001–012 de `programacion.csv`, una por semana, martes, 50 min) |
| Archivo | `guia-periodo-I-triangulos.tex` |
| Título propuesto | La sombra de la pirámide |
| Hilo | **Tales de Mileto y la medición de la gran pirámide** (aprobado en `plan-anual.md`) |
| Registro | Juvenil (7°–11°): definiciones formales y notación, citas con fuente, justificar y argumentar |
| DBA | Matemáticas grado 8 · DBA 6 y DBA 7 |
| Guía en paralelo | Álgebra 8°, «La cacería de π» (`materias/algebra/octavo/guia-didactica/`) |

## Decisiones y preguntas para la docente

Nada de lo siguiente se decidió aquí; se marca para la Revisión 1.

1. **Temas de la guía.** Los `tema` distintos de las filas 003–011 son cinco: Ángulos de un
   triángulo, Congruencia, Semejanza, Teorema de Pitágoras y Teorema de Thales. Las filas
   001–002 (tema «Triángulos», clasificación, ya dictadas) no tienen DBA. ¿Se agrega un
   repaso corto de clasificación al comienzo del tema 1, o la guía empieza en la semana 03?
2. **Fila 003 sin DBA.** «Suma de ángulos internos y externos» tiene `dba` vacío. Podría
   servir a la evidencia «Resuelve problemas utilizando teoremas básicos» (DBA 7), pero es
   también contenido de grados anteriores. ¿Le asigna DBA 7, o se queda como repaso sin DBA?
   (No se tocó `programacion.csv`.)
3. **Orden del hilo.** El paso más famoso (la pirámide) cae en la semana 07, y el «Teorema de
   Thales» en la semana 11, *después* de Pitágoras. El plan lo cuenta así: en la semana 07,
   Tales mide con triángulos semejantes; en la semana 11 se enuncia en general la
   proporcionalidad que usó. ¿Le parece bien, o prefiere pasar Thales antes de Pitágoras?
4. **Qué es el «teorema de Tales».** En español (y en el DBA) es el de las paralelas que
   cortan lados proporcionales (Euclides VI.2); en inglés, *Thales' theorem* es el ángulo
   inscrito en una semicircunferencia (Euclides III.31), el único que una fuente antigua
   (Diógenes Laercio, citando a Pánfila) le atribuye a Tales. Propuesta: enseñar el primero
   (es el de la fila 011) y mencionar el segundo como «el otro teorema de Tales», sin
   ejercicios. ¿De acuerdo?
5. **Semana 12.** Evaluación del periodo sin repaso previo (el plan anual lo marca como
   pendiente de confirmar). La guía no depende de eso, pero el cierre anuncia la evaluación.
6. **Álgebra 8° en paralelo.** Álgebra usa Pitágoras como herramienta enunciada antes de la
   semana 09 (diagonal del cuadrado de lado 1, espiral de Teodoro) y en sus semanas 09–10 hace
   problemas de escalera y de televisores. Aquí se evita repetir: Geometría hace la
   **demostración con material concreto**, el **recíproco** y aplicaciones distintas
   (escuadra 3-4-5 en obra, diagonal de una cancha, distancias en un plano). Ninguna guía
   repite las historias de la otra (π, √2, Hipatia, Cantor se quedan en Álgebra).
7. **Duplicados del banco entre grados** (`recursos/banco/PENDIENTES.md`, *no decididos*):
   - Triángulos, verdadero o falso y problemas: `triangulos-6` o `triangulos-8` (mismos
     enunciados). ¿Qué grado se los queda?
   - Ángulos, demostraciones: `angulos-6-002/003` o `angulos-8-012/013`.
   - Pitágoras, problemas 3–8 del módulo: `pitagoras-9-002…005` o `medicion-11-008…011`; si
     quedan en 9° u 11°, en 8° solo se usarían con permiso.
   - `pitagoras-8` «2n»: el módulo imprime √225 (= 15) pero el texto alternativo dice «raíz
     cuadrada de 255»; el banco dejó √225 (`pitagoras-8-039`). Confirmar con el original.
   - `triangulos-8-003` (ítem 1c del módulo): «las bisectrices de dos ángulos adyacentes son
     perpendiculares» — el banco la da como *falsa en general* (solo es cierta si los ángulos
     son suplementarios); la figura del módulo sugiere «verdadera». Confirmar el criterio.
8. **Error del recurso.** El módulo de Geometría (Tema 2, «Congruencia de triángulos») da como
   primer criterio de congruencia «si dos ángulos de un triángulo son congruentes con dos
   ángulos de otro, los triángulos son congruentes». **Es falso**: con dos ángulos iguales
   solo son *semejantes* (el criterio correcto es ALA, con el lado comprendido). También
   rotula «Ángulos Semejantes» una figura de ángulos congruentes. La guía no toma esa parte.
9. **Ejercicios de ángulos pendientes de aprobación.** `angulos-8-001…017` están en estado
   `manual-pendiente` (definiciones de axioma, teorema… y demostraciones). No entran a la
   guía mientras no los apruebe.
10. **Medidas de la pirámide.** Se usarán redondeadas: altura original ≈ 146 m (el Ministerio
    de Turismo y Antigüedades de Egipto da 146,5 m). El lado de la base (≈ 230 m) solo lo
    encontré en Wikipedia y en sitios de divulgación: queda **por confirmar** antes de la
    etapa C; mientras tanto los problemas se pueden plantear con la sombra, sin la base.

## Por qué este hilo

Tales es a la vez el primer nombre de la geometría griega y un personaje cuya historia está
llena de leyendas; eso sirve para el grado: cada paso enseña matemática *y* a distinguir lo
que dicen las fuentes de lo que se cuenta después. Las fuentes antiguas le atribuyen
justamente los resultados del trimestre: ángulos opuestos por el vértice e iguales en la base
del isósceles (tema 1), un criterio de congruencia para medir barcos en el mar (tema 2), la
sombra de la pirámide (tema 3) y la proporcionalidad que lleva su nombre (tema 5). Pitágoras
(tema 4) llega una generación después, desde Samos, a pocos kilómetros de Mileto; y la
tablilla Plimpton 322 muestra que los babilonios ya conocían la relación mil años antes.

## DBA y evidencias

Fuente: `dba/matematicas/grados/grado08.tex` (texto literal).

**DBA 6** — «Identifica relaciones de congruencia y semejanza entre las formas geométricas
que configuran el diseño de un objeto.»

| Evidencia | Tema que la atiende |
|---|---|
| Utiliza criterios para argumentar la congruencia de dos triángulos. | 2 (LLL, LAL, ALA; por qué AAA no basta) |
| Discrimina casos de semejanza de triángulos en situaciones diversas. | 3 (AA, LLL, LAL; sombras, fotos, logotipos) |
| Resuelve problemas que implican aplicación de los criterios de semejanza. | 3 (pirámide, altura de un árbol, planos y mapas), 5 |
| Compara figuras y argumenta la posibilidad de ser congruente o semejantes entre sí. | 2 y 3 (ejemplo de los logotipos del DBA; ¿congruente ⇒ semejante? ¿y al revés?) |

**DBA 7** — «Identifica regularidades y argumenta propiedades de figuras geométricas a partir
de teoremas y las aplica en situaciones reales.»

| Evidencia | Tema que la atiende |
|---|---|
| Describe teoremas y argumenta su validez a través de diferentes recursos (Software, tangram, papel, entre otros). | 1 (suma de ángulos con papel recortado y con paralelas), 4, 5 (GeoGebra) |
| Argumenta la relación pitagórica por medio de construcción al utilizar material concreto. | 4 (rompecabezas de los dos cuadrados de lado a + b; cuadrícula del DBA) |
| Reconoce relaciones geométricas al utilizar el teorema de Pitágoras y Thales, entre otros. | 4, 5 |
| Aplica el teorema de Pitágoras para calcular la medida de cualquier lado de un triángulo rectángulo. | 4 |
| Resuelve problemas utilizando teoremas básicos. | 1 (si se le asigna DBA 7; ver pregunta 2), 4, 5 |

Ejemplos del propio DBA que se usan: los logotipos (DBA 6) en los temas 2–3; el cuadrado
inclinado dentro de otro sobre cuadrícula (DBA 7) en el tema 4. Revisados: el de los
logotipos pide «figuras congruentes» en figuras con simetría rotacional — está bien, pero hay
que dejar claro que congruentes = una se lleva sobre la otra con un movimiento rígido.

## Frase introductoria

«La filosofía está escrita en ese grandísimo libro que continuamente está abierto ante
nuestros ojos (digo: el universo)… Está escrito en lengua matemática, y sus caracteres son
triángulos, círculos y otras figuras geométricas.» — Galileo Galilei, *Il Saggiatore* (1623),
cap. 6 (trad. propia; está en la lista verificada de `REFERENCE.md`).

Original: «La filosofia è scritta in questo grandissimo libro che continuamente ci sta aperto
innanzi a gli occhi (io dico l'universo)… Egli è scritto in lingua matematica, e i caratteri
son triangoli, cerchi, ed altre figure geometriche».

Por qué esta: la frase nombra literalmente los triángulos, el objeto del trimestre, y abre el
tema de fondo del hilo: con triángulos se mide lo que no se puede alcanzar.

## Marco teórico (redactado)

**Un sabio de Mileto.** Tales vivió en Mileto, una ciudad griega de la costa de la actual
Turquía, aproximadamente entre el 624 y el 547 a. C. [mactutorthales]. No se conserva nada
escrito por él: todo lo que sabemos viene de autores que vivieron siglos después. Por eso los
historiadores advierten que a los hombres famosos de la época se les atribuían
descubrimientos que quizás no hicieron [mactutorthales]. Aun así, la tradición lo presenta
como el primero que no se contentó con saber *que* algo es cierto en geometría, sino que
quiso saber *por qué*.

**Lo que le atribuyen.** Proclo, un filósofo que escribió hacia el año 450 d. C. apoyándose en
una historia de la geometría perdida de Eudemo (discípulo de Aristóteles), cuenta que Tales
fue el primero en afirmar que los ángulos opuestos por el vértice son iguales y que en todo
triángulo isósceles los ángulos de la base son iguales; y que midió la distancia de los barcos
en el mar con un método que requiere lo que hoy llamamos el criterio ángulo-lado-ángulo
[ogrady; mactutorthales].

**La sombra de la pirámide.** La historia más famosa llega en dos versiones. Diógenes Laercio
(siglo III d. C.) cita a Jerónimo de Rodas: Tales midió la altura de las pirámides por su
sombra, «tomando la observación a la hora en que nuestra sombra es tan larga como nosotros»
[diogenes, I.27; trad. propia]. Plutarco, en el *Banquete de los siete sabios*, pone en boca de
un personaje otra versión más geométrica: Tales clavó su bastón en el extremo de la sombra de
la pirámide y, con los dos triángulos que formaban los rayos del sol, mostró que la pirámide es
al bastón como una sombra es a la otra [plutarco]. Ninguna de las dos es un testimonio de la
época: son relatos escritos entre seis y ocho siglos después, y hay que contarlos como
**leyenda**. Lo que sí es cierto es la matemática: con rayos de sol paralelos, los dos
triángulos son semejantes, y el método funciona. La pirámide más grande de Guiza, la de
Keops, medía originalmente unos 146 metros de altura [egipto].

**Mil años antes de Pitágoras.** La relación a² + b² = c² no la inventó Pitágoras. La tablilla
babilónica Plimpton 322, escrita en Larsa (en el actual Irak) hacia 1820–1762 a. C. y guardada
hoy en la Universidad de Columbia, contiene ternas de números que la cumplen [columbia]. Otra
tablilla, la YBC 7289, muestra un cuadrado con sus diagonales y una aproximación de √2 correcta
en cinco cifras decimales [mactutorbabilonia]. Pitágoras nació en Samos, cerca de Mileto,
hacia el 570 a. C.; no escribió libros, y la historia de que sacrificó bueyes al descubrir el
teorema viene de unos versos tardíos de autor incierto [huffman]. Proclo no le atribuye una
demostración, sino el conocer la verdad del teorema [huffman]. La demostración escrita más
antigua que conservamos es la de Euclides (*Elementos*, I.47, hacia el 300 a. C.), y el nombre
«teorema de Pitágoras» se lo pusieron autores muy posteriores [euclidesI47; maor].

**Más de trescientas demostraciones.** El teorema se ha demostrado de muchísimas maneras; en
1876, James A. Garfield, que años después fue presidente de Estados Unidos, publicó una con un
trapecio y tres triángulos rectángulos [ellermeyer]. Es la prueba de que en matemáticas se
puede llegar a la misma verdad por caminos diferentes.

**La proporcionalidad de Tales.** Lo que en los países de habla hispana se llama «teorema de
Tales» —una recta paralela a un lado de un triángulo corta los otros dos lados en segmentos
proporcionales— aparece demostrado en Euclides (*Elementos*, VI.2) [euclidesVI2]. En inglés,
*Thales' theorem* nombra otro resultado: todo ángulo inscrito en una semicircunferencia es
recto [mathworld], el que Diógenes Laercio, citando a Pánfila, atribuye a Tales cuando cuenta
que «fue el primero en inscribir un triángulo rectángulo en un círculo» [diogenes, I.24]. Los
dos nombres honran al mismo personaje.

**De la sombra a la órbita: Katherine Johnson.** Veinticinco siglos después, medir con
triángulos seguía siendo cuestión de vida o muerte. Katherine Johnson (1918–2020),
matemática estadounidense, entró en 1953 al laboratorio de la NACA (luego NASA) en Langley.
Calculó la trayectoria del primer vuelo espacial tripulado de Estados Unidos (Alan Shepard,
mayo de 1961) y, antes del vuelo orbital de John Glenn en 1962, él mismo pidió que ella
comprobara a mano los números del computador. Sus cálculos ayudaron a sincronizar el módulo
lunar con el módulo de mando en el programa Apolo, y en 2015 recibió la Medalla Presidencial de
la Libertad [nasajohnson].

## Temas

Cinco `tema` de las filas 003–011, en orden. Los títulos vienen de `programacion.csv`.

### Tema 1 — Ángulos de un triángulo · `tema:angulostriangulo`

Sesión 003 (semana 03). DBA: pendiente (pregunta 2). Tarea.

- **Hilo:** Tales llega a Egipto (así lo cuentan las fuentes) y se hace una pregunta que los
  egipcios no se hacían: *¿por qué* los ángulos de la base de un isósceles son iguales? Antes de
  medir pirámides hay que conocer las leyes de los ángulos.
- **Explicación:**
  - Repaso de 30 segundos: ángulos opuestos por el vértice, complementarios, suplementarios;
    ángulos entre paralelas y una secante (alternos internos iguales).
  - Teorema: la suma de los ángulos internos de un triángulo es 180°. Dos argumentos: con papel
    (recortar las tres esquinas y juntarlas en una recta) y con una paralela por un vértice
    (demostración con alternos internos) — «ver» no es lo mismo que «demostrar».
  - Ángulo externo: es igual a la suma de los dos internos no adyacentes; suma de los externos
    = 360°.
  - Consecuencias: un triángulo tiene a lo sumo un ángulo recto u obtuso; los agudos de un
    rectángulo son complementarios; en el isósceles, ángulos de la base iguales (se enuncia).
  - Ejemplo resuelto: ángulos de un triángulo con un ángulo doble de otro (tipo del módulo).
- **Aplicación:** las cerchas de un techo o el soporte de una repisa: el ángulo que falta se
  calcula sin medirlo.
- **Recursos:** módulo de Geometría, Tema 1 (paralelas y secante) y Tema 2 («Practica lo
  aprendido»); `triangulos-8-015…023` (verificados) — **sujeto a la decisión 6°/8°**.
- **Ejercicios planeados** (3–4):
  1. Calcular ángulos internos y externos faltantes (cálculo, dif. 1).
  2. Encontrar el error: «un triángulo puede tener dos ángulos obtusos» o similar
     (argumentación, dif. 2) — candidatos `triangulos-8-001…014`.
  3. Problema con una condición (un ángulo es el doble de otro; isósceles con ángulo dado)
     (cálculo, dif. 2) — `triangulos-8-015…018`.
  4. Demostrar que el ángulo externo es la suma de los internos no adyacentes
     (argumentación, dif. 3).

### Tema 2 — Congruencia de triángulos · `tema:congruencia`

Sesiones 004–005 (semanas 04–05). DBA 6. Taller (004), tarea (005).

- **Hilo:** según Eudemo, Tales calculaba desde la costa la distancia a un barco. Si se conocen
  un lado y los dos ángulos de sus extremos, el triángulo queda determinado: se puede copiar en
  tierra, y medir allí la distancia que en el mar no se puede medir.
- **Explicación:**
  - Definición: dos triángulos son congruentes si tienen lados y ángulos correspondientes
    iguales; notación △ABC ≅ △DEF y la importancia del orden de los vértices.
  - Criterios LLL, LAL (ángulo *comprendido*) y ALA (lado *comprendido*); por qué **AAA no
    basta** (corrige el recurso, pregunta 8) y por qué LLA en general tampoco (contraejemplo
    con compás).
  - Construcción con regla y compás de un triángulo congruente a otro (LLL) — la semana 05.
  - Ejemplo resuelto: demostrar con LAL que la diagonal de un rombo lo divide en dos triángulos
    congruentes; y usar ALA para una distancia inaccesible (el barco de Tales, con números).
  - Propiedades reflexiva, simétrica y transitiva (breve).
- **Aplicación:** la rigidez del triángulo (LLL): por eso puentes, torres y cerchas usan
  triángulos; un cuadrilátero de varillas se deforma, un triángulo no.
- **Recursos:** módulo de Geometría, Tema 2 («Congruencia de triángulos», **sin** su primer
  criterio); ejemplo de los logotipos del DBA 6. En el banco no hay ejercicios de congruencia
  de 8°: se escriben en la etapa B.
- **Ejercicios planeados** (4–5):
  1. Decidir qué criterio justifica la congruencia de pares de triángulos dados (conceptual,
     dif. 1).
  2. Encontrar el error: «dos triángulos con los tres ángulos iguales son congruentes»
     (argumentación, dif. 2).
  3. Demostración corta con LAL o ALA en una figura (argumentación, dif. 2–3).
  4. Construir con regla y compás un triángulo congruente y justificar (construcción, dif. 1).
  5. Logotipos del DBA: identificar figuras congruentes y argumentar (contexto, dif. 2).

### Tema 3 — Semejanza de triángulos · `tema:semejanza`

Sesiones 006–008 (semanas 06–08). DBA 6. Taller (006), tarea (007), **quiz (008)**.

- **Hilo:** el paso central. Tales frente a la gran pirámide: no puede subir a medirla, pero sí
  medir su sombra. Las dos versiones (Jerónimo: esperar a que la sombra sea igual a la altura;
  Plutarco: comparar con la sombra de un bastón), contadas como leyenda, y por qué la segunda
  funciona a cualquier hora.
- **Explicación:**
  - Definición: triángulos semejantes (ángulos iguales y lados proporcionales); razón de
    semejanza k; notación △ABC ~ △DEF.
  - Criterios AA, LLL (lados proporcionales), LAL (dos lados proporcionales y ángulo
    comprendido igual).
  - Congruencia como caso k = 1; ¿semejante ⇒ congruente? (no).
  - Ejemplo resuelto: la pirámide con la sombra de un bastón (números redondeados, altura ≈ 146
    m; ver pregunta 10). Por qué los rayos de sol son paralelos y los triángulos semejantes (AA).
  - Razón de perímetros = k (se muestra); razón de áreas = k² (se menciona como curiosidad).
  - Semana 08: escalas en planos y mapas — la escala como razón de semejanza (sin volver a
    enseñar la escala de 7°, DBA 4 de grado 7; aquí se *justifica* con semejanza).
- **Aplicación:** medir en el patio del colegio la altura de un árbol o de un poste con un palo
  de escoba y un metro (actividad posible en la semana 07); leer distancias en un mapa de Cali.
- **Recursos:** módulo de Geometría, Tema 2 («Semejanza de figuras», ejemplos con lados 3-4-5 y
  9-12-15 y criterios); DBA 6 (logotipos). Sin ejercicios de semejanza de 8° en el banco
  (`semejanza-escala-5` es de 5°); se escriben en la etapa B.
- **Ejercicios planeados** (4–5):
  1. ¿Son semejantes? Pares de triángulos con ángulos o lados dados; decir el criterio
     (conceptual, dif. 1).
  2. Hallar lados desconocidos con la razón de semejanza (cálculo, dif. 2).
  3. La sombra: altura de un edificio o de la pirámide con la sombra de un bastón (contexto,
     dif. 2).
  4. Plano o mapa a escala: distancia real y comprobación (contexto, dif. 2).
  5. Argumentar: «todos los triángulos equiláteros son semejantes», «todos los isósceles son
     semejantes» — ¿verdadero o falso? (argumentación, dif. 2–3).

### Tema 4 — Teorema de Pitágoras · `tema:pitagoras`

Sesiones 009–010 (semanas 09–10). DBA 7. Taller (009), tarea (010).

- **Hilo:** una generación después de Tales, en Samos, a pocos kilómetros de Mileto, crece
  Pitágoras. La relación que lleva su nombre ya estaba en las tablillas babilónicas mil años
  antes; la leyenda de los bueyes sacrificados es tardía. Lo que sí hicieron los griegos fue
  **demostrarla**.
- **Explicación:**
  - Enunciado (catetos, hipotenusa, c² = a² + b²) y su recíproco (si a² + b² = c², el triángulo
    es rectángulo).
  - Demostración con material concreto (semana 09): los dos cuadrados de lado a + b con cuatro
    triángulos iguales (la del módulo; en papel o tangram); la cuadrícula con un cuadrado
    inclinado del ejemplo del DBA 7. Por qué la figura del centro es un cuadrado (tema 1: los
    agudos suman 90°).
  - Extensión: la prueba de Garfield con el trapecio (usa congruencia y áreas).
  - Calcular hipotenusa y cateto; resultados exactos (con raíces) y aproximados — Álgebra ya
    trabaja los radicales esa misma semana, así que aquí solo se aproxima.
  - Ternas pitagóricas (3-4-5, 5-12-13) y Plimpton 322 como la «tabla» más antigua.
- **Aplicación:** en obra, los maestros de construcción comprueban una esquina recta con una
  cuerda o un metro marcando 3, 4 y 5 (o 60, 80 y 100 cm); también la diagonal de una cancha de
  microfútbol. (Se evitan la escalera y el televisor, que son de Álgebra.)
- **Recursos:** módulo de Geometría, Tema 3 (demostración y problemas); `pitagoras-8-001…045`
  (verificados: 25 de recíproco con ternas, 20 de hallar un lado) — revisar `pitagoras-8-039`
  (√225 o √255). Los problemas 3–8 del módulo están en `pitagoras-9` / `medicion-11`
  (decisión 9°/11° pendiente).
- **Ejercicios planeados** (4–5):
  1. Construir la demostración con papel y explicarla por escrito (construcción y
     argumentación, dif. 2) — evidencia 2 del DBA 7.
  2. ¿Es rectángulo? Recíproco con ternas (cálculo, dif. 1) — `pitagoras-8-001…025`.
  3. Hallar un lado desconocido, hipotenusa o cateto (cálculo, dif. 1–2) —
     `pitagoras-8-026…045`.
  4. La escuadra de 3-4-5 en una obra o la diagonal de una cancha (contexto, dif. 2).
  5. Encontrar el error: «c = a + b» o aplicar el teorema a un triángulo no rectángulo
     (argumentación, dif. 2).

### Tema 5 — Teorema de Thales · `tema:teoremathales`

Sesión 011 (semana 11). DBA 7. Taller.

- **Hilo:** la sombra de la pirámide, vista de nuevo: lo que Tales usó no era un truco para un
  día de sol sino una ley general de las paralelas. Euclides la escribió dos siglos y medio
  después; hoy lleva el nombre de Tales. Y el «otro» teorema de Tales, el del semicírculo.
- **Explicación:**
  - Enunciado: si una recta paralela a un lado de un triángulo corta los otros dos, los divide
    en segmentos proporcionales; versión con dos transversales cortadas por paralelas. El
    recíproco (Euclides VI.2 lo incluye).
  - Relación con la semejanza (tema 3): el triángulo pequeño y el grande son semejantes (AA).
  - Ejemplo resuelto: hallar un segmento con la proporción; dividir un segmento en partes
    iguales con regla y paralelas (sin medir).
  - Mención: ángulo inscrito en una semicircunferencia = 90° (sin ejercicios; pregunta 4).
  - Comprobación en GeoGebra: mover los puntos y ver que la razón no cambia (evidencia 1 del
    DBA 7).
- **Aplicación:** dividir una tabla o una cartulina en franjas iguales sin regla graduada;
  las líneas de un cuaderno como paralelas equidistantes.
- **Recursos:** módulo de Geometría (no trae el teorema de Tales como tema propio: se escribe
  desde Euclides VI.2); en el banco no hay ejercicios de Tales de 8°: se escriben en la etapa B.
- **Ejercicios planeados** (3–4):
  1. Hallar un segmento con la proporcionalidad (cálculo, dif. 1).
  2. ¿Son paralelas? Recíproco con medidas dadas (argumentación, dif. 2).
  3. Dividir un segmento en 5 partes iguales y justificar la construcción (construcción,
     dif. 2).
  4. Problema de contexto: rampa, calles paralelas o sombra (contexto, dif. 2–3).

## Cierre del hilo

De la sombra de un bastón a la trayectoria de una cápsula espacial: Tales (según la leyenda)
midió lo inalcanzable comparando triángulos, Pitágoras y Euclides demostraron las relaciones
que ya usaban los babilonios, y Katherine Johnson, veinticinco siglos después, confió vidas a la
misma geometría. La lección: la congruencia copia, la semejanza agranda y achica, y los teoremas
permiten medir sin tocar. Anuncio del trimestre II: de las figuras planas a los sólidos —
volumen de prismas y otros cuerpos con lenguaje algebraico (DBA 4).

## Evaluación (borrador de la matriz)

- **Saber:** enuncia la suma de ángulos del triángulo, los criterios de congruencia y de
  semejanza y los teoremas de Pitágoras y de Tales; distingue congruente de semejante.
- **Hacer:** justifica congruencias y semejanzas con el criterio adecuado; demuestra el
  teorema de Pitágoras con material concreto; calcula lados y alturas inaccesibles con
  semejanza, Pitágoras y Tales.
- **Ser:** argumenta sus respuestas con criterios, no con «se ve igual»; revisa sus medidas.
- **Convivir:** trabaja en equipo en las mediciones con sombras y construcciones; distingue lo
  demostrado de lo que se cuenta como leyenda.

## Referencias

Verificadas el 2026-09-14. En la etapa C cada `\bibitem` lleva su `% verificado:`.

| Clave | Referencia | Veredicto | Corrección | URL |
|---|---|---|---|---|
| columbia | Columbia University Libraries, exhibición *«Our Tools of Learning»: George Arthur Plimpton's Gifts*, Plimpton 322 | confirmada: Larsa, ca. 1820–1762 a. C., ternas pitagóricas, Rare Book & Manuscript Library | fecha precisa (no «1800 a. C.») | https://exhibitions.library.columbia.edu/exhibits/show/plimpton/mathematics/page-2 |
| diogenes | Diógenes Laercio (1925). *Lives of Eminent Philosophers*, vol. I (trad. R. D. Hicks; Loeb Classical Library 184). Harvard University Press. I.24 (Pánfila, triángulo en el círculo) y I.27 (Jerónimo, sombra) | confirmada (texto en Wikisource; edición en Harvard UP) | «las pirámides», no «la gran pirámide»; citas en trad. propia | https://en.wikisource.org/wiki/Lives_of_the_Eminent_Philosophers/Book_I · https://www.hup.harvard.edu/books/9780674992030 |
| egipto | Ministerio de Turismo y Antigüedades de Egipto, *The Great Pyramid* | confirmada: altura original 146,5 m | base (≈ 230 m) **no confirmada** fuera de Wikipedia: pendiente | https://egymonuments.gov.eg/en/monuments/the-great-pyramid |
| ellermeyer | Ellermeyer, S. F., *James Garfield's Proof of the Pythagorean Theorem* (Kennesaw State University) | confirmada: 1876, prueba con trapecio | la revista (*New-England Journal of Education*, 1 abr. 1876) solo aparece en Wikipedia y en la reseña de MAA Convergence (Kolpas), que no cargó: se dice «publicó en 1876» sin nombrar la revista | https://facultyweb.kennesaw.edu/sellerme/docs/garfieldpro.pdf |
| euclidesI47 | Euclides, *Elementos* I.47 (ed. D. E. Joyce, Clark University) | confirmada: nombre dado por Proclo y otros siglos después; conocido por los babilonios más de mil años antes | — | https://mathcs.clarku.edu/~djoyce/elements/bookI/propI47.html |
| euclidesVI2 | Euclides, *Elementos* VI.2 (ed. D. E. Joyce) | confirmada (incluye el recíproco) | la página no menciona a Tales: el nombre es de la tradición escolar | https://mathcs.clarku.edu/~djoyce/elements/bookVI/propVI2.html |
| galileo (frase) | Galilei, G. (1623). *Il Saggiatore*, cap. 6. Roma | confirmada (texto italiano en Wikisource); ya en la lista verificada | trad. propia | https://it.wikisource.org/wiki/Il_Saggiatore/6 |
| huffman | Huffman, C. (2024). Pythagoras. *Stanford Encyclopedia of Philosophy* (rev. 5 feb. 2024) | confirmada: ca. 570–490 a. C., no escribió libros, Proclo no le atribuye la demostración, versos de Apolodoro de autor incierto | — | https://plato.stanford.edu/entries/pythagoras/ |
| mactutorbabilonia | O'Connor, J. J. y Robertson, E. F. *Pythagoras's theorem in Babylonian mathematics*. MacTutor | confirmada: YBC 7289 (√2 ≈ 1;24,51,10 = 1,414213) | — | https://mathshistory.st-andrews.ac.uk/HistTopics/Babylonian_Pythagoras/ |
| mactutorthales | O'Connor, J. J. y Robertson, E. F. *Thales of Miletus*. MacTutor | confirmada: ca. 624–547 a. C.; tres relatos de la pirámide; advertencia sobre atribuciones | — | https://mathshistory.st-andrews.ac.uk/Biographies/Thales/ |
| maor | Maor, E. (2007). *The Pythagorean Theorem: A 4,000-Year History*. Princeton University Press (ISBN 978-0-691-12526-8) | confirmada (reseña en *Mathematical Gazette*; JSTOR) | — | https://www.jstor.org/stable/j.ctvh9w0ks · https://www.cambridge.org/core/journals/mathematical-gazette/article/abs/pythagorean-theorem-a-4000year-history-by-eli-maor-pp-272-1595-2007-isbn-9780691125268-princeton-university-press-donel0408/C9FCCF8FDBD72706FED74ABE52FDCCDC |
| mathworld | Weisstein, E. W. *Thales' Theorem*. MathWorld | confirmada: en inglés = ángulo inscrito en semicircunferencia | fuente de apoyo del nombre, no histórica | https://mathworld.wolfram.com/ThalesTheorem.html |
| mendba | Ministerio de Educación Nacional (2016). *Derechos Básicos de Aprendizaje V.2: Matemáticas*. Bogotá: MEN. ISBN 978-958-691-913-5 | confirmada (misma ficha que la guía de Álgebra 8°) | — | https://gblumen.mineducacion.gov.co/cgi-bin/koha/opac-detail.pl?biblionumber=4785 |
| nasajohnson | NASA, *Katherine Johnson Biography* | confirmada: 1918–2020; NACA 1953; Shepard 1961; Glenn 1962; Apolo; Medalla 2015 | — | https://www.nasa.gov/centers-and-facilities/langley/katherine-johnson-biography/ |
| ogrady | O'Grady, P. *Thales of Miletus*. Internet Encyclopedia of Philosophy | confirmada: Proclo/Eudemo (opuestos por el vértice, isósceles, barcos → Euclides I.26), relatos de la pirámide | — | https://iep.utm.edu/thales/ |
| plutarco | Plutarco. *Banquete de los siete sabios* (Moralia 147A). Loeb Classical Library 222, trad. F. C. Babbitt (1928); texto inglés en línea en Monadnock Valley Press | confirmada en su contenido (bastón, dos triángulos, sombras proporcionales) | la página Loeb no cargó (403) y Perseus falló: el número 147A y el traductor de la versión en línea **quedan por confirmar**; se parafrasea, sin cita textual | https://monadnock.net/plutarch/banquet.html · https://www.loebclassics.com/view/plutarch-moralia_dinner_seven_wise_men/1928/pb_LCL222.353.xml |
| — | Módulo de Geometría (Quintero Palomino), Temas 1–3 | archivo local | error en el primer criterio de congruencia (pregunta 8) | `recursos/matematicas/Guías pedagógicas Matemáticas/markdown/Modulo_Matematicas_Geometria.md` |

**Quitados o reformulados:** «Tales midió *la gran pirámide*» → las fuentes dicen «las
pirámides» (Diógenes) o «una de las pirámides» (Plutarco); «Pitágoras demostró el teorema» →
se conocía antes y no hay prueba suya conservada; «teorema de Tales = ángulo en el
semicírculo» → depende del idioma. No se usa la cuerda de 12 nudos de los «tensadores de
cuerda» egipcios (sin fuente primaria).

## Etapas B y C (modo rápido, 2026-09-15, sin esperar la Revisión 1)

La docente pidió avanzar sin la Revisión 1. Las preguntas de arriba se resolvieron con las
recomendaciones del propio plan como **decisión provisional**; todas quedan para la revisión.

**Decisiones provisionales**

1. Repaso corto de clasificación (filas 001–002) dentro del tema 1; la guía no tiene tema
   «Triángulos» aparte.
2. Fila 003 sin DBA: no se tocó el CSV; la guía no le asigna DBA (los ejercicios del tema 1
   quedan con `matematicas-8-7` en el banco, como `triangulos-8`).
3. Orden: Tales (proporcionalidad) después de Pitágoras, como dice el CSV.
4. «Teorema de Tales» = el de las paralelas (Euclides VI.2); el de la semicircunferencia solo
   se menciona, sin ejercicios.
5. Duplicados 6°/8° y 9°/11° sin decidir: se usan `triangulos-8` y `pitagoras-8` (son de 8°);
   no se usan `pitagoras-9`, `medicion-11` ni `angulos-8`.
6. `pitagoras-8-039` (√225 o √255) y `triangulos-8-003` (bisectrices) **no se usan**.
7. El criterio falso del módulo («dos ángulos iguales ⇒ congruentes») se corrige en la guía
   sin nombrar el recurso.

**Referencias re-verificadas (antes «por confirmar»)**

| Clave | Veredicto | URL |
|---|---|---|
| plutarco | confirmada: *Moralia* 147A, trad. F. C. Babbitt, Loeb 222 (1928); se cita textual (trad. propia) | https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Plutarch/Moralia/Dinner_of_the_Seven*.html |
| elgabry (nueva) | confirmada: base ≈ 230,33 m, altura original 146,59 m (*Scientific Reports*, 2026) | https://pmc.ncbi.nlm.nih.gov/articles/PMC13194686/ |
| garfield (nueva) | confirmada: «Pons Asinorum», J. A. G., *New-England Journal of Education* 3(14), 1 abr. 1876, p. 161 (registro JSTOR hallado por búsqueda; la página no cargó el texto) | https://www.jstor.org/stable/44764657 |

No se usan en la guía: `mactutorbabilonia` (YBC 7289 y √2 son de Álgebra) ni la cita
Diógenes I.24 textual (va parafraseada).

**Ejercicios (etapa B)** — regla de la docente del 2026-09-15 («Reuse, don't multiply»):
se reusa todo lo posible y solo se escribe lo que el banco no tiene. Buscado también en otros
grados: `congruencia-9` y `medicion-indirecta-9` están *sin verificar*; `icfes-cuadernillo-2026-015`
(sombras) es de 11° y va textual con figura; `semejanza-escala-5` es de 5°. Nuevos en
`recursos/banco/matematicas/triangulos-geometria-8.py` (verificados con
`verificar --sin-registro`; falta el `verificar` con registro). Ningún manual nuevo.

| Tema | Reusados | Nuevos y por qué |
|---|---|---|
| 1 ángulos | ejemplo triangulos-8-015; ejercicios triangulos-8-017, -021, -014, -018 | ninguno |
| 2 congruencia | — | tg-001 (qué criterio, y por qué AAA no basta: no hay congruencia de 8° en el banco); tg-002 (el barco de Tales, ALA en contexto: el hilo) |
| 3 semejanza | — | tg-003 (¿son semejantes?: no hay semejanza de 8°); tg-004 (altura con la sombra de un palo: contexto); tg-005 (la pirámide, ejemplo resuelto del hilo) |
| 4 Pitágoras | pitagoras-8-008, -005 (recíproco), -036, -026, -041 (lados); demostraciones sin id (son teoría) | tg-006 (escuadra 60-80-100 del maestro de obra: `pitagoras-8` no tiene contexto, y `pitagoras-9`/`medicion-11` esperan la decisión 9°/11°) |
| 5 Tales | — (ejemplo resuelto: la construcción, sin números) | tg-007 (hallar un segmento); tg-008 (recíproco, argumentación): no hay Tales de 8° |

(tg = `triangulos-geometria-8`.) 8 nuevos, todos verificados: más que el rango orientativo
(0–5) porque tres temas (congruencia, semejanza, Tales) no tenían ningún ejercicio de 8°; son
dos por tema más el ejemplo de la pirámide y un contexto de Pitágoras. Una primera versión con
28 (series de reserva y 5 manuales) se recortó antes de registrarse.

## Lo que viene

- **Etapa B** (tras la aprobación): usar `triangulos-8` y `pitagoras-8` según las decisiones
  6°/8° y 9°/11°; aprobar o descartar `angulos-8`; escribir y verificar los de congruencia,
  semejanza (sombras, escalas) y Tales, y los ejemplos resueltos (pirámide, barco, Garfield).
- **Etapa C:** `guia-periodo-I-triangulos.tex` desde la plantilla trimestral; sin «Prepárate
  para Saber 11» (es 8°).
