"""Banco de ejercicios — Matemáticas — Inecuaciones racionales.
Fuente: módulo de Matemáticas 11° de las Guías de Apoyo (Adriana Quintero Palomino), Tema 1;
se lee en recursos/matematicas/Guías pedagógicas Matemáticas/markdown/11 - Modulo_Matematicas_Undecimo.md
(El ejercicio 8 del módulo, el del medicamento, ya está en el banco: inecuaciones-004.)
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/inecuaciones-racionales.py
"""
from sympy import Interval, N, S, oo, solveset, sqrt, symbols

from ejercicios import conjunto, desigualdad, ejercicio, serie

FUENTE = "módulo 11° (Quintero Palomino), Tema 1, Inecuaciones racionales — Practica lo aprendido"
COMUN = dict(tema="inecuaciones racionales", grados=[11], dba=["matematicas-11-2"])

# (n, literal, inecuación, solución calculada a mano, dificultad)
serie("inecuaciones-racionales", "Determina los valores de $x$ que satisfacen …", FUENTE, [
    (1, "1a", "(x - 3)/(x + 2) < 0", "(-2, 3)", 1),
    (2, "1b", "(x + 5)/x >= 0", "(-oo, -5] U (0, oo)", 1),
    (3, "1c", "(2x + 6)/(x - 3) <= 0", "[-3, 3)", 1),
    (4, "1d", "(x + 1)/(x - 1) + 2 >= 0", "(-oo, 1/3] U (1, oo)", 2),
    (5, "1e", "(2x - 3)/(5x + 2) >= -2", "(-oo, -2/5) U [-1/12, oo)", 2),
    (6, "1f", "(x - 1)/(3x + 2) >= 0", "(-oo, -2/3) U [1, oo)", 1),
    (7, "1g", "x*(x - 1)/(x + 5) >= 0", "(-5, 0] U [1, oo)", 2),
    (8, "1h", "(3x^2 - 2x)/(3x - 2) <= -2", "(-oo, -2]", 3),
], tipo="calculo", **COMUN)

serie("inecuaciones-racionales", "Resuelve … y expresa el resultado en forma de intervalos.",
      FUENTE, [
          (9, "2a", "(3x + 2)/(2x - 7) <= 0", "[-2/3, 7/2)", 1),
          (10, "2b", "5/(7 - 2x) > 0", "(-oo, 7/2)", 1),
          (11, "2c", "(x + 2)/(x - 1) < 0", "(-2, 1)", 1),
          (12, "2d", "(x + 3)/(x - 4) > 1", "(4, oo)", 2),
          (13, "2e", "3/(2x - 2) > 1/(2x + 1)", "(-5/4, -1/2) U (1, oo)", 3),
          (14, "2f", "x/(1 + x) > (x - 1)/(x + 2)", "(-2, -1) U (-1/2, oo)", 3),
      ], tipo="calculo", **COMUN)

serie("inecuaciones-racionales", "Halla el intervalo donde puede encontrarse $x$: …", FUENTE, [
    (15, "3a", "(x + 5)/(x^2 - 7x + 12) <= 0", "(-oo, -5] U (3, 4)", 3),
    (16, "3b", "(x^2 - 1)(x + 3)/(x^2 - 4) > 0", "(-3, -2) U (-1, 1) U (2, oo)", 3),
], tipo="calculo", **COMUN)

POSITIVA = "(x^4 + 8)/(x^6 + x^2 + 6) > 0"


@ejercicio(
    id="inecuaciones-racionales-017", tipo="argumentacion", dificultad=2, fuente=f"{FUENTE} 4",
    enunciado=rf"¿Es posible encontrar algún valor de $x$ que satisfaga "
              rf"${desigualdad(POSITIVA)[0]}$? Explica.",
    respuesta=r"Sí, cualquier número real: $x^4 + 8 \ge 8 > 0$ y $x^6 + x^2 + 6 \ge 6 > 0$, así "
              r"que el cociente de dos positivos siempre es positivo. La solución es "
              r"$\mathbb{R}$.", **COMUN)
def _():
    assert desigualdad(POSITIVA)[1] == S.Reals


@ejercicio(
    id="inecuaciones-racionales-018", tipo="encuentra-el-error", dificultad=2,
    fuente=f"{FUENTE} 5",
    enunciado=r"Observa este procedimiento para resolver $\dfrac{3x + 2}{x} < 1$. "
              r"Paso 1: se multiplican ambos lados por $x$, $\dfrac{3x + 2}{x} \cdot x < 1 \cdot x$. "
              r"Paso 2: se cancela $x$, $3x + 2 < x$. Paso 3: se resta $x$ a ambos lados, "
              r"$3x + 2 - x < x - x$. Paso 4: se opera, $2x + 2 < 0$. Paso 5: se despeja, "
              r"$x < -1$. ¿Cuál de los pasos no es correcto? ¿Por qué?",
    respuesta=r"El paso 1: se multiplicó por $x$ sin saber su signo, y si $x < 0$ la desigualdad "
              r"se invierte. Por ejemplo, $x = -2$ cumple $x < -1$ pero "
              r"$\dfrac{3(-2) + 2}{-2} = 2$, que no es menor que $1$. Correcto: "
              r"$\dfrac{3x + 2}{x} - 1 = \dfrac{2x + 2}{x} < 0$, solución $(-1, 0)$.",
    notas="En el módulo, el paso 2 dice «3x + 2 < x • x»; debe decir «3x + 2 < x», como "
          "confirma el paso 3.", **COMUN)
def _():
    correcta = desigualdad("(3x + 2)/x < 1")[1]
    assert correcta == conjunto("(-1, 0)")[1]
    assert correcta != conjunto("(-oo, -1)")[1]                # la respuesta del procedimiento
    assert -2 not in correcta                                  # contraejemplo de la respuesta


@ejercicio(
    id="inecuaciones-racionales-019", tipo="argumentacion", dificultad=2, fuente=f"{FUENTE} 6",
    enunciado=r"Explica para qué valores de $x$ se cumple $\dfrac{x^2 + 5}{x^{10}} > 0$.",
    respuesta=r"Para todo $x \neq 0$: el numerador es mayor o igual que $5$ y $x^{10}$ es "
              r"positivo si $x \neq 0$; en $x = 0$ no está definida. Solución: "
              r"$(-\infty, 0) \cup (0, \infty)$.", **COMUN)
def _():
    assert desigualdad("(x^2 + 5)/x^10 > 0")[1] == conjunto("(-oo, 0) U (0, oo)")[1]


x = symbols("x", real=True)


@ejercicio(
    id="inecuaciones-racionales-020", tipo="contexto", dificultad=3, fuente=f"{FUENTE} 7",
    enunciado=r"Después de que un astronauta es lanzado al espacio, su peso disminuye hasta que "
              r"alcanza un estado de ingravidez. El peso (en libras) de un astronauta de $140$ "
              r"libras a una altitud de $x$ km sobre el nivel del mar es "
              r"$W = 140\left(\dfrac{6400}{6400 + x}\right)^2$. ¿A qué altitud su peso será "
              r"menor de $10$ libras?",
    respuesta=r"$\left(\dfrac{6400}{6400 + x}\right)^2 < \dfrac{1}{14} \iff 6400 + x > "
              r"6400\sqrt{14}$: a más de $6400(\sqrt{14} - 1) \approx \num{17547}$ km.",
    notas="En el módulo la altitud aparece como «X km» y en la fórmula como x; se usa x.",
    **COMUN)
def _():
    limite = 6400 * (sqrt(14) - 1)
    assert solveset(140 * (6400 / (6400 + x))**2 < 10, x, Interval(0, oo)) == Interval.open(limite, oo)
    assert abs(N(limite) - 17547) < 1
