"""Banco de ejercicios — Geometría 8° — Ángulos: vocabulario, demostraciones y paralelas.
Fuente: módulo de Geometría de las Guías de Apoyo (Adriana Quintero Palomino), Tema 1; se lee en
recursos/matematicas/Guías pedagógicas Matemáticas/markdown/Modulo_Matematicas_Geometria.md
Todos son de respuesta abierta (definir, demostrar): quedan manual-pendiente hasta que la
docente apruebe la respuesta modelo. DBA 7 de 8° («describe teoremas y argumenta su validez»).
No se incluyeron: Practica lo aprendido (1.ª) 2a–e (medir ángulos: dependen de las figuras,
que no traen medidas) y 3 (trazar la bisectriz de esos mismos ángulos).
En el banco no había ejercicios de este tema: nada duplicado.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/angulos-8.py
"""
from ejercicios import ejercicio_manual

REC = "módulo de Geometría (Quintero Palomino), Tema 1: Ángulos"
F1 = f"{REC}, Definición y clasificación de ángulos — Practica lo aprendido"
F2 = f"{REC}, Ángulos formados por dos rectas paralelas y una secante — Practica lo aprendido"
COMUN = dict(tema="ángulos", grados=[8], dba=["matematicas-8-7"])

# 1. Investiga la definición (en matemáticas): (n, literal, término, respuesta modelo)
TERMINOS = [
    (1, "1a", "definición",
     r"Enunciado que precisa el significado de un término usando términos ya conocidos. "
     r"Ejemplo: «ángulo recto es el que mide $90^\circ$»."),
    (2, "1b", "axioma",
     r"Proposición que se acepta como verdadera sin demostración y sirve de punto de partida. "
     r"Ejemplo: «dos cantidades iguales a una tercera son iguales entre sí»."),
    (3, "1c", "postulado",
     r"Proposición (en geometría) que se acepta sin demostración. Ejemplo: el postulado de las "
     r"paralelas de Euclides: por un punto exterior a una recta pasa una sola paralela a ella."),
    (4, "1d", "teorema",
     r"Proposición que se demuestra a partir de definiciones, axiomas, postulados y teoremas ya "
     r"probados. Ejemplo: los ángulos opuestos por el vértice son iguales."),
    (5, "1e", "lema",
     r"Teorema auxiliar que se demuestra para usarlo en la demostración de otro teorema."),
    (6, "1f", "corolario",
     r"Consecuencia inmediata de un teorema, que casi no necesita demostración. Ejemplo: cada "
     r"ángulo de un triángulo equilátero mide $60^\circ$ (de la suma de ángulos del triángulo)."),
    (7, "1g", "demostración",
     r"Razonamiento en el que cada paso se justifica con una definición, un axioma, un postulado "
     r"o un teorema ya probado, y que muestra que la conclusión se sigue de la hipótesis."),
    (8, "1h", "hipótesis",
     r"Lo que se supone verdadero en un teorema: la parte «si…». En «si dos ángulos son opuestos "
     r"por el vértice, entonces son iguales», la hipótesis es «son opuestos por el vértice»."),
    (9, "1i", "conclusión",
     r"Lo que el teorema afirma y hay que demostrar: la parte «entonces…». En el ejemplo "
     r"anterior, «son iguales»."),
    (10, "1j", "problema",
     r"Situación o pregunta que pide hallar algo (una medida, una construcción, una relación) "
     r"aplicando definiciones y teoremas."),
]
for n, literal, termino, modelo in TERMINOS:
    ejercicio_manual(id=f"angulos-8-{n:03d}", tipo="conceptual", dificultad=1,
                     fuente=f"{F1} {literal}",
                     enunciado=f"Investiga qué significa en matemáticas el término «{termino}» y "
                               f"da un ejemplo si es posible.",
                     respuesta=modelo, **COMUN)

ejercicio_manual(
    id="angulos-8-011", tipo="argumentacion", dificultad=2, fuente=f"{F1} 4",
    enunciado=r"Demuestra que si dos ángulos tienen el mismo conjugado, entonces son iguales.",
    respuesta=r"Sea $\xi$ el conjugado común de $\alpha$ y $\beta$. Por definición de ángulos "
              r"conjugados, $\alpha + \xi = 360^\circ$ y $\beta + \xi = 360^\circ$. Entonces "
              r"$\alpha = 360^\circ - \xi$ y $\beta = 360^\circ - \xi$; como los dos son iguales a "
              r"la misma cantidad, $\alpha = \beta$.", **COMUN)

ejercicio_manual(
    id="angulos-8-012", tipo="argumentacion", dificultad=2, fuente=f"{F1} 5",
    enunciado=r"Demuestra que si dos ángulos suplementarios son iguales, entonces cada uno es "
              r"un ángulo recto.",
    respuesta=r"Si $\alpha$ y $\beta$ son suplementarios, $\alpha + \beta = 180^\circ$. Como "
              r"$\alpha = \beta$, al sustituir queda $2\alpha = 180^\circ$, así que "
              r"$\alpha = 90^\circ$ y también $\beta = 90^\circ$: los dos son rectos.", **COMUN)

ejercicio_manual(
    id="angulos-8-013", tipo="argumentacion", dificultad=2, fuente=f"{F1} 6",
    enunciado=r"Demuestra que si dos ángulos complementarios son iguales, entonces cada uno "
              r"mide $45^\circ$.",
    respuesta=r"Si $\alpha$ y $\beta$ son complementarios, $\alpha + \beta = 90^\circ$. Como "
              r"$\alpha = \beta$, queda $2\alpha = 90^\circ$, así que $\alpha = \beta = 45^\circ$.",
    **COMUN)

# 1. Defina y grafique (dos paralelas cortadas por una secante)
PARALELAS = [
    (14, "1a", "los ángulos internos (o interiores)",
     r"Son los cuatro ángulos que quedan entre las dos paralelas. Dibujo: dos rectas paralelas "
     r"horizontales $l_1$ y $l_2$, una secante oblicua que las corta, y marcados los dos ángulos "
     r"de cada cruce que quedan en la franja entre $l_1$ y $l_2$.", None),
    (15, "1b", "los ángulos externos (o exteriores)",
     r"Son los cuatro ángulos que quedan fuera de la franja entre las paralelas: dos por encima "
     r"de $l_1$ y dos por debajo de $l_2$, en el mismo dibujo.", None),
    (16, "1c", "los ángulos alternos internos",
     r"Son pares de ángulos internos situados a lados opuestos de la secante y no adyacentes; "
     r"hay dos pares y, si las rectas son paralelas, los ángulos de cada par son iguales. "
     r"Dibujo: se marca el ángulo interno de $l_1$ a la derecha de la secante y el interno de "
     r"$l_2$ a la izquierda (forman una «Z»).",
     "En el módulo el literal c dice «Ángulos internos», que repite el a («Interiores»); se "
     "cambió por «alternos internos», otra de las clases de la sección."),
    (17, "1d", "los ángulos correspondientes",
     r"Son pares de ángulos del mismo lado de la secante, uno interno y otro externo, no "
     r"adyacentes (ocupan la misma posición en cada cruce); hay cuatro pares y, si las rectas "
     r"son paralelas, son iguales. Dibujo: se marca el ángulo de arriba a la derecha en el cruce "
     r"con $l_1$ y el de arriba a la derecha en el cruce con $l_2$ (forman una «F»).", None),
]
for n, literal, nombre, modelo, notas in PARALELAS:
    extra = dict(notas=notas) if notas else {}
    ejercicio_manual(id=f"angulos-8-{n:03d}", tipo="conceptual", dificultad=1,
                     fuente=f"{F2} {literal}",
                     enunciado=f"Dos rectas paralelas son cortadas por una secante. Define y "
                               f"dibuja {nombre}.",
                     respuesta=modelo, **extra, **COMUN)
