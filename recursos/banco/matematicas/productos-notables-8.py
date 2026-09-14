"""Banco de ejercicios — Álgebra 8° — Productos notables.
Fuente: módulo de Matemáticas 8° de las Guías de Apoyo (Adriana Quintero Palomino), Tema 3;
se lee en recursos/matematicas/Guías pedagógicas Matemáticas/markdown/08 - Modulo_Matematicas_Octavo.md
OJO: en este tema casi todas las fórmulas del .docx son imágenes WMF con texto alternativo; la
copia markdown las pierde y vuelve a numerar los literales. Aquí los literales (a, b, c…) siguen
el orden del .docx original, y cada fórmula se transcribió de la imagen impresa (no del texto
alternativo, que a veces no coincide: ver `notas`).
No se incluyeron: 8i «(2 - 5 + 3)(2 + 5 - 3)» (se perdieron las letras en el original);
12l (es el mismo producto que 8g); ICFES 9 (perímetro de ABYXZC: la figura no trae medidas) e
ICFES 10 (depende de la figura y dos opciones son equivalentes: (a+b)²−(a−b)² = 4ab);
Pasatiempos (probabilidad y lógica, fuera del tema).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/productos-notables-8.py
"""
import sympy as sp

from ejercicios import ejercicio, ejercicio_manual, expresion as E, tex

AUTORA = "módulo 8° (Quintero Palomino), Tema 3"
PNL = f"{AUTORA}, Productos notables — Practica lo aprendido"
ICFES = f"{AUTORA}, Productos notables — Prepárate para el ICFES"
COMUN = dict(tema="productos notables", grados=[8], dba=["matematicas-8-3", "matematicas-8-9"])
MODELO = dict(COMUN, dba=["matematicas-8-8", "matematicas-8-9"])
_n = [0]


def _id():
    _n[0] += 1
    return f"productos-notables-8-{_n[0]:03d}"


def serie_productos(instr, fuente, filas, modo="expandido", base=COMUN, tipo="calculo"):
    """Filas (literal, expresión, respuesta, dificultad[, opciones]). opciones: etex / rtex
    (LaTeX escrito a mano, p. ej. con exponentes negativos), notas. La comprobación desarrolla
    la expresión con SymPy y la compara con la respuesta escrita a mano."""
    for lit, expr, ans, dif, *resto in filas:
        opc = resto[0] if resto else {}
        meta = dict(base, id=_id(), tipo=tipo, dificultad=dif, fuente=f"{fuente} {lit}",
                    enunciado=instr.replace("…", f"${opc.get('etex') or tex(expr)}$"),
                    respuesta=f"${opc.get('rtex') or tex(ans)}$.")
        if "notas" in opc:
            meta["notas"] = opc["notas"]

        def comprobar(expr=expr, ans=ans, modo=modo):
            a, b = E(expr), E(ans)
            assert sp.expand(a - b) == 0, "la respuesta no es igual a la expresión"
            if modo == "expandido":
                assert sp.expand(b) == b, "la respuesta no está desarrollada"
            else:  # «cuadrado»: la respuesta es el cuadrado de un binomio
                assert isinstance(b, sp.Pow) and b.exp == 2 and len(sp.Add.make_args(b.base)) == 2
        ejercicio(**meta)(comprobar)


def opciones(*items):
    return r" \begin{opciones} " + " ".join(r"\item " + i for i in items) + r" \end{opciones}"


# ---------- 1. (x + a)(x + b) ----------
serie_productos(
    "Calcula aplicando el producto notable de la forma $(x + a)(x + b)$: …", PNL, [
        ("1a", "(x - 9)(x - 12)", "x^2 - 21x + 108", 1),
        ("1b", "(a - 4)(a - 2)", "a^2 - 6a + 8", 1),
        ("1c", "(a + 7)(a - 12)", "a^2 - 5a - 84", 1),
        ("1d", "(a + 8)(a + 7)", "a^2 + 15a + 56", 1),
        ("1e", "(7a x + 1)(7a x - 6)", "49a^2x^2 - 35a x - 6", 2),
        ("1f", "(5a^2 - a)(5a^2 - 20)", "25a^4 - 5a^3 - 100a^2 + 20a", 2),
        ("1g", "(6a^3 + 5)(6a^3 + 7)", "36a^6 + 72a^3 + 35", 1),
        ("1h", "(0.5a^2x^7 - 7)(0.5a^2x^7 + 6)", "0.25a^4x^14 - 0.5a^2x^7 - 42", 2),
        ("1i", "(x^(-3)y^(-4) + 5)(x^(-3)y^(-4) + 7)", "x^(-6)y^(-8) + 12x^(-3)y^(-4) + 35", 2,
         dict(etex=r"\left(x^{-3}y^{-4} + 5\right)\left(x^{-3}y^{-4} + 7\right)",
              rtex=r"x^{-6}y^{-8} + 12x^{-3}y^{-4} + 35",
              notas="En la imagen del módulo el segundo factor sale cortado y el texto "
                    "alternativo dice «x^{-4}»; se usó x^{-3}y^{-4} en los dos factores, como "
                    "exige la forma (x + a)(x + b).")),
        ("1j", "((3/4)a^(-2) + 6)((3/4)a^(-2) + 2)", "(9/16)a^(-4) + 6a^(-2) + 12", 2,
         dict(etex=r"\left(\frac{3}{4}a^{-2} + 6\right)\left(\frac{3}{4}a^{-2} + 2\right)",
              rtex=r"\frac{9}{16}a^{-4} + 6a^{-2} + 12")),
        ("1k", "(a^(-3) + a)(a^(-3) + 7a)", "a^(-6) + 8a^(-2) + 7a^2", 3,
         dict(etex=r"\left(a^{-3} + a\right)\left(a^{-3} + 7a\right)",
              rtex=r"a^{-6} + 8a^{-2} + 7a^{2}")),
        ("1l", "(a^(-5) + b^4)(a^(-5) + 8b^4)", "a^(-10) + 9a^(-5)b^4 + 8b^8", 2,
         dict(etex=r"\left(a^{-5} + b^{4}\right)\left(a^{-5} + 8b^{4}\right)",
              rtex=r"a^{-10} + 9a^{-5}b^{4} + 8b^{8}")),
        ("1m", "((3/4)h + 7)((3/4)h - 3)", "(9/16)h^2 + 3h - 21", 2),
        ("1n", "(5 - 2x)(5 + 3x)", "25 + 5x - 6x^2", 1),
        ("1o", "213*215", "45795", 1,
         dict(etex=r"213 \cdot 215", rtex=r"(200 + 13)(200 + 15) = 40\,000 + 28 \cdot 200 + 195 "
                                          r"= 45\,795")),
        ("1p", "170*180", "30600", 1,
         dict(etex=r"170 \cdot 180", rtex=r"(175 - 5)(175 + 5) = 175^{2} - 25 = 30\,600")),
    ])

# ---------- 2. Cuadrado de un binomio ----------
serie_productos("Resuelve aplicando el cuadrado de un binomio: …", PNL, [
    ("2a", "(a - 3)^2", "a^2 - 6a + 9", 1),
    ("2b", "(2a + 5)^2", "4a^2 + 20a + 25", 1),
    ("2c", "(3a + 4b)^2", "9a^2 + 24a b + 16b^2", 1),
    ("2d", "(5a - 6b)^2", "25a^2 - 60a b + 36b^2", 1),
    ("2e", "(8a - 3)^2", "64a^2 - 48a + 9", 1),
    ("2f", "(7a^2c + 2)^2", "49a^4c^2 + 28a^2c + 4", 2),
    ("2g", "(14a b c - 2d)^2", "196a^2b^2c^2 - 56a b c d + 4d^2", 2),
    ("2h", "(15a^3 + b^4)^2", "225a^6 + 30a^3b^4 + b^8", 2),
    ("2i", "(7x^(-2) + 6)^2", "49x^(-4) + 84x^(-2) + 36", 2,
     dict(etex=r"\left(7x^{-2} + 6\right)^{2}", rtex=r"49x^{-4} + 84x^{-2} + 36",
          notas="El texto alternativo de la imagen dice «7x²»; la imagen impresa dice 7x^{-2}.")),
    ("2j", "(2a^(-1) - 3a^2)^2", "4a^(-2) - 12a + 9a^4", 2,
     dict(etex=r"\left(2a^{-1} - 3a^{2}\right)^{2}", rtex=r"4a^{-2} - 12a + 9a^{4}")),
    ("2k", "(5a^2b - 6a b^3)^2", "25a^4b^2 - 60a^3b^4 + 36a^2b^6", 2),
    ("2l", "(15a^2b^4 - 16a b^3)^2", "225a^4b^8 - 480a^3b^7 + 256a^2b^6", 2),
    ("2m", "((2/5)h^(-2) - (3/7)k^(-4))^2", "(4/25)h^(-4) - (12/35)h^(-2)k^(-4) + (9/49)k^(-8)", 3,
     dict(etex=r"\left(\frac{2}{5}h^{-2} - \frac{3}{7}k^{-4}\right)^{2}",
          rtex=r"\frac{4}{25}h^{-4} - \frac{12}{35}h^{-2}k^{-4} + \frac{9}{49}k^{-8}")),
    ("2n", "((5/3)a - (3/5)b)^2", "(25/9)a^2 - 2a b + (9/25)b^2", 2),
    ("2o", "(0.2x - 0.3y)^2", "0.04x^2 - 0.12x y + 0.09y^2", 2),
    ("2p", "(0.9a - 1.3b)^2", "0.81a^2 - 2.34a b + 1.69b^2", 2),
    ("2q", "((3/5)x^(-1) - 0.7y)^2", "(9/25)x^(-2) - 0.84x^(-1)y + 0.49y^2", 3,
     dict(etex=r"\left(\frac{3}{5}x^{-1} - 0{,}7y\right)^{2}",
          rtex=r"\frac{9}{25}x^{-2} - 0{,}84x^{-1}y + 0{,}49y^{2}")),
    ("2r", "(0.8r^(-3) - (10/7)t^2)^2", "0.64r^(-6) - (16/7)r^(-3)t^2 + (100/49)t^4", 3,
     dict(etex=r"\left(0{,}8r^{-3} - \frac{10}{7}t^{2}\right)^{2}",
          rtex=r"0{,}64r^{-6} - \frac{16}{7}r^{-3}t^{2} + \frac{100}{49}t^{4}",
          notas="El texto alternativo dice «r elevado a la menos menos»; la imagen dice r^{-3}.")),
    ("2s", "19^2", "361", 1, dict(etex="19^{2}", rtex=r"(20 - 1)^{2} = 400 - 40 + 1 = 361")),
    ("2t", "27^2", "729", 1, dict(etex="27^{2}", rtex=r"(30 - 3)^{2} = 900 - 180 + 9 = 729")),
    ("2u", "42^2", "1764", 1, dict(etex="42^{2}", rtex=r"(40 + 2)^{2} = 1600 + 160 + 4 = 1764")),
    ("2v", "33^2", "1089", 1, dict(etex="33^{2}", rtex=r"(30 + 3)^{2} = 900 + 180 + 9 = 1089")),
    ("2w", "103^2", "10609", 1,
     dict(etex="103^{2}", rtex=r"(100 + 3)^{2} = 10\,000 + 600 + 9 = 10\,609")),
    ("2x", "99^2", "9801", 1,
     dict(etex="99^{2}", rtex=r"(100 - 1)^{2} = 10\,000 - 200 + 1 = 9801")),
])

# ---------- 3. Problemas ----------
a, b, c, d, h, m, q, r = sp.symbols("a b c d h m q r", positive=True)


@ejercicio(
    id=_id(), tipo="contexto", dificultad=2, fuente=f"{PNL} 3a",
    enunciado=r"Un terreno de forma cuadrada mide $a$ metros por lado. Debido a un nuevo loteo, "
              r"su frente aumentó en $d$ metros y su fondo disminuyó en $b$ metros. Determina la "
              r"nueva área del terreno.",
    respuesta=r"$(a + d)(a - b) = a^{2} - ab + ad - bd$ metros cuadrados.", **MODELO)
def _():
    assert sp.expand((a + d) * (a - b) - (a**2 - a * b + a * d - b * d)) == 0


@ejercicio(
    id=_id(), tipo="contexto", dificultad=2, fuente=f"{PNL} 3b",
    enunciado=r"Un triángulo tiene base y altura de $c$ metros de longitud. Si la altura crece "
              r"$q$ metros y la base disminuye $m$ metros, ¿qué expresión da la nueva área?",
    respuesta=r"$\dfrac{(c - m)(c + q)}{2} = \dfrac{c^{2} + cq - cm - mq}{2}$ metros cuadrados.",
    **MODELO)
def _():
    assert sp.expand((c - m) * (c + q) / 2 - (c**2 + c * q - c * m - m * q) / 2) == 0


# ---------- 4. Cubo de un binomio ----------
serie_productos("Desarrolla aplicando el cubo de un binomio: …", PNL, [
    ("4a", "(2a + 1)^3", "8a^3 + 12a^2 + 6a + 1", 1),
    ("4b", "(3a - 2)^3", "27a^3 - 54a^2 + 36a - 8", 1),
    ("4c", "((4/3)x - 3)^3", "(64/27)x^3 - 16x^2 + 36x - 27", 2),
    ("4d", "(2r - m)^3", "8r^3 - 12r^2m + 6r m^2 - m^3", 1),
    ("4e", "(t^5 + 2t)^3", "t^15 + 6t^11 + 12t^7 + 8t^3", 2),
    ("4f", "((3/4)x - (4/3)y)^3", "(27/64)x^3 - (9/4)x^2y + 4x y^2 - (64/27)y^3", 3),
    ("4g", "(a^4 - b^4)^3", "a^12 - 3a^8b^4 + 3a^4b^8 - b^12", 2),
    ("4h", "(2a^(-1) + 3a)^3", "8a^(-3) + 36a^(-1) + 54a + 27a^3", 3,
     dict(etex=r"\left(2a^{-1} + 3a\right)^{3}", rtex=r"8a^{-3} + 36a^{-1} + 54a + 27a^{3}")),
    ("4i", "((2/5)a - (5/2)b)^3", "(8/125)a^3 - (6/5)a^2b + (15/2)a b^2 - (125/8)b^3", 3),
    ("4j", "(4a + 5b)^3", "64a^3 + 240a^2b + 300a b^2 + 125b^3", 2),
    ("4k", "(r^2 + r c^2)^3", "r^6 + 3r^5c^2 + 3r^4c^4 + r^3c^6", 2),
    ("4l", "(3r - (1/3)r)^3", "(512/27)r^3", 2,
     dict(rtex=r"27r^{3} - 9r^{3} + r^{3} - \frac{1}{27}r^{3} = \frac{512}{27}r^{3}",
          notas="Los dos términos del binomio son semejantes: también se puede reducir primero, "
                "(8r/3)³ = 512r³/27.")),
])

# ---------- 5 y 6. Trinomio → cuadrado de un binomio ----------
serie_productos("Escribe como el cuadrado de un binomio suma: …", PNL, [
    ("5a", "x^2 + 2x y^2 + y^4", "(x + y^2)^2", 1),
    ("5b", "x^2 + 2x y + y^2", "(x + y)^2", 1),
    ("5c", "a^2 + 2a b + b^2", "(a + b)^2", 1),
    ("5d", "m^2 + 2m n + n^2", "(m + n)^2", 1),
    ("5e", "a^2x^2 + 2a x b y + b^2y^2", "(a x + b y)^2", 2),
    ("5f", "9x^2 + 18x y^2 + 9y^4", "(3x + 3y^2)^2", 2,
     dict(rtex=r"\left(3x + 3y^{2}\right)^{2} = 9\left(x + y^{2}\right)^{2}")),
    ("5g", "16m^2 + 40m y + 25y^2", "(4m + 5y)^2", 1),
    ("5h", "9s^2 + 6s t + t^2", "(3s + t)^2", 1),
    ("5i", "36m^6 + 36m^3n^4 + 9n^8", "(6m^3 + 3n^4)^2", 2),
], modo="cuadrado")

serie_productos("Escribe como el cuadrado de un binomio diferencia: …", PNL, [
    ("6a", "x^2 - 2x y^2 + y^4", "(x - y^2)^2", 1),
    ("6b", "x^2 - 2x y + y^2", "(x - y)^2", 1),
    ("6c", "a^2 - 2a b + b^2", "(a - b)^2", 1),
    ("6d", "m^2 - 2m n + n^2", "(m - n)^2", 1),
    ("6e", "a^2x^2 - 2a x b y + b^2y^2", "(a x - b y)^2", 2),
    ("6f", "100m^2 - 80m y^2 + 16y^4", "(10m - 4y^2)^2", 2),
    ("6g", "49a^2b^4 - 14a b^2c + c^2", "(7a b^2 - c)^2", 2),
    ("6h", "4n^8 - 4n^4m^3 + m^6", "(2n^4 - m^3)^2", 2),
    ("6i", "81g^2 - 18g z^5 + z^10", "(9g - z^5)^2", 2),
], modo="cuadrado")

# ---------- 7. Cuadrado de un trinomio ----------
serie_productos("Calcula el cuadrado del trinomio (sugerencia: asocia sus términos): …", PNL, [
    ("7a", "(2a + b + c)^2", "4a^2 + b^2 + c^2 + 4a b + 4a c + 2b c", 2),
    ("7b", "(a - b - c)^2", "a^2 + b^2 + c^2 - 2a b - 2a c + 2b c", 2),
    ("7c", "(2x + y + 2)^2", "4x^2 + y^2 + 4 + 4x y + 8x + 4y", 2),
    ("7d", "(3a + b - c)^2", "9a^2 + b^2 + c^2 + 6a b - 6a c - 2b c", 2),
    ("7e", "(3a + 2b + 2c)^2", "9a^2 + 4b^2 + 4c^2 + 12a b + 12a c + 8b c", 2),
    ("7f", "(2a + b - (1/2)c)^2", "4a^2 + b^2 + (1/4)c^2 + 4a b - 2a c - b c", 3),
    ("7g", "(x + y + 1)^2", "x^2 + y^2 + 1 + 2x y + 2x + 2y", 2),
    ("7h", "(x^2 - y^3 + z^2)^2", "x^4 + y^6 + z^4 - 2x^2y^3 + 2x^2z^2 - 2y^3z^2", 3),
])

# ---------- 8. Trinomios que se asocian ----------
serie_productos("Asocia convenientemente los términos y calcula: …", PNL, [
    ("8a", "(a x + b y + c)(a x - b y - c)", "a^2x^2 - b^2y^2 - 2b c y - c^2", 2),
    ("8b", "(x - y + 1)(x + y + 1)", "x^2 + 2x + 1 - y^2", 2),
    ("8c", "(a + b - c)(a + b + c)", "a^2 + 2a b + b^2 - c^2", 2),
    ("8d", "(2x - 3y + z)(2x + 3y - z)", "4x^2 - 9y^2 + 6y z - z^2", 2),
    ("8e", "(a - 2b - c)(a + 2b + c)", "a^2 - 4b^2 - 4b c - c^2", 2),
    ("8f", "(7 - 2x + y)(7 + 2x - y)", "49 - 4x^2 + 4x y - y^2", 2),
    ("8g", "(x - 1 + y)(x + y + 1)", "x^2 + 2x y + y^2 - 1", 2),
    ("8h", "(3 - 4a + b)(3 + 4a - b)", "9 - 16a^2 + 8a b - b^2", 2),
    ("8j", "(a x + a y - a z)(a x - a y - a z)", "a^2x^2 - 2a^2x z + a^2z^2 - a^2y^2", 3),
    ("8k", "(x^2 + 3x + 7)(x^2 - 3x - 7)", "x^4 - 9x^2 - 42x - 49", 3,
     dict(notas="En el módulo aparece «(y² + 3x + 7)(x³ −− 3x − 7)» (y² en lugar de x², x³ y "
                "un signo doble); se corrigió a (x² + 3x + 7)(x² − 3x − 7), como los "
                "literales vecinos.")),
    ("8l", "(u^2 - 2u + 4)(u^2 + 2u - 4)", "u^4 - 4u^2 + 16u - 16", 3),
    ("8m", "(y^2 - 2y + 9)(y^2 - 2y - 9)", "y^4 - 4y^3 + 4y^2 - 81", 3),
    ("8n", "(u^2 - 3u + 16)(u^2 - 3u - 16)", "u^4 - 6u^3 + 9u^2 - 256", 3),
    ("8o", "(2x + 3y + 1)(2x + 3y - 1)", "4x^2 + 12x y + 9y^2 - 1", 2),
    ("8p", "(a^2 + b^2 + c^2)(a^2 - b^2 + c^2)", "a^4 + 2a^2c^2 + c^4 - b^4", 3),
    ("8q", "(a^2 - a x + x^2)(a^2 + a x + x^2)", "a^4 + a^2x^2 + x^4", 3),
])

# ---------- 9 y 10. Problemas geométricos ----------


@ejercicio(
    id=_id(), tipo="contexto", dificultad=2, fuente=f"{PNL} 9a",
    enunciado=r"En un triángulo, la base y la altura miden $h$ metros. Si ambas longitudes "
              r"disminuyen $r$ metros ($r < h$), determina su nueva área.",
    respuesta=r"$\dfrac{(h - r)^{2}}{2} = \dfrac{h^{2} - 2hr + r^{2}}{2}$ metros cuadrados.",
    notas="Se añadió la condición r < h para que las nuevas medidas sean positivas.", **MODELO)
def _():
    assert sp.expand((h - r) ** 2 / 2 - (h**2 - 2 * h * r + r**2) / 2) == 0


@ejercicio(
    id=_id(), tipo="contexto", dificultad=2, fuente=f"{PNL} 9b",
    enunciado=r"Un terreno cuadrado de $b$ metros de lado se transforma en uno rectangular: el "
              r"frente aumenta $c$ metros y el fondo disminuye esa misma longitud ($c < b$). "
              r"Determina su nueva área. ¿Es mayor o menor que la del terreno cuadrado?",
    respuesta=r"$(b + c)(b - c) = b^{2} - c^{2}$ metros cuadrados: $c^{2}$ metros cuadrados "
              r"menos que el terreno cuadrado.",
    notas="Se añadieron la condición c < b y la comparación con el área inicial.", **MODELO)
def _():
    assert sp.expand((b + c) * (b - c)) == b**2 - c**2
    assert b**2 - sp.expand((b + c) * (b - c)) == c**2 and c**2 > 0


@ejercicio(
    id=_id(), tipo="contexto", dificultad=2, fuente=f"{PNL} 9c",
    enunciado=r"Determina el volumen de un cubo cuya arista mide $3a - 2$ centímetros, con "
              r"$a > \frac{2}{3}$.",
    respuesta=r"$(3a - 2)^{3} = 27a^{3} - 54a^{2} + 36a - 8$ centímetros cúbicos.",
    notas="En el módulo la condición es «a > 0», pero con 0 < a ≤ 2/3 la arista no sería "
          "positiva; se cambió a a > 2/3. (El desarrollo es el mismo del literal 4b.)", **MODELO)
def _():
    assert sp.expand((3 * a - 2) ** 3) == 27 * a**3 - 54 * a**2 + 36 * a - 8
    assert sp.solve(3 * a - 2, a) == [sp.Rational(2, 3)]


@ejercicio(
    id=_id(), tipo="contexto", dificultad=3, fuente=f"{PNL} 9d",
    enunciado=r"Calcula el volumen de una esfera cuyo radio mide $a + 6b$ centímetros, con "
              r"$a > 0$ y $b > 0$. (Volumen de la esfera: $V = \frac{4}{3}\pi r^{3}$.)",
    respuesta=r"$V = \dfrac{4}{3}\pi (a + 6b)^{3} = \dfrac{4}{3}\pi\left(a^{3} + 18a^{2}b + "
              r"108ab^{2} + 216b^{3}\right)$ centímetros cúbicos.",
    notas="En el módulo el radio es «a + 66» con la condición «b > 0», que no aparece en el "
          "radio: se interpretó «66» como «6b». Se añadió la fórmula del volumen.", **MODELO)
def _():
    assert sp.expand((a + 6 * b) ** 3) == a**3 + 18 * a**2 * b + 108 * a * b**2 + 216 * b**3


@ejercicio(
    id=_id(), tipo="contexto", dificultad=1, fuente=f"{PNL} 10",
    enunciado=r"El lado de un cuadrado mide $(3a + 2c)$ centímetros. Calcula su perímetro y su "
              r"área.",
    respuesta=r"Perímetro: $4(3a + 2c) = 12a + 8c$ cm. Área: $(3a + 2c)^{2} = 9a^{2} + 12ac + "
              r"4c^{2}$ cm².", **MODELO)
def _():
    assert sp.expand(4 * (3 * a + 2 * c)) == 12 * a + 8 * c
    assert sp.expand((3 * a + 2 * c) ** 2) == 9 * a**2 + 12 * a * c + 4 * c**2


@ejercicio(
    id=_id(), tipo="argumentacion", dificultad=3, fuente=f"{PNL} 11",
    enunciado=r"Comprueba que $\left(a^{2} + b^{2}\right)\left(c^{2} + d^{2}\right) = "
              r"(ac + bd)^{2} + (ad - bc)^{2}$.",
    respuesta=r"Lado izquierdo: $a^{2}c^{2} + a^{2}d^{2} + b^{2}c^{2} + b^{2}d^{2}$. Lado "
              r"derecho: $a^{2}c^{2} + 2abcd + b^{2}d^{2} + a^{2}d^{2} - 2abcd + b^{2}c^{2}$; los "
              r"términos $\pm 2abcd$ se cancelan y quedan los mismos cuatro términos.", **COMUN)
def _():
    izq = sp.expand((a**2 + b**2) * (c**2 + d**2))
    assert izq == sp.expand((a * c + b * d) ** 2 + (a * d - b * c) ** 2)
    assert izq == a**2 * c**2 + a**2 * d**2 + b**2 * c**2 + b**2 * d**2


# ---------- 12. Por simple inspección ----------
serie_productos("Resuelve por simple inspección: …", PNL, [
    ("12a", "(a x + b y)(a x - b y)", "a^2x^2 - b^2y^2", 1),
    ("12b", "(x^2 + y)^3", "x^6 + 3x^4y + 3x^2y^2 + y^3", 2),
    ("12c", "(a x + y)^3", "a^3x^3 + 3a^2x^2y + 3a x y^2 + y^3", 2),
    ("12d", "(x + 5y)(x + 7y)", "x^2 + 12x y + 35y^2", 1),
    ("12e", "(6x + 8y)(6x - 8y)", "36x^2 - 64y^2", 1),
    ("12f", "(m x + n^3y)^3", "m^3x^3 + 3m^2n^3x^2y + 3m n^6x y^2 + n^9y^3", 3),
    ("12g", "(x^3 + y^2)(x^3 - y^2)", "x^6 - y^4", 1,
     dict(notas="El texto alternativo dice «(x² − y²)» en el segundo factor; la imagen muestra "
                "x³ (cortada), que da la suma por diferencia.")),
    ("12h", "(5x^2 + 7y)^2", "25x^4 + 70x^2y + 49y^2", 1),
    ("12i", "(5x - 7y)^3", "125x^3 - 525x^2y + 735x y^2 - 343y^3", 2),
    ("12j", "(x - 6y)^2", "x^2 - 12x y + 36y^2", 1),
    ("12k", "(a x + b y + c z)^2", "a^2x^2 + b^2y^2 + c^2z^2 + 2a b x y + 2a c x z + 2b c y z", 3),
    ("12m", "(2x - 5y)(2x + 5y)", "4x^2 - 25y^2", 1),
    ("12n", "(x - (1/2)y)^3", "x^3 - (3/2)x^2y + (3/4)x y^2 - (1/8)y^3", 2),
])

# ---------- Prepárate para el ICFES ----------
FIGURA = (r"Un cuadrado de lado $a$ se divide con un corte horizontal y uno vertical, cada uno a "
          r"$b$ unidades de dos lados del cuadrado ($0 < b < a$). Quedan un cuadrado de área "
          r"$(a - b)^{2}$, un cuadrado de área $b^{2}$ y dos rectángulos iguales. ")
x_, y_ = sp.symbols("x y", positive=True)


@ejercicio(
    id=_id(), tipo="seleccion", dificultad=2, fuente=f"{ICFES} 1",
    enunciado=FIGURA + r"Cada uno de los rectángulos tiene un área de:" + opciones(
        "$ab$", "$(b - a)a$", "$(a - b)b$", "$(a - b)a$", "$b(b - a)$"),
    respuesta=r"C: cada rectángulo mide $(a - b)$ por $b$, así que su área es $(a - b)b$.",
    notas="La figura (colores amarillo, verde y azul) se describió en palabras.", **COMUN)
def _():
    rect = (a - b) * b   # lados del rectángulo: a − b y b
    assert sp.expand((a - b) ** 2 + b**2 + 2 * rect - a**2) == 0   # las piezas llenan el cuadrado
    otras = [a * b, (b - a) * a, (a - b) * a, b * (b - a)]
    assert all(sp.expand(o - rect) != 0 for o in otras)


@ejercicio(
    id=_id(), tipo="seleccion", dificultad=2, fuente=f"{ICFES} 2",
    enunciado=FIGURA + r"Si al área del cuadrado de lado $a$ se le restan las áreas de los dos "
              r"rectángulos y la del cuadrado de área $b^{2}$, se obtiene la expresión:" + opciones(
                  r"$a^{2} + 2b(a - b) - b^{2}$", r"$a^{2} + 2b(a - b) + b^{2}$",
                  r"$a^{2} - 2b(a - b) - b^{2}$", r"$a^{2} - 2b(a - b) + b^{2}$"),
    respuesta=r"C: $a^{2} - 2b(a - b) - b^{2}$, que es el área $(a - b)^{2}$ del otro cuadrado.",
    notas="En el módulo la opción D aparece como «a² −− 2b(a − b) + b²»; se escribió con un "
          "solo signo.", **COMUN)
def _():
    correcta = a**2 - 2 * b * (a - b) - b**2
    assert sp.expand(correcta - (a - b) ** 2) == 0
    otras = [a**2 + 2 * b * (a - b) - b**2, a**2 + 2 * b * (a - b) + b**2,
             a**2 - 2 * b * (a - b) + b**2]
    assert all(sp.expand(o - correcta) != 0 for o in otras)


@ejercicio(
    id=_id(), tipo="seleccion", dificultad=2, fuente=f"{ICFES} 3",
    enunciado=FIGURA + r"El producto notable que esta figura interpreta geométricamente es:" +
    opciones(r"$(a + b)^{2} = a^{2} - 2ab - b^{2}$", r"$(a - b)^{2} = a^{2} + 2ab - b^{2}$",
             r"$(a + b)^{2} = a^{2} + 2ab - b^{2}$", r"$(a - b)^{2} = a^{2} - 2ab + b^{2}$"),
    respuesta=r"D: $(a - b)^{2} = a^{2} - 2ab + b^{2}$; es la única igualdad verdadera para "
              r"todos los valores de $a$ y $b$.", **COMUN)
def _():
    igualdades = [((a + b) ** 2, a**2 - 2 * a * b - b**2), ((a - b) ** 2, a**2 + 2 * a * b - b**2),
                  ((a + b) ** 2, a**2 + 2 * a * b - b**2), ((a - b) ** 2, a**2 - 2 * a * b + b**2)]
    verdaderas = [i for i, (izq, der) in enumerate(igualdades) if sp.expand(izq - der) == 0]
    assert verdaderas == [3]


@ejercicio(
    id=_id(), tipo="seleccion", dificultad=1, fuente=f"{ICFES} 4",
    enunciado=r"Dentro de un cuadrado de lado $y$ se dibuja un círculo de radio $x$ que toca los "
              r"cuatro lados. La expresión que representa el área de la parte del cuadrado que no "
              r"ocupa el círculo es:" + opciones(r"$y^{2} - \pi x^{2}$", r"$\pi x^{2}$",
                                                 r"$y^{2}$", r"$\pi x^{2} - y^{2}$"),
    respuesta=r"A: área del cuadrado menos área del círculo, $y^{2} - \pi x^{2}$ (que es "
              r"positiva, porque $y = 2x$ y $4x^{2} > \pi x^{2}$).",
    notas="En el módulo la región pedida es «la figura sombreada» y la descripción dice "
          "«círculo circunscrito»; se escribió en palabras la región (la parte del cuadrado sin "
          "el círculo) y que el círculo está inscrito.", **MODELO)
def _():
    correcta = y_**2 - sp.pi * x_**2
    assert sp.simplify(correcta.subs(y_, 2 * x_)) == (4 - sp.pi) * x_**2 and 4 - sp.pi > 0
    assert sp.simplify((sp.pi * x_**2 - y_**2).subs(y_, 2 * x_) / x_**2) < 0   # D: negativa


@ejercicio(
    id=_id(), tipo="seleccion", dificultad=1, fuente=f"{ICFES} 5",
    enunciado=r"Consideremos un cuadrado de lado $a$. Si duplicamos el lado del cuadrado, podemos "
              r"afirmar que su área:" + opciones("Se duplica.", "No varía.",
                                                "Aumenta cuatro veces.", "No se puede determinar."),
    respuesta=r"C: $(2a)^{2} = 4a^{2}$, el área se multiplica por $4$.", **MODELO)
def _():
    assert sp.expand((2 * a) ** 2) / a**2 == 4


@ejercicio(
    id=_id(), tipo="seleccion", dificultad=1, fuente=f"{ICFES} 6",
    enunciado=r"Si el área de un cuadrado es $\frac{1}{4}a^{2}$, entonces la longitud de su lado, "
              r"con respecto a la de un cuadrado de lado $a$:" + opciones(
                  "Se duplicó.", "Aumentó tres veces.", "Disminuyó cuatro veces.",
                  "Se redujo a la mitad."),
    respuesta=r"D: $\sqrt{\frac{1}{4}a^{2}} = \frac{a}{2}$, el lado se redujo a la mitad.",
    notas="En el módulo dice «un tercer cuadrado» (se refiere a la figura anterior); se "
          "escribió «un cuadrado».", **MODELO)
def _():
    assert sp.sqrt(sp.Rational(1, 4) * a**2) == a / 2


@ejercicio(
    id=_id(), tipo="seleccion", dificultad=1, fuente=f"{ICFES} 7",
    enunciado=r"Considera un cubo de arista $a$. Si se duplica su arista, el volumen del cubo "
              r"obtenido es:" + opciones("$2a^{3}$", "$4a^{3}$", "$6a^{3}$", "$8a^{3}$"),
    respuesta=r"D: $(2a)^{3} = 8a^{3}$.", **MODELO)
def _():
    assert sp.expand((2 * a) ** 3) == 8 * a**3


@ejercicio(
    id=_id(), tipo="seleccion", dificultad=1, fuente=f"{ICFES} 8",
    enunciado=r"Si el volumen de un cubo es $V = \frac{1}{8}a^{3}$, entonces la longitud de su "
              r"arista, con respecto a la de un cubo de arista $a$:" + opciones(
                  "Se duplicó.", "Se redujo a la mitad.", "Se redujo a la tercera parte.",
                  "Se triplicó."),
    respuesta=r"B: $\sqrt[3]{\frac{1}{8}a^{3}} = \frac{a}{2}$, la arista se redujo a la mitad.",
    **MODELO)
def _():
    assert sp.root(sp.Rational(1, 8) * a**3, 3) == a / 2


@ejercicio(
    id=_id(), tipo="seleccion", dificultad=2, fuente=f"{ICFES} 11",
    enunciado=r"¿Cuál de las siguientes igualdades es verdadera para todos los valores de $a$ y "
              r"$b$?" + opciones(r"$(a + b)^{2} - (a - b)^{2} = 4ab$",
                                 r"$(a - b)^{2} - (a + b)^{2} = 4ab$",
                                 r"$(a + b)^{2} + (a - b)^{2} = 4ab$",
                                 r"$(a - b)^{2} + (a + b)^{2} = 4ab$"),
    respuesta=r"A: $(a + b)^{2} - (a - b)^{2} = (a^{2} + 2ab + b^{2}) - (a^{2} - 2ab + b^{2}) = "
              r"4ab$.",
    notas="En el módulo la pregunta es «La figura anterior representa la interpretación "
          "geométrica de:» (cuadrado de lado a + b con cuatro rectángulos ab alrededor de un "
          "cuadrado de lado a − b); se preguntó directamente por la identidad. La opción A "
          "aparece con la errata «(a ams b)».", **COMUN)
def _():
    P, M = (a + b) ** 2, (a - b) ** 2
    lados = [P - M, M - P, P + M, M + P]
    assert [i for i, e in enumerate(lados) if sp.expand(e - 4 * a * b) == 0] == [0]


# ---------- Curiosidades, Proyecto ----------
n_ = sp.symbols("n")


@ejercicio(
    id=_id(), tipo="argumentacion", dificultad=2,
    fuente=f"{AUTORA}, Productos notables — Curiosidades matemáticas",
    enunciado=r"Dile a un amigo: «Piensa un número, multiplícalo por $2$, súmale $18$, calcula la "
              r"mitad y dime el resultado». Si al resultado le restas $9$, obtienes el número que "
              r"pensó tu amigo. ¿Por qué ocurre esto? Explícalo con una expresión algebraica.",
    respuesta=r"Si el número es $n$: $\dfrac{2n + 18}{2} = n + 9$, y $n + 9 - 9 = n$.",
    dba=["matematicas-8-9"], tema="productos notables", grados=[8])
def _():
    assert sp.simplify((2 * n_ + 18) / 2 - 9 - n_) == 0


PROY = f"{AUTORA}, Productos notables — Proyecto"
serie_productos(
    r"El producto $(2x + 1)(x + 5)$ es el área de un rectángulo de lados $2x + 1$ y $x + 5$; "
    r"partiendo el rectángulo en cuatro rectángulos interiores se obtiene "
    r"$2x^{2} + x + 10x + 5 = 2x^{2} + 11x + 5$. Usa ese método para calcular …",
    PROY, [
        ("a", "(2x + 3)(x + 4)", "2x^2 + 11x + 12", 1),
        ("b", "(x + 2)(x + 3)", "x^2 + 5x + 6", 1),
        ("c", "(4x + 1)(2x + 5)", "8x^2 + 22x + 5", 1),
        ("d", "(x + 1)(3x + 4)", "3x^2 + 7x + 4", 1),
    ])

ejercicio_manual(
    id=_id(), tipo="argumentacion", dificultad=2, fuente=f"{PROY}, pregunta inicial",
    enunciado=r"El producto $(2x + 1)(x + 5)$ se puede calcular como el área de un rectángulo "
              r"de lados $2x + 1$ y $x + 5$. ¿Crees que este método sirve solo si los números que "
              r"aparecen son positivos? Explica.",
    respuesta=r"Como dibujo de áreas, sí necesita longitudes positivas (por ejemplo $x > 0$ y "
              r"términos positivos), porque un lado no puede medir un número negativo. Pero la "
              r"igualdad que se obtiene, $(2x + 1)(x + 5) = 2x^{2} + 11x + 5$, es la propiedad "
              r"distributiva y vale para cualquier número real: con términos negativos se "
              r"multiplica igual, término a término, cuidando los signos (o se piensa en áreas "
              r"que se restan).", **COMUN)


@ejercicio(
    id=_id(), tipo="argumentacion", dificultad=2, fuente=f"{PROY}, actividad",
    enunciado=r"Con una hoja cuadrada y dos pliegues se forma un cuadrado de lado $a + b$ "
              r"dividido en cuatro regiones: un cuadrado $A$ de área $b^{2}$, un cuadrado $C$ de "
              r"área $a^{2}$ y dos rectángulos $B$ y $D$ de área $ab$ cada uno. Deduce la fórmula "
              r"del cuadrado de un binomio.",
    respuesta=r"El área total es la suma de las cuatro regiones: "
              r"$(a + b)^{2} = a^{2} + 2ab + b^{2}$.", **COMUN)
def _():
    assert sp.expand((a + b) ** 2) == b**2 + a * b + a**2 + a * b
