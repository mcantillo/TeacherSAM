# Plan de la guía — Álgebra 8° · Trimestre I (etapa A)

> Etapa A del skill `crear-guia`: estructura, teoría, hilo y fuentes, **sin enunciados de
> ejercicios**. Espera la **Revisión 1** de la docente. Rehace la guía que se escribió el
> 2026-09-13 sin este proceso (`guia-periodo-I-numeros-irracionales.tex`, que se reemplaza en
> la etapa C).

## Datos

| | |
|---|---|
| Asignatura | Álgebra |
| Grado | 8° |
| Trimestre | I (semanas 03–12; sesiones 007–036 de `programacion.csv`) |
| Archivo | `guia-periodo-I-numeros-irracionales.tex` |
| Título | La cacería de π |
| Hilo | **La cacería de π**: cuatro mil años persiguiendo un número que no se deja escribir como fracción, del papiro Rhind a los computadores de hoy (elegido el 2026-09-14; reemplaza a «El escándalo de los inconmensurables», porque ninguna fuente antigua liga a Hipaso con los irracionales) |
| Registro | Juvenil (7°–11°): definiciones formales y notación, citas con fuente, justificar y generalizar |

## Decisiones tomadas (2026-09-14)

1. **DBA de las sesiones 007–009:** 007 → DBA 1, 008 → DBA 1 y 2, 009 → DBA 1 (ya en
   `programacion.csv`). Pasar entre fracción y decimal es contenido de 7° (DBA 2 de grado 7), así
   que la sesión 007 es un repaso al servicio de la segunda evidencia del DBA 1 de 8°; la 008
   argumenta con esas representaciones (DBA 1) y construye dos representaciones del mismo número
   (DBA 2); la 009 plantea la existencia de decimales no periódicos (DBA 1).
2. **Hilo nuevo:** «La cacería de π» (arriba). Hipaso queda solo como una leyenda que se cuenta
   como tal en el marco teórico.
3. **Teorema de Pitágoras:** en Álgebra se usa como herramienta enunciada, sin demostrarlo; antes
   de la semana 09 solo con el cuadrado de lado 1 y el triángulo de catetos 1 y 2.
4. **Semana 12:** repaso final, evaluación del periodo y socialización (confirmado).

## Por qué este hilo

π es el irracional que los estudiantes ya conocen, y su historia pasa, en orden, por todo lo que
pide el trimestre: primero la pregunta de si su decimal se repite (tema 1), luego √2 como el primer
número que alguien demostró que no es fracción —el ensayo de lo que tardaría dos mil años con π—
(tema 2), después π y sus parientes en la vida real (tema 3), y por último las raíces cuadradas
con las que Arquímedes encerró a π entre dos polígonos (tema 4). Cada paso es un dato histórico
verificable, no una leyenda.

## DBA y evidencias

Fuente: `dba/matematicas/grados/grado08.tex` (texto literal).

**DBA 1** — «Reconoce la existencia de los números irracionales como números no racionales y
los describe de acuerdo con sus características y propiedades.»

| Evidencia | Tema que la atiende |
|---|---|
| Utiliza procedimientos geométricos para representar números racionales e irracionales. | 2 (diagonal del cuadrado, recta numérica) |
| Identifica las diferentes representaciones (decimales y no decimales) para argumentar por qué un número es o no racional. | 1 (decimales exactos/periódicos), 3 (clasificación) |

**DBA 2** — «Construye representaciones, argumentos y ejemplos de propiedades de los números
racionales y no racionales.»

| Evidencia | Tema que la atiende |
|---|---|
| Utiliza procedimientos geométricos o aritméticos para construir algunos números irracionales y los ubica en la recta numérica. | 2 (construcción de √2, espiral de Teodoro), 4 (raíces no exactas) |
| Justificar procedimientos con los cuales se representa geométricamente números racionales y números reales. | 2 (por qué el compás lleva √2 a la recta) |
| Construye varias representaciones (geométrica, decimales o no decimales) de un mismo número racional o irracional. | 1 (fracción y decimal del mismo racional), 2 y 3 (√2 como diagonal, como 1,41421…, como solución de x² = 2; π como razón, como decimal, como 22/7 aproximado) |

Ejemplos del propio DBA que se usan: Marina, Julián, Catalina y Marcela (DBA 1) en el tema 1;
√(△ + □) frente a √△ + √□ (DBA 2) en el tema 3. Su matemática está revisada: en el de Marcela,
«infinitos dígitos sin patrón» debe decir «sin que ningún bloque se repita periódicamente» (un
dado sí puede repetir dígitos).

## Frase introductoria

«La esencia de la matemática está precisamente en su libertad.» — Georg Cantor, *Grundlagen
einer allgemeinen Mannichfaltigkeitslehre* (1883), §8 (trad. propia). Original: «das Wesen der
Mathematik liegt gerade in ihrer Freiheit»; *Gesammelte Abhandlungen* (1932), p. 182.

Por qué esta: Cantor es quien, en el siglo XIX, terminó de darles a los irracionales un lugar
propio entre los números; la cacería de π es la historia de matemáticos que se tomaron la
libertad de preguntar si un número conocido por todos era lo que parecía.

## Marco teórico (redactado)

**Un número conocido desde siempre.** Cualquier círculo, grande o pequeño, cumple lo mismo: su
circunferencia mide un poco más de tres veces su diámetro. Esa razón es el número que hoy
llamamos π. En el papiro Rhind, copiado en Egipto hacia el 1650 a. C., el área de un círculo se
calcula de una manera que equivale a usar π ≈ 3,16 [mactutorpi]. Durante miles de años nadie
dudó de que π, como cualquier medida, se pudiera escribir como una fracción; el problema era solo
encontrarla.

**«Todo es número».** En el siglo VI a. C., en el sur de Italia, los pitagóricos pensaban que los
principios de los números eran los principios de todas las cosas [aristoteles]: cualquier
longitud, y cualquier relación entre longitudes, debía poder escribirse como una razón entre
números enteros —lo que hoy llamamos un número racional—. Lo comprobaban en la música: dos
cuerdas iguales suenan a una octava cuando sus longitudes están en razón 2 : 1.

**El primer número que no es fracción.** Esa convicción se rompió con una figura mucho más simple
que el círculo: la diagonal de un cuadrado no es conmensurable con su lado; en lenguaje de hoy,
√2 no es racional. No sabemos quién lo descubrió: autores antiguos tardíos cuentan que el
pitagórico que reveló el secreto murió en el mar, y la tradición le puso después el nombre de
Hipaso de Metaponto, pero ninguna fuente antigua lo liga directamente con este descubrimiento
[huffman]. Lo que sí sabemos es que en el siglo IV a. C. la demostración ya circulaba: Aristóteles
la pone como ejemplo de razonamiento por el absurdo —la diagonal es inconmensurable con el lado
«porque, si se supone conmensurable, los impares resultan iguales a los pares» (*Primeros
analíticos* I.23, 41a26–27)— [corry]. Poco después, según cuenta Platón en el *Teeteto*, Teodoro
de Cirene demostraba lo mismo para las raíces de 3, de 5 y así hasta la de 17 [mactutortheodorus],
y hacia el 300 a. C. Euclides dedicó el Libro X de sus *Elementos*, el más extenso de los trece, a
las magnitudes inconmensurables [euclides]. Si √2 no era fracción, ¿lo sería π?

**Arquímedes encierra a π.** Hacia el 250 a. C., Arquímedes de Siracusa no intentó escribir π
exactamente: lo *encerró*. Dibujó un polígono regular de 96 lados dentro del círculo y otro fuera;
el perímetro del de adentro es menor que la circunferencia y el del de afuera, mayor. Así demostró
que 223/71 < π < 22/7, es decir, que π está entre 3,1408 y 3,1429 [mactutorpi]. Para llegar ahí
necesitó aproximar raíces cuadradas: usó que 265/153 < √3 < 1351/780, sin explicar cómo lo había
obtenido [arqraices]. Por eso 22/7 sigue siendo la aproximación escolar de π.

**Hipatia.** Hacia el año 400, en Alejandría —la ciudad de Euclides—, Hipatia dirigía una escuela
donde enseñaba matemáticas y filosofía; las fuentes antiguas le atribuyen comentarios a la
*Aritmética* de Diofanto y a las *Cónicas* de Apolonio. Es la primera mujer de la que sabemos con
seguridad que hizo un aporte importante a las matemáticas, sobre todo conservando y enseñando la
obra de los griegos [dzielska].

**355/113.** En China, Zu Chongzhi (430–501) dio el valor 355/113 = 3,1415929…, que coincide con
π en sus primeras seis cifras decimales y que nadie superó en casi mil años [mactutorpi].

**Fin de la cacería… y otra que empieza.** Tanta precisión hacía sospechar que π no era ninguna
fracción, pero sospechar no es demostrar. En 1761 Johann Heinrich Lambert presentó ante la
Academia de Berlín la demostración de que π es irracional; su memoria se publicó en 1768
[lambert]. Desde entonces se sabe que su decimal nunca termina ni se repite. La cacería cambió
de presa: ya no se busca la fracción de π, sino más cifras. A finales de 2025, un solo servidor
calculó 314 billones de cifras decimales de π en 110 días [storagereview].

## Temas

Los cuatro `tema` de las filas 007–033, en orden. Las etiquetas se conservan porque la semana 03
ya cita `tema:racionalesirracionales`. Los títulos de los temas vienen de `programacion.csv`; si
la docente quiere que el tema 2 cambie de nombre por el cambio de hilo («El escándalo pitagórico»
→ p. ej. «El primer número que no es fracción»), se cambia en el CSV y en la guía, no la etiqueta.

### Tema 1 — De los racionales a los irracionales · `tema:racionalesirracionales`

Sesiones 007–009 (semana 03). DBA 1 (y 2 en la 008).

- **Hilo:** durante milenios se buscó la fracción de π. Antes de salir a cazarla, hay que saber
  qué aspecto tiene una fracción cuando se escribe como decimal.
- **Explicación:**
  - Definición de número racional (p/q, enteros, q ≠ 0); conjunto ℚ.
  - Ejemplo resuelto: por qué toda fracción da un decimal exacto o periódico (los restos de la
    división solo pueden ser 0, 1, …, q − 1: si ninguno es 0, alguno se repite).
  - Ejemplo resuelto: de decimal periódico a fracción (0,4545… = 45/99 = 5/11), incluido un
    periódico mixto.
  - Conclusión: los racionales son *exactamente* los decimales exactos o periódicos. Pregunta
    que pasa al tema 2: si el decimal de π nunca se repitiera, π no sería una fracción; ¿existe
    un número así?
- **Aplicación:** lo que muestra la calculadora al dividir 1 ÷ 3 o al pulsar π (la pantalla corta
  el decimal; el número no termina ahí).
- **Recursos:** módulo de 8° (Tema 1, decimales finitos y aproximaciones), solo como apoyo;
  ejemplo de Marina, Julián, Catalina y Marcela del DBA 1.
- **Ejercicios planeados** (3–4):
  1. Argumentar: los cuatro números del ejemplo del DBA 1, cuáles son racionales y por qué
     (argumentación, dif. 2).
  2. Decimal periódico → fracción irreducible, tres casos incluido uno mixto (cálculo, dif. 1–2).
  3. Encontrar el error: «0,999… no es igual a 1» (argumentación, dif. 2).
  4. ¿22/7 es π? Escribir 22/7 como decimal, ver que es periódico y concluir (argumentación,
     dif. 2) — puente al tema 2.

### Tema 2 — El escándalo pitagórico · `tema:escandalopitagorico`

Sesiones 010–015 (semanas 04–05). DBA 1 y 2.

- **Hilo:** la primera presa no fue π sino un número más sencillo: la diagonal de un cuadrado.
  Las fracciones 7/5, 17/12, 99/70 se le acercan cada vez más, pero ninguna la alcanza.
- **Explicación:**
  - Teorema: √2 no es racional. Demostración por el absurdo (la de paridad que menciona
    Aristóteles), paso a paso.
  - Definición de número irracional (decimal infinito no periódico; conjunto 𝕀).
  - Construcción: diagonal del cuadrado de lado 1 llevada a la recta con compás, y **por qué** el
    procedimiento es válido (el compás conserva la longitud).
  - Espiral de Teodoro: cada triángulo tiene catetos 1 y √n e hipotenusa √(n+1); ubicar √3 y √5
    en la recta. El nombre es un homenaje moderno a Teodoro [davis].
  - Un número, tres representaciones: √2 como diagonal, como 1,41421356…, como el número positivo
    cuyo cuadrado es 2 (evidencia 3 del DBA 2).
  - Cierre del paso del hilo: demostrar que √2 no es fracción cabe en media página; con π costó
    dos mil años más.
- **Aplicación:** la hoja A4 (norma ISO 216): su razón largo/ancho es √2, la única que se conserva
  al doblar la hoja por la mitad; la hoja carta que se usa en Colombia (21,6 × 27,9 cm) no la sigue.
- **Recursos:** `numeros-reales-8` del banco (representar en la recta real, ya verificados).
- **Ejercicios planeados** (4–5):
  1. Adaptar la demostración para √3 (argumentación, dif. 2).
  2. Ubicar √2, −√2 y √5 en la recta con construcción justificada (representación, dif. 2) —
     candidatos en `numeros-reales-8`.
  3. Continuar la espiral de Teodoro hasta √6 y medir (construcción, dif. 1).
  4. Comprobar con una hoja A4 real: medir y calcular largo/ancho (contexto, dif. 1).
  5. Aproximaciones de √2 por fracciones (7/5, 17/12, 99/70): ¿cuánto se equivoca cada una?
     (cálculo, dif. 2).

### Tema 3 — Los irracionales en la vida real · `tema:irracionalesvidareal`

Sesiones 016–024 (semanas 06–08). DBA 1 y 2.

- **Hilo:** ahora sí, la presa principal. π aparece en cada rueda, cada tubo y cada pista; el
  Rhind, Zu Chongzhi y Lambert, cada uno con su aproximación o su prueba.
- **Explicación:**
  - π como razón circunferencia/diámetro; sus aproximaciones históricas (≈ 3,16 del Rhind,
    22/7, 355/113) comparadas con su decimal, y qué error comete cada una.
  - Otros irracionales: e y φ = (1 + √5)/2, qué miden y su aproximación (sin demostrar que son
    irracionales).
  - Aproximaciones decimales y redondeo: cuántas cifras tiene sentido usar según la medida.
  - Los reales: ℝ = ℚ ∪ 𝕀 y la cadena ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ (𝕀 como complemento de ℚ, no dentro de la
    cadena).
  - Operaciones: racional + irracional siempre es irracional (demostración corta); irracional +
    irracional o × irracional puede ser racional (√2 + (3 − √2), √2 · √2).
  - Ejemplo del DBA 2: √(a + b) frente a √a + √b.
- **Aplicación:** la rueda de bicicleta (66 cm de diámetro → unas 482 vueltas por kilómetro; la
  cuenta se verifica en la etapa B) y el cuentakilómetros que cuenta vueltas; ¿cuánto se equivoca
  si usa 22/7 en vez de π?
- **Recursos:** módulo de 8° (operaciones con reales); `numeros-reales-8` del banco.
- **Ejercicios planeados** (4–5):
  1. Clasificar números en ℕ, ℤ, ℚ, 𝕀, incluidos 22/7 y π (conceptual, dif. 1).
  2. Comparar 3,16, 22/7 y 355/113 con π: cuál se acerca más y cuántas cifras acierta cada una
     (cálculo, dif. 2).
  3. ¿Es siempre irracional la suma de dos irracionales? Contraejemplos (argumentación, dif. 2).
  4. √(a + b) = √a + √b: probar con valores y concluir (argumentación, dif. 2, ejemplo del DBA).
  5. Llanta de carro: vueltas por kilómetro y por qué se redondea (contexto, dif. 2).

### Tema 4 — Radicales y aplicaciones · `tema:radicalesaplicaciones`

Sesiones 025–030 (semanas 09–10). DBA 1 y 2.

- **Hilo:** para encerrar a π con sus polígonos, Arquímedes tuvo que calcular con raíces
  cuadradas, como √3; para usar los radicales en medidas reales hay que saber simplificarlos y
  aproximarlos.
- **Explicación:**
  - Propiedad √(ab) = √a · √b (a, b ≥ 0) y simplificación sacando cuadrados perfectos.
  - Raíz no exacta de un entero: es irracional (se enuncia; se justifica con el caso de √2).
  - Radicales semejantes: por qué √18 + √2 = 4√2 y no √20.
  - Encerrar una raíz entre dos fracciones, como Arquímedes con √3: comprobar 265/153 < √3 <
    1351/780 elevando al cuadrado.
  - El perímetro del hexágono inscrito en un círculo de radio 1 es 6 y el del circunscrito, 4√3:
    primer encierro de π (3 < π < 2√3 ≈ 3,46), con el teorema de Pitágoras como herramienta.
  - Problemas de medidas con el teorema de Pitágoras (decisión 3).
- **Aplicación:** el tamaño de un televisor se da por su diagonal; con razón 16 : 9, la diagonal es
  √337 · k (se verifica en la etapa B).
- **Recursos:** módulo de 8° (radicación, radicales semejantes, raíces de productos);
  `radicacion-8` y `medidas-con-radicales-8` del banco (ya verificados).
- **Ejercicios planeados** (4–5):
  1. Simplificar radicales (cálculo, dif. 1) — `radicacion-8`.
  2. Encontrar el error: √18 + √2 = √20 (argumentación, dif. 2).
  3. Como Arquímedes: comprobar que 265/153 < √3 < 1351/780 y decir cuántas cifras acierta cada
     fracción (cálculo, dif. 2).
  4. Escalera contra la pared: altura exacta y aproximada (contexto, dif. 2).
  5. Perímetros y áreas con radicales — `medidas-con-radicales-8` (cálculo, dif. 2).

## Cierre del hilo

Cuatro mil años de cacería: del 3,16 del Rhind al 22/7 de Arquímedes, al 355/113 de Zu Chongzhi,
a la prueba de Lambert de que ninguna fracción es π, y a los 314 billones de cifras de hoy. La
lección matemática: hay números que no caben en ninguna fracción, y aun así podemos construirlos,
ubicarlos en la recta y calcularlos con la precisión que haga falta. Anuncio del trimestre II: del
número fijo a la letra —lenguaje algebraico, expresiones y ecuaciones (DBA 3 y 9)—.

## Evaluación (borrador de la matriz)

- **Saber:** distingue racionales de irracionales por su expresión decimal; reconoce √2, π, e, φ
  y sabe por qué 22/7 no es π.
- **Hacer:** demuestra que √2 (y √3) no es racional; construye y ubica irracionales en la recta;
  simplifica y aproxima radicales en problemas de medidas.
- **Ser:** revisa sus procedimientos y los de otros con argumentos, no con «se ve que sí».
- **Convivir:** valora que la matemática avanza cuestionando lo que parecía evidente y distingue
  lo demostrado de lo que solo se sospecha o se cuenta.

## Referencias

Todas verificadas el 2026-09-14. En la etapa C cada `\bibitem` lleva su `% verificado:`.

| Clave | Referencia | Veredicto | Corrección | URL |
|---|---|---|---|---|
| aristoteles | Aristóteles (1994). *Metafísica* (trad. T. Calvo Martínez; Biblioteca Clásica Gredos, 200). Madrid: Gredos. | confirmada | — | https://bibcatalogo.uca.es/cgi-bin/koha/opac-detail.pl?biblionumber=603122 |
| arqraices | Archimedes' calculations of square roots (arXiv:1101.0492): Arquímedes usa 265/153 < √3 < 1351/780 en *La medida del círculo*, con polígonos de 96 lados, sin explicar cómo lo obtuvo | confirmada | nueva | https://arxiv.org/pdf/1101.0492 |
| cantor (frase) | Cantor, G. (1883). *Grundlagen einer allgemeinen Mannichfaltigkeitslehre*, §8. Leipzig: Teubner; *Ges. Abh.* (1932), p. 182 | confirmada | «trad. propia»; evidencia nueva (el PDF privado anterior no sirve) | https://books.google.com/books/about/Grundlagen_einer_allgemeinen_Mannichfalt.html?id=1LPOSWUtK4UC · https://de.wikiquote.org/wiki/Georg_Cantor (solo para ubicar la página) |
| corry | Corry, L., nota «Aristotle on incommensurability» (Tel Aviv University): *Primeros analíticos* I.23 | confirmada | nueva | https://www.tau.ac.il/~corry/publications/articles/Narrative/notes/aristo.html |
| davis | Davis, P. J. (1993). *Spirals: From Theodorus to Chaos* (con W. Gautschi y A. Iserles). Taylor & Francis. | confirmada | nueva | https://books.google.com.co/books/about/Spirals.html?id=eEbvAAAAMAAJ |
| dzielska | Dzielska, M. (1995). *Hypatia of Alexandria* (trad. F. Lyra; Revealing Antiquity, 8). Cambridge, MA: Harvard University Press. | confirmada | se reformula «primera mujer matemática de la que tenemos noticias confiables» | https://bmcr.brynmawr.edu/1995/1995.07.07/ · https://mathshistory.st-andrews.ac.uk/Biographies/Hypatia/ |
| euclides | Euclides (ca. 300 a. C.). *Elementos*, Libro X (ed. electrónica de D. E. Joyce, Clark University). | confirmada (115 proposiciones, el libro más largo) | nuevo dominio; se quita «la demostración es esencialmente la de Euclides» | https://mathcs.clarku.edu/~djoyce/elements/bookX/bookX.html |
| huffman | Huffman, C. (2020). Pythagoreanism. *Stanford Encyclopedia of Philosophy* (ed. otoño 2020). | confirmada | nueva: ninguna fuente antigua liga a Hipaso con los irracionales | https://plato.stanford.edu/archives/fall2020/entries/pythagoreanism/ |
| lambert | Lambert, J. H. (1768/2004). Mémoire sur quelques propriétés remarquables des quantités transcendantes circulaires et logarithmiques. En L. Berggren, J. Borwein y P. Borwein (eds.), *Pi: A Source Book* (3.ª ed., pp. 129–140). Springer. | confirmada | presentada en 1761, publicada en 1768 | https://link.springer.com/book/10.1007/978-1-4757-4217-6 · https://mathshistory.st-andrews.ac.uk/HistTopics/Pi_through_the_ages/ |
| mactutorpi | O'Connor, J. J. y Robertson, E. F. *A history of Pi*. MacTutor History of Mathematics, University of St Andrews. | confirmada: Rhind (~1650 a. C., ≈ 3,16), Arquímedes 223/71 < π < 22/7, Zu Chongzhi (430–501) 355/113, Lambert 1761 | nueva | https://mathshistory.st-andrews.ac.uk/HistTopics/Pi_through_the_ages/ |
| mactutortheodorus | O'Connor, J. J. y Robertson, E. F. *Theodorus of Cyrene*. MacTutor (cita *Teeteto* 147d) | confirmada | nueva | https://mathshistory.st-andrews.ac.uk/Biographies/Theodorus/ |
| mendba | Ministerio de Educación Nacional (2016). *Derechos Básicos de Aprendizaje V.2: Matemáticas*. Bogotá: MEN. | confirmada | **ISBN corregido**: 978-958-691-913-5 | https://gblumen.mineducacion.gov.co/cgi-bin/koha/opac-detail.pl?biblionumber=4785 |
| storagereview | StorageReview (dic. 2025). *StorageReview Sets New Pi Record: 314 Trillion Digits on a Dell PowerEdge R7725* (110 días de cálculo). | confirmada | nueva; antes de la etapa C, revisar si hay un récord más reciente | https://www.storagereview.com/review/storagereview-sets-new-pi-record-314-trillion-digits-on-a-dell-poweredge-r7725 |
| — | ISO 216: razón √2 y conservación al doblar (dato de la aplicación) | confirmada | — | https://www.cl.cam.ac.uk/~mgk25/iso-paper.html |

Se retira `kline` (sostenía la leyenda de Hipaso, que ya no es parte del hilo).

## Etapa B — ejercicios del banco (2026-09-14)

Nuevos en `recursos/banco/matematicas/irracionales-8.py` (22 verificados con SymPy, 4 manuales
pendientes de aprobación); los demás se reutilizan tal cual. **E** = ejemplo resuelto de la
explicación; **M** = manual (la docente aprueba la respuesta modelo con
`python3 tools/ejercicios.py aprobar <id>`). Solo los `verificado` o `manual-aprobado` entran a
la guía.

| Tema | Uso | Id | Enunciado (corto) | Respuesta | Estado |
|---|---|---|---|---|---|
| 1 | E | irracionales-8-001 | 3/8 y 1/9 como decimales | 0,375 exacto; 0,(1) periódico | verificado |
| 1 | E | irracionales-8-002 | 0,(45) a fracción | 5/11 | verificado |
| 1 | E | irracionales-8-003 | 0,1(6) a fracción | 1/6 | verificado |
| 1 | 1 | irracionales-8-004 | Marina, Julián, Catalina, Marcela (DBA 1) | Marina y Catalina racionales; Julián y Marcela irracionales | **M pendiente** |
| 1 | 2 | irracionales-8-005 | 0,(6); 0,(27); 1,2(3) a fracción | 2/3; 3/11; 37/30 | verificado |
| 1 | 3 | irracionales-8-006 | Error: «0,999… ≠ 1» | 9x = 9, x = 1 | verificado |
| 1 | 4 | irracionales-8-007 | ¿22/7 es π? | 3,(142857), periódico; difiere en la 3.ª cifra | verificado |
| 2 | E | irracionales-8-008 | √2 no es racional (demostración) | por paridad | **M pendiente** |
| 2 | E | irracionales-8-010 | Llevar √2 y √5 a la recta | diagonal 1–1 y 1–2 con compás | verificado |
| 2 | 1 | irracionales-8-009 | Adaptar la demostración a √3 | 3 primo divide a p y a q | **M pendiente** |
| 2 | 2 | numeros-reales-8-001 … 006 | Ubicar 2 + √2, √5 − √3, … en la recta | aproximación y ubicación | verificado (reuso) |
| 2 | 3 | irracionales-8-011 | Espiral de Teodoro hasta √6 | √2, √3, 2, √5, √6; solo √4 racional | verificado |
| 2 | 4 | irracionales-8-012 | Hoja A4 y hoja carta: razón y doblez | A4 ≈ 1,414 se conserva; carta 1,292 → 1,548 | verificado |
| 2 | 5 | irracionales-8-013 | 7/5, 17/12, 99/70 frente a √2 | cuadrados 1,96; 2,0069; 2,0002; errores 0,0142; 0,0025; 0,00007 | verificado |
| 3 | 1 | irracionales-8-014 | 256/81, 22/7, 355/113 frente a π | 1, 2 y 6 cifras correctas | verificado |
| 3 | 2 | irracionales-8-015 | Clasificar √9, √7, −4/2, 22/7, π, 2,1010010001… | según conjuntos | verificado |
| 3 | 3 | irracionales-8-016 | ¿Suma de irracionales siempre irracional? | no: √2 + (3 − √2) = 3 | verificado |
| 3 | 4 | numeros-reales-8-025, 026 | √(5 + 4) ≠ √5 + √4 (ejemplo del DBA 2) | 3 frente a 4,236 | verificado (reuso) |
| 3 | E | irracionales-8-017 | Rueda de 66 cm: vueltas por km; error con 22/7 | 482,3 vueltas; 0,4 m de más (0,04 %) | verificado |
| 3 | 5 | irracionales-8-018 | Llanta de 58 cm: vueltas por km | ≈ 549 | verificado |
| 3 | E | irracionales-8-019 | Racional + irracional = irracional | por el absurdo | **M pendiente** |
| 4 | E+1 | irracionales-8-020 | Simplificar √50, √18, √75, √200 | 5√2, 3√2, 5√3, 10√2 | verificado |
| 4 | 2 | irracionales-8-021 | Error: √18 + √2 = √20 | 4√2 ≈ 5,66 ≠ 2√5 ≈ 4,47 | verificado |
| 4 | 2b | radicacion-8-034 | 5√2 + 8√3 + 9√2 − √3 | 14√2 + 7√3 | verificado (reuso) |
| 4 | 3 | irracionales-8-022 | 265/153 < √3 < 1351/780 (Arquímedes) | 70225 < 70227; 1825201 > 1825200; 4 y 5 cifras | verificado |
| 4 | E | irracionales-8-023 | Hexágonos: 3 < π < 2√3 | perímetros 6 y 4√3 | verificado |
| 4 | 4 | irracionales-8-024 | Escalera de 5 m, base a 2 m | √21 ≈ 4,58 m | verificado |
| 4 | 4b | irracionales-8-025 | Diagonal de 6 × 4 y de 3 × 4 | 2√13 irracional; 5 racional | verificado |
| 4 | 5 | medidas-con-radicales-8-001, 004 | Perímetro con 5√2; diagonal del cubo 5√3 | 10 + 5√2; 5√3 | verificado (reuso) |
| 4 | E | irracionales-8-026 | Televisor 32″ de razón 16 : 9 | √337 k; 27,9 × 15,7 pulgadas | verificado |

Correcciones al plan de la etapa A que salieron al verificar: el ejercicio de las diagonales
(4b) se reformuló para que sea cierto (la guía anterior decía «casi nunca es racional»); en el
ejemplo de Marcela del DBA se precisa «sin que ningún bloque se repita periódicamente»; con
22/7 el cuentakilómetros cuenta unos 0,4 m de más por km.

→ **Revisión 2:** la docente aprueba esta tabla y las 4 respuestas modelo.

## Lo que viene

- **Etapa C:** reemplazar el `.tex` actual con este plan y los ejercicios del banco
  (`% Ejercicio: <id>` encima de cada `\pregunta`).
