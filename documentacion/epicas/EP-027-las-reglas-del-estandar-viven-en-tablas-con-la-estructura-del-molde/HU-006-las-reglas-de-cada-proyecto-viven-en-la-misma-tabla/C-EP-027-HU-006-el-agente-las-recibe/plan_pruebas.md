# Plan de Pruebas · Fase C-EP-027-HU-006, el agente las recibe   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP027-HU006-C |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-006](../HU-006-las-reglas-de-cada-proyecto-viven-en-la-misma-tabla.md), CA-03 |
| **Fecha** | 2026-10-07 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 136](../../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md) y el «apruebo» del usuario del 2026-10-07 |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.enganches`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-006 | CA-03 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-006 | CA-03 | CP-002 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 1 de 1 exigencias de esta fase cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · El índice llega al abrir la sesión

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir el contexto de un proyecto con reglas en la tabla | El índice con cada código, título y grupo, y el comando `ver_regla` para leerlas |
| 2 | Pedirlo con un tope pequeño | Cabe en el tope y dice cómo ver el resto |
| 3 | Pedirlo de un proyecto sin reglas en la tabla | Nada |

### CP-002 · El freno deja escribir lo que autorizan

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir lo autorizado de un proyecto con reglas en la tabla | Las rutas de la regla que autoriza, con su código |
| 2 | Pedirlo de un proyecto sin reglas en la tabla y con su archivo | Lo del archivo, como antes |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 2, en `resultado_pruebas.md`.
