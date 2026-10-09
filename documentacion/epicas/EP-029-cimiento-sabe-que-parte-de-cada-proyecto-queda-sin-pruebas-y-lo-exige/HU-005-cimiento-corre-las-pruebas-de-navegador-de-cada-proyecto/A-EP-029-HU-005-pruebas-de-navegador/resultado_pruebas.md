# Resultado de Pruebas · Fase `A-EP-029-HU-005-pruebas-de-navegador`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-029-HU-005-pruebas-de-navegador` |
| **HU** | [HU-005](../HU-005-cimiento-corre-las-pruebas-de-navegador-de-cada-proyecto.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-08 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | La base de pruebas de Django sobre MariaDB; `npx`, pip y Playwright simulados; versión 56.8.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `LaRevisionCorreLasPruebasDeNavegador` | «pasaron» con 3; «fallaron»; Django corre `app.tests_pantallas` con su Python; sin ninguna, nada | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `ElResultadoSaleEnLaPagina` | La fila dice «Pasaron» | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Alta | `PlaywrightEnCimiento` | Instala `playwright==1.63.0` y Chromium; quita los navegadores; las cuatro versiones exactas en `lock.txt` | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá.

**Qué salió distinto de lo esperado:** al cerrar la épica apareció que `coverage run` dejaba un archivo `.coverage` dentro del proyecto revisado. Se corrigió en `revisar.py` (los datos van a la carpeta temporal) y lo prueba `LosDatosDeCoverageNoQuedanEnElProyecto`; `core.pruebas` volvió a pasar entera, 50 pruebas.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las versiones exactas de Playwright y sus dependencias | `pip install playwright==1.63.0 --dry-run` | greenlet 3.5.6, playwright 1.63.0, pyee 13.0.1, typing_extensions 4.16.0 |

## 4. Defectos encontrados

El `.coverage` suelto en el proyecto revisado, de la HU-002, corregido en esta fase.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| RNF-01 | CP-003, paso 3 | Aprobado | Sí |
| RNF-02 | Los textos de `navegador.py` | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios tienen su caso aprobado y la regresión pasa entera.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `manage.py test core.pruebas core.ayuda core.inicio core.herramientas.tests_instalacion`: Ran 313 tests, OK |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-08 | 3 | 0 | Primera ejecución |
