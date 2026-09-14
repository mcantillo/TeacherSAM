"""Banco de ejercicios — Matemáticas 8° — Notación científica.
Fuente: módulo de Matemáticas 8° de las Guías de Apoyo (Adriana Quintero Palomino), Tema 1;
se lee en recursos/matematicas/Guías pedagógicas Matemáticas/markdown/08 - Modulo_Matematicas_Octavo.md
DBA: matematicas-8-9 («opera con formas simbólicas que representan números»); también 8-1
(representaciones decimales de los números).
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/notacion-cientifica-8.py
"""
from fractions import Fraction as Fr

from ejercicios import ejercicio

FUENTE = "módulo 8° (Quintero Palomino), Tema 1, Notación científica — Practica lo aprendido"
COMUN = dict(tema="notación científica", grados=[8], dba=["matematicas-8-9", "matematicas-8-1"])


def item(n, literal, enunciado, respuesta, comprobar, dificultad=1, notas=None):
    extra = dict(notas=notas) if notas else {}

    def envuelta():
        assert bool(comprobar()), "la comprobación dio falso"
    envuelta.__wrapped__ = comprobar          # la huella usa el código de la comprobación
    ejercicio(id=f"notacion-cientifica-8-{n:03d}", fuente=f"{FUENTE} {literal}",
              enunciado=enunciado, respuesta=respuesta, tipo="calculo", dificultad=dificultad,
              **extra, **COMUN)(envuelta)


def cientifica(valor, mantisa, exp):
    """valor = mantisa · 10^exp con 1 ≤ mantisa < 10 (todo exacto con fracciones)."""
    assert 1 <= Fr(mantisa) < 10, "la mantisa no está entre 1 y 10"
    assert Fr(valor) == Fr(mantisa) * Fr(10) ** exp, "el valor no coincide"
    return True


A_CIENT = "Efectúa las operaciones (si las hay) y escribe en notación científica: ${}$."
for n, lit, tx, valor, rt, mant, exp, dif in [
    (1, "1a", r"4\,000\,000\,000", 4000000000, r"4 \times 10^{9}", "4", 9, 1),
    (2, "1b", r"12 \cdot 10^{5} \cdot 10^{8}", 12 * 10**13, r"\num{1,2} \times 10^{14}", "1.2", 14, 2),
    (3, "1c", r"10^{5} \cdot \num{3,5} \cdot 10^{4}", Fr("3.5") * 10**9,
     r"\num{3,5} \times 10^{9}", "3.5", 9, 1),
    (4, "1d", r"9\,000\,000 \times 5000", 9000000 * 5000, r"\num{4,5} \times 10^{10}", "4.5", 10, 2),
    (5, "1e", r"7 \cdot 10^{2} + 4 \cdot 10^{3}", 7 * 10**2 + 4 * 10**3,
     r"4700 = \num{4,7} \times 10^{3}", "4.7", 3, 2),
    (6, "1f", r"25\,000 \times 186\,000\,000", 25000 * 186000000,
     r"\num{4,65} \times 10^{12}", "4.65", 12, 2),
    (7, "1g", r"\num{0,093}", Fr("0.093"), r"\num{9,3} \times 10^{-2}", "9.3", -2, 1),
    (8, "1h", r"\num{0,00053}", Fr("0.00053"), r"\num{5,3} \times 10^{-4}", "5.3", -4, 1),
    (9, "1i", r"\num{0,000000000023}", Fr("0.000000000023"), r"\num{2,3} \times 10^{-11}", "2.3",
     -11, 1),
]:
    item(n, lit, A_CIENT.format(tx), f"${rt}$.",
         lambda valor=valor, mant=mant, exp=exp: cientifica(valor, mant, exp), dificultad=dif)

A_DECIMAL = "Escribe en notación decimal: ${}$."
for n, lit, tx, mant, exp, rt, rv, nota in [
    (10, "2a", r"10^{-7}", "1", -7, r"\num{0,0000001}", "0.0000001", None),
    (11, "2b", r"5 \cdot 10^{-3}", "5", -3, r"\num{0,005}", "0.005", None),
    (12, "2c", r"\num{14,3} \cdot 10^{2}", "14.3", 2, "1430", "1430", None),
    (13, "2d", r"\num{38,5} \cdot 10^{4}", "38.5", 4, r"385\,000", "385000", None),
    (14, "2e", r"\num{423,32} \cdot 10^{-6}", "423.32", -6, r"\num{0,00042332}", "0.00042332",
     "El texto alternativo del módulo dice «10 elevado a la menos 5», pero la fórmula impresa "
     "es 10^{-6}; se respetó la impresa."),
]:
    item(n, lit, A_DECIMAL.format(tx), f"${rt}$.",
         lambda mant=mant, exp=exp, rv=rv: Fr(mant) * Fr(10) ** exp == Fr(rv), notas=nota)
