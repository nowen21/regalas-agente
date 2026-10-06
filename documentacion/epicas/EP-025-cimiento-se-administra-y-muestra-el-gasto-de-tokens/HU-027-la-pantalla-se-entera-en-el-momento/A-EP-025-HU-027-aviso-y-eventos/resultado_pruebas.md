# Resultado de Pruebas · Fase `A-EP-025-HU-027-aviso-y-eventos`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-027-aviso-y-eventos` |
| **HU** | [HU-027](../HU-027-la-pantalla-se-entera-en-el-momento.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-06 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Cimiento local con MariaDB, sobre `ae82d18` con los cambios de las fases sin guardar; versión 55.5.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | `ElAvisoDespiertaSinReloj`: un hilo espera, otro avisa; el flujo SSE tras un aviso; y la búsqueda de relojes en `avisos.py`, `vigilante.py` y `tablero.html` | El que esperaba despertó con el número nuevo, el flujo trajo `event: gasto` y no hay `sleep(`, `every ` ni `setInterval` | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-01 | Crítica | `ElVigilanteAvisa`: un `.jsonl` con gasto, el mismo sin nada nuevo, y un aviso a un puerto cerrado | Avisó una vez y no la segunda; al puerto cerrado devolvió `False` en menos de 2,5 s | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-01 | Alta | `LasRutas.test_la_pantalla_escucha_los_eventos` y `test_los_eventos_piden_cuenta`; y con Cimiento prendido en el 8015, `curl` a `/gasto/eventos/` sin cuenta | La página trae `new EventSource("/gasto/eventos/")`; los eventos dan 200 `text/event-stream` con cuenta y 302 sin ella, también en el Cimiento prendido | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-02 | Crítica | `LasRutas.test_el_aviso_desde_esta_maquina_sin_cuenta` y `test_el_aviso_desde_otra_maquina_o_por_get_se_rechaza`; y `curl -X POST` al 8015 | 204 desde 127.0.0.1 sin cuenta y el número subió; 403 desde 10.0.0.5, 405 por GET, sin cambio; el Cimiento prendido respondió 204 | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** No se vio en un navegador la franja cambiando sola con una sesión de Claude Code: pide entrar con una cuenta, y queda para el usuario.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `.venv\Scripts\python.exe manage.py test core.consumo` | Ran 73 tests in 10.531s, OK |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001, CP-002, CP-003 | Aprobado | Sí |
| CA-02 | CP-004 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 2 de 2 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 4 de 4 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** Los dos criterios tienen sus casos aprobados y `core.consumo` pasa 73 de 73; falta ver con los ojos la pantalla cambiando sola.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `core/consumo/tests_en_vivo.py` y la salida de §3 |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-06 | 4 | 0 | Primera ejecución |
