# Resultado de Pruebas · Fase `A-EP-025-HU-019-la-regla-y-su-plantilla`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-019-la-regla-y-su-plantilla` |
| **HU** | [HU-019](../HU-019-toda-accion-trae-su-contraria.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-05 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Máquina local, rama `main`, sobre el commit `2c3b67b` más los cambios sin guardar; versión 55.0.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `validar.py metareglas`, `estandar` e `indices`; `mapa_tareas.py` | Sin fallas sobre `F30`; el mapa la pone bajo `trabajar-cadena` y `cambiar-codigo` | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Media | Lectura de la plantilla | La sección 2.8 enlaza `F30` y trae la tabla de acción, contraria y prueba | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Alta | `validar.py versionado` | Sin fallas; la 55.0.0 es MAYOR y dice qué hace un proyecto al día | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá.

**Qué salió distinto de lo esperado:** la primera redacción medía 562 caracteres para un molde de 320; se recortó, y la excepción quedó en una línea.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `python validadores\validar.py metareglas && python validadores\validar.py versionado` | 0 falla(s), 1 aviso(s). |

## 4. Defectos encontrados

Ninguno.

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
| Cobertura de exigencias | Plan §12.1 | 100% | 3 de 3 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 3 de 3 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** la regla pasa el checklist y los validadores, la plantilla la declara y la versión subió de mayor.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Validadores | La salida de `validar.py metareglas` y `versionado`, en la sección 3 |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-05 | 3 | 0 | Primera ejecución |
| 2 | 2026-10-05 | 3 | 0 | Reabierta: la sección 2.1 declaraba la carpeta base/reglas-por-tarea/ en vez de sus archivos, y validar.py flujo lo marca como falla (02·F8) |
