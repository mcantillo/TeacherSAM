# Plan de la guía — Física 10° · Trimestre I (etapas A y B)

> **BORRADOR — generación rápida (2026-09-14/15)**, etapas A, B y C en una sola pasada por
> pedido de la docente. La fuente es la **propuesta** de `curriculo/plan-anual.md` (clases
> 005–024), todavía **no aprobada** ni escrita en `programacion.csv`.

## Datos

| | |
|---|---|
| Asignatura | Física |
| Grado | 10° (dos sesiones semanales de 100 min) |
| Trimestre | I (semanas 01–12; clases 001–024) |
| Archivo | `guia-periodo-I-leyes-newton.tex` |
| Título | Fuerza y movimiento: las leyes de Newton |
| Hilo | **De la inercia a los *Principia*** (opción A de `plan-anual.md`) |
| Registro | Juvenil |

### Por qué este hilo y cómo no se cruza con el de 9°

- Recorre todo el trimestre: medir (Galileo y su reloj de agua; hoy el SI), describir (el
  repaso de cinemática), y explicar con fuerzas (las tres leyes de los *Principia*, 1687).
  Las opciones B (Goddard) y C (el metro) solo sostienen una parte del trimestre.
- Tiene una científica con papel real en la historia: Émilie du Châtelet, cuya traducción
  comentada de los *Principia* sigue siendo la francesa de referencia.
- **Frontera con 9°:** la guía de 9° («De Aristóteles a Galileo») se queda en la
  *descripción*; esta empieza donde aquella termina, con las *causas*. Galileo aparece aquí
  solo como precursor de la inercia y como el que midió la caída; el barco de Galileo y Oresme
  quedan para 9°.
- Hechos verificados que el hilo usa con cuidado: la torre de Pisa es **leyenda** (Viviani);
  la manzana de Newton es una **anécdota** que Newton contó en su vejez (Stukeley, conversación
  del 15 de abril de 1726, memoria de 1752); los *Principia* se publicaron en **1687**, con
  imprimatur de Samuel Pepys (5 de julio de 1686) y a **costa de Halley**, porque la Royal
  Society no tenía fondos tras imprimir la *Historia piscium*.

## DBA y evidencias

Fuente: `dba/naturales/grados/grado10.tex` (literal).

**DBA 1** — «Comprende, que el reposo o el movimiento rectilíneo uniforme, se presentan
cuando las fuerzas aplicadas sobre el sistema se anulan entre ellas, y que en presencia de
fuerzas resultantes no nulas se producen cambios de velocidad.»

| Evidencia | Tema |
|---|---|
| Predice el equilibrio (de reposo o movimiento uniforme en línea recta) de un cuerpo a partir del análisis de las fuerzas que actúan sobre él (primera ley de Newton). | `tema:primeraley` (y `tema:vectores`, fuerza neta) |
| Estima, a partir de las expresiones matemáticas, los cambios de velocidad (aceleración) que experimenta un cuerpo a partir de la relación entre fuerza y masa (segunda ley de Newton). | `tema:segundaley`, `tema:cinematica` |
| Identifica, en diferentes situaciones de interacción entre cuerpos (de forma directa y a distancia), la fuerza de acción y la de reacción e indica sus valores y direcciones (tercera ley de Newton). | `tema:terceraley` (la cuerda del ejemplo del DBA; la manzana y la Tierra) |

El DBA 2 (energía) va en el trimestre III. **Medición no tiene DBA**: es herramienta (decisión
pendiente de la docente); la guía lo dice. Estándares 10°–11°: «Establezco relaciones entre
las diferentes fuerzas que actúan sobre los cuerpos en reposo o en movimiento rectilíneo
uniforme…» y «Modelo matemáticamente el movimiento de objetos cotidianos a partir de las
fuerzas que actúan sobre ellos».

## Frase introductoria

«Si he visto más lejos es porque estoy de pie sobre hombros de gigantes.» — Isaac Newton, carta
a Robert Hooke, 5 feb. 1675/76 (ya verificada en `crear-guia/REFERENCE.md`). Encaja: Newton se
apoya en Galileo.

## Marco teórico (redactado; pasa a la guía)

1. **Galileo: la inercia antes de Newton.** Galileo imaginó un plano sin roce y concluyó que un
   cuerpo en movimiento sin fuerzas seguiría con rapidez constante en línea recta; midió la
   caída en planos inclinados con un reloj de agua (*Discursos*, 1638) [galileo1638, recurso].
   La torre de Pisa: leyenda de Viviani (1654, publicada en 1717) [physicsworld].
2. **Halley y los *Principia*.** Halley animó a Newton a escribirlos, pagó la impresión y
   corrigió las pruebas; se publicaron en Londres en 1687 [halley, newton1687].
3. **Las tres leyes**, en traducción propia del latín (3.ª ed., 1726) [newton1726] — citas.
4. **La manzana**: anécdota contada por el propio Newton en 1726 a William Stukeley, que la
   escribió en 1752 [stukeley]; se presenta como anécdota.
5. **Émilie du Châtelet** (1706–1749): *Institutions de physique* (1740); terminó la
   traducción francesa comentada de los *Principia* poco antes de morir en 1749; se publicó en
   1756 (parcial) y 1759; sigue siendo la traducción francesa de referencia [sep-chatelet,
   chatelet1759].
6. **Medir hoy:** desde el 20 de mayo de 2019 el kilogramo se define fijando el valor de la
   constante de Planck [bipm] (enlace con el tema de medición).

## Temas

| Etiqueta | Tema (propuesta) | Clases |
|---|---|---|
| `tema:medicion` | Medición (incluye un repaso de la notación científica ya dictada, 003–004) | 005–006 |
| `tema:vectores` | Vectores | 007–008 |
| `tema:cinematica` | Repaso de cinemática | 009–010 |
| `tema:primeraley` | Primera ley de Newton | 011–014 |
| `tema:segundaley` | Segunda ley de Newton | 015–018 |
| `tema:terceraley` | Tercera ley de Newton | 019–020 |
| `tema:tresleyes` | Las tres leyes | 021–022 |

Omitidos: «Inicio de año» (001–002), «Herramientas de trabajo» (003–004, dictada; se retoma
dentro de medición) y «Evaluación del periodo» (023–024).

Ejemplos resueltos (comprobados con script, no van al banco): 72 km/h = 20 m/s; área
4,5 × 3,25 cm → 15 cm²; 30 N + 40 N perpendiculares → 50 N a 53,1°; plano de Galileo 0,30 m →
1,2 m → 2,7 m, a = 0,60 m/s²; MUA 0 → 20 m/s en 8 s (2,5 m/s², 80 m); caída de 2,0 s (19,6 m/s,
19,6 m); libro de 1,5 kg (N = 14,7 N); caja de 20 kg, 80 N, μk = 0,25 (a = 1,55 m/s²);
patinadora de 50 kg y 100 N (2 m/s²).

## Ejercicios — tabla de ids (etapa B)

Regla de la docente (2026-09-15): la guía usa **solo** ejercicios que ya están en el banco
(`verificado` o `manual-aprobado`), salvo cuando un tema no tiene **nada** en el banco
(aclaración del 2026-09-15). Aquí eso solo pasa con la tercera ley: van 2 nuevos, en
`recursos/banco/fisica/fuerzas-10.py`, verificados con `verificar --sin-registro` (falta que
una sesión corra `verificar` para registrarlos). Los otros que se habían escrito se borraron.

| id | tema | estado |
|---|---|---|
| mediciones-10-001, -058, -055, -062 | medición | verificado |
| cinematica-2d-10-007, -031, -030, -029; leyes-newton-10-056 | vectores | verificado |
| cinematica-10-044, -059, -064, -042 | cinemática | verificado |
| leyes-newton-10-044, -051, -053, -057 | primera ley | verificado |
| leyes-newton-10-032, -033, -040, -060, -062 | segunda ley | verificado |
| fuerzas-10-001 | tercera ley | verificado | **nuevo**: el ejemplo del DBA (adulto sobre hielo y niño) |
| fuerzas-10-002 | tercera ley | verificado | **nuevo**: acción y reacción a distancia (manzana–Tierra) |
| leyes-newton-10-058, -061, -064 | tres leyes | verificado |
| cinematica-10-002, mediciones-10-071, cinematica-10-008 | Saber 11 | verificado |

Saber 11: `cinematica-10-002` (a), `mediciones-10-071` (b), `cinematica-10-008` (b).

**Evidencias sin ejercicio en el banco (pendientes):**
- DBA 1, evidencia 3 (tercera ley): el banco no tenía ninguno; se cubre con los 2 nuevos.
  `leyes-newton-10-025` (halar la cuerda) espera aprobación y está comentado en el `.tex`.
- Primera ley: no hay un «encuentra el error» verificado (el DBA pide *predecir* y justificar).
- Saber 11 de leyes de Newton: el banco solo tiene selección múltiple de cinemática, medición,
  energía y gravitación.

## Cierre del hilo

De un plano inclinado a un libro que cambió la física, traducido por una mujer que la entendió
mejor que casi todos sus contemporáneos. Hacia el trimestre II: la misma ley de fuerzas explica
proyectiles, órbitas y la gravitación universal (el libro III de los *Principia*).

## Evaluación (matriz)

- Saber: enuncia las tres leyes y reconoce cuándo un cuerpo está en equilibrio.
- Hacer: dibuja diagramas de cuerpo libre, suma fuerzas por componentes y calcula aceleraciones con unidades del SI y cifras adecuadas.
- Ser: distingue hechos documentados de anécdotas y leyendas; revisa si sus resultados son razonables.
- Convivir: trabaja en equipo en los laboratorios y comparte datos honestamente.

## Referencias (verificadas 2026-09-14/15)

| Clave | Referencia | Veredicto | URL |
|---|---|---|---|
| bipm | BIPM. Redefinición del kilogramo (vigente desde el 20 may. 2019). | confirmada | https://www.bipm.org/en/-/2021-kg-consensus |
| chatelet1759 | Du Châtelet, É. (1756–1759). *Principes mathématiques de la philosophie naturelle*. París: Desaint & Saillant; Lambert. | confirmada (ya usada en la plantilla) | https://www.e-rara.ch/doi/10.3931/e-rara-14635 |
| galileo1638 | Galilei, G. (1638). *Discorsi…* Leiden: Elzevir. | confirmada | https://portalegalileo.museogalileo.it/igjr.asp?c=36308 |
| halley | MacTutor. *Edmond Halley*. | confirmada: animó a Newton, pagó la edición, corrigió pruebas | https://mathshistory.st-andrews.ac.uk/Biographies/Halley/ |
| mendba | MEN (2016). DBA Ciencias Naturales. | tomada de 11° | https://www.colombiaaprende.edu.co/sites/default/files/files_public/2022-06/DBA_C.Naturales-min.pdf |
| newton1676 | Newton, carta a Hooke, 5 feb. 1675/76. | ya verificada | https://digitallibrary.hsp.org/index.php/detail/objects/9792 |
| newton1687 | Newton, I. (1687). *Philosophiæ naturalis principia mathematica*. Londres: Streater, para la Royal Society. | confirmada (Pepys, 5 jul. 1686; Historia piscium) | https://archive.org/details/McGillLibrary-osl_newton-philosophiae-naturalis-principia-mathematica_N563p1687-20098 · https://royalsociety.org/blog/2014/07/principia/ |
| newton1726 | Newton, *Principia*, 3.ª ed. (1726), Axiomata sive leges motus. | confirmada (texto latino de las tres leyes) | https://www.thelatinlibrary.com/newton.leges.html |
| physicsworld | Physics World. *The legend of the leaning tower*. | confirmada | https://physicsworld.com/a/the-legend-of-the-leaning-tower/ |
| sep-chatelet | Stanford Encyclopedia of Philosophy. *Émilie du Châtelet*. | confirmada: 1706–1749, Institutions 1740, traducción publicada 1759, sigue siendo la de referencia | https://plato.stanford.edu/entries/emilie-du-chatelet/ |
| stukeley | Stukeley, W. (1752). *Memoirs of Sir Isaac Newton's life*. Royal Society, MS/142. | confirmada: conversación del 15 abr. 1726 | https://newtonproject.ox.ac.uk/view/texts/normalized/OTHE00001 |
| recurso10 | Guía de apoyo Física 10°, caps. 1–4 | archivo local | `recursos/fisica/Guías pedagógicas Física/markdown/10 - Guia_de_apoyo_cinematica_y_dinamica_grado_10_fisica.md` |

## Errores encontrados en el recurso (guía de apoyo 10°)

- Cap. 2: los de la guía de 9° (eje «–x» por «+x», Imagen 3 «a la derecha −x», «Distancia
  tiempo ÷ transcurrido», «_t = 3.00 s», «Km»).
- Cap. 4: «Isaac Newton construyó su célebre teoría… basándose en los cimientos asentados por
  Galileo El análisis…» (falta el punto); la frase «Si un objeto está en reposo, para empezar a
  moverlo se requiere una fuerza» es correcta, pero conviene precisar *fuerza neta*.
- Cap. 2, introducción: Newton «1642–1727» (juliano; 1643 gregoriano).
