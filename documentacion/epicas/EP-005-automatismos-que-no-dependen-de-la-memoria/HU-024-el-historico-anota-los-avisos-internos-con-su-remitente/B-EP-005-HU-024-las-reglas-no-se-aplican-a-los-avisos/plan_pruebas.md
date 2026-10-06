# Plan de Pruebas · Fase B-EP-005-HU-024, las reglas no se aplican a los avisos   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que ningún criterio de aceptación quede sin al menos un caso, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba **antes** de correr la primera prueba y no se modifica al ejecutar: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP005-HU024-B |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-024](../HU-024-el-historico-anota-los-avisos-internos-con-su-remitente.md), CA-02 |
| **Fecha** | 2026-10-06 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 124](../../../../../historico-chat/resumenes/2026-10-05/pendientes/124-la-pantalla-gasto-no-dice-por-donde-empezar/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

`manage.py test core.herramientas.tests_avisos_internos`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-024 | CA-02 | CP-001 | Funcional | Crítica | Sí | ☑ |

**Cobertura:** 1 de 1 = 100 %.

## 6. Casos de prueba

### CP-001 · El aviso interno no recibe reglas ni el aviso de `01·C28`

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir `como_texto` de un `<task-notification>` | `""` |
| 2 | Pedir `como_texto` de un `<agent-message` | `""` |
| 3 | Pedir `como_texto` de «hola», sin palabra clave | Trae el aviso de `01·C28`, como antes |

## 9. Gestión de defectos

Van a `resultado_pruebas.md` §4.

## 12. Métricas e informe

1 caso.
