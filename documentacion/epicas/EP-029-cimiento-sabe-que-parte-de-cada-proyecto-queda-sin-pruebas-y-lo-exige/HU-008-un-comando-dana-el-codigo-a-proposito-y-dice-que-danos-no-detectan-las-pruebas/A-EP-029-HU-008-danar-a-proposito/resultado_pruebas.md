# Resultado de Pruebas · Fase `A-EP-029-HU-008-danar-a-proposito`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-029-HU-008-danar-a-proposito` |
| **HU** | [HU-008](../HU-008-un-comando-dana-el-codigo-a-proposito-y-dice-que-danos-no-detectan-las-pruebas.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-09 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Python 3.11.9 de `proyectos/cimiento/.venv/`, Windows 11, carpetas temporales; versión 56.8.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 6 | 6 | 6 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | `test_un_dano_detectado_y_otro_no`, `test_escribe_la_tabla` | «la suma resta» sale detectado y «la resta suma» no detectado; la tabla del comando lo dice | Aprobado | EV-01 | DEF-01, corregido |
| CP-002 | CA-01 | Alta | `test_el_texto_que_no_aparece_o_aparece_dos_veces_no_se_aplica`, `test_reconoce_el_texto_aunque_el_archivo_use_saltos_de_windows` | Los tres salen «no se aplicó» y el archivo no cambia; con saltos de Windows el daño sí se aplica | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-02 | Crítica | `test_borra_lo_que_el_dano_escribio` | `rastro.txt` no existe al terminar y aparece en la lista de borrados | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-02 | Crítica | `test_el_dano_que_cuelga_las_pruebas_cuenta_como_detectado`, con `tiempo=5` | Sale «detectado (se pasó del tiempo)» y `suma.py` es igual al original | Aprobado | EV-01 | Ninguno |
| CP-005 | CA-02 | Crítica | `test_si_se_cae_con_el_dano_puesto_el_archivo_vuelve` | El error sale y `suma.py` es igual al original | Aprobado | EV-01 | Ninguno |
| CP-006 | CA-03 | Alta | `test_no_toca_nada_si_las_pruebas_fallan_sin_danos` | El comando dice «primero hay que arreglarlas» y `suma.py` no cambia | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 6 casos en el plan, 6 acá.

**Qué salió distinto de lo esperado:** en la primera corrida, CP-001 dio los resultados al revés: el daño que la prueba sí detecta salió «no detectado». Es el DEF-01.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `python manage.py test core.pruebas.tests_danar` | Ran 8 tests in 12.146s, OK |

## 4. Defectos encontrados

| ID | Qué pasó | Causa | Estado |
|---|---|---|---|
| DEF-01 | Un daño que la prueba detecta salía «no detectado» | Python reusa el `.pyc` si el archivo tiene el mismo tamaño y la misma hora; cambiar «+» por «-» en el mismo segundo corría el código sin daño (`S-362`) | Corregido: cada daño le pone al archivo una hora distinta |

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001, CP-002 | Aprobado | Sí |
| CA-02 | CP-003, CP-004, CP-005 | Aprobado | Sí |
| CA-03 | CP-006 | Aprobado | Sí |
| RNF-01 | `preparar_salida` en el comando; `test_escribe_la_tabla` lee «daños» bien | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 3 de 3 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 6 de 6 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los 6 casos pasan (8 pruebas) y cubren los 3 CA; el único defecto se corrigió dentro de la fase.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/pruebas/danar.py`, `core/pruebas/management/commands/danar_a_proposito.py`, `core/pruebas/tests_danar.py`; salida de `python manage.py test core.pruebas.tests_danar` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-09 | 6 | 0 | Primera ejecución |
