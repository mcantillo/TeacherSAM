"""Banco de ejercicios — Física 10° — Mediciones: cifras significativas, notación científica,
unidades, estimación y análisis dimensional.
Fuente: Guía de apoyo de Física 10° «Cinemática y dinámica», Capítulo 1 (mediciones y
estimaciones); se lee en
recursos/fisica/Guías pedagógicas Física/markdown/10 - Guia_de_apoyo_cinematica_y_dinamica_grado_10_fisica.md
Secciones: «Practiquemos» (dentro del texto), Preguntas, Problemas, Problemas generales.
DBA: ningún DBA de física de 10° trata la medición (es herramienta de todos los temas); se deja
dba vacío. Estándar 10°–11°, columna «…me aproximo al conocimiento como científico natural»
(medir, registrar datos, modelar con matemáticas): dba/naturales/estandares-fisica.md.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/fisica/mediciones-10.py
"""
from math import cos, log10, pi, radians, sin, tan

from sympy import Rational
from sympy.physics.units import (angstrom, convert_to, day, foot, gram, hour,
                                 inch, kilogram, kilometer, lightyear, meter, micrometer, mile,
                                 millimeter, minute, nanometer, picosecond, second, volt, yard,
                                 year)

from ejercicios import ejercicio, ejercicio_manual

PRE = "mediciones-10"
G1 = "Guía de apoyo Física 10° (cinemática y dinámica), Cap. 1 Mediciones y estimaciones"
PRAC = f"{G1}, Practiquemos"
PREG = f"{G1}, Preguntas"
PROB = f"{G1}, Problemas"
GEN = f"{G1}, Problemas generales"
COMUN = dict(tema="mediciones y unidades", grados=[10], dba=[])


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
        return float(convert_to(q, [meter, kilogram, second, volt]))
    return float(convert_to(q, unidad) / unidad)


def aprox(q, esperado, unidad, rel=0.01):
    v = val(q, unidad)
    assert abs(v - esperado) <= rel * abs(esperado), f"{v} ≠ {esperado}"


def cifras(s):
    """Cifras significativas de un número escrito como en la guía («0,0086», «8.700»):
    punto = separador de miles; en un entero, los ceros finales no cuentan."""
    s = s.replace(".", "")
    if "," in s:
        return len(s.replace(",", "").lstrip("0"))
    return len(s.strip("0"))


def decimales(s):
    return len(s.split(",")[1]) if "," in s else 0


def redondea(x, n):
    return float(f"{float(x):.{n}g}")


def num(s):
    return Rational(s.replace(".", "").replace(",", "."))


# ---------- Practiquemos (dentro del texto) ----------

@E(1, f"{PRAC} (cifras significativas) — 1", tipo="seleccion",
   enunciado=r"El área de un rectángulo de $\num{4,5}$ cm por $\num{3,25}$ cm se da "
             r"correctamente con:" + op(r"$\num{14,625}\ \mathrm{cm^2}$",
                                        r"$\num{14,63}\ \mathrm{cm^2}$",
                                        r"$\num{14,6}\ \mathrm{cm^2}$", r"$15\ \mathrm{cm^2}$"),
   respuesta=r"d) $15\ \mathrm{cm^2}$: $\num{4,5} \times \num{3,25} = \num{14,625}$ y el "
             r"resultado lleva dos cifras significativas, las del dato menos preciso "
             r"($\num{4,5}$).")
def _():
    area = num("4,5") * num("3,25")
    n = min(cifras("4,5"), cifras("3,25"))
    assert area == num("14,625") and n == 2 and redondea(area, n) == 15
    opciones = ["14,625", "14,63", "14,6", "15"]
    assert [cifras(o) for o in opciones] == [5, 4, 3, 2]   # solo d) tiene 2 cifras


@E(2, f"{PRAC} (cifras significativas) — 2", tipo="conceptual",
   enunciado=r"¿$\num{0,00324}$ y $\num{0,00056}$ tienen el mismo número de cifras "
             r"significativas?",
   respuesta=r"No: $\num{0,00324}$ tiene tres cifras significativas y $\num{0,00056}$ tiene "
             r"dos (los ceros de la izquierda no cuentan), aunque los dos tienen cinco lugares "
             r"decimales.")
def _():
    assert (cifras("0,00324"), cifras("0,00056")) == (3, 2)
    assert decimales("0,00324") == decimales("0,00056") == 5


for _n, _lit, _s, _c, _d in [(3, "a", "1,23", 3, 2), (4, "b", "0,123", 3, 3),
                             (5, "c", "0,0123", 3, 4)]:
    @E(_n, f"{PRAC} (cifras significativas) — 3{_lit}",
       enunciado=rf"Especifica el número de cifras significativas y el número de lugares "
                 rf"decimales de $\num{{{_s}}}$.",
       respuesta=rf"{_c} cifras significativas y {_d} lugares decimales.")
    def _(s=_s, c=_c, d=_d):
        assert cifras(s) == c and decimales(s) == d

for _n, _lit, _s, _m, _e, _c in [(6, "a", "0,0258", "2,58", -2, 3),
                                 (7, "b", "42.300", "4,23", 4, 3),
                                 (8, "c", "344,50", "3,4450", 2, 5)]:
    @E(_n, f"{PRAC} (notación científica) — {_lit}",
       enunciado=rf"Escribe $\num{{{_s.replace('.', '')}}}$ en notación científica y "
                 rf"especifica su número de cifras significativas.",
       respuesta=rf"$\num{{{_m}e{_e}}}$; {_c} cifras significativas.")
    def _(s=_s, m=_m, e=_e, c=_c):
        assert num(m) * Rational(10) ** e == num(s)
        assert 1 <= num(m) < 10 and cifras(m) == cifras(s) == c


@E(9, f"{PRAC} (conversión de unidades) — 1", tipo="contexto",
   enunciado=r"Las tres cumbres más altas del mundo son el Everest ($8850$ m), el K2 "
             r"($8611$ m) y el Kangchenjunga ($8586$ m) (tabla de las cumbres de 8000 m). "
             r"Determina su elevación en pies (ft), con $1\ \mathrm{ft} = \num{0,3048}$ m.",
   respuesta=r"Everest $\approx \num{29035}$ ft; K2 $\approx \num{28251}$ ft; "
             r"Kangchenjunga $\approx \num{28169}$ ft (con cuatro cifras significativas: "
             r"$\num{2,904e4}$, $\num{2,825e4}$ y $\num{2,817e4}$ ft).")
def _():
    for h, ft in [(8850, 29035), (8611, 28251), (8586, 28169)]:
        aprox(h * meter, ft, foot, rel=1e-4)


# ---------- Preguntas ----------

M(10, f"{PREG} — 1a",
  r"¿Cuáles son las ventajas y desventajas de usar como estándar de longitud el pie de una "
  r"persona en particular? (Un buen estándar debe ser accesible, invariable, reproducible e "
  r"indestructible).",
  r"Ventaja: es invariable y fácil de definir mientras la persona viva. Desventajas: no es "
  r"accesible para todos (la persona no puede estar en todas partes), no es reproducible y "
  r"no es indestructible: la persona envejece, su pie cambia un poco y un día muere.")
M(11, f"{PREG} — 1b",
  r"¿Cuáles son las ventajas y desventajas de usar como estándar de longitud el pie de "
  r"cualquier persona?",
  r"Ventaja: es muy accesible, todos lo llevamos encima. Desventaja: no es invariable ni "
  r"reproducible, porque los pies de distintas personas miden distinto; dos medidas de la "
  r"misma cosa darían resultados diferentes.")
M(12, f"{PREG} — 2",
  r"¿Por qué es incorrecto pensar que cuantos más dígitos se utilicen en una respuesta, más "
  r"exacta será?",
  r"Porque la exactitud de un resultado la limitan los datos medidos: los dígitos de más que "
  r"da la calculadora no son confiables. El resultado no puede tener más cifras "
  r"significativas que el dato menos preciso.")
M(13, f"{PREG} — 3",
  r"¿Qué está equivocado en esta señal de carretera? «Memphis 7 mi ($\num{11,263}$ km)».",
  r"La conversión tiene demasiadas cifras significativas: «7 mi» tiene una sola cifra "
  r"significativa, así que la distancia en kilómetros debe escribirse como unos 11 km "
  r"($7 \times \num{1,609} \approx 11$), no con la precisión de metros.")
M(14, f"{PREG} — 4",
  r"Para que una respuesta esté completa es necesario especificar las unidades. ¿Por qué?",
  r"Porque un número sin unidad no dice cuánto mide la cantidad: «5» puede ser 5 m, 5 km o "
  r"5 s. La unidad indica con qué patrón se comparó la medida y qué tipo de magnitud es.")
M(15, f"{PREG} — 5",
  r"Explica cómo podrías usar la noción de simetría para estimar el número de canicas en un "
  r"recipiente de un litro.",
  r"Si las canicas están acomodadas de manera regular, se cuentan las que caben a lo largo "
  r"de una arista (o de una capa) del recipiente y, por simetría, se supone que el número se "
  r"repite en las otras dos direcciones: $N \approx n^3$ (o número por capa $\times$ número "
  r"de capas).")
M(16, f"{PREG} — 6",
  r"Mides el radio de una rueda y obtienes $\num{4,16}$ cm. Si multiplicas por 2 para obtener "
  r"el diámetro, ¿debes escribir el resultado como 8 cm o como $\num{8,32}$ cm? Explica.",
  r"$\num{8,32}$ cm: el 2 es un número exacto (no una medida), así que el resultado conserva "
  r"las tres cifras significativas del radio.")


@E(17, f"{PREG} — 7",
   enunciado=r"Expresa el seno de $\num{30,0}^\circ$ con el número correcto de cifras "
             r"significativas.",
   respuesta=r"$\operatorname{sen} \num{30,0}^\circ = \num{0,500}$ (tres cifras "
             r"significativas, como el ángulo).")
def _():
    assert abs(sin(radians(30.0)) - 0.5) < 1e-12 and cifras("30,0") == cifras("0,500") == 3


M(18, f"{PREG} — 8",
  r"Una receta de suflé pide medir los ingredientes con exactitud y pide seis huevos "
  r"grandes. El tamaño de los «huevos grandes» varía en un 10\,\%. ¿Qué indica esto sobre "
  r"cuán exactas deben ser las mediciones de los otros ingredientes?",
  r"Que no tiene sentido medir los demás ingredientes con mucha más precisión que un 10\,\%: "
  r"la incertidumbre de los huevos ya es de ese orden y domina la del resultado.")
M(19, f"{PREG} — 9",
  r"Elabora una lista de suposiciones útiles para estimar el número de mecánicos automotrices "
  r"en tu ciudad y haz luego la estimación.",
  r"Ejemplo para Cali (unos $2{,}2$ millones de habitantes): una familia de 4 personas tiene "
  r"en promedio 1 carro $\Rightarrow$ unos $5{,}5\times10^5$ carros; cada carro va al taller "
  r"unas 2 veces al año y cada visita ocupa unas 4 h de mecánico $\Rightarrow$ "
  r"$\approx 4{,}4\times10^6$ h/año; un mecánico trabaja unas $2000$ h/año. Resultado: del "
  r"orden de $2\times10^3$ mecánicos. Se acepta cualquier estimación coherente con las "
  r"suposiciones escritas.", tipo="contexto")
M(20, f"{PREG} — 10",
  r"Sugiere una forma de medir la distancia de la Tierra al Sol.",
  r"Por ejemplo, con trigonometría: se mide la distancia Tierra–Luna (con radar o láser, o "
  r"por paralaje) y, cuando la Luna está en cuarto (ángulo Tierra–Luna–Sol de $90^\circ$), "
  r"se mide el ángulo $\theta$ entre la Luna y el Sol vistos desde la Tierra: "
  r"$d_{TS} = d_{TL}/\cos\theta$ (método de Aristarco). Hoy se usa el radar a Venus y las "
  r"leyes de Kepler.")


# ---------- Problemas: medición e incertidumbre; cifras significativas ----------

@E(21, f"{PROB} — 1",
   enunciado=r"Se cree que la edad del Universo es de aproximadamente 14 mil millones de años. "
             r"Con dos cifras significativas, escribe esa edad en potencias de diez, en años y "
             r"en segundos.",
   respuesta=r"$\num{1,4e10}$ años $\approx \num{4,4e17}$ s (con $1\ \text{año} \approx "
             r"\num{3,16e7}$ s).")
def _():
    assert 14 * 10**9 == num("1,4") * 10**10
    aprox(14e9 * year, 4.4e17, second, rel=0.01)


for _n, _lit, _s, _c in [(22, "a", "214", 3), (23, "b", "81,60", 4), (24, "c", "7,03", 3),
                         (25, "d", "0,03", 1), (26, "e", "0,0086", 2), (27, "f", "3.236", 4),
                         (28, "g", "8.700", 2)]:
    @E(_n, f"{PROB} — 2{_lit}",
       enunciado=rf"¿Cuántas cifras significativas tiene el número "
                 rf"$\num{{{_s.replace('.', '')}}}$?",
       respuesta=rf"{_c}." + (r" (Según la nota de la guía, los ceros finales de un entero "
                              r"sin coma no se cuentan).") * (_s == "8.700"))
    def _(s=_s, c=_c):
        assert cifras(s) == c

for _n, _lit, _s, _m, _e in [(29, "a", "1,156", "1,156", 0), (30, "b", "21,8", "2,18", 1),
                             (31, "c", "0,0068", "6,8", -3), (32, "d", "328,65", "3,2865", 2),
                             (33, "e", "0,219", "2,19", -1), (34, "f", "444", "4,44", 2)]:
    @E(_n, f"{PROB} — 3{_lit}",
       enunciado=rf"Escribe $\num{{{_s}}}$ en potencias de diez.",
       respuesta=rf"$\num{{{_m}}} \times 10^{{{_e}}}$.")
    def _(s=_s, m=_m, e=_e):
        assert num(m) * Rational(10) ** e == num(s) and 1 <= num(m) < 10

for _n, _lit, _m, _e, _r in [(35, "a", "8,69", 4, "86900"), (36, "b", "9,1", 3, "9100"),
                             (37, "c", "8,8", -1, "0,88"), (38, "d", "4,76", 2, "476"),
                             (39, "e", "3,62", -5, "0,0000362")]:
    @E(_n, f"{PROB} — 4{_lit}",
       enunciado=rf"Escribe completo, con el número correcto de ceros: "
                 rf"$\num{{{_m}}} \times 10^{{{_e}}}$.",
       respuesta=rf"$\num{{{_r}}}$.")
    def _(m=_m, e=_e, r=_r):
        assert num(m) * Rational(10) ** e == num(r)


@E(40, f"{PROB} — 5",
   enunciado=r"¿Cuál es la incertidumbre porcentual en la medición $\num{5,48} \pm \num{0,25}$ m?",
   respuesta=r"$\dfrac{\num{0,25}}{\num{5,48}} \times 100\,\% \approx \num{4,6}\,\%$ "
             r"(unos 5\,\%).",
   notas="En la guía la incertidumbre aparece con punto decimal («0.25»); se escribe con coma.")
def _():
    assert abs(float(num("0,25") / num("5,48") * 100) - 4.56) < 0.01


# ---------- Problemas: unidades, estándares y sistema SI ----------

_MICROV, _GIGAV, _FM = volt / 10**6, 10**9 * volt, meter / 10**15
for _n, _lit, _dato, _q, _u, _r, _txt in [
        (41, "a", r"$\num{286,6}$ mm", num("286,6") * millimeter, meter, "0,2866", "m"),
        (42, "b", r"$85\ \mu$V", 85 * _MICROV, volt, "0,000085", "V"),
        (43, "c", r"$760$ mg", 760 * gram / 1000, kilogram, "0,000760", "kg"),
        (44, "d", r"$\num{60,0}$ ps", num("60,0") * picosecond, second, "0,0000000000600", "s"),
        (45, "e", r"$\num{22,5}$ fm", num("22,5") * _FM, meter, "0,0000000000000225", "m"),
        (46, "f", r"$\num{2,50}$ gigavoltios", num("2,50") * _GIGAV, volt, "2500000000", "V")]:
    @E(_n, f"{PROB} — 6{_lit}",
       enunciado=rf"Escribe completo (como número decimal) y en la unidad estándar del SI: "
                 rf"{_dato}.",
       respuesta=rf"$\num{{{_r}}}$ {_txt}.")
    def _(q=_q, u=_u, r=_r):
        assert convert_to(q, u) == num(r) * u

for _n, _lit, _dato, _r, _ok in [
        (47, "a", r"$1 \times 10^{6}$ voltios", r"1 MV (megavoltio)", 10**6 * volt == 1 * volt * 10**6),
        (48, "b", r"$2 \times 10^{-6}$ metros", r"$2\ \mu$m (micrómetros)",
         convert_to(2 * micrometer, meter) == Rational(2, 10**6) * meter),
        (49, "c", r"$6 \times 10^{3}$ días", r"6 kilodías (kd)",
         convert_to(6000 * day, second) == 6 * 10**3 * convert_to(day, second)),
        (50, "d", r"$18 \times 10^{2}$ dólares",
         r"18 hectodólares, o mejor $\num{1,8}$ kilodólares", 18 * 10**2 == num("1,8") * 10**3),
        (51, "e", r"$8 \times 10^{-8}$ segundos", r"80 ns (nanosegundos)",
         Rational(8, 10**8) == Rational(80, 10**9))]:
    @E(_n, f"{PROB} — 7{_lit}",
       enunciado=rf"Expresa usando los prefijos del SI: {_dato}.",
       respuesta=rf"{_r}.")
    def _(ok=_ok):
        assert ok

M(52, f"{PROB} — 8", r"Determina tu propia altura en metros y tu masa en kilogramos.",
  r"Respuesta personal; por ejemplo, $\num{1,65}$ m y $58$ kg. Deben usarse el metro y el "
  r"kilogramo, con cifras significativas acordes al instrumento (cinta métrica al "
  r"centímetro, báscula al kilogramo o a la décima).", tipo="contexto")


@E(53, f"{PROB} — 9a",
   enunciado=r"El Sol está en promedio a 93 millones de millas de la Tierra "
             r"($1\ \text{mi} = \num{1609}$ m). ¿A cuántos metros equivale esto? Exprésalo "
             r"usando potencias de diez.",
   respuesta=r"$\num{9,3e7}\ \text{mi} \times \num{1609}\ \text{m/mi} \approx \num{1,5e11}$ m.")
def _():
    aprox(93e6 * mile, 1.5e11, meter, rel=0.01)


@E(54, f"{PROB} — 9b",
   enunciado=r"El Sol está en promedio a 93 millones de millas de la Tierra. Expresa esa "
             r"distancia en metros usando un prefijo métrico.",
   respuesta=r"$\approx 150$ Gm (gigámetros), pues $\num{1,5e11}\ \text{m} = "
             r"150 \times 10^{9}$ m.")
def _():
    aprox(93e6 * mile, 150, 10**9 * meter, rel=0.01)


@E(55, f"{PROB} — 10",
   enunciado=r"Si un avión viaja a $950$ km/h, ¿cuánto tiempo le tomará recorrer "
             r"$\num{1,00}$ km?",
   respuesta=r"$t = \dfrac{\num{1,00}\ \text{km}}{950\ \text{km/h}} \approx "
             r"\num{1,05e-3}$ h $\approx \num{3,8}$ s.")
def _():
    aprox((1 * kilometer) / (950 * kilometer / hour), 3.79, second, rel=0.01)


@E(56, f"{PROB} — 11a",
   enunciado=r"Un átomo típico tiene un diámetro de aproximadamente $\num{1,0e-10}$ m. "
             r"¿Cuánto es esto en pulgadas ($1\ \text{in} = \num{2,54}$ cm)?",
   respuesta=r"$\approx \num{3,9e-9}$ in.")
def _():
    aprox(1.0e-10 * meter, 3.9e-9, inch, rel=0.02)


@E(57, f"{PROB} — 11b",
   enunciado=r"Un átomo típico tiene un diámetro de aproximadamente $\num{1,0e-10}$ m. "
             r"¿Cuántos átomos hay aproximadamente en una línea de $\num{1,0}$ cm?",
   respuesta=r"$\dfrac{\num{1,0e-2}\ \text{m}}{\num{1,0e-10}\ \text{m}} = \num{1,0e8}$ átomos.")
def _():
    assert abs(val(Rational(1, 100) * meter / (Rational(1, 10**10) * meter), 1) - 1e8) < 1


@E(58, f"{PROB} — 12",
   enunciado=r"Expresa la siguiente suma con el número correcto de cifras significativas: "
             r"$\num{1,80}\ \text{m} + \num{142,5}\ \text{cm} + \num{5,34e5}\ \mu\text{m}$.",
   respuesta=r"$\num{1,80} + \num{1,425} + \num{0,534} = \num{3,759}$ m $\approx "
             r"\num{3,76}$ m (en una suma manda el dato con menos decimales: $\num{1,80}$ m, "
             r"centésimas de metro).")
def _():
    total = num("1,80") * meter + num("142,5") * meter / 100 + num("5,34") * 10**5 * micrometer
    assert convert_to(total, meter) == num("3,759") * meter
    assert round(float(num("3,759")), 2) == 3.76


@E(59, f"{PROB} — 13a",
   enunciado=r"Un año luz es la distancia que recorre la luz en un año, a una rapidez de "
             r"$\num{2,998e8}$ m/s. ¿Cuántos metros hay en $\num{1,00}$ año luz?",
   respuesta=r"$\num{2,998e8}\ \text{m/s} \times \num{3,156e7}\ \text{s} \approx "
             r"\num{9,46e15}$ m.")
def _():
    aprox(2.998e8 * meter / second * year, 9.46e15, meter, rel=0.002)
    aprox(lightyear, 9.46e15, meter, rel=0.002)


@E(60, f"{PROB} — 13b",
   enunciado=r"Una unidad astronómica (UA) es la distancia promedio entre el Sol y la Tierra, "
             r"$\num{1,50e8}$ km. ¿Cuántas UA hay en $\num{1,00}$ año luz "
             r"($\num{9,46e15}$ m)?",
   respuesta=r"$\dfrac{\num{9,46e15}\ \text{m}}{\num{1,50e11}\ \text{m}} \approx "
             r"\num{6,31e4}$ UA.")
def _():
    ua = 1.50e8 * kilometer
    aprox(2.998e8 * meter / second * year, 6.31e4, ua, rel=0.003)


@E(61, f"{PROB} — 13c",
   enunciado=r"¿Cuál es la rapidez de la luz ($\num{2,998e8}$ m/s) en UA/h, si "
             r"$1\ \text{UA} = \num{1,50e8}$ km?",
   respuesta=r"$\dfrac{\num{2,998e8}\ \text{m/s} \times 3600\ \text{s/h}}{\num{1,50e11}\ "
             r"\text{m/UA}} \approx \num{7,20}$ UA/h.")
def _():
    aprox(2.998e8 * meter / second, 7.20, 1.50e8 * kilometer / hour, rel=0.002)


for _n, _lit, _s, _x, _e in [(62, "a", r"$2800$", 2800, 3),
                             (63, "b", r"$\num{86,30} \times 10^{2}$", 8630, 4),
                             (64, "c", r"$\num{0,0076}$", 0.0076, -2),
                             (65, "d", r"$\num{15,0} \times 10^{8}$", 1.5e9, 9)]:
    @E(_n, f"{PROB} — 14{_lit}",
       enunciado=rf"Estima el orden de magnitud (potencia de diez) de {_s}.",
       respuesta=rf"$10^{{{_e}}}$.")
    def _(x=_x, e=_e):
        assert round(log10(x)) == e

M(66, f"{PROB} — 15", tipo="contexto", dificultad=2,
  enunciado=r"Estima cuántos libros se pueden almacenar en una biblioteca universitaria con "
            r"$3500\ \mathrm{m^2}$ de espacio en la planta. Supón que hay ocho anaqueles de "
            r"alto, con libros en ambos lados y corredores de $\num{1,5}$ m de ancho, y que "
            r"los libros miden en promedio unos 5 cm de grueso y 25 cm de fondo.",
  respuesta=r"Cada estante doble ($\num{0,5}$ m de fondo) más su corredor ocupa una franja de "
            r"unos 2 m de ancho: hay $3500/2 \approx 1750$ m de estantería doble. Longitud "
            r"total de repisa: $1750 \times 2\ \text{lados} \times 8 \approx \num{2,8e4}$ m; a "
            r"20 libros por metro, $\approx \num{5,6e5}$ libros: del orden de $10^{6}$.",
  notas="En la guía falta la unidad del ancho de los corredores («1,5 de ancho»): se escribe "
        "1,5 m. «Los libros tienen el tamaño de éste» se cambia por dimensiones explícitas.")
M(67, f"{PROB} — 16",
  r"Estima el número de litros de agua que un ser humano bebe durante su vida.",
  r"Unos 2 L por día durante unos 70 años: $2 \times 365 \times 70 \approx \num{5e4}$ L "
  r"(del orden de $10^{4}$ a $10^{5}$ L).", tipo="contexto")
M(68, f"{PROB} — 17",
  r"¿Cuáles son las dimensiones de la densidad, definida como masa entre volumen?",
  r"$[M/L^{3}]$ (masa sobre longitud al cubo); en el SI, $\mathrm{kg/m^3}$.")


@E(69, f"{PROB} — 18a",
   enunciado=r"La rapidez $v$ de un cuerpo está dada por $v = At^{3} - Bt$, donde $t$ es el "
             r"tiempo. ¿Cuáles son las dimensiones de $A$ y $B$?",
   respuesta=r"$[A] = [L/T^{4}]$ y $[B] = [L/T^{2}]$, para que $At^{3}$ y $Bt$ tengan "
             r"dimensiones de rapidez $[L/T]$.")
def _():
    v = meter / second
    assert (v / second**3) == meter / second**4 and (v / second) == meter / second**2


@E(70, f"{PROB} — 18b",
   enunciado=r"La rapidez $v$ de un cuerpo está dada por $v = At^{3} - Bt$. ¿Cuáles son las "
             r"unidades SI de las constantes $A$ y $B$?",
   respuesta=r"$A$ en $\mathrm{m/s^4}$ y $B$ en $\mathrm{m/s^2}$.")
def _():
    t = 2 * second
    assert convert_to((1 * meter / second**4) * t**3 - (1 * meter / second**2) * t,
                      meter / second) == 6 * meter / second


@E(71, f"{PROB} — 19", tipo="seleccion", dificultad=2,
   enunciado=r"Tres estudiantes obtienen las siguientes ecuaciones, donde $x$ es la distancia "
             r"recorrida, $v$ la rapidez, $a$ la aceleración, $t$ el tiempo y el subíndice 0 "
             r"indica el valor en $t = 0$. ¿Cuál es correcta según una comprobación "
             r"dimensional?" + op(r"$x = vt^{2} + 2at$", r"$x = v_{0}t + \frac{1}{2}at^{2}$",
                                   r"$x = v_{0}t + 2at^{2}$"),
   respuesta=r"b) y c) son dimensionalmente correctas (cada término tiene dimensión $[L]$); "
             r"a) no, porque $vt^{2}$ tiene dimensiones $[L\,T]$ y $2at$ de $[L/T]$. La "
             r"comprobación dimensional no detecta factores numéricos: la ecuación "
             r"físicamente correcta es b), con el factor $\frac{1}{2}$.",
   notas="La guía pregunta por «la» ecuación correcta, pero b y c pasan la prueba dimensional.")
def _():
    v, a, t = meter / second, meter / second**2, second

    def es_longitud(q):
        return (convert_to(q, meter) / meter).is_number
    assert not es_longitud(v * t**2) and not es_longitud(2 * a * t)
    assert es_longitud(v * t) and es_longitud(a * t**2 / 2) and es_longitud(2 * a * t**2)


# ---------- Problemas generales ----------

@E(72, f"{GEN} — 1", tipo="contexto",
   enunciado=r"Un satélite GPS está a $\num{20000}$ km de ti. ¿Qué incertidumbre porcentual "
             r"en la distancia representa una incertidumbre de 2 m? ¿Cuántas cifras "
             r"significativas implica eso en la distancia?",
   respuesta=r"$\dfrac{2\ \text{m}}{\num{2,0e7}\ \text{m}} = \num{1e-7} = \num{1e-5}\,\%$. La "
             r"distancia se conoce hasta el metro: $\num{20000000} \pm 2$ m, es decir, 8 "
             r"cifras significativas.")
def _():
    frac = val(2 * meter / (20000 * kilometer), 1)
    assert abs(frac * 100 - 1e-5) < 1e-12
    assert len(str(20000 * 1000)) == 8     # hasta las unidades de metro


@E(73, f"{GEN} — 2", tipo="contexto",
   enunciado=r"Los chips de computadora se graban en obleas de silicio de $\num{0,300}$ mm de "
             r"grosor, que se rebanan de un cilindro de silicio de 25 cm de longitud. Si cada "
             r"oblea puede contener 100 chips, ¿cuál es el número máximo de chips que se pueden "
             r"producir con un cilindro completo?",
   respuesta=r"$\dfrac{250\ \text{mm}}{\num{0,300}\ \text{mm}} \approx 833$ obleas "
             r"$\Rightarrow$ unos $\num{8,3e4}$ chips ($\num{83300}$).",
   notas="Se desprecia el material que se pierde al cortar.")
def _():
    obleas = val(25 * meter / 100 / (num("0,300") * millimeter), 1)
    assert int(obleas) == 833 and int(obleas) * 100 == 83300


for _n, _lit, _preg, _resp, _q, _u, _x in [
        (74, "a", "¿Cuántos segundos hay en 1 año?", r"$\approx \num{3,16e7}$ s.",
         1 * year, second, 3.16e7),
        (75, "b", "¿Cuántos nanosegundos hay en 1 año?", r"$\approx \num{3,16e16}$ ns.",
         1 * year, second / 10**9, 3.16e16),
        (76, "c", "¿Cuántos años hay en 1 segundo?", r"$\approx \num{3,17e-8}$ años.",
         1 * second, year, 3.17e-8)]:
    @E(_n, f"{GEN} — 3{_lit}", enunciado=_preg + " Exprésalo en notación científica.",
       respuesta=_resp)
    def _(q=_q, u=_u, x=_x):
        aprox(q, x, u, rel=0.003)


@E(77, f"{GEN} — 4", tipo="contexto",
   enunciado=r"El fútbol americano se juega en un campo de 100 yardas de longitud y el campo "
             r"de fútbol mide 100 m de largo. ¿Qué campo es más largo y por cuánto (en yardas, "
             r"metros y porcentaje)? ($1\ \text{yd} = \num{0,9144}$ m).",
   respuesta=r"El de fútbol: 100 yd $= \num{91,44}$ m, así que es más largo por "
             r"$\num{8,56}$ m $= \num{9,36}$ yd, un $\num{9,4}\,\%$ más largo.")
def _():
    dif = 100 * meter - 100 * yard
    aprox(dif, 8.56, meter, rel=0.001)
    aprox(dif, 9.36, yard, rel=0.001)
    assert abs(val(dif / (100 * yard), 1) * 100 - 9.4) < 0.05


M(78, f"{GEN} — 5", tipo="contexto", dificultad=2,
  enunciado=r"El pulmón de un adulto contiene cerca de 300 millones de cavidades diminutas "
            r"llamadas alvéolos. Estima el diámetro promedio de un alvéolo.",
  respuesta=r"Si los pulmones tienen unos 4 L $= \num{4e-3}\ \mathrm{m^3}$, cada alvéolo ocupa "
            r"$\num{4e-3}/\num{3e8} \approx \num{1,3e-11}\ \mathrm{m^3}$; tomando cada uno "
            r"como un cubo, $d \approx \sqrt[3]{\num{1,3e-11}} \approx \num{2e-4}$ m, unas "
            r"$\num{0,2}$ mm (del orden de $10^{-4}$ m).")


@E(79, f"{GEN} — 6",
   enunciado=r"Una hectárea se define como $1 \times 10^{4}\ \mathrm{m^2}$. Un acre tiene "
             r"$\num{4,356e4}\ \mathrm{ft^2}$. ¿Cuántos acres hay en una hectárea?",
   respuesta=r"$1\ \text{acre} = \num{4,356e4} \times (\num{0,3048})^2 \approx \num{4047}\ "
             r"\mathrm{m^2}$, así que 1 ha $\approx \num{2,47}$ acres.")
def _():
    acre = num("4,356") * 10**4 * foot**2
    aprox(10**4 * meter**2, 2.47, acre, rel=0.002)


@E(80, f"{GEN} — 7", tipo="contexto", dificultad=2,
   enunciado=r"Una familia de cuatro personas usa unos $1200$ L de agua por día "
             r"($1\ \text{L} = 1000\ \mathrm{cm^3}$). ¿Qué profundidad perdería cada año un "
             r"lago que cubre uniformemente $50\ \mathrm{km^2}$ si abastece a una población "
             r"de $\num{40000}$ personas? Considera solo el uso de la población.",
   respuesta=r"$\num{10000}$ familias $\times 1200$ L/día $\times 365$ días "
             r"$\approx \num{4,4e6}\ \mathrm{m^3}$ al año; profundidad "
             r"$= \dfrac{\num{4,38e6}\ \mathrm{m^3}}{\num{5,0e7}\ \mathrm{m^2}} \approx "
             r"\num{0,088}$ m $\approx 9$ cm.")
def _():
    from sympy.physics.units import liter
    vol = (40000 / 4) * 1200 * liter * 365
    aprox(vol / (50 * kilometer**2), 0.0876, meter, rel=0.002)


@E(81, f"{GEN} — 8", tipo="contexto",
   enunciado=r"Un CD de audio contiene $\num{783,216}$ megabytes de información. El "
             r"reproductor lee la información a una tasa constante de $\num{1,4}$ megabytes "
             r"por segundo. ¿Cuántos minutos le toma leer el CD completo?",
   respuesta=r"$\dfrac{\num{783,216}}{\num{1,4}} \approx 559$ s $\approx \num{9,3}$ min.",
   notas="En la guía: «taza constante»; es «tasa». El dato de 8 bits por byte no se necesita.")
def _():
    aprox(num("783,216") / num("1,4") * second, 9.3, minute, rel=0.005)


@E(82, f"{GEN} — 9", tipo="contexto", dificultad=2,
   enunciado=r"El arca de Noé debía medir 300 codos de largo, 50 de ancho y 30 de alto. El "
             r"codo era la longitud del antebrazo, del codo a la punta del dedo más largo. "
             r"Expresa las dimensiones del arca en metros y estima su volumen.",
   respuesta=r"Con 1 codo $\approx \num{0,5}$ m: $150\ \text{m} \times 25\ \text{m} \times "
             r"15\ \text{m}$, y $V \approx \num{5,6e4}\ \mathrm{m^3}$ (del orden de "
             r"$10^{5}\ \mathrm{m^3}$; con 1 codo $\approx \num{0,45}$ m, "
             r"$\approx \num{4e4}\ \mathrm{m^3}$).")
def _():
    codo = meter / 2
    aprox((300 * codo) * (50 * codo) * (30 * codo), 5.6e4, meter**3, rel=0.01)
    aprox((300 * 50 * 30) * (Rational(45, 100) * meter)**3, 4.1e4, meter**3, rel=0.02)


@E(83, f"{GEN} — 10", tipo="contexto",
   enunciado=r"Estima cuánto tiempo tomaría caminar alrededor del mundo, suponiendo que se "
             r"camina 10 h por día a 4 km/h.",
   respuesta=r"La circunferencia de la Tierra es de unos $\num{40000}$ km; a 40 km por día, "
             r"$\num{1000}$ días, unos $\num{2,7}$ años (sin contar los océanos).")
def _():
    por_dia = 4 * kilometer / hour * 10 * hour
    dias = val(40000 * kilometer / por_dia, 1)
    assert dias == 1000
    aprox(dias * day, 2.7, year, rel=0.02)


@E(84, f"{GEN} — 11",
   enunciado=r"Un fabricante de relojes afirma que sus relojes ganan o pierden no más de "
             r"8 segundos al año. ¿Qué tan exactos son? Expresa el resultado como porcentaje.",
   respuesta=r"$\dfrac{8\ \text{s}}{\num{3,16e7}\ \text{s}} \approx \num{2,5e-7}$, es decir, "
             r"$\num{2,5e-5}\,\%$.")
def _():
    assert abs(val(8 * second / year, 1) * 100 - 2.5e-5) < 0.05e-5


for _n, _lit, _preg, _resp, _q, _u, _x in [
        (85, "a", r"¿Cuántos nanómetros hay en $\num{1,0}$ Å?", r"$\num{0,10}$ nm.",
         1 * angstrom, nanometer, 0.1),
        (86, "b", r"¿Cuántos femtómetros (fermis) hay en $\num{1,0}$ Å?", r"$\num{1,0e5}$ fm.",
         1 * angstrom, _FM, 1e5),
        (87, "c", r"¿Cuántos ángstroms hay en $\num{1,0}$ m?", r"$\num{1,0e10}$ Å.",
         1 * meter, angstrom, 1e10),
        (88, "d", r"¿Cuántos ángstroms hay en $\num{1,0}$ año luz ($\num{9,46e15}$ m)?",
         r"$\approx \num{9,5e25}$ Å.", 1 * lightyear, angstrom, 9.46e25)]:
    @E(_n, f"{GEN} — 12{_lit}",
       enunciado=r"Un ángstrom (Å) es una unidad de longitud igual a $10^{-10}$ m. " + _preg,
       respuesta=_resp, notas="En la guía: «es una de longitud»; falta «unidad».")
    def _(q=_q, u=_u, x=_x):
        aprox(q, x, u, rel=0.003)


@E(89, f"{GEN} — 13", tipo="contexto", dificultad=2,
   enunciado=r"El diámetro de la Luna es de $\num{3480}$ km. ¿Cuál es su volumen? ¿Cuántas "
             r"Lunas se necesitarían para igualar el volumen de la Tierra "
             r"(radio $\num{6380}$ km)?",
   respuesta=r"$V_L = \frac{4}{3}\pi(\num{1,74e6}\ \text{m})^3 \approx \num{2,2e19}\ "
             r"\mathrm{m^3}$; $V_T/V_L = (\num{6380}/\num{1740})^3 \approx 49$ Lunas.",
   notas="La guía no da el radio de la Tierra; se usa 6380 km.")
def _():
    vl = 4 * pi / 3 * (1.74e6 * meter)**3
    vt = 4 * pi / 3 * (6.38e6 * meter)**3
    aprox(vl, 2.2e19, meter**3, rel=0.01)
    assert round(val(vt / vl, 1)) == 49


for _n, _lit, _t, _pt, _ps in [(90, "a", 15.0, "3,3", "3,3"), (91, "b", 75.0, "0,67", "0,23")]:
    @E(_n, f"{GEN} — 14{_lit}", dificultad=2,
       enunciado=rf"Determina la incertidumbre porcentual en $\theta$ y en "
                 rf"$\operatorname{{sen}}\theta$ cuando "
                 rf"$\theta = \num{{{str(_t).replace('.', ',')}}}^\circ \pm \num{{0,5}}^\circ$.",
       respuesta=rf"En $\theta$: $\num{{{_pt}}}\,\%$; en $\operatorname{{sen}}\theta$: "
                 rf"$\approx \num{{{_ps}}}\,\%$ (se calcula "
                 rf"$\dfrac{{\operatorname{{sen}}(\theta + \num{{0,5}}^\circ) - "
                 rf"\operatorname{{sen}}\theta}}{{\operatorname{{sen}}\theta}}$).",
       notas="En la guía los ángulos llevan punto decimal («15.0° ± 0.5°»); se usa coma.")
    def _(t=_t, pt=_pt, ps=_ps):
        q = float(pt.replace(",", "."))
        assert abs(0.5 / t * 100 - q) < 0.02 * q               # redondeado a dos cifras
        rel = (sin(radians(t + 0.5)) - sin(radians(t))) / sin(radians(t)) * 100
        p = float(ps.replace(",", "."))
        assert abs(rel - p) < 0.05 * p
        assert abs(rel - radians(0.5) / tan(radians(t)) * 100) < 0.03 * rel   # derivada

M(92, f"{GEN} — 15",
  r"Haz una estimación burda del volumen de tu cuerpo en centímetros cúbicos.",
  r"El cuerpo es casi todo agua (densidad $\approx 1\ \mathrm{g/cm^3}$): una persona de "
  r"60 kg ocupa unos $\num{60000}\ \mathrm{cm^3}$ ($\approx \num{6e4}\ \mathrm{cm^3}$). "
  r"También vale modelarlo como un cilindro de $\num{1,7}$ m de alto y 20 cm de diámetro.",
  tipo="contexto")
M(93, f"{GEN} — 16",
  r"La capacidad pulmonar esperada, en litros, de una persona de altura $H$ (en metros) y "
  r"edad $A$ (en años) es $V = \num{4,1}H - \num{0,018}A - \num{2,69}$. ¿Cuáles son las "
  r"unidades de los números $\num{4,1}$, $\num{0,018}$ y $\num{2,69}$?",
  r"Cada término debe estar en litros: $\num{4,1}$ en L/m, $\num{0,018}$ en L/año y "
  r"$\num{2,69}$ en L.")
