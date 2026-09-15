# Plantillas LaTeX — Área de Matemáticas

María Mercedes Cantillo · Colegio San Alberto Magno

Plantillas en español para quices, evaluaciones y documentos de clase (Cálculo, Física, Trigonometría, …), listas para escribir matemáticas y hacer gráficas. Diseñadas para imprimir en blanco y negro.

## Estructura

```
plantillas/
├── estilo/                 ← compartido por todas las plantillas (no duplicar)
│   ├── mmcantillo.sty      diseño: encabezado, pie, preguntas, cajas, gráficas
│   └── logo-colegio.png
├── quiz/quiz.tex           quiz corto
├── evaluacion/evaluacion.tex   evaluación con secciones
├── documento/documento.tex     clase, taller, tarea o material de estudio
├── guia-trimestral/guia-trimestral.tex   guía del estudiante (una por periodo) — ejemplo Cálculo 11°
│   └── guia-geometria-3.tex    ejemplo para primaria: Geometría 3°
└── guia-didactica/         formato institucional de la Guía Didáctica (independiente)
```

Cada plantilla carga el estilo y el logo desde `../estilo/`, así que **hay una sola copia del diseño**: si cambias `estilo/mmcantillo.sty`, cambian todos los documentos.

## Crear un documento nuevo

1. Copia la plantilla **dentro de su misma carpeta** con otro nombre, p. ej. `quiz/quiz-derivadas.tex`.
2. Edita el bloque de datos al inicio:
   ```latex
   \tipodocumento{Quiz}          % Quiz, Evaluación, Taller, Guía, Notas de clase...
   \asignatura{Cálculo}          % Cálculo, Física, Trigonometría...
                                 % (con Física, la cabecera dice «Área de Ciencias Naturales»)
   % \area{Área de ...}          % opcional, después de \asignatura: cambia el área de la cabecera
   \titulo{Derivadas: reglas básicas}
   \grado{11°}
   \periodo{III}
   \tiempo{20 min}               % opcional
   % \anio{2026}                 % por defecto, el año actual
   ```
3. Compila desde la carpeta de la plantilla:
   ```
   latexmk -pdf quiz-derivadas.tex
   ```
   (o `pdflatex` dos veces: en la segunda pasada aparecen el total de puntos y de páginas).

> Si guardas un archivo en otra ubicación (una carpeta más adentro, por ejemplo), ajusta la ruta en la línea
> `\def\input@path{{../estilo/}}` — p. ej. `{{../../estilo/}}`.

## Comandos principales

| Comando | Qué hace |
|---|---|
| `\encabezado` | Título + recuadro de Nombre, Fecha, Curso, Tiempo y Nota |
| `\encabezado*` | Solo el título (material de lectura) |
| `\begin{instrucciones}…\end{instrucciones}` | Recuadro de instrucciones |
| `\seccion{Selección múltiple}` | Separador de sección |
| `\begin{preguntas} \pregunta[2] … \end{preguntas}` | Preguntas numeradas; `[2]` son los puntos (opcional). La numeración continúa entre secciones y los puntos se suman solos en “Nota: ___ / total” |
| `\begin{opciones} \item …` | Opciones a), b), c)… una debajo de otra |
| `\begin{opciones*}(4) \item …` | Opciones en columnas (2 por defecto) |
| `\espacio{3cm}` · `\renglones{3}` | Espacio en blanco · renglones para escribir |
| `\begin{solucion}[4cm] … \end{solucion}` | Respuesta de la clave; oculta en la versión del estudiante, donde deja 4 cm en blanco |
| `definicion`, `teorema`, `ejemplo`, `nota` | Cajas para talleres y notas: `\begin{teorema}[Nombre] … \end{teorema}` |

### Matemáticas

- Conjuntos: `\R \N \Z \Q \C`
- `\abs{x}`, `\norm{v}`, `\dd x` (diferencial), `\dv{y}{x}`, `\pdv{f}{x}`, `\eval{F(x)}{a}{b}`, `\vect{F}`, `\cancel{x}`
- Funciones en español: `\sen x`, `\tg x`, `\lim` → “lím”
- Coma decimal: `$3,5$`
- Unidades (Física): `\qty{9,8}{m/s^2}`, `\unit{km/h}`

### Gráficas

Basta con el estilo `mmc` en el eje:

```latex
\begin{tikzpicture}
\begin{axis}[mmc, xmin=-3, xmax=3, ymin=-2, ymax=4]
  \addplot+[domain=-2:2] {x^2};        % trazo continuo
  \addplot+[domain=-2:2] {2*x};        % trazo discontinuo (2.ª curva)
\end{axis}
\end{tikzpicture}
```

Usa `\addplot+` (con `+`) para heredar los trazos del estilo. En B/N las curvas se distinguen por el tipo de línea: continua, discontinua, gris y punteada. Para gráficas por tramos (rectas), agrega `sharp plot`.

## Clave de respuestas

Sin editar el archivo:

```
pdflatex -jobname=quiz-derivadas-clave "\def\clave{}\input{quiz-derivadas}"
```

(ejecútalo dos veces). También puedes descomentar `\mostrarsoluciones` en el bloque de datos.

## Guía del estudiante (trimestral)

Una guía por periodo que soporta todos los temas de las clases. El ejemplo (`guia-trimestral/guia-trimestral.tex`, Cálculo 11°) muestra la estructura completa:

| Parte | Comando |
|---|---|
| Subtítulo con el hilo conductor | `\hiloconductor{La carrera por el cálculo}` |
| Frase introductoria | `\frase{texto}{Autor, \emph{Obra} (año)}` |
| DBA oficial | `\begin{dba}[Grado 11 · DBA 5] … \end{dba}` |
| Cita en el marco teórico | `\begin{cita}{Autor, fuente~\cite{clave}} … \end{cita}` |
| Tema numerado | `\tema{La pendiente}\label{tema:pendiente}` |
| Paso de la historia | `\begin{hilo} … \end{hilo}` |
| Aplicación real | `\begin{aplicacion}[Robótica] … \end{aplicacion}` |
| Resumen del tema (recuadro) | `\begin{resumen} … \end{resumen}` |
| Secciones institucionales | `\matrizevaluacion{saber}{hacer}{ser}{convivir}`, `\autoevaluacion`, `\seguimientodocente` |
| Bibliografía | `\begin{referencias} \bibitem{clave} … \end{referencias}` |

**Citar la guía desde una clase:** en el preámbulo de `clase.tex` escribe
`\guiadelestudiante{../../guia-didactica/guia-periodo-I-derivadas}` (ruta sin `.tex`) y en el texto
`\refguia{tema:pendiente}` → «Guía del estudiante, Tema 1 (p. 3)». Compila primero la guía y no borres su `.aux`.

## Requisitos

TeX Live / MacTeX completo (o Overleaf). En Overleaf sube la carpeta `plantillas/` completa manteniendo la estructura, para que la ruta `../estilo/` funcione.
