"""Banco de ejercicios — Geometría 7° — Perímetro y área: razones y variación.
Fuente: módulo de Matemáticas 7° de las Guías de Apoyo; se lee en
recursos/matematicas/Guías pedagógicas Matemáticas/markdown/07 - Modulo_Matematicas_Septimo.md
El módulo 7° es numérico-variacional (enteros, ecuaciones, proporcionalidad); aquí están solo los
literales de pensamiento métrico que encajan en el DBA 6 de 7° (variación de perímetro y área).
No se incluyeron (fuera de los DBA de Geometría 7°: son despeje de fórmulas o planteamiento de
ecuaciones con un contexto geométrico): Tema 2, Resolución de ecuaciones 10 y Pasos para resolver
una ecuación 2e y 6 (ángulos de un triángulo o suplementarios), Fórmulas 1a–f, 2a, 3c–d, 5b y
Ecuaciones con la incógnita en ambos miembros 3a–b (fórmulas de área y volumen).
En el banco no había ejercicios de este tema: nada duplicado.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/perimetro-area-7.py
"""
from sympy import Rational, simplify, solve, sqrt, symbols
from sympy.physics import units as u

from ejercicios import ejercicio

REC = "módulo 7° (Guías de Apoyo)"
COMUN = dict(tema="perímetro y área", grados=[7], dba=["matematicas-7-6"])
L, k, x = symbols("L k x", positive=True)


def opciones(*items):
    return r" \begin{opciones} " + " ".join(r"\item " + i for i in items) + r" \end{opciones}"


RAZON = f"{REC}, Tema 3: Proporcionalidad, Razón — Practica lo aprendido"


@ejercicio(id="perimetro-area-7-001", tipo="calculo", dificultad=1, fuente=f"{RAZON} 3a",
           enunciado=r"El perímetro de un cuadrado de lado $L$ es $4L$. ¿Cuál es la razón entre "
                     r"el lado y el perímetro?",
           respuesta=r"$\frac{L}{4L} = \frac{1}{4}$: el lado es la cuarta parte del perímetro.",
           **COMUN)
def _():
    assert simplify(L / (4 * L)) == Rational(1, 4)


@ejercicio(id="perimetro-area-7-002", tipo="calculo", dificultad=1, fuente=f"{RAZON} 3b",
           enunciado=r"Si cada lado de un cuadrado de lado $L$ se multiplica por $2$, ¿cuál es la "
                     r"razón entre el nuevo lado y el nuevo perímetro?",
           respuesta=r"El nuevo lado mide $2L$ y el nuevo perímetro $8L$: la razón es "
                     r"$\frac{2L}{8L} = \frac{1}{4}$, la misma de antes.",
           notas="En el módulo: «la razón entre el lado y el nuevo perímetro»; se precisó «el "
                 "nuevo lado» (con el lado original la razón sería 1/8, que no es lo que busca "
                 "el literal c).", **COMUN)
def _():
    lado, perimetro = 2 * L, 4 * (2 * L)
    assert perimetro == 8 * L and simplify(lado / perimetro) == Rational(1, 4)


@ejercicio(id="perimetro-area-7-003", tipo="argumentacion", dificultad=2, fuente=f"{RAZON} 3c",
           enunciado=r"Repite el ejercicio anterior multiplicando cada lado del cuadrado por otro "
                     r"número (por ejemplo, $3$) y saca una conclusión sobre la razón entre el lado "
                     r"y el perímetro.",
           respuesta=r"Con factor $3$: $\frac{3L}{12L} = \frac{1}{4}$. Con cualquier factor $k$: "
                     r"$\frac{kL}{4kL} = \frac{1}{4}$. Conclusión: al ampliar o reducir el cuadrado, "
                     r"el perímetro cambia en el mismo factor que el lado, y la razón lado : "
                     r"perímetro siempre es $\frac{1}{4}$.", **COMUN)
def _():
    assert simplify((3 * L) / (4 * 3 * L)) == Rational(1, 4)
    assert simplify((k * L) / (4 * k * L)) == Rational(1, 4)
    assert simplify(4 * (k * L) / (4 * L)) == k          # el perímetro cambia en el factor k


@ejercicio(id="perimetro-area-7-004", tipo="calculo", dificultad=2, fuente=f"{RAZON} 3d",
           enunciado=r"Halla la razón entre el lado y el área de un cuadrado de lado $L$. ¿Es "
                     r"siempre la misma, como la del lado y el perímetro?",
           respuesta=r"$\frac{L}{L^2} = \frac{1}{L}$. No es constante: depende del lado. Si el "
                     r"lado se multiplica por $2$, el área se multiplica por $4$ y la razón queda "
                     r"$\frac{1}{2L}$.", **COMUN)
def _():
    assert simplify(L / L**2) == 1 / L
    assert simplify((2 * L)**2 / L**2) == 4
    assert simplify((2 * L) / (2 * L)**2) == 1 / (2 * L)


@ejercicio(id="perimetro-area-7-005", tipo="contexto", dificultad=2, fuente=f"{RAZON} 4",
           enunciado=r"El área de un círculo menor es $97$~m$^2$. ¿Cuál es el área de un círculo "
                     r"mayor si la razón entre el área del menor y la del mayor es "
                     r"$\frac{2}{3}$?",
           respuesta=r"$\frac{97}{A} = \frac{2}{3}$, así que $A = \frac{97 \cdot 3}{2} = "
                     r"\num{145,5}$~m$^2$.", **COMUN)
def _():
    A = symbols("A", positive=True)
    mayor = solve(Rational(97) / A - Rational(2, 3), A)
    assert mayor == [Rational(291, 2)] and Rational(291, 2) == Rational(1455, 10)
    assert mayor[0] > 97


@ejercicio(id="perimetro-area-7-006", tipo="contexto", dificultad=2, fuente=f"{RAZON} 5",
           enunciado=r"El área de un rectángulo mayor es $60$~m$^2$. ¿Cuál es el área de un "
                     r"rectángulo menor si la razón entre el área del mayor y la del menor es "
                     r"$\frac{5}{4}$?",
           respuesta=r"$\frac{60}{A} = \frac{5}{4}$, así que $A = \frac{60 \cdot 4}{5} = 48$~m$^2$.",
           **COMUN)
def _():
    A = symbols("A", positive=True)
    assert solve(Rational(60) / A - Rational(5, 4), A) == [48]


@ejercicio(id="perimetro-area-7-007", tipo="calculo", dificultad=1,
           fuente=f"{REC}, Tema 2: Ecuaciones, Fórmulas — Práctica lo aprendido 5a",
           enunciado=r"El perímetro de un cuadrado es de $204$~m. ¿Cuánto mide su lado?",
           respuesta=r"$4L = 204$, así que $L = 51$~m.", **COMUN)
def _():
    lado = solve(4 * L - 204, L)
    assert lado == [51]
    assert u.convert_to(204 * u.meter / 4, u.meter) == 51 * u.meter


@ejercicio(id="perimetro-area-7-008", tipo="seleccion", dificultad=2,
           fuente=f"{REC}, Tema 2: Ecuaciones, Pasos para resolver una ecuación — "
                  f"Practica lo aprendido 2b",
           enunciado=r"El perímetro de un rectángulo es de $378$~m y el ancho es la tercera parte "
                     r"del largo. Si $x$ es el largo, ¿cuál ecuación resuelve el problema? Halla "
                     r"después las dimensiones." + opciones(
                         r"$2\left(x + \frac{x}{3}\right) = 378$",
                         r"$\frac{378}{3} = \frac{x}{2}$",
                         r"$78 + x = 180$",
                         r"$x + 3x + 2 = 378$",
                         r"$78 = x + 2x + x$",
                         r"$3x + (2x + 3) + x + \frac{x}{2} = 2$"),
           respuesta=r"La primera: $2\left(x + \frac{x}{3}\right) = 378$. Entonces "
                     r"$\frac{8x}{3} = 378$, el largo mide $x = \num{141,75}$~m y el ancho "
                     r"$\num{47,25}$~m.",
           notas="En el módulo las seis ecuaciones (A–F) sirven para cinco problemas (a–e); aquí "
                 "solo el del rectángulo (b). Las soluciones no son enteras.", **COMUN)
def _():
    X = symbols("X")
    ecuaciones = [2 * (X + X / 3) - 378, Rational(378, 3) - X / 2, 78 + X - 180,
                  X + 3 * X + 2 - 378, 78 - (X + 2 * X + X),
                  3 * X + (2 * X + 3) + X + X / 2 - 2]
    cumplen = []
    for ec in ecuaciones:
        (s,) = solve(ec, X)
        cumplen.append(s > 0 and 2 * (s + s / 3) == 378)
    assert cumplen == [True, False, False, False, False, False]
    largo = solve(ecuaciones[0], X)[0]
    assert largo == Rational(14175, 100) and largo / 3 == Rational(4725, 100)


@ejercicio(id="perimetro-area-7-009", tipo="seleccion", dificultad=1,
           fuente=f"{REC}, Tema 1: Números enteros — Preparémonos para el ICFES 6",
           enunciado=r"El área de un lote de forma cuadrada es $\num{4900}$~m$^2$. El lado del lote "
                     r"es:" + opciones(r"$-70$~m", r"$7$~m", r"$70$~m$^2$", r"$70$~m",
                                        r"Ninguna de las anteriores"),
           respuesta=r"$70$~m, porque $70^2 = \num{4900}$ (una longitud no es negativa y se mide "
                     r"en m, no en m$^2$).", **COMUN)
def _():
    lado = sqrt(4900 * u.meter**2)
    assert lado == 70 * u.meter
    distractores = [-70 * u.meter, 7 * u.meter, 70 * u.meter**2]
    assert all(d != lado for d in distractores)
    assert (7 * u.meter)**2 != 4900 * u.meter**2


@ejercicio(id="perimetro-area-7-010", tipo="seleccion", dificultad=2,
           fuente=f"{REC}, Tema 3: Proporcionalidad — Preparémonos para el ICFES 13",
           enunciado=r"La razón entre el perímetro y el área de un cuadrado de lado $L$ es:"
                     + opciones(r"$4L$", r"$L$", r"$\frac{L}{4}$", r"$\frac{4}{L}$"),
           respuesta=r"$\frac{4L}{L^2} = \frac{4}{L}$.", **COMUN)
def _():
    razon = simplify(4 * L / L**2)
    assert razon == 4 / L
    assert all(simplify(razon - o) != 0 for o in (4 * L, L, L / 4))
