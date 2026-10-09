# Funcionalidad implementada · Fase `A-EP-029-HU-005-pruebas-de-navegador` (módulo Pruebas de Cimiento: `core/pruebas/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-029-HU-005-pruebas-de-navegador` |
| **Módulo** | Pruebas de Cimiento: `core/pruebas/`, con el instalador y las dependencias |
| **Especificación del módulo** | Los CA de la [HU-005](../HU-005-cimiento-corre-las-pruebas-de-navegador-de-cada-proyecto.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-005 (CA-01, CA-02, CA-03) |
| **Fecha de cierre** | 2026-10-08 |
| **Versión del estándar al cerrar** | 56.8.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Cada revisión corre también las pruebas de navegador del proyecto, si las tiene: con `npx playwright test` donde haya un `playwright.config`, o con el Python del proyecto para los archivos de prueba que usan Playwright. Guarda si pasaron, si fallaron o si no hay, y la lista de «Revisión de pruebas» lo muestra en la columna «Navegador». La instalación del estándar en su propia carpeta deja Playwright 1.63.0 y su Chromium en el ambiente de Cimiento; la desinstalación quita los navegadores.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Dominio | `core/pruebas/navegador.py`, `core/pruebas/revisar.py` | Hecho | CP-001 |
| CA-02 | Plantilla | `core/pruebas/templates/pruebas/lista.html` | Hecho | CP-002 |
| CA-03 | Instalador | `Instalador.preparar_playwright`, `Desinstalador.quitar_playwright`, `requirements/` | Hecho | CP-003 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 4 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

El botón «Revisar» corre también las pruebas de navegador; su resultado sale en la columna «Navegador» y en el detalle del proyecto. Para tener Playwright en Cimiento hay que volver a instalar el estándar en su propia carpeta.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| En Django, las pruebas de navegador se corren aparte | Así se sabe cuáles fallaron; se descartó sacarlo de la corrida de coverage.py | Ninguna |
| La desinstalación deja el paquete | Es una dependencia declarada de Cimiento (`10·DEP2`) | Ninguna |

## 6. Deuda técnica y pendientes generados

Ninguna. Se corrigió que `coverage run` dejaba `.coverage` en el proyecto revisado.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

`requirements/base.txt` y `requirements/lock.txt`; la sección «Revisión de pruebas» del manual.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Volver a instalar el estándar en su propia carpeta: baja Playwright y Chromium (varios cientos de megas, la primera vez).
