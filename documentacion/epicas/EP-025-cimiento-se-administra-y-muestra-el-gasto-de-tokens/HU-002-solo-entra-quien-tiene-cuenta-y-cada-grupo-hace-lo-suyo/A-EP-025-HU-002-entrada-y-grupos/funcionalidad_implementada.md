# Funcionalidad implementada · Fase `A-EP-025-HU-002-entrada-y-grupos` (módulo `proyectos/cimiento/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-002-entrada-y-grupos` |
| **Módulo** | `proyectos/cimiento/` |
| **Especificación del módulo** | Los CA de la [HU-002](../HU-002-solo-entra-quien-tiene-cuenta-y-cada-grupo-hace-lo-suyo.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-002 (CA-01 a CA-04) |
| **Fecha de cierre** | 2026-10-04 |
| **Versión del estándar al cerrar** | 54.2.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Toda pantalla de Cimiento pide entrar con usuario y contraseña, salvo la de base apagada. Hay dos grupos, administrador y consulta; un superusuario cuenta como administrador. La mezcla `SoloAdministrador` le da 403 al grupo consulta en las pantallas que cambian algo. Las cuentas se crean con `manage.py crear_cuenta`.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Programa | `proyectos/cimiento/core/cuentas/urls.py`, `proyectos/cimiento/core/cuentas/templates/cuentas/entrar.html`, `proyectos/cimiento/config/settings/base.py`, `proyectos/cimiento/templates/base.html`, `proyectos/cimiento/core/inicio/middleware.py` | ✅ | CP-001 |
| CA-02 | Pantalla | `proyectos/cimiento/core/cuentas/templates/cuentas/entrar.html` | ✅ | CP-002 |
| CA-03 | Programa | `proyectos/cimiento/core/cuentas/permisos.py`, `proyectos/cimiento/core/cuentas/templates/cuentas/sin_permiso.html` | ✅ | CP-003 |
| CA-04 | Programa | `proyectos/cimiento/core/cuentas/migrations/0001_grupos.py`, `proyectos/cimiento/core/cuentas/management/commands/crear_cuenta.py` | ✅ | CP-004 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 8 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno. `sin_permiso.html` se agregó al plan antes de crearlo.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

La primera cuenta: `python manage.py createsuperuser`. Las demás: `python manage.py crear_cuenta --usuario «nombre» --grupo administrador` o `consulta`. Una pantalla que cambia algo hereda de `SoloAdministrador` (`core/cuentas/permisos.py`) antes que de su vista.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La base se revisa en `process_view` de `BaseApagada`, antes de `LoginRequiredMiddleware` | Revisar la sesión ya usa la base, y ese error no llega a `process_exception` | No hace falta: está en el comentario del middleware |
| Un superusuario cuenta como administrador | `createsuperuser` no le pone grupo a la primera cuenta | No hace falta |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] `proyectos/cimiento/README.md`.

## 8. Despliegue, si aplica  ·  `13·DOC4`

En esta máquina: `preparar_base` crea los grupos; la primera cuenta la crea el usuario con `createsuperuser`.
