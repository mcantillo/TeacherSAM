# Plan anual 2026–2027 — Álgebra 9°

Aprobado por la docente el 2026-09-18: el reparto por trimestre, el ritmo de evaluación
y el hilo del trimestre I (opción **A**, «Al-Juarismi y el nacimiento del álgebra»). El trimestre I ya está escrito
sesión a sesión en `programacion.csv` (se llenó el 2026-09-17). Quedan abiertas las
preguntas de este plan, que la docente responde una por una; ver `PENDIENTES.md`.

Sesiones 001–004 (semanas 01–02) registradas el 2026-09-14 con lo que se dictó según la
bitácora de la docente (`bitacora-2026-2027.md`): semana 01, actividades de inicio, dinámicas
de grupo y prueba diagnóstica; semana 02, refuerzo de factorización, casos 1 a 4 (factor
común, diferencia de cuadrados, trinomio cuadrado perfecto, trinomio x² + bx + c). La
bitácora no dice qué cubrió cada sesión de la semana, así que las dos sesiones de cada semana
llevan el mismo subtema. Quedan sin DBA (diagnóstico y refuerzo, no contenido nuevo del grado)
y sin paquete de clase.

## DBA de la asignatura

Fuente: `dba/matematicas/grados/grado09.tex`. Álgebra 9° cubre el componente
numérico-variacional; el espacial-métrico es de Geometría 9° y la estadística y probabilidad
(DBA 10–11) es de otra asignatura.

| DBA | Enunciado | Asignatura |
|---|---|---|
| 1 | Utiliza los números reales (sus operaciones, relaciones y propiedades) para resolver problemas con expresiones polinómicas. | **Álgebra** |
| 2 | Propone y desarrolla expresiones algebraicas en el conjunto de los números reales y utiliza las propiedades de la igualdad y de orden para determinar el conjunto solución de relaciones entre tales expresiones. | **Álgebra** |
| 3 | Utiliza los números reales, sus operaciones, relaciones y representaciones para analizar procesos infinitos y resolver problemas. | **Álgebra** |
| 4 | Volumen y capacidad de cuerpos redondos (cilindro, cono, esfera) | Geometría 9° |
| 5 | Thales y Pitágoras para medir y calcular longitudes | Geometría 9° |
| 6 | Semejanza, congruencia y teoremas básicos | Geometría 9° |
| 7 | Trayectorias y desplazamientos de los cuerpos (interpretación analítica del espacio) | Geometría 9° (**a confirmar**, ver preguntas) |
| 8 | Utiliza expresiones numéricas, algebraicas o gráficas para hacer descripciones de situaciones concretas y tomar decisiones con base en su interpretación. | **Álgebra** |
| 9 | Utiliza procesos inductivos y lenguaje simbólico o algebraico para formular, proponer y resolver conjeturas en la solución de problemas numéricos, geométricos, métricos, en situaciones cotidianas y no cotidianas. | **Álgebra** |
| 10, 11 | Estadística y probabilidad | otra asignatura |

Evidencias que guían cada trimestre (textuales del `.tex`):

- DBA 1: «Considera el error que genera la aproximación de un número real a partir de números
  racionales»; «Identifica la diferencia entre exactitud y aproximación en las diferentes
  representaciones de los números reales»; «Construye representaciones geométricas y numéricas
  de los números reales (con decimales, raíces, razones, y otros símbolos) y realiza
  conversiones entre ellas».
- DBA 2: «Identifica y utiliza múltiples representaciones de números reales para realizar
  transformaciones y comparaciones entre expresiones algebraicas»; «Establece conjeturas al
  resolver una situación problema, apoyado en propiedades y relaciones entre números reales»;
  «Determina y describe relaciones al comparar características de gráficas y expresiones
  algebraicas o funciones».
- DBA 3: «Encuentra las relaciones y propiedades que determinan la formación de secuencias
  numéricas»; «Determina y utiliza la expresión general de una sucesión para calcular cualquier
  valor de la misma y para compararla con otras sucesiones».
- DBA 8: «Opera con formas simbólicas que representan cantidades»; «Reconoce que las letras
  pueden representar números y cantidades, y que se pueden operar con ellas y sobre ellas»;
  «Interpreta expresiones numéricas, algebraicas o gráficas y toma decisiones con base en su
  interpretación».
- DBA 9: «Efectúa exploraciones, organiza los resultados de las mismas y propone patrones de
  comportamiento»; «Propone conjeturas sobre configuraciones geométricas o numéricas y las
  expresa verbal o simbólicamente»; «Valida las conjeturas y explica sus conclusiones»;
  «Interpreta expresiones numéricas y toma decisiones con base en su interpretación».

## Reparto por trimestre

Sesiones y semanas contadas en `programacion.csv` (2026-09-14). El curso tiene **dos sesiones
por semana**: martes 1:00–1:40 (40 min) y viernes 6:55–7:50 (55 min).

| Trimestre | Semanas | Sesiones | DBA | Contenido |
|---|---|---|---|---|
| I | 01–12 | 24 (001–024) | 1, 2 | Números reales y expresiones polinómicas: la recta real, aproximación y error, radicales; productos notables, factorización completa; fracciones algebraicas; ecuaciones que se resuelven factorizando. De las 24 sesiones, 4 ya se usaron en diagnóstico y refuerzo, y 2 son de repaso y evaluación. |
| II | 13–26 (sin semana 16; la 14 tiene una sola sesión por el festivo del 8 de diciembre) | 25 (025–049) | 8, 2 | Función lineal como modelo: pendiente, rectas paralelas y perpendiculares, lectura de gráficas para decidir. Sistemas de ecuaciones 2×2 (métodos y aplicaciones), inecuaciones lineales e intervalos, determinantes y regla de Cramer; sistemas 3×3 si alcanza el tiempo. |
| III | 27–37 | 22 (050–071) | 2, 8, 3, 9 | Función cuadrática: gráfica, traslaciones, vértice, discriminante; ecuación cuadrática (fórmula general) y comparación de funciones con intervalos (el ejemplo del DBA 2). Sucesiones aritméticas y geométricas, Fibonacci; patrones, conjeturas y su validación. |

## Criterios

- **Solo los DBA del componente** numérico-variacional (skill `alinear-dba`); los DBA 4–7 son
  de Geometría 9°, que la misma docente dicta (jueves 1:00–1:40).
- **Partir del diagnóstico.** La semana 02 reforzó los casos 1 a 4 de factorización; el
  trimestre I los retoma y completa (trinomio ax² + bx + c, agrupación, cubos, combinación de
  casos) dentro del DBA 1, «resolver problemas con expresiones polinómicas».
- **Del número a la expresión y de la expresión a la función.** Trimestre I, los reales y el
  cálculo algebraico; trimestre II, la primera función (lineal) y los sistemas; trimestre III,
  la cuadrática y las sucesiones, que necesitan todo lo anterior.
- **Pocas sesiones y cortas** (40 y 55 min): un subtema por sesión, y el trimestre I deja el
  DBA 3 (procesos infinitos) para el III, donde se une con el DBA 9 (patrones y conjeturas).
- **Orden del módulo de 9°** (`recursos/`): sus temas 1–4 (función lineal, sistemas,
  determinantes, sistemas 3×3) van en el trimestre II y su tema 5 (función cuadrática) en el
  III. El módulo no trae números reales ni factorización: para el trimestre I se usan el módulo
  de 8° y el banco de 8° como repaso (ver «Recursos principales»).

## Ritmo de evaluación (propuesto)

- **Tarea** asignada el viernes y revisada el martes siguiente, todas las semanas de
  contenido.
- **Taller** el viernes (55 min), en semanas alternas: unos 4 por trimestre.
- **Quiz** de 15–20 min al comienzo del viernes de la semana en que cierra un tema: unos 3 por
  trimestre. Nunca taller y quiz el mismo día.
- El martes (40 min) queda para explicación nueva y revisión de la tarea.
- La **última semana de cada trimestre** es de repaso y evaluación del periodo: sin taller,
  sin quiz y sin tarea nueva.

## Hilos conductores

Opciones para el trimestre I, en registro juvenil (9°, ≈ 14–15 años). Se evitaron los hilos ya
usados en otros cursos: Hipaso y el infinito (Cálculo 11°) y la cacería de π (Álgebra 8°).

| Opción | Hilo | Por qué encaja | Datos a verificar antes de la guía |
|---|---|---|---|
| **A (recomendada)** | **Al-Juarismi y el nacimiento del álgebra.** En la Casa de la Sabiduría de Bagdad, hacia el año 820, Muhammad ibn Musa al-Juarismi escribió el libro cuyo título (*al-jabr wa-l-muqabala*) dio nombre al «álgebra»; de su nombre latinizado viene «algoritmo». Resolvía sus problemas con cuadrados y rectángulos: los mismos modelos de área de los productos notables y la factorización. | El álgebra nace como técnica para transformar expresiones sin cambiar su valor: es el DBA 2 hecho historia, y los diagramas de área dan la representación geométrica que pide el DBA 1. El hilo puede seguir en el III (completar el cuadrado → fórmula general). | Fecha aproximada (c. 813–833, califato de al-Mamún) y título exacto de la obra; que sus soluciones eran geométricas y sin símbolos. Datos conocidos, no verificados contra fuente en esta propuesta. |
| B | **Aproximar lo que no termina: la tablilla YBC 7289.** Una tablilla babilónica (colección de Yale, periodo paleobabilónico) da √2 en base 60 con un error menor que una millonésima. De ahí a la calculadora: ¿cuántas cifras necesitamos? | Ataca de frente la evidencia «error de la aproximación» del DBA 1 y el ejemplo de los globos (√5). Menos apoyo para la factorización. | Datación (≈ 1800–1600 a. C.) y el valor exacto 1;24,51,10 ≈ 1,41421296. Conocidos, no verificados en esta propuesta. |
| C | **Factorizar para guardar secretos.** Euclides probó que los primos son infinitos; en 1977 Rivest, Shamir y Adleman publicaron el cifrado RSA, cuya seguridad depende de lo difícil que es factorizar números enormes. | Enganche tecnológico fuerte y da sentido a «factorizar». Riesgo: RSA factoriza enteros, no polinomios; la analogía hay que explicarla con cuidado. | Elementos IX.20 (infinitud de los primos); fecha y autores de RSA. Conocidos, no verificados en esta propuesta. |

Recomendación: **A**, usando la tablilla de B como anécdota de apertura del tema de
aproximación (sesión 006). Ninguna cita textual se incluye todavía: las citas y fechas se
verifican contra fuente al escribir la guía, como pide `crear-guia`.

| Trimestre | Hilo | Estado |
|---|---|---|
| I | Al-Juarismi y el nacimiento del álgebra | aprobado |
| II | por definir | — |
| III | por definir | — |

## Propuesta del trimestre I, sesión por sesión

Martes = 40 min · viernes = 55 min. Filas 001–004 ya dictadas (registradas en el CSV); las
demás son propuesta y **no** están en el CSV. Temas: **T1** Números reales (DBA 1) · **T2**
Productos notables y factorización (DBA 1, 2) · **T3** Fracciones algebraicas y ecuaciones
por factorización (DBA 2).

| Sem. | Clase | Fecha | Tema | Subtema | DBA | Quiz | Taller | Tarea |
|---|---|---|---|---|---|---|---|---|
| 01 | 001 | 2026-09-01 mar | Inicio de año | Actividades de inicio, dinámicas de grupo y prueba diagnóstica *(dictada)* | — | | | |
| 01 | 002 | 2026-09-04 vie | Inicio de año | Actividades de inicio, dinámicas de grupo y prueba diagnóstica *(dictada)* | — | | | |
| 02 | 003 | 2026-09-08 mar | Refuerzo de factorización | Casos 1 a 4 (factor común, diferencia de cuadrados, trinomio cuadrado perfecto, trinomio x² + bx + c) *(dictada)* | — | | | |
| 02 | 004 | 2026-09-11 vie | Refuerzo de factorización | Casos 1 a 4 *(dictada)* | — | | | |
| 03 | 005 | 2026-09-15 mar | T1 Números reales | Racionales e irracionales en la recta real | 1 | | | |
| 03 | 006 | 2026-09-18 vie | T1 Números reales | Aproximación y error: exactitud frente a aproximación (√2, π) | 1 | | x | x |
| 04 | 007 | 2026-09-22 mar | T1 Números reales | Representación geométrica de raíces en la recta | 1 | | | |
| 04 | 008 | 2026-09-25 vie | T1 Números reales | Radicales: propiedades y simplificación | 1 | | | x |
| 05 | 009 | 2026-09-29 mar | T1 Números reales | Operaciones con radicales y racionalización | 1 | | | |
| 05 | 010 | 2026-10-02 vie | T1 Números reales | Problemas con reales: la razón √5 de los globos y el error de aproximar | 1 | x | | x |
| 06 | 011 | 2026-10-06 mar | T2 Productos notables y factorización | Polinomios con coeficientes reales: valor numérico y operaciones | 1; 2 | | | |
| 06 | 012 | 2026-10-09 vie | T2 Productos notables y factorización | Productos notables con modelos de área: (a + b)², (a + b)(a − b), (a + b)³ | 1; 2 | | x | x |
| — | — | 2026-10-12 → 10-16 | *Receso de octubre* | | | | | |
| 07 | 013 | 2026-10-20 mar | T2 Productos notables y factorización | Repaso de los casos 1–4 y trinomio ax² + bx + c | 1 | | | |
| 07 | 014 | 2026-10-23 vie | T2 Productos notables y factorización | Factorización por agrupación; suma y diferencia de cubos | 1 | | | x |
| 08 | 015 | 2026-10-27 mar | T2 Productos notables y factorización | Factorización completa: combinación de casos | 1; 2 | | | |
| 08 | 016 | 2026-10-30 vie | T2 Productos notables y factorización | Factorizar áreas y volúmenes: problemas con expresiones polinómicas | 1; 2 | | x | x |
| 09 | 017 | 2026-11-03 mar | T2 Productos notables y factorización | ¿Son equivalentes? Comparar y transformar expresiones (conjeturas) | 2 | | | |
| 09 | 018 | 2026-11-06 vie | T3 Fracciones algebraicas y ecuaciones | Fracciones algebraicas: dominio y simplificación | 2 | x | | x |
| 10 | 019 | 2026-11-10 mar | T3 Fracciones algebraicas y ecuaciones | Multiplicación y división de fracciones algebraicas | 2 | | | |
| 10 | 020 | 2026-11-13 vie | T3 Fracciones algebraicas y ecuaciones | Suma y resta de fracciones algebraicas | 2 | | x | x |
| 11 | 021 | 2026-11-17 mar | T3 Fracciones algebraicas y ecuaciones | Ecuaciones que se resuelven factorizando (si ab = 0, a = 0 o b = 0) | 2 | | | |
| 11 | 022 | 2026-11-20 vie | T3 Fracciones algebraicas y ecuaciones | Problemas que llevan a ecuaciones por factorización | 2 | x | | x |
| 12 | 023 | 2026-11-24 mar | Repaso y evaluación del periodo | Repaso general del trimestre I | 1; 2 | | | |
| 12 | 024 | 2026-11-27 vie | Repaso y evaluación del periodo | Evaluación del periodo I | 1; 2 | | | |

Resumen: 18 sesiones de contenido nuevo (005–022), 3 quices (010, 018, 022), 4 talleres (006,
012, 016, 020), 9 tareas (viernes de las semanas 03–11), y la semana 12 de repaso y
evaluación. La tarea del 022 es la guía de repaso para el examen.

## Recursos principales

- `recursos/matematicas/Guías pedagógicas Matemáticas/09 - Modulo_Matematicas_Noveno.docx`
  (leer en `markdown/`): tema 1 función lineal, tema 2 sistemas de ecuaciones, tema 3
  determinantes y Cramer, tema 4 sistemas 3×3 → **trimestre II**; tema 5 función cuadrática
  (traslaciones, vértice, discriminante) → **trimestre III**. No trae reales, factorización,
  fracciones algebraicas ni sucesiones.
- `recursos/matematicas/Guías pedagógicas Matemáticas/08 - Modulo_Matematicas_Octavo.docx`
  (en `markdown/`): tema 1 (operaciones con reales, radicación, radicales semejantes), tema 3
  (productos y cocientes notables) y tema 4 (factorización) → base del **trimestre I**,
  subiendo el nivel a 9°.
- Banco (`python3 tools/ejercicios.py listar --grado 9`): `funcion-lineal-9`,
  `sistemas-ecuaciones-9`, `determinantes-9`, `sistemas-3x3-9` (trimestre II) y
  `funcion-cuadratica-9` (trimestre III). Para el trimestre I solo hay ejercicios marcados de
  8°: `numeros-reales-8`, `radicacion-8`, `medidas-con-radicales-8`, `productos-notables-8`,
  `factorizacion-8`. `pitagoras-9` es de Geometría 9° (DBA 5), no de este curso.
- Faltan recursos para fracciones algebraicas (T3 del trimestre I) y para sucesiones (DBA 3,
  trimestre III): habría que agregarlos a `recursos/` o redactar ejercicios propios desde los
  DBA.

## Pendientes de la docente que tocan este curso

(De `recursos/banco/PENDIENTES.md`; aquí solo se señalan, no se deciden.)

- Contextos del módulo de 9°: ¿pasar a unidades y pesos colombianos el tema 2 (millas,
  euros…)? ¿Se acepta cambiar el contexto bélico del tema 3, ICFES 4–6?
- Datos elegidos por un agente: $225 000 (tema 1, ICFES 1); segunda trayectoria de tema 5,
  Practica 14.
- Selección múltiple con más de una respuesta defendible: ICFES Al-Juarismi pregunta 2;
  sueldo del vendedor (falta la comisión); sistemas 17 (discos, 4 o 5).
- Posibles erratas: tema 4, 2f (sin solución) y tema 4, ICFES 4 (bis) c (infinitas
  soluciones).
- Omitidos por ilegibles: tema 3, actividad 2i y ICFES 1c.
- 16 preguntas abiertas de Matemáticas 9° esperan aprobación de su respuesta modelo.
