# Plan de Pruebas · Fase A-EP-025-HU-032, el catálogo y la pantalla   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU032-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-032](../HU-032-cada-momento-de-cada-enganche-y-cada-revision-de-git-se-puede-suspender.md) |
| **Fecha** | 2026-10-09 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 149](../../../../../historico-chat/resumenes/2026-10-08/pendientes/149-cada-enganche-se-puede-suspender-desde-cimiento/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Desde `proyectos/cimiento/`: `manage.py test core.proyectos.tests_suspender_enganches core.proyectos.tests_configuracion core.ayuda`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-032 | CA-01 | CP-001 | Funcional | Crítica | Sí | ☑ |
| HU-032 | CA-01 | CP-002 | Funcional | Crítica | Sí | ☑ |

**Cobertura:** 1 de 1 exigencias cubiertas = 100 %.

## 6. Casos de prueba

### CP-001 · El catálogo nombra todo

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Revisar cada `(evento, guion)` de `HOOKS_CLAUDE` y cada revisión de git | Todos tienen nombre; los dos del freno se llaman «freno»; ningún otro nombre se repite |

### CP-002 · La pantalla deja suspender cualquiera

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Suspender `historico-del-usuario` con motivo y vencimiento | Se guarda con ese nombre |
| 2 | Suspender `git-versionado` | Se guarda |
| 3 | Suspender un nombre que no está en el catálogo | Se rechaza |
| 4 | Un enganche sin nombre | Se guarda como «freno», como hoy |
| 5 | Abrir la pantalla | Sale lo que se puede suspender, con la recomendación junto al histórico |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 2, en `resultado_pruebas.md`.
