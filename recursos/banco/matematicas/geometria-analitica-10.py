"""Banco de ejercicios — Matemáticas (Geometría 10°) — Plano cartesiano, distancia y pendiente.
Fuente: redactados para la guía del trimestre I de Geometría 10° (2026-09-14); el curso no tiene
recurso aprobado en recursos/. Regla «reutilizar, no multiplicar» (2026-09-15): la guía reutiliza
plano-cartesiano-5, coordenadas-11, lugares-geometricos-11, funcion-lineal-9 y preguntas del
Icfes; aquí quedan solo los 4 que el banco no tenía (los ids que faltan se descartaron antes de
registrarse):
  002 — cuadrantes y ejes con coordenadas negativas (no hay uno verificado para secundaria);
  006 — Cali en el plano latitud–longitud (contexto del hilo);
  012 — 1° de latitud ≈ 111 km (contexto del hilo);
  030 — encuentra el error en el cálculo de la pendiente (funcion-lineal-9 no trae uno).
Datos reales: coordenadas de Cali 3°27′00″ N, 76°32′00″ O
(https://www.cali.gov.co/informatica/publicaciones/106104/geografia-de-cali/) y 1° de latitud
≈ 111 km (https://oceanservice.noaa.gov/facts/latitude.html).
La relación m = tan θ (ángulo de inclinación) queda en Trigonometría 10° (rectas-inclinacion-10.py).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/geometria-analitica-10.py
"""
from sympy import Rational, sqrt

from ejercicios import ejercicio

FUENTE = "redactado para la guía de Geometría 10°, trimestre I (2026-09-14)"
P = "geometria-analitica-10"
DBA = ["matematicas-10-5"]


def cuadrante(p):
    a, b = float(p[0]), float(p[1])
    if a == 0 and b == 0:
        return "origen"
    if a == 0:
        return "eje y"
    if b == 0:
        return "eje x"
    return {(1, 1): "I", (-1, 1): "II", (-1, -1): "III", (1, -1): "IV"}[(a > 0) - (a < 0), (b > 0) - (b < 0)]


def pendiente(p, q):
    if p[0] == q[0]:
        return None
    return Rational(q[1] - p[1], q[0] - p[0])


def reg(n, tema, enunciado, respuesta, tipo="calculo", dificultad=1, notas=None):
    meta = dict(id=f"{P}-{n:03d}", tema=tema, grados=[10], dba=DBA, tipo=tipo,
                dificultad=dificultad, fuente=FUENTE, enunciado=enunciado, respuesta=respuesta)
    if notas:
        meta["notas"] = notas
    return ejercicio(**meta)


@reg(2, "plano cartesiano",
     r"¿Dónde está cada punto: en qué cuadrante o sobre qué eje? $(-3, 5)$, $(4, -2)$, "
     r"$(0, -6)$, $(-1, -1)$, $(7, 0)$.",
     r"$(-3, 5)$: II; $(4, -2)$: IV; $(0, -6)$: eje $y$; $(-1, -1)$: III; $(7, 0)$: eje $x$.")
def _():
    assert [cuadrante(p) for p in [(-3, 5), (4, -2), (0, -6), (-1, -1), (7, 0)]] == \
        ["II", "IV", "eje y", "III", "eje x"]


@reg(6, "plano cartesiano",
     r"Según la Alcaldía, Cali está en $3^\circ 27'$ de latitud norte y $76^\circ 32'$ de "
     r"longitud oeste. Toma un plano en el que $x$ es la longitud (positiva al este) e $y$ "
     r"la latitud (positiva al norte), en grados. Escribe la ubicación de Cali como un par "
     r"ordenado con dos decimales y di en qué cuadrante queda.",
     r"$(-76{,}53;\ 3{,}45)$, en el cuadrante II (oeste y norte).", tipo="contexto", dificultad=2,
     notas="Dato de https://www.cali.gov.co/informatica/publicaciones/106104/geografia-de-cali/")
def _():
    lon = -(76 + Rational(32, 60))
    lat = 3 + Rational(27, 60)
    assert round(float(lon), 2) == -76.53 and round(float(lat), 2) == 3.45
    assert cuadrante((lon, lat)) == "II"


@reg(12, "distancia y punto medio",
     r"Cada grado de latitud equivale a unos $111$ km sobre la superficie de la Tierra. "
     r"Dos lugares están sobre el mismo meridiano: uno en $2^\circ 15'$ N y otro en "
     r"$3^\circ 45'$ N. ¿Aproximadamente qué distancia los separa en dirección norte–sur?",
     r"La diferencia es $1^\circ 30' = \num{1,5}^\circ$; $\num{1,5} \cdot 111 \approx \num{166,5}$ km.",
     tipo="contexto", notas="Dato: https://oceanservice.noaa.gov/facts/latitude.html")
def _():
    dif = (3 + Rational(45, 60)) - (2 + Rational(15, 60))
    assert dif == Rational(3, 2) and dif * 111 == Rational(333, 2)


@reg(30, "la recta",
     r"Sofía calculó la pendiente de la recta que pasa por $(1, 3)$ y $(4, 9)$ así: "
     r"$m = \frac{4 - 1}{9 - 3} = \frac{1}{2}$. Encuentra el error y corrígelo.",
     r"Invirtió el cociente: puso la diferencia de las $x$ arriba. Lo correcto es "
     r"$m = \frac{9 - 3}{4 - 1} = 2$.", tipo="encuentra-el-error")
def _():
    assert Rational(4 - 1, 9 - 3) == Rational(1, 2) != pendiente((1, 3), (4, 9)) == 2


# --- Añadidos el 2026-09-19 para la tarea de la sesión 003 (semana 04) ----------------
# La sesión deduce la fórmula de la distancia desde Pitágoras. El banco no tenía ejercicios
# de distancia entre dos puntos para 10°: coordenadas-11 y lugares-geometricos-11 ya los usa
# la guía, y plano-cartesiano-5 es de primaria.


def dist(p, q):
    return sqrt((q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2)


@reg(40, "distancia entre dos puntos",
     r"Calcula la distancia entre cada pareja de puntos y deja el resultado exacto: "
     r"(a) $A(2, 3)$ y $B(6, 6)$; (b) $C(-3, 2)$ y $D(5, -4)$; (c) $E(1, -2)$ y $F(7, 6)$.",
     r"(a) $\sqrt{4^2 + 3^2} = \sqrt{25} = 5$. (b) $\sqrt{8^2 + (-6)^2} = \sqrt{100} = 10$. "
     r"(c) $\sqrt{6^2 + 8^2} = \sqrt{100} = 10$. Los tres son ternas pitagóricas: "
     r"$3$-$4$-$5$, $6$-$8$-$10$ y $6$-$8$-$10$.")
def _():
    assert dist((2, 3), (6, 6)) == 5
    assert dist((-3, 2), (5, -4)) == 10
    assert dist((1, -2), (7, 6)) == 10


@reg(41, "distancia entre dos puntos",
     r"Los vértices de un triángulo son $P(1, 1)$, $Q(5, 1)$ y $R(3, 5)$. Calcula la longitud "
     r"de sus tres lados y decide si el triángulo es equilátero, isósceles o escaleno. "
     r"Justifica con los números, no con el dibujo.",
     r"$PQ = \sqrt{4^2 + 0^2} = 4$; $QR = \sqrt{(-2)^2 + 4^2} = \sqrt{20} = 2\sqrt{5}$; "
     r"$PR = \sqrt{2^2 + 4^2} = \sqrt{20} = 2\sqrt{5}$. Como $QR = PR \neq PQ$, el triángulo es "
     r"\textbf{isósceles}. Medir con regla sobre el dibujo no bastaría: $\sqrt{20} \approx "
     r"\num{4,47}$ se parece mucho a $4$.",
     tipo="argumentacion", dificultad=2,
     notas="El punto del ejercicio es que la fórmula decide lo que el ojo no distingue.")
def _():
    P_, Q_, R_ = (1, 1), (5, 1), (3, 5)
    pq, qr, pr = dist(P_, Q_), dist(Q_, R_), dist(P_, R_)
    assert pq == 4 and qr == pr == 2 * sqrt(5) and qr != pq


@reg(42, "distancia entre dos puntos",
     r"Un cuadrilátero tiene vértices $A(0, 0)$, $B(4, 3)$, $C(8, 0)$ y $D(4, -3)$. Calcula "
     r"$AB$, $BC$, $CD$ y $DA$. ¿Qué tienen en común los cuatro lados? ¿Basta eso para afirmar "
     r"que es un cuadrado? Calcula también las dos diagonales $AC$ y $BD$ y decide.",
     r"Los cuatro lados miden $5$: $AB = \sqrt{4^2 + 3^2} = 5$, y lo mismo $BC$, $CD$ y $DA$. "
     r"Tener los cuatro lados iguales lo hace un \textbf{rombo}, pero \emph{no} basta para decir "
     r"que es un cuadrado. Las diagonales lo resuelven: $AC = 8$ y $BD = 6$. En un cuadrado las "
     r"dos diagonales miden lo mismo, así que este rombo no es un cuadrado.",
     tipo="argumentacion", dificultad=3,
     notas="La comparación de diagonales prepara el criterio de perpendicularidad de la sesión "
           "siguiente. Con lados iguales y diagonales iguales sí sería un cuadrado.")
def _():
    A_, B_, C_, D_ = (0, 0), (4, 3), (8, 0), (4, -3)
    assert [dist(A_, B_), dist(B_, C_), dist(C_, D_), dist(D_, A_)] == [5, 5, 5, 5]
    assert dist(A_, C_) == 8 and dist(B_, D_) == 6 and dist(A_, C_) != dist(B_, D_)


@reg(43, "distancia entre dos puntos",
     r"Camila calculó así la distancia entre $M(-2, 5)$ y $N(4, -3)$: «$d = \sqrt{(4 - 2)^2 + "
     r"(-3 - 5)^2} = \sqrt{4 + 64} = \sqrt{68}$». Encuentra el error, corrígelo y explica en una "
     r"frase por qué el resultado correcto no cambia si se intercambian $M$ y $N$.",
     r"El error está en la resta de las abscisas: es $4 - (-2) = 6$, no $4 - 2 = 2$. Lo correcto "
     r"es $d = \sqrt{6^2 + (-8)^2} = \sqrt{36 + 64} = \sqrt{100} = 10$. Intercambiar los puntos "
     r"no cambia nada porque las diferencias solo cambian de signo y van elevadas al cuadrado.",
     tipo="argumentacion", dificultad=2)
def _():
    M_, N_ = (-2, 5), (4, -3)
    assert dist(M_, N_) == 10 and dist(N_, M_) == 10
    assert sqrt((4 - 2) ** 2 + (-3 - 5) ** 2) == 2 * sqrt(17)  # lo que le dio a Camila
