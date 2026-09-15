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
from sympy import Rational

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
