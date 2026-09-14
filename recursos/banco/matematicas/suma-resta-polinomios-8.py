"""Banco de ejercicios — Matemáticas 8° — Adición y sustracción de polinomios; signos de agrupación.
Fuente: módulo de Matemáticas 8° de las Guías de Apoyo (Adriana Quintero Palomino), Tema 2;
se lee en recursos/matematicas/Guías pedagógicas Matemáticas/markdown/08 - Modulo_Matematicas_Octavo.md
(«Practica lo aprendido» de la sección «Sustracción de polinomios»).
No incluidos por estar repetidos en el módulo: 1j (= 1c, q(a) + t(a)), 2n (= 2g, p(x) + p(x) + p(x)),
2p (= 2e, q(x) + t(x)) y 7c (le sobra un corchete; sin él es idéntico a 7d).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/suma-resta-polinomios-8.py
"""
import re

from sympy import Add, expand

from ejercicios import ejercicio, expresion

FUENTE = ("módulo 8° (Quintero Palomino), Tema 2, Expresiones algebraicas, Sustracción de "
          "polinomios — Practica lo aprendido")
COMUN = dict(tema="adición y sustracción de polinomios", grados=[8], dba=["matematicas-8-9"])
PREFIJO = "suma-resta-polinomios-8"
_n = 0


def nuevo_id():
    global _n
    _n += 1
    return f"{PREFIJO}-{_n:03d}"


def ltx(s):
    """LaTeX de un texto «llano» escrito para expresion()."""
    s = re.sub(r"\((-?)(\d+)/(\d+)\)", lambda m: f"{m[1]}\\frac{{{m[2]}}}{{{m[3]}}}", s)
    s = re.sub(r"\^\(([^()]*)\)", r"^{\1}", s)
    s = re.sub(r"\^(\d+)", r"^{\1}", s)
    s = re.sub(r"(\d)\.(\d)", r"\1{,}\2", s)
    return re.sub(r"(?<=[\w})]) (?=[\w\\(])", "", s)


def py(latex):
    """Texto para expresion() a partir del LaTeX de los ejercicios de signos de agrupación."""
    s = latex.replace(r"\{", "(").replace(r"\}", ")").replace("[", "(").replace("]", ")")
    return re.sub(r"(?<=[a-z])(?=[a-z])", " ", s)


def serie_polinomios(lit0, polis, var, operaciones, dificultad=1):
    """polis: {nombre: polinomio}; operaciones: (literal, operación en Python con p, q, r, t,
    LaTeX de la operación o None, resultado escrito a mano[, notas])."""
    defin = ", ".join(f"${k}({var}) = {ltx(v)}$" for k, v in polis.items())
    for lit, op, op_tex, r, *nota in operaciones:
        if op_tex is None:
            op_tex = re.sub(r"\b([pqrt])\b", rf"\1({var})", op).replace("*", "")

        @ejercicio(id=nuevo_id(), tipo="calculo", dificultad=dificultad,
                   fuente=f"{FUENTE} {lit0}{lit}",
                   enunciado=f"Considera los polinomios {defin}. Calcula ${op_tex}$.",
                   respuesta=f"${ltx(r)}$.", **(dict(notas=nota[0]) if nota else {}), **COMUN)
        def _(op=op, r=r):
            valores = {k: expresion(v) for k, v in polis.items()}
            assert expand(eval(op, {}, valores) - expresion(r)) == 0


# ---------- 1 ----------
serie_polinomios("1", {"p": "3a - a^3 + 4a^4", "q": "6a^5 - 2a^3", "r": "7a^3 - 6a^4 - 2",
                       "t": "a^3 - a^2 + 7a^5"}, "a", [
    ("a", "p + q", None, "6a^5 + 4a^4 - 3a^3 + 3a"),
    ("b", "r + t", None, "7a^5 - 6a^4 + 8a^3 - a^2 - 2"),
    ("c", "q + t", None, "13a^5 - a^3 - a^2"),
    ("d", "p + t + q", None, "13a^5 + 4a^4 - 2a^3 - a^2 + 3a"),
    ("e", "p + r", None, "-2a^4 + 6a^3 + 3a - 2"),
    ("f", "p + q + r", None, "6a^5 - 2a^4 + 4a^3 + 3a - 2"),
    ("g", "r + t + q", None, "13a^5 - 6a^4 + 6a^3 - a^2 - 2"),
    ("h", "p + q + r + r", None, "6a^5 - 8a^4 + 11a^3 + 3a - 4"),
    ("i", "q + p", None, "6a^5 + 4a^4 - 3a^3 + 3a"),
    ("k", "q + r", None, "6a^5 - 6a^4 + 5a^3 - 2"),
    ("l", "p + r + q", None, "6a^5 - 2a^4 + 4a^3 + 3a - 2"),
    ("m", "p + t", None, "7a^5 + 4a^4 - a^2 + 3a"),
    ("n", "p + r + t", None, "7a^5 - 2a^4 + 7a^3 - a^2 + 3a - 2"),
    ("o", "t + t + q", None, "20a^5 - 2a^2"),
    ("p", "p + p + r", None, "2a^4 + 5a^3 + 6a - 2"),
    ("q", "5*p - 3*q", None, "-18a^5 + 20a^4 + a^3 + 15a"),
    ("r", "3*p + 5*t", None, "35a^5 + 12a^4 + 2a^3 - 5a^2 + 9a"),
])

# ---------- 2 ----------
serie_polinomios("2", {"p": "(3/4)x^3 - (2/3)x + 1", "q": "(1/5)x^2 - (1/4)x",
                       "r": "(2/3)x - 4", "t": "(1/4)x^2 + 5"}, "x", [
    ("a", "p + q", None, "(3/4)x^3 + (1/5)x^2 - (11/12)x + 1"),
    ("b", "r + p", None, "(3/4)x^3 - 3"),
    ("c", "r + q", None, "(1/5)x^2 + (5/12)x - 4"),
    ("d", "r + p + q", None, "(3/4)x^3 + (1/5)x^2 - (1/4)x - 3"),
    ("e", "q + t", None, "(9/20)x^2 - (1/4)x + 5"),
    ("f", "t + p + q", None, "(3/4)x^3 + (9/20)x^2 - (11/12)x + 6"),
    ("g", "p + p + p", None, "(9/4)x^3 - 2x + 3"),
    ("h", "t + t + t", None, "(3/4)x^2 + 15"),
    ("i", "q + p", None, "(3/4)x^3 + (1/5)x^2 - (11/12)x + 1"),
    ("j", "p + t", None, "(3/4)x^3 + (1/4)x^2 - (2/3)x + 6"),
    ("k", "t + r", None, "(1/4)x^2 + (2/3)x + 1"),
    ("l", "p + r + t", None, "(3/4)x^3 + (1/4)x^2 + 2"),
    ("m", "p + p", None, "(3/2)x^3 - (4/3)x + 2"),
    ("o", "t + t + q", None, "(7/10)x^2 - (1/4)x + 10"),
    ("q", "12*p - 4*t", None, "9x^3 - x^2 - 8x - 8"),
    ("r", "20*q + 3*r", None, "4x^2 - 3x - 12"),
], dificultad=2)

# ---------- 3 ----------
serie_polinomios("3", {"p": "3x y - 5y^2 + 6x^2", "q": "3y^2 - 2x y + x^2",
                       "r": "5x^2 - 3y^2 + 2x y"}, "x, y", [
    ("a", "p + q + q + p", None, "14x^2 + 2x y - 4y^2"),
    ("b", "p + p", None, "12x^2 + 6x y - 10y^2"),
    ("c", "p + r", None, "11x^2 + 5x y - 8y^2"),
    ("d", "(r + p) + q", r"[r(x, y) + p(x, y)] + q(x, y)", "12x^2 + 3x y - 5y^2"),
    ("e", "q + r", None, "6x^2"),
    ("f", "(p + q) + (p + r)", r"[p(x, y) + q(x, y)] + [p(x, y) + r(x, y)]",
     "18x^2 + 6x y - 10y^2"),
    ("g", "p + q + r", None, "12x^2 + 3x y - 5y^2"),
    ("h", "((q + r) + p) + r", r"\{[q(x, y) + r(x, y)] + p(x, y)\} + r(x, y)",
     "17x^2 + 5x y - 8y^2",
     "En el módulo aparece «g(x, y)», polinomio que no está definido; se corrigió a q(x, y)."),
])

# ---------- 4 y 5. Resta de monomios: (literal, enunciado, minuendo, sustraendo, resultado) ----------
RESTAS = [
    ("4a", "De {A} resta {B}.", "-2a^2 b", "41a^2 b", "-43a^2 b"),
    ("4b", "Resta {B} de {A}.", "16m^2 n", "46m^2 n", "-30m^2 n"),
    ("4c", "Resta {B} de {A}.", "-x^3 y", "x^3 y", "-2x^3 y"),
    ("4d", "De {A} resta {B}.", "107u v", "109u v", "-2u v"),
    ("4e", "De {A} resta {B}.", "-6x^2 y^2", "11x^2 y^2", "-17x^2 y^2"),
    ("4f", "Resta {B} de {A}.", "-83x y", "-16x y", "-67x y"),
    ("4g", "Resta {B} de {A}.", "16a^2 b^3", "-24a^2 b^3", "40a^2 b^3"),
    ("4h", "De {A} resta {B}.", "89t v", "-48t v", "137t v"),
    ("4i", "De {A} resta {B}.", "49y^9", "-23y^9", "72y^9"),
    ("4j", "Resta {B} de {A}.", "11t^4", "-113t^4", "124t^4"),
    ("5a", "De {A} resta {B}.", "-(1/2)a^2 b", "(1/4)a^2 b", "-(3/4)a^2 b"),
    ("5b", "Resta {B} de {A}.", "-(1/2)x^3 y", "(2/3)x^3 y", "-(7/6)x^3 y"),
    ("5c", "Resta {B} de {A}.", "(1/6)m^2 n", "(2/3)m^2 n", "-(1/2)m^2 n"),
    ("5d", "Resta {B} de {A}.", "-72f^2 g", "6f^2 g", "-78f^2 g"),
    ("5e", "De {A} resta {B}.", "-(1/6)x^2 y^2", "(1/11)x^2 y^2", "-(17/66)x^2 y^2"),
    ("5f", "De {A} resta {B}.", "5p y^2", "5p y^2", "0"),
    ("5g", "Resta {B} de {A}.", "(1/6)a^2 b^3", "-(1/2)a^2 b^3", "(2/3)a^2 b^3"),
    ("5h", "Resta {B} de {A}.", "-(1/6)v^3 m", "(3/2)v^3 m", "-(5/3)v^3 m"),
    ("5i", "De {A} resta {B}.", "(4/9)y^9", "-(2/3)y^9", "(10/9)y^9"),
    ("5j", "Resta {B} de {A}.", "-12v w", "-9v w", "-3v w"),
]
for lit, frase, a, b, r in RESTAS:
    instr = ("Escribe la operación correspondiente y halla la resta. " if lit[0] == "4"
             else "Resta los monomios semejantes. ")

    @ejercicio(id=nuevo_id(), tipo="calculo", dificultad=1 if lit[0] == "4" else 2,
               fuente=f"{FUENTE} {lit}",
               enunciado=instr + frase.format(A=f"${ltx(a)}$", B=f"${ltx(b)}$"),
               respuesta=f"${ltx(a)} - ({ltx(b)}) = {ltx(r)}$.", **COMUN)
    def _(a=a, b=b, r=r):
        assert expand(expresion(a) - expresion(b) - expresion(r)) == 0


# ---------- 6 ----------
serie_polinomios("6", {"p": "3a - a^3 + 4a^4 - 5a^2 + 6", "q": "6a^4 - 2a^3 - 8",
                       "r": "7a^3 + 8a^4 + 5", "t": "5a^4 - 6a^2 + 7a^3 + 8a - 5"}, "a", [
    ("a", "p - t", None, "-a^4 - 8a^3 + a^2 - 5a + 11"),
    ("b", "p + q", None, "10a^4 - 3a^3 - 5a^2 + 3a - 2"),
    ("c", "q - r", None, "-2a^4 - 9a^3 - 13"),
    ("d", "t - p", None, "a^4 + 8a^3 - a^2 + 5a - 11"),
    ("e", "r - t", None, "3a^4 + 6a^2 - 8a + 10"),
    ("f", "-p + q - t", None, "-3a^4 - 8a^3 + 11a^2 - 11a - 9"),
    ("g", "-(-(p + t)) + r", r"-[-(p(a) + t(a))] + r(a)", "17a^4 + 13a^3 - 11a^2 + 11a + 6"),
    ("h", "-(q + (t - r)) + p", r"-\{q(a) + [t(a) - r(a)]\} + p(a)", "a^4 + a^3 + a^2 - 5a + 24"),
], dificultad=2)

# ---------- 7 ----------
serie_polinomios("7", {"p": "3z^2 - 2z + 0.5", "q": "5z^3 + 2z^2 - 1.2",
                       "r": "4z^3 - 5z^2 + z + 3.4"}, "z", [
    ("a", "(p + q) - (r - p)", r"[p(z) + q(z)] - [r(z) - p(z)]", "z^3 + 13z^2 - 5z - 3.6"),
    ("b", "p - (-r + (q - p) + p)", r"p(z) - [-r(z) + (q(z) - p(z)) + p(z)]",
     "-z^3 - 4z^2 - z + 5.1", "En el módulo la expresión está encerrada entre llaves "
                              "sobrantes; se quitaron."),
    ("d", "-p - (-p + p) + p", r"-p(z) - [-p(z) + p(z)] + p(z)", "0"),
    ("e", "(p + q) - r", r"[p(z) + q(z)] - r(z)", "z^3 + 10z^2 - 3z - 4.1"),
    ("f", "(p - r) + q", r"[p(z) - r(z)] + q(z)", "z^3 + 10z^2 - 3z - 4.1"),
    ("g", "p - (q - r)", r"p(z) - [q(z) - r(z)]", "-z^3 - 4z^2 - z + 5.1"),
    ("h", "(p - q) - (r - q)", r"[p(z) - q(z)] - [r(z) - q(z)]", "-4z^3 + 8z^2 - 3z - 2.9"),
    ("i", "(p + q) - (r + q)", r"[p(z) + q(z)] - [r(z) + q(z)]", "-4z^3 + 8z^2 - 3z - 2.9"),
], dificultad=2)

# ---------- 8. Propiedades ----------
P8 = {"p": "(2/3)x^2 - 5x + (3/5)", "q": "(3/4)x + 5x^2 - (2/3)", "r": "5 - (3/2)x^2 + (1/5)x"}
DEF8 = "Considera los polinomios " + ", ".join(f"${k}(x) = {ltx(v)}$" for k, v in P8.items()) + ". "


def v8():
    return {k: expresion(v) for k, v in P8.items()}


@ejercicio(id=nuevo_id(), tipo="calculo", dificultad=2, fuente=f"{FUENTE} 8a",
           enunciado=DEF8 + r"Verifica que $p(x) + q(x)$ y $q(x) + p(x)$ dan el mismo resultado.",
           respuesta=r"Las dos sumas dan $\frac{17}{3}x^{2} - \frac{17}{4}x - \frac{1}{15}$ "
                     r"(propiedad conmutativa).", **COMUN)
def _():
    p, q, r = v8().values()
    esperado = expresion("(17/3)x^2 - (17/4)x - (1/15)")
    assert expand(p + q - esperado) == 0 and expand(q + p - esperado) == 0


@ejercicio(id=nuevo_id(), tipo="calculo", dificultad=2, fuente=f"{FUENTE} 8b",
           enunciado=DEF8 + r"Verifica que $p(x) + [q(x) + r(x)]$ es igual a "
                     r"$[p(x) + q(x)] + r(x)$.",
           respuesta=r"Las dos dan $\frac{25}{6}x^{2} - \frac{81}{20}x + \frac{74}{15}$ "
                     r"(propiedad asociativa).", **COMUN)
def _():
    p, q, r = v8().values()
    esperado = expresion("(25/6)x^2 - (81/20)x + (74/15)")
    assert expand(p + (q + r) - esperado) == 0 and expand((p + q) + r - esperado) == 0


@ejercicio(id=nuevo_id(), tipo="calculo", dificultad=1, fuente=f"{FUENTE} 8c",
           enunciado=DEF8 + r"Comprueba que la suma de cada polinomio con su opuesto aditivo da "
                     r"el polinomio nulo.",
           respuesta=r"$-p(x) = -\frac{2}{3}x^{2} + 5x - \frac{3}{5}$, "
                     r"$-q(x) = -\frac{3}{4}x - 5x^{2} + \frac{2}{3}$, "
                     r"$-r(x) = -5 + \frac{3}{2}x^{2} - \frac{1}{5}x$; al sumar cada polinomio con "
                     r"su opuesto, cada término se anula con su opuesto y queda $0$.", **COMUN)
def _():
    opuestos = [expresion("-(2/3)x^2 + 5x - (3/5)"), expresion("-(3/4)x - 5x^2 + (2/3)"),
                expresion("-5 + (3/2)x^2 - (1/5)x")]
    for pol, op in zip(v8().values(), opuestos):
        assert expand(pol + op) == 0


@ejercicio(id=nuevo_id(), tipo="conceptual", dificultad=2, fuente=f"{FUENTE} 8d",
           enunciado=DEF8 + r"¿Qué puedes decir al comparar $q(x) - r(x)$ con $r(x) - q(x)$?",
           respuesta=r"Son polinomios opuestos: $q(x) - r(x) = \frac{13}{2}x^{2} + \frac{11}{20}x "
                     r"- \frac{17}{3}$ y $r(x) - q(x) = -\frac{13}{2}x^{2} - \frac{11}{20}x + "
                     r"\frac{17}{3}$. La sustracción no es conmutativa.", **COMUN)
def _():
    p, q, r = v8().values()
    assert expand(q - r - expresion("(13/2)x^2 + (11/20)x - (17/3)")) == 0
    assert expand((r - q) + (q - r)) == 0 and expand(q - r) != expand(r - q)


# ---------- 9. Operaciones combinadas ----------
COMB = [
    ("9a", r"De la diferencia entre $(3a - 2b)$ y $(2a - b)$, sustrae la suma de $(8a - b)$ y "
           r"$(5a - b)$.", "((3a - 2b) - (2a - b)) - ((8a - b) + (5a - b))", "-12a + b"),
    ("9b", r"De la suma de $(5m - 3n - 8)$ y $(4m - 2n + 8)$, sustrae la diferencia entre "
           r"$(m + n + 1)$ y $(m - n - 2)$.",
     "((5m - 3n - 8) + (4m - 2n + 8)) - ((m + n + 1) - (m - n - 2))", "9m - 7n - 3"),
    ("9c", r"Sustrae la suma de $(2p + 3q + 5r)$ y $(4p - 3q - 6r)$ a la suma de $(2p + q - r)$ "
           r"y $(3p - 4q - 5r)$.",
     "((2p + q - r) + (3p - 4q - 5r)) - ((2p + 3q + 5r) + (4p - 3q - 6r))", "-p - 3q - 5r"),
    ("9d", r"Sustrae $(3a - 2 - 5c + 8)$ a la diferencia entre $(3a - 2b + 5c - 9)$ y "
           r"$(4a + b - c - 1)$.",
     "((3a - 2b + 5c - 9) - (4a + b - c - 1)) - (3a - 2 - 5c + 8)", "-4a - 3b + 11c - 14"),
]
for lit, enun, s, r in COMB:
    @ejercicio(id=nuevo_id(), tipo="calculo", dificultad=2, fuente=f"{FUENTE} {lit}",
               enunciado=f"Realiza la operación. {enun}", respuesta=f"${ltx(r)}$.", **COMUN)
    def _(s=s, r=r):
        assert expand(expresion(s) - expresion(r)) == 0


# ---------- 10. Signos de agrupación ----------
AGRUPACION = [
    ("10a", r"2a + \{a - (b - c)\}", "3a - b + c"),
    ("10b", r"-\{-(-a)\} - \{(-a)\} + [-\{-b + c\} - \{-(-b)\}]", "-c"),
    ("10c", r"12mn - \{5mn - 2m + (2mn - 5mn)\}", "10m n + 2m"),
    ("10d", r"a + \{(-2c) - (3b + 3c) - (a + b + c)\}", "-4b - 6c"),
    ("10e", r"-(x + y) + \{3x - 2y - (3x - 4y)\}", "-x + y"),
    ("10f", r"(-r + s) + \{-(s - r + 3r) - (5r - 9s)\}", "-8r + 9s"),
    ("10g", r"6c - [-(3a - 5b) - \{a - 2c + (3c - 8b)\}]", "4a - 13b + 7c"),
    ("10h", r"a - [-7ab + \{-b + (-a + 3ab - 2b)\}]", "2a + 4a b + 3b"),
    ("10i", r"-(3x + y) - [2x + \{-x + (2y - 5)\} - (y + 6)]", "-4x - 2y + 11"),
    ("10j", r"2a + \{a - (2b - c) + (c - 3b)\} - \{-(a + b)\}", "4a - 4b + 2c",
     "En el módulo falta la llave que cierra «{- (a + b)»; se agregó."),
    ("10k", r"-\{(4bc - 9a) + (3bc + 3c) - (a + bc + c)\}", "10a - 6b c - 2c"),
    ("10l", r"-r + \{3s - (s - r) + 8r\} - (-8r + 11s)", "16r - 9s",
     "En el módulo sobra una llave de cierre al final; se quitó."),
    ("10m", r"-[-(-7x - 12y) - \{-3x - 2y + (3x - 11y)\}]", "-7x - 25y"),
    ("10n", r"(-a + 3ab - 2b) + \{a + [-7ab - \{-5b + 8\}]\}", "-4a b + 3b - 8",
     "En el módulo falta la llave que cierra «{a + [...]»; se agregó."),
    ("10o", r"-[2x - \{-x - (2y + 5)\} - (5y - 6)] + (9x - y)", "6x + 2y - 11"),
    ("10p", r"-(-2r - 5s) - \{-(5s - 9r) - (-11r + 29s)\}", "-18r + 39s"),
]
for lit, t, r, *nota in AGRUPACION:
    @ejercicio(id=nuevo_id(), tipo="calculo", dificultad=2, fuente=f"{FUENTE} {lit}",
               enunciado=f"Suprime los signos de agrupación y reduce los términos semejantes: "
                         f"${t}$.",
               respuesta=f"${ltx(r)}$.", **(dict(notas=nota[0]) if nota else {}), **COMUN)
    def _(t=t, r=r):
        assert t.count("(") == t.count(")") and t.count("[") == t.count("]")
        assert t.count(r"\{") == t.count(r"\}")
        assert expand(expresion(py(t)) - expresion(r)) == 0


# ---------- 11. Introducir términos en un paréntesis precedido de «-» ----------
INTRODUCIR = [
    ("11a", "5a + 3a b - 2b x + c z", "5a", "-3a b + 2b x - c z"),
    ("11b", "-a + 5v - 2c + 4x", "-a", "-5v + 2c - 4x"),
    ("11c", "m + 3m n - 24n + 1", "m", "-3m n + 24n - 1"),
    ("11d", "-a + 3a b + 2b + c", "-a", "-3a b - 2b - c"),
    ("11e", "2m - 5n - 3x + 9y", "2m", "5n + 3x - 9y"),
    ("11f", "-2b - c - b c - a", "-2b", "c + b c + a"),
    ("11g", "5x y - 6 + 9x - y", "5x y", "6 - 9x + y"),
    ("11h", "a - 2b c + 3c - 8b", "a", "2b c - 3c + 8b"),
    ("11i", "9x + 12y - 3 - y", "9x", "-12y + 3 + y"),
    ("11j", "10y z - 3y - 8x + 10y", "10y z", "3y + 8x - 10y"),
    ("11k", "9x y + 2 - 7x - 8y", "9x y", "-2 + 7x + 8y"),
    ("11l", "-7w - 12y - 3x - 2w", "-7w", "12y + 3x + 2w"),
]
for lit, s, primero, dentro in INTRODUCIR:
    @ejercicio(id=nuevo_id(), tipo="calculo", dificultad=1, fuente=f"{FUENTE} {lit}",
               enunciado=f"Introduce los tres últimos términos de ${ltx(s)}$ dentro de un "
                         f"paréntesis precedido del signo $-$.",
               respuesta=f"${ltx(primero)} - ({ltx(dentro)})$.", **COMUN)
    def _(s=s, primero=primero, dentro=dentro):
        assert expand(expresion(primero) - expresion(dentro) - expresion(s)) == 0
        assert len(Add.make_args(expresion(dentro, evaluar=False))) == 3
