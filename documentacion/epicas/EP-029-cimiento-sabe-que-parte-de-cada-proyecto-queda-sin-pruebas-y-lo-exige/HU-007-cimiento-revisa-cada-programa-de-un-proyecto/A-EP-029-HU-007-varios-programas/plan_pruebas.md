# Plan de Pruebas · Fase A-EP-029-HU-007, varios programas   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP029-HU007-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-007](../HU-007-cimiento-revisa-cada-programa-de-un-proyecto.md) |
| **Fecha** | 2026-10-08 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 4 del pendiente 141](../../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-4.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

La herramienta de cada lenguaje se simula (`08·T3`).

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.pruebas`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-007 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-007 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |
| HU-007 | CA-03 | CP-003 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 3 de 3 exigencias cubiertas = 100%.

## 6. Casos de prueba

### CP-001 · Encuentra todos los programas

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `proyectos/front/angular.json` y `proyectos/back/requirements.txt` | Angular y Python, en sus carpetas |
| 2 | Django con un `requirements.txt` en una subcarpeta | Un solo programa |

### CP-002 · Revisa y pone la herramienta en cada uno

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Revisar el proyecto de dos programas | Dos revisiones con la misma fecha, `programa` `proyectos/back` y `proyectos/front` |
| 2 | Poner la parte con la herramienta simulada | Se pide instalar coverage.py en el programa Python y se revisa Angular |

### CP-003 · La fila y el detalle

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Revisiones de 80% y 30% con la misma fecha | La fila dice 30% |
| 2 | Abrir el detalle | Muestra los dos programas |

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 3, en `resultado_pruebas.md`.
