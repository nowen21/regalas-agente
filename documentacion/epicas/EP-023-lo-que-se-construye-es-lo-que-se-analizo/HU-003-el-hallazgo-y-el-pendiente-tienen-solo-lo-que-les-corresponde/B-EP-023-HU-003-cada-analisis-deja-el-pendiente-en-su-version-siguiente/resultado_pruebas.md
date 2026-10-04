# Resultado de Pruebas · Fase `B-EP-023-HU-003-cada-analisis-deja-el-pendiente-en-su-version-siguiente`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-023-HU-003-cada-analisis-deja-el-pendiente-en-su-version-siguiente` |
| **HU** | [HU-003](../HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-03 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Repositorio del estándar en la máquina local, rama `main`, sobre el commit `2f1b9ab` más los cambios sin guardar, versión 52.0.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-09 | Alta | `test_el_analisis_mejora_su_pendiente.py` (4 pruebas) | Sin el H-7 en «De dónde sale» no hay marca y el aviso lo nombra; con él, se aprueba; sin número, no se aprueba; el H-70 no cuenta como H-7 | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-09 | Alta | `test_el_analisis_mejora_su_pendiente.py` (1 prueba) | El análisis 1 se aprueba sin revisar el pendiente | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-09 | Media | `test_el_analisis_mejora_su_pendiente.py` (1 prueba) | La «Propuesta final» de la plantilla pide el «Pendiente V«N+1»» y pasarlo antes de aprobar | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá. El CP-003 se automatizó.

**Qué salió distinto de lo esperado:**

- Una prueba de `test_analisis_en_curso.py`, escrita hoy en el análisis 14, armaba un análisis 2 sin hallazgo y la regla nueva la rechazó. Se le agregó el hallazgo de práctica bajo la fila 4 del análisis 14, que ya autorizaba ese archivo.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Marcas de `00·ID8` en lo que escribió la fase | `marcas.py` | Ninguna nueva |
| 2 | Coherencia del estándar y origen | `validar.py estandar` y `origen` | Sin fallas |
| 3 | Que el programa que cambió siga andando | Las 20 pruebas de `test_analisis_en_curso.py` y las de `test_origen.py` | Pasan |

## 4. Defectos encontrados

Ninguno en esta fase.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-09 | CP-001 a CP-003 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 1 de 1 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 3 de 3 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple. Aprobada por el usuario el 2026-10-03.

**Justificación:** el CA-09 tiene sus tres casos ejecutados y aprobados; pasan las 6 pruebas de la fase y las de los programas que lee.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `validadores/analisis_en_curso.py`, `validadores/tests/test_el_analisis_mejora_su_pendiente.py` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-03 | 3 | 0 | Primera ejecución |
