"""Banco de ejercicios — Geometría 11° — Coordenadas cartesianas como modelo (guía del trimestre I, 2026-09-14).
DBA 6 de 11° (modelar en sistemas de coordenadas; comparar desde puntos de referencia distintos).
Ejercicios propios; no hay recurso de geometría analítica en recursos/. No usa
medicion-11-008…011 (Pitágoras, decisión pendiente 9°/11°).
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/coordenadas-11.py
"""
from sympy import Rational, sqrt
from sympy.geometry import Point

from ejercicios import ejercicio

PROPIO = "propio (guía Geometría 11°, trimestre I)"
COMUN = dict(tema="coordenadas cartesianas: distancia y punto medio", grados=[11],
             dba=["matematicas-11-6"], fuente=PROPIO)


@ejercicio(id="coordenadas-11-001", tipo="calculo", dificultad=1,
           enunciado=r"Halla la distancia y el punto medio entre $A(-3, 2)$ y $B(5, 8)$.",
           respuesta=r"$d = \sqrt{(5 + 3)^2 + (8 - 2)^2} = \sqrt{64 + 36} = 10$; punto medio "
                     r"$M\left(\frac{-3 + 5}{2}, \frac{2 + 8}{2}\right) = (1, 5)$.", **COMUN)
def _():
    A, B = Point(-3, 2), Point(5, 8)
    assert A.distance(B) == 10 and A.midpoint(B) == Point(1, 5)


@ejercicio(id="coordenadas-11-002", tipo="calculo", dificultad=1,
           enunciado=r"Halla la distancia y el punto medio de cada par de puntos: "
                     r"a) $(1, 1)$ y $(4, 5)$ \quad b) $(-2, 3)$ y $(4, -5)$ \quad c) $(0, 0)$ y $(3, 3)$",
           respuesta=r"a) $5$; $\left(\frac{5}{2}, 3\right)$. b) $10$; $(1, -1)$. "
                     r"c) $3\sqrt{2} \approx \num{4,24}$; $\left(\frac{3}{2}, \frac{3}{2}\right)$.",
           **COMUN)
def _():
    assert Point(1, 1).distance(Point(4, 5)) == 5 and Point(1, 1).midpoint(Point(4, 5)) == Point(Rational(5, 2), 3)
    assert Point(-2, 3).distance(Point(4, -5)) == 10 and Point(-2, 3).midpoint(Point(4, -5)) == Point(1, -1)
    assert Point(0, 0).distance(Point(3, 3)) == 3 * sqrt(2)
    assert Point(0, 0).midpoint(Point(3, 3)) == Point(Rational(3, 2), Rational(3, 2))


@ejercicio(id="coordenadas-11-003", tipo="contexto", dificultad=2,
           enunciado=r"En un mapa con unidades en kilómetros y origen en el puerto, una estación de "
                     r"radio está en $E(0, 0)$ y un barco en $B(30, 40)$. Un segundo mapa pone el "
                     r"origen en un faro que está $20$~km al este y $10$~km al norte del puerto. "
                     r"a) Escribe las coordenadas de $E$ y $B$ en el segundo mapa. b) Calcula la "
                     r"distancia $EB$ en los dos mapas. ¿Qué cambia y qué no cambia al mover el origen?",
           respuesta=r"a) Se resta $(20, 10)$: $E'(-20, -10)$ y $B'(10, 30)$. b) En los dos, "
                     r"$EB = 50$~km. Cambian las coordenadas, pero no las distancias ni la forma de "
                     r"las figuras: son propiedades de los objetos, no del sistema de referencia.",
           **COMUN)
def _():
    o = Point(20, 10)
    E, B = Point(0, 0), Point(30, 40)
    E2, B2 = E - o, B - o
    assert E2 == Point(-20, -10) and B2 == Point(10, 30)
    assert E.distance(B) == E2.distance(B2) == 50


@ejercicio(id="coordenadas-11-004", tipo="argumentacion", dificultad=2,
           enunciado=r"Demuestra con coordenadas que el triángulo de vértices $A(1, 1)$, $B(5, 4)$ y "
                     r"$C(2, 8)$ es isósceles y rectángulo.",
           respuesta=r"$AB = \sqrt{16 + 9} = 5$, $BC = \sqrt{9 + 16} = 5$ y $AC = \sqrt{1 + 49} = "
                     r"\sqrt{50}$. Es isósceles ($AB = BC$) y rectángulo en $B$, porque "
                     r"$AB^2 + BC^2 = 25 + 25 = 50 = AC^2$ (recíproco de Pitágoras).", **COMUN)
def _():
    A, B, C = Point(1, 1), Point(5, 4), Point(2, 8)
    assert A.distance(B) == B.distance(C) == 5 and A.distance(C) == sqrt(50)
    assert A.distance(B)**2 + B.distance(C)**2 == A.distance(C)**2


@ejercicio(id="coordenadas-11-005", tipo="contexto", dificultad=2,
           enunciado=r"Un dron de rescate sale del punto $(2, -1)$ y debe llegar a $(14, 4)$ "
                     r"(coordenadas en km). a) ¿Qué distancia recorre en línea recta? b) Debe "
                     r"reportarse a mitad de camino: ¿en qué punto? c) Si vuela a $52$~km/h, ¿cuántos "
                     r"minutos tarda?",
           respuesta=r"a) $\sqrt{12^2 + 5^2} = 13$~km. b) $(8; \num{1,5})$. "
                     r"c) $\frac{13}{52} = \num{0,25}$~h $= 15$~min.", **COMUN)
def _():
    P, Q = Point(2, -1), Point(14, 4)
    assert P.distance(Q) == 13 and P.midpoint(Q) == Point(8, Rational(3, 2))
    assert Rational(13, 52) * 60 == 15
