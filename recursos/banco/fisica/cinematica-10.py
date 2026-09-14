"""Banco de ejercicios — Física 10° — Cinemática en una dimensión (velocidad, aceleración,
movimiento con aceleración constante, caída libre).
Fuente: Guía de apoyo de Física 10° «Cinemática y dinámica», Capítulo 2 (Descripción del
movimiento. Cinemática en una dimensión); se lee en
recursos/fisica/Guías pedagógicas Física/markdown/10 - Guia_de_apoyo_cinematica_y_dinamica_grado_10_fisica.md
Secciones: «Practiquemos» (dentro del texto), Preguntas, Problemas.
DBA: naturales grado 10 · DBA 1 (en presencia de fuerzas resultantes no nulas se producen
cambios de velocidad): la cinemática es la base para describir esos cambios.
g = 9,8 m/s² (la guía usa 9,80 m/s²).
No se incluyeron: Problemas 8a, 8b y 8c (velocidad instantánea del conejo en t = 10 s y
t = 30 s, y velocidad promedio entre 0 y 5 s): exigen trazar tangentes o leer valores de la
Imagen 18 que la descripción no da.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/fisica/cinematica-10.py
"""
from math import sqrt

from sympy.physics.units import (centimeter, convert_to, hour, kilogram, kilometer, meter,
                                 micrometer, mile, millimeter, minute, second)

from ejercicios import ejercicio, ejercicio_manual

PRE = "cinematica-10"
G1 = "Guía de apoyo Física 10° (cinemática y dinámica), Cap. 2 Cinemática en una dimensión"
PRAC = f"{G1}, Practiquemos"
PREG = f"{G1}, Preguntas"
PROB = f"{G1}, Problemas"
COMUN = dict(tema="cinemática en una dimensión", grados=[10], dba=["naturales-10-1"])

m, s, km, h = meter, second, kilometer, hour
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
    """Raíz cuadrada de una cantidad cuyo cuadrado se da en unidad**2."""
    return sqrt(val(q, unidad**2)) * unidad


# ---------- Practiquemos ----------

@E(1, f"{PRAC} (marcos de referencia y desplazamiento) — 1",
   enunciado=r"Una hormiga parte de $x = 20$ cm sobre una hoja cuadriculada y camina a lo "
             r"largo del eje $x$ hasta $x = -20$ cm. Luego se devuelve y camina hasta "
             r"$x = -10$ cm. ¿Cuál es el desplazamiento de la hormiga y cuál la distancia "
             r"total recorrida?",
   respuesta=r"Desplazamiento: $\Delta x = -10 - 20 = -30$ cm (30 cm en el sentido "
             r"negativo). Distancia recorrida: $40 + 10 = 50$ cm.")
def _():
    x = [20, -20, -10]
    assert x[-1] - x[0] == -30
    assert sum(abs(b - a) for a, b in zip(x, x[1:])) == 50


@E(2, f"{PRAC} (velocidad promedio) — 1", tipo="seleccion",
   enunciado=r"Un automóvil viaja a una rapidez constante de 50 km/h durante 100 km. Luego "
             r"acelera a 100 km/h y recorre otros 100 km. ¿Cuál es la rapidez promedio de su "
             r"viaje de 200 km?" + op("67 km/h", "75 km/h", "81 km/h", "50 km/h"),
   respuesta=r"a) 67 km/h: tarda $2\ \text{h} + 1\ \text{h} = 3$ h, y "
             r"$\bar v = 200\ \text{km}/3\ \text{h} \approx 67$ km/h (no es el promedio de "
             r"las rapideces, porque va más tiempo a 50 km/h).")
def _():
    t = 100 * km / (50 * km / h) + 100 * km / (100 * km / h)
    v = val(200 * km / t, km / h)
    assert [abs(v - o) < 1 for o in (67, 75, 81, 50)] == [True, False, False, False]


M(3, f"{PRAC} (velocidad instantánea) — 1", tipo="seleccion",
  enunciado=r"¿Cuál es tu rapidez en el instante en que te das la vuelta para moverte en "
            r"sentido contrario?" + op("Depende de qué tan rápido te des la vuelta.",
                                       "Siempre es cero.", "Siempre es negativa.",
                                       "Ninguna de las anteriores."),
  respuesta=r"b) Siempre es cero: para cambiar el sentido del movimiento en línea recta, la "
            r"velocidad pasa de positiva a negativa y en ese instante vale cero. (La rapidez "
            r"nunca es negativa).")
for _n, _lit, _caso, _resp in [
        (4, "a", r"se mueve en el sentido $x$ positivo con rapidez creciente",
         r"Positivo: la velocidad es positiva y aumenta, así que $a$ apunta en el sentido "
         r"$+x$."),
        (5, "b", r"se mueve en el sentido $x$ positivo con rapidez decreciente",
         r"Negativo: la velocidad es positiva y disminuye; $a$ apunta en sentido opuesto a "
         r"$v$."),
        (6, "c", r"se mueve en el sentido $x$ negativo con rapidez creciente",
         r"Negativo: la velocidad es negativa y cada vez más negativa; $a$ apunta en el "
         r"mismo sentido que $v$, hacia $-x$."),
        (7, "d", r"se mueve en el sentido $x$ negativo con rapidez decreciente",
         r"Positivo: la velocidad es negativa y se acerca a cero; $a$ apunta hacia $+x$.")]:
    M(_n, f"{PRAC} (aceleración) — {_lit}",
      rf"Un automóvil se mueve a lo largo del eje $x$. ¿Cuál es el signo de su aceleración si "
      rf"{_caso}?", _resp)


@E(8, f"{PRAC} (aceleración constante) — 1", tipo="seleccion",
   enunciado=r"Un automóvil parte del reposo y acelera a $10\ \mathrm{m/s^2}$ constantes "
             r"durante una carrera de un cuarto de milla (402 m). ¿Qué tan rápido viaja "
             r"cuando cruza la línea de meta?" + op("8090 m/s", "90 m/s", "81 m/s", "809 m/s"),
   respuesta=r"b) 90 m/s: $v = \sqrt{2ax} = \sqrt{2(10)(402)} \approx \num{89,7}$ m/s.")
def _():
    v = val(raiz(2 * 10 * m / s**2 * 402 * m, m / s), m / s)
    assert [abs(v - o) < 1 for o in (8090, 90, 81, 809)] == [False, True, False, False]


# ---------- Preguntas ----------

M(9, f"{PREG} — 1", r"¿El velocímetro de un automóvil mide rapidez, velocidad o ambas?",
  r"Mide la rapidez (la magnitud de la velocidad instantánea); no indica la dirección ni "
  r"el sentido del movimiento.")
M(10, f"{PREG} — 2",
  r"¿Un objeto puede tener rapidez variable si su velocidad es constante? ¿Puede tener "
  r"velocidad variable si su rapidez es constante? Da ejemplos.",
  r"Lo primero, no: si la velocidad es constante, su magnitud (la rapidez) también. Lo "
  r"segundo, sí: un carro que da la vuelta a una glorieta a 30 km/h constantes cambia la "
  r"dirección de su velocidad.")
M(11, f"{PREG} — 3",
  r"Cuando un objeto se mueve con velocidad constante, ¿su velocidad promedio en cualquier "
  r"intervalo difiere de su velocidad instantánea en cualquier instante?",
  r"No: con velocidad constante, la velocidad promedio en cualquier intervalo es igual a la "
  r"velocidad instantánea en cualquier instante.")
M(12, f"{PREG} — 4",
  r"Si un objeto tiene mayor rapidez que otro, ¿tiene necesariamente mayor aceleración? "
  r"Explica con ejemplos.",
  r"No. Un avión que vuela a 900 km/h constantes tiene aceleración cero, mientras que un "
  r"carro que arranca en un semáforo tiene poca rapidez pero aceleración distinta de cero. "
  r"La aceleración depende de cómo cambia la velocidad, no de su valor.")
M(13, f"{PREG} — 5",
  r"Compara la aceleración de una motocicleta que pasa de 80 km/h a 90 km/h con la de una "
  r"bicicleta que pasa del reposo a 10 km/h en el mismo tiempo.",
  r"Son iguales: las dos cambian su velocidad en 10 km/h en el mismo intervalo, y "
  r"$a = \Delta v/\Delta t$.")
M(14, f"{PREG} — 6",
  r"¿Puede un objeto tener velocidad hacia el norte y aceleración hacia el sur? Explica.",
  r"Sí: un carro que avanza hacia el norte y frena. La velocidad apunta al norte y la "
  r"aceleración al sur, porque la rapidez disminuye.")
M(15, f"{PREG} — 7",
  r"¿La velocidad de un objeto puede ser negativa cuando su aceleración es positiva? ¿Y "
  r"viceversa?",
  r"Sí en ambos casos: un objeto que se mueve hacia $-x$ y frena tiene $v < 0$ y $a > 0$; uno "
  r"que se mueve hacia $+x$ y frena tiene $v > 0$ y $a < 0$.")
M(16, f"{PREG} — 8", r"Da un ejemplo donde la velocidad y la aceleración sean negativas.",
  r"Una piedra que cae, tomando el eje $y$ positivo hacia arriba: se mueve hacia abajo "
  r"($v < 0$) cada vez más rápido, con $a = -g$.")
M(17, f"{PREG} — 9",
  r"Dos automóviles entran lado a lado a un túnel. El automóvil A va a 60 km/h con una "
  r"aceleración de 40 km/h/min; el B va a 40 km/h con una aceleración de 60 km/h/min. ¿Cuál "
  r"irá adelante cuando salgan del túnel? Explica tu razonamiento.",
  r"Depende de la longitud del túnel. Al principio A va más rápido y se adelanta; B lo "
  r"iguala en velocidad al cabo de 1 min y lo alcanza a los 2 min, cuando ambos han "
  r"recorrido unos $\num{3,3}$ km ($x_A - x_B = 20t - 600t^2$ con $t$ en horas). En un túnel "
  r"de menos de unos $\num{3,3}$ km sale adelante A; en uno más largo, B.", dificultad=2)
M(18, f"{PREG} — 10",
  r"¿Puede un objeto aumentar su rapidez si su aceleración disminuye? Da un ejemplo o "
  r"explica.",
  r"Sí, mientras la aceleración siga en el sentido de la velocidad: un carro que se acerca "
  r"a su velocidad de crucero sigue ganando rapidez aunque acelere cada vez menos; una gota "
  r"de lluvia que se acerca a su velocidad terminal también.")
M(19, f"{PREG} — 11",
  r"Un bateador golpea la pelota verticalmente hacia arriba, con una rapidez de 120 km/h. "
  r"Sin resistencia del aire, ¿con qué rapidez llega la pelota al guante del receptor?",
  r"Con 120 km/h (si la atrapa a la misma altura): la subida y la bajada son simétricas.")
M(20, f"{PREG} — 12a",
  r"Cuando un objeto en caída libre aumenta su velocidad, ¿qué pasa con su aceleración si "
  r"se ignora la resistencia del aire?",
  r"Permanece igual: $a = g \approx \num{9,8}\ \mathrm{m/s^2}$ durante toda la caída.")
M(21, f"{PREG} — 12b",
  r"Cuando un objeto que cae aumenta su velocidad, ¿qué pasa con su aceleración si se "
  r"considera la resistencia del aire?",
  r"Disminuye: la resistencia del aire crece con la rapidez y se opone al peso, hasta que la "
  r"aceleración se anula y el objeto cae con velocidad constante (velocidad terminal).")


@E(22, f"{PREG} — 13", tipo="argumentacion",
   enunciado=r"Viajas del punto A al B con rapidez constante de 70 km/h y luego la misma "
             r"distancia de B a C con rapidez constante de 90 km/h. ¿Tu rapidez promedio para "
             r"el viaje completo es de 80 km/h? Explica.",
   respuesta=r"No: vas más tiempo a 70 km/h. Con una distancia $d$ en cada tramo, "
             r"$\bar v = \dfrac{2d}{d/70 + d/90} = \num{78,75}$ km/h.")
def _():
    d = 1 * km
    v = val(2 * d / (d / (70 * km / h) + d / (90 * km / h)), km / h)
    assert abs(v - 78.75) < 1e-9 and v != 80


M(23, f"{PREG} — 14",
  r"¿Puede un objeto tener velocidad cero y aceleración distinta de cero al mismo tiempo? "
  r"Da ejemplos.",
  r"Sí: una pelota lanzada hacia arriba en su punto más alto ($v = 0$, $a = g$), o un carro "
  r"en el instante en que arranca.")
M(24, f"{PREG} — 15",
  r"¿Puede un objeto tener aceleración cero y velocidad distinta de cero al mismo tiempo? "
  r"Da ejemplos.",
  r"Sí: cualquier movimiento rectilíneo uniforme, como un carro a 60 km/h constantes en una "
  r"recta, o un paracaidista que cae con su velocidad terminal.")
M(25, f"{PREG} — 16",
  r"¿Cuál de estos movimientos no tiene aceleración constante: una roca que cae desde un "
  r"acantilado, un elevador que sube del segundo al quinto piso con paradas en el trayecto, "
  r"un plato que descansa sobre una mesa?",
  r"El elevador: acelera, va a velocidad constante, frena y se detiene varias veces. La "
  r"roca tiene $a = g$ constante (sin aire) y el plato $a = 0$ constante.")
M(26, f"{PREG} — 17",
  r"Una cuerda vertical de $\num{3,0}$ m con 10 tornillos amarrados a intervalos iguales se "
  r"suelta desde el techo y cae sobre una placa metálica. ¿Por qué los tintineos no ocurren "
  r"a intervalos de tiempo iguales? ¿El tiempo entre tintineos aumenta o disminuye cerca "
  r"del final? ¿Cómo amarrarías los tornillos para que los tintineos sean regulares?",
  r"Los tornillos de arriba caen más distancia y llegan más rápido al piso, así que cada "
  r"tramo igual se recorre en menos tiempo: el tiempo entre tintineos disminuye hacia el "
  r"final. Como $y = \frac{1}{2}gt^2$, para intervalos de tiempo iguales las distancias al "
  r"piso deben crecer como $1, 4, 9, 16, \dots$ (proporcionales a $n^2$).", dificultad=2)
M(27, f"{PREG} — 18",
  r"Describe con palabras el movimiento de la gráfica $x$ contra $t$ que pasa por los puntos "
  r"$(0, 0)$, $(10; \num{2,5})$, $(20, 6)$, $(25, 8)$, $(30, 11)$, $(35, 19)$, $(37, 20)$, "
  r"$(40, 19)$, $(45, 15)$ y $(50, 10)$ ($t$ en s, $x$ en m).",
  r"Parte del origen y avanza en sentido positivo cada vez más rápido (la pendiente crece) "
  r"hasta cerca de $t = 35$ s; luego frena, se detiene un instante hacia $t \approx 37$ s en "
  r"$x \approx 20$ m y se devuelve en sentido negativo, cada vez más rápido al principio y "
  r"luego a velocidad casi constante ($\approx -1$ m/s), hasta $x = 10$ m en $t = 50$ s.",
  dificultad=2)
M(28, f"{PREG} — 19",
  r"Describe con palabras el movimiento de la gráfica $v$ contra $t$ que pasa por los puntos "
  r"$(0, 15)$, $(10, 20)$, $(20, 25)$, $(30, 30)$, $(40, 35)$, $(50, 38)$, $(60, 32)$, "
  r"$(70, 20)$, $(80, 5)$, $(90, 0)$, $(100, 0)$, $(110, 3)$ y $(120, 10)$ ($t$ en s, $v$ en "
  r"m/s).",
  r"Empieza a 15 m/s y acelera uniformemente ($a = \num{0,5}\ \mathrm{m/s^2}$) hasta "
  r"$t = 40$ s; sigue acelerando menos hasta la rapidez máxima ($\approx 38$ m/s en "
  r"$t \approx 50$ s); luego frena hasta detenerse en $t = 90$ s, permanece en reposo hasta "
  r"$t = 100$ s y vuelve a arrancar en el mismo sentido. Siempre se mueve en sentido "
  r"positivo ($v \ge 0$).", dificultad=2)


# ---------- Problemas: rapidez y velocidad ----------

@E(29, f"{PROB} — 1", tipo="contexto",
   enunciado=r"Si vas manejando a 110 km/h por una carretera recta y te distraes durante "
             r"$\num{2,0}$ s, ¿qué distancia recorres sin prestar atención?",
   respuesta=r"$x = vt = \num{30,6}\ \mathrm{m/s} \times \num{2,0}\ \text{s} \approx 61$ m.")
def _():
    aprox(110 * km / h * 2 * s, 61, m, rel=0.005)


@E(30, f"{PROB} — 2",
   enunciado=r"¿Cuál debe ser la rapidez promedio de tu automóvil para recorrer 235 km en "
             r"$\num{3,25}$ h?",
   respuesta=r"$\bar v = 235/\num{3,25} \approx \num{72,3}$ km/h ($\approx \num{20,1}$ m/s).")
def _():
    aprox(235 * km / (3.25 * h), 72.3, km / h, rel=0.001)


@E(31, f"{PROB} — 3",
   enunciado=r"En $t_1 = -\num{2,0}$ s una partícula está en $x_1 = \num{4,3}$ cm y en "
             r"$t_2 = \num{4,5}$ s está en $x_2 = \num{8,5}$ cm. ¿Cuál es su velocidad "
             r"promedio? ¿Puedes calcular su rapidez promedio con estos datos?",
   respuesta=r"$\bar v = \dfrac{\num{8,5} - \num{4,3}}{\num{4,5} - (-\num{2,0})} = "
             r"\dfrac{\num{4,2}\ \text{cm}}{\num{6,5}\ \text{s}} \approx \num{0,65}$ cm/s. La "
             r"rapidez promedio no se puede calcular: no se conoce la distancia total "
             r"recorrida (la partícula pudo ir y volver).",
   notas="En la guía x1, x2 llevan punto decimal («4.3», «8.5»); se usa coma.")
def _():
    aprox((8.5 - 4.3) * centimeter / ((4.5 + 2.0) * s), 0.646, centimeter / s, rel=0.002)


@E(32, f"{PROB} — 4",
   enunciado=r"Una pelota rueda desde $x_1 = \num{3,4}$ cm hasta $x_2 = \num{4,2}$ cm entre "
             r"$t_1 = \num{3,0}$ s y $t_2 = \num{5,1}$ s. ¿Cuál es su velocidad promedio?",
   respuesta=r"$\bar v = \dfrac{\num{0,8}\ \text{cm}}{\num{2,1}\ \text{s}} \approx \num{0,38}$ "
             r"cm/s.")
def _():
    aprox((4.2 - 3.4) * centimeter / ((5.1 - 3.0) * s), 0.38, centimeter / s, rel=0.005)


@E(33, f"{PROB} — 5", tipo="contexto",
   enunciado=r"Según una regla práctica, cada cinco segundos entre un relámpago y su trueno "
             r"indican una milla de distancia. Suponiendo que la luz llega instantáneamente, "
             r"estima con esta regla la rapidez del sonido en m/s. ¿Cuál sería la regla en "
             r"kilómetros?",
   respuesta=r"$v \approx \dfrac{1609\ \text{m}}{5\ \text{s}} \approx 320$ m/s (el valor real "
             r"es unos 340 m/s). En kilómetros: cada 3 s equivalen a 1 km "
             r"($1000/320 \approx 3$ s).")
def _():
    v = 1 * mile / (5 * s)
    aprox(v, 322, m / s, rel=0.005)
    assert round(val(1 * km / v, s)) == 3


@E(34, f"{PROB} — 6a", tipo="contexto", dificultad=2,
   enunciado=r"Vas de la escuela a la casa a 95 km/h de manera uniforme a lo largo de 130 km. "
             r"Empieza a llover, bajas la velocidad a 65 km/h y llegas a casa después de "
             r"conducir 3 horas y 20 minutos en total. ¿Qué tan lejos está tu casa de la "
             r"escuela?",
   respuesta=r"Primer tramo: $130/95 \approx \num{1,37}$ h. Quedan "
             r"$\num{3,33} - \num{1,37} = \num{1,97}$ h a 65 km/h: $\approx 128$ km. Total "
             r"$\approx 258$ km.")
def _():
    t1 = 130 * km / (95 * km / h)
    assert convert_to(20 * minute, h) == h / 3
    d2 = 65 * km / h * ((3 + 20 / 60) * h - t1)
    aprox(130 * km + d2, 258, km, rel=0.003)


@E(35, f"{PROB} — 6b", tipo="contexto", dificultad=2,
   enunciado=r"En el viaje anterior (130 km a 95 km/h y el resto a 65 km/h, con 3 h 20 min de "
             r"viaje en total), ¿cuál fue la rapidez promedio?",
   respuesta=r"$\bar v = \dfrac{258\ \text{km}}{\num{3,33}\ \text{h}} \approx 77$ km/h.")
def _():
    t = (3 + 20 / 60) * h                 # 3 h 20 min
    d = 130 * km + 65 * km / h * (t - 130 * km / (95 * km / h))
    aprox(d / t, 77.3, km / h, rel=0.003)


@E(36, f"{PROB} — 7a", tipo="contexto",
   enunciado=r"Un caballo se aleja de su entrenador galopando en línea recta 116 m en "
             r"$\num{14,0}$ s. Luego se devuelve y recorre la mitad de esa distancia en "
             r"$\num{4,8}$ s. Calcula su rapidez promedio.",
   respuesta=r"$\dfrac{116 + 58}{\num{14,0} + \num{4,8}} = \dfrac{174\ \text{m}}{\num{18,8}\ "
             r"\text{s}} \approx \num{9,26}$ m/s.")
def _():
    aprox((116 + 58) * m / ((14.0 + 4.8) * s), 9.26, m / s, rel=0.001)


@E(37, f"{PROB} — 7b", tipo="contexto",
   enunciado=r"Para el caballo anterior (116 m alejándose en $\num{14,0}$ s y 58 m de regreso "
             r"en $\num{4,8}$ s), calcula la velocidad promedio de todo el viaje, tomando "
             r"«alejándose del entrenador» como sentido positivo.",
   respuesta=r"$\bar v = \dfrac{116 - 58}{\num{18,8}} = \dfrac{58\ \text{m}}{\num{18,8}\ "
             r"\text{s}} \approx +\num{3,1}$ m/s.")
def _():
    aprox((116 - 58) * m / ((14.0 + 4.8) * s), 3.09, m / s, rel=0.002)


for _n, _lit, _t1, _x1, _t2, _x2, _v in [(38, "d", 25, 8, 30, 11, 0.6),
                                         (39, "e", 40, 19, 50, 10, -0.9)]:
    @E(_n, f"{PROB} — 8{_lit}", dificultad=2,
       enunciado=rf"La posición de un conejo en un túnel recto se da en la gráfica $x$ contra "
                 rf"$t$ de la Imagen 18, que pasa por $({_t1}, {_x1})$ y $({_t2}, {_x2})$ "
                 rf"($t$ en s, $x$ en m). ¿Cuál es su velocidad promedio entre $t = {_t1}$ s "
                 rf"y $t = {_t2}$ s?",
       respuesta=rf"$\bar v = \dfrac{{{_x2} - {_x1}}}{{{_t2} - {_t1}}} = "
                 rf"\num{{{str(_v).replace('.', ',')}}}$ m/s (valores leídos de la gráfica).",
       notas="Los puntos se tomaron de la descripción de la Imagen 18 (valores aproximados).")
    def _(t1=_t1, x1=_x1, t2=_t2, x2=_x2, v=_v):
        aprox((x2 - x1) * m / ((t2 - t1) * s), v, m / s, rel=1e-9)


@E(40, f"{PROB} — 9a", tipo="contexto", dificultad=2,
   enunciado=r"En un CD de audio, los bits se codifican a lo largo de una espiral y cada bit "
             r"ocupa aproximadamente $\num{0,28}\ \mu$m. El lector láser recorre la espiral a "
             r"una rapidez constante de aproximadamente $\num{1,2}$ m/s. Determina el número "
             r"$N$ de bits que el reproductor lee cada segundo.",
   respuesta=r"$N = \dfrac{\num{1,2}\ \mathrm{m/s}}{\num{0,28e-6}\ \text{m/bit}} \approx "
             r"\num{4,3e6}$ bits/s.",
   notas="La guía dice «0,28 mm» por bit: con ese dato N ≈ 4300 bits/s, menor que los "
         "1,4×10⁶ bits/s que el literal b dice que se necesitan, lo cual es imposible. El "
         "valor correcto (Giancoli) es 0,28 µm.")
def _():
    aprox(1.2 * m / s / (0.28 * micrometer), 4.29e6, 1 / s, rel=0.002)
    assert val(1.2 * m / s / (0.28 * millimeter), 1 / s) < 1.4e6   # el dato de la guía no sirve


@E(41, f"{PROB} — 9b", tipo="contexto", dificultad=2,
   enunciado=r"La información de audio se envía a cada uno de los dos altavoces "
             r"$\num{44100}$ veces por segundo, y cada muestra requiere 16 bits, así que "
             r"$N_0 = 2 \times \num{44100} \times 16 \approx \num{1,4e6}$ bits/s. El exceso de "
             r"bits $N - N_0$ (con $N \approx \num{4,3e6}$ bits/s, del literal a) se usa para "
             r"codificar y corregir errores. ¿Qué porcentaje de los bits del CD se dedica a "
             r"eso?",
   respuesta=r"$\dfrac{N - N_0}{N} = \dfrac{\num{4,29e6} - \num{1,41e6}}{\num{4,29e6}} "
             r"\approx 67\,\%$.",
   notas="En la guía aparece «44,100 veces» con coma de miles; se escribe 44 100.")
def _():
    n = val(1.2 * m / s / (0.28 * micrometer), 1 / s)
    n0 = 2 * 44100 * 16
    assert abs((n - n0) / n * 100 - 67) < 0.5


@E(42, f"{PROB} — 10", tipo="contexto",
   enunciado=r"Un automóvil que viaja a 95 km/h va 110 m detrás de un camión que viaja a "
             r"75 km/h. ¿Cuánto tiempo le tomará al automóvil alcanzar al camión?",
   respuesta=r"Velocidad relativa: $20\ \text{km/h} = \num{5,56}$ m/s; "
             r"$t = 110/\num{5,56} \approx \num{19,8}$ s.")
def _():
    aprox(110 * m / (20 * km / h), 19.8, s, rel=0.002)


@E(43, f"{PROB} — 11", tipo="contexto", dificultad=2,
   enunciado=r"Una bola de boliche que rueda con rapidez constante golpea los pinos al final "
             r"de una pista de $\num{16,5}$ m. El jugador oye el golpe $\num{2,50}$ s después "
             r"de lanzarla. ¿Cuál es la rapidez de la bola, si la del sonido es 340 m/s?",
   respuesta=r"El sonido tarda $\num{16,5}/340 \approx \num{0,0485}$ s, así que la bola tarda "
             r"$\num{2,45}$ s: $v = \num{16,5}/\num{2,45} \approx \num{6,73}$ m/s.")
def _():
    t_bola = 2.50 * s - 16.5 * m / (340 * m / s)
    aprox(16.5 * m / t_bola, 6.73, m / s, rel=0.002)


# ---------- Problemas: aceleración ----------

@E(44, f"{PROB} — 12",
   enunciado=r"Un auto deportivo acelera desde el reposo hasta 95 km/h en $\num{4,5}$ s. "
             r"¿Cuál es su aceleración promedio en $\mathrm{m/s^2}$?",
   respuesta=r"$a = \dfrac{\num{26,4}\ \mathrm{m/s}}{\num{4,5}\ \text{s}} \approx \num{5,9}\ "
             r"\mathrm{m/s^2}$.")
def _():
    aprox(95 * km / h / (4.5 * s), 5.86, m / s**2, rel=0.002)


@E(45, f"{PROB} — 13",
   enunciado=r"Un automóvil alcanza una aceleración de aproximadamente $\num{1,8}\ "
             r"\mathrm{m/s^2}$. A esta razón, ¿cuánto tiempo le toma pasar de 80 km/h a "
             r"110 km/h?",
   respuesta=r"$t = \dfrac{30\ \text{km/h}}{\num{1,8}\ \mathrm{m/s^2}} = "
             r"\dfrac{\num{8,33}\ \mathrm{m/s}}{\num{1,8}\ \mathrm{m/s^2}} \approx \num{4,6}$ s.")
def _():
    aprox((110 - 80) * km / h / (1.8 * m / s**2), 4.63, s, rel=0.002)


@E(46, f"{PROB} — 14a",
   enunciado=r"Una velocista acelera desde el reposo hasta $\num{9,00}$ m/s en $\num{1,28}$ s. "
             r"Calcula su aceleración en $\mathrm{m/s^2}$.",
   respuesta=r"$a = \num{9,00}/\num{1,28} \approx \num{7,03}\ \mathrm{m/s^2}$.")
def _():
    aprox(9.00 * m / s / (1.28 * s), 7.03, m / s**2, rel=0.001)


@E(47, f"{PROB} — 14b",
   enunciado=r"Una velocista acelera desde el reposo hasta $\num{9,00}$ m/s en $\num{1,28}$ s. "
             r"Calcula su aceleración en $\mathrm{km/h^2}$.",
   respuesta=r"$\num{7,03}\ \mathrm{m/s^2} \times \dfrac{(3600\ \text{s/h})^2}{1000\ "
             r"\text{m/km}} \approx \num{9,11e4}\ \mathrm{km/h^2}$.",
   notas="En la guía la unidad aparece como «Km/h cuadrado»; el símbolo del kilómetro es km.")
def _():
    aprox(9.00 * m / s / (1.28 * s), 9.11e4, km / h**2, rel=0.001)


for _n, _lit, _preg, _resp in [
        (48, "a", "¿En qué momento fue máxima su velocidad?",
         r"Hacia $t \approx 50$ s, cuando $v \approx 38$ m/s."),
        (49, "b", "¿Durante qué periodos, si los hubo, su velocidad fue constante?",
         r"Solo entre $t = 90$ s y $t = 100$ s, cuando el tren está detenido ($v = 0$)."),
        (50, "c", "¿Durante qué periodos, si los hubo, su aceleración fue constante?",
         r"De $t = 0$ a $t = 40$ s, cuando $v$ crece en línea recta "
         r"($a = \num{0,5}\ \mathrm{m/s^2}$), y de $t = 90$ s a $t = 100$ s ($a = 0$)."),
        (51, "d", "¿Cuándo fue máxima la magnitud de la aceleración?",
         r"Entre $t \approx 60$ s y $t \approx 80$ s, donde la gráfica baja con más pendiente "
         r"(de 32 a 5 m/s en 20 s: $|a| \approx \num{1,4}\ \mathrm{m/s^2}$).")]:
    M(_n, f"{PROB} — 15{_lit}",
      r"La gráfica de la velocidad de un tren en función del tiempo (Imagen 19) pasa por los "
      r"puntos $(0, 15)$, $(10, 20)$, $(20, 25)$, $(30, 30)$, $(40, 35)$, $(50, 38)$, "
      r"$(60, 32)$, $(70, 20)$, $(80, 5)$, $(90, 0)$, $(100, 0)$, $(110, 3)$ y $(120, 10)$ "
      r"($t$ en s, $v$ en m/s). " + _preg, _resp, dificultad=2,
      notas="Respuesta leída de la descripción de la Imagen 19 (valores aproximados).")


@E(52, f"{PROB} — 16", tipo="contexto",
   enunciado=r"Un automóvil deportivo que se mueve con rapidez constante recorre 110 m en "
             r"$\num{5,0}$ s. Si después frena y se detiene en $\num{4,0}$ s, ¿cuál es la "
             r"magnitud de su aceleración en $\mathrm{m/s^2}$ y en unidades de $g$ "
             r"($g = \num{9,80}\ \mathrm{m/s^2}$)?",
   respuesta=r"$v = 110/5 = 22$ m/s; $|a| = 22/4 = \num{5,5}\ \mathrm{m/s^2} \approx "
             r"\num{0,56}\,g$.")
def _():
    a = (110 * m / (5.0 * s)) / (4.0 * s)
    aprox(a, 5.5, m / s**2, rel=1e-9)
    assert abs(val(a / (9.80 * m / s**2), 1) - 0.56) < 0.005


@E(53, f"{PROB} — 17a",
   enunciado=r"Un automóvil que se mueve en línea recta parte de $x = 0$ en $t = 0$. Pasa por "
             r"$x = \num{25,0}$ m con rapidez de $\num{11,0}$ m/s en $t = \num{3,00}$ s y por "
             r"$x = 385$ m con rapidez de $\num{45,0}$ m/s en $t = \num{20,0}$ s. Encuentra "
             r"su velocidad promedio entre $t = 0$ y $t = \num{20,0}$ s.",
   respuesta=r"$\bar v = 385/\num{20,0} \approx \num{19,3}$ m/s.",
   notas="La guía no dice el intervalo; se toma de t = 0 a t = 20,0 s (en el libro original, "
         "Giancoli, la respuesta es 19,3 m/s).")
def _():
    aprox(385 * m / (20.0 * s), 19.25, m / s, rel=1e-9)


@E(54, f"{PROB} — 17b",
   enunciado=r"El mismo automóvil pasa por $x = \num{25,0}$ m con $\num{11,0}$ m/s en "
             r"$t = \num{3,00}$ s y por $x = 385$ m con $\num{45,0}$ m/s en "
             r"$t = \num{20,0}$ s. Encuentra su aceleración promedio entre esos instantes.",
   respuesta=r"$\bar a = \dfrac{45 - 11}{20 - 3} = \dfrac{34}{17} = \num{2,00}\ "
             r"\mathrm{m/s^2}$.")
def _():
    aprox((45.0 - 11.0) * m / s / ((20.0 - 3.00) * s), 2.00, m / s**2, rel=1e-9)


# ---------- Problemas: movimiento con aceleración constante ----------

@E(55, f"{PROB} — 18",
   enunciado=r"Un auto desacelera de 25 m/s al reposo en una distancia de 85 m. ¿Cuál fue su "
             r"aceleración, suponiéndola constante?",
   respuesta=r"$a = \dfrac{0 - 25^2}{2(85)} \approx -\num{3,7}\ \mathrm{m/s^2}$.")
def _():
    aprox(-(25 * m / s)**2 / (2 * 85 * m), -3.68, m / s**2, rel=0.002)


@E(56, f"{PROB} — 19",
   enunciado=r"Un auto acelera de 12 m/s a 21 m/s en $\num{6,0}$ s. ¿Cuál fue su aceleración? "
             r"¿Qué distancia recorrió en ese tiempo? Supón aceleración constante.",
   respuesta=r"$a = 9/6 = \num{1,5}\ \mathrm{m/s^2}$; "
             r"$x = \dfrac{12 + 21}{2}(\num{6,0}) = 99$ m.")
def _():
    v0, v, t = 12 * m / s, 21 * m / s, 6.0 * s
    a = (v - v0) / t
    aprox(a, 1.5, m / s**2, rel=1e-9)
    aprox(v0 * t + a * t**2 / 2, 99, m, rel=1e-9)


@E(57, f"{PROB} — 20", tipo="contexto",
   enunciado=r"Una avioneta debe alcanzar una rapidez de 32 m/s para despegar. ¿Qué longitud "
             r"de pista necesita si su aceleración constante es de $\num{3,0}\ "
             r"\mathrm{m/s^2}$?",
   respuesta=r"$x = \dfrac{v^2}{2a} = \dfrac{32^2}{6} \approx 171$ m "
             r"($\approx \num{1,7e2}$ m).")
def _():
    aprox((32 * m / s)**2 / (2 * 3.0 * m / s**2), 170.7, m, rel=0.002)


@E(58, f"{PROB} — 21", tipo="contexto",
   enunciado=r"Un lanzador de béisbol lanza una pelota a 41 m/s. Al lanzarla, acelera la "
             r"pelota a lo largo de unos $\num{3,5}$ m, desde atrás de su cuerpo hasta el "
             r"punto donde la suelta. Estima la aceleración promedio de la pelota.",
   respuesta=r"$a = \dfrac{v^2}{2x} = \dfrac{41^2}{7} \approx 240\ \mathrm{m/s^2}$ "
             r"($\approx 24\,g$).")
def _():
    aprox((41 * m / s)**2 / (2 * 3.5 * m), 240, m / s**2, rel=0.002)


@E(59, f"{PROB} — 22", tipo="contexto",
   enunciado=r"Una corredora de nivel mundial alcanza su rapidez máxima, de "
             r"$\num{11,5}$ m/s, en los primeros $\num{15,0}$ m de una carrera. ¿Cuál es su "
             r"aceleración promedio y cuánto tarda en alcanzar esa rapidez?",
   respuesta=r"$a = \dfrac{\num{11,5}^2}{2(15)} \approx \num{4,4}\ \mathrm{m/s^2}$; "
             r"$t = \dfrac{2x}{v} = \dfrac{30}{\num{11,5}} \approx \num{2,6}$ s.")
def _():
    v, x = 11.5 * m / s, 15.0 * m
    a = v**2 / (2 * x)
    aprox(a, 4.41, m / s**2, rel=0.002)
    aprox(v / a, 2.61, s, rel=0.002)


@E(60, f"{PROB} — 23", tipo="contexto", dificultad=2,
   enunciado=r"Un conductor distraído va a $\num{18,0}$ m/s cuando ve adelante una luz roja, "
             r"a $\num{20,0}$ m de la intersección. Su automóvil puede desacelerar a "
             r"$\num{3,65}\ \mathrm{m/s^2}$ y a él le toma $\num{0,200}$ s aplicar los frenos. "
             r"¿Será capaz de detenerse a tiempo?",
   respuesta=r"No. En el tiempo de reacción recorre $18 \times \num{0,2} = \num{3,6}$ m y "
             r"frenando $\dfrac{18^2}{2(\num{3,65})} \approx \num{44,4}$ m: necesita unos "
             r"48 m y solo tiene 20 m.")
def _():
    v = 18.0 * m / s
    d = v * 0.200 * s + v**2 / (2 * 3.65 * m / s**2)
    aprox(d, 48.0, m, rel=0.002)
    assert val(d, m) > 20.0


@E(61, f"{PROB} — 24",
   enunciado=r"Un automóvil desacelera uniformemente desde $\num{18,0}$ m/s hasta el reposo en "
             r"$\num{5,00}$ s. ¿Qué distancia viajó en ese tiempo?",
   respuesta=r"$x = \dfrac{18 + 0}{2}(5) = 45$ m.")
def _():
    v0, t = 18.0 * m / s, 5.00 * s
    a = -v0 / t
    aprox(v0 * t + a * t**2 / 2, 45, m, rel=1e-9)


@E(62, f"{PROB} — 25", tipo="contexto",
   enunciado=r"Al detenerse, un automóvil deja marcas de derrape de 85 m de longitud. "
             r"Suponiendo una desaceleración de $\num{4,00}\ \mathrm{m/s^2}$, estima la "
             r"rapidez del automóvil justo antes de frenar.",
   respuesta=r"$v_0 = \sqrt{2ax} = \sqrt{2(4)(85)} \approx 26$ m/s ($\approx 94$ km/h).")
def _():
    v0 = raiz(2 * 4.00 * m / s**2 * 85 * m, m / s)
    aprox(v0, 26.1, m / s, rel=0.002)
    aprox(v0, 94, km / h, rel=0.005)


@E(63, f"{PROB} — 26", tipo="contexto", dificultad=3,
   enunciado=r"Un corredor espera completar la carrera de $\num{10000}$ m en menos de "
             r"$\num{30,0}$ min. Después de correr con rapidez constante durante exactamente "
             r"$\num{27,0}$ min, aún le faltan $1100$ m. ¿Durante cuántos segundos debe "
             r"acelerar a $\num{0,20}\ \mathrm{m/s^2}$ (y seguir luego con la nueva rapidez) "
             r"para terminar en el tiempo deseado?",
   respuesta=r"Su rapidez es $8900/1620 \approx \num{5,49}$ m/s y le quedan 180 s. Si acelera "
             r"durante $t$: $\num{5,49}t + \num{0,1}t^2 + (\num{5,49} + \num{0,2}t)(180 - t) = "
             r"1100$, o sea $t^2 - 360t + 1111 = 0$, y $t \approx \num{3,1}$ s.")
def _():
    v = val(8900 * m / (27.0 * 60 * s), m / s)
    a, T, D = 0.20, 180.0, 1100.0
    # D = v t + a t²/2 + (v + a t)(T − t)  →  −(a/2) t² + a T t + v T − D = 0
    A, B, C = -a / 2, a * T, v * T - D
    t = (-B + sqrt(B * B - 4 * A * C)) / (2 * A)
    assert abs(t - 3.1) < 0.05
    assert abs(v * t + a * t**2 / 2 + (v + a * t) * (T - t) - D) < 1e-6


# ---------- Problemas: caída libre (sin resistencia del aire) ----------

@E(64, f"{PROB} — 27",
   enunciado=r"Se deja caer una piedra desde lo alto de un acantilado y toca el suelo "
             r"$\num{3,75}$ s después. ¿Cuál es la altura del acantilado?",
   respuesta=r"$h = \frac{1}{2}gt^2 = \frac{1}{2}(\num{9,8})(\num{3,75})^2 \approx 69$ m.")
def _():
    aprox(G * (3.75 * s)**2 / 2, 68.9, m, rel=0.002)


@E(65, f"{PROB} — 28",
   enunciado=r"Si un automóvil cae desde un acantilado vertical partiendo del reposo, "
             r"¿cuánto tiempo le toma alcanzar 55 km/h?",
   respuesta=r"$t = \dfrac{v}{g} = \dfrac{\num{15,3}\ \mathrm{m/s}}{\num{9,8}\ "
             r"\mathrm{m/s^2}} \approx \num{1,6}$ s.")
def _():
    aprox(55 * km / h / G, 1.56, s, rel=0.003)


@E(66, f"{PROB} — 29a", tipo="contexto",
   enunciado=r"¿Cuánto tiempo le tomó a King Kong caer desde la cima del edificio Empire "
             r"State, de 380 m de altura?",
   respuesta=r"$t = \sqrt{2h/g} = \sqrt{2(380)/\num{9,8}} \approx \num{8,8}$ s.")
def _():
    aprox(raiz(2 * 380 * m / G, s), 8.81, s, rel=0.002)


@E(67, f"{PROB} — 29b", tipo="contexto",
   enunciado=r"¿Con qué velocidad «aterrizó» King Kong al caer desde 380 m de altura?",
   respuesta=r"$v = \sqrt{2gh} = \sqrt{2(\num{9,8})(380)} \approx 86$ m/s "
             r"($\approx 310$ km/h), hacia abajo.")
def _():
    v = raiz(2 * G * 380 * m, m / s)
    aprox(v, 86.3, m / s, rel=0.002)
    aprox(v, 311, km / h, rel=0.003)


@E(68, f"{PROB} — 30a",
   enunciado=r"Se batea una pelota casi verticalmente hacia arriba con una rapidez de unos "
             r"20 m/s. ¿Qué tan alto sube?",
   respuesta=r"$h = \dfrac{v_0^2}{2g} = \dfrac{400}{\num{19,6}} \approx 20$ m.")
def _():
    aprox((20 * m / s)**2 / (2 * G), 20.4, m, rel=0.002)


@E(69, f"{PROB} — 30b",
   enunciado=r"Se batea una pelota verticalmente hacia arriba a unos 20 m/s. ¿Cuánto tiempo "
             r"permanece en el aire?",
   respuesta=r"$t = \dfrac{2v_0}{g} = \dfrac{40}{\num{9,8}} \approx \num{4,1}$ s.")
def _():
    aprox(2 * 20 * m / s / G, 4.08, s, rel=0.002)


@E(70, f"{PROB} — 31",
   enunciado=r"Un jugador atrapa una pelota $\num{3,2}$ s después de lanzarla verticalmente "
             r"hacia arriba. ¿Con qué velocidad la lanzó y qué altura alcanzó la pelota?",
   respuesta=r"Sube durante $\num{1,6}$ s: $v_0 = g(\num{1,6}) \approx \num{15,7}$ m/s; "
             r"$h = \frac{1}{2}g(\num{1,6})^2 \approx \num{12,5}$ m.")
def _():
    t = 3.2 * s / 2
    aprox(G * t, 15.68, m / s, rel=0.001)
    aprox(G * t**2 / 2, 12.54, m, rel=0.001)


@E(71, f"{PROB} — 32",
   enunciado=r"Un canguro salta y alcanza una altura vertical de $\num{1,65}$ m. ¿Cuánto "
             r"tiempo está en el aire antes de tocar el suelo de nuevo?",
   respuesta=r"$t = 2\sqrt{2h/g} = 2\sqrt{2(\num{1,65})/\num{9,8}} \approx \num{1,16}$ s.")
def _():
    aprox(2 * raiz(2 * 1.65 * m / G, s), 1.16, s, rel=0.003)


@E(72, f"{PROB} — 33a",
   enunciado=r"Los mejores saltadores de baloncesto tienen un salto vertical de unos "
             r"120 cm. ¿Cuál es su rapidez inicial al despegar del piso?",
   respuesta=r"$v_0 = \sqrt{2gh} = \sqrt{2(\num{9,8})(\num{1,20})} \approx \num{4,85}$ m/s.")
def _():
    aprox(raiz(2 * G * 120 * centimeter, m / s), 4.85, m / s, rel=0.002)


@E(73, f"{PROB} — 33b",
   enunciado=r"Un saltador de baloncesto sube 120 cm en su salto vertical. ¿Cuánto tiempo "
             r"permanece en el aire?",
   respuesta=r"$t = \dfrac{2v_0}{g} = \dfrac{2(\num{4,85})}{\num{9,8}} \approx \num{0,99}$ s.")
def _():
    aprox(2 * raiz(2 * G * 1.20 * m, m / s) / G, 0.99, s, rel=0.005)


@E(74, f"{PROB} — 34", tipo="contexto", dificultad=2,
   enunciado=r"Un helicóptero asciende verticalmente con una rapidez de $\num{5,10}$ m/s. A "
             r"una altura de 105 m se deja caer un paquete desde una ventana. ¿Cuánto tarda "
             r"el paquete en llegar al suelo? (El paquete sale con la velocidad del "
             r"helicóptero).",
   respuesta=r"Con $+$ hacia arriba: $0 = 105 + \num{5,10}t - \num{4,9}t^2$, de donde "
             r"$t \approx \num{5,2}$ s.")
def _():
    a, b, c = -4.9, 5.10, 105.0
    t = (-b - sqrt(b * b - 4 * a * c)) / (2 * a)
    assert abs(t - 5.18) < 0.01
    y = 105 * m + 5.10 * m / s * (t * s) - G * (t * s)**2 / 2      # altura al llegar
    assert abs(val(y, m)) < 1e-9


for _n, _lit, _preg, _resp in [
        (75, "a", "¿Cuál era su rapidez inicial?",
         r"$v_0 = \sqrt{14^2 + 2(\num{9,8})(23)} \approx \num{25,4}$ m/s."),
        (76, "b", "¿Hasta qué altura llega?",
         r"$h = \dfrac{v_0^2}{2g} \approx 33$ m."),
        (77, "c", "¿Cuándo se lanzó?",
         r"$t = \dfrac{v_0 - 14}{g} \approx \num{1,17}$ s antes de pasar por la ventana."),
        (78, "d", "¿Cuándo regresará a la calle?",
         r"A los $\dfrac{2v_0}{g} \approx \num{5,19}$ s de lanzada, es decir, unos "
         r"$\num{4,0}$ s después de pasar hacia arriba por la ventana.")]:
    @E(_n, f"{PROB} — 35{_lit}", tipo="contexto", dificultad=2,
       enunciado=r"Una pelota de béisbol pasa hacia arriba frente a una ventana que está a "
                 r"23 m sobre la calle, con rapidez vertical de 14 m/s. Si la pelota se lanzó "
                 r"desde la calle: " + _preg,
       respuesta=_resp)
    def _(lit=_lit):
        v0 = raiz((14 * m / s)**2 + 2 * G * 23 * m, m / s)
        aprox(v0, 25.4, m / s, rel=0.002)
        if lit == "b":
            aprox(v0**2 / (2 * G), 33.0, m, rel=0.002)
        if lit == "c":
            aprox((v0 - 14 * m / s) / G, 1.17, s, rel=0.005)
        if lit == "d":
            aprox(2 * v0 / G, 5.19, s, rel=0.002)
            aprox(2 * v0 / G - (v0 - 14 * m / s) / G, 4.02, s, rel=0.005)


@E(79, f"{PROB} — 36", tipo="contexto", dificultad=3,
   enunciado=r"Un cohete de juguete que sube verticalmente pasa frente a una ventana de "
             r"$\num{2,0}$ m de altura cuyo alféizar está a $\num{8,0}$ m sobre el suelo, y "
             r"tarda $\num{0,15}$ s en recorrer los $\num{2,0}$ m de la ventana. ¿Con qué "
             r"rapidez se lanzó y qué tan alto subirá? (Todo el combustible se quema durante "
             r"el despegue).",
   respuesta=r"En el alféizar: $2 = v_1(\num{0,15}) - \num{4,9}(\num{0,15})^2 \Rightarrow "
             r"v_1 \approx \num{14,1}$ m/s. Entonces $v_0 = \sqrt{v_1^2 + 2g(8)} \approx 19$ "
             r"m/s y $h_{\max} = v_0^2/2g \approx 18$ m.",
   notas="Se supone que el cohete pasa por la ventana mientras sube.")
def _():
    t = 0.15
    v1 = (2.0 + 4.9 * t * t) / t
    v0 = raiz((v1 * m / s)**2 + 2 * G * 8.0 * m, m / s)
    aprox(v0, 18.8, m / s, rel=0.005)
    aprox(v0**2 / (2 * G), 18.1, m, rel=0.005)
