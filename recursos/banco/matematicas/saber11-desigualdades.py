"""Banco de ejercicios — Matemáticas — Preparación Saber 11: desigualdades, modelos y sistemas.
Fuente: módulo de Matemáticas 11° de las Guías de Apoyo (Adriana Quintero Palomino), Tema 2,
«Prepárate para el ICFES»; se lee en
recursos/matematicas/Guías pedagógicas Matemáticas/markdown/11 - Modulo_Matematicas_Undecimo.md
El módulo no trae clave: las respuestas se calcularon y se comprueban aquí.
No se incluyó el problema 2 (lámparas, literales a–e): depende de la figura y sus enunciados
están confusos («las lámparas B y C tienen la misma potencia que B», opción «(-r_b, x + r_b)»);
queda a decisión de la docente.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/saber11-desigualdades.py
"""
from sympy import Interval, Rational, S, oo, solve, solveset, sqrt, symbols

from ejercicios import ejercicio

FUENTE = "módulo 11° (Quintero Palomino), Tema 2, Prepárate para el ICFES"
COMUN = dict(grados=[11], tipo="seleccion", dificultad=2)

x, y, t, p = symbols("x y t p", real=True)


def opciones(*items):
    return r" \begin{opciones} " + " ".join(r"\item " + i for i in items) + r" \end{opciones}"


# ---------- Programación lineal (introducción de la sección) ----------

@ejercicio(
    id="saber11-desigualdades-001", tema="desigualdades lineales en dos variables",
    grados=[11], dba=["matematicas-11-2"], tipo="contexto", dificultad=3,
    fuente=f"{FUENTE}, pregunta 1 de la introducción",
    enunciado=r"Una fábrica produce $x$ artículos de un tipo y $y$ de otro cada día, a un costo "
              r"de \$5000 y \$7000 por artículo, respectivamente, y el costo diario no debe "
              r"superar los \$2\,000\,000: $5000x + 7000y \le 2\,000\,000$. Si además el número "
              r"de artículos $y$ no puede superar el doble del número de artículos $x$, "
              r"representa gráficamente la región de las posibilidades.",
    respuesta=r"Los puntos del primer cuadrante que están debajo de la recta "
              r"$5000x + 7000y = 2\,000\,000$ y debajo de la recta $y = 2x$: el triángulo de "
              r"vértices $(0, 0)$, $(400, 0)$ y $\left(\frac{2000}{19}, \frac{4000}{19}\right) "
              r"\approx (\num{105,3}; \num{210,5})$ (en la práctica, sus puntos de coordenadas "
              r"enteras).",
    notas="En el módulo: «artículos del producto x y v»; se escribe x y y.")
def _():
    corte = solve([5000 * x + 7000 * y - 2000000, y - 2 * x], [x, y])
    assert corte == {x: Rational(2000, 19), y: Rational(4000, 19)}
    assert solve(5000 * x - 2000000, x) == [400]
    dentro = lambda a, b: 5000 * a + 7000 * b <= 2000000 and b <= 2 * a and a >= 0 and b >= 0
    assert dentro(100, 100) and not dentro(10, 100) and not dentro(300, 100)


@ejercicio(
    id="saber11-desigualdades-002", tema="desigualdades lineales en dos variables",
    grados=[11], dba=["matematicas-11-2"], tipo="calculo", dificultad=2,
    fuente=f"{FUENTE}, pregunta 2 de la introducción",
    enunciado=r"Representa gráficamente la región de los puntos $(x, y)$ que cumplen a la vez "
              r"$x + 3y < 6$ y $2x < 3y$.",
    respuesta=r"Los puntos que están debajo de la recta $x + 3y = 6$ y encima de la recta "
              r"$y = \frac{2}{3}x$, que se cortan en $\left(2, \frac{4}{3}\right)$; las dos "
              r"rectas van punteadas porque las desigualdades son estrictas. Por ejemplo, "
              r"$(0, 1)$ está en la región y $(3, 0)$ no.")
def _():
    assert solve([x + 3 * y - 6, 2 * x - 3 * y], [x, y]) == {x: 2, y: Rational(4, 3)}
    region = lambda a, b: a + 3 * b < 6 and 2 * a < 3 * b
    assert region(0, 1) and not region(3, 0) and not region(0, 3)


# ---------- 1. Tarifas de acueducto ----------

ACUEDUCTO = (r"La empresa de acueducto de Bogotá cobra una tarifa preferencial a quienes "
             r"consumen menos de $40$ m³ de agua al mes. Para esos consumos, el valor de la "
             r"tarifa de acueducto es $y = 1033x + 13\,830$ (en pesos), donde $x$ es el consumo "
             r"en m³ y \$13\,830 es el cargo fijo. ")


@ejercicio(
    id="saber11-desigualdades-003", tema="inecuaciones de primer grado",
    dba=["matematicas-11-2", "matematicas-11-7"], fuente=f"{FUENTE}, problema 1a",
    enunciado=ACUEDUCTO + r"Si un usuario quiere pagar por acueducto un valor que esté entre el "
              r"doble y el triple del cargo fijo, debe consumir mensualmente entre:" + opciones(
                  r"$13\,830$ y $27\,660$ m³",
                  r"$\dfrac{13\,830}{1033}$ y $\dfrac{27\,660}{1033}$ m³",
                  r"$\dfrac{27\,660}{1033}$ y $\dfrac{41\,490}{1033}$ m³",
                  r"$\dfrac{13\,830}{22}$ y $\dfrac{27\,660}{22}$ m³"),
    respuesta=r"b) $2(13\,830) \le 1033x + 13\,830 \le 3(13\,830) \iff 13\,830 \le 1033x \le "
              r"27\,660$: entre $\dfrac{13\,830}{1033} \approx \num{13,4}$ y "
              r"$\dfrac{27\,660}{1033} \approx \num{26,8}$ m³.", **COMUN)
def _():
    correcta = solveset((1033 * x + 13830 - 2 * 13830) * (1033 * x + 13830 - 3 * 13830) <= 0,
                        x, S.Reals)
    opcion = {"a": (13830, 27660), "b": (Rational(13830, 1033), Rational(27660, 1033)),
              "c": (Rational(27660, 1033), Rational(41490, 1033)),
              "d": (Rational(13830, 22), Rational(27660, 22))}
    assert [k for k, v in opcion.items() if Interval(*v) == correcta] == ["b"]
    assert correcta.sup < 40                                  # sigue en la tarifa preferencial


@ejercicio(
    id="saber11-desigualdades-004", tema="funciones lineales a trozos",
    dba=["matematicas-11-7"], fuente=f"{FUENTE}, problema 1b",
    enunciado=r"Cuando el consumo está entre $41$ y $80$ m³, el metro cúbico cuesta \$1420 y la "
              r"tarifa básica es de \$13\,830. Para calcular el mayor valor que paga un usuario "
              r"que consume menos de $80$ m³ (se cobran metros cúbicos completos), se debe "
              r"hacer:" + opciones(r"$13\,830 \times 79 + 1420$", r"$1420 \times 80 + 13\,830$",
                                   r"$1420 \times 13\,830 + 79$", r"$1420 \times 79 + 13\,830$"),
    respuesta=r"d) El mayor consumo menor que $80$ m³ es $79$ m³: "
              r"$1420 \times 79 + 13\,830 = 126\,010$ pesos.",
    notas="Se agregó «(se cobran metros cúbicos completos)»; «X» del módulo pasa a ×.", **COMUN)
def _():
    valor = {"a": 13830 * 79 + 1420, "b": 1420 * 80 + 13830, "c": 1420 * 13830 + 79,
             "d": 1420 * 79 + 13830}
    maximo = max(1420 * c + 13830 for c in range(41, 80))     # consumos enteros de 41 a 79
    assert [k for k, v in valor.items() if v == maximo] == ["d"] and maximo == 126010


@ejercicio(
    id="saber11-desigualdades-005", tema="funciones lineales a trozos",
    dba=["matematicas-11-7"], fuente=f"{FUENTE}, problema 1c",
    enunciado=r"Con las tarifas anteriores (\$1033 por m³ hasta $40$ m³ y \$1420 por m³ entre "
              r"$41$ y $80$ m³), ¿cuál gráfica representa la relación entre la cantidad de "
              r"metros cúbicos consumidos y el costo de ese consumo, sin el cargo fijo? Cada "
              r"gráfica está formada por dos segmentos:" + opciones(
                  r"de $(0, 0)$ a $(40; 55\,150)$ y de $(40; 70\,630)$ a $(80; 127\,430)$",
                  r"de $(0, 0)$ a $(40; 41\,320)$ y de $(40; 56\,800)$ a $(80; 113\,600)$",
                  r"de $(0, 0)$ a $(40; 1030)$ y de $(40; 1030)$ a $(80; 1420)$",
                  r"de $(0, 0)$ a $(40; 55\,150)$ y de $(40; 55\,150)$ a $(80; 127\,430)$"),
    respuesta=r"b) Hasta $40$ m³ el costo es $1033x$ ($1033 \cdot 40 = 41\,320$) y desde ahí "
              r"es $1420x$ ($1420 \cdot 40 = 56\,800$, $1420 \cdot 80 = 113\,600$). La gráfica "
              r"a suma el cargo fijo, pero entonces no podría empezar en $(0, 0)$.",
    notas="Se agregó «sin el cargo fijo» (sin eso la opción a también se podría defender). "
          "Las gráficas son imágenes en el módulo: se describen con sus segmentos. En la "
          "opción d el módulo dice «(40, 551500)», error de digitación de 55 150.", **COMUN)
def _():
    costo = lambda m: 1033 * m if m <= 40 else 1420 * m
    graficas = {"a": [(0, 0), (40, 55150), (40, 70630), (80, 127430)],
                "b": [(0, 0), (40, 41320), (40, 56800), (80, 113600)],
                "c": [(0, 0), (40, 1030), (40, 1030), (80, 1420)],
                "d": [(0, 0), (40, 55150), (40, 55150), (80, 127430)]}
    esperado = [(0, 0), (40, costo(40)), (40, 1420 * 40), (80, costo(80))]
    assert [k for k, v in graficas.items() if v == esperado] == ["b"]
    assert all(b == c + 13830 for (_, b), (_, c) in zip(graficas["a"][1:], esperado[1:]))


@ejercicio(
    id="saber11-desigualdades-006", tema="ecuaciones de primer grado",
    dba=["matematicas-11-7"], fuente=f"{FUENTE}, problema 1d",
    enunciado=r"Si la tarifa básica se mantiene en \$13\,830 y un usuario que consume entre "
              r"$79$ y $81$ m³ paga entre \$126\,010 y \$140\,190, el valor del metro cúbico "
              r"de agua se puede calcular aplicando:" + opciones(
                  "una ecuación lineal.", "una proporción.", "una regla de tres.",
                  "una ecuación cuadrática."),
    respuesta=r"a) $13\,830 + 79p = 126\,010$ da $p = 1420$ pesos por m³ (y con $81$ m³, "
              r"$p = 1560$, la tarifa de más de $80$ m³). No es una proporción ni una regla de "
              r"tres: por el cargo fijo, lo que se paga no es proporcional al consumo.", **COMUN)
def _():
    assert solve(13830 + 79 * p - 126010, p) == [1420]
    assert solve(13830 + 81 * p - 140190, p) == [1560]
    assert Rational(126010, 79) != 1420                       # no es proporcional


# ---------- 3. Concierto de salsa ----------

SALSA = (r"Un empresario trae un grupo de salsa para las fiestas de fin de año. Las boletas "
         r"cuestan \$20\,000 para damas y \$25\,000 para caballeros, y el empresario le pagará "
         r"al grupo \$5000 por cada boleta de \$20\,000 y \$8000 por cada boleta de \$25\,000. ")
COMUN_SALSA = dict(tema="sistemas de ecuaciones lineales",
                   dba=["matematicas-11-7", "matematicas-11-2"], **COMUN)
d, c = symbols("d c", real=True)


@ejercicio(
    id="saber11-desigualdades-007", fuente=f"{FUENTE}, problema 3a",
    enunciado=SALSA + r"Si entran $6000$ personas y de un género entra el doble que del otro, "
              r"los valores mínimo y máximo que puede ganar el grupo son:" + opciones(
                  r"\$36\,000\,000 y \$48\,000\,000", r"\$36\,000\,000 y \$42\,000\,000",
                  r"\$42\,000\,000 y \$48\,000\,000", r"\$150\,000\,000 y \$300\,000\,000"),
    respuesta=r"b) Entran $4000$ de un género y $2000$ del otro. Con $4000$ damas: "
              r"$4000 \cdot 5000 + 2000 \cdot 8000 = 36\,000\,000$; con $4000$ caballeros: "
              r"$2000 \cdot 5000 + 4000 \cdot 8000 = 42\,000\,000$.",
    notas="En el módulo ninguna opción es correcta (a: 48 y 36 millones; b: 56 y 42; c: 42 y "
          "48; d: 150 y 300); se cambiaron las opciones a, b y c. «Dos veces más de un género "
          "que del otro» se lee como «el doble».", **COMUN_SALSA)
def _():
    ganancia = lambda damas, caballeros: 5000 * damas + 8000 * caballeros
    casos = [ganancia(4000, 2000), ganancia(2000, 4000)]
    assert (min(casos), max(casos)) == (36000000, 42000000)
    opcion = {"a": (36000000, 48000000), "b": (36000000, 42000000),
              "c": (42000000, 48000000), "d": (150000000, 300000000)}
    assert [k for k, v in opcion.items() if v == (min(casos), max(casos))] == ["b"]


@ejercicio(
    id="saber11-desigualdades-008", fuente=f"{FUENTE}, problema 3b",
    enunciado=SALSA + r"Si la boletería vendida suma \$120 millones y entraron $5000$ personas, "
              r"¿cuántas mujeres entraron?" + opciones(
                  r"$2000$ mujeres.", r"$1000$ mujeres.", r"$15\,000$ mujeres.",
                  r"$500$ mujeres."),
    respuesta=r"b) $d + c = 5000$ y $20\,000d + 25\,000c = 120\,000\,000$: "
              r"$125\,000\,000 - 5000d = 120\,000\,000$, luego $d = 1000$ mujeres.",
    notas="El módulo pregunta «la menor cantidad de mujeres», pero la cantidad es única.",
    **COMUN_SALSA)
def _():
    sol = solve([d + c - 5000, 20000 * d + 25000 * c - 120000000], [d, c])
    assert sol == {d: 1000, c: 4000}
    assert [k for k, v in {"a": 2000, "b": 1000, "c": 15000, "d": 500}.items()
            if v == sol[d]] == ["b"]


@ejercicio(
    id="saber11-desigualdades-009", fuente=f"{FUENTE}, problema 3c",
    enunciado=SALSA + r"Si se garantiza la entrada de $6000$ personas y se venden \$130 millones "
              r"en boletas, ¿qué par de rectas representa estas condiciones? (En el eje "
              r"horizontal, el número de damas; en el vertical, el de caballeros.)" + opciones(
                  r"una recta horizontal por $5200$ y otra por $(0, 6000)$ y $(6000, 0)$",
                  r"una recta por $(0, 0)$ y $(6000, 6000)$, y otra por $(0, 5200)$ y "
                  r"$(6500, 0)$",
                  r"una recta por $(0, 5200)$ y $(6500, 0)$, y otra por $(0, 6000)$ y "
                  r"$(6000, 0)$",
                  r"una recta horizontal por $5200$ y otra por $(0, 0)$ y $(6000, 6000)$"),
    respuesta=r"c) $d + c = 6000$ corta los ejes en $(6000, 0)$ y $(0, 6000)$; "
              r"$20\,000d + 25\,000c = 130\,000\,000$ los corta en $(6500, 0)$ y $(0, 5200)$.",
    notas="Las gráficas son imágenes en el módulo: se describen con sus rectas; se aclaró qué "
          "va en cada eje.", **COMUN_SALSA)
def _():
    cortes = lambda ec: (solve(ec.subs(c, 0), d)[0], solve(ec.subs(d, 0), c)[0])
    assert cortes(d + c - 6000) == (6000, 6000)
    assert cortes(20000 * d + 25000 * c - 130000000) == (6500, 5200)


@ejercicio(
    id="saber11-desigualdades-010", fuente=f"{FUENTE}, problema 3d",
    enunciado=SALSA + r"Si entran $6000$ personas y se venden \$130 millones en boletas, "
              r"¿cuánto dinero ganará el grupo?" + opciones(
                  r"\$42\,000\,000", r"\$40\,000\,000", r"\$36\,000\,000", r"\$20\,000\,000"),
    respuesta=r"c) De $d + c = 6000$ y $20\,000d + 25\,000c = 130\,000\,000$ salen $d = 4000$ "
              r"damas y $c = 2000$ caballeros: $4000 \cdot 5000 + 2000 \cdot 8000 = "
              r"36\,000\,000$.",
    notas="El módulo pregunta por «el valor mínimo», pero el valor es único.", **COMUN_SALSA)
def _():
    sol = solve([d + c - 6000, 20000 * d + 25000 * c - 130000000], [d, c])
    ganancia = 5000 * sol[d] + 8000 * sol[c]
    assert ganancia == 36000000
    assert [k for k, v in {"a": 42000000, "b": 40000000, "c": 36000000, "d": 20000000}.items()
            if v == ganancia] == ["c"]


# ---------- 4. Movimiento con modelo cuadrático ----------

MOVIMIENTO = (r"Un cuerpo se mueve según $y = 9t^2 + 18t$, donde $y$ es la distancia recorrida "
              r"en metros y $t$ el tiempo en segundos desde que inició su movimiento. ")
POSICION = 9 * t**2 + 18 * t
COMUN_MOV = dict(tema="inecuaciones cuadráticas", dba=["matematicas-11-2", "matematicas-11-7"],
                 **COMUN)


@ejercicio(
    id="saber11-desigualdades-011", fuente=f"{FUENTE}, problema 4a",
    enunciado=MOVIMIENTO + r"Si el cuerpo ha recorrido $72$ metros, ¿en qué intervalo de tiempo "
              r"recorrerá $63$ metros más?" + opciones(
                  r"Entre $2$ y $4$ s.", r"Entre $3$ y $5$ s.", r"Entre $2$ y $3$ s.",
                  r"Entre $3$ y $4$ s."),
    respuesta=r"c) $9t^2 + 18t = 72$ en $t = 2$ y $9t^2 + 18t = 72 + 63 = 135$ en $t = 3$: "
              r"entre los $2$ y los $3$ segundos.",
    notas="El módulo dice «27 metros más»: se llegaría a 99 m en t = -1 + 2√3 ≈ 2,46 s y "
          "ninguna opción da ese intervalo; con 63 m (llegar a 135 m, como en el literal b) "
          "la opción c es exacta. El módulo presenta y = 9t² + 18t como caída libre y dice que "
          "el coeficiente de t² es la gravedad; no lo es (sería 4,9t² en el SI): se presenta "
          "solo como modelo.", **COMUN_MOV)
def _():
    inicio = solveset(POSICION - 72, t, Interval(0, oo))
    fin = solveset(POSICION - 135, t, Interval(0, oo))
    assert (inicio, fin) == ({2}, {3})
    opcion = {"a": (2, 4), "b": (3, 5), "c": (2, 3), "d": (3, 4)}
    assert [k for k, v in opcion.items() if v == (2, 3)] == ["c"]
    assert solveset(POSICION - 99, t, Interval(0, oo)) == {-1 + 2 * sqrt(3)}  # el dato original


@ejercicio(
    id="saber11-desigualdades-012", fuente=f"{FUENTE}, problema 4b",
    enunciado=MOVIMIENTO + r"¿En qué intervalo de tiempo el cuerpo pasa de los $135$ a los "
              r"$216$ metros?" + opciones(r"$(2, 5)$", r"$(1, 2)$", r"$(3, 4)$", r"$(3, 5)$"),
    respuesta=r"c) $135 < 9t^2 + 18t < 216$ con $t \ge 0$: $y(3) = 135$ y $y(4) = 216$, así "
              r"que $t \in (3, 4)$.", **COMUN_MOV)
def _():
    intervalo = solveset(POSICION > 135, t, Interval(0, oo)) & \
        solveset(POSICION < 216, t, Interval(0, oo))
    assert intervalo == Interval.open(3, 4)
    opcion = {"a": (2, 5), "b": (1, 2), "c": (3, 4), "d": (3, 5)}
    assert [k for k, v in opcion.items() if Interval.open(*v) == intervalo] == ["c"]


@ejercicio(
    id="saber11-desigualdades-013", fuente=f"{FUENTE}, problema 4c",
    enunciado=MOVIMIENTO + r"Entre $\frac{1}{3}$ s y $\frac{2}{3}$ s después de iniciado el "
              r"movimiento, el cuerpo está entre los $7$ y los $16$ metros. Para encontrar esos "
              r"valores se debe:" + opciones(
                  r"resolver la desigualdad $7 < 9t^2 + 18t < 16$.",
                  r"hallar la posición del cuerpo a los $\frac{1}{3}$ s y a los "
                  r"$\frac{2}{3}$ s.",
                  r"restar $\frac{2}{3} - \frac{1}{3}$ y calcular la posición al cabo de ese "
                  r"tiempo.",
                  r"resolver las ecuaciones $9t^2 + 18t = \frac{1}{3}$ y "
                  r"$9t^2 + 18t = \frac{2}{3}$."),
    respuesta=r"b) $y\left(\frac{1}{3}\right) = 1 + 6 = 7$ y "
              r"$y\left(\frac{2}{3}\right) = 4 + 12 = 16$. La opción a hace el camino inverso: "
              r"da los tiempos a partir de las distancias.", **COMUN_MOV)
def _():
    y_de = lambda s: POSICION.subs(t, s)
    assert (y_de(Rational(1, 3)), y_de(Rational(2, 3))) == (7, 16)
    assert y_de(Rational(2, 3) - Rational(1, 3)) != 16                       # la opción c falla
    tiempos = solveset(POSICION > 7, t, Interval(0, oo)) & solveset(POSICION < 16, t,
                                                                    Interval(0, oo))
    assert tiempos == Interval.open(Rational(1, 3), Rational(2, 3))          # a: el inverso
