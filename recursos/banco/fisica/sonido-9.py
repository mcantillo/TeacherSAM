"""Banco de ejercicios — Física 9° — Sonido.
Fuente: Guía de Apoyo de Física 9° (ondas, sonido y luz), Capítulo 2 «Sonido»: Preguntas de
repaso, Ejercicios y Problemas. Se lee en
recursos/fisica/Guías pedagógicas Física/markdown/09 - Guia_de_Apoyo_Conceptos_ondas_de_sonido_y_de_luz_grado_9_fisica.md
Alineación: Estándares 8°–9° (dba/naturales/estandares-fisica.md) — relaciones entre frecuencia,
amplitud, velocidad de propagación y longitud de onda en ondas mecánicas; ondas estacionarias e
instrumentos musicales. Los problemas de eco (distancia = rapidez × tiempo) también sirven para
el DBA 1 de 9° (movimiento), y así se marcan.
No incluidos: los «Examínate», la «Práctica de física» (parrilla colgada de los oídos) y los
Proyectos 1–2 (actividades prácticas).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/fisica/sonido-9.py
"""
from sympy import Rational as Q, simplify, solve, symbols
from sympy.physics.units import convert_to, hertz, hour, kelvin, kilogram, meter, minute, second

from ejercicios import ejercicio, ejercicio_manual

P = "sonido-9"
GUIA = "Guía de Apoyo Física 9° (ondas, sonido y luz), Cap. 2 Sonido"
COMUN = dict(tema="sonido", grados=[9], dba=[])
ECO = dict(tema="sonido", grados=[9], dba=["naturales-9-1"])
C_LUZ = 3 * 10**8 * meter / second
V_SON = 340 * meter / second              # aire a unos 20 °C (valor de la guía)
V_MAR = 1530 * meter / second             # agua de mar (valor de la guía)


def fuente(seccion, lit):
    return f"{GUIA}, {seccion} — {lit}"


def cerca(a, b, tol=Q(5, 1000)):
    """a y b son cantidades de la misma dimensión; iguales salvo el redondeo tol (relativo)."""
    base = [meter, second, kilogram, kelvin]
    r = simplify(convert_to(a, base) / convert_to(b, base))
    assert r.is_number, f"dimensiones distintas: {a} / {b}"
    assert abs(float(r) - 1) <= tol, f"{float(r)}"


def manuales(seccion, filas, **extra):
    for n, lit, enunciado, respuesta, *notas in filas:
        meta = {**COMUN, **extra}
        if notas:
            meta["notas"] = notas[0]
        ejercicio_manual(id=f"{P}-{n:03d}", fuente=fuente(seccion, lit),
                         enunciado=enunciado, respuesta=respuesta, **meta)


# ---------------------------------------------------------------- Preguntas de repaso
REPASO = "Preguntas de repaso"
manuales(REPASO, [
    (1, "1", r"¿Cómo suele definir un físico el sonido?",
     r"Como una forma de energía que existe aunque nadie la escuche: una onda mecánica "
     r"(longitudinal en el aire) que se propaga por un medio material."),
    (2, "2", r"¿Cuál es la relación entre frecuencia y tono?",
     r"El tono (la altura) es la impresión que produce la frecuencia: a mayor frecuencia, sonido "
     r"más agudo (alto); a menor frecuencia, más grave (bajo)."),
    (3, "3", r"En una persona joven, ¿cuál es el intervalo promedio de audición?",
     r"De unos $20\,\text{Hz}$ a unos $\num{20000}\,\text{Hz}$."),
    (4, "4", r"Describe la diferencia entre las ondas sonoras infrasónicas y las ultrasónicas.",
     r"Las infrasónicas tienen frecuencias menores que $20\,\text{Hz}$ y las ultrasónicas "
     r"mayores que $\num{20000}\,\text{Hz}$; el oído humano no percibe ninguna de las dos."),
    (5, "5", r"Describe la diferencia entre una compresión y un enrarecimiento.",
     r"En una compresión las moléculas del medio están más juntas (mayor presión y densidad); en "
     r"un enrarecimiento (rarefacción) están más separadas (menor presión y densidad)."),
    (6, "6", r"¿Las compresiones y los enrarecimientos se propagan en la misma dirección que una "
             r"onda? Proporciona evidencias para apoyar tu respuesta.",
     r"Sí, ambos viajan en la misma dirección y con la misma rapidez, alejándose de la fuente. "
     r"Evidencia: al abrir la puerta (compresión) o al cerrarla (enrarecimiento), la cortina de "
     r"la ventana del otro extremo del cuarto se mueve después, en los dos casos; y en el tubo "
     r"frente al diapasón, compresiones y enrarecimientos salen alternados hacia el mismo lado."),
    (7, "7", r"En relación con los sólidos y los líquidos, ¿qué lugar ocupa el aire como "
             r"conductor del sonido?",
     r"Es el peor conductor: el sonido viaja mejor y más rápido en líquidos y sólidos."),
    (8, "8", r"¿Por qué el sonido no se propaga por el vacío?",
     r"Porque necesita un medio material que se comprima y se expanda; en el vacío no hay nada "
     r"que vibre."),
    (9, "9", r"¿De qué factores depende la rapidez del sonido? ¿Cuáles son algunos factores de "
             r"los cuales no depende la rapidez del sonido?",
     r"Depende del medio y de sus condiciones: temperatura, humedad y viento. No depende de la "
     r"intensidad (volumen) ni de la frecuencia del sonido."),
    (10, "10", r"¿Cuál es la rapidez del sonido en el aire seco a $0\,^{\circ}\text{C}$?",
     r"Aproximadamente $330\,\text{m/s}$ (unos $\num{1200}\,\text{km/h}$)."),
    (11, "11", r"¿El sonido se propaga con más rapidez en el aire cálido que en el aire frío? "
               r"Defiende tu respuesta.",
     r"Sí. En el aire caliente las moléculas se mueven más rápido y chocan más a menudo, así que "
     r"transmiten el impulso en menos tiempo: la rapidez aumenta unos $\num{0,6}\,\text{m/s}$ "
     r"por cada grado Celsius."),
    (12, "12", r"¿Qué es el eco?", r"La reflexión del sonido."),
    (13, "13", r"¿Qué es una reverberación?",
     r"La persistencia de un sonido debida a reflexiones múltiples en paredes, techo y piso."),
    (14, "14", r"¿Cuál es la causa de la refracción?",
     r"Que distintas partes del frente de onda viajan con rapideces distintas (por el viento o "
     r"por capas de aire a diferente temperatura)."),
    (15, "15", r"¿El sonido tiende a desviarse hacia arriba o hacia abajo, cuando su rapidez es "
               r"menor cerca del suelo?",
     r"Hacia abajo, hacia el suelo (como en las noches frías), y por eso se oye a mayores "
     r"distancias."),
    (16, "16", r"¿Por qué a veces el sonido se refracta bajo el agua?",
     r"Porque la rapidez del sonido en el agua cambia con la temperatura, y en el mar hay capas "
     r"de agua a distintas temperaturas."),
    (17, "17", r"¿Qué suele ser mayor, la energía en el sonido ordinario o la energía en la luz "
               r"ordinaria?",
     r"La energía de la luz: la del sonido es extremadamente pequeña."),
    (18, "18", r"A final de cuentas, ¿cuál es el destino de la energía del sonido en el aire?",
     r"Se disipa como energía térmica (energía interna) del aire."),
    (19, "19", r"¿Por qué suena más fuerte un diapasón cuando se golpea sujetándolo contra una "
               r"mesa?",
     r"Porque obliga a la mesa a vibrar con él (vibración forzada), y la mesa, con su gran "
     r"superficie, pone en movimiento mucho más aire."),
    (20, "20", r"Menciona al menos dos factores que determinen la frecuencia natural de un "
               r"objeto.",
     r"Su elasticidad (el material) y su forma (y tamaño)."),
    (21, "21", r"¿Qué tienen que ver las vibraciones forzadas con la resonancia?",
     r"La resonancia es una vibración forzada en la que la frecuencia de la fuerza coincide con "
     r"la frecuencia natural del objeto; entonces la amplitud crece mucho."),
    (22, "22", r"Cuando escuchas tu radio, ¿por qué sólo escuchas una estación a la vez, y no "
               r"todas al mismo tiempo?",
     r"Porque al sintonizar se ajusta la frecuencia natural del circuito del radio para que "
     r"resuene solo con la frecuencia de una estación."),
    (23, "23", r"¿Cómo la resonancia generada por el viento afectó el puente Tacoma Narrows, en "
               r"Washington, en 1940?",
     r"El viento produjo una fuerza que coincidió con la frecuencia natural del puente; la "
     r"amplitud de la vibración creció sin parar hasta que el puente se desplomó."),
    (24, "24", r"¿Cuándo es posible que una onda anule a otra?",
     r"Cuando llegan al mismo lugar con igual amplitud y desfasadas media longitud de onda: la "
     r"cresta (compresión) de una coincide con el valle (enrarecimiento) de la otra."),
    (25, "25", r"¿Qué clase de ondas pueden mostrar interferencia?",
     r"Todas, transversales y longitudinales."),
    (26, "26", r"¿Qué fenómeno físico es básico en la producción de pulsaciones?",
     r"La interferencia."),
], tipo="conceptual", dificultad=1)


@ejercicio(id=f"{P}-027", tipo="calculo", dificultad=1, fuente=fuente(REPASO, "27"),
           enunciado=r"¿Qué frecuencia de pulsación se producirá cuando se hacen sonar al unísono "
                     r"fuentes de $370\,\text{Hz}$ y $374\,\text{Hz}$?",
           respuesta=r"$374 - 370 = 4\,\text{Hz}$.", **COMUN)
def _():
    assert 374 * hertz - 370 * hertz == 4 * hertz


manuales(REPASO, [
    (28, "28", r"¿En qué difiere una onda de radio de una onda sonora?",
     r"La onda de radio es electromagnética: no necesita medio, viaja a la rapidez de la luz "
     r"($\num{3e8}\,\text{m/s}$) y tiene frecuencias muchísimo mayores. La onda sonora es "
     r"mecánica: necesita un medio material y en el aire viaja a unos $340\,\text{m/s}$."),
], tipo="conceptual", dificultad=1)

# ---------------------------------------------------------------- Ejercicios
EJ = "Ejercicios"
manuales(EJ, [
    (29, "1", r"¿Por qué no escuchas el sonido de los fuegos artificiales distantes, sino hasta "
              r"después de que los viste?",
     r"Porque la luz llega casi al instante y el sonido, a unos $340\,\text{m/s}$, tarda "
     r"bastante más en recorrer la misma distancia."),
    (30, "2", r"Si la Luna explotara, ¿por qué no escucharíamos la detonación?",
     r"Porque entre la Luna y la Tierra hay vacío y el sonido no se propaga sin un medio."),
    (31, "3", r"¿Por qué sería vano el intento de detectar sonidos de otros planetas, incluso si "
              r"se contara con los mejores detectores de sonido?",
     r"Porque el espacio entre los planetas es prácticamente vacío: el sonido no puede viajar "
     r"desde allá hasta la Tierra."),
    (32, "4", r"Lanza una piedra al agua inmóvil y se formarán círculos concéntricos. ¿Qué forma "
              r"tendrán las ondas, si la piedra se lanza cuando el agua fluye uniformemente?",
     r"También serán círculos, pero sus centros se desplazarán junto con la corriente."),
    (33, "5", r"¿Por qué zumban las abejas al volar?",
     r"Porque baten las alas cientos de veces por segundo; esa vibración produce ondas sonoras "
     r"con frecuencias que el oído percibe."),
], tipo="conceptual", dificultad=2)


@ejercicio(id=f"{P}-034", tipo="contexto", dificultad=2, fuente=fuente(EJ, "6"),
           enunciado=r"Un gato puede oír frecuencias hasta de $\num{70000}\,\text{Hz}$. Los "
                     r"murciélagos emiten y reciben chillidos con ultra alta frecuencia, hasta de "
                     r"$\num{120000}\,\text{Hz}$. ¿Quiénes oyen sonidos de longitudes de onda más "
                     r"cortas, los gatos o los murciélagos?",
           respuesta=r"Los murciélagos: con la misma rapidez del sonido, mayor frecuencia implica "
                     r"menor longitud de onda. En el aire, $\lambda \approx \num{2,8}\,\text{mm}$ "
                     r"para el murciélago y $\approx \num{4,9}\,\text{mm}$ para el gato.", **COMUN)
def _():
    murcielago, gato = V_SON / (120000 * hertz), V_SON / (70000 * hertz)
    cerca(murcielago, Q(28, 10) / 1000 * meter, tol=0.02)
    cerca(gato, Q(49, 10) / 1000 * meter, tol=0.02)
    assert convert_to(murcielago, meter) < convert_to(gato, meter)


manuales(EJ, [
    (35, "7", r"¿Qué quiere decir que una estación de radio está «en el \num{101,1} de su radio "
              r"FM»?",
     r"Que transmite con una onda portadora de $\num{101,1}\,\text{MHz}$, es decir, "
     r"\num{101100000} vibraciones por segundo, en la banda de frecuencia modulada."),
], tipo="conceptual", dificultad=1)


@ejercicio(id=f"{P}-036", tipo="conceptual", dificultad=2, fuente=fuente(EJ, "8"),
           enunciado=r"El sonido de la fuente A tiene el doble de frecuencia que el sonido de la "
                     r"fuente B. Compara las longitudes de las ondas sonoras de las dos fuentes.",
           respuesta=r"La longitud de onda de A es la mitad de la de B, porque ambos sonidos viajan "
                     r"con la misma rapidez y $\lambda = v/f$.", **COMUN)
def _():
    fB = 200 * hertz                                   # cualquier valor sirve
    assert simplify((V_SON / (2 * fB)) / (V_SON / fB)) == Q(1, 2)


@ejercicio(id=f"{P}-037", tipo="conceptual", dificultad=2, fuente=fuente(EJ, "9"),
           enunciado=r"Imagina que una onda sonora y una onda electromagnética tuvieran la misma "
                     r"frecuencia. ¿Cuál tendría la mayor longitud de onda?",
           respuesta=r"La electromagnética: viaja casi un millón de veces más rápido "
                     r"($\num{3e8}\,\text{m/s}$ frente a $340\,\text{m/s}$), y con la misma "
                     r"frecuencia $\lambda = v/f$ es proporcional a la rapidez.", **COMUN)
def _():
    razon = simplify((C_LUZ / (1000 * hertz)) / (V_SON / (1000 * hertz)))
    assert razon > 800000                              # unas \num{880000} veces


manuales(EJ, [
    (38, "10", r"¿Qué sucede con la longitud de onda del sonido conforme se incrementa la "
               r"frecuencia?",
     r"Disminuye, porque la rapidez del sonido en el mismo medio no cambia y $\lambda = v/f$."),
    (39, "11", r"En los arrancadores de una pista de atletismo, se aprecia el humo de la pistola "
               r"de arranque antes de oír el disparo. Explica por qué.",
     r"La luz que viene del humo llega casi al instante; el sonido del disparo viaja a unos "
     r"$340\,\text{m/s}$ y tarda más en llegar."),
    (40, "12", r"En una competencia olímpica, un micrófono capta el sonido de la pistola de "
               r"arranque y lo manda eléctricamente a altoparlantes, en cada arrancador de los "
               r"competidores. ¿Por qué?",
     r"Para que todos oigan el disparo al mismo tiempo. Sin altoparlantes, los corredores más "
     r"lejanos de la pistola lo oirían un poco después (unos $3\,\text{ms}$ por cada metro) y "
     r"arrancarían en desventaja; la señal eléctrica llega prácticamente al instante."),
    (41, "13", r"Cuando una onda sonora pasa por un punto en el aire, ¿hay cambios de la densidad "
               r"del aire en ese punto? Explica por qué.",
     r"Sí. La onda sonora es una sucesión de compresiones y enrarecimientos: en ese punto la "
     r"densidad (y la presión) del aire aumenta y disminuye periódicamente."),
    (42, "14", r"En el instante en que una región de alta presión se crea justo fuera de las "
               r"ramas de un diapasón que vibra, ¿qué se crea dentro de las ramas?",
     r"Una región de baja presión (un enrarecimiento): cuando las ramas se separan comprimen el "
     r"aire de afuera y dejan más espacio al aire de adentro."),
    (43, "15", r"Si una campana suena dentro de un capelo de vidrio, ya no la podremos oír si "
               r"dentro del capelo se hace el vacío, pero la podemos seguir viendo. ¿Qué indica "
               r"esto acerca de las diferentes propiedades de las ondas sonoras y las ondas "
               r"luminosas?",
     r"Que el sonido necesita un medio material para propagarse y la luz no: la luz (onda "
     r"electromagnética) viaja por el vacío."),
    (44, "16", r"¿Por qué la Luna se considera un «planeta silencioso»?",
     r"Porque no tiene atmósfera: no hay aire que transmita el sonido."),
    (45, "17", r"Al verter agua en un vaso, lo golpeas repetidamente con una cuchara. A medida que "
               r"el vaso se llena, ¿aumentará o disminuirá la altura del sonido producido? (¿Qué "
               r"debes hacer para contestar esta pregunta?)",
     r"Disminuye (el sonido se hace más grave): el agua vibra junto con el vidrio, agrega masa y "
     r"baja la frecuencia natural del vaso. Para contestar con seguridad hay que hacer el "
     r"experimento y escuchar."),
    (46, "18", r"Si la rapidez del sonido dependiera de su frecuencia, ¿disfrutarías de un "
               r"concierto sentado hasta un segundo piso? Explica por qué.",
     r"No. Los sonidos de distintas frecuencias, emitidos al mismo tiempo, llegarían en momentos "
     r"distintos, y cuanto más lejos del escenario, mayor sería el desfase: la música se oiría "
     r"desordenada."),
], tipo="conceptual", dificultad=2)


@ejercicio(id=f"{P}-047", tipo="conceptual", dificultad=2, fuente=fuente(EJ, "19"),
           enunciado=r"Si la frecuencia del sonido sube al doble, ¿qué cambio tendrá su rapidez? "
                     r"¿Y su longitud de onda?",
           respuesta=r"La rapidez no cambia (depende del medio); la longitud de onda se reduce a "
                     r"la mitad.", **COMUN)
def _():
    fr = symbols("f", positive=True)
    assert (V_SON / (2 * fr)) / (V_SON / fr) == Q(1, 2)


manuales(EJ, [
    (48, "20", r"¿Por qué el sonido se propaga con más rapidez en aire cálido?",
     r"Porque las moléculas del aire caliente se mueven más rápido y chocan más a menudo, así que "
     r"transmiten el impulso en menos tiempo."),
    (49, "21", r"¿Por qué el sonido se propaga con más rapidez en aire húmedo? (Sugerencia: a la "
               r"misma temperatura, las moléculas de vapor de agua tienen la misma energía "
               r"cinética promedio que las moléculas de nitrógeno u oxígeno del aire, que son más "
               r"pesadas. Entonces, ¿cómo se comparan las rapideces promedio de las moléculas de "
               r"$\text{H}_2\text{O}$ con las de $\text{N}_2$ y $\text{O}_2$?)",
     r"Las moléculas de $\text{H}_2\text{O}$ (masa 18) son más livianas que las de $\text{N}_2$ "
     r"(28) y $\text{O}_2$ (32); con la misma energía cinética promedio, se mueven más rápido. "
     r"Por eso el aire húmedo transmite la perturbación con más rapidez."),
    (50, "22", r"¿Sería posible la refracción del sonido, si la rapidez de éste no se afectara con "
               r"el viento, la temperatura y otras condiciones? Defiende tu respuesta.",
     r"No. La refracción se produce justamente porque distintas partes del frente de onda viajan "
     r"con rapideces distintas; si la rapidez fuera igual en todas partes, el sonido no se "
     r"desviaría."),
    (51, "23", r"¿Por qué se puede sentir la vibración del suelo lejos de una explosión, antes que "
               r"se oiga el sonido de ésta?",
     r"Porque el sonido viaja más rápido por el suelo (un sólido) que por el aire."),
    (52, "24", r"¿Qué clase de condiciones de viento harían que el sonido se escuchara con más "
               r"facilidad a grandes distancias? ¿Y con menos facilidad a grandes distancias?",
     r"Se oye mejor a favor del viento, cuando el viento es más fuerte en lo alto que cerca del "
     r"suelo: la parte alta del frente de onda avanza más rápido y el sonido se curva hacia el "
     r"suelo. Se oye peor contra el viento: el frente se curva hacia arriba y se aleja del "
     r"suelo."),
    (53, "25", r"Las ondas ultrasónicas tienen muchas aplicaciones en la tecnología y en la "
               r"medicina. Una de sus ventajas es que se pueden usar grandes intensidades sin "
               r"dañar los oídos. Menciona otra ventaja debida a su corta longitud de onda. "
               r"(Sugerencia: ¿por qué los microscopistas usan luz azul y no roja para ver con "
               r"mayor detalle?)",
     r"Se difractan menos, así que permiten detectar y ver detalles más pequeños (mayor "
     r"resolución), como hace la luz azul en el microscopio o el delfín con sus ecos."),
    (54, "26", r"¿Por qué el eco es más débil que el sonido original?",
     r"Porque la superficie que lo refleja absorbe o deja pasar parte de la energía, y además "
     r"el sonido se reparte en un recorrido más largo (ida y vuelta)."),
], tipo="conceptual", dificultad=2)


@ejercicio(id=f"{P}-055", tipo="calculo", dificultad=2, fuente=fuente(EJ, "27"),
           enunciado=r"Si la distancia a la que se encuentra un clarín se triplicara, ¿por qué "
                     r"factor disminuiría la intensidad del sonido? Supón que el sonido no se ve "
                     r"afectado por reflexiones.",
           respuesta=r"La intensidad disminuye con el cuadrado de la distancia: se reduce a "
                     r"$\left(\tfrac{1}{3}\right)^2 = \tfrac{1}{9}$, es decir, nueve veces menos.",
           notas="La ley del inverso del cuadrado no está explicada en el capítulo 2; la guía la "
                 "enuncia en el ejercicio 35 del capítulo 3.", **COMUN)
def _():
    r = symbols("r", positive=True)
    intensidad = lambda d: 1 / (4 * 3.14159 * d**2)    # potencia repartida en una esfera
    assert abs(float(intensidad(3 * 2) / intensidad(2)) - 1 / 9) < 1e-12
    assert simplify((1 / (3 * r)**2) / (1 / r**2)) == Q(1, 9)


manuales(EJ, [
    (56, "28", r"¿Cuáles son los dos errores de física que se cometen en una película de ciencia "
               r"ficción, cuando se ve una explosión lejana en el espacio exterior, y observas y "
               r"escuchas esa explosión al mismo tiempo?",
     r"Primero, en el espacio (vacío) el sonido no se propaga, así que no se oiría nada. "
     r"Segundo, aunque hubiera un medio, el sonido llegaría mucho después que la luz, no al "
     r"mismo tiempo."),
    (57, "29", r"Si una sola perturbación a cierta distancia manda ondas transversales y "
               r"longitudinales al mismo tiempo, que se propagan con rapideces bastante distintas "
               r"en el medio, por ejemplo, en el suelo durante un terremoto, ¿cómo se podría "
               r"determinar la distancia a la perturbación?",
     r"Midiendo el tiempo $\Delta t$ entre la llegada de la onda rápida y la de la lenta. Si sus "
     r"rapideces son $v_1 > v_2$, la distancia $d$ cumple "
     r"$\dfrac{d}{v_2} - \dfrac{d}{v_1} = \Delta t$, de donde se despeja $d$."),
    (58, "30", r"¿Por qué todos los soldados al final de un largo desfile, que marchan con el ritmo "
               r"de una banda, no guardan el mismo paso que los del principio del desfile?",
     r"Porque el sonido de la banda tarda más en llegar a los soldados que están lejos: oyen el "
     r"ritmo con retraso y marchan desfasados respecto a los que están cerca de la banda."),
    (59, "31", r"¿Por qué los soldados rompen filas al cruzar por un puente?",
     r"Para evitar que el ritmo de la marcha coincida con la frecuencia natural del puente y lo "
     r"haga entrar en resonancia (así se derrumbó un puente cerca de Manchester en 1831)."),
    (60, "32", r"¿Por qué el sonido de un arpa es suave en comparación con el de un piano?",
     r"Porque la caja de resonancia del arpa es pequeña comparada con la tabla armónica del "
     r"piano, que al vibrar (vibración forzada) pone en movimiento mucho más aire."),
    (61, "33", r"Los habitantes de los edificios de apartamentos son testigos de que las notas "
               r"bajas se escuchan mejor cuando suena la música en los apartamentos más cercanos. "
               r"¿Por qué crees que los sonidos de menor frecuencia atraviesan con más facilidad "
               r"las paredes, los pisos y los techos?",
     r"Porque la energía del sonido de alta frecuencia se transforma más rápido en energía "
     r"térmica en los materiales, mientras que los sonidos graves pierden menos energía y ponen "
     r"a vibrar con más facilidad paredes y pisos (vibración forzada), que a su vez mueven el "
     r"aire del otro lado."),
    (62, "34", r"Si el asa de un diapasón se sujeta con firmeza contra una mesa, el sonido de ese "
               r"diapasón se hace más intenso. ¿Por qué? ¿En qué afecta eso el tiempo que el "
               r"diapasón dura vibrando? Explica cómo.",
     r"La mesa vibra forzada por el diapasón y, con su gran superficie, mueve más aire: el "
     r"sonido es más intenso. Como el diapasón entrega su energía más rápido, deja de vibrar "
     r"antes (la energía total es la misma)."),
    (63, "35", r"La cítara es un instrumento musical de la India y tiene un conjunto de cuerdas "
               r"que vibran y producen música, aun cuando el músico nunca las toca. Esas «cuerdas "
               r"simpáticas» son idénticas a las cuerdas que se pulsan, y están montadas abajo de "
               r"ellas. ¿Cuál es tu explicación?",
     r"Resonancia (vibración simpática): las cuerdas simpáticas tienen las mismas frecuencias "
     r"naturales que las cuerdas pulsadas, y el sonido de estas las pone a vibrar."),
    (64, "36", r"¿Por qué un tablado de danza sólo se mueve cuando se ejecutan ciertos pasos de "
               r"baile?",
     r"Porque solo algunos pasos tienen un ritmo que coincide con la frecuencia natural del "
     r"tablado; entonces entra en resonancia y la amplitud de su vibración crece."),
    (65, "37", r"Un par de altavoces colocados a ambos lados de un escenario emiten tonos puros "
               r"idénticos (de una frecuencia fija y con una longitud de onda fija en el aire). "
               r"Cuando uno se sitúa en el pasillo central, a igual distancia de ambos altavoces, "
               r"el sonido se escucha fuerte y claro. ¿Por qué la intensidad del sonido disminuye "
               r"considerablemente cuando uno se coloca más cerca de un lado? Sugerencia: utiliza "
               r"un diagrama para hacer tu planteamiento.",
     r"En el pasillo central las distancias a los dos altavoces son iguales: las ondas llegan en "
     r"fase e interfieren constructivamente. Al moverse hacia un lado, en algún punto una "
     r"distancia supera a la otra en media longitud de onda: las compresiones de un altavoz "
     r"llegan con los enrarecimientos del otro y hay interferencia destructiva."),
    (66, "38", r"Un dispositivo especial puede transmitir sonido fuera de fase proveniente de un "
               r"ruidoso rotomartillo a los audífonos de su operador. Sobre el ruido del martillo, "
               r"el operador puede oír con facilidad tu voz, mientras que tú no puedes escuchar "
               r"la de él. Explica por qué.",
     r"Los audífonos del operador reproducen el ruido del martillo invertido (desfasado), que "
     r"anula el ruido por interferencia destructiva pero no tu voz. Tú no tienes ese sistema: el "
     r"ruido del martillo te llega completo y tapa la voz del operador."),
    (67, "39", r"¿Cómo cierta nota emitida por un cantante puede provocar que se rompa un vaso de "
               r"cristal?",
     r"Si la nota coincide con la frecuencia natural del vaso y es suficientemente intensa, el "
     r"vaso entra en resonancia: la amplitud de su vibración crece hasta que el cristal se "
     r"rompe."),
    (68, "40", r"Un objeto resuena cuando la frecuencia de una fuerza vibratoria coincide con su "
               r"frecuencia natural, o es un submúltiplo de esa frecuencia. ¿Por qué no resuena "
               r"con múltiplos de su frecuencia natural? (Imagina que impulsas a un niño en un "
               r"columpio.)",
     r"Con un submúltiplo (por ejemplo, empujar el columpio una vez cada dos oscilaciones) cada "
     r"impulso llega en el momento adecuado y en el sentido del movimiento. Con un múltiplo (dos "
     r"empujones por oscilación) la mitad de los impulsos llegan cuando el columpio viene en "
     r"sentido contrario y lo frenan, así que la amplitud no crece."),
    (69, "41", r"¿Las pulsaciones son el resultado de la interferencia, o del efecto Doppler, o de "
               r"ambos?",
     r"De la interferencia. El efecto Doppler puede producir la diferencia de frecuencias (como "
     r"en el eco que recibe un delfín o en el radar), pero las pulsaciones mismas se deben a la "
     r"interferencia de las dos ondas."),
    (70, "42", r"¿Es posible decir, sin temor a equivocarse, que las pulsaciones de sonido son lo "
               r"mismo que los «ritmos» de la música? Argumenta tu respuesta.",
     r"No. Las pulsaciones son variaciones periódicas de la intensidad producidas por la "
     r"interferencia de dos sonidos de frecuencias cercanas; el ritmo musical es la organización "
     r"de los tiempos que decide el músico."),
    (71, "43", r"Dos ondas sonoras de la misma frecuencia pueden interferir, pero para producir "
               r"pulsaciones, las dos ondas sonoras deben tener distintas frecuencias. ¿Por qué?",
     r"Con la misma frecuencia, la diferencia de fase entre las dos ondas es constante: en cada "
     r"lugar la interferencia es siempre la misma (fija). Las pulsaciones necesitan que las "
     r"ondas pasen alternadamente de estar en fase a estar desfasadas, y eso solo ocurre si sus "
     r"frecuencias son distintas."),
], tipo="argumentacion", dificultad=2)


@ejercicio(id=f"{P}-072", tipo="contexto", dificultad=2, fuente=fuente(EJ, "44"),
           enunciado=r"Al caminar junto a ti, tu amigo da 50 pasos por minuto, mientras que tú das "
                     r"48 pasos por minuto. Si comienzan al mismo tiempo, ¿cuándo mantendrán el "
                     r"mismo paso?",
           respuesta=r"La diferencia es de 2 pasos por minuto, así que coinciden dos veces por "
                     r"minuto: cada $30\,\text{s}$ (a los 30 s, al minuto, a los 90 s…).", **COMUN)
def _():
    diferencia = 50 / minute - 48 / minute
    assert convert_to(1 / diferencia, second) == 30 * second
    # comprobación directa: en 30 s el amigo da 25 pasos y tú 24 (números enteros)
    assert (50 * Q(1, 2), 48 * Q(1, 2)) == (25, 24)


@ejercicio(id=f"{P}-073", tipo="argumentacion", dificultad=3, fuente=fuente(EJ, "45"),
           enunciado=r"Un afinador de pianos oye tres pulsaciones por segundo al escuchar el sonido "
                     r"combinado de un diapasón y la nota del piano que afina. Después de apretar "
                     r"un poco la cuerda escucha cinco pulsaciones por segundo. ¿Debería apretar o "
                     r"aflojar la cuerda?",
           respuesta=r"Aflojarla. Al apretar la cuerda su frecuencia sube; como las pulsaciones "
                     r"aumentaron (de 3 a 5), la cuerda ya estaba por encima de la frecuencia del "
                     r"diapasón y se alejó más. Hay que bajar su frecuencia hasta que las "
                     r"pulsaciones desaparezcan.", **COMUN)
def _():
    fd = 264                                            # frecuencia del diapasón (cualquiera)
    for antes in (fd - 3, fd + 3):
        despues = antes + 2                             # apretar sube la frecuencia
        if abs(despues - fd) == 5:
            assert antes > fd                           # solo es posible si estaba por encima
    assert abs((fd - 3) + 2 - fd) == 1                  # si estuviera por debajo, bajarían


@ejercicio(id=f"{P}-074", tipo="calculo", dificultad=2, fuente=fuente(EJ, "46"),
           enunciado=r"Un afinador de pianos que utiliza un diapasón de $264\,\text{Hz}$ escucha "
                     r"cuatro pulsaciones por segundo. ¿Cuáles son las dos frecuencias de vibración "
                     r"posibles de la cuerda del piano?",
           respuesta=r"$264 - 4 = 260\,\text{Hz}$ o $264 + 4 = 268\,\text{Hz}$.", **COMUN)
def _():
    x = symbols("x", real=True)
    from sympy import Abs, S, solveset
    assert solveset(Abs(x - 264) - 4, x, S.Reals) == {260, 268}


@ejercicio(id=f"{P}-075", tipo="argumentacion", dificultad=3, fuente=fuente(EJ, "47"),
           enunciado=r"Un ser humano no puede escuchar un sonido con $100\,\text{kHz}$ de "
                     r"frecuencia, ni uno de $102\,\text{kHz}$. Pero si entra en un recinto donde "
                     r"haya dos fuentes que emiten ondas sonoras, una a $100\,\text{kHz}$ y otra a "
                     r"$102\,\text{kHz}$, sí escuchará un sonido. Explica por qué.",
           respuesta=r"Las dos ondas se combinan y producen pulsaciones de "
                     r"$102 - 100 = 2\,\text{kHz} = \num{2000}\,\text{Hz}$, una frecuencia que sí "
                     r"está en el intervalo audible (20 a \num{20000} Hz).",
           notas="Precisión para la docente: estrictamente, el oído no «oye» las pulsaciones de "
                 "dos ultrasonidos como un tono; el tono de 2 kHz aparece porque el aire y el oído "
                 "no responden de forma perfectamente lineal a sonidos intensos (tono "
                 "diferencial). A este nivel basta la explicación de la guía.", **COMUN)
def _():
    pulso = 102000 * hertz - 100000 * hertz
    assert pulso == 2000 * hertz and 20 * hertz <= pulso <= 20000 * hertz
    assert 100000 > 20000                                # las dos fuentes son inaudibles


# ---------------------------------------------------------------- Problemas
PR = "Problemas"


@ejercicio(id=f"{P}-076", tipo="calculo", dificultad=1, fuente=fuente(PR, "1"),
           enunciado=r"¿Cuál es la longitud de onda de un tono de $340\,\text{Hz}$ en el aire? "
                     r"¿Cuál es la longitud de una onda ultrasónica de $\num{34000}\,\text{Hz}$ en "
                     r"el aire? (Rapidez del sonido: $340\,\text{m/s}$.)",
           respuesta=r"$\lambda = \dfrac{340\,\text{m/s}}{340\,\text{Hz}} = 1\,\text{m}$; "
                     r"$\lambda = \dfrac{340\,\text{m/s}}{\num{34000}\,\text{Hz}} = "
                     r"\num{0,01}\,\text{m} = 1\,\text{cm}$.", **COMUN)
def _():
    assert convert_to(V_SON / (340 * hertz), meter) == meter
    assert convert_to(V_SON / (34000 * hertz), meter) == Q(1, 100) * meter


@ejercicio(id=f"{P}-077", tipo="contexto", dificultad=2, fuente=fuente(PR, "2"),
           enunciado=r"Durante años, a los oceanógrafos les intrigaron las ondas sonoras captadas "
                     r"por micrófonos bajo las aguas del océano Pacífico. Estas llamadas ondas T "
                     r"son de los sonidos más puros de la naturaleza; su fuente son volcanes "
                     r"submarinos, cuyas columnas de burbujas resuenan como tubos de órgano. ¿Cuál "
                     r"es la longitud de una onda T característica cuya frecuencia es "
                     r"$7\,\text{Hz}$? (La rapidez del sonido en el agua de mar es "
                     r"$\num{1530}\,\text{m/s}$.)",
           respuesta=r"$\lambda = \dfrac{\num{1530}\,\text{m/s}}{7\,\text{Hz}} \approx "
                     r"219\,\text{m}$.", **COMUN)
def _():
    cerca(V_MAR / (7 * hertz), 219 * meter, tol=0.003)


@ejercicio(id=f"{P}-078", tipo="contexto", dificultad=2, fuente=fuente(PR, "3"),
           enunciado=r"Un barco-sonda explora el fondo del mar con ondas ultrasónicas que se "
                     r"propagan a $\num{1530}\,\text{m/s}$ en el agua. ¿Qué profundidad tiene el "
                     r"agua directamente abajo del barco, si el tiempo entre la salida de la señal "
                     r"y el regreso del eco es de $6\,\text{s}$?",
           respuesta=r"El sonido baja en $3\,\text{s}$ y sube en $3\,\text{s}$: "
                     r"$d = \num{1530}\,\text{m/s} \times 3\,\text{s} = \num{4590}\,\text{m}$.",
           **ECO)
def _():
    assert convert_to(V_MAR * 6 * second / 2, meter) == 4590 * meter


@ejercicio(id=f"{P}-079", tipo="contexto", dificultad=2, fuente=fuente(PR, "4"),
           enunciado=r"Un murciélago, al volar en una caverna, emite un sonido y recibe el eco "
                     r"$\num{0,1}\,\text{s}$ después. ¿A qué distancia está la pared de la caverna? "
                     r"(Rapidez del sonido: $340\,\text{m/s}$.)",
           respuesta=r"$d = \dfrac{340\,\text{m/s} \times \num{0,1}\,\text{s}}{2} = "
                     r"17\,\text{m}$.",
           notas="La guía no da la rapidez del sonido en este problema; se usa 340 m/s. Se "
                 "desprecia lo que avanza el murciélago durante 0,1 s.", **ECO)
def _():
    assert convert_to(V_SON * Q(1, 10) * second / 2, meter) == 17 * meter


@ejercicio(id=f"{P}-080", tipo="contexto", dificultad=3, fuente=fuente(PR, "5"),
           enunciado=r"Te fijas en una persona a lo lejos que está clavando tachuelas en el "
                     r"vestíbulo de su casa, dando un golpe por segundo. Escuchas el sonido de los "
                     r"golpes exactamente en sincronía con cada golpe del martillo. Y después que "
                     r"termina de martillar, escuchas un golpe de más. ¿A qué distancia está esa "
                     r"persona? (Rapidez del sonido: $340\,\text{m/s}$.)",
           respuesta=r"El golpe de más indica que cada sonido llega $1\,\text{s}$ después del "
                     r"golpe que lo produjo (coincide con el golpe siguiente). Entonces "
                     r"$d = 340\,\text{m/s} \times 1\,\text{s} = 340\,\text{m}$.", **ECO)
def _():
    retraso = 1 * second                                # un golpe de más, a un golpe por segundo
    assert convert_to(V_SON * retraso, meter) == 340 * meter


@ejercicio(id=f"{P}-081", tipo="contexto", dificultad=2, fuente=fuente(PR, "6"),
           enunciado=r"Imagina a un leñador dormilón que vive en las montañas. Antes de acostarse "
                     r"a dormir grita: «¡DESPIÉRTATE!», y el eco del sonido en la montaña más "
                     r"cercana le llega ocho horas después y lo despierta. ¿A qué distancia está "
                     r"la montaña? (Rapidez del sonido: $340\,\text{m/s}$.)",
           respuesta=r"Ida en $4\,\text{h} = \num{14400}\,\text{s}$: "
                     r"$d = 340\,\text{m/s} \times \num{14400}\,\text{s} \approx "
                     r"\num{4,9e6}\,\text{m}$, casi $\num{4900}\,\text{km}$ (un problema en broma: "
                     r"un eco no se oiría a esa distancia).",
           notas="Se añade la rapidez del sonido (340 m/s), que la guía no da aquí.", **ECO)
def _():
    d = V_SON * 4 * hour
    assert convert_to(d, meter) == 4896000 * meter
    cerca(d, 4900 * 1000 * meter, tol=0.001)


for n, lit, d1, d2, tipo_int, explic in [
        (82, "7a", 12, 12, "constructiva",
         r"las distancias son iguales (diferencia $0$), así que las ondas llegan en fase"),
        (83, "7b", 9, 9, "constructiva",
         r"las distancias son iguales (diferencia $0$), así que las ondas llegan en fase"),
        (84, "7c", 9, 12, "destructiva",
         r"la diferencia de caminos es $3\,\text{m} = \frac{\lambda}{2}$, así que las ondas "
         r"llegan desfasadas")]:
    lugar = {"7a": r"a $12\,\text{m}$ de cada una de las bocinas (frente a ellas)",
             "7b": r"a $9\,\text{m}$ de ambas bocinas",
             "7c": r"a $9\,\text{m}$ de una bocina y a $12\,\text{m}$ de la otra"}[lit]

    @ejercicio(id=f"{P}-{n:03d}", tipo="contexto", dificultad=2, fuente=fuente(PR, lit),
               enunciado=r"Dos bocinas se conectan para emitir sonidos idénticos al unísono. La "
                         r"longitud de onda de los sonidos en el aire es $6\,\text{m}$. ¿Los "
                         r"sonidos interfieren constructiva o destructivamente si estás "
                         + lugar + "?",
               respuesta=f"Interferencia {tipo_int}: {explic}.",
               notas=("En la guía: «12 m frente a las bocinas»; se entiende a 12 m de cada una."
                      if lit == "7a" else None) or "", **COMUN)
    def _(d1=d1, d2=d2, tipo_int=tipo_int):
        diferencia = Q(abs(d1 - d2), 6)                  # en longitudes de onda
        constructiva = diferencia.q == 1                 # número entero de longitudes de onda
        destructiva = (2 * diferencia).q == 1 and not constructiva   # múltiplo impar de λ/2
        assert (tipo_int == "constructiva" and constructiva) or \
               (tipo_int == "destructiva" and destructiva)


@ejercicio(id=f"{P}-085", tipo="contexto", dificultad=2, fuente=fuente(PR, "8"),
           enunciado=r"¿Cuál es la frecuencia del sonido emitido por las bocinas del problema "
                     r"anterior (longitud de onda $6\,\text{m}$ en el aire, rapidez "
                     r"$340\,\text{m/s}$)? ¿Es de un tono grave o de uno agudo, en relación con el "
                     r"rango de audición del oído humano?",
           respuesta=r"$f = \dfrac{340\,\text{m/s}}{6\,\text{m}} \approx 57\,\text{Hz}$: un tono "
                     r"grave, cerca del extremo inferior del intervalo audible (20 a "
                     r"\num{20000} Hz).", **COMUN)
def _():
    fr = convert_to(V_SON / (6 * meter), hertz)
    cerca(fr, 57 * hertz, tol=0.01)
    assert 20 * hertz < fr < 200 * hertz


@ejercicio(id=f"{P}-086", tipo="contexto", dificultad=2, fuente=fuente(PR, "9"),
           enunciado=r"Una marsopa emite un sonido a $57\,\text{Hz}$. ¿Cuál es la longitud de onda "
                     r"de este sonido en el agua, donde la rapidez del sonido es de "
                     r"$\num{1500}\,\text{m/s}$?",
           respuesta=r"$\lambda = \dfrac{\num{1500}\,\text{m/s}}{57\,\text{Hz}} \approx "
                     r"\num{26,3}\,\text{m}$.", **COMUN)
def _():
    cerca(1500 * meter / second / (57 * hertz), Q(263, 10) * meter, tol=0.002)


@ejercicio(id=f"{P}-087", tipo="calculo", dificultad=2, fuente=fuente(PR, "10"),
           enunciado=r"¿Qué frecuencias de pulsaciones se pueden obtener con diapasones cuyas "
                     r"frecuencias sean de 256, 259 y $261\,\text{Hz}$?",
           respuesta=r"Combinándolos de dos en dos: $259 - 256 = 3\,\text{Hz}$, "
                     r"$261 - 259 = 2\,\text{Hz}$ y $261 - 256 = 5\,\text{Hz}$.", **COMUN)
def _():
    from itertools import combinations
    assert {abs(a - b) for a, b in combinations([256, 259, 261], 2)} == {2, 3, 5}
