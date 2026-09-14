"""Banco de ejercicios — Física 11° — Oscilaciones (resorte, M.A.S., péndulo, energía).
Fuente: Guía de Apoyo «Fenómenos ondulatorios» grado 11, Capítulo 1: oscilaciones; se lee en
recursos/fisica/Guías pedagógicas Física/markdown/11 - Guia_de_Apoyo_Fenomenos_ondulatorios_grado_11_fisica.md
Secciones: Pregunta de inicio de capítulo, los dos «Ejercicio» de «Oscilaciones de un resorte»,
Desarrolla tus competencias, Actividades y Problemas.
No se incluyen las dos «Práctica de laboratorio» (son experimentos, no ejercicios).
Las viñetas sin letra (V/F de Actividades 1 y 12) reciben las letras a, b, c… en orden.
Correcciones (detalle en `notas` de cada id): Ejercicio 2 (opciones partidas), Actividades 4
(ninguna opción era correcta), 15 (enunciado confuso), 21 y Problemas 18 (masa «1.000 kg»),
Problemas 9–10 (enunciado y literales separados), 13 («soporte»), 14 (período sin unidades),
15 (punto P0 «a π/4»), 16 (velocidad «del muelle») y el problema sin número tras el 16 («16 bis»).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/fisica/oscilaciones-11.py
"""
import sympy as sp
from sympy.physics import units as u
from sympy.physics.units import convert_to

from ejercicios import ejercicio, ejercicio_manual

GUIA = "Guía de Apoyo Fenómenos ondulatorios 11°"
CAP = f"{GUIA}, Capítulo 1: oscilaciones"
COMUN = dict(grados=[11], dba=["naturales-11-1"])
G = sp.Rational(98, 10) * u.meter / u.second**2
N_M = u.newton / u.meter
MS, MS2 = u.meter / u.second, u.meter / u.second**2


def valor(q, unidad):
    return float(convert_to(q, unidad) / unidad)


def aprox(a, b, rel=0.01):
    return abs(float(a) - float(b)) <= rel * abs(float(b))


def opciones(*items):
    return r" \begin{opciones} " + " ".join(r"\item " + i for i in items) + r" \end{opciones}"


def _id(n):
    return f"oscilaciones-11-{n:03d}"


def manual(n, ref, enunciado, respuesta, tipo="conceptual", dificultad=1, notas=None,
           tema="oscilaciones"):
    extra = {"notas": notas} if notas else {}
    ejercicio_manual(id=_id(n), tema=tema, tipo=tipo, dificultad=dificultad,
                     fuente=f"{CAP}, {ref}", enunciado=enunciado, respuesta=respuesta,
                     **extra, **COMUN)


def vf(n, ref, afirmacion, veredicto, justificacion, notas=None, tema="oscilaciones"):
    manual(n, ref, r"Escribe V si la afirmación es verdadera o F si es falsa, y justifica tu "
                   rf"respuesta: «{afirmacion}»", f"{veredicto}. {justificacion}",
           tipo="argumentacion", notas=notas, tema=tema)


def ej(n, ref, enunciado, respuesta, tipo="calculo", dificultad=2, notas=None,
       tema="oscilaciones"):
    extra = {"notas": notas} if notas else {}
    return ejercicio(id=_id(n), tema=tema, tipo=tipo, dificultad=dificultad,
                     fuente=f"{CAP}, {ref}", enunciado=enunciado, respuesta=respuesta,
                     **extra, **COMUN)


def periodo_resorte(m, k):
    return 2 * sp.pi * sp.sqrt(m / k)


def periodo_pendulo(L, g):
    return 2 * sp.pi * sp.sqrt(L / g)


# ---------- Pregunta de inicio de capítulo ----------

manual(1, "Pregunta de inicio de capítulo",
       r"Un péndulo simple consiste en una masa $m$ que cuelga del extremo de una cuerda delgada "
       r"de longitud $l$ y masa despreciable. Se separa la masa de manera que la cuerda forme un "
       r"ángulo de $\num{5,0}^{\circ}$ con la vertical y, al soltarla, oscila con una frecuencia "
       r"$f$. Si en cambio se separa hasta $\num{10,0}^{\circ}$, su frecuencia sería:" + opciones(
           "dos veces mayor.", "la mitad.", "la misma o casi la misma.",
           "casi dos veces mayor.", "un poco más de la mitad."),
       r"c. Para ángulos pequeños el período $T = 2\pi\sqrt{l/g}$ no depende de la amplitud "
       r"(isocronismo): la frecuencia es prácticamente la misma.", tipo="seleccion",
       tema="péndulo")

# ---------- «Ejercicio» 1 (Oscilaciones de un resorte): un literal por entrada ----------

_E1 = (r"Un objeto oscila de ida y vuelta. ¿La siguiente afirmación es verdadera en algún "
       r"momento del movimiento? Justifica: ")
for n, lit, afirm, resp in [
    (2, "a", "El objeto puede tener velocidad cero y, simultáneamente, aceleración distinta de "
             "cero.",
     r"Verdadera: en los extremos ($x = \pm A$) la velocidad es cero y la aceleración es máxima."),
    (3, "b", "El objeto puede tener velocidad cero y, simultáneamente, aceleración cero.",
     r"Falsa: la aceleración es cero solo en $x = 0$, donde la rapidez es máxima; mientras el "
     r"objeto oscila, nunca son cero las dos a la vez."),
    (4, "c", "El objeto puede tener aceleración cero y, simultáneamente, velocidad distinta de "
             "cero.",
     r"Verdadera: al pasar por la posición de equilibrio ($x = 0$) la aceleración es cero y la "
     r"rapidez es máxima."),
    (5, "d", "El objeto puede tener, simultáneamente, velocidad y aceleración distintas de cero.",
     r"Verdadera: en cualquier punto entre el equilibrio y un extremo ($0 < |x| < A$)."),
]:
    manual(n, f"Oscilaciones de un resorte, Ejercicio 1 — {lit}", _E1 + f"«{afirm}»", resp,
           tipo="argumentacion", tema="movimiento armónico simple")

manual(6, "Oscilaciones de un resorte, Ejercicio 2",
       r"Una masa oscila sobre una superficie sin fricción en el extremo de un resorte "
       r"horizontal. ¿Dónde, si acaso, la aceleración de la masa es cero?" + opciones(
           r"En $x = -A$.", r"En $x = 0$.", r"En $x = +A$.",
           r"Tanto en $x = -A$ como en $x = +A$.", "En ningún lado."),
       r"b. Por la ley de Hooke, $a = -\dfrac{k}{m}x$: la aceleración es cero solo donde la "
       r"fuerza del resorte es cero, en la posición de equilibrio $x = 0$.", tipo="seleccion",
       tema="movimiento armónico simple",
       notas="En la guía las opciones quedaron partidas: «a) Tanto en x = −A», «b) como en "
             "x = 0», «c) en x = +A»… Se reescribieron como cinco opciones completas.")

# ---------- Desarrolla tus competencias ----------

_DEF = opciones(
    "Ciclo que produce un objeto después de ocupar todas las posiciones posibles de la "
    "trayectoria.",
    "Número de ciclos que realiza un objeto en un segundo.",
    "Mayor distancia que alcanza un objeto respecto a la posición de equilibrio.",
    "Tiempo que tarda un objeto en realizar una oscilación.",
    "Posición que ocupa un objeto respecto a su posición de equilibrio.")
for n, lit, elem, resp in [
    (7, "a", "Período", "Tiempo que tarda un objeto en realizar una oscilación."),
    (8, "b", "Frecuencia", "Número de ciclos que realiza un objeto en un segundo."),
    (9, "c", "Oscilación", "Ciclo que produce un objeto después de ocupar todas las posiciones "
                           "posibles de la trayectoria."),
    (10, "d", "Amplitud", "Mayor distancia que alcanza un objeto respecto a la posición de "
                          "equilibrio."),
    (11, "e", "Elongación", "Posición que ocupa un objeto respecto a su posición de "
                            "equilibrio."),
]:
    manual(n, f"Desarrolla tus competencias — 1{lit}",
           rf"Relaciona el elemento del movimiento oscilatorio «{elem}» con su definición:" + _DEF,
           resp, tipo="seleccion")

manual(12, "Desarrolla tus competencias — 2",
       r"Uno de los siguientes procesos no lo realiza el motor de cuatro tiempos:" + opciones(
           "Admisión.", "Escape.", "Explosión.", "Inmersión."),
       r"d. Los cuatro tiempos son admisión, compresión, explosión (combustión) y escape; "
       r"«inmersión» no es uno de ellos.", tipo="seleccion", tema="motor de cuatro tiempos")

manual(13, "Desarrolla tus competencias — 3",
       r"La energía mecánica de un sistema masa-resorte en los extremos del movimiento depende "
       r"de:" + opciones("La masa.", "La amplitud.", "La velocidad.",
                         "La energía en el punto de equilibrio."),
       r"b. En los extremos la velocidad es cero y toda la energía es potencial elástica: "
       r"$E = \frac{1}{2}kA^2$, que depende de la amplitud (y de $k$), no de la masa.",
       tipo="seleccion", tema="energía en el M.A.S.",
       notas="La guía dice «sistema oscilante»; se precisó «masa-resorte» porque en un péndulo "
             "la energía sí depende de la masa. La opción d es circular (la energía mecánica se "
             "conserva y es la misma en el equilibrio), pero no es de lo que «depende».")

manual(14, "Desarrolla tus competencias — 4",
       r"Una oscilación amortiguada no se puede presentar cuando:" + opciones(
           "Se necesita un largo tiempo para alcanzar el equilibrio.",
           "El amortiguamiento lo alcanza en un corto tiempo.",
           "La amplitud del movimiento armónico se mantiene constante.",
           "Se necesitan varias oscilaciones para llegar al reposo."),
       r"c. En una oscilación amortiguada la amplitud disminuye con el tiempo; si se mantiene "
       r"constante, no hay amortiguamiento.", tipo="seleccion",
       tema="oscilaciones amortiguadas",
       notas="Opción d: la guía dice «varias amortiguaciones»; se escribió «varias oscilaciones».")

manual(15, "Desarrolla tus competencias — 5", r"Explica cómo se produce el movimiento de un "
       r"péndulo.",
       r"Al separar la masa de la vertical, la componente del peso tangente a la trayectoria "
       r"($mg\sen\theta$) actúa como fuerza restauradora hacia la posición de equilibrio. La masa "
       r"acelera hacia abajo, pasa por el punto más bajo con rapidez máxima (por inercia) y sube al "
       r"otro lado hasta detenerse; luego vuelve. La energía se transforma de potencial "
       r"gravitacional en cinética y viceversa.", tema="péndulo")

manual(16, "Desarrolla tus competencias — 6",
       r"Explica la diferencia entre movimiento oscilatorio y movimiento periódico.",
       r"Un movimiento periódico se repite en intervalos iguales de tiempo (por ejemplo, el "
       r"movimiento circular uniforme). Un movimiento oscilatorio es un vaivén alrededor de una "
       r"posición de equilibrio, causado por una fuerza restauradora. Todo movimiento oscilatorio "
       r"sin amortiguamiento es periódico, pero no todo movimiento periódico es oscilatorio.")

manual(17, "Desarrolla tus competencias — 7",
       r"¿El período de un péndulo depende de su masa? Explica tu respuesta.",
       r"No. Para oscilaciones pequeñas $T = 2\pi\sqrt{L/g}$: solo depende de la longitud y de la "
       r"gravedad. La masa se cancela porque la fuerza restauradora (el peso) y la inercia son "
       r"proporcionales a ella.", tema="péndulo")

manual(18, "Desarrolla tus competencias — 8a",
       r"Al golpear una regla sujeta en el extremo de una mesa, la amplitud de oscilación del "
       r"extremo va disminuyendo con el tiempo (movimiento oscilatorio amortiguado). ¿Qué sucede "
       r"con la energía que se transmite por la regla?",
       r"No desaparece: se transforma. Parte se disipa como calor por la fricción interna del "
       r"material y en el apoyo, y parte se transmite al aire como sonido (y a la mesa como "
       r"vibración). Por eso la energía mecánica de la regla, y con ella la amplitud, disminuye.",
       tema="oscilaciones amortiguadas")

manual(19, "Desarrolla tus competencias — 8b",
       r"En la situación de la regla que vibra sujeta al borde de una mesa, plantea una opción "
       r"para que el sistema amortiguado oscile durante más tiempo.",
       r"Reducir las pérdidas de energía: sujetar la regla con más firmeza (menos fricción en el "
       r"apoyo), usar un material más elástico con menos fricción interna (acero en vez de "
       r"plástico) o darle un impulso periódico en su frecuencia natural (oscilación forzada).",
       tema="oscilaciones amortiguadas")

# ---------- Actividades ----------

vf(20, "Actividades — 1a", "Todo movimiento armónico simple es periódico.", "V",
   r"Se repite cada período $T$; $x(t) = A\cos(\omega t + \varphi)$ es una función periódica.",
   notas="La guía presenta las afirmaciones de Actividades 1 como viñetas sin letra; se "
         "rotularon a–e en orden.", tema="movimiento armónico simple")
vf(21, "Actividades — 1b", "La frecuencia de un movimiento armónico simple es inversamente "
   "proporcional al período de oscilación.", "V", r"$f = \dfrac{1}{T}$.",
   tema="movimiento armónico simple")
vf(22, "Actividades — 1c", "La velocidad de un péndulo no cambia durante una oscilación "
   "completa.", "F", r"Es cero en los extremos y máxima en el punto más bajo; además cambia de "
   r"sentido.", tema="péndulo")
vf(23, "Actividades — 1d", "La aceleración de un objeto que describe un movimiento armónico "
   "simple es proporcional a la elongación.", "V",
   r"$a = -\omega^2 x$: es proporcional a la elongación y de sentido contrario a ella.",
   tema="movimiento armónico simple")
vf(24, "Actividades — 1e", "En un motor de cuatro tiempos la explosión se da cuando la válvula "
   "de admisión se cierra y sube el pistón comprimiendo la mezcla.", "F",
   r"Eso describe el tiempo de compresión. La explosión ocurre al final de la compresión, "
   r"cuando la chispa de la bujía enciende la mezcla y los gases empujan el pistón hacia abajo.",
   tema="motor de cuatro tiempos")

for n, lit, concepto, resp in [
    (25, "a", "Período", r"Tiempo que tarda un objeto en realizar una oscilación completa; se "
                         r"mide en segundos: $T = 1/f$."),
    (26, "b", "Frecuencia", r"Número de oscilaciones completas por unidad de tiempo; se mide en "
                            r"hercios (1 Hz = 1 oscilación por segundo): $f = 1/T$."),
    (27, "c", "Movimiento armónico simple", r"Movimiento oscilatorio producido por una fuerza "
     r"restauradora proporcional a la elongación ($F = -kx$); su posición es "
     r"$x = A\cos(\omega t + \varphi)$."),
    (28, "d", "Movimiento circular uniforme", r"Movimiento en una circunferencia con rapidez "
     r"constante; recorre ángulos iguales en tiempos iguales y es periódico."),
    (29, "e", "Velocidad angular", r"Ángulo barrido por unidad de tiempo, $\omega = "
     r"\dfrac{\Delta\theta}{\Delta t} = \dfrac{2\pi}{T} = 2\pi f$; se mide en rad/s."),
]:
    manual(n, f"Actividades — 2{lit}", rf"Define el concepto: {concepto}.", resp)


@ej(30, "Actividades — 3",
    r"¿Cuál es la frecuencia de un péndulo simple si su período es \num{0,5} s?" + opciones(
        r"\num{0,25} Hz", r"\num{0,5} Hz", "1 Hz", "2 Hz"),
    r"d. $f = \dfrac{1}{T} = \dfrac{1}{\num{0,5}\ \text{s}} = 2$ Hz.", tipo="seleccion",
    dificultad=1, tema="péndulo")
def _():
    f = valor(1 / (sp.Rational(1, 2) * u.second), u.hertz)
    opc = [0.25, 0.5, 1, 2]
    assert [aprox(f, o) for o in opc] == [False, False, False, True]


@ej(31, "Actividades — 4",
    r"¿Cuál es la frecuencia de un sistema masa-resorte si $m = 4$ kg y $k = 1$ N/m?" + opciones(
        "4 Hz", "1 Hz", r"\num{0,25} Hz", r"\num{0,08} Hz"),
    r"d. $f = \dfrac{1}{2\pi}\sqrt{\dfrac{k}{m}} = \dfrac{1}{2\pi}\sqrt{\dfrac{1}{4}} = "
    r"\dfrac{1}{4\pi} \approx \num{0,08}$ Hz.", tipo="seleccion",
    tema="movimiento armónico simple",
    notas="Error de la guía: ninguna opción era correcta (a 4 Hz, b 1 Hz, c 0,25 Hz, d 0,5 Hz). "
          "0,5 es la frecuencia angular ω = √(k/m) en rad/s, no la frecuencia en Hz. Se cambió "
          "la opción d por 0,08 Hz.")
def _():
    f = valor(1 / periodo_resorte(4 * u.kilogram, 1 * N_M), u.hertz)
    assert aprox(f, 1 / (4 * float(sp.pi)))
    opc = [4, 1, 0.25, 0.08]
    assert [aprox(f, o, 0.05) for o in opc] == [False, False, False, True]
    assert aprox(valor(sp.sqrt(1 * N_M / (4 * u.kilogram)), 1 / u.second), 0.5)  # ω, no f


manual(32, "Actividades — 5",
       r"Comprueba, a partir de un movimiento circular uniforme, que la posición de un movimiento "
       r"armónico simple que parte del extremo positivo ($x = A$ en $t = 0$) está dada por "
       r"$x = A\cos(\omega t)$.",
       r"Un punto gira con velocidad angular $\omega$ en una circunferencia de radio $A$, "
       r"partiendo de $\theta = 0$; en el instante $t$ el radio forma el ángulo $\theta = \omega t$ "
       r"con el eje $x$. La proyección del punto sobre el eje $x$ es $x = A\cos\theta = "
       r"A\cos(\omega t)$: oscila entre $-A$ y $A$ con período $T = 2\pi/\omega$, y en $t = 0$ vale "
       r"$A$.", tipo="argumentacion", dificultad=2, tema="movimiento armónico simple",
       notas="La guía dice «cuando parte de la posición inicial»; se precisó «extremo positivo».")

manual(33, "Actividades — 6",
       r"¿De qué depende el período de oscilación de un sólido rígido que oscila suspendido de un "
       r"punto (péndulo físico)?",
       r"De la distribución de su masa respecto al eje (momento de inercia), de la distancia del "
       r"punto de suspensión al centro de masa y de la gravedad: "
       r"$T = 2\pi\sqrt{\dfrac{I}{m g d}}$. Para oscilaciones pequeñas no depende de la amplitud.",
       dificultad=3, tema="péndulo",
       notas="La guía dice «un sólido sujeto desde algún punto de oscilación»; se precisó "
             "«suspendido de un punto (péndulo físico)».")

manual(34, "Actividades — 7", r"¿Qué es necesario para que un movimiento sea considerado como "
       r"oscilatorio?",
       r"Que exista una posición de equilibrio estable y una fuerza restauradora que, al separar "
       r"el objeto de ella, lo haga volver; el objeto va y viene alrededor de esa posición.")


@ej(35, "Actividades — 8",
    r"Considera los sistemas masa-resorte A y B. La constante elástica del resorte A es cuatro "
    r"veces la del resorte B y la masa del sistema A es cuatro veces la del sistema B. ¿Para "
    r"cuál de los sistemas es mayor la frecuencia de oscilación? Explica tu respuesta.",
    r"Para ninguno: tienen la misma frecuencia, porque "
    r"$f_A = \dfrac{1}{2\pi}\sqrt{\dfrac{4k_B}{4m_B}} = \dfrac{1}{2\pi}\sqrt{\dfrac{k_B}{m_B}} "
    r"= f_B$.", tipo="argumentacion", tema="movimiento armónico simple")
def _():
    k, m = sp.symbols("k m", positive=True)
    f = lambda kk, mm: sp.sqrt(kk / mm) / (2 * sp.pi)
    assert sp.simplify(f(4 * k, 4 * m) - f(k, m)) == 0


manual(36, "Actividades — 9", r"En la bicicleta se pueden observar diferentes movimientos "
       r"oscilatorios. Explica uno de ellos.",
       r"Por ejemplo, los pedales o las piernas del ciclista suben y bajan periódicamente; o la "
       r"suspensión (resortes y amortiguadores) oscila al pasar por un hueco: el resorte ejerce "
       r"una fuerza restauradora y el amortiguador disipa la energía para que la oscilación se "
       r"apague rápido. (Se acepta cualquier ejemplo bien explicado.)", tipo="contexto")

manual(37, "Actividades — 10",
       r"El cometa Halley da una vuelta completa alrededor del Sol cada 75 o 76 años en promedio. "
       r"Si se considera este evento como periódico, ¿es cierto afirmar que el movimiento del "
       r"cometa Halley es un movimiento oscilatorio? ¿Por qué?",
       r"No. Es periódico (se repite cada 75–76 años), pero no es un vaivén alrededor de una "
       r"posición de equilibrio: el cometa recorre una órbita cerrada (una elipse) siempre en el "
       r"mismo sentido.", tipo="argumentacion",
       notas="Se omitió el dato «en dirección contraria a los planetas», que no interviene.")

manual(38, "Actividades — 11",
       r"Una pelota atada a una raqueta con una banda elástica se golpea una y otra vez contra "
       r"la raqueta. Explica por qué se puede considerar un movimiento periódico.",
       r"Porque, si los golpes son regulares, la pelota va y vuelve por la misma trayectoria en "
       r"intervalos de tiempo aproximadamente iguales: la banda elástica actúa como fuerza "
       r"restauradora que la regresa y la raqueta le repone la energía que se pierde.",
       tipo="argumentacion")

vf(39, "Actividades — 12a", "En los extremos de la trayectoria de un movimiento armónico "
   "simple la energía cinética es cero.", "V", r"En $x = \pm A$ la velocidad es cero.",
   notas="Las afirmaciones de Actividades 12 son viñetas sin letra; se rotularon a–h.",
   tema="energía en el M.A.S.")
vf(40, "Actividades — 12b", "La energía potencial máxima se encuentra en el punto de equilibrio "
   "del movimiento armónico simple.", "F",
   r"En el equilibrio ($x = 0$) la energía potencial es cero y la cinética es máxima; la "
   r"potencial es máxima en los extremos.", tema="energía en el M.A.S.")
vf(41, "Actividades — 12c", "El período de un péndulo depende de la masa que él posee.", "F",
   r"$T = 2\pi\sqrt{L/g}$ no depende de la masa.", tema="péndulo")
vf(42, "Actividades — 12d", "Al aumentar la longitud de un péndulo el período de oscilación "
   "aumenta.", "V", r"$T$ es proporcional a $\sqrt{L}$.", tema="péndulo")
vf(43, "Actividades — 12e", "En los sistemas amortiguados la amplitud decrece hasta detenerse "
   "el objeto oscilante.", "V",
   r"La fricción disipa la energía mecánica hasta que el objeto queda en reposo en el "
   r"equilibrio.", tema="oscilaciones amortiguadas")
vf(44, "Actividades — 12f", "Para realizar un movimiento con una oscilación forzada no es "
   "necesario utilizar una fuerza externa.", "F",
   r"Una oscilación forzada es, por definición, la producida por una fuerza externa periódica.",
   tema="oscilaciones forzadas")


@ej(45, "Actividades — 12g",
    r"Escribe V si la afirmación es verdadera o F si es falsa, y justifica tu respuesta: «Para "
    r"un objeto con movimiento armónico simple cuya amplitud es $A$, la energía cinética es "
    r"igual a la potencial en la posición $x = A/2$.»",
    r"F. En $x = A/2$: $E_p = \frac{1}{2}k\left(\frac{A}{2}\right)^2 = \frac{1}{4}E$ y "
    r"$E_c = \frac{3}{4}E$. Son iguales cuando $E_p = \frac{1}{2}E$, es decir, en "
    r"$x = \pm\dfrac{A}{\sqrt{2}} \approx \pm\num{0,71}A$.", tipo="argumentacion",
    tema="energía en el M.A.S.")
def _():
    k, A, x = sp.symbols("k A x", positive=True)
    E = k * A**2 / 2
    Ep = lambda xx: k * xx**2 / 2
    assert sp.simplify(Ep(A / 2) - E / 4) == 0          # no es la mitad
    assert sp.solve(sp.Eq(Ep(x), E - Ep(x)), x) == [A * sp.sqrt(2) / 2]


vf(46, "Actividades — 12h", "Para aumentar la energía de un sistema oscilante es necesario que "
   "la fuerza externa entre en resonancia con el sistema.", "F",
   r"Cualquier fuerza externa que haga trabajo positivo aumenta la energía; la resonancia "
   r"(fuerza con la frecuencia natural del sistema) solo hace que la transferencia de energía "
   r"sea máxima.", tema="oscilaciones forzadas")

for n, lit, par, resp in [
    (47, "a", "la energía cinética y la energía potencial de un sistema oscilante",
     r"La cinética, $\frac{1}{2}mv^2$, depende de la velocidad: es máxima en el equilibrio y "
     r"cero en los extremos. La potencial (elástica $\frac{1}{2}kx^2$ o gravitacional) depende de "
     r"la posición: es cero en el equilibrio y máxima en los extremos. Su suma se conserva si no "
     r"hay fricción."),
    (48, "b", "el período de un péndulo simple y el de un sistema masa-resorte",
     r"Péndulo: $T = 2\pi\sqrt{L/g}$, depende de la longitud y de la gravedad, no de la masa. "
     r"Masa-resorte: $T = 2\pi\sqrt{m/k}$, depende de la masa y de la constante del resorte, no "
     r"de la gravedad. Ninguno depende de la amplitud (el péndulo, para ángulos pequeños)."),
    (49, "c", "las oscilaciones amortiguadas y las oscilaciones forzadas",
     r"En las amortiguadas la fricción disipa energía y la amplitud disminuye hasta que el "
     r"objeto se detiene. En las forzadas una fuerza externa periódica repone energía y el "
     r"sistema oscila con la frecuencia de esa fuerza."),
    (50, "d", "la frecuencia natural y la frecuencia de resonancia",
     r"La frecuencia natural es aquella con la que el sistema oscila libremente, sin fuerzas "
     r"externas. La resonancia ocurre cuando una fuerza externa actúa con una frecuencia igual "
     r"(o muy cercana) a la natural: entonces la amplitud crece al máximo."),
]:
    manual(n, f"Actividades — 13{lit}", rf"Establece diferencias entre {par}.", resp)

_A14 = (r"La energía mecánica de un sistema masa-resorte que oscila horizontalmente es de 32 J y "
        r"la constante elástica del resorte, de masa despreciable, es 400 N/m. ¿Es correcta la "
        r"siguiente afirmación? Justifica: ")
E14, K14 = 32 * u.joule, 400 * N_M
A14 = sp.sqrt(2 * E14 / K14)


@ej(51, "Actividades — 14a", _A14 + "«La amplitud del movimiento es \\num{0,4} m.»",
    r"Correcta: $A = \sqrt{\dfrac{2E}{k}} = \sqrt{\dfrac{2(32)}{400}} = \num{0,4}$ m.",
    tipo="argumentacion", tema="energía en el M.A.S.")
def _():
    assert aprox(valor(A14, u.meter), 0.4)


@ej(52, "Actividades — 14b", _A14 + "«En los extremos de la trayectoria la energía potencial "
    "es nula.»",
    r"Incorrecta: en los extremos la energía potencial es máxima, $E_p = \frac{1}{2}kA^2 = "
    r"32$ J, y la cinética es cero.", tipo="argumentacion", tema="energía en el M.A.S.")
def _():
    assert aprox(valor(K14 * A14**2 / 2, u.joule), 32)


@ej(53, "Actividades — 14c", _A14 + "«En el punto central de la trayectoria la energía "
    "cinética es máxima.»",
    r"Correcta: en $x = 0$ la energía potencial es cero y toda la energía, 32 J, es cinética.",
    tipo="argumentacion", tema="energía en el M.A.S.")
def _():
    Ec = lambda x: E14 - K14 * x**2 / 2
    assert aprox(valor(Ec(0 * u.meter), u.joule), 32)
    assert valor(Ec(sp.Rational(1, 10) * u.meter), u.joule) < 32


@ej(54, "Actividades — 14d", _A14 + r"«Para una elongación de $\num{0,2}\sqrt{2}$ m, la energía "
    r"potencial elástica tiene el mismo valor que la energía cinética.»",
    r"Correcta: $E_p = \frac{1}{2}(400)(\num{0,2}\sqrt{2})^2 = 16$ J y $E_c = 32 - 16 = 16$ J.",
    tipo="argumentacion", tema="energía en el M.A.S.")
def _():
    Ep = K14 * (sp.Rational(2, 10) * sp.sqrt(2) * u.meter) ** 2 / 2
    assert aprox(valor(Ep, u.joule), 16) and aprox(valor(E14 - Ep, u.joule), 16)


@ej(55, "Actividades — 14e", _A14 + "«La energía mecánica del sistema cambia durante todo el "
    "movimiento.»",
    r"Incorrecta: sin fricción la energía mecánica se conserva, $E_c + E_p = 32$ J en todo "
    r"punto; solo cambia la forma en que se reparte.", tipo="argumentacion",
    tema="energía en el M.A.S.")
def _():
    t = sp.symbols("t", real=True)
    w = sp.sqrt(400 / sp.Rational(1))    # con cualquier masa (1 kg): ω = √(k/m)
    x = sp.Rational(2, 5) * sp.cos(w * t)
    v = sp.diff(x, t)
    assert sp.simplify(sp.Rational(1, 2) * 1 * v**2 + 200 * x**2 - 32) == 0

_A15 = (r"Un péndulo simple de longitud $L$ y masa $m$ oscila con un período $T$; la cuerda es "
        r"inextensible y de masa despreciable. ¿Es correcta la siguiente afirmación? Justifica: ")
for n, lit, afirm, resp in [
    (56, "a", "«Si la longitud $L$ aumenta, la frecuencia de oscilación disminuye.»",
     r"Correcta: $f = \dfrac{1}{2\pi}\sqrt{\dfrac{g}{L}}$ disminuye cuando $L$ aumenta."),
    (57, "b", "«Manteniendo la longitud constante y aumentando la masa $m$, el período aumenta.»",
     r"Incorrecta: el período $T = 2\pi\sqrt{L/g}$ no depende de la masa."),
    (58, "c", "«Manteniendo constante la longitud de la cuerda, si se traslada el péndulo a otro "
              "lugar donde la aceleración de la gravedad es mayor, el período aumenta.»",
     r"Incorrecta: con $g$ mayor, $T = 2\pi\sqrt{L/g}$ disminuye."),
    (59, "d", "«Durante la oscilación, al pasar por la posición de equilibrio la tensión de la "
              "cuerda es igual al peso del péndulo.»",
     r"Incorrecta: en el punto más bajo la masa describe un arco (aceleración centrípeta hacia "
     r"arriba), así que $T_{\text{cuerda}} - mg = \dfrac{mv^2}{L}$ y la tensión es mayor que el "
     r"peso."),
]:
    manual(n, f"Actividades — 15{lit}", _A15 + afirm, resp, tipo="argumentacion", dificultad=2,
           tema="péndulo",
           notas=("El enunciado de la guía dice «Si la longitud L varía podemos afirmar que» como "
                  "encabezado de todos los literales; se reescribió como «¿Es correcta…?» y el "
                  "literal a se precisó a «si L aumenta» (si L disminuye, f aumenta).")
           if lit == "a" else None)

manual(60, "Actividades — 16",
       r"Se construye un péndulo con una esfera llena de arena que tiene un orificio en la parte "
       r"inferior. Mientras el péndulo oscila, la arena va saliendo por el orificio. Se observa "
       r"que el período de oscilación primero aumenta y luego disminuye. Explica por qué sucede "
       r"esto.",
       r"El período depende de la distancia del punto de suspensión al centro de masa (longitud "
       r"efectiva), no de la masa. Al salir la arena por abajo, el centro de masa del conjunto "
       r"esfera + arena baja y la longitud efectiva aumenta: el período aumenta. Cuando queda poca "
       r"arena, el centro de masa vuelve a subir hacia el centro de la esfera vacía: la longitud "
       r"efectiva y el período disminuyen.", tipo="argumentacion", dificultad=3, tema="péndulo",
       notas="La guía remite a una figura que solo muestra el montaje; el enunciado lo describe.")


@ej(61, "Actividades — 17",
    r"Las masas oscilantes de dos péndulos simples son de 30 g y 50 g, respectivamente, y la "
    r"longitud del hilo del primer péndulo es el doble que la del segundo. ¿Cuál de los dos "
    r"péndulos tendrá un período mayor?",
    r"El primero: $\dfrac{T_1}{T_2} = \sqrt{\dfrac{L_1}{L_2}} = \sqrt{2} \approx \num{1,41}$; las "
    r"masas no influyen.", tema="péndulo")
def _():
    L = sp.symbols("L", positive=True)
    r = sp.simplify(periodo_pendulo(2 * L, G) / periodo_pendulo(L, G))
    assert r == sp.sqrt(2)


@ej(62, "Actividades — 18",
    r"Un resorte estirado hasta alcanzar 2 m de longitud, con sus dos extremos fijos, se pone a "
    r"vibrar longitudinalmente con un vibrador aplicado cerca de uno de sus extremos. Cuando la "
    r"frecuencia de excitación es de 6 Hz, se observan en el resorte cuatro amplitudes máximas "
    r"(vientres). ¿Cuál es la velocidad de las ondas de compresión en el resorte?",
    r"Con los extremos como nodos, cuatro vientres son cuatro medias longitudes de onda: "
    r"$4\cdot\dfrac{\lambda}{2} = 2$ m, $\lambda = 1$ m y $v = \lambda f = (1)(6) = 6$ m/s.",
    dificultad=3, tema="ondas estacionarias",
    notas="Es un problema de ondas estacionarias (Capítulo 2), incluido aquí porque está en "
          "Actividades del Capítulo 1. Se añadió «con sus dos extremos fijos» (nodos en los "
          "extremos), necesario para que la respuesta sea única.")
def _():
    lam = 2 * (2 * u.meter) / 4
    assert aprox(valor(lam * 6 * u.hertz, MS), 6)


@ej(63, "Actividades — 19",
    r"Un resorte de constante elástica 120 N/m oscila entre los puntos A y B, separados entre "
    r"sí 16 cm. Si despreciamos la fricción, ¿cuál es la energía asociada al sistema?",
    r"La amplitud es la mitad de AB: $A = 8$ cm. $E = \frac{1}{2}kA^2 = \frac{1}{2}(120)"
    r"(\num{0,08})^2 = \num{0,384}$ J.", tema="energía en el M.A.S.")
def _():
    A = 16 * u.centimeter / 2
    assert aprox(valor(120 * N_M * A**2 / 2, u.joule), 0.384)


_A20 = (r"Un cuerpo de 4 kg oscila apoyado en un plano horizontal, unido a un resorte de 200 N/m. "
        r"Todas las fricciones son despreciables y la amplitud es 10 cm. Calcula ")
M20, K20, AMP20 = 4 * u.kilogram, 200 * N_M, 10 * u.centimeter


@ej(64, "Actividades — 20a", _A20 + "la máxima energía potencial.",
    r"$E_{p,\text{máx}} = \frac{1}{2}kA^2 = \frac{1}{2}(200)(\num{0,1})^2 = 1$ J.",
    tema="energía en el M.A.S.")
def _():
    assert aprox(valor(K20 * AMP20**2 / 2, u.joule), 1)


@ej(65, "Actividades — 20b", _A20 + "la velocidad máxima.",
    r"$\frac{1}{2}mv_{\text{máx}}^2 = 1$ J, así que $v_{\text{máx}} = A\sqrt{k/m} = "
    r"\num{0,1}\sqrt{50} \approx \num{0,71}$ m/s.", tema="energía en el M.A.S.")
def _():
    v = sp.sqrt(2 * (K20 * AMP20**2 / 2) / M20)
    assert aprox(valor(v, MS), 0.707)


@ej(66, "Actividades — 20c", _A20 + "la aceleración máxima.",
    r"$a_{\text{máx}} = \dfrac{kA}{m} = \dfrac{(200)(\num{0,1})}{4} = 5$ m/s².",
    tema="movimiento armónico simple")
def _():
    assert aprox(valor(K20 * AMP20 / M20, MS2), 5)


@ej(67, "Actividades — 21",
    r"Un cuerpo de masa 1 kg oscila atado a un resorte de constante elástica 300 N/m. Se estira "
    r"\num{0,15} m a partir de su posición de equilibrio y se suelta. Calcula la distancia a la "
    r"que se aleja de la posición de equilibrio en el otro extremo de la trayectoria, si en el "
    r"recorrido hasta él se disipa el 40 \% de la energía mecánica a causa de la fricción.",
    r"$E_0 = \frac{1}{2}(300)(\num{0,15})^2 = \num{3,375}$ J; queda el 60 \%: "
    r"$\num{2,025}$ J $= \frac{1}{2}(300)x^2$, $x = \num{0,15}\sqrt{\num{0,6}} \approx "
    r"\num{0,116}$ m $\approx \num{11,6}$ cm (la masa no interviene).", dificultad=3,
    tema="oscilaciones amortiguadas",
    notas="La guía da «1.000 kg», poco realista para un resorte de 300 N/m (y ambiguo: ¿mil o "
          "uno?). Se escribió 1 kg; la masa no afecta el resultado.")
def _():
    k = 300 * N_M
    E1 = sp.Rational(6, 10) * k * (sp.Rational(15, 100) * u.meter) ** 2 / 2
    assert aprox(valor(E1, u.joule), 2.025)
    assert aprox(valor(sp.sqrt(2 * E1 / k), u.meter), 0.116)


@ej(68, "Actividades — 22",
    r"Un astronauta puso a oscilar un péndulo en la Luna para medir su campo gravitatorio y "
    r"registró un período de \num{2,45} s. En la Tierra, el mismo péndulo registró un período de "
    r"1 s. ¿Cuál es la relación entre la gravedad de la Luna y la de la Tierra?",
    r"$g = \dfrac{4\pi^2 L}{T^2}$, así que $\dfrac{g_L}{g_T} = \left(\dfrac{T_T}{T_L}\right)^2 = "
    r"\left(\dfrac{1}{\num{2,45}}\right)^2 \approx \num{0,167} \approx \dfrac{1}{6}$.",
    tema="péndulo")
def _():
    L = 1 * u.meter
    gT = 4 * sp.pi**2 * L / (1 * u.second) ** 2
    gL = 4 * sp.pi**2 * L / (sp.Rational(245, 100) * u.second) ** 2
    assert aprox(gL / gT, 0.1666)


@ej(69, "Actividades — 23",
    r"Un péndulo simple de un metro de longitud realiza 90 oscilaciones en 3 minutos. Calcula "
    r"el valor de la aceleración de la gravedad en m/s².",
    r"$T = \dfrac{180\ \text{s}}{90} = 2$ s; $g = \dfrac{4\pi^2 L}{T^2} = \pi^2 \approx "
    r"\num{9,87}$ m/s².", tema="péndulo")
def _():
    T = 3 * u.minute / 90
    assert aprox(valor(4 * sp.pi**2 * u.meter / T**2, MS2), 9.87)


@ej(70, "Actividades — 24",
    r"Un péndulo tiene una longitud de 4 m. Calcula la frecuencia de oscilación del péndulo "
    r"considerando $g = \pi^2$ m/s².",
    r"$T = 2\pi\sqrt{\dfrac{4}{\pi^2}} = 4$ s, así que $f = \num{0,25}$ Hz.", tema="péndulo")
def _():
    T = periodo_pendulo(4 * u.meter, sp.pi**2 * MS2)
    assert aprox(valor(T, u.second), 4) and aprox(valor(1 / T, u.hertz), 0.25)


@ej(71, "Actividades — 25",
    r"Un cuerpo de masa $m$ está ligado a un resorte y oscila con una amplitud de 10 cm. Si la "
    r"constante elástica del resorte es 25 N/m, determina la energía total del movimiento.",
    r"$E = \frac{1}{2}kA^2 = \frac{1}{2}(25)(\num{0,1})^2 = \num{0,125}$ J.",
    dificultad=1, tema="energía en el M.A.S.")
def _():
    assert aprox(valor(25 * N_M * (10 * u.centimeter) ** 2 / 2, u.joule), 0.125)


@ej(72, "Actividades — 26",
    r"En la superficie del agua de una piscina se producen ondas cuya frecuencia es de 4 Hz y "
    r"cuya amplitud es de 5 cm. Si las ondas tardan 10 s en recorrer 2 m, calcula el período, "
    r"la frecuencia y la longitud de esas ondas.",
    r"$T = \dfrac{1}{4} = \num{0,25}$ s; $f = 4$ Hz; $v = \dfrac{2\ \text{m}}{10\ \text{s}} = "
    r"\num{0,2}$ m/s y $\lambda = \dfrac{v}{f} = \num{0,05}$ m $= 5$ cm.", tema="ondas",
    notas="La guía dice «se programan ondas»; se escribió «se producen ondas». Es un problema de "
          "ondas (Capítulo 2) ubicado en el Capítulo 1.")
def _():
    f = 4 * u.hertz
    v = 2 * u.meter / (10 * u.second)
    assert aprox(valor(1 / f, u.second), 0.25) and aprox(valor(v / f, u.meter), 0.05)


@ej(73, "Actividades — 27",
    r"Para simular un choque frontal entre un automóvil familiar y un vehículo de mayor masa se "
    r"usa un gran péndulo de 20 m de longitud cuya masa es cuatro veces la del automóvil. "
    r"Determina desde qué ángulo con la vertical se debe soltar el péndulo para que en el "
    r"momento del choque (punto más bajo) su velocidad sea de 70 km/h.",
    r"$v = \dfrac{70}{\num{3,6}} \approx \num{19,4}$ m/s; $h = \dfrac{v^2}{2g} \approx "
    r"\num{19,3}$ m; $\cos\theta = 1 - \dfrac{h}{L} \approx \num{0,036}$, así que "
    r"$\theta \approx 88^{\circ}$ (casi horizontal; la masa no interviene).", dificultad=3,
    tema="péndulo",
    notas="Se precisó «desde qué ángulo con la vertical se debe soltar» y «punto más bajo».")
def _():
    v = 70 * u.kilometer / u.hour
    h = v**2 / (2 * G)
    c = 1 - valor(h, u.meter) / 20
    assert aprox(valor(v, MS), 19.44) and aprox(valor(h, u.meter), 19.29)
    assert aprox(float(sp.deg(sp.acos(c))), 88, 0.005)


manual(74, "Actividades — 28",
       r"Considera un movimiento armónico simple de un cuerpo de masa $m$ ligado a un resorte de "
       r"constante elástica $k$. Escribe tres formas diferentes de expresar la energía mecánica "
       r"del sistema.",
       r"$E = \frac{1}{2}kA^2$ (en un extremo); $E = \frac{1}{2}mv_{\text{máx}}^2$ (en el "
       r"equilibrio); $E = \frac{1}{2}mv^2 + \frac{1}{2}kx^2$ (en cualquier punto). También "
       r"$E = \frac{1}{2}m\omega^2A^2$.", tipo="calculo", dificultad=2,
       tema="energía en el M.A.S.")

# ---------- Problemas ----------


@ej(75, "Problemas — 1",
    r"La rueda de una bicicleta realiza 180 giros en 5 min. Halla el período y la frecuencia "
    r"del movimiento.",
    r"$f = \dfrac{180}{300\ \text{s}} = \num{0,6}$ Hz; $T = \dfrac{1}{f} \approx \num{1,67}$ s.",
    dificultad=1, tema="movimiento periódico")
def _():
    f = 180 / (5 * u.minute)
    assert aprox(valor(f, u.hertz), 0.6) and aprox(valor(1 / f, u.second), 1.667)


@ej(76, "Problemas — 2",
    r"Dos péndulos simples de igual longitud se sueltan desde posiciones que forman ángulos de "
    r"$5^{\circ}$ y $10^{\circ}$ con la vertical. Si $T_5$ y $T_{10}$ son los tiempos que tardan "
    r"en adquirir por primera vez su máxima velocidad, ¿cuál es el valor de $T_5/T_{10}$?",
    r"La velocidad máxima se alcanza al pasar por la vertical, un cuarto de período después de "
    r"soltarlo. Para ángulos pequeños el período no depende de la amplitud: "
    r"$T_5/T_{10} = 1$ (el cálculo exacto da $\num{0,9986}$).", tipo="argumentacion",
    tema="péndulo")
def _():
    K = lambda grados: sp.elliptic_k(sp.sin(sp.rad(grados) / 2) ** 2)   # T = 4√(L/g)·K
    r = float(K(5) / K(10))
    assert aprox(r, 1, 0.002) and aprox(r, 0.9986, 0.0002)


@ej(77, "Problemas — 3",
    r"Un resorte realiza 10 oscilaciones en 2 s. Calcula su frecuencia en hercios y su período "
    r"de oscilación en segundos.",
    r"$f = \dfrac{10}{2\ \text{s}} = 5$ Hz; $T = \num{0,2}$ s.", dificultad=1,
    tema="movimiento armónico simple")
def _():
    f = 10 / (2 * u.second)
    assert aprox(valor(f, u.hertz), 5) and aprox(valor(1 / f, u.second), 0.2)


manual(78, "Problemas — 4a",
       r"En un sistema masa-resorte horizontal se comprime el resorte hasta la posición A y se "
       r"suelta. Describe el movimiento de la masa cuando hay fricción y cuando no la hay.",
       r"Sin fricción: la masa oscila indefinidamente entre A y el punto simétrico al otro lado "
       r"del equilibrio, con amplitud constante (M.A.S.). Con fricción: oscila con amplitud cada "
       r"vez menor (movimiento amortiguado) hasta detenerse en la posición de equilibrio.",
       tipo="argumentacion", tema="oscilaciones amortiguadas",
       notas="La guía remite a una figura; se describió el montaje en el enunciado. «fricción con "
             "el aire» se generalizó a «fricción».")


@ej(79, "Problemas — 4b",
    r"En un sistema masa-resorte, si la masa oscila 20 veces en un minuto, ¿cuál es el valor del "
    r"período y de la frecuencia?",
    r"$T = \dfrac{60\ \text{s}}{20} = 3$ s; $f = \dfrac{1}{3} \approx \num{0,33}$ Hz.",
    dificultad=1, tema="movimiento armónico simple")
def _():
    T = u.minute / 20
    assert aprox(valor(T, u.second), 3) and aprox(valor(1 / T, u.hertz), 0.3333)


t = sp.symbols("t", real=True)


@ej(80, "Problemas — 5a",
    r"Un cuerpo describe un M.A.S. con un período de 2 s y una amplitud de 3 m. Si en el "
    r"instante inicial está en el extremo positivo de la trayectoria, halla las ecuaciones de "
    r"la elongación, la velocidad y la aceleración.",
    r"$\omega = \dfrac{2\pi}{T} = \pi$ rad/s: $x = 3\cos(\pi t)$ m, "
    r"$v = -3\pi\sen(\pi t)$ m/s, $a = -3\pi^2\cos(\pi t)$ m/s².",
    tema="movimiento armónico simple",
    notas="La guía dice «uno de los extremos»; se fijó el extremo positivo para que la "
          "respuesta sea única (en el negativo cambian todos los signos).")
def _():
    x = 3 * sp.cos(2 * sp.pi / 2 * t)
    assert sp.simplify(sp.diff(x, t) + 3 * sp.pi * sp.sin(sp.pi * t)) == 0
    assert sp.simplify(sp.diff(x, t, 2) + 3 * sp.pi**2 * sp.cos(sp.pi * t)) == 0


@ej(81, "Problemas — 5b",
    r"Para el cuerpo del problema anterior ($T = 2$ s, $A = 3$ m, parte del extremo positivo), "
    r"halla la elongación, la velocidad y la aceleración cuando $t = 1$ s.",
    r"$x = 3\cos\pi = -3$ m (extremo opuesto), $v = 0$, $a = 3\pi^2 \approx \num{29,6}$ m/s².",
    tema="movimiento armónico simple")
def _():
    x = 3 * sp.cos(sp.pi * t)
    assert x.subs(t, 1) == -3 and sp.diff(x, t).subs(t, 1) == 0
    assert aprox(sp.diff(x, t, 2).subs(t, 1), 29.61)


X6 = 2 * sp.cos(sp.pi / 2 * t + sp.pi)
_P6 = (r"Un cuerpo describe un movimiento armónico simple según la expresión "
       r"$x = 2\cos\left(\dfrac{\pi}{2}t + \pi\right)$, con unidades del S.I. Determina ")


@ej(82, "Problemas — 6a", _P6 + "la amplitud, la frecuencia angular, el período y la constante "
    "de fase.",
    r"$A = 2$ m, $\omega = \dfrac{\pi}{2}$ rad/s, $T = \dfrac{2\pi}{\omega} = 4$ s, "
    r"$\varphi = \pi$ rad.", tema="movimiento armónico simple")
def _():
    w = sp.diff(sp.pi / 2 * t + sp.pi, t)
    assert w == sp.pi / 2 and 2 * sp.pi / w == 4 and X6.subs(t, 0) == -2


@ej(83, "Problemas — 6b", _P6 + "las funciones de velocidad y aceleración del movimiento.",
    r"$v = -\pi\sen\left(\dfrac{\pi}{2}t + \pi\right)$ m/s; "
    r"$a = -\dfrac{\pi^2}{2}\cos\left(\dfrac{\pi}{2}t + \pi\right)$ m/s².",
    tema="movimiento armónico simple")
def _():
    f = sp.pi / 2 * t + sp.pi
    assert sp.simplify(sp.diff(X6, t) + sp.pi * sp.sin(f)) == 0
    assert sp.simplify(sp.diff(X6, t, 2) + sp.pi**2 / 2 * sp.cos(f)) == 0


@ej(84, "Problemas — 6c", _P6 + "la aceleración en función de la elongación $x$.",
    r"$a = -\omega^2 x = -\dfrac{\pi^2}{4}x$ (m/s²).", tema="movimiento armónico simple")
def _():
    assert sp.simplify(sp.diff(X6, t, 2) + sp.pi**2 / 4 * X6) == 0


X7 = 2 * sp.cos(sp.pi / 4 * t)
_P7 = (r"Un móvil realiza un movimiento armónico simple según la ecuación "
       r"$x = 2\cos\left(\dfrac{\pi}{4}t\right)$, con unidades del S.I. Halla ")


@ej(85, "Problemas — 7a", _P7 + "la amplitud, la velocidad angular, el período y la constante "
    "de fase del movimiento.",
    r"$A = 2$ m, $\omega = \dfrac{\pi}{4}$ rad/s, $T = 8$ s, $\varphi = 0$.",
    tema="movimiento armónico simple")
def _():
    w = sp.pi / 4
    assert 2 * sp.pi / w == 8 and X7.subs(t, 0) == 2


@ej(86, "Problemas — 7b", _P7 + "la velocidad y la aceleración máximas.",
    r"$v_{\text{máx}} = A\omega = \dfrac{\pi}{2} \approx \num{1,57}$ m/s; "
    r"$a_{\text{máx}} = A\omega^2 = \dfrac{\pi^2}{8} \approx \num{1,23}$ m/s².",
    tema="movimiento armónico simple")
def _():
    v, a = sp.diff(X7, t), sp.diff(X7, t, 2)
    assert v.subs(t, 2) == -sp.pi / 2 and a.subs(t, 0) == -sp.pi**2 / 8
    assert aprox(sp.pi / 2, 1.57) and aprox(sp.pi**2 / 8, 1.234)


X8 = -sp.cos(2 * sp.pi / 3 * t)
_P8 = (r"Un cuerpo experimenta un movimiento armónico simple de período 3 s y amplitud 1 m. "
       r"Al iniciar el movimiento se encuentra en el extremo negativo de la trayectoria. Halla ")


@ej(87, "Problemas — 8a", _P8 + "las funciones de elongación, velocidad y aceleración respecto "
    "al tiempo.",
    r"$\omega = \dfrac{2\pi}{3}$ rad/s: $x = -\cos\left(\dfrac{2\pi}{3}t\right) = "
    r"\cos\left(\dfrac{2\pi}{3}t + \pi\right)$ m, $v = \dfrac{2\pi}{3}\sen\left(\dfrac{2\pi}{3}t"
    r"\right)$ m/s, $a = \dfrac{4\pi^2}{9}\cos\left(\dfrac{2\pi}{3}t\right)$ m/s².",
    tema="movimiento armónico simple")
def _():
    w = 2 * sp.pi / 3
    assert X8.subs(t, 0) == -1
    assert sp.simplify(X8 - sp.cos(w * t + sp.pi)) == 0
    assert sp.simplify(sp.diff(X8, t) - w * sp.sin(w * t)) == 0
    assert sp.simplify(sp.diff(X8, t, 2) - w**2 * sp.cos(w * t)) == 0


@ej(88, "Problemas — 8b", _P8 + "la elongación, la velocidad y la aceleración cuando ha "
    "transcurrido un segundo.",
    r"$x = -\cos\dfrac{2\pi}{3} = \num{0,5}$ m; $v = \dfrac{2\pi}{3}\cdot\dfrac{\sqrt{3}}{2} = "
    r"\dfrac{\pi}{\sqrt{3}} \approx \num{1,81}$ m/s; $a = -\dfrac{2\pi^2}{9} \approx "
    r"\num{-2,19}$ m/s².", tema="movimiento armónico simple")
def _():
    assert X8.subs(t, 1) == sp.Rational(1, 2)
    assert aprox(sp.diff(X8, t).subs(t, 1), 1.814)
    assert aprox(sp.diff(X8, t, 2).subs(t, 1), -2.193)


_P9 = (r"Una masa de 4 kg está ligada a un resorte de constante elástica 100 N/m y el sistema "
       r"oscila en un plano horizontal sin fricción. Determina si la siguiente afirmación es "
       r"correcta o incorrecta y justifica: ")
_N9 = ("En la guía el enunciado es el problema 9 y las afirmaciones son el 10 (numeración "
       "partida); se unieron y se citan como «9–10».")
M9, K9 = 4 * u.kilogram, 100 * N_M

manual(89, "Problemas — 9–10a", _P9 + "«El período del movimiento depende de la amplitud de "
       "oscilación.»",
       r"Incorrecta: $T = 2\pi\sqrt{m/k}$ no depende de la amplitud.", tipo="argumentacion",
       tema="movimiento armónico simple", notas=_N9)


@ej(90, "Problemas — 9–10b", _P9 + "«El valor de la velocidad angular es de 5 rad/s.»",
    r"Correcta: $\omega = \sqrt{k/m} = \sqrt{100/4} = 5$ rad/s.", tipo="argumentacion",
    tema="movimiento armónico simple", notas=_N9)
def _():
    assert aprox(valor(sp.sqrt(K9 / M9), 1 / u.second), 5)


@ej(91, "Problemas — 9–10c", _P9 + "«El período de oscilación es aproximadamente \\num{1,256} "
    "s.»",
    r"Correcta: $T = \dfrac{2\pi}{5} \approx \num{1,257}$ s.", tipo="argumentacion",
    tema="movimiento armónico simple", notas=_N9)
def _():
    assert aprox(valor(periodo_resorte(M9, K9), u.second), 1.256, 0.001)


manual(92, "Problemas — 9–10d", _P9 + "«Si el sistema se pone a oscilar verticalmente, el "
       "período será diferente.»",
       r"Incorrecta: en vertical el peso solo desplaza la posición de equilibrio ($x_0 = mg/k$); "
       r"el período sigue siendo $T = 2\pi\sqrt{m/k}$.", tipo="argumentacion",
       tema="movimiento armónico simple", notas=_N9)


@ej(93, "Problemas — 11",
    r"Un movimiento armónico simple es descrito por la función $x = \num{0,05}\cos(2\pi t + "
    r"\pi)$ (S.I.). Halla la amplitud y el período.",
    r"$A = \num{0,05}$ m $= 5$ cm; $\omega = 2\pi$ rad/s, así que $T = 1$ s.", dificultad=1,
    tema="movimiento armónico simple")
def _():
    x = sp.Rational(5, 100) * sp.cos(2 * sp.pi * t + sp.pi)
    assert sp.maximum(x, t, sp.Interval(0, 1)) == sp.Rational(5, 100)
    assert sp.simplify(x.subs(t, t + 1) - x) == 0


@ej(94, "Problemas — 12",
    r"Un resorte con un bloque de masa $m$ atado a su extremo se estira una distancia $x_0$ y "
    r"luego se suelta. ¿A qué distancia del equilibrio alcanza la cuarta parte de su velocidad "
    r"máxima?",
    r"Con $A = x_0$: $\frac{1}{2}k x_0^2 = \frac{1}{2}m\left(\frac{v_{\text{máx}}}{4}\right)^2 + "
    r"\frac{1}{2}kx^2$ y $\frac{1}{2}mv_{\text{máx}}^2 = \frac{1}{2}kx_0^2$, así que "
    r"$x = \dfrac{\sqrt{15}}{4}x_0 \approx \num{0,97}\,x_0$.", dificultad=3,
    tema="energía en el M.A.S.",
    notas="La guía llama x a la distancia estirada y pregunta por otra distancia; se renombró "
          "el estiramiento como x₀.")
def _():
    k, m, x0, x = sp.symbols("k m x_0 x", positive=True)
    vmax2 = k * x0**2 / m
    sol = sp.solve(sp.Eq(k * x0**2, m * vmax2 / 16 + k * x**2), x)
    assert sol == [sp.sqrt(15) * x0 / 4]


@ej(95, "Problemas — 13",
    r"Un cuerpo de 2 kg está unido a un resorte horizontal de constante elástica "
    r"$k = \num{2000}$ N/m. Si se alarga el resorte 10 cm y se deja libre, ¿cuál es la "
    r"frecuencia y cuál es el período?",
    r"$\omega = \sqrt{2000/2} \approx \num{31,6}$ rad/s; $f = \dfrac{\omega}{2\pi} \approx "
    r"\num{5,03}$ Hz; $T \approx \num{0,199}$ s (la amplitud no interviene).",
    tema="movimiento armónico simple",
    notas="La guía dice «unido a un soporte horizontal»; se corrigió a «resorte horizontal».")
def _():
    T = periodo_resorte(2 * u.kilogram, 2000 * N_M)
    assert aprox(valor(T, u.second), 0.1987) and aprox(valor(1 / T, u.hertz), 5.033)


@ej(96, "Problemas — 14",
    r"Un sistema masa-resorte tiene un período de $8\pi$ s cuando la masa suspendida es de "
    r"\num{16000} g. Calcula el valor de la constante de elasticidad del resorte.",
    r"$k = \dfrac{4\pi^2 m}{T^2} = \dfrac{4\pi^2(16)}{64\pi^2} = 1$ N/m.",
    tema="movimiento armónico simple",
    notas="La guía da el período «8∙π» sin unidades; se supuso 8π s.")
def _():
    m, T = 16000 * u.gram, 8 * sp.pi * u.second
    assert aprox(valor(4 * sp.pi**2 * m / T**2, N_M), 1)


_P15 = (r"Un objeto describe un M.A.S. con velocidad angular $10\pi$ rad/s y amplitud 5 cm, según "
        r"$x = A\cos(\omega t + \varphi)$. En el instante en que pasa por el punto $P_0$ su fase "
        r"es $\dfrac{\pi}{4}$ rad. Halla ")
_N15 = ("La guía dice «un punto P0 a π/4 de la posición de equilibrio», que no es una distancia; "
        "se interpretó π/4 como la fase en P0 (x = A cos(ωt + π/4), t = 0 en P0).")
X15 = sp.Rational(5, 100) * sp.cos(10 * sp.pi * t + sp.pi / 4)


@ej(97, "Problemas — 15a", _P15 + "la posición del objeto en $P_0$.",
    r"$x_0 = 5\cos\dfrac{\pi}{4} = \dfrac{5\sqrt{2}}{2} \approx \num{3,54}$ cm.",
    tema="movimiento armónico simple", notas=_N15)
def _():
    assert aprox(X15.subs(t, 0), 0.03536)


@ej(98, "Problemas — 15b", _P15 + r"la posición del objeto \num{0,5} s después de haber pasado "
    r"por $P_0$.",
    r"$x = 5\cos\left(5\pi + \dfrac{\pi}{4}\right) = -\dfrac{5\sqrt{2}}{2} \approx "
    r"\num{-3,54}$ cm (punto simétrico de $P_0$).", tema="movimiento armónico simple",
    notas=_N15)
def _():
    assert sp.simplify(X15.subs(t, sp.Rational(1, 2)) + X15.subs(t, 0)) == 0
    assert aprox(X15.subs(t, sp.Rational(1, 2)), -0.03536)


@ej(99, "Problemas — 15c", _P15 + r"la velocidad al cabo de \num{0,5} s.",
    r"$v = -A\omega\sen\left(5\pi + \dfrac{\pi}{4}\right) = \dfrac{\sqrt{2}}{4}\pi \approx "
    r"\num{1,11}$ m/s (en sentido positivo).", tema="movimiento armónico simple", notas=_N15)
def _():
    v = sp.diff(X15, t).subs(t, sp.Rational(1, 2))
    assert sp.simplify(v - sp.sqrt(2) * sp.pi / 4) == 0 and aprox(v, 1.111)


M16, T16, A16 = sp.Rational(1, 2) * u.kilogram, sp.Rational(3, 10) * u.second, \
    sp.Rational(1, 10) * u.meter
W16 = 2 * sp.pi / T16
_P16 = (r"Una masa de \num{0,5} kg unida al extremo de un resorte oscila con período de "
        r"\num{0,3} s y amplitud \num{0,1} m. Halla ")


@ej(100, "Problemas — 16a", _P16 + "la constante del resorte.",
    r"$k = \dfrac{4\pi^2 m}{T^2} = \dfrac{4\pi^2(\num{0,5})}{\num{0,09}} \approx \num{219}$ N/m.",
    tema="movimiento armónico simple")
def _():
    assert aprox(valor(M16 * W16**2, N_M), 219.3)


@ej(101, "Problemas — 16b", _P16 + "la frecuencia de oscilación.",
    r"$f = \dfrac{1}{\num{0,3}} \approx \num{3,33}$ Hz.", dificultad=1,
    tema="movimiento armónico simple",
    notas="«La frecuencia del muelle» → «la frecuencia de oscilación».")
def _():
    assert aprox(valor(1 / T16, u.hertz), 3.333)


@ej(102, "Problemas — 16c", _P16 + "la velocidad máxima que alcanza la masa.",
    r"$v_{\text{máx}} = A\omega = \num{0,1}\cdot\dfrac{2\pi}{\num{0,3}} \approx \num{2,09}$ m/s.",
    tema="movimiento armónico simple",
    notas="La guía dice «la velocidad máxima que alcanza el muelle»; es la de la masa.")
def _():
    assert aprox(valor(A16 * W16, MS), 2.094)


@ej(103, "Problemas — 16d", _P16 + "la máxima aceleración alcanzada por el objeto.",
    r"$a_{\text{máx}} = A\omega^2 = \num{0,1}\left(\dfrac{2\pi}{\num{0,3}}\right)^2 \approx "
    r"\num{43,9}$ m/s².", tema="movimiento armónico simple")
def _():
    assert aprox(valor(A16 * W16**2, MS2), 43.86)


@ej(104, "Problemas — 16 bis",
    r"Una masa suspendida de un resorte oscila; cuando el desplazamiento de la masa desde el "
    r"equilibrio es de 40 cm, la fuerza en el resorte es de \num{2,5} N, y el período de "
    r"oscilación es de 3 s. ¿Cuál es el valor de la masa suspendida?",
    r"$k = \dfrac{F}{x} = \dfrac{\num{2,5}}{\num{0,4}} = \num{6,25}$ N/m; "
    r"$m = \dfrac{kT^2}{4\pi^2} = \dfrac{(\num{6,25})(9)}{4\pi^2} \approx \num{1,42}$ kg.",
    tema="movimiento armónico simple",
    notas="En la guía este problema aparece sin número entre el 16 y el 17; se cita como "
          "«16 bis». Se precisó «desplazamiento desde el equilibrio» (fuerza restauradora).")
def _():
    k = sp.Rational(25, 10) * u.newton / (40 * u.centimeter)
    m = k * (3 * u.second) ** 2 / (4 * sp.pi**2)
    assert aprox(valor(k, N_M), 6.25) and aprox(valor(m, u.kilogram), 1.425)


@ej(105, "Problemas — 17",
    r"Un bloque de madera se sujeta al extremo de un resorte vertical y el conjunto vibra con "
    r"un período de \num{0,5} s. Si la velocidad del bloque es de \num{0,2} m/s cuando pasa por "
    r"la posición de equilibrio, calcula la amplitud del movimiento y su aceleración máxima.",
    r"$\omega = \dfrac{2\pi}{\num{0,5}} = 4\pi$ rad/s; $A = \dfrac{v_{\text{máx}}}{\omega} = "
    r"\dfrac{\num{0,2}}{4\pi} \approx \num{0,0159}$ m $\approx \num{1,6}$ cm; "
    r"$a_{\text{máx}} = v_{\text{máx}}\,\omega \approx \num{2,51}$ m/s².",
    tema="movimiento armónico simple",
    notas="«muelle vertical» → «resorte vertical».")
def _():
    w = 2 * sp.pi / (sp.Rational(1, 2) * u.second)
    v = sp.Rational(2, 10) * MS
    assert aprox(valor(v / w, u.meter), 0.01592) and aprox(valor(v * w, MS2), 2.513)


@ej(106, "Problemas — 18",
    r"En $t = 0$, un cuerpo de 1 kg en reposo en el extremo de un resorte horizontal de "
    r"constante elástica 200 N/m es golpeado por un martillo que le comunica una velocidad "
    r"inicial de \num{3,2} m/s. Encuentra el período y la frecuencia del movimiento.",
    r"$T = 2\pi\sqrt{\dfrac{1}{200}} \approx \num{0,444}$ s; $f \approx \num{2,25}$ Hz (la "
    r"velocidad inicial solo fija la amplitud, $A = v_0/\omega \approx \num{0,23}$ m).",
    tema="movimiento armónico simple",
    notas="La guía da «1.000 kg»: con 1000 kg, T ≈ 14 s y un martillazo no le daría 3,2 m/s a "
          "una tonelada; se tomó 1 kg (lectura de «1.000» como 1,000).")
def _():
    T = periodo_resorte(1 * u.kilogram, 200 * N_M)
    assert aprox(valor(T, u.second), 0.4443) and aprox(valor(1 / T, u.hertz), 2.251)
    assert aprox(valor(sp.Rational(32, 10) * MS * T / (2 * sp.pi), u.meter), 0.2263)
