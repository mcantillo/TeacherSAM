"""Banco de ejercicios — Álgebra 8° — Factorización.
Fuente: módulo de Matemáticas 8° de las Guías de Apoyo (Adriana Quintero Palomino), Tema 4;
se lee en recursos/matematicas/Guías pedagógicas Matemáticas/markdown/08 - Modulo_Matematicas_Octavo.md
OJO: casi todas las fórmulas de este tema son imágenes WMF en el .docx; la copia markdown las
pierde y vuelve a numerar los literales. Aquí los literales siguen el orden del .docx y cada
fórmula se transcribió de la imagen impresa (el texto alternativo a veces no coincide: `notas`).
Comprobación: la respuesta es igual a la expresión (SymPy la desarrolla) y, en «Factoriza», cada
factor que no es numérico es irreducible sobre los racionales y no le queda factor numérico
entero (factorización completa). En «factor común» se comprueba que el paréntesis ya no tiene
factor común.
No se incluyeron (ver informe a la docente):
- Factores comunes, Practica 1 (factores primos de números: contenido de 6°) y la actividad
  inicial con fracciones (operaciones con racionales, de 7°).
- Factores comunes 4h («57ab² . (16,/,2)», ilegible); 5m (repite 5c); 9o, 9v y 9z (tal como
  están impresos no se factorizan y no se puede saber cuál era la expresión:
  3ab − b − 4 + 18a, 6ab − 4ad − 9bc + 6bd + 15c² − 10cd, 3a³ − 9ax² − x + 3a);
  10k–10p (son las expresiones de 8a–8f, ya factorizadas en 7a–7f; 10o además cambia un signo);
  11f (repite 3g); ICFES «La física y el álgebra» (comprensión de lectura, sin álgebra).
- Trinomios 2u (repite 2h), 6l (repite 2a), 6p (repite 6d); Practica 2 literal a (repite 3l).
- Binomios 5q (repite 5p) y 6l («2x² 2x³ − 8x»: falta un signo).
- Combinación de casos, actividad inicial a (repite trinomios 2b); 2r (repite binomios 6i);
  ICFES «Medir para creer» (lectura y física).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/factorizacion-8.py
"""
import sympy as sp

from ejercicios import ejercicio, ejercicio_manual, expresion as E, tex

A = "módulo 8° (Quintero Palomino), Tema 4"
F0 = f"{A}, Factorización o descomposición factorial — actividad inicial"
F1 = f"{A}, Factorización de expresiones que contienen factores comunes — Practica lo aprendido"
F2I = f"{A}, Factorización de trinomios — actividad inicial"
F2 = f"{A}, Factorización de trinomios — Practica lo aprendido (1)"
F2B = f"{A}, Factorización de trinomios — Practica lo aprendido (2)"
F3I = f"{A}, Factorización de binomios — actividad inicial"
F3 = f"{A}, Factorización de binomios — Practica lo aprendido"
F3C = f"{A}, Factorización de binomios — Prepárate para el ICFES"
F4I = f"{A}, Factorización con combinación de casos — actividad inicial"
F4 = f"{A}, Factorización con combinación de casos — Practica lo aprendido"
COMUN = dict(tema="factorización", grados=[8], dba=["matematicas-8-3", "matematicas-8-9"])
NO = "No se puede factorizar con coeficientes enteros."
_n = [0]


def _id():
    _n[0] += 1
    return f"factorizacion-8-{_n[0]:03d}"


# ---------- comprobaciones ----------

def _hojas(e):
    if e.is_Mul:
        for arg in e.args:
            yield from _hojas(arg)
    elif e.is_Pow and not e.base.is_number:
        yield from _hojas(e.base)
    else:
        yield e


def _factores(ans):
    """Factores de la respuesta tal como está escrita (sin evaluar: al evaluar, SymPy reparte
    9(a + 7b)(a − 7b) en (9a + 63b)(a − 7b)); cada factor se evalúa por separado."""
    return [E(str(h)) for h in _hojas(E(ans, evaluar=False)) if not h.is_number]


def _irreducible(f):
    c, lista = sp.factor_list(f)
    return len(lista) == 1 and lista[0][1] == 1 and not (c.is_integer and abs(c) > 1)


def comprobar_fila(expr, ans, modo):
    a = E(expr)
    if modo == "no":                                   # no se puede factorizar
        c, p = sp.expand(a).as_content_primitive()
        assert c == 1 and _irreducible(p), "sí se puede factorizar"
        return
    b = E(ans)
    assert sp.expand(a - b) == 0, "la respuesta no es igual a la expresión"
    fs = [f for f in _factores(ans) if not f.is_number]
    if modo == "total":
        assert all(_irreducible(f) for f in fs), "la factorización no está completa"
    elif modo == "comun":                               # queda un paréntesis sin factor común
        sumas = [f for f in fs if f.is_Add]
        assert len(sumas) == 1 and sp.factor_terms(sumas[0]) == sumas[0], "queda factor común"
    elif modo == "expandido":
        assert sp.expand(b) == b, "la respuesta no está desarrollada"
    else:                                               # «eq»: producto equivalente
        assert len(fs) >= 2, "la respuesta no es un producto"


def serie(instr, fuente, filas, modo="total", tipo="calculo", base=COMUN):
    """Filas (literal, expresión, respuesta, dificultad[, opciones]); opciones: etex, rtex,
    notas, modo. En modo «no» la respuesta se ignora."""
    for lit, expr, ans, dif, *resto in filas:
        opc = resto[0] if resto else {}
        m = opc.get("modo", modo)
        resp = NO if m == "no" else f"${opc.get('rtex') or tex(ans)}$."
        meta = dict(base, id=_id(), tipo=tipo, dificultad=dif, fuente=f"{fuente} {lit}",
                    enunciado=instr.replace("…", f"${opc.get('etex') or tex(expr)}$"),
                    respuesta=resp)
        if "notas" in opc:
            meta["notas"] = opc["notas"]

        def comprobar(expr=expr, ans=ans, m=m):
            comprobar_fila(expr, ans, m)
        ejercicio(**meta)(comprobar)


def serie_numerica(instr, fuente, filas):
    """Filas (literal, cálculo, forma con factor común, valor): los tres coinciden."""
    for lit, calc, fact, valor in filas:
        meta = dict(COMUN, id=_id(), tipo="calculo", dificultad=1, fuente=f"{fuente} {lit}",
                    enunciado=instr.replace("…", f"${tex(calc)}$"),
                    respuesta=f"${tex(fact)} = {valor}$.")

        def comprobar(calc=calc, fact=fact, valor=valor):
            assert E(calc) == E(fact) == valor
        ejercicio(**meta)(comprobar)


def opciones(*items):
    return r" \begin{opciones} " + " ".join(r"\item " + i for i in items) + r" \end{opciones}"


x, y = sp.symbols("x y", real=True)

# ================= Factorización o descomposición factorial =================
serie("Desarrolla el producto: …", F0, [
    ("a", "4x*(3b + 2b)", "20b x", 1,
     dict(notas="Así aparece en el módulo: el paréntesis tiene términos semejantes (3b + 2b).")),
    ("b", "5x*(x^2 + 11)", "5x^3 + 55x", 1),
    ("c", "(4m - 3)(3m + 2)", "12m^2 - m - 6", 1),
], modo="expandido")

# ================= Factores comunes =================
serie("Aplica la propiedad distributiva: …", F1, [
    ("2a", "a*(b + 1)", "a b + a", 1), ("2b", "-a*(m + n)", "-a m - a n", 1),
    ("2c", "r*(r + s)", "r^2 + r s", 1), ("2d", "3a*(m + d)", "3a m + 3a d", 1),
    ("2e", "2(x + y)", "2x + 2y", 1), ("2f", "x*(a - b)", "a x - b x", 1),
    ("2g", "4x*(y + z)", "4x y + 4x z", 1), ("2h", "a*(a + c)", "a^2 + a c", 1),
    ("2i", "3(a + b)", "3a + 3b", 1), ("2j", "-p*(p + q)", "-p^2 - p q", 1),
    ("2k", "2b*(b + 2)", "2b^2 + 4b", 1), ("2l", "10z*(x + z)", "10x z + 10z^2", 1),
], modo="expandido")

serie_numerica(
    r"Calcula sacando factor común, como en el ejemplo "
    r"$11^{2} - 7 \cdot 11 = 11(11 - 7) = 11 \cdot 4 = 44$: …", F1, [
        ("3a", "12*13 - 60 + 12", "12*(13 - 5 + 1)", 108),
        ("3b", "65*3 + 65*7", "65*(3 + 7)", 650),
        ("3c", "7*13 + 8*13", "13*(7 + 8)", 195),
        ("3d", "7^2 - 28 + 7*17", "7*(7 - 4 + 17)", 140),
        ("3f", "83^2*3 + 83*17", "83*(83*3 + 17)", 22078),
        ("3g", "11^2 - 6*11 + 5*11", "11*(11 - 6 + 5)", 110),
        ("3h", "23^2*5 + 23*11", "23*(23*5 + 11)", 2898),
        ("3i", "7*19 - 3*19", "19*(7 - 3)", 76),
        ("3j", "13^2 - 5*13 + 2*13", "13*(13 - 5 + 2)", 130),
        ("3k", "2*9 + 9^2", "9*(2 + 9)", 99),
        ("3l", "18^2 - 3*18 + 1*18", "18*(18 - 3 + 1)", 288),
    ])


@ejercicio(
    id=_id(), tipo="calculo", dificultad=2, fuente=f"{F1} 3e",
    enunciado=r"Calcula sacando factor común: $45 \cdot 13 - 43 \cdot 3$.",
    respuesta=r"El único factor común es $3$: $3(15 \cdot 13 - 43) = 3 \cdot 152 = 456$.",
    notas="A diferencia de los otros literales, los dos productos no comparten un factor "
          "evidente (¿errata por 45 · 13 − 45 · 3 = 450?). Se dejó como está impreso.", **COMUN)
def _():
    assert 45 * 13 - 43 * 3 == 3 * (15 * 13 - 43) == 456
    assert sp.gcd(45 * 13, 43 * 3) == 3


# 4. Factor que completa la igualdad: (literal, total, factor dado, factor buscado, LaTeX)
FALTANTE = [
    ("4a", "6t^2", "2t", "3t", r"6t^{2} = (2t)(\ ?\ )"),
    ("4b", "48c^5d^4", "-3c^3d^2", "-16c^2d^2", r"48c^{5}d^{4} = \left(-3c^{3}d^{2}\right)(\ ?\ )"),
    ("4c", "72h^3k", "-8h k", "-9h^2", r"72h^{3}k = (-8hk)(\ ?\ )"),
    ("4d", "9a^2b^4", "3a^2b^2", "3b^2", r"9a^{2}b^{4} = \left(3a^{2}b^{2}\right)(\ ?\ )"),
    ("4e", "-28r^4s^3", "-r", "28r^3s^3", r"-28r^{4}s^{3} = (-r)(\ ?\ )"),
    ("4f", "18a^6b^7", "(3a^3b^2)^2", "2b^3", r"\left(3a^{3}b^{2}\right)^{2}(\ ?\ ) = 18a^{6}b^{7}"),
    ("4g", "-35x^3y^5", "7x^2y", "-5x y^4", r"-35x^{3}y^{5} = \left(7x^{2}y\right)(\ ?\ )"),
    ("4i", "30a^3b^4", "(15a b^2)^2", "(2/15)a", r"\left(15ab^{2}\right)^{2}(\ ?\ ) = 30a^{3}b^{4}"),
]
for lit, total, dado, buscado, etex in FALTANTE:
    @ejercicio(id=_id(), tipo="calculo", dificultad=1 if "^2)" not in dado else 2,
               fuente=f"{F1} {lit}", enunciado=f"Encuentra el factor que completa la igualdad: "
                                               f"${etex}$.",
               respuesta=f"${tex(buscado)}$.", **COMUN)
    def _(total=total, dado=dado, buscado=buscado):
        assert sp.expand(E(total) - E(dado) * E(buscado)) == 0
        assert len(sp.Add.make_args(E(buscado))) == 1          # es un monomio

serie("Factoriza sacando el factor común monomio: …", F1, [
    ("5a", "24a^2b + 4a b c", "4a b*(6a + c)", 1),
    ("5b", "15x^3y^2 - 10x^2y^3", "5x^2y^2*(3x - 2y)", 1),
    ("5c", "a^2b^3d - a^2b^2d^2", "a^2b^2d*(b - d)", 1),
    ("5d", "x^3 - 3x^2 + 4x^4", "x^2*(x - 3 + 4x^2)", 1),
    ("5e", "75(r s t^2)^2 + (5r)^3", "25r^2*(3s^2t^4 + 5r)", 2,
     dict(etex=r"75\left(rst^{2}\right)^{2} + (5r)^{3}",
          rtex=r"75r^{2}s^{2}t^{4} + 125r^{3} = 25r^{2}\left(3s^{2}t^{4} + 5r\right)")),
    ("5f", "15a - 27b + 9c", "3(5a - 9b + 3c)", 1),
    ("5g", "5a - a^2 + a^3", "a*(5 - a + a^2)", 1),
    ("5h", "2x^4 + 6x + 8x^3 - 10x^4", "2x*(-4x^3 + 4x^2 + 3)", 2,
     dict(rtex=r"-8x^{4} + 8x^{3} + 6x = 2x\left(-4x^{3} + 4x^{2} + 3\right)",
          notas="El polinomio del módulo tiene términos semejantes (2x⁴ y −10x⁴): se reducen "
                "antes de factorizar.")),
    ("5i", "20m^3 + 30m^4 - 40m^2 - 50m^5", "10m^2*(2m + 3m^2 - 4 - 5m^3)", 1),
    ("5j", "27a^2b^3 - 18a^4b^5 + 45a b^4", "9a b^3*(3a - 2a^3b^2 + 5b)", 2),
    ("5k", "5x^2y^3 + 7x y^4 - 8x^3y^7 - 9x^5y^5", "x y^3*(5x + 7y - 8x^2y^4 - 9x^4y^2)", 2),
    ("5l", "a b c - 2a^2d + 3a c - 5a", "a*(b c - 2a d + 3c - 5)", 1),
    ("5n", "10p^2q^3 + 14p^3q^2 - 18p^4q^3 - 16p^5q^2", "2p^2q^2*(5q + 7p - 9p^2q - 8p^3)", 2),
    ("5o", "14p^3q^4 - 7p^2q^2 + 28p^5q^6 + 21p^7q^2", "7p^2q^2*(2p q^2 - 1 + 4p^3q^4 + 3p^5)", 2),
    ("5p", "0.6a b^5 + 0.4a^2b^3 - 0.8a^3b^4", "0.2a b^3*(3b^2 + 2a - 4a^2b)", 2),
    ("5q", "21a^3b^5 - 1.5a^2b^4 + 0.9a^4b^3", "0.3a^2b^3*(70a b^2 - 5b + 3a^2)", 3,
     dict(notas="Así está impreso; el coeficiente 21 (entre 1,5 y 0,9) podría ser una errata "
                "por 2,1, que daría 0,3a²b³(7ab² − 5b + 3a²).")),
    ("5r", "2.2p^3q^4 + 3.3p^4q^3 + 4.4p^5q^4 - 5.5p^4q^5", "1.1p^3q^3*(2q + 3p + 4p^2q - 5p q^2)", 2),
    ("5s", "(1/2)a^2b^3 + (1/4)a^3b^5 - (1/8)a^5b^5 + (1/16)a^4b^3",
     "(1/16)a^2b^3*(8 + 4a b^2 - 2a^3b^2 + a^2)", 3),
    ("5t", "(4/35)a^2b - (12/5)a b + (8/15)a^2b^3 - (16/25)a^5b^6",
     "(4/525)a b*(15a - 315 + 70a b^2 - 84a^4b^5)", 3,
     dict(rtex=r"\frac{4}{525}ab\left(15a - 315 + 70ab^{2} - 84a^{4}b^{5}\right)")),
    ("5u", "(12/5)m n - (18/7)m^2n + (24/9)m n^2", "(2/105)m n*(126 - 135m + 140n)", 3,
     dict(rtex=r"\frac{2}{105}mn\left(126 - 135m + 140n\right)")),
    ("5v", "(15/21)x^3y^4 - (27/28)x^4y^3 + (9/14)x^2y^3 + (21/35)x^3y^2",
     "(1/140)x^2y^2*(100x y^2 - 135x^2y + 90y + 84x)", 3),
    ("5w", "1.5a - 2.5b", "0.5(3a - 5b)", 1),
    ("5x", "0.6a b^3 + 6a^3b", "0.6a b*(b^2 + 10a^2)", 2),
    ("5y", "(3/4)x^2y - (9/8)x y^2", "(3/8)x y*(2x - 3y)", 2,
     dict(rtex=r"\frac{3}{8}xy(2x - 3y)")),
    ("5z", "2x^4 + 6x", "2x*(x^3 + 3)", 1),
], modo="comun")

serie("Factoriza sacando el factor común: …", F1, [
    ("6a", "3(x + y) + z*(x + y)", "(x + y)(3 + z)", 1),
    ("6b", "e*(f - g) - 4(f - g)", "(f - g)(e - 4)", 1),
    ("6c", "7(r - s) + t*(r - s)", "(r - s)(7 + t)", 1),
    ("6d", "2a*(a + 3) - (3 + a)", "(a + 3)(2a - 1)", 1),
    ("6e", "2x*(x - y) + y*(y - x)", "(x - y)(2x - y)", 2),
    ("6f", "2u*(u - 2v) + v*(u - 2v) + (u - 2v)", "(u - 2v)(2u + v + 1)", 1,
     dict(etex=r"2u(u - 2v) + v(u - 2v) + (u - 2v)")),
    ("6g", "x*(2w - 3v + u) - (2w - 3v + u)", "(2w - 3v + u)(x - 1)", 1,
     dict(notas="En el módulo la primera letra es una X mayúscula; se escribió x.")),
    ("6h", "(s^2 - 2p s + 2s) - (2s - 4p + 4)", "(s - 2p + 2)(s - 2)", 2,
     dict(etex=r"\left(s^{2} - 2ps + 2s\right) - (2s - 4p + 4)")),
    ("6i", "(3t - 3s t) + (r s - r)", "(1 - s)(3t - r)", 2,
     dict(etex=r"(3t - 3st) + (rs - r)")),
    ("6j", "(12x^2 - 8x y) - 5(3x z - 2y z)", "(3x - 2y)(4x - 5z)", 2,
     dict(etex=r"\left(12x^{2} - 8xy\right) - 5(3xz - 2yz)")),
    ("6k", "9m - 3 + 24m^2 - 8m", "(3m - 1)(8m + 3)", 2),
    ("6l", "w*(x - y) - 8(x - y)", "(x - y)(w - 8)", 1),
    ("6m", "7(m - n) + p*(n - m)", "(m - n)(7 - p)", 2),
    ("6n", "u*(v - 2) + 2(2 - v)", "(v - 2)(u - 2)", 2),
    ("6o", "3p*(2q - p) - 2q*(p - 2q)", "(2q - p)(3p + 2q)", 2),
    ("6p", "a*(a - b) + 4b*(a - b) - a*(a - b)", "4b*(a - b)", 1),
    ("6q", "r*(r - s - 2t) + s*(r - s - 2t)", "(r - s - 2t)(r + s)", 1),
    ("6r", "(x^2 - x y + x) - (y - x - 1)", "(x - y + 1)(x + 1)", 2,
     dict(etex=r"\left(x^{2} - xy + x\right) - (y - x - 1)")),
    ("6s", "(9p - 3p q) + (2n q - 6n)", "(3 - q)(3p - 2n)", 2,
     dict(etex=r"(9p - 3pq) + (2nq - 6n)")),
    ("6t", "(p^2 - 2p q) - 2(2q r - p r)", "(p - 2q)(p + 2r)", 2,
     dict(etex=r"\left(p^{2} - 2pq\right) - 2(2qr - pr)")),
])

serie("Determina el factor común de cada grupo y completa la factorización: …", F1, [
    ("7a", "(3x^2 - 3x) + (2x - 2)", "(x - 1)(3x + 2)", 1,
     dict(etex=r"\left(3x^{2} - 3x\right) + (2x - 2)", rtex=r"3x(x - 1) + 2(x - 1) = (x - 1)(3x + 2)")),
    ("7b", "(3x^2 - 12x) - (2x - 8)", "(x - 4)(3x - 2)", 1,
     dict(etex=r"\left(3x^{2} - 12x\right) - (2x - 8)", rtex=r"3x(x - 4) - 2(x - 4) = (x - 4)(3x - 2)")),
    ("7c", "(8u^2 + 4u) - (2u + 1)", "(2u + 1)(4u - 1)", 1,
     dict(etex=r"\left(8u^{2} + 4u\right) - (2u + 1)", rtex=r"4u(2u + 1) - (2u + 1) = (2u + 1)(4u - 1)")),
    ("7d", "(2x^2 + 4x) + (3x + 6)", "(x + 2)(2x + 3)", 1,
     dict(etex=r"\left(2x^{2} + 4x\right) + (3x + 6)", rtex=r"2x(x + 2) + 3(x + 2) = (x + 2)(2x + 3)")),
    ("7e", "(2y^2 - 10y) - (3y - 15)", "(y - 5)(2y - 3)", 1,
     dict(etex=r"\left(2y^{2} - 10y\right) - (3y - 15)", rtex=r"2y(y - 5) - 3(y - 5) = (y - 5)(2y - 3)")),
    ("7f", "(6x^2 + 10x) - (3x + 5)", "(3x + 5)(2x - 1)", 1,
     dict(etex=r"\left(6x^{2} + 10x\right) - (3x + 5)", rtex=r"2x(3x + 5) - (3x + 5) = (3x + 5)(2x - 1)")),
])

# 8. Completar la agrupación: (literal, polinomio, primer grupo, signo, segundo grupo)
AGRUPAR = [
    ("8a", "3x^2 - 3x + 2x - 2", "3x^2 - 3x", "+", "2x - 2"),
    ("8b", "3x^2 - 12x - 2x + 8", "3x^2 - 12x", "-", "2x - 8"),
    ("8c", "8u^2 + 4u - 2u - 1", "8u^2 + 4u", "-", "2u + 1"),
    ("8d", "2x^2 + 4x + 3x + 6", "2x^2 + 4x", "+", "3x + 6"),
    ("8e", "2y^2 - 10y - 3y + 15", "2y^2 - 10y", "-", "3y - 15"),
    ("8f", "6x^2 + 10x - 3x - 5", "6x^2 + 10x", "-", "3x + 5"),
]
for lit, poli, g1, signo, g2 in AGRUPAR:
    @ejercicio(id=_id(), tipo="calculo", dificultad=1, fuente=f"{F1} {lit}",
               enunciado=f"Escribe en lugar de $?$ una expresión que haga verdadera la igualdad: "
                         f"${tex(poli)} = \\left({tex(g1)}\\right) {signo} (\\ ?\\ )$.",
               respuesta=f"${tex(g2)}$.", **COMUN)
    def _(poli=poli, g1=g1, signo=signo, g2=g2):
        s = 1 if signo == "+" else -1
        assert sp.expand(E(poli) - (E(g1) + s * E(g2))) == 0

serie("Factoriza agrupando términos: …", F1, [
    ("9a", "3a + a b + 3c + b c", "(3 + b)(a + c)", 1),
    ("9b", "x^2 - 2x + x y - 2y", "(x - 2)(x + y)", 1),
    ("9c", "h^2 - h k + h r - k r", "(h - k)(h + r)", 1),
    ("9d", "p^3 - 2p^2 + 4p - 8", "(p - 2)(p^2 + 4)", 2,
     dict(notas="En la copia markdown y en el texto alternativo solo aparece «p³»; la imagen "
                "dice p³ − 2p² + 4p − 8.")),
    ("9e", "p^2 - 2p q + p r - 2q r", "(p - 2q)(p + r)", 1),
    ("9f", "3h k - 2k - 12h + 8", "(3h - 2)(k - 4)", 2),
    ("9g", "4z^3 - 6z^2 - 6z + 9", "(2z - 3)(2z^2 - 3)", 2),
    ("9h", "(h^2k + 4k^2) + (h^2k + 4k)", "2k*(h^2 + 2k + 2)", 2,
     dict(etex=r"\left(h^{2}k + 4k^{2}\right) + \left(h^{2}k + 4k\right)",
          rtex=r"2h^{2}k + 4k^{2} + 4k = 2k\left(h^{2} + 2k + 2\right)",
          notas="Así está impreso: los dos grupos no dejan un binomio común; reduciendo "
                "términos semejantes queda un factor común monomio. Puede ser una errata.")),
    ("9i", "x^3 - 3x^2 - x + 3", "(x - 3)(x - 1)(x + 1)", 2,
     dict(rtex=r"x^{2}(x - 3) - (x - 3) = (x - 3)\left(x^{2} - 1\right) = (x - 3)(x - 1)(x + 1)")),
    ("9j", "r s + 5r + s t + 5t", "(s + 5)(r + t)", 1),
    ("9k", "u^2 - 2u + u v - 2v", "(u - 2)(u + v)", 1),
    ("9l", "x^2 - 2x y + 4x z - 8y z", "(x - 2y)(x + 4z)", 1),
    ("9m", "3a^3 + a^2 + 6a + 2", "(3a + 1)(a^2 + 2)", 2),
    ("9n", "u^2 - 3u v - 6u w + 18v w", "(u - 3v)(u - 6w)", 2),
    ("9p", "3u^3 - u^2 - 9u + 3", "(3u - 1)(u^2 - 3)", 2),
    ("9q", "(a^2b^2 + 2a^2) - (2a b^2 + 4a)", "a*(a - 2)(b^2 + 2)", 2,
     dict(etex=r"\left(a^{2}b^{2} + 2a^{2}\right) - \left(2ab^{2} + 4a\right)",
          rtex=r"a^{2}\left(b^{2} + 2\right) - 2a\left(b^{2} + 2\right) = a(a - 2)\left(b^{2} + 2\right)")),
    ("9r", "n^3 + 2n^2 - 4n - 8", "(n + 2)^2*(n - 2)", 3,
     dict(rtex=r"n^{2}(n + 2) - 4(n + 2) = (n + 2)\left(n^{2} - 4\right) = (n + 2)^{2}(n - 2)")),
    ("9s", "x^3 + x^2 + x + 1", "(x + 1)(x^2 + 1)", 1),
    ("9t", "r^2s^2 + s^2t - r^2t - t^2", "(r^2 + t)(s^2 - t)", 2),
    ("9u", "a^2 - 2a - 2b + a b", "(a - 2)(a + b)", 1),
    ("9w", "-a c + b n^2 + a m^2 - b c + b m^2 + a n^2", "(a + b)(m^2 + n^2 - c)", 3),
    ("9x", "0.2x z - 2x + 3y - 0.3y z", "0.1(z - 10)(2x - 3y)", 2,
     dict(rtex=r"0{,}2x(z - 10) - 0{,}3y(z - 10) = (z - 10)(0{,}2x - 0{,}3y)")),
    ("9y", "(15/4)x^2 - (21/4)x z - (10/3)x y + (14/3)y z + 5x - 7z",
     "(5x - 7z)((3/4)x - (2/3)y + 1)", 3),
])

serie("Factoriza: …", F1, [
    ("10a", "2m^2 - 8m + 5m - 20", "(m - 4)(2m + 5)", 1),
    ("10b", "4x^2 - 10x + 2x - 5", "(2x - 5)(2x + 1)", 1,
     dict(notas="En el módulo el último término es −4: 4x² − 10x + 2x − 4 = 4(x² − 2x − 1) no se "
                "factoriza por agrupación. Se corrigió a −5 (2x(2x − 5) + (2x − 5)).")),
    ("10c", "6x^2 - 9x - 4x + 6", "(2x - 3)(3x - 2)", 1),
    ("10d", "12x^2 + 8x - 9x - 6", "(3x + 2)(4x - 3)", 1),
    ("10e", "3u^2 - 12u - u + 4", "(u - 4)(3u - 1)", 1),
    ("10f", "6m^2 + 4m - 3m - 2", "(3m + 2)(2m - 1)", 1),
    ("10g", "6u^2 + 3u v - 4u v - 2v^2", "(2u + v)(3u - 2v)", 2,
     dict(notas="En el módulo el último término es «2y²» (mezcla y con u, v); se corrigió a 2v².")),
    ("10h", "2x^2 - 4x y - x y + 2y^2", "(x - 2y)(2x - y)", 2),
    ("10i", "6x^2 + 3x y - 10x y - 5y^2", "(2x + y)(3x - 5y)", 2),
    ("10j", "4u^2 - 16u v - 3u v + 12v^2", "(u - 4v)(4u - 3v)", 2,
     dict(notas="En el módulo aparece «4u² − 16uv − 3uv − 12v», que no se factoriza; se "
                "corrigió a «− 3uv + 12v²».")),
])

serie_numerica(r"Calcula sacando factor común, como en $12^{2} - 8 \cdot 12 = (12 - 8) \cdot 12 "
               r"= 48$: …", F1, [
                   ("11a", "85*5 + 85*7", "85*(5 + 7)", 1020),
                   ("11b", "15^2 - 7*15 + 2*15", "15*(15 - 7 + 2)", 150),
                   ("11c", "42*11 + 73*11", "11*(42 + 73)", 1265),
                   ("11d", "5*18 - 4*18 + 7*18", "18*(5 - 4 + 7)", 144),
                   ("11e", "77^2 + 77*24", "77*(77 + 24)", 7777),
               ])

serie("Factoriza: …", F1, [
    ("12a", "2x A + 3A", "A*(2x + 3)", 1),
    ("12b", "x M - 4M", "M*(x - 4)", 1),
    ("12c", "10x^2 + 15x", "5x*(2x + 3)", 1),
    ("12d", "2x^3V - 6x^2V^2", "2x^2V*(x - 3V)", 1,
     dict(notas="La imagen usa V mayúscula en los dos términos (el texto alternativo mezcla V y "
                "v); se mantuvo V.")),
    ("12e", "6x^2v^2 - 6x v^3", "6x v^2*(x - v)", 1),
    ("12f", "3x*(x + 2) + 5(x + 2)", "(x + 2)(3x + 5)", 1),
    ("12g", "4y*(y + 3) + 7(y + 3)", "(y + 3)(4y + 7)", 1),
    ("12h", "14u^2 - 6u", "2u*(7u - 3)", 1),
    ("12i", "20m^2 + 12m", "4m*(5m + 3)", 1),
    ("12j", "3m*(m - 4) - 2(m - 4)", "(m - 4)(3m - 2)", 1),
    ("12k", "x*(x + y) - y*(x + y)", "(x + y)(x - y)", 1),
    ("12l", "m*(m - n) + n*(m - n)", "(m - n)(m + n)", 1),
    ("12m", "6x^4 - 9x^3 + 3x^2", "3x^2*(2x - 1)(x - 1)", 2,
     dict(rtex=r"3x^{2}\left(2x^{2} - 3x + 1\right) = 3x^{2}(2x - 1)(x - 1)")),
    ("12n", "6m^4 - 8m^3 - 2m^2", "2m^2*(3m^2 - 4m - 1)", 1),
    ("12o", "8x^3v - 6x^2v^2 + 4x v^3", "2x v*(4x^2 - 3x v + 2v^2)", 1),
    ("12p", "10u^3v + 20u^2v^2 - 15u v^3", "5u v*(2u^2 + 4u v - 3v^2)", 1),
    ("12q", "8x^4 - 12x^3y + 4x^2y^2", "4x^2*(2x - y)(x - y)", 2,
     dict(rtex=r"4x^{2}\left(2x^{2} - 3xy + y^{2}\right) = 4x^{2}(2x - y)(x - y)")),
    ("12r", "9m^4 - 6m^3n - 6m^2n^2", "3m^2*(3m^2 - 2m n - 2n^2)", 1),
    ("12s", "3x*(2x + 3) - 5(2x + 3)", "(2x + 3)(3x - 5)", 1),
    ("12t", "2u*(3u - 8) - 3(3u - 8)", "(3u - 8)(2u - 3)", 1),
    ("12u", "x*(x + 1) - (x + 1)", "(x + 1)(x - 1)", 1),
    ("12v", "3u*(u - 1) - (u - 1)", "(u - 1)(3u - 1)", 1),
    ("12w", "4x*(2x - 3) - (2x - 3)", "(2x - 3)(4x - 1)", 1),
    ("12x", "3y*(4y - 5) - (4y - 5)", "(4y - 5)(3y - 1)", 1),
])

r_, a_ = sp.symbols("r a", positive=True)
ECUACIONES = dict(COMUN, dba=["matematicas-8-8", "matematicas-8-3"])


@ejercicio(
    id=_id(), tipo="contexto", dificultad=2, fuente=f"{F1} 13a",
    enunciado=r"El perímetro de un círculo, medido en centímetros, y su área, medida en "
              r"centímetros cuadrados, tienen el mismo valor numérico. Plantea una ecuación y "
              r"resuélvela factorizando: ¿cuánto mide el radio?",
    respuesta=r"$2\pi r - \pi r^{2} = 0 \Rightarrow \pi r(2 - r) = 0$. Como $r \neq 0$, "
              r"$r = 2$ cm.",
    notas="En el módulo: «la diferencia entre la circunferencia … y su área … es cero»; una "
          "longitud y un área no se pueden restar (unidades distintas), así que se pide que los "
          "valores numéricos sean iguales.", **ECUACIONES)
def _():
    assert sp.solve(2 * sp.pi * r_ - sp.pi * r_**2, r_) == [2]
    assert sp.expand(sp.pi * r_ * (2 - r_) - (2 * sp.pi * r_ - sp.pi * r_**2)) == 0


@ejercicio(
    id=_id(), tipo="contexto", dificultad=2, fuente=f"{F1} 13b",
    enunciado=r"El volumen de un cubo de arista $a$, medido en centímetros cúbicos, y el área "
              r"total de sus seis caras, medida en centímetros cuadrados, tienen el mismo valor "
              r"numérico. Plantea una ecuación y resuélvela factorizando: ¿cuánto mide la arista?",
    respuesta=r"$a^{3} - 6a^{2} = 0 \Rightarrow a^{2}(a - 6) = 0$. Como $a \neq 0$, $a = 6$ cm.",
    notas="En el módulo: «la diferencia entre el volumen … y su área … es cero»; se pide la "
          "igualdad de valores numéricos (unidades distintas) y se aclara que es el área total "
          "(6a²).", **ECUACIONES)
def _():
    assert sp.solve(a_**3 - 6 * a_**2, a_) == [6]


ejercicio_manual(
    id=_id(), tipo="argumentacion", dificultad=3,
    fuente=f"{A}, Factorización de expresiones que contienen factores comunes — Curiosidades "
           f"matemáticas",
    enunciado=r"Tres números enteros consecutivos cualesquiera, escritos uno a continuación del "
              r"otro, forman siempre un número divisible por tres (por ejemplo, $8$, $9$ y $10$ "
              r"forman $8910$). Ensaya con otros tres consecutivos y explica por qué ocurre.",
    respuesta=r"Ejemplos: $456$, $111213$, $495051$ son divisibles por $3$. Un número es "
              r"divisible por $3$ si la suma de sus cifras lo es. Al escribir los tres números "
              r"seguidos, la suma de las cifras es la suma de las cifras de $n$, de $n + 1$ y de "
              r"$n + 2$; cada número deja el mismo residuo al dividir por $3$ que la suma de sus "
              r"cifras, así que esa suma deja el mismo residuo que $n + (n + 1) + (n + 2) = "
              r"3n + 3 = 3(n + 1)$, que es múltiplo de $3$.",
    tema="factorización", grados=[8], dba=["matematicas-8-9"])

# ================= Trinomios =================
a, b = sp.symbols("a b", real=True)


@ejercicio(
    id=_id(), tipo="argumentacion", dificultad=2, fuente=F2I,
    enunciado=r"Explica si $(a + b)^{2} = a^{2} + b^{2}$. ¿Qué condiciones deben cumplir $a$ y "
              r"$b$ para que se cumpla esa igualdad?",
    respuesta=r"En general no: $(a + b)^{2} = a^{2} + 2ab + b^{2}$. La igualdad solo se cumple "
              r"si $2ab = 0$, es decir, si $a = 0$ o $b = 0$. Por ejemplo, $(1 + 2)^{2} = 9$ y "
              r"$1^{2} + 2^{2} = 5$.", **COMUN)
def _():
    diferencia = sp.expand((a + b) ** 2 - (a**2 + b**2))
    assert diferencia == 2 * a * b
    assert (1 + 2) ** 2 != 1**2 + 2**2


def _es_cuadrado(f):
    c, lista = sp.factor_list(f)
    return c > 0 and sp.sqrt(c).is_rational and all(k % 2 == 0 for _, k in lista)


# 1. ¿Trinomio cuadrado perfecto? (literal, trinomio, es TCP, factorización o None, respuesta)
TCP = [
    ("1a", "x^2 + 6x - 9", False, None, r"No: el término $-9$ es negativo."),
    ("1b", "9x^2 - 24x y + 16y^2", True, "(3x - 4y)^2", None),
    ("1c", "64x^2 + 112x y - 49y^2", False, None, r"No: el término $-49y^{2}$ es negativo."),
    ("1d", "-4x^2 - 20x y + 25y^2", False, None, r"No: el término $-4x^{2}$ es negativo."),
    ("1e", "225 - 30r + r^2", True, "(15 - r)^2", None),
    ("1f", "2x^2y - 36x y + 162y", False, "2y*(x - 9)^2",
     r"No tal como está ($2x^{2}y$ no es un cuadrado), pero al sacar el factor común $2y$ queda "
     r"uno: $2y\left(x^{2} - 18x + 81\right) = 2y(x - 9)^{2}$."),
    ("1g", "5c^2 - 10c + 5", False, "5(c - 1)^2",
     r"No tal como está ($5$ no es un cuadrado perfecto), pero $5\left(c^{2} - 2c + 1\right) = "
     r"5(c - 1)^{2}$."),
    ("1h", "4x^2 + 24x - 36", False, "4(x^2 + 6x - 9)",
     r"No: el término $-36$ es negativo; solo se puede sacar el factor común: "
     r"$4\left(x^{2} + 6x - 9\right)$."),
    ("1i", "16a^2 + 40a + 25", True, "(4a + 5)^2", None),
    ("1j", "25p^2 + 35p + 49", False, None,
     r"No: el doble producto de $5p$ y $7$ es $70p$, no $35p$."),
    ("1k", "v^2 - 28v + 196", True, "(v - 14)^2", None),
    ("1l", "x^2 - 6x - 9", False, None, r"No: el término $-9$ es negativo."),
]
for lit, trin, es, fact, texto in TCP:
    resp = texto or f"Sí: ${tex(trin)} = {tex(fact)}$."

    @ejercicio(id=_id(), tipo="calculo", dificultad=1 if es else 2, fuente=f"{F2} {lit}",
               enunciado=f"¿Es ${tex(trin)}$ un trinomio cuadrado perfecto? Si lo es, factorízalo.",
               respuesta=resp, **COMUN)
    def _(trin=trin, es=es, fact=fact):
        assert _es_cuadrado(E(trin)) == es
        if fact:
            comprobar_fila(trin, fact, "total")

serie("Factoriza, si es posible: …", F2, [
    ("2a", "x^2 - 6x y + 9y^2", "(x - 3y)^2", 1),
    ("2b", "4a^2 + 4a + 1", "(2a + 1)^2", 1),
    ("2c", "4m^4 + 20m^2 + 25", "(2m^2 + 5)^2", 1),
    ("2d", "9m^6 + 16n^10 + 24m^3n^5", "(3m^3 + 4n^5)^2", 2),
    ("2e", "x^4y^6 + z^8 - 2x^2y^3z^4", "(x^2y^3 - z^4)^2", 2,
     dict(notas="En la copia markdown y en el texto alternativo solo aparece «y⁶»; la imagen "
                "dice x⁴y⁶ + z⁸ − 2x²y³z⁴.")),
    ("2f", "16x^6y^8 + z^14 - 8x^3y^4z^7", "(4x^3y^4 - z^7)^2", 2),
    ("2g", "81a^2 - 36a b + 4b^2", "(9a - 2b)^2", 1),
    ("2h", "361a^6 - 646a^5b + 289a^4b^2", "a^4*(19a - 17b)^2", 3),
    ("2i", "1 + 6a + 9a^2", "(1 + 3a)^2", 1),
    ("2j", "x^16 - 2x^8y^6 + y^12", "(x^4 - y^3)^2*(x^4 + y^3)^2", 3,
     dict(rtex=r"\left(x^{8} - y^{6}\right)^{2} = \left(x^{4} - y^{3}\right)^{2}"
               r"\left(x^{4} + y^{3}\right)^{2}")),
    ("2k", "25m^2 + 49n^2 - 70m n", "(5m - 7n)^2", 1),
    ("2l", "441x^10y^6 + 126x^11y^3 + 9x^12", "9x^10*(7y^3 + x)^2", 3),
    ("2m", "225p^6 - 420p^3q^4 + 196q^8", "(15p^3 - 14q^4)^2", 2),
    ("2n", "25a^2c^2 + 4d^2 - 20a c d", "(5a c - 2d)^2", 2),
    ("2o", "p^12 + 16p^6q^4 + 68q^8", None, 2,
     dict(modo="no", notas="No es trinomio cuadrado perfecto: haría falta 64q⁸ en lugar de "
                           "68q⁸ (posible errata del módulo; el literal dice «si es posible»).")),
    ("2p", "289a^2 + 68a b c + 4b^2c^2", "(17a + 2b c)^2", 2),
    ("2q", "(169/196)w^2 - (65/7)w + 25", "((13/14)w - 5)^2", 3),
    ("2r", "a^2b^2 - 10a b + 25", "(a b - 5)^2", 1),
    ("2s", "-12h^4k^7 + 9k^14 + 4h^8", "(2h^4 - 3k^7)^2", 2),
    ("2t", "121a^10 - 198a^5b^3c + 81b^6c^2", "(11a^5 - 9b^3c)^2", 2),
    ("2v", "a^6b^2 - 6a^3b c + 9c^2", "(a^3b - 3c)^2", 2,
     dict(notas="El texto alternativo dice «a²b²»; la imagen dice a⁶b².")),
    ("2w", "(9/25)p^6 + (2/15)p^3q^4 + (1/81)q^8", "((3/5)p^3 + (1/9)q^4)^2", 3),
    ("2x", "(1/25)m^16 + (25/64)n^2 - (1/4)m^8n", "((1/5)m^8 - (5/8)n)^2", 3),
])

serie("Factoriza: …", F2, [
    ("3a", "x^2 + 8x + 7", "(x + 7)(x + 1)", 1), ("3b", "y^2 + 7y + 12", "(y + 3)(y + 4)", 1),
    ("3c", "r^2 + 9r + 20", "(r + 4)(r + 5)", 1), ("3d", "y^2 + 25y + 24", "(y + 24)(y + 1)", 1),
    ("3e", "p^2 - 5p + 6", "(p - 2)(p - 3)", 1), ("3f", "u^2 + 11u + 18", "(u + 2)(u + 9)", 1),
    ("3g", "x^2 - 14x + 24", "(x - 2)(x - 12)", 1), ("3h", "z^2 - 6z + 5", "(z - 1)(z - 5)", 1),
    ("3i", "c^2 - 15c + 14", "(c - 1)(c - 14)", 1), ("3j", "s^2 - 12s + 20", "(s - 2)(s - 10)", 1),
    ("3k", "x^2 + 11x + 28", "(x + 4)(x + 7)", 1), ("3l", "x^2 + 5x + 4", "(x + 1)(x + 4)", 1),
    ("3m", "c^2 - 10c + 16", "(c - 2)(c - 8)", 1), ("3n", "q^2 + 16q + 15", "(q + 1)(q + 15)", 1),
    ("3o", "m^2 + 5m + 6", "(m + 2)(m + 3)", 1), ("3p", "f^2 - 12f + 20", "(f - 2)(f - 10)", 1),
])

serie("Factoriza: …", F2, [
    ("4a", "p^2 + 19p q + 34q^2", "(p + 2q)(p + 17q)", 1),
    ("4b", "x^2 - 17x y + 72y^2", "(x - 8y)(x - 9y)", 1),
    ("4c", "x^2 - 14x y + 45y^2", "(x - 5y)(x - 9y)", 1),
    ("4d", "p^2 + 15p q + 50q^2", "(p + 5q)(p + 10q)", 1),
    ("4e", "m^2 + 20m n + 51n^2", "(m + 3n)(m + 17n)", 1),
    ("4f", "h^2 - 14h k + 49k^2", "(h - 7k)^2", 1),
    ("4g", "a^2 + 10a b + 24b^2", "(a + 4b)(a + 6b)", 1),
    ("4h", "r^2 - 15r s + 54s^2", "(r - 6s)(r - 9s)", 1),
    ("4i", "a^2 + 5a b + 6b^2", "(a + 2b)(a + 3b)", 1),
    ("4j", "u^2 + 41u v + 40v^2", "(u + v)(u + 40v)", 1),
    ("4k", "c^2 - 16c d + 48d^2", "(c - 4d)(c - 12d)", 1),
    ("4l", "r^2 + 8r + 16", "(r + 4)^2", 1),
])

SIN_FACTOR = ("Tal como está impreso no se factoriza con coeficientes enteros (discriminante "
              "{}); puede ser una errata del módulo: se respondió que no se puede.")
serie("Factoriza: …", F2, [
    ("5a", "5x^2 - 13x + 6", "(5x - 3)(x - 2)", 2), ("5b", "2x^2 - x - 10", "(2x - 5)(x + 2)", 2),
    ("5c", "5x^2 - 11x + 2", "(5x - 1)(x - 2)", 2), ("5d", "14x^2 + 13x + 3", "(7x + 3)(2x + 1)", 2),
    ("5e", "4x^2 + 8x + 3", "(2x + 1)(2x + 3)", 2), ("5f", "6x^2 + 5x + 1", "(3x + 1)(2x + 1)", 2),
    ("5g", "8x^2 - 25x + 3", "(8x - 1)(x - 3)", 2),
    ("5h", "10x^2 - 10x - 9", None, 2, dict(modo="no", notas=SIN_FACTOR.format(460))),
    ("5i", "2x^2 + x - 6", "(2x - 3)(x + 2)", 2), ("5j", "4x^2 - 4x - 3", "(2x - 3)(2x + 1)", 2),
    ("5k", "3x^2 + 4x - 4", "(3x - 2)(x + 2)", 2), ("5l", "9x^2 + 6x - 8", "(3x - 2)(3x + 4)", 2),
    ("5m", "3x^2 + 7x + 2", "(3x + 1)(x + 2)", 2), ("5n", "3c^2 - 8c + 5", "(3c - 5)(c - 1)", 2),
    ("5o", "5y^2 + 4y - 1", "(5y - 1)(y + 1)", 2),
    ("5p", "5u^2 - 6u - 2", None, 2, dict(modo="no", notas=SIN_FACTOR.format(76))),
    ("5q", "7x^2 + 8x + 1", "(7x + 1)(x + 1)", 2), ("5r", "5x^2 - 17x + 6", "(5x - 2)(x - 3)", 2),
    ("5s", "3p^2 + 7p - 6", "(3p - 2)(p + 3)", 2), ("5t", "4y^2 - y - 3", "(4y + 3)(y - 1)", 2),
    ("5u", "5 + 7x - 6x^2", "(5 - 3x)(1 + 2x)", 3),
    ("5v", "1 - 5b - 8b^2", None, 2, dict(modo="no", notas=SIN_FACTOR.format(57))),
    ("5w", "3m^2 + 11m n + 6n^2", "(3m + 2n)(m + 3n)", 2),
    ("5x", "2x^2 + x y - 3y^2", "(2x + 3y)(x - y)", 2),
])

serie("Factoriza, si es posible: …", F2, [
    ("6a", "y^2 - 10y + 25", "(y - 5)^2", 1),
    ("6b", "x^2 + 24x + 128", "(x + 8)(x + 16)", 1),
    ("6c", "6x^2 - x + 12", None, 2, dict(modo="no")),
    ("6d", "x^2 - 3x - 28", "(x - 7)(x + 4)", 1),
    ("6e", "x^2 - 30x + 225", "(x - 15)^2", 1),
    ("6f", "4x^2 + 3x - 10", "(4x - 5)(x + 2)", 2),
    ("6g", "4x^2 - 12x + 9", "(2x - 3)^2", 1),
    ("6h", "x^2 - 10x + 21", "(x - 3)(x - 7)", 1),
    ("6i", "15x^2 + 38x - 21", "(15x - 7)(x + 3)", 3),
    ("6j", "9x^2 + 30x + 25", "(3x + 5)^2", 1),
    ("6k", "14x^2 - 25x - 25", "(2x - 5)(7x + 5)", 3),
    ("6m", "x^2 + 260x + 2500", "(x + 10)(x + 250)", 2),
    ("6n", "6x^2 - 13x y - 15y^2", "(x - 3y)(6x + 5y)", 3),
    ("6o", "-x^2 + 3x + 28", "(7 - x)(x + 4)", 2),
])

serie(r"El área de un rectángulo de lados $x + \ ?$ y $x + \ ?$ es el trinomio dado. "
      r"Completa: …", F2B, [
          ("b", "x^2 + 6x + 8", "(x + 2)(x + 4)", 1,
           dict(etex=r"x^{2} + 6x + 8 = (x + \ ?\ )(x + \ ?\ )")),
          ("c", "x^2 + 7x + 12", "(x + 3)(x + 4)", 1,
           dict(etex=r"x^{2} + 7x + 12 = (x + \ ?\ )(x + \ ?\ )")),
      ])

X = sp.symbols("x")


@ejercicio(
    id=_id(), tipo="seleccion", dificultad=1, fuente=f"{F2B}, pregunta 1",
    enunciado=r"Un rectángulo tiene área $x^{2} + 5x + 4$ y lados $x + \ ?$ y $x + \ ?$. Los "
              r"valores correctos de los signos de interrogación son:" + opciones(
                  r"$-4$ y $-1$", r"$4$ y $-1$", r"$-4$ y $1$", r"$4$ y $1$"),
    respuesta=r"D: $(x + 4)(x + 1) = x^{2} + 5x + 4$.", **COMUN)
def _():
    pares = [(-4, -1), (4, -1), (-4, 1), (4, 1)]
    buenos = [i for i, (p, q) in enumerate(pares)
              if sp.expand((X + p) * (X + q)) == X**2 + 5 * X + 4]
    assert buenos == [3]


@ejercicio(
    id=_id(), tipo="seleccion", dificultad=1, fuente=f"{F2B}, pregunta 2",
    enunciado=r"El perímetro de un rectángulo de área $x^{2} + 6x + 8$ cuyos lados son de la "
              r"forma $x + \ ?$ es:" + opciones(r"$2(x + 2) + 2(x + 4)$", r"$(x + 2) + (x + 4)$",
                                                r"$2(x - 2) + 2(x - 4)$",
                                                r"$2(x - 2) + 2(x - 4)$"),
    respuesta=r"A: los lados miden $x + 2$ y $x + 4$, y el perímetro es $2(x + 2) + 2(x + 4) = "
              r"4x + 12$.",
    notas="En el módulo las opciones C y D son iguales; se dejaron así porque no afectan la "
          "respuesta, pero conviene cambiar una.", **COMUN)
def _():
    assert sp.factor(X**2 + 6 * X + 8) == (X + 2) * (X + 4)
    per = 2 * (X + 2) + 2 * (X + 4)
    otras = [(X + 2) + (X + 4), 2 * (X - 2) + 2 * (X - 4)]
    assert all(sp.expand(o - per) != 0 for o in otras)


@ejercicio(
    id=_id(), tipo="seleccion", dificultad=1, fuente=f"{F2B}, pregunta 3",
    enunciado=r"Un rectángulo de lados $x + 3$ y $x + 4$ se divide en cuatro rectángulos (de "
              r"áreas $x^{2}$, $3x$, $4x$ y $12$). Al sumar sus áreas se obtiene:" + opciones(
                  r"$x^{2} - 7x + 12$", r"$x^{2} - 7x - 12$", r"$x^{2} + 7x - 12$",
                  r"$x^{2} + 7x + 12$"),
    respuesta=r"D: $x^{2} + 3x + 4x + 12 = x^{2} + 7x + 12$.",
    notas="Se escribieron en palabras los lados del rectángulo 3 de la figura.", **COMUN)
def _():
    total = sp.expand((X + 3) * (X + 4))
    ops = [X**2 - 7 * X + 12, X**2 - 7 * X - 12, X**2 + 7 * X - 12, X**2 + 7 * X + 12]
    assert [i for i, o in enumerate(ops) if o == total] == [3]


# ================= Binomios =================
serie("Desarrolla el producto: …", F3I, [
    ("1", "(3x - 2b)(3x + 2b)", "9x^2 - 4b^2", 1),
    ("2", "(x - y)(x^2 - x y + y^2)", "x^3 - 2x^2y + 2x y^2 - y^3", 2,
     dict(notas="Así está en el módulo; no es una suma ni diferencia de cubos (para eso el primer "
                "factor tendría que ser x + y).")),
    ("3", "(2x + 7y)(4x^2 - 14x y + 49y^2)", "8x^3 + 343y^3", 2),
], modo="expandido")

serie("Expresa el producto como un binomio: …", F3, [
    ("1a", "(n + 2)(n - 2)", "n^2 - 4", 1), ("1b", "(r - 5)(r + 5)", "r^2 - 25", 1),
    ("1c", "(2x + 5)(2x - 5)", "4x^2 - 25", 1), ("1d", "(4y + 1)(4y - 1)", "16y^2 - 1", 1),
    ("1e", "(3s - 2)(3s + 2)", "9s^2 - 4", 1), ("1f", "(a - 2b)(a + 2b)", "a^2 - 4b^2", 1),
], modo="expandido")

serie("Factoriza la diferencia de cuadrados: …", F3, [
    ("2a", "a^2 - 1", "(a + 1)(a - 1)", 1),
    ("2b", "36x^2 - 25y^2", "(6x + 5y)(6x - 5y)", 1),
    ("2c", "169m^2 - 196n^2", "(13m + 14n)(13m - 14n)", 1),
    ("2d", "121h^2 - 144k^2", "(11h + 12k)(11h - 12k)", 1,
     dict(notas="El texto alternativo dice «k²⁴»; la imagen dice k².")),
    ("2e", "1 - 100x^2", "(1 + 10x)(1 - 10x)", 1),
    ("2f", "a^6 - 9b^2", "(a^3 + 3b)(a^3 - 3b)", 1),
    ("2g", "m^8 - n^2", "(m^4 + n)(m^4 - n)", 1),
    ("2h", "a^4b^6 - c^10", "(a^2b^3 + c^5)(a^2b^3 - c^5)", 2),
    ("2i", "d^14 - x^2y^2", "(d^7 + x y)(d^7 - x y)", 2),
    ("2j", "(9/25)a^2 - (49/36)b^2", "((3/5)a + (7/6)b)((3/5)a - (7/6)b)", 2),
    ("2k", "0.01x^2 - 0.0009y^2", "(0.1x + 0.03y)(0.1x - 0.03y)", 2),
    ("2l", "(1/256)x^2 - (1/25)y^12", "((1/16)x + (1/5)y^6)((1/16)x - (1/5)y^6)", 2),
    ("2m", "x^2 - 144", "(x + 12)(x - 12)", 1),
    ("2n", "9a^2 - 441b^2", "9(a + 7b)(a - 7b)", 2),
    ("2o", "36a^2b^8 - 16x^2", "4(3a b^4 + 2x)(3a b^4 - 2x)", 2),
    ("2p", "9m^4n^6 - 100", "(3m^2n^3 + 10)(3m^2n^3 - 10)", 1),
    ("2q", "4x^2 - 64y^8", "4(x + 4y^4)(x - 4y^4)", 2),
    ("2r", "121x^4y^10 - 25m^8", "(11x^2y^5 + 5m^4)(11x^2y^5 - 5m^4)", 2),
    ("2s", "(36/25)a^2 - (25/9)b^8", "((6/5)a + (5/3)b^4)((6/5)a - (5/3)b^4)", 2),
])

serie(r"Factoriza como diferencia de cuadrados, como en el ejemplo "
      r"$(m - x)^{2} - (3m - 2x)^{2} = [(m - x) + (3m - 2x)][(m - x) - (3m - 2x)] = "
      r"(4m - 3x)(-2m + x)$: …", F3, [
          ("3a", "(a - b)^4 - c^2", "((a - b)^2 + c)((a - b)^2 - c)", 2,
           dict(rtex=r"\left[(a - b)^{2} + c\right]\left[(a - b)^{2} - c\right]")),
          ("3b", "(5m + n)^2 - (3m - 2n)^2", "(8m - n)(2m + 3n)", 2),
          ("3c", "(t - 2v)^2 - (5t - x)^2", "(6t - 2v - x)(x - 4t - 2v)", 2,
           dict(notas="El texto alternativo dice «(t − 2x)»; la imagen dice (t − 2v).")),
          ("3d", "n^8 - (3x - n^2)^2", "(n^4 + 3x - n^2)(n^4 - 3x + n^2)", 2),
          ("3e", "1 - 100(x - y)^2", "(1 + 10x - 10y)(1 - 10x + 10y)", 2),
          ("3f", "(x^2 - y^2)^2 - (x^4 - y^2)^4", "(x^2 - y^2 + (x^4 - y^2)^2)(x^2 - y^2 - (x^4 - y^2)^2)", 3,
           dict(modo="eq",
                rtex=r"\left[x^{2} - y^{2} + \left(x^{4} - y^{2}\right)^{2}\right]"
                     r"\left[x^{2} - y^{2} - \left(x^{4} - y^{2}\right)^{2}\right]",
                notas="Así está impreso (con exponente 4 en el segundo término, que parece "
                      "errata por 2). La respuesta es la diferencia de cuadrados; sus factores "
                      "todavía se pueden descomponer, pero no con los casos de 8°.")),
          ("3g", "(1 - m)^2 - (1 + m)^2", "-4m", 1),
          ("3h", "169m^2 - (m - n)^2", "(14m - n)(12m + n)", 2),
          ("3i", "(s + 3t^2)^2 - (s - 3t)^2", "3t*(t + 1)(2s + 3t^2 - 3t)", 3,
           dict(rtex=r"\left(2s + 3t^{2} - 3t\right)\left(3t^{2} + 3t\right) = "
                     r"3t(t + 1)\left(2s + 3t^{2} - 3t\right)")),
          ("3j", "(1 + x)^2 - x^2", "1 + 2x", 1),
      ])

serie("Factoriza el binomio: …", F3, [
    ("4a", "a^3 - b^3", "(a - b)(a^2 + a b + b^2)", 1),
    ("4b", "a^3 + b^3", "(a + b)(a^2 - a b + b^2)", 1),
    ("4c", "a^3 + 1", "(a + 1)(a^2 - a + 1)", 1),
    ("4d", "a^3 - 1", "(a - 1)(a^2 + a + 1)", 1),
    ("4e", "a^6 - b^6", "(a + b)(a - b)(a^2 - a b + b^2)(a^2 + a b + b^2)", 3,
     dict(rtex=r"\left(a^{3} + b^{3}\right)\left(a^{3} - b^{3}\right) = (a + b)(a - b)"
               r"\left(a^{2} - ab + b^{2}\right)\left(a^{2} + ab + b^{2}\right)")),
    ("4f", "a^15 + b^9", "(a^5 + b^3)(a^10 - a^5b^3 + b^6)", 2),
    ("4g", "m^18 + n^21", "(m^6 + n^7)(m^12 - m^6n^7 + n^14)", 2),
    ("4h", "1 - z^15", "(1 - z^5)(1 + z^5 + z^10)", 2,
     dict(modo="eq", notas="Respuesta como diferencia de cubos; 1 − z⁵ y 1 + z⁵ + z¹⁰ todavía se "
                           "descomponen, pero no con los casos de 8°.")),
    ("4i", "512m^3 - 64p^3", "64(2m - p)(4m^2 + 2m p + p^2)", 2),
    ("4j", "1000h^3 + 27k^3", "(10h + 3k)(100h^2 - 30h k + 9k^2)", 2),
    ("4k", "x^3/8 - 1/27", "(x/2 - 1/3)(x^2/4 + x/6 + 1/9)", 2),
    ("4l", "448a^4 - 7a b^3", "7a*(4a - b)(16a^2 + 4a b + b^2)", 3),
    ("4m", "8a^3/125 - 64b^12/343",
     "((2/5)a - (4/7)b^4)((4/25)a^2 + (8/35)a b^4 + (16/49)b^8)", 3),
    ("4n", "x^4y - x y^4", "x y*(x - y)(x^2 + x y + y^2)", 2),
    ("4o", "m^5 + m^2n^3", "m^2*(m + n)(m^2 - m n + n^2)", 2),
    ("4p", "c^4d^2 - 8c d^5", "c d^2*(c - 2d)(c^2 + 2c d + 4d^2)", 2),
    ("4q", "27p^5q - 8p^2q^4", "p^2q*(3p - 2q)(9p^2 + 6p q + 4q^2)", 2),
    ("4r", "343a^3/2 - 125b^3/2", "(1/2)(7a - 5b)(49a^2 + 35a b + 25b^2)", 3),
    ("4s", "125r s a^3/3 - 512r s b^3/3", "(1/3)r s*(5a - 8b)(25a^2 + 40a b + 64b^2)", 3),
    ("4t", "81m^3 - 648n^3", "81(m - 2n)(m^2 + 2m n + 4n^2)", 2),
])

serie("Factoriza, si es posible: …", F3, [
    ("5a", "v^5 - 25", None, 1,
     dict(modo="no", notas="Así está impreso (v⁵); si fuera v² − 25 (posible errata) sería "
                           "(v + 5)(v − 5).")),
    ("5b", "x^2 - 81", "(x + 9)(x - 9)", 1), ("5c", "9x^2 - 4", "(3x + 2)(3x - 2)", 1),
    ("5d", "4m^2 - 1", "(2m + 1)(2m - 1)", 1),
    ("5e", "x^2 + 49", None, 1, dict(modo="no")), ("5f", "y^2 + 64", None, 1, dict(modo="no")),
    ("5g", "9x^2 - 16y^2", "(3x + 4y)(3x - 4y)", 1), ("5h", "25u^2 - 4v^2", "(5u + 2v)(5u - 2v)", 1),
    ("5i", "x^3 + 1", "(x + 1)(x^2 - x + 1)", 1), ("5j", "y^3 - 1", "(y - 1)(y^2 + y + 1)", 1),
    ("5k", "m^3 - n^3", "(m - n)(m^2 + m n + n^2)", 1),
    ("5l", "p^3 + q^3", "(p + q)(p^2 - p q + q^2)", 1),
    ("5m", "8x^3 + 27", "(2x + 3)(4x^2 - 6x + 9)", 2),
    ("5n", "u^3 - 8v^3", "(u - 2v)(u^2 + 2u v + 4v^2)", 2),
    ("5o", "6u^2v^2 - 3u v^3", "3u v^2*(2u - v)", 1),
    ("5p", "27x^3y - 6x^2y^3", "3x^2y*(9x - 2y^2)", 1),
    ("5r", "3y^2 - 27", "3(y + 3)(y - 3)", 1), ("5s", "2x^3 + 8x", "2x*(x^2 + 4)", 1),
    ("5t", "3x^4 + 27x^2", "3x^2*(x^2 + 9)", 1),
    ("5u", "12x^3 - 3x y^2", "3x*(2x + y)(2x - y)", 2),
    ("5v", "2u^3v - 2u v^3", "2u v*(u + v)(u - v)", 2),
    ("5w", "2x^4 + 2x", "2x*(x + 1)(x^2 - x + 1)", 2),
    ("5x", "x y^3 + x^4", "x*(x + y)(x^2 - x y + y^2)", 2),
    ("5y", "x^2y^2 - 16", "(x y + 4)(x y - 4)", 1), ("5z", "t^8 - 100", "(t^4 + 10)(t^4 - 10)", 1),
])

serie("Factoriza, si es posible: …", F3, [
    ("6a", "6x^2 + 36x + 48", "6(x + 2)(x + 4)", 1),
    ("6b", "4x^3y + 14x^2y^2 + 6x y^3", "2x y*(2x + y)(x + 3y)", 2),
    ("6c", "3x^3y - 15x^2y^2 + 18x y^3", "3x y*(x - 2y)(x - 3y)", 2),
    ("6d", "60x^2y^2 - 200x y^3 - 35y^4", "5y^2*(2x - 7y)(6x + y)", 3),
    ("6e", "60x^4 + 68x^3y - 16x^2y^2", "4x^2*(5x - y)(3x + 4y)", 3),
    ("6f", "4x^2 - 4x - 24", "4(x - 3)(x + 2)", 1),
    ("6g", "3x^3 - 6x + 15", "3(x^3 - 2x + 5)", 1,
     dict(notas="Así está impreso (3x³); si fuera 3x² (posible errata), 3(x² − 2x + 5) tampoco "
                "se factoriza más.")),
    ("6h", "2x^3 - 2x^2 + 8x", "2x*(x^2 - x + 4)", 1),
    ("6i", "x^4 - 3x^2 - 4", "(x + 2)(x - 2)(x^2 + 1)", 2),
    ("6j", "x^4 - 7x^2 - 18", "(x + 3)(x - 3)(x^2 + 2)", 2),
    ("6k", "2x^2 - 2x - 12", "2(x - 3)(x + 2)", 1),
])

serie("Factoriza, si es posible: …", F3, [
    ("7a", "4u^3 + 32v^3", "4(u + 2v)(u^2 - 2u v + 4v^2)", 2),
    ("7b", "54x^3 - 2y^3", "2(3x - y)(9x^2 + 3x y + y^2)", 2),
    ("7c", "x y + 2x + y^2 + 2y", "(y + 2)(x + y)", 1),
    ("7d", "x^2 - 3x - x y + 3y", "(x - 3)(x - y)", 1),
    ("7e", "(x - 3)^2 - 16y^2", "(x - 3 + 4y)(x - 3 - 4y)", 2),
    ("7f", "(x + 2)^2 - 9y^2", "(x + 2 + 3y)(x + 2 - 3y)", 2),
    ("7g", "(a - b)^2 - 4(c - d)^2", "(a - b + 2c - 2d)(a - b - 2c + 2d)", 2),
    ("7h", "(x^2 - x)^2 - 9(y^2 - y)^2", "(x^2 - x + 3y^2 - 3y)(x^2 - x - 3y^2 + 3y)", 3),
    ("7i", "25(4x^2 - 12x y + 9y^2)^2 - 9a^2b^2",
     "(20x^2 - 60x y + 45y^2 + 3a b)(20x^2 - 60x y + 45y^2 - 3a b)", 3,
     dict(rtex=r"\left[5(2x - 3y)^{2} + 3ab\right]\left[5(2x - 3y)^{2} - 3ab\right]")),
    ("7j", "25 - a^2 - 2a b - b^2", "(5 + a + b)(5 - a - b)", 2),
    ("7k", "x^2 - 2x y + y^2 - 9", "(x - y + 3)(x - y - 3)", 2),
    ("7l", "16x^4 - x^2 + 6x y - 9y^2", "(4x^2 + x - 3y)(4x^2 - x + 3y)", 3),
    ("7m", "x^4 - x^2 + 4x - 4", "(x + 2)(x - 1)(x^2 - x + 2)", 3,
     dict(rtex=r"x^{4} - (x - 2)^{2} = \left(x^{2} + x - 2\right)\left(x^{2} - x + 2\right) = "
               r"(x + 2)(x - 1)\left(x^{2} - x + 2\right)")),
    ("7n", "m^8 - n^10", "(m^4 + n^5)(m^4 - n^5)", 1),
])

CUBOS = (r"Una diferencia de cubos se puede ver con volúmenes: a un cubo de arista $x$ se le "
         r"quita un cubo de arista $y$ y lo que queda se parte en tres cajas, lo que da "
         r"$x^{3} - y^{3} = (x - y)x^{2} + (x - y)xy + (x - y)y^{2} = "
         r"(x - y)\left(x^{2} + xy + y^{2}\right)$. ")
NOTA_CUBOS = ("En el módulo la igualdad tiene erratas: «(m − y)y²» y «(x³ + xy + y²)»; se "
              "escribió (x − y)y² y (x² + xy + y²). La figura se describió en palabras.")
SUMANDOS = [(x - y) * x**2, (x - y) * x * y, (x - y) * y**2]


@ejercicio(
    id=_id(), tipo="seleccion", dificultad=2, fuente=f"{F3C} 1",
    enunciado=CUBOS + r"En esa igualdad, cada uno de los sumandos representa:" + opciones(
        "El área de las caras laterales de las cajas.", "La longitud de los lados de las cajas.",
        "El volumen de las cajas.", "El volumen de dos de las cajas y el área de la más pequeña."),
    respuesta=r"C: cada sumando es el producto de tres longitudes (largo, ancho y alto de una "
              r"caja), es decir, un volumen.", notas=NOTA_CUBOS, **COMUN)
def _():
    assert sp.expand(sum(SUMANDOS) - (x**3 - y**3)) == 0
    assert all(sp.Poly(s, x, y).is_homogeneous and sp.Poly(s, x, y).total_degree() == 3
               for s in SUMANDOS)                         # tres longitudes: volumen


@ejercicio(
    id=_id(), tipo="seleccion", dificultad=2, fuente=f"{F3C} 2",
    enunciado=CUBOS + r"En esa deducción se utilizó:" + opciones(
        "Factor común monomio.", "Factor común polinomio.", "Factor común por agrupación.",
        "Diferencia de cuadrados."),
    respuesta=r"B: el binomio $(x - y)$ es común a los tres sumandos y se saca como factor.",
    notas=NOTA_CUBOS, **COMUN)
def _():
    cocientes = [sp.div(s, x - y, x, y) for s in SUMANDOS]
    assert all(r == 0 for _, r in cocientes)
    assert sp.expand(sum(c for c, _ in cocientes) - (x**2 + x * y + y**2)) == 0


# ================= Combinación de casos =================
serie("Factoriza: …", F4I, [
    ("b", "x^4 - 1", "(x^2 + 1)(x + 1)(x - 1)", 1),
    ("c", "m^2 - 5m + 6", "(m - 2)(m - 3)", 1),
])

serie("Factoriza: …", F4, [
    ("1a", "18x - 8x^3", "2x*(3 + 2x)(3 - 2x)", 2),
    ("1b", "4(z - 4)^2 - 16", "4(z - 2)(z - 6)", 2),
    ("1c", "4(x + y)^2 - (2y - z)^2", "(2x + 4y - z)(2x + z)", 3,
     dict(notas="En la imagen el 4 va fuera de la fórmula («4 (x + y)² − (2y − z)²»); se "
                "entendió 4(x + y)² − (2y − z)².")),
    ("1d", "x^2 - 2x y + y^2 - 4", "(x - y + 2)(x - y - 2)", 2),
    ("1e", "m^2 - 9n^2 + 2m + 1", "(m + 1 + 3n)(m + 1 - 3n)", 2),
    ("1f", "a^2 - b^2 - 2a + 1", "(a - 1 + b)(a - 1 - b)", 2),
    ("1g", "4x^2 - 4y^2 + 4x + 1", "(2x + 1 + 2y)(2x + 1 - 2y)", 2),
    ("1h", "m^2 - 9n^2 + 9 - 6m", "(m - 3 + 3n)(m - 3 - 3n)", 2),
    ("1i", "p^2 - q^2 - 2p + 2q", "(p - q)(p + q - 2)", 2),
    ("1j", "a^4 + b^4 - c^4 + 2a^2b^2", "(a^2 + b^2 + c^2)(a^2 + b^2 - c^2)", 3),
    ("1k", "h^2 - 4k^2 + 4h - 8k", "(h - 2k)(h + 2k + 4)", 2),
    ("1l", "(a + 2b)^2 - (2b + c)^2", "(a + 4b + c)(a - c)", 2),
    ("1m", "a^2 + 4a + 4 - b^2", "(a + 2 + b)(a + 2 - b)", 2),
    ("1n", "u^2 - v^2", "(u + v)(u - v)", 1),
    ("1o", "h^2 - 4k^2 - 4h + 4", "(h - 2 + 2k)(h - 2 - 2k)", 2),
    ("1p", "p^2 - q^2 + r^2 - 2p r", "(p - r + q)(p - r - q)", 2),
    ("1q", "6a^2 - 9a b - 15b^2", "3(2a - 5b)(a + b)", 2),
    ("1r", "6a b + 9a^2b - 15a^3b", "3a b*(1 - a)(2 + 5a)", 2),
    ("1s", "x^2 - 4y^2 + 4z^2 - 4x z", "(x - 2z + 2y)(x - 2z - 2y)", 2),
    ("1t", "a^2 + b^2 + 2a b + 2a + 2b", "(a + b)(a + b + 2)", 2),
    ("1u", "x^4 - y^4 - 4x^2 + 4", "(x^2 + y^2 - 2)(x^2 - y^2 - 2)", 3),
    ("1v", "p^2 + q^2 - r^2 - 2p q + 2r - 1", "(p - q + r - 1)(p - q - r + 1)", 3),
    ("1w", "15r^3 + 20r^2s - 20r s^2", "5r*(3r - 2s)(r + 2s)", 2),
    ("1x", "12x^2y - 36x y^2 + 27y^3", "3y*(2x - 3y)^2", 2),
    ("1y", "5a^3 - 15a b", "5a*(a^2 - 3b)", 1),
    ("1z", "3a^3 - 3", "3(a - 1)(a^2 + a + 1)", 2),
])

serie("Factoriza: …", F4, [
    ("2a", "x^4 - 81", "(x^2 + 9)(x + 3)(x - 3)", 2,
     dict(notas="El texto alternativo dice «x² − 81»; la imagen dice x⁴ − 81.")),
    ("2b", "16v^3 - 48v^2w + 36v w^2", "4v*(2v - 3w)^2", 2),
    ("2c", "b^3 + 3b^2 - 16b - 48", "(b + 3)(b + 4)(b - 4)", 2,
     dict(notas="El texto alternativo dice «b³ − 3b²»; la imagen dice b³ + 3b².")),
    ("2d", "32m^5n - 48m^3n w + 18m n w^2", "2m n*(4m^2 - 3w)^2", 3,
     dict(notas="En el módulo el último término es «18mn²w»; así no queda un trinomio cuadrado "
                "perfecto. Se corrigió a 18mnw².")),
    ("2e", "s^3t + 2s^2t + s t v^2 - s t w^2", "s t*(s^2 + 2s + v^2 - w^2)", 2,
     dict(notas="Así está impreso: solo se saca el factor común st. Parece una errata (con "
                "2s²tv quedaría st(s + v + w)(s + v − w)).")),
    ("2f", "12m n - 4p n + 12m p - 4p^2", "4(3m - p)(n + p)", 2),
    ("2g", "(4/5)x^2y^3 - (4/5)x^2", "(4/5)x^2*(y - 1)(y^2 + y + 1)", 2),
    ("2h", "(1/4)x^4 - 4x^2 - 64", "(1/4)(x^4 - 16x^2 - 256)", 2,
     dict(notas="Así está impreso: después de sacar 1/4 el polinomio no se factoriza con "
                "coeficientes enteros (posible errata).")),
    ("2i", "(1/8)x^2y + 12x y^2 + 10y^3", "(1/8)y*(x^2 + 96x y + 80y^2)", 2,
     dict(notas="Así está impreso: después de sacar y/8 el trinomio no se factoriza con "
                "coeficientes enteros (posible errata).")),
    ("2j", "(x^2 - 2x y)(a + 1) + y^2*(a + 1)", "(a + 1)(x - y)^2", 2),
    ("2k", "(1/3)a^2x - (4/3)b^2x + (2/3)a^2y - (8/3)b^2y", "(1/3)(a + 2b)(a - 2b)(x + 2y)", 3),
    ("2l", "5a^2x^4 - (20/9)a^2", "(5/9)a^2*(3x^2 + 2)(3x^2 - 2)", 3,
     dict(rtex=r"5a^{2}\left(x^{4} - \frac{4}{9}\right) = "
               r"\frac{5}{9}a^{2}\left(3x^{2} + 2\right)\left(3x^{2} - 2\right)")),
    ("2m", "70m^4 + 26m^3 - 24m^2", "2m^2*(7m - 3)(5m + 4)", 3),
    ("2n", "16w^5v - 56w^3v^3 + 49w v^5", "w v*(4w^2 - 7v^2)^2", 2),
    ("2p", "(x + y)^6 - 1",
     "(x + y + 1)(x + y - 1)(x^2 + 2x y + y^2 - x - y + 1)(x^2 + 2x y + y^2 + x + y + 1)", 3,
     dict(rtex=r"(x + y + 1)(x + y - 1)\left[(x + y)^{2} - (x + y) + 1\right]"
               r"\left[(x + y)^{2} + (x + y) + 1\right]")),
    ("2q", "a^2 - b^2 + a^3 - b^3", "(a - b)(a^2 + a b + b^2 + a + b)", 3),
    ("2s", "5a^5 + 3a^3 + 3a", "a*(5a^4 + 3a^2 + 3)", 1),
])

mm, nn = sp.symbols("m n", positive=True, integer=True)


@ejercicio(
    id=_id(), tipo="calculo", dificultad=3, fuente=f"{F4} 2o",
    enunciado=r"Factoriza: $x^{2m + 2} - x^{2}y^{2n}$ ($m$ y $n$ son enteros positivos).",
    respuesta=r"$x^{2}\left(x^{2m} - y^{2n}\right) = x^{2}\left(x^{m} + y^{n}\right)"
              r"\left(x^{m} - y^{n}\right)$.", **COMUN)
def _():
    producto = sp.expand(x**2 * (x**mm + y**nn) * (x**mm - y**nn))
    assert sp.simplify(sp.powsimp(producto) - (x ** (2 * mm + 2) - x**2 * y ** (2 * nn))) == 0
    for k in range(1, 4):
        for j in range(1, 4):
            assert sp.expand(x**2 * (x**k + y**j) * (x**k - y**j)) == x ** (2 * k + 2) - x**2 * y ** (2 * j)
