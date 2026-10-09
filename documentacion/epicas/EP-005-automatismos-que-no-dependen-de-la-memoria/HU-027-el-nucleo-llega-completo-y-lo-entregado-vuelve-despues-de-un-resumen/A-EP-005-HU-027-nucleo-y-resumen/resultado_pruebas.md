# Resultado de Pruebas · Fase `A-EP-005-HU-027-nucleo-y-resumen`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-005-HU-027-nucleo-y-resumen` |
| **HU** | [HU-027](../HU-027-el-nucleo-llega-completo-y-lo-entregado-vuelve-despues-de-un-resumen.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-09 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Pruebas de Django de Cimiento, con el estándar leído del disco y proyectos temporales; versión 56.8.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | Abrir con `startup` y mandar mensajes hasta vaciar | Llegan solo blindadas, sin pasar del tope; al final llegó todo el núcleo, cada regla una vez | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-01 | Crítica | `hook_reglas_sesion.py` con `source: startup` | Sale con 0; el texto va como `additionalContext` de `SessionStart` | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-02 | Crítica | Todo entregado y después `compact`, y después `clear` | Vuelve el núcleo, y la escritura de `x.py` vuelve a traer `cambiar-codigo` | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-02 | Crítica | `resume` y un subagente después de `compact` | Con `resume` no llega nada; el subagente conserva su cuenta | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** nada.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `"C:/Ing. Jose/ia/agente/proyectos/cimiento/.venv/Scripts/python.exe" "C:/Ing. Jose/ia/agente/proyectos/cimiento/manage.py" test core.herramientas.tests_entrega_de_reglas core.comun.tests` | Ran 52 tests in 46.955s, OK |
| 2 | El instalador, que lee el catálogo | `manage.py test core.herramientas.tests_instalacion` | 227 pruebas, OK |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001, CP-002 | Aprobado | Sí |
| CA-02 | CP-003, CP-004 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §5 | 100% | 2 de 2 | Sí |
| Casos ejecutados | Plan §12 | 100% | 4 de 4 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los 4 casos pasan.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/herramientas/tests_entrega_de_reglas.py` y la salida de §3 |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-09 | 4 | 0 | Primera ejecución |
