# Resultado de Pruebas · Fase `A-EP-030-HU-002-la-pantalla-sirve-a-cada-tipo`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-030-HU-002-la-pantalla-sirve-a-cada-tipo` |
| **HU** | [HU-002](../HU-002-los-cambios-de-los-documentos-se-revisan-y-se-aprueban-en-la-pantalla.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-09 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Cimiento en la máquina local, base de pruebas de Django sobre MariaDB; versión 56.8.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | 2026-10-09 | `LaPantallaMuestraLoQueCambio`: la página trae las líneas que salen y las que entran del documento y del recuerdo | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Crítica | 2026-10-09 | `SeApruebaConUnBoton`: el botón cambia el texto y guarda la cuenta y la hora | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-02 | Crítica | 2026-10-09 | `UnTipoNuevoSeSirveSolo`: aprobar llama al `aplicar` del tipo registrado | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá.

**Qué salió distinto de lo esperado:** nada.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase y las vecinas | `manage.py test core.estandar.tests_revision core.estandar.tests_documentos core.estandar.tests_pantalla` | Ran 24 tests in 26.523s, OK |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002, CP-003 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §5 | 100% | 2 de 2 | Sí |
| Casos ejecutados | Plan §12 | 100% | 3 de 3 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los dos criterios tienen sus casos aprobados: 24 pruebas en verde.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Pruebas | `historico-chat/scripts/2026-10-08/salida_pruebas_ep030_hu002.txt`: 24 OK |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-09 | 3 | 0 | Primera ejecución |
