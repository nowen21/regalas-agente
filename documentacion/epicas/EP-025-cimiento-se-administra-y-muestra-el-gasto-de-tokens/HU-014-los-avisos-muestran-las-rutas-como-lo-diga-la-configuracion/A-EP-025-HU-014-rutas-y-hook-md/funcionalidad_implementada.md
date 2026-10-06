# Funcionalidad implementada · Fase `A-EP-025-HU-014-rutas-y-hook-md` (módulo `proyectos/cimiento/core/enganches/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-014-rutas-y-hook-md` |
| **Módulo** | `proyectos/cimiento/core/enganches/` |
| **Especificación del módulo** | Los CA de la [HU-014](../HU-014-los-avisos-muestran-las-rutas-como-lo-diga-la-configuracion.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-014 (CA-01 a CA-02) |
| **Fecha de cierre** | 2026-10-05 |
| **Versión del estándar al cerrar** | 55.0.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

`Proyecto.mostrar` da las rutas relativas o completas según «Rutas en los avisos» del proyecto, leído una vez por proceso; sin registro vale el de fábrica. `hook_resumen.py`, `hook_sesion.py` y `hook_veredicto.py` muestran sus rutas con él. La lógica de `hook_md.py` pasó a `core/enganches/md.py`, con lo de `core/`; el adaptador solo lee la entrada y llama.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Programa | `proyectos/cimiento/core/comun/proyecto.py`, `proyectos/cimiento/core/enganches/configuracion.py`, `adaptadores/claude-code/hook_resumen.py`, `adaptadores/claude-code/hook_sesion.py`, `adaptadores/claude-code/hook_veredicto.py` | ✅ | CP-001 |
| CA-02 | Programa | `proyectos/cimiento/core/enganches/md.py`, `adaptadores/claude-code/hook_md.py` | ✅ | CP-002 |

**Faltantes / diferimientos:** retirar `validadores/comun.py`, `enlaces.py`, `marcas.py` y `sesiones.py` espera a que `evals/correr.py` deje de usarlos.

### 2.2 Plan de trabajo → ejecución

Las 4 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): `tests_limites.py` se declaró durante la fase, al cambiar la consulta de la configuración.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

«Rutas en los avisos» en «Configuración» o en «Proyectos» → «Editar». Vale desde el siguiente aviso de un enganche nuevo, porque cada uno lo lee al arrancar.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Sin registro, todo de fábrica | La base es de los proyectos que Cimiento administra; una prueba no cambia según la máquina | No hace falta: está en `configuracion.py` |

## 6. Deuda técnica y pendientes generados

Los cuatro módulos viejos de `validadores/` que sigue usando `evals/correr.py`.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

No aplica.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica.
