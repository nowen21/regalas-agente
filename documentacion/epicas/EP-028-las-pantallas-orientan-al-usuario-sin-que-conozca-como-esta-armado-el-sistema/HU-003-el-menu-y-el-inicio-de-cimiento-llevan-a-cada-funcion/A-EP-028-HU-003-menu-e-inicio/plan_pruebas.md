# Plan de Pruebas · Fase A-EP-028-HU-003, menú e inicio   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP028-HU003-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-003](../HU-003-el-menu-y-el-inicio-de-cimiento-llevan-a-cada-funcion.md) |
| **Fecha** | 2026-10-07 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 137](../../../../../historico-chat/resumenes/2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.inicio core.ayuda core.estandar.tests_pantalla`: la prueba nueva y las suites de las pantallas que usan el menú.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-003 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-003 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 2 de 2 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · Toda pantalla está en el menú

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir el inicio con una cuenta | El menú enlaza todas las pantallas que no son detalle de un registro |
| 2 | Abrir «Propuestas» | Su entrada del menú está marcada como activa |

### CP-002 · El inicio muestra lo que espera una decisión

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Con 2 propuestas sin aprobar y 1 reporte abierto, abrir el inicio | Dice 2 y 1, con el enlace a cada pantalla; el menú muestra los mismos números |
| 2 | Sin nada pendiente, abrir el inicio | Dice que no hay nada esperando una decisión |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 2, en `resultado_pruebas.md`.
