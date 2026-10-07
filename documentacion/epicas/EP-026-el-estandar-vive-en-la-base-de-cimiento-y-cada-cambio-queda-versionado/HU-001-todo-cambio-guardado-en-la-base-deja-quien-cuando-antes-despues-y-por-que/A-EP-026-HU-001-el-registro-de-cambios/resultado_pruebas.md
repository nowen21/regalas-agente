# Resultado de Pruebas · Fase `A-EP-026-HU-001-el-registro-de-cambios`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-026-HU-001-el-registro-de-cambios` |
| **HU** | [HU-001](../HU-001-todo-cambio-guardado-en-la-base-deja-quien-cuando-antes-despues-y-por-que.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-06 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Cimiento en la máquina local con la base de pruebas de Django sobre MariaDB, commit `e9c0e72` más los cambios de la fase; versión 56.1.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | 2026-10-06 | `CrearCambiarYBorrarQuedan`: crear, cambiar con cuenta y motivo, guardar sin cambios, borrar, grupos y programa | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | 2026-10-06 | `LoQueEscribeElEngancheQueda`: `EstadoEnBase.guardar` dos veces y `borrar`, por PyMySQL | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Alta | 2026-10-06 | `DeshacerDesdeLaPantalla`: lista, 403 para consulta, deshacer del administrador | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-04 | Crítica | 2026-10-06 | `SinClavesEnLaHistoria`: contraseña «cambiada» y clave del motivo tapada | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** la primera corrida falló al crear la base de pruebas: las migraciones de datos de otros módulos corren antes que la tabla de la historia. Se anota solo cuando la tabla existe. La segunda dio dos fallas: el tapado devuelve el texto y la cuenta, y se guardaba el par. Se toma el texto

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `.venv\Scripts\python.exe manage.py test core.historia --noinput` | Ran 9 tests in 13.818s, OK |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| CA-04 | CP-004 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 4 de 4 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 4 de 4 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los cuatro criterios tienen su caso aprobado: 9 pruebas de `core.historia` en verde y 115 en la regresión de los módulos que toca la fase.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `manage.py test core.historia`: 9 OK; regresión `core.historia core.proyectos core.niveles core.cuentas core.ayuda core.enganches.tests_analisis_en_curso`: 115 OK |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-06 | 4 | 0 | Primera ejecución |
