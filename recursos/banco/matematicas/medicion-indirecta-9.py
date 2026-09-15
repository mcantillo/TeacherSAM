"""Banco de ejercicios — Geometría 9° — Estrategias de medición y precisión (guía del trimestre I, 2026-09-15).
DBA 5 de 9°. Excepción a «solo banco»: el banco verificado no tenía NADA para las evidencias
«Valida la precisión de instrumentos para medir longitudes» y «Propone alternativas para estimar
y medir con precisión», ni el ejemplo del DBA (Camila). Solo dos ejercicios, los mínimos.
  - 006: ejemplo del DBA 5 de 9°. ERROR DEL DBA: el texto llama h a la distancia al árbol, pero
    la figura llama h a la estatura de la persona; aquí d es la distancia y h la altura de los ojos.
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/medicion-indirecta-9.py
"""
from sympy import Rational

from ejercicios import ejercicio

PROPIO = "propio (guía Geometría 9°, trimestre I)"
COMUN = dict(tema="estrategias de medición", grados=[9], dba=["matematicas-9-5"])


@ejercicio(id="medicion-indirecta-9-006", tipo="contexto", dificultad=2,
           fuente="ejemplo del DBA 5 de grado 9 (MEN, 2016): Camila y la escuadra con plomada",
           enunciado=r"Camila mira un ave por un pitillo pegado a la hipotenusa de una escuadra "
                     r"isósceles ($45^\circ$), con una plomada que mantiene un cateto vertical. Se "
                     r"acerca al árbol hasta ver el ave por el pitillo; en ese punto mide la distancia "
                     r"al árbol, $d = \num{8,4}$~m. Sus ojos están a $h = \num{1,55}$~m del suelo. ¿A "
                     r"qué altura está el ave? Justifica.",
           respuesta=r"La visual forma $45^\circ$ con la horizontal, así que el triángulo formado por "
                     r"la visual, la horizontal a la altura de los ojos y el árbol es rectángulo "
                     r"isósceles: la altura sobre los ojos es $H = d = \num{8,4}$~m. El ave está a "
                     r"$h + H = \num{1,55} + \num{8,4} = \num{9,95}$~m.",
           notas="En el DBA, el texto llama h a la distancia al árbol y la figura llama h a la "
                 "estatura; aquí d es la distancia y h la altura de los ojos.", **COMUN)
def _():
    d, h = Rational("8.4"), Rational("1.55")
    H = d * 1                                    # tan 45° = 1: catetos iguales
    assert h + H == Rational("9.95")


@ejercicio(id="medicion-indirecta-9-008", tipo="contexto", dificultad=2, fuente=PROPIO,
           enunciado=r"Para medir el asta de la bandera del colegio, un palo de $\num{1,20}$~m da una "
                     r"sombra de $\num{0,80}$~m. Cuatro estudiantes miden la sombra del asta y obtienen "
                     r"$\num{6,10}$, $\num{6,25}$, $\num{6,05}$ y $\num{6,20}$~m. a) Calcula la altura "
                     r"con el promedio. b) ¿Entre qué valores está la altura según la medida más "
                     r"pequeña y la más grande? c) ¿Cómo reportarías el resultado?",
           respuesta=r"a) Promedio $\num{6,15}$~m; altura $\num{6,15} \cdot \frac{\num{1,20}}{\num{0,80}} "
                     r"= \num{9,225} \approx \num{9,2}$~m. b) Entre $\num{9,075}$ y $\num{9,375}$~m. "
                     r"c) Unos $\num{9,2}$~m con un margen de $\pm \num{0,2}$~m: no tiene sentido dar "
                     r"tres decimales si las medidas varían en décimas.", **COMUN)
def _():
    s = [Rational(x) for x in ("6.10", "6.25", "6.05", "6.20")]
    k = Rational("1.20") / Rational("0.80")
    prom = sum(s) / 4
    assert prom == Rational("6.15") and prom * k == Rational("9.225")
    assert min(s) * k == Rational("9.075") and max(s) * k == Rational("9.375")
