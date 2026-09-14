"""Banco de ejercicios — Matemáticas — Preguntas liberadas del Icfes (Saber 11.º).
Fuente: Icfes, Cuadernillo de preguntas, Prueba Matemáticas, Saber 11.º (marzo de 2026),
recursos/matematicas/icfes/09-Marzo_Cuadernillo-de-Preguntas-Matematicas-Saber-11-2026.pdf
© Icfes, 2026. Uso académico, sin ánimo de lucro, citando al Icfes. Los enunciados y las
opciones se transcriben TEXTUALMENTE (solo se pasan las fórmulas a LaTeX): transformarlos
requiere autorización expresa del Icfes (ver recursos/CLAUDE.md). Si una pregunta tiene un
error, se le avisa a la docente; no se corrige aquí.
La letra correcta es la de la «Tabla de respuestas correctas» del cuadernillo; la explicación
de la respuesta es nuestra y la comprobación verifica que coincida con esa clave.
Se escogieron las preguntas de Cálculo 11° que no dependen de una figura. La 43 (función
f(x) = 5/x y el área x·f(x); clave B, la recta horizontal y = 5) tiene opciones gráficas:
se usa imprimiendo la página 28 del PDF.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/icfes-cuadernillo-2026.py
"""
from sympy import Interval, Rational, log, oo, simplify, solve, solveset, symbols
from sympy import S as Reales

from ejercicios import desigualdad, ejercicio

CITA = "Icfes, Cuadernillo de preguntas Matemáticas Saber 11.º (marzo 2026), pregunta"
NOTA = "Transcripción textual del Icfes (© Icfes 2026, uso académico): no modificar."
COMUN = dict(grados=[11], tipo="seleccion", notas=NOTA)

x, y, D, j = symbols("x y D j", real=True)


def opciones(*items):
    return r" \begin{opciones} " + " ".join(r"\item " + i for i in items) + r" \end{opciones}"


def unica(valores, correcta):
    """La clave del Icfes es la única opción que cumple."""
    return [k for k, v in valores.items() if v] == [correcta]


# ---------- Números reales, porcentajes y potencias ----------

@ejercicio(
    id="icfes-cuadernillo-2026-002", tema="porcentajes y proporcionalidad",
    dba=["matematicas-11-1"], dificultad=2, fuente=f"{CITA} 2",
    enunciado=r"Una persona que vive en Colombia tiene inversiones en dólares en Estados Unidos, "
              r"y sabe que la tasa de cambio del dólar respecto al peso colombiano se mantendrá "
              r"constante este mes, siendo 1 dólar equivalente a 4.000 pesos colombianos y que "
              r"su inversión, en dólares, le dará ganancias del 3~\% en el mismo periodo. Un "
              r"amigo le asegura que en pesos sus ganancias también serán del 3~\%. ¿La "
              r"afirmación de su amigo es correcta?" + opciones(
                  r"Sí, porque, sin importar las variaciones en la tasa de cambio, la proporción "
                  r"en que aumenta la inversión en dólares es la misma que en pesos.",
                  r"No, porque debería conocerse el valor exacto de la inversión para poder "
                  r"calcular la cantidad de dinero que ganará.",
                  r"Sí, porque el 3~\% representa una proporción fija en cualquiera de las dos "
                  r"monedas, puesto que la tasa de cambio permanecerá constante.",
                  r"No, porque el 3~\% representa un incremento, que será mayor en pesos "
                  r"colombianos, pues en esta moneda cada dólar representa un valor 4.000 veces "
                  r"mayor."),
    respuesta=r"c) Si se invierten $D$ dólares, en pesos se pasa de $4000D$ a "
              r"$4000 \cdot \num{1,03}D$: la ganancia es $\dfrac{4000 \cdot \num{0,03}D}{4000D} "
              r"= 3~\%$, porque la tasa de cambio es constante (si cambiara, como supone la "
              r"opción a, el porcentaje en pesos sería otro).", **COMUN)
def _():
    en_pesos = lambda tasa_final: (tasa_final * D * Rational(103, 100) - 4000 * D) / (4000 * D)
    assert simplify(en_pesos(4000)) == Rational(3, 100)
    assert simplify(en_pesos(4100)) != Rational(3, 100)          # la opción a falla


@ejercicio(
    id="icfes-cuadernillo-2026-027", tema="densidad de los números reales",
    dba=["matematicas-11-1"], dificultad=1, fuente=f"{CITA} 27",
    enunciado=r"Una prueba atlética tiene un récord mundial de 10,49 segundos y un récord "
              r"olímpico de 10,50 segundos. ¿Es posible que un atleta registre un tiempo, en el "
              r"mismo tipo de prueba, que rompa el récord olímpico pero no el mundial?" + opciones(
                  r"Sí, porque puede registrar, por ejemplo, un tiempo de 10,497 segundos, que "
                  r"está entre los dos tiempos récord.",
                  r"Sí, porque puede registrar un tiempo menor que 10,4 y marcaría un nuevo "
                  r"récord.",
                  r"No, porque no existe un registro posible entre los dos tiempos récord.",
                  r"No, porque cualquier registro menor que el récord olímpico va a ser menor que "
                  r"el récord mundial."),
    respuesta=r"a) Entre dos números reales distintos siempre hay otros (densidad): "
              r"$\num{10,49} < \num{10,497} < \num{10,50}$, así que $\num{10,497}$ rompe el "
              r"récord olímpico pero no el mundial.", **COMUN)
def _():
    mundial, olimpico, t = Rational("10.49"), Rational("10.50"), Rational("10.497")
    assert mundial < t < olimpico
    assert Rational("10.3") < mundial                        # b: menos de 10,4 rompe ambos
    assert mundial < (mundial + olimpico) / 2 < olimpico     # c y d fallan


@ejercicio(
    id="icfes-cuadernillo-2026-040", tema="densidad de los números reales",
    dba=["matematicas-11-1"], dificultad=2, fuente=f"{CITA} 40",
    enunciado=r"Se puede encontrar números racionales mayores que un número entero $k$, de "
              r"manera que sean cada vez más cercanos a él, calculando $k + \frac{1}{j}$ (con "
              r"$j$ entero positivo). Cuanto más grande sea $j$, más cercano a $k$ será el "
              r"racional construido. ¿Cuántos números racionales se pueden construir cercanos a "
              r"$k$ y menores que $k + \frac{1}{11}$?" + opciones(
                  r"10, que es la cantidad de racionales menores que 11.",
                  r"Una cantidad infinita, pues existen infinitos números enteros mayores que 11.",
                  r"11, que es el número que equivale en este caso a $j$.",
                  r"Uno, pues el racional más cercano a $k$ se halla con $j = 10$, es decir, con "
                  r"$k + 0{,}1$."),
    respuesta=r"b) $k + \frac{1}{j} < k + \frac{1}{11} \iff \frac{1}{j} < \frac{1}{11} \iff "
              r"j > 11$ (con $j$ positivo): sirve cualquier entero $12, 13, 14, \ldots$, que son "
              r"infinitos.", **COMUN)
def _():
    assert solveset(1 / j < Rational(1, 11), j, Interval.open(0, oo)) == Interval.open(11, oo)
    assert 1 + Rational(1, 10) > 1 + Rational(1, 11)          # d: j = 10 no sirve


@ejercicio(
    id="icfes-cuadernillo-2026-034", tema="potencias y logaritmos",
    dba=["matematicas-11-1", "matematicas-11-3"], dificultad=2, fuente=f"{CITA} 34",
    enunciado=r"Una regla usada en física indica que, para aumentar el nivel de intensidad del "
              r"sonido en 10 dB (dB es decibelios, la unidad de medida del nivel de intensidad "
              r"del sonido), es necesario que la intensidad medida se multiplique por 10. Ramiro "
              r"es el encargado de aumentar en 20 dB la medida del nivel de intensidad del "
              r"sistema de sonido de un evento y, según su interpretación de la regla, "
              r"multiplica por 20 la intensidad actual del sistema. ¿Es correcta su "
              r"interpretación?" + opciones(
                  r"No, porque la regla no considera aumentos de 20 dB, solamente de 10 dB; no "
                  r"hay consideraciones para aumentos mayores.",
                  r"Sí, porque la regla presentada indica que para aumentar en $x$ unidades el "
                  r"nivel de la medida de intensidad se agrega $x$ a la intensidad.",
                  r"No, porque aumentar 20 dB equivale a aumentar 10 dB dos veces, es decir, "
                  r"multiplicar por 10 la intensidad dos veces; en total, multiplicar por 100.",
                  r"Sí, porque el resultado de multiplicar dos veces por 10 la intensidad es "
                  r"multiplicarla por 20; así, se ahorra un paso y obtiene el resultado "
                  r"correcto."),
    respuesta=r"c) Cada aumento de 10 dB multiplica la intensidad por 10; dos aumentos la "
              r"multiplican por $10 \cdot 10 = 100$, no por $20$ (el nivel crece con el "
              r"logaritmo de la intensidad: $10\log_{10} 100 = 20$ dB).", **COMUN)
def _():
    decibeles = lambda factor: 10 * log(factor, 10)
    assert decibeles(100) == 20 and decibeles(10) == 10
    assert simplify(decibeles(20) - 20) != 0                  # multiplicar por 20 no da 20 dB


@ejercicio(
    id="icfes-cuadernillo-2026-047", tema="potencias y logaritmos",
    dba=["matematicas-11-1", "matematicas-11-3"], dificultad=1, fuente=f"{CITA} 47",
    enunciado=r"La expresión $10^3 = \dfrac{I}{I_0}$ relaciona la sonoridad de un sonido de 30 "
              r"decibeles con su intensidad ($I$) y la menor intensidad ($I_0$) que percibe el "
              r"oído humano. ¿Cuántas veces es el valor de $I$ respecto a $I_0$?" + opciones(
                  "Una milésima.", "Un tercio.", "Tres veces.", "Mil veces."),
    respuesta=r"d) $\dfrac{I}{I_0} = 10^3 = 1000$: $I$ es mil veces $I_0$.", **COMUN)
def _():
    razon = 10**3
    assert unica({"a": razon == Rational(1, 1000), "b": razon == Rational(1, 3),
                  "c": razon == 3, "d": razon == 1000}, "d")


@ejercicio(
    id="icfes-cuadernillo-2026-035", tema="porcentajes y proporcionalidad",
    dba=["matematicas-11-1"], tipo="encuentra-el-error", grados=[11], notas=NOTA,
    dificultad=2, fuente=f"{CITA} 35",
    enunciado=r"En una librería se ofrece un descuento del 10~\% sobre el precio original de "
              r"todos los libros impresos. Juan tiene un cupón de descuento adicional del 10~\% "
              r"sobre el precio de venta, el cual incluye el descuento inicial. Para saber "
              r"cuánto debe pagar por un libro cuyo precio original es de \$~50, Juan efectúa el "
              r"siguiente procedimiento: Paso 1. Multiplica el precio original del libro por 9. "
              r"Paso 2. Divide el resultado del paso 1 entre 10. Paso 3. Multiplica el resultado "
              r"del paso 2 por 10. Paso 4. Divide el resultado del paso 3 entre 100. ¿En cuál "
              r"paso del procedimiento hay un error?" + opciones(
                  r"En el paso 1, porque el precio de venta es el 90~\% del precio original, por "
                  r"tanto, debe multiplicarse por 90 y no por 9.",
                  r"En el paso 3, porque el precio final es el 90~\% del precio de venta, por "
                  r"tanto, debe multiplicarse por 90 y no por 10.",
                  r"En el paso 2, porque para calcular el precio al aplicar un porcentaje de "
                  r"descuento es necesario dividir entre 100 y no entre 10.",
                  r"En el paso 4, porque solo es necesario dividir una vez para calcular el "
                  r"precio final; es suficiente con la división del paso 2."),
    respuesta=r"b) Los pasos 1 y 2 dan el precio de venta, $50 \cdot 9 / 10 = 45$. El cupón deja "
              r"el 90~\% de eso: $45 \cdot 90 / 100 = \num{40,5}$; con el paso 3 como está se "
              r"obtiene $45 \cdot 10 / 100 = \num{4,5}$.")
def _():
    correcto = 50 * Rational(90, 100) * Rational(90, 100)
    juan = Rational(50 * 9, 10) * 10 / 100
    corregido_b = Rational(50 * 9, 10) * 90 / 100
    assert correcto == Rational(81, 2) and juan != correcto and corregido_b == correcto
    assert Rational(50 * 90, 10) * 10 / 100 != correcto       # cambiar el paso 1 no basta


# ---------- Capacitación (preguntas 4 a 6) ----------

CAPACITACION = (
    r"Responde de acuerdo con la siguiente información. Para capacitar en informática básica a "
    r"los trabajadores de algunas dependencias de una empresa, se contrata una institución que "
    r"ofrece un plan educativo de 4 módulos: I. Fundamentación, 40 h, \$~35.000 por hora; "
    r"II. Procesador de texto, 30 h, \$~30.000 por hora; III. Hoja de cálculo, 40 h, "
    r"\$~40.000 por hora; IV. Presentación con diapositivas, 10 h, \$~45.000 por hora. La "
    r"capacitación de cada módulo se hace con cursos de mínimo 20 y máximo 30 personas, de la "
    r"misma dependencia. ")
MODULOS = {"I": 40 * 35000, "II": 30 * 30000, "III": 40 * 40000, "IV": 10 * 45000}


def cursos(personas):
    """Menor número de cursos (de 20 a 30 personas) para un grupo, o None si no se puede."""
    for n in range(1, personas // 20 + 1):
        if 20 * n <= personas <= 30 * n:
            return n
    return None


@ejercicio(
    id="icfes-cuadernillo-2026-004", tema="desigualdades en contexto",
    dba=["matematicas-11-2"], dificultad=3, fuente=f"{CITA} 4",
    enunciado=CAPACITACION + r"La empresa pagará \$4.200.000 por capacitar a los trabajadores "
              r"de la dependencia «Insumos» en el módulo I, ¿cuántos empleados tiene esta "
              r"dependencia?" + opciones(
                  "Entre 20 y 30 trabajadores.", "Entre 41 y 60 trabajadores.",
                  "Entre 61 y 90 trabajadores.", "Entre 80 y 120 trabajadores."),
    respuesta=r"c) Un curso del módulo I cuesta $40 \cdot 35\,000 = 1\,400\,000$, así que se "
              r"pagan $3$ cursos. Si la empresa arma la menor cantidad de cursos, con $60$ o "
              r"menos personas bastarían $2$; con $3$ cursos de hasta $30$ caben $90$: entre $61$ "
              r"y $90$ trabajadores.", **COMUN)
def _():
    n_cursos = Rational(4200000, MODULOS["I"])
    posibles = [p for p in range(1, 200) if cursos(p) == n_cursos]
    assert n_cursos == 3 and (min(posibles), max(posibles)) == (61, 90)
    rangos = {"a": (20, 30), "b": (41, 60), "c": (61, 90), "d": (80, 120)}
    assert unica({k: v == (61, 90) for k, v in rangos.items()}, "c")


@ejercicio(
    id="icfes-cuadernillo-2026-005", tema="operaciones con números reales",
    dba=["matematicas-11-1"], dificultad=2, fuente=f"{CITA} 5",
    enunciado=CAPACITACION + r"Si se les cobrara a los 50 trabajadores de la dependencia "
              r"«Recursos Humanos» la capacitación del módulo II, y todos pagaran el mismo valor, "
              r"¿cuánto debería pagar cada uno por esa capacitación?" + opciones(
                  r"\$~18.000", r"\$~36.000", r"\$~450.000", r"\$~900.000"),
    respuesta=r"b) $50$ personas se reparten en $2$ cursos (de $25$); cada curso del módulo II "
              r"cuesta $30 \cdot 30\,000 = 900\,000$: en total $1\,800\,000$, y "
              r"$1\,800\,000 / 50 = 36\,000$ pesos por persona.", **COMUN)
def _():
    cada_uno = Rational(cursos(50) * MODULOS["II"], 50)
    assert cursos(50) == 2 and cada_uno == 36000
    assert unica({k: v == cada_uno for k, v in
                  {"a": 18000, "b": 36000, "c": 450000, "d": 900000}.items()}, "b")


@ejercicio(
    id="icfes-cuadernillo-2026-006", tema="operaciones con números reales",
    dba=["matematicas-11-1"], dificultad=2, fuente=f"{CITA} 6",
    enunciado=CAPACITACION + r"La empresa paga \$~900.000 por la capacitación de los 40 "
              r"funcionarios de la dependencia «Importaciones». De acuerdo con el valor pagado, "
              r"¿cuál de los siguientes módulos corresponde al tomado por la dependencia "
              r"«Importaciones»?" + opciones("I.", "II.", "III.", "IV."),
    respuesta=r"d) $40$ personas forman $2$ cursos, así que cada curso costó "
              r"$900\,000 / 2 = 450\,000$, que es el valor del módulo IV: "
              r"$10 \cdot 45\,000 = 450\,000$.", **COMUN)
def _():
    por_curso = Rational(900000, cursos(40))
    assert unica({"a": MODULOS["I"] == por_curso, "b": MODULOS["II"] == por_curso,
                  "c": MODULOS["III"] == por_curso, "d": MODULOS["IV"] == por_curso}, "d")


# ---------- Ecuaciones y sistemas ----------

@ejercicio(
    id="icfes-cuadernillo-2026-019", tema="ecuaciones de primer grado",
    dba=["matematicas-11-2"], dificultad=2, fuente=f"{CITA} 19",
    enunciado=r"En una feria robótica, el robot $P$ y el robot $Q$ disputan un juego de tenis de "
              r"mesa. En el momento que el marcador se encuentra 7 a 2 a favor del robot $P$, "
              r"estos se reprograman de tal forma que por cada 2 puntos que anota el robot $P$, "
              r"el robot $Q$ anota 3. ¿Cuál de las siguientes ecuaciones permite determinar "
              r"cuándo igualará en puntos el robot $Q$ al robot $P$?" + opciones(
                  r"$\frac{3}{2}x = 0$. Donde $x$ es la cantidad de puntos que anotará $P$.",
                  r"$7 + x = \frac{3}{2}x + 2$. Donde $x$ es la cantidad de puntos que anotará "
                  r"$P$.",
                  r"$7 + 3x = 2 + 2y$. Donde $x$ es la cantidad de puntos que anotará $P$, y $y$ "
                  r"es la cantidad de puntos que anotará $Q$.",
                  r"$x + y = 7 + 2$. Donde $x$ es la cantidad de puntos que anotará $P$, y $y$ "
                  r"es la cantidad de puntos que anotará $Q$."),
    respuesta=r"b) Si $P$ anota $x$ puntos, $Q$ anota $\frac{3}{2}x$; se igualan cuando "
              r"$7 + x = \frac{3}{2}x + 2$, es decir, con $x = 10$: $17$ a $17$.", **COMUN)
def _():
    (x_igual,) = solve(7 + x - (Rational(3, 2) * x + 2), x)
    assert x_igual == 10 and 7 + x_igual == 2 + Rational(3, 2) * x_igual == 17
    assert solve(Rational(3, 2) * x, x) == [0]                # a: x = 0 no iguala
    assert 7 + 3 * 10 != 2 + 2 * 15                           # c: con x = 10, y = 15 no cumple


@ejercicio(
    id="icfes-cuadernillo-2026-021", tema="sistemas de ecuaciones lineales",
    dba=["matematicas-11-2"], dificultad=2, fuente=f"{CITA} 21",
    enunciado=r"En una tienda se venden mesas a \$~40.000 y sillas a \$~20.000. El dueño de la "
              r"tienda olvidó registrar la cantidad total de mesas y sillas que se vendieron, "
              r"pero sabe que los ingresos por ventas del mes fueron de \$~1.400.000 y que se "
              r"vendieron 3 veces más sillas que mesas. Para determinar la cantidad vendida de "
              r"cada artículo, siendo $M$ la cantidad de mesas y $S$ la de sillas vendidas, "
              r"representó la información con las siguientes ecuaciones: Ecuación 1. "
              r"$40.000M + 20.000S = 1.400.000$. Ecuación 2. $M = 3S$. ¿Las ecuaciones "
              r"representan correctamente la situación?" + opciones(
                  r"No, porque aunque la ecuación 1 relaciona cada precio con la variable "
                  r"adecuada de forma correcta, la ecuación 2 significa que se venden 3 veces más "
                  r"mesas que sillas.",
                  r"Sí, porque la ecuación 1 relaciona cada precio con la variable adecuada y la "
                  r"ecuación 2 tiene en cuenta que la cantidad de sillas es 3 veces mayor que la "
                  r"de mesas.",
                  r"No, porque aunque la ecuación 2 tiene en cuenta que la cantidad de sillas es "
                  r"3 veces mayor que la de mesas, en la ecuación 1 los precios deberían estar "
                  r"dividiendo y no multiplicando.",
                  r"Sí, porque al solucionar las dos ecuaciones se obtiene un número entero, lo "
                  r"cual es consistente con las condiciones iniciales del problema."),
    respuesta=r"a) «3 veces más sillas que mesas» es $S = 3M$; con esa ecuación se vendieron "
              r"$14$ mesas y $42$ sillas. $M = 3S$ también da enteros ($30$ mesas y $10$ "
              r"sillas), así que que salga un entero no prueba nada (opción d).", **COMUN)
def _():
    M, S = symbols("M S")
    correcto = solve([40000 * M + 20000 * S - 1400000, S - 3 * M], [M, S])
    del_dueno = solve([40000 * M + 20000 * S - 1400000, M - 3 * S], [M, S])
    assert correcto == {M: 14, S: 42} and del_dueno == {M: 30, S: 10}
    assert del_dueno[S] != 3 * del_dueno[M]                   # su ecuación 2 no dice lo pedido


@ejercicio(
    id="icfes-cuadernillo-2026-031", tema="ecuaciones cuadráticas",
    dba=["matematicas-11-2"], dificultad=2, fuente=f"{CITA} 31",
    enunciado=r"Un profesor de Matemáticas les pide a sus estudiantes solucionar la siguiente "
              r"ecuación: $(x + 2)(x + 3) = 5(x + 3)$. María, Nelson y Óscar realizan, cada uno, "
              r"los siguientes procedimientos: María: $x^2 + 5x + 6 = 5x + 15$; $x^2 + 6 = 15$; "
              r"$x^2 = 15 - 6$; $x^2 = 9$; $x = \pm 3$. Nelson: $(x + 2)(x + 3) - 5(x + 3) = 0$; "
              r"$(x + 3)[(x + 2) - 5] = 0$; $(x + 3)(x - 3) = 0$; $x^2 - 9 = 0$; $x^2 = 9$; "
              r"$x = \pm 3$. Óscar: $x + 2 + x + 3 = 5 + x + 3$; $2x + 5 = x + 8$; "
              r"$2x - x = 8 - 5$; $x = 3$. ¿Cuál(es) estudiante(s) desarrolló(aron) un "
              r"procedimiento correcto para solucionar la ecuación?" + opciones(
                  "Solo Nelson y Óscar.", "Solo María y Nelson.", "Solamente Óscar.",
                  "Solamente María."),
    respuesta=r"b) María desarrolla el producto y Nelson factoriza $(x + 3)$: los dos llegan a "
              r"$x = \pm 3$, que son las soluciones. Óscar cambia los productos por sumas y "
              r"pierde $x = -3$ (para $x = -3$ ambos lados valen $0$).",
    **{**COMUN, "tipo": "encuentra-el-error"})
def _():
    soluciones = desigualdad("(x + 2)(x + 3) = 5(x + 3)")[1]
    assert soluciones == {-3, 3}
    maria = ["x^2 + 5x + 6 = 5x + 15", "x^2 + 6 = 15", "x^2 = 9"]
    nelson = ["(x + 2)(x + 3) - 5(x + 3) = 0", "(x + 3)*((x + 2) - 5) = 0", "x^2 - 9 = 0"]
    assert all(desigualdad(paso)[1] == soluciones for paso in maria + nelson)
    assert desigualdad("x + 2 + x + 3 = 5 + x + 3")[1] == {3}                  # Óscar


# ---------- Funciones como modelos ----------

@ejercicio(
    id="icfes-cuadernillo-2026-008", tema="función lineal",
    dba=["matematicas-11-7"], dificultad=2, fuente=f"{CITA} 8",
    enunciado=r"Un grupo de montañistas sabe que cada vez que aumenta la altitud en 100 m, la "
              r"temperatura disminuye en 1~°C. Si el grupo se encuentra a una altitud de "
              r"1.000 m, donde la temperatura es de 20~°C, ¿cuál de las siguientes expresiones "
              r"les permite determinar la temperatura que habrá cuando se encuentren a 4.000 m "
              r"de altitud?" + opciones(
                  r"$\text{Temperatura} = \left(\dfrac{\text{Altitud}}{100}\right) + 10$",
                  r"$\text{Temperatura} = -\,\text{Altitud} \times 100 + 30$",
                  r"$\text{Temperatura} = -\left(\dfrac{\text{Altitud}}{100}\right) + 30$",
                  r"$\text{Temperatura} = \text{Altitud} \times 100 + 10$"),
    respuesta=r"c) La temperatura baja $1$~°C cada $100$ m (pendiente $-\frac{1}{100}$) y a "
              r"$1000$ m vale $20$~°C: $-\frac{1000}{100} + 30 = 20$. A $4000$ m: "
              r"$-40 + 30 = -10$~°C. La opción a también da $20$~°C a $1000$ m, pero la "
              r"temperatura subiría con la altitud.", **COMUN)
def _():
    a = symbols("a")
    formulas = {"a": a / 100 + 10, "b": -a * 100 + 30, "c": -(a / 100) + 30, "d": a * 100 + 10}
    cumple = {k: f.subs(a, 1000) == 20 and f.subs(a, 1100) == 19 for k, f in formulas.items()}
    assert unica(cumple, "c") and formulas["c"].subs(a, 4000) == -10


@ejercicio(
    id="icfes-cuadernillo-2026-020", tema="función lineal",
    dba=["matematicas-11-7"], dificultad=2, fuente=f"{CITA} 20",
    enunciado=r"La tabla presenta la información sobre el gasto en publicidad y las ganancias de "
              r"una empresa durante los años 2020 a 2022 (datos en millones de pesos): 2020, "
              r"gasto en publicidad 200, ganancia obtenida 8.000; 2021, gasto 280, ganancia "
              r"10.400; 2022, gasto 250, ganancia 9.500. ¿Cuál es la función que representa la "
              r"ganancia obtenida $G$, en millones de pesos, en función del gasto en publicidad "
              r"$p$?" + opciones(r"$G(p) = 30p + 2.000$", r"$G(p) = 10p$", r"$G(p) = 40p$",
                                 r"$G(p) = 40p - 800$"),
    respuesta=r"a) Es la única que da los tres datos: $30 \cdot 200 + 2000 = 8000$, "
              r"$30 \cdot 280 + 2000 = 10\,400$ y $30 \cdot 250 + 2000 = 9500$ (la pendiente es "
              r"$\frac{10\,400 - 8000}{280 - 200} = 30$).",
    notas=NOTA + " La tabla del cuadernillo se escribe en línea.", grados=[11], tipo="seleccion")
def _():
    datos = {200: 8000, 280: 10400, 250: 9500}
    funciones = {"a": lambda p: 30 * p + 2000, "b": lambda p: 10 * p, "c": lambda p: 40 * p,
                 "d": lambda p: 40 * p - 800}
    assert unica({k: all(f(p) == g for p, g in datos.items()) for k, f in funciones.items()},
                 "a")


@ejercicio(
    id="icfes-cuadernillo-2026-049", tema="función exponencial",
    dba=["matematicas-11-7"], dificultad=2, fuente=f"{CITA} 49",
    enunciado=r"En determinada zona de una ciudad se construyen edificios de apartamentos en los "
              r"que cada metro cuadrado tiene un costo de \$~800.000, y se asegura a los "
              r"compradores que en esta zona anualmente, el metro cuadrado se valoriza un 5~\% "
              r"respecto al costo del año anterior. ¿Con cuál de las siguientes expresiones se "
              r"representa el costo de un metro cuadrado en esa zona, transcurridos $n$ años?"
              + opciones(r"$800.000 + 5n$", r"$800.000\,(5n)$",
                         r"$800.000\left(\dfrac{5}{100}\right)^n$",
                         r"$800.000\left(1 + \dfrac{5}{100}\right)^n$"),
    respuesta=r"d) Cada año el costo se multiplica por $1 + \frac{5}{100} = \num{1,05}$: después "
              r"de $1$ año vale $840\,000$, después de $2$, $882\,000$, y después de $n$, "
              r"$800\,000\left(1 + \frac{5}{100}\right)^n$.", **COMUN)
def _():
    n = symbols("n")
    esperado = {0: 800000, 1: 840000, 2: 882000}
    formulas = {"a": 800000 + 5 * n, "b": 800000 * (5 * n),
                "c": 800000 * Rational(5, 100)**n, "d": 800000 * (1 + Rational(5, 100))**n}
    assert unica({k: all(f.subs(n, a) == v for a, v in esperado.items())
                  for k, f in formulas.items()}, "d")
