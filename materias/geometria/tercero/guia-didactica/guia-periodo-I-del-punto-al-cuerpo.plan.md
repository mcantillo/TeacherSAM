# Plan de la guía — Geometría 3° · Trimestre I (etapas A y B)

> **Generación rápida (2026-09-14):** etapas A, B y C del skill `crear-guia` hechas en una sola
> pasada, sin las revisiones intermedias de la docente. El plan del trimestre
> (`curriculo/plan-anual.md`) es todavía una **propuesta** sin aprobar y `programacion.csv` no
> tiene las filas 003–012: esta guía es un **borrador** que se ajusta cuando la docente apruebe
> el plan, el hilo y los ejercicios.

## Datos

| | |
|---|---|
| Asignatura | Geometría |
| Grado | 3° |
| Trimestre | I (semanas 03–11; clases 003–011 de la propuesta; 001 inicio de año y 002 punto, línea y plano ya dictadas; 012 evaluación) |
| Archivo | `guia-periodo-I-del-punto-al-cuerpo.tex` |
| Título | Del punto al cuerpo |
| Hilo | **Rinrín Renacuajo sale de paseo** (opción A del plan anual, la recomendada; el nombre se distingue del de la plantilla de 3°, «El paseo de Rinrín Renacuajo», que `revisar_guia.py` marca como texto de ejemplo) |
| Registro | 3° (≈ 8–9 años): oraciones cortas, trato cercano, cada palabra nueva con dibujo; anécdotas «¿Sabías que…?» sin citas textuales (salvo la frase de apertura, de dominio público); trabajo manipulativo: dibujar, contar, pasar el dedo, recortar, armar |

## Por qué este hilo

Se eligió la opción A porque es la que mejor conecta con la matemática del trimestre y con la
edad: Rinrín **sale de su charco** (el borde del charco es una línea cerrada: dentro, fuera y en
el borde), **deja caminos** rectos y curvos (tema Líneas), llega a la **casa de Doña Ratona**,
hecha de figuras planas (tema Figuras planas), y en la **tienda** encuentra cajas, latas y conos
(tema Cuerpos). Es un cuento colombiano de dominio público (Pombo, 1867), el personaje explora,
como pide el registro de 3°, y hay una plantilla del grado que ya lo usa. La opción B (la
hormiga) es parecida pero con menos lugares; la C (liebre y tortuga) gira alrededor de una
carrera, que se presta más a caminos y posición (DBA 7, trimestre III) que a formas.

**Cuidado con el cuento:** en el poema original el paseo termina mal (unos gatos se comen al Ratón y a Doña
Ratona, y un pato se come a Rinrín). La guía usa **una versión propia** que se queda en el
paseo y en la visita, y termina con Rinrín de regreso en su charco. Solo se cita textualmente el
comienzo del poema.

## DBA y evidencias

Fuente: `dba/matematicas/grados/grado03.tex` (texto literal).

**DBA 6** — «Describe y representa formas bidimensionales y tridimensionales de acuerdo con las
propiedades geométricas.»

| Evidencia | Tema que la atiende |
|---|---|
| Relaciona objetos de su entorno con formas bidimensionales y tridimensionales, nombra y describe sus elementos. | 1 (líneas en el salón), 2 (lados y vértices), 3 (caras, aristas y vértices), 4 (objetos ↔ figuras y cuerpos) |
| Clasifica y representa formas bidimensionales y tridimensionales tomando en cuenta sus características geométricas comunes y describe el criterio utilizado. | 1 (abiertas/cerradas, rectas/curvas), 2 (clasificar por número de lados y decir la regla), 3 (ruedan / no ruedan) |
| Interpreta, compara y justifica propiedades de formas bidimensionales y tridimensionales. | 2 (el cuadrado girado sigue siendo cuadrado), 3 (caras que son figuras planas; el dado no tiene 6 vértices), 4 (adivinanzas y mensajes) |

**Ejemplo del DBA como cierre:** la profesora de tercero tiene un prisma rectangular, un prisma
triangular y un cilindro; David y María faltaron y hay que escribirles un mensaje, sin dibujos,
para que los construyan (tema 4). Los mensajes de Patricia y Román del DBA son imágenes que no
se extrajeron en `dba/`. El mensaje es el ejercicio formas-3-003 (manual pendiente de aprobación).

## Frase introductoria

«El hijo de Rana, Rinrín Renacuajo, salió esta mañana muy tieso y muy majo, con pantalón corto,
corbata a la moda, sombrero encintado y chupa de boda.» — Rafael Pombo, *El renacuajo paseador*,
en *Cuentos pintados para niños* (Nueva York: Appleton, 1867). Dominio público. Ya verificada en
`REFERENCE.md` y en la plantilla de 3°.

## Marco teórico (redactado, «¿Sabías que…?»)

**El poeta que estudió matemáticas.** Rafael Pombo nació en Bogotá en 1833 y murió allí en
1912. Antes de ser el poeta de los niños colombianos estudió matemáticas e ingeniería en el
Colegio Militar. Sus *Cuentos pintados para niños*, donde está Rinrín, se publicaron en Nueva
York en 1867 [banrep-pombo, pombo].

**Un libro de formas muy antiguo.** Hace más de 2 000 años, un maestro griego llamado Euclides
escribió los *Elementos*. Empieza así: un **punto** es lo que no tiene partes, y una **línea**
es un largo sin ancho. Con puntos y líneas se arman todas las figuras [euclides]. (Enlace con la
clase 002: el punto de luz del láser.)

**Las abejas y los hexágonos.** Las celdas del panal tienen seis lados. En 2001, el matemático
Thomas Hales demostró que, para dividir un piso en partes del mismo tamaño, los hexágonos son
la forma que usa menos borde. Por eso se piensa que las abejas ahorran cera [hales].

## Temas

Los valores distintos de `tema` de las clases 003–011 de la propuesta, en orden. No hay clases
escritas que citen las etiquetas todavía.

### Tema 1 — Líneas · `tema:lineas`

Clases 003–004 (semanas 03–04). DBA 6.

- **Hilo:** Rinrín sale de su charco y deja caminos en la arena: unos rectos, otros curvos; unos
  que vuelven al charco y otros que no.
- **Explicación:** repaso de punto y línea (clase 002, láser); líneas rectas y curvas; posición:
  horizontal, vertical, inclinada (con dibujo de la casa y el salón); líneas abiertas y
  cerradas («si terminas donde empezaste sin levantar el lápiz, es cerrada»); una línea cerrada
  separa: dentro, fuera y en el borde.
- **Aplicación:** las líneas de la cancha del colegio: la línea del borde es cerrada y dice si
  el balón está dentro o fuera.
- **Ejercicios planeados:** reconocer rectas y curvas (dif. 1); posición de líneas (dif. 1);
  abiertas y cerradas (dif. 1); dentro/fuera/borde (dif. 1); buscar líneas en el salón (manual);
  argumentar si se puede cerrar con rectas o con una curva (manual, dif. 2).

### Tema 2 — Figuras planas · `tema:figuras`

Clases 005–008 (semanas 05–08; quiz en la 007 después del receso). DBA 6.

- **Hilo:** Rinrín encuentra a su vecino el Ratón y juntos van a visitar a Doña Ratona. Su casa
  está hecha de figuras.
- **Explicación:** de la línea cerrada a la figura; triángulo, cuadrado, rectángulo, círculo;
  lado y vértice; contar y comparar; el cuadrado girado sigue siendo cuadrado; clasificar por
  número de lados y **decir la regla**.
- **Aplicación:** señales de tránsito: la de PARE tiene 8 lados; la de CEDA EL PASO es un
  triángulo (se reconocen de lejos por su forma).
- **Ejercicios planeados:** tabla de lados y vértices (dif. 1); contar figuras en la casa de
  Doña Ratona (contexto, dif. 1); clasificar seis figuras y decir el criterio (dif. 2);
  encontrar el error del cuadrado «de punta» (dif. 2); casita con palitos (contexto, dif. 2);
  dibujar una figura de 5 lados (manual).

### Tema 3 — Cuerpos geométricos · `tema:cuerpos`

Clases 009–010 (semanas 09–10). DBA 6.

- **Hilo:** de regreso, Rinrín pasa por la tienda del barrio: cajas de cereal, latas, pelotas y
  conos de helado. «¡Estas formas se pueden agarrar!»
- **Explicación:** cubo, caja (prisma rectangular), cilindro, esfera, cono, pirámide y prisma
  triangular; caras, aristas y vértices; las caras son figuras planas; ruedan / no ruedan.
- **Aplicación:** en la tienda las cajas se apilan porque sus caras son planas; las latas se
  acuestan y ruedan.
- **Ejercicios planeados:** tabla de caras, aristas y vértices (dif. 2); qué figuras son las caras
  de la pirámide y del prisma triangular (dif. 2); error «el dado tiene 6 vértices» (dif. 2);
  lana en las aristas de la caja (contexto, dif. 1); ruedan / no ruedan con explicación (manual).

### Tema 4 — Formas a mi alrededor · `tema:formas`

Clase 011 (semana 11; quiz). DBA 6 (ejemplo oficial).

- **Hilo:** en casa, Rinrín le cuenta a Mamá Rana todo lo que vio… sin poder mostrarle dibujos.
- **Explicación:** relacionar objetos con figuras y con cuerpos (la huella de una cara es una
  figura plana); describir un cuerpo solo con palabras: cuántas caras, qué figura es cada una y
  de qué tamaño.
- **Aplicación:** las instrucciones de armado de un juguete o de una caja de regalo.
- **Ejercicios planeados:** adivinanzas de cuerpos (dif. 2); la huella de cada cuerpo (dif. 1);
  mensaje a David y María (ejemplo del DBA, manual, dif. 3); mejorar los mensajes de Patricia y
  Román (manual, dif. 2).

## Cierre del hilo

Rinrín vuelve a su charco antes de que oscurezca (versión propia: no hay gato ni pato). En un
solo paseo vio líneas, figuras y cuerpos: del punto al cuerpo. Anuncio del trimestre II: medir
—el contorno y el recubrimiento de las figuras (DBA 4 y 5)—.

## Evaluación (matriz)

- **Saber:** nombra líneas, figuras planas y cuerpos, y sus partes (lados, vértices, caras, aristas).
- **Hacer:** clasifica líneas, figuras y cuerpos y dice la regla que usó.
- **Ser:** explora con curiosidad las formas de su casa y su colegio.
- **Convivir:** escucha y mejora las descripciones de sus compañeros con respeto.

## Referencias

Verificadas el 2026-09-14/15. En la etapa C cada `\bibitem` lleva su `% verificado:`.

| Clave | Referencia | Veredicto | Corrección | URL |
|---|---|---|---|---|
| pombo (frase) | Pombo, R. (1867). *Cuentos pintados para niños*. Nueva York: D. Appleton y Cía. | confirmada (el enlace responde con el PDF del libro; texto del poema contrastado en Wikisource) | — | https://babel.banrepcultural.org/digital/api/collection/p17054coll10/id/2720/download · https://es.wikisource.org/wiki/El_renacuajo_paseador |
| banrep-pombo | Banco de la República. *Rafael Pombo*. Enciclopedia de la Red Cultural del Banco de la República: nació en Bogotá el 7 nov. 1833, murió el 5 may. 1912; doctor en matemáticas e ingeniería del Colegio Militar; *Cuentos pintados* en Appleton, 1867 | confirmada | nueva | https://enciclopedia.banrepcultural.org/Rafael_Pombo |
| euclides | Euclides. *Elementos*, Libro I, definiciones 1 y 2 (ed. electrónica de D. E. Joyce, Clark University): «A point is that which has no part»; «A line is breadthless length» | confirmada | se cambia la edición Gredos de la plantilla por la de Joyce, que muestra el texto | https://mathcs.clarku.edu/~djoyce/elements/bookI/bookI.html |
| hales | Hales, T. C. (2001). The honeycomb conjecture. *Discrete & Computational Geometry*, 25(1), 1–22. | confirmada | — | https://arxiv.org/abs/math/9906042 |
| mendba | Ministerio de Educación Nacional (2016). *Derechos Básicos de Aprendizaje V.2: Matemáticas*. Bogotá: MEN. | confirmada | — | https://gblumen.mineducacion.gov.co/cgi-bin/koha/opac-detail.pl?biblionumber=4785 |

Se retira de la plantilla de 3° la anécdota de Hipatia («muchos estudiantes viajaban desde
lejos para escucharla»): la reseña del libro de Dzielska no la sostiene, y no hace falta aquí.

## Etapa B — ejercicios del banco (2026-09-15)

**Excepción aprobada por la docente (2026-09-15):** en grados sin ningún ejercicio en el banco,
la guía puede traer ejercicios nuevos, los mínimos, uno o dos por tema y cubriendo las
evidencias. **Reutilizados: ninguno** — el banco no tiene ejercicios de 3°, y en 2°, 4°–7° no hay
ninguno de líneas, figuras o cuerpos a este nivel. **Todos son NUEVOS: 8 (7 verificados + 1
manual pendiente)**, en `recursos/banco/matematicas/lineas-3.py`, `figuras-planas-3.py`,
`cuerpos-geometricos-3.py`, `formas-3.py` (`verificar --sin-registro`, 0 fallas; ids con huecos
porque versiones anteriores más largas nunca se registraron). Los dibujos de la guía usan las
mismas coordenadas que las comprobaciones; caras, aristas y vértices se calculan con una
envolvente convexa, con la fórmula de Euler como control.

| Tema | Id | Enunciado (corto) | Respuesta | Estado | Nuevo: evidencia que cubre |
|---|---|---|---|---|---|
| 1 | lineas-3-002 | Horizontal, vertical, inclinada (dibujo) | 1 h, 2 v, 3 i, 4 h | verificado (nuevo) | 1: nombra y describe (líneas) |
| 1 | lineas-3-004 | Dentro, fuera y borde del charco | Rinrín dentro; mosca fuera; flor y hoja en el borde | verificado (nuevo) | 2: clasifica (línea cerrada) |
| 2 | figuras-planas-3-003 | Clasificar seis figuras y decir la regla | 3: A, D; 4: B, C, F; 5: E | verificado (nuevo) | 2: clasifica y describe el criterio |
| 2 | figuras-planas-3-004 | Error: «de punta no es cuadrado» | sí es cuadrado | verificado (nuevo) | 3: justifica propiedades |
| 3 | cuerpos-geometricos-3-001 | Caras, aristas, vértices de 4 cuerpos | 6-12-8, 6-12-8, 5-8-5, 5-9-6 | verificado (nuevo) | 1: nombra elementos |
| 3 | cuerpos-geometricos-3-003 | Error: «el dado tiene 6 vértices» | 8 | verificado (nuevo) | 3: justifica propiedades |
| 4 | formas-3-001 | Adivinanzas de cuerpos | cubo, prisma triangular, pirámide | verificado (nuevo) | 1 y 3: relaciona caras y cuerpos |
| 4 | formas-3-003 | Mensaje a David y María (ejemplo del DBA) | modelo con caras y medidas | **manual-pendiente (nuevo)**, comentado en la guía | ejemplo oficial del DBA 6 |

## Preguntas para la docente


1. ¿Aprueba el plan del trimestre, el hilo A y la versión amable del cuento (sin gato ni pato)?
2. Las 6 respuestas modelo manuales (tabla de arriba): ¿las aprueba? En la guía van comentadas.
3. ¿Incluye el prisma triangular y la pirámide en 3° (aparecen en el ejemplo del DBA y en la
   propuesta), o solo cubo, caja, cilindro, esfera y cono?
