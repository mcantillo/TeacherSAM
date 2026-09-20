"""Banco de ejercicios — Matemáticas (Geometría 7°) — Transformaciones rígidas en el plano:
traslación, rotación, reflexión, composición y congruencia.
Escritos para la guía de Geometría 7°, trimestre I («Escher: el arte de mover figuras»), desde el
DBA 5 de grado 7. El banco no tenía ningún ejercicio de transformaciones (ningún grado); regla de
la docente del 2026-09-15: uno por tema, lo mínimo. Coordenadas con enteros (Matemáticas 7°).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/transformaciones-7.py
"""
from sympy import Line, Point, Polygon, pi, simplify

from ejercicios import ejercicio

FUENTE = "propio (guía Geometría 7°, trimestre I), desde el DBA 5 de grado 7"
COMUN = dict(grados=[7], dba=["matematicas-7-5"])
O = Point(0, 0)
EJE_X, EJE_Y = Line(O, Point(1, 0)), Line(O, Point(0, 1))


def lados(P):
    return sorted(simplify(s.length) for s in P.sides)


@ejercicio(id="transformaciones-7-001", tema="traslaciones", tipo="calculo", dificultad=1,
           fuente=FUENTE,
           enunciado=r"Traslada el triángulo de vértices $A(1, 1)$, $B(4, 1)$ y $C(2, 3)$ con el "
                     r"vector $\langle 3, 2 \rangle$ (3 unidades a la derecha y 2 hacia arriba). "
                     r"Escribe las coordenadas de $A'$, $B'$ y $C'$ y dibuja las dos figuras.",
           respuesta=r"$A'(4, 3)$, $B'(7, 3)$, $C'(5, 5)$.", **COMUN)
def _():
    T = [Point(1, 1), Point(4, 1), Point(2, 3)]
    assert [p.translate(3, 2) for p in T] == [Point(4, 3), Point(7, 3), Point(5, 5)]


@ejercicio(id="transformaciones-7-004", tema="rotaciones", tipo="calculo", dificultad=2,
           fuente=FUENTE,
           enunciado=r"Gira el punto $P(3, 1)$ alrededor del origen: a) $90^\circ$ en sentido "
                     r"antihorario; b) $180^\circ$; c) $90^\circ$ en sentido horario. Usa papel "
                     r"cuadriculado y una escuadra para comprobar cada giro.",
           respuesta=r"a) $(-1, 3)$; b) $(-3, -1)$; c) $(1, -3)$.", **COMUN)
def _():
    P = Point(3, 1)
    assert P.rotate(pi / 2) == Point(-1, 3)
    assert P.rotate(pi) == Point(-3, -1)
    assert P.rotate(-pi / 2) == Point(1, -3)


@ejercicio(id="transformaciones-7-009", tema="reflexiones", tipo="encuentra-el-error",
           dificultad=2, fuente=FUENTE,
           enunciado=r"Valentina afirma: «reflejar una figura respecto al eje $y$ es lo mismo que "
                     r"girarla $180^\circ$ alrededor del origen». Encuentra el error con el punto "
                     r"$(2, 3)$ y explica qué diferencia hay entre las dos figuras que se obtienen "
                     r"con una letra F.",
           respuesta=r"La reflexión da $(-2, 3)$ y el giro da $(-2, -3)$: no son iguales. Una "
                     r"reflexión invierte la figura (la F queda «al revés», como en un espejo); un "
                     r"giro solo la voltea sin invertirla (la F queda de cabeza, pero se puede "
                     r"leer girando la hoja).", **COMUN)
def _():
    A = Point(2, 3)
    assert A.reflect(EJE_Y) == Point(-2, 3) and A.rotate(pi) == Point(-2, -3)
    # orientación: la reflexión invierte el sentido de los vértices; la rotación no
    T = [Point(0, 0), Point(2, 0), Point(0, 1)]
    assert Polygon(*T).area > 0
    assert Polygon(*[p.reflect(EJE_Y) for p in T]).area < 0
    assert Polygon(*[p.rotate(pi) for p in T]).area > 0


@ejercicio(id="transformaciones-7-012", tema="transformaciones", tipo="conceptual", dificultad=2,
           fuente=FUENTE,
           enunciado=r"Aplica al triángulo $A(0, 0)$, $B(3, 0)$, $C(0, 2)$ un giro de $90^\circ$ "
                     r"antihorario alrededor del origen y luego una traslación con "
                     r"$\langle 5, 1 \rangle$. Halla la figura final y compara las longitudes de sus "
                     r"lados con las del triángulo original. ¿Son congruentes? ¿Por qué?",
           respuesta=r"Giro: $(0, 0)$, $(0, 3)$, $(-2, 0)$. Traslación: $A''(5, 1)$, $B''(5, 4)$, "
                     r"$C''(3, 1)$. Los lados miden 2, 3 y $\sqrt{13}$ en los dos triángulos: son "
                     r"congruentes, porque giros y traslaciones no cambian las medidas.", **COMUN)
def _():
    T = [Point(0, 0), Point(3, 0), Point(0, 2)]
    F = [p.rotate(pi / 2).translate(5, 1) for p in T]
    assert F == [Point(5, 1), Point(5, 4), Point(3, 1)]
    assert lados(Polygon(*F)) == lados(Polygon(*T))


# --- Añadidos el 2026-09-20 para el taller de la sesión 004 (semana 04) ---------------
# La guía usa el 001 como único ejercicio de traslaciones y no quedaban libres. Estos
# cuatro sostienen el taller: aplicar el vector, deducirlo, componer dos, y el error típico.


@ejercicio(id="transformaciones-7-020", tema="traslaciones", tipo="calculo", dificultad=1,
           fuente=FUENTE,
           enunciado=r"Traslada el cuadrilátero de vértices $P(-2, 1)$, $Q(1, 1)$, $R(2, 3)$ y "
                     r"$S(-1, 3)$ con el vector $\langle 4, -3 \rangle$. Escribe las coordenadas "
                     r"de $P'$, $Q'$, $R'$ y $S'$, y dibuja las dos figuras en la cuadrícula.",
           respuesta=r"$P'(2, -2)$, $Q'(5, -2)$, $R'(6, 0)$, $S'(3, 0)$. Ojo con el signo: la "
                     r"segunda coordenada del vector es negativa, así que la figura baja.",
           **COMUN)
def _():
    F = [Point(-2, 1), Point(1, 1), Point(2, 3), Point(-1, 3)]
    assert [p.translate(4, -3) for p in F] == [Point(2, -2), Point(5, -2), Point(6, 0), Point(3, 0)]


@ejercicio(id="transformaciones-7-021", tema="traslaciones", tipo="calculo", dificultad=2,
           fuente=FUENTE,
           enunciado=r"Una baldosa con un vértice en $A(2, 5)$ se deslizó hasta quedar con ese "
                     r"vértice en $A'(7, 2)$. ¿Cuál fue el vector de la traslación? Si otro "
                     r"vértice de la baldosa estaba en $B(4, 5)$, ¿dónde quedó?",
           respuesta=r"El vector es $\langle 7 - 2,\; 2 - 5 \rangle = \langle 5, -3 \rangle$. "
                     r"Entonces $B'(4 + 5,\; 5 - 3) = B'(9, 2)$. El vector se halla restando "
                     r"\emph{la original a la imagen}, no al revés.",
           **COMUN)
def _():
    A, Ap, B = Point(2, 5), Point(7, 2), Point(4, 5)
    v = (Ap.x - A.x, Ap.y - A.y)
    assert v == (5, -3)
    assert B.translate(*v) == Point(9, 2)


@ejercicio(id="transformaciones-7-022", tema="traslaciones", tipo="argumentacion", dificultad=2,
           fuente=FUENTE,
           enunciado=r"En un papel de colgadura, una figura se traslada primero con "
                     r"$\langle 3, 1 \rangle$ y después el resultado se traslada con "
                     r"$\langle 2, 4 \rangle$. ¿Se puede llegar al mismo sitio con una sola "
                     r"traslación? Si se puede, di con qué vector, y comprueba con el punto "
                     r"$M(0, 0)$. ¿Cambia algo si se hacen en el otro orden?",
           respuesta=r"Sí: basta la traslación de vector $\langle 3 + 2,\; 1 + 4 \rangle = "
                     r"\langle 5, 5 \rangle$. Con $M(0,0)$: primero llega a $(3, 1)$ y luego a "
                     r"$(5, 5)$, lo mismo que con el vector único. El orden no cambia nada, "
                     r"porque sumar números se puede hacer en cualquier orden. Por eso en los "
                     r"teselados de Escher la figura se repite siempre igual, se recorra la fila "
                     r"hacia donde se recorra.",
           notas="El punto es que la composición de traslaciones es otra traslación, y que es "
                 "conmutativa; sostiene el paso al teselado del tema 6.",
           **COMUN)
def _():
    M = Point(0, 0)
    assert M.translate(3, 1).translate(2, 4) == M.translate(5, 5) == Point(5, 5)
    assert M.translate(2, 4).translate(3, 1) == Point(5, 5)


@ejercicio(id="transformaciones-7-023", tema="traslaciones", tipo="argumentacion", dificultad=2,
           fuente=FUENTE,
           enunciado=r"Mateo trasladó el punto $T(-3, 4)$ con el vector $\langle 2, -6 \rangle$ y "
                     r"escribió $T'(-5, 10)$. Encuentra el error, corrígelo y explica en una "
                     r"frase cómo se puede comprobar el resultado sin volver a hacer la cuenta.",
           respuesta=r"Mateo restó en vez de sumar. Lo correcto es "
                     r"$T'(-3 + 2,\; 4 - 6) = T'(-1, -2)$. Para comprobarlo basta dibujar: el "
                     r"punto debe quedar 2 unidades a la derecha y 6 hacia abajo del original, y "
                     r"el de Mateo quedó a la izquierda y arriba, justo al contrario.",
           **COMUN)
def _():
    T = Point(-3, 4)
    assert T.translate(2, -6) == Point(-1, -2)
    assert T.translate(-2, 6) == Point(-5, 10)  # lo que hizo Mateo
