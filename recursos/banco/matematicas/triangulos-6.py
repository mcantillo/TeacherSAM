"""Banco de ejercicios — Matemáticas (Geometría 6°) — Propiedades y ángulos de los triángulos.
Fuente: módulo de Geometría de las Guías de Apoyo (Adriana Quintero Palomino), Tema 2:
Triángulos — «Practica lo aprendido» después de «Ortocentro»; se lee en
recursos/matematicas/Guías pedagógicas Matemáticas/markdown/Modulo_Matematicas_Geometria.md
El Tema 3 (teorema de Pitágoras, con raíces irracionales) no se incluyó: corresponde a los DBA
de 8° y 9°, no a los de 3° a 6°.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/triangulos-6.py
"""
from sympy import Eq, Line, Point, Rational, Segment, Triangle, deg, pi, simplify, solve, sqrt, symbols, tan

from ejercicios import ejercicio

FUENTE = ("módulo de Geometría (Quintero Palomino), Tema 2, Triángulos, Ortocentro — "
          "Practica lo aprendido")
VF = dict(tema="triángulos", grados=[6], dba=["matematicas-6-6"], tipo="argumentacion")
PR = dict(tema="triángulos", grados=[6], dba=["matematicas-6-5"], tipo="calculo")
INSTR = (r"Indica si la afirmación es verdadera o falsa y argumenta tu respuesta (las figuras "
         r"están en un plano): ")
x, y, t, p, q, m, h = symbols("x y t p q m h", positive=True)


def grados(angulo):
    return simplify(deg(angulo))


# ---------- 1. Verdadero o falso ----------

@ejercicio(id="triangulos-6-001", dificultad=1, fuente=f"{FUENTE} 1a",
           enunciado=INSTR + r"«La suma de las longitudes de dos lados de un triángulo puede "
                     r"ser mayor que el tercer lado».",
           respuesta=r"Verdadera; de hecho siempre lo es (desigualdad triangular). Por ejemplo, en "
                     r"el triángulo de lados 3, 4 y 5: $3 + 4 > 5$, $3 + 5 > 4$ y $4 + 5 > 3$.",
           **VF)
def _():
    T = Triangle(Point(0, 0), Point(4, 0), Point(0, 3))
    lados = sorted(s.length for s in T.sides)
    assert lados == [3, 4, 5] and lados[0] + lados[1] > lados[2]


@ejercicio(id="triangulos-6-002", dificultad=1, fuente=f"{FUENTE} 1b",
           enunciado=INSTR + r"«Ningún ángulo interno de un triángulo puede ser entrante (mayor "
                     r"que $180^\circ$)».",
           respuesta=r"Verdadera: los tres ángulos internos suman $180^\circ$, así que ninguno "
                     r"puede pasar de $180^\circ$.", **VF)
def _():
    T = Triangle(Point(0, 0), Point(7, 0), Point(-2, 1))       # uno muy obtuso
    angs = [float(deg(v)) for v in T.angles.values()]
    assert abs(sum(angs) - 180) < 1e-9 and all(v < 180 for v in angs) and max(angs) > 90


def angulo_bisectrices(alfa, beta):
    """Ángulo entre las bisectrices de dos ángulos adyacentes alfa y beta."""
    return alfa / 2 + beta / 2


@ejercicio(id="triangulos-6-003", dificultad=2, fuente=f"{FUENTE} 1c",
           enunciado=INSTR + r"«Las bisectrices de dos ángulos adyacentes son perpendiculares».",
           respuesta=r"Falsa en general: forman un ángulo igual a la mitad de la suma de los dos "
                     r"ángulos. Por ejemplo, si los adyacentes miden $30^\circ$ y $40^\circ$, las "
                     r"bisectrices forman $15^\circ + 20^\circ = 35^\circ$. Solo son "
                     r"perpendiculares cuando los adyacentes suman $180^\circ$.",
           notas="La figura del módulo muestra dos adyacentes suplementarios (cuyas bisectrices sí "
                 "son perpendiculares); la afirmación general es falsa.", **VF)
def _():
    assert angulo_bisectrices(30, 40) == 35 != 90
    assert solve(Eq(angulo_bisectrices(x, y), 90), y) == [180 - x]


@ejercicio(id="triangulos-6-004", dificultad=2, fuente=f"{FUENTE} 1d",
           enunciado=INSTR + r"«Las bisectrices de dos ángulos complementarios adyacentes son "
                     r"perpendiculares».",
           respuesta=r"Falsa: si los ángulos suman $90^\circ$, sus bisectrices forman "
                     r"$\frac{90^\circ}{2} = 45^\circ$.",
           notas="Se añadió «adyacentes» para que el ángulo entre las bisectrices tenga sentido.",
           **VF)
def _():
    assert angulo_bisectrices(x, 90 - x) == 45


@ejercicio(id="triangulos-6-005", dificultad=2, fuente=f"{FUENTE} 1e",
           enunciado=INSTR + r"«Las bisectrices de dos ángulos suplementarios adyacentes son "
                     r"perpendiculares».",
           respuesta=r"Verdadera: si los ángulos suman $180^\circ$, sus bisectrices forman "
                     r"$\frac{180^\circ}{2} = 90^\circ$.",
           notas="Se añadió «adyacentes» para que el ángulo entre las bisectrices tenga sentido.",
           **VF)
def _():
    assert angulo_bisectrices(x, 180 - x) == 90


@ejercicio(id="triangulos-6-006", dificultad=2, fuente=f"{FUENTE} 1f",
           enunciado=INSTR + r"«Si se dibuja una recta paralela a la base de un triángulo "
                     r"isósceles que pase por el vértice opuesto, esta forma dos ángulos de la "
                     r"misma medida con los lados iguales del triángulo».",
           respuesta=r"Verdadera: cada uno de esos ángulos es alterno interno con uno de los "
                     r"ángulos de la base, y en el triángulo isósceles los ángulos de la base "
                     r"son iguales.",
           notas="La descripción de la figura del módulo dice «triángulo equilátero», pero la "
                 "afirmación es sobre el isósceles (vale para los dos).", **VF)
def _():
    def angulos(A, B, C):
        """Ángulos que forma la paralela a AB por C con CA (hacia la izquierda) y con CB."""
        from sympy import acos
        u, v = A - C, B - C
        a_izq = acos(Point(-1, 0).dot(u) / u.distance(Point(0, 0)))
        a_der = acos(Point(1, 0).dot(v) / v.distance(Point(0, 0)))
        return a_izq, a_der

    A, B, C = Point(-m, 0), Point(m, 0), Point(0, h)       # isósceles: C sobre la mediatriz
    i, d = angulos(A, B, C)
    assert simplify(i - d) == 0
    from sympy import acos
    u, w = B - A, C - A
    base_A = acos(u.dot(w) / (u.distance(Point(0, 0)) * w.distance(Point(0, 0))))
    assert simplify(i - base_A) == 0                       # alterno interno con el de la base
    i2, d2 = angulos(Point(-2, 0), Point(2, 0), Point(1, 3))  # no isósceles: distintos
    assert simplify(i2 - d2) != 0


@ejercicio(id="triangulos-6-007", dificultad=1, fuente=f"{FUENTE} 1g",
           enunciado=INSTR + r"«Si la suma de dos ángulos internos de un triángulo es igual al "
                     r"tercer ángulo, entonces el triángulo es rectángulo».",
           respuesta=r"Verdadera: si $A + B = C$ y $A + B + C = 180^\circ$, entonces "
                     r"$2C = 180^\circ$ y $C = 90^\circ$.", **VF)
def _():
    a, b, c = symbols("a b c", positive=True)
    assert solve([Eq(a + b, c), Eq(a + b + c, 180)], [b, c])[c] == 90


@ejercicio(id="triangulos-6-008", dificultad=3, fuente=f"{FUENTE} 1h",
           enunciado=INSTR + r"«Si la mediana de la base de un triángulo es perpendicular a la "
                     r"base, entonces el triángulo es isósceles».",
           respuesta=r"Verdadera: esa mediana pasa por el punto medio de la base y es "
                     r"perpendicular a ella, así que es la mediatriz de la base; el vértice "
                     r"opuesto está en la mediatriz y por eso está a la misma distancia de los "
                     r"dos extremos de la base: los otros dos lados son iguales.", **VF)
def _():
    A, B, C = Point(0, 0), Point(2 * m, 0), Point(p, q)
    mediana = Line(C, Segment(A, B).midpoint)
    cond = solve(Eq(mediana.direction.dot(Point(1, 0)), 0), p)     # perpendicular a AB
    assert cond == [m]
    assert simplify(C.subs(p, m).distance(A) - C.subs(p, m).distance(B)) == 0


@ejercicio(id="triangulos-6-009", dificultad=2, fuente=f"{FUENTE} 1i",
           enunciado=INSTR + r"«Una de las medianas de un triángulo isósceles es perpendicular a "
                     r"la base».",
           respuesta=r"Verdadera: la mediana que va del vértice opuesto al punto medio de la "
                     r"base; como ese vértice está a igual distancia de los extremos de la base, "
                     r"la mediana coincide con la mediatriz de la base.", **VF)
def _():
    A, B, C = Point(-m, 0), Point(m, 0), Point(0, h)
    mediana = Line(C, Segment(A, B).midpoint)
    assert mediana.is_perpendicular(Line(A, B))


@ejercicio(id="triangulos-6-010", dificultad=2, fuente=f"{FUENTE} 1j",
           enunciado=INSTR + r"«Cualquier triángulo rectángulo isósceles puede dividirse con una "
                     r"recta en otros dos triángulos rectángulos isósceles».",
           respuesta=r"Verdadera: la altura trazada desde el ángulo recto lo divide en dos "
                     r"triángulos, cada uno con un ángulo recto (en el pie de la altura) y dos "
                     r"ángulos de $45^\circ$.", **VF)
def _():
    A, B, C = Point(0, 0), Point(t, 0), Point(0, t)          # recto en A
    D = Segment(B, C).midpoint                                # pie de la altura desde A
    assert Line(A, D).is_perpendicular(Line(B, C))
    for T in (Triangle(A, B, D), Triangle(A, C, D)):
        angs = sorted((grados(v) for v in T.angles.values()), key=float)
        assert angs == [45, 45, 90]


@ejercicio(id="triangulos-6-011", dificultad=3, fuente=f"{FUENTE} 1k",
           enunciado=INSTR + r"«Si la mediatriz de la base de un triángulo coincide con la "
                     r"bisectriz del ángulo opuesto a la base, entonces el triángulo es "
                     r"isósceles».",
           respuesta=r"Verdadera: si coinciden, el vértice opuesto está sobre la mediatriz de la "
                     r"base, así que está a la misma distancia de sus dos extremos: los otros dos "
                     r"lados son iguales.", **VF)
def _():
    A, B = Point(-m, 0), Point(m, 0)
    C = Point(0, h)                          # sobre la mediatriz x = 0
    assert simplify(C.distance(A) - C.distance(B)) == 0
    ang_izq = Line(C, A).angle_between(Line(C, Point(0, 0)))
    ang_der = Line(C, B).angle_between(Line(C, Point(0, 0)))
    assert simplify(ang_izq - ang_der) == 0          # la mediatriz es también bisectriz


@ejercicio(id="triangulos-6-012", dificultad=3, fuente=f"{FUENTE} 1l",
           enunciado=INSTR + r"«Una recta perpendicular a la bisectriz de un ángulo forma un "
                     r"triángulo isósceles con los lados del ángulo».",
           respuesta=r"Verdadera: la recta corta los dos lados en puntos $P$ y $Q$. Los "
                     r"triángulos que forman la bisectriz, la recta y cada lado tienen un lado "
                     r"común, un ángulo recto y la mitad del ángulo, así que son congruentes; "
                     r"por eso $OP = OQ$ ($O$ es el vértice).", **VF)
def _():
    # vértice en el origen, bisectriz sobre el eje x, lados con inclinación ±x (0 < x < 90°)
    P, Q = Point(t, t * tan(x)), Point(t, -t * tan(x))        # recta x = t
    assert simplify(Point(0, 0).distance(P) - Point(0, 0).distance(Q)) == 0


@ejercicio(id="triangulos-6-013", dificultad=1, fuente=f"{FUENTE} 1m",
           enunciado=INSTR + r"«Ningún triángulo puede tener más de un ángulo recto».",
           respuesta=r"Verdadera: dos ángulos rectos ya suman $180^\circ$ y el tercer ángulo "
                     r"tendría que medir $0^\circ$.", **VF)
def _():
    assert solve(Eq(90 + 90 + y, 180), y) == []            # y > 0 no tiene solución


@ejercicio(id="triangulos-6-014", dificultad=1, fuente=f"{FUENTE} 1n",
           enunciado=INSTR + r"«Ningún triángulo puede tener más de un ángulo obtuso».",
           respuesta=r"Verdadera: dos ángulos obtusos suman más de $180^\circ$, y los tres "
                     r"ángulos del triángulo suman exactamente $180^\circ$.", **VF)
def _():
    assert solve(Eq((90 + x) + (90 + y) + t, 180), t) == []      # x, y, t > 0


# ---------- 2. Problemas ----------

@ejercicio(id="triangulos-6-015", dificultad=2, fuente=f"{FUENTE} 2a",
           enunciado=r"Los ángulos agudos de un triángulo rectángulo son tales que uno es el "
                     r"doble del otro. ¿Cuánto miden los tres ángulos internos?",
           respuesta=r"$x + 2x = 90^\circ$, así que miden $30^\circ$, $60^\circ$ y $90^\circ$.",
           **PR)
def _():
    assert solve(Eq(x + 2 * x + 90, 180), x) == [30]


@ejercicio(id="triangulos-6-016", dificultad=1, fuente=f"{FUENTE} 2b",
           enunciado=r"Los ángulos agudos de un triángulo rectángulo son iguales. ¿Cuánto miden "
                     r"los tres ángulos internos?",
           respuesta=r"$45^\circ$, $45^\circ$ y $90^\circ$.", **PR)
def _():
    assert solve(Eq(2 * x + 90, 180), x) == [45]


@ejercicio(id="triangulos-6-017", dificultad=1, fuente=f"{FUENTE} 2c",
           enunciado=r"El ángulo opuesto a la base de un triángulo isósceles mide $50^\circ$. "
                     r"¿Cuánto miden los otros dos ángulos internos?",
           respuesta=r"Son iguales y suman $180^\circ - 50^\circ = 130^\circ$: cada uno mide "
                     r"$65^\circ$.", **PR)
def _():
    assert solve(Eq(2 * x + 50, 180), x) == [65]


@ejercicio(id="triangulos-6-018", dificultad=2, fuente=f"{FUENTE} 2d",
           enunciado=r"El ángulo opuesto a la base de un triángulo isósceles mide el doble de lo "
                     r"que mide cada uno de los otros dos. ¿Cuánto miden los ángulos internos?",
           respuesta=r"$x + x + 2x = 180^\circ$: miden $45^\circ$, $45^\circ$ y $90^\circ$.", **PR)
def _():
    assert solve(Eq(x + x + 2 * x, 180), x) == [45]


@ejercicio(id="triangulos-6-019", dificultad=3, fuente=f"{FUENTE} 2e",
           enunciado=r"¿Dentro de qué clasificaciones cae el triángulo del problema anterior "
                     r"(ángulos de $45^\circ$, $45^\circ$ y $90^\circ$)? ¿Qué medida debe tener "
                     r"cada uno de los ángulos de la base de un triángulo isósceles para que "
                     r"este sea acutángulo?",
           respuesta=r"Es un triángulo rectángulo (tiene un ángulo de $90^\circ$) e isósceles "
                     r"(dos ángulos, y por eso dos lados, iguales). Para que un isósceles sea "
                     r"acutángulo, cada ángulo de la base debe medir más de $45^\circ$ y menos "
                     r"de $90^\circ$ (así el ángulo opuesto, $180^\circ - 2x$, es menor que "
                     r"$90^\circ$).",
           notas="En el módulo la segunda pregunta aparece sin letra, después de la «e»; se "
                 "unió a la «e».", **PR)
def _():
    from sympy import Interval, S, solveset
    angulos = [45, 45, 90]
    assert 90 in angulos and len(set(angulos)) == 2
    b = symbols("b", real=True)
    cond = solveset(180 - 2 * b < 90, b, Interval.open(0, 90))
    assert cond == Interval.open(45, 90)


@ejercicio(id="triangulos-6-020", dificultad=2, fuente=f"{FUENTE} 2f",
           enunciado=r"En el triángulo $ABC$, el ángulo con vértice en $A$ mide $30^\circ$ y el "
                     r"ángulo externo en $B$ mide $110^\circ$. ¿Cuánto mide el ángulo $C$?",
           respuesta=r"El ángulo interno en $B$ mide $180^\circ - 110^\circ = 70^\circ$, así que "
                     r"$C = 180^\circ - 30^\circ - 70^\circ = 80^\circ$ (también: el externo en "
                     r"$B$ es igual a $A + C$).", **PR)
def _():
    B = 180 - 110
    assert 180 - 30 - B == 80 and 110 - 30 == 80


@ejercicio(id="triangulos-6-021", dificultad=3, fuente=f"{FUENTE} 2g",
           enunciado=r"En el triángulo $ABC$, los ángulos con vértice en $A$ y $B$ miden "
                     r"$50^\circ$ y $70^\circ$. Se forma un triángulo con las bisectrices de esos "
                     r"dos ángulos y el lado $AB$. ¿Cuánto mide cada ángulo de este nuevo "
                     r"triángulo?",
           respuesta=r"$25^\circ$ en $A$, $35^\circ$ en $B$ y $180^\circ - 25^\circ - 35^\circ = "
                     r"120^\circ$ en el punto donde se cortan las bisectrices.",
           notas="En el módulo aparece «triángulo 6ABC» (el símbolo del triángulo se convirtió "
                 "en «6»); se escribió «triángulo ABC».", **PR)
def _():
    A, B = Point(0, 0), Point(1, 0)
    C = Line(A, A + Point(1, tan(pi * 50 / 180))).intersection(
        Line(B, B + Point(-1, tan(pi * 70 / 180))))[0]
    I = Triangle(A, B, C).incenter                 # donde se cortan las bisectrices
    angs = Triangle(A, B, I).angles
    assert [round(float(deg(angs[v])), 9) for v in (A, B, I)] == [25, 35, 120]


@ejercicio(id="triangulos-6-022", dificultad=3, fuente=f"{FUENTE} 2h",
           enunciado=r"En el triángulo $ABC$, $\angle CAB = 30^\circ$ y $\angle CBA = 50^\circ$. "
                     r"Desde el vértice $C$ se trazan la altura y la bisectriz del ángulo $C$. "
                     r"¿Cuánto mide el ángulo formado por la altura y la bisectriz?",
           respuesta=r"$C = 100^\circ$, así que la bisectriz forma $50^\circ$ con $CA$. La altura "
                     r"forma con $CA$ un ángulo de $90^\circ - 30^\circ = 60^\circ$. El ángulo "
                     r"entre ellas es $60^\circ - 50^\circ = 10^\circ$.",
           notas="La figura del módulo solo muestra la altura y la bisectriz desde C; se "
                 "describió en el enunciado.", **PR)
def _():
    A, B = Point(0, 0), Point(1, 0)
    C = Line(A, A + Point(1, tan(pi * 30 / 180))).intersection(
        Line(B, B + Point(-1, tan(pi * 50 / 180))))[0]
    pie = Line(A, B).projection(C)
    I = Triangle(A, B, C).incenter
    ang = Line(C, pie).angle_between(Line(C, I))
    assert round(float(deg(ang)), 9) == 10
