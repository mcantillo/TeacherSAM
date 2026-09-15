"""Banco de ejercicios — Matemáticas (Geometría 4°) — Polígonos: línea poligonal abierta y
cerrada; lados, vértices y ángulos; nombres según el número de lados.
Fuente: ejercicios propios para la guía del trimestre I de Geometría 4° (hilo: La vuelta al
mundo en 80 días). El banco no tenía ningún ejercicio de 4°; poligonos-6-001 (6°) está sin
verificar y es de otro grado (excepción aprobada por la docente el 2026-09-15).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/poligonos-4.py
"""
from sympy import Polygon

from ejercicios import ejercicio

FUENTE = "propio — guía Geometría 4°, trimestre I, tema Polígonos"
COMUN = dict(tema="polígonos", grados=[4], dba=["matematicas-4-6"])

NOMBRES = {3: "triángulo", 4: "cuadrilátero", 5: "pentágono", 6: "hexágono", 8: "octágono"}

# ¿Es polígono? Cada figura es una lista de trozos: ("seg", a, b) o ("arco", a, b).
FIGURAS = {
    1: [("seg", (0, 0), (2, 0)), ("seg", (2, 0), (3, 2)), ("seg", (3, 2), (1, 3)),
        ("seg", (1, 3), (-1, 2)), ("seg", (-1, 2), (0, 0))],
    2: [("seg", (4, 0), (5, 2)), ("seg", (5, 2), (6, 0)), ("seg", (6, 0), (7, 2))],
    3: [("seg", (8, 0), (10, 0)), ("arco", (10, 0), (8, 0))],
    4: [("seg", (11, 0), (14, 0)), ("seg", (14, 0), (13, 2)), ("seg", (13, 2), (11, 2)),
        ("seg", (11, 2), (11, 0))],
}


def es_poligono(trozos):
    cerrada = trozos[0][1] == trozos[-1][2] and all(
        a[2] == b[1] for a, b in zip(trozos, trozos[1:]))
    return cerrada and all(t[0] == "seg" for t in trozos)


@ejercicio(id="poligonos-4-001", tipo="conceptual", dificultad=1, fuente=FUENTE,
           enunciado=r"¿Cuáles de las cuatro figuras del dibujo son polígonos? Para las que no "
                     r"lo son, explica por qué.",
           respuesta=r"Son polígonos la 1 y la 4. La 2 no, porque es una línea poligonal abierta. "
                     r"La 3 no, porque uno de sus lados es curvo.",
           notas="Dibujo: 1 pentágono (0,0),(2,0),(3,2),(1,3),(-1,2); 2 zigzag abierto "
                 "(4,0),(5,2),(6,0),(7,2); 3 segmento (8,0)–(10,0) cerrado con un arco por arriba; "
                 "4 cuadrilátero (11,0),(14,0),(13,2),(11,2).",
           **COMUN)
def _():
    assert [k for k, f in FIGURAS.items() if es_poligono(f)] == [1, 4]


POLIGONOS = {
    "A": Polygon((0, 0), (3, 0), (1, 2)),
    "B": Polygon((0, 0), (4, 0), (3, 2), (1, 3)),
    "C": Polygon((0, 0), (2, 0), (3, 2), (1, 3), (-1, 2)),
    "D": Polygon((0, 0), (3, 0), (4, 2), (3, 4), (0, 4), (-1, 2)),
    "E": Polygon((1, 0), (3, 0), (4, 1), (4, 3), (3, 4), (1, 4), (0, 3), (0, 1)),
}


@ejercicio(id="poligonos-4-002", tipo="calculo", dificultad=1, fuente=FUENTE,
           enunciado=r"Para cada polígono del dibujo (A a E), cuenta sus lados, sus vértices y "
                     r"sus ángulos, y escribe su nombre.",
           respuesta=r"A: 3, 3, 3, triángulo. B: 4, 4, 4, cuadrilátero. C: 5, 5, 5, pentágono. "
                     r"D: 6, 6, 6, hexágono. E: 8, 8, 8, octágono.",
           notas="Dibujo: coordenadas de POLIGONOS.",
           **COMUN)
def _():
    r = {k: (len(p.sides), len(p.vertices), len(p.angles), NOMBRES[len(p.sides)])
         for k, p in POLIGONOS.items()}
    assert r == {"A": (3, 3, 3, "triángulo"), "B": (4, 4, 4, "cuadrilátero"),
                 "C": (5, 5, 5, "pentágono"), "D": (6, 6, 6, "hexágono"),
                 "E": (8, 8, 8, "octágono")}
