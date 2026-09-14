"""Banco de ejercicios — Física 10° — Movimiento circular, gravitación universal y rotación de
sólidos (torque).
Fuente: Guía de apoyo de Física 10° «Movimiento circular, energía, fluidos y termodinámica»,
Capítulo 1 (el movimiento circular); se lee en
recursos/fisica/Guías pedagógicas Física/markdown/10 - Guia_de_Apoyo_movimiento_circular_energia_fluidos_y_termodinamica_grado_10_fisica.md
Secciones: Desarrolla tus competencias, Actividades, Problemas.
DBA: naturales grado 10 · DBA 1 (fuerza resultante no nula → cambio de velocidad: la fuerza
centrípeta cambia la dirección de la velocidad). Estándar 10°–11°: «Relaciono masa, distancia
y fuerza de atracción gravitacional entre objetos».
Datos de la guía: G = 6,67×10⁻¹¹ N·m²/kg²; Tierra M = 6,0×10²⁴ kg, R = 6,4×10⁶ m (Tabla 2),
órbita T = 3,15×10⁷ s, r = 1,5×10¹¹ m (Tabla 1); g = 9,8 m/s².
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/fisica/movimiento-circular-10.py
"""
from math import pi, sqrt

from sympy.physics.units import (centimeter, convert_to, hour, kilogram, kilometer, meter,
                                 minute, newton, pound, second)

from ejercicios import ejercicio, ejercicio_manual

PRE = "movimiento-circular-10"
G2 = ("Guía de apoyo Física 10° (movimiento circular, energía, fluidos y termodinámica), "
      "Cap. 1 El movimiento circular")
DES = f"{G2}, Desarrolla tus competencias"
ACT = f"{G2}, Actividades"
PROB = f"{G2}, Problemas"
COMUN = dict(tema="movimiento circular y gravitación", grados=[10], dba=["naturales-10-1"])

m, s, kg, N, cm, km = meter, second, kilogram, newton, centimeter, kilometer
GC = 6.67e-11 * N * m**2 / kg**2
MT, RT = 6.0e24 * kg, 6.4e6 * m
TT, AT = 3.15e7 * s, 1.5e11 * m          # período y radio de la órbita terrestre (Tabla 1)
G = 9.8 * m / s**2


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


# ---------- Desarrolla tus competencias ----------

M(1, f"{DES} — 1",
  r"El segundero de un reloj tiene movimiento circular uniforme y pasa por cada marca de un "
  r"segundo con la misma velocidad angular. Explica por qué.",
  r"Porque barre ángulos iguales en tiempos iguales: $6^\circ$ ($\pi/30$ rad) cada segundo. "
  r"Su velocidad angular es constante, $\omega = 2\pi/60\ \text{s} \approx \num{0,105}$ "
  r"rad/s, y por eso tarda lo mismo entre dos marcas cualesquiera.")
M(2, f"{DES} — 2",
  r"¿Puede afirmarse que la velocidad lineal de un cuerpo con movimiento circular uniforme "
  r"permanece constante? ¿Por qué?",
  r"No: su magnitud (la rapidez) es constante, pero su dirección cambia en cada punto "
  r"(siempre es tangente a la circunferencia), así que la velocidad como vector cambia.")


@E(3, f"{DES} — 3",
   enunciado=r"Un motor gira a razón de 840 r.p.m. ¿Cuánto tiempo, en segundos, tarda en dar "
             r"una vuelta?",
   respuesta=r"$T = \dfrac{60\ \text{s}}{840} \approx \num{0,071}$ s.")
def _():
    aprox(1 / (840 / minute), 0.0714, s, rel=0.002)


@E(4, f"{DES} — 4", tipo="contexto",
   enunciado=r"La velocidad de escape es la velocidad mínima que debe tener un objeto en la "
             r"superficie de un planeta para que, lanzado hacia arriba, no vuelva a caer; en un "
             r"planeta de masa $M$ y radio $R$ vale $v_{\text{escape}} = \sqrt{2GM/R}$. ¿Cuál "
             r"es la velocidad de escape de la Tierra ($M = \num{6,0e24}$ kg, "
             r"$R = \num{6,4e6}$ m)?",
   respuesta=r"$v = \sqrt{\dfrac{2(\num{6,67e-11})(\num{6,0e24})}{\num{6,4e6}}} \approx "
             r"\num{1,1e4}$ m/s ($\approx \num{11,2}$ km/s).")
def _():
    aprox(raiz(2 * GC * MT / RT, m / s), 1.12e4, m / s, rel=0.005)


@E(5, f"{DES} — 5", dificultad=2,
   enunciado=r"Dos ruedas de 18 cm y 27 cm de diámetro están unidas por una correa. Si la "
             r"rueda de mayor diámetro gira a 5 rad/s, ¿cuál es la frecuencia de la otra?",
   respuesta=r"La correa da la misma rapidez lineal a los dos bordes: "
             r"$v = 5(\num{0,135}) = \num{0,675}$ m/s; en la pequeña, "
             r"$\omega = \num{0,675}/\num{0,09} = \num{7,5}$ rad/s y "
             r"$f = \omega/2\pi \approx \num{1,2}$ Hz.")
def _():
    v = 5 / s * (27 * cm / 2)
    w2 = v / (18 * cm / 2)
    aprox(w2, 7.5, 1 / s, rel=1e-9)
    aprox(w2 / (2 * pi), 1.194, 1 / s, rel=0.001)


M(6, f"{DES} — 6",
  r"¿La magnitud de la aceleración centrípeta de un cuerpo con movimiento circular uniforme "
  r"es constante? ¿Por qué?",
  r"Sí: $a_c = v^2/r$ y en el movimiento circular uniforme $v$ y $r$ no cambian. Lo que cambia "
  r"es su dirección, que siempre apunta hacia el centro.")
M(7, f"{DES} — 7",
  r"¿Por qué un cuerpo con movimiento circular uniforme tiene aceleración, si la magnitud de "
  r"su velocidad no cambia?",
  r"Porque la aceleración mide cualquier cambio de la velocidad, también de dirección. En el "
  r"movimiento circular la dirección de la velocidad cambia continuamente, y la aceleración "
  r"centrípeta, dirigida hacia el centro, describe ese cambio.")


@E(8, f"{DES} — 7 (pregunta de selección que sigue a la 7, sin número)", tipo="seleccion",
   enunciado=r"La fuerza gravitacional entre dos cuerpos es $F_0$. Si la distancia entre ellos "
             r"se duplica, la fuerza $F$ sería:" + op(r"$F = 2F_0$", r"$F = 4F_0$",
                                                      r"$F = F_0/2$", r"$F = F_0/4$"),
   respuesta=r"d) $F = F_0/4$: la fuerza es inversamente proporcional al cuadrado de la "
             r"distancia, y $1/2^2 = 1/4$.",
   notas="En la guía esta pregunta no tiene número; está entre la 7 y la 8.")
def _():
    f = (1 / 2)**2
    assert [f == o for o in (2, 4, 1 / 2, 1 / 4)] == [False, False, False, True]


M(9, f"{DES} — 8",
  r"¿Cómo afecta la duración de las estaciones el hecho de que la Tierra se mueva más rápido "
  r"en su órbita durante el invierno del hemisferio norte que durante su verano?",
  r"Por la segunda ley de Kepler, la Tierra va más rápido cuando está más cerca del Sol "
  r"(en enero). Por eso recorre en menos tiempo la parte de la órbita correspondiente al "
  r"invierno del hemisferio norte: el invierno boreal dura unos días menos que el verano "
  r"boreal.")
M(10, f"{DES} — 9",
  r"¿Es diferente la velocidad angular de una persona en el Ecuador y la de otra en uno de "
  r"los polos, debido a la rotación de la Tierra? Explica.",
  r"No: la Tierra gira como un cuerpo rígido y todos sus puntos dan una vuelta en un día, "
  r"$\omega = 2\pi/24$ h. Lo que cambia es la velocidad lineal $v = \omega r$: es máxima en "
  r"el Ecuador (unos $\num{1670}$ km/h) y casi cero en los polos, donde la distancia al eje "
  r"es casi nula.")
M(11, f"{DES} — 10",
  r"Según la relatividad general, la gravedad de un astro puede desviar la luz. ¿Qué puedes "
  r"concluir de la masa de los agujeros negros, que no dejan escapar la luz?",
  r"Que tienen una masa enorme concentrada en un volumen muy pequeño: su gravedad es tan "
  r"intensa que la velocidad de escape supera la de la luz ($\sqrt{2GM/R} > c$).")
M(12, f"{DES} — 11",
  r"Da un ejemplo de un objeto que tenga un eje de rotación fijo y que se encuentre en "
  r"equilibrio.",
  r"Un balancín con dos niños que se equilibran (torque neto cero), una puerta quieta sobre "
  r"sus bisagras, o un ventilador que gira con velocidad angular constante (equilibrio de "
  r"rotación).")


@E(13, f"{DES} — 12", tipo="seleccion",
   enunciado=r"Dos objetos separados una distancia $r$ se atraen gravitacionalmente. ¿A qué "
             r"distancia se deben colocar para que su fuerza de atracción se duplique?" +
             op(r"$2r$", r"$r/4$", r"$r/\sqrt{2}$", r"$4r$"),
   respuesta=r"c) $r/\sqrt{2} \approx \num{0,71}\,r$: como $F \propto 1/d^2$, para "
             r"$F' = 2F$ se necesita $d'^2 = r^2/2$.",
   notas="En la guía ninguna opción es correcta (a. 2r, b. r/4, c. r/2, d. 4r): con r/2 la "
         "fuerza se cuadruplica. Se cambió la opción c por r/√2.")
def _():
    opciones = [2, 1 / 4, 1 / sqrt(2), 4]
    assert [abs(1 / d**2 - 2) < 1e-12 for d in opciones] == [False, False, True, False]
    assert abs(1 / (1 / 2)**2 - 4) < 1e-12        # la opción original r/2 cuadruplica


M(14, f"{DES} — 13", tipo="seleccion",
  enunciado=r"La afirmación «Los planetas están situados en esferas cuyo centro es la Tierra» "
            r"corresponde a:" + op("Copérnico.", "Aristóteles.", "Ptolomeo.", "Kepler."),
  respuesta=r"c) Ptolomeo, que desarrolló el modelo geocéntrico de esferas (iniciado por "
            r"Aristóteles, como dice la guía).",
  notas="Aristóteles también propuso esferas concéntricas a la Tierra; la guía atribuye el "
        "modelo a Ptolomeo. Conviene aceptar b o c, o precisar el enunciado.")
M(15, f"{DES} — 14", tipo="seleccion",
  enunciado=r"Cuando los rayos del Sol caen perpendicularmente sobre el paralelo "
            r"$\num{23,5}^\circ$ de latitud norte (trópico de Cáncer), se tiene un:" +
            op("equinoccio de primavera.", "solsticio de verano.", "solsticio de invierno.",
               "equinoccio de otoño."),
  respuesta=r"b) Solsticio de verano del hemisferio norte (hacia el 21 de junio).",
  notas="La guía dice «paralelo 23»; el trópico de Cáncer está a unos 23,5° N.")
M(16, f"{DES} — 15", tipo="seleccion",
  enunciado=r"El conjunto de leyes que describen el movimiento planetario recibe el nombre de:" +
            op("Leyes de Newton.", "Modelo geocéntrico.", "Leyes de Kepler.",
               "Modelo heliocéntrico."),
  respuesta=r"c) Leyes de Kepler.")


@E(17, f"{DES} — 16", dificultad=2,
   enunciado=r"¿A qué distancia del Sol estaría un planeta del sistema solar si su período de "
             r"revolución fuera de tres años? (La Tierra: $T = 1$ año, "
             r"$r = \num{1,5e11}$ m).",
   respuesta=r"Por la tercera ley de Kepler, $r^3 \propto T^2$: "
             r"$r = \num{1,5e11} \times 3^{2/3} \approx \num{3,1e11}$ m (unas $\num{2,1}$ UA).",
   notas="En la guía dice «período de rotación»; el que interviene en la ley de Kepler es el "
         "período de revolución (alrededor del Sol).")
def _():
    t = 3 * TT
    r = (val(AT**3 * t**2 / TT**2, m**3)) ** (1 / 3)
    assert abs(r - 3.12e11) < 0.01e11
    assert abs(r / 1.5e11 - 3**(2 / 3)) < 1e-9


M(18, f"{DES} — 17",
  r"¿Qué diferencia existe entre la masa inercial y la masa gravitacional de un cuerpo?",
  r"La masa inercial mide la resistencia del cuerpo a cambiar su velocidad ($m = F/a$, "
  r"segunda ley). La masa gravitacional mide cuánto lo atrae la gravedad (ley de "
  r"gravitación). Son conceptos distintos, pero los experimentos muestran que tienen el mismo "
  r"valor; por eso todos los cuerpos caen con la misma aceleración.")

# ---------- Actividades ----------


@E(19, f"{ACT} — 1",
   enunciado=r"Un disco da una vuelta en $\num{0,25}$ s. ¿Cuántas r.p.m. realiza?",
   respuesta=r"$f = 1/\num{0,25} = 4$ vueltas/s $= 240$ r.p.m.")
def _():
    aprox(1 / (0.25 * s), 240, 1 / minute, rel=1e-9)


for _n, _lit, _af, _resp in [
        (20, "a", "El número de revoluciones que realiza el cuerpo en la unidad de tiempo se "
                  "llama frecuencia.", "V."),
        (21, "b", "En un movimiento circular uniforme la velocidad angular está cambiando "
                  "respecto al tiempo.", "F: en el MCU la velocidad angular es constante."),
        (22, "c", "La fuerza centrípeta tiende a llevar los cuerpos hacia afuera de la curva.",
         "F: la fuerza centrípeta apunta hacia el centro de la curva."),
        (23, "d", "La fuerza centrípeta y la fuerza centrífuga son fuerzas de acción y "
                  "reacción.",
         "F: la «fuerza centrífuga» es una fuerza aparente que se percibe en un marco que "
         "gira; no es la reacción de la centrípeta (la reacción actúa sobre otro cuerpo)."),
        (24, "e", "La aceleración centrípeta se relaciona con el módulo de la velocidad lineal "
                  "del cuerpo.", r"V: $a_c = v^2/r$.")]:
    M(_n, f"{ACT} — 2{_lit}", "Escribe V si el enunciado es verdadero o F si es falso: " + _af,
      _resp)
M(25, f"{ACT} — 3", tipo="seleccion",
  enunciado=r"En un movimiento circular uniforme, la velocidad lineal es directamente "
            r"proporcional al radio de la trayectoria, y la constante de proporcionalidad es:" +
            op("el período.", "la frecuencia.", "la velocidad angular.",
               "la aceleración centrípeta."),
  respuesta=r"c) La velocidad angular: $v = \omega r$.")
M(26, f"{ACT} — 4", tipo="seleccion",
  enunciado=r"Una moneda pegada con plastilina a un disco que gira con movimiento circular "
            r"uniforme. ¿Cuál de las siguientes afirmaciones no es cierta? Justifica." +
            op("Recorre ángulos iguales en tiempos iguales.", "La velocidad lineal no cambia.",
               "Experimenta una aceleración centrípeta.",
               "Da el mismo número de vueltas en cada unidad de tiempo.",
               "Tiene velocidad tangencial."),
  respuesta=r"b): la rapidez es constante, pero la dirección de la velocidad lineal cambia en "
            r"cada punto. Las demás son ciertas.")
M(27, f"{ACT} — 5",
  r"¿De qué factores depende el mayor o menor ángulo de peralte que los constructores dan a "
  r"una curva de carretera?",
  r"De la velocidad para la que se diseña la curva y de su radio: $\tan\theta = v^2/(rg)$. A "
  r"mayor velocidad o menor radio, más peralte (también influye la fricción esperada entre "
  r"llantas y pavimento).")
M(28, f"{ACT} — 6",
  r"En el ciclismo de pista el velódromo es peraltado y los competidores se ubican en "
  r"diagonal para la salida. ¿Por qué?",
  r"El peralte hace que una componente de la fuerza normal apunte hacia el centro y dé la "
  r"fuerza centrípeta necesaria a alta velocidad sin depender solo de la fricción. La salida "
  r"en diagonal compensa que los carriles exteriores son más largos, para que todos recorran "
  r"la misma distancia.")
M(29, f"{ACT} — 7", dificultad=2,
  enunciado=r"Un camión viaja por una carretera recta con velocidad constante. ¿Cómo es la "
            r"velocidad angular en cada punto de una de sus llantas? ¿Es igual la velocidad "
            r"lineal en cada punto? ¿Por qué?",
  respuesta=r"La velocidad angular es la misma en todos los puntos (la llanta es rígida y "
            r"todos dan una vuelta en el mismo tiempo). La velocidad lineal no: respecto al "
            r"eje, $v = \omega r$ crece con la distancia al eje; respecto al suelo, el punto "
            r"de contacto está un instante en reposo y el punto más alto va al doble de la "
            r"velocidad del camión.")


for _n, _lit, _que in [(30, "a", "sus velocidades angulares"), (31, "b", "sus frecuencias")]:
    @E(_n, f"{ACT} — 8{_lit}", dificultad=2,
       enunciado=rf"En una bicicleta antigua, la relación entre los radios de las ruedas es de "
                 rf"3 a 1. ¿Qué puedes afirmar sobre la relación entre {_que}?",
       respuesta=r"Las dos ruedas avanzan con la bicicleta a la misma velocidad lineal, "
                 r"$v = \omega r$: la rueda grande gira con un tercio de la "
                 + ("velocidad angular" if _lit == "a" else "frecuencia") +
                 r" de la pequeña ($1 : 3$).")
    def _():
        v = 2 * m / s
        w_grande, w_peq = v / (3 * m / 10), v / (1 * m / 10)
        assert abs(val(w_grande / w_peq, 1) - 1 / 3) < 1e-12
        assert abs(val((w_grande / (2 * pi)) / (w_peq / (2 * pi)), 1) - 1 / 3) < 1e-12

M(32, f"{ACT} — 9",
  r"Una nave espacial debe ir a la Luna y volver. Si gasta más de la mitad del combustible en "
  r"el viaje de ida, ¿es posible que le alcance el que le queda para el regreso? Justifica.",
  r"Sí: en la ida la mayor parte del combustible se gasta en vencer la gravedad de la Tierra, "
  r"mucho más intensa que la de la Luna. Para regresar basta escapar de la débil gravedad "
  r"lunar; luego la Tierra atrae la nave.")
M(33, f"{ACT} — 10",
  r"Si todos los objetos son atraídos hacia el centro de la Tierra, ¿por qué la Luna no se "
  r"choca contra la Tierra?",
  r"Porque la Luna tiene una gran velocidad tangencial: la gravedad la desvía continuamente "
  r"hacia la Tierra (es la fuerza centrípeta de su órbita), pero mientras «cae» avanza lo "
  r"suficiente para no acercarse; está en órbita.")
M(34, f"{ACT} — 11",
  r"¿Cuándo es más rápido el movimiento de la Tierra: cuando está más cerca del Sol o cuando "
  r"está más lejos? Explica.",
  r"Cuando está más cerca (perihelio): por la segunda ley de Kepler el radio vector barre "
  r"áreas iguales en tiempos iguales, así que cerca del Sol debe recorrer más arco en el "
  r"mismo tiempo.")


@E(35, f"{ACT} — 12",
   enunciado=r"¿En qué factor aumentaría el peso de una persona si la masa de la Tierra fuera "
             r"cuatro veces mayor (con el mismo radio)?",
   respuesta=r"En un factor 4: $W = \dfrac{GMm}{R^2}$ es proporcional a $M$.")
def _():
    persona = 60 * kg
    w = GC * MT * persona / RT**2
    assert abs(val(GC * 4 * MT * persona / RT**2 / w, 1) - 4) < 1e-12


M(36, f"{ACT} — 13",
  r"Un satélite meteorológico se sale de su órbita. ¿Cómo piensas que será su trayectoria si "
  r"cae a la Tierra?",
  r"Una espiral que se va cerrando: el roce con la atmósfera le quita energía, su órbita se "
  r"hace cada vez más baja y al final entra en la atmósfera, donde se frena y en gran parte "
  r"se quema.")
M(37, f"{ACT} — 14",
  r"¿Cómo se verían afectados el Polo Norte y los países del Ecuador si la Luna no existiera?",
  r"No habría mareas lunares (solo las solares, más débiles) y, sobre todo, la Luna ya no "
  r"estabilizaría la inclinación del eje terrestre: esta podría variar mucho con el tiempo, "
  r"con cambios extremos de clima; por ejemplo, los polos podrían recibir mucho más sol y "
  r"el Ecuador mucho menos en ciertas épocas.")
M(38, f"{ACT} — 15",
  r"Las observaciones de Edwin Hubble demostraron que el universo está en expansión. ¿Estas "
  r"observaciones favorecen o contradicen la teoría gravitacional de Newton? Explica.",
  r"No la contradicen directamente: según Newton la gravedad, siempre atractiva, frenaría la "
  r"expansión, pero no la explica; la expansión viene de las condiciones iniciales (la Gran "
  r"Explosión). Para describir el universo en expansión se usa la relatividad general, más "
  r"completa que la teoría de Newton.")
M(39, f"{ACT} — 16",
  r"¿Puede compararse la atracción gravitacional de la Tierra sobre los cuerpos con la que "
  r"ejerce un imán sobre una puntilla de acero? ¿Por qué?",
  r"Solo en parte: ambas actúan a distancia. Pero la gravedad actúa sobre toda masa, siempre "
  r"atrae y es muy débil; la fuerza magnética solo actúa sobre ciertos materiales, puede "
  r"atraer o repeler y es mucho más intensa a distancias cortas (un imán pequeño levanta la "
  r"puntilla venciendo la atracción de toda la Tierra).")

# ---------- Problemas ----------

_R1, _T1 = 45 * cm / 2, 0.5 * s
for _n, _lit, _preg, _resp, _q, _u, _x in [
        (40, "a", "Período y frecuencia de su movimiento.",
         r"$T = \num{0,5}$ s; $f = 1/T = 2$ Hz.", 1 / _T1, 1 / s, 2),
        (41, "b", "Distancia que recorre al dar una vuelta.",
         r"$2\pi r = \pi(\num{0,45}\ \text{m}) \approx \num{1,41}$ m.", 2 * pi * _R1, m, 1.414),
        (42, "c", "Velocidad lineal.", r"$v = 2\pi r/T \approx \num{2,83}$ m/s.",
         2 * pi * _R1 / _T1, m / s, 2.827),
        (43, "d", "Velocidad angular.", r"$\omega = 2\pi/T = 4\pi \approx \num{12,6}$ rad/s.",
         2 * pi / _T1, 1 / s, 12.57),
        (44, "e", "Aceleración centrípeta.",
         r"$a_c = \omega^2 r = (4\pi)^2(\num{0,225}) \approx \num{35,5}\ \mathrm{m/s^2}$.",
         (2 * pi / _T1)**2 * _R1, m / s**2, 35.5)]:
    @E(_n, f"{PROB} — 1{_lit}",
       enunciado=r"Un carro de juguete da vueltas en una pista circular de 45 cm de diámetro y "
                 r"tarda $\num{0,5}$ s en dar una vuelta. Determina: " + _preg,
       respuesta=_resp)
    def _(q=_q, u=_u, x=_x):
        aprox(q, x, u, rel=0.002)

for _n, _lit, _preg, _resp, _q, _u, _x in [
        (45, "a", "el período del movimiento.",
         r"$T = \dfrac{60\ \text{s}}{2500} = \num{0,024}$ s.", 1 / (2500 / minute), s, 0.024),
        (46, "b", "su velocidad angular.",
         r"$\omega = 2\pi f = 2\pi\dfrac{2500}{60} \approx 262$ rad/s.",
         2 * pi * 2500 / minute, 1 / s, 261.8)]:
    @E(_n, f"{PROB} — 2{_lit}",
       enunciado=r"Un disco gira a razón de 2500 r.p.m. Determina " + _preg, respuesta=_resp)
    def _(q=_q, u=_u, x=_x):
        aprox(q, x, u, rel=0.001)

for _n, _lit, _preg, _resp, _q, _u, _x in [
        (47, "a", "¿Cuál es el período y la frecuencia de su movimiento?",
         r"$T = 8/10 = \num{0,8}$ s; $f = \num{1,25}$ Hz.", 10 / (8 * s), 1 / s, 1.25),
        (48, "b", "¿Con qué velocidad angular se mueve?",
         r"$\omega = 2\pi f = \num{2,5}\pi \approx \num{7,85}$ rad/s.",
         2 * pi * 10 / (8 * s), 1 / s, 7.854)]:
    @E(_n, f"{PROB} — 3{_lit}",
       enunciado=r"Un cuerpo se mueve uniformemente en una trayectoria circular de 20 cm de "
                 r"radio y da 10 vueltas en 8 segundos. " + _preg, respuesta=_resp)
    def _(q=_q, u=_u, x=_x):
        aprox(q, x, u, rel=0.001)

_W4, _R4 = 2 * pi / (0.25 * s), 6 * cm
for _n, _lit, _preg, _resp, _q, _u, _x in [
        (49, "a", "¿Cuál es su velocidad angular?",
         r"$\omega = 2\pi/\num{0,25} = 8\pi \approx \num{25,1}$ rad/s.", _W4, 1 / s, 25.13),
        (50, "b", "¿Con qué velocidad lineal se mueve un punto del borde?",
         r"$v = \omega r = 8\pi(\num{0,06}) \approx \num{1,51}$ m/s.", _W4 * _R4, m / s, 1.508),
        (51, "c", "¿Qué aceleración centrípeta tiene un punto del borde?",
         r"$a_c = \omega^2 r \approx \num{37,9}\ \mathrm{m/s^2}$.", _W4**2 * _R4, m / s**2, 37.9)]:
    @E(_n, f"{PROB} — 4{_lit}",
       enunciado=r"Una polea de 12 cm de diámetro gira con un período de $\num{0,25}$ s. " + _preg,
       respuesta=_resp)
    def _(q=_q, u=_u, x=_x):
        aprox(q, x, u, rel=0.002)


@E(52, f"{PROB} — 5",
   enunciado=r"La llanta de una bicicleta tiene 45 cm de diámetro y da 10 vueltas en "
             r"4 segundos. ¿Cuál es su período, su frecuencia y su velocidad angular? ¿Qué "
             r"rapidez lineal tiene un punto del borde de la llanta?",
   respuesta=r"$T = \num{0,4}$ s; $f = \num{2,5}$ Hz; $\omega = 5\pi \approx \num{15,7}$ rad/s; "
             r"$v = \omega r = 5\pi(\num{0,225}) \approx \num{3,53}$ m/s.")
def _():
    f = 10 / (4 * s)
    aprox(1 / f, 0.4, s, rel=1e-9)
    aprox(2 * pi * f, 15.71, 1 / s, rel=0.001)
    aprox(2 * pi * f * 45 * cm / 2, 3.53, m / s, rel=0.002)


@E(53, f"{PROB} — 6a", tipo="contexto",
   enunciado=r"La rapidez orbital de la Luna es de aproximadamente $\num{1,03}$ km/s y su "
             r"distancia promedio a la Tierra es $\num{3,84e8}$ m. Suponiendo movimiento "
             r"circular uniforme, ¿cuál es su período de revolución?",
   respuesta=r"$T = \dfrac{2\pi r}{v} = \dfrac{2\pi(\num{3,84e8})}{\num{1,03e3}} \approx "
             r"\num{2,34e6}$ s $\approx 27$ días.",
   notas="La guía dice «período de rotación»; es el de revolución alrededor de la Tierra.")
def _():
    from sympy.physics.units import day
    t = 2 * pi * 3.84e8 * m / (1.03 * km / s)
    aprox(t, 2.34e6, s, rel=0.002)
    aprox(t, 27.1, day, rel=0.003)


@E(54, f"{PROB} — 6b", tipo="contexto",
   enunciado=r"La Luna gira alrededor de la Tierra a $\num{1,03}$ km/s en una órbita de radio "
             r"$\num{3,84e8}$ m. ¿Cuál es su aceleración centrípeta?",
   respuesta=r"$a_c = \dfrac{v^2}{r} = \dfrac{(\num{1,03e3})^2}{\num{3,84e8}} \approx "
             r"\num{2,76e-3}\ \mathrm{m/s^2}$.")
def _():
    aprox((1.03 * km / s)**2 / (3.84e8 * m), 2.76e-3, m / s**2, rel=0.002)


_V7, _R7 = 15 * m / s, 3.2 * m
for _n, _lit, _preg, _resp, _q, _u, _x in [
        (55, "a", "¿Cuántas vueltas da el aspa en un segundo?",
         r"$f = \dfrac{v}{2\pi r} = \dfrac{15}{2\pi(\num{3,2})} \approx \num{0,75}$ vueltas/s.",
         _V7 / (2 * pi * _R7), 1 / s, 0.746),
        (56, "b", "¿Cuál es su velocidad angular?",
         r"$\omega = v/r = 15/\num{3,2} \approx \num{4,7}$ rad/s.", _V7 / _R7, 1 / s, 4.6875),
        (57, "c", "¿Cuánto tiempo tarda el aspa en dar una vuelta?",
         r"$T = 1/f \approx \num{1,34}$ s.", 2 * pi * _R7 / _V7, s, 1.340)]:
    @E(_n, f"{PROB} — 7{_lit}",
       enunciado=r"Las aspas de un molino de viento miden $\num{3,2}$ m. Un punto del borde de "
                 r"una de ellas se mueve a 15 m/s. " + _preg, respuesta=_resp)
    def _(q=_q, u=_u, x=_x):
        aprox(q, x, u, rel=0.002)

_A8, _R8 = 6.52 * m / s**2, 50 * m
for _n, _lit, _preg, _resp, _check in [
        (58, "a", "¿Cuál es su velocidad lineal?",
         r"$v = \sqrt{a_c r} = \sqrt{\num{6,52}(50)} \approx \num{18,1}$ m/s.",
         lambda: aprox(raiz(_A8 * _R8, m / s), 18.06, m / s, rel=0.002)),
        (59, "b", "¿Cuánto tarda en dar una vuelta?",
         r"$T = 2\pi r/v \approx \num{17,4}$ s.",
         lambda: aprox(2 * pi * _R8 / raiz(_A8 * _R8, m / s), 17.4, s, rel=0.003)),
        (60, "c", "¿Cuál es su velocidad angular?",
         r"$\omega = v/r \approx \num{0,361}$ rad/s.",
         lambda: aprox(raiz(_A8 * _R8, m / s) / _R8, 0.361, 1 / s, rel=0.003)),
        (61, "d", "¿Qué fuerza de fricción actúa sobre el patinador si su masa es de 52 kg?",
         r"La fricción es la fuerza centrípeta: $F = ma_c = 52(\num{6,52}) \approx 339$ N.",
         lambda: aprox(52 * kg * _A8, 339, N, rel=0.002))]:
    @E(_n, f"{PROB} — 8{_lit}", tipo="contexto",
       enunciado=r"Un patinador recorre una pista circular de 50 m de radio con una aceleración "
                 r"centrípeta de $\num{6,52}\ \mathrm{m/s^2}$. " + _preg, respuesta=_resp)
    def _(check=_check):
        check()

_NOTA9 = ("Dato de la guía conservado (0,6 rev/s), pero da una aceleración de unas 4,3 g, "
          "irreal para una rueda de Chicago; la docente podría cambiarlo, p. ej., a 0,1 rev/s.")
for _n, _lit, _preg, _resp, _q, _u, _x in [
        (62, "a", "¿Cuál es la velocidad angular de la rueda?",
         r"$\omega = 2\pi(\num{0,6}) \approx \num{3,77}$ rad/s.", 2 * pi * 0.6 / s, 1 / s, 3.77),
        (63, "b", "¿Qué aceleración centrípeta experimenta una persona montada en la rueda?",
         r"$a_c = \omega^2 r = (\num{3,77})^2(3) \approx \num{42,6}\ \mathrm{m/s^2}$.",
         (2 * pi * 0.6 / s)**2 * 3 * m, m / s**2, 42.6)]:
    @E(_n, f"{PROB} — 9{_lit}", tipo="contexto", notas=_NOTA9,
       enunciado=r"En un parque de diversiones, la rueda de Chicago tiene 6 m de diámetro y "
                 r"gira a razón de $\num{0,6}$ revoluciones por segundo. " + _preg,
       respuesta=_resp)
    def _(q=_q, u=_u, x=_x):
        aprox(q, x, u, rel=0.002)


@E(64, f"{PROB} — 10", tipo="contexto", dificultad=2,
   enunciado=r"Un automóvil con ruedas de 80 cm de diámetro parte del reposo y acelera "
             r"uniformemente hasta 72 km/h en 20 s. ¿Cuántas vueltas da cada rueda en ese "
             r"tiempo?",
   respuesta=r"Recorre $x = \frac{0 + 20}{2}(20) = 200$ m; cada vuelta avanza "
             r"$2\pi(\num{0,40}) \approx \num{2,51}$ m: unas 80 vueltas ($\approx \num{79,6}$).")
def _():
    x = (72 * km / hour) / 2 * (20 * s)
    aprox(x, 200, m, rel=1e-9)
    aprox(x / (2 * pi * 40 * cm), 79.6, 1, rel=0.002)


_W11 = 2 * pi * 20000 / minute
for _n, _lit, _preg, _resp, _q, _u, _x in [
        (65, "a", "¿Qué velocidad angular alcanza al cabo de los 8 s?",
         r"$\omega = 2\pi\dfrac{\num{20000}}{60} \approx \num{2,09e3}$ rad/s.", _W11, 1 / s, 2094),
        (66, "b", "¿Cuál es su aceleración angular?",
         r"$\alpha = \omega/t \approx 262\ \mathrm{rad/s^2}$.", _W11 / (8 * s), 1 / s**2, 261.8),
        (67, "c", "¿Cuántas vueltas da en los 8 segundos?",
         r"$\theta = \frac{1}{2}\omega t$: $\frac{1}{2}(\num{20000}/60)(8) \approx \num{1,33e3}$ "
         r"vueltas.", (20000 / minute) / 2 * (8 * s), 1, 1333)]:
    @E(_n, f"{PROB} — 11{_lit}",
       enunciado=r"La hélice de un avión parte del reposo y, con aceleración angular constante, "
                 r"a los 8 s gira a $\num{20000}$ r.p.m. " + _preg, respuesta=_resp)
    def _(q=_q, u=_u, x=_x):
        aprox(q, x, u, rel=0.002)


@E(68, f"{PROB} — 12", tipo="contexto",
   enunciado=r"¿Qué aceleración de la gravedad experimenta un avión que vuela a 12 km de "
             r"altura sobre la superficie terrestre ($M_T = \num{6,0e24}$ kg, "
             r"$R_T = \num{6,4e6}$ m)?",
   respuesta=r"$g = \dfrac{GM_T}{(R_T + h)^2} = \dfrac{(\num{6,67e-11})(\num{6,0e24})}"
             r"{(\num{6,412e6})^2} \approx \num{9,73}\ \mathrm{m/s^2}$, apenas un "
             r"$\num{0,4}\,\%$ menos que en la superficie.")
def _():
    assert convert_to(12 * km, m) == 12000 * m
    g_h = GC * MT / ((6.4e6 + 12e3) * m)**2
    aprox(g_h, 9.73, m / s**2, rel=0.002)
    assert abs(val(g_h / (GC * MT / RT**2), 1) - 0.9963) < 0.0005


@E(69, f"{PROB} — 13", tipo="argumentacion", dificultad=2,
   enunciado=r"Un joven astrónomo anuncia haber descubierto un pequeño planeta del sistema "
             r"solar con un período de revolución de $\num{4,5}$ años y una distancia media al "
             r"Sol de $\num{9650}$ km. ¿Es cierta la afirmación? ¿Por qué?",
   respuesta=r"No. Por la tercera ley de Kepler, con $T = \num{4,5}$ años el radio de la órbita "
             r"debe ser $r = \num{1,5e11} \times \num{4,5}^{2/3} \approx \num{4,1e11}$ m "
             r"($\approx \num{2,7}$ UA). Además, $\num{9650}$ km es menos que el radio del "
             r"propio Sol ($\num{7,0e8}$ m).",
   notas="La guía dice «período de rotación»; es el de revolución.")
def _():
    r = val(AT**3 * (4.5 * TT)**2 / TT**2, m**3) ** (1 / 3)
    assert abs(r - 4.09e11) < 0.02e11
    assert 9650e3 < 7.0e8 < r


@E(70, f"{PROB} — 14",
   enunciado=r"Dos personas sentadas en los extremos de un café internet están separadas "
             r"$\num{3,5}$ m. Si sus masas son 52 kg y 61 kg, ¿qué fuerza de atracción "
             r"gravitacional existe entre ellas?",
   respuesta=r"$F = G\dfrac{m_1 m_2}{d^2} = \dfrac{(\num{6,67e-11})(52)(61)}{\num{3,5}^2} "
             r"\approx \num{1,7e-8}$ N.")
def _():
    aprox(GC * 52 * kg * 61 * kg / (3.5 * m)**2, 1.73e-8, N, rel=0.003)


@E(71, f"{PROB} — 15", dificultad=2,
   enunciado=r"¿A qué altura sobre la superficie terrestre la aceleración de la gravedad es "
             r"$g/2$? ($R_T = \num{6,4e6}$ m).",
   respuesta=r"$\dfrac{GM}{(R + h)^2} = \dfrac{1}{2}\dfrac{GM}{R^2} \Rightarrow "
             r"R + h = \sqrt{2}\,R$, $h = (\sqrt{2} - 1)R \approx \num{2,65e6}$ m "
             r"($\approx \num{2650}$ km).")
def _():
    hh = (sqrt(2) - 1) * RT
    aprox(hh, 2.65e6, m, rel=0.002)
    aprox(GC * MT / (RT + hh)**2 / (GC * MT / RT**2), 0.5, 1, rel=1e-9)


@E(72, f"{PROB} — 16",
   enunciado=r"Dos esferas de igual tamaño y 300 lb de masa cada una están separadas "
             r"$\num{2,5}$ m. ¿Cuál es la fuerza de atracción gravitacional entre ellas? "
             r"($1\ \text{lb} = \num{0,4536}$ kg).",
   respuesta=r"$m = 300\ \text{lb} \approx 136$ kg; $F = \dfrac{(\num{6,67e-11})(136)^2}"
             r"{\num{2,5}^2} \approx \num{2,0e-7}$ N.",
   notas="Se supone que las 2,5 m son la distancia entre los centros.")
def _():
    aprox(300 * pound, 136.1, kg, rel=0.001)
    aprox(GC * (300 * pound)**2 / (2.5 * m)**2, 1.98e-7, N, rel=0.003)


@E(73, f"{PROB} — 17", tipo="contexto",
   enunciado=r"La fuerza de atracción gravitacional entre dos automóviles parqueados es de "
             r"$\num{9,5e-6}$ N. Si sus masas son 1200 kg y 1450 kg, ¿a qué distancia está "
             r"uno del otro?",
   respuesta=r"$d = \sqrt{\dfrac{Gm_1m_2}{F}} = \sqrt{\dfrac{(\num{6,67e-11})(1200)(1450)}"
             r"{\num{9,5e-6}}} \approx \num{3,5}$ m.",
   notas="En la guía la fuerza aparece como «9,5  1024 N» (se perdieron el signo × y el signo "
         "menos del exponente). Con 10⁻⁶ la distancia es 3,5 m, realista; se usa 9,5×10⁻⁶ N.")
def _():
    aprox(raiz(GC * 1200 * kg * 1450 * kg / (9.5e-6 * N), m), 3.5, m, rel=0.005)


@E(74, f"{PROB} — 18", tipo="contexto",
   enunciado=r"Dos aviones esperan pista sobrevolando un aeropuerto. En cierto momento están a "
             r"850 m uno del otro y la fuerza de atracción entre ellos es de $\num{3,8e-9}$ N. "
             r"Si uno tiene una masa de 5 toneladas, ¿cuál es la masa del otro?",
   respuesta=r"$m_2 = \dfrac{Fd^2}{Gm_1} = \dfrac{(\num{3,8e-9})(850)^2}{(\num{6,67e-11})"
             r"(5000)} \approx \num{8,2e3}$ kg (unas $\num{8,2}$ toneladas).",
   notas="En la guía la fuerza aparece como «3,8  1029 N» (se perdieron el × y el signo del "
         "exponente). Con 10⁻⁹ la masa sale 8,2 t, realista para un avión; se usa 3,8×10⁻⁹ N.")
def _():
    aprox(3.8e-9 * N * (850 * m)**2 / (GC * 5000 * kg), 8.23e3, kg, rel=0.003)


@E(75, f"{PROB} — 19a", tipo="contexto", dificultad=2,
   enunciado=r"Calixto, una luna de Júpiter, tarda 384 horas en dar una vuelta alrededor del "
             r"planeta, en una órbita de radio $\num{1,9e6}$ km. ¿Cuál es la masa de Júpiter?",
   respuesta=r"La gravedad es la fuerza centrípeta: $\dfrac{GM}{r^2} = \dfrac{4\pi^2 r}{T^2} "
             r"\Rightarrow M = \dfrac{4\pi^2 r^3}{GT^2} = \dfrac{4\pi^2(\num{1,9e9})^3}"
             r"{(\num{6,67e-11})(\num{1,38e6})^2} \approx \num{2,1e27}$ kg.",
   notas="«Período de rotación» en la guía: es el de revolución alrededor de Júpiter. La "
         "masa real de Júpiter es 1,9×10²⁷ kg (el período real de Calixto es de 400 h).")
def _():
    r, t = 1.9e6 * km, 384 * hour
    aprox(4 * pi**2 * r**3 / (GC * t**2), 2.12e27, kg, rel=0.005)


@E(76, f"{PROB} — 19b", dificultad=2,
   enunciado=r"Si la masa de Júpiter se redujera a la mitad, ¿cuál sería el período de "
             r"revolución de Calixto (hoy 384 h), en la misma órbita?",
   respuesta=r"$T = 2\pi\sqrt{\dfrac{r^3}{GM}}$: con $M/2$ el período se multiplica por "
             r"$\sqrt{2}$, $T \approx 384\sqrt{2} \approx 543$ h.")
def _():
    r = 1.9e6 * km
    mj = 4 * pi**2 * r**3 / (GC * (384 * hour)**2)
    t2 = 2 * pi * raiz(r**3 / (GC * mj / 2), s)
    aprox(t2, 543, hour, rel=0.002)


@E(77, f"{PROB} — 20",
   enunciado=r"¿Qué torque realiza una fuerza de 35 N aplicada perpendicularmente sobre una "
             r"barra a 20 cm de su punto de apoyo?",
   respuesta=r"$\tau = Fd = 35(\num{0,20}) = 7$ N·m.",
   notas="La guía no dice que la fuerza sea perpendicular; se agrega para que el problema "
         "tenga una sola respuesta.")
def _():
    aprox(35 * N * 20 * cm, 7.0, N * m, rel=1e-9)


@E(78, f"{PROB} — 21",
   enunciado=r"¿Cuál es el torque realizado por una fuerza de 18 N aplicada perpendicularmente "
             r"sobre una barra a 45 cm de su punto de apoyo?",
   respuesta=r"$\tau = 18(\num{0,45}) = \num{8,1}$ N·m.")
def _():
    aprox(18 * N * 45 * cm, 8.1, N * m, rel=1e-9)


@E(79, f"{PROB} — 22a", tipo="contexto",
   enunciado=r"Un mecánico aplica una fuerza de 20 N, perpendicular a la llave, en el extremo "
             r"de una llave de 24 cm de longitud para soltar una tuerca de una llanta. ¿Qué "
             r"torque realiza?",
   respuesta=r"$\tau = 20(\num{0,24}) = \num{4,8}$ N·m.",
   notas="En la guía el enunciado empieza con un «15» sobrante («22. 15 Un mecánico…»).")
def _():
    aprox(20 * N * 24 * cm, 4.8, N * m, rel=1e-9)


@E(80, f"{PROB} — 22b", tipo="contexto",
   enunciado=r"Si el mecánico anterior usara una extensión de 10 cm en la llave de 24 cm, ¿qué "
             r"fuerza debería aplicar para producir el mismo torque de $\num{4,8}$ N·m?",
   respuesta=r"$F = \dfrac{\tau}{d} = \dfrac{\num{4,8}}{\num{0,34}} \approx 14$ N.")
def _():
    aprox(20 * N * 24 * cm / (34 * cm), 14.1, N, rel=0.002)
