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
from sympy import Eq, solve, symbols

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
