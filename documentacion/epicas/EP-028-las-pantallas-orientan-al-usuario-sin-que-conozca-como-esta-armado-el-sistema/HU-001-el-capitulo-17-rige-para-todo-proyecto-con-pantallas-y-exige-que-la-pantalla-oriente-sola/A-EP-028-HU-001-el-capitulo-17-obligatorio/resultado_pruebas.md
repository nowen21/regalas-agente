# Resultado de Pruebas · Fase `A-EP-028-HU-001-el-capitulo-17-obligatorio`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-028-HU-001-el-capitulo-17-obligatorio` |
| **HU** | [HU-001](../HU-001-el-capitulo-17-rige-para-todo-proyecto-con-pantallas-y-exige-que-la-pantalla-oriente-sola.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-07 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | La base de pruebas de Django y el estándar real leído sin escribir, con la propuesta 7 aprobada; versión 56.8.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `test_cp001_sin_opt_in_ni_ajuste_y_un_claude_md_viejo_no_lo_apaga` | El encabezado no dice opt-in, no hay ajuste `opt_in_17` y un `CLAUDE.md` con «no» en el 17 no lo apaga | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `test_cp002_i7_existe_con_su_checklist_e_i5_pide_la_plantilla_instalada` | `I7` está con su checklist e `I5` pide la plantilla instalada | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 2 casos en el plan, 2 acá.

**Qué salió distinto de lo esperado:** una carpeta sin registro con un `CLAUDE.md` viejo seguía apagando el 17; el recuperador ahora solo cuenta los capítulos que siguen siendo opt-in. La prueba de opt-in contaba siete capítulos y pasó a seis.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `.venv\Scripts\python.exe manage.py test core.estandar.tests_capitulo17 --noinput` | Ran 2 tests in 0.332s, OK |

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

**Justificación:** los dos criterios tienen su caso aprobado; la regresión de `core.proyectos`, `core.ayuda` y `core.herramientas` pasa con la prueba de opt-in ajustada.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `manage.py test core.estandar.tests_capitulo17`: 2 OK; regresión de 377 con una prueba ajustada; la base real sin ajustes `opt_in_17` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-07 | 2 | 0 | Primera ejecución |
