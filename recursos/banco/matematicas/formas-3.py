"""Banco de ejercicios — Matemáticas (Geometría 3°) — Formas a mi alrededor: reconocer un
cuerpo por sus caras; describir un cuerpo sin dibujarlo (ejemplo del DBA 6 de 3°).
Fuente: ejercicios propios para la guía del trimestre I de Geometría 3° (hilo: Rinrín Renacuajo
sale de paseo) y el ejemplo del DBA 6 de grado 3 (dba/matematicas/grados/grado03.tex: la
profesora con un prisma rectangular, un prisma triangular y un cilindro). El banco no tenía
ningún ejercicio de 3° (excepción aprobada por la docente el 2026-09-15). El manual formas-3-003
es el ejemplo del propio DBA (lo pide el DBA y no había ninguno).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/formas-3.py
"""
from itertools import combinations

from sympy import Matrix

from ejercicios import ejercicio, ejercicio_manual

FUENTE = "propio — guía Geometría 3°, trimestre I, tema Formas a mi alrededor"
FUENTE_DBA = "ejemplo del DBA 6 de grado 3 (MEN 2016), adaptado"
COMUN = dict(tema="formas a mi alrededor", grados=[3], dba=["matematicas-3-6"])

CUERPOS = {
    "cubo": [(x, y, z) for x in (0, 2) for y in (0, 2) for z in (0, 2)],
    "caja": [(x, y, z) for x in (0, 3) for y in (0, 2) for z in (0, 1)],
    "pirámide": [(0, 0, 0), (2, 0, 0), (2, 2, 0), (0, 2, 0), (1, 1, 2)],
    "prisma triangular": [(x, y, z) for (x, y) in ((0, 0), (2, 0), (1, 2)) for z in (0, 3)],
}


def caras(pts):
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


def es_cuadrado(pts, cara):
    q = [pts[i] for i in cara]
    d = sorted(sum((a[k] - b[k]) ** 2 for k in range(3)) for a, b in combinations(q, 2))
    return len(q) == 4 and d[0] == d[3] and d[4] == d[5] == 2 * d[0]


def ficha(nombre):
    pts = CUERPOS[nombre]
    F = caras(pts)
    return dict(caras=len(F), vertices=len(pts),
                triangulos=sum(len(f) == 3 for f in F),
                cuadrilateros=sum(len(f) == 4 for f in F),
                cuadrados=sum(es_cuadrado(pts, f) for f in F))


ADIVINANZAS = [
    ("Tengo 6 caras y todas son cuadrados iguales.", "cubo",
     lambda f: f["caras"] == 6 and f["cuadrados"] == 6),
    ("Tengo 5 caras: 2 son triángulos y 3 son rectángulos.", "prisma triangular",
     lambda f: f["caras"] == 5 and f["triangulos"] == 2 and f["cuadrilateros"] == 3),
    ("Tengo 5 caras y 5 vértices; una cara es un cuadrado y las otras son triángulos.",
     "pirámide", lambda f: f["caras"] == 5 and f["vertices"] == 5 and f["cuadrados"] == 1
     and f["triangulos"] == 4),
]


@ejercicio(id="formas-3-001", tipo="conceptual", dificultad=2, fuente=FUENTE,
           enunciado=r"Adivina, adivinador: ¿qué cuerpo soy? Elige entre el cubo, la caja, la "
                     r"pirámide y el prisma triangular. "
                     r"a) «" + ADIVINANZAS[0][0] + "» "
                     r"b) «" + ADIVINANZAS[1][0] + "» "
                     r"c) «" + ADIVINANZAS[2][0] + "»",
           respuesta=r"a) el cubo; b) el prisma triangular; c) la pirámide.",
           **COMUN)
def _():
    for _texto, esperado, cumple in ADIVINANZAS:
        quienes = [k for k in CUERPOS if cumple(ficha(k))]
        assert quienes == [esperado], (esperado, quienes)


ejercicio_manual(id="formas-3-003", tipo="argumentacion", dificultad=3, fuente=FUENTE_DBA,
                 enunciado=r"David y María faltaron a clase y no vieron los cuerpos que tenía la "
                           r"profesora: una caja, un prisma triangular y un cilindro. Escríbeles "
                           r"un mensaje, sin dibujos, para que puedan construirlos en cartulina "
                           r"iguales a los de la profesora.",
                 respuesta=r"Respuesta abierta. Un buen mensaje dice, para cada cuerpo, cuántas "
                           r"caras tiene, qué figura es cada cara y de qué tamaño. Por ejemplo: "
                           r"«La caja tiene 6 caras rectangulares: 2 de 10 por 5 cm, 2 de 10 por 3 "
                           r"cm y 2 de 5 por 3 cm. El prisma tiene 2 triángulos iguales y 3 "
                           r"rectángulos. El cilindro tiene 2 círculos iguales y una parte curva "
                           r"que se hace enrollando un rectángulo». Se valora que nombre las "
                           r"figuras de las caras y que diga las medidas.", **COMUN)
