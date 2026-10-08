# Resultado de Pruebas · Fase `A-EP-028-HU-007-adminlte`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-028-HU-007-adminlte` |
| **HU** | [HU-007](../HU-007-cimiento-usa-adminlte-4.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-07 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | La base de pruebas de Django; versión 58.0.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `LasPantallasUsanAdminLTE` (2 pruebas) | Inicio, estándar, historia, proyectos y gasto cargan AdminLTE y Bootstrap, no Tabler, con `app-wrapper`, `app-header`, `app-sidebar` y `app-main`; la entrada es la de AdminLTE | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `LosIconos` (en `tests_menu.py`) | Cada enlace del menú lateral, entradas y submenús, trae su ícono de Bootstrap Icons | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Alta | `NingunaClaseDeTabler` | Ninguna clase propia de Tabler en las plantillas ni en `presentar.py` | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá.

**Qué salió distinto de lo esperado:** la primera regresión dio 12 fallas: diez pruebas viejas buscaban rastros de Tabler, una tabla de `presentar.py` conservaba sus clases, y la prueba de la entrada usaba una dirección mal escrita. Se corrigieron.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `proyectos\cimiento\.venv\Scripts\python.exe proyectos\cimiento\manage.py test core.inicio.tests_adminlte core.inicio.tests_menu --noinput` | Ran 7 tests in 9.823s, OK |
| 2 | La regresión de todas las apps con pantallas | `manage.py test core.inicio core.estandar core.historia core.proyectos core.niveles core.consumo core.ayuda core.cuentas` | 304 pruebas; tras corregir, `core.inicio` 25 OK y las demás sin fallas (`historico-chat/scripts/2026-10-07/salida_pruebas_adminlte.txt`) |

## 4. Defectos encontrados

Ninguno abierto.

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

**Justificación:** los tres criterios tienen su caso aprobado y la regresión de todas las apps con pantallas queda en verde.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | §3 |
| EV-02 | La propuesta de la guía | Propuesta 15, en «Estándar → Propuestas por aprobar» |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-07 | 3 | 0 | Primera ejecución |
