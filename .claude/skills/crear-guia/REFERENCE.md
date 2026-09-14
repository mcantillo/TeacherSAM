# Referencia — guía del estudiante trimestral

## Bloque de datos (preámbulo)

```latex
\documentclass[11pt]{article}
\makeatletter\def\input@path{{../../../../plantillas/estilo/}}\makeatother
\usepackage{mmcantillo}
\tipodocumento{Guía del estudiante}
\asignatura{Cálculo}           % nombre de la asignatura, con tildes
\titulo{Los números reales: orden e infinito}
\grado{11°}
\periodo{I}                    % I, II o III
\hiloconductor{La historia del infinito}
% DBA: matematicas grado 11 · DBA 1 — <enunciado literal>
```

Los macros propios de cada guía (por ejemplo `\abierto`/`\cerrado` para la recta numérica)
van después del bloque de datos.

## Estructura y macros, en orden

| # | Parte | Macro | Reglas |
|---|---|---|---|
| 1 | Frase introductoria | `\frase{texto}{Autor, \emph{Obra} (año)}` | Cita real, con su fuente; en 3°–6° puede ser de literatura infantil de dominio público |
| 2 | Introducción | `\seccion{Introducción}` | Objetivo del trimestre en lenguaje sencillo, entrada al hilo, lista «Al terminar este trimestre podrás:» |
| 3 | DBA | `\begin{dba}[Grado 11 · DBA 5] … \end{dba}` | Texto literal; una caja por DBA |
| 4 | Marco teórico | `\seccion{Marco teórico}` + `\subsubsection*{…}` | Historia, conceptos y **todas** las citas (`\begin{cita}{Autor, fuente~\cite{k}} … \end{cita}`) |
| 5 | Temas | `\tema{Título}\label{tema:slug}` | Uno por tema del plan (ver bloque abajo) |
| 6 | Saber 11 (solo 9°–11°) | `\seccion{Prepárate para Saber 11}` | 3–5 preguntas de selección múltiple con `opciones*`; varía la letra correcta |
| 7 | Cierre | `\seccion{Cierre: …}` | Cierra la historia y anuncia el trimestre siguiente |
| 8 | Evaluación | `\matrizevaluacion{saber}{hacer}{ser}{convivir}`, `\autoevaluacion`, `\seguimientodocente` | Criterios propios del trimestre, nunca copiados; la matriz imprime su propio título |
| 9 | Referencias | `\begin{referencias} \bibitem{k} … \end{referencias}` | Cada `\cite` con su `\bibitem`, orden alfabético, formato APA sencillo |

### Bloque de un tema

```latex
\tema{Valor absoluto}\label{tema:valorabsoluto}
\begin{hilo} …el siguiente paso de la historia… \end{hilo}
…explicación: \begin{definicion}[…], \begin{teorema}[…], \begin{ejemplo}[…]…
\begin{aplicacion}[Tolerancias en la fabricación] …uso real y cierto… \end{aplicacion}
\begin{preguntas}
\pregunta … \espacio{3cm}      % sin puntos: la guía no se califica por ejercicio
\end{preguntas}
\begin{resumen} \begin{itemize} \item … \end{itemize} \end{resumen}
```

- **Etiquetas:** `tema:` + un slug sin tildes (`tema:sistemas`, `tema:valorabsoluto`). Las clases las citan con `\refguia{tema:slug}`.
- **Ejercicios:** entre 2 y 5 por tema, de dificultad creciente. Incluye al menos uno de argumentar o de encontrar el error (el DBA pide *justificar*) y uno en contexto.
- **Sub-ítems a), b), c):** van en `\begin{opciones*}(3)` y no en la misma línea (ver EXAMPLES.md).

## Citas: qué se puede usar

Solo citas con **fuente comprobable** (libro, carta, artículo, con fecha), y la traducción
marcada como «trad. propia». Estas ya están verificadas y usadas:

| Cita | Fuente |
|---|---|
| «La esencia de la matemática está precisamente en su libertad» (*gerade in ihrer Freiheit*) — Cantor | *Grundlagen einer allgemeinen Mannigfaltigkeitslehre* (1883), §8; *Gesammelte Abhandlungen*, p. 182 |
| «Del paraíso que Cantor creó para nosotros, nadie debe poder expulsarnos» — Hilbert | «Über das Unendliche», *Math. Annalen* 95 (1926), p. 170 |
| Carta de Gauss a Sophie Germain (original en francés) | 30 abr. 1807; trad. inglesa en Bucciarelli y Dworsky (1980), cap. 3 |
| «La filosofía está escrita en ese grandísimo libro… en lengua matemática» — Galileo | *Il Saggiatore* (1623) |
| «Si he visto más lejos es porque estoy de pie sobre hombros de gigantes» (*standing*, no «sentado») — Newton | Carta a R. Hooke, 5 feb. 1675/76 (juliano); original en la Historical Society of Pennsylvania |
| «La Máquina Analítica teje patrones algebraicos…» — Ada Lovelace | Nota A de su traducción de Menabrea, *Scientific Memoirs* 3 (1843), pp. 666–731 |
| «La matemática pura es… la poesía de las ideas lógicas» — Einstein | Carta sobre Emmy Noether, *NYT*, 4 may. 1935 |
| «El hijo de Rana, Rinrín Renacuajo…» — Rafael Pombo | *Cuentos pintados para niños* (1867) |

**Solo como paráfrasis, con referencia:** la doctrina pitagórica de que «todo es número»
(Aristóteles, *Metafísica* I.5); la leyenda de Hipaso («según la leyenda»); Hipatia (no se
conservan frases suyas). Muchas frases populares de Einstein, Tesla o Turing son apócrifas:
si no puedes dar la fuente primaria, **parafrasea la idea y atribúyela**.

Científicas que conviene incluir: Hipatia, Émilie du Châtelet, Sophie Germain, Ada Lovelace,
Marie Curie, Emmy Noether, Grace Hopper, Katherine Johnson, Maryam Mirzakhani.

## Verificación de referencias

Los modelos de lenguaje inventan referencias creíbles: autores reales con libros que no
existen, páginas equivocadas, citas apócrifas. Por eso **cada** `\bibitem`, `\frase` y
`\begin{cita}` se verifica en internet y lleva la evidencia en la línea anterior:

```latex
% verificado: https://doi.org/10.1007/BF01206605 — Math. Annalen 95 (1926), pp. 161–190
\bibitem{hilbert} Hilbert, D. (1926). Über das Unendliche. \emph{Mathematische Annalen}, 95, 161--190.
```

**Qué cuenta como evidencia (URL concreta):**
- Catálogos de bibliotecas (WorldCat, Biblioteca Nacional, Biblioteca Luis Ángel Arango) y páginas de la editorial.
- Página de la revista o el DOI (Springer, JSTOR, EuDML, GDZ Göttingen).
- Escaneos de obras antiguas en Archive.org, Wikisource, Gallica o Google Books.
- Sitios oficiales (MEN, NASA, ICFES).
- Para `recursos/`, la ruta local: `% verificado: recursos/matematicas/… (archivo local)`.

Wikipedia y los sitios de frases **no** son evidencia final: úsalos solo para encontrar la
fuente real.

**Qué se comprueba:**
- Referencia: que la obra exista con ese autor, título, año, editorial o revista, volumen y páginas. Si algo no coincide, se corrige.
- Cita: que exista en esa fuente, con esa redacción o ese sentido, y con esa fecha. Si es traducción, se marca «trad. propia».
- Datos históricos del marco teórico (fechas, quién hizo qué): se comprueban con la misma exigencia, aunque no lleven `\cite`.
- Si no aparece evidencia, la referencia o la cita **se quita** y la idea se parafrasea con otra fuente verificada.

En el informe de entrega va una tabla: referencia · veredicto · corrección · URL.

## Hilo conductor

- Una sola historia para todo el trimestre, con un paso por tema (`hilo`) y un cierre. Debe *conectar* con la matemática, no decorarla.
- Puede ser historia de la ciencia o literatura (Harry Potter, Narnia, El señor de los anillos…), según el registro del grado (`.claude/referencias/registro-grados.md`); *El señor de los anillos* y los libros finales de Harry Potter solo desde 7°.
- En obras con derechos, alude a personajes y situaciones y cita como máximo una frase.
- Se registra en la tabla «Hilos conductores» de `plan-anual.md`.

## Saber 11 (9°–11°)

- Selección múltiple con única respuesta, contextos colombianos y cantidades realistas.
- Adapta de «Prepárate para el ICFES» de los recursos y verifica que cada opción correcta lo sea.
- La guía no lleva las respuestas: dáselas a la docente en el informe de entrega.
