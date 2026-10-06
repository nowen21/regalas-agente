# Funcionalidad implementada · Fase `A-EP-025-HU-016-cerrar-reabrir-y-separar` (módulo `proyectos/cimiento/core/herramientas/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-016-cerrar-reabrir-y-separar` |
| **Módulo** | `proyectos/cimiento/core/herramientas/` |
| **Especificación del módulo** | Los CA de la [HU-016](../HU-016-cerrar-y-reabrir-una-fase-y-separar-los-cambios-por-sesion-son-funcionalidades-de-cimiento.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-016 (CA-01 a CA-04) |
| **Fecha de cierre** | 2026-10-05 |
| **Versión del estándar al cerrar** | 54.4.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Tres órdenes de `manage.py`. `cerrar_fase` escribe el estado, el resultado y la funcionalidad con lo que dicen los planes y marca por llenar lo que un programa no sabe; cuando ya no queda ninguna marca, cierra la fase en el plan, la HU y la épica. `reabrir_fase` es su contraria. `cambios_por_sesion` lista lo que cambió cada sesión y prepara o suelta para el commit lo de una sola.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Programa | `proyectos/cimiento/core/herramientas/fase.py` | ✅ | CP-001 |
| CA-02 | Programa | `proyectos/cimiento/core/herramientas/fase.py` | ✅ | CP-002 |
| CA-03 | Programa | `proyectos/cimiento/core/herramientas/cambios.py` | ✅ | CP-003 |
| CA-04 | Programa | `proyectos/cimiento/core/proyectos/management/commands/` | ✅ | CP-004 |

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

Desde `proyectos/cimiento/`, con el ambiente de Cimiento:

1. `python manage.py cerrar_fase «carpeta de la fase» --pruebas "«orden de las pruebas»" --aplicar` escribe los documentos y dice qué líneas faltan por llenar.
2. Se llenan esas líneas y se corre otra vez `python manage.py cerrar_fase «carpeta» --aplicar`.
3. Para reabrir: `python manage.py reabrir_fase «carpeta» --motivo "«por qué»" --aplicar`.
4. Antes de un commit: `python manage.py cambios_por_sesion` lista lo de cada sesión; `python manage.py cambios_por_sesion «sesión» --preparar --aplicar` prepara lo de una, y `--soltar` lo saca.

Sin `--aplicar`, las tres dicen qué harían. En `--pruebas`, la ruta del programa va con `\` y entre comillas: la corre `cmd`.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Lo humano se escribe en el documento, no por argumentos | Son textos largos, y el validador de marcas ya las vigila | No hace falta: está en `fase.py` |
| Lo que tocaron dos sesiones no se prepara | Quien hace el commit decide; prepararlo mezclaría trabajo ajeno | No hace falta: está en `cambios.py` |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

No aplica.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica: las órdenes llegan con Cimiento.
