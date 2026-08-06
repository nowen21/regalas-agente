# Hecho · Memoria semántica

Origen: pendiente 05. La memoria ya se busca **por significado**, no solo por palabra — híbrida con FTS5, local y opcional.

Cerrado el 2026-08-06.

---

## La decisión que estaba abierta

**Qué modelo genera los embeddings y si corre local.** Resuelto:

- **Opt-in, no por defecto.** `search` sigue siendo léxico (FTS5) sin instalar nada; si están los extras (`memoria/requirements-semantica.txt`), pasa a **híbrida**. Así el invariante "sin instalación" se mantiene para todos.
- **Modelo local, nunca API hosted.** `model2vec` (`potion-base-8M`, ~30 MB, estático, sin `torch`) genera los embeddings **en la máquina** — el contenido de las señales no sale (`00·N6`). Una API de embeddings externa se descartó por privacidad, no solo por el modo offline.
- **Almacén: brute-force numpy**, no `sqlite-vec`. A esta escala (cientos-miles de señales) el coseno en memoria es instantáneo, sigue siendo un solo archivo y **evita cargar extensiones nativas** (frágil en Windows). `sqlite-vec` recién valdría a 10k+ señales.

## Qué se hizo

- **`memoria/semantica.py`** — `disponible()` (degrada solo si faltan deps), `indexar()` (embebe solo lo nuevo/cambiado, por hash del texto; no carga el modelo si no hay nada), `buscar()` y `ranking()` (coseno puro). Vectores en `senales.db` (tabla `senales_vec`, blobs).
- **`memoria.py`** — `search` **híbrida** (léxica ∪ semántica fusionadas por rango recíproco, `_rrf`); `--lexica` fuerza solo palabras; comando `indexar`. Fallback y aviso si no está instalado.
- **`requirements-semantica.txt`** con el modelo + numpy.
- **Pruebas:** `ranking`, `_rrf`, `disponible` (16 verdes en memoria). Base real indexada (198 señales): una consulta por significado que la léxica devuelve vacía, la híbrida la resuelve.

## Lo que hereda del 02: contradicciones

Con embeddings ya es viable **detectar contradicciones** (dos señales activas del mismo scope semánticamente opuestas). No se implementó aún: es el siguiente paso natural sobre esta base (comparar por similitud alta + señal de oposición). Queda anotado como mejora, no como pendiente aparte.

## Nota de calidad

El modelo estático 8M da separación semántica **modesta**; para la escala actual, combinado con la léxica, alcanza. Si hiciera falta más precisión, el upgrade es cambiar `MEMORIA_MODELO` a `potion-base-32M` (misma interfaz), sin tocar código.
