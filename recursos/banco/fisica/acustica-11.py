"""Banco de ejercicios — Física 11° — Acústica (sonido, intensidad, Doppler, cuerdas y tubos).
Fuente: Guía de Apoyo «Fenómenos ondulatorios» grado 11, Capítulo 3: acústica; se lee en
recursos/fisica/Guías pedagógicas Física/markdown/11 - Guia_de_Apoyo_Fenomenos_ondulatorios_grado_11_fisica.md
(secciones «Desarrolla tus competencias», «Actividades» y «Problemas»).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/fisica/acustica-11.py

Convenciones de la guía: v = 331 m/s + 0,6 m/s·°C⁻¹·T (aire, 0–35 °C); I₀ = 10⁻¹² W/m²;
β = 10 dB·log(I/I₀); I = P/(4πr²); cuerdas y tubos abiertos fₙ = nv/(2L); tubos cerrados
fₙ = nv/(4L) con n impar. Si el problema no da la velocidad del sonido se usa 340 m/s.

Numeración de la guía: en «Desarrolla tus competencias», los literales 5a–5c y 6a–6b son
preguntas sueltas sin relación con los enunciados 5 y 6; se citan tal como aparecen.

No incluidos:
- Desarrolla tus competencias 3a–3f (límites de intensidad audible a 32, 128, … 8.192 Hz):
  requieren la curva de audibilidad, que la guía no trae.
- Prácticas de laboratorio del capítulo.

Errores de la teoría (no son ejercicios, se avisan): la Tabla 7 da 336 m/s para el aire a
100 °C (debería ser ≈ 386 m/s: la velocidad aumenta con la temperatura); el texto de «Tubos
sonoros» llama «valles» a las compresiones.
"""
import math

from sympy import nsolve, sqrt, symbols
from sympy.physics import units as u
from sympy.physics.units import convert_to

from ejercicios import ejercicio, ejercicio_manual

GUIA = "Guía de Apoyo Fenómenos ondulatorios 11°"
CAP = "Capítulo 3: acústica"
DTC, ACT, PRO = "Desarrolla tus competencias", "Actividades", "Problemas"
COMUN = dict(grados=[11], dba=["naturales-11-1"])
V = 340 * u.meter / u.second          # velocidad del sonido en el aire (convención)
I0 = 1e-12 * u.watt / u.meter**2


def fuente(seccion, literal):
    return f"{GUIA}, {CAP}, {seccion} — {literal}"


def valor(q, unidad):
    return float(convert_to(q, unidad) / unidad)


def aprox(a, b, rel=0.01):
    return math.isclose(a, b, rel_tol=rel)


def opciones(*items):
    return r" \begin{opciones} " + " ".join(r"\item " + i for i in items) + r" \end{opciones}"


def manual(n, seccion, literal, enunciado, respuesta, tema="acústica", tipo="conceptual",
           dificultad=1, **extra):
    ejercicio_manual(id=f"acustica-11-{n:03d}", tema=tema, tipo=tipo, dificultad=dificultad,
                     fuente=fuente(seccion, literal), enunciado=enunciado,
                     respuesta=respuesta, **COMUN, **extra)


def vf(n, seccion, literal, afirmacion, verdad, justificacion, tema="acústica", **extra):
    manual(n, seccion, literal,
           r"Escribe V si la afirmación es verdadera o F si es falsa, y justifica: " + afirmacion,
           ("V. " if verdad else "F. ") + justificacion, tema=tema, tipo="argumentacion",
           **extra)


def num(n, seccion, literal, enunciado, respuesta, tema="acústica", tipo="calculo",
        dificultad=2, **extra):
    return ejercicio(id=f"acustica-11-{n:03d}", tema=tema, tipo=tipo, dificultad=dificultad,
                     fuente=fuente(seccion, literal), enunciado=enunciado,
                     respuesta=respuesta, **COMUN, **extra)


# ======================= Desarrolla tus competencias =======================

CONCEPTOS = (r" Conceptos: intensidad, ondas de presión, decibeles, ondas de choque, timbre, "
             r"tono.")
for n, lit, definicion, concepto in [
    (1, "1a", "Ondas que tienen un aumento de presión y, luego, una disminución que se propaga a "
              "las demás regiones del medio.", "Ondas de presión."),
    (2, "1b", "Característica que permite diferenciar los sonidos graves de los agudos.",
     "Tono (depende de la frecuencia)."),
    (3, "1c", "Característica que permite diferenciar los sonidos fuertes de los débiles.",
     "Intensidad."),
    (4, "1d", "Unidad de medida utilizada para medir el nivel de intensidad del sonido.",
     "Decibeles (dB)."),
    (5, "1e", "Característica para distinguir los sonidos emitidos por dos fuentes aun si tienen "
              "otras características idénticas.", "Timbre."),
    (6, "1f", "Ondas que se forman alineándose para generar un sonido mayor.",
     "Ondas de choque (se forman cuando la fuente va más rápido que el sonido)."),
]:
    manual(n, DTC, lit, "Relaciona la definición con su concepto: " + definicion + CONCEPTOS,
           concepto, tipo="seleccion",
           notas="En 1d la guía dice «intensidad del sonido»; el decibel mide el *nivel* de "
                 "intensidad." if lit == "1d" else None)

for n, lit, par, resp in [
    (7, "2a", "tubos abiertos y tubos cerrados",
     r"El tubo abierto tiene los dos extremos abiertos (vientres en ambos) y produce todos los "
     r"armónicos, $f_n = \dfrac{nv}{2L}$; el cerrado tiene un extremo cerrado (nodo) y otro "
     r"abierto (vientre) y solo produce armónicos impares, $f_n = \dfrac{nv}{4L}$. Con igual "
     r"longitud, el cerrado suena una octava más grave."),
    (8, "2b", "frecuencia fundamental y segundo armónico",
     r"La fundamental es la frecuencia más baja con que resuena el sistema ($n = 1$); el segundo "
     r"armónico tiene el doble de esa frecuencia ($n = 2$) y existe en cuerdas y tubos abiertos, "
     r"no en tubos cerrados."),
    (9, "2c", "onda predominante y onda de choque",
     r"La onda predominante es la componente de mayor amplitud de un sonido compuesto (define su "
     r"tono); la onda de choque es el frente cónico de gran intensidad que se forma cuando la "
     r"fuente se mueve más rápido que el sonido."),
    (10, "2d", "reverberación e intensidad del sonido",
     r"La reverberación es la persistencia del sonido por reflexiones sucesivas que llegan con "
     r"menos de \num{0,1} s de diferencia; la intensidad es la potencia que transporta la onda "
     r"por unidad de área (W/m²)."),
    (11, "2e", "umbral de dolor y umbral de audición",
     r"El umbral de audición es la mínima intensidad audible, $10^{-12}$ W/m² (0 dB); el umbral "
     r"de dolor es la intensidad a partir de la cual el sonido causa dolor, cerca de 1 W/m² "
     r"(120 dB)."),
]:
    manual(n, DTC, lit, f"Establece diferencias entre {par}.", resp)

manual(12, DTC, "4",
       r"Ordena de menor a mayor los medios según la rapidez de propagación del sonido en ellos y "
       r"explica: metal, aire frío, aire caliente, arena.",
       r"Aire frío < aire caliente < arena < metal. En los gases la rapidez aumenta con la "
       r"temperatura; en los sólidos es mayor porque son mucho menos compresibles, y el metal, "
       r"rígido y continuo, es el más rápido. (La arena suelta y seca transmite mal el sonido: "
       r"su rapidez es solo algo mayor que la del aire.)", dificultad=2)


@num(13, DTC, "5",
     r"Dos cuerdas de 80 cm de longitud y densidad lineal de masa $\num{0,0045}$ kg/m están "
     r"sometidas a tensiones de 180 N y 200 N. ¿Cuál es la frecuencia de las pulsaciones "
     r"producidas al hacerlas vibrar simultáneamente en su frecuencia fundamental?",
     r"$f_1 = \frac{1}{2L}\sqrt{F/\mu}$: $f_A = 125$ Hz y $f_B \approx \num{131,8}$ Hz; "
     r"pulsaciones $f_B - f_A \approx \num{6,8}$ Hz.", tema="pulsaciones", dificultad=3)
def _():
    L, mu = 0.8 * u.meter, 0.0045 * u.kilogram / u.meter
    fA = valor(sqrt(180 * u.newton / mu) / (2 * L), u.hertz)
    fB = valor(sqrt(200 * u.newton / mu) / (2 * L), u.hertz)
    assert aprox(fA, 125) and aprox(fB, 131.8)
    assert aprox(fB - fA, 6.8, 0.02)


manual(14, DTC, "5a",
       r"Escribe cuatro ejemplos de trabajadores que deben extremar las medidas de protección "
       r"para evitar los problemas derivados de la contaminación acústica.",
       r"Por ejemplo: operarios de martillos neumáticos y maquinaria de construcción, personal "
       r"de tierra de los aeropuertos, trabajadores de fábricas con máquinas (textiles, "
       r"metalmecánica), músicos y técnicos de sonido de conciertos y discotecas.",
       tipo="contexto",
       notas="Literal suelto de la guía, sin relación con el enunciado 5.")
manual(15, DTC, "5b",
       r"¿Cómo se explica que, al caer al suelo, distintos cuerpos emitan sonidos diferentes?",
       r"Cada cuerpo vibra con sus propias frecuencias naturales (según su material, forma, "
       r"tamaño y rigidez) y con distinta combinación de armónicos: por eso cambian el tono y el "
       r"timbre del sonido.", notas="Literal suelto de la guía, sin relación con el enunciado 5.")
manual(16, DTC, "5c", r"¿Puede una onda sonora anular a otra? Explica tu respuesta.",
       r"Sí, en ciertos puntos: si dos ondas de igual frecuencia y amplitud llegan en oposición "
       r"de fase (compresión con rarefacción), la interferencia es destructiva y allí se anulan. "
       r"Es el principio de los audífonos con cancelación de ruido. La energía no desaparece: se "
       r"redistribuye hacia los puntos de interferencia constructiva.", dificultad=2,
       notas="Literal suelto de la guía, sin relación con el enunciado 5.")
manual(17, DTC, "6",
       r"Según la lectura sobre la ecolocalización, ¿por qué los seres humanos no emitimos ni "
       r"percibimos ultrasonidos? Explica tu respuesta.",
       r"Porque nuestras cuerdas vocales no vibran tan rápido (producimos frecuencias de unos "
       r"cientos a pocos miles de hercios) y el oído humano solo responde entre 20 Hz y "
       r"20.000 Hz; los ultrasonidos, por encima de 20.000 Hz, quedan fuera de ese intervalo.")
manual(18, DTC, "6a",
       r"En los últimos años los científicos han estudiado la forma de ayudar a las personas "
       r"ciegas por medio de la ecolocalización. ¿Cómo podría concretarse esta ayuda?",
       r"Con dispositivos (bastones, gafas o pulseras) que emiten ultrasonidos, reciben el eco y "
       r"lo convierten en sonidos audibles o vibraciones que indican la distancia y dirección "
       r"de los obstáculos; también entrenando la ecolocalización con chasquidos de la lengua.",
       tipo="contexto", notas="Literal suelto de la guía, sin relación con el enunciado 6.")
manual(19, DTC, "6b", r"¿Cuáles son las posibles consecuencias de la exposición al ruido excesivo?",
       r"Pérdida auditiva temporal o permanente (sobre todo en frecuencias altas, cerca de "
       r"4.000 Hz), zumbido (tinnitus), ruptura del tímpano con ruidos muy intensos, además de "
       r"estrés, insomnio, irritabilidad y dificultad para concentrarse.", tipo="contexto",
       notas="Literal suelto de la guía, sin relación con el enunciado 6.")
manual(20, DTC, "7",
       r"La mitad de los jóvenes entre 18 y 27 años presentan algún tipo de discapacidad auditiva, "
       r"normalmente por el uso excesivo de audífonos y el ruido de conciertos o discotecas. "
       r"¿Qué propondrías para evitar este tipo de daños al oído?",
       r"Escuchar con audífonos a no más del 60 % del volumen y por periodos cortos (regla "
       r"60/60), preferir audífonos con cancelación de ruido para no subir el volumen, usar "
       r"tapones en conciertos y discotecas, alejarse de los parlantes y descansar el oído en "
       r"silencio después de exponerse a ruido fuerte.", tipo="contexto")

# ================================ Actividades ================================

for n, lit, af, verdad, just in [
    (21, "1a", "El sonido es una onda longitudinal y mecánica.", True,
     "Necesita un medio material y las partículas oscilan en la dirección de propagación."),
    (22, "1b", "Cuando la temperatura aumenta, la rapidez de las moléculas disminuye.", False,
     "Al aumentar la temperatura las moléculas se mueven más rápido, y por eso el sonido "
     "también se propaga más rápido en el aire."),
    (23, "1c", "Al disminuir la densidad del medio de propagación de la onda, la velocidad de "
               "propagación de la onda disminuye.", False,
     "Con la misma compresibilidad, a menor densidad del medio mayor rapidez del sonido."),
    (24, "1d", "El ser humano percibe sonidos que están en frecuencias entre 20 Hz y 20.000 Hz.",
     True, "Ese es el intervalo audible; por debajo están los infrasonidos y por encima los "
           "ultrasonidos."),
    (25, "1e", "El nivel de intensidad del sonido depende de la mínima intensidad audible por el "
               "ser humano.", True,
     r"$\beta = 10\,\text{dB}\cdot\log\frac{I}{I_0}$ compara la intensidad con "
     r"$I_0 = 10^{-12}$ W/m², la mínima audible."),
    (26, "1f", "La variación de la intensidad del sonido tiene una relación directamente "
               "proporcional con la superficie donde se propaga el sonido.", False,
     r"$I = \frac{P}{4\pi r^2}$: la intensidad es inversamente proporcional al área del frente "
     r"de onda."),
    (27, "1g", "La frecuencia de las ondas sonoras depende del movimiento relativo que tiene la "
               "fuente sonora o el observador.", True,
     "Es el efecto Doppler: la frecuencia *percibida* cambia con el movimiento relativo "
     "(la frecuencia emitida por la fuente no cambia)."),
]:
    vf(n, ACT, lit, af, verdad, just)

manual(28, ACT, "2", r"El eco de un sonido depende de:" + opciones(
    "La interferencia.", "La reflexión.", "La difracción.", "La refracción."),
       r"b. La reflexión: el eco es el sonido reflejado en un obstáculo que regresa al emisor.",
       tipo="seleccion")
manual(29, ACT, "3", r"La velocidad de propagación de un sonido depende de:" + opciones(
    "La compresibilidad.", "El tono.", "La intensidad.", "El timbre."),
       r"a. La compresibilidad (del medio); tono, intensidad y timbre son cualidades del sonido "
       r"que no cambian su rapidez.", tipo="seleccion")
manual(30, ACT, "4", r"La rarefacción del aire ocurre:" + opciones(
    "Cuando su temperatura aumenta.", "Cuando la presión del aire aumenta.",
    "Cuando disminuye la densidad del aire.", "Cuando su temperatura y presión disminuyen."),
       r"c. Una rarefacción es una zona donde las moléculas se separan: disminuyen la densidad y "
       r"la presión del aire.", tipo="seleccion")


@num(31, ACT, "5",
     r"Si una trompeta y un piano suenan afinados a una temperatura de 16 °C, ¿seguirán "
     r"estándolo a 30 °C?",
     r"No. La trompeta es un tubo sonoro: su frecuencia $f = \frac{nv}{2L}$ es proporcional a la "
     r"velocidad del sonido, que pasa de $\num{340,6}$ m/s a 349 m/s; su tono sube cerca de un "
     r"\num{2,5} \%. Las cuerdas del piano casi no cambian (su frecuencia depende de la tensión y "
     r"la densidad de la cuerda), así que quedan desafinados.",
     tipo="argumentacion", tema="tubos sonoros", dificultad=3)
def _():
    v16 = 331 + 0.6 * 16
    v30 = 331 + 0.6 * 30
    assert aprox(v16, 340.6) and aprox(v30, 349)
    assert aprox(v30 / v16 - 1, 0.025, 0.05)   # la frecuencia del tubo sube ≈ 2,5 %


manual(32, ACT, "6",
       r"Si apoyas firmemente un diapasón contra una mesa de madera, el sonido se hace más "
       r"intenso. ¿Por qué? ¿Cómo afecta esto al tiempo durante el cual puede vibrar el diapasón? "
       r"Explícalo con la ley de conservación de la energía.",
       r"La mesa entra en vibración forzada y, por su gran superficie, pone en movimiento mucho "
       r"más aire (actúa como caja de resonancia): se emite más potencia sonora. Como la energía "
       r"del diapasón es la misma y ahora se entrega más rápido al aire, se agota antes: el "
       r"diapasón vibra menos tiempo.", dificultad=2)
manual(33, ACT, "7",
       r"Javier ubica un parlante que emite sonidos de 200 Hz frente a él. Explica qué ocurre con "
       r"el aire que está entre Javier y el parlante. ¿Por qué Javier recibe sonido en ambos "
       r"oídos?",
       r"Las capas de aire oscilan de ida y vuelta en la dirección de propagación, 200 veces por "
       r"segundo, formando compresiones y rarefacciones que avanzan hasta Javier (el aire no viaja "
       r"hasta él, solo oscila). Su longitud de onda es $\lambda = 340/200 = \num{1,7}$ m, mucho "
       r"mayor que la cabeza, así que la onda la rodea por difracción y llega a ambos oídos.",
       dificultad=2, notas="La guía remite a una figura; el enunciado se escribió sin ella.")
manual(34, ACT, "8",
       r"Cuando un instrumento suena, ¿sus vibraciones producen ondas sonoras? Explica tu "
       r"respuesta.",
       r"Sí: la vibración de la cuerda, la membrana o la columna de aire empuja las moléculas de "
       r"aire vecinas y produce compresiones y rarefacciones que se propagan como onda sonora "
       r"longitudinal; la caja de resonancia amplifica esa vibración.")

for n, lit, af, verdad, just, tema in [
    (35, "9a", "El sonido se produce gracias a la vibración de los objetos.", True,
     "Toda fuente sonora es un cuerpo que vibra y transmite esa vibración al medio.", "sonido"),
    (36, "9b", "La frecuencia en una cuerda aumenta cuando la longitud de la cuerda aumenta, "
               "manteniendo la velocidad de propagación constante.", False,
     r"$f_n = \frac{nv}{2L}$: con $v$ constante, al aumentar $L$ la frecuencia disminuye.",
     "tubos sonoros"),
    (37, "9c", "En los extremos de un tubo abierto se generan los vientres de la onda.", True,
     "En un extremo abierto el aire se mueve libremente: allí hay un vientre de desplazamiento.",
     "tubos sonoros"),
    (38, "9d", "La voz se forma por ondas sonoras producidas en la tráquea.", False,
     "La voz se produce en la laringe, donde vibran las cuerdas vocales; la tráquea solo conduce "
     "el aire de los pulmones.", "sonido"),
    (39, "9e", "La reverberación impide escuchar de forma nítida los sonidos.", True,
     "Cuando es excesiva, las reflexiones se superponen con el sonido directo y lo hacen "
     "confuso; en poca medida da «cuerpo» al sonido de un auditorio.", "sonido"),
    (40, "9f", "Si en un tubo cerrado se generan tres vientres en la onda, hay tres nodos.", True,
     "En el tubo cerrado hay un nodo en el extremo cerrado y un vientre en el abierto, "
     r"alternados: N–V–N–V–N–V, tres de cada uno (quinto armónico, $L = 5\lambda/4$).",
     "tubos sonoros"),
    (41, "9g", "La frecuencia de los sonidos producidos por dos tubos de igual longitud, uno "
               "abierto y el otro cerrado, es la misma.", False,
     r"La fundamental del abierto es $\frac{v}{2L}$ y la del cerrado $\frac{v}{4L}$: el cerrado "
     r"suena una octava más grave.", "tubos sonoros"),
]:
    vf(n, ACT, lit, af, verdad, just, tema=tema)

manual(42, ACT, "10", r"Elige la respuesta correcta. Los sonidos de la voz son producidos por:"
       + opciones("La tráquea.", "Las cuerdas vocales.", "La laringe.", "La garganta."),
       r"b. Las cuerdas vocales, que vibran al paso del aire (están dentro de la laringe).",
       tipo="seleccion", tema="sonido",
       notas="Se añadió «de la voz» al enunciado («Los sonidos son producidos por:»). La opción c "
             "(laringe) puede considerarse aceptable, pues allí están las cuerdas vocales; "
             "decisión de la docente.")
manual(43, ACT, "11",
       r"En los vehículos, el silenciador funciona gracias a dos conductos diferentes por donde "
       r"viaja el sonido, de modo que se genera una diferencia de caminos. ¿Cómo esta diferencia "
       r"de caminos reduce el ruido?",
       r"Si la diferencia de caminos es media longitud de onda (o un número impar de medias "
       r"longitudes de onda), las dos partes del sonido se encuentran en oposición de fase "
       r"(compresión con rarefacción) y se produce interferencia destructiva: la amplitud, y con "
       r"ella la intensidad, disminuye.", dificultad=2)
manual(44, ACT, "12",
       r"Explica por qué cuando se tienen recipientes llenos de agua a diferentes alturas se "
       r"pueden generar distintos sonidos.",
       r"Cada recipiente se comporta como un tubo cerrado por el agua: la columna de aire tiene "
       r"distinta longitud y resuena a $f = \frac{v}{4L}$, así que más agua (columna más corta) "
       r"da un sonido más agudo al soplar. Si se golpea el vaso, lo que vibra es el vidrio con el "
       r"agua, y más agua da un sonido más grave.", tema="tubos sonoros", dificultad=2)
manual(45, ACT, "13",
       r"Explica las razones para construir auditorios con techos en forma parabólica, como en "
       r"la Ópera de Sídney.",
       r"Una superficie parabólica refleja el sonido de manera ordenada y lo dirige hacia el "
       r"público, de modo que llegue con intensidad pareja a todas las sillas y sin ecos "
       r"molestos; se aprovecha la reflexión del sonido.")
manual(46, ACT, "14",
       r"Explica por qué el arpa, para generar diferentes sonidos, tiene unas cuerdas más largas "
       r"que otras.",
       r"La frecuencia fundamental de una cuerda es $f_1 = \frac{1}{2L}\sqrt{F/\mu}$: las cuerdas "
       r"largas producen sonidos graves y las cortas, agudos; así el arpa cubre muchas notas.",
       tema="tubos sonoros")
manual(47, ACT, "15",
       r"Explica por qué los sonidos producidos por un bajo son más graves que los de una guitarra "
       r"si su funcionamiento es similar.",
       r"Las cuerdas del bajo son más largas y mucho más gruesas (mayor densidad lineal $\mu$); "
       r"como $f_1 = \frac{1}{2L}\sqrt{F/\mu}$, ambas cosas bajan la frecuencia fundamental.",
       tema="tubos sonoros")
manual(48, ACT, "16",
       r"¿Por qué las cuerdas vocales de los hombres, en la mayoría de los casos, producen sonidos "
       r"más graves que las de las mujeres?",
       r"En los hombres las cuerdas vocales suelen ser más largas y gruesas (más masa), por lo que "
       r"vibran con menor frecuencia y la voz es más grave.", tema="sonido")
manual(49, ACT, "17",
       r"Explica por qué cambian los sonidos en los instrumentos de cuerda cuando la longitud de "
       r"las cuerdas cambia, como en los violines o las guitarras.",
       r"Al pisar la cuerda se acorta la parte que vibra; como $f_n = \frac{nv}{2L}$ con la misma "
       r"$v$, una longitud menor da una frecuencia mayor (sonido más agudo).",
       tema="tubos sonoros")
manual(50, ACT, "18",
       r"La flauta de pan consta de varios tubos cerrados unidos, de distintas longitudes. "
       r"Explica por qué se generan diferentes sonidos en este instrumento.",
       r"Cada tubo cerrado resuena con fundamental $f_1 = \frac{v}{4L}$: los tubos largos dan "
       r"notas graves y los cortos, agudas.", tema="tubos sonoros")

# ================================ Problemas ================================


@num(51, PRO, "1",
     r"Calcula la distancia a la que se produce una tormenta si un trueno se escucha 4 s después "
     r"de haber visto el rayo. Considera la velocidad del sonido como 340 m/s.",
     r"$d = vt = (340\ \text{m/s})(4\ \text{s}) = 1360$ m (la luz llega prácticamente al "
     r"instante).", dificultad=1)
def _():
    assert valor(V * 4 * u.second, u.meter) == 1360
    assert valor(1360 * u.meter / u.speed_of_light, u.second) < 1e-5


@num(52, PRO, "2",
     r"Al dejar caer una piedra en un pozo, se escucha 4 s después el sonido que produce al "
     r"chocar contra la superficie del agua. ¿A qué profundidad está la superficie del agua? "
     r"Usa $g = \num{9,8}$ m/s² y $v = 340$ m/s.",
     r"El tiempo total es el de caída más el de subida del sonido: "
     r"$\sqrt{\dfrac{2h}{g}} + \dfrac{h}{v} = 4$ s. Resolviendo, $h \approx \num{70,5}$ m "
     r"(caída \num{3,79} s y sonido \num{0,21} s).", dificultad=3,
     notas="La guía no da g ni la velocidad del sonido: se añadieron g = 9,8 m/s² y "
           "v = 340 m/s.")
def _():
    h = symbols("h", positive=True)
    prof = float(nsolve(sqrt(2 * h / 9.8) + h / 340 - 4, h, 70))
    assert aprox(prof, 70.5, 0.005)
    caida = valor(sqrt(2 * prof * u.meter / (9.8 * u.meter / u.second**2)), u.second)
    assert aprox(caida + prof / 340, 4, 1e-6)


@num(53, PRO, "3",
     r"Un avión vuela horizontalmente a 900 km/h. El sonido que emite cuando pasa exactamente "
     r"sobre nosotros tarda 5 s en llegar a nuestros oídos. ¿A qué altura vuela y a qué distancia "
     r"horizontal se encontrará el avión cuando escuchemos ese sonido?",
     r"Altura: $h = vt = 340 \cdot 5 = 1700$ m. En esos 5 s el avión avanza "
     r"$(250\ \text{m/s})(5\ \text{s}) = 1250$ m: esa es su distancia horizontal.", dificultad=2,
     notas="En la guía falta la velocidad del avión y no se puede calcular la distancia "
           "horizontal; se añadió 900 km/h y se pidió también la altura.")
def _():
    assert valor(V * 5 * u.second, u.meter) == 1700
    va = 900 * u.kilometer / u.hour
    assert aprox(valor(va, u.meter / u.second), 250)
    assert aprox(valor(va * 5 * u.second, u.meter), 1250)


@num(54, PRO, "4",
     r"Una persona parada frente a una montaña emite un grito y su eco se escucha 2 s después. "
     r"Calcula la distancia entre la persona y la montaña. ¿Se percibe el mismo fenómeno si la "
     r"montaña se encuentra a 10 m?",
     r"El sonido va y vuelve: $d = \frac{vt}{2} = \frac{340 \cdot 2}{2} = 340$ m. A 10 m el eco "
     r"regresaría en $\frac{20}{340} \approx \num{0,06}$ s, menos de \num{0,1} s (tiempo mínimo "
     r"para que el oído distinga dos sonidos): no se oye eco, sino reverberación.")
def _():
    assert valor(V * 2 * u.second / 2, u.meter) == 340
    t10 = valor(20 * u.meter / V, u.second)
    assert aprox(t10, 0.059, 0.01) and t10 < 0.1


@num(55, PRO, "5a",
     r"La velocidad del sonido en el aire es de 340 m/s. Calcula la longitud de onda de una "
     r"vibración de 256 Hz cuando se propaga en el aire.",
     r"$\lambda = \frac{v}{f} = \frac{340}{256} \approx \num{1,33}$ m.", dificultad=1)
def _():
    assert aprox(valor(V / (256 * u.hertz), u.meter), 1.33, 0.005)


@num(56, PRO, "5b",
     r"La velocidad del sonido en el agua es de 1.490 m/s. Calcula la longitud de onda de una "
     r"vibración de 256 Hz cuando se propaga en el agua.",
     r"$\lambda = \frac{v}{f} = \frac{1490}{256} \approx \num{5,82}$ m.", dificultad=1,
     notas="La guía da 1.240 m/s para el agua, que contradice su propia Tabla 7 (1.490 m/s a "
           "25 °C); se usó 1.490 m/s. Con 1.240 m/s daría 4,84 m.")
def _():
    lam = valor(1490 * u.meter / u.second / (256 * u.hertz), u.meter)
    assert aprox(lam, 5.82, 0.005)


@num(57, PRO, "6a",
     r"Dos personas están a 1,1 km una de otra. Una hace explotar un petardo y la otra mide el "
     r"tiempo transcurrido: 3 s. Calcula el tiempo que tarda el sonido (340 m/s) en recorrer la "
     r"distancia entre ellas y compáralo con el dato del enunciado.",
     r"$t = \frac{1100}{340} \approx \num{3,24}$ s: el sonido llegó \num{0,24} s antes de lo "
     r"esperado.")
def _():
    t = valor(1.1 * u.kilometer / V, u.second)
    assert aprox(t, 3.24, 0.005) and t > 3


@num(58, PRO, "6b",
     r"En la situación anterior (1,1 km en 3 s), razona si durante la experiencia sopla viento a "
     r"favor o en contra.",
     r"A favor: el sonido avanzó a $\frac{1100}{3} \approx \num{366,7}$ m/s, más que 340 m/s; el "
     r"viento lo arrastró a unos \num{26,7} m/s (unos 96 km/h, un viento muy fuerte).",
     tipo="argumentacion")
def _():
    vef = valor(1.1 * u.kilometer / (3 * u.second), u.meter / u.second)
    assert aprox(vef, 366.7, 0.001) and aprox(vef - 340, 26.7, 0.01)


@num(59, PRO, "7a",
     r"La onda acústica de una sirena de bomberos tiene una frecuencia de 3.600 Hz. Calcula su "
     r"velocidad de propagación en el aire.",
     r"340 m/s: la velocidad del sonido depende del medio, no de la frecuencia.",
     tipo="conceptual", dificultad=1,
     notas="Se añadió «en el aire»; la respuesta es la velocidad del sonido (340 m/s).")
def _():
    lam = V / (3600 * u.hertz)
    assert aprox(valor(lam * 3600 * u.hertz, u.meter / u.second), 340)


@num(60, PRO, "7b",
     r"La onda acústica de una sirena de bomberos tiene una frecuencia de 3.600 Hz. Calcula su "
     r"período.",
     r"$T = \frac{1}{f} = \frac{1}{3600} \approx \num{2,78}\times10^{-4}$ s.", dificultad=1)
def _():
    assert aprox(valor(1 / (3600 * u.hertz), u.second), 2.78e-4, 0.005)


manual(61, PRO, "7c", r"¿Originan algún tipo de contaminación las sirenas?",
       r"Sí, contaminación acústica: su nivel es de unos 110–120 dB cerca de la fuente. Se "
       r"justifica por su función de alerta, pero deben usarse solo en emergencias.",
       tipo="contexto")


@num(62, PRO, "8",
     r"El sonar de un barco emite señales que tardan 2 s desde que se emiten hasta que rebotan en "
     r"un grupo de peces y retornan al barco. Si la velocidad del sonido en el agua es 5.200 km/h, "
     r"¿a qué distancia se encuentran los peces?",
     r"$v = 5200$ km/h $\approx \num{1444}$ m/s; ida y vuelta: "
     r"$d = \frac{vt}{2} \approx \num{1444}$ m $\approx \num{1,44}$ km.")
def _():
    v = 5200 * u.kilometer / u.hour
    vs = valor(v, u.meter / u.second)
    assert aprox(vs, 1444.4, 0.001) and 1400 < vs < 1550     # realista en el agua de mar
    assert aprox(valor(v * 2 * u.second / 2, u.meter), 1444, 0.001)


@num(63, PRO, "9a",
     r"Algunos animales, como los perros y los delfines, pueden percibir sonidos muy agudos de "
     r"hasta 100.000 Hz. Calcula el período de ese sonido.",
     r"$T = \frac{1}{f} = 10^{-5}$ s.", dificultad=1)
def _():
    assert aprox(valor(1 / (100000 * u.hertz), u.second), 1e-5)


@num(64, PRO, "9b",
     r"Calcula la longitud de onda de un sonido de 100.000 Hz en el aire (340 m/s).",
     r"$\lambda = \frac{v}{f} = \frac{340}{100\,000} = \num{3,4}\times10^{-3}$ m "
     r"$= \num{3,4}$ mm.", dificultad=1,
     notas="La guía no dice en qué medio; se especificó el aire (en el agua, a 1.490 m/s, "
           "sería 1,49 cm).")
def _():
    assert aprox(valor(V / (100000 * u.hertz), u.meter), 3.4e-3)


@num(65, PRO, "10",
     r"Halla la longitud de onda de un sonido en el aire a 20 °C si su frecuencia es 10.000 Hz.",
     r"$v = 331 + \num{0,6}\cdot 20 = 343$ m/s; $\lambda = \frac{343}{10\,000} = "
     r"\num{0,0343}$ m $= \num{3,43}$ cm.", dificultad=2)
def _():
    v = (331 + 0.6 * 20) * u.meter / u.second
    assert aprox(valor(v / (10000 * u.hertz), u.centimeter), 3.43)


@num(66, PRO, "11",
     r"Un sonar emite en el agua de mar ultrasonidos de 40.000 Hz. Si la temperatura del agua es "
     r"0 °C, la velocidad del sonido es de unos 1.450 m/s. Calcula la longitud de onda de los "
     r"ultrasonidos.",
     r"$\lambda = \frac{v}{f} = \frac{1450}{40\,000} \approx \num{0,036}$ m $= \num{3,6}$ cm.",
     notas="La guía no da la velocidad del sonido en el agua de mar a 0 °C (su fórmula es solo "
           "para el aire); se añadió el dato 1.450 m/s.")
def _():
    assert aprox(valor(1450 * u.meter / u.second / (40000 * u.hertz), u.centimeter), 3.625)


manual(67, PRO, "12a",
       r"El oído humano solo percibe frecuencias entre 20 Hz y 20.000 Hz. ¿Cómo se denominan los "
       r"sonidos con frecuencias superiores?", r"Ultrasonidos.", tema="sonido")
manual(68, PRO, "12b", r"¿Qué aplicaciones tienen los ultrasonidos?",
       r"Ecografías médicas, destrucción de cálculos renales sin cirugía, sonares para medir "
       r"profundidades y detectar peces, detección de fallas en materiales, limpieza de piezas y "
       r"alarmas o repelentes de animales.", tipo="contexto", tema="sonido")


@num(69, PRO, "12c",
     r"Calcula las longitudes de onda (en el aire, a 340 m/s) de los sonidos que el oído humano "
     r"no percibe.",
     r"Los audibles van de $\lambda = \frac{340}{20\,000} = \num{1,7}$ cm a "
     r"$\lambda = \frac{340}{20} = 17$ m. No se perciben los ultrasonidos, con "
     r"$\lambda < \num{1,7}$ cm, ni los infrasonidos, con $\lambda > 17$ m.")
def _():
    assert aprox(valor(V / (20000 * u.hertz), u.centimeter), 1.7)
    assert aprox(valor(V / (20 * u.hertz), u.meter), 17)


@num(70, PRO, "13a",
     r"Un excursionista grita frente a un precipicio de 680 m de profundidad. ¿Cuánto tiempo "
     r"tarda en escuchar el eco?",
     r"El sonido baja y sube: $t = \frac{2 \cdot 680}{340} = 4$ s.", dificultad=1)
def _():
    assert aprox(valor(2 * 680 * u.meter / V, u.second), 4)


manual(71, PRO, "13b",
       r"Si el excursionista grita frente al precipicio en un día caluroso, ¿tardará más o menos "
       r"tiempo en escuchar el eco?",
       r"Menos: con mayor temperatura el sonido viaja más rápido en el aire "
       r"($v = 331 + \num{0,6}\,T$).")


@num(72, PRO, "14",
     r"Una fuente sonora de 25.000 W emite en todas las direcciones. El observador A está a "
     r"100 m de la fuente; B, sobre la misma recta, a 150 m; C, en dirección perpendicular, a "
     r"250 m, y D en el punto (150 m, 250 m) respecto a la fuente. ¿Con qué intensidad percibe "
     r"el sonido cada observador?",
     r"$I = \frac{P}{4\pi r^2}$. A: $\approx \num{0,199}$ W/m²; B: $\approx \num{0,088}$ W/m²; "
     r"C: $\approx \num{0,032}$ W/m²; D ($r = \sqrt{150^2 + 250^2} \approx \num{291,5}$ m): "
     r"$\approx \num{0,023}$ W/m².", tema="intensidad del sonido", dificultad=3,
     notas="Se reescribió la ubicación de los observadores; se interpretó que todas las "
           "distancias se miden desde la fuente.")
def _():
    P = 25000 * u.watt
    Wm2 = u.watt / u.meter**2
    I = lambda r: valor(P / (4 * math.pi * (r * u.meter)**2), Wm2)
    assert aprox(I(100), 0.199) and aprox(I(150), 0.0884, 0.01)
    assert aprox(I(250), 0.0318, 0.01)
    rD = math.hypot(150, 250)
    assert aprox(rD, 291.5, 0.001) and aprox(I(rD), 0.0234, 0.01)
    assert I(100) < 1          # por debajo del umbral de dolor


@num(73, PRO, "15",
     r"En un concierto de rock hay 45.000 aficionados gritando las canciones de su banda "
     r"preferida. Cada aficionado produce una potencia sonora promedio de 1 mW. Si la distancia "
     r"promedio al centro del escenario es de 100 m, ¿cuál será la intensidad del sonido en ese "
     r"punto? ¿Cuál es su nivel de intensidad?",
     r"$P = 45\,000 \cdot 10^{-3}$ W $= 45$ W; $I = \frac{45}{4\pi (100)^2} \approx "
     r"\num{3,6}\times10^{-4}$ W/m²; $\beta = 10\log\frac{I}{10^{-12}} \approx \num{85,5}$ dB.",
     tema="intensidad del sonido", dificultad=3,
     notas="La guía da 900 W por aficionado, un valor irreal (un grito emite del orden de "
           "1 mW): daría 322 W/m² y 145 dB, más que un motor de reacción. Se cambió a 1 mW y "
           "se pidió también el nivel de intensidad.")
def _():
    P = 45000 * 1e-3 * u.watt
    I = P / (4 * math.pi * (100 * u.meter)**2)
    Iv = valor(I, u.watt / u.meter**2)
    assert aprox(Iv, 3.58e-4, 0.01)
    beta = 10 * math.log10(Iv / valor(I0, u.watt / u.meter**2))
    assert aprox(beta, 85.5, 0.005) and 60 < beta < 120


@num(74, PRO, "16a",
     r"El sonido de un disparo tiene una potencia de 1,5 W y llega a una persona con un nivel de "
     r"intensidad de 110 dB. Halla la intensidad del sonido.",
     r"$110 = 10\log\frac{I}{10^{-12}} \Rightarrow I = 10^{11}\cdot 10^{-12} = \num{0,1}$ W/m².",
     tema="intensidad del sonido")
def _():
    Iv = valor(I0, u.watt / u.meter**2) * 10**(110 / 10)
    assert aprox(Iv, 0.1)


@num(75, PRO, "16b",
     r"Con los datos anteriores (potencia 1,5 W, intensidad \num{0,1} W/m²), halla la distancia "
     r"entre la persona y el lugar del disparo.",
     r"$r = \sqrt{\frac{P}{4\pi I}} = \sqrt{\frac{\num{1,5}}{4\pi\cdot\num{0,1}}} \approx "
     r"\num{1,09}$ m.", tema="intensidad del sonido")
def _():
    r = sqrt(1.5 * u.watt / (4 * math.pi * 0.1 * u.watt / u.meter**2))
    assert aprox(valor(r, u.meter), 1.09, 0.005)


@num(76, PRO, "17",
     r"Dos tractomulas viajan en direcciones opuestas por la vía Bogotá–Cartagena y se acercan "
     r"una a la otra: una a 90 km/h y la otra a 50 km/h. Cuando están a 200 m, tocan la bocina "
     r"simultáneamente con una frecuencia de 900 Hz. ¿Qué frecuencia percibe cada conductor al "
     r"escuchar la bocina de la otra? Usa $v = 340$ m/s y "
     r"$f_o = f_f\dfrac{v + v_o}{v - v_f}$ (fuente y observador acercándose).",
     r"$90$ km/h $= 25$ m/s y $50$ km/h $\approx \num{13,9}$ m/s. El conductor a 90 km/h oye "
     r"$900\cdot\frac{340 + 25}{340 - \num{13,9}} \approx 1007$ Hz; el conductor a 50 km/h oye "
     r"$900\cdot\frac{340 + \num{13,9}}{340 - 25} \approx 1011$ Hz.", tema="efecto Doppler",
     dificultad=3,
     notas="La guía solo presenta fórmulas con fuente u observador en reposo; se da en el "
           "enunciado la fórmula combinada. Se precisó que las tractomulas se acercan (aún no se "
           "han cruzado); la distancia de 200 m no interviene.")
def _():
    v1 = valor(90 * u.kilometer / u.hour, u.meter / u.second)
    v2 = valor(50 * u.kilometer / u.hour, u.meter / u.second)
    assert aprox(v1, 25) and aprox(v2, 13.89, 0.001)
    oye1 = 900 * (340 + v1) / (340 - v2)
    oye2 = 900 * (340 + v2) / (340 - v1)
    assert aprox(oye1, 1007, 0.001) and aprox(oye2, 1011, 0.001)


@num(77, PRO, "18",
     r"Un automóvil con velocidad constante de 72 km/h se aproxima a un observador parado en el "
     r"andén. Si hace sonar la bocina con una frecuencia de 720 Hz y la velocidad del sonido es "
     r"340 m/s, ¿qué frecuencia percibe el observador?",
     r"$72$ km/h $= 20$ m/s; $f_o = \frac{v}{v - v_f} f_f = \frac{340}{320}\cdot 720 = 765$ Hz.",
     tema="efecto Doppler")
def _():
    vf_ = valor(72 * u.kilometer / u.hour, u.meter / u.second)
    assert aprox(vf_, 20)
    assert aprox(340 / (340 - vf_) * 720, 765, 1e-9)


@num(78, PRO, "19",
     r"Si una cuerda se acorta 15 cm, emite un sonido con frecuencia fundamental de 350 Hz, y si "
     r"se acorta 5 cm, emite un sonido de 120 Hz. ¿Cuál es la longitud de la cuerda?",
     r"Con la misma velocidad de propagación, $f(L - x)$ es constante: "
     r"$350(L - 15) = 120(L - 5) \Rightarrow 230L = 4650 \Rightarrow L \approx \num{20,2}$ cm.",
     tema="tubos sonoros", dificultad=3,
     notas="Los datos son coherentes (más acortada, más aguda), aunque la cuerda resultante es "
           "muy corta (20,2 cm).")
def _():
    L = symbols("L", positive=True)
    sol = float(nsolve(350 * (L - 15) - 120 * (L - 5), L, 20))
    assert aprox(sol, 20.2, 0.005) and sol > 15


@num(79, PRO, "20", r"Calcula el quinto armónico de un tubo abierto de \num{1,2} m de longitud "
     r"(v = 340 m/s).",
     r"$f_5 = \frac{5v}{2L} = \frac{5\cdot 340}{\num{2,4}} \approx \num{708,3}$ Hz.",
     tema="tubos sonoros")
def _():
    assert aprox(valor(5 * V / (2 * 1.2 * u.meter), u.hertz), 708.3, 0.001)


@num(80, PRO, "21", r"Halla el tercer armónico de un tubo cerrado de 30 cm de longitud "
     r"(v = 340 m/s).",
     r"En un tubo cerrado solo hay armónicos impares; el tercero es $n = 3$: "
     r"$f_3 = \frac{3v}{4L} = \frac{3\cdot 340}{\num{1,2}} = 850$ Hz.", tema="tubos sonoros",
     notas="Se toma «tercer armónico» como n = 3 (primer sobretono). La guía llama «segundo "
           "armónico» a 3λ/4; con ese conteo el «tercero» sería n = 5: 1416,7 Hz.")
def _():
    f3 = valor(3 * V / (4 * 0.30 * u.meter), u.hertz)
    assert aprox(f3, 850)


@num(81, PRO, "22a",
     r"Una varilla de hierro de \num{1,2} m de longitud tiene sus extremos fijos y se excitan en "
     r"ella ondas transversales estacionarias que se propagan a 5.130 m/s. Halla las frecuencias "
     r"de los cuatro primeros armónicos.",
     r"$f_n = \frac{nv}{2L} = n\cdot\num{2137,5}$ Hz: \num{2137,5} Hz, 4275 Hz, "
     r"\num{6412,5} Hz y 8550 Hz.", tema="ondas estacionarias",
     notas="La guía pide «la frecuencia fundamental de los cuatro primeros armónicos»; se "
           "piden las frecuencias de los cuatro primeros armónicos.")
def _():
    v, L = 5130 * u.meter / u.second, 1.2 * u.meter
    fs = [valor(n * v / (2 * L), u.hertz) for n in range(1, 5)]
    assert all(aprox(a, b) for a, b in zip(fs, [2137.5, 4275, 6412.5, 8550]))


@num(82, PRO, "22b",
     r"En la varilla anterior (\num{1,2} m, extremos fijos), calcula la longitud de onda de los "
     r"tres primeros armónicos.",
     r"$\lambda_n = \frac{2L}{n}$: \num{2,4} m, \num{1,2} m y \num{0,8} m.",
     tema="ondas estacionarias", dificultad=1)
def _():
    lams = [valor(2 * 1.2 * u.meter / n, u.meter) for n in (1, 2, 3)]
    assert all(aprox(a, b) for a, b in zip(lams, [2.4, 1.2, 0.8]))


manual(83, PRO, "22c",
       r"Realiza el dibujo representativo de la onda estacionaria en la varilla (extremos fijos) "
       r"para los tres primeros armónicos.",
       r"Primer armónico: nodos en los dos extremos y un vientre en el centro (media longitud de "
       r"onda). Segundo: tres nodos (extremos y centro) y dos vientres. Tercero: cuatro nodos "
       r"igualmente espaciados cada 40 cm y tres vientres.", tema="ondas estacionarias")


@num(84, PRO, "23a",
     r"La velocidad del sonido en el aire a 20 °C es de 340 m/s. ¿Cuál es la longitud de un tubo "
     r"cerrado cuya frecuencia fundamental corresponde a la nota la de 440 Hz?",
     r"$L = \frac{v}{4f_1} = \frac{340}{1760} \approx \num{0,193}$ m $\approx \num{19,3}$ cm.",
     tema="tubos sonoros",
     notas="El valor 340 m/s de la guía corresponde a 15 °C; a 20 °C su fórmula da 343 m/s. "
           "Se conserva 340 m/s.")
def _():
    assert aprox(valor(V / (4 * 440 * u.hertz), u.centimeter), 19.3, 0.005)


@num(85, PRO, "23b",
     r"¿Cuáles son las tres primeras frecuencias armónicas del tubo cerrado de fundamental "
     r"440 Hz?",
     r"Solo armónicos impares: 440 Hz, 1320 Hz y 2200 Hz.", tema="tubos sonoros", dificultad=1)
def _():
    L = V / (4 * 440 * u.hertz)
    fs = [valor(n * V / (4 * L), u.hertz) for n in (1, 3, 5)]
    assert all(aprox(a, b) for a, b in zip(fs, [440, 1320, 2200]))


@num(86, PRO, "23c",
     r"¿Cuál debería ser la longitud de un tubo abierto para producir un sonido con una "
     r"frecuencia fundamental de 440 Hz (v = 340 m/s)?",
     r"$L = \frac{v}{2f_1} = \frac{340}{880} \approx \num{0,386}$ m $\approx \num{38,6}$ cm.",
     tema="tubos sonoros")
def _():
    assert aprox(valor(V / (2 * 440 * u.hertz), u.centimeter), 38.6, 0.005)


@num(87, PRO, "23d",
     r"¿Cuáles son las tres primeras frecuencias armónicas del tubo abierto de fundamental "
     r"440 Hz?",
     r"Todos los armónicos: 440 Hz, 880 Hz y 1320 Hz.", tema="tubos sonoros", dificultad=1)
def _():
    L = V / (2 * 440 * u.hertz)
    fs = [valor(n * V / (2 * L), u.hertz) for n in (1, 2, 3)]
    assert all(aprox(a, b) for a, b in zip(fs, [440, 880, 1320]))


@num(88, PRO, "24",
     r"Un alambre de 60 cm se mantiene fijo en sus extremos A y B. Excitado con una frecuencia de "
     r"60 Hz, forma una onda estacionaria con 5 nodos. ¿Cuál es la velocidad de propagación de "
     r"la onda en el alambre?",
     r"5 nodos (contando los extremos) son 4 vientres: $n = 4$, $\lambda = \frac{2L}{4} = "
     r"\num{0,3}$ m y $v = \lambda f = \num{0,3}\cdot 60 = 18$ m/s.",
     tema="ondas estacionarias")
def _():
    lam = 2 * 0.6 * u.meter / (5 - 1)
    assert aprox(valor(lam * 60 * u.hertz, u.meter / u.second), 18)


@num(89, PRO, "25",
     r"La parte vibrante de una cuerda de una guitarra eléctrica tiene \num{1,2} m de longitud, "
     r"está sometida a una tensión de 1.800 N y tiene una densidad lineal de \num{0,02} kg/m. "
     r"Un músico produce vibraciones estacionarias en el modo fundamental. Calcula la velocidad "
     r"de las ondas en la cuerda y la frecuencia fundamental.",
     r"$v = \sqrt{F/\mu} = \sqrt{1800/\num{0,02}} = 300$ m/s; "
     r"$f_1 = \frac{v}{2L} = \frac{300}{\num{2,4}} = 125$ Hz.", tema="tubos sonoros",
     notas="En la guía el problema no tiene pregunta; se pide la velocidad y la frecuencia "
           "fundamental. (1,2 m y 1.800 N son valores exagerados para una guitarra real, "
           "~0,65 m y ~100 N, pero el resultado es un sonido audible.)")
def _():
    v = sqrt(1800 * u.newton / (0.02 * u.kilogram / u.meter))
    assert aprox(valor(v, u.meter / u.second), 300)
    assert aprox(valor(v / (2 * 1.2 * u.meter), u.hertz), 125)
