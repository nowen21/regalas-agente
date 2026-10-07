# Plan de Pruebas · Fase A-EP-028-HU-006, tablas avanzadas   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP028-HU006-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-006](../HU-006-las-tablas-de-cimiento-usan-los-recursos-de-tablas-de-la-plantilla.md) |
| **Fecha** | 2026-10-07 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 137](../../../../../historico-chat/resumenes/2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.inicio core.estandar core.historia core.proyectos core.niveles core.ayuda core.consumo`: la prueba nueva y las suites de las pantallas con tablas.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-006 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-006 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 2 de 2 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · Las listas se ordenan, se filtran y se paginan

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir cada lista de registros | Cada columna con su botón de ordenar y su filtro; el pie con las filas por página |

### CP-002 · Un solo código y un solo pie

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Revisar las tablas y la página | `data-tabla-avanzada`, el pie común, `tablas.js` y List.js de Tabler |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 2, en `resultado_pruebas.md`.
