"""Banco de ejercicios — Física 9° — Calor y termodinámica (problemas de la guía de 8°).
Fuente: Guía de Apoyo de Física 8° (calor y termodinámica), se lee en
recursos/fisica/Guías pedagógicas Física/markdown/08 - Guia_de_Apoyo_Conceptos_de_Calor_y_termodinamica_grado_8_fisica.md
Solo se tomaron los ejercicios cuantitativos que corresponden a los Estándares 8°–9° de Física 9°
(dba/naturales/estandares-fisica.md): «Comparo masa, peso, cantidad de sustancia y densidad…»,
«Establezco relaciones entre las variables de estado en un sistema termodinámico… y las expreso
matemáticamente», «Establezco relaciones entre energía interna de un sistema termodinámico,
trabajo y transferencia de energía térmica», «Explico la relación entre ciclos termodinámicos y el
funcionamiento de motores». Son: Cap. 1 Ejercicios 17 y 44; Problemas de los caps. 2, 3, 4 y 5.
No incluidos: las preguntas conceptuales de la guía de 8° (repaso, ejercicios, «Desarrolla tus
competencias», laboratorios), que son material de 8°.
Unidades: 1 cal = 4,184 J (valor de la guía); g = 9,8 m/s².
Formato y reglas: .claude/skills/verificar-ejercicios/SKILL.md
Verificar:  python3 tools/ejercicios.py verificar recursos/banco/fisica/termodinamica-9.py
"""
from itertools import product

from sympy import Eq, Rational as Q, pi, simplify, solve, symbols
from sympy.physics.units import (centimeter, convert_to, gram, hour, joule, kelvin, kilogram,
                                 meter, newton, second, watt, year)

from ejercicios import ejercicio

P = "termodinamica-9"
GUIA = "Guía de Apoyo Física 8° (calor y termodinámica)"
CAL = Q(4184, 1000) * joule
C_AGUA = 1 * CAL / (gram * kelvin)                  # 1 cal/(g·°C); ΔT en °C = ΔT en K
G = Q(98, 10) * meter / second**2
ALFA_ACERO, ALFA_AL = Q(11, 10**6) / kelvin, Q(24, 10**6) / kelvin
T = symbols("T", real=True)


def fuente(cap, seccion, lit):
    return f"{GUIA}, {cap}, {seccion} — {lit}"


def cerca(a, b, tol=Q(5, 1000)):
    """a y b son cantidades de la misma dimensión; iguales salvo el redondeo tol (relativo)."""
    base = [meter, second, kilogram, kelvin]
    r = simplify(convert_to(a, base) / convert_to(b, base))
    assert r.is_number, f"dimensiones distintas: {a} / {b}"
    assert abs(float(r) - 1) <= tol, f"{float(r)}"


def comun(tema):
    return dict(tema=tema, grados=[9], dba=[])


# ---------------------------------------------------------------- Cap. 1 Los fluidos
C1 = "Cap. 1 Los fluidos"


@ejercicio(id=f"{P}-001", tipo="contexto", dificultad=2, fuente=fuente(C1, "Ejercicios", "17"),
           enunciado=r"Se quiere construir una figura en oro con una masa de "
                     r"$\num{0,4}\,\text{kg}$. Se observa que el volumen de la figura es de "
                     r"$176\,\text{cm}^3$. ¿Está hecha la figura de oro puro? Explica. (Densidad "
                     r"del oro: $\num{19,3}\,\text{g/cm}^3$.)",
           respuesta=r"$\rho = \dfrac{m}{V} = \dfrac{400\,\text{g}}{176\,\text{cm}^3} \approx "
                     r"\num{2,3}\,\text{g/cm}^3$, muy por debajo de $\num{19,3}\,\text{g/cm}^3$: "
                     r"no es de oro puro (una figura de oro de $400\,\text{g}$ ocuparía solo unos "
                     r"$21\,\text{cm}^3$).",
           notas="Se añade la densidad del oro, que el ejercicio no da.",
           **comun("densidad"))
def _():
    rho = 400 * gram / (176 * centimeter**3)
    cerca(rho, Q(23, 10) * gram / centimeter**3, tol=0.02)
    assert float(convert_to(rho / (Q(193, 10) * gram / centimeter**3), [])) < 0.2
    cerca(400 * gram / (Q(193, 10) * gram / centimeter**3), 21 * centimeter**3, tol=0.02)


@ejercicio(id=f"{P}-002", tipo="calculo", dificultad=2, fuente=fuente(C1, "Ejercicios", "44"),
           enunciado=r"Un globo inflado se comprime, a temperatura constante, a la mitad de su "
                     r"volumen. ¿En cuánto se incrementa su presión?",
           respuesta=r"Por la ley de Boyle ($PV$ constante), la presión se duplica: aumenta en "
                     r"otro tanto de la presión inicial.",
           notas="Se añade «a temperatura constante», condición de la ley de Boyle.",
           **comun("gases"))
def _():
    P1, V1, P2 = symbols("P1 V1 P2", positive=True)
    assert solve(Eq(P1 * V1, P2 * V1 / 2), P2) == [2 * P1]


# ---------------------------------------------------------------- Cap. 2
C2 = "Cap. 2 Temperatura, calor y expansión"
CALOR = comun("calor y temperatura")
DILAT = comun("dilatación térmica")


@ejercicio(id=f"{P}-003", tipo="calculo", dificultad=1, fuente=fuente(C2, "Problemas", "1"),
           enunciado=r"¿Cuál será la temperatura final de una mezcla de $50\,\text{g}$ de agua a "
                     r"$20\,^{\circ}\text{C}$ y $50\,\text{g}$ de agua a $40\,^{\circ}\text{C}$?",
           respuesta=r"Como las masas son iguales, la temperatura final es el promedio: "
                     r"$30\,^{\circ}\text{C}$.", **CALOR)
def _():
    assert solve(Eq(50 * (T - 20), 50 * (40 - T)), T) == [30]


@ejercicio(id=f"{P}-004", tipo="calculo", dificultad=1, fuente=fuente(C2, "Problemas", "2"),
           enunciado=r"Si deseas elevar $20\,^{\circ}\text{C}$ la temperatura de $100\,\text{kg}$ "
                     r"de agua para tu baño, ¿cuánto calor se requiere? Da tu resultado en calorías "
                     r"y en joules.",
           respuesta=r"$Q = c\,m\,\Delta T = (1\,\text{cal/g}\,^{\circ}\text{C})"
                     r"(\num{100000}\,\text{g})(20\,^{\circ}\text{C}) = \num{2e6}\,\text{cal}$ "
                     r"$= \num{2000}\,\text{kcal} \approx \num{8,4e6}\,\text{J}$.",
           notas="En la guía: «calentar 100 kg de agua 20 °C»; se aclara que 20 °C es el aumento "
                 "de temperatura.", **CALOR)
def _():
    q = C_AGUA * 100 * kilogram * 20 * kelvin
    cerca(q, 2 * 10**6 * CAL, tol=Q(1, 10**9))
    cerca(q, Q(84, 10) * 10**6 * joule, tol=0.005)


@ejercicio(id=f"{P}-005", tipo="calculo", dificultad=2, fuente=fuente(C2, "Problemas", "3"),
           enunciado=r"La capacidad calorífica específica del cobre es "
                     r"$\num{0,092}\,\text{cal/g}\,^{\circ}\text{C}$. ¿Cuánto calor se requiere para "
                     r"subir la temperatura de una pieza de cobre de $10\,\text{g}$ de "
                     r"$0\,^{\circ}\text{C}$ a $100\,^{\circ}\text{C}$? ¿Cómo se compara con el "
                     r"necesario para calentar una masa igual de agua en la misma diferencia de "
                     r"temperaturas?",
           respuesta=r"$Q = (\num{0,092})(10)(100) = 92\,\text{cal}$. Para el agua se necesitan "
                     r"$(1)(10)(100) = \num{1000}\,\text{cal}$: unas 11 veces más que para el "
                     r"cobre.", **CALOR)
def _():
    cobre = Q(92, 1000) * CAL / (gram * kelvin) * 10 * gram * 100 * kelvin
    agua = C_AGUA * 10 * gram * 100 * kelvin
    cerca(cobre, 92 * CAL, tol=Q(1, 10**9))
    assert round(float(simplify(agua / cobre))) == 11


@ejercicio(id=f"{P}-006", tipo="calculo", dificultad=2, fuente=fuente(C2, "Problemas", "4"),
           enunciado=r"¿Cuál sería la temperatura final al mezclar $100\,\text{g}$ de agua a "
                     r"$25\,^{\circ}\text{C}$ con $75\,\text{g}$ de agua a $40\,^{\circ}\text{C}$? "
                     r"(Sugerencia: iguala el calor ganado por el agua fría con el calor perdido "
                     r"por el agua caliente.)",
           respuesta=r"$100(T - 25) = 75(40 - T) \Rightarrow 175\,T = \num{5500} \Rightarrow "
                     r"T \approx \num{31,4}\,^{\circ}\text{C}$.", **CALOR)
def _():
    (t,) = solve(Eq(100 * (T - 25), 75 * (40 - T)), T)
    assert t == Q(220, 7) and abs(float(t) - 31.4) < 0.05


@ejercicio(id=f"{P}-007", tipo="calculo", dificultad=2, fuente=fuente(C2, "Problemas", "5"),
           enunciado=r"¿Cuál será la temperatura final de $100\,\text{g}$ de agua a "
                     r"$20\,^{\circ}\text{C}$ cuando se sumergen en ella $100\,\text{g}$ de clavos "
                     r"de acero a $40\,^{\circ}\text{C}$? (El calor específico del acero es "
                     r"$\num{0,12}\,\text{cal/g}\,^{\circ}\text{C}$. Iguala el calor ganado por el "
                     r"agua y el calor perdido por los clavos.)",
           respuesta=r"$100(1)(T - 20) = 100(\num{0,12})(40 - T) \Rightarrow 112\,T = \num{2480} "
                     r"\Rightarrow T \approx \num{22,1}\,^{\circ}\text{C}$.", **CALOR)
def _():
    (t,) = solve(Eq(100 * (T - 20), 100 * Q(12, 100) * (40 - T)), T)
    assert t == Q(2480, 112) and abs(float(t) - 22.1) < 0.05


@ejercicio(id=f"{P}-008", tipo="calculo", dificultad=1, fuente=fuente(C2, "Problemas", "6"),
           enunciado=r"Imagina que una barra de $1\,\text{m}$ de longitud se dilata "
                     r"$\num{0,5}\,\text{cm}$ al calentarse. ¿Cuánto se dilatará una barra de "
                     r"$100\,\text{m}$ de longitud, del mismo material, al calentarla en igual "
                     r"forma?",
           respuesta=r"La dilatación es proporcional a la longitud ($\Delta L = L\alpha\Delta T$): "
                     r"$100 \times \num{0,5}\,\text{cm} = 50\,\text{cm}$.", **DILAT)
def _():
    alfa_dt = Q(5, 1000) * meter / meter                 # ΔL/L de la primera barra
    assert convert_to(100 * meter * alfa_dt, centimeter) == 50 * centimeter


@ejercicio(id=f"{P}-009", tipo="contexto", dificultad=2, fuente=fuente(C2, "Problemas", "7"),
           enunciado=r"Supón que el claro principal del puente Golden Gate, de "
                     r"$\num{1,3}\,\text{km}$ y hecho de acero "
                     r"($\alpha = \num{11e-6}\,/^{\circ}\text{C}$), no tuviera juntas de expansión. "
                     r"¿Cuánto aumentaría su longitud si su temperatura aumentara "
                     r"$15\,^{\circ}\text{C}$?",
           respuesta=r"$\Delta L = L\alpha\Delta T = (\num{1300}\,\text{m})(\num{11e-6}\,/"
                     r"^{\circ}\text{C})(15\,^{\circ}\text{C}) \approx \num{0,21}\,\text{m}$ "
                     r"(unos $21\,\text{cm}$).",
           notas="La guía no dice el material; se indica que es acero (α dado en la introducción "
                 "de los problemas).", **DILAT)
def _():
    cerca(1300 * meter * ALFA_ACERO * 15 * kelvin, Q(21, 100) * meter, tol=0.03)


@ejercicio(id=f"{P}-010", tipo="calculo", dificultad=2, fuente=fuente(C2, "Problemas", "8"),
           enunciado=r"Un alambre de acero de $\num{10,00}\,\text{m}$ sostiene una lenteja de "
                     r"péndulo en su extremo. ¿Cuántos milímetros se alarga cuando su temperatura "
                     r"aumenta $\num{20,0}\,^{\circ}\text{C}$? "
                     r"($\alpha_{\text{acero}} = \num{11e-6}\,/^{\circ}\text{C}$.)",
           respuesta=r"$\Delta L = (\num{10,00}\,\text{m})(\num{11e-6})(\num{20,0}) = "
                     r"\num{2,20e-3}\,\text{m} = \num{2,20}\,\text{mm}$.", **DILAT)
def _():
    dl = convert_to(10 * meter * ALFA_ACERO * 20 * kelvin, meter)
    assert dl == Q(22, 10000) * meter


@ejercicio(id=f"{P}-011", tipo="calculo", dificultad=2, fuente=fuente(C2, "Problemas", "9"),
           enunciado=r"Se calientan dos bandas de dimensiones iguales, una de aluminio "
                     r"($\alpha = \num{24e-6}\,/^{\circ}\text{C}$) y la otra de acero "
                     r"($\alpha = \num{11e-6}\,/^{\circ}\text{C}$). ¿Cuál se dilata más? ¿En qué "
                     r"factor es mayor una dilatación que la otra?",
           respuesta=r"La de aluminio, $\dfrac{24}{11} \approx \num{2,2}$ veces más que la de "
                     r"acero.", **DILAT)
def _():
    assert ALFA_AL / ALFA_ACERO == Q(24, 11) and abs(float(Q(24, 11)) - 2.2) < 0.02


@ejercicio(id=f"{P}-012", tipo="contexto", dificultad=3, fuente=fuente(C2, "Problemas", "10"),
           enunciado=r"Un tubo de acero de \num{40000} kilómetros forma un anillo que se ajusta bien "
                     r"a la circunferencia de la Tierra. Imagina que las personas junto a él "
                     r"respiran para calentarlo con su aliento y aumentar su temperatura "
                     r"$1\,^{\circ}\text{C}$. El tubo se hace más largo y ya no queda ajustado. ¿A "
                     r"qué distancia sube sobre el nivel del suelo? (Ten en cuenta solo la "
                     r"expansión de su distancia radial al centro de la Tierra, y usa "
                     r"$C = 2\pi r$.)",
           respuesta=r"$\Delta C = (\num{4e7}\,\text{m})(\num{11e-6})(1) = 440\,\text{m}$, así "
                     r"que $\Delta r = \dfrac{\Delta C}{2\pi} = \dfrac{440\,\text{m}}{2\pi} "
                     r"\approx 70\,\text{m}$.", **DILAT)
def _():
    dc = convert_to(40000 * 1000 * meter * ALFA_ACERO * 1 * kelvin, meter)
    assert dc == 440 * meter
    cerca(dc / (2 * pi), 70 * meter, tol=0.001)


# ---------------------------------------------------------------- Cap. 3
C3 = "Cap. 3 Transferencia de calor"
TRANSF = comun("transferencia de calor")


@ejercicio(id=f"{P}-013", tipo="contexto", dificultad=2, fuente=fuente(C3, "Problemas", "1a"),
           enunciado=r"Julián quema un maní de $\num{0,6}\,\text{g}$ bajo $50\,\text{g}$ de agua, "
                     r"que aumenta su temperatura de $22\,^{\circ}\text{C}$ a "
                     r"$50\,^{\circ}\text{C}$. Suponiendo que solo el $40\,\%$ de la energía del "
                     r"maní llega al agua, ¿cuál es el valor alimenticio del maní en calorías?",
           respuesta=r"El agua recibe $Q = (1)(50)(28) = \num{1400}\,\text{cal}$, que es el "
                     r"$40\,\%$ de la energía del maní: $\dfrac{\num{1400}}{\num{0,4}} = "
                     r"\num{3500}\,\text{cal} = \num{3,5}\,\text{kcal}$ (\num{3,5} «Calorías» de "
                     r"las etiquetas de alimentos).",
           notas="En la guía: «cacahuate» (se escribe maní) y «Suponiendo una eficiencia de 40%»; "
                 "se precisa qué significa esa eficiencia.", **TRANSF)
def _():
    q_agua = C_AGUA * 50 * gram * 28 * kelvin
    cerca(q_agua / Q(4, 10), 3500 * CAL, tol=Q(1, 10**9))


@ejercicio(id=f"{P}-014", tipo="contexto", dificultad=2, fuente=fuente(C3, "Problemas", "1b"),
           enunciado=r"Con los datos anteriores (el maní de $\num{0,6}\,\text{g}$ libera "
                     r"\num{3500} cal), ¿cuál es su valor alimenticio en calorías por gramo?",
           respuesta=r"$\dfrac{\num{3500}\,\text{cal}}{\num{0,6}\,\text{g}} \approx "
                     r"\num{5800}\,\text{cal/g} \approx \num{5,8}\,\text{kcal/g}$.", **TRANSF)
def _():
    cerca(3500 * CAL / (Q(6, 10) * gram), 5800 * CAL / gram, tol=0.01)


@ejercicio(id=f"{P}-015", tipo="contexto", dificultad=3, fuente=fuente(C3, "Problemas", "2"),
           enunciado=r"El decaimiento radiactivo del granito y otras rocas del interior de la "
                     r"Tierra libera, en promedio, unos $\num{0,03}\,\text{J}$ por kilogramo de roca "
                     r"cada año. ¿Cuántos años se requieren para que un trozo de granito aislado "
                     r"térmicamente aumente su temperatura en $500\,^{\circ}\text{C}$? Supón que su "
                     r"capacidad calorífica específica es $800\,\text{J/kg}\,^{\circ}\text{C}$.",
           respuesta=r"Cada kilogramo necesita $Q = (800)(1)(500) = \num{4e5}\,\text{J}$; a "
                     r"$\num{0,03}\,\text{J}$ por año: $\dfrac{\num{4e5}}{\num{0,03}} \approx "
                     r"\num{1,3e7}$ años (unos 13 millones de años).", **TRANSF)
def _():
    q = 800 * joule / (kilogram * kelvin) * 1 * kilogram * 500 * kelvin
    tiempo = q / (Q(3, 100) * joule / year)
    cerca(tiempo, Q(13, 10) * 10**7 * year, tol=0.03)


@ejercicio(id=f"{P}-016", tipo="contexto", dificultad=3, fuente=fuente(C3, "Problemas", "3"),
           enunciado=r"Al introducir un clavo en la madera, el clavo se calienta. Supón que el "
                     r"martillo ejerce una fuerza promedio de $500\,\text{N}$ sobre un clavo de "
                     r"acero de $6\,\text{cm}$ y $5\,\text{g}$ al clavarlo, y que todo el trabajo "
                     r"calienta el clavo. Calcula el aumento de temperatura del clavo. (Capacidad "
                     r"calorífica específica del acero: $450\,\text{J/kg}\,^{\circ}\text{C}$.)",
           respuesta=r"$W = F\,d = (500\,\text{N})(\num{0,06}\,\text{m}) = 30\,\text{J}$; "
                     r"$\Delta T = \dfrac{W}{c\,m} = \dfrac{30}{(450)(\num{0,005})} \approx "
                     r"13\,^{\circ}\text{C}$.",
           notas="La guía no da la masa del clavo (sin ella el problema no tiene solución); se "
                 "añaden 5 g y la suposición de que todo el trabajo calienta el clavo (en "
                 "realidad parte calienta la madera).", **TRANSF)
def _():
    w = 500 * newton * 6 * centimeter
    assert convert_to(w, joule) == 30 * joule
    dt = w / (450 * joule / (kilogram * kelvin) * 5 * gram)
    cerca(dt, Q(133, 10) * kelvin, tol=0.003)


@ejercicio(id=f"{P}-017", tipo="contexto", dificultad=3, fuente=fuente(C3, "Problemas", "4"),
           enunciado=r"Un recipiente con agua caliente a $80\,^{\circ}\text{C}$ se enfría a "
                     r"$79\,^{\circ}\text{C}$ en $15\,\text{s}$ cuando se coloca en un recinto que "
                     r"está a $20\,^{\circ}\text{C}$. Aplica la ley de Newton del enfriamiento para "
                     r"estimar el tiempo que tardará en enfriarse de $50$ a $49\,^{\circ}\text{C}$. "
                     r"Y después, el tiempo que tardará en enfriarse de $40$ a "
                     r"$39\,^{\circ}\text{C}$.",
           respuesta=r"La rapidez de enfriamiento es proporcional a la diferencia de temperatura "
                     r"con el recinto: unos $60\,^{\circ}\text{C}$ al principio, unos "
                     r"$30\,^{\circ}\text{C}$ y unos $20\,^{\circ}\text{C}$ después. Así, bajar "
                     r"un grado tarda el doble, unos $30\,\text{s}$, y luego el triple, unos "
                     r"$45\,\text{s}$.", **TRANSF)
def _():
    # tiempo ∝ 1 / (diferencia media con el recinto); de 80 a 79 °C la diferencia media es 59,5
    tiempo = lambda t_alto: 15 * (Q(795, 10) - 20) / (t_alto - Q(1, 2) - 20)
    cerca(tiempo(50) * second, 30 * second, tol=0.02)
    cerca(tiempo(40) * second, 45 * second, tol=0.02)


@ejercicio(id=f"{P}-018", tipo="contexto", dificultad=3, fuente=fuente(C3, "Problemas", "5"),
           enunciado=r"En un recinto a $25\,^{\circ}\text{C}$, el café caliente de un termo se "
                     r"enfría de $75$ a $50\,^{\circ}\text{C}$ en ocho horas. ¿Cuál será su "
                     r"temperatura después de otras ocho horas?",
           respuesta=r"La diferencia con el recinto pasó de $50\,^{\circ}\text{C}$ a "
                     r"$25\,^{\circ}\text{C}$ (se redujo a la mitad) en 8 horas. En las siguientes "
                     r"8 horas vuelve a reducirse a la mitad, a $\num{12,5}\,^{\circ}\text{C}$: el "
                     r"café quedará a unos $\num{37,5}\,^{\circ}\text{C}$.", **TRANSF)
def _():
    from sympy import exp, log
    k = log(2) / 8                                       # ΔT = 50·e^(−k t), mitad a las 8 h
    temperatura = lambda t: 25 + 50 * exp(-k * t)
    assert simplify(temperatura(8)) == 50
    assert simplify(temperatura(16)) == Q(75, 2)


@ejercicio(id=f"{P}-019", tipo="contexto", dificultad=2, fuente=fuente(C3, "Problemas", "6"),
           enunciado=r"En determinado lugar, la potencia solar por unidad de área que llega a la "
                     r"superficie terrestre es de $200\,\text{W/m}^2$, en promedio, en un día de "
                     r"24 horas. Si vives en una casa cuyas necesidades promedio de potencia son "
                     r"$3\,\text{kW}$, y puedes convertir la energía solar en energía eléctrica con "
                     r"una eficiencia del $10\,\%$, ¿de qué extensión será el área del colector "
                     r"para satisfacer todas las necesidades de energía de tu casa? ¿Cabría en tu "
                     r"patio?",
           respuesta=r"Cada metro cuadrado aporta $(\num{0,10})(200) = 20\,\text{W}$ eléctricos; "
                     r"se necesitan $\dfrac{\num{3000}\,\text{W}}{20\,\text{W/m}^2} = "
                     r"150\,\text{m}^2$ (un cuadrado de unos $12\,\text{m}$ de lado): no cabe en "
                     r"el patio de la mayoría de las casas.", **TRANSF)
def _():
    area = 3000 * watt / (Q(1, 10) * 200 * watt / meter**2)
    assert convert_to(area, meter**2) == 150 * meter**2
    assert 12**2 < 150 < 13**2


# ---------------------------------------------------------------- Cap. 4
C4 = "Cap. 4 Cambio de fase"
FASE = comun("cambios de fase")
L_FUS, L_VAP = 80 * CAL / gram, 540 * CAL / gram

for n, lit, texto, calorias in [
        (20, "1a", r"1 kg de hielo a $0\,^{\circ}\text{C}$ en agua helada a "
                   r"$0\,^{\circ}\text{C}$", 80),
        (21, "1b", r"1 kg de agua helada a $0\,^{\circ}\text{C}$ en 1 kg de agua hirviente a "
                   r"$100\,^{\circ}\text{C}$", 100),
        (22, "1c", r"1 kg de agua hirviente a $100\,^{\circ}\text{C}$ en 1 kg de vapor a "
                   r"$100\,^{\circ}\text{C}$", 540),
        (23, "1d", r"1 kg de hielo a $0\,^{\circ}\text{C}$ en 1 kg de vapor a "
                   r"$100\,^{\circ}\text{C}$", 720)]:
    procedimiento = {
        "1a": r"$Q = mL_f = (1\,\text{kg})(80\,\text{kcal/kg}) = 80\,\text{kcal}$",
        "1b": r"$Q = cm\Delta T = (1\,\text{kcal/kg}\,^{\circ}\text{C})(1\,\text{kg})"
              r"(100\,^{\circ}\text{C}) = 100\,\text{kcal}$",
        "1c": r"$Q = mL_v = (1\,\text{kg})(540\,\text{kcal/kg}) = 540\,\text{kcal}$",
        "1d": r"$Q = 80 + 100 + 540 = 720\,\text{kcal}$ (fundir, calentar y evaporar)"}[lit]

    @ejercicio(id=f"{P}-{n:03d}", tipo="calculo", dificultad=1 if lit != "1d" else 2,
               fuente=fuente(C4, "Problemas", lit),
               enunciado=r"Con $Q = cm\Delta T$ ($c_{\text{agua}} = 1\,\text{cal/g}\,^{\circ}"
                         r"\text{C}$) y $Q = mL$ (calor de fusión del agua $80\,\text{cal/g}$, "
                         r"de vaporización $540\,\text{cal/g}$), determina la cantidad de calorías "
                         r"para convertir " + texto + ".",
               respuesta=procedimiento + ".", **FASE)
    def _(lit=lit, calorias=calorias):
        m = 1000 * gram
        pasos = {"1a": m * L_FUS, "1b": C_AGUA * m * 100 * kelvin, "1c": m * L_VAP}
        pasos["1d"] = pasos["1a"] + pasos["1b"] + pasos["1c"]
        cerca(pasos[lit], calorias * 1000 * CAL, tol=Q(1, 10**9))


@ejercicio(id=f"{P}-024", tipo="calculo", dificultad=3, fuente=fuente(C4, "Problemas", "2"),
           enunciado=r"La capacidad calorífica específica aproximada del hielo es "
                     r"$\num{0,5}\,\text{cal/g}\,^{\circ}\text{C}$. Suponiendo que permanece en ese "
                     r"valor hasta el cero absoluto, calcula la cantidad de calorías que se "
                     r"necesitarían para convertir un cubo de hielo de $1\,\text{g}$ en el cero "
                     r"absoluto ($-273\,^{\circ}\text{C}$) en agua hirviente. ¿Cómo se compara esa "
                     r"cantidad con la necesaria para convertir el mismo gramo de agua hirviente a "
                     r"$100\,^{\circ}\text{C}$ en vapor a $100\,^{\circ}\text{C}$?",
           respuesta=r"Calentar el hielo: $(\num{0,5})(1)(273) = \num{136,5}\,\text{cal}$; "
                     r"fundirlo: $80\,\text{cal}$; calentar el agua hasta $100\,^{\circ}\text{C}$: "
                     r"$100\,\text{cal}$. Total: $\num{316,5}\,\text{cal} \approx 317\,\text{cal}$, "
                     r"menos que las $540\,\text{cal}$ para evaporar ese gramo (casi el "
                     r"$60\,\%$).", **FASE)
def _():
    total = (Q(1, 2) * CAL / (gram * kelvin) * gram * 273 * kelvin + gram * L_FUS
             + C_AGUA * gram * 100 * kelvin)
    cerca(total, Q(6330, 20) * CAL, tol=Q(1, 10**9))
    assert abs(float(simplify(total / (gram * L_VAP))) - 0.59) < 0.01


@ejercicio(id=f"{P}-025", tipo="calculo", dificultad=3, fuente=fuente(C4, "Problemas", "3"),
           enunciado=r"Calcula la masa de hielo a $0\,^{\circ}\text{C}$ que pueden fundir "
                     r"$10\,\text{g}$ de vapor a $100\,^{\circ}\text{C}$.",
           respuesta=r"El vapor, al condensarse, cede $(10)(540) = \num{5400}\,\text{cal}$ y, al "
                     r"enfriarse de 100 a $0\,^{\circ}\text{C}$, otras \num{1000} cal: en total "
                     r"\num{6400} cal, que funden $\dfrac{\num{6400}}{80} = 80\,\text{g}$ de "
                     r"hielo.", **FASE)
def _():
    cedido = 10 * gram * L_VAP + C_AGUA * 10 * gram * 100 * kelvin
    cerca(cedido / L_FUS, 80 * gram, tol=Q(1, 10**9))


@ejercicio(id=f"{P}-026", tipo="calculo", dificultad=2, fuente=fuente(C4, "Problemas", "4"),
           enunciado=r"Si se vierten $50\,\text{g}$ de agua caliente a $80\,^{\circ}\text{C}$ en "
                     r"una cavidad de un bloque de hielo muy grande a $0\,^{\circ}\text{C}$, ¿cuál "
                     r"será la temperatura final del agua en la cavidad? ¿Cuánto hielo se debe "
                     r"fundir para enfriar el agua a esa temperatura?",
           respuesta=r"El bloque es muy grande, así que el agua termina a $0\,^{\circ}\text{C}$. "
                     r"Cede $(1)(50)(80) = \num{4000}\,\text{cal}$, que funden "
                     r"$\dfrac{\num{4000}}{80} = 50\,\text{g}$ de hielo.", **FASE)
def _():
    cerca(C_AGUA * 50 * gram * 80 * kelvin / L_FUS, 50 * gram, tol=Q(1, 10**9))


@ejercicio(id=f"{P}-027", tipo="calculo", dificultad=2, fuente=fuente(C4, "Problemas", "5"),
           enunciado=r"Un trozo de hierro de $50\,\text{g}$ a $80\,^{\circ}\text{C}$ se deja caer "
                     r"en una cavidad de un bloque de hielo muy grande a $0\,^{\circ}\text{C}$. "
                     r"¿Cuántos gramos de hielo se fundirán? (La capacidad calorífica específica "
                     r"del hierro es $\num{0,11}\,\text{cal/g}\,^{\circ}\text{C}$.)",
           respuesta=r"El hierro cede $(\num{0,11})(50)(80) = 440\,\text{cal}$, que funden "
                     r"$\dfrac{440}{80} = \num{5,5}\,\text{g}$ de hielo.", **FASE)
def _():
    cedido = Q(11, 100) * CAL / (gram * kelvin) * 50 * gram * 80 * kelvin
    cerca(cedido / L_FUS, Q(55, 10) * gram, tol=Q(1, 10**9))


@ejercicio(id=f"{P}-028", tipo="contexto", dificultad=3, fuente=fuente(C4, "Problemas", "6"),
           enunciado=r"Calcula la altura desde donde se debe dejar caer un bloque de hielo a "
                     r"$0\,^{\circ}\text{C}$ para que se funda totalmente por el impacto en el "
                     r"suelo. Imagina que no hay resistencia del aire y que toda la energía se usa "
                     r"en fundir el hielo. Sugerencia: iguala la energía potencial gravitacional "
                     r"$mgh$ con $mL$, donde el calor de fusión es "
                     r"$L = \num{335000}\,\text{J/kg}$. ¿Ves por qué el resultado no depende de la "
                     r"masa?",
           respuesta=r"$mgh = mL \Rightarrow h = \dfrac{L}{g} = \dfrac{\num{335000}\,\text{J/kg}}"
                     r"{\num{9,8}\,\text{m/s}^2} \approx \num{34000}\,\text{m}$ (unos "
                     r"$34\,\text{km}$). La masa aparece en los dos lados y se cancela.", **FASE)
def _():
    m = symbols("m", positive=True)
    h = symbols("h", positive=True)
    (altura,) = solve(Eq(m * Q(98, 10) * h, m * 335000), h)
    assert altura.free_symbols == set()                  # no depende de m
    cerca(altura * meter, 34000 * meter, tol=0.006)
    cerca(335000 * joule / kilogram / G, 34000 * meter, tol=0.006)


@ejercicio(id=f"{P}-029", tipo="contexto", dificultad=3, fuente=fuente(C4, "Problemas", "7"),
           enunciado=r"Una esfera de hierro de $10\,\text{kg}$ se deja caer desde una altura de "
                     r"$100\,\text{m}$ hasta el pavimento. Si la mitad del calor generado se emplea "
                     r"en calentar la esfera, calcula su aumento de temperatura. (Capacidad "
                     r"calorífica específica del hierro: $450\,\text{J/kg}\,^{\circ}\text{C}$.) "
                     r"¿Por qué la respuesta es igual para una esfera de cualquier masa?",
           respuesta=r"$\tfrac{1}{2}mgh = mc\Delta T \Rightarrow \Delta T = \dfrac{gh}{2c} = "
                     r"\dfrac{(\num{9,8})(100)}{2(450)} \approx \num{1,09}\,^{\circ}\text{C}$. La "
                     r"masa se cancela: una esfera más pesada libera más energía, pero también "
                     r"necesita más para calentarse.", **FASE)
def _():
    dt = Q(1, 2) * 10 * kilogram * G * 100 * meter / (10 * kilogram * 450 * joule /
                                                     (kilogram * kelvin))
    cerca(dt, Q(109, 100) * kelvin, tol=0.002)


@ejercicio(id=f"{P}-030", tipo="calculo", dificultad=2, fuente=fuente(C4, "Problemas", "8"),
           enunciado=r"El calor de evaporación del alcohol etílico es, aproximadamente, "
                     r"$200\,\text{cal/g}$. Si se dejaran evaporar $2\,\text{kg}$ de alcohol en un "
                     r"refrigerador, ¿cuántos gramos de hielo se formarían con agua a "
                     r"$0\,^{\circ}\text{C}$?",
           respuesta=r"El alcohol absorbe $(\num{2000})(200) = \num{400000}\,\text{cal}$; al "
                     r"quitarle esas calorías al agua a $0\,^{\circ}\text{C}$ se congelan "
                     r"$\dfrac{\num{400000}}{80} = \num{5000}\,\text{g}$ ($5\,\text{kg}$) de "
                     r"hielo.", **FASE)
def _():
    cerca(2000 * gram * 200 * CAL / gram / L_FUS, 5000 * gram, tol=Q(1, 10**9))


# ---------------------------------------------------------------- Cap. 5
C5 = "Cap. 5 Termodinámica"
TERMO = comun("termodinámica")


@ejercicio(id=f"{P}-031", tipo="calculo", dificultad=2, fuente=fuente(C5, "Problemas", "1"),
           enunciado=r"Durante cierto proceso termodinámico, una muestra de gas se expande y se "
                     r"enfría, y su energía interna se reduce $\num{3000}\,\text{J}$, sin haberle "
                     r"agregado ni retirado calor. ¿Cuánto trabajo se efectúa en este proceso?",
           respuesta=r"Por la primera ley, $Q = \Delta U + W$. Con $Q = 0$ y "
                     r"$\Delta U = -\num{3000}\,\text{J}$: el gas efectúa un trabajo "
                     r"$W = \num{3000}\,\text{J}$ (proceso adiabático).", **TERMO)
def _():
    W = symbols("W")
    assert solve(Eq(0, -3000 + W), W) == [3000]


@ejercicio(id=f"{P}-032", tipo="calculo", dificultad=2, fuente=fuente(C5, "Problemas", "2"),
           enunciado=r"¿Cuál es la eficiencia ideal de un motor de automóvil cuando el combustible "
                     r"se calienta a $\num{2700}\,\text{K}$ y el aire del exterior está a "
                     r"$270\,\text{K}$?",
           respuesta=r"$e = 1 - \dfrac{T_{\text{fría}}}{T_{\text{caliente}}} = 1 - "
                     r"\dfrac{270}{\num{2700}} = \num{0,9}$, es decir, $90\,\%$.", **TERMO)
def _():
    assert 1 - Q(270, 2700) == Q(9, 10)


@ejercicio(id=f"{P}-033", tipo="contexto", dificultad=2, fuente=fuente(C5, "Problemas", "3"),
           enunciado=r"Calcula la eficiencia de Carnot de una planta de energía eléctrica OTEC que "
                     r"funciona con la diferencia de temperatura entre el agua del fondo, a "
                     r"$4\,^{\circ}\text{C}$, y la de la superficie, a $25\,^{\circ}\text{C}$.",
           respuesta=r"Con temperaturas absolutas: $e = 1 - \dfrac{277\,\text{K}}{298\,\text{K}} "
                     r"\approx \num{0,07}$, apenas un $7\,\%$.", **TERMO)
def _():
    e = 1 - Q(27715, 100) / Q(29815, 100)
    assert abs(float(e) - 0.070) < 0.001
    assert abs(float(1 - Q(277, 298)) - 0.070) < 0.001


@ejercicio(id=f"{P}-034", tipo="contexto", dificultad=3, fuente=fuente(C5, "Problemas", "4"),
           enunciado=r"En un día frío a $10\,^{\circ}\text{C}$, tu amigo, al que le gusta el clima "
                     r"frío, te dice que le gustaría que hubiera el doble de frío. Si lo interpretas "
                     r"literalmente, ¿más o menos a qué temperatura debería estar?",
           respuesta=r"«El doble de frío» significa la mitad de la temperatura absoluta: "
                     r"$10\,^{\circ}\text{C} = 283\,\text{K}$, y la mitad es unos "
                     r"$141\,\text{K}$, o sea, unos $-132\,^{\circ}\text{C}$.", **TERMO)
def _():
    mitad = Q(28315, 100) / 2
    assert abs(float(mitad) - 141.6) < 0.1
    assert abs(float(mitad - Q(27315, 100)) - (-131.6)) < 0.1   # ≈ −132 °C


@ejercicio(id=f"{P}-035", tipo="contexto", dificultad=3, fuente=fuente(C5, "Problemas", "5"),
           enunciado=r"Imagina una bolsa de tintorería muy grande, llena de aire a "
                     r"$-35\,^{\circ}\text{C}$, flotando como un globo atado con un cordón, a "
                     r"$10\,\text{km}$ del suelo. Estima su temperatura si de repente tiraras del "
                     r"cordón y la bajaras hasta la superficie de la Tierra. (El aire que se "
                     r"comprime adiabáticamente se calienta unos $10\,^{\circ}\text{C}$ por cada "
                     r"kilómetro que desciende.)",
           respuesta=r"Al bajar $10\,\text{km}$ se comprime adiabáticamente y se calienta "
                     r"$10 \times 10 = 100\,^{\circ}\text{C}$: llegaría a unos "
                     r"$-35 + 100 = 65\,^{\circ}\text{C}$.",
           notas="Se recuerda en el enunciado la tasa de 10 °C por kilómetro, que la guía da en "
                 "la teoría del proceso adiabático.", **TERMO)
def _():
    assert -35 + 10 * 10 == 65


@ejercicio(id=f"{P}-036", tipo="contexto", dificultad=3, fuente=fuente(C5, "Problemas", "6"),
           enunciado=r"Una planta de energía eléctrica tiene una eficiencia de \num{0,4}, genera "
                     r"$\num{1e8}\,\text{W}$ de potencia eléctrica y disipa "
                     r"$\num{1,5e8}\,\text{W}$ de energía térmica en el agua de enfriamiento que "
                     r"pasa por ella. Sabiendo que el calor específico del agua es "
                     r"$\num{4184}\,\text{J/kg}\,^{\circ}\text{C}$, calcula cuántos kilogramos de "
                     r"agua pasan por la planta cada segundo, si esa agua se calienta "
                     r"$3\,^{\circ}\text{C}$.",
           respuesta=r"Cada segundo el agua recibe $\num{1,5e8}\,\text{J}$: "
                     r"$m = \dfrac{Q}{c\,\Delta T} = \dfrac{\num{1,5e8}}{(\num{4184})(3)} \approx "
                     r"\num{1,2e4}\,\text{kg}$ por segundo (unos \num{12000} kg/s).",
           notas="En la guía: «genera 108 W» (el exponente se perdió); son 10^8 W, coherente con "
                 "la eficiencia 0,4 = 10^8/(10^8 + 1,5·10^8).", **TERMO)
def _():
    assert Q(10**8, 10**8 + Q(15, 10) * 10**8) == Q(2, 5)      # eficiencia 0,4
    flujo = Q(15, 10) * 10**8 * watt / (4184 * joule / (kilogram * kelvin) * 3 * kelvin)
    cerca(flujo, Q(12, 10) * 10**4 * kilogram / second, tol=0.01)


for n, lit, t_fria, t_caliente, trabajo, trabajo_tex, lugar in [
        (37, "7a", 295, 308, Q(13, 295), r"\num{0,044}",
         r"del interior de un recinto a $T_{\text{fría}} = 295\,\text{K}$ al exterior, con "
         r"$T_{\text{caliente}} = 308\,\text{K}$"),
        (38, "7b", 173, 293, Q(120, 173), r"\num{0,69}",
         r"del interior de un congelador de laboratorio con $T_{\text{fría}} = 173\,\text{K}$ al "
         r"recinto, que está a $T_{\text{caliente}} = 293\,\text{K}$"),
        (39, "7c", 4, 300, 74, r"74",
         r"de un refrigerador de helio cuya temperatura interna es $T_{\text{fría}} = "
         r"4\,\text{K}$ a un recinto donde $T_{\text{caliente}} = 300\,\text{K}$")]:
    @ejercicio(id=f"{P}-{n:03d}", tipo="calculo", dificultad=2,
               fuente=fuente(C5, "Problemas", lit),
               enunciado=r"Una bomba de calor lleva energía de un lugar frío a otro más caliente "
                         r"(es el corazón de un refrigerador o de un aire acondicionado). El "
                         r"trabajo mínimo necesario es $W_{\text{mín}} = (\text{energía "
                         r"transferida}) \times \dfrac{T_{\text{caliente}} - T_{\text{fría}}}"
                         r"{T_{\text{fría}}}$. Calcula el trabajo mínimo necesario para mover "
                         r"$1\,\text{J}$ de energía " + lugar + "."
                         + (r" Comenta las diferencias entre los tres casos." if lit == "7c"
                            else ""),
               respuesta=rf"$W = (1\,\text{{J}})\,\dfrac{{{t_caliente} - {t_fria}}}{{{t_fria}}} "
                         rf"\approx {trabajo_tex}\,\text{{J}}$."
                         + (r" Cuanto más fría es la fuente de la que se extrae la energía, "
                            r"más trabajo cuesta: mover 1 J desde 4 K cuesta 74 J, unas "
                            r"\num{1700} veces más que en el aire acondicionado."
                            if lit == "7c" else ""),
               notas="En la guía la fórmula aparece como «(Tcaliente _ Tfría)/Tfría»: el «_» es "
                     "un signo menos.", **TERMO)
    def _(t_fria=t_fria, t_caliente=t_caliente, trabajo=trabajo):
        w = 1 * joule * Q(t_caliente - t_fria, t_fria)
        assert w == trabajo * joule
        if t_fria == 295:
            assert abs(float(trabajo) - 0.044) < 0.0005
        if t_fria == 173:
            assert abs(float(trabajo) - 0.69) < 0.005
        if t_fria == 4:
            assert 1650 < float(trabajo / Q(13, 295)) < 1700    # «unas 1700 veces»


@ejercicio(id=f"{P}-040", tipo="argumentacion", dificultad=2, fuente=fuente(C5, "Problemas", "8"),
           enunciado=r"Elabora una tabla de todas las combinaciones de números que puedas obtener "
                     r"al lanzar dos dados. Tu amigo dice: «Ya sé que el siete es el número más "
                     r"probable cuando se tiran dos dados. Pero, ¿por qué siete?». Con tu tabla, "
                     r"explícale por qué, relacionándolo con la idea de la termodinámica de que "
                     r"los casos más probables son los que se pueden formar de más maneras.",
           respuesta=r"Hay $6 \times 6 = 36$ combinaciones. La suma 7 se forma de 6 maneras "
                     r"(1+6, 2+5, 3+4, 4+3, 5+2, 6+1), más que cualquier otra suma (el 2 y el 12, "
                     r"de una sola manera). Igual que en termodinámica, el resultado más probable "
                     r"es el que corresponde a más arreglos posibles (el mayor desorden).",
           **TERMO)
def _():
    from collections import Counter
    sumas = Counter(a + b for a, b in product(range(1, 7), repeat=2))
    assert sum(sumas.values()) == 36 and sumas[7] == 6
    assert max(sumas, key=sumas.get) == 7 and sumas[2] == sumas[12] == 1
