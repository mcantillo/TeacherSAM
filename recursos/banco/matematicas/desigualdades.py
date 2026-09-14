"""Banco de ejercicios — Matemáticas — Propiedades de las desigualdades.
Fuente: módulo de Matemáticas 11° de las Guías de Apoyo (Adriana Quintero Palomino), Tema 1;
se lee en recursos/matematicas/Guías pedagógicas Matemáticas/markdown/11 - Modulo_Matematicas_Undecimo.md
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/desigualdades.py
"""
from sympy import Rational, S

from ejercicios import desigualdad, ejercicio, ejercicio_manual, expresion

FUENTE = ("módulo 11° (Quintero Palomino), Tema 1, Propiedades de las desigualdades — "
          "Practica lo aprendido")
COMUN = dict(tema="propiedades de orden", grados=[11], dba=["matematicas-11-2"])

# Dado -6 > -9: (n, literal, operación, qué se hace a cada lado, respuesta escrita a mano, dif)
OPERACIONES = [
    (1, "1a", r"se suma $8$ a ambos lados", lambda v: v + 8, "2 > -1", 1),
    (2, "1b", r"se suma $-6$ a ambos lados", lambda v: v + (-6), "-12 > -15", 1),
    (3, "1c", r"se multiplican ambos lados por $2$", lambda v: 2 * v, "-12 > -18", 1),
    (4, "1d", r"se multiplican ambos lados por $-3$", lambda v: -3 * v, "18 < 27", 1),
    (5, "1e", r"se resta $-8$ a ambos lados", lambda v: v - (-8), "2 > -1", 1),
    (6, "1f", r"se dividen ambos lados entre $-6$", lambda v: Rational(v, -6), "1 < 3/2", 2),
    (7, "1g", r"se multiplican ambos lados por $1$", lambda v: 1 * v, "-6 > -9", 1),
    (8, "1h", r"se dividen ambos lados entre $1$", lambda v: Rational(v, 1), "-6 > -9", 1),
]
for n, literal, texto, operar, resultado, dificultad in OPERACIONES:
    invierte = "<" in resultado
    motivo = ("el sentido se invierte porque se operó con un número negativo" if invierte
              else "el sentido se conserva")

    @ejercicio(id=f"desigualdades-{n:03d}", tipo="calculo", dificultad=dificultad,
               fuente=f"{FUENTE} {literal}",
               enunciado=rf"Dado $-6 > -9$, escribe la desigualdad que se obtiene si {texto}.",
               respuesta=f"${desigualdad(resultado)[0]}$: {motivo}.", **COMUN)
    def _(operar=operar, resultado=resultado):
        izquierda, _, derecha = resultado.partition("<" if "<" in resultado else ">")
        assert expresion(izquierda) == operar(-6) and expresion(derecha) == operar(-9)
        assert desigualdad(resultado)[1] == S.Reals            # la desigualdad es verdadera


ejercicio_manual(
    id="desigualdades-009", tipo="conceptual", dificultad=1, fuente=f"{FUENTE} 2",
    enunciado=r"¿Qué sucede con una desigualdad si ambos lados se multiplican por cero?",
    respuesta=r"Los dos lados quedan en $0$: de $-6 > -9$ se pasaría a $0 > 0$, que es falso. "
              r"La desigualdad no se conserva; por eso la propiedad pide multiplicar por un "
              r"número distinto de cero (positivo para conservar el sentido, negativo para "
              r"invertirlo).", **COMUN)

ejercicio_manual(
    id="desigualdades-010", tipo="conceptual", dificultad=1, fuente=f"{FUENTE} 3",
    enunciado=r"¿Es posible dividir ambos lados de una desigualdad entre cero? Explica.",
    respuesta=r"No: la división entre cero no está definida, ni en las igualdades ni en las "
              r"desigualdades.", **COMUN)

ejercicio_manual(
    id="desigualdades-011", tipo="argumentacion", dificultad=2, fuente=f"{FUENTE} 4",
    enunciado=r"¿Cumplen las desigualdades las mismas propiedades de las igualdades?",
    respuesta=r"No todas. Sumar o restar el mismo número a ambos lados, y multiplicar o dividir "
              r"por un positivo, funciona igual que en las igualdades, y ambas relaciones son "
              r"transitivas. Pero al multiplicar o dividir por un negativo el sentido de la "
              r"desigualdad se invierte, y la desigualdad no es simétrica: $a < b$ no implica "
              r"$b < a$, mientras que $a = b$ sí implica $b = a$.", **COMUN)
