# Plan de Pruebas · Fase A-EP-005-HU-027, el núcleo y lo que vuelve después de un resumen   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP005-HU027-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-027](../HU-027-el-nucleo-llega-completo-y-lo-entregado-vuelve-despues-de-un-resumen.md) |
| **Fecha** | 2026-10-09 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 133](../../../../../historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.herramientas.tests_entrega_de_reglas core.comun.tests`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-027 | CA-01 | CP-001, CP-002 | Funcional | Crítica | Sí | ☐ |
| HU-027 | CA-02 | CP-003, CP-004 | Funcional | Crítica | Sí | ☐ |

**Cobertura:** 2 de 2 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · Al abrir llega el núcleo

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir una sesión nueva | Llegan reglas blindadas, sin pasar del tope |
| 2 | Mandar mensajes hasta vaciar la entrega | Al final llegaron todas las blindadas vigentes, cada una una vez |

### CP-002 · El enganche de `SessionStart` no frena

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `hook_reglas_sesion.py` con `source: startup` | Sale con 0; si trae texto, es `additionalContext` de `SessionStart` |

### CP-003 · Después de un resumen vuelve lo entregado

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Entregar `cambiar-codigo` entera y abrir con `source: compact` | Llega otra vez el núcleo, y la siguiente escritura de `x.py` vuelve a traer `cambiar-codigo` |
| 2 | Lo mismo con `source: clear` | Igual |

### CP-004 · Retomar no vuelve a cero

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir con `source: resume` después de entregar todo | No llega nada |
| 2 | Un subagente después de `compact` | Conserva su cuenta |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 4, en `resultado_pruebas.md`.
