# Funcionalidad implementada — Fase `A-EP-005-HU-019-el-enganche-de-git-pone-el-hash` (módulo Enganches)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-019-el-enganche-de-git-pone-el-hash` |
| **Módulo** | Enganches |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-27 |
| **HU / CA cubiertas** | [HU-019](../HU-019-el-hash-del-commit-se-anota-solo.md): `CA-01` a `CA-05`. Los cinco |
| **Fecha de cierre** | 2026-08-27 |
| **Versión del estándar al cerrar** | `35.6.0` |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | `6abffdc` |

---

## 1. Qué se implementó — resumen

**La casilla del commit se marca sola.** Antes había que volver al documento a escribirla, y casi nadie volvía: **el commit ocurre después de que el trabajo se dio por terminado**. Solo el 2026-08-27 se marcó a mano cinco veces.

**Y al medir apareció algo que cambió el alcance:** de los 140 documentos de estado, **106 no tienen la casilla siquiera**.

| | |
|---|---|
| Con la casilla marcada | 11 |
| Sin marcar | 23 |
| **Sin la casilla** | **106** |

**Tres de cada cuatro no tienen dónde.** No se les inventa: **se cuentan aparte y se nombran**.

**Y las 23 sin marcar eran dos cosas:** 22 están guardadas de hecho, y **una no**. Antes eso era «23 sin commitear», donde hay una.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem de la historia | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| `RN-01` el hash se escribe sin que nadie lo ponga | servicio | `estacion_commit.marcar_las_fases` | ✅ | CP-001 |
| `RN-02` solo donde hay dónde | servicio | `tiene_fila_de_estacion` | ✅ | CP-003, sabotaje 1 |
| `RN-03` no se pisa un hash puesto | servicio | `ya_esta_marcada` | ✅ | CP-002, sabotaje 2 |
| `RN-04` sin cierre en git no se marca | servicio | `cerrada_en_git` | ✅ | CP-005, sabotaje 3 |
| `RN-05` el conteo separa marca de trabajo | servicio | `estacion_del_commit_sin_marcar` en [fases.py](../../../../../validadores/fases.py) | ✅ | CP-004 |
| `RN-06` las sin fila se cuentan aparte | servicio | El tercer grupo | ✅ | CP-004 |
| `RN-07` un fallo no pierde el commit | adaptador | `hook_estacion.py` | ✅ | CP-005, sabotaje 4 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-00 · impacto sobre las pruebas del instalador | ✅ | Ninguna compara la lista |
| T-01 · **resolver la duda 1 midiendo** | ✅ | `S-067` |
| T-02 · encontrar la fase que el commit cierra | ✅ | CP-001 |
| T-03 · las tres condiciones para escribir | ✅ | CP-002, CP-003, CP-005 |
| T-04 · el enganche que nunca deshace un commit | ✅ | CP-005 |
| T-05 · que el instalador lo cuelgue | ✅ | CP-006, sabotaje 5 |
| T-06 · el conteo con sus tres grupos | ✅ | CP-004 |
| T-07 · los cinco CA | ✅ | 16 pruebas |
| T-08 · **correrlo commiteando** | ✅ | §3 del resultado |
| T-09 · `CHANGELOG` y `VERSION` | ✅ | `35.6.0` |
| T-10 · sabotear | ✅ | Cinco, en tres ciclos |

**Correspondencia:** 11 tareas, 11 con resultado. **Ninguna sin hacer.**

**Archivos tocados que el plan no declaraba** (`02·F8`): **uno**, `validadores/hook_estacion.py` — el plan nombraba `estacion_commit.py` y el enganche como una sola pieza, y se partieron en dos: **la lógica agnóstica y lo que habla con git**, que es como están los otros nueve enganches del repositorio. Se declara acá en vez de callarlo.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, en el ciclo 3 |
| **Suites ejecutadas + resultado** | `python validadores/pruebas.py`: **500 verdes** |
| **Defectos abiertos que se aceptaron** | Ninguno. `DEF-01` a `DEF-04` corregidos |

**Ninguno en la lógica.** El más grave —`DEF-03`— es que **ninguna prueba tocaba la red de seguridad del enganche**: la que existía rompía el guion de shell que lo llama, no el enganche. Es la **cuarta** vez en la jornada que una prueba no toca lo que dice tocar.

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

**No hay nada que correr.** Al commitear, si el commit incluye el cierre de una fase que tiene su casilla vacía, el enganche la marca y lo dice:

```
post-commit: anotado `f0c14bf` en la estación 12 de A-EP-…
             — queda sin guardar, y entra en el commit siguiente.
```

- **El conteo:** `python validadores/validar.py fases`, con sus tres grupos.
- **Desde el código:** `estacion_commit.marcar(texto, hash)` devuelve `None` si no hay que tocar nada — **sin cambio no puede haber escritura**.

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal |
|---|---|---|
| **El archivo queda sin guardar** | El hash no existe hasta que el commit está hecho. `--amend` **se muerde la cola** —cambia el hash— y un segundo commit automático **cruza `00·N1`** | `S-067` |
| Se escribe **solo donde hay fila** | Son 106 de 140. Inventar estructura en documentos viejos hace más daño que el problema | `S-066` |
| **No se pisa un hash puesto** | El hash dice qué commit cerró la fase; el último la haría apuntar a una corrección de una coma | `CP-002` |
| **Sin cierre en git no se marca** | Diría que se commiteó algo que no se commiteó | `CP-005` |
| `marcar` devuelve **`None`**, no el mismo texto | Para que quien llame **no pueda reescribir el archivo sin querer** | `CP-000` |
| La fase se reconoce **por la forma del nombre** | Una lista envejece; la forma sirve en cualquier proyecto que herede el estándar | `RN-01` |
| **Cualquier fallo termina en silencio y código 0** | Cuando esto corre el commit ya está hecho: lo único que logra un fallo es alarmar sin motivo | `CP-005` |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| **Las 22 fases con la marca pendiente** | **Abierta, y ahora nombrada.** Su cierre está en git: es la marca, no el trabajo |
| **Las 106 sin la fila** | **Abierta y contada aparte.** El enganche no las toca, y rellenarlas es otro trabajo |
| **El árbol queda sucio después de cada commit** | **Es el costo elegido**, declarado en `S-067`. Un archivo, una línea, que entra en el commit siguiente |
| Una fase **sin cierre escrito** y sin marcar | **Abierta.** `A-EP-004-HU-010`. Es la única que sí es trabajo |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] La épica [EP-005](../../epica.md): la `HU-019` en sus tablas.
- [x] El [README](../README.md) de la carpeta de la historia.
- [x] Las señales `S-066`, `S-067` y `S-068`.
- [x] `VERSION` en `35.6.0` y su entrada en el `CHANGELOG`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** ninguna.
- **Qué cambia para quien ya tenía el estándar:** al volver a instalar, el enganche queda colgado. **Sus documentos viejos no se tocan**, y el conteo le dirá cuántos de los suyos no tienen dónde marcar.
- **Reversión:** se descarta el commit, se baja `VERSION`, y se vuelve a correr el instalador.
