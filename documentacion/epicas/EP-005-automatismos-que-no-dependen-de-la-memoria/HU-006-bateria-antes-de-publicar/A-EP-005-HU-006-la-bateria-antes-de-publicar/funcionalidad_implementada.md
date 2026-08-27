# Funcionalidad implementada — Fase `A-EP-005-HU-006-la-bateria-antes-de-publicar` (módulo Automatismos)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-006-la-bateria-antes-de-publicar` |
| **Módulo** | Automatismos que no dependen de la memoria |
| **Especificación del módulo** | La propia [HU-006](../HU-006-bateria-antes-de-publicar.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | [HU-006](../HU-006-bateria-antes-de-publicar.md): `CA-01` y `CA-02`. Los dos |
| **Fecha de cierre** | 2026-08-26 |
| **Versión del estándar al cerrar** | `35.1.0` |
| **Commit** | `b19ca91` |

> **Se ejecutó el 2026-08-22 y se cierra el 2026-08-26.** Entre las dos fechas no se tocó nada de esta fase: faltaba este documento.

---

## 1. Qué se implementó — resumen

**Antes de publicar corre una batería de comprobaciones, y no depende de que nadie se acuerde.** La escribe el instalador como enganche de `pre-push`.

**Y lo que detiene está separado de lo que informa**, con su motivo: un incumplimiento claro para el trabajo; lo demás avisa y deja pasar.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem de la historia | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| `CA-01` antes de publicar corre todo | automatismo | El enganche de `pre-push` que escribe [instalar.py](../../../../../validadores/instalar.py) | ✅ | Leído, con lo que corre |
| `CA-02` un incumplimiento claro detiene | automatismo | El reparto entre lo que detiene y lo que informa | ✅ | Su motivo escrito, y **un caso vivo ese mismo día** |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado |
|---|---|
| Las del plan | ✅ hechas |

**Lo que no se hizo:** cerrar la trazabilidad, que es este documento. **La fase quedó cuatro días en la estación 11.**

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Qué | Resultado |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, los dos criterios |
| **Defectos abiertos que se aceptaron** | `D-01` (media) y `D-02` (baja). Los dos siguen abiertos. Ver §6 |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

No se usa: **corre solo**, al publicar. El enganche lo escribe el instalador en `.githooks/`, y `core.hooksPath` lo apunta.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué |
|---|---|
| Lo que detiene y lo que informa están **separados, con su motivo** | Una batería que detiene por todo se desactiva en una tarde. La que no detiene por nada no sirve |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Severidad | Estado al cerrar |
|---|---|---|
| **`D-01` · La batería corre `estandar` y `versionado`, y no corre las pruebas de los validadores.** Un cambio que rompa una prueba se publica igual mientras no rompa enlaces ni versión | Media | **Abierta** |
| **`D-02` · El enganche vive en la máquina, no viaja con el repositorio.** Un clon nuevo no lo tiene hasta que corra el instalador, y eso no se avisa en ninguna parte | Baja | **Abierta** |

**`D-01` se sintió en esta misma jornada.** El 2026-08-26 la suite completa destapó tres defectos que ninguna otra comprobación vio: una comprobación descolgada de su corrida, un guion que reportaba en verde sin correr nada, y una que reportaba fuera de su tema. **Ninguno de los tres habría detenido una publicación**, porque la batería no corre las pruebas.

**Y `D-02` es exactamente lo que se volvió a encontrar el 2026-08-26**, por otro camino: al construir la [`EP-007 · HU-009`](../../../EP-007-instalacion-y-actualizacion/HU-009-las-rutas-largas-no-detienen-el-guardado/HU-009-las-rutas-largas-no-detienen-el-guardado.md) se comprobó clonando que **la configuración de git no viaja**, y por eso el instalador solo alcanza a la copia donde corre.

**Estaba escrito acá desde el 2026-08-22 y se volvió a descubrir cuatro días después.** Es el costo exacto de dejar una fase sin cerrar: **la deuda existía, estaba bien redactada, y no la leyó nadie** — porque vivía en un documento que el inventario contaba como trabajo a medias.

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] La historia [HU-006](../HU-006-bateria-antes-de-publicar.md): su §8 nombra esta fase.
- [x] El inventario de historias, que **ya no se mantiene a mano** desde la `35.0.0`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** ninguna.
- **Qué cambia para quien ya tenía el estándar:** nada. El enganche ya lo escribía el instalador.
- **Reversión:** no aplica. La fase comprobó; no cambió el producto.
