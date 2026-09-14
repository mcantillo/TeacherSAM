"""Banco de ejercicios — Física 11° — Corriente eléctrica y circuitos.
Fuente: Guía de Apoyo «Fenómenos electromagnéticos» grado 11 (Ciencias Naturales), Capítulo 2:
cargas eléctricas en movimiento — secciones «Desarrolla tus competencias», «Actividades» y
«Problemas»; se lee en
recursos/fisica/Guías pedagógicas Física/markdown/11 - Guia_de_Apoyo_Fenomenos_electromagneticos_grado_11_fisica.md
La guía no trae clave: las respuestas se calcularon y se comprueban aquí (resistividad del
aluminio de la tabla 2 de la guía, 2,6·10^-8 Ω·m; e = elementary_charge de sympy).

Numeración: en «Desarrolla tus competencias» los puntos 2, 3 y 4 son una sola lectura (rayos y
pararrayos) con las preguntas 4a–4d; se citan como «4a»…«4d». En «Actividades» los puntos 6 y 8
arrastran números sueltos («6. 8 Responde», «8. 10 Responde»); se citan como 6 y 8.
Correcciones (detalle en `notas`): Problemas 3 (unidad perdida «0,01 _», «10°» y «coeficiente de
dilatación lineal» → coeficiente térmico de la resistividad); Desarrolla tus competencias 4b
(la punta del pararrayos no está «cargada positivamente» de por sí: la carga se induce).
No se omitió ningún literal.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/fisica/circuitos-11.py
"""
from sympy import Rational, pi
from sympy.physics import units as u
from sympy.physics.units import convert_to

from ejercicios import ejercicio, ejercicio_manual

GUIA = "Guía de Apoyo Fenómenos electromagnéticos 11°, Capítulo 2: cargas eléctricas en movimiento"
TEMA = "corriente eléctrica y circuitos"
DBA = ["naturales-11-3"]
COMUN = dict(tema=TEMA, grados=[11], dba=DBA)

A, V, ohm, C, J, W, s = u.ampere, u.volt, u.ohm, u.coulomb, u.joule, u.watt, u.second
e = u.elementary_charge


def valor(q, unidad):
    return float(convert_to(q, unidad) / unidad)


def aprox(a, b, rel=0.01):
    return abs(a - b) <= rel * abs(b)


def paralelo(*rs):
    return 1 / sum(1 / r for r in rs)


def opciones(*items):
    return r" \begin{opciones} " + " ".join(r"\item " + i for i in items) + r" \end{opciones}"


def fuente(ref):
    return f"{GUIA}, {ref}"


def manual(n, ref, enunciado, respuesta, tipo="conceptual", dificultad=1, notas=None):
    extra = {"notas": notas} if notas else {}
    ejercicio_manual(id=f"circuitos-11-{n:03d}", tipo=tipo, dificultad=dificultad,
                     fuente=fuente(ref), enunciado=enunciado, respuesta=respuesta,
                     **COMUN, **extra)


def vf(n, ref, afirmacion, verdadera, justificacion, notas=None):
    manual(n, ref, r"Escribe V si la afirmación es verdadera o F si es falsa, y justifica tu "
                   r"respuesta: «" + afirmacion + "»",
           ("V. " if verdadera else "F. ") + justificacion, tipo="argumentacion", notas=notas)


# ---------- Desarrolla tus competencias ----------
DC = "Desarrolla tus competencias — "
manual(1, DC + "1", r"Un fusible es un dispositivo que consiste en un hilo de cobre o plomo. "
       r"Cuando por algún motivo aumenta la corriente que pasa a través de él, se funde e "
       r"interrumpe el flujo de carga. Explica su funcionamiento en términos del efecto Joule.",
       r"Por efecto Joule, el hilo disipa calor con una potencia $P = I^2R$. Si la corriente "
       r"aumenta (un cortocircuito o una sobrecarga), el calor crece con el cuadrado de $I$; "
       r"el hilo, delgado y de bajo punto de fusión, se calienta hasta fundirse y abre el "
       r"circuito antes de que se dañen los cables o los aparatos.", tipo="argumentacion")

RAYOS = (r"Lee: «Las tormentas eléctricas cargan negativamente las nubes y, a su vez, provocan "
         r"fuertes cargas eléctricas positivas en la Tierra. Los campos eléctricos producen "
         r"iones y electrones libres en el aire, por lo que el aire se convierte en conductor "
         r"de electricidad; esto permite que el rayo se desplace. El pararrayos está formado "
         r"por una antena metálica terminada en punta, ubicada en la parte más alta de una "
         r"edificación y conectada a tierra por un cable conductor, que lleva la descarga hacia "
         r"el suelo.» ")
NOTA_LECTURA = ("En la guía la lectura ocupa los puntos 2, 3 y 4 y las preguntas son 4a–4d; "
                "se unió la lectura en el enunciado.")
manual(2, DC + "4a", RAYOS + r"¿En Colombia hay hogares que no cuentan con pararrayos? "
       r"Investiga.",
       r"Sí: la mayoría de las viviendas, sobre todo las rurales y las casas de uno o dos "
       r"pisos, no tienen pararrayos; son obligatorios en edificios altos y en instalaciones "
       r"que lo exigen la norma (RETIE / NTC 4552). Colombia es uno de los países con más "
       r"actividad de rayos del mundo, por lo que la protección es importante.",
       notas=NOTA_LECTURA)
manual(3, DC + "4b", RAYOS + r"¿Por qué en la punta de los pararrayos aparecen fuertes "
       r"cargas positivas?",
       r"La nube, cargada negativamente, repele los electrones del pararrayos hacia tierra "
       r"(inducción), y el pararrayos queda con carga positiva. En un conductor la carga se "
       r"concentra en las zonas de menor radio de curvatura (efecto de las puntas), así que "
       r"la densidad de carga y el campo eléctrico son máximos en la punta.",
       tipo="argumentacion", dificultad=2,
       notas=NOTA_LECTURA + " La guía dice que la punta tiene «una bola de cobre o platino "
             "cargada positivamente»; la carga positiva no es propia del pararrayos sino "
             "inducida por la nube, y se quitó esa frase.")
manual(4, DC + "4c", RAYOS + r"¿Por qué crees que el rayo va hacia la punta del pararrayos?",
       r"Porque en la punta el campo eléctrico es muy intenso: ioniza el aire a su alrededor "
       r"y crea un camino conductor, conectado a tierra, de menor resistencia que el resto "
       r"del edificio. La descarga sigue ese camino.", tipo="argumentacion", dificultad=2,
       notas=NOTA_LECTURA)
manual(5, DC + "4d", RAYOS + r"El lugar donde cae un rayo no se puede predecir. ¿Cómo le "
       r"explicarías a una persona que está parada en la azotea de un edificio que existe la "
       r"posibilidad de que le caiga un rayo?",
       r"Parada en la azotea, la persona es el punto más alto y cercano a la nube, y su "
       r"cuerpo (con agua y sales) es conductor: el campo es más intenso sobre ella y puede "
       r"ser el camino de la descarga. Debe bajar y refugiarse dentro del edificio durante "
       r"la tormenta.", tipo="argumentacion", notas=NOTA_LECTURA)
manual(6, DC + "5", r"En las sierras y en las selvas son frecuentes las tormentas eléctricas. "
       r"¿Qué tipo de campaña realizarías para proteger la vida de los pobladores y de sus "
       r"animales?",
       r"Respuesta abierta. Debe incluir, por ejemplo: no refugiarse bajo árboles aislados ni "
       r"en lugares altos; alejarse de cercas de alambre y del agua; resguardar a los animales "
       r"en establos con protección; instalar pararrayos y polos a tierra en escuelas y "
       r"viviendas; talleres y carteles en la comunidad.", notas="La guía dice «campana»; "
       "se corrigió a «campaña».")
manual(7, DC + "6", r"El mal uso de la electricidad causa muertes y lesiones graves. Escribe "
       r"tres medidas de prevención para evitar electrocutarse en la cocina y en la ducha.",
       r"Por ejemplo: no manipular aparatos ni interruptores con las manos mojadas o descalzo "
       r"sobre piso húmedo; instalar la ducha eléctrica con polo a tierra y un interruptor "
       r"diferencial (GFCI) y no tocarla mientras funciona; mantener cables y enchufes en buen "
       r"estado y lejos del agua; desconectar los aparatos antes de limpiarlos.")
manual(8, DC + "7", r"La energía eléctrica que llega a nuestro hogar se produce con fuentes no "
       r"renovables, como los combustibles fósiles, o usando recursos como el agua. Plantea "
       r"recomendaciones que permitan ahorrar energía en los hogares.",
       r"Por ejemplo: apagar las luces y los aparatos que no se usan y desconectar los que "
       r"quedan en espera; cambiar a bombillos LED; aprovechar la luz natural; usar la "
       r"lavadora y la plancha con carga completa; no abrir la nevera sin necesidad; preferir "
       r"electrodomésticos de alta eficiencia.")

# ---------- Actividades ----------
AC = "Actividades — "
vf(9, AC + "1a", "La corriente eléctrica es un concepto asociado al movimiento de cargas.",
   True, r"La corriente es el flujo de carga a través de un conductor, $I = q/t$.")
vf(10, AC + "1b", "Uno de los efectos producidos por la corriente eléctrica es el "
   "desprendimiento de calor cuando hay flujo de electrones.", True,
   r"Es el efecto Joule: el conductor disipa calor con potencia $P = I^2R$.")
vf(11, AC + "1c", "Cuando hay flujo de electrones por un circuito, estos se mueven del polo "
   "positivo hacia el polo negativo.", False,
   r"Por fuera de la fuente, los electrones van del polo negativo al positivo; el sentido "
   r"del positivo al negativo es el de la corriente convencional.")
vf(12, AC + "1d", "La función de un generador es suministrar energía a los electrones libres "
   "de un conductor de tal forma que puedan moverse por la conexión eléctrica.", True,
   r"El generador mantiene la diferencia de potencial (fem) que entrega energía a las cargas.")
vf(13, AC + "1e", "La resistencia de un material es inversamente proporcional a su área "
   "transversal.", True, r"$R = \rho\dfrac{L}{A}$: al duplicar el área, la resistencia se "
                         r"reduce a la mitad.")
vf(14, AC + "1f", "La ley de Ohm relaciona el voltaje con el calor generado cuando hay una "
   "diferencia de potencial en un circuito.", False,
   r"La ley de Ohm relaciona voltaje, corriente y resistencia: $V = IR$. El calor lo "
   r"describe la ley de Joule.")
vf(15, AC + "1g", "La resistencia eléctrica en un circuito óhmico es el cociente entre la "
   "corriente y el voltaje.", False, r"Es el cociente entre el voltaje y la corriente, "
                                     r"$R = V/I$.")
DIF = r"Escribe las diferencias que hay entre los siguientes conceptos: "
manual(16, AC + "2a", DIF + "corriente eléctrica e intensidad de corriente eléctrica.",
       r"La corriente eléctrica es el fenómeno (el movimiento ordenado de cargas por un "
       r"conductor); la intensidad es la magnitud que la mide: carga que atraviesa una "
       r"sección por unidad de tiempo, $I = q/t$, en amperios.")
manual(17, AC + "2b", DIF + "resistencia eléctrica y resistividad de un material.",
       r"La resistencia (en $\Omega$) es la oposición de un conductor concreto al paso de la "
       r"corriente y depende de su forma: $R = \rho L/A$. La resistividad $\rho$ (en "
       r"$\Omega\cdot$m) es una propiedad del material, independiente de sus dimensiones "
       r"(depende de la temperatura).")
manual(18, AC + "2c", DIF + "resistencias en serie y resistencias en paralelo.",
       r"En serie, por todas pasa la misma corriente, los voltajes se suman y "
       r"$R_{eq} = R_1 + R_2 + \dots$ (mayor que cada una). En paralelo, todas tienen el mismo "
       r"voltaje, las corrientes se suman y $\dfrac{1}{R_{eq}} = \dfrac{1}{R_1} + "
       r"\dfrac{1}{R_2} + \dots$ (menor que la menor).")
manual(19, AC + "2d", DIF + "corriente alterna y corriente continua.",
       r"En la corriente continua las cargas se mueven siempre en el mismo sentido (pilas, "
       r"baterías); en la alterna el sentido y el valor del voltaje cambian periódicamente "
       r"(en Colombia, 60 veces por segundo: 60 Hz), como en la red domiciliaria.")
manual(20, AC + "3", r"Cuando se lavan tanques de petróleo con chorros de agua a gran presión "
       r"hay que ser especialmente cuidadosos para que no se produzca una explosión de los "
       r"vapores del combustible. Basándote en la carga por fricción, explica por qué se puede "
       r"producir la explosión.",
       r"El roce del chorro de agua con el combustible y las paredes separa cargas "
       r"(electrización por fricción); las gotas y el tanque quedan cargados. Si la carga se "
       r"acumula, salta una chispa que enciende la mezcla de vapores y aire. Por eso se "
       r"conectan los equipos a tierra.", tipo="argumentacion", dificultad=2,
       notas="La guía dice «se lava el petróleo»; se precisó «tanques de petróleo».")
manual(21, AC + "4", r"Enumera algunos efectos producidos por la corriente eléctrica que "
       r"conozcas y comenta alguna aplicación de cada uno.",
       r"Térmico o Joule (estufas, planchas, duchas, fusibles); luminoso (bombillos); "
       r"magnético (electroimanes, motores, timbres); químico (electrólisis, galvanoplastia, "
       r"carga de baterías); fisiológico (desfibriladores, pero también el peligro de "
       r"electrocución).")


@ejercicio(id="circuitos-11-022", tipo="calculo", dificultad=1, fuente=fuente(AC + "5a"),
           enunciado=r"Se conectan a una pila de $12$ V tres resistencias en paralelo de "
                     r"$2\ \Omega$, $3\ \Omega$ y $4\ \Omega$. ¿Por cuál de ellas es mayor la "
                     r"intensidad de corriente?",
           respuesta=r"Las tres tienen $12$ V: $I = V/R$ da $6$ A, $4$ A y $3$ A. La corriente "
                     r"es mayor por la de $2\ \Omega$ (la de menor resistencia).", **COMUN)
def _():
    corrientes = {r: valor(12 * V / (r * ohm), A) for r in (2, 3, 4)}
    assert corrientes == {2: 6, 3: 4, 4: 3}
    assert max(corrientes, key=corrientes.get) == 2


manual(23, AC + "5b", r"Dibuja el circuito de una pila de $12$ V con tres resistencias en "
       r"paralelo de $2\ \Omega$, $3\ \Omega$ y $4\ \Omega$.",
       r"Tres ramas, cada una con una resistencia, conectadas entre los mismos dos nodos, que "
       r"a su vez se unen a los bornes de la pila; cada rama lleva su propia corriente "
       r"($6$ A, $4$ A y $3$ A) y por la pila pasan $13$ A.", tipo="conceptual")
manual(24, AC + "6", r"¿Por qué en los metales se mueven los electrones y los protones no?",
       r"Los protones están en los núcleos, fijos en la red cristalina del metal. Los "
       r"electrones más externos de cada átomo están débilmente ligados y se mueven "
       r"libremente por todo el metal (electrones libres): son ellos los que forman la "
       r"corriente.", notas="En la guía: «6. 8 Responde» (número suelto); se quitó el 8.")


@ejercicio(id="circuitos-11-025", tipo="calculo", dificultad=2, fuente=fuente(AC + "7"),
           enunciado=r"¿Cómo se tienen que asociar tres resistencias de $6\ \Omega$ cada una "
                     r"para que la resistencia equivalente del conjunto sea $9\ \Omega$?",
           respuesta=r"Dos en paralelo ($3\ \Omega$) y esa pareja en serie con la tercera: "
                     r"$3 + 6 = 9\ \Omega$.", **COMUN)
def _():
    R = 6
    config = {"serie": 3 * R, "paralelo": paralelo(R, R, R),
              "par+serie": paralelo(R, R) + R, "(serie)||uno": paralelo(2 * R, R)}
    assert [c for c, v in config.items() if v == 9] == ["par+serie"]


manual(26, AC + "8", r"¿Qué medirá un voltímetro si en vez de colocarlo en paralelo lo "
       r"colocamos en serie?",
       r"El voltímetro tiene una resistencia interna muy grande: en serie casi no deja pasar "
       r"corriente, el circuito deja de funcionar y el aparato marca aproximadamente el "
       r"voltaje de la fuente, no el del elemento que se quería medir.", tipo="argumentacion",
       dificultad=2, notas="En la guía: «8. 10 Responde» (número suelto); se quitó el 10.")
manual(27, AC + "9", r"Si aumenta la resistencia de un circuito, ¿la intensidad de corriente "
       r"aumenta o disminuye? Explica tu respuesta.",
       r"Disminuye: con el mismo voltaje, $I = V/R$ es inversamente proporcional a $R$.",
       tipo="argumentacion")
manual(28, AC + "10", r"¿Qué representan los símbolos $I$, $V$ y $R$ y en qué unidades se "
       r"miden?",
       r"$I$: intensidad de corriente, en amperios (A). $V$: diferencia de potencial o "
       r"voltaje, en voltios (V). $R$: resistencia eléctrica, en ohmios ($\Omega$).")
vf(29, AC + "11a", "Los focos de mayor potencia tienen mayor resistencia eléctrica.", False,
   r"Conectados al mismo voltaje, $P = V^2/R$: el de mayor potencia tiene menor resistencia "
   r"(un foco de 100 W a 120 V tiene $144\ \Omega$ y uno de 60 W, $240\ \Omega$).")
vf(30, AC + "11b", "La potencia consumida por una resistencia se mide en kilovatios-hora.",
   False, r"La potencia se mide en vatios (W); el kilovatio-hora es una unidad de energía.")
vf(31, AC + "11c", "Un conductor sometido a una diferencia de potencial se calienta.", True,
   r"Por él circula corriente y disipa calor por efecto Joule ($P = VI$).")
vf(32, AC + "11d", "La resistencia eléctrica origina caídas de potencial o de tensión "
   "eléctrica.", True, r"Por la ley de Ohm, entre los extremos de una resistencia hay una "
                       r"caída de potencial $V = IR$.")
vf(33, AC + "11e", "La energía eléctrica no se puede transformar en energía calorífica.", False,
   r"Se transforma en calor por efecto Joule (estufas, planchas, duchas).")
vf(34, AC + "11f", "La diferencia de potencial utilizada en los hogares es normalmente 110 V.",
   True, r"En Colombia la red domiciliaria es de $110$–$120$ V (nominal $120$ V, a 60 Hz); en "
         r"otros países es de $220$–$240$ V.")
vf(35, AC + "11g", "El ohmímetro es un instrumento que se utiliza para medir resistencias.",
   True, r"Mide la resistencia en ohmios, con el elemento desconectado del circuito.")
vf(36, AC + "11h", "Los semiconductores son materiales cuya resistividad tiene un valor "
   "intermedio entre la de los conductores y la de los aislantes.", True,
   r"Por ejemplo, el silicio y el germanio.")
manual(37, AC + "12", r"Explica para qué sirven la solapa metálica de algunos enchufes y el "
       r"tercer agujero del tomacorriente.",
       r"Son la conexión a tierra (polo a tierra): unen la carcasa metálica del aparato con "
       r"el suelo. Si un cable se suelta y toca la carcasa, la corriente se va a tierra (y "
       r"salta el breaker) en lugar de pasar por el cuerpo de quien toca el aparato.")

# ---------- Problemas ----------
PR = "Problemas — "


@ejercicio(id="circuitos-11-038", tipo="calculo", dificultad=1, fuente=fuente(PR + "1"),
           enunciado=r"Una fuente de fem realiza un trabajo de $3$ J para llevar una carga de "
                     r"$2$ C de un extremo a otro. Calcula la diferencia de potencial.",
           respuesta=r"$V = \dfrac{W}{q} = \dfrac{3\ \text{J}}{2\ \text{C}} = \num{1,5}$ V.",
           **COMUN)
def _():
    assert valor(3 * J / (2 * C), V) == 1.5


ALAMBRE = (r"Por un conductor de aluminio de $1$ mm de diámetro y $10$ m de largo circula una "
           r"corriente de $2$ mA durante $1$ minuto. ")
q_al = 2 * 10**-3 * A * 60 * s


@ejercicio(id="circuitos-11-039", tipo="calculo", dificultad=1, fuente=fuente(PR + "2a"),
           enunciado=ALAMBRE + r"Calcula la carga eléctrica que pasa por el conductor.",
           respuesta=r"$q = It = (2\times10^{-3}\ \text{A})(60\ \text{s}) = \num{0,12}$ C.",
           **COMUN)
def _():
    assert aprox(valor(q_al, C), 0.12)


@ejercicio(id="circuitos-11-040", tipo="calculo", dificultad=1, fuente=fuente(PR + "2b"),
           enunciado=ALAMBRE + r"Calcula el número de electrones que pasan por una sección "
                               r"del conductor.",
           respuesta=r"$n = \dfrac{q}{e} = \dfrac{\num{0,12}}{\num{1,6}\times10^{-19}} "
                     r"\approx \num{7,5}\times10^{17}$ electrones.", **COMUN)
def _():
    assert aprox(valor(q_al / e, 1), 7.5e17)


@ejercicio(id="circuitos-11-041", tipo="calculo", dificultad=2, fuente=fuente(PR + "2c"),
           enunciado=ALAMBRE + r"Calcula la resistencia del conductor (resistividad del "
                               r"aluminio: $\num{2,6}\times10^{-8}\ \Omega\cdot$m).",
           respuesta=r"$A = \pi r^2 = \pi(\num{0,5}\times10^{-3}\ \text{m})^2 \approx "
                     r"\num{7,85}\times10^{-7}$ m²; $R = \rho\dfrac{L}{A} = "
                     r"\dfrac{(\num{2,6}\times10^{-8})(10)}{\num{7,85}\times10^{-7}} \approx "
                     r"\num{0,33}\ \Omega$.",
           notas="Se añadió al enunciado la resistividad del aluminio (tabla 2 de la guía).",
           **COMUN)
def _():
    area = pi * (Rational(1, 2) * u.millimeter)**2
    R = 2.6e-8 * ohm * u.meter * 10 * u.meter / area
    assert aprox(valor(R, ohm), 0.33)


@ejercicio(id="circuitos-11-042", tipo="calculo", dificultad=2, fuente=fuente(PR + "3"),
           enunciado=r"La resistencia de una aleación, inicialmente de $\num{0,08}\ \Omega$, "
                     r"aumenta $\num{0,01}\ \Omega$ cuando la temperatura aumenta "
                     r"$10\,^{\circ}$C. ¿Cuál es su coeficiente térmico de la resistividad?",
           respuesta=r"$\Delta R = R_0\,\alpha\,\Delta T \Rightarrow \alpha = "
                     r"\dfrac{\num{0,01}}{(\num{0,08})(10)} = \num{0,0125}\,^{\circ}\text{C}^{-1} "
                     r"= \num{1,25}\times10^{-2}\,^{\circ}\text{C}^{-1}$.",
           notas="En la guía: «varía su resistencia en 0,01 _» (unidad perdida), «10°» y "
                 "«coeficiente de dilatación lineal»; lo que se calcula con R = R0(1 + αΔT) es "
                 "el coeficiente térmico de la resistividad.", **COMUN)
def _():
    alfa = Rational(1, 100) / (Rational(8, 100) * 10)
    assert alfa == Rational(1, 80) and float(alfa) == 0.0125
    assert Rational(8, 100) * (1 + alfa * 10) == Rational(9, 100)


@ejercicio(id="circuitos-11-043", tipo="calculo", dificultad=2, fuente=fuente(PR + "4"),
           enunciado=r"Dos resistencias de $100$ k$\Omega$ y $400$ k$\Omega$ se conectan en "
                     r"paralelo y el conjunto se conecta en serie con una resistencia de "
                     r"$40$ k$\Omega$. Todo el sistema se conecta a una batería ideal de $12$ V. "
                     r"¿Cuál es la intensidad de la corriente que sale de la fuente?",
           respuesta=r"$R_p = \dfrac{100\cdot400}{100+400} = 80$ k$\Omega$; "
                     r"$R_{eq} = 80 + 40 = 120$ k$\Omega$; "
                     r"$I = \dfrac{12\ \text{V}}{\num{1,2}\times10^{5}\ \Omega} = "
                     r"1\times10^{-4}$ A $= \num{0,1}$ mA.", **COMUN)
def _():
    kohm = 1000 * ohm
    Req = paralelo(100 * kohm, 400 * kohm) + 40 * kohm
    assert valor(Req, kohm) == 120
    assert aprox(valor(12 * V / Req, A), 1e-4)


@ejercicio(id="circuitos-11-044", tipo="contexto", dificultad=3, fuente=fuente(PR + "5"),
           enunciado=r"En una feria se proyecta colocar $100$ focos iguales, de resistencia "
                     r"$R = 50\ \Omega$, en paralelo. Si los focos deben funcionar durante $5$ "
                     r"horas continuas a una diferencia de potencial de $12$ V, ¿cuántas "
                     r"baterías de $12$ V y capacidad de $40$ A·h deben comprarse como mínimo?",
           respuesta=r"Cada foco: $I = 12/50 = \num{0,24}$ A; los $100$ focos: $24$ A. En $5$ h "
                     r"se necesitan $24 \times 5 = 120$ A·h, así que se requieren "
                     r"$120/40 = 3$ baterías (conectadas en paralelo).", **COMUN)
def _():
    I_total = 100 * 12 * V / (50 * ohm)
    carga = I_total * 5 * u.hour
    Ah = A * u.hour
    assert aprox(valor(I_total, A), 24) and aprox(valor(carga, Ah), 120)
    import math
    assert math.ceil(valor(carga, Ah) / 40 - 1e-9) == 3


BATERIA = (r"Por una batería pasa una corriente de $3$ mA y la diferencia de potencial entre "
           r"sus terminales es de $9$ V. ")


@ejercicio(id="circuitos-11-045", tipo="calculo", dificultad=1, fuente=fuente(PR + "6a"),
           enunciado=BATERIA + r"¿Cuál es la potencia cedida por la batería?",
           respuesta=r"$P = VI = (9\ \text{V})(3\times10^{-3}\ \text{A}) = "
                     r"\num{0,027}$ W $= 27$ mW.", **COMUN)
def _():
    assert aprox(valor(9 * V * 3 * 10**-3 * A, W), 0.027)


@ejercicio(id="circuitos-11-046", tipo="calculo", dificultad=1, fuente=fuente(PR + "6b"),
           enunciado=BATERIA + r"¿En cuánto aumenta la energía de cada culombio de carga que "
                               r"la atraviesa?",
           respuesta=r"$9$ J por cada culombio: $U = qV = (1\ \text{C})(9\ \text{V}) = 9$ J.",
           **COMUN)
def _():
    assert valor(1 * C * 9 * V, J) == 9


@ejercicio(id="circuitos-11-047", tipo="calculo", dificultad=2, fuente=fuente(PR + "6c"),
           enunciado=BATERIA + r"¿Qué energía recibe cada electrón que la atraviesa?",
           respuesta=r"$U = eV = (\num{1,6}\times10^{-19}\ \text{C})(9\ \text{V}) \approx "
                     r"\num{1,44}\times10^{-18}$ J ($9$ eV).", **COMUN)
def _():
    assert aprox(valor(e * 9 * V, J), 1.44e-18)


@ejercicio(id="circuitos-11-048", tipo="calculo", dificultad=1, fuente=fuente(PR + "7a"),
           enunciado=r"Por un alambre metálico circula una corriente de $2$ A. ¿Qué cantidad "
                     r"de carga atraviesa una sección transversal en $1$ minuto?",
           respuesta=r"$q = It = (2\ \text{A})(60\ \text{s}) = 120$ C.", **COMUN)
def _():
    assert valor(2 * A * u.minute, C) == 120


@ejercicio(id="circuitos-11-049", tipo="calculo", dificultad=1, fuente=fuente(PR + "7b"),
           enunciado=r"Por un alambre metálico circula una corriente de $2$ A. ¿Cuántos "
                     r"electrones pasan por una sección transversal en $1$ minuto?",
           respuesta=r"$n = \dfrac{q}{e} = \dfrac{120}{\num{1,6}\times10^{-19}} \approx "
                     r"\num{7,5}\times10^{20}$ electrones.", **COMUN)
def _():
    assert aprox(valor(2 * A * u.minute / e, 1), 7.5e20)


@ejercicio(id="circuitos-11-050", tipo="calculo", dificultad=1, fuente=fuente(PR + "8a"),
           enunciado=r"Por una bombilla conectada a $230$ V pasa una corriente de $\num{0,1}$ A. "
                     r"Halla la resistencia de la bombilla.",
           respuesta=r"$R = \dfrac{V}{I} = \dfrac{230}{\num{0,1}} = \num{2300}\ \Omega$.",
           **COMUN)
def _():
    assert aprox(valor(230 * V / (Rational(1, 10) * A), ohm), 2300)


@ejercicio(id="circuitos-11-051", tipo="calculo", dificultad=1, fuente=fuente(PR + "8b"),
           enunciado=r"Por una bombilla conectada a $230$ V pasa una corriente de $\num{0,1}$ A. "
                     r"Halla la carga eléctrica que circula por la bombilla en $30$ minutos.",
           respuesta=r"$q = It = (\num{0,1}\ \text{A})(1800\ \text{s}) = 180$ C.", **COMUN)
def _():
    assert aprox(valor(Rational(1, 10) * A * 30 * u.minute, C), 180)
