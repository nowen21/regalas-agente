# Funcionalidad implementada · Fase `A-EP-025-HU-003-registro-de-proyectos` (módulo `proyectos/cimiento/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-003-registro-de-proyectos` |
| **Módulo** | `proyectos/cimiento/` |
| **Especificación del módulo** | Los CA de la [HU-003](../HU-003-los-proyectos-quedan-registrados-en-cimiento.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-003 (CA-01 a CA-04) |
| **Fecha de cierre** | 2026-10-04; ciclo 2, 2026-10-05 |
| **Versión del estándar al cerrar** | 54.2.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

«Proyectos» en el menú lista los proyectos registrados en Cimiento, con su ruta, su carpeta de Claude Code y sus límites de aviso por enganche y por archivo. Un administrador los registra, los edita y los desactiva; el grupo consulta solo ve la lista. La carpeta de Claude Code se calcula desde la ruta. La base arranca con los proyectos de `plantillas/proyectos.md` cuya carpeta existe, y el instalador registra cada proyecto nuevo.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Programa | `proyectos/cimiento/core/proyectos/models.py`, `proyectos/cimiento/core/proyectos/claude.py`, `proyectos/cimiento/core/proyectos/views.py`, `proyectos/cimiento/core/proyectos/templates/proyectos/lista.html`, `proyectos/cimiento/core/proyectos/templates/proyectos/formulario.html` | ✅ | CP-001 |
| CA-02 | Programa | `proyectos/cimiento/core/proyectos/models.py`, `proyectos/cimiento/core/proyectos/forms.py` | ✅ | CP-002 |
| CA-03 | Programa | `proyectos/cimiento/core/proyectos/views.py`, `proyectos/cimiento/core/proyectos/urls.py` | ✅ | CP-003 |
| CA-04 | Programa | `proyectos/cimiento/core/proyectos/views.py`, `proyectos/cimiento/core/proyectos/templates/proyectos/lista.html` | ✅ | CP-004 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 10 tareas del plan quedaron hechas; T-08 a T-10, en el ciclo 2, por D-01.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

`/proyectos/`, desde «Proyectos» en el menú. El instalador corre `manage.py registrar --nombre «n» --ruta «r»`; repetirla con la misma carpeta no cambia nada. Otro módulo que necesite la carpeta de registros de un proyecto la arma con `os.path.join(proyectos_de_claude(), proyecto.carpeta_claude)` (`core/proyectos/claude.py`).

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La ruta se compara sin distinguir mayúsculas en `clean` | El índice único de la base distingue `C:` de `c:`, y en Windows son la misma carpeta | No hace falta: está en el modelo |
| Límites por defecto de 2000 y 10 000 tokens | Propuesta del agente; cambian por proyecto en la pantalla | No hace falta |
| La tabla vieja de `interfaz/` se borró con la base, después de respaldarla en `cimiento_respaldo_20261005` | Orden del usuario del 2026-10-05; adoptar la tabla vieja dejaba dos registros y columnas que nadie usa | Sí |
| La migración `0002` trae los proyectos de `plantillas/proyectos.md`, no de la tabla vieja | Esa lista está en cada máquina donde se instaló el estándar; la tabla vieja solo en esta. La base de pruebas no trae nada | No hace falta: está en la migración |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

No aplica.

## 8. Despliegue, si aplica  ·  `13·DOC4`

`preparar_base` crea la tabla al instalar el estándar y la `0002` la llena con los proyectos que existen.
