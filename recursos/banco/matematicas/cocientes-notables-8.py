"""Banco de ejercicios — Álgebra 8° — Cocientes notables.
Fuente: módulo de Matemáticas 8° de las Guías de Apoyo (Adriana Quintero Palomino), Tema 3,
Cocientes notables; se lee en
recursos/matematicas/Guías pedagógicas Matemáticas/markdown/08 - Modulo_Matematicas_Octavo.md
OJO: estas fórmulas son imágenes en el .docx (la copia markdown las pierde); los literales
siguen el orden del .docx y cada fórmula se transcribió de la imagen impresa.
El ejercicio 15 del módulo («Calcula») repite 14a, 14c y 14b: no se duplicó.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/cocientes-notables-8.py
"""
import sympy as sp

from ejercicios import ejercicio, expresion as E, tex

FUENTE = "módulo 8° (Quintero Palomino), Tema 3, Cocientes notables — Practica lo aprendido"
COMUN = dict(tema="cocientes notables", grados=[8], dba=["matematicas-8-3", "matematicas-8-9"],
             tipo="calculo")
_n = [0]


def _id():
    _n[0] += 1
    return f"cocientes-notables-8-{_n[0]:03d}"


def serie_cocientes(instr, filas):
    """Filas (literal, cociente, respuesta, dificultad[, notas o dict(notas=…, etex=…)]).
    Comprueba que la división es exacta y que el cociente es el polinomio escrito a mano."""
    for lit, expr, ans, dif, *resto in filas:
        opc = resto[0] if resto else {}
        opc = {"notas": opc} if isinstance(opc, str) else opc
        meta = dict(COMUN, id=_id(), dificultad=dif, fuente=f"{FUENTE} {lit}",
                    enunciado=instr.replace("…", f"${opc.get('etex') or tex(expr)}$"),
                    respuesta=f"${tex(ans)}$.")
        if "notas" in opc:
            meta["notas"] = opc["notas"]

        def comprobar(expr=expr, ans=ans):
            num, den = sp.fraction(E(expr))
            cociente, resto = sp.div(sp.expand(num), sp.expand(den), *sorted(num.free_symbols, key=str))
            assert resto == 0, "la división no es exacta"
            assert sp.expand(cociente - E(ans)) == 0, "el cociente no coincide"
        ejercicio(**meta)(comprobar)


serie_cocientes("Halla por simple inspección el cociente: …", [
    ("13a", "(x^5 - 1)/(x - 1)", "x^4 + x^3 + x^2 + x + 1", 1),
    ("13b", "(8m^3 + n^6)/(2m + n^2)", "4m^2 - 2m n^2 + n^4", 2),
    ("13c", "(1 - a^3)/(1 - a)", "1 + a + a^2", 1),
    ("13d", "(x^3 - 8y^3)/(x - 2y)", "x^2 + 2x y + 4y^2", 1),
    ("13e", "(x^6 - 49y^6)/(x^3 + 7y^3)", "x^3 - 7y^3", 1),
    ("13f", "(a^16 - b^16)/(a^2 + b^2)",
     "a^14 - a^12b^2 + a^10b^4 - a^8b^6 + a^6b^8 - a^4b^10 + a^2b^12 - b^14", 3),
    ("13g", "(1 + a^3)/(1 + a)", "1 - a + a^2", 1),
    ("13h", "(16x^2y^4 - 25m^6)/(4x y^2 + 5m^3)", "4x y^2 - 5m^3", 1),
    ("13i", "(x^27 + y^27)/(x^3 + y^3)",
     "x^24 - x^21y^3 + x^18y^6 - x^15y^9 + x^12y^12 - x^9y^15 + x^6y^18 - x^3y^21 + y^24", 3),
    ("13j", "(a^9 + y^9)/(a + y)",
     "a^8 - a^7y + a^6y^2 - a^5y^3 + a^4y^4 - a^3y^5 + a^2y^6 - a y^7 + y^8", 2),
    ("13k", "(a^4b^4 - 64x^6)/(a^2b^2 + 8x^3)", "a^2b^2 - 8x^3", 1),
    ("13l", "(1 - a^2b^4c^8)/(1 - a b^2c^4)", "1 + a b^2c^4", 1),
    ("13m", "(32x^5 + 243y^5)/(2x + 3y)", "16x^4 - 24x^3y + 36x^2y^2 - 54x y^3 + 81y^4", 2),
    ("13n", "(16 - (a + 1)^2)/(4 + (a + 1))", "3 - a", 2,
     dict(etex=r"\frac{16 - (a + 1)^{2}}{4 + (a + 1)}")),
    ("13o", "(1 - x^12)/(1 - x^4)", "1 + x^4 + x^8", 2),
    ("13p", "(64x^6 - 343y^9)/(4x^2 - 7y^3)", "16x^4 + 28x^2y^3 + 49y^6", 2),
    ("13q", "(a^18 - b^18)/(a^3 + b^3)", "a^15 - a^12b^3 + a^9b^6 - a^6b^9 + a^3b^12 - b^15", 3,
     "El texto alternativo dice «a³b³» en el divisor; la imagen impresa dice a³ + b³."),
    ("13r", "(1 + x^11)/(x + 1)",
     "1 - x + x^2 - x^3 + x^4 - x^5 + x^6 - x^7 + x^8 - x^9 + x^10", 2),
    ("13s", "(x^40 - y^40)/(x^8 - y^8)", "x^32 + x^24y^8 + x^16y^16 + x^8y^24 + y^32", 2),
    ("13t", "(9 - 36x^10)/(3 + 6x^5)", "3 - 6x^5", 1),
    ("13u", "(36m^2 - 49n^2x^4)/(6m - 7n x^2)", "6m + 7n x^2", 1),
    ("13v", "(a^4b^6 - 4x^8y^10)/(a^2b^3 + 2x^4y^5)", "a^2b^3 - 2x^4y^5", 1),
    ("13x", "((a - x)^2 - y^2)/((a - x) - y)", "a - x + y", 2,
     dict(etex=r"\frac{(a - x)^{2} - y^{2}}{(a - x) - y}")),
])

m = sp.symbols("m", positive=True, integer=True)
x = sp.symbols("x")


@ejercicio(
    id=_id(), dificultad=3, fuente=f"{FUENTE} 13w",
    enunciado=r"Halla por simple inspección el cociente: "
              r"$\dfrac{1 - 9x^{2m + 4}}{1 + 3x^{m + 2}}$.",
    respuesta=r"$1 - 3x^{m + 2}$, porque $1 - 9x^{2m + 4} = 1 - \left(3x^{m + 2}\right)^{2}$.",
    **COMUN)
def _():
    t = x ** (m + 2)
    assert sp.simplify(sp.expand((1 - 3 * t) * (1 + 3 * t)) - (1 - 9 * x ** (2 * m + 4))) == 0
    for k in range(1, 6):                                  # comprobación con valores de m
        num, den = 1 - 9 * x ** (2 * k + 4), 1 + 3 * x ** (k + 2)
        assert sp.div(num, den, x) == (1 - 3 * x ** (k + 2), 0)


serie_cocientes("Escribe el cociente sin efectuar la división: …", [
    ("14a", "(x^8 - 1)/(1 + x^4)", "x^4 - 1", 1),
    ("14b", "(27m^3 + n^6)/(3m + n^2)", "9m^2 - 3m n^2 + n^4", 2),
    ("14c", "(1 - a^7)/(1 - a)", "1 + a + a^2 + a^3 + a^4 + a^5 + a^6", 1),
    ("14d", "(x^18 - 125y^3)/(x^6 - 5y)", "x^12 + 5x^6y + 25y^2", 2),
    ("14e", "(x^12 - 81y^2)/(x^6 + 9y)", "x^6 - 9y", 1),
    ("14f", "(m^14 - n^14)/(m^2 - n^2)",
     "m^12 + m^10n^2 + m^8n^4 + m^6n^6 + m^4n^8 + m^2n^10 + n^12", 2),
    ("14g", "(1 + a^7)/(1 + a)", "1 - a + a^2 - a^3 + a^4 - a^5 + a^6", 2,
     "En el módulo aparece (1 + a⁶)/(1 + a), que no es exacta (a⁶ + 1 da residuo 2 al dividir "
     "por a + 1: la suma de potencias pares no es divisible por la suma de las bases); se "
     "cambió el exponente a 7."),
    ("14h", "(25x^2y^4 - 4m^6)/(5x y^2 + 2m^3)", "5x y^2 - 2m^3", 1),
    ("14i", "(1 + y^11)/(y + 1)",
     "1 - y + y^2 - y^3 + y^4 - y^5 + y^6 - y^7 + y^8 - y^9 + y^10", 2),
    ("14j", "(100 - (x + 1)^2)/(10 + (x + 1))", "9 - x", 2,
     dict(etex=r"\frac{100 - (x + 1)^{2}}{10 + (x + 1)}")),
    ("14k", "(x^3 + y^12)/(x + y^4)", "x^2 - x y^4 + y^8", 2,
     "En el módulo aparece (y³ + y¹²)/(y + x⁴), que no es un cociente notable (ni una división "
     "exacta); se corrigió a (x³ + y¹²)/(x + y⁴), suma de cubos."),
    ("14l", "(100x^6 - 36y^8)/(10x^3 - 6y^4)", "10x^3 + 6y^4", 1),
    ("14m", "(a^12 - b^12)/(a^4 - b^4)", "a^8 + a^4b^4 + b^8", 2,
     "En la imagen del módulo el divisor es a⁴ + b⁴ (el texto alternativo dice a⁴b⁴); con ese "
     "divisor la división no es exacta (residuo −2b¹²). Se corrigió a a⁴ − b⁴."),
    ("14n", "((m + n)^6 - y^6)/((m + n)^2 - y^2)", "(m + n)^4 + (m + n)^2y^2 + y^4", 3),
    ("14o", "(1 + x^13)/(x + 1)",
     "1 - x + x^2 - x^3 + x^4 - x^5 + x^6 - x^7 + x^8 - x^9 + x^10 - x^11 + x^12", 2),
    ("14p", "(x^20 - y^20)/(x^4 - y^4)", "x^16 + x^12y^4 + x^8y^8 + x^4y^12 + y^16", 2),
])
