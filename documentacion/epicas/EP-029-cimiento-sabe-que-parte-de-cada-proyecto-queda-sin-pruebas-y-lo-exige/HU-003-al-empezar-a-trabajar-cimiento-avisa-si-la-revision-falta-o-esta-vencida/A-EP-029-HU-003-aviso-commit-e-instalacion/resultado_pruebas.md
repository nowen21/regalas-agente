# Resultado de Pruebas · Fase `A-EP-029-HU-003-aviso-commit-e-instalacion`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-029-HU-003-aviso-commit-e-instalacion` |
| **HU** | [HU-003](../HU-003-al-empezar-a-trabajar-cimiento-avisa-si-la-revision-falta-o-esta-vencida.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 2 |
| **Fecha de ejecución** | 2026-10-08 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | La base de pruebas de Django sobre MariaDB, leída también sin Django; pip simulado; versión 56.8.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 2 | 5 | 5 | 5 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `AvisaLoQueFalta` | «hace 12 días» y «Toca hacer otra»; nunca; sin la parte; al día, nada | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-01 | Alta | `CallaCuandoNoCorresponde` | Con «nada» y sin registro, nada; el arranque trae el aviso | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-02 | Alta | `ElCommit` | «no dejar guardar» sale con 1; «solo avisar» con 0; la plantilla lo llama | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-03 | Alta | `ElInstaladorPoneCoverage` | Le falta: se instala y queda puesta por Cimiento; ya la tenía: no; sin lenguaje: nada | Aprobado | EV-01 | Ninguno |
| CP-005 | CA-03 | Alta | `ElDesinstaladorQuitaSoloLoSuyo` | Quita la que puso Cimiento; deja la del proyecto; marcar y quitar | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 5 casos en el plan, 5 acá.

**Qué salió distinto de lo esperado:** en el ciclo 1, las pruebas que leen la base sin Django la vaciaban al terminar y rompían la preparación de `tests_reglas_del_proyecto`; se les puso `serialized_rollback`, como al resto de Cimiento.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que Django no pida más migraciones | `manage.py makemigrations --check --dry-run` | No changes detected |

## 4. Defectos encontrados

El de §2, corregido. Fuera de la fase, la regresión muestra tres fallas ajenas: la del pendiente 140 (`tests_freno`) y dos de `tests_validar` que causa el enlace roto del pendiente 142, de otra sesión.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001, CP-002 | Aprobado | Sí |
| CA-02 | CP-003 | Aprobado | Sí |
| CA-03 | CP-004, CP-005 | Aprobado | Sí |
| RNF-01 | `RevisionDelProyecto` hace una sola conexión | Aprobado | Sí |
| RNF-02 | CP-002, sin registro | Aprobado | Sí |
| RNF-03 | Los textos de `aviso.py` y `parte.py` | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios tienen sus casos aprobados; de 861 pruebas de regresión fallan 3, ajenas a la fase.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `manage.py test core.pruebas core.enganches core.herramientas`: Ran 861 tests, 3 fallas ajenas (pendientes 140 y 142); `core.pruebas core.enganches.tests_reglas_del_proyecto`: Ran 46 tests, OK |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-08 | 5 | 0 | La regresión mostró el vaciado de la base |
| 2 | 2026-10-08 | 5 | 0 | `serialized_rollback` |
