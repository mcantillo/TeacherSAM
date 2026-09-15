"""Banco de ejercicios — Matemáticas (Geometría 5°) — Ubicación: sistemas de referencia, plano
cartesiano (primer cuadrante), trayectorias en cuadrícula y mapas.

Escritos para la guía del trimestre I de Geometría 5° («Cali, mi ciudad»):
materias/geometria/quinto/guia-didactica/guia-periodo-I-ubicacion.plan.md (etapa B).
Las figuras de la guía se describen aquí como datos (SALON, COLEGIO, MAPA); el enunciado
remite a la figura y la comprobación usa esos mismos datos.
Acuerdos: en la cuadrícula del salón, (fila, columna), filas A–D desde el tablero y columnas
1–5 de izquierda a derecha (lo enseñado en la semana 03); en el plano, (x, y) con x hacia la
derecha (oriente) e y hacia arriba (norte); solo el primer cuadrante.
Reutiliza plano-cartesiano-5-005 (el origen); no duplica nada del banco.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/ubicacion-5.py
"""
from itertools import combinations
from collections import deque

from sympy import Point, Matrix

from ejercicios import ejercicio, ejercicio_manual

FUENTE = "propio (guía Geometría 5°, trimestre I, «Cali, mi ciudad»)"
COMUN = dict(grados=[5], dba=["matematicas-5-7"])

# --------------------------------------------------------------------------------------------
# Tema 1 — Sistemas de referencia
# --------------------------------------------------------------------------------------------
FILAS = "ABCD"          # A es la fila más cercana al tablero
SALON = {("A", 2): "Sofía", ("A", 5): "el escritorio", ("B", 4): "Andrés",
         ("C", 1): "Isabela", ("C", 4): "Juliana", ("D", 3): "Nicolás", ("D", 5): "el estante"}
POS = {v: k for k, v in SALON.items()}
T1 = dict(tema="sistemas de referencia", **COMUN)


@ejercicio(id="ubicacion-5-001", tipo="calculo", dificultad=1, fuente=FUENTE,
           enunciado=r"En la cuadrícula del salón, ¿en qué posición está Andrés? ¿Quién está en "
                     r"$(D, 3)$?",
           respuesta=r"Andrés está en $(B, 4)$: fila $B$, columna 4. En $(D, 3)$ está Nicolás.",
           notas="Ejemplo resuelto de la explicación del tema 1.", **T1)
def _():
    assert POS["Andrés"] == ("B", 4) and SALON[("D", 3)] == "Nicolás"


@ejercicio(id="ubicacion-5-002", tipo="calculo", dificultad=1, fuente=FUENTE,
           enunciado=r"Usa la cuadrícula del salón. Escribe la posición (fila, columna) de Sofía y "
                     r"de Isabela, y di qué hay en $(A, 5)$ y en $(D, 5)$.",
           respuesta=r"Sofía: $(A, 2)$. Isabela: $(C, 1)$. En $(A, 5)$ está el escritorio y en "
                     r"$(D, 5)$, el estante.", **T1)
def _():
    assert POS["Sofía"] == ("A", 2) and POS["Isabela"] == ("C", 1)
    assert SALON[("A", 5)] == "el escritorio" and SALON[("D", 5)] == "el estante"


@ejercicio(id="ubicacion-5-003", tipo="encuentra-el-error", dificultad=2, fuente=FUENTE,
           enunciado=r"Camilo le dice a Tatiana que Andrés está en $(C, 4)$, porque contó las "
                     r"filas desde el fondo del salón y no desde el tablero. Encuentra el error: "
                     r"¿a quién encontraría Tatiana en $(C, 4)$? ¿Cuál es la posición correcta de "
                     r"Andrés y por qué?",
           respuesta=r"En $(C, 4)$ Tatiana encontraría a Juliana, no a Andrés. La posición correcta "
                     r"es $(B, 4)$: el acuerdo del salón es contar las filas desde el tablero. Si "
                     r"cada uno cuenta desde un lugar distinto, el mismo par señala puestos "
                     r"distintos.", **T1)
def _():
    desde_fondo = {f: FILAS[::-1][i] for i, f in enumerate(FILAS)}   # A↔D, B↔C
    fila, col = POS["Andrés"]
    leido = (desde_fondo[fila], col)
    assert leido == ("C", 4) and SALON[leido] == "Juliana" != "Andrés"


# Plano del colegio (norte arriba): lugares alrededor del patio, como vectores (oriente, norte)
COLEGIO = {"la biblioteca": (0, 1), "la cafetería": (1, 0), "el coliseo": (0, -1),
           "la portería": (-1, 0)}
CARDINAL = {"norte": (0, 1), "oriente": (1, 0), "sur": (0, -1), "occidente": (-1, 0)}
IZQUIERDA = Matrix([[0, -1], [1, 0]])        # girar 90° a la izquierda


def lugar(direccion):
    return next(k for k, v in COLEGIO.items() if v == tuple(direccion))


@ejercicio(id="ubicacion-5-004", tipo="calculo", dificultad=1, fuente=FUENTE,
           enunciado=r"Observa el plano del colegio (el norte está arriba). Tatiana está en el "
                     r"patio. ¿Qué lugar queda al norte del patio? Si camina hacia el occidente, "
                     r"¿a dónde llega? Si se para mirando hacia donde sale el Sol, ¿qué lugar "
                     r"tiene a su izquierda y cuál a su espalda?",
           respuesta=r"Al norte, la biblioteca. Hacia el occidente llega a la portería. Mirando "
                     r"hacia la salida del Sol (el oriente), a su izquierda queda el norte, la "
                     r"biblioteca, y a su espalda el occidente, la portería.", **T1)
def _():
    assert lugar(CARDINAL["norte"]) == "la biblioteca"
    assert lugar(CARDINAL["occidente"]) == "la portería"
    mira = Matrix(CARDINAL["oriente"])
    assert lugar(IZQUIERDA * mira) == "la biblioteca"
    assert lugar(-mira) == "la portería"


ejercicio_manual(id="ubicacion-5-005", tipo="conceptual", dificultad=2, fuente=FUENTE,
                 enunciado=r"Diseña un sistema de referencia para la biblioteca del colegio o para "
                           r"el parqueadero: dibuja la cuadrícula, nombra filas y columnas y "
                           r"escribe en dos o tres renglones las reglas, para que Tatiana pueda "
                           r"encontrar tres lugares que tú marques.",
                 respuesta=r"Respuesta abierta. Debe tener: un punto de partida claro (desde dónde "
                           r"se cuentan filas y columnas), una forma de nombrarlas (letras y "
                           r"números, por ejemplo), el orden en que se escribe el par y tres "
                           r"lugares con su posición escrita según esas reglas.", **T1)

# --------------------------------------------------------------------------------------------
# Tema 2 — El plano cartesiano (primer cuadrante)
# --------------------------------------------------------------------------------------------
T2 = dict(tema="plano cartesiano", **COMUN)


def camino_desde_origen(x, y):
    """Punto al que se llega desde el origen: x unidades a la derecha, y hacia arriba."""
    return Point(0, 0) + Point(x, 0) + Point(0, y)


@ejercicio(id="ubicacion-5-006", tipo="calculo", dificultad=1, fuente=FUENTE,
           enunciado=r"Ubica el punto $P(2, 3)$ en el plano cartesiano. ¿Es el mismo punto que "
                     r"$(3, 2)$?",
           respuesta=r"Desde el origen se avanzan 2 unidades a la derecha y luego 3 hacia arriba. "
                     r"$(3, 2)$ es otro punto: 3 a la derecha y 2 hacia arriba.",
           notas="Ejemplo resuelto de la explicación del tema 2.", **T2)
def _():
    assert camino_desde_origen(2, 3) == Point(2, 3) != Point(3, 2)


@ejercicio(id="ubicacion-5-007", tipo="contexto", dificultad=1,
           fuente="módulo 5° (Guías de Apoyo), Tema 5, Parejas ordenadas y distancias — "
                  "explicación (el banco a 3 cuadras al oriente y 2 al norte)",
           enunciado=r"Desde el hotel de Tatiana, que está en el origen, el banco queda 3 cuadras "
                     r"al oriente y 2 al norte. ¿Qué par ordenado le corresponde al banco?",
           respuesta=r"$(3, 2)$: oriente es hacia la derecha (el primer número) y norte es hacia "
                     r"arriba (el segundo).",
           notas="Ejemplo resuelto de la explicación del tema 2, adaptado del módulo.", **T2)
def _():
    x = 3 * CARDINAL["oriente"][0] + 2 * CARDINAL["norte"][0]
    y = 3 * CARDINAL["oriente"][1] + 2 * CARDINAL["norte"][1]
    assert Point(x, y) == Point(3, 2)


PUNTOS = {"A": (1, 4), "B": (4, 2), "C": (5, 5), "D": (0, 3), "E": (6, 0)}


@ejercicio(id="ubicacion-5-008", tipo="calculo", dificultad=1, fuente=FUENTE,
           enunciado=r"Escribe las coordenadas de los puntos $A$, $B$, $C$, $D$ y $E$ del plano. "
                     r"¿Cuáles están sobre un eje y sobre cuál?",
           respuesta=r"$A(1, 4)$, $B(4, 2)$, $C(5, 5)$, $D(0, 3)$, $E(6, 0)$. $D$ está sobre el "
                     r"eje $y$ (su $x$ es 0) y $E$ sobre el eje $x$ (su $y$ es 0).", **T2)
def _():
    assert all(x >= 0 and y >= 0 for x, y in PUNTOS.values())          # primer cuadrante
    assert [k for k, (x, y) in PUNTOS.items() if x == 0] == ["D"]
    assert [k for k, (x, y) in PUNTOS.items() if y == 0] == ["E"]


@ejercicio(id="ubicacion-5-009", tipo="argumentacion", dificultad=2, fuente=FUENTE,
           enunciado=r"Ponemos la cuadrícula del salón sobre un plano cartesiano: las columnas "
                     r"1 a 5 son los valores de $x$, y las filas se numeran de abajo hacia arriba "
                     r"($D$ es $y = 1$, $C$ es $y = 2$, $B$ es $y = 3$ y $A$, la del tablero, es "
                     r"$y = 4$). Escribe la posición de Andrés como (fila, columna) y como par "
                     r"$(x, y)$. ¿Por qué el dato de la columna pasó a ser el primero?",
           respuesta=r"(fila, columna): $(B, 4)$. Par ordenado: $(4, 3)$. En el plano cartesiano "
                     r"se escribe primero la distancia horizontal ($x$), que en el salón es la "
                     r"columna, y después la vertical ($y$), que es la fila. Son dos acuerdos "
                     r"distintos para el mismo puesto.", **T2)
def _():
    y_de_fila = {f: 4 - i for i, f in enumerate(FILAS)}                 # A=4, B=3, C=2, D=1
    fila, col = POS["Andrés"]
    assert (fila, col) == ("B", 4) and (col, y_de_fila[fila]) == (4, 3)
    assert (col, y_de_fila[fila]) != (y_de_fila[fila], col)             # el orden importa


# (literal, cuadras al oriente, cuadras al norte) desde el hotel en el origen
INSTR = [("a", 4, 1), ("b", 0, 5)]
PARES = [("c", (6, 2)), ("d", (3, 0))]


@ejercicio(id="ubicacion-5-010", tipo="calculo", dificultad=1, fuente=FUENTE,
           enunciado=r"El hotel de Tatiana está en el origen. Escribe el par ordenado de cada "
                     r"lugar: a) 4 cuadras al oriente y 1 al norte; b) 5 cuadras al norte. "
                     r"Escribe con puntos cardinales cómo llegar a: c) $(6, 2)$; d) $(3, 0)$.",
           respuesta=r"a) $(4, 1)$. b) $(0, 5)$. c) 6 cuadras al oriente y 2 al norte. "
                     r"d) 3 cuadras al oriente (no hay que subir).", **T2)
def _():
    assert [camino_desde_origen(e, n) for _, e, n in INSTR] == [Point(4, 1), Point(0, 5)]
    assert [(p[0], p[1]) for _, p in PARES] == [(6, 2), (3, 0)]
    assert camino_desde_origen(6, 2) == Point(6, 2) and camino_desde_origen(3, 0) == Point(3, 0)


@ejercicio(id="ubicacion-5-011", tipo="calculo", dificultad=2, fuente=FUENTE,
           enunciado=r"Tres vértices de un rectángulo son $(1, 1)$, $(5, 1)$ y $(5, 4)$. ¿Cuál es "
                     r"el cuarto vértice? ¿Cuánto miden la base y la altura?",
           respuesta=r"El cuarto vértice es $(1, 4)$. La base mide 4 unidades y la altura, 3.", **T2)
def _():
    a, b, c = Point(1, 1), Point(5, 1), Point(5, 4)
    d = a + (c - b)
    assert d == Point(1, 4)
    ab, bc = b - a, c - b
    assert ab.dot(bc) == 0                                              # ángulo recto en B
    assert (d - c).dot(a - d) == 0 and a.distance(b) == 4 and b.distance(c) == 3


# --------------------------------------------------------------------------------------------
# Tema 3 — Trayectorias (solo por las calles de la cuadrícula)
# --------------------------------------------------------------------------------------------
T3 = dict(tema="trayectorias", **COMUN)


def recorrer(inicio, pasos):
    """pasos: lista de (cuadras, dirección cardinal). Devuelve los puntos de giro y la longitud."""
    x, y = inicio
    puntos, largo = [(x, y)], 0
    for n, d in pasos:
        dx, dy = CARDINAL[d]
        x, y = x + n * dx, y + n * dy
        puntos.append((x, y))
        largo += n
    return puntos, largo


def manhattan(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


@ejercicio(id="ubicacion-5-012", tipo="calculo", dificultad=1, fuente=FUENTE,
           enunciado=r"Del hotel $(1, 1)$ al zoológico $(4, 3)$: compara el camino «3 al oriente y "
                     r"2 al norte», el camino «2 al norte y 3 al oriente» y el camino «4 al "
                     r"oriente, 2 al norte y 1 al occidente».",
           respuesta=r"Los tres llegan a $(4, 3)$. Los dos primeros miden 5 cuadras, que es lo "
                     r"mínimo; el tercero mide 7, porque se pasa una cuadra y tiene que volver.",
           notas="Ejemplo resuelto de la explicación del tema 3.", **T3)
def _():
    caminos = [[(3, "oriente"), (2, "norte")], [(2, "norte"), (3, "oriente")],
               [(4, "oriente"), (2, "norte"), (1, "occidente")]]
    res = [recorrer((1, 1), c) for c in caminos]
    assert all(p[-1] == (4, 3) for p, _ in res)
    assert [l for _, l in res] == [5, 5, 7] and manhattan((1, 1), (4, 3)) == 5


@ejercicio(id="ubicacion-5-013", tipo="calculo", dificultad=1, fuente=FUENTE,
           enunciado=r"Tatiana sale de $(0, 2)$ y sigue estas instrucciones: 3 cuadras al "
                     r"oriente, 2 al norte, 1 al oriente y 1 al sur. Dibuja la trayectoria en "
                     r"papel cuadriculado. ¿Por qué puntos gira? ¿A qué punto llega? ¿Cuántas "
                     r"cuadras camina?",
           respuesta=r"Gira en $(3, 2)$, $(3, 4)$ y $(4, 4)$; llega a $(4, 3)$. Camina 7 cuadras.",
           **T3)
def _():
    puntos, largo = recorrer((0, 2), [(3, "oriente"), (2, "norte"), (1, "oriente"), (1, "sur")])
    assert puntos[1:-1] == [(3, 2), (3, 4), (4, 4)] and puntos[-1] == (4, 3) and largo == 7


@ejercicio(id="ubicacion-5-014", tipo="calculo", dificultad=1, fuente=FUENTE,
           enunciado=r"Observa la trayectoria dibujada: sale de $(1, 4)$, pasa por $(1, 1)$ y por "
                     r"$(6, 1)$, y termina en $(6, 3)$. Escribe las instrucciones con puntos "
                     r"cardinales y di cuántas cuadras mide.",
           respuesta=r"3 cuadras al sur, 5 al oriente y 2 al norte: 10 cuadras en total.", **T3)
def _():
    pts = [(1, 4), (1, 1), (6, 1), (6, 3)]
    puntos, largo = recorrer((1, 4), [(3, "sur"), (5, "oriente"), (2, "norte")])
    assert puntos == pts and largo == sum(manhattan(p, q) for p, q in zip(pts, pts[1:])) == 10


def caminos_cortos(p, q):
    """Todos los caminos más cortos de p a q (q al nororiente de p) como listas de 'E'/'N'."""
    e, n = q[0] - p[0], q[1] - p[1]
    return [["N" if i in pos else "E" for i in range(e + n)] for pos in combinations(range(e + n), n)]


@ejercicio(id="ubicacion-5-015", tipo="argumentacion", dificultad=2, fuente=FUENTE,
           enunciado=r"Tatiana va de la biblioteca $(2, 1)$ al parque $(5, 4)$ por las calles. "
                     r"Propón dos caminos más cortos distintos y di cuánto mide cada uno. ¿Cuántas "
                     r"cuadras al oriente y cuántas al norte tiene cualquier camino más corto? ¿Qué "
                     r"pasa con un camino que da una vuelta de más?",
           respuesta=r"Por ejemplo, «3 al oriente y 3 al norte» y «1 al norte, 3 al oriente y 2 al "
                     r"norte»: los dos miden 6 cuadras. Todo camino más corto tiene 3 cuadras al "
                     r"oriente y 3 al norte, en cualquier orden. Un camino con una vuelta de más "
                     r"mide más: por cada cuadra que se devuelve hay que caminar esa cuadra de "
                     r"regreso (por ejemplo, 8 cuadras).", **T3)
def _():
    cs = caminos_cortos((2, 1), (5, 4))
    assert len(cs) == 20 and all(c.count("E") == 3 and c.count("N") == 3 for c in cs)
    for pasos in ([(3, "oriente"), (3, "norte")], [(1, "norte"), (3, "oriente"), (2, "norte")]):
        pts, largo = recorrer((2, 1), pasos)
        assert pts[-1] == (5, 4) and largo == 6
    pts, largo = recorrer((2, 1), [(4, "oriente"), (3, "norte"), (1, "occidente")])
    assert pts[-1] == (5, 4) and largo == 8


CERRADAS = {(2, 0), (2, 1), (2, 2)}


def bfs(inicio, fin, cerradas, xmax=6, ymax=4):
    dist = {inicio: 0}
    cola = deque([inicio])
    while cola:
        p = cola.popleft()
        for dx, dy in CARDINAL.values():
            q = (p[0] + dx, p[1] + dy)
            if 0 <= q[0] <= xmax and 0 <= q[1] <= ymax and q not in cerradas and q not in dist:
                dist[q] = dist[p] + 1
                cola.append(q)
    return dist.get(fin)


@ejercicio(id="ubicacion-5-016", tipo="contexto", dificultad=3, fuente=FUENTE,
           enunciado=r"Tatiana está en $(0, 1)$ y quiere llegar al parque, en $(4, 1)$. Las "
                     r"esquinas $(2, 0)$, $(2, 1)$ y $(2, 2)$ están cerradas por obras y no se "
                     r"puede pasar por ellas. Caminando solo por las calles de la cuadrícula (de "
                     r"$x = 0$ a $x = 6$ y de $y = 0$ a $y = 4$), ¿cuál es un camino más corto? "
                     r"¿Cuántas cuadras mide? ¿Cuántas cuadras de más camina por culpa de las obras?",
           respuesta=r"Por ejemplo: 2 cuadras al norte, 4 al oriente y 2 al sur (pasa por "
                     r"$(0, 3)$ y $(4, 3)$). Mide 8 cuadras; sin obras serían 4, así que camina 4 "
                     r"cuadras de más.", **T3)
def _():
    assert bfs((0, 1), (4, 1), CERRADAS) == 8 and bfs((0, 1), (4, 1), set()) == 4
    pts, largo = recorrer((0, 1), [(2, "norte"), (4, "oriente"), (2, "sur")])
    assert pts[-1] == (4, 1) and largo == 8
    # el camino propuesto no pisa esquinas cerradas: recorre x = 0 (y 1..3), y = 3, x = 4
    tramo = [(0, y) for y in range(1, 4)] + [(x, 3) for x in range(5)] + [(4, y) for y in range(1, 4)]
    assert not CERRADAS & set(tramo)


# --------------------------------------------------------------------------------------------
# Tema 4 — Mapas y planos (mapa simplificado del barrio, sin escala)
# --------------------------------------------------------------------------------------------
T4 = dict(tema="mapas y planos", **COMUN)
MAPA = {"el hotel": (1, 1), "la estación del MIO": (4, 1), "la biblioteca": (2, 4),
        "el parque": (5, 3), "la iglesia": (7, 5), "el museo": (6, 1)}


def relativo(a, b):
    """Cómo ir de b a a: (cuadras al oriente, cuadras al norte), con signo."""
    return MAPA[a][0] - MAPA[b][0], MAPA[a][1] - MAPA[b][1]


@ejercicio(id="ubicacion-5-017", tipo="calculo", dificultad=1, fuente=FUENTE,
           enunciado=r"En el mapa del barrio, ¿dónde queda el parque y cómo se llega desde el hotel?",
           respuesta=r"El parque está en $(5, 3)$; desde el hotel $(1, 1)$ hay que caminar 4 "
                     r"cuadras al oriente y 2 al norte.",
           notas="Ejemplo resuelto de la explicación del tema 4.", **T4)
def _():
    assert MAPA["el parque"] == (5, 3) and relativo("el parque", "el hotel") == (4, 2)


@ejercicio(id="ubicacion-5-018", tipo="calculo", dificultad=1, fuente=FUENTE,
           enunciado=r"En el mapa del barrio, ¿qué lugar está en $(2, 4)$? ¿Y en $(6, 1)$? Escribe "
                     r"las coordenadas de la iglesia y de la estación del MIO.",
           respuesta=r"En $(2, 4)$, la biblioteca; en $(6, 1)$, el museo. La iglesia está en "
                     r"$(7, 5)$ y la estación del MIO en $(4, 1)$.", **T4)
def _():
    inv = {v: k for k, v in MAPA.items()}
    assert inv[(2, 4)] == "la biblioteca" and inv[(6, 1)] == "el museo"
    assert MAPA["la iglesia"] == (7, 5) and MAPA["la estación del MIO"] == (4, 1)


@ejercicio(id="ubicacion-5-019", tipo="calculo", dificultad=1, fuente=FUENTE,
           enunciado=r"Usa el mapa del barrio y los puntos cardinales. Describe dónde queda: "
                     r"a) la iglesia respecto al parque; b) la biblioteca respecto al museo; "
                     r"c) el hotel respecto a la estación del MIO.",
           respuesta=r"a) 2 cuadras al oriente y 2 al norte del parque. b) 4 cuadras al occidente "
                     r"y 3 al norte del museo. c) 3 cuadras al occidente de la estación, en la "
                     r"misma calle.", **T4)
def _():
    assert relativo("la iglesia", "el parque") == (2, 2)
    assert relativo("la biblioteca", "el museo") == (-4, 3)
    assert relativo("el hotel", "la estación del MIO") == (-3, 0)


def largo_ruta(lugares):
    return sum(manhattan(MAPA[a], MAPA[b]) for a, b in zip(lugares, lugares[1:]))


RUTA = ["el hotel", "la biblioteca", "el parque", "la iglesia"]


@ejercicio(id="ubicacion-5-020", tipo="contexto", dificultad=3, fuente=FUENTE,
           enunciado=r"Escríbele a Tatiana un mensaje con el recorrido hotel → biblioteca → parque "
                     r"→ iglesia: las coordenadas de cada lugar, las instrucciones de cada tramo "
                     r"con puntos cardinales (por el camino más corto) y el total de cuadras.",
           respuesta=r"Hotel $(1, 1)$ → biblioteca $(2, 4)$: 1 al oriente y 3 al norte (4 cuadras). "
                     r"Biblioteca → parque $(5, 3)$: 3 al oriente y 1 al sur (4 cuadras). Parque "
                     r"→ iglesia $(7, 5)$: 2 al oriente y 2 al norte (4 cuadras). Total: 12 "
                     r"cuadras.",
           notas="Situación del ejemplo del DBA 7 de 5° (Tatiana).", **T4)
def _():
    tramos = [relativo(b, a) for a, b in zip(RUTA, RUTA[1:])]
    assert tramos == [(1, 3), (3, -1), (2, 2)]
    assert [abs(e) + abs(n) for e, n in tramos] == [4, 4, 4] and largo_ruta(RUTA) == 12


@ejercicio(id="ubicacion-5-021", tipo="argumentacion", dificultad=2, fuente=FUENTE,
           enunciado=r"Tatiana propone otro orden: hotel → parque → biblioteca → iglesia. ¿Cuántas "
                     r"cuadras camina así? ¿Cuál de los dos recorridos le conviene más y por qué?",
           respuesta=r"Hotel → parque: 6 cuadras; parque → biblioteca: 4; biblioteca → iglesia: 6. "
                     r"Total: 16 cuadras. Le conviene más el primero (12 cuadras): visita los "
                     r"mismos lugares caminando 4 cuadras menos.", **T4)
def _():
    otra = ["el hotel", "el parque", "la biblioteca", "la iglesia"]
    tramos = [manhattan(MAPA[a], MAPA[b]) for a, b in zip(otra, otra[1:])]
    assert tramos == [6, 4, 6] and largo_ruta(otra) == 16 and largo_ruta(RUTA) == 12
