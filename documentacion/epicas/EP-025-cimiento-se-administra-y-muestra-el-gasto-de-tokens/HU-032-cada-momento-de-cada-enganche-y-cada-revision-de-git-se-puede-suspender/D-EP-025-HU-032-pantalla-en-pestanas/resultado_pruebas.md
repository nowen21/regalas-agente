# Resultado de Pruebas · Fase `D-EP-025-HU-032-pantalla-en-pestanas`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `D-EP-025-HU-032-pantalla-en-pestanas` |
| **HU** | [HU-032](../HU-032-cada-momento-de-cada-enganche-y-cada-revision-de-git-se-puede-suspender.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-09 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Python 3.11.9 de `proyectos/cimiento/.venv/`, la base de pruebas de Django, Windows 11; versión 56.8.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-008 | CA-04 | Alta | `test_tres_pestanas_con_suspensiones_abierta`, `test_reglas_y_enganches_en_tablas_como_la_de_suspensiones` | Las tres pestañas, con «Suspensiones» activa; «Reglas» trae `02·F8` y «Enganches» `historico-del-usuario`, las dos con `data-tabla-avanzada` | Aprobado | EV-01 | Ninguno |
| CP-009 | CA-04 | Alta | `test_el_boton_abre_el_modal_y_con_errores_vuelve_abierto`, `test_quien_solo_consulta_no_ve_el_boton_ni_el_modal` | El botón apunta a `#suspender`; con un nombre que no existe la página vuelve con el modal abierto y el error; la cuenta de consulta no ve el botón ni el modal | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 2 casos en el plan, 2 acá.

**Qué salió distinto de lo esperado:** nada.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `python manage.py test core.proyectos.tests_suspender_enganches core.proyectos.tests_configuracion core.ayuda` | Ran 39 tests in 15.753s, OK |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-04 | CP-008, CP-009 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 1 de 1 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 2 de 2 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los 2 casos pasan, y las 35 pruebas de suspensiones, configuración y ayuda siguen pasando (39 en total).

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `core/proyectos/templates/proyectos/suspensiones.html`, `core/proyectos/views.py`, `core/proyectos/tests_suspender_enganches.py` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-09 | 2 | 0 | Primera ejecución |
