# Funcionalidad implementada · Fase `A-EP-026-HU-005-la-pantalla-del-estandar` (módulo Estándar en la base)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-026-HU-005-la-pantalla-del-estandar` |
| **Módulo** | Estándar en la base, `proyectos/cimiento/core/estandar/` |
| **Especificación del módulo** | Los CA de la [HU-005](../HU-005-el-estandar-se-administra-y-se-autoriza-desde-la-pantalla.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-005 () |
| **Fecha de cierre** | 2026-10-06 |
| **Versión del estándar al cerrar** | 56.2.1 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

En «Estándar» se ven y se cambian los documentos del estándar y la memoria de cada proyecto. Cada envío hace las dos preguntas, queda en la historia y sube la versión que le toca; al cambiar un documento, el mapa de tareas y las reglas por tarea se arman de nuevo en la base. Lo que propone el agente con `manage.py proponer` espera en «Propuestas» hasta que el administrador lo aprueba o lo rechaza. El agente lee con `ver_estandar` y `ver_recuerdo`, y el arranque toma la memoria de la base.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|


**Faltantes / diferimientos:** ninguno

### 2.2 Plan de trabajo → ejecución

Las 6 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Menú → «Estándar». Desde `proyectos/cimiento/`: `manage.py proponer`, `manage.py ver_estandar <ruta>` y `manage.py ver_recuerdo <nombre> --proyecto <carpeta>`.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Se edita el documento entero y el mapa se arma en la base; las propuestas no suben versión | Es como está guardado; derivados viejos darían reglas de antes; nada se aplica sin aprobar | S-337 |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Aplicar `manage.py migrate estandar` (hecho en esta máquina el 2026-10-06).
