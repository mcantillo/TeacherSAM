#!/usr/bin/env python3
"""Convierte un .docx en texto plano, sin dependencias (funciona fuera de macOS).

Uso:  python3 tools/docx_a_texto.py archivo.docx [salida.txt]

Por defecto escribe en texto/<nombre>.txt, junto al .docx (la convención de recursos/).
- Un párrafo por línea; tabulaciones y saltos de línea respetados.
- Tablas: una celda por línea, como textutil.
- Ecuaciones: las del editor moderno de Word (OMML) salen como texto. Las de Microsoft
  Equation 3.0 (objetos incrustados, como las 710 del módulo de 11° de las Guías de Apoyo)
  no se pueden leer como texto: se marcan «[ecuación]» para que se sepa que ahí había una
  fórmula (textutil las borra sin avisar). Para leerlas hay que abrir el .docx.
- Imágenes: no se extraen; en las Guías de Apoyo accesibles, su «Descripción Imagen» ya es
  texto y sí aparece.
Solo usa la biblioteca estándar.
"""
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
M = "{http://schemas.openxmlformats.org/officeDocument/2006/math}"


def texto_parrafo(p):
    """Texto de un párrafo, incluidas las ecuaciones que contenga."""
    partes = []
    for nodo in p.iter():
        if nodo.tag in (W + "t", M + "t"):
            partes.append(nodo.text or "")
        elif nodo.tag == W + "tab":
            partes.append("\t")
        elif nodo.tag in (W + "br", W + "cr"):
            partes.append("\n")
        elif nodo.tag == W + "object":  # Equation 3.0 u otro objeto incrustado
            partes.append(" [ecuación] ")
    return "".join(partes)


def recorrer(elemento, lineas):
    """Párrafos y tablas en orden de lectura (también dentro de controles de contenido)."""
    for hijo in elemento:
        if hijo.tag == W + "p":
            vineta = "•\t" if hijo.find(f"{W}pPr/{W}numPr") is not None else ""
            lineas.append(vineta + texto_parrafo(hijo))
        elif hijo.tag == W + "tbl":
            for fila in hijo.findall(W + "tr"):
                for celda in fila.findall(W + "tc"):
                    recorrer(celda, lineas)
        elif hijo.tag != W + "sectPr":
            recorrer(hijo, lineas)


def main():
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    docx = Path(sys.argv[1])
    salida = (Path(sys.argv[2]) if len(sys.argv) == 3
              else docx.parent / "texto" / (docx.stem + ".txt"))
    with zipfile.ZipFile(docx) as z:
        raiz = ET.fromstring(z.read("word/document.xml"))
    lineas = []
    recorrer(raiz.find(W + "body"), lineas)
    salida.parent.mkdir(parents=True, exist_ok=True)
    texto = "\n".join(lineas) + "\n"
    salida.write_text(texto, encoding="utf-8")
    print(f"{salida}: {len(texto.split())} palabras")


if __name__ == "__main__":
    main()
