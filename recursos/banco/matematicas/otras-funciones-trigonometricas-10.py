"""Banco de ejercicios — Trigonometría 10° — Tangente, cotangente, secante y cosecante;
definiciones con (a, b, r); identidades y aplicaciones.
Fuente: módulo de Matemáticas 10° de las Guías de Apoyo, Tema 4 («Otras funciones
trigonométricas», Practica lo aprendido) y los problemas 9, 10 y 14 del «Prepárate para el
ICFES» final; se lee en
recursos/matematicas/Guías pedagógicas Matemáticas/markdown/10 - Modulo_Matematicas_Decimo.md
Los problemas 13, 14, 15, 16, 22 y 29 del Tema 4 (rectas: pendiente, ángulo de inclinación,
puntos del plano) están en rectas-inclinacion-10.py (Geometría 10°).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/otras-funciones-trigonometricas-10.py
"""
import math

import sympy as sp
from sympy import Interval, Rational as Q, cos, cot, csc, pi, sec, sin, sqrt, tan

from ejercicios import ejercicio, ejercicio_manual, latex_es

PRE = "otras-funciones-trigonometricas-10"
FP = "módulo 10° (Guías de Apoyo), Tema 4, Otras funciones trigonométricas — Practica lo aprendido"
FR = "módulo 10° (Guías de Apoyo), Resumen del capítulo — Prepárate para el ICFES"
COMUN = dict(tema="tangente, cotangente, secante y cosecante", grados=[10], dba=["matematicas-10-4"])
t = sp.Symbol("t", real=True)
th = sp.Symbol("theta", real=True)
G = pi / 180


def N(x):
    return r"\num{" + str(x).replace(".", ",") + "}"


def igual(a, b):
    assert sp.simplify(a - b) == 0, f"{a} ≠ {b}"


def cierto(cond, msj="no se cumple"):
    assert bool(cond), msj


def cerca(calc, mano, dec):
    assert abs(float(calc) - mano) <= 0.5 * 10 ** -dec + 1e-9, f"calculado {calc}, a mano {mano}"


def identica(a, b):
    """a ≡ b como identidad trigonométrica (se reescribe todo en exponenciales)."""
    d = sp.simplify(sp.trigsimp(a - b))
    if d != 0:
        d = sp.simplify((a - b).rewrite(sp.exp))
    assert d == 0, f"{a} ≢ {b}"


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


NOM = {"tg": r"\tg", "cot": r"\cot", "sec": r"\sec", "csc": r"\csc", "sen": r"\sen", "cos": r"\cos"}
FX = {"tg": lambda s, c: s / c, "cot": lambda s, c: c / s, "sec": lambda s, c: 1 / c,
      "csc": lambda s, c: 1 / s, "sen": lambda s, c: s, "cos": lambda s, c: c}

# ---------- 1–4. A partir de seno y coseno ----------
for base, (s, c, stx, ctx, vals) in enumerate([
        (Q(4, 5), -Q(3, 5), r"\dfrac{4}{5}", r"-\dfrac{3}{5}",
         [("tg", -Q(4, 3)), ("cot", -Q(3, 4)), ("sec", -Q(5, 3)), ("csc", Q(5, 4))]),
        (-1 / sqrt(5), 2 / sqrt(5), r"-\dfrac{1}{\sqrt{5}}", r"\dfrac{2}{\sqrt{5}}",
         [("tg", -Q(1, 2)), ("cot", -2), ("sec", sqrt(5) / 2), ("csc", -sqrt(5))])]):
    for j, (f, v) in enumerate(vals):
        reg(1 + 4 * base + j, f"{FP} {base + 1}{'abcd'[j]}",
            r"Si $\sen t = %s$ y $\cos t = %s$, evalúa $%s t$." % (stx, ctx, NOM[f]),
            r"$%s t = %s$." % (NOM[f], latex_es(v)),
            lambda f=f, s=s, c=c, v=v: (igual(s**2 + c**2, 1), igual(FX[f](s, c), v)),
            notas="En el módulo el literal d dice «csc» sin la t." if (base, j) == (0, 3) else None)
reg(9, f"{FP} 3",
    r"El lado final de un ángulo $\theta$ en posición estándar corta al círculo unitario en "
    r"$\left(-\dfrac{2}{3}, \dfrac{\sqrt{5}}{3}\right)$. Encuentra $\tg\theta$ y $\csc\theta$.",
    r"$\tg\theta = \dfrac{\sqrt{5}/3}{-2/3} = -\dfrac{\sqrt{5}}{2}$ y $\csc\theta = "
    r"\dfrac{3}{\sqrt{5}} = \dfrac{3\sqrt{5}}{5}$.",
    lambda: (igual(Q(4, 9) + Q(5, 9), 1), igual((sqrt(5) / 3) / (-Q(2, 3)), -sqrt(5) / 2),
             igual(1 / (sqrt(5) / 3), 3 * sqrt(5) / 5)),
    notas="En el módulo: «para el ángulo θ de la con coordenadas…»; se completa la redacción.")
reg(10, f"{FP} 4",
    r"El lado final de un ángulo $\theta$ en posición estándar corta al círculo unitario en "
    r"$\left(-\dfrac{3}{5}, -\dfrac{4}{5}\right)$. Encuentra $\cot\theta$ y $\sec\theta$.",
    r"$\cot\theta = \dfrac{-3/5}{-4/5} = \dfrac{3}{4}$ y $\sec\theta = -\dfrac{5}{3}$.",
    lambda: (igual(Q(9, 25) + Q(16, 25), 1), igual(FX["cot"](-Q(4, 5), -Q(3, 5)), Q(3, 4)),
             igual(FX["sec"](-Q(4, 5), -Q(3, 5)), -Q(5, 3))))

# ---------- 5. Valores exactos ----------
SYM = {"tg": tan, "cot": cot, "sec": sec, "csc": csc, "sen": sin, "cos": cos}
filas5 = [("a", "tg", pi / 6, None, sqrt(3) / 3), ("b", "cot", pi / 6, None, sqrt(3)),
          ("c", "sec", pi / 6, None, 2 * sqrt(3) / 3), ("d", "csc", pi / 6, None, 2),
          ("e", "cot", pi / 4, None, 1), ("f", "sec", pi / 4, None, sqrt(2)),
          ("g", "csc", pi / 3, None, 2 * sqrt(3) / 3), ("h", "sec", pi / 3, None, 2),
          ("i", "cos", 4 * pi / 3, None, -Q(1, 2)), ("j", "sen", 4 * pi / 3, None, -sqrt(3) / 2),
          ("k", "tg", 4 * pi / 3, None, sqrt(3)), ("l", "sec", 4 * pi / 3, None, -2),
          ("m", "tg", pi, None, 0), ("n", "sec", pi, None, -1),
          ("o", "tg", None, 330, -sqrt(3) / 3), ("p", "cot", None, 120, -sqrt(3) / 3),
          ("q", "sec", None, 600, -2), ("r", "csc", None, -150, -2)]
for i, (lit, f, r, g, v) in enumerate(filas5):
    arg = r"\left(%s\right)" % latex_es(r) if g is None else (
        r"(%d^\circ)" % g if g < 0 else r" %d^\circ" % g)
    reg(11 + i, f"{FP} 5{lit}",
        r"Con los valores de seno y coseno de los ángulos especiales, encuentra el valor exacto de "
        r"$%s%s$." % (NOM[f], arg),
        r"$%s%s = %s$." % (NOM[f], arg, latex_es(v)),
        lambda f=f, r=r, g=g, v=v: igual(SYM[f](r if g is None else g * G), v),
        dificultad=1 if i < 14 else 2)

# ---------- 6–7. Dónde no están definidas / dónde valen 1, en [0, 4π] ----------
CUATRO = Interval(0, 4 * pi)
for i, (lit, f, den, sols) in enumerate([
        ("a", "sec", cos(t), [pi / 2, 3 * pi / 2, 5 * pi / 2, 7 * pi / 2]),
        ("b", "tg", cos(t), [pi / 2, 3 * pi / 2, 5 * pi / 2, 7 * pi / 2]),
        ("c", "csc", sin(t), [0, pi, 2 * pi, 3 * pi, 4 * pi]),
        ("d", "cot", sin(t), [0, pi, 2 * pi, 3 * pi, 4 * pi])]):
    reg(29 + i, f"{FP} 6{lit}",
        r"¿Para qué valores de $t$ en $0 \le t \le 4\pi$ no está definida $%s t$?" % NOM[f],
        r"Donde se anula su denominador: $t = %s$." % ", ".join(latex_es(s) for s in sols),
        lambda den=den, sols=sols: cierto(sp.solveset(den, t, CUATRO) == sp.FiniteSet(*sols)))
for i, (lit, f, ec, sols) in enumerate([
        ("a", "sec", cos(t) - 1, [0, 2 * pi, 4 * pi]),
        ("b", "tg", sin(t) - cos(t), [pi / 4, 5 * pi / 4, 9 * pi / 4, 13 * pi / 4]),
        ("c", "csc", sin(t) - 1, [pi / 2, 5 * pi / 2]),
        ("d", "cot", cos(t) - sin(t), [pi / 4, 5 * pi / 4, 9 * pi / 4, 13 * pi / 4])]):
    reg(33 + i, f"{FP} 7{lit}",
        r"¿Para qué valores de $t$ en $0 \le t \le 4\pi$ se cumple $%s t = 1$?" % NOM[f],
        r"$t = %s$." % ", ".join(latex_es(s) for s in sols),
        lambda f=f, ec=ec, sols=sols: (cierto(sp.solveset(ec, t, CUATRO) == sp.FiniteSet(*sols)),
                                       [igual(SYM[f](s), 1) for s in sols]),
        dificultad=2)

# ---------- 8–12. Definiciones con (a, b, r) ----------
for i, (lit, a, b, vs) in enumerate([
        ("a", 5, -12, (-Q(12, 13), -Q(12, 5), Q(13, 5))),
        ("b", 7, 24, (Q(24, 25), Q(24, 7), Q(25, 7))),
        ("c", -1, -2, (-2 * sqrt(5) / 5, 2, -sqrt(5))),
        ("d", -3, 2, (2 * sqrt(13) / 13, -Q(2, 3), -sqrt(13) / 3))]):
    reg(37 + i, f"{FP} 8{lit}",
        r"El punto $(%d, %d)$ está en el lado final de un ángulo $\theta$ en posición estándar. "
        r"Encuentra $\sen\theta$, $\tg\theta$ y $\sec\theta$." % (a, b),
        r"$r = %s$; $\sen\theta = %s$, $\tg\theta = %s$ y $\sec\theta = %s$."
        % (latex_es(sqrt(a**2 + b**2)), latex_es(vs[0]), latex_es(vs[1]), latex_es(vs[2])),
        lambda a=a, b=b, vs=vs: (lambda th0=sp.atan2(b, a): (
            igual(sin(th0), vs[0]), igual(tan(th0), vs[1]), igual(sec(th0), vs[2])))())
reg(41, f"{FP} 9",
    r"Si $\tg\theta = \dfrac{3}{4}$ y $\theta$ está en el primer cuadrante, encuentra "
    r"$\sen\theta$ y $\sec\theta$. Sugerencia: el punto $(4, 3)$ está en el lado final de $\theta$.",
    r"$r = 5$: $\sen\theta = \dfrac{3}{5}$ y $\sec\theta = \dfrac{5}{4}$.",
    lambda: (igual(sin(sp.atan(Q(3, 4))), Q(3, 5)), igual(sec(sp.atan(Q(3, 4))), Q(5, 4))))
reg(42, f"{FP} 10",
    r"Si $\tg\theta = \dfrac{3}{4}$ y $\theta$ está en el tercer cuadrante, encuentra "
    r"$\cos\theta$ y $\csc\theta$. Sugerencia: el punto $(-4, -3)$ está en el lado final de $\theta$.",
    r"$r = 5$: $\cos\theta = -\dfrac{4}{5}$ y $\csc\theta = -\dfrac{5}{3}$.",
    lambda: (igual(tan(sp.atan2(-3, -4)), Q(3, 4)), igual(cos(sp.atan2(-3, -4)), -Q(4, 5)),
             igual(csc(sp.atan2(-3, -4)), -Q(5, 3))))
reg(43, f"{FP} 11",
    r"Si $\sen\theta = \dfrac{5}{13}$ y $\theta$ está en el segundo cuadrante, encuentra "
    r"$\cos\theta$ y $\cot\theta$. Sugerencia: un punto con coordenada $y$ igual a $5$ y $r = 13$ "
    r"está en el lado final de $\theta$; su coordenada $x$ debe ser $-12$.",
    r"$\cos\theta = -\dfrac{12}{13}$ y $\cot\theta = -\dfrac{12}{5}$.",
    lambda: (igual(cos(pi - sp.asin(Q(5, 13))), -Q(12, 13)), igual(cot(pi - sp.asin(Q(5, 13))), -Q(12, 5))),
    notas="En el módulo: «coordenada^ igual a 5»; es la coordenada y.")
reg(44, f"{FP} 12",
    r"Si $\cos\theta = \dfrac{4}{5}$ y $\sen\theta < 0$, encuentra $\tg\theta$.",
    r"$\theta$ está en el cuadrante IV: $\sen\theta = -\dfrac{3}{5}$ y $\tg\theta = -\dfrac{3}{4}$.",
    lambda: igual(tan(-sp.acos(Q(4, 5))), -Q(3, 4)))

# ---------- 17. Evaluar sin calculadora ----------
for i, (lit, f, r, g, v, vtx) in enumerate([
        ("a", "sec", 7 * pi / 6, None, -2 * sqrt(3) / 3, None), ("b", "cot", 11 * pi / 4, None, -1, None),
        ("c", "tg", -2 * pi / 3, None, sqrt(3), None), ("d", "csc", None, 570, -2, None),
        ("e", "csc", 3 * pi / 4, None, sqrt(2), None),
        ("f", "tg", None, Q(180045, 1000), pi / 4000, r"\tg \num{0,045}^\circ \approx "
                                                      r"\dfrac{\pi}{4000} \approx \num{0,000785}")]):
    arg = (r"\left(%s\right)" % latex_es(r)) if g is None else (
        r"(\num{180,045}^\circ)" if lit == "f" else r"(%d^\circ)" % g)
    reg(45 + i, f"{FP} 17{lit}",
        r"Evalúa sin calculadora $%s%s$." % (NOM[f], arg),
        r"$%s%s = %s$." % (NOM[f], arg, vtx or latex_es(v)),
        (lambda: cerca(math.tan(math.radians(180.045)), 0.000785, 6)) if lit == "f" else
        (lambda f=f, r=r, g=g, v=v: igual(SYM[f](r if g is None else g * G), v)),
        dificultad=3 if lit == "f" else 2,
        notas="Para 180,045° se espera tg(180° + x) = tg x ≈ x (en radianes) para x pequeño."
        if lit == "f" else None)

# ---------- 18. Calcular (calculadora; el argumento exterior en radianes) ----------
NOTA18 = ("Convención: el argumento exterior es un número real (radianes); el grado solo se "
          "usa donde el módulo lo escribe.")
for i, (lit, tx, fn, v, dec) in enumerate([
        ("a", r"\tg(\sen \num{2,4})", lambda: math.tan(math.sin(2.4)), "0.8012", 4),
        ("b", r"\sec^2(\tg \num{91,2}^\circ)",
         lambda: 1 / math.cos(math.tan(math.radians(91.2))) ** 2, "1.5003", 4),
        ("c", r"\cot(\tg \num{1,49})", lambda: 1 / math.tan(math.tan(1.49)), "-4.5462", 4),
        ("d", r"\csc(\sen \num{11,8}^\circ)", lambda: 1 / math.sin(math.sin(math.radians(11.8))),
         "4.9243", 4),
        ("f", r"\tg[\tg(\tg \num{1,5})]", lambda: math.tan(math.tan(math.tan(1.5))), "-0.3224", 4)]):
    reg(51 + i, f"{FP} 18{lit}", r"Calcula con la calculadora $%s$ (cuatro decimales)." % tx,
        r"$%s \approx %s$." % (tx, N(v)), lambda fn=fn, v=float(v), dec=dec: cerca(fn(), v, dec),
        dificultad=2, notas=NOTA18)
reg(56, f"{FP} 18e", r"Calcula $\csc(\tg \pi)$.",
    r"No está definido: $\tg\pi = 0$ y $\csc 0 = \dfrac{1}{\sen 0}$ no existe.",
    lambda: (igual(tan(pi), 0), cierto(csc(sp.Integer(0)) is sp.zoo)), tipo="conceptual",
    dificultad=2)

# ---------- 19. csc t = 25/24, cos t < 0 ----------
T19 = pi - sp.asin(Q(24, 25))
for i, (lit, tx, e, v) in enumerate([
        ("a", r"\sen t", sin(T19), Q(24, 25)), ("b", r"\cos t", cos(T19), -Q(7, 25)),
        ("c", r"\tg t", tan(T19), -Q(24, 7)),
        ("d", r"\sec\left(\dfrac{\pi}{2} - t\right)", sec(pi / 2 - T19), Q(25, 24)),
        ("e", r"\cot\left(\dfrac{\pi}{2} - t\right)", cot(pi / 2 - T19), -Q(24, 7)),
        ("f", r"\csc\left(\dfrac{\pi}{2} - t\right)", csc(pi / 2 - T19), -Q(25, 7))]):
    reg(57 + i, f"{FP} 19{lit}",
        r"Si $\csc t = \dfrac{25}{24}$ y $\cos t < 0$, encuentra $%s$." % tx,
        r"$%s = %s$." % (tx, latex_es(v)),
        lambda e=e, v=v: (igual(csc(T19), Q(25, 24)), cierto(cos(T19) < 0), igual(e, v)),
        dificultad=2)

# ---------- 20. Demostraciones ----------
for i, (lit, tx, resp) in enumerate([
        ("a", r"\tg(-t) = -\tg t",
         r"$\tg(-t) = \dfrac{\sen(-t)}{\cos(-t)} = \dfrac{-\sen t}{\cos t} = -\tg t$."),
        ("b", r"\sec(-t) = \sec t", r"$\sec(-t) = \dfrac{1}{\cos(-t)} = \dfrac{1}{\cos t} = \sec t$."),
        ("c", r"\csc(-t) = -\csc t",
         r"$\csc(-t) = \dfrac{1}{\sen(-t)} = \dfrac{1}{-\sen t} = -\csc t$.")]):
    manual(63 + i, f"{FP} 20{lit}", r"Prueba que $%s$ es una identidad." % tx,
           resp + r" Se usa que el seno es impar y el coseno es par.")

for i, (lit, tx, ec, sols) in enumerate([
        ("a", r"\tg t = -1", sin(t) + cos(t), [3 * pi / 4, 7 * pi / 4]),
        ("b", r"\sec t = \sqrt{2}", cos(t) - 1 / sqrt(2), [pi / 4, 7 * pi / 4]),
        ("c", r"|\csc t| = 1", sin(t) ** 2 - 1, [pi / 2, 3 * pi / 2])]):
    reg(66 + i, f"{FP} 21{lit}",
        r"Encuentra los dos valores positivos más pequeños de $t$ que cumplen $%s$." % tx,
        r"$t = %s$ y $t = %s$." % (latex_es(sols[0]), latex_es(sols[1])),
        lambda ec=ec, sols=sols: cierto(sorted(sp.solveset(ec, t, Interval.open(0, 2 * pi)),
                                               key=float) == sols),
        dificultad=2)

# ---------- 23. Simplificar ----------
for i, (lit, tx, e, v, vtx) in enumerate([
        ("a", r"\dfrac{\sec\theta\csc\theta}{\tg\theta + \cot\theta}",
         sec(th) * csc(th) / (tan(th) + cot(th)), sp.Integer(1), "1"),
        ("b", r"\tg\theta\,(\cos\theta - \csc\theta)", tan(th) * (cos(th) - csc(th)),
         sin(th) - 1 / cos(th), r"\sen\theta - \dfrac{1}{\cos\theta}"),
        ("c", r"\dfrac{(1 + \tg\theta)^2}{\sec^2\theta}", (1 + tan(th)) ** 2 / sec(th) ** 2,
         (cos(th) + sin(th)) ** 2, r"(\cos\theta + \sen\theta)^2 = 1 + 2\sen\theta\cos\theta"),
        ("d", r"\dfrac{\sec\theta\cot\theta}{\sec^2\theta - \tg^2\theta}",
         sec(th) * cot(th) / (sec(th) ** 2 - tan(th) ** 2), 1 / sin(th), r"\dfrac{1}{\sen\theta}"),
        ("e", r"\dfrac{\cot\theta - \tg\theta}{\csc\theta - \sec\theta}",
         (cot(th) - tan(th)) / (csc(th) - sec(th)), cos(th) + sin(th), r"\cos\theta + \sen\theta"),
        ("f", r"\tg^4\theta - \sec^4\theta", tan(th) ** 4 - sec(th) ** 4,
         -(1 + sin(th) ** 2) / cos(th) ** 2, r"-\dfrac{1 + \sen^2\theta}{\cos^2\theta}")]):
    reg(69 + i, f"{FP} 23{lit}",
        r"Escribe $%s$ en términos de senos y cosenos y simplifica." % tx,
        r"$%s = %s$ (donde la expresión está definida)." % (tx, vtx),
        lambda e=e, v=v: identica(e, v), dificultad=2 if lit in "abc" else 3)
s = sp.Symbol("s", positive=True)
reg(75, f"{FP} 24",
    r"Sea $\theta$ un ángulo del primer cuadrante. Expresa las otras cinco funciones "
    r"trigonométricas solo en términos de $\sen\theta$.",
    r"$\cos\theta = \sqrt{1 - \sen^2\theta}$, $\tg\theta = \dfrac{\sen\theta}{\sqrt{1 - "
    r"\sen^2\theta}}$, $\cot\theta = \dfrac{\sqrt{1 - \sen^2\theta}}{\sen\theta}$, "
    r"$\sec\theta = \dfrac{1}{\sqrt{1 - \sen^2\theta}}$ y $\csc\theta = \dfrac{1}{\sen\theta}$.",
    lambda: [igual(f(sp.asin(s)), v) for f, v in [
        (cos, sqrt(1 - s**2)), (tan, s / sqrt(1 - s**2)), (cot, sqrt(1 - s**2) / s),
        (sec, 1 / sqrt(1 - s**2)), (csc, 1 / s)]],
    tipo="calculo", dificultad=2)
manual(76, f"{FP} 25",
       r"Prueba que $|\sec t| \ge 1$ y $|\csc t| \ge 1$ para todo $t$ en el que estén definidas.",
       r"Como $0 < |\cos t| \le 1$ donde la secante está definida, $|\sec t| = \dfrac{1}{|\cos t|}"
       r" \ge 1$. Del mismo modo, $0 < |\sen t| \le 1$ da $|\csc t| = \dfrac{1}{|\sen t|} \ge 1$.")
reg(77, f"{FP} 26",
    r"Si $\tg\theta = \dfrac{5}{12}$ y $\sen\theta < 0$, evalúa $\cos^2\theta - \sen^2\theta$.",
    r"$\theta$ está en el cuadrante III: $\sen\theta = -\dfrac{5}{13}$, $\cos\theta = "
    r"-\dfrac{12}{13}$ y $\cos^2\theta - \sen^2\theta = \dfrac{144 - 25}{169} = \dfrac{119}{169}$.",
    lambda: (lambda a=sp.atan2(-5, -12): (igual(tan(a), Q(5, 12)), cierto(sin(a) < 0),
                                          igual(cos(a) ** 2 - sin(a) ** 2, Q(119, 169))))(),
    dificultad=2, notas="En el módulo: «sen θ < O» (letra O); es cero.")

# ---------- 27–32. Aplicaciones ----------
reg(78, f"{FP} 27",
    r"Una rueda de radio $5$ centrada en el origen gira en sentido contrario a las manecillas "
    r"del reloj a $1$ radián por segundo. En $t = 0$ una mancha de barro del borde está en "
    r"$(5, 0)$. ¿Cuáles son las coordenadas de la mancha en el instante $t$?",
    r"$(5\cos t, 5\sen t)$.",
    lambda: (igual(5 * cos(0), 5), igual(5 * sin(0), 0), igual((5 * cos(t)) ** 2 + (5 * sin(t)) ** 2, 25),
             igual(sp.diff(sp.atan2(5 * sin(t), 5 * cos(t)), t), 1)),
    tipo="contexto", dificultad=2)
reg(79, f"{FP} 28",
    r"En $t = \dfrac{2\pi}{3}$ la mancha del problema anterior (rueda de radio $5$, en $(5\cos t, "
    r"5\sen t)$) se desprende y sale volando por la recta tangente. ¿Dónde cruza el eje $x$?",
    r"Se desprende en $\left(-\dfrac{5}{2}, \dfrac{5\sqrt{3}}{2}\right)$; la tangente es "
    r"perpendicular al radio: $x\cos\frac{2\pi}{3} + y\sen\frac{2\pi}{3} = 5$. Con $y = 0$: "
    r"$x = \dfrac{5}{\cos\frac{2\pi}{3}} = -10$. Cruza el eje $x$ en $(-10, 0)$.",
    lambda: (lambda P=sp.Point(5 * cos(2 * pi / 3), 5 * sin(2 * pi / 3)):
             cierto(sp.Line(P, P + sp.Point(-sin(2 * pi / 3), cos(2 * pi / 3)))
                    .intersection(sp.Line((0, 0), (1, 0))) == [sp.Point(-10, 0)]))(),
    tipo="contexto", dificultad=3)
reg(80, f"{FP} 30",
    r"Desde un avión que está a $h$ millas sobre la superficie de la Tierra (esfera de $3960$ "
    r"millas de radio) se ve una luz en el horizonte a $d$ millas de distancia. Si el ángulo de "
    r"depresión de la luz mide $\num{2,1}^\circ$, halla $d$ y $h$.",
    r"La visual es tangente a la Tierra y el ángulo en el centro de la Tierra también mide "
    r"$\num{2,1}^\circ$: $d = 3960 \tg \num{2,1}^\circ \approx 145$ millas y $h = "
    r"\dfrac{3960}{\cos \num{2,1}^\circ} - 3960 \approx \num{2,66}$ millas.",
    lambda: (lambda H=3960 / math.cos(math.radians(2.1)) - 3960: (
        cerca(H, 2.66, 2), cerca(math.sqrt((3960 + H) ** 2 - 3960 ** 2), 145, 0)))(),
    tipo="contexto", dificultad=3, notas="En el módulo: «2.1»»; es 2,1°.")


def banda_abierta(r, R, D):
    """Longitud de una banda abierta, sumando tramos rectos y arcos de contacto medidos con
    los puntos de tangencia calculados con vectores."""
    c = (R - r) / D                      # coseno del ángulo del radio de tangencia con el eje
    n = (c, math.sqrt(1 - c * c))        # normal unitaria de la tangente exterior
    T1 = (R * n[0], R * n[1])
    T2 = (D + r * n[0], r * n[1])
    recta = math.dist(T1, T2)
    ang = math.atan2(n[1], n[0])         # posición angular de los puntos de tangencia
    return 2 * recta + R * (2 * math.pi - 2 * ang) + r * 2 * ang


reg(81, f"{FP} 31",
    r"Una rueda de $20$ cm de radio mueve otra de $50$ cm de radio por medio de una banda que "
    r"las rodea (sin cruzarse). ¿Qué longitud tiene la banda si los centros están a $100$ cm?",
    r"Si $\cos\varphi = \dfrac{50 - 20}{100} = \num{0,3}$, cada tramo recto mide $\sqrt{100^2 - "
    r"30^2} = \sqrt{9100}$, la banda abraza $2(\pi - \varphi)$ rad de la rueda grande y $2\varphi$ "
    r"de la pequeña: $L = 2\sqrt{9100} + 100(\pi - \varphi) + 40\varphi \approx 429$ cm.",
    lambda: (cerca(banda_abierta(20, 50, 100), 429, 0),
             cerca(2 * math.sqrt(9100) + 100 * (math.pi - math.acos(0.3)) + 40 * math.acos(0.3),
                   banda_abierta(20, 50, 100), 9)),
    tipo="contexto", dificultad=3)
a_, r_, R_ = sp.symbols("alpha r R", positive=True)


def banda_cruzada(r, R, alfa):
    """Banda cruzada: se ubican los centros con sen α = (R + r)/D, se calculan los puntos de
    tangencia y se miden tramos, arcos y el ángulo de cruce."""
    D = (R + r) / math.sin(alfa)
    nx = (R + r) / D
    n = (nx, math.sqrt(1 - nx * nx))
    T1 = (R * n[0], R * n[1])
    T2 = (D - r * n[0], -r * n[1])
    tramo = math.dist(T1, T2)
    cruce = 2 * math.atan2(abs(T2[1] - T1[1]), T2[0] - T1[0])
    arco = 2 * math.pi - 2 * math.acos(nx)
    return 2 * tramo + (R + r) * arco, cruce


reg(82, f"{FP} 32",
    r"Una banda cruzada rodea dos ruedas de radios $r$ y $R$, y sus dos tramos rectos se cortan "
    r"formando un ángulo $2\alpha$. Expresa la longitud $L$ de la banda en términos de $r$, $R$ "
    r"y $\alpha$.",
    r"Cada tramo recto forma el ángulo $\alpha$ con la recta de los centros y mide "
    r"$(R + r)\cot\alpha$; la banda abraza en cada rueda un arco de $\pi + 2\alpha$ radianes: "
    r"$L = 2(R + r)\cot\alpha + (R + r)(\pi + 2\alpha)$.",
    lambda: [(lambda Lc=banda_cruzada(r, R, al): (
        cerca(Lc[1], 2 * al, 9),
        cerca(Lc[0], 2 * (R + r) / math.tan(al) + (R + r) * (math.pi + 2 * al), 9)))()
        for r, R, al in [(1, 3, 0.4), (2, 5, 0.9), (10, 10, 0.2)]],
    tipo="contexto", dificultad=3)

# ---------- Prepárate para el ICFES del final del módulo ----------
reg(83, f"{FR} 9a",
    r"El punto $(-5, -12)$ está en el lado final de un ángulo $\theta$ en posición estándar. "
    r"Encuentra $\cot\theta$.", r"$r = 13$; $\cot\theta = \dfrac{-5}{-12} = \dfrac{5}{12}$.",
    lambda: igual(cot(sp.atan2(-12, -5)), Q(5, 12)))
reg(84, f"{FR} 9b",
    r"El punto $(-5, -12)$ está en el lado final de un ángulo $\theta$ en posición estándar. "
    r"Encuentra $\sec\theta$.", r"$r = 13$; $\sec\theta = \dfrac{13}{-5} = -\dfrac{13}{5}$.",
    lambda: igual(sec(sp.atan2(-12, -5)), -Q(13, 5)))
reg(85, f"{FR} 10",
    r"Si $\sen\theta = \dfrac{2}{3}$ y $\theta$ está en el segundo cuadrante, encuentra "
    r"$\tg\theta$.",
    r"$\cos\theta = -\dfrac{\sqrt{5}}{3}$, así que $\tg\theta = -\dfrac{2}{\sqrt{5}} = "
    r"-\dfrac{2\sqrt{5}}{5}$.",
    lambda: igual(tan(pi - sp.asin(Q(2, 3))), -2 * sqrt(5) / 5), dificultad=2)
manual(86, f"{FR} 14",
       r"Usando que el seno es impar y el coseno es par, prueba que la cotangente es impar.",
       r"$\cot(-t) = \dfrac{\cos(-t)}{\sen(-t)} = \dfrac{\cos t}{-\sen t} = -\cot t$ para todo "
       r"$t$ con $\sen t \ne 0$.")
