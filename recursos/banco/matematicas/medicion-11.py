"""Banco de ejercicios — Geometría 11° — Medición: áreas por triangulación, precisión y medición indirecta.
Fuente: módulo de Geometría de las Guías de Apoyo, que se lee en
recursos/matematicas/Guías pedagógicas Matemáticas/markdown/Modulo_Matematicas_Geometria.md
DBA 4 de grado 11 (mediciones con precisión creciente, mediciones indirectas) y DBA 6 (modelar
figuras en coordenadas cartesianas). El módulo es de geometría básica (ángulos, triángulos,
Pitágoras, polígonos, circunferencia) y no trae coordenadas polares ni esféricas; se tomaron las
partes que sirven para esos DBA:
  - Tema 4, «Perímetros y áreas», Ejemplos 1 a 4: los polígonos del módulo están dibujados en
    cuadrícula; aquí se dan sus vértices en coordenadas (leídos de las figuras del .docx) para que
    el ejercicio no dependa del dibujo. El Ejemplo 1 mide una base y una altura con regla, y el
    módulo comenta que la triangulación externa es «más exacta»: sirve para hablar de precisión.
  - Tema 3, «Practica lo aprendido», problemas 3 a 8 (diagonales: medición indirecta). Los
    ejercicios 1 y 2 (ternas pitagóricas) son de nivel 8° y no se incluyeron.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/medicion-11.py
"""
from sympy import Rational, sqrt, symbols, simplify
from sympy.geometry import Line, Point, Polygon, Triangle

from ejercicios import ejercicio, ejercicio_manual

REC = "módulo de Geometría (Guías de Apoyo)"
AREAS = f"{REC}, Tema 4: Polígonos, Perímetros y áreas —"
PITAGORAS = f"{REC}, Tema 3: Teorema de Pitágoras — Practica lo aprendido"
COMUN = dict(grados=[11], tema="medición de áreas y perímetros")
MEDICION = ["matematicas-11-4"]
AMBOS = ["matematicas-11-4", "matematicas-11-6"]

# Terreno de los Ejemplos 3 y 4 (cuadrícula de 6 m × 5 m, origen en la esquina inferior izquierda)
TERRENO = [Point(0, 0), Point(3, 0), Point(5, 1), Point(6, 3), Point(5, 5), Point(2, 5), Point(0, 2)]
TERRENO_TEX = (r"$(0, 0)$, $(3, 0)$, $(5, 1)$, $(6, 3)$, $(5, 5)$, $(2, 5)$ y $(0, 2)$ "
               r"(en metros)")


# ---------- Áreas por triangulación y precisión (Tema 4) ----------

@ejercicio(
    id="medicion-11-001", dba=AMBOS, tipo="contexto", dificultad=2,
    fuente=f"{AREAS} Ejemplo 1",
    enunciado=r"En papel cuadriculado (cuadros de 1 cm) se dibuja el cuadrilátero de vértices "
              r"$A(0, 0)$, $B(5, 0)$, $C(4, 3)$ y $D(0, 1)$. Para hallar su área se traza la "
              r"diagonal $BD$, que lo divide en el triángulo rectángulo $ABD$ y el triángulo "
              r"$BCD$; en este último se midieron con regla la base $BD \approx \num{5,1}$ cm y la "
              r"altura sobre ella, $\approx \num{2,75}$ cm. a) Calcula el área con esas medidas. "
              r"b) Calcula el área exacta con las coordenadas. c) ¿Cuál es el error de la "
              r"medición, en cm² y en porcentaje?",
    respuesta=r"a) $\frac{5 \cdot 1}{2} + \frac{\num{5,1} \cdot \num{2,75}}{2} = \num{2,5} + "
              r"\num{7,0125} = \num{9,5125}$ cm². b) $BD = \sqrt{26} \approx \num{5,099}$ cm y la "
              r"altura es $\frac{14}{\sqrt{26}} \approx \num{2,746}$ cm, así que el área exacta es "
              r"$\num{2,5} + 7 = \num{9,5}$ cm² (también por la fórmula del área con "
              r"coordenadas). c) El error es $\num{0,0125}$ cm², un $\num{0,13}~\%$ del área: la "
              r"medición con regla es muy precisa, pero no exacta.",
    notas="En el módulo el ejemplo se resuelve sobre la figura; aquí se dan los vértices "
          "(leídos de la figura del .docx) y se añaden b) y c) para comparar la medición con el "
          "valor exacto.", **COMUN)
def _():
    A, B, C, D = Point(0, 0), Point(5, 0), Point(4, 3), Point(0, 1)
    medida = Rational(5 * 1, 2) + Rational("5.1") * Rational("2.75") / 2
    assert medida == Rational("9.5125")
    exacta = abs(Polygon(A, B, C, D).area)
    assert exacta == Rational(19, 2)
    assert B.distance(D) == sqrt(26) and Line(B, D).distance(C) == 14 / sqrt(26)
    assert abs(float(B.distance(D)) - 5.1) < 0.01 and abs(float(14 / sqrt(26)) - 2.75) < 0.01
    error = medida - exacta
    assert error == Rational("0.0125") and round(float(100 * error / exacta), 2) == 0.13


@ejercicio(
    id="medicion-11-002", dba=AMBOS, tipo="calculo", dificultad=1,
    fuente=f"{AREAS} Ejemplo 2",
    enunciado=r"Calcula por triangulación el área del pentágono de vértices $(0, 0)$, $(4, 0)$, "
              r"$(5, 2)$, $(1, 4)$ y $(0, 2)$ (en centímetros), trazando las diagonales desde el "
              r"vértice $(0, 2)$.",
    respuesta=r"Las diagonales desde $(0, 2)$ forman tres triángulos: el de base $4$ y altura $2$ "
              r"($A_1 = 4$ cm²), el de base horizontal $5$ (de $(0, 2)$ a $(5, 2)$) y altura $2$ "
              r"hacia abajo ($A_2 = 5$ cm²) y el de la misma base y altura $2$ hacia arriba "
              r"($A_3 = 5$ cm²). Área: $A_1 + A_2 + A_3 = 14$ cm².",
    notas="En el módulo: «A = A2 + A2 + A3»; debe ser A1 + A2 + A3. Los vértices se leyeron de "
          "la figura del .docx.", **COMUN)
def _():
    P = [Point(0, 0), Point(4, 0), Point(5, 2), Point(1, 4), Point(0, 2)]
    v = P[4]
    partes = [abs(Triangle(v, P[i], P[i + 1]).area) for i in range(3)]
    assert partes == [4, 5, 5] and sum(partes) == abs(Polygon(*P).area) == 14


@ejercicio(
    id="medicion-11-003", dba=AMBOS, tipo="contexto", dificultad=2,
    fuente=f"{AREAS} Ejemplo 3",
    enunciado=r"El plano de un terreno se cuadriculó para medirlo (cuadros de 1 m); sus vértices "
              r"son " + TERRENO_TEX + r". Calcula su área uniendo cada vértice con el punto "
              r"$C(3, 3)$ del terreno y sumando las áreas de los siete triángulos que se forman. "
              r"En el triángulo de vértices $C$, $(2, 5)$ y $(0, 2)$, la base y la altura no "
              r"caen sobre la cuadrícula: el módulo las midió como $\num{3,61}$ m y $\num{1,94}$ m. "
              r"¿Qué área da con esas medidas y cuál es la exacta?",
    respuesta=r"Los triángulos miden $\num{4,5}$, $3$, $3$, $3$, $3$ y $3$ m² (seis triángulos "
              r"con un lado sobre la cuadrícula) más el de $C$, $(2, 5)$ y $(0, 2)$: con las "
              r"medidas, $\frac{\num{3,61} \cdot \num{1,94}}{2} \approx \num{3,50}$ m². Total: "
              r"$\approx 23$ m². Exacto: la base es $\sqrt{13} \approx \num{3,606}$ m y la altura "
              r"$\frac{7}{\sqrt{13}} \approx \num{1,941}$ m, así que ese triángulo mide "
              r"$\num{3,5}$ m² y el terreno $23$ m² exactos.",
    notas="En el módulo las áreas del terreno aparecen en cm² aunque el plano está en metros; "
          "aquí van en m². Los vértices y el punto C se leyeron de la figura del .docx.", **COMUN)
def _():
    C = Point(3, 3)
    n = len(TERRENO)
    tri = [abs(Triangle(C, TERRENO[i], TERRENO[(i + 1) % n]).area) for i in range(n)]
    assert sorted(tri) == sorted([Rational(9, 2), 3, 3, 3, 3, 3, Rational(7, 2)])
    assert sum(tri) == abs(Polygon(*TERRENO).area) == 23
    base, altura = Point(2, 5).distance(Point(0, 2)), Line(Point(2, 5), Point(0, 2)).distance(C)
    assert base == sqrt(13) and simplify(altura - 7 / sqrt(13)) == 0
    assert round(float(Rational("3.61") * Rational("1.94") / 2), 2) == 3.50


@ejercicio(
    id="medicion-11-004", dba=AMBOS, tipo="contexto", dificultad=2,
    fuente=f"{AREAS} Ejemplo 4",
    enunciado=r"Calcula el área del terreno de vértices " + TERRENO_TEX + r" por "
              r"«triangulación externa»: al área del rectángulo de $6 \times 5$ m que lo contiene "
              r"réstale las áreas de las regiones que quedan por fuera del terreno.",
    respuesta=r"Por fuera quedan cuatro triángulos rectángulos (tres de catetos $2$ y $1$, de "
              r"$1$ m² cada uno, y uno de catetos $3$ y $2$, de $3$ m²) y un cuadrado de $1$ m² "
              r"en la esquina $(5, 0)$–$(6, 1)$. Área: $30 - [3(1) + 3 + 1] = 23$ m², igual que "
              r"por triangulación interna.",
    notas="En el módulo: «30 − [(3)(1) – 3 − 1] = 23»; los signos dentro del corchete deben ser "
          "+ (30 − [3 + 3 + 1] = 23).", **COMUN)
def _():
    fuera = [Triangle(Point(3, 0), Point(5, 0), Point(5, 1)),
             Triangle(Point(5, 1), Point(6, 1), Point(6, 3)),
             Triangle(Point(6, 3), Point(6, 5), Point(5, 5)),
             Triangle(Point(2, 5), Point(0, 5), Point(0, 2))]
    cuadrado = Polygon(Point(5, 0), Point(6, 0), Point(6, 1), Point(5, 1))
    areas = sorted(abs(t.area) for t in fuera)
    assert areas == [1, 1, 1, 3] and abs(cuadrado.area) == 1
    assert 30 - (sum(areas) + 1) == abs(Polygon(*TERRENO).area) == 23


@ejercicio(
    id="medicion-11-005", dba=AMBOS, tipo="calculo", dificultad=2,
    fuente=f"{AREAS} Ejemplo 4 (perímetro)",
    enunciado=r"Calcula el perímetro del terreno de vértices " + TERRENO_TEX + r", en forma "
              r"exacta y aproximado a centésimas.",
    respuesta=r"Los lados miden $3$, $\sqrt{5}$, $\sqrt{5}$, $\sqrt{5}$, $3$, $\sqrt{13}$ y $2$ m "
              r"(los inclinados, por Pitágoras). Perímetro: $8 + 3\sqrt{5} + \sqrt{13} \approx "
              r"\num{18,31}$ m.",
    notas="En el módulo: «8 + √13 + 3√13 ≈ 18,314»; la expresión correcta es 8 + 3√5 + √13 "
          "(el valor aproximado sí es el correcto).", **COMUN)
def _():
    n = len(TERRENO)
    lados = [TERRENO[i].distance(TERRENO[(i + 1) % n]) for i in range(n)]
    perimetro = sum(lados)
    assert simplify(perimetro - (8 + 3 * sqrt(5) + sqrt(13))) == 0
    assert round(float(perimetro), 2) == 18.31
    assert round(float(8 + 4 * sqrt(13)), 2) != 18.31                     # la del módulo no


ejercicio_manual(
    id="medicion-11-006", dba=MEDICION, tipo="argumentacion", dificultad=2,
    fuente=f"{AREAS} Ejemplo 4 (comentario)",
    enunciado=r"Con el terreno de vértices " + TERRENO_TEX + r", la triangulación interna desde "
              r"$C(3, 3)$ obligó a medir una base y una altura que no caen sobre la cuadrícula, y "
              r"la triangulación externa no. Explica por qué la triangulación externa es más "
              r"exacta y qué harías para mejorar la precisión si tuvieras que medir en el terreno "
              r"real.",
    respuesta=r"En la triangulación externa todos los triángulos que se restan tienen catetos "
              r"sobre la cuadrícula ($1$, $2$, $3$ m), que se cuentan sin error; en la interna, "
              r"un triángulo tiene base $\sqrt{13}$ y altura $\frac{7}{\sqrt{13}}$, que solo se "
              r"pueden medir de forma aproximada ($\num{3,61}$ y $\num{1,94}$), y ese error pasa "
              r"al área. Para mejorar la precisión: escoger descomposiciones cuyas medidas caigan "
              r"en la cuadrícula, usar un instrumento con divisiones más finas (cinta métrica en "
              r"cm), medir varias veces y promediar, y comprobar el resultado por dos métodos "
              r"(medición indirecta), como aquí, donde ambos dan $23$ m².",
    notas="Pregunta nuestra, basada en el comentario del módulo «Generalmente la triangulación "
          "externa es más exacta…».", **COMUN)


# ---------- Medición indirecta con el teorema de Pitágoras (Tema 3) ----------

PITA = dict(grados=[11], tema="medición indirecta: teorema de Pitágoras", dba=MEDICION,
            tipo="calculo")


@ejercicio(
    id="medicion-11-007", dificultad=2, fuente=f"{PITAGORAS} 3",
    enunciado=r"¿Qué distancias irracionales puedes obtener al dibujar triángulos rectángulos con "
              r"lados de longitudes 9 cm y 7 cm?",
    respuesta=r"Si $9$ y $7$ son los catetos, la hipotenusa mide $\sqrt{9^2 + 7^2} = \sqrt{130} "
              r"\approx \num{11,40}$ cm. Si $9$ es la hipotenusa y $7$ un cateto, el otro cateto "
              r"mide $\sqrt{9^2 - 7^2} = \sqrt{32} = 4\sqrt{2} \approx \num{5,66}$ cm. Las dos "
              r"son irracionales.",
    notas="El enunciado del módulo no dice si 9 y 7 son catetos; se dan los dos casos.", **PITA)
def _():
    hip, cat = sqrt(9**2 + 7**2), sqrt(9**2 - 7**2)
    assert hip == sqrt(130) and cat == 4 * sqrt(2)
    assert not hip.is_rational and not cat.is_rational


@ejercicio(
    id="medicion-11-008", dificultad=1, fuente=f"{PITAGORAS} 4",
    enunciado=r"¿Cuánto mide la diagonal de un cuadrado de lado 7 cm?",
    respuesta=r"$\sqrt{7^2 + 7^2} = 7\sqrt{2} \approx \num{9,90}$ cm.", **PITA)
def _():
    assert Point(0, 0).distance(Point(7, 7)) == 7 * sqrt(2)


@ejercicio(
    id="medicion-11-009", dificultad=1, fuente=f"{PITAGORAS} 5",
    enunciado=r"¿Cuánto mide la diagonal de un cuadrado de lado 10 cm?",
    respuesta=r"$\sqrt{10^2 + 10^2} = 10\sqrt{2} \approx \num{14,14}$ cm.", **PITA)
def _():
    assert Point(0, 0).distance(Point(10, 10)) == 10 * sqrt(2)


@ejercicio(
    id="medicion-11-010", dificultad=1, fuente=f"{PITAGORAS} 6",
    enunciado=r"¿Cuánto mide la diagonal de un cuadrado de lado $x$ cm?",
    respuesta=r"$\sqrt{x^2 + x^2} = x\sqrt{2}$ cm.", **PITA)
def _():
    x = symbols("x", positive=True)
    assert simplify(Point(0, 0).distance(Point(x, x)) - x * sqrt(2)) == 0


@ejercicio(
    id="medicion-11-011", dificultad=1, fuente=f"{PITAGORAS} 7",
    enunciado=r"¿Cuánto mide la diagonal de un rectángulo de base 7 cm y altura 6 cm?",
    respuesta=r"$\sqrt{7^2 + 6^2} = \sqrt{85} \approx \num{9,22}$ cm.", **PITA)
def _():
    assert Point(0, 0).distance(Point(7, 6)) == sqrt(85)


@ejercicio(
    id="medicion-11-012", dificultad=2, fuente=f"{PITAGORAS} 8",
    enunciado=r"¿Cuánto mide la diagonal de un rectángulo de base 10 cm y con un área de 50 cm "
              r"cuadrados?",
    respuesta=r"La altura es $\frac{50}{10} = 5$ cm y la diagonal "
              r"$\sqrt{10^2 + 5^2} = \sqrt{125} = 5\sqrt{5} \approx \num{11,18}$ cm.", **PITA)
def _():
    altura = Rational(50, 10)
    assert altura == 5 and Point(0, 0).distance(Point(10, altura)) == 5 * sqrt(5)
