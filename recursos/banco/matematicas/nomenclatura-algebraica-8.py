"""Banco de ejercicios — Álgebra 8° — Reducción de términos semejantes.
Fuente: Baldor, Álgebra (1983), transcripción parcial en recursos/algebra/baldor/baldor.tex
(Nomenclatura algebraica, pp. 14-23). La transcripción usa punto decimal: aquí, coma decimal.
La sección de nomenclatura y clasificación de la transcripción solo trae ejercicios de
reducción (ejercicio 10); no hay ejercicios de clasificación, grado ni valor numérico.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/nomenclatura-algebraica-8.py
"""
import re

from sympy import Add, expand

from ejercicios import ejercicio, expresion

FUENTE = "Baldor, Álgebra (1983), Reducción de términos semejantes — Ejercicio 10, p. 23,"
COMUN = dict(tema="reducción de términos semejantes", grados=[8],
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
    """Número de términos de la respuesta escrita (signos + y - de primer nivel)."""
    nivel, n = 0, 1
    for i, c in enumerate(s):
        nivel += c in "({[" and 1 or c in ")}]" and -1 or 0
        n += nivel == 0 and c in "+-" and i > 0
    return n


# (n, literal en la transcripción, polinomio, reducción escrita a mano, dificultad, notas)
FILAS = [
    (1, "1", "7a-9b+6a-4b", "13a-13b", 1, None),
    (2, "2", "a+b-c-b-c+2c-a", "0", 1, None),
    (3, "3", "5x-11y-9+20x-1-y", "25x-12y-10", 1, None),
    (4, "4", "-6m+8n+5-m-n-6m-11", "-13m+7n-6", 1, None),
    (5, "5", "-1+b+2b-2c+3a+2c-3b", "3a-1", 1, None),
    (6, "6", "-81x+19y-30z+6y+80x+x-25y", "-30z", 1, None),
    (7, "7", "15a^2-6ab-8a^2+20-5ab-31+a^2-ab", "8a^2-12ab-11", 1, None),
    (8, "8", "-3a+4b-6a+81b-114b+31a-a-b", "21a-30b", 1, None),
    (9, "9", "-71a^3b-84a^4b^2+50a^3b+84a^4b^2-45a^3b+18a^3b", "-48a^3b", 1, None),
    (10, "10", "-a+b-c+8+2a+2b-19-2c-3a-3-3b+3c", "-2a-14", 1, None),
    (11, "11", "a^{m+2}-x^{m+3}-5+8-3a^{m+2}+5x^{m+3}-6+a^{m+2}-5x^{m+3}",
     "-a^{m+2}-x^{m+3}-3", 2, "Es el n.º 14 del ejercicio 10 de Baldor (la transcripción salta "
     "números)."),
    (12, "12", r"\frac{1}{2}a+\frac{1}{3}b+2a-3b-\frac{3}{4}a-\frac{1}{6}b+\frac{3}{4}-\frac{1}{2}",
     r"\frac{7}{4}a-\frac{17}{6}b+\frac{1}{4}", 2, "Es el n.º 16 del ejercicio 10 de Baldor."),
    (13, "13", r"\frac{3}{25}a^{m-1}-\frac{7}{50}b^{m-1}+\frac{3}{5}a^{m-1}-\frac{1}{25}b^{m-1}"
               r"-0{,}2a^{m-1}+\frac{1}{5}b^{m-1}",
     r"\frac{13}{25}a^{m-1}+\frac{1}{50}b^{m-1}", 3,
     "En la transcripción falta el signo entre «-7/50 b^{m-1}» y «3/5 a^{m-1}»; se puso «+». "
     "El «0.2» se escribe con coma decimal. Es el n.º 20 de Baldor con los exponentes de b "
     "modificados por quien transcribió."),
]

for n, literal, poli, red, dif, notas in FILAS:
    extra = dict(notas=notas) if notas else {}

    @ejercicio(id=f"nomenclatura-algebraica-8-{n:03d}", dificultad=dif,
               fuente=f"{FUENTE} n.º {literal}",
               enunciado=f"Reduce los términos semejantes: ${poli}$.",
               respuesta=f"${red}$.", **extra, **COMUN)
    def _(poli=poli, red=red):
        assert expand(ltx(poli) - ltx(red)) == 0, "la reducción no es equivalente"
        assert len(Add.make_args(expand(ltx(red)))) == terminos(red), "quedan términos semejantes"
