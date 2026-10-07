# Plan de Pruebas · Fase A-EP-028-HU-002, la guía   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP028-HU002-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-002](../HU-002-el-estandar-tiene-su-guia-de-diseno-de-pantallas.md) |
| **Fecha** | 2026-10-07 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 137](../../../../../historico-chat/resumenes/2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.estandar.tests_guia`. La fase no cambia programas: solo texto del estándar.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-002 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-002 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 2 de 2 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · La guía cubre el encargo

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer la guía del estándar en la base | Trae las 14 secciones del encargo |
| 2 | Leer el capítulo 17 | Enlaza la guía |

### CP-002 · La plantilla instalada va primero

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer las secciones de componentes, tablas y formularios | Cada una dice el recurso de Tabler con que se hace |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 2, en `resultado_pruebas.md`.
