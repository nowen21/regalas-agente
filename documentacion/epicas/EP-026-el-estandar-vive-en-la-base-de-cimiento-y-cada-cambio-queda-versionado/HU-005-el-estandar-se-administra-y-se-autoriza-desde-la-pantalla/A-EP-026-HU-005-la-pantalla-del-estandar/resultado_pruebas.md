# Resultado de Pruebas · Fase `A-EP-026-HU-005-la-pantalla-del-estandar`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-026-HU-005-la-pantalla-del-estandar` |
| **HU** | [HU-005](../HU-005-el-estandar-se-administra-y-se-autoriza-desde-la-pantalla.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-06 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Cimiento en la máquina local con la base de pruebas de Django sobre MariaDB, con el estándar importado en la prueba; versión 56.2.1 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 5 | 5 | 5 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | 2026-10-06 | `CambiarUnDocumento`: «tocar-git» en la línea «Aplica a» de `C29`, MENOR, y `C29` en `reglas-por-tarea/tocar-git.md` en la misma versión | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | 2026-10-06 | `CrearYQuitar`: crear `base/anexo-prueba.md`, negar `plantillas/x.md`, quitar con borrado en la historia | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Alta | 2026-10-06 | `LaMemoria`: el recuerdo cambiado sube la versión del proyecto, y el arranque lee el índice de la base | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-04 | Crítica | 2026-10-06 | `LasPropuestas`: `proponer` deja pendiente; aprobar aplica y anota quién; rechazar no cambia nada | Aprobado | EV-01 | Ninguno |
| CP-005 | CA-05 | Crítica | 2026-10-06 | `ConsultaYLectura`: 403 al guardar y quitar con consulta; `ver_estandar` imprime el texto de la base | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 5 casos en el plan, 5 acá.

**Qué salió distinto de lo esperado:** nada: los cinco casos pasaron en la primera corrida. Antes, el freno detuvo una plantilla de mensajes que el plan no nombraba (H-8); se sumó al plan

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `.venv\Scripts\python.exe manage.py test core.estandar --noinput` | Ran 13 tests in 72.950s, OK |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| CA-04 | CP-004 | Aprobado | Sí |
| CA-05 | CP-005 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 5 de 5 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 5 de 5 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los cinco criterios tienen su caso aprobado: 5 pruebas de la pantalla y 174 en la regresión de `core.estandar core.ayuda core.enganches.tests_sesion core.historia`.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `manage.py test core.estandar.tests_pantalla`: 5 OK; regresión: 174 OK |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-06 | 5 | 0 | Primera ejecución |
