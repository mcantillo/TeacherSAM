# Registro de cambios

Lo que ya se hizo, por fecha (lo más reciente primero). Lo que falta está en `PENDIENTES.md`.

## 2026-09-20

- **Paquetes de la semana 04 de Física 10° y Geometría 9°** (los del jueves 24):
  - **Física 10°**, sesiones 007 y 008 (100 min cada una): `clase.tex` de las dos, con la
    demostración de la cuerda que abre el tema —dos estudiantes halando con la misma fuerza
    en tres direcciones distintas y tres resultados— más `taller.tex` (jueves) y `tarea.tex`
    (viernes), de 5 puntos cada uno. Regla de la clase: **dibujar el vector antes de
    calcular**, porque la calculadora no sabe en qué cuadrante estamos.
  - **Geometría 9°**, sesión 004 (40 min): `clase.tex` con los tres criterios (AA, LAL, LLL)
    y el cierre del hilo —la sombra del árbol es el método de Eratóstenes— y `tarea.tex` de
    5 puntos. La tarea exige nombrar el criterio: «la respuesta numérica sola vale la mitad».
- **Diez ejercicios nuevos en dos archivos de banco que no existían:**
  `recursos/banco/fisica/vectores-10.py` (6: componentes, cuadrante, resultante
  perpendicular, suma de tres por componentes, el rango de la neta entre 10 y 70 N, y el
  error de sumar magnitudes y ángulos) y
  `recursos/banco/matematicas/semejanza-triangulos-9.py` (4: LLL, Thales como AA, la sombra
  del árbol, y el verdadero/falso que incluye el error del módulo de recursos). El banco no
  tenía **nada** de vectores ni de criterios de semejanza en triángulos.

- **Paquete de la semana 04 de Trigonometría 10°**, el más grande del curso: cuatro sesiones
  (013 a 016) en un solo `clase.tex`, más `taller.tex` y `tarea.tex` de 5 puntos cada uno.
  El martes, las seis razones a partir de dos lados; el jueves, el triángulo auxiliar para
  deducir las demás a partir de una, y el taller por la tarde; el viernes, la calculadora.
  El taller va **sin calculadora** (respuestas exactas) y la tarea **con** ella.
- La sesión 016 abre con la prueba de control de la calculadora: `sen 30°` debe dar `0,5`, o
  está en radianes. Queda propuesta como ritual para el resto del año.
- **Tres ejercicios nuevos** (`razones-trigonometricas-10-070…072`): las seis razones con
  catetos 5 y 12, el triángulo auxiliar con `tg θ = 3/4`, y el error de confundir el cateto
  opuesto con el adyacente. El banco tenía 38 libres, pero ninguno de esos dos tipos.
- **Unidades:** de los 38 libres, 10 vienen en pies y pulgadas y se descartaron por la
  decisión del 2026-09-19 de trabajar todo en métricas. Queda dicho en el `clase.tex`.

- **Paquetes de la semana 04 de Geometría 7° y Álgebra 9°** (los del martes 22):
  - **Geometría 7°**, sesión 004: `clase.tex` (el vector de traslación, deducirlo restando
    «imagen menos original», y por qué la figura trasladada es congruente) y `taller.tex` de
    5 puntos.
  - **Álgebra 9°**, sesiones 007 y 008: `clase.tex` de las dos (simplificar radicales el martes;
    el viernes, la trampa de $\sqrt{18}+\sqrt{2}$ y los radicales semejantes), `taller.tex` y
    `tarea.tex` de 5 puntos cada uno. Los ejercicios salen del banco de 8°, así que el paquete
    repite el aviso del reparto de irracionales entre 8° y 9°, que sigue sin decidirse.
- **Cuatro ejercicios nuevos de traslaciones** (`transformaciones-7-020…023`): aplicar el vector
  con una coordenada negativa, deducir el vector, componer dos traslaciones (y ver que da otra
  traslación, y que el orden da igual), y el error de restar en vez de sumar. El banco solo tenía
  uno de traslaciones y ya lo usaba la guía.
- Escrito en Cowork: los PDF no están compilados ni revisados.

## 2026-09-19 (tarde)

- **Los dos workflows se pisaban.** Los paquetes de Geometría 6° y 10° **sí compilaron** —los
  seis PDF se crearon—, pero `pdfs.yml` no pudo guardarlos: mientras compilaba (instala TeX
  Live en cada corrida, varios minutos), `ejercicios.yml` terminó y empujó su commit; cuando el
  de los PDF fue a empujar, main ya se había movido y GitHub lo rechazó por
  «non-fast-forward». El trabajo compilado se perdió.
  **Arreglo:** los dos reintentan el push hasta tres veces, rebasando sobre lo que haya en
  main. Era un error de diseño del 2026-09-19: dos robots escribiendo en la misma rama sin
  prever la carrera.

- **Catálogo del banco en marcha:** la docente lanzó «Verificar ejercicios» con la casilla de
  todo el banco. Resultado: **4098 ejercicios, 3144 verificados** y 954 manuales pendientes de
  su aprobación; los **17 que citaban las guías sin verificar quedaron verificados**. Con
  `recursos/banco/catalogo.jsonl` en el repositorio ya se pueden escoger ejercicios desde
  Cowork.
- **Paquetes de la semana 04 de Geometría 6° y Geometría 10°** (los dos del lunes 21 que
  faltaban):
  - **Geometría 6°**, sesión 003: `clase.tex` (estimar con el ángulo recto como referente,
    el error aceptable de 10°, y la figura del ángulo de tiro que resuelve la apuesta del
    trimestre) y `taller.tex` de 5 puntos.
  - **Geometría 10°**, sesión 003: `clase.tex` (deducir la distancia desde Pitágoras, los dos
    cuidados con los negativos, y el triángulo que parece equilátero y no lo es) y `tarea.tex`
    de 5 puntos.
- **Ocho ejercicios nuevos en el banco**, porque ninguno de los dos temas tenía libres:
  `angulos-medicion-6-005…008` (error de estimación, referentes del recto, ángulo de tiro de
  frente contra de lado, suplementarios) y `geometria-analitica-10-040…043` (distancias con
  ternas pitagóricas, triángulo isósceles que parece equilátero, rombo que no es cuadrado,
  y el error de restar mal un negativo). Los ocho son comprobables con código: el robot los
  verifica al subirlos.
- **Escrito en Cowork: falta compilar y revisar.** Lo hacen `pdfs.yml` y `ejercicios.yml` al
  subirlo.

- **Paquete de la semana 04 de Física 9°** (sesión 003, lunes 21): `clase.tex` del segundo y
  último día de exposiciones — las 3 que faltan, la rejilla de 5 puntos para calificarlas y el
  cierre «describir no es explicar», que abre el tema siguiente. Sin taller ni tarea, como
  quedó el plan. **Escrito en Cowork: falta compilarlo y revisarlo** (lo hace `pdfs.yml` al
  subirlo).
- **Límite encontrado:** sin SymPy, `tools/ejercicios.py listar` ni siquiera puede importar los
  archivos del banco, así que **desde Cowork no se pueden escoger ejercicios**. Los paquetes con
  taller, quiz o tarea tienen que hacerse en Claude Code. Física 9° salió porque su sesión no
  lleva ninguno.

- **Estado real de las guías, medido** (antes se venía describiendo de oído): las 16 existen,
  compilan y tienen PDF. Cinco pasaron por el proceso de tres etapas (Álgebra 8°, Cálculo 11°,
  Física 11°, Geometría 5° y 8°); las otras once salieron de la generación rápida del 2026-09-14,
  pero **no son bosquejos**: tienen de 4 a 8 temas y entre 22 y 45 KB, con hilo, marco teórico y
  ejercicios del banco. De todos los ejercicios que citan las 16 guías, **solo 17 no están
  verificados**, repartidos en tres cursos: Geometría 10° (9), Geometría 11° (6) y 9° (2).
- **`ejercicios.yml`: SymPy ahora corre en el repositorio.** Un workflow nuevo verifica el banco
  cuando cambia un `.py` de `recursos/banco/` y escribe `verificados.json`; también se lanza a
  mano con «Run workflow» y la casilla *Verificar todo el banco*. Así el material escrito en
  Cowork —que no tiene SymPy ni internet para instalarlo— se comprueba al subirlo, igual que los
  PDF con `pdfs.yml`.
- Corrección: el 2026-09-19 en la mañana se anotó que a Geometría 3°, 4° y 7° «el banco casi no
  les alcanza». Ese conteo se hizo por prefijos de nombre y estaba mal; sus guías citan 8/8, 8/8
  y 9/9 ejercicios verificados. Lo que sí falta es margen para talleres y tareas nuevos.

## 2026-09-19

- **Las siete preguntas abiertas de los planes quedaron resueltas** por la docente, una por una.
  Con eso **ningún curso espera ya una decisión suya para pasar al paso 3 (la guía)**:
  - **Física 9°:** quedan 7 exposiciones y ocupan las sesiones 002 y 003 completas (4 y 3); esas
    dos van sin taller y los dos talleres del trimestre pasan a la 005 y la 007. Los experimentos
    de la semana 01 fueron **demostraciones de la docente**, no un proyecto de estudiantes: no
    hay nada que evaluar y la guía los retoma como enganche del hilo.
  - **Física 10°:** el grupo vio cinemática **a medias** en 9° (MRU sí; MUA y caída libre no), así
    que el bloque pasa de 2 a 3 sesiones (009–011) y en parte deja de ser repaso. «Tercera ley»
    baja a 1 sesión (020) y «Las tres leyes» conserva 2.
  - **Trigonometría 10°:** seno y coseno se quedan en el trimestre II (el I no cambia) y **todo el
    material va en métricas** — los pies y millas se convierten antes de llegar al estudiante.
  - **Geometría 3°:** no hubo prueba diagnóstica; la sesión 003 abre con un repaso de punto y línea.
  - **Geometría 4°:** la sesión 002 fue solo la introducción (la bitácora decía más); la 003
    retoma el tema desde el principio.
  - **Geometría 11°:** las preguntas ICFES 15, 37 y 41 entran en la guía, con su formato original.
  - **Geometría 10° y Física 9°, trimestre III:** las semanas 36–37 son festivas y esos cursos de
    lunes no tienen sesión en su semana de evaluación; el examen se adelanta a la sesión 029
    (semana 35) y el repaso va en la 028.
- Efecto en el calendario: solo Física 9°, Física 10° y el trimestre III de los dos cursos de
  lunes cambiaron sesiones. Los demás quedaron como estaban.

## 2026-09-18 (tarde)

- **Los 11 planes anuales que faltaban quedaron aprobados por la docente**, todos con el hilo
  recomendado: Álgebra 9° (Al-Juarismi), Física 9° (De Aristóteles a Galileo), Física 10° (De la
  inercia a los *Principia*), Trigonometría 10° (Medir lo inalcanzable), Geometría 3° (*El
  renacuajo paseador*), 4° (*La vuelta al mundo en 80 días*), 6° (La geometría del fútbol),
  7° (Escher), 9° (Eratóstenes), 10° (Ubicarse en la Tierra) y 11° (LORAN). **Los 16 cursos
  tienen ya plan anual aprobado y trimestre I programado.**
- Las preguntas abiertas de cada plan **no** se aprobaron: la docente las responde una por una y
  quedan listadas en `PENDIENTES.md`. Cuatro cursos no tenían ninguna (Álgebra 9°, Geometría 6°,
  7° y 9°), así que están listos para escribir su guía con el proceso de tres etapas.

## 2026-09-18

- **Recompilación completa del repositorio** (Actions → «Compilar PDF» → «Run workflow» →
  *Recompilar todos*): **los 56 `.tex` de `materias/` tienen su PDF**. Se cerró lo último que
  quedaba del lío de los PDF:
  - Las **guías de Geometría 9° y 11°** volvieron a compilar; sus PDF se regeneraron. La causa
    era `txfonts`, igual que los `clase.tex` de la semana 03 — no un error dentro de los `.tex`.
  - Salieron los `clase.pdf` de **Geometría 7° y Trigonometría 10°** (semana 03), que el push
    anterior no había tocado porque el CI solo compila los `.tex` que cambian.
- **Lección, anotada porque costó tres vueltas:** cuando una compilación falla, el `.aux` marca
  hasta dónde alcanzó a llegar, **no dónde está el error**. Deducir el problema leyendo los
  `.tex` mandó a buscar en el sitio equivocado; el mensaje del registro del CI lo resolvió en un
  minuto. Primero el registro, después las hipótesis.

## 2026-09-17 (tarde)

- **Los 4 archivos que fallaban en el CI, diagnosticados** (registro de Actions de la corrida
  de `366c762`). Son dos errores distintos, no uno:
  - **Fuente monoespaciada ausente en el CI** (3 archivos: `clase.tex` de Álgebra 9°,
    Geometría 7° y Trigonometría 10°, semana 03): «Font T1/npxtt/m/n/10.95=t1xtt not
    loadable: Metric (TFM) file not found». Es la primera vez que un material de `materias/`
    usa `\texttt`; `newpxtext` toma sus metrías de **`txfonts`**, que no estaba en la lista
    de `tlmgr install` del workflow. Se agregó. En el Mac no se nota porque allí el TeX Live
    está completo.
  - **`%` dentro de modo matemático** (1 archivo: `tarea.tex` de Álgebra 9°, y el mismo caso
    en su `clase.tex`, que ya moría antes por la fuente): «Incompatible glue units» en
    `\es@sppercent`. babel-spanish mide `\lastskip` al componer el `%`, y en modo matemático
    ese `\lastskip` es *muglue*. Se cambiaron los dos `$\num{…}\,\%$` por
    `\qty{…}{\percent}` (siunitx, que ya estaba cargado). **Regla para lo que venga: los
    porcentajes se escriben con `\qty{}{\percent}`, nunca con `\%` dentro de `$…$`.**

## 2026-09-17

- **Se recuperaron dos guías borradas por el CI:** las del trimestre I de Geometría 9°
  (`guia-periodo-I-semejanza-medicion`) y Geometría 11° (`guia-periodo-I-hiperbola-navegacion`).
  El commit `ca898e5` («Compilar PDF») había borrado su `.pdf` y dejado su `.aux` a medias; se
  restauraron ambos desde `4083e90`. Los `.tex` nunca cambiaron, así que los PDF recuperados
  corresponden a su fuente.
- **Causa y arreglo:** `pdflatex` borra el PDF anterior al arrancar, así que una compilación
  fallida deja la carpeta sin PDF; el paso «Subir los PDF» usaba `git add -A`, que publicaba ese
  borrado. Ahora `tools/compilar-pdfs.sh` recupera del repositorio el `.pdf` y el `.aux` del
  archivo que falló, y el workflow usa `git add --ignore-removal`: **un error de compilación ya
  no puede destruir un PDF que servía**.
- Queda pendiente el error de fondo: esas dos guías no compilan en el CI (ver `PENDIENTES.md`).
- **Trimestre I programado en los 9 cursos que faltaban** (106 filas: `tema`, `subtema`, `dba` y
  las marcas `quiz`/`taller`/`tarea`), por instrucción de la docente de no esperar su aprobación:
  Álgebra 9°, Física 9° y 10°, y Geometría 3°, 4°, 6°, 7°, 9° y 11°. Cada fila sale del plan de
  la guía del curso (que ya reparte los temas por número de sesión) y el ritmo de quices,
  talleres y tareas, del «Ritmo de evaluación» de su `plan-anual.md`. Trigonometría 10° y
  Geometría 10° ya estaban programados. **Sigue siendo una propuesta:** se escribió sin
  aprobación, y la docente puede cambiar cualquier fila.
- Dos filas quedaron **a propósito sin DBA**, porque son decisiones abiertas de la docente
  (`PENDIENTES.md`, sección 1): «Medición» en Física 10° (sesiones 005–006) y «Líneas» en
  Geometría 4° (003–006, no están en ningún DBA de 4°). Y la sesión 002 de Geometría 9° sigue
  vacía: la bitácora no dice qué se dictó ese día y no se inventa.

## 2026-09-15

- **Paquetes de la semana 03** (clases del 15 al 18 de septiembre): Trigonometría 10°
  (clase de 4 sesiones, taller de medición y tarea con ejercicios del banco), Geometría 7°
  (clase) y Álgebra 9° (clase de 2 sesiones, taller y tarea). Los de Geometría 7° y
  Álgebra 9° van marcados **BORRADOR**: sus filas de `programacion.csv` siguen vacías y su
  plan del trimestre I espera aprobación; no se escribió nada en el CSV.
- **Revisión del estado tras el corte por límite de uso.** Quedó en `main` más de lo que
  parecía: las **16** guías del trimestre I (no 13), los paquetes de las semanas 03 y 04 de
  Física 11°, y los archivos del banco `coordenadas-11.py`, `lugares-geometricos-11.py`,
  `hiperbola-11.py`, `medicion-indirecta-9.py` y `navegacion-11.py`. Los 9 ejercicios que
  cita la guía de Geometría 10° **sí existen**; lo que falta es verificarlos (no están en
  `verificados.json`).
- **Guías de Geometría 9° y 11°:** el CI las compiló y falló, así que borró sus PDF y dejó
  su `.aux` a medias (commit `ca898e5`). Los `.tex` están completos; falta encontrar y
  corregir el error de compilación.

## 2026-09-15 — antes del corte por límite de uso

- **Regla del banco:** los documentos usan solo ejercicios del banco; por defecto no se crean
  ejercicios nuevos (skills `verificar-ejercicios` y `crear-guia`). Si falta uno, se anota como
  pendiente.
- **Cabecera de Física:** con `\asignatura{Física}` la cabecera dice «Área de Ciencias
  Naturales»; `\area{…}` la cambia a mano (`mmcantillo.sty`, `plantillas/README.md`).
- Guías del trimestre I en generación rápida (varios agentes a la vez): Geometría 5°, 8° y 10°
  y Física 11° terminadas; las demás en curso.

## 2026-09-14

- **Calendario oficial** en `programacion-2026-2027.md`; se regeneraron los 16
  `programacion.csv`. El trimestre I de Cálculo 11° se reajustó a 33 sesiones (filas 001–033).
- **Bitácora de la docente** (`bitacora-2026-2027.md`): lo que se dictó en las semanas 01–02 de
  cada curso. Con ella se registraron las filas ya dictadas; en Cálculo 11° las filas 001–005
  quedaron como diagnóstico y refuerzo de factorización.
- **Fusión del respaldo** de una sesión anterior (escrito con el calendario provisional y pasado
  al oficial; su semana 13 se juntó con la 12): plan anual y trimestre I de Álgebra 8°,
  Geometría 8°, Geometría 5° y Física 11°; guías del trimestre I de Álgebra 8°, Geometría 5° y
  Física 11°; paquetes de la semana 03 de Álgebra 8° y Geometría 5°, enlazados a su guía. Se
  corrigieron los errores de hecho de esas guías.
- **Física 11°:** la docente aprobó el plan anual, el trimestre I y el hilo «De Tales al
  pararrayos», sincronizado con Cálculo 11°.
- **Guía de Álgebra 8°** rehecha con el proceso de tres etapas y un hilo nuevo, «La cacería de
  π» (ninguna fuente antigua liga a Hipaso con los irracionales): plan con fuentes verificadas
  (etapa A), ejercicios en `recursos/banco/matematicas/irracionales-8.py` (22 verificados,
  4 manuales; etapa B) y LaTeX de 13 páginas (etapa C). DBA de las sesiones 007–009 asignados.
- **Planes de etapa A** de las guías de Física 11°, Geometría 5° y Geometría 8°.
- **Propuestas de plan anual y trimestre I** (pendientes de aprobación) para Álgebra 9°,
  Física 9° y 10°, Trigonometría 10° y Geometría 3°, 4°, 6°, 7°, 9°, 10° y 11°.
- Rama `trimestre-i-planeacion` y `main` en GitHub.

## 2026-09-13

- **Banco de ejercicios:** ocho agentes en paralelo lo llenaron para todos los cursos desde sus
  recursos (solo las partes de cada asignatura y DBA): unos 3 040 ejercicios verificados y unos
  950 abiertos pendientes de aprobación (la mayoría de Física). Lista de lo que falta para
  confiar en él: `recursos/banco/PENDIENTES.md`.
- En el banco: los «Practica lo aprendido» de los temas 1–2 del módulo de 11° (desigualdades,
  intervalos, inecuaciones, valor absoluto) y su «Prepárate para el ICFES»
  (`saber11-desigualdades.py`; el problema de las lámparas quedó fuera, pendiente de la
  docente), y 15 preguntas liberadas del ICFES copiadas textualmente
  (`icfes-cuadernillo-2026.py`).
- Material oficial del ICFES en `recursos/matematicas/icfes/`.
- Plan anual de Álgebra 8° y Geometría 8° aprobados por la docente (hecho en la sesión que luego
  se fusionó).

## 2026-09-12

- Se generaron los 16 `programacion.csv` (columnas de planeación vacías).
- **Piloto Cálculo 11°:** plan anual, plan del trimestre I y guía del trimestre I; paquetes de
  las semanas 01–02 (clase, taller, tarea y quiz de la semana 02, con claves).
