# Resultado de Pruebas · Fase `A-EP-030-HU-001-camino-unico-y-comando-documento`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-030-HU-001-camino-unico-y-comando-documento` |
| **HU** | [HU-001](../HU-001-un-solo-camino-para-leer-y-escribir-documentos-con-un-comando-fijo-por-tipo.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 2 |
| **Fecha de ejecución** | 2026-10-09 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Cimiento en la máquina local, base de pruebas de Django sobre MariaDB; versión 56.8.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 2 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | 2026-10-09 | `ListarYVer`: lista, muestra el texto exacto, muestra un recuerdo y da error con lo que no está | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-01 | Crítica | 2026-10-09 | `CrearEditarQuitar`: crear, editar y quitar dejan propuesta sin cambiar nada; error al crear lo que existe, sin motivo y con un tipo que no existe | Aprobado | EV-01 | D-01, corregido |
| CP-003 | CA-02 | Alta | 2026-10-09 | `LasOrdenesDeAntesUsanElCamino`: `ver_estandar`, `ver_recuerdo` y `proponer` dan lo mismo que `documento` | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-03 | Alta | 2026-10-09 | `LaHistoria`: aprobar deja en `Cambio` el texto de antes y el de después | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** en el ciclo 1, la base de prueba compartida falló al crearse (bloqueos y tablas faltantes) mientras otra sesión corría sus pruebas; falló igual con una prueba que no toca esta fase. Con la base libre, todo pasó.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase y las vecinas que usan las órdenes cambiadas | `manage.py test core.estandar.tests_documentos core.estandar.tests_pantalla core.estandar.tests_congelado core.estandar.tests_texto_desde_tablas core.estandar.tests_en_base` | Ran 37 tests in 195.747s, OK |
| 2 | La consulta del aviso y el comando nuevo en la base real | `ver_estandar base/01-conducta/palabras-clave.md`, `documento tipos`, `documento listar recuerdo --proyecto …` | Responden; 33 recuerdos |

## 4. Defectos encontrados

| ID | Defecto | Causa | Corrección |
|---|---|---|---|
| D-01 | `test_crear_un_recuerdo_deja_la_propuesta` esperaba `\n` y recibía `\r\n` | La prueba escribía su archivo temporal con el salto de línea de Windows | La prueba escribe con `newline=""` |

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001, CP-002 | Aprobado | Sí |
| CA-02 | CP-003 | Aprobado | Sí |
| CA-03 | CP-004 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §5 | 100% | 3 de 3 | Sí |
| Casos ejecutados | Plan §12 | 100% | 4 de 4 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios tienen su caso aprobado: 37 pruebas en verde, entre ellas las 16 de la fase, y el comando responde en la base real.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Pruebas | `historico-chat/scripts/2026-10-08/salida_pruebas_ep030_hu001.txt`: 37 OK |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-08 | 15 de 16 de la fase | 1, y las vecinas sin poder crear la base | Se corrigió D-01; la base de prueba quedó libre |
| 2 | 2026-10-09 | 4 | 0 | |
