"""Banco de ejercicios — Geometría 8° — Longitudes, áreas y volúmenes con números reales.
Fuente: módulo de Matemáticas 8° de las Guías de Apoyo (Adriana Quintero Palomino), Tema 1;
se lee en recursos/matematicas/Guías pedagógicas Matemáticas/markdown/08 - Modulo_Matematicas_Octavo.md
Solo los literales de pensamiento espacial y métrico (Pitágoras, área y volumen); el resto del
módulo 8° es de Álgebra. No se incluyeron: Sustracción — Practica lo aprendido 2a–b (perímetro
de un cuadrilátero con lados √5, √3 y π: es operación con reales, no usa relaciones geométricas)
ni Tema 2, Valor numérico 14a–e (evaluar fórmulas de perímetro y área: valor numérico de
expresiones algebraicas) — quedan para Álgebra.
En el banco no había ejercicios de este tema: nada duplicado.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/medidas-con-radicales-8.py
"""
from sympy import N, Point, Point3D, Triangle, sqrt
from sympy.physics import units as u

from ejercicios import ejercicio

REC = "módulo 8° (Quintero Palomino), Tema 1: Operaciones con números reales"
COMUN = dict(tema="longitudes, áreas y volúmenes con radicales", grados=[8])


@ejercicio(id="medidas-con-radicales-8-001", tipo="calculo", dificultad=2,
           dba=["matematicas-8-7"], fuente=f"{REC}, Sustracción — Practica lo aprendido 3",
           enunciado=r"Encuentra el perímetro de un triángulo rectángulo isósceles cuyos catetos "
                     r"miden $5$~cm.",
           respuesta=r"La hipotenusa mide $\sqrt{5^2 + 5^2} = \sqrt{50} = 5\sqrt{2}$~cm, así que "
                     r"el perímetro es $10 + 5\sqrt{2} \approx \num{17,07}$~cm.",
           notas="En el módulo: «cuyo cateto mide 5 cm»; en un triángulo rectángulo isósceles los "
                 "dos catetos son iguales.", **COMUN)
def _():
    t = Triangle(Point(0, 0), Point(5, 0), Point(0, 5))
    assert t.is_right() and t.perimeter == 10 + 5 * sqrt(2)
    assert abs(N(t.perimeter) - 17.07) < 0.005


@ejercicio(id="medidas-con-radicales-8-002", tipo="calculo", dificultad=2,
           dba=["matematicas-8-7"], fuente=f"{REC}, Sustracción — Practica lo aprendido 4",
           enunciado=r"En el triángulo isósceles $ABC$, la base $AB$ mide $10$~cm, $BC = CA$ y la "
                     r"altura $CH$ mide $8$~cm ($CH$ es perpendicular a $AB$ y $AH = HB$). "
                     r"Encuentra su perímetro.",
           respuesta=r"$AH = 5$~cm, así que $CA = CB = \sqrt{5^2 + 8^2} = \sqrt{89}$~cm y el "
                     r"perímetro es $10 + 2\sqrt{89} \approx \num{28,87}$~cm.",
           notas="La descripción de la imagen del módulo dice «triángulo equilátero»; con estos "
                 "datos es isósceles (√89 ≈ 9,43 cm ≠ 10 cm). Se dejó la figura descrita en el "
                 "enunciado.", **COMUN)
def _():
    t = Triangle(Point(0, 0), Point(10, 0), Point(5, 8))
    lados = sorted(set(s.length for s in t.sides), key=N)
    assert lados == [sqrt(89), 10]                        # isósceles, no equilátero
    assert t.perimeter == 10 + 2 * sqrt(89)
    assert abs(N(t.perimeter) - 28.87) < 0.005


CUBO = (r"Un cubo tiene la cara frontal $ABCD$ y la base $ABFE$, y cada arista mide $5$~cm "
        r"($E$ es el vértice de la base opuesto a $B$ y $C$ está sobre $B$). ")
CUBO_FUENTE = f"{REC}, Multiplicación y división — Practica lo aprendido 3"
A, B, F, E = Point3D(0, 0, 0), Point3D(5, 0, 0), Point3D(5, 5, 0), Point3D(0, 5, 0)
C = Point3D(5, 0, 5)


@ejercicio(id="medidas-con-radicales-8-003", tipo="calculo", dificultad=2,
           dba=["matematicas-8-7"], fuente=f"{CUBO_FUENTE}a",
           enunciado=CUBO + r"Calcula la longitud de la diagonal $EB$ de la base.",
           respuesta=r"$EB = \sqrt{5^2 + 5^2} = 5\sqrt{2} \approx \num{7,07}$~cm.", **COMUN)
def _():
    assert E.distance(B) == 5 * sqrt(2) and abs(N(5 * sqrt(2)) - 7.07) < 0.005


@ejercicio(id="medidas-con-radicales-8-004", tipo="calculo", dificultad=3,
           dba=["matematicas-8-7", "matematicas-8-4"], fuente=f"{CUBO_FUENTE}b",
           enunciado=CUBO + r"Calcula la longitud de la diagonal $EC$ del cubo.",
           respuesta=r"El triángulo $EBC$ es rectángulo en $B$: $EC = \sqrt{(5\sqrt{2})^2 + 5^2} "
                     r"= \sqrt{75} = 5\sqrt{3} \approx \num{8,66}$~cm.", **COMUN)
def _():
    assert (B - E).dot(C - B) == 0                       # ángulo recto en B
    assert E.distance(C) == 5 * sqrt(3) and abs(N(5 * sqrt(3)) - 8.66) < 0.005


@ejercicio(id="medidas-con-radicales-8-005", tipo="calculo", dificultad=1,
           dba=["matematicas-8-4"], fuente=f"{CUBO_FUENTE}c",
           enunciado=CUBO + r"Calcula la superficie total del cubo.",
           respuesta=r"$6 \cdot 5^2 = 150$~cm$^2$.", **COMUN)
def _():
    arista = 5 * u.centimeter
    assert u.convert_to(6 * arista**2, u.centimeter**2) == 150 * u.centimeter**2


@ejercicio(id="medidas-con-radicales-8-006", tipo="calculo", dificultad=1,
           dba=["matematicas-8-4", "matematicas-8-5"], fuente=f"{CUBO_FUENTE}d",
           enunciado=CUBO + r"Calcula el volumen del cubo.",
           respuesta=r"$5^3 = 125$~cm$^3$ (es decir, $\num{0,125}$~L).", **COMUN)
def _():
    arista = 5 * u.centimeter
    assert u.convert_to(arista**3, u.centimeter**3) == 125 * u.centimeter**3
    assert u.convert_to(arista**3, u.liter) == u.liter / 8
