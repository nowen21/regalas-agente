# Funcionalidad implementada · Fase `A-EP-025-HU-010-segunda-tanda` (módulo `proyectos/cimiento/core/consumo/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-010-segunda-tanda` |
| **Módulo** | `proyectos/cimiento/core/consumo/`, `proyectos/cimiento/core/herramientas/recuperar.py` |
| **Especificación del módulo** | Los CA de la [HU-010](../HU-010-el-gasto-se-ve-por-los-demas-niveles.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-010 (CA-01 a CA-03) |
| **Fecha de cierre** | 2026-10-05 |
| **Versión del estándar al cerrar** | 54.2.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

El gasto queda también por mensaje del usuario, con su palabra clave y el trabajo que tocó su turno; por herramienta; por agente auxiliar, cuyos registros ahora se leen; por modelo y por tipo de token. «Gasto» suma esas secciones, lo que llena el contexto y los últimos mensajes.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Programa | `proyectos/cimiento/core/consumo/lector.py`, `proyectos/cimiento/core/consumo/trabajo.py`, `proyectos/cimiento/core/herramientas/recuperar.py`, `proyectos/cimiento/core/consumo/models.py`, `proyectos/cimiento/core/consumo/migrations/0003_segunda_tanda.py`, `proyectos/cimiento/core/consumo/guardar.py` | ✅ | CP-001 |
| CA-02 | Programa | `proyectos/cimiento/core/consumo/lector.py`, `proyectos/cimiento/core/consumo/guardar.py`, `proyectos/cimiento/core/consumo/telemetria.py`, `proyectos/cimiento/core/consumo/views.py` | ✅ | CP-002 |
| CA-03 | Programa | `proyectos/cimiento/core/consumo/tablero.py`, `proyectos/cimiento/core/consumo/templates/consumo/_datos.html` | ✅ | CP-003 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 6 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): `proyectos/cimiento/core/consumo/tests.py` se declaró durante la fase, al ver que su prueba de la HU-006 pedía lo contrario de esta HU; `proyectos/cimiento/core/consumo/views.py` también, al ver que la vista de la telemetría tenía que pasar las herramientas al guardado.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

«Gasto» en el menú, con los mismos filtros de la HU-008.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El trabajo sale de las rutas tocadas en el turno | El aviso de acuerdos nombra fases de otras sesiones | No hace falta: está en `trabajo.py` |
| El avance de lectura guarda el mensaje en curso | Un turno puede quedar partido entre dos lecturas | No hace falta: está en `guardar.py` |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

No aplica.

## 8. Despliegue, si aplica  ·  `13·DOC4`

`preparar_base` aplica la migración `0003`. Para llenar lo ya guardado: borrar el avance de lectura y correr `leer_consumo`.
