"""Banco de ejercicios — Trigonometría 10° — Razones trigonométricas y triángulo rectángulo.
Fuente: módulo de Matemáticas 10° de las Guías de Apoyo, Tema 1 («Trigonometría del triángulo
rectángulo»: Practica lo aprendido y Prepárate para el ICFES) y los problemas 1 y 2 del
«Prepárate para el ICFES» final del módulo; se lee en
recursos/matematicas/Guías pedagógicas Matemáticas/markdown/10 - Modulo_Matematicas_Decimo.md
Las medidas del módulo están en pies y pulgadas; se conservan.
Convención: lados redondeados a una décima (o a tres cifras significativas si son pequeños),
ángulos a una décima de grado, valores de razones a cuatro decimales.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/razones-trigonometricas-10.py
"""
from math import atan, atan2, asin, acos, cos, hypot, pi, sin, sqrt, tan
from math import degrees as grd
from math import radians as rad

import sympy as sp

from ejercicios import ejercicio

PRE = "razones-trigonometricas-10"
FP = "módulo 10° (Guías de Apoyo), Tema 1, Trigonometría del triángulo rectángulo — Practica lo aprendido"
FI = ("módulo 10° (Guías de Apoyo), Tema 1, Trigonometría del triángulo rectángulo — "
      "Prepárate para el ICFES")
FR = "módulo 10° (Guías de Apoyo), Resumen del capítulo — Prepárate para el ICFES"
COMUN = dict(tema="razones trigonométricas", grados=[10], dba=["matematicas-10-4"])


def N(x):
    """\\num{…} con coma decimal a partir de un texto «41.3»."""
    return r"\num{" + str(x).replace(".", ",") + "}"


def cerca(calc, mano, dec):
    assert abs(calc - mano) <= 0.5 * 10 ** -dec + 1e-9, f"calculado {calc}, a mano {mano}"


def reg(n, fuente, enunciado, respuesta, check, tipo="calculo", dificultad=1, notas=None):
    meta = dict(id=f"{PRE}-{n:03d}", fuente=fuente, enunciado=enunciado, respuesta=respuesta,
                tipo=tipo, dificultad=dificultad, **COMUN)
    if notas:
        meta["notas"] = notas
    ejercicio(**meta)(check)


FUN = {"sen": sin, "cos": cos, "tg": tan}
INV = {"sen": asin, "cos": acos, "tg": atan}

# ---------- 1. Evaluar con calculadora (grados) ----------
for n, lit, f, g, v in [(1, "a", "sen", "41.3", "0.6600"), (2, "b", "sen", "89.3", "0.9999"),
                        (3, "c", "tg", "54.4", "1.3968"), (4, "d", "tg", "72.3", "3.1334"),
                        (5, "e", "cos", "49.2", "0.6534"), (6, "f", "cos", "38.7", "0.7804")]:
    reg(n, f"{FP} 1{lit}",
        r"Usa la calculadora (en modo grados) para evaluar $\%s %s^\circ$. Da el resultado con "
        r"cuatro decimales." % (f, N(g)),
        r"$\%s %s^\circ \approx %s$." % (f, N(g), N(v)),
        lambda F=FUN[f], g=float(g), v=float(v): cerca(F(rad(g)), v, 4))

# ---------- 2. Ángulo agudo a partir del valor de la razón ----------
for n, lit, f, x, v in [(7, "a", "sen", "0.2164", "12.5"), (8, "b", "cos", "0.9354", "20.7"),
                        (9, "c", "tg", "0.3096", "17.2"), (10, "d", "cos", "0.3535", "69.3"),
                        (11, "e", "tg", "2.311", "66.6"), (12, "f", "sen", "0.7302", "46.9")]:
    reg(n, f"{FP} 2{lit}",
        r"Con la calculadora, encuentra el ángulo agudo $\theta$ (en grados, a la décima) tal que "
        r"$\%s \theta = %s$." % (f, N(x)),
        r"$\theta \approx %s^\circ$." % N(v),
        lambda G=INV[f], x=float(x), v=float(v): cerca(grd(G(x)), v, 1))

# ---------- 3. Encontrar x (figuras del módulo descritas en palabras) ----------
reg(13, f"{FP} 3a",
    r"En un triángulo rectángulo la hipotenusa mide $35$ y uno de los ángulos agudos mide "
    r"$29^\circ$. Halla la longitud $x$ del cateto opuesto a ese ángulo.",
    r"$x = 35 \sen 29^\circ \approx \num{17,0}$.",
    lambda: cerca(35 * sin(rad(29)), 17.0, 1))
reg(14, f"{FP} 3b",
    r"En un triángulo rectángulo la hipotenusa mide $60$ y uno de los ángulos agudos mide "
    r"$43^\circ$. Halla la longitud $x$ del cateto adyacente a ese ángulo.",
    r"$x = 60 \cos 43^\circ \approx \num{43,9}$.",
    lambda: cerca(60 * cos(rad(43)), 43.9, 1))
reg(15, f"{FP} 3c",
    r"Un triángulo rectángulo tiene un ángulo agudo de $14^\circ$ y el cateto opuesto a ese "
    r"ángulo mide $10$. Halla la longitud $x$ de la hipotenusa.",
    r"$x = \dfrac{10}{\sen 14^\circ} \approx \num{41,3}$.",
    lambda: cerca(10 / sin(rad(14)), 41.3, 1),
    notas="En el módulo este literal aparece como «a.» (es el tercero, entre las figuras b y d).")
reg(16, f"{FP} 3d",
    r"En un triángulo rectángulo el cateto adyacente a un ángulo de $40^\circ$ mide $24$. Halla "
    r"la longitud $x$ de la hipotenusa.",
    r"$x = \dfrac{24}{\cos 40^\circ} \approx \num{31,3}$.",
    lambda: cerca(24 / cos(rad(40)), 31.3, 1))
reg(17, f"{FP} 3e",
    r"Dos triángulos rectángulos comparten un cateto vertical de longitud $20$. En uno, ese "
    r"cateto es opuesto a un ángulo de $26^\circ$; en el otro, es opuesto a un ángulo de "
    r"$38^\circ$. Los catetos horizontales están sobre la misma recta, uno a cada lado del "
    r"cateto común, y juntos miden $x$. Halla $x$.",
    r"$x = \dfrac{20}{\tg 26^\circ} + \dfrac{20}{\tg 38^\circ} \approx \num{41,0} + \num{25,6}"
    r" \approx \num{66,6}$.",
    lambda: cerca(20 / tan(rad(26)) + 20 / tan(rad(38)), 66.6, 1), dificultad=2,
    notas="La figura del módulo se describe en palabras.")
reg(18, f"{FP} 3f",
    r"Desde el pie $P$ de un poste vertical se mide sobre el suelo horizontal: a $15$ unidades "
    r"de $P$ el ángulo de elevación a la punta del poste es $44^\circ$, y a $15 + x$ unidades "
    r"(en la misma dirección) es $24^\circ$. Halla $x$.",
    r"La altura es $h = 15 \tg 44^\circ \approx \num{14,49}$ y $15 + x = \dfrac{h}{\tg 24^\circ}"
    r"$, así que $x = \dfrac{15 \tg 44^\circ}{\tg 24^\circ} - 15 \approx \num{17,5}$.",
    lambda: cerca(15 * tan(rad(44)) / tan(rad(24)) - 15, 17.5, 1), dificultad=2,
    notas="La figura del módulo (dos triángulos con un cateto opuesto común) se describe como "
          "un poste visto desde dos puntos.")


# ---------- Resolver triángulos rectángulos (gamma = 90°) ----------
def resolver(alfa=None, beta=None, a=None, b=None, c=None):
    if alfa is None and beta is not None:
        alfa = 90 - beta
    if alfa is not None:
        A = rad(alfa)
        if c is not None:
            a, b = c * sin(A), c * cos(A)
        elif a is not None:
            b, c = a / tan(A), a / sin(A)
        else:
            a, c = b * tan(A), b / cos(A)
    else:
        if c is None:
            c = hypot(a, b)
        elif b is None:
            assert c > a
            b = sqrt(c * c - a * a)
        else:
            assert c > b
            a = sqrt(c * c - b * b)
        alfa = grd(atan2(a, b))
    return dict(alfa=alfa, beta=90 - alfa, a=a, b=b, c=c)


SIMB = {"alfa": r"\alpha", "beta": r"\beta", "a": "a", "b": "b", "c": "c"}


def triangulo(n, fuente, datos, conocidos, resp, dificultad=1, notas=None):
    """resp: {nombre: (texto del valor, decimales, exacto)}."""
    partes = []
    for k, (v, dec, exacto) in resp.items():
        grado = r"^\circ" if k in ("alfa", "beta") else ""
        partes.append("$%s %s %s%s$" % (SIMB[k], "=" if exacto else r"\approx", N(v), grado))
    reg(n, fuente,
        r"Resuelve el triángulo rectángulo con $\gamma = 90^\circ$ (hipotenusa $c$) en el que "
        + datos + ". Dibújalo primero y marca sus partes.",
        ", ".join(partes[:-1]) + " y " + partes[-1] + ".",
        lambda k=conocidos, r=resp: [cerca(resolver(**k)[x], float(v), d)
                                     for x, (v, d, _) in r.items()],
        dificultad=dificultad, notas=notas)


T = True
F_ = False
triangulo(19, f"{FP} 4a", r"$\alpha = 42^\circ$ y $c = 35$", dict(alfa=42, c=35),
          dict(beta=("48", 0, T), a=("23.4", 1, F_), b=("26.0", 1, F_)))
triangulo(20, f"{FP} 4b", r"$\alpha = \num{56,2}^\circ$ y $c = \num{91,3}$",
          dict(alfa=56.2, c=91.3), dict(beta=("33.8", 1, T), a=("75.9", 1, F_), b=("50.8", 1, F_)))
triangulo(21, f"{FP} 4c", r"$\alpha = \num{39,4}^\circ$ y $a = 120$", dict(alfa=39.4, a=120),
          dict(beta=("50.6", 1, T), b=("146.1", 1, F_), c=("189.1", 1, F_)))
triangulo(22, f"{FP} 4d", r"$\beta = 29^\circ$ y $c = 50$", dict(beta=29, c=50),
          dict(alfa=("61", 0, T), a=("43.7", 1, F_), b=("24.2", 1, F_)))
triangulo(23, f"{FP} 4e", r"$\alpha = \num{69,9}^\circ$ y $c = \num{10,6}$",
          dict(alfa=69.9, c=10.6), dict(beta=("20.1", 1, T), a=("9.95", 2, F_), b=("3.64", 2, F_)))
triangulo(24, f"{FP} 4f", r"$\alpha = \num{40,6}^\circ$ y $b = 163$", dict(alfa=40.6, b=163),
          dict(beta=("49.4", 1, T), a=("139.7", 1, F_), c=("214.7", 1, F_)))
triangulo(25, f"{FP} 5a", r"$a = 9$ y $b = 12$", dict(a=9, b=12),
          dict(c=("15", 0, T), alfa=("36.9", 1, F_), beta=("53.1", 1, F_)))
triangulo(26, f"{FP} 5b", r"$a = 40$ y $c = 50$", dict(a=40, c=50),
          dict(b=("30", 0, T), alfa=("53.1", 1, F_), beta=("36.9", 1, F_)))
triangulo(27, f"{FP} 5c", r"$a = \num{14,6}$ y $c = \num{32,5}$", dict(a=14.6, c=32.5),
          dict(b=("29.0", 1, F_), alfa=("26.7", 1, F_), beta=("63.3", 1, F_)),
          notas="En el módulo: «a = 14.6, c = 32.5» con punto decimal; se escribe con coma.")
triangulo(28, f"{FP} 5d", r"$a = \num{9,52}$ y $b = \num{14,7}$", dict(a=9.52, b=14.7),
          dict(c=("17.51", 2, F_), alfa=("32.9", 1, F_), beta=("57.1", 1, F_)))
triangulo(29, f"{FP} 5e", r"$a = 24$ y $b = 10$", dict(a=24, b=10),
          dict(c=("26", 0, T), alfa=("67.4", 1, F_), beta=("22.6", 1, F_)))
triangulo(30, f"{FP} 5f", r"$c = 41$ y $a = 40$", dict(c=41, a=40),
          dict(b=("9", 0, T), alfa=("77.3", 1, F_), beta=("12.7", 1, F_)))
triangulo(31, f"{FP} 5g", r"$a = 243$ y $c = 419$", dict(a=243, c=419),
          dict(b=("341.3", 1, F_), alfa=("35.4", 1, F_), beta=("54.6", 1, F_)))
triangulo(32, f"{FP} 5h", r"$a = \num{0,123}$ y $b = \num{0,456}$", dict(a=0.123, b=0.456),
          dict(c=("0.472", 3, F_), alfa=("15.1", 1, F_), beta=("74.9", 1, F_)))

# ---------- Problemas de aplicación ----------
reg(33, f"{FP} 6",
    r"Una trayectoria recta que sube una colina se eleva $26$ pies por cada $100$ pies "
    r"horizontales. ¿Qué ángulo forma con la horizontal?",
    r"$\theta = \arctg \dfrac{26}{100} \approx \num{14,6}^\circ$.",
    lambda: cerca(grd(atan(26 / 100)), 14.6, 1), tipo="contexto")
reg(34, f"{FP} 7",
    r"Una escalera de $20$ pies de longitud se apoya en una pared y forma un ángulo de "
    r"$76^\circ$ con el suelo. ¿A qué altura de la pared llega el extremo superior de la "
    r"escalera?",
    r"$h = 20 \sen 76^\circ \approx \num{19,4}$ pies.",
    lambda: cerca(20 * sin(rad(76)), 19.4, 1), tipo="contexto",
    notas="En el módulo: «una escalera de 20 pies de altura»; los 20 pies son la longitud de "
          "la escalera (la altura es lo que se pregunta).")
reg(35, f"{FP} 8",
    r"Encuentra el ángulo de elevación del Sol si una mujer de $5$ pies y $9$ pulgadas de "
    r"estatura proyecta una sombra de $\num{46,8}$ pies. (El ángulo de elevación es el ángulo "
    r"hacia arriba formado con la horizontal; $1$ pie $= 12$ pulgadas.)",
    r"La estatura es $\num{5,75}$ pies; $\theta = \arctg \dfrac{\num{5,75}}{\num{46,8}} "
    r"\approx \num{7,0}^\circ$.",
    lambda: cerca(grd(atan((5 + 9 / 12) / 46.8)), 7.0, 1), tipo="contexto", dificultad=2)
reg(36, f"{FP} 9",
    r"Un alambre tensor atado a un poste forma un ángulo de $69^\circ$ con el suelo y está "
    r"fijado al suelo a $14$ pies del poste. ¿A qué altura del poste está atado el alambre?",
    r"$h = 14 \tg 69^\circ \approx \num{36,5}$ pies.",
    lambda: cerca(14 * tan(rad(69)), 36.5, 1), tipo="contexto")
reg(37, f"{FP} 10",
    r"La mujer del problema anterior del ángulo de elevación del Sol ($5$ pies $9$ pulgadas de "
    r"estatura, sombra de $\num{46,8}$ pies) camina con su hija Susana, que mide $3$ pies y "
    r"$10$ pulgadas. ¿Qué longitud tiene la sombra de Susana en ese momento?",
    r"Con el mismo ángulo de elevación, las sombras son proporcionales a las estaturas: "
    r"$s = \num{46,8} \cdot \dfrac{46}{69} = \num{31,2}$ pies.",
    lambda: cerca((3 + 10 / 12) / tan(atan((5 + 9 / 12) / 46.8)), 31.2, 1), tipo="contexto",
    dificultad=2,
    notas="En el módulo: «la mujer del problema 35»; es el problema 8 de esta lista.")
reg(38, f"{FP} 11",
    r"En el problema del alambre tensor (ángulo de $69^\circ$ con el suelo, fijado a $14$ pies "
    r"del poste), encuentra la longitud del alambre.",
    r"$L = \dfrac{14}{\cos 69^\circ} \approx \num{39,1}$ pies.",
    lambda: cerca(14 / cos(rad(69)), 39.1, 1), tipo="contexto")

for n, lit, tx, v, dec, fn in [
        (39, "a", r"\tg \num{14,5}^\circ", "0.2586", 4, lambda: tan(rad(14.5))),
        (40, "b", r"\num{24,6} \cos \num{74,3}^\circ", "6.657", 3, lambda: 24.6 * cos(rad(74.3))),
        (41, "c", r"\num{15,6}\,\dfrac{(\sen 14^\circ)^2}{\cos 87^\circ}", "17.45", 2,
         lambda: 15.6 * sin(rad(14)) ** 2 / cos(rad(87)))]:
    reg(n, f"{FI} 12{lit}", r"Calcula con la calculadora $%s$." % tx, r"$%s \approx %s$." % (tx, N(v)),
        lambda fn=fn, v=float(v), dec=dec: cerca(fn(), v, dec))
for n, lit, f, x, v in [(42, "a", "sen", "0.6691", "42.0"), (43, "b", "cos", "0.5519", "56.5"),
                        (44, "c", "tg", "5.396", "79.5")]:
    reg(n, f"{FI} 13{lit}",
        r"Encuentra el ángulo agudo $\theta$ (en grados, a la décima) tal que $\%s \theta = %s$."
        % (f, N(x)), r"$\theta \approx %s^\circ$." % N(v),
        lambda G=INV[f], x=float(x), v=float(v): cerca(grd(G(x)), v, 1))

reg(45, f"{FI} 14",
    r"Desde la punta de un faro, a $120$ pies sobre el nivel del mar, el ángulo de depresión "
    r"(el ángulo hacia abajo desde la horizontal) hacia un barco a la deriva es de "
    r"$\num{9,4}^\circ$. ¿A qué distancia está el barco de la base del faro?",
    r"$d = \dfrac{120}{\tg \num{9,4}^\circ} \approx 725$ pies.",
    lambda: cerca(120 / tan(rad(9.4)), 725, 0), tipo="contexto")
triangulo(46, f"{FI} 15", r"$b = \num{67,3}$ y $c = \num{82,9}$", dict(b=67.3, c=82.9),
          dict(a=("48.4", 1, F_), alfa=("35.7", 1, F_), beta=("54.3", 1, F_)))
reg(47, f"{FI} 16",
    r"Cuando el ángulo de elevación del Sol es de $\num{28,4}^\circ$, la Torre Eiffel, en "
    r"París, proyecta una sombra horizontal de $1822$ pies. ¿Qué altura tiene la torre?",
    r"$h = 1822 \tg \num{28,4}^\circ \approx 985$ pies.",
    lambda: cerca(1822 * tan(rad(28.4)), 985, 0), tipo="contexto")
reg(48, f"{FI} 17",
    r"Sara vuela una cometa con las manos a $5$ pies del suelo. La cometa está a $200$ pies "
    r"de altura y la cuerda forma un ángulo de $\num{32,4}^\circ$ con la horizontal. ¿Cuántos "
    r"pies de cuerda está usando?",
    r"$L = \dfrac{200 - 5}{\sen \num{32,4}^\circ} \approx 364$ pies.",
    lambda: cerca(195 / sin(rad(32.4)), 364, 0), tipo="contexto", dificultad=2)
reg(49, f"{FI} 18",
    r"Un avión se aleja de un observador en tierra con rapidez constante y a una altura de "
    r"$15\,000$ pies. En cierto instante el observador mide un ángulo de elevación de "
    r"$44^\circ$ y, $15$ segundos después, de $31^\circ$. ¿A cuántas millas por hora vuela el "
    r"avión? ($1$ milla $= 5280$ pies.)",
    r"Recorre $\dfrac{15\,000}{\tg 31^\circ} - \dfrac{15\,000}{\tg 44^\circ} \approx 9431$ pies "
    r"en $15$ s, unos $\num{628,7}$ pies/s, es decir, $\approx 429$ millas por hora.",
    lambda: cerca((15000 / tan(rad(31)) - 15000 / tan(rad(44))) / 15 * 3600 / 5280, 429, 0),
    tipo="contexto", dificultad=3)
reg(50, f"{FI} 19",
    r"Desde la ventana de un edificio de oficinas se ve una torre de televisión a $600$ m de "
    r"distancia horizontal. El ángulo de elevación de la punta de la torre es $\num{19,6}^\circ$ "
    r"y el ángulo de depresión de su base es $\num{21,3}^\circ$. ¿Qué altura tiene la torre?",
    r"$h = 600\,(\tg \num{19,6}^\circ + \tg \num{21,3}^\circ) \approx 448$ m.",
    lambda: cerca(600 * (tan(rad(19.6)) + tan(rad(21.3))), 448, 0), tipo="contexto",
    dificultad=2)
reg(51, f"{FI} 20",
    r"En un almacén la distancia vertical del primer piso al segundo es de $28$ pies. La "
    r"escalera eléctrica tiene un alcance horizontal de $96$ pies y tarda $25$ segundos en "
    r"llevar a una persona de un piso al otro. ¿A qué velocidad se mueve la escalera?",
    r"La escalera mide $\sqrt{28^2 + 96^2} = 100$ pies; su velocidad es "
    r"$\dfrac{100}{25} = 4$ pies por segundo.",
    lambda: cerca(hypot(28, 96) / 25, 4, 6), tipo="contexto")
reg(52, f"{FI} 21",
    r"La Gran Pirámide tiene $480$ pies de altura y su base es un cuadrado de $760$ pies de "
    r"lado. Encuentra el ángulo de elevación de una de sus aristas laterales (el ángulo que "
    r"forma con la base).",
    r"El pie de la altura está en el centro de la base, a media diagonal $380\sqrt{2} \approx "
    r"\num{537,4}$ pies de cada vértice: $\theta = \arctg \dfrac{480}{380\sqrt{2}} \approx "
    r"\num{41,8}^\circ$.",
    lambda: cerca(grd(atan(480 / (hypot(760, 760) / 2))), 41.8, 1), tipo="contexto", dificultad=3)
reg(53, f"{FI} 22",
    r"Encuentra el ángulo entre una diagonal principal de un cubo y la diagonal de una de sus "
    r"caras que parte del mismo vértice.",
    r"Con arista $1$: la diagonal de la cara mide $\sqrt{2}$ y la arista perpendicular mide $1$, "
    r"así que $\theta = \arctg \dfrac{1}{\sqrt{2}} \approx \num{35,3}^\circ$.",
    lambda: cerca(grd(acos(sp.Matrix([1, 1, 0]).dot(sp.Matrix([1, 1, 1]))
                            / (sqrt(2) * sqrt(3)))), 35.3, 1), dificultad=3)
reg(54, f"{FI} 23",
    r"Un hexágono regular está inscrito en un círculo de radio $4$. Encuentra su perímetro $P$ "
    r"y su área $A$.",
    r"El hexágono se divide en $6$ triángulos equiláteros de lado $4$: $P = 24$ y "
    r"$A = 6 \cdot \dfrac{\sqrt{3}}{4} \cdot 4^2 = 24\sqrt{3} \approx \num{41,6}$.",
    lambda: (cerca(6 * 2 * 4 * sin(pi / 6), 24, 9),
             [cerca(float(sp.Polygon(*[sp.Point(4 * sp.cos(k * sp.pi / 3), 4 * sp.sin(k * sp.pi / 3))
                                        for k in range(6)]).area), float(24 * sp.sqrt(3)), 9)]),
    dificultad=2)
reg(55, f"{FI} 24",
    r"Un decágono regular está inscrito en un círculo de radio $12$. ¿Qué porcentaje del área "
    r"del círculo es el área del decágono?",
    r"$A = 10 \cdot \tfrac{1}{2} \cdot 12^2 \sen 36^\circ$; la razón es $\dfrac{5 \sen 36^\circ}"
    r"{\pi} \approx \num{0,935}$, es decir, cerca del $\num{93,5}\,\%$.",
    lambda: cerca(float(sp.Polygon(*[sp.Point(12 * sp.cos(k * sp.pi / 5), 12 * sp.sin(k * sp.pi / 5))
                                     for k in range(10)]).area) / (pi * 144) * 100, 93.5, 1),
    dificultad=2)


def estrella(n, R=1.0):
    """Área de la estrella regular de n puntas {n/2} inscrita en un círculo de radio R,
    como polígono de 2n vértices (puntas y cortes interiores de las diagonales)."""
    V = [(R * cos(pi / 2 + 2 * pi * k / n), R * sin(pi / 2 + 2 * pi * k / n)) for k in range(n)]

    def corte(p1, p2, p3, p4):
        (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p1, p2, p3, p4
        d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        a, b = x1 * y2 - y1 * x2, x3 * y4 - y3 * x4
        return ((a * (x3 - x4) - (x1 - x2) * b) / d, (a * (y3 - y4) - (y1 - y2) * b) / d)
    pts = []
    for k in range(n):
        pts.append(V[k])
        pts.append(corte(V[k], V[(k + 2) % n], V[(k + 1) % n], V[(k - 1) % n]))
    return abs(sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1]))) / 2


reg(56, f"{FI} 25",
    r"Encuentra el área de una estrella de David regular (estrella de $6$ puntas formada por "
    r"dos triángulos equiláteros) inscrita en un círculo de radio $1$.",
    r"Cada triángulo tiene lado $\sqrt{3}$ y área $\dfrac{3\sqrt{3}}{4}$; la estrella es un "
    r"triángulo más $3$ triangulitos equiláteros de lado $\dfrac{\sqrt{3}}{3}$: "
    r"$A = \dfrac{3\sqrt{3}}{4} + 3 \cdot \dfrac{\sqrt{3}}{12} = \sqrt{3} \approx \num{1,73}$.",
    lambda: cerca(estrella(6), sqrt(3), 9), dificultad=3)
reg(57, f"{FI} 26",
    r"Ingenioso: encuentra el área de la estrella regular de $5$ puntas (el pentagrama) "
    r"inscrita en un círculo de radio $1$.",
    r"Los cortes interiores están a distancia $r = \dfrac{\cos 72^\circ}{\cos 36^\circ}$ del "
    r"centro; la estrella se divide en $10$ triángulos de lados $1$ y $r$ con ángulo de "
    r"$36^\circ$: $A = 10 \cdot \tfrac{1}{2} \cdot r \sen 36^\circ \approx \num{1,12}$.",
    lambda: (cerca(estrella(5), 1.12, 2),
             cerca(5 * cos(rad(72)) / cos(rad(36)) * sin(rad(36)), estrella(5), 9)),
    dificultad=3)

# ---------- Prepárate para el ICFES del final del módulo ----------
triangulo(58, f"{FR} 1a", r"$\alpha = \num{47,1}^\circ$ y $c = \num{36,9}$",
          dict(alfa=47.1, c=36.9), dict(beta=("42.9", 1, T), a=("27.0", 1, F_), b=("25.1", 1, F_)),
          notas="En el módulo: «α = 47.1°» con punto decimal.")
triangulo(59, f"{FR} 1b", r"$a = 417$ y $c = 573$", dict(a=417, c=573),
          dict(b=("393.0", 1, F_), alfa=("46.7", 1, F_), beta=("43.3", 1, F_)))
reg(60, f"{FR} 2",
    r"A $10$ pies de una pared, el ángulo de elevación del borde superior de un mural, medido "
    r"desde el nivel de los ojos, es de $18^\circ$, y el ángulo de depresión del borde inferior "
    r"es de $10^\circ$. ¿Qué altura tiene el mural?",
    r"$h = 10 \tg 18^\circ + 10 \tg 10^\circ \approx \num{3,25} + \num{1,76} \approx "
    r"\num{5,0}$ pies.",
    lambda: cerca(10 * tan(rad(18)) + 10 * tan(rad(10)), 5.0, 1), tipo="contexto", dificultad=2)
