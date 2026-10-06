# Resultado de Pruebas · Fase `A-EP-025-HU-023-desde-un-turno-y-en-la-base`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-023-desde-un-turno-y-en-la-base` |
| **HU** | [HU-023](../HU-023-el-analisis-se-prende-desde-un-turno-anterior.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-05 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Máquina local, rama `main`, sobre el commit `2c3b67b` más los cambios sin guardar; base de pruebas y base real en MariaDB 11.4.9; versión 55.0.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `ElAnalisisSePrendeDesdeUnTurnoAnterior` (6) | El mensaje da el turno; prende desde el 4 en el turno 12; ya prendido desde el 10 pasa al 4; el 0 y el 13 se rechazan; sin «desde» sigue igual; la conversación entra desde el turno 4 y no el 3 | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `ElEstadoViveEnLaBase` (6), con la base de pruebas | Prender escribe la fila y ningún archivo; pausar y borrar cambian la fila; sin sesión se lee la más reciente; el archivo pasa a la base y se borra; un proyecto sin registro no tiene fila; sin base sigue en archivo | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 2 casos en el plan, 2 acá.

**Qué salió distinto de lo esperado:** al aplicar la migración en la base real, el primer enganche que corrió pasó solo a la base el estado del análisis 1 del pendiente 116, que estaba en el archivo único, y borró el archivo.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `cd proyectos\cimiento && python -m unittest core.enganches.tests_analisis_desde core.enganches.tests_analisis_en_curso && .venv\Scripts\python.exe manage.py test core.proyectos.tests_analisis_prendido` | Ran 6 tests in 10.097s, OK |
| 2 | Que lo demás siga | `core.enganches.tests_freno` y `manage.py migrate proyectos` en la base real | 322 pruebas pasan; la `0003` aplicada; la fila del análisis del 116 quedó en la tabla |

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

**Justificación:** los dos criterios pasan; `tests_analisis_en_curso` (7) y `tests_freno` (322) siguen en verde, y el estado ya vive en la base real.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/enganches/tests_analisis_desde.py` (6) y `proyectos/cimiento/core/proyectos/tests_analisis_prendido.py` (6) |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-05 | 2 | 0 | Primera ejecución |
