# Funcionalidad implementada · Fase `A-EP-029-HU-003-aviso-commit-e-instalacion` (módulo Pruebas de Cimiento: `core/pruebas/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-029-HU-003-aviso-commit-e-instalacion` |
| **Módulo** | Pruebas de Cimiento: `core/pruebas/`, con el arranque, el commit y la instalación |
| **Especificación del módulo** | Los CA de la [HU-003](../HU-003-al-empezar-a-trabajar-cimiento-avisa-si-la-revision-falta-o-esta-vencida.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-003 (CA-01, CA-02, CA-03) |
| **Fecha de cierre** | 2026-10-08 |
| **Versión del estándar al cerrar** | 56.8.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Al abrir una sesión, el aviso de arranque dice si al proyecto le falta la herramienta que revisa sus pruebas, si nunca se revisó o si la última revisión pasó los días elegidos. Lo lee de la base de Cimiento sin arrancar Django, y calla con «nada», sin registro o sin base. El `pre-commit` corre `validar.py pruebas`: con «no dejar guardar», la revisión vencida es falla y el commit se rechaza. El instalador pone coverage.py en el Python del proyecto si le falta (Python y Django), comprueba PHPUnit y PCOV (Laravel) o `karma-coverage` (Angular), y lo anota en Cimiento con `manage.py marcar_pruebas`. El desinstalador quita coverage.py solo si la puso Cimiento.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Enganche | `core/pruebas/aviso.py`, `core/enganches/sesion.py` | Hecho | CP-001, CP-002 |
| CA-02 | Validador | `core/herramientas/validar.py`, `PLANTILLA_PRE_COMMIT` de `core/herramientas/instalar.py` | Hecho | CP-003 |
| CA-03 | Instalador | `core/pruebas/parte.py`, `core/pruebas/management/commands/marcar_pruebas.py`, `instalar.py`, `desinstalar.py` | Hecho | CP-004, CP-005 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 4 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno. `core/pruebas/lenguaje.py` y `core/pruebas/revisar.py` se agregaron al plan antes de tocarlos, para que `python_del_proyecto` viva en un solo sitio sin Django.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Funciona solo: el aviso sale al abrir cada sesión, y el commit se rechaza si el proyecto eligió «no dejar guardar». Para que un proyecto reciba la herramienta y la línea nueva del `pre-commit` hay que volver a instalar Cimiento en él. A mano: `python validadores/validar.py pruebas --raiz «carpeta»`.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La parte solo se pone en proyectos del registro real, fuera de la carpeta temporal | Las pruebas del instalador no deben instalar paquetes | Ninguna |
| `marcar_pruebas --quitar` dice si la puso Cimiento antes de borrar | El desinstalador corre sin Django y necesita saberlo | Ninguna |

## 6. Deuda técnica y pendientes generados

Ninguna. Fallas ajenas vistas en la regresión: pendiente 140 y el enlace roto del pendiente 142, de otra sesión.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

`manage.py migrate` en Cimiento, y volver a instalar cada proyecto (versión MAYOR).
