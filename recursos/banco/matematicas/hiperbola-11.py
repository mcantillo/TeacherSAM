"""Banco de ejercicios — Geometría 11° — La hipérbola (guía del trimestre I, 2026-09-15).
DBA 6 de 11°. Excepción a «solo banco»: el banco no tenía NINGÚN ejercicio de hipérbola (ni hay
recurso de cónicas en recursos/). Solo los dos mínimos para el tema. La hipérbola se presenta
completa desde su definición porque no se puede suponer vista en 10° (decisión pendiente).
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/hiperbola-11.py
"""
from sympy import Abs, simplify, sqrt
from sympy.geometry import Point

from ejercicios import ejercicio

PROPIO = "propio (guía Geometría 11°, trimestre I)"
COMUN = dict(tema="la hipérbola", grados=[11], dba=["matematicas-11-6"], fuente=PROPIO)


def en_hiperbola(P, f1, f2, dos_a):
    return simplify(Abs(P.distance(f1) - P.distance(f2)) - dos_a) == 0


@ejercicio(id="hiperbola-11-002", tipo="calculo", dificultad=1,
           enunciado=r"Para la hipérbola $\frac{x^2}{16} - \frac{y^2}{9} = 1$ halla $a$, $b$, $c$, "
                     r"los vértices, los focos y las asíntotas.",
           respuesta=r"$a = 4$, $b = 3$, $c = \sqrt{16 + 9} = 5$. Vértices $(\pm 4, 0)$, focos "
                     r"$(\pm 5, 0)$, asíntotas $y = \pm \frac{3}{4}x$.", **COMUN)
def _():
    a, b = 4, 3
    c = sqrt(a**2 + b**2)
    assert c == 5
    assert en_hiperbola(Point(4, 0), Point(-5, 0), Point(5, 0), 2 * a)
    assert en_hiperbola(Point(8, sqrt(27)), Point(-5, 0), Point(5, 0), 8)   # 64/16 − 27/9 = 1


@ejercicio(id="hiperbola-11-004", tipo="encuentra-el-error", dificultad=2,
           enunciado=r"Laura tiene la hipérbola $\frac{x^2}{16} - \frac{y^2}{9} = 1$ y calcula sus "
                     r"focos así: «$c^2 = a^2 - b^2 = 16 - 9 = 7$, así que los focos son "
                     r"$(\pm\sqrt{7}, 0)$». ¿Cuál es el error? Muestra que el punto $(4, 0)$ no cumple "
                     r"la definición con esos focos.",
           respuesta=r"Usó la relación de la elipse. En la hipérbola $c^2 = a^2 + b^2 = 25$, así que "
                     r"los focos son $(\pm 5, 0)$. Con focos $(\pm\sqrt{7}, 0)$, el vértice $(4, 0)$ "
                     r"daría $(4 + \sqrt{7}) - (4 - \sqrt{7}) = 2\sqrt{7} \approx \num{5,29}$, y no "
                     r"$2a = 8$.", **COMUN)
def _():
    V = Point(4, 0)
    assert not en_hiperbola(V, Point(-sqrt(7), 0), Point(sqrt(7), 0), 8)
    assert en_hiperbola(V, Point(-5, 0), Point(5, 0), 8)
