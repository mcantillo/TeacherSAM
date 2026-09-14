"""Banco de ejercicios — Matemáticas — Preguntas liberadas del Icfes (Saber 11.º): geometría y medición.
Fuente: Icfes, Cuadernillo de preguntas, Prueba Matemáticas, Saber 11.º (marzo de 2026),
recursos/matematicas/icfes/09-Marzo_Cuadernillo-de-Preguntas-Matematicas-Saber-11-2026.pdf
© Icfes, 2026. Uso académico, sin ánimo de lucro, citando al Icfes. Los enunciados y las
opciones se transcriben TEXTUALMENTE (solo se pasan las fórmulas a LaTeX): transformarlos
requiere autorización expresa del Icfes (ver recursos/CLAUDE.md). Si una pregunta tiene un
error, se le avisa a la docente; no se corrige aquí.
La letra correcta es la de la «Tabla de respuestas correctas» del cuadernillo; la explicación
de la respuesta es nuestra y la comprobación verifica que coincida con esa clave.
Complementa icfes-cuadernillo-2026.py (preguntas de Cálculo 11°); los id usan el número de la
pregunta. Se escogieron las preguntas de geometría y medición (Geometría 11°: DBA 4, medición y
precisión; DBA 6, sistemas de coordenadas) cuyos datos están en el texto; cuando la figura del
cuadernillo solo ilustra, «notas» dice en qué página del PDF está, para imprimirla si se quiere.
No se incluyeron (se usan imprimiendo la página del PDF):
  18 (p. 15, triángulo de los faros: los datos 2, 1, 30°, 60°, 75° solo están en la figura; clave C),
  24 (p. 18, cuadrados construidos en las figuras 1 a 3; clave D),
  29 (p. 21, escalera: las medidas 5 y 13 solo están en la figura; clave C),
  42 (p. 27, maqueta de la cancha: las opciones son dibujos; clave D).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/icfes-cuadernillo-2026-geometria.py
"""
from sympy import Rational, pi, sin, sqrt, symbols, simplify, atan, deg, nsimplify
from sympy.geometry import Point, Polygon

from ejercicios import ejercicio

CITA = "Icfes, Cuadernillo de preguntas Matemáticas Saber 11.º (marzo 2026), pregunta"
NOTA = "Transcripción textual del Icfes (© Icfes 2026, uso académico): no modificar."
COMUN = dict(grados=[11], tipo="seleccion")
MEDICION = ["matematicas-11-4"]


def opciones(*items):
    return r" \begin{opciones} " + " ".join(r"\item " + i for i in items) + r" \end{opciones}"


def unica(valores, correcta):
    """La clave del Icfes es la única opción que cumple."""
    return [k for k, v in valores.items() if v] == [correcta]


def figura(pagina, que="solo ilustra la situación; los datos están en el texto"):
    return f"{NOTA} La figura del cuadernillo (p. {pagina} del PDF) {que}."


# ---------- Longitudes, áreas y volúmenes (DBA 4) ----------

@ejercicio(
    id="icfes-cuadernillo-2026-007", tema="semejanza y razón de áreas", dba=MEDICION,
    dificultad=2, fuente=f"{CITA} 7", notas=figura(9, "muestra el portalápices con el caucho "
                                                    "en la base y en la boca"),
    enunciado=r"La figura muestra el portalápices de Eliécer. Él sabe que es posible colocar un "
              r"caucho de 18 cm de perímetro alrededor de la base sin estirarlo, pero a medida "
              r"que sube el caucho por el portalápices, este se estira hasta que, en la boca del "
              r"portalápices, su perímetro es 24 cm. El portalápices tiene base y boca cuadrada, "
              r"por lo cual Eliécer afirma: «Como los perímetros de la base y la boca del "
              r"portalápices están en relación $\frac{18}{24} = \frac{3}{4}$, el área de la base "
              r"debe ser también tres cuartas partes del área de la boca del portalápices». ¿Es "
              r"verdadera esta afirmación?" + opciones(
                  r"No, porque la medición se realiza con el mismo caucho y, por tanto, las áreas "
                  r"de la base y la boca deben ser iguales.",
                  r"Sí, porque el caucho se estira dependiendo del área que encierre, por lo que "
                  r"las relaciones de las áreas y los perímetros son iguales.",
                  r"No, porque la relación obtenida se cumple para las longitudes de los lados, "
                  r"pero al calcular las áreas, la razón obtenida se eleva al cuadrado.",
                  r"Sí, porque como las figuras son semejantes, todas sus medidas deben tener la "
                  r"misma razón que los perímetros."),
    respuesta=r"c) Los lados miden $18/4 = \num{4,5}$ cm y $24/4 = 6$ cm (razón $\frac{3}{4}$), "
              r"pero las áreas son $\num{20,25}$ cm² y $36$ cm²: su razón es "
              r"$\left(\frac{3}{4}\right)^2 = \frac{9}{16}$, no $\frac{3}{4}$.", **COMUN)
def _():
    lado_base, lado_boca = Rational(18, 4), Rational(24, 4)
    assert lado_base / lado_boca == Rational(3, 4)
    razon_areas = lado_base**2 / lado_boca**2
    assert razon_areas == Rational(9, 16) and razon_areas != Rational(3, 4)   # b y d fallan
    assert razon_areas != 1                                                   # a falla


@ejercicio(
    id="icfes-cuadernillo-2026-014", tema="área del rectángulo", dba=MEDICION, dificultad=1,
    fuente=f"{CITA} 14", notas=NOTA,
    enunciado=r"Si en un rectángulo se aumenta la longitud de uno de sus lados en 100~\%, ¿Qué se "
              r"puede concluir de su área?" + opciones(
                  r"Aumenta en un 50~\%.", r"Se duplica.", r"No cambia.",
                  r"Aumenta en 100 unidades."),
    respuesta=r"b) Si los lados miden $b$ y $h$, aumentar $b$ en un 100~\% lo vuelve $2b$: el "
              r"área pasa de $bh$ a $2b \cdot h = 2(bh)$.", **COMUN)
def _():
    b, h = symbols("b h", positive=True)
    nueva, vieja = (b + b * Rational(100, 100)) * h, b * h
    assert simplify(nueva / vieja) == 2
    assert unica({"a": simplify(nueva / vieja - Rational(3, 2)) == 0,
                  "b": simplify(nueva / vieja - 2) == 0,
                  "c": simplify(nueva - vieja) == 0,
                  "d": simplify(nueva - vieja - 100) == 0}, "b")


@ejercicio(
    id="icfes-cuadernillo-2026-017", tema="aristas de un prisma rectangular", dba=MEDICION,
    dificultad=1, fuente=f"{CITA} 17",
    notas=figura(14, "muestra la caja con las aristas marcadas l, a y h"),
    enunciado=r"La longitud de las aristas de la caja de la figura son $l$, $a$ y $h$. ¿Cuál de las "
              r"siguientes expresiones determina la longitud total de las aristas de la caja?"
              + opciones(r"$lah$", r"$4lah$", r"$l+a+h$", r"$4l + 4a + 4h$"),
    respuesta=r"d) Una caja tiene $12$ aristas: $4$ de largo $l$, $4$ de ancho $a$ y $4$ de alto "
              r"$h$; en total $4l + 4a + 4h$ ($lah$ es su volumen).", **COMUN)
def _():
    l, a, h = symbols("l a h", positive=True)
    # aristas de la caja [0, l] x [0, a] x [0, h]: pares de vértices que difieren en una coordenada
    vertices = [(x, y, z) for x in (0, l) for y in (0, a) for z in (0, h)]
    aristas = [(p, q) for i, p in enumerate(vertices) for q in vertices[i + 1:]
               if sum(u != v for u, v in zip(p, q)) == 1]
    total = sum(sum(abs(u - v) for u, v in zip(p, q)) for p, q in aristas)
    assert len(aristas) == 12
    formulas = {"a": l * a * h, "b": 4 * l * a * h, "c": l + a + h, "d": 4 * l + 4 * a + 4 * h}
    assert unica({k: simplify(f - total) == 0 for k, f in formulas.items()}, "d")


@ejercicio(
    id="icfes-cuadernillo-2026-022", tema="medición indirecta con trigonometría", dba=MEDICION,
    dificultad=2, fuente=f"{CITA} 22",
    notas=figura(17, "muestra el triángulo con el lado de 120 cm junto al ángulo de 45° y el "
                     "corte punteado"),
    enunciado=r"La línea punteada en la figura muestra un corte realizado a un triángulo. El corte "
              r"es paralelo a la base y corta por la mitad a la altura, $h$, que es perpendicular a "
              r"la base. Para realizar el corte, se determinó la altura del triángulo usando la "
              r"fórmula $\sen(45^\circ) = \frac{h}{120}$; luego se dividió h entre dos. Realizando "
              r"este procedimiento, y teniendo en cuenta que "
              r"$\sen(45^\circ) = \frac{\sqrt{2}}{2} \approx \num{0,71}$, ¿cuál fue, "
              r"aproximadamente, la distancia a la que se cortó la altura del triángulo?"
              + opciones("85 cm.", "60 cm.", "42 cm.", "30 cm."),
    respuesta=r"c) $h = 120 \sen(45^\circ) \approx 120 \cdot \num{0,71} = \num{85,2}$ cm, y la "
              r"mitad es $\num{42,6} \approx 42$ cm (con el valor exacto, "
              r"$h/2 = 30\sqrt{2} \approx \num{42,4}$ cm). La opción a es $h$ sin dividir.",
    **COMUN)
def _():
    h_aprox = 120 * Rational(71, 100)
    mitad = h_aprox / 2
    assert mitad == Rational(426, 10)
    assert abs(float(120 * sin(pi / 4) / 2) - 42.43) < 0.01
    valores = {"a": 85, "b": 60, "c": 42, "d": 30}
    cercana = min(valores, key=lambda k: abs(valores[k] - mitad))
    assert cercana == "c" and abs(valores["a"] - h_aprox) < 1       # a: olvidó dividir


@ejercicio(
    id="icfes-cuadernillo-2026-023", tema="medición indirecta con trigonometría", dba=MEDICION,
    dificultad=2, fuente=f"{CITA} 23",
    notas=figura(17, "muestra el cartabón con el ángulo de 60° y el cateto de 32 cm; el recuadro "
                     "«Recuerde que» se transcribe (con tan, como en el original)"),
    enunciado=r"Un cartabón es una plantilla que se utiliza en dibujo técnico y que tiene forma de "
              r"triángulo rectángulo escaleno, de modo que su hipotenusa mide el doble del cateto "
              r"de menor longitud. Recuerde que: $\sen 30^\circ = \frac{1}{2}$; "
              r"$\sen 60^\circ = \frac{\sqrt{3}}{2}$; $\cos 30^\circ = \frac{\sqrt{3}}{2}$; "
              r"$\cos 60^\circ = \frac{1}{2}$; $\tan 30^\circ = \frac{1}{\sqrt{3}}$; "
              r"$\tan 60^\circ = \sqrt{3}$; Si el cateto más largo de un cartabón mide 32 "
              r"centímetros, como muestra la figura, ¿cuál de las siguientes medidas corresponde "
              r"a su cateto menor?" + opciones(
                  "16 cm.", r"$\frac{32}{\sqrt{3}}$ cm.", "27 cm.", r"$\frac{64}{\sqrt{3}}$ cm."),
    respuesta=r"b) Si el cateto menor mide $c$, la hipotenusa mide $2c$ y, por Pitágoras, "
              r"$c^2 + 32^2 = (2c)^2$, así que $3c^2 = 1024$ y $c = \frac{32}{\sqrt{3}} "
              r"\approx \num{18,5}$ cm (también $\tan 30^\circ = \frac{c}{32}$).", **COMUN)
def _():
    candidatos = {"a": 16, "b": 32 / sqrt(3), "c": 27, "d": 64 / sqrt(3)}
    cumple = {k: simplify(c**2 + 32**2 - (2 * c)**2) == 0 for k, c in candidatos.items()}
    assert unica(cumple, "b")
    assert simplify(32 * sqrt(3) / 3 - 32 / sqrt(3)) == 0                    # = 32·tan 30°


@ejercicio(
    id="icfes-cuadernillo-2026-044", tema="área de un sector circular", dba=MEDICION,
    dificultad=2, fuente=f"{CITA} 44",
    notas=figura(29, "muestra la rueda dividida en 10 sectores"),
    enunciado=r"En un parque hay una rueda giratoria de 3 m de radio. La rueda está diseñada para "
              r"10 personas, cada una en un sector circular de igual área, como muestra la figura. "
              r"Para determinar el área que le corresponde a cada persona, se divide $2\pi$ entre "
              r"10 lo que determina el ángulo $\theta$ de cada sector y se usa la fórmula del área "
              r"de un sector circular $S$: $S = r^2\,\frac{\theta}{2}$ donde $r$ es el radio de la "
              r"circunferencia. Utilizando una aproximación de $\pi = 3$, ¿cuál es el área "
              r"aproximada que le corresponde a cada persona?" + opciones(
                  r"$\num{3,6}$ m²", r"$\num{2,7}$ m²", r"$\num{9,0}$ m²", r"$\num{1,8}$ m²"),
    respuesta=r"b) $\theta = \frac{2\pi}{10} \approx \frac{2 \cdot 3}{10} = \num{0,6}$ y "
              r"$S = 3^2 \cdot \frac{\num{0,6}}{2} = \num{2,7}$ m² (con el valor exacto de $\pi$, "
              r"$S = \frac{9\pi}{10} \approx \num{2,83}$ m²).", **COMUN)
def _():
    theta = 2 * 3 / Rational(10)
    S = 3**2 * theta / 2
    assert S == Rational(27, 10)
    assert simplify(3**2 * (2 * pi / 10) / 2 - pi * 3**2 / 10) == 0          # = círculo / 10
    valores = {"a": Rational(36, 10), "b": Rational(27, 10), "c": 9, "d": Rational(18, 10)}
    assert unica({k: v == S for k, v in valores.items()}, "b")


@ejercicio(
    id="icfes-cuadernillo-2026-050", tema="volumen de cuerpos redondos y prismas", dba=MEDICION,
    dificultad=2, fuente=f"{CITA} 50",
    notas=figura(32, "es una tabla con los tres empaques; el texto de sus casillas se transcribe"),
    enunciado=r"Alfonso tiene tres empaques para almacenar dulces. Los empaques y las medidas de "
              r"estos se muestran en la figura. 1. Un cilindro cuya altura es $h = 2$, y el radio "
              r"de la base mide $r = \left(\frac{3}{2}\right)$. 2. Una caja de base cuadrada, cuya "
              r"altura es $h = 2$ y el lado de la base mide $L = \left(\frac{3}{2}\right)$. 3. Una "
              r"esfera con radio $r = \left(\frac{3}{2}\right)$. ¿Cuál de las siguientes "
              r"afirmaciones es verdadera respecto al volumen de los tres empaques?" + opciones(
                  r"El volumen del cilindro es mayor que el volumen de la caja; además, el volumen "
                  r"de la esfera es igual que el volumen del cilindro.",
                  r"El volumen del cilindro es igual que el volumen de la caja; además, el volumen "
                  r"de la esfera es mayor que el volumen del cilindro.",
                  r"El volumen del cilindro es menor que el volumen de la caja; además, el volumen "
                  r"de la esfera es igual que el volumen del cilindro.",
                  r"El volumen del cilindro es mayor que el volumen de la caja; además, el volumen "
                  r"de la esfera es mayor que el volumen del cilindro."),
    respuesta=r"a) Cilindro: $\pi \left(\frac{3}{2}\right)^2 \cdot 2 = \frac{9\pi}{2}$; caja: "
              r"$\left(\frac{3}{2}\right)^2 \cdot 2 = \frac{9}{2}$; esfera: "
              r"$\frac{4}{3}\pi \left(\frac{3}{2}\right)^3 = \frac{9\pi}{2}$. El cilindro supera "
              r"a la caja ($\pi > 1$) y la esfera tiene el mismo volumen que el cilindro.", **COMUN)
def _():
    r = L = Rational(3, 2)
    cil, caja, esf = pi * r**2 * 2, L**2 * 2, Rational(4, 3) * pi * r**3
    assert cil == 9 * pi / 2 and caja == Rational(9, 2) and esf == 9 * pi / 2
    assert unica({"a": cil > caja and esf == cil, "b": cil == caja and esf > cil,
                  "c": cil < caja and esf == cil, "d": cil > caja and esf > cil}, "a")


# ---------- Ángulos, triángulos y circunferencia ----------

@ejercicio(
    id="icfes-cuadernillo-2026-015", tema="ángulos y rayos paralelos", dificultad=1,
    fuente=f"{CITA} 15",
    notas=figura(13, "muestra los dos postes con sus sombras y los ángulos α y β entre la acera y "
                     "la sombra"),
    enunciado=r"Las sombras proyectadas por dos postes paralelos de 10 metros y 5 metros se "
              r"muestran en la figura. El ángulo entre la acera horizontal y la sombra del poste 1 "
              r"es $\alpha = 30^\circ$. De acuerdo con esto, se puede afirmar que el ángulo entre "
              r"la acera horizontal y la sombra del poste 2 es" + opciones(
                  r"$\beta = 5^\circ$.", r"$\beta = 15^\circ$.", r"$\beta = 30^\circ$.",
                  r"$\beta = 60^\circ$."),
    respuesta=r"c) Los rayos del Sol que llegan a los dos postes son paralelos, así que forman el "
              r"mismo ángulo con la acera: $\beta = \alpha = 30^\circ$. El ángulo no depende de la "
              r"altura del poste; solo cambia la longitud de la sombra.", **COMUN)
def _():
    # con el ángulo del sol de 30°, la sombra de cada poste mide altura / tan 30°
    sombra = lambda altura: altura * sqrt(3)
    angulo = lambda altura: deg(atan(altura / sombra(altura)))
    assert angulo(10) == angulo(5) == 30
    assert unica({"a": angulo(5) == 5, "b": angulo(5) == 15, "c": angulo(5) == 30,
                  "d": angulo(5) == 60}, "c")


@ejercicio(
    id="icfes-cuadernillo-2026-037", tema="circunferencia: radio y cuerdas", dificultad=2,
    fuente=f"{CITA} 37", notas=NOTA,
    enunciado=r"Sobre una circunferencia de centro $O$ se localizan dos puntos $P$ y $P'$ "
              r"diferentes. De las siguientes, ¿cuál figura NO puede resultar al unir entre sí los "
              r"tres puntos $P$, $P'$ y $O$?" + opciones(
                  "Un triángulo isósceles.", "Un radio de la circunferencia.",
                  "Un triángulo equilátero.", "Un diámetro de la circunferencia."),
    respuesta=r"b) $OP = OP'$ son radios. Si $P$, $O$ y $P'$ no están alineados, se forma un "
              r"triángulo isósceles (equilátero si $\angle POP' = 60^\circ$); si están alineados, "
              r"$PP'$ es un diámetro. Al unir los tres puntos siempre aparecen $P$ y $P'$, que "
              r"son distintos: nunca queda un solo radio.", **COMUN)
def _():
    def figura_obtenida(angulo):        # ángulo POP', en grados, con 0 < ángulo <= 180
        O, P = Point(0, 0), Point(1, 0)
        Pp = Point(1, 0).rotate(pi * angulo / 180)
        if Point.is_collinear(O, P, Pp):
            return "diametro"
        t = Polygon(O, P, Pp)
        lados = sorted(nsimplify(s.length) for s in t.sides)
        return "equilatero" if lados[0] == lados[2] else "isosceles"
    obtenidas = {figura_obtenida(g) for g in (30, 60, 90, 120, 180)}
    assert obtenidas == {"isosceles", "equilatero", "diametro"}
    assert unica({"a": "isosceles" not in obtenidas, "b": "radio" not in obtenidas,
                  "c": "equilatero" not in obtenidas, "d": "diametro" not in obtenidas}, "b")


@ejercicio(
    id="icfes-cuadernillo-2026-041", tema="desigualdad triangular", dificultad=2,
    fuente=f"{CITA} 41", notas=NOTA,
    enunciado=r"Un terreno con forma triangular se debe encerrar, cumpliendo con los siguientes "
              r"requerimientos: \textbf{Requerimiento 1.} Uno de sus ángulos interiores debe ser "
              r"de 90°. \textbf{Requerimiento 2.} Dos lados deben medir 7 metros y el otro debe "
              r"medir 18 metros. \textbf{Requerimiento 3.} Uno de sus ángulos interiores debe ser "
              r"menor que 45°. \textbf{Requerimiento 4.} La suma de sus ángulos interiores debe "
              r"ser de 180°. ¿Cuál de los requerimientos es \textbf{imposible} de cumplir?"
              + opciones("Requerimiento 1.", "Requerimiento 2.", "Requerimiento 3.",
                         "Requerimiento 4."),
    respuesta=r"b) En todo triángulo cada lado es menor que la suma de los otros dos, y "
              r"$7 + 7 = 14 < 18$: no existe un triángulo con lados $7$, $7$ y $18$. Los otros "
              r"se cumplen, por ejemplo, con un triángulo rectángulo de catetos $7$ y $18$ (su "
              r"ángulo menor mide unos $21^\circ$), y la suma $180^\circ$ se cumple siempre.",
    **COMUN)
def _():
    es_triangulo = lambda a, b, c: a + b > c and a + c > b and b + c > a
    assert not es_triangulo(7, 7, 18)
    # catetos 7 y 18: ángulo recto y un ángulo agudo menor que 45°
    assert float(deg(atan(Rational(7, 18)))) < 45 and es_triangulo(7, 18, sqrt(7**2 + 18**2))


# ---------- Coordenadas cartesianas (DBA 6) ----------

@ejercicio(
    id="icfes-cuadernillo-2026-032", tema="figuras en el plano cartesiano",
    dba=["matematicas-11-6"], dificultad=2, fuente=f"{CITA} 32", notas=NOTA,
    enunciado=r"Un trapecio isósceles es un trapecio cuyos lados no paralelos son congruentes. En "
              r"un plano cartesiano se dibuja un trapecio isósceles de modo que el eje $y$ divide "
              r"al trapecio en dos figuras iguales. Si las coordenadas de dos de los vértices del "
              r"trapecio son $(-4, 2)$ y $(-2, 8)$, ¿cuáles son las coordenadas de los otros dos "
              r"vértices?" + opciones(r"$(8, 2)$ y $(2, 4)$.", r"$(2, 8)$ y $(4, 2)$.",
                                      r"$(-2, -4)$ y $(-8, -2)$.", r"$(-4, -2)$ y $(-2, -8)$."),
    respuesta=r"b) El eje $y$ es eje de simetría: cada vértice $(x, y)$ tiene su reflejo "
              r"$(-x, y)$. Los reflejos de $(-4, 2)$ y $(-2, 8)$ son $(4, 2)$ y $(2, 8)$; el "
              r"trapecio $(-4, 2)$, $(4, 2)$, $(2, 8)$, $(-2, 8)$ tiene las bases horizontales y "
              r"los lados no paralelos de longitud $\sqrt{40} = 2\sqrt{10}$.", **COMUN)
def _():
    dados = [Point(-4, 2), Point(-2, 8)]
    opciones_ = {"a": [Point(8, 2), Point(2, 4)], "b": [Point(2, 8), Point(4, 2)],
                 "c": [Point(-2, -4), Point(-8, -2)], "d": [Point(-4, -2), Point(-2, -8)]}
    reflejos = {Point(-p.x, p.y) for p in dados}

    def sirve(otros):
        if set(otros) != reflejos:                          # simetría respecto al eje y
            return False
        A, D = dados
        B, C = Point(-A.x, A.y), Point(-D.x, D.y)
        t = Polygon(A, B, C, D)
        return (A.y == B.y and C.y == D.y and t.sides[1].length == t.sides[3].length
                and t.sides[0].length != t.sides[2].length)
    assert unica({k: sirve(v) for k, v in opciones_.items()}, "b")
    assert Point(-4, 2).distance(Point(-2, 8)) == 2 * sqrt(10)
