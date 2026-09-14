"""Banco de ejercicios — Trigonometría 10° — Gráficas de las funciones trigonométricas:
dominio, rango, periodo, amplitud, asíntotas; modelos periódicos.
Fuente: módulo de Matemáticas 10° de las Guías de Apoyo, Tema 5 («Gráficas de las funciones
trigonométricas», Practica lo aprendido) y los problemas 11, 12 y 13 del «Prepárate para el
ICFES» final; se lee en
recursos/matematicas/Guías pedagógicas Matemáticas/markdown/10 - Modulo_Matematicas_Decimo.md
Los ejercicios que solo piden dibujar son manuales: la respuesta modelo describe la gráfica.
Donde se pide «determina … y dibuja», la parte numérica se verifica y el dibujo lo revisa la
docente.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/graficas-trigonometricas-10.py
"""
import math

import sympy as sp
from sympy import Interval, Rational as Q, S, cos, cot, csc, oo, pi, sec, sin, tan

from ejercicios import ejercicio, ejercicio_manual, latex_es

PRE = "graficas-trigonometricas-10"
FP = "módulo 10° (Guías de Apoyo), Tema 5, Gráficas de las funciones trigonométricas — Practica lo aprendido"
FR = "módulo 10° (Guías de Apoyo), Resumen del capítulo — Prepárate para el ICFES"
COMUN = dict(tema="gráficas de funciones trigonométricas", grados=[10], dba=["matematicas-10-4"])
t = sp.Symbol("t", real=True)
k = sp.Symbol("k", integer=True)


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


def manual(n, fuente, enunciado, respuesta, tipo="conceptual", dificultad=2, notas=None):
    ejercicio_manual(**meta(n, fuente, enunciado, respuesta, tipo, dificultad, notas))


def amplitud_periodo(expr):
    """Periodo con sympy.periodicity y amplitud como (máx − mín)/2 en un periodo."""
    p = sp.periodicity(expr, t)
    rango = sp.calculus.util.function_range(expr, t, Interval(0, p))
    return (rango.sup - rango.inf) / 2, p


RANGO_SEC = sp.Union(Interval(-oo, -1), Interval(1, oo))

# ---------- 1–12. Propiedades ----------
manual(1, f"{FP} 1", r"Haz una tabla de valores y dibuja la gráfica de $y = \cos t$.",
       r"Tabla con $t = 0, \frac{\pi}{6}, \frac{\pi}{4}, \frac{\pi}{3}, \frac{\pi}{2}, \dots, "
       r"2\pi$: $y = 1, \frac{\sqrt{3}}{2}, \frac{\sqrt{2}}{2}, \frac{1}{2}, 0, \dots, 1$. La "
       r"gráfica es una onda que empieza en $(0, 1)$, corta el eje en $\frac{\pi}{2}$, baja a "
       r"$-1$ en $\pi$, vuelve a cortar en $\frac{3\pi}{2}$ y regresa a $1$ en $2\pi$; se repite "
       r"con periodo $2\pi$ y es simétrica respecto al eje $y$.", dificultad=1)
reg(2, f"{FP} 2", r"¿Cuáles números reales forman el dominio del coseno? ¿Y su rango?",
    r"Dominio: $\mathbb{R}$; rango: $[-1, 1]$.",
    lambda: (cierto(sp.calculus.util.continuous_domain(cos(t), t, S.Reals) == S.Reals),
             cierto(sp.calculus.util.function_range(cos(t), t, S.Reals) == Interval(-1, 1))),
    tipo="conceptual")
manual(3, f"{FP} 3",
       r"Dibuja la gráfica de $y = \cot t$ para $-2\pi \le t \le 2\pi$; muestra las asíntotas.",
       r"Asíntotas verticales en $t = -2\pi, -\pi, 0, \pi, 2\pi$. En cada intervalo entre dos "
       r"asíntotas la curva baja de $+\infty$ a $-\infty$, cortando el eje en $t = "
       r"-\frac{3\pi}{2}, -\frac{\pi}{2}, \frac{\pi}{2}, \frac{3\pi}{2}$, y pasa por los puntos "
       r"de altura $\pm 1$ en $\frac{\pi}{4} + k\frac{\pi}{2}$.")
reg(4, f"{FP} 4", r"¿Qué números reales forman el dominio de la cotangente? ¿Y su rango?",
    r"Dominio: todos los reales excepto $t = k\pi$ ($k$ entero); rango: $\mathbb{R}$.",
    lambda: (cierto(sp.solveset(sin(t), t, Interval.Ropen(0, 2 * pi)) == sp.FiniteSet(0, pi)),
             igual(sp.periodicity(sin(t), t), 2 * pi),
             cierto(sp.limit(cot(t), t, 0, "+") == oo), cierto(sp.limit(cot(t), t, pi, "-") == -oo),
             igual(sp.diff(cot(t), t) + csc(t) ** 2, 0)),
    tipo="conceptual")
manual(5, f"{FP} 5",
       r"Usando el hecho correspondiente del coseno, demuestra algebraicamente que "
       r"$\sec(t + 2\pi) = \sec t$.",
       r"$\sec(t + 2\pi) = \dfrac{1}{\cos(t + 2\pi)} = \dfrac{1}{\cos t} = \sec t$, porque el "
       r"coseno tiene periodo $2\pi$.", tipo="argumentacion", dificultad=1)
manual(6, f"{FP} 6", r"Dibuja la gráfica de $y = \csc t$.",
       r"Se dibuja $y = \sen t$ y se toman recíprocos: asíntotas verticales en $t = k\pi$; ramas "
       r"en forma de U con mínimo $1$ en $t = \frac{\pi}{2} + 2k\pi$ (donde $\sen t > 0$) y ramas "
       r"en forma de U invertida con máximo $-1$ en $t = \frac{3\pi}{2} + 2k\pi$. Periodo $2\pi$; "
       r"ningún punto entre $-1$ y $1$.")
reg(7, f"{FP} 7", r"¿Cuál es el dominio de la secante? ¿Y su rango?",
    r"Dominio: todos los reales excepto $t = \frac{\pi}{2} + k\pi$; rango: "
    r"$(-\infty, -1] \cup [1, \infty)$.",
    lambda: (cierto(sp.solveset(cos(t), t, Interval.Ropen(0, 2 * pi)) == sp.FiniteSet(pi / 2, 3 * pi / 2)),
             cierto(sp.imageset(sp.Lambda(t, 1 / t), sp.Union(Interval.Ropen(-1, 0), Interval.Lopen(0, 1)))
                    == RANGO_SEC)),
    tipo="conceptual")
reg(8, f"{FP} 8", r"¿Cuál es el dominio de la cosecante? ¿Y su rango?",
    r"Dominio: todos los reales excepto $t = k\pi$; rango: $(-\infty, -1] \cup [1, \infty)$.",
    lambda: (cierto(sp.solveset(sin(t), t, Interval.Ropen(0, 2 * pi)) == sp.FiniteSet(0, pi)),
             cierto(sp.calculus.util.function_range(sin(t), t, S.Reals) == Interval(-1, 1)),
             cierto(sp.imageset(sp.Lambda(t, 1 / t), sp.Union(Interval.Ropen(-1, 0), Interval.Lopen(0, 1)))
                    == RANGO_SEC)),
    tipo="conceptual")
reg(9, f"{FP} 9", r"¿Cuál es el periodo de la cotangente? ¿Y el de la secante?",
    r"Cotangente: $\pi$; secante: $2\pi$.",
    lambda: (igual(sp.periodicity(cot(t), t), pi), igual(sp.periodicity(sec(t), t), 2 * pi)),
    tipo="conceptual")
reg(10, f"{FP} 10", r"En el intervalo $-2\pi \le t \le 2\pi$, ¿dónde es creciente la cotangente?",
    r"En ninguna parte: en cada intervalo donde está definida ($-2\pi < t < -\pi$, $-\pi < t < 0$, "
    r"$0 < t < \pi$, $\pi < t < 2\pi$) es decreciente.",
    lambda: igual(sp.diff(cot(t), t) + csc(t) ** 2, 0), tipo="conceptual", dificultad=2,
    notas="La comprobación usa que la derivada de cot t es −csc² t < 0 (argumento para la "
          "docente; en clase se justifica con la gráfica).")
reg(11, f"{FP} 11", r"¿Cuál es cierta: $\cot(-t) = \cot t$ o $\cot(-t) = -\cot t$?",
    r"$\cot(-t) = -\cot t$ (la cotangente es impar).", lambda: igual(cot(-t), -cot(t)),
    tipo="seleccion")
reg(12, f"{FP} 12", r"¿Cuál es cierta: $\csc(-t) = \csc t$ o $\csc(-t) = -\csc t$?",
    r"$\csc(-t) = -\csc t$ (la cosecante es impar).",
    lambda: (igual(csc(-t), -csc(t)), cierto(sp.simplify(csc(-t) - csc(t)) != 0)), tipo="seleccion")

# ---------- 13. Amplitud y periodo ----------
filas13 = [("a", r"y = 3\cos t", 3 * cos(t), r"-\pi \le t \le \pi", 3, 2 * pi),
           ("b", r"y = -\sen t", -sin(t), r"-\pi \le t \le \pi", 1, 2 * pi),
           ("c", r"y = \cos 4t", cos(4 * t), r"-\pi \le t \le \pi", 1, pi / 2),
           ("d", r"y = 2\sen \tfrac{1}{2}t", 2 * sin(t / 2), r"-2\pi \le t \le 2\pi", 2, 4 * pi),
           ("e", r"y = 2\cos 3t", 2 * cos(3 * t), r"-\pi \le t \le \pi", 2, 2 * pi / 3),
           ("f", r"y = \tfrac{1}{2}\cos t", cos(t) / 2, r"-\pi \le t \le \pi", Q(1, 2), 2 * pi),
           ("g", r"y = -2\cos t", -2 * cos(t), r"-\pi \le t \le \pi", 2, 2 * pi),
           ("h", r"y = \cos 3t", cos(3 * t), r"-\tfrac{\pi}{2} \le t \le \tfrac{\pi}{2}", 1, 2 * pi / 3),
           ("i", r"y = 3\sen \tfrac{1}{3}t", 3 * sin(t / 3), r"-3\pi \le t \le 3\pi", 3, 6 * pi),
           ("j", r"y = 4\sen 3t", 4 * sin(3 * t), r"-\pi \le t \le \pi", 4, 2 * pi / 3)]
for i, (lit, tx, e, intervalo, A, p) in enumerate(filas13):
    reg(13 + i, f"{FP} 13{lit}",
        r"Determina la amplitud y el periodo de $%s$. Después dibuja su gráfica en $%s$." % (tx, intervalo),
        r"Amplitud $%s$ y periodo $%s$." % (latex_es(A), latex_es(p)),
        lambda e=e, A=A, p=p: (lambda ap=amplitud_periodo(e): (igual(ap[0], A), igual(ap[1], p)))(),
        dificultad=1 if lit in "abfg" else 2,
        notas="En el módulo, junto a «1/3» aparece el texto alternativo «un medio»; se conserva "
              "1/3, que concuerda con el intervalo −3π ≤ t ≤ 3π (un periodo de 6π)."
        if lit == "i" else None)

# ---------- 14–15. Gráficas (manuales) ----------
for i, (lit, tx, desc) in enumerate([
        ("a", r"y = 2\sen t + \cos t", r"Periodo $2\pi$; es una onda como la del seno con máximo "
         r"$\sqrt{5} \approx \num{2,24}$ y mínimo $-\sqrt{5}$; pasa por $(0, 1)$."),
        ("b", r"y = \sen 2t + \cos t", r"Periodo $2\pi$; no es una onda simple: máximo "
         r"$\approx \num{1,76}$ cerca de $t \approx \num{0,63}$ y mínimo $\approx -\num{1,76}$ "
         r"cerca de $t \approx \num{3,77}$; ceros en $t = \frac{\pi}{2}, \frac{7\pi}{6}, "
         r"\frac{3\pi}{2}, \frac{11\pi}{6}$."),
        ("c", r"y = \sen \tfrac{1}{2}t + \tfrac{1}{2}\sen t", r"Periodo $4\pi$ (el de "
         r"$\sen\frac{1}{2}t$); vale $0$ en $t = 0, 2\pi, 4\pi$; es positiva en $(0, 2\pi)$ y "
         r"negativa en $(2\pi, 4\pi)$, con máximo $\approx \num{1,30}$ cerca de "
         r"$t \approx \num{2,09}$."),
        ("d", r"y = \sen t + 2\cos t", r"Periodo $2\pi$; onda con máximo $\sqrt{5}$ y mínimo "
         r"$-\sqrt{5}$; pasa por $(0, 2)$."),
        ("e", r"y = \sen t + \cos 2t", r"Periodo $2\pi$; máximo $\frac{9}{8}$ (en $\sen t = "
         r"\frac{1}{4}$), mínimo $-2$ en $t = \frac{3\pi}{2}$; pasa por $(0, 1)$."),
        ("f", r"y = \cos \tfrac{1}{2}t + \cos t", r"Periodo $4\pi$; máximo $2$ en $t = 0$ y "
         r"$t = 4\pi$, mínimo $-\frac{9}{8}$ (en $\cos\frac{t}{2} = -\frac{1}{4}$).")]):
    manual(23 + i, f"{FP} 14{lit}",
           r"Dibuja la gráfica de $%s$ por el método de sumar ordenadas. Muestra al menos un "
           r"periodo completo." % tx,
           r"Se dibujan las dos funciones sumandos y se suman sus ordenadas punto a punto. " + desc)
for i, (lit, tx, intervalo, desc) in enumerate([
        ("a", r"y = -\cos t", r"-\pi \le t \le \pi", r"la de $\cos t$ reflejada en el eje $t$: "
         r"$-1$ en $t = 0$, $1$ en $t = \pm\pi$, ceros en $\pm\frac{\pi}{2}$."),
        ("b", r"y = 3\sen t", r"-\pi \le t \le \pi", r"onda de amplitud $3$: $3$ en "
         r"$\frac{\pi}{2}$, $-3$ en $-\frac{\pi}{2}$, ceros en $-\pi, 0, \pi$."),
        ("c", r"y = \sen 4t", r"0 \le t \le \pi", r"dos ciclos completos (periodo "
         r"$\frac{\pi}{2}$): máximos $1$ en $\frac{\pi}{8}, \frac{5\pi}{8}$; mínimos $-1$ en "
         r"$\frac{3\pi}{8}, \frac{7\pi}{8}$; ceros cada $\frac{\pi}{4}$."),
        ("d", r"y = 3\cos \tfrac{1}{2}t", r"-2\pi \le t \le 2\pi", r"un ciclo (periodo $4\pi$): "
         r"$3$ en $t = 0$, $-3$ en $t = \pm 2\pi$, ceros en $\pm\pi$.")]):
    manual(29 + i, f"{FP} 15{lit}", r"Dibuja la gráfica de $%s$ en $%s$." % (tx, intervalo),
           r"Es " + desc, dificultad=1)
reg(33, f"{FP} 16",
    r"¿Cuáles son la amplitud y el periodo de $y = \sen 4t$ y de $y = 3\cos \tfrac{1}{2}t$?",
    r"$y = \sen 4t$: amplitud $1$, periodo $\dfrac{\pi}{2}$. $y = 3\cos\frac{1}{2}t$: "
    r"amplitud $3$, periodo $4\pi$.",
    lambda: (igual(amplitud_periodo(sin(4 * t))[0], 1), igual(amplitud_periodo(sin(4 * t))[1], pi / 2),
             igual(amplitud_periodo(3 * cos(t / 2))[0], 3), igual(amplitud_periodo(3 * cos(t / 2))[1], 4 * pi)),
    notas="En el módulo: «los problemas c y d del numeral anterior» (15c y 15d); se escriben "
          "las funciones.")
reg(34, f"{FP} 17",
    r"¿Cuáles son la amplitud y el periodo de $y = -\cos t$ y de $y = 3\sen t$?",
    r"$y = -\cos t$: amplitud $1$, periodo $2\pi$. $y = 3\sen t$: amplitud $3$, periodo $2\pi$.",
    lambda: (igual(amplitud_periodo(-cos(t))[0], 1), igual(amplitud_periodo(-cos(t))[1], 2 * pi),
             igual(amplitud_periodo(3 * sin(t))[0], 3), igual(amplitud_periodo(3 * sin(t))[1], 2 * pi)),
    notas="En el módulo: «los problemas a y b del ejercicio previo» (15a y 15b).")

# ---------- 18–19. Periodo y asíntotas ----------
for i, (fu, lit, tx, e, den, p, asin_tx, a0, paso) in enumerate([
        ("18", "a", r"y = \tg 2t", tan(2 * t), cos(2 * t), pi / 2,
         r"t = \frac{\pi}{4} + k\frac{\pi}{2}", pi / 4, pi / 2),
        ("18", "b", r"y = 3\tg\left(\tfrac{t}{2}\right)", 3 * tan(t / 2), cos(t / 2), 2 * pi,
         r"t = \pi + 2k\pi", pi, 2 * pi),
        ("19", "a", r"y = 2\cot 2t", 2 * cot(2 * t), sin(2 * t), pi / 2, r"t = k\frac{\pi}{2}", 0, pi / 2),
        ("19", "b", r"y = \sec 3t", sec(3 * t), cos(3 * t), 2 * pi / 3,
         r"t = \frac{\pi}{6} + k\frac{\pi}{3}", pi / 6, pi / 3)]):
    reg(35 + i, f"{FP} {fu}{lit}",
        r"Determina el periodo de $%s$ y dibuja su gráfica mostrando al menos tres periodos." % tx,
        r"Periodo $%s$; asíntotas verticales en $%s$ ($k$ entero)." % (latex_es(p), asin_tx),
        lambda e=e, den=den, p=p, a0=a0, paso=paso: (
            igual(sp.periodicity(e, t), p),
            cierto(sp.solveset(den, t, Interval.Ropen(0, 2 * pi))
                   == sp.FiniteSet(*[a0 + j * paso for j in range(int(2 * pi / paso) + 1)
                                     if a0 + j * paso < 2 * pi]))),
        dificultad=2,
        notas="El problema 19 del módulo dice «Síganse las indicaciones del problema anterior»; "
              "se escribe la instrucción completa." if fu == "19" else None)

manual(39, f"{FP} 20",
       r"Dibuja en los mismos ejes las gráficas de $f(t) = \sen t$, $g(t) = 3 + \sen t$ y "
       r"$h(t) = \sen\left(t - \tfrac{\pi}{4}\right)$.",
       r"$g$ es la gráfica de $\sen t$ subida $3$ unidades (oscila entre $2$ y $4$); $h$ es la "
       r"de $\sen t$ corrida $\frac{\pi}{4}$ a la derecha (corta el eje en $\frac{\pi}{4}$ y "
       r"$\frac{5\pi}{4}$, máximo en $\frac{3\pi}{4}$). Las tres tienen periodo $2\pi$ y "
       r"amplitud $1$.", notas="Los literales a–c son las tres curvas de una misma gráfica.")
manual(40, f"{FP} 21",
       r"Dibuja en los mismos ejes las gráficas de $f(t) = \cos t$, $g(t) = -2 + \cos t$ y "
       r"$h(t) = \cos\left(t + \tfrac{\pi}{3}\right)$.",
       r"$g$ es la de $\cos t$ bajada $2$ unidades (oscila entre $-3$ y $-1$); $h$ es la de "
       r"$\cos t$ corrida $\frac{\pi}{3}$ a la izquierda (máximo en $t = -\frac{\pi}{3}$, ceros "
       r"en $\frac{\pi}{6}$ y $\frac{7\pi}{6}$).",
       notas="Los literales a–c son las tres curvas de una misma gráfica. En el módulo: "
             "«Hágalo usando los mismos ejes».")
manual(41, f"{FP} 22",
       r"Dibuja la gráfica de $y = \cos 3t + 2\sen t$ para $-\pi \le t \le \pi$ por el método de "
       r"sumar ordenadas.",
       r"Se suman las ordenadas de $\cos 3t$ (periodo $\frac{2\pi}{3}$) y $2\sen t$. La suma "
       r"tiene periodo $2\pi$; pasa por $(0, 1)$, vale $-1$ en $t = \pm\pi$, alcanza cerca de "
       r"$\num{2,5}$ poco después de $t = \frac{\pi}{2}$ y cerca de $-\num{2,5}$ poco antes de "
       r"$t = -\frac{\pi}{2}$ (máximo $\approx \num{2,53}$ en $t \approx \num{1,91}$).")
manual(42, f"{FP} 23",
       r"Dibuja la gráfica de $y = t + \sen t$ para $-4\pi \le t \le 4\pi$ por el método de sumar "
       r"ordenadas.",
       r"Es la recta $y = t$ con una ondulación: la curva se enrolla alrededor de la recta, la "
       r"toca en $t = k\pi$ y queda entre $y = t - 1$ y $y = t + 1$. Siempre es creciente, con "
       r"tramos horizontales (pendiente $0$) en $t = \pi + 2k\pi$.")
reg(43, f"{FP} 24",
    r"Dibuja la gráfica de $y = t - \cos t$ para $0 \le t \le 6$ calculando $y$ en "
    r"$t = 0; \num{0,5}; 1; \num{1,5}; \dots; 6$ (dos decimales).",
    r"$y \approx -\num{1,00};\ -\num{0,38};\ \num{0,46};\ \num{1,43};\ \num{2,42};\ \num{3,30};\ "
    r"\num{3,99};\ \num{4,44};\ \num{4,65};\ \num{4,71};\ \num{4,72};\ \num{4,79};\ \num{5,04}$. "
    r"La curva sube siempre, cerca de la recta $y = t$ (entre $y = t - 1$ y $y = t + 1$).",
    lambda: [cerca(j / 2 - math.cos(j / 2), v, 2) for j, v in enumerate(
        [-1.00, -0.38, 0.46, 1.43, 2.42, 3.30, 3.99, 4.44, 4.65, 4.71, 4.72, 4.79, 5.04])],
    notas="La tabla se verifica; el dibujo lo revisa la docente.")
reg(44, f"{FP} 25",
    r"Dibuja las gráficas de $y = t$ y $y = 3\sen t$ en los mismos ejes para hallar "
    r"aproximadamente todas las soluciones de $t = 3\sen t$.",
    r"Las gráficas se cortan en tres puntos: $t = 0$ y $t \approx \pm\num{2,28}$.",
    lambda: (cerca(sp.nsolve(t - 3 * sin(t), t, 2.3), 2.28, 2),
             cerca(sp.nsolve(t - 3 * sin(t), t, -2.3), -2.28, 2),
             igual(3 * sin(0), 0),
             # para |t| > 3 no hay cortes porque |3 sen t| ≤ 3
             cierto(sp.calculus.util.function_range(3 * sin(t), t, S.Reals) == Interval(-3, 3))),
    dificultad=2)
I_ = 30 * sin(120 * pi * t)
reg(45, f"{FP} 26a",
    r"La intensidad de corriente $I$ (en amperios) en un circuito de corriente alterna es "
    r"$I = 30\sen(120\pi t)$, con $t$ en segundos. ¿Cuál es el periodo?",
    r"$p = \dfrac{2\pi}{120\pi} = \dfrac{1}{60}$ s.", lambda: igual(sp.periodicity(I_, t), Q(1, 60)),
    tipo="contexto")
reg(46, f"{FP} 26b",
    r"Con $I = 30\sen(120\pi t)$ ($t$ en segundos), ¿cuántos ciclos (periodos) hay en un segundo?",
    r"$60$ ciclos por segundo ($60$ Hz).", lambda: igual(1 / sp.periodicity(I_, t), 60),
    tipo="contexto")
reg(47, f"{FP} 26c",
    r"Con $I = 30\sen(120\pi t)$, ¿cuál es la máxima intensidad de la corriente?",
    r"$30$ amperios.",
    lambda: igual(sp.calculus.util.function_range(I_, t, Interval(0, Q(1, 60))).sup, 30),
    tipo="contexto")
reg(48, f"{FP} 27",
    r"Dibuja la gráfica de $y = \dfrac{\sen t}{t}$ en $-3\pi \le t \le 3\pi$. Marca varios "
    r"puntos con $t$ cerca de $0$ (por ejemplo $t = -\num{0,5}; -\num{0,2}; -\num{0,1}; "
    r"\num{0,1}; \num{0,2}; \num{0,5}$). ¿A qué valor parece acercarse $y$ cuando $t$ se "
    r"acerca a $0$?",
    r"$y(\pm\num{0,5}) \approx \num{0,959}$, $y(\pm\num{0,2}) \approx \num{0,993}$, "
    r"$y(\pm\num{0,1}) \approx \num{0,998}$: $y$ se acerca a $1$. (La función es par, corta el "
    r"eje en $t = \pm\pi, \pm 2\pi, \pm 3\pi$ y sus oscilaciones se achican.)",
    lambda: (igual(sp.limit(sin(t) / t, t, 0), 1),
             [cerca(math.sin(v) / v, m, 3) for v, m in [(0.5, 0.959), (0.2, 0.993), (0.1, 0.998),
                                                         (-0.5, 0.959)]]),
    dificultad=2,
    notas="En el módulo: «t = -0,5; -0,2; 0,1; 0,1; 0,2; 0,5»; el tercero es −0,1.")
reg(49, f"{FP} 28a",
    r"Considera $y = \sen\left(\dfrac{1}{t}\right)$ en el intervalo $0 < t \le 1$. ¿Dónde "
    r"cruza su gráfica el eje $t$?",
    r"Donde $\dfrac{1}{t} = k\pi$: en $t = \dfrac{1}{k\pi}$, $k = 1, 2, 3, \dots$ (infinitos "
    r"cortes que se amontonan cerca de $0$).",
    lambda: ([igual(sin(1 / (1 / (j * pi))), 0) for j in range(1, 6)],
             cierto(1 / pi <= 1),
             # con u = 1/t: t en (1/20, 1] equivale a u en [1, 20)
             cierto(sp.solveset(sin(t), t, Interval.Ropen(1, 20))
                    == sp.FiniteSet(*[j * pi for j in range(1, 7)]))),
    dificultad=3)
reg(50, f"{FP} 28b",
    r"Evalúa $y = \sen\left(\dfrac{1}{t}\right)$ para $t = \dfrac{2}{\pi}; \dfrac{2}{3\pi}; "
    r"\dfrac{2}{5\pi}; \dfrac{2}{7\pi}; \dots$",
    r"$y = 1, -1, 1, -1, \dots$ (alterna entre $1$ y $-1$).",
    lambda: [igual(sin(1 / (2 / ((2 * j - 1) * pi))), (-1) ** (j + 1)) for j in range(1, 9)],
    dificultad=2)
manual(51, f"{FP} 28c",
       r"Dibuja lo mejor que puedas la gráfica de $y = \sen\left(\dfrac{1}{t}\right)$ en "
       r"$0 < t \le 1$, usando una unidad grande en el eje $t$.",
       r"Cerca de $t = 1$ la curva sube despacio hasta $y = 1$ en $t = \frac{2}{\pi} \approx "
       r"\num{0,64}$ y baja a cortar el eje en $t = \frac{1}{\pi} \approx \num{0,32}$; a medida "
       r"que $t$ se acerca a $0$ oscila entre $-1$ y $1$ cada vez más rápido (los cortes "
       r"$\frac{1}{k\pi}$ se amontonan), sin acercarse a ningún valor.", dificultad=3)

# ---------- Prepárate para el ICFES del final del módulo ----------
manual(52, f"{FR} 11", r"Dibuja la gráfica de $y = 3\cos 2t$ para $t$ entre $\pi$ y $2\pi$.",
       r"Amplitud $3$ y periodo $\pi$: en $[\pi, 2\pi]$ hay un ciclo completo; $y = 3$ en "
       r"$t = \pi$ y $t = 2\pi$, $y = -3$ en $t = \frac{3\pi}{2}$, ceros en $\frac{5\pi}{4}$ y "
       r"$\frac{7\pi}{4}$.", dificultad=1)
manual(53, f"{FR} 12",
       r"Dibuja la gráfica de $y = \sen t + \sen 2t$ por el método de sumar ordenadas.",
       r"Periodo $2\pi$; ceros en $t = 0, \frac{2\pi}{3}, \pi, \frac{4\pi}{3}, 2\pi$; máximo "
       r"$\approx \num{1,76}$ en $t \approx \num{0,94}$ y mínimo $\approx -\num{1,76}$ en "
       r"$t \approx \num{5,34}$; es impar (simétrica respecto al origen).")
reg(54, f"{FR} 13", r"¿Cuál es el rango de la función seno? ¿Y el de la función cosecante?",
    r"Seno: $[-1, 1]$; cosecante: $(-\infty, -1] \cup [1, \infty)$.",
    lambda: (cierto(sp.calculus.util.function_range(sin(t), t, S.Reals) == Interval(-1, 1)),
             cierto(sp.imageset(sp.Lambda(t, 1 / t), sp.Union(Interval.Ropen(-1, 0), Interval.Lopen(0, 1)))
                    == RANGO_SEC)),
    tipo="conceptual")
