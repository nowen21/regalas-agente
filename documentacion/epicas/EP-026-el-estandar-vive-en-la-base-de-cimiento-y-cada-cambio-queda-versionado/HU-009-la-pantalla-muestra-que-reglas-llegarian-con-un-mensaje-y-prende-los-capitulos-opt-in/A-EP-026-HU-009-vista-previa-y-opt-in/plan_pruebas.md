# Plan de Pruebas · Fase A-EP-026-HU-009, vista previa y opt-in   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP026-HU009-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-009](../HU-009-la-pantalla-muestra-que-reglas-llegarian-con-un-mensaje-y-prende-los-capitulos-opt-in.md) |
| **Fecha** | 2026-10-06 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 132](../../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.proyectos core.estandar core.herramientas core.enganches`: las suites de los programas que la fase cambia.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-009 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-009 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |
| HU-009 | CA-03 | CP-003 | Funcional | Alta | Sí | ☑ |
| HU-009 | CA-04 | CP-004 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 4 de 4 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · Los opt-in son ajustes del proyecto

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Editar un proyecto registrado con «Sí» en el patrón opt-in 15 | El ajuste queda en el proyecto, con historia y versión nueva del proyecto |
| 2 | Leer `.agente/configuracion.md` del proyecto | Lista el patrón opt-in 15 en «sí» |

### CP-002 · Las reglas se eligen con los opt-in de la base

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Con el `CLAUDE.md` en «no» y la base en «sí», pedir los apagados del proyecto | El 15 no está apagado |
| 2 | Pedir los apagados de una carpeta sin registro | Salen de su `CLAUDE.md` |

### CP-003 · Lo que dice el CLAUDE.md pasa a la base

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pasar los opt-in de un proyecto con el 18 en «sí» en su `CLAUDE.md` | La base queda con el 18 en «sí» |
| 2 | Pasarlos otra vez | Nada cambia |

### CP-004 · La vista previa

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir «Vista previa» con un proyecto y un mensaje | Muestra el bloque de reglas de ese mensaje |
| 2 | Contar la historia antes y después | No cambió |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 4, en `resultado_pruebas.md`.
