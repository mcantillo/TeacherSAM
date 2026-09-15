"""Banco de ejercicios — Matemáticas (Geometría 4°) — Líneas: rectas paralelas, secantes y
perpendiculares.
Fuente: ejercicios propios para la guía del trimestre I de Geometría 4° (hilo: La vuelta al
mundo en 80 días). El banco no tenía ningún ejercicio de 4° ni de este tema en grados vecinos
(excepción aprobada por la docente el 2026-09-15).
Nota de DBA: paralelas y perpendiculares no están nombradas en los DBA de 4° (son del DBA 7 de
2°); aquí se usan como base para describir figuras (DBA 6 de 4°), según plan-anual.md.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/lineas-4.py
"""
from sympy import Line, Point, Segment

from ejercicios import ejercicio

FUENTE = "propio — guía Geometría 4°, trimestre I, tema Líneas"
COMUN = dict(tema="líneas", grados=[4], dba=["matematicas-4-6"])


def relacion(l1, l2):
    if l1.is_parallel(l2):
        return "paralelas"
    return "perpendiculares" if l1.is_perpendicular(l2) else "secantes"


RECTAS = {"r": Line(Point(0, 0), Point(4, 0)), "s": Line(Point(0, 2), Point(4, 2)),
          "t": Line(Point(1, -1), Point(1, 3)), "u": Line(Point(2, -1), Point(5, 3))}


@ejercicio(id="lineas-4-001", tipo="conceptual", dificultad=1, fuente=FUENTE,
           enunciado=r"Observa las rectas $r$, $s$, $t$ y $u$ del dibujo. Escribe si cada pareja "
                     r"es de rectas paralelas, perpendiculares o secantes no perpendiculares: "
                     r"$r$ y $s$; $r$ y $t$; $s$ y $t$; $r$ y $u$.",
           respuesta=r"$r$ y $s$: paralelas. $r$ y $t$: perpendiculares. $s$ y $t$: "
                     r"perpendiculares. $r$ y $u$: secantes (se cortan, pero no forman ángulo "
                     r"recto).",
           notas="Dibujo: r por (0,0),(4,0); s por (0,2),(4,2); t por (1,-1),(1,3); u por (2,-1),(5,3).",
           **COMUN)
def _():
    R = RECTAS
    assert [relacion(R["r"], R["s"]), relacion(R["r"], R["t"]), relacion(R["s"], R["t"]),
            relacion(R["r"], R["u"])] == ["paralelas", "perpendiculares", "perpendiculares",
                                          "secantes"]


@ejercicio(id="lineas-4-003", tipo="encuentra-el-error", dificultad=2, fuente=FUENTE,
           enunciado=r"En el dibujo hay dos segmentos que no se tocan. Passepartout dice: «Como "
                     r"no se tocan, son paralelos». ¿Tiene razón? Prolonga los dos segmentos con "
                     r"tu regla y explica.",
           respuesta=r"No tiene razón. Al prolongarlos, las dos rectas se cortan: son secantes. "
                     r"Dos rectas son paralelas solo si no se cortan aunque se prolonguen todo lo "
                     r"que se quiera.",
           notas="Dibujo: segmento (0,0)–(3,0) y segmento (5,1)–(7,3); sus rectas se cortan en (4,0).",
           **COMUN)
def _():
    s1, s2 = Segment(Point(0, 0), Point(3, 0)), Segment(Point(5, 1), Point(7, 3))
    assert s1.intersection(s2) == []
    assert Line(s1).intersection(Line(s2)) == [Point(4, 0)]
