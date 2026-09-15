"""Banco de ejercicios — Álgebra 9° — Fracciones algebraicas.
Guía de Álgebra 9°, trimestre I («El libro que le dio nombre al álgebra»):
materias/algebra/noveno/guia-didactica/guia-periodo-I-reales-y-factorizacion.plan.md
NUEVOS porque el banco no tenía nada de fracciones algebraicas (ni hay recurso; ver
plan-anual.md): regla de la docente del 2026-09-15 — solo banco, salvo un tema sin ningún
ejercicio. Mínimo necesario: dos ejercicios; un literal de cada uno es ejemplo resuelto en la
guía.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/fracciones-algebraicas-9.py
"""
from sympy import S, simplify, solveset, symbols

from ejercicios import ejercicio

FUENTE = "guía Álgebra 9° P-I (Al-Juarismi), tema 3 (sin recurso)"
COMUN = dict(tema="fracciones algebraicas", grados=[9], dba=["matematicas-9-2"])
x = symbols("x", real=True)


def eq(p, q):
    return simplify(p - q) == 0


def ceros(p):
    return solveset(p, x, S.Reals)


@ejercicio(
    id="fracciones-algebraicas-9-001", tipo="calculo", dificultad=2, fuente=FUENTE,
    notas="literal a) = ejemplo resuelto de la guía",
    enunciado=r"Simplifica e indica los valores de $x$ para los que la expresión no está "
              r"definida: a) $\dfrac{x^2 - 9}{x^2 + 3x}$ \quad b) $\dfrac{x^2 - 4}{x^2 - 4x + 4}$ "
              r"\quad c) $\dfrac{2x^2 + 6x}{x^2 - 9}$ \quad d) $\dfrac{x^3 - 1}{x^2 - 1}$",
    respuesta=r"a) $\dfrac{(x - 3)(x + 3)}{x(x + 3)} = \dfrac{x - 3}{x}$; $x \ne 0, -3$ \quad "
              r"b) $\dfrac{x + 2}{x - 2}$; $x \ne 2$ \quad c) $\dfrac{2x}{x - 3}$; $x \ne \pm 3$ "
              r"\quad d) $\dfrac{x^2 + x + 1}{x + 1}$; $x \ne \pm 1$", **COMUN)
def _():
    assert eq((x**2 - 9) / (x**2 + 3 * x), (x - 3) / x) and ceros(x**2 + 3 * x) == {0, -3}
    assert eq((x**2 - 4) / (x**2 - 4 * x + 4), (x + 2) / (x - 2)) and ceros(x**2 - 4 * x + 4) == {2}
    assert eq((2 * x**2 + 6 * x) / (x**2 - 9), 2 * x / (x - 3)) and ceros(x**2 - 9) == {-3, 3}
    assert eq((x**3 - 1) / (x**2 - 1), (x**2 + x + 1) / (x + 1)) and ceros(x**2 - 1) == {-1, 1}


@ejercicio(
    id="fracciones-algebraicas-9-002", tipo="calculo", dificultad=3, fuente=FUENTE,
    notas="literales a) y c) = ejemplos resueltos de la guía",
    enunciado=r"Efectúa y simplifica: a) $\dfrac{x^2 - 1}{x + 2} \cdot \dfrac{x^2 + 4x + 4}{x - 1}$ "
              r"\quad b) $\dfrac{x^2 - x - 6}{x^2 - 4} \div \dfrac{x - 3}{x + 2}$ \quad "
              r"c) $\dfrac{1}{x - 1} + \dfrac{2}{x + 1}$ \quad "
              r"d) $\dfrac{x}{x^2 - 9} - \dfrac{1}{x - 3}$",
    respuesta=r"a) $(x + 1)(x + 2)$ \quad b) $\dfrac{x + 2}{x - 2}$ \quad "
              r"c) $\dfrac{(x + 1) + 2(x - 1)}{(x - 1)(x + 1)} = \dfrac{3x - 1}{x^2 - 1}$ \quad "
              r"d) $\dfrac{x - (x + 3)}{(x - 3)(x + 3)} = \dfrac{-3}{x^2 - 9}$", **COMUN)
def _():
    assert eq((x**2 - 1) / (x + 2) * (x**2 + 4 * x + 4) / (x - 1), (x + 1) * (x + 2))
    assert eq((x**2 - x - 6) / (x**2 - 4) / ((x - 3) / (x + 2)), (x + 2) / (x - 2))
    assert eq(1 / (x - 1) + 2 / (x + 1), (3 * x - 1) / (x**2 - 1))
    assert eq(x / (x**2 - 9) - 1 / (x - 3), -3 / (x**2 - 9))
