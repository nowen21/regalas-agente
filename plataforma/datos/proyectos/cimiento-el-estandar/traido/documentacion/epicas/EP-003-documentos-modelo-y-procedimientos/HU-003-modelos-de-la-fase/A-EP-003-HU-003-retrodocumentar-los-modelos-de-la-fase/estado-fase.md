# Estado de fase — Fase A-EP-003-HU-003-retrodocumentar-los-modelos-de-la-fase (módulo Documentos modelo)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-003-HU-003-retrodocumentar-los-modelos-de-la-fase` |
| **Módulo** | Documentos modelo — los cinco modelos de la fase de [`plantillas/`](../../../../../plantillas/ciclo-vida-proyectos/07-plan-trabajo.md) |
| **Épica / HU / origen** | [EP-003](../../epica.md) · [HU-003](../HU-003-modelos-de-la-fase.md) · retro-documentación, fila de HU-003 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** 9 — commit único. **Última puerta pasada:** 8, con la trazabilidad cerrada.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 orden de bajar a fase las HU del inventario 48 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 presentado el 2026-08-17 | ☑ |
| 5 | Aprobación del plan detallado | 👤 «autorizados los planes de trabajo», 2026-08-17 | ☑ |
| 6 | Ejecución continua | 7 tareas, las 7 hechas | ☑ |
| 7 | Pruebas | [`resultado_pruebas.md`](resultado_pruebas.md) con veredicto **Cumple** | ☑ |
| 8 | Cierre documental | [`funcionalidad_implementada.md`](funcionalidad_implementada.md), §8 de la HU y fila del inventario 48 | ☑ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** §2.7 no dejó dudas abiertas: la fase arranca en cuanto se apruebe el plan.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 3 de 3, y los dos transversales |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | 1 — `D-01`, que el molde del plan de pruebas no obliga a una fila por transversal, que es el hueco que arrastran las 51 fases |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) de esta fase |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | **Hecha** | Incremento en la especificación: los cinco modelos y qué pregunta responde cada uno |
| T-02 | **Hecha** | Prueba del solape entre modelos — CP-001. Va detrás de T-01 |
| T-03 | **Hecha** | Caso del plan que no se reescribe, por el historial — CP-003 |
| T-04 | **Hecha** | Caso de la ausencia de columna de estado — CP-004 |
| T-05 | **Hecha** | Caso de la tarea sin criterio y el criterio sin desglose — CP-005 |
| T-06 | **Hecha** | Anotar la cuenta de avisos de `F18` como línea base |
| T-07 | **Hecha** | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 7 de 7. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| El CA-02 se prueba por el rastro del control de versiones: el historial ya guarda cada versión del plan, y una copia paralela sería otro archivo que se desincroniza | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| El solape se mide por «qué pregunta responde cada modelo», no sección por sección: dos modelos pueden compartir sección y contestar cosas distintas | §2.6 del plan y CP-001 del [`plan_pruebas.md`](plan_pruebas.md) |
| Los avisos de `F18` de fases viejas se cuentan, no se arreglan: cada uno pertenece a la fase de otra HU | §2.6 del plan |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del plan.** Es lo único que falta para arrancar.
- **Cruce con la fase [A-EP-002-HU-005](../../../EP-002-versionado-y-adopcion/HU-005-sellar-el-trabajo-cerrado/A-EP-002-HU-005-el-sello-de-version-en-el-cierre/plan_trabajo.md)**, que toca dos de estos mismos modelos (riesgo `R-02`). La que llegue segunda relee antes de escribir.
- **Si el CA-02 falla en alguna fase** —plan editado después de aprobado— se anota con fase y fecha: es un incumplimiento de [`02·F9`](../../../../../base/02-flujo-de-trabajo/reglas/F9-no-subdividas-ni-renegocies-un-plan-ya-aprobado.md) y corregirlo es de esa fase.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 9 esperando la autorización del commit, que es la puerta normal.
