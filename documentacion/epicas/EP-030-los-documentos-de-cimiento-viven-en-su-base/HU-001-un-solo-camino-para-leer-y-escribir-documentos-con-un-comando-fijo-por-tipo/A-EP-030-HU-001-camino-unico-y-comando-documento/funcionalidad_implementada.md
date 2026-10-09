# Funcionalidad implementada · Fase `A-EP-030-HU-001-camino-unico-y-comando-documento` (módulo Estándar de Cimiento)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-030-HU-001-camino-unico-y-comando-documento` |
| **Módulo** | Estándar de Cimiento, `proyectos/cimiento/core/estandar/` |
| **Especificación del módulo** | Los CA de la [HU-001](../HU-001-un-solo-camino-para-leer-y-escribir-documentos-con-un-comando-fijo-por-tipo.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-001 (CA-01, CA-02, CA-03) |
| **Fecha de cierre** | 2026-10-09 |
| **Versión del estándar al cerrar** | 56.8.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

`core/estandar/documentos.py` es el camino único: un registro de tipos (`TIPOS`) y las funciones `listar`, `ver` y `proponer`. Hoy tiene dos tipos: `estandar` (los documentos de `base/`) y `recuerdo` (la memoria de cada proyecto). El comando `manage.py documento tipos|listar|ver|crear|editar|quitar <tipo>` los sirve. Crear, editar y quitar dejan una propuesta que se aprueba en «Estándar → Propuestas»; al aprobarse, `Cambio` guarda el antes y el después. `ver_estandar`, `ver_recuerdo` y `proponer` pasan por el mismo camino, con los mismos argumentos y la misma salida.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Funcional | `core/estandar/management/commands/documento.py`, `core/estandar/documentos.py` | Hecho | EV-01 |
| CA-02 | Funcional | `ver_estandar.py`, `ver_recuerdo.py`, `proponer.py` | Hecho | EV-01 |
| CA-03 | Funcional | `documentos.proponer` y la aprobación de `cambios.aplicar`, anotada por `historia/registro.py` | Hecho | EV-01 |

**Faltantes / diferimientos:** los demás tipos se registran en las HU-003 a HU-006.

### 2.2 Plan de trabajo → ejecución

Las 4 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Desde `proyectos/cimiento/`: `manage.py documento tipos` lista los tipos; `documento listar|ver <tipo> <clave>` lee; `documento crear|editar|quitar <tipo> <clave> --archivo … --motivo …` propone. Los tipos que piden proyecto llevan `--proyecto <carpeta>`.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Escribir es proponer | Nada cambia sin revisarse en la pantalla (acuerdo 5); se reusa `Propuesta` | S-359 |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Nada.
