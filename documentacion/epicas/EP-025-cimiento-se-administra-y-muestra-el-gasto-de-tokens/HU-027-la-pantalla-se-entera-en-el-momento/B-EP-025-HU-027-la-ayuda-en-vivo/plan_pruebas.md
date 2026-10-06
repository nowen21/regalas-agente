# Plan de Pruebas · Fase B-EP-025-HU-027, la ayuda en vivo   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que ningún criterio de aceptación quede sin al menos un caso, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba **antes** de correr la primera prueba y no se modifica al ejecutar: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU027-B |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-027](../HU-027-la-pantalla-se-entera-en-el-momento.md), CA-03 |
| **Fecha** | 2026-10-06 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 124](../../../../../historico-chat/resumenes/2026-10-05/pendientes/124-la-pantalla-gasto-no-dice-por-donde-empezar/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

`manage.py test core.ayuda`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-027 | CA-03 | CP-001 | Documental | Media | Sí | ☑ |
| HU-027 | CA-03 | CP-002 | Funcional | Media | Sí | ☑ |

**Cobertura:** 1 de 1 = 100 %.

## 6. Casos de prueba

### CP-001 · La ayuda dice que se actualiza sola

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer la sección `gasto` | Dice que lo nuevo aparece solo en cuanto el vigilante lo guarda |

### CP-002 · Las rutas nuevas no piden sección

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr la prueba de cobertura de la ayuda | Ninguna ruta queda sin sección |

## 9. Gestión de defectos

Van a `resultado_pruebas.md` §4.

## 12. Métricas e informe

2 casos.
