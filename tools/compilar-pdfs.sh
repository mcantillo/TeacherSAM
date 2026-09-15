#!/usr/bin/env bash
# Compila a PDF los .tex de materias/ que cambiaron entre dos commits.
#
#   tools/compilar-pdfs.sh [BASE [HEAD]]   cambiados entre BASE y HEAD (por defecto HEAD~1 y HEAD)
#   tools/compilar-pdfs.sh --todos         todos los .tex de materias/
#
# Orden: primero las guías (guia-didactica/), porque las clases leen su .aux; si cambia
# una guía, también se recompilan las clases que la citan con \guiadelestudiante.
# Los .tex con \begin{solucion} generan además su clave (<nombre>-clave.pdf).
# Se limpia con latexmk -c, salvo en guia-didactica/, cuyo .aux debe quedar.
set -uo pipefail

cd "$(git rev-parse --show-toplevel)"

if [[ "${1:-}" == "--todos" ]]; then
  mapfile -t cambiados < <(git ls-files 'materias/*.tex')
else
  base="${1:-HEAD~1}" head="${2:-HEAD}"
  mapfile -t cambiados < <(git diff --name-only --diff-filter=AMR "$base" "$head" -- 'materias/*.tex')
fi

# Clases que citan una guía cambiada.
declare -A lista=()
for f in "${cambiados[@]}"; do
  [[ -f "$f" ]] || continue
  lista["$f"]=1
  if [[ "$f" == */guia-didactica/* ]]; then
    guia="$(basename "$f" .tex)"
    curso="${f%%/guia-didactica/*}"
    while IFS= read -r c; do lista["$c"]=1; done \
      < <(grep -rlE "\\\\guiadelestudiante\{[^}]*/${guia}\}" --include='*.tex' "$curso" || true)
  fi
done

if [[ ${#lista[@]} -eq 0 ]]; then
  echo "No hay .tex nuevos o modificados en materias/."
  exit 0
fi

# Guías primero, luego el resto en orden alfabético.
mapfile -t ordenados < <(printf '%s\n' "${!lista[@]}" | sort | awk '/\/guia-didactica\//{print; next} {r[++n]=$0} END{for(i=1;i<=n;i++) print r[i]}')

echo "Se compilarán ${#ordenados[@]} archivo(s):"
printf '  %s\n' "${ordenados[@]}"

compilar() {  # compilar <nombre.tex> [jobname con clave]
  local opts=(-pdf -interaction=nonstopmode -halt-on-error -file-line-error)
  [[ -n "${2:-}" ]] && opts+=(-jobname="$2" -usepretex='\def\clave{}')
  local salida
  salida="$(latexmk "${opts[@]}" "$1" 2>&1)" || {
    local log="${2:-${1%.tex}}.log"
    echo "    ERROR:"
    if grep -qE '^(!|.*:[0-9]+:)' "$log" 2>/dev/null; then
      grep -A3 -E '^(!|.*:[0-9]+:)' "$log" | head -15 | sed 's/^/      /'
    else
      tail -15 <<< "$salida" | sed 's/^/      /'
    fi
    return 1
  }
}

fallidos=()
for f in "${ordenados[@]}"; do
  dir="$(dirname "$f")" archivo="$(basename "$f")" nombre="$(basename "$f" .tex)"
  echo "==> $f"
  (
    cd "$dir" || exit 1
    ok=0
    compilar "$archivo" || ok=1
    if grep -q '\\begin{solucion}' "$archivo"; then
      echo "    + clave: $nombre-clave.pdf"
      compilar "$archivo" "$nombre-clave" || ok=1
    fi
    if [[ "$dir" != */guia-didactica ]]; then
      latexmk -c "$archivo" > /dev/null 2>&1
      [[ -f "$nombre-clave.pdf" ]] && latexmk -c -jobname="$nombre-clave" "$archivo" > /dev/null 2>&1
    else
      rm -f "$nombre".{log,fls,fdb_latexmk,out,toc}   # el .aux se queda
    fi
    exit $ok
  ) || fallidos+=("$f")
done

if [[ ${#fallidos[@]} -gt 0 ]]; then
  echo
  echo "Fallaron ${#fallidos[@]} archivo(s):"
  printf '  %s\n' "${fallidos[@]}"
  exit 1
fi
echo "Listo."
