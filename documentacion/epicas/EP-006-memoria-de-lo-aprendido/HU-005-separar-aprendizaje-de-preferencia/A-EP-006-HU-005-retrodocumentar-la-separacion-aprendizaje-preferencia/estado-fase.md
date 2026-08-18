# Estado de fase — Fase A-EP-006-HU-005-retrodocumentar-la-separacion-aprendizaje-preferencia (módulo Memoria)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-005-retrodocumentar-la-separacion-aprendizaje-preferencia` |
| **Módulo** | Memoria — [`memoria/senales.db`](../../../../../memoria/esquema.sql) y [`historico-chat/memory/`](../../../../../historico-chat/memory/memory.md) |
| **Épica / HU / origen** | [EP-006](../../epica.md) · [HU-005](../HU-005-separar-aprendizaje-de-preferencia.md) · retro-documentación, fila de HU-005 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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

**Nada se ejecutó todavía.** Ningún recuerdo se mueve de sitio en esta fase: mover uno cambia lo que rige la sesión.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **No cumple** |
| **CA cumplidos** | 1 de 2. Los dos transversales, en «Sí» |
| **CA en "No"** | El **CA-01**. El criterio que le faltaba **ya está escrito**, y aun así no se cumple: la terminología del proyecto está guardada **en los dos sitios a la vez**, y las dos versiones ya dicen cosas distintas |
| **Defectos abiertos aceptados** | 3 — `D-01` la terminología duplicada y divergida; `D-02` un aprendizaje guardado como preferencia, que además debería subir a `base/`; `D-03` el plan declaró cobertura completa sin contar los transversales |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) de esta fase |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | **Hecha** | El criterio «Cuál va dónde» está escrito en [`memory.md`](../../../../../historico-chat/memory/memory.md), con el caso de borde y la regla de un solo sitio |
| T-02 | **Hecha** | CP-001. **Tres de cinco no coinciden** con dónde están; una de ellas está en los dos sitios |
| T-03 | **Hecha** | CP-003. Clase `ElRecuerdoTraeSusTresPartes`: 18 de 18 completos |
| T-04 | **Hecha** | CP-004. El caso negativo caza al que le falta una parte |
| T-05 | **Hecha** | Corrida completa (260 pruebas, verde con 2 fallos esperados), resultado escrito y trazabilidad cerrada |

**Hechas:** 5 de 5. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| El criterio se escribe en el índice de la memoria, no en `base/`: qué es preferencia del usuario es de este repositorio. Si aplicara a cualquier proyecto sería regla — y ese es justo el caso de borde que hay que escribir | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Lo que esté en el sitio equivocado se **anota**, no se mueve: mover un recuerdo cambia lo que rige la sesión | §2.6 del plan |
| La prueba mira que las **tres partes estén**, no si el porqué convence: lo primero es sí o no, lo segundo es criterio | §2.6 del plan |
| El caso de borde es la prueba del criterio: si con él no se puede decidir, al criterio le falta texto | Riesgo `R-03` y CP-002 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **Cuál de las dos versiones de la terminología manda** (`D-01`). La señal `S-002` dice «el agente = Claude Code»; el recuerdo dice **Cimiento** desde el 2026-08-14. **Es del usuario**: cambiar un recuerdo cambia lo que rige la sesión, y ninguna de las dos se tocó.
- **Si «fixtures sin secretos literales» sube a `base/`** (`D-02`, riesgo `R-01`): queda anotado y propuesto. Subir un recuerdo a regla lo decide el usuario, como ya pasó con dos en [EP-001 · HU-004](../../../EP-001-cuerpo-de-reglas-heredable/HU-004-conducta-de-la-ia/HU-004-conducta-de-la-ia.md).
- **Nadie detecta lo guardado en dos sitios.** Esto se encontró leyendo, no corriendo nada. Queda sin destino.
- **El módulo de la memoria no tiene especificación aparte.** Es uno de los casos que [EP-001 · HU-010](../../../EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) viene a resolver.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 9 esperando la autorización del commit, que es la puerta normal.
