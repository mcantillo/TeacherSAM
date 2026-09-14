# Plantilla LaTeX — Guía Didáctica de Aprendizaje (Colegio San Alberto Magno)

Convierte el formato de `guia-didactica.docx` en una plantilla LaTeX reutilizable, conservando:

- El logo del colegio y el encabezado de página (nombre del colegio, dirección, resolución oficial, código "FPLAN v3") en **todas las páginas**.
- Los bloques con fondo azul de cada sección: Identificación y Propósito, Ruta de Aprendizaje (4 Momentos), Matriz de Evaluación, Autoevaluación, Seguimiento y Apoyos, Diario de Campo.
- Las casillas de Proyecto Transversal (EDPC, PEEF, EVS, PRAE, COLOM, NOCEST, OTRO).

## Archivos

- `guia-didactica.sty` — el estilo (colores, encabezado con logo, comandos de sección). **No lo edites** salvo que quieras cambiar el diseño para todas las guías futuras.
- `guia-template.tex` — la plantilla de una guía. Este es el archivo que copias y llenas cada vez.
- `logo-colegio.png` — el escudo del colegio, usado por el encabezado.
- `guia-template.pdf` — un ejemplo ya compilado, para que veas el resultado.

## Cómo generar una guía nueva

1. Copia `guia-template.tex` con un nombre nuevo, por ejemplo `guia-07-fracciones.tex`, y déjalo en la misma carpeta que `guia-didactica.sty` y `logo-colegio.png`.
2. Al inicio del archivo, en la sección **DATOS DE LA GUÍA**, edita:
   - `\NumeroGuia`, `\Area`, `\Asignatura`, `\Grado`, `\Periodo`, `\Docente`, `\FechaInicio`, `\FechaEntrega`.
   - Las casillas de proyectos transversales (`\MarcaEDPC`, `\MarcaPRAE`, etc.): pon una `x` para marcarlas.
3. Completa el contenido de cada campo (Eje Temático, DBA, Pregunta Problematizadora, los 4 Momentos, la Matriz de Evaluación, etc.) reemplazando las llaves vacías `{}` que siguen a cada `\gdCampo{Etiqueta:}{...}`.
4. Compila con:
   ```
   pdflatex guia-07-fracciones.tex
   ```
   (ejecútalo dos veces si cambias números de página o referencias).

## Requisitos

Necesitas una distribución LaTeX (TeX Live o MiKTeX) con estos paquetes, todos estándar:
`geometry`, `graphicx`, `xcolor`, `array`, `tabularx`, `longtable`, `multirow`, `colortbl`, `fancyhdr`, `enumitem`, `amssymb`, `ragged2e`, `tikz`, `pgffor`, `tcolorbox`.

Si usas Overleaf, todo esto ya viene instalado — solo sube los 3 archivos (`.sty`, `.tex`, `.png`) al mismo proyecto.

**Sobre el español:** la plantilla detecta sola si está instalado el soporte de español de `babel`. Si no lo está, compila igual (mismo diseño, mismas páginas) y solo muestra un aviso; lo único que se pierde es la separación silábica en español. Para instalarlo:

- Linux/Debian/Ubuntu: `sudo apt install texlive-lang-spanish`
- TeX Live / MacTeX: `sudo tlmgr install babel-spanish`
- Overleaf: ya viene incluido

## Ajustar el encabezado

- **Alto del encabezado:** `\gdAltoEncabezado` (por defecto `2.5cm`) en `guia-didactica.sty`. Las tres celdas (logo, datos del colegio, código) son `\parbox` de esa altura con alineación `[c]` por fuera y por dentro, así que el logo queda **centrado vertical y horizontalmente** de forma exacta. Si cambias este valor, ajusta también `headheight` y `top` en el bloque `\geometry` (regla: `top = margen superior + headheight + headsep`, y `headheight` debe ser mayor que el alto real de la tabla).
- **Tamaño del logo:** el `height=2.1cm` del `\includegraphics` en el `\fancyhead`.
- **Ancho de las columnas de etiquetas** del bloque de datos (Área:, Asignatura:, ...): `\gdAnchoEtiqueta` (por defecto `3.3cm`); los anchos de las columnas de valores se recalculan solos.

## Notas técnicas (por si algo falla)

- El encabezado usa tablas con anchos de columna fijos (no la columna `X` de `tabularx`) porque `babel[spanish]` convierte `<` y `>` en atajos activos para comillas (« »), lo cual choca con la sintaxis `>{...}` de columnas de `tabularx`/`array`. El estilo ya desactiva ese atajo (`\shorthandoff{<>}`), así que puedes usar `tabularx` con columnas `X` en tus propias tablas sin `>{...}` o `<{...}` en el preámbulo de columnas.
- Para cambiar el logo de una guía específica, redefine `\GuiaLogo{otro-archivo.png}` después de `\usepackage{guia-didactica}`.
