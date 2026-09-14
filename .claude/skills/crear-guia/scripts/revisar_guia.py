#!/usr/bin/env python3
"""Revisa la estructura de una guía del estudiante trimestral (skill crear-guia).

Uso:  python3 revisar_guia.py ruta/guia-periodo-I-tema.tex [--compilar]

Comprueba: ruta del estilo, bloque de datos sin valores de ejemplo, orden de las
secciones obligatorias, que cada \\tema tenga etiqueta y los bloques hilo → aplicacion →
preguntas → resumen, que las citas estén en el marco teórico, y que cada \\cite tenga
su \\bibitem. Con --compilar corre latexmk (sin borrar el .aux) y resume el log.
Sale con código 1 si hay errores. Solo usa la biblioteca estándar.
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

DATOS = ["tipodocumento", "asignatura", "titulo", "grado", "periodo", "hiloconductor"]
MUESTRAS = ["La matemática del cambio: la derivada", "La carrera por el cálculo",
            "Formas y caminos a mi alrededor", "El paseo de Rinrín Renacuajo"]
BLOQUES = ["hilo", "aplicacion", "preguntas", "resumen"]


def sin_comentarios(texto):
    return re.sub(r"(?m)(?<!\\)%.*$", "", texto)


def main():
    rutas = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(rutas) != 1:
        sys.exit(__doc__)
    tex = Path(rutas[0]).resolve()
    fuente = tex.read_text(encoding="utf-8")
    cuerpo = sin_comentarios(fuente)
    errores, avisos = [], []

    # Ubicación y nombre
    es_plantilla = "/plantillas/" in tex.as_posix()
    if not es_plantilla and not re.search(
            r"/materias/[^/]+/[^/]+/guia-didactica/guia-periodo-(I|II|III)-[a-z0-9-]+\.tex$",
            tex.as_posix()):
        avisos.append("nombre o ubicación fuera del esquema: "
                      "materias/<a>/<g>/guia-didactica/guia-periodo-<I|II|III>-<slug>.tex")

    # Estilo compartido
    ruta = re.search(r"\\def\\input@path\{\{([^}]*)\}\}", cuerpo)
    if not ruta:
        errores.append("falta \\def\\input@path{{...}} antes de \\usepackage{mmcantillo}")
    elif not (tex.parent / ruta.group(1) / "mmcantillo.sty").exists():
        errores.append(f"\\input@path no llega a mmcantillo.sty: {ruta.group(1)}")

    # Bloque de datos
    for campo in DATOS:
        v = re.search(r"\\" + campo + r"\{([^}]*)\}", cuerpo)
        if not v or not v.group(1).strip():
            errores.append(f"falta \\{campo}{{...}} en el bloque de datos")
    if not es_plantilla and any(m in cuerpo for m in MUESTRAS):
        errores.append("quedaron título o hilo de ejemplo de una plantilla")
    if not re.search(r"(?m)^%\s*DBA:", fuente):
        avisos.append("falta el comentario «% DBA: …» con el enunciado de cada DBA")

    # Orden de las partes obligatorias
    partes = [("\\frase{", "frase introductoria"),
              ("\\seccion{Introducción}", "introducción"),
              ("\\begin{dba}", "caja dba"),
              ("\\seccion{Marco teórico", "marco teórico"),  # admite «Marco teórico: …»
              ("\\tema{", "primer \\tema"),
              ("\\matrizevaluacion", "\\matrizevaluacion"),
              ("\\autoevaluacion", "\\autoevaluacion"),
              ("\\seguimientodocente", "\\seguimientodocente"),
              ("\\begin{referencias}", "referencias")]
    pos = []
    for marca, nombre in partes:
        i = cuerpo.find(marca)
        if i < 0:
            errores.append(f"falta la parte obligatoria: {nombre}")
        pos.append(i)
    presentes = [(p, n) for p, (_, n) in zip(pos, partes) if p >= 0]
    for (p1, n1), (p2, n2) in zip(presentes, presentes[1:]):
        if p2 < p1:
            errores.append(f"orden incorrecto: «{n2}» aparece antes que «{n1}»")
    if re.search(r"\\seccion\{Evaluaci", cuerpo):
        avisos.append("sobra \\seccion{Evaluación…}: \\matrizevaluacion ya imprime su título")

    # Temas
    inicios = [m.start() for m in re.finditer(r"\\tema\{", cuerpo)]
    fin_temas = min([i for i in (cuerpo.find("\\seccion{", inicios[-1] if inicios else 0),
                                 cuerpo.find("\\matrizevaluacion")) if i >= 0] or [len(cuerpo)])
    etiquetas = []
    for k, ini in enumerate(inicios):
        fin = inicios[k + 1] if k + 1 < len(inicios) else fin_temas
        bloque = cuerpo[ini:fin]
        titulo = re.match(r"\\tema\{([^}]*)\}", bloque).group(1)
        etiqueta = re.match(r"\\tema\{[^}]*\}\s*\\label\{(tema:[^}]+)\}", bloque)
        if not etiqueta:
            errores.append(f"«{titulo}»: falta \\label{{tema:...}} justo después de \\tema")
        else:
            etiquetas.append(etiqueta.group(1))
        lugares = [bloque.find("\\begin{" + b + "}") for b in BLOQUES]
        for b, i in zip(BLOQUES, lugares):
            if i < 0:
                errores.append(f"«{titulo}»: falta el bloque {b}")
        vistos = [(i, b) for b, i in zip(BLOQUES, lugares) if i >= 0]
        if [b for _, b in sorted(vistos)] != [b for _, b in vistos]:
            errores.append(f"«{titulo}»: el orden debe ser hilo → aplicacion → preguntas → resumen")
        if bloque.rfind("\\begin{preguntas}") > bloque.rfind("\\begin{resumen}") >= 0:
            errores.append(f"«{titulo}»: el resumen debe cerrar el tema")
        for preg in re.split(r"\\pregunta\b", bloque)[1:]:
            preg = preg.split("\\end{preguntas}")[0]
            if (re.search(r"(?<![\w\\])a\)\s", preg) and re.search(r"(?<![\w\\])b\)\s", preg)
                    and "\\begin{opciones" not in preg):
                avisos.append(f"«{titulo}»: sub-ítems a) b) escritos en línea; "
                              f"usa \\begin{{opciones*}}")
                break
    for e in {e for e in etiquetas if etiquetas.count(e) > 1}:
        errores.append(f"etiqueta repetida: {e}")

    # Citas y referencias
    marco = cuerpo.find("\\seccion{Marco teórico")
    primer_tema = inicios[0] if inicios else len(cuerpo)
    for m in re.finditer(r"\\begin\{cita\}", cuerpo):
        if not marco <= m.start() < primer_tema:
            avisos.append("hay una cita (\\begin{cita}) fuera del marco teórico")
    citas = {c.strip() for grupo in re.findall(r"\\cite\{([^}]*)\}", cuerpo)
             for c in grupo.split(",")}
    items = set(re.findall(r"\\bibitem\{([^}]*)\}", cuerpo))
    for c in sorted(citas - items):
        errores.append(f"\\cite{{{c}}} sin \\bibitem")
    for b in sorted(items - citas):
        avisos.append(f"\\bibitem{{{b}}} nunca se cita")

    # Verificación: la línea anterior a cada \bibitem, \frase y \begin{cita} debe ser
    # «% verificado: <URL o ruta en recursos/> — <qué se comprobó>»
    lineas = fuente.splitlines()
    sin_verificar = []
    for n, linea in enumerate(lineas):
        m = re.match(r"\s*\\(?:bibitem\{([^}]*)\}|(frase)\{|begin\{(cita)\})", linea)
        if not m:
            continue
        previa = lineas[n - 1].strip() if n else ""
        ok = re.match(r"%\s*verificado:\s*(https?://\S+|recursos/\S+)", previa)
        if not ok:
            que = (f"\\bibitem{{{m.group(1)}}}" if m.group(1)
                   else "\\frase" if m.group(2) else f"cita (línea {n + 1})")
            sin_verificar.append(que)
    for que in sin_verificar:
        errores.append(f"{que} sin «% verificado: <URL> — …» en la línea anterior")

    print(f"{tex.name}: {len(inicios)} temas, {len(citas)} fuentes citadas, "
          f"{cuerpo.count(chr(92) + 'begin{dba}')} cajas DBA, "
          f"{cuerpo.count(chr(92) + 'pregunta')} preguntas")
    for e in etiquetas:
        print(f"  {e}")

    if "--compilar" in sys.argv and not errores and not shutil.which("latexmk"):
        errores.append("no hay LaTeX (latexmk) en este entorno: la guía NO se compiló ni se "
                       "revisó visualmente; hay que compilarla donde haya LaTeX (el Mac de la docente)")
    elif "--compilar" in sys.argv and not errores:
        r = subprocess.run(["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error",
                            tex.name], cwd=tex.parent, capture_output=True, text=True,
                           encoding="utf-8", errors="replace")  # latexmk no siempre emite UTF-8
        log = tex.with_suffix(".log")
        texto = log.read_text(encoding="utf-8", errors="replace") if log.exists() else ""
        for linea in texto.splitlines():
            if linea.startswith("!"):
                errores.append(f"LaTeX: {linea}")
        perdidos = texto.count("Missing character")
        if perdidos:
            errores.append(f"{perdidos} caracteres que la fuente no tiene: salen en blanco sin "
                           f"error. Para ver la línea: pdflatex \"\\tracinglostchars=3\\input{{{tex.stem}}}\"")
        overfull = texto.count("Overfull \\hbox")
        if overfull:
            avisos.append(f"{overfull} líneas Overfull \\hbox (texto que se sale del margen)")
        if re.search(r"(Citation|Reference) .* undefined", texto):
            errores.append("hay citas o referencias sin definir (¿falta una pasada de latexmk?)")
        if r.returncode == 0:
            pdf = tex.with_suffix(".pdf")
            paginas = (subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True)
                       if shutil.which("pdfinfo") else None)
            n = paginas and re.search(r"Pages:\s+(\d+)", paginas.stdout)
            print(f"Compilado: {pdf.name}, {n.group(1) if n else '?'} páginas "
                  f"(el .aux se conserva para \\refguia)")

    for a in avisos:
        print(f"AVISO: {a}")
    for e in errores:
        print(f"ERROR: {e}")
    if not errores:
        print("Sin errores de estructura. Falta la revisión visual página por página.")
    sys.exit(1 if errores else 0)


if __name__ == "__main__":
    main()
