# Funcionalidad implementada · Fase `A-EP-025-HU-029-reinicio-solo` (módulo El gasto: `core/consumo/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-029-reinicio-solo` |
| **Módulo** | El gasto: `core/consumo/` |
| **Especificación del módulo** | Los CA de la [HU-029](../HU-029-el-vigilante-se-reinicia-solo-cuando-cambia-su-codigo.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-029 (CA-01, CA-02) |
| **Fecha de cierre** | 2026-10-08 |
| **Versión del estándar al cerrar** | 58.0.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

- **El vigilante vigila también el código de Cimiento**, con el mismo `watchdog` que le avisa de los `.jsonl`: sin relojes. Cuentan los `.py`; no las pruebas, ni `.venv`, `__pycache__`, `node_modules`, `.agente` o `.git`.
- **El relevo** (`core/consumo/reinicio.py`): cuando el código lleva 10 segundos sin cambiar, lanza un vigilante nuevo y se detiene apenas el nuevo escribe su número. Si el nuevo no arranca en 60 segundos, el viejo sigue y anota por qué.
- **Arranca sin consola.** Desde el inicio de sesión no hay consola, y el primer mensaje tumbaba al vigilante; ahora lo que diga se descarta. El arranque al iniciar sesión nunca había funcionado (H-41).

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 · Un cambio de código reinicia el vigilante | CA | `core/consumo/reinicio.py`, `core/consumo/vigilante.py` | Hecho | CP-001 |
| CA-02 · El relevo no deja al consumo sin vigilante | CA | `core/consumo/reinicio.py`, `core/consumo/management/commands/vigilar_consumo.py` | Hecho | CP-002 |
| RNF-01 · Sin relojes | RNF | `core/consumo/vigilante.py` | Hecho | CP-001 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 3 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Nada que hacer: el vigilante se reinicia solo. Para detenerlo, `manage.py vigilar_consumo --parar`.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El reinicio va en `reinicio.py`, aparte | Sus dos esperas (la calma y el relevo) son acotadas; `vigilante.py` sigue sin ninguna | Ninguna |
| El viejo espera a que el nuevo escriba su número | Si el nuevo falla, el consumo no queda sin vigilante; se descartó detenerse apenas se lanza el nuevo | Ninguna |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

En cada equipo, arrancar una última vez el vigilante con el código nuevo (abrir `Cimiento vigilar consumo.cmd` o reiniciar sesión); desde ahí se reinicia solo.
