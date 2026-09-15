"""Banco de ejercicios — Matemáticas (Geometría 3°) — Figuras planas: clasificar por número de
lados diciendo el criterio; el cuadrado girado sigue siendo cuadrado.
Fuente: ejercicios propios para la guía del trimestre I de Geometría 3° (hilo: Rinrín Renacuajo
sale de paseo). El banco no tenía ningún ejercicio de 3° ni de este tema en grados vecinos
(excepción aprobada por la docente el 2026-09-15).
Cada dibujo de la guía se hace con las mismas coordenadas que usa la comprobación (ver notas).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/figuras-planas-3.py
"""
from sympy import Polygon, pi

from ejercicios import ejercicio

FUENTE = "propio — guía Geometría 3°, trimestre I, tema Figuras planas"
COMUN = dict(tema="figuras planas", grados=[3], dba=["matematicas-3-6"])


def nombre(poli):
    """Nombre de 3° para un polígono: triángulo, cuadrado, rectángulo o «de n lados»."""
    n = len(poli.vertices)
    if n == 3:
        return "triángulo"
    if n == 4 and all(a == pi / 2 for a in poli.angles.values()):
        lados = {s.length for s in poli.sides}
        return "cuadrado" if len(lados) == 1 else "rectángulo"
    return f"{n} lados"


# Clasificar por número de lados (evidencia 2 del DBA: describir el criterio).
SEIS = {"A": Polygon((0, 0), (2, 0), (1, 2)),
        "B": Polygon((3, 0), (5, 0), (5, 2), (3, 2)),
        "C": Polygon((6, 0), (9, 0), (9, 1), (6, 1)),
        "D": Polygon((10, 0), (13, 0), (10, 1)),
        "E": Polygon((0, 3), (2, 3), (3, 4), (1, 5), (-1, 4)),
        "F": Polygon((4, 3), (7, 3), (6, 5), (5, 5))}


@ejercicio(id="figuras-planas-3-003", tipo="conceptual", dificultad=2, fuente=FUENTE,
           enunciado=r"Separa las seis figuras del dibujo en grupos según su número de lados. "
                     r"Escribe qué regla usaste para hacer los grupos.",
           respuesta=r"3 lados: A y D. 4 lados: B, C y F. 5 lados: E. La regla: contar los lados "
                     r"(o los vértices) de cada figura.",
           notas="Dibujo: A (0,0),(2,0),(1,2); B (3,0)–(5,2); C (6,0)–(9,1); D (10,0),(13,0),(10,1); "
                 "E (0,3),(2,3),(3,4),(1,5),(-1,4); F (4,3),(7,3),(6,5),(5,5).",
           **COMUN)
def _():
    grupos = {}
    for k, f in SEIS.items():
        grupos.setdefault(len(f.sides), []).append(k)
    assert grupos == {3: ["A", "D"], 4: ["B", "C", "F"], 5: ["E"]}
    assert all(len(f.sides) == len(f.vertices) for f in SEIS.values())


@ejercicio(id="figuras-planas-3-004", tipo="encuentra-el-error", dificultad=2, fuente=FUENTE,
           enunciado=r"El Ratón mira la figura del dibujo y dice: «No es un cuadrado, porque está "
                     r"de punta». ¿Tiene razón? Explica.",
           respuesta=r"No tiene razón. Sus 4 lados miden lo mismo y sus 4 esquinas son iguales "
                     r"(ángulos rectos): es un cuadrado. Solo está girado; girar una figura no "
                     r"cambia su forma.",
           notas="Dibujo: cuadrado girado (2,0),(4,2),(2,4),(0,2).",
           **COMUN)
def _():
    girado = Polygon((2, 0), (4, 2), (2, 4), (0, 2))
    assert nombre(girado) == "cuadrado"
