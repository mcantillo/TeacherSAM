"""Banco de ejercicios — Física 9° — Propiedades de la luz.
Fuente: Guía de Apoyo de Física 9° (ondas, sonido y luz), Capítulo 3 «Propiedades de la luz»:
Preguntas de repaso, Ejercicios y Problemas. Se lee en
recursos/fisica/Guías pedagógicas Física/markdown/09 - Guia_de_Apoyo_Conceptos_ondas_de_sonido_y_de_luz_grado_9_fisica.md
Alineación: Estándares 8°–9° (dba/naturales/estandares-fisica.md) — «Reconozco y diferencio
modelos para explicar la naturaleza y el comportamiento de la luz». Los problemas de tiempo de
viaje de la luz (distancia = rapidez × tiempo) se marcan también con el DBA 1 de 9°.
No incluidos: los «Examínate» (ya traen su respuesta en la guía) y las ilusiones ópticas
(dependen de las imágenes 24–26).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/fisica/luz-9.py
"""
from sympy import Rational as Q, simplify
from sympy.physics.units import (convert_to, hertz, kelvin, kilogram, meter, minute, second,
                                 year)

from ejercicios import ejercicio, ejercicio_manual

P = "luz-9"
GUIA = "Guía de Apoyo Física 9° (ondas, sonido y luz), Cap. 3 Propiedades de la luz"
COMUN = dict(tema="propiedades de la luz", grados=[9], dba=[])
VIAJE = dict(tema="propiedades de la luz", grados=[9], dba=["naturales-9-1"])
C_LUZ = 3 * 10**8 * meter / second        # valor que usa la guía (300 000 km/s)
V_SON = 340 * meter / second
NM = meter / 10**9


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
    (1, "1", r"¿Qué induce un campo magnético que varía?", r"Un campo eléctrico."),
    (2, "2", r"¿Qué induce un campo eléctrico que varía?", r"Un campo magnético."),
    (3, "3", r"¿Qué produce una onda electromagnética?",
     r"Una carga eléctrica que vibra (acelera), por lo general un electrón."),
    (4, "4", r"¿Por qué, según la conservación de la energía, una onda electromagnética en el "
             r"espacio nunca desacelera?",
     r"Si se frenara, su campo eléctrico cambiante induciría un campo magnético más débil, este "
     r"un campo eléctrico más débil, y así sucesivamente: la onda se extinguiría y su energía "
     r"desaparecería sin transferirse a nada, lo que contradice la conservación de la energía."),
    (5, "5", r"¿Por qué, según la conservación de la energía, una onda electromagnética en el "
             r"espacio nunca acelera?",
     r"Si acelerara, los campos inducidos serían cada vez más intensos y la energía de la onda "
     r"crecería sin que nada la aportara: también violaría la conservación de la energía. Solo "
     r"con la rapidez $c$ la inducción mutua se mantiene sin ganar ni perder energía."),
    (6, "6", r"¿Qué contienen y transportan los campos eléctricos y magnéticos?",
     r"Energía."),
    (7, "7", r"¿Cuál es la diferencia principal entre una onda de radio y la luz visible? ¿Y entre "
             r"la luz visible y un rayo X?",
     r"La frecuencia (y, con ella, la longitud de onda): la onda de radio tiene una frecuencia "
     r"mucho menor que la luz visible, y el rayo X una frecuencia mucho mayor. Las tres son ondas "
     r"electromagnéticas que viajan a la misma rapidez en el vacío."),
    (8, "8", r"¿Qué parte o cuánto del espectro electromagnético medido ocupa la luz visible?",
     r"Menos de la millonésima parte del $1\,\%$."),
    (9, "9", r"¿Qué color tiene la luz visible de las frecuencias mínimas visibles? ¿Y en las "
             r"frecuencias máximas?",
     r"Rojo en las mínimas; violeta en las máximas."),
    (10, "10", r"¿Cómo se compara la frecuencia de una onda de radio con la de los electrones "
               r"vibratorios que la producen?",
     r"Es la misma."),
    (11, "11", r"¿Cómo se relaciona la longitud de onda de la luz visible con su frecuencia?",
     r"De forma inversa: a mayor frecuencia, menor longitud de onda ($\lambda = c/f$)."),
], tipo="conceptual", dificultad=1)


@ejercicio(id=f"{P}-012", tipo="calculo", dificultad=1, fuente=fuente(REPASO, "12"),
           enunciado=r"¿Cuál es la longitud de una onda cuya frecuencia es de $1\,\text{Hz}$ y se "
                     r"propaga a $\num{300000}\,\text{km/s}$?",
           respuesta=r"$\lambda = \dfrac{v}{f} = \num{300000}\,\text{km}$: en un segundo se genera "
                     r"una sola onda, que avanza \num{300000} km.", **COMUN)
def _():
    assert convert_to(C_LUZ / (1 * hertz), meter) == 300000 * 1000 * meter


manuales(REPASO, [
    (13, "13", r"¿En qué sentido decimos que el espacio exterior en realidad no está vacío?",
     r"En que está lleno de radiación electromagnética (luz, ondas de radio, microondas…) que lo "
     r"atraviesa en todas direcciones."),
    (14, "14", r"El sonido que proviene de un diapasón puede hacer que otro diapasón vibre. ¿Cuál "
               r"es el efecto análogo en la luz?",
     r"La resonancia de los electrones de un material: la luz de cierta frecuencia pone a "
     r"vibrar con gran amplitud a los electrones cuya frecuencia natural es la misma (así ocurre "
     r"con la luz ultravioleta en el vidrio)."),
    (15, "15", r"¿En qué región del espectro electromagnético está la frecuencia de resonancia de "
               r"los electrones en el vidrio?",
     r"En el ultravioleta."),
    (16, "16", r"¿Cuál es el destino de la energía en la luz ultravioleta que incide en un vidrio?",
     r"Se absorbe y, por los choques entre átomos, se convierte en calor (energía interna del "
     r"vidrio)."),
    (17, "17", r"¿Cuál es el destino de la energía en la luz visible que incide en un vidrio?",
     r"Los electrones la reemiten como luz de la misma frecuencia, que atraviesa el vidrio "
     r"(el vidrio es transparente a la luz visible)."),
    (18, "18", r"¿Cómo se compara la frecuencia de la luz reemitida en un material transparente "
               r"con la de la luz que estimula la reemisión?",
     r"Es idéntica."),
    (19, "19", r"¿Cómo se compara la rapidez promedio de la luz en el vidrio con su rapidez en el "
               r"vacío?",
     r"Es menor: más o menos $\num{0,67}\,c$, según la clase de vidrio."),
    (20, "20", r"¿Por qué a las ondas infrarrojas se les llama con frecuencia ondas de calor?",
     r"Porque hacen vibrar átomos y moléculas completos, lo que aumenta la energía interna y la "
     r"temperatura de los materiales."),
    (21, "21", r"¿Por qué los materiales se calientan cuando los ilumina la luz?",
     r"Porque las vibraciones que la luz produce en sus átomos y moléculas se convierten en "
     r"energía cinética desordenada, es decir, en energía interna."),
    (22, "22", r"¿Por qué los metales son brillantes?",
     r"Porque sus electrones externos están libres: la luz los pone a vibrar y ellos la reemiten "
     r"hacia afuera (la reflejan) en vez de pasarla de átomo en átomo."),
    (23, "23", r"¿Por qué los objetos mojados se ven normalmente más oscuros que los objetos "
               r"secos?",
     r"Porque en la superficie mojada la luz rebota varias veces dentro de la capa de agua antes "
     r"de salir, y en cada rebote se absorbe parte de ella."),
    (24, "24", r"Describe la diferencia entre sombra (umbra) y penumbra.",
     r"La umbra es la sombra total, donde no llega ninguna luz de la fuente; la penumbra es la "
     r"sombra parcial que la rodea, donde llega parte de la luz."),
    (25, "25", r"¿La Tierra y la Luna siempre producen sombras? ¿Qué se produce cuando una pasa por "
               r"la sombra de la otra?",
     r"Sí, siempre proyectan sombra del lado opuesto al Sol. Cuando una pasa por la sombra de la "
     r"otra se produce un eclipse (lunar si la Luna entra en la sombra de la Tierra, solar si la "
     r"sombra de la Luna cae sobre la Tierra)."),
    (26, "26", r"Explica la diferencia entre los bastones y los conos del ojo, y entre sus "
               r"funciones.",
     r"Los bastones son muy sensibles a la luz débil y al movimiento, no distinguen colores y "
     r"predominan en la periferia de la retina. Los conos necesitan más luz, permiten ver los "
     r"colores (hay tres clases, para frecuencias bajas, intermedias y altas) y se concentran en "
     r"la fóvea."),
], tipo="conceptual", dificultad=1)

# ---------------------------------------------------------------- Ejercicios
EJ = "Ejercicios"
manuales(EJ, [
    (27, "1", r"Un amigo te dice, de forma enfática, que la luz es lo único que podemos ver. ¿Está "
              r"en lo correcto?",
     r"Sí: vemos los objetos solo por la luz que emiten o reflejan y que llega a nuestros ojos."),
    (28, "2", r"Además, tu amigo dice que la luz se produce por la conexión entre la electricidad "
              r"y el magnetismo. ¿Está en lo correcto?",
     r"Sí: la luz es una onda electromagnética, formada por campos eléctricos y magnéticos que "
     r"se regeneran mutuamente."),
    (29, "3", r"¿Cuál es la fuente fundamental de radiación electromagnética?",
     r"Las cargas eléctricas aceleradas (electrones que vibran)."),
    (30, "4", r"¿Cuáles tienen la mayor longitud de onda: la luz visible, los rayos X o las ondas "
              r"de radio?",
     r"Las ondas de radio."),
    (31, "5", r"¿Cuál tiene longitudes de onda más cortas, la ultravioleta o la infrarroja? ¿Cuál "
              r"tiene las mayores frecuencias?",
     r"La ultravioleta tiene las longitudes de onda más cortas y las mayores frecuencias."),
    (32, "6", r"¿Cómo es posible tomar fotografías en la oscuridad completa?",
     r"Con cámaras sensibles a la radiación infrarroja, que emiten todos los cuerpos tibios "
     r"(personas, animales, motores) aunque no haya luz visible."),
    (33, "7", r"Exactamente, ¿qué es lo que ondula en una onda luminosa?",
     r"Los campos eléctrico y magnético."),
    (34, "8", r"Se escucha a las personas hablar de la «luz ultravioleta» y de la «luz "
              r"infrarroja». ¿Por qué son engañosos esos términos? ¿Por qué es menos probable "
              r"escuchar acerca de la «luz de radio» y de la «luz de rayos X»?",
     r"Porque «luz» suele significar lo que vemos, y el ultravioleta y el infrarrojo no son "
     r"visibles (aunque son de la misma naturaleza electromagnética). Las ondas de radio y los "
     r"rayos X están mucho más lejos de la parte visible del espectro, así que casi nadie los "
     r"llama «luz»."),
    (35, "9", r"Sabiendo que el espacio interplanetario consiste en vacío, ¿cuál es tu evidencia "
              r"de que las ondas electromagnéticas pueden viajar por el vacío?",
     r"La luz del Sol y de las estrellas llega hasta nosotros atravesando el espacio vacío."),
    (36, "10", r"¿Cuál es la principal diferencia entre un rayo gamma y un rayo infrarrojo?",
     r"La frecuencia (y la longitud de onda): el rayo gamma tiene una frecuencia muchísimo mayor "
     r"y una longitud de onda muchísimo menor."),
], tipo="conceptual", dificultad=2)


@ejercicio(id=f"{P}-037", tipo="conceptual", dificultad=1, fuente=fuente(EJ, "11"),
           enunciado=r"¿Cuál es la rapidez de los rayos X en el vacío?",
           respuesta=r"La rapidez de la luz, $c = \num{300000}\,\text{km/s} = "
                     r"\num{3e8}\,\text{m/s}$, como toda onda electromagnética.", **COMUN)
def _():
    assert convert_to(C_LUZ, 1000 * meter / second) == 300000 * (1000 * meter / second)


manuales(EJ, [
    (38, "12", r"¿Qué viaja con mayor rapidez en el vacío, un rayo infrarrojo o un rayo gamma?",
     r"Ninguno: en el vacío todas las ondas electromagnéticas viajan con la misma rapidez $c$."),
    (39, "13", r"Tu amigo te dice que cualquier onda de radio viaja considerablemente más rápido "
               r"que cualquier onda sonora. ¿Estás de acuerdo con él? ¿Por qué?",
     r"Sí. Las ondas de radio viajan a unos $\num{3e8}\,\text{m/s}$, mientras que el sonido, "
     r"incluso en los sólidos, viaja a unos pocos miles de metros por segundo."),
    (40, "14", r"Tu amigo te dice que el espacio exterior, en vez de estar vacío, está abarrotado "
               r"de ondas electromagnéticas. ¿Estás de acuerdo con él? ¿Por qué?",
     r"Sí: por todas partes lo atraviesan radiaciones de las estrellas, ondas de radio y el "
     r"fondo cósmico de microondas, aunque no haya materia."),
    (41, "15", r"Las señales de longitud de onda de radio y televisión, ¿son más largas o más "
               r"cortas que las ondas detectables por el ojo humano?",
     r"Más largas (tienen menor frecuencia que la luz visible)."),
], tipo="conceptual", dificultad=2)


@ejercicio(id=f"{P}-042", tipo="conceptual", dificultad=2, fuente=fuente(EJ, "16"),
           enunciado=r"Imagina que una onda luminosa y una sonora tienen la misma frecuencia. "
                     r"¿Cuál tiene la mayor longitud de onda?",
           respuesta=r"La luminosa: con la misma frecuencia, $\lambda = v/f$ es proporcional a la "
                     r"rapidez, y la luz es casi un millón de veces más rápida que el sonido.",
           **COMUN)
def _():
    assert simplify((C_LUZ / (500 * hertz)) / (V_SON / (500 * hertz))) > 800000


manuales(EJ, [
    (43, "17", r"¿Las ondas de radio se propagan a la rapidez del sonido, a la rapidez de la luz, "
               r"o a una rapidez intermedia?",
     r"A la rapidez de la luz: son ondas electromagnéticas."),
    (44, "18", r"Cuando los astrónomos observan una explosión de supernova en una galaxia lejana, "
               r"lo que ven es un aumento repentino y simultáneo en la luz visible y en otras "
               r"formas de radiación electromagnética. ¿Eso es una prueba que respalde la idea de "
               r"que la rapidez de la luz es independiente de la frecuencia? Explica por qué.",
     r"Sí. Todas las radiaciones salieron al mismo tiempo y recorrieron la misma distancia "
     r"enorme; si viajaran con rapideces distintas según la frecuencia, llegarían en momentos "
     r"distintos. Llegan juntas, así que viajan con la misma rapidez."),
    (45, "19", r"¿Qué es igual acerca de las ondas de radio y de luz visible? ¿Qué es diferente "
               r"acerca de ellas?",
     r"Iguales: ambas son ondas electromagnéticas, las producen cargas que vibran y viajan en el "
     r"vacío a la misma rapidez $c$. Diferentes: la frecuencia y la longitud de onda (la radio "
     r"tiene frecuencia mucho menor y longitud de onda mucho mayor)."),
], tipo="conceptual", dificultad=2)


@ejercicio(id=f"{P}-046", tipo="contexto", dificultad=2, fuente=fuente(EJ, "20"),
           enunciado=r"Un láser de helio-neón emite luz de $633\,\text{nm}$ de longitud de onda. La "
                     r"longitud de onda de un láser de argón es de $515\,\text{nm}$. ¿Cuál láser "
                     r"emite la luz de mayor frecuencia?",
           respuesta=r"El de argón: a menor longitud de onda, mayor frecuencia ($f = c/\lambda$; "
                     r"unos $\num{5,8e14}\,\text{Hz}$ frente a $\num{4,7e14}\,\text{Hz}$ del "
                     r"helio-neón).", **COMUN)
def _():
    argon, hene = convert_to(C_LUZ / (515 * NM), hertz), convert_to(C_LUZ / (633 * NM), hertz)
    assert argon > hene
    cerca(argon, Q(58, 10) * 10**14 * hertz, tol=0.01)
    cerca(hene, Q(47, 10) * 10**14 * hertz, tol=0.01)


manuales(EJ, [
    (47, "21", r"¿Por qué esperas que la rapidez de la luz sea un poco menor en la atmósfera que "
               r"en el vacío?",
     r"Porque en el aire hay moléculas que absorben y reemiten la luz, con pequeñas demoras en "
     r"cada interacción; por eso la rapidez promedio es un poco menor que $c$."),
    (48, "22", r"Si disparas una bala que atraviese un árbol, se desacelerará dentro del tronco y "
               r"saldrá a una rapidez menor que la rapidez con la que entró. Entonces, ¿la luz "
               r"también desacelera al pasar por el vidrio y sale con menor rapidez? Defiende tu "
               r"respuesta.",
     r"No. Dentro del vidrio su rapidez \emph{promedio} es menor por las demoras de absorción y "
     r"reemisión, pero entre átomo y átomo viaja a $c$, y la luz reemitida al salir al aire "
     r"vuelve a viajar a su rapidez original. No pierde energía como la bala."),
    (49, "23", r"¿El vidrio es transparente a luz de frecuencias que coinciden con sus propias "
               r"frecuencias naturales? Explica por qué.",
     r"No. Con esas frecuencias hay resonancia: los electrones vibran con gran amplitud, retienen "
     r"la energía y la pasan a los átomos vecinos como calor, en vez de reemitirla. El vidrio es "
     r"opaco a esas frecuencias (el ultravioleta)."),
    (50, "24", r"Las longitudes de onda cortas de la luz visible interactúan con más frecuencia "
               r"con los átomos en el vidrio que las de mayor longitud de onda. ¿Ese tiempo de "
               r"interacción tiende a aumentar o a disminuir la rapidez promedio de la luz en el "
               r"vidrio?",
     r"A disminuirla: la luz de longitud de onda corta (violeta, azul) viaja más despacio en el "
     r"vidrio que la de longitud de onda larga (roja)."),
    (51, "25", r"¿Qué determina si un material es transparente u opaco?",
     r"La relación entre la frecuencia de la luz y las frecuencias naturales de sus electrones y "
     r"moléculas: si la luz se reemite, el material es transparente a ella; si se absorbe y se "
     r"convierte en calor, es opaco."),
    (52, "26", r"Puedes resultar con quemaduras de sol en un día nublado, pero no te quemarás a "
               r"través de un vidrio, aunque el día esté muy soleado. ¿Por qué?",
     r"Porque las nubes son semitransparentes al ultravioleta, que causa las quemaduras, "
     r"mientras que el vidrio es opaco al ultravioleta."),
    (53, "27", r"Imagina que la luz solar incide en un par de anteojos para leer y un par de "
               r"anteojos oscuros para el sol. ¿Cuáles anteojos crees que se van a calentar más? "
               r"Defiende tu respuesta.",
     r"Los oscuros: absorben más luz y esa energía se convierte en energía interna; los "
     r"anteojos para leer dejan pasar casi toda la luz."),
    (54, "28", r"¿Por qué un avión que vuela muy alto casi no produce sombra, o no produce sombra "
               r"en el suelo; mientras que uno que vuele bajo produce una sombra bien definida?",
     r"Porque el Sol no es un punto: sus rayos llegan desde direcciones un poco distintas. Si el "
     r"avión está muy alto, la umbra no alcanza el suelo y solo llega una penumbra difusa; si "
     r"vuela bajo, la sombra cae cerca y es nítida."),
    (55, "29", r"Los eclipses lunares siempre son eclipses en luna llena. Esto es, la Luna siempre "
               r"está llena inmediatamente antes y después de que la sombra de la Tierra pasa "
               r"sobre ella. ¿Por qué? ¿Por qué nunca veremos un eclipse lunar cuando haya luna "
               r"creciente, menguante o nueva?",
     r"Porque la sombra de la Tierra está en el lado opuesto al Sol, y la Luna solo puede entrar "
     r"en ella cuando la Tierra queda entre el Sol y la Luna, que es justamente la posición de "
     r"luna llena. En las otras fases la Luna no está detrás de la Tierra."),
    (56, "30", r"¿Los planetas proyectan sombras? ¿Cómo lo compruebas?",
     r"Sí: todo cuerpo opaco iluminado por el Sol proyecta sombra. Lo comprobamos con la sombra "
     r"de la Tierra sobre la Luna en los eclipses lunares y con los eclipses de las lunas de "
     r"Júpiter cuando entran en la sombra del planeta."),
    (57, "31", r"¿Qué evento astronómico verían unos observadores en la Luna en el momento en que "
               r"en la Tierra se viera un eclipse lunar? ¿Y en el momento en que en la Tierra se "
               r"viera un eclipse solar?",
     r"Durante un eclipse lunar, desde la Luna se vería un eclipse de Sol: la Tierra tapando al "
     r"Sol. Durante un eclipse solar, desde la Luna se vería la pequeña sombra de la Luna "
     r"moviéndose como una mancha oscura sobre la Tierra."),
    (58, "32", r"La luz que procede de un lugar donde concentras tu atención llega a la fóvea, que "
               r"sólo contiene conos. Si deseas observar una fuente luminosa débil, por ejemplo "
               r"una estrella débil, ¿por qué no debes ver la fuente directamente?",
     r"Porque los conos necesitan más luz para activarse. Mirando un poco al lado, la luz de la "
     r"estrella cae en la periferia de la retina, donde están los bastones, más sensibles a la "
     r"luz débil."),
    (59, "33", r"¿Por qué les falta color a los objetos iluminados por la luz de la Luna?",
     r"Porque la luz de la Luna es tan débil que solo activa los bastones, que no distinguen "
     r"colores."),
    (60, "34", r"¿Por qué no vemos colores en la periferia de nuestra visión?",
     r"Porque en la periferia de la retina casi no hay conos, que son los que perciben el color; "
     r"predominan los bastones."),
    (61, "35", r"La intensidad de la luz disminuye de acuerdo con el inverso del cuadrado de la "
               r"distancia a la fuente. ¿Quiere decir eso que se pierde la energía luminosa? "
               r"Explica por qué.",
     r"No. La energía no se pierde: se reparte sobre una superficie cada vez mayor (una esfera "
     r"cuya área crece con el cuadrado del radio), así que a cada unidad de área le llega menos."),
    (62, "36", r"La luz de una lámpara de destello en fotografía se debilita al aumentar la "
               r"distancia, siguiendo la ley del inverso del cuadrado. Comenta acerca de un "
               r"pasajero que toma una foto panorámica desde un avión que vuela muy alto sobre "
               r"una ciudad, usando su flash.",
     r"El flash no sirve de nada: a esa distancia, la luz que llega hasta la ciudad y regresa "
     r"es insignificante. Solo ilumina la ventanilla (y produce un reflejo en ella); la foto se "
     r"toma con la luz de la ciudad misma."),
    (63, "37", r"En los barcos la profundidad del mar se determina haciendo rebotar en él ondas de "
               r"sonar y midiendo el tiempo en el viaje de ida y vuelta. ¿Cómo se hace (en forma "
               r"parecida) en algunos aviones para determinar su distancia al suelo?",
     r"Con un radar (o un láser): envían ondas electromagnéticas hacia el suelo, miden el tiempo "
     r"$t$ que tarda el eco en volver y calculan la distancia $d = \dfrac{c\,t}{2}$."),
], tipo="conceptual", dificultad=2)


@ejercicio(id=f"{P}-064", tipo="calculo", dificultad=2, fuente=fuente(EJ, "38"),
           enunciado=r"El planeta Júpiter está más de cinco veces más alejado del Sol que la "
                     r"Tierra. ¿Cómo aparece el brillo del Sol a esta mayor distancia?",
           respuesta=r"Mucho más débil: por la ley del inverso del cuadrado, a una distancia cinco "
                     r"veces mayor la intensidad es $\left(\tfrac{1}{5}\right)^2 = \tfrac{1}{25}$ "
                     r"de la que llega a la Tierra (y aún menos, porque la distancia es algo "
                     r"mayor que cinco veces).", **COMUN)
def _():
    assert Q(1, 5)**2 == Q(1, 25)
    assert Q(1, Q(52, 10)**2) < Q(1, 25)                 # Júpiter está a unas 5,2 UA


manuales(EJ, [
    (65, "39", r"Cuando ves el cielo nocturno, algunas estrellas brillan más que otras. ¿Puedes "
               r"decir correctamente que las estrellas más brillantes emiten más luz? Defiende tu "
               r"respuesta.",
     r"No necesariamente. El brillo que vemos depende de la luz que emite la estrella y de su "
     r"distancia (inverso del cuadrado): una estrella cercana puede verse más brillante que otra "
     r"más lejana aunque emita menos luz."),
], tipo="argumentacion", dificultad=2)

# ---------------------------------------------------------------- Problemas
PR = "Problemas"


@ejercicio(id=f"{P}-066", tipo="contexto", dificultad=3, fuente=fuente(PR, "1"),
           enunciado=r"En 1675 el astrónomo danés Olaus Roemer midió las horas de aparición de una "
                     r"de las lunas de Júpiter y notó que se demoraban a medida que la Tierra se "
                     r"alejaba de Júpiter; concluyó que la luz tarda 22 minutos adicionales en "
                     r"recorrer los \num{300000000} km del diámetro de la órbita de la Tierra "
                     r"alrededor del Sol. ¿Qué valor aproximado de la rapidez de la luz calculó "
                     r"Roemer con esos datos? ¿En cuánto se diferencia del valor moderno?",
           respuesta=r"$v = \dfrac{\num{3e11}\,\text{m}}{22 \times 60\,\text{s}} \approx "
                     r"\num{2,3e8}\,\text{m/s}$. Es unos $\num{0,7e8}\,\text{m/s}$ menor que el "
                     r"valor moderno, $\num{3e8}\,\text{m/s}$ (alrededor de un $24\,\%$ menos).",
           **VIAJE)
def _():
    v = 300000000 * 1000 * meter / (22 * minute)
    cerca(v, Q(23, 10) * 10**8 * meter / second, tol=0.02)
    diferencia = convert_to(C_LUZ - v, meter / second)
    cerca(diferencia, Q(7, 10) * 10**8 * meter / second, tol=0.05)
    assert abs(float(simplify(convert_to(v, meter / second) / C_LUZ)) - 0.76) < 0.01


@ejercicio(id=f"{P}-067", tipo="contexto", dificultad=2, fuente=fuente(PR, "2"),
           enunciado=r"En uno de los experimentos de Michelson, un haz procedente de un espejo "
                     r"giratorio recorrió $15\,\text{km}$ hasta un espejo estacionario. ¿Cuánto "
                     r"tiempo pasó para que regresara al espejo giratorio?",
           respuesta=r"Recorre $30\,\text{km}$ (ida y vuelta): $t = \dfrac{\num{3e4}\,\text{m}}"
                     r"{\num{3e8}\,\text{m/s}} = \num{1e-4}\,\text{s} = \num{0,1}\,\text{ms}$.",
           **VIAJE)
def _():
    assert convert_to(2 * 15000 * meter / C_LUZ, second) == Q(1, 10000) * second


@ejercicio(id=f"{P}-068", tipo="contexto", dificultad=2, fuente=fuente(PR, "3"),
           enunciado=r"El Sol está a $\num{1,50e11}\,\text{m}$ de la Tierra. ¿Cuánto tarda la luz "
                     r"del Sol en llegar a la Tierra? ¿Cuánto tarda en cruzar el diámetro de la "
                     r"órbita de la Tierra? Compara tu resultado con el tiempo que midió Roemer en "
                     r"el siglo XVII (22 minutos, problema 1).",
           respuesta=r"$t = \dfrac{\num{1,5e11}\,\text{m}}{\num{3e8}\,\text{m/s}} = "
                     r"500\,\text{s} \approx \num{8,3}\,\text{min}$. El diámetro de la órbita "
                     r"($\num{3e11}\,\text{m}$) lo cruza en $\num{1000}\,\text{s} \approx "
                     r"\num{16,7}\,\text{min}$: Roemer midió unos 5 minutos de más.",
           notas="En la guía la potencia aparece como «1,50 × 10 11»; se escribe 1,50·10^11.",
           **VIAJE)
def _():
    t1 = convert_to(Q(15, 10) * 10**11 * meter / C_LUZ, second)
    assert t1 == 500 * second
    t2 = convert_to(2 * t1, minute)
    cerca(t2, Q(167, 10) * minute, tol=0.002)
    cerca(22 * minute - t2, 5 * minute, tol=0.07)


@ejercicio(id=f"{P}-069", tipo="contexto", dificultad=2, fuente=fuente(PR, "4"),
           enunciado=r"¿Cuánto tarda un impulso de luz láser en llegar a la Luna, reflejarse y "
                     r"llegar a la Tierra? (Distancia Tierra–Luna: $\num{3,84e8}\,\text{m}$.)",
           respuesta=r"$t = \dfrac{2 \times \num{3,84e8}\,\text{m}}{\num{3e8}\,\text{m/s}} "
                     r"\approx \num{2,56}\,\text{s}$.",
           notas="La guía no da la distancia Tierra–Luna; se añade 3,84·10^8 m.", **VIAJE)
def _():
    assert convert_to(2 * Q(384, 100) * 10**8 * meter / C_LUZ, second) == Q(256, 100) * second


@ejercicio(id=f"{P}-070", tipo="contexto", dificultad=2, fuente=fuente(PR, "5"),
           enunciado=r"La estrella más cercana, aparte de nuestro Sol, es Alfa Centauri, que está a "
                     r"$\num{4,2e16}\,\text{m}$ de distancia. Si hoy recibiéramos un mensaje de "
                     r"radio emitido desde esa estrella, ¿hace cuánto se habría enviado?",
           respuesta=r"$t = \dfrac{\num{4,2e16}\,\text{m}}{\num{3e8}\,\text{m/s}} = "
                     r"\num{1,4e8}\,\text{s}$, unos $\num{4,4}$ años.",
           notas="En la guía: «Alpha Centauri» y la potencia escrita «4,2 × 10 16».", **VIAJE)
def _():
    t = convert_to(Q(42, 10) * 10**16 * meter / C_LUZ, second)
    assert t == 140000000 * second
    cerca(t, Q(44, 10) * year, tol=0.01)


@ejercicio(id=f"{P}-071", tipo="calculo", dificultad=2, fuente=fuente(PR, "6"),
           enunciado=r"La longitud de onda de la luz amarilla del sodio, en el aire, es "
                     r"$589\,\text{nm}$. ¿Cuál es su frecuencia?",
           respuesta=r"$f = \dfrac{c}{\lambda} = \dfrac{\num{3e8}\,\text{m/s}}"
                     r"{\num{5,89e-7}\,\text{m}} \approx \num{5,1e14}\,\text{Hz}$.", **COMUN)
def _():
    cerca(C_LUZ / (589 * NM), Q(51, 10) * 10**14 * hertz, tol=0.005)


@ejercicio(id=f"{P}-072", tipo="contexto", dificultad=3, fuente=fuente(PR, "7"),
           enunciado=r"La longitud de onda de la luz cambia al pasar de un medio a otro, mientras "
                     r"que la frecuencia permanece constante. ¿La longitud de onda es mayor o menor "
                     r"en el agua que en el aire? Explícalo en términos de la ecuación "
                     r"rapidez $=$ frecuencia $\times$ longitud de onda. Una luz amarillo-verdosa "
                     r"tiene $600\,\text{nm}$ ($\num{6e-7}\,\text{m}$) de longitud de onda en el "
                     r"aire. ¿Cuál es su longitud de onda en el agua, donde la luz se propaga al "
                     r"$75\,\%$ de su rapidez en el aire? ¿Y en plexiglás, donde se propaga al "
                     r"$67\,\%$ de su rapidez en el aire?",
           respuesta=r"Menor: la frecuencia no cambia y $\lambda = v/f$, así que si la rapidez "
                     r"baja, la longitud de onda baja en la misma proporción. En el agua: "
                     r"$\num{0,75} \times 600\,\text{nm} = 450\,\text{nm}$; en plexiglás: "
                     r"$\num{0,67} \times 600\,\text{nm} \approx 400\,\text{nm}$ "
                     r"(\num{402} nm).", **COMUN)
def _():
    f_luz = C_LUZ / (600 * NM)                          # frecuencia, igual en los tres medios
    agua = convert_to(Q(75, 100) * C_LUZ / f_luz, meter)
    plexi = convert_to(Q(67, 100) * C_LUZ / f_luz, meter)
    assert agua == 450 * NM and plexi == 402 * NM
    assert agua < 600 * NM


@ejercicio(id=f"{P}-073", tipo="calculo", dificultad=2, fuente=fuente(PR, "8a"),
           enunciado=r"Determinada instalación de radar se usa para rastrear los aviones y transmite "
                     r"radiación electromagnética de $3\,\text{cm}$ de longitud de onda. ¿Cuál es "
                     r"la frecuencia de esta radiación, medida en miles de millones de hertz "
                     r"(GHz)?",
           respuesta=r"$f = \dfrac{\num{3e8}\,\text{m/s}}{\num{0,03}\,\text{m}} = "
                     r"\num{1e10}\,\text{Hz} = 10\,\text{GHz}$.", **COMUN)
def _():
    assert convert_to(C_LUZ / (Q(3, 100) * meter), hertz) == 10 * 10**9 * hertz


@ejercicio(id=f"{P}-074", tipo="contexto", dificultad=2, fuente=fuente(PR, "8b"),
           enunciado=r"¿Cuál es el tiempo necesario para que un impulso de ondas de radar llegue a "
                     r"un avión que está a $5\,\text{km}$ de distancia y regrese?",
           respuesta=r"$t = \dfrac{2 \times \num{5000}\,\text{m}}{\num{3e8}\,\text{m/s}} \approx "
                     r"\num{3,3e-5}\,\text{s}$ (unos $33$ microsegundos).", **VIAJE)
def _():
    t = convert_to(2 * 5000 * meter / C_LUZ, second)
    assert t == Q(1, 30000) * second
    cerca(t, Q(33, 10) * 10**-5 * second, tol=0.02)
