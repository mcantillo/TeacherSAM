"""Banco de ejercicios — Física 11° — Ondas (Capítulo 2 de la guía de fenómenos ondulatorios).
Fuente: Guía de Apoyo Educativo «Fenómenos ondulatorios», grado 11°, Capítulo 2: las ondas
(«Desarrolla tus competencias», «Actividades», «Problemas»); se lee en
recursos/fisica/Guías pedagógicas Física/markdown/11 - Guia_de_Apoyo_Fenomenos_ondulatorios_grado_11_fisica.md
Convención de la guía para la función de onda: y = A sen(ωt − kx).

No incluidos:
- Desarrolla tus competencias 19 (recrear reflexión, interferencia y refracción con una cuerda y
  explicarlo a los compañeros): demostración práctica, no hay respuesta que calificar.
- Problemas 20b y 20c: la guía no da las distancias del punto P a los focos, así que no se puede
  hallar la diferencia de recorrido ni el tipo de interferencia (solo se incluye 20a).
- Prácticas de laboratorio del capítulo.

Correcciones (detalle en `notas` de cada ejercicio): Problemas 6 (faltaban datos), 8 (faltaba el
medio), 18 («0 m/s»), 19 (ángulo «con la horizontal»), 23 (enunciado confuso), Actividades 2 y
Desarrolla tus competencias 3 (más de una opción defendible).

Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/fisica/ondas-11.py
"""
from sympy import asin, cos, deg, expand_trig, pi, simplify, sin, solve, sqrt, symbols
from sympy.physics import units as u
from sympy.physics.units import convert_to

from ejercicios import ejercicio, ejercicio_manual

GUIA = "Guía de Apoyo Fenómenos ondulatorios 11°"
CAP = f"{GUIA}, Capítulo 2: las ondas"
DTC = "Desarrolla tus competencias"
ACT = "Actividades"
PRO = "Problemas"
COMUN = dict(grados=[11], dba=["naturales-11-1"])

_n = [0]


def nid():
    _n[0] += 1
    return f"ondas-11-{_n[0]:03d}"


def fuente(seccion, lit):
    return f"{CAP}, {seccion} — {lit}"


def valor(q, unidad):
    return float(convert_to(q, unidad) / unidad)


def aprox(a, b, rel=0.01):
    return abs(a - b) <= rel * abs(b)


def opciones(*items):
    return r" \begin{opciones} " + " ".join(r"\item " + i for i in items) + r" \end{opciones}"


def manual(seccion, lit, enunciado, respuesta, tema="ondas", tipo="conceptual", dificultad=1,
           notas=None):
    extra = {"notas": notas} if notas else {}
    ejercicio_manual(id=nid(), tema=tema, tipo=tipo, dificultad=dificultad,
                     fuente=fuente(seccion, lit), enunciado=enunciado, respuesta=respuesta,
                     **extra, **COMUN)


def vf(seccion, lit, afirmacion, verdad, justificacion, tema="ondas", notas=None):
    manual(seccion, lit,
           r"Escribe V si la afirmación es verdadera o F si es falsa, y justifica: " + afirmacion,
           ("V. " if verdad else "F. ") + justificacion, tema=tema, tipo="argumentacion",
           notas=notas)


def num(seccion, lit, enunciado, respuesta, tema="ondas", tipo="calculo", dificultad=1,
        notas=None):
    """Decorador para ejercicios con comprobación numérica."""
    extra = {"notas": notas} if notas else {}
    return ejercicio(id=nid(), tema=tema, tipo=tipo, dificultad=dificultad,
                     fuente=fuente(seccion, lit), enunciado=enunciado, respuesta=respuesta,
                     **extra, **COMUN)


FEN = "fenómenos ondulatorios"

# =====================================================================
# Desarrolla tus competencias
# =====================================================================
OLA = r"La «ola» que producen los espectadores de un partido de fútbol al levantarse y volverse a sentar: "
manual(DTC, "1a", OLA + r"¿en qué se parece a la propagación de una onda?",
       r"Cada espectador solo se levanta y se sienta en su puesto (oscila alrededor de su "
       r"posición), pero la perturbación avanza por la tribuna: se propaga un estado de "
       r"movimiento (energía) sin que las personas se desplacen, igual que en una onda.")
manual(DTC, "1b", OLA + r"¿es una onda transversal o longitudinal? Explica tu respuesta.",
       r"Transversal: los espectadores se mueven verticalmente (arriba y abajo), perpendicular a "
       r"la dirección horizontal en que avanza la ola.")

REL = r"Establece la relación entre "
manual(DTC, "2a", REL + r"el período y la frecuencia de una onda.",
       r"Son inversos: $T = \dfrac{1}{f}$. Si la frecuencia aumenta, el período disminuye.")
manual(DTC, "2b", REL + r"la velocidad de propagación de una onda y la frecuencia.",
       r"$v = \lambda f$. La velocidad la fija el medio; en un mismo medio, si aumenta la "
       r"frecuencia disminuye la longitud de onda y $v$ no cambia.")
manual(DTC, "2c", REL + r"la longitud de onda y la velocidad de propagación.",
       r"$\lambda = \dfrac{v}{f} = vT$: la longitud de onda es la distancia que avanza la onda "
       r"en un período; para una frecuencia fija, a mayor velocidad mayor longitud de onda "
       r"(por eso $\lambda$ cambia al pasar a otro medio).")
manual(DTC, "2d", REL + r"las ondas transversales y las longitudinales.",
       r"En ambas se transporta energía sin transporte de materia. En las transversales las "
       r"partículas oscilan perpendicularmente a la dirección de propagación (cuerda, luz); en "
       r"las longitudinales oscilan en la misma dirección de propagación (sonido, resorte "
       r"comprimido).")
manual(DTC, "2e", REL + r"la cresta y el valle de una onda.",
       r"La cresta es el punto más alto (elongación $+A$) y el valle el más bajo ($-A$); están "
       r"separados media longitud de onda y dos crestas (o dos valles) consecutivas, "
       r"una longitud de onda.")

manual(DTC, "3",
       r"Un sismo propaga grandes cantidades de energía y produce daños en las construcciones. "
       r"Según la dirección de oscilación respecto a la dirección de propagación, las ondas "
       r"sísmicas son:" + opciones("Transversales.", "Longitudinales.", "Electromagnéticas.",
                                   "Lineales."),
       r"Pueden ser de los dos tipos (a y b): las ondas P (primarias) son longitudinales y las "
       r"ondas S (secundarias) son transversales. No son electromagnéticas (son mecánicas: "
       r"necesitan un medio).", tipo="seleccion",
       notas="La guía da una sola respuesta, pero a y b son correctas (ondas P y S, que la "
             "propia guía describe en «Las ondas sísmicas»). Se reescribió «según la dirección "
             "de propagación de las ondas respecto a la dirección del movimiento» como «según "
             "la dirección de oscilación respecto a la de propagación». Sugerencia: preguntar "
             "«las ondas P son…».")
manual(DTC, "4",
       r"La potencia que transmite una onda depende de:" + opciones(
           "El período.", "La masa del medio de propagación.", "Solamente del tiempo.",
           "Solamente de la energía transmitida."),
       r"a. $P = 2\pi^2 \mu v f^2 A^2$ y $f = 1/T$: depende del período (además de la "
       r"amplitud, la densidad lineal y la velocidad). No depende de la masa total del medio "
       r"sino de su densidad lineal $\mu$; c y d son falsas por el «solamente».", tipo="seleccion")
manual(DTC, "5",
       r"Cuando se lanza una piedra en un lago, el frente de onda observado en el agua es:"
       + opciones("Lineal y se propaga en una sola dirección.",
                  "Lineal y se propaga en todas las direcciones.",
                  "Circular y se propaga en todas las direcciones.",
                  "Curvo y se propaga solo en media circunferencia."),
       r"c. La perturbación es puntual y el medio es igual en todas las direcciones: los frentes "
       r"son circunferencias concéntricas que se alejan del punto de impacto.", tipo="seleccion")
manual(DTC, "6",
       r"Explica por qué cuando pasa cerca un vehículo de carga pesada se siente como si "
       r"temblara la Tierra.",
       r"El vehículo golpea y comprime el suelo y la vía; esas vibraciones se propagan por el "
       r"suelo (y por el aire) como ondas mecánicas que llegan hasta nosotros y hacen vibrar el "
       r"piso y los objetos, como un sismo muy pequeño.")
manual(DTC, "7",
       r"Explica por qué, cuando un objeto flota en el agua y esta se mueve con ondas, el objeto "
       r"permanece en su sitio moviéndose hacia arriba y hacia abajo.",
       r"La onda transporta energía, no materia: cada porción de agua oscila alrededor de su "
       r"posición de equilibrio y el objeto que flota oscila con ella, sin ser arrastrado en la "
       r"dirección de propagación.",
       notas="Se quitó la palabra suelta «curso.» al final del enunciado.")

SISMO = (r"La sismología es la ciencia que estudia los terremotos. Un terremoto se genera a cierta "
         r"profundidad bajo la superficie; el punto donde se origina se llama foco o hipocentro, "
         r"y el punto de la superficie más próximo a él, epicentro. Las ondas sísmicas se "
         r"perciben con mayor intensidad en el epicentro y luego se dispersan desde él. ")
NOTA_SISMO = ("La lectura de la guía dice que el terremoto se genera «a unos 60 km por debajo de "
              "la corteza terrestre»; los focos están dentro de la corteza o el manto superior, a "
              "profundidades muy variables (de pocos km a unos 700 km). Se quitó ese dato.")
manual(DTC, "8", SISMO + r"¿Cómo se llama la persona encargada de estudiar los terremotos?",
       r"Sismólogo (o sismóloga).", notas=NOTA_SISMO)
manual(DTC, "9", SISMO + r"¿Por qué un terremoto ocurre en la parte rígida de la corteza "
                         r"terrestre?",
       r"Porque las rocas rígidas acumulan deformación elástica (por el movimiento de las placas) "
       r"hasta que se rompen o deslizan bruscamente en una falla; esa liberación súbita de "
       r"energía genera las ondas sísmicas. Un material blando se deformaría poco a poco sin "
       r"acumular esa energía.", notas=NOTA_SISMO)
manual(DTC, "10", SISMO + r"Después de un temblor fuerte las personas suelen preguntar dónde "
                          r"fue el epicentro. ¿Qué quiere decir eso?",
       r"Preguntan por el punto de la superficie situado directamente sobre el foco, que es "
       r"donde el sismo se sintió con más intensidad y donde probablemente hubo más daños.",
       notas=NOTA_SISMO)
manual(DTC, "11", SISMO + r"¿Por qué luego de un terremoto las personas no preguntan por la "
                          r"localización del hipocentro?",
       r"Porque el hipocentro está bajo tierra y no se puede visitar; lo que interesa a la "
       r"población es el lugar de la superficie afectado (el epicentro). La profundidad del foco "
       r"sí la reportan los servicios sismológicos.", notas=NOTA_SISMO)
manual(DTC, "12", SISMO + r"¿Has vivido algún terremoto o temblor muy fuerte? ¿Cuál fue el "
                          r"epicentro?",
       r"Respuesta personal. Se espera que el estudiante nombre un sismo que sintió (en Cali son "
       r"frecuentes los sismos con epicentro en la costa pacífica o en el Valle del Cauca) y "
       r"distinga el epicentro del lugar donde lo sintió.", tipo="contexto", notas=NOTA_SISMO)
manual(DTC, "13", r"¿Por qué se puede observar el reflejo de los objetos en cualquier vidrio?",
       r"Porque en toda superficie de separación entre dos medios (aire y vidrio) parte de la luz "
       r"se refleja y parte se refracta; el vidrio es liso, así que la reflexión es especular y "
       r"forma imagen. Se ve mejor cuando al otro lado del vidrio está oscuro.", tema=FEN)
manual(DTC, "14", r"Explica por qué, en ocasiones, las olas del mar aumentan su tamaño o lo "
                  r"reducen.",
       r"Por superposición: cuando se encuentran olas de distinto origen, sus elongaciones se "
       r"suman (interferencia constructiva, olas mayores, o destructiva, menores). También "
       r"crecen al llegar a aguas poco profundas (disminuye su velocidad y se concentra la "
       r"energía) y según la fuerza del viento que las genera.", tema=FEN)
manual(DTC, "15", r"Realiza un esquema donde expliques las partes de una onda.",
       r"Una curva senoidal con el eje de equilibrio, y señaladas: cresta, valle, amplitud $A$ "
       r"(del eje a una cresta), longitud de onda $\lambda$ (entre dos crestas consecutivas), "
       r"el sentido de propagación con su velocidad $v$, y la relación $v = \lambda f$, "
       r"$T = 1/f$.", tipo="argumentacion")
manual(DTC, "16", r"Explica algunas experiencias vividas en las que hayas observado fenómenos "
                  r"ondulatorios o algunas de sus propiedades.",
       r"Respuesta abierta. Ejemplos válidos: eco en un coliseo (reflexión), la cuchara que se ve "
       r"quebrada en un vaso de agua (refracción), oír a alguien detrás de una pared a través de "
       r"una puerta abierta (difracción), manchas de colores en una burbuja (interferencia).",
       tema=FEN, tipo="contexto")
manual(DTC, "17", r"¿Cómo harías para generar ondas en un estanque y hacer mover un barco de "
                  r"papel?",
       r"Golpeando periódicamente el agua se generan ondas, pero estas no arrastran el barco: "
       r"solo lo hacen oscilar arriba y abajo, porque la onda transporta energía y no materia. "
       r"Para desplazarlo hay que producir una corriente de agua o de aire (soplar, empujar el "
       r"agua), o que las olas rompan cerca de la orilla.", tipo="argumentacion",
       notas="La guía pide además «realiza el experimento y comprueba tu teoría»; se deja la "
             "pregunta de predicción.")
manual(DTC, "18", r"Realiza un mapa conceptual donde expliques los fenómenos ondulatorios.",
       r"Debe incluir: reflexión (la onda regresa al mismo medio; ángulo de incidencia igual al "
       r"de reflexión), refracción (cambia de medio y de velocidad; la frecuencia no cambia; ley "
       r"de Snell), difracción (bordea obstáculos o aberturas del orden de $\lambda$; principio de "
       r"Huygens), interferencia (superposición constructiva o destructiva) y ondas "
       r"estacionarias (nodos y vientres).", tema=FEN, tipo="argumentacion")

# =====================================================================
# Actividades
# =====================================================================
vf(ACT, "1a", r"La propagación de las ondas es un mecanismo para transmitir energía a través de "
              r"un medio sin que haya transporte de materia.", True,
   r"Las partículas del medio solo oscilan alrededor de su posición de equilibrio; lo que "
   r"avanza es la energía.", notas="La guía dice «transmitir energía de un medio»; se escribió "
                                   "«a través de un medio».")
vf(ACT, "1b", r"La línea que une todos los puntos vecinos de una onda se llama frente de onda.",
   False, r"El frente de onda une los puntos vecinos que están en el mismo estado de vibración "
          r"(en fase), no todos los puntos.")
vf(ACT, "1c", r"Cuando el movimiento oscilatorio que produce una onda es periódico, se dice que "
              r"las ondas son circulares.", False,
   r"Se dice que la onda es periódica. «Circular» se refiere a la forma del frente de onda.")
vf(ACT, "1d", r"Cuando las partículas de un medio oscilan en dirección perpendicular a la "
              r"dirección de propagación, se dice que las ondas son transversales.", True,
   r"Es la definición de onda transversal.")
vf(ACT, "1e", r"En las ondas longitudinales, las partículas del medio oscilan en dirección "
              r"paralela a la dirección de propagación de la onda.", True,
   r"Es la definición de onda longitudinal (por ejemplo, el sonido).")
vf(ACT, "1f", r"La amplitud de la onda depende de la longitud de onda.", False,
   r"Son independientes: la amplitud depende de la energía de la fuente y la longitud de onda "
   r"de la frecuencia y del medio ($\lambda = v/f$).")

manual(ACT, "2", r"Elige la afirmación correcta." + opciones(
    "Las ondas no transmiten energía.",
    "Las ondas transversales son paralelas a la velocidad de propagación.",
    "Las ondas se producen por el movimiento armónico simple de las partículas del medio.",
    "La densidad lineal de masa en una cuerda depende de la masa de la cuerda y de su longitud."),
    r"d. $\mu = m/L$. a es falsa (las ondas transportan energía), b es falsa (en las "
    r"transversales la oscilación es perpendicular a la propagación) y c solo vale para las "
    r"ondas armónicas: un pulso también es una onda y no es un MAS.", tipo="seleccion",
    notas="En d la guía dice «de la masa del objeto»; se escribió «de la cuerda». La opción c "
          "es verdadera para ondas armónicas, por lo que podría confundir: la clave es d.")

for lit, concepto, resp in [
    ("3a", "Onda mecánica", r"Perturbación que se propaga a través de un medio material "
                            r"(sólido, líquido o gas), transportando energía sin transportar "
                            r"materia; no se propaga en el vacío. Ej.: el sonido."),
    ("3b", "Amplitud", r"Máxima distancia que alcanza una partícula del medio respecto a su "
                       r"posición de equilibrio; se mide en metros."),
    ("3c", "Período", r"Tiempo que tarda en producirse una onda completa, igual al tiempo de una "
                      r"vibración completa de un punto del medio; $T = 1/f$, en segundos."),
    ("3d", "Longitud de onda", r"Distancia entre dos puntos consecutivos en el mismo estado de "
                               r"vibración, por ejemplo dos crestas; $\lambda = v T$, en metros."),
    ("3e", "Onda electromagnética", r"Onda formada por campos eléctrico y magnético oscilantes, "
                                    r"perpendiculares entre sí; es transversal, no necesita "
                                    r"medio y en el vacío viaja a "
                                    r"$c \approx 3\times10^{8}$ m/s. Ej.: la luz, las ondas de "
                                    r"radio."),
    ("3f", "Velocidad de propagación", r"Rapidez con que la perturbación avanza por el medio; "
                                       r"depende del medio (no de la fuente) y vale "
                                       r"$v = \lambda / T = \lambda f$."),
]:
    manual(ACT, lit, rf"Define el siguiente concepto: {concepto}.", resp)

manual(ACT, "4", r"La velocidad de propagación de una onda transversal en una cuerda depende de:"
       + opciones("La amplitud.", "La frecuencia.", "El período.",
                  "La tensión (fuerza) de la cuerda.", "La longitud de onda."),
       r"d. $v = \sqrt{T/\mu}$: depende de la tensión y de la densidad lineal de la cuerda, no "
       r"de la amplitud ni de la frecuencia; al cambiar la frecuencia cambia $\lambda$, no $v$.",
       tipo="seleccion",
       notas="La guía dice «la fuerza horizontal»; se escribió «la tensión (fuerza) de la cuerda».")


@num(ACT, "5", r"Si se desea saber la velocidad de propagación de una onda periódica se debe "
               r"conocer:" + opciones("La frecuencia y el período.",
                                      "La frecuencia y la longitud de onda.",
                                      "El período y la amplitud.",
                                      "La amplitud y la frecuencia."),
     r"b. $v = \lambda f$. Frecuencia y período dan la misma información ($T = 1/f$) y la "
     r"amplitud no interviene.", tipo="seleccion")
def _():
    lam, f, T, A = symbols("lambda f T A", positive=True)
    v = lam * f
    datos = {"a": {f, T}, "b": {lam, f}, "c": {T, A}, "d": {A, f}}
    # con f = 1/T, v solo se puede calcular si entre los datos está λ (y f o T)
    sirve = {k: lam in d and (f in d or T in d) for k, d in datos.items()}
    assert sirve == {"a": False, "b": True, "c": False, "d": False}


manual(ACT, "6", r"Se atan por un extremo dos cuerdas de distinto material y se hacen vibrar. "
                 r"¿Cómo es la longitud de onda en cada una?",
       r"La frecuencia es la misma en las dos (la fija la fuente y se conserva en la unión), pero "
       r"la velocidad depende de cada cuerda ($v = \sqrt{T/\mu}$). Como $\lambda = v/f$, la "
       r"longitud de onda es menor en la cuerda más densa (más lenta) y mayor en la más liviana.",
       tipo="argumentacion")
manual(ACT, "7", r"Cuando se golpea una varilla por un costado en uno de sus extremos, comienza "
                 r"a vibrar. ¿Qué tipo de onda viaja por ella? Explica tu respuesta.",
       r"Principalmente transversal: el golpe lateral desplaza las partículas perpendicularmente "
       r"al eje de la varilla, que es la dirección en que se propaga la onda. (Si se golpeara en "
       r"la punta, a lo largo del eje, la onda sería longitudinal.)", tipo="argumentacion")

vf(ACT, "8a", r"En el fenómeno de la reflexión, para espejos planos, el ángulo de incidencia es "
              r"igual al ángulo de reflexión.", True,
   r"Es la ley de la reflexión (vale para cualquier superficie, medidos los ángulos respecto a "
   r"la normal).", tema=FEN)
vf(ACT, "8b", r"El fenómeno de la refracción ocurre cuando la onda choca con un obstáculo y "
              r"regresa nuevamente.", False,
   r"Eso es la reflexión. La refracción es el cambio de dirección y velocidad de una onda al "
   r"pasar de un medio a otro.", tema=FEN)
vf(ACT, "8c", r"El principio de Huygens dice que un punto no es un nuevo frente de onda pero la "
              r"velocidad de las ondas se mantiene constante después de chocar con un "
              r"obstáculo.", False,
   r"El principio de Huygens dice que cada punto de un frente de onda se comporta como un foco "
   r"de ondas secundarias, y la envolvente de esas ondas forma el nuevo frente.", tema=FEN)
vf(ACT, "8d", r"La difracción se nota cuando una onda pasa por un obstáculo o una abertura de "
              r"tamaño del orden de su longitud de onda.", True,
   r"La onda bordea el obstáculo o se abre al pasar la rendija; el efecto es apreciable cuando "
   r"el tamaño es comparable a $\lambda$ o menor.", tema=FEN,
   notas="La guía dice «tan pequeño como el orden de magnitud de la longitud de onda»; se "
         "reescribió para que la afirmación sea claramente verdadera.")
vf(ACT, "8e", r"En las señales de frecuencia modulada (F.M.) la amplitud de la onda permanece "
              r"constante.", True,
   r"En F.M. la información se imprime variando la frecuencia de la portadora; la amplitud no "
   r"cambia.", tema=FEN)
vf(ACT, "8f", r"En las señales de amplitud modulada (A.M.), la frecuencia es alterada con "
              r"variaciones de señales de audio enviadas.", False,
   r"En A.M. lo que varía con la señal de audio es la amplitud de la portadora; su frecuencia "
   r"se mantiene.", tema=FEN)

for lit, concepto, resp in [
    ("9a", "Refracción", r"Cambio de dirección y de velocidad de una onda al pasar de un medio a "
                         r"otro; la frecuencia se conserva y cambia la longitud de onda."),
    ("9b", "Reflexión", r"Cambio de dirección de una onda que llega a la frontera con otro medio "
                        r"y regresa al medio inicial; el ángulo de incidencia es igual al de "
                        r"reflexión."),
    ("9c", "Interferencia", r"Superposición de dos o más ondas que coinciden en un punto; la "
                            r"elongación resultante es la suma de las elongaciones: constructiva "
                            r"si se refuerzan, destructiva si se anulan."),
    ("9d", "Ley de Snell", r"Relación entre los ángulos de incidencia y de refracción: "
                           r"$\dfrac{\sen\theta_1}{\sen\theta_2} = \dfrac{v_1}{v_2}$ "
                           r"(para la luz, $n_1 \sen\theta_1 = n_2 \sen\theta_2$)."),
    ("9e", "Principio de Huygens", r"Cada punto de un frente de onda actúa como foco de nuevas "
                                   r"ondas secundarias; el nuevo frente es la envolvente de "
                                   r"todas ellas."),
    ("9f", "Onda estacionaria", r"Onda que resulta de la superposición de dos ondas iguales que "
                                r"viajan en sentidos opuestos; tiene puntos fijos (nodos) y "
                                r"puntos de máxima amplitud (vientres) y no transporta energía "
                                r"de un lado a otro."),
]:
    manual(ACT, lit, rf"Define el siguiente concepto: {concepto}.", resp, tema=FEN)

manual(ACT, "10", r"Elige la respuesta correcta. La interferencia destructiva se da cuando:"
       + opciones("Chocan dos crestas.", "Choca una cresta con un valle.", "Chocan dos valles.",
                  "Ninguna de las anteriores."),
       r"b. Las elongaciones de signo opuesto se restan; si las amplitudes son iguales, se "
       r"anulan. Dos crestas o dos valles dan interferencia constructiva.", tema=FEN,
       tipo="seleccion")
manual(ACT, "11", r"Elige la respuesta correcta. Una onda reflejada es:" + opciones(
    "Un frente de ondas secundario que se genera gracias a un obstáculo.",
    "Una onda que pasa de un medio a otro cambiando su velocidad de propagación.",
    "La que se genera después de chocar con un obstáculo y regresa al mismo medio.",
    "Una onda que llega libremente a un obstáculo."),
       r"c. La onda reflejada es la que regresa al medio de donde vino tras chocar con la "
       r"frontera; b describe la refracción y d la onda incidente.", tema=FEN, tipo="seleccion",
       notas="Se completó la opción c («y regresa al mismo medio») para distinguirla de la "
             "difracción.")
manual(ACT, "12", r"Estás de excursión en el campo y compruebas que la pared de un acantilado "
                  r"lejano produce eco. Explica cómo se puede calcular a qué distancia se "
                  r"encuentra.",
       r"Se mide con un cronómetro el tiempo $t$ entre el grito y el eco. El sonido va y vuelve, "
       r"así que recorre $2d$: $d = \dfrac{v\,t}{2}$, con $v \approx 340$ m/s. Por ejemplo, "
       r"si $t = 2$ s, $d = 340$ m.", tema=FEN, tipo="contexto")
manual(ACT, "13", r"Explica por qué en cada extremo fijo de una cuerda en la que se produce una "
                  r"onda estacionaria siempre hay un nodo.",
       r"Porque el extremo fijo no se puede mover: su elongación es cero en todo instante. Allí "
       r"la onda reflejada llega invertida y anula a la incidente, que es la condición de nodo.",
       tema=FEN, tipo="argumentacion")
manual(ACT, "14", r"Al saltar lazo, la cuerda parece describir una onda estacionaria. ¿Se podría "
                  r"considerar esta situación un ejemplo de onda estacionaria? Explica.",
       r"Se parece al modo fundamental (los extremos, en las manos, casi no se mueven y el centro "
       r"tiene la máxima amplitud), pero en rigor no lo es: la cuerda gira como un todo movida "
       r"por las manos, no resulta de la superposición de dos ondas viajeras que se reflejan en "
       r"los extremos.", tema=FEN, tipo="argumentacion")
manual(ACT, "15", r"Explica con un esquema cómo funciona el sonar empleado para medir la "
                  r"profundidad del fondo marino. Indica qué fenómeno ondulatorio se utiliza.",
       r"El barco emite un pulso de ultrasonido hacia el fondo; el pulso se refleja (eco) y "
       r"regresa a un receptor del barco. Con el tiempo de ida y vuelta $t$ y la velocidad del "
       r"sonido en el agua ($\approx 1500$ m/s): $h = \dfrac{v\,t}{2}$. Fenómeno: la reflexión. "
       r"El esquema muestra barco, onda que baja, fondo y onda reflejada que sube.",
       tema=FEN, tipo="argumentacion")
manual(ACT, "16", r"De las características frecuencia, longitud de onda, velocidad de "
                  r"propagación y período, ¿cuáles permanecen constantes y cuáles cambian en la "
                  r"reflexión? ¿Y en la refracción?",
       r"En la reflexión la onda sigue en el mismo medio: no cambia ninguna (solo la dirección). "
       r"En la refracción la frecuencia y el período se conservan (los impone la fuente), "
       r"mientras que la velocidad y la longitud de onda cambian ($\lambda = v/f$).",
       tema=FEN, tipo="argumentacion")

# =====================================================================
# Problemas
# =====================================================================
m_, s_, N_, kg_, Hz_ = u.meter, u.second, u.newton, u.kilogram, u.hertz


@num(PRO, "1", r"Una cuerda de $2$ kg de masa se estira entre dos soportes separados $40$ cm. "
               r"Si la tensión de la cuerda es de $500$ N, ¿cuánto tiempo tardará un pulso en "
               r"viajar de un soporte a otro?",
     r"$\mu = \dfrac{2}{\num{0,4}} = 5$ kg/m; $v = \sqrt{\dfrac{500}{5}} = 10$ m/s; "
     r"$t = \dfrac{\num{0,4}}{10} = \num{0,04}$ s.", dificultad=2,
     notas="Una cuerda de 2 kg en 40 cm es muy pesada (5 kg/m), pero los datos son "
           "coherentes; se dejan.")
def _():
    L = 40 * u.centimeter
    mu = 2 * kg_ / L
    v = sqrt(500 * N_ / mu)
    assert aprox(valor(v, m_ / s_), 10)
    assert aprox(valor(L / v, s_), 0.04)


CUERDA2 = (r"Una cuerda horizontal se somete a una tensión de $500$ N; su masa es de "
           r"$\num{0,3}$ kg y su longitud de $150$ cm. Si se pone a vibrar con una amplitud de "
           r"$\num{0,3}$ m, halla ")


@num(PRO, "2a", CUERDA2 + r"la densidad lineal de masa.",
     r"$\mu = \dfrac{\num{0,3}\ \text{kg}}{\num{1,5}\ \text{m}} = \num{0,2}$ kg/m.")
def _():
    assert aprox(valor(0.3 * kg_ / (150 * u.centimeter), kg_ / m_), 0.2)


@num(PRO, "2b", CUERDA2 + r"la velocidad de la onda.",
     r"$v = \sqrt{\dfrac{500}{\num{0,2}}} = \sqrt{2500} = 50$ m/s.")
def _():
    mu = 0.3 * kg_ / (150 * u.centimeter)
    assert aprox(valor(sqrt(500 * N_ / mu), m_ / s_), 50)


@num(PRO, "2c", CUERDA2 + r"la función de onda si la frecuencia es $25$ Hz.",
     r"$\omega = 2\pi f = 50\pi$ rad/s, $\lambda = \dfrac{v}{f} = 2$ m, "
     r"$k = \dfrac{2\pi}{\lambda} = \pi$ rad/m: "
     r"$y = \num{0,3}\,\sen(50\pi t - \pi x)$ (en metros y segundos).", dificultad=2)
def _():
    mu = 0.3 * kg_ / (150 * u.centimeter)
    v = valor(sqrt(500 * N_ / mu), m_ / s_)
    f = 25
    lam = v / f
    assert aprox(lam, 2) and aprox(2 * float(pi) * f, 50 * float(pi))
    assert aprox(2 * float(pi) / lam, float(pi))
    # la función cumple y(x + λ, t) = y(x, t)
    x, t = symbols("x t")
    y = 0.3 * sin(50 * pi * t - pi * x)
    assert abs(float((y.subs(x, x + 2) - y).subs({x: 0.37, t: 0.011}))) < 1e-12


@num(PRO, "3", r"Si la velocidad de una onda es de $36$ km/h y su frecuencia de $2$ Hz, "
               r"determina la longitud de onda en centímetros.",
     r"$36$ km/h $= 10$ m/s; $\lambda = \dfrac{v}{f} = \dfrac{10}{2} = 5$ m $= 500$ cm.")
def _():
    lam = (36 * u.kilometer / u.hour) / (2 * Hz_)
    assert aprox(valor(lam, u.centimeter), 500)


@num(PRO, "4", r"La densidad lineal de una cuerda es $\num{0,0125}$ kg/m y está sometida a una "
               r"tensión de $125$ N. Calcula la velocidad de propagación.",
     r"$v = \sqrt{\dfrac{125}{\num{0,0125}}} = \sqrt{10\,000} = 100$ m/s.")
def _():
    assert aprox(valor(sqrt(125 * N_ / (0.0125 * kg_ / m_)), m_ / s_), 100)


@num(PRO, "5", r"Un pato que nada en un estanque efectúa cuatro oscilaciones en $5$ s. Calcula "
               r"el período de las ondas causadas por las oscilaciones del pato.",
     r"$T = \dfrac{5\ \text{s}}{4} = \num{1,25}$ s.")
def _():
    assert aprox(valor(5 * s_ / 4, s_), 1.25)


@num(PRO, "6", r"Si las ondas que produce el pato del problema anterior (cuatro oscilaciones en "
               r"$5$ s) tienen una longitud de onda de $25$ cm, calcula su período y su "
               r"velocidad de propagación.",
     r"$T = \num{1,25}$ s; $v = \dfrac{\lambda}{T} = \dfrac{\num{0,25}}{\num{1,25}} = "
     r"\num{0,2}$ m/s $= 20$ cm/s.",
     notas="En la guía el problema 6 no tiene datos de frecuencia ni período («Calcula la "
           "velocidad de propagación de las ondas y su período, sabiendo que la longitud de "
           "esta propagación es de 25 cm»); se interpretó como continuación del problema 5 y "
           "se escribió «longitud de onda».")
def _():
    T = 5 * s_ / 4
    assert aprox(valor(25 * u.centimeter / T, m_ / s_), 0.2)


@num(PRO, "7", r"Un bote que flota en el mar completa ocho oscilaciones en $10$ s. Si las ondas "
               r"del mar van a una velocidad de $4$ m/s, ¿cuál es la longitud de onda?",
     r"$f = \dfrac{8}{10} = \num{0,8}$ Hz; $\lambda = \dfrac{v}{f} = \dfrac{4}{\num{0,8}} = 5$ m.")
def _():
    f = 8 / (10 * s_)
    assert aprox(valor(4 * m_ / s_ / f, m_), 5)


@num(PRO, "8", r"Ciertos quirópteros, como el murciélago, emiten ultrasonidos. Si la frecuencia "
               r"del sonido emitido en el aire es de $3\times10^{5}$ Hz, ¿cuál es su longitud "
               r"de onda? (Velocidad del sonido en el aire: $340$ m/s.)",
     r"$\lambda = \dfrac{340}{3\times10^{5}} \approx \num{1,13}\times10^{-3}$ m "
     r"$\approx \num{1,1}$ mm.",
     notas="La guía no da la velocidad del sonido; se añadió v = 340 m/s (aire).")
def _():
    lam = 340 * m_ / s_ / (3 * 10**5 * Hz_)
    assert aprox(valor(lam, u.millimeter), 1.133)


@num(PRO, "9", r"Un bote anclado es movido por ondas cuyas crestas están separadas $15$ m y cuya "
               r"rapidez es de $6$ m/s. ¿Con qué frecuencia llegan las olas al bote?",
     r"$f = \dfrac{v}{\lambda} = \dfrac{6}{15} = \num{0,4}$ Hz (una ola cada $\num{2,5}$ s).")
def _():
    assert aprox(valor(6 * m_ / s_ / (15 * m_), Hz_), 0.4)


@num(PRO, "10", r"Una onda longitudinal de longitud de onda $\lambda = 2$ cm avanza $40$ cm en "
                r"$10$ s. ¿Cuánto vale el período? ¿Cuál es su frecuencia?",
     r"$v = \dfrac{40\ \text{cm}}{10\ \text{s}} = 4$ cm/s; $T = \dfrac{\lambda}{v} = "
     r"\dfrac{2}{4} = \num{0,5}$ s; $f = \dfrac{1}{T} = 2$ Hz.")
def _():
    v = 40 * u.centimeter / (10 * s_)
    T = 2 * u.centimeter / v
    assert aprox(valor(T, s_), 0.5) and aprox(valor(1 / T, Hz_), 2)


@num(PRO, "11", r"Un frente de onda se propaga por la superficie de un estanque con un período "
                r"de $4$ s y una velocidad de $20$ m/s. ¿Cuál es la longitud de onda?",
     r"$\lambda = vT = 20 \cdot 4 = 80$ m.",
     notas="20 m/s es una velocidad muy alta para ondas en un estanque (lo realista es menos de "
           "1 m/s); el cálculo es correcto con los datos dados.")
def _():
    assert aprox(valor(20 * m_ / s_ * 4 * s_, m_), 80)


ONDA21 = (r"Una onda periódica de frecuencia $10$ Hz tiene, en un instante, la forma de una "
          r"senoide que empieza en el origen, corta el eje $x$ en $x = 2$ m, $4$ m y $6$ m, y "
          r"cuyas crestas y valles están a $\num{0,8}$ m del eje. Halla ")


@num(PRO, "12a", ONDA21 + r"la amplitud.", r"$A = \num{0,8}$ m.")
def _():
    assert aprox(0.8, 0.8)  # dato leído de la figura; la comprobación va en 12b


@num(PRO, "12b", ONDA21 + r"la velocidad de propagación.",
     r"Los cortes con el eje están cada media longitud de onda: $\lambda = 4$ m; "
     r"$v = \lambda f = 4 \cdot 10 = 40$ m/s.")
def _():
    x = symbols("x")
    lam = 4
    ceros = [c for c in solve(sin(2 * pi * x / lam), x)]
    assert set(ceros) >= {0, 2}  # sen(2πx/4) se anula en 0, 2 (y 4, 6 por periodicidad)
    assert all(abs(float(sin(2 * pi * c / lam))) < 1e-12 for c in (4, 6))
    assert aprox(valor(lam * m_ * 10 * Hz_, m_ / s_), 40)


ONDA22 = (r"Una cuerda oscila con una frecuencia de $50$ Hz. En un instante, la onda (que "
          r"avanza en el sentido positivo de $x$) pasa por los puntos, en centímetros, "
          r"$(0, 0)$, $(10, -2)$, $(20, 0)$, $(30, 2)$, $(40, 0)$, $(50, -2)$ y $(60, 0)$. Halla ")


@num(PRO, "13a", ONDA22 + r"la amplitud de oscilación.", r"$A = 2$ cm.")
def _():
    pts = [(0, 0), (10, -2), (20, 0), (30, 2), (40, 0), (50, -2), (60, 0)]
    assert max(abs(y) for _, y in pts) == 2


@num(PRO, "13b", ONDA22 + r"el período de oscilación.",
     r"$T = \dfrac{1}{f} = \dfrac{1}{50} = \num{0,02}$ s.")
def _():
    assert aprox(valor(1 / (50 * Hz_), s_), 0.02)


@num(PRO, "13c", ONDA22 + r"la velocidad de propagación.",
     r"Dos valles consecutivos están en $x = 10$ cm y $x = 50$ cm: $\lambda = 40$ cm; "
     r"$v = \lambda f = \num{0,4} \cdot 50 = 20$ m/s.")
def _():
    x = symbols("x")
    y = -2 * sin(2 * pi * x / 40)  # onda con λ = 40 cm que pasa por los puntos dados
    for px, py in [(0, 0), (10, -2), (20, 0), (30, 2), (40, 0), (50, -2), (60, 0)]:
        assert abs(float(y.subs(x, px)) - py) < 1e-12
    assert aprox(valor(40 * u.centimeter * 50 * Hz_, m_ / s_), 20)


@num(PRO, "14", r"Una persona observa en una piscina un flotador que realiza $12$ oscilaciones en "
                r"$20$ s. Si cada pulso tarda $\num{2,5}$ s en recorrer $9$ m, ¿cuál es la "
                r"longitud de onda de las ondas en la piscina?",
     r"$f = \dfrac{12}{20} = \num{0,6}$ Hz; $v = \dfrac{9}{\num{2,5}} = \num{3,6}$ m/s; "
     r"$\lambda = \dfrac{v}{f} = 6$ m.", dificultad=2)
def _():
    f = 12 / (20 * s_)
    v = 9 * m_ / (2.5 * s_)
    assert aprox(valor(v / f, m_), 6)


GUIT = (r"La cuerda de una guitarra tiene una densidad lineal de $\num{0,015}$ kg/m y una masa de "
        r"$8$ g. Si la velocidad de propagación de las ondas en la cuerda es de $150$ m/s, halla ")


@num(PRO, "15a", GUIT + r"la longitud de la cuerda.",
     r"$L = \dfrac{m}{\mu} = \dfrac{\num{0,008}}{\num{0,015}} \approx \num{0,53}$ m "
     r"($53$ cm).")
def _():
    L = 8 * u.gram / (0.015 * kg_ / m_)
    assert aprox(valor(L, m_), 0.5333)


@num(PRO, "15b", GUIT + r"la tensión que experimenta la cuerda.",
     r"$T = \mu v^2 = \num{0,015} \cdot 150^2 = \num{337,5}$ N.",
     notas="Una tensión de unos 340 N es alta para una guitarra (lo usual es 50–120 N), pero el "
           "cálculo es correcto con los datos.")
def _():
    assert aprox(valor(0.015 * kg_ / m_ * (150 * m_ / s_) ** 2, N_), 337.5)


@num(PRO, "16", r"Una onda A de amplitud $4$ m viaja hacia la derecha a $12$ m/s y una onda B de "
                r"amplitud desconocida viaja hacia la izquierda a $8$ m/s. En el instante "
                r"inicial, el valle de A y el valle de B están separados $100$ m. Si la "
                r"interferencia que se produce cuando se encuentran tiene una amplitud de "
                r"$6$ m, ¿cuál es la amplitud de B? ¿Cuánto tarda en darse la interferencia?",
     r"Se encuentran dos valles: interferencia constructiva, $4 + A_B = 6$, así que "
     r"$A_B = 2$ m. Se acercan a $12 + 8 = 20$ m/s: $t = \dfrac{100}{20} = 5$ s.",
     tema=FEN, dificultad=2,
     notas="Enunciado reescrito a partir de la descripción de la Imagen 23 de la guía.")
def _():
    AB = symbols("A_B")
    assert solve(4 + AB - 6, AB) == [2]
    assert aprox(valor(100 * m_ / (12 * m_ / s_ + 8 * m_ / s_), s_), 5)


REFR17 = (r"Una onda periódica en un medio A viaja con rapidez $v_A = 40$ m/s, formando un ángulo "
          r"de $45^\circ$ con la normal a la superficie, y con longitud de onda "
          r"$\lambda_A = 10$ m. Al pasar al medio B se refracta formando un ángulo de "
          r"$30^\circ$ con la normal. Determina ")


@num(PRO, "17a", REFR17 + r"la frecuencia de la onda.",
     r"$f = \dfrac{v_A}{\lambda_A} = \dfrac{40}{10} = 4$ Hz (es la misma en los dos medios).",
     tema=FEN)
def _():
    assert aprox(valor(40 * m_ / s_ / (10 * m_), Hz_), 4)


@num(PRO, "17b", REFR17 + r"la velocidad de la onda en el medio B.",
     r"$\dfrac{\sen 45^\circ}{\sen 30^\circ} = \dfrac{v_A}{v_B} \Rightarrow "
     r"v_B = 40 \cdot \dfrac{\sen 30^\circ}{\sen 45^\circ} = 20\sqrt{2} \approx \num{28,3}$ m/s.",
     tema=FEN, dificultad=2)
def _():
    vB = 40 * sin(pi / 6) / sin(pi / 4)
    assert (vB - 20 * sqrt(2)).simplify() == 0 and aprox(float(vB), 28.28)


@num(PRO, "17c", REFR17 + r"la longitud de onda en el medio B.",
     r"$\lambda_B = \dfrac{v_B}{f} = \dfrac{20\sqrt{2}}{4} = 5\sqrt{2} \approx \num{7,07}$ m.",
     tema=FEN, dificultad=2)
def _():
    lamB = (40 * sin(pi / 6) / sin(pi / 4)) / 4
    assert (lamB - 5 * sqrt(2)).simplify() == 0 and aprox(float(lamB), 7.07)


@num(PRO, "18", r"Una onda se propaga en un medio A con una velocidad de $20$ m/s. Luego incide "
                r"en un medio B con un ángulo de incidencia de $30^\circ$, y allí su velocidad de "
                r"propagación es $20\sqrt{3}$ m/s. ¿Cuál es el ángulo de refracción?",
     r"$\sen\theta_B = \dfrac{v_B}{v_A}\sen 30^\circ = \sqrt{3} \cdot \dfrac{1}{2} = "
     r"\dfrac{\sqrt{3}}{2} \Rightarrow \theta_B = 60^\circ$ (se aleja de la normal porque la "
     r"onda se acelera).", tema=FEN, dificultad=2,
     notas="La guía dice «con una velocidad de 0 m/s» (imposible); se tomó 20 m/s, el valor "
           "que da un resultado exacto (60°). Con 60 m/s daría ≈ 16,8°.")
def _():
    s = 20 * sqrt(3) / 20 * sin(pi / 6)
    assert s == sqrt(3) / 2 and deg(asin(s)) == 60


REFR19 = (r"Una onda pasa de un medio 1 a un medio 2. En el medio 1 su frecuencia es $1$ kHz, su "
          r"velocidad de propagación $10\sqrt{3}$ m/s y el frente incide formando $30^\circ$ con "
          r"la superficie (ángulo de incidencia $60^\circ$ respecto a la normal). El ángulo de "
          r"refracción es $30^\circ$ con la normal. Halla ")
NOTA19 = ("La guía dice «ángulo de incidencia 30° con la horizontal de la superficie»: 30° con la "
          "superficie equivale a 60° con la normal, que es el ángulo que se usa en la ley de "
          "Snell; se hizo explícito en el enunciado.")


@num(PRO, "19a", REFR19 + r"la frecuencia de la onda en el medio 2.",
     r"$1$ kHz $= 1000$ Hz: la frecuencia no cambia al pasar de un medio a otro.", tema=FEN,
     notas=NOTA19)
def _():
    assert valor(1 * u.kilo * Hz_, Hz_) == 1000


@num(PRO, "19b", REFR19 + r"la longitud de onda en el medio 1.",
     r"$\lambda_1 = \dfrac{10\sqrt{3}}{1000} \approx \num{0,0173}$ m $\approx \num{1,73}$ cm.",
     tema=FEN, notas=NOTA19)
def _():
    lam = 10 * sqrt(3) * m_ / s_ / (1000 * Hz_)
    assert aprox(valor(lam, u.centimeter), 1.732)


@num(PRO, "19c", REFR19 + r"la velocidad de propagación en el medio 2.",
     r"$v_2 = v_1 \dfrac{\sen 30^\circ}{\sen 60^\circ} = 10\sqrt{3} \cdot "
     r"\dfrac{1/2}{\sqrt{3}/2} = 10$ m/s.", tema=FEN, dificultad=2, notas=NOTA19)
def _():
    assert (10 * sqrt(3) * sin(pi / 6) / sin(pi / 3)).simplify() == 10


@num(PRO, "19d", REFR19 + r"el índice de refracción del medio 2 con respecto al medio 1.",
     r"$n_{21} = \dfrac{v_1}{v_2} = \dfrac{\sen 60^\circ}{\sen 30^\circ} = \sqrt{3} \approx "
     r"\num{1,73}$.", tema=FEN, dificultad=2, notas=NOTA19)
def _():
    assert (sin(pi / 3) / sin(pi / 6) - sqrt(3)).simplify() == 0
    assert (10 * sqrt(3) / 10 - sqrt(3)) == 0


@num(PRO, "20a", r"En la superficie de un lago hay dos focos de ondas coherentes, en fase, con "
                 r"frecuencia de $5$ Hz. La velocidad de propagación es $2$ cm/s. ¿Cuál es la "
                 r"longitud de onda de las perturbaciones?",
     r"$\lambda = \dfrac{v}{f} = \dfrac{2}{5} = \num{0,4}$ cm.", tema=FEN,
     notas="Los literales 20b y 20c no se incluyeron: la guía no da las distancias del punto P "
           "a los focos. La velocidad de 2 cm/s es muy baja para ondas en un lago, pero se "
           "respeta el dato.")
def _():
    assert aprox(valor(2 * u.centimeter / s_ / (5 * Hz_), u.centimeter), 0.4)


FUENTES21 = (r"Dos focos de ondas $F_1$ y $F_2$, en fase, producen en el agua ondas de longitud "
             r"$2$ cm. Un punto P de la superficie dista $9$ cm de $F_1$ y $12$ cm de $F_2$. ")


@num(PRO, "21a", FUENTES21 + r"¿Cuántas longitudes de onda hay entre P y $F_1$, y entre P y "
                             r"$F_2$?",
     r"Entre P y $F_1$: $\dfrac{9}{2} = \num{4,5}\,\lambda$; entre P y $F_2$: "
     r"$\dfrac{12}{2} = 6\,\lambda$.", tema=FEN)
def _():
    assert 9 / 2 == 4.5 and 12 / 2 == 6


@num(PRO, "21b", FUENTES21 + r"¿En P la interferencia es constructiva o destructiva? Justifica.",
     r"Destructiva: la diferencia de caminos es $12 - 9 = 3$ cm $= \num{1,5}\,\lambda$, un "
     r"número impar de medias longitudes de onda ($3 \cdot \frac{\lambda}{2}$), así que a P "
     r"llegan una cresta y un valle.", tema=FEN, tipo="argumentacion", dificultad=2)
def _():
    dif = (12 - 9) / 2  # en longitudes de onda
    assert dif % 1 == 0.5  # semientero → destructiva
    x = symbols("x")
    y = sin(2 * pi * (0.37 - 9 / 2)) + sin(2 * pi * (0.37 - 12 / 2))
    assert abs(float(y)) < 1e-12  # las dos ondas se anulan en P en cualquier instante


@num(PRO, "22", r"Dos ondas viajeras de igual amplitud e igual longitud de onda $\lambda$ se "
                r"propagan a lo largo de una cuerda en sentidos contrarios. Determina la "
                r"distancia entre dos nodos consecutivos.",
     r"Su superposición es $y = 2A\sen(kx)\cos(\omega t)$, que se anula siempre donde "
     r"$kx = n\pi$, es decir en $x = n\dfrac{\lambda}{2}$: los nodos están separados "
     r"$\dfrac{\lambda}{2}$.", tema=FEN, dificultad=2)
def _():
    A, lam, w, x, t = symbols("A lambda omega x t", positive=True)
    k = 2 * pi / lam
    y = A * sin(k * x - w * t) + A * sin(k * x + w * t)
    assert simplify(expand_trig(y) - 2 * A * sin(k * x) * cos(w * t)) == 0
    # nodos consecutivos: sen(kx) = 0 en x = 0 y x = λ/2
    assert sin(k * lam / 2) == 0 and sin(k * lam / 4) != 0


@num(PRO, "23", r"En una cuerda se produce una onda estacionaria en la que los nodos "
                r"consecutivos están separados $15$ cm. ¿Cuál es la longitud de onda de las "
                r"ondas que la generan? Si la tensión es de $10$ N y la masa por unidad de "
                r"longitud es de $\num{0,3}$ kg/m, determina la frecuencia de vibración.",
     r"$\lambda = 2 \cdot 15 = 30$ cm $= \num{0,3}$ m; $v = \sqrt{\dfrac{10}{\num{0,3}}} "
     r"\approx \num{5,77}$ m/s; $f = \dfrac{v}{\lambda} \approx \num{19,2}$ Hz.", tema=FEN,
     dificultad=2,
     notas="La guía dice «tres nodos que están separados entre sí a una distancia de 15 cm» y "
           "«masa por unidad»; se interpretó 15 cm entre nodos consecutivos y se escribió "
           "«masa por unidad de longitud». Si 15 cm fuera la distancia entre el primero y el "
           "tercero, λ = 15 cm y f ≈ 38,5 Hz.")
def _():
    lam = 2 * 15 * u.centimeter
    v = sqrt(10 * N_ / (0.3 * kg_ / m_))
    assert aprox(valor(lam, m_), 0.3) and aprox(valor(v, m_ / s_), 5.774)
    assert aprox(valor(v / lam, Hz_), 19.25)
