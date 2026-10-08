# Plan de Pruebas · Fase E-EP-027-HU-006, la plantilla y el paso   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP027-HU006-E |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-006](../HU-006-las-reglas-de-cada-proyecto-viven-en-la-misma-tabla.md), CA-05 |
| **Fecha** | 2026-10-07 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 136](../../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md) y el «apruebo» del usuario del 2026-10-07 |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.herramientas`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-006 | CA-05 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-006 | CA-05 | CP-002 | Funcional | Alta | No | ☑ |

**Cobertura:** 1 de 1 exigencias de esta fase cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · La plantilla dice dónde viven

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Rellenar la plantilla `CLAUDE.md` como el instalador | El paso 4 y el punto 5.2 dicen que las reglas del proyecto registrado viven en Cimiento y llegan como índice; el archivo queda para el proyecto no registrado |
| 2 | Instalar en una carpeta nueva | No se crea `.agente/reglas-proyecto.md` |

### CP-002 · El paso en la base viva

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `pasar_reglas_proyecto --todos --borrar` | Cuatro proyectos pasan y su archivo queda en la historia y se borra; AgroSystem no pasa y lo dice |
| 2 | `ver_regla --proyecto` de cada uno de los cuatro | Sus reglas, las mismas que tenía el archivo |
| 3 | Las cinco propuestas | Quedan en «Propuestas por aprobar» |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 2, en `resultado_pruebas.md`.
