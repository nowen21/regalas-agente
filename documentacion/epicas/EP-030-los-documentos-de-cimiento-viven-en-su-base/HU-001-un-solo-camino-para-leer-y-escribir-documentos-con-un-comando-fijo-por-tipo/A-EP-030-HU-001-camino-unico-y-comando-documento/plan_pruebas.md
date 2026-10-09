# Plan de Pruebas · Fase A-EP-030-HU-001, el camino único y el comando `documento`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP030-HU001-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-001](../HU-001-un-solo-camino-para-leer-y-escribir-documentos-con-un-comando-fijo-por-tipo.md) |
| **Fecha** | 2026-10-08 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 142](../../../../../historico-chat/resumenes/2026-10-08/pendientes/142-los-documentos-de-cimiento-viven-en-la-base/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.estandar.tests_documentos core.estandar.tests_en_base`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-001 | CA-01 | CP-001, CP-002 | Funcional | Crítica | Sí | ☑ |
| HU-001 | CA-02 | CP-003 | Funcional | Alta | Sí | ☑ |
| HU-001 | CA-03 | CP-004 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 3 de 3 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · Listar y ver

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `documento listar estandar base/` | Salen las rutas que empiezan así |
| 2 | `documento ver estandar <ruta>` | Sale el texto exacto |
| 3 | `documento ver recuerdo <nombre> --proyecto <ruta>` | Sale el texto del recuerdo |
| 4 | `documento ver estandar <ruta que no existe>` | Error que dice que no está |

### CP-002 · Crear, editar y quitar dejan una propuesta

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `documento crear recuerdo nuevo.md --proyecto … --archivo … --motivo …` | Queda una propuesta pendiente de crear; el recuerdo todavía no existe |
| 2 | `documento editar estandar <ruta> --archivo … --motivo …` | Propuesta pendiente de cambiar; el texto sigue igual |
| 3 | `documento quitar estandar <ruta> --motivo …` | Propuesta pendiente de quitar |
| 4 | Un tipo que no está registrado | Error que lista los tipos que hay |

### CP-003 · Las órdenes de antes leen por el camino único

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `ver_estandar <ruta>` y `ver_recuerdo <nombre>` | La misma salida que `documento ver` |
| 2 | `proponer --ruta …` | Deja la misma propuesta que `documento editar` |

### CP-004 · La historia

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Aprobar la propuesta de cambiar un documento | Queda una fila en `Cambio` con el texto de antes y el de después |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 4, en `resultado_pruebas.md`.
