"""Banco de ejercicios — Álgebra 8° — Supresión de signos de agrupación.
Fuente: Baldor, Álgebra (1983), transcripción parcial en recursos/algebra/baldor/baldor.tex
(Signos de agrupación, pp. 58-60). En la transcripción, los n.º 1-8 son del ejercicio 31 de
Baldor y los n.º 9-18 del ejercicio 32 (anotado en los comentarios del .tex).
Los ejercicios de supresión de signos con productos indicados están en
multiplicacion-algebraica-8.py.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/signos-agrupacion-8.py
"""
import re

from sympy import Add, expand

from ejercicios import ejercicio, expresion

FUENTE = "Baldor, Álgebra (1983), Signos de agrupación — Ejercicio 31, p. 60,"
COMUN = dict(tema="signos de agrupación", grados=[8],
             dba=["matematicas-8-3", "matematicas-8-9"], tipo="calculo")


def ltx(s):
    """SymPy de una expresión escrita en LaTeX sencillo (letras sueltas = variables)."""
    s = s.replace(r"\left", "").replace(r"\right", "").replace("{,}", ".")
    s = s.replace(r"\lbrack", "(").replace(r"\rbrack", ")").replace("[", "(").replace("]", ")")
    s = re.sub(r"\\d?frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", s)
    s = re.sub(r"\^\{([^{}]*)\}", r"^(\1)", s)
    s = re.sub(r"(?<=[a-z])(?=[a-z])", "*", s)
    return expresion(s)


def terminos(s):
    nivel, n = 0, 1
    for i, c in enumerate(s):
        nivel += c in "({[" and 1 or c in ")}]" and -1 or 0
        n += nivel == 0 and c in "+-" and i > 0
    return n


# (n, expresión, resultado escrito a mano, dificultad, notas)
FILAS = [
    (1, "x-(x-y)", "y", 1, None),
    (2, "x^2+(-3x-x^2+5)", "-3x+5", 1, None),
    (3, "a+b-(-2a+3)", "3a+b-3", 1, None),
    (4, "4m-(-2m-n)", "6m+n", 1, None),
    (5, "2x+3y-(4x+3y)", "-2x", 1, None),
    (6, "a+(a-b)+(-a+b)", "a", 1, None),
    (7, "a-(b+a)+(-a+b)-(-a+2b)", "-2b", 1, "Es el n.º 12 del ejercicio 31 de Baldor."),
    (8, "-(a+b)+(-a-b)-(-b+a)+(3a+b)", "0", 1, "Es el n.º 15 del ejercicio 31 de Baldor."),
    (9, r"2a+\lbrack a-(a+b)\rbrack", "2a-b", 1, "Es el n.º 1 del ejercicio 32 de Baldor."),
    (10, r"3x-\lbrack x+y-(2x+y)\rbrack", "4x", 1, "Es el n.º 2 del ejercicio 32 de Baldor."),
    (11, r"2m-\lbrack(m-n)-(m+n)\rbrack", "2m+2n", 1, "Del ejercicio 32 de Baldor."),
    (12, r"4x^2+\lbrack-(x^2-xy)+(-3y^2+2xy)-(-3x^2+y^2)\rbrack", "6x^2+3xy-4y^2", 2,
     "Del ejercicio 32 de Baldor."),
    (13, r"a+\lbrack(-2a+b)-(-a+b-c)+a\rbrack", "a+c", 2, "Del ejercicio 32 de Baldor."),
    (14, r"4m-\lbrack 2m+(n-3)\rbrack+\lbrack-4n-(2m+1)\rbrack", "-5n+2", 2,
     "Del ejercicio 32 de Baldor."),
    (15, r"2x+\lbrack-5x-(-2y+\lbrack-x+y\rbrack)\rbrack", "-2x+y", 2,
     "Del ejercicio 32 de Baldor."),
    (16, r"x^2-\lbrack-7xy+(-y^2+\lbrack-x^2+3xy-2y^2\rbrack)\rbrack", "2x^2+4xy+3y^2", 2,
     "Del ejercicio 32 de Baldor."),
    (17, r"-(a+b)+(-3a+b-\lbrack-2a+b-(a-b)\rbrack+2a)", "a-2b", 3,
     "Del ejercicio 32 de Baldor."),
    (18, r"(-x+y)-(4x+2y+\lbrack-x-y-(x+y)\rbrack)", "-3x+y", 3,
     "Del ejercicio 32 de Baldor."),
]

for n, expr, res, dif, notas in FILAS:
    extra = dict(notas=notas) if notas else {}

    @ejercicio(id=f"signos-agrupacion-8-{n:03d}", dificultad=dif, fuente=f"{FUENTE} n.º {n}",
               enunciado=f"Simplifica, suprimiendo los signos de agrupación y reduciendo "
                         f"términos semejantes: ${expr}$.",
               respuesta=f"${res}$.", **extra, **COMUN)
    def _(expr=expr, res=res):
        assert expand(ltx(expr) - ltx(res)) == 0, "el resultado no es equivalente"
        assert len(Add.make_args(expand(ltx(res)))) == terminos(res), "quedan términos semejantes"
