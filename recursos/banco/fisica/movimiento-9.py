"""Banco de ejercicios — Física 9° — Describir el movimiento: marco de referencia, posición,
trayectoria y desplazamiento.
Fuente: ejercicios propios para la semana 05 de Física 9° (hilo del trimestre I: «De
Aristóteles a Galileo: aprender a describir el movimiento»). El banco solo tenía cinemática de
10° (cinematica-10.py), centrada en velocidad y aceleración; los de marco de referencia y
trayectoria que sí servían (cinematica-10-001, -002, -008, -022) ya están usados en la guía del
trimestre, así que la sesión y su tarea se quedaban sin ejercicios.
Nota: los contextos son de Cali (el MIO, la ciclovía) para que el marco de referencia sea un
lugar que los estudiantes puedan imaginar.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/fisica/movimiento-9.py
"""
from sympy import Rational, nsimplify, sqrt

from ejercicios import ejercicio

FUENTE = "propio — clase de Física 9°, trimestre I, describir el movimiento"
COMUN = dict(tema="describir el movimiento", grados=[9], dba=["naturales-9-1"])


@ejercicio(id="movimiento-9-001", tipo="contexto", dificultad=1, fuente=FUENTE,
           enunciado=r"Una ruta del MIO va por una avenida recta. Tomamos como origen la "
                     r"estación Universidades y como sentido positivo el norte. El bus está "
                     r"primero en $x_1 = \qty{+800}{m}$ y después en $x_2 = \qty{+200}{m}$. "
                     r"a) ¿Cuál es su desplazamiento? b) Repite la cuenta poniendo el origen "
                     r"\qty{500}{m} al sur de la estación (allí las posiciones son "
                     r"\qty{1300}{m} y \qty{700}{m}). ¿Cambió el desplazamiento?",
           respuesta=r"a) $\Delta x = 200 - 800 = \qty{-600}{m}$: seiscientos metros hacia el "
                     r"sur (el signo indica el sentido). b) $\Delta x = 700 - 1300 = "
                     r"\qty{-600}{m}$: el mismo. Cambiar el origen cambia las posiciones, pero "
                     r"no el desplazamiento, porque el desplazamiento es una \emph{diferencia} "
                     r"de posiciones y el corrimiento se cancela al restar.",
           **COMUN)
def _():
    d1 = 200 - 800
    d2 = (200 + 500) - (800 + 500)
    assert d1 == -600 and d1 == d2


@ejercicio(id="movimiento-9-002", tipo="calculo", dificultad=2, fuente=FUENTE,
           enunciado=r"En la ciclovía, Laura da exactamente una vuelta a una manzana "
                     r"rectangular de \qty{120}{m} por \qty{80}{m} y termina donde arrancó. "
                     r"Tarda \qty{100}{s}. Calcula: a) la distancia recorrida; b) la magnitud "
                     r"del desplazamiento; c) la rapidez media; d) la velocidad media.",
           respuesta=r"a) Es el perímetro: $2(120) + 2(80) = \qty{400}{m}$. b) Cero: empezó y "
                     r"terminó en el mismo punto. c) $400/100 = \qty{4}{m/s}$. d) "
                     r"$0/100 = \qty{0}{m/s}$. No es un error: la rapidez mide cuánto camino "
                     r"hizo y la velocidad media, qué tan lejos quedó de donde arrancó. Dar la "
                     r"vuelta completa deja las dos cosas muy distintas.",
           **COMUN)
def _():
    perimetro = 2 * 120 + 2 * 80
    assert perimetro == 400
    assert Rational(perimetro, 100) == 4
    assert Rational(0, 100) == 0


@ejercicio(id="movimiento-9-003", tipo="encuentra-el-error", dificultad=2, fuente=FUENTE,
           enunciado=r"Un estudiante camina \qty{5}{m} hacia el oriente y luego \qty{12}{m} "
                     r"hacia el norte. Escribe: «mi desplazamiento fue de \qty{17}{m}». "
                     r"Encuentra el error, corrígelo y di qué fue lo que sí calculó.",
           respuesta=r"Lo que calculó fueron \qty{17}{m} de \emph{distancia recorrida}: la "
                     r"longitud del camino, $5 + 12$. El desplazamiento es el segmento recto "
                     r"desde donde arrancó hasta donde terminó, y como los dos tramos son "
                     r"perpendiculares se halla con Pitágoras: $\sqrt{5^2 + 12^2} = "
                     r"\sqrt{169} = \qty{13}{m}$, hacia el nororiente. El desplazamiento nunca "
                     r"es mayor que la distancia recorrida; solo son iguales cuando el camino "
                     r"es recto y sin devolverse.",
           **COMUN)
def _():
    recorrido = 5 + 12
    desplazamiento = sqrt(5 ** 2 + 12 ** 2)
    assert recorrido == 17
    assert desplazamiento == 13
    assert desplazamiento < recorrido


@ejercicio(id="movimiento-9-004", tipo="conceptual", dificultad=2, fuente=FUENTE,
           enunciado=r"Un pasajero va sentado y quieto en su silla de un bus que viaja por una "
                     r"recta a \qty{60}{km/h}. a) ¿Cuál es su velocidad respecto del bus? "
                     r"b) ¿Y respecto de la vía? Da esta última también en \unit{m/s}. "
                     r"c) ¿Está el pasajero en movimiento o en reposo?",
           respuesta=r"a) Cero: respecto del bus no cambia de posición. b) \qty{60}{km/h}, que "
                     r"en \unit{m/s} es $60 \div \num{3,6} = \qty{16,7}{m/s}$ "
                     r"(exactamente $\frac{50}{3}$). c) Las dos cosas, y no hay contradicción: "
                     r"estar en movimiento o en reposo no es una propiedad del pasajero, sino "
                     r"de la pareja pasajero–marco de referencia. Por eso lo primero al "
                     r"describir un movimiento es decir desde dónde se mira.",
           **COMUN)
def _():
    ms = Rational(60 * 1000, 3600)
    assert ms == Rational(50, 3)
    assert nsimplify(round(float(ms), 1)) == Rational(167, 10)
