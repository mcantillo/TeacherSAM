"""Banco de ejercicios — Matemáticas — Números irracionales (8°).
Etapa B de la guía de Álgebra 8°, trimestre I («La cacería de π»):
materias/algebra/octavo/guia-didactica/guia-periodo-I-numeros-irracionales.plan.md
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/irracionales-8.py

Ya cubiertos en el banco y reutilizados en la guía (no se duplican aquí):
- ubicar irracionales en la recta real: numeros-reales-8-001 … 006;
- √(a + b) frente a √a + √b (ejemplo del DBA 2): numeros-reales-8-025, 026;
- radicales semejantes: radicacion-8-034;
- medidas con radicales: medidas-con-radicales-8-001, 003, 004.
"""
from fractions import Fraction

from sympy import Integer, Rational, N, floor, nsimplify, pi, sqrt

from ejercicios import ejercicio, ejercicio_manual

FUENTE = "guía Álgebra 8° P-I («La cacería de π»), plan etapa A"
DBA1, DBA2 = "matematicas-8-1", "matematicas-8-2"


def decimales(p, q, n):
    """Primeras n cifras decimales de p/q por división larga (p, q > 0)."""
    entero, resto = divmod(p, q)
    cifras = []
    for _ in range(n):
        resto *= 10
        c, resto = divmod(resto, q)
        cifras.append(str(c))
    return entero, "".join(cifras)


def periodo(p, q):
    """(anteperíodo, período) del decimal de p/q; período '' si es exacto."""
    _, resto = divmod(p, q)
    vistos, cifras = {}, []
    while resto and resto not in vistos:
        vistos[resto] = len(cifras)
        resto *= 10
        c, resto = divmod(resto, q)
        cifras.append(str(c))
    if not resto:
        return "".join(cifras), ""
    i = vistos[resto]
    return "".join(cifras[:i]), "".join(cifras[i:])


def de_periodico(entera, ante, per):
    """Valor exacto de entera,ante(per)(per)… sumando la serie geométrica, no con la regla escolar."""
    base = Rational(int(entera)) + (Rational(int(ante), 10 ** len(ante)) if ante else 0)
    a = Rational(int(per), 10 ** (len(ante) + len(per)))
    return base + a / (1 - Rational(1, 10 ** len(per)))


def cifras_correctas(aprox, exacto, maximo=20):
    """Cuántas cifras decimales comparten aprox y exacto al truncar (comparación con 40 dígitos)."""
    a, e = N(aprox, 40), N(exacto, 40)
    k = 0
    while k < maximo and floor(a * 10 ** (k + 1)) == floor(e * 10 ** (k + 1)):
        k += 1
    return k


def irreducible(r):
    return Fraction(int(r.p), int(r.q))


# --------------------------------------------------------------------------------------
# Tema 1 — De los racionales a los irracionales
# --------------------------------------------------------------------------------------

@ejercicio(
    id="irracionales-8-001", tema="decimales y fracciones", grados=[8], dba=[DBA1, DBA2],
    tipo="calculo", dificultad=1, fuente=FUENTE + ", tema 1 (ejemplo resuelto)",
    notas="ejemplo resuelto de la explicación: exacto y periódico",
    enunciado=r"Escribe $\dfrac{3}{8}$ y $\dfrac{1}{9}$ como decimales y di si cada uno es exacto o periódico.",
    respuesta=r"$\dfrac{3}{8} = \num{0,375}$ (exacto: el resto llega a $0$); "
              r"$\dfrac{1}{9} = 0{,}\overline{1}$ (periódico: el resto $1$ se repite siempre).")
def _():
    assert periodo(3, 8) == ("375", "")
    assert periodo(1, 9) == ("", "1")


@ejercicio(
    id="irracionales-8-002", tema="decimales y fracciones", grados=[8], dba=[DBA1, DBA2],
    tipo="calculo", dificultad=1, fuente=FUENTE + ", tema 1 (ejemplo resuelto)",
    notas="ejemplo resuelto: periódico puro a fracción",
    enunciado=r"Escribe $0{,}\overline{45}$ como fracción irreducible.",
    respuesta=r"Si $x = 0{,}\overline{45}$, entonces $100x = 45{,}\overline{45}$; restando, "
              r"$99x = 45$ y $x = \dfrac{45}{99} = \dfrac{5}{11}$.")
def _():
    x = de_periodico("0", "", "45")
    assert x == Rational(5, 11) and 100 * x - x == 45
    assert periodo(5, 11) == ("", "45")


@ejercicio(
    id="irracionales-8-003", tema="decimales y fracciones", grados=[8], dba=[DBA1, DBA2],
    tipo="calculo", dificultad=2, fuente=FUENTE + ", tema 1 (ejemplo resuelto)",
    notas="ejemplo resuelto: periódico mixto a fracción",
    enunciado=r"Escribe $0{,}1\overline{6}$ como fracción irreducible.",
    respuesta=r"Si $x = 0{,}1\overline{6}$: $100x = 16{,}\overline{6}$ y $10x = 1{,}\overline{6}$; "
              r"restando, $90x = 15$, así que $x = \dfrac{15}{90} = \dfrac{1}{6}$.")
def _():
    x = de_periodico("0", "1", "6")
    assert x == Rational(1, 6) and 100 * x - 10 * x == 15
    assert periodo(1, 6) == ("1", "6")


ejercicio_manual(
    id="irracionales-8-004", tema="decimales y fracciones", grados=[8], dba=[DBA1],
    tipo="argumentacion", dificultad=2,
    fuente="MEN, DBA V.2 Matemáticas, grado 8, DBA 1 (ejemplo), adaptado",
    notas="El ejemplo del DBA dice que el número de Marcela no tiene «patrón»; un dado puede "
          "repetir cifras, así que el enunciado precisa «sin que ningún bloque se repita "
          "periódicamente».",
    enunciado=r"En clase, cuatro estudiantes construyeron números decimales. \textbf{Marina} empezó "
              r"con el $5$ y formó 10 cifras decimales lanzando un dado 10 veces. \textbf{Julián} "
              r"escribió $0{,}1234567891011121314\ldots$, poniendo los naturales uno tras otro, "
              r"para siempre. \textbf{Catalina} dividió $1 \div 3$. \textbf{Marcela} siguió el "
              r"método de Marina, pero imaginando que puede lanzar el dado para siempre, sin que "
              r"ningún bloque de cifras se repita periódicamente. ¿Cuáles números son racionales y "
              r"cuáles no? Argumenta cada caso.",
    respuesta=r"Marina: racional (decimal exacto de 10 cifras, se escribe como fracción con "
              r"denominador $10^{10}$). Catalina: racional, $\frac{1}{3} = 0{,}\overline{3}$. "
              r"Julián: irracional: cada vez aparecen más cifras (números de 2, 3, … dígitos) y "
              r"ningún bloque se repite periódicamente, porque luego vienen, por ejemplo, tantos "
              r"ceros seguidos como se quiera (en 10, 100, 1000…). Marcela: irracional por "
              r"construcción, su decimal es infinito y no periódico.")


@ejercicio(
    id="irracionales-8-005", tema="decimales y fracciones", grados=[8], dba=[DBA1, DBA2],
    tipo="calculo", dificultad=2, fuente=FUENTE + ", tema 1",
    enunciado=r"Escribe como fracción irreducible: a) $0{,}\overline{6}$; b) $0{,}\overline{27}$; "
              r"c) $1{,}2\overline{3}$.",
    respuesta=r"a) $\dfrac{6}{9} = \dfrac{2}{3}$. b) $\dfrac{27}{99} = \dfrac{3}{11}$. "
              r"c) $100x - 10x = 123{,}\overline{3} - 12{,}\overline{3} = 111$, "
              r"$x = \dfrac{111}{90} = \dfrac{37}{30}$.")
def _():
    assert de_periodico("0", "", "6") == Rational(2, 3)
    assert de_periodico("0", "", "27") == Rational(3, 11)
    assert de_periodico("1", "2", "3") == Rational(37, 30)
    assert irreducible(Rational(111, 90)) == Fraction(37, 30)


@ejercicio(
    id="irracionales-8-006", tema="decimales y fracciones", grados=[8], dba=[DBA1],
    tipo="encuentra-el-error", dificultad=2, fuente=FUENTE + ", tema 1",
    enunciado=r"Un compañero afirma: «$0{,}999\ldots$ (con nueves para siempre) no es igual a $1$, "
              r"solo se le acerca mucho». Usa el método de restar $10x - x$ para decidir si tiene "
              r"razón.",
    respuesta=r"No tiene razón: si $x = 0{,}\overline{9}$, entonces $10x - x = 9{,}\overline{9} - "
              r"0{,}\overline{9} = 9$, así que $9x = 9$ y $x = 1$. Son dos escrituras del mismo número.")
def _():
    x = de_periodico("0", "", "9")
    assert x == 1 and 10 * x - x == 9


@ejercicio(
    id="irracionales-8-007", tema="decimales y fracciones", grados=[8], dba=[DBA1],
    tipo="argumentacion", dificultad=2, fuente=FUENTE + ", tema 1 (puente al tema 2)",
    enunciado=r"Muchas personas usan $\dfrac{22}{7}$ en lugar de $\pi$. Escribe $\dfrac{22}{7}$ como "
              r"decimal por división larga. ¿Es exacto o periódico? Sabiendo que "
              r"$\pi = \num{3,14159265}\ldots$, ¿puede ser $\dfrac{22}{7}$ igual a $\pi$?",
    respuesta=r"$\dfrac{22}{7} = 3{,}\overline{142857}$, periódico (como toda fracción). Ya en la "
              r"tercera cifra decimal difiere de $\pi$: $\num{3,142}\ldots$ frente a "
              r"$\num{3,141}\ldots$. No son iguales; $\frac{22}{7}$ solo es una aproximación.")
def _():
    assert periodo(22, 7) == ("", "142857")
    assert decimales(22, 7, 3) == (3, "142")
    assert int(floor(pi * 1000)) == 3141
    assert Rational(22, 7) != pi


# --------------------------------------------------------------------------------------
# Tema 2 — El primer número que no es fracción (√2)
# --------------------------------------------------------------------------------------

ejercicio_manual(
    id="irracionales-8-008", tema="irracionalidad de √2", grados=[8], dba=[DBA1],
    tipo="argumentacion", dificultad=2, fuente=FUENTE + ", tema 2 (demostración de la explicación)",
    notas="demostración resuelta de la explicación (la de paridad que menciona Aristóteles)",
    enunciado=r"Demuestra que $\sqrt{2}$ no es un número racional.",
    respuesta=r"Supongamos que $\sqrt{2} = \frac{p}{q}$ con la fracción reducida. Entonces "
              r"$p^2 = 2q^2$: $p^2$ es par, luego $p$ es par, $p = 2k$. Así $4k^2 = 2q^2$, es decir "
              r"$q^2 = 2k^2$, y $q$ también es par. Entonces $p$ y $q$ tienen el factor común $2$, "
              r"contra lo supuesto. La suposición es falsa: $\sqrt{2}$ no es racional.")

ejercicio_manual(
    id="irracionales-8-009", tema="irracionalidad de √2", grados=[8], dba=[DBA1],
    tipo="argumentacion", dificultad=2, fuente=FUENTE + ", tema 2",
    enunciado=r"Adapta la demostración de que $\sqrt{2}$ no es racional para probar que "
              r"$\sqrt{3}$ tampoco lo es. (Pista: si $p^2 = 3q^2$, ¿qué puedes decir de $p$?)",
    respuesta=r"Si $\sqrt{3} = \frac{p}{q}$ reducida, $p^2 = 3q^2$: $3$ divide a $p^2$ y, como $3$ "
              r"es primo, divide a $p$: $p = 3k$. Entonces $9k^2 = 3q^2$, $q^2 = 3k^2$, y $3$ "
              r"divide a $q$. La fracción no estaba reducida: contradicción. (Con «par» ya no basta: "
              r"hay que usar que $3$ es primo.)")


@ejercicio(
    id="irracionales-8-010", tema="construcción de irracionales", grados=[8], dba=[DBA1, DBA2],
    tipo="calculo", dificultad=1, fuente=FUENTE + ", tema 2 (construcción de la explicación)",
    notas="construcción resuelta de la explicación; usa el teorema de Pitágoras como herramienta",
    enunciado=r"Explica cómo llevar $\sqrt{2}$ y $\sqrt{5}$ a la recta numérica con regla y compás, "
              r"usando un cuadrado de lado $1$ y un triángulo rectángulo de catetos $1$ y $2$.",
    respuesta=r"La diagonal del cuadrado de lado $1$ mide $\sqrt{1^2 + 1^2} = \sqrt{2}$; con el "
              r"compás en $0$ y abertura igual a la diagonal, se marca $\sqrt{2} \approx \num{1,41}$. "
              r"Con catetos $1$ y $2$, la hipotenusa mide $\sqrt{1^2 + 2^2} = \sqrt{5}$, que se lleva "
              r"igual hasta $\sqrt{5} \approx \num{2,24}$. El compás conserva la longitud: por eso "
              r"el punto marcado es exactamente $\sqrt{2}$ (o $\sqrt{5}$).")
def _():
    assert sqrt(1**2 + 1**2) == sqrt(2) and sqrt(1**2 + 2**2) == sqrt(5)
    assert round(float(sqrt(2)), 2) == 1.41 and round(float(sqrt(5)), 2) == 2.24


@ejercicio(
    id="irracionales-8-011", tema="construcción de irracionales", grados=[8], dba=[DBA2],
    tipo="calculo", dificultad=1, fuente=FUENTE + ", tema 2 (espiral de Teodoro)",
    enunciado=r"En la espiral de Teodoro, cada triángulo rectángulo tiene un cateto de $1$ y el otro "
              r"igual a la hipotenusa del triángulo anterior; el primero tiene catetos $1$ y $1$. "
              r"Calcula la hipotenusa de los cinco primeros triángulos y di cuáles son números "
              r"racionales.",
    respuesta=r"$\sqrt{2}$, $\sqrt{3}$, $\sqrt{4} = 2$, $\sqrt{5}$ y $\sqrt{6} \approx \num{2,45}$: "
              r"cada una es $\sqrt{n + 1}$ si el cateto anterior es $\sqrt{n}$. Solo $\sqrt{4} = 2$ es "
              r"racional; las demás son raíces no exactas, irracionales.")
def _():
    h, hip = Integer(1), []
    for _ in range(5):
        h = sqrt(1 + h**2)
        hip.append(h)
    assert hip == [sqrt(2), sqrt(3), 2, sqrt(5), sqrt(6)]
    assert [x.is_rational for x in hip] == [False, False, True, False, False]
    assert round(float(sqrt(6)), 2) == 2.45


@ejercicio(
    id="irracionales-8-012", tema="construcción de irracionales", grados=[8], dba=[DBA2],
    tipo="contexto", dificultad=1, fuente=FUENTE + ", tema 2 (aplicación: norma ISO 216)",
    notas="Medidas: A4 = 210 × 297 mm (ISO 216); carta = 21,6 × 27,9 cm. Dato de la aplicación "
          "verificado en https://www.cl.cam.ac.uk/~mgk25/iso-paper.html",
    enunciado=r"Una hoja A4 mide $210 \times 297$ mm y una hoja carta, $216 \times 279$ mm. Calcula "
              r"la razón largo/ancho de cada una y compárala con $\sqrt{2}$. Luego dobla cada hoja por "
              r"la mitad (la mitad del largo) y calcula de nuevo la razón. ¿Cuál conserva su forma?",
    respuesta=r"A4: $297/210 \approx \num{1,414}$, casi $\sqrt{2} \approx \num{1,414}$; doblada "
              r"($210 \times \num{148,5}$), $210/\num{148,5} \approx \num{1,414}$: conserva la forma. "
              r"Carta: $279/216 \approx \num{1,292}$; doblada ($216 \times \num{139,5}$), "
              r"$216/\num{139,5} \approx \num{1,548}$: cambia de forma.")
def _():
    a4, a4m = Rational(297, 210), Rational(210) / Rational(297, 2)
    ca, cam = Rational(279, 216), Rational(216) / Rational(279, 2)
    assert round(float(a4), 3) == round(float(a4m), 3) == round(float(sqrt(2)), 3) == 1.414
    assert round(float(ca), 3) == 1.292 and round(float(cam), 3) == 1.548


@ejercicio(
    id="irracionales-8-013", tema="aproximaciones de √2", grados=[8], dba=[DBA1, DBA2],
    tipo="calculo", dificultad=2, fuente=FUENTE + ", tema 2 (hilo)",
    enunciado=r"Las fracciones $\dfrac{7}{5}$, $\dfrac{17}{12}$ y $\dfrac{99}{70}$ se acercan cada "
              r"vez más a $\sqrt{2}$. Eleva cada una al cuadrado y compara con $2$; luego calcula, con "
              r"la calculadora, cuánto se aleja cada una de $\sqrt{2}$.",
    respuesta=r"$\left(\frac{7}{5}\right)^2 = \frac{49}{25} = \num{1,96}$; "
              r"$\left(\frac{17}{12}\right)^2 = \frac{289}{144} \approx \num{2,0069}$; "
              r"$\left(\frac{99}{70}\right)^2 = \frac{9801}{4900} \approx \num{2,0002}$. Ninguna da "
              r"exactamente $2$. Distancias a $\sqrt{2}$: $\approx \num{0,0142}$, "
              r"$\approx \num{0,0025}$ y $\approx \num{0,00007}$.")
def _():
    fr = [Rational(7, 5), Rational(17, 12), Rational(99, 70)]
    assert [f**2 for f in fr] == [Rational(49, 25), Rational(289, 144), Rational(9801, 4900)]
    assert all(f**2 != 2 for f in fr)
    d = [abs(float(f - sqrt(2))) for f in fr]
    assert round(d[0], 4) == 0.0142 and round(d[1], 4) == 0.0025 and round(d[2], 5) == 0.00007
    assert d[0] > d[1] > d[2]


# --------------------------------------------------------------------------------------
# Tema 3 — Los irracionales en la vida real (π)
# --------------------------------------------------------------------------------------

@ejercicio(
    id="irracionales-8-014", tema="π y sus aproximaciones", grados=[8], dba=[DBA1],
    tipo="calculo", dificultad=2, fuente=FUENTE + ", tema 3 (marco teórico: MacTutor, A history of Pi)",
    notas="3,16 del papiro Rhind = 4·(8/9)² = 256/81 (MacTutor); 22/7 de Arquímedes; 355/113 de "
          "Zu Chongzhi.",
    enunciado=r"Tres aproximaciones históricas de $\pi$ son $\dfrac{256}{81}$ (papiro Rhind, Egipto), "
              r"$\dfrac{22}{7}$ (Arquímedes) y $\dfrac{355}{113}$ (Zu Chongzhi, China). Escribe cada "
              r"una como decimal con siete cifras y di cuántas cifras decimales coinciden con "
              r"$\pi = \num{3,1415926}\ldots$",
    respuesta=r"$\frac{256}{81} \approx \num{3,1604938}$: $1$ cifra decimal ($3{,}1$). "
              r"$\frac{22}{7} \approx \num{3,1428571}$: $2$ cifras ($3{,}14$). "
              r"$\frac{355}{113} \approx \num{3,1415929}$: $6$ cifras ($\num{3,141592}$).")
def _():
    assert Rational(256, 81) == 4 * Rational(8, 9) ** 2
    assert decimales(256, 81, 7) == (3, "1604938")
    assert decimales(22, 7, 7) == (3, "1428571")
    assert decimales(355, 113, 7) == (3, "1415929")
    assert [cifras_correctas(Rational(a, b), pi) for a, b in [(256, 81), (22, 7), (355, 113)]] == [1, 2, 6]


@ejercicio(
    id="irracionales-8-015", tema="clasificación de números reales", grados=[8], dba=[DBA1],
    tipo="conceptual", dificultad=1, fuente=FUENTE + ", tema 3",
    enunciado=r"Clasifica cada número como natural, entero, racional o irracional (puede pertenecer "
              r"a varios conjuntos): $\sqrt{9}$, $\sqrt{7}$, $-\dfrac{4}{2}$, $\dfrac{22}{7}$, $\pi$, "
              r"$2{,}101001000100001\ldots$ (cada vez un cero más entre los unos).",
    respuesta=r"$\sqrt{9} = 3$: natural, entero y racional. $\sqrt{7}$: irracional. "
              r"$-\frac{4}{2} = -2$: entero y racional. $\frac{22}{7}$: racional. $\pi$: irracional. "
              r"$2{,}1010010001\ldots$: irracional, porque el bloque de ceros crece y nunca se repite "
              r"un mismo período.")
def _():
    assert sqrt(9) == 3 and Integer(3).is_integer and Integer(3) > 0
    assert sqrt(7).is_rational is False
    assert Rational(-4, 2) == -2
    assert Rational(22, 7).is_rational and not Rational(22, 7).is_integer
    assert pi.is_rational is False
    # El último se justifica con el argumento del enunciado (no se comprueba con código).


@ejercicio(
    id="irracionales-8-016", tema="operaciones con irracionales", grados=[8], dba=[DBA2],
    tipo="argumentacion", dificultad=2, fuente=FUENTE + ", tema 3",
    enunciado=r"¿Es siempre irracional el resultado de sumar dos números irracionales? Calcula "
              r"$\sqrt{2} + \sqrt{2}$ y $\sqrt{2} + (3 - \sqrt{2})$ y explica qué observas.",
    respuesta=r"No siempre. $\sqrt{2} + \sqrt{2} = 2\sqrt{2}$ es irracional, pero "
              r"$\sqrt{2} + (3 - \sqrt{2}) = 3$ es racional, aunque $3 - \sqrt{2}$ es irracional.")
def _():
    assert (sqrt(2) + sqrt(2) - 2 * sqrt(2)).simplify() == 0 and (2 * sqrt(2)).is_rational is False
    assert (3 - sqrt(2)).is_rational is False
    assert (sqrt(2) + (3 - sqrt(2))).simplify() == 3


@ejercicio(
    id="irracionales-8-017", tema="π en contexto", grados=[8], dba=[DBA1],
    tipo="contexto", dificultad=1, fuente=FUENTE + ", tema 3 (aplicación resuelta)",
    notas="aplicación resuelta de la explicación",
    enunciado=r"Una rueda de bicicleta mide $66$ cm de diámetro. ¿Cuánto avanza en una vuelta y "
              r"cuántas vueltas da en $1$ km? Si el cuentakilómetros usara $\frac{22}{7}$ en vez de "
              r"$\pi$, ¿cuántos metros de más contaría en $1$ km?",
    respuesta=r"Una vuelta: $66\pi \approx \num{207,3}$ cm. En $1$ km $= \num{100000}$ cm: "
              r"$\num{100000} \div 66\pi \approx \num{482,3}$ vueltas. Con $\frac{22}{7}$ cada vuelta "
              r"mediría $\num{207,43}$ cm, y en esas $\num{482,3}$ vueltas contaría unos "
              r"$\num{0,4}$ m de más (un error del $\num{0,04}\,\%$).")
def _():
    c = 66 * pi
    v = Rational(100000) / c
    assert round(float(c), 1) == 207.3 and round(float(v), 1) == 482.3
    c2 = 66 * Rational(22, 7)
    assert round(float(c2), 2) == 207.43
    extra_m = float(v * c2 - 100000) / 100
    assert round(extra_m, 1) == 0.4
    assert round(float((Rational(22, 7) - pi) / pi * 100), 2) == 0.04


@ejercicio(
    id="irracionales-8-018", tema="π en contexto", grados=[8], dba=[DBA1],
    tipo="contexto", dificultad=2, fuente=FUENTE + ", tema 3",
    enunciado=r"Una llanta de carro tiene $58$ cm de diámetro. ¿Cuántas vueltas da al recorrer "
              r"$1$ km? Redondea a la vuelta más cercana y explica por qué aquí tiene sentido "
              r"redondear.",
    respuesta=r"$\num{100000} \div 58\pi \approx \num{548,8}$, unas $549$ vueltas. Se redondea porque "
              r"el diámetro ya es una medida aproximada (y la llanta se deforma con el peso): más "
              r"cifras no serían reales.")
def _():
    v = Rational(100000) / (58 * pi)
    assert round(float(v), 1) == 548.8 and round(float(v)) == 549


ejercicio_manual(
    id="irracionales-8-019", tema="operaciones con irracionales", grados=[8], dba=[DBA2],
    tipo="argumentacion", dificultad=2, fuente=FUENTE + ", tema 3 (propiedad de la explicación)",
    notas="demostración resuelta de la explicación",
    enunciado=r"Explica por qué la suma de un número racional y uno irracional siempre es irracional.",
    respuesta=r"Si $r$ es racional, $a$ irracional y $r + a = s$ fuera racional, entonces "
              r"$a = s - r$ sería la resta de dos racionales, que es racional: contradicción. Luego "
              r"$r + a$ es irracional.")


# --------------------------------------------------------------------------------------
# Tema 4 — Radicales y aplicaciones
# --------------------------------------------------------------------------------------

@ejercicio(
    id="irracionales-8-020", tema="simplificación de radicales", grados=[8], dba=[DBA2],
    tipo="calculo", dificultad=1, fuente=FUENTE + ", tema 4 (ejemplo resuelto y ejercicio)",
    enunciado=r"Simplifica: a) $\sqrt{50}$; b) $\sqrt{18}$; c) $\sqrt{75}$; d) $\sqrt{200}$.",
    respuesta=r"a) $\sqrt{25 \cdot 2} = 5\sqrt{2}$. b) $\sqrt{9 \cdot 2} = 3\sqrt{2}$. "
              r"c) $\sqrt{25 \cdot 3} = 5\sqrt{3}$. d) $\sqrt{100 \cdot 2} = 10\sqrt{2}$.")
def _():
    assert [sqrt(n) for n in (50, 18, 75, 200)] == [5 * sqrt(2), 3 * sqrt(2), 5 * sqrt(3), 10 * sqrt(2)]


@ejercicio(
    id="irracionales-8-021", tema="simplificación de radicales", grados=[8], dba=[DBA2],
    tipo="encuentra-el-error", dificultad=2, fuente=FUENTE + ", tema 4",
    enunciado=r"Camila dice: «$\sqrt{18} + \sqrt{2} = \sqrt{20}$, porque sumé lo de adentro de la "
              r"raíz». ¿Estás de acuerdo? Simplifica cada radical por separado y muestra el "
              r"procedimiento correcto.",
    respuesta=r"No: la raíz no se reparte en la suma. $\sqrt{18} + \sqrt{2} = 3\sqrt{2} + \sqrt{2} = "
              r"4\sqrt{2} \approx \num{5,66}$, mientras que $\sqrt{20} = 2\sqrt{5} \approx \num{4,47}$.")
def _():
    s = sqrt(18) + sqrt(2)
    assert (s - 4 * sqrt(2)).simplify() == 0
    assert sqrt(20) == 2 * sqrt(5) and (s - sqrt(20)).simplify() != 0
    assert round(float(s), 2) == 5.66 and round(float(sqrt(20)), 2) == 4.47


@ejercicio(
    id="irracionales-8-022", tema="aproximaciones de raíces", grados=[8], dba=[DBA1, DBA2],
    tipo="calculo", dificultad=2,
    fuente=FUENTE + ", tema 4 (Arquímedes, La medida del círculo; arXiv:1101.0492)",
    enunciado=r"Para encerrar a $\pi$, Arquímedes usó que $\dfrac{265}{153} < \sqrt{3} < "
              r"\dfrac{1351}{780}$. Compruébalo sin calculadora elevando al cuadrado (compara "
              r"$265^2$ con $3 \cdot 153^2$, y $1351^2$ con $3 \cdot 780^2$). Luego, con la "
              r"calculadora, di cuántas cifras decimales de $\sqrt{3} = \num{1,7320508}\ldots$ "
              r"acierta cada fracción.",
    respuesta=r"$265^2 = \num{70225} < 3 \cdot 153^2 = \num{70227}$ y "
              r"$1351^2 = \num{1825201} > 3 \cdot 780^2 = \num{1825200}$, así que la desigualdad es "
              r"cierta. $\frac{265}{153} \approx \num{1,7320261}$ acierta $4$ cifras "
              r"($\num{1,7320}$); $\frac{1351}{780} \approx \num{1,7320513}$ acierta $5$ "
              r"($\num{1,73205}$).")
def _():
    assert 265**2 == 70225 and 3 * 153**2 == 70227 and 265**2 < 3 * 153**2
    assert 1351**2 == 1825201 and 3 * 780**2 == 1825200 and 1351**2 > 3 * 780**2
    assert Rational(265, 153) < sqrt(3) < Rational(1351, 780)
    assert decimales(265, 153, 7) == (1, "7320261") and decimales(1351, 780, 7) == (1, "7320512")
    assert cifras_correctas(Rational(265, 153), sqrt(3)) == 4
    assert cifras_correctas(Rational(1351, 780), sqrt(3)) == 5


@ejercicio(
    id="irracionales-8-023", tema="aproximaciones de raíces", grados=[8], dba=[DBA1, DBA2],
    tipo="calculo", dificultad=3, fuente=FUENTE + ", tema 4 (ejemplo resuelto: primer encierro de π)",
    notas="ejemplo resuelto de la explicación; el lado del hexágono circunscrito (2/√3) se da, "
          "o se obtiene con Pitágoras",
    enunciado=r"En un círculo de radio $1$ se dibujan un hexágono regular inscrito (lado $1$) y uno "
              r"circunscrito (lado $\dfrac{2}{\sqrt{3}}$). Usa sus perímetros para demostrar que "
              r"$3 < \pi < 2\sqrt{3}$.",
    respuesta=r"La circunferencia mide $2\pi$ y está entre los dos perímetros: "
              r"$6 < 2\pi < 6 \cdot \frac{2}{\sqrt{3}} = \frac{12}{\sqrt{3}} = 4\sqrt{3}$. Dividiendo "
              r"entre $2$: $3 < \pi < 2\sqrt{3} \approx \num{3,46}$.")
def _():
    lado_c = 2 / sqrt(3)
    # el lado circunscrito sale de Pitágoras: apotema 1, mitad del lado = lado/2, radio = lado
    assert (lado_c**2 - (lado_c / 2) ** 2 - 1).simplify() == 0
    per_c = 6 * lado_c
    assert (per_c - 4 * sqrt(3)).simplify() == 0
    assert 6 < 2 * pi < per_c
    assert 3 < pi < 2 * sqrt(3) and round(float(2 * sqrt(3)), 2) == 3.46


@ejercicio(
    id="irracionales-8-024", tema="radicales en contexto", grados=[8], dba=[DBA2],
    tipo="contexto", dificultad=2, fuente=FUENTE + ", tema 4",
    notas="usa el teorema de Pitágoras como herramienta (decisión de la docente, 2026-09-14)",
    enunciado=r"Una escalera de $5$ m se apoya contra una pared, con la base a $2$ m del muro. "
              r"¿A qué altura llega? Da el resultado exacto (radical simplificado) y una "
              r"aproximación con dos cifras decimales.",
    respuesta=r"$h = \sqrt{5^2 - 2^2} = \sqrt{21} \approx \num{4,58}$ m ($\sqrt{21}$ ya está "
              r"simplificado: $21 = 3 \cdot 7$ no tiene factores cuadrados).")
def _():
    h = sqrt(5**2 - 2**2)
    assert h == sqrt(21) and round(float(h), 2) == 4.58
    assert h.is_rational is False


@ejercicio(
    id="irracionales-8-025", tema="radicales en contexto", grados=[8], dba=[DBA1, DBA2],
    tipo="argumentacion", dificultad=2, fuente=FUENTE + ", tema 4",
    notas="corrige el ejercicio de la guía anterior («casi nunca es racional», falso para 3 × 4)",
    enunciado=r"Calcula la diagonal exacta de un jardín rectangular de $6$ m por $4$ m y la de uno de "
              r"$3$ m por $4$ m. ¿Por qué una es racional y la otra no?",
    respuesta=r"$\sqrt{6^2 + 4^2} = \sqrt{52} = 2\sqrt{13} \approx \num{7,21}$ m, irracional; "
              r"$\sqrt{3^2 + 4^2} = \sqrt{25} = 5$ m, racional. La diagonal es racional solo cuando "
              r"$a^2 + b^2$ es un cuadrado perfecto (como $9 + 16 = 25$).")
def _():
    d1, d2 = sqrt(6**2 + 4**2), sqrt(3**2 + 4**2)
    assert d1 == 2 * sqrt(13) and d1.is_rational is False and round(float(d1), 2) == 7.21
    assert d2 == 5


@ejercicio(
    id="irracionales-8-026", tema="radicales en contexto", grados=[8], dba=[DBA2],
    tipo="contexto", dificultad=3, fuente=FUENTE + ", tema 4 (aplicación resuelta)",
    notas="aplicación resuelta de la explicación; 1 pulgada = 2,54 cm",
    enunciado=r"Un televisor de $32$ pulgadas (medida de la diagonal) tiene pantalla de razón "
              r"$16 : 9$. Si el ancho es $16k$ y el alto $9k$, halla la diagonal en función de $k$ y "
              r"calcula el ancho y el alto en pulgadas.",
    respuesta=r"Diagonal: $\sqrt{(16k)^2 + (9k)^2} = \sqrt{337}\,k \approx \num{18,36}\,k$. Con "
              r"$\sqrt{337}\,k = 32$, $k \approx \num{1,743}$: ancho $\approx \num{27,9}$ pulgadas y "
              r"alto $\approx \num{15,7}$ pulgadas.")
def _():
    from sympy import symbols
    k = symbols("k", positive=True)
    assert (sqrt((16 * k) ** 2 + (9 * k) ** 2) - sqrt(337) * k).simplify() == 0
    kv = Rational(32) / sqrt(337)
    assert round(float(sqrt(337)), 2) == 18.36 and round(float(kv), 3) == 1.743
    assert round(float(16 * kv), 1) == 27.9 and round(float(9 * kv), 1) == 15.7
