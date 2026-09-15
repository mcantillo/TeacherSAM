"""Banco de ejercicios — Matemáticas (Geometría 3°) — Líneas: horizontales, verticales e
inclinadas; líneas cerradas: dentro, fuera y en el borde.
Fuente: ejercicios propios para la guía del trimestre I de Geometría 3° (hilo: Rinrín Renacuajo
sale de paseo). El banco no tenía ningún ejercicio de 3° ni de este tema en grados vecinos
(excepción aprobada por la docente el 2026-09-15 para grados sin ejercicios en el banco).
Cada dibujo de la guía se hace con las mismas coordenadas que usa la comprobación (ver notas).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/lineas-3.py
"""
from sympy import Point, Polygon, Segment

from ejercicios import ejercicio

FUENTE = "propio — guía Geometría 3°, trimestre I, tema Líneas"
COMUN = dict(tema="líneas", grados=[3], dba=["matematicas-3-6"])

# Horizontales, verticales e inclinadas.
LINEAS = {1: Segment(Point(0, 0), Point(3, 0)), 2: Segment(Point(4, 0), Point(4, 2)),
          3: Segment(Point(5, 0), Point(7, 2)), 4: Segment(Point(8, 2), Point(11, 2))}


def posicion(s):
    d = s.p2 - s.p1
    return "vertical" if d.x == 0 else "horizontal" if d.y == 0 else "inclinada"


@ejercicio(id="lineas-3-002", tipo="conceptual", dificultad=1, fuente=FUENTE,
           enunciado=r"Mira las cuatro líneas del dibujo. Escribe al lado de cada número si la "
                     r"línea es horizontal, vertical o inclinada.",
           respuesta=r"1: horizontal. 2: vertical. 3: inclinada. 4: horizontal.",
           notas="Dibujo: 1 (0,0)–(3,0); 2 (4,0)–(4,2); 3 (5,0)–(7,2); 4 (8,2)–(11,2).",
           **COMUN)
def _():
    assert [posicion(LINEAS[k]) for k in (1, 2, 3, 4)] == \
        ["horizontal", "vertical", "inclinada", "horizontal"]


# Dentro, fuera y en el borde del charco (rectángulo 0..6 × 0..4).
CHARCO = Polygon(Point(0, 0), Point(6, 0), Point(6, 4), Point(0, 4))
COSAS = {"Rinrín": Point(2, 2), "la mosca": Point(8, 3), "la flor": Point(6, 1), "la hoja": Point(4, 0)}


def lugar(p):
    if any(lado.contains(p) for lado in CHARCO.sides):
        return "borde"
    return "dentro" if CHARCO.encloses_point(p) else "fuera"


@ejercicio(id="lineas-3-004", tipo="conceptual", dificultad=1, fuente=FUENTE,
           enunciado=r"El borde del charco de Rinrín es una línea cerrada (mira el dibujo). "
                     r"¿Quién está dentro del charco, quién está fuera y quién está justo en el "
                     r"borde: Rinrín, la mosca, la flor o la hoja?",
           respuesta=r"Dentro: Rinrín. Fuera: la mosca. En el borde: la flor y la hoja.",
           notas="Dibujo: rectángulo (0,0)–(6,4); Rinrín (2,2), mosca (8,3), flor (6,1), hoja (4,0).",
           **COMUN)
def _():
    r = {k: lugar(p) for k, p in COSAS.items()}
    assert r == {"Rinrín": "dentro", "la mosca": "fuera", "la flor": "borde", "la hoja": "borde"}
