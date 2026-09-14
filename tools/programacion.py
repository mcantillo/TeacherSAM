#!/usr/bin/env python3
"""Genera o actualiza materias/<asignatura>/<grado>/curriculo/programacion.csv.

Uso:  python3 tools/programacion.py            # escribe los CSV
      python3 tools/programacion.py --dry-run  # solo muestra el resumen

Fuentes (en la raíz del repo, nunca se copian fechas aquí):
  horario-2026-2027.md      horario semanal (tabla H / Lunes..Viernes, celdas «11° Cálculo»)
  programacion-2026-2027.md calendario: tablas «Trimestres», «Semanas sin clases» y «Festivos»

Una fila por sesión: las horas seguidas del mismo curso el mismo día son una sola sesión
(minutos sumados); horas no seguidas el mismo día son filas distintas. `semana` es la semana
escolar del año (solo cuentan las semanas con al menos un día de clase), y todas las filas de
una semana comparten carpeta = clases/semana-NN.

Si el CSV ya existe, conserva las columnas de planeación (tema, subtema, dba, quiz, taller,
tarea) por número de clase y recalcula fecha, dia, inicio, minutos, periodo, semana y carpeta.
Solo usa la biblioteca estándar.
"""
import csv
import re
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HORARIO = ROOT / "horario-2026-2027.md"
CALENDARIO = ROOT / "programacion-2026-2027.md"

ASIGNATURAS = {"geomet": "geometria", "geometría": "geometria", "álgebra": "algebra",
               "cálculo": "calculo", "física": "fisica", "trigo": "trigonometria",
               "trigonometría": "trigonometria"}
GRADOS = {3: "tercero", 4: "cuarto", 5: "quinto", 6: "sexto", 7: "septimo",
          8: "octavo", 9: "noveno", 10: "decimo", 11: "undecimo"}
DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes"]
CAMPOS = ["clase", "fecha", "dia", "inicio", "minutos", "periodo", "semana",
          "tema", "subtema", "dba", "quiz", "taller", "tarea", "carpeta"]
PLAN = ["tema", "subtema", "dba", "quiz", "taller", "tarea"]
FECHA = re.compile(r"\d{4}-\d{2}-\d{2}")


def minutos_del_dia(hhmm):
    """«1:40» -> minutos desde medianoche; las horas 1–5 son de la tarde."""
    h, m = map(int, hhmm.split(":"))
    return (h + 12 if h < 6 else h) * 60 + m


def leer_horario():
    """{(asignatura, grado): [[dia, inicio, fin], ...]} con las horas seguidas unidas."""
    bloques = {}
    for linea in HORARIO.read_text(encoding="utf-8").splitlines():
        celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
        if len(celdas) < 7 or not celdas[1].isdigit():
            continue  # encabezado, separador o descanso
        m = re.match(r"(\d{1,2}:\d{2}) a (\d{1,2}:\d{2})", celdas[0])
        ini, fin = minutos_del_dia(m.group(1)), minutos_del_dia(m.group(2))
        for dia, celda in enumerate(celdas[2:7]):
            c = re.match(r"(\d{1,2})°\s*(\S+)", celda)
            if not c:
                continue
            nombre = c.group(2).lower()
            if nombre not in ASIGNATURAS:
                sys.exit(f"Asignatura desconocida en el horario: «{celda}»")
            clave = (ASIGNATURAS[nombre], int(c.group(1)))
            bloques.setdefault(clave, []).append([dia, ini, fin])
    for clave, bs in bloques.items():
        bs.sort()
        unidos = []
        for b in bs:
            if unidos and unidos[-1][0] == b[0] and unidos[-1][2] == b[1]:
                unidos[-1][2] = b[2]  # hora seguida: misma sesión
            else:
                unidos.append(b)
        bloques[clave] = unidos
    return bloques


def leer_calendario():
    """(periodos [(nombre, inicio, fin)], sin_clase [(inicio, fin)], festivos {fecha})."""
    periodos, sin_clase, festivos, seccion = [], [], set(), ""
    for linea in CALENDARIO.read_text(encoding="utf-8").splitlines():
        if linea.startswith("## "):
            seccion = linea[3:].lower()
            continue
        fechas = [date.fromisoformat(f) for f in FECHA.findall(linea)]
        if not linea.startswith("|") or not fechas:
            continue
        if seccion.startswith("trimestres"):
            nombre = linea.strip().strip("|").split("|")[0].strip()
            periodos.append((nombre, fechas[0], fechas[1]))
        elif seccion.startswith("semanas sin clases"):
            sin_clase.append((fechas[0], fechas[1]))
        elif seccion.startswith("festivos"):
            festivos.add(fechas[0])
    if not periodos:
        sys.exit(f"No encontré la tabla «## Trimestres» en {CALENDARIO.name}")
    return periodos, sin_clase, festivos


def dias_de_clase(periodos, sin_clase, festivos):
    """[(fecha, periodo, semana)] de todos los días hábiles con clase del año."""
    dias, semanas = [], {}
    for nombre, ini, fin in periodos:
        f = ini
        while f <= fin:
            libre = (f.weekday() > 4 or f in festivos
                     or any(a <= f <= b for a, b in sin_clase))
            if not libre:
                lunes = f - timedelta(days=f.weekday())
                semanas.setdefault(lunes, len(semanas) + 1)
                dias.append((f, nombre, semanas[lunes]))
            f += timedelta(days=1)
    return dias


def hhmm(minutos):
    return f"{minutos // 60:02d}:{minutos % 60:02d}"


def main(dry_run=False):
    periodos, sin_clase, festivos = leer_calendario()
    dias = dias_de_clase(periodos, sin_clase, festivos)
    print(f"Calendario: {len(dias)} días de clase, {dias[-1][2]} semanas escolares")
    for (asig, grado), bloques in sorted(leer_horario().items()):
        carpeta = ROOT / "materias" / asig / GRADOS[grado]
        if not carpeta.is_dir():
            print(f"AVISO {asig} {grado}°: no existe {carpeta.relative_to(ROOT)}; "
                  f"pregúntale a la docente antes de crearla")
            continue
        filas = []
        for f, periodo, semana in dias:
            for dia, ini, fin in bloques:
                if dia == f.weekday():
                    filas.append({"fecha": f.isoformat(), "dia": DIAS[dia],
                                  "inicio": hhmm(ini), "minutos": str(fin - ini),
                                  "periodo": periodo, "semana": f"{semana:02d}",
                                  "carpeta": f"clases/semana-{semana:02d}"})
        destino = carpeta / "curriculo" / "programacion.csv"
        previas = {}
        if destino.exists():
            with open(destino, encoding="utf-8", newline="") as fh:
                previas = {r["clase"]: r for r in csv.DictReader(fh)}
        for i, fila in enumerate(filas, 1):
            fila["clase"] = f"{i:03d}"
            vieja = previas.get(fila["clase"], {})
            for campo in PLAN:
                fila[campo] = vieja.get(campo, "")
        perdidas = [c for c, r in previas.items()
                    if int(c) > len(filas) and any(r.get(k) for k in PLAN)]
        por_periodo = {p: sum(1 for r in filas if r["periodo"] == p) for p, _, _ in periodos}
        resumen = " · ".join(f"{p}: {n}" for p, n in por_periodo.items())
        print(f"{asig:14} {grado:>2}°  {len(bloques)} sesiones/semana  "
              f"{len(filas):3} sesiones ({resumen})")
        if perdidas:
            print(f"  AVISO: el calendario nuevo tiene menos sesiones; se perderían los "
                  f"temas planeados de las clases {', '.join(perdidas)}. No se escribe.")
            continue
        if not dry_run:
            destino.parent.mkdir(exist_ok=True)
            with open(destino, "w", encoding="utf-8", newline="") as fh:
                w = csv.DictWriter(fh, fieldnames=CAMPOS)
                w.writeheader()
                w.writerows(filas)


if __name__ == "__main__":
    main(dry_run="--dry-run" in sys.argv)
