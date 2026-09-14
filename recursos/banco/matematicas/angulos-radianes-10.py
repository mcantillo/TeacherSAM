"""Banco de ejercicios — Trigonometría 10° — Ángulos en grados y radianes, longitud de arco,
velocidad angular.
Fuente: módulo de Matemáticas 10° de las Guías de Apoyo, Tema 2 («La visión dinámica de los
ángulos», Practica lo aprendido) y los problemas 3 y 4 del «Prepárate para el ICFES» final;
se lee en recursos/matematicas/Guías pedagógicas Matemáticas/markdown/10 - Modulo_Matematicas_Decimo.md
Las unidades inglesas del módulo (pies, pulgadas, millas) se conservan.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/angulos-radianes-10.py
"""
from math import cos as fcos
from math import pi as PI
from math import sqrt as fsqrt

import sympy as sp
from sympy import Rational as Q
from sympy import pi

from ejercicios import ejercicio, latex_es

PRE = "angulos-radianes-10"
FP = "módulo 10° (Guías de Apoyo), Tema 2, La visión dinámica de los ángulos — Practica lo aprendido"
FR = "módulo 10° (Guías de Apoyo), Resumen del capítulo — Prepárate para el ICFES"
COMUN = dict(tema="ángulos en grados y radianes", grados=[10], dba=["matematicas-10-4"])


def N(x):
    return r"\num{" + str(x).replace(".", ",") + "}"


def cerca(calc, mano, dec):
    calc = float(calc)
    assert abs(calc - mano) <= 0.5 * 10 ** -dec + 1e-9, f"calculado {calc}, a mano {mano}"


def igual(a, b):
    assert sp.simplify(a - b) == 0, f"{a} ≠ {b}"


def reg(n, fuente, enunciado, respuesta, check, tipo="calculo", dificultad=1, notas=None):
    meta = dict(id=f"{PRE}-{n:03d}", fuente=fuente, enunciado=enunciado, respuesta=respuesta,
                tipo=tipo, dificultad=dificultad, **COMUN)
    if notas:
        meta["notas"] = notas
    ejercicio(**meta)(check)


# ---------- 1. Grados → radianes (exacto) ----------
NOTA_77 = ("En el módulo: «(%s/77)°»; el 77 es un π dañado en el original (el texto plano "
           "también dice 77). Con π el resultado es exacto, como en el ejercicio 12c.")
filas1 = [("a", "120", 120, 2 * pi / 3), ("b", "150", 150, 5 * pi / 6), ("c", "315", 315, 7 * pi / 4),
          ("d", "450", 450, 5 * pi / 2), ("e", "160", 160, 8 * pi / 9),
          ("f", r"\left(\dfrac{150}{\pi}\right)", 150 / pi, Q(5, 6)),
          ("g", "225", 225, 5 * pi / 4), ("h", "210", 210, 7 * pi / 6), ("i", "300", 300, 5 * pi / 3),
          ("j", "-420", -420, -7 * pi / 3), ("k", "200", 200, 10 * pi / 9),
          ("l", "240", 240, 4 * pi / 3), ("m", "330", 330, 11 * pi / 6), ("n", "540", 540, 3 * pi),
          ("o", "-660", -660, -11 * pi / 3),
          ("p", r"\left(\dfrac{20}{\pi}\right)", 20 / pi, Q(1, 9))]
for i, (lit, tx, g, r) in enumerate(filas1):
    reg(1 + i, f"{FP} 1{lit}",
        r"Convierte $%s^\circ$ a radianes. Puedes dejar $\pi$ en la respuesta." % tx,
        r"$%s^\circ = %s$ rad." % (tx, latex_es(r)),
        lambda g=g, r=r: igual(g * pi / 180, r),
        notas=NOTA_77 % ("150" if lit == "f" else "20") if lit in "fp" else None)

# ---------- 2. Radianes → grados (a la décima) ----------
filas2 = [("a", r"\dfrac{14}{3}\pi", 14 * pi / 3, "840", True),
          ("b", r"\dfrac{5}{6}\pi", 5 * pi / 6, "150", True),
          ("c", r"-\dfrac{2}{3}\pi", -2 * pi / 3, "-120", True),
          ("d", r"-\dfrac{7}{4}\pi", -7 * pi / 4, "-315", True),
          ("e", r"3\pi", 3 * pi, "540", True), ("f", "3", 3, "171.9", False),
          ("g", r"\num{4,52}", Q(452, 100), "259.0", False),
          ("h", r"\dfrac{11}{4}", Q(11, 4), "157.6", False),
          ("i", r"\dfrac{1}{\pi}", 1 / pi, "18.2", False),
          ("j", r"\dfrac{4}{3\pi}", 4 / (3 * pi), "24.3", False)]
for i, (lit, tx, r, g, exacto) in enumerate(filas2):
    reg(17 + i, f"{FP} 2{lit}",
        r"Convierte $%s$ radianes a grados. Redondea a la décima de grado." % tx,
        r"$%s \text{ rad} %s %s^\circ$." % (tx, "=" if exacto else r"\approx", N(g)),
        lambda r=r, g=float(g), exacto=exacto: cerca(r * 180 / pi, g, 9 if exacto else 1))

# ---------- 3–5. Longitud de arco s = r t ----------
reg(27, f"{FP} 3a",
    r"Encuentra la medida en radianes del ángulo central de un círculo de $6$ pulgadas de radio "
    r"que abarca un arco de $12$ pulgadas.",
    r"$t = \dfrac{s}{r} = \dfrac{12}{6} = 2$ rad.", lambda: igual(Q(12, 6), 2))
reg(28, f"{FP} 3b",
    r"Encuentra la medida en radianes del ángulo central de un círculo de $6$ pulgadas de radio "
    r"que abarca un arco de $\num{18,84}$ pulgadas.",
    r"$t = \dfrac{\num{18,84}}{6} = \num{3,14}$ rad (casi $\pi$: media vuelta).",
    lambda: cerca(18.84 / 6, 3.14, 9))
for i, (lit, tx, t, s_tx, s) in enumerate([
        ("a", "2", 2, "6", 6), ("b", r"\num{5,5}", Q(11, 2), r"\num{16,5}", 16.5),
        ("c", r"\dfrac{\pi}{4}", pi / 4, r"\dfrac{3\pi}{4} \approx \num{2,36}", 2.36),
        ("d", r"\dfrac{5}{6}\pi", 5 * pi / 6, r"\dfrac{5\pi}{2} \approx \num{7,85}", 7.85)]):
    reg(29 + i, f"{FP} 4{lit}",
        r"Encuentra la longitud del arco que abarca, en un círculo de $3$ pies de radio, un "
        r"ángulo central de $%s$ radianes." % tx,
        r"$s = 3 \cdot %s = %s$ pies." % (tx, s_tx),
        lambda t=t, s=s: cerca(3 * t, s, 2))
reg(33, f"{FP} 5a",
    r"Encuentra el radio $r$ de un círculo en el que un ángulo central de $t = \num{2,8}$ "
    r"radianes abarca un arco de $s = \num{8,4}$ cm.",
    r"$r = \dfrac{s}{t} = \dfrac{\num{8,4}}{\num{2,8}} = 3$ cm.", lambda: igual(Q(84, 28), 3))
reg(34, f"{FP} 5b",
    r"Encuentra el radio $r$ de un círculo en el que un ángulo central de $t = 6$ radianes "
    r"abarca un arco de $s = 33$ pulgadas.",
    r"$r = \dfrac{33}{6} = \num{5,5}$ pulgadas.", lambda: igual(Q(33, 6), Q(11, 2)))
reg(35, f"{FP} 6",
    r"¿Cuántos radianes recorre el minutero de un reloj en $1$ hora? ¿Y el horario en $1$ hora? "
    r"¿Y el minutero en $5$ horas?",
    r"Minutero en $1$ h: $2\pi$ rad; horario en $1$ h: $\dfrac{\pi}{6}$ rad; minutero en $5$ h: "
    r"$10\pi$ rad. (Giran en el sentido de las manecillas del reloj, así que con la convención "
    r"de signos son $-2\pi$, $-\frac{\pi}{6}$ y $-10\pi$.)",
    lambda: (igual(2 * pi * 1, 2 * pi), igual(2 * pi / 12, pi / 6), igual(5 * 2 * pi, 10 * pi)),
    tipo="contexto")


# ---------- 7. Cuadrante de P después de recorrer una distancia ----------
def cuadrante(t):
    r = sp.Mod(t, 2 * pi)
    q = sp.floor(r / (pi / 2))
    assert sp.simplify(r - q * pi / 2) != 0, "cae sobre un eje"
    return int(q) + 1


ROM = {1: "I", 2: "II", 3: "III", 4: "IV"}
filas7 = [("a", "3", 3, 2), ("b", r"\num{4,8}", Q(48, 10), 4), ("c", "100", 100, 4),
          ("d", r"\num{4,7}", Q(47, 10), 3), ("e", r"\num{3,2}", Q(32, 10), 3),
          ("f", r"\left(\dfrac{5\pi}{2} + 1\right)", 5 * pi / 2 + 1, 2),
          ("g", r"\left(\dfrac{9\pi}{2} - 1\right)", 9 * pi / 2 - 1, 1), ("h", "200", 200, 4)]
for i, (lit, tx, t, q) in enumerate(filas7):
    reg(36 + i, f"{FP} 7{lit}",
        r"Un punto $P$ se mueve sobre el círculo unitario en sentido contrario a las manecillas "
        r"del reloj, empezando en $(1, 0)$. ¿En qué cuadrante está $P$ cuando ha recorrido "
        r"$%s$ unidades?" % tx,
        r"En el cuadrante %s." % ROM[q], lambda t=t, q=q: igual(cuadrante(t), q),
        dificultad=1 if lit in "abde" else 2)

# ---------- 8–27. Velocidad angular y aplicaciones ----------
reg(44, f"{FP} 8",
    r"Sandra pedalea su triciclo de modo que la rueda delantera (radio $8$ pulgadas) gira a "
    r"$4$ revoluciones por segundo. ¿A cuántos pies por segundo avanza? (Sugerencia: $4$ "
    r"revoluciones por segundo son $8\pi$ radianes por segundo.)",
    r"$v = r\omega = 8 \cdot 8\pi = 64\pi$ pulgadas/s $= \dfrac{16\pi}{3} \approx \num{16,8}$ "
    r"pies/s.",
    lambda: (igual(Q(8, 12) * 4 * 2 * pi, 16 * pi / 3), cerca(16 * PI / 3, 16.8, 1)),
    tipo="contexto", notas="En el módulo: «radiantes»; se escribe radianes.")
reg(45, f"{FP} 9",
    r"La llanta de un automóvil tiene un diámetro exterior de $\num{2,5}$ pies. ¿A cuántas "
    r"revoluciones por minuto gira cuando el automóvil va a $60$ millas por hora? ($1$ milla "
    r"$= 5280$ pies.)",
    r"$60$ mi/h $= 88$ pies/s; $\omega = \dfrac{88}{\num{1,25}} = \num{70,4}$ rad/s, que son "
    r"$\dfrac{\num{70,4} \cdot 60}{2\pi} \approx 672$ revoluciones por minuto.",
    lambda: cerca(60 * 5280 / 3600 / 1.25 * 60 / (2 * PI), 672, 0), tipo="contexto", dificultad=2)
reg(46, f"{FP} 10",
    r"Una mosca muerta está pegada a una banda que pasa por dos poleas de $6$ y $8$ pulgadas de "
    r"radio. Si la banda no resbala, ¿qué tan rápido se mueve la mosca cuando la polea mayor gira "
    r"a $20$ revoluciones por minuto?",
    r"$v = 8 \cdot 2\pi \cdot 20 = 320\pi \approx 1005$ pulgadas por minuto ($\approx "
    r"\num{83,8}$ pies por minuto).",
    lambda: (cerca(8 * 2 * PI * 20, 1005, 0), cerca(8 * 2 * PI * 20 / 12, 83.8, 1)),
    tipo="contexto", notas="En el módulo: «¿qué tan rápido se mueve la rosca?»; es la mosca.")
reg(47, f"{FP} 11",
    r"En el problema de la banda (poleas de $6$ y $8$ pulgadas de radio, la mayor a $20$ "
    r"revoluciones por minuto), ¿a cuántas revoluciones por minuto gira la polea pequeña?",
    r"La banda lleva la misma rapidez: $6 \cdot 2\pi \cdot n = 320\pi$, así que "
    r"$n = \dfrac{80}{3} \approx \num{26,7}$ revoluciones por minuto.",
    lambda: igual(320 * pi / (6 * 2 * pi), Q(80, 3)), tipo="contexto")
for i, (lit, tx, r, rtx) in enumerate([("a", r"-1440^\circ", -1440 * pi / 180, r"-8\pi"),
                                       ("b", r"23 \text{ revoluciones}", 23 * 2 * pi, r"46\pi"),
                                       ("c", r"\left(\dfrac{60}{\pi}\right)^\circ",
                                        (60 / pi) * pi / 180, r"\dfrac{1}{3}")]):
    reg(48 + i, f"{FP} 12{lit}", r"Convierte a radianes: $%s$." % tx, r"$%s$ rad." % rtx,
        lambda r=r, rtx=rtx: igual(r, sp.sympify({r"-8\pi": "-8*pi", r"46\pi": "46*pi",
                                                   r"\dfrac{1}{3}": "1/3"}[rtx])))
reg(51, f"{FP} 13a", r"Convierte a grados: $\dfrac{23\pi}{36}$ radianes.",
    r"$\dfrac{23\pi}{36} \cdot \dfrac{180^\circ}{\pi} = 115^\circ$.",
    lambda: igual(23 * pi / 36 * 180 / pi, 115),
    notas="En el módulo la fórmula es ilegible («[ecuación ilegible]»); se toma del texto "
          "alternativo «23 pi sobre 36».")
reg(52, f"{FP} 13b", r"Convierte a grados: $-\num{4,63}$ radianes (a la décima).",
    r"$-\num{4,63} \cdot \dfrac{180^\circ}{\pi} \approx -\num{265,3}^\circ$.",
    lambda: cerca(-4.63 * 180 / PI, -265.3, 1))
reg(53, f"{FP} 13c", r"Convierte a grados: $\dfrac{3}{2\pi}$ radianes (a la décima).",
    r"$\dfrac{3}{2\pi} \cdot \dfrac{180^\circ}{\pi} = \dfrac{270^\circ}{\pi^2} \approx "
    r"\num{27,4}^\circ$.",
    lambda: (igual(3 / (2 * pi) * 180 / pi, 270 / pi**2), cerca(270 / PI**2, 27.4, 1)))
for i, (lit, tx, t, stx, s, dec) in enumerate([
        ("a", "6 radianes", 6, r"\num{25,5}", 25.5, 6),
        ("b", r"\left(\dfrac{18}{13\pi}\right)^\circ", Q(18, 13) / pi * pi / 180,
         r"\dfrac{\num{4,25}}{130} \approx \num{0,0327}", 0.0327, 4),
        ("c", r"\dfrac{17\pi}{6} \text{ radianes}", 17 * pi / 6,
         r"\dfrac{\num{72,25}\pi}{6} \approx \num{37,8}", 37.8, 1)]):
    reg(54 + i, f"{FP} 14{lit}",
        r"Encuentra la longitud del arco que abarca, en un círculo de radio $\num{4,25}$ cm, un "
        r"ángulo central de $%s$." % tx,
        r"$s = %s$ cm." % stx, lambda t=t, s=s, dec=dec: cerca(Q(425, 100) * t, s, dec),
        notas=("El ángulo «(18/13π)°» es muy pequeño (1/130 rad); se conserva como está en el "
               "módulo. Posible error del original: la docente decide si lo usa.")
        if lit == "b" else None)
reg(57, f"{FP} 15",
    r"La rueda delantera del triciclo de Toño tiene $20$ pulgadas de diámetro. ¿Qué distancia "
    r"recorre si la rueda da $60$ vueltas?",
    r"$d = 60 \cdot 20\pi = 1200\pi \approx 3770$ pulgadas ($\approx 314$ pies).",
    lambda: (cerca(60 * PI * 20, 3770, 0), cerca(60 * PI * 20 / 12, 314, 0)), tipo="contexto")
reg(58, f"{FP} 16",
    r"El piñón del pedal de la bicicleta de María tiene $12$ cm de radio, el de la rueda trasera "
    r"$3$ cm y las ruedas $40$ cm de radio. ¿Qué distancia recorre María si da $30$ vueltas "
    r"completas al pedal?",
    r"La cadena mueve la misma longitud en los dos piñones: la rueda trasera da "
    r"$30 \cdot \dfrac{12}{3} = 120$ vueltas y recorre $120 \cdot 2\pi \cdot 40 = 9600\pi "
    r"\approx 30\,159$ cm $\approx \num{301,6}$ m.",
    lambda: cerca(30 * 2 * PI * 12 / (2 * PI * 3) * 2 * PI * 40 / 100, 301.6, 1),
    tipo="contexto", dificultad=2)
reg(59, f"{FP} 17",
    r"Una banda se mueve a $60$ pies por segundo y hace girar una polea a $900$ revoluciones "
    r"por minuto. Encuentra el radio de la polea.",
    r"$900$ rev/min $= 30\pi$ rad/s; $r = \dfrac{v}{\omega} = \dfrac{60}{30\pi} = \dfrac{2}{\pi}"
    r" \approx \num{0,637}$ pies ($\approx \num{7,64}$ pulgadas).",
    lambda: (igual(60 / (Q(900, 60) * 2 * pi), 2 / pi), cerca(24 / PI, 7.64, 2)),
    tipo="contexto", dificultad=2)
reg(60, f"{FP} 18",
    r"Supón que la Tierra es una esfera de $3960$ millas de radio. ¿A qué rapidez (en millas por "
    r"hora) se mueve un punto del ecuador por la rotación de la Tierra?",
    r"$v = \dfrac{2\pi \cdot 3960}{24} = 330\pi \approx 1037$ millas por hora.",
    lambda: (igual(2 * pi * 3960 / 24, 330 * pi), cerca(330 * PI, 1037, 0)), tipo="contexto")
reg(61, f"{FP} 19",
    r"La órbita de la Tierra alrededor del Sol es casi un círculo de $93$ millones de millas de "
    r"radio y una vuelta tarda $\num{365,25}$ días. ¿Cuál es la rapidez aproximada de la Tierra "
    r"en su órbita, en millas por hora?",
    r"$v = \dfrac{2\pi \cdot 93\,000\,000}{\num{365,25} \cdot 24} \approx 66\,700$ millas por "
    r"hora.",
    lambda: cerca(2 * PI * 93e6 / (365.25 * 24) / 100, 667, 0), tipo="contexto")
reg(62, f"{FP} 20",
    r"Visto desde la Tierra, a $93$ millones de millas, el Sol abarca un ángulo de "
    r"$\num{0,0093}$ radianes. Encuentra el diámetro del Sol.",
    r"$D \approx s = r t = 93\,000\,000 \cdot \num{0,0093} = 864\,900$ millas.",
    lambda: cerca(93e6 * 0.0093, 864900, 3), tipo="contexto")
reg(63, f"{FP} 21",
    r"Una milla náutica es la longitud de $1$ minuto ($\frac{1}{60}$ de grado) de arco del "
    r"ecuador. ¿Cuántas millas hay en una milla náutica? (Radio de la Tierra: $3960$ millas.)",
    r"$s = 3960 \cdot \dfrac{\pi}{180 \cdot 60} = \dfrac{11\pi}{30} \approx \num{1,15}$ millas.",
    lambda: (igual(3960 * pi / 180 / 60, 11 * pi / 30), cerca(11 * PI / 30, 1.15, 2)),
    tipo="contexto", notas="Se añade al enunciado el radio de la Tierra (3960 millas, dato del "
                           "problema 18).")
reg(64, f"{FP} 22",
    r"Una persona vive a $45^\circ$ de latitud norte. ¿Cuánto tarda en volar hasta el Polo "
    r"Norte a $600$ millas por hora, siguiendo un meridiano? (La Tierra es una esfera de "
    r"$3960$ millas de radio.)",
    r"Debe recorrer $3960 \cdot \dfrac{\pi}{4} = 990\pi \approx 3110$ millas: "
    r"$t = \dfrac{990\pi}{600} \approx \num{5,18}$ h (unas $5$ h $11$ min).",
    lambda: cerca(3960 * PI / 4 / 600, 5.18, 2), tipo="contexto", dificultad=2,
    notas="En el módulo: «Uno de los autores (Dale Varberg) vive…»; se generaliza a «una persona».")
reg(65, f"{FP} 23",
    r"Nueva York está a $\num{40,5}^\circ$ de latitud norte. ¿A qué distancia está del ecuador, "
    r"medida sobre su meridiano? (Radio de la Tierra: $3960$ millas.)",
    r"$s = 3960 \cdot \num{40,5} \cdot \dfrac{\pi}{180} \approx 2799$ millas (unas $2800$).",
    lambda: cerca(3960 * 40.5 * PI / 180, 2799, 0), tipo="contexto",
    notas="En el módulo: «40.5°» y «¿A distancia está…?»; se corrige la redacción y se añade el "
          "radio de la Tierra.")
reg(66, f"{FP} 24",
    r"Oslo (Noruega) y San Petersburgo (Rusia) están a $60^\circ$ de latitud norte; Oslo está "
    r"a $6^\circ$ este del meridiano de Greenwich y San Petersburgo a $30^\circ$ este. ¿Qué "
    r"distancia las separa a lo largo del paralelo de $60^\circ$? (Radio de la Tierra: $3960$ "
    r"millas.)",
    r"El paralelo de $60^\circ$ tiene radio $3960 \cos 60^\circ = 1980$ millas; la diferencia "
    r"de longitud es $24^\circ = \dfrac{2\pi}{15}$: $s = 1980 \cdot \dfrac{2\pi}{15} = 264\pi "
    r"\approx 829$ millas.",
    lambda: (igual(3960 * sp.cos(pi / 3) * 24 * pi / 180, 264 * pi), cerca(264 * PI, 829, 0)),
    tipo="contexto", dificultad=3,
    notas="En el módulo: «Leningrado» (hoy San Petersburgo). Se añade el radio de la Tierra.")
reg(67, f"{FP} 25",
    r"El minutero y el horario de un reloj miden $6$ pulgadas y llegan hasta el borde de la "
    r"carátula. Encuentra el área de la región entre las dos manecillas a las $5{:}40$ (el "
    r"sector menor).",
    r"A las $5{:}40$ el minutero está a $240^\circ$ de las $12$ y el horario a "
    r"$150^\circ + 20^\circ = 170^\circ$; el ángulo es $70^\circ = \dfrac{7\pi}{18}$ y "
    r"$A = \tfrac{1}{2} \cdot 6^2 \cdot \dfrac{7\pi}{18} = 7\pi \approx 22$ pulgadas cuadradas.",
    lambda: igual(Q(1, 2) * 36 * ((40 * 6) - (5 * 30 + Q(40, 60) * 30)) * pi / 180, 7 * pi),
    tipo="contexto", dificultad=3)
R, L, t_, x_ = sp.symbols("R L t x", positive=True)
reg(68, f"{FP} 26",
    r"Un cono tiene base de radio $R$ y generatriz (altura inclinada) $L$. Encuentra la fórmula "
    r"de su superficie lateral. Sugerencia: imagina que el cono es de papel, córtalo a lo largo "
    r"de una generatriz y extiéndelo sobre una mesa.",
    r"Al extenderlo queda un sector circular de radio $L$ cuyo arco mide $2\pi R$; su ángulo es "
    r"$t = \dfrac{2\pi R}{L}$ y su área $A = \tfrac{1}{2}L^2 t = \pi R L$.",
    lambda: igual(Q(1, 2) * L**2 * (2 * pi * R / L), pi * R * L), tipo="argumentacion",
    dificultad=3)
reg(69, f"{FP} 27",
    r"Dos círculos tienen radio $r$ y el centro de cada uno está sobre el borde del otro. "
    r"Encuentra el área de la parte común de los dos círculos.",
    r"La cuerda común subtiende en cada centro un ángulo de $\dfrac{2\pi}{3}$; la región común "
    r"son dos segmentos circulares: $A = 2\left(\tfrac{1}{2}r^2 \cdot \tfrac{2\pi}{3} - "
    r"\tfrac{1}{2}r^2 \sen \tfrac{2\pi}{3}\right) = r^2\left(\dfrac{2\pi}{3} - "
    r"\dfrac{\sqrt{3}}{2}\right) \approx \num{1,23}\,r^2$.",
    lambda: igual(2 * sp.integrate(2 * sp.sqrt(1 - x_**2), (x_, Q(1, 2), 1)),
                  2 * pi / 3 - sp.sqrt(3) / 2),
    dificultad=3)

# ---------- Prepárate para el ICFES del final del módulo ----------
reg(70, f"{FR} 3", r"Convierte $33^\circ$ a radianes y $\dfrac{9\pi}{4}$ radianes a grados.",
    r"$33^\circ = \dfrac{11\pi}{60} \approx \num{0,576}$ rad; $\dfrac{9\pi}{4}$ rad $= 405^\circ$.",
    lambda: (igual(33 * pi / 180, 11 * pi / 60), igual(9 * pi / 4 * 180 / pi, 405)))
reg(71, f"{FR} 4",
    r"¿Qué distancia avanza una rueda de $30$ cm de radio si da $100$ vueltas?",
    r"$d = 100 \cdot 2\pi \cdot 30 = 6000\pi \approx 18\,850$ cm $\approx \num{188,5}$ m.",
    lambda: cerca(100 * 2 * PI * 30 / 100, 188.5, 1), tipo="contexto")
