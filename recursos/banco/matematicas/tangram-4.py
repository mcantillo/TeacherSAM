"""Banco de ejercicios — Matemáticas (Geometría 4°) — Figuras con polígonos: el tangram (armar,
desarmar y crear formas, evidencia 1 del DBA 6 de 4°).
Fuente: ejercicios propios para la guía del trimestre I de Geometría 4° (hilo: La vuelta al
mundo en 80 días). Tangram clásico de 7 piezas dibujado en un cuadrado de 4 × 4. El banco no
tenía ningún ejercicio de tangram ni de 4° (excepción aprobada por la docente el 2026-09-15).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/tangram-4.py
"""
from itertools import combinations

from sympy import Polygon, pi

from ejercicios import ejercicio

FUENTE = "propio — guía Geometría 4°, trimestre I, tema Figuras con polígonos"
COMUN = dict(tema="figuras con polígonos", grados=[4], dba=["matematicas-4-6"])

PIEZAS = {
    "triángulo grande 1": Polygon((0, 0), (4, 0), (2, 2)),
    "triángulo grande 2": Polygon((0, 0), (2, 2), (0, 4)),
    "triángulo mediano": Polygon((4, 2), (4, 4), (2, 4)),
    "triángulo pequeño 1": Polygon((4, 0), (4, 2), (3, 1)),
    "triángulo pequeño 2": Polygon((2, 2), (3, 3), (1, 3)),
    "cuadrado": Polygon((2, 2), (3, 1), (4, 2), (3, 3)),
    "paralelogramo": Polygon((0, 4), (1, 3), (3, 3), (2, 4)),
}
MARCO = Polygon((0, 0), (4, 0), (4, 4), (0, 4))


def area(p):
    return abs(p.area)


def dentro_o_borde(poly, q):
    return poly.encloses_point(q) or any(s.contains(q) for s in poly.sides)


def no_se_montan(polis):
    return all(not b.encloses_point(a.centroid) and not a.encloses_point(b.centroid)
               for a, b in combinations(polis, 2))


def tipo(p):
    n = len(p.vertices)
    if n == 3:
        return "triángulo"
    v = p.vertices
    lados = [v[(i + 1) % 4] - v[i] for i in range(4)]
    par = all(lados[i].x * lados[i + 2].y - lados[i].y * lados[i + 2].x == 0 for i in (0, 1))
    rectos = all(a == pi / 2 for a in p.angles.values())
    iguales = len({s.length for s in p.sides}) == 1
    if par and rectos and iguales:
        return "cuadrado"
    return "paralelogramo" if par else "cuadrilátero"


@ejercicio(id="tangram-4-001", tipo="conceptual", dificultad=1, fuente=FUENTE,
           enunciado=r"Observa las siete piezas del tangram en el dibujo. ¿Cuántas son "
                     r"triángulos? ¿Cuáles son cuadriláteros y cómo se llaman?",
           respuesta=r"5 triángulos (2 grandes, 1 mediano y 2 pequeños) y 2 cuadriláteros: un "
                     r"cuadrado y un paralelogramo.",
           notas="Dibujo: coordenadas de PIEZAS en el cuadrado 4 × 4.",
           **COMUN)
def _():
    polis = list(PIEZAS.values())
    assert sum(area(p) for p in polis) == area(MARCO)              # las 7 piezas llenan el cuadrado
    assert all(dentro_o_borde(MARCO, q) for p in polis for q in p.vertices)
    assert no_se_montan(polis)
    tipos = [tipo(p) for p in polis]
    assert tipos.count("triángulo") == 5 and sorted(t for t in tipos if t != "triángulo") == \
        ["cuadrado", "paralelogramo"]


# Dos triángulos pequeños (rectángulos e isósceles, catetos 1) forman tres figuras.
T1 = Polygon((0, 0), (1, 0), (1, 1))
UNIONES = {
    "cuadrado": (Polygon((0, 0), (1, 1), (0, 1)), Polygon((0, 0), (1, 0), (1, 1), (0, 1))),
    "triángulo": (Polygon((1, 0), (2, 0), (1, 1)), Polygon((0, 0), (2, 0), (1, 1))),
    "paralelogramo": (Polygon((1, 0), (2, 1), (1, 1)), Polygon((0, 0), (1, 0), (2, 1), (1, 1))),
}


@ejercicio(id="tangram-4-003", tipo="conceptual", dificultad=2, fuente=FUENTE,
           enunciado=r"Con los dos triángulos pequeños del tangram se pueden armar tres figuras "
                     r"distintas juntando dos lados iguales. Dibújalas y escribe su nombre.",
           respuesta=r"Un cuadrado, un triángulo (más grande) y un paralelogramo.",
           **COMUN)
def _():
    lados_t1 = sorted(s.length for s in T1.sides)
    for nombre, (t2, contorno) in UNIONES.items():
        assert sorted(s.length for s in t2.sides) == lados_t1       # es otro triangulito igual
        assert area(T1) + area(t2) == area(contorno)
        assert all(dentro_o_borde(contorno, q) for q in T1.vertices + t2.vertices)
        assert no_se_montan([T1, t2])
        assert tipo(contorno) == nombre
