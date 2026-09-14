"""Banco de ejercicios — Matemáticas — Valor absoluto: ecuaciones e inecuaciones.
Fuente: módulo de Matemáticas 11° de las Guías de Apoyo (Adriana Quintero Palomino), Tema 2;
se lee en recursos/matematicas/Guías pedagógicas Matemáticas/markdown/11 - Modulo_Matematicas_Undecimo.md
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/valor-absoluto.py
"""
from ejercicios import conjunto, desigualdad, ejercicio, ejercicio_manual, serie

FUENTE = "módulo 11° (Quintero Palomino), Tema 2, Valor absoluto — Practica lo aprendido"
COMUN = dict(tema="valor absoluto", grados=[11], dba=["matematicas-11-2"])

# (n, literal, ecuación o inecuación, solución calculada a mano, dificultad[, notas])
serie("valor-absoluto", "Resuelve …", FUENTE, [
    (1, "1a", "Abs(x) < 2", "(-2, 2)", 1),
    (2, "1b", "Abs(x - 2) < 1", "(1, 3)", 1),
    (3, "1c", "Abs(x - 5) < 1", "(4, 6)", 1),
    (4, "1d", "Abs((x + 2)/2) <= 1", "[-4, 0]", 1),
    (5, "1e", "Abs(x - 1) < 1", "(0, 2)", 1),
    (6, "1f", "Abs(2x + 1) >= 5", "(-oo, -3] U [2, oo)", 2),
    (7, "1g", "Abs((7 - 3x)/2) <= 1", "[5/3, 3]", 2),
    (8, "1h", "Abs(x - 10) < 0.3", "(9.7, 10.3)", 1),
    (9, "1i", "Abs(25x - 8) > 7", "(-oo, 1/25) U (3/5, oo)", 2),
    (10, "1j", "Abs(2x - 7) <= 0.01", "[3.495, 3.505]", 2),
    (11, "1k", "Abs((2x - 1)/x) > 2", "(-oo, 0) U (0, 1/4)", 3),
    (12, "1l", "Abs(4x - 5) = 3", "{1/2, 2}", 1),
    (13, "1m", "Abs(x + 6) = 2", "{-8, -4}", 1),
    (14, "1n", "Abs(x + 1) = Abs(x + 2)", "{-3/2}", 2),
    (15, "1o", "Abs(3x - 4) = Abs(2x + 1)", "{3/5, 5}", 2),
    (16, "1p", "Abs(x/3 - 2) <= 4", "[-6, 18]", 2),
    (17, "1q", "Abs(3/x - 2) <= 4", "(-oo, -3/2] U [1/2, oo)", 3),
    (18, "1r", "Abs(4/x) < 3", "(-oo, -4/3) U (4/3, oo)", 2),
    (19, "1s", "Abs(x/(x + 2)) <= 2", "(-oo, -4] U [-4/3, oo)", 3),
    (20, "1t", "Abs(x/(x - 3)) <= 5", "(-oo, 5/2] U [15/4, oo)", 3),
], tipo="calculo", **COMUN)

serie("valor-absoluto", "Halla los valores de $x$ que satisfacen … y expresa la solución "
      "como intervalo o conjunto y en la recta real.", FUENTE, [
          (21, "2a", "Abs(2x + 1) = 2", "{-3/2, 1/2}", 1),
          (22, "2b", "2x + 3 = Abs(3x - 1)", "{-2/5, 4}", 2),
          (23, "2c", "Abs(3 - 2x) = 7", "{-2, 5}", 1),
          (24, "2d", "Abs(x - 8) = 9", "{-1, 17}", 1),
          (25, "2e", "Abs(x + sqrt(2)) >= 1", "(-oo, -1 - sqrt(2)] U [1 - sqrt(2), oo)", 2),
          (26, "2f", "Abs((3x - 1)/4) < 6", "(-23/3, 25/3)", 2,
           "En el módulo la barra de cierre quedó después del 6: «|(3x - 1)/4 < 6|»; se "
           "corrigió a |(3x - 1)/4| < 6."),
          (27, "2g", "Abs(6 - 5x) <= 1/2", "[11/10, 13/10]", 2),
          (28, "2h", "Abs((x + 2)/(2x - 3)) < 4", "(-oo, 10/9) U (2, oo)", 3),
      ], tipo="calculo", **COMUN)


@ejercicio(
    id="valor-absoluto-029", tipo="calculo", dificultad=2, fuente=f"{FUENTE} 3",
    enunciado=r"Si se define $\sqrt{x^2} = |x|$, ¿cuál es la solución de la inecuación "
              r"$x^2 < 25$?",
    respuesta=r"$\sqrt{x^2} < 5 \iff |x| < 5 \iff -5 < x < 5$: la solución es $(-5, 5)$.",
    **COMUN)
def _():
    assert desigualdad("x^2 < 25")[1] == desigualdad("Abs(x) < 5")[1] == conjunto("(-5, 5)")[1]


ejercicio_manual(
    id="valor-absoluto-030", tipo="conceptual", dificultad=2, fuente=f"{FUENTE} 4a",
    enunciado=r"Expresa con una desigualdad con valor absoluto: el radio $r$ de un componente no "
              r"debe diferir de $1$ cm en más de $\num{0,1}$ cm.",
    respuesta=r"$|r - 1| \le \num{0,1}$ (en cm).", **COMUN)

ejercicio_manual(
    id="valor-absoluto-031", tipo="conceptual", dificultad=2, fuente=f"{FUENTE} 4b",
    enunciado=r"Expresa con una desigualdad con valor absoluto: la diferencia entre las edades "
              r"$a$ y $b$ de dos personas tiene que estar entre $0$ y $4$ años.",
    respuesta=r"$|a - b| \le 4$ (la diferencia $|a - b|$ ya es mayor o igual que $0$).", **COMUN)

ejercicio_manual(
    id="valor-absoluto-032", tipo="conceptual", dificultad=2, fuente=f"{FUENTE} 4c",
    enunciado=r"Expresa con una desigualdad con valor absoluto: la distancia entre dos números "
              r"$a$ y $b$ de la recta real debe estar entre $5$ y $27$ unidades.",
    respuesta=r"$5 \le |a - b| \le 27$.", **COMUN)


@ejercicio(
    id="valor-absoluto-033", tipo="calculo", dificultad=2, fuente=f"{FUENTE} 5",
    enunciado=r"Usando que $\sqrt{x^2} = |x|$, resuelve $(3x + 5)^2 < 100$.",
    respuesta=r"$|3x + 5| < 10 \iff -15 < 3x < 5$: la solución es "
              r"$\left(-5, \frac{5}{3}\right)$.", **COMUN)
def _():
    assert desigualdad("(3x + 5)^2 < 100")[1] == desigualdad("Abs(3x + 5) < 10")[1] \
        == conjunto("(-5, 5/3)")[1]


@ejercicio(
    id="valor-absoluto-034", tipo="argumentacion", dificultad=2, fuente=f"{FUENTE} 6",
    enunciado=r"Dada la inecuación $x^2 < 16$, ¿es posible resolverla sacando la raíz cuadrada "
              r"en ambos miembros? Verifica tu respuesta.",
    respuesta=r"Sí, pero $\sqrt{x^2} = |x|$, no $x$: queda $|x| < 4$, es decir $(-4, 4)$. Si se "
              r"escribe $x < 4$ se incluyen valores como $x = -5$, y $(-5)^2 = 25$ no es menor "
              r"que $16$.", **COMUN)
def _():
    correcta = desigualdad("x^2 < 16")[1]
    assert correcta == conjunto("(-4, 4)")[1]
    assert correcta != conjunto("(-oo, 4)")[1] and -5 not in correcta


ejercicio_manual(
    id="valor-absoluto-035", tipo="argumentacion", dificultad=3, fuente=f"{FUENTE} 7",
    enunciado=r"¿Para qué valores de $x$ es cierta la desigualdad $|ax + b| > 0$? Explica.",
    respuesta=r"El valor absoluto es $0$ solo cuando $ax + b = 0$. Si $a \neq 0$, la "
              r"desigualdad se cumple para todo $x$ excepto $x = -\frac{b}{a}$. Si $a = 0$, "
              r"se cumple para todo $x$ cuando $b \neq 0$, y para ninguno cuando $b = 0$.",
    **COMUN)

ejercicio_manual(
    id="valor-absoluto-036", tipo="argumentacion", dificultad=3, fuente=f"{FUENTE} 8",
    enunciado=r"Dados los números reales $m$ y $n$, ¿la desigualdad $|m + n| < |m| + |n|$ es "
              r"siempre cierta? Verifícalo con varios valores de $m$ y $n$. ¿Para qué valores "
              r"no se cumple?",
    respuesta=r"No siempre. Lo que siempre se cumple es $|m + n| \le |m| + |n|$ (desigualdad "
              r"triangular). La igualdad se da cuando $m$ y $n$ tienen el mismo signo o alguno "
              r"es $0$ (por ejemplo $m = 2$, $n = 3$: $5 = 5$), y ahí la desigualdad estricta "
              r"falla. Es estricta solo si tienen signos contrarios ($m = 2$, $n = -3$: "
              r"$1 < 5$).", **COMUN)
