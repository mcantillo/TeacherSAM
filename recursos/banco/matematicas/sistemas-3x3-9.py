"""Banco de ejercicios — Matemáticas 9° — Sistemas de ecuaciones 3×3 (y algunos 4×4).
Fuente: módulo de Matemáticas 9° de las Guías de Apoyo (Adriana Quintero Palomino), Tema 4;
se lee en recursos/matematicas/Guías pedagógicas Matemáticas/markdown/09 - Modulo_Matematicas_Noveno.md
Incluye la actividad inicial del Tema 4 (dos ejercicios de sistemas 2×2).
En «Prepárate para el ICFES» el módulo numera «4» dos veces; la segunda se cita como «4 (bis)».
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/sistemas-3x3-9.py
"""
from sympy import Matrix, Rational, solve, symbols

from ejercicios import ejercicio, ejercicio_manual, expresion, tex

AUTOR = "módulo 9° (Quintero Palomino), Tema 4, Sistemas de ecuaciones 3×3"
PRACTICA = f"{AUTOR}, Regla de Cramer — Practica lo aprendido"
ICFES = f"{AUTOR} — Prepárate para el ICFES"
INICIO = f"{AUTOR} — actividad inicial"
COMUN = dict(grados=[9], dba=["matematicas-9-2"])
CONTEXTO = dict(grados=[9], dba=["matematicas-9-2", "matematicas-9-8"], tipo="contexto")
ARGUMENTO = {**CONTEXTO, "tipo": "argumentacion"}


def sistema(ecuaciones):
    filas, exprs = [], []
    for e in ecuaciones:
        a, b = (s.strip() for s in e.split("="))
        filas.append(f"{tex(a)} = {tex(b)}")
        exprs.append(expresion(a) - expresion(b))
    return r"\begin{cases} " + r" \\ ".join(filas) + r" \end{cases}", exprs


def resolver(exprs):
    libres = sorted(set().union(*(e.free_symbols for e in exprs)), key=str)
    return solve(exprs, libres, dict=True)


def solucion_tex(sol):
    return ", ".join(f"${k} = {tex(v)}$" for k, v in sol.items())


# ---------- Actividad inicial ----------

@ejercicio(id="sistemas-3x3-9-001", tema="sistemas de ecuaciones 2×2", dificultad=2,
           fuente=f"{INICIO} 1",
           enunciado=r"Al cambiar un cheque de \$3\,000\,000, Fanny pide al banco que le den "
                     r"billetes de \$10\,000 y de \$20\,000. Si recibió en total $190$ billetes, "
                     r"¿cuántos billetes de cada clase le dio el banco?",
           respuesta=r"$a + b = 190$ y $10\,000a + 20\,000b = 3\,000\,000$: $80$ billetes de "
                     r"\$10\,000 y $110$ de \$20\,000.",
           notas="En el módulo el cheque es de $4 000 000: con 190 billetes de $10 000 y "
                 "$20 000 se puede reunir como máximo $3 800 000 (saldrían −20 billetes de "
                 "$10 000). Se cambió a $3 000 000.", **CONTEXTO)
def _():
    a, b = symbols("a b")
    assert solve([a + b - 190, 10000 * a + 20000 * b - 4000000], [a, b])[a] < 0   # el original
    sol = solve([a + b - 190, 10000 * a + 20000 * b - 3000000], [a, b])
    assert sol == {a: 80, b: 110}


PAREJAS = [
    (2, "2a", ("5", "-3"), r"«Una balanza marca $2$ g con una pesa $x$ y una “pesa de ajuste” $y$ "
     r"que resta; con dos pesas $x$ y una de ajuste marca $7$ g.» $x + y = 2$, $2x + y = 7$: "
     r"$x = 5$, $y = -3$ (el signo negativo indica que $y$ resta masa)."),
    (3, "2b", ("4", "2"), r"«$1$ tuerca y $1$ tornillo pesan $6$ g; $2$ tuercas y $3$ tornillos, "
     r"$14$ g.» $x + y = 6$, $2x + 3y = 14$: tuerca $4$ g, tornillo $2$ g."),
    (4, "2c", ("-3", "1"), r"«La variación de masa de dos muestras suma $-2$ g y la primera "
     r"pierde $4$ g más de lo que gana la segunda.» $x + y = -2$, $y - x = 4$: $x = -3$ g, "
     r"$y = 1$ g."),
    (5, "2d", ("12", "20"), r"«Dos bolsas pesan juntas $32$ g y la segunda pesa $8$ g más que la "
     r"primera.» $x + y = 32$, $y - x = 8$: $12$ g y $20$ g."),
]
for n, literal, (p, q), modelo in PAREJAS:
    ejercicio_manual(
        id=f"sistemas-3x3-9-{n:03d}", tema="sistemas de ecuaciones 2×2", tipo="argumentacion",
        dificultad=2, fuente=f"{INICIO} {literal}",
        enunciado=f"Con la pareja de números ${tex(p)}$ y ${tex(q)}$, construye un problema con "
                  f"masas en gramos que se resuelva con un sistema $2 \\times 2$, y resuélvelo.",
        respuesta=f"Respuesta abierta. Modelo: {modelo} Se revisa que el sistema tenga solución "
                  f"única y que sea la pareja dada; con números negativos el problema debe "
                  f"hablar de cambios de masa, no de masas.", **COMUN)


# ---------- Practica 1: determinantes 3×3 ----------
DET3 = [
    (6, "1a", [[5, -6, 3], [1, 8, -4], [0, -2, 7]], 276),
    (7, "1b", [[10, 0, 1], [2, 5, 0], [-3, 3, -9]], -429),
    (8, "1c", [[-4, -9, 7], [-8, 3, -8], [12, 1, -9]], 1280),
    (9, "1d", [[3, -9, 0], [-8, -7, 1], [5, 3, 0]], -54),
]
for n, literal, m, valor in DET3:
    cuerpo = r" \\ ".join(" & ".join(str(c) for c in fila) for fila in m)

    @ejercicio(id=f"sistemas-3x3-9-{n:03d}", tema="determinantes", tipo="calculo", dificultad=2,
               fuente=f"{PRACTICA} {literal}",
               enunciado=rf"Halla el determinante $\begin{{vmatrix}} {cuerpo} \end{{vmatrix}}$.",
               respuesta=f"${valor}$.", **COMUN)
    def _(m=m, valor=valor):
        A = Matrix(m)
        sarrus = (A[0, 0] * A[1, 1] * A[2, 2] + A[0, 1] * A[1, 2] * A[2, 0]
                  + A[0, 2] * A[1, 0] * A[2, 1] - A[0, 2] * A[1, 1] * A[2, 0]
                  - A[0, 0] * A[1, 2] * A[2, 1] - A[0, 1] * A[1, 0] * A[2, 2])
        assert A.det() == sarrus == valor


# ---------- Practica 2, ICFES 4 y 4 (bis): sistemas ----------
# (n, fuente, ecuaciones, solución a mano | "ninguna" | "infinitas", respuesta si no es única,
#  dificultad, notas)
SISTEMAS = [
    (10, f"{PRACTICA} 2a", ["x - y + 3z = 3", "3x - 2y + 2z = 0", "3x - 4y - z = 1"],
     {"x": "-2", "y": "-2", "z": "1"}, None, 2, None),
    (11, f"{PRACTICA} 2b", ["(1/3)x + y - 2z = 3", "x = y + 1", "x - (1/4)y + z = 11"],
     {"x": "9", "y": "8", "z": "4"}, None, 2, None),
    (12, f"{PRACTICA} 2c", ["6u - 4v + 2w = -1", "5u + 4v - 3w = 3", "4u - 2v + 2w = -1"],
     {"u": "1/8", "v": "1/8", "w": "-5/8"}, None, 2, None),
    (13, f"{PRACTICA} 2d", ["2u + 2v - w = 2", "4u - v + w = 4", "6u - 2v + 3w = 2"],
     {"u": "4/3", "v": "-2", "w": "-10/3"}, None, 2, None),
    (14, f"{PRACTICA} 2e", ["4x + y + 2z = 10", "3x + 2y + z = 5", "2x + 3y + 2z = 10"],
     {"x": "0", "y": "0", "z": "5"}, None, 2, None),
    (15, f"{PRACTICA} 2f", ["1/x + 1/y + 1/z = 1/8", "2/x - 3/y + 1/z = -2",
                            "-4/x + 1/y - 2/z = 4"], "ninguna",
     r"Con $p = \frac{1}{x}$, $q = \frac{1}{y}$, $r = \frac{1}{z}$ queda un sistema lineal cuya "
     r"única solución es $p = -\frac{17}{8}$, $q = 0$, $r = \frac{9}{4}$. Pero "
     r"$\frac{1}{y} = 0$ no se cumple para ningún $y$: el sistema no tiene solución.", 3,
     "Así está en el módulo; conviene que la docente decida si lo usa como ejercicio de "
     "análisis (no tiene solución) o si es una errata."),
    (16, f"{PRACTICA} 2g", ["x - y = 1", "x + z = -1", "y - z = 6"],
     {"x": "3", "y": "2", "z": "-4"}, None, 1, None),
    (17, f"{ICFES} 4a", ["2x + y + 3z = -4", "x - 4y - 2z = 3", "4x - 2y + z = 4",
                         "5x + 3y + 4z = 5"], {"x": "3", "y": "2", "z": "-4"},
     r"Sí tiene solución: las tres primeras ecuaciones dan $x = 3$, $y = 2$, $z = -4$, y la "
     r"cuarta también se cumple: $15 + 6 - 16 = 5$.", 3, None),
    (18, f"{ICFES} 4b", ["2x + 4y + 3z = 5", "x - 4y - 2z = 7", "4x - 3y + 5z = 2",
                         "3x + 2y + 4z = 8"], "ninguna",
     r"No tiene solución: las tres primeras ecuaciones dan $x = 5$, $y = 1$, $z = -3$, pero en la "
     r"cuarta $3 \cdot 5 + 2 \cdot 1 + 4(-3) = 5 \neq 8$.", 3, None),
    (19, f"{ICFES} 4 (bis) a", ["w - 2x + y - 2z = -4", "2w + 2x - 3y - 3z = -1",
                                "-w + x + 2y + z = 5", "x - 2y + z = 0"],
     {"w": "-1", "x": "2", "y": "1", "z": "0"}, None, 3,
     "En el módulo la primera ecuación empieza «2 - 2x + y - 2z = -4» (falta la incógnita w); "
     "se escribió w - 2x + y - 2z = -4, la única lectura con coeficiente entero de w que da "
     "solución entera. Con 2w la solución sería w = -1/5, x = 51/25, y = 6/5, z = 9/25."),
    (20, f"{ICFES} 4 (bis) b", ["3x + 2y = -2", "x + y + u = -3", "3x - 2y - u = -7",
                                "4x + 5y + 6z + 3u = 11"],
     {"u": "-3", "x": "-2", "y": "2", "z": "3"}, None, 3,
     "En el módulo la cuarta ecuación es «4x + 5y + 6z + 3y = 11» (y dos veces); se corrigió "
     "a 3u, que da solución entera."),
    (21, f"{ICFES} 4 (bis) c", ["2w - 3x + y - 8z = -2", "w + 3x + 2y - z = 5",
                                "-w + 2x + y + 3z = 3", "3w + 2x + 3y - 7z = 5"], "infinitas",
     r"Tiene infinitas soluciones: $w = 2z$, $x = 1 - z$, $y = z + 1$ para cualquier valor de "
     r"$z$ (por ejemplo, $z = 0$ da $w = 0$, $x = 1$, $y = 1$).", 3,
     "Así está en el módulo; la docente puede decidir si es intencional."),
    (22, f"{ICFES} 4 (bis) d", ["x - 2y + z + 3u = -3", "3x + y - 4z - 2u = 7",
                                "2x + 2y - z - u = 1", "x + 4y + 2z - 5u = 12"],
     {"u": "-4", "x": "2", "y": "-3", "z": "1"}, None, 3,
     "En el módulo la cuarta ecuación es «X + 4y + 2z -5 = 12» (falta la u); se escribió -5u."),
    (23, f"{ICFES} 4 (bis) e", ["2x - 3y + z + 4u = 0", "3x + y - 5z - 3u = -10",
                                "6x + 2y - z + u = -3", "x + 5y + 4z - 3u = -6"],
     {"u": "5", "x": "-3", "y": "4", "z": "-2"}, None, 3, None),
    (24, f"{ICFES} 4 (bis) f", ["2x - 3z - u = 2", "3y - 2z - 5u = 3", "4y - 3u = 2",
                                "x - 3y + 3u = 0"],
     {"u": "-2", "x": "3", "y": "-1", "z": "2"}, None, 3, None),
]
for n, fuente, ecuaciones, sol, texto, dificultad, notas in SISTEMAS:
    latex, _exprs = sistema(ecuaciones)
    instr = ("Determina si el sistema tiene solución; si la tiene, encuéntrala, y si no, "
             "resuelve un sistema con tres de las ecuaciones y muestra que su solución no "
             "cumple la otra ecuación" if "ICFES 4" in fuente and "bis" not in fuente
             else "Resuelve el sistema")
    resp = texto or solucion_tex(sol) + "."
    extra = dict(notas=notas) if notas else {}
    tema = "sistemas de ecuaciones 4×4" if "bis" in fuente else "sistemas de ecuaciones 3×3"

    @ejercicio(id=f"sistemas-3x3-9-{n:03d}", tema=tema, tipo="calculo", dificultad=dificultad,
               fuente=fuente, enunciado=f"{instr}: $ {latex} $", respuesta=resp, **extra, **COMUN)
    def _(exprs=_exprs, sol=sol, n=n):
        obtenida = resolver(exprs)
        if sol == "infinitas":
            w, x, y, z = (expresion(c) for c in "wxyz")
            assert obtenida == [{w: 2 * z, x: 1 - z, y: z + 1}]
        elif sol == "ninguna":
            assert obtenida == []
            if n == 15:                                  # el sistema lineal en 1/x, 1/y, 1/z
                p, q, r = symbols("p q r")
                assert solve([p + q + r - Rational(1, 8), 2 * p - 3 * q + r + 2,
                              -4 * p + q - 2 * r - 4], [p, q, r]) == \
                    {p: Rational(-17, 8), q: 0, r: Rational(9, 4)}
            if n == 18:
                assert resolver(exprs[:3]) == [{expresion("x"): 5, expresion("y"): 1,
                                                 expresion("z"): -3}]
        else:
            assert obtenida == [{expresion(k): expresion(v) for k, v in sol.items()}]


# ---------- Practica 3: problemas ----------

@ejercicio(id="sistemas-3x3-9-025", tema="sistemas de ecuaciones 3×3", dificultad=1,
           fuente=f"{PRACTICA} 3a",
           enunciado=r"Halla tres números tales que el primero más el segundo sumen $50$, el "
                     r"primero más el tercero sumen $30$ y el segundo más el tercero sumen $40$.",
           respuesta=r"$a + b = 50$, $a + c = 30$, $b + c = 40$: los números son $20$, $30$ y "
                     r"$10$.", **CONTEXTO)
def _():
    a, b, c = symbols("a b c")
    assert solve([a + b - 50, a + c - 30, b + c - 40], [a, b, c]) == {a: 20, b: 30, c: 10}


@ejercicio(id="sistemas-3x3-9-026", tema="sistemas de ecuaciones 3×3", dificultad=2,
           fuente=f"{PRACTICA} 3b",
           enunciado=r"Tres personas tienen cierta cantidad de dinero. La primera y la tercera "
                     r"tienen juntas \$500 más que la segunda; la segunda y la tercera tienen "
                     r"\$2500 más que la primera, y la segunda tiene \$4500 más que la tercera. "
                     r"¿Cuánto tiene cada una?",
           respuesta=r"$a + c = b + 500$, $b + c = a + 2500$, $b = c + 4500$: la primera tiene "
                     r"\$5000, la segunda \$6000 y la tercera \$1500.", **CONTEXTO)
def _():
    a, b, c = symbols("a b c")
    assert solve([a + c - b - 500, b + c - a - 2500, b - c - 4500], [a, b, c]) == \
        {a: 5000, b: 6000, c: 1500}


@ejercicio(id="sistemas-3x3-9-027", tema="sistemas de ecuaciones 3×3",
           dificultad=3, fuente=f"{PRACTICA} 3c",
           enunciado=r"La suma de las tres cifras de un número es $16$. La suma de las cifras de "
                     r"las centenas y de las decenas es igual al cuádruplo de la cifra de las "
                     r"unidades. Si se intercambian las cifras de las unidades y de las decenas, "
                     r"el número disminuye en $36$. ¿Puede existir un número con esas "
                     r"características?",
           respuesta=r"No. Con cifras $c$, $d$, $u$: $c + d + u = 16$ y $c + d = 4u$ dan "
                     r"$5u = 16$, $u = \frac{16}{5}$, que no es una cifra (además, $9(d - u) = 36$ "
                     r"daría $d = u + 4$). Ningún número de tres cifras cumple las condiciones.",
           **ARGUMENTO)
def _():
    c, d, u = symbols("c d u")
    sol = solve([c + d + u - 16, c + d - 4 * u, (100 * c + 10 * d + u) - (100 * c + 10 * u + d)
                 - 36], [c, d, u])
    assert sol[u] == Rational(16, 5)
    assert not [k for k in range(100, 1000) if sum(map(int, str(k))) == 16
                and k // 100 + k // 10 % 10 == 4 * (k % 10)
                and k - (k // 100 * 100 + k % 10 * 10 + k // 10 % 10) == 36]


@ejercicio(id="sistemas-3x3-9-028", tema="sistemas de ecuaciones 3×3", dificultad=1,
           fuente=f"{PRACTICA} 3d",
           enunciado=r"Una persona emplea diariamente $14$ horas en trabajo, estudio y diversión. "
                     r"Si en trabajo y diversión emplea $11$ horas y en trabajo y estudio $10$ "
                     r"horas, ¿cómo emplea su tiempo?",
           respuesta=r"$t + e + d = 14$, $t + d = 11$, $t + e = 10$: trabaja $7$ h, estudia $3$ h "
                     r"y se divierte $4$ h.", **CONTEXTO)
def _():
    t, e, d = symbols("t e d")
    assert solve([t + e + d - 14, t + d - 11, t + e - 10], [t, e, d]) == {t: 7, e: 3, d: 4}


@ejercicio(id="sistemas-3x3-9-029", tema="sistemas de ecuaciones 3×3",
           dificultad=3, fuente=f"{PRACTICA} 3e",
           enunciado=r"Encuentra un número de tres cifras sabiendo que la suma de las dos primeras "
                     r"(de izquierda a derecha) es igual a la última, y que al dividir el número "
                     r"entre $9$ el cociente es un múltiplo de $9$.",
           respuesta=r"El número es múltiplo de $81$, luego de $9$: sus cifras suman $9$ o $18$. "
                     r"Como la suma es $2u$ (dos veces la última cifra), $u = 9$ y las dos "
                     r"primeras suman $9$. Entre $189, 279, \dots, 909$ el único múltiplo de $81$ "
                     r"es $729$ ($729 \div 9 = 81 = 9 \cdot 9$).", **ARGUMENTO)
def _():
    assert [k for k in range(100, 1000) if k // 100 + k // 10 % 10 == k % 10
            and k % 9 == 0 and (k // 9) % 9 == 0] == [729]


# ---------- Prepárate para el ICFES 1–3 (conceptuales) y 5 ----------
CONCEPTUALES = [
    (30, "1", "¿Qué características presenta un sistema de ecuaciones que no tiene solución?",
     r"Sus ecuaciones son incompatibles: al combinarlas se llega a una igualdad falsa, como "
     r"$0 = 5$. En un sistema $2 \times 2$, las rectas son paralelas (misma pendiente, distinto "
     r"corte): los coeficientes de las incógnitas son proporcionales, pero los términos "
     r"independientes no guardan esa proporción, y el determinante del sistema es $0$."),
    (31, "2", "¿Cómo deben ser los coeficientes de las ecuaciones para que un sistema tenga "
     "infinitas soluciones?",
     r"Una ecuación debe ser múltiplo de la otra (o, en sistemas mayores, combinación de las "
     r"demás): en $2 \times 2$, $\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}$. Las "
     r"rectas coinciden y el determinante del sistema es $0$."),
    (32, "3", "Si una ecuación lineal de dos incógnitas se representa gráficamente por medio de "
     "una recta, ¿cómo se representa una ecuación lineal de tres incógnitas?",
     r"Con un plano en el espacio (tres ejes $x$, $y$, $z$). Resolver un sistema $3 \times 3$ es "
     r"buscar el punto donde se cortan tres planos."),
]
for n, literal, enunciado, respuesta in CONCEPTUALES:
    ejercicio_manual(id=f"sistemas-3x3-9-{n:03d}", tema="sistemas de ecuaciones",
                     tipo="conceptual", dificultad=2, fuente=f"{ICFES} {literal}",
                     enunciado=enunciado, respuesta=respuesta, **COMUN)


@ejercicio(id="sistemas-3x3-9-033", tema="sistemas de ecuaciones 3×3", dificultad=3,
           fuente=f"{ICFES} 5",
           enunciado=r"Se invierten \$250\,000 en tres partes: una al $5\,\%$, otra al $6\,\%$ y "
                     r"otra al $8\,\%$ mensual. El interés total que se recibe en un mes es "
                     r"\$16\,000, y el interés de la parte colocada al $8\,\%$ es igual a la suma de "
                     r"los intereses de las otras dos. ¿Cuánto se colocó a cada porcentaje?",
           respuesta=r"$a + b + c = 250\,000$, $\num{0,05}a + \num{0,06}b + \num{0,08}c = "
                     r"16\,000$ y $\num{0,08}c = \num{0,05}a + \num{0,06}b$: \$100\,000 al $5\,\%$, "
                     r"\$50\,000 al $6\,\%$ y \$100\,000 al $8\,\%$.",
           notas="Se aclaró «en un mes» (el módulo dice «mensual» sin decir el plazo).",
           **CONTEXTO)
def _():
    a, b, c = symbols("a b c")
    r = Rational
    sol = solve([a + b + c - 250000, r(5, 100) * a + r(6, 100) * b + r(8, 100) * c - 16000,
                 r(8, 100) * c - r(5, 100) * a - r(6, 100) * b], [a, b, c])
    assert sol == {a: 100000, b: 50000, c: 100000}
