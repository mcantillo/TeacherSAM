# Ejemplos y lecciones aprendidas

## Guías de referencia

| Archivo | Qué muestra |
|---|---|
| `materias/calculo/undecimo/guia-didactica/guia-periodo-I-numeros-reales.tex` | **Guía real del piloto** (11°, trimestre I, 7 temas, 17 pp.): hilo histórico (la historia del infinito), citas verificadas, ejemplos oficiales de los DBA adaptados, recursos citados, sección Saber 11 |
| `plantillas/guia-trimestral/guia-trimestral.tex` | Plantilla de secundaria (11°, derivadas): la estructura mínima con 3 temas |
| `plantillas/guia-trimestral/guia-geometria-3.tex` | Registro **infantil** (3°): cuento de dominio público (Rinrín Renacuajo), marco teórico con anécdotas («¿Sabías que…?») sin citas textuales, ejercicios manipulativos, dibujos en TikZ |

Antes de escribir, lee la guía de referencia más cercana al grado.

## Cómo el piloto usó sus fuentes

- **DBA:** el ejemplo oficial del DBA 1 (Carolina: «¿por qué no sigue 5,1 después de 5?») se volvió un ejercicio de densidad. El del DBA 2 (Ana divide por un negativo sin invertir el signo) se volvió un ejercicio de «encuentra el error».
- **Recursos:** del módulo de 11° (Quintero Palomino) salieron la diferencia de intervalos, las inecuaciones simultáneas con el caso que no se despeja en el centro, el descubrimiento con tablas, los contextos (ley de Ohm, °F→°C, medicamento), la traducción a valor absoluto y las preguntas tipo Saber. Todo reescrito, verificado y citado.
- **Errores encontrados en ese recurso** (verificar siempre): signos perdidos (−5x → 5x), «3x + 9» en lugar de «3x + 6», unidades mezcladas (metros de alambre y pies cuadrados), y el coeficiente de t² presentado como la aceleración de la gravedad, cuando es la mitad. Los problemas en pies y millas se pasan a metros.
- **Ejemplos oficiales defectuosos:** el ejemplo del atleta del DBA 5 de 11° no tiene sentido (con una distancia cuadrática la velocidad máxima está en el instante inicial): no usarlo.

## Defectos de maquetación ya vistos (y su arreglo)

| Defecto | Arreglo |
|---|---|
| Sub-ítems a) b) c) en una línea que se parte o pasa a la página siguiente | `\begin{opciones*}(3) \item … \end{opciones*}` (el número es de columnas) |
| Recuadro `resumen` partido entre dos páginas | Ya no es `breakable` en el estilo; si queda un hueco grande antes del recuadro, es aceptable |
| Título «Evaluación del periodo» solo al pie de la página | `\matrizevaluacion` imprime su propio título con `\Needspace`: no escribas `\seccion{Evaluación…}` aparte |
| Una figura separada de su leyenda (mapa + convenciones) | Envolver ambas en `\begin{minipage}{\linewidth}\centering … \end{minipage}` |
| Enunciado separado de su tabla | `\Needspace{11\baselineskip}` antes del `\pregunta` |
| Etiquetas de TikZ desalineadas (por ejemplo, «cono» más alto que «cilindro») | `every node/.append style={text height=1.6ex, text depth=0.3ex}` |
| La leyenda de pgfplots tapa la etiqueta de un eje | `legend pos=outer north east` |
| Se pierde el símbolo de grado en `\unit{°C/min}` | `\unit{\degreeCelsius\per\minute}` |
| «lím», «máx», «mín» salen sin tilde («lım») | Ya corregido en el estilo (redefine `\es@op@ac` de babel-spanish). Si otra letra desaparece, `revisar_guia.py --compilar` lo marca; para ver la línea: `pdflatex "\tracinglostchars=3\input{archivo}"` |
| Comillas « » con espacios dentro de `cita` | Ya corregido en el estilo; escribe el texto sin espacios de más |
| Intervalos con coma decimal (`icomma`) | Deja un espacio después de la coma separadora: `$[-2, 3)$`; los decimales van con `{,}` o sin espacio: `$0{,}5$` |

## Informe de entrega (modelo)

1. Ruta del PDF, número de páginas y confirmación de que compila sin errores.
2. Temas con su etiqueta `tema:…` (para citarlos desde las clases).
3. Citas y fuentes usadas; qué va parafraseado y por qué.
4. Recursos usados y errores encontrados en ellos.
5. Respuestas de la sección Saber 11 (no van en la guía).
6. Preguntas pendientes para la docente (por ejemplo, cambios de subtema en el CSV).
