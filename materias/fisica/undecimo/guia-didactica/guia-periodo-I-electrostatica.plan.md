# Plan de la guía — Física 11° · Trimestre I (etapa A)

> Etapa A del skill `crear-guia`: estructura, teoría, hilo y fuentes, **sin enunciados de
> ejercicios**. Espera la **Revisión 1** de la docente. Rehace la guía que se escribió el
> 2026-09-14 sin este proceso (`guia-periodo-I-electrostatica.tex`, que se reemplaza en la
> etapa C); se conserva lo que estaba bien y se corrige lo que encontró la revisión de ese día.

## Datos

| | |
|---|---|
| Asignatura | Física |
| Grado | 11° |
| Trimestre | I (semanas 01–12; sesiones 001–021 de `programacion.csv`) |
| Archivo | `guia-periodo-I-electrostatica.tex` |
| Título | Cargas, fuerzas y campos: la electricidad que no se ve |
| Hilo | **De Tales al pararrayos** (aprobado el 2026-09-14): del ámbar frotado de la tradición griega a Gilbert, Coulomb y Franklin |
| Registro | Juvenil (7°–11°): definiciones formales, notación vectorial, citas con fuente, justificar |

## Decisiones ya tomadas (2026-09-14)

- Plan anual, filas 001–021 e hilo del trimestre I: aprobados por la docente.
- Semana 12: la 020 es el repaso general (con el pararrayos y la jaula de Faraday) y la 021 la
  evaluación del periodo; el quiz de campo eléctrico no se reubica.

## Para decidir en la Revisión 1

1. **La cometa de Franklin.** Lo único que se sabe del experimento viene de la carta de Franklin
   publicada el 19 de octubre de 1752 y del relato de Priestley de 1767; algunos historiadores
   dudan de que Franklin lo haya hecho él mismo, y la fecha (junio de 1752) no es segura.
   Propongo contarlo así —«Franklin publicó cómo hacerlo y afirmó que funcionaba»— y apoyar el
   paso del hilo en lo que sí está documentado: su propuesta del pararrayos en el almanaque de
   1753. ¿De acuerdo?
2. **Tales.** Ninguna obra de Tales se conserva, y la atribución del ámbar viene de Diógenes
   Laercio (siglo III d. C.), que cita a Aristóteles y a Hipias; Aristóteles solo menciona el imán.
   Propongo presentarlo como tradición («la tradición griega atribuye a Tales…»), no como hecho.
3. **Contexto colombiano:** propongo que el pararrayos se cuente desde Colombia —uno de los
   países con más actividad de rayos por su ubicación tropical y su relieve (Younes, 2020)— y
   que las preguntas tipo Saber 11 usen contextos de aquí (una finca del Valle en tormenta, un
   carrotanque que descarga en una estación de gasolina de Cali, un globo en una fiesta).
   ¿Te parece bien?

## DBA y evidencias

Fuente: `dba/naturales/grados/grado11.tex` (texto literal). Este trimestre trabaja **la primera
parte** del DBA 2 (cargas en reposo); la segunda (cargas en movimiento, electroimán) va en el
trimestre II.

**DBA 2** — «Comprende que la interacción de las cargas en reposo genera fuerzas eléctricas y que
cuando las cargas están en movimiento genera fuerzas magnéticas.»

| Evidencia | Tema que la atiende |
|---|---|
| Identifica el tipo de carga eléctrica (positiva o negativa) que adquiere un material cuando se somete a procedimientos de fricción o contacto. | Carga (sesiones 004–008, con el laboratorio 007): **nuevo** — serie de materiales frotados (vidrio y seda, plástico y lana) y predicción del signo; la guía anterior no tenía ningún ejercicio sobre esto |
| Reconoce que las fuerzas eléctricas y magnéticas pueden ser de atracción y repulsión, mientras que las gravitacionales solo generan efectos de atracción. | Coulomb (014: eléctrica frente a gravitacional); la parte magnética, en el trimestre II |
| Construye y explica el funcionamiento de un electroimán. | Trimestre II (no se atiende aquí) |

Estándares MEN (2004), grupo 10°–11°, entorno físico (`dba/naturales/estandares-fisica.md`): la
meta «Explico las fuerzas entre objetos como interacciones debidas a la carga eléctrica y a la
masa», y los que relacionan fuerzas electrostáticas con fuerzas macroscópicas y el campo
electrostático con el gravitacional (el texto literal se toma del archivo en la etapa C). La
columna «me aproximo al conocimiento como científico natural» sostiene el laboratorio de la
sesión 007.

**Tema sin DBA:** la notación científica (sesión 002) no corresponde a ningún DBA de física; es
una herramienta de trabajo para todo el trimestre (y el puente con Cálculo 11°). Se dice así en
la guía.

El ejemplo del DBA 2 (circuito con brújula, experimento de Oersted) es del trimestre II.

## Frase introductoria

«[…] y así queda completamente demostrada la identidad de la materia eléctrica con la del rayo.»
— Benjamin Franklin, *Pennsylvania Gazette*, 19 de octubre de 1752 (trad. propia). Original:
«and thereby the Sameness of the Electric Matter with that of Lightning compleatly demonstrated».

Por qué esta: es la frase con que Franklin cierra la descripción de la cometa, el paso final del
hilo; y su «completamente demostrada» da pie a la pregunta de la decisión 1: ¿qué hace falta para
demostrar algo en física?

## Marco teórico (redactado)

**Un trozo de ámbar y una palabra griega.** La observación más antigua de la electricidad es muy
sencilla: el ámbar frotado atrae pajitas, hilos y plumas. La tradición griega atribuye esa
observación a Tales de Mileto, en el siglo VI a. C.: Diógenes Laercio cuenta, citando a
Aristóteles y a Hipias, que Tales les atribuía alma a los objetos inanimados apoyándose en el imán
y en el ámbar [laercio]. No se conserva nada escrito por Tales, así que es una tradición, no un
dato seguro. El ámbar se llamaba en griego *élektron*, y de esa palabra viene todo nuestro
vocabulario: electricidad, electrón, electrónica.

**Gilbert separa dos fenómenos.** En 1600 el médico inglés William Gilbert publicó *De magnete*
[gilbert1600], el primer estudio sistemático del magnetismo. Allí mostró que no solo el ámbar:
unas treinta sustancias —vidrio, azufre, lacre, varias piedras preciosas— atraen objetos livianos
al ser frotadas; las llamó *electrica* (palabra que inventó a partir de *élektron*), y las
detectó con un instrumento propio, el *versorium*, una aguja que gira libre sobre un pivote. Y
sobre todo mostró que la atracción del ámbar y la del imán son fenómenos **distintos**. Hoy
sabemos que están profundamente relacionados —eso dice la segunda parte de nuestro DBA—, pero
para entenderlos primero había que separarlos.

**Medir lo invisible.** En 1785, el ingeniero militar francés Charles-Augustin de Coulomb presentó
a la Academia de Ciencias de París su primera memoria sobre la electricidad [coulomb1785]: dentro
de un cilindro de vidrio colgó una aguja de un hilo de plata tan fino que bastaba una fuerza
diminuta para torcerlo. Midiendo cuánto giraba el hilo cuando dos esferitas cargadas se
repelían, estableció que la fuerza entre ellas es inversamente proporcional al cuadrado de la
distancia —la misma forma matemática de la gravedad de Newton, para una fuerza muy distinta—.

**Laura Bassi.** En esos mismos años, la física experimental europea empezaba, muy despacio, a
abrirse a las mujeres. Laura Bassi (Bolonia, 1711) se graduó en filosofía en la Universidad de
Bolonia en 1732, a los veinte años, y en 1776 obtuvo la cátedra de física experimental del
Istituto delle Scienze de su ciudad [bassi]: una de las primeras mujeres de Europa en enseñar
física en una institución universitaria, en la misma época en que Coulomb hacía sus mediciones.

**Del rayo al pararrayos.** En Filadelfia, Benjamin Franklin sostenía que el rayo era la misma
electricidad que se produce frotando vidrio, a una escala enorme. El 19 de octubre de 1752 publicó
cómo comprobarlo con una cometa y una llave, y afirmó que el experimento funcionaba [franklin1752];
lo que se sabe de cómo y cuándo lo hizo viene de esa carta y de un relato de Joseph Priestley de
1767, y algunos historiadores dudan de que lo haya realizado él mismo [debatecometa]. Lo que sí
está documentado es lo que siguió: en su almanaque para 1753 explicó cómo proteger una casa con
una varilla de hierro terminada en punta y enterrada en el suelo húmedo: el pararrayos
[franklin1753].

**Del empujón a distancia al campo.** Queda una pregunta: si nada toca a una carga, ¿cómo le
llega la fuerza? En el siglo XIX la física respondió con una idea nueva: cada carga modifica el
espacio que la rodea —crea un **campo**— y la otra carga responde al campo que hay donde ella está
[serway]. Esa idea es el último tema del trimestre y la puerta a la corriente y al magnetismo del
trimestre II.

**En Colombia.** Por su ubicación tropical y su relieve, Colombia es un caso especial en el
estudio del rayo: tiene una de las actividades eléctricas atmosféricas más altas del mundo, y la
Universidad Nacional la mide desde hace más de veinte años [younes2020]. El invento de Franklin
aquí no es una curiosidad histórica.

## Temas

Se conservan las cuatro etiquetas de la guía anterior (ninguna clase las cita todavía, pero así se
evita cambiar lo que no hace falta). Mapa con `programacion.csv`:

| Etiqueta | Tema en la guía | Filas |
|---|---|---|
| `tema:notacion` | Notación científica y orden de magnitud | 002 («Herramientas de trabajo»), sin DBA |
| `tema:carga` | La carga eléctrica | 004–008 |
| `tema:coulomb` | La ley de Coulomb | 009–014 |
| `tema:campo` | El campo eléctrico | 015–019; la 003 («Introducción a la electrostática», ya dictada) fue un primer vistazo a Coulomb y al campo, y la 020 cierra con el pararrayos y la jaula de Faraday |

### Tema 1 — Notación científica y orden de magnitud · `tema:notacion`

Sesión 002 (ya dictada). Sin DBA.

- **Hilo:** la carga que se lleva un trozo de ámbar frotado es del orden de nanocoulombs; para
  hablar de ella hay que saber escribir números muy pequeños y muy grandes.
- **Explicación:** notación científica (a × 10ⁿ con 1 ≤ |a| < 10); orden de magnitud; prefijos
  (micro, nano, kilo); las constantes del trimestre (e = 1,602 × 10⁻¹⁹ C, mₑ, k = 8,99 × 10⁹
  N·m²/C²) —**sin** la comparación de «28 órdenes de magnitud» entre la carga del electrón y k, que
  no tiene sentido porque son magnitudes con unidades distintas—.
- **Aplicación:** estimar antes de calcular: un resultado absurdo delata una potencia de diez mal
  puesta.
- **Recursos:** bank `notacion-cientifica-8` (nivel 8°, solo como calentamiento); guía de apoyo
  de 11°, conversiones de carga (1 C ≈ 6,25 × 10¹⁸ e).
- **Ejercicios planeados** (3):
  1. Escribir en notación científica medidas de carga y distancia con prefijos (cálculo, dif. 1).
  2. ¿Cuántos electrones hay en 1 nC? (cálculo, dif. 1).
  3. Encontrar el error en una suma en notación científica (argumentación, dif. 2).

### Tema 2 — La carga eléctrica · `tema:carga`

Sesiones 004–008 (semanas 03–05). DBA 2 (evidencia 1).

- **Hilo:** Gilbert frota decenas de materiales y anota cuáles atraen; en el laboratorio de la
  sesión 007 hacemos lo mismo, pero preguntando además *qué signo* adquiere cada uno.
- **Explicación:**
  - Carga: dos clases, ley de signos, unidad (coulomb); estructura del átomo.
  - Conservación y cuantización (q = n e).
  - Electrización por frotamiento (el material que gana electrones queda negativo: el plástico
    frotado con lana; el vidrio frotado con seda queda positivo), por contacto (los dos quedan con
    el mismo signo) y por inducción (el electroscopio; con conexión a tierra queda el signo
    contrario).
  - **Nuevo:** una serie de materiales ordenados según su tendencia a ceder o ganar electrones al
    frotarse (serie triboeléctrica), para predecir el signo; su fuente se verifica en la etapa B.
  - Conductores, aislantes y semiconductores.
  - Ejemplo resuelto: electrones en exceso de un globo con −2 nC.
- **Aplicación:** por qué un carrotanque se conecta a tierra antes de descargar combustible (título
  corregido: la guía anterior hablaba de una «cadena» y describía la conexión a tierra) y la
  pulsera antiestática de un técnico.
- **Recursos:** guía de apoyo de 11°, capítulo 1 («La carga eléctrica», «La electrización»,
  «Conductores y aislantes», «Carga por contacto y carga por inducción»).
- **Ejercicios planeados** (4–5):
  1. **Nuevo:** predecir el signo que adquiere cada material en tres pares frotados y el signo tras
     un contacto (conceptual, dif. 1–2) — evidencia 1 del DBA.
  2. Conservación de la carga: globo y pelo (argumentación, dif. 1).
  3. Inducción en una esfera metálica aislada y por qué es atraída con carga total cero
     (argumentación, dif. 2) — candidatos `electrostatica-11-051`, `-052`.
  4. Carga de n electrones **con su signo** (−801 nC para 5 × 10¹² electrones) y cuantización
     (cálculo, dif. 1) — candidatos `-006`, `-053`.
  5. Conductor o aislante (conceptual, dif. 1) — candidatos `-020` a `-029` (manuales, pendientes de
     aprobación).

### Tema 3 — La ley de Coulomb · `tema:coulomb`

Sesiones 009–014 (semanas 05–08). DBA 2 (evidencia 2).

- **Hilo:** Coulomb cuelga su aguja del hilo de plata y convierte una curiosidad en una ley con
  números.
- **Explicación:**
  - F = k |q₁q₂| / r², dirección y sentido; la distancia siempre en metros.
  - Inverso del cuadrado: al duplicar la distancia, la fuerza baja a la cuarta parte; gráfica de F
    contra r (puente con Cálculo 11°).
  - Superposición en una línea y en el plano.
  - Ejemplo resuelto: dos cargas de 2 μC y −3 μC a 5 cm (≈ 21,6 N, atracción).
  - Eléctrica contra gravitacional: el cociente entre dos electrones (≈ 4 × 10⁴²) y por qué no
    notamos la fuerza eléctrica (la materia es neutra; la gravedad solo atrae) — evidencia 2.
- **Aplicación:** la pintura electrostática de los carros y el tóner de las impresoras láser (se
  verifica la descripción en la etapa B).
- **Recursos:** guía de apoyo de 11°, «La ley de Coulomb» y sus ejemplos resueltos (se revisan
  antes de reutilizarlos).
- **Ejercicios planeados** (4–5):
  1. Fuerza entre dos cargas y su sentido (cálculo, dif. 1) — candidatos `-049`, `-055`, `-057`.
  2. Cambio de la fuerza al cambiar la distancia, primero razonando (cálculo, dif. 1) — candidatos
     `-046`, `-047`, `-054`.
  3. Superposición en una línea (cálculo, dif. 2) — candidato `-058`.
  4. Encontrar el error: la distancia en centímetros al cuadrado (argumentación, dif. 2).
  5. Eléctrica frente a gravitacional en contexto (contexto, dif. 3) — candidato `-048`.

### Tema 4 — El campo eléctrico · `tema:campo`

Sesiones 015–019 (semanas 08–11), más la 003 y la 020. DBA 2.

- **Hilo:** Franklin propone que el rayo y la chispa son lo mismo; queda la pregunta de cómo llega
  la fuerza sin contacto, y la respuesta es el campo. El pararrayos es la aplicación que cierra el
  hilo.
- **Explicación:**
  - E = F/q₀ (N/C); campo de una carga puntual, E = k|q|/r², y su sentido según el signo.
  - Líneas de campo de una carga, de un dipolo y de dos cargas iguales; no se cruzan.
  - Fuerza sobre una carga negativa: opuesta al campo.
  - Campo uniforme entre placas paralelas; campo nulo dentro de un conductor en equilibrio.
  - Ejemplo resuelto: campo a 30 cm de 5 μC (≈ 5,0 × 10⁵ N/C) y fuerza sobre 2 nC.
- **Aplicación:** el pararrayos (el campo se concentra en las puntas) y la jaula de Faraday (un carro
  en una tormenta), contados desde Colombia.
- **Recursos:** guía de apoyo de 11°, «Campo eléctrico», «Las líneas de fuerza», «Campo eléctrico
  uniforme», «Algunas aplicaciones electrostáticas».
- **Ejercicios planeados** (4):
  1. Campo de una carga negativa: magnitud y dirección (cálculo, dif. 1) — candidato `-059`.
  2. Fuerza sobre una carga negativa en un campo dado (cálculo, dif. 1) — candidato `-044`.
  3. Líneas de campo de dos cargas iguales y punto de campo nulo (representación, dif. 2) —
     candidato `-045` (manual).
  4. Por qué las líneas de campo no se cruzan (argumentación, dif. 2).

## Prepárate para Saber 11

Cuatro preguntas de selección múltiple con única respuesta, contextos colombianos y la letra
correcta variada; las respuestas van a la docente, no a la guía.

1. Carga de un cuerpo con n electrones en exceso, con signo y prefijo (contexto: el globo de una
   fiesta). Corrige el sentido físico de la anterior.
2. Cómo cambia la fuerza entre dos esferas con cargas iguales (que **se repelen**) si la distancia
   se reduce a la mitad — corrige el error de la versión anterior, que decía «se atraen».
3. Qué ocurre en una esfera metálica neutra cuando se le acerca una barra negativa sin tocarla
   (inducción).
4. Sentido de la fuerza sobre una carga negativa en un campo que apunta a la derecha (contexto: el
   campo bajo una nube de tormenta en una finca del Valle).

Fuente para adaptar: «Prepárate para el ICFES» de los recursos, si la guía de apoyo de 11° lo trae
(se revisa en la etapa B); si no, se escriben y se verifican en el banco.

## Cierre del hilo

Del ámbar al pararrayos: una tradición griega, un médico que separó dos fenómenos, un ingeniero que
pesó una fuerza invisible, una profesora que enseñó física experimental cuando casi ninguna mujer
podía, y un impresor que convirtió el rayo en algo que se puede desviar. Pregunta que abre el
trimestre II: todo lo de este trimestre ocurre con cargas quietas; ¿qué pasa cuando se mueven?
Aparecen la corriente, los circuitos y el magnetismo que Gilbert había separado (segunda parte del
DBA 2 y DBA 3).

## Evaluación (borrador de la matriz)

- **Saber:** explica la naturaleza de la carga, las formas de electrización y la idea de campo.
- **Hacer:** predice el signo de un material frotado o tocado; calcula fuerzas y campos con Coulomb
  y superposición, con unidades correctas.
- **Ser:** estima órdenes de magnitud y revisa sus resultados antes de darlos por buenos;
  distingue lo documentado de lo que solo se cuenta (la cometa).
- **Convivir:** trabaja en equipo en el laboratorio y cuida los materiales y a sus compañeros.

## Referencias

Verificadas el 2026-09-14. En la etapa C cada `\bibitem` lleva su `% verificado:`.

| Clave | Referencia | Veredicto | Corrección | URL |
|---|---|---|---|---|
| bassi | Università di Bologna. *Laura Bassi*. | confirmada: nació en Bolonia en 1711; se graduó en filosofía en abril de 1732; cátedra de física experimental del Istituto delle Scienze en 1776 | edad: veinte años (no veintiuno) | https://www.unibo.it/en/university/who-we-are/our-history/famous-people-and-students/laura-bassi |
| coulomb1785 | Coulomb, C.-A. (1785). Premier mémoire sur l'électricité et le magnétisme. *Histoire de l'Académie Royale des Sciences*, 569–577. | confirmada (pp. 569–577, balanza de torsión con hilo de plata, inverso del cuadrado) | — | https://www.academie-sciences.fr/pdf/dossiers/Coulomb/Coulomb_pdf/Mem1785_p569.pdf · https://search.worldcat.org/title/Premier-troisieme-memoire-sur-l'electricite-et-le-magnetisme/oclc/123182481 · https://skullsinthestars.com/2026/03/19/coulombs-remarkable-experiment-in-electricity-1785/ (traducción de los pasajes) |
| debatecometa | National Constitution Center. *The great debate about if Benjamin Franklin really flew his kite*. | confirmada: las únicas fuentes son la carta de octubre de 1752 y Priestley (1767); hay historiadores que dudan | nueva | https://constitutioncenter.org/blog/the-great-debate-about-if-benjamin-franklin-really-flew-his-kite |
| franklin1752 | Franklin, B. (1752, 19 de octubre). [El experimento de la cometa]. *Pennsylvania Gazette*. En *Founders Online*, National Archives. | confirmada (frase: «the Sameness of the Electric Matter with that of Lightning compleatly demonstrated») | se aclara que Franklin «afirmó» el resultado | https://founders.archives.gov/documents/Franklin/01-04-02-0135 · https://fi.edu/en/science-and-education/benjamin-franklin/kite-key-experiment |
| franklin1753 | Franklin, B. (1752). *Poor Richard Improved, 1753*: «How to secure Houses, &c. from Lightning». En *Founders Online*. | confirmada (varilla de hierro en punta, enterrada en suelo húmedo) | nueva | https://founders.archives.gov/documents/Franklin/01-04-02-0148 |
| gilbert1600 | Gilbert, W. (1600). *De magnete, magneticisque corporibus, et de magno magnete tellure*. Londres: Peter Short. | confirmada (acuña *electricus*; unas treinta sustancias; versorium; separa ámbar e imán, libro 2, cap. 2) | — | https://archive.org/details/1600-william-gilbert-de-magnete · https://nationalmaglab.org/magnet-academy/history-of-electricity-magnetism/pioneers/william-gilbert/ |
| laercio | Diógenes Laercio, *Vidas de los filósofos ilustres*, I.24 (Tales: el imán y el ámbar, según Aristóteles e Hipias) | confirmada | nueva; en la etapa C se cita una edición en español verificada | http://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0258:book%3D1:chapter%3D1 |
| menestandares | Ministerio de Educación Nacional (2004). *Estándares Básicos de Competencias en Ciencias Naturales y Ciencias Sociales* (Guía n.º 7), p. 23. | confirmada (PDF local en `dba/`) | — | https://www.mineducacion.gov.co/1780/articles-81033_archivo_pdf.pdf |
| mendba | Ministerio de Educación Nacional (2016). *Derechos Básicos de Aprendizaje: Ciencias Naturales*. | tomada de la guía anterior, **sin reverificar** hoy | reverificar editorial, año e ISBN en la etapa C (la de Matemáticas tenía mal el ISBN) | https://www.colombiaaprende.edu.co/sites/default/files/files_public/2022-06/DBA_C.Naturales-min.pdf |
| serway | Serway, R. A. y Jewett, J. W. (2018). *Física para ciencias e ingeniería*, vol. 2 (10.ª ed.). Cengage. ISBN 978-607-526-670-1. | confirmada | antes no tenía año ni edición y la URL era de un distribuidor dudoso | https://www.gonvill.com.mx/libro/fisica-para-ciencias-e-ingenieria-vol-2-10ed-_17552422 · https://www.vitalsource.com/products/fisica-para-ciencias-e-ingenieria-volumen-2-raymond-a-serway-john-w-v9786075266725 |
| younes2020 | Younes-Velosa, C. (2020). Caracterización de parámetros del rayo en Colombia con base en sistemas de localización terrestres y satelitales, 20 años de análisis. *Revista de la Academia Colombiana de Ciencias Exactas, Físicas y Naturales*, 44(173). | confirmada («caso especial» por su actividad eléctrica atmosférica, relieve y ubicación tropical) | nueva | https://raccefyn.co/index.php/raccefyn/article/view/1171 |

## Errores encontrados en el recurso (guía de apoyo de 11°, capítulo 1)

- Atribuye a **Gilbert** los dos tipos de carga, «vítrea» y «resinosa»; fue **Charles du Fay**
  (1733), a quien el mismo texto menciona en el párrafo siguiente.
- «Keike Kamerling Onnes»: es **Heike Kamerlingh Onnes**.
- La lectura en voz alta de la fórmula de la carga elemental dice «1/(,25 × 10 a la 18)»: falta
  el 6 (6,25).
- La carga elemental se da como 1,6 × 10⁻¹⁹ C; la guía usa 1,602 × 10⁻¹⁹ C: conviene decir que
  es un redondeo.

## Lo que viene

- **Etapa B** (tras la aprobación de este plan): revisar los candidatos del banco
  (`electrostatica-11`: 20 verificados y 44 manuales pendientes); escribir y verificar los que
  faltan —la predicción del signo por fricción y contacto, con su serie de materiales y su fuente;
  la notación científica en contexto de carga; las cuatro preguntas de Saber 11— y los ejemplos
  resueltos del marco teórico (21,6 N; 5,0 × 10⁵ N/C; 4 × 10⁴²; 1,25 × 10¹⁰ electrones); tabla
  id · enunciado · respuesta · estado para la Revisión 2, con las respuestas de Saber 11.
- **Etapa C:** reemplazar el `.tex` actual con este plan y los ejercicios del banco.
