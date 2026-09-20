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


# --- Añadidos el 2026-09-20 para el taller de la sesión 004 (semana 04) --------------
# El 002 y el 004 los usa la guía. Estos tres son del taller: abiertas y cerradas, y el
# borde como frontera. Mismas coordenadas en el dibujo y en la comprobación.

CAMINOS = {"A": [Point(0, 0), Point(2, 1), Point(4, 0)],
           "B": [Point(6, 0), Point(8, 2), Point(10, 0), Point(6, 0)],
           "C": [Point(0, 4), Point(3, 6), Point(6, 4), Point(3, 2), Point(0, 4)],
           "D": [Point(8, 4), Point(10, 6), Point(12, 4)]}


def cerrada(camino):
    return camino[0] == camino[-1]


@ejercicio(id="lineas-3-010", tipo="conceptual", dificultad=1, fuente=FUENTE,
           enunciado=r"Rinrín dejó cuatro caminos en la arena: $A$, $B$, $C$ y $D$. Mira el "
                     r"dibujo y escribe al lado de cada letra si el camino es \emph{abierto} o "
                     r"\emph{cerrado}. Acuérdate: es cerrado si terminas donde empezaste sin "
                     r"levantar el lápiz.",
           respuesta=r"$A$: abierto. $B$: cerrado. $C$: cerrado. $D$: abierto.",
           notas="Dibujo: A (0,0)-(2,1)-(4,0); B (6,0)-(8,2)-(10,0)-(6,0); "
                 "C (0,4)-(3,6)-(6,4)-(3,2)-(0,4); D (8,4)-(10,6)-(12,4).",
           **COMUN)
def _():
    assert [cerrada(CAMINOS[k]) for k in ("A", "B", "C", "D")] == [False, True, True, False]


@ejercicio(id="lineas-3-011", tipo="conceptual", dificultad=2, fuente=FUENTE,
           enunciado=r"El camino $C$ del dibujo es cerrado. Mamá Rana está en el punto "
                     r"$(3, 4)$, una hormiga en el punto $(7, 5)$ y una piedrita justo en el "
                     r"punto $(3, 6)$. ¿Quién está dentro del camino, quién está fuera y quién "
                     r"está en el borde?",
           respuesta=r"Mamá Rana está \emph{dentro}, la hormiga está \emph{fuera} y la piedrita "
                     r"está \emph{en el borde}. Una línea cerrada siempre parte el papel en tres "
                     r"partes: lo de dentro, lo de fuera y la línea misma.",
           notas="Dibujo: el mismo camino C del ejercicio anterior, con los tres puntos marcados.",
           **COMUN)
def _():
    C = Polygon(*CAMINOS["C"][:-1])
    def lugar(p):
        if any(l.contains(p) for l in C.sides):
            return "borde"
        return "dentro" if C.encloses_point(p) else "fuera"
    assert lugar(Point(3, 4)) == "dentro"
    assert lugar(Point(7, 5)) == "fuera"
    assert lugar(Point(3, 6)) == "borde"


@ejercicio(id="lineas-3-012", tipo="conceptual", dificultad=2, fuente=FUENTE,
           enunciado=r"Rinrín dice: «Mi camino $A$ es cerrado, porque el papel se acabó y no "
                     r"pude seguir». ¿Tiene razón? Explícale con tus palabras qué le falta al "
                     r"camino $A$ para ser cerrado.",
           respuesta=r"No tiene razón. Que el papel se acabe no cierra un camino. Al camino $A$ "
                     r"le falta volver hasta donde empezó: si desde el final $(4, 0)$ dibuja una "
                     r"línea hasta el comienzo $(0, 0)$, entonces sí queda cerrado y ya se puede "
                     r"decir qué está dentro y qué está fuera.",
           **COMUN)
def _():
    A = CAMINOS["A"]
    assert not cerrada(A)
    assert cerrada(A + [A[0]])
