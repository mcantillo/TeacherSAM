"""Banco de ejercicios — Matemáticas (Geometría 6°) — Ángulos complementarios, suplementarios y
conjugados.
Fuente: módulo de Geometría de las Guías de Apoyo (Adriana Quintero Palomino), Tema 1: Ángulos
— «Practica lo aprendido» después de «Rectas oblicuas»; se lee en
recursos/matematicas/Guías pedagógicas Matemáticas/markdown/Modulo_Matematicas_Geometria.md
No se incluyeron: 1 (investigar «axioma, lema, corolario…»: vocabulario de demostración que no
pide ningún DBA de 3° a 6°), 2 (medir ángulos dibujados: dependen de la figura) y 3 (trazar la
bisectriz de los ángulos del 2). Tampoco la práctica de «Ángulos formados por dos rectas
paralelas y una secante» (definir y graficar), que no corresponde a un DBA de 3° a 6°.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/angulos-6.py
"""
from sympy import Eq, simplify, solve, symbols

from ejercicios import ejercicio

FUENTE = ("módulo de Geometría (Quintero Palomino), Tema 1, Ángulos, Rectas oblicuas — "
          "Practica lo aprendido")
COMUN = dict(tema="ángulos", grados=[6], dba=["matematicas-6-5"], tipo="argumentacion")
a, b, c = symbols("alpha beta gamma", real=True)


@ejercicio(id="angulos-6-001", dificultad=2, fuente=f"{FUENTE} 4",
           enunciado=r"Dos ángulos son conjugados si suman $360^\circ$. Demuestra que si dos "
                     r"ángulos tienen el mismo conjugado, entonces son iguales.",
           respuesta=r"Si $\gamma$ es el conjugado de $\alpha$ y de $\beta$, entonces "
                     r"$\alpha + \gamma = 360^\circ$ y $\beta + \gamma = 360^\circ$. Así, "
                     r"$\alpha = 360^\circ - \gamma$ y $\beta = 360^\circ - \gamma$, luego "
                     r"$\alpha = \beta$.",
           notas="Se escribió en el enunciado la definición de ángulos conjugados (del mismo "
                 "módulo).", **COMUN)
def _():
    sol = solve([Eq(a + c, 360), Eq(b + c, 360)], [a, b], dict=True)[0]
    assert sol[a] - sol[b] == 0


@ejercicio(id="angulos-6-002", dificultad=1, fuente=f"{FUENTE} 5",
           enunciado=r"Demuestra que si dos ángulos suplementarios son iguales, entonces cada uno "
                     r"es un ángulo recto.",
           respuesta=r"Si $\alpha = \beta$ y $\alpha + \beta = 180^\circ$, entonces "
                     r"$2\alpha = 180^\circ$, así que $\alpha = \beta = 90^\circ$: cada uno es "
                     r"recto.", **COMUN)
def _():
    assert solve([Eq(a, b), Eq(a + b, 180)], [a, b]) == {a: 90, b: 90}


@ejercicio(id="angulos-6-003", dificultad=1, fuente=f"{FUENTE} 6",
           enunciado=r"Demuestra que si dos ángulos complementarios son iguales, entonces cada "
                     r"uno mide $45^\circ$.",
           respuesta=r"Si $\alpha = \beta$ y $\alpha + \beta = 90^\circ$, entonces "
                     r"$2\alpha = 90^\circ$, así que $\alpha = \beta = 45^\circ$.", **COMUN)
def _():
    assert solve([Eq(a, b), Eq(a + b, 90)], [a, b]) == {a: 45, b: 45}


# --- Añadidos el 2026-09-20 para la semana 05 (ángulos entre rectas) ------------------
# El módulo de Quintero Palomino deja fuera «ángulos entre rectas» (adyacentes, opuestos por
# el vértice y bisectriz), que es el subtema de la sesión 005 de Geometría 6°. Son ejercicios
# propios; el tema y el DBA son los mismos del resto del archivo.
PROPIO = "propio — clase de Geometría 6°, trimestre I, ángulos entre rectas"


@ejercicio(id="angulos-6-004", tipo="calculo", dificultad=1, fuente=PROPIO,
           enunciado=r"Dos rectas se cortan y forman cuatro ángulos. Uno de ellos mide "
                     r"$47^\circ$. ¿Cuánto miden los otros tres? Di cuál de ellos es el opuesto "
                     r"por el vértice del primero.",
           respuesta=r"Los adyacentes miden $180^\circ - 47^\circ = 133^\circ$ cada uno, y el "
                     r"opuesto por el vértice mide $47^\circ$. En orden de giro: $47^\circ$, "
                     r"$133^\circ$, $47^\circ$, $133^\circ$. El opuesto por el vértice es el "
                     r"tercero, el que no comparte ningún lado con el primero.",
           **COMUN)
def _():
    ady = solve(Eq(47 + a, 180), a)[0]
    op = solve(Eq(ady + b, 180), b)[0]
    assert (ady, op) == (133, 47)
    assert 47 + ady + op + ady == 360


@ejercicio(id="angulos-6-005", tipo="calculo", dificultad=2, fuente=PROPIO,
           enunciado=r"Dos rectas se cortan. Uno de los ángulos mide $(3x + 10)^\circ$ y su "
                     r"opuesto por el vértice mide $(5x - 20)^\circ$. Halla $x$ y la medida de "
                     r"los cuatro ángulos.",
           respuesta=r"Los ángulos opuestos por el vértice son iguales: $3x + 10 = 5x - 20$, "
                     r"luego $2x = 30$ y $x = 15$. Cada uno de esos dos mide "
                     r"$3(15) + 10 = 55^\circ$, y los otros dos, $180^\circ - 55^\circ = "
                     r"125^\circ$.",
           **COMUN)
def _():
    x = symbols("x", real=True)
    xs = solve(Eq(3 * x + 10, 5 * x - 20), x)[0]
    assert xs == 15
    m = (3 * xs + 10)
    assert m == 55 and (5 * xs - 20) == 55
    assert solve(Eq(m + a, 180), a)[0] == 125
    assert 2 * 55 + 2 * 125 == 360


@ejercicio(id="angulos-6-006", dificultad=2, fuente=PROPIO,
           enunciado=r"Demuestra que dos ángulos opuestos por el vértice son iguales. "
                     r"(Sugerencia: los dos son adyacentes al mismo ángulo.)",
           respuesta=r"Sean $\alpha$ y $\beta$ opuestos por el vértice y $\gamma$ el ángulo "
                     r"adyacente a los dos. Entonces $\alpha + \gamma = 180^\circ$ y "
                     r"$\beta + \gamma = 180^\circ$, así que $\alpha = 180^\circ - \gamma$ y "
                     r"$\beta = 180^\circ - \gamma$: luego $\alpha = \beta$. No hace falta "
                     r"medirlos.",
           notas="Mismo razonamiento que el 001 (conjugados), pero con suplementarios; es la "
                 "demostración que sostiene el subtema de la sesión 005.",
           **COMUN)
def _():
    sol = solve([Eq(a + c, 180), Eq(b + c, 180)], [a, b], dict=True)[0]
    assert sol[a] - sol[b] == 0


@ejercicio(id="angulos-6-007", tipo="calculo", dificultad=2, fuente=PROPIO,
           enunciado=r"El ángulo $AOB$ mide $70^\circ$ y $BOC$ es su adyacente. $OM$ es la "
                     r"bisectriz de $AOB$ y $ON$ es la bisectriz de $BOC$. ¿Cuánto mide el "
                     r"ángulo $MON$? Repite la cuenta cambiando $70^\circ$ por otra medida: "
                     r"¿qué observas?",
           respuesta=r"$BOC = 180^\circ - 70^\circ = 110^\circ$. La bisectriz parte cada uno en "
                     r"dos: $MOB = 35^\circ$ y $BON = 55^\circ$, luego $MON = 35^\circ + "
                     r"55^\circ = 90^\circ$. Con cualquier otra medida da lo mismo: si $AOB = "
                     r"\alpha$, entonces $MON = \frac{\alpha}{2} + \frac{180^\circ - \alpha}{2} "
                     r"= 90^\circ$. Las bisectrices de dos ángulos adyacentes son siempre "
                     r"perpendiculares.",
           **COMUN)
def _():
    boc = solve(Eq(70 + a, 180), a)[0]
    assert boc == 110
    assert 70 / 2 + boc / 2 == 90
    alfa = symbols("alfa", real=True)
    assert simplify(alfa / 2 + (180 - alfa) / 2 - 90) == 0
