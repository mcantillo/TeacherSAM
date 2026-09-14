"""Banco de ejercicios — Matemáticas 8° — Radicación en R: raíces n-ésimas, simplificación de
radicales, radicales semejantes, raíces de productos y cocientes, potencias de radicales y
raíces de radicales.
Fuente: módulo de Matemáticas 8° de las Guías de Apoyo (Adriana Quintero Palomino), Tema 1;
se lee en recursos/matematicas/Guías pedagógicas Matemáticas/markdown/08 - Modulo_Matematicas_Octavo.md
DBA: matematicas-8-2 (representaciones y propiedades de números no racionales) y 8-9.
No se incluyó el ejercicio 3 de «Raíces de productos… Racionalización» («En cada uno de los
siguientes ejercicios, racionalizar el denominador:»): en el módulo no trae ningún literal.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/radicacion-8.py
"""
import sympy as sp
from sympy import FiniteSet, Rational, S, cbrt, real_root, root, solveset, sqrt, symbols

from ejercicios import ejercicio

F_RAD = "módulo 8° (Quintero Palomino), Tema 1, Radicación — Practica lo aprendido"
F_SIMP = ("módulo 8° (Quintero Palomino), Tema 1, Raíces de productos, raíces de cocientes y "
          "racionalización — Practica lo aprendido")
F_POT = "módulo 8° (Quintero Palomino), Tema 1, Potencias y raíces de radicales — Practica lo aprendido"
COMUN = dict(tema="radicación", grados=[8], dba=["matematicas-8-2", "matematicas-8-9"])
a, b, c, m, n_, t, x, y = symbols("a b c m n t x y", positive=True)
xr = symbols("x", real=True)


def item(n, fuente, enunciado, respuesta, comprobar, dificultad=1, tipo="calculo", notas=None):
    extra = dict(notas=notas) if notas else {}

    def envuelta():
        assert bool(comprobar()), "la comprobación dio falso"
    envuelta.__wrapped__ = comprobar          # la huella usa el código de la comprobación
    ejercicio(id=f"radicacion-8-{n:03d}", fuente=fuente, enunciado=enunciado,
              respuesta=respuesta, tipo=tipo, dificultad=dificultad, **extra, **COMUN)(envuelta)


def igual(u, v):
    """Igualdad exacta o, si SymPy no la reduce, numérica (60 cifras) en dos puntos positivos."""
    d = sp.simplify(u - v)
    if d != 0:
        libres = sorted(d.free_symbols, key=str)
        for vals in ([2, 3, 5, 7], [Rational(7, 3), 11, 13, Rational(5, 2)]):
            assert abs(sp.N(d.subs(dict(zip(libres, vals))), 60)) < sp.Float("1e-45"), f"{u} ≠ {v}"
    return True


# ---------- Radicación: 1. valor de cada raíz ----------
HALLA = "Halla el número representado por ${}$."
for n, lit, tx, ex, rt, rx in [
    (1, "1a", r"\sqrt{81}", sqrt(81), "9", 9),
    (2, "1b", r"-\sqrt{36}", -sqrt(36), "-6", -6),
    (3, "1c", r"\sqrt[3]{-64}", real_root(-64, 3), "-4", -4),
    (4, "1d", r"\sqrt[3]{125\,000}", real_root(125000, 3), "50", 50),
    (5, "1e", r"\sqrt[5]{-243}", real_root(-243, 5), "-3", -3),
    (6, "1f", r"\sqrt[6]{64}", root(64, 6), "2", 2),
    (7, "1g", r"-\sqrt[4]{625}", -root(625, 4), "-5", -5),
    (8, "1h", r"\sqrt[5]{-32}", real_root(-32, 5), "-2", -2),
    (9, "1i", r"-\sqrt{\num{0,16}}", -sqrt(Rational(16, 100)), r"-\num{0,4}", Rational(-2, 5)),
    (10, "1j", r"\sqrt[5]{\num{0,00032}}", root(Rational(32, 100000), 5), r"\num{0,2}",
     Rational(1, 5)),
]:
    item(n, f"{F_RAD} {lit}", HALLA.format(tx), f"${rt}$.", lambda ex=ex, rx=rx: igual(ex, rx))

# ---------- Radicación: 2. conjuntos ----------
CONJ = "Encuentra los elementos del conjunto ${}$."
item(11, f"{F_RAD} 2a", CONJ.format(r"A = \{n \in \mathbb{R} \mid n^7 = -128\}"),
     r"$A = \{-2\}$.", lambda: solveset(xr**7 + 128, xr, S.Reals) == FiniteSet(-2))
item(12, f"{F_RAD} 2b", CONJ.format(r"B = \{x \in \mathbb{R} \mid x^6 = 10\}"),
     r"$B = \{-\sqrt[6]{10}, \sqrt[6]{10}\}$ (una potencia par de exponente $6$ tiene dos raíces "
     r"reales opuestas).",
     lambda: solveset(xr**6 - 10, xr, S.Reals) == FiniteSet(-root(10, 6), root(10, 6)),
     dificultad=2)
item(13, f"{F_RAD} 2c", CONJ.format(r"C = \{x \in \mathbb{R} \mid x^4 = -16\}"),
     r"$C = \varnothing$: ninguna potencia cuarta de un número real es negativa.",
     lambda: solveset(xr**4 + 16, xr, S.Reals) == S.EmptySet, dificultad=2)

# ---------- Raíces de productos y cocientes: 1. forma más simple ----------
SIMPLE = ("Escribe en la forma más simple (las letras representan números positivos): ${}$.")
for n, lit, tx, ex, rt, rx, dif, nota in [
    (14, "1a", r"\sqrt[3]{40}", cbrt(40), r"2\sqrt[3]{5}", 2 * cbrt(5), 1, None),
    (15, "1b", r"\sqrt[4]{48}", root(48, 4), r"2\sqrt[4]{3}", 2 * root(3, 4), 1, None),
    (16, "1c", r"\sqrt[3]{-250}", real_root(-250, 3), r"-5\sqrt[3]{2}", -5 * cbrt(2), 1, None),
    (17, "1d", r"\sqrt[5]{224}", root(224, 5), r"2\sqrt[5]{7}", 2 * root(7, 5), 1, None),
    (18, "1e", r"\sqrt{2 \cdot 6^4}", sqrt(2 * 6**4), r"36\sqrt{2}", 36 * sqrt(2), 1, None),
    (19, "1f", r"\sqrt[5]{-96}", real_root(-96, 5), r"-2\sqrt[5]{3}", -2 * root(3, 5), 1, None),
    (20, "1g", r"\sqrt[6]{10^6 \cdot 11^{12}}", root(10**6 * 11**12, 6), r"10 \cdot 11^2 = 1210",
     1210, 2, "El texto alternativo del módulo dice «raíz quinta», pero la fórmula impresa es "
     "raíz sexta (con la que el ejercicio sale exacto); se respetó la impresa."),
    (21, "1h", r"\sqrt{6} \cdot \sqrt{21} \cdot \sqrt{70}", sqrt(6) * sqrt(21) * sqrt(70),
     r"\sqrt{8820} = 42\sqrt{5}", 42 * sqrt(5), 2, None),
    (22, "1i", r"\sqrt[3]{30} \cdot \sqrt[3]{-400}", cbrt(30) * real_root(-400, 3),
     r"\sqrt[3]{-12\,000} = -10\sqrt[3]{12}", -10 * cbrt(12), 2, None),
    (23, "1j", r"-\sqrt[4]{25} \cdot \sqrt[4]{50}", -root(25, 4) * root(50, 4),
     r"-\sqrt[4]{1250} = -5\sqrt[4]{2}", -5 * root(2, 4), 2, None),
    (24, "1k", r"\sqrt[4]{36} \cdot \sqrt[4]{180}", root(36, 4) * root(180, 4),
     r"\sqrt[4]{6480} = 6\sqrt[4]{5}", 6 * root(5, 4), 2, None),
    (25, "1l", r"\sqrt{\num{0,7}}", sqrt(Rational(7, 10)), r"\sqrt{\dfrac{70}{100}} = "
     r"\dfrac{\sqrt{70}}{10}", sqrt(70) / 10, 2, None),
    (26, "1m", r"\sqrt[3]{\num{0,7}}", cbrt(Rational(7, 10)), r"\sqrt[3]{\dfrac{700}{1000}} = "
     r"\dfrac{\sqrt[3]{700}}{10}", cbrt(700) / 10, 2, None),
    (27, "1n", r"\sqrt[3]{-\dfrac{1}{10^5}}", real_root(Rational(-1, 10**5), 3),
     r"-\dfrac{1}{10\sqrt[3]{100}} = -\dfrac{\sqrt[3]{10}}{100}", -cbrt(10) / 100, 3, None),
    (28, "1o", r"-\sqrt[5]{-\dfrac{32}{27}}", -real_root(Rational(-32, 27), 5),
     r"\dfrac{2}{\sqrt[5]{27}} = \dfrac{2\sqrt[5]{9}}{3}", 2 * root(9, 5) / 3, 3,
     "El texto alternativo omite los dos signos «menos» («menos raíz quinta de 32 27avos»); se "
     "respetó la fórmula impresa."),
    (29, "1p", r"\sqrt[3]{108a^4b^3}", cbrt(108 * a**4 * b**3), r"3ab\sqrt[3]{4a}",
     3 * a * b * cbrt(4 * a), 2, None),
    (30, "1q", r"\sqrt{5a^3} \div \sqrt{24b^2}", sqrt(5 * a**3) / sqrt(24 * b**2),
     r"\dfrac{a\sqrt{5a}}{2b\sqrt{6}} = \dfrac{a\sqrt{30a}}{12b}", a * sqrt(30 * a) / (12 * b), 3,
     None),
    (31, "1r", r"2\sqrt[3]{27x^2} \div 3\sqrt[3]{16a^2b^4}",
     2 * cbrt(27 * x**2) / (3 * cbrt(16 * a**2 * b**4)),
     r"\dfrac{\sqrt[3]{x^2}}{b\sqrt[3]{2a^2b}} = \dfrac{\sqrt[3]{4ab^2x^2}}{2ab^2}",
     cbrt(4 * a * b**2 * x**2) / (2 * a * b**2), 3, None),
    (32, "1s", r"\sqrt[10]{m^{11}n^{10}t^{20}}", root(m**11 * n_**10 * t**20, 10),
     r"mnt^2\sqrt[10]{m}", m * n_ * t**2 * root(m, 10), 2, None),
    (33, "1t", r"\left(\sqrt{18x^2y} \cdot \sqrt{2xy^3}\right) \div \sqrt{12x^3y^4}",
     sqrt(18 * x**2 * y) * sqrt(2 * x * y**3) / sqrt(12 * x**3 * y**4),
     r"\dfrac{\sqrt{36x^3y^4}}{\sqrt{12x^3y^4}} = \sqrt{3}", sqrt(3), 3, None),
]:
    item(n, f"{F_SIMP} {lit}", SIMPLE.format(tx), f"${rt}$.",
         lambda ex=ex, rx=rx: igual(ex, rx), dificultad=dif, notas=nota)

# ---------- 2. Radicales semejantes ----------
EXPR = "Simplifica la expresión ${}$."
for n, lit, tx, ex, rt, rx, dif in [
    (34, "2a", r"5\sqrt{2} + 8\sqrt{3} + 9\sqrt{2} - \sqrt{3}",
     5 * sqrt(2) + 8 * sqrt(3) + 9 * sqrt(2) - sqrt(3), r"14\sqrt{2} + 7\sqrt{3}",
     14 * sqrt(2) + 7 * sqrt(3), 1),
    (35, "2b", r"5\sqrt{27} - \sqrt{147} + \sqrt{12}", 5 * sqrt(27) - sqrt(147) + sqrt(12),
     r"15\sqrt{3} - 7\sqrt{3} + 2\sqrt{3} = 10\sqrt{3}", 10 * sqrt(3), 2),
    (36, "2c", r"2\sqrt[3]{250} + \sqrt[3]{16} - 3\sqrt[3]{54}",
     2 * cbrt(250) + cbrt(16) - 3 * cbrt(54),
     r"10\sqrt[3]{2} + 2\sqrt[3]{2} - 9\sqrt[3]{2} = 3\sqrt[3]{2}", 3 * cbrt(2), 2),
    (37, "2d", r"\sqrt{\dfrac{24}{25}} + 12\sqrt{\dfrac{2}{3}} - 8\sqrt{\dfrac{3}{2}}",
     sqrt(Rational(24, 25)) + 12 * sqrt(Rational(2, 3)) - 8 * sqrt(Rational(3, 2)),
     r"\dfrac{2\sqrt{6}}{5} + 4\sqrt{6} - 4\sqrt{6} = \dfrac{2\sqrt{6}}{5}", 2 * sqrt(6) / 5, 3),
]:
    item(n, f"{F_SIMP} {lit}", EXPR.format(tx), f"${rt}$.",
         lambda ex=ex, rx=rx: igual(ex, rx), dificultad=dif)

# ---------- Potencias y raíces de radicales ----------
EFECT = ("Efectúa y simplifica el resultado si es posible (las letras representan números "
         "positivos): ${}$.")
for n, lit, tx, ex, rt, rx, dif, nota in [
    (38, "1a", r"(2\sqrt{5})^2", (2 * sqrt(5))**2, "20", 20, 1, None),
    (39, "1b", r"\left(4a\sqrt[3]{4b^2}\right)^2", (4 * a * cbrt(4 * b**2))**2,
     r"16a^2\sqrt[3]{16b^4} = 32a^2b\sqrt[3]{2b}", 32 * a**2 * b * cbrt(2 * b), 2, None),
    (40, "1c", r"\left(\sqrt[4]{x^2}\right)^3", root(x**2, 4)**3,
     r"\sqrt[4]{x^6} = x\sqrt{x}", x * sqrt(x), 2, None),
    (41, "1d", r"\left(\sqrt{a}\,\sqrt[3]{b}\,\sqrt[4]{c}\right)^5",
     (sqrt(a) * cbrt(b) * root(c, 4))**5,
     r"a^2bc\,\sqrt[12]{a^6b^8c^3}", a**2 * b * c * root(a**6 * b**8 * c**3, 12), 3, None),
    (42, "1e", r"\left(\sqrt[5]{81ab^3} \cdot \sqrt[6]{9a^3b^4}\right)^3",
     (root(81 * a * b**3, 5) * root(9 * a**3 * b**4, 6))**3,
     r"27a^2b^3\,\sqrt[10]{81ab^8}", 27 * a**2 * b**3 * root(81 * a * b**8, 10), 3, None),
    (43, "1f", r"\sqrt{\sqrt[3]{a^2}}", sqrt(cbrt(a**2)), r"\sqrt[6]{a^2} = \sqrt[3]{a}", cbrt(a),
     1, None),
    (44, "1g", r"\sqrt[3]{3\sqrt[5]{3}}", cbrt(3 * root(3, 5)),
     r"\sqrt[15]{3^6} = \sqrt[5]{3^2} = \sqrt[5]{9}", root(9, 5), 2,
     "El texto alternativo del módulo está confuso («raíz cúbica de 3 elevado a la 5 raíz "
     "cuadrada de 3»); se respetó la fórmula impresa ∛(3·⁵√3)."),
    (45, "1h", r"\sqrt[3]{2\sqrt{2}}", cbrt(2 * sqrt(2)), r"\sqrt[6]{2^3} = \sqrt{2}", sqrt(2), 2,
     None),
    (46, "1i", r"\sqrt[4]{\sqrt[3]{16}}", root(cbrt(16), 4), r"\sqrt[12]{2^4} = \sqrt[3]{2}",
     cbrt(2), 2, None),
    (47, "1j", r"\sqrt{\sqrt{\sqrt{2}}}", sqrt(sqrt(sqrt(2))), r"\sqrt[8]{2}", root(2, 8), 1, None),
]:
    item(n, f"{F_POT} {lit}", EFECT.format(tx), f"${rt}$.",
         lambda ex=ex, rx=rx: igual(ex, rx), dificultad=dif, notas=nota)
