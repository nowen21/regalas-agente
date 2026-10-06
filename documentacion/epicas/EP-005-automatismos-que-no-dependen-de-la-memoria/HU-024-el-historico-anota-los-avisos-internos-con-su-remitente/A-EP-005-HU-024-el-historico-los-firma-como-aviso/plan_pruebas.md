# Plan de Pruebas · Fase A-EP-005-HU-024, el histórico los firma como aviso   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que ningún criterio de aceptación quede sin al menos un caso, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba **antes** de correr la primera prueba y no se modifica al ejecutar: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP005-HU024-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-024](../HU-024-el-historico-anota-los-avisos-internos-con-su-remitente.md), CA-01 |
| **Fecha** | 2026-10-06 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 124](../../../../../historico-chat/resumenes/2026-10-05/pendientes/124-la-pantalla-gasto-no-dice-por-donde-empezar/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

`manage.py test core.enganches.tests_avisos_internos` y `core.enganches.tests_sesion`, que prueba el histórico.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-024 | CA-01 | CP-001 | Funcional | Crítica | Sí | ☑ |
| HU-024 | CA-01 | CP-002 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 1 de 1 = 100 %.

## 6. Casos de prueba

### CP-001 · El aviso queda como «Aviso del sistema»

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Anotar un mensaje que abre con `<task-notification>` | Queda `### N · Aviso del sistema` con su texto |
| 2 | Anotar uno que abre con `<agent-message` | Lo mismo |

### CP-002 · El mensaje del usuario sigue igual

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Anotar «Hágalo» | Queda `### N · Usuario` |
| 2 | Anotar un texto que menciona `<agent-message` en la mitad | Queda como «Usuario» |

## 9. Gestión de defectos

Van a `resultado_pruebas.md` §4.

## 12. Métricas e informe

2 casos.
