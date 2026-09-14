"""Banco de ejercicios — Física 9° — Vibraciones y ondas.
Fuente: Guía de Apoyo de Física 9° (ondas, sonido y luz), Capítulo 1 «Vibraciones y ondas»:
Preguntas de repaso, Ejercicios y Problemas. Se lee en
recursos/fisica/Guías pedagógicas Física/markdown/09 - Guia_de_Apoyo_Conceptos_ondas_de_sonido_y_de_luz_grado_9_fisica.md
Alineación: los DBA de física de 9° (dba/naturales/grados/grado09.tex) solo tienen el DBA 1
(movimiento); las ondas corresponden a los Estándares 8°–9° (dba/naturales/estandares-fisica.md):
«Establezco relaciones entre frecuencia, amplitud, velocidad de propagación y longitud de onda en
diversos tipos de ondas mecánicas». Por eso el campo dba va vacío salvo donde el ejercicio es de
movimiento uniforme.
No incluidos: los «Examínate» (ya traen su respuesta en la guía) y los Proyectos 1–3
(actividades prácticas y una carta).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/fisica/ondas-9.py
"""
from sympy import Rational as Q, simplify, symbols
from sympy.physics.units import (convert_to, hertz, hour, kelvin, kilogram, meter,
                                 minute, second)

from ejercicios import ejercicio, ejercicio_manual

P = "ondas-9"
GUIA = "Guía de Apoyo Física 9° (ondas, sonido y luz), Cap. 1 Vibraciones y ondas"
COMUN = dict(tema="vibraciones y ondas", grados=[9], dba=[])
C_LUZ = 3 * 10**8 * meter / second        # valor que usa la guía (300 000 km/s)
V_SON = 340 * meter / second              # sonido en el aire a unos 20 °C (guía, cap. 2)


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


f, T, lam, v = symbols("f T lambda v", positive=True)

# ---------------------------------------------------------------- Preguntas de repaso
REPASO = "Preguntas de repaso"
manuales(REPASO, [
    (1, "1", r"¿Cómo se llama un vaivén en el tiempo? ¿Y un vaivén en el espacio y en el tiempo?",
     r"Un vaivén en el tiempo es una \textbf{vibración} (oscilación); un vaivén en el espacio y "
     r"en el tiempo es una \textbf{onda}."),
    (2, "2", r"¿Cuál es la fuente de todas las ondas?",
     r"Algo que vibra: toda onda se origina en un objeto (o una carga) en vibración."),
    (3, "3", r"¿Qué quiere decir periodo de un péndulo?",
     r"Es el tiempo que tarda el péndulo en hacer una oscilación completa de ida y vuelta."),
    (4, "4", r"¿Qué tiene mayor periodo, un péndulo corto o uno largo?",
     r"El péndulo largo: cuanto mayor es la longitud, mayor es el periodo."),
    (5, "5", r"¿En qué se relaciona una senoide con una onda?",
     r"La senoide es la representación gráfica de una onda: es la curva que traza un objeto con "
     r"movimiento armónico simple (un péndulo o una masa en un resorte) sobre una banda que avanza "
     r"con rapidez constante; en ella se ven las crestas, los valles, la amplitud y la longitud "
     r"de onda."),
    (6, "6", r"Describe lo siguiente acerca de las ondas: periodo, amplitud, longitud de onda y "
             r"frecuencia.",
     r"\emph{Periodo}: tiempo que tarda una vibración completa. \emph{Amplitud}: desplazamiento "
     r"máximo desde la posición de equilibrio (del punto medio a una cresta o a un valle). "
     r"\emph{Longitud de onda}: distancia entre dos crestas sucesivas (o entre dos partes "
     r"idénticas sucesivas). \emph{Frecuencia}: número de vibraciones por unidad de tiempo; se "
     r"mide en hertz ($1\,\text{Hz} = 1$ vibración por segundo)."),
], tipo="conceptual", dificultad=1)


@ejercicio(id=f"{P}-007", tipo="calculo", dificultad=1, fuente=fuente(REPASO, "7"),
           enunciado=r"¿Cuántas vibraciones por segundo representa una onda de radio de "
                     r"$\num{101,7}\,\text{MHz}$?",
           respuesta=r"$\num{101,7}\,\text{MHz} = \num{101700000}\,\text{Hz}$: "
                     r"\num{101700000} vibraciones por segundo.",
           notas="En la guía: «101.7 MHz» con punto decimal; se escribe con coma.", **COMUN)
def _():
    assert convert_to(Q(1017, 10) * (10**6 * hertz), 1 / second) == 101700000 / second


manuales(REPASO, [
    (8, "8", r"¿Cómo se relacionan entre sí frecuencia y periodo?",
     r"Son recíprocos: $f = \dfrac{1}{T}$ y $T = \dfrac{1}{f}$. Si uno aumenta, el otro "
     r"disminuye."),
    (9, "9", r"En una palabra, ¿qué es lo que se mueve de la fuente al receptor en el movimiento "
             r"ondulatorio?",
     r"Energía."),
    (10, "10", r"¿El medio en el cual se propaga una onda se mueve con ella? Describe un ejemplo "
               r"que respalde tu respuesta.",
     r"No. Cada parte del medio solo oscila alrededor de su posición y regresa a ella; lo que "
     r"viaja es la perturbación. Ejemplo: una hoja que flota en un estanque sube y baja cuando "
     r"pasan las ondas, pero termina donde estaba (igual que el césped que se mece con el "
     r"viento sin moverse de su lugar)."),
    (11, "11", r"¿Cuál es la relación entre frecuencia, longitud de onda y rapidez de onda?",
     r"Rapidez de la onda $=$ longitud de onda $\times$ frecuencia: $v = \lambda f$."),
    (12, "12", r"¿Qué dirección tienen las vibraciones en relación con la dirección de "
               r"propagación de una onda transversal?",
     r"Perpendicular (forman un ángulo recto con la dirección en que viaja la onda)."),
    (13, "13", r"¿Qué dirección tienen las vibraciones en relación con la dirección de "
               r"propagación de una onda longitudinal?",
     r"La misma dirección (paralela) en la que se propaga la onda."),
    (14, "14", r"La longitud de onda en una onda transversal es la distancia entre crestas (o "
               r"valles) sucesivas. ¿Cuál es la longitud de onda en una onda longitudinal?",
     r"La distancia entre dos compresiones sucesivas (o entre dos rarefacciones sucesivas)."),
    (15, "15", r"¿Qué entendemos por principio de superposición?",
     r"Cuando dos o más ondas ocupan el mismo lugar al mismo tiempo, el desplazamiento en cada "
     r"punto es la suma de los desplazamientos que produciría cada onda por separado."),
    (16, "16", r"Explica la diferencia entre interferencia constructiva e interferencia "
               r"destructiva.",
     r"En la constructiva se encuentran cresta con cresta (o valle con valle) y los efectos se "
     r"suman: la amplitud resultante es mayor. En la destructiva se encuentra la cresta de una "
     r"onda con el valle de otra y los efectos se restan: la amplitud disminuye o se anula."),
    (17, "17", r"¿Qué clase de ondas pueden mostrar interferencia?",
     r"Todas: ondas en el agua, sonoras y luminosas, tanto transversales como longitudinales."),
    (18, "18", r"¿Qué es un nodo? ¿Qué es un antinodo?",
     r"En una onda estacionaria, un nodo es un punto que permanece quieto (desplazamiento mínimo "
     r"o cero); un antinodo es un punto de desplazamiento máximo, a mitad de camino entre dos "
     r"nodos."),
    (19, "19", r"¿Las ondas estacionarias pertenecen a las ondas transversales, a las "
               r"longitudinales o a ambas?",
     r"A ambas: se forman en cuerdas (transversales) y en el aire de tubos y botellas "
     r"(longitudinales)."),
    (20, "20", r"¿En el efecto Doppler cambia la frecuencia? ¿Cambia la longitud de onda? "
               r"¿Cambia la rapidez de la onda?",
     r"Cambia la frecuencia que recibe el observador. Cuando la fuente se mueve también cambia "
     r"la longitud de onda (más corta delante de la fuente, más larga detrás). La rapidez de la "
     r"onda no cambia: depende del medio, no del movimiento de la fuente."),
    (21, "21", r"¿Puede observarse el efecto Doppler en las ondas longitudinales, en las ondas "
               r"transversales o en ambas?",
     r"En ambas: se observa en el sonido (longitudinal) y en la luz (transversal)."),
    (22, "22", r"¿Qué significa corrimiento hacia el azul y corrimiento hacia el rojo de la luz?",
     r"Corrimiento al azul: aumento de la frecuencia de la luz recibida porque la fuente se "
     r"acerca (hacia el extremo azul del espectro). Corrimiento al rojo: disminución de la "
     r"frecuencia porque la fuente se aleja (hacia el extremo rojo)."),
    (23, "23", r"¿Con qué rapidez debe nadar un insecto para emparejarse con las ondas que "
               r"produce? ¿Con qué rapidez debe nadar para producir una onda de proa?",
     r"Para emparejarse, con la misma rapidez que las ondas; para producir una onda de proa, con "
     r"una rapidez mayor que la de las ondas."),
    (24, "24", r"¿Cuál es la rapidez con que avanza un avión supersónico, en comparación con la "
               r"del sonido?",
     r"Mayor que la rapidez del sonido."),
    (25, "25", r"¿Cómo varía la forma en V de una onda de proa, en función de la rapidez de la "
               r"fuente?",
     r"Cuanto más rápida es la fuente (por encima de la rapidez de las ondas), más angosta es la "
     r"V."),
    (26, "26", r"Una onda de proa sobre la superficie del agua es bidimensional. ¿Y una onda de "
               r"choque en el aire?",
     r"Es tridimensional: tiene forma de cono."),
    (27, "27", r"¿Cierto o falso? El estampido sónico sólo se produce cuando un avión rompe la "
               r"barrera del sonido. Defiende tu respuesta.",
     r"Falso. Mientras el avión vuele más rápido que el sonido lleva consigo la onda de choque, "
     r"que barre continuamente el suelo; cada persona oye el estampido cuando el cono pasa por "
     r"donde ella está, aunque el avión haya superado la rapidez del sonido minutos antes."),
    (28, "28", r"Para producir un estampido sónico un objeto debe ser «ruidoso». ¿Cierto o falso? "
               r"Da dos ejemplos que respalden tu respuesta.",
     r"Falso. Basta que se mueva más rápido que el sonido: una bala supersónica produce un "
     r"crujido y la punta de un látigo al restallar produce un pequeño estampido, aunque ninguno "
     r"de los dos es una fuente de sonido."),
], tipo="conceptual", dificultad=1)

# ---------------------------------------------------------------- Ejercicios
EJ = "Ejercicios"
manuales(EJ, [
    (29, "1", r"¿El periodo de un péndulo depende de la masa que cuelga de él? ¿Del largo de la "
              r"cuerda?",
     r"No depende de la masa; sí depende de la longitud de la cuerda: cuanto más larga, mayor "
     r"es el periodo (también depende de la aceleración de la gravedad)."),
    (30, "2", r"Una persona pesada y una liviana se balancean de un lado a otro en columpios de "
              r"la misma longitud. ¿Cuál de las dos tiene el mayor periodo?",
     r"Ninguna: tienen el mismo periodo, porque el periodo de un péndulo no depende de la masa."),
    (31, "3", r"Cierto reloj antiguo de péndulo funciona con mucha exactitud. A continuación se "
              r"pasa a una casa de veraneo, en unas montañas altas. ¿Se adelantará, se atrasará o "
              r"quedará igual? Explica por qué.",
     r"Se atrasará. En la montaña la aceleración de la gravedad es un poco menor, el péndulo "
     r"oscila más despacio (su periodo aumenta) y el reloj cuenta menos oscilaciones de las que "
     r"debería en cada hora."),
    (32, "4", r"Si se acorta un péndulo, ¿su frecuencia aumentará o disminuirá? ¿Y su periodo?",
     r"La frecuencia aumenta y el periodo disminuye."),
    (33, "5", r"Puedes hacer balancear una maleta vacía con su frecuencia natural. Si estuviera "
              r"llena de libros, ¿su frecuencia sería menor, mayor o igual que antes?",
     r"Igual (si los libros quedan repartidos de modo que el centro de masa no cambie de "
     r"lugar), porque la frecuencia de un péndulo no depende de la masa."),
    (34, "6", r"¿El tiempo necesario para oscilar y regresar (el periodo) de un columpio es mayor "
              r"o menor cuando te paras en él en vez de estar sentado? Explica por qué.",
     r"Menor. De pie, tu centro de masa sube y queda más cerca del punto de donde cuelga el "
     r"columpio: el péndulo efectivo es más corto y un péndulo más corto tiene menor periodo."),
    (35, "7", r"¿Por qué tiene sentido el hecho de que la masa que cuelga de un péndulo simple no "
              r"afecta la frecuencia de éste?",
     r"Porque la gravedad acelera igual a todos los cuerpos: una masa mayor recibe una fuerza "
     r"(peso) mayor, pero también tiene más inercia, y los dos efectos se compensan; por eso "
     r"dos péndulos de igual longitud oscilan al unísono."),
], tipo="conceptual", dificultad=2)


@ejercicio(id=f"{P}-036", tipo="conceptual", dificultad=1, fuente=fuente(EJ, "8"),
           enunciado=r"¿Qué sucede con el periodo de una onda cuando disminuye la frecuencia?",
           respuesta=r"Aumenta, porque $T = \dfrac{1}{f}$.", **COMUN)
def _():
    assert (1 / (f / 2)) / (1 / f) == 2          # si f se reduce a la mitad, T se duplica


@ejercicio(id=f"{P}-037", tipo="conceptual", dificultad=1, fuente=fuente(EJ, "9"),
           enunciado=r"¿Qué sucede con la longitud de onda cuando disminuye la frecuencia?",
           respuesta=r"Aumenta: en un mismo medio la rapidez no cambia y $\lambda = "
                     r"\dfrac{v}{f}$.", **COMUN)
def _():
    assert (v / (f / 2)) / (v / f) == 2


@ejercicio(id=f"{P}-038", tipo="conceptual", dificultad=1, fuente=fuente(EJ, "10"),
           enunciado=r"Si la rapidez de una onda se duplica mientras su frecuencia permanece "
                     r"constante, ¿qué sucede con la longitud de onda?",
           respuesta=r"Se duplica ($\lambda = v/f$).", **COMUN)
def _():
    assert ((2 * v) / f) / (v / f) == 2


@ejercicio(id=f"{P}-039", tipo="conceptual", dificultad=1, fuente=fuente(EJ, "11"),
           enunciado=r"Si la rapidez de una onda se duplica mientras la longitud de onda permanece "
                     r"constante, ¿qué sucede con la frecuencia?",
           respuesta=r"Se duplica ($f = v/\lambda$).", **COMUN)
def _():
    assert ((2 * v) / lam) / (v / lam) == 2


manuales(EJ, [
    (40, "12", r"Si sujetas un extremo de una segueta en un tornillo de banco y golpeas el "
               r"extremo libre, oscilará. Ahora repítelo, pero con una bola de arcilla o "
               r"plastilina en el extremo libre. ¿Cómo difiere, si es que lo hace, la frecuencia "
               r"de vibración en ambos casos? ¿Sería distinto si la bola se pegara a la mitad? "
               r"Explica por qué.",
     r"Con la bola en el extremo la frecuencia disminuye: se agrega masa (inercia) justo donde "
     r"la segueta se mueve más. Si la bola se pega en la mitad, la frecuencia también baja, pero "
     r"menos, porque esa parte de la segueta se mueve poco y la bola aporta menos inercia a la "
     r"vibración."),
    (41, "13", r"La aguja de una máquina de coser sube y baja, y su movimiento es armónico simple. "
               r"Lo que la impulsa es una rueda giratoria, movida a la vez por un motor eléctrico. "
               r"¿Cómo crees que se relacionan el periodo de subida y bajada de la aguja con el "
               r"periodo de la rueda giratoria?",
     r"Son iguales: por cada vuelta de la rueda la aguja sube y baja una vez."),
    (42, "14", r"Si agitas el extremo de un resorte para generar una onda, ¿cómo se compara la "
               r"frecuencia de la onda con la frecuencia de tu mano al realizar la sacudida? ¿Tu "
               r"respuesta depende de si produces una onda transversal o una longitudinal? "
               r"Argumenta tu respuesta.",
     r"Son iguales, y no depende del tipo de onda: la frecuencia de una onda es siempre la de la "
     r"fuente que la produce (aquí, tu mano)."),
    (43, "15", r"¿Qué clase de movimiento debes impartir a la boquilla de una manguera en el "
               r"jardín para que el chorro que salga tenga aproximadamente una forma senoidal?",
     r"Un movimiento de vaivén regular (armónico simple) de arriba abajo, o de lado a lado, "
     r"perpendicular a la dirección del chorro y con frecuencia constante."),
    (44, "16", r"¿Qué clase de movimiento debes impartir a un resorte helicoidal estirado (un "
               r"slinky) para generar una onda transversal? ¿Y para generar una onda "
               r"longitudinal?",
     r"Transversal: mover el extremo de arriba abajo o de lado a lado (perpendicular al "
     r"resorte). Longitudinal: empujar y tirar del extremo a lo largo del resorte."),
    (45, "17a", r"¿Qué clase de onda es una ola del mar que se dirige hacia la playa de "
                r"Cartagena?",
     r"Transversal (onda en la superficie de un líquido)."),
    (46, "17b", r"¿Qué clase de onda es el sonido de una ballena que llama a otra bajo el agua?",
     r"Longitudinal (es una onda sonora)."),
    (47, "17c", r"¿Qué clase de onda es un impulso mandado por una cuerda tensa, al sacudir uno de "
                r"sus extremos?",
     r"Transversal.",
     "En la guía: «al golpear uno de sus extremos»; se escribe «sacudir», que es el sentido del "
     "original (Hewitt) y evita pensar en un golpe a lo largo de la cuerda."),
    (48, "18", r"Si se abre una llave de gas durante pocos segundos, alguien que esté a un par de "
               r"metros oirá el escape del gas, mucho antes de captar su olor. ¿Qué indica esto "
               r"acerca de la rapidez del sonido y del movimiento de las moléculas en el medio "
               r"que lo transporta?",
     r"Que el sonido (unos $340\,\text{m/s}$) avanza mucho más rápido que las moléculas del gas "
     r"que se difunden por el aire. En el sonido las moléculas no viajan hasta el oído: cada una "
     r"vibra y empuja a sus vecinas; para oler, en cambio, las moléculas del gas mismo tienen que "
     r"llegar, y eso es lento."),
], tipo="conceptual", dificultad=2)


@ejercicio(id=f"{P}-049", tipo="conceptual", dificultad=1, fuente=fuente(EJ, "19"),
           enunciado=r"Si sube al doble la frecuencia de un objeto en vibración, ¿qué sucederá con "
                     r"su periodo?",
           respuesta=r"Se reduce a la mitad ($T = 1/f$).", **COMUN)
def _():
    assert (1 / (2 * f)) / (1 / f) == Q(1, 2)


manuales(EJ, [
    (50, "20", r"¿Los términos rapidez de onda y frecuencia de onda se refieren a lo mismo? "
               r"Argumenta tu respuesta.",
     r"No. La rapidez indica qué tan rápido avanza la perturbación de un lugar a otro (en "
     r"$\text{m/s}$); la frecuencia indica cuántas vibraciones ocurren por segundo (en "
     r"$\text{Hz}$). Se relacionan mediante $v = \lambda f$, pero son magnitudes distintas."),
], tipo="argumentacion", dificultad=2)


@ejercicio(id=f"{P}-051", tipo="conceptual", dificultad=2, fuente=fuente(EJ, "21"),
           enunciado=r"La longitud de onda de la luz roja es mayor que la de la luz violeta. ¿Cuál "
                     r"de ellas es la que tiene mayor frecuencia?",
           respuesta=r"La violeta: todas las luces viajan con la misma rapidez $c$ y "
                     r"$f = c/\lambda$, así que a menor longitud de onda, mayor frecuencia.",
           **COMUN)
def _():
    rojo, violeta = 700e-9 * meter, 400e-9 * meter        # valores típicos
    assert convert_to(C_LUZ / violeta, hertz) > convert_to(C_LUZ / rojo, hertz)


manuales(EJ, [
    (52, "22", r"Considera una onda que viaja a lo largo de una cuerda gruesa atada a una cuerda "
               r"delgada. ¿Cuál de estas tres características de las ondas no tiene cambios: la "
               r"rapidez, la frecuencia o la longitud de onda?",
     r"La frecuencia, porque la fija la fuente; al pasar a la otra cuerda cambian la rapidez y, "
     r"con ella, la longitud de onda."),
], tipo="conceptual", dificultad=2)


@ejercicio(id=f"{P}-053", tipo="calculo", dificultad=2, fuente=fuente(EJ, "23"),
           enunciado=r"¿Cuál es la frecuencia del segundero de un reloj? ¿Y la del minutero? ¿La "
                     r"de la manecilla de las horas?",
           respuesta=r"Segundero: una vuelta cada $60\,\text{s}$, $f = \frac{1}{60}\,\text{Hz} "
                     r"\approx \num{0,017}\,\text{Hz}$. Minutero: una vuelta cada hora, "
                     r"$f = \frac{1}{3600}\,\text{Hz} \approx \num{2,8e-4}\,\text{Hz}$. Horario: "
                     r"una vuelta cada $12\,\text{h}$, $f = \frac{1}{43\,200}\,\text{Hz} "
                     r"\approx \num{2,3e-5}\,\text{Hz}$.", **COMUN)
def _():
    assert convert_to(1 / minute, hertz) == Q(1, 60) * hertz
    assert convert_to(1 / hour, hertz) == Q(1, 3600) * hertz
    assert convert_to(1 / (12 * hour), hertz) == Q(1, 43200) * hertz
    cerca(1 / hour, Q(28, 10) * 10**-4 * hertz, tol=0.01)
    cerca(1 / (12 * hour), Q(23, 10) * 10**-5 * hertz, tol=0.01)


manuales(EJ, [
    (54, "24", r"¿Cuál es la fuente del movimiento ondulatorio?",
     r"Algo que vibra."),
    (55, "25", r"Si sumerges repetidamente el dedo en un plato lleno de agua formas ondas. ¿Qué "
               r"sucede con la longitud de las ondas si sumerges el dedo con más frecuencia?",
     r"Se hace más corta: la rapidez de las ondas en el agua no cambia y "
     r"$\lambda = v/f$."),
    (56, "26", r"¿Cómo se compara la frecuencia de vibración de un objeto pequeño que flota en el "
               r"agua, con la cantidad de ondas que pasan por él cada segundo?",
     r"Son iguales: el objeto sube y baja una vez por cada onda que pasa."),
    (57, "27", r"¿Hasta dónde llega una onda en un periodo, en términos de longitud de onda?",
     r"Avanza exactamente una longitud de onda."),
], tipo="conceptual", dificultad=1)


@ejercicio(id=f"{P}-058", tipo="calculo", dificultad=2, fuente=fuente(EJ, "28"),
           enunciado=r"¿Cuántos nodos, sin incluir los extremos, hay en una onda estacionaria que "
                     r"tiene dos longitudes de onda de largo? ¿Y una con tres longitudes de onda?",
           respuesta=r"Cada longitud de onda tiene dos segmentos (entre nodo y nodo hay media "
                     r"longitud de onda). Con dos longitudes de onda hay 4 segmentos y "
                     r"\textbf{3 nodos} interiores; con tres longitudes de onda hay 6 segmentos y "
                     r"\textbf{5 nodos}.", **COMUN)
def _():
    nodos = lambda longitudes: 2 * longitudes - 1        # segmentos − 1
    # comprobación por conteo: nodos en múltiplos de λ/2 dentro de una cuerda de largo n·λ
    for n, esperado in [(2, 3), (3, 5)]:
        interiores = [k for k in range(1, 2 * n)]          # posiciones k·λ/2, 0 < k < 2n
        assert len(interiores) == nodos(n) == esperado


manuales(EJ, [
    (59, "29", r"Se deja caer una piedra al agua, y las ondas se difunden por la superficie plana "
               r"del agua. ¿Qué sucede con la energía de esas ondas cuando desaparecen?",
     r"No desaparece: se reparte en un círculo cada vez mayor y termina transformada en energía "
     r"térmica (energía interna) del agua y de la orilla."),
    (60, "30", r"¿Por qué se ve primero el rayo y después se escucha el trueno?",
     r"Porque la luz viaja a unos $\num{3e8}\,\text{m/s}$, casi un millón de veces más rápido "
     r"que el sonido en el aire (unos $340\,\text{m/s}$)."),
    (61, "31", r"Un músico toca el banjo pulsando una cuerda en la mitad. ¿Dónde están los nodos "
               r"de la onda estacionaria en la cuerda? ¿Cuál es la longitud de onda de la cuerda "
               r"vibratoria?",
     r"La cuerda vibra en un solo segmento: los nodos están solo en los dos extremos fijos y hay "
     r"un antinodo en el centro, donde se pulsó. Ese segmento es media longitud de onda, así que "
     r"la longitud de onda es el doble de la longitud de la cuerda: $\lambda = 2L$."),
    (62, "32", r"Un murciélago emite su sonido característico (gorjea) al volar con dirección a "
               r"un muro. ¿La frecuencia del eco del sonido que recibe es mayor, menor o igual "
               r"que la del sonido emitido?",
     r"Mayor: el murciélago se acerca al muro, así que el muro recibe (y refleja) una frecuencia "
     r"mayor, y el murciélago, que va al encuentro del eco, lo percibe aún más alto."),
    (63, "33", r"¿Por qué hay un efecto Doppler cuando la fuente sonora es estacionaria y la "
               r"persona que escucha está en movimiento? ¿En qué dirección debe moverse la "
               r"persona para escuchar una frecuencia mayor? ¿Y para escuchar una frecuencia "
               r"menor?",
     r"Porque al moverse, la persona encuentra las crestas más a menudo (o menos a menudo) de lo "
     r"que le llegarían si estuviera quieta. Para oír una frecuencia mayor debe acercarse a la "
     r"fuente; para oír una menor, alejarse."),
    (64, "34a", r"Una locomotora está parada y suena el silbato; a continuación se acerca hacia "
                r"ti. ¿La frecuencia que escuchas aumenta, disminuye o queda igual?",
     r"Aumenta."),
    (65, "34b", r"Una locomotora está parada y suena el silbato; a continuación se acerca hacia "
                r"ti. ¿Y la longitud de onda que llega al oído?",
     r"Disminuye."),
    (66, "34c", r"Una locomotora está parada y suena el silbato; a continuación se acerca hacia "
                r"ti. ¿Y la rapidez del sonido en el aire que hay entre tú y la locomotora?",
     r"Queda igual: la rapidez del sonido depende del aire, no del movimiento de la fuente."),
    (67, "35", r"Cuando suenas el claxon al manejar hacia una persona que está parada, ella "
               r"escucha un aumento de su frecuencia. ¿Escucharía un aumento en la frecuencia del "
               r"claxon si estuviera también dentro de un automóvil que se mueve con la misma "
               r"rapidez y en la misma dirección que el tuyo? Explica por qué.",
     r"No. El efecto Doppler depende del movimiento relativo entre la fuente y quien escucha; si "
     r"los dos autos van a la misma velocidad, la distancia entre ellos no cambia y no hay "
     r"cambio de frecuencia."),
    (68, "36", r"¿Hay efecto Doppler apreciable cuando el movimiento de la fuente es "
               r"perpendicular al escucha? Explica por qué.",
     r"No. El cambio de frecuencia se debe a que la fuente se acerca o se aleja; si en ese "
     r"momento se mueve perpendicular a la línea que la une con el escucha, la distancia entre "
     r"ellos casi no cambia."),
    (69, "37", r"¿Cómo ayuda el efecto Doppler a que la policía determine quiénes son los "
               r"infractores por exceso de rapidez?",
     r"La pistola de radar envía ondas electromagnéticas que se reflejan en el automóvil; como "
     r"este se mueve, la onda reflejada vuelve con otra frecuencia (efecto Doppler). La "
     r"diferencia entre la frecuencia enviada y la recibida (las pulsaciones entre ambas) indica "
     r"la rapidez del auto."),
    (70, "38", r"Los astrónomos dicen que la luz emitida por determinado elemento en una de las "
               r"orillas del Sol tiene una frecuencia un poco mayor que la que proviene del lado "
               r"opuesto. ¿Qué indican esas determinaciones acerca del movimiento del Sol?",
     r"Que el Sol gira sobre sí mismo: el borde con mayor frecuencia (corrimiento al azul) se "
     r"acerca a nosotros y el borde opuesto (corrimiento al rojo) se aleja."),
    (71, "39", r"¿Sería correcto decir que el efecto Doppler es el cambio aparente de la rapidez "
               r"de una onda, debido al movimiento de la fuente? (¿Por qué esta pregunta es para "
               r"comprobar la comprensión en la lectura y también el conocimiento de física?)",
     r"No. El efecto Doppler es el cambio de la \emph{frecuencia} recibida, no de la rapidez, "
     r"que depende solo del medio. La pregunta comprueba la lectura (distinguir las palabras "
     r"«rapidez» y «frecuencia» en la definición) y la física (entender que son magnitudes "
     r"distintas)."),
    (72, "40", r"¿Cómo interviene el fenómeno de la interferencia en la producción de ondas de "
               r"proa o de ondas de choque?",
     r"Las ondas de proa y de choque se forman por interferencia constructiva: muchas ondas "
     r"circulares (o esféricas) se traslapan en los bordes y sus crestas se suman, formando la V "
     r"(o el cono)."),
    (73, "41", r"¿Qué puedes decir acerca de la rapidez de un bote que produce una onda de proa?",
     r"Que el bote se mueve más rápido que las ondas que produce en el agua."),
    (74, "42", r"¿El ángulo del cono de una onda de choque se abre, se cierra o permanece "
               r"constante cuando un avión supersónico aumenta su rapidez?",
     r"Se cierra: el cono se hace más angosto."),
    (75, "43", r"Si el sonido de un avión no proviene de la parte del cielo donde se ve, ¿significa "
               r"eso que el avión viaja con más rapidez que la del sonido? Explica.",
     r"No necesariamente. El sonido tarda en llegar al suelo y mientras tanto el avión avanza, "
     r"así que el sonido de cualquier avión parece venir de un punto detrás de donde se ve, "
     r"aunque vuele más despacio que el sonido."),
    (76, "44", r"¿Se produce estampido sónico en el momento en el que el avión atraviesa la "
               r"barrera del sonido? Explica por qué.",
     r"No solo en ese momento. Mientras el avión vuele más rápido que el sonido arrastra la onda "
     r"de choque, y el estampido se oye en cada lugar por el que pasa el cono, de manera "
     r"continua, no una única vez al superar la rapidez del sonido."),
    (77, "45", r"¿Por qué un avión subsónico, por más ruidoso que sea, no puede producir un "
               r"estampido sónico?",
     r"Porque sus ondas sonoras avanzan delante de él y no se apilan ni se traslapan formando una "
     r"onda de choque: llegan a los oídos una tras otra, como un sonido continuo."),
    (78, "46", r"Imagina un pez súper rápido, que puede nadar a una rapidez mayor que la del "
               r"sonido en el agua. ¿Ese pez produciría un «estampido sónico»?",
     r"Sí: produciría una onda de choque en el agua (un estampido bajo el agua), igual que un "
     r"avión supersónico en el aire; tendría que nadar a más de unos $1500\,\text{m/s}$."),
], tipo="conceptual", dificultad=2)

# ---------------------------------------------------------------- Problemas
PR = "Problemas"
for n, lit, periodo, texto, frec, ftex in [
        (79, "1a", Q(1, 10), r"\num{0,10}", 10, r"10"),
        (80, "1b", 5, r"5", Q(1, 5), r"\num{0,2}"),
        (81, "1c", Q(1, 60), r"\frac{1}{60}", 60, r"60")]:
    @ejercicio(id=f"{P}-{n:03d}", tipo="calculo", dificultad=1, fuente=fuente(PR, lit),
               enunciado=rf"¿Cuál es la frecuencia en hertz que corresponde a un periodo de "
                         rf"${texto}\,\text{{s}}$?",
               respuesta=rf"$f = \dfrac{{1}}{{T}} = {ftex}\,\text{{Hz}}$.", **COMUN)
    def _(periodo=periodo, frec=frec):
        assert convert_to(1 / (periodo * second), hertz) == frec * hertz

for n, lit, frec, texto, periodo, ptex in [
        (82, "2a", 10, r"10", Q(1, 10), r"\num{0,1}"),
        (83, "2b", Q(1, 5), r"\num{0,2}", 5, r"5"),
        (84, "2c", 60, r"60", Q(1, 60), r"\frac{1}{60} \approx \num{0,017}")]:
    @ejercicio(id=f"{P}-{n:03d}", tipo="calculo", dificultad=1, fuente=fuente(PR, lit),
               enunciado=rf"¿Cuál es el periodo, en segundos, que corresponde a una frecuencia "
                         rf"de ${texto}\,\text{{Hz}}$?",
               respuesta=rf"$T = \dfrac{{1}}{{f}} = {ptex}\,\text{{s}}$.", **COMUN)
    def _(frec=frec, periodo=periodo):
        assert convert_to(1 / (frec * hertz), second) == periodo * second
        cerca(1 / (frec * hertz), float(periodo) * second, tol=0.02)


@ejercicio(id=f"{P}-085", tipo="contexto", dificultad=2, fuente=fuente(PR, "3"),
           enunciado=r"Un marinero en una lancha observa que las crestas de las olas pasan por la "
                     r"cadena del ancla cada $5\,\text{s}$. Estima que la distancia entre las "
                     r"crestas es $15\,\text{m}$. ¿Cuál es la rapidez de las olas?",
           respuesta=r"$v = \dfrac{\lambda}{T} = \dfrac{15\,\text{m}}{5\,\text{s}} = "
                     r"3\,\text{m/s}$.", **COMUN)
def _():
    assert convert_to(15 * meter / (5 * second), meter / second) == 3 * meter / second


@ejercicio(id=f"{P}-086", tipo="contexto", dificultad=2, fuente=fuente(PR, "4"),
           enunciado=r"Un peso colgado de un resorte sube y baja dos veces cada segundo; entre el "
                     r"punto más alto y el más bajo hay $20\,\text{cm}$. ¿Cuáles son su "
                     r"frecuencia, su periodo y su amplitud?",
           respuesta=r"$f = 2\,\text{Hz}$; $T = \dfrac{1}{f} = \num{0,5}\,\text{s}$; la amplitud "
                     r"se mide desde el punto medio, así que es la mitad del recorrido: "
                     r"$A = 10\,\text{cm}$.",
           notas="En la guía: «sube y baja una distancia de 20 centímetros»; se precisa que los "
                 "20 cm van del punto más alto al más bajo, para que la amplitud (10 cm) no se "
                 "confunda con el recorrido total.", **COMUN)
def _():
    frecuencia = 2 / second
    assert convert_to(frecuencia, hertz) == 2 * hertz
    assert convert_to(1 / frecuencia, second) == Q(1, 2) * second
    assert Q(20, 2) == 10                                   # amplitud en cm


@ejercicio(id=f"{P}-087", tipo="contexto", dificultad=2, fuente=fuente(PR, "5"),
           enunciado=r"Las ondas de radio viajan a la rapidez de la luz, "
                     r"$\num{300000}\,\text{km/s}$. ¿Cuál es la longitud de las ondas de radio que "
                     r"se reciben de la estación de $\num{100,1}\,\text{MHz}$ en tu radio de FM?",
           respuesta=r"$\lambda = \dfrac{v}{f} = \dfrac{\num{3e8}\,\text{m/s}}"
                     r"{\num{1,001e8}\,\text{Hz}} \approx 3\,\text{m}$ (\num{3,00} m).",
           notas="En la guía: «100.1 MHz» con punto decimal.", **COMUN)
def _():
    cerca(C_LUZ / (Q(1001, 10) * (10**6 * hertz)), 3 * meter, tol=0.002)


@ejercicio(id=f"{P}-088", tipo="contexto", dificultad=2, fuente=fuente(PR, "6"),
           enunciado=r"Un mosquito bate sus alas 600 veces por segundo, lo cual produce el molesto "
                     r"zumbido de $600\,\text{Hz}$. Si el sonido viaja a $340\,\text{m/s}$, ¿cuánto "
                     r"avanza el sonido entre dos batidos del ala? En otras palabras, calcula la "
                     r"longitud de onda del zumbido.",
           respuesta=r"$\lambda = \dfrac{v}{f} = \dfrac{340\,\text{m/s}}{600\,\text{Hz}} \approx "
                     r"\num{0,57}\,\text{m}$ (unos $57\,\text{cm}$).",
           notas="La guía no da la rapidez del sonido en este problema; se añade 340 m/s "
                 "(el valor que usa en el problema 7).", **COMUN)
def _():
    cerca(V_SON / (600 * hertz), Q(57, 100) * meter, tol=0.01)


@ejercicio(id=f"{P}-089", tipo="contexto", dificultad=2, fuente=fuente(PR, "7a"),
           enunciado=r"En un teclado, la frecuencia del «do» central es $256\,\text{Hz}$. ¿Cuál es "
                     r"el periodo de una vibración con este tono?",
           respuesta=r"$T = \dfrac{1}{256}\,\text{s} \approx \num{0,0039}\,\text{s}$ "
                     r"(unos $\num{3,9}\,\text{ms}$).",
           notas="256 Hz es el «do» de la afinación científica; en la afinación usual "
                 "(la = 440 Hz) el do central es de unos 261,6 Hz. Se conserva el dato de la guía.",
           **COMUN)
def _():
    assert convert_to(1 / (256 * hertz), second) == Q(1, 256) * second
    cerca(1 / (256 * hertz), Q(39, 10000) * second, tol=0.01)


@ejercicio(id=f"{P}-090", tipo="contexto", dificultad=2, fuente=fuente(PR, "7b"),
           enunciado=r"El «do» central de $256\,\text{Hz}$ sale del instrumento con una rapidez de "
                     r"$340\,\text{m/s}$. ¿Cuál será su longitud de onda en el aire?",
           respuesta=r"$\lambda = \dfrac{340\,\text{m/s}}{256\,\text{Hz}} \approx "
                     r"\num{1,33}\,\text{m}$.", **COMUN)
def _():
    cerca(V_SON / (256 * hertz), Q(133, 100) * meter, tol=0.005)


@ejercicio(id=f"{P}-091", tipo="contexto", dificultad=2, fuente=fuente(PR, "8a"),
           enunciado=r"Si fueras tan ingenuo como para tocar el teclado bajo el agua, donde la "
                     r"rapidez del sonido es $\num{1500}\,\text{m/s}$, ¿cuál sería la longitud de "
                     r"onda del «do» central ($256\,\text{Hz}$) en el agua?",
           respuesta=r"$\lambda = \dfrac{\num{1500}\,\text{m/s}}{256\,\text{Hz}} \approx "
                     r"\num{5,86}\,\text{m}$.", **COMUN)
def _():
    cerca(1500 * meter / second / (256 * hertz), Q(586, 100) * meter, tol=0.005)


manuales(PR, [
    (92, "8b", r"Explica por qué el «do» central (o cualquier otra nota) tiene mayor longitud de "
               r"onda en el agua que en el aire.",
     r"La frecuencia la fija el instrumento y es la misma en los dos medios, pero el sonido "
     r"viaja más rápido en el agua ($\num{1500}\,\text{m/s}$) que en el aire "
     r"($340\,\text{m/s}$). Como $\lambda = v/f$, a mayor rapidez con la misma frecuencia, mayor "
     r"longitud de onda."),
], tipo="argumentacion", dificultad=2)


@ejercicio(id=f"{P}-093", tipo="contexto", dificultad=3, fuente=fuente(PR, "9"),
           enunciado=r"La longitud de onda del canal 6 de la televisión es $\num{3,42}\,\text{m}$. "
                     r"¿El canal 6 transmite con una frecuencia mayor o menor que la banda de "
                     r"radio FM, que va de 88 a $108\,\text{MHz}$?",
           respuesta=r"$f = \dfrac{c}{\lambda} = \dfrac{\num{3e8}\,\text{m/s}}"
                     r"{\num{3,42}\,\text{m}} \approx \num{87,7}\,\text{MHz}$: un poco "
                     r"\textbf{menor} que la banda de FM.", **COMUN)
def _():
    fc = convert_to(C_LUZ / (Q(342, 100) * meter), hertz)
    cerca(fc, Q(877, 10) * (10**6 * hertz), tol=0.001)
    assert fc < 88 * (10**6 * hertz)
