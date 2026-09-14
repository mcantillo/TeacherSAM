"""Banco de ejercicios — Matemáticas (Geometría 6°) — Área y volumen: recubrir y contar unidades.
Fuente: módulo de Matemáticas 6° de las Guías de Apoyo; ejercicios de área y volumen que
aparecen en las prácticas de potenciación, divisibilidad y máximo común divisor; se lee en
recursos/matematicas/Guías pedagógicas Matemáticas/markdown/06 - Modulo_Matematicas_Sexto.md
No se incluyó el 5 de «Potenciación en los naturales» (baldosas para un cuadrado de 90 cm de
lado): no dice el tamaño de la baldosa. Los demás literales de esas prácticas son del componente
numérico.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/area-volumen-6.py
"""
from itertools import product
from math import gcd

from sympy import Rational, divisors
from sympy.physics.units import centimeter, meter

from ejercicios import ejercicio, ejercicio_manual

M6 = "módulo 6° (Guías de Apoyo), Tema"
FPOT = f"{M6} 3, Potenciación en los naturales — Práctica lo aprendido"
FDIV = f"{M6} 4, Criterios de divisibilidad — Práctica lo aprendido"
FMCD = f"{M6} 4, Máximo común divisor — Práctica lo aprendido"
COMUN = dict(tema="área y volumen", grados=[6], dba=["matematicas-6-5"])


# ---------- Potenciación: contar cuadrados y cubos ----------

@ejercicio(id="area-volumen-6-001", tipo="calculo", dificultad=1, fuente=f"{FPOT} 6",
           enunciado=r"El piso de una caja está cubierto por una capa de cubos iguales, "
                     r"ordenados en 5 filas y 5 columnas. Indica con una potencia cuántos cubos "
                     r"hay en el piso.",
           respuesta=r"$5^2 = 25$ cubos.",
           notas="La figura del módulo (cuadrado de 5 filas y 5 columnas) se describió en el "
                 "enunciado.", **COMUN)
def _():
    assert len(list(product(range(5), repeat=2))) == 5**2 == 25


@ejercicio(id="area-volumen-6-002", tipo="calculo", dificultad=1, fuente=f"{FPOT} 7",
           enunciado=r"Un cubo grande está armado con cubos pequeños iguales: en cada arista hay "
                     r"5 cubos pequeños. Indica con una potencia cuántos cubos pequeños hay.",
           respuesta=r"$5^3 = 125$ cubos.",
           notas="La figura del módulo (cubo con caras de 5 × 5) se describió en el enunciado.",
           **COMUN)
def _():
    assert len(list(product(range(5), repeat=3))) == 5**3 == 125


# ---------- Divisibilidad: galletas en una bandeja ----------

BANDEJA = (r"En una bandeja cuadrada de 40 cm de lado se quieren poner galletas rectangulares "
           r"de distintos tamaños, sin que se monten unas sobre otras.")
NOTA_B = ("En el módulo la bandeja es «de 40 metros cuadrados»: una bandeja de 40 m² es "
          "irreal y sin sus lados no se puede saber cómo caben las galletas; se cambió por una "
          "bandeja cuadrada de 40 cm de lado (el módulo pide justificar con divisibilidad).")
L = 40


def caben(a, b, lado=L):
    """Galletas a × b en filas y columnas, sin sobrar espacio si a y b dividen el lado."""
    return (lado // a) * (lado // b)


@ejercicio(id="area-volumen-6-003", tipo="contexto", dificultad=1, fuente=f"{FDIV} 3a",
           enunciado=BANDEJA + r" ¿Cuántas galletas cuadradas de 2 cm $\times$ 2 cm caben?",
           respuesta=r"$20 \times 20 = 400$ galletas (40 es divisible entre 2: caben 20 por "
                     r"lado).", notas=NOTA_B, **COMUN)
def _():
    assert L % 2 == 0 and caben(2, 2) == 400 == (L * L) // (2 * 2)


@ejercicio(id="area-volumen-6-004", tipo="contexto", dificultad=2, fuente=f"{FDIV} 3b",
           enunciado=BANDEJA + r" Si se hacen galletas de 4 cm $\times$ 2 cm, ¿queda espacio "
                     r"libre en la bandeja?",
           respuesta=r"No: 40 es divisible entre 4 y entre 2, así que caben 10 galletas en un "
                     r"sentido y 20 en el otro ($200$ galletas) y cubren toda la bandeja.",
           notas=NOTA_B, **COMUN)
def _():
    assert L % 4 == 0 and L % 2 == 0
    assert caben(4, 2) * 4 * 2 == L * L and caben(4, 2) == 200


@ejercicio(id="area-volumen-6-005", tipo="contexto", dificultad=2, fuente=f"{FDIV} 3c",
           enunciado=BANDEJA + r" ¿Cuántas galletas de 4 cm $\times$ 2 cm menos que de 2 cm "
                     r"$\times$ 2 cm se pueden poner en la bandeja?",
           respuesta=r"$400 - 200 = 200$ galletas menos (cada galleta de 4 cm $\times$ 2 cm "
                     r"ocupa el lugar de dos de 2 cm $\times$ 2 cm).", notas=NOTA_B, **COMUN)
def _():
    assert caben(2, 2) - caben(4, 2) == 200


@ejercicio(id="area-volumen-6-006", tipo="contexto", dificultad=2, fuente=f"{FDIV} 3d",
           enunciado=BANDEJA + r" Si se quieren hacer varias galletas cuadradas iguales, lo más "
                     r"grandes posible, sin que quede espacio libre en la bandeja, ¿de qué "
                     r"medidas se deben hacer? ¿Cuántas galletas serían?",
           respuesta=r"El lado de la galleta debe dividir a 40; el mayor divisor de 40 menor que "
                     r"40 es 20. Galletas de 20 cm $\times$ 20 cm: 4 galletas.",
           notas=NOTA_B + " Se añadió «varias» para excluir una sola galleta del tamaño de la "
                          "bandeja.", **COMUN)
def _():
    lado = max(d for d in divisors(L) if d < L)
    assert lado == 20 and caben(lado, lado) == 4


@ejercicio(id="area-volumen-6-007", tipo="argumentacion", dificultad=3, fuente=f"{FDIV} 3e",
           enunciado=BANDEJA + r" ¿Es posible poner galletas de 3 cm $\times$ 2 cm de tal forma "
                     r"que no quede espacio libre en la bandeja? Justifica tu respuesta.",
           respuesta=r"No. La bandeja tiene $40 \times 40 = 1600$ cm$^2$ y cada galleta "
                     r"$6$ cm$^2$; como 1600 no es divisible entre 6 (tampoco entre 3), no se "
                     r"puede cubrir exactamente con galletas enteras.", notas=NOTA_B, **COMUN)
def _():
    assert (L * L) % (3 * 2) != 0 and (L * L) % 3 != 0


ejercicio_manual(id="area-volumen-6-008", tipo="conceptual", dificultad=1, fuente=f"{FDIV} 4a",
                 enunciado=r"Representa una bandeja cuadrada en la que se puedan poner "
                           r"exactamente 16 galletas de 3 cm $\times$ 3 cm, sin que sobre "
                           r"espacio.",
                 respuesta=r"Un cuadrado dividido en 4 filas y 4 columnas de cuadrados de 3 cm "
                           r"de lado (la bandeja mide 12 cm de lado).", **COMUN)


@ejercicio(id="area-volumen-6-009", tipo="calculo", dificultad=2, fuente=f"{FDIV} 4b",
           enunciado=r"En una bandeja cuadrada caben exactamente 16 galletas de 3 cm $\times$ "
                     r"3 cm, sin que sobre espacio. ¿Cuáles son las medidas de la bandeja?",
           respuesta=r"16 galletas forman 4 filas de 4, así que la bandeja mide "
                     r"$4 \times 3 = 12$ cm de lado (12 cm $\times$ 12 cm; área 144 cm$^2$).",
           **COMUN)
def _():
    lado = (16 * 3 * 3 * centimeter**2) ** Rational(1, 2)
    assert lado == 12 * centimeter and caben(3, 3, 12) == 16


@ejercicio(id="area-volumen-6-010", tipo="calculo", dificultad=2, fuente=f"{FDIV} 7",
           enunciado=r"Con 60 cuadrados iguales, ¿cuántos rectángulos de formas distintas se "
                     r"pueden formar sin que sobren cuadrados?",
           respuesta=r"6 rectángulos, uno por cada pareja de números que multiplicados dan 60: "
                     r"$1 \times 60$, $2 \times 30$, $3 \times 20$, $4 \times 15$, $5 \times 12$ "
                     r"y $6 \times 10$.",
           notas="Se cuenta la fila de 1 × 60 como rectángulo, y 6 × 10 y 10 × 6 como la misma "
                 "forma.", **COMUN)
def _():
    formas = {tuple(sorted((d, 60 // d))) for d in divisors(60)}
    assert len(formas) == 6 and (6, 10) in formas


# ---------- Máximo común divisor: triángulos y baldosas ----------

TRI = r"Un triángulo $ABC$ tiene 18 cm$^2$ de área."
NOTA_T = "En el módulo se nombra «el ΔABC» sin haberlo presentado; se escribió «Un triángulo ABC»."


@ejercicio(id="area-volumen-6-011", tipo="argumentacion", dificultad=2, fuente=f"{FMCD} 3a",
           enunciado=TRI + r" ¿Es posible formarlo con triángulos de 4 cm$^2$, sin que se monten "
                     r"unos sobre otros? Justifica tu respuesta.",
           respuesta=r"No: 18 no es múltiplo de 4 ($4 \times 4 = 16$ y $4 \times 5 = 20$), así "
                     r"que ningún número entero de triángulos de 4 cm$^2$ suma 18 cm$^2$.",
           notas=NOTA_T, **COMUN)
def _():
    assert 18 % 4 != 0


@ejercicio(id="area-volumen-6-012", tipo="argumentacion", dificultad=2, fuente=f"{FMCD} 3b",
           enunciado=TRI + r" ¿Es posible formarlo con triángulos de 9 cm$^2$, sin que se monten "
                     r"unos sobre otros? Justifica tu respuesta.",
           respuesta=r"Sí, con 2 triángulos ($18 = 2 \times 9$): la mediana trazada desde un "
                     r"vértice divide el triángulo en dos triángulos de igual base y la misma "
                     r"altura, es decir, de 9 cm$^2$ cada uno.", notas=NOTA_T, **COMUN)
def _():
    from sympy import Point, Segment, Triangle
    A, B, C = Point(0, 0), Point(6, 0), Point(2, 6)          # área 18
    assert Triangle(A, B, C).area == 18
    M = Segment(A, B).midpoint
    assert abs(Triangle(A, M, C).area) == abs(Triangle(M, B, C).area) == 9


@ejercicio(id="area-volumen-6-013", tipo="argumentacion", dificultad=3, fuente=f"{FMCD} 3c",
           enunciado=TRI + r" ¿Es posible formarlo con triángulos de 2 cm$^2$ y de 3 cm$^2$ "
                     r"(usando de los dos tamaños), sin que se monten unos sobre otros? Si es "
                     r"así, ¿cuántos triángulos de cada uno se necesitan?",
           respuesta=r"Sí. Hay que lograr $2a + 3b = 18$ con $a$ y $b$ mayores que cero: "
                     r"6 triángulos de 2 cm$^2$ y 2 de 3 cm$^2$, o 3 de 2 cm$^2$ y 4 de "
                     r"3 cm$^2$. (Se puede cortar el triángulo desde un vértice, dividiendo el "
                     r"lado opuesto en tramos proporcionales a esas áreas).",
           notas=NOTA_T + " El módulo no aclara si deben usarse los dos tamaños; hay dos "
                          "respuestas posibles.", **COMUN)
def _():
    sols = [(a, b) for a in range(1, 10) for b in range(1, 7) if 2 * a + 3 * b == 18]
    assert sols == [(3, 4), (6, 2)]


PISTAS = dict(A=(12, 4), B=(15, 6), C=(10, 5), D=(16, 7))
TABLA = (r"Cuatro pistas de baile rectangulares miden: A, 12 m $\times$ 4 m; B, 15 m $\times$ "
         r"6 m; C, 10 m $\times$ 5 m; D, 16 m $\times$ 7 m. Se quieren cubrir con baldosas "
         r"cuadradas iguales (en cada pista), sin cortar ninguna.")
NOTA_P = ("La tabla del módulo no tiene unidades; se usaron metros. Las «baldosas» más grandes "
          "posibles resultan de 3 m a 5 m de lado, poco realistas: en clase conviene hablar de "
          "«placas» o de «cuadros del diseño».")


def baldosa(pista):
    largo, ancho = PISTAS[pista]
    lado = gcd(largo, ancho)
    return lado, (largo // lado) * (ancho // lado)


@ejercicio(id="area-volumen-6-014", tipo="contexto", dificultad=2, fuente=f"{FMCD} 4a",
           enunciado=TABLA + r" ¿Qué medida, como máximo, deben tener las baldosas de la pista "
                     r"A? ¿Cuántas se usarán?",
           respuesta=r"$\text{mcd}(12, 4) = 4$: baldosas de 4 m $\times$ 4 m; se usan "
                     r"$3 \times 1 = 3$.", notas=NOTA_P, **COMUN)
def _():
    assert baldosa("A") == (4, 3)
    assert 3 * (4 * meter) ** 2 == 12 * meter * 4 * meter


@ejercicio(id="area-volumen-6-015", tipo="contexto", dificultad=2, fuente=f"{FMCD} 4b",
           enunciado=TABLA + r" ¿Qué medida, como máximo, deben tener las baldosas de la pista "
                     r"B?",
           respuesta=r"$\text{mcd}(15, 6) = 3$: baldosas de 3 m $\times$ 3 m (se usan "
                     r"$5 \times 2 = 10$).", notas=NOTA_P, **COMUN)
def _():
    assert baldosa("B") == (3, 10)


@ejercicio(id="area-volumen-6-016", tipo="contexto", dificultad=2, fuente=f"{FMCD} 4c",
           enunciado=TABLA + r" ¿Qué medida, como máximo, deben tener las baldosas de la pista "
                     r"D?",
           respuesta=r"$\text{mcd}(16, 7) = 1$: baldosas de 1 m $\times$ 1 m (se usan "
                     r"$16 \times 7 = 112$).", notas=NOTA_P, **COMUN)
def _():
    assert baldosa("D") == (1, 112)


@ejercicio(id="area-volumen-6-017", tipo="contexto", dificultad=2, fuente=f"{FMCD} 4d",
           enunciado=TABLA + r" Si en cada pista se usan las baldosas más grandes posibles, "
                     r"¿en cuál pista se usarán más baldosas?",
           respuesta=r"En la pista D: 112 baldosas (A usa 3; B, 10; C, 2 de 5 m $\times$ 5 m).",
           notas=NOTA_P, **COMUN)
def _():
    cuantas = {k: baldosa(k)[1] for k in PISTAS}
    assert cuantas == dict(A=3, B=10, C=2, D=112)
    assert max(cuantas, key=cuantas.get) == "D"
