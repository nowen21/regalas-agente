# Plan de Pruebas · Fase B-EP-025-HU-032, los enganches leen lo suspendido   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU032-B |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-032](../HU-032-cada-momento-de-cada-enganche-y-cada-revision-de-git-se-puede-suspender.md) |
| **Fecha** | 2026-10-09 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 149](../../../../../historico-chat/resumenes/2026-10-08/pendientes/149-cada-enganche-se-puede-suspender-desde-cimiento/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Desde `proyectos/cimiento/`: `python -m unittest core.enganches.tests_suspendidos`, y las del freno que leen las suspensiones: `manage.py test core.proyectos.tests_configuracion`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-032 | CA-02 | CP-003 | Funcional | Crítica | Sí | ☑ |
| HU-032 | CA-02 | CP-004 | Funcional | Crítica | Sí | ☑ |
| HU-032 | CA-02 | CP-005 | Funcional | Crítica | Sí | ☑ |

**Cobertura:** 1 de 1 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-003 · Una sola consulta con varios a la vez

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Lanzar 8 hilos a la vez con el mismo mensaje | La consulta corre una vez y los 8 tienen la misma lista |
| 2 | Un evento sin mensaje propio (antes de usar una herramienta) en la misma sesión | Usa la lista del mensaje, sin consultar |
| 3 | Un mensaje nuevo | Se consulta una vez más |

### CP-004 · El suspendido sale, lo vencido no, y la entrada queda intacta

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr un adaptador con su momento suspendido | Sale con 0 y sin escribir nada |
| 2 | Una suspensión vencida | El enganche corre |
| 3 | Sin base | El enganche corre |
| 4 | Sin suspensión | El programa del enganche lee el mismo JSON que llegó |

### CP-005 · Solo «freno» apaga el freno entero

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Suspender `historico-del-usuario` | El freno sigue frenando |
| 2 | Suspender `freno` | El freno deja pasar todo menos el núcleo, como hoy |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 3, en `resultado_pruebas.md`.
