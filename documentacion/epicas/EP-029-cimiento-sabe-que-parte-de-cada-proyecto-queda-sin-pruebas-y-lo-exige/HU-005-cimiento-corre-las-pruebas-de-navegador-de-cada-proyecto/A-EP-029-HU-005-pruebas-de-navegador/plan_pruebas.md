# Plan de Pruebas · Fase A-EP-029-HU-005, pruebas de navegador   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP029-HU005-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-005](../HU-005-cimiento-corre-las-pruebas-de-navegador-de-cada-proyecto.md) |
| **Fecha** | 2026-10-08 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 141](../../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

`npx`, pip y Playwright se simulan (`08·T3`): ninguna prueba abre un navegador ni baja nada. La salida simulada de `npx playwright test --reporter=json` sigue la documentación de Playwright.

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.pruebas core.ayuda core.inicio core.herramientas.tests_instalacion`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-005 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-005 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |
| HU-005 | CA-03 | CP-003 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 3 de 3 exigencias cubiertas = 100%.

## 6. Casos de prueba

### CP-001 · La revisión corre las pruebas de navegador

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Carpeta con `playwright.config.ts` y salida con 3 esperadas y 0 inesperadas | «pasaron», con «3» en el detalle |
| 2 | La misma con 1 inesperada | «fallaron» |
| 3 | Django con `app/tests_pantallas.py` que importa Playwright | Se corre `manage.py test app.tests_pantallas` con el Python del proyecto |
| 4 | Carpeta sin ninguna | «sin pruebas de navegador», sin correr nada |

### CP-002 · El resultado sale en la página

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Revisión con navegador «pasaron» | La fila dice «Pasaron» |

### CP-003 · Playwright en Cimiento

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Preparar Playwright sin el paquete | Se pide instalar `playwright==1.63.0` y después `playwright install chromium` |
| 2 | Quitarlo | Se pide `playwright uninstall --all` |
| 3 | Las dependencias | `base.txt` trae playwright y `lock.txt` sus cuatro versiones exactas |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 3, en `resultado_pruebas.md`.
