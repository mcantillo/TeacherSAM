"""Banco de ejercicios — Geometría 9° — Teorema de Pitágoras para medir longitudes.
Fuente: módulo de Geometría de las Guías de Apoyo (Adriana Quintero Palomino), Tema 3; se lee en
recursos/matematicas/Guías pedagógicas Matemáticas/markdown/Modulo_Matematicas_Geometria.md
DBA 5 de 9° (Pitágoras para proponer y justificar estrategias de medición y cálculo de
longitudes). También sirven en 8° (DBA 7). Los literales 1a–y y 2a–t están en pitagoras-8.py.
El módulo 9° (funciones, sistemas, función cuadrática) no tiene ejercicios de Geometría: su
Tema 1 (pendiente, rectas paralelas y perpendiculares) queda para Álgebra.
En el banco no había ejercicios de este tema: nada duplicado.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/pitagoras-9.py
"""
from sympy import N, Point, Polygon, simplify, sqrt, symbols
from sympy.physics import units as u

from ejercicios import ejercicio

FUENTE = ("módulo de Geometría (Quintero Palomino), Tema 3: Teorema de Pitágoras — "
          "Practica lo aprendido")
COMUN = dict(tema="teorema de Pitágoras", grados=[9], dba=["matematicas-9-5"])


@ejercicio(id="pitagoras-9-001", tipo="argumentacion", dificultad=2, fuente=f"{FUENTE} 3",
           enunciado=r"¿Qué longitudes irracionales puedes obtener al dibujar triángulos "
                     r"rectángulos que tengan dos lados de $9$~cm y $7$~cm?",
           respuesta=r"Hay dos casos. Si $9$ y $7$ son los catetos, la hipotenusa mide "
                     r"$\sqrt{81 + 49} = \sqrt{130} \approx \num{11,40}$~cm. Si $9$ es la "
                     r"hipotenusa y $7$ un cateto, el otro cateto mide $\sqrt{81 - 49} = \sqrt{32} "
                     r"= 4\sqrt{2} \approx \num{5,66}$~cm. Las dos son irracionales.",
           notas="En el módulo: «con lados de longitudes 9 cm y 7 cm» y «distancias»; se precisó "
                 "«dos lados» y «longitudes».", **COMUN)
def _():
    hip, cat = sqrt(9**2 + 7**2), sqrt(9**2 - 7**2)
    assert hip == sqrt(130) and cat == 4 * sqrt(2)
    assert not hip.is_rational and not cat.is_rational
    assert abs(N(hip) - 11.40) < 0.005 and abs(N(cat) - 5.66) < 0.005


# 4.–6. Diagonal de un cuadrado: (n, literal, lado, respuesta, aproximación)
x = symbols("x", positive=True)
CUADRADOS = [(2, "4", 7, 7 * sqrt(2), r" \approx \num{9,90}", 9.90),
             (3, "5", 10, 10 * sqrt(2), r" \approx \num{14,14}", 14.14),
             (4, "6", x, x * sqrt(2), "", None)]
for n, literal, lado, diag, aprox, valor in CUADRADOS:
    lado_tex = "x" if lado is x else str(lado)

    @ejercicio(id=f"pitagoras-9-{n:03d}", tipo="calculo", dificultad=1 if valor else 2,
               fuente=f"{FUENTE} {literal}",
               enunciado=f"¿Cuánto mide la diagonal de un cuadrado de lado ${lado_tex}$~cm?",
               respuesta=f"$\\sqrt{{{lado_tex}^2 + {lado_tex}^2}} = "
                         f"{lado_tex}\\sqrt{{2}}{aprox}$~cm.", **COMUN)
    def _(lado=lado, diag=diag, valor=valor):
        cuadrado = Polygon(Point(0, 0), Point(lado, 0), Point(lado, lado), Point(0, lado))
        assert simplify(Point(0, 0).distance(Point(lado, lado)) - diag) == 0
        assert simplify(cuadrado.area - lado**2) == 0
        if valor:
            assert abs(N(diag) - valor) < 0.005


@ejercicio(id="pitagoras-9-005", tipo="calculo", dificultad=1, fuente=f"{FUENTE} 7",
           enunciado=r"¿Cuánto mide la diagonal de un rectángulo de base $7$~cm y altura $6$~cm?",
           respuesta=r"$\sqrt{7^2 + 6^2} = \sqrt{85} \approx \num{9,22}$~cm.", **COMUN)
def _():
    d = Point(0, 0).distance(Point(7, 6))
    assert d == sqrt(85) and abs(N(d) - 9.22) < 0.005


@ejercicio(id="pitagoras-9-006", tipo="calculo", dificultad=2, fuente=f"{FUENTE} 8",
           enunciado=r"¿Cuánto mide la diagonal de un rectángulo de base $10$~cm y área "
                     r"$50$~cm$^2$?",
           respuesta=r"La altura es $\frac{50}{10} = 5$~cm y la diagonal "
                     r"$\sqrt{10^2 + 5^2} = \sqrt{125} = 5\sqrt{5} \approx \num{11,18}$~cm.",
           **COMUN)
def _():
    altura = u.convert_to(50 * u.centimeter**2 / (10 * u.centimeter), u.centimeter)
    assert altura == 5 * u.centimeter
    d = Point(0, 0).distance(Point(10, 5))
    assert d == 5 * sqrt(5) and abs(N(d) - 11.18) < 0.005
