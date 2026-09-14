"""Banco de ejercicios — Trigonometría 10° — Seno y coseno en el círculo unitario.
Fuente: módulo de Matemáticas 10° de las Guías de Apoyo, Tema 3 («Definición del seno y del
coseno»: Practica lo aprendido y Prepárate para el ICFES) y los problemas 5, 7, 8 y 15 del
«Prepárate para el ICFES» final; se lee en
recursos/matematicas/Guías pedagógicas Matemáticas/markdown/10 - Modulo_Matematicas_Decimo.md
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/circulo-unitario-10.py
"""
import math

import sympy as sp
from sympy import Interval, Rational as Q, S, cos, pi, sin, sqrt

from ejercicios import ejercicio, ejercicio_manual, latex_es

PRE = "circulo-unitario-10"
FP = "módulo 10° (Guías de Apoyo), Tema 3, Definición del seno y del coseno — Practica lo aprendido"
FI = "módulo 10° (Guías de Apoyo), Tema 3, Definición del seno y del coseno — Prepárate para el ICFES"
FR = "módulo 10° (Guías de Apoyo), Resumen del capítulo — Prepárate para el ICFES"
COMUN = dict(tema="seno y coseno en el círculo unitario", grados=[10], dba=["matematicas-10-4"])
t = sp.Symbol("t", real=True)


def N(x):
    return r"\num{" + str(x).replace(".", ",") + "}"


def igual(a, b):
    assert sp.simplify(a - b) == 0, f"{a} ≠ {b}"


def cierto(cond, msj="no se cumple"):
    assert bool(cond), msj


def cerca(calc, mano, dec):
    assert abs(float(calc) - mano) <= 0.5 * 10 ** -dec + 1e-9, f"calculado {calc}, a mano {mano}"


def meta(n, fuente, enunciado, respuesta, tipo, dificultad, notas):
    m = dict(id=f"{PRE}-{n:03d}", fuente=fuente, enunciado=enunciado, respuesta=respuesta,
             tipo=tipo, dificultad=dificultad, **COMUN)
    if notas:
        m["notas"] = notas
    return m


def reg(n, fuente, enunciado, respuesta, check, tipo="calculo", dificultad=1, notas=None):
    ejercicio(**meta(n, fuente, enunciado, respuesta, tipo, dificultad, notas))(check)


def manual(n, fuente, enunciado, respuesta, tipo="argumentacion", dificultad=2, notas=None):
    ejercicio_manual(**meta(n, fuente, enunciado, respuesta, tipo, dificultad, notas))


def punto(x, y):
    return r"\left(%s, %s\right)" % (latex_es(x), latex_es(y))


def en_intervalo(expr, rel, a, b):
    """Conjunto de t en [a, b] donde «expr rel 0», calculado con las raíces de expr = 0 y el
    signo en cada tramo (independiente de la respuesta escrita a mano)."""
    raices = sorted(set(sp.solveset(sp.Eq(expr, 0), t, Interval(a, b))) | {a, b},
                    key=lambda v: float(v))
    cumple = {">": lambda v: v > 1e-12, ">=": lambda v: v > -1e-12,
              "<": lambda v: v < -1e-12, "<=": lambda v: v < 1e-12}[rel]
    val = lambda v: float(expr.subs(t, v))
    total = S.EmptySet
    for p, q in zip(raices, raices[1:]):
        if cumple(val((p + q) / 2)):
            total |= Interval(p, q, not cumple(val(p)), not cumple(val(q)))
    for p in raices:
        if cumple(val(p)):
            total |= sp.FiniteSet(p)
    return total


# ---------- 1. Coordenadas de P(t) ----------
filas1 = [("a", 13 * pi / 6, sqrt(3) / 2, Q(1, 2)), ("b", 19 * pi / 6, -sqrt(3) / 2, -Q(1, 2)),
          ("c", 19 * pi / 4, -sqrt(2) / 2, sqrt(2) / 2), ("d", 15 * pi / 4, sqrt(2) / 2, -sqrt(2) / 2),
          ("e", sp.Add(24 * pi, 5 * pi / 4, evaluate=False), -sqrt(2) / 2, -sqrt(2) / 2),
          ("f", sp.Add(16 * pi, 5 * pi / 6, evaluate=False), -sqrt(3) / 2, Q(1, 2)),
          ("g", -7 * pi / 6, -sqrt(3) / 2, Q(1, 2)), ("h", 13 * pi / 4, -sqrt(2) / 2, -sqrt(2) / 2)]
for i, (lit, tt, x, y) in enumerate(filas1):
    tx = r"24\pi + \dfrac{5\pi}{4}" if lit == "e" else (
        r"16\pi + \dfrac{5\pi}{6}" if lit == "f" else latex_es(tt))
    reg(1 + i, f"{FP} 1{lit}",
        r"Encuentra las coordenadas del punto trigonométrico $P(t)$ para $t = %s$. Dibuja el "
        r"círculo unitario y ubica $P(t)$." % tx,
        r"$P\left(%s\right) = %s$." % (tx, punto(x, y)),
        lambda tt=tt, x=x, y=y: (igual(cos(tt), x), igual(sin(tt), y)))

# ---------- 2. Valores de seno y coseno ----------
G = pi / 180
filas2 = [("a", "sen", -pi / 4, None, -sqrt(2) / 2), ("b", "sen", 15 * pi / 4, None, -sqrt(2) / 2),
          ("c", "sen", -5 * pi / 4, None, sqrt(2) / 2), ("d", "sen", 9 * pi / 4, None, sqrt(2) / 2),
          ("e", "cos", 13 * pi / 4, None, -sqrt(2) / 2), ("f", "cos", -7 * pi / 4, None, sqrt(2) / 2),
          ("g", "cos", 10 * pi / 3, None, -Q(1, 2)), ("h", "cos", 25 * pi / 6, None, sqrt(3) / 2),
          ("i", "sen", 5 * pi / 2, None, 1), ("j", "cos", 7 * pi, None, -1),
          ("k", "sen", -4 * pi, None, 0), ("l", "cos", 7 * pi / 2, None, 0),
          ("m", "cos", 19 * pi / 6, None, -sqrt(3) / 2), ("n", "sen", 14 * pi / 3, None, sqrt(3) / 2),
          ("o", "cos", -pi / 3, None, Q(1, 2)), ("p", "sen", -5 * pi / 6, None, -Q(1, 2)),
          ("q", "cos", 125 * pi / 4, None, -sqrt(2) / 2), ("r", "cos", -13 * pi / 6, None, sqrt(3) / 2),
          ("s", "sen", None, 510, Q(1, 2)), ("t", "cos", None, -720, 1),
          ("u", "sen", None, -390, -Q(1, 2)), ("v", "cos", None, -210, -sqrt(3) / 2),
          ("w", "cos", None, 840, -Q(1, 2)), ("x", "sen", None, 900, 0)]
for i, (lit, f, r, g, v) in enumerate(filas2):
    arg = r"\left(%s\right)" % latex_es(r) if g is None else r"(%d^\circ)" % g
    fx = {"sen": sin, "cos": cos}[f]
    reg(9 + i, f"{FP} 2{lit}",
        r"Usa el círculo unitario (sin calculadora) para hallar el valor exacto de "
        r"$\%s%s$." % (f, arg),
        r"$\%s%s = %s$." % (f, arg, latex_es(v)),
        lambda fx=fx, r=r, g=g, v=v: igual(fx(r if g is None else g * G), v),
        dificultad=1 if lit in "aioks" else 2)

# ---------- 3–6. Paridad e identidad pitagórica ----------
reg(33, f"{FP} 3",
    r"Si $\sen \num{1,87} = \num{0,95557}$ y $\cos \num{1,87} = -\num{0,29476}$, encuentra "
    r"$\sen(-\num{1,87})$ y $\cos(-\num{1,87})$.",
    r"$\sen(-\num{1,87}) = -\num{0,95557}$ (el seno es impar) y $\cos(-\num{1,87}) = "
    r"-\num{0,29476}$ (el coseno es par).",
    lambda: (cerca(math.sin(1.87), 0.95557, 5), cerca(math.sin(-1.87), -0.95557, 5),
             cerca(math.cos(-1.87), -0.29476, 5)))
reg(34, f"{FP} 4",
    r"Si $\sen \num{15,2}^\circ = \num{0,2622}$ y $\cos \num{15,2}^\circ = \num{0,9650}$, "
    r"encuentra $\sen(-\num{15,2}^\circ)$ y $\cos(-\num{15,2}^\circ)$.",
    r"$\sen(-\num{15,2}^\circ) = -\num{0,2622}$ y $\cos(-\num{15,2}^\circ) = \num{0,9650}$.",
    lambda: (cerca(math.sin(math.radians(-15.2)), -0.2622, 4),
             cerca(math.cos(math.radians(-15.2)), 0.9650, 4)))
T5 = sp.atan2(-2 / sqrt(5), 1 / sqrt(5))
reg(35, f"{FP} 5a",
    r"$P(t)$ tiene coordenadas $\left(\dfrac{1}{\sqrt{5}}, \dfrac{-2}{\sqrt{5}}\right)$. "
    r"¿Cuáles son las coordenadas de $P(-t)$?",
    r"$P(-t) = \left(\dfrac{1}{\sqrt{5}}, \dfrac{2}{\sqrt{5}}\right)$ (simétrico respecto al "
    r"eje $x$).",
    lambda: (igual(Q(1, 5) + Q(4, 5), 1), igual(cos(-T5), 1 / sqrt(5)), igual(sin(-T5), 2 / sqrt(5))))
reg(36, f"{FP} 5b",
    r"$P(t)$ tiene coordenadas $\left(\dfrac{1}{\sqrt{5}}, \dfrac{-2}{\sqrt{5}}\right)$. "
    r"¿Cuáles son los valores de $\sen(-t)$ y $\cos(-t)$?",
    r"$\sen(-t) = \dfrac{2}{\sqrt{5}}$ y $\cos(-t) = \dfrac{1}{\sqrt{5}}$.",
    lambda: (igual(sin(-T5), 2 / sqrt(5)), igual(cos(-T5), 1 / sqrt(5))))
T6 = pi + sp.asin(Q(3, 5))   # cuadrante III con sen t = -3/5
for i, (lit, tx, e, v) in enumerate([("a", r"\sen(-t)", sin(-T6), Q(3, 5)),
                                     ("b", r"\cos t", cos(T6), -Q(4, 5)),
                                     ("c", r"\cos(-t)", cos(-T6), -Q(4, 5))]):
    reg(37 + i, f"{FP} 6{lit}",
        r"$t$ es la medida en radianes de un ángulo del cuadrante III y $\sen t = -\dfrac{3}{5}$. "
        r"Evalúa $%s$.%s" % (tx, " Sugerencia: usa la identidad pitagórica." if lit == "b" else ""),
        r"$%s = %s$." % (tx, latex_es(v)),
        lambda e=e, v=v: (igual(sin(T6), -Q(3, 5)), igual(e, v)),
        notas="En el módulo: «c. os ( -t )»; es cos(−t)." if lit == "c" else None)
manual(40, f"{FP} 7a",
       r"Los puntos $P(t)$ y $P(t + \pi)$ son simétricos respecto al origen. Usa este hecho para "
       r"probar que $\sen(\pi + t) = -\sen t$.",
       r"Si $P(t) = (x, y)$, el simétrico respecto al origen es $P(t + \pi) = (-x, -y)$. Como el "
       r"seno es la coordenada $y$: $\sen(\pi + t) = -y = -\sen t$.")
manual(41, f"{FP} 7b",
       r"Los puntos $P(t)$ y $P(t + \pi)$ son simétricos respecto al origen. Usa este hecho para "
       r"probar que $\cos(\pi + t) = -\cos t$.",
       r"Si $P(t) = (x, y)$, entonces $P(t + \pi) = (-x, -y)$. Como el coseno es la coordenada "
       r"$x$: $\cos(\pi + t) = -x = -\cos t$.")
reg(42, f"{FP} 8",
    r"Los puntos $P(t)$ y $P(\pi - t)$ son simétricos respecto al eje $y$. Usa este hecho para "
    r"encontrar identidades para $\sen(\pi - t)$ y $\cos(\pi - t)$.",
    r"Si $P(t) = (x, y)$, entonces $P(\pi - t) = (-x, y)$: $\sen(\pi - t) = \sen t$ y "
    r"$\cos(\pi - t) = -\cos t$.",
    lambda: (igual(sin(pi - t), sin(t)), igual(cos(pi - t), -cos(t))), tipo="argumentacion",
    dificultad=2)

# ---------- 9–19. Prepárate para el ICFES del Tema 3 ----------
for i, (lit, tx, e, s) in enumerate([("a", r"\cos 2", cos(2), "-"),
                                     ("b", r"\sen(-3)", sin(-3), "-"),
                                     ("c", r"\cos 428^\circ", cos(428 * G), "+"),
                                     ("d", r"\sen \num{21,4}", sin(Q(214, 10)), "+"),
                                     ("e", r"\sen\left(\dfrac{23\pi}{32}\right)", sin(23 * pi / 32), "+"),
                                     ("f", r"\sen(-820^\circ)", sin(-820 * G), "-")]):
    reg(43 + i, f"{FI} 9{lit}",
        r"Usa el círculo unitario (sin calculadora) para determinar el signo de $%s$." % tx,
        r"$%s %s 0$." % (tx, "<" if s == "-" else ">"),
        lambda e=e, s=s: igual(sp.sign(e.evalf()), -1 if s == "-" else 1), tipo="conceptual",
        dificultad=2)
filas10 = [("a", r"\pi", pi, -1, 0), ("b", r"\dfrac{3\pi}{2}", 3 * pi / 2, 0, -1),
           ("c", r"-\dfrac{3\pi}{4}", -3 * pi / 4, -sqrt(2) / 2, -sqrt(2) / 2),
           ("d", r"\dfrac{5\pi}{6}", 5 * pi / 6, -sqrt(3) / 2, Q(1, 2)),
           ("e", r"\dfrac{44\pi}{3}", 44 * pi / 3, -Q(1, 2), sqrt(3) / 2),
           ("f", r"-\num{93,5}\pi", -Q(187, 2) * pi, 0, 1)]
for i, (lit, tx, tt, x, y) in enumerate(filas10):
    reg(49 + i, f"{FI} 10{lit}",
        r"Encuentra las coordenadas de $P(t)$ para $t = %s$." % tx,
        r"$P\left(%s\right) = %s$." % (tx, punto(x, y)),
        lambda tt=tt, x=x, y=y: (igual(cos(tt), x), igual(sin(tt), y)))
reg(55, f"{FI} 11a",
    r"$P(t)$ tiene coordenadas $\left(x, -\dfrac{1}{2}\right)$. Encuentra los dos valores "
    r"posibles de $x$.",
    r"Como $x^2 + \frac{1}{4} = 1$: $x = \dfrac{\sqrt{3}}{2}$ o $x = -\dfrac{\sqrt{3}}{2}$.",
    lambda: cierto(sp.solveset(sp.Symbol("x") ** 2 + Q(1, 4) - 1, sp.Symbol("x"), S.Reals)
                   == sp.FiniteSet(sqrt(3) / 2, -sqrt(3) / 2)))
reg(56, f"{FI} 11b",
    r"$P(t)$ tiene coordenadas $\left(x, -\dfrac{1}{2}\right)$. Encuentra los valores de $t$ que "
    r"corresponden a cada valor posible de $x$.",
    r"Para $x = \dfrac{\sqrt{3}}{2}$: $t = \dfrac{11\pi}{6} + 2k\pi$; para $x = -\dfrac{\sqrt{3}}"
    r"{2}$: $t = \dfrac{7\pi}{6} + 2k\pi$ ($k$ entero).",
    lambda: (cierto(sp.solveset(sin(t) + Q(1, 2), t, Interval.Ropen(0, 2 * pi))
                    == sp.FiniteSet(7 * pi / 6, 11 * pi / 6)),
             igual(cos(11 * pi / 6), sqrt(3) / 2), igual(cos(7 * pi / 6), -sqrt(3) / 2)),
    dificultad=2)
reg(57, f"{FI} 12",
    r"Una cuerda de longitud $\dfrac{4\pi}{3}$ se enrolla alrededor del círculo unitario en el "
    r"sentido de las manecillas del reloj, empezando en el punto $(0, -1)$. ¿Cuáles son las "
    r"coordenadas del otro extremo?",
    r"$(0, -1) = P\left(-\frac{\pi}{2}\right)$ y el extremo es $P\left(-\frac{\pi}{2} - "
    r"\frac{4\pi}{3}\right) = P\left(-\frac{11\pi}{6}\right) = P\left(\frac{\pi}{6}\right) = "
    r"\left(\dfrac{\sqrt{3}}{2}, \dfrac{1}{2}\right)$.",
    lambda: (igual(cos(-pi / 2 - 4 * pi / 3), sqrt(3) / 2), igual(sin(-pi / 2 - 4 * pi / 3), Q(1, 2))),
    dificultad=2, notas="En el módulo: «punto inicial (0. -1)»; es (0, −1).")
DOS = 2 * pi
filas13 = [("a", r"\sen t = \cos t", sp.FiniteSet(pi / 4, 5 * pi / 4),
            lambda: sp.solveset(sin(t) - cos(t), t, Interval(0, DOS))),
           ("b", r"\dfrac{1}{2} < \sen t < \dfrac{\sqrt{3}}{2}",
            sp.Union(Interval.open(pi / 6, pi / 3), Interval.open(2 * pi / 3, 5 * pi / 6)),
            lambda: en_intervalo(sin(t) - Q(1, 2), ">", 0, DOS)
            & en_intervalo(sin(t) - sqrt(3) / 2, "<", 0, DOS)),
           ("c", r"\cos^2 t \ge \num{0,25}",
            sp.Union(Interval(0, pi / 3), Interval(2 * pi / 3, 4 * pi / 3), Interval(5 * pi / 3, DOS)),
            lambda: en_intervalo(cos(t) ** 2 - Q(1, 4), ">=", 0, DOS)),
           ("d", r"\cos^2 t \ge \sen^2 t",
            sp.Union(Interval(0, pi / 4), Interval(3 * pi / 4, 5 * pi / 4), Interval(7 * pi / 4, DOS)),
            lambda: en_intervalo(cos(t) ** 2 - sin(t) ** 2, ">=", 0, DOS))]
for i, (lit, tx, sol, calc) in enumerate(filas13):
    reg(58 + i, f"{FI} 13{lit}",
        r"¿Para qué valores de $t$ con $0 \le t \le 2\pi$ se cumple $%s$?" % tx,
        r"$%s$." % latex_es(sol),
        lambda sol=sol, calc=calc: igual(sp.Integer(calc() == sol), 1),
        dificultad=2 if lit == "a" else 3)
filas14 = [("a", r"\sen t = 1", sin(t) - 1, [pi / 2, 5 * pi / 2, 9 * pi / 2, 13 * pi / 2]),
           ("b", r"\cos t = -\dfrac{\sqrt{3}}{2}", cos(t) + sqrt(3) / 2,
            [5 * pi / 6, 7 * pi / 6, 17 * pi / 6, 19 * pi / 6]),
           ("c", r"|\cos t| = \dfrac{1}{2}", cos(t) ** 2 - Q(1, 4),
            [pi / 3, 2 * pi / 3, 4 * pi / 3, 5 * pi / 3]),
           ("d", r"\sen t = -\dfrac{\sqrt{2}}{2}", sin(t) + sqrt(2) / 2,
            [5 * pi / 4, 7 * pi / 4, 13 * pi / 4, 15 * pi / 4])]
for i, (lit, tx, e, sols) in enumerate(filas14):
    reg(62 + i, f"{FI} 14{lit}",
        r"Encuentra las cuatro soluciones positivas más pequeñas de $%s$." % tx,
        r"$t = %s$." % ", ".join(latex_es(s) for s in sols),
        lambda e=e, sols=sols: igual(sp.Integer(
            sorted(sp.solveset(e, t, Interval.open(0, 8 * pi)), key=float)[:4] == sols), 1),
        dificultad=2)
reg(66, f"{FI} 15a",
    r"$\theta$ está en posición estándar con lado final en el cuarto cuadrante. Usa "
    r"$\sen^2\theta + \cos^2\theta = 1$ para hallar $\cos\theta$ si $\sen\theta = -\dfrac{4}{5}$.",
    r"$\cos\theta = \sqrt{1 - \frac{16}{25}} = \dfrac{3}{5}$ (positivo en el cuadrante IV).",
    lambda: igual(cos(-sp.asin(Q(4, 5))), Q(3, 5)))
reg(67, f"{FI} 15b",
    r"$\theta$ está en posición estándar con lado final en el cuarto cuadrante. Usa "
    r"$\sen^2\theta + \cos^2\theta = 1$ para hallar $\sen\theta$ si $\cos\theta = \dfrac{24}{25}$.",
    r"$\sen\theta = -\sqrt{1 - \frac{576}{625}} = -\dfrac{7}{25}$ (negativo en el cuadrante IV).",
    lambda: igual(sin(-sp.acos(Q(24, 25))), -Q(7, 25)),
    notas="En el módulo: «cos θ = 25/24», imposible porque |cos θ| ≤ 1; se corrige a 24/25 "
          "(el recíproco, como en el problema 19 del Tema 4).")
reg(68, f"{FI} 16",
    r"Usa el círculo unitario para encontrar identidades para $\sen(2\pi - t)$ y "
    r"$\cos(2\pi - t)$.",
    r"$P(2\pi - t) = P(-t)$ es el simétrico de $P(t)$ respecto al eje $x$: $\sen(2\pi - t) = "
    r"-\sen t$ y $\cos(2\pi - t) = \cos t$.",
    lambda: (igual(sin(2 * pi - t), -sin(t)), igual(cos(2 * pi - t), cos(t))),
    tipo="argumentacion", dificultad=2)
T17 = -sp.asin(Q(3, 5))   # P(t) = (4/5, -3/5)
for i, (lit, tx, e, v) in enumerate([("a", r"\sen(-t)", sin(-T17), Q(3, 5)),
                                     ("b", r"\cos(2\pi + t)", cos(2 * pi + T17), Q(4, 5)),
                                     ("c", r"\sen(\pi + t)", sin(pi + T17), Q(3, 5)),
                                     ("d", r"\sen\left(\dfrac{\pi}{2} - t\right)", sin(pi / 2 - T17), Q(4, 5)),
                                     ("e", r"\cos(2\pi - t)", cos(2 * pi - T17), Q(4, 5)),
                                     ("f", r"\cos(\pi - t)", cos(pi - T17), -Q(4, 5))]):
    reg(69 + i, f"{FI} 17{lit}",
        r"Si $P(t)$ tiene coordenadas $\left(\dfrac{4}{5}, -\dfrac{3}{5}\right)$, evalúa $%s$." % tx,
        r"$%s = %s$." % (tx, latex_es(v)),
        lambda e=e, v=v: (igual(cos(T17), Q(4, 5)), igual(e, v)))

# 18. Tabla: una entrada por fila
COLS = [r"\sen t", r"\cos t", r"\sen(\pi + t)", r"\cos(\pi + t)", r"\sen(\pi - t)",
        r"\sen(2\pi - t)"]


def columnas(tt):
    return [sin(tt), cos(tt), sin(pi + tt), cos(pi + tt), sin(pi - tt), sin(2 * pi - tt)]


filas18 = [  # (datos: {columna: valor}, t hallado a mano, valores completos a mano)
    ({0: sqrt(3) / 2, 1: -Q(1, 2)}, 2 * pi / 3,
     [sqrt(3) / 2, -Q(1, 2), -sqrt(3) / 2, Q(1, 2), sqrt(3) / 2, -sqrt(3) / 2]),
    ({1: sqrt(2) / 2, 2: sqrt(2) / 2}, 7 * pi / 4,
     [-sqrt(2) / 2, sqrt(2) / 2, sqrt(2) / 2, -sqrt(2) / 2, -sqrt(2) / 2, sqrt(2) / 2]),
    ({0: Q(1, 2), 3: -sqrt(3) / 2}, pi / 6,
     [Q(1, 2), sqrt(3) / 2, -Q(1, 2), -sqrt(3) / 2, Q(1, 2), -Q(1, 2)]),
    ({0: -1}, 3 * pi / 2, [-1, 0, 1, 0, -1, 1]),
    ({3: sqrt(3) / 2, 5: Q(1, 2)}, 7 * pi / 6,
     [-Q(1, 2), -sqrt(3) / 2, Q(1, 2), sqrt(3) / 2, -Q(1, 2), Q(1, 2)]),
    ({1: 0, 5: -1}, pi / 2, [1, 0, -1, 0, 1, -1])]
for i, (datos, tt, vals) in enumerate(filas18):
    dados = ", ".join("$%s = %s$" % (COLS[k], latex_es(v)) for k, v in datos.items())
    reg(75 + i, f"{FI} 18 (fila {i + 1})",
        r"Completa la fila de la tabla en la que " + dados + r": halla $\sen t$, $\cos t$, "
        r"$\sen(\pi + t)$, $\cos(\pi + t)$, $\sen(\pi - t)$, $\sen(2\pi - t)$ y el menor valor "
        r"positivo de $t$.",
        ", ".join("$%s = %s$" % (c, latex_es(v)) for c, v in zip(COLS, vals))
        + r"; el menor $t$ positivo es $%s$." % latex_es(tt),
        lambda datos=datos, tt=tt, vals=vals: (
            [igual(columnas(tt)[k], v) for k, v in datos.items()],
            [igual(a, b) for a, b in zip(columnas(tt), vals)],
            # ningún t positivo menor cumple los datos: sen y cos fijan t en [0, 2π)
            igual(sp.Integer(sp.solveset(sin(t) - vals[0], t, Interval.Ropen(0, 2 * pi))
                             .intersect(sp.solveset(cos(t) - vals[1], t, Interval.Ropen(0, 2 * pi)))
                             == sp.FiniteSet(tt)), 1)),
        dificultad=3, notas="La tabla del módulo se reparte en una entrada por fila." if i == 0 else None)

# 19. Periodicidad de funciones con [x] y {x}
x = sp.Symbol("x", real=True)
ENT = r"Recuerda que $[x]$ es el mayor entero menor o igual que $x$ y $\{x\}$ es la distancia de $x$ al entero más cercano. "
dist = lambda v: abs(v - sp.floor(v + Q(1, 2)))
MUESTRA = [Q(k, 7) for k in range(-20, 21)]
reg(81, f"{FI} 19a", ENT + r"¿Es periódica $f(x) = \{x\}$? Si lo es, da su periodo.",
    r"Sí, con periodo $1$: $\{x + 1\} = \{x\}$, y ningún $p$ con $0 < p < 1$ sirve porque "
    r"$\{0\} = 0$ pero $\{p\} > 0$.",
    lambda: ([igual(dist(v + 1), dist(v)) for v in MUESTRA],
             [cierto(dist(p) > 0) for p in [Q(k, 10) for k in range(1, 10)]]),
    tipo="conceptual", dificultad=3)
reg(82, f"{FI} 19b", ENT + r"¿Es periódica $f(x) = \{3\}$? Si lo es, da su periodo.",
    r"$\{3\} = 0$ para todo $x$: es una función constante, periódica, pero sin periodo mínimo "
    r"(cualquier $p > 0$ cumple $f(x + p) = f(x)$).",
    lambda: igual(dist(sp.Integer(3)), 0), tipo="conceptual", dificultad=3)
reg(83, f"{FI} 19c", ENT + r"¿Es periódica $f(x) = [x]$? Si lo es, da su periodo.",
    r"No: $[x]$ crece sin límite. Si tuviera periodo $p > 0$, sería $[np] = [0] = 0$ para todo "
    r"entero $n$, pero $[np] \ge 1$ cuando $n \ge \frac{1}{p}$.",
    lambda: [cierto(sp.floor((sp.ceiling(1 / p) + 1) * p) >= 1)
             for p in [Q(1, 10), Q(1, 3), Q(7, 10), 1, Q(5, 2)]],
    tipo="conceptual", dificultad=3)
reg(84, f"{FI} 19d", ENT + r"¿Es periódica $f(x) = x - [x]$? Si lo es, da su periodo.",
    r"Sí, con periodo $1$: $(x + 1) - [x + 1] = x - [x]$; y ningún $0 < p < 1$ sirve porque "
    r"$f(0) = 0$ y $f(p) = p \ne 0$.",
    lambda: ([igual((v + 1) - sp.floor(v + 1), v - sp.floor(v)) for v in MUESTRA],
             [igual(p - sp.floor(p), p) for p in [Q(k, 10) for k in range(1, 10)]]),
    tipo="conceptual", dificultad=2)

# ---------- Prepárate para el ICFES del final del módulo ----------
for i, (lit, f, r, v) in enumerate([("a", "sen", 7 * pi / 6, -Q(1, 2)), ("b", "cos", 11 * pi / 6, sqrt(3) / 2),
                                    ("c", "tg", 13 * pi / 4, 1), ("d", "sen", 41 * pi / 6, Q(1, 2))]):
    fx = {"sen": sin, "cos": cos, "tg": sp.tan}[f]
    reg(85 + i, f"{FR} 5{lit}",
        r"Calcula sin tablas ni calculadora $\%s\left(%s\right)$." % (f, latex_es(r)),
        r"$\%s\left(%s\right) = %s$." % (f, latex_es(r), latex_es(v)),
        lambda fx=fx, r=r, v=v: igual(fx(r), v))
for i, (lit, tx, e, v, vtx) in enumerate([("a", r"\sen(-t)", sin(-t), -sin(t), r"-\sen t"),
                                          ("b", r"\sen(t + 4\pi)", sin(t + 4 * pi), sin(t), r"\sen t"),
                                          ("c", r"\sen(\pi + t)", sin(pi + t), -sin(t), r"-\sen t"),
                                          ("d", r"\cos\left(\dfrac{\pi}{2} - t\right)", cos(pi / 2 - t),
                                           sin(t), r"\sen t")]):
    reg(89 + i, f"{FR} 7{lit}", r"Escribe $%s$ en términos de $\sen t$." % tx,
        r"$%s = %s$." % (tx, vtx), lambda e=e, v=v: igual(e, v))
for i, (lit, tx, e, sol) in enumerate([
        ("a", r"\cos t > 0", cos(t), sp.Union(Interval.Ropen(0, pi / 2), Interval.Lopen(3 * pi / 2, DOS))),
        ("b", r"\cos 2t > 0", cos(2 * t), sp.Union(Interval.Ropen(0, pi / 4), Interval.open(3 * pi / 4, 5 * pi / 4),
                                                   Interval.Lopen(7 * pi / 4, DOS)))]):
    reg(93 + i, f"{FR} 8{lit}", r"¿Para qué valores de $t$ entre $0$ y $2\pi$ se cumple $%s$?" % tx,
        r"$%s$." % latex_es(sol),
        lambda e=e, sol=sol: igual(sp.Integer(en_intervalo(e, ">", 0, DOS) == sol), 1),
        dificultad=2)
manual(95, f"{FR} 15", r"Da la definición general de $\cos t$ basándote en el círculo unitario.",
       r"Se recorre el círculo unitario desde $(1, 0)$ una distancia dirigida $|t|$ (en sentido "
       r"contrario a las manecillas del reloj si $t > 0$ y en el sentido de las manecillas si "
       r"$t < 0$); si se llega al punto $P(t) = (x, y)$, entonces $\cos t = x$, la abscisa de ese "
       r"punto.", tipo="conceptual", dificultad=1)
