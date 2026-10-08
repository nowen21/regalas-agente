# Plan de Pruebas · Fase A-EP-027-HU-002, el paso   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP027-HU002-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-002](../HU-002-las-269-reglas-pasan-a-las-tablas-sin-perder-nada.md) |
| **Fecha** | 2026-10-07 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 136](../../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.estandar core.enganches`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-002 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-002 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |
| HU-002 | CA-03 | CP-003 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 3 de 3 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · Todas las reglas quedan en las tablas

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pasar el estándar | Una fila por regla del texto; F1 con su capítulo «02 · Flujo de trabajo», sus tareas en orden y su ejemplo |
| 2 | Mirar F0 | Sus dependencias «depende de» F2, DOC15 y DOC16, unidas a esas reglas |
| 3 | Mirar «validable» de G2, de F2 y de C1 | «sí» con `commits.py`, «falta el programa» y «no» |

### CP-002 · Nada se pierde

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Comparar el texto de cada documento antes y después | Iguales salvo las notas con fecha del sello y el orden del molde |
| 2 | Buscar la nota «Corregida el 2026-08-22» de C1 | Está en la historia de C1, con esa fecha, y no en su sello |

### CP-003 · Pasar dos veces no duplica

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pasar el estándar dos veces | Las mismas filas y las mismas notas |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 3, en `resultado_pruebas.md`.
