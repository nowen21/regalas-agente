# Resultado de Pruebas · Fase `A-EP-026-HU-004-leer-de-la-base`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-026-HU-004-leer-de-la-base` |
| **HU** | [HU-004](../HU-004-los-enganches-leen-el-estandar-de-la-base.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-06 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Cimiento en la máquina local con la base de pruebas de Django sobre MariaDB, y la base real para la sincronización; versión 56.2.1 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | 2026-10-06 | `test_cp001_lo_que_dice_la_base_es_lo_que_se_lee` y `test_cp001_el_orden_es_el_de_la_carpeta` | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Crítica | 2026-10-06 | `test_cp002_sin_base_se_dice_y_no_se_autoriza`: reglas, autorizaciones y arranque con la base apagada | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Alta | 2026-10-06 | `test_cp003_las_mismas_reglas`: seis mensajes, mismo texto leyendo de la base y del disco | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-04 | Alta | 2026-10-06 | `SincronizarConGit`: un documento cambiado a mano vuelve a lo de git en una versión nueva; sin diferencias, no sube | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** el código de la HU-004 se escribió una vez antes de abrir la fase y el freno lo detuvo (H-7); se volvió a escribir con la fase abierta. La lectura desde la base quedó encendida al instalar el código, porque la base ya tenía el estándar; se sincronizó en seguida: 3 documentos y la versión 56.2.0, con «Liste» y «OK»

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `.venv\Scripts\python.exe manage.py test core.estandar --noinput` | Ran 8 tests in 41.830s, OK |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| CA-04 | CP-004 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 4 de 4 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 4 de 4 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los cuatro criterios tienen su caso aprobado: 8 pruebas de `core.estandar` y 908 en la regresión de lo que usa los lectores cambiados, sin fallas.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `manage.py test core.estandar`: 8 OK; regresión `core.estandar core.validadores core.niveles core.herramientas.tests_respondo core.enganches.tests_freno core.enganches.tests_sesion`: 908 OK, 4 saltadas; `sincronizar_estandar` real: 3 cambiados, 56.2.0 |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-06 | 4 | 0 | Primera ejecución |
