# Resultado de Pruebas · Fase `A-EP-025-HU-007-recepcion-de-la-telemetria`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-007-recepcion-de-la-telemetria` |
| **HU** | [HU-007](../HU-007-el-gasto-llega-a-cimiento-en-vivo.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-05 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Máquina local, rama `main`, sobre el commit `29a30ad` más los cambios sin guardar; base de pruebas y base real en MariaDB 11.4.9; versión 54.2.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `ElEnvioSeLee` (3 pruebas), `UnaLlamadaLlegaYQuedaGuardada` (3) y un envío a Cimiento prendido en el puerto 8001 | La llamada con modelo, tokens y solicitud, y el archivo con ruta y 300 bytes, en la base con su proyecto; comprimido con gzip también; el envío manual respondió 200 con `{}` y quedó en «Estándar de Agente», y esa fila de prueba se borró | Aprobado | EV-01, EV-02 | Ninguno |
| CP-002 | CA-02 | Media | `LoQueNoValeNoSeGuarda` (5 pruebas) | Otra máquina: 403; JSON roto: 400; sesión sin proyecto o con `../`: 200 y nada guardado; `GET`: 405 | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Alta | `LaMismaLlamadaCuentaUnaVez` (4 pruebas) | Una llamada en los dos órdenes, con el `message.id` del `.jsonl`; el mismo envío dos veces deja una llamada y un archivo; el `.jsonl` deja el archivo en 70 caracteres | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-04 | Media | `ActivarLaTelemetria` (6 pruebas) y la configuración real | Las seis variables, con `http://127.0.0.1:8015/v1/logs`; lo del usuario sigue; otra vez no cambia nada; en simulación no escribe; sin puerto, el 8000; JSON roto no se toca. En `~/.claude/settings.json` quedaron las seis, y la simulación del instalador dice «ya estaba activa» | Aprobado | EV-01, EV-03 | Ninguno |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** el envío manual fue al 8001, donde se había levantado Cimiento a mano; la configuración apunta al 8015, el `PUERTO` del `.env`.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | La migración en la base real | `manage.py preparar_base` | Sin migraciones pendientes |
| 2 | Que lo de la HU-006 siga andando | `manage.py test core.consumo` | 27 pruebas, todas pasan |
| 3 | Las pruebas del instalador que tocó la fase | `ActivarLaTelemetria`, `LaLecturaDelConsumoQuedaProgramada`, `PrepararCimiento` | 18 pruebas, todas pasan |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| CA-04 | CP-004 | Aprobado | Sí |
| RNF-01 | CP-002 | Solo desde `127.0.0.1` o `::1` | Sí |
| RNF-02 | CP-001 | `test_no_guarda_texto` | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 4 de 4 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 4 de 4 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los cuatro criterios pasan en la base de pruebas, y un envío real llegó a Cimiento prendido.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/consumo/tests_telemetria.py` (15 pruebas) y `proyectos/cimiento/core/herramientas/tests_instalacion.py` |
| EV-02 | Base real | El envío manual, guardado y borrado |
| EV-03 | Configuración | El bloque `env` de `~/.claude/settings.json` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-05 | 4 | 0 | Primera ejecución |
