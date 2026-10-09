# Plan de Pruebas · Fase A-EP-026-HU-011, `manage.py` busca su Python   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP026-HU011-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-011](../HU-011-manage-py-se-abre-siempre-con-el-python-de-cimiento.md) |
| **Fecha** | 2026-10-08 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 145](../../../../../historico-chat/resumenes/2026-10-08/pendientes/145-manage-py-usa-el-python-de-cimiento/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.comun.tests_arranque`. Además, la consulta real: `python proyectos/cimiento/manage.py ver_estandar base/01-conducta/palabras-clave.md`, con el Python del computador.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-011 | CA-01 | CP-001, CP-004 | Funcional | Crítica | Sí | ☑ |
| HU-011 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |
| HU-011 | CA-03 | CP-003, CP-004 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 3 de 3 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · Con otro Python, se vuelve a abrir con el de `.venv`

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir el Python que toca, con una carpeta que tiene `.venv` y otro Python corriendo | Devuelve el de `.venv` |
| 2 | Correr `manage.py check` con el Python del computador | Termina sin error |

### CP-002 · Sin `.venv`, o ya con él, sigue igual

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir el Python que toca, con una carpeta sin `.venv` | No devuelve ninguno |
| 2 | Pedirlo cuando el que corre ya es el de `.venv` | No devuelve ninguno |

### CP-003 · Las tildes en UTF-8

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `manage.py` con otro Python y que escriba «capítulo» | La salida, leída como UTF-8, trae «capítulo» |

### CP-004 · La consulta real

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `python proyectos/cimiento/manage.py ver_estandar base/01-conducta/palabras-clave.md` | Termina sin error y las tildes salen bien |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 4, en `resultado_pruebas.md`.
