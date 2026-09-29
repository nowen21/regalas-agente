# Plan de Pruebas · Fase `A-EP-016-HU-005-la-promesa-dice-cuando-llegan-las-reglas`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que ningún criterio de aceptación quede sin al menos un caso, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP016-005-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-005 de EP-016, CA-01 |
| **Fecha** | 2026-09-28 |
| **Elaborado por** | El agente |
| **Revisado por** | El usuario |
| **Aprobado por** | El usuario |
| **Estado** | Aprobado el 2026-09-28 |

## 3. Estrategia de pruebas

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Sistema | Que ningún documento vigente prometa las reglas al abrir | El agente | Local | Sí, con búsqueda y `validar.py estandar` |
| Aceptación | Que la promesa nueva se entienda | El usuario | Local | No |

No cambia ningún programa, así que no se corre ninguna batería de pruebas (`02·F5`).

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-005 | [CA-01](../HU-005-entregarle-las-reglas-al-agente.md) | [CP-001](#cp-001--la-promesa-dice-cuándo-llegan-las-reglas) | Documental | Alta | Parcial | ☐ |

**Cobertura:** 1 de 1, 100%.

## 6. Casos de prueba

### CP-001 · La promesa dice cuándo llegan las reglas

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-01 |
| **Tipo** | Documental |
| **Prioridad** | Alta |
| **Precondiciones** | La T-01 a la T-05 terminadas |
| **Datos de entrada** | `cvds/` y `documentacion/epicas/EP-016-…/`, sin las fases cerradas |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar «al abrir» y «reglas» en el mismo renglón | Ninguno que prometa que las reglas llegan al abrir |
| 2 | Leer la ficha de `F-009` y la fila de `RF-09` | Dicen que llegan con cada mensaje las de la tarea, y enteras cuando se piden |
| 3 | Leer HU-005 | La narrativa y el título del CA-01 dicen lo mismo, y el contexto explica por qué no al abrir |
| 4 | Correr `python validadores/validar.py estandar` | Sin incumplimientos |

**Resultado esperado final:** la plataforma promete lo que pasa.

## 9. Gestión de defectos

Un caso que no da lo esperado se corrige en la misma fase si está dentro de los archivos de la sección 2.1 del plan de trabajo. Si pide tocar otro archivo, se detiene el trabajo y se le pregunta al usuario (`02·F8`).

| ID | Título | CP | Severidad | Estado | Asignado | Fecha | Cierre |
|---|---|---|---|---|---|---|---|
| | Ninguno todavía | | | | | | |

## 12. Métricas e informe

| Métrica | Fórmula | Meta |
|---|---|---|
| Promesas de «al abrir» | Conteo del paso 1 | 0 |
| Fallas de `estandar` | Conteo | 0 |

El resultado de cada métrica va en el [resultado_pruebas.md](resultado_pruebas.md).

## 15. Aprobación

| Rol | Nombre | Firma | Fecha |
|---|---|---|---|
| Product Owner | El usuario | «Apruebo los dos planes. Hágalo», en el chat | 2026-09-28 |
