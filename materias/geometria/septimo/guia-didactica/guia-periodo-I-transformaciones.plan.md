# Plan de la guía — Geometría 7° · Trimestre I (etapas A y B)

> **Generación rápida (2026-09-14/15):** etapas A, B y C del skill `crear-guia` en una sola
> pasada, sin esperar las revisiones de la docente. El plan del trimestre (`plan-anual.md`) es
> todavía una **propuesta**: todo lo que sigue queda en borrador hasta la Revisión 1.

## Datos

| | |
|---|---|
| Asignatura | Geometría |
| Grado | 7° |
| Trimestre | I (semanas 01–12; sesiones 001–012 de la propuesta de `plan-anual.md`, martes, 55 min) |
| Archivo | `guia-periodo-I-transformaciones.tex` |
| Título | Escher: el arte de mover figuras |
| Hilo | **Escher: el arte de mover figuras** (opción 1 de `plan-anual.md`) |
| Registro | Juvenil (7°–11°): definiciones formales y notación, citas con fuente, justificar |
| DBA | Matemáticas grado 7 · DBA 5 |

## Por qué este hilo

- **Cubre todo el trimestre con una sola obra real y verificable.** Las tres transformaciones y su
  composición están en los teselados de M. C. Escher; sus grabados de mundos con varios «arribas»
  (*Relatividad*, 1953) sirven para las vistas, y *Reptiles* (1943), donde los lagartos salen del
  dibujo plano y vuelven a entrar, para los objetos transformados.
- **Los hechos están confirmados** en fuentes del museo Escher, de la M. C. Escher Company y de
  AramcoWorld: las visitas a la Alhambra el 19–20 de octubre de 1922 (copió un mosaico con una
  estrella de 16 puntas) y en mayo de 1936, tres días, con su esposa Jetta.
- **Trae dos matemáticas con datos verificados:** Doris Schattschneider, que estudió los cuadernos
  de Escher (*Visions of Symmetry*, 1990), y Marjorie Rice, que sin formación matemática más allá
  del colegio descubrió desde 1976 cuatro tipos nuevos de pentágonos que cubren el plano, y que
  Schattschneider confirmó.
- **Tetris** (opción 2) daba menos historia y exigía mencionar una marca; **Monge** (opción 3) solo
  sostenía las vistas.
- **No duplica con 6°** («La geometría del fútbol»): 6° mide ángulos y ve los teselados solo como
  suma de ángulos; aquí el ángulo es un giro y los teselados se hacen con transformaciones.
- **Derechos de autor:** las obras de Escher se describen; no se reproducen imágenes.

## Decisiones provisionales (a confirmar en la Revisión 1)

1. **Temas** = valores distintos de `tema` de las sesiones 002–010 de la propuesta (sin «Inicio
   del año», «Repaso» ni «Evaluación»): Ángulos (002, ya dictada, sin DBA) · Ángulos y giros ·
   Traslaciones · Rotaciones · Reflexiones · Transformaciones · Vistas de un objeto · Objetos
   transformados. Son ocho temas cortos; el primero es un repaso breve.
2. **Enteros en el plano cartesiano:** las coordenadas usan números negativos. Matemáticas 7° los
   trabaja en su Tema 1; conviene confirmar que ya se vieron antes de la semana 04.
3. **Ejes de simetría** (sesión 006) se nombran en la teoría, sin ejercicio propio, para no
   escribir otro ejercicio nuevo (regla de la docente del 2026-09-15).

## DBA y evidencias

Fuente: `dba/matematicas/grados/grado07.tex` (texto literal).

**DBA 5** — «Observa objetos tridimensionales desde diferentes puntos de vista, los representa
según su ubicación y los reconoce cuando se transforman mediante rotaciones, traslaciones y
reflexiones.»

| Evidencia | Tema que la atiende |
|---|---|
| Establece relaciones entre la posición y las vistas de un objeto. | 7 |
| Reconoce e interpreta la representación de un objeto. | 7, 8 |
| Representa objetos tridimensionales cuando se transforman. | 8 (y 2–6 en el plano, como paso previo) |

Ejemplo oficial usado: el envase visto de frente, desde arriba y desde abajo (tema 7, como
actividad de la explicación; su ejercicio abierto no se escribió, ver etapa B).

## Frase introductoria

«Pensé: qué maravilloso debe ser que alguien pueda descubrir estas cosas que nadie había visto
antes, estos patrones hermosos.» — Marjorie Rice, en N. Wolchover, «Marjorie Rice's Secret
Pentagons», *Quanta Magazine* (11 jul. 2017) (trad. propia; original: «I thought, my, that must be
wonderful that someone could discover these things which no one had seen before, these beautiful
patterns»).

## Marco teórico (redactado)

**Un joven en la Alhambra.** El 19 de octubre de 1922, Maurits Cornelis Escher, un estudiante
holandés de artes gráficas de 24 años, pasó la tarde en la Alhambra de Granada copiando un mosaico
con una estrella de 16 puntas; al día siguiente lo terminó con acuarelas [museo, aramco].

**La segunda visita.** En mayo de 1936 volvió con su esposa, Jetta: durante tres días los dos
llenaron cuadernos con notas y dibujos de los mosaicos [aramco]. Escher admiraba cómo esos
artistas llenaban el plano con figuras iguales que encajan; como allí solo hay formas
geométricas, él decidió llenar el plano con figuras reconocibles: pájaros, peces, lagartos
[museo]. Desde 1936 practicó durante años lo que llamó la «división regular del plano».

**Mover sin deformar.** Lo que hacía Escher tiene nombre matemático: una baldosa se copia con
traslaciones, rotaciones y reflexiones, movimientos que no cambian ni el tamaño ni la forma. Por
eso todas sus figuras son congruentes.

**Dos matemáticas miran a Escher.** Doris Schattschneider estudió los cuadernos del artista y
explicó con matemáticas cómo construyó sus dibujos periódicos en *Visions of Symmetry* (1990)
[schattschneider1990]. En 1975, Marjorie Rice, que vivía en San Diego y no había estudiado
matemáticas después del colegio, leyó en la revista *Scientific American* una columna de Martin
Gardner sobre los pentágonos que cubren el plano. Inventó su propia notación y encontró cuatro
tipos nuevos; Schattschneider revisó su trabajo y lo confirmó. Rice pintó además mosaicos a la
manera de Escher con sus pentágonos. Hoy se sabe que hay exactamente 15 tipos de pentágonos
convexos que cubren el plano: lo demostró Michaël Rao en 2017 [quanta, schattschneider2018].

**Mundos vistos desde varios lados.** En *Relatividad* (julio de 1953) Escher dibujó escaleras en
las que lo que para unos personajes es pared, para otros es piso: la misma construcción vista con
tres «arribas» distintos. En *Reptiles* (marzo de 1943) unos lagartos salen de un dibujo plano de
teselado, caminan en tres dimensiones sobre los objetos de un escritorio y vuelven a entrar al
dibujo [mcescher].

## Temas

Cada tema: hilo → explicación → aplicación → ejercicios → resumen.

| # | Tema | Etiqueta | Sesión | Paso del hilo | Aplicación |
|---|---|---|---|---|---|
| 1 | Ángulos | `tema:angulos` | 002 | la estrella de 16 puntas: cada punta es un ángulo | ángulos en un mosaico |
| 2 | Ángulos y giros | `tema:giros` | 003 | girar la estrella | reloj, rueda de la fortuna |
| 3 | Traslaciones | `tema:traslaciones` | 004 | una baldosa que se repite | papel de colgadura, estampados |
| 4 | Rotaciones | `tema:rotaciones` | 005 | la estrella queda igual cada 22,5° | logotipos y rines |
| 5 | Reflexiones | `tema:reflexiones` | 006 | 1936: Escher y Jetta copian los mosaicos | espejos, la palabra AMBULANCIA |
| 6 | Transformaciones | `tema:transformaciones` | 007 | la división regular del plano; Rice y Schattschneider | teselados y baldosas |
| 7 | Vistas de un objeto | `tema:vistas` | 008–009 | *Relatividad* (1953) | planos de arquitectura |
| 8 | Objetos transformados | `tema:objetostransformados` | 010 | *Reptiles* (1943) | modelado 3D y videojuegos |

## Cierre del hilo

Escher nunca estudió matemáticas formalmente, pero los matemáticos se reconocieron en su obra: lo
que él llamaba «dividir el plano» es trasladar, girar y reflejar figuras congruentes. Anuncio del
trimestre II: escalas, planos y mapas (DBA 4): no mover las figuras, sino cambiar su tamaño.

## Evaluación (borrador de la matriz)

- **Saber:** describe una traslación (vector), una rotación (centro, ángulo, sentido) y una
  reflexión (eje); reconoce las vistas de un objeto.
- **Hacer:** aplica transformaciones en el plano cartesiano y a construcciones con cubos; dibuja
  vistas.
- **Ser:** comprueba sus transformaciones midiendo lados antes de dar un resultado por bueno.
- **Convivir:** valora el trabajo de artistas y aficionados, como Escher y Rice, en la matemática.

## Referencias (verificadas el 2026-09-14/15)

| Clave | Referencia | Veredicto | URL |
|---|---|---|---|
| aramco | AramcoWorld (2023). *Artwork by M. C. Escher blending math and illusion*. | confirmada: 19 oct. 1922, estrella de 16 puntas; mayo de 1936, tres días, con Jetta | https://www.aramcoworld.com/articles/2023/escher-alhambra-infinity |
| mcescher | The M. C. Escher Company. *Gallery: Back in Holland (1941–1954)*. | confirmada: *Reptiles*, marzo de 1943, litografía; *Relativity*, julio de 1953 | https://mcescher.com/gallery/back-in-holland/ |
| mendba | Ministerio de Educación Nacional (2016). *DBA V.2: Matemáticas*. | confirmada | https://gblumen.mineducacion.gov.co/cgi-bin/koha/opac-detail.pl?biblionumber=4785 |
| museo | Escher in Het Paleis. *Wall mosaic in the Alhambra*. | confirmada: 19–20 oct. 1922; vuelve en 1936; la división regular desde 1936 | https://escherinhetpaleis.nl/escher-today/wall-mosaic-in-the-alhambra/?lang=en |
| quanta (y frase) | Wolchover, N. (2017, 11 de julio). Marjorie Rice's secret pentagons. *Quanta Magazine*. | confirmada: frase textual; cuatro tipos; 15 tipos; Rao 2017 | https://www.quantamagazine.org/marjorie-rices-secret-pentagons-20170711/ |
| schattschneider1990 | Schattschneider, D. (1990). *Visions of Symmetry: Notebooks, Periodic Drawings, and Related Work of M. C. Escher*. Nueva York: W. H. Freeman. ISBN 0-7167-2126-0. | confirmada | https://openlibrary.org/books/OL1851833M/Visions_of_symmetry |
| schattschneider2018 | Schattschneider, D. (2018). Marjorie Rice and her pentagonal tilings. *Bridges 2018 Conference Proceedings*. | confirmada: sin formación más allá del colegio; columna de julio de 1975; cuatro tipos nuevos | https://archive.bridgesmathart.org/2018/bridges2018-1.pdf |

Quitado o parafraseado:
- «Los moros eran maestros en el arte de llenar un plano con figuras iguales que encajan» se
  atribuye a Escher, pero solo se encontró en una fuente secundaria (AramcoWorld), sin la obra
  original: va parafraseada.
- La frase de Hermann Weyl sobre la simetría (*Symmetry*, 1952) no se pudo ver en un escaneo:
  no se usa.
- Las imágenes de Escher no se reproducen (derechos de The M. C. Escher Company).

## Etapa B — ejercicios (2026-09-15)

Reglas de la docente del 2026-09-15: la guía usa **solo ejercicios del banco**; si el banco no
tiene nada para un tema, se escribe **lo mínimo**, verificado con `--sin-registro` y marcado como
nuevo. **El banco no tenía ningún ejercicio de giros, transformaciones ni vistas** en ningún grado
(búsqueda de «traslación», «rotación», «reflexión», «simetría», «vista» en todos los archivos), así
que cada tema del 2 al 8 lleva **un** ejercicio nuevo. Sin ejercicios abiertos nuevos.

| Tema | Id | Enunciado (corto) | Respuesta | Estado | Origen |
|---|---|---|---|---|---|
| 1 | angulos-6-002 | Suplementarios iguales → rectos | 90° | verificado | reuso (banco de 6°, repaso) |
| 1 | angulos-6-003 | Complementarios iguales → 45° | 45° | verificado | reuso (banco de 6°, repaso) |
| 2 | angulos-7-003 | 270° antihorario = 90° horario | sí, suman 360° | verificado | **nuevo** |
| 3 | transformaciones-7-001 | Trasladar A(1,1), B(4,1), C(2,3) con ⟨3, 2⟩ | (4,3), (7,3), (5,5) | verificado | **nuevo** |
| 4 | transformaciones-7-004 | Girar P(3,1) 90°, 180°, −90° | (−1,3), (−3,−1), (1,−3) | verificado | **nuevo** |
| 5 | transformaciones-7-009 | Error: reflexión = giro de 180° | (−2,3) ≠ (−2,−3) | verificado | **nuevo** |
| 6 | transformaciones-7-012 | Giro y traslación: ¿congruentes? | lados 2, 3, √13; sí | verificado | **nuevo** |
| 7 | vistas-7-001 | Plano de alturas: cubos y vistas | 10; 3-1-2; 2-3 | verificado | **nuevo** |
| 8 | vistas-7-004 | Construcción girada 90° | 2 3 / 1 1 / 1 2; 10 cubos | verificado | **nuevo** |

Nuevos: **7** (`recursos/banco/matematicas/angulos-7.py`, `transformaciones-7.py`, `vistas-7.py`);
reusados: 2. Pendiente de registrar: una sesión corre `python3 tools/ejercicios.py verificar`
(sin `--sin-registro`) cuando terminen los agentes en paralelo.

**Lo que queda sin ejercicio** (la skill pide 2–5 por tema; aquí hay 1 por la regla de la docente):
- Tema 1: la clasificación por medida (solo hay las dos demostraciones de 6°).
- Tema 5: ejes de simetría (se explican en la teoría).
- Tema 6: teselados propios (la baldosa «a lo Escher» sería abierta).
- Tema 7: el ejemplo del DBA 5 (dibujar las vistas de un envase y compararlas con fotos) queda
  como actividad en la explicación, sin ejercicio (sería abierto).
- Tema 8: reflejar una construcción en un espejo (queda como ejemplo resuelto).

No se usó ningún recurso de 7°: los módulos no traen transformaciones ni vistas.
