"""Banco de ejercicios — Geometría 8° — Teorema de Pitágoras (ternas y lado desconocido).
Fuente: módulo de Geometría de las Guías de Apoyo (Adriana Quintero Palomino), Tema 3; se lee en
recursos/matematicas/Guías pedagógicas Matemáticas/markdown/Modulo_Matematicas_Geometria.md
DBA 7 de 8°: «Aplica el teorema de Pitágoras para calcular la medida de cualquier lado de un
triángulo rectángulo». Los problemas 3–8 (diagonales, medición) están en pitagoras-9.py.
En el banco no había ejercicios de este tema: nada duplicado.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/pitagoras-8.py
"""
from sympy import Integer, latex, sqrt

from ejercicios import ejercicio

FUENTE = ("módulo de Geometría (Quintero Palomino), Tema 3: Teorema de Pitágoras — "
          "Practica lo aprendido")
COMUN = dict(tema="teorema de Pitágoras", grados=[8], dba=["matematicas-8-7"])

# 1. ¿Pueden a, b (catetos) y c (hipotenusa) ser los lados de un triángulo rectángulo?
#    (n, literal, a, b, c, respuesta escrita a mano: True = sí)
TERNAS = [
    (1, "a", 3, 4, 5, True), (2, "b", 8, 6, 10, True), (3, "c", 5, 12, 13, True),
    (4, "d", 15, 8, 17, True), (5, "e", 12, 16, 20, True), (6, "f", 7, 24, 25, True),
    (7, "g", 24, 10, 26, True), (8, "h", 21, 20, 29, True), (9, "i", 16, 30, 34, True),
    (10, "j", 9, 40, 41, True), (11, "k", 35, 12, 37, True), (12, "l", 32, 24, 40, True),
    (13, "m", 27, 36, 45, True), (14, "n", 20, 48, 52, True), (15, "o", 11, 60, 61, True),
    (16, "p", 48, 14, 50, True), (17, "q", 45, 28, 53, True), (18, "r", 40, 42, 58, True),
    (19, "s", 33, 56, 65, True), (20, "t", 24, 70, 74, True), (21, "u", 13, 84, 85, True),
    (22, "v", 63, 16, 65, True), (23, "w", 60, 32, 68, True), (24, "x", 55, 48, 73, True),
    (25, "y", 48, 64, 80, True),
]
for n, literal, a, b, c, si in TERNAS:
    cuenta = f"${a}^2 + {b}^2 = {a * a} + {b * b} = {a * a + b * b}$ y ${c}^2 = {c * c}$"
    veredicto = "Sí" if si else "No"

    @ejercicio(id=f"pitagoras-8-{n:03d}", tipo="calculo", dificultad=1,
               fuente=f"{FUENTE} 1{literal}",
               enunciado=f"¿Pueden las longitudes $a = {a}$, $b = {b}$ (catetos) y $c = {c}$ "
                         f"(hipotenusa) ser los lados de un triángulo rectángulo?",
               respuesta=f"{veredicto}: {cuenta}.", **COMUN)
    def _(a=a, b=b, c=c, si=si):
        assert c > a and c > b and a + b > c                  # triángulo posible
        assert (Integer(a)**2 + Integer(b)**2 == Integer(c)**2) == si


# 2. Lado desconocido: (n, literal, dato 1, dato 2, qué se busca, respuesta a mano, notas)
#    «cc» = dos catetos → hipotenusa; «ch» = cateto e hipotenusa → otro cateto.
NOTA2 = ("En el módulo el punto 2 empieza con «¿Cuáles de las siguientes longitudes pueden "
         "corresponder a los lados de un triángulo rectángulo?», que no corresponde a los "
         "literales (piden el lado que falta); se reescribió la instrucción.")
LADOS = [
    (26, "a", 7, sqrt(53), "ch", Integer(2), None),
    (27, "b", 11, sqrt(265), "ch", Integer(12), None),
    (28, "c", 10, 9, "cc", sqrt(181), None),
    (29, "d", 4, 7, "cc", sqrt(65), None),
    (30, "e", 7, sqrt(170), "ch", Integer(11), None),
    (31, "f", 7, 3, "cc", sqrt(58), None),
    (32, "g", 13, 3, "cc", sqrt(178), None),
    (33, "h", 13, 7, "cc", sqrt(218), None),
    (34, "i", 2, 3, "cc", sqrt(13), None),
    (35, "j", 1, sqrt(5), "ch", Integer(2), None),
    (36, "k", 12, 5, "cc", Integer(13), None),
    (37, "l", 9, sqrt(106), "ch", Integer(5), None),
    (38, "m", 11, sqrt(122), "ch", Integer(1), None),
    (39, "n", 9, sqrt(225), "ch", Integer(12),
     "La hipotenusa impresa es √225 (= 15); el texto alternativo de la fórmula dice «raíz "
     "cuadrada de 255», con la que el cateto sería √174. Se dejó la impresa."),
    (40, "o", 2, sqrt(29), "ch", Integer(5), None),
    (41, "p", 6, sqrt(72), "ch", Integer(6), None),
    (42, "q", 3, sqrt(109), "ch", Integer(10), None),
    (43, "r", 2, sqrt(8), "ch", Integer(2), None),
    (44, "s", 1, 11, "cc", sqrt(122), None),
    (45, "t", 3, sqrt(10), "ch", Integer(1), None),
]
for n, literal, d1, d2, caso, sol, notas in LADOS:
    if caso == "cc":
        texto = (f"En un triángulo rectángulo los catetos miden ${latex(d1)}$ y ${latex(d2)}$. "
                 f"Halla la longitud de la hipotenusa.")
    else:
        texto = (f"En un triángulo rectángulo un cateto mide ${latex(d1)}$ y la hipotenusa mide "
                 f"${latex(d2)}$. Halla la longitud del otro cateto.")
    nota = NOTA2 + (" " + notas if notas else "")

    @ejercicio(id=f"pitagoras-8-{n:03d}", tipo="calculo", dificultad=1 if caso == "cc" else 2,
               fuente=f"{FUENTE} 2{literal}", enunciado=texto,
               respuesta=f"${latex(sol)}$.", notas=nota, **COMUN)
    def _(d1=d1, d2=d2, caso=caso, sol=sol):
        d1, d2 = Integer(1) * d1, Integer(1) * d2
        if caso == "cc":
            assert sqrt(d1**2 + d2**2) == sol
        else:
            assert d2 > d1                                  # la hipotenusa es el lado mayor
            assert sqrt(d2**2 - d1**2) == sol
            assert sol**2 + d1**2 == d2**2
