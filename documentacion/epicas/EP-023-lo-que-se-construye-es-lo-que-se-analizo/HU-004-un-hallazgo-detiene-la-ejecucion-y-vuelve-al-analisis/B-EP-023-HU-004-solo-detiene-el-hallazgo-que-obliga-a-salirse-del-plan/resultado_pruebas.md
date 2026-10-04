# Resultado de Pruebas · Fase `B-EP-023-HU-004-solo-detiene-el-hallazgo-que-obliga-a-salirse-del-plan`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-023-HU-004-solo-detiene-el-hallazgo-que-obliga-a-salirse-del-plan` |
| **HU** | [HU-004](../HU-004-un-hallazgo-detiene-la-ejecucion-y-vuelve-al-analisis.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-03 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Repositorio del estándar en la máquina local, rama `main`, sobre el commit `2f1b9ab` más los cambios sin guardar, versión 52.1.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-08 | Alta | Lectura de `02·F9`, `13·DOC24` y la nota de `plantillas/analisis.md` | La excepción de `02·F9` detiene solo el hallazgo que obliga a tocar algo que el plan no declara; el otro se anota con su pendiente y el trabajo sigue. `13·DOC24` y la plantilla dicen que solo ese abre el análisis siguiente | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-08 | Media | `mapa_tareas.py`, `validar.py estandar` y `tareas`, y `test_cada_tarea_sabe_que_reglas_le_aplican.py` (17 pruebas) | La copia de `13·DOC24` en `escribir-documento-2.md` quedó al día; la de `02·F9` en `trabajar-cadena-2.md` no lleva la excepción y no cambió; sin fallas | Aprobado | EV-02 | Ninguno |

**Correspondencia con el plan:** 2 casos en el plan, 2 acá.

**Qué salió distinto de lo esperado:** `base/reglas-por-tarea/trabajar-cadena-2.md` no cambió, porque copia solo el enunciado de `02·F9`, sin su excepción.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Marcas de `00·ID8` en lo que escribió la fase | `marcas.py` | Ninguna nueva |
| 2 | Sellos de las reglas editadas | Checklist contra 52.1.0 | `02·F9` y `13·DOC24` cumplen |

## 4. Defectos encontrados

Ninguno en esta fase.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-08 | CP-001, CP-002 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 1 de 1 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 2 de 2 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple. Aprobada por el usuario el 2026-10-03.

**Justificación:** el CA-08 tiene sus dos casos ejecutados y aprobados.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Reglas y plantilla | `base/02-flujo-de-trabajo/reglas/F9-no-subdividas-ni-renegocies-un-plan-ya-aprobado.md`, `base/13-documentacion/reglas/DOC24-cierra-el-analisis-en-su-mismo-archivo.md`, `plantillas/analisis.md` |
| EV-02 | Copia generada | `base/reglas-por-tarea/escribir-documento-2.md` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-03 | 2 | 0 | Primera ejecución |
