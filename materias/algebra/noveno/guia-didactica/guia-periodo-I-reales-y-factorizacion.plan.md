# Plan de la guía — Álgebra 9° · Trimestre I (etapas A y B)

> **BORRADOR — generación rápida (2026-09-14/15).** Etapas A, B y C del skill `crear-guia` en
> una sola pasada, a pedido, **sin las revisiones 1 y 2 de la docente**. El plan del trimestre
> (`curriculo/plan-anual.md`) es todavía una **propuesta**: sus filas 005–024 no están en
> `programacion.csv`. Si la docente cambia temas o el hilo, se rehace esta guía.
>
> **Regla de ejercicios (2026-09-15):** la guía usa **solo ejercicios que ya estaban en el
> banco** (verificados), salvo un tema para el que el banco no tenga nada: aquí, solo las
> **fracciones algebraicas** (2 ejercicios nuevos, marcados **NUEVO** abajo). Lo demás que el
> banco no cubre queda como pendiente (ver «Evidencias sin ejercicios»).

## Datos

| | |
|---|---|
| Asignatura | Álgebra |
| Grado | 9° |
| Trimestre | I (semanas 03–12; sesiones 005–024 propuestas en `plan-anual.md`) |
| Archivo | `guia-periodo-I-reales-y-factorizacion.tex` |
| Título | El libro que le dio nombre al álgebra |
| Hilo | **Al-Juarismi y el nacimiento del álgebra** (opción A de `plan-anual.md`), con la tablilla YBC 7289 (opción B) como apertura del tema 1 |
| Registro | Juvenil (7°–11°): definiciones y notación, citas con fuente, justificar y generalizar |

## Por qué este hilo

- **Conecta con la matemática, no la decora.** Al-Juarismi resolvía ecuaciones con cuadrados y
  rectángulos: su «completar el cuadrado» es el modelo de área de (a + b)², corazón del tema 2;
  su libro transforma igualdades sin cambiar su valor (DBA 2), que es el tema 3.
- **Da la representación geométrica que pide el DBA 1** y la diferencia entre exactitud y
  aproximación: la tablilla babilónica da √2 con seis cifras correctas, pero no es √2.
- **No repite a 8°** («La cacería de π»: Pitágoras, Arquímedes, Hipatia, Lambert) ni a Cálculo
  11° (Hipaso y el infinito), y continúa en el trimestre III (completar el cuadrado → fórmula
  general). El banco ya tenía una pregunta de Al-Juarismi (`producto-polinomios-8-124`).
- **Descartada C (RSA):** factoriza enteros, no polinomios; la analogía confunde en 9°.

**Correcciones a la propuesta de `plan-anual.md`:** (1) «hacia el año 820» no se confirmó en una
fuente académica accesible (Britannica e Iranica rechazaron la consulta); la guía dice «a
comienzos del siglo IX, bajo el califa al-Mamún, que gobernó desde 813», confirmado en MacTutor,
y la dedicatoria está en el propio libro (Rosen, p. 3). (2) YBC 7289 no se data «1800–1600
a. C.»: Fowler y Robson solo la sitúan en el primer tercio del segundo milenio a. C. (periodo
paleobabilónico). (3) El valor 1;24,51,10 = 1,41421296… sí se confirma.

## DBA y evidencias

Fuente: `dba/matematicas/grados/grado09.tex` (texto literal).

**DBA 1** — «Utiliza los números reales (sus operaciones, relaciones y propiedades) para
resolver problemas con expresiones polinómicas.»

| Evidencia | Tema | Ejercicios del banco |
|---|---|---|
| Considera el error que genera la aproximación de un número real a partir de números racionales. | 1 | irracionales-8-013 |
| Identifica la diferencia entre exactitud y aproximación en las diferentes representaciones de los números reales. | 1 | irracionales-8-013; medidas-con-radicales-8-002 (exacto y aproximado) |
| Construye representaciones geométricas y numéricas de los números reales (con decimales, raíces, razones, y otros símbolos) y realiza conversiones entre ellas. | 1, 2 | numeros-reales-8-013; factorizacion-8-264, -262, -158 (modelos de área) |

**DBA 2** — «Propone y desarrolla expresiones algebraicas en el conjunto de los números reales y
utiliza las propiedades de la igualdad y de orden para determinar el conjunto solución de
relaciones entre tales expresiones.»

| Evidencia | Tema | Ejercicios del banco |
|---|---|---|
| Identifica y utiliza múltiples representaciones de números reales para realizar transformaciones y comparaciones entre expresiones algebraicas. | 2, 3 | productos notables y factorización (abajo); fracciones-algebraicas-9-001, -002 (**NUEVOS**) |
| Establece conjeturas al resolver una situación problema, apoyado en propiedades y relaciones entre números reales. | 2, 3 | factorizacion-8-158; icfes-cuadernillo-2026-031 |
| Determina y describe relaciones al comparar características de gráficas y expresiones algebraicas o funciones. | — | no es del trimestre I (II: función lineal; III: cuadrática, ejemplo oficial del DBA 2) |

Ejemplo oficial del DBA 1 (los globos), revisado para la docente: Mónica escribe √5 = 2,23 (es
aproximación; a centésimas es 2,24); Alex dice «raíz de dos es más o menos 2.23» — **errata del
MEN**, debe ser raíz de cinco. No está en el banco, así que la guía no lo usa; la explicación
del tema 1 menciona solo que √5 = 2,23 debe escribirse √5 ≈ 2,24.

## Evidencias sin ejercicios (pendientes)

La guía explica la teoría pero no trae ejemplo resuelto ni preguntas de esto, porque el banco
no tiene ejercicios y el tema sí tiene otros en el banco (no aplica la excepción):

1. ~~Fracciones algebraicas~~ — **resuelto con 2 ejercicios nuevos** (el banco no tenía
   ninguno; excepción aclarada por la docente el 2026-09-15): `fracciones-algebraicas-9-001`
   (simplificar y valores excluidos) y `-002` (multiplicar, dividir, sumar, restar), en
   `recursos/banco/matematicas/fracciones-algebraicas-9.py`, verificados con
   `verificar --sin-registro`; falta registrarlos con `verificar` (sin la opción).
2. **Racionalización con denominador binomio** (conjugado; sesión 009): el banco solo tiene
   denominadores monomios (`radicacion-8-030`, `-031`, que sí se usan).
3. **Ecuaciones por factorización como serie de práctica** (sesión 021): solo hay problemas
   (`factorizacion-8-155`, `-156`) y la pregunta del Icfes 31; basta para la guía, pero no hay
   ejercicios directos del tipo «resuelve x² − 7x = 0».
4. **El ejemplo de los globos del DBA 1** (error al elevar una aproximación al cubo) y la
   **tablilla YBC 7289 como ejercicio** (base 60 → decimal): la guía los cuenta en el texto,
   sin preguntas.

## Frase introductoria

«[Me animé] a componer un breve tratado sobre el cálculo por compleción y reducción,
limitándome a lo más fácil y más útil de la aritmética, lo que los hombres necesitan
constantemente en casos de herencias, legados, particiones, pleitos y comercio» —
Al-Juarismi, prólogo del *Álgebra* (trad. propia de la versión inglesa de F. Rosen, 1831, p. 3).

## Marco teórico (en la guía, redactado)

1. **Una tablilla de escuela** — YBC 7289 [fowler].
2. **Bagdad y la Casa de la Sabiduría** — al-Mamún, título, «álgebra», «algoritmo», sin
   símbolos [mactutorjuarismi]; racionales e irracionales como objetos algebraicos
   [mactutorarabe].
3. **Resolver con figuras** — x² + 10x = 39 [rosen].
4. **Emmy Noether** — la científica del trimestre: 1882–1935, Gotinga, *Idealtheorie in
   Ringbereichen* (1921), teorema de 1918, Bryn Mawr (1933) [mactutornoether]; cita de
   Einstein [einstein].

## Temas y ejercicios (todos reutilizados y verificados)

**E** = ejemplo resuelto en la explicación; **P** = pregunta.

### Tema 1 — Números reales: aproximación, error y radicales · `tema:numerosreales`
Sesiones 005–010. Hilo: el escriba de YBC 7289; Al-Juarismi opera con raíces. Aplicación: planos
exactos y obras aproximadas (tolerancia de medida, sin cifras).

| Uso | Id | Enunciado (corto) |
|---|---|---|
| E | radicacion-8-035 | 5√27 − √147 + √12 = 10√3 |
| E | radicacion-8-030 | √(5a³) ÷ √(24b²), racionalizando |
| P | irracionales-8-013 | 7/5, 17/12, 99/70 frente a √2 (error) |
| P | numeros-reales-8-013 | ½ − (1 + √2) en la recta |
| P | radicacion-8-014, -036 | ∛40; 2∛250 + ∛16 − 3∛54 |
| P | numeros-reales-8-031, -033 | (√2 + √5)(√3 + √5); (3 − √2)(1 − √2) |
| P | radicacion-8-031 | cociente de raíces cúbicas, sin raíz en el denominador |
| P | medidas-con-radicales-8-002 | perímetro de un isósceles (√89) |

### Tema 2 — Productos notables y factorización · `tema:factorizacion`
Sesiones 011–017. Hilo y figura: completar el cuadrado de x² + 10x = 39 (texto de Rosen, sin
ejercicio). Aplicación: cajas de cartón (sin cifras).

| Uso | Id | Enunciado (corto) |
|---|---|---|
| E | factorizacion-8-264 | rectángulo (x + 3)(x + 4) en cuatro piezas |
| E | numeros-reales-8-036, productos-notables-8-043 | (a + b)(a − b); (2a + 1)³ |
| E | factorizacion-8-226 | 4x² + 8x + 3 (método ac) |
| E | factorizacion-8-109 | n³ + 2n² − 4n − 8 (agrupación + diferencia de cuadrados) |
| P | productos-notables-8-018, -021, -044 | (2a + 5)², (8a − 3)², (3a − 2)³ |
| P | factorizacion-8-222, -223, -230 | ax² + bx + c |
| P | factorizacion-8-305, -306, -312 | suma y diferencia de cubos |
| P | factorizacion-8-101, -375, -377, -400 | factorización completa |
| P | factorizacion-8-158 | ¿(a + b)² = a² + b²? |
| P | productos-notables-8-099 | volumen de un cubo de arista 3a − 2 |
| P | factorizacion-8-262 | lados de un rectángulo de área x² + 5x + 4 |

### Tema 3 — Fracciones algebraicas y ecuaciones · `tema:fraccionesecuaciones`
Sesiones 018–022. Hilo: compleción y equilibrio. Aplicación: soluciones que el problema no
admite.

| Uso | Id | Enunciado (corto) |
|---|---|---|
| E | fracciones-algebraicas-9-001 a) — **NUEVO** | (x² − 9)/(x² + 3x) = (x − 3)/x; x ≠ 0, −3 |
| E | fracciones-algebraicas-9-002 a), c) — **NUEVO** | producto → (x + 1)(x + 2); suma → (3x − 1)/(x² − 1) |
| E | factorizacion-8-376 | m² − 5m + 6 = 0 por factorización |
| P | fracciones-algebraicas-9-001 b)–d) — **NUEVO** | (x + 2)/(x − 2); 2x/(x − 3); (x² + x + 1)/(x + 1) |
| P | fracciones-algebraicas-9-002 b), d) — **NUEVO** | (x + 2)/(x − 2); −3/(x² − 9) |
| P | factorizacion-8-155 | perímetro = área de un círculo |
| P | factorizacion-8-156 | volumen = área total de un cubo |
| P | icfes-cuadernillo-2026-031 | María, Nelson y Óscar (textual, © Icfes) |

**Por qué son nuevos:** en todo el banco no había ningún ejercicio de fracciones algebraicas
(ni recurso del que sacarlos). Se escribieron solo dos, con varios literales, que cubren
simplificar, valores excluidos y las cuatro operaciones.

### Prepárate para Saber 11

| Id | Tema | Clave |
|---|---|---|
| icfes-cuadernillo-2026-027 (textual) | densidad de los reales | A |
| producto-polinomios-8-124 | Al-Juarismi: diez en dos porciones | B |
| factorizacion-8-373 | diferencia de cubos con volúmenes | C |
| productos-notables-8-122 | duplicar la arista de un cubo | D |

No se usa `producto-polinomios-8-125` (manual-pendiente y con más de una respuesta defendible
según `PENDIENTES.md`).

## Cierre del hilo

De la tablilla del escriba al libro de Bagdad y al álgebra abstracta de Noether. Anuncio: en el
trimestre II, la función lineal y los sistemas; en el III, completar el cuadrado para llegar a
la fórmula general.

## Evaluación (matriz)

- **Saber:** valor exacto y aproximación; productos notables, casos de factorización y valores
  excluidos de una fracción algebraica.
- **Hacer:** calcula errores; simplifica, opera y racionaliza radicales; factoriza
  completamente; opera fracciones algebraicas; resuelve ecuaciones por factorización.
- **Ser:** comprueba sus resultados y corrige.
- **Convivir:** reconoce el aporte de culturas distintas y de mujeres como Emmy Noether.

## Referencias (verificadas el 2026-09-14/15)

| Clave | Referencia | Veredicto | Corrección | URL |
|---|---|---|---|---|
| rosen | Rosen, F. (ed. y trad.) (1831). *The Algebra of Mohammed ben Musa*. Londres: Oriental Translation Fund. | confirmada: dedicatoria a al-Mamún y la frase (p. 3); x² + 10x = 39 y la receta (p. 8); prueba con figuras (pp. 13–15) | frase como «trad. propia de la versión inglesa» | https://archive.org/details/algebraofmohamme00khuwuoft |
| mactutorjuarismi | O'Connor y Robertson, *Al-Khwarizmi*, MacTutor | confirmada: Casa de la Sabiduría, al-Mamún califa desde 813, dedicatoria, *Hisab al-jabr w'al-muqabala*, «álgebra», «algoritmo», sin símbolos, c. 780–c. 850 | se quita «hacia 820» | https://mathshistory.st-andrews.ac.uk/Biographies/Al-Khwarizmi/ |
| mactutorarabe | O'Connor y Robertson, *Arabic mathematics: forgotten brilliance?*, MacTutor | confirmada | — | https://mathshistory.st-andrews.ac.uk/HistTopics/Arabic_mathematics/ |
| fowler | Fowler, D. y Robson, E. (1998). Square root approximations in Old Babylonian mathematics: YBC 7289 in context. *Historia Mathematica*, 25(4), 366–378. | confirmada: lado 30, 1;24,51,10, 42;25,35, ejercicio escolar | datación corregida | https://www.sciencedirect.com/science/article/pii/S0315086098922091 · https://www.ux1.eiu.edu/~cidelman/Classes/4900/Class%20Notes/Babylonian%20Approximations.pdf |
| mactutornoether | O'Connor y Robertson, *Emmy Amalie Noether*, MacTutor | confirmada | — | https://mathshistory.st-andrews.ac.uk/Biographies/Noether_Emmy/ |
| einstein | Einstein, A. (1935, 4 may.). The late Emmy Noether. *The New York Times*. | confirmada | trad. propia | https://mathshistory.st-andrews.ac.uk/Obituaries/Noether_Emmy_Einstein/ |
| mendba | MEN (2016). *DBA V.2: Matemáticas*. | confirmada, ISBN 978-958-691-913-5 | — | https://gblumen.mineducacion.gov.co/cgi-bin/koha/opac-detail.pl?biblionumber=4785 |
| icfes | Icfes (2026). *Cuadernillo de preguntas Matemáticas Saber 11.°*, preguntas 27 y 31. | archivo local | uso textual con crédito | recursos/matematicas/icfes/09-Marzo_Cuadernillo-de-Preguntas-Matematicas-Saber-11-2026.pdf |

## Etapa B — resumen

- **Ejercicios nuevos: 2**, solo de fracciones algebraicas (tema sin ningún ejercicio en el
  banco): `fracciones-algebraicas-9-001`, `-002`, verificados con `verificar --sin-registro`.
  Falta que una sesión corra `python3 tools/ejercicios.py verificar` para registrarlos.
- Los demás que se escribieron en esta pasada (`reales-9.py`, `factorizacion-guia-9.py`,
  `fracciones-ecuaciones-9.py`, `saber11-algebra-9.py`) se **borraron** por la regla de la
  docente; nunca se registraron en `verificados.json`.
- **Reutilizados: 39 ids**, todos `verificado` (comprobado con `listar` el 2026-09-15).
