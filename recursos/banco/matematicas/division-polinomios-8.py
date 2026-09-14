"""Banco de ejercicios — Matemáticas 8° — División de polinomios.
Fuente: módulo de Matemáticas 8° de las Guías de Apoyo (Adriana Quintero Palomino), Tema 2;
se lee en recursos/matematicas/Guías pedagógicas Matemáticas/markdown/08 - Modulo_Matematicas_Octavo.md
(«Practica lo aprendido» de la sección «División de polinomios»).
No incluidos: los ejercicios 1 a 10 de esta sección. En el .docx del módulo sus fórmulas (dividendos,
divisores, la tabla del ejercicio 1, los volúmenes de los ejercicios 6 y 7 y los polinomios del 10)
no están como texto ni como ecuaciones legibles: la copia en markdown/ y la de texto/ solo
conservan los divisores sueltos («(x + 3)», «( + 13m + 6) (2m + 3)»…), así que no se pueden
reconstruir con fidelidad. Si la docente tiene el módulo impreso, pueden transcribirse después.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/division-polinomios-8.py
"""
from ejercicios import ejercicio_manual

FUENTE = ("módulo 8° (Quintero Palomino), Tema 2, Expresiones algebraicas, División de "
          "polinomios — Practica lo aprendido")

ejercicio_manual(
    id="division-polinomios-8-001", tema="división de polinomios", grados=[8],
    dba=["matematicas-8-9"], tipo="argumentacion", dificultad=2, fuente=f"{FUENTE} 11",
    enunciado=r"¿Qué opinas del procedimiento de Ruffini-Horner (división sintética)? ¿Es útil? "
              r"¿Por qué?",
    respuesta=r"Respuesta modelo: es útil para dividir un polinomio entre un binomio de la forma "
              r"$x - a$, porque solo se trabaja con los coeficientes (sin escribir las letras), "
              r"lo que hace la división más corta y con menos errores; además, el residuo es el "
              r"valor $P(a)$ (teorema del residuo), así que sirve para evaluar polinomios y para "
              r"saber si $x - a$ es un factor (residuo $0$). Su limitación es que solo sirve para "
              r"divisores de la forma $x - a$ (o, ajustando, $bx - a$); para otros divisores hay "
              r"que usar la división larga.")
