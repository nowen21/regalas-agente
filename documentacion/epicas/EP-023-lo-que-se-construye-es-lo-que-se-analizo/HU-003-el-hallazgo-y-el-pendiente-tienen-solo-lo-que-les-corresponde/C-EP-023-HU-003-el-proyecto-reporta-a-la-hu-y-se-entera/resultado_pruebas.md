# Resultado de Pruebas · Fase `C-EP-023-HU-003-el-proyecto-reporta-a-la-hu-y-se-entera`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `C-EP-023-HU-003-el-proyecto-reporta-a-la-hu-y-se-entera` |
| **HU** | [HU-003](../HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-03 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Repositorio del estándar en la máquina local, rama `main`, sobre el commit `372c94e` más los cambios sin guardar, versión 53.0.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-10 | Alta | Lectura de `02·F24` y de las dos plantillas | La regla dice dónde nace el pendiente reportado y cuándo cierra el seguimiento; las plantillas dicen dónde se crea cada uno y que el seguimiento cierra al comprobar | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-11 | Alta | `test_el_proyecto_reporta_y_se_entera.py` (4 pruebas) | Sin el plan cumplido no escribe; cumplido, escribe el aviso al lado del seguimiento; no lo duplica; con el enlace roto no escribe y nombra el hallazgo | Aprobado | EV-02 | Ninguno |
| CP-003 | CA-11 | Alta | `test_el_proyecto_reporta_y_se_entera.py` (2 pruebas) | Con «Comprobado: no» el seguimiento sigue abierto; con la fecha, cierra | Aprobado | EV-02 | Ninguno |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá.

**Qué salió distinto de lo esperado:** la prueba del seguimiento de la fase A esperaba el cierre con el padre, sin aviso. Se puso al día bajo la fila 8 del análisis 14 del pendiente 103.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Coherencia del estándar y copias por tarea | `validar.py estandar`, `tareas`, `flujo` y `origen`, y `mapa_tareas.py` | Sin fallas |
| 2 | Que lo demás de los pendientes siga andando | Las 67 pruebas que llaman una función `estado` | Pasan |
| 3 | Las pruebas de `validadores/pruebas.py` | 571 pruebas | Pasan. Una, que esperaba que la falta de `pendientes/` fuera falla, se puso al día bajo la fila 10 del análisis 14 |

## 4. Defectos encontrados

Ninguno en esta fase.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-10 | CP-001 | Aprobado | Sí |
| CA-11 | CP-002, CP-003 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 2 de 2 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 3 de 3 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple. Aprobada por el usuario el 2026-10-03.

**Justificación:** el CA-10 y el CA-11 tienen sus casos ejecutados y aprobados.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Regla y plantillas | `02·F24`, `plantillas/pendiente-reportado.md`, `plantillas/pendiente-de-seguimiento.md` |
| EV-02 | Programas, enganche y pruebas | `validadores/aviso_resuelto.py`, `validadores/pendientes.py`, `adaptadores/claude-code/hook_estacion.py`, `validadores/tests/test_el_proyecto_reporta_y_se_entera.py` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-03 | 3 | 0 | Primera ejecución |
