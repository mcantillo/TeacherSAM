"""Banco de ejercicios — Física 10° — Dinámica: leyes de Newton, peso, fuerza normal, tensión
y diagramas de cuerpo libre.
Fuente: Guía de apoyo de Física 10° «Cinemática y dinámica», Capítulo 4 (Dinámica: leyes de
Newton del movimiento); se lee en
recursos/fisica/Guías pedagógicas Física/markdown/10 - Guia_de_apoyo_cinematica_y_dinamica_grado_10_fisica.md
Secciones: Preguntas, Problemas.
DBA: naturales grado 10 · DBA 1 — Comprende que el reposo o el movimiento rectilíneo uniforme
se presentan cuando las fuerzas aplicadas sobre el sistema se anulan entre ellas, y que en
presencia de fuerzas resultantes no nulas se producen cambios de velocidad.
g = 9,8 m/s² (la guía usa 9,80 m/s²).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/fisica/leyes-newton-10.py
"""
from math import asin, atan2, cos, degrees, hypot, radians, sin, sqrt

import sympy as sp
from sympy.physics.units import (centimeter, convert_to, gram, hour, kilogram, kilometer,
                                 meter, newton, second)

from ejercicios import ejercicio, ejercicio_manual

PRE = "leyes-newton-10"
G1 = "Guía de apoyo Física 10° (cinemática y dinámica), Cap. 4 Dinámica: leyes de Newton"
PREG = f"{G1}, Preguntas"
PROB = f"{G1}, Problemas"
COMUN = dict(tema="leyes de Newton", grados=[10], dba=["naturales-10-1"])

m, s, kg, N, km, h = meter, second, kilogram, newton, kilometer, hour
G = 9.8 * m / s**2
g = 9.8


def _meta(n, fuente, enunciado, respuesta, kw, tipo):
    d = dict(id=f"{PRE}-{n:03d}", fuente=fuente, enunciado=enunciado, respuesta=respuesta,
             tipo=tipo, dificultad=1, **COMUN)
    d.update(kw)
    return d


def E(n, fuente, enunciado, respuesta, **kw):
    return ejercicio(**_meta(n, fuente, enunciado, respuesta, kw, "calculo"))


def M(n, fuente, enunciado, respuesta, **kw):
    ejercicio_manual(**_meta(n, fuente, enunciado, respuesta, kw, "conceptual"))


def op(*items):
    return r" \begin{opciones} " + " ".join(r"\item " + i for i in items) + r" \end{opciones}"


def val(q, unidad):
    """Número de «unidad» que hay en q (unidad=1: cociente adimensional); falla si las
    dimensiones no coinciden."""
    if unidad == 1:
        return float(convert_to(q, [meter, kilogram, second]))
    return float(convert_to(q, unidad) / unidad)


def aprox(q, esperado, unidad, rel=0.01):
    v = val(q, unidad)
    assert abs(v - esperado) <= rel * abs(esperado), f"{v} ≠ {esperado}"


def cerca(x, esperado, rel=0.005):
    assert abs(x - esperado) <= rel * abs(esperado), f"{x} ≠ {esperado}"


# ---------- Preguntas ----------

M(1, f"{PREG} — 1",
  r"¿Por qué un niño sentado en un carrito parece caer hacia atrás cuando le das al carrito "
  r"un jalón repentino hacia adelante?",
  r"Por inercia (primera ley de Newton): el carrito acelera hacia adelante, pero el cuerpo "
  r"del niño tiende a seguir en reposo; respecto al carrito, el niño se va hacia atrás.")
M(2, f"{PREG} — 2a",
  r"Una caja descansa sobre la plataforma sin fricción de un camión, que arranca y acelera "
  r"hacia adelante; la caja empieza a deslizarse hacia la parte trasera. Analiza el "
  r"movimiento de la caja según las leyes de Newton, visto por Andrea, que está parada en el "
  r"suelo al lado del camión.",
  r"Para Andrea (marco inercial) sobre la caja no actúa ninguna fuerza horizontal (no hay "
  r"fricción), así que la caja sigue en reposo, como dice la primera ley; es el camión el "
  r"que acelera y se mueve por debajo de ella.")
M(3, f"{PREG} — 2b",
  r"Para la misma caja sobre el camión sin fricción que acelera, analiza su movimiento "
  r"según las leyes de Newton, visto por Jim, que viaja en el camión.",
  r"Jim ve que la caja acelera hacia atrás sin que nada la empuje: en su marco, que acelera, "
  r"las leyes de Newton no se cumplen. Es un marco de referencia no inercial.")
M(4, f"{PREG} — 3",
  r"Si la aceleración de un objeto es cero, ¿significa que no actúan fuerzas sobre él? "
  r"Explica.",
  r"No: significa que la fuerza neta es cero. Pueden actuar varias fuerzas que se anulan, "
  r"como el peso y la fuerza normal sobre un libro que descansa en una mesa.")
M(5, f"{PREG} — 4",
  r"Si un objeto se mueve, ¿es posible que la fuerza neta sobre él sea cero?",
  r"Sí: si se mueve en línea recta con rapidez constante (primera ley), como un carro a "
  r"velocidad constante en una recta.")
M(6, f"{PREG} — 5",
  r"Sobre un objeto actúa una sola fuerza. ¿Puede tener aceleración cero? ¿Puede tener "
  r"velocidad cero? Explica.",
  r"Aceleración cero, no: la fuerza neta no es cero, así que $a = F/m \ne 0$. Velocidad cero, "
  r"sí, en un instante: una pelota lanzada hacia arriba (solo actúa el peso) tiene $v = 0$ en "
  r"el punto más alto.")
M(7, f"{PREG} — 6a",
  r"Cuando una pelota de golf se deja caer al pavimento, rebota. ¿Es necesaria una fuerza "
  r"para hacerla rebotar?",
  r"Sí: su velocidad cambia de hacia abajo a hacia arriba, lo que exige una aceleración y, "
  r"por tanto, una fuerza neta hacia arriba.")
M(8, f"{PREG} — 6b",
  r"Si es necesaria una fuerza para que la pelota de golf rebote, ¿qué es lo que la ejerce?",
  r"El pavimento: durante el choque, la pelota se deforma y el suelo la empuja hacia arriba "
  r"con una fuerza mucho mayor que su peso.")
M(9, f"{PREG} — 7",
  r"Si intentas caminar sobre un tronco que flota en un lago, ¿por qué el tronco se mueve en "
  r"dirección opuesta?",
  r"Por la tercera ley: para avanzar empujas el tronco hacia atrás con los pies y el tronco "
  r"te empuja hacia adelante. Como flota casi sin fricción, esa fuerza sobre él lo mueve "
  r"hacia atrás.")
M(10, f"{PREG} — 8",
  r"¿Por qué podrías lastimarte el pie si pateas un escritorio pesado o una pared?",
  r"Por la tercera ley el escritorio ejerce sobre el pie una fuerza igual y opuesta a la del "
  r"pie. Como el escritorio casi no se mueve, el pie se detiene en muy poco tiempo: la "
  r"desaceleración y la fuerza sobre el pie son muy grandes.")
M(11, f"{PREG} — 9a",
  r"Cuando corres y quieres detenerte rápido, debes desacelerar mucho. ¿Cuál es el origen "
  r"de la fuerza que te detiene?",
  r"La fricción del suelo sobre tus pies, dirigida hacia atrás (tercera ley: tus pies empujan "
  r"el suelo hacia adelante).")
M(12, f"{PREG} — 9b",
  r"Estima, con tu experiencia, la desaceleración máxima de una persona que corre a su "
  r"velocidad máxima y quiere detenerse.",
  r"Una persona que corre a unos 8 m/s tarda del orden de 2 s en detenerse: "
  r"$a \approx 8/2 = 4\ \mathrm{m/s^2}$, es decir, entre 3 y 6 $\mathrm{m/s^2}$ (unos "
  r"$\num{0,5}\,g$). Se acepta cualquier estimación razonada.", tipo="contexto")
M(13, f"{PREG} — 10a",
  r"¿Por qué empujas los pedales de una bicicleta con más fuerza al arrancar que cuando va "
  r"con rapidez constante?",
  r"Al arrancar hay que acelerar la bicicleta (fuerza neta distinta de cero); con rapidez "
  r"constante solo hay que equilibrar la fricción y la resistencia del aire.")
M(14, f"{PREG} — 10b",
  r"¿Por qué hay que pedalear cuando la bicicleta rueda con rapidez constante?",
  r"Para compensar la fricción y la resistencia del aire, de modo que la fuerza neta sea "
  r"cero; si dejas de pedalear, esas fuerzas la frenan.")
M(15, f"{PREG} — 11",
  r"Un padre y su hija pequeña, en reposo sobre patines en el hielo, se empujan mutuamente y "
  r"se mueven en direcciones opuestas. ¿Quién tendrá mayor velocidad final?",
  r"La hija: las fuerzas que se ejercen son iguales y opuestas (tercera ley) y actúan el "
  r"mismo tiempo, pero ella tiene menos masa, así que su aceleración y su velocidad final "
  r"son mayores.")
M(16, f"{PREG} — 12", tipo="seleccion",
  enunciado=r"Estás parado sobre una caja de cartón que apenas logra sostenerte. ¿Qué le "
            r"pasaría a la caja si saltaras hacia arriba?" +
            op("Se colapsaría.", "No se vería afectada.", "Se elevaría un poco.",
               "Se movería lateralmente."),
  respuesta=r"a) Se colapsaría: para saltar tienes que empujar la caja hacia abajo con una "
            r"fuerza mayor que tu peso (así ella te empuja hacia arriba con más que tu peso), "
            r"y la caja solo aguanta tu peso.")
M(17, f"{PREG} — 13", dificultad=2,
  enunciado=r"Una piedra cuelga del techo por un hilo delgado y otro trozo del mismo hilo "
            r"cuelga por debajo de la piedra. Si alguien da un jalón fuerte al hilo de abajo, "
            r"¿dónde es más probable que se rompa: debajo o arriba de la piedra? ¿Y si el "
            r"jalón es lento y constante? Explica.",
  respuesta=r"Con un jalón brusco se rompe el hilo de abajo: por su inercia la piedra casi no "
            r"alcanza a moverse, así que el hilo de arriba casi no siente el jalón. Con un "
            r"jalón lento se rompe el de arriba, que soporta el peso de la piedra más la "
            r"fuerza del jalón.")
M(18, f"{PREG} — 14",
  r"La fuerza de gravedad sobre una roca de 2 kg es el doble que sobre una de 1 kg. ¿Por qué "
  r"la roca más pesada no cae más rápido?",
  r"Porque también tiene el doble de masa (el doble de inercia): $a = F/m = 2mg/2m = g$, "
  r"igual para las dos.")
M(19, f"{PREG} — 15a",
  r"¿Una báscula de resorte calibrada en la Tierra en libras (unidad de fuerza) daría "
  r"resultados correctos en la Luna?",
  r"Sí: la báscula de resorte mide fuerza, así que marcaría correctamente el peso en la "
  r"Luna (unas 6 veces menor que en la Tierra).")
M(20, f"{PREG} — 15b",
  r"¿Una báscula de resorte calibrada en la Tierra en kilogramos daría resultados correctos "
  r"en la Luna?",
  r"No: la escala en kilogramos supone $m = F/\num{9,8}$; en la Luna la fuerza es unas 6 "
  r"veces menor, así que marcaría una masa unas 6 veces menor que la real.")
M(21, f"{PREG} — 16", tipo="seleccion",
  enunciado=r"Jalas una caja con una fuerza constante a lo largo de una mesa sin fricción, "
            r"con una cuerda horizontal. Si ahora jalas con la misma fuerza pero formando un "
            r"ángulo con la horizontal (con la caja todavía sobre la mesa), la aceleración "
            r"de la caja:" + op("permanece igual.", "aumenta.", "disminuye."),
  respuesta=r"c) Disminuye: solo la componente horizontal $F\cos\theta < F$ acelera la caja.")
M(22, f"{PREG} — 17",
  r"Un objeto que cae libremente siente la fuerza $mg$ que ejerce la Tierra y, por la "
  r"tercera ley, ejerce sobre la Tierra una fuerza igual y opuesta. ¿La Tierra se mueve?",
  r"Sí, pero su aceleración $a = mg/M_T$ es tan pequeña (la masa de la Tierra es "
  r"$\approx \num{6e24}$ kg) que es imposible notarla.")
M(23, f"{PREG} — 18",
  r"Compara la fuerza necesaria para levantar un objeto de 10 kg en la Luna con la "
  r"necesaria en la Tierra. Compara la fuerza necesaria para lanzar horizontalmente un "
  r"objeto de 2 kg con una rapidez dada en la Luna y en la Tierra.",
  r"Levantarlo en la Luna requiere unas 6 veces menos fuerza, porque su peso es 6 veces "
  r"menor. Lanzarlo horizontalmente con la misma rapidez requiere la misma fuerza: acelerarlo "
  r"depende de su masa, que es igual en ambos lugares.")
M(24, f"{PREG} — 19", tipo="seleccion",
  enunciado=r"¿Cuál de los siguientes pesa aproximadamente 1 N?" +
            op("Una manzana.", "Un mosquito.", "Un libro de física.", "Tú."),
  respuesta=r"a) Una manzana: tiene unos 100 g, y $\num{0,1}\ \text{kg} \times \num{9,8}\ "
            r"\mathrm{m/s^2} \approx 1$ N.")
M(25, f"{PREG} — 20",
  r"En el juego de halar la cuerda, por la tercera ley cada equipo hala al otro con una "
  r"fuerza de igual magnitud. ¿Qué determina entonces qué equipo gana?",
  r"La fricción que el suelo ejerce sobre los pies de cada equipo: gana el equipo que "
  r"empuja el suelo con más fuerza (y logra más fricción sin resbalar), porque la fuerza "
  r"neta sobre el sistema de los dos equipos apunta hacia su lado.")
M(26, f"{PREG} — 21",
  r"Cuando estás parado sobre el suelo, ¿qué tan grande es la fuerza que el suelo ejerce "
  r"sobre ti? ¿Por qué no te levanta?",
  r"Es igual a tu peso, $mg$ (la fuerza normal). No te levanta porque se equilibra con el "
  r"peso: la fuerza neta sobre ti es cero.")
M(27, f"{PREG} — 22",
  r"En un choque por detrás, los ocupantes del carro golpeado sufren lesiones de cuello. "
  r"Explica por qué la cabeza parece lanzada hacia atrás. ¿Es así realmente?",
  r"El carro y el asiento aceleran de golpe hacia adelante y empujan el torso; la cabeza, "
  r"por inercia, tiende a quedarse donde estaba. Parece que se va hacia atrás, pero en "
  r"realidad es el cuerpo el que se adelanta.")
for _n, _lit, _preg, _resp in [(28, "a", "su magnitud", "40 N."),
                               (29, "b", "su sentido", "Hacia abajo."),
                               (30, "c", "sobre qué objeto se ejerce", "Sobre la mano de Mary."),
                               (31, "d", "qué objeto la ejerce", "La bolsa de provisiones.")]:
    M(_n, f"{PREG} — 23{_lit}",
      rf"Mary ejerce una fuerza de 40 N hacia arriba para sostener una bolsa de provisiones. "
      rf"Describe la fuerza de «reacción» (tercera ley de Newton) indicando {_preg}.", _resp)

# ---------- Problemas: leyes de Newton, fuerza gravitacional, fuerza normal ----------


@E(32, f"{PROB} — 1",
   enunciado=r"¿Qué fuerza se requiere para acelerar a un niño sobre un trineo (masa total "
             r"55 kg) a $\num{1,4}\ \mathrm{m/s^2}$?",
   respuesta=r"$F = ma = 55 \times \num{1,4} = 77$ N.")
def _():
    aprox(55 * kg * 1.4 * m / s**2, 77, N, rel=1e-9)


@E(33, f"{PROB} — 2",
   enunciado=r"Una fuerza neta de 265 N acelera a una persona en bicicleta a "
             r"$\num{2,30}\ \mathrm{m/s^2}$. ¿Cuál es la masa de la persona con la bicicleta?",
   respuesta=r"$m = F/a = 265/\num{2,30} \approx 115$ kg.")
def _():
    aprox(265 * N / (2.30 * m / s**2), 115.2, kg, rel=0.001)


for _n, _lit, _donde, _gl, _w in [(34, "a", "en la Tierra", 9.8, 666.4),
                                  (35, "b", r"en la Luna ($g = \num{1,7}\ \mathrm{m/s^2}$)",
                                   1.7, 115.6),
                                  (36, "c", r"en Marte ($g = \num{3,7}\ \mathrm{m/s^2}$)",
                                   3.7, 251.6)]:
    @E(_n, f"{PROB} — 3{_lit}",
       enunciado=rf"¿Cuál es el peso de un astronauta de 68 kg {_donde}?",
       respuesta=rf"$W = mg = 68 \times \num{{{str(_gl).replace('.', ',')}}} \approx "
                 rf"\num{{{str(round(_w)).replace('.', ',')}}}$ N.")
    def _(gl=_gl, w=_w):
        aprox(68 * kg * gl * m / s**2, w, N, rel=1e-6)

M(37, f"{PROB} — 3d",
  r"¿Cuál es el peso de un astronauta de 68 kg en el espacio exterior, lejos de todo "
  r"planeta, viajando con velocidad constante?",
  r"Prácticamente cero: lejos de cualquier astro no hay atracción gravitacional apreciable "
  r"(su masa sigue siendo 68 kg).")


@E(38, f"{PROB} — 4",
   enunciado=r"¿Cuánta tensión debe resistir una cuerda que se usa para acelerar "
             r"horizontalmente un automóvil de 1210 kg a $\num{1,20}\ \mathrm{m/s^2}$ sobre "
             r"una superficie sin fricción?",
   respuesta=r"$T = ma = 1210 \times \num{1,20} \approx \num{1,45e3}$ N.")
def _():
    aprox(1210 * kg * 1.20 * m / s**2, 1452, N, rel=1e-6)


@E(39, f"{PROB} — 5", tipo="contexto", dificultad=2,
   enunciado=r"Superman debe detener en 150 m un tren que viaja a 120 km/h para evitar que "
             r"choque con un automóvil detenido en la vía. Si la masa del tren es "
             r"$\num{3,6e5}$ kg, ¿cuánta fuerza debe ejercer? Compárala con el peso del tren "
             r"(en porcentaje). ¿Cuánta fuerza ejerce el tren sobre Superman?",
   respuesta=r"$a = \dfrac{v^2}{2x} = \dfrac{(\num{33,3})^2}{300} \approx \num{3,70}\ "
             r"\mathrm{m/s^2}$; $F = ma \approx \num{1,3e6}$ N, un 38\,\% del peso del tren "
             r"($\num{3,5e6}$ N). Por la tercera ley, el tren ejerce sobre Superman la misma "
             r"fuerza, $\num{1,3e6}$ N, en sentido opuesto.")
def _():
    a = (120 * km / h)**2 / (2 * 150 * m)
    F = 3.6e5 * kg * a
    aprox(F, 1.33e6, N, rel=0.003)
    assert abs(val(F / (3.6e5 * kg * G), 1) * 100 - 38) < 0.5


@E(40, f"{PROB} — 6",
   enunciado=r"¿Qué fuerza promedio se requiere para detener en $\num{8,0}$ s un automóvil de "
             r"950 kg que viaja a 95 km/h?",
   respuesta=r"$a = \dfrac{\num{26,4}\ \mathrm{m/s}}{\num{8,0}\ \text{s}} \approx \num{3,3}\ "
             r"\mathrm{m/s^2}$; $F = ma \approx \num{3,1e3}$ N (opuesta al movimiento).")
def _():
    aprox(950 * kg * (95 * km / h) / (8.0 * s), 3134, N, rel=0.002)


@E(41, f"{PROB} — 7", tipo="contexto",
   enunciado=r"Estima la fuerza promedio que ejerce un lanzador de bala sobre una bala de "
             r"$\num{7,0}$ kg, si la mueve a lo largo de $\num{2,8}$ m y la suelta a 13 m/s.",
   respuesta=r"$a = \dfrac{13^2}{2(\num{2,8})} \approx \num{30,2}\ \mathrm{m/s^2}$; "
             r"$F = ma \approx 211$ N ($\approx \num{2,1e2}$ N).")
def _():
    aprox(7.0 * kg * (13 * m / s)**2 / (2 * 2.8 * m), 211, N, rel=0.003)


@E(42, f"{PROB} — 8", tipo="contexto",
   enunciado=r"Una pelota de béisbol de $\num{0,140}$ kg que viaja a $\num{35,0}$ m/s golpea "
             r"el guante del receptor, que se mueve $\num{11,0}$ cm hacia atrás al detenerla. "
             r"¿Cuál fue la fuerza promedio de la pelota sobre el guante?",
   respuesta=r"$a = \dfrac{35^2}{2(\num{0,110})} \approx \num{5,57e3}\ \mathrm{m/s^2}$; "
             r"$F = ma \approx 780$ N ($\approx \num{7,8e2}$ N).")
def _():
    aprox(0.140 * kg * (35.0 * m / s)**2 / (2 * 11.0 * centimeter), 780, N, rel=0.003)


@E(43, f"{PROB} — 9", tipo="contexto", dificultad=2,
   enunciado=r"Un pescador saca verticalmente un pez del agua con una aceleración de "
             r"$\num{2,5}\ \mathrm{m/s^2}$, usando un cordel muy ligero que aguanta una "
             r"tensión máxima de 18 N antes de romperse. El cordel se rompe. ¿Qué puedes "
             r"decir de la masa del pez?",
   respuesta=r"$T - mg = ma \Rightarrow m = \dfrac{T}{g + a} = \dfrac{18}{\num{12,3}} \approx "
             r"\num{1,5}$ kg es la masa con la que el cordel quedaría justo al límite; como se "
             r"rompió, el pez tenía más de $\num{1,5}$ kg.")
def _():
    aprox(18 * N / (G + 2.5 * m / s**2), 1.46, kg, rel=0.003)


@E(44, f"{PROB} — 10a",
   enunciado=r"Una caja de $\num{20,0}$ kg descansa sobre una mesa. ¿Cuál es su peso y cuál "
             r"la fuerza normal que actúa sobre ella?",
   respuesta=r"$W = mg = 196$ N hacia abajo; $N = 196$ N hacia arriba (está en equilibrio).")
def _():
    aprox(20.0 * kg * G, 196, N, rel=1e-9)


@E(45, f"{PROB} — 10b",
   enunciado=r"Sobre la caja de $\num{20,0}$ kg se coloca una caja de $\num{10,0}$ kg. "
             r"Determina la fuerza normal que ejerce la mesa sobre la caja de "
             r"$\num{20,0}$ kg y la que ejerce la caja de $\num{20,0}$ kg sobre la de "
             r"$\num{10,0}$ kg.",
   respuesta=r"La mesa sobre la caja de abajo: $(20 + 10)(\num{9,8}) = 294$ N. La caja de "
             r"abajo sobre la de arriba: $10(\num{9,8}) = 98$ N.")
def _():
    aprox(30.0 * kg * G, 294, N, rel=1e-9)
    aprox(10.0 * kg * G, 98, N, rel=1e-9)


@E(46, f"{PROB} — 11",
   enunciado=r"¿Qué fuerza promedio se necesita para acelerar una bala de $\num{9,20}$ g desde "
             r"el reposo hasta 125 m/s en $\num{0,800}$ m a lo largo del cañón de un fusil?",
   respuesta=r"$a = \dfrac{125^2}{2(\num{0,800})} \approx \num{9,77e3}\ \mathrm{m/s^2}$; "
             r"$F = ma \approx \num{89,8}$ N.")
def _():
    aprox(9.20 * gram * (125 * m / s)**2 / (2 * 0.800 * m), 89.8, N, rel=0.002)


@E(47, f"{PROB} — 12",
   enunciado=r"¿Cuánta tensión debe resistir una cuerda que se usa para acelerar un vehículo de "
             r"1200 kg verticalmente hacia arriba a $\num{0,70}\ \mathrm{m/s^2}$?",
   respuesta=r"$T = m(g + a) = 1200(\num{9,8} + \num{0,70}) = \num{1,26e4}$ N.")
def _():
    aprox(1200 * kg * (G + 0.70 * m / s**2), 12600, N, rel=1e-9)


@E(48, f"{PROB} — 13",
   enunciado=r"Una cubeta de $\num{14,0}$ kg se baja verticalmente con una cuerda cuya tensión, "
             r"en un instante dado, es de 163 N. ¿Cuál es la aceleración de la cubeta? ¿Es "
             r"hacia arriba o hacia abajo?",
   respuesta=r"$a = \dfrac{T - mg}{m} = \dfrac{163 - \num{137,2}}{14} \approx \num{1,84}\ "
             r"\mathrm{m/s^2}$ hacia arriba (la cubeta baja cada vez más despacio).")
def _():
    peso = val(14.0 * kg * G, N)
    a = (163 - peso) * N / (14.0 * kg)
    aprox(a, 1.84, m / s**2, rel=0.003)


@E(49, f"{PROB} — 14", tipo="contexto", dificultad=2,
   enunciado=r"Un automóvil de carreras recorre un cuarto de milla (402 m) en $\num{6,40}$ s "
             r"partiendo del reposo. Suponiendo aceleración constante, ¿cuántas «$g$» siente "
             r"el piloto? Si la masa del piloto y el auto es 535 kg, ¿qué fuerza horizontal "
             r"debe ejercer el camino sobre las llantas?",
   respuesta=r"$a = \dfrac{2x}{t^2} = \dfrac{804}{\num{6,40}^2} \approx \num{19,6}\ "
             r"\mathrm{m/s^2} \approx \num{2,0}\,g$; $F = ma \approx \num{1,05e4}$ N.")
def _():
    a = 2 * 402 * m / (6.40 * s)**2
    assert abs(val(a / G, 1) - 2.0) < 0.01
    aprox(535 * kg * a, 1.05e4, N, rel=0.003)


@E(50, f"{PROB} — 15", tipo="contexto", dificultad=2,
   enunciado=r"Un ladrón de 75 kg quiere escapar por la ventana de un tercer piso con una "
             r"cuerda hecha de sábanas que solo soporta el peso de una masa de 58 kg. ¿Cómo "
             r"podría usar esa cuerda para escapar? Da una respuesta cuantitativa.",
   respuesta=r"Bajando con aceleración hacia abajo, para que la tensión sea menor que su peso: "
             r"$mg - T = ma \Rightarrow a \ge g\left(1 - \dfrac{58}{75}\right) \approx "
             r"\num{2,2}\ \mathrm{m/s^2}$. Debe deslizarse por la cuerda con al menos esa "
             r"aceleración.")
def _():
    a = G - 58 * kg * G / (75 * kg)
    aprox(a, 2.22, m / s**2, rel=0.003)


# ---------- Problemas: uso de las leyes de Newton ----------

for _n, _lit, _w, _r in [(51, "a", 30.0, r"$N = 77 - 30 = 47$ N."),
                         (52, "b", 60.0, r"$N = 77 - 60 = 17$ N."),
                         (53, "c", 90.0, r"$N = 0$: el peso colgado (90 N) es mayor que el de "
                                         r"la caja (77 N), así que la caja se levanta de la "
                                         r"mesa y el sistema acelera.")]:
    @E(_n, f"{PROB} — 16{_lit}", dificultad=2,
       enunciado=rf"Una caja que pesa $\num{{77,0}}$ N descansa sobre una mesa. Una cuerda "
                 rf"atada a la caja sube verticalmente, pasa por una polea y en el otro "
                 rf"extremo cuelga un peso de $\num{{{str(_w).replace('.', ',')}}}$ N. "
                 rf"Determina la fuerza que ejerce la mesa sobre la caja.",
       respuesta=_r)
    def _(w=_w):
        n = max(77.0 - w, 0.0)             # si el peso supera 77 N, la caja deja la mesa
        assert n == {30.0: 47.0, 60.0: 17.0, 90.0: 0.0}[w]

for _n, _lit, _caso, _resp in [
        (54, "a", "justo antes de dejar el suelo al saltar",
         r"El peso $m\vec g$ hacia abajo y la fuerza normal del piso hacia arriba, mayor que el "
         r"peso (por eso acelera hacia arriba)."),
        (55, "b", "mientras está en el aire",
         r"Solo el peso $m\vec g$ hacia abajo (despreciando el aire); no hay ninguna fuerza "
         r"«hacia arriba».")]:
    M(_n, f"{PROB} — 17{_lit}",
      rf"Dibuja el diagrama de cuerpo libre de un jugador de baloncesto {_caso}.", _resp)


@E(56, f"{PROB} — 18", dificultad=2,
   enunciado=r"Una fuerza de 650 N actúa hacia el noroeste. ¿En qué dirección debe actuar una "
             r"segunda fuerza de 650 N para que la resultante apunte hacia el oeste? Ilustra "
             r"con un diagrama de vectores.",
   respuesta=r"Hacia el suroeste ($45^\circ$ al sur del oeste): las componentes norte y sur se "
             r"anulan y la resultante es $2(650)\cos45^\circ \approx 919$ N hacia el oeste.")
def _():
    f1 = (650 * cos(radians(135)), 650 * sin(radians(135)))
    f2 = (650 * cos(radians(225)), 650 * sin(radians(225)))
    rx, ry = f1[0] + f2[0], f1[1] + f2[1]
    assert abs(ry) < 1e-9 and rx < 0
    cerca(hypot(rx, ry), 919, 0.001)


@E(57, f"{PROB} — 19a",
   enunciado=r"Dos cubetas de pintura de $\num{3,2}$ kg cada una cuelgan una debajo de la otra "
             r"mediante dos cuerdas ligeras (la cuerda de arriba sostiene la cubeta superior "
             r"y de esta cuelga la otra). Si están en reposo, ¿cuál es la tensión en cada "
             r"cuerda?",
   respuesta=r"Cuerda inferior: $\num{3,2}(\num{9,8}) \approx \num{31,4}$ N; cuerda superior: "
             r"$\num{6,4}(\num{9,8}) \approx \num{62,7}$ N.")
def _():
    aprox(3.2 * kg * G, 31.36, N, rel=1e-6)
    aprox(6.4 * kg * G, 62.72, N, rel=1e-6)


@E(58, f"{PROB} — 19b",
   enunciado=r"Las dos cubetas de $\num{3,2}$ kg se jalan hacia arriba por la cuerda superior "
             r"con una aceleración de $\num{1,25}\ \mathrm{m/s^2}$. Calcula la tensión en "
             r"cada cuerda.",
   respuesta=r"$T = m(g + a)$: inferior $\num{3,2}(\num{11,05}) \approx \num{35,4}$ N; "
             r"superior $\num{6,4}(\num{11,05}) \approx \num{70,7}$ N.")
def _():
    a = 1.25 * m / s**2
    aprox(3.2 * kg * (G + a), 35.36, N, rel=1e-6)
    aprox(6.4 * kg * (G + a), 70.72, N, rel=1e-6)


@E(59, f"{PROB} — 20", dificultad=3,
   enunciado=r"Ahora las cuerdas que aceleran las cubetas del problema anterior "
             r"($\num{3,2}$ kg cada una, $a = \num{1,25}\ \mathrm{m/s^2}$ hacia arriba) pesan "
             r"$\num{2,0}$ N cada una. Determina la tensión en cada extremo de cada cuerda.",
   respuesta=r"Cada tensión sostiene y acelera todo lo que cuelga por debajo: "
             r"$T = \dfrac{W_{\text{debajo}}}{g}(g + a)$. Cuerda inferior: $\num{35,4}$ N en la "
             r"cubeta de abajo y $\num{37,6}$ N en la de arriba; cuerda superior: "
             r"$\num{73,0}$ N en la cubeta de arriba y $\num{75,2}$ N en el extremo superior.",
   notas="La guía pide «los tres puntos de conexión de la figura»; se dan las tensiones en "
         "los cuatro extremos de las dos cuerdas.")
def _():
    f = (G + 1.25 * m / s**2) / G            # factor (g + a)/g
    wc, wq = 3.2 * kg * G, 2.0 * N
    for w, t in [(wc, 35.4), (wc + wq, 37.6), (2 * wc + wq, 73.0), (2 * wc + 2 * wq, 75.2)]:
        aprox(w * f, t, N, rel=0.002)


@E(60, f"{PROB} — 21", tipo="contexto",
   enunciado=r"Un niño en un trineo llega a la base de una colina a $\num{10,0}$ m/s y luego "
             r"recorre $\num{25,0}$ m por una superficie horizontal hasta detenerse. Si juntos "
             r"tienen una masa de $\num{60,0}$ kg, ¿cuál es la fuerza retardadora promedio en "
             r"el tramo horizontal?",
   respuesta=r"$a = \dfrac{10^2}{2(25)} = \num{2,0}\ \mathrm{m/s^2}$; $F = ma = 120$ N, "
             r"opuesta al movimiento.",
   notas="En la guía: «Su juntos el niño y el trineo…»; se corrige a «Si juntos…».")
def _():
    aprox(60.0 * kg * (10.0 * m / s)**2 / (2 * 25.0 * m), 120, N, rel=1e-9)


@E(61, f"{PROB} — 22", tipo="contexto", dificultad=2,
   enunciado=r"Un adolescente en patineta, con rapidez inicial de $\num{2,0}$ m/s, baja rodando "
             r"casi sin fricción por un plano inclinado recto de 18 m de largo en "
             r"$\num{3,3}$ s. ¿Cuál es el ángulo de inclinación $\theta$ del plano?",
   respuesta=r"$18 = 2(\num{3,3}) + \frac{1}{2}a(\num{3,3})^2 \Rightarrow a \approx "
             r"\num{2,09}\ \mathrm{m/s^2}$; como $a = g\operatorname{sen}\theta$, "
             r"$\theta = \arcsen(\num{2,09}/\num{9,8}) \approx 12^\circ$.")
def _():
    a = sp.solve(sp.Eq(18, 2.0 * 3.3 + sp.Symbol("a") * 3.3**2 / 2))[0]
    cerca(float(a), 2.094, 0.002)
    cerca(degrees(asin(float(a) / g)), 12.3, 0.005)


@E(62, f"{PROB} — 23a",
   enunciado=r"Un bloque de masa $m = \num{7,0}$ kg está sobre un plano liso (sin fricción) "
             r"inclinado $\num{22,0}^\circ$ respecto a la horizontal. Determina la aceleración "
             r"del bloque al deslizarse por el plano.",
   respuesta=r"$a = g\operatorname{sen}\theta = \num{9,8}\operatorname{sen}22^\circ \approx "
             r"\num{3,7}\ \mathrm{m/s^2}$, hacia abajo del plano (no depende de la masa).")
def _():
    aprox(G * sin(radians(22.0)), 3.67, m / s**2, rel=0.002)


@E(63, f"{PROB} — 23b",
   enunciado=r"Si el bloque anterior (plano liso a $\num{22,0}^\circ$) parte del reposo a "
             r"$\num{12,0}$ m de la base, medidos a lo largo del plano, ¿con qué rapidez llega "
             r"al fondo?",
   respuesta=r"$v = \sqrt{2ax} = \sqrt{2(\num{3,67})(12)} \approx \num{9,4}$ m/s.")
def _():
    v2 = 2 * G * sin(radians(22.0)) * 12.0 * m
    cerca(sqrt(val(v2, m**2 / s**2)), 9.39, 0.002)


@E(64, f"{PROB} — 24a",
   enunciado=r"A un bloque se le da una rapidez inicial de $\num{4,5}$ m/s hacia arriba de un "
             r"plano liso inclinado $22^\circ$. ¿Qué distancia sube por el plano?",
   respuesta=r"La desaceleración es $g\operatorname{sen}22^\circ \approx \num{3,67}\ "
             r"\mathrm{m/s^2}$: $x = \dfrac{\num{4,5}^2}{2(\num{3,67})} \approx \num{2,8}$ m.")
def _():
    aprox((4.5 * m / s)**2 / (2 * G * sin(radians(22))), 2.76, m, rel=0.003)


@E(65, f"{PROB} — 24b",
   enunciado=r"Para el bloque lanzado a $\num{4,5}$ m/s hacia arriba del plano liso de "
             r"$22^\circ$, ¿cuánto tiempo pasa antes de que vuelva a su punto de partida? "
             r"Ignora la fricción.",
   respuesta=r"Sube en $\num{4,5}/\num{3,67} \approx \num{1,23}$ s y baja en el mismo tiempo: "
             r"$t \approx \num{2,5}$ s.")
def _():
    aprox(2 * 4.5 * m / s / (G * sin(radians(22))), 2.45, s, rel=0.003)


M(66, f"{PROB} — 25a", dificultad=2,
  enunciado=r"Un bloque de masa $m_A$ está sobre una superficie horizontal lisa y está unido "
            r"por una cuerda delgada, que pasa por una polea, a un segundo bloque de masa "
            r"$m_B$ que cuelga verticalmente. Dibuja el diagrama de cuerpo libre de cada "
            r"bloque, con el peso, la tensión de la cuerda y las fuerzas normales.",
  respuesta=r"Bloque A: peso $m_A g$ hacia abajo, normal $N = m_A g$ hacia arriba y tensión "
            r"$T$ horizontal hacia la polea. Bloque B: peso $m_B g$ hacia abajo y tensión $T$ "
            r"hacia arriba (no tiene fuerza normal).")


@E(67, f"{PROB} — 25b", dificultad=3,
   enunciado=r"Para el sistema anterior (bloque $m_A$ en una mesa lisa unido por una cuerda "
             r"que pasa por una polea a un bloque $m_B$ que cuelga), aplica la segunda ley de "
             r"Newton para hallar la aceleración del sistema y la tensión de la cuerda. "
             r"Desprecia la fricción y las masas de la polea y de la cuerda.",
   respuesta=r"A: $T = m_A a$; B: $m_B g - T = m_B a$. Sumando: "
             r"$a = \dfrac{m_B}{m_A + m_B}\,g$ y $T = \dfrac{m_A m_B}{m_A + m_B}\,g$.")
def _():
    ma, mb, gg, a, T = sp.symbols("m_A m_B g a T", positive=True)
    sol = sp.solve([sp.Eq(T, ma * a), sp.Eq(mb * gg - T, mb * a)], [a, T], dict=True)[0]
    assert sp.simplify(sol[a] - mb * gg / (ma + mb)) == 0
    assert sp.simplify(sol[T] - ma * mb * gg / (ma + mb)) == 0
