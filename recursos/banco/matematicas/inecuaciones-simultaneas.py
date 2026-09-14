"""Banco de ejercicios — Matemáticas — Inecuaciones simultáneas de primer grado.
Fuente: módulo de Matemáticas 11° de las Guías de Apoyo (Adriana Quintero Palomino), Tema 1;
se lee en recursos/matematicas/Guías pedagógicas Matemáticas/markdown/11 - Modulo_Matematicas_Undecimo.md
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/matematicas/inecuaciones-simultaneas.py
"""
from ejercicios import serie

FUENTE = ("módulo 11° (Quintero Palomino), Tema 1, Inecuaciones simultáneas de primer grado — "
          "Practica lo aprendido")
COMUN = dict(tema="inecuaciones simultáneas", grados=[11], dba=["matematicas-11-2"],
             tipo="calculo")

# (n, literal, inecuación simultánea, solución calculada a mano, dificultad[, notas])
serie("inecuaciones-simultaneas", "Halla los valores de $x$ que satisfacen …", FUENTE, [
    (1, "1a", "-7 <= 2x + 1 <= 19", "[-4, 9]", 1),
    (2, "1b", "-5 < x - 3 <= -3", "(-2, 0]", 1),
    (3, "1c", "sqrt(2) + 1 < 3x + 1 < 7", "(sqrt(2)/3, 2)", 2),
    (4, "1d", "-3 <= -x < 2", "(-2, 3]", 1),
    (5, "1e", "100 > 400 - 6x > 10", "(50, 65)", 2),
    (6, "1f", "2 <= (1/2)x - 6 <= 8", "[16, 28]", 1),
    (7, "1g", "7 < 3 - (1/2)x <= 8", "[-10, -8)", 2),
    (8, "1h", "-5 <= 3x + 4 < 13", "[-3, 3)", 1),
    (9, "1i", "1/2 <= 2x - 1/2 <= 3/4", "[1/2, 5/8]", 2),
    (10, "1j", "3/7 <= 3x - 1/5 <= 2/5", "vacio", 3,
     "Queda vacía: 3x tendría que estar entre 22/35 y 21/35. Puede ser un error de "
     "digitación del módulo; sirve como ejercicio de conjunto vacío."),
    (11, "2a", "-1 < (3 - 7x)/4 <= 6", "[-3, 1)", 2),
    (12, "2b", "12 >= 5x - 3 > -7", "(-4/5, 3]", 1),
    (13, "2c", "2x < x < 3", "(-oo, 0)", 2),
    (14, "2d", "x <= 3 - x < 0", "vacio", 2),
    (15, "2e", "7/2 > (1 - 4x)/5 > 3/2", "(-33/8, -13/8)", 3),
    (16, "2f", "(1/2)x <= 2 <= (1/3)x", "vacio", 2),
    (17, "2g", "-3x + 1 < x < 5", "(1/4, 5)", 2),
    (18, "2h", "-x <= x <= 0", "{0}", 2),
    (19, "2i", "1/2 - x < 0 < x - 1", "(1, oo)", 2),
    (20, "2j", "sqrt(3)x <= 5x <= sqrt(3)", "[0, sqrt(3)/5]", 3),
], **COMUN)
