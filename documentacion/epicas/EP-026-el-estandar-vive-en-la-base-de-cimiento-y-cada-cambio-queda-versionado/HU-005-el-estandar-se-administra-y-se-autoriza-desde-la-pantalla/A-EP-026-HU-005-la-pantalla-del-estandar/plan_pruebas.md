# Plan de Pruebas · Fase A-EP-026-HU-005, la pantalla del estándar   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP026-HU005-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-005](../HU-005-el-estandar-se-administra-y-se-autoriza-desde-la-pantalla.md) |
| **Fecha** | 2026-10-06 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 132](../../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.estandar core.ayuda core.enganches.tests_sesion`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-005 | CA-01 | CP-001 | Funcional | Crítica | Sí | ☑ |
| HU-005 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |
| HU-005 | CA-03 | CP-003 | Funcional | Alta | Sí | ☑ |
| HU-005 | CA-04 | CP-004 | Funcional | Crítica | Sí | ☑ |
| HU-005 | CA-05 | CP-005 | Seguridad | Crítica | Sí | ☑ |

**Cobertura:** 5 de 5 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · Cambiar un documento

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | El administrador cambia la línea `**Aplica a:**` de una regla y responde «no» y «sí» | El documento cambia; el estándar sube un MENOR |
| 2 | Mirar el mapa en la base | La regla aparece bajo la tarea nueva, y el cambio del mapa es de la misma versión |

### CP-002 · Crear y quitar

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Crear `base/anexo-prueba.md` | Existe en la base, con su cambio |
| 2 | Crear `plantillas/x.md` | Se rechaza |
| 3 | Quitar `base/anexo-prueba.md` | Ya no está, y la historia tiene el borrado |

### CP-003 · La memoria

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Cambiar un recuerdo de un proyecto | Cambia y sube la versión del proyecto |
| 2 | Pedir el índice de la memoria del proyecto al arranque | Sale el texto de la base |

### CP-004 · Las propuestas

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Proponer un texto nuevo para un documento con `manage.py proponer` | Queda pendiente y el documento no cambia |
| 2 | Aprobarla con las dos preguntas | El documento cambia con su versión y la propuesta queda aprobada |
| 3 | Rechazar otra | Nada cambia y queda rechazada |

### CP-005 · Consulta y las órdenes de lectura

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Guardar, quitar y aprobar con la cuenta de consulta | 403, nada cambia |
| 2 | Correr `ver_estandar base/tareas.md` y `ver_recuerdo` | Imprimen el texto de la base |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 5, en `resultado_pruebas.md`.
