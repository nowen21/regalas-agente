# Estado de fase — Fase A-EP-006-HU-006-retrodocumentar-el-vaciado-del-almacen-local (módulo Memoria)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-006-retrodocumentar-el-vaciado-del-almacen-local` |
| **Módulo** | Memoria — [`recuerdos.py`](../../../../../validadores/recuerdos.py) y [`hook_recuerdos.py`](../../../../../validadores/hook_recuerdos.py) |
| **Épica / HU / origen** | [EP-006](../../epica.md) · [HU-006](../HU-006-sacar-del-almacen-local.md) · retro-documentación. Es la otra cara de [EP-005 · HU-007](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-007-recoger-lo-guardado-por-fuera/HU-007-recoger-lo-guardado-por-fuera.md): allá se prueba el enganche, acá el resultado. Fila de HU-006 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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
| 7 | Pruebas | [`resultado_pruebas.md`](resultado_pruebas.md) con veredicto **No cumple** | ☑ |
| 8 | Cierre documental | [`funcionalidad_implementada.md`](funcionalidad_implementada.md), §8 de la HU y fila del inventario 48 | ☑ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** Lo que haya en el almacén de esta máquina **se observa, no se borra a mano**: vaciarlo haría el trabajo del programa y borraría la evidencia.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **No cumple** |
| **CA cumplidos** | 1 de 2. El RNF y los dos transversales, en «Sí» |
| **CA en "No"** | El **CA-01**, en un solo punto: el recogido **se lleva también lo que no es un recuerdo**. El almacén queda vacío, que era la otra mitad |
| **Defectos abiertos aceptados** | 2 — `D-01` el recogido no distingue qué es recuerdo, y resolverlo toca `01·C19`; `D-02` el plan declaró cobertura completa sin contar los transversales |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) de esta fase |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | **Hecha** | CP-001. El almacén queda sin archivos. Destapó `D-01` en su paso 5 |
| T-02 | **Hecha** | CP-003. El almacén de esta máquina está **vacío**, el 2026-08-17 |
| T-03 | **Hecha** | CP-002. No queda ni el texto ni el puntero, y no hay dos versiones |
| T-04 | **Hecha** | CP-002 con el puntero escrito a mano: el escenario que el CA-02 nombra y que no tenía prueba |
| T-05 | **Hecha** | Corrida completa (260 pruebas, verde con 2 fallos esperados), resultado escrito y trazabilidad cerrada |

**Hechas:** 5 de 5. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Las pruebas usan almacenes de mentira: el real puede tener algo del usuario sin recoger todavía | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| El caso del puntero se prueba **a propósito**: es el caso que el índice de la memoria nombra, y un puntero es peor que nada porque parece que hay memoria donde no hay | §2.6 del plan |
| Lo que haya en el almacén de esta máquina se **anota**, no se borra a mano: vaciarlo hace el trabajo del programa y pierde la evidencia de si funcionaba | §2.6 del plan y riesgo `R-01` |

---

## 3. Pendiente / preguntas abiertas

- **Qué debe hacer el recogido con lo que no es un recuerdo** (`D-01`). **A** que distinga y `01·C19` acepte lo que queda · **B** que se lleve todo, y quede dicho. Toca `base/`: **es del usuario**.
- **El riesgo `R-01` no se materializó:** el almacén de esta máquina estaba vacío, así que no hubo nada que recoger ni que anotar.
- **El módulo de la memoria no tiene especificación aparte.** Es uno de los casos que [EP-001 · HU-010](../../../EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) viene a resolver.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 9 esperando la autorización del commit, que es la puerta normal.
