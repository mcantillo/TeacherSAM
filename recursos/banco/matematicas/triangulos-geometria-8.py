"""Banco de ejercicios — Geometría 8° — Trimestre I: congruencia, semejanza, Pitágoras en
contexto y teorema de Tales.
Escritos para la guía «La sombra de la pirámide»
(materias/geometria/octavo/guia-didactica/guia-periodo-I-triangulos.plan.md), solo donde el
banco no tenía nada verificado de 8° (regla «Reuse, don't multiply»): el módulo de Geometría
no trae ejercicios de congruencia, semejanza ni Tales, y pitagoras-8 no tiene problemas en
contexto. Los ángulos del triángulo reusan triangulos-8; recíproco y lado desconocido,
pitagoras-8. Nada duplicado.
DBA: matematicas-8-6 (congruencia y semejanza) y matematicas-8-7 (teoremas).
Datos de la pirámide de Keops: altura original ≈ 146 m, lado de la base ≈ 230 m
(ElGabry et al., Scientific Reports, 2026; Ministerio de Turismo y Antigüedades de Egipto).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/matematicas/triangulos-geometria-8.py
"""
from sympy import Line, N, Point, Rational, Triangle, cos, deg, rad, simplify, sin, sqrt

from ejercicios import ejercicio

FUENTE = "guía Geometría 8°, trimestre I (La sombra de la pirámide), escrito para la guía"
CON = dict(tema="congruencia de triángulos", grados=[8], dba=["matematicas-8-6"])
SEM = dict(tema="semejanza de triángulos", grados=[8], dba=["matematicas-8-6"])
PIT = dict(tema="teorema de Pitágoras", grados=[8], dba=["matematicas-8-7"])
TAL = dict(tema="teorema de Tales", grados=[8], dba=["matematicas-8-7"])


def lados(*pts):
    return sorted(s.length for s in Triangle(*map(Point, pts)).sides)


# ---------------------------------------------------------------- congruencia
@ejercicio(id="triangulos-geometria-8-001", tipo="conceptual", dificultad=1, fuente=FUENTE,
           enunciado=r"En cada caso se sabe lo que se indica sobre los triángulos $ABC$ y $DEF$. "
                     r"¿Qué criterio permite asegurar que son congruentes? Si ninguno, dilo. "
                     r"a) $AB = DE$, $BC = EF$, $CA = FD$. "
                     r"b) $AB = DE$, $\angle B = \angle E$, $BC = EF$. "
                     r"c) $\angle A = \angle D$, $AB = DE$, $\angle B = \angle E$. "
                     r"d) $\angle A = \angle D$, $\angle B = \angle E$, $\angle C = \angle F$.",
           respuesta=r"a) LLL. b) LAL (el ángulo $B$ está entre los dos lados). c) ALA (el lado "
                     r"$AB$ está entre los dos ángulos). d) Ninguno: con los tres ángulos iguales "
                     r"los triángulos son semejantes, pero pueden tener distinto tamaño (por "
                     r"ejemplo, lados $3$, $4$, $5$ y $6$, $8$, $10$).", **CON)
def _():
    # d) contraejemplo: mismos ángulos, lados distintos
    p1, p2 = ((0, 0), (4, 0), (0, 3)), ((0, 0), (8, 0), (0, 6))
    ang = lambda p: sorted(N(deg(v)) for v in Triangle(*map(Point, p)).angles.values())
    assert all(abs(u - v) < 1e-9 for u, v in zip(ang(p1), ang(p2)))
    assert lados(*p1) == [3, 4, 5] and lados(*p2) == [6, 8, 10]
    # b) LAL: AB = 2, BC = 3, ∠B = 50° fijan AC (arriba o abajo de AB, la misma longitud)
    B, A = Point(0, 0), Point(2, 0)
    for s in (1, -1):
        C = Point(3 * cos(rad(50)), s * 3 * sin(rad(50)))
        assert abs(N(A.distance(C) - sqrt(13 - 12 * cos(rad(50))))) < 1e-12
    # c) ALA: con AB = 1 y ángulos 40° y 60° en sus extremos, el tercer vértice es un único punto
    A0, B0 = Point(0, 0), Point(1, 0)
    r1 = Line(A0, A0 + Point(cos(rad(40)), sin(rad(40))))
    r2 = Line(B0, B0 + Point(-cos(rad(60)), sin(rad(60))))
    assert len(r1.intersection(r2)) == 1


@ejercicio(id="triangulos-geometria-8-002", tipo="contexto", dificultad=2, fuente=FUENTE,
           enunciado=r"Desde dos puntos $A$ y $B$ de la playa, separados $100$~m, se ve un barco "
                     r"$C$. El ángulo $\angle CAB$ mide $60^\circ$ y el ángulo $\angle CBA$ "
                     r"mide $70^\circ$. Dibuja en tu cuaderno, a escala $1$~cm $= 10$~m, un "
                     r"triángulo con esos datos. ¿Qué criterio asegura que tu dibujo es una copia "
                     r"fiel del triángulo real? Mide en el dibujo y estima la distancia de $A$ al "
                     r"barco.",
           respuesta=r"ALA: un lado ($AB$) y los dos ángulos de sus extremos determinan el "
                     r"triángulo. En el dibujo $AC$ mide unos $12{,}3$~cm, así que el barco está "
                     r"a unos $123$~m de $A$ (se aceptan medidas entre $120$ y $126$~m).", **CON)
def _():
    A, B = Point(0, 0), Point(100, 0)
    C = Line(A, A + Point(cos(rad(60)), sin(rad(60)))).intersection(
        Line(B, B + Point(-cos(rad(70)), sin(rad(70)))))[0]
    assert abs(N(A.distance(C)) - 122.67) < 0.01 and 120 <= N(A.distance(C)) <= 126


# ---------------------------------------------------------------- semejanza
@ejercicio(id="triangulos-geometria-8-003", tipo="conceptual", dificultad=1, fuente=FUENTE,
           enunciado=r"¿Son semejantes? Si lo son, di el criterio y la razón de semejanza. "
                     r"a) Un triángulo con ángulos de $40^\circ$ y $60^\circ$ y otro con ángulos "
                     r"de $60^\circ$ y $80^\circ$. "
                     r"b) Lados $4$, $6$, $8$ y lados $6$, $9$, $12$. "
                     r"c) Lados $3$, $4$, $5$ y lados $6$, $8$, $11$.",
           respuesta=r"a) Sí, por AA: el tercer ángulo del primero es $80^\circ$ y el del segundo "
                     r"$40^\circ$; los dos tienen $40^\circ$, $60^\circ$, $80^\circ$. "
                     r"b) Sí, por LLL: $\frac{6}{4} = \frac{9}{6} = \frac{12}{8} = 1{,}5$. "
                     r"c) No: $\frac{6}{3} = \frac{8}{4} = 2$ pero $\frac{11}{5} \ne 2$.", **SEM)
def _():
    assert sorted([40, 60, 180 - 40 - 60]) == sorted([60, 80, 180 - 60 - 80])
    assert Rational(6, 4) == Rational(9, 6) == Rational(12, 8) == Rational(3, 2)
    assert Rational(6, 3) == Rational(8, 4) != Rational(11, 5)


@ejercicio(id="triangulos-geometria-8-004", tipo="contexto", dificultad=2, fuente=FUENTE,
           enunciado=r"A cierta hora de la mañana, un palo de escoba de $1{,}5$~m puesto vertical "
                     r"en el patio proyecta una sombra de $2$~m. A la misma hora, la sombra de un "
                     r"edificio mide $24$~m. ¿Cuánto mide el edificio? Explica por qué los dos "
                     r"triángulos son semejantes.",
           respuesta=r"Los rayos del sol son paralelos, así que los dos triángulos tienen el mismo "
                     r"ángulo con el suelo, y ambos tienen un ángulo recto: son semejantes por AA. "
                     r"$\frac{h}{24} = \frac{1{,}5}{2}$, $h = 18$~m.", **SEM)
def _():
    # rayo con la pendiente del palo: el edificio de sombra 24 m tiene altura 24·(1,5/2)
    pend = Rational(3, 2) / 2
    rayo = Line(Point(24, 0), Point(24 - 2, Rational(3, 2)))
    assert rayo.slope == -pend and rayo.intersection(Line(Point(0, 0), Point(0, 1)))[0].y == 18


@ejercicio(id="triangulos-geometria-8-005", tipo="contexto", dificultad=2, fuente=FUENTE,
           enunciado=r"(La pirámide, a la manera de Plutarco.) La base de la gran pirámide es un "
                     r"cuadrado de unos $230$~m de lado, así que su centro está a $115$~m de cada "
                     r"lado. Un día, la sombra sobresale $104$~m desde el borde de la base. Un "
                     r"bastón de $2$~m clavado en la punta de la sombra da una sombra de $3$~m. "
                     r"¿Qué altura tiene la pirámide?",
           respuesta=r"La sombra de la pirámide, medida desde el centro de la base, es "
                     r"$115 + 104 = 219$~m. Por semejanza, $\frac{h}{219} = \frac{2}{3}$, así "
                     r"que $h = 146$~m.",
           notas="Ejemplo resuelto del tema 3 (el paso central del hilo). Datos redondeados "
                 "(146,6 m y 230,3 m en ElGabry et al., 2026). Supone el sol en el plano "
                 "perpendicular a un lado.", **SEM)
def _():
    assert Rational(2, 3) * (Rational(230, 2) + 104) == 146


# ---------------------------------------------------------------- Pitágoras en contexto
@ejercicio(id="triangulos-geometria-8-006", tipo="contexto", dificultad=2, fuente=FUENTE,
           enunciado=r"Para comprobar que la esquina de un muro es recta, un maestro de obra marca "
                     r"$60$~cm sobre un muro y $80$~cm sobre el otro, desde la esquina, y mide la "
                     r"distancia entre las dos marcas. a) ¿Cuánto debe medir si la esquina es "
                     r"recta? b) Si mide $98$~cm, ¿el ángulo es mayor o menor que $90^\circ$? "
                     r"Explica.",
           respuesta=r"a) $\sqrt{60^2 + 80^2} = 100$~cm. b) Menor: con el ángulo recto la "
                     r"distancia sería $100$~cm; si las marcas quedan más cerca ($98 < 100$), los "
                     r"muros están más cerrados, y el ángulo es agudo ($98^2 < 60^2 + 80^2$).",
           **PIT)
def _():
    assert sqrt(60**2 + 80**2) == 100
    # ley del coseno: 98² = 60² + 80² − 2·60·80·cos θ  ⇒  cos θ > 0  ⇒  θ < 90°
    assert Rational(60**2 + 80**2 - 98**2, 2 * 60 * 80) > 0


# ---------------------------------------------------------------- Tales
@ejercicio(id="triangulos-geometria-8-007", tipo="calculo", dificultad=1, fuente=FUENTE,
           enunciado=r"En el triángulo $ABC$, $DE \parallel BC$ ($D$ en $AB$, $E$ en $AC$). Si "
                     r"$AD = 4$, $DB = 6$ y $AE = 5$, halla $EC$ y $AC$.",
           respuesta=r"$\frac{4}{6} = \frac{5}{EC}$, $EC = 7{,}5$; $AC = 12{,}5$.", **TAL)
def _():
    # triángulo con AB = 10 y AC = 12,5; la paralela a BC por D (AD = 4) corta AC en AE = 5
    A, B = Point(0, 0), Point(10, 0)
    C = Point(Rational(25, 2) * cos(rad(50)), Rational(25, 2) * sin(rad(50)))
    D = Point(4, 0)
    E = Line(D, D + (C - B)).intersection(Line(A, C))[0]
    assert abs(N(A.distance(E)) - 5) < 1e-12 and abs(N(E.distance(C)) - 7.5) < 1e-12


@ejercicio(id="triangulos-geometria-8-008", tipo="argumentacion", dificultad=2, fuente=FUENTE,
           enunciado=r"En el triángulo $ABC$ se marcan $D$ en $AB$ y $E$ en $AC$. ¿Es $DE$ "
                     r"paralela a $BC$? Justifica con el recíproco del teorema de Tales. "
                     r"a) $AD = 3$, $DB = 4{,}5$, $AE = 4$, $EC = 6$. "
                     r"b) $AD = 3$, $DB = 4{,}5$, $AE = 4$, $EC = 5$.",
           respuesta=r"a) Sí: $\frac{3}{4{,}5} = \frac{4}{6} = \frac{2}{3}$, los segmentos son "
                     r"proporcionales. b) No: $\frac{3}{4{,}5} = \frac{2}{3}$ pero "
                     r"$\frac{4}{5} \ne \frac{2}{3}$.", **TAL)
def _():
    for ae, ec, paralela in ((4, 6, True), (4, 5, False)):
        A, B = Point(0, 0), Point(Rational(15, 2), 0)
        C = Point((ae + ec) * cos(rad(55)), (ae + ec) * sin(rad(55)))
        D = Point(3, 0)
        E = A + (C - A) * Rational(ae, ae + ec)
        u, v = E - D, C - B
        assert (simplify(u.x * v.y - u.y * v.x) == 0) == paralela
        assert (Rational(3) / Rational(9, 2) == Rational(ae, ec)) == paralela
