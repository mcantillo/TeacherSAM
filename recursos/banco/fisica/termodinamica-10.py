"""Banco de ejercicios — Física 10° — Termodinámica: calor y temperatura, escalas, calorimetría,
equilibrio térmico, transmisión del calor y dilatación.
Fuente: Guía de apoyo de Física 10° «Movimiento circular, energía, fluidos y termodinámica»,
Capítulo 4 (termodinámica); se lee en
recursos/fisica/Guías pedagógicas Física/markdown/10 - Guia_de_Apoyo_movimiento_circular_energia_fluidos_y_termodinamica_grado_10_fisica.md
Secciones: Desarrolla tus competencias, Actividades, Problemas.
DBA: los DBA de física de 10° no tratan calor ni temperatura; dba vacío. Estándar 10°–11°
(dba/naturales/estandares-fisica.md): «Explico la transformación de energía mecánica en energía
térmica».
Datos: Tablas 4 y 6 de la guía (calor específico del agua 1 cal/g·°C; α del hierro
12×10⁻⁶ °C⁻¹); 1 cal = 4,186 J. Las conversiones de temperatura se comprueban con aritmética
exacta (sympy.physics.units no maneja escalas con cero desplazado); la dilatación y el calor,
con unidades.
No se incluyó: Desarrolla tus competencias 5 (experimento con tres vasos de agua): es una
actividad práctica.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/fisica/termodinamica-10.py
"""
from sympy import Rational, solve, symbols
from sympy.physics.units import (centimeter, convert_to, gram, joule, kelvin, kilogram, liter,
                                 meter, minute, second)

from ejercicios import ejercicio, ejercicio_manual

PRE = "termodinamica-10"
G2 = ("Guía de apoyo Física 10° (movimiento circular, energía, fluidos y termodinámica), "
      "Cap. 4 Termodinámica")
DES = f"{G2}, Desarrolla tus competencias"
ACT = f"{G2}, Actividades"
PROB = f"{G2}, Problemas"
COMUN = dict(tema="calor y temperatura", grados=[10], dba=[])

m, cm, K = meter, centimeter, kelvin
CAL = Rational("4.186") * joule


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
        return float(convert_to(q, [meter, kilogram, second, kelvin]))
    return float(convert_to(q, unidad) / unidad)


def aprox(q, esperado, unidad, rel=0.01):
    v = val(q, unidad)
    assert abs(v - esperado) <= rel * abs(esperado), f"{v} ≠ {esperado}"


def c_a_k(c):
    return Rational(str(c)) + Rational("273.15")


def f_a_c(f):
    return (Rational(str(f)) - 32) * Rational(5, 9)


# ---------- Desarrolla tus competencias ----------

M(1, f"{DES} — 1", tipo="seleccion",
  enunciado=r"Un termo consta de dos recipientes separados por una zona de vacío; cada "
            r"recipiente y la zona de vacío evitan una forma de propagación del calor. Los "
            r"recipientes del termo cumplen la función de:" +
            op("propagar el calor más rápido de lo normal.",
               "aislar térmicamente del interior las sustancias más calientes del exterior.",
               "aislar térmicamente del exterior las sustancias del interior, manteniendo su "
               "temperatura.", "conducir el calor lentamente."),
  respuesta=r"c) Aislar del exterior lo que hay adentro para que conserve su temperatura: el "
            r"vacío impide la conducción y la convección, y las paredes plateadas reflejan la "
            r"radiación.")
M(2, f"{DES} — 2", tipo="seleccion",
  enunciado=r"Un alumno dice que al abrir la ventana sintió cómo el frío entraba a su cuerpo. "
            r"¿Cuál es la verdadera razón de su sensación de frío?" +
            op("El aire tiene menor temperatura que su cuerpo y por eso se propaga más rápido.",
               "La temperatura de su cuerpo, mayor que la del ambiente, se disipó al exterior.",
               "El calor de su cuerpo pasa al ambiente, porque la temperatura del niño es mayor "
               "que la del aire exterior.",
               "La temperatura del aire es igual a la del cuerpo."),
  respuesta=r"c) El calor (energía) pasa de su cuerpo, más caliente, al aire, más frío. No "
            r"«entra frío» ni se «disipa la temperatura»: lo que se transfiere es calor.")
M(3, f"{DES} — 3", tipo="seleccion",
  enunciado=r"Las corrientes de aire frío y caliente dentro de un refrigerador se deben a:" +
            op("la radiación del calor.", "las corrientes de convección.",
               "un proceso de conducción.", "radiaciones electromagnéticas."),
  respuesta=r"b) Corrientes de convección: el aire frío, más denso, baja y el caliente sube.")
for _n, _lit, _caso, _resp in [
        (4, "a", "Calentamiento del agua de mar por la energía que viene del Sol.",
         "Radiación (luego la convección reparte el calor en el agua)."),
        (5, "b", "Aumento de temperatura al calentar agua en una estufa eléctrica.",
         "Conducción de la resistencia a la olla y de la olla al agua; dentro del agua, "
         "convección."),
        (6, "c", "Calentamiento de una viga metálica en un incendio.",
         "Radiación y convección de las llamas y los gases calientes hacia la viga, y "
         "conducción a lo largo del metal."),
        (7, "d", "Aumento de temperatura de una persona cuando entra a un baño turco.",
         "Convección: el vapor caliente que circula le transfiere calor (y se condensa sobre "
         "la piel)."),
        (8, "e", "Calentamiento del aire en un globo.",
         "Convección: el aire calentado por el quemador sube y circula dentro del globo.")]:
    M(_n, f"{DES} — 4{_lit}",
      "Indica el mecanismo de transferencia de energía térmica que ocurre: " + _caso, _resp)
for _n, _lit, _af, _resp in [
        (9, "a", "Cuanto mayor es la masa de un cuerpo, mayor es el calor específico de la "
                 "sustancia que lo forma.",
         "F: el calor específico es una propiedad de la sustancia; lo que crece con la masa "
         "es la capacidad calorífica ($mc$)."),
        (10, "b", "Si envolvemos un trozo de hielo en un abrigo de piel, se derrite más rápido "
                  "porque la piel calienta.",
         "F: la piel es un aislante; reduce el paso de calor del ambiente al hielo, que se "
         "derrite más despacio. El abrigo no produce calor."),
        (11, "c", "El calor se propaga en el vacío por radiación.", "V."),
        (12, "d", "El calor es una medida de la energía cinética que poseen las moléculas de "
                  "un cuerpo.",
         "F: esa es la temperatura (mide la energía cinética promedio). El calor es energía "
         "en tránsito entre cuerpos a distinta temperatura."),
        (13, "e", "La unidad de calor específico en el Sistema Internacional es cal/g·°C.",
         r"F: en el SI es $\mathrm{J/(kg\cdot K)}$; cal/g·°C es una unidad práctica.")]:
    M(_n, f"{DES} — 6{_lit}",
      "Escribe V si la afirmación es verdadera o F si es falsa, y justifica: " + _af, _resp)
M(14, f"{DES} — 7",
  r"Investiga sobre el termostato: ¿qué fenómeno lo hace útil y en qué aparatos se usa?",
  r"Usa la dilatación térmica: una lámina bimetálica (dos metales que se dilatan distinto) "
  r"se curva al calentarse y abre o cierra un circuito eléctrico. Se usa en planchas, "
  r"neveras, hornos, calentadores de agua y aires acondicionados para mantener una "
  r"temperatura.", tipo="contexto")
M(15, f"{DES} — 8a",
  r"Si tocamos un trozo de mármol y otro de madera a la misma temperatura, la madera parece "
  r"estar más caliente. Explica por qué se tiene esta sensación.",
  r"El mármol conduce el calor mucho mejor que la madera: saca calor de la mano más rápido y "
  r"la sentimos enfriarse. La piel percibe la rapidez con que pierde calor, no la "
  r"temperatura del objeto.")
M(16, f"{DES} — 8b",
  r"¿Cómo se podría comprobar si la sensación de que la madera está más caliente que el "
  r"mármol coincide con la realidad?",
  r"Midiendo la temperatura de los dos con un termómetro: marcan lo mismo (están en "
  r"equilibrio con el ambiente), lo que muestra que la sensación no coincide con la "
  r"realidad.")

# ---------- Actividades ----------

M(17, f"{ACT} — 1", r"Siempre que un cuerpo recibe calor, ¿aumenta su temperatura?",
  r"No: durante un cambio de estado recibe calor sin cambiar su temperatura; por ejemplo, el "
  r"hielo que se funde a $0\,^\circ$C.")
M(18, f"{ACT} — 2", r"Si un cuerpo pierde calor, ¿disminuye necesariamente su temperatura?",
  r"No: al solidificarse o condensarse cede calor a temperatura constante (el agua que se "
  r"congela a $0\,^\circ$C).")
M(19, f"{ACT} — 3",
  r"En el experimento de Joule, ¿qué pasa con la energía de la pesa? ¿De dónde procede el "
  r"calor que aumenta la temperatura del agua?",
  r"La pesa, al bajar, pierde energía potencial; esa energía mueve unas paletas que agitan el "
  r"agua y, por el rozamiento, se convierte en energía interna del agua. El «calor» viene del "
  r"trabajo mecánico: así Joule mostró que el calor es una forma de energía.")

for _n, _lit, _ti, _tf, _resp in [
        (20, "a", "100 °C", "200 °C",
         r"$\num{373,15}$ K y $\num{473,15}$ K; diferencia: $100\,^\circ$C $= 100$ K."),
        (21, "b", "273 K", "300 K",
         r"$-\num{0,15}\,^\circ$C y $\num{26,85}\,^\circ$C; diferencia: $27\,^\circ$C "
         r"$= 27$ K."),
        (22, "c", "300 K", "30 °C",
         r"$\num{26,85}\,^\circ$C $= 300$ K y $30\,^\circ$C $= \num{303,15}$ K; diferencia: "
         r"$\num{3,15}\,^\circ$C $= \num{3,15}$ K."),
        (23, "d", "230 °C", "200 °C",
         r"$\num{503,15}$ K y $\num{473,15}$ K; diferencia: $-30\,^\circ$C $= -30$ K.")]:
    @E(_n, f"{ACT} — 4{_lit}",
       enunciado=rf"Expresa en °C y en kelvin la temperatura inicial ({_ti}) y la final "
                 rf"({_tf}), y la diferencia de temperaturas en °C y en K.",
       respuesta=_resp)
    def _(lit=_lit):
        casos = {"a": (c_a_k(100), c_a_k(200)), "b": (Rational(273), Rational(300)),
                 "c": (Rational(300), c_a_k(30)), "d": (c_a_k(230), c_a_k(200))}
        ti, tf = casos[lit]
        dif = {"a": 100, "b": 27, "c": Rational("3.15"), "d": -30}[lit]
        assert tf - ti == dif                                   # igual en K y en °C
        assert (tf - Rational("273.15")) - (ti - Rational("273.15")) == dif


@E(24, f"{ACT} — 5",
   enunciado=r"Escribe de menor a mayor las temperaturas: $100\,^\circ$C, 350 K y "
             r"$200\,^\circ$F.",
   respuesta=r"$350\ \text{K} = \num{76,85}\,^\circ$C $< 200\,^\circ$F $\approx "
             r"\num{93,3}\,^\circ$C $< 100\,^\circ$C.")
def _():
    t = {"100 °C": Rational(100), "350 K": Rational(350) - Rational("273.15"),
         "200 °F": f_a_c(200)}
    assert sorted(t, key=t.get) == ["350 K", "200 °F", "100 °C"]


for _n, _lit, _af, _resp in [
        (25, "a", "Su unidad en el SI es el julio.", "Calor (la de la temperatura es el kelvin)."),
        (26, "b", "Se mide con un termómetro.", "Temperatura."),
        (27, "c", "Depende de la masa.", "Calor: para un mismo cambio de temperatura, a más "
                                         "masa, más calor ($Q = mc\\Delta T$)."),
        (28, "d", "Es una forma de energía.", "Calor (energía en tránsito)."),
        (29, "e", "Se mide con un calorímetro.", "Calor."),
        (30, "f", "No depende de la masa.", "Temperatura."),
        (31, "g", "Se expresa en grados.", "Temperatura."),
        (32, "h", "Es una medida de la energía interna.",
         "Temperatura: mide la energía cinética promedio de las partículas, que forma parte "
         "de la energía interna.")]:
    M(_n, f"{ACT} — 6{_lit}",
      "Indica si el enunciado corresponde a calor o a temperatura: " + _af, _resp)


@E(33, f"{ACT} — 7", tipo="argumentacion",
   enunciado=r"¿Es correcto afirmar que las diferencias de temperatura tienen el mismo valor en "
             r"grados Celsius que en kelvin?",
   respuesta=r"Sí: $T_K = T_C + \num{273,15}$, así que al restar dos temperaturas el "
             r"$\num{273,15}$ se cancela; un grado Celsius y un kelvin tienen el mismo tamaño.")
def _():
    a, b = symbols("a b", real=True)
    assert ((b + Rational("273.15")) - (a + Rational("273.15"))).expand() == b - a


M(34, f"{ACT} — 8",
  r"¿Por qué la temperatura de las estrellas puede llegar a millones de grados y, en cambio, "
  r"no se pueden obtener temperaturas por debajo de 0 K ($-\num{273,15}\,^\circ$C)?",
  r"La temperatura mide la agitación (energía cinética promedio) de las partículas: puede "
  r"crecer sin límite conocido, pero no puede bajar de la agitación mínima, que corresponde "
  r"al cero absoluto, 0 K.")
for _n, _lit, _preg, _resp in [
        (35, "a", "¿Qué bola atravesará primero la lámina?",
         "La de cobre: tiene el mayor calor específico, así que al enfriarse cede más calor "
         "a la cera ($Q = mc\\Delta T$, con igual $m$ y $\\Delta T$) y la funde antes."),
        (36, "b", "¿Cuál lo hará de última? Justifica.",
         "La de plomo, que tiene el menor calor específico y cede menos calor.")]:
    @E(_n, f"{ACT} — 9{_lit}", tipo="argumentacion",
       enunciado=r"Tres bolas de igual masa, de cobre, plomo y estaño, a $60\,^\circ$C, se "
                 r"colocan sobre una lámina delgada de cera. Calores específicos: cobre "
                 r"$\num{0,093}$, estaño $\num{0,054}$ y plomo $\num{0,031}$ cal/g·°C. " + _preg,
       respuesta=_resp,
       notas="La guía no da los calores específicos del plomo ni del estaño (su Tabla 4 solo "
             "trae el cobre, 0,09); se agregan los valores usuales.")
    def _(lit=_lit):
        c = {"cobre": 0.093, "estaño": 0.054, "plomo": 0.031}
        q = {k: 100 * gram * v * CAL / (gram * K) * 10 * K for k, v in c.items()}
        orden = sorted(q, key=lambda k: val(q[k], joule), reverse=True)
        assert orden[0] == "cobre" and orden[-1] == "plomo"

M(37, f"{ACT} — 10", r"¿Por qué se usa agua como refrigerante de los motores de los automóviles?",
  r"Porque tiene un calor específico muy alto: absorbe mucho calor del motor con poco aumento "
  r"de temperatura; además es barata y fluye con facilidad.")
M(38, f"{ACT} — 11",
  r"Si llenas un globo con agua y lo pones en contacto con una llama, ¿qué crees que sucederá?",
  r"El globo no se revienta (al menos por un buen rato): el agua absorbe el calor que el "
  r"caucho recibe de la llama y, por su alto calor específico, mantiene el caucho por debajo "
  r"de la temperatura a la que se daña.")
M(39, f"{ACT} — 12", r"Explica qué significa que un cuerpo tenga mayor calor específico que otro.",
  r"Que necesita más calor para elevar en $1\,^\circ$C la temperatura de la misma masa; "
  r"también se calienta y se enfría más despacio.")
M(40, f"{ACT} — 13", r"Explica por qué un termo puede mantener caliente el agua.",
  r"Su doble pared con vacío impide la conducción y la convección, sus paredes plateadas "
  r"reflejan la radiación y la tapa evita que el aire caliente escape.")
M(41, f"{ACT} — 14",
  r"Dos recipientes iguales, uno negro y otro blanco (o plateado), se llenan con agua "
  r"caliente. La temperatura del recipiente negro disminuye más rápido. ¿A qué se debe?",
  r"Las superficies negras son buenas emisoras de radiación (y buenas absorbentes): el "
  r"recipiente negro pierde calor por radiación más rápido que el claro.",
  notas="La guía remite a una figura; se describió en el enunciado (recipiente negro y otro "
        "claro).")
M(42, f"{ACT} — 15",
  r"¿Existe algún límite para la temperatura más alta que se puede alcanzar? ¿Y para la más "
  r"baja?",
  r"No se conoce un límite superior (las estrellas llegan a millones de grados). El límite "
  r"inferior es el cero absoluto, 0 K ($-\num{273,15}\,^\circ$C), al que uno se puede "
  r"acercar pero nunca llegar.")
M(43, f"{ACT} — 16",
  r"Si se deja un refrigerador con la puerta abierta dentro de un cuarto cerrado, ¿se "
  r"enfriará la habitación?",
  r"No, se calentará: el refrigerador saca calor de su interior y lo expulsa por la parte de "
  r"atrás al mismo cuarto, y además su motor convierte energía eléctrica en calor.")
M(44, f"{ACT} — 17",
  r"Mientras las manos se frotan, ¿cuál de ellas se calienta? ¿Pasa calor de una a la otra "
  r"o las dos reciben calor a la vez? ¿De dónde proviene ese calor?",
  r"Las dos se calientan a la vez; no pasa calor de una a otra, porque están a la misma "
  r"temperatura. La energía viene del trabajo del rozamiento: la energía mecánica se "
  r"transforma en energía térmica.")
M(45, f"{ACT} — 18",
  r"Dos cafeteras de igual forma contienen cada una un litro de café a $70\,^\circ$C; una es "
  r"de aluminio y la otra de acero inoxidable. Pasados unos minutos, ¿de cuál servirías el "
  r"café? Pasado mucho tiempo, ¿importaría cuál elegir?",
  r"Pasados unos minutos, de la de acero inoxidable: conduce peor el calor y el café se "
  r"enfría más despacio que en la de aluminio. Pasado mucho tiempo da igual: las dos llegan a "
  r"la temperatura ambiente.")
M(46, f"{ACT} — 19",
  r"Cuando una persona siente frío tiende a temblar o sentir escalofríos. ¿Cómo justificas "
  r"este comportamiento?",
  r"Temblar es contraer los músculos muchas veces seguidas: ese trabajo muscular transforma "
  r"energía química en calor y ayuda a mantener la temperatura del cuerpo.")


@E(47, f"{ACT} — 20", tipo="argumentacion",
   enunciado=r"Se quiere hervir el agua de un vaso y el agua de una caneca. Si inicialmente "
             r"están a la misma temperatura, ¿a cuál hay que darle más calor?",
   respuesta=r"A la de la caneca: el calor necesario es $Q = mc\Delta T$, con igual $c$ y "
             r"$\Delta T$, y la caneca tiene mucha más masa de agua.")
def _():
    c, dt = 1 * CAL / (gram * K), 80 * K
    q_vaso, q_caneca = 250 * gram * c * dt, 50000 * gram * c * dt
    assert val(q_caneca, joule) > val(q_vaso, joule)


# ---------- Problemas ----------

for _n, _lit, _t, _es_f, _k in [(48, "a", "24", False, "297,15"), (49, "b", "210", False, "483,15"),
                                (50, "c", "72", True, "295,37"), (51, "d", "2460", True, "1622,04")]:
    @E(_n, f"{PROB} — 1{_lit}",
       enunciado=rf"Expresa en kelvin la temperatura ${_t}\,^\circ${'F' if _es_f else 'C'}.",
       respuesta=(rf"${_t}\,^\circ$F $= \dfrac{{5}}{{9}}({_t} - 32)\,^\circ$C, y "
                  rf"$T \approx \num{{{_k}}}$ K." if _es_f else
                  rf"$T = {_t} + \num{{273,15}} = \num{{{_k}}}$ K."))
    def _(t=_t, es_f=_es_f, k=_k):
        tk = c_a_k(f_a_c(t)) if es_f else c_a_k(t)
        assert abs(float(tk) - float(k.replace(",", "."))) < 0.005


@E(52, f"{PROB} — 2",
   enunciado=r"Un termómetro Fahrenheit mide la temperatura corporal en $98\,^\circ$F. ¿Cuál es "
             r"la lectura correspondiente en grados Celsius y en kelvin?",
   respuesta=r"$\dfrac{5}{9}(98 - 32) \approx \num{36,7}\,^\circ$C $\approx \num{309,8}$ K.")
def _():
    tc = f_a_c(98)
    assert abs(float(tc) - 36.67) < 0.005 and abs(float(c_a_k(tc)) - 309.82) < 0.005


@E(53, f"{PROB} — 3", tipo="contexto",
   enunciado=r"Una tina contiene 50 L de agua a $70\,^\circ$C. ¿Cuántos litros de agua a "
             r"$20\,^\circ$C hay que añadir para que la temperatura final sea de "
             r"$40\,^\circ$C?",
   respuesta=r"Calor cedido $=$ calor ganado: $50(70 - 40) = V(40 - 20)$, así que "
             r"$V = 75$ L.",
   notas="Sin pérdidas de calor; 1 L de agua ≈ 1 kg.")
def _():
    v = symbols("V", positive=True)
    c = 1 * CAL / (gram * K)
    dens = 1000 * gram / liter
    cedido = val(50 * liter * dens * c * 30 * K, joule)      # agua caliente: 70 → 40 °C
    por_litro = val(1 * liter * dens * c * 20 * K, joule)   # agua fría: 20 → 40 °C
    sol = solve(cedido - v * por_litro, v)
    assert len(sol) == 1 and abs(float(sol[0]) - 75) < 1e-9


@E(54, f"{PROB} — 4", tipo="contexto", dificultad=2,
   enunciado=r"Una tina contiene 50 L de agua a $25\,^\circ$C. Si del grifo sale agua caliente "
             r"a $80\,^\circ$C con un caudal de 5 L/min, ¿cuánto tiempo hay que abrirlo para "
             r"que la temperatura final del agua sea de $40\,^\circ$C?",
   respuesta=r"$V(80 - 40) = 50(40 - 25) \Rightarrow V = \num{18,75}$ L; "
             r"$t = \num{18,75}/5 = \num{3,75}$ min (3 min 45 s).",
   notas="Enunciado reordenado: en la guía dice «abrir el grifo para que salga agua caliente a "
         "80 °C y conseguir…».")
def _():
    v = symbols("V", positive=True)
    vol = solve(v * 40 - 50 * 15, v)[0]
    assert vol == Rational(75, 4)
    aprox(vol * liter / (5 * liter / minute), 3.75, minute, rel=1e-9)


@E(55, f"{PROB} — 5",
   enunciado=r"¿En qué temperatura coinciden las escalas Celsius y Fahrenheit?",
   respuesta=r"$T = \dfrac{9}{5}T + 32 \Rightarrow T = -40$: $-40\,^\circ$C $= -40\,^\circ$F.")
def _():
    t = symbols("T", real=True)
    assert solve(Rational(9, 5) * t + 32 - t, t) == [-40]


@E(56, f"{PROB} — 6",
   enunciado=r"Una varilla de hierro mide 5 m a $15\,^\circ$C. ¿Cuánto medirá a "
             r"$25\,^\circ$C? ($\alpha_{\text{hierro}} = 12 \times 10^{-6}\,^\circ$C$^{-1}$).",
   respuesta=r"$\Delta L = \alpha L_0 \Delta T = 12 \times 10^{-6}(5)(10) = \num{6e-4}$ m; "
             r"$L = \num{5,0006}$ m.")
def _():
    dl = Rational(12, 10**6) / K * 5 * m * 10 * K
    assert convert_to(5 * m + dl, m) == Rational("5.0006") * m


@E(57, f"{PROB} — 7", dificultad=3,
   enunciado=r"Una vasija de vidrio de exactamente $\num{1000}\ \mathrm{cm^3}$ a $0\,^\circ$C "
             r"se llena por completo de mercurio a esa temperatura. Al calentar la vasija y el "
             r"mercurio hasta $100\,^\circ$C se derraman $\num{15,8}\ \mathrm{cm^3}$ de "
             r"mercurio. Si el coeficiente de dilatación cúbica del mercurio es "
             r"$\num{0,000182}\,^\circ$C$^{-1}$, calcula el coeficiente de dilatación lineal "
             r"del vidrio.",
   respuesta=r"El mercurio se dilata $\num{0,000182}(1000)(100) = \num{18,2}\ \mathrm{cm^3}$ y "
             r"la vasija $\num{18,2} - \num{15,8} = \num{2,4}\ \mathrm{cm^3}$: "
             r"$\gamma_v = \dfrac{\num{2,4}}{1000(100)} = \num{2,4e-5}\,^\circ$C$^{-1}$ y "
             r"$\alpha = \gamma/3 = \num{8e-6}\,^\circ$C$^{-1}$.")
def _():
    v0, dt = 1000 * cm**3, 100 * K
    dv_hg = Rational("0.000182") / K * v0 * dt
    dv_vid = dv_hg - Rational("15.8") * cm**3
    alfa = dv_vid / (v0 * dt) / 3
    assert convert_to(alfa, 1 / K) == Rational(8, 10**6) / K


@E(58, f"{PROB} — 8",
   enunciado=r"Un cable de aluminio mide 30 m a $20\,^\circ$C y se calienta hasta "
             r"$60\,^\circ$C. Si el coeficiente de dilatación lineal del aluminio es "
             r"$24 \times 10^{-6}\,^\circ$C$^{-1}$, determina su dilatación y su longitud final.",
   respuesta=r"$\Delta L = 24 \times 10^{-6}(30)(40) = \num{0,0288}$ m ($\num{2,88}$ cm); "
             r"$L = \num{30,0288}$ m.",
   notas="La Tabla 6 de la guía da 25×10⁻⁶ °C⁻¹ para el aluminio; se usa el valor del "
         "enunciado.")
def _():
    dl = Rational(24, 10**6) / K * 30 * m * 40 * K
    assert convert_to(dl, cm) == Rational("2.88") * cm
    assert convert_to(30 * m + dl, m) == Rational("30.0288") * m


@E(59, f"{PROB} — 9",
   enunciado=r"Un cuerpo a $20\,^\circ$C se pone en contacto con otro a $\num{293,15}$ K. ¿Se "
             r"producirá un flujo de calor entre ellos?",
   respuesta=r"No: $\num{293,15}\ \text{K} = 20\,^\circ$C; están a la misma temperatura "
             r"(equilibrio térmico).")
def _():
    assert c_a_k(20) == Rational("293.15")


@E(60, f"{PROB} — 10",
   enunciado=r"En un recipiente hay 100 g de agua a $20\,^\circ$C. Se agregan 100 g de agua "
             r"caliente y la mezcla queda a $35\,^\circ$C. ¿A qué temperatura estaba el agua "
             r"que se agregó?",
   respuesta=r"$100(35 - 20) = 100(T - 35) \Rightarrow T = 50\,^\circ$C.")
def _():
    t = symbols("T", real=True)
    assert solve(100 * (35 - 20) - 100 * (t - 35), t) == [50]


@E(61, f"{PROB} — 11",
   enunciado=r"Una taza de café a $100\,^\circ$C se enfría hasta $20\,^\circ$C y libera "
             r"800 cal. ¿Qué cantidad de calor hay que darle para calentarla de nuevo de "
             r"$20\,^\circ$C a $50\,^\circ$C?",
   respuesta=r"$mc = \dfrac{800\ \text{cal}}{80\,^\circ\text{C}} = 10$ cal/°C; "
             r"$Q = 10(30) = 300$ cal ($\approx 1256$ J).")
def _():
    mc = 800 * CAL / (80 * K)
    aprox(mc * 30 * K, 300, CAL, rel=1e-9)
    aprox(mc * 30 * K, 1256, joule, rel=0.001)


@E(62, f"{PROB} — 12",
   enunciado=r"En un calorímetro de capacidad despreciable se mezclan 150 g de agua a "
             r"$12\,^\circ$C con 50 g de agua a $80\,^\circ$C. Calcula la temperatura de "
             r"equilibrio.",
   respuesta=r"$150(T - 12) = 50(80 - T) \Rightarrow 200T = 5800$, $T = 29\,^\circ$C.")
def _():
    t = symbols("T", real=True)
    assert solve(150 * (t - 12) - 50 * (80 - t), t) == [29]
