"""Banco de ejercicios — Matemáticas — Intervalos y operaciones con intervalos.
Fuente: módulo de Matemáticas 11° de las Guías de Apoyo (Adriana Quintero Palomino), Tema 1;
se lee en recursos/matematicas/Guías pedagógicas Matemáticas/markdown/11 - Modulo_Matematicas_Undecimo.md
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/intervalos.py
"""
from sympy import Complement, Intersection, Union

from ejercicios import conjunto, desigualdad, ejercicio, ejercicio_manual

FUENTE = "módulo 11° (Quintero Palomino), Tema 1, Intervalos — Practica lo aprendido"
COMUN = dict(tema="intervalos", grados=[11], dba=["matematicas-11-1"], tipo="calculo")

# 5. Desigualdades (unidas con «y» / «o») → intervalo:
#    (n, literal, desigualdades, conector, solución escrita a mano, dificultad)
DESIGUALDADES = [
    (1, "5a", ["x < -5", "x > -8"], "y", "(-8, -5)", 1),
    (2, "5b", ["x < -10", "x > 3"], "y", "vacio", 2),
    (3, "5c", ["x >= 9"], "y", "[9, oo)", 1),
    (4, "5d", ["x < 0", "x > -8"], "y", "(-8, 0)", 1),
    (5, "5e", ["x <= 2/3", "x > 3/2"], "o", "(-oo, 2/3] U (3/2, oo)", 2),
    (6, "5f", ["x <= 0", "x > 1/2"], "o", "(-oo, 0] U (1/2, oo)", 2),
    (7, "5g", ["x > -5/4"], "y", "(-5/4, oo)", 1),
    (8, "5h", ["x <= 2/3", "x > 3/2"], "y", "vacio", 2),
]
for n, literal, partes, conector, solucion, dificultad in DESIGUALDADES:
    formula = f" {conector} ".join(f"${desigualdad(p)[0]}$" for p in partes)
    vacia = " (ningún número cumple las dos)" if solucion == "vacio" else ""

    @ejercicio(id=f"intervalos-{n:03d}", dificultad=dificultad, fuente=f"{FUENTE} {literal}",
               enunciado=f"Escribe en forma de intervalo y representa en la recta real: {formula}.",
               respuesta=f"${conjunto(solucion)[0]}${vacia}.", **COMUN)
    def _(partes=partes, conector=conector, solucion=solucion):
        conjuntos = [desigualdad(p)[1] for p in partes]
        total = Intersection(*conjuntos) if conector == "y" else Union(*conjuntos)
        assert total == conjunto(solucion)[1]


# 6. Intervalo → desigualdad: (n, literal, intervalo, desigualdad escrita a mano, dif, notas)
INTERVALOS = [
    (9, "6a", "(-6, 8)", "-6 < x < 8", 1, None),
    (10, "6b", "[-3.6, 126]", "-3.6 <= x <= 126", 1,
     "En el módulo aparece «[-3,6, 126]»: con coma decimal, los extremos se separan con punto "
     "y coma."),
    (11, "6c", "[-2, 0)", "-2 <= x < 0", 1,
     "En el módulo aparece «[2, 0)», que no es un intervalo (el extremo izquierdo es mayor que "
     "el derecho); se corrigió a [-2, 0)."),
    (12, "6d", "(-4, 4.1]", "-4 < x <= 4.1", 1,
     "En el módulo aparece «(-4, 4,1]»; los extremos se separan con punto y coma."),
    (13, "6e", "(-oo, 3)", "x < 3", 1, None),
    (14, "6f", "(-oo, oo)", "-oo < x < oo", 2, None),
]
for n, literal, intervalo, texto, dificultad, notas in INTERVALOS:
    extra = dict(notas=notas) if notas else {}
    todos = " (todos los números reales)" if intervalo == "(-oo, oo)" else ""

    @ejercicio(id=f"intervalos-{n:03d}", dificultad=dificultad, fuente=f"{FUENTE} {literal}",
               enunciado=f"Expresa el intervalo ${conjunto(intervalo)[0]}$ como una desigualdad "
                         f"en términos de $x$.",
               respuesta=f"${desigualdad(texto)[0]}${todos}.", **extra, **COMUN)
    def _(intervalo=intervalo, texto=texto):
        assert desigualdad(texto)[1] == conjunto(intervalo)[1]


ejercicio_manual(
    id="intervalos-015", tema="intervalos", grados=[11], dba=["matematicas-11-1"],
    tipo="argumentacion", dificultad=2, fuente=f"{FUENTE} 7",
    enunciado=r"¿Por qué la notación $[\infty, 8)$ no es correcta?",
    respuesta=r"Porque $\infty$ no es un número real: no puede ser un extremo cerrado (el "
              r"corchete diría que se incluye) y además aparece a la izquierda de $8$, cuando "
              r"$\infty$ indica que el intervalo no termina hacia la derecha. Lo correcto sería "
              r"$(-\infty, 8)$.")


def operar(t):
    """(LaTeX, conjunto) de un intervalo o de una operación (A, op, B), op en U, ∩, -."""
    if isinstance(t, str):
        return conjunto(t)
    a, op, b = t
    (ta, ca), (tb, cb) = operar(a), operar(b)
    ta = rf"\bigl({ta}\bigr)" if isinstance(a, tuple) else ta
    tb = rf"\bigl({tb}\bigr)" if isinstance(b, tuple) else tb
    simbolo, resultado = {"U": (r"\cup", Union(ca, cb)), "∩": (r"\cap", Intersection(ca, cb)),
                          "-": ("-", Complement(ca, cb))}[op]
    return f"{ta} {simbolo} {tb}", resultado


# 8 y 9. Operaciones: (n, literal, operación, resultado escrito a mano, dificultad, notas)
OPERACIONES = [
    (16, "8a", ("(1, 6)", "U", "(-2, 9)"), "(-2, 9)", 1, None),
    (17, "8b", ("[-2, 6/7)", "∩", "[0, 1)"), "[0, 6/7)", 2, None),
    (18, "8c", ("[-2, 6/7)", "-", "[0, 1)"), "[-2, 0)", 2, None),
    (19, "8d", ("(-oo, -2/3)", "∩", "(-2/3, oo)"), "vacio", 2, None),
    (20, "8e", ("(-oo, 1/2)", "U", "(3/4, 8)"), "(-oo, 1/2) U (3/4, 8)", 1, None),
    (21, "8f", ("(-oo, 12)", "U", "(11.9, oo)"), "R", 2,
     "En el módulo aparece «(11,9, ∞)»; los extremos se separan con punto y coma."),
    (22, "8g", ("R", "-", ("(-oo, 5)", "U", "[6, oo)")), "[5, 6)", 3,
     "En el módulo se agrupa con llaves, «R - {(-∞, 5) ∪ [6, ∞)}»; se usan paréntesis."),
    (23, "8h", (("(-2, 8)", "U", "(0, 6]"), "∩", "[4, 7)"), "[4, 7)", 3,
     "En el módulo se agrupa con llaves; se usan paréntesis."),
    (24, "9a", ("(1, 6)", "U", "(-3, 5)"), "(-3, 6)", 1, None),
    (25, "9b", ("[-1, 1/2)", "∩", "(1, 5)"), "vacio", 1, None),
    (26, "9c", ("(-oo, 4)", "U", "(5, oo)"), "(-oo, 4) U (5, oo)", 1, None),
]
for n, literal, operacion, solucion, dificultad, notas in OPERACIONES:
    extra = dict(notas=notas) if notas else {}
    instruccion = ("Escribe como un intervalo o una unión de intervalos:" if literal[0] == "8"
                   else "Representa en la recta real y escribe el resultado:")

    @ejercicio(id=f"intervalos-{n:03d}", dificultad=dificultad, fuente=f"{FUENTE} {literal}",
               enunciado=f"{instruccion} ${operar(operacion)[0]}$.",
               respuesta=f"${conjunto(solucion)[0]}$.", **extra, **COMUN)
    def _(operacion=operacion, solucion=solucion):
        assert operar(operacion)[1] == conjunto(solucion)[1]
