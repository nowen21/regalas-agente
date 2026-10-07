# Plan de Pruebas · Fase A-EP-026-HU-007, subir a git   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP026-HU007-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-007](../HU-007-un-boton-de-la-pantalla-guarda-en-git-lo-que-cambio-en-cimiento.md) |
| **Fecha** | 2026-10-06 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 132](../../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.estandar core.ayuda core.herramientas.tests_cambios`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-007 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-007 | CA-02 | CP-002 | Funcional | Crítica | Sí | ☑ |
| HU-007 | CA-03 | CP-003 | Funcional | Alta | Sí | ☑ |
| HU-007 | CA-04 | CP-004 | Seguridad | Crítica | Sí | ☑ |

**Cobertura:** 4 de 4 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · Lo que cambió cada sesión

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir la pantalla con dos sesiones y un archivo compartido | Lista cada sesión con sus archivos y el compartido aparte |

### CP-002 · El commit de una sesión

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Oprimir el botón de una sesión con asunto, idea y hecho | El último commit lleva solo sus archivos, la idea antes que lo hecho y ningún `Co-Authored-By` |

### CP-003 · Si falla

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Hacer que el commit falle | Nada queda preparado, no hay commit nuevo y la pantalla dice el error |

### CP-004 · Consulta

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Oprimir el botón con la cuenta de consulta | 403 y no hay commit |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 4, en `resultado_pruebas.md`.
