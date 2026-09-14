"""Banco de ejercicios — Física 11° — Electrostática.
Fuente: Guía de Apoyo «Fenómenos electromagnéticos» grado 11 (Ciencias Naturales), Capítulo 1:
electrostática — secciones «Desarrolla tus competencias», «Actividades» y «Problemas»; se lee en
recursos/fisica/Guías pedagógicas Física/markdown/11 - Guia_de_Apoyo_Fenomenos_electromagneticos_grado_11_fisica.md
La guía no trae clave: las respuestas se calcularon y se comprueban aquí (k = coulomb_constant de
sympy ≈ 8,99·10^9 N·m²/C²; e = elementary_charge; G = gravitational_constant).

No se incluyeron (dependen de una figura que la guía no describe):
  Problemas 14 (campo en P1 y P2) y 18 (diferencia de potencial entre los puntos 1 y 2).
Correcciones (detalle en `notas`): Problemas 3, 4, 8 y 9 (cargas de culombios o milicoulombs,
irreales → microcoulombs), 12 (no decía dónde se pide el campo → punto medio), 17 (pregunta
ambigua → potencial que crea una carga donde está la otra); Actividades 10 (no tenía pregunta).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/fisica/electrostatica-11.py
"""
from sympy import Rational, sqrt, symbols, Matrix, simplify
from sympy.physics import units as u
from sympy.physics.units import convert_to

from ejercicios import ejercicio, ejercicio_manual

GUIA = "Guía de Apoyo Fenómenos electromagnéticos 11°, Capítulo 1: electrostática"
TEMA = "electrostática"
DBA = ["naturales-11-2"]
COMUN = dict(tema=TEMA, grados=[11], dba=DBA)

k = u.coulomb_constant
e = u.elementary_charge
G = u.gravitational_constant
N, C, m, V = u.newton, u.coulomb, u.meter, u.volt
uC = 10**-6 * C


def valor(q, unidad):
    """Número que acompaña a `unidad` al expresar la cantidad q en ella."""
    return float(convert_to(q, unidad) / unidad)


def aprox(a, b, rel=0.01):
    return abs(a - b) <= rel * abs(b)


def opciones(*items):
    return r" \begin{opciones} " + " ".join(r"\item " + i for i in items) + r" \end{opciones}"


def fuente(ref):
    return f"{GUIA}, {ref}"


def manual(n, ref, enunciado, respuesta, tipo="conceptual", dificultad=1, notas=None):
    extra = {"notas": notas} if notas else {}
    ejercicio_manual(id=f"electrostatica-11-{n:03d}", tipo=tipo, dificultad=dificultad,
                     fuente=fuente(ref), enunciado=enunciado, respuesta=respuesta,
                     **COMUN, **extra)


def vf(n, ref, afirmacion, verdadera, justificacion, notas=None):
    manual(n, ref, r"Escribe V si la afirmación es verdadera o F si es falsa, y justifica tu "
                   r"respuesta: «" + afirmacion + "»",
           ("V. " if verdadera else "F. ") + justificacion, tipo="argumentacion", notas=notas)


# ---------- Desarrolla tus competencias ----------
DC = "Desarrolla tus competencias — "

manual(1, DC + "1", r"La propiedad que poseen algunos cuerpos de atraer a otros cuerpos después "
       r"de ser frotados se denomina:" + opciones("Inducción eléctrica.", "Carga eléctrica.",
                                                  "Fuerza eléctrica.", "Magnetismo."),
       r"b. Al frotarlos, los cuerpos adquieren carga eléctrica (se electrizan), y es esa carga "
       r"la que les permite atraer otros cuerpos.", tipo="seleccion")
manual(2, DC + "2", r"Un electroscopio es un dispositivo para:" + opciones(
    "Transferir constantemente corriente.", "Distribuir electricidad sobre cualquier objeto.",
    "Evidenciar la presencia de cargas eléctricas.", "Generar carga eléctrica."),
       r"c. Sus láminas se separan cuando el electroscopio recibe carga: detecta cargas, no "
       r"las genera.", tipo="seleccion")
manual(3, DC + "3", r"En la ley de Coulomb se cumple que:" + opciones(
    "La fuerza eléctrica es inversamente proporcional a las cargas eléctricas.",
    "La fuerza eléctrica es directamente proporcional a la distancia entre las cargas.",
    "Cuanto más grandes sean los objetos cargados, mayor es la fuerza eléctrica que se ejerce "
    "sobre ellos.",
    "La fuerza eléctrica es inversamente proporcional al cuadrado de la distancia entre las "
    "cargas."),
       r"d. $F = k\dfrac{q_1 q_2}{r^2}$: es directamente proporcional al producto de las cargas "
       r"e inversamente proporcional a $r^2$; el tamaño de los objetos no interviene.",
       tipo="seleccion")
manual(4, DC + "4", r"La constante dieléctrica $k_d$:" + opciones(
    "Caracteriza si la fuerza es de atracción o repulsión.",
    "Determina la energía por unidad de carga que tiene el sistema.",
    "Caracteriza el medio material donde se encuentra el campo.",
    "Representa el espacio donde hay presencia de cargas eléctricas."),
       r"c. Depende del medio: en él la fuerza entre las cargas es $k_d$ veces menor que en el "
       r"vacío.", tipo="seleccion")
manual(5, DC + "5", r"¿Qué tipo de carga eléctrica posee un cuerpo que tiene más electrones que "
       r"protones? ¿Por qué?",
       r"Carga negativa: la carga de cada electrón es negativa y la de cada protón positiva, de "
       r"igual valor; si hay más electrones, la carga neta es negativa.")


@ejercicio(id="electrostatica-11-006", tipo="calculo", dificultad=1, fuente=fuente(DC + "6"),
           enunciado=r"Si al frotar con lana un globo inflado, el globo gana dos millones de "
                     r"electrones, ¿de qué signo es la carga adquirida por la lana y por el "
                     r"globo? ¿Cuánta carga adquiere el globo?",
           respuesta=r"El globo queda con carga negativa (ganó electrones) y la lana con carga "
                     r"positiva (los perdió), de igual valor: "
                     r"$q_{\text{globo}} = -2\times10^{6}\cdot\num{1,6}\times10^{-19}\ \text{C} "
                     r"\approx -\num{3,2}\times10^{-13}$ C y $q_{\text{lana}} \approx "
                     r"+\num{3,2}\times10^{-13}$ C.",
           notas="Se añadió la pregunta «¿cuánta carga adquiere el globo?» para practicar la "
                 "cuantización de la carga.", **COMUN)
def _():
    q_globo = -2 * 10**6 * e
    assert aprox(valor(q_globo, C), -3.2e-13)
    assert valor(-q_globo, C) > 0          # la lana queda positiva: conservación de la carga


manual(7, DC + "7", r"¿Por qué se plantea que la fuerza electrostática que existe entre dos "
       r"cargas es directamente proporcional al producto de las cargas que interactúan?",
       r"Porque los experimentos (balanza de torsión de Coulomb) muestran que si se duplica una "
       r"de las cargas la fuerza se duplica, y si se duplican las dos se cuadruplica. Además, "
       r"la fuerza que cada carga ejerce sobre la otra debe ser igual (tercera ley de Newton), "
       r"lo que exige que las dos cargas entren en la fórmula de la misma manera: como "
       r"producto $q_1 q_2$. El producto da además el signo: positivo (repulsión) si son del "
       r"mismo signo, negativo (atracción) si son de signo contrario.", tipo="argumentacion",
       dificultad=2)
manual(8, DC + "8", r"¿Habrá alguna disposición de cargas que logre crear superficies "
       r"equipotenciales que se crucen? Justifica tu respuesta.",
       r"No. En cada punto el potencial tiene un único valor, así que un punto no puede estar "
       r"en dos superficies de potencial distinto. Además, el campo eléctrico es perpendicular "
       r"a la superficie equipotencial: en un cruce habría dos direcciones de campo en el mismo "
       r"punto, lo cual es imposible (en un punto donde el campo es nulo, como el punto medio "
       r"entre dos cargas iguales, una misma equipotencial puede cortarse a sí misma, pero dos "
       r"superficies de distinto potencial nunca se cruzan).", tipo="argumentacion",
       dificultad=3,
       notas="En la guía: «Propón una solución a la situación planteada»; se cambió por "
             "«Justifica tu respuesta».")

ESTATICA = (r"Cuando una persona toca a otra que estaba cargada de electricidad estática, es "
            r"posible que esta se descargue hacia el suelo a través de la persona, produciéndole "
            r"una molesta sensación de contacto eléctrico que, en pequeñas cantidades, no causa "
            r"gran daño. ")
manual(9, DC + "9a", ESTATICA + r"¿Por qué es importante evitar la concentración de "
       r"electricidad estática?",
       r"Porque al acumularse mucha carga la descarga puede producir chispas, que pueden "
       r"encender gases o polvos inflamables, dañar equipos electrónicos o causar choques "
       r"eléctricos.")
manual(10, DC + "9b", ESTATICA + r"¿En qué tipos de ambientes la electricidad estática "
       r"constituye un grave peligro?",
       r"Donde hay sustancias inflamables o explosivas (estaciones de gasolina, depósitos de "
       r"combustible, minas con gas, fábricas de harinas o pólvora, quirófanos con gases "
       r"anestésicos) y donde se manejan componentes electrónicos sensibles.")
manual(11, DC + "9c", ESTATICA + r"¿Qué recomendaciones darías para prevenir daños por "
       r"transferencia de cargas estáticas?",
       r"Conectar a tierra los equipos y los tanques; tocar un objeto metálico conectado a "
       r"tierra antes de manipular combustibles o circuitos; usar pulseras y calzado "
       r"antiestáticos; mantener una humedad adecuada en el ambiente; evitar ropa sintética en "
       r"ambientes de riesgo.")

# ---------- Actividades ----------
AC = "Actividades — "
vf(12, AC + "1a", "La electrización consiste en hacer que un objeto pueda atraer a otros "
   "después de ser frotado.", True,
   r"Al frotarlo, el objeto gana o pierde electrones y queda cargado; por eso atrae objetos "
   r"livianos (aunque también se electriza por contacto o por inducción, sin frotar).")
vf(13, AC + "1b", "Un cuerpo está cargado positivamente cuando tiene un exceso de electrones.",
   False, r"Con exceso de electrones queda cargado negativamente; la carga positiva corresponde "
          r"a un defecto de electrones.")
vf(14, AC + "1c", "Cuando se encuentran dos cargas de diferente signo, una cerca de la otra, se "
   "dice que hay una interacción de atracción.", True,
   r"Cargas de signo contrario se atraen; las del mismo signo se repelen.")
vf(15, AC + "1d", "En un sistema aislado, la carga eléctrica no se crea ni se destruye, solo se "
   "transfiere de un cuerpo a otro.", True, r"Es el principio de conservación de la carga.")
vf(16, AC + "1e", "Un material aislante es aquel que permite el paso de electrones sobre él.",
   False, r"Eso describe un conductor; en un aislante los electrones no se mueven libremente.")
vf(17, AC + "1f", "Las fuerzas eléctricas aparecen sobre cada una de las cargas que "
   "interactúan y son de igual magnitud e igual línea de acción, pero en sentidos opuestos.",
   True, r"Es un par de acción y reacción (tercera ley de Newton), como muestra la ley de "
         r"Coulomb.")
vf(18, AC + "1g", "La constante electrostática $k$ no varía en ningún medio donde hay "
   "presencia de cargas eléctricas.", False,
   r"En un medio material la constante efectiva es $k/k_d$, donde $k_d$ es la constante "
   r"dieléctrica del medio: la fuerza es menor que en el vacío.")
manual(19, AC + "2", r"Escribe una lista de algunos fenómenos relacionados con las cargas "
       r"eléctricas.",
       r"Por ejemplo: los rayos; el cabello que se levanta al peinarlo; el globo frotado que se "
       r"pega a la pared; la chispa al tocar una manija metálica; la ropa que se pega al "
       r"sacarla de la secadora; el funcionamiento de fotocopiadoras e impresoras láser.")

MATERIALES = [("a", "agua", "conductor",
               "El agua común conduce por los iones disueltos (el agua pura es mala conductora)."),
              ("b", "aire", "aislante", "Salvo cuando se ioniza, como en un rayo."),
              ("c", "plástico", "aislante", None), ("d", "aluminio", "conductor", None),
              ("e", "cobre", "conductor", None), ("f", "plata", "conductor", None),
              ("g", "vidrio", "aislante", None), ("h", "cartón", "aislante", None),
              ("i", "mármol", "aislante", None), ("j", "oro", "conductor", None)]
for i, (lit, mat, tipo_mat, extra) in enumerate(MATERIALES):
    manual(20 + i, AC + "3" + lit, rf"Clasifica el material como conductor o aislante: {mat}.",
           f"{tipo_mat.capitalize()}." + (f" {extra}" if extra else ""), tipo="conceptual")

manual(30, AC + "4", r"Un cuerpo se carga positivamente:" + opciones(
    "Al agregarle protones.", "Al quitarle protones.", "Al agregarle electrones.",
    "Al quitarle electrones."),
       r"d. Los protones están fijos en los núcleos; solo se transfieren electrones, y al "
       r"perderlos el cuerpo queda con carga positiva.", tipo="seleccion")
manual(31, AC + "5", r"¿Cuál de las partículas que componen el átomo tiene menor masa?"
       + opciones("El electrón.", "El neutrón.", "El protón.", "El núcleo."),
       r"a. La masa del electrón ($\num{9,11}\times10^{-31}$ kg) es unas 1836 veces menor que "
       r"la del protón.", tipo="seleccion")
manual(32, AC + "6", r"El científico que inventó la balanza de torsión es:" + opciones(
    "Michael Faraday.", "Charles Coulomb.", "Charles du Fay.", "William Gilbert."),
       r"b. Charles-Augustin de Coulomb la usó para medir la fuerza entre cargas (1785).",
       tipo="seleccion")
manual(33, AC + "7", r"Una carga eléctrica positiva se obtiene al frotar:" + opciones(
    "Vidrio y vidrio.", "Vidrio y seda.", "Vidrio y metal.", "Seda y metal."),
       r"b. Al frotar vidrio con seda, el vidrio cede electrones a la seda y queda cargado "
       r"positivamente.", tipo="seleccion")

vf(34, AC + "8a", "La dirección del campo eléctrico coincide con la de la fuerza que actúa "
   "sobre la carga de prueba.", True,
   r"La carga de prueba es positiva por convenio y $\vec F = q\vec E$ (para una carga negativa "
   r"la fuerza tendría sentido contrario al campo).")
vf(35, AC + "8b", "La unidad de intensidad del campo eléctrico es V/C.", False,
   r"Es N/C, que equivale a V/m.")
vf(36, AC + "8c", "En un punto del espacio, el vector campo eléctrico es tangente a la línea "
   "de fuerza que pasa por ahí.", True, r"Así se definen las líneas de fuerza.")
vf(37, AC + "8d", "Cuanto menor es la carga eléctrica, mayor es la energía potencial asociada "
   "a esa carga.", False,
   r"La energía potencial $U = qV$ es proporcional a la carga: en el mismo punto, a menor "
   r"carga (en valor absoluto) menor energía potencial.")
vf(38, AC + "8e", "Una superficie equipotencial contiene un conjunto de puntos al mismo "
   "potencial.", True, r"Es la definición de superficie equipotencial.")
vf(39, AC + "8f", "El campo eléctrico en el interior de un conductor es igual al que hay en la "
   "superficie.", False,
   r"En equilibrio electrostático el campo es nulo en el interior de un conductor; en la "
   r"superficie es perpendicular a ella y, en general, distinto de cero.")
vf(40, AC + "8g", "El campo eléctrico en el interior de un conductor es igual a cero.", True,
   r"En equilibrio electrostático las cargas libres se redistribuyen en la superficie hasta "
   r"anular el campo interior (blindaje electrostático).")
manual(41, AC + "9", r"El trabajo requerido para mover una carga de un lugar a otro dividido "
       r"entre el valor de la carga se llama:" + opciones(
           "Campo eléctrico.", "Fuerza eléctrica.", "Potencial eléctrico.", "Carga eléctrica."),
       r"c. La diferencia de potencial es $\Delta V = W/q$, en J/C = V.", tipo="seleccion")
manual(42, AC + "10", r"En algunas recomendaciones de uso de los electrodomésticos se indica "
       r"que no se deben colocar juntos varios aparatos eléctricos, porque «se generan campos "
       r"eléctricos que pueden afectar su funcionamiento». ¿Es correcta esa explicación? "
       r"Justifica tu respuesta.",
       r"Solo en parte. Los aparatos producen campos eléctricos y, sobre todo, campos "
       r"magnéticos variables (transformadores, motores) que pueden causar interferencias en "
       r"equipos sensibles como radios, televisores o parlantes; pero la razón principal de la "
       r"recomendación suele ser otra: el calor que desprenden y la sobrecarga de un mismo "
       r"tomacorriente o extensión, que puede recalentar los cables.",
       tipo="argumentacion", dificultad=2,
       notas="En la guía el literal es solo una afirmación, sin pregunta; se añadió «¿Es "
             "correcta esa explicación? Justifica tu respuesta».")
manual(43, AC + "11", r"Explica cómo puedes verificar si alrededor de un televisor hay un campo "
       r"eléctrico.",
       r"Acercando una carga de prueba: un electroscopio (sus láminas se separan), un péndulo "
       r"electrostático (una bolita liviana colgada de un hilo que se desvía) o pedacitos de "
       r"papel o el vello del brazo, que se atraen o se erizan cerca de la pantalla (efecto "
       r"muy notorio en los televisores antiguos de tubo).")


@ejercicio(id="electrostatica-11-044", tipo="calculo", dificultad=2, fuente=fuente(AC + "12"),
           enunciado=r"Una carga puntual produce, a cierta distancia $r$, un potencial "
                     r"eléctrico de $10$ V y un campo eléctrico de módulo $E$. ¿Cuánto vale el "
                     r"potencial eléctrico en otro punto donde el campo eléctrico es $E/4$?",
           respuesta=r"$E = kq/r^2$: si el campo es la cuarta parte, la distancia es el doble, "
                     r"$2r$. Como $V = kq/r$, el potencial es la mitad: $5$ V.", **COMUN)
def _():
    q, r, r2 = symbols("q r r2", positive=True)
    E = lambda d: q / d**2      # k se simplifica
    Vp = lambda d: q / d
    from sympy import solve
    d = [s for s in solve(E(r2) - E(r) / 4, r2) if s.is_positive]
    assert d == [2 * r]
    assert simplify(10 * Vp(d[0]) / Vp(r)) == 5


manual(45, AC + "13", r"En una región del espacio el campo eléctrico es nulo. ¿Debe ser nulo "
       r"también el potencial eléctrico en dicha región? Explica tu respuesta.",
       r"No. Que el campo sea nulo significa que el potencial no cambia de un punto a otro "
       r"(no se hace trabajo al mover una carga): el potencial es constante, pero puede tener "
       r"cualquier valor. Por ejemplo, dentro de una esfera conductora cargada $E = 0$ y el "
       r"potencial es igual al de su superficie, $V = kQ/R \ne 0$.", tipo="argumentacion",
       dificultad=2)

# ---------- Problemas ----------
PR = "Problemas — "
q1, q2, r = symbols("q_1 q_2 r", positive=True)
F = lambda a, b, d: a * b / d**2      # proporcionalidad de Coulomb (k se simplifica)


@ejercicio(id="electrostatica-11-046", tipo="calculo", dificultad=1, fuente=fuente(PR + "1a"),
           enunciado=r"Dos esferas se atraen con una fuerza determinada. ¿Cómo se ve afectado "
                     r"el valor de la fuerza si se triplica el valor de la carga de cada esfera?",
           respuesta=r"$F' = k\dfrac{(3q_1)(3q_2)}{r^2} = 9F$: la fuerza se hace nueve veces "
                     r"mayor.", **COMUN)
def _():
    assert simplify(F(3 * q1, 3 * q2, r) / F(q1, q2, r)) == 9


@ejercicio(id="electrostatica-11-047", tipo="calculo", dificultad=1, fuente=fuente(PR + "1b"),
           enunciado=r"Dos esferas se atraen con una fuerza determinada. ¿Qué sucede con la "
                     r"fuerza si la carga de cada esfera se reduce a la tercera parte?",
           respuesta=r"$F' = k\dfrac{(q_1/3)(q_2/3)}{r^2} = \dfrac{F}{9}$: la fuerza se reduce "
                     r"a la novena parte.", **COMUN)
def _():
    assert simplify(F(q1 / 3, q2 / 3, r) / F(q1, q2, r)) == Rational(1, 9)


@ejercicio(id="electrostatica-11-048", tipo="contexto", dificultad=3, fuente=fuente(PR + "2"),
           enunciado=r"Calcula la carga que deberían tener la Tierra y la Luna (la misma carga "
                     r"cada una) para que la fuerza de repulsión eléctrica entre ellas igualara "
                     r"la fuerza gravitatoria. Datos: $M_T = 6\times10^{24}$ kg; "
                     r"$M_L = \num{7,4}\times10^{22}$ kg; $d_{T,L} = \num{384400}$ km; "
                     r"$G = \num{6,67}\times10^{-11}\ \text{N·m}^2/\text{kg}^2$.",
           respuesta=r"$k\dfrac{q^2}{d^2} = G\dfrac{M_T M_L}{d^2} \Rightarrow "
                     r"q = \sqrt{\dfrac{G M_T M_L}{k}} \approx \num{5,7}\times10^{13}$ C. La "
                     r"distancia se simplifica: el resultado no depende de ella.",
           notas="Se precisó «la misma carga cada una» (sin eso el problema tiene infinitas "
                 "soluciones) y se añadió el valor de G.", **COMUN)
def _():
    MT, ML, d = 6e24 * u.kilogram, 7.4e22 * u.kilogram, 384400 * u.kilometer
    q = sqrt(G * MT * ML / k)
    assert aprox(valor(q, C), 5.7e13)
    # comprobación: con esa carga las dos fuerzas son iguales
    assert aprox(valor(k * q**2 / d**2, N), valor(G * MT * ML / d**2, N), 1e-9)


@ejercicio(id="electrostatica-11-049", tipo="calculo", dificultad=1, fuente=fuente(PR + "3"),
           enunciado=r"Calcula las fuerzas que ejerce una carga de $5\ \mu$C sobre otras dos "
                     r"cargas de $2\ \mu$C y $1\ \mu$C, situadas cada una a $3$ m de ella.",
           respuesta=r"$F_1 = k\dfrac{(5\times10^{-6})(2\times10^{-6})}{3^2} \approx "
                     r"\num{1,0}\times10^{-2}$ N y $F_2 = k\dfrac{(5\times10^{-6})"
                     r"(1\times10^{-6})}{3^2} \approx \num{5,0}\times10^{-3}$ N, ambas de "
                     r"repulsión.",
           notas="En la guía las cargas son de 2 C y 1 C (≈ 10^4 N y 5·10^3 N, cargas "
                 "irreales); se cambiaron a microcoulombs y se precisó que ambas están a 3 m.",
           **COMUN)
def _():
    F1 = k * 5 * uC * 2 * uC / (3 * m)**2
    F2 = k * 5 * uC * 1 * uC / (3 * m)**2
    assert aprox(valor(F1, N), 1.0e-2) and aprox(valor(F2, N), 5.0e-3)


@ejercicio(id="electrostatica-11-050", tipo="calculo", dificultad=1, fuente=fuente(PR + "4"),
           enunciado=r"Un cuerpo de masa $\num{0,5}$ kg y carga $\num{0,5}\ \mu$C se encuentra "
                     r"a $2$ m de otro cuerpo de masa $\num{1,5}$ kg y carga "
                     r"$\num{1,5}\ \mu$C. Determina si se atraen o se repelen y calcula la "
                     r"fuerza electrostática.",
           respuesta=r"Las dos cargas son positivas: se repelen. "
                     r"$F = k\dfrac{(\num{0,5}\times10^{-6})(\num{1,5}\times10^{-6})}{2^2} "
                     r"\approx \num{1,7}\times10^{-3}$ N. Las masas no intervienen en la fuerza "
                     r"eléctrica.",
           notas="En la guía las cargas son de 0,5 C y 1,5 C (F ≈ 1,7·10^9 N, irreal); se "
                 "cambiaron a microcoulombs.", **COMUN)
def _():
    Fe = k * Rational(1, 2) * uC * Rational(3, 2) * uC / (2 * m)**2
    assert aprox(valor(Fe, N), 1.7e-3)
    Fg = G * Rational(1, 2) * u.kilogram * Rational(3, 2) * u.kilogram / (2 * m)**2
    assert valor(Fg, N) < 1e-6 * valor(Fe, N)     # la gravitación es despreciable


@ejercicio(id="electrostatica-11-051", tipo="calculo", dificultad=2, fuente=fuente(PR + "5"),
           enunciado=r"Una barra de vidrio A inicialmente neutra es frotada con seda y pierde "
                     r"$1\times10^{13}$ electrones; otra barra de vidrio idéntica, B, también es "
                     r"frotada y pierde $3\times10^{13}$ electrones. Si ambas barras se ponen en "
                     r"contacto y después quedan con igual cantidad de carga, ¿cuál es el "
                     r"déficit de electrones de cada barra después del contacto?",
           respuesta=r"El déficit total, $4\times10^{13}$ electrones, se reparte por igual: "
                     r"cada barra queda con un déficit de $2\times10^{13}$ electrones "
                     r"($q \approx +\num{3,2}\times10^{-6}$ C cada una).",
           notas="La guía escribe 10 × 10^12 y 30 × 10^12; se pasó a notación científica.",
           **COMUN)
def _():
    total = 10 * 10**12 + 30 * 10**12
    assert total / 2 == 2 * 10**13
    assert aprox(valor(total / 2 * e, C), 3.2e-6)


@ejercicio(id="electrostatica-11-052", tipo="calculo", dificultad=2, fuente=fuente(PR + "6"),
           enunciado=r"Un electroscopio está cargado negativamente con un exceso de "
                     r"$2\times10^{13}$ electrones; otro electroscopio idéntico ha sido cargado "
                     r"positivamente y tiene un déficit de $\num{1,2}\times10^{13}$ electrones. "
                     r"Si los electroscopios se ponen en contacto, ¿cuántos electrones se "
                     r"transfieren?",
           respuesta=r"La carga neta es de $2\times10^{13} - \num{1,2}\times10^{13} = "
                     r"8\times10^{12}$ electrones en exceso, y cada electroscopio queda con "
                     r"$4\times10^{12}$. El negativo pasa de $2\times10^{13}$ a $4\times10^{12}$: "
                     r"transfiere $\num{1,6}\times10^{13}$ electrones al otro.", **COMUN)
def _():
    a, b = -20 * 10**12, 12 * 10**12        # carga en unidades de e (exceso = negativo)
    final = (a + b) / 2
    assert final == -4 * 10**12
    assert final - a == 16 * 10**12 and b - final == 16 * 10**12


@ejercicio(id="electrostatica-11-053", tipo="argumentacion", dificultad=2,
           fuente=fuente(PR + "7"),
           enunciado=r"¿Cuál de las siguientes cargas no concuerda con la realidad? Considera "
                     r"$q_1 = \num{2,4}\times10^{-19}$ C y $q_2 = \num{11,2}\times10^{-19}$ C. "
                     r"Justifica con el valor de la carga del electrón, "
                     r"$e = \num{1,6}\times10^{-19}$ C.",
           respuesta=r"Toda carga es un múltiplo entero de $e$. $q_2/e = 7$: es posible "
                     r"(7 electrones). $q_1/e = \num{1,5}$: no es entero, así que $q_1$ no "
                     r"concuerda con la realidad.", **COMUN)
def _():
    n1 = valor(2.4e-19 * C / e, 1)
    n2 = valor(11.2e-19 * C / e, 1)
    assert abs(n2 - 7) < 0.02 and abs(n1 - round(n1)) > 0.4


@ejercicio(id="electrostatica-11-054", tipo="calculo", dificultad=2, fuente=fuente(PR + "8"),
           enunciado=r"Dos cargas de $40\ \mu$C se repelen con una fuerza de $360$ N. Calcula "
                     r"la distancia que las separa.",
           respuesta=r"$r = \sqrt{\dfrac{k q^2}{F}} = \sqrt{\dfrac{(\num{8,99}\times10^{9})"
                     r"(40\times10^{-6})^2}{360}} \approx \num{0,20}$ m $= 20$ cm.",
           notas="En la guía las cargas son de 40 mC (daría r ≈ 200 m, cargas irreales); se "
                 "cambió a 40 μC.", **COMUN)
def _():
    dist = sqrt(k * (40 * uC)**2 / (360 * N))
    assert aprox(valor(dist, m), 0.20)


@ejercicio(id="electrostatica-11-055", tipo="calculo", dificultad=1, fuente=fuente(PR + "9"),
           enunciado=r"Se tienen dos cargas de $2\ \mu$C y $8\ \mu$C separadas por una "
                     r"distancia de $10$ cm. Calcula la fuerza, en newtons, que existe entre "
                     r"ellas.",
           respuesta=r"$F = k\dfrac{(2\times10^{-6})(8\times10^{-6})}{(\num{0,1})^2} \approx "
                     r"\num{14,4}$ N, de repulsión.",
           notas="En la guía las cargas son de 2 C y 8 C (F ≈ 1,4·10^13 N, irreal); se "
                 "cambiaron a microcoulombs.", **COMUN)
def _():
    assert aprox(valor(k * 2 * uC * 8 * uC / (10 * u.centimeter)**2, N), 14.4)


@ejercicio(id="electrostatica-11-056", tipo="argumentacion", dificultad=1,
           fuente=fuente(PR + "10"),
           enunciado=r"¿Cuál de las siguientes situaciones da como resultado una mayor fuerza, "
                     r"si la distancia entre las cargas es la misma? ¿Por qué? "
                     r"\begin{enumerate}[a.] \item La fuerza de repulsión que ejerce una carga "
                     r"de $100\ \mu$C sobre una de $1\ \mu$C. \item La fuerza de repulsión que "
                     r"ejerce una carga de $1\ \mu$C sobre una de $100\ \mu$C. \end{enumerate}",
           respuesta=r"Ninguna: las dos fuerzas tienen el mismo valor, $F = k\dfrac{q_1 q_2}"
                     r"{r^2}$ con el mismo producto $q_1 q_2$. Son un par de acción y reacción "
                     r"(tercera ley de Newton).",
           notas="En la guía las cargas son de 100 C y 1 C; se cambiaron a microcoulombs y se "
                 "precisó que la distancia es la misma.", **COMUN)
def _():
    assert simplify(F(100 * q1, q1, r) - F(q1, 100 * q1, r)) == 0


@ejercicio(id="electrostatica-11-057", tipo="calculo", dificultad=1, fuente=fuente(PR + "11"),
           enunciado=r"Calcula la fuerza que experimenta una carga de $-5\ \mu$C en un campo "
                     r"eléctrico de $200$ N/C.",
           respuesta=r"$F = |q|E = (5\times10^{-6})(200) = 1\times10^{-3}$ N, en sentido "
                     r"contrario al campo porque la carga es negativa.", **COMUN)
def _():
    assert aprox(valor(5 * uC * 200 * N / C, N), 1e-3)


@ejercicio(id="electrostatica-11-058", tipo="calculo", dificultad=2, fuente=fuente(PR + "12"),
           enunciado=r"Dos cargas $q_1 = 6\times10^{-6}$ C y $q_2 = 28\times10^{-6}$ C están "
                     r"separadas $6$ m. Halla la intensidad del campo eléctrico en el punto "
                     r"medio del segmento que las une.",
           respuesta=r"Cada carga está a $3$ m. $E_1 = k\dfrac{6\times10^{-6}}{3^2} \approx "
                     r"\num{5,99}\times10^{3}$ N/C (apunta hacia $q_2$) y $E_2 = "
                     r"k\dfrac{28\times10^{-6}}{3^2} \approx \num{2,80}\times10^{4}$ N/C "
                     r"(apunta hacia $q_1$). Tienen sentidos opuestos: "
                     r"$E = E_2 - E_1 \approx \num{2,2}\times10^{4}$ N/C, dirigido hacia $q_1$.",
           notas="La guía no dice en qué punto se pide el campo; se eligió el punto medio.",
           **COMUN)
def _():
    E1 = valor(k * 6 * uC / (3 * m)**2, N / C)
    E2 = valor(k * 28 * uC / (3 * m)**2, N / C)
    assert aprox(E1, 5.99e3) and aprox(E2, 2.80e4) and aprox(E2 - E1, 2.2e4)


@ejercicio(id="electrostatica-11-059", tipo="calculo", dificultad=1, fuente=fuente(PR + "13"),
           enunciado=r"Determina el campo eléctrico generado por una carga de $1\times10^{-6}$ C "
                     r"a $80$ cm de ella.",
           respuesta=r"$E = k\dfrac{q}{r^2} = \dfrac{(\num{8,99}\times10^{9})(10^{-6})}"
                     r"{(\num{0,8})^2} \approx \num{1,4}\times10^{4}$ N/C, alejándose de la "
                     r"carga.", **COMUN)
def _():
    assert aprox(valor(k * 1 * uC / (80 * u.centimeter)**2, N / C), 1.4e4, 0.02)


@ejercicio(id="electrostatica-11-060", tipo="calculo", dificultad=2, fuente=fuente(PR + "15"),
           enunciado=r"En los vértices de un cuadrado cuya diagonal mide $2d$ se colocan cuatro "
                     r"cargas positivas iguales $q$. ¿Cuál es la intensidad del campo eléctrico "
                     r"en el centro del cuadrado?",
           respuesta=r"Cero: las cuatro cargas están a la misma distancia $d$ del centro y los "
                     r"campos de cargas opuestas por la diagonal son iguales y de sentido "
                     r"contrario, así que se anulan de dos en dos.", **COMUN)
def _():
    d, q = symbols("d q", positive=True)
    total = Matrix([0, 0])
    for p in [Matrix([d, 0]), Matrix([-d, 0]), Matrix([0, d]), Matrix([0, -d])]:
        total += q * (-p) / p.norm()**3       # campo en el origen: apunta del vértice al centro
    assert simplify(total) == Matrix([0, 0])


@ejercicio(id="electrostatica-11-061", tipo="calculo", dificultad=2, fuente=fuente(PR + "16"),
           enunciado=r"El potencial eléctrico a cierta distancia de una carga puntual es de "
                     r"$\num{1600}$ V y la intensidad del campo eléctrico es de $800$ N/C. ¿Cuál "
                     r"es la distancia a la carga puntual?",
           respuesta=r"$V = kq/r$ y $E = kq/r^2$, así que $r = V/E = 1600/800 = 2$ m.", **COMUN)
def _():
    assert valor((1600 * V) / (800 * N / C), m) == 2
    q = 2 * m * 1600 * V / k            # carga compatible con los datos
    assert aprox(valor(k * q / (2 * m)**2, N / C), 800)


@ejercicio(id="electrostatica-11-062", tipo="calculo", dificultad=3, fuente=fuente(PR + "17"),
           enunciado=r"Dos cargas iguales de $2\times10^{-6}$ C se repelen con una fuerza "
                     r"electrostática de $\num{0,4}$ N. Determina la distancia entre ellas y el "
                     r"potencial eléctrico que crea cada una en el punto donde está la otra.",
           respuesta=r"$r = \sqrt{kq^2/F} = \sqrt{\dfrac{(\num{8,99}\times10^{9})(2\times10^{-6})^2}"
                     r"{\num{0,4}}} \approx \num{0,30}$ m; $V = \dfrac{kq}{r} \approx "
                     r"6\times10^{4}$ V.",
           notas="La guía solo dice «determina el potencial eléctrico»; se precisó en qué punto "
                 "y se pide primero la distancia.", **COMUN)
def _():
    dist = sqrt(k * (2 * uC)**2 / (Rational(2, 5) * N))
    assert aprox(valor(dist, m), 0.30)
    assert aprox(valor(k * 2 * uC / dist, V), 6e4)


@ejercicio(id="electrostatica-11-063", tipo="calculo", dificultad=2, fuente=fuente(PR + "19"),
           enunciado=r"Dos esferas conductoras aisladas, de $12$ cm y $20$ cm de radio, están en "
                     r"el vacío con sus centros separados $10$ m, y cada una tiene una carga de "
                     r"$25\times10^{-9}$ C. Calcula el potencial de cada esfera antes de "
                     r"ponerlas en contacto.",
           respuesta=r"$V = kQ/R$ (la otra esfera, a $10$ m, influye muy poco): "
                     r"$V_1 = \dfrac{(\num{8,99}\times10^{9})(25\times10^{-9})}{\num{0,12}} "
                     r"\approx \num{1,87}\times10^{3}$ V y $V_2 \approx \num{1,12}\times10^{3}$ "
                     r"V.",
           notas="La guía menciona que luego se unen con un hilo, pero solo pregunta el "
                 "potencial antes del contacto; esa parte se omitió.", **COMUN)
def _():
    Q = 25 * 10**-9 * C
    V1, V2 = valor(k * Q / (12 * u.centimeter), V), valor(k * Q / (20 * u.centimeter), V)
    assert aprox(V1, 1.87e3) and aprox(V2, 1.12e3)
    assert valor(k * Q / (10 * m), V) < 0.025 * V2     # la otra esfera aporta ≈ 2 %


manual(64, PR + "20", r"Investiga acerca del desfibrilador cardioversor implantable (DCI) como "
       r"una aplicación de la electrostática.",
       r"El DCI es un aparato pequeño que se implanta bajo la piel y se conecta al corazón con "
       r"electrodos. Vigila el ritmo cardíaco y, si detecta una arritmia grave, descarga un "
       r"condensador que almacenó carga (y energía, $U = \frac12 CV^2$, del orden de decenas de "
       r"julios) a través del corazón para restablecer el ritmo. Relación con el capítulo: "
       r"condensadores, diferencia de potencial y energía potencial eléctrica.",
       tipo="conceptual", dificultad=2)
