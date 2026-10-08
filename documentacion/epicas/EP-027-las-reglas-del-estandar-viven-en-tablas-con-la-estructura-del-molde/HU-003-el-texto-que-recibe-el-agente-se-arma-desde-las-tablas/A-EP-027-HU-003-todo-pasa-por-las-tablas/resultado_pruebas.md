# Resultado de Pruebas · Fase `A-EP-027-HU-003-todo-pasa-por-las-tablas`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-027-HU-003-todo-pasa-por-las-tablas` |
| **HU** | [HU-003](../HU-003-el-texto-que-recibe-el-agente-se-arma-desde-las-tablas.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-07 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | La base de pruebas de Django, con el estándar importado de `base/` y pasado a las tablas; versión 57.4.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `CambiarPasaPorLasTablas` (3 pruebas) | Desde la pantalla, al aprobar una propuesta y al sincronizar con git, la fila toma el cambio y el texto guardado es el armado | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `NadaSeBorra` (2 pruebas) | Quitar el documento de F2 deja F2 sin documento; sacar C1 del texto la deja sin documento y C2 sigue en el suyo | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Alta | `ElAgenteRecibeElTextoArmado` | `ver_estandar` da el texto armado, con el cambio | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá.

**Qué salió distinto de lo esperado:** nada.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `proyectos\cimiento\.venv\Scripts\python.exe proyectos\cimiento\manage.py test core.estandar.tests_texto_desde_tablas --noinput` | Ran 6 tests in 70.388s, OK |
| 2 | Cuánto tarda armar las reglas por tarea al vuelo | Leer la base y armar las 16 con `MapaDeTareas` | 0,8 s por mensaje: siguen guardadas hasta que decida el usuario |

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
| Cobertura de exigencias | Plan §5 | 100% | 3 de 3 | Sí |
| Casos ejecutados | Plan §12 | 100% | 3 de 3 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios tienen su caso aprobado, y `core.estandar` pasa completa (66 pruebas).

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `manage.py test core.estandar`: 66 OK |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-07 | 3 | 0 | Primera ejecución |
