"""Banco de ejercicios — Física 11° — Óptica (naturaleza y velocidad de la luz, interferencia,
espejos, refracción).
Fuente: Guía de Apoyo «Fenómenos ondulatorios» grado 11 (Ciencias Naturales), Capítulo 4: óptica;
se lee en recursos/fisica/Guías pedagógicas Física/markdown/
11 - Guia_de_Apoyo_Fenomenos_ondulatorios_grado_11_fisica.md
Secciones: «Desarrolla tus competencias», «Actividades» y «Problemas» del capítulo 4.

Convenciones: espejos con la convención de la guía, 1/d_o + 1/d_i = 1/f y h_i/h_o = -d_i/d_o, con
distancias positivas del lado reflejante (f > 0 cóncavo, f < 0 convexo; d_i > 0 imagen real).
c = 3·10^8 m/s; año luz = c · (365,25 días).

Correcciones (detalle en «notas»): Actividades 1 — las viñetas sin letra se rotulan a–h en orden;
Problemas 13 — «objeto convexo» → «espejo convexo»; Problemas 11b y 11e — con f = 4 cm, «a 4 cm» y
«en el foco» son el mismo caso (se conserva cada literal y se advierte); Desarrolla 1b — el autor de
la teoría corpuscular (Newton) no está en la lista de autores.
No se omitió ningún literal (el capítulo no tiene práctica de laboratorio con preguntas).

Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/fisica/optica-11.py
"""
import math

from sympy import Rational, asin, deg, pi, sin, solve, symbols
from sympy.physics import units as u
from sympy.physics.units import convert_to

from ejercicios import ejercicio, ejercicio_manual

GUIA = "Guía de Apoyo Fenómenos ondulatorios 11°"
CAP = "Capítulo 4: óptica"
DTC = f"{GUIA}, {CAP}, Desarrolla tus competencias"
ACT = f"{GUIA}, {CAP}, Actividades"
PRO = f"{GUIA}, {CAP}, Problemas"
COMUN = dict(grados=[11], dba=["naturales-11-1"])

C = 3 * 10**8 * u.meter / u.second
ANO = Rational(36525, 100) * u.day
ANO_LUZ = C * ANO


def valor(q, unidad):
    return float(convert_to(q, unidad) / unidad)


def aprox(a, b, rel=0.01):
    return abs(a - b) <= rel * abs(b)


def opciones(*items):
    return r" \begin{opciones} " + " ".join(r"\item " + i for i in items) + r" \end{opciones}"


def manual(n, fuente, enunciado, respuesta, tema="óptica", tipo="conceptual", dificultad=1,
           notas=None):
    meta = dict(id=f"optica-11-{n:03d}", tema=tema, tipo=tipo, dificultad=dificultad,
                fuente=fuente, enunciado=enunciado, respuesta=respuesta, **COMUN)
    if notas:
        meta["notas"] = notas
    ejercicio_manual(**meta)


def vf(n, fuente, afirmacion, veredicto, justificacion, tema="óptica", notas=None):
    manual(n, fuente, r"Escribe V si la afirmación es verdadera o F si es falsa, y justifica: "
           + afirmacion, f"{veredicto}. {justificacion}", tema=tema, tipo="argumentacion",
           notas=notas)


def espejo(f, do):
    """Distancia de imagen (convención de la guía); None si el objeto está en el foco."""
    if do == f:
        return None
    return 1 / (Rational(1) / f - Rational(1) / do)


# =====================================================================
# Desarrolla tus competencias
# =====================================================================

AUTORES = (r"Relaciona la afirmación con su autor (Alhasén, Christian Huygens, Thomas Young, "
           r"James Maxwell, Jean Fresnel): ")
T_NAT = "naturaleza de la luz"
manual(1, f"{DTC} — 1a", AUTORES + "«Existe un medio llamado éter por donde se propaga la luz "
       "como una onda».", "Christian Huygens.", tema=T_NAT)
manual(2, f"{DTC} — 1b", AUTORES + "«La luz está compuesta por pequeñas partículas denominadas "
       "corpúsculos».", "Isaac Newton (teoría corpuscular); no aparece en la lista de autores.",
       tema=T_NAT, notas="La guía da seis afirmaciones y cinco autores: la teoría corpuscular es "
       "de Newton, que no está en la lista. Conviene añadir «Isaac Newton» a la lista.")
manual(3, f"{DTC} — 1c", AUTORES + "«La luz proviene del Sol, siendo los ojos receptores y no "
       "emisores».", "Alhasén (Ibn al-Haytham).", tema=T_NAT)
manual(4, f"{DTC} — 1d", AUTORES + "«Demostró de forma teórica la naturaleza ondulatoria de la "
       "luz».", "Jean Fresnel (teoría matemática de la difracción).", tema=T_NAT)
manual(5, f"{DTC} — 1e", AUTORES + "«La luz es un pequeño espectro de ondas electromagnéticas».",
       "James Maxwell.", tema=T_NAT)
manual(6, f"{DTC} — 1f", AUTORES + "«Comprobó la naturaleza ondulatoria de la luz haciendo "
       "experimentos sobre interferencia y difracción».", "Thomas Young (doble rendija, 1801).",
       tema=T_NAT)
manual(7, f"{DTC} — 2", r"El método para medir la velocidad de la luz en el que se determinó el "
       r"período de Ío, una de las lunas de Júpiter, midiendo el tiempo entre dos eclipses "
       r"sucesivos, fue realizado por:" + opciones("Louis Fizeau.", "Galileo Galilei.",
                                                   "Albert Michelson.", "Olaus Roemer."),
       "d. Olaus Roemer (1675).", tema=T_NAT, tipo="seleccion")
manual(8, f"{DTC} — 3", r"El fenómeno ondulatorio que producen los cristales que dejan pasar la "
       r"luz en ciertas direcciones de vibración y absorben las demás es:" + opciones(
           "Interferencia.", "Polarización.", "Difracción.", "Reflexión."),
       "b. Polarización.", tipo="seleccion")
manual(9, f"{DTC} — 4", r"Cuando miramos un objeto, ¿la luz sale de los ojos o entra en ellos? "
       r"¿Qué diferencia hay entre un objeto luminoso y un objeto iluminado? ¿Ambos emiten luz?",
       r"La luz entra en los ojos. Un objeto luminoso produce su propia luz (el Sol, un bombillo "
       r"encendido); un objeto iluminado solo refleja la luz que le llega de una fuente. Solo el "
       r"luminoso emite luz propia; el iluminado la devuelve (reflexión difusa) y por eso lo vemos.",
       tema=T_NAT)
FOTO = (r"Las primeras fotografías (heliografías) las hizo Niépce; luego Daguerre usó placas "
        r"cubiertas con yoduro de plata, sensible a la luz, y en el siglo XX se popularizó la "
        r"fotografía digital. ")
manual(10, f"{DTC} — 5a", FOTO + "¿Qué parte de la óptica está relacionada con la fotografía?",
       r"La óptica geométrica (formación de imágenes con lentes: la cámara es una cámara oscura "
       r"con lente convergente que forma una imagen real e invertida sobre el sensor o la "
       r"película); también la fotometría, que mide la cantidad de luz (exposición).")
manual(11, f"{DTC} — 5b", FOTO + "¿Por qué se dice que la fotografía es un excelente instrumento "
       "de documentación?", r"Porque registra de forma fiel y permanente la luz que llega de una "
       r"escena en un instante: conserva evidencia de lugares, personas y hechos que se pueden "
       r"revisar, comparar y compartir después.", tipo="argumentacion")
manual(12, f"{DTC} — 6", r"Realiza un cuadro comparativo entre una cámara fotográfica de película "
       r"y una cámara digital, con sus ventajas y desventajas.",
       r"Ambas tienen lente, diafragma y obturador y forman una imagen real e invertida. Película: "
       r"la imagen se registra químicamente (haluros de plata); hay que revelar, cada foto tiene "
       r"costo, número limitado de tomas; ventaja: gran rango de tonos y archivo físico duradero. "
       r"Digital: un sensor (CCD/CMOS) convierte la luz en señales eléctricas; ventajas: se ve la "
       r"foto al instante, se borra y edita, almacena miles de fotos sin costo por toma; "
       r"desventajas: depende de baterías y dispositivos, los archivos pueden perderse.",
       tipo="argumentacion")
manual(13, f"{DTC} — 7", r"Muchos jóvenes sufren enfermedades visuales, a veces por herencia y "
       r"otras por falta de cuidados básicos. ¿Qué recomendarías a tus compañeros para prevenirlas?",
       r"Respuesta abierta. Por ejemplo: descansar la vista (regla 20-20-20: cada 20 minutos mirar "
       r"a unos 6 m durante 20 s), buena iluminación al leer, no mirar el Sol ni punteros láser, "
       r"usar gafas con filtro UV al sol, mantener distancia de las pantallas y bajar su brillo, "
       r"y hacerse controles con el optómetra.", tipo="argumentacion")
manual(14, f"{DTC} — 8", r"¿Cómo se relacionan la física y la biología en el estudio del ojo "
       r"humano?", r"El ojo es un sistema óptico: la córnea y el cristalino actúan como una lente "
       r"convergente que forma en la retina una imagen real e invertida (óptica: refracción, "
       r"distancia focal, acomodación). La biología explica cómo los conos y bastones convierten "
       r"la luz en impulsos nerviosos y cómo el cerebro interpreta la imagen. Defectos como la "
       r"miopía o la hipermetropía se corrigen con lentes gracias a la física.",
       tipo="argumentacion")
manual(15, f"{DTC} — 9", r"¿Crees que la física ayuda en la solución de problemas médicos? "
       r"Explica tu respuesta.", r"Sí. Ejemplos: lentes y cirugía láser para corregir la visión, "
       r"endoscopios de fibra óptica (reflexión total), rayos X y tomografía, ecografía "
       r"(ultrasonido), resonancia magnética, radioterapia y marcapasos.", tipo="argumentacion")
VIDRIO = (r"Cuando de noche miras a través del vidrio de una ventana hacia el exterior, a veces ves "
          r"una imagen doble de ti mismo. ")
manual(16, f"{DTC} — 10a", VIDRIO + "¿Qué fenómeno de la luz ocurre?",
       r"Reflexión (parcial) de la luz en el vidrio; como afuera está oscuro, la luz reflejada "
       r"desde el cuarto iluminado predomina sobre la que llega de afuera.", tema="espejos")
manual(17, f"{DTC} — 10b", VIDRIO + "¿Cuántos medios interactúan?",
       r"Tres: el aire del interior, el vidrio y el aire del exterior (aire–vidrio–aire).",
       tema="espejos")
manual(18, f"{DTC} — 10c", VIDRIO + "¿El vidrio presenta doble interfaz de medios?",
       r"Sí: la cara interior (aire–vidrio) y la cara exterior (vidrio–aire).", tema="espejos")
manual(19, f"{DTC} — 10d", VIDRIO + "¿Cada interfaz genera una imagen?",
       r"Sí: cada cara refleja parte de la luz y actúa como un espejo plano; las dos imágenes "
       r"están ligeramente desplazadas (según el grosor del vidrio), por eso se ve doble.",
       tema="espejos")
manual(20, f"{DTC} — 11", r"En una noche lluviosa, las irregularidades de la carretera se llenan de "
       r"agua y la luz experimenta reflexión especular. Explica en qué consiste este fenómeno.",
       r"En la reflexión especular la superficie es lisa (aquí, la capa de agua tapa las "
       r"irregularidades): todos los rayos paralelos que llegan se reflejan paralelos, con ángulo "
       r"de reflexión igual al de incidencia, como en un espejo. Por eso la luz de los faros se "
       r"refleja lejos del conductor que la emite y la vía se ve oscura, con reflejos que "
       r"deslumbran a los demás; en la vía seca la reflexión es difusa (en todas direcciones).",
       tema="espejos")
manual(21, f"{DTC} — 12", r"Si la imagen producida por un espejo esférico es real, ¿necesariamente "
       r"es invertida con respecto al objeto?", r"Sí. Con $h_i/h_o = -d_i/d_o$: si la imagen es "
       r"real, $d_i > 0$, y como el objeto es real ($d_o > 0$), el aumento es negativo: la imagen "
       r"es invertida.", tema="espejos", tipo="argumentacion")

# =====================================================================
# Actividades
# =====================================================================

NOTA_VINETAS = ("En la guía las afirmaciones de este punto son viñetas sin letra; se rotulan "
                "a, b, c… en el orden en que aparecen.")
vf(22, f"{ACT} — 1a", r"Albert Einstein planteaba que la velocidad de la luz es la máxima que "
   r"puede existir en el universo y es $3\times10^{8}$ m/s.", "V",
   r"Es un postulado de la relatividad: nada con masa alcanza la velocidad de la luz en el "
   r"vacío, $c = \num{299792458}$ m/s $\approx 3\times10^{8}$ m/s.", tema=T_NAT, notas=NOTA_VINETAS)
vf(23, f"{ACT} — 1b", r"En el modelo electromagnético la luz se comporta como una corriente de "
   r"partículas en forma rectilínea a gran velocidad.", "F",
   r"Esa es la teoría corpuscular (Newton). En el modelo electromagnético (Maxwell) la luz es una "
   r"onda formada por campos eléctrico y magnético que oscilan perpendiculares entre sí.",
   tema=T_NAT, notas=NOTA_VINETAS)
vf(24, f"{ACT} — 1c", r"Louis Fizeau utilizó una rueda dentada que giraba y por allí cruzaba un "
   r"haz de luz, el cual recorría diferentes caminos y regresaba al observador para calcular la "
   r"velocidad de la luz.", "V",
   r"La luz pasaba por una ranura, se reflejaba en un espejo a \num{8,63} km y volvía; con la "
   r"velocidad de giro para la cual el haz regresaba por la ranura siguiente obtuvo "
   r"$c \approx \num{3,13}\times10^{8}$ m/s. (La luz hace el mismo camino de ida y vuelta.)",
   tema=T_NAT, notas=NOTA_VINETAS)
vf(25, f"{ACT} — 1d", r"La longitud de onda de la luz según el espectro electromagnético es del "
   r"orden de $10^{-11}$ m.", "F",
   r"La luz visible va de unos 400 nm a 700 nm, es decir, del orden de $10^{-7}$ m; "
   r"$10^{-11}$ m corresponde a rayos X o gamma.", tema=T_NAT, notas=NOTA_VINETAS)
vf(26, f"{ACT} — 1e", r"En el experimento de la doble rendija el patrón de interferencia se "
   r"observa mediante franjas oscuras y claras.", "V",
   r"Las franjas brillantes son interferencia constructiva ($d\sen\theta = n\lambda$) y las "
   r"oscuras, destructiva.", notas=NOTA_VINETAS)
vf(27, f"{ACT} — 1f", r"La distancia entre dos líneas consecutivas de interferencia constructiva "
   r"depende de la longitud de onda de la luz utilizada.", "V",
   r"La separación entre franjas brillantes es $\Delta y = \dfrac{\lambda L}{d}$: es "
   r"proporcional a $\lambda$.", notas=NOTA_VINETAS)
vf(28, f"{ACT} — 1g", r"El flujo luminoso a una determinada distancia de la fuente se distribuye en "
   r"la superficie de una esfera con centro en un punto diferente a la fuente luminosa.", "F",
   r"Se distribuye en una esfera centrada en la fuente: $E = \dfrac{F}{4\pi r^2}$.",
   notas=NOTA_VINETAS)
vf(29, f"{ACT} — 1h", r"Una onda de color rojo tiene una longitud de onda de 690 nm.", "V",
   r"La luz roja tiene longitudes de onda entre unos 620 nm y 750 nm.", notas=NOTA_VINETAS)
manual(30, f"{ACT} — 2", r"¿Qué característica de la luz pone de manifiesto el efecto "
       r"fotoeléctrico?" + opciones("Su carácter corpuscular.", "Su carácter ondulatorio.",
                                    "Su carácter electromagnético.",
                                    "Su dualidad onda-partícula."),
       r"a. Su carácter corpuscular: la luz llega en paquetes (fotones) de energía $E = hf$; "
       r"solo arranca electrones si la frecuencia supera un umbral, sin importar la intensidad.",
       tema=T_NAT, tipo="seleccion", notas="Junto con la interferencia, el efecto fotoeléctrico "
       "sustenta la dualidad (d), pero lo que él muestra por sí solo es el carácter corpuscular.")
manual(31, f"{ACT} — 3", r"Explica los tres modelos de la naturaleza de la luz.",
       r"Corpuscular (Newton): la luz son partículas que viajan en línea recta; explica la "
       r"reflexión y la propagación rectilínea. Ondulatorio (Huygens, Young, Fresnel): la luz es "
       r"una onda; explica la interferencia y la difracción. Electromagnético (Maxwell): la luz es "
       r"una onda electromagnética que viaja en el vacío a $c$ y es una pequeña parte del espectro. "
       r"Hoy se acepta la dualidad onda-partícula (fotones, Einstein).", tema=T_NAT)
manual(32, f"{ACT} — 4", r"¿Cómo podemos medir velocidades extremadamente grandes como la de la "
       r"luz?", r"Usando distancias muy grandes o tiempos muy pequeños medidos indirectamente: "
       r"con fenómenos astronómicos (Roemer, eclipses de Ío), con ruedas dentadas o espejos "
       r"giratorios que convierten un tiempo diminuto en un ángulo de giro (Fizeau, Foucault, "
       r"Michelson), y hoy con láseres y relojes electrónicos.", tema=T_NAT)
manual(33, f"{ACT} — 5", r"¿Qué características tiene la luz monocromática en lo que se refiere a "
       r"la longitud de onda?", r"Tiene una sola longitud de onda (una sola frecuencia), es "
       r"decir, un solo color; por ejemplo, la luz de un láser.", tema=T_NAT)
manual(34, f"{ACT} — 6", r"¿A qué se llama interferencia constructiva? ¿Qué es la interferencia "
       r"destructiva? ¿En qué fenómenos cotidianos se puede observar la interferencia de ondas "
       r"luminosas?", r"Constructiva: dos ondas llegan en fase (diferencia de camino "
       r"$n\lambda$) y sus amplitudes se suman: franja brillante. Destructiva: llegan en "
       r"oposición de fase (diferencia $(n + \tfrac12)\lambda$) y se anulan: franja oscura. Se "
       r"observa en los colores de las pompas de jabón, las manchas de aceite en el agua y el "
       r"reflejo de un CD o DVD.")
manual(35, f"{ACT} — 7", r"Explica si se obtienen franjas de interferencia con rendijas "
       r"extremadamente anchas. ¿Qué relación tiene la longitud de onda con este hecho?",
       r"No se obtienen franjas apreciables: para que cada rendija difracte la luz y los haces se "
       r"superpongan, su ancho y su separación deben ser comparables con la longitud de onda "
       r"($\sim 10^{-7}$ m). Además $\Delta y = \lambda L / d$: si $d$ es muy grande, las franjas "
       r"quedan tan juntas que no se distinguen.", tipo="argumentacion")
vf(36, f"{ACT} — 8a", r"Un rayo de luz es una línea imaginaria que se traza en dirección "
   r"perpendicular a la onda.", "V",
   r"El rayo indica la dirección de propagación y es perpendicular a los frentes de onda.",
   tema="espejos", notas="«Perpendicular a la onda» se entiende como perpendicular al frente "
   "de onda.")
vf(37, f"{ACT} — 8b", r"Una onda reflejada es aquella que viaja por el mismo medio de la onda "
   r"incidente después de alcanzar la frontera entre dos medios.", "V",
   r"La onda reflejada regresa al mismo medio por el que llegó.", tema="espejos")
vf(38, f"{ACT} — 8c", r"La normal es una recta perpendicular a la línea que divide los dos medios.",
   "V", r"Se traza perpendicular a la superficie de separación en el punto de incidencia, y los "
   r"ángulos se miden desde ella.", tema="espejos")
vf(39, f"{ACT} — 8d", r"En los espejos planos el ángulo de incidencia es igual al ángulo de "
   r"reflexión.", "V", r"Es la ley de la reflexión (se cumple también en los espejos curvos, "
   r"respecto a la normal en cada punto).", tema="espejos")
vf(40, f"{ACT} — 8e", r"En los espejos convexos la luz incide por la parte interna de la "
   r"superficie esférica.", "F", r"En el espejo convexo la cara reflejante es la exterior de "
   r"la esfera; la luz incide por la parte interna en el espejo cóncavo.", tema="espejos")
vf(41, f"{ACT} — 8f", r"El foco está a una distancia equivalente al doble del radio de curvatura "
   r"de un espejo esférico.", "F", r"Es al revés: la distancia focal es la mitad del radio, "
   r"$f = R/2$.", tema="espejos")
vf(42, f"{ACT} — 8g", r"En un espejo esférico una imagen derecha es aquella que está por encima "
   r"del eje óptico.", "F", r"Una imagen es derecha si tiene la misma orientación que el objeto "
   r"(aumento positivo); si el objeto estuviera por debajo del eje, su imagen derecha también "
   r"estaría por debajo. Por encima del eje significa $h_i > 0$ en la convención de signos.",
   tema="espejos")
PAR = r"Nombra diferencias entre los conceptos: "
manual(43, f"{ACT} — 9a", PAR + "ángulo de incidencia y ángulo de reflexión.",
       r"El de incidencia es el que forma el rayo que llega con la normal; el de reflexión, el "
       r"que forma el rayo reflejado con la normal. Son iguales, pero corresponden a rayos "
       r"distintos, a uno y otro lado de la normal.", tema="espejos")
manual(44, f"{ACT} — 9b", PAR + "un haz de luz y un rayo de luz.",
       r"Un rayo es una línea imaginaria que indica la dirección de propagación; un haz es un "
       r"conjunto de rayos (paralelo, convergente o divergente) y sí es real.", tema="espejos")
manual(45, f"{ACT} — 9c", PAR + "espejos planos y espejos esféricos.",
       r"El plano tiene superficie plana y da siempre imágenes virtuales, derechas, del mismo "
       r"tamaño y simétricas; el esférico es parte de una esfera, tiene foco y centro de "
       r"curvatura, y sus imágenes pueden ser reales o virtuales, mayores o menores.",
       tema="espejos")
manual(46, f"{ACT} — 9d", PAR + "espejo cóncavo y espejo convexo.",
       r"Cóncavo: refleja por la cara interna, converge los rayos (foco real, $f > 0$) y da "
       r"imágenes reales o virtuales según la posición del objeto. Convexo: refleja por la cara "
       r"externa, diverge los rayos (foco virtual, $f < 0$) y da siempre imágenes virtuales, "
       r"derechas y menores.", tema="espejos")
manual(47, f"{ACT} — 9e", PAR + "radio de curvatura y centro de curvatura.",
       r"El centro de curvatura es un punto: el centro de la esfera de la que forma parte el "
       r"espejo; el radio de curvatura es una distancia: la del centro de curvatura al espejo.",
       tema="espejos")
manual(48, f"{ACT} — 9f", PAR + "imagen real e imagen virtual.",
       r"La real se forma donde los rayos reflejados se cortan de verdad y se puede proyectar en "
       r"una pantalla (delante del espejo); la virtual se forma con las prolongaciones de los "
       r"rayos, detrás del espejo, y no se puede proyectar.", tema="espejos")
manual(49, f"{ACT} — 10", r"Una imagen virtual es aquella que:" + opciones(
    "Se forma invertida en el espejo.", "Se forma por fuera del espejo.",
    "Se forma en el interior del espejo.", "Es opaca."),
    r"c. Se forma «en el interior» del espejo, es decir, detrás de él, con las prolongaciones de "
    r"los rayos reflejados.", tema="espejos", tipo="seleccion")
manual(50, f"{ACT} — 11", r"En la reflexión de la luz:" + opciones(
    "El ángulo de incidencia es mayor que el ángulo de reflexión.",
    "El ángulo de reflexión es mayor que el ángulo de incidencia.",
    "El ángulo de incidencia es igual al ángulo de reflexión.", "Los ángulos son despreciables."),
    "c. El ángulo de incidencia es igual al ángulo de reflexión.", tema="espejos",
    tipo="seleccion")
manual(51, f"{ACT} — 12", r"En los espejos se cumple que:" + opciones(
    "La distancia focal siempre es negativa.", "Las imágenes reales están delante del espejo.",
    "La distancia del objeto siempre es positiva.",
    "Las imágenes generadas pueden ser reales o virtuales."),
    r"d. Las imágenes pueden ser reales o virtuales. (La a es falsa: $f > 0$ en los cóncavos.)",
    tema="espejos", tipo="seleccion",
    notas="Pregunta ambigua: con la convención de la guía, b (las imágenes reales están delante "
          "del espejo) y c (para objetos reales, d_o > 0) también son ciertas. Se da d como la "
          "más general; conviene reformular las opciones b y c antes de usarla.")
manual(52, f"{ACT} — 13", r"¿La imagen producida por un espejo plano siempre es virtual? Explica "
       r"tu respuesta.", r"Sí (para objetos reales): los rayos reflejados divergen y solo sus "
       r"prolongaciones se cortan detrás del espejo, a la misma distancia que el objeto está "
       r"delante; esa imagen no se puede proyectar.", tema="espejos", tipo="argumentacion")
manual(53, f"{ACT} — 14", r"¿Los espejos convexos siempre generan imágenes reales para cualquier "
       r"posición del objeto?", r"No: es al contrario. Un espejo convexo da siempre imágenes "
       r"virtuales, derechas y menores que el objeto, porque con $f < 0$ y $d_o > 0$ la ecuación "
       r"$\frac{1}{d_i} = \frac{1}{f} - \frac{1}{d_o}$ da siempre $d_i < 0$.", tema="espejos",
       tipo="argumentacion")
manual(54, f"{ACT} — 15", r"En los parqueaderos, para revisar la parte inferior de los vehículos, "
       r"se usan espejos convexos. ¿Por qué crees que son útiles para este trabajo?",
       r"Porque el espejo convexo tiene un campo visual amplio: muestra imágenes derechas y "
       r"reducidas de una zona grande, así que con un espejo pequeño se ve casi todo el bajo del "
       r"vehículo.", tema="espejos", tipo="argumentacion")
manual(55, f"{ACT} — 16", r"¿Cuántas imágenes completas se generan con dos espejos planos "
       r"perpendiculares entre sí?", r"Tres: $n = \dfrac{360^\circ}{90^\circ} - 1 = 3$ (una en "
       r"cada espejo y una tercera por doble reflexión).", tema="espejos")
manual(56, f"{ACT} — 17", r"Si te colocas frente a un espejo plano, tu lado izquierdo se refleja al "
       r"lado derecho de tu imagen. ¿Es correcto afirmar que el espejo plano invierte la imagen?",
       r"No en el sentido de «invertida» (arriba–abajo): la imagen es derecha. Lo que invierte es "
       r"la dirección perpendicular al espejo (adelante–atrás); por eso la imagen es simétrica "
       r"(«reversión»): tu mano izquierda queda frente a la mano de la imagen que parece la "
       r"derecha.", tema="espejos", tipo="argumentacion")

# =====================================================================
# Problemas
# =====================================================================


@ejercicio(id="optica-11-057", tema=T_NAT, tipo="calculo", dificultad=1, fuente=f"{PRO} — 1",
           enunciado=r"Calcula la longitud de onda de una radiación electromagnética cuya "
                     r"frecuencia es 100 MHz.",
           respuesta=r"$\lambda = \dfrac{c}{f} = \dfrac{3\times10^{8}\ \text{m/s}}{10^{8}\ "
                     r"\text{Hz}} = 3$ m (onda de radio FM).", **COMUN)
def _():
    lam = C / (100 * 10**6 * u.hertz)
    assert valor(lam, u.meter) == 3


@ejercicio(id="optica-11-058", tema=T_NAT, tipo="calculo", dificultad=2, fuente=f"{PRO} — 2a",
           enunciado=r"La distancia entre cuerpos celestes muy lejanos se expresa en años luz "
                     r"(distancia que recorre la luz en un año). Si la luz de una estrella tarda "
                     r"10 años en llegar a la Tierra, ¿qué distancia recorre en ese tiempo?",
           respuesta=r"10 años luz: $d = c\,t = (3\times10^{8}\ \text{m/s})(10 \cdot "
                     r"\num{3,156}\times10^{7}\ \text{s}) \approx \num{9,47}\times10^{16}$ m.",
           notas="Año de 365,25 días = 3,156·10^7 s.", **COMUN)
def _():
    assert aprox(valor(10 * ANO_LUZ, u.meter), 9.47e16)
    assert aprox(valor(ANO, u.second), 3.156e7, 0.001)


manual(59, f"{PRO} — 2b", r"La luz de una estrella tarda 10 años en llegar a la Tierra. ¿Podríamos "
       r"afirmar que la estrella sigue existiendo si la observamos desde la Tierra?",
       r"No con certeza: vemos la luz que la estrella emitió hace 10 años, es decir, cómo era "
       r"entonces. Pudo haber cambiado o desaparecido después y no lo sabríamos hasta dentro de "
       r"10 años.", tema=T_NAT, tipo="argumentacion")


@ejercicio(id="optica-11-060", tema=T_NAT, tipo="calculo", dificultad=1, fuente=f"{PRO} — 3",
           enunciado=r"¿Cuánto tiempo, en segundos, tarda la luz del Sol en llegar a la Tierra, si "
                     r"la distancia promedio entre ellos es de 150 millones de kilómetros?",
           respuesta=r"$t = \dfrac{d}{c} = \dfrac{\num{1,5}\times10^{11}\ \text{m}}{3\times10^{8}"
                     r"\ \text{m/s}} = 500$ s (unos 8 min 20 s).", **COMUN)
def _():
    t = 150 * 10**6 * u.kilometer / C
    assert valor(t, u.second) == 500


@ejercicio(id="optica-11-061", tema=T_NAT, tipo="calculo", dificultad=1, fuente=f"{PRO} — 4a",
           enunciado=r"La estrella Alfa Centauri se encuentra a \num{4,3} años luz del sistema "
                     r"solar. Expresa la distancia en unidades del Sistema Internacional.",
           respuesta=r"$d = \num{4,3} \cdot \num{9,47}\times10^{15}\ \text{m} \approx "
                     r"\num{4,07}\times10^{16}$ m.", notas="Año de 365,25 días.", **COMUN)
def _():
    assert aprox(valor(Rational(43, 10) * ANO_LUZ, u.meter), 4.07e16)


@ejercicio(id="optica-11-062", tema=T_NAT, tipo="calculo", dificultad=2, fuente=f"{PRO} — 4b",
           enunciado=r"Alfa Centauri está a \num{4,3} años luz. Si una nave espacial viajara a diez "
                     r"veces la velocidad del sonido (340 m/s), ¿cuánto tardaría en recorrer esa "
                     r"distancia?",
           respuesta=r"$v = 3400$ m/s; $t = \dfrac{\num{4,07}\times10^{16}\ \text{m}}{3400\ "
                     r"\text{m/s}} \approx \num{1,20}\times10^{13}$ s $\approx$ \num{379000} "
                     r"años.", notas="Se toma v_sonido = 340 m/s (la guía no la da).", **COMUN)
def _():
    t = Rational(43, 10) * ANO_LUZ / (10 * 340 * u.meter / u.second)
    assert aprox(valor(t, u.second), 1.20e13)
    assert aprox(valor(t, ANO), 379000)


@ejercicio(id="optica-11-063", tema=T_NAT, tipo="calculo", dificultad=1, fuente=f"{PRO} — 5a",
           enunciado=r"Una estrella se encuentra a 500 años luz de la Tierra. ¿Cuánto tiempo "
                     r"tarda su luz en llegar a la Tierra?",
           respuesta=r"500 años (por definición de año luz): unos $\num{1,58}\times10^{10}$ s.",
           **COMUN)
def _():
    t = 500 * ANO_LUZ / C
    assert valor(t, ANO) == 500
    assert aprox(valor(t, u.second), 1.58e10)


@ejercicio(id="optica-11-064", tema=T_NAT, tipo="calculo", dificultad=1, fuente=f"{PRO} — 5b",
           enunciado=r"Una estrella se encuentra a 500 años luz de la Tierra. ¿Cuál es la "
                     r"distancia, en kilómetros, hasta la Tierra?",
           respuesta=r"$d = 500 \cdot \num{9,47}\times10^{12}\ \text{km} \approx "
                     r"\num{4,73}\times10^{15}$ km.", notas="Año de 365,25 días.", **COMUN)
def _():
    assert aprox(valor(500 * ANO_LUZ, u.kilometer), 4.73e15)


@ejercicio(id="optica-11-065", tema=T_NAT, tipo="calculo", dificultad=1, fuente=f"{PRO} — 6",
           enunciado=r"La luz que proviene de una estrella recorre \num{4,6} años luz para llegar a "
                     r"la Tierra. ¿A qué distancia, en metros, se encuentra la estrella?",
           respuesta=r"$d = \num{4,6} \cdot \num{9,47}\times10^{15}\ \text{m} \approx "
                     r"\num{4,35}\times10^{16}$ m.",
           notas="Se pide la distancia en metros (la guía no dice en qué unidad).", **COMUN)
def _():
    assert aprox(valor(Rational(46, 10) * ANO_LUZ, u.meter), 4.35e16)


@ejercicio(id="optica-11-066", tema=T_NAT, tipo="calculo", dificultad=1, fuente=f"{PRO} — 7",
           enunciado=r"Los astrónomos descubren un sistema solar semejante al nuestro en torno a "
                     r"la estrella Vega, situada a 26 años luz de la Tierra. ¿Cuál es la distancia, "
                     r"en metros, de Vega a la Tierra?",
           respuesta=r"$d = 26 \cdot \num{9,47}\times10^{15}\ \text{m} \approx "
                     r"\num{2,46}\times10^{17}$ m.", **COMUN)
def _():
    assert aprox(valor(26 * ANO_LUZ, u.meter), 2.46e17)


EMISORA = r"Una emisora de radio transmite a 93 MHz. "


@ejercicio(id="optica-11-067", tema=T_NAT, tipo="calculo", dificultad=1, fuente=f"{PRO} — 8a",
           enunciado=EMISORA + r"¿Cuál es la velocidad de propagación de sus ondas?",
           respuesta=r"Es una onda electromagnética: viaja a la velocidad de la luz, "
                     r"$c = 3\times10^{8}$ m/s, sin importar su frecuencia.", **COMUN)
def _():
    assert aprox(valor(u.speed_of_light, u.meter / u.second), 3e8, 0.001)


@ejercicio(id="optica-11-068", tema=T_NAT, tipo="calculo", dificultad=1, fuente=f"{PRO} — 8b",
           enunciado=EMISORA + r"Expresa su frecuencia en Hz.",
           respuesta=r"$f = 93\times10^{6}$ Hz $= \num{9,3}\times10^{7}$ Hz.", **COMUN)
def _():
    assert 93 * 10**6 == 9.3e7


@ejercicio(id="optica-11-069", tema=T_NAT, tipo="calculo", dificultad=1, fuente=f"{PRO} — 8c",
           enunciado=EMISORA + r"¿Cuál es su período?",
           respuesta=r"$T = \dfrac{1}{f} = \dfrac{1}{\num{9,3}\times10^{7}\ \text{Hz}} \approx "
                     r"\num{1,08}\times10^{-8}$ s.", **COMUN)
def _():
    T = 1 / (93 * 10**6 * u.hertz)
    assert aprox(valor(T, u.second), 1.075e-8, 0.001)


@ejercicio(id="optica-11-070", tema=T_NAT, tipo="calculo", dificultad=1, fuente=f"{PRO} — 9a",
           enunciado=r"La distancia entre la Tierra y la Luna es de \num{384000} km. ¿Cuánto tiempo "
                     r"tardaría en llegar una nave que viaja a \num{1000} km/h?",
           respuesta=r"$t = \dfrac{\num{384000}\ \text{km}}{\num{1000}\ \text{km/h}} = 384$ h "
                     r"$= 16$ días.", **COMUN)
def _():
    t = 384000 * u.kilometer / (1000 * u.kilometer / u.hour)
    assert valor(t, u.hour) == 384 and valor(t, u.day) == 16


@ejercicio(id="optica-11-071", tema=T_NAT, tipo="calculo", dificultad=1, fuente=f"{PRO} — 9b",
           enunciado=r"La distancia entre la Tierra y la Luna es de \num{384000} km. ¿Qué tiempo "
                     r"emplea la luz en el mismo viaje?",
           respuesta=r"$t = \dfrac{\num{3,84}\times10^{8}\ \text{m}}{3\times10^{8}\ \text{m/s}} = "
                     r"\num{1,28}$ s.", **COMUN)
def _():
    assert aprox(valor(384000 * u.kilometer / C, u.second), 1.28, 1e-9)


@ejercicio(id="optica-11-072", tema="interferencia de la luz", tipo="calculo", dificultad=2,
           fuente=f"{PRO} — 10",
           enunciado=r"Dos rendijas de Young están separadas \num{0,04} mm y distan 1 m de una "
                     r"pantalla. Si la franja brillante de segundo orden ($n = 2$) está a 3 cm del "
                     r"máximo central y la luz es monocromática, determina su longitud de onda.",
           respuesta=r"$y = \dfrac{\lambda L}{d}\,n \Rightarrow \lambda = \dfrac{y\,d}{n\,L} = "
                     r"\dfrac{(\num{0,03})(4\times10^{-5})}{2 \cdot 1}\ \text{m} = "
                     r"6\times10^{-7}$ m $= 600$ nm (luz naranja).", **COMUN)
def _():
    y, d, L = 3 * u.centimeter, Rational(4, 100) * u.millimeter, 1 * u.meter
    lam = y * d / (2 * L)
    assert aprox(valor(lam, u.nanometer), 600, 1e-9)
    assert 400 < valor(lam, u.nanometer) < 700      # es luz visible


# ---------- Problema 11: espejo cóncavo, f = 4 cm, objeto de 1 cm ----------

E11 = (r"Un espejo cóncavo tiene distancia focal de 4 cm. Determina gráficamente (con los rayos "
       r"principales) y por medio de ecuaciones la posición y el tamaño de la imagen de un objeto "
       r"de 1 cm de altura, y di si es real o virtual, derecha o invertida, mayor o menor que el "
       r"objeto, si el objeto se coloca ")
CONV = r" (Convención: distancias positivas del lado reflejante.)"
NOTA_FOCO = ("Con f = 4 cm, los literales «a 4 cm del espejo» (11b) y «en el foco» (11e) son el "
             "mismo caso, igual que «a 8 cm» (11a) y «en el centro de curvatura» (11d). Se "
             "conservan los literales; conviene cambiar uno de cada par (p. ej. 11b a 2 cm).")


@ejercicio(id="optica-11-073", tema="espejos", tipo="calculo", dificultad=2, fuente=f"{PRO} — 11a",
           enunciado=E11 + "a 8 cm del espejo.",
           respuesta=r"$\frac{1}{d_i} = \frac14 - \frac18 = \frac18 \Rightarrow d_i = 8$ cm; "
                     r"$h_i = -\frac{d_i}{d_o}h_o = -1$ cm. Imagen real, invertida y del mismo "
                     r"tamaño, en el centro de curvatura." + CONV, notas=NOTA_FOCO, **COMUN)
def _():
    di = espejo(4, 8)
    assert di == 8 and -di / 8 * 1 == -1


@ejercicio(id="optica-11-074", tema="espejos", tipo="calculo", dificultad=2, fuente=f"{PRO} — 11b",
           enunciado=E11 + "a 4 cm del espejo.",
           respuesta=r"El objeto está en el foco: $\frac{1}{d_i} = \frac14 - \frac14 = 0$; los "
                     r"rayos reflejados salen paralelos y no se forma imagen (se forma «en el "
                     r"infinito»).", notas=NOTA_FOCO, **COMUN)
def _():
    assert espejo(4, 4) is None
    di = symbols("d_i")
    assert solve(1 / di + Rational(1, 4) - Rational(1, 4), di) == []


@ejercicio(id="optica-11-075", tema="espejos", tipo="calculo", dificultad=2, fuente=f"{PRO} — 11c",
           enunciado=E11 + "a 10 cm del espejo.",
           respuesta=r"$\frac{1}{d_i} = \frac14 - \frac1{10} = \frac{3}{20} \Rightarrow d_i = "
                     r"\frac{20}{3} \approx \num{6,67}$ cm; $h_i = -\frac{20/3}{10}\cdot 1 = "
                     r"-\frac23 \approx -\num{0,67}$ cm. Imagen real, invertida y menor, entre el "
                     r"foco y el centro de curvatura." + CONV, **COMUN)
def _():
    di = espejo(4, 10)
    assert di == Rational(20, 3) and -di / 10 == Rational(-2, 3)


@ejercicio(id="optica-11-076", tema="espejos", tipo="calculo", dificultad=2, fuente=f"{PRO} — 11d",
           enunciado=E11 + "en el centro de curvatura.",
           respuesta=r"$R = 2f = 8$ cm, así que $d_o = 8$ cm: $d_i = 8$ cm y $h_i = -1$ cm. Imagen "
                     r"real, invertida, del mismo tamaño, en el centro de curvatura." + CONV,
           notas=NOTA_FOCO, **COMUN)
def _():
    R = 2 * 4
    di = espejo(4, R)
    assert di == R and -di / R == -1


@ejercicio(id="optica-11-077", tema="espejos", tipo="calculo", dificultad=2, fuente=f"{PRO} — 11e",
           enunciado=E11 + "en el foco.",
           respuesta=r"$d_o = f = 4$ cm: los rayos reflejados salen paralelos al eje y no se forma "
                     r"imagen (está «en el infinito»).", notas=NOTA_FOCO, **COMUN)
def _():
    assert espejo(4, 4) is None


E12 = (r"Se coloca un objeto a 5 cm del vértice de un espejo cóncavo cuyo radio de curvatura es "
       r"24 cm. ")


@ejercicio(id="optica-11-078", tema="espejos", tipo="calculo", dificultad=2, fuente=f"{PRO} — 12a",
           enunciado=E12 + "¿A qué distancia del espejo se forma la imagen?",
           respuesta=r"$f = R/2 = 12$ cm; $\frac{1}{d_i} = \frac1{12} - \frac15 = -\frac{7}{60} "
                     r"\Rightarrow d_i = -\frac{60}{7} \approx -\num{8,57}$ cm: a \num{8,57} cm "
                     r"detrás del espejo." + CONV, **COMUN)
def _():
    assert espejo(12, 5) == Rational(-60, 7)


@ejercicio(id="optica-11-079", tema="espejos", tipo="calculo", dificultad=2, fuente=f"{PRO} — 12b",
           enunciado=E12 + "¿Qué tipo de imagen se forma?",
           respuesta=r"Virtual ($d_i < 0$), derecha y mayor: aumento $-\frac{d_i}{d_o} = "
                     r"\frac{12}{7} \approx \num{1,71}$ (el objeto está entre el foco y el espejo, "
                     r"como en un espejo de maquillaje).", **COMUN)
def _():
    di = espejo(12, 5)
    m = -di / 5
    assert di < 0 and m == Rational(12, 7) and m > 1


@ejercicio(id="optica-11-080", tema="espejos", tipo="calculo", dificultad=3, fuente=f"{PRO} — 13",
           enunciado=r"¿A qué distancia de un espejo convexo de distancia focal 30 cm se debe "
                     r"colocar un objeto de 8 cm para obtener una imagen de 4 cm?",
           respuesta=r"En el convexo $f = -30$ cm y la imagen es derecha: $\frac{h_i}{h_o} = "
                     r"\frac12 = -\frac{d_i}{d_o} \Rightarrow d_i = -\frac{d_o}{2}$. Entonces "
                     r"$\frac{1}{d_o} - \frac{2}{d_o} = -\frac{1}{30} \Rightarrow d_o = 30$ cm "
                     r"(imagen virtual a 15 cm detrás del espejo).",
           notas="En la guía dice «un objeto convexo»; se corrige a «espejo convexo».", **COMUN)
def _():
    do = symbols("d_o", positive=True)
    sol = solve(1 / do + 1 / (-do / 2) - Rational(1, -30), do)
    assert sol == [30]
    assert espejo(-30, 30) == -15 and -espejo(-30, 30) / 30 * 8 == 4


@ejercicio(id="optica-11-081", tema="espejos", tipo="calculo", dificultad=2, fuente=f"{PRO} — 14",
           enunciado=r"Un espejo esférico cóncavo forma una imagen real a 8 cm del espejo cuando el "
                     r"objeto está a 24 cm. Halla el radio de curvatura del espejo.",
           respuesta=r"$\frac1f = \frac18 + \frac1{24} = \frac{4}{24} \Rightarrow f = 6$ cm; "
                     r"$R = 2f = 12$ cm.",
           notas="Se precisa que la imagen es real (la guía no lo dice; si fuera virtual, "
                 "d_i = -8 cm daría f = 12 cm y R = 24 cm).", **COMUN)
def _():
    f = 1 / (Rational(1, 8) + Rational(1, 24))
    assert f == 6 and 2 * f == 12
    assert espejo(f, 24) == 8


@ejercicio(id="optica-11-082", tema="espejos", tipo="calculo", dificultad=2, fuente=f"{PRO} — 15",
           enunciado=r"A 10 cm del vértice de un espejo esférico convexo se coloca un objeto. Si la "
                     r"distancia focal es de 18 cm, ¿a qué distancia se forma la imagen?",
           respuesta=r"$f = -18$ cm: $\frac{1}{d_i} = -\frac1{18} - \frac1{10} = -\frac{14}{90} "
                     r"\Rightarrow d_i = -\frac{45}{7} \approx -\num{6,43}$ cm: imagen virtual a "
                     r"\num{6,43} cm detrás del espejo.", **COMUN)
def _():
    assert espejo(-18, 10) == Rational(-45, 7)


@ejercicio(id="optica-11-083", tema="espejos", tipo="calculo", dificultad=2, fuente=f"{PRO} — 16",
           enunciado=r"El radio de curvatura de un espejo cóncavo es de 50 cm. Si se coloca un "
                     r"objeto a 30 cm del espejo, ¿cuál es la distancia entre el objeto y la imagen?",
           respuesta=r"$f = 25$ cm; $\frac1{d_i} = \frac1{25} - \frac1{30} = \frac1{150} "
                     r"\Rightarrow d_i = 150$ cm (imagen real, del mismo lado que el objeto). "
                     r"Distancia objeto–imagen: $150 - 30 = 120$ cm.", **COMUN)
def _():
    di = espejo(25, 30)
    assert di == 150 and di - 30 == 120


@ejercicio(id="optica-11-084", tema="espejos", tipo="calculo", dificultad=2, fuente=f"{PRO} — 17",
           enunciado=r"¿Cuál es el radio de curvatura de un espejo cóncavo si un objeto situado a "
                     r"12 cm forma su imagen real a 18 cm del espejo?",
           respuesta=r"$\frac1f = \frac1{12} + \frac1{18} = \frac{5}{36} \Rightarrow f = "
                     r"\num{7,2}$ cm; $R = 2f = \num{14,4}$ cm.",
           notas="Se precisa «imagen real». Si la imagen fuera virtual (d_i = -18 cm): f = 36 cm, "
                 "R = 72 cm.", **COMUN)
def _():
    f = 1 / (Rational(1, 12) + Rational(1, 18))
    assert f == Rational(36, 5) and 2 * f == Rational(72, 5)
    assert 1 / (Rational(1, 12) - Rational(1, 18)) == 36      # caso virtual (nota)


@ejercicio(id="optica-11-085", tema="refracción de la luz", tipo="calculo", dificultad=2,
           fuente=f"{PRO} — 18",
           enunciado=r"Determina el ángulo límite para el paso de la luz de un prisma de vidrio "
                     r"($n = \num{1,5}$) al aire y dibuja la trayectoria que sigue el rayo.",
           respuesta=r"$\sen i_l = \dfrac{n_2}{n_1} = \dfrac{1}{\num{1,5}} \Rightarrow i_l \approx "
                     r"\num{41,8}^\circ$. Si el rayo incide dentro del vidrio con más de "
                     r"\num{41,8}° respecto a la normal, se refleja totalmente; con ese ángulo, el "
                     r"rayo refractado sale rasante a la superficie.", **COMUN)
def _():
    il = float(deg(asin(Rational(1) / Rational(3, 2))))
    assert aprox(il, 41.8, 0.001)


@ejercicio(id="optica-11-086", tema="refracción de la luz", tipo="calculo", dificultad=2,
           fuente=f"{PRO} — 19",
           enunciado=r"Rayos de luz se propagan en el agua ($n = \num{1,33}$) y se dirigen hacia el "
                     r"aire. Determina el ángulo de refracción para ángulos de incidencia de 20°, "
                     r"40° y 45°.",
           respuesta=r"$\sen r = \num{1,33}\sen i$: para 20°, $r \approx \num{27,1}^\circ$; para "
                     r"40°, $r \approx \num{58,8}^\circ$; para 45°, $r \approx \num{70,1}^\circ$. "
                     r"(Los tres son menores que el ángulo límite, \num{48,8}°, así que siempre hay "
                     r"refracción.)", **COMUN)
def _():
    n = 1.33
    r = [math.degrees(math.asin(n * math.sin(math.radians(i)))) for i in (20, 40, 45)]
    for calc, esperado in zip(r, (27.1, 58.8, 70.1)):
        assert abs(calc - esperado) < 0.06
    assert abs(math.degrees(math.asin(1 / n)) - 48.8) < 0.06


@ejercicio(id="optica-11-087", tema="refracción de la luz", tipo="calculo", dificultad=1,
           fuente=f"{PRO} — 20",
           enunciado=r"Una luz con $\lambda = 589$ nm en el vacío atraviesa un objeto de sílice "
                     r"cuyo índice de refracción es $n = \num{1,458}$. ¿Cuál es su longitud de onda "
                     r"en la sílice?",
           respuesta=r"La frecuencia no cambia y $v = c/n$, así que $\lambda_n = \dfrac{\lambda}{n} "
                     r"= \dfrac{589\ \text{nm}}{\num{1,458}} \approx 404$ nm.", **COMUN)
def _():
    lam0 = 589 * u.nanometer
    f = C / lam0
    lam = (C / Rational(1458, 1000)) / f
    assert aprox(valor(lam, u.nanometer), 404, 0.001)


@ejercicio(id="optica-11-088", tema="refracción de la luz", tipo="calculo", dificultad=1,
           fuente=f"{PRO} — 21",
           enunciado=r"Un rayo de luz pasa del aire a un medio con índice de refracción \num{1,4}. "
                     r"Si el ángulo de incidencia es 40°, determina el ángulo de refracción.",
           respuesta=r"$\sen r = \dfrac{\sen 40^\circ}{\num{1,4}} \approx \num{0,459} \Rightarrow "
                     r"r \approx \num{27,3}^\circ$.", **COMUN)
def _():
    r = float(deg(asin(sin(40 * pi / 180) / Rational(14, 10))))
    assert abs(r - 27.3) < 0.05
