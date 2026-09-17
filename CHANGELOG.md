# Registro de cambios

Lo que ya se hizo, por fecha (lo más reciente primero). Lo que falta está en `PENDIENTES.md`.

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
