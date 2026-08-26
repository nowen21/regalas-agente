# Estado de fase — Fase A-EP-005-HU-007-retrodocumentar-el-recogido-de-lo-guardado-por-fuera (módulo Automatismos)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-005-HU-007-retrodocumentar-el-recogido-de-lo-guardado-por-fuera` |
| **Módulo** | Automatismos — [`hook_recuerdos.py`](../../../../../validadores/hook_recuerdos.py) |
| **Épica / HU / origen** | [EP-005](../../epica.md) · [HU-007](../HU-007-recoger-lo-guardado-por-fuera.md) · retro-documentación, fila de HU-007 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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
| 6 | Ejecución continua | 5 tareas, las 5 hechas | ☑ |
| 7 | Pruebas | [`resultado_pruebas.md`](resultado_pruebas.md) con veredicto **Cumple** | ☑ |
| 8 | Cierre documental | [`funcionalidad_implementada.md`](funcionalidad_implementada.md), §8 de la HU y fila del inventario 48 | ☑ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** El recogido **no se cambia** en esta fase: cambiarlo sin saber qué hace puede perder un recuerdo del usuario.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 2 de 2, y los dos transversales |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | 2 — `D-01` el recogido se lleva lo que no es recuerdo (es de EP-006 · HU-006, decisión del usuario); `D-02` el plan declaró cobertura completa sin contar los transversales |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) de esta fase |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | **Hecha** | Caso del recuerdo que llega al repositorio — CP-001 |
| T-02 | **Hecha** | Caso del almacén que queda vacío — CP-002 |
| T-03 | **Hecha** | Prueba de que no se sobrescribe — CP-003 |
| T-04 | **Hecha** | Caso del choque de nombres — CP-004 |
| T-05 | **Hecha** | Correr, escribir el incremento de la especificación y cerrar la trazabilidad |

**Hechas:** 5 de 5. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| La prueba usa un almacén local **de mentira**: el almacén real tiene los recuerdos del usuario, y una prueba no lo toca | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) y riesgo `R-01` |
| El CA-02 se prueba con **contenido distinto** en los dos lados, no solo con el mismo nombre: pisar es sobrescribir contenido, y con el mismo texto no se notaría | §2.6 del plan |
| El choque de nombres se **observa y se escribe**, no se cambia: primero hay que saber qué hace hoy, porque cambiar el recogido puede perder un recuerdo | §2.6 del plan y riesgo `R-02` |
| El vaciado del almacén incluye el puntero: un puntero dejado atrás es la segunda versión del recuerdo, y es la que nadie mantiene | CP-002 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del plan.** Es lo único que falta para arrancar: §2.7 no dejó dudas.
- **Si el choque de nombres resulta mal resuelto** (riesgo `R-02`): se anota y se propone. Perder un recuerdo es grave y merece su propia fase.
- **Si otra sesión está tocando `validadores/pruebas.py`** (riesgo `R-03`): se guarda solo lo propio.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 9 esperando la autorización del commit, que es la puerta normal.
