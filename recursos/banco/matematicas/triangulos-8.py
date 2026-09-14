"""Banco de ejercicios — Geometría 8° — Triángulos: ángulos, rectas notables y propiedades.
Fuente: módulo de Geometría de las Guías de Apoyo (Adriana Quintero Palomino), Tema 2; se lee en
recursos/matematicas/Guías pedagógicas Matemáticas/markdown/Modulo_Matematicas_Geometria.md
Literales 1a–n: falso o verdadero con argumento. La comprobación verifica el valor de verdad
(en general, con coordenadas o ángulos simbólicos, o con un contraejemplo); el argumento de la
respuesta es modelo. DBA 7 de 8° (propiedades de figuras a partir de teoremas).
Las secciones de congruencia y semejanza del módulo no traen ejercicios.
En el banco no había ejercicios de este tema: nada duplicado.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/triangulos-8.py
"""
from sympy import (Interval, Line, N, Point, Rational, S, Triangle, acos, cos, deg, pi, rad,
                   simplify, sin, solve, solveset, sqrt, symbols, tan)
from sympy.solvers.inequalities import reduce_rational_inequalities

from ejercicios import ejercicio

REC = "módulo de Geometría (Quintero Palomino), Tema 2: Triángulos"
FUENTE = f"{REC}, Definición y clasificación — Practica lo aprendido"
COMUN = dict(tema="triángulos", grados=[8], dba=["matematicas-8-7"])
VF = (r"Indica si la afirmación es verdadera o falsa y argumenta tu respuesta (las figuras "
      r"están en un plano): ")

a, h, t, d = symbols("a h t d", positive=True)
al, be = symbols("alpha beta", positive=True)


def angulo(u, v):
    """Ángulo entre dos vectores (Point) en radianes."""
    return acos(simplify(u.dot(v) / (u.distance(Point(0, 0)) * v.distance(Point(0, 0)))))


@ejercicio(id="triangulos-8-001", tipo="argumentacion", dificultad=1, fuente=f"{FUENTE} 1a",
           enunciado=VF + r"«La suma de las longitudes de dos lados de un triángulo puede ser mayor "
                          r"que el tercer lado».",
           respuesta=r"Verdadera; de hecho siempre lo es (desigualdad triangular): el camino recto "
                     r"entre dos vértices es más corto que el que pasa por el tercero. Por "
                     r"ejemplo, en el triángulo de lados $3$, $4$, $5$: $3 + 4 > 5$.", **COMUN)
def _():
    for pts in [((0, 0), (3, 0), (0, 4)), ((0, 0), (7, 0), (2, 1)), ((0, 0), (1, 0), (5, 9))]:
        l1, l2, l3 = (s.length for s in Triangle(*map(Point, pts)).sides)
        assert N(l1 + l2 - l3) > 0 and N(l2 + l3 - l1) > 0 and N(l1 + l3 - l2) > 0
    # con 1 + 2 = 3 (puntos alineados) no hay triángulo: SymPy devuelve un segmento
    assert not isinstance(Triangle(Point(0, 0), Point(1, 0), Point(3, 0)), Triangle)


@ejercicio(id="triangulos-8-002", tipo="argumentacion", dificultad=1, fuente=f"{FUENTE} 1b",
           enunciado=VF + r"«Ningún ángulo interno de un triángulo puede ser entrante».",
           respuesta=r"Verdadera: los tres ángulos internos suman $180^\circ$ y cada uno es "
                     r"positivo, así que cada uno mide menos de $180^\circ$; un ángulo entrante "
                     r"mide más de $180^\circ$.", **COMUN)
def _():
    gamma = 180 - al - be                  # con alpha, beta > 0
    assert (180 - gamma).is_positive       # gamma < 180


@ejercicio(id="triangulos-8-003", tipo="argumentacion", dificultad=2, fuente=f"{FUENTE} 1c",
           enunciado=VF + r"«Las bisectrices de dos ángulos adyacentes son mutuamente "
                          r"perpendiculares».",
           respuesta=r"Falsa en general: las bisectrices de dos ángulos adyacentes $\alpha$ y "
                     r"$\beta$ forman un ángulo de $\frac{\alpha + \beta}{2}$, que es $90^\circ$ "
                     r"solo si $\alpha + \beta = 180^\circ$. Contraejemplo: con $30^\circ$ y "
                     r"$40^\circ$ las bisectrices forman $35^\circ$. (La figura del módulo muestra "
                     r"el caso particular de ángulos adyacentes suplementarios.)", **COMUN)
def _():
    entre = lambda x, y: x / 2 + y / 2          # ángulo entre las dos bisectrices
    assert entre(30, 40) == 35
    assert solve(entre(al, be) - 90, be) == [180 - al]


@ejercicio(id="triangulos-8-004", tipo="argumentacion", dificultad=2, fuente=f"{FUENTE} 1d",
           enunciado=VF + r"«Las bisectrices de dos ángulos complementarios (adyacentes) son "
                          r"mutuamente perpendiculares».",
           respuesta=r"Falsa: si $\alpha + \beta = 90^\circ$, las bisectrices forman "
                     r"$\frac{\alpha}{2} + \frac{\beta}{2} = 45^\circ$, nunca $90^\circ$.",
           notas="Se añadió «(adyacentes)»: el ángulo entre bisectrices solo tiene sentido si "
                 "los ángulos comparten vértice y lado.", **COMUN)
def _():
    assert simplify(al / 2 + (90 - al) / 2) == Rational(45)


@ejercicio(id="triangulos-8-005", tipo="argumentacion", dificultad=2, fuente=f"{FUENTE} 1e",
           enunciado=VF + r"«Las bisectrices de dos ángulos suplementarios (adyacentes) son "
                          r"mutuamente perpendiculares».",
           respuesta=r"Verdadera: si $\alpha + \beta = 180^\circ$, las bisectrices forman "
                     r"$\frac{\alpha}{2} + \frac{\beta}{2} = 90^\circ$.",
           notas="Se añadió «(adyacentes)», como en el literal d.", **COMUN)
def _():
    assert simplify(al / 2 + (180 - al) / 2) == 90


@ejercicio(id="triangulos-8-006", tipo="argumentacion", dificultad=2, fuente=f"{FUENTE} 1f",
           enunciado=VF + r"«Si se dibuja una recta paralela a la base de un triángulo isósceles que "
                          r"pase por el vértice opuesto, esta formará dos ángulos de la misma "
                          r"medida con los lados del triángulo».",
           respuesta=r"Verdadera: cada uno de esos ángulos es alterno interno con uno de los "
                     r"ángulos de la base (paralelas cortadas por una secante), y los ángulos de "
                     r"la base de un triángulo isósceles son iguales.", **COMUN)
def _():
    A, B, C = Point(-a, 0), Point(a, 0), Point(0, h)
    izq = angulo(Point(-1, 0), A - C)                 # paralela hacia la izquierda y lado CA
    der = angulo(Point(1, 0), B - C)                  # paralela hacia la derecha y lado CB
    base = angulo(B - A, C - A)
    assert simplify(izq - der) == 0 and simplify(der - base) == 0


@ejercicio(id="triangulos-8-007", tipo="argumentacion", dificultad=1, fuente=f"{FUENTE} 1g",
           enunciado=VF + r"«Si la suma de dos ángulos internos de un triángulo es igual al tercer "
                          r"ángulo, entonces el triángulo es rectángulo».",
           respuesta=r"Verdadera: si $\alpha + \beta = \gamma$, como $\alpha + \beta + \gamma = "
                     r"180^\circ$, queda $2\gamma = 180^\circ$ y $\gamma = 90^\circ$.", **COMUN)
def _():
    g = symbols("g")
    assert solve([al + be - g, al + be + g - 180], [g, be])[g] == 90


@ejercicio(id="triangulos-8-008", tipo="argumentacion", dificultad=2, fuente=f"{FUENTE} 1h",
           enunciado=VF + r"«Si la mediana de la base de un triángulo es perpendicular a la base, "
                          r"entonces el triángulo es isósceles».",
           respuesta=r"Verdadera: esa mediana pasa por el punto medio de la base y es "
                     r"perpendicular a ella, así que es su mediatriz; el vértice opuesto está sobre "
                     r"la mediatriz y por eso equidista de los extremos de la base: los dos lados "
                     r"son iguales.", **COMUN)
def _():
    A, B, M = Point(-a, 0), Point(a, 0), Point(0, 0)
    x, y = symbols("x y", real=True)
    C = Point(x, y)
    (sol,) = solve((C - M).dot(B - A), [x], dict=True)   # CM ⟂ AB
    Cp = C.subs(sol)
    assert simplify(Cp.distance(A) - Cp.distance(B)) == 0


@ejercicio(id="triangulos-8-009", tipo="argumentacion", dificultad=2, fuente=f"{FUENTE} 1i",
           enunciado=VF + r"«Una de las medianas de un triángulo isósceles es perpendicular a la "
                          r"base».",
           respuesta=r"Verdadera: la mediana trazada desde el vértice opuesto a la base (el que "
                     r"une los dos lados iguales) es perpendicular a la base, porque ese vértice y "
                     r"el punto medio de la base equidistan de sus extremos. Las otras dos "
                     r"medianas, en general, no lo son.", **COMUN)
def _():
    A, B, C = Point(-a, 0), Point(a, 0), Point(0, h)
    M = Point(0, 0)                                    # punto medio de AB
    assert A.midpoint(B) == M and simplify((C - M).dot(B - A)) == 0
    A1, B1, C1 = Point(-1, 0), Point(1, 0), Point(0, 3)
    otra = C1.midpoint(B1) - A1                        # mediana desde A
    assert otra.dot(B1 - A1) != 0


@ejercicio(id="triangulos-8-010", tipo="argumentacion", dificultad=2, fuente=f"{FUENTE} 1j",
           enunciado=VF + r"«Cualquier triángulo rectángulo isósceles puede dividirse en otros dos "
                          r"triángulos rectángulos isósceles por medio de una recta».",
           respuesta=r"Verdadera: la altura trazada desde el vértice del ángulo recto cae en el "
                     r"punto medio $M$ de la hipotenusa y forma dos triángulos con un ángulo recto "
                     r"en $M$ y dos ángulos de $45^\circ$; cada uno es rectángulo e isósceles.",
           **COMUN)
def _():
    A, B, C = Point(0, 0), Point(t, 0), Point(0, t)   # ángulo recto en A
    M = B.midpoint(C)
    assert simplify((M - A).dot(C - B)) == 0           # AM es la altura
    assert simplify(M.distance(A) - M.distance(B)) == 0
    assert simplify(M.distance(A) - M.distance(C)) == 0


@ejercicio(id="triangulos-8-011", tipo="argumentacion", dificultad=2, fuente=f"{FUENTE} 1k",
           enunciado=VF + r"«Si la mediatriz de la base de un triángulo coincide con la bisectriz "
                          r"del ángulo del vértice opuesto a la base, entonces el triángulo es "
                          r"isósceles».",
           respuesta=r"Verdadera: la bisectriz pasa por el vértice opuesto; si coincide con la "
                     r"mediatriz de la base, ese vértice está en la mediatriz y equidista de los "
                     r"extremos de la base, así que los dos lados que llegan a él son iguales.",
           **COMUN)
def _():
    A, B = Point(-a, 0), Point(a, 0)
    C = Point(0, h)                                    # un punto cualquiera de la mediatriz x = 0
    assert simplify(C.distance(A) - C.distance(B)) == 0
    bis = (A - C) / C.distance(A) + (B - C) / C.distance(B)
    assert simplify(bis.x) == 0                        # la bisectriz es la recta x = 0


@ejercicio(id="triangulos-8-012", tipo="argumentacion", dificultad=3, fuente=f"{FUENTE} 1l",
           enunciado=VF + r"«Una perpendicular a la bisectriz de un ángulo forma un triángulo "
                          r"isósceles con los lados del ángulo».",
           respuesta=r"Verdadera: los dos triángulos que la bisectriz forma con esa perpendicular "
                     r"tienen un lado común (sobre la bisectriz), un ángulo recto y ángulos iguales "
                     r"en el vértice; son congruentes (criterio ángulo–lado–ángulo), así que los "
                     r"dos segmentos sobre los lados del ángulo son iguales.",
           notas="En el módulo: «La perpendicular a la bisectriz»; se escribe «Una "
                 "perpendicular» (cualquiera que corte los dos lados).", **COMUN)
def _():
    O = Point(0, 0)
    P, Q = Point(d, d * tan(t)), Point(d, -d * tan(t))    # lados a ±t, bisectriz = eje x
    assert simplify(O.distance(P) - O.distance(Q)) == 0


@ejercicio(id="triangulos-8-013", tipo="argumentacion", dificultad=1, fuente=f"{FUENTE} 1m",
           enunciado=VF + r"«Ningún triángulo puede tener más de un ángulo recto».",
           respuesta=r"Verdadera: dos ángulos rectos ya suman $180^\circ$ y el tercer ángulo "
                     r"tendría que medir $0^\circ$.", **COMUN)
def _():
    assert 180 - 90 - 90 == 0


@ejercicio(id="triangulos-8-014", tipo="argumentacion", dificultad=1, fuente=f"{FUENTE} 1n",
           enunciado=VF + r"«Ningún triángulo puede tener más de un ángulo obtuso».",
           respuesta=r"Verdadera: dos ángulos obtusos sumarían más de $180^\circ$, y los tres "
                     r"ángulos de un triángulo suman exactamente $180^\circ$.", **COMUN)
def _():
    x, y = symbols("x y", positive=True)
    assert (x + 90 + y + 90 - 180).is_positive       # ángulos 90 + x y 90 + y


# ---------- 2. Problemas ----------

F2 = f"{FUENTE} 2"


@ejercicio(id="triangulos-8-015", tipo="calculo", dificultad=1, fuente=f"{F2}a",
           enunciado=r"Los ángulos agudos de un triángulo rectángulo son tales que uno es el doble "
                     r"del otro. ¿Cuánto miden los tres ángulos internos?",
           respuesta=r"$x + 2x = 90^\circ$, así que miden $30^\circ$, $60^\circ$ y $90^\circ$.",
           **COMUN)
def _():
    x = symbols("x")
    (s,) = solve(x + 2 * x - 90, x)
    assert (s, 2 * s, 90) == (30, 60, 90) and s + 2 * s + 90 == 180


@ejercicio(id="triangulos-8-016", tipo="calculo", dificultad=1, fuente=f"{F2}b",
           enunciado=r"Los ángulos agudos de un triángulo rectángulo son iguales. ¿Cuánto miden los "
                     r"tres ángulos internos?",
           respuesta=r"$45^\circ$, $45^\circ$ y $90^\circ$.", **COMUN)
def _():
    x = symbols("x")
    assert solve(2 * x - 90, x) == [45]


@ejercicio(id="triangulos-8-017", tipo="calculo", dificultad=1, fuente=f"{F2}c",
           enunciado=r"El ángulo opuesto a la base de un triángulo isósceles mide $50^\circ$. "
                     r"¿Cuánto miden los otros dos ángulos internos?",
           respuesta=r"$\frac{180^\circ - 50^\circ}{2} = 65^\circ$ cada uno.", **COMUN)
def _():
    x = symbols("x")
    assert solve(50 + 2 * x - 180, x) == [65]


@ejercicio(id="triangulos-8-018", tipo="calculo", dificultad=2, fuente=f"{F2}d",
           enunciado=r"El ángulo opuesto a la base de un triángulo isósceles mide el doble de cada "
                     r"uno de los otros dos. ¿Cuánto miden los ángulos internos de ese triángulo?",
           respuesta=r"$x + x + 2x = 180^\circ$, así que $x = 45^\circ$: miden $45^\circ$, "
                     r"$45^\circ$ y $90^\circ$.", **COMUN)
def _():
    x = symbols("x")
    (s,) = solve(4 * x - 180, x)
    assert (s, s, 2 * s) == (45, 45, 90)


@ejercicio(id="triangulos-8-019", tipo="conceptual", dificultad=1, fuente=f"{F2}e",
           enunciado=r"¿En qué clasificaciones cae el triángulo del problema anterior (ángulos de "
                     r"$45^\circ$, $45^\circ$ y $90^\circ$)?",
           respuesta=r"Por sus lados es isósceles (dos ángulos iguales, luego dos lados iguales) y "
                     r"por sus ángulos es rectángulo: es un triángulo rectángulo isósceles.",
           **COMUN)
def _():
    T = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))   # ángulos 90, 45, 45
    assert sorted(deg(v) for v in T.angles.values()) == [45, 45, 90]
    assert T.is_right() and T.is_isosceles() and not T.is_equilateral()


@ejercicio(id="triangulos-8-020", tipo="calculo", dificultad=2,
           fuente=f"{F2}e (segunda pregunta)",
           enunciado=r"¿Qué medida debe tener cada uno de los ángulos adyacentes a la base de un "
                     r"triángulo isósceles para que este sea acutángulo?",
           respuesta=r"Más de $45^\circ$ y menos de $90^\circ$: si cada ángulo de la base mide $x$, "
                     r"el tercero mide $180^\circ - 2x$, y $x < 90^\circ$ y $180^\circ - 2x < "
                     r"90^\circ$ dan $45^\circ < x < 90^\circ$.",
           notas="En el módulo esta pregunta aparece sin letra, a continuación del literal e.",
           **COMUN)
def _():
    x = symbols("x", real=True)
    cond = [[x > 0, x < 90, 180 - 2 * x > 0, 180 - 2 * x < 90]]
    assert reduce_rational_inequalities(cond, x, relational=False) == Interval.open(45, 90)


@ejercicio(id="triangulos-8-021", tipo="calculo", dificultad=2, fuente=f"{F2}f",
           enunciado=r"En el triángulo $ABC$, el ángulo con vértice en $A$ mide $30^\circ$ y el "
                     r"ángulo externo en $B$ mide $110^\circ$. ¿Cuánto mide el ángulo $C$?",
           respuesta=r"El ángulo externo es igual a la suma de los internos no adyacentes: "
                     r"$110^\circ = 30^\circ + C$, así que $C = 80^\circ$ (y $B = 70^\circ$).",
           **COMUN)
def _():
    B = 180 - 110
    C = 180 - 30 - B
    assert (B, C) == (70, 80) and 30 + C == 110


@ejercicio(id="triangulos-8-022", tipo="calculo", dificultad=2, fuente=f"{F2}g",
           enunciado=r"En el triángulo $ABC$ los ángulos con vértice en $A$ y $B$ miden $50^\circ$ y "
                     r"$70^\circ$. Se forma un triángulo con las bisectrices de estos dos ángulos y "
                     r"el lado $AB$. ¿Cuánto mide cada ángulo de este nuevo triángulo?",
           respuesta=r"$25^\circ$ en $A$, $35^\circ$ en $B$ y $180^\circ - 25^\circ - 35^\circ = "
                     r"120^\circ$ en el punto donde se cortan las bisectrices.", **COMUN)
def _():
    A, B = Point(0, 0), Point(1, 0)
    ba = Line(A, A + Point(cos(rad(25)), sin(rad(25))))
    bb = Line(B, B + Point(-cos(rad(35)), sin(rad(35))))
    (I,) = ba.intersection(bb)
    ang = deg(angulo(A - I, B - I))
    assert abs(N(ang) - 120) < 1e-9
    assert 50 / 2 + 70 / 2 + 120 == 180


@ejercicio(id="triangulos-8-023", tipo="calculo", dificultad=3, fuente=f"{F2}h",
           enunciado=r"En el triángulo $ABC$, $\angle CAB = 30^\circ$ y $\angle CBA = 50^\circ$. "
                     r"¿Cuánto mide el ángulo formado por la altura y la bisectriz que pasan por "
                     r"$C$?",
           respuesta=r"$C = 100^\circ$. La altura forma con $CA$ un ángulo de $90^\circ - 30^\circ "
                     r"= 60^\circ$ y la bisectriz uno de $50^\circ$; el ángulo entre ellas es "
                     r"$60^\circ - 50^\circ = 10^\circ$.", **COMUN)
def _():
    A, B = Point(0, 0), Point(1, 0)
    la = Line(A, A + Point(cos(pi / 6), sin(pi / 6)))
    lb = Line(B, B + Point(-cos(rad(50)), sin(rad(50))))
    (C,) = la.intersection(lb)
    altura = Point(0, -1)
    bisectriz = (A - C) / C.distance(A) + (B - C) / C.distance(B)
    assert abs(N(deg(angulo(altura, bisectriz))) - 10) < 1e-9
