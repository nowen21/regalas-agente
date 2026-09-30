# Funcionalidad implementada · Fase `C-EP-005-HU-023-las-reglas-llegan-antes-de-actuar` (módulo Cuerpo de reglas y validadores)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-005-HU-023-las-reglas-llegan-antes-de-actuar` |
| **Módulo** | Cuerpo de reglas, `validadores/` y el adaptador |
| **Especificación del módulo** | RN-07 a RN-09 de [HU-023](../HU-023-cada-tarea-sabe-que-reglas-le-aplican.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | HU-023 (CA-08, CA-09, CA-10) |
| **Fecha de cierre** | 2026-09-28 |
| **Versión del estándar al cerrar** | 39.6.0 |
| **Commit** | Se completa al commitear |

## 1. Qué se implementó, resumen

Con cada mensaje, las reglas que recibe el agente salen de la palabra de `01·C28` con que abre el mensaje, sin adivinar. Si el mensaje no la trae, el agente recibe el aviso con la lista, no actúa y espera; si cita una regla, recibe también su texto. Las reglas de cada tarea están completas en `base/reglas-por-tarea/`. Ninguna escritura sale de la carpeta del proyecto.

El agente no tiene que leer las reglas por comando antes de actuar: eso se construyó en los ciclos 1 a 3 y el usuario lo descartó en el ciclo 4 (sección 12 del [plan](plan_trabajo.md)).

## 2. Trazabilidad  ·  `13·DOC11`

| Tarea | Qué se hizo | Dónde quedó | Evidencia |
|---|---|---|---|
| T-01 | Columnas de palabras clave y de acciones | `base/tareas.md` | CP-001, CP-002 |
| T-02 | Archivos por tarea, partidos a 25.000 caracteres, con los enlaces reescritos, y su validación | `validadores/mapa_tareas.py`, `validadores/comun.py`, `base/reglas-por-tarea/` | CP-003 |
| T-03 | Tareas por palabra clave al abrir una frase; sin palabra, el aviso de `01·C28` y las reglas citadas; lo que no cabe nombra su archivo | `validadores/recuperar.py` | CP-001, ciclo 4 |
| T-04 | `leidas.py` se construyó en el ciclo 1 y se borró en el ciclo 4 | — | Ciclo 4 |
| T-05 | Detención de toda escritura fuera del proyecto; los modos de lectura se quitaron en el ciclo 4 | `adaptadores/claude-code/hook_antes.py` | Ciclos 2 y 4 |
| T-06 | Solo el freno de escritura en el instalador | `validadores/instalar.py`, `.gitignore` | Ciclo 4 |
| Ciclo 3 | El enganche del commit no cuenta las marcas de las copias por tarea | `validadores/marcas.py` | Ciclo 4 |
| T-07 | 9 casos nuevos del enganche, 3 del mapa, 3 del recuperador, y los que esperaban palabras sueltas reescritos | `validadores/tests/`, `validadores/pruebas.py` | CP-001 a CP-004 |
| T-08 | Guías de los cuatro programas, anatomía, `CLAUDE.md` y su plantilla | `validadores/docs/`, `anatomia/que-esta-amarrado-a-la-herramienta.md`, `CLAUDE.md`, `plantillas/CLAUDE.md.plantilla` | CP-004 |
| T-09 | `39.6.0` | `CHANGELOG.md`, `VERSION` | CP-004 |
| T-10 | Cierre de HU-023 y de H-1 | HU-023, resumen de la sesión | — |

**Faltantes / diferimientos:** el freno de escritura no está puesto en el `.claude/settings.json` del estándar, porque la herramienta no dejó que el agente editara ese archivo; se pone con el instalador. La cita «00 id9» con espacio no trae la regla: va como pendiente. Los cambios posteriores a la aprobación están en la sección 12 del [plan](plan_trabajo.md), aprobados el 2026-09-29.

## 3. Qué se probó

| Qué | Resultado |
|---|---|
| CP-001 a CP-004 | Cumple; detalle en [resultado_pruebas.md](resultado_pruebas.md) |
| Pruebas de la fase | Ciclo 1: 157 en OK. Ciclo 2: 84 + 79. Ciclo 3: 63 + 48. Ciclo 4: 63 + 58 |
| Prueba real en esta sesión | Los mensajes sin palabra recibieron el aviso y el agente solo la recordó; los que la traían recibieron sus reglas sin orden de leer |
| `validar.py estandar`, `tareas`, `amarre` y `versionado` | Sin fallas |
