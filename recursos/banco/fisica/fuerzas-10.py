"""Banco de ejercicios — Física 10° — Tercera ley de Newton.
Escritos para la guía del trimestre I de Física 10° (hilo «De la inercia a los Principia»,
2026-09-15) porque el banco no tenía ningún ejercicio verificado de la tercera ley (solo
leyes-newton-10-025, abierto y pendiente de aprobación). Regla de la docente: solo lo mínimo
para que el tema no quede vacío.
  -001  el ejemplo del propio DBA 1 de 10° (adulto sobre hielo y niño que tiran de una cuerda).
  -002  acción y reacción a distancia (manzana y Tierra), que la evidencia 3 nombra.
DBA: naturales grado 10 · DBA 1 — Comprende, que el reposo o el movimiento rectilíneo
uniforme, se presentan cuando las fuerzas aplicadas sobre el sistema se anulan entre ellas, y
que en presencia de fuerzas resultantes no nulas se producen cambios de velocidad.
g = 9,8 m/s².
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar --sin-registro recursos/banco/fisica/fuerzas-10.py
"""
from sympy.physics.units import convert_to, kilogram, meter, newton, second

from ejercicios import ejercicio

PRE = "fuerzas-10"
COMUN = dict(tema="tercera ley de Newton", grados=[10], dba=["naturales-10-1"],
             fuente="Escrito para la guía de Física 10°, trimestre I (2026-09-15); "
                    "-001 adapta el ejemplo del DBA 1 de 10°")
g = 9.8


def cerca(x, esperado, rel=0.005):
    assert abs(x - esperado) <= rel * abs(esperado), f"{x} ≠ {esperado}"


@ejercicio(id=f"{PRE}-001", tipo="contexto", dificultad=2,
           enunciado=r"Un adulto de \qty{70}{kg} está parado sobre hielo (sin fricción) y un "
           r"niño de \qty{35}{kg}, bien apoyado en el piso, tira de una cuerda atada al adulto "
           r"con una fuerza de \qty{140}{N}. ¿Qué fuerza ejerce el adulto sobre el niño a "
           r"través de la cuerda? ¿Qué aceleración adquiere el adulto? ¿Por qué el niño no "
           r"se mueve?",
           respuesta=r"Por la tercera ley, el adulto tira del niño con \qty{140}{N} en sentido "
           r"contrario. El adulto, sin fricción, acelera $a = 140/70 = \qty{2}{m/s^2}$ hacia el "
           r"niño. El niño no se mueve porque la fricción del piso sobre sus pies equilibra los "
           r"\qty{140}{N}: sobre él la fuerza neta es cero.", **COMUN)
def _():
    F = 140 * newton
    a = convert_to(F / (70 * kilogram), meter / second**2) / (meter / second**2)
    assert a == 2
    friccion_nino = F          # equilibrio del niño: cuerda y fricción del piso se anulan
    assert F - friccion_nino == 0


@ejercicio(id=f"{PRE}-002", tipo="contexto", dificultad=3,
           enunciado=r"Una manzana de \qty{0,20}{kg} cae de un árbol. La Tierra la atrae con su "
           r"peso; por la tercera ley, la manzana atrae a la Tierra con una fuerza igual. "
           r"Calcula esa fuerza y la aceleración que produce en la Tierra "
           r"($M_T = \qty{5,97e24}{kg}$). ¿Por qué no notamos que la Tierra «sube» hacia la "
           r"manzana?",
           respuesta=r"$F = mg = 0{,}20 \times 9{,}8 = \qty{1,96}{N}$ sobre cada una. "
           r"$a_T = 1{,}96/\num{5,97e24} \approx \qty{3,3e-25}{m/s^2}$: la fuerza es la misma, "
           r"pero la masa de la Tierra es enorme, así que su aceleración es imperceptible.",
           **COMUN)
def _():
    F = 0.20 * g
    cerca(F, 1.96)
    cerca(F / 5.97e24, 3.28e-25, 0.01)
