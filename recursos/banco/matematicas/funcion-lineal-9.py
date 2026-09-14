"""Banco de ejercicios — Matemáticas 9° — Función lineal, pendiente, rectas paralelas y perpendiculares.
Fuente: módulo de Matemáticas 9° de las Guías de Apoyo (Adriana Quintero Palomino), Tema 1
«Funciones lineales»; se lee en
recursos/matematicas/Guías pedagógicas Matemáticas/markdown/09 - Modulo_Matematicas_Noveno.md
El módulo llama «funciones de gráfica lineal» a las de la forma f(x) = mx + b.
En varios literales el módulo escribe «X» mayúscula por «x» (5d, 14b) y «Ax + By + C = O» con la
letra O (ejercicio 11): aquí se escriben x y 0.
No se incluyó el ejemplo resuelto de utilidades de «Prepárate para el ICFES» (no es un ejercicio;
se comprobó que U(20 000) = $25 000 000 es correcto).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/funcion-lineal-9.py
"""
import re

from sympy import FiniteSet, Rational as Q, S, diff, simplify, solve, solveset, symbols

from ejercicios import ejercicio, ejercicio_manual, expresion, tex

MODULO = "módulo 9° (Quintero Palomino), Tema 1, Funciones lineales"
FUENTE = f"{MODULO} — Practica lo aprendido"
ICFES = f"{MODULO} — Prepárate para el ICFES, problema"
COMUN = dict(tema="función lineal", grados=[9], dba=["matematicas-9-8", "matematicas-9-2"])

x, y = symbols("x y", real=True)
_N = [0]


def nid():
    _N[0] += 1
    return f"funcion-lineal-9-{_N[0]:03d}"


# ---------- utilidades: una misma cadena da el LaTeX del enunciado y la ecuación de SymPy ----------

def ecuacion(s):
    """«4x + 3y = 8» → 4x + 3y - 8 (f(x), f(t) se leen como y)."""
    a, b = re.sub(r"f\(\w\)", "y", s).split("=")
    return expresion(a) - expresion(b)


def eqtex(s):
    a, b = (t.strip() for t in s.split("="))
    return f"{a if re.fullmatch(r'f\(\w\)', a) else tex(a)} = {tex(b)}"


def despejar_y(s):
    sol = solve(ecuacion(s), y)
    assert len(sol) == 1
    return sol[0]


def fr(q):
    q = Q(q)
    s = "-" if q < 0 else ""
    a = abs(q)
    return s + (str(a.p) if a.q == 1 else rf"\frac{{{a.p}}}{{{a.q}}}")


def coef(m, var="x"):
    m = Q(m)
    if m == 0:
        return ""
    if abs(m) == 1:
        return ("-" if m < 0 else "") + var
    return fr(m) + var


def ymxb(m, b, v="y"):
    t, b = coef(m), Q(b)
    if b == 0:
        return f"{v} = {t or '0'}"
    if not t:
        return f"{v} = {fr(b)}"
    return f"{v} = {t} {'+' if b > 0 else '-'} {fr(abs(b))}"


def pt(a, b):
    a, b = Q(a), Q(b)
    if a.q == 1 and b.q == 1:
        return f"({a}, {b})"
    return rf"\left({fr(a)}, {fr(b)}\right)"


def abc(s):
    """Coeficientes (A, B, C) de Ax + By + C = 0."""
    L = ecuacion(s)
    return diff(L, x), diff(L, y), L.subs({x: 0, y: 0})


# ---------- 1. Trazar funciones de gráfica lineal ----------
# (literal, ecuación, pendiente, corte con el eje y, abscisa de un segundo punto) — a mano
E1 = [("a", "y = x", 1, 0, 1), ("b", "y = 4x + 5", 4, 5, -1), ("c", "y = 8 - 3x", -3, 8, 2),
      ("d", "y = (x + 6)/2", Q(1, 2), 3, -6), ("e", "4x + 3y = 8", Q(-4, 3), Q(8, 3), 2),
      ("f", "f(x) = 5x - 4", 5, -4, 1), ("g", "f(x) = x + 1/2", 1, Q(1, 2), Q(-1, 2)),
      ("h", "3y + 9 = x", Q(1, 3), -3, 9), ("i", "f(x) = 3x + 3", 3, 3, -1),
      ("j", "f(x) = -2x - 1", -2, -1, 1), ("k", "y = -2x + 4", -2, 4, 2),
      ("l", "f(x) = x/2 + 4", Q(1, 2), 4, -8), ("m", "f(x) = -3x", -3, 0, 1),
      ("n", "f(x) = -2x + 3", -2, 3, 1), ("o", "f(x) = -x + 6", -1, 6, 6),
      ("p", "y = (1/2)x + 3/5", Q(1, 2), Q(3, 5), 2)]
for lit, s, m, b, x1 in E1:
    y1 = Q(m) * x1 + b

    @ejercicio(id=nid(), tipo="calculo", dificultad=1 if Q(m).q == 1 and Q(b).q == 1 else 2,
               fuente=f"{FUENTE} 1{lit}",
               enunciado=f"Traza la gráfica de la función ${eqtex(s)}$.",
               respuesta=f"Es la recta ${ymxb(m, b)}$, de pendiente ${fr(m)}$, que corta el eje $y$ "
                         f"en ${pt(0, b)}$ y pasa también por ${pt(x1, y1)}$: se ubican esos dos "
                         f"puntos y se traza la recta que los une.", **COMUN)
    def _(s=s, m=m, b=b, x1=x1, y1=y1):
        assert simplify(despejar_y(s) - (m * x + b)) == 0
        assert ecuacion(s).subs({x: x1, y: y1}) == 0 and ecuacion(s).subs({x: 0, y: b}) == 0


# ---------- 2. Situaciones → función ----------
E2 = [("a", r"El costo de $n$ artículos si cada uno tiene un valor de \$3500.",
       r"$C(n) = 3500n$, donde $n$ es el número de artículos.", 3500),
      ("b", r"La cantidad de viajes que realiza un camión en el mes si cada día realiza $6$ "
            r"viajes.",
       r"$V(d) = 6d$, donde $d$ es el número de días del mes que trabaja el camión.", 6),
      ("c", r"El recaudo por las entradas a un evento si cada una cuesta \$8000.",
       r"$R(n) = 8000n$, donde $n$ es el número de entradas vendidas.", 8000)]
for lit, texto, resp, k in E2:
    @ejercicio(id=nid(), tipo="contexto", dificultad=1, fuente=f"{FUENTE} 2{lit}",
               enunciado=f"Representa en forma de función la siguiente situación: {texto}",
               respuesta=resp, **COMUN)
    def _(k=k, resp=resp):
        f = expresion(re.search(r"= (\w+)\$", resp).group(1).replace(str(k), f"{k}*"))
        v = f.free_symbols.pop()
        for n in range(6):                       # n unidades valen n veces el precio unitario
            assert f.subs(v, n) == sum([k] * n)

ejercicio_manual(
    id=nid(), tipo="conceptual", dificultad=1, fuente=f"{FUENTE} 3",
    enunciado=r"¿Es $f(x) = k$, siendo $k$ un número real cualquiera, una función de gráfica "
              r"lineal?",
    respuesta=r"Sí: es de la forma $f(x) = mx + b$ con $m = 0$ y $b = k$. Su gráfica es una recta "
              r"horizontal que corta el eje $y$ en $(0, k)$; su pendiente es $0$ (función "
              r"constante).", **COMUN)

ejercicio_manual(
    id=nid(), tipo="conceptual", dificultad=1, fuente=f"{FUENTE} 4",
    enunciado=r"¿Cuántos puntos como mínimo se necesitan para graficar una función lineal?",
    respuesta=r"Dos: por dos puntos distintos pasa una única recta. (Un tercer punto sirve para "
              r"comprobar que no hubo errores en los cálculos.)", **COMUN)

# ---------- 5. Cortes con los ejes ----------
# (literal, ecuación, var. horizontal, var. vertical, nombre del eje vertical,
#  corte con el eje horizontal (None si no hay), corte con el eje vertical, otro punto, notas, LaTeX)
E5 = [("a", "f(x) = 4x + 5", "x", "y", "y", Q(-5, 4), 5, None,
       "En el módulo aparece «f(x) = 4 + 5», sin la x (sería la constante 9, y el literal b ya es "
       "una constante); se corrigió a f(x) = 4x + 5.", None),
      ("b", "f(x) = 7", "x", "y", "y", None, 7, None, None, None),
      ("c", "10 - x = 3y", "x", "y", "y", 10, Q(10, 3), None, None, None),
      ("d", "x = 11 - 3y", "x", "y", "y", 11, Q(11, 3), None, None, None),
      ("e", "y = -8x - 1/2", "x", "y", "y", Q(-1, 16), Q(-1, 2), None, None, None),
      ("f", "4x - 2y = 6", "x", "y", "y", Q(3, 2), -3, None, None, None),
      ("g", "m/6 = 2y/3", "m", "y", "y", 0, 0, (4, 1), None, None),
      ("h", "5x + 3y = 2", "x", "y", "y", Q(2, 5), Q(2, 3), None, None, None),
      ("i", "f(t) = 3 - 5t", "t", "y", "f", Q(3, 5), 3, None, None, None),
      ("j", "a = 5b", "b", "a", "a", 0, 0, (1, 5), None, None),
      ("k", "4 = 8y - 6x", "x", "y", "y", Q(-2, 3), Q(1, 2), None, None, None),
      ("l", "-1 = -3a - 8b", "a", "b", "b", Q(1, 3), Q(1, 8), None, None, None),
      ("m", "s = -13t + 5", "t", "s", "S", Q(5, 13), 5, None, None, "S = -13t + 5"),
      ("n", "(2/5)x - 7y = 1", "x", "y", "y", Q(5, 2), Q(-1, 7), None, None, None),
      ("o", "n = 6x - 0.5", "x", "n", "n", Q(1, 12), Q(-1, 2), None, None, None),
      ("p", "m = (3/4)n + 2", "n", "m", "m", Q(-8, 3), 2, None, None, None)]
for lit, s, h, v, vn, ch, cv, otro, notas, ltx in E5:
    ejes = "" if (h, vn) == ("x", "y") else \
        f" (ubica ${h}$ en el eje horizontal y ${vn}$ en el vertical)"
    if ch is None:
        resp = (f"No corta el eje ${h}$ (es la recta horizontal ${vn} = {cv}$); corta el eje "
                f"${vn}$ en ${pt(0, cv)}$. Se traza la recta horizontal que pasa por ese punto.")
    elif otro:
        resp = (f"Corta los dos ejes en el origen $(0, 0)$. Para graficarla hace falta otro "
                f"punto, por ejemplo ${pt(*otro)}$; se traza la recta que pasa por los dos.")
    else:
        resp = (f"Corta el eje ${h}$ en ${pt(ch, 0)}$ y el eje ${vn}$ en ${pt(0, cv)}$; se traza "
                f"la recta que pasa por esos dos puntos.")
    extra = dict(notas=notas) if notas else {}

    @ejercicio(id=nid(), tipo="calculo", dificultad=2 if ejes or ch is None else 1,
               fuente=f"{FUENTE} 5{lit}", respuesta=resp, **extra, **COMUN,
               enunciado=f"Encuentra los puntos de intersección de la recta "
                         f"${ltx or eqtex(s)}$ con los ejes{ejes} y, con base en ellos, "
                         f"grafícala.")
    def _(s=s, h=h, v=v, ch=ch, cv=cv, otro=otro):
        H, V, L = expresion(h), expresion(v), ecuacion(s)
        esperado = S.EmptySet if ch is None else FiniteSet(ch)
        assert solveset(L.subs(V, 0), H, S.Reals) == esperado
        assert solveset(L.subs(H, 0), V, S.Reals) == FiniteSet(cv)
        if otro:
            assert otro != (0, 0) and L.subs({H: otro[0], V: otro[1]}) == 0

# ---------- 6. Forma y = mx + b y pendiente ----------
E6 = [("a", "6x - 8y = 1", Q(3, 4), Q(-1, 8)), ("b", "7y = 6 - x", Q(-1, 7), Q(6, 7)),
      ("c", "5x - 7y = 2", Q(5, 7), Q(-2, 7)), ("d", "0 = 15 - 9x - 4y", Q(-9, 4), Q(15, 4)),
      ("e", "5x - y = 2", 5, -2), ("f", "4x - y = 8", 4, -8),
      ("g", "2x - 7y = 10", Q(2, 7), Q(-10, 7)), ("h", "3y = -4x + 5", Q(-4, 3), Q(5, 3))]
for lit, s, m, b in E6:
    @ejercicio(id=nid(), tipo="calculo", dificultad=1 if Q(m).q == 1 else 2,
               fuente=f"{FUENTE} 6{lit}",
               enunciado=f"Expresa ${eqtex(s)}$ en la forma $y = mx + b$, halla su pendiente y "
                         f"traza su gráfica.",
               respuesta=f"${ymxb(m, b)}$; pendiente $m = {fr(m)}$. La recta corta el eje $y$ en "
                         f"${pt(0, b)}$.", **COMUN)
    def _(s=s, m=m, b=b):
        assert simplify(despejar_y(s) - (m * x + b)) == 0

# ---------- 7 y 8. Pendiente por dos puntos ----------
E7 = [("7a", (2, 5), (6, 10), Q(5, 4)), ("7b", (5, 6), (-6, -5), 1), ("7c", (6, 0), (7, -6), -6),
      ("7d", (0, -6), (-10, 0), Q(-3, 5)), ("7e", (Q(1, 2), 5), (7, 11), Q(12, 13)),
      ("7f", (Q(5, 2), Q(9, 2)), (Q(1, 2), 5), Q(-1, 4)),
      ("8a", (0, 0), (5, 8), Q(8, 5)), ("8b", (0, 0), (-1, 13), -13),
      ("8c", (0, 0), (-5, -6), Q(6, 5)), ("8d", (0, 0), (10, 10), 1), ("8e", (0, 0), (3, 9), 3),
      ("8f", (0, 0), (9, -1), Q(-1, 9)), ("8g", (0, 0), (Q(-8, 5), Q(9, 2)), Q(-45, 16)),
      ("8h", (0, 0), (Q(1, 7), Q(-6, 11)), Q(-42, 11))]
for lit, P, R, m in E7:
    if lit.startswith("7"):
        enun = f"Halla la pendiente de la recta que pasa por los puntos ${pt(*P)}$ y ${pt(*R)}$."
    else:
        enun = f"Calcula la pendiente de la recta que pasa por el origen $(0, 0)$ y por ${pt(*R)}$."
    dif = 1 if all(Q(c).q == 1 for c in P + R) else 2
    extra = dict(notas="El texto alternativo del módulo dice «6 onceavos» sin el signo; se deja el "
                       "signo menos de la fórmula impresa.") if lit == "8h" else {}

    @ejercicio(id=nid(), tipo="calculo", dificultad=dif, fuente=f"{FUENTE} {lit}", enunciado=enun,
               respuesta=f"$m = {fr(m)}$.", **extra, **COMUN)
    def _(P=P, R=R, m=m):
        assert Q(R[1] - P[1]) / (R[0] - P[0]) == m

# ---------- 9. Ecuación de la recta por dos puntos; 10. paralela y perpendicular a cada una ----------
E9 = [("a", (5, 3), (2, 8), Q(-5, 3), Q(34, 3)), ("b", (4, -4), (-8, 8), -1, 0),
      ("c", (0, -5), (4, Q(1, 2)), Q(11, 8), -5), ("d", (-9, 9), (3, -2), Q(-11, 12), Q(3, 4)),
      ("e", (2, Q(5, 2)), (0, 0), Q(5, 4), 0), ("f", (Q(1, 7), 2), (-2, 6), Q(-28, 15), Q(34, 15)),
      ("g", (-4, -2), (-1, 0), Q(2, 3), Q(2, 3)), ("h", (10, -6), (-2, -7), Q(1, 12), Q(-41, 6)),
      ("i", (-1, -2), (-3, -4), 1, -1)]
for lit, P, R, m, b in E9:
    @ejercicio(id=nid(), tipo="calculo", dificultad=2, fuente=f"{FUENTE} 9{lit}",
               enunciado=f"Encuentra la ecuación de la recta que pasa por ${pt(*P)}$ y ${pt(*R)}$.",
               respuesta=f"${ymxb(m, b)}$ (pendiente ${fr(m)}$).", **COMUN)
    def _(P=P, R=R, m=m, b=b):
        for X, Y in (P, R):
            assert Q(m) * X + b == Y

for lit, P, R, m, b in E9:
    bp = 0 if b != 0 else 1
    mp = -1 / Q(m)

    @ejercicio(id=nid(), tipo="calculo", dificultad=2, fuente=f"{FUENTE} 10 (sobre 9{lit})",
               enunciado=f"Encuentra la ecuación de una recta paralela y la de una recta "
                         f"perpendicular a la recta ${ymxb(m, b)}$ (la que pasa por ${pt(*P)}$ y "
                         f"${pt(*R)}$).",
               respuesta=f"Por ejemplo, paralela: ${ymxb(m, bp)}$ (misma pendiente, otro corte con "
                         f"el eje $y$); perpendicular: ${ymxb(mp, 0)}$ (pendiente "
                         f"$-\\frac{{1}}{{m}} = {fr(mp)}$). Sirve cualquier recta con esas "
                         f"pendientes.", **COMUN)
    def _(m=m, b=b, bp=bp, mp=mp):
        assert bp != b and Q(m) * mp == -1

# ---------- 11. Transformar entre y = mx + b y Ax + By + C = 0 ----------
E11 = [("a", "6x - 2y = -1", "y = 3x + 1/2"), ("b", "x - 8y = -5", "y = (1/8)x + 5/8"),
       ("c", "5x + 7y - 1 = 0", "y = -(5/7)x + 1/7"), ("d", "y = 8 - 3x", "3x + y - 8 = 0"),
       ("e", "5 + 9x - 3y = 2", "y = 3x + 1"), ("f", "8x - 6y + 4 = 0", "y = (4/3)x + 2/3"),
       ("g", "f(x) = 4x - 6", "4x - y - 6 = 0"), ("h", "f(x) = (5 - x)/6", "x + 6y - 5 = 0"),
       ("i", "(2/5)x - (1/2)y = 1", "y = (4/5)x - 2"), ("j", "f(x) = (1/2)x - 7", "x - 2y - 14 = 0"),
       ("k", "(y + 3)/2 = x", "y = 2x - 3"), ("l", "x - (1/5)y + 3 = 0", "y = 5x + 15")]
for lit, s, r in E11:
    forma = "$Ax + By + C = 0$" if r.endswith("= 0") else "$y = mx + b$"

    @ejercicio(id=nid(), tipo="calculo", dificultad=2 if "/" in s else 1,
               fuente=f"{FUENTE} 11{lit}",
               enunciado=f"Transforma la ecuación ${eqtex(s)}$ a la forma {forma}.",
               respuesta=f"${eqtex(r)}$.", **COMUN)
    def _(s=s, r=r):
        assert simplify(despejar_y(s) - despejar_y(r)) == 0

# ---------- 12. Pendiente a partir de la gráfica (descrita por sus puntos) ----------
E12 = [("a", "$(2, 0)$, $(0, 1)$, $(-2, 2)$, $(-4, 3)$ y $(-6, 4)$", [(2, 0), (0, 1), (-2, 2), (-4, 3), (-6, 4)],
        Q(-1, 2)),
       ("b", "$(0, 0)$, $(1, 2)$, $(2, 4)$, $(3, 6)$ y $(4, 8)$", [(0, 0), (1, 2), (2, 4), (3, 6), (4, 8)], 2)]
for lit, texto, puntos, m in E12:
    @ejercicio(id=nid(), tipo="calculo", dificultad=1, fuente=f"{FUENTE} 12{lit}",
               enunciado=f"La gráfica de una función de gráfica lineal es la recta que pasa por los "
                         f"puntos {texto}. Halla su pendiente.",
               respuesta=f"$m = {fr(m)}$.", **COMUN)
    def _(puntos=puntos, m=m):
        (x0, y0) = puntos[0]
        assert all(Q(Y - y0) / (X - x0) == m for X, Y in puntos[1:])

# ---------- 13. ¿Paralelas o perpendiculares? ----------
E13 = [("a", "4x + 5y = 1", "4x + 5y = 0", "paralelas",
        r"Paralelas: las dos tienen pendiente $-\frac{4}{5}$ y distinto corte con el eje $y$."),
       ("b", "y = 4x + 1", "5 - 4x + y = 0", "paralelas",
        r"Paralelas: la segunda es $y = 4x - 5$; las dos tienen pendiente $4$."),
       ("c", "y = 5", "x = 4", "perpendiculares",
        r"Perpendiculares: una es horizontal y la otra vertical."),
       ("d", "2x + 3y = -2", "3x - y = 4", "ninguna",
        r"Ni paralelas ni perpendiculares: las pendientes son $-\frac{2}{3}$ y $3$, distintas, y "
        r"su producto es $-2 \neq -1$; se cortan sin formar ángulo recto."),
       ("e", "y = 2x", "f(x) = 5 - x", "ninguna",
        r"Ni paralelas ni perpendiculares: pendientes $2$ y $-1$, producto $-2 \neq -1$."),
       ("f", "y = 5 + 4x", "y = 8 - 4x", "ninguna",
        r"Ni paralelas ni perpendiculares: pendientes $4$ y $-4$, producto $-16 \neq -1$."),
       ("g", "(1/3)x + (2/7)y - 5 = 0", "y = (6/7)x - 7", "perpendiculares",
        r"Perpendiculares: la primera es $y = -\frac{7}{6}x + \frac{35}{2}$ y "
        r"$-\frac{7}{6} \cdot \frac{6}{7} = -1$."),
       ("h", "(y - 4)/4 = x/3", "3y - 18 = 4x", "paralelas",
        r"Paralelas: son $y = \frac{4}{3}x + 4$ y $y = \frac{4}{3}x + 6$.")]
for lit, s1, s2, clase, resp in E13:
    @ejercicio(id=nid(), tipo="calculo", dificultad=2, fuente=f"{FUENTE} 13{lit}",
               enunciado=f"Grafica las rectas ${eqtex(s1)}$ y ${eqtex(s2)}$ y determina si son "
                         f"paralelas, perpendiculares o ninguna de las dos.",
               respuesta=resp, **COMUN)
    def _(s1=s1, s2=s2, clase=clase):
        (A1, B1, C1), (A2, B2, C2) = abc(s1), abc(s2)
        if A1 * B2 - A2 * B1 == 0:
            assert (A1 * C2 - A2 * C1, B1 * C2 - B2 * C1) != (0, 0)   # no es la misma recta
            calculada = "paralelas"
        elif A1 * A2 + B1 * B2 == 0:
            calculada = "perpendiculares"
        else:
            calculada = "ninguna"
        assert calculada == clase

# ---------- 14. Paralela y perpendicular a una recta dada ----------
E14 = [("a", "2 + 6x - 5y = 0", "y = (6/5)x + 2/5", "y = (6/5)x", "y = -(5/6)x"),
       ("b", "x + 6y - 1 = 0", "y = -(1/6)x + 1/6", "y = -(1/6)x", "y = 6x"),
       ("c", "5x - 3y = 4", "y = (5/3)x - 4/3", "y = (5/3)x", "y = -(3/5)x"),
       ("d", "10 + 2x = y", "y = 2x + 10", "y = 2x", "y = -(1/2)x"),
       ("e", "f(x) = 9 + x", "y = x + 9", "y = x", "y = -x"),
       ("f", "4 + y = x", "y = x - 4", "y = x + 2", "y = -x + 1"),
       ("g", "f(x) = 5", "y = 5", "y = 1", "x = 0"),
       ("h", "4 + x = y", "y = x + 4", "y = x + 1", "y = -x + 4"),
       ("i", "y = (3/5)x - 1", "y = (3/5)x - 1", "y = (3/5)x + 2", "y = -(5/3)x"),
       ("j", "(5/2)x + (1/3)y = 6x", "y = (21/2)x", "y = (21/2)x + 1", "y = -(2/21)x")]
for lit, s, forma, par, perp in E14:
    nota = (" (la recta vertical $x = 0$, el eje $y$; no es una función, pero es la recta "
            "perpendicular a una horizontal)") if perp == "x = 0" else ""
    dada = "" if eqtex(s) == eqtex(forma) else f"La recta dada es ${eqtex(forma)}$. "

    @ejercicio(id=nid(), tipo="calculo", dificultad=2, fuente=f"{FUENTE} 14{lit}",
               enunciado=f"Encuentra la ecuación de una recta paralela y la de una recta "
                         f"perpendicular a ${eqtex(s)}$. Grafica las tres rectas.",
               respuesta=f"{dada}Por ejemplo, paralela: ${eqtex(par)}$; "
                         f"perpendicular: ${eqtex(perp)}${nota}. Sirve cualquier recta con la "
                         f"misma pendiente (paralela) o con pendiente opuesta e inversa "
                         f"(perpendicular).", **COMUN)
    def _(s=s, forma=forma, par=par, perp=perp):
        A, B, C = abc(s)
        assert simplify(despejar_y(s) - despejar_y(forma)) == 0
        A1, B1, C1 = abc(par)
        assert A * B1 - A1 * B == 0 and (A * C1 - A1 * C, B * C1 - B1 * C) != (0, 0)
        A2, B2, _c = abc(perp)
        assert A * A2 + B * B2 == 0


# ---------- Prepárate para el ICFES ----------
COMUN_ICFES = dict(tema="función lineal", grados=[9], dba=["matematicas-9-8"])

ejercicio_manual(
    id=nid(), tipo="contexto", dificultad=1, fuente=f"{MODULO} — Prepárate para el ICFES, "
                                                     f"situación inicial",
    enunciado=r"El sueldo de un vendedor en un almacén de calzado depende del número de pares de "
              r"zapatos que vende en el mes; además tiene un ingreso básico de \$100\,000. ¿Qué "
              r"función representa su sueldo mensual?",
    respuesta=r"$S(n) = 100\,000 + kn$, donde $n$ es el número de pares vendidos en el mes y $k$ "
              r"lo que gana el vendedor por cada par (el enunciado no da ese valor).",
    notas="El módulo no dice cuánto gana el vendedor por par vendido; la respuesta queda en "
          "términos de k. Si se usa en clase, conviene dar un valor (p. ej., $5000 por par).",
    **COMUN_ICFES)

DETECTORES = (r"Un grupo de ingenieros quiere formar una compañía para producir detectores de "
              r"humo. Estiman que los costos variables por unidad (materia prima, mano de obra y "
              r"mercadeo) son de \$225\,000, que los costos fijos (formación, operación y "
              r"administración de la compañía, equipo y maquinaria) suman \$2\,500\,000\,000 y que "
              r"el precio de venta será de \$300\,000 por detector. ")
NOTA_DET = ("En el módulo, el costo variable por unidad es «$ 22 500 000», mayor que el precio de "
            "venta ($ 300 000): la empresa perdería con cada detector y nunca llegaría al "
            "equilibrio. Se corrigió a $225 000 (el problema clásico, a escala: costo variable "
            "22,50; fijos 250 000; precio 30).")
n = symbols("n", positive=True)


@ejercicio(id=nid(), tipo="contexto", dificultad=2, fuente=f"{ICFES} 1a", notas=NOTA_DET,
           enunciado=DETECTORES + r"Determina cuántos detectores se deben vender para que la "
                                  r"empresa esté en equilibrio (ni gane ni pierda).",
           respuesta=r"La utilidad es $U(n) = 300\,000n - (225\,000n + 2\,500\,000\,000) = "
                     r"75\,000n - 2\,500\,000\,000$. $U(n) = 0$ para $n = \num{33333,3}$…; como "
                     r"se venden unidades enteras, hay que vender $33\,334$ detectores (con "
                     r"$33\,333$ todavía hay una pequeña pérdida).", **COMUN_ICFES)
def _():
    U = 300000 * n - (225000 * n + 2500000000)
    assert solve(U, n) == [Q(100000, 3)]
    assert U.subs(n, 33333) < 0 < U.subs(n, 33334)


@ejercicio(id=nid(), tipo="contexto", dificultad=2, fuente=f"{ICFES} 1b", notas=NOTA_DET,
           enunciado=DETECTORES + r"Los datos de mercado indican que, con ese precio, se "
                                  r"venderían unos $30\,000$ detectores durante la vida del "
                                  r"proyecto. Determina la utilidad esperada con ese nivel de "
                                  r"producción.",
           respuesta=r"$U(30\,000) = 75\,000 \cdot 30\,000 - 2\,500\,000\,000 = "
                     r"-250\,000\,000$: una pérdida de \$250\,000\,000 (no se alcanza el punto de "
                     r"equilibrio).", **COMUN_ICFES)
def _():
    assert 300000 * 30000 - (225000 * 30000 + 2500000000) == -250000000


ejercicio_manual(
    id=nid(), tipo="contexto", dificultad=2, fuente=f"{ICFES} 2",
    enunciado=r"Construye una función que determine lo que queda cada mes del salario de tus "
              r"padres, teniendo en cuenta los ingresos adicionales y los gastos (mercado, "
              r"servicios, transporte, etc.).",
    respuesta=r"Respuesta abierta. Modelo: $U = (S + A) - (M + V + T + O)$, con $S$ el salario, "
              r"$A$ los ingresos adicionales, $M$ el mercado, $V$ los servicios, $T$ el "
              r"transporte y $O$ otros gastos, todo en pesos al mes. Si algún gasto depende de una "
              r"cantidad (p. ej. $T = 2\,950t$ con $t$ pasajes), la función queda lineal en esa "
              r"variable.", **COMUN_ICFES)

TRES = (r"Una compañía produce tres productos, que se venden a \$100, \$150 y \$85, "
        r"respectivamente. Cada unidad necesita $\num{2,5}$; $\num{3,5}$ y $2$ horas de mano de "
        r"obra, respectivamente; la mano de obra cuesta \$30 por hora y los costos fijos anuales "
        r"son de \$500\,000. Sean $x$, $y$, $z$ las unidades vendidas de cada producto. ")
a, b, c = symbols("x y z", nonnegative=True)
INGRESO = 100 * a + 150 * b + 85 * c
COSTO = 30 * (Q(5, 2) * a + Q(7, 2) * b + 2 * c) + 500000


@ejercicio(id=nid(), tipo="contexto", dificultad=2, fuente=f"{ICFES} 3a",
           enunciado=TRES + r"Construye la función de ingresos totales por las ventas de los tres "
                            r"productos.",
           respuesta=r"$I(x, y, z) = 100x + 150y + 85z$.", **COMUN_ICFES)
def _():
    assert INGRESO.subs({a: 1, b: 0, c: 0}) == 100 and INGRESO.subs({a: 0, b: 2, c: 1}) == 385


@ejercicio(id=nid(), tipo="contexto", dificultad=2, fuente=f"{ICFES} 3b",
           enunciado=TRES + r"Determina la función de costo anual de la producción de los tres "
                            r"productos.",
           respuesta=r"$C(x, y, z) = 30(\num{2,5}x + \num{3,5}y + 2z) + 500\,000 = "
                     r"75x + 105y + 60z + 500\,000$.", **COMUN_ICFES)
def _():
    assert (COSTO - (75 * a + 105 * b + 60 * c + 500000)).expand() == 0


@ejercicio(id=nid(), tipo="contexto", dificultad=2, fuente=f"{ICFES} 3c",
           enunciado=TRES + r"Determina la función de utilidad de los tres productos.",
           respuesta=r"$U = I - C = 25x + 45y + 25z - 500\,000$.", **COMUN_ICFES)
def _():
    assert (INGRESO - COSTO - (25 * a + 45 * b + 25 * c - 500000)).expand() == 0


@ejercicio(id=nid(), tipo="contexto", dificultad=2, fuente=f"{ICFES} 3d",
           enunciado=TRES + r"¿Cuál es la utilidad anual si se venden $20\,000$, $10\,000$ y "
                            r"$30\,000$ unidades, respectivamente, de cada producto?",
           respuesta=r"$U = 25(20\,000) + 45(10\,000) + 25(30\,000) - 500\,000 = \$1\,200\,000$.",
           **COMUN_ICFES)
def _():
    assert (INGRESO - COSTO).subs({a: 20000, b: 10000, c: 30000}) == 1200000
