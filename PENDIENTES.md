# Pendientes

Lista de lo que falta, agrupada por quién lo desbloquea. Se actualiza cada vez que se abre o se
cierra un pendiente (ver `CLAUDE.md`); lo ya hecho pasa a `CHANGELOG.md`. Los pendientes del
banco de ejercicios están aparte, en `recursos/banco/PENDIENTES.md`.

Última actualización: 2026-09-17.

## 0. Urgente — desbloquea clases de esta semana

- [ ] **Faltan 11 paquetes de la semana 04** (clases del 21 al 25 de septiembre): Física 9° y
      10°, Álgebra 9°, Trigonometría 10° y Geometría 3°, 4°, 6°, 7°, 9°, 10° y 11°. La lista
      con día, sesión y advertencias está en `GUIA-CLAUDE-CODE.md`, sección 8.1. **Se hacen en
      Claude Code**, no en Cowork: allá sí se compilan y se revisan los PDF.

- [ ] **Quitar la marca BORRADOR** a los paquetes del 15 al 18 de septiembre de Geometría 7° y
      Álgebra 9°: sus planes quedaron **aprobados el 2026-09-18** y sus filas de
      `programacion.csv` están llenas, así que la advertencia que llevan impresa
      («las filas 005 y 006 están vacías», «la fila 003 está vacía») ya no es cierta. Hay que
      editar esos `clase.tex` y `tarea.tex` y recompilar.
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
tienen plan anual aprobado**. **El 2026-09-19 la docente respondió las siete preguntas abiertas:
esta sección ya no bloquea nada.** Los 11 cursos están listos para el paso 3 (la guía).

- [x] **Álgebra 9°** — hilo A: Al-Juarismi y el nacimiento del álgebra. Sin preguntas abiertas.
- [x] **Geometría 6°** — hilo 1: La geometría del fútbol. Sin preguntas abiertas.
- [x] **Geometría 7°** — hilo 1: Escher, el arte de mover figuras. Sin preguntas abiertas.
- [x] **Geometría 9°** — hilo A: Eratóstenes mide la Tierra con una sombra. Sin preguntas abiertas.
- [x] **Física 9°** — hilo A: De Aristóteles a Galileo. **Resuelto (2026-09-19):** quedan 7
      exposiciones y ocupan las sesiones 002 y 003 completas (esas dos sin taller; los talleres
      pasan a la 005 y la 007); y los experimentos de la semana 01 fueron **demostraciones de la
      docente**, no un proyecto de estudiantes — no hay nada que evaluar y la guía los retoma
      como enganche del hilo. Sin preguntas abiertas.
- [x] **Física 10°** — hilo A: De la inercia a los *Principia*. **Resuelto (2026-09-19):** la
      vieron a medias (MRU sí, MUA y caída libre no) → el repaso pasa a 3 sesiones (009–011),
      «Tercera ley» baja a 1 (020) y «Las tres leyes» se queda con 2. Sin preguntas abiertas.
- [x] **Trigonometría 10°** — hilo A: Medir lo inalcanzable. **Resuelto (2026-09-19):** seno y
      coseno se quedan en el trimestre II (el trimestre I no cambia) y **todo el material va en
      métricas** — los pies y millas de las fuentes se convierten antes de llegar al estudiante.
      Sin preguntas abiertas.
- [x] **Geometría 3°** — hilo A: *El renacuajo paseador*. **Resuelto (2026-09-19):** no hubo
      diagnóstico; el tema 1 arranca desde cero y la sesión 003 abre con un repaso de punto y
      línea. Sin preguntas abiertas.
- [x] **Geometría 4°** — hilo A: *La vuelta al mundo en 80 días*. **Resuelto (2026-09-19):** la
      sesión 002 fue solo la introducción; la 003 retoma el tema desde el principio y el reparto
      no cambia. Sin preguntas abiertas.
- [x] **Geometría 10°** — hilo A: Ubicarse en la Tierra. **Resuelto (2026-09-19):** el examen
      del trimestre III se adelanta a la sesión 029 (semana 35) y el repaso va en la 028. Sin
      preguntas abiertas.
- [x] **Geometría 11°** — hilo A: LORAN, ubicar un barco con dos hipérbolas. **Resuelto
      (2026-09-19):** sí, las preguntas ICFES 15, 37 y 41 van en la guía, con su formato
      original y citando la fuente. Sin preguntas abiertas.
- [x] **Física 9°, trimestre III: resuelto (2026-09-19)** — mismo arreglo que Geometría 10°:
      examen en la sesión 029 (semana 35), repaso en la 028.

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
