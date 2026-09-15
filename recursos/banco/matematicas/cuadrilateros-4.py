"""Banco de ejercicios — Matemáticas (Geometría 4°) — Cuadriláteros: cuadrado, rectángulo,
rombo y trapecio según sus lados iguales, sus lados paralelos y sus ángulos rectos.
Fuente: ejercicios propios para la guía del trimestre I de Geometría 4° (hilo: La vuelta al
mundo en 80 días). El banco no tenía ningún ejercicio de 4° ni de clasificación de
cuadriláteros en grados vecinos (excepción aprobada por la docente el 2026-09-15). La
clasificación se calcula desde las coordenadas.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/cuadrilateros-4.py
"""
from sympy import Polygon, pi

from ejercicios import ejercicio

FUENTE = "propio — guía Geometría 4°, trimestre I, tema Cuadriláteros"
COMUN = dict(tema="cuadriláteros", grados=[4], dba=["matematicas-4-6"])


def propiedades(p):
    v = p.vertices
    lados = [v[(i + 1) % 4] - v[i] for i in range(4)]
    iguales = len({s.length for s in p.sides}) == 1
    rectos = all(a == pi / 2 for a in p.angles.values())
    par = sum(1 for i in (0, 1) if lados[i].x * lados[i + 2].y - lados[i].y * lados[i + 2].x == 0)
    return dict(iguales=iguales, rectos=rectos, pares_paralelos=par)


def clase(p):
    f = propiedades(p)
    if f["pares_paralelos"] == 2:
        if f["iguales"] and f["rectos"]:
            return "cuadrado"
        if f["rectos"]:
            return "rectángulo"
        if f["iguales"]:
            return "rombo"
        return "paralelogramo"
    return "trapecio" if f["pares_paralelos"] == 1 else "trapezoide"


FIG = {"A": Polygon((0, 0), (3, 0), (3, 3), (0, 3)),
       "B": Polygon((0, 0), (5, 0), (5, 2), (0, 2)),
       "C": Polygon((2, 0), (4, 3), (2, 6), (0, 3)),
       "D": Polygon((0, 0), (6, 0), (4, 3), (1, 3)),
       "E": Polygon((0, 0), (4, 0), (5, 3), (1, 4))}


@ejercicio(id="cuadrilateros-4-001", tipo="conceptual", dificultad=2, fuente=FUENTE,
           enunciado=r"Los cinco cuadriláteros del dibujo están en una cuadrícula. Con la regla "
                     r"y la escuadra, revisa sus lados y sus ángulos y escribe el nombre de cada "
                     r"uno: cuadrado, rectángulo, rombo, trapecio o ninguno de ellos.",
           respuesta=r"A: cuadrado. B: rectángulo. C: rombo. D: trapecio. E: ninguno (no tiene "
                     r"lados paralelos; se llama trapezoide).",
           notas="Dibujo: coordenadas de FIG.",
           **COMUN)
def _():
    assert {k: clase(p) for k, p in FIG.items()} == {
        "A": "cuadrado", "B": "rectángulo", "C": "rombo", "D": "trapecio", "E": "trapezoide"}


@ejercicio(id="cuadrilateros-4-003", tipo="argumentacion", dificultad=3, fuente=FUENTE,
           enunciado=r"Responde y explica: a) ¿Un cuadrado es también un rectángulo? b) ¿Todo "
                     r"rombo es un cuadrado?",
           respuesta=r"a) Sí: el rectángulo es el cuadrilátero con 4 ángulos rectos, y el "
                     r"cuadrado los tiene; es un rectángulo con los 4 lados iguales. b) No: el "
                     r"rombo tiene los 4 lados iguales, pero sus ángulos no tienen que ser "
                     r"rectos, como el rombo C del dibujo.",
           **COMUN)
def _():
    cuadrado = propiedades(FIG["A"])
    assert cuadrado["rectos"] and cuadrado["pares_paralelos"] == 2        # cumple lo del rectángulo
    rombo = propiedades(FIG["C"])
    assert rombo["iguales"] and not rombo["rectos"]                       # contraejemplo
