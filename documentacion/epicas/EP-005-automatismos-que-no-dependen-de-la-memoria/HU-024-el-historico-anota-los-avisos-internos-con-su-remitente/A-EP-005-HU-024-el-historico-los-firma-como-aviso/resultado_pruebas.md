# Resultado de Pruebas · Fase `A-EP-005-HU-024-el-historico-los-firma-como-aviso`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-005-HU-024-el-historico-los-firma-como-aviso` |
| **HU** | [HU-024](../HU-024-el-historico-anota-los-avisos-internos-con-su-remitente.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-06 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Cimiento local, sobre `ae82d18` con los cambios de las fases sin guardar; versión 55.6.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | `test_los_dos_avisos_quedan_como_aviso_del_sistema`: un `<task-notification>` y un `<agent-message` | Los dos quedaron `### N · Aviso del sistema`, con su texto, y ninguno como «Usuario» | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-01 | Alta | `test_el_mensaje_del_usuario_sigue_igual` y `test_reconoce_solo_lo_que_abre_con_la_marca` | «Hágalo» y un texto que nombra `<agent-message` en la mitad quedaron como «Usuario»; solo lo que abre con la marca es aviso | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 2 casos en el plan, 2 acá.

**Qué salió distinto de lo esperado:** Nada.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `.venv\Scripts\python.exe manage.py test core.enganches.tests_avisos_internos core.enganches.tests_sesion` | Ran 134 tests in 4.389s, OK |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001, CP-002 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 1 de 1 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 2 de 2 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** El histórico firma los avisos con su remitente y sus pruebas pasan, 134 de 134 con las de `tests_sesion`.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `core/enganches/tests_avisos_internos.py` y la salida de §3 |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-06 | 2 | 0 | Primera ejecución |
