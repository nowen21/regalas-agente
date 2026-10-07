# Plan de Pruebas · Fase A-EP-028-HU-004, propuestas claras   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP028-HU004-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-004](../HU-004-la-pantalla-de-propuestas-y-las-preguntas-de-version-se-entienden.md) |
| **Fecha** | 2026-10-07 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 137](../../../../../historico-chat/resumenes/2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.estandar core.ayuda core.historia core.proyectos core.niveles`: la prueba nueva y las suites de los formularios que traen las preguntas de versión.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-004 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-004 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 2 de 2 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · Se ve qué cambia y rechazar pide el motivo

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Proponer el cambio de una línea de un documento y abrir «Propuestas» | La tarjeta muestra la línea que sale y la que entra |
| 2 | Rechazar sin motivo | No se rechaza y se avisa |
| 3 | Rechazar con motivo | Queda rechazada con su motivo |

### CP-002 · Las preguntas de versión se entienden

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir «Propuestas» con una pendiente | Las dos preguntas nuevas, cada una con su «?», y el tipo que resulta |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 2, en `resultado_pruebas.md`.
