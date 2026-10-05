# Resultado de Pruebas · Fase `A-EP-025-HU-009-avisos-por-limite`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-009-avisos-por-limite` |
| **HU** | [HU-009](../HU-009-se-avisa-cuando-un-enganche-o-un-archivo-pesa-demasiado.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-05 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Máquina local, rama `main`, sobre el commit `29a30ad` más los cambios sin guardar; base real en MariaDB 11.4.9; versión 54.2.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `LoQuePasaElLimiteSeAvisa` (6 pruebas) | El turno anterior, con el mensaje siguiente escrito o sin escribir; solo lo que pasó el límite, y lo que está justo en él no; un mismo enganche dos veces sale una, con «(2 veces)»; el enganche entero avisa y sale con 0; sin transcripción, sale con 0 y callado | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `CadaExcesoSeAvisaUnaVez` | El turno siguiente sin excesos no avisa | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Media | `LosLimitesSonLosDelProyecto` (3 pruebas) y el límite por enganche de este proyecto en 100, en la base real | Los del registro; sin registro o sin base, 2000 y 10 000. Con 100 en la base real, el enganche avisó con «el límite del proyecto es 100» y salió con 0; el límite volvió a 2000 | Aprobado | EV-01, EV-02 | D-01 |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá.

**Qué salió distinto de lo esperado:** el paso manual mostró D-01.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que lo de la HU-006 y el freno sigan andando | `manage.py test core.consumo core.proyectos` y `ElNivelDeLaRegla`, `SinBaseNoSeModifica` | Todas pasan |
| 2 | Los enganches guardados, leídos otra vez con el lector corregido | Se borraron los enganches y el avance de lectura, que salen de los `.jsonl`, y se corrió `leer_consumo` | Llamadas de 12 890 a 13 111 (las nuevas de la sesión, sin duplicar); enganches de 3850 a 5823 |

## 4. Defectos encontrados

| ID | Caso | Qué pasó | Esperado | Obtenido | Estado |
|---|---|---|---|---|---|
| D-01 | CP-003 | El aviso nombraba «UserPromptSubmit» y no contaba el enganche de las señales | El nombre de cada enganche, y todo lo que llega al modelo | Los contextos de `UserPromptSubmit` no tienen `hook_success` hermano, y el texto plano de un enganche en `UserPromptSubmit` o `SessionStart` no se contaba | Corregido en `lector.py`: el nombre sale del título entre corchetes, y el texto plano de esos dos momentos cuenta. Dos pruebas en `ElLectorVeTodosLosEnganches` |

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| RNF-01 | CP-003 | `LimitesDelProyecto` con PyMySQL, sin Django | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 3 de 3 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 3 de 3 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios pasan, y el aviso llegó con el límite de la base real.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/enganches/tests_limites.py` (12 pruebas) |
| EV-02 | Base real | El aviso con el límite 100, devuelto a 2000 |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-05 | 3 | 0 | Primera ejecución |
