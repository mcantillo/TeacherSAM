"""Banco de ejercicios — Matemáticas (Geometría 7°) — El ángulo como medida de giro.
Escrito para la guía de Geometría 7°, trimestre I («Escher: el arte de mover figuras»), tema
«Ángulos y giros» (prepara la rotación del DBA 5 de grado 7). El banco no tenía nada para este
tema; regla de la docente del 2026-09-15: solo lo mínimo que falta.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/angulos-7.py
"""
from sympy import Matrix, cos, rad, sin

from ejercicios import ejercicio


def rot(grados):
    t = rad(grados)
    return Matrix([[cos(t), -sin(t)], [sin(t), cos(t)]])


@ejercicio(id="angulos-7-003", tema="ángulos y giros", grados=[7], dba=["matematicas-7-5"],
           tipo="argumentacion", dificultad=2, fuente="propio (guía Geometría 7°, trimestre I)",
           enunciado=r"Laura dice que girar una figura $270^\circ$ en sentido antihorario la deja "
                     r"en la misma posición que girarla $90^\circ$ en sentido horario. ¿Tiene "
                     r"razón? Explica con la vuelta completa y compruébalo girando una escuadra.",
           respuesta=r"Sí: $270^\circ + 90^\circ = 360^\circ$, una vuelta completa. Girar "
                     r"$270^\circ$ en un sentido es quedarse a $90^\circ$ de completar la vuelta, "
                     r"que es lo mismo que girar $90^\circ$ en el sentido contrario.")
def _():
    assert rot(270) == rot(-90)
    assert rot(90) ** 4 == Matrix.eye(2)
