"""Banco de ejercicios — Matemáticas 9° — Sistemas de ecuaciones lineales 2×2.
Fuente: módulo de Matemáticas 9° de las Guías de Apoyo (Adriana Quintero Palomino), Tema 2
«Sistemas de ecuaciones», «Práctica lo aprendido»; se lee en
recursos/matematicas/Guías pedagógicas Matemáticas/markdown/09 - Modulo_Matematicas_Noveno.md
El módulo escribe «X», «Y» mayúsculas por x, y en varios sistemas; aquí se escriben en minúscula.
No se incluyó el ejercicio 3f (reducción: 3x − 2y = 19, x − 2y = 5): es el mismo sistema del 1a
con las ecuaciones en otro orden (id sistemas-ecuaciones-9-001).
Los problemas 15, 16 y 17 del módulo son inecuaciones (no sistemas de ecuaciones); se incluyen
aquí porque están en esta lista de ejercicios.
Varios problemas vienen de textos españoles (euros, «jersey»); se conservan los euros.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/sistemas-ecuaciones-9.py
"""
from sympy import FiniteSet, Interval, Rational as Q, S, linsolve, oo, solve, solveset, symbols
from sympy.physics.units import centimeter, convert_to, decimeter, meter

from ejercicios import ejercicio, expresion, tex

MODULO = "módulo 9° (Quintero Palomino), Tema 2, Sistemas de ecuaciones — Práctica lo aprendido"
COMUN = dict(tema="sistemas de ecuaciones lineales", grados=[9], dba=["matematicas-9-2"])
PROBLEMAS = dict(tema="sistemas de ecuaciones lineales", grados=[9],
                 dba=["matematicas-9-2", "matematicas-9-8"], tipo="contexto")

x, y = symbols("x y", real=True)
_N = [0]


def nid():
    _N[0] += 1
    return f"sistemas-ecuaciones-9-{_N[0]:03d}"


def ecuacion(s):
    a, b = s.split("=")
    return expresion(a) - expresion(b)


def eqtex(s):
    a, b = s.split("=")
    return f"{tex(a)} = {tex(b)}"


def sistema(e1, e2):
    return rf"$\begin{{cases}} {eqtex(e1)} \\ {eqtex(e2)} \end{{cases}}$"


def fr(q):
    q = Q(q)
    a = abs(q)
    return ("-" if q < 0 else "") + (str(a.p) if a.q == 1 else rf"\frac{{{a.p}}}{{{a.q}}}")


# ---------- 1–3. Resolver por un método dado: (literal, ec. 1, ec. 2, x, y) ----------
METODOS = [
    ("sustitución", "1", [("a", "x - 2y = 5", "3x - 2y = 19", 7, 1),
                          ("b", "y = 3", "5x/2 + 2y/3 = 17", 6, 3),
                          ("c", "3x - 2y = 19", "2x - y = 5", -9, -23),
                          ("d", "3x + 2y = 6", "x = -20 + 3y", -2, 6),
                          ("e", "5x - 4y = 0", "10x + 2y = 5", Q(2, 5), Q(1, 2)),
                          ("f", "2x - 16 = 2y", "2y - 3x = 16", -32, -40)]),
    ("igualación", "2", [("a", "2x + y = 2", "3x + y = 5", 3, -4),
                         ("b", "y = (x + 2)/3", "2x - 4y = 2", 7, 3),
                         ("c", "y = -5x + 1", "y = (3x - 11)/2", 1, -4),
                         ("d", "x - 2y = 13", "x - 5y = -8", 27, 7),
                         ("e", "5x + y = 3", "2x - y = -3", 0, 3),
                         ("f", "6x - 4y = 3", "3x + 8y = 4", Q(2, 3), Q(1, 4))]),
    ("reducción", "3", [("a", "5x + 2y = 4", "3x - 2y = 12", 2, -3),
                        ("b", "x - 2y = 13", "3x - 3y = 24", 3, -5),
                        ("c", "-2x + y = -15", "3x - 2y = 26", 4, -7),
                        ("d", "7x + y = -4", "7x + 2y = -10", Q(2, 7), -6),
                        ("e", "-3x - 2y = -1", "2x + 3y = 1", Q(1, 5), Q(1, 5))]),
]
for metodo, num, filas in METODOS:
    for lit, e1, e2, x0, y0 in filas:
        dif = 1 if Q(x0).q == 1 and Q(y0).q == 1 and "/" not in e1 + e2 else 2

        @ejercicio(id=nid(), tipo="calculo", dificultad=dif, fuente=f"{MODULO} {num}{lit}",
                   enunciado=f"Resuelve por {metodo} el sistema {sistema(e1, e2)}",
                   respuesta=f"$x = {fr(x0)}$, $y = {fr(y0)}$.", **COMUN)
        def _(e1=e1, e2=e2, x0=x0, y0=y0):
            assert linsolve([ecuacion(e1), ecuacion(e2)], [x, y]) == FiniteSet((x0, y0))

# ---------- 4. Clasificar antes de resolver ----------
CLASES = [("a", "x + y = -4", "x + y = -10", "incompatible",
           r"Incompatible: $x + y$ no puede valer a la vez $-4$ y $-10$ (rectas paralelas); no "
           r"tiene solución.", None),
          ("b", "x + 2y = -10", "3x + y = -4", "determinado",
           r"Compatible determinado: las pendientes $-\frac{1}{2}$ y $-3$ son distintas, así que "
           r"las rectas se cortan en un solo punto.", None),
          ("c", "3x + 3y = -12", "x + y = -4", "indeterminado",
           r"Compatible indeterminado: la primera ecuación es la segunda multiplicada por $3$ "
           r"(la misma recta). Tiene infinitas soluciones: $y = -4 - x$, es decir, todos los "
           r"pares $(x, -4 - x)$.", "-4 - x"),
          ("d", "5x + 2y = 4", "-3x + y = 2", "determinado",
           r"Compatible determinado: las pendientes $-\frac{5}{2}$ y $3$ son distintas.", None),
          ("e", "14x + 2y = 5", "7x + y = -4", "incompatible",
           r"Incompatible: al multiplicar la segunda por $2$ queda $14x + 2y = -8$, que "
           r"contradice $14x + 2y = 5$ (rectas paralelas); no tiene solución.", None),
          ("f", "-6x + 4y = -12", "3x - 2y = 6", "indeterminado",
           r"Compatible indeterminado: la primera ecuación es la segunda multiplicada por $-2$. "
           r"Tiene infinitas soluciones: $y = \frac{3x - 6}{2}$, es decir, todos los pares "
           r"$\left(x, \frac{3x - 6}{2}\right)$.", "(3x - 6)/2")]
for lit, e1, e2, clase, resp, param in CLASES:
    @ejercicio(id=nid(), tipo="conceptual", dificultad=2, fuente=f"{MODULO} 4{lit}",
               enunciado=f"Sin resolverlo, decide si el sistema {sistema(e1, e2)} es compatible "
                         f"determinado, compatible indeterminado o incompatible. Si es compatible "
                         f"indeterminado, resuélvelo.",
               respuesta=resp, **COMUN)
    def _(e1=e1, e2=e2, clase=clase, param=param):
        sol = linsolve([ecuacion(e1), ecuacion(e2)], [x, y])
        if sol == S.EmptySet:
            calculada = "incompatible"
        else:
            (px, py), = sol
            calculada = "indeterminado" if py.free_symbols or px.free_symbols else "determinado"
        assert calculada == clase
        if param:
            for e in (e1, e2):                 # la recta y = param cumple las dos ecuaciones
                assert ecuacion(e).subs(y, expresion(param)).expand() == 0


# ---------- 5–30. Problemas ----------
# (n, enunciado, respuesta, ecuaciones en x, y, solución {x, y}, dificultad, notas)
P = [
    (5, r"Halla dos números sabiendo que el mayor más seis veces el menor es igual a $62$ y el "
        r"menor más cinco veces el mayor es igual a $78$.",
     r"Con $x$ el mayor y $y$ el menor: $x + 6y = 62$ y $y + 5x = 78$. Los números son $14$ y "
     r"$8$.", ["x + 6y = 62", "y + 5x = 78"], (14, 8), 2, None),
    (6, r"Dos números suman $241$ y su diferencia es $99$. ¿Qué números son?",
     r"$x + y = 241$, $x - y = 99$: son $170$ y $71$.", ["x + y = 241", "x - y = 99"],
     (170, 71), 1, None),
    (7, r"Pedro tiene $335$ € en billetes de $5$ € y de $10$ €; si en total tiene $52$ billetes, "
        r"¿cuántos tiene de cada clase?",
     r"Con $x$ billetes de $5$ € y $y$ de $10$ €: $x + y = 52$, $5x + 10y = 335$. Tiene $37$ "
     r"billetes de $5$ € y $15$ de $10$ €.", ["x + y = 52", "5x + 10y = 335"], (37, 15), 2, None),
    (8, r"En un hotel hay $67$ habitaciones entre dobles y sencillas. Si el número total de "
        r"camas es $92$, ¿cuántas habitaciones hay de cada tipo?",
     r"Con $x$ dobles y $y$ sencillas: $x + y = 67$, $2x + y = 92$. Hay $25$ habitaciones dobles "
     r"y $42$ sencillas.", ["x + y = 67", "2x + y = 92"], (25, 42), 2, None),
    (9, r"María compró un pantalón y un jersey (suéter). Los precios de las dos prendas suman "
        r"$77$ €, pero le hicieron un descuento del $10\,\%$ en el pantalón y del $20\,\%$ en el "
        r"jersey, y pagó en total $\num{63,6}$ €. ¿Cuál es el precio sin rebaja de cada prenda?",
     r"Con $x$ el pantalón y $y$ el jersey: $x + y = 77$, $\num{0,9}x + \num{0,8}y = \num{63,6}$. "
     r"El pantalón costaba $20$ € y el jersey $57$ €.",
     ["x + y = 77", "0.9x + 0.8y = 63.6"], (20, 57), 2,
     "En el módulo el total aparece como «63’6€» (apóstrofo como separador decimal); se escribe "
     "63,6 €."),
    (10, r"Halla dos números tales que, si se divide el primero por $3$ y el segundo por $4$, la "
         r"suma de los cocientes es $15$, y si se multiplica el primero por $2$ y el segundo por "
         r"$5$, la suma de los productos es $188$.",
     r"$\frac{x}{3} + \frac{y}{4} = 15$ y $2x + 5y = 188$: los números son $24$ y $28$.",
     ["x/3 + y/4 = 15", "2x + 5y = 188"], (24, 28), 2, None),
    (11, r"En un parque de atracciones, subir a la noria cuesta $1$ € y subir a la montaña rusa "
         r"$4$ €. Ana sube un total de $13$ veces y gasta $16$ €. ¿Cuántas veces subió a cada "
         r"atracción?",
     r"$x + y = 13$, $x + 4y = 16$: subió $12$ veces a la noria y $1$ vez a la montaña rusa.",
     ["x + y = 13", "x + 4y = 16"], (12, 1), 1, None),
    (12, r"En un corral hay ovejas y gallinas, $77$ animales en total, y si contamos las patas "
         r"obtenemos $274$. ¿Cuántas ovejas y cuántas gallinas hay?",
     r"Con $x$ ovejas y $y$ gallinas: $x + y = 77$, $4x + 2y = 274$. Hay $60$ ovejas y $17$ "
     r"gallinas.", ["x + y = 77", "4x + 2y = 274"], (60, 17), 2, None),
    (13, r"Encuentra un número de dos cifras sabiendo que la suma de sus cifras es $7$ y que la "
         r"diferencia entre el número y el que resulta al intercambiarlas es $27$.",
     r"Con $x$ la cifra de las decenas y $y$ la de las unidades: $x + y = 7$ y "
     r"$(10x + y) - (10y + x) = 27$, o sea $x - y = 3$. El número es $52$.",
     ["x + y = 7", "(10x + y) - (10y + x) = 27"], (5, 2), 3, None),
    (14, r"La suma de las edades de Luisa y de Miguel es $32$ años. Dentro de $8$ años la edad de "
         r"Miguel será el doble de la edad de Luisa. ¿Qué edades tienen?",
     r"Con $x$ la edad de Luisa y $y$ la de Miguel: $x + y = 32$, $y + 8 = 2(x + 8)$. Luisa "
     r"tiene $8$ años y Miguel $24$.", ["x + y = 32", "y + 8 = 2(x + 8)"], (8, 24), 2, None),
    (18, r"Un joyero vendió $18$ pulseras de plata y $13$ de oro por \$3500. Una pulsera de oro "
         r"cuesta cuatro veces lo que cuesta una de plata. ¿Cuál es el precio de una pulsera de "
         r"cada clase?",
     r"Con $x$ el precio de la de plata y $y$ el de la de oro: $18x + 13y = 3500$, $y = 4x$. La "
     r"de plata cuesta \$50 y la de oro \$200.", ["18x + 13y = 3500", "y = 4x"], (50, 200), 2,
     None),
    (19, r"Esteban pagó una cuenta de \$300 con billetes de \$2 y de \$5. En total empleó $90$ "
         r"billetes. ¿Cuántos billetes de cada valor utilizó?",
     r"$x + y = 90$, $2x + 5y = 300$: $50$ billetes de \$2 y $40$ de \$5.",
     ["x + y = 90", "2x + 5y = 300"], (50, 40), 2, None),
    (20, r"Entre dos estantes de una librería hay $90$ libros. Si se pasan $10$ libros del "
         r"segundo al primer estante, los dos quedan con la misma cantidad. ¿Cuántos libros "
         r"había inicialmente en cada estante?",
     r"$x + y = 90$, $x + 10 = y - 10$: el primero tenía $35$ libros y el segundo $55$.",
     ["x + y = 90", "x + 10 = y - 10"], (35, 55), 2, None),
    (21, r"En un número de dos cifras, la cifra de las decenas es el doble de la de las unidades, "
         r"y la diferencia de las dos cifras, aumentada en $12$, es igual a $15$. Calcula el "
         r"número.",
     r"Con $x$ la cifra de las decenas y $y$ la de las unidades: $x = 2y$, $(x - y) + 12 = 15$. "
     r"El número es $63$.", ["x = 2y", "(x - y) + 12 = 15"], (6, 3), 2, None),
    (22, r"Laura es $17$ años mayor que Pablo y la suma de sus edades es $75$ años. ¿Qué edad "
         r"tiene cada uno?",
     r"$x = y + 17$, $x + y = 75$: Laura tiene $46$ años y Pablo $29$.",
     ["x = y + 17", "x + y = 75"], (46, 29), 1, None),
    (23, r"En un grupo de $560$ personas asistentes a un espectáculo, la razón entre hombres y "
         r"mujeres es $\frac{2}{5}$. ¿Cuántos hombres y cuántas mujeres asistieron?",
     r"$x + y = 560$, $\frac{x}{y} = \frac{2}{5}$ (o $5x = 2y$): $160$ hombres y $400$ mujeres.",
     ["x + y = 560", "5x = 2y"], (160, 400), 2, None),
    (24, r"La edad de María más el doble de la edad de Pedro es $14$. El doble de la edad de María "
         r"dentro de $4$ años será la edad de Pedro dentro de $6$ años. Calcula la edad de los dos.",
     r"$x + 2y = 14$, $2(x + 4) = y + 6$: María tiene $2$ años y Pedro $6$.",
     ["x + 2y = 14", "2(x + 4) = y + 6"], (2, 6), 2, None),
    (25, r"Un comerciante compra dos objetos por \$2100 y los vende por \$2202. Si en la venta de "
         r"uno gana el $10\,\%$ y en la del otro pierde el $8\,\%$, ¿cuánto pagó por cada objeto?",
     r"$x + y = 2100$, $\num{1,1}x + \num{0,92}y = 2202$: pagó \$1500 por el que vendió con "
     r"ganancia y \$600 por el otro.", ["x + y = 2100", "1.1x + 0.92y = 2202"], (1500, 600), 3,
     None),
    (27, r"Si se aumentan en $2$ m tanto el ancho como el largo de un rectángulo, el perímetro "
         r"mide $30$ m. Si el largo se disminuye en $2$ m, resulta un cuadrado. ¿Cuáles son las "
         r"dimensiones del rectángulo?",
     r"Con $x$ el largo y $y$ el ancho: $2(x + 2) + 2(y + 2) = 30$ y $x - 2 = y$. El rectángulo "
     r"mide $\num{6,5}$ m de largo y $\num{4,5}$ m de ancho.",
     ["2(x + 2) + 2(y + 2) = 30", "x - 2 = y"], (Q(13, 2), Q(9, 2)), 2, None),
    (29, r"El propietario de un campo decidió sembrar dos cultivos, A y B. La semilla del cultivo "
         r"A cuesta \$4 por hectárea y la del B, \$6 por hectárea. La mano de obra cuesta \$20 "
         r"por hectárea para el cultivo A y \$10 por hectárea para el B. Si dispone de \$480 para "
         r"semillas y \$1400 para mano de obra, ¿cuántas hectáreas de cada cultivo podrá sembrar?",
     r"Con $x$ hectáreas de A y $y$ de B: $4x + 6y = 480$, $20x + 10y = 1400$. Puede sembrar $45$ "
     r"hectáreas de A y $50$ de B.", ["4x + 6y = 480", "20x + 10y = 1400"], (45, 50), 2, None),
    (30, r"Un productor de vinos artesanales prepara una mezcla de dos variedades, chardonnay y "
         r"pinot gris. El volumen total de la mezcla debe ser de $1420$ litros, y el volumen de "
         r"chardonnay debe ser igual a dos tercios del volumen de pinot gris más $120$ litros. "
         r"¿Cuántos litros de cada variedad deben mezclarse?",
     r"Con $x$ litros de chardonnay y $y$ de pinot gris: $x + y = 1420$, "
     r"$x = \frac{2}{3}y + 120$. Se mezclan $640$ litros de chardonnay y $780$ de pinot gris.",
     ["x + y = 1420", "x = (2/3)y + 120"], (640, 780), 2,
     "En el módulo aparece «chardonay»; se escribe chardonnay."),
]
for n, enun, resp, ecs, (x0, y0), dif, notas in P:
    extra = dict(notas=notas) if notas else {}

    @ejercicio(id=nid(), dificultad=dif, fuente=f"{MODULO} {n}", enunciado=enun, respuesta=resp,
               **extra, **PROBLEMAS)
    def _(ecs=ecs, x0=x0, y0=y0, n=n):
        assert linsolve([ecuacion(e) for e in ecs], [x, y]) == FiniteSet((x0, y0))
        assert x0 >= 0 and y0 >= 0
        if n == 5:
            assert x0 > y0                      # x es el mayor
        if n in (13, 21):
            assert 0 < x0 <= 9 and 0 <= y0 <= 9  # son cifras
        if n == 25:
            assert Q(11, 10) * x0 - x0 == 150 and y0 - Q(92, 100) * y0 == 48


@ejercicio(id=nid(), dificultad=2, fuente=f"{MODULO} 26",
           enunciado=r"En un triángulo isósceles, la suma de la base y la altura es $40$ cm. Si a "
                     r"la base se le agregan $12$ cm, se obtienen $\frac{9}{4}$ de la altura. "
                     r"Calcula el área del triángulo.",
           respuesta=r"Con $b$ la base y $h$ la altura: $b + h = 40$ y $b + 12 = \frac{9}{4}h$. "
                     r"Entonces $h = 16$ cm, $b = 24$ cm y el área es "
                     r"$\frac{24 \cdot 16}{2} = 192$ cm².", **PROBLEMAS)
def _():
    b, h = symbols("b h", positive=True)
    sol = solve([b + h - 40, b + 12 - Q(9, 4) * h], [b, h])
    assert sol == {b: 24, h: 16} and sol[b] * sol[h] / 2 == 192


@ejercicio(id=nid(), dificultad=3, fuente=f"{MODULO} 28",
           enunciado=r"El perímetro de un rectángulo mide $17$ cm y su base mide $\num{0,1}$ dm "
                     r"más que el doble de la altura. Averigua las medidas del rectángulo en "
                     r"metros.",
           respuesta=r"$\num{0,1}$ dm $= 1$ cm. Con $b$ la base y $h$ la altura (en cm): "
                     r"$2b + 2h = 17$ y $b = 2h + 1$, así que $h = \num{2,5}$ cm y $b = 6$ cm. En "
                     r"metros: altura $\num{0,025}$ m y base $\num{0,06}$ m.", **PROBLEMAS)
def _():
    assert convert_to(Q(1, 10) * decimeter, centimeter) == 1 * centimeter
    b, h = symbols("b h", positive=True)
    sol = solve([2 * b + 2 * h - 17, b - 2 * h - 1], [b, h])
    assert sol == {b: 6, h: Q(5, 2)}
    assert convert_to(sol[h] * centimeter, meter) == Q(1, 40) * meter
    assert convert_to(sol[b] * centimeter, meter) == Q(6, 100) * meter


# ---------- 15–17. Inecuaciones de la lista ----------
INEC = dict(tema="inecuaciones lineales", grados=[9], dba=["matematicas-9-2", "matematicas-9-8"],
            tipo="contexto")
s = symbols("s", integer=True)


@ejercicio(id=nid(), dificultad=3, fuente=f"{MODULO} 15",
           enunciado=r"Rosa quiere comprar globos y serpentinas para adornar la fiesta de fin de "
                     r"curso. Quiere comprar el doble de paquetes de globos que de serpentinas y no "
                     r"menos de $30$ paquetes de globos. El paquete de serpentinas vale $4$ € y el "
                     r"de globos $3$ €, y no quiere gastar más de $248$ €. ¿Cuántos paquetes de "
                     r"serpentinas puede comprar?",
           respuesta=r"Con $s$ paquetes de serpentinas y $2s$ de globos: $2s \ge 30$ y "
                     r"$4s + 3(2s) \le 248$, o sea $15 \le s \le \num{24,8}$. Puede comprar entre "
                     r"$15$ y $24$ paquetes de serpentinas.", **INEC)
def _():
    r = symbols("r", real=True)
    assert solveset(2 * r >= 30, r, S.Reals) & solveset(4 * r + 6 * r <= 248, r, S.Reals) == \
        Interval(15, Q(124, 5))
    assert [k for k in range(100) if 2 * k >= 30 and 10 * k <= 248] == list(range(15, 25))


@ejercicio(id=nid(), dificultad=2, fuente=f"{MODULO} 16",
           enunciado=r"La piscina del edificio A es un cuadrado y la del edificio B es un "
                     r"rectángulo: uno de sus lados mide lo mismo que el lado del cuadrado y el otro "
                     r"mide $6$ m. ¿Para qué medidas del lado del cuadrado el perímetro de la piscina "
                     r"A es mayor que el de la piscina B?",
           respuesta=r"Con $x$ el lado del cuadrado (en m): $4x > 2x + 12$, o sea $x > 6$. El lado "
                     r"del cuadrado debe medir más de $6$ m.", **INEC)
def _():
    r = symbols("r", real=True)
    assert solveset(4 * r > 2 * r + 12, r, Interval.open(0, oo)) == Interval.open(6, oo)


@ejercicio(id=nid(), dificultad=3, fuente=f"{MODULO} 17",
           enunciado=r"Pedro tiene $87$ € para comprar todos los discos de su cantante preferido. "
                     r"Si cada disco costara $23$ €, no le alcanzaría el dinero, pero si costara "
                     r"$15$ €, le sobraría. ¿Cuántos discos tiene el cantante?",
           respuesta=r"Con $n$ discos: $23n > 87$ y $15n < 87$, o sea $\num{3,78} < n < \num{5,8}$ "
                     r"(aproximadamente). Como $n$ es un número natural, el cantante tiene $4$ o "
                     r"$5$ discos (los datos no permiten decidir entre los dos).", **INEC)
def _():
    assert [k for k in range(1, 100) if 23 * k > 87 and 15 * k < 87] == [4, 5]
