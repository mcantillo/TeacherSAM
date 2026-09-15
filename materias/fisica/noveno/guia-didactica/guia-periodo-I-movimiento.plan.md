# Plan de la guía — Física 9° · Trimestre I (etapas A y B)

> **BORRADOR — generación rápida (2026-09-14/15)**, etapas A, B y C en una sola pasada por
> pedido de la docente, sin esperar las revisiones. La fuente es la **propuesta** de
> `curriculo/plan-anual.md` (clases 002–009), todavía **no aprobada** ni escrita en
> `programacion.csv`. Todo lo de aquí queda sujeto a la revisión de la docente.

## Datos

| | |
|---|---|
| Asignatura | Física |
| Grado | 9° (una sesión semanal de 50 min) |
| Trimestre | I (semanas 02–12; clases 001–009 de la propuesta) |
| Archivo | `guia-periodo-I-movimiento.tex` |
| Título | Describir el movimiento: posición, velocidad y marcos de referencia |
| Hilo | **De Aristóteles a Galileo** (opción A de `plan-anual.md`) |
| Registro | Juvenil (7°–11°) |

### Por qué este hilo y cómo no se cruza con el de 10°

- Continúa las exposiciones de científicos que ya se asignaron (clase 001) y cierra con la
  pregunta que ellas dejan: ¿cómo se pasó de *explicar* el movimiento con palabras
  (Aristóteles) a *describirlo* con números y gráficas (Oresme, Galileo)? Eso es exactamente
  el DBA 1 de 9°: describir con gráficas y predecir con ecuaciones.
- El barco de Galileo (1632) es la mejor puerta histórica al cambio de marco (evidencia 3), y
  el ejemplo del propio DBA (la pelota en el bus) es su versión moderna.
- **Frontera con 10°:** esta guía termina en Galileo y en la *descripción* del movimiento
  (cinemática). La de 10° («De la inercia a los *Principia*») empieza donde esta termina: con
  las *causas* del movimiento (fuerzas, Newton, du Châtelet). Galileo aparece en las dos, pero
  en 9° como el que mide y describe, y en 10° como el precursor de la inercia.
- Opciones descartadas: «El barco de Galileo» (B) solo sostiene un tema; «Cronómetros y
  récords» (C) exige verificar marcas deportivas y no es historia de la física.

## DBA y evidencias

Fuente: `dba/naturales/grados/grado09.tex` (literal).

**DBA 1** — «Comprende que el movimiento de un cuerpo, en un marco de referencia inercial
dado, se puede describir con gráficos y predecir por medio de expresiones matemáticas.»

| Evidencia (literal) | En este trimestre |
|---|---|
| Describe el movimiento de un cuerpo (rectilíneo uniforme y uniformemente acelerado, en dos dimensiones – circular uniforme y parabólico) en gráficos que relacionan el desplazamiento, la velocidad y la aceleración en función del tiempo. | Solo MRU: gráficas x–t y v–t (`tema:mru`); MUA, parabólico y circular en el trimestre II |
| Predice el movimiento de un cuerpo a partir de las expresiones matemáticas con las que se relaciona, según el caso, la distancia recorrida, la velocidad y la aceleración en función del tiempo. | `tema:describir` (velocidad media) y `tema:mru` (x = x₀ + v t, encuentros) |
| Identifica las modificaciones necesarias en la descripción del movimiento de un cuerpo, representada en gráficos, cuando se cambia de marco de referencia. | `tema:marcos` (en una dimensión; la pelota del bus, cualitativa) |

Estándares 8°–9° (`dba/naturales/estandares-fisica.md`): ninguno trata el movimiento; se cita
solo el DBA. La columna «me aproximo al conocimiento como científico natural» (medir, registrar
datos, graficar) sostiene los talleres.

## Frase introductoria

«Me propongo exponer una ciencia muy nueva sobre un tema muy antiguo. Quizá no haya en la
naturaleza nada más antiguo que el movimiento […]» — Galileo Galilei, *Discursos y
demostraciones matemáticas sobre dos nuevas ciencias* (1638), comienzo de la Jornada tercera;
trad. propia de la versión inglesa de Crew y de Salvio (1914), pp. 153–154.

## Marco teórico (redactado; pasa tal cual a la guía)

1. **Aristóteles: todo movimiento necesita un motor.** En su *Física* (siglo IV a. C.)
   distinguió el movimiento natural (lo pesado cae hacia el centro, lo liviano sube) del
   forzado o «violento» (una piedra lanzada), y sostuvo que todo movimiento necesita algo que
   lo mueva [sep-aristoteles]. Explicaba el *porqué*, no el *cuánto*.
2. **Oresme: dibujar el movimiento.** Nicole Oresme (c. 1323–1382), en su *Tratado de las
   configuraciones de las cualidades y los movimientos* (década de 1350), representó una
   magnitud que cambia —como la velocidad— con figuras en las que una línea representa el
   tiempo, y con ellas demostró la regla de la velocidad media de los calculadores de Oxford
   [oresme]. Es un antepasado de nuestras gráficas.
3. **Galileo: medir.** En los *Discursos* (Leiden, 1638) definió el movimiento uniforme —
   distancias iguales en tiempos iguales, *cualesquiera* que sean esos tiempos— y midió con un
   plano inclinado y un reloj de agua (pesaba el agua que salía durante cada bajada) que las
   distancias en tiempos iguales crecen como los números impares 1, 3, 5, 7… [galileo1638,
   crew1914].
4. **La torre de Pisa: una leyenda.** La historia de las bolas lanzadas desde la torre viene
   de la biografía de Vincenzo Viviani, escrita en 1654 y publicada en 1717; Galileo no dejó
   ningún registro de ese experimento y la mayoría de los historiadores dudan de él
   [physicsworld]. En la guía se cuenta como leyenda.
5. **El barco de Galileo (1632).** En el *Diálogo sobre los dos máximos sistemas* (Jornada
   segunda) Galileo propone encerrarse bajo cubierta con moscas, mariposas, peces y un
   recipiente que gotea: si el barco se mueve con velocidad constante, nada permite saber si
   se mueve o está quieto [galileo1632]. Cita textual (trad. propia del italiano).
6. **Katherine Johnson (científica del trimestre).** Matemática de la NACA/NASA en Langley
   desde 1953 (1918–2020): hizo el análisis de trayectoria del vuelo de Alan Shepard (1961) y
   verificó a mano los cálculos de la órbita de John Glenn (1962) antes del lanzamiento;
   Medalla Presidencial de la Libertad en 2015 [nasa-johnson]. Enlace con el trimestre:
   describir una trayectoria exige elegir un marco de referencia (esa conexión es nuestra, no
   una afirmación de la fuente).

## Temas

| Etiqueta | Tema (valor `tema` de la propuesta) | Clases |
|---|---|---|
| `tema:cientificos` | Científicos que cambiaron la física | 002–003 |
| `tema:describir` | Describir el movimiento | 004–005 |
| `tema:mru` | Movimiento rectilíneo uniforme | 006–007 |
| `tema:marcos` | Marcos de referencia | 008 (con el repaso) |

Omitidos: «Inicio de año» (001, dictada) y «Evaluación del periodo» (009).

### `tema:cientificos` — Científicos que cambiaron la física
- Hilo: de las exposiciones al método de Galileo. Explicación: qué es describir y qué es
  explicar; el movimiento uniforme de Galileo; el patrón de los impares.
- Aplicación: el trueno y el relámpago (medir distancias con el tiempo).
- Ejercicios: `cinematica-10-033` (reutilizado, relámpago y trueno). **Pendiente:** el banco
  no tiene ejercicios de historia del movimiento (el tema queda con uno solo).

### `tema:describir` — Describir el movimiento
- Explicación: marco de referencia, posición, trayectoria, distancia y desplazamiento; rapidez
  media y velocidad media; km/h ↔ m/s. Ejemplos resueltos (del recurso, comprobados): la
  caminata de 70 m al este y 30 m al oeste en 70 s (1,4 m/s y 0,57 m/s); el corredor de 50,0 m a
  30,5 m en 3,00 s (−6,50 m/s); 36 km/h = 10 m/s.
- Aplicación: el odómetro y el GPS del celular (distancia frente a desplazamiento).
- Ejercicios (todos reutilizados): `cinematica-10-001`, `-036`, `-037`, `-030`, `-022`
  (argumentación).

### `tema:mru` — Movimiento rectilíneo uniforme
- Explicación: x = x₀ + v t; la pendiente de x–t es la velocidad; la gráfica v–t es horizontal
  y su área es el desplazamiento. Ejemplos: x = 20 + 5t (tabla y gráfica); un perro que regresa,
  x = 60 − 10t; área 5 m/s × 6 s = 30 m.
- Aplicación: las distancias de seguridad al conducir (lo que se recorre distraído).
- Ejercicios: `cinematica-10-029`, `-043`, `-040` (reutilizados). **Pendiente (evidencia 1):**
  ningún ejercicio verificado pide leer una gráfica x–t y escribir x = x₀ + v t
  (`cinematica-10-038`/`-039` citan una imagen que no está en la guía).

### `tema:marcos` — Marcos de referencia
- Explicación: el mismo movimiento visto desde dos observadores; velocidad relativa en una
  dimensión (v de A respecto a B = v_A − v_B); cómo cambian la ecuación y la gráfica x–t al
  cambiar de marco; la pelota del bus (ejemplo del DBA), cualitativa.
- Ejemplo: bus a 12 m/s y pasajero a 1,5 m/s (13,5 y 10,5 m/s); gráfica x–t del pasajero en
  los dos marcos.
- Aplicación: el barco de Galileo y un avión en vuelo de crucero.
- Ejercicios: `cinematica-10-042` (reutilizado). **Pendiente (evidencia 3):** ningún ejercicio
  verificado pide cambiar una gráfica o ecuación de marco de referencia.
  La pelota lanzada en el tren (`cinematica-2d-10-021` a `-025`) es abierta y está
  `manual-pendiente`: queda comentada en el `.tex` hasta que la docente la apruebe.

## Prepárate para Saber 11

`cinematica-10-002` (a), `cinematica-10-008` (b), `mediciones-10-071` (b). Respuestas solo en el
informe. **Pendiente:** el banco no tiene preguntas tipo Saber de cinemática con contexto
colombiano; `cinematica-10-008` es de aceleración (anticipa el trimestre II).

## Ejercicios — tabla de ids (etapa B)

Regla de la docente (2026-09-15): la guía usa **solo** ejercicios que ya están en el banco
(`verificado` o `manual-aprobado`); no se escribió ninguno nuevo. Los que se habían escrito
(`cinematica-9.py`) se borraron.

| id | tema | estado |
|---|---|---|
| cinematica-10-033 | científicos | verificado |
| cinematica-10-001, -036, -037, -030, -022 | describir | verificado |
| cinematica-10-029, -043, -040 | mru | verificado |
| cinematica-10-042 | marcos | verificado |
| cinematica-10-002, -008; mediciones-10-071 | Saber 11 | verificado |

Todos están marcados `grados=[10]`: usarlos en 9° es decisión de la docente (ver
`plan-anual.md`). Comentados en el `.tex` por estar `manual-pendiente`: `cinematica-2d-10-021`.

**Evidencias sin ejercicio en el banco (pendientes):**
- Evidencia 1: leer/construir una gráfica x–t o v–t de un MRU (hay ejemplos resueltos, no ejercicios).
- Evidencia 3: cambiar de marco la descripción representada en gráficos (solo hay velocidad relativa).
- Tema «Científicos»: solo un ejercicio.
- Saber 11 con contexto colombiano.

Los ejemplos resueltos del marco se comprobaron con un script aparte (no están en el banco).

## Cierre del hilo

De Aristóteles, que explicaba, a Galileo, que medía: el movimiento se describe con números,
gráficas y un marco de referencia. Pregunta abierta hacia el trimestre II: ¿y si la velocidad
cambia? Galileo ya lo había medido en su plano inclinado: la aceleración, la caída libre y el
movimiento en el plano (la pelota del bus, de nuevo).

## Evaluación (matriz)

- Saber: distingue distancia de desplazamiento y rapidez de velocidad en un marco dado.
- Hacer: construye e interpreta gráficas x–t y v–t de un MRU y predice posiciones con x = x₀ + v t.
- Ser: distingue lo documentado de las leyendas (la torre de Pisa) y revisa sus unidades.
- Convivir: expone y escucha a sus compañeros con respeto en las presentaciones de científicos.

## Referencias (verificadas 2026-09-14/15)

| Clave | Referencia | Veredicto | Corrección | URL |
|---|---|---|---|---|
| crew1914 | Galilei, G. (1914). *Dialogues concerning two new sciences* (H. Crew y A. de Salvio, trads.). Macmillan. | confirmada: frase de apertura de la Jornada tercera y definición de movimiento uniforme, pp. 153–154 | — | https://galileoandeinstein.phys.virginia.edu/tns_draft/tns_153to160.html · https://archive.org/details/dialoguesconcern00galiuoft |
| galileo1632 | Galilei, G. (1632). *Dialogo sopra i due massimi sistemi del mondo*. Florencia: Landini. | confirmada; pasaje del «gran navilio», Jornada segunda | — | https://portalegalileo.museogalileo.it/igjr.asp?c=36307 · https://www.robertoocca.net/fis/fren/fr_principi/galileo_gran_navilio.htm |
| galileo1638 | Galilei, G. (1638). *Discorsi e dimostrazioni matematiche intorno a due nuove scienze*. Leiden: Elzevir. | confirmada; plano inclinado, reloj de agua, ley de los impares | — | https://portalegalileo.museogalileo.it/igjr.asp?c=36308 · https://galileo.library.rice.edu/lib/student_work/experiment95/inclined_plane.html |
| mendba | MEN (2016). *Derechos Básicos de Aprendizaje: Ciencias Naturales*. | tomada de la guía de 11° | — | https://www.colombiaaprende.edu.co/sites/default/files/files_public/2022-06/DBA_C.Naturales-min.pdf |
| nasa-johnson | NASA. *Katherine Johnson Biography*. | confirmada: 1918–2020, Langley desde 1953, Shepard 1961, Glenn 1962, Medalla 2015 | — | https://www.nasa.gov/centers-and-facilities/langley/katherine-johnson-biography/ |
| oresme | MacTutor. *Nicole Oresme*. | confirmada: 1323–1382; gráficas de una magnitud variable; prueba de la regla de Merton. La década de 1350 del tratado, en Encyclopedia.com/Britannica (Britannica dio 403) | «hacia 1350» → «década de 1350» | https://mathshistory.st-andrews.ac.uk/Biographies/Oresme/ · https://www.encyclopedia.com/people/philosophy-and-religion/other-religious-beliefs-biographies/nicole-oresme |
| physicsworld | Physics World. *The legend of the leaning tower*. | confirmada: única fuente, Viviani; historiadores dudan | nueva | https://physicsworld.com/a/the-legend-of-the-leaning-tower/ |
| sep-aristoteles | Stanford Encyclopedia of Philosophy. *Aristotle's Natural Philosophy*, §5. | confirmada: movimiento natural / forzado; todo movimiento necesita un motor | — | https://plato.stanford.edu/entries/aristotle-natphil/ |
| recurso10 | Guía de apoyo Física 10° «Cinemática y dinámica», cap. 2 | archivo local | — | `recursos/fisica/Guías pedagógicas Física/markdown/10 - Guia_de_apoyo_cinematica_y_dinamica_grado_10_fisica.md` |

Viviani 1654/1717: confirmado también en https://upittpress.org/wp-content/uploads/2018/07/9780822944072exr.pdf.

## Errores encontrados en el recurso (guía de apoyo 10°, cap. 2)

- «la velocidad promedio es positiva si el objeto se mueve hacia la derecha a lo largo del eje
  –x (menos x)»: debe decir eje **+x**.
- Descripción de la Imagen 3: «a la derecha +x y a la derecha −x»: el −x va a la **izquierda**.
- «Distancia tiempo ÷ transcurrido = 100 m ÷ 70 s» (palabras invertidas) y «Desplazamiento ÷
  transcurrido» (falta «tiempo»).
- Ejemplo del corredor: «_t = 3.00 s» (se perdió la Δ y usa punto decimal).
- «45 Km», «18 Km/h»: el símbolo del kilómetro es **km**.
- Introducción: «Isaac Newton (1642-1727)»: 1642 es la fecha del calendario juliano; en el
  gregoriano nació el 4 de enero de 1643 (conviene aclararlo si se usa).
