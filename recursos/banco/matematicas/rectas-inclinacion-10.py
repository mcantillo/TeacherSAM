"""Banco de ejercicios — Geometría 10° — Rectas en el plano cartesiano: pendiente, ángulo de
inclinación, puntos sobre rectas y círculos.
Fuente: módulo de Matemáticas 10° de las Guías de Apoyo, Tema 4 («Otras funciones
trigonométricas», sección «La función tangente y la pendiente», Practica lo aprendido,
problemas 13, 14, 15, 16, 22 y 29); se lee en
recursos/matematicas/Guías pedagógicas Matemáticas/markdown/10 - Modulo_Matematicas_Decimo.md
Es el único material de geometría analítica de los módulos para 10°: el módulo de Geometría
(Modulo_Matematicas_Geometria.md) cubre ángulos, triángulos, Pitágoras, polígonos y
circunferencia al nivel de 6°–8° y no trae cónicas ni lugares geométricos en el plano
cartesiano.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/rectas-inclinacion-10.py
"""
import math

import sympy as sp
from sympy import Point, Rational as Q, pi, sqrt

from ejercicios import ejercicio

PRE = "rectas-inclinacion-10"
FP = ("módulo 10° (Guías de Apoyo), Tema 4, La función tangente y la pendiente — "
      "Practica lo aprendido")
COMUN = dict(tema="pendiente y ángulo de inclinación de una recta", grados=[10],
             dba=["matematicas-10-5"])
x, y = sp.symbols("x y", real=True)


def cierto(cond, msj="no se cumple"):
    assert bool(cond), msj


def igual(a, b):
    assert sp.simplify(a - b) == 0, f"{a} ≠ {b}"


def cerca(calc, mano, dec):
    assert abs(float(calc) - mano) <= 0.5 * 10 ** -dec + 1e-9, f"calculado {calc}, a mano {mano}"


def reg(n, fuente, enunciado, respuesta, check, tipo="calculo", dificultad=1, notas=None):
    meta = dict(id=f"{PRE}-{n:03d}", fuente=fuente, enunciado=enunciado, respuesta=respuesta,
                tipo=tipo, dificultad=dificultad, **COMUN)
    if notas:
        meta["notas"] = notas
    ejercicio(**meta)(check)


def corte_circulo_unitario(P):
    """Punto donde el rayo desde el origen hacia P corta el círculo unitario."""
    pts = sp.Circle(Point(0, 0), 1).intersection(sp.Ray(Point(0, 0), P))
    assert len(pts) == 1
    return pts[0]


def inclinacion(m):
    """Ángulo de inclinación (grados, en [0°, 180°)) de una recta de pendiente m."""
    return math.degrees(math.atan(m)) % 180


reg(1, f"{FP} 13",
    r"¿En qué punto corta al círculo unitario $x^2 + y^2 = 1$ el segmento que va desde el origen "
    r"hasta $(5, -12)$?",
    r"La distancia de $(5, -12)$ al origen es $13$; el punto es $\left(\dfrac{5}{13}, "
    r"-\dfrac{12}{13}\right)$.",
    lambda: cierto(corte_circulo_unitario(Point(5, -12)) == Point(Q(5, 13), -Q(12, 13))))
reg(2, f"{FP} 14",
    r"¿En qué punto corta al círculo unitario $x^2 + y^2 = 1$ el segmento que va desde el origen "
    r"hasta $(-6, 8)$?",
    r"La distancia de $(-6, 8)$ al origen es $10$; el punto es $\left(-\dfrac{3}{5}, "
    r"\dfrac{4}{5}\right)$.",
    lambda: cierto(corte_circulo_unitario(Point(-6, 8)) == Point(-Q(3, 5), Q(4, 5))))
reg(3, f"{FP} 15", r"Encuentra el ángulo de inclinación de la recta $5x + 2y = 6$.",
    r"Su pendiente es $m = -\dfrac{5}{2}$; como $m < 0$, $\theta = 180^\circ - \arctg\dfrac{5}{2} "
    r"\approx \num{111,8}^\circ$.",
    lambda: (igual(sp.Line(5 * x + 2 * y - 6).slope, -Q(5, 2)),
             cerca(inclinacion(float(sp.Line(5 * x + 2 * y - 6).slope)), 111.8, 1)),
    dificultad=2)
reg(4, f"{FP} 16",
    r"Encuentra la ecuación de la recta que tiene ángulo de inclinación $75^\circ$ y pasa por "
    r"$(-2, 4)$.",
    r"$m = \tg 75^\circ = 2 + \sqrt{3}$, así que $y - 4 = (2 + \sqrt{3})(x + 2)$.",
    lambda: (igual(sp.tan(75 * pi / 180), 2 + sqrt(3)),
             cierto(sp.Line(Point(-2, 4), slope=2 + sqrt(3)).contains(Point(-1, 6 + sqrt(3))))),
    dificultad=2)
reg(5, f"{FP} 22",
    r"Encuentra el ángulo de inclinación de la recta perpendicular a la recta $4x + 3y = 9$.",
    r"La recta dada tiene pendiente $-\dfrac{4}{3}$; la perpendicular tiene pendiente "
    r"$\dfrac{3}{4}$ y ángulo de inclinación $\arctg\dfrac{3}{4} \approx \num{36,9}^\circ$.",
    lambda: (lambda L=sp.Line(4 * x + 3 * y - 9): (
        igual(L.perpendicular_line(Point(0, 3)).slope, Q(3, 4)),
        cerca(inclinacion(float(L.perpendicular_line(Point(0, 3)).slope)), 36.9, 1)))(),
    dificultad=2)


def manecilla(angulo_desde_las_12, largo=5):
    """Punta de una manecilla: el ángulo se mide desde las 12 en el sentido del reloj."""
    a = sp.pi / 2 - sp.rad(angulo_desde_las_12)
    return Point(largo * sp.cos(a), largo * sp.sin(a))


reg(6, f"{FP} 29a",
    r"La carátula de un reloj está en el plano $xy$ con centro en el origen y el $12$ sobre el "
    r"eje $y$ positivo; las dos manecillas miden $5$ unidades. Encuentra la pendiente del "
    r"minutero a las $2{:}24$.",
    r"A los $24$ minutos el minutero está $144^\circ$ después de las $12$, es decir, a "
    r"$90^\circ - 144^\circ = -54^\circ$ en posición estándar: $m = \tg(-54^\circ) \approx "
    r"-\num{1,376}$.",
    lambda: cerca(sp.Line(Point(0, 0), manecilla(24 * 6)).slope.evalf(), -1.376, 3),
    tipo="contexto", dificultad=2)
reg(7, f"{FP} 29b",
    r"En el mismo reloj (centro en el origen, $12$ sobre el eje $y$ positivo, manecillas de $5$ "
    r"unidades), encuentra la pendiente de la recta que pasa por las puntas de las dos "
    r"manecillas a las $12{:}50$.",
    r"El minutero está a $300^\circ$ de las $12$ (posición estándar $150^\circ$) y el horario "
    r"a $25^\circ$ (posición estándar $65^\circ$). Las puntas son $(5\cos 150^\circ, "
    r"5\sen 150^\circ)$ y $(5\cos 65^\circ, 5\sen 65^\circ)$, y la pendiente es "
    r"$\dfrac{\sen 65^\circ - \sen 150^\circ}{\cos 65^\circ - \cos 150^\circ} = "
    r"\tg \num{17,5}^\circ \approx \num{0,315}$.",
    lambda: (cerca(sp.Line(manecilla(50 * 6), manecilla(Q(50, 60) * 30)).slope.evalf(), 0.315, 3),
             cerca(math.tan(math.radians(17.5)), 0.315, 3)),
    tipo="contexto", dificultad=3)
