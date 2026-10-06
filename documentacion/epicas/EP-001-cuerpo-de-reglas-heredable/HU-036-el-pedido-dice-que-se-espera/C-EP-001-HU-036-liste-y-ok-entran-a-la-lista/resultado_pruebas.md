# Resultado de Pruebas · Fase `C-EP-001-HU-036-liste-y-ok-entran-a-la-lista`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `C-EP-001-HU-036-liste-y-ok-entran-a-la-lista` |
| **HU** | [HU-036](../HU-036-el-pedido-dice-que-se-espera.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-06 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Cimiento local, sobre `634b28a` con los cambios de la fase sin guardar; versión 56.2.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-02 | Alta | `test_cp_001_liste_y_ok_estan_en_la_lista_y_no_reciben_el_aviso` | La lista trae «Liste» y «OK», `palabra_clave` devuelve cada una desde el mensaje en minúscula, y no llega el aviso de `01·C28` | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `test_cp_002_ok_no_autoriza_ninguna_tarea` | `tareas_del_mensaje` da `{}` para «ok» y para «Liste las palabras» | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Alta | `test_cp_003_la_pregunta_entre_signos_se_trata_como_ausente` | Ninguna fila de la lista abre con `¿`, «¿qué sigue?» no trae palabra, y el aviso ya no ofrece esa forma | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá.

**Qué salió distinto de lo esperado:** Nada en las pruebas. Lo que sí salió distinto fue el orden: al intentar crear el archivo de pruebas, el freno lo detuvo porque el plan todavía figuraba sin aprobar. Se registró la aprobación del usuario en el plan y en el plan de pruebas, y el segundo intento pasó. El freno hizo lo que tenía que hacer.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `.venv\Scripts\python.exe manage.py test core.herramientas.tests_liste_y_ok` | Ran 3 tests in 0.525s, OK |
| 2 | Que la fase no rompiera la suite hermana, que lee el mismo anexo | `.venv\Scripts\python.exe manage.py test core.herramientas.tests_respondo core.herramientas.tests_liste_y_ok` | Ran 5 tests in 0.842s, OK |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-02 | CP-001, CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de criterios | Plan de pruebas §5 | 100% | 2 de 2 | Sí |
| Casos ejecutados | Plan de pruebas §5 | 100% | 3 de 3 | Sí |
| Correr solo la suite que la fase toca | Plan de trabajo §11 | Solo esa | Esa y la hermana que lee el mismo anexo | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** El enganche reconoce «Liste» y «OK», ninguna de las dos autoriza tarea, y la forma de la pregunta entre signos salió de la lista sin dejar rastro en el aviso. Las tres pruebas de la fase pasan, y la suite hermana sigue en verde.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `core/herramientas/tests_liste_y_ok.py` y la salida de §3 |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-06 | 3 | 0 | Primera ejecución |
