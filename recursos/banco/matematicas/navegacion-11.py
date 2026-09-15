"""Banco de ejercicios — Geometría 11° — Navegación hiperbólica (LORAN) y precisión (guía del trimestre I, 2026-09-15).
DBA 6 y DBA 4 de 11°. Excepción a «solo banco»: el banco no tenía NADA de navegación hiperbólica
(el hilo de la guía). Solo los dos mínimos: el cruce de dos hipérbolas (003) y precisión frente
a exactitud (005, evidencia del DBA 4). Modelo plano y simplificado: en LORAN real las
estaciones de una cadena comparten una «maestra» y la secundaria emite con un retraso conocido;
aquí cada par emite a la vez y sus hipérbolas están centradas. Rapidez de la señal: 0,3 km/µs
(c = 299 792 458 m/s, NIST).
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/navegacion-11.py
"""
from sympy import N, Rational, simplify, solve, sqrt, symbols
from sympy.geometry import Point

from ejercicios import ejercicio

PROPIO = "propio (guía Geometría 11°, trimestre I)"
COMUN = dict(tema="navegación hiperbólica", grados=[11], fuente=PROPIO,
             dba=["matematicas-11-6", "matematicas-11-4"])
V = Rational(3, 10)                     # km por microsegundo
x, y = symbols("x y", real=True)


@ejercicio(id="navegacion-11-003", tipo="contexto", dificultad=3,
           enunciado=r"Unidades: $100$~km. Un par de estaciones en $(\pm 5, 0)$ ubica al barco sobre "
                     r"$\frac{x^2}{9} - \frac{y^2}{16} = 1$, rama derecha; otro par en $(0, \pm 5)$ lo "
                     r"ubica sobre $\frac{y^2}{9} - \frac{x^2}{16} = 1$, rama superior. Halla la "
                     r"posición del barco.",
           respuesta=r"Restando las ecuaciones: $x^2\left(\frac{1}{9} + \frac{1}{16}\right) = "
                     r"y^2\left(\frac{1}{9} + \frac{1}{16}\right)$, así que $x = y$ (primer "
                     r"cuadrante). Entonces $x^2\left(\frac{1}{9} - \frac{1}{16}\right) = 1$, "
                     r"$x^2 = \frac{144}{7}$ y $x = y = \frac{12}{\sqrt{7}} \approx \num{4,54}$: el "
                     r"barco está en $(454, 454)$~km, aproximadamente.", **COMUN)
def _():
    sols = solve([x**2 / 9 - y**2 / 16 - 1, y**2 / 9 - x**2 / 16 - 1], [x, y], dict=True)
    buenas = [s for s in sols if s[x] > 0 and s[y] > 0]
    assert len(buenas) == 1
    s = buenas[0]
    assert simplify(s[x] - 12 / sqrt(7)) == 0 and simplify(s[y] - 12 / sqrt(7)) == 0
    assert abs(N(s[x]) - 4.54) < 0.005
    P = Point(s[x], s[y])
    assert simplify(P.distance(Point(-5, 0)) - P.distance(Point(5, 0)) - 6) == 0
    assert simplify(P.distance(Point(0, -5)) - P.distance(Point(0, 5)) - 6) == 0


@ejercicio(id="navegacion-11-005", tipo="contexto", dificultad=3,
           enunciado=r"Un receptor mide cuatro veces la diferencia de tiempos para el mismo barco "
                     r"quieto: $\num{400,2}$; $\num{399,8}$; $\num{400,1}$ y $\num{399,9}$~µs. a) Halla "
                     r"el promedio y la diferencia de distancias. b) ¿Cuánto varían las distancias "
                     r"entre la medida mayor y la menor? c) Después se descubre que el receptor tiene "
                     r"un retraso fijo de $5$~µs en todas sus medidas. ¿Las medidas eran precisas? "
                     r"¿Eran exactas? ¿Cuánto error produce el retraso?",
           respuesta=r"a) $\num{400,0}$~µs y $\num{0,3} \cdot 400 = 120$~km. b) $\num{0,4}$~µs, es "
                     r"decir, $\num{0,12}$~km $= 120$~m. c) Eran precisas (muy parecidas entre sí), "
                     r"pero no exactas: todas estaban corridas $5$~µs, que son "
                     r"$\num{1,5}$~km de error en la diferencia de distancias.", **COMUN)
def _():
    t = [Rational(s) for s in ("400.2", "399.8", "400.1", "399.9")]
    prom = sum(t) / 4
    assert prom == 400 and V * prom == 120
    assert (max(t) - min(t)) * V == Rational("0.12")
    assert V * 5 == Rational("1.5")
