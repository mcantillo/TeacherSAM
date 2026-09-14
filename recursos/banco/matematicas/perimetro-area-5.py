"""Banco de ejercicios — Matemáticas (Geometría 5°) — Perímetro, área y área total.
Fuente: módulo de Matemáticas 5° de las Guías de Apoyo; ejercicios de medición que aparecen
sueltos en prácticas de otros temas; se lee en
recursos/matematicas/Guías pedagógicas Matemáticas/markdown/05 - Modulo_Matematicas_Quinto.md
No se incluyó el 6 de «Multiplicación de números mixtos» (ángulo w del paralelogramo): la
descripción de la figura no dice si w es vecino u opuesto al ángulo de 135°.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/perimetro-area-5.py
"""
from sympy import Rational, Symbol, solve
from sympy.physics.units import centimeter, meter

from ejercicios import ejercicio

M5 = "módulo 5° (Guías de Apoyo)"
COMUN = dict(tema="perímetro y área", grados=[5])
n = Symbol("n", positive=True)


@ejercicio(id="perimetro-area-5-001", tipo="calculo", dificultad=2, dba=["matematicas-5-4"],
           fuente=f"{M5}, Tema 5, Parejas ordenadas y distancias — Práctica lo aprendido 14",
           enunciado=r"Una caja con forma de prisma rectangular mide 5 cm de largo, \num{4,5} cm "
                     r"de profundidad y \num{3,5} cm de altura. Describe cómo se calcula su área "
                     r"total y luego calcúlala.",
           respuesta=r"Se suman las áreas de las 6 caras, que son 3 pares de rectángulos iguales: "
                     r"$2(5 \times \num{4,5}) + 2(5 \times \num{3,5}) + 2(\num{4,5} \times "
                     r"\num{3,5}) = 45 + 35 + \num{31,5} = \num{111,5}$ cm$^2$.",
           notas="El módulo da las medidas en una figura; se escribieron en el enunciado.", **COMUN)
def _():
    a, b, c = 5 * centimeter, Rational(9, 2) * centimeter, Rational(7, 2) * centimeter
    assert 2 * (a * b + a * c + b * c) == Rational(223, 2) * centimeter**2


@ejercicio(id="perimetro-area-5-002", tipo="calculo", dificultad=2, dba=["matematicas-5-5"],
           fuente=f"{M5}, Tema 3, Nociones de división de fracciones — Práctica lo aprendido 9",
           enunciado=r"Un polígono regular tiene un perímetro de 8 unidades. Si cada lado mide "
                     r"$\frac{4}{5}$ de unidad, ¿cuántos lados tiene el polígono?",
           respuesta=r"$8 \div \frac{4}{5} = 10$: tiene 10 lados (es un decágono).", **COMUN)
def _():
    assert solve(n * Rational(4, 5) - 8, n) == [10]


@ejercicio(id="perimetro-area-5-003", tipo="calculo", dificultad=1, dba=["matematicas-5-5"],
           fuente=f"{M5}, Tema 4, Patrones y ecuaciones — Práctica lo aprendido 9",
           enunciado=r"Un triángulo isósceles tiene una base de 12 cm; uno de los otros lados "
                     r"mide $x$ y el otro mide 18 cm. ¿Cuál es el perímetro del triángulo?",
           respuesta=r"Los dos lados que no son la base son iguales, así que $x = 18$ cm y el "
                     r"perímetro es $12 + 18 + 18 = 48$ cm.",
           notas="El módulo no da unidades; se usaron centímetros.", **COMUN)
def _():
    lados = [12, 18, 18]
    assert 2 * max(lados) < sum(lados)          # el triángulo existe
    assert sum(lados) == 48


@ejercicio(id="perimetro-area-5-004", tipo="contexto", dificultad=3, dba=["matematicas-5-5"],
           fuente=f"{M5}, Tema 4, Usar tablas de razones — Práctica lo aprendido 13",
           enunciado=r"Jorge quiere dividir su jardín rectangular de $10\frac{1}{2}$ m por "
                     r"$7\frac{1}{4}$ m en 3 secciones de igual área. ¿Cuál es el área de cada "
                     r"sección?",
           respuesta=r"El jardín mide $\frac{21}{2} \times \frac{29}{4} = \frac{609}{8} = "
                     r"76\frac{1}{8}$ m$^2$; cada sección mide $\frac{609}{8} \div 3 = "
                     r"\frac{203}{8} = 25\frac{3}{8}$ m$^2$ (\num{25,375} m$^2$).",
           notas="Se añadió «rectangular» y «de igual área», que el módulo da por supuestos.",
           **COMUN)
def _():
    area = Rational(21, 2) * meter * Rational(29, 4) * meter
    assert area == Rational(609, 8) * meter**2
    assert area / 3 == Rational(203, 8) * meter**2 == Rational(25375, 1000) * meter**2
