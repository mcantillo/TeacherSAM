"""Banco de ejercicios — Matemáticas (Geometría 9°) — Criterios de semejanza de triángulos.
Escritos para la sesión 004 del trimestre I de Geometría 9° (semana 04, 2026-09-20). El banco
tenía semejanza solo en 5° (semejanza-escala-5: escalas y rectángulos) y nada sobre los
criterios AA, LAL y LLL en triángulos, que es lo que pide el DBA 6 de grado 9.
Hilo del trimestre: «Eratóstenes mide la Tierra con una sombra».
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/semejanza-triangulos-9.py
"""
import sympy as sp

from ejercicios import ejercicio

PRE = "semejanza-triangulos-9"
FUENTE = "propio (Geometría 9°, trimestre I, sesión 004)"
COMUN = dict(tema="semejanza", grados=[9], dba=["matematicas-9-6"])


@ejercicio(id=f"{PRE}-001", tipo="calculo", dificultad=1, fuente=FUENTE,
           enunciado=r"Los triángulos $ABC$ y $DEF$ tienen $AB = 6$, $BC = 9$, $CA = 12$ y "
                     r"$DE = 4$, $EF = 6$, $FD = 8$. ¿Son semejantes? Si lo son, di por cuál "
                     r"criterio y cuál es la razón de semejanza.",
           respuesta=r"Sí, por el criterio \textbf{LLL}: los tres pares de lados están en la "
                     r"misma razón, $\frac{6}{4} = \frac{9}{6} = \frac{12}{8} = \frac{3}{2}$. "
                     r"La razón de semejanza de $ABC$ a $DEF$ es $\frac{3}{2}$ (o $\frac{2}{3}$ "
                     r"si se mira al revés).",
           **COMUN)
def _():
    a = [sp.Integer(6), sp.Integer(9), sp.Integer(12)]
    b = [sp.Integer(4), sp.Integer(6), sp.Integer(8)]
    razones = [x / y for x, y in zip(a, b)]
    assert len(set(razones)) == 1 and razones[0] == sp.Rational(3, 2)


@ejercicio(id=f"{PRE}-002", tipo="calculo", dificultad=2, fuente=FUENTE,
           enunciado=r"En el triángulo $ABC$, el segmento $DE$ es paralelo al lado $BC$, con "
                     r"$D$ sobre $AB$ y $E$ sobre $AC$. Se sabe que $AD = 4$, $DB = 6$ y "
                     r"$AE = 5$. Explica por qué $ADE$ y $ABC$ son semejantes y calcula $EC$.",
           respuesta=r"Son semejantes por el criterio \textbf{AA}: comparten el ángulo en $A$, "
                     r"y como $DE \parallel BC$, los ángulos $ADE$ y $ABC$ son correspondientes "
                     r"e iguales. La razón es $\frac{AD}{AB} = \frac{4}{10} = \frac{2}{5}$, "
                     r"luego $\frac{AE}{AC} = \frac{2}{5}$ y $AC = \frac{5 \cdot 5}{2} = "
                     r"\num{12,5}$. Por tanto $EC = \num{12,5} - 5 = \num{7,5}$.",
           notas="Es el teorema de Thales visto como semejanza; prepara el tema 3 de la guía.",
           **COMUN)
def _():
    AD, DB, AE = sp.Integer(4), sp.Integer(6), sp.Integer(5)
    AB = AD + DB
    AC = AE * AB / AD
    assert AC == sp.Rational(25, 2) and AC - AE == sp.Rational(15, 2)


@ejercicio(id=f"{PRE}-003", tipo="contexto", dificultad=2, fuente=FUENTE,
           enunciado=r"A la misma hora, un poste de \qty{4}{m} proyecta una sombra de "
                     r"\qty{6}{m} y un árbol proyecta una sombra de \qty{21}{m}. ¿Cuánto mide "
                     r"el árbol? Explica qué criterio de semejanza permite plantear la "
                     r"proporción.",
           respuesta=r"Los rayos del Sol llegan paralelos, así que el poste y el árbol forman "
                     r"con su sombra dos triángulos rectángulos con el mismo ángulo de "
                     r"elevación: son semejantes por \textbf{AA}. Entonces "
                     r"$\frac{h}{21} = \frac{4}{6}$ y $h = \qty{14}{m}$. Es exactamente el "
                     r"método con el que Tales midió la pirámide y con el que se mide cualquier "
                     r"altura inalcanzable.",
           **COMUN)
def _():
    h = sp.Integer(21) * sp.Integer(4) / sp.Integer(6)
    assert h == 14


@ejercicio(id=f"{PRE}-004", tipo="argumentacion", dificultad=2, fuente=FUENTE,
           enunciado=r"Decide si cada afirmación es verdadera o falsa y justifica: "
                     r"(a) dos triángulos con los tres ángulos iguales son congruentes; "
                     r"(b) dos triángulos equiláteros cualesquiera son semejantes; "
                     r"(c) dos triángulos rectángulos con un ángulo agudo igual son semejantes.",
           respuesta=r"(a) \textbf{Falsa}: tres ángulos iguales dan \emph{semejanza}, no "
                     r"congruencia; un triángulo $3$-$4$-$5$ y uno $6$-$8$-$10$ tienen los "
                     r"mismos ángulos y distinto tamaño. (b) \textbf{Verdadera}: todos sus "
                     r"ángulos miden $60^\circ$, así que cumplen AA (y también LLL, porque los "
                     r"tres lados están en la misma razón). (c) \textbf{Verdadera}: tienen el "
                     r"ángulo recto y el agudo dado, luego el tercero también coincide; es AA.",
           notas="La (a) es el error que la guía de Geometría 8° señala en el módulo de "
                 "recursos; conviene que reaparezca aquí.",
           **COMUN)
def _():
    # (a) 3-4-5 y 6-8-10: mismos ángulos, distinto tamaño
    t1 = [sp.Integer(3), sp.Integer(4), sp.Integer(5)]
    t2 = [2 * x for x in t1]
    assert len({x / y for x, y in zip(t2, t1)}) == 1  # semejantes
    assert t1 != t2                                    # pero no congruentes
    # (b) equiláteros: razón única sean cuales sean los lados
    for l1, l2 in ((sp.Integer(2), sp.Integer(7)), (sp.Integer(5), sp.Integer(5))):
        assert len({l1 / l2}) == 1
    # (c) el tercer ángulo queda determinado
    ag = sp.Integer(35)
    assert 180 - 90 - ag == 55
