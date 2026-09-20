"""Banco de ejercicios — Matemáticas (Geometría 5°) — Parejas ordenadas y distancias en el plano.
Fuente: módulo de Matemáticas 5° de las Guías de Apoyo, Tema 5, «Parejas ordenadas y
distancias» — Práctica lo aprendido; se lee en
recursos/matematicas/Guías pedagógicas Matemáticas/markdown/05 - Modulo_Matematicas_Quinto.md
No se incluyeron los ejercicios 8 a 13 y 15 de esa práctica (enteros, fracciones y decimales:
componente numérico); el 14 (área total del prisma) está en perimetro-area-5.py. El módulo
salta del ejercicio 5 al 7 (no hay 6).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/plano-cartesiano-5.py
"""
from sympy import Point

from ejercicios import ejercicio, ejercicio_manual

FUENTE = "módulo 5° (Guías de Apoyo), Tema 5, Parejas ordenadas y distancias — Práctica lo aprendido"
COMUN = dict(tema="plano cartesiano", grados=[5], dba=["matematicas-5-7"])

# 1. Distancia entre dos enteros de la recta: (n, literal, a, b, distancia a mano)
for n, lit, a, b, d in [(1, "1a", -4, 3, 7), (2, "1b", -5, -1, 4), (3, "1c", 4, 7, 3)]:
    @ejercicio(id=f"plano-cartesiano-5-{n:03d}", tipo="calculo", dificultad=1,
               fuente=f"{FUENTE} {lit}",
               enunciado=f"Halla la distancia entre los enteros ${a:+d}$ y ${b:+d}$ de la recta "
                         f"numérica.",
               respuesta=f"{d} unidades.", **COMUN)
    def _(a=a, b=b, d=d):
        assert abs(a - b) == d and len(range(min(a, b), max(a, b))) == d

ejercicio_manual(id="plano-cartesiano-5-004", tipo="conceptual", dificultad=1,
                 fuente=f"{FUENTE} 2",
                 enunciado=r"Describe cómo marcar el par ordenado $(-3, +4)$ en el plano "
                           r"cartesiano.",
                 respuesta=r"Se parte del origen, se avanzan 3 unidades hacia la izquierda sobre "
                           r"el eje $x$ (porque $-3$ es negativo) y luego 4 unidades hacia arriba, "
                           r"paralelo al eje $y$; allí se marca el punto. Queda en el segundo "
                           r"cuadrante.", **COMUN)


@ejercicio(id="plano-cartesiano-5-005", tipo="conceptual", dificultad=1, fuente=f"{FUENTE} 3",
           enunciado=r"¿Qué par ordenado representa el origen de cualquier plano cartesiano?",
           respuesta=r"$(0, 0)$.", **COMUN)
def _():
    origen = Point(0, 0)
    assert all(origen.distance(Point(*e)) == 0 for e in [(0, 0)])      # dista 0 de sí mismo
    assert all(origen.distance(Point(a, b)) > 0 for a, b in [(1, 0), (0, 1), (-2, 3)])


# 4. Grafica y halla la distancia: (n, literal, P, Q, distancia a mano)
PARES = [(6, "4a", (-5, -5), (-2, -5), 3), (7, "4b", (2, -4), (2, -5), 1),
         (8, "4c", (-4, 3), (1, 3), 5), (9, "4d", (-1, 4), (-1, -3), 7),
         (10, "4e", (4, -2), (4, 0), 2), (11, "4f", (0, 1), (0, -5), 6)]


def par(p):
    return "(" + ", ".join(f"{c:+d}" if c else "0" for c in p) + ")"


for n, lit, p, q, d in PARES:
    @ejercicio(id=f"plano-cartesiano-5-{n:03d}", tipo="calculo", dificultad=1,
               fuente=f"{FUENTE} {lit}",
               enunciado=f"Grafica y rotula los puntos ${par(p)}$ y ${par(q)}$ en el plano "
                         f"cartesiano. Luego halla la distancia entre ellos.",
               respuesta=f"Los dos puntos están en la misma línea de la cuadrícula; la distancia "
                         f"es {d} " + ("unidad." if d == 1 else "unidades."), **COMUN)
    def _(p=p, q=q, d=d):
        assert p[0] == q[0] or p[1] == q[1]           # se puede contar sobre la cuadrícula
        assert Point(*p).distance(Point(*q)) == d


PUNTOS = dict(D=(-1, 1), H=(2, 1), K=(5, 1), A=(-5, 2), C=(-3, 2), E=(0, 2), B=(-3, 4), F=(0, 4),
              G=(2, 4), J=(5, 4), N=(-3, -2), L=(2, -2), M=(4, -2), P=(-3, -4))
LISTA = ", ".join(f"${k}{par(v)}$" for k, v in PUNTOS.items())
CONTEXTO = f"En un plano cartesiano están marcados los puntos {LISTA}."
NOTA = "La figura del módulo se reemplazó por la lista de coordenadas de su descripción."


def a_distancia(centro, d):
    return sorted(k for k, v in PUNTOS.items()
                  if Point(*v).distance(Point(*PUNTOS[centro])) == d)


@ejercicio(id="plano-cartesiano-5-012", tipo="calculo", dificultad=2, fuente=f"{FUENTE} 5a",
           enunciado=CONTEXTO + r" ¿Qué punto está exactamente a 7 unidades del punto $N$?",
           respuesta=r"El punto $M(+4, -2)$: está en la misma fila que $N$ y "
                     r"$4 - (-3) = 7$.", notas=NOTA, **COMUN)
def _():
    assert a_distancia("N", 7) == ["M"]


@ejercicio(id="plano-cartesiano-5-013", tipo="calculo", dificultad=2, fuente=f"{FUENTE} 5b",
           enunciado=CONTEXTO + r" ¿Cuál es mayor: la distancia del punto $B$ al punto $N$ o la "
                     r"distancia del punto $A$ al punto $E$?",
           respuesta=r"La de $B$ a $N$: mide 6 unidades, y la de $A$ a $E$ mide 5.", notas=NOTA,
           **COMUN)
def _():
    bn = Point(*PUNTOS["B"]).distance(Point(*PUNTOS["N"]))
    ae = Point(*PUNTOS["A"]).distance(Point(*PUNTOS["E"]))
    assert (bn, ae) == (6, 5)


@ejercicio(id="plano-cartesiano-5-014", tipo="calculo", dificultad=2, fuente=f"{FUENTE} 7",
           enunciado=CONTEXTO + r" Enumera todos los puntos que están exactamente a 3 unidades "
                     r"del punto $H$.",
           respuesta=r"$D$, $G$, $K$ y $L$ (dos en la misma fila de $H$ y dos en la misma "
                     r"columna).", notas=NOTA + " En el módulo este ejercicio es el 7 (no hay 6).",
           **COMUN)
def _():
    assert a_distancia("H", 3) == ["D", "G", "K", "L"]


# --- Añadidos el 2026-09-20 para la semana 05 (ejes, origen y cuadrantes) -------------
# El módulo de 5° nombra los ejes y el origen, pero no trabaja los cuatro cuadrantes, que es
# la mitad del subtema de la sesión 005. Ejercicios propios, mismo tema y DBA del archivo.
PROPIO = "propio — clase de Geometría 5°, trimestre I, ejes, origen y cuadrantes"


def cuadrante(p):
    """Devuelve el cuadrante (I a IV) de un punto, o 0 si está sobre un eje."""
    x, y = p.x, p.y
    if x == 0 or y == 0:
        return 0
    return {(True, True): 1, (False, True): 2, (False, False): 3, (True, False): 4}[(x > 0, y > 0)]


@ejercicio(id="plano-cartesiano-5-015", tipo="conceptual", dificultad=1, fuente=PROPIO,
           enunciado=r"Di en qué cuadrante está cada punto: $A(3, 4)$, $B(-2, 5)$, $C(-4, -1)$ "
                     r"y $D(6, -3)$. Explica en qué te fijaste para decidirlo.",
           respuesta=r"$A$ en el I, $B$ en el II, $C$ en el III y $D$ en el IV. Basta mirar los "
                     r"dos signos: $(+,+)$ es el I, $(-,+)$ el II, $(-,-)$ el III y $(+,-)$ el "
                     r"IV. Los cuadrantes se numeran empezando arriba a la derecha y girando "
                     r"como las manecillas del reloj al revés.",
           **COMUN)
def _():
    assert [cuadrante(Point(3, 4)), cuadrante(Point(-2, 5)), cuadrante(Point(-4, -1)),
            cuadrante(Point(6, -3))] == [1, 2, 3, 4]


@ejercicio(id="plano-cartesiano-5-016", tipo="conceptual", dificultad=2, fuente=PROPIO,
           enunciado=r"¿En qué cuadrante están los puntos $E(0, -4)$, $F(-5, 0)$ y el origen? "
                     r"Si crees que alguno no está en ninguno, di dónde está.",
           respuesta=r"Ninguno de los tres está en un cuadrante: están \emph{sobre} los ejes. "
                     r"$E$ está en el eje $y$ (porque su $x$ es 0), $F$ está en el eje $x$ "
                     r"(porque su $y$ es 0) y el origen $(0,0)$ es el punto donde se cruzan los "
                     r"dos ejes. Los ejes son la frontera entre cuadrantes y no pertenecen a "
                     r"ninguno.",
           **COMUN)
def _():
    assert [cuadrante(Point(0, -4)), cuadrante(Point(-5, 0)), cuadrante(Point(0, 0))] == [0, 0, 0]


@ejercicio(id="plano-cartesiano-5-017", tipo="encuentra-el-error", dificultad=2, fuente=PROPIO,
           enunciado=r"Juan dice: «$(-3, 7)$ y $(7, -3)$ son el mismo punto, porque tienen los "
                     r"mismos números». Ubica los dos en el plano y explica por qué se equivoca.",
           respuesta=r"No son el mismo punto. En $(-3, 7)$ se camina 3 a la izquierda y 7 hacia "
                     r"arriba: queda en el cuadrante II. En $(7, -3)$ se camina 7 a la derecha y "
                     r"3 hacia abajo: queda en el cuadrante IV. En una pareja ordenada importa "
                     r"el orden: el primer número siempre es el horizontal.",
           **COMUN)
def _():
    p, q = Point(-3, 7), Point(7, -3)
    assert p != q
    assert (cuadrante(p), cuadrante(q)) == (2, 4)
