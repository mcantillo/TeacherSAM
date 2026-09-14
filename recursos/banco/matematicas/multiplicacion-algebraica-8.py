"""Banco de ejercicios — Álgebra 8° — Multiplicación algebraica.
Fuente: Baldor, Álgebra (1983), transcripción parcial en recursos/algebra/baldor/baldor.tex
(Multiplicación, pp. 65-76): monomios (ejercicios 35-38), polinomio por monomio (39-40),
polinomio por polinomio (41-44), producto continuado, multiplicación combinada con suma y
resta (47) y supresión de signos de agrupación con productos indicados. La página y el número
de ejercicio son los que cita la transcripción (ver «dudas» en las notas de las series
afectadas). La transcripción usa punto decimal: aquí, coma decimal.
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/multiplicacion-algebraica-8.py
"""
import re

from sympy import Add, expand, powsimp

from ejercicios import ejercicio, expresion

BALDOR = "Baldor, Álgebra (1983)"
DBA = ["matematicas-8-3", "matematicas-8-9"]


def ltx(s):
    """SymPy de una expresión escrita en LaTeX sencillo (letras sueltas = variables)."""
    s = s.replace(r"\left", "").replace(r"\right", "").replace("{,}", ".")
    s = s.replace(r"\lbrack", "(").replace(r"\rbrack", ")").replace("[", "(").replace("]", ")")
    s = re.sub(r"\\d?frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", s)
    s = re.sub(r"\^\{([^{}]*)\}", r"^(\1)", s)
    s = re.sub(r"(?<=[a-z])(?=[a-z])", "*", s)
    return expresion(s)


def terminos(s):
    """Número de términos de la respuesta escrita (signos + y - de primer nivel)."""
    nivel, n = 0, 1
    for i, c in enumerate(s):
        nivel += c in "({[" and 1 or c in ")}]" and -1 or 0
        n += nivel == 0 and c in "+-" and i > 0
    return n


def normal(e):
    """Expande y junta potencias de igual base (a·a^m = a^{m+1}), también con exponentes literales."""
    return powsimp(expand(e))


def reducida(res):
    return len(Add.make_args(normal(ltx(res)))) == terminos(res)


_n = [0]


def multiplicar(tema, fuente, filas):
    """Filas (literal, factor 1, factor 2, producto escrito a mano, dificultad[, notas])."""
    for literal, p, q, res, dif, *notas in filas:
        _n[0] += 1
        extra = dict(notas=notas[0]) if notas else {}

        @ejercicio(id=f"multiplicacion-algebraica-8-{_n[0]:03d}", tema=tema, grados=[8], dba=DBA,
                   tipo="calculo", dificultad=dif, fuente=f"{fuente} n.º {literal}",
                   enunciado=f"Multiplica ${p}$ por ${q}$.", respuesta=f"${res}$.", **extra)
        def _(p=p, q=q, res=res):
            assert normal(ltx(p) * ltx(q) - ltx(res)) == 0, "el producto no coincide"
            assert reducida(res), "quedan términos semejantes"


def desarrollar(tema, instruccion, fuente, filas):
    """Filas (literal, expresión, resultado escrito a mano, dificultad[, notas])."""
    for literal, e, res, dif, *notas in filas:
        _n[0] += 1
        extra = dict(notas=notas[0]) if notas else {}

        @ejercicio(id=f"multiplicacion-algebraica-8-{_n[0]:03d}", tema=tema, grados=[8], dba=DBA,
                   tipo="calculo", dificultad=dif, fuente=f"{fuente} n.º {literal}",
                   enunciado=f"{instruccion} ${e}$.", respuesta=f"${res}$.", **extra)
        def _(e=e, res=res):
            assert normal(ltx(e) - ltx(res)) == 0, "el resultado no es equivalente"
            assert reducida(res), "quedan términos semejantes"


F = r"\frac"

# ---------- Monomios ----------
multiplicar("multiplicación de monomios",
            f"{BALDOR}, Multiplicación de monomios — Ejercicio 35, pp. 65-66,", [
                ("1", "2", "-3", "-6", 1),
                ("2", "-4", "-8", "32", 1),
                ("3", "-15", "16", "-240", 1),
                ("4", "ab", "-ab", "-a^2b^2", 1),
                ("5", "2x^2", "-3x", "-6x^3", 1),
                ("6", "-4a^2b", "-ab^2", "4a^3b^3", 1),
                ("7", "-5x^3y", "xy^2", "-5x^4y^3", 1),
                ("8", "a^2b^3", "3a^2x", "3a^4b^3x", 1),
                ("9", "-4m^2", "-5mn^2p", "20m^3n^2p", 1),
                ("10", "5a^2y", "-6x^2", "-30a^2x^2y", 1),
                ("11", "-x^2y^3", "-4y^3z^4", "4x^2y^6z^4", 1),
                ("12", "abc", "cd", "abc^2d", 1),
                ("13", "-15x^4y^3", "-16a^2x^3", "240a^2x^7y^3", 1),
                ("14", "3a^2b^3", "-4x^2y", "-12a^2b^3x^2y", 1),
                ("15", "3a^2bx", "7b^3x^5", "21a^2b^4x^6", 1),
                ("16", "-8m^2n^3", "-9a^2mx^4", "72a^2m^3n^3x^4", 1),
                ("17", "a^mb^n", "-ab", "-a^{m+1}b^{n+1}", 2),
                ("18", "-5a^mb^n", "-6a^2b^3x", "30a^{m+2}b^{n+3}x", 2),
                ("19", "x^my^nc", "-x^my^nc^x", "-c^{x+1}x^{2m}y^{2n}", 2),
                ("20", "-m^xn^a", "-6m^2n", "6m^{x+2}n^{a+1}", 2),
            ])

multiplicar("multiplicación de monomios",
            f"{BALDOR}, Multiplicación de monomios con exponentes literales — Ejercicio 36, "
            f"pp. 65-66,", [
                ("1", "a^m", "a^{m+1}", "a^{2m+1}", 2),
                ("2", "-x^a", "-x^{a+2}", "x^{2a+2}", 2),
                ("3", "4a^nb^x", "-ab^{x+1}", "-4a^{n+1}b^{2x+1}", 2),
                ("4", "-a^{n+1}b^{n+2}", "a^{n+2}b^n", "-a^{2n+3}b^{2n+2}", 2),
                ("5", "-3a^{n+4}b^{n+1}", "-4a^{n+2}b^{n+3}", "12a^{2n+6}b^{2n+4}", 2),
                ("6", "3x^2y^3", "4x^{m+1}y^{m+2}", "12x^{m+3}y^{m+5}", 2),
                ("7", "4x^{a+2}b^{a+4}", "-5x^{a+5}b^{a+1}", "-20b^{2a+5}x^{2a+7}", 2),
                ("8", "a^mb^nc", "-a^mb^{2n}", "-a^{2m}b^{3n}c", 2),
                ("9", "-x^{m+1}y^{a+2}", "-4x^{m-3}y^{a-5}c^2", "4c^2x^{2m-2}y^{2a-3}", 2),
                ("10", "-5m^an^{b-1}c", "-7m^{2a-3}n^{b-4}", "35cm^{3a-3}n^{2b-5}", 2),
            ])

multiplicar("multiplicación de monomios",
            f"{BALDOR}, Multiplicación de monomios con coeficientes fraccionarios — "
            f"Ejercicio 37, pp. 65-66,", [
                ("1", f"{F}{{1}}{{2}}a^2", f"{F}{{4}}{{5}}a^3b", f"{F}{{2}}{{5}}a^5b", 1),
                ("2", f"-{F}{{3}}{{7}}m^2n", f"-{F}{{7}}{{14}}a^2m^3", f"{F}{{3}}{{14}}a^2m^5n", 2,
                 "El coeficiente -7/14 aparece así en la fuente (sin simplificar: -1/2)."),
                ("3", f"{F}{{2}}{{3}}x^2y^3", f"-{F}{{3}}{{5}}a^2x^4y", f"-{F}{{2}}{{5}}a^2x^6y^4", 1),
                ("4", f"-{F}{{1}}{{8}}m^3n^4", f"-{F}{{4}}{{5}}a^3m^2n", f"{F}{{1}}{{10}}a^3m^5n^5", 1),
                ("5", f"-{F}{{7}}{{8}}abc", f"{F}{{2}}{{7}}a^3", f"-{F}{{1}}{{4}}a^4bc", 1),
                ("6", f"-{F}{{3}}{{5}}x^3y^4", f"-{F}{{5}}{{6}}a^2by^5", f"{F}{{1}}{{2}}a^2bx^3y^9", 1),
                ("7", f"{F}{{1}}{{3}}a", f"{F}{{3}}{{5}}a^m", f"{F}{{1}}{{5}}a^{{m+1}}", 2),
                ("8", f"-{F}{{3}}{{4}}a^m", f"-{F}{{2}}{{5}}ab^3", f"{F}{{3}}{{10}}a^{{m+1}}b^3", 2),
                ("9", f"{F}{{5}}{{6}}a^mb^n", f"-{F}{{3}}{{10}}ab^2c", f"-{F}{{1}}{{4}}a^{{m+1}}b^{{n+2}}c", 2),
                ("10", f"-{F}{{2}}{{9}}a^xb^{{m+1}}", f"-{F}{{3}}{{5}}a^{{x-1}}b^m",
                 f"{F}{{2}}{{15}}a^{{2x-1}}b^{{2m+1}}", 2),
                ("11", f"{F}{{3}}{{8}}a^mb^n", f"-{F}{{4}}{{5}}a^{{2m}}b^n", f"-{F}{{3}}{{10}}a^{{3m}}b^{{2n}}", 2),
                ("12", f"-{F}{{2}}{{11}}a^{{x+1}}b^{{x-3}}c^2", f"-{F}{{44}}{{7}}a^{{x-3}}b^2",
                 f"{F}{{8}}{{7}}a^{{2x-2}}b^{{x-1}}c^2", 2),
            ])

desarrollar("multiplicación de monomios", "Multiplica:",
            f"{BALDOR}, Multiplicación de más de dos monomios — Ejercicio 38, p. 67,", [
                ("1", "(a)(-3a)(a^2)", "-3a^4", 1),
                ("2", "(3x^2)(-x^3y)(-a^2x)", "3a^2x^6y", 1),
                ("3", "(-m^2n)(-3m^2)(-5mn^3)", "-15m^5n^4", 1),
                ("4", "(4a^2)(-5a^3x^2)(-ay^2)", "20a^6x^2y^2", 1),
                ("5", "(-a^m)(-2ab)(-3a^2b^x)", "-6a^{m+3}b^{x+1}", 2),
                ("6", r"\left(\frac{1}{2}x^3\right)\left(-\frac{2}{3}a^2x\right)\left(-\frac{3}{5}a^4m\right)",
                 r"\frac{1}{5}a^6mx^4", 2),
                ("7", r"\left(\frac{2}{3}a^m\right)\left(\frac{3}{4}a^2b^4\right)\left(-3a^4b^{x+1}\right)",
                 r"-\frac{3}{2}a^{m+6}b^{x+5}", 2),
                ("8", r"\left(-\frac{3}{5}m^3\right)\left(-5a^2m\right)\left(-\frac{1}{10}a^xm^a\right)",
                 r"-\frac{3}{10}a^{x+2}m^{a+4}", 2),
                ("9", "(2a)(-a^2)(-3a^3)(4a)", "24a^7", 1),
                ("10", "(-3b^2)(-4a^3b)(ab)(-5a^2x)", "-60a^6b^4x", 1),
                ("11", "(a^mb^x)(-a^2)(-2ab)(-3a^2x)", "-6a^{m+5}b^{x+1}x", 2),
                ("12", r"\left(-\frac{1}{2}x^2y\right)\left(-\frac{3}{5}xy^2\right)\left(-\frac{3}{4}x^2y\right)",
                 r"-\frac{9}{40}x^5y^4", 2),
            ])

# ---------- Polinomio por monomio ----------
multiplicar("multiplicación de polinomio por monomio",
            f"{BALDOR}, Multiplicación de polinomios por monomios — Ejercicio 39, p. 68,", [
                ("1", "3x^3-x^2", "-2x", "-6x^4+2x^3", 1),
                ("2", "8x^2y-3y^2", "2ax^3", "16ax^5y-6ax^3y^2", 1),
                ("3", "x^2-4x+3", "-2x", "-2x^3+8x^2-6x", 1),
                ("4", "a^3-4a^2+6a", "3ab", "3a^4b-12a^3b+18a^2b", 1),
                ("5", "a^2-2ab+b^2", "-ab", "-a^3b+2a^2b^2-ab^3", 1),
                ("6", "x^5-6x^3-8x", "3a^2x^2", "3a^2x^7-18a^2x^5-24a^2x^3", 1),
                ("7", "m^4-3m^2n^2+8n^4", "-4m^3x", "-4m^7x+12m^5n^2x-32m^3n^4x", 1),
                ("8", "x^3-4x^2y+6xy^2", "ax^3y", "ax^6y-4ax^5y^2+6ax^4y^3", 1),
                ("9", "a^3-5a^2b-8ab^2", "-4a^4m^2", "-4a^7m^2+20a^6bm^2+32a^5b^2m^2", 1),
                ("10", "a^m-a^{m-1}+a^{m-2}", "-2a", "-2a^{m+1}+2a^m-2a^{m-1}", 2),
                ("11", "x^{m+1}+3x^m-x^{m-1}", "3x^{2m}", "3x^{3m+1}+9x^{3m}-3x^{3m-1}", 2),
                ("12", "a^mb^n+a^{m-1}b^{n+1}-a^{m-2}b^{n+2}", "3a^2b",
                 "3a^{m+2}b^{n+1}+3a^{m+1}b^{n+2}-3a^mb^{n+3}", 2),
                ("13", "x^3-3x^2+5x-6", "-4x^2", "-4x^5+12x^4-20x^3+24x^2", 1),
                ("14", "a^4-6a^3x+9a^2x^2-8", "3bx^3", "3a^4bx^3-18a^3bx^4+27a^2bx^5-24bx^3", 1),
                ("15", "a^{n+3}-3a^{n+2}-4a^{n+1}-a^n", "-a^nx^2",
                 "-a^{2n+3}x^2+3a^{2n+2}x^2+4a^{2n+1}x^2+a^{2n}x^2", 2),
                ("16", "x^4-6x^3+8x^2-7x+5", "-3a^2x^3",
                 "-3a^2x^7+18a^2x^6-24a^2x^5+21a^2x^4-15a^2x^3", 1),
                ("17", "-3x^3+5x^2y-7xy^2-4y^3", "5a^2xy^2",
                 "-15a^2x^4y^2+25a^2x^3y^3-35a^2x^2y^4-20a^2xy^5", 1),
                ("18", "x^{a+5}-3x^{a+4}+x^{a+3}-5x^{a+1}", "-2x^2",
                 "-2x^{a+7}+6x^{a+6}-2x^{a+5}+10x^{a+3}", 2),
            ])

multiplicar("multiplicación de polinomio por monomio",
            f"{BALDOR}, Multiplicación de polinomios por monomios con coeficientes "
            f"fraccionarios — Ejercicio 40, p. 68,", [
                ("1", r"\frac{1}{2}a-\frac{2}{3}b", r"\frac{2}{5}a^2",
                 r"\frac{1}{5}a^3-\frac{4}{15}a^2b", 2),
                ("2", r"\frac{2}{3}a-\frac{3}{4}b", r"-\frac{2}{3}a^3b",
                 r"-\frac{4}{9}a^4b+\frac{1}{2}a^3b^2", 2),
                ("3", r"\frac{3}{5}a-\frac{1}{6}b+\frac{2}{5}c", r"-\frac{5}{3}ac^2",
                 r"-a^2c^2+\frac{5}{18}abc^2-\frac{2}{3}ac^3", 2),
                ("4", r"\frac{2}{5}a^2+\frac{1}{3}ab-\frac{2}{9}b^2", "3a^x",
                 r"\frac{6}{5}a^{x+2}+a^{x+1}b-\frac{2}{3}a^xb^2", 2),
                ("5", r"\frac{1}{3}x^2-\frac{2}{5}xy-\frac{1}{4}y^2", r"\frac{3}{2}y^3",
                 r"\frac{1}{2}x^2y^3-\frac{3}{5}xy^4-\frac{3}{8}y^5", 2),
                ("6", "3a-5b+6c", r"-\frac{3}{10}a^2x^3",
                 r"-\frac{9}{10}a^3x^3+\frac{3}{2}a^2bx^3-\frac{9}{5}a^2cx^3", 2),
                ("7", r"\frac{2}{9}x^4-x^2y^2+\frac{1}{3}y^4", r"\frac{3}{7}x^3y^4",
                 r"\frac{2}{21}x^7y^4-\frac{3}{7}x^5y^6+\frac{1}{7}x^3y^8", 2),
                ("8", r"\frac{1}{2}a^2-\frac{1}{3}b^2+\frac{1}{3}x^2-\frac{1}{5}y^2",
                 r"-\frac{5}{8}a^2m",
                 r"-\frac{5}{16}a^4m+\frac{5}{24}a^2b^2m-\frac{5}{24}a^2mx^2+\frac{1}{8}a^2my^2", 2),
                ("9", r"\frac{2}{3}m^3+\frac{1}{2}m^2n-\frac{5}{6}mn^2-\frac{1}{9}n^3",
                 r"\frac{3}{4}m^2n^3",
                 r"\frac{1}{2}m^5n^3+\frac{3}{8}m^4n^4-\frac{5}{8}m^3n^5-\frac{1}{12}m^2n^6", 2),
                ("10", r"\frac{2}{5}x^6-\frac{1}{3}x^4y^2+\frac{3}{5}x^2y^4-\frac{1}{10}y^6",
                 r"-\frac{5}{7}a^3x^4y^3",
                 r"-\frac{2}{7}a^3x^{10}y^3+\frac{5}{21}a^3x^8y^5-\frac{3}{7}a^3x^6y^7"
                 r"+\frac{1}{14}a^3x^4y^9", 2),
            ])

# ---------- Polinomio por polinomio ----------
multiplicar("multiplicación de polinomios",
            f"{BALDOR}, Multiplicación de polinomios por polinomios — Ejercicio 41, p. 69,", [
                ("1", "a+3", "a-1", "a^2+2a-3", 1),
                ("2", "a-3", "a+1", "a^2-2a-3", 1),
                ("3", "x+5", "x-4", "x^2+x-20", 1),
                ("4", "m-6", "m-5", "m^2-11m+30", 1),
                ("5", "-x+3", "-x+5", "x^2-8x+15", 1),
                ("6", "-a-2", "-a-3", "a^2+5a+6", 1),
                ("7", "3x-2y", "y+2x", "6x^2-xy-2y^2", 1),
                ("8", "-4y+5x", "-3x+2y", "-15x^2+22xy-8y^2", 1),
                ("9", "5a-7b", "a+3b", "5a^2+8ab-21b^2", 1),
                ("10", "8n-9m", "4n+6m", "-54m^2+12mn+32n^2", 1,
                 "Es el n.º 13 del ejercicio 41 de Baldor."),
            ])

multiplicar("multiplicación de polinomios",
            f"{BALDOR}, Multiplicación de polinomios por polinomios — Ejercicio 42, p. 70,", [
                ("1", "x^2+xy+y^2", "x-y", "x^3-y^3", 1),
                ("2", "a^2+b^2-2ab", "a-b", "a^3-3a^2b+3ab^2-b^3", 1),
                ("3", "a^2+b^2+2ab", "a+b", "a^3+3a^2b+3ab^2+b^3", 1),
                ("4", "x^3-3x^2+1", "x+3", "x^4-9x^2+x+3", 1),
                ("5", "a^3-a+a^2", "a-1", "a^4-2a^2+a", 1,
                 "En la transcripción aparece «a^2 - a + a^2» (el a^2 repetido); en Baldor es "
                 "a^3 - a + a^2, que da a^4 - 2a^2 + a."),
                ("6", "m^4+m^2n^2+n^4", "m^2-n^2", "m^6-n^6", 1),
                ("7", "x^3-2x^2+3x-1", "2x+3", "2x^4-x^3+7x-3", 2),
                ("8", "3y^3+5-6y", "y^2+2", "3y^5+5y^2-12y+10", 2),
                ("9", "m^3-m^2+m-2", "am+a", "am^4-am-2a", 2),
                ("10", "3a^2-5ab+2b^2", "4a-5b", "12a^3-35a^2b+33ab^2-10b^3", 2),
                ("11", "5m^4-3m^2n^2+n^4", "3m-n", "15m^5-5m^4n-9m^3n^2+3m^2n^3+3mn^4-n^5", 2),
                ("12", "a^2+a+1", "a^2-a-1", "a^4-a^2-2a-1", 2),
                ("13", "x^3+2x^2-x", "x^2-2x+5", "x^5+12x^2-5x", 2),
                ("14", "m^3-3m^2n+2mn^2", "m^2-2mn", "m^5-5m^4n+8m^3n^2-4m^2n^3", 2,
                 "Quien transcribió anota que el ejercicio fue modificado respecto a Baldor."),
                ("15", "x^2+1+x", "x^2-x-1", "x^4-x^2-2x-1", 2),
                ("16", "2-3x^2+x^4", "x^2-2x+3", "x^6-2x^5+6x^3-7x^2-4x+6", 2),
                ("17", "m^3-4m+m^2-1", "m^3+1", "m^6+m^5-4m^4+m^2-4m-1", 2),
                ("18", "a^3-5a+2", "a^2-a+5", "a^5-a^4+7a^2-27a+10", 2),
                ("19", "x^2-2xy+y^2", "xy-x^2+3y^2", "-x^4+3x^3y-5xy^3+3y^4", 2),
                ("20", "n^2-2n+1", "n^2-1", "n^4-2n^3+2n-1", 1),
            ])

multiplicar("multiplicación de polinomios",
            f"{BALDOR}, Multiplicación de polinomios con exponentes literales — Ejercicio 43, "
            f"p. 71,", [
                ("1", "a^x-a^{x+1}+a^{x+2}", "a+1", "a^{x+3}+a^x", 2),
                ("2", "x^{n+1}+2x^{n+2}-x^{n+3}", "x^2+x", "-x^{n+5}+x^{n+4}+3x^{n+3}+x^{n+2}", 2),
                ("3", "m^{a-1}+m^{a+1}+m^{a+2}-m^a", "m^2-2m+3",
                 "m^{a+4}-m^{a+3}+6m^{a+1}-5m^a+3m^{a-1}", 3),
                ("4", "a^{n+2}-2a^n+2a^{n+1}", "a^n+a^{n+1}", "a^{2n+3}+3a^{2n+2}-2a^{2n}", 3),
                ("5", "x^{a+2}-x^a+2x^{a+1}", "x^{a+3}-2x^{a+1}",
                 "x^{2a+5}+2x^{2a+4}-3x^{2a+3}-4x^{2a+2}+2x^{2a+1}", 3),
                ("6", "3a^{x-2}-2a^{x-1}+a^x", "a^2+2a-1", "a^{x+2}-2a^x+8a^{x-1}-3a^{x-2}", 3),
                ("7", "3a^{x-1}+a^x-2a^{x-2}", "a^x-a^{x-1}+a^{x-2}",
                 "a^{2x}+2a^{2x-1}-4a^{2x-2}+5a^{2x-3}-2a^{2x-4}", 3),
                ("8", "m^{a+1}-2m^{a+2}-m^{a+3}+m^{a+4}", "m^{a-3}-m^{a-1}+m^{a-2}",
                 "-m^{2a+3}+2m^{2a+2}+2m^{2a+1}-4m^{2a}-m^{2a-1}+m^{2a-2}", 3),
                ("9", "x^{a-1}+2x^{a-2}-x^{a-3}+x^{a-4}", "-x^{a-3}+x^{a-1}-x^{a-2}",
                 "x^{2a-2}+x^{2a-3}-4x^{2a-4}-x^{2a-7}", 3),
                ("10", "a^nb-a^{n-1}b^2+2a^{n-2}b^3-a^{n-3}b^4", "a^nb^2-a^{n-2}b^4",
                 "a^{2n}b^3-a^{2n-1}b^4+a^{2n-2}b^5-2a^{2n-4}b^7+a^{2n-5}b^8", 3),
                ("11", "a^x+b^x", "a^m+b^m", "a^{m+x}+a^xb^m+a^mb^x+b^{m+x}", 2),
                ("12", "a^{x-1}-b^{n-1}", "a-b", "a^x-a^{x-1}b-ab^{n-1}+b^n", 2),
                ("13", "a^{2m+1}-5a^{2m+2}+3a^{2m}", "a^{3m-3}+6a^{3m-1}-8a^{3m-2}",
                 "-30a^{5m+1}+46a^{5m}+5a^{5m-1}-23a^{5m-2}+3a^{5m-3}", 3),
                ("14", "x^{a+2}y^{x-1}+3x^ay^{x+1}-4x^{a+1}y^x",
                 "-2x^{2a-1}y^{x-2}-10x^{2a-3}y^x-4x^{2a-2}y^{x-1}",
                 "-2x^{3a+1}y^{2x-3}+4x^{3a}y^{2x-2}+28x^{3a-2}y^{2x}-30x^{3a-3}y^{2x+1}", 3,
                 "La letra x aparece como base y como exponente, igual que en Baldor."),
            ])

multiplicar("multiplicación de polinomios",
            f"{BALDOR}, Multiplicación de polinomios con coeficientes fraccionarios — "
            f"Ejercicio 44, p. 72,", [
                ("1", r"\frac{1}{2}a-\frac{1}{3}b", r"\frac{1}{3}a+\frac{1}{2}b",
                 r"\frac{1}{6}a^2+\frac{5}{36}ab-\frac{1}{6}b^2", 2,
                 "En la transcripción el primer factor es «1/2 a - 1/3» (falta la b); en Baldor es "
                 "1/2 a - 1/3 b."),
                ("2", r"x-\frac{2}{5}y", r"\frac{5}{6}y+\frac{1}{3}x",
                 r"\frac{1}{3}x^2+\frac{7}{10}xy-\frac{1}{3}y^2", 2),
                ("3", r"\frac{1}{2}x^2-\frac{1}{3}xy+\frac{1}{4}y^2", r"\frac{2}{3}x-\frac{3}{2}y",
                 r"\frac{1}{3}x^3-\frac{35}{36}x^2y+\frac{2}{3}xy^2-\frac{3}{8}y^3", 3),
                ("4", r"\frac{1}{4}a^2-ab+\frac{2}{3}b^2", r"\frac{1}{4}a-\frac{3}{2}b",
                 r"\frac{1}{16}a^3-\frac{5}{8}a^2b+\frac{5}{3}ab^2-b^3", 3),
                ("5", r"\frac{2}{5}m^2+\frac{1}{3}mn-\frac{3}{2}n^2", r"\frac{3}{2}m^2+2n^2-mn",
                 r"\frac{3}{5}m^4+\frac{1}{10}m^3n-\frac{107}{60}m^2n^2+\frac{13}{6}mn^3-3n^4", 3,
                 "En la transcripción el último coeficiente está como número mixto «1 1/2»; se "
                 "escribe 3/2 para que no se lea como un producto."),
                ("6", r"\frac{3}{8}x^2+\frac{1}{4}x-\frac{2}{5}", r"2x^3-\frac{1}{3}x+2",
                 r"\frac{3}{4}x^5+\frac{1}{2}x^4-\frac{37}{40}x^3+\frac{2}{3}x^2+\frac{19}{30}x"
                 r"-\frac{4}{5}", 3),
                ("7", r"\frac{1}{3}ax-\frac{1}{2}x^2+\frac{3}{2}a^2", r"\frac{3}{2}x^2-ax+\frac{2}{3}a^2",
                 r"-\frac{3}{4}x^4+ax^3+\frac{19}{12}a^2x^2-\frac{23}{18}a^3x+a^4", 3),
                ("8", r"\frac{2}{7}x^3+\frac{1}{2}xy^2-\frac{1}{5}x^2y",
                 r"\frac{1}{4}x^2-\frac{2}{3}xy+\frac{5}{6}y^2",
                 r"\frac{1}{14}x^5-\frac{101}{420}x^4y+\frac{139}{280}x^3y^2-\frac{1}{2}x^2y^3"
                 r"+\frac{5}{12}xy^4", 3),
            ])

# ---------- Producto continuado ----------
desarrollar("producto continuado de polinomios", "Desarrolla y simplifica:",
            f"{BALDOR}, Producto continuado de polinomios — Ejercicio 44 (así lo cita la "
            f"transcripción), p. 72,", [
                ("1", "4(a+5)(a-3)", "4a^2+8a-60", 1),
                ("2", "3a^2(x+1)(x-1)", "3a^2x^2-3a^2", 1),
                ("3", "2(a-3)(a-1)(a+4)", "2a^3-26a+24", 2),
                ("4", "(x^2+1)(x^2-1)(x^2+1)", "x^6+x^4-x^2-1", 2),
                ("5", "m(m-4)(m-6)(3m+2)", "3m^4-28m^3+52m^2+48m", 2),
                ("6", "(a-b)(a^2-2ab+b^2)(a+b)", "a^4-2a^3b+2ab^3-b^4", 2),
                ("7", "(a^m-3)(a^{m-1}+2)(a^{m-1}-1)",
                 "a^{3m-2}+a^{2m-1}-3a^{2m-2}-2a^m-3a^{m-1}+6", 3,
                 "Es el n.º 9 del ejercicio de Baldor."),
                ("8", "a^x(a^{x+1}+b^{x+2})(a^{x+1}-b^{x+2})b^x", "a^{3x+2}b^x-a^xb^{3x+4}", 3,
                 "Es el n.º 14 del ejercicio de Baldor."),
            ])

# ---------- Multiplicación combinada con suma y resta ----------
desarrollar("multiplicación combinada con suma y resta", "Desarrolla y simplifica:",
            f"{BALDOR}, Multiplicación combinada con suma y resta — Ejercicio 47, p. 76,", [
                ("1", "4(x+3)+5(x+2)", "9x+22", 1),
                ("2", "6(x^2+4)-3(x^2+1)+5(x^2+2)", "8x^2+31", 1),
                ("3", "a(a-x)+3a(x+2a)-a(x-3a)", "10a^2+ax", 1),
                ("4", "x^2(y^2+1)+y^2(x^2+1)-3x^2y^2", "-x^2y^2+x^2+y^2", 1),
                ("5", "4m^3-5mn^2+3m^2(m^2+n^2)-3m(m^2-n^2)", "3m^4+m^3+3m^2n^2-2mn^2", 2),
                ("6", "y^2+x^2y^3-y^3(x^2+1)+y^2(x^2+1)-y^2(x^2-1)", "-y^3+3y^2", 2),
                ("7", "5(x+2)-(x+1)(x+4)-6x", "-x^2-6x+6", 2),
                ("8", "(a+5)(a-5)-3(a+2)(a-2)+5(a+4)", "-2a^2+5a+7", 2),
                ("9", "(a+b)(4a-3b)-(5a-2b)(3a+b)-(a+b)(3a-6b)", "-14a^2+5ab+5b^2", 2),
                ("10", "(a+c)^2-(a-c)^2", "4ac", 2),
                ("11", "3(x+y)^2-4(x-y)^2+3x^2-3y^2", "2x^2+14xy-4y^2", 2),
                ("12", "(m+n)^2-(2m+n)^2+(m-4n)^2", "-2m^2-10mn+16n^2", 2),
                ("13", "x(a+x)+3x(a+1)-(x+1)(a+2x)-(a-x)^2", "-a^2+5ax-2x^2-a+x", 3),
                ("14", "(a+b-c)^2+(a-b+c)^2-(a+b+c)^2", "a^2+b^2+c^2-2ab-2ac-6bc", 3),
                ("15", "(x^2+x-3)^2-(x^2-2+x)^2+(x^2-x-3)^2", "x^4-2x^3-7x^2+4x+14", 3,
                 "En la transcripción el último término es «(x^2 - x - 3)^3» (cubo de un "
                 "trinomio, fuera del nivel de la sección y distinto de los demás, que son "
                 "cuadrados); se corrigió a (x^2 - x - 3)^2."),
                ("16", "(x+y+z)^2-(x+y)(x-y)+3(x^2+xy+y^2)", "3x^2+5xy+5y^2+2xz+2yz+z^2", 3),
                ("17", r"\lbrack x+(2x-3)\rbrack\lbrack 3x-(x+1)\rbrack+4x-x^2", "5x^2-5x+3", 2),
                ("18", r"\lbrack 3(x+1)-4(x+1)\rbrack\lbrack 3(x+4)-2(x+2)\rbrack", "-x^2-9x-8", 2),
                ("19", r"\lbrack(m+n)(m-n)-(m+n)(m+n)\rbrack\lbrack 2(m+n)-3(m-n)\rbrack",
                 "2m^2n-8mn^2-10n^3", 3),
                ("20", r"\lbrack(x+y)^2-3(x-y)^2\rbrack\lbrack(x+y)(x-y)+x(y-x)\rbrack",
                 "-2x^3y+10x^2y^2-10xy^3+2y^4", 3),
            ])

# ---------- Supresión de signos de agrupación con productos indicados ----------
desarrollar("signos de agrupación con productos indicados", "Desarrolla y simplifica:",
            f"{BALDOR}, Supresión de signos de agrupación con productos indicados — "
            f"Ejercicio 44 (así lo cita la transcripción), p. 72,", [
                ("1", "x-(3a+2(-x+1))", "-3a+3x-2", 1),
                ("2", "-(a+b)-3(2a+b(-a+2))", "-7a+3ab-7b", 2),
                ("3", "-(3x-2y+(x-2y)-2(x+y)-3(2x+1))", "4x+6y+3", 2),
                ("4", "4x^2-(-3x+5-(-x+x(2-x)))", "3x^2+4x-5", 2),
                ("5", "2a-(-3x+2(-a+3x-2(-a+b-(2+a))))", "-4a+4b-3x-8", 3),
                ("6", "a-(x+y)-3(x-y)+2(-(x-2y)-2(-x-y))", "a-2x+10y", 2),
                ("7", "m-(m+n)-3(-2m+(-2m+n+2(-1+n)-(m+n-1)))", "15m-7n+3", 3),
                ("8", "-2(a-b)-3(a+2b)-4(a-2b+2(-a+b-1+2(a-b)))", "-17a+12b+8", 3),
                ("9", "-5(x+y)-(2x-y+2(-x+y-3-(x-y-1)))+2x", "-x-8y+4", 3),
                ("10", "m-3(m+n)+(-(-(-2m+n-2-3(m-n+1))+m))", "-8m+n-5", 3),
                ("11", "-3(x-2y)+2(-4(-2x-3(x+y)))-(-(-(x+y)))", "36x+29y", 3),
                ("12", "5(-(a+b)-3(-2a+3b-(a+b)+(-a-b)+2(-a+b))-a)", "80a-50b", 3),
                ("13", "-3(-(+(-a+b)))-4(-(-(-a-b)))", "a+7b", 2),
                ("14", "-(a+b-2(a-b)+3(-(2a+b-3(a+b-1)))-3(-a+2(-1+a)))", "a-9b+3", 3),
            ])
