# Funcionalidad implementada — Fase `B-EP-006-HU-003-la-busqueda-dice-donde-esta` (módulo Memoria)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-006-HU-003-la-busqueda-dice-donde-esta` |
| **Módulo** | Memoria |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), escrito el 2026-08-17 y aprobado el 2026-08-30 |
| **HU / CA cubiertas** | [HU-003](../HU-003-busqueda-por-palabra.md): el CA-01, el resultado alcanza para abrir lo que se encontró |
| **Fecha de cierre** | 2026-08-30 |
| **Versión del estándar al cerrar** | `36.0.2` — **sin cambio**: no se toca `base/` ni `plantillas/` |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |
| **Reemplaza el veredicto de** | `A-EP-006-HU-003-retrodocumentar-la-busqueda-por-palabra` |

> **Por qué se declara el reemplazo:** el defecto que dejó aquella fase en rojo está arreglado y su prueba corre. **El veredicto de aquella fase no se toca** (`20·M11`).

---

## 1. Qué se implementó — resumen

**Dos defectos, y el segundo no se veía.**

El primero es el que la historia pedía: la búsqueda encontraba y **no decía dónde está lo que encontró**, así que el resultado no alcanzaba para abrirlo. Ahora la consulta trae también ese dato y lo imprime **debajo** de cada resultado, en su propia línea: una línea de más por resultado se lee, una columna más en la misma línea no.

El segundo lo destapó la fase `A` al probarlo de una forma que vale la pena copiar: el camino «(sin señales relevantes)» **retornaba sin cerrar la conexión**, y eso no se deduce leyendo. La prueba borra el archivo después de buscar, porque en Windows no se puede borrar lo que está tomado. El descuido se ve en vez de suponerse.

| Antes | Ahora |
|---|---|
| La búsqueda encuentra y no dice dónde | Imprime la ubicación debajo de cada resultado |
| El camino sin resultados deja la conexión tomada | La cierra antes de salir |

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem | Categoría | Ubicación | Estado |
|---|---|---|---|
| CA-01, el resultado alcanza para abrir lo que se encontró | servicio | `memoria/` | ✅ |

### 2.2 Plan de trabajo → ejecución

| Tarea | Evidencia |
|---|---|
| T-01 · traer la ubicación en la consulta | CP-001 |
| T-02 · imprimirla debajo, y solo si la hay | CP-001 |
| T-03 · cerrar la conexión en el camino sin resultados | CP-005 |
| T-04 · destapar las dos pruebas | 59 en verde |

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
| La ubicación va en su propia línea | Una columna más en la misma línea deja el renglón ilegible cuando la ruta es larga |
| Solo se imprime si la señal la tiene | Una línea vacía por resultado es ruido |
| La conexión se cierra en el camino que retorna temprano | Es el único que se escapaba, y en Windows deja el archivo bloqueado |

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
