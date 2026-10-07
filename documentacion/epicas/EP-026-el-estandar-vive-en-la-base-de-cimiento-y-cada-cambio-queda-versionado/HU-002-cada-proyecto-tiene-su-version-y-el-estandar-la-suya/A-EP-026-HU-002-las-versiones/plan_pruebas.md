# Plan de Pruebas · Fase A-EP-026-HU-002, las versiones   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP026-HU002-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-002](../HU-002-cada-proyecto-tiene-su-version-y-el-estandar-la-suya.md) |
| **Fecha** | 2026-10-06 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 132](../../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.historia core.proyectos core.niveles core.ayuda`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-002 | CA-01 | CP-001 | Funcional | Crítica | Sí | ☑ |
| HU-002 | CA-02 | CP-002 | Funcional | Crítica | Sí | ☑ |
| HU-002 | CA-03 | CP-003 | Funcional | Alta | Sí | ☑ |
| HU-002 | CA-04 | CP-004 | Funcional | Media | Sí | ☑ |

**Cobertura:** 4 de 4 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · El nivel de un proyecto sube la versión del proyecto

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Guardar un nivel desde la pantalla de reglas con «no» y «no» | Versión del proyecto 1.0.1, PARCHE; el cambio apunta a ella |
| 2 | Mirar la versión del estándar | No cambió |
| 3 | Guardar dos niveles en un mismo envío | Una sola versión nueva con los dos cambios |

### CP-002 · Las dos preguntas fijan el tipo

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | «sí» a la primera | MAYOR: 2.0.0 |
| 2 | «no» y «sí» | MENOR |
| 3 | «no» y «no» | PARCHE |
| 4 | Abrir los formularios de niveles, configuración, proyecto y suspensiones | Traen las dos preguntas |

### CP-003 · Un ajuste común sube el estándar

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Guardar un ajuste de capa 1 con «no» y «no» | El estándar sube un PARCHE sobre lo que dice `VERSION` |

### CP-004 · La pantalla de versiones

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir `/historia/versiones/` | Lista las versiones con número, tipo y sus cambios |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 4, en `resultado_pruebas.md`.
