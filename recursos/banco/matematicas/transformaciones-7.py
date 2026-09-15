"""Banco de ejercicios — Matemáticas (Geometría 7°) — Transformaciones rígidas en el plano:
traslación, rotación, reflexión, composición y congruencia.
Escritos para la guía de Geometría 7°, trimestre I («Escher: el arte de mover figuras»), desde el
DBA 5 de grado 7. El banco no tenía ningún ejercicio de transformaciones (ningún grado); regla de
la docente del 2026-09-15: uno por tema, lo mínimo. Coordenadas con enteros (Matemáticas 7°).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/transformaciones-7.py
"""
from sympy import Line, Point, Polygon, pi, simplify

from ejercicios import ejercicio

FUENTE = "propio (guía Geometría 7°, trimestre I), desde el DBA 5 de grado 7"
COMUN = dict(grados=[7], dba=["matematicas-7-5"])
O = Point(0, 0)
EJE_X, EJE_Y = Line(O, Point(1, 0)), Line(O, Point(0, 1))


def lados(P):
    return sorted(simplify(s.length) for s in P.sides)


@ejercicio(id="transformaciones-7-001", tema="traslaciones", tipo="calculo", dificultad=1,
           fuente=FUENTE,
           enunciado=r"Traslada el triángulo de vértices $A(1, 1)$, $B(4, 1)$ y $C(2, 3)$ con el "
                     r"vector $\langle 3, 2 \rangle$ (3 unidades a la derecha y 2 hacia arriba). "
                     r"Escribe las coordenadas de $A'$, $B'$ y $C'$ y dibuja las dos figuras.",
           respuesta=r"$A'(4, 3)$, $B'(7, 3)$, $C'(5, 5)$.", **COMUN)
def _():
    T = [Point(1, 1), Point(4, 1), Point(2, 3)]
    assert [p.translate(3, 2) for p in T] == [Point(4, 3), Point(7, 3), Point(5, 5)]


@ejercicio(id="transformaciones-7-004", tema="rotaciones", tipo="calculo", dificultad=2,
           fuente=FUENTE,
           enunciado=r"Gira el punto $P(3, 1)$ alrededor del origen: a) $90^\circ$ en sentido "
                     r"antihorario; b) $180^\circ$; c) $90^\circ$ en sentido horario. Usa papel "
                     r"cuadriculado y una escuadra para comprobar cada giro.",
           respuesta=r"a) $(-1, 3)$; b) $(-3, -1)$; c) $(1, -3)$.", **COMUN)
def _():
    P = Point(3, 1)
    assert P.rotate(pi / 2) == Point(-1, 3)
    assert P.rotate(pi) == Point(-3, -1)
    assert P.rotate(-pi / 2) == Point(1, -3)


@ejercicio(id="transformaciones-7-009", tema="reflexiones", tipo="encuentra-el-error",
           dificultad=2, fuente=FUENTE,
           enunciado=r"Valentina afirma: «reflejar una figura respecto al eje $y$ es lo mismo que "
                     r"girarla $180^\circ$ alrededor del origen». Encuentra el error con el punto "
                     r"$(2, 3)$ y explica qué diferencia hay entre las dos figuras que se obtienen "
                     r"con una letra F.",
           respuesta=r"La reflexión da $(-2, 3)$ y el giro da $(-2, -3)$: no son iguales. Una "
                     r"reflexión invierte la figura (la F queda «al revés», como en un espejo); un "
                     r"giro solo la voltea sin invertirla (la F queda de cabeza, pero se puede "
                     r"leer girando la hoja).", **COMUN)
def _():
    A = Point(2, 3)
    assert A.reflect(EJE_Y) == Point(-2, 3) and A.rotate(pi) == Point(-2, -3)
    # orientación: la reflexión invierte el sentido de los vértices; la rotación no
    T = [Point(0, 0), Point(2, 0), Point(0, 1)]
    assert Polygon(*T).area > 0
    assert Polygon(*[p.reflect(EJE_Y) for p in T]).area < 0
    assert Polygon(*[p.rotate(pi) for p in T]).area > 0


@ejercicio(id="transformaciones-7-012", tema="transformaciones", tipo="conceptual", dificultad=2,
           fuente=FUENTE,
           enunciado=r"Aplica al triángulo $A(0, 0)$, $B(3, 0)$, $C(0, 2)$ un giro de $90^\circ$ "
                     r"antihorario alrededor del origen y luego una traslación con "
                     r"$\langle 5, 1 \rangle$. Halla la figura final y compara las longitudes de sus "
                     r"lados con las del triángulo original. ¿Son congruentes? ¿Por qué?",
           respuesta=r"Giro: $(0, 0)$, $(0, 3)$, $(-2, 0)$. Traslación: $A''(5, 1)$, $B''(5, 4)$, "
                     r"$C''(3, 1)$. Los lados miden 2, 3 y $\sqrt{13}$ en los dos triángulos: son "
                     r"congruentes, porque giros y traslaciones no cambian las medidas.", **COMUN)
def _():
    T = [Point(0, 0), Point(3, 0), Point(0, 2)]
    F = [p.rotate(pi / 2).translate(5, 1) for p in T]
    assert F == [Point(5, 1), Point(5, 4), Point(3, 1)]
    assert lados(Polygon(*F)) == lados(Polygon(*T))
