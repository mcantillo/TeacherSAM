"""Banco de ejercicios — Matemáticas (Geometría 6°) — Estimación y medición de ángulos.
Escrito para la guía de Geometría 6°, trimestre I («La geometría del fútbol»), desde el DBA 5 de
grado 6 (su ejemplo: estimar y medir los ángulos de tiro al arco). El banco no tenía ningún
ejercicio de estimar o medir ángulos (angulos-6 son demostraciones); regla de la docente del
2026-09-15: solo lo mínimo que el banco no cubre.
Medidas del arco: IFAB, Reglas de Juego, Regla 1 (https://www.theifab.com/laws/latest/the-field-of-play/).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/angulos-medicion-6.py
"""
from sympy import Point, Rational, atan2, deg

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
