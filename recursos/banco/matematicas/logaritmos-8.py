"""Banco de ejercicios — Matemáticas 8° — Logaritmación (relación entre potencia, raíz y
logaritmo).
Fuente: módulo de Matemáticas 8° de las Guías de Apoyo (Adriana Quintero Palomino), Tema 1;
se lee en recursos/matematicas/Guías pedagógicas Matemáticas/markdown/08 - Modulo_Matematicas_Octavo.md
DBA: matematicas-8-9 (operar con formas simbólicas y encontrar valores desconocidos en
ecuaciones numéricas). Ningún DBA de 8° nombra los logaritmos; queda a criterio de la docente.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/logaritmos-8.py
"""
import sympy as sp
from sympy import Rational, log, root

from ejercicios import ejercicio

FUENTE = "módulo 8° (Quintero Palomino), Tema 1, Logaritmación — Practica lo aprendido"
COMUN = dict(tema="logaritmos", grados=[8], dba=["matematicas-8-9"], tipo="calculo")


def item(n, literal, enunciado, respuesta, comprobar, dificultad=1):
    def envuelta():
        assert bool(comprobar()), "la comprobación dio falso"
    envuelta.__wrapped__ = comprobar          # la huella usa el código de la comprobación
    ejercicio(id=f"logaritmos-8-{n:03d}", fuente=f"{FUENTE} {literal}", enunciado=enunciado,
              respuesta=respuesta, dificultad=dificultad, **COMUN)(envuelta)


def es_log(base, arg, exp):
    """log_base(arg) = exp  ⇔  base^exp = arg (con base > 0, base ≠ 1, arg > 0)."""
    base, arg = sp.nsimplify(base), sp.nsimplify(arg)
    assert base > 0 and base != 1 and arg > 0
    return sp.simplify(base**exp - arg) == 0 and sp.simplify(log(arg, base) - exp) == 0


A_LOG = "Expresa en forma de logaritmo: ${}$."
for n, lit, tx, base, arg, exp, rt, dif in [
    (1, "1a", r"5^{-1} = \dfrac{1}{5}", 5, Rational(1, 5), -1, r"\log_5 \dfrac{1}{5} = -1", 1),
    (2, "1b", r"\left(\dfrac{3}{2}\right)^{-2} = \dfrac{4}{9}", Rational(3, 2), Rational(4, 9), -2,
     r"\log_{\frac{3}{2}} \dfrac{4}{9} = -2", 2),
    (3, "1c", r"6^0 = 1", 6, 1, 0, r"\log_6 1 = 0", 1),
    (4, "1d", r"3^4 = 81", 3, 81, 4, r"\log_3 81 = 4", 1),
    (5, "1e", r"\left(\dfrac{2}{3}\right)^3 = \dfrac{8}{27}", Rational(2, 3), Rational(8, 27), 3,
     r"\log_{\frac{2}{3}} \dfrac{8}{27} = 3", 2),
]:
    item(n, lit, A_LOG.format(tx), f"${rt}$.",
         lambda base=base, arg=arg, exp=exp: es_log(base, arg, exp), dificultad=dif)

RAIZ = "Expresa en forma de logaritmo: ${}$."
for n, lit, tx, rad, ind, val, rt, dif in [
    (6, "2a", r"\sqrt[3]{64} = 4", 64, 3, 4, r"\log_4 64 = 3", 1),
    (7, "2b", r"\sqrt[5]{32} = 2", 32, 5, 2, r"\log_2 32 = 5", 1),
    (8, "2c", r"\sqrt[3]{\dfrac{1}{8}} = \dfrac{1}{2}", Rational(1, 8), 3, Rational(1, 2),
     r"\log_{\frac{1}{2}} \dfrac{1}{8} = 3", 2),
    (9, "2d", r"\sqrt{100} = 10", 100, 2, 10, r"\log_{10} 100 = 2", 1),
    (10, "2e", r"\sqrt[7]{128} = 2", 128, 7, 2, r"\log_2 128 = 7", 1),
]:
    porque = (f"{sp.latex(val)}^{ind} = {sp.latex(rad)}".replace(r"\frac", r"\dfrac")
              .replace(r"\dfrac{1}{2}^", r"\left(\dfrac{1}{2}\right)^"))
    item(n, lit, RAIZ.format(tx), f"${rt}$ (porque ${porque}$).",
         lambda rad=rad, ind=ind, val=val: root(rad, ind) == val and es_log(val, rad, ind),
         dificultad=dif)

POT = "Expresa en forma de potencia: ${}$."
for n, lit, tx, base, arg, exp, rt, dif in [
    (11, "3a", r"\log_3 27 = 3", 3, 27, 3, "3^3 = 27", 1),
    (12, "3b", r"\log_4 16 = 2", 4, 16, 2, "4^2 = 16", 1),
    (13, "3c", r"\log_{16} 2 = \dfrac{1}{4}", 16, 2, Rational(1, 4),
     r"16^{\frac{1}{4}} = 2$, es decir, $\sqrt[4]{16} = 2", 2),
    (14, "3d", r"\log_3 \dfrac{1}{27} = -3", 3, Rational(1, 27), -3, r"3^{-3} = \dfrac{1}{27}", 1),
    (15, "3e", r"\log_{10} \num{0,001} = -3", 10, Rational(1, 1000), -3,
     r"10^{-3} = \num{0,001}", 1),
]:
    item(n, lit, POT.format(tx), f"${rt}$.",
         lambda base=base, arg=arg, exp=exp: es_log(base, arg, exp), dificultad=dif)

CALC = ("Con la calculadora, encuentra una aproximación racional con cuatro cifras decimales "
        "de ${}$.")
for n, lit, tx, base, arg, rt, aprox in [
    (16, "4a", r"\log_3 25", 3, 25, r"\log_3 25 = \dfrac{\log 25}{\log 3} \approx \num{2,9299}",
     "2.9299"),
    (17, "4b", r"\log_5 700", 5, 700, r"\log_5 700 = \dfrac{\log 700}{\log 5} \approx \num{4,0704}",
     "4.0704"),
    (18, "4c", r"\log_{10} 1500", 10, 1500, r"\log 1500 \approx \num{3,1761}", "3.1761"),
]:
    item(n, lit, CALC.format(tx), f"${rt}$.",
         lambda base=base, arg=arg, aprox=aprox:
         abs(sp.N(log(arg, base), 30) - sp.Rational(aprox)) < sp.Rational(1, 20000), dificultad=2)
