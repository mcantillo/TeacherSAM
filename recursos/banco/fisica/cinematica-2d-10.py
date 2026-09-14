"""Banco de ejercicios — Física 10° — Cinemática en dos dimensiones: vectores, movimiento de
proyectiles y velocidad relativa.
Fuente: Guía de apoyo de Física 10° «Cinemática y dinámica», Capítulo 3 (Cinemática en dos o en
tres dimensiones: Vectores); se lee en
recursos/fisica/Guías pedagógicas Física/markdown/10 - Guia_de_apoyo_cinematica_y_dinamica_grado_10_fisica.md
Secciones: «Practiquemos» (dentro del texto), Preguntas, Problemas.
DBA: naturales grado 10 · DBA 1 (cambios de velocidad en presencia de fuerzas; el proyectil es
el caso de fuerza neta constante).
g = 9,8 m/s².
Problemas 5 y 6: en la guía falta la ecuación de la posición (era una imagen que no pasó al
texto). Se reconstruyó con el problema original de Giancoli, Física para ciencias e ingeniería,
cap. 3: r = (9,60t i + 8,85 j − 1,00t² k) m. La docente debe confirmarla.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/fisica/cinematica-2d-10.py
"""
from math import asin, atan2, cos, degrees, hypot, radians, sin, sqrt

import sympy as sp
from sympy.physics.units import convert_to, kilogram, kilometer, meter, second

from ejercicios import ejercicio, ejercicio_manual

PRE = "cinematica-2d-10"
G1 = "Guía de apoyo Física 10° (cinemática y dinámica), Cap. 3 Cinemática en dos dimensiones"
PRAC = f"{G1}, Practiquemos"
PREG = f"{G1}, Preguntas"
PROB = f"{G1}, Problemas"
COMUN = dict(tema="cinemática en dos dimensiones", grados=[10], dba=["naturales-10-1"])

m, s, km = meter, second, kilometer
G = 9.8 * m / s**2
g = 9.8


def _meta(n, fuente, enunciado, respuesta, kw, tipo):
    d = dict(id=f"{PRE}-{n:03d}", fuente=fuente, enunciado=enunciado, respuesta=respuesta,
             tipo=tipo, dificultad=1, **COMUN)
    d.update(kw)
    return d


def E(n, fuente, enunciado, respuesta, **kw):
    return ejercicio(**_meta(n, fuente, enunciado, respuesta, kw, "calculo"))


def M(n, fuente, enunciado, respuesta, **kw):
    ejercicio_manual(**_meta(n, fuente, enunciado, respuesta, kw, "conceptual"))


def val(q, unidad):
    """Número de «unidad» que hay en q (unidad=1: cociente adimensional); falla si las
    dimensiones no coinciden."""
    if unidad == 1:
        return float(convert_to(q, [meter, kilogram, second]))
    return float(convert_to(q, unidad) / unidad)


def aprox(q, esperado, unidad, rel=0.01):
    v = val(q, unidad)
    assert abs(v - esperado) <= rel * abs(esperado), f"{v} ≠ {esperado}"


def cerca(x, esperado, rel=0.005):
    assert abs(x - esperado) <= rel * abs(esperado), f"{x} ≠ {esperado}"


# ---------- Practiquemos ----------

M(1, f"{PRAC} (suma de vectores) — 1",
  r"Un desplazamiento $\vec D_1$ de $\num{10,0}$ km al este y otro $\vec D_2$ de "
  r"$\num{5,0}$ km al norte dan una resultante de $\num{11,2}$ km. ¿En qué condiciones la "
  r"magnitud de la resultante de dos vectores es $D_R = D_1 + D_2$?",
  r"Solo cuando los dos vectores tienen la misma dirección y el mismo sentido (son "
  r"paralelos y apuntan hacia el mismo lado). En cualquier otro caso $D_R < D_1 + D_2$.")

# ---------- Preguntas ----------

M(2, f"{PREG} — 1",
  r"Un automóvil viaja hacia el este a 40 km/h y otro hacia el norte a 40 km/h. ¿Son "
  r"iguales sus velocidades? Explica.",
  r"No: tienen la misma rapidez, pero la velocidad es un vector y sus direcciones son "
  r"distintas.")
M(3, f"{PREG} — 2",
  r"¿Puedes concluir que un automóvil no está acelerando si el velocímetro marca "
  r"constantemente 60 km/h?",
  r"No: el velocímetro solo indica la rapidez. Si el carro toma una curva, la dirección de "
  r"su velocidad cambia y hay aceleración.")
M(4, f"{PREG} — 3",
  r"Da varios ejemplos de un objeto que recorre una gran distancia pero cuyo desplazamiento "
  r"es cero.",
  r"Un atleta que da una vuelta completa a la pista; un bus que hace su recorrido y vuelve "
  r"al paradero; la Tierra al completar una órbita alrededor del Sol.")
M(5, f"{PREG} — 4",
  r"¿La magnitud del desplazamiento de una partícula que se mueve en dos dimensiones puede "
  r"ser mayor que la longitud de la trayectoria recorrida en el mismo intervalo? ¿Puede ser "
  r"menor? Explica.",
  r"Mayor, nunca: la línea recta es el camino más corto entre dos puntos. Menor, sí, siempre "
  r"que la trayectoria no sea una recta recorrida en un solo sentido; son iguales solo en "
  r"ese caso.")
M(6, f"{PREG} — 5",
  r"Un jugador de béisbol batea una pelota muy elevada, corre en línea recta y la atrapa. "
  r"¿Quién tuvo mayor desplazamiento, el jugador o la pelota?",
  r"Tienen el mismo desplazamiento (aproximadamente): los dos empiezan en el mismo sitio y "
  r"terminan en el mismo sitio. La pelota recorre una trayectoria más larga, pero eso es la "
  r"distancia, no el desplazamiento.")


@E(7, f"{PREG} — 6",
   enunciado=r"Dos vectores tienen magnitudes $V_1 = \num{3,5}$ km y $V_2 = \num{4,0}$ km. "
             r"¿Cuáles son las magnitudes máxima y mínima de su suma vectorial?",
   respuesta=r"Máxima: $\num{7,5}$ km (mismo sentido); mínima: $\num{0,5}$ km (sentidos "
             r"opuestos).")
def _():
    mags = [hypot(3.5 + 4.0 * cos(radians(a)), 4.0 * sin(radians(a))) for a in range(0, 361)]
    cerca(max(mags), 7.5, 1e-9)
    cerca(min(mags), 0.5, 1e-9)


M(8, f"{PREG} — 7",
  r"¿Pueden sumarse dos vectores de distinta magnitud y dar el vector cero? ¿Es posible con "
  r"tres vectores desiguales? ¿En qué condiciones?",
  r"Con dos, no: para anularse necesitan la misma magnitud y sentidos opuestos. Con tres, "
  r"sí: si, puestos cola con punta, forman un triángulo cerrado (cada magnitud debe ser "
  r"menor o igual que la suma de las otras dos).")
M(9, f"{PREG} — 8a",
  r"¿La magnitud de un vector puede ser igual a alguna de sus componentes?",
  r"Sí, cuando el vector está sobre uno de los ejes: la otra componente es cero y "
  r"$|\vec V| = |V_x|$.")
M(10, f"{PREG} — 8b",
  r"¿La magnitud de un vector puede ser menor que alguna de sus componentes?",
  r"No: $|\vec V| = \sqrt{V_x^2 + V_y^2} \ge |V_x|$ y $\ge |V_y|$.")
M(11, f"{PREG} — 9",
  r"¿Puede una partícula acelerar si su rapidez es constante? ¿Puede acelerar si su "
  r"velocidad es constante?",
  r"Lo primero, sí: en un movimiento circular uniforme cambia la dirección de la velocidad. "
  r"Lo segundo, no: si la velocidad (vector) es constante, la aceleración es cero.")
M(12, f"{PREG} — 10",
  r"¿El odómetro de un automóvil mide una cantidad escalar o vectorial? ¿Y el velocímetro?",
  r"Los dos miden cantidades escalares: el odómetro, la distancia recorrida; el "
  r"velocímetro, la rapidez (la magnitud de la velocidad, sin dirección).")
M(13, f"{PREG} — 11", dificultad=2,
  enunciado=r"Un niño quiere determinar la rapidez que una cauchera le da a una piedra. "
            r"¿Cómo puede hacerlo usando solo una regla de un metro, una piedra y la "
            r"cauchera?",
  respuesta=r"Dispara la piedra horizontalmente desde una altura $h$ que mide con la regla "
            r"y mide el alcance horizontal $x$ (también con la regla). Como la caída dura "
            r"$t = \sqrt{2h/g}$, la rapidez es $v_0 = x/t = x\sqrt{g/2h}$.",
  notas="En la guía: «lanzadera (resortera)»; en Colombia se dice cauchera.")
M(14, f"{PREG} — 12",
  r"En arquería, ¿hay que apuntar la flecha directamente hacia el blanco? ¿Cómo depende el "
  r"ángulo de mira de la distancia al blanco?",
  r"No: la flecha cae mientras avanza, así que hay que apuntar un poco por encima del "
  r"blanco. Cuanto más lejos está el blanco, mayor debe ser el ángulo de elevación (hasta "
  r"$45^\circ$, que da el alcance máximo).")


@E(15, f"{PREG} — 13", tipo="conceptual",
   enunciado=r"Un proyectil se dispara con un ángulo de $30^\circ$ sobre la horizontal y una "
             r"rapidez de 30 m/s. ¿Cómo se compara la componente horizontal de su velocidad "
             r"1,0 s después del lanzamiento con la de 2,0 s después?",
   respuesta=r"Son iguales: sin resistencia del aire la componente horizontal no cambia, "
             r"$v_x = 30\cos 30^\circ \approx 26$ m/s en todo instante.")
def _():
    t = sp.symbols("t")
    x = 30 * sp.cos(sp.pi / 6) * t
    vx = sp.diff(x, t)
    assert vx.subs(t, 1) == vx.subs(t, 2) and abs(float(vx) - 26) < 0.1


M(16, f"{PREG} — 14", r"¿En qué punto de su trayectoria tiene un proyectil su menor rapidez?",
  r"En el punto más alto: allí la componente vertical de la velocidad es cero y solo queda "
  r"la horizontal (si se lanzó con un ángulo).")
M(17, f"{PREG} — 15",
  r"Se cuenta que en la Primera Guerra Mundial un piloto que volaba a 2 km de altura atrapó "
  r"con la mano una bala disparada hacia su avión. Usando que la resistencia del aire "
  r"frena mucho la bala, explica cómo pudo pasar.",
  r"La bala, frenada por el aire, llegó cerca del punto más alto de su trayectoria con muy "
  r"poca rapidez; si en ese momento se movía en el mismo sentido que el avión y con una "
  r"velocidad parecida, su velocidad relativa al piloto era casi cero y pudo tomarla.")
for _n, _lit, _preg, _resp in [
        (18, "a", "¿Cuál bala alcanza mayor elevación?",
         r"La A: su componente vertical inicial $v_0\operatorname{sen}\theta_A$ es mayor y "
         r"$h = \dfrac{(v_0\operatorname{sen}\theta)^2}{2g}$."),
        (19, "b", "¿Cuál permanece más tiempo en el aire?",
         r"La A: el tiempo de vuelo $t = \dfrac{2v_0\operatorname{sen}\theta}{g}$ crece con "
         r"el ángulo."),
        (20, "c", "¿Cuál viaja más lejos?",
         r"Depende: el alcance $R = \dfrac{v_0^2\operatorname{sen}2\theta}{g}$ es mayor para "
         r"el ángulo más cercano a $45^\circ$; si los ángulos son complementarios "
         r"($\theta_A + \theta_B = 90^\circ$), llegan igual de lejos.")]:
    M(_n, f"{PREG} — 16{_lit}",
      r"Dos balas de cañón, A y B, se disparan desde el suelo con la misma rapidez inicial, "
      r"pero con $\theta_A > \theta_B$. " + _preg, _resp)
for _n, _lit, _caso, _resp in [
        (21, "a", "el vagón se mueve con velocidad constante",
         "Vuelve a caer en su mano: la pelota conserva la velocidad horizontal del tren."),
        (22, "b", "el vagón acelera",
         "Cae detrás de su mano (hacia la parte trasera del vagón): el tren gana velocidad y "
         "la pelota no."),
        (23, "c", "el vagón desacelera",
         "Cae delante de su mano: el tren pierde velocidad y la pelota no."),
        (24, "d", "el vagón va por una curva",
         "Cae hacia el lado exterior de la curva: la pelota sigue en línea recta mientras el "
         "tren gira."),
        (25, "e", "el vagón se mueve con velocidad constante pero está abierto al aire",
         "Cae un poco detrás de su mano: el aire, que se mueve respecto al tren, la frena "
         "horizontalmente.")]:
    M(_n, f"{PREG} — 17{_lit}",
      rf"Una persona sentada en un vagón de tren lanza una pelota verticalmente hacia arriba "
      rf"según su propio marco de referencia. ¿Dónde caerá la pelota si {_caso}?", _resp)
M(26, f"{PREG} — 18",
  r"Si viajas en un tren que adelanta a otro que va en el mismo sentido por una vía "
  r"paralela, parece que el otro tren se mueve hacia atrás. ¿Por qué?",
  r"Porque ves su velocidad relativa a ti: $\vec v_{\text{otro}} - \vec v_{\text{tú}}$ "
  r"apunta hacia atrás cuando tu tren es más rápido.")
M(27, f"{PREG} — 19",
  r"Dos remeros que reman con la misma rapidez en aguas tranquilas empiezan a cruzar un río "
  r"al mismo tiempo. Uno rema perpendicular a la orilla y la corriente lo arrastra aguas "
  r"abajo; el otro rema en ángulo, aguas arriba, para llegar justo al frente. ¿Quién llega "
  r"primero a la otra orilla?",
  r"El que rema perpendicular: toda su velocidad respecto al agua sirve para cruzar. El otro "
  r"gasta parte de su velocidad en contrarrestar la corriente, así que su componente "
  r"perpendicular es menor y tarda más.", dificultad=2)
M(28, f"{PREG} — 20",
  r"Si estás quieto bajo la lluvia con un paraguas y las gotas caen verticalmente, no te "
  r"mojas. Si corres, la lluvia te moja las piernas aunque estén bajo el paraguas. ¿Por qué?",
  r"Respecto a ti, la velocidad de las gotas es $\vec v_{\text{gota}} - \vec v_{\text{tú}}$: "
  r"tiene una componente horizontal hacia ti, así que las gotas llegan inclinadas desde "
  r"adelante y alcanzan las piernas.")

# ---------- Problemas: suma de vectores ----------


@E(29, f"{PROB} — 1", tipo="contexto", dificultad=2,
   enunciado=r"Un automóvil recorre 225 km al oeste y luego 78 km al suroeste ($45^\circ$). "
             r"¿Cuál es su desplazamiento desde el punto de partida (magnitud y dirección)? "
             r"Dibuja un diagrama.",
   respuesta=r"Con $x$ al este y $y$ al norte: $D_x = -225 - 78\cos45^\circ \approx -280$ km, "
             r"$D_y = -78\operatorname{sen}45^\circ \approx -55$ km. $D \approx 286$ km, "
             r"$\approx 11^\circ$ al sur del oeste.")
def _():
    dx, dy = -225 - 78 * cos(radians(45)), -78 * sin(radians(45))
    cerca(hypot(dx, dy), 285.5, 0.002)
    cerca(degrees(atan2(-dy, -dx)), 11.1, 0.01)


@E(30, f"{PROB} — 2", tipo="contexto",
   enunciado=r"Un camión repartidor recorre 28 cuadras al norte, 16 al este y 26 al sur. "
             r"¿Cuál es su desplazamiento desde el origen? Las cuadras tienen igual longitud.",
   respuesta=r"$16$ cuadras al este y $2$ al norte: $\sqrt{16^2 + 2^2} \approx \num{16,1}$ "
             r"cuadras, $\approx \num{7,1}^\circ$ al norte del este.")
def _():
    dx, dy = 16, 28 - 26
    cerca(hypot(dx, dy), 16.1, 0.002)
    cerca(degrees(atan2(dy, dx)), 7.1, 0.005)


@E(31, f"{PROB} — 3",
   enunciado=r"Si $V_x = \num{7,80}$ unidades y $V_y = -\num{6,40}$ unidades, determina la "
             r"magnitud y la dirección de $\vec V$.",
   respuesta=r"$|\vec V| = \sqrt{\num{7,80}^2 + \num{6,40}^2} \approx \num{10,1}$ unidades, "
             r"a $\num{39,4}^\circ$ por debajo del eje $x$ positivo (cuarto cuadrante).")
def _():
    cerca(hypot(7.80, -6.40), 10.1, 0.002)
    cerca(degrees(atan2(-6.40, 7.80)), -39.4, 0.002)


@E(32, f"{PROB} — 4", tipo="calculo", dificultad=2,
   enunciado=r"Determina gráficamente la resultante de los tres desplazamientos: 24 m a "
             r"$36^\circ$ al norte del este; 18 m a $37^\circ$ al este del norte; 26 m a "
             r"$33^\circ$ al oeste del sur. Comprueba con componentes.",
   respuesta=r"Componentes: $(\num{19,4}; \num{14,1}) + (\num{10,8}; \num{14,4}) + "
             r"(-\num{14,2}; -\num{21,8}) \approx (\num{16,1}; \num{6,7})$ m. Resultante "
             r"$\approx \num{17,4}$ m a $\approx \num{22,5}^\circ$ al norte del este (el "
             r"dibujo a escala debe dar aproximadamente lo mismo).",
   notas="Los literales a, b y c de la guía son los tres vectores de un mismo ejercicio.")
def _():
    vs = [(24, 36), (18, 90 - 37), (26, 180 + 90 - 33)]    # ángulos desde el este
    rx = sum(r * cos(radians(a)) for r, a in vs)
    ry = sum(r * sin(radians(a)) for r, a in vs)
    cerca(hypot(rx, ry), 17.4, 0.003)
    cerca(degrees(atan2(ry, rx)), 22.5, 0.005)


# ---------- Problemas: cinemática vectorial ----------

_t = sp.symbols("t", real=True)
_R = sp.Matrix([sp.Rational("9.60") * _t, sp.Rational("8.85"), -_t**2])

_NOTA56 = ("En la guía falta la ecuación de la posición (era una imagen). Se reconstruyó con "
           "el problema original de Giancoli: r = (9,60t i + 8,85 j − 1,00t² k) m. Confirmar.")


@E(33, f"{PROB} — 5", dificultad=2, notas=_NOTA56,
   enunciado=r"La posición de una partícula en función del tiempo es "
             r"$\vec r = (\num{9,60}\,t\,\hat\imath + \num{8,85}\,\hat\jmath - "
             r"\num{1,00}\,t^2\,\hat k)$ m. Determina su velocidad y su aceleración en función "
             r"del tiempo.",
   respuesta=r"$\vec v = \dfrac{d\vec r}{dt} = (\num{9,60}\,\hat\imath - \num{2,00}\,t\,"
             r"\hat k)$ m/s; $\vec a = \dfrac{d\vec v}{dt} = -\num{2,00}\,\hat k\ "
             r"\mathrm{m/s^2}$ (constante).")
def _():
    v = _R.diff(_t)
    assert v == sp.Matrix([sp.Rational("9.60"), 0, -2 * _t])
    assert v.diff(_t) == sp.Matrix([0, 0, -2])


@E(34, f"{PROB} — 6", dificultad=2, notas=_NOTA56,
   enunciado=r"Para la partícula con $\vec r = (\num{9,60}\,t\,\hat\imath + \num{8,85}\,"
             r"\hat\jmath - \num{1,00}\,t^2\,\hat k)$ m, ¿cuál es su velocidad promedio entre "
             r"$t = \num{1,00}$ s y $t = \num{3,00}$ s? ¿Cuál es la magnitud de su velocidad "
             r"instantánea en $t = \num{2,00}$ s?",
   respuesta=r"$\bar{\vec v} = \dfrac{\vec r(3) - \vec r(1)}{2} = (\num{9,60}\,\hat\imath - "
             r"\num{4,00}\,\hat k)$ m/s; $|\vec v(2)| = \sqrt{\num{9,60}^2 + \num{4,00}^2} = "
             r"\num{10,4}$ m/s.")
def _():
    prom = (_R.subs(_t, 3) - _R.subs(_t, 1)) / 2
    assert prom == sp.Matrix([sp.Rational("9.60"), 0, -4])
    v2 = _R.diff(_t).subs(_t, 2)
    assert abs(float(v2.norm()) - 10.4) < 0.001


M(35, f"{PROB} — 7a", dificultad=2,
  enunciado=r"Un automóvil va a $\num{18,0}$ m/s hacia el sur en un momento y a "
            r"$\num{27,5}$ m/s hacia el este $\num{8,00}$ s después. ¿Puedes determinar la "
            r"magnitud y la dirección de su velocidad promedio en ese intervalo?",
  respuesta=r"No: la velocidad promedio es el desplazamiento dividido entre el tiempo, y no "
            r"se conoce el desplazamiento (depende del camino recorrido en esos 8 s).")


@E(36, f"{PROB} — 7b", dificultad=2,
   enunciado=r"Un automóvil va a $\num{18,0}$ m/s hacia el sur en un momento y a "
             r"$\num{27,5}$ m/s hacia el este $\num{8,00}$ s después. Determina la magnitud y "
             r"la dirección de su aceleración promedio en ese intervalo.",
   respuesta=r"$\Delta\vec v = (\num{27,5}\ \text{E}) - (\num{18,0}\ \text{S}) = "
             r"(\num{27,5}; \num{18,0})$ m/s; $\bar a = \dfrac{\sqrt{\num{27,5}^2 + "
             r"\num{18,0}^2}}{\num{8,00}} \approx \num{4,11}\ \mathrm{m/s^2}$, a "
             r"$\num{33,2}^\circ$ al norte del este.")
def _():
    ax, ay = (27.5 - 0) / 8.00, (0 - (-18.0)) / 8.00
    cerca(hypot(ax, ay), 4.11, 0.002)
    cerca(degrees(atan2(ay, ax)), 33.2, 0.002)


M(37, f"{PROB} — 7c",
  r"Un automóvil va a $\num{18,0}$ m/s hacia el sur en un momento y a $\num{27,5}$ m/s hacia "
  r"el este $\num{8,00}$ s después. ¿Cuál es su rapidez promedio en ese intervalo?",
  r"No se puede calcular: haría falta la distancia recorrida en los 8 s, que depende de "
  r"cómo se movió el carro.", dificultad=2)

# ---------- Problemas: movimiento de proyectiles (sin resistencia del aire) ----------


@E(38, f"{PROB} — 8", tipo="contexto",
   enunciado=r"Un tigre salta horizontalmente desde una roca de $\num{7,5}$ m de altura con una "
             r"rapidez de $\num{3,2}$ m/s. ¿A qué distancia de la base de la roca cae?",
   respuesta=r"$t = \sqrt{2h/g} = \sqrt{15/\num{9,8}} \approx \num{1,24}$ s; "
             r"$x = \num{3,2} \times \num{1,24} \approx \num{4,0}$ m.")
def _():
    t = sqrt(val(2 * 7.5 * m / G, s**2)) * s
    aprox(3.2 * m / s * t, 3.96, m, rel=0.003)


@E(39, f"{PROB} — 9", tipo="contexto",
   enunciado=r"Un clavadista corre a $\num{2,3}$ m/s, se lanza horizontalmente desde el borde "
             r"de un acantilado vertical y toca el agua $\num{3,0}$ s después. ¿Qué altura "
             r"tiene el acantilado y a qué distancia de su base cae el clavadista?",
   respuesta=r"$h = \frac{1}{2}g t^2 = \num{4,9}(9) \approx 44$ m; $x = \num{2,3}(\num{3,0}) "
             r"= \num{6,9}$ m.")
def _():
    t = 3.0 * s
    aprox(G * t**2 / 2, 44.1, m, rel=0.001)
    aprox(2.3 * m / s * t, 6.9, m, rel=1e-9)


@E(40, f"{PROB} — 10",
   enunciado=r"Determina qué tan alto puede saltar una persona en la Luna, comparado con la "
             r"Tierra, si la rapidez y el ángulo de despegue son los mismos. La gravedad en la "
             r"Luna es un sexto de la terrestre.",
   respuesta=r"Como $h = \dfrac{(v_0\operatorname{sen}\theta)^2}{2g}$, al dividir $g$ entre 6 "
             r"la altura se multiplica por 6: salta 6 veces más alto.")
def _():
    v, th, gg = sp.symbols("v theta g", positive=True)
    h = (v * sp.sin(th))**2 / (2 * gg)
    assert sp.simplify(h.subs(gg, gg / 6) / h) == 6


@E(41, f"{PROB} — 11", tipo="contexto", dificultad=2,
   enunciado=r"Una manguera contra incendios, cerca del suelo, lanza agua a $\num{6,5}$ m/s. "
             r"¿Con qué ángulo o ángulos debe apuntarse la boquilla para que el agua llegue a "
             r"$\num{2,5}$ m de distancia? ¿Por qué hay dos ángulos? Dibuja las dos "
             r"trayectorias.",
   respuesta=r"$\operatorname{sen}2\theta = \dfrac{Rg}{v_0^2} = \dfrac{\num{2,5}(\num{9,8})}"
             r"{\num{6,5}^2} \approx \num{0,580}$, así que $\theta \approx \num{17,7}^\circ$ o "
             r"$\theta \approx \num{72,3}^\circ$. Hay dos porque "
             r"$\operatorname{sen}2\theta = \operatorname{sen}(180^\circ - 2\theta)$: ángulos "
             r"complementarios dan el mismo alcance (uno con trayectoria baja y otro alta).")
def _():
    k = 2.5 * g / 6.5**2
    t1 = degrees(asin(k)) / 2
    cerca(t1, 17.7, 0.003)
    cerca(90 - t1, 72.3, 0.001)
    for th in (t1, 90 - t1):
        cerca(6.5**2 * sin(radians(2 * th)) / g, 2.5, 1e-9)


@E(42, f"{PROB} — 12",
   enunciado=r"Una pelota se lanza horizontalmente desde el techo de un edificio de "
             r"$\num{9,0}$ m de altura y cae a $\num{9,5}$ m de la base. ¿Cuál fue su rapidez "
             r"inicial?",
   respuesta=r"$t = \sqrt{2(9)/\num{9,8}} \approx \num{1,36}$ s; $v_0 = \num{9,5}/\num{1,36} "
             r"\approx \num{7,0}$ m/s.",
   notas="En la guía la altura aparece como «9.0 m»; se usa coma decimal.")
def _():
    t = sqrt(val(2 * 9.0 * m / G, s**2)) * s
    aprox(9.5 * m / t, 7.01, m / s, rel=0.003)


@E(43, f"{PROB} — 13",
   enunciado=r"Un balón se patea desde el suelo y sale a $\num{18,0}$ m/s con un ángulo de "
             r"$\num{38,0}^\circ$ sobre la horizontal. ¿Cuánto tarda en volver al suelo?",
   respuesta=r"$t = \dfrac{2v_0\operatorname{sen}\theta}{g} = "
             r"\dfrac{2(18)\operatorname{sen}38^\circ}{\num{9,8}} \approx \num{2,26}$ s.")
def _():
    aprox(2 * 18.0 * sin(radians(38.0)) * m / s / G, 2.26, s, rel=0.003)


@E(44, f"{PROB} — 14", tipo="contexto",
   enunciado=r"El piloto de un avión que vuela horizontalmente a 170 km/h quiere lanzar "
             r"suministros a víctimas de una inundación que están 150 m más abajo. ¿Cuántos "
             r"segundos antes de estar directamente sobre ellas debe soltar los suministros?",
   respuesta=r"Lo que tardan en caer 150 m: $t = \sqrt{2(150)/\num{9,8}} \approx \num{5,5}$ s. "
             r"(Mientras caen avanzan $\approx 261$ m horizontalmente, igual que el avión).")
def _():
    t = sqrt(val(2 * 150 * m / G, s**2)) * s
    aprox(t, 5.53, s, rel=0.003)
    aprox(170 * km / (3600 * s) * t, 261, m, rel=0.005)


_VX, _VY = 46.6 * cos(radians(42.2)), 46.6 * sin(radians(42.2))
for _n, _lit, _preg, _resp in [
        (45, "a", "La altura máxima que alcanza.",
         r"$h = \dfrac{(v_0\operatorname{sen}\theta)^2}{2g} = "
         r"\dfrac{\num{31,3}^2}{\num{19,6}} \approx \num{50,0}$ m."),
        (46, "b", "El tiempo total de vuelo.",
         r"$t = \dfrac{2v_0\operatorname{sen}\theta}{g} \approx \num{6,39}$ s."),
        (47, "c", "La distancia horizontal total que recorre (su alcance).",
         r"$R = v_0\cos\theta\ t = \num{34,5} \times \num{6,39} \approx 221$ m."),
        (48, "d", r"Su velocidad (magnitud y dirección) $\num{1,50}$ s después del disparo.",
         r"$v_x = \num{34,5}$ m/s, $v_y = \num{31,3} - \num{9,8}(\num{1,50}) \approx "
         r"\num{16,6}$ m/s: $v \approx \num{38,3}$ m/s, a $\num{25,7}^\circ$ sobre la "
         r"horizontal.")]:
    @E(_n, f"{PROB} — 15{_lit}", dificultad=2,
       enunciado=r"Se dispara un proyectil con una rapidez inicial de $\num{46,6}$ m/s a "
                 r"$\num{42,2}^\circ$ sobre la horizontal, en un terreno largo y plano. "
                 r"Determina: " + _preg,
       respuesta=_resp)
    def _(lit=_lit):
        vx, vy = _VX * m / s, _VY * m / s
        t = 2 * vy / G
        if lit == "a":
            aprox(vy**2 / (2 * G), 50.0, m, rel=0.002)
        if lit == "b":
            aprox(t, 6.39, s, rel=0.002)
        if lit == "c":
            aprox(vx * t, 221, m, rel=0.003)
        if lit == "d":
            vy1 = _VY - g * 1.50
            cerca(hypot(_VX, vy1), 38.3, 0.002)
            cerca(degrees(atan2(vy1, _VX)), 25.7, 0.003)


@E(49, f"{PROB} — 16a", tipo="contexto", dificultad=2,
   enunciado=r"Un atleta de salto largo despega con un ángulo de $\num{27,0}^\circ$ y cae a "
             r"$\num{7,80}$ m. ¿Cuál fue su rapidez de despegue?",
   respuesta=r"$v_0 = \sqrt{\dfrac{Rg}{\operatorname{sen}2\theta}} = "
             r"\sqrt{\dfrac{\num{7,80}(\num{9,8})}{\operatorname{sen}54^\circ}} \approx "
             r"\num{9,72}$ m/s.")
def _():
    v0 = sqrt(val(7.80 * m * G, m**2 / s**2) / sin(radians(54.0)))
    cerca(v0, 9.72, 0.002)


@E(50, f"{PROB} — 16b", tipo="contexto", dificultad=2,
   enunciado=r"Si la rapidez de despegue del atleta anterior ($\num{7,80}$ m a "
             r"$\num{27,0}^\circ$) aumentara solo un $\num{5,0}\,\%$, ¿cuánto más largo sería "
             r"el salto?",
   respuesta=r"El alcance es proporcional a $v_0^2$: $R' = \num{7,80}(\num{1,05})^2 \approx "
             r"\num{8,60}$ m, unos $\num{0,80}$ m más.")
def _():
    v0 = sqrt(7.80 * g / sin(radians(54.0)))
    r2 = (1.05 * v0)**2 * sin(radians(54.0)) / g
    cerca(r2, 8.60, 0.002)
    cerca(r2 - 7.80, 0.80, 0.02)
