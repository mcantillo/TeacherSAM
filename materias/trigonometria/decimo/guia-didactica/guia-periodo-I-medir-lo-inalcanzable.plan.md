# Plan de la guía — Trigonometría 10° · Trimestre I (etapas A y B)

> **Borrador de generación rápida (2026-09-14):** etapas A, B y C en una sola pasada, sin las
> revisiones intermedias de la docente. Se apoya en la **propuesta** de `curriculo/plan-anual.md`
> (sesiones 009–044), que aún no está aprobada ni escrita en `programacion.csv`: si la docente
> cambia temas o subtemas, esta guía se ajusta.

## Datos

| | |
|---|---|
| Asignatura | Trigonometría |
| Grado | 10° |
| Trimestre | I (semanas 03–12; sesiones 009–048 de la propuesta) |
| Archivo | `guia-periodo-I-medir-lo-inalcanzable.tex` |
| Título | Triángulos, ángulos y arcos |
| Hilo | **Medir lo inalcanzable**: de Tales y la sombra de la pirámide a la Comisión Corográfica de Codazzi |
| Registro | Juvenil (7°–11°): definiciones formales, citas con fuente, justificar y generalizar |

## Por qué este hilo (opción A de `plan-anual.md`)

- Sigue el orden exacto de los temas: semejanza (Tales, que retoma el refuerzo de la semana 02)
  → razones y tablas (Hiparco) → resolver con cuidado (Hipatia revisando cálculos del
  *Almagesto*) → medición indirecta (triangulación de la Misión Geodésica) → la vuelta y el grado
  → el ángulo como fracción de vuelta y el arco (Eratóstenes) → coordenadas angulares (Codazzi).
- Trae historia latinoamericana y colombiana verificable (Quito 1736–1744; Nueva Granada 1850).
- Da pie a la actividad planeada del clinómetro en el patio (sesión 027).
- La opción B (de la cuerda al seno) solo sirve de verdad para el paso al círculo unitario; la C
  (navegar sin GPS) tiene menos historia comprobable y se cruza con Geometría 10°.

## DBA y evidencias

Fuente: `dba/matematicas/grados/grado10.tex` (texto literal).

**DBA 4** — «Comprende y utiliza funciones para modelar fenómenos periódicos y justifica las soluciones.»

| Evidencia | Temas |
|---|---|
| Reconoce el significado de las razones trigonométricas en un triángulo rectángulo para ángulos agudos, en particular, seno, coseno y tangente. | 1–4 |
| Calcula algunos valores de las razones seno y coseno para ángulos no agudos, auxiliándose de ángulos de referencia inscritos en el círculo unitario. | 5–8 (solo el comienzo: ángulos cuadrantales y del primer cuadrante; el resto en el trimestre II) |

El DBA 1 (irracionales √2, √3, π) aparece como apoyo en los temas 2 y 6, pendiente de la
pregunta 1 del plan anual; no se pone caja de DBA 1 en la guía.

## Frase introductoria

«Está escrito en lengua matemática, y sus caracteres son triángulos, círculos y otras figuras
geométricas, sin los cuales es imposible entender humanamente una palabra.» — Galileo Galilei,
*Il Saggiatore* (1623), cap. 6 (trad. propia). Original: «Egli è scritto in lingua matematica, e i
caratteri son triangoli, cerchi, ed altre figure geometriche, senza i quali mezi è impossibile a
intenderne umanamente parola». Encaja: triángulos (temas 1–4) y círculos (temas 5–8).

## Marco teórico (resumen; el texto completo está en el `.tex`)

1. **Tales y la sombra** [mactutortales]: la anécdota de la altura de las pirámides la cuentan
   siglos después Diógenes Laercio (citando a Jerónimo), Plinio y Plutarco; solo la versión de
   Plutarco usa triángulos semejantes. Se presenta como anécdota.
2. **Eratóstenes (276–194 a. C.)** [mactutoreratostenes]: sombra al mediodía del solsticio en
   Siena y Alejandría, 7°12′ = 1/50 de vuelta, 250 000 estadios; su obra se perdió y la conocemos
   por Cleómedes, Teón de Esmirna y Estrabón; el estadio medía entre 157,2 y 166,7 m (incierto).
3. **Hiparco (c. 190–120 a. C.)** [mactutorhiparco]: primera tabla de cuerdas; «algunos
   historiadores» lo consideran el fundador de la trigonometría (no se dice «padre» como hecho).
4. **Hipatia (m. 415)** [mactutorhipatia, cameron1990]: ayudó a Teón en su comentario al
   *Almagesto*; el título del libro III dice que la edición fue revisada por «la filósofa Hipatia,
   mi hija» (cita, trad. propia de la inglesa). Cuánto aportó se discute: se dice así.
5. **Misión Geodésica (1735–1744)** [mactutorlacondamine, mactutorjuan]: Godin, Bouguer,
   La Condamine, con Jorge Juan y Antonio de Ulloa; triangulación entre Quito y Cuenca, base en la
   llanura de Yaruquí de más de 12 km, unos 3° de latitud; Newton (Tierra achatada en los polos)
   frente a Descartes.
6. **Codazzi y la Comisión Corográfica** [bnc]: contrato del 1 de enero de 1850; Codazzi nació en
   Lugo (Italia) en 1793 y murió el 7 de febrero de 1859; la *Carta* y el *Atlas de los Estados
   Unidos de Colombia* se publicaron en 1865.

## Temas

Los ocho valores distintos de `tema` de las sesiones 009–044 de la propuesta, en orden.

| # | Tema | Etiqueta | Hilo | Aplicación |
|---|---|---|---|---|
| 1 | Razones trigonométricas | `tema:razones` | Tales y la sombra | la calculadora científica |
| 2 | Ángulos especiales | `tema:angulosespeciales` | Hiparco y la cuerda de 60° | la escuadra de dibujo (30-60 y 45) |
| 3 | Resolución de triángulos rectángulos | `tema:resolucion` | Hipatia revisa los cálculos | cifras significativas en ingeniería |
| 4 | Aplicaciones del triángulo rectángulo | `tema:aplicaciones` | la triangulación de la Misión Geodésica | el clinómetro casero |
| 5 | Ángulos como rotación | `tema:rotacion` | los 360° y el cielo que gira | la Tierra gira 15° por hora |
| 6 | Radianes | `tema:radianes` | Eratóstenes: el ángulo como fracción de vuelta | la calculadora en modo RAD |
| 7 | Arco y sector circular | `tema:arcosector` | Eratóstenes mide la Tierra | un grado de meridiano (≈ 111 km) |
| 8 | Círculo unitario | `tema:circulounitario` | Codazzi y los mapas de la Nueva Granada | latitud y longitud son ángulos |

Explicaciones: definiciones de seno, coseno y tangente; independencia del tamaño por semejanza;
triángulo equilátero partido y cuadrado partido; resolver con dos lados o con lado y ángulo;
ángulos de elevación y depresión; posición estándar, sentido, coterminales, cuadrantes,
sexagesimal; radián, conversión; s = rt y A = ½r²t; P(θ) = (cos θ, sen θ).

## Cierre del hilo

De la sombra de un palo a un mapa de todo un país: lo inalcanzable se mide con un lado conocido
y ángulos. Anuncio del trimestre II: el círculo unitario completo (ángulos no agudos, signos por
cuadrante, las otras funciones e identidades).

## Evaluación (matriz)

- **Saber:** define las razones y explica por qué dependen solo del ángulo; conoce los valores
  exactos de 30°, 45° y 60°; relaciona grados, radianes y arcos.
- **Hacer:** resuelve triángulos rectángulos y problemas de medición indirecta; convierte
  ángulos y calcula arcos y sectores; ubica puntos del círculo unitario.
- **Ser:** revisa sus cálculos (unidades, modo de la calculadora, redondeo) y los de otros.
- **Convivir:** trabaja en equipo en la medición del patio y valora el trabajo colectivo de las
  expediciones científicas.

## Referencias (verificadas el 2026-09-14)

| Clave | Referencia | Veredicto | Corrección | URL |
|---|---|---|---|---|
| galileo1623 | Galilei, G. (1623). *Il Saggiatore*, cap. 6. Roma: Mascardi. | confirmada (texto) | «trad. propia» | https://it.wikisource.org/wiki/Il_Saggiatore/6 |
| mactutortales | MacTutor, *Thales of Miletus* | confirmada | anécdota tardía (D. Laercio, Plinio, Plutarco) | https://mathshistory.st-andrews.ac.uk/Biographies/Thales/ |
| mactutoreratostenes | MacTutor, *Eratosthenes* | confirmada | estadio incierto; fuente Cleómedes | https://mathshistory.st-andrews.ac.uk/Biographies/Eratosthenes/ |
| mactutorhiparco | MacTutor, *Hipparchus* | confirmada | «fundador» solo según algunos historiadores | https://mathshistory.st-andrews.ac.uk/Biographies/Hipparchus/ |
| mactutorhipatia | MacTutor, *Hypatia* | confirmada | — | https://mathshistory.st-andrews.ac.uk/Biographies/Hypatia/ |
| cameron1990 | Cameron, A. (1990). Isidore of Miletus and Hypatia: On the editing of mathematical texts. *GRBS*, 31, 103–127. | confirmada | la inscripción del libro III se cita desde la trad. inglesa (Encyclopedia.com) | https://grbs.library.duke.edu/article/view/4171 · https://www.encyclopedia.com/people/philosophy-and-religion/philosophy-biographies/hypatia |
| mactutorlacondamine | MacTutor, *Charles-Marie de La Condamine* | confirmada (1735, Quito 4 jun. 1736, Quito–Cuenca, triangulación) | — | https://mathshistory.st-andrews.ac.uk/Biographies/La_Condamine/ |
| mactutorjuan | MacTutor, *Jorge Juan* | confirmada (Juan y Ulloa, 1735–1744, base de Yaruquí > 12 km, ~3°) | — | https://mathshistory.st-andrews.ac.uk/Biographies/Santacilia/ |
| bnc | Biblioteca Nacional de Colombia, *Mapeando*, cap. 5 «La Comisión Corográfica» | confirmada (1850, Codazzi 1793–1859, 1865) | — | https://www.bibliotecanacional.gov.co/es-co/colecciones/biblioteca-digital/mapeando/Paginas/capitulocinco.html |
| icfes2026 | Icfes (2026). *Cuadernillo de preguntas Matemáticas Saber 11.º*, pregunta 29 | archivo local | textual, con crédito | recursos/matematicas/icfes/ |
| mendba | MEN (2016). *DBA V.2 Matemáticas* | confirmada | — | https://gblumen.mineducacion.gov.co/cgi-bin/koha/opac-detail.pl?biblionumber=4785 |
| quintero | Quintero Palomino, A. (s. f.). *Conceptos de las funciones trigonométricas y la resolución de triángulos para el grado 10.º* | archivo local (portada) | — | recursos/matematicas/Guías pedagógicas Matemáticas/ |
| — | Cali, 3°27′ N (aplicación del tema 8) | confirmada | — | https://www.cali.gov.co/publicaciones/geografia_de_cali_pub |

**Quitado o rebajado al verificar:** «Hiparco, padre de la trigonometría» (→ «algunos
historiadores»); el valor de 110,61 km por grado de la Misión (solo en una enciclopedia
derivada de Wikipedia: no se usa); que la Comisión Corográfica midiera por triangulación (no se
encontró fuente: no se dice); la versión de que Hipatia «editó el *Almagesto*» (discutida: se dice
que revisó la edición, según la inscripción).

## Etapa B — ejercicios (solo del banco)

Regla del usuario (2026-09-15): la guía usa **únicamente** ejercicios que ya estaban en el banco
(`verificado`). Se escribieron ejercicios nuevos en un primer borrador
(`trigonometria-guia-10.py`), pero se **borraron** sin registrarlos (nunca pasaron a
`verificados.json`). **E** = ejemplo resuelto. Todos son reutilizados.

| Tema | Uso | Id | Enunciado (corto) | Respuesta | Estado |
|---|---|---|---|---|---|
| 1 | E | razones-trigonometricas-10-013 | hipotenusa 35, 29°: cateto opuesto | ≈ 17,0 | verificado |
| 1 | 1 | razones-trigonometricas-10-001, 003, 005 | calculadora | 0,6600; 1,3968; 0,6534 | verificado |
| 1 | 2 | razones-trigonometricas-10-007, 009 | ángulo con la razón inversa | 12,5°; 17,2° | verificado |
| 1 | 3 | razones-trigonometricas-10-014 | hipotenusa 60, 43°: cateto adyacente | ≈ 43,9 | verificado |
| 1 | 4 | razones-trigonometricas-10-015 | opuesto 10, 14°: hipotenusa | ≈ 41,3 | verificado |
| 2 | 1 | razones-trigonometricas-10-054 | hexágono inscrito, r = 4 | P = 24; A = 24√3 ≈ 41,6 | verificado |
| 2 | 2 | razones-trigonometricas-10-056 | estrella de David en r = 1 | √3 ≈ 1,73 | verificado |
| 3 | E | razones-trigonometricas-10-020, 028 | un ángulo y la hipotenusa; dos catetos | ver banco | verificado |
| 3 | 1 | razones-trigonometricas-10-019, 022 | lado y ángulo | ver banco | verificado |
| 3 | 2 | razones-trigonometricas-10-025, 030 | dos lados | ver banco | verificado |
| 3 | 3 | razones-trigonometricas-10-021, 046 | lado y ángulo; cateto e hipotenusa | ver banco | verificado |
| 4 | E | razones-trigonometricas-10-018 | poste visto desde dos puntos | x ≈ 17,5 | verificado |
| 4 | 1 | razones-trigonometricas-10-033 | colina: 26 por cada 100 | ≈ 14,6° | verificado |
| 4 | 2 | razones-trigonometricas-10-050 | torre a 600 m, elevación y depresión | ≈ 448 m | verificado |
| 4 | 3 | razones-trigonometricas-10-017 | dos triángulos con cateto común 20 | ≈ 66,6 | verificado |
| 4 | 4 | razones-trigonometricas-10-053 | diagonal del cubo y de la cara | ≈ 35,3° | verificado |
| 5 | 1 | circulo-unitario-10-028, 032 | cos(−720°), sen 900° | 1; 0 | verificado |
| 5 | 2 | angulos-radianes-10-035 | minutero y horario | 2π; π/6; 10π (negativos) | verificado |
| 6 | E | angulos-radianes-10-070 | 33° y 9π/4 | 11π/60; 405° | verificado |
| 6 | 1 | angulos-radianes-10-001, 003, 010 | a radianes | 2π/3; 7π/4; −7π/3 | verificado |
| 6 | 2 | angulos-radianes-10-017, 022 | a grados | 840°; 171,9° | verificado |
| 6 | 3 | angulos-radianes-10-049, 050 | 23 revoluciones; (60/π)° | 46π; 1/3 | verificado |
| 7 | E | angulos-radianes-10-071 | rueda de 30 cm, 100 vueltas | ≈ 188,5 m | verificado |
| 7 | 1 | angulos-radianes-10-033 | radio con s y t | 3 cm | verificado |
| 7 | 2 | angulos-radianes-10-054, 056 | arcos en r = 4,25 cm | 25,5 cm; ≈ 37,8 cm | verificado |
| 7 | 3 | angulos-radianes-10-058 | bicicleta de María | ≈ 301,6 m | verificado |
| 7 | 4 | angulos-radianes-10-068 | superficie lateral del cono (argumentación) | πRL | verificado |
| 8 | 1 | circulo-unitario-10-017, 018, 019, 020 | cuadrantales | 1; −1; 0; 0 | verificado |
| 8 | 2 | angulos-radianes-10-036, 037, 038 | cuadrante tras recorrer 3; 4,8; 100 | II; IV; IV | verificado |
| S11 | 1 | icfes-cuadernillo-2026-044 | rueda de 10 sectores (textual) | **B** | verificado |
| S11 | 2 | icfes-cuadernillo-2026-022 | corte a la mitad de h, sen 45° (textual) | **C** | verificado |
| S11 | 3 | icfes-cuadernillo-2026-023 | cartabón de 32 cm (textual) | **B** | verificado |

Las figuras de las preguntas del Icfes se recortaron del PDF, en gris y sin cambios
(`figuras/icfes-2026-pregunta-22.png`, `-23.png`, `-44.png`).

### Pendientes: lo que el banco no cubre (no se inventó nada)

Las dos evidencias del DBA 4 que toca el trimestre tienen ejercicios. Quedan sin ejercicio:

- **Justificar / encontrar el error** en los temas 1–6 y 8 (el DBA dice «justifica las
  soluciones»; `crear-guia` pide uno por tema): el banco no tiene ninguno del trimestre I. Solo el
  tema 7 tiene uno (cono, `angulos-radianes-10-068`). Candidatos pendientes: por qué la razón no
  depende del tamaño (semejanza); el error «sen 30° + sen 30° = sen 60°».
- **Ángulos coterminales y cuadrantes en grados** (tema 5): solo hay ejercicios que los usan
  para hallar valores (`circulo-unitario-10-027`…`032`).
- **Valores exactos de 30°, 45°, 60° en el triángulo** (tema 2): el banco los tiene en radianes y
  para el trimestre II (`otras-funciones-trigonometricas-10-011`…); en la guía se usaron el
  hexágono y la estrella de David.
- **Contextos en metros y colombianos** del triángulo rectángulo: casi todos los problemas del
  banco están en pies (escalera, faro, cometa, Torre Eiffel…); se usaron solo los que no dependen
  de la unidad o están en metros. La conversión a metros (pedida en la tarea) queda pendiente de
  la decisión de `recursos/banco/PENDIENTES.md` («¿Pasamos a unidades colombianas…?»).
- **Eratóstenes y la triangulación** (hilo): solo en la narración, sin ejercicio.
- **Pregunta 29 del Icfes** (coseno de la escalera): encaja perfecto, pero no está en el banco
  (`icfes-cuadernillo-2026-geometria.py` la dejó fuera porque sus datos están en la figura).
- **Clinómetro en el patio** (taller de la sesión 027): sin ejercicio en el banco.

## Errores encontrados en el módulo de 10° (Temas 1–2)

- Tabla de ángulos especiales: «Tan45° = √2/2»; es **1**.
- «el coseno de 6» (por θ); «0 a = √3» (por «o»); paréntesis sin cerrar en el campanario.
- Problema 7: «escalera de 20 pies **de altura**» (es la longitud); problema 10 remite al
  «problema 35» (es el 8).
- Tema 2, 1f y 1p: «(150/77)°» y «(20/77)°» (π dañado); 14b «(18/13π)°» sigue pendiente.
- Todo en pies, pulgadas y millas: en la guía se pasó a metros.

## Preguntas para la docente

1. Aprobar el plan del trimestre I (sesiones 009–048) y escribirlo en `programacion.csv`.
2. ¿Hilo A («Medir lo inalcanzable»)? Es el recomendado y el que usa este borrador.
3. ¿Se agregan al banco los ejercicios de la lista «Pendientes» (sobre todo los de justificar y la pregunta 29 del Icfes)?
4. ¿DBA 1 como apoyo (√2, √3, π)?
