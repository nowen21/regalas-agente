# Resultado de Pruebas · Fase `B-EP-025-HU-028-ningun-mensaje-sin-trabajo`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-025-HU-028-ningun-mensaje-sin-trabajo` |
| **HU** | [HU-028](../HU-028-el-trabajo-de-cada-mensaje-sale-de-lo-que-esta-abierto.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-08 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | La base de pruebas de Django y la base real de Cimiento; versión 58.0.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-005 | CA-05 | Alta | `tests_trabajo_abierto.NingunMensajeSinTrabajo` (4 pruebas) y el diagnóstico en la base real | Los pasos 1 a 4 pasan; en la base real quedan 0 de 3.669 mensajes sin trabajo | Aprobado | EV-01, EV-02 | Ninguno |

**Correspondencia con el plan:** 1 caso en el plan, 1 acá.

**Qué salió distinto de lo esperado:** el diagnóstico encontró que 159 de los mensajes sin trabajo eran de conversaciones sin sus líneas en la base. El vigilante corre desde el 2026-10-05 con el código de antes de la HU-025 y no guardó ninguna línea desde el 2026-10-06. Se trajeron con `leer_consumo --desde-cero` (124.017 líneas). Las 4 pruebas que esperaban «(sin trabajo)» se cambiaron a la regla nueva.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `proyectos\cimiento\.venv\Scripts\python.exe proyectos\cimiento\manage.py test core.consumo core.ayuda --noinput` | 105 pruebas, OK |
| 2 | La base real | `leer_consumo --desde-cero`, `recalcular_trabajo` y el diagnóstico | 0 de 3.669 sin trabajo |

## 4. Defectos encontrados

Ninguno de esta fase. El del vigilante viejo queda en los hallazgos del plan.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-05 | CP-005 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 1 de 1 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 1 de 1 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** ningún mensaje de la base queda sin trabajo, y las pruebas cubren los cuatro caminos.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/consumo/tests_trabajo_abierto.py` |
| EV-02 | Diagnóstico en la base real | `historico-chat/scripts/2026-10-08/salida_diagnostico_sin_trabajo.txt` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-08 | 1 | 0 | Primera ejecución |
