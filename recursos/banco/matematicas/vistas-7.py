"""Banco de ejercicios — Matemáticas (Geometría 7°) — Vistas de objetos y objetos transformados
(construcciones con cubos).
Escritos para la guía de Geometría 7°, trimestre I («Escher: el arte de mover figuras»), desde el
DBA 5 de grado 7. El banco no tenía nada de vistas (ningún grado); regla de la docente del
2026-09-15: uno por tema, lo mínimo.
Una construcción con cubos se describe con su «plano de alturas»: la vista superior en cuadrícula,
con el número de cubos apilados en cada casilla. Filas = de atrás hacia adelante; columnas = de
izquierda a derecha, vistas desde el frente.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/vistas-7.py
"""
from ejercicios import ejercicio

FUENTE = "propio (guía Geometría 7°, trimestre I), desde el DBA 5 de grado 7"
COMUN = dict(grados=[7], dba=["matematicas-7-5"])

PLANO = [[3, 1, 2],     # fila de atrás
         [2, 1, 1]]     # fila de adelante


def total(p):
    return sum(map(sum, p))


def frontal(p):
    """Altura de cada columna, de izquierda a derecha, vista desde el frente."""
    return [max(col) for col in zip(*p)]


def lateral_derecha(p):
    """Altura de cada fila vista desde la derecha, de adelante hacia atrás."""
    return [max(fila) for fila in reversed(p)]


def girar_horario(p):
    """Gira la construcción 90° en sentido horario vista desde arriba."""
    return [list(f) for f in zip(*reversed(p))]


@ejercicio(id="vistas-7-001", tema="vistas de un objeto", tipo="calculo", dificultad=2,
           fuente=FUENTE,
           enunciado=r"Este plano de alturas muestra una construcción vista desde arriba; cada "
                     r"número dice cuántos cubos hay apilados en esa casilla (la fila de abajo es "
                     r"la de adelante):\newline"
                     r"\begin{tabular}{|c|c|c|}\hline 3 & 1 & 2\\\hline 2 & 1 & 1\\\hline"
                     r"\end{tabular}\newline"
                     r"a) ¿Cuántos cubos tiene? b) Dibuja su vista frontal y su vista lateral "
                     r"derecha en papel cuadriculado, indicando la altura de cada columna.",
           respuesta=r"a) 10 cubos. b) Vista frontal, de izquierda a derecha: alturas 3, 1 y 2. "
                     r"Vista lateral derecha, de adelante hacia atrás: alturas 2 y 3.", **COMUN)
def _():
    assert total(PLANO) == 10
    assert frontal(PLANO) == [3, 1, 2]
    assert lateral_derecha(PLANO) == [2, 3]


@ejercicio(id="vistas-7-004", tema="objetos transformados", tipo="calculo", dificultad=2,
           fuente=FUENTE,
           enunciado=r"La construcción del plano de alturas\newline"
                     r"\begin{tabular}{|c|c|c|}\hline 3 & 1 & 2\\\hline 2 & 1 & 1\\\hline"
                     r"\end{tabular}\newline"
                     r"se gira $90^\circ$ en sentido horario sobre la mesa (vista desde arriba). "
                     r"Escribe el nuevo plano de alturas y la nueva vista frontal. ¿Cambió el "
                     r"número de cubos?",
           respuesta=r"Nuevo plano (3 filas y 2 columnas, de atrás hacia adelante): 2 3; 1 1; "
                     r"1 2. Vista frontal: alturas 2 y 3. Sigue teniendo 10 cubos: girar no "
                     r"cambia el objeto, solo su posición.", **COMUN)
def _():
    g = girar_horario(PLANO)
    assert g == [[2, 3], [1, 1], [1, 2]]
    assert frontal(g) == [2, 3] and total(g) == total(PLANO) == 10
