# Resultado de Pruebas · Fase `A-EP-005-HU-025-entrega-por-accion`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-005-HU-025-entrega-por-accion` |
| **HU** | [HU-025](../HU-025-las-reglas-de-cada-tarea-llegan-antes-de-la-accion.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-09 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Pruebas de Django de Cimiento, con el estándar leído del disco y proyectos temporales; versión 56.8.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 7 | 7 | 7 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | Escritura de `.py`, `.md` y en `base/`, `git commit`, `WebFetch` y lectura | Cada acción da su tarea; leer no da ninguna | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-01 | Crítica | `hook_reglas_accion.py` con una escritura de `x.py` | Sale con 0, sin decisión de permiso | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-02 | Crítica | La misma tarea pedida hasta vaciarla, otra sesión y un subagente | Cada regla llegó una vez; el subagente y la otra sesión reciben las suyas | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-02 | Crítica | `cambiar-codigo`, que no cabe en el tope | Lo que no cupo llega en la entrega siguiente; ninguna entrega pasa del tope; sin nada por dar, no lee el estándar | Aprobado | EV-01 | Ninguno |
| CP-005 | CA-03 | Alta | Mensajes con «Pregunta», «Hágalo», una cita y sin palabra | Solo `responder` con la pregunta; `recibir-pedido` con «Hágalo»; nada se repite; la cita y el aviso llegan | Aprobado | EV-01 | Ninguno |
| CP-006 | CA-03 | Alta | `hook_reglas.py` con un mensaje | Sin «LAS REGLAS DE CADA TURNO» | Aprobado | EV-01 | Ninguno |
| CP-007 | CA-04 | Alta | El catálogo y el aviso con la sesión de la entrada | Las señales están solo en `SessionStart` y avisan una vez | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 7 casos en el plan, 7 acá.

**Qué salió distinto de lo esperado:** en la primera corrida, CP-004 encontró una entrega de 9.725 bytes contra un tope de 8.704: la lista de lo que no cupo no se medía. Se corrigió midiendo el texto entero.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `"C:/Ing. Jose/ia/agente/proyectos/cimiento/.venv/Scripts/python.exe" "C:/Ing. Jose/ia/agente/proyectos/cimiento/manage.py" test core.herramientas.tests_entrega_de_reglas core.enganches.tests_suspendidos` | Ran 33 tests in 24.792s, OK |
| 2 | El catálogo y el instalador, que lo usan | `manage.py test core.comun.tests core.herramientas.tests_instalacion` | 22 y 227 pruebas, OK |
| 3 | El enganche en esta misma sesión | Un comando de consola después de cambiar `.claude/settings.json` | Llegaron las reglas de `correr-comando` y `tocar-git`, por partes y sin frenar el comando |

## 4. Defectos encontrados

Uno, corregido en el mismo ciclo: la lista de lo que no cupo hacía pasar la entrega del tope.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001, CP-002 | Aprobado | Sí |
| CA-02 | CP-003, CP-004 | Aprobado | Sí |
| CA-03 | CP-005, CP-006 | Aprobado | Sí |
| CA-04 | CP-007 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 4 de 4 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 7 de 7 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los 7 casos pasan, y el enganche ya entregó en esta sesión las reglas de `correr-comando` y `tocar-git` antes de un comando, por partes y sin repetir.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/herramientas/tests_entrega_de_reglas.py` y la salida de §3 |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-09 | 7 | 0 | Primera ejecución |
