# Pendientes del banco de ejercicios

Estado al 2026-09-13, cuando ocho agentes llenaron el banco desde los recursos. Hay **3988 entradas**:
**3040 verificadas** con Python + SymPy, **948 abiertas** (esperan que la docente apruebe su
respuesta modelo), **563 con correcciones** al recurso anotadas en `notas` y **594 sin DBA**.

Que un ejercicio esté *verificado* garantiza que su respuesta es correcta **para el enunciado
que tiene**. No garantiza que el enunciado se haya copiado bien del recurso, que la corrección
elegida sea la que la docente prefiere ni que el LaTeX compile. Para eso sirven estas tareas.
Marca cada casilla (`[x]`) al terminarla. Cuando estén todas, el banco queda con confianza total
(ver «Criterio de cierre» al final).

Comandos útiles (desde la raíz; funcionan igual en Claude Code y en Cowork):

```
python3 tools/ejercicios.py listar --grado 9 --estado manual-pendiente   # abiertas de un grado
python3 tools/ejercicios.py listar --grado 8 --con-notas                 # correcciones de un grado
python3 tools/ejercicios.py mostrar <id> [<id> …]                        # enunciado y respuesta
python3 tools/ejercicios.py aprobar <id> [<id> …]                        # aprobar una abierta
python3 tools/ejercicios.py verificar --todos                            # volver a comprobar todo
```

---

## 1. Decisiones de la docente (bloquean el resto)

- [ ] **Temas repetidos en dos grados.** Tres temas del módulo de Geometría quedaron en dos
      cursos (18 ejercicios con el mismo enunciado). Decidir en qué grado se queda cada uno y
      borrar la copia del otro (o dejar uno solo con los dos grados en `grados`):
  - [ ] Triángulos, verdadero o falso y problemas: `triangulos-6.py` o `triangulos-8.py` (10 iguales).
  - [ ] Ángulos, demostraciones: `angulos-6-002/003` o `angulos-8-012/013`.
  - [ ] Pitágoras, problemas 3–8: `pitagoras-9-002…005` o `medicion-11-008…011`.
  - [ ] Física 9°: `ondas-9-017` y `sonido-9-025` son la misma pregunta, repetida en la guía; dejar una.
- [ ] **Física sin DBA** (594 entradas con `dba=[]`, que citan solo los estándares en la
      cabecera del archivo). Decidir cómo alinearlas:
  - [ ] 9°: `ondas-9`, `sonido-9`, `luz-9`, `optica-9`, `ondas-luminosas-9`, `termodinamica-9`
        (el único DBA de física de 9° es el de movimiento).
  - [ ] 10°: `mediciones-10`, `fluidos-10`, `termodinamica-10`.
  - [ ] 11°: preguntas del Icfes 15, 37 y 41 de `icfes-cuadernillo-2026-geometria.py` (no
        encajan en los DBA 4 ni 6): ¿se quedan como práctica Saber 11?
- [ ] **Grados y temas sin recurso.** Agregar un recurso a `recursos/` o pedir ejercicios propios
      redactados desde los DBA:
  - [ ] Geometría 3° y 4° (no hay ningún ejercicio).
  - [ ] Geometría 10°: cónicas (solo hay 7 ejercicios de rectas).
  - [ ] Geometría 11°: coordenadas polares y esféricas, precisión con instrumentos.
  - [ ] Geometría 7° y 9°: hay poco (10 y 6 ejercicios).
- [ ] **Contextos.** ¿Pasamos a unidades y pesos colombianos los problemas en millas, pies,
      varas y euros (Trigonometría 10°, Álgebra 9° tema 2, Física)? ¿Se acepta el cambio del
      contexto bélico de Álgebra 9° T3 ICFES 4–6 a uno neutral?
- [ ] **Alcance de Álgebra 8°.** ¿Entran los logaritmos (`logaritmos-8.py`, ningún DBA de 8° los
      nombra), el binomio de Newton hasta exponente 60 y los exponentes literales de Baldor?

## 2. Revisión de contenido

- [ ] **Aprobar las 948 abiertas**, por grado (`listar --grado N --estado manual-pendiente`,
      luego `mostrar` y `aprobar`). Si una respuesta modelo está mal, se corrige en su archivo
      antes de aprobarla.
  - [ ] Física 11° (337) · [ ] Física 9° (278) · [ ] Física 10° (250)
  - [ ] Matemáticas 10° (29) · [ ] 8° (21) · [ ] 9° (16) · [ ] 11° (12) · [ ] 5° (4) · [ ] 6° (1)
- [ ] **Revisar las 563 correcciones** (`listar --grado N --con-notas`). Cada una dice qué
      estaba mal en el recurso y cómo quedó. Se acepta, o se cambia el ejercicio. (El comando
      muestra 589: incluye las 26 preguntas del Icfes, cuya nota solo dice que son textuales.)
- [ ] **Datos que eligió un agente**, sin respaldo en el recurso. Confirmarlos o cambiarlos:
  - [ ] Física 11°: campo final de 2·10⁻⁴ T (magnetismo, Desarrolla 4); 20 m/s (ondas, Problemas
        18); «1.000 kg» leído como 1 kg; cargas en µC (Problemas 3, 4, 8, 9, 10); fase π/4
        (oscilaciones, Problemas 15); tercer armónico como n = 3 (acústica, Problemas 21).
  - [ ] Física 10°: ecuación de cinemática Cap. 3 Problemas 5–6 (reconstruida de Giancoli);
        exponentes de movimiento circular 17–18; área 2,5·10⁻⁴ m² (fluidos 7); 1000 kg (energía 6b).
        Datos irreales conservados: rueda de Chicago a 0,6 rev/s, persona sobre 16 m², hélice a
        20 000 rpm.
  - [ ] Física 9°: masa del clavo (5 g), distancia Tierra–Luna, densidad del oro, 340 m/s.
  - [ ] Álgebra 8° y 9°: valor de a en Multiplicación 4; $225 000 (9° T1 ICFES 1); segunda
        trayectoria de 9° T5 Practica 14; enunciado de Producto 13; cheque de $3 000 000.
  - [ ] Geometría 5° y 6°: escala 1:10 del carro, escala 0,5 cm = 1 km, bandeja de 40 cm de
        lado, pistas en metros.
  - [ ] Cálculo 11°: los 63 m del ICFES 4a (`saber11-desigualdades-011`) y las opciones
        cambiadas del 3a (`-007`).
- [ ] **Selección múltiple con más de una respuesta defendible.** Fijar la clave o reescribir:
  - [ ] Física 11°: ondas Desarrolla 3 (a y b); óptica Actividades 12 (b, c, d); óptica Actividades 2
        (a o d); acústica Actividades 10.
  - [ ] Física 10°: movimiento circular Desarrolla 13 (Ptolomeo o Aristóteles).
  - [ ] Álgebra 9°: ICFES Al-Juarismi pregunta 2; sueldo del vendedor (falta la comisión);
        sistemas 17 (discos, 4 o 5).
- [ ] **Posibles erratas que quedaron como se imprimieron** (el agente no se atrevió a cambiarlas):
  - [ ] Álgebra 8°: literales con respuesta «no se puede factorizar» (Trinomios 5h, 5p, 5v, 2o;
        Binomios 5a, 6g, 3f; Combinación 2e, 2h, 2i; Factorización 3e, 5q; Sustracción 9d).
  - [ ] Álgebra 9°: T4 2f (sin solución) y T4 ICFES 4 (bis) c (infinitas soluciones).
  - [ ] Cálculo 11°: `inecuaciones-simultaneas-010` (conjunto vacío) y
        `inecuaciones-cuadraticas-015` (raíces irracionales).
  - [ ] Trigonometría 10°: T2-14b «(18/13π)°»; resumen 6b «cos 1312» (¿radianes o grados?).
  - [ ] Geometría 8°: Pitágoras 2n (¿√225 o √255?); triángulos 1c (verdadera o falsa).
  - [ ] Física 11°: óptica Problema 11, dos pares de literales iguales.

## 3. Fidelidad al recurso (el enunciado se copió bien)

- [ ] **Muestra de Álgebra 8° transcrita de imágenes.** En los temas 3 y 4 del módulo de 8° las
      fórmulas son imágenes y el agente las leyó del `.docx`. Comparar estas 30 con el módulo
      impreso (`mostrar <id>`); si hay más de 1 error, revisar todo el archivo:
  - factorizacion-8: 027, 049, 098, 107, 120, 171, 187, 191, 193, 203, 216, 319, 402, 405, 412, 417
  - productos-notables-8: 015, 035, 037, 042, 104, 126, 127, 128
  - cocientes-notables-8: 006, 008, 017, 020, 024, 028
- [ ] **Temas 1 y 2 del módulo de 8°.** El agente no abrió el `.docx`, así que pueden faltar
      literales cuyas fórmulas se perdieron. Contrastar el número de literales de cada sección
      con el módulo impreso.
- [ ] **Recuperar lo omitido por ilegible.** División de polinomios 1–10 (8°, solo existe
      `division-polinomios-8-001`); Productos 8i; Factores comunes 4h, 9o, 9v, 9z; Binomios 6l;
      Producto 5, 6, 7d; 9° T3 actividad 2i y T3 ICFES 1c.
- [ ] **Preguntas del Icfes.** Comparar 5 al azar de `icfes-cuadernillo-2026.py` y de
      `-geometria.py` con el PDF: deben ser textuales (sus condiciones de uso no permiten
      modificarlas). Posibles erratas del Icfes, sin corregir: preguntas 15, 17 y 50.
- [ ] **Preguntas con figura, fuera del banco.** Decidir si se usan imprimiendo la página del
      recurso: Icfes 43 (clave B), 42 (D), 18 (C), 24 (D) y 29 (C); módulo 11° problema 2
      (lámparas); los ítems con figura que listó cada agente (ver «Informe» en la cabecera de
      cada archivo).

## 4. Comprobaciones técnicas

- [ ] **Todo el banco otra vez desde cero:** `python3 tools/ejercicios.py verificar --todos`
      debe dar 0 fallas. Las funciones de ayuda de `tools/ejercicios.py` cambiaron durante el
      trabajo, y las entradas que ya estaban verificadas no se vuelven a correr solas.
- [ ] **Que el LaTeX compile.** Ningún enunciado del banco se ha compilado todavía. Generar un
      catálogo por archivo con la plantilla y `mmcantillo.sty` (`\num`, `opciones`, `\sen`,
      `\mathbb`, `\cancel`, `\overleftrightarrow`) y revisar el PDF.
- [ ] **Revisión independiente de las comprobaciones.** Que otro agente o sesión lea una muestra
      de comprobaciones por archivo (unas 5 por archivo) y confirme que calculan la respuesta
      desde los datos y no la repiten.
- [ ] **Mejoras de redacción del conversor.** Hay 305 marcas `<!-- alt: … -->` en las copias
      `markdown/`, y 6 fórmulas no se pudieron leer (módulos de 7°, 8° y 10°). Revisarlas cuando
      se usen esos recursos.

## Criterio de cierre (confianza total)

- [ ] Todas las casillas anteriores marcadas.
- [ ] `python3 tools/ejercicios.py listar --estado manual-pendiente` no muestra nada.
- [ ] `python3 tools/ejercicios.py verificar --todos` da 0 fallas.
- [ ] El catálogo del banco compila sin errores y la docente lo revisó.
- [ ] Ninguna entrada queda sin `dba`, o las que quedan están decididas en la sección 1.

---

## Anexo: estado por archivo (2026-09-13)

| Archivo | Grado | Verif. | Abiertas | Con correcciones | Sin DBA |
|---|---|---|---|---|---|
| `matematicas/perimetro-area-5.py` | 5° | 4 | 0 | 3 | 0 |
| `matematicas/plano-cartesiano-5.py` | 5° | 13 | 1 | 3 | 0 |
| `matematicas/semejanza-escala-5.py` | 5° | 16 | 3 | 8 | 0 |
| `matematicas/angulos-6.py` | 6° | 3 | 0 | 1 | 0 |
| `matematicas/area-volumen-6.py` | 6° | 16 | 1 | 15 | 0 |
| `matematicas/triangulos-6.py` | 6° | 22 | 0 | 7 | 0 |
| `matematicas/perimetro-area-7.py` | 7° | 10 | 0 | 2 | 0 |
| `matematicas/angulos-8.py` | 8° | 0 | 17 | 1 | 0 |
| `matematicas/cocientes-notables-8.py` | 8° | 40 | 0 | 4 | 0 |
| `matematicas/division-polinomios-8.py` | 8° | 0 | 1 | 0 | 0 |
| `matematicas/expresiones-algebraicas-8.py` | 8° | 176 | 0 | 22 | 0 |
| `matematicas/factorizacion-8.py` | 8° | 419 | 1 | 37 | 0 |
| `matematicas/irracionales-8.py` (2026-09-14, guía Álgebra 8° P-I) | 8° | 22 | 4 | 0 | 0 |
| `matematicas/logaritmos-8.py` | 8° | 18 | 0 | 0 | 0 |
| `matematicas/medidas-con-radicales-8.py` | 8° | 6 | 0 | 2 | 0 |
| `matematicas/multiplicacion-algebraica-8.py` | 8° | 176 | 0 | 10 | 0 |
| `matematicas/nomenclatura-algebraica-8.py` | 8° | 13 | 0 | 3 | 0 |
| `matematicas/notacion-cientifica-8.py` | 8° | 14 | 0 | 1 | 0 |
| `matematicas/numeros-reales-8.py` | 8° | 48 | 0 | 6 | 0 |
| `matematicas/pitagoras-8.py` | 8° | 45 | 0 | 20 | 0 |
| `matematicas/potenciacion-8.py` | 8° | 30 | 0 | 0 | 0 |
| `matematicas/producto-polinomios-8.py` | 8° | 124 | 1 | 43 | 0 |
| `matematicas/productos-notables-8.py` | 8° | 130 | 1 | 15 | 0 |
| `matematicas/radicacion-8.py` | 8° | 47 | 0 | 3 | 0 |
| `matematicas/signos-agrupacion-8.py` | 8° | 18 | 0 | 12 | 0 |
| `matematicas/suma-resta-polinomios-8.py` | 8° | 113 | 0 | 5 | 0 |
| `matematicas/triangulos-8.py` | 8° | 23 | 0 | 4 | 0 |
| `fisica/luz-9.py` | 9° | 14 | 60 | 3 | 68 |
| `fisica/ondas-9.py` | 9° | 23 | 70 | 6 | 93 |
| `fisica/ondas-luminosas-9.py` | 9° | 6 | 44 | 1 | 50 |
| `fisica/optica-9.py` | 9° | 8 | 39 | 4 | 46 |
| `fisica/sonido-9.py` | 9° | 22 | 65 | 5 | 83 |
| `fisica/termodinamica-9.py` | 9° | 40 | 0 | 11 | 40 |
| `matematicas/determinantes-9.py` | 9° | 25 | 5 | 6 | 0 |
| `matematicas/funcion-cuadratica-9.py` | 9° | 22 | 0 | 2 | 0 |
| `matematicas/funcion-lineal-9.py` | 9° | 113 | 4 | 5 | 0 |
| `matematicas/pitagoras-9.py` | 9° | 6 | 0 | 1 | 0 |
| `matematicas/sistemas-3x3-9.py` | 9° | 26 | 7 | 7 | 0 |
| `matematicas/sistemas-ecuaciones-9.py` | 9° | 49 | 0 | 2 | 0 |
| `fisica/cinematica-10.py` | 10° | 51 | 28 | 12 | 0 |
| `fisica/cinematica-2d-10.py` | 10° | 22 | 28 | 5 | 0 |
| `fisica/energia-10.py` | 10° | 43 | 33 | 16 | 0 |
| `fisica/fluidos-10.py` | 10° | 14 | 42 | 6 | 56 |
| `fisica/leyes-newton-10.py` | 10° | 32 | 35 | 2 | 0 |
| `fisica/mediciones-10.py` | 10° | 76 | 17 | 12 | 93 |
| `fisica/movimiento-circular-10.py` | 10° | 51 | 29 | 15 | 0 |
| `fisica/termodinamica-10.py` | 10° | 24 | 38 | 6 | 62 |
| `matematicas/angulos-radianes-10.py` | 10° | 71 | 0 | 10 | 0 |
| `matematicas/circulo-unitario-10.py` | 10° | 92 | 3 | 4 | 0 |
| `matematicas/graficas-trigonometricas-10.py` | 10° | 33 | 21 | 10 | 0 |
| `matematicas/otras-funciones-trigonometricas-10.py` | 10° | 81 | 5 | 11 | 0 |
| `matematicas/razones-trigonometricas-10.py` | 10° | 60 | 0 | 7 | 0 |
| `matematicas/rectas-inclinacion-10.py` | 10° | 7 | 0 | 0 | 0 |
| `matematicas/valores-trigonometricos-10.py` | 10° | 78 | 0 | 5 | 0 |
| `fisica/acustica-11.py` | 11° | 36 | 53 | 22 | 0 |
| `fisica/circuitos-11.py` | 11° | 16 | 35 | 10 | 0 |
| `fisica/electrostatica-11.py` | 11° | 20 | 44 | 13 | 0 |
| `fisica/magnetismo-11.py` | 11° | 8 | 35 | 6 | 0 |
| `fisica/ondas-11.py` | 11° | 36 | 58 | 26 | 0 |
| `fisica/optica-11.py` | 11° | 31 | 57 | 24 | 0 |
| `fisica/oscilaciones-11.py` | 11° | 51 | 55 | 32 | 0 |
| `matematicas/desigualdades.py` | 11° | 8 | 3 | 0 | 0 |
| `matematicas/icfes-cuadernillo-2026-geometria.py` | 11° | 11 | 0 | 0 | 3 |
| `matematicas/icfes-cuadernillo-2026.py` | 11° | 15 | 0 | 0 | 0 |
| `matematicas/inecuaciones-cuadraticas.py` | 11° | 27 | 1 | 2 | 0 |
| `matematicas/inecuaciones-lineales.py` | 11° | 43 | 0 | 2 | 0 |
| `matematicas/inecuaciones-racionales.py` | 11° | 20 | 0 | 2 | 0 |
| `matematicas/inecuaciones-simultaneas.py` | 11° | 20 | 0 | 1 | 0 |
| `matematicas/inecuaciones.py` | 11° | 5 | 1 | 0 | 0 |
| `matematicas/intervalos.py` | 11° | 25 | 1 | 6 | 0 |
| `matematicas/medicion-11.py` | 11° | 11 | 1 | 7 | 0 |
| `matematicas/saber11-desigualdades.py` | 11° | 13 | 0 | 8 | 0 |
| `matematicas/valor-absoluto.py` | 11° | 31 | 5 | 1 | 0 |
