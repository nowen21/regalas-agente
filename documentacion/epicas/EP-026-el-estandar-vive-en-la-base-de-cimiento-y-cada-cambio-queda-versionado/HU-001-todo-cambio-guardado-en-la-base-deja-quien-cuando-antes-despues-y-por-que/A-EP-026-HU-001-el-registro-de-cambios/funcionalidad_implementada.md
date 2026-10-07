# Funcionalidad implementada · Fase `A-EP-026-HU-001-el-registro-de-cambios` (módulo Historia de Cimiento)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-026-HU-001-el-registro-de-cambios` |
| **Módulo** | Historia de Cimiento, `proyectos/cimiento/core/historia/` |
| **Especificación del módulo** | Los CA de la [HU-001](../HU-001-todo-cambio-guardado-en-la-base-deja-quien-cuando-antes-despues-y-por-que.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-001 () |
| **Fecha de cierre** | 2026-10-06 |
| **Versión del estándar al cerrar** | 56.1.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Toda tabla de Cimiento deja su historia: crear, cambiar y borrar, con quién, cuándo, la fila, antes y después de lo que cambió y el motivo. Cubre cuentas y grupos y el estado del análisis que escriben los enganches. La pantalla «Historia» filtra por tabla y acción, y el grupo administrador deshace un cambio, lo que suma otro.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|


**Faltantes / diferimientos:** ninguno

### 2.2 Plan de trabajo → ejecución

Las 5 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Menú → «Historia» (`/historia/`). Desde código, `core.historia.registro.quien_y_por_que(cuenta, motivo=…)` pone quién y por qué de lo que se guarde adentro.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La historia se llena con señales de Django y deja fuera el gasto | Una tabla nueva queda cubierta sola; el gasto ya es su propia historia y duplicarlo pesaría miles de filas al día | S-331 |

## 6. Deuda técnica y pendientes generados

`CambioDeNivel` sigue al lado de la historia nueva, que también registra los niveles; se puede retirar cuando la pantalla de niveles lea la historia.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Aplicar la migración `historia 0001` con `manage.py migrate` (hecho en esta máquina el 2026-10-06).
