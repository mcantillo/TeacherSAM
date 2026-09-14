"""Banco de ejercicios — Matemáticas 8° — Operaciones con números reales (adición, sustracción,
multiplicación con irracionales).
Fuente: módulo de Matemáticas 8° de las Guías de Apoyo (Adriana Quintero Palomino), Tema 1;
se lee en recursos/matematicas/Guías pedagógicas Matemáticas/markdown/08 - Modulo_Matematicas_Octavo.md
DBA: matematicas-8-1 y 8-2 (irracionales: representación en la recta, propiedades y operaciones).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/numeros-reales-8.py
"""
import sympy as sp
from sympy import E, Rational, floor, pi, sqrt, symbols

from ejercicios import ejercicio, ejercicio_manual

F_SUMA = "módulo 8° (Quintero Palomino), Tema 1, Adición y sustracción — Practica lo aprendido"
F_MULT = ("módulo 8° (Quintero Palomino), Tema 1, Multiplicación y división — "
          "Practica lo aprendido")
COMUN = dict(tema="operaciones con números reales", grados=[8],
             dba=["matematicas-8-1", "matematicas-8-2"])
a, b, c = symbols("a b c", real=True)
ap, bp = symbols("a b", positive=True)


def igual(x, y):
    """Igualdad exacta (simplify) o, si SymPy no la reduce, numérica con 60 cifras."""
    d = sp.simplify(x - y)
    if d != 0:
        libres = sorted(d.free_symbols, key=str)
        for vals in ([2, 3, 5], [Rational(7, 3), 11, 13]):
            sub = dict(zip(libres, vals))
            assert abs(sp.N(d.subs(sub), 60)) < sp.Float("1e-45"), f"{x} ≠ {y}"
    return True


def item(n, fuente, enunciado, respuesta, comprobar, dificultad=1, tipo="calculo", notas=None):
    extra = dict(notas=notas) if notas else {}
    def envuelta():
        assert bool(comprobar()), "la comprobación dio falso"
    envuelta.__wrapped__ = comprobar          # la huella usa el código de la comprobación
    ejercicio(id=f"numeros-reales-8-{n:03d}", fuente=fuente, enunciado=enunciado,
              respuesta=respuesta, tipo=tipo, dificultad=dificultad, **extra, **COMUN)(envuelta)


def entre(x, lo, hi):
    assert lo < sp.N(x, 30) < hi, f"{sp.N(x)} no está entre {lo} y {hi}"
    return True


# ---------- Adición y sustracción ----------
RECTA = "Representa en la recta real el número que resulta de la operación ${}$."
item(1, f"{F_SUMA} 1a", RECTA.format(r"2 + \sqrt{2}"),
     r"$2 + \sqrt{2} \approx \num{3,41}$: entre $3$ y $4$, un poco antes de $3{,}5$.",
     lambda: entre(2 + sqrt(2), 3.41, 3.42))
item(2, f"{F_SUMA} 1b", RECTA.format(r"\sqrt{2} + \sqrt{2} + 2"),
     r"$2 + 2\sqrt{2} \approx \num{4,83}$: entre $4$ y $5$, más cerca de $5$.",
     lambda: entre(sqrt(2) + sqrt(2) + 2, 4.82, 4.83) and igual(sqrt(2) + sqrt(2) + 2, 2 + 2 * sqrt(2)))
item(3, f"{F_SUMA} 1c", RECTA.format(r"\sqrt{5} + \sqrt{3} + \sqrt{3}"),
     r"$\sqrt{5} + 2\sqrt{3} \approx \num{5,70}$: entre $5$ y $6$.",
     lambda: entre(sqrt(5) + 2 * sqrt(3), 5.70, 5.71))
item(4, f"{F_SUMA} 1d", RECTA.format(r"\sqrt{5} - \sqrt{3}"),
     r"$\sqrt{5} - \sqrt{3} \approx \num{0,50}$: entre $0$ y $1$, casi en la mitad.",
     lambda: entre(sqrt(5) - sqrt(3), 0.50, 0.51))
item(5, f"{F_SUMA} 1e", RECTA.format(r"\sqrt{3} - \sqrt{5}"),
     r"$\sqrt{3} - \sqrt{5} \approx -\num{0,50}$: entre $-1$ y $0$, es el opuesto del "
     r"anterior.",
     lambda: entre(sqrt(3) - sqrt(5), -0.51, -0.50))
item(6, f"{F_SUMA} 1f", RECTA.format(r"\dfrac{\sqrt{2}}{2} - 1"),
     r"$\dfrac{\sqrt{2}}{2} - 1 \approx -\num{0,29}$: entre $-1$ y $0$, más cerca de $0$.",
     lambda: entre(sqrt(2) / 2 - 1, -0.30, -0.29))

CUADRILATERO = (r"Dos de los lados de un cuadrilátero $ABCD$ miden $\sqrt{5}$ cm cada uno y los "
                r"otros dos miden $\sqrt{3}$ cm y $\pi$ cm. ")
NOTA_CUAD = "En el módulo dice «De los lados de un cuadrilátero…»; se corrigió a «Dos de los lados»."
item(7, f"{F_SUMA} 2a", CUADRILATERO + "Halla el perímetro.",
     r"$2\sqrt{5} + \sqrt{3} + \pi \approx \num{9,35}$ cm.",
     lambda: igual(sqrt(5) + sqrt(5) + sqrt(3) + pi, 2 * sqrt(5) + sqrt(3) + pi), notas=NOTA_CUAD)
item(8, f"{F_SUMA} 2b", CUADRILATERO + "Halla la diferencia entre el lado más largo y el más corto.",
     r"El más largo mide $\pi$ cm y el más corto $\sqrt{3}$ cm: $\pi - \sqrt{3} \approx \num{1,41}$ cm.",
     lambda: max([sqrt(5), sqrt(3), pi], key=lambda v: sp.N(v)) == pi
     and min([sqrt(5), sqrt(3), pi], key=lambda v: sp.N(v)) == sqrt(3), notas=NOTA_CUAD)
item(9, f"{F_SUMA} 3",
     "Encuentra el perímetro de un triángulo rectángulo isósceles cuyos catetos miden $5$ cm.",
     r"La hipotenusa mide $\sqrt{5^2 + 5^2} = 5\sqrt{2}$ cm; perímetro $10 + 5\sqrt{2} \approx "
     r"\num{17,07}$ cm.",
     lambda: igual(5 + 5 + sqrt(5**2 + 5**2), 10 + 5 * sqrt(2)))
item(10, f"{F_SUMA} 4",
     r"En el triángulo isósceles $ABC$, la base $AB$ mide $10$ cm, $BC = CA$ y la altura $CH$ "
     r"mide $8$ cm ($CH$ es perpendicular a $AB$ y $H$ es el punto medio de $AB$). Encuentra el "
     r"perímetro del triángulo.",
     r"$CA = \sqrt{5^2 + 8^2} = \sqrt{89}$ cm; perímetro $10 + 2\sqrt{89} \approx \num{28,87}$ cm.",
     lambda: igual(10 + 2 * sqrt(5**2 + 8**2), 10 + 2 * sqrt(89)), dificultad=2,
     notas="La figura del módulo se describe en el enunciado (la descripción accesible la llama "
           "«equilátero», pero el texto dice isósceles con base 10 y altura 8).")
item(11, f"{F_SUMA} 5",
     r"Usa las propiedades conmutativa y asociativa de la adición en $\mathbb{R}$ para expresar "
     r"de tres maneras diferentes la suma $\sqrt{2} + \pi + \sqrt{3} + \sqrt{2} + \sqrt{3}$.",
     r"Por ejemplo: $(\sqrt{2} + \sqrt{2}) + (\sqrt{3} + \sqrt{3}) + \pi = 2\sqrt{2} + "
     r"2\sqrt{3} + \pi$; $\pi + (\sqrt{2} + \sqrt{3}) + (\sqrt{2} + \sqrt{3})$; "
     r"$(\sqrt{3} + \pi) + (\sqrt{2} + \sqrt{2} + \sqrt{3})$. Todas valen $\approx \num{9,43}$.",
     lambda: igual(sqrt(2) + pi + sqrt(3) + sqrt(2) + sqrt(3), 2 * sqrt(2) + 2 * sqrt(3) + pi)
     and igual(pi + 2 * (sqrt(2) + sqrt(3)), (sqrt(3) + pi) + (2 * sqrt(2) + sqrt(3))),
     tipo="argumentacion")
item(12, f"{F_SUMA} 6a",
     r"Representa en la recta real $1 + \sqrt{2}$ y su opuesto $-(1 + \sqrt{2})$. "
     r"¿Es cierto que $-(1 + \sqrt{2}) = -1 - \sqrt{2}$? Explica.",
     r"$1 + \sqrt{2} \approx \num{2,41}$ y su opuesto $\approx -\num{2,41}$, a la misma distancia "
     r"del $0$. Sí: el opuesto de una suma es la suma de los opuestos, "
     r"$-(1 + \sqrt{2}) = (-1) + (-\sqrt{2}) = -1 - \sqrt{2}$.",
     lambda: igual(-(1 + sqrt(2)), -1 - sqrt(2)) and entre(1 + sqrt(2), 2.41, 2.42),
     tipo="argumentacion")
item(13, f"{F_SUMA} 6b",
     r"Representa en la recta real $\dfrac{1}{2} - (1 + \sqrt{2})$ y constata que "
     r"$\dfrac{1}{2} - (1 + \sqrt{2}) = \left(\dfrac{1}{2} - 1\right) - \sqrt{2}$.",
     r"Las dos expresiones valen $-\dfrac{1}{2} - \sqrt{2} \approx -\num{1,91}$: está entre "
     r"$-2$ y $-1$, cerca de $-2$.",
     lambda: igual(Rational(1, 2) - (1 + sqrt(2)), (Rational(1, 2) - 1) - sqrt(2))
     and entre(Rational(1, 2) - (1 + sqrt(2)), -1.92, -1.91), dificultad=2)

OPUESTO = "Encuentra el inverso aditivo (opuesto) de ${}$."
for n, lit, tx, ex, rt, rx in [
    (14, "7a", r"\sqrt{5}", sqrt(5), r"-\sqrt{5}", -sqrt(5)),
    (15, "7b", r"-\pi", -pi, r"\pi", pi),
    (16, "7c", r"-(\sqrt{2} - \sqrt{3})", -(sqrt(2) - sqrt(3)), r"\sqrt{2} - \sqrt{3}",
     sqrt(2) - sqrt(3)),
    (17, "7d", r"\pi - \sqrt{5}", pi - sqrt(5), r"\sqrt{5} - \pi", sqrt(5) - pi),
    (18, "7e", r"(\sqrt{2} - \sqrt{3}) - \sqrt{5}", sqrt(2) - sqrt(3) - sqrt(5),
     r"\sqrt{3} + \sqrt{5} - \sqrt{2}", sqrt(3) + sqrt(5) - sqrt(2)),
]:
    item(n, f"{F_SUMA} {lit}", OPUESTO.format(tx), f"${rt}$.",
         lambda ex=ex, rx=rx: igual(ex + rx, 0))

EFECTUA = "Efectúa ${}$."
for n, lit, tx, ex, rt, rx, dif, nota in [
    (19, "8a", r"\sqrt{5} - \sqrt{3} + \sqrt{5} - 2\sqrt{3} + 4\sqrt{5}",
     sqrt(5) - sqrt(3) + sqrt(5) - 2 * sqrt(3) + 4 * sqrt(5), r"6\sqrt{5} - 3\sqrt{3}",
     6 * sqrt(5) - 3 * sqrt(3), 1, None),
    (20, "8b", r"(4 - 3\sqrt{2}) + (1 - 2\sqrt{2})", (4 - 3 * sqrt(2)) + (1 - 2 * sqrt(2)),
     r"5 - 5\sqrt{2}", 5 - 5 * sqrt(2), 1, None),
    (21, "8c", r"(3 - 2\sqrt{3}) - (1 - \sqrt{3})", (3 - 2 * sqrt(3)) - (1 - sqrt(3)),
     r"2 - \sqrt{3}", 2 - sqrt(3), 1, None),
    (22, "8d", r"(1 + \sqrt{5}) + (\sqrt{5} - 1) - (2\sqrt{5} - 3)",
     (1 + sqrt(5)) + (sqrt(5) - 1) - (2 * sqrt(5) - 3), "3", 3, 2, None),
    (23, "8e", r"\sqrt{100} - \sqrt{36} - (\sqrt{16} - \sqrt{25})",
     sqrt(100) - sqrt(36) - (sqrt(16) - sqrt(25)), r"10 - 6 - (4 - 5) = 5", 5, 1,
     "En el módulo la fórmula es ilegible (Equation 3.0 no decodificada); se reconstruyó con su "
     "texto alternativo «raíz cuadrada de 100 menos raíz cuadrada de 36 menos (raíz cuadrada de "
     "16 menos raíz cuadrada de 25)». Conviene cotejarla con el .docx."),
    (24, "8f", r"\dfrac{1}{\sqrt{4}} - \left(\sqrt{\dfrac{1}{36}} - \sqrt{\dfrac{1}{25}} + "
     r"\sqrt{\dfrac{1}{49}}\right)",
     1 / sqrt(4) - (sqrt(Rational(1, 36)) - sqrt(Rational(1, 25)) + sqrt(Rational(1, 49))),
     r"\dfrac{1}{2} - \left(\dfrac{1}{6} - \dfrac{1}{5} + \dfrac{1}{7}\right) = "
     r"\dfrac{1}{2} - \dfrac{23}{210} = \dfrac{41}{105}", Rational(41, 105), 2, None),
]:
    item(n, f"{F_SUMA} {lit}", EFECTUA.format(tx), f"${rt}$.",
         lambda ex=ex, rx=rx: igual(ex, rx), dificultad=dif, notas=nota)

item(25, f"{F_SUMA} 9a", r"Verifica con una calculadora que $\sqrt{5 + 4} \neq \sqrt{5} + \sqrt{4}$.",
     r"$\sqrt{9} = 3$, mientras que $\sqrt{5} + \sqrt{4} \approx \num{2,236} + 2 = \num{4,236}$.",
     lambda: sp.N(sqrt(5 + 4) - (sqrt(5) + sqrt(4))) < -1, tipo="argumentacion")
item(26, f"{F_SUMA} 9b", r"Verifica con una calculadora que $\sqrt{5 - 4} \neq \sqrt{5} - \sqrt{4}$.",
     r"$\sqrt{1} = 1$, mientras que $\sqrt{5} - \sqrt{4} \approx \num{2,236} - 2 = \num{0,236}$.",
     lambda: sqrt(5 - 4) == 1 and entre(sqrt(5) - 2, 0.236, 0.237), tipo="argumentacion")
item(27, f"{F_SUMA} 9c", r"Verifica con una calculadora que $\sqrt{3} - 1 > 0$ y $1 - \sqrt{3} < 0$.",
     r"$\sqrt{3} \approx \num{1,732}$: $\sqrt{3} - 1 \approx \num{0,732} > 0$ y "
     r"$1 - \sqrt{3} \approx -\num{0,732} < 0$.",
     lambda: bool(sqrt(3) - 1 > 0) and bool(1 - sqrt(3) < 0), tipo="argumentacion")
item(28, f"{F_SUMA} 9d",
     r"Verifica con una calculadora que $\sqrt{\num{1,69}} + \sqrt{\num{0,81}} - \sqrt{\num{2,25}} "
     r"= \num{0,7}$.",
     r"$\num{1,3} + \num{0,9} - \num{1,5} = \num{0,7}$ (las tres raíces son exactas).",
     lambda: sqrt(Rational(169, 100)) + sqrt(Rational(81, 100)) - sqrt(Rational(225, 100))
     == Rational(7, 10), tipo="argumentacion")

# ---------- Multiplicación ----------
SIMPL = "Efectúa en $\\mathbb{{R}}$ y simplifica si es posible: ${}$."
for n, lit, tx, ex, rt, rx, dif, nota in [
    (29, "1a", r"(\sqrt{7} + \sqrt{5}) \cdot \sqrt{2}", (sqrt(7) + sqrt(5)) * sqrt(2),
     r"\sqrt{14} + \sqrt{10}", sqrt(14) + sqrt(10), 1, None),
    (30, "1b", r"(\pi + e - 3) \cdot 5", (pi + E - 3) * 5, r"5\pi + 5e - 15",
     5 * pi + 5 * E - 15, 1, None),
    (31, "1c", r"(\sqrt{2} + \sqrt{5})(\sqrt{3} + \sqrt{5})", (sqrt(2) + sqrt(5)) * (sqrt(3) + sqrt(5)),
     r"\sqrt{6} + \sqrt{10} + \sqrt{15} + 5", sqrt(6) + sqrt(10) + sqrt(15) + 5, 2, None),
    (32, "1d", r"\dfrac{\sqrt{2}}{3} + \dfrac{\sqrt{5}}{4} - \dfrac{\pi}{6}",
     sqrt(2) / 3 + sqrt(5) / 4 - pi / 6, r"\dfrac{4\sqrt{2} + 3\sqrt{5} - 2\pi}{12}",
     (4 * sqrt(2) + 3 * sqrt(5) - 2 * pi) / 12, 2,
     "En el módulo este literal es una suma (no un producto) dentro de la práctica de "
     "multiplicación; se dejó como está."),
    (33, "1e", r"(3 - \sqrt{2})(1 - \sqrt{2})", (3 - sqrt(2)) * (1 - sqrt(2)), r"5 - 4\sqrt{2}",
     5 - 4 * sqrt(2), 1, None),
    (34, "1f", r"\sqrt{3} \cdot \sqrt{5} \cdot \sqrt{3} \cdot \sqrt{7} \cdot 5 \cdot \dfrac{1}{3}",
     sqrt(3) * sqrt(5) * sqrt(3) * sqrt(7) * 5 * Rational(1, 3), r"5\sqrt{35}", 5 * sqrt(35), 2, None),
    (35, "1g", r"\dfrac{1}{\sqrt{2}} \cdot \dfrac{1}{\sqrt{3}} \cdot \dfrac{1}{\sqrt{2}} \cdot "
     r"\dfrac{2}{\sqrt{3}} \cdot 3",
     1 / sqrt(2) * 1 / sqrt(3) * 1 / sqrt(2) * 2 / sqrt(3) * 3, "1", 1, 2, None),
]:
    item(n, f"{F_MULT} {lit}", SIMPL.format(tx), f"${rt}$.",
         lambda ex=ex, rx=rx: igual(ex, rx), dificultad=dif, notas=nota)

PROD = "Si $a$, $b$ y $c$ son números reales, calcula el producto ${}$."
for n, lit, tx, ex, rt, rx in [
    (36, "2a", "(a + b)(a - b)", (a + b) * (a - b), "a^2 - b^2", a**2 - b**2),
    (37, "2b", "(a + b)(a + b)", (a + b) * (a + b), "a^2 + 2ab + b^2", a**2 + 2 * a * b + b**2),
    (38, "2c", "(a - b)(a - c)", (a - b) * (a - c), "a^2 - ac - ab + bc",
     a**2 - a * c - a * b + b * c),
    (39, "2d", "(a + b)(a + c)", (a + b) * (a + c), "a^2 + ac + ab + bc",
     a**2 + a * c + a * b + b * c),
    (40, "2e", "(a - b)(b - c)", (a - b) * (b - c), "ab - ac - b^2 + bc",
     a * b - a * c - b**2 + b * c),
]:
    item(n, f"{F_MULT} {lit}", PROD.format(tx), f"${rt}$.",
         lambda ex=ex, rx=rx: sp.expand(ex - rx) == 0)

CUBO = (r"Un cubo tiene aristas de $5$ cm; $ABFE$ es una de sus caras (la base) y $EC$ une dos "
        r"vértices opuestos del cubo. ")
item(41, f"{F_MULT} 3a", CUBO + "Calcula la longitud de la diagonal $EB$ de la base $ABFE$.",
     r"$EB = \sqrt{5^2 + 5^2} = 5\sqrt{2} \approx \num{7,07}$ cm.",
     lambda: igual(sqrt(5**2 + 5**2), 5 * sqrt(2)))
item(42, f"{F_MULT} 3b", CUBO + "Calcula la longitud de la diagonal $EC$ del cubo.",
     r"$EC = \sqrt{(5\sqrt{2})^2 + 5^2} = 5\sqrt{3} \approx \num{8,66}$ cm.",
     lambda: igual(sqrt((5 * sqrt(2))**2 + 5**2), 5 * sqrt(3)), dificultad=2)
item(43, f"{F_MULT} 3c", CUBO + "Calcula la superficie total del cubo.",
     r"$6 \cdot 5^2 = 150$ cm².", lambda: 6 * 5**2 == 150)
item(44, f"{F_MULT} 3d", CUBO + "Calcula el volumen del cubo.",
     r"$5^3 = 125$ cm³.", lambda: 5**3 == 125)

item(45, f"{F_MULT} 4",
     r"Si $a = \sqrt{3} + \sqrt{2}$ y $b = \sqrt{3} - \sqrt{2}$, encuentra el valor de "
     r"$a^2 + ab + b^2$.",
     r"$a^2 = 5 + 2\sqrt{6}$, $b^2 = 5 - 2\sqrt{6}$, $ab = 3 - 2 = 1$: $a^2 + ab + b^2 = 11$.",
     lambda: igual((sqrt(3) + sqrt(2))**2 + (sqrt(3) + sqrt(2)) * (sqrt(3) - sqrt(2))
                   + (sqrt(3) - sqrt(2))**2, 11), dificultad=2,
     notas="En el módulo falta el valor de a («Si a =, b = √3 − √2»); se tomó a = √3 + √2, el "
           "conjugado de b, como en el ejercicio 5. Conviene confirmarlo con la docente.")
item(46, f"{F_MULT} 5",
     r"Si $a = 2\sqrt{2} + \sqrt{3}$ y $b = 2\sqrt{2} - \sqrt{3}$, encuentra el valor de "
     r"$a^2 - ab + b^2$.",
     r"$a^2 = 11 + 4\sqrt{6}$, $b^2 = 11 - 4\sqrt{6}$, $ab = 8 - 3 = 5$: $a^2 - ab + b^2 = 17$.",
     lambda: igual((2 * sqrt(2) + sqrt(3))**2 - (2 * sqrt(2) + sqrt(3)) * (2 * sqrt(2) - sqrt(3))
                   + (2 * sqrt(2) - sqrt(3))**2, 17), dificultad=2)
item(47, f"{F_MULT} 6",
     r"Si $x = \sqrt{a} + \sqrt{b}$ y $y = \sqrt{a} - \sqrt{b}$, donde $a$ y $b$ son enteros "
     r"positivos, calcula $x^2$, $y^2$ y $xy$.",
     r"$x^2 = a + b + 2\sqrt{ab}$, $y^2 = a + b - 2\sqrt{ab}$, $xy = a - b$.",
     lambda: sp.expand((sqrt(ap) + sqrt(bp))**2 - (ap + bp + 2 * sqrt(ap * bp))) == 0
     and sp.expand((sqrt(ap) - sqrt(bp))**2 - (ap + bp - 2 * sqrt(ap * bp))) == 0
     and sp.expand((sqrt(ap) + sqrt(bp)) * (sqrt(ap) - sqrt(bp)) - (ap - bp)) == 0, dificultad=2)
item(48, f"{F_MULT} 7",
     r"Si $x = \sqrt{2} - \sqrt{3} + \sqrt{5}$ y $y = \sqrt{7} + \sqrt{2}$, calcula $xy$ y $y^2$.",
     r"$xy = \sqrt{14} + 2 - \sqrt{21} - \sqrt{6} + \sqrt{35} + \sqrt{10}$; "
     r"$y^2 = 9 + 2\sqrt{14}$.",
     lambda: igual((sqrt(2) - sqrt(3) + sqrt(5)) * (sqrt(7) + sqrt(2)),
                   sqrt(14) + 2 - sqrt(21) - sqrt(6) + sqrt(35) + sqrt(10))
     and igual((sqrt(7) + sqrt(2))**2, 9 + 2 * sqrt(14)), dificultad=3)
