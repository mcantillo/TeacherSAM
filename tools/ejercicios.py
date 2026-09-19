#!/usr/bin/env python3
"""Banco de ejercicios verificados: registro, verificación condicional y consulta.

Uso (desde la raíz, igual en Claude Code y en Cowork). Si este Python no tiene SymPy y la carpeta
tiene un .venv/ que funciona (el Mac de la docente), la herramienta pasa a usarlo sola; si no,
instala las dependencias con: python3 -m pip install -r tools/requirements.txt
  python3 tools/ejercicios.py verificar [recursos/banco/.../tema.py ...]  # solo nuevos o cambiados
  python3 tools/ejercicios.py verificar --todos                   # vuelve a ejecutar todo
  python3 tools/ejercicios.py listar [--tema T] [--grado N] [--estado E]
  python3 tools/ejercicios.py mostrar ID [ID ...]                  # enunciado y respuesta en LaTeX
  python3 tools/ejercicios.py aprobar ID [ID ...]                  # la docente aprobó una respuesta manual
  python3 tools/ejercicios.py catalogo                             # vuelca el banco a recursos/banco/catalogo.jsonl

Cada archivo recursos/banco/<area>/<tema>.py registra ejercicios con @ejercicio(...) (comprobación con
código) o ejercicio_manual(...) (respuesta modelo que aprueba la docente). El formato está en
.claude/skills/verificar-ejercicios/SKILL.md.

El estado vive en recursos/banco/verificados.json: id -> {huella, estado, fecha, archivo}. La huella
cubre enunciado, respuesta y el código de la comprobación: si nada cambió y el ejercicio ya
estaba verificado, no se vuelve a ejecutar.
Estados: verificado · falla · manual-pendiente · manual-aprobado.
"""
import argparse
import hashlib
import importlib.util
import inspect
import json
import os
import re
import sys
import traceback
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
BANCO = RAIZ / "recursos" / "banco"
REGISTRO = BANCO / "verificados.json"
OBLIGATORIOS = {"id", "enunciado", "respuesta"}
CAMPOS = OBLIGATORIOS | {"tema", "grados", "dba", "tipo", "dificultad", "fuente", "notas"}
USABLES = {"verificado", "manual-aprobado"}

_EJERCICIOS = []


# ---------- API para los archivos del banco ----------

def _registrar(meta, comprobar):
    faltan = OBLIGATORIOS - set(meta)
    desconocidos = set(meta) - CAMPOS
    if faltan or desconocidos:
        raise TypeError(f"{meta.get('id', '?')}: faltan {sorted(faltan)} / "
                        f"campos desconocidos {sorted(desconocidos)}")
    _EJERCICIOS.append({**meta, "enunciado": meta["enunciado"].strip(),
                        "respuesta": meta["respuesta"].strip(), "comprobar": comprobar})


def ejercicio(**meta):
    """Decorador: la función decorada comprueba la respuesta con assert (sin argumentos)."""
    def registrar(funcion):
        _registrar(meta, funcion)
        return funcion
    return registrar


def ejercicio_manual(**meta):
    """Ejercicio sin comprobación con código (explicar, argumentar, dibujar)."""
    _registrar(meta, None)


def latex_es(expr):
    """sympy.latex con los nombres de funciones en español (sen, tg, arcsen, arctg)."""
    import sympy
    s = sympy.latex(expr)
    for ingles, espanol in ((r"\sin", r"\sen"), (r"\tan", r"\tg"),
                            (r"\operatorname{asin}", r"\arcsen"), (r"\operatorname{atan}", r"\arctg")):
        s = s.replace(ingles, espanol)
    return s


# ---------- Ayudas para desigualdades, intervalos y conjuntos ----------
# Una misma cadena («4 - 3x > 7 + 2x») da el enunciado en LaTeX y la expresión que resuelve
# SymPy, así que no pueden contradecirse. La solución la escribe a mano quien crea el
# ejercicio, con conjunto(«(-oo, -3/5)»), y la comprobación la compara con solveset.
# Si cambias estas funciones, vuelve a correr: python3 tools/ejercicios.py verificar --todos

_REL = r"(<=|>=|<|>|=)"
_REL_TEX = {"<=": r"\le", ">=": r"\ge", "<": "<", ">": ">", "=": "="}


def expresion(texto, evaluar=True):
    """SymPy de «3x - 5/2», «Abs(x - 2)», «sqrt(2)x», «x^2»: minúsculas = variables reales.
    Con evaluar=True los decimales pasan a fracciones (0.3 → 3/10) para resolver exacto."""
    import sympy
    from sympy.parsing.sympy_parser import (convert_xor, implicit_multiplication, parse_expr,
                                            rationalize, standard_transformations)
    trans = standard_transformations + (implicit_multiplication, convert_xor)
    if evaluar:
        trans += (rationalize,)
    letras = {c: sympy.Symbol(c, real=True) for c in "abcdfghjklmnpqrstuvwxyz"}
    return parse_expr(texto, local_dict=letras, transformations=trans, evaluate=evaluar)


def tex(texto):
    """LaTeX de una expresión tal como está escrita (sin reordenar ni simplificar)."""
    import sympy
    s = sympy.latex(expresion(texto, evaluar=False), order="none")
    s = re.sub(r"(?<![\d.}])1 \\cdot ", "", s)          # «- 1 \cdot \frac{1}{4}» → «- \frac{1}{4}»
    s = s.replace(r"\left|{", r"\left|").replace(r"}\right|", r"\right|")
    s = re.sub(r"(\d)\.(\d)", r"\1{,}\2", s)            # coma decimal
    s = re.sub(r"(\d) (?=[a-z]|\\(?:sqrt|left|pi))", r"\1", s)   # «3 x» → «3x»
    return re.sub(r"^- ", "-", s)


def desigualdad(texto):
    """(LaTeX, conjunto solución en ℝ) de «4 - 3x > 7 + 2x», de una cadena
    «-1 < (3 - 7x)/4 <= 6» o de una ecuación «Abs(4x - 5) = 3». Sin variables: ℝ si es
    verdadera, ∅ si es falsa."""
    import sympy
    trozos = [t.strip() for t in re.split(_REL, texto)]
    miembros, rels = trozos[0::2], trozos[1::2]
    partes = []
    for m, r in zip(miembros, rels):
        partes += [tex(m), _REL_TEX[r]]
    latex = " ".join(partes + [tex(miembros[-1])])
    clase = {"<": sympy.Lt, "<=": sympy.Le, ">": sympy.Gt, ">=": sympy.Ge, "=": sympy.Eq}
    solucion = sympy.S.Reals
    for a, r, b in zip(miembros, rels, miembros[1:]):
        rel = clase[r](expresion(a), expresion(b))
        libres = rel.free_symbols
        if not libres:
            solucion = solucion if bool(rel) else sympy.S.EmptySet
            continue
        assert len(libres) == 1, f"«{texto}» tiene más de una variable"
        solucion = solucion.intersect(sympy.solveset(rel, libres.pop(), sympy.S.Reals))
    return latex, solucion


def _separar(s):
    """Separa por comas de primer nivel: «-oo, (pi + 8)/3» → ['-oo', '(pi + 8)/3']."""
    partes, nivel, actual = [], 0, ""
    for c in s:
        nivel += c in "([" and 1 or c in ")]" and -1 or 0
        if c == "," and nivel == 0:
            partes.append(actual)
            actual = ""
        else:
            actual += c
    return [p.strip() for p in partes + [actual]]


def conjunto(texto):
    """(LaTeX, conjunto de SymPy) de «(-oo, -3/5]», «[2, 3) U (5, oo)», «{-8, -4}», «R»,
    «vacio». Si un extremo tiene decimales («[-3.6, 126]»), se separan con punto y coma."""
    import sympy
    total, partes = sympy.S.EmptySet, []
    for trozo in (t.strip() for t in texto.split(" U ")):
        if trozo == "R":
            total, t = total | sympy.S.Reals, r"\mathbb{R}"
        elif trozo == "vacio":
            t = r"\varnothing"
        elif trozo.startswith("{"):
            elementos = _separar(trozo[1:-1])
            total = total | sympy.FiniteSet(*map(expresion, elementos))
            t = r"\{" + ", ".join(map(tex, elementos)) + r"\}"
        else:
            a, b = _separar(trozo[1:-1])
            total = total | sympy.Interval(expresion(a), expresion(b),
                                           trozo[0] == "(", trozo[-1] == ")")
            sep = "; " if "." in a + b else ", "
            t = f"{trozo[0]}{tex(a)}{sep}{tex(b)}{trozo[-1]}"
        partes.append(t)
    return r" \cup ".join(partes), total


def serie(prefijo, instruccion, fuente, filas, **comun):
    """Registra ejercicios «resuelve…»: cada fila es (n, literal, inecuación o ecuación,
    solución escrita a mano con la notación de conjunto(), dificultad[, notas]).
    La «…» de la instrucción se reemplaza por la fórmula."""
    for n, literal, texto, solucion, dificultad, *notas in filas:
        vacia = " (ningún número real la cumple)" if solucion == "vacio" else ""
        frase = instruccion + ("." if instruccion.endswith("…") else "")
        meta = dict(id=f"{prefijo}-{n:03d}", dificultad=dificultad, fuente=f"{fuente} {literal}",
                    enunciado=frase.replace("…", f"${desigualdad(texto)[0]}$"),
                    respuesta=f"${conjunto(solucion)[0]}${vacia}.", **comun)
        if notas:
            meta["notas"] = notas[0]

        def comprobar(texto=texto, solucion=solucion):
            assert desigualdad(texto)[1] == conjunto(solucion)[1], "la solución no coincide"
        _registrar(meta, comprobar)


# ---------- Herramienta ----------

def huella(e):
    codigo = inspect.getsource(e["comprobar"]) if e["comprobar"] else "manual"
    datos = "\x00".join([e["enunciado"], e["respuesta"], codigo])
    return hashlib.sha256(datos.encode("utf-8")).hexdigest()[:16]


def cargar(archivo):
    _EJERCICIOS.clear()
    spec = importlib.util.spec_from_file_location(f"banco_{archivo.stem}", archivo)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    for e in _EJERCICIOS:
        e["archivo"] = archivo.relative_to(RAIZ).as_posix()
    return list(_EJERCICIOS)


def archivos_banco(rutas=None):
    if rutas:
        return [Path(r).resolve() for r in rutas]
    return sorted(p for p in BANCO.rglob("*.py") if not p.name.startswith("_"))


def cargar_todos(rutas=None):
    todos, errores = [], []
    for archivo in archivos_banco(rutas):
        try:
            todos += cargar(archivo)
        except Exception as ex:  # p. ej. falta SymPy o hay un error de sintaxis
            pista = (" — instala las dependencias: python3 -m pip install -r tools/requirements.txt"
                     if isinstance(ex, ModuleNotFoundError) else "")
            errores.append(f"{archivo.relative_to(RAIZ)}: {type(ex).__name__}: {ex}{pista}")
    vistos = {}
    for e in todos:
        if e["id"] in vistos:
            errores.append(f"id repetido: {e['id']} ({vistos[e['id']]} y {e['archivo']})")
        vistos[e["id"]] = e["archivo"]
    return todos, errores


def leer_registro():
    return json.loads(REGISTRO.read_text(encoding="utf-8")) if REGISTRO.exists() else {}


def guardar_registro(registro):
    REGISTRO.parent.mkdir(parents=True, exist_ok=True)
    REGISTRO.write_text(json.dumps(dict(sorted(registro.items())), ensure_ascii=False, indent=1)
                        + "\n", encoding="utf-8")


def cmd_verificar(args):
    ejercicios, errores = cargar_todos(args.archivos)
    # --sin-registro: corre todas las comprobaciones sin leer ni escribir verificados.json
    # (para agentes que trabajan en paralelo; el registro lo hace después una sola sesión).
    registro = {} if args.sin_registro else leer_registro()
    hoy = date.today().isoformat()
    cuenta = {"reutilizados": 0, "verificados": 0, "fallas": 0, "manuales pendientes": 0}
    for e in ejercicios:
        h, previo = huella(e), registro.get(e["id"], {})
        if not args.todos and previo.get("huella") == h and previo.get("estado") in USABLES:
            cuenta["reutilizados"] += 1
            continue
        if e["comprobar"] is None:
            estado, detalle = "manual-pendiente", "requiere aprobación de la docente"
            cuenta["manuales pendientes"] += 1
        else:
            try:
                e["comprobar"]()
                estado, detalle = "verificado", ""
                cuenta["verificados"] += 1
            except Exception:
                estado = "falla"
                detalle = traceback.format_exc(limit=1).strip().splitlines()[-1]
                cuenta["fallas"] += 1
        registro[e["id"]] = {"huella": h, "estado": estado, "fecha": hoy, "archivo": e["archivo"]}
        print(f"{'✓' if estado == 'verificado' else '✗' if estado == 'falla' else '·'} "
              f"{e['id']}: {estado}{' — ' + detalle if detalle else ''}")
    if not args.sin_registro:
        guardar_registro(registro)
    for err in errores:
        print(f"ERROR: {err}")
    print(" · ".join(f"{n} {k}" for k, n in cuenta.items()))
    return 1 if cuenta["fallas"] or errores else 0


def cmd_listar(args):
    ejercicios, errores = cargar_todos()
    registro = leer_registro()
    for e in ejercicios:
        estado = registro.get(e["id"], {}).get("estado", "sin verificar")
        if registro.get(e["id"], {}).get("huella") not in (None, huella(e)):
            estado = "cambió: re-verificar"
        if args.tema and args.tema.lower() not in str(e.get("tema", "")).lower():
            continue
        if args.grado and args.grado not in e.get("grados", []):
            continue
        if args.estado and args.estado != estado:
            continue
        if args.con_notas and not e.get("notas"):
            continue
        print(f"{e['id']:24} {estado:19} {e.get('grados', '')!s:8} {e.get('tipo', ''):18} "
              f"dif {e.get('dificultad', '?')}  {e.get('tema', '')} — {e['enunciado'][:60]}")
        if args.con_notas:
            print(f"{'':24} notas: {e['notas']}")
    for err in errores:
        print(f"ERROR: {err}")
    return 1 if errores else 0


def cmd_mostrar(args):
    ejercicios, errores = cargar_todos()
    registro = leer_registro()
    por_id = {e["id"]: e for e in ejercicios}
    for i in args.ids:
        e = por_id.get(i)
        if not e:
            print(f"{i}: no existe en el banco")
            continue
        print(f"% Ejercicio: {i}  ({registro.get(i, {}).get('estado', 'sin verificar')}; "
              f"{e['archivo']}; fuente: {e.get('fuente', '—')})")
        print(f"ENUNCIADO: {e['enunciado']}\nRESPUESTA: {e['respuesta']}\n")
    return 1 if errores else 0


def cmd_catalogo(args):
    """Vuelca todo el banco a un archivo de texto, para poder consultarlo sin SymPy.

    Existe porque cargar el banco importa los .py, y esos importan SymPy: en un entorno sin
    SymPy (Cowork) ni «listar» ni «mostrar» funcionan. El catálogo se regenera en GitHub
    Actions (.github/workflows/ejercicios.yml) y se guarda en el repositorio, así que desde
    cualquier parte se puede leer con json y escoger ejercicios.
    """
    ejercicios, errores = cargar_todos()
    registro = leer_registro()
    salida = Path(args.salida) if args.salida else BANCO / "catalogo.jsonl"
    with open(salida, "w", encoding="utf-8") as fh:
        for e in sorted(ejercicios, key=lambda x: x["id"]):
            estado = registro.get(e["id"], {}).get("estado", "sin verificar")
            if registro.get(e["id"], {}).get("huella") not in (None, huella(e)):
                estado = "cambió: re-verificar"
            fila = {"id": e["id"], "estado": estado, "usable": estado in USABLES,
                    "tema": e.get("tema"), "grados": e.get("grados", []),
                    "dba": e.get("dba"), "tipo": e.get("tipo"),
                    "dificultad": e.get("dificultad"), "manual": e["comprobar"] is None,
                    "archivo": str(e["archivo"]), "fuente": e.get("fuente"),
                    "notas": e.get("notas"),
                    "enunciado": e["enunciado"], "respuesta": e["respuesta"]}
            fh.write(json.dumps(fila, ensure_ascii=False) + "\n")
    print(f"{len(ejercicios)} ejercicios en {os.path.relpath(salida, RAIZ)}")
    for err in errores:
        print(f"ERROR: {err}")
    return 1 if errores else 0


def cmd_aprobar(args):
    ejercicios, errores = cargar_todos()
    registro = leer_registro()
    por_id = {e["id"]: e for e in ejercicios}
    for i in args.ids:
        e = por_id.get(i)
        if not e or e["comprobar"] is not None:
            print(f"{i}: no es un ejercicio manual del banco")
            continue
        registro[i] = {"huella": huella(e), "estado": "manual-aprobado",
                       "fecha": date.today().isoformat(), "archivo": e["archivo"]}
        print(f"· {i}: manual-aprobado")
    guardar_registro(registro)
    return 1 if errores else 0


def main():
    p = argparse.ArgumentParser(description="Banco de ejercicios verificados")
    sub = p.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("verificar"); v.add_argument("archivos", nargs="*"); v.add_argument("--todos", action="store_true")
    v.add_argument("--sin-registro", action="store_true",
                   help="comprobar sin escribir recursos/banco/verificados.json")
    ls = sub.add_parser("listar"); ls.add_argument("--tema"); ls.add_argument("--grado", type=int); ls.add_argument("--estado")
    ls.add_argument("--con-notas", action="store_true",
                    help="solo los que tienen notas (correcciones al recurso) y mostrarlas")
    m = sub.add_parser("mostrar"); m.add_argument("ids", nargs="+")
    a = sub.add_parser("aprobar"); a.add_argument("ids", nargs="+")
    sub.add_parser("catalogo").add_argument("--salida")
    args = p.parse_args()
    return {"verificar": cmd_verificar, "listar": cmd_listar, "mostrar": cmd_mostrar,
            "aprobar": cmd_aprobar, "catalogo": cmd_catalogo}[args.cmd](args)


if __name__ == "__main__":
    sys.dont_write_bytecode = True  # no dejar carpetas __pycache__ dentro de recursos/banco/ ni tools/
    try:
        import sympy  # noqa: F401
    except ImportError:
        venv = RAIZ / ".venv"
        if (venv / "bin" / "python").exists() and Path(sys.prefix).resolve() != venv.resolve():
            try:  # en el Mac de la docente; en Cowork ese .venv no puede ejecutarse y se sigue
                os.execv(str(venv / "bin" / "python"), [str(venv / "bin" / "python"), *sys.argv])
            except OSError:
                pass
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import ejercicios as lib  # los archivos del banco importan este mismo módulo
    sys.exit(lib.main())
