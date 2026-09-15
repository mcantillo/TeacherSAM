"""Banco de ejercicios — Geometría 11° — Lugares geométricos: circunferencia y mediatriz (guía del trimestre I, 2026-09-14).
DBA 6 de 11°. Ejercicios propios. Rapidez de las ondas de radio: se toma c ≈ 300 000 km/s
= 0,3 km/µs (valor exacto en el vacío: 299 792 458 m/s, NIST).
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/lugares-geometricos-11.py
"""
from sympy import Rational, expand, simplify, symbols
from sympy.geometry import Circle, Line, Point

from ejercicios import ejercicio

PROPIO = "propio (guía Geometría 11°, trimestre I)"
COMUN = dict(tema="lugares geométricos: circunferencia y mediatriz", grados=[11],
             dba=["matematicas-11-6"], fuente=PROPIO)
x, y = symbols("x y", real=True)


@ejercicio(id="lugares-geometricos-11-001", tipo="calculo", dificultad=1,
           enunciado=r"Escribe la ecuación de la circunferencia de centro $(3, -2)$ y radio $5$. "
                     r"¿El punto $(6, 2)$ está sobre ella?",
           respuesta=r"$(x - 3)^2 + (y + 2)^2 = 25$. Sí: $(6 - 3)^2 + (2 + 2)^2 = 9 + 16 = 25$.",
           **COMUN)
def _():
    c = Circle(Point(3, -2), 5)
    assert simplify(c.equation(x, y) - ((x - 3)**2 + (y + 2)**2 - 25)) == 0
    assert c.encloses_point(Point(6, 2)) is False and Point(3, -2).distance(Point(6, 2)) == 5


@ejercicio(id="lugares-geometricos-11-002", tipo="calculo", dificultad=2,
           enunciado=r"Completa cuadrados para hallar el centro y el radio de "
                     r"$x^2 + y^2 - 6x + 4y - 12 = 0$.",
           respuesta=r"$(x^2 - 6x + 9) + (y^2 + 4y + 4) = 12 + 9 + 4$, es decir, "
                     r"$(x - 3)^2 + (y + 2)^2 = 25$: centro $(3, -2)$ y radio $5$.", **COMUN)
def _():
    assert expand((x - 3)**2 + (y + 2)**2 - 25) == x**2 + y**2 - 6 * x + 4 * y - 12


@ejercicio(id="lugares-geometricos-11-003", tipo="contexto", dificultad=2,
           enunciado=r"Una estación en el origen emite un pulso de radio que tarda $200$~µs en llegar "
                     r"a un barco. Las ondas de radio viajan a unos $\num{0,3}$~km/µs. a) ¿A qué "
                     r"distancia está el barco? b) ¿Dónde puede estar? Escribe la ecuación. c) ¿Por qué "
                     r"una sola estación no basta para saber la posición?",
           respuesta=r"a) $\num{0,3} \cdot 200 = 60$~km. b) En cualquier punto de la circunferencia "
                     r"$x^2 + y^2 = 3\,600$ (en km). c) Todos los puntos de esa circunferencia están a "
                     r"$60$~km: hace falta otra medición para escoger uno.", **COMUN)
def _():
    d = Rational("0.3") * 200
    assert d == 60 and d**2 == 3600


@ejercicio(id="lugares-geometricos-11-004", tipo="calculo", dificultad=2,
           enunciado=r"Dos estaciones están en $A(0, 0)$ y $B(8, 4)$. Halla la ecuación de la "
                     r"mediatriz de $AB$ (los puntos a igual distancia de las dos) y comprueba que "
                     r"$(5, 0)$ está a igual distancia de $A$ y de $B$.",
           respuesta=r"Punto medio $(4, 2)$; la pendiente de $AB$ es $\frac{1}{2}$, así que la "
                     r"mediatriz tiene pendiente $-2$: $y = -2x + 10$. El punto $(5, 0)$ la cumple, y "
                     r"$d(A) = 5$, $d(B) = \sqrt{9 + 16} = 5$.", **COMUN)
def _():
    A, B = Point(0, 0), Point(8, 4)
    m = Line(A, B).perpendicular_line(A.midpoint(B))
    assert simplify(m.equation(x, y).subs(y, -2 * x + 10)) == 0
    P = Point(5, 0)
    assert P in m and A.distance(P) == B.distance(P) == 5


@ejercicio(id="lugares-geometricos-11-005", tipo="encuentra-el-error", dificultad=2,
           enunciado=r"Pedro dice: «Los puntos que están a igual distancia de $A(1, 2)$ y $B(5, 2)$ "
                     r"forman la circunferencia de centro $(3, 2)$ que pasa por $A$ y $B$». Da un punto "
                     r"de esa circunferencia que no esté a igual distancia de $A$ y $B$, y escribe el "
                     r"lugar geométrico correcto.",
           respuesta=r"La circunferencia es $(x - 3)^2 + (y - 2)^2 = 4$; su punto $(1, 2) = A$ está a "
                     r"distancia $0$ de $A$ y $4$ de $B$. El lugar correcto es la mediatriz: la recta "
                     r"$x = 3$ (por ejemplo, $(3, 7)$ está a $\sqrt{29}$ de los dos).", **COMUN)
def _():
    A, B = Point(1, 2), Point(5, 2)
    assert A.distance(Point(3, 2)) == 2 and A.distance(A) != B.distance(A)
    Q = Point(3, 7)
    assert A.distance(Q) == B.distance(Q) == (29)**Rational(1, 2)
    t = symbols("t", real=True)
    assert simplify(A.distance(Point(3, t)) - B.distance(Point(3, t))) == 0
