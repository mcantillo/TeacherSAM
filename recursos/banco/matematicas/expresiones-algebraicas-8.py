"""Banco de ejercicios — Matemáticas 8° — Expresiones algebraicas: términos semejantes,
clasificación, grado, reducción, lenguaje algebraico y valor numérico.
Fuente: módulo de Matemáticas 8° de las Guías de Apoyo (Adriana Quintero Palomino), Tema 2;
se lee en recursos/matematicas/Guías pedagógicas Matemáticas/markdown/08 - Modulo_Matematicas_Octavo.md
(«Practica lo aprendido» y «Prepárate para el ICFES» de la sección «Valor numérico de un polinomio»).
No incluidos: 5t (en el módulo se imprimió «6x^4 - 3x^4 + 7», idéntico a 5c; su texto alternativo
describe otra expresión). En la sección ICFES, «1.» y «2.» son las fórmulas, no preguntas.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/expresiones-algebraicas-8.py
"""
import re

from sympy import Add, Eq, Poly, Rational, S, expand, pi, simplify, sqrt, symbols

from ejercicios import ejercicio, expresion

FUENTE = ("módulo 8° (Quintero Palomino), Tema 2, Expresiones algebraicas, Valor numérico de un "
          "polinomio — Practica lo aprendido")
ICFES = ("módulo 8° (Quintero Palomino), Tema 2, Expresiones algebraicas, Valor numérico de un "
         "polinomio — Prepárate para el ICFES")
COMUN = dict(tema="expresiones algebraicas", grados=[8], dba=["matematicas-8-9"])
PREFIJO = "expresiones-algebraicas-8"
_n = 0


def nuevo_id():
    global _n
    _n += 1
    return f"{PREFIJO}-{_n:03d}"


def ltx(s):
    """LaTeX de un texto «llano» escrito para expresion(): (5/4) → \\frac{5}{4}, ^3 → ^{3},
    0.5 → 0{,}5, espacios entre factores fuera."""
    s = re.sub(r"\((-?)(\d+)/(\d+)\)", lambda m: f"{m[1]}\\frac{{{m[2]}}}{{{m[3]}}}", s)
    s = re.sub(r"\^\(([^()]*)\)", r"^{\1}", s)
    s = re.sub(r"\^(\d+)", r"^{\1}", s)
    s = re.sub(r"(\d)\.(\d)", r"\1{,}\2", s)
    s = s.replace("*", r" \cdot ")
    return re.sub(r"(?<=[\w})]) (?=[\w\\(])", "", s)


def literal(e):
    return e.as_coeff_Mul()[1]


def opciones(*items):
    return r" \begin{opciones} " + " ".join(r"\item " + i for i in items) + r" \end{opciones}"


# ---------- 1. ¿Términos semejantes? ----------
SEMEJANTES = [
    ("1a", "2x^2 y^3", "2x^3 y^2", False),
    ("1b", "3x^2 y^3", "2x^2 y^3", True),
    ("1c", "4x^2 y^3", "2x y", False),
    ("1d", "-2x^2 y^3", "2x^2 y^3", True),
    ("1e", "-(1/2)a b", "(3/10)a b", True),
    ("1f", "-6a^(x + 1)", "8a^x", False),
]
for lit, a, b, sem in SEMEJANTES:
    @ejercicio(id=nuevo_id(), tipo="conceptual", dificultad=1, fuente=f"{FUENTE} {lit}",
               enunciado=f"¿Son términos semejantes ${ltx(a)}$ y ${ltx(b)}$?",
               respuesta=("Sí: tienen la misma parte literal." if sem else
                          "No: su parte literal no es la misma (las letras no tienen los mismos "
                          "exponentes)."), **COMUN)
    def _(a=a, b=b, sem=sem):
        assert (literal(expresion(a)) == literal(expresion(b))) == sem


# ---------- 2. Cinco términos semejantes ----------
COEFS = ["2", "-3", "(1/2)", "10", "-7"]
for lit, t in [("2a", "x y^2 z"), ("2b", "x^2 y z"), ("2c", "x y z^2"), ("2d", "x^2 y^2 z^2"),
               ("2e", "x y z"), ("2f", "x y z")]:
    dado = {"2a": "5x y^2 z", "2b": "-x^2 y z", "2c": "5x y z^2", "2d": "x^2 y^2 z^2",
            "2e": "6x y z", "2f": "-6x y z"}[lit]
    lista = [f"{c}{t}" for c in COEFS]

    @ejercicio(id=nuevo_id(), tipo="conceptual", dificultad=1, fuente=f"{FUENTE} {lit}",
               enunciado=f"Escribe cinco términos semejantes a ${ltx(dado)}$.",
               respuesta="Por ejemplo: " + ", ".join(f"${ltx(x)}$" for x in lista)
                         + " (cualquier coeficiente con la misma parte literal).", **COMUN)
    def _(dado=dado, lista=lista):
        assert all(literal(expresion(x)) == literal(expresion(dado)) for x in lista)
        assert len({expresion(x) for x in lista}) == 5


# ---------- 3. Monomio, binomio, trinomio, polinomio o ninguno ----------
NOMBRES = {1: "monomio", 2: "binomio", 3: "trinomio"}
CLASES = [
    ("3a", "1/x", r"\frac{1}{x}", "ninguno"),
    ("3b", "15p^2 q r^5", None, "monomio"),
    ("3c", "-12a b^7 - 12", None, "binomio"),
    ("3d", "y^3 - 3y^2 - 5", None, "trinomio"),
    ("3e", "r^2/7", r"\frac{r^{2}}{7}", "monomio"),
    ("3f", "5x^3 - 6x - 3", None, "trinomio"),
    ("3g", "-4m^5 + 6/m - 1", r"-4m^{5} + \frac{6}{m} - 1", "ninguno"),
    ("3h", "4 + y", None, "binomio"),
    ("3i", "-h^2 - 3h + 8", None, "trinomio"),
    ("3j", "7/r^2", r"\frac{7}{r^{2}}", "ninguno"),
    ("3k", "7 + 6x^2", None, "binomio"),
    ("3l", "a^2 + a b + b^3", None, "trinomio"),
    ("3m", "-43", None, "monomio"),
    ("3n", "5x^5 y^3 + 5x^3 y^2 + 6", None, "trinomio"),
    ("3o", "7x^4 - 9x^2 + 6x - 1", None, "polinomio"),
]
for lit, s, latex, clase in CLASES:
    resp = {"ninguno": "Ninguno: no es un polinomio, porque tiene una variable en el "
                       "denominador (exponente negativo).",
            "polinomio": "Polinomio de cuatro términos."}.get(clase, clase.capitalize() + ".")

    @ejercicio(id=nuevo_id(), tipo="conceptual", dificultad=1, fuente=f"{FUENTE} {lit}",
               enunciado=f"Di si ${latex or ltx(s)}$ es un monomio, un binomio, un trinomio, un "
                         f"polinomio o ninguno de ellos.",
               respuesta=resp,
               notas=("El texto alternativo del módulo repite «y elevado a la 3»; la fórmula "
                      "impresa es correcta." if lit == "3d" else None), **COMUN)
    def _(s=s, clase=clase):
        e = expresion(s)
        if not e.is_polynomial(*e.free_symbols):
            calc = "ninguno"
        else:
            k = len(Add.make_args(e))
            calc = NOMBRES.get(k, "polinomio")
        assert calc == clase


# ---------- 4. Grado de cada término y del polinomio ----------
GRADOS = [
    ("4a", "2x - 4", [1, 0], 1), ("4b", "-3x + 6", [1, 0], 1),
    ("4c", "3x^2 - 5x + 2", [2, 1, 0], 2), ("4d", "5x^2 + 3x + 3", [2, 1, 0], 2),
    ("4e", "-7x^3 + 6x^2 + 3x + 7", [3, 2, 1, 0], 3), ("4f", "5x^4 + x^2 - x + 2", [4, 2, 1, 0], 4),
    ("4g", "x^2 - 3x + x^6 - 9x^4", [2, 1, 6, 4], 6), ("4h", "8x - 3x^2 + 9 - 8x^3", [1, 2, 0, 3], 3),
    ("4i", "-7x^3 y^3 + 6x^2 y^2 + 3x y + 7", [6, 4, 2, 0], 6),
    ("4j", "5x^4 y - x^2 y - x + 2", [5, 3, 1, 0], 5),
    ("4k", "-5x^4 y^5 + 6x^3 y^6 - 3x^2 y^2", [9, 9, 4], 9),
    ("4l", "7x^3 y - 4x^2 - 4x y + 5", [4, 2, 2, 0], 4),
]
for lit, s, gs, g in GRADOS:
    @ejercicio(id=nuevo_id(), tipo="calculo", dificultad=1, fuente=f"{FUENTE} {lit}",
               enunciado=f"Identifica el grado de cada término y el grado del polinomio "
                         f"${ltx(s)}$.",
               respuesta=f"Grados de los términos, en el orden escrito: "
                         f"{', '.join(map(str, gs))}. Grado del polinomio: {g}.", **COMUN)
    def _(s=s, gs=gs, g=g):
        e = expresion(s)
        v = sorted(e.free_symbols, key=str)
        calc = sorted(Poly(t, *v).total_degree() for t in Add.make_args(e))
        assert calc == sorted(gs) and Poly(e, *v).total_degree() == g == max(gs)


# ---------- 5. Reducción de términos semejantes ----------
REDUCIR = [
    ("5a", "2x - 5x", "-3x"), ("5b", "3x^2 - 4x^2", "-x^2"),
    ("5c", "6x^4 - 3x^4 + 7", "3x^4 + 7"), ("5d", "5x^3 - 3 - 2x^3", "3x^3 - 3"),
    ("5e", "3a^4 - 2a + 2a + a^4", "4a^4"),
    ("5f", "4x y^2 + 2x^2 y - x y^2 + 3x^2 y", "3x y^2 + 5x^2 y"),
    ("5g", "2a b^2 + 3a b - 5a^2 b + 4a b^2", "6a b^2 + 3a b - 5a^2 b"),
    ("5h", "x - 9x", "-8x", "En el módulo aparece «X – 9x» (X mayúscula); se escribe x."),
    ("5i", "x^3 - 5x - 2x^3", "-x^3 - 5x"), ("5j", "6x^4 - 2x^4 + 5", "4x^4 + 5"),
    ("5k", "-3x^4 - 6x^4 + 5", "-9x^4 + 5"), ("5l", "2x^2 - 6x + 3x + 4x^2", "6x^2 - 3x"),
    ("5m", "-7m^2 n^2 + 2m n - 2m^2 n^2", "-9m^2 n^2 + 2m n"),
    ("5n", "6x^2 + 5x y^2 + 2x^2 - 3x y^2", "8x^2 + 2x y^2"),
    ("5o", "2x^2 + 8x^2", "10x^2"), ("5p", "5x^3 + 6x^3 + 4", "11x^3 + 4"),
    ("5q", "19x^4 - 6x^4 + 4x^2", "13x^4 + 4x^2"),
    ("5r", "2m n^2 - 3m^2 n - 5m^2 n^2 + 4m n^2", "6m n^2 - 3m^2 n - 5m^2 n^2"),
    ("5s", "2h^3 - 3h^2 - 6h^3", "-4h^3 - 3h^2"),
    ("5u", "-a^4 - a + 7a + a^4", "6a"),
    ("5v", "(5/4)x^3 - (3/5)x^3 + 5x^3", "(113/20)x^3"),
    ("5w", "-(2/3)n p^3 + (7/4)p^3 n + 5p^3", "(13/12)n p^3 + 5p^3",
     "El texto alternativo dice «5 p elevado a la 5»; la fórmula impresa dice 5p^3 y se "
     "conserva."),
    ("5x", "(9/7)x^3 y - 2x y^3 + (1/7)y x^3", "(10/7)x^3 y - 2x y^3",
     "El texto alternativo describe otra expresión (en n y p); se usa la fórmula impresa."),
]
for lit, s, r, *nota in REDUCIR:
    @ejercicio(id=nuevo_id(), tipo="calculo", dificultad=2 if "/" in s else 1,
               fuente=f"{FUENTE} {lit}", enunciado=f"Reduce los términos semejantes: ${ltx(s)}$.",
               respuesta=f"${ltx(r)}$.", **(dict(notas=nota[0]) if nota else {}), **COMUN)
    def _(s=s, r=r):
        assert expand(expresion(s) - expresion(r)) == 0
        assert len(Add.make_args(expand(expresion(r)))) == r.count(" + ") + r.count(" - ") + 1


# ---------- 6. Perímetros ----------
PERIMETROS = [
    ("6a", "un pentágono cuyos lados miden $x + 2$, $3y + 1$, $2x - 5$, $x + y$ y $2y - 3$",
     ["x + 2", "3y + 1", "2x - 5", "x + y", "2y - 3"], "4x + 6y - 5"),
    ("6b", "un rectángulo cuyos lados miden $x + y$ y $x - 1$",
     ["x + y", "x - 1", "x + y", "x - 1"], "4x + 2y - 2"),
    ("6c", "una figura de ocho lados que miden $2x$, $10x - 30$, $5x - 20$, $x + 10$, $x$, "
           "$4x - 10$, $7x - 50$ y $2x$",
     ["2x", "10x - 30", "5x - 20", "x + 10", "x", "4x - 10", "7x - 50", "2x"], "32x - 100"),
    ("6d", "un triángulo cuyos lados miden $a^{2} - a + 2$, $3a^{2} - 2a - 1$ y "
           "$a^{2} + 2a - 2$",
     ["a^2 - a + 2", "3a^2 - 2a - 1", "a^2 + 2a - 2"], "5a^2 - a - 1"),
]
for lit, fig, lados, r in PERIMETROS:
    @ejercicio(id=nuevo_id(), tipo="contexto", dificultad=2, fuente=f"{FUENTE} {lit}",
               dba=["matematicas-8-9", "matematicas-8-4"],
               tema=COMUN["tema"], grados=[8],
               enunciado=f"Escribe un polinomio para el perímetro de {fig}. Simplifícalo "
                         f"reduciendo los términos semejantes.",
               respuesta=f"$P = {ltx(r)}$.",
               notas=("En el módulo, la descripción de la figura dice «a al cuadrado, - a + 2»; "
                      "se interpreta como a^2 - a + 2." if lit == "6d" else
                      "Las medidas se toman de la descripción de la imagen del módulo."))
    def _(lados=lados, r=r):
        assert expand(sum(expresion(l) for l in lados) - expresion(r)) == 0


# ---------- 7. Términos y coeficientes ----------
TERMINOS = [
    ("7a", ["-4m^9", "6m", "-1"], ["-4", "6", "-1"]),
    ("7b", ["a^5", "4a^3", "-3a^2", "a"], ["1", "4", "-3", "1"]),
    ("7c", ["2x^2 y", "5x y^2", "-6y^4"], ["2", "5", "-6"]),
    ("7d", ["m^4 n^3", "-3m^3 n^2", "6m^2 n^4"], ["1", "-3", "6"]),
    ("7e", ["8p^3", "2p q", "-4"], ["8", "2", "-4"]),
    ("7f", ["a^4 b^6", "-2a^6 b^4"], ["1", "-2"]),
    ("7g", ["-3n^6", "3n", "-3"], ["-3", "3", "-3"]),
    ("7h", ["x^6", "-2x^5", "3x^2", "-2x", "-4"], ["1", "-2", "3", "-2", "-4"]),
    ("7i", ["x^8 y^6", "-2x^6 y^6", "8x^4 y^7", "-4x y^8"], ["1", "-2", "8", "-4"],
     "El texto alternativo dice «menos x elevado a la 4 y elevado a la 7»; se conserva la "
     "fórmula impresa, +8x^4y^7."),
    ("7j", ["12m^12", "-8m^11 n^10", "5m^5 n^11", "-m^4 n^12", "n^14"], ["12", "-8", "5", "-1", "1"]),
    ("7k", ["4x y^2", "2x^2 y", "-x y^2", "3x^2 y"], ["4", "2", "-1", "3"]),
    ("7l", ["6x^2", "5x y^2", "2x^2", "-3x y^2"], ["6", "5", "2", "-3"],
     "En el módulo la fórmula es ilegible; se reconstruyó con su texto alternativo."),
    ("7m", ["-3x^4", "-6x^4", "-5"], ["-3", "-6", "-5"],
     "En el módulo la fórmula es ilegible; se reconstruyó con su texto alternativo."),
    ("7n", ["8x", "-3x^2", "9", "-8x^3"], ["8", "-3", "9", "-8"]),
    ("7o", ["5x^4 y", "-x^2 y", "-x", "2"], ["5", "-1", "-1", "2"]),
    ("7p", ["-5x^4 y^5", "6x^3 y^6", "-3x^2 y^2"], ["-5", "6", "-3"]),
    ("7q", ["-7x^3 y^3", "6x^2 y^2", "3x y", "7"], ["-7", "6", "3", "7"]),
    ("7r", ["(3/4)x^3", "-(2/3)x", "1"], ["(3/4)", "-(2/3)", "1"]),
    ("7s", ["(1/5)x^2", "-(1/4)x"], ["(1/5)", "-(1/4)"]),
]
for lit, ts, cs, *nota in TERMINOS:
    s = ts[0] + "".join(f" - {t[1:]}" if t.startswith("-") else f" + {t}" for t in ts[1:])

    @ejercicio(id=nuevo_id(), tipo="conceptual", dificultad=1, fuente=f"{FUENTE} {lit}",
               enunciado=f"Identifica los términos de ${ltx(s)}$ y el coeficiente de cada uno.",
               respuesta="; ".join(f"${ltx(t)}$: coeficiente ${ltx(c)}$" for t, c in zip(ts, cs))
                         + ".", **(dict(notas=nota[0]) if nota else {}), **COMUN)
    def _(ts=ts, cs=cs, s=s):
        assert expand(sum(map(expresion, ts)) - expresion(s)) == 0
        for t, c in zip(ts, cs):
            assert expresion(t).as_coeff_Mul()[0] == expresion(c)


# ---------- 8. Signo, coeficiente, parte literal y grado ----------
ELEMENTOS = [
    ("8a", "2x^2 y", "+", "2", "x^{2}y", 3), ("8b", "3x", "+", "3", "x", 1),
    ("8c", "a^2 b^3 c", "+", "1", "a^{2}b^{3}c", 6), ("8d", "(3/4)a", "+", "(3/4)", "a", 1),
    ("8e", "-2x", "-", "-2", "x", 1), ("8f", "-8a^2 c^3 d^3", "-", "-8", "a^{2}c^{3}d^{3}", 8),
    ("8g", "-15x^3", "-", "-15", "x^{3}", 3),
    ("8h", "-(sqrt(3)/3)h^4 k^5", "-", "-(sqrt(3)/3)", "h^{4}k^{5}", 9),
    ("8i", "x y^2/2", "+", "(1/2)", "xy^{2}", 3), ("8j", "-0.7m n^3", "-", "-0.7", "mn^{3}", 4),
    ("8k", "0.2a b^4", "+", "0.2", "ab^{4}", 5),
    ("8l", "(1/4)a b r^3", "+", "(1/4)", "abr^{3}", 5), ("8m", "a b", "+", "1", "ab", 2),
    ("8n", "-(3/5)a b^5", "-", "-(3/5)", "ab^{5}", 6),
]
TEX8 = {"8h": r"-\frac{\sqrt{3}}{3}h^{4}k^{5}", "8i": r"\frac{xy^{2}}{2}"}
TEXC = {"-(sqrt(3)/3)": r"-\frac{\sqrt{3}}{3}"}
NOTAS8 = {"8k": "El texto alternativo dice «b elevado a la 2»; se conserva la fórmula impresa, "
                "b^4.",
          "8m": "En el módulo aparece «Ab» (A mayúscula); se escribe ab."}
for lit, s, sg, c, pl, g in ELEMENTOS:
    @ejercicio(id=nuevo_id(), tipo="conceptual", dificultad=1, fuente=f"{FUENTE} {lit}",
               enunciado=f"Determina el signo, el coeficiente, la parte literal y el grado del "
                         f"término ${TEX8.get(lit, ltx(s))}$.",
               respuesta=f"Signo: {'positivo' if sg == '+' else 'negativo'}; coeficiente: "
                         f"${TEXC.get(c, ltx(c))}$; parte literal: ${pl}$; grado: {g}.",
               **(dict(notas=NOTAS8[lit]) if lit in NOTAS8 else {}), **COMUN)
    def _(s=s, sg=sg, c=c, g=g):
        e = expresion(s)
        coef, _lit = e.as_independent(*e.free_symbols, as_Add=False)
        assert simplify(coef - expresion(c)) == 0 and (coef > 0) == (sg == "+")
        assert Poly(e, *sorted(e.free_symbols, key=str)).total_degree() == g


# ---------- 9–11. Lenguaje algebraico ----------
m, n, x, y = symbols("m n x y", real=True)


@ejercicio(id=nuevo_id(), tipo="calculo", dificultad=1, fuente=f"{FUENTE} 9",
           enunciado=r"Expresa en lenguaje algebraico: «La suma de un número y $2$ se multiplica "
                     r"por ese número y después se resta $3$ al resultado».",
           respuesta=r"Si el número es $x$: $(x + 2)x - 3$, es decir, $x^{2} + 2x - 3$.", **COMUN)
def _():
    assert expand((x + 2) * x - 3 - (x**2 + 2 * x - 3)) == 0
    assert ((x + 2) * x - 3).subs(x, 5) == 32          # (5 + 2)·5 − 3


FRASES10 = [
    ("10a", "El número que es cinco veces un número $x$.", "5x", 5 * x),
    ("10b", "El número que equivale al doble de $y$ más tres.", "2y + 3", 2 * y + 3),
    ("10c", "El número que es cinco más que $x$.", "x + 5", x + 5),
    ("10d", "El número que es ocho menos que $y$.", "y - 8", y - 8),
    ("10e", "El número correspondiente a la mitad de la suma de $x$ y $y$.", None, (x + y) / 2),
]
for lit, frase, r, ind in FRASES10:
    rt = r"\frac{x + y}{2}" if r is None else ltx(r)

    @ejercicio(id=nuevo_id(), tipo="calculo", dificultad=1, fuente=f"{FUENTE} {lit}",
               enunciado=f"Expresa mediante una expresión algebraica: {frase}",
               respuesta=f"${rt}$.", **COMUN)
    def _(r=r, ind=ind):
        e = (x + y) / 2 if r is None else expresion(r)
        assert simplify(e - ind) == 0


FRASES11 = [
    ("11a", "Su suma.", "m + n", m + n), ("11b", "El cuadrado de su suma.", "(m + n)^2", (m + n)**2),
    ("11c", "Su diferencia.", "m - n", m - n),
    ("11d", "El cubo de su diferencia.", "(m - n)^3", (m - n)**3),
    ("11e", "Su producto.", "m n", m * n),
    ("11f", "La diferencia de sus cubos.", "m^3 - n^3", m**3 - n**3),
    ("11g", "Su cociente.", None, m / n),
    ("11h", "La raíz cuadrada de la suma de sus cuadrados.", None, sqrt(m**2 + n**2)),
    ("11i", "La suma de sus cuadrados.", "m^2 + n^2", m**2 + n**2),
    ("11j", "El doble de su producto.", "2m n", 2 * m * n),
]
T11 = {"11g": r"\frac{m}{n}\ (n \neq 0)", "11h": r"\sqrt{m^{2} + n^{2}}"}
for lit, frase, r, ind in FRASES11:
    @ejercicio(id=nuevo_id(), tipo="calculo", dificultad=1, fuente=f"{FUENTE} {lit}",
               enunciado=f"Simboliza la operación entre dos números $m$ y $n$: {frase}",
               respuesta=f"${T11.get(lit) or ltx(r)}$.", **COMUN)
    def _(r=r, ind=ind, lit=lit):
        e = {"11g": m / n, "11h": sqrt(m**2 + n**2)}.get(lit) if r is None else expresion(r)
        assert simplify(e - ind) == 0
        assert e.subs({m: 3, n: 4}) == ind.subs({m: 3, n: 4})


# ---------- 12. Operaciones combinadas ----------
OPS = [
    ("12a", r"8 + 3 \cdot 4", 8 + 3 * 4, 20,
     "En el módulo el producto se escribe con una «X»; se usa el punto."),
    ("12b", r"(5 + 10) \div 5", Rational(5 + 10, 5), 3, None),
    ("12c", r"(9 + 5) \cdot 2", (9 + 5) * 2, 28, None),
    ("12d", r"\dfrac{6 + 5 \cdot 3}{6 + 1}", Rational(6 + 5 * 3, 6 + 1), 3, None),
    ("12e", r"6 - 3 \div 3", 6 - Rational(3, 3), 5, None),
    ("12f", r"\dfrac{8 + 3 \cdot 2}{4 + 3}", Rational(8 + 3 * 2, 4 + 3), 2, None),
]
for lit, t, val, r, nota in OPS:
    @ejercicio(id=nuevo_id(), tipo="calculo", dificultad=1, fuente=f"{FUENTE} {lit}",
               enunciado=f"Efectúa las operaciones indicadas y simplifica: ${t}$.",
               respuesta=f"${r}$.", **(dict(notas=nota) if nota else {}), **COMUN)
    def _(val=val, r=r):
        assert val == r


# ---------- 13. Valor numérico con t = 6, x = 3, y = 4, z = 5 ----------
VALORES = {"t": 6, "x": 3, "y": 4, "z": 5}
EVAL13 = [
    ("13a", "2(x + 7)", 20), ("13b", "5y - 3", 17), ("13c", "(18 - 4)x", 42),
    ("13d", "7z + 8", 43), ("13e", "z(t - y)", 10), ("13f", "4(x z + 3y)", 108),
    ("13g", "9x y z - t", 534), ("13h", "5(3y - 4x)", 0), ("13i", "6y - 2x y", 0),
    ("13j", "x y z - 4z", 40), ("13k", "(y y + z)z", 105), ("13l", "(9x + z)/(x + z)", 4),
    ("13m", "(4y - 2t)/(y + 2t)", Rational(1, 4)), ("13n", "(10t - z)/(10(t - z))", Rational(11, 2)),
    ("13o", "2(y + x)/(2y + x)", Rational(14, 11)), ("13p", "2(x + 4(y + z))", 78),
    ("13q", "3(z + 5(2y - x))", 90), ("13r", "((5y + 6z) - 36) + y", 18),
    ("13s", "2t - (7z + (y + x))", -30), ("13t", "5z + 8x - 3y", 37),
    ("13u", "4x y - 5x^2 y", -132),
]
TEX13 = {"13k": "(yy + z)z", "13l": r"\dfrac{9x + z}{x + z}", "13m": r"\dfrac{4y - 2t}{y + 2t}",
         "13n": r"\dfrac{10t - z}{10(t - z)}", "13o": r"\dfrac{2(y + x)}{2y + x}",
         "13p": "2[x + 4(y + z)]", "13q": "3[z + 5(2y - x)]", "13r": "[(5y + 6z) - 36] + y",
         "13s": "2t - [7z + (y + x)]"}
NOTAS13 = {"13e": "En el módulo aparece «Z(t – y)» (Z mayúscula); se escribe z.",
           "13j": "En el módulo aparece «Xyz – 4z» (X mayúscula); se escribe x."}
for lit, s, r in EVAL13:
    @ejercicio(id=nuevo_id(), tipo="calculo", dificultad=1 if "/" not in s else 2,
               fuente=f"{FUENTE} {lit}",
               enunciado=f"Evalúa ${TEX13.get(lit, ltx(s))}$ si $t = 6$, $x = 3$, $y = 4$ y "
                         f"$z = 5$.",
               respuesta=(rf"$\frac{{{r.p}}}{{{r.q}}}$." if isinstance(r, Rational) and r.q != 1
                          else f"${r}$."),
               **(dict(notas=NOTAS13[lit]) if lit in NOTAS13 else {}), **COMUN)
    def _(s=s, r=r):
        e = expresion(s)
        assert e.subs({sym: VALORES[str(sym)] for sym in e.free_symbols}) == r


# ---------- 14. Fórmulas ----------
FORMULAS = [
    ("14a", r"Perímetro de un paralelogramo: $2(a + b)$, si $a = \num{7,5}$ y $b = \num{19,5}$.",
     "2(a + b)", {"a": "7.5", "b": "19.5"}, "$54$.", 54, None),
    ("14b", r"Perímetro de un trapecio isósceles: $2a + b + c$, si $a = 16$, $b = 20$ y $c = 48$.",
     "2a + b + c", {"a": 16, "b": 20, "c": 48}, "$100$.", 100, None),
    ("14c", r"Área de un trapecio: $\frac{1}{2}h(b + c)$, si $h = 12$, $b = 16$ y $c = 48$.",
     "(1/2)h(b + c)", {"h": 12, "b": 16, "c": 48}, "$384$.", 384,
     "En el módulo sobra un paréntesis: «½ h ( b +c ) )»."),
    ("14d", r"Área de un círculo: $\pi r^{2}$, si $r = 28$.",
     "pi r^2", {"r": 28}, r"$784\pi \approx \num{2463,01}$.", 784 * pi,
     "En el módulo dice «s r = 28»; se escribe «si r = 28»."),
    ("14e", r"Área total de un prisma: $2(lw + wh + lh)$, si $l = 14$, $w = 12$ y $h = 10$.",
     "2(l w + w h + l h)", {"l": 14, "w": 12, "h": 10}, "$856$.", 856, None),
]
for lit, enun, s, vals, resp, r, nota in FORMULAS:
    @ejercicio(id=nuevo_id(), tipo="contexto", dificultad=1, fuente=f"{FUENTE} {lit}",
               enunciado=f"Evalúa la expresión con los valores dados. {enun}", respuesta=resp,
               **(dict(notas=nota) if nota else {}), tema=COMUN["tema"], grados=[8],
               dba=["matematicas-8-9", "matematicas-8-4"])
    def _(s=s, vals=vals, r=r):
        e = expresion(s)
        v = e.subs({sym: Rational(str(vals[str(sym)])) for sym in e.free_symbols})
        assert simplify(v - r) == 0
        if "pi" in s:
            assert abs(float(v) - 2463.01) < 0.005


# ---------- 15. Tabla de valores ----------
FILAS15 = [(2, 3, 4, 12, 18, 5, 1), (-1, 4, 1, -6, -12, 3, -6), (5, -2, 25, 30, -30, 3, 12),
           (-4, 6, 16, -24, -72, 2, -14), (0, 5, 0, 0, 0, 5, -5)]


@ejercicio(id=nuevo_id(), tipo="calculo", dificultad=1, fuente=f"{FUENTE} 15",
           enunciado=r"Completa la tabla reemplazando $x$ y $y$ por los valores indicados. "
                     r"\begin{center}\begin{tabular}{|c|c|c|c|c|c|c|} \hline $x$ & $y$ & $x^{2}$ & "
                     r"$6x$ & $3xy$ & $x + y$ & $2x - y$ \\ \hline "
                     + " ".join(f"${f[0]}$ & ${f[1]}$ & & & & & \\\\ \\hline" for f in FILAS15)
                     + r" \end{tabular}\end{center}",
           respuesta="Por filas ($x^{2}$, $6x$, $3xy$, $x + y$, $2x - y$): "
                     + "; ".join(f"$({f[0]}, {f[1]})$: " + ", ".join(f"${v}$" for v in f[2:])
                                 for f in FILAS15) + ".",
           notas="En el módulo la columna dice «X al cuadrado»; se escribe x^2.", **COMUN)
def _():
    for a, b, *vals in FILAS15:
        assert [a**2, 6 * a, 3 * a * b, a + b, 2 * a - b] == vals


# ---------- 16. ¿Se satisface la igualdad? ----------
IGUALDADES = [
    ("16a", "5x - 2y", 23, {"x": "7", "y": "-6"}, False),
    ("16b", "3a - 5b", 21, {"a": "2", "b": "-3"}, True),
    ("16c", "3a - 4b", 11, {"a": "-5/3", "b": "-4"}, True),
    ("16d", "3m - 2n", 6, {"m": "5/3", "n": "-1/2"}, True),
    ("16e", "4m - 5n", 9, {"m": "1", "n": "-1"}, True),
    ("16f", "2x + 3y", 13, {"x": "5", "y": "1"}, True),
    ("16g", "3a - 2b", 13, {"a": "3", "b": "-2"}, True),
    ("16h", "5x - 4y", 9, {"x": "-3", "y": "-6"}, True),
    ("16i", "x^2 - 3y^2", 15, {"x": "4", "y": "-1"}, False),
]


def tex_valor(v):
    if "/" in v:
        a, b = v.lstrip("-").split("/")
        return ("-" if v.startswith("-") else "") + rf"\frac{{{a}}}{{{b}}}"
    return v


for lit, s, k, vals, ok in IGUALDADES:
    e = expresion(s)
    obtenido = e.subs({sym: Rational(vals[str(sym)]) for sym in e.free_symbols})
    asign = ", ".join(f"${v} = {tex_valor(vals[v])}$" for v in vals)

    @ejercicio(id=nuevo_id(), tipo="calculo", dificultad=1, fuente=f"{FUENTE} {lit}",
               dba=["matematicas-8-9", "matematicas-8-3"], tema=COMUN["tema"], grados=[8],
               enunciado=f"Reemplaza {asign} en ${ltx(s)} = {k}$ y determina si la igualdad se "
                         f"satisface.",
               respuesta=(f"El primer miembro vale ${obtenido}$: "
                          + ("sí se satisface." if ok else f"no se satisface (${obtenido} \\neq {k}$).")))
    def _(s=s, k=k, vals=vals, ok=ok):
        e = expresion(s)
        v = e.subs({sym: Rational(vals[str(sym)]) for sym in e.free_symbols})
        assert (v == k) == ok


# ---------- 17. Tres pares que satisfacen la igualdad ----------
PARES = [
    ("17a", "2x + y", 6, [(0, 6), (1, 4), (3, 0)]),
    ("17b", "5x + y", 7, [(0, 7), (1, 2), (2, -3)]),
    ("17c", "3x + 7y", 7, [(0, 1), (7, -2), (-7, 4)]),
    ("17d", "x + 3y", 9, [(0, 3), (3, 2), (9, 0)]),
    ("17e", "3x + 2y", 8, [(0, 4), (2, 1), (4, -2)]),
    ("17f", "x + 2y", 9, [(1, 4), (3, 3), (9, 0)]),
    ("17g", "2x + 5y", 10, [(0, 2), (5, 0), (-5, 4)]),
    ("17h", "3x + y", 7, [(0, 7), (1, 4), (2, 1)]),
    ("17i", "5x y", 30, [(1, 6), (2, 3), (-1, -6)]),
    ("17j", "3x y", 9, [(1, 3), (3, 1), (-1, -3)]),
    ("17k", "x y", 12, [(3, 4), (2, 6), (-3, -4)]),
    ("17l", "x y + 7", 23, [(2, 8), (4, 4), (1, 16)]),
    ("17m", "x y", 4, [(1, 4), (2, 2), (-1, -4)]),
    ("17n", "(x + 2)y", 5, [(3, 1), (-1, 5), (0, Rational(5, 2))]),
    ("17o", "(4 - x)y", 4, [(3, 4), (2, 2), (0, 1)]),
    ("17p", "(x + 6)y", 7, [(1, 1), (-5, 7), (0, Rational(7, 6))]),
]
NOTAS17 = {"17k": "En el módulo aparece «Xy = 12» (X mayúscula); se escribe xy.",
           "17o": "En el módulo aparece «(4 - x) = 4», sin la y (solo tendría la solución x = 0); "
                  "se corrigió a (4 - x)y = 4 como en los literales vecinos.",
           "17p": "En el módulo aparece «(x + 6) = 7», sin la y; se corrigió a (x + 6)y = 7."}


def tex_num(v):
    v = Rational(v)
    return rf"\frac{{{v.p}}}{{{v.q}}}" if v.q != 1 else str(v)


for lit, s, k, pares in PARES:
    @ejercicio(id=nuevo_id(), tipo="calculo", dificultad=1, fuente=f"{FUENTE} {lit}",
               dba=["matematicas-8-9", "matematicas-8-3"], tema=COMUN["tema"], grados=[8],
               enunciado=f"Encuentra tres pares de valores de $x$ y $y$ que satisfagan "
                         f"${ltx(s)} = {k}$.",
               respuesta="Por ejemplo, " + ", ".join(f"$({tex_num(a)}, {tex_num(b)})$"
                                                     for a, b in pares)
                         + " (hay infinitos pares; se comprueba reemplazando).",
               **(dict(notas=NOTAS17[lit]) if lit in NOTAS17 else {}))
    def _(s=s, k=k, pares=pares):
        e = expresion(s)
        assert len(set(pares)) == 3
        for a, b in pares:
            assert e.subs({x: a, y: b}) == k


# ---------- Prepárate para el ICFES ----------
C, F = symbols("C F", real=True)
TEMP = (r"La relación entre la escala de grados centígrados $C$ y la de grados Fahrenheit $F$ "
        r"está dada por las fórmulas $F = \frac{9}{5}C + 32$ y $C = \frac{5F - 160}{9}$. ")


@ejercicio(id=nuevo_id(), tipo="seleccion", dificultad=1, fuente=f"{ICFES} 3",
           tema=COMUN["tema"], grados=[8], dba=["matematicas-8-9", "matematicas-8-8"],
           enunciado=TEMP + r"Si una señora está cocinando una torta en el horno a una temperatura "
                     r"de $350\,^{\circ}$C, la temperatura del horno en grados Fahrenheit es:"
                     + opciones("$600$", "$598$", "$632$", "$662$"),
           respuesta=r"d. $662\,^{\circ}$F, porque $\frac{9}{5}\cdot 350 + 32 = 630 + 32 = 662$.")
def _():
    f = Rational(9, 5) * 350 + 32
    assert [f == o for o in (600, 598, 632, 662)] == [False, False, False, True]


@ejercicio(id=nuevo_id(), tipo="seleccion", dificultad=1, fuente=f"{ICFES} 4",
           tema=COMUN["tema"], grados=[8], dba=["matematicas-8-9", "matematicas-8-8"],
           enunciado=TEMP + r"Si un termómetro en grados Fahrenheit marca $32$ al medir la "
                     r"temperatura de cierto líquido, la temperatura en grados centígrados es:"
                     + opciones("$-32$", "$32$", "$0$", "No se puede determinar."),
           respuesta=r"c. $0\,^{\circ}$C, porque $\frac{5 \cdot 32 - 160}{9} = 0$.")
def _():
    c = Rational(5 * 32 - 160, 9)
    assert c == 0 and c not in (-32, 32)


@ejercicio(id=nuevo_id(), tipo="argumentacion", dificultad=2, fuente=f"{ICFES} 5",
           tema=COMUN["tema"], grados=[8], dba=["matematicas-8-8", "matematicas-8-10"],
           enunciado=TEMP + r"¿Se puede afirmar que la temperatura en grados centígrados es "
                     r"directamente proporcional a la temperatura en grados Fahrenheit? Explica.",
           respuesta=r"No. En una proporcionalidad directa el cociente $\frac{F}{C}$ es constante "
                     r"y a $C = 0$ le corresponde $F = 0$; aquí a $0\,^{\circ}$C le corresponden "
                     r"$32\,^{\circ}$F, y al duplicar $C$ de $10$ a $20$, $F$ pasa de $50$ a $68$, "
                     r"no se duplica. La relación es lineal, pero no proporcional.")
def _():
    f = lambda c: Rational(9, 5) * c + 32
    assert f(0) == 32 and f(10) == 50 and f(20) == 68 and f(20) != 2 * f(10)
    assert f(10) / 10 != f(20) / 20
