"""Banco de ejercicios — Matemáticas 9° — Función cuadrática.
Fuente: módulo de Matemáticas 9° de las Guías de Apoyo (Adriana Quintero Palomino), Tema 5;
se lee en recursos/matematicas/Guías pedagógicas Matemáticas/markdown/09 - Modulo_Matematicas_Noveno.md
Los ejercicios 8 a 12 («representa en los mismos ejes… ¿en qué se parecen y se diferencian?»)
van como un solo ejercicio cada uno: sus literales son las funciones de una misma gráfica.
Los de «dibuja» se registran con las características que debe mostrar la gráfica (vértice, eje,
concavidad, cortes), que sí se comprueban.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/funcion-cuadratica-9.py
"""
from sympy import FiniteSet, Poly, Rational, S, expand, solve, solveset, symbols

from ejercicios import ejercicio, expresion, tex

FUENTE = "módulo 9° (Quintero Palomino), Tema 5, Función cuadrática — Practica lo aprendido"
COMUN = dict(tema="función cuadrática", grados=[9], dba=["matematicas-9-2"])
CONTEXTO = dict(tema="función cuadrática", grados=[9], dba=["matematicas-9-2", "matematicas-9-8"],
                tipo="contexto")
x = expresion("x")


def vertice(f):
    a, b, _c = Poly(expand(f), x).all_coeffs()
    h = -b / (2 * a)
    return h, expand(f).subs(x, h)


# ---------- 1–4: determinar la función ----------
a, b, c, m, n_ = symbols("a b c m n")


@ejercicio(id="funcion-cuadratica-9-001", tipo="argumentacion", dificultad=3,
           fuente=f"{FUENTE} 1",
           enunciado=r"Una función cuadrática de la forma $y = ax^2 + bx + c$ toma el valor $7$ "
                     r"para $x = -1$ y para $x = 2$. Determina esta función.",
           respuesta=r"Las condiciones $a - b + c = 7$ y $4a + 2b + c = 7$ dan $b = -a$ y "
                     r"$c = 7 - 2a$: hay infinitas funciones, $y = ax^2 - ax + 7 - 2a$ con "
                     r"$a \neq 0$, todas con eje de simetría $x = \frac{1}{2}$ (por ejemplo, "
                     r"$y = x^2 - x + 5$). Para una sola función haría falta un tercer dato.",
           notas="El enunciado del módulo da solo dos condiciones para tres coeficientes; se "
                 "dejó así y la respuesta explica que la función no queda determinada.", **COMUN)
def _():
    sol = solve([a - b + c - 7, 4 * a + 2 * b + c - 7], [b, c])
    assert sol == {b: -a, c: 7 - 2 * a}
    f = a * x**2 - a * x + 7 - 2 * a
    assert expand(f.subs(x, -1)) == 7 and expand(f.subs(x, 2)) == 7
    assert vertice(f.subs(a, 1))[0] == Rational(1, 2)


@ejercicio(id="funcion-cuadratica-9-002", tipo="calculo", dificultad=1, fuente=f"{FUENTE} 2",
           enunciado=r"Sea la función $f(x) = x^2 + mx + m$. Determina $m$ sabiendo que la gráfica "
                     r"pasa por el punto $(2, 7)$.",
           respuesta=r"$4 + 2m + m = 7$, luego $m = 1$: $f(x) = x^2 + x + 1$.", **COMUN)
def _():
    assert solve((x**2 + m * x + m).subs(x, 2) - 7, m) == [1]


@ejercicio(id="funcion-cuadratica-9-003", tipo="calculo", dificultad=2, fuente=f"{FUENTE} 3",
           enunciado=r"Sea la función $f(x) = x^2 + mx + n$. Determina $m$ y $n$ sabiendo que la "
                     r"gráfica pasa por los puntos $(1, 0)$ y $(-3, 4)$.",
           respuesta=r"$1 + m + n = 0$ y $9 - 3m + n = 4$: $m = 1$, $n = -2$; "
                     r"$f(x) = x^2 + x - 2$.", **COMUN)
def _():
    f = x**2 + m * x + n_
    assert solve([f.subs(x, 1), f.subs(x, -3) - 4], [m, n_]) == {m: 1, n_: -2}


@ejercicio(id="funcion-cuadratica-9-004", tipo="calculo", dificultad=2, fuente=f"{FUENTE} 4",
           enunciado=r"Sea la función $y = ax^2 + bx + c$. Determina $a$, $b$ y $c$ sabiendo que "
                     r"la gráfica pasa por los puntos $(1, 0)$, $(0, 0)$ y $(-1, 2)$.",
           respuesta=r"$c = 0$, $a + b = 0$ y $a - b = 2$: $a = 1$, $b = -1$, $c = 0$; "
                     r"$y = x^2 - x$.", **COMUN)
def _():
    f = a * x**2 + b * x + c
    assert solve([f.subs(x, 1), f.subs(x, 0), f.subs(x, -1) - 2], [a, b, c]) == \
        {a: 1, b: -1, c: 0}


# ---------- 5: dibujar ----------
# (n, literal, función, vértice (h, k), cortes con el eje x escritos a mano, corte con el eje y)
DIBUJOS = [
    (5, "5a", "x^2 - 6x + 10", ("3", "1"), [], "10"),
    (6, "5b", "x^2 - 4x + 4", ("2", "0"), ["2"], "4"),
    (7, "5c", "-x^2 - 4x - 2", ("-2", "2"), ["-2 - sqrt(2)", "-2 + sqrt(2)"], "-2"),
    (8, "5d", "x^2 - 4", ("0", "-4"), ["-2", "2"], "-4"),
    (9, "5e", "-2x^2 - x + 6", ("-1/4", "49/8"), ["-2", "3/2"], "6"),
    (10, "5f", "x^2 + 2x + 2", ("-1", "1"), [], "2"),
]
for n, literal, f, (h, k), cortes, corte_y in DIBUJOS:
    abre = "hacia arriba" if not f.startswith("-") else "hacia abajo"
    if not cortes:
        txt_cortes = r"no corta el eje $x$ ($\Delta < 0$)"
    elif len(cortes) == 1:
        txt_cortes = rf"toca el eje $x$ solo en $x = {tex(cortes[0])}$ ($\Delta = 0$)"
    else:
        txt_cortes = (rf"corta el eje $x$ en $x = {tex(cortes[0])}$ y $x = {tex(cortes[1])}$ "
                      r"($\Delta > 0$)")

    @ejercicio(id=f"funcion-cuadratica-9-{n:03d}", tipo="calculo", dificultad=2,
               fuente=f"{FUENTE} {literal}",
               enunciado=rf"Dibuja la función $y = {tex(f)}$: señala su vértice, su eje de "
                         r"simetría y los cortes con los ejes.",
               respuesta=rf"Parábola que abre {abre}, vértice $\left({tex(h)}, {tex(k)}\right)$, "
                         rf"eje $x = {tex(h)}$; {txt_cortes}; corta el eje $y$ en "
                         rf"$(0, {tex(corte_y)})$.", **COMUN)
    def _(f=f, h=h, k=k, cortes=cortes, corte_y=corte_y):
        g = expresion(f)
        assert vertice(g) == (expresion(h), expresion(k))
        assert solveset(g, x, S.Reals) == FiniteSet(*map(expresion, cortes))
        assert g.subs(x, 0) == expresion(corte_y)
        a_ = Poly(g, x).LC()
        assert (a_ < 0) == f.startswith("-")


# ---------- 6: tabla y simetría ----------
TABLA = r"""Una función cuadrática viene dada por esta tabla:
\begin{center}\begin{tabular}{c|ccccccccc}
$x$ & $-4$ & $-3$ & $-2$ & $-1$ & $0$ & $1$ & $2$ & $3$ & $4$ \\ \hline
$y$ & $17$ & $10$ & & $2$ & $1$ & & $5$ & & $17$
\end{tabular}\end{center}
"""
DATOS = {-4: 17, -3: 10, -1: 2, 0: 1, 2: 5, 4: 17}


@ejercicio(id="funcion-cuadratica-9-011", tipo="calculo", dificultad=1, fuente=f"{FUENTE} 6a",
           enunciado=TABLA + "Completa la tabla teniendo en cuenta la simetría.",
           respuesta=r"Como $y(-4) = y(4) = 17$, el eje de simetría es $x = 0$: "
                     r"$y(-2) = y(2) = 5$, $y(1) = y(-1) = 2$ y $y(3) = y(-3) = 10$.", **COMUN)
def _():
    f = solve([a * t**2 + b * t + c - v for t, v in list(DATOS.items())[:3]], [a, b, c])
    g = f[a] * x**2 + f[b] * x + f[c]
    assert all(g.subs(x, t) == v for t, v in DATOS.items())            # los datos son de g
    assert [g.subs(x, t) for t in (-2, 1, 3)] == [5, 2, 10]


@ejercicio(id="funcion-cuadratica-9-012", tipo="calculo", dificultad=2, fuente=f"{FUENTE} 6b",
           enunciado=TABLA + "¿Puedes determinar la fórmula que define esta función?",
           respuesta=r"Sí: el vértice es $(0, 1)$ y al pasar de $x = 0$ a $x = \pm 1$ la $y$ "
                     r"aumenta $1$, a $x = \pm 2$ aumenta $4$: $y = x^2 + 1$.", **COMUN)
def _():
    assert all((x**2 + 1).subs(x, t) == v for t, v in DATOS.items())


@ejercicio(id="funcion-cuadratica-9-013", tipo="argumentacion", dificultad=1,
           fuente=f"{FUENTE} 6c",
           enunciado=TABLA + "¿Tiene valores negativos esta función?",
           respuesta=r"No: $y = x^2 + 1 \ge 1$ para todo $x$; su valor mínimo es $1$, en el "
                     r"vértice $(0, 1)$.", **COMUN)
def _():
    assert solveset(x**2 + 1 < 0, x, S.Reals) == S.EmptySet
    assert vertice(x**2 + 1) == (0, 1)


# ---------- 7: producto de dos números que suman 32 ----------

@ejercicio(id="funcion-cuadratica-9-014", dificultad=2, fuente=f"{FUENTE} 7",
           enunciado=r"Determina una función que calcule el producto de dos números que suman "
                     r"$32$. ¿Qué tipo de función es? Dibújala.",
           respuesta=r"Si uno de los números es $x$, el otro es $32 - x$ y el producto es "
                     r"$P(x) = x(32 - x) = -x^2 + 32x$: una función cuadrática. Su gráfica es una "
                     r"parábola que abre hacia abajo, corta el eje $x$ en $0$ y $32$, y tiene "
                     r"vértice $(16, 256)$: el producto mayor es $256$, cuando los dos números "
                     r"valen $16$.", **CONTEXTO)
def _():
    P = x * (32 - x)
    assert expand(P - (-x**2 + 32 * x)) == 0
    assert vertice(P) == (16, 256)
    assert solveset(P, x, S.Reals) == S({0, 32})


# ---------- 8–12: familias de parábolas ----------
# (n, literal, funciones, vértices escritos a mano, respuesta)
FAMILIAS = [
    (15, "8", ["x^2", "x^2 + 2", "x^2 - 4", "x^2 + 4"], [(0, 0), (0, 2), (0, -4), (0, 4)],
     r"Todas tienen la misma forma y abren hacia arriba ($a = 1$) y el mismo eje, $x = 0$. Se "
     r"diferencian en el vértice: $(0, 0)$, $(0, 2)$, $(0, -4)$ y $(0, 4)$; cada una es "
     r"$f(x) = x^2$ desplazada verticalmente $2$ hacia arriba, $4$ hacia abajo y $4$ hacia "
     r"arriba."),
    (16, "9", ["-2x^2", "-2x^2 + 2", "-2x^2 - 2", "-2x^2 + 8"], [(0, 0), (0, 2), (0, -2), (0, 8)],
     r"Todas abren hacia abajo, con la misma abertura ($a = -2$, más cerradas que $y = x^2$) y "
     r"eje $x = 0$. Se diferencian en el vértice: $(0, 0)$, $(0, 2)$, $(0, -2)$ y $(0, 8)$ "
     r"(desplazamientos verticales de $2$, $-2$ y $8$)."),
    (17, "10", ["x^2", "(x + 2)^2", "(x - 3)^2", "(x + 4)^2"], [(0, 0), (-2, 0), (3, 0), (-4, 0)],
     r"Todas abren hacia arriba con la misma forma y tienen el vértice sobre el eje $x$. Se "
     r"diferencian en el eje de simetría: $x = 0$, $x = -2$, $x = 3$ y $x = -4$; son "
     r"$y = x^2$ desplazada horizontalmente $2$ a la izquierda, $3$ a la derecha y $4$ a la "
     r"izquierda."),
    (18, "11", ["-2x^2", "-2(x + 2)^2", "-2(x - 3)^2", "-2(x + 4)^2"],
     [(0, 0), (-2, 0), (3, 0), (-4, 0)],
     r"Todas abren hacia abajo con $a = -2$ y tienen el vértice sobre el eje $x$. Se diferencian "
     r"en el vértice y el eje: $(0, 0)$, $(-2, 0)$, $(3, 0)$ y $(-4, 0)$ (desplazamientos "
     r"horizontales de $2$ a la izquierda, $3$ a la derecha y $4$ a la izquierda)."),
    (19, "12", ["x^2", "(x + 2)^2 + 1", "(x - 3)^2 - 4", "(x + 4)^2 + 2"],
     [(0, 0), (-2, 1), (3, -4), (-4, 2)],
     r"Todas abren hacia arriba con la misma forma ($a = 1$). Se diferencian en el vértice: "
     r"$(0, 0)$, $(-2, 1)$, $(3, -4)$ y $(-4, 2)$; cada una es $y = x^2$ trasladada a la vez "
     r"horizontal y verticalmente."),
]
NOMBRES = ["f", "g", "h", "m"]
for n, numero, funciones, vertices, respuesta in FAMILIAS:
    lista = ", ".join(f"${nom}(x) = {tex(fn)}$" for nom, fn in zip(NOMBRES, funciones))

    @ejercicio(id=f"funcion-cuadratica-9-{n:03d}", tipo="conceptual", dificultad=2,
               fuente=f"{FUENTE} {numero}",
               enunciado=f"Representa en los mismos ejes de coordenadas las funciones {lista}. "
                         f"¿En qué se parecen y en qué se diferencian?",
               respuesta=respuesta, **COMUN)
    def _(funciones=funciones, vertices=vertices):
        gs = [expresion(fn) for fn in funciones]
        assert [vertice(g) for g in gs] == [tuple(map(S, v)) for v in vertices]
        lc = {Poly(g, x).LC() for g in gs}
        assert len(lc) == 1                              # misma forma y misma concavidad
        for g, (h, k) in zip(gs, vertices):              # g es la primera trasladada (h, k)
            assert expand(g - gs[0].subs(x, x - h) - k) == 0


# ---------- 13: la piedra ----------
t = symbols("t", nonnegative=True)
PIEDRA = (r"Si lanzamos una piedra hacia arriba, su altura está dada por la función "
          r"$f(t) = -5t^2 + 50t$, donde $t$ es el tiempo en segundos y $f(t)$ la altura en "
          r"metros. ")


@ejercicio(id="funcion-cuadratica-9-020", dificultad=2, fuente=f"{FUENTE} 13a",
           enunciado=PIEDRA + r"¿En qué segundo alcanza la altura máxima y cuál es esa altura?",
           respuesta=r"En el vértice: $t = -\dfrac{50}{2(-5)} = 5$ s, y $f(5) = -125 + 250 = 125$ "
                     r"m.", **CONTEXTO)
def _():
    f = -5 * t**2 + 50 * t
    assert solve(f.diff(t), t) == [5] and f.subs(t, 5) == 125


@ejercicio(id="funcion-cuadratica-9-021", dificultad=2, fuente=f"{FUENTE} 13b",
           enunciado=PIEDRA + r"¿En qué segundo cae a tierra? Representa la función.",
           respuesta=r"$-5t^2 + 50t = 0 \iff 5t(10 - t) = 0$: sale en $t = 0$ y cae en "
                     r"$t = 10$ s. La gráfica es el arco de parábola que abre hacia abajo entre "
                     r"$(0, 0)$ y $(10, 0)$, con vértice $(5, 125)$.", **CONTEXTO)
def _():
    assert solve(-5 * t**2 + 50 * t, t) == [0, 10]


# ---------- 14: el tiro al arco ----------

@ejercicio(id="funcion-cuadratica-9-022", dificultad=3, fuente=f"{FUENTE} 14",
           enunciado=r"Un jugador de fútbol está a $8$ metros de la portería. El portero está a "
                     r"$4$ metros del jugador y, saltando, puede cubrir hasta $\num{2,5}$ metros de "
                     r"altura. El jugador puede escoger entre dos trayectorias para el balón: "
                     r"$y = \num{0,4}x - \num{0,05}x^2$ y $y = \num{1,6}x - \num{0,2}x^2$ ($x$ es "
                     r"la distancia horizontal y $y$ la altura, en metros). ¿Cuál es mejor? "
                     r"¿Por qué?",
           respuesta=r"Las dos llegan a la portería: en $x = 8$ ambas dan $y = 0$ (el balón entra "
                     r"a ras de piso). Al pasar por el portero ($x = 4$), la primera va a "
                     r"$\num{0,8}$ m, que él alcanza, y la segunda a $\num{3,2}$ m, más de lo "
                     r"que cubre. Es mejor la segunda: $y = \num{1,6}x - \num{0,2}x^2$.",
           notas="El módulo anuncia dos trayectorias pero solo escribe y = 1,6x - 0,2x^2; se "
                 "añadió y = 0,4x - 0,05x^2 (reconstruida; la docente debe confirmarla o "
                 "cambiarla). Se aclaró que el portero está a 4 m del jugador.", **CONTEXTO)
def _():
    y1 = Rational(2, 5) * x - Rational(1, 20) * x**2
    y2 = Rational(8, 5) * x - Rational(1, 5) * x**2
    assert y1.subs(x, 8) == 0 and y2.subs(x, 8) == 0
    assert y1.subs(x, 4) == Rational(4, 5) < Rational(5, 2) < y2.subs(x, 4) == Rational(16, 5)
