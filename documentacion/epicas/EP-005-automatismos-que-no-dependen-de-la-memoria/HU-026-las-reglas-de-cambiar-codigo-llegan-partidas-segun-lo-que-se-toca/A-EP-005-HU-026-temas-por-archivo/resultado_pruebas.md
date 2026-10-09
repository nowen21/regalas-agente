# Resultado de Pruebas · Fase `A-EP-005-HU-026-temas-por-archivo`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-005-HU-026-temas-por-archivo` |
| **HU** | [HU-026](../HU-026-las-reglas-de-cambiar-codigo-llegan-partidas-segun-lo-que-se-toca.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-09 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Pruebas de Django de Cimiento, con el estándar leído del disco y la tabla de `tareas-con-temas.txt`; versión 56.8.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | Escribir `core/tests_x.py` hasta vaciar | Llegan los capítulos 08 y los de `todos`; ninguno del 03, 17 ni 18; 24 KB de reglas de código | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-01 | Crítica | Una prueba y después `core/views.py` | La vista recibe el 04, 05 y 06 | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-02 | Crítica | `algo.xyz` con la tabla, y una prueba sin tabla | Las dos reciben todas las de `cambiar-codigo` | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-03 | Alta | `manage.py documento editar estandar base/tareas.md` con `tareas-con-temas.txt` | Quedó la propuesta 19 | Aprobado | EV-02 | Ninguno |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** nada.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `"C:/Ing. Jose/ia/agente/proyectos/cimiento/.venv/Scripts/python.exe" "C:/Ing. Jose/ia/agente/proyectos/cimiento/manage.py" test core.herramientas.tests_entrega_de_reglas` | Ran 37 tests in 51.186s, OK |
| 2 | Lo que llega por tipo de archivo, con la tabla | Las reglas de `cambiar-codigo` filtradas por los capítulos de cada archivo | Prueba 46 reglas (24 KB); vista 63 (32 KB); modelo 62 (33 KB); pantalla 44 (23 KB); configuración 55 (30 KB); sin patrón 128 (67 KB) |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001, CP-002 | Aprobado | Sí |
| CA-02 | CP-003 | Aprobado | Sí |
| CA-03 | CP-004 | Aprobado | Sí, con la tabla propuesta; queda en el estándar cuando el usuario apruebe la propuesta 19 |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §5 | 100% | 3 de 3 | Sí |
| Casos ejecutados | Plan §12 | 100% | 4 de 4 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los 4 casos pasan. La tabla rige en cuanto se aprueben las propuestas 18 y 19; mientras tanto la entrega sigue como en la HU-025.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/herramientas/tests_entrega_de_reglas.py` y la salida de §3 |
| EV-02 | Propuesta | Propuesta 19 en Cimiento → Estándar → Propuestas; texto en `historico-chat/scripts/2026-10-09/tareas-con-temas.txt` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-09 | 4 | 0 | Primera ejecución |
