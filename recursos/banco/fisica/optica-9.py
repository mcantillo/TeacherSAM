"""Banco de ejercicios — Física 9° — Reflexión y refracción de la luz.
Fuente: Guía de Apoyo de Física 9° (ondas, sonido y luz), Capítulo 4 «Reflexión y refracción»:
Preguntas de repaso, Ejercicios y Problemas. Se lee en
recursos/fisica/Guías pedagógicas Física/markdown/09 - Guia_de_Apoyo_Conceptos_ondas_de_sonido_y_de_luz_grado_9_fisica.md
Alineación: Estándares 8°–9° (dba/naturales/estandares-fisica.md) — «Reconozco y diferencio
modelos para explicar la naturaleza y el comportamiento de la luz» y «Explico el principio de
conservación de la energía en ondas que cambian de medio de propagación».
No incluidos: los «Examínate» (ya traen su respuesta en la guía) y el Proyecto 1 (carta; su
contenido, el espejo de media altura, está en el ejercicio 7).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/fisica/optica-9.py
"""
from sympy import Rational as Q, asin, deg, simplify
from sympy.physics.units import convert_to, kelvin, kilogram, meter, minute, second

from ejercicios import ejercicio, ejercicio_manual

P = "optica-9"
GUIA = "Guía de Apoyo Física 9° (ondas, sonido y luz), Cap. 4 Reflexión y refracción"
COMUN = dict(tema="reflexión y refracción", grados=[9], dba=[])


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


def angulo_critico(v_dentro, v_fuera):
    """Ángulo crítico (en grados) para la luz que sale de un medio lento a uno rápido:
    sen θc = v_dentro / v_fuera (ley de Snell escrita con las rapideces)."""
    return float(deg(asin(Q(v_dentro) / Q(v_fuera))))


# ---------------------------------------------------------------- Preguntas de repaso
REPASO = "Preguntas de repaso"
manuales(REPASO, [
    (1, "1", r"Explica la diferencia entre reflexión y refracción.",
     r"En la reflexión la luz regresa al medio del que venía al llegar a una superficie; en la "
     r"refracción pasa a otro medio transparente y se desvía, porque cambia su rapidez."),
    (2, "2", r"¿La luz incidente que llega a un objeto cómo afecta el movimiento de los electrones "
             r"en los átomos del objeto?",
     r"Los pone a vibrar con más energía, forzados por el campo eléctrico oscilante de la luz."),
    (3, "3", r"¿Qué hacen los electrones en un objeto iluminado cuando son forzados a vibrar con "
             r"mayor energía?",
     r"Reemiten luz: esa es la luz reflejada con la que vemos el objeto."),
    (4, "4", r"¿Cuál es el principio de Fermat del tiempo mínimo?",
     r"Entre todas las trayectorias posibles para ir de un punto a otro, la luz sigue la que "
     r"requiere el menor tiempo."),
    (5, "5", r"Explica la ley de la reflexión.",
     r"El ángulo de incidencia es igual al ángulo de reflexión, medidos ambos respecto a la "
     r"normal (la perpendicular a la superficie); el rayo incidente, la normal y el rayo "
     r"reflejado están en un mismo plano."),
    (6, "6", r"En relación con la distancia de un objeto frente a un espejo plano, ¿a qué "
             r"distancia se encuentra la imagen detrás del espejo?",
     r"A la misma distancia: la imagen está tan lejos detrás del espejo como el objeto está "
     r"delante, y tiene su mismo tamaño."),
    (7, "7", r"¿Qué fracción de la luz que llega directa a una lámina de vidrio se refleja en la "
             r"primera superficie?",
     r"Cerca del $4\,\%$."),
    (8, "8", r"¿Puede pulirse una superficie para reflejar unas ondas pero otras no?",
     r"Sí: una superficie está «pulida» para las ondas cuya longitud de onda es mucho mayor que "
     r"sus irregularidades. La malla de una antena parabólica es un espejo para las ondas de "
     r"radio, pero es áspera para la luz visible."),
    (9, "9", r"La luz se desvía al pasar de un medio a otro en dirección oblicua a la superficie "
             r"que los separa, y toma un camino un poco más largo para ir de un punto a otro "
             r"punto. ¿Qué tiene que ver ese camino más largo con el tiempo de recorrido de la "
             r"luz?",
     r"Aunque es más largo, es el de menor tiempo: recorre más distancia en el medio donde es "
     r"más rápida y menos en el medio donde es más lenta."),
    (10, "10", r"¿Cómo se compara el ángulo con el que llega la luz al vidrio de una ventana con "
               r"el ángulo con el que sale por el otro lado?",
     r"Son iguales: la luz sale paralela a como entró, solo desplazada."),
    (11, "11", r"¿Cómo se compara el ángulo con el que llega un rayo de luz a un prisma con el "
               r"ángulo que forma al salir por la otra cara?",
     r"No son iguales: como las caras del prisma no son paralelas, la luz sale en otra "
     r"dirección, desviada hacia la base del prisma."),
    (12, "12", r"¿La luz viaja más rápido por aire ligero o por aire denso? ¿Qué tiene que ver esa "
               r"diferencia de rapideces con la duración de un día?",
     r"Por el aire ligero (enrarecido). Por eso la luz del Sol se curva al entrar en la "
     r"atmósfera, cuya densidad aumenta hacia abajo, y seguimos viendo el Sol unos minutos "
     r"después de que ha bajado del horizonte (y lo vemos antes de que salga): el día se alarga "
     r"un poco."),
    (13, "13", r"¿Un espejismo es producido por la reflexión o por la refracción?",
     r"Por la refracción."),
    (14, "14", r"Cuando un carrito rueda por una acera lisa y pasa a un césped, la interacción de "
               r"la rueda con las hojas del pasto desacelera aquélla. ¿Qué desacelera a la luz "
               r"cuando pasa del aire al vidrio o al agua?",
     r"Las interacciones con los átomos del material: la absorción y reemisión de la luz, con "
     r"pequeñas demoras."),
    (15, "15", r"¿Cuál es la relación entre la refracción y los cambios de la rapidez de la luz en "
               r"un material?",
     r"La refracción es consecuencia de que la rapidez de la luz cambie al pasar de un medio a "
     r"otro; sin cambio de rapidez no habría refracción."),
    (16, "16", r"¿La refracción de la luz hace que una alberca parezca más o menos profunda?",
     r"Menos profunda: los objetos sumergidos parecen más cerca de la superficie."),
    (17, "17", r"¿Qué sucede con la luz de determinada frecuencia cuando llega a un material cuya "
               r"frecuencia natural es igual a la frecuencia de la luz?",
     r"Se absorbe (hay resonancia) y su energía se convierte en calor."),
    (18, "18", r"¿Qué se propaga con menos rapidez en el vidrio, la luz roja o la luz violeta?",
     r"La luz violeta (más o menos un $1\,\%$ más lenta que la roja)."),
    (19, "19", r"¿Una sola gota de lluvia iluminada por la luz del Sol desvía la luz de un solo "
               r"color, o dispersa un espectro de colores?",
     r"Dispersa todo el espectro de colores."),
    (20, "20", r"¿El espectador observa un solo color o un espectro de colores que provienen de "
               r"una sola gota lejana?",
     r"Un solo color: de cada gota le llega solo el color que sale en la dirección de su ojo."),
    (21, "21", r"¿Por qué un arcoíris secundario es más tenue que un arcoíris primario?",
     r"Porque se forma con una reflexión adicional dentro de las gotas, y en cada reflexión se "
     r"pierde parte de la luz."),
], tipo="conceptual", dificultad=1)

# ---------------------------------------------------------------- Ejercicios
EJ = "Ejercicios"
manuales(EJ, [
    (22, "1", r"El principio de Fermat es de tiempo mínimo, y no de distancia mínima. ¿Se "
              r"aplicaría la distancia mínima también en la reflexión? ¿Y en la refracción? ¿Por "
              r"qué tus respuestas son distintas?",
     r"En la reflexión sí: la luz no cambia de medio, su rapidez es la misma y el camino de menor "
     r"tiempo es también el más corto. En la refracción no: la rapidez cambia de un medio a "
     r"otro, y el camino de menor tiempo no es el de menor distancia."),
    (23, "2", r"El vaquero Joe quiere disparar a un asaltante haciendo rebotar una bala en una "
              r"placa metálica pulida como espejo. Para hacerlo, ¿simplemente debería apuntar a "
              r"la imagen reflejada del asaltante? Explica por qué.",
     r"Sí. Si la bala rebota como la luz (ángulo de incidencia igual al de reflexión), sigue el "
     r"mismo camino que la luz que llega del asaltante a los ojos de Joe, pero en sentido "
     r"contrario; apuntando a la imagen, la bala llega al asaltante."),
    (24, "3", r"Con frecuencia, los camiones tienen letreros atrás que dicen «si no puedes ver mis "
              r"espejos, yo no te puedo ver». Explica los procesos físicos que intervienen aquí.",
     r"La reflexión y la reversibilidad de los caminos de la luz: la luz que va de ti al "
     r"conductor, reflejándose en el espejo, recorre el mismo camino que la que va del conductor "
     r"a ti. Si desde tu posición no ves el espejo (o los ojos del conductor en él), la luz "
     r"tampoco puede ir de ti a él."),
    (25, "4", r"Los espejos retrovisores de los automóviles no están recubiertos en la primera "
              r"superficie, y están plateados en la superficie trasera. Cuando el espejo se "
              r"ajusta en forma correcta, la luz que llega de atrás se refleja en la superficie "
              r"plateada y va hacia los ojos del conductor. Pero no está tan bien durante la "
              r"noche, con la luz deslumbrante de los autos que vienen atrás. Este problema se "
              r"resuelve porque el vidrio del espejo tiene forma de cuña. Cuando el espejo se "
              r"inclina un poco hacia arriba, a su posición «nocturna», la luz deslumbrante se "
              r"dirige hacia el techo del automóvil y se aleja de los ojos del conductor. Sin "
              r"embargo, el conductor puede seguir viendo en el espejo los vehículos que vienen "
              r"atrás. Explica por qué.",
     r"Porque hay dos reflexiones: la de la superficie plateada (refleja casi toda la luz) y la "
     r"de la primera superficie de vidrio (refleja cerca del $4\,\%$). Como el vidrio es una "
     r"cuña, las dos reflexiones salen en direcciones distintas: en la posición nocturna la "
     r"fuerte va al techo y al conductor le llega la débil, suficiente para ver los carros sin "
     r"deslumbrarse."),
    (26, "5", r"Para reducir el resplandor de los alrededores, las ventanas de algunas tiendas por "
              r"departamentos están inclinadas con el lado inferior hacia adentro, en vez de ser "
              r"verticales. ¿Cómo se reduce así el resplandor?",
     r"La luz de la calle que se refleja en el vidrio inclinado sale dirigida hacia el suelo, no "
     r"hacia los ojos de los peatones, así que ellos ven la vitrina sin el reflejo."),
    (27, "6", r"Una persona en un cuarto oscuro que ve por una ventana puede mirar con claridad a "
              r"una persona que esté afuera a la luz del día; mientras que la persona en el "
              r"exterior no puede ver a la persona dentro del cuarto oscuro. Explica por qué.",
     r"La mucha luz de afuera atraviesa el vidrio y llega a quien está adentro. La persona de "
     r"afuera recibe dos luces: la poca que sale del cuarto oscuro y el reflejo (cerca del "
     r"$4\,\%$) de la luz intensa del exterior; el reflejo es mucho más brillante y tapa lo que "
     r"hay adentro."),
    (28, "7", r"¿Cuál debe ser la altura mínima de un espejo plano para que te veas de cuerpo "
              r"completo en él?",
     r"La mitad de tu estatura, sin importar la distancia al espejo: la luz que va de tus pies a "
     r"tus ojos se refleja a mitad de altura entre ellos, y la de la coronilla a mitad de camino "
     r"entre la coronilla y los ojos; el espejo solo necesita cubrir la mitad del cuerpo, bien "
     r"colocado."),
    (29, "8", r"¿Puedes decir si una persona tiene miopía o hipermetropía al ver cómo su cara "
              r"aparece en sus anteojos? Cuando los ojos de una persona se ven aumentados, ¿la "
              r"persona tiene miopía o hipermetropía?",
     r"Sí. Si los ojos se ven aumentados, las lentes son convergentes (como una lupa) y la "
     r"persona tiene hipermetropía; si se ven reducidos, las lentes son divergentes y tiene "
     r"miopía."),
    (30, "9", r"Un pulso de luz roja y uno de luz azul entran a un bloque de vidrio, normal a su "
              r"superficie y al mismo tiempo. Estrictamente hablando, después de atravesar el "
              r"bloque, ¿cuál pulso sale primero?",
     r"El rojo, porque en el vidrio la luz roja viaja un poco más rápido que la azul."),
    (31, "10", r"Durante un eclipse lunar, la Luna no está totalmente negra, sino con frecuencia "
               r"tiene un color rojo intenso. Explica lo que sucede en términos de la refracción "
               r"en los ocasos y las auroras en todo el mundo.",
     r"La atmósfera de la Tierra refracta (desvía) parte de la luz del Sol hacia la zona de "
     r"sombra. Esa luz atraviesa mucho aire, igual que la de los atardeceres y amaneceres de todo "
     r"el mundo, y en el camino pierde el azul: le llega a la Luna enrojecida."),
    (32, "11", r"Si al estar parado a la orilla de un río quieres pescar con arpón a un pez que "
               r"está frente a ti, ¿deberías apuntar hacia arriba o hacia abajo del pez, o "
               r"directamente hacia él? Si en lugar de ello pudieras atrapar al pez con un rayo "
               r"láser, ¿deberías apuntar hacia arriba o hacia abajo del pez, o directamente "
               r"hacia él? Defiende tus respuestas.",
     r"Con el arpón, por debajo del pez que ves: por la refracción, el pez está más hondo de lo "
     r"que parece y el arpón sigue en línea recta. Con el láser, directamente al pez que ves: la "
     r"luz del láser se refracta en la superficie y recorre, al revés, el mismo camino que la luz "
     r"que viene del pez a tus ojos."),
], tipo="conceptual", dificultad=2)


@ejercicio(id=f"{P}-033", tipo="argumentacion", dificultad=3, fuente=fuente(EJ, "12"),
           enunciado=r"Cuando un pez mira hacia arriba en un ángulo de $45^{\circ}$ respecto a la "
                     r"vertical, ¿ve el cielo o sólo la reflexión del fondo? Defiende tu respuesta.",
           respuesta=r"Ve el cielo. La luz solo se refleja totalmente en la superficie del agua si "
                     r"llega con un ángulo mayor que el ángulo crítico, que para el agua es de unos "
                     r"$49^{\circ}$ (la luz viaja en el agua al $75\,\%$ de su rapidez en el aire: "
                     r"$\operatorname{sen}\theta_c = \num{0,75}$). Como "
                     r"$45^{\circ} < 49^{\circ}$, la luz del cielo sí entra refractada y llega al "
                     r"pez.",
           notas="La guía dice «en un ángulo de 45°» sin decir respecto a qué; se precisa «respecto "
                 "a la vertical» (con 45° el resultado es el mismo si se mide desde la "
                 "superficie). El ángulo crítico solo aparece en el resumen de términos de la "
                 "guía.", **COMUN)
def _():
    critico = angulo_critico(Q(75, 100), 1)
    assert 48 < critico < 49                            # 48,6°
    assert 45 < critico


manuales(EJ, [
    (34, "13", r"Si fueras a mandar un rayo láser a una estación espacial sobre la atmósfera y "
               r"justo encima del horizonte, ¿apuntarías el rayo láser arriba, abajo o hacia la "
               r"estación espacial visible? Defiende tu respuesta.",
     r"Directamente hacia la estación que ves: el láser se refracta en la atmósfera siguiendo, "
     r"en sentido contrario, el mismo camino curvo que la luz que llega de la estación a tus "
     r"ojos."),
    (35, "14", r"Dos observadores separados entre sí no ven el «mismo» arcoíris. Explica por qué.",
     r"Cada observador ve la luz de las gotas que están en un cono de unos $40^{\circ}$ a "
     r"$42^{\circ}$ alrededor de la línea que pasa por su propio ojo (en dirección opuesta al "
     r"Sol). Como sus ojos están en lugares distintos, sus conos cortan gotas distintas: cada uno "
     r"ve su propio arcoíris."),
    (36, "15", r"Un arcoíris visto desde un avión puede formar un círculo completo. ¿Dónde "
               r"aparecerá la sombra del avión? Explica por qué.",
     r"En el centro del círculo: el centro del arcoíris está en la dirección opuesta al Sol "
     r"(el eje del cono pasa por el observador y el Sol), justo donde cae la sombra del avión."),
    (37, "16", r"Cuando los ojos se sumergen en agua, ¿la desviación de los rayos de luz del agua a "
               r"los ojos es mayor, menor o igual que en el aire?",
     r"Menor: la luz viaja con una rapidez parecida en el agua y en la córnea, así que al pasar "
     r"del agua al ojo casi no se desvía. Por eso bajo el agua vemos borroso."),
    (38, "17", r"¿Por qué los goggles permiten que un nadador bajo el agua enfoque con más claridad "
               r"lo que está mirando?",
     r"Porque dejan una capa de aire frente a los ojos: la luz vuelve a pasar del aire a la "
     r"córnea, se desvía como de costumbre y el ojo enfoca normalmente."),
    (39, "18", r"Si un pez usara goggles sobre la superficie del agua, ¿por qué su visión sería "
               r"mejor si estuvieran llenos de agua?",
     r"Porque los ojos del pez están hechos para enfocar la luz que les llega desde el agua; con "
     r"goggles llenos de agua, la luz entraría a sus ojos como está acostumbrado."),
], tipo="conceptual", dificultad=2)


@ejercicio(id=f"{P}-040", tipo="argumentacion", dificultad=3, fuente=fuente(EJ, "19"),
           enunciado=r"¿Un diamante bajo el agua destella más o menos que en el aire? Defiende tu "
                     r"respuesta.",
           respuesta=r"Menos. El destello se debe a la gran diferencia entre la rapidez de la luz "
                     r"en el diamante ($\num{0,41}\,c$) y afuera: la luz se refracta mucho y se "
                     r"refleja totalmente dentro del diamante. En el agua ($\num{0,75}\,c$) la "
                     r"diferencia es menor: se desvía menos y el ángulo crítico sube de unos "
                     r"$24^{\circ}$ a unos $33^{\circ}$, así que se refleja menos luz dentro y el "
                     r"diamante brilla menos.",
           notas="Los ángulos críticos se calculan con las rapideces que da la guía "
                 "(diamante 0,41c; agua 0,75c).", **COMUN)
def _():
    en_aire, en_agua = angulo_critico(Q(41, 100), 1), angulo_critico(Q(41, 100), Q(75, 100))
    assert round(en_aire) == 24 and round(en_agua) == 33
    assert en_agua > en_aire


# ---------------------------------------------------------------- Problemas
PR = "Problemas"
manuales(PR, [
    (41, "1", r"Demuestra, con un diagrama sencillo, que cuando un espejo con un rayo fijo que "
              r"incide en él gira determinado ángulo, el rayo reflejado gira un ángulo dos veces "
              r"mayor.",
     r"Si el rayo incidente forma un ángulo $\alpha$ con la normal, el reflejado forma $\alpha$ "
     r"al otro lado: entre los dos hay $2\alpha$. Al girar el espejo un ángulo $\theta$, la "
     r"normal gira $\theta$ y el ángulo de incidencia pasa a ser $\alpha + \theta$; el ángulo "
     r"entre incidente y reflejado pasa a ser $2(\alpha + \theta) = 2\alpha + 2\theta$. Como el "
     r"incidente no se movió, el reflejado giró $2\theta$. (El diagrama muestra el espejo, su "
     r"normal y los dos rayos antes y después del giro.)",
     "Demostración con diagrama: queda como ejercicio manual."),
], tipo="argumentacion", dificultad=3)


@ejercicio(id=f"{P}-042", tipo="contexto", dificultad=2, fuente=fuente(PR, "2"),
           enunciado=r"Una mariposa, a la altura de los ojos, está a $20\,\text{cm}$ frente a un "
                     r"espejo plano. Tú estás detrás de la mariposa, a $50\,\text{cm}$ del espejo. "
                     r"¿Cuál es la distancia entre tu ojo y la imagen de la mariposa en el espejo?",
           respuesta=r"La imagen está $20\,\text{cm}$ detrás del espejo; tu ojo, "
                     r"$50\,\text{cm}$ delante: $50 + 20 = 70\,\text{cm}$.", **COMUN)
def _():
    ojo, imagen = 50, -20                                # posiciones (cm) medidas desde el espejo
    assert ojo - imagen == 70


@ejercicio(id=f"{P}-043", tipo="contexto", dificultad=1, fuente=fuente(PR, "3"),
           enunciado=r"Si tomas una fotografía de tu imagen en un espejo plano, ¿a cuántos metros "
                     r"debes enfocar si estás a $2\,\text{m}$ frente al espejo?",
           respuesta=r"A $4\,\text{m}$: la imagen está $2\,\text{m}$ detrás del espejo, y la cámara "
                     r"$2\,\text{m}$ delante.", **COMUN)
def _():
    assert 2 - (-2) == 4


@ejercicio(id=f"{P}-044", tipo="contexto", dificultad=2, fuente=fuente(PR, "4"),
           enunciado=r"Imagina que caminas hacia un espejo a $2\,\text{m/s}$. ¿Con qué rapidez se "
                     r"acercan tú y tu imagen entre sí? (La respuesta no es $2\,\text{m/s}$.)",
           respuesta=r"A $4\,\text{m/s}$: la imagen también se acerca al espejo a "
                     r"$2\,\text{m/s}$, desde el otro lado.",
           grados=[9], tema="reflexión y refracción", dba=["naturales-9-1"])
def _():
    from sympy import diff, symbols
    t, d0 = symbols("t d0", positive=True)
    tu = d0 - 2 * t                                       # posición (m) delante del espejo
    imagen = -(d0 - 2 * t)                                # simétrica, detrás del espejo
    assert diff(tu - imagen, t) == -4                     # la separación disminuye 4 m cada s
    assert convert_to(4 * meter / second, meter / second) == 4 * meter / second


@ejercicio(id=f"{P}-045", tipo="calculo", dificultad=2, fuente=fuente(PR, "5"),
           enunciado=r"Cuando la luz llega perpendicularmente al vidrio, se refleja en cada "
                     r"superficie más o menos el $4\,\%$. ¿Cuánta luz se transmite a través de una "
                     r"lámina de vidrio?",
           respuesta=r"Pasa el $96\,\%$ por la primera cara y el $96\,\%$ de eso por la segunda: "
                     r"$\num{0,96} \times \num{0,96} \approx \num{0,92}$, cerca del $92\,\%$.",
           **COMUN)
def _():
    assert Q(96, 100)**2 == Q(9216, 10000)
    assert abs(float(Q(96, 100)**2) - 0.92) < 0.005


@ejercicio(id=f"{P}-046", tipo="calculo", dificultad=2, fuente=fuente(PR, "6"),
           enunciado=r"Ningún vidrio es perfectamente transparente. Principalmente debido a las "
                     r"reflexiones, un $92\,\%$ de la luz atraviesa una lámina promedio de vidrio "
                     r"transparente de ventana. La pérdida de $8\,\%$ no se nota cuando sólo es una "
                     r"lámina, pero sí se nota a través de varias láminas. ¿Cuánta luz transmite "
                     r"una ventana «con vidrio doble» (una que tiene dos hojas de vidrio)?",
           respuesta=r"$\num{0,92} \times \num{0,92} \approx \num{0,85}$: cerca del $85\,\%$.",
           **COMUN)
def _():
    assert Q(92, 100)**2 == Q(8464, 10000)
    assert abs(float(Q(92, 100)**2) - 0.85) < 0.005


@ejercicio(id=f"{P}-047", tipo="contexto", dificultad=3, fuente=fuente(PR, "7"),
           enunciado=r"El diámetro del Sol, visto desde la Tierra, abarca un ángulo de "
                     r"$\num{0,53}^{\circ}$. ¿Cuántos minutos tarda el Sol en recorrer un diámetro "
                     r"solar en el cenit (el Sol directamente arriba de nosotros)? Recuerda que "
                     r"tarda 24 horas, o \num{1440} minutos, en recorrer $360^{\circ}$. ¿Cómo se "
                     r"compara tu respuesta con el tiempo que tarda el Sol en desaparecer desde "
                     r"que la orilla inferior toca el horizonte en el crepúsculo? (¿La refracción "
                     r"influyó sobre tu respuesta?)",
           respuesta=r"El Sol recorre $\dfrac{360^{\circ}}{\num{1440}\,\text{min}} = "
                     r"\num{0,25}^{\circ}$ por minuto, así que un diámetro le toma "
                     r"$\dfrac{\num{0,53}}{\num{0,25}} \approx \num{2,1}\,\text{min}$. Cerca del "
                     r"ecuador (como en Cali) el Sol baja casi en vertical y su disco también "
                     r"tarda unos 2 minutos en ocultarse; en latitudes altas tarda más, porque "
                     r"baja inclinado. La refracción no entra en el cálculo: retrasa todo el "
                     r"ocaso un par de minutos y achata el disco, pero casi no cambia esa "
                     r"duración.",
           notas="En la guía: «0.53°» con punto decimal.", **COMUN)
def _():
    rapidez = Q(360, 1440)                                # grados por minuto
    t = Q(53, 100) / rapidez * minute
    cerca(t, Q(21, 10) * minute, tol=0.01)
