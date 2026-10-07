# Plan de Pruebas · Fase A-EP-028-HU-001, el capítulo 17 obligatorio   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP028-HU001-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-001](../HU-001-el-capitulo-17-rige-para-todo-proyecto-con-pantallas-y-exige-que-la-pantalla-oriente-sola.md) |
| **Fecha** | 2026-10-07 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 137](../../../../../historico-chat/resumenes/2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.estandar.tests_capitulo17 core.proyectos core.ayuda core.herramientas`: la prueba nueva y las suites de los ajustes, la ayuda y el recuperador de reglas.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-001 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-001 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 2 de 2 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · El capítulo 17 rige para todo proyecto con pantallas

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer el encabezado del capítulo 17 | No dice opt-in |
| 2 | Pedir las reglas de un mensaje de interfaz para una carpeta cuyo `CLAUDE.md` dice «no» en el 17 | Llegan reglas `17·I` |
| 3 | Revisar el catálogo de ajustes | No trae `opt_in_17` |

### CP-002 · La pantalla orienta sola, y la plantilla instalada va primero

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer el capítulo 17 | Trae `I7 · La pantalla orienta sola` con su checklist |
| 2 | Leer `I5` | Pide usar lo que trae la plantilla instalada |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 2, en `resultado_pruebas.md`.
