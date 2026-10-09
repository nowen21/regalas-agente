# Funcionalidad implementada · Fase `A-EP-026-HU-011-manage-py-busca-su-python` (módulo arranque de Cimiento)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-026-HU-011-manage-py-busca-su-python` |
| **Módulo** | Arranque de Cimiento, `proyectos/cimiento/manage.py` |
| **Especificación del módulo** | Los CA de la [HU-011](../HU-011-manage-py-se-abre-siempre-con-el-python-de-cimiento.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-011 (CA-01, CA-02, CA-03) |
| **Fecha de cierre** | 2026-10-08 |
| **Versión del estándar al cerrar** | 56.8.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

`manage.py` revisa con qué Python lo abrieron. Si no es el de `proyectos/cimiento/.venv/` y ese existe, se vuelve a abrir con él, con los mismos argumentos, y devuelve lo que él devuelva. Si ya corre con el de `.venv`, o si no hay `.venv`, sigue igual. La salida y los errores se escriben en UTF-8. Con eso, el comando del aviso de cada sesión (`python manage.py ver_estandar …`) funciona tal como está escrito.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Funcional | `proyectos/cimiento/manage.py` (`python_que_toca`, `main`) | Hecho | EV-01, EV-02 |
| CA-02 | Funcional | `proyectos/cimiento/manage.py` (`python_que_toca`) | Hecho | EV-01 |
| CA-03 | Funcional | `proyectos/cimiento/manage.py` (`en_utf8`, `PYTHONIOENCODING`) | Hecho | EV-01, EV-02 |

**Faltantes / diferimientos:** ninguno

### 2.2 Plan de trabajo → ejecución

Las 3 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Igual que antes: `python manage.py <orden>` desde cualquier Python. No hace falta acordarse de usar el de `.venv`.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Se compara `sys.prefix` con `.venv`, no el ejecutable | Así `pythonw` del mismo ambiente, que usa el vigilante, no se vuelve a abrir con `python.exe` | S-355 |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Nada.
