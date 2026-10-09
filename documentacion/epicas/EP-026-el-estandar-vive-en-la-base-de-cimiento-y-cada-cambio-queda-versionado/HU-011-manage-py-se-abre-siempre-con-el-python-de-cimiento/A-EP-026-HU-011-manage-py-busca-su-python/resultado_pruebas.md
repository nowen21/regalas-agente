# Resultado de Pruebas · Fase `A-EP-026-HU-011-manage-py-busca-su-python`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-026-HU-011-manage-py-busca-su-python` |
| **HU** | [HU-011](../HU-011-manage-py-se-abre-siempre-con-el-python-de-cimiento.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-08 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Cimiento en la máquina local, abierto con el Python 3.11 del computador; versión 56.8.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | 2026-10-08 | `test_con_otro_python_devuelve_el_de_venv` y `test_responde_y_escribe_las_tildes`: con el Python del computador, `manage.py shell` termina con 0 | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | 2026-10-08 | `test_sin_venv_no_devuelve_ninguno` y `test_ya_con_el_de_venv_no_devuelve_ninguno` | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Alta | 2026-10-08 | `test_responde_y_escribe_las_tildes`: la salida, leída como UTF-8, trae «capítulo» | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-01, CA-03 | Crítica | 2026-10-08 | `python proyectos/cimiento/manage.py ver_estandar base/01-conducta/palabras-clave.md` sale con 0 y escribe «capítulo» y «qué» bien | Aprobado | EV-02 | Ninguno |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** nada.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase, con el Python del computador | `python manage.py test core.comun.tests_arranque -v 2` | Ran 4 tests in 3.606s, OK |
| 2 | La consulta del aviso, tal como está escrita | `python proyectos/cimiento/manage.py ver_estandar base/01-conducta/palabras-clave.md` | Sale con 0 y las tildes bien |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001, CP-004 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003, CP-004 | Aprobado | Sí |
| RNF-01 | CP-001, CP-002 | `python_que_toca` busca en `Scripts/` y en `bin/`; se probó en Windows | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §5 | 100% | 3 de 3 | Sí |
| Casos ejecutados | Plan §12 | 100% | 4 de 4 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios tienen su caso aprobado: las 4 pruebas de `core.comun.tests_arranque` en verde, corridas con el Python del computador, y la consulta del aviso responde con las tildes bien.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Pruebas | `python manage.py test core.comun.tests_arranque`: 4 OK |
| EV-02 | Consulta real | `python proyectos/cimiento/manage.py ver_estandar base/01-conducta/palabras-clave.md`: salida 0 |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-08 | 4 | 0 | Primera ejecución |
