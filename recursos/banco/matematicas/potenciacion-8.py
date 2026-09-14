"""Banco de ejercicios — Matemáticas 8° — Potenciación en R con exponentes enteros
(producto y cociente de potencias, exponente 0, potencia de una potencia, de un producto y de un
cociente, exponentes negativos).
Fuente: módulo de Matemáticas 8° de las Guías de Apoyo (Adriana Quintero Palomino), Tema 1;
se lee en recursos/matematicas/Guías pedagógicas Matemáticas/markdown/08 - Modulo_Matematicas_Octavo.md
DBA: matematicas-8-9 («opera con formas simbólicas que representan números»).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/potenciacion-8.py
"""
import sympy as sp
from sympy import Integer, Rational, symbols

from ejercicios import ejercicio

F_PROD = ("módulo 8° (Quintero Palomino), Tema 1, Producto y cociente de potencias — "
          "Practica lo aprendido")
F_POT = ("módulo 8° (Quintero Palomino), Tema 1, Potencia de una potencia, de un producto y "
         "de un cociente — Practica lo aprendido")
COMUN = dict(tema="potenciación", grados=[8], dba=["matematicas-8-9"])
m, x, z, b, p, q, r, y = symbols("m x z b p q r y", positive=True)
a = symbols("a", positive=True, integer=True)
aa = symbols("a", positive=True)


def item(n, fuente, enunciado, respuesta, comprobar, dificultad=1, tipo="calculo", notas=None):
    extra = dict(notas=notas) if notas else {}

    def envuelta():
        assert bool(comprobar()), "la comprobación dio falso"
    envuelta.__wrapped__ = comprobar          # la huella usa el código de la comprobación
    ejercicio(id=f"potenciacion-8-{n:03d}", fuente=fuente, enunciado=enunciado,
              respuesta=respuesta, tipo=tipo, dificultad=dificultad, **extra, **COMUN)(envuelta)


def igual(u, v):
    assert sp.simplify(sp.powsimp(u - v, force=True)) == 0, f"{u} ≠ {v}"
    return True


# ---------- 1. Producto y cociente de potencias ----------
SIMPL = "Simplifica ${}$."
for n, lit, tx, ex, rt, rx, dif in [
    (1, "1a", r"m^3 \cdot m^{11}", m**3 * m**11, "m^{14}", m**14, 1),
    (2, "1b", r"(x^3)(x^9)", x**3 * x**9, "x^{12}", x**12, 1),
    (3, "1c", r"(x^{2a})(x^a)$, con $a \in \mathbb{Z}", x**(2 * a) * x**a, "x^{3a}", x**(3 * a), 2),
    (4, "1d", r"2^5 \cdot 3^2 \cdot 5 \cdot 2^2 \cdot 3^3 \cdot 5^2",
     Integer(2)**5 * 3**2 * 5 * 2**2 * 3**3 * 5**2,
     r"2^7 \cdot 3^5 \cdot 5^3 = 3\,888\,000", Integer(2)**7 * 3**5 * 5**3, 2),
    (5, "1e", r"(3a)(3^5a^4)", 3 * aa * 3**5 * aa**4, "3^6a^5 = 729a^5", 3**6 * aa**5, 1),
    (6, "1f", r"2^{10} \div 2^{13}", Rational(2**10, 2**13), r"2^{-3} = \dfrac{1}{8}", Rational(1, 8), 1),
    (7, "1g", r"z^3 \div z^3$, donde $z \in \mathbb{R}$, $z \neq 0", z**3 / z**3, "z^0 = 1", 1, 1),
    (8, "1h", r"(5x)(5x) \div 5^3x^3$, donde $x \in \mathbb{R}$, $x \neq 0",
     (5 * x) * (5 * x) / (5**3 * x**3), r"\dfrac{1}{5x}", 1 / (5 * x), 2),
    (9, "1i", r"3^2b^6 \div 3b^4$, donde $b \in \mathbb{R}$, $b \neq 0", 3**2 * b**6 / (3 * b**4),
     "3b^2", 3 * b**2, 1),
    (10, "1j", r"4^2a \div 4a^2$, donde $a \in \mathbb{R}$, $a \neq 0", 4**2 * aa / (4 * aa**2),
     r"\dfrac{4}{a}", 4 / aa, 1),
]:
    item(n, f"{F_PROD} {lit}", SIMPL.format(tx), f"${rt}$.",
         lambda ex=ex, rx=rx: igual(ex, rx), dificultad=dif)

# ---------- 2. Verdadero o falso ----------
VF = "Determina si el enunciado es verdadero o falso y justifica: {}."
for n, lit, tx, valor, rt, dif in [
    (11, "2a", "$2^3 + 3^3 = 5^3$", 2**3 + 3**3 == 5**3,
     r"Falso: $8 + 27 = 35$ y $5^3 = 125$.", 1),
    (12, "2b", "$2^3 + 3^3 = 6^3$", 2**3 + 3**3 == 6**3,
     r"Falso: $8 + 27 = 35$ y $6^3 = 216$.", 1),
    (13, "2c", r"$2^3 \cdot 3^3 = 6^9$", 2**3 * 3**3 == 6**9,
     r"Falso: $2^3 \cdot 3^3 = (2 \cdot 3)^3 = 6^3$, no $6^9$.", 1),
    (14, "2d", "$3^3 + 3^3 = 3^4$", 3**3 + 3**3 == 3**4,
     r"Falso: $3^3 + 3^3 = 2 \cdot 3^3 = 54$ y $3^4 = 81$.", 2),
    (15, "2e", "$5^3 + 5^3 + 5^3 + 5^3 + 5^3 = 5^4$", 5 * 5**3 == 5**4,
     r"Verdadero: $5 \cdot 5^3 = 5^4$.", 2),
    (16, "2f", "$3^3$ es un factor de $3^3 + 3^5$", (3**3 + 3**5) % 3**3 == 0,
     r"Verdadero: $3^3 + 3^5 = 3^3(1 + 3^2) = 3^3 \cdot 10$.", 2),
    (17, "2g", r"$\dfrac{5a^2}{7b^2} = \dfrac{5^2a^2}{7^2b^2}$ (con $a \neq 0$, $b \neq 0$)",
     Rational(5, 7) == Rational(25, 49),
     r"Falso: el segundo es $\dfrac{25}{49} \cdot \dfrac{a^2}{b^2}$ y $\dfrac{25}{49} \neq "
     r"\dfrac{5}{7}$; elevar numerador y denominador al cuadrado cambia la fracción.", 2),
    (18, "2h", r"$\dfrac{2}{3} = \dfrac{2^2}{3^2}$", Rational(2, 3) == Rational(4, 9),
     r"Falso: $\dfrac{2^2}{3^2} = \dfrac{4}{9} \neq \dfrac{2}{3}$.", 1),
    (19, "2i", r"si $10^{-4} \cdot 10^{-4} = 10^n$, entonces $n = 8$",
     sp.solve(sp.Eq(-4 + -4, symbols("n")), symbols("n")) == [8],
     r"Falso: $10^{-4} \cdot 10^{-4} = 10^{-8}$, así que $n = -8$.", 2),
    (20, "2j", r"si $10^n \cdot 10^n = 10^{-4}$, entonces $n = -2$",
     sp.solve(sp.Eq(2 * symbols("n"), -4), symbols("n")) == [-2],
     r"Verdadero: $10^{2n} = 10^{-4}$, así que $2n = -4$ y $n = -2$.", 2),
]:
    item(n, f"{F_PROD} {lit}", VF.format(tx), rt,
         lambda valor=valor, rt=rt: valor == rt.startswith("Verdadero"),
         dificultad=dif, tipo="argumentacion")

# ---------- Potencia de una potencia, de un producto y de un cociente ----------
POS = ("Simplifica y escribe la respuesta solo con exponentes positivos (ninguna variable "
       "toma el valor $0$): ${}$.")
for n, lit, tx, ex, rt, rx, dif in [
    (21, "1a", r"(5a^2)^3", (5 * aa**2)**3, "125a^6", 125 * aa**6, 1),
    (22, "1b", r"3(x^3)^2", 3 * (x**3)**2, "3x^6", 3 * x**6, 1),
    (23, "1c", r"(3a^2)^3", (3 * aa**2)**3, "27a^6", 27 * aa**6, 1),
    (24, "1d", r"(2y^5) \div (2y^5)", (2 * y**5) / (2 * y**5), "1", 1, 1),
    (25, "1e", r"\left(\dfrac{p^3q^0}{r^2}\right)^{-1}", (p**3 * q**0 / r**2)**-1,
     r"\dfrac{r^2}{p^3}", r**2 / p**3, 2),
    (26, "1f", r"\dfrac{x^{-2} + y^{-2}}{(xy)^{-2}}", (x**-2 + y**-2) / (x * y)**-2,
     "x^2 + y^2", x**2 + y**2, 3),
    (27, "1g", r"\dfrac{2^{-1} + 3^{-1}}{2^{-1}}", (Rational(1, 2) + Rational(1, 3)) / Rational(1, 2),
     r"\dfrac{5}{3}", Rational(5, 3), 2),
    (28, "1h", r"(x^2y^{-2})^{-1}(x^3y^0)^2", (x**2 * y**-2)**-1 * (x**3 * y**0)**2,
     "x^4y^2", x**4 * y**2, 2),
    (29, "1i", r"\left(\dfrac{p^{-3}q^{-2}}{2^0r^{-1}}\right)^{-2}",
     (p**-3 * q**-2 / (2**0 * r**-1))**-2, r"\dfrac{p^6q^4}{r^2}", p**6 * q**4 / r**2, 3),
    (30, "1j", r"\dfrac{2^{-1} + 1^{-1}}{2^{-1} - 1^{-1}}",
     (Rational(1, 2) + 1) / (Rational(1, 2) - 1), "-3", -3, 2),
]:
    item(n, f"{F_POT} {lit}", POS.format(tx), f"${rt}$.",
         lambda ex=ex, rx=rx: igual(ex, rx), dificultad=dif)
