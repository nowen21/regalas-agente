# Plan de Pruebas · Fase A-EP-029-HU-003, aviso, commit e instalación   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP029-HU003-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-003](../HU-003-al-empezar-a-trabajar-cimiento-avisa-si-la-revision-falta-o-esta-vencida.md) |
| **Fecha** | 2026-10-08 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 141](../../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

La lectura sin Django usa la base de pruebas con `TransactionTestCase`. Las órdenes de pip se simulan (`08·T3`): ninguna prueba instala nada.

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.pruebas core.enganches core.herramientas`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-003 | CA-01 | CP-001, CP-002 | Funcional | Alta | Sí | ☑ |
| HU-003 | CA-02 | CP-003 | Funcional | Alta | Sí | ☑ |
| HU-003 | CA-03 | CP-004, CP-005 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 3 de 3 exigencias cubiertas = 100%.

## 6. Casos de prueba

### CP-001 · Avisa lo que falta

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Proyecto registrado, con la parte, revisado hace 12 días, 7 días | Aviso que dice «hace 12 días» y «Toca hacer otra» |
| 2 | Proyecto registrado, con la parte, nunca revisado | Aviso de que nunca se ha revisado |
| 3 | Proyecto registrado sin la parte | Aviso de volver a instalar Cimiento |
| 4 | Revisado hace 2 días | Ningún aviso |

### CP-002 · Calla cuando no corresponde

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Con «nada» y vencida | Ningún aviso |
| 2 | Carpeta sin registro | Ningún aviso |
| 3 | El arranque de un proyecto vencido | Trae el aviso entre sus hallazgos |

### CP-003 · El commit

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | «no dejar guardar» y vencida | El hallazgo es FALLA |
| 2 | «solo avisar» y vencida | El hallazgo es AVISO |
| 3 | La plantilla del `pre-commit` | Llama `validar.py pruebas` y rechaza si falla |

### CP-004 · El instalador pone coverage.py

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Proyecto Django sin coverage.py | Se pide `pip install coverage` en su Python, y se anota la parte puesta por Cimiento |
| 2 | Proyecto Django que ya la tiene | No se instala nada; se anota la parte, no puesta por Cimiento |
| 3 | Proyecto sin lenguaje reconocido | No se instala nada y se dice por qué |

### CP-005 · El desinstalador quita solo lo suyo

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | La puso Cimiento | Se pide `pip uninstall coverage` y se borra la anotación |
| 2 | Ya la tenía el proyecto | No se desinstala; se borra la anotación |
| 3 | `marcar_pruebas` y `marcar_pruebas --quitar` | La base dice sí y después no |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 5, en `resultado_pruebas.md`.
