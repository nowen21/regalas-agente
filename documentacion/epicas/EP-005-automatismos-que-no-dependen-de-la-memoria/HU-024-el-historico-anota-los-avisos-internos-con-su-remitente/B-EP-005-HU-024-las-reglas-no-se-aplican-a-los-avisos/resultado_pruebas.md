# Resultado de Pruebas · Fase `B-EP-005-HU-024-las-reglas-no-se-aplican-a-los-avisos`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-005-HU-024-las-reglas-no-se-aplican-a-los-avisos` |
| **HU** | [HU-024](../HU-024-el-historico-anota-los-avisos-internos-con-su-remitente.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-06 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Cimiento local, sobre `ae82d18` con los cambios de las fases sin guardar; versión 55.6.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-02 | Crítica | `LasReglasNoSeAplicanAlAviso`: un `<task-notification>`, un `<agent-message` y «hola» | Los dos avisos devolvieron `""`; «hola» siguió trayendo el aviso de `01·C28` | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 1 casos en el plan, 1 acá.

**Qué salió distinto de lo esperado:** Nada.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `.venv\Scripts\python.exe manage.py test core.herramientas.tests_avisos_internos core.enganches.tests_sesion` | Ran 133 tests in 5.161s, OK |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-02 | CP-001 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 1 de 1 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 1 de 1 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** El enganche de reglas no le aplica nada a los avisos internos, y `tests_sesion` sigue en verde: 133 de 133.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `core/herramientas/tests_avisos_internos.py` y la salida de §3 |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-06 | 1 | 0 | Primera ejecución |
