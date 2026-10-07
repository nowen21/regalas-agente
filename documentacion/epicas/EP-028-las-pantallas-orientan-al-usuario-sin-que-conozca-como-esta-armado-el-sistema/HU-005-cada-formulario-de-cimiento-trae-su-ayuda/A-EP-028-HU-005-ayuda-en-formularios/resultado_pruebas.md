# Resultado de Pruebas · Fase `A-EP-028-HU-005-ayuda-en-formularios`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-028-HU-005-ayuda-en-formularios` |
| **HU** | [HU-005](../HU-005-cada-formulario-de-cimiento-trae-su-ayuda.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-07 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Las plantillas de Cimiento y la base de pruebas de Django; versión 56.8.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `test_cp001_cada_campo_tiene_su_ayuda_con_texto` | Los 31 campos de los 13 formularios tienen su «?», y todas sus claves tienen texto | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `test_cp002_cada_pantalla_con_formulario_dice_para_que_sirve` | Las 14 pantallas con formulario traen su ayuda de pantalla | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 2 casos en el plan, 2 acá.

**Qué salió distinto de lo esperado:** la regresión mostró que una prueba del gasto buscaba el texto viejo del menú de la HU-003 («Gasto», ahora «Gasto de tokens»); la regresión de esa fase no había incluido `core.consumo`. Se corrigió aquí.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `.venv\Scripts\python.exe manage.py test core.ayuda.tests_formularios --noinput` | Ran 2 tests in 0.012s, OK |

## 4. Defectos encontrados

El de §2, corregido en esta fase. Ninguno queda abierto.

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

**Justificación:** los dos criterios tienen su caso aprobado y la regresión de 250 pruebas pasa con la prueba del gasto corregida.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `manage.py test core.ayuda core.estandar core.historia core.proyectos core.niveles core.consumo core.cuentas core.inicio`: 250, con una prueba corregida |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-07 | 2 | 0 | Primera ejecución |
