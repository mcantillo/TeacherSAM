"""Banco de ejercicios — Física 10° — Vectores: componentes, suma gráfica y por componentes,
fuerza neta.
Escritos para las sesiones 007 y 008 del trimestre I de Física 10° (semana 04, 2026-09-20). El
banco no tenía ningún ejercicio de vectores: cinematica-10 y leyes-newton-10 los usan pero no
los enseñan, y la guía solo trae el ejemplo resuelto de 30 N + 40 N perpendiculares.
DBA: naturales grado 10 · DBA 1 — Comprende que el reposo o el movimiento rectilíneo uniforme
se presentan cuando las fuerzas aplicadas sobre el sistema se anulan entre ellas, y que en
presencia de fuerzas resultantes no nulas se producen cambios de velocidad (la fuerza neta de
un sistema es la suma vectorial de las fuerzas).
Convención: magnitudes a una décima, ángulos a una décima de grado, medidos desde el eje +x
en sentido antihorario. Todo en métricas.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/fisica/vectores-10.py
"""
from math import atan2, cos, degrees, hypot, radians, sin

from ejercicios import ejercicio

PRE = "vectores-10"
FUENTE = "propio (Física 10°, trimestre I, sesiones 007 y 008)"
COMUN = dict(tema="vectores", grados=[10], dba=["naturales-10-1"])


def comp(magnitud, angulo_grados):
    """Componentes (x, y) de un vector dado por su magnitud y su ángulo con el eje +x."""
    a = radians(angulo_grados)
    return magnitud * cos(a), magnitud * sin(a)


def polar(x, y):
    """Magnitud y ángulo (en grados, desde +x, antihorario) de un vector dado por componentes."""
    return hypot(x, y), degrees(atan2(y, x))


@ejercicio(id=f"{PRE}-001", tipo="calculo", dificultad=1, fuente=FUENTE,
           enunciado=r"Una fuerza de \qty{50}{N} forma un ángulo de $37^\circ$ con el eje $x$ "
                     r"positivo. Calcula sus componentes $F_x$ y $F_y$, a una décima.",
           respuesta=r"$F_x = 50\cos 37^\circ \approx \qty{39,9}{N}$ y "
                     r"$F_y = 50\sen 37^\circ \approx \qty{30,1}{N}$. "
                     r"Comprobación: $\sqrt{39{,}9^2 + 30{,}1^2} \approx 50$.",
           **COMUN)
def _():
    x, y = comp(50, 37)
    assert round(x, 1) == 39.9 and round(y, 1) == 30.1
    assert round(hypot(x, y), 1) == 50.0


@ejercicio(id=f"{PRE}-002", tipo="calculo", dificultad=1, fuente=FUENTE,
           enunciado=r"Un vector tiene componentes $v_x = \qty{-6}{m/s}$ y "
                     r"$v_y = \qty{8}{m/s}$. Halla su magnitud y el ángulo que forma con el eje "
                     r"$x$ positivo (medido en sentido antihorario). ¿En qué cuadrante está?",
           respuesta=r"Magnitud: $\sqrt{(-6)^2 + 8^2} = \sqrt{100} = \qty{10}{m/s}$. "
                     r"Ángulo: $\arctg\frac{8}{-6}$ con la componente $x$ negativa y la $y$ "
                     r"positiva da $\approx 126{,}9^\circ$. Está en el \textbf{segundo "
                     r"cuadrante}. Si se usa la calculadora sin mirar los signos sale "
                     r"$-53{,}1^\circ$, que apunta justo al lado contrario.",
           notas="El punto del ejercicio es el cuadrante: la calculadora no lo sabe.",
           **COMUN)
def _():
    mag, ang = polar(-6, 8)
    assert round(mag, 1) == 10.0 and round(ang, 1) == 126.9
    assert round(degrees(atan2(-8, 6)), 1) == -53.1  # lo que sale si se ignoran los signos


@ejercicio(id=f"{PRE}-003", tipo="calculo", dificultad=2, fuente=FUENTE,
           enunciado=r"Sobre una caja actúan dos fuerzas perpendiculares: \qty{30}{N} hacia el "
                     r"este y \qty{40}{N} hacia el norte. Halla la fuerza neta (magnitud y "
                     r"dirección) y dibuja la suma con el método del paralelogramo.",
           respuesta=r"$F = \sqrt{30^2 + 40^2} = \sqrt{2500} = \qty{50}{N}$, y el ángulo con el "
                     r"este es $\arctg\frac{40}{30} \approx 53{,}1^\circ$ hacia el norte. "
                     r"Es el triángulo $3$-$4$-$5$ de siempre, en newtons.",
           **COMUN)
def _():
    mag, ang = polar(30, 40)
    assert mag == 50.0 and round(ang, 1) == 53.1


@ejercicio(id=f"{PRE}-004", tipo="calculo", dificultad=2, fuente=FUENTE,
           enunciado=r"Sobre un cuerpo actúan tres fuerzas: $\vec{F_1}$ de \qty{20}{N} a "
                     r"$0^\circ$, $\vec{F_2}$ de \qty{30}{N} a $90^\circ$ y $\vec{F_3}$ de "
                     r"\qty{10}{N} a $180^\circ$. Halla la fuerza neta sumando por componentes: "
                     r"primero $\sum F_x$ y $\sum F_y$, después la magnitud y el ángulo.",
           respuesta=r"$\sum F_x = 20 - 10 = \qty{10}{N}$ y $\sum F_y = \qty{30}{N}$. "
                     r"Magnitud: $\sqrt{10^2 + 30^2} = \sqrt{1000} \approx \qty{31,6}{N}$; "
                     r"ángulo: $\arctg\frac{30}{10} \approx 71{,}6^\circ$. Sumar por "
                     r"componentes evita dibujar y es lo que se usa de aquí en adelante.",
           **COMUN)
def _():
    fx = 20 * cos(radians(0)) + 30 * cos(radians(90)) + 10 * cos(radians(180))
    fy = 20 * sin(radians(0)) + 30 * sin(radians(90)) + 10 * sin(radians(180))
    assert round(fx, 6) == 10.0 and round(fy, 6) == 30.0
    mag, ang = polar(fx, fy)
    assert round(mag, 1) == 31.6 and round(ang, 1) == 71.6


@ejercicio(id=f"{PRE}-005", tipo="argumentacion", dificultad=2, fuente=FUENTE,
           enunciado=r"Dos fuerzas de \qty{30}{N} y \qty{40}{N} actúan sobre el mismo cuerpo. "
                     r"Sin hacer cuentas, ¿entre qué valores puede estar la magnitud de la "
                     r"fuerza neta? Da un ejemplo de cada extremo y explica por qué "
                     r"\qty{70}{N} no siempre es la respuesta.",
           respuesta=r"Entre \qty{10}{N} y \qty{70}{N}. El máximo, \qty{70}{N}, se da si las "
                     r"dos apuntan en el mismo sentido; el mínimo, "
                     r"$40 - 30 = \qty{10}{N}$, si apuntan en sentidos opuestos. Cualquier "
                     r"valor intermedio corresponde a algún ángulo entre ellas: con "
                     r"$90^\circ$, por ejemplo, da \qty{50}{N}. Sumar \qty{70}{N} siempre es el "
                     r"error de tratar los vectores como si fueran números sueltos.",
           notas="Cierra la idea de la sesión: la dirección importa. El caso de 90° conecta con "
                 "el ejercicio 003.",
           **COMUN)
def _():
    assert round(hypot(30 + 40, 0), 1) == 70.0
    assert round(abs(40 - 30), 1) == 10.0
    assert round(hypot(30, 40), 1) == 50.0
    for a in (0, 45, 90, 135, 180):
        r = hypot(30 + 40 * cos(radians(a)), 40 * sin(radians(a)))
        assert 10.0 - 1e-9 <= r <= 70.0 + 1e-9


@ejercicio(id=f"{PRE}-006", tipo="argumentacion", dificultad=2, fuente=FUENTE,
           enunciado=r"Julián sumó una fuerza de \qty{60}{N} a $30^\circ$ con otra de "
                     r"\qty{80}{N} a $120^\circ$ y escribió que la neta mide "
                     r"$60 + 80 = \qty{140}{N}$ a $150^\circ$. Encuentra los dos errores, haz "
                     r"la suma correcta por componentes y explica en una frase qué se sumó mal.",
           respuesta=r"Julián sumó magnitudes y ángulos como si fueran números sueltos. Por "
                     r"componentes: $\sum F_x = 60\cos 30^\circ + 80\cos 120^\circ \approx "
                     r"51{,}96 - 40 = \qty{11,96}{N}$ y $\sum F_y = 60\sen 30^\circ + "
                     r"80\sen 120^\circ \approx 30 + 69{,}28 = \qty{99,28}{N}$. La neta mide "
                     r"$\approx \qty{100,0}{N}$ a $\approx 83{,}1^\circ$. Los ángulos nunca se "
                     r"suman, y las magnitudes solo si las dos fuerzas van en el mismo sentido "
                     r"(aquí forman $90^\circ$).",
           **COMUN)
def _():
    x1, y1 = comp(60, 30)
    x2, y2 = comp(80, 120)
    mag, ang = polar(x1 + x2, y1 + y2)
    assert round(mag, 1) == 100.0 and round(ang, 1) == 83.1
    assert round(mag, 1) != 140.0
