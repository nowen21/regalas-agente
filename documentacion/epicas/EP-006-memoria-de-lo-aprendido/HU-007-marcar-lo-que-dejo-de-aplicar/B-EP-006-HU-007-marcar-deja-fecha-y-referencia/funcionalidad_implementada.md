# Funcionalidad implementada — Fase `B-EP-006-HU-007-marcar-deja-fecha-y-referencia` (módulo Memoria)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-006-HU-007-marcar-deja-fecha-y-referencia` |
| **Módulo** | Memoria |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), escrito el 2026-08-17 y aprobado el 2026-08-30 |
| **HU / CA cubiertas** | [HU-007](../HU-007-marcar-lo-que-dejo-de-aplicar.md): el CA-01, la marcada queda con la fecha y con qué la reemplazó |
| **Fecha de cierre** | 2026-08-30 |
| **Versión del estándar al cerrar** | `36.0.2` — **sin cambio**: no se toca `base/` ni `plantillas/` |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |
| **Reemplaza el veredicto de** | `A-EP-006-HU-007-retrodocumentar-la-marca-de-lo-que-dejo-de-aplicar` |

> **Por qué se declara el reemplazo:** el defecto que dejó aquella fase en rojo está arreglado y su prueba corre. **El veredicto de aquella fase no se toca** (`20·M11`).

---

## 1. Qué se implementó — resumen

**Lo que decía la consola se perdía al cerrarla.**

Marcar una señal como reemplazada imprimía «S-001 marcada reemplazada por S-002» y **no guardaba ni por cuál ni cuándo**. Archivar tampoco dejaba fecha. De una señal marcada no se sabía nada de lo que la marca prometía.

Se notó usándolo: esta misma sesión marcó una señal de terminología como reemplazada y tuvo que rodear el defecto escribiendo la nueva con el enlace puesto a mano.

**Y apareció un tercer defecto, en la propia prueba.** La que comprueba que la marca de vigencia no dependa del huso usaba 181 días como si fueran seis meses, cuando el contador va por meses de calendario: fallaba o pasaba según el mes en que se corriera. Ahora cuenta seis meses de calendario.

| Antes | Ahora |
|---|---|
| Marcar no guardaba por cuál ni cuándo | Guarda las dos cosas |
| Archivar no dejaba fecha | La deja |
| Una prueba pasaba o fallaba según el mes | Cuenta meses de calendario |

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem | Categoría | Ubicación | Estado |
|---|---|---|---|
| CA-01, la marcada queda con la fecha y con qué la reemplazó | servicio | `memoria/` | ✅ |

### 2.2 Plan de trabajo → ejecución

| Tarea | Evidencia |
|---|---|
| T-01 · marcar guarda por cuál y cuándo | CP-001 |
| T-02 · archivar deja fecha | CP-002 |
| T-03 · destapar las dos pruebas | 59 en verde |
| T-04 · arreglar la prueba que dependía del mes | CP-004 |

**Correspondencia:** 4 tareas, 4 con resultado.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, ciclo 1 |
| **Suites ejecutadas** | Las 59 pruebas de la memoria, 59 en verde |
| **Defectos abiertos** | Ninguno |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Sin punto de entrada nuevo.

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué |
|---|---|
| La fecha va en la columna que ya existía para el cierre | No hacía falta columna nueva: la que había estaba vacía |
| Marcar migra el esquema antes de escribir | Una base vieja no tiene esas columnas, y el comando no puede fallar por eso |
| La prueba del huso cuenta meses, no días | Contar días contra un contador de meses da un resultado que cambia con el calendario |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| Ninguna | — |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] El `Estado` de la historia y su tabla de fases.
- [ ] `VERSION` y `CHANGELOG.md`: **no aplica**.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Nada que desplegar.**
