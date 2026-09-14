"""Banco de ejercicios — Matemáticas — Inecuaciones de primer grado.
Fuente: módulo de Matemáticas 11° de las Guías de Apoyo (Adriana Quintero Palomino), Tema 1;
se lee en recursos/matematicas/Guías pedagógicas Matemáticas/markdown/11 - Modulo_Matematicas_Undecimo.md
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/inecuaciones-lineales.py
"""
from sympy import Interval, Rational, S, oo, solveset, symbols
from sympy.physics.units import ampere, convert_to, ohm, volt

from ejercicios import ejercicio, serie

FUENTE = ("módulo 11° (Quintero Palomino), Tema 1, Solución de inecuaciones de primer grado — "
          "Practica lo aprendido")
COMUN = dict(tema="inecuaciones de primer grado", grados=[11], dba=["matematicas-11-2"])

# (n, literal, inecuación, solución calculada a mano, dificultad)
serie("inecuaciones-lineales", "Resuelve … y expresa la solución en forma de intervalo.",
      FUENTE, [
          (1, "1a", "4 - 3x > 7 + 2x", "(-oo, -3/5)", 1),
          (2, "1b", "-2x + 3 < 7", "(-2, oo)", 1),
          (3, "1c", "3x - 4 <= 8", "(-oo, 4]", 1),
          (4, "1d", "-2x + 3 <= 7", "[-2, oo)", 1),
          (5, "1e", "2x - 3 > 0", "(3/2, oo)", 1),
          (6, "1f", "-(3/5)x - 1/4 <= 2/7", "[-25/28, oo)", 2),
      ], tipo="calculo", **COMUN)

serie("inecuaciones-lineales", "Resuelve … y representa la solución en la recta real.",
      FUENTE, [
          (7, "2a", "3x - 5 < 10", "(-oo, 5)", 1),
          (8, "2b", "7 - 2x >= -3", "(-oo, 5]", 1),
          (9, "2c", "5 + 3x > 6x - 4", "(-oo, 3)", 1),
          (10, "2d", "2 + 7x < 3x - 10", "(-oo, -3)", 1),
          (11, "2e", "6x - 7 > 1", "(4/3, oo)", 1),
          (12, "2f", "2(x + 2) < 5", "(-oo, 1/2)", 1),
          (13, "2g", "3x - 10 >= 5x", "(-oo, -5]", 1),
          (14, "2h", "4x + 10 > 4 - 2x", "(-1, oo)", 1),
          (15, "2i", "x + 4 < 3", "(-oo, -1)", 1),
          (16, "2j", "x + 1/2 < 2 + x/4", "(-oo, 2)", 2),
          (17, "2k", "3x - 5/2 > (1/2)x", "(1, oo)", 2),
          (18, "2l", "(1/3)y - 9 <= 2y - 4", "[-3, oo)", 2),
      ], tipo="calculo", **COMUN)

serie("inecuaciones-lineales", "Halla el conjunto solución de …", FUENTE, [
    (19, "3a", "x + 3 <= 1", "(-oo, -2]", 1),
    (20, "3b", "5 + 3x > 2(3x - 2)", "(-oo, 3)", 1),
    (21, "3c", "3x - 2 < 2x + 1", "(-oo, 3)", 1),
    (22, "3d", "2x + 4 < 5", "(-oo, 1/2)", 1),
    (23, "3e", "3x - 4 > (1/2)(x - 3)", "(1, oo)", 2),
    (24, "3f", "3x - 4 > 5x + 6", "(-oo, -5)", 1),
    (25, "3g", "pi + 6 >= 3x - 2", "(-oo, (pi + 8)/3]", 2),
    (26, "3h", "sqrt(2) - 4 < 3/2 - (1/2)x", "(-oo, 11 - 2sqrt(2))", 3),
    (27, "3i", "(x - 1)(x + 2) <= (x + 1)(x - 2)", "(-oo, 0]", 2),
    (28, "3j", "2x + 1 >= 3 + (x - 1)", "[1, oo)", 1),
], tipo="calculo", **COMUN)

serie("inecuaciones-lineales",
      "Halla el conjunto solución de … y represéntalo en la recta real.", FUENTE, [
          (29, "4a", "x - 5 > 3 - x", "(4, oo)", 1),
          (30, "4b", "2 - 7x < 16", "(-2, oo)", 1),
          (31, "4c", "2x + 1 < 3x - 1", "(2, oo)", 1),
          (32, "4d", "x - 2/3 > 2x + 4/3", "(-oo, -2)", 2),
          (33, "4e", "x + 1 > 3x + 5", "(-oo, -2)", 1),
          (34, "4f", "4x + 3 > 2x - 5", "(-4, oo)", 1),
          (35, "4g", "5x - 6 > 11", "(17/5, oo)", 1),
          (36, "4h", "3x + 2 < 5x - 8", "(5, oo)", 1),
          (37, "4i", "4x - 3/5 > -x - 6", "(-27/25, oo)", 2),
          (38, "4j", "-5x + 2/3 <= sqrt(3)x", "[(5 - sqrt(3))/33, oo)", 3),
          (39, "4k", "x/5 - (2/3)x >= x/5", "(-oo, 0]", 2),
          (40, "4l", "12 - (5/3)x < -9x + 4", "(-oo, -12/11)", 2),
      ], tipo="calculo", **COMUN)

R, F, t = symbols("R F t", real=True)


@ejercicio(
    id="inecuaciones-lineales-041", tipo="contexto", dificultad=2, fuente=f"{FUENTE} 5a",
    enunciado=r"La ley de Ohm, $I = \dfrac{V}{R}$, relaciona la corriente $I$ (en amperios, A) "
              r"que circula por un objeto, la diferencia de potencial $V$ (en voltios, V) y la "
              r"resistencia $R$ del objeto (en ohmios, $\Omega$). Si el voltaje es de $110$ V, "
              r"¿qué valores de la resistencia producen una corriente que no exceda los $10$ A?",
    respuesta=r"$\dfrac{110}{R} \le 10$ con $R > 0$, es decir, $R \ge 11\ \Omega$.",
    notas="En el módulo, el voltio aparece como «v» minúscula; se usa «V».", **COMUN)
def _():
    assert solveset(110 / R <= 10, R, Interval.open(0, oo)) == Interval(11, oo)
    assert convert_to(110 * volt / (11 * ohm), ampere) == 10 * ampere   # unidades


@ejercicio(
    id="inecuaciones-lineales-042", tipo="contexto", dificultad=2, fuente=f"{FUENTE} 5b",
    enunciado=r"La fórmula $C = \dfrac{5}{9}(F - 32)$ relaciona las lecturas de temperatura en "
              r"grados Celsius ($C$) y Fahrenheit ($F$). ¿Qué temperaturas en grados Fahrenheit "
              r"corresponden a menos de $30\,^{\circ}$C?",
    respuesta=r"$\dfrac{5}{9}(F - 32) < 30 \iff F - 32 < 54 \iff F < 86$: menos de "
              r"$86\,^{\circ}$F.",
    notas="En el módulo aparece «Farenheit».", **COMUN)
def _():
    assert solveset(Rational(5, 9) * (F - 32) < 30, F, S.Reals) == Interval.open(-oo, 86)


@ejercicio(
    id="inecuaciones-lineales-043", tipo="contexto", dificultad=2, fuente=f"{FUENTE} 5c",
    enunciado=r"La posición de un móvil está dada por $s(t) = 30t + 8$, donde $t$ es el tiempo "
              r"en minutos y $s$ la posición en metros. ¿Para qué valores de $t$ la posición es "
              r"de máximo $500$ metros?",
    respuesta=r"$30t + 8 \le 500 \iff t \le \num{16,4}$; como $t \ge 0$: "
              r"$0 \le t \le \num{16,4}$ minutos.", **COMUN)
def _():
    assert solveset(30 * t + 8 <= 500, t, Interval(0, oo)) == Interval(0, Rational(82, 5))
