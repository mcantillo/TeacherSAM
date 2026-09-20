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


# --- Añadidos el 2026-09-20 para el taller de la sesión 004 (semana 04) --------------
# El 001 y el 003 los usa la guía. Estos cuatro sostienen el taller sin repetirlos; todos
# con coordenadas, para que el dibujo del taller y la comprobación digan lo mismo.

VIA = {"riel A": Line(Point(0, 0), Point(9, 0)), "riel B": Line(Point(0, 3), Point(9, 3)),
       "durmiente": Line(Point(2, -1), Point(2, 4)), "cruce": Line(Point(0, -1), Point(6, 5))}


@ejercicio(id="lineas-4-010", tipo="conceptual", dificultad=1, fuente=FUENTE,
           enunciado=r"En el dibujo de la vía del tren hay cuatro rectas: los dos rieles "
                     r"($A$ y $B$), un durmiente y el camino que cruza. Di si cada pareja es de "
                     r"rectas paralelas, perpendiculares o secantes no perpendiculares: "
                     r"riel $A$ y riel $B$; riel $A$ y durmiente; riel $B$ y durmiente; "
                     r"riel $A$ y cruce.",
           respuesta=r"Riel $A$ y riel $B$: paralelas (por eso el tren no se sale). "
                     r"Riel $A$ y durmiente: perpendiculares. Riel $B$ y durmiente: "
                     r"perpendiculares. Riel $A$ y cruce: secantes, porque se cortan pero no "
                     r"forman ángulo recto.",
           notas="Dibujo: riel A (0,0)–(9,0); riel B (0,3)–(9,3); durmiente (2,-1)–(2,4); "
                 "cruce (0,-1)–(6,5).",
           **COMUN)
def _():
    assert [relacion(VIA["riel A"], VIA["riel B"]), relacion(VIA["riel A"], VIA["durmiente"]),
            relacion(VIA["riel B"], VIA["durmiente"]), relacion(VIA["riel A"], VIA["cruce"])] == \
        ["paralelas", "perpendiculares", "perpendiculares", "secantes"]


@ejercicio(id="lineas-4-011", tipo="conceptual", dificultad=1, fuente=FUENTE,
           enunciado=r"Los dos rieles son paralelos y el durmiente es perpendicular al riel $A$. "
                     r"Sin mirar el dibujo, ¿el durmiente es perpendicular también al riel $B$? "
                     r"Explica por qué.",
           respuesta=r"Sí. Si dos rectas son paralelas, van en la misma dirección; una recta que "
                     r"forma ángulo recto con una de ellas forma el mismo ángulo recto con la "
                     r"otra. Por eso los durmientes quedan bien puestos con los dos rieles a la "
                     r"vez.",
           **COMUN)
def _():
    assert VIA["riel A"].is_parallel(VIA["riel B"])
    assert VIA["durmiente"].is_perpendicular(VIA["riel A"])
    assert VIA["durmiente"].is_perpendicular(VIA["riel B"])


@ejercicio(id="lineas-4-012", tipo="calculo", dificultad=2, fuente=FUENTE,
           enunciado=r"Con la regla y la escuadra, traza en tu cuaderno: a) una recta paralela "
                     r"al riel $A$ que pase por el punto $(1, 5)$; b) una recta perpendicular al "
                     r"riel $A$ que pase por el punto $(7, 1)$. Después di por qué punto del "
                     r"riel $A$ pasa la recta de la parte b).",
           respuesta=r"a) Una recta horizontal por $(1, 5)$: pasa también por $(9, 5)$, por "
                     r"ejemplo. b) Una recta vertical por $(7, 1)$; corta al riel $A$ en el "
                     r"punto $(7, 0)$. Al ser perpendicular, lo corta «en la esquina», formando "
                     r"cuatro ángulos rectos.",
           notas="Mismo dibujo del 010.",
           **COMUN)
def _():
    A = VIA["riel A"]
    par = A.parallel_line(Point(1, 5))
    per = A.perpendicular_line(Point(7, 1))
    assert par.is_parallel(A) and par.contains(Point(9, 5))
    assert per.is_perpendicular(A) and per.intersection(A) == [Point(7, 0)]


@ejercicio(id="lineas-4-013", tipo="conceptual", dificultad=2, fuente=FUENTE,
           enunciado=r"Fogg dibuja un cuadrilátero con vértices $P(0, 0)$, $Q(6, 0)$, "
                     r"$R(6, 4)$ y $S(0, 4)$. ¿Qué parejas de lados son paralelas? ¿Qué parejas "
                     r"son perpendiculares? ¿Cómo se llama esa figura?",
           respuesta=r"$PQ$ es paralelo a $SR$, y $QR$ es paralelo a $PS$. Cada lado horizontal "
                     r"es perpendicular a cada lado vertical. Como tiene los cuatro ángulos "
                     r"rectos y los lados opuestos iguales, es un \textbf{rectángulo}.",
           notas="Se retoma en el tema 3 (cuadriláteros).",
           **COMUN)
def _():
    P, Q, R, S = Point(0, 0), Point(6, 0), Point(6, 4), Point(0, 4)
    PQ, QR, SR, PS = Line(P, Q), Line(Q, R), Line(S, R), Line(P, S)
    assert PQ.is_parallel(SR) and QR.is_parallel(PS)
    assert PQ.is_perpendicular(QR) and SR.is_perpendicular(PS)
