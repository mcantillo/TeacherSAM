"""Banco de ejercicios — Matemáticas (Geometría 3°) — Cuerpos geométricos: caras, aristas y
vértices.
Fuente: ejercicios propios para la guía del trimestre I de Geometría 3° (hilo: Rinrín Renacuajo
sale de paseo). El banco no tenía ningún ejercicio de 3° ni de este tema en grados vecinos
(excepción aprobada por la docente el 2026-09-15).
Las caras, aristas y vértices se calculan desde las coordenadas de cada cuerpo (envolvente
convexa hecha a mano), no se copian de una tabla.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/cuerpos-geometricos-3.py
"""
from itertools import combinations

from sympy import Matrix

from ejercicios import ejercicio

FUENTE = "propio — guía Geometría 3°, trimestre I, tema Cuerpos geométricos"
COMUN = dict(tema="cuerpos geométricos", grados=[3], dba=["matematicas-3-6"])

CUERPOS = {
    "cubo": [(x, y, z) for x in (0, 2) for y in (0, 2) for z in (0, 2)],
    "caja": [(x, y, z) for x in (0, 3) for y in (0, 2) for z in (0, 1)],
    "pirámide": [(0, 0, 0), (2, 0, 0), (2, 2, 0), (0, 2, 0), (1, 1, 2)],
    "prisma triangular": [(x, y, z) for (x, y) in ((0, 0), (2, 0), (1, 2)) for z in (0, 3)],
}


def caras(pts):
    """Caras del poliedro convexo: conjuntos de vértices sobre un plano de apoyo."""
    P = [Matrix(p) for p in pts]
    res = set()
    for a, b, c in combinations(range(len(P)), 3):
        n = (P[b] - P[a]).cross(P[c] - P[a])
        if n == Matrix([0, 0, 0]):
            continue
        lados = [n.dot(q - P[a]) for q in P]
        if all(s >= 0 for s in lados) or all(s <= 0 for s in lados):
            res.add(frozenset(i for i, s in enumerate(lados) if s == 0))
    return res


def elementos(pts):
    F = caras(pts)
    aristas = {frozenset(e) for e in combinations(range(len(pts)), 2)
               if sum(1 for f in F if set(e) <= f) == 2}
    return len(F), len(aristas), len(pts)


@ejercicio(id="cuerpos-geometricos-3-001", tipo="calculo", dificultad=2, fuente=FUENTE,
           enunciado=r"Completa la tabla contando en cada cuerpo sus caras, sus aristas (los "
                     r"bordes donde se juntan dos caras) y sus vértices (las puntas): cubo, caja, "
                     r"pirámide de base cuadrada y prisma triangular.",
           respuesta=r"Cubo: 6 caras, 12 aristas, 8 vértices. Caja: 6, 12, 8. Pirámide: 5, 8, 5. "
                     r"Prisma triangular: 5, 9, 6.",
           **COMUN)
def _():
    r = {k: elementos(v) for k, v in CUERPOS.items()}
    assert r == {"cubo": (6, 12, 8), "caja": (6, 12, 8), "pirámide": (5, 8, 5),
                 "prisma triangular": (5, 9, 6)}
    assert all(c - a + v == 2 for c, a, v in r.values())   # fórmula de Euler: conteo coherente


@ejercicio(id="cuerpos-geometricos-3-003", tipo="encuentra-el-error", dificultad=2, fuente=FUENTE,
           enunciado=r"El Ratón dice: «El dado tiene 6 caras, así que también tiene 6 "
                     r"vértices». ¿Tiene razón? Cuenta en un dado de verdad.",
           respuesta=r"No. El dado (un cubo) tiene 6 caras pero 8 vértices: 4 arriba y 4 abajo.",
           **COMUN)
def _():
    c, a, v = elementos(CUERPOS["cubo"])
    assert c == 6 and v == 8 and v != c
