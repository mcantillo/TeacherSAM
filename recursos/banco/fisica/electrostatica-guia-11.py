"""Banco de ejercicios — Física 11° — Electrostática: los pocos ejercicios que la guía del
trimestre I (materias/fisica/undecimo/guia-didactica/guia-periodo-I-electrostatica.tex) necesitaba
y el banco no tenía. Todo lo demás de la guía se reutiliza de `electrostatica-11.py` y
`notacion-cientifica-8.py` (regla «Reuse, don't multiply», 2026-09-15).

- 001: predecir el signo por frotamiento y contacto con una serie triboeléctrica (evidencia 1 del
  DBA 2 de 11°; en el banco solo había selecciones manuales pendientes sobre esto).
- 002–005: «Prepárate para Saber 11», selección múltiple con contexto colombiano (las selecciones
  de electrostatica-11 son manuales pendientes y no traen esos contextos).

Serie de materiales (tendencia a quedar positivo → negativo): vidrio, papel, lana, polietileno,
PVC, tomada de la tabla de AlphaLab reproducida por el Departamento de Física de la Universidad
de Iowa (vidrio +25, papel +10, lana 0, polietileno −90, PVC −100):
https://instructional-resources.physics.uiowa.edu/5a1015-triboelectric-series

Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/fisica/electrostatica-guia-11.py
"""
from sympy import Rational, symbols
from sympy.physics import units as u
from sympy.physics.units import convert_to

from ejercicios import ejercicio

FUENTE = "Propio, guía Física 11° trimestre I (plan guia-periodo-I-electrostatica.plan.md)"
COMUN = dict(tema="electrostática", grados=[11], dba=["naturales-11-2"], fuente=FUENTE)

e = u.elementary_charge
N, C = u.newton, u.coulomb


def valor(q, unidad):
    return float(convert_to(q, unidad) / unidad)


def aprox(a, b, rel=0.01):
    return abs(a - b) <= rel * abs(b)


def nid(n):
    return f"electrostatica-guia-11-{n:03d}"


# ---------------------------------------------------------------- Tema 2: la carga
SERIE = ["vidrio", "papel", "lana", "polietileno", "PVC"]   # de + a −


def signo_frotado(a, b):
    """Signo que adquiere `a` al frotarse con `b`: el que está antes en la serie queda +."""
    return +1 if SERIE.index(a) < SERIE.index(b) else -1


@ejercicio(id=nid(1), tipo="conceptual", dificultad=2,
           enunciado=r"Usa la serie de la figura (vidrio, papel, lana, polietileno, PVC, de mayor a "
                     r"menor tendencia a quedar positivo). Al frotar dos materiales, el que está "
                     r"más a la izquierda cede electrones. Predice el signo que adquiere cada "
                     r"material: \begin{opciones*}(1) \item un tubo de PVC frotado con lana; "
                     r"\item una lámina de vidrio frotada con una bolsa de polietileno; \item una "
                     r"hoja de papel frotada con lana. \end{opciones*} Después, el tubo de PVC del "
                     r"literal a) toca una esfera metálica neutra y aislada. ¿Qué signo adquiere "
                     r"la esfera?",
           respuesta=r"a) PVC negativo, lana positiva. b) Vidrio positivo, polietileno negativo. "
                     r"c) Papel positivo, lana negativa. La esfera queda negativa: por contacto "
                     r"los dos cuerpos quedan con carga del mismo signo.",
           notas="Serie: tabla de AlphaLab en la página de la Universidad de Iowa (ver docstring). "
                 "La lana es positiva frente al PVC y negativa frente al papel: el signo depende "
                 "del par, no del material.", **COMUN)
def _():
    assert signo_frotado("PVC", "lana") == -1 and signo_frotado("lana", "PVC") == +1
    assert signo_frotado("vidrio", "polietileno") == +1
    assert signo_frotado("papel", "lana") == +1 and signo_frotado("lana", "papel") == -1
    # contacto: la carga negativa del PVC se reparte; la esfera queda con el mismo signo
    q_pvc, q_esfera = -1, 0
    assert (q_pvc + q_esfera) / 2 < 0


# ---------------------------------------------------------------- Prepárate para Saber 11
def sm(n, enunciado, opciones, correcta, respuesta, cols=4, dificultad=2):
    items = " ".join(r"\item " + o for o in opciones)
    return ejercicio(id=nid(n), tipo="seleccion", dificultad=dificultad,
                     enunciado=enunciado + rf" \begin{{opciones*}}({cols}) {items} \end{{opciones*}}",
                     respuesta=f"{correcta}) " + respuesta, **COMUN)


@sm(2, r"Para una fiesta en Cali, Sofía infla un globo y lo frota contra su pelo. El globo "
       r"queda con $\num{2,0e13}$ electrones en exceso. Si la carga de un electrón es "
       r"$\num{-1,602e-19}$ C, la carga del globo es, aproximadamente:",
    [r"$\num{3,2}\ \mu$C", r"$\num{-3,2}$ nC", r"$\num{-3,2}\ \mu$C", r"$\num{3,2}$ nC"], "c",
    r"$q = (\num{2,0e13})(\num{-1,602e-19}\ \text{C}) \approx \num{-3,2e-6}$ C.")
def _():
    q = valor(-2 * 10**13 * e, C)
    valores = {"a": 3.2e-6, "b": -3.2e-9, "c": -3.2e-6, "d": 3.2e-9}
    assert [l for l, v in valores.items() if aprox(q, v)] == ["c"]


@sm(3, r"En el laboratorio, dos esferitas con cargas iguales se repelen con una fuerza $F$ "
       r"cuando están separadas una distancia $d$. Si la separación se reduce a $d/2$, la fuerza "
       r"entre ellas será:",
    [r"$4F$", r"$F/4$", r"$2F$", r"$F/2$"], "a",
    r"$F \propto 1/d^2$: con $d/2$ la fuerza se multiplica por $2^2 = 4$.")
def _():
    q, d = symbols("q d", positive=True)
    F = lambda s: q**2 / s**2
    razon = F(d / 2) / F(d)
    valores = {"a": 4, "b": Rational(1, 4), "c": 2, "d": Rational(1, 2)}
    assert [l for l, v in valores.items() if razon == v] == ["a"]


@sm(4, r"Un tubo de PVC frotado con lana queda cargado negativamente y se acerca, sin tocarla, a "
       r"una esfera metálica neutra y aislada. Mientras el tubo está cerca, en la esfera:",
    [r"entran electrones del tubo y la esfera queda negativa",
     r"salen protones y la esfera queda negativa",
     r"no ocurre nada, porque el tubo no la toca",
     r"los electrones se alejan del tubo: la cara cercana queda positiva y la carga total sigue "
     r"siendo cero"], "d",
    r"Inducción: sin contacto no hay transferencia de carga (la total sigue en cero); los "
    r"protones no se mueven y los electrones libres son repelidos por el tubo negativo.", cols=1)
def _():
    # Modelo: sin contacto no entra ni sale carga; los protones están fijos en la red;
    # los electrones libres se desplazan alejándose de un inductor negativo.
    contacto, inductor = False, -1
    carga_total = 0
    se_mueven_protones = False
    cara_cercana = -inductor                 # electrones repelidos → cara cercana +
    efecto = {
        "a": contacto and carga_total < 0,
        "b": se_mueven_protones,
        "c": False,                          # sí hay reacomodo de carga
        "d": (not contacto) and carga_total == 0 and cara_cercana > 0,
    }
    assert [l for l, v in efecto.items() if v] == ["d"]


@sm(5, r"Durante una tormenta en una finca del Valle del Cauca, supón que cerca del suelo el campo "
       r"eléctrico apunta verticalmente hacia arriba y vale $\num{1,0e4}$ N/C. Sobre una gotita "
       r"de agua con carga $\num{-2,0e-12}$ C la fuerza eléctrica es:",
    [r"$\num{2,0e-8}$ N hacia arriba", r"$\num{2,0e-8}$ N hacia abajo", r"cero, porque la carga "
     r"es negativa", r"$\num{5,0e15}$ N hacia abajo"], "b",
    r"$F = |q|E = (\num{2,0e-12})(\num{1,0e4}) = \num{2,0e-8}$ N, opuesta al campo porque la "
    r"carga es negativa: hacia abajo.", cols=2)
def _():
    E = 1.0e4 * N / C            # +: hacia arriba
    q = -2.0e-12 * C
    F = valor(q * E, N)          # con signo
    assert aprox(F, -2.0e-8)
    opciones = {"a": 2.0e-8, "b": -2.0e-8, "c": 0.0, "d": -5.0e15}
    assert [l for l, v in opciones.items() if v != 0 and aprox(F, v)] == ["b"]
