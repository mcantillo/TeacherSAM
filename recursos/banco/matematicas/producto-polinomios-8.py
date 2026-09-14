"""Banco de ejercicios — Matemáticas 8° — Producto de monomios y polinomios; binomio de Newton.
Fuente: módulo de Matemáticas 8° de las Guías de Apoyo (Adriana Quintero Palomino), Tema 2;
se lee en recursos/matematicas/Guías pedagógicas Matemáticas/markdown/08 - Modulo_Matematicas_Octavo.md
(«Practica lo aprendido» y «Prepárate para el ICFES» de la sección «Producto entre polinomios»).
No incluidos: 3p (repite 3k); 5 (tabla sin indicar qué valores toma cada variable); 6 (la rueda
tiene 9 casillas y el módulo da solo 8 monomios); 7d («(x + 5y)» sin el otro factor); 12a y 12b
(volúmenes que dependen de la figura: a la 12a le falta una medida y en la 12b no es claro si x es
la altura de la pirámide o la de una cara).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/producto-polinomios-8.py
"""
import re

from sympy import Add, Mul, Poly, Rational, binomial, expand, simplify, solve, symbols

from ejercicios import ejercicio, ejercicio_manual, expresion

FUENTE = ("módulo 8° (Quintero Palomino), Tema 2, Expresiones algebraicas, Producto entre "
          "polinomios — Practica lo aprendido")
ICFES = ("módulo 8° (Quintero Palomino), Tema 2, Expresiones algebraicas, Producto entre "
         "polinomios — Prepárate para el ICFES")
COMUN = dict(tema="producto de polinomios", grados=[8], dba=["matematicas-8-9"])
PREFIJO = "producto-polinomios-8"
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
    s = s.replace("*", r" \cdot ")
    return re.sub(r"(?<=[\w})]) (?=[\w\\(])", "", s)


def opciones(*items):
    return r" \begin{opciones} " + " ".join(r"\item " + i for i in items) + r" \end{opciones}"


# ---------- 1. Forma exponencial ----------
EXPONENCIAL = [
    ("1a", ["x"] * 5, "x^5", None), ("1b", ["c", "c", "3", "c"], "3c^3", None),
    ("1c", ["-3", "x", "2", "x"], "-6x^2", "En el módulo aparece «X» mayúscula; se escribe x."),
    ("1d", ["m"] * 3, "m^3", None), ("1e", ["-6", "z", "z", "z"], "-6z^3", None),
    ("1f", ["7", "n", "(-2)", "n"], "-14n^2", "En el módulo aparece «N» mayúscula; se escribe n."),
    ("1g", ["4", "t", "t", "t"], "4t^3", None), ("1h", ["y", "y", "(-5)"], "-5y^2", None),
    ("1i", ["(-2)", "(-2)", "x", "x"], "4x^2", None),
]
for lit, fs, r, nota in EXPONENCIAL:
    @ejercicio(id=nuevo_id(), tipo="calculo", dificultad=1, fuente=f"{FUENTE} {lit}",
               enunciado=f"Escribe en forma exponencial: ${r' \cdot '.join(fs)}$.",
               respuesta=f"${ltx(r)}$.", **(dict(notas=nota) if nota else {}), **COMUN)
    def _(fs=fs, r=r):
        assert expand(expresion("*".join(fs)) - expresion(r)) == 0


# ---------- 2. Áreas de rectángulos ----------
AREAS = [("2a", "3y", "2", "6y"), ("2b", "2x + 5", "3x + 9", "6x^2 + 33x + 45"),
         ("2c", "x + 3", "x", "x^2 + 3x")]
for lit, l1, l2, r in AREAS:
    @ejercicio(id=nuevo_id(), tipo="contexto", dificultad=1, fuente=f"{FUENTE} {lit}",
               tema=COMUN["tema"], grados=[8], dba=["matematicas-8-9", "matematicas-8-4"],
               enunciado=f"Encuentra una expresión algebraica para el área de un rectángulo cuyos "
                         f"lados miden ${ltx(l1)}$ y ${ltx(l2)}$.",
               respuesta=f"$A = ({ltx(l1)})({ltx(l2)}) = {ltx(r)}$.",
               notas="Las medidas se toman de la descripción de la imagen del módulo.")
    def _(l1=l1, l2=l2, r=r):
        assert expand(expresion(l1) * expresion(l2) - expresion(r)) == 0


# ---------- 3 y 4. Producto de monomios ----------
MONOMIOS = [
    ("3a", ["3x^3", "(1/6)x^2", "8x"], "4x^6"), ("3b", ["x^3", "x^4", "x^2"], "x^9"),
    ("3c", ["n^2", "n^2", "n"], "n^5"), ("3d", ["2x^5", "5x^5"], "10x^10"),
    ("3e", ["5a^5", "6a^5"], "30a^10"), ("3f", ["m^2 n", "m n^4"], "m^3 n^5"),
    ("3g", ["y^3 z", "y^2 z^3"], "y^5 z^4"), ("3h", ["2a b", "3a b^5"], "6a^2 b^6"),
    ("3i", ["3p^3 q", "-(5/6)q^3", "-p^4"], "(5/2)p^7 q^4"),
    ("3j", ["5x^2 y", "3x^3 y^4"], "15x^5 y^5"), ("3k", ["4x^5", "-3x^2"], "-12x^7"),
    ("3l", ["5y^3", "-2y^4"], "-10y^7"), ("3m", ["-3x y^3", "-2x^3 y"], "6x^4 y^4"),
    ("3n", ["3r^2 s^3", "4y^4 z^2"], "12r^2 s^3 y^4 z^2"),
    ("3o", ["3y^3 z", "4y^4 z^2"], "12y^7 z^3",
     "El texto alternativo describe otro factor («menos 3 x elevado a la 2»); se usa la fórmula "
     "impresa."),
    ("3q", ["8c^2", "-d", "-(1/4)c d^2"], "2c^3 d^3"),
    ("3r", ["3a^2", "-2b", "6a b"], "-36a^3 b^2"),
    ("4a", ["5m^2", "3m"], "15m^3"),
    ("4b", ["3h^2 p", "-5h p^2", "-3h^2 p^2"], "45h^5 p^5"),
    ("4c", ["-x", "-2x", "-3x^3", "-4x^4"], "24x^9"),
    ("4d", ["0.6a^2 b", "-0.3a b^3"], "-0.18a^3 b^4"),
    ("4e", ["0.5x^2 y", "(1/5)a x"], "0.1a x^3 y"),
    ("4f", ["(3/4)a^2 b", "(2/3)a^5 b^6"], "(1/2)a^7 b^7"),
    ("4g", ["-(2/3)m^2 n^4", "-(3/4)m n^5"], "(1/2)m^3 n^9"),
    ("4h", ["(11/4)a h k^4", "(12/11)a^2 h^(-3) k^(-2)"], "3a^3 h^(-2) k^2"),
    ("4i", ["-x^(-4)", "-(3/5)x^(-2)", "0.75x"], "(9/20)x^(-5)"),
    ("4j", ["0.6x^(-3)", "-(2/3)x^4"], "-0.4x"),
    ("4k", ["a^2 b^3", "-a^(-2) b^5", "-b^(-8)"], "1"),
    ("4l", ["0.4x^(-2)", "0.4x^2 y"], "0.16y"),
    ("4m", ["-(2/3)x^(-1) y^(-2)", "-(3/2)x y^2", "(1/4)x^5 y"], "(1/4)x^5 y"),
    ("4n", ["0.5a^3 b^2", "0.05b^4", "0.4a^3 b"], "0.01a^6 b^7"),
    ("4o", ["2.5a^3 b^4", "4a^(-3) b^(-5)", "-(3/5)a"], "-6a b^(-1)"),
    ("4p", ["-x^3 y", "-x y^3", "-x^2 y^4", "-x^3 y"], "x^9 y^9"),
    ("4q", ["2a b", "-b", "-c", "-d", "-5a^3 b^2 c d"], "10a^4 b^4 c^2 d^2"),
]
EXTRA = {"4h": r" = \frac{3a^{3}k^{2}}{h^{2}}", "4i": r" = \frac{9}{20x^{5}}",
         "4o": r" = -\frac{6a}{b}"}
for lit, fs, r, *nota in MONOMIOS:
    instr = ("Aplica la propiedad $a^{m} \\cdot a^{n} = a^{m + n}$ y simplifica: " if lit[0] == "3"
             else "Utiliza las propiedades de la potenciación para simplificar: ")
    neg = "^(-" in "".join(fs)

    @ejercicio(id=nuevo_id(), tipo="calculo", dificultad=3 if neg else (2 if "/" in "".join(fs)
                                                                      or "." in "".join(fs) else 1),
               fuente=f"{FUENTE} {lit}",
               enunciado=instr + "$" + "".join(f"\\left({ltx(f)}\\right)" for f in fs) + "$"
                         + (" (las letras representan números distintos de cero)." if neg else "."),
               respuesta=f"${ltx(r)}{EXTRA.get(lit, '')}$.",
               **(dict(notas=nota[0]) if nota else {}), **COMUN)
    def _(fs=fs, r=r):
        assert simplify(Mul(*map(expresion, fs)) - expresion(r)) == 0



# ---------- 7. Monomio por polinomio ----------
DISTRIB = [
    ("7a", "7(5a + b)", "35a + 7b"), ("7b", "(x^2 + 3y)2x", "2x^3 + 6x y"),
    ("7c", "(a^2 - 2a b)b^2", "a^2 b^2 - 2a b^3"), ("7e", "(3a + 5b)(-4)", "-12a - 20b"),
    ("7f", "6x y(x y + y)", "6x^2 y^2 + 6x y^2"), ("7g", "(2a - 4b)a b", "2a^2 b - 4a b^2"),
    ("7h", "(5a + 4a^2)3a^2", "15a^3 + 12a^4"), ("7i", "(x + y)x^2", "x^3 + x^2 y"),
    ("7j", "(2y + 6)y", "2y^2 + 6y"), ("7k", "4(2a + 5b)", "8a + 20b"),
    ("7l", "a b(4a - b)", "4a^2 b - a b^2"), ("7m", "-6a^2 b(a^2 + b)", "-6a^4 b - 6a^2 b^2"),
    ("7n", "2a^2(a^3 + 3a b)", "2a^5 + 6a^3 b"), ("7o", "(c + 5d)(-15)", "-15c - 75d"),
]
for lit, s, r in DISTRIB:
    @ejercicio(id=nuevo_id(), tipo="calculo", dificultad=1, fuente=f"{FUENTE} {lit}",
               enunciado=f"Calcula el producto ${ltx(s)}$.", respuesta=f"${ltx(r)}$.",
               **(dict(notas="El texto alternativo dice «4 a elevado a la 2» como factor; se usa "
                             "la fórmula impresa, 3a^2.") if lit == "7h" else {}), **COMUN)
    def _(s=s, r=r):
        assert expand(expresion(s) - expresion(r)) == 0


# ---------- 8. Grado del producto ----------
x = symbols("x", real=True)
GRADO8 = [
    ("8a", "Al multiplicar dos polinomios de grado $n$, ¿cuál es el grado del producto?",
     "$2n$, porque el producto de los términos de mayor grado es $x^{n} \\cdot x^{n} = x^{2n}$."),
    ("8b", "Al multiplicar dos polinomios de grado $m$ y $n$, ¿cuál es el grado del producto?",
     "$m + n$, porque $x^{m} \\cdot x^{n} = x^{m + n}$."),
    ("8c", "El grado del producto de dos polinomios es $m + n$. Si uno de los factores tiene "
           "grado $m$, ¿cuál es el grado del otro factor?", "$n$."),
]
for lit, enun, r in GRADO8:
    @ejercicio(id=nuevo_id(), tipo="conceptual", dificultad=2, fuente=f"{FUENTE} {lit}",
               enunciado=enun, respuesta=r, **COMUN)
    def _():
        for m_, n_ in [(1, 1), (2, 3), (4, 2), (3, 3)]:
            a = x**m_ + 2 * x - 1 if m_ > 1 else 3 * x + 1
            b = 5 * x**n_ - x + 7 if n_ > 1 else x - 4
            assert Poly(expand(a * b), x).degree() == m_ + n_


# ---------- 9 y 10. Operaciones con polinomios dados ----------
def serie_ops(lit0, polis, ops):
    defin = ", ".join(f"${k}(x) = {ltx(v)}$" for k, v in polis.items())
    for lit, op, op_tex, r in ops:
        @ejercicio(id=nuevo_id(), tipo="calculo", dificultad=2, fuente=f"{FUENTE} {lit0}{lit}",
                   enunciado=f"Con los polinomios {defin}, resuelve ${op_tex}$.",
                   respuesta=f"${ltx(r)}$.",
                   notas="En el módulo el producto se escribe con una «x», que se confunde con la "
                         "variable; se usa el punto.", **COMUN)
        def _(op=op, r=r):
            valores = {k: expresion(v) for k, v in polis.items()}
            assert expand(eval(op, {}, valores) - expresion(r)) == 0


serie_ops("9", {"p": "2x + 3", "q": "x + 4", "r": "3x - 2"}, [
    ("a", "p*q", r"p(x) \cdot q(x)", "2x^2 + 11x + 12"),
    ("b", "p*(q + r)", r"p(x) \cdot [q(x) + r(x)]", "8x^2 + 16x + 6"),
    ("c", "q*r - p*r", r"q(x) \cdot r(x) - p(x) \cdot r(x)", "-3x^2 + 5x - 2"),
    ("d", "q*p", r"q(x) \cdot p(x)", "2x^2 + 11x + 12"),
    ("e", "p*r", r"p(x) \cdot r(x)", "6x^2 + 5x - 6"),
    ("f", "(q - p)*(r + p)", r"[q(x) - p(x)] \cdot [r(x) + p(x)]", "-5x^2 + 4x + 1"),
])
serie_ops("10", {"m": "6", "n": "2 + x^2", "t": "6x - 2", "w": "-2"}, [
    ("a", "m*n", r"m(x) \cdot n(x)", "6x^2 + 12"),
    ("b", "(w + m)*n", r"[w(x) + m(x)] \cdot n(x)", "4x^2 + 8"),
    ("c", "n*t*m", r"n(x) \cdot t(x) \cdot m(x)", "36x^3 - 12x^2 + 72x - 24"),
    ("d", "m*n + m", r"m(x) \cdot n(x) + m(x)", "6x^2 + 18"),
    ("e", "(w - m)*t", r"[w(x) - m(x)] \cdot t(x)", "-48x + 16"),
    ("f", "(n - t*w) + m", r"[n(x) - t(x) \cdot w(x)] + m(x)", "x^2 + 12x + 4"),
    ("g", "(t - n)*w", r"[t(x) - n(x)] \cdot w(x)", "2x^2 - 12x + 8"),
    ("h", "(t - n + w)*m", r"[t(x) - n(x) + w(x)] \cdot m(x)", "-6x^2 + 36x - 36"),
    ("i", "(m*n)*t", r"[m(x) \cdot n(x)] \cdot t(x)", "36x^3 - 12x^2 + 72x - 24"),
])


# ---------- 11. Factor que falta: (literal, factor dado, producto, factor escrito a mano, lado) ----------
FALTA = [
    ("11a", "6", "6b", "b", "izq"), ("11b", "2", "2a^2", "a^2", "der"),
    ("11c", "-x", "x^2", "-x", "izq"), ("11d", "4a", "8a^2", "2a", "izq"),
    ("11e", "4a x", "8a x^2", "2x", "der"), ("11f", "a x", "3a x", "3", "der"),
    ("11g", "8x", "0", "0", "izq"), ("11h", "11c", "-132c^2", "-12c", "der"),
    ("11i", "3x", "-18n x y", "-6n y", "der"), ("11j", "9x y", "27x^2 y^2 m", "3x y m", "izq"),
    ("11k", "5m^2 n", "15m^3 n^3", "3m n^2", "der"), ("11l", "c^4 d", "22c^4 d", "22", "izq"),
    ("11m", "12a m", "36a b m", "3b", "der"),
]
for lit, dado, prod, r, lado in FALTA:
    hueco = r"\square"
    op = (f"{hueco} \\cdot {ltx(dado)}" if lado == "izq" else f"{ltx(dado)} \\cdot {hueco}")

    @ejercicio(id=nuevo_id(), tipo="calculo", dificultad=1, fuente=f"{FUENTE} {lit}",
               enunciado=f"Escribe el factor que falta para que el producto sea el indicado: "
                         f"${op} = {ltx(prod)}$.",
               respuesta=f"${ltx(r)}$, porque ${op.replace(hueco, '(' + ltx(r) + ')')} = "
                         f"{ltx(prod)}$.",
               notas="En el módulo los productos están escritos en palabras («2 a al cuadrado»).",
               **COMUN)
    def _(dado=dado, prod=prod, r=r):
        assert expand(expresion(dado) * expresion(r) - expresion(prod)) == 0


# ---------- 13. Cuadrado sobre un cateto ----------
y = symbols("y", positive=True)


@ejercicio(id=nuevo_id(), tipo="contexto", dificultad=3, fuente=f"{FUENTE} 13",
           tema=COMUN["tema"], grados=[8], dba=["matematicas-8-9", "matematicas-8-7"],
           enunciado=r"Un triángulo rectángulo tiene hipotenusa $5y$ y un cateto $5y - 2$. Sobre "
                     r"el otro cateto se construye un cuadrado. Escribe un polinomio para el área "
                     r"de ese cuadrado.",
           respuesta=r"Por el teorema de Pitágoras, el área es $(5y)^{2} - (5y - 2)^{2} = "
                     r"25y^{2} - (25y^{2} - 20y + 4) = 20y - 4$ (con $y > \frac{2}{5}$).",
           notas="La descripción de la imagen del módulo es confusa («el volumen de un triángulo "
                 "rectángulo… la profundidad de la figura es cuadrado»); se redactó el enunciado "
                 "con los datos que da: hipotenusa 5y, cateto 5y − 2 y cuadrado sobre el otro "
                 "cateto. Conviene revisarlo con la imagen original.")
def _():
    assert expand((5 * y)**2 - (5 * y - 2)**2 - (20 * y - 4)) == 0
    assert solve(20 * y - 4, y) == [Rational(1, 5)]            # área > 0 si y > 1/5 …
    assert Rational(2, 5) > Rational(1, 5)                     # … y el cateto 5y − 2 > 0 si y > 2/5


# ---------- 14. Potencias de un binomio ----------
BINOMIOS = [
    ("14a", "2x - 1", 4, "16x^4 - 32x^3 + 24x^2 - 8x + 1"),
    ("14b", "x - 3", 5, "x^5 - 15x^4 + 90x^3 - 270x^2 + 405x - 243"),
    ("14c", "x - 4y", 4, "x^4 - 16x^3 y + 96x^2 y^2 - 256x y^3 + 256y^4"),
    ("14d", "x + 1", 6, "x^6 + 6x^5 + 15x^4 + 20x^3 + 15x^2 + 6x + 1"),
    ("14e", "3x - 2y", 5, "243x^5 - 810x^4 y + 1080x^3 y^2 - 720x^2 y^3 + 240x y^4 - 32y^5"),
    ("14f", "2x - y", 5, "32x^5 - 80x^4 y + 80x^3 y^2 - 40x^2 y^3 + 10x y^4 - y^5"),
    ("14g", "(1/2)x - (1/3)y", 4,
     "(1/16)x^4 - (1/6)x^3 y + (1/6)x^2 y^2 - (2/27)x y^3 + (1/81)y^4"),
    ("14h", "a - 2b", 7,
     "a^7 - 14a^6 b + 84a^5 b^2 - 280a^4 b^3 + 560a^3 b^4 - 672a^2 b^5 + 448a b^6 - 128b^7"),
    ("14i", "2m - (1/2)n", 9,
     "512m^9 - 1152m^8 n + 1152m^7 n^2 - 672m^6 n^3 + 252m^5 n^4 - 63m^4 n^5 + (21/2)m^3 n^6"
     " - (9/8)m^2 n^7 + (9/128)m n^8 - (1/512)n^9"),
    ("14j", "(2/3)p - (4/5)", 6,
     "(64/729)p^6 - (256/405)p^5 + (256/135)p^4 - (2048/675)p^3 + (1024/375)p^2"
     " - (4096/3125)p + (4096/15625)"),
    ("14k", "3x - 2", 3, "27x^3 - 54x^2 + 36x - 8"),
    ("14l", "(1/3)x + (2/5)y", 4,
     "(1/81)x^4 + (8/135)x^3 y + (8/75)x^2 y^2 + (32/375)x y^3 + (16/625)y^4"),
    ("14m", "2m - 4n", 5,
     "32m^5 - 320m^4 n + 1280m^3 n^2 - 2560m^2 n^3 + 2560m n^4 - 1024n^5"),
    ("14n", "a - 1", 3, "a^3 - 3a^2 + 3a - 1"),
    ("14o", "(2/3)m^2 + 4n", 5,
     "(32/243)m^10 + (320/81)m^8 n + (1280/27)m^6 n^2 + (2560/9)m^4 n^3 + (2560/3)m^2 n^4"
     " + 1024n^5"),
    ("14p", "9m - 2p", 3, "729m^3 - 486m^2 p + 108m p^2 - 8p^3"),
]
TEXB = {"14g": r"\frac{x}{2} - \frac{y}{3}"}
for lit, b, k, r in BINOMIOS:
    @ejercicio(id=nuevo_id(), tipo="calculo", dificultad=3 if k > 5 or "/" in b else 2,
               fuente=f"{FUENTE} {lit}",
               enunciado=f"Calcula $\\left({TEXB.get(lit, ltx(b))}\\right)^{{{k}}}$.",
               respuesta=f"${ltx(r)}$.", **COMUN)
    def _(b=b, k=k, r=r):
        assert expand(expresion(b)**k - expresion(r)) == 0
        assert len(Add.make_args(expresion(r))) == k + 1


# ---------- 15. Interés compuesto ----------
@ejercicio(id=nuevo_id(), tipo="contexto", dificultad=2, fuente=f"{FUENTE} 15",
           tema=COMUN["tema"], grados=[8], dba=["matematicas-8-9", "matematicas-8-8"],
           enunciado=r"El capital final $C_f$ de un depósito a un interés anual del $i\,\%$ se "
                     r"calcula con la fórmula $C_f = C_i\left(1 + \frac{i}{100}\right)^{n}$, donde "
                     r"$n$ es el número de años. Determina el capital final de una persona que "
                     r"depositó \$100\,000 en un banco durante cuatro años, a un interés anual del "
                     r"$15\,\%$.",
           respuesta=r"$C_f = 100\,000 \cdot \num{1,15}^{4} = \num{174900,625}$: unos "
                     r"\$174\,900,63.")
def _():
    cf = 100000 * (1 + Rational(15, 100))**4
    assert cf == Rational(174900625, 1000)


# ---------- 16. Término pedido ----------
a_, b_ = symbols("a b", real=True)
TERMINO = [
    ("16a", "tercer", 3, "x^2", "1/y", 2, "1/y^2", r"\frac{1}{y^{2}}",
     r"x^{2} + \frac{1}{y}"),
    ("16b", "cuarto", 4, "2x", "-4", 7, "-35840x^4", None, None),
    ("16c", "quinto", 5, "x", "-3y", 6, "1215x^2 y^4", None, None),
    ("16d", "sexto", 6, "2a", "-(1/2)b", 6, "-(3/8)a b^5", None, r"2a - \frac{1}{2}b"),
    ("16e", "tercer", 3, "4a", "3b", 11, "129761280a^9 b^2", None, None),
    ("16f", "quinto", 5, "(1/2)x", "-y", 12, "(495/256)x^8 y^4", None, r"\frac{1}{2}x - y"),
    ("16g", "octavo", 8, "2m", "-n", 11, "-5280m^4 n^7", None, None),
    ("16h", "sexto", 6, "3x", "-2y", 5, "-32y^5", None, None),
]
for lit, nombre, pos, a, b, k, r, rtex, btex in TERMINO:
    base = btex or (ltx(a) + (" - " + ltx(b[1:]) if b.startswith("-") else " + " + ltx(b)))

    @ejercicio(id=nuevo_id(), tipo="calculo", dificultad=2, fuente=f"{FUENTE} {lit}",
               enunciado=f"Encuentra el {nombre} término del desarrollo de "
                         f"$\\left({base}\\right)^{{{k}}}$.",
               respuesta=f"${rtex or ltx(r)}$.", **COMUN)
    def _(pos=pos, a=a, b=b, k=k, r=r):
        j = pos - 1
        termino = binomial(k, j) * expresion(a)**(k - j) * expresion(b)**j
        assert simplify(termino - expresion(r)) == 0


# ---------- 17. Término con una potencia dada ----------
POTENCIA = [
    ("17a", "quinta potencia de $h$", "h + 7", 7, "h", 5, "1029h^5",
     r"\binom{7}{2}h^{5} \cdot 7^{2} = 21 \cdot 49\,h^{5}"),
    ("17b", "novena potencia de $y$", "x - 2y", 13, "y", 9, "-366080x^4 y^9",
     r"\binom{13}{9}x^{4}(-2y)^{9} = 715 \cdot (-512)\,x^{4}y^{9}"),
    ("17c", "quinta potencia de $t$", "t - 4", 10, "t", 5, "-258048t^5",
     r"\binom{10}{5}t^{5}(-4)^{5} = 252 \cdot (-1024)\,t^{5}"),
    ("17d", "sexta potencia de $w$", "u + 3w", 11, "w", 6, "336798u^5 w^6",
     r"\binom{11}{6}u^{5}(3w)^{6} = 462 \cdot 729\,u^{5}w^{6}"),
]
for lit, frase, b, k, var, e, r, paso in POTENCIA:
    @ejercicio(id=nuevo_id(), tipo="calculo", dificultad=3, fuente=f"{FUENTE} {lit}",
               enunciado=f"Escribe en lenguaje simbólico y encuentra el término que contiene la "
                         f"{frase} en el desarrollo de $({ltx(b)})^{{{k}}}$.",
               respuesta=f"$({ltx(b)})^{{{k}}}$; el término es ${paso} = {ltx(r)}$.",
               notas="En el módulo la potencia del binomio está escrita en palabras («(h + 7) a "
                     "la 7»).", **COMUN)
    def _(b=b, k=k, var=var, e=e, r=r):
        v = symbols(var, real=True)
        desarrollo = expand(expresion(b)**k)
        termino = sum(t for t in Add.make_args(desarrollo) if Poly(t, v).degree() == e)
        assert expand(termino - expresion(r)) == 0


# ---------- 18 y 19. Término independiente ----------
z = symbols("z", real=True)


@ejercicio(id=nuevo_id(), tipo="calculo", dificultad=3, fuente=f"{FUENTE} 18",
           enunciado=r"Encuentra el término que no contiene a $x$ en el desarrollo de "
                     r"$\left(x^{2} - \frac{2}{x^{2}}\right)^{10}$.",
           respuesta=r"El término general es $\binom{10}{k}x^{20 - 4k}(-2)^{k}$; con $k = 5$: "
                     r"$\binom{10}{5}(-2)^{5} = 252 \cdot (-32) = -8064$.", **COMUN)
def _():
    d = expand((x**2 - 2 / x**2)**10)
    assert sum(t for t in Add.make_args(d) if not t.has(x)) == -8064


@ejercicio(id=nuevo_id(), tipo="calculo", dificultad=3, fuente=f"{FUENTE} 19",
           enunciado=r"Encuentra el término que no contiene a $z$ en el desarrollo de "
                     r"$\left(z^{3} - \frac{1}{z^{3}}\right)^{60}$.",
           respuesta=r"El término general es $\binom{60}{k}z^{180 - 6k}(-1)^{k}$; con $k = 30$: "
                     r"$\binom{60}{30} = 118\,264\,581\,564\,861\,424$.",
           notas="El texto alternativo del módulo dice «elevado a la 50»; se usa el exponente "
                 "impreso, 60 (con 50 el término sería -binom(50, 25) = -126 410 606 437 752).",
           **COMUN)
def _():
    d = expand((z**3 - 1 / z**3)**60)
    assert sum(t for t in Add.make_args(d) if not t.has(z)) == 118264581564861424


# ---------- Prepárate para el ICFES ----------
AL_JUARISMI = (r"Al-Juarismi escribía: «He partido diez en dos porciones. He multiplicado una de "
               r"las dos porciones por la otra. Después he multiplicado una de las dos por sí "
               r"misma, y el producto de la multiplicación por sí misma es cuatro veces el "
               r"producto de una por la otra». En notación moderna: si las porciones son $x$ y "
               r"$10 - x$, su producto es $x(10 - x) = 10x - x^{2}$ y el producto de $x$ por sí "
               r"misma es $x^{2}$, así que $x^{2} = 4(10x - x^{2})$. Sumando $4x^{2}$ en ambos "
               r"lados queda $5x^{2} = 40x$, y dividiendo por $5x$ se obtiene $x = 8$. ")


@ejercicio(id=nuevo_id(), tipo="seleccion", dificultad=2, fuente=f"{ICFES} 1",
           tema=COMUN["tema"], grados=[8], dba=["matematicas-8-9", "matematicas-8-3"],
           enunciado=AL_JUARISMI + r"Las porciones en las que se divide $10$ de acuerdo con el "
                     r"método de Al-Juarismi son:"
                     + opciones("$9$ y $1$", "$8$ y $2$", "$6$ y $4$", "$10$ y $0$"),
           respuesta=r"b. $8$ y $2$: $8^{2} = 64 = 4 \cdot (8 \cdot 2)$.",
           notas="En el módulo faltan las fórmulas intermedias (x(10 - x) = …, x^2 = …, la "
                 "ecuación y lo que se suma en ambos lados) y el nombre aparece como «AI-Khuarizmi»; "
                 "se completaron.")
def _():
    xx = symbols("xx")
    assert solve(xx**2 - 4 * xx * (10 - xx), xx) == [0, 8]
    metodo = solve(5 * xx - 40, xx)                          # tras dividir 5x^2 = 40x por 5x
    assert metodo == [8]
    cumple = [a**2 == 4 * a * b for a, b in [(9, 1), (8, 2), (6, 4), (10, 0)]]
    assert cumple == [False, True, False, False]


ejercicio_manual(
    id=nuevo_id(), tipo="argumentacion", dificultad=3, fuente=f"{ICFES} 2",
    tema=COMUN["tema"], grados=[8], dba=["matematicas-8-3"],
    enunciado=AL_JUARISMI + r"Con respecto a la solución del problema se puede establecer que:"
              + opciones(r"No es única porque existe otro valor para el cual el problema tiene "
                         r"solución.",
                         r"Es única porque es imposible encontrar otro par de valores que "
                         r"satisfaga la ecuación.",
                         r"Tiene infinitas soluciones porque es suficiente que las dos porciones "
                         r"buscadas sumen $10$.",
                         r"El método de Al-Juarismi no es fiable para hallar la solución porque, al "
                         r"dividir entre $5x$ los dos miembros de la igualdad, no se tiene en "
                         r"cuenta que $x$ puede ser $0$."),
    respuesta=r"d. La ecuación $5x^{2} = 40x$ equivale a $5x(x - 8) = 0$, que tiene dos "
              r"soluciones, $x = 0$ y $x = 8$; al dividir entre $5x$ se pierde $x = 0$. (Si se "
              r"acepta una «porción» igual a $0$, la opción a también es verdadera; si no, la "
              r"solución $8$ y $2$ es única y lo que falla es solo la justificación.)",
    notas="Pregunta ambigua: a y d pueden defenderse a la vez (x = 0 da las porciones 0 y 10). "
          "Queda como manual para que la docente decida la clave o ajuste las opciones.")
