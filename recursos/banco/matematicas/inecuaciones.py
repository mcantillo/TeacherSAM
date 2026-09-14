"""Banco de ejercicios — Matemáticas — Inecuaciones.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/inecuaciones.py
"""
from sympy import Interval, S, Union, oo, solveset, symbols

from ejercicios import ejercicio, ejercicio_manual

x, t = symbols("x t", real=True)


@ejercicio(
    id="inecuaciones-001", tema="inecuaciones cuadráticas", grados=[11], dba=["matematicas-11-2"],
    tipo="calculo", dificultad=1, fuente="guía Cálculo 11° P-I, ejemplo 6",
    enunciado=r"Resuelve $x^2 - x - 6 \le 0$ y escribe la solución como intervalo.",
    respuesta=r"$(x - 3)(x + 2) \le 0$; puntos críticos $-2$ y $3$; solución $[-2, 3]$.")
def _():
    assert solveset(x**2 - x - 6 <= 0, x, S.Reals) == Interval(-2, 3)


@ejercicio(
    id="inecuaciones-002", tema="inecuaciones racionales", grados=[11], dba=["matematicas-11-2"],
    tipo="calculo", dificultad=2, fuente="guía Cálculo 11° P-I, ejemplo 7",
    enunciado=r"Resuelve $\dfrac{x - 1}{x + 2} \ge 0$.",
    respuesta=r"$(-\infty, -2) \cup [1, \infty)$; el $-2$ se excluye porque anula el denominador.")
def _():
    assert solveset((x - 1) / (x + 2) >= 0, x, S.Reals) == Union(Interval.open(-oo, -2), Interval(1, oo))


@ejercicio(
    id="inecuaciones-003", tema="inecuaciones polinómicas", grados=[11], dba=["matematicas-11-2"],
    tipo="calculo", dificultad=2, fuente="guía Cálculo 11° P-I, tema 6",
    enunciado=r"Resuelve $(x - 2)(x + 3)(x + 5) \le 0$ con una tabla de signos de tres factores.",
    respuesta=r"$(-\infty, -5] \cup [-3, 2]$.")
def _():
    assert solveset((x - 2) * (x + 3) * (x + 5) <= 0, x, S.Reals) == Union(Interval(-oo, -5), Interval(-3, 2))


@ejercicio(
    id="inecuaciones-004", tema="inecuaciones racionales", grados=[11], dba=["matematicas-11-2"],
    tipo="contexto", dificultad=3,
    fuente="guía Cálculo 11° P-I, tema 6 (idea: módulo 11° de Quintero Palomino)",
    enunciado=r"La concentración de un medicamento en la sangre, $t$ horas después de tomarlo, es "
              r"$c(t) = \dfrac{20t}{t^2 + 4}$ mg/L, y hace efecto cuando supera 4 mg/L. "
              r"¿Durante qué intervalo de tiempo hace efecto?",
    respuesta=r"Como $t^2 + 4 > 0$, $20t > 4t^2 + 16 \iff t^2 - 5t + 4 < 0 \iff (t-1)(t-4) < 0$: "
              r"entre la hora 1 y la hora 4, $t \in (1, 4)$.")
def _():
    assert solveset(20 * t / (t**2 + 4) > 4, t, Interval.open(0, oo)) == Interval.open(1, 4)


@ejercicio(
    id="inecuaciones-005", tema="inecuaciones racionales", grados=[11], dba=["matematicas-11-2"],
    tipo="encuentra-el-error", dificultad=2, fuente="guía Cálculo 11° P-I, tema 6",
    enunciado=r"Pedro resolvió $\dfrac{2}{x} < 1$ así: «Multiplico ambos lados por $x$ y queda "
              r"$2 < x$. Solución: $(2, \infty)$». ¿Qué paso no es correcto y por qué? Halla la "
              r"solución correcta.",
    respuesta=r"Multiplicó por $x$ sin saber su signo: si $x < 0$ la desigualdad se invierte. "
              r"Solución: $(-\infty, 0) \cup (2, \infty)$ (por ejemplo, $x = -1$ cumple).")
def _():
    correcta = solveset(2 / x < 1, x, S.Reals)
    assert correcta == Union(Interval.open(-oo, 0), Interval.open(2, oo))
    assert correcta != Interval.open(2, oo)          # la respuesta de Pedro está mal
    assert bool((2 / x < 1).subs(x, -1))             # un negativo que Pedro dejó por fuera


ejercicio_manual(
    id="inecuaciones-006", tema="propiedades de orden", grados=[11], dba=["matematicas-11-2"],
    tipo="argumentacion", dificultad=2, fuente="guía Cálculo 11° P-I, tema 4",
    enunciado=r"Explica con un ejemplo y con un argumento general por qué, al multiplicar ambos "
              r"lados de una desigualdad por un número negativo, el sentido se invierte.",
    respuesta=r"Ejemplo: $2 < 5$; al multiplicar por $-1$ quedan $-2$ y $-5$, y $-5$ está a la "
              r"izquierda de $-2$, así que $-2 > -5$. General: si $a < b$ y $c < 0$, entonces "
              r"$bc - ac = (b - a)c < 0$ (positivo por negativo), luego $ac > bc$.")
