# Pendientes

Lista de lo que falta, agrupada por quién lo desbloquea. Se actualiza cada vez que se abre o se
cierra un pendiente (ver `CLAUDE.md`); lo ya hecho pasa a `CHANGELOG.md`. Los pendientes del
banco de ejercicios están aparte, en `recursos/banco/PENDIENTES.md`.

Última actualización: 2026-09-15.

## 0. Urgente — desbloquea clases de esta semana

- [ ] **Aprobar el trimestre I de Geometría 7° y Álgebra 9°** (o corregir la propuesta de
      su `plan-anual.md`). Sus filas de `programacion.csv` están vacías desde la semana 03.
      Los paquetes del 15 al 18 de septiembre ya están escritos, pero marcados
      **BORRADOR**; en cuanto se apruebe se llenan las filas y se les quita la marca.
- [ ] **Geometría 7° no tiene ejercicios verificados** para el trimestre I: el banco solo
      trae `angulos-7-003`, que ya usa la guía. Por eso la sesión 003 va sin tarea aunque
      la propuesta la marque. Hay que escribir y verificar ejercicios de giros,
      traslaciones, rotaciones, reflexiones y vistas para 7°.
- [ ] **Irracionales en 8° y en 9°:** el trimestre I de los dos cursos trabaja los mismos
      temas y los mismos ejercicios (`irracionales-8`). Decidir el reparto antes de la
      semana 04, o el trimestre se repite entero.
- [ ] **Guías de Geometría 9° y 11°:** el CI no las compila (borró sus PDF en `ca898e5`).
      Falta reproducir el error y corregirlo; hasta entonces no hay PDF que imprimir.
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

### Cursos con propuesta de plan anual y trimestre I (pendientes de aprobación)
Para cada uno: aprobar el reparto por trimestres, el ritmo de evaluación y un hilo del
trimestre I (el plan propone 2–3), y responder sus preguntas (listadas en su `plan-anual.md`).

- [ ] **Álgebra 9°** — hilo sugerido: Al-Juarismi y el nacimiento del álgebra.
- [ ] **Física 9°** — hilo sugerido: De Aristóteles a Galileo. ¿Quién hizo el proyecto de la
      semana 01 (primera ley / presión atmosférica)? ¿Cuántas sesiones de exposiciones? Examen
      del trimestre III (no hay sesión en su semana de evaluación).
- [ ] **Física 10°** — hilo sugerido: De la inercia a los *Principia*. ¿Vieron cinemática en 9°?
- [ ] **Trigonometría 10°** — hilo sugerido: Medir lo inalcanzable. ¿Leyes del seno y del coseno
      en el trimestre II? ¿Unidades inglesas a métricas?
- [ ] **Geometría 3°** — hilo sugerido: *El renacuajo paseador*. ¿Hubo prueba diagnóstica?
- [ ] **Geometría 4°** — hilo sugerido: *La vuelta al mundo en 80 días*. ¿Hasta dónde llegó la
      sesión 002?
- [ ] **Geometría 6°** — hilo sugerido: La geometría del fútbol. Reparto con 7°.
- [ ] **Geometría 7°** — hilo sugerido: Escher y las transformaciones.
- [ ] **Geometría 9°** — hilo sugerido: Eratóstenes midiendo la Tierra.
- [ ] **Geometría 10°** — hilo sugerido: Ubicarse en la Tierra. Examen del trimestre III (no hay
      sesión en su semana de evaluación).
- [ ] **Geometría 11°** — hilo sugerido: LORAN, ubicar un barco con dos hipérbolas. ¿Usar las
      preguntas ICFES 15, 37 y 41?

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
- [ ] **Cursos con propuesta:** llenar las filas del trimestre I en `programacion.csv` y escribir
      la guía (tres etapas) de cada curso, a medida que se aprueben.
- [ ] **Paquetes semanales** de Álgebra 8° y Geometría 5° desde la semana 05; de Geometría 8°
      desde la semana 05 y de Física 11° desde la semana 05 (las semanas 03 y 04 ya están).
- [ ] **Semanas 03 y 04 que faltan:** Geometría 3°, 4°, 6°, 9° y 10°, Física 9° y 10°, y la
      semana 04 de Geometría 7°, Álgebra 9° y Trigonometría 10°. Las de Geometría 10° y
      Trigonometría 10° no necesitan aprobación (su `programacion.csv` ya está lleno); las
      demás sí.
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

- [x] `.claude/worktrees/` (copias de trabajo de los agentes) agregado a `.gitignore` (2026-09-14).
