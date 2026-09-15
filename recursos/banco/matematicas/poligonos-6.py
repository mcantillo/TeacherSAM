"""Banco de ejercicios — Matemáticas (Geometría 6°) — Polígonos: elementos y diagonales.
Escritos para la guía de Geometría 6°, trimestre I («La geometría del fútbol»), desde el DBA 6 de
grado 6 y el Tema 4 del módulo de Geometría (Quintero Palomino). El banco no tenía ningún
ejercicio de polígonos de 6°; regla de la docente del 2026-09-15: solo lo mínimo que falta.
Error encontrado en el recurso: en «Triangulación de polígonos» dice «n − 2 diagonales que partan
de un mismo vértice»; son n − 3 diagonales, que forman n − 2 triángulos.
Balón Telstar (1970): 12 pentágonos y 20 hexágonos (adidas, https://news.adidas.com/timeline/
how-adidas-has-shaped-the-history-of-world-cup-balls-from-1970-to-the-present-day/s/
012334d5-aee6-4153-a1dd-0fb0085c14a5).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/poligonos-6.py
"""
from itertools import combinations

from sympy import Point, RegularPolygon

from ejercicios import ejercicio

FUENTE = ("propio (guía Geometría 6°, trimestre I), desde el DBA 6 de grado 6 y el módulo de "
          "Geometría (Quintero Palomino), Tema 4")
COMUN = dict(tema="polígonos", grados=[6], dba=["matematicas-6-6"])


@ejercicio(id="poligonos-6-001", tipo="calculo", dificultad=1, fuente=FUENTE,
           enunciado=r"Completa la tabla para el pentágono, el hexágono y el octágono: número de "
                     r"lados, número de vértices, diagonales que salen de un vértice y total de "
                     r"diagonales.",
           respuesta=r"Pentágono: 5, 5, 2, 5. Hexágono: 6, 6, 3, 9. Octágono: 8, 8, 5, 20. (De "
                     r"cada vértice salen $n - 3$ diagonales; en total son "
                     r"$\frac{n(n-3)}{2}$ porque cada diagonal se cuenta dos veces.)", **COMUN)
def _():
    for n, desde, total in ((5, 2, 5), (6, 3, 9), (8, 5, 20)):
        P = RegularPolygon(Point(0, 0), 1, n)
        V = P.vertices
        lados = {frozenset(s.points) for s in P.sides}
        diag = [c for c in combinations(V, 2) if frozenset(c) not in lados]
        assert len(diag) == total == n * (n - 3) // 2
        assert sum(1 for c in diag if V[0] in c) == desde == n - 3


@ejercicio(id="poligonos-6-005", tipo="contexto", dificultad=3, fuente=FUENTE,
           enunciado=r"El balón Telstar del Mundial de 1970 tenía 12 pentágonos y 20 hexágonos "
                     r"cosidos. a) ¿Cuántos lados suman todas las piezas? b) Cada costura une el "
                     r"lado de una pieza con el lado de otra: ¿cuántas costuras tiene el balón? "
                     r"c) En cada vértice del balón se juntan tres piezas: ¿cuántos vértices "
                     r"tiene?",
           respuesta=r"a) $12 \cdot 5 + 20 \cdot 6 = 180$ lados. b) $180 \div 2 = 90$ costuras. "
                     r"c) $180 \div 3 = 60$ vértices.",
           notas="Datos del balón: adidas (ver cabecera). Es un icosaedro truncado: 32 caras, "
                 "90 aristas, 60 vértices (Euler: 60 − 90 + 32 = 2).", **COMUN)
def _():
    lados = 12 * 5 + 20 * 6
    costuras, vertices = lados // 2, lados // 3
    assert (lados, costuras, vertices) == (180, 90, 60)
    assert vertices - costuras + (12 + 20) == 2          # Euler, comprobación independiente
