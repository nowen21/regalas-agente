# Funcionalidad implementada · Fase `A-EP-025-HU-007-recepcion-de-la-telemetria` (módulo `proyectos/cimiento/core/consumo/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-007-recepcion-de-la-telemetria` |
| **Módulo** | `proyectos/cimiento/core/consumo/`, `proyectos/cimiento/core/herramientas/` |
| **Especificación del módulo** | Los CA de la [HU-007](../HU-007-el-gasto-llega-a-cimiento-en-vivo.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-007 (CA-01 a CA-04) |
| **Fecha de cierre** | 2026-10-05 |
| **Versión del estándar al cerrar** | 54.2.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Claude Code manda cada llamada y cada archivo leído a Cimiento, en `/v1/logs`, a los 5 segundos. Cimiento los guarda en las tablas de la HU-006, con su proyecto, y una llamada que llega también por el `.jsonl` queda una sola vez. La instalación del estándar activa la telemetría en la configuración del usuario.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Programa | `proyectos/cimiento/core/consumo/telemetria.py`, `proyectos/cimiento/core/consumo/views.py`, `proyectos/cimiento/core/consumo/urls.py`, `proyectos/cimiento/core/consumo/guardar.py`, `proyectos/cimiento/config/urls.py` | ✅ | CP-001 |
| CA-02 | Programa | `proyectos/cimiento/core/consumo/views.py`, `proyectos/cimiento/core/consumo/guardar.py` | ✅ | CP-002 |
| CA-03 | Programa | `proyectos/cimiento/core/consumo/guardar.py`, `proyectos/cimiento/core/consumo/models.py`, `proyectos/cimiento/core/consumo/lector.py`, `proyectos/cimiento/core/consumo/migrations/0002_llamada_solicitud.py` | ✅ | CP-003 |
| CA-04 | Programa | `proyectos/cimiento/core/herramientas/instalar.py`, `validadores/instalar.py` | ✅ | CP-004 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 7 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Levantar Cimiento con `python manage.py runserver`, sin número: escucha en el `PUERTO` del `.env`, que es adonde Claude Code manda. Vale desde la siguiente sesión de Claude Code que se abra.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El proyecto sale de la sesión, buscando su `.jsonl` | La telemetría no trae la carpeta, y `OTEL_RESOURCE_ATTRIBUTES` es de toda la máquina | No hace falta: está en `guardar.py` |
| La llamada por telemetría se guarda con la solicitud como mensaje, y el `.jsonl` le pone el suyo | Así se ve en vivo sin duplicar | No hace falta: está en `guardar.py` |
| Responder `{}` aunque se descarte | Un error haría reintentar lo que nunca va a entrar | No hace falta |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

No aplica.

## 8. Despliegue, si aplica  ·  `13·DOC4`

La instalación del estándar activa la telemetría en `~/.claude/settings.json`. Para quitarla, borrar de su `env` las claves `CLAUDE_CODE_ENABLE_TELEMETRY` y `OTEL_*`.
