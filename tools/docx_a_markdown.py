#!/usr/bin/env python3
"""Convierte un .docx en Markdown con las fórmulas en LaTeX, sin dependencias.

Uso:  python3 tools/docx_a_markdown.py archivo.docx [otro.docx ...] [--diagnostico]

Escribe markdown/<nombre>.md junto al .docx (al lado de texto/, la copia en texto plano).
- Fórmulas de Microsoft Equation 3.0 (objetos OLE, como las de los módulos de matemáticas de
  las Guías de Apoyo): se lee el MTEF v3 del stream «Equation Native» y se pasa a LaTeX.
  Cada objeto trae además un texto alternativo hablado («x sobre 4 menor o igual que 70»);
  si los números de ese texto no coinciden con los de la fórmula, se deja al lado como
  <!-- alt: … --> para revisarla a mano (el texto alternativo también tiene errores).
- Fórmulas del editor moderno de Word (OMML, las de las guías de física): a LaTeX.
- Una fórmula sola en su párrafo va en un bloque ```latex; dentro de un texto, entre $…$.
- Títulos → #, listas → -, tablas → tablas Markdown, pies de figura en cursiva.
Con --diagnostico lista los caracteres y plantillas que no se supieron traducir.
Solo usa la biblioteca estándar.
"""
import re
import struct
import sys
import zipfile
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
M = "{http://schemas.openxmlformats.org/officeDocument/2006/math}"
V = "{urn:schemas-microsoft-com:vml}"
O = "{urn:schemas-microsoft-com:office:office}"
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
MC = "{http://schemas.openxmlformats.org/markup-compatibility/2006}"
PR = "{http://schemas.openxmlformats.org/package/2006/relationships}"

desconocidos = Counter()

# ---------------------------------------------------------------- caracteres → LaTeX

UNICODE = {
    "≤": r"\le ", "≥": r"\ge ", "≠": r"\neq ", "±": r"\pm ", "∓": r"\mp ", "×": r"\times ",
    "÷": r"\div ", "·": r"\cdot ", "⋅": r"\cdot ", "•": r"\cdot ", "∞": r"\infty ",
    "∈": r"\in ", "∉": r"\notin ", "∋": r"\ni ", "⊂": r"\subset ", "⊆": r"\subseteq ",
    "⊃": r"\supset ", "⊇": r"\supseteq ", "⊄": r"\not\subset ", "∪": r"\cup ",
    "∩": r"\cap ", "∅": r"\emptyset ", "∀": r"\forall ", "∃": r"\exists ", "¬": r"\neg ",
    "∧": r"\wedge ", "∨": r"\vee ", "→": r"\to ", "←": r"\leftarrow ",
    "↔": r"\leftrightarrow ", "⇒": r"\Rightarrow ", "⇐": r"\Leftarrow ",
    "⇔": r"\Leftrightarrow ", "↑": r"\uparrow ", "↓": r"\downarrow ", "≈": r"\approx ",
    "≅": r"\cong ", "≡": r"\equiv ", "∼": r"\sim ", "~": r"\sim ", "∝": r"\propto ",
    "∂": r"\partial ", "∇": r"\nabla ", "∠": r"\angle ", "⊥": r"\perp ", "∥": r"\parallel ",
    "∴": r"\therefore ", "…": r"\ldots ", "⋯": r"\cdots ", "°": r"^{\circ}", "′": "'",
    "″": "''", "−": "-", "–": "-", "⁄": "/", "√": r"\surd ", "∑": r"\sum ", "∏": r"\prod ",
    "∫": r"\int ", "〈": r"\langle ", "〉": r"\rangle ", "⟨": r"\langle ",
    "⟩": r"\rangle ", "ℝ": r"\mathbb{R}", "ℕ": r"\mathbb{N}", "ℤ": r"\mathbb{Z}",
    "ℚ": r"\mathbb{Q}", "ℂ": r"\mathbb{C}", "ℵ": r"\aleph ", "△": r"\triangle ",
    "∆": r"\Delta ", "Ω": r"\Omega ", "µ": r"\mu ", "ƒ": "f", "{": r"\{", "}": r"\}",
    "%": r"\%", "#": r"\#", "&": r"\&", "$": r"\$", "_": r"\_", "\\": r"\backslash ",
    " ": r"\ ", " ": r"\,", " ": r"\quad ", " ": r"\ ", "⊗": r"\otimes ",
    "⊕": r"\oplus ", "◊": r"\diamond ", "□": r"\square ", "∘": r"\circ ", "⌊": r"\lfloor ",
    "⌋": r"\rfloor ", "⌈": r"\lceil ", "⌉": r"\rceil ", "∕": "/", "∗": "*", "ϕ": r"\phi ",
    "∙": r"\cdot ",
    "": "|", "": "|",   # MTExtra (uso privado): barras del valor absoluto
    "": r"\|",                # MTExtra: paralela
    "´": "'", "’": "'",             # primas escritas con tilde o apóstrofo
    "︸": "", "︷": "",              # dibujo de la llave horizontal (la da \underbrace)
}
GRIEGAS = ("alpha beta gamma delta epsilon zeta eta theta iota kappa lambda mu nu xi "
           "omicron pi rho varsigma sigma tau upsilon varphi chi psi omega").split()
for i, nombre in enumerate(GRIEGAS):
    UNICODE[chr(0x3B1 + i)] = "\\" + ("o" if nombre == "omicron" else nombre) + " "
    mayus = nombre.capitalize()
    if nombre in ("gamma", "delta", "theta", "lambda", "xi", "pi", "sigma", "upsilon",
                  "psi", "omega"):
        UNICODE[chr(0x391 + i)] = "\\" + mayus + " "
    elif nombre == "varphi":
        UNICODE[chr(0x391 + i)] = r"\Phi "
    elif nombre != "varsigma":
        UNICODE[chr(0x391 + i)] = {"alpha": "A", "beta": "B", "epsilon": "E", "zeta": "Z",
                                    "eta": "H", "iota": "I", "kappa": "K", "mu": "M",
                                    "nu": "N", "omicron": "O", "rho": "P", "tau": "T",
                                    "chi": "X"}[nombre]
UNICODE["ϑ"] = r"\vartheta "
UNICODE["ϖ"] = r"\varpi "

# Codificación de la fuente Symbol (la usa Equation 3.0 para símbolos y griegas).
SYMBOL = dict(zip("ABCDEFGHIKLMNOPQRSTUWXYZabcdefghiklmnopqrstuvwxyz",
                  "ΑΒΧΔΕΦΓΗΙΚΛΜΝΟΠΘΡΣΤΥΩΞΨΖαβχδεφγηικλμνοπθρστυϖωξψζ"))
SYMBOL.update({"J": "ϑ", "V": "ς", "j": "ϕ"})
SYMBOL_ALTO = {
    0x22: "∀", 0x24: "∃", 0x27: "∋", 0x2A: "∗", 0x2D: "−", 0x40: "≅", 0x5C: "∴", 0x5E: "⊥",
    0x7E: "∼", 0xA2: "′", 0xA3: "≤", 0xA4: "⁄", 0xA5: "∞", 0xAB: "↔", 0xAC: "←", 0xAD: "↑",
    0xAE: "→", 0xAF: "↓", 0xB0: "°", 0xB1: "±", 0xB2: "″", 0xB3: "≥", 0xB4: "×", 0xB5: "∝",
    0xB6: "∂", 0xB7: "•", 0xB8: "÷", 0xB9: "≠", 0xBA: "≡", 0xBB: "≈", 0xBC: "…", 0xC0: "ℵ",
    0xC4: "⊗", 0xC5: "⊕", 0xC6: "∅", 0xC7: "∩", 0xC8: "∪", 0xC9: "⊃", 0xCA: "⊇",
    0xCB: "⊄", 0xCC: "⊂", 0xCD: "⊆", 0xCE: "∈", 0xCF: "∉", 0xD0: "∠", 0xD1: "∇",
    0xD5: "∏", 0xD6: "√", 0xD7: "⋅", 0xD8: "¬", 0xD9: "∧", 0xDA: "∨", 0xDB: "⇔",
    0xDC: "⇐", 0xDE: "⇒", 0xE0: "◊", 0xE1: "〈", 0xE5: "∑", 0xF1: "〉", 0xF2: "∫",
}
FUNCIONES = {"sen", "sin", "cos", "tan", "tg", "cot", "ctg", "sec", "csc", "cosec", "log",
             "ln", "exp", "lim", "max", "min", "arcsen", "arcsin", "arccos", "arctan"}


def latex_caracter(c, fuente_symbol=False):
    """LaTeX de un carácter suelto (letra, dígito, operador o símbolo)."""
    if fuente_symbol and c in SYMBOL:
        c = SYMBOL[c]
    elif fuente_symbol and ord(c) in SYMBOL_ALTO:
        c = SYMBOL_ALTO[ord(c)]
    if c in UNICODE:
        return UNICODE[c]
    if c.isascii() or c.isalpha() or c.isdigit():
        return c
    desconocidos[f"U+{ord(c):04X} {c}"] += 1
    return c


def grupo(s):
    """{s} salvo que s sea un solo símbolo."""
    s = s.strip()
    if len(s) == 1 or re.fullmatch(r"\\[A-Za-z]+", s):
        return s
    return "{" + s + "}"


def funcion(nombre):
    nombre = nombre.strip()
    if nombre in ("sen", "tg", "ctg", "cosec", "arcsen"):
        return r"\operatorname{" + nombre + "}"
    if nombre in FUNCIONES:
        return "\\" + nombre
    return r"\operatorname{" + nombre + "}" if nombre else ""


def juntar(partes):
    """Concatena LaTeX sin pegar un comando a la letra siguiente (\\sum x, no \\sumx)."""
    s = ""
    for p in partes:
        if p and p[0].isalpha() and re.search(r"\\[A-Za-z]+$", s):
            s += " "
        s += p
    return s


def limpiar(s):
    s = re.sub(r" +", " ", s).strip()
    s = re.sub(r"(\\[A-Za-z]+) (?=[^A-Za-z])", r"\1", s)
    return s

# ---------------------------------------------------------------- OLE (Compound File)


def streams_ole(datos):
    """{nombre: bytes} de los streams de un archivo OLE2 (Compound File Binary)."""
    if datos[:8] != bytes.fromhex("d0cf11e0a1b11ae1"):
        return {}
    sec = 1 << struct.unpack_from("<H", datos, 0x1E)[0]
    mini = 1 << struct.unpack_from("<H", datos, 0x20)[0]
    n_fat, dir0 = struct.unpack_from("<II", datos, 0x2C)
    corte, minifat0, n_minifat, difat0, n_difat = struct.unpack_from("<IIIII", datos, 0x38)

    def sector(i):
        return datos[(i + 1) * sec:(i + 2) * sec]

    difat = list(struct.unpack_from("<109I", datos, 0x4C))
    i = difat0
    for _ in range(n_difat):
        bloque = struct.unpack(f"<{sec // 4}I", sector(i))
        difat += bloque[:-1]
        i = bloque[-1]
    fat = []
    for i in difat[:n_fat]:
        fat += struct.unpack(f"<{sec // 4}I", sector(i))

    def cadena(inicio, tabla):
        vistos = set()
        while inicio < 0xFFFFFFFA and inicio not in vistos and inicio < len(tabla):
            vistos.add(inicio)
            yield inicio
            inicio = tabla[inicio]

    def leer(inicio):
        return b"".join(sector(i) for i in cadena(inicio, fat))

    directorio = leer(dir0)
    minifat_b = leer(minifat0) if n_minifat else b""
    minifat = list(struct.unpack(f"<{len(minifat_b) // 4}I", minifat_b))
    entradas = []
    for k in range(0, len(directorio), 128):
        e = directorio[k:k + 128]
        largo = struct.unpack_from("<H", e, 64)[0]
        nombre = e[:max(largo - 2, 0)].decode("utf-16-le", "replace")
        tipo = e[66]
        inicio, tam = struct.unpack_from("<II", e, 116)
        entradas.append((nombre, tipo, inicio, tam))
    raiz = entradas[0]
    ministream = leer(raiz[2])
    salida = {}
    for nombre, tipo, inicio, tam in entradas[1:]:
        if tipo != 2:
            continue
        if tam < corte:
            b = b"".join(ministream[i * mini:(i + 1) * mini] for i in cadena(inicio, minifat))
        else:
            b = leer(inicio)
        salida[nombre] = b[:tam]
    return salida

# ---------------------------------------------------------------- MTEF v3 → LaTeX


class MTEF:
    """Lector de MTEF v3 (Equation 3.0). Devuelve LaTeX."""

    def __init__(self, datos):
        self.b = datos
        self.i = 0

    def byte(self):
        v = self.b[self.i]
        self.i += 1
        return v

    def palabra(self):
        v = struct.unpack_from("<H", self.b, self.i)[0]
        self.i += 2
        return v

    def empuje(self):
        dx, dy = self.byte(), self.byte()
        if dx == 128 and dy == 128:
            self.i += 4

    def regla(self):
        n = self.byte()
        self.i += 3 * n

    def latex(self):
        if self.b[0] != 3:
            raise ValueError(f"MTEF versión {self.b[0]}, se esperaba 3")
        self.i = 5
        return limpiar(self.lista())

    def lista(self, hasta_fin=True):
        """Objetos hasta END; devuelve el LaTeX concatenado."""
        return self.unir(self.objetos())

    def objetos(self):
        """Lista de ('linea'|'car'|'otro', latex, info) hasta el END (o fin de datos)."""
        salida = []
        while self.i < len(self.b):
            tag = self.byte()
            tipo, op = tag & 0x0F, tag >> 4
            if tipo == 0:
                break
            if tipo == 1:        # LINE
                if op & 8:
                    self.empuje()
                if op & 4:
                    self.i += 2
                if op & 2:
                    self.byte()
                    self.regla()
                salida.append(("linea", "" if op & 1 else self.lista(), None))
            elif tipo == 2:      # CHAR
                if op & 8:
                    self.empuje()
                fuente = self.byte() - 128
                c = chr(self.palabra())
                adornos = self.adornos() if op & 2 else []
                salida.append(("car", c, (fuente, adornos)))
            elif tipo == 3:      # TMPL
                if op & 8:
                    self.empuje()
                sel, var = self.byte(), self.byte()
                self.byte()
                hijos = self.objetos()
                salida.append(("otro", self.plantilla(sel, var, hijos), None))
            elif tipo == 4:      # PILE
                if op & 8:
                    self.empuje()
                self.byte(); self.byte()
                if op & 2:
                    self.byte()
                    self.regla()
                lineas = [t for k, t, _ in self.objetos() if k == "linea"]
                salida.append(("otro", r"\begin{array}{l}" + r" \\ ".join(lineas)
                               + r"\end{array}", None))
            elif tipo == 5:      # MATRIX
                if op & 8:
                    self.empuje()
                self.byte(); self.byte(); self.byte()
                filas, cols = self.byte(), self.byte()
                self.i += ((filas + 1) * 2 + 7) // 8 + ((cols + 1) * 2 + 7) // 8
                celdas = [t for k, t, _ in self.objetos() if k == "linea"]
                filas_tex = [" & ".join(celdas[f * cols:(f + 1) * cols]) for f in range(filas)]
                salida.append(("otro", r"\begin{array}{" + "c" * cols + "}"
                               + r" \\ ".join(filas_tex) + r"\end{array}", None))
            elif tipo == 6:      # EMBELL (suelto: no debería ocurrir)
                if op & 8:
                    self.empuje()
                self.byte()
            elif tipo == 7:      # RULER
                self.regla()
            elif tipo == 8:      # FONT
                self.byte(); self.byte()
                while self.byte() != 0:
                    pass
            elif tipo == 9:      # SIZE
                l = self.byte()
                if l == 101:
                    self.i += 2
                elif l == 100:
                    self.i += 3
                else:
                    self.i += 1
            elif 10 <= tipo <= 14:
                pass             # FULL, SUB, SUB2, SYM, SUBSYM
            else:
                raise ValueError(f"registro MTEF desconocido {tipo}")
        return salida

    def adornos(self):
        salida = []
        while True:
            tag = self.byte()
            if tag & 0x0F == 0:
                return salida
            if tag >> 4 & 8:
                self.empuje()
            salida.append(self.byte())

    def unir(self, objetos):
        """Concatena objetos; junta letras de función y texto en un solo bloque."""
        partes, func, texto = [], "", ""

        def vaciar():
            nonlocal func, texto
            if func:
                partes.append(funcion(func) + " ")
                func = ""
            if texto:
                partes.append(r"\text{" + texto + "}")
                texto = ""

        for tipo, valor, info in objetos:
            if tipo != "car":
                vaciar()
                partes.append(valor)
                continue
            fuente, adornos = info
            if fuente == 2 and valor.isalpha() and not adornos:
                if texto:
                    vaciar()
                func += valor
                continue
            if fuente in (1, 12) and not adornos and valor not in "{}\\$%#&_^":
                if func:
                    p, texto = texto, ""
                    vaciar()
                    texto = p
                texto += valor
                continue
            vaciar()
            partes.append(self.caracter(valor, fuente, adornos))
        vaciar()
        return juntar(partes)

    def caracter(self, c, fuente, adornos):
        t = latex_caracter(c, fuente_symbol=fuente in (4, 5, 6) and ord(c) < 0x100)
        if fuente == 7:
            t = r"\mathbf{" + t + "}"
        for a in adornos:
            t = {2: r"\dot{%s}", 3: r"\ddot{%s}", 4: r"\dddot{%s}", 5: "%s'", 6: "%s''",
                 7: "`%s", 8: r"\tilde{%s}", 9: r"\hat{%s}", 10: r"\not %s",
                 11: r"\vec{%s}", 12: r"\overleftarrow{%s}", 13: r"\overleftrightarrow{%s}",
                 14: r"\vec{%s}", 15: r"\overleftarrow{%s}", 16: r"\bar{%s}",
                 17: r"\overline{%s}", 18: "%s'''", 19: r"\overset{\frown}{%s}",
                 20: r"\overset{\smile}{%s}"}.get(a, "%s") % t
        return t

    def plantilla(self, sel, var, hijos):
        # Casillas: líneas (o pilas/matrices sueltas); los CHAR son los delimitadores u
        # operadores que la plantilla dibuja (en v3 los cercos traen sus caracteres).
        lineas = [t for k, t, _ in hijos if k != "car"]
        cars = [self.caracter(t, i[0], i[1]).strip() for k, t, i in hijos if k == "car"]
        ln = lambda n: lineas[n] if n < len(lineas) else ""
        cerca = {0: (r"\langle", r"\rangle"), 1: ("(", ")"), 2: (r"\{", r"\}"),
                 3: ("[", "]"), 4: ("|", "|"), 5: (r"\|", r"\|"), 6: (r"\lfloor", r"\rfloor"),
                 7: (r"\lceil", r"\rceil"), 8: ("[", "["), 9: ("]", "]"), 10: ("]", "["),
                 11: ("[", ")"), 12: ("(", "]")}
        if sel in cerca:
            izq, der = cerca[sel]
            if len(cars) >= 2:
                izq, der = cars[0], cars[1]
            elif len(cars) == 1:
                izq, der = (".", cars[0]) if var & 2 and not var & 1 else (cars[0], ".")
            cuerpo = ln(0)
            if izq == "." or der == "." or re.search(r"\\frac|\\begin|\\sum|\\int", cuerpo):
                return rf"\left{izq} {cuerpo} \right{der}"
            return f"{izq}{cuerpo}{der}"
        if sel == 13:
            return rf"\sqrt[{ln(1)}]{{{ln(0)}}}" if var & 1 and ln(1) else rf"\sqrt{{{ln(0)}}}"
        if sel == 14:
            return rf"\frac{{{ln(0)}}}{{{ln(1)}}}"
        if sel in (16, 17):
            return (r"\underline{%s}" if sel == 16 else r"\overline{%s}") % ln(0)
        if sel == 18:
            return rf"\xrightarrow[{ln(1)}]{{{ln(0)}}}"
        if 19 <= sel <= 26 or sel == 43:   # [término, inferior, superior, operador]
            op = cars[0] if cars else (ln(3).strip() or {
                19: r"\int", 25: r"\int", 20: r"\sum", 26: r"\sum", 43: r"\sum",
                21: r"\prod", 22: r"\coprod", 23: r"\bigcup", 24: r"\bigcap"}[sel])
            lim = (f"_{{{ln(1)}}}" if ln(1) else "") + (f"^{{{ln(2)}}}" if ln(2) else "")
            return f"{op}{lim} {ln(0)}"
        if sel == 27:
            nombre = ln(0) if ln(0) else r"\lim"
            return f"{nombre}_{{{ln(1)}}}" + (f"^{{{ln(2)}}}" if ln(2) else "") + " "
        if sel in (28, 29):
            comando = r"\overbrace" if var & 1 else r"\underbrace"
            marca = "^" if var & 1 else "_"
            return f"{comando}{{{ln(0)}}}{marca}{{{ln(1)}}}" if ln(1) else f"{comando}{{{ln(0)}}}"
        if sel == 30:
            return rf"{ln(1)}\,\overline{{){ln(0)}}}"
        if sel in (15, 31, 32, 33):  # 15: sub/superíndice de v3 (casillas [sub, sup])
            sub, sup = ln(0), ln(1)
            return (f"_{{{sub}}}" if sub else "") + (f"^{{{sup}}}" if sup else "")
        if sel == 34:
            return rf"\langle {ln(0)} | {ln(1)} \rangle"
        if 35 <= sel <= 38:
            return {35: r"\vec{%s}", 36: r"\widetilde{%s}", 37: r"\widehat{%s}",
                    38: r"\overset{\frown}{%s}"}[sel] % ln(0)
        if sel == 47:                # flecha sobre letras: segmento, rayo, recta
            return {0: r"\overline{%s}", 1: r"\overrightarrow{%s}",
                    2: r"\overleftrightarrow{%s}"}.get(var, r"\overleftarrow{%s}") % ln(0)
        if sel == 40:
            return r"\cancel{%s}" % ln(0)
        if sel == 41:
            return r"\boxed{%s}" % ln(0)
        desconocidos[f"plantilla {sel}/{var}"] += 1
        return " ".join(lineas)


def ecuacion_ole(datos):
    """LaTeX de un objeto Equation 3.0, o None si no se puede leer."""
    streams = streams_ole(datos)
    # Algunos objetos guardan el stream sin nombre: se reconoce por la cabecera de 28 bytes.
    nativo = streams.get("Equation Native") or next(
        (b for b in streams.values() if b[:6] == bytes([0x1C, 0, 0, 0, 2, 0])), None)
    if not nativo:
        return None
    cab = struct.unpack_from("<H", nativo, 0)[0]
    try:
        return MTEF(nativo[cab:]).latex()
    except (IndexError, ValueError, struct.error) as e:
        desconocidos[f"MTEF ilegible: {e}"] += 1
        return None

# ---------------------------------------------------------------- OMML → LaTeX


def omml(nodo):
    """LaTeX de un nodo OMML (oMath y sus hijos)."""
    partes = []
    for h in nodo:
        t = h.tag
        if t.endswith("Pr") or t == M + "ctrlPr":
            continue
        partes.append(omml_elemento(h))
    return "".join(partes)


def hijo(nodo, nombre):
    h = nodo.find(M + nombre)
    return omml(h) if h is not None else ""


def valor(nodo, ruta, defecto=None):
    h = nodo.find(ruta)
    return h.get(M + "val", defecto) if h is not None else defecto


def omml_elemento(h):
    t = h.tag
    if t == M + "r":
        texto = "".join(x.text or "" for x in h.iter(M + "t"))
        normal = valor(h, f"{M}rPr/{M}sty") == "p" or h.find(f"{M}rPr/{M}nor") is not None
        if normal and re.fullmatch(r"[A-Za-záéíóúñÁÉÍÓÚÑ]{2,}", texto.strip()):
            palabra = texto.strip()
            if palabra in FUNCIONES:
                return funcion(palabra) + " "
            return r"\mathrm{" + palabra + "}"
        if normal and re.search(r"[A-Za-zá-ú]{2,} ", texto):   # frase: «cambio de velocidad»
            return r"\text{" + texto + "}"
        return "".join(latex_caracter(c) for c in texto)
    if t == M + "f":
        if valor(h, f"{M}fPr/{M}type") == "lin":
            return f"{hijo(h, 'num')}/{hijo(h, 'den')}"
        return rf"\frac{{{hijo(h, 'num')}}}{{{hijo(h, 'den')}}}"
    if t == M + "sSup":
        return f"{grupo(hijo(h, 'e'))}^{{{hijo(h, 'sup')}}}"
    if t == M + "sSub":
        return f"{grupo(hijo(h, 'e'))}_{{{hijo(h, 'sub')}}}"
    if t == M + "sSubSup":
        return f"{grupo(hijo(h, 'e'))}_{{{hijo(h, 'sub')}}}^{{{hijo(h, 'sup')}}}"
    if t == M + "sPre":
        return f"{{}}_{{{hijo(h, 'sub')}}}^{{{hijo(h, 'sup')}}}{hijo(h, 'e')}"
    if t == M + "rad":
        if valor(h, f"{M}radPr/{M}degHide") in ("1", "on", "true") or not hijo(h, "deg"):
            return rf"\sqrt{{{hijo(h, 'e')}}}"
        return rf"\sqrt[{hijo(h, 'deg')}]{{{hijo(h, 'e')}}}"
    if t == M + "d":
        izq = valor(h, f"{M}dPr/{M}begChr", "(")
        der = valor(h, f"{M}dPr/{M}endChr", ")")
        sep = valor(h, f"{M}dPr/{M}sepChr", "|")
        cuerpo = f" {latex_caracter(sep).strip()} ".join(omml(e) for e in h.findall(M + "e"))
        d = lambda c: {"": ".", "{": r"\{", "}": r"\}", "⟨": r"\langle", "⟩": r"\rangle",
                       "〈": r"\langle", "〉": r"\rangle", "‖": r"\|", "⌊": r"\lfloor",
                       "⌋": r"\rfloor", "⌈": r"\lceil", "⌉": r"\rceil"}.get(c, c)
        return rf"\left{d(izq)} {cuerpo} \right{d(der)}"
    if t == M + "acc":
        c = valor(h, f"{M}accPr/{M}chr", "̂")
        comando = {"̅": r"\overline", "̄": r"\overline", "¯": r"\overline",
                   "⃗": r"\vec", "→": r"\vec", "̂": r"\hat", "̃": r"\tilde",
                   "̇": r"\dot", "̈": r"\ddot"}.get(c)
        if not comando:
            desconocidos[f"acento U+{ord(c[0]):04X}"] += 1
            comando = r"\overline"
        return f"{comando}{{{hijo(h, 'e')}}}"
    if t == M + "bar":
        arriba = valor(h, f"{M}barPr/{M}pos", "bot") == "top"
        return (r"\overline{%s}" if arriba else r"\underline{%s}") % hijo(h, "e")
    if t == M + "func":
        nombre = hijo(h, "fName").strip()
        nombre = nombre[len(r"\mathrm{"):-1] if nombre.startswith(r"\mathrm{") else nombre
        return f"{funcion(nombre) if nombre.isalpha() else nombre} {hijo(h, 'e')}"
    if t == M + "nary":
        c = valor(h, f"{M}naryPr/{M}chr", "∫")
        op = {"∑": r"\sum", "∏": r"\prod", "∫": r"\int", "∬": r"\iint", "∮": r"\oint",
              "⋃": r"\bigcup", "⋂": r"\bigcap"}.get(c, c)
        return f"{op}_{{{hijo(h, 'sub')}}}^{{{hijo(h, 'sup')}}} {hijo(h, 'e')}"
    if t in (M + "limLow", M + "limUpp"):
        marca = "_" if t == M + "limLow" else "^"
        return f"{hijo(h, 'e')}{marca}{{{hijo(h, 'lim')}}}"
    if t == M + "groupChr":
        arriba = valor(h, f"{M}groupChrPr/{M}pos", "bot") == "top"
        return (r"\overbrace{%s}" if arriba else r"\underbrace{%s}") % hijo(h, "e")
    if t == M + "eqArr":
        return r"\begin{array}{l}" + r" \\ ".join(omml(e) for e in h.findall(M + "e")) \
            + r"\end{array}"
    if t == M + "m":
        filas = [" & ".join(omml(e) for e in fila.findall(M + "e"))
                 for fila in h.findall(M + "mr")]
        cols = max((len(f.findall(M + "e")) for f in h.findall(M + "mr")), default=1)
        return r"\begin{array}{" + "c" * cols + "}" + r" \\ ".join(filas) + r"\end{array}"
    if t in (M + "box", M + "borderBox", M + "phant", M + "e", M + "oMath"):
        return omml(h)
    if t == M + "oMathPara":
        return omml(h)
    if t.startswith(W):          # w:r u otros dentro de la fórmula
        return "".join(x.text or "" for x in h.iter(W + "t"))
    desconocidos[f"OMML {t.split('}')[1]}"] += 1
    return omml(h)

# ---------------------------------------------------------------- documento → Markdown


class Documento:
    def __init__(self, ruta):
        self.z = zipfile.ZipFile(ruta)
        rels = ET.fromstring(self.z.read("word/_rels/document.xml.rels"))
        self.rels = {r.get("Id"): r.get("Target") for r in rels.iter(PR + "Relationship")}
        self.n_ole = self.n_ok = self.n_alt = self.n_omml = 0
        self.formatos = self.leer_numeracion()
        self.contadores = {}

    def leer_numeracion(self):
        """{numId: {nivel: (numFmt, lvlText, inicio)}} de word/numbering.xml."""
        try:
            raiz = ET.fromstring(self.z.read("word/numbering.xml"))
        except KeyError:
            return {}
        abstractos = {}
        for a in raiz.findall(W + "abstractNum"):
            niveles = {}
            for lvl in a.findall(W + "lvl"):
                val = lambda n, d: (lvl.find(W + n).get(W + "val")
                                    if lvl.find(W + n) is not None else d)
                niveles[int(lvl.get(W + "ilvl"))] = (val("numFmt", "decimal"),
                                                     val("lvlText", ""), int(val("start", "1")))
            abstractos[a.get(W + "abstractNumId")] = niveles
        nums = {}
        for n in raiz.findall(W + "num"):
            ref = n.find(W + "abstractNumId")
            nums[n.get(W + "numId")] = abstractos.get(ref.get(W + "val"), {}) \
                if ref is not None else {}
        return nums

    def etiqueta(self, num_id, nivel):
        """Etiqueta que Word muestra en un párrafo numerado: «3.», «b)», «iv.» o «-»."""
        niveles = self.formatos.get(num_id, {})
        fmt, plantilla, inicio = niveles.get(nivel, ("bullet", "", 1))
        if fmt in ("bullet", "none"):
            return "-"
        cont = self.contadores.setdefault(num_id, {})
        cont[nivel] = cont.get(nivel, inicio - 1) + 1
        for k in [k for k in cont if k > nivel]:
            del cont[k]

        def numero(k):
            f, _, ini = niveles.get(k, ("decimal", "", 1))
            n = cont.get(k, ini)
            if f == "lowerLetter":
                return chr(96 + (n - 1) % 26 + 1)
            if f == "upperLetter":
                return chr(64 + (n - 1) % 26 + 1)
            if f in ("lowerRoman", "upperRoman"):
                r = romano(n)
                return r.lower() if f == "lowerRoman" else r
            return str(n)

        return re.sub(r"%(\d)", lambda m: numero(int(m.group(1)) - 1), plantilla) \
            or f"{cont[nivel]}."

    def ole(self, obj):
        """('math', latex, alt) de un w:object de Equation 3.0."""
        ole = obj.find(f"{O}OLEObject")
        forma = obj.find(f"{V}shape")
        alt = (forma.get("alt") or "").strip() if forma is not None else ""
        if ole is None or not (ole.get("ProgID") or "").startswith("Equation"):
            return ("txt", f"[objeto: {alt}]" if alt else "[objeto]")
        self.n_ole += 1
        destino = self.rels.get(ole.get(R + "id"), "")
        try:
            latex = ecuacion_ole(self.z.read("word/" + destino))
        except KeyError:
            latex = None
        if latex is None:
            return ("math", r"\text{[ecuación ilegible]}", alt or "?")
        self.n_ok += 1
        if alt and not coinciden(latex, alt):
            self.n_alt += 1
            return ("math", latex, alt)
        return ("math", latex, None)

    def en_linea(self, nodo, piezas):
        for h in nodo:
            t = h.tag
            if t == M + "oMathPara":
                self.n_omml += 1
                piezas.append(("mathbloque", limpiar(omml(h)), None))
            elif t == M + "oMath":
                self.n_omml += 1
                piezas.append(("math", limpiar(omml(h)), None))
            elif t == W + "t":
                piezas.append(("txt", h.text or ""))
            elif t == W + "tab":
                piezas.append(("txt", " "))
            elif t in (W + "br", W + "cr"):
                piezas.append(("txt", "  \n"))
            elif t == W + "object":
                piezas.append(self.ole(h))
            elif t == MC + "AlternateContent":
                eleccion = h.find(MC + "Choice")
                if eleccion is not None:
                    self.en_linea(eleccion, piezas)
            elif t in (W + "pPr", W + "rPr", W + "delText", W + "instrText"):
                continue
            else:
                self.en_linea(h, piezas)

    def parrafo(self, p, en_tabla=False):
        estilo = p.find(f"{W}pPr/{W}pStyle")
        estilo = estilo.get(W + "val") if estilo is not None else ""
        if estilo.startswith("TDC") or estilo == "TtuloTDC":
            return None
        piezas = []
        self.en_linea(p, piezas)
        solo_math = [x for x in piezas if x[0] != "txt" or x[1].strip()]
        # Un literal numerado que es solo una fórmula («b. <fracción>») conserva su etiqueta:
        # va en línea, no en bloque, para no perder la letra ni correr las siguientes.
        numerado = p.find(f"{W}pPr/{W}numPr/{W}numId") is not None and \
            p.find(f"{W}pPr/{W}numPr/{W}numId").get(W + "val") != "0"
        if not en_tabla and not numerado and solo_math \
                and all(x[0].startswith("math") for x in solo_math):
            cuerpo = "\n".join(x[1] for x in solo_math)
            alts = [f"<!-- alt: {x[2]} -->" for x in solo_math if x[2]]
            return "```latex\n" + cuerpo + "\n```" + ("\n" + "\n".join(alts) if alts else "")
        texto = ""
        for x in piezas:
            if x[0] == "txt":
                texto += x[1]
            else:
                texto += f" ${x[1]}$ " + (f"<!-- alt: {x[2]} -->" if x[2] else "")
        texto = re.sub(r"[ \t]+", " ", texto).strip()
        if not texto:
            return ""
        m = re.fullmatch(r"Ttulo(\d)", estilo)
        if m:
            return "#" * int(m.group(1)) + " " + texto
        if estilo == "Subttulo":
            return f"**{texto}**"
        if estilo == "Descripcin":
            return f"*{texto}*"
        num = p.find(f"{W}pPr/{W}numPr")
        if num is not None and not en_tabla:
            nivel = num.find(W + "ilvl")
            nivel = int(nivel.get(W + "val")) if nivel is not None else 0
            num_id = num.find(W + "numId")
            num_id = num_id.get(W + "val") if num_id is not None else "0"
            if num_id != "0":
                return "  " * nivel + self.etiqueta(num_id, nivel) + " " + texto
        return texto

    def tabla(self, tbl):
        filas = []
        for tr in tbl.findall(W + "tr"):
            celdas = []
            for tc in tr.findall(W + "tc"):
                partes = [self.parrafo(p, en_tabla=True) for p in tc.iter(W + "p")]
                celdas.append("<br>".join(x for x in partes if x).replace("|", r"\|"))
            filas.append(celdas)
        if not filas:
            return ""
        n = max(len(f) for f in filas)
        filas = [f + [""] * (n - len(f)) for f in filas]
        lineas = ["| " + " | ".join(filas[0]) + " |", "|" + " --- |" * n]
        lineas += ["| " + " | ".join(f) + " |" for f in filas[1:]]
        return "\n".join(lineas)

    def recorrer(self, elemento, bloques):
        for h in elemento:
            if h.tag == W + "p":
                b = self.parrafo(h)
                if b:
                    bloques.append(b)
            elif h.tag == W + "tbl":
                bloques.append(self.tabla(h))
            elif h.tag != W + "sectPr":
                self.recorrer(h, bloques)

    def markdown(self):
        raiz = ET.fromstring(self.z.read("word/document.xml"))
        bloques = []
        self.recorrer(raiz.find(W + "body"), bloques)
        md = "\n\n".join(bloques) + "\n"
        return re.sub(r"\n{3,}", "\n\n", md)


def romano(n):
    salida = ""
    for valor_r, letra in ((1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
                           (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
                           (5, "V"), (4, "IV"), (1, "I")):
        while n >= valor_r:
            salida += letra
            n -= valor_r
    return salida


def coinciden(latex, alt):
    """¿Los números de la fórmula son los mismos que los de su texto alternativo?"""
    nums = lambda s: re.findall(r"\d+", s.replace(".", "").replace(",", ""))
    alt = alt.lower()
    for palabra, n in PALABRAS_NUMERO:
        alt = re.sub(rf"\b{palabra}\b", f" {n} ", alt)
    return nums(re.sub(r"\\[A-Za-z]+", " ", latex)) == nums(alt)


# Cómo lee números el texto alternativo: «un medio», «5 tercios», «x al cuadrado».
PALABRAS_NUMERO = [
    ("al cuadrado", 2), ("al cubo", 3), ("medios?", 2), ("tercios?", 3), ("cuartos?", 4),
    ("quintos?", 5), ("sextos?", 6), ("s[eé]ptimos?", 7), ("octavos?", 8), ("novenos?", 9),
    ("d[eé]cimos?", 10), ("un[oa]?", 1), ("dos", 2), ("tres", 3), ("cuatro", 4), ("cinco", 5),
    ("seis", 6), ("siete", 7), ("ocho", 8), ("nueve", 9), ("diez", 10), ("cero", 0),
]


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit(__doc__)
    for ruta in map(Path, args):
        doc = Documento(ruta)
        md = doc.markdown()
        salida = ruta.parent / "markdown" / (ruta.stem + ".md")
        salida.parent.mkdir(parents=True, exist_ok=True)
        salida.write_text(md, encoding="utf-8")
        resumen = f"{salida}: {len(md.split())} palabras"
        if doc.n_ole:
            resumen += (f"; Equation 3.0: {doc.n_ok}/{doc.n_ole} leídas, "
                        f"{doc.n_alt} con <!-- alt --> para revisar")
        if doc.n_omml:
            resumen += f"; OMML: {doc.n_omml}"
        print(resumen)
    if "--diagnostico" in sys.argv and desconocidos:
        print("\nSin traducir:")
        for k, n in desconocidos.most_common():
            print(f"  {n:5}  {k}")


if __name__ == "__main__":
    main()
