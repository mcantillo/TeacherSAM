"""Banco de ejercicios — Matemáticas (Geometría 6°) — Estimación y medición de ángulos.
Escrito para la guía de Geometría 6°, trimestre I («La geometría del fútbol»), desde el DBA 5 de
grado 6 (su ejemplo: estimar y medir los ángulos de tiro al arco). El banco no tenía ningún
ejercicio de estimar o medir ángulos (angulos-6 son demostraciones); regla de la docente del
2026-09-15: solo lo mínimo que el banco no cubre.
Medidas del arco: IFAB, Reglas de Juego, Regla 1 (https://www.theifab.com/laws/latest/the-field-of-play/).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/angulos-medicion-6.py
"""
from sympy import Eq, Point, Rational, atan2, deg, solve, symbols

from ejercicios import ejercicio

FUENTE = "propio (guía Geometría 6°, trimestre I), desde el ejemplo del DBA 5 de grado 6"


def angulo_tiro(x, y):
    """Ángulo (en grados) con que se ve el arco desde (x, y); postes en (±3,66; 0) m."""
    p1, p2 = Point(Rational(366, 100), 0), Point(-Rational(366, 100), 0)
    a = atan2(p1.y - y, p1.x - x)
    b = atan2(p2.y - y, p2.x - x)
    return abs(float(deg(b - a)))


@ejercicio(id="angulos-medicion-6-004", tema="ángulos", grados=[6], dba=["matematicas-6-5"],
           tipo="contexto", dificultad=2, fuente=FUENTE,
           enunciado=r"El arco mide $\qty{7,32}{m}$ entre los postes. Dibuja a escala "
                     r"($\qty{1}{cm}$ por metro) el arco y tres jugadores: $A$ en el punto penal, "
                     r"a $\qty{11}{m}$ del centro del arco; $B$ en el borde del área, a "
                     r"$\qty{16,5}{m}$ del centro, de frente; $C$ a $\qty{11}{m}$ de la línea de "
                     r"meta pero corrido $\qty{9}{m}$ hacia un lado. Primero estima el ángulo de "
                     r"tiro de cada uno (el ángulo con vértice en el jugador y lados hacia los dos "
                     r"postes); luego mídelo con el transportador. ¿Quién tiene más ángulo para "
                     r"hacer gol?",
           respuesta=r"Aproximadamente $A \approx 37^\circ$, $B \approx 25^\circ$ y "
                     r"$C \approx 23^\circ$ (se aceptan medidas con $1^\circ$ o $2^\circ$ de "
                     r"diferencia). $A$ tiene el mayor ángulo: está más cerca y de frente. $C$, "
                     r"aunque está a la misma distancia de la línea de meta que $A$, ve el arco "
                     r"«de lado» y su ángulo es incluso menor que el de $B$.",
           notas="Adaptado del ejemplo del DBA 5 de 6° (tiro al arco). Medidas IFAB, Regla 1.")
def _():
    a, b, c = angulo_tiro(0, 11), angulo_tiro(0, Rational(33, 2)), angulo_tiro(9, 11)
    assert round(a) == 37 and round(b) == 25 and round(c) == 23
    assert a > b > c


# --- Añadidos el 2026-09-19 para el taller de la sesión 003 (semana 04) ---------------
# El banco no tenía más ejercicios de estimar y medir ángulos: solo el 004, que ya usa la
# guía. Estos cuatro sostienen el taller sin repetirlo.


@ejercicio(id="angulos-medicion-6-005", tema="ángulos", grados=[6], dba=["matematicas-6-5"],
           tipo="contexto", dificultad=1, fuente=FUENTE,
           enunciado=r"Antes de medir, Andrés estimó que un ángulo medía $50^\circ$. Al medirlo "
                     r"con el transportador le dio $62^\circ$. ¿De cuántos grados fue su error? "
                     r"Si en clase acordamos que una estimación sirve cuando se aleja menos de "
                     r"$10^\circ$ del valor medido, ¿la de Andrés sirve?",
           respuesta=r"El error es $62^\circ - 50^\circ = 12^\circ$. Como $12^\circ > 10^\circ$, "
                     r"la estimación no sirve según lo acordado: se quedó corto por poco más del "
                     r"margen. Conviene volver a estimar comparando con el ángulo recto.")
def _():
    error = abs(62 - 50)
    assert error == 12 and error > 10


@ejercicio(id="angulos-medicion-6-006", tema="ángulos", grados=[6], dba=["matematicas-6-5"],
           tipo="calculo", dificultad=1, fuente=FUENTE,
           enunciado=r"Sin usar transportador, y tomando el ángulo recto como referente, di "
                     r"cuánto mide cada ángulo: (a) la mitad de un recto; (b) un recto y medio; "
                     r"(c) dos tercios de un recto. Clasifica cada uno como agudo, recto u obtuso.",
           respuesta=r"(a) $\frac{90^\circ}{2} = 45^\circ$, agudo. (b) $90^\circ \cdot "
                     r"\frac{3}{2} = 135^\circ$, obtuso. (c) $90^\circ \cdot \frac{2}{3} = "
                     r"60^\circ$, agudo.")
def _():
    a, b, c = Rational(90, 2), 90 * Rational(3, 2), 90 * Rational(2, 3)
    assert (a, b, c) == (45, 135, 60)
    assert a < 90 and b > 90 and c < 90


@ejercicio(id="angulos-medicion-6-007", tema="ángulos", grados=[6], dba=["matematicas-6-5"],
           tipo="contexto", dificultad=2, fuente=FUENTE,
           enunciado=r"Dos jugadores están a la misma distancia de la línea de meta, "
                     r"$\qty{5,5}{m}$: $D$ está justo frente al centro del arco y $E$ está "
                     r"corrido $\qty{5,5}{m}$ hacia un lado. Dibuja a escala ($\qty{1}{cm}$ por "
                     r"metro), estima y luego mide el ángulo de tiro de cada uno. ¿Cuál de los "
                     r"dos tiene mejor ángulo, y por qué, si están a la misma distancia?",
           respuesta=r"$D \approx 67^\circ$ y $E \approx 41^\circ$ (se aceptan $1^\circ$ o "
                     r"$2^\circ$ de diferencia). $D$ tiene mucho mejor ángulo: estar a la misma "
                     r"distancia de la línea de meta no basta, porque $E$ ve el arco «de lado» y "
                     r"los dos postes le quedan casi alineados. Lo que importa es la posición "
                     r"frente al arco, no solo la distancia.",
           notas="Mismo montaje del 004 (postes en ±3,66 m, medidas IFAB), con la comparación "
                 "que ahí no se hace: misma distancia y ángulos muy distintos.")
def _():
    d, e = angulo_tiro(0, Rational(11, 2)), angulo_tiro(Rational(11, 2), Rational(11, 2))
    assert round(d) == 67 and round(e) == 41
    assert d > e


@ejercicio(id="angulos-medicion-6-008", tema="ángulos", grados=[6], dba=["matematicas-6-5"],
           tipo="calculo", dificultad=2, fuente=FUENTE,
           enunciado=r"Dos ángulos son suplementarios y uno mide el doble del otro. ¿Cuánto mide "
                     r"cada uno? Comprueba tu respuesta sumándolos.",
           respuesta=r"Si el menor mide $x$, el otro mide $2x$ y $x + 2x = 180^\circ$, luego "
                     r"$3x = 180^\circ$ y $x = 60^\circ$. Los ángulos miden $60^\circ$ y "
                     r"$120^\circ$, y en efecto $60^\circ + 120^\circ = 180^\circ$.")
def _():
    x = symbols("x", positive=True)
    sol = solve(Eq(x + 2 * x, 180), x)[0]
    assert sol == 60 and sol + 2 * sol == 180
