# Plan de Pruebas · Fase A-EP-026-HU-008, los reportes   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP026-HU008-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-008](../HU-008-lo-que-un-proyecto-reporta-llega-al-estandar-como-pendiente.md) |
| **Fecha** | 2026-10-06 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 132](../../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.estandar core.ayuda core.validadores core.herramientas.tests_instalacion core.enganches.tests_sesion`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-008 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-008 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |
| HU-008 | CA-03 | CP-003 | Funcional | Alta | Sí | ☑ |
| HU-008 | CA-04 | CP-004 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 4 de 4 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · Reportar

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `manage.py reportar` desde un proyecto registrado | Reporte abierto, con historia, sin versión nueva del estándar |
| 2 | Abrir «Reportes» | Lo lista |

### CP-002 · Corregir

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Marcarlo corregido con una versión del estándar posterior | Corregido, apuntando a esa versión |

### CP-003 · El proyecto se entera

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir los avisos del proyecto | Dice el reporte y la versión |
| 2 | Pedirlos otra vez | Nada |

### CP-004 · El aviso de versión mira la base

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Con el estándar congelado, pedir la vigente y las publicadas | Salen de la base |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 4, en `resultado_pruebas.md`.
