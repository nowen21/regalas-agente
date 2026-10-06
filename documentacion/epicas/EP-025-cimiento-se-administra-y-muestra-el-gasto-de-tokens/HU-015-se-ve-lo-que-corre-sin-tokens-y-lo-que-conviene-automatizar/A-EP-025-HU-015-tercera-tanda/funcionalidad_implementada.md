# Funcionalidad implementada · Fase `A-EP-025-HU-015-tercera-tanda` (módulo `proyectos/cimiento/core/consumo/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-015-tercera-tanda` |
| **Módulo** | `proyectos/cimiento/core/consumo/` |
| **Especificación del módulo** | Los CA de la [HU-015](../HU-015-se-ve-lo-que-corre-sin-tokens-y-lo-que-conviene-automatizar.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-015 (CA-01 a CA-02) |
| **Fecha de cierre** | 2026-10-05 |
| **Versión del estándar al cerrar** | 55.0.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

El lector guarda cada corrida de un enganche, le entregue o no algo al modelo, y de cada comando solo el programa y su orden. «Gasto» suma «Lo que corre sin tokens» (cada enganche con sus corridas y los tokens que agregó) y «Candidatos a automatizar» (archivos leídos tres veces o más, enganches en casi cada mensaje y comandos repetidos, con lo que se ahorraría).

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Programa | `proyectos/cimiento/core/consumo/lector.py`, `proyectos/cimiento/core/consumo/models.py`, `proyectos/cimiento/core/consumo/migrations/0004_tercera_tanda.py`, `proyectos/cimiento/core/consumo/guardar.py`, `proyectos/cimiento/core/consumo/tablero.py`, `proyectos/cimiento/core/consumo/templates/consumo/_datos.html` | ✅ | CP-001 |
| CA-02 | Programa | `proyectos/cimiento/core/consumo/lector.py`, `proyectos/cimiento/core/consumo/guardar.py`, `proyectos/cimiento/core/consumo/tablero.py`, `proyectos/cimiento/core/consumo/templates/consumo/_datos.html` | ✅ | CP-002 |

**Faltantes / diferimientos:** los pedidos de una misma palabra que siguen los mismos pasos, como dice el acuerdo, para cuando haya más datos.

### 2.2 Plan de trabajo → ejecución

Las 5 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): `vigilante.py` y `tests_vigilante.py` se declararon durante la fase, al ver que el vigilante se caía con un error de un archivo.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

«Gasto» en el menú: las dos secciones van al final, con el mismo filtro de proyecto y período.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Las corridas van en una tabla propia | Sumadas a la del gasto, las que entregan JSON contarían dos veces | No hace falta: está en el modelo |
| Lo entre comillas no es orden | Puede ser texto o datos | No hace falta: está en `lector.py` |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

No aplica.

## 8. Despliegue, si aplica  ·  `13·DOC4`

`preparar_base` aplica la `0004` de consumo; después hay que reiniciar el vigilante (`vigilar_consumo --parar` y la instalación lo arranca otra vez).
