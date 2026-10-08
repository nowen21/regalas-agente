# Plan de Pruebas · Fase D-EP-027-HU-006, el catálogo   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP027-HU006-D |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-006](../HU-006-las-reglas-de-cada-proyecto-viven-en-la-misma-tabla.md), CA-04 |
| **Fecha** | 2026-10-07 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 136](../../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md) y el «apruebo» del usuario del 2026-10-07 |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.validadores`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-006 | CA-04 | CP-001 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 1 de 1 exigencias de esta fase cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · El catálogo lee la tabla

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Validar un proyecto sin archivo y con dos reglas en la tabla, una sin respaldo | Una falla: la regla sin respaldo; ningún aviso de que falta el archivo |
| 2 | Validar un proyecto sin archivo y sin reglas en la tabla | El aviso de siempre |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 1, en `resultado_pruebas.md`.
