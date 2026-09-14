"""Banco de ejercicios — Matemáticas — Inecuaciones cuadráticas.
Fuente: módulo de Matemáticas 11° de las Guías de Apoyo (Adriana Quintero Palomino), Tema 1;
se lee en recursos/matematicas/Guías pedagógicas Matemáticas/markdown/11 - Modulo_Matematicas_Undecimo.md
(El ejercicio 6 del módulo, (x - 2)(x + 3)(x + 5) <= 0, ya está en el banco: inecuaciones-003.)
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/inecuaciones-cuadraticas.py
"""
from sympy import Interval, Rational, oo, solveset, symbols

from ejercicios import ejercicio, ejercicio_manual, serie

FUENTE = "módulo 11° (Quintero Palomino), Tema 1, Inecuaciones cuadráticas — Practica lo aprendido"
COMUN = dict(tema="inecuaciones cuadráticas", grados=[11], dba=["matematicas-11-2"])

# (n, literal, inecuación, solución calculada a mano, dificultad[, notas])
serie("inecuaciones-cuadraticas", "Resuelve …", FUENTE, [
    (1, "1a", "x^2 + 2x - 15 > 0", "(-oo, -5) U (3, oo)", 1),
    (2, "1b", "x^2 + 3x + 2 > 0", "(-oo, -2) U (-1, oo)", 1),
    (3, "1c", "x^2 - 3x + 2 > 0", "(-oo, 1) U (2, oo)", 1),
    (4, "1d", "4x^2 - 4x + 1 < 0", "vacio", 2),
    (5, "1e", "4x^2 + 9x - 9 < 0", "(-3, 3/4)", 2),
    (6, "1f", "x^2 - 16 < 0", "(-4, 4)", 1),
    (7, "1g", "x^2 + 6x + 9 >= 0", "R", 2),
    (8, "1h", "x^2 + 9x + 20 < 0", "(-5, -4)", 1),
    (9, "1i", "4x^2 - 20x + 25 >= 0", "R", 2),
    (10, "1j", "2x^2 - x - 1 < 0", "(-1/2, 1)", 2),
    (11, "1k", "3x^2 + 2x - 5 > 0", "(-oo, -5/3) U (1, oo)", 2),
    (12, "1l", "2x^2 + 9x + 4 <= 0", "[-4, -1/2]", 2),
    (13, "1m", "8x^2 - 22x + 15 >= 0", "(-oo, 5/4] U [3/2, oo)", 2),
    (14, "1n", "25x^2 + 15x + 2 > 0", "(-oo, -2/5) U (-1/5, oo)", 2),
    (15, "1o", "9x^2 - 36x + 1 <= 0", "[2 - sqrt(35)/3, 2 + sqrt(35)/3]", 3,
     "Las raíces son irracionales (2 ± √35/3): quizás el módulo quería otro término "
     "independiente. Sirve para practicar la fórmula cuadrática."),
    (16, "1p", "x*(x - 5) < 0", "(0, 5)", 1),
    (17, "1q", "(3x - 1)(2x + 3) > 0", "(-oo, -3/2) U (1/3, oo)", 1),
    (18, "1r", "(x + 1)(x - 2) < 0", "(-1, 2)", 1),
], tipo="calculo", **COMUN)

serie("inecuaciones-cuadraticas", "Describe y representa en la recta real el conjunto "
      "determinado por …", FUENTE, [
          (19, "2a", "x^2 < 4", "(-2, 2)", 1),
          (20, "2b", "x^2 >= 9", "(-oo, -3] U [3, oo)", 1),
          (21, "2c", "(x - 2)^2 > 1", "(-oo, 1) U (3, oo)", 2),
          (22, "2d", "(2x + 1)^2 > 1", "(-oo, -1) U (0, oo)", 2),
          (23, "2e", "6x^2 + 13x < 5", "(-5/2, 1/3)", 2),
          (24, "2f", "x^2 + 6x + 8 < 0", "(-4, -2)", 1),
      ], tipo="calculo", **COMUN)

t, v, l = symbols("t v l", real=True)


@ejercicio(
    id="inecuaciones-cuadraticas-025", tipo="contexto", dificultad=3, fuente=f"{FUENTE} 3",
    enunciado=r"Si se lanza un objeto verticalmente hacia arriba desde el suelo con una "
              r"velocidad inicial de $528$ pies por segundo, su altura sobre el suelo es "
              r"$d = -16t^2 + 528t$ (en pies), donde $t$ es el tiempo en segundos. ¿Para qué "
              r"valores de $t$ el objeto está a más de $3200$ pies del suelo?",
    respuesta=r"$-16t^2 + 528t > 3200 \iff t^2 - 33t + 200 < 0 \iff (t - 8)(t - 25) < 0$: "
              r"entre los $8$ y los $25$ segundos, $t \in (8, 25)$.", **COMUN)
def _():
    assert solveset(-16 * t**2 + 528 * t > 3200, t, Interval(0, oo)) == Interval.open(8, 25)


@ejercicio(
    id="inecuaciones-cuadraticas-026", tipo="contexto", dificultad=3, fuente=f"{FUENTE} 4",
    enunciado=r"El número de millas $M$ que cierto auto recorre con un galón de gasolina depende "
              r"de su velocidad $v$ (en millas por hora) según "
              r"$M = -\dfrac{1}{30}v^2 + \dfrac{5}{2}v$, para $0 < v < 70$. ¿A qué velocidades "
              r"$M$ es al menos $45$ millas?",
    respuesta=r"$-\dfrac{1}{30}v^2 + \dfrac{5}{2}v \ge 45 \iff v^2 - 75v + 1350 \le 0 \iff "
              r"(v - 30)(v - 45) \le 0$: entre $30$ y $45$ millas por hora, $v \in [30, 45]$.",
    **COMUN)
def _():
    M = -Rational(1, 30) * v**2 + Rational(5, 2) * v
    assert solveset(M >= 45, v, Interval.open(0, 70)) == Interval(30, 45)


ejercicio_manual(
    id="inecuaciones-cuadraticas-027", tipo="argumentacion", dificultad=2, fuente=f"{FUENTE} 5",
    enunciado=r"Describe un procedimiento para resolver una inecuación de la forma "
              r"$(x + a)(x + b)(x + c) \le 0$.",
    respuesta=r"Se hallan los puntos críticos $-a$, $-b$ y $-c$, donde cada factor vale cero, y "
              r"se ubican en orden en la recta. En cada intervalo que determinan se estudia el "
              r"signo de los tres factores (tabla de signos): el producto es negativo donde hay "
              r"un número impar de factores negativos. Como la desigualdad es $\le 0$, la "
              r"solución es la unión de esos intervalos, incluidos los puntos críticos.",
    **COMUN)


@ejercicio(
    id="inecuaciones-cuadraticas-028", tipo="contexto", dificultad=3, fuente=f"{FUENTE} 7",
    enunciado=r"Se tienen $100$ metros de alambre para cercar un terreno rectangular. ¿Cuánto "
              r"pueden medir el largo y el ancho si el terreno cercado debe tener al menos "
              r"$600$ metros cuadrados?",
    respuesta=r"Si el largo es $l$, el ancho es $50 - l$ y $l(50 - l) \ge 600 \iff "
              r"(l - 20)(l - 30) \le 0$: el largo mide entre $20$ y $30$ m, y el ancho, "
              r"$50 - l$, también queda entre $20$ y $30$ m.",
    notas="En el módulo, el área está en «pies cuadrados» y el alambre en metros; se usan "
          "metros cuadrados.", **COMUN)
def _():
    assert solveset(l * (50 - l) >= 600, l, Interval.open(0, 50)) == Interval(20, 30)
