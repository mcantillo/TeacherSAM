# Pendientes

Lista de lo que falta, agrupada por quién lo desbloquea. Se actualiza cada vez que se abre o se
cierra un pendiente (ver `CLAUDE.md`); lo ya hecho pasa a `CHANGELOG.md`. Los pendientes del
banco de ejercicios están aparte, en `recursos/banco/PENDIENTES.md`.

Última actualización: 2026-09-17.

## 0. Urgente — desbloquea clases de esta semana

- [ ] **Aprobar el trimestre I de Geometría 7° y Álgebra 9°** (o corregir la propuesta de
      su `plan-anual.md`). Sus filas de `programacion.csv` **ya se llenaron el 2026-09-17**
      (por instrucción de la docente de no esperar la aprobación), así que a los paquetes del
      15 al 18 de septiembre se les puede quitar la marca **BORRADOR** en cuanto la docente
      confirme el plan; si lo corrige, hay que rehacer las filas y los paquetes.
- [ ] **Geometría 7° no tiene ejercicios verificados** para el trimestre I: el banco solo
      trae `angulos-7-003`, que ya usa la guía. Por eso la sesión 003 va sin tarea aunque
      la propuesta la marque. Hay que escribir y verificar ejercicios de giros,
      traslaciones, rotaciones, reflexiones y vistas para 7°.
- [ ] **Irracionales en 8° y en 9°:** el trimestre I de los dos cursos trabaja los mismos
      temas y los mismos ejercicios (`irracionales-8`). Decidir el reparto antes de la
      semana 04, o el trimestre se repite entero.
- [x] **Recompilación completa hecha** (2026-09-18, `--todos` desde Actions): **los 56 `.tex`
      de `materias/` tienen su PDF**, incluidas las guías de Geometría 9° y 11°. Era la fuente
      que faltaba (`txfonts`), no un error de los `.tex`.
- [ ] **Los 9 ejercicios de la guía de Geometría 10°** (`coordenadas-11-001…005` y
      `lugares-geometricos-11-001, -003, -004, -005`) existen en el banco pero **no están
      verificados** (`verificados.json` no los tiene). Hay que correr
      `python3 tools/ejercicios.py verificar` con SymPy antes de dar la guía por buena.
## 1. Decisiones de la docente — generales

- [ ] **Rangos del SIEE:** confirmar la escala 1,0–5,0 y los rangos de desempeño (Bajo, Básico,
      Alto, Superior).
- [ ] **Qué grado se queda con cada tema repetido:**
  - [ ] triángulos y ángulos del módulo de Geometría: 6° o 8° (`triangulos-6`/`-8`,
        `angulos-6-002/003`/`angulos-8-012/013`);
  - [ ] problemas de Pitágoras: 9° o 11° (`pitagoras-9-002…005` = `medicion-11-008…011`);
  - [ ] pendiente y ángulo de inclinación: Geometría 10° o Trigonometría 10°;
  - [ ] la hipérbola: Geometría 10° (DBA 5 de 10°) o Geometría 11°;
  - [ ] sistemas de ecuaciones: Álgebra 8° (trimestre II) o Álgebra 9° (¿repaso?);
  - [ ] rectas paralelas y perpendiculares en 4° (no están en ningún DBA de 4°).
- [ ] **DBA sin dueño en 10°:** como no hay Álgebra ni Cálculo en 10°, ¿Trigonometría toma los
      DBA 1, 2, 3, 6 y 7 como apoyo?
- [ ] **Temas de Física sin DBA:** ondas, luz y calor en 9°; mediciones, fluidos y termodinámica
      en 10°. ¿Entran?
- [ ] **Recursos que faltan** (para aprobar en `recursos/`): Geometría 3° y 4°; geometría
      analítica y cónicas (10°–11°), coordenadas polares y esféricas; Álgebra 9° (reales,
      factorización, fracciones algebraicas, sucesiones); cuerpos redondos y trayectorias (9°);
      momento lineal y choques (Física 10°).

## 2. Decisiones de la docente — por curso

### Cálculo 11° (piloto)
- [ ] Según la bitácora, en las semanas 01–02 se hizo diagnóstico y refuerzo de factorización:
      decidir dónde se recuperan los subtemas planeados de «Los sistemas numéricos» (los
      paquetes de las semanas 01–02 quedaron sin dictar).
- [ ] Aprobar los hilos de los trimestres II y III, compartidos con Física 11° («Las leyes que se
      ven en una gráfica», «Faraday no sabía matemáticas»).

### Álgebra 8°
- [ ] **Revisión 2 de la guía:** aprobar la tabla de ejercicios del plan y las 4 respuestas
      modelo (`irracionales-8-004`, `-008`, `-009`, `-019`) con
      `python3 tools/ejercicios.py aprobar <id>`.
- [ ] **Revisión 3:** revisar el PDF de la guía (`guia-periodo-I-numeros-irracionales.pdf`).
- [ ] ¿Renombrar el tema 2 «El escándalo pitagórico» (p. ej. «El primer número que no es
      fracción»), ahora que el hilo es «La cacería de π»?
- [ ] Revisar el paquete de la semana 03 (clase + tarea).

### Física 11°
- [ ] Revisión 1 del plan de la guía (`guia-periodo-I-electrostatica.plan.md`), con sus
      preguntas: contar la cometa de Franklin como «publicó cómo hacerlo y que funcionó» y
      centrar el hilo en el pararrayos documentado de 1753; Tales y el ámbar como tradición;
      contextos colombianos para el pararrayos y Saber 11.
- [ ] Confirmar cómo se repartieron el 7 y el 9 de septiembre la notación científica y la
      primera aproximación a Coulomb y al campo.

### Geometría 5°
- [ ] Revisión 1 del plan de la guía (`guia-periodo-I-ubicacion.plan.md`): ¿escala sencilla en
      el tema 4? ¿nombrar los cuatro cuadrantes aunque solo se trabaje el primero?
- [ ] Confirmar la semana 12 (evaluación) tras el paso al calendario oficial.
- [ ] Revisar el paquete de la semana 03 (dictado el 2026-09-14).

### Geometría 8°
- [ ] Revisión 1 del plan de la guía (`guia-periodo-I-triangulos.plan.md`): ¿DBA 7 para la
      fila 003? ¿repaso de las filas 001–002? ¿Tales después de Pitágoras? ¿«teorema de Tales»
      en el sentido español (paralelas)?
- [ ] Confirmar la semana 12 (evaluación sin sesión de repaso).
- [ ] Aprobar las 17 abiertas de `angulos-8`.

### Cursos aprobados el 2026-09-18 — preguntas abiertas
Los 11 planes que estaban como propuesta quedaron **aprobados** (reparto por trimestre, ritmo de
evaluación e hilo del trimestre I, en todos la opción recomendada). Con eso, **los 16 cursos
tienen plan anual aprobado**. Lo que sigue pendiente es solo responder estas preguntas; la
docente las contesta una por una y aquí se van tachando.

- [x] **Álgebra 9°** — hilo A: Al-Juarismi y el nacimiento del álgebra. Sin preguntas abiertas.
- [x] **Geometría 6°** — hilo 1: La geometría del fútbol. Sin preguntas abiertas.
- [x] **Geometría 7°** — hilo 1: Escher, el arte de mover figuras. Sin preguntas abiertas.
- [x] **Geometría 9°** — hilo A: Eratóstenes mide la Tierra con una sombra. Sin preguntas abiertas.
- [ ] **Física 9°** — hilo A: De Aristóteles a Galileo. Exposiciones **resuelto** (2026-09-19):
      quedan 7 y ocupan las sesiones 002 y 003 completas, 4 y 3; esas dos sesiones van sin taller
      y los talleres del trimestre pasan a la 005 y la 007. Falta: ¿quién hizo el proyecto de la
      semana 01 (primera ley / presión atmosférica)?
- [ ] **Física 10°** — hilo A: De la inercia a los *Principia*. Falta: ¿vieron cinemática en 9°?
      De la respuesta depende si el repaso son 2 sesiones o 4.
- [ ] **Trigonometría 10°** — hilo A: Medir lo inalcanzable. Falta: ¿leyes del seno y del coseno
      en el trimestre II? ¿Conversión de unidades inglesas a métricas?
- [ ] **Geometría 3°** — hilo A: *El renacuajo paseador*. Falta: ¿hubo prueba diagnóstica?
- [ ] **Geometría 4°** — hilo A: *La vuelta al mundo en 80 días*. Falta: ¿hasta dónde llegó la
      sesión 002?
- [ ] **Geometría 10°** — hilo A: Ubicarse en la Tierra. Falta: dónde va el examen del
      trimestre III (no hay sesión en su semana de evaluación).
- [ ] **Geometría 11°** — hilo A: LORAN, ubicar un barco con dos hipérbolas. Falta: ¿uso las
      preguntas ICFES 15, 37 y 41?
- [ ] **Física 9°, trimestre III:** tampoco hay sesión en su semana de evaluación (semanas
      36–37, lunes festivos). Decidir dónde va ese examen.

### Lo que se dictó y aún no está registrado
Contárselo a Claude para registrarlo en `programacion.csv` (o escribirlo en la bitácora):
- [ ] Sesiones del 2026-09-14 en adelante de todos los cursos (6°, Física 9°, Geometría 9° y 10°
      tuvieron clase ese día; 7° el 15).
- [ ] Geometría 9°, sesión 002 (2026-09-10): la bitácora no la menciona.

## 3. Trabajo de Claude que espera una decisión

- [ ] **Guías, etapa B y C** de Física 11°, Geometría 5° y Geometría 8°: después de su Revisión 1.
- [ ] **Guía de Álgebra 8°:** descomentar los 2 ejercicios manuales y recompilar después de la
      Revisión 2.
- [ ] **Cálculo 11°:** paquetes de las semanas 03–04, después de decidir la recuperación de las
      semanas 01–02.
- [x] **Cursos con propuesta:** filas del trimestre I llenas en `programacion.csv` (2026-09-17).
- [ ] **Cursos con propuesta:** escribir la guía con el proceso de tres etapas (hoy solo hay el
      borrador de la tanda rápida) de cada curso.
- [ ] **Paquetes semanales** de Álgebra 8° y Geometría 5° desde la semana 05; de Geometría 8°
      desde la semana 05 y de Física 11° desde la semana 05 (las semanas 03 y 04 ya están).
- [ ] **Semanas 03 y 04 que faltan:** Geometría 3°, 4°, 6°, 9° y 10°, Física 9° y 10°, y la
      semana 04 de Geometría 7°, Álgebra 9° y Trigonometría 10°. Desde el 2026-09-17 todas
      tienen lleno su `programacion.csv`, así que ya se pueden escribir sin esperar la
      aprobación; las filas son provisionales y la docente puede corregirlas.
- [ ] **Verificar antes de escribir cada guía** los datos históricos marcados como no
      verificados en los planes (p. ej. Eratóstenes, Hiparco, Escher en la Alhambra, el balón
      Telstar, alcances de LORAN, Plutarco *Moralia* 147A, la base de la pirámide).

## 4. Correcciones pendientes de verificar

- [ ] Física 11°: la referencia a los DBA de Ciencias Naturales (ISBN y año) se copió de la guía
      anterior sin verificar; el de Matemáticas estaba mal.
- [ ] Geometría 5°: el autor de la entrada de la Stanford Encyclopedia sobre Descartes.
- [ ] Errores encontrados en recursos, para avisar a la docente:
  - Guía de apoyo de Física 11°, cap. 1: atribuye a Gilbert las cargas vítrea y resinosa (fue
    du Fay, 1733); «Keike Kamerling Onnes» por Heike Kamerlingh Onnes; lectura de 6,25 sin el 6.
  - Módulo de Geometría: su primer criterio de congruencia dice que dos ángulos iguales bastan
    (eso da semejanza, no congruencia).

## 5. Repositorio

- [x] **Las guías del trimestre I de Geometría 9° y 11° ya compilan** (2026-09-18). Era el
      paquete `txfonts`, que faltaba en la lista de `tlmgr install` del workflow — la misma
      causa que los `clase.tex` de la semana 03. Quedó dicho aquí que «no es un paquete que
      falte»: **era exactamente eso**, y el diagnóstico por el `.aux` (que la compilación moría
      en tal tema) apuntaba al sitio equivocado, porque el `.aux` se queda donde iba, no donde
      está el error. Para la próxima: el mensaje del CI manda sobre cualquier deducción hecha
      desde los archivos.
- [x] Una compilación fallida ya no borra el PDF ni el `.aux` que estaban bien
      (`tools/compilar-pdfs.sh` los recupera; el workflow usa `git add --ignore-removal`)
      (2026-09-17).
- [x] `.claude/worktrees/` (copias de trabajo de los agentes) agregado a `.gitignore` (2026-09-14).
