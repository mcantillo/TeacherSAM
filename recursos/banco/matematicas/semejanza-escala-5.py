"""Banco de ejercicios — Matemáticas (Geometría 5°) — Figuras semejantes, mapas y dibujos a escala.
Fuente: módulo de Matemáticas 5° de las Guías de Apoyo, Tema 5 (Proporciones), secciones
«Figuras semejantes» y «Mapas y dibujos a escala» — Práctica lo aprendido; se lee en
recursos/matematicas/Guías pedagógicas Matemáticas/markdown/05 - Modulo_Matematicas_Quinto.md
El módulo no trae clave: las respuestas se calcularon y se comprueban aquí.
Nota: en el ejemplo de «Mapas y dibujos a escala» (no es ejercicio) el módulo escribe
«La escala es 10 pulgs: 2 pulgs» aunque las medidas están en dm.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/semejanza-escala-5.py
"""
from sympy import Rational, Symbol, solve
from sympy.physics.units import centimeter, convert_to, kilometer, meter, millimeter, minute

from ejercicios import ejercicio, ejercicio_manual

FS = "módulo 5° (Guías de Apoyo), Tema 5, Figuras semejantes — Práctica lo aprendido"
FE = "módulo 5° (Guías de Apoyo), Tema 5, Mapas y dibujos a escala — Práctica lo aprendido"
COMUN = dict(tema="semejanza y escala", grados=[5], dba=["matematicas-5-4", "matematicas-5-6"])
x = Symbol("x", positive=True)


def opciones(*items):
    return r" \begin{opciones} " + " ".join(r"\item " + i for i in items) + r" \end{opciones}"


def cm(v):
    return convert_to(v, centimeter)


# ---------- Figuras semejantes ----------

@ejercicio(id="semejanza-escala-5-001", tipo="calculo", dificultad=1, fuente=f"{FS} 1",
           enunciado=r"Los rectángulos 1, 2 y 3 son semejantes. El rectángulo 1 mide 7 cm de "
                     r"largo y 2 cm de ancho; el rectángulo 2 mide $x$ de largo y 12 cm de ancho, "
                     r"y el rectángulo 3 mide 49 cm de largo y $y$ de ancho. Usa proporciones "
                     r"para hallar las longitudes que faltan.",
           respuesta=r"$\frac{7}{2} = \frac{x}{12}$, así que $x = 42$ cm; "
                     r"$\frac{7}{2} = \frac{49}{y}$, así que $y = 14$ cm.",
           notas="El módulo solo da las figuras; se escribió en el enunciado que los tres "
                 "rectángulos son semejantes y sus medidas.", **COMUN)
def _():
    assert solve(Rational(7, 2) - x / 12, x) == [42]
    assert solve(Rational(7, 2) - 49 / x, x) == [14]


@ejercicio(id="semejanza-escala-5-002", tipo="contexto", dificultad=1, fuente=f"{FS} 2",
           enunciado=r"Un ingeniero automotriz está diseñando un carro a partir de un modelo a "
                     r"escala $1:10$. Si el modelo tiene 40 cm de longitud, ¿cuál es la longitud "
                     r"del carro que está diseñando?",
           respuesta=r"$40 \times 10 = 400$ cm, es decir, 4 m.",
           notas="En el módulo la escala es 1:4, que da un carro de 1,6 m (irreal); se cambió a "
                 "1:10 para que mida 4 m, como un carro de verdad.", **COMUN)
def _():
    real = convert_to(40 * centimeter * 10, meter)
    assert real == 4 * meter
    assert 3 < real / meter < 6                  # longitud realista de un carro (en m)
    assert convert_to(40 * centimeter * 4, meter) / meter < 2    # con 1:4 no lo sería


TABLA = (r"Rectángulo A: 5 cm de longitud y 19 cm de ancho; rectángulo B: 20 cm y 38 cm; "
         r"rectángulo C: 15 cm y 57 cm.")


@ejercicio(id="semejanza-escala-5-003", tipo="argumentacion", dificultad=2, fuente=f"{FS} 3a",
           enunciado=TABLA + r" ¿Qué rectángulos son figuras semejantes? Explica por qué.",
           respuesta=r"A y C: $\frac{5}{19} = \frac{15}{57}$ (C es A con cada lado multiplicado "
                     r"por 3). B no es semejante a ellos: $\frac{20}{38} = \frac{10}{19} \ne "
                     r"\frac{5}{19}$.", **COMUN)
def _():
    r = {k: Rational(a, b) for k, (a, b) in dict(A=(5, 19), B=(20, 38), C=(15, 57)).items()}
    assert r["A"] == r["C"] and r["B"] != r["A"]


@ejercicio(id="semejanza-escala-5-004", tipo="calculo", dificultad=1, fuente=f"{FS} 3b",
           enunciado=TABLA + r" Si un rectángulo de 25 cm de longitud es semejante al "
                     r"rectángulo A, ¿cuál es su ancho?",
           respuesta=r"$\frac{5}{19} = \frac{25}{x}$, así que $x = 95$ cm.", **COMUN)
def _():
    assert solve(Rational(5, 19) - 25 / x, x) == [95]


ejercicio_manual(id="semejanza-escala-5-005", tipo="conceptual", dificultad=1, fuente=f"{FS} 3c",
                 enunciado=TABLA + r" Haz un diagrama de un rectángulo que sea semejante al "
                           r"rectángulo A.",
                 respuesta=r"Cualquier rectángulo cuyos lados estén en la razón $5:19$; por "
                           r"ejemplo, uno de 1 cm por \num{3,8} cm (A dividido entre 5) o uno de "
                           r"\num{2,5} cm por \num{9,5} cm (A dividido entre 2).",
                 notas="El módulo dice «semejante al Rectángulo 6», que no existe (la tabla tiene "
                       "A, B y C); se cambió por A.", **COMUN)


@ejercicio(id="semejanza-escala-5-006", tipo="contexto", dificultad=2, fuente=f"{FS} 4",
           enunciado=r"Dos rectángulos son semejantes. Uno mide \num{98,5} m de longitud y 50 m de "
                     r"ancho. Si el otro mide 25 m de ancho, estima su longitud y luego calcúlala.",
           respuesta=r"El ancho se reduce a la mitad, así que la longitud también: cerca de 49 m; "
                     r"exactamente $\num{98,5} \div 2 = \num{49,25}$ m.", **COMUN)
def _():
    L = solve(Rational(985, 10) / 50 - x / 25, x)[0]
    assert L == Rational(4925, 100) and abs(L - 49) < 1


@ejercicio(id="semejanza-escala-5-007", tipo="contexto", dificultad=2, fuente=f"{FS} 5",
           enunciado=r"Tania quiere saber la altura del asta de la bandera que está frente a su "
                     r"escuela. A la misma hora, la sombra de una regla de 1 m mide 2 m y la "
                     r"sombra del asta mide \num{20,2} m. ¿Cuál es la altura del asta?",
           respuesta=r"$\frac{1}{2} = \frac{x}{\num{20,2}}$, así que el asta mide \num{10,1} m.",
           **COMUN)
def _():
    h = solve(Rational(1, 2) - x / Rational(202, 10), x)[0]
    assert h == Rational(101, 10) and 5 < h < 20           # altura realista de un asta


# ---------- Mapas y dibujos a escala ----------

@ejercicio(id="semejanza-escala-5-008", tipo="calculo", dificultad=1, fuente=f"{FE} 1a",
           enunciado=r"Si la escala de un mapa es 1 cm : 15 km, ¿cuántos kilómetros representan "
                     r"\num{6,5} cm?",
           respuesta=r"$\num{6,5} \times 15 = \num{97,5}$ km.", **COMUN)
def _():
    assert Rational(65, 10) * 15 * kilometer == Rational(975, 10) * kilometer


@ejercicio(id="semejanza-escala-5-009", tipo="calculo", dificultad=1, fuente=f"{FE} 1b",
           enunciado=r"Si la escala de un mapa es 1 dm : 550 m, ¿cuál es la distancia real si la "
                     r"distancia en el mapa es 7 dm?",
           respuesta=r"$7 \times 550 = 3850$ m, es decir, \num{3,85} km.", **COMUN)
def _():
    d = 7 * 550 * meter
    assert convert_to(d, kilometer) == Rational(385, 100) * kilometer


@ejercicio(id="semejanza-escala-5-010", tipo="contexto", dificultad=2, fuente=f"{FE} 2",
           enunciado=r"Para el anuario escolar se va a reducir una foto de 10 dm de alto y 8 dm "
                     r"de ancho, sin deformarla, para que quepa en un espacio de 4 cm de alto. "
                     r"¿Qué estrategia usarías para hallar el ancho? ¿Cuál es el ancho?",
           respuesta=r"Una proporción entre alto y ancho: $\frac{10}{8} = \frac{4}{y}$ "
                     r"(10 dm = 100 cm se reduce a 4 cm, 25 veces menos). El ancho es "
                     r"\num{3,2} cm.",
           notas="El módulo remite a «el anuario de arriba» (el ejemplo de la sección); se "
                 "escribieron las medidas de la foto en el enunciado.", **COMUN)
def _():
    alto, ancho = convert_to(10 * 10 * centimeter, centimeter), 8 * 10 * centimeter
    y = ancho * (4 * centimeter) / alto
    assert cm(y) == Rational(32, 10) * centimeter


ejercicio_manual(id="semejanza-escala-5-011", tipo="conceptual", dificultad=2, fuente=f"{FE} 3",
                 enunciado=r"Escribe un problema de la vida diaria usando esta información: un "
                           r"plano tiene una escala de 1 cm : 2 m.",
                 respuesta=r"Por ejemplo: «En el plano de la casa, la sala mide 3 cm de largo y "
                           r"\num{2,5} cm de ancho. ¿Cuáles son sus medidas reales?» Respuesta: "
                           r"6 m por 5 m. Se acepta cualquier problema que multiplique (o divida) "
                           r"por 200 las medidas.", **COMUN)

ANDRES = (r"En un dibujo a escala, \num{0,5} cm representan 1 km. La casa de Andrés, el parque "
          r"acuático y el teatro forman un triángulo: de la casa al parque hay 1 cm, del parque "
          r"al teatro \num{1,5} cm y del teatro a la casa \num{1,25} cm.")
NOTA_ANDRES = ("En el módulo la escala es «0,5 cm = 1 m», que da caminatas de 2 m en 30 minutos; "
               "se cambió a 0,5 cm = 1 km.")


def real(cm_dibujo):
    return cm_dibujo * 2 * kilometer                 # 0,5 cm → 1 km


@ejercicio(id="semejanza-escala-5-012", tipo="contexto", dificultad=1, fuente=f"{FE} 4a",
           enunciado=ANDRES + r" Andrés caminó de su casa al parque acuático. ¿Cuál fue la "
                     r"distancia real que caminó?",
           respuesta=r"1 cm son dos veces \num{0,5} cm: 2 km.", notas=NOTA_ANDRES, **COMUN)
def _():
    lados = [1, Rational(3, 2), Rational(5, 4)]
    assert 2 * max(lados) < sum(lados)                           # el triángulo existe
    assert real(1) == 2 * kilometer


@ejercicio(id="semejanza-escala-5-013", tipo="contexto", dificultad=2, fuente=f"{FE} 4b",
           enunciado=ANDRES + r" Andrés tardó 30 minutos en caminar de su casa al parque "
                     r"acuático. Si camina al mismo ritmo, ¿cuánto tardará en caminar del parque "
                     r"acuático al teatro?",
           respuesta=r"Del parque al teatro hay 3 km; si 2 km le toman 30 minutos, 1 km le toma "
                     r"15 minutos: tardará 45 minutos.", notas=NOTA_ANDRES, **COMUN)
def _():
    ritmo = 30 * minute / real(1)
    t = ritmo * real(Rational(3, 2))
    assert t == 45 * minute
    assert convert_to(real(1) / (30 * minute), kilometer / minute) * 60 == 4 * kilometer / minute


@ejercicio(id="semejanza-escala-5-014", tipo="contexto", dificultad=2, fuente=f"{FE} 4c",
           enunciado=ANDRES + r" Si Andrés caminó de su casa al teatro, del teatro al parque "
                     r"acuático y del parque acuático a su casa, ¿cuál fue la distancia total "
                     r"real que caminó?",
           respuesta=r"En el dibujo, $\num{1,25} + \num{1,5} + 1 = \num{3,75}$ cm, que representan "
                     r"\num{7,5} km.", notas=NOTA_ANDRES, **COMUN)
def _():
    assert real(Rational(5, 4) + Rational(3, 2) + 1) == Rational(15, 2) * kilometer


@ejercicio(id="semejanza-escala-5-015", tipo="contexto", dificultad=2, fuente=f"{FE} 5",
           enunciado=r"El edificio Empire State, en Nueva York, mide aproximadamente 381 m de "
                     r"altura. Si haces un modelo con la escala 1 cm : 50 m, usa una proporción "
                     r"para hallar la altura de tu modelo.",
           respuesta=r"$\frac{1}{50} = \frac{x}{381}$, así que el modelo mide \num{7,62} cm.",
           notas="En el módulo aparece «I cm = 50 m»; se corrigió a 1 cm.", **COMUN)
def _():
    assert solve(Rational(1, 50) - x / 381, x) == [Rational(762, 100)]


@ejercicio(id="semejanza-escala-5-016", tipo="seleccion", dificultad=2, fuente=f"{FE} 6",
           enunciado=r"En un dibujo a escala de un chip de computador, 100 mm en el dibujo "
                     r"representan 1 mm del tamaño real. ¿Cuál de las expresiones da la longitud "
                     r"real de una pieza que en el dibujo mide 3 mm?"
                     + opciones(r"$3 \times 100$", r"$3 - 100$", r"$3 \div 100$", r"$100 \div 3$"),
           respuesta=r"c. $3 \div 100$ (la pieza real mide \num{0,03} mm).", **COMUN)
def _():
    correcta = 3 * millimeter / 100
    valores = [3 * 100, 3 - 100, Rational(3, 100), Rational(100, 3)]
    assert [v * millimeter == correcta for v in valores] == [False, False, True, False]


@ejercicio(id="semejanza-escala-5-017", tipo="calculo", dificultad=1, fuente=f"{FE} 7",
           enunciado=r"Los rectángulos A y B son semejantes. A mide 4 mm de largo y 3 mm de "
                     r"ancho; B mide 24 mm de largo y $h$ de ancho. Halla $h$.",
           respuesta=r"$\frac{4}{3} = \frac{24}{h}$, así que $h = 18$ mm.", **COMUN)
def _():
    assert solve(Rational(4, 3) - 24 / x, x) == [18]


ejercicio_manual(id="semejanza-escala-5-018", tipo="conceptual", dificultad=1, fuente=f"{FE} 8",
                 enunciado=r"En papel cuadriculado, dibuja un lápiz. Luego dibuja otro lápiz "
                           r"semejante que sea dos veces más grande que el primero. Incluye una "
                           r"escala en tu dibujo.",
                 respuesta=r"Por ejemplo, un lápiz de 6 cuadritos de largo y 1 de ancho y otro de "
                           r"12 cuadritos de largo y 2 de ancho (todas las medidas se duplican), "
                           r"con la escala «1 cuadrito del primer dibujo : 2 cuadritos del "
                           r"segundo» o «2 : 1».", **COMUN)


@ejercicio(id="semejanza-escala-5-019", tipo="contexto", dificultad=1, fuente=f"{FE} 9",
           enunciado=r"Si la distancia real entre dos ciudades es aproximadamente 200 km, ¿cuál "
                     r"sería la distancia en un mapa con escala \num{0,5} cm : 50 km?",
           respuesta=r"200 km son 4 veces 50 km: $4 \times \num{0,5} = 2$ cm.", **COMUN)
def _():
    assert (200 * kilometer) / (50 * kilometer) * Rational(1, 2) * centimeter == 2 * centimeter
