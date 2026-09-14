"""Banco de ejercicios — Trigonometría 10° — Ángulos y números de referencia; valores de las
funciones trigonométricas para cualquier ángulo.
Fuente: módulo de Matemáticas 10° de las Guías de Apoyo, segundo «Tema 4» («Cálculo de valores
de las funciones trigonométricas», Practica lo aprendido) y el problema 6 del «Prepárate para
el ICFES» final; se lee en
recursos/matematicas/Guías pedagógicas Matemáticas/markdown/10 - Modulo_Matematicas_Decimo.md
El módulo trae dos temas numerados «4»; aquí se cita este como «Tema 4 (cálculo de valores)».
Valores con cuatro decimales (la calculadora); donde el módulo pide usar π ≈ 3,14 y la tabla
se da también ese valor.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/valores-trigonometricos-10.py
"""
import math
from math import radians as rad

import sympy as sp
from sympy import Rational as Q, pi

from ejercicios import ejercicio, latex_es

PRE = "valores-trigonometricos-10"
FP = ("módulo 10° (Guías de Apoyo), Tema 4 (cálculo de valores de las funciones "
      "trigonométricas), Ángulos de referencia y números de referencia — Practica lo aprendido")
FR = "módulo 10° (Guías de Apoyo), Resumen del capítulo — Prepárate para el ICFES"
COMUN = dict(tema="ángulos y números de referencia", grados=[10], dba=["matematicas-10-4"])
NOM = {"tg": r"\tg", "cot": r"\cot", "sec": r"\sec", "csc": r"\csc", "sen": r"\sen", "cos": r"\cos"}
FX = {"sen": math.sin, "cos": math.cos, "tg": math.tan, "cot": lambda v: 1 / math.tan(v)}


def N(x):
    return r"\num{" + str(x).replace(".", ",") + "}"


def cerca(calc, mano, dec):
    assert abs(float(calc) - mano) <= 0.5 * 10 ** -dec + 1e-9, f"calculado {calc}, a mano {mano}"


def igual(a, b):
    assert sp.simplify(a - b) == 0, f"{a} ≠ {b}"


def reg(n, fuente, enunciado, respuesta, check, tipo="calculo", dificultad=1, notas=None):
    meta = dict(id=f"{PRE}-{n:03d}", fuente=fuente, enunciado=enunciado, respuesta=respuesta,
                tipo=tipo, dificultad=dificultad, **COMUN)
    if notas:
        meta["notas"] = notas
    ejercicio(**meta)(check)


def referencia(t, P):
    """Número de referencia de t con «π» = P (P exacto o aproximado) y cuadrante."""
    r = t - 2 * P * sp.floor(t / (2 * P))
    if r <= P / 2:
        return r, 1
    if r <= P:
        return P - r, 2
    if r <= 3 * P / 2:
        return r - P, 3
    return 2 * P - r, 4


SIGNO = {"sen": {1: 1, 2: 1, 3: -1, 4: -1}, "cos": {1: 1, 2: -1, 3: -1, 4: 1},
         "tg": {1: 1, 2: -1, 3: 1, 4: -1}, "cot": {1: 1, 2: -1, 3: 1, 4: -1}}

# ---------- 1. Valores directos ----------
for i, (lit, f, a, g, v) in enumerate([
        ("a", "sen", "1.38", False, "0.9819"), ("b", "cot", "0.82", False, "0.9331"),
        ("c", "cos", "0.67", False, "0.7838"), ("d", "tg", "1.11", False, "2.0143"),
        ("e", "cos", "42.8", True, "0.7337"), ("f", "sen", "68.3", True, "0.9291"),
        ("g", "tg", "18.0", True, "0.3249"), ("h", "cot", "49.6", True, "0.8511")]):
    tx = r"%s %s%s" % (NOM[f], N(a), r"^\circ" if g else "")
    reg(1 + i, f"{FP} 1{lit}",
        r"Encuentra el valor de $%s$ con una tabla o con la calculadora (cuatro decimales)." % tx,
        r"$%s \approx %s$." % (tx, N(v)),
        lambda f=f, a=float(a), g=g, v=float(v): cerca(FX[f](rad(a) if g else a), v, 4),
        notas="El módulo pide usar una tabla; la calculadora da el mismo valor." if i == 0 else None)

# ---------- 2. Número de referencia con π ≈ 3,14 ----------
P314 = Q(314, 100)
for i, (lit, tt, r0) in enumerate([("a", "1.84", "1.30"), ("b", "2.14", "1.00"), ("c", "3.54", "0.40"),
                                   ("d", "3.74", "0.60"), ("e", "5.18", "1.10"), ("f", "6.08", "0.20"),
                                   ("g", "10.48", "1.06"), ("h", "8.38", "1.04"),
                                   ("i", "-1.12", "1.12"), ("j", "-1.86", "1.28"),
                                   ("k", "-2.64", "0.50"), ("l", "-4.24", "1.10")]):
    reg(9 + i, f"{FP} 2{lit}",
        r"Encuentra el número de referencia $t_0$ de $t = %s$. Usa $\num{3,14}$ para $\pi$." % N(tt),
        r"$t_0 = %s$." % N(r0),
        lambda tt=sp.Rational(tt), r0=sp.Rational(r0): igual(referencia(tt, P314)[0], r0),
        dificultad=1 if i < 6 else 2)

# ---------- 3. Número de referencia exacto ----------
for i, (lit, tx, tt, r0, r0tx) in enumerate([
        ("a", r"\dfrac{13\pi}{8}", 13 * pi / 8, 3 * pi / 8, None),
        ("b", r"3\pi + \num{0,24}", 3 * pi + Q(24, 100), Q(24, 100), r"\num{0,24}"),
        ("c", r"\dfrac{11\pi}{2}", 11 * pi / 2, pi / 2, None),
        ("d", r"\dfrac{37\pi}{36}", 37 * pi / 36, pi / 36, None),
        ("e", r"\dfrac{3\pi}{2} + \num{0,17}", 3 * pi / 2 + Q(17, 100), pi / 2 - Q(17, 100),
         r"\dfrac{\pi}{2} - \num{0,17}"),
        ("f", r"26\pi", 26 * pi, 0, None),
        ("g", r"\dfrac{40\pi}{3}", 40 * pi / 3, pi / 3, None),
        ("h", r"3\pi - \num{0,24}", 3 * pi - Q(24, 100), Q(24, 100), r"\num{0,24}"),
        ("i", r"-\dfrac{11\pi}{5}", -11 * pi / 5, pi / 5, None),
        ("j", r"\dfrac{3\pi}{2} - \num{0,17}", 3 * pi / 2 - Q(17, 100), pi / 2 - Q(17, 100),
         r"\dfrac{\pi}{2} - \num{0,17}")]):
    reg(21 + i, f"{FP} 3{lit}",
        r"Encuentra el número de referencia de $%s$. Puedes dejar la respuesta en términos de "
        r"$\pi$." % tx,
        r"$t_0 = %s$." % (r0tx or latex_es(r0)),
        lambda tt=tt, r0=r0: igual(referencia(tt, pi)[0], r0), dificultad=2)

# ---------- 4. Valores con π ≈ 3,14 y tabla, comparados con la calculadora ----------
for i, (lit, f, tx, tt, r0, vtab, vcalc) in enumerate([
        ("a", "cos", r"\cos \num{1,42}", 1.42, "1.42", "0.1502", "0.1502"),
        ("b", "sen", r"\sen \num{2,14}", 2.14, "1.00", "0.8415", "0.8423"),
        ("c", "cos", r"\cos(-\num{2,54})", -2.54, "0.60", "-0.8253", "-0.8244"),
        ("d", "sen", r"\sen \num{0,97}", 0.97, "0.97", "0.8249", "0.8249"),
        ("e", "cos", r"\cos \num{3,08}", 3.08, "0.06", "-0.9982", "-0.9981"),
        ("f", "sen", r"\sen(-\num{4,18})", -4.18, "1.04", "0.8624", "0.8616"),
        ("g", "tg", r"\tg \num{1,39}", 1.39, "1.39", "5.4707", "5.4707"),
        ("h", "cot", r"\cot \num{5,62}", 5.62, "0.66", "-1.2885", "-1.2800"),
        ("i", "cot", r"\cot \num{0,08}", 0.08, "0.08", "12.4733", "12.4733"),
        ("j", "tg", r"\tg \num{4,11}", 4.11, "0.97", "1.4592", "1.4542")]):
    igualan = vtab == vcalc
    reg(31 + i, f"{FP} 4{lit}",
        r"Encuentra el valor de $%s$ con su número de referencia, usando $\pi \approx \num{3,14}$ "
        r"y la tabla (o la calculadora para el número de referencia). Compara con el valor que "
        r"da la calculadora directamente." % tx,
        (r"$t_0 = %s$; $%s \approx %s$." % (N(r0), tx, N(vtab)) if igualan else
         r"$t_0 = %s$; con $\pi \approx \num{3,14}$ se obtiene $%s \approx %s$; la calculadora "
         r"da $%s$ (la diferencia viene de aproximar $\pi$)." % (N(r0), tx, N(vtab), N(vcalc))),
        lambda f=f, tt=tt, r0=float(r0), vtab=float(vtab), vcalc=float(vcalc): (
            lambda ref=referencia(sp.Rational(str(tt)), P314): (
                cerca(ref[0], r0, 9),
                cerca(SIGNO[f][ref[1]] * FX[f](float(ref[0])), vtab, 4),
                cerca(FX[f](tt), vcalc, 4)))(),
        dificultad=2)

# ---------- 5. Dos valores de t en [0, 2π] ----------
def dos_valores(f, x):
    """Las dos soluciones en [0, 2π) de f(t) = x, con la función inversa y la simetría del
    cuadrante (se comprueba además que de verdad son soluciones)."""
    if f == "sen":
        a = math.asin(x)
        sols = (a, math.pi - a)
    elif f == "cos":
        a = math.acos(x)
        sols = (a, -a)
    else:
        a = math.atan(x if f == "tg" else 1 / x)
        sols = (a, math.pi + a)
    sols = sorted(v % (2 * math.pi) for v in sols)
    for v in sols:
        assert abs(FX[f](v) - x) < 1e-9
    return sols



for i, (lit, f, x, t1, t2) in enumerate([
        ("a", "cos", "-0.08071", "1.65", "4.63"), ("b", "cot", "1.4007", "0.62", "3.76"),
        ("c", "sen", "0.94898", "1.25", "1.89"), ("d", "sen", "-0.48818", "3.65", "5.77"),
        ("e", "tg", "3.6021", "1.30", "4.44"), ("f", "cos", "0.72484", "0.76", "5.52"),
        ("g", "tg", "4.9131", "1.37", "4.51"), ("h", "cot", "-0.47175", "2.01", "5.15")]):
    reg(41 + i, f"{FP} 5{lit}",
        r"Encuentra dos valores de $t$ entre $0$ y $2\pi$ (a la centésima) para los que "
        r"$%s t = %s$." % (NOM[f], N(x)),
        r"$t \approx %s$ y $t \approx %s$." % (N(t1), N(t2)),
        lambda f=f, x=float(x), t1=float(t1), t2=float(t2): (
            lambda sols=dos_valores(f, x): (cerca(sols[0], t1, 2), cerca(sols[1], t2, 2)))(),
        dificultad=2,
        notas="En el módulo: «tan t = 0,3.6021»; el valor de la tabla es 3,6021 (= tg 1,30)."
        if lit == "e" else None)


# ---------- 6. Ángulo de referencia en grados ----------
def ref_grados(g):
    r = g % 360
    return min(r, abs(180 - r), abs(360 - r))


for i, (lit, g, r0) in enumerate([("a", "136.6", "43.4"), ("b", "375.4", "15.4"),
                                  ("c", "348.7", "11.3"), ("d", "-224.4", "44.4"),
                                  ("e", "218.1", "38.1"), ("f", "-99.8", "80.2")]):
    reg(49 + i, f"{FP} 6{lit}",
        r"Encuentra el ángulo de referencia (en grados) de $%s^\circ$." % N(g),
        r"$\theta_0 = %s^\circ$." % N(r0),
        lambda g=sp.Rational(g), r0=sp.Rational(r0): igual(ref_grados(g), r0))

# ---------- 7. Valores para ángulos en grados ----------
for i, (lit, f, g, v) in enumerate([
        ("a", "sen", "156.1", "0.4051"), ("b", "cos", "138.7", "-0.7513"),
        ("c", "tg", "348.9", "-0.1962"), ("d", "cot", "224.9", "1.0035"),
        ("e", "cos", "-66.1", "0.4051"), ("f", "sen", "487", "0.7986"),
        ("g", "cos", "441.3", "0.1513"), ("h", "sen", "180.2", "-0.0035"),
        ("i", "cot", "-134", "0.9657"), ("j", "tg", "311.6", "-1.1263")]):
    tx = (r"%s(%s^\circ)" if g.startswith("-") else r"%s %s^\circ") % (NOM[f], N(g))
    reg(55 + i, f"{FP} 7{lit}",
        r"Encuentra el valor de $%s$ usando su ángulo de referencia (cuatro decimales)." % tx,
        r"$%s \approx %s$." % (tx, N(v)),
        lambda f=f, g=float(g), v=float(v): (
            cerca(FX[f](rad(g)), v, 4),
            cerca(SIGNO[f][int((g % 360) // 90) + 1] * FX[f](rad(ref_grados(g))), v, 4)),
        notas="En el módulo: «cos 441, 3°»; es 441,3°." if lit == "g" else None)

# ---------- 8. Dos ángulos en [0°, 360°) ----------
for i, (lit, f, x, g1, g2) in enumerate([
        ("a", "sen", "0.3633", "21.3", "158.7"), ("b", "cot", "1.2799", "38.0", "218.0"),
        ("c", "cos", "0.9907", "7.8", "352.2"), ("d", "cos", "-0.9085", "155.3", "204.7"),
        ("e", "tg", "0.4942", "26.3", "206.3"), ("f", "sen", "-0.2045", "191.8", "348.2")]):
    reg(65 + i, f"{FP} 8{lit}",
        r"Encuentra dos valores de $\theta$ entre $0^\circ$ y $360^\circ$ (a la décima) para los "
        r"que $%s\theta = %s$." % (NOM[f], N(x)),
        r"$\theta \approx %s^\circ$ y $\theta \approx %s^\circ$." % (N(g1), N(g2)),
        lambda f=f, x=float(x), g1=float(g1), g2=float(g2): [
            cerca(FX[f](rad(g)), x, 3) for g in (g1, g2)] + [
            cerca(abs(g1 - g2) % 360 != 0, 1, 0)],
        dificultad=2,
        notas="En el módulo: «tan θ = 0,4942 70.»; se quita el «70.» sobrante." if lit == "e" else None)

# ---------- 9. Varios ----------
for i, (lit, f, tx, a, g, v) in enumerate([
        ("a", "cos", r"\cos \num{5,63}", 5.63, False, "0.7942"),
        ("b", "sen", r"\sen \num{10,34}", 10.34, False, "-0.7927"),
        ("c", "sen", r"\sen \num{311,3}^\circ", 311.3, True, "-0.7513"),
        ("d", "tg", r"\tg(-411^\circ)", -411, True, "-1.2349")]):
    reg(71 + i, f"{FP} 9{lit}",
        r"Encuentra el valor de $%s$ (cuatro decimales)." % tx, r"$%s \approx %s$." % (tx, N(v)),
        lambda f=f, a=a, g=g, v=float(v): cerca(FX[f](rad(a) if g else a), v, 4))

# ---------- Prepárate para el ICFES del final del módulo ----------
for i, (lit, f, tx, a, g, v, nota) in enumerate([
        ("a", "sen", r"\sen 411^\circ", 411, True, "0.7771", None),
        ("b", "cos", r"\cos 1312", 1312, False, "0.3756",
         "En el módulo: «cos 1312», sin símbolo de grado; se toma en radianes como está escrito "
         "(si fuera 1312°, el valor sería −0,6157)."),
        ("c", "tg", r"\tg \num{5,77}^\circ", 5.77, True, "0.1010", None),
        ("d", "sen", r"\sen \num{13,12}", 13.12, False, "0.5258", None)]):
    reg(75 + i, f"{FR} 6{lit}", r"Evalúa $%s$ (cuatro decimales)." % tx,
        r"$%s \approx %s$." % (tx, N(v)),
        lambda f=f, a=a, g=g, v=float(v): cerca(FX[f](rad(a) if g else a), v, 4), notas=nota)
