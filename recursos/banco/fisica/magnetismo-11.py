"""Banco de ejercicios — Física 11° — Magnetismo e inducción electromagnética.
Fuente: Guía de Apoyo «Fenómenos electromagnéticos» grado 11 (Ciencias Naturales), Capítulo 3:
electromagnetismo — secciones «Desarrolla tus competencias», «Actividades» y «Problemas»; se lee en
recursos/fisica/Guías pedagógicas Física/markdown/11 - Guia_de_Apoyo_Fenomenos_electromagneticos_grado_11_fisica.md
La guía no trae clave: las respuestas se calcularon y se comprueban aquí
(μ0 = magnetic_constant de sympy = 4π·10^-7 T·m/A).

No se incluyó: Problemas 3 (campo en un punto P a 37° de la normal al extremo de una barra: depende
de una figura que la guía no describe y de datos que faltan, como la distancia).
Correcciones (detalle en `notas`): Desarrolla tus competencias 4 (el campo «disminuye» de
8·10^-4 T a 8·10^-4 T → a 2·10^-4 T); Problemas 7 (falta el valor de ω → respuesta en función de
ω), 6 (no dice el ángulo entre el alambre y el campo → perpendicular); Actividades 3 (dos
preguntas distintas en un literal: se conservan juntas).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/fisica/magnetismo-11.py
"""
from sympy import Rational, pi, symbols, simplify
from sympy.physics import units as u
from sympy.physics.units import convert_to

from ejercicios import ejercicio, ejercicio_manual

GUIA = "Guía de Apoyo Fenómenos electromagnéticos 11°, Capítulo 3: electromagnetismo"
TEMA = "magnetismo e inducción electromagnética"
DBA = ["naturales-11-2"]
COMUN = dict(tema=TEMA, grados=[11], dba=DBA)

T, A, N, V, m, s = u.tesla, u.ampere, u.newton, u.volt, u.meter, u.second
mu0 = u.magnetic_constant
cm = u.centimeter


def valor(q, unidad):
    return float(convert_to(q, unidad) / unidad)


def aprox(a, b, rel=0.01):
    return abs(a - b) <= rel * abs(b)


def fuente(ref):
    return f"{GUIA}, {ref}"


def manual(n, ref, enunciado, respuesta, tipo="conceptual", dificultad=1, notas=None):
    extra = {"notas": notas} if notas else {}
    ejercicio_manual(id=f"magnetismo-11-{n:03d}", tipo=tipo, dificultad=dificultad,
                     fuente=fuente(ref), enunciado=enunciado, respuesta=respuesta,
                     **COMUN, **extra)


def vf(n, ref, afirmacion, verdadera, justificacion, notas=None):
    manual(n, ref, r"Escribe V si la afirmación es verdadera o F si es falsa, y justifica tu "
                   r"respuesta: «" + afirmacion + "»",
           ("V. " if verdadera else "F. ") + justificacion, tipo="argumentacion", notas=notas)


# ---------- Desarrolla tus competencias ----------
DC = "Desarrolla tus competencias — "
manual(1, DC + "1", r"Habitualmente los imanes tienen pintado el polo norte de un color y el "
       r"polo sur de otro. Si se rompe un imán justo por la zona que separa los colores, "
       r"¿habremos separado el polo norte del polo sur? Justifica tu respuesta.",
       r"No. Cada trozo se convierte en un imán completo, con su polo norte y su polo sur: "
       r"el magnetismo se debe al alineamiento de dominios en todo el material, y no existen "
       r"polos magnéticos aislados (monopolos).", tipo="argumentacion")
manual(2, DC + "2", r"Si frotamos una aguja de hierro contra un imán, siempre en el mismo "
       r"sentido, la aguja adquiere propiedades magnéticas. Esas propiedades desaparecen con "
       r"el tiempo, y muy rápidamente si ponemos la aguja en una llama. Explica estos "
       r"fenómenos.",
       r"Al frotarla, el campo del imán orienta los dominios magnéticos del hierro en una "
       r"misma dirección y la aguja se imanta. Con el tiempo la agitación térmica los "
       r"desordena poco a poco; al calentarla, la agitación es mucho mayor y, por encima de "
       r"la temperatura de Curie (unos $770\,^{\circ}$C para el hierro), el orden se pierde "
       r"por completo.", tipo="argumentacion", dificultad=2)
manual(3, DC + "3", r"A partir de la forma en que se orienta la aguja de una brújula dentro de "
       r"un campo magnético, explica por qué se puede concluir que el polo sur magnético de la "
       r"Tierra se encuentra cerca del polo norte geográfico.",
       r"El polo norte de la aguja apunta hacia el norte geográfico. Como los polos opuestos "
       r"se atraen, lo que hay cerca del norte geográfico tiene que ser un polo sur magnético.",
       tipo="argumentacion")


@ejercicio(id="magnetismo-11-004", tipo="calculo", dificultad=2, fuente=fuente(DC + "4"),
           enunciado=r"Una espira circular de $10$ cm de radio se encuentra en un campo "
                     r"magnético de $8\times10^{-4}$ T perpendicular a ella. Si en una centésima "
                     r"de segundo el campo magnético disminuye a $2\times10^{-4}$ T, calcula la "
                     r"fuerza electromotriz inducida.",
           respuesta=r"$\varepsilon = \dfrac{|\Delta\Phi|}{\Delta t} = \dfrac{A\,|\Delta B|}"
                     r"{\Delta t} = \dfrac{\pi(\num{0,1})^2(6\times10^{-4})}{\num{0,01}} \approx "
                     r"\num{1,9}\times10^{-3}$ V.",
           notas="En la guía el campo «disminuye» de 8·10^-4 T a 8·10^-4 T (no cambia: fem "
                 "nula); se tomó como valor final 2·10^-4 T. Confirmar con la docente.",
           **COMUN)
def _():
    area = pi * (10 * cm)**2
    fem = area * (8e-4 - 2e-4) * T / (Rational(1, 100) * s)
    assert aprox(valor(fem, V), 1.9e-3)


AVES = (r"Algunos experimentos con aves migratorias en jaulas muestran que tienden a "
        r"orientarse en la dirección de su vuelo migratorio, pero cuando se colocan grandes "
        r"bobinas a cada lado de la jaula para cambiar la dirección del campo magnético, las "
        r"aves cambian su orientación. ")
manual(5, DC + "5a", AVES + r"¿Vale la pena el uso de animales para realizar experimentos?",
       r"Respuesta abierta de opinión. Debe argumentar considerando el conocimiento que se "
       r"obtiene, el bienestar de los animales y alternativas; en este experimento las aves no "
       r"sufren daño y se liberan, lo que lo hace éticamente más aceptable.",
       tipo="argumentacion")
manual(6, DC + "5b", AVES + r"¿Qué beneficios obtiene el ser humano de saber que las aves se "
       r"orientan con el campo magnético?",
       r"Por ejemplo: proteger las rutas migratorias (evitar líneas eléctricas y antenas en "
       r"ellas), entender la biología de la orientación e inspirar sistemas de navegación.")
manual(7, DC + "5c", AVES + r"Averigua qué otros animales son sensibles al campo magnético de "
       r"la Tierra.",
       r"Por ejemplo: tortugas marinas, salmones, palomas mensajeras, abejas, hormigas, "
       r"tiburones y rayas, algunas bacterias (magnetotácticas) y el ganado, que tiende a "
       r"alinearse norte-sur al pastar.")
manual(8, DC + "6", r"¿Crees que el descubrimiento de que es posible generar campos "
       r"magnéticos usando corriente eléctrica es un gran adelanto? Explica.",
       r"Sí. El experimento de Oersted mostró que electricidad y magnetismo están unidos y "
       r"permitió construir electroimanes, motores, parlantes, timbres, relés y, con la "
       r"inducción, generadores y transformadores: la base de la tecnología eléctrica "
       r"actual.", tipo="argumentacion")
manual(9, DC + "7", r"Dos conductores paralelos transportan corriente en el mismo sentido: "
       r"¿se atraen o se repelen?",
       r"Se atraen: cada conductor está en el campo magnético del otro, y la fuerza "
       r"$\vec F = I\vec L\times\vec B$ apunta hacia el otro conductor. Si las corrientes "
       r"fueran de sentidos opuestos, se repelerían.", tipo="conceptual")
manual(10, DC + "8", r"Si no existiera el campo magnético terrestre muchas cosas no "
       r"funcionarían. Explica cómo crees que sería la vida en la Tierra sin campo magnético.",
       r"No habría brújulas y muchos animales perderían su orientación; sobre todo, el viento "
       r"solar y los rayos cósmicos llegarían sin desviarse: más radiación en la superficie y, "
       r"a largo plazo, pérdida de parte de la atmósfera, lo que dificultaría la vida como la "
       r"conocemos (tampoco habría auroras).", tipo="argumentacion", dificultad=2)
manual(11, DC + "9", r"¿Crees que los campos magnéticos producidos por los celulares, "
       r"computadores o televisores son dañinos para el ser humano? Consulta sobre el tema.",
       r"Respuesta abierta basada en consulta. Según la OMS, a los niveles de exposición "
       r"habituales no se ha demostrado que estos campos causen daños a la salud; sus campos "
       r"son débiles y disminuyen rápidamente con la distancia. Se recomienda un uso "
       r"moderado.", tipo="argumentacion")
manual(12, DC + "10", r"Los aceleradores de partículas usan campos magnéticos para guiar "
       r"partículas a velocidades cercanas a la de la luz y hacerlas chocar. Algunas personas "
       r"creen que su funcionamiento es de gran riesgo para la Tierra. Consulta sobre el tema "
       r"y prepara argumentos para un debate.",
       r"Respuesta abierta. Argumentos esperados: los rayos cósmicos producen en la atmósfera, "
       r"desde hace miles de millones de años, choques de más energía que los de los "
       r"aceleradores sin consecuencias; los estudios de seguridad del CERN concluyen que no "
       r"hay riesgo. En el acelerador, los campos magnéticos curvan y enfocan el haz; la "
       r"energía la dan los campos eléctricos.", tipo="argumentacion", dificultad=2,
       notas="La guía dice que los campos magnéticos «mueven» (aceleran) las partículas; "
             "en realidad las curvan y enfocan, y son los campos eléctricos los que las "
             "aceleran. Se corrigió en el enunciado.")

# ---------- Actividades ----------
AC = "Actividades — "
vf(13, AC + "1a", "La temperatura a la cual los imanes pierden sus propiedades magnéticas se "
   "llama temperatura de Curie.", True, r"Por encima de ella la agitación térmica destruye el "
                                        r"orden de los dominios magnéticos.")
vf(14, AC + "1b", "El polo norte de un imán apunta al sur magnético de la Tierra.", True,
   r"Los polos opuestos se atraen: el polo norte de la brújula apunta hacia el polo sur "
   r"magnético, que está cerca del norte geográfico.")
vf(15, AC + "1c", "Las líneas de campo de un imán se dirigen de sur a norte en el interior del "
   "imán.", True, r"Las líneas son cerradas: por fuera van de norte a sur y por dentro de sur "
                  r"a norte.")
vf(16, AC + "1d", "La fuerza magnética es paralela al campo magnético.", False,
   r"Es perpendicular al campo y a la velocidad: $\vec F = q\,\vec v\times\vec B$.")
vf(17, AC + "1e", "En el espectrógrafo de masas, la masa depende de la trayectoria que "
   "describe la partícula cuando actúa sobre ella un campo magnético.", False,
   r"Es al revés: el radio de la trayectoria depende de la masa, $r = \dfrac{mv}{qB}$; "
   r"midiendo $r$ se determina la masa, pero la masa no depende de la trayectoria.")
vf(18, AC + "1f", "La intensidad del campo magnético no depende de la intensidad de corriente "
   "que circula por un conductor.", False,
   r"Es proporcional a la corriente; por ejemplo, en un conductor recto "
   r"$B = \dfrac{\mu_0 I}{2\pi r}$.")
vf(19, AC + "1g", "La fuerza magnética sobre un conductor es directamente proporcional al "
   "campo magnético.", True, r"$F = BIL\sen\theta$.")
vf(20, AC + "1h", "Entre cargas eléctricas actúan siempre fuerzas magnéticas.", False,
   r"Entre cargas en reposo solo hay fuerzas eléctricas; las magnéticas aparecen cuando las "
   r"cargas se mueven.")
manual(21, AC + "2", r"Tienes cuatro imanes de barra. ¿Cómo los ordenarías para formar un "
       r"cuadrado estable?",
       r"Como los lados de un cuadrado, uno a continuación del otro, de modo que el polo norte "
       r"de cada imán quede junto al polo sur del siguiente: todos los extremos se atraen y "
       r"las líneas de campo forman un circuito cerrado.")
manual(22, AC + "3", r"Los televisores de pantalla de vidrio (de tubo) utilizan campos "
       r"magnéticos para mostrar imágenes: ¿cuántos campos magnéticos utilizan? ¿Por qué las "
       r"bobinas de los transformadores están enrolladas en un núcleo de hierro?",
       r"Dos: un par de bobinas desvía el haz de electrones horizontalmente y otro "
       r"verticalmente, para barrer toda la pantalla. El núcleo de hierro se imanta con "
       r"facilidad, concentra el campo magnético y conduce casi todo el flujo de la bobina "
       r"primaria a la secundaria.", tipo="conceptual", dificultad=2,
       notas="La guía junta dos preguntas distintas en el mismo punto; se conservan juntas.")
manual(23, AC + "4", r"Un imán se acerca a una espira con su polo sur hacia ella. Realiza un "
       r"esquema indicando cómo son las líneas de campo del imán.",
       r"Las líneas salen del polo norte del imán, lo rodean y entran por el polo sur; frente "
       r"a la espira apuntan hacia el imán (entran en su polo sur) y se hacen más densas a "
       r"medida que el imán se acerca, así que el flujo a través de la espira aumenta.",
       notas="Se pide un esquema; la respuesta modelo describe lo que debe mostrar.")
manual(24, AC + "5", r"¿Por qué se usan limaduras de hierro para visualizar el campo "
       r"magnético? ¿Se podrían usar las de cualquier otro metal?",
       r"El hierro es ferromagnético: cada limadura se imanta y se orienta como una pequeña "
       r"brújula a lo largo de las líneas de campo. No sirve cualquier metal: el cobre, el "
       r"aluminio o el oro casi no responden; solo otros ferromagnéticos, como el níquel o el "
       r"cobalto.")
manual(25, AC + "6", r"Además de los imanes, las cargas eléctricas también producen campos "
       r"magnéticos. ¿En qué condiciones sucede esto?",
       r"Cuando están en movimiento (corrientes eléctricas), como mostró Oersted; una carga en "
       r"reposo solo produce campo eléctrico.")
manual(26, AC + "7", r"¿Es posible que una partícula cargada sometida a la acción de un campo "
       r"electrostático tenga movimiento uniforme? ¿Y si está sometida a la acción de un campo "
       r"magnético?",
       r"En un campo eléctrico, no (si solo actúa ese campo): la fuerza $q\vec E$ no depende de "
       r"la velocidad y siempre la acelera. En un campo magnético, sí: si se mueve paralela "
       r"al campo, la fuerza es nula y el movimiento es rectilíneo uniforme; si se mueve "
       r"perpendicular, describe un movimiento circular uniforme (su rapidez no cambia).",
       tipo="argumentacion", dificultad=2)
manual(27, AC + "8", r"Una partícula con carga $q$ entra en una región donde hay un campo "
       r"magnético perpendicular a la dirección de su movimiento. Analiza el trabajo que "
       r"realiza la fuerza magnética y la variación de energía cinética de la partícula.",
       r"La fuerza magnética es siempre perpendicular a la velocidad, así que no realiza "
       r"trabajo ($W = 0$). Por el teorema del trabajo y la energía, la energía cinética no "
       r"cambia: la rapidez es constante y solo cambia la dirección (movimiento circular "
       r"uniforme de radio $r = mv/(qB)$).", tipo="argumentacion", dificultad=2)
manual(28, AC + "9", r"Define qué es una corriente eléctrica inducida y explica en qué se "
       r"diferencia de una corriente convencional.",
       r"Es la corriente que aparece en un circuito cerrado cuando varía el flujo magnético "
       r"que lo atraviesa (ley de Faraday), sin pilas ni baterías. La corriente de un circuito "
       r"con pila se debe a la diferencia de potencial de la fuente; la inducida dura solo "
       r"mientras el flujo cambia y su sentido se opone al cambio (ley de Lenz).")
manual(29, AC + "10", r"Para que se produzca una corriente eléctrica es necesario que un "
       r"generador suministre energía a las cargas. Acercando un imán a un circuito cerrado "
       r"se puede inducir una corriente sin que exista un generador. ¿Es un ejemplo de "
       r"generación espontánea de energía?",
       r"No. Por la ley de Lenz, la corriente inducida crea un campo que se opone al "
       r"movimiento del imán: quien lo acerca tiene que hacer trabajo contra esa fuerza, y "
       r"ese trabajo es la energía que recibe la corriente. La energía se conserva.",
       tipo="argumentacion", dificultad=2)
vf(30, AC + "11a", "Todo campo magnético genera una corriente eléctrica.", False,
   r"Solo un flujo magnético que varía con el tiempo induce corriente en un circuito cerrado; "
   r"un campo constante no.")
vf(31, AC + "11b", "Faraday concluyó que al acercar y alejar el imán del conductor no hay "
   "cambio en las líneas de campo magnético que atraviesan la espira.", False,
   r"Concluyó lo contrario: al acercar o alejar el imán cambia el número de líneas (el "
   r"flujo) que atraviesan la espira, y ese cambio induce la corriente.")
vf(32, AC + "11c", "La fuerza electromotriz inducida depende de la variación del campo "
   "magnético que atraviesa un circuito.", True,
   r"Ley de Faraday: $\varepsilon = -N\dfrac{\Delta\Phi}{\Delta t}$; depende de la rapidez con "
   r"que cambia el flujo.")
vf(33, AC + "11d", "El transformador convierte la corriente de la red eléctrica en una "
   "corriente con menor diferencia de potencial.", False,
   r"Puede reducir o elevar el voltaje, según la relación entre el número de espiras: "
   r"$V_s/V_p = N_s/N_p$ (y solo funciona con corriente alterna).")
vf(34, AC + "11e", "Para que un motor de corriente continua funcione es necesario alimentarlo "
   "con corriente mediante colectores.", True,
   r"El colector (conmutador) con las escobillas invierte el sentido de la corriente en la "
   r"bobina cada media vuelta, para que el giro continúe siempre en el mismo sentido.")
manual(35, AC + "12", r"¿Qué sucede cuando circula corriente eléctrica por un conductor "
       r"situado en el interior de un imán de herradura?",
       r"El campo del imán ejerce sobre el conductor una fuerza $F = BIL\sen\theta$, "
       r"perpendicular al conductor y al campo, y el conductor se desplaza (hacia afuera o "
       r"hacia adentro de la herradura, según el sentido de la corriente). Es el principio "
       r"del motor eléctrico.")
manual(36, AC + "13", r"¿Qué diferencia hay entre el inductor y el inducido de un motor "
       r"eléctrico?",
       r"El inductor es el que produce el campo magnético (imanes o electroimanes, "
       r"generalmente fijos: el estator); el inducido es la bobina por la que circula la "
       r"corriente y sobre la que actúan las fuerzas magnéticas (la parte que gira: el rotor).")

# ---------- Problemas ----------
PR = "Problemas — "


@ejercicio(id="magnetismo-11-037", tipo="calculo", dificultad=1, fuente=fuente(PR + "1"),
           enunciado=r"Una partícula con carga $q = 20\ \mu$C entra perpendicularmente en un "
                     r"campo magnético uniforme de $1$ T, con una velocidad de "
                     r"$2\times10^{6}$ m/s. Calcula la intensidad de la fuerza magnética que "
                     r"actúa sobre la carga.",
           respuesta=r"$F = qvB = (20\times10^{-6})(2\times10^{6})(1) = 40$ N.", **COMUN)
def _():
    assert aprox(valor(20 * 10**-6 * u.coulomb * 2e6 * m / s * 1 * T, N), 40)


@ejercicio(id="magnetismo-11-038", tipo="calculo", dificultad=2, fuente=fuente(PR + "2"),
           enunciado=r"Una espira de alambre de $50$ cm de radio, que transporta una corriente "
                     r"de $2$ A, está en un campo magnético uniforme de $\num{0,4}$ T. Determina "
                     r"el torque máximo que actúa sobre la espira.",
           respuesta=r"$\tau_{max} = IAB = (2)\,\pi(\num{0,5})^2(\num{0,4}) \approx "
                     r"\num{0,63}$ N·m.", **COMUN)
def _():
    tau = 2 * A * pi * (50 * cm)**2 * Rational(2, 5) * T
    assert aprox(valor(tau, N * m), 0.63)


@ejercicio(id="magnetismo-11-039", tipo="calculo", dificultad=2, fuente=fuente(PR + "4"),
           enunciado=r"¿A qué distancia de un alambre conductor largo por el cual circula una "
                     r"corriente de $95$ A el campo magnético es de $\num{1,2}\times10^{-4}$ T?",
           respuesta=r"$B = \dfrac{\mu_0 I}{2\pi r} \Rightarrow r = \dfrac{\mu_0 I}{2\pi B} = "
                     r"\dfrac{(4\pi\times10^{-7})(95)}{2\pi(\num{1,2}\times10^{-4})} \approx "
                     r"\num{0,16}$ m $= 16$ cm.", **COMUN)
def _():
    r = mu0 * 95 * A / (2 * pi * 1.2e-4 * T)
    assert aprox(valor(r, m), 0.158)


@ejercicio(id="magnetismo-11-040", tipo="calculo", dificultad=2, fuente=fuente(PR + "5"),
           enunciado=r"Calcula la intensidad del campo magnético en el centro de una espira de "
                     r"$10$ cm de radio que transporta una corriente de $5$ A.",
           respuesta=r"$B = \dfrac{\mu_0 I}{2R} = \dfrac{(4\pi\times10^{-7})(5)}{2(\num{0,1})} "
                     r"\approx \num{3,1}\times10^{-5}$ T.", **COMUN)
def _():
    assert aprox(valor(mu0 * 5 * A / (2 * 10 * cm), T), 3.14e-5)


@ejercicio(id="magnetismo-11-041", tipo="calculo", dificultad=1, fuente=fuente(PR + "6"),
           enunciado=r"Sobre un alambre de $50$ cm de longitud actúa un campo magnético "
                     r"horizontal de $\num{0,0005}$ T, perpendicular al alambre. Si por el "
                     r"conductor circula una corriente de $\num{0,2}$ A, ¿cuál es el valor de la "
                     r"fuerza que experimenta el conductor?",
           respuesta=r"$F = BIL = (5\times10^{-4})(\num{0,2})(\num{0,5}) = 5\times10^{-5}$ N.",
           notas="La guía no indica el ángulo entre el alambre y el campo; se precisó que es "
                 "perpendicular (fuerza máxima).", **COMUN)
def _():
    assert aprox(valor(5e-4 * T * Rational(1, 5) * A * 50 * cm, N), 5e-5)


w = symbols("omega", positive=True)


@ejercicio(id="magnetismo-11-042", tipo="calculo", dificultad=2, fuente=fuente(PR + "7"),
           enunciado=r"En el interior de un campo magnético constante de $\num{0,8}$ T hay una "
                     r"bobina de $10$ espiras rectangulares de área $\num{0,01}$ m². ¿Entre qué "
                     r"valores oscilará la fuerza electromotriz inducida cuando la bobina gira "
                     r"con una velocidad angular $\omega$ (en rad/s)?",
           respuesta=r"$\varepsilon = NBA\omega\,\sen(\omega t)$, con "
                     r"$\varepsilon_{max} = (10)(\num{0,8})(\num{0,01})\,\omega = "
                     r"\num{0,08}\,\omega$: oscila entre $-\num{0,08}\,\omega$ V y "
                     r"$+\num{0,08}\,\omega$ V (por ejemplo, entre $-\num{0,8}$ V y "
                     r"$\num{0,8}$ V si $\omega = 10$ rad/s).",
           notas="La guía no da el valor de la velocidad angular («con una velocidad angular "
                 "en rad/s»); se deja en función de ω.", **COMUN)
def _():
    fem_max = 10 * Rational(8, 10) * Rational(1, 100) * w
    assert simplify(fem_max - Rational(8, 100) * w) == 0
    assert fem_max.subs(w, 10) == Rational(8, 10)


@ejercicio(id="magnetismo-11-043", tipo="calculo", dificultad=2, fuente=fuente(PR + "8"),
           enunciado=r"En el interior de un generador hay $200$ espiras de área $\num{0,01}$ m² "
                     r"en un campo magnético de $2$ T. ¿Entre qué valores oscilará la fuerza "
                     r"electromotriz inducida cuando la bobina gira con una velocidad angular de "
                     r"$6\pi$ rad/s?",
           respuesta=r"$\varepsilon_{max} = NBA\omega = (200)(2)(\num{0,01})(6\pi) = 24\pi "
                     r"\approx \num{75,4}$ V: oscila entre $-\num{75,4}$ V y $+\num{75,4}$ V.",
           **COMUN)
def _():
    fem = 200 * 2 * T * Rational(1, 100) * m**2 * 6 * pi / s
    assert valor(fem, V) == float(24 * pi) and aprox(valor(fem, V), 75.4)
