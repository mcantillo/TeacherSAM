"""Banco de ejercicios — Física 10° — Trabajo, energía, potencia y conservación de la energía.
Fuente: Guía de apoyo de Física 10° «Movimiento circular, energía, fluidos y termodinámica»,
Capítulo 2 (la energía); se lee en
recursos/fisica/Guías pedagógicas Física/markdown/10 - Guia_de_Apoyo_movimiento_circular_energia_fluidos_y_termodinamica_grado_10_fisica.md
Secciones: Desarrolla tus competencias, Actividades, Problemas.
DBA: naturales grado 10 · DBA 2 — Comprende la conservación de la energía mecánica como un
principio que permite cuantificar y explicar diferentes fenómenos mecánicos: choques entre
cuerpos, movimiento pendular, caída libre, deformación de un sistema masa-resorte.
g = 9,8 m/s²; 1 HP = 746 W.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/fisica/energia-10.py
"""
from math import cos, radians, sin, sqrt

import sympy as sp
from sympy.physics.units import (centimeter, convert_to, gram, hour, joule, kilogram, kilometer,
                                 meter, minute, newton, second, watt)

from ejercicios import ejercicio, ejercicio_manual

PRE = "energia-10"
G2 = ("Guía de apoyo Física 10° (movimiento circular, energía, fluidos y termodinámica), "
      "Cap. 2 La energía")
DES = f"{G2}, Desarrolla tus competencias"
ACT = f"{G2}, Actividades"
PROB = f"{G2}, Problemas"
COMUN = dict(tema="trabajo y energía", grados=[10], dba=["naturales-10-2"])

m, s, kg, N, J, W, cm, km, h = meter, second, kilogram, newton, joule, watt, centimeter, \
    kilometer, hour
G = 9.8 * m / s**2
HP = 746 * W


def _meta(n, fuente, enunciado, respuesta, kw, tipo):
    d = dict(id=f"{PRE}-{n:03d}", fuente=fuente, enunciado=enunciado, respuesta=respuesta,
             tipo=tipo, dificultad=1, **COMUN)
    d.update(kw)
    return d


def E(n, fuente, enunciado, respuesta, **kw):
    return ejercicio(**_meta(n, fuente, enunciado, respuesta, kw, "calculo"))


def M(n, fuente, enunciado, respuesta, **kw):
    ejercicio_manual(**_meta(n, fuente, enunciado, respuesta, kw, "conceptual"))


def op(*items):
    return r" \begin{opciones} " + " ".join(r"\item " + i for i in items) + r" \end{opciones}"


def val(q, unidad):
    """Número de «unidad» que hay en q (unidad=1: cociente adimensional); falla si las
    dimensiones no coinciden."""
    if unidad == 1:
        return float(convert_to(q, [meter, kilogram, second]))
    return float(convert_to(q, unidad) / unidad)


def aprox(q, esperado, unidad, rel=0.01):
    v = val(q, unidad)
    assert abs(v - esperado) <= rel * abs(esperado), f"{v} ≠ {esperado}"


def raiz(q, unidad):
    return sqrt(val(q, unidad**2)) * unidad


def _es(condicion):
    assert condicion


# ---------- Desarrolla tus competencias ----------

M(1, f"{DES} — 1",
  r"Dos personas suben hasta 4 m de altura por una escalera: una la apoya inclinada y la otra "
  r"totalmente vertical. ¿Cuál de las dos realiza más trabajo?",
  r"Si tienen la misma masa, las dos hacen el mismo trabajo contra la gravedad, $W = mgh$: "
  r"solo importa la altura que suben, no el camino. (Si las masas son distintas, trabaja "
  r"más la de mayor masa).")
M(2, f"{DES} — 2",
  r"Desde la terraza de un edificio se deja caer un globo lleno de agua. Sin fricción con el "
  r"aire, ¿cómo se transforma su energía desde que se suelta hasta que toca el suelo? ¿Qué "
  r"cambia si se tiene en cuenta la fricción con el aire?",
  r"Sin fricción, la energía potencial gravitacional se convierte en energía cinética y la "
  r"energía mecánica se conserva. Con fricción, parte de la energía se transforma en energía "
  r"térmica (calor) por el roce con el aire, y el globo llega al suelo con menos energía "
  r"cinética.")
M(3, f"{DES} — 3",
  r"¿Qué influencia tiene en la producción de energía de una central eólica la velocidad del "
  r"viento que mueve las hélices? Justifica.",
  r"Mucha: la energía cinética del aire es $\frac{1}{2}mv^2$ y, además, a mayor velocidad pasa "
  r"más masa de aire por segundo; la potencia disponible crece como $v^3$. Si la velocidad "
  r"del viento se duplica, la potencia se multiplica por 8.")
M(4, f"{DES} — 4",
  r"Una pelota de masa $m$ se deja caer desde una altura $h_0$. En una gráfica de energía "
  r"contra altura, la energía cinética es una recta. Representa en el mismo plano la energía "
  r"potencial y la energía mecánica.",
  r"$E_p = mgh$ es una recta que va de 0 (en $h = 0$) a $mgh_0$ (en $h = h_0$); "
  r"$E_c = mg(h_0 - h)$ es la recta opuesta, de $mgh_0$ en el suelo a 0 arriba; la energía "
  r"mecánica $E_m = E_c + E_p = mgh_0$ es una recta horizontal.", dificultad=2)
M(5, f"{DES} — 5",
  r"¿Por qué la fuerza centrípeta que actúa sobre un yoyo que se hace girar no realiza "
  r"trabajo?",
  r"Porque es perpendicular al desplazamiento en cada instante ($\theta = 90^\circ$, "
  r"$W = Fd\cos90^\circ = 0$): cambia la dirección de la velocidad, pero no la rapidez.")
M(6, f"{DES} — 6",
  r"¿Las máquinas simples (poleas, palancas, plano inclinado) sirven para ahorrar trabajo? "
  r"¿Por qué?",
  r"No: permiten hacer menos fuerza, pero a lo largo de una distancia mayor; el trabajo "
  r"$W = Fd$ es el mismo (o un poco mayor, por la fricción). Lo que ahorran es fuerza.")
M(7, f"{DES} — 7",
  r"¿Cuál es la fuente de energía en el salto con garrocha? ¿Cómo se transforma la energía en "
  r"el movimiento del atleta?",
  r"La energía química de los músculos (que viene de los alimentos). Al correr se convierte "
  r"en energía cinética; al clavar la garrocha, en energía potencial elástica de la garrocha "
  r"doblada; esta impulsa al atleta hacia arriba y se convierte en energía potencial "
  r"gravitacional; en la caída vuelve a ser energía cinética.")
M(8, f"{DES} — 8a",
  r"El ascensor de un edificio sube del primer al séptimo piso con velocidad constante. ¿Qué "
  r"variaciones tiene su energía cinética mientras se mueve?",
  r"Ninguna: con velocidad constante, $E_c = \frac{1}{2}mv^2$ no cambia.")
M(9, f"{DES} — 8b",
  r"El ascensor que sube con velocidad constante del primer al séptimo piso, ¿conserva su "
  r"energía mecánica? ¿Por qué?",
  r"No: la energía cinética es constante y la potencial aumenta, así que la mecánica aumenta. "
  r"La aporta el motor, una fuerza externa que hace trabajo.")
M(10, f"{DES} — 9",
  r"Desde el punto de vista de la conservación de la energía, ¿por qué la mayoría de los "
  r"caminos que llevan a la cima de una montaña no son en línea recta?",
  r"La energía para subir, $mgh$, es la misma por cualquier camino; pero un camino en zigzag, "
  r"menos empinado, reparte ese trabajo en una distancia mayor, así que se necesita menos "
  r"fuerza: los vehículos y las personas pueden subir sin un esfuerzo imposible.")
M(11, f"{DES} — 10",
  r"¿Qué implica que los caminos a la cima de una montaña sean en zigzag para la potencia "
  r"que necesita el motor de un vehículo?",
  r"Como el camino es más largo y menos empinado, la misma energía se entrega en más tiempo: "
  r"a una misma velocidad el motor necesita menos fuerza y menos potencia ($P = Fv$), aunque "
  r"el viaje dure más.")
for _n, _lit, _af, _resp in [
        (12, "a", "Una fuerza es conservativa si su energía mecánica es constante.",
         "F: una fuerza es conservativa si el trabajo que realiza no depende del camino (o es "
         "cero en una trayectoria cerrada). Cuando solo actúan fuerzas conservativas, la "
         "energía mecánica del sistema se conserva."),
        (13, "b", "La energía mecánica es la suma de las energías cinética y radiante.",
         "F: es la suma de la energía cinética y la potencial."),
        (14, "c", "El carbón es un recurso energético renovable.",
         "F: es un combustible fósil; tarda millones de años en formarse."),
        (15, "d", "La energía eólica es una fuente de energía alternativa.", "V."),
        (16, "e", "Es posible crear energía a través de las energías alternativas.",
         "F: la energía no se crea ni se destruye; las fuentes alternativas transforman la "
         "energía del viento, el Sol, etc., en otras formas útiles.")]:
    M(_n, f"{DES} — 11{_lit}", "Escribe V si el enunciado es verdadero o F si es falso: " + _af,
      _resp)
M(17, f"{DES} — 12", tipo="seleccion",
  enunciado=r"Un resorte se sujeta verticalmente y se pone a oscilar. El punto en el que su "
            r"energía cinética es máxima es:" +
            op("su máxima elongación, el punto más bajo.", "el punto de equilibrio, el punto medio.",
               "su máxima compresión, el punto más alto.",
               "cualquier punto, pues su energía cinética es constante."),
  respuesta=r"b) El punto de equilibrio: allí la velocidad es máxima; en los extremos la masa "
            r"se detiene un instante y la energía es toda potencial.")
M(18, f"{DES} — 13", tipo="seleccion",
  enunciado=r"La fuente de energía que se encuentra en la materia orgánica, de origen vegetal "
            r"o animal, y en los materiales obtenidos de su transformación, se llama:" +
            op("biomasa.", "geotérmica.", "mareomotriz.", "solar."),
  respuesta=r"a) Biomasa.")

# ---------- Actividades ----------


@E(19, f"{ACT} — 1", tipo="seleccion",
   enunciado=r"Una fuerza aplicada sobre un cuerpo no realiza trabajo cuando el ángulo que "
             r"forma con el desplazamiento es:" + op(r"$180^\circ$", r"$90^\circ$", r"$0^\circ$",
                                                     r"$30^\circ$"),
   respuesta=r"b) $90^\circ$: $W = Fd\cos\theta$ y $\cos90^\circ = 0$.")
def _():
    assert [sp.cos(sp.rad(a)) == 0 for a in (180, 90, 0, 30)] == [False, True, False, False]


M(20, f"{ACT} — 2", tipo="seleccion",
  enunciado=r"Un automóvil se mueve con velocidad constante por una carretera recta. ¿Cuál de "
            r"las siguientes afirmaciones es falsa?" +
            op("No se realiza trabajo alguno sobre el carro.",
               "La fuerza de rozamiento realiza trabajo.", "La fuerza normal no realiza trabajo.",
               "El auto solo tiene energía cinética."),
  respuesta=r"a): sí se realiza trabajo sobre el carro: la fuerza del motor (a través de las "
            r"llantas) hace trabajo positivo y el rozamiento trabajo negativo; lo que es cero "
            r"es el trabajo neto.",
  notas="La opción d depende del nivel de referencia (sobre la carretera, Ep = 0).")
M(21, f"{ACT} — 3", r"¿Por qué la energía asociada a un resorte es potencial?",
  r"Porque depende de la configuración del resorte (de cuánto está estirado o comprimido, "
  r"$E_p = \frac{1}{2}kx^2$) y no de su movimiento: es energía almacenada que puede "
  r"convertirse en cinética al soltarlo.")
M(22, f"{ACT} — 4", r"¿Es posible que la energía cinética de un cuerpo sea negativa? Justifica.",
  r"No: $E_c = \frac{1}{2}mv^2$, y la masa es positiva y $v^2 \ge 0$; como mucho vale cero, "
  r"cuando el cuerpo está en reposo.")


@E(23, f"{ACT} — 5", tipo="seleccion",
   enunciado=r"Un tren que viaja a una velocidad $v_1$ tiene una energía cinética $E_{c1}$. "
             r"Si reduce su velocidad a la tercera parte, su energía cinética será:" +
             op(r"$E_c = 3E_{c1}$", r"$E_c = E_{c1}/9$", r"$E_c = E_{c1}/6$",
                r"$E_c = E_{c1}/3$"),
   respuesta=r"b) $E_c = E_{c1}/9$: la energía cinética es proporcional a $v^2$ y "
             r"$(1/3)^2 = 1/9$.")
def _():
    mm, v = sp.symbols("m v", positive=True)
    ec = lambda x: mm * x**2 / 2
    r = sp.simplify(ec(v / 3) / ec(v))
    assert [r == o for o in (3, sp.Rational(1, 9), sp.Rational(1, 6), sp.Rational(1, 3))] == \
        [False, True, False, False]


M(24, f"{ACT} — 6",
  r"En una presentación de porras, dos deportistas, uno de $\num{1,8}$ m y otro de "
  r"$\num{1,6}$ m de estatura, levantan cada uno a su compañera hasta la altura de su cabeza. "
  r"Si las dos porristas tienen la misma masa, ¿cuál deportista realiza más trabajo? Explica.",
  r"El de $\num{1,8}$ m: $W = mgh$ y levanta a su compañera a mayor altura.")


@E(25, f"{ACT} — 7", tipo="argumentacion",
   enunciado=r"En una construcción se dejan caer un ladrillo y un bloque pequeño que tiene la "
             r"mitad de la masa del ladrillo. Si el ladrillo cae desde el piso 4 y el bloque "
             r"desde el piso 8, ¿cuál de los dos puede causar más daño al caer? Explica.",
   respuesta=r"Los dos llegan al suelo con la misma energía: $E_p = mgh$ y el bloque tiene la "
             r"mitad de la masa pero cae desde el doble de altura ($\frac{m}{2} \cdot 2h = mh$). "
             r"Sin fricción, ambos pueden causar un daño parecido (el bloque llega más rápido).")
def _():
    mm, hh, g = sp.symbols("m h g", positive=True)
    assert sp.simplify((mm / 2) * g * (2 * hh) - mm * g * hh) == 0


M(26, f"{ACT} — 8",
  r"Dos automóviles iguales recorren la misma distancia, uno por una carretera plana y el "
  r"otro por un camino con una inclinación de $20^\circ$ respecto a la horizontal (subiendo). "
  r"¿En cuál de los dos casos se realiza más trabajo?",
  r"En el camino inclinado: además de vencer el rozamiento, el motor debe aumentar la energía "
  r"potencial del carro, $mgd\operatorname{sen}20^\circ$.")
M(27, f"{ACT} — 9",
  r"Dos obreros suben cada uno una caneca de pintura del primer al segundo piso: uno por las "
  r"escaleras y otro por el frente de la casa con una polea. ¿Realizan los dos el mismo "
  r"trabajo? ¿Por qué?",
  r"Sí, si las canecas tienen igual masa y se suben con velocidad constante: el trabajo "
  r"contra la gravedad es $mgh$ y solo depende de la altura, no del camino. (El que sube por "
  r"las escaleras hace además trabajo para subir su propio cuerpo).")
M(28, f"{ACT} — 10",
  r"Una persona se para en un escalón de una escalera eléctrica y se queda quieta mientras "
  r"la escalera sube. ¿Realiza trabajo la persona? ¿Por qué?",
  r"No: sus pies no se desplazan respecto al escalón que empujan. Quien hace el trabajo es la "
  r"escalera (su motor), que aumenta la energía potencial de la persona.")
M(29, f"{ACT} — 11",
  r"Dos estudiantes discuten: uno afirma que se hace más trabajo al estirar un resorte una "
  r"distancia $x$ y el otro que al comprimirlo esa misma distancia. ¿Quién tiene la razón? "
  r"¿Por qué?",
  r"Ninguno: en un resorte ideal el trabajo es $\frac{1}{2}kx^2$ en los dos casos, porque "
  r"depende de $x^2$ y no del sentido de la deformación.")
M(30, f"{ACT} — 12a",
  r"Un balón de masa $m$ rueda por el suelo con velocidad $v_0$ hasta detenerse. ¿Qué fuerza "
  r"realiza trabajo?",
  r"La fuerza de rozamiento (fricción con el suelo y el aire), que se opone al movimiento. "
  r"El peso y la normal son perpendiculares al desplazamiento y no hacen trabajo.")


@E(31, f"{ACT} — 12b",
   enunciado=r"Un balón de masa $m$ rueda por el suelo con velocidad $v_0$ hasta detenerse. "
             r"¿Cuál es la expresión del trabajo realizado sobre la pelota?",
   respuesta=r"Por el teorema del trabajo y la energía, $W = \Delta E_c = 0 - "
             r"\frac{1}{2}mv_0^2 = -\frac{1}{2}mv_0^2$ (lo hace el rozamiento).")
def _():
    mm, v0 = sp.symbols("m v_0", positive=True)
    assert sp.simplify((0 - mm * v0**2 / 2) + mm * v0**2 / 2) == 0


M(32, f"{ACT} — 13",
  r"Plantea una situación en la que la energía cinética de un cuerpo se transforme en "
  r"energía potencial y otra en la que se transforme en calor.",
  r"Una pelota lanzada hacia arriba: su energía cinética se convierte en potencial "
  r"gravitacional al subir. Un carro que frena: su energía cinética se convierte en calor en "
  r"los frenos y las llantas.")
M(33, f"{ACT} — 14", r"¿Por qué una bombilla se calienta cuando se enciende?",
  r"Porque la corriente eléctrica que pasa por el filamento (o por los circuitos, en un "
  r"bombillo LED) transforma energía eléctrica en luz y, en buena parte, en energía térmica "
  r"(efecto Joule).")
M(34, f"{ACT} — 15",
  r"¿Qué consume más combustible, un auto pequeño o un camión de acarreos? ¿Por qué?",
  r"El camión: tiene mucha más masa, así que necesita más trabajo para acelerarlo y subir "
  r"pendientes ($\frac{1}{2}mv^2$, $mgh$) y sufre más rozamiento; esa energía sale del "
  r"combustible.")
M(35, f"{ACT} — 16", r"¿Es posible estirar un resorte ilimitadamente? ¿Por qué?",
  r"No: cada resorte tiene un límite de elasticidad. Más allá, la ley de Hooke deja de "
  r"cumplirse, el resorte queda deformado permanentemente y puede romperse.")
M(36, f"{ACT} — 17",
  r"¿Por qué la red de seguridad de los trapecistas en los circos debe quedar poco tensa?",
  r"Porque así se estira una distancia mayor al detener al artista: la misma energía "
  r"($W = Fd$) se absorbe con una fuerza menor, que no lo lastima.")
M(37, f"{ACT} — 18",
  r"¿Es posible que una pelota lanzada contra el suelo rebote y alcance una altura mayor que "
  r"aquella desde la que fue lanzada? ¿Por qué?",
  r"Sí, si se lanzó hacia abajo con cierta velocidad: además de la energía potencial tenía "
  r"energía cinética inicial, y en un rebote casi elástico puede subir hasta "
  r"$h_0 + v_0^2/2g$. Lo que no puede es superar la energía total que tenía al lanzarla. Si "
  r"solo se deja caer, no sube más alto que el punto de partida.")


@E(38, f"{ACT} — 19", tipo="seleccion",
   enunciado=r"Desde lo alto de un plano inclinado sin fricción, de altura $h$, se deja rodar "
             r"una esfera de masa $m$. La velocidad que alcanza la esfera depende de:" +
             op("la masa de la esfera.", "la altura del plano.",
                "el ángulo de inclinación del plano.", "la masa de la esfera y la altura del plano."),
   respuesta=r"b) La altura del plano: $mgh = \frac{1}{2}mv^2 \Rightarrow v = \sqrt{2gh}$, "
             r"que no depende de la masa ni del ángulo.",
   notas="Modelo de deslizamiento sin fricción (como en la guía); si la esfera rueda, "
         "v = √(10gh/7), que tampoco depende de la masa ni del ángulo.")
def _():
    mm, g, hh, v, th = sp.symbols("m g h v theta", positive=True)
    sol = sp.solve(sp.Eq(mm * g * hh, mm * v**2 / 2), v)[0]
    assert sol.free_symbols == {g, hh}


@E(39, f"{ACT} — 20", tipo="argumentacion",
   enunciado=r"Un bloque de masa $m$ que se mueve con rapidez $v$ choca contra un resorte sobre "
             r"una superficie horizontal sin rozamiento. Si se aumenta la rapidez del bloque, "
             r"¿qué pasa con la compresión del resorte?",
   respuesta=r"Aumenta en la misma proporción: $\frac{1}{2}mv^2 = \frac{1}{2}kx^2 \Rightarrow "
             r"x = v\sqrt{m/k}$; si $v$ se duplica, $x$ se duplica.")
def _():
    mm, k, v, x = sp.symbols("m k v x", positive=True)
    sol = sp.solve(sp.Eq(mm * v**2 / 2, k * x**2 / 2), x)[0]
    assert sp.simplify(sol.subs(v, 2 * v) / sol) == 2


# ---------- Problemas ----------

@E(40, f"{PROB} — 1", tipo="contexto",
   enunciado=r"Un panadero lleva horizontalmente una lata con pan de 6 kg y recorre "
             r"$\num{2,5}$ m. Luego la sube 50 cm para ubicarla en la parte superior del "
             r"horno. ¿Qué trabajo realizó el panadero?",
   respuesta=r"Al llevarla horizontalmente con velocidad constante no hace trabajo (su fuerza, "
             r"vertical, es perpendicular al desplazamiento). Al subirla: "
             r"$W = mgh = 6(\num{9,8})(\num{0,50}) \approx \num{29,4}$ J.")
def _():
    aprox(6 * kg * G * 50 * cm, 29.4, J, rel=1e-9)
    assert cos(radians(90)) < 1e-15        # tramo horizontal: fuerza ⟂ desplazamiento


@E(41, f"{PROB} — 2", tipo="contexto",
   enunciado=r"Un obrero levanta un bulto de cemento de 25 kg desde el suelo hasta una altura "
             r"de $\num{1,8}$ m. ¿Cuál es el trabajo realizado por la fuerza de gravedad?",
   respuesta=r"$W_g = -mgh = -25(\num{9,8})(\num{1,8}) = -441$ J (negativo: el peso se opone "
             r"a la subida).")
def _():
    aprox(-25 * kg * G * 1.8 * m, -441, J, rel=1e-9)


@E(42, f"{PROB} — 3",
   enunciado=r"Un niño lanza verticalmente hacia arriba su pelota de 500 g. Si sube $\num{2,6}$ m "
             r"respecto al punto de lanzamiento, ¿cuánto trabajo realiza la gravedad sobre la "
             r"pelota durante la subida?",
   respuesta=r"$W_g = -mgh = -\num{0,5}(\num{9,8})(\num{2,6}) \approx -\num{12,7}$ J.")
def _():
    aprox(-500 * gram * G * 2.6 * m, -12.74, J, rel=1e-6)


@E(43, f"{PROB} — 4",
   enunciado=r"Dos niños estiran una banda elástica 45 cm, halándola entre los dos. Si su "
             r"constante de elasticidad es de 60 N/m, ¿cuánto trabajo realizan sobre la banda?",
   respuesta=r"$W = \frac{1}{2}kx^2 = \frac{1}{2}(60)(\num{0,45})^2 \approx \num{6,1}$ J.")
def _():
    aprox(60 * N / m * (45 * cm)**2 / 2, 6.075, J, rel=1e-6)


@E(44, f"{PROB} — 5", tipo="contexto",
   enunciado=r"Un joven realiza un trabajo de 55 J al pasar horizontalmente una caja de "
             r"$\num{3,5}$ kg de un estante a otro separados $\num{2,2}$ m. ¿Qué aceleración "
             r"experimenta la caja?",
   respuesta=r"$F = W/d = 55/\num{2,2} = 25$ N; $a = F/m = 25/\num{3,5} \approx \num{7,1}\ "
             r"\mathrm{m/s^2}$.",
   notas="Se supone que la fuerza del joven es la fuerza neta (sin rozamiento) y constante.")
def _():
    f = 55 * J / (2.2 * m)
    aprox(f, 25, N, rel=1e-9)
    aprox(f / (3.5 * kg), 7.14, m / s**2, rel=0.002)


@E(45, f"{PROB} — 6a",
   enunciado=r"Un hombre empuja una caja 5 m aplicándole una fuerza horizontal de 45 N. Si la "
             r"fuerza de rozamiento es de 20 N, ¿cuánto vale el trabajo neto sobre la caja?",
   respuesta=r"$W_{\text{neto}} = (45 - 20)(5) = 125$ J.",
   notas="En la guía, el problema 6 une dos problemas distintos; se separan en 6a y 6b.")
def _():
    aprox((45 * N - 20 * N) * 5 * m, 125, J, rel=1e-9)


@E(46, f"{PROB} — 6b",
   enunciado=r"¿Cuál es la energía cinética de un automóvil de $\num{1000}$ kg que se mueve "
             r"por un camino recto con una rapidez constante de 45 km/h?",
   respuesta=r"$v = \num{12,5}$ m/s; $E_c = \frac{1}{2}(1000)(\num{12,5})^2 \approx "
             r"\num{7,8e4}$ J.",
   notas="En la guía falta la masa del automóvil; se agregó 1000 kg.")
def _():
    aprox(1000 * kg * (45 * km / h)**2 / 2, 78125, J, rel=1e-6)


@E(47, f"{PROB} — 7",
   enunciado=r"Un malabarista lanza hacia arriba un bolo de 100 g con una velocidad de 12 m/s. "
             r"¿Cuál es su energía cinética en el momento del lanzamiento? ¿Cuándo su energía "
             r"mecánica será solo potencial? ¿Cuál será su energía potencial gravitacional "
             r"máxima?",
   respuesta=r"$E_c = \frac{1}{2}(\num{0,1})(12)^2 = \num{7,2}$ J. En el punto más alto "
             r"($v = 0$) toda la energía es potencial, y $E_{p,\max} = \num{7,2}$ J (a "
             r"$h = 12^2/2g \approx \num{7,3}$ m).",
   notas="«Equilibrista» en la guía; se dice malabarista.")
def _():
    ec = 100 * gram * (12 * m / s)**2 / 2
    aprox(ec, 7.2, J, rel=1e-9)
    hmax = (12 * m / s)**2 / (2 * G)
    aprox(100 * gram * G * hmax, 7.2, J, rel=1e-9)


for _n, _lit, _preg, _resp, _check, _nota in [
        (48, "a", "¿Cuánto vale su energía potencial en el suelo?",
         r"0 J, tomando el suelo como nivel de referencia.",
         lambda: _es(val(3.5 * kg * G * (0 * m), J) == 0.0), None),
        (49, "b", "¿Cuál es su energía potencial gravitacional máxima?",
         r"$E_p = mgh = \num{3,5}(\num{9,8})(1) = \num{34,3}$ J.",
         lambda: aprox(3.5 * kg * G * 1 * m, 34.3, J, rel=1e-9), None),
        (50, "c", "Si lo suelta desde 1 m, ¿qué velocidad lleva cuando está a 50 cm del suelo?",
         r"$v = \sqrt{2g(1 - \num{0,5})} = \sqrt{\num{9,8}} \approx \num{3,1}$ m/s.",
         lambda: aprox(raiz(2 * G * 50 * cm, m / s), 3.13, m / s, rel=0.002),
         "La guía no dice que el camión se suelte; si el niño lo sube o baja con la mano, la "
         "velocidad no se puede calcular. Se añadió «si lo suelta desde 1 m»."),
        (51, "d", "Si lo suelta desde 1 m, ¿cuánto vale la energía mecánica cuando está a 30 cm "
                  "del suelo?",
         r"La misma de arriba, $\num{34,3}$ J: sin fricción la energía mecánica se conserva "
         r"($E_p = \num{10,3}$ J y $E_c = 24$ J).",
         lambda: aprox(3.5 * kg * G * 30 * cm + 3.5 * kg * G * 70 * cm, 34.3, J, rel=1e-9),
         "Se añadió «si lo suelta desde 1 m», como en el literal c.")]:
    @E(_n, f"{PROB} — 8{_lit}",
       enunciado=r"Un niño levanta su camión de madera de $\num{3,5}$ kg desde el suelo hasta "
                 r"una altura de 1 m. " + _preg, respuesta=_resp,
       **({"notas": _nota} if _nota else {}))
    def _(check=_check):
        check()

_NOTA9 = ("En la guía la energía potencial es de 22,5 J, que da una pelota de 0,57 kg, "
          "irreal para un juego de raqueta; con 2,25 J resulta 57 g, la masa de una pelota de "
          "tenis. Se corrigió a 2,25 J (la velocidad no cambia).")


@E(52, f"{PROB} — 9a", notas=_NOTA9,
   enunciado=r"Una pelota golpeada con una raqueta sube verticalmente 4 m y alcanza una "
             r"energía potencial de $\num{2,25}$ J. ¿Qué masa tiene la pelota?",
   respuesta=r"$m = \dfrac{E_p}{gh} = \dfrac{\num{2,25}}{\num{9,8}(4)} \approx \num{0,057}$ kg "
             r"(57 g).")
def _():
    aprox(2.25 * J / (G * 4 * m), 0.0574, kg, rel=0.002)
    aprox(22.5 * J / (G * 4 * m), 0.574, kg, rel=0.002)     # dato original: 0,57 kg


@E(53, f"{PROB} — 9b",
   enunciado=r"Una pelota golpeada verticalmente hacia arriba con una raqueta sube 4 m. ¿Con "
             r"qué velocidad fue lanzada?",
   respuesta=r"$v_0 = \sqrt{2gh} = \sqrt{2(\num{9,8})(4)} \approx \num{8,9}$ m/s.")
def _():
    aprox(raiz(2 * G * 4 * m, m / s), 8.85, m / s, rel=0.002)


@E(54, f"{PROB} — 10", tipo="contexto",
   enunciado=r"La propaganda de un automóvil de 1250 kg afirma que su motor le permite pasar "
             r"de 0 km/h a 90 km/h en $\num{4,5}$ segundos. ¿Qué potencia desarrolla el motor, "
             r"en HP ($1\ \text{HP} = 746$ W)?",
   respuesta=r"$W = \Delta E_c = \frac{1}{2}(1250)(25)^2 \approx \num{3,9e5}$ J; "
             r"$P = W/t \approx \num{8,7e4}$ W $\approx 116$ HP (potencia media, sin "
             r"pérdidas).")
def _():
    p = 1250 * kg * (90 * km / h)**2 / 2 / (4.5 * s)
    aprox(p, 8.68e4, W, rel=0.002)
    aprox(p, 116.4, HP, rel=0.002)


for _n, _lit, _preg, _resp, _q, _x in [
        (55, "a", "¿Cuánto vale su energía potencial?",
         r"$E_p = mgh = 1600(\num{9,8})(1800) \approx \num{2,8e7}$ J.",
         1600 * kg * G * 1800 * m, 2.82e7),
        (56, "b", "¿Cuál es el valor de su energía cinética?",
         r"$v = \num{83,3}$ m/s; $E_c = \frac{1}{2}(1600)(\num{83,3})^2 \approx \num{5,6e6}$ J.",
         1600 * kg * (300 * km / h)**2 / 2, 5.56e6)]:
    @E(_n, f"{PROB} — 11{_lit}",
       enunciado=r"Un helicóptero de 1600 kg vuela a 1800 m de altura con una velocidad de "
                 r"300 km/h. " + _preg, respuesta=_resp)
    def _(q=_q, x=_x):
        aprox(q, x, J, rel=0.003)

_M12, _H12 = (1950 + 3 * 55) * kg, 4 * 3 * m
for _n, _lit, _preg, _resp, _check in [
        (57, "a", "¿Cuál es el aumento de su energía potencial al llegar al quinto piso?",
         r"Masa total 2115 kg; sube 4 pisos $= 12$ m: $\Delta E_p = 2115(\num{9,8})(12) \approx "
         r"\num{2,49e5}$ J.",
         lambda: aprox(_M12 * G * _H12, 2.487e5, J, rel=0.002)),
        (58, "b", "¿Qué trabajo realiza el motor del ascensor y cuál es su potencia?",
         r"Con velocidad constante, el motor hace el trabajo que aumenta la energía potencial: "
         r"$W \approx \num{2,49e5}$ J; $P = W/t = \num{2,49e5}/18 \approx \num{1,4e4}$ W.",
         lambda: aprox(_M12 * G * _H12 / (18 * s), 1.38e4, W, rel=0.003))]:
    @E(_n, f"{PROB} — 12{_lit}", tipo="contexto", dificultad=2,
       enunciado=r"Un ascensor de 1950 kg lleva a tres personas de 55 kg cada una. Sube del "
                 r"primer al quinto piso en 18 s y cada piso tiene 3 m de alto. " + _preg,
       respuesta=_resp)
    def _(check=_check):
        check()


@E(59, f"{PROB} — 13", tipo="contexto",
   enunciado=r"Un montacargas sube cajas de 40 kg desde el suelo hasta 3 m de altura, 10 cajas "
             r"por viaje. Si tarda $\num{1,5}$ h en subir 800 cajas, ¿cuál es la potencia "
             r"que desarrolla?",
   respuesta=r"$W = 800(40)(\num{9,8})(3) \approx \num{9,4e5}$ J en $5400$ s: "
             r"$P \approx 174$ W (potencia útil media).")
def _():
    aprox(800 * 40 * kg * G * 3 * m / (1.5 * h), 174.2, W, rel=0.002)


@E(60, f"{PROB} — 14", tipo="contexto",
   enunciado=r"En el desfile del 20 de julio, un padre sube a su hijo de 18 kg sobre sus "
             r"hombros, a $\num{1,6}$ m de altura, en 3 s. ¿Cuánto trabajo realiza el padre "
             r"sobre el niño? ¿Qué potencia desarrolla?",
   respuesta=r"$W = mgh = 18(\num{9,8})(\num{1,6}) \approx 282$ J; $P = 282/3 \approx 94$ W.",
   notas="«Desfile de independencia» en la guía; se usa el 20 de julio. Se omite la edad.")
def _():
    w = 18 * kg * G * 1.6 * m
    aprox(w, 282.2, J, rel=0.001)
    aprox(w / (3 * s), 94.1, W, rel=0.001)


@E(61, f"{PROB} — 15", tipo="contexto",
   enunciado=r"En la estación, un bombero de 68 kg baja por un tubo de 4 m hasta el piso "
             r"donde está el carro de bomberos, en 5 segundos. ¿Qué trabajo realiza la fuerza "
             r"de gravedad sobre él? ¿Con qué potencia media lo hace?",
   respuesta=r"$W_g = mgh = 68(\num{9,8})(4) \approx \num{2,7e3}$ J; "
             r"$P = W/t \approx 533$ W.",
   notas="La guía pregunta «¿Qué trabajo realiza?» sin decir qué fuerza; se precisa que es el "
         "trabajo del peso.")
def _():
    w = 68 * kg * G * 4 * m
    aprox(w, 2665.6, J, rel=1e-6)
    aprox(w / (5 * s), 533.1, W, rel=0.001)


@E(62, f"{PROB} — 16", tipo="contexto", dificultad=2,
   enunciado=r"Un profesor de educación física lleva en una bolsa 15 balones de voleibol de "
             r"270 g cada uno. Si baja 6 m, del salón de profesores al patio, en 40 s, ¿cuál "
             r"es el peso de la bolsa con los balones? ¿Qué trabajo realiza el profesor sobre "
             r"la bolsa? ¿Qué potencia emplea?",
   respuesta=r"$m = 15(\num{0,27}) = \num{4,05}$ kg; peso $\approx \num{39,7}$ N. El profesor "
             r"sostiene la bolsa con una fuerza hacia arriba mientras baja 6 m: "
             r"$W = -\num{39,7}(6) \approx -238$ J. Potencia (en valor absoluto): "
             r"$238/40 \approx \num{5,95}$ W.",
   notas="Se desprecia la masa de la bolsa; el trabajo del profesor es negativo porque la "
         "fuerza es opuesta al desplazamiento.")
def _():
    peso = 15 * 270 * gram * G
    aprox(peso, 39.69, N, rel=1e-6)
    aprox(-peso * 6 * m, -238.1, J, rel=0.001)
    aprox(peso * 6 * m / (40 * s), 5.95, W, rel=0.002)


@E(63, f"{PROB} — 17", tipo="contexto", dificultad=2,
   enunciado=r"En un apartamento, cada día, se tienen encendidos 5 bombillos de 60 W durante "
             r"5 h, un televisor de 250 W durante 8 h, un microondas de 500 W durante 45 min y "
             r"una plancha de $\num{1000}$ W durante 20 min. Si el kW·h cuesta "
             r"\$\num{331,39}, ¿cuánto cuesta la energía consumida en un mes de 30 días?",
   respuesta=r"Por día: $1500 + 2000 + 375 + \num{333,3} \approx \num{4208}$ W·h "
             r"$= \num{4,21}$ kW·h; al mes, $\num{126,25}$ kW·h; costo "
             r"$\approx$ \$\num{41838}.",
   notas="Se supone un mes de 30 días.")
def _():
    kwh = 1000 * W * h
    dia = 5 * 60 * W * 5 * h + 250 * W * 8 * h + 500 * W * 45 * minute + 1000 * W * 20 * minute
    mes = val(30 * dia, kwh)
    assert abs(mes - 126.25) < 1e-6
    assert round(mes * 331.39) == 41838


@E(64, f"{PROB} — 18 (primera parte)",
   enunciado=r"Un niño lanza su pelota hacia arriba por un plano inclinado sin fricción. Si "
             r"recorre $\num{1,5}$ m sobre el plano y alcanza una altura de 90 cm, ¿con qué "
             r"velocidad la lanzó?",
   respuesta=r"$\frac{1}{2}mv_0^2 = mgh \Rightarrow v_0 = \sqrt{2(\num{9,8})(\num{0,90})} "
             r"\approx \num{4,2}$ m/s (la longitud del plano no se necesita).",
   notas="En la guía el problema 18 incluye pegado otro problema («13 Una flecha…»), que se "
         "registra aparte.")
def _():
    aprox(raiz(2 * G * 90 * cm, m / s), 4.2, m / s, rel=0.002)


_VF, _TH = 22 * m / s, radians(45)
for _n, _lit, _preg, _resp, _check in [
        (65, "a", "¿Cuál es su energía cinética en el punto más alto de su trayectoria?",
         r"Allí solo queda $v_x = 22\cos45^\circ \approx \num{15,6}$ m/s: "
         r"$E_c = \frac{1}{2}(\num{0,025})(\num{15,6})^2 \approx \num{3,0}$ J.",
         lambda: aprox(25 * gram * (_VF * cos(_TH))**2 / 2, 3.025, J, rel=0.002)),
        (66, "b", "¿Qué altura alcanza?",
         r"$h = \dfrac{(22\operatorname{sen}45^\circ)^2}{2g} \approx \num{12,3}$ m.",
         lambda: aprox((_VF * sin(_TH))**2 / (2 * G), 12.35, m, rel=0.002)),
        (67, "c", "¿Cuál es su energía potencial en el punto más alto de su trayectoria?",
         r"$E_p = mgh = \num{0,025}(\num{9,8})(\num{12,3}) \approx \num{3,0}$ J (la energía "
         r"cinética inicial, $\num{6,05}$ J, se reparte por mitades).",
         lambda: aprox(25 * gram * G * (_VF * sin(_TH))**2 / (2 * G), 3.025, J, rel=0.002))]:
    @E(_n, f"{PROB} — 18 (flecha, numerada «13» dentro del 18) {_lit}", tipo="contexto",
       dificultad=2,
       enunciado=r"Una flecha de 25 g se lanza con una velocidad de 22 m/s formando un ángulo "
                 r"de $45^\circ$ con la horizontal. El arquero está acostado (la flecha sale "
                 r"desde el nivel del suelo). " + _preg, respuesta=_resp)
    def _(check=_check):
        check()


@E(68, f"{PROB} — 19",
   enunciado=r"Un joven en su patineta se lanza desde el reposo por una rampa sin fricción de "
             r"8 m de altura. ¿Con qué velocidad llega al final de la rampa?",
   respuesta=r"$v = \sqrt{2gh} = \sqrt{2(\num{9,8})(8)} \approx \num{12,5}$ m/s.")
def _():
    aprox(raiz(2 * G * 8 * m, m / s), 12.52, m / s, rel=0.002)


@E(69, f"{PROB} — 20a", tipo="contexto",
   enunciado=r"Un niño de 35 kg se lanza desde el reposo por un tobogán sin fricción de "
             r"$\num{3,5}$ m de altura y luego se mueve por un plano horizontal con "
             r"coeficiente de rozamiento $\num{0,5}$, en el que se detiene. ¿Qué velocidad "
             r"tiene al empezar el recorrido horizontal?",
   respuesta=r"$v = \sqrt{2gh} = \sqrt{2(\num{9,8})(\num{3,5})} \approx \num{8,3}$ m/s.")
def _():
    aprox(raiz(2 * G * 3.5 * m, m / s), 8.28, m / s, rel=0.002)


@E(70, f"{PROB} — 20b", tipo="contexto",
   enunciado=r"El niño de 35 kg llega al plano horizontal (coeficiente de rozamiento "
             r"$\num{0,5}$) después de bajar por un tobogán sin fricción de $\num{3,5}$ m de "
             r"altura. ¿Qué distancia recorre en el plano antes de detenerse?",
   respuesta=r"El rozamiento disipa toda la energía: $\mu mgd = mgh \Rightarrow "
             r"d = h/\mu = \num{3,5}/\num{0,5} = 7$ m.")
def _():
    ec = 35 * kg * G * 3.5 * m
    aprox(ec / (0.5 * 35 * kg * G), 7, m, rel=1e-9)


@E(71, f"{PROB} — 21a",
   enunciado=r"Se requiere colgar una masa de 850 g para estirar un resorte 5 cm. ¿Cuál es la "
             r"constante de elasticidad del resorte?",
   respuesta=r"$k = \dfrac{mg}{x} = \dfrac{\num{0,85}(\num{9,8})}{\num{0,05}} \approx 167$ N/m.")
def _():
    aprox(850 * gram * G / (5 * cm), 166.6, N / m, rel=0.001)


@E(72, f"{PROB} — 21b",
   enunciado=r"Para estirar lentamente 5 cm un resorte de constante $k \approx 167$ N/m (el "
             r"que se estira 5 cm al colgarle 850 g), ¿qué trabajo se realiza?",
   respuesta=r"$W = \frac{1}{2}kx^2 = \frac{1}{2}(\num{166,6})(\num{0,05})^2 \approx "
             r"\num{0,21}$ J.",
   notas="Se interpreta como el trabajo para estirar el resorte lentamente (fuerza variable "
         "de 0 a mg), que es ½kx².")
def _():
    k = 850 * gram * G / (5 * cm)
    aprox(k * (5 * cm)**2 / 2, 0.208, J, rel=0.002)


@E(73, f"{PROB} — 22a",
   enunciado=r"Una fuerza de 45 N comprime un resorte 15 cm. Determina la constante de "
             r"elasticidad del resorte.",
   respuesta=r"$k = F/x = 45/\num{0,15} = 300$ N/m.")
def _():
    aprox(45 * N / (15 * cm), 300, N / m, rel=1e-9)


@E(74, f"{PROB} — 22b",
   enunciado=r"Una fuerza de 45 N comprime un resorte 15 cm. Determina la energía potencial "
             r"elástica almacenada.",
   respuesta=r"$E_p = \frac{1}{2}kx^2 = \frac{1}{2}(300)(\num{0,15})^2 \approx \num{3,4}$ J.")
def _():
    aprox(45 * N / (15 * cm) * (15 * cm)**2 / 2, 3.375, J, rel=1e-9)


@E(75, f"{PROB} — 23a",
   enunciado=r"Se deja caer una esfera de $\num{2,5}$ kg desde 4 m de altura sobre un resorte "
             r"vertical de constante 300 N/m apoyado en el suelo. ¿Con qué velocidad llega la "
             r"esfera al resorte?",
   respuesta=r"$v = \sqrt{2gh} = \sqrt{2(\num{9,8})(4)} \approx \num{8,9}$ m/s.",
   notas="Se toman los 4 m como la altura sobre el extremo superior del resorte.")
def _():
    aprox(raiz(2 * G * 4 * m, m / s), 8.85, m / s, rel=0.002)


@E(76, f"{PROB} — 23b", dificultad=3,
   enunciado=r"La esfera de $\num{2,5}$ kg cae desde 4 m sobre el resorte de 300 N/m. ¿Cuánto "
             r"se comprime el resorte?",
   respuesta=r"Toda la energía perdida, incluida la de los $x$ metros que baja al comprimirlo, "
             r"se almacena en el resorte: $mg(4 + x) = \frac{1}{2}kx^2$, o sea "
             r"$150x^2 - \num{24,5}x - 98 = 0$, y $x \approx \num{0,89}$ m. (Si se desprecia "
             r"ese tramo extra, $x = \sqrt{2mgh/k} \approx \num{0,81}$ m).")
def _():
    x = sp.symbols("x", positive=True)
    sol = sp.solve(sp.Eq(2.5 * 9.8 * (4 + x), 300 * x**2 / 2), x)
    assert len(sol) == 1 and abs(float(sol[0]) - 0.894) < 0.002
    aprox(raiz(2 * 2.5 * kg * G * 4 * m / (300 * N / m), m), 0.808, m, rel=0.003)
