# Resultado de Pruebas · Fase `A-EP-025-HU-012-retirar-la-telemetria`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-012-retirar-la-telemetria` |
| **HU** | [HU-012](../HU-012-la-telemetria-se-retira.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-05 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Máquina local, rama `main`, sobre el commit `2c3b67b` más los cambios sin guardar; base de pruebas en MariaDB 11.4.9; versión 55.0.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `LaTelemetriaYaNoEsta` y `manage.py test core.consumo` (41) | `/v1/logs` ya no resuelve y `telemetria.py` no está; las pruebas de consumo pasan sin el lector de la telemetría | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `LaTelemetriaSeRetira` (5) | Salen las seis con su valor y se quedan la que tenía otro valor y las demás del usuario; sin nada más se va el `env`; la segunda vez no hay nada; la simulación no escribe; un JSON roto no se toca | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 2 casos en el plan, 2 acá.

**Qué salió distinto de lo esperado:** nada.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `cd proyectos\cimiento && .venv\Scripts\python.exe manage.py test core.consumo && python -m unittest core.herramientas.tests_instalacion core.herramientas.tests_desinstalar` | Ran 237 tests in 38.361s, OK |
| 2 | En esta máquina | `Instalador().retirar_telemetria(True)` | Salieron 6 variables; quedaron `agentPushNotifEnabled`, `permissions` y `remoteControlAtStartup` |
| 3 | Que Django arranque sin la ruta | `manage.py check` | Sin problemas |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 2 de 2 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 2 de 2 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los dos criterios pasan, y en esta máquina salieron las seis variables de `~/.claude/settings.json` con lo demás del usuario intacto.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/consumo/tests_vigilante.py` y `proyectos/cimiento/core/herramientas/tests_instalacion.py` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-05 | 2 | 0 | Primera ejecución |
