# Plan de Pruebas · Fase A-EP-026-HU-006, congelar base   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP026-HU006-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-006](../HU-006-los-archivos-de-base-quedan-quietos-en-la-version-55-1-0.md) |
| **Fecha** | 2026-10-06 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 132](../../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.estandar core.enganches.tests_freno core.enganches.tests_sesion core.herramientas.tests_respondo core.validadores`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-006 | CA-01 | CP-001 | Funcional | Crítica | Sí | ☑ |
| HU-006 | CA-02 | CP-002 | Funcional | Crítica | Sí | ☑ |
| HU-006 | CA-03 | CP-003 | Funcional | Alta | Sí | ☑ |
| HU-006 | CA-04 | CP-004 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 4 de 4 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · El freno

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Con la marca, pedir el motivo de `base/x.md`, `VERSION` y `CHANGELOG.md` en el estándar | Detenido, con la pantalla de Cimiento en el motivo |
| 2 | Sin la marca, o en otra carpeta | No se detiene por esto |

### CP-002 · El commit

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Con la marca, validar un commit con `base/x.md` | Falla |
| 2 | Con la marca, un commit con `plantillas/x.md` sin versión nueva en la base | Falla |
| 3 | El mismo, con una versión registrada después del último commit | Pasa |

### CP-003 · Congelar y descongelar

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Congelar | La marca queda y la versión de la base no queda por debajo de la de `VERSION` |
| 2 | Descongelar | La marca se va |

### CP-004 · Dónde leer las reglas completas

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir el texto de un mensaje con reglas que no caben | Dice `ver_estandar` con la ruta |
| 2 | Pedir la instrucción del arranque | Dice `ver_estandar` |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 4, en `resultado_pruebas.md`.
