# Plan de Pruebas · Fase A-EP-025-HU-033, el encabezado y las secciones del análisis   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU033-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-033](../HU-033-cimiento-llena-los-analisis-sin-guiones-sueltos.md) |
| **Fecha** | 2026-10-09 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 3 del pendiente 133](../../../../../historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-3.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.enganches.tests_llenar_analisis`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-033 | CA-01 | CP-001, CP-002 | Funcional | Crítica | Sí | ☐ |
| HU-033 | CA-02 | CP-003, CP-004 | Funcional | Crítica | Sí | ☐ |

**Cobertura:** 2 de 2 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · El primer análisis queda con su encabezado

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Prender el primer análisis de un pendiente cuyo «De dónde sale» enlaza el H-1 de un resumen | No queda `«RUTA-ESTANDAR»`, `«copia del pendiente»` ni `«copia del hallazgo»`; trae el texto del pendiente y el del H-1 |

### CP-002 · El segundo análisis deja el hallazgo al agente

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Prender el segundo análisis del mismo pendiente | Trae el pendiente y las rutas, y conserva `«copia del hallazgo»` |
| 2 | Un pendiente sin hallazgo enlazado | Conserva `«copia del hallazgo»` y el análisis se crea igual |

### CP-003 · El comando guarda una sección

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `manage.py analisis seccion «análisis» "Lo acordado" --archivo texto.md` | La sección trae el texto nuevo y el resto del análisis no cambia |

### CP-004 · Una sección que no existe

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr el comando con «No existe» | Falla y nombra las secciones que hay; el análisis no cambia |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 4, en `resultado_pruebas.md`.
