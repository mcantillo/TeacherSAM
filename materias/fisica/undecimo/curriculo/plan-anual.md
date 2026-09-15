# Plan anual 2026–2027 — Física 11°

Reparto propuesto el 2026-09-14 para quedar **sincronizado con Cálculo 11°** (ver
`materias/calculo/undecimo/curriculo/plan-anual.md`) y **aprobado por la docente ese mismo
día**, junto con el plan del trimestre I y su hilo. El detalle por sesión se hace en la planeación de cada periodo, en
`programacion.csv`.

Trimestre I pasado al calendario oficial el 2026-09-14 (21 sesiones en vez de 23): las
sesiones 001–019 quedaron como estaban; en la semana 12, la de evaluación, la 020 es el repaso
general (con el pararrayos y la jaula de Faraday) y la 021 la evaluación del periodo. Se
perdió el quiz de campo eléctrico. **Pendiente de confirmar con la docente**, incluido si
el quiz de campo pasa a la sesión 019. *(Aprobado tal como está el 2026-09-14: el quiz de
campo no se reubica.)*

## DBA y estándares de la asignatura

Fuentes: `dba/naturales/grados/grado11.tex` (los tres DBA de física de grado 11) y
`dba/naturales/estandares-fisica.md` (Estándares MEN 2004, grupo 10°–11°, entorno físico), que
son los que permiten repartir los temas dentro de cada DBA.

| DBA | Enunciado (resumido) | Trimestre |
|---|---|---|
| 2 | La interacción de cargas en reposo genera fuerzas eléctricas; en movimiento, fuerzas magnéticas | I (electrostática) y II (magnetismo) |
| 3 | Relaciones entre corriente y voltaje en circuitos resistivos en serie, paralelo y mixtos | II |
| 1 | La propagación del sonido y de la luz como fenómenos ondulatorios | III |

Estándares del grupo 10°–11° que sostienen el reparto: «establezco relaciones entre fuerzas
macroscópicas y fuerzas electrostáticas», «establezco relaciones entre campo gravitacional y
electrostático y entre campo eléctrico y magnético», y «relaciono voltaje y corriente con los
diferentes elementos de un circuito eléctrico complejo y para todo el sistema». Ondas, sonido
y luz figuran en los estándares de 8°–9°, pero el DBA 1 de 11° los retoma con más profundidad
(ver la nota final de `estandares-fisica.md`).

## Reparto por trimestre

| Trimestre | Semanas | Sesiones | DBA | Contenido |
|---|---|---|---|---|
| I | 01–12 | 21 | 2 (primera parte) | Carga eléctrica: electrización por frotamiento y contacto, conductores y aislantes. Ley de Coulomb. Campo eléctrico y líneas de campo. Notación científica y orden de magnitud como herramienta de trabajo. |
| II | 13–26 | 25 | 3 y 2 (segunda parte) | Corriente y voltaje. Ley de Ohm. Resistencias en serie, paralelo y circuitos mixtos. Potencia eléctrica. Carga y descarga de un condensador. Magnetismo: cargas en movimiento, experimento de Oersted, campo magnético y electroimán. |
| III | 27–37 | 19 | 1 | Ondas mecánicas y electromagnéticas. Sonido: tono, intensidad (escala de decibelios) y audibilidad. Luz: reflexión, refracción, interferencia, difracción y polarización; color y visibilidad. Cierre: la luz como onda electromagnética. |

Criterios del reparto:

- El trimestre I ya arrancó con electrostática (ley de Coulomb y campo eléctrico, según la
  bitácora de la docente): el reparto respeta lo que ya se dictó en lugar de reordenarlo.
- El DBA 2 se parte en dos: cargas en reposo en el I y cargas en movimiento en el II, junto
  al DBA 3, porque el magnetismo necesita la idea de corriente para tener sentido.
- Las ondas quedan en el III porque el hilo del trimestre (Faraday y Maxwell) desemboca justo
  en la luz como onda electromagnética: el cierre del hilo es la apertura del tema.

## Sincronización con Cálculo 11°

Las dos asignaturas las dicta la misma docente y comparten el hilo conductor de los trimestres
II y III. La regla de la sincronización es que **la física llega primero con el fenómeno y el
cálculo llega después con el lenguaje**: ningún tema de Cálculo depende de física que todavía
no se haya visto.

| Trimestre | Física 11° | Cálculo 11° | Puente |
|---|---|---|---|
| I | Carga, ley de Coulomb, campo eléctrico | Números reales, desigualdades, inecuaciones, valor absoluto | Notación científica y orden de magnitud; el valor absoluto como distancia; intervalos para expresar rangos de medida. |
| II | Circuitos, ley de Ohm, potencia, condensador, magnetismo | Funciones como modelos | Ohm da la función lineal; las resistencias en paralelo, una racional; la potencia, una cuadrática; el condensador, la exponencial (y el logaritmo al despejar el tiempo); la ley de Coulomb del trimestre I, el inverso del cuadrado. |
| III | Ondas, sonido y luz | Límites, derivada y aplicaciones | La corriente como razón de cambio de la carga; la fuerza electromotriz como rapidez de cambio del flujo; el campo eléctrico definido como un límite; optimización de la potencia entregada. |

## Hilos conductores

| Trimestre | Hilo | Compartido con Cálculo 11° | Estado |
|---|---|---|---|
| I | De Tales al pararrayos: la carga que nadie veía (Tales, Gilbert, Coulomb, Franklin) | no (Cálculo I va con «La historia del infinito») | aprobado (2026-09-14) |
| II | Las leyes que se ven en una gráfica | sí | propuesto |
| III | Faraday no sabía matemáticas (Faraday experimenta, Maxwell lo escribe con derivadas, y la luz resulta ser una onda electromagnética) | sí | propuesto |

Las citas y fechas de estos hilos se verifican contra fuente antes de escribir cada guía, como
pide el procedimiento de `crear-guia`.

## Ritmo de evaluación

Aprobado el 2026-09-14. Dos sesiones semanales de 100 min (lunes 11:00 y miércoles 10:10), que
sí dan margen para explicar y evaluar el mismo día, a diferencia de los cursos de una sesión.

- **Taller** en la sesión del **lunes**, casi todas las semanas, dentro de los 100 min.
- **Tarea** asignada el **miércoles** y revisada el lunes siguiente.
- **Quiz** de unos 20 min al comienzo del **miércoles** de la semana en que cierra un tema
  (tres en el trimestre I: carga eléctrica, ley de Coulomb y campo eléctrico).
- En las semanas que pierden el lunes por festivo (2 y 16 de noviembre de 2026) queda solo la
  tarea del miércoles.
- La **última semana del trimestre** es de repaso y evaluación del periodo: sin taller ni quiz
  nuevos.
- Al menos un **laboratorio o demostración** por tema, siguiendo la columna «me aproximo al
  conocimiento como científico-a natural» de los estándares.

En el trimestre I esto da 7 talleres, 7 tareas y 2 quices (el tercero, de campo eléctrico,
se perdió al pasar al calendario oficial; ver arriba).

## Estado de la planeación

El **trimestre I ya está planeado sesión por sesión** en `programacion.csv` (clases 001–021,
DBA 2), en tres temas: la carga eléctrica (clases 004–008), la ley de Coulomb (009–014) y el
campo eléctrico (015–019), con repaso y evaluación del periodo en la semana 12. Las clases
001–003 quedaron registradas con lo que ya se dictó, según la bitácora de la docente
(`bitacora-2026-2027.md`): prueba
diagnóstica, notación científica y una primera aproximación a la ley de Coulomb y al campo
eléctrico. **Confirmar con la docente** cómo se repartieron esos contenidos entre la sesión del
lunes 7 y la del miércoles 9 de septiembre.

La **guía del estudiante del trimestre I** ya está escrita:
`guia-didactica/guia-periodo-I-electrostatica.tex`, con cuatro temas (`tema:notacion`,
`tema:carga`, `tema:coulomb`, `tema:campo`) y sección «Prepárate para Saber 11». Compilada
el 2026-09-14 (12 páginas, sin errores de `revisar_guia.py`); falta la revisión página por
página de la docente.

Los trimestres II y III se planean sesión por sesión al comenzar cada uno.

## Recursos principales

- `recursos/fisica/Guías pedagógicas Física/11 - Guia_de_Apoyo_Fenomenos_electromagneticos_grado_11_fisica.docx`
  (texto en `texto/`): corresponde a los trimestres I y II.
- `recursos/fisica/Guías pedagógicas Física/11 - Guia_de_Apoyo_Fenomenos_ondulatorios_grado_11_fisica.docx`
  (texto en `texto/`): corresponde al trimestre III.
  Ambas tienen errores de digitación y de unidades: verificar cada ejercicio antes de adaptarlo.
