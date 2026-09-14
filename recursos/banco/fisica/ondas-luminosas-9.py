"""Banco de ejercicios — Física 9° — Ondas luminosas (difracción, interferencia, polarización).
Fuente: Guía de Apoyo de Física 9° (ondas, sonido y luz), Capítulo 5 «Ondas luminosas»:
Preguntas de repaso y Ejercicios (el capítulo no tiene Problemas). Se lee en
recursos/fisica/Guías pedagógicas Física/markdown/09 - Guia_de_Apoyo_Conceptos_ondas_de_sonido_y_de_luz_grado_9_fisica.md
Alineación: Estándares 8°–9° (dba/naturales/estandares-fisica.md) — «Reconozco y diferencio
modelos para explicar la naturaleza y el comportamiento de la luz»; «Identifico aplicaciones de
los diferentes modelos de la luz».
No incluidos: los «Examínate» (ya traen su respuesta; el de los anteojos depende de la imagen 54)
y el Proyecto 1 (diapositivas con celofán y Polaroid).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/fisica/ondas-luminosas-9.py
"""
from sympy import Rational as Q, cos, integrate, pi, simplify, sin, symbols

from ejercicios import ejercicio, ejercicio_manual

P = "ondas-luminosas-9"
GUIA = "Guía de Apoyo Física 9° (ondas, sonido y luz), Cap. 5 Ondas luminosas"
COMUN = dict(tema="ondas luminosas", grados=[9], dba=[])
th, x = symbols("theta x", real=True)


def fuente(seccion, lit):
    return f"{GUIA}, {seccion} — {lit}"


def manuales(seccion, filas, **extra):
    for n, lit, enunciado, respuesta, *notas in filas:
        meta = {**COMUN, **extra}
        if notas:
            meta["notas"] = notas[0]
        ejercicio_manual(id=f"{P}-{n:03d}", fuente=fuente(seccion, lit),
                         enunciado=enunciado, respuesta=respuesta, **meta)


def fraccion_no_polarizada():
    """Fracción de la luz no polarizada que deja pasar un polarizador ideal: el promedio de
    cos² sobre todas las direcciones de vibración."""
    return integrate(cos(th)**2, (th, 0, 2 * pi)) / (2 * pi)


# ---------------------------------------------------------------- Preguntas de repaso
REPASO = "Preguntas de repaso"
manuales(REPASO, [
    (1, "1", r"Según Huygens, ¿cómo se comporta cada punto de un frente de onda?",
     r"Como una fuente de ondas secundarias pequeñas; la envolvente de todas ellas forma el "
     r"frente de onda siguiente."),
    (2, "2", r"¿Las ondas planas que inciden en una pequeña abertura en una barrera se extenderán "
             r"o continuarán en forma de ondas planas?",
     r"Se extenderán hacia la región de sombra (se difractan): la abertura se comporta como una "
     r"fuente casi puntual de ondas circulares."),
    (3, "3", r"¿La difracción es más pronunciada a través de una abertura pequeña que a través de "
             r"una grande?",
     r"Sí: cuanto más pequeña es la abertura comparada con la longitud de onda, más se nota la "
     r"difracción."),
    (4, "4", r"Para una abertura de tamaño determinado, ¿la difracción es más pronunciada para una "
             r"longitud de onda mayor que para una longitud de onda menor?",
     r"Sí: las ondas más largas se difractan más."),
    (5, "5", r"¿Qué se difracta con más facilidad en torno a las construcciones, las ondas de radio "
             r"AM o las de FM? ¿Por qué?",
     r"Las de AM, porque su longitud de onda (de 180 a 550 m) es mucho mayor que la de las de FM "
     r"(unos 3 m) y grande comparada con los edificios."),
    (6, "6", r"¿Se restringe la interferencia sólo a algunas clases de ondas, o sucede con todo "
             r"tipo de ellas?",
     r"Sucede con todo tipo de ondas."),
    (7, "7", r"¿Qué demostró exactamente Thomas Young en su famoso experimento con la luz?",
     r"Que la luz es una onda: al pasar por dos agujeros (o rendijas) muy cercanos, la luz "
     r"interfiere consigo misma y forma bandas claras y oscuras en una pantalla."),
    (8, "8", r"¿Qué fenómeno distingue a las ondas longitudinales de las transversales?",
     r"La polarización: solo las ondas transversales se pueden polarizar."),
    (9, "9", r"¿La polarización es característica de todas las clases de ondas?",
     r"No, solo de las ondas transversales."),
    (10, "10", r"¿Cómo se compara la dirección de polarización de la luz con la dirección de "
               r"vibración del electrón que la produce?",
     r"Coinciden: el plano de polarización es el de la vibración del electrón."),
    (11, "11", r"¿Por qué la luz pasa por un par de filtros polarizadores cuando están alineados "
               r"los ejes, pero no cuando los ejes están perpendiculares entre sí?",
     r"El primer filtro deja pasar solo la luz que vibra en la dirección de su eje. Si el segundo "
     r"tiene el eje en la misma dirección, esa luz pasa; si lo tiene perpendicular, bloquea "
     r"justamente esa dirección de vibración y no pasa luz."),
], tipo="conceptual", dificultad=1)


@ejercicio(id=f"{P}-012", tipo="conceptual", dificultad=1, fuente=fuente(REPASO, "12"),
           enunciado=r"¿Cuánta luz ordinaria (no polarizada) transmite un filtro Polaroid?",
           respuesta=r"Un filtro ideal transmite el $50\,\%$ (y esa luz sale polarizada).",
           **COMUN)
def _():
    assert fraccion_no_polarizada() == Q(1, 2)


manuales(REPASO, [
    (13, "13", r"Cuando la luz ordinaria incide formando un ángulo con el agua, ¿qué puedes decir "
               r"acerca de la luz reflejada?",
     r"Que está (parcialmente) polarizada: vibra sobre todo en dirección paralela a la "
     r"superficie del agua, es decir, horizontal."),
    (14, "14", r"¿Por qué no percibirías la profundidad si examinaras dos copias de diapositivas "
               r"ordinarias con un visor estereoscópico, y sí cuando examinas los pares de "
               r"transparencias tomadas con una cámara estereoscópica?",
     r"Porque dos copias iguales muestran la escena desde el mismo punto de vista. Para percibir "
     r"profundidad, cada ojo debe ver una imagen tomada desde una posición un poco distinta, "
     r"como las de la cámara estereoscópica."),
    (15, "15", r"¿Qué papel juegan los filtros polarizadores en una proyección de transparencias en "
               r"3-D (tercera dimensión)?",
     r"Cada proyector tiene un filtro con el eje en una dirección distinta (por ejemplo, "
     r"horizontal y vertical); con anteojos polarizados orientados igual, cada ojo ve solo la "
     r"imagen de su proyector, y el cerebro las combina con sensación de profundidad."),
    (16, "16", r"¿En qué difiere un holograma de una fotografía convencional?",
     r"La fotografía registra una imagen formada por una lente (cada punto del objeto en un "
     r"punto de la película). El holograma, sin lente, registra el patrón de interferencia entre "
     r"la luz que refleja el objeto y un haz de referencia; al iluminarlo con luz coherente "
     r"reproduce una imagen tridimensional."),
    (17, "17", r"¿En qué difiere la luz coherente de la luz ordinaria?",
     r"La luz coherente tiene una sola frecuencia y todas sus partes están en fase (como la de un "
     r"láser); la luz ordinaria mezcla muchas frecuencias con fases al azar."),
    (18, "18", r"¿Cómo se puede obtener un aumento holográfico?",
     r"Haciendo el holograma con luz de longitud de onda corta y observándolo con luz de "
     r"longitud de onda más larga: la imagen se amplía en la misma proporción que las longitudes "
     r"de onda."),
], tipo="conceptual", dificultad=1)

# ---------------------------------------------------------------- Ejercicios
EJ = "Ejercicios"
manuales(EJ, [
    (19, "1", r"¿Por qué la luz solar que ilumina la Tierra se puede aproximar con ondas planas, "
              r"mientras que la de una lámpara cercana no?",
     r"Porque el Sol está tan lejos que sus frentes de onda esféricos llegan con una curvatura "
     r"insignificante (casi planos); los de una lámpara cercana todavía son muy curvos."),
    (20, "2", r"En nuestro ambiente cotidiano, la difracción es mucho más evidente en las ondas "
              r"sonoras que en las ondas luminosas. ¿Por qué?",
     r"Porque las longitudes de onda del sonido (de centímetros a metros) son comparables con el "
     r"tamaño de puertas, muebles y personas, mientras que las de la luz son de cientos de "
     r"nanómetros, muchísimo menores que los objetos cotidianos."),
    (21, "3", r"¿Por qué las ondas de radio se difractan en torno a los edificios, mientras que las "
              r"ondas luminosas no?",
     r"Porque la longitud de onda de las ondas de radio es comparable o mayor que el tamaño de "
     r"los edificios, y la de la luz es muchísimo menor."),
    (22, "4", r"¿Puedes imaginar una razón por la que los canales de TV de número bajo pueden dar "
              r"mejores imágenes en regiones de recepción deficiente? (Sugerencia: los canales "
              r"bajos representan menores frecuencias de portadora.)",
     r"Menor frecuencia significa mayor longitud de onda, y las ondas más largas se difractan "
     r"más: rodean mejor montañas y edificios y llegan a las zonas «de sombra»."),
    (23, "5", r"Dos altavoces a una distancia aproximada de 1 metro emiten tonos puros de la misma "
              r"frecuencia y sonoridad. Cuando un escucha pasa frente a ellos, en una trayectoria "
              r"paralela a la línea que los une, oye que el sonido alterna de fuerte a débil. "
              r"¿Qué está sucediendo?",
     r"Interferencia: en algunos puntos las ondas de los dos altavoces llegan en fase "
     r"(constructiva, sonido fuerte) y en otros llegan desfasadas media longitud de onda "
     r"(destructiva, sonido débil)."),
    (24, "6", r"En el ejercicio anterior, sugiere una trayectoria para que el escucha que la siga "
              r"camine sin oír los sonidos fuertes y débiles alternadamente.",
     r"Caminar por la línea perpendicular al segmento que une los altavoces y que pasa por su "
     r"punto medio (acercándose o alejándose por el centro): en ella las distancias a los dos "
     r"altavoces son siempre iguales y la interferencia es siempre constructiva."),
    (25, "7", r"¿En qué se parecen las bandas de interferencia a la intensidad variable del sonido "
              r"que percibes al pasar frente a un par de altavoces que emitan el mismo sonido?",
     r"En ambos casos hay zonas alternadas de interferencia constructiva y destructiva, "
     r"producidas por la diferencia de caminos desde dos fuentes: en la luz se ven como bandas "
     r"claras y oscuras; en el sonido, como zonas de sonido fuerte y débil."),
], tipo="conceptual", dificultad=2)


@ejercicio(id=f"{P}-026", tipo="conceptual", dificultad=2, fuente=fuente(EJ, "8"),
           enunciado=r"¿En cuánto deberían diferir en longitud un par de rayos de luz de una fuente "
                     r"común, para producir interferencia destructiva?",
           respuesta=r"En media longitud de onda (o en un múltiplo impar de ella: "
                     r"$\frac{3}{2}\lambda$, $\frac{5}{2}\lambda$…).", **COMUN)
def _():
    onda = lambda desfase: sin(2 * pi * x) + sin(2 * pi * (x + desfase))   # λ = 1
    for d in (Q(1, 2), Q(3, 2), Q(5, 2)):
        assert simplify(onda(d)) == 0
    assert simplify(onda(1)) != 0


manuales(EJ, [
    (27, "9", r"Una luz ilumina dos rendijas pequeñas y próximas, y produce un patrón de "
              r"interferencia en una pantalla más adelante. ¿En qué será diferente la distancia "
              r"entre las bandas producidas por luz roja y por luz azul?",
     r"Con luz roja las bandas quedan más separadas, porque su longitud de onda es mayor; con "
     r"luz azul, más juntas."),
], tipo="conceptual", dificultad=2)


@ejercicio(id=f"{P}-028", tipo="conceptual", dificultad=2, fuente=fuente(EJ, "10"),
           enunciado=r"Si la diferencia en la longitud de la trayectoria entre dos haces idénticos y "
                     r"coherentes es de dos longitudes de onda cuando llegan a una pantalla, "
                     r"¿producirán una mancha clara o una oscura?",
           respuesta=r"Una mancha clara: una diferencia de un número entero de longitudes de onda "
                     r"hace que lleguen en fase (interferencia constructiva).", **COMUN)
def _():
    suma = sin(2 * pi * x) + sin(2 * pi * (x + 2))
    assert simplify(suma - 2 * sin(2 * pi * x)) == 0     # amplitud doble


manuales(EJ, [
    (29, "11", r"¿Cuál producirá franjas de luz más anchas al pasar a través de una rejilla de "
               r"difracción, la de un láser de luz verde o la de un láser de luz azul?",
     r"La del láser verde, porque su longitud de onda es mayor que la de la luz azul."),
    (30, "12", r"Se produce un patrón de bandas cuando pasa luz monocromática por un par de "
               r"rendijas delgadas. ¿Se produciría ese mismo patrón con tres rendijas delgadas y "
               r"paralelas? ¿Y con miles de esas rendijas? Menciona un ejemplo que apoye tus "
               r"respuestas.",
     r"Sí, también se forman bandas (con más rendijas las franjas brillantes son más angostas y "
     r"nítidas). Con miles de rendijas se tiene una rejilla de difracción, como la de los "
     r"espectrómetros o los surcos de un disco compacto, que separa la luz blanca en colores."),
    (31, "13", r"Imagina que colocas una rejilla de difracción frente a la lente de una cámara, y "
               r"que tomas una foto del alumbrado público encendido. ¿Qué crees que verás en la "
               r"fotografía?",
     r"Cada lámpara aparecerá acompañada, a los lados, de franjas con los colores del espectro, "
     r"porque la rejilla separa su luz en colores."),
    (32, "14", r"¿Qué sucede a la distancia entre las franjas de interferencia cuando se aumenta la "
               r"separación de las dos rendijas?",
     r"Disminuye: las franjas quedan más juntas."),
    (33, "15", r"¿Por qué el experimento de Young es más efectivo con rendijas que con agujeros de "
               r"alfiler?",
     r"Porque las rendijas dejan pasar más luz y producen bandas rectas, más brillantes y fáciles "
     r"de ver que el patrón de los agujeros."),
    (34, "16", r"Los colores de los pavos reales y de los colibríes no se deben a pigmentos, sino a "
               r"elevaciones en las capas superficiales de sus plumas. ¿Mediante qué principio "
               r"físico tales elevaciones producen colores?",
     r"La interferencia de la luz reflejada en esas capas y estructuras microscópicas."),
    (35, "17", r"Las alas de colores de muchas mariposas se deben a pigmentaciones; pero en otras, "
               r"como en la mariposa morfo, los colores no se deben a pigmentaciones. Cuando el ala "
               r"se ve desde distintos ángulos, sus colores cambian. ¿Cómo se producen esos "
               r"colores?",
     r"Por interferencia de la luz que se refleja en las capas microscópicas de las escamas del "
     r"ala. Como la diferencia de caminos depende del ángulo de observación, el color que se "
     r"refuerza cambia al mirar desde otro ángulo."),
    (36, "18", r"Cuando los platos no se enjuagan bien después de lavarlos, se reflejan distintos "
               r"colores en sus superficies. Explica cómo y por qué.",
     r"Queda una película delgada de jabón. La luz que se refleja en su cara superior interfiere "
     r"con la que se refleja en la inferior; según el espesor de la película, unos colores se "
     r"refuerzan y otros se anulan."),
    (37, "19", r"¿La luz de dos estrellas que estén muy cercanas producirá un patrón de "
               r"interferencia? Explica por qué.",
     r"No: la luz de dos estrellas distintas no es coherente (sus fases cambian al azar), así que "
     r"no se forma un patrón estable."),
    (38, "20", r"Para el telescopio espacial Hubble, ¿qué luz (roja, verde, azul o ultravioleta) es "
               r"mejor para ver los detalles finos de los cuerpos astronómicos lejanos?",
     r"La ultravioleta: tiene la menor longitud de onda y, por tanto, la menor difracción (el "
     r"Hubble, fuera de la atmósfera, sí la recibe)."),
    (39, "21", r"La luz polarizada es parte de la naturaleza, pero el sonido polarizado no. ¿Por "
               r"qué?",
     r"Porque la polarización solo existe en las ondas transversales, y el sonido (en el aire) es "
     r"una onda longitudinal."),
    (40, "22", r"Normalmente, las pantallas digitales de los relojes y otros aparatos son "
               r"polarizadas. ¿Qué problema se presenta al usar también lentes polarizados para "
               r"sol?",
     r"Si el eje de los lentes queda perpendicular al de la luz de la pantalla, la pantalla se ve "
     r"oscura y no se puede leer (hay que girar la cabeza o el aparato)."),
], tipo="conceptual", dificultad=2)


@ejercicio(id=f"{P}-041", tipo="argumentacion", dificultad=2, fuente=fuente(EJ, "23"),
           enunciado=r"¿Por qué un filtro polarizador ideal transmite el $50\,\%$ de la luz "
                     r"incidente no polarizada?",
           respuesta=r"Porque la luz no polarizada vibra en todas las direcciones por igual y se "
                     r"puede representar con dos componentes perpendiculares de la misma "
                     r"intensidad; el filtro deja pasar la componente paralela a su eje y bloquea "
                     r"la otra.", **COMUN)
def _():
    assert fraccion_no_polarizada() == Q(1, 2)
    assert cos(0)**2 + cos(pi / 2)**2 == 1               # las dos componentes suman el total


@ejercicio(id=f"{P}-042", tipo="calculo", dificultad=2, fuente=fuente(EJ, "24"),
           enunciado=r"¿Qué porcentaje de la luz (no polarizada) transmiten dos filtros "
                     r"polarizadores, uno tras otro, con sus ejes de polarización alineados? ¿Con "
                     r"sus ejes perpendiculares entre sí?",
           respuesta=r"Alineados: el $50\,\%$ (el segundo deja pasar toda la luz que sale del "
                     r"primero). Perpendiculares: $0\,\%$.", **COMUN)
def _():
    primero = fraccion_no_polarizada()
    assert primero * cos(0)**2 == Q(1, 2)
    assert primero * cos(pi / 2)**2 == 0


manuales(EJ, [
    (43, "25", r"¿Cómo puedes determinar el eje de polarización de una sola lámina de filtro "
               r"Polaroid?",
     r"Mirando a través de ella el reflejo de la luz en una superficie horizontal (agua, vidrio "
     r"o un piso pulido), que está polarizado horizontalmente, y girándola: cuando el reflejo se "
     r"ve más oscuro, el eje de la lámina está vertical."),
    (44, "26", r"¿Por qué los anteojos polarizados reducen el resplandor, mientras que los no "
               r"polarizados sólo bajan la cantidad total de luz que llega a los ojos?",
     r"Porque el resplandor es luz reflejada polarizada horizontalmente, y los anteojos "
     r"polarizados (eje vertical) la bloquean casi toda; los no polarizados reducen por igual "
     r"toda la luz, sin quitar especialmente el resplandor."),
    (45, "27", r"Para eliminar el resplandor de la luz procedente de un piso pulido, el eje de un "
               r"filtro polarizador, ¿debe estar horizontal o vertical?",
     r"Vertical."),
    (46, "28", r"La mayoría del resplandor de las superficies no metálicas está polarizado, y el "
               r"eje de polarización es paralelo a la superficie reflectora. ¿Esperarías que el "
               r"eje de polarización de los anteojos polarizados fuera vertical u horizontal? ¿Por "
               r"qué?",
     r"Vertical: el resplandor de superficies horizontales (carretera, agua) está polarizado "
     r"horizontalmente, y un eje vertical lo bloquea."),
], tipo="conceptual", dificultad=2)


@ejercicio(id=f"{P}-047", tipo="argumentacion", dificultad=3, fuente=fuente(EJ, "29"),
           enunciado=r"La luz no pasa a través de un par de láminas Polaroid con ejes "
                     r"perpendiculares. Pero si entre las dos se intercala una tercera (con su eje a "
                     r"$45^{\circ}$ con los de las otras dos), algo de luz logra pasar. ¿Por qué?",
           respuesta=r"La lámina intermedia deja pasar una componente de la luz que sale de la "
                     r"primera, y esa luz sale polarizada a $45^{\circ}$; como ya no es "
                     r"perpendicular al último filtro, este deja pasar una componente de ella. "
                     r"(Con filtros ideales pasa $\tfrac{1}{2}\cos^2 45^{\circ}\cos^2 45^{\circ} "
                     r"= \tfrac{1}{8}$, un $\num{12,5}\,\%$ de la luz no polarizada.)",
           notas="El cálculo del 12,5 % usa la ley de Malus (cos²), que la guía no presenta; "
                 "es opcional.", **COMUN)
def _():
    sin_intermedia = fraccion_no_polarizada() * cos(pi / 2)**2
    con_intermedia = fraccion_no_polarizada() * cos(pi / 4)**2 * cos(pi / 4)**2
    assert sin_intermedia == 0 and simplify(con_intermedia - Q(1, 8)) == 0


manuales(EJ, [
    (48, "30", r"¿Por qué la holografía práctica tuvo que esperar a la llegada del láser?",
     r"Porque un holograma requiere luz coherente, de una sola frecuencia y con todas sus partes "
     r"en fase, y solo el láser la produce con facilidad; con luz blanca las bandas de "
     r"interferencia de unas frecuencias taparían las de otras."),
    (49, "31", r"¿Cómo se obtienen las ampliaciones con los hologramas?",
     r"Grabando el holograma con luz de longitud de onda corta y observándolo con luz de "
     r"longitud de onda mayor; la imagen se amplía en la proporción entre las dos longitudes de "
     r"onda."),
    (50, "32", r"¿Cuál de los siguientes fenómenos es más fundamental para la holografía: "
               r"interferencia, reflexión selectiva, refracción o todos los anteriores?",
     r"La interferencia: el holograma es el registro de un patrón de interferencia."),
], tipo="conceptual", dificultad=2)
