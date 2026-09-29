# Funcionalidad implementada · Fase `D-EP-004-HU-012-las-marcas-se-miden-al-escribir` (módulo Comprobación automática)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `D-EP-004-HU-012-las-marcas-se-miden-al-escribir` |
| **Módulo** | Comprobación automática |
| **Especificación del módulo** | RN-06 y RN-07 de [HU-012](../HU-012-marcas-de-generacion-automatica.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | HU-012 (CA-05, CA-06) |
| **Fecha de cierre** | 2026-09-28 |
| **Versión del estándar al cerrar** | 39.5.0 |
| **Commit** | Se completa al commitear |

## 1. Qué se implementó, resumen

Cuando el agente escribe o edita un `.md`, le llegan en ese mismo turno las marcas de redacción de lo que acaba de escribir, con su línea y qué poner en su lugar. No se repiten las marcas que el archivo ya tenía. El modelo del resumen de sesión lleva sus campos en tabla, así que llenarlo no produce marcas, y los resúmenes viejos se siguen leyendo.

## 2. Trazabilidad  ·  `13·DOC11`

| Tarea | Qué se hizo | Dónde quedó | Evidencia |
|---|---|---|---|
| T-01 | `medir_texto` y la tabla de qué poner en lugar de cada marca | `validadores/marcas.py` | CP-001 |
| T-02 | Mide lo recién escrito y lo devuelve por el contexto del agente | `adaptadores/claude-code/hook_md.py` | CP-001 |
| T-03 | 6 casos del enganche | `validadores/tests/test_las_marcas_se_miden_al_escribir.py` | CP-001 |
| T-04 | Campos del hallazgo y «Viene de» en tabla | `plantillas/sesion.md` | CP-002 |
| T-05 | Lee los campos en tabla y en viñeta; escribe «Viene de» en tabla | `validadores/resumen.py` | CP-002 |
| T-06 | 5 casos del molde y de la lectura, y el caso del enganche del resumen ajustado | El mismo archivo de pruebas y `validadores/pruebas.py` | CP-002 |
| T-07 | Guía, registro y versión | `validadores/docs/hook_md.md`, `CHANGELOG.md`, `VERSION` | CP-003 |
| T-08 | Cierre de HU-012, del pendiente 102 y del H-4 | HU-012, `pendientes/`, resumen de la sesión | — |

**Faltantes / diferimientos:** ninguno.

## 3. Qué se probó

| Qué | Resultado |
|---|---|
| CP-001 a CP-003 | Cumple; detalle en [resultado_pruebas.md](resultado_pruebas.md) |
| Pruebas de la fase | 86 en OK |
| `validar.py estandar` y `versionado` | Sin incumplimientos |
