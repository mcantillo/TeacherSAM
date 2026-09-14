"""Banco de ejercicios — Física 10° — Mecánica de fluidos: densidad, presión, presión
hidrostática, principios de Pascal y de Arquímedes, presión atmosférica.
Fuente: Guía de apoyo de Física 10° «Movimiento circular, energía, fluidos y termodinámica»,
Capítulo 3 (mecánica de fluidos); se lee en
recursos/fisica/Guías pedagógicas Física/markdown/10 - Guia_de_Apoyo_movimiento_circular_energia_fluidos_y_termodinamica_grado_10_fisica.md
Secciones: Desarrolla tus competencias, Actividades, Problemas.
DBA: los DBA de física de 10° (dba/naturales/grados/grado10.tex) no tratan fluidos; dba vacío.
Estándares 10°–11° (dba/naturales/estandares-fisica.md): «Explico el comportamiento de fluidos
en movimiento y en reposo» y «Explico aplicaciones tecnológicas del modelo de mecánica de
fluidos».
Datos: Tabla 3 de la guía (aluminio 2,7 g/cm³, mercurio 13,6 g/cm³, agua 1 g/cm³);
agua de mar 1,04 g/cm³ (dato del problema 2; la Tabla 3 dice 1, que es el agua dulce);
1 atm = 101 325 Pa; g = 9,8 m/s².
No se incluyeron: Desarrolla tus competencias 11a–11e (experiencias con hojas, moneda y
cartulina) y 12 (diseñar un experimento para medir volúmenes y densidades): son
actividades de laboratorio.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/fisica/fluidos-10.py
"""
from math import sqrt

from sympy.physics.units import (atmosphere, centimeter, convert_to, gram, kilogram, meter,
                                 newton, pascal, second)

from ejercicios import ejercicio, ejercicio_manual

PRE = "fluidos-10"
G2 = ("Guía de apoyo Física 10° (movimiento circular, energía, fluidos y termodinámica), "
      "Cap. 3 Mecánica de fluidos")
DES = f"{G2}, Desarrolla tus competencias"
ACT = f"{G2}, Actividades"
PROB = f"{G2}, Problemas"
COMUN = dict(tema="mecánica de fluidos", grados=[10], dba=[])

m, s, kg, N, Pa, cm, gr = meter, second, kilogram, newton, pascal, centimeter, gram
G = 9.8 * m / s**2
GCM3 = gr / cm**3
AGUA, MAR, HG, AL = 1 * GCM3, 1.04 * GCM3, 13.6 * GCM3, 2.7 * GCM3


def _meta(n, fuente, enunciado, respuesta, kw, tipo):
    d = dict(id=f"{PRE}-{n:03d}", fuente=fuente, enunciado=enunciado, respuesta=respuesta,
             tipo=tipo, dificultad=1, **COMUN)
    d.update(kw)
    return d


def E(n, fuente, enunciado, respuesta, **kw):
    return ejercicio(**_meta(n, fuente, enunciado, respuesta, kw, "calculo"))


def M(n, fuente, enunciado, respuesta, **kw):
    ejercicio_manual(**_meta(n, fuente, enunciado, respuesta, kw, "conceptual"))


def val(q, unidad):
    """Número de «unidad» que hay en q (unidad=1: cociente adimensional); falla si las
    dimensiones no coinciden."""
    if unidad == 1:
        return float(convert_to(q, [meter, kilogram, second]))
    return float(convert_to(q, unidad) / unidad)


def aprox(q, esperado, unidad, rel=0.01):
    v = val(q, unidad)
    assert abs(v - esperado) <= rel * abs(esperado), f"{v} ≠ {esperado}"


# ---------- Desarrolla tus competencias ----------

M(1, f"{DES} — 1",
  r"La mayoría de turistas que llegan a Colombia visitan la Sierra Nevada de Santa Marta. "
  r"¿Qué tipo de zapatos les recomendarías usar para caminar en la nieve de sus cumbres?",
  r"Zapatos (o raquetas) de suela ancha: con el mismo peso, un área de apoyo mayor produce "
  r"menos presión ($p = F/A$) y la persona se hunde menos en la nieve; además, con buen "
  r"agarre para no resbalar.")
M(2, f"{DES} — 2",
  r"Si un bañista nada a cierta profundidad y luego se sumerge al doble de esa profundidad, "
  r"¿qué sucede con la presión que soportan sus oídos?",
  r"La presión del agua ($p = \rho g h$) se duplica. La presión total (agua más atmósfera) "
  r"también aumenta, aunque menos del doble.")
M(3, f"{DES} — 3",
  r"¿En qué situación pesa más un cuerpo, cuando está en el agua o cuando está fuera de "
  r"ella?",
  r"Su peso real ($mg$) es el mismo, pero fuera del agua parece pesar más: dentro, el empuje "
  r"hacia arriba reduce su peso aparente.")
M(4, f"{DES} — 4",
  r"¿Qué condiciones deben cumplirse para que un cuerpo se hunda en un líquido?",
  r"Que su peso sea mayor que el empuje máximo (el peso del líquido que desaloja cuando está "
  r"totalmente sumergido); es decir, que su densidad media sea mayor que la del líquido.")
M(5, f"{DES} — 5",
  r"¿Por qué baja la línea de flotación de un barco cuando pasa de navegar en un río a "
  r"navegar en el mar?",
  r"El agua de mar es más densa que la del río: para producir el mismo empuje (igual al peso "
  r"del barco) necesita desalojar menos volumen, así que el barco se hunde menos y la línea "
  r"de flotación queda más abajo en el casco.")
M(6, f"{DES} — 6",
  r"Describe y explica por lo menos dos patologías circulatorias.",
  r"Hipertensión arterial: la sangre ejerce una presión anormalmente alta sobre las paredes "
  r"de las arterias, lo que obliga al corazón a trabajar más. Aterosclerosis: placas de grasa "
  r"estrechan las arterias; en el tramo estrecho la sangre va más rápido, aumenta la "
  r"resistencia al flujo y puede taparse el vaso (infarto). Várices: las válvulas de las "
  r"venas fallan y la sangre se acumula en las piernas por efecto de la presión.",
  tipo="contexto")
M(7, f"{DES} — 7",
  r"¿Por qué el granizo, a pesar de caer desde tan alto, no causa los destrozos que causaría "
  r"una caída libre desde esa altura?",
  r"Por la resistencia del aire: al aumentar su velocidad, la fuerza de arrastre crece hasta "
  r"igualar el peso y el granizo cae con una velocidad terminal pequeña (decenas de m/s), "
  r"muy lejos de los cientos de m/s que tendría en caída libre.")
M(8, f"{DES} — 8",
  r"¿Cómo se podría hacer subir un submarino sumergido en las profundidades del mar?",
  r"Expulsando el agua de sus tanques de lastre con aire comprimido: su peso (y su densidad "
  r"media) disminuye mientras el empuje sigue igual, y como el empuje queda mayor que el "
  r"peso, sube.")
for _n, _lit, _preg, _resp in [
        (9, "a", "Cuando hay derrames de petróleo, peces y otros animales mueren intoxicados. "
                 "¿A qué conduce esto?",
         "Se rompen las cadenas alimentarias: mueren o se desplazan los depredadores que "
         "dependen de esos animales, disminuye la pesca y se afectan las comunidades costeras "
         "que viven de ella."),
        (10, "b", "Explica cómo se ven afectados los ecosistemas marinos con el petróleo "
                  "flotando en la superficie.",
         "El petróleo, menos denso que el agua, forma una capa que impide el paso de la luz y "
         "el intercambio de oxígeno con el aire: el plancton no hace fotosíntesis y falta "
         "oxígeno; además impregna las plumas de las aves y la piel de los mamíferos marinos."),
        (11, "c", "¿Cómo se podría evitar la propagación del petróleo en los ecosistemas "
                  "marinos cuando ocurren estos accidentes?",
         "Con barreras flotantes que lo contengan, aprovechando que flota, y luego "
         "recogiéndolo con bombas o materiales absorbentes; también con dispersantes y con "
         "bacterias que lo degradan (biorremediación).")]:
    M(_n, f"{DES} — 9{_lit}",
      "Cuando un barco petrolero sufre un accidente, grandes cantidades de petróleo se "
      "derraman y quedan flotando sobre el agua (mareas negras). " + _preg, _resp,
      tipo="contexto")
M(12, f"{DES} — 10a",
  r"Algunas personas que escalan montañas sienten dolor de cabeza, mareo, respiración "
  r"entrecortada y taquicardia, porque el organismo intenta adaptarse a la falta de oxígeno. "
  r"¿Qué recomendaciones darías a quien quiere iniciar esta aventura por primera vez?",
  r"Subir de forma gradual para aclimatarse (pasar noches a alturas intermedias), "
  r"hidratarse, evitar esfuerzos intensos al principio y descender si los síntomas empeoran.",
  tipo="contexto")
M(13, f"{DES} — 10b",
  r"Explica a qué se debe la falta de oxígeno a medida que se asciende una montaña.",
  r"Al subir disminuye la presión atmosférica (hay menos aire encima) y el aire es menos "
  r"denso: en cada respiración entran menos moléculas de oxígeno y la menor presión del "
  r"oxígeno hace que pase menos a la sangre.")
M(14, f"{DES} — 13a",
  r"¿De qué manera se usa la mecánica de fluidos en un taller automotriz?",
  r"En el gato y el elevador hidráulicos y en los frenos hidráulicos (principio de Pascal), "
  r"en los compresores y herramientas neumáticas, y al medir la presión de las llantas.",
  tipo="contexto")
M(15, f"{DES} — 13b",
  r"¿De qué manera se usa la mecánica de fluidos para entender la circulación de la sangre "
  r"en el cuerpo humano?",
  r"El corazón funciona como una bomba que crea diferencias de presión; la sangre fluye de "
  r"mayor a menor presión, más rápido donde los vasos son más estrechos (ecuación de "
  r"continuidad); el tensiómetro mide la presión arterial.", tipo="contexto")

# ---------- Actividades ----------

for _n, _lit, _af, _resp in [
        (16, "a", "Es más fácil mover un objeto en una piscina cuando está desocupada que "
                  "cuando está llena.",
         "F: con la piscina llena, el empuje del agua reduce el peso aparente del objeto y es "
         "más fácil levantarlo o moverlo (aunque arrastrarlo rápido cuesta más por la "
         "resistencia del agua)."),
        (17, "b", "Hay mayor presión atmosférica en Bogotá que en Barranquilla.",
         "F: Bogotá está a unos 2600 m de altura y tiene menos aire encima; Barranquilla, a "
         "nivel del mar, tiene mayor presión atmosférica."),
        (18, "c", "Un balón de fútbol ejerce la misma presión sin importar su posición sobre "
                  "el césped.",
         "V: es una esfera; en cualquier posición apoya igual área con el mismo peso."),
        (19, "d", "Existe mayor cantidad de objetos que pueden flotar en mercurio que en agua.",
         "V: el mercurio ($\\num{13,6}\\ \\mathrm{g/cm^3}$) es mucho más denso que el agua; "
         "en él flota todo lo que tenga menor densidad, incluso metales como el hierro."),
        (20, "e", "Un poste de la luz ejerce mayor presión sobre la tierra cuando se instala "
                  "(parado) que cuando está acostado.",
         "V: con el mismo peso, parado se apoya en un área mucho menor (su base)."),
        (21, "f", "En una prensa hidráulica, al aplicar una fuerza en un punto se genera en "
                  "otro punto una fuerza menor.",
         "F: la presión se transmite igual y en el émbolo grande se obtiene una fuerza mayor: "
         "$F_2 = F_1 A_2/A_1$."),
        (22, "g", "Ejerce mayor presión sobre la nieve una persona con zapatos de "
                  "$150\\ \\mathrm{cm^2}$ de área que con otros de $200\\ \\mathrm{cm^2}$.",
         "V: con el mismo peso, a menor área, mayor presión.")]:
    M(_n, f"{ACT} — 1{_lit}",
      "Escribe V si la afirmación es verdadera o F si es falsa, y justifica: " + _af, _resp)

for _n, _lit, _preg, _resp in [
        (23, "a", "¿Qué son los vasos comunicantes?",
         "Recipientes unidos por su parte inferior. Un mismo líquido en reposo alcanza en "
         "todos el mismo nivel, porque la presión es igual a la misma profundidad."),
        (24, "b", "¿Para qué sirve una prensa hidráulica?",
         "Para multiplicar fuerzas usando el principio de Pascal: una fuerza pequeña sobre "
         "un émbolo pequeño produce una fuerza grande sobre un émbolo grande (gatos, "
         "elevadores de autos, prensas)."),
        (25, "c", "¿Es igual el peso de un cuerpo que su peso específico? Explica.",
         "No: el peso es la fuerza con que la Tierra lo atrae ($mg$, en N); el peso "
         "específico es el peso por unidad de volumen ($\\rho g$, en $\\mathrm{N/m^3}$)."),
        (26, "d", "¿Cómo se define el peso aparente?",
         "Es el peso real de un cuerpo sumergido menos el empuje del fluido: "
         "$W_{\\text{ap}} = mg - E$."),
        (27, "e", "¿Qué volumen tiene sumergido un cuerpo que flota?",
         "El necesario para que el peso del líquido desalojado sea igual al peso del cuerpo: "
         "$V_{\\text{sum}} = V\\,\\rho_{\\text{cuerpo}}/\\rho_{\\text{líquido}}$."),
        (28, "f", "¿Qué es un picnómetro?",
         "Un frasco de vidrio de volumen conocido con gran exactitud que se usa para medir la "
         "densidad de líquidos (y de sólidos en polvo)."),
        (29, "g", "¿Qué es un barómetro?", "Un instrumento para medir la presión atmosférica."),
        (30, "h", "¿En qué consistió el experimento de Torricelli?",
         "Llenó de mercurio un tubo de 1 m cerrado por un extremo y lo invirtió en una cubeta "
         "con mercurio: la columna bajó hasta unos 76 cm a nivel del mar. La presión "
         "atmosférica sostiene esa columna: $1\\ \\text{atm} = 76\\ \\text{cm de Hg}$.")]:
    M(_n, f"{ACT} — 2{_lit}", _preg, _resp)

for _n, _num, _preg, _resp in [
        (31, 3, "Un globo se eleva cuando se calienta el aire de su interior. Explica la razón.",
         "El aire caliente es menos denso que el aire frío de afuera: el peso del globo con su "
         "aire interior queda menor que el empuje del aire exterior que desaloja."),
        (32, 4, "Explica lo que le pasa a una persona que se sumerge a gran profundidad en el "
                "agua.",
         "La presión hidrostática aumenta con la profundidad ($\\rho g h$): comprime el pecho, "
         "los oídos y los pulmones, y hace que se disuelva más gas (nitrógeno) en la sangre."),
        (33, 5, "Investiga por qué un buzo debe ascender lentamente desde el fondo del mar.",
         "Porque a gran profundidad se disuelve mucho nitrógeno en su sangre; si sube rápido, "
         "la presión baja de golpe y el gas forma burbujas en la sangre y los tejidos "
         "(enfermedad por descompresión). Subiendo despacio, el gas se elimina por los "
         "pulmones."),
        (34, 6, "Explica por qué una bola de billar puede flotar sobre mercurio.",
         "Su densidad (unos $2\\ \\mathrm{g/cm^3}$) es mucho menor que la del mercurio "
         "($\\num{13,6}\\ \\mathrm{g/cm^3}$): el empuje iguala su peso con solo una pequeña "
         "parte sumergida."),
        (35, 7, "Explica por qué un globo lleno de aire se revienta cuando se le presiona con "
                "la punta de una aguja y no con un trozo de madera.",
         "Con la misma fuerza, la punta de la aguja tiene un área muy pequeña y produce una "
         "presión enorme ($p = F/A$) que rompe el caucho; la madera reparte la fuerza en un "
         "área mucho mayor."),
        (36, 8, "El mar Muerto tiene una salinidad muy alta. ¿Por qué una persona flota con "
                "mayor facilidad en él que en cualquier otro lago?",
         "El agua tan salada es mucho más densa: el empuje que iguala el peso de la persona se "
         "logra con menos volumen sumergido, así que flota más alto."),
        (37, 9, "¿Qué le sucede a la densidad de un trozo de madera uniforme cuando se corta en "
                "tres partes iguales?",
         "Nada: cada parte tiene un tercio de la masa y un tercio del volumen; la densidad es "
         "una propiedad del material, no del tamaño."),
        (38, 10, "Los submarinos resisten una presión hidrostática máxima. Explica qué le "
                 "pasaría a un submarino a mayor profundidad de la prevista.",
         "La presión del agua superaría la resistencia de su casco: se deformaría y podría "
         "colapsar hacia adentro (implosión)."),
        (39, 11, "Explica qué sucede con la presión en el fondo de un vaso de agua si se tapa "
                 "la parte superior del vaso.",
         "No cambia, mientras el aire que queda encerrado siga a la presión atmosférica: la "
         "presión en el fondo es la del aire más $\\rho g h$."),
        (40, 12, "Si el peso y el empuje son iguales, ¿un cuerpo puede flotar? Explica.",
         "Sí: la fuerza neta es cero y el cuerpo queda en equilibrio, flotando en la superficie "
         "o suspendido dentro del líquido si su densidad es igual a la del líquido."),
        (41, 13, "Un bañista se sumerge hasta el fondo de una piscina con un globo inflado. "
                 "¿Qué le pasará al volumen del globo a medida que baja?",
         "Disminuye: la presión del agua aumenta con la profundidad y comprime el aire del "
         "globo (a mayor presión, menor volumen del gas)."),
        (42, 14, "¿Por qué el aire es más denso en lugares como La Guajira o Cartagena que en "
                 "Bogotá o Pasto?",
         "Porque están a nivel del mar: tienen más aire encima, la presión atmosférica es mayor "
         "y el aire está más comprimido. En Bogotá y Pasto, a más de 2500 m, la presión es "
         "menor y el aire menos denso.")]:
    M(_n, f"{ACT} — {_num}", _preg, _resp)

# ---------- Problemas ----------


@E(43, f"{PROB} — 1",
   enunciado=r"¿Cuál es el volumen que ocupan $\num{1000}$ g de aluminio "
             r"($\rho = \num{2,7}\ \mathrm{g/cm^3}$)?",
   respuesta=r"$V = \dfrac{m}{\rho} = \dfrac{1000}{\num{2,7}} \approx 370\ \mathrm{cm^3}$.")
def _():
    aprox(1000 * gr / AL, 370.4, cm**3, rel=0.001)


@E(44, f"{PROB} — 2", tipo="contexto", dificultad=2,
   enunciado=r"La presión máxima que soporta una persona normal es de 8 atm. ¿Cuál es la "
             r"profundidad máxima a la que puede descender en el mar sin correr peligro? La "
             r"densidad del agua de mar es $\num{1,04}\ \mathrm{g/cm^3}$.",
   respuesta=r"En la superficie ya hay 1 atm, así que el agua puede aportar 7 atm: "
             r"$h = \dfrac{7(\num{101325})}{1040(\num{9,8})} \approx 70$ m.",
   notas="Se interpreta 8 atm como presión total (absoluta). Si fuera solo la del agua, "
         "h ≈ 80 m.")
def _():
    aprox(7 * atmosphere / (MAR * G), 69.6, m, rel=0.002)
    aprox(8 * atmosphere / (MAR * G), 79.5, m, rel=0.002)


@E(45, f"{PROB} — 3", tipo="contexto",
   enunciado=r"Una lancha tiene un volumen de $5\ \mathrm{m^3}$. ¿Cuántas personas de 50 kg "
             r"puede llevar sin hundirse en el mar ($\rho = \num{1,04}\ \mathrm{g/cm^3}$)? "
             r"Desprecia la masa de la lancha.",
   respuesta=r"El empuje máximo equivale a $5 \times 1040 = 5200$ kg de agua desalojada: "
             r"$5200/50 = 104$ personas (menos, si se cuenta la masa de la lancha).",
   notas="La guía no da la masa de la lancha ni la densidad del mar; se usa 1,04 g/cm³ "
         "(como en el problema 2). La Tabla 3 de la guía dice «agua de mar: 1», que es el "
         "valor del agua dulce (el real es ≈ 1,03 g/cm³).")
def _():
    masa = MAR * 5 * m**3
    aprox(masa, 5200, kg, rel=1e-9)
    assert int(val(masa / (50 * kg), 1) + 1e-9) == 104


@E(46, f"{PROB} — 4",
   enunciado=r"La densidad del osmio es $\num{22,6}\ \mathrm{g/cm^3}$ y la del aluminio "
             r"$\num{2,7}\ \mathrm{g/cm^3}$. ¿Cuántas veces mayor es el volumen de 100 g de "
             r"aluminio que el de 100 g de osmio?",
   respuesta=r"$\dfrac{V_{Al}}{V_{Os}} = \dfrac{\num{22,6}}{\num{2,7}} \approx \num{8,4}$ veces.")
def _():
    aprox((100 * gr / AL) / (100 * gr / (22.6 * GCM3)), 8.37, 1, rel=0.002)


@E(47, f"{PROB} — 5", tipo="contexto", dificultad=2,
   enunciado=r"Un hombre que pesa 800 N está de pie sobre una superficie cuadrada de 4 m de "
             r"lado. Si se carga al hombro un saco de 40 kg, ¿cuánto debe medir la superficie "
             r"de apoyo para que la presión sea la misma?",
   respuesta=r"Presión inicial: $800/16 = 50$ Pa. Con el saco, el peso es $800 + 392 = 1192$ N: "
             r"$A = 1192/50 \approx \num{23,8}\ \mathrm{m^2}$, un cuadrado de unos "
             r"$\num{4,9}$ m de lado.",
   notas="Dato de la guía conservado; un apoyo de 16 m² para una persona es irreal (quizá "
         "quiso decir 40 cm de lado: el resultado sería 48,8 cm de lado).")
def _():
    p = 800 * N / (4 * m)**2
    a = (800 + val(40 * kg * G, N)) * N / p
    aprox(a, 23.84, m**2, rel=0.001)
    assert abs(sqrt(val(a, m**2)) - 4.88) < 0.005


@E(48, f"{PROB} — 6",
   enunciado=r"Calcula la presión que ejerce un cuerpo de 120 kg apoyado sobre una superficie de "
             r"$\num{0,8}\ \mathrm{m^2}$. ¿Qué presión ejercería si estuviera apoyado sobre "
             r"$\num{1,2}\ \mathrm{m^2}$? Compara y saca conclusiones.",
   respuesta=r"$p_1 = \dfrac{120(\num{9,8})}{\num{0,8}} = 1470$ Pa; $p_2 = \dfrac{1176}"
             r"{\num{1,2}} = 980$ Pa. Con el mismo peso, a mayor área de apoyo, menor presión "
             r"(son inversamente proporcionales).")
def _():
    peso = 120 * kg * G
    aprox(peso / (0.8 * m**2), 1470, Pa, rel=1e-9)
    aprox(peso / (1.2 * m**2), 980, Pa, rel=1e-9)


@E(49, f"{PROB} — 7",
   enunciado=r"Se ejerce una fuerza de 25 N sobre el émbolo de una jeringa de "
             r"$\num{2,5e-4}\ \mathrm{m^2}$ de área. Si el fluido no puede salir, ¿cuál es la "
             r"presión dentro de la jeringa (debida a la fuerza)?",
   respuesta=r"$p = F/A = 25/\num{2,5e-4} = \num{1,0e5}$ Pa (unas 1 atm, además de la "
             r"atmosférica).",
   notas="En la guía falta el número del área («un área de ×10⁻⁴ m²»); se eligió 2,5×10⁻⁴ m² "
         "(unos 2,5 cm², tamaño realista). La docente puede cambiarlo.")
def _():
    aprox(25 * N / (2.5e-4 * m**2), 1.0e5, Pa, rel=1e-9)


@E(50, f"{PROB} — 8",
   enunciado=r"Un cilindro con agua está tapado por un pistón de $\num{0,2}$ kg y "
             r"$\num{0,008}\ \mathrm{m^2}$ de área. Si la atmósfera ejerce 100 kPa sobre el "
             r"pistón, calcula la presión total sobre la superficie del agua (justo debajo "
             r"del pistón).",
   respuesta=r"$p = p_{\text{atm}} + \dfrac{mg}{A} = \num{100000} + \dfrac{\num{0,2}(\num{9,8})}"
             r"{\num{0,008}} = \num{100245}$ Pa $\approx \num{100,2}$ kPa. (En la base habría "
             r"que sumar $\rho g h$ del agua).",
   notas="La guía pide la presión «en la base del cilindro» pero no da la altura del agua; se "
         "pregunta por la presión sobre la superficie del agua.")
def _():
    aprox(100e3 * Pa + 0.2 * kg * G / (0.008 * m**2), 100245, Pa, rel=1e-9)


@E(51, f"{PROB} — 9",
   enunciado=r"Calcula la presión hidrostática en un punto situado a 15 m de profundidad en "
             r"agua ($\rho = 1000\ \mathrm{kg/m^3}$), y la diferencia de presiones entre dos "
             r"puntos a 10 m y 13 m de profundidad.",
   respuesta=r"$p = \rho g h = 1000(\num{9,8})(15) = \num{1,47e5}$ Pa; "
             r"$\Delta p = \rho g\,\Delta h = 1000(\num{9,8})(3) = \num{2,94e4}$ Pa.")
def _():
    aprox(AGUA * G * 15 * m, 1.47e5, Pa, rel=1e-9)
    aprox(AGUA * G * (13 - 10) * m, 2.94e4, Pa, rel=1e-9)


@E(52, f"{PROB} — 10", dificultad=2,
   enunciado=r"En un tubo en U hay agua y mercurio. Si la columna de agua mide "
             r"$\num{31,5}$ cm por encima de la superficie de separación, ¿cuál es la altura "
             r"$h$ del mercurio, medida desde ese mismo nivel, en el otro brazo, cuando el "
             r"sistema está en equilibrio?",
   respuesta=r"A la misma altura las presiones son iguales: $\rho_{\text{agua}}h_{\text{agua}} = "
             r"\rho_{Hg}h$, así que $h = \dfrac{\num{31,5}}{\num{13,6}} \approx \num{2,3}$ cm.",
   notas="La guía remite a una figura que no está descrita; se precisa desde dónde se miden "
         "las alturas.")
def _():
    aprox(AGUA * 31.5 * cm / HG, 2.316, cm, rel=0.002)


@E(53, f"{PROB} — 11",
   enunciado=r"En un tubo en U hay agua y mercurio. Si la columna de mercurio mide 13 cm por "
             r"encima de la superficie de separación, ¿qué altura alcanza el agua, medida "
             r"desde ese mismo nivel?",
   respuesta=r"$h_{\text{agua}} = \dfrac{\rho_{Hg}}{\rho_{\text{agua}}}h_{Hg} = "
             r"\num{13,6}(13) \approx 177$ cm ($\approx \num{1,77}$ m).")
def _():
    aprox(HG * 13 * cm / AGUA, 176.8, cm, rel=1e-6)


@E(54, f"{PROB} — 12",
   enunciado=r"¿Cuál debe ser la densidad, en $\mathrm{g/cm^3}$, de una roca que flota en un "
             r"océano de densidad $\num{1027}\ \mathrm{kg/m^3}$, si el 20\,\% de su volumen "
             r"queda fuera del agua?",
   respuesta=r"Flotando, $\rho_{\text{roca}}V = \rho_{\text{mar}}(\num{0,8}V)$: "
             r"$\rho = \num{0,8}(1027) \approx 822\ \mathrm{kg/m^3} \approx \num{0,82}\ "
             r"\mathrm{g/cm^3}$ (una piedra pómez, por ejemplo).")
def _():
    aprox(0.8 * 1027 * kg / m**3, 0.82, GCM3, rel=0.003)


@E(55, f"{PROB} — 13",
   enunciado=r"Convierte $\num{35000}$ pascales a atmósferas.",
   respuesta=r"$\dfrac{\num{35000}}{\num{101325}} \approx \num{0,345}$ atm.")
def _():
    aprox(35000 * Pa, 0.345, atmosphere, rel=0.002)


@E(56, f"{PROB} — 14", tipo="contexto",
   enunciado=r"¿Qué altura debe tener un tubo para hacer el experimento de Torricelli con agua "
             r"en vez de mercurio?",
   respuesta=r"La columna debe equilibrar 1 atm: $h = \dfrac{\num{101325}}{1000(\num{9,8})} "
             r"\approx \num{10,3}$ m (13,6 veces los 76 cm de mercurio).")
def _():
    aprox(1 * atmosphere / (AGUA * G), 10.34, m, rel=0.002)
    aprox(HG * 76 * cm / AGUA, 10.34, m, rel=0.002)
