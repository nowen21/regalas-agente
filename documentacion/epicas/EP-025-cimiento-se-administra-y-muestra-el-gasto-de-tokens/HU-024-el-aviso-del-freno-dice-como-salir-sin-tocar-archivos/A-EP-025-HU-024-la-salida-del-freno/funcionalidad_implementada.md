# Funcionalidad implementada · Fase `A-EP-025-HU-024-la-salida-del-freno` (módulo `proyectos/cimiento/core/enganches/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-024-la-salida-del-freno` |
| **Módulo** | `proyectos/cimiento/core/enganches/` |
| **Especificación del módulo** | Los CA de la [HU-024](../HU-024-el-aviso-del-freno-dice-como-salir-sin-tocar-archivos.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-024 (CA-01 a CA-03) |
| **Fecha de cierre** | 2026-10-05 |
| **Versión del estándar al cerrar** | 55.0.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Cuando el freno detiene, su aviso dice cómo salir sin tocar archivos: la contraria de la herramienta que creó lo que estorba, o pedirle al usuario la suspensión de la regla en Cimiento, con la dirección de la pantalla; la del núcleo no se suspende. El freno lee el análisis prendido de su propia sesión (H-8) y resuelve las rutas de cada parte de una orden después de su `cd`.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Programa | `proyectos/cimiento/core/enganches/freno.py`, `adaptadores/claude-code/hook_antes.py` | ✅ | CP-001 |
| CA-02 | Programa | `proyectos/cimiento/core/enganches/freno.py`, `adaptadores/claude-code/hook_antes.py`, `adaptadores/claude-code/hook_despues.py` | ✅ | CP-002 |
| CA-03 | Programa | `proyectos/cimiento/core/enganches/freno.py` | ✅ | CP-003 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 4 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

No hay que hacer nada: el aviso llega solo cuando el freno detiene.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Solo se parte la orden cuando trae un `cd` | Partir antes podría cortar un texto entre comillas con `;` | No hace falta: está en `freno.py` |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

No aplica.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica.
