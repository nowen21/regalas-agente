# Funcionalidad implementada · Fase `A-EP-025-HU-011-el-vigilante` (módulo `proyectos/cimiento/core/consumo/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-011-el-vigilante` |
| **Módulo** | `proyectos/cimiento/core/consumo/` |
| **Especificación del módulo** | Los CA de la [HU-011](../HU-011-el-gasto-llega-a-la-base-en-cuanto-claude-code-lo-escribe.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-011 (CA-01 a CA-03) |
| **Fecha de cierre** | 2026-10-05 |
| **Versión del estándar al cerrar** | 55.0.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

`manage.py vigilar_consumo` queda corriendo: `watchdog` avisa cuando cambia un `.jsonl` de un proyecto activo y cada dos segundos se guarda lo nuevo con el lector y el guardado de siempre. Guarda su número de proceso y `--parar` lo detiene. La instalación del estándar lo pone a arrancar al iniciar sesión, lo arranca y quita la tarea diaria; la desinstalación lo quita. «Gasto» ya no lee los `.jsonl` al abrirse.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Programa | `proyectos/cimiento/core/consumo/vigilante.py` | ✅ | CP-001 |
| CA-02 | Programa | `proyectos/cimiento/core/consumo/management/commands/vigilar_consumo.py`, `proyectos/cimiento/core/herramientas/instalar.py`, `proyectos/cimiento/core/herramientas/desinstalar.py`, `proyectos/cimiento/core/herramientas/tests_desinstalar.py`, `proyectos/cimiento/requirements/base.txt`, `proyectos/cimiento/requirements/lock.txt` | ✅ | CP-002 |
| CA-03 | Programa | `proyectos/cimiento/core/consumo/views.py`, `proyectos/cimiento/core/consumo/management/commands/leer_consumo.py`, el plan de la HU-006 | ✅ | CP-003 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 6 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): `tests_instalacion.py` y `tests_tablero.py` se declararon durante la fase, al ver que probaban la tarea diaria y la lectura al abrir que esta HU reemplaza.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Arranca solo al iniciar sesión. A mano, desde `proyectos/cimiento/`: `python manage.py vigilar_consumo`, y `python manage.py vigilar_consumo --parar` para detenerlo.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Los avisos se juntan y se guarda cada 2 segundos | Claude Code escribe varias líneas seguidas | No hace falta: está en `vigilante.py` |
| Solo se cierra la conexión que ya no responde | `close_old_connections` cierra también la sana | No hace falta: está en `vigilante.py` |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

No aplica.

## 8. Despliegue, si aplica  ·  `13·DOC4`

`pip install -r requirements/lock.txt` en el ambiente de Cimiento y `python validadores/instalar.py «estándar» --aplicar`.
