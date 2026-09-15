# Plan de la guía — Geometría 4° · Trimestre I (etapas A y B)

> **Generación rápida (2026-09-14):** etapas A, B y C del skill `crear-guia` hechas en una sola
> pasada, sin las revisiones intermedias de la docente. El plan del trimestre
> (`curriculo/plan-anual.md`) es todavía una **propuesta** sin aprobar y `programacion.csv` no
> tiene las filas 003–012: esta guía es un **borrador** que se ajusta cuando la docente apruebe
> el plan, el hilo y los ejercicios.

## Datos

| | |
|---|---|
| Asignatura | Geometría |
| Grado | 4° |
| Trimestre | I (semanas 03–11; clases 003–011 de la propuesta; 001 inicio de año y 002 recta y paralelas ya dictadas; 012 evaluación) |
| Archivo | `guia-periodo-I-lineas-y-poligonos.tex` |
| Título | Líneas y polígonos alrededor del mundo |
| Hilo | **La vuelta al mundo en 80 días** (Julio Verne, 1872), contada con nuestras palabras (opción A del plan anual, la recomendada) |
| Registro | 4° (≈ 9–10 años): frases más largas; términos geométricos con definición sencilla; aventuras y viajes; contextos de casa, barrio, deportes y mapas; anécdotas breves y una cita muy corta; del concreto al dibujo, primeros procedimientos escritos (trazar con regla y escuadra); sin mascotas |

## Por qué este hilo

La opción A es la mejor de las tres: es el ejemplo del propio registro de 4°, es de dominio
público, y el viaje de Phileas Fogg está hecho de **trenes y barcos**, donde las líneas son
protagonistas (rieles paralelos, durmientes perpendiculares, rutas que se cruzan). Además es un
viaje por **etapas** con un itinerario exacto de 8 tramos que suman 80 días (cap. III), igual que
el trimestre avanza tema por tema, y termina con una sorpresa matemática (el día ganado al viajar
hacia el este, cap. XXXVII). No se cruza con el hilo de 3° (cuento y animales) ni con el de 5°
(Cali y los planos). La B (expedición por el colegio) se parece al trabajo de planos de 5°; la C
(inventos) no tiene una historia que avance.

**Cuidado con la novela:** se usan solo los pasajes amables (la apuesta en el Reform Club, los
trenes, los barcos, el elefante, el día ganado). Se omiten el rescate de Aouda de la pira
funeraria y el ataque al tren en Estados Unidos (violencia). El tangram del tema 4 **no está en la
novela**: se presenta como parte de «nuestra versión» (Passepartout se entretiene en el largo cruce
del Pacífico).

## DBA y evidencias

Fuente: `dba/matematicas/grados/grado04.tex` (texto literal).

**DBA 6** — «Identifica, describe y representa figuras bidimensionales y tridimensionales, y
establece relaciones entre ellas.»

| Evidencia | Tema que la atiende |
|---|---|
| Arma, desarma y crea formas bidimensionales y tridimensionales. | 4 (tangram: armar figuras con las 7 piezas y con dos triangulitos), 3 (construir cuadriláteros en cuadrícula) |
| Reconoce entre un conjunto de desarrollos planos, los que corresponden a determinados sólidos atendiendo a las relaciones entre la posición de las diferentes caras y aristas. | **No en este trimestre**: la parte tridimensional va en el trimestre III, según `plan-anual.md` |

El enunciado del DBA pide además *identificar, describir y representar* figuras
bidimensionales y *establecer relaciones entre ellas*: temas 2 y 3 (polígonos y cuadriláteros,
el cuadrado como rectángulo especial). **Líneas paralelas y perpendiculares** no están en los DBA
de 4°: son del DBA 7 de 2° («Describe desplazamientos y referencia la posición de un objeto
mediante nociones de horizontalidad, verticalidad, paralelismo y perpendicularidad…»); el tema 1
las retoma como herramienta para describir los cuadriláteros (tema 3), según la nota de
`plan-anual.md`. El ejemplo del DBA 6 de 4° (esculturas con cubos y medios cubos) es
tridimensional y queda para el trimestre III.

## Frase introductoria

«Lo imprevisto no existe.» — Phileas Fogg, en Julio Verne, *La vuelta al mundo en 80 días*
(1872), cap. III (trad. propia del original «L'imprévu n'existe pas»). Cita muy corta y sencilla,
como permite el registro de 4°. En la introducción se explica con palabras propias: Fogg planeó
su viaje con un itinerario exacto, como un geómetra que traza con regla y escuadra.

## Marco teórico (redactado, «¿Sabías que…?» breves)

**Una novela por entregas.** Julio Verne publicó *La vuelta al mundo en 80 días* por capítulos en
el periódico francés *Le Temps*, entre noviembre y diciembre de 1872; el libro completo salió en
enero de 1873 [cijv]. En ella, el inglés Phileas Fogg apuesta veinte mil libras a que puede dar la
vuelta al mundo en 80 días, y sale con su criado, Passepartout [verne].

**Un itinerario de 8 tramos.** El plan de Fogg: Londres–Suez (7 días), Suez–Bombay (13),
Bombay–Calcutá (3), Calcuta–Hong Kong (13), Hong Kong–Yokohama (6), Yokohama–San Francisco (22),
San Francisco–Nueva York (7) y Nueva York–Londres (9): en total, 80 días [verne].

**Una periodista que lo hizo de verdad.** En 1889, la periodista estadounidense Nellie Bly leyó la
novela y decidió intentarlo. Lo logró en 72 días, y el periódico *New York World* contó su viaje
día por día [nwhm].

**Paralelas desde hace 2 300 años.** En los *Elementos*, Euclides definió las rectas paralelas
como las que están en el mismo plano y, prolongadas indefinidamente hacia los dos lados, no se
encuentran nunca [euclides]. Es la misma idea que usamos hoy.

**Un rompecabezas chino.** El tangram (en chino, «siete piezas ingeniosas») se inventó en China
hacia 1800; en 1817 y 1818 se volvió una moda en Europa, y se considera la primera gran fiebre de
los rompecabezas [britz].

## Temas

Los valores distintos de `tema` de las clases 003–011 de la propuesta, en orden. No hay clases
escritas que citen las etiquetas todavía.

### Tema 1 — Líneas · `tema:lineas`

Clases 003–006 (semanas 03–06; quiz en la 006, antes del receso).

- **Hilo:** en el Reform Club de Londres, Fogg apuesta que dará la vuelta al mundo en 80 días.
  El primer tramo es en tren: los dos rieles nunca se encuentran.
- **Explicación:** recta, segmento y semirrecta (con dibujo y notación); rectas paralelas,
  secantes y perpendiculares; el ángulo recto como la «esquina» de la escuadra; cómo trazar una
  paralela y una perpendicular con regla y escuadra (procedimiento escrito); definición de
  Euclides: «prolongadas, no se encuentran».
- **Aplicación:** la vía del tren: rieles paralelos para que las ruedas no se salgan y durmientes
  perpendiculares a los rieles.
- **Ejercicios planeados:** clasificar parejas de rectas (dif. 1); encontrar el error «no se tocan, entonces
  son paralelas» (dif. 2).

### Tema 2 — Polígonos · `tema:poligonos`

Clases 007–008 (semanas 07–08).

- **Hilo:** en el barco hacia Suez y Bombay, Passepartout dibuja en su libreta las formas del
  barco: ventanas, velas y banderas, todas con lados rectos.
- **Explicación:** línea poligonal abierta y cerrada; polígono (cerrado, solo lados rectos);
  lados, vértices y ángulos (tantos como lados); nombres: triángulo, cuadrilátero, pentágono,
  hexágono, octágono.
- **Aplicación:** las señales de tránsito: la de PARE es un octágono y la de CEDA EL PASO un
  triángulo; se reconocen por la forma aunque no se lean.
- **Ejercicios planeados:** ¿es polígono o no? (dif. 1); contar lados, vértices y ángulos y nombrar (dif. 1).

### Tema 3 — Cuadriláteros · `tema:cuadrilateros`

Clases 009–010 (semanas 09–10).

- **Hilo:** en Hong Kong y Yokohama, Passepartout recorre calles con baldosas, ventanas y
  cometas: muchos cuadriláteros distintos. ¿Cómo distinguirlos?
- **Explicación:** cuadrado, rectángulo, rombo, trapecio según lados iguales, lados paralelos y
  ángulos rectos (tabla); el cuadrado es un rectángulo y también un rombo; construir en cuadrícula
  o geoplano.
- **Aplicación:** baldosas y ventanas (rectángulos y cuadrados, para que encajen sin huecos); la
  cometa en forma de rombo.
- **Ejercicios planeados:** clasificar cinco cuadriláteros en cuadrícula (dif. 2); argumentar «¿el cuadrado
  es un rectángulo? ¿todo rombo es cuadrado?» (dif. 3).

### Tema 4 — Figuras con polígonos · `tema:tangram`

Clase 011 (semana 11; quiz y repaso).

- **Hilo:** en nuestra versión, en los 22 días de barco de Yokohama a San Francisco, Passepartout
  se entretiene con un rompecabezas chino de siete piezas.
- **Explicación:** las 7 piezas del tangram (5 triángulos, un cuadrado, un paralelogramo); armar y
  desarmar: con dos triángulos pequeños se arman un cuadrado, un triángulo y un paralelogramo;
  crear figuras con las 7 piezas.
- **Aplicación:** los mosaicos y los pisos: figuras armadas con polígonos que encajan sin huecos.
- **Ejercicios planeados:** reconocer las piezas (dif. 1); armar tres figuras con dos triangulitos (dif. 2).

## Cierre del hilo

Fogg llega a Londres creyendo que perdió la apuesta por un día… pero la ganó: al viajar siempre
hacia el este, cada día fue un poco más corto; 360 grados por 4 minutos cada uno son 24 horas: un
día entero ganado (cap. XXXVII) [verne]. Anuncio del trimestre II: medir —longitudes, perímetro y
área (DBA 5)—.

## Evaluación (matriz)

- **Saber:** reconoce rectas paralelas, perpendiculares y secantes, polígonos y cuadriláteros por
  sus propiedades.
- **Hacer:** traza paralelas y perpendiculares con regla y escuadra; clasifica cuadriláteros; arma
  figuras con polígonos.
- **Ser:** planea y revisa su trabajo con cuidado, como Fogg su itinerario.
- **Convivir:** comparte las piezas y las ideas en el trabajo con tangram y respeta las figuras
  de los demás.

## Referencias

Verificadas el 2026-09-14/15. En la etapa C cada `\bibitem` lleva su `% verificado:`.

| Clave | Referencia | Veredicto | Corrección | URL |
|---|---|---|---|---|
| verne (frase) | Verne, J. (1873). *Le Tour du monde en quatre-vingts jours*. París: Hetzel. Cap. III: «L'imprévu n'existe pas» (Fogg), la apuesta de 20 000 libras y el itinerario de 8 tramos = 80 días; cap. XXXVII: 360° × 4 min = 24 h | confirmada (texto en Wikisource) | trad. propia | https://fr.wikisource.org/wiki/Le_Tour_du_monde_en_quatre-vingts_jours/Chapitre_3 · https://fr.wikisource.org/wiki/Le_Tour_du_monde_en_quatre-vingts_jours/Chapitre_37 |
| cijv | Centre international Jules Verne. *Le Tour du monde en quatre-vingts jours* (1872–1873): *Le Temps*, nov.–dic. 1872; Hetzel, 30 ene. 1873 | confirmada | — | https://jules-verne.net/l-oeuvre/les-voyages-extraordinaires/1872-1873-1-le-tour-du-monde-en-quatre-vingts-jours/ |
| nwhm | National Women's History Museum. *Nellie Bly* (biografía): viaje de 72 días en 1889, *New York World*, inspirado en Verne | confirmada | la guía de la Library of Congress respondió 403 | https://www.womenshistory.org/education-resources/biographies/nellie-bly-0 |
| euclides | Euclides. *Elementos*, Libro I, def. 23 (ed. electrónica de D. E. Joyce, Clark University) | confirmada | — | https://mathcs.clarku.edu/~djoyce/elements/bookI/bookI.html |
| britz | Britz, T. (2022, 28 dic.). The history and mystery of Tangram… *The Conversation*: invento chino hacia 1800, 7 piezas (5 triángulos, cuadrado, paralelogramo), fiebre en Europa en 1817–18 | confirmada | nueva | https://theconversation.com/the-history-and-mystery-of-tangram-the-childrens-puzzle-game-that-harbours-a-mathematical-paradox-or-two-190529 |
| mintransporte | Ministerio de Transporte (2015). *Manual de señalización vial* (Resolución 1885 de 2015): la señal SR-01 PARE es un octágono | confirmada a través de una ficha técnica oficial (Unidad de Mantenimiento Vial de Bogotá, Colombia Compra) que cita la resolución: «misma forma … de la señal SR-01 Pare … un octágono» | la página de la ANSV (manual vigente) no deja leer el anexo | https://operaciones.colombiacompra.gov.co/sites/cce_public/files/documentos_adicionales_oc/ficha_tecnica_48.pdf · https://ansv.gov.co/es/publicaciones/manual-de-senalizacion-vial |
| mendba | Ministerio de Educación Nacional (2016). *Derechos Básicos de Aprendizaje V.2: Matemáticas*. Bogotá: MEN. | confirmada | — | https://gblumen.mineducacion.gov.co/cgi-bin/koha/opac-detail.pl?biblionumber=4785 |

## Etapa B — ejercicios del banco (2026-09-15)

**Excepción aprobada por la docente (2026-09-15):** en grados sin ningún ejercicio en el banco,
la guía puede traer ejercicios nuevos, los mínimos, uno o dos por tema y cubriendo las
evidencias. **Reutilizados: ninguno** — el banco no tiene ejercicios de 4°, y en 2°, 3°, 5°–7° no
hay ninguno de paralelas, polígonos, cuadriláteros o tangram a este nivel (`poligonos-6` está
sin verificar y es de otro curso). **Todos son NUEVOS: 8, todos verificados, sin abiertos**, en
`recursos/banco/matematicas/lineas-4.py`, `poligonos-4.py`, `cuadrilateros-4.py`,
`tangram-4.py` (`verificar --sin-registro`, 0 fallas; ids con huecos porque versiones anteriores
más largas nunca se registraron). Todo se comprueba desde las coordenadas de los dibujos.

| Tema | Id | Enunciado (corto) | Respuesta | Estado | Nuevo: qué cubre |
|---|---|---|---|---|---|
| 1 | lineas-4-001 | Parejas de rectas r, s, t, u | r∥s; t⊥r; t⊥s; r y u secantes | verificado (nuevo) | posiciones de rectas (base DBA 7 de 2°) |
| 1 | lineas-4-003 | Error: «no se tocan, son paralelos» | se cortan al prolongarlos | verificado (nuevo) | argumentar con la definición |
| 2 | poligonos-4-001 | ¿Polígono o no? | 1 y 4 sí; 2 abierta; 3 lado curvo | verificado (nuevo) | identifica figuras bidimensionales |
| 2 | poligonos-4-002 | Lados, vértices, ángulos y nombre (A–E) | 3, 4, 5, 6, 8 | verificado (nuevo) | describe y nombra |
| 3 | cuadrilateros-4-001 | Clasificar A–E en cuadrícula | cuadrado, rectángulo, rombo, trapecio, ninguno | verificado (nuevo) | describe y clasifica |
| 3 | cuadrilateros-4-003 | ¿Cuadrado es rectángulo? ¿Rombo es cuadrado? | sí; no | verificado (nuevo) | establece relaciones entre figuras |
| 4 | tangram-4-001 | Piezas del tangram | 5 triángulos, cuadrado, paralelogramo | verificado (nuevo) | evidencia 1: desarma |
| 4 | tangram-4-003 | Tres figuras con dos triangulitos | cuadrado, triángulo, paralelogramo | verificado (nuevo) | evidencia 1: arma y crea |

La evidencia 2 (desarrollos planos) no se trabaja en este trimestre (va en el III).

## Preguntas para la docente


1. ¿Aprueba el plan del trimestre, el hilo A y el uso libre del tangram dentro de «nuestra
   versión» (no está en la novela)?
2. ¿Se trabajan paralelas y perpendiculares aunque no estén en los DBA de 4° (son del DBA 7 de
   2°)? La guía las usa como base para los cuadriláteros.
3. La segunda evidencia del DBA 6 (desarrollos planos) no entra en este trimestre: ¿confirma que
   va en el III?
