# Resultado de Pruebas · Fase `A-EP-026-HU-010-la-copia-diaria`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-026-HU-010-la-copia-diaria` |
| **HU** | [HU-010](../HU-010-la-base-se-copia-sola-en-una-carpeta-hermana-de-agente.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-06 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Cimiento en la máquina local con la base de pruebas de Django sobre MariaDB y la base real para la copia de verdad; versión 56.1.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | 2026-10-06 | `test_cp001`: la copia de un día con sus tablas, y `hay_de_hoy` | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | 2026-10-06 | `test_cp002`: 8 copias viejas más la de hoy dejan 7 | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Crítica | 2026-10-06 | `test_cp003`: la copia trae la tabla de sesiones sin filas y `probar` la restaura en una base aparte que después no existe | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá.

**Qué salió distinto de lo esperado:** la primera copia de la base real pesó 437 MB por el gasto de tokens; se comprimió con gzip y quedó en 97 MB. La base real se copió y se restauró: 27 tablas, 153.834 filas. El agente quiso borrar a mano la primera copia y el freno lo detuvo (H-6); la quitó la poda del programa

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `.venv\Scripts\python.exe manage.py test core.historia --noinput` | Ran 19 tests in 30.666s, OK |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 3 de 3 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 3 de 3 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios tienen su caso aprobado: 19 pruebas de `core.historia` en verde, y la copia de la base real se escribió y se restauró.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `manage.py test core.historia`: 19 OK; `manage.py copiar_base` y `manage.py probar_copia` sobre la base real: 27 tablas, 153.834 filas |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-06 | 3 | 0 | Primera ejecución |
