# Resultado de Pruebas · Fase `A-EP-029-HU-006-sin-interfaz`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-029-HU-006-sin-interfaz` |
| **HU** | [HU-006](../HU-006-el-visor-viejo-interfaz-sale-del-estandar.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-08 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | El repositorio real; versión 59.0.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 0 | 0 | 0 |

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `ElVisorViejoSalio` | La carpeta no existe; nada vivo la nombra; el estándar se reconoce como Django en `proyectos/cimiento` | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 1 caso en el plan, 1 acá.

**Qué salió distinto de lo esperado:** borrar la carpeta dejó 6 enlaces rotos en archivos que el plan no nombraba (H-8). El análisis 5 del pendiente 141 los sumó al plan y quedaron como texto; `validar.py estandar` ya no reporta ninguno a `interfaz/`.

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| RNF-01 | `git rm`: la carpeta queda en la historia de git | Aprobado | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** el criterio tiene su caso aprobado.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `manage.py test core.pruebas.tests_un_programa`: Ran 3 tests, OK |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-08 | 1 | 0 | Primera ejecución; aparecieron los enlaces rotos |
| 2 | 2026-10-08 | 1 | 0 | Los 6 enlaces quedaron como texto |
