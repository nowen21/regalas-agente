# Estado de fase — Fase A-EP-002-HU-001-retrodocumentar-el-numero-de-version (módulo Versionado y adopción)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-002-HU-001-retrodocumentar-el-numero-de-version` |
| **Módulo** | Versionado y adopción — [`VERSION`](../../../../../VERSION) y [`validadores/version.py`](../../../../../validadores/version.py) |
| **Épica / HU / origen** | [EP-002](../../epica.md) · [HU-001](../HU-001-numero-de-version-y-que-significa.md) · retro-documentación, fila de HU-001 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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
| 6 | Ejecución continua | 6 tareas, las 6 hechas | ☑ |
| 7 | Pruebas | [`resultado_pruebas.md`](resultado_pruebas.md) con veredicto **No cumple** | ☑ |
| 8 | Cierre documental | [`funcionalidad_implementada.md`](funcionalidad_implementada.md), §8 de la HU y fila del inventario 48 | ☑ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** §2.7 no dejó dudas abiertas: la fase arranca en cuanto se apruebe el plan.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **No cumple** |
| **CA cumplidos** | 2 de 3, y los dos transversales |
| **CA en "No"** | El **CA-01**: `15.4.0` figura dos veces, así que un proyecto que la declare no puede saber cuál adoptó |
| **Defectos abiertos aceptados** | 2 — `D-01` el número repetido (renumerar una versión publicada es del usuario); `D-02` el plan declaró cobertura completa sin contar los transversales |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) de esta fase |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | **Hecha** | Prueba de que `VERSION` manda — CP-001 |
| T-02 | **Hecha** | Caso de los números sueltos en el repositorio — CP-002 |
| T-03 | **Hecha** | Caso de las tres entradas MAYOR — CP-003 |
| T-04 | **Hecha** | Caso de las tres entradas PARCHE — CP-004 |
| T-05 | **Hecha** | Prueba de continuidad de las tres partes — CP-005 |
| T-06 | **Hecha** | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 6 de 6. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| La prueba lee el número de `VERSION` en vez de traerlo escrito: una versión escrita a mano envejece en la subida siguiente | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Una subida mal clasificada se anota, no se corrige: el registro es rastro, y reescribirlo borra lo que pasó | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) y RN-04 de [HU-002](../../HU-002-registro-de-cambios/HU-002-registro-de-cambios.md) |
| El tramo de las dos numeraciones vivas se declara como excepción **en el caso**, no se silencia en la prueba | §3.3 del [`plan_pruebas.md`](plan_pruebas.md) y pendiente [22](../../../../../pendientes/22-dos-sesiones-versionando-a-la-vez.md) |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del plan.** Es lo único que falta para arrancar.
- **El tramo de las dos numeraciones vivas del 2026-08-14** (pendiente [22](../../../../../pendientes/22-dos-sesiones-versionando-a-la-vez.md)) va a hacer ruido en la prueba de continuidad. Se documenta, no se tapa.
- **Si otra sesión está tocando `validadores/pruebas.py`** (riesgo `R-03`): se guarda solo lo propio.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 9 esperando la autorización del commit, que es la puerta normal.
