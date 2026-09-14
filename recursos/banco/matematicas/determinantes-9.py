"""Banco de ejercicios — Matemáticas 9° — Determinantes 2×2 y regla de Cramer (sistemas 2×2).
Fuente: módulo de Matemáticas 9° de las Guías de Apoyo (Adriana Quintero Palomino), Tema 3;
se lee en recursos/matematicas/Guías pedagógicas Matemáticas/markdown/09 - Modulo_Matematicas_Noveno.md
Incluye la actividad de repaso con que abre el Tema 3 (sistemas por igualación y por suma y resta).
No se incluyeron: el repaso 2i (x - (3x+4)/7 = (x+24)/2 …: la primera ecuación solo tiene x y la
solución es x = 176, y = 992/11; parece una errata que no se puede reconstruir con certeza) y el
ICFES 1c (almacenes, segundo mes: con los datos no se puede determinar cuántos artículos se
vendieron; faltan datos).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/determinantes-9.py
"""
from sympy import Matrix, Rational, nsimplify, solve, symbols

from ejercicios import ejercicio, ejercicio_manual, expresion, tex

AUTOR = "módulo 9° (Quintero Palomino), Tema 3, Determinantes"
PRACTICA = f"{AUTOR}, Regla de Cramer — Practica lo aprendido"
ICFES = f"{AUTOR} — Prepárate para el ICFES"
REPASO = f"{AUTOR} — actividad inicial"
COMUN = dict(grados=[9], dba=["matematicas-9-2"])
CONTEXTO = dict(grados=[9], dba=["matematicas-9-2", "matematicas-9-8"], tipo="contexto")


def sistema(ecuaciones):
    """(LaTeX con cases, lista de expresiones = 0) de ["x + y = 3", "3x - 2y = -1"]."""
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


# ---------- Repaso inicial y Practica 2: resolver sistemas ----------
# (n, fuente, instrucción, ecuaciones, solución a mano {var: valor} | "ninguna" | "infinitas", notas)
SISTEMAS = [
    (1, f"{REPASO} 1i", "Resuelve por el método de igualación",
     ["3x - (4y + 6) = 2y - (x + 18)", "2x - 3 = x - y + 4"], {"x": "3", "y": "4"}, None),
    (2, f"{REPASO} 1ii", "Resuelve por el método de igualación",
     ["3(2x + y) - 2(y - x) = -4(y + 7)", "3(2y + 3x) - 20 = -53"], {"x": "-1", "y": "-4"}, None),
    (3, f"{REPASO} 2ii", "Resuelve por el método de suma y resta",
     ["(x + y)/(x - y) = -2/7", "(8x + y - 1)/(x - y - 2) = 2"], {"x": "-5", "y": "9"},
     "En el módulo el primer denominador aparece como «x_y»; es x - y."),
    (4, f"{PRACTICA} 2a", "Resuelve por la regla de Cramer",
     ["x + y = 3", "3x - 2y = -1"], {"x": "1", "y": "2"}, None),
    (5, f"{PRACTICA} 2b", "Resuelve por la regla de Cramer",
     ["3y - x = 1", "15x - 5y = -15"], {"x": "-1", "y": "0"}, None),
    (6, f"{PRACTICA} 2c", "Resuelve por la regla de Cramer",
     ["3x - y = 1", "x - (1/3)y = 1/3"], "infinitas", None),
    (7, f"{PRACTICA} 2d", "Resuelve por la regla de Cramer",
     ["3x + 11y = -21", "5x - 3y = 29"], {"x": "4", "y": "-3"}, None),
    (8, f"{PRACTICA} 2e", "Resuelve (sugerencia: toma $\\frac{1}{x}$ y $\\frac{1}{y}$ como "
     "incógnitas)", ["9/x + 10/y = 2", "-6/x + 7/y = 11/2"], {"x": "-3", "y": "2"}, None),
    (9, f"{PRACTICA} 2f", "Resuelve por la regla de Cramer",
     ["(x - 3)/3 - (y - 4)/4 = 0", "(x - 4)/2 + (y + 2)/5 = 3"], {"x": "6", "y": "8"}, None),
]
for n, fuente, instruccion, ecuaciones, sol, notas in SISTEMAS:
    latex, _exprs = sistema(ecuaciones)
    if sol == "infinitas":
        resp = (r"El determinante del sistema es $\left|\begin{smallmatrix}3 & -1 \\ 1 & "
                r"-\frac{1}{3}\end{smallmatrix}\right| = -1 + 1 = 0$: la segunda ecuación es la "
                r"primera dividida entre $3$. El sistema tiene infinitas soluciones: todos los "
                r"puntos de la recta $y = 3x - 1$ (sistema compatible indeterminado).")
    else:
        resp = solucion_tex(sol) + "."
    extra = dict(notas=notas) if notas else {}

    @ejercicio(id=f"determinantes-9-{n:03d}", tema="sistemas de ecuaciones 2×2", tipo="calculo",
               dificultad=2 if "/" in "".join(ecuaciones) else 1, fuente=fuente,
               enunciado=f"{instruccion}: $ {latex} $", respuesta=resp, **extra, **COMUN)
    def _(exprs=_exprs, sol=sol):
        obtenida = resolver(exprs)
        if sol == "infinitas":
            x, y = expresion("x"), expresion("y")
            assert obtenida == [{x: (y + 1) / 3}]                      # y queda libre
            A = Matrix([[3, -1], [1, Rational(-1, 3)]])
            assert A.det() == 0
            for e in exprs:                                            # (t, 3t - 1) cumple
                t = Rational(7, 5)
                assert e.subs({x: t, y: 3 * t - 1}) == 0
        else:
            esperada = {expresion(k): expresion(v) for k, v in sol.items()}
            assert obtenida == [esperada]


# ---------- Practica 1: determinantes 2×2 ----------
DET2 = [
    (10, "1a", [["5", "6"], ["1", "3"]], "9"),
    (11, "1b", [["4", "-9"], ["-2", "-14"]], "-74"),
    (12, "1c", [["-6", "0.5"], ["-1.5", "0"]], "0.75"),
    (13, "1d", [["12", "16"], ["-3", "-4"]], "0"),
]
for n, literal, m, valor in DET2:
    cuerpo = r" \\ ".join(" & ".join(tex(c) for c in fila) for fila in m)

    @ejercicio(id=f"determinantes-9-{n:03d}", tema="determinantes", tipo="calculo", dificultad=1,
               fuente=f"{PRACTICA} {literal}",
               enunciado=rf"Halla el determinante $\begin{{vmatrix}} {cuerpo} \end{{vmatrix}}$.",
               respuesta=f"${tex(valor)}$.", **COMUN)
    def _(m=m, valor=valor):
        assert Matrix([[nsimplify(c) for c in f] for f in m]).det() == nsimplify(valor)


# ---------- Practica 3: problemas ----------
a, b, n_, c_ = symbols("a b n c", positive=True)


@ejercicio(id="determinantes-9-014", tema="sistemas de ecuaciones 2×2", dificultad=1,
           fuente=f"{PRACTICA} 3a",
           enunciado="Halla dos números cuya suma sea $182$ y su diferencia $60$.",
           respuesta=r"$x + y = 182$, $x - y = 60$: los números son $121$ y $61$.",
           notas="En el módulo aparece «1 82» (con un espacio); es 182.", **CONTEXTO)
def _():
    x, y = symbols("x y")
    assert solve([x + y - 182, x - y - 60], [x, y]) == {x: 121, y: 61}


@ejercicio(id="determinantes-9-015", tema="sistemas de ecuaciones 2×2", dificultad=2,
           fuente=f"{PRACTICA} 3b",
           enunciado=r"En un cine hay $150$ personas entre adultos y niños. Cada niño pagó "
                     r"\$3000 y cada adulto \$5000 por su entrada. Si se recaudaron \$570\,000, "
                     r"¿cuántos adultos y cuántos niños hay en el cine?",
           respuesta=r"$a + n = 150$ y $5000a + 3000n = 570\,000$: hay $60$ adultos y $90$ niños.",
           **CONTEXTO)
def _():
    assert solve([a + n_ - 150, 5000 * a + 3000 * n_ - 570000], [a, n_]) == {a: 60, n_: 90}


@ejercicio(id="determinantes-9-016", tema="sistemas de ecuaciones 2×2", dificultad=2,
           fuente=f"{PRACTICA} 3c",
           enunciado=r"La suma de las cifras de un número de dos cifras es $15$, y si al número "
                     r"se le resta $9$, las cifras se invierten. Halla el número.",
           respuesta=r"Con decenas $d$ y unidades $u$: $d + u = 15$ y $10d + u - 9 = 10u + d$, "
                     r"o sea $d - u = 1$. Entonces $d = 8$, $u = 7$: el número es $87$.",
           notas="En el módulo aparece «1 5» (con un espacio); es 15.", **CONTEXTO)
def _():
    d, u = symbols("d u")
    sol = solve([d + u - 15, 10 * d + u - 9 - (10 * u + d)], [d, u])
    assert sol == {d: 8, u: 7}
    assert [k for k in range(10, 100) if k // 10 + k % 10 == 15
            and k - 9 == (k % 10) * 10 + k // 10] == [87]


@ejercicio(id="determinantes-9-017", tema="sistemas de ecuaciones 2×2", dificultad=2,
           fuente=f"{PRACTICA} 3d",
           enunciado=r"La razón entre dos números es de $3$ a $4$. Si al menor se le suma $2$ y "
                     r"al mayor se le resta $9$, quedan en la razón de $4$ a $3$. Halla los "
                     r"números.",
           respuesta=r"$\dfrac{x}{y} = \dfrac{3}{4}$ y $\dfrac{x + 2}{y - 9} = \dfrac{4}{3}$, es "
                     r"decir, $4x = 3y$ y $3x + 6 = 4y - 36$: los números son $18$ y $24$.",
           **CONTEXTO)
def _():
    x, y = symbols("x y")
    assert solve([4 * x - 3 * y, 3 * (x + 2) - 4 * (y - 9)], [x, y]) == {x: 18, y: 24}
    assert Rational(18, 24) == Rational(3, 4) and Rational(20, 15) == Rational(4, 3)


@ejercicio(id="determinantes-9-018", tema="sistemas de ecuaciones 2×2", dificultad=3,
           fuente=f"{PRACTICA} 3e",
           enunciado=r"Un número consta de dos cifras cuya suma es $9$. Cuando se invierten sus "
                     r"cifras se obtiene un número que, multiplicado por $6$, es $5$ veces el "
                     r"número primitivo. Halla el número.",
           respuesta=r"$d + u = 9$ y $6(10u + d) = 5(10d + u)$, o sea $4d = 5u$: $d = 5$, $u = 4$. "
                     r"El número es $54$ (en efecto, $6 \cdot 45 = 270 = 5 \cdot 54$).",
           **CONTEXTO)
def _():
    d, u = symbols("d u")
    assert solve([d + u - 9, 6 * (10 * u + d) - 5 * (10 * d + u)], [d, u]) == {d: 5, u: 4}
    assert [k for k in range(10, 100) if k // 10 + k % 10 == 9
            and 6 * ((k % 10) * 10 + k // 10) == 5 * k] == [54]


# ---------- Practica 4: construir problemas (abiertos) ----------
PAREJAS = [
    (19, "4a", "5 y 11", r"«Dos números suman $16$ y el mayor excede al menor en $6$. ¿Cuáles "
     r"son?» $x + y = 16$, $y - x = 6$; por Cramer, $x = \frac{-10}{-2} = 5$, $y = 11$."),
    (20, "4b", "-4 y -3", r"«Dos números suman $-7$ y el doble del primero menos el segundo es "
     r"$-5$.» $x + y = -7$, $2x - y = -5$: $x = -4$, $y = -3$."),
    (21, "4c", "4 y 8", r"«En una tienda, $2$ cuadernos y $1$ lápiz cuestan \$16 mil; $1$ cuaderno "
     r"y $3$ lápices, \$28 mil. ¿Cuánto cuesta cada uno (en miles)?» $2x + y = 16$, "
     r"$x + 3y = 28$: $x = 4$, $y = 8$."),
    (22, "4d", "10 y -4", r"«La suma de dos números es $6$ y su diferencia es $14$.» "
     r"$x + y = 6$, $x - y = 14$: $x = 10$, $y = -4$."),
    (23, "4e", "-4 y -7", r"«Una temperatura $x$ y otra $y$ (en °C) suman $-11$ y la primera "
     r"supera a la segunda en $3$ grados.» $x + y = -11$, $x - y = 3$: $x = -4$, $y = -7$."),
]
for n, literal, pareja, modelo in PAREJAS:
    ejercicio_manual(
        id=f"determinantes-9-{n:03d}", tema="sistemas de ecuaciones 2×2", tipo="argumentacion",
        dificultad=2, fuente=f"{PRACTICA} {literal}",
        enunciado=f"Con la pareja de números ${tex(pareja.split(' y ')[0])}$ y "
                  f"${tex(pareja.split(' y ')[1])}$, construye un problema que se resuelva con un "
                  f"sistema de dos ecuaciones y resuélvelo por cualquiera de los métodos que "
                  f"aprendiste.",
        respuesta=f"Respuesta abierta. Modelo: {modelo} Se revisa que el sistema tenga solución "
                  f"única y que esa solución sea la pareja dada.", **COMUN)


# ---------- Prepárate para el ICFES ----------
ALMACENES = (r"Una fábrica de artículos deportivos distribuye cada mes a dos almacenes, A y B, "
             r"$15$ raquetas, $40$ balones, $35$ palos de golf y $42$ bolas de tenis. El almacén A "
             r"vende raquetas a \$20\,000 y palos de golf a \$32\,000; el almacén B vende balones "
             r"a \$12\,500 y bolas de tenis a \$7500. ")


@ejercicio(id="determinantes-9-024", tema="sistemas de ecuaciones 2×2", dificultad=2,
           fuente=f"{ICFES} 1a",
           enunciado=ALMACENES + r"Si durante el primer mes el almacén A vendió $27$ artículos y "
                     r"recaudó en total \$744\,000, ¿cuántas raquetas y cuántos palos de golf "
                     r"vendió?",
           respuesta=r"$r + p = 27$ y $20\,000r + 32\,000p = 744\,000$: vendió $10$ raquetas y "
                     r"$17$ palos de golf.", **CONTEXTO)
def _():
    r, p = symbols("r p")
    sol = solve([r + p - 27, 20000 * r + 32000 * p - 744000], [r, p])
    assert sol == {r: 10, p: 17} and sol[r] <= 15 and sol[p] <= 35      # hay existencias


@ejercicio(id="determinantes-9-025", tema="sistemas de ecuaciones 2×2", dificultad=2,
           fuente=f"{ICFES} 1b",
           enunciado=ALMACENES + r"Si el almacén B recaudó \$670\,000 en $66$ artículos, "
                     r"¿cuántos balones y cuántas bolas de tenis vendió?",
           respuesta=r"$b + t = 66$ y $12\,500b + 7500t = 670\,000$: vendió $35$ balones y $31$ "
                     r"bolas de tenis.", **CONTEXTO)
def _():
    bb, t = symbols("b t")
    sol = solve([bb + t - 66, 12500 * bb + 7500 * t - 670000], [bb, t])
    assert sol == {bb: 35, t: 31} and sol[bb] <= 40 and sol[t] <= 42


@ejercicio(id="determinantes-9-026", tema="sistemas de ecuaciones 2×2", dificultad=3,
           fuente=f"{ICFES} 2",
           enunciado=r"Dos máquinas de imprenta, trabajando juntas, pueden imprimir un libro en "
                     r"$20$ horas. A las $15$ horas una de ellas se daña y a la otra le toma $9$ "
                     r"horas más terminar el trabajo. ¿Cuántas horas necesitaría cada máquina "
                     r"para imprimir ella sola el libro?",
           respuesta=r"Si las máquinas tardan $a$ y $b$ horas: $\dfrac{1}{a} + \dfrac{1}{b} = "
                     r"\dfrac{1}{20}$ y $15\left(\dfrac{1}{a} + \dfrac{1}{b}\right) + "
                     r"\dfrac{9}{b} = 1$. Entonces $\dfrac{9}{b} = \dfrac{1}{4}$: $b = 36$ h y "
                     r"$a = 45$ h.", **CONTEXTO)
def _():
    assert solve([1 / a + 1 / b - Rational(1, 20), 15 * (1 / a + 1 / b) + 9 / b - 1],
                 [a, b], dict=True) == [{a: 45, b: 36}]


@ejercicio(id="determinantes-9-027", tema="sistemas de ecuaciones 2×2", dificultad=3,
           fuente=f"{ICFES} 3",
           enunciado=r"Dos nadadores, A y B, se entrenan para una competencia de relevos en una "
                     r"piscina de $30$ metros de largo. Si A hace $2$ recorridos y B hace $2$, "
                     r"tardan en total $76$ segundos; si A hace $1$ recorrido y B hace $3$, tardan "
                     r"$74$ segundos. Halla la velocidad de cada uno.",
           respuesta=r"Con $p$ y $q$ los segundos por recorrido de A y de B: $2p + 2q = 76$ y "
                     r"$p + 3q = 74$, así que $p = 20$ s y $q = 18$ s. Velocidades: A, "
                     r"$\frac{30}{20} = \num{1,5}$ m/s; B, $\frac{30}{18} = \frac{5}{3} \approx "
                     r"\num{1,67}$ m/s.", **CONTEXTO)
def _():
    p, q = symbols("p q")
    sol = solve([2 * p + 2 * q - 76, p + 3 * q - 74], [p, q])
    assert sol == {p: 20, q: 18}
    assert (Rational(30) / sol[p], Rational(30) / sol[q]) == (Rational(3, 2), Rational(5, 3))


@ejercicio(id="determinantes-9-028", tema="sistemas de ecuaciones 2×2", dificultad=2,
           fuente=f"{ICFES} 4",
           enunciado=r"En una batalla había $4$ tanques de un ejército por cada $3$ del otro. "
                     r"Durante la batalla el primero perdió $20$ tanques y el segundo $10$, y "
                     r"quedaron $5$ tanques del primero por cada $4$ del segundo. ¿Cuántos tanques "
                     r"tenía cada ejército al comienzo?",
           respuesta=r"$3x = 4y$ y $4(x - 20) = 5(y - 10)$: al comienzo había $120$ y $90$ tanques.",
           notas="El módulo habla de tanques italianos e ingleses en el norte de África; se "
                 "neutralizó el contexto (los datos no cambian).", **CONTEXTO)
def _():
    x, y = symbols("x y")
    assert solve([3 * x - 4 * y, 4 * (x - 20) - 5 * (y - 10)], [x, y]) == {x: 120, y: 90}


@ejercicio(id="determinantes-9-029", tema="sistemas de ecuaciones 2×2", dificultad=3,
           fuente=f"{ICFES} 5",
           enunciado=r"Navegando a toda velocidad río arriba, un bote de motor recorre $18$ "
                     r"kilómetros en una hora. Navegando a media velocidad río abajo, recorre $15$ "
                     r"kilómetros en una hora. Halla la velocidad máxima del bote y la velocidad "
                     r"de la corriente.",
           respuesta=r"$v - c = 18$ y $\dfrac{v}{2} + c = 15$: velocidad máxima $v = 22$ km/h, "
                     r"corriente $c = 4$ km/h.",
           notas="El módulo usa millas; se cambió a kilómetros (los números no cambian).",
           **CONTEXTO)
def _():
    v, c = symbols("v c")
    assert solve([v - c - 18, v / 2 + c - 15], [v, c]) == {v: 22, c: 4}


@ejercicio(id="determinantes-9-030", tema="sistemas de ecuaciones 2×2", dificultad=3,
           fuente=f"{ICFES} 6",
           enunciado=r"Un granjero desea cercar un lote rectangular. Si usa un material que cuesta "
                     r"\$2400 por metro para el frente del lote y uno de \$2100 por metro para los "
                     r"otros tres lados, la cerca cuesta \$58\,950. Si usa el material más caro "
                     r"para los cuatro lados, la cerca le cuesta \$64\,800. Halla las dimensiones "
                     r"del lote.",
           respuesta=r"Con frente $x$ y fondo $y$: $2400x + 2100(x + 2y) = 58\,950$ y "
                     r"$2400(2x + 2y) = 64\,800$, es decir, $4500x + 4200y = 58\,950$ y "
                     r"$x + y = \num{13,5}$. El frente mide $\num{7,5}$ m y el fondo $6$ m.",
           notas="El módulo usa «vara» como unidad; se cambió a metros.", **CONTEXTO)
def _():
    x, y = symbols("x y", positive=True)
    assert solve([2400 * x + 2100 * (x + 2 * y) - 58950, 2400 * (2 * x + 2 * y) - 64800],
                 [x, y]) == {x: Rational(15, 2), y: 6}
