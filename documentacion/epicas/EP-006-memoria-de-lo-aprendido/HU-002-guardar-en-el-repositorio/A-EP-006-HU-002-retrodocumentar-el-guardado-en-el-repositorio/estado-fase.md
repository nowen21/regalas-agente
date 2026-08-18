# Estado de fase — Fase A-EP-006-HU-002-retrodocumentar-el-guardado-en-el-repositorio (módulo Memoria)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-002-retrodocumentar-el-guardado-en-el-repositorio` |
| **Módulo** | Memoria — [`historico-chat/memory/`](../../../../../historico-chat/memory/memory.md) y [`memoria/senales.db`](../../../../../memoria/esquema.sql) |
| **Épica / HU / origen** | [EP-006](../../epica.md) · [HU-002](../HU-002-guardar-en-el-repositorio.md) · 🔀 híbrido: los recuerdos cumplen, las señales no. Fila de HU-002 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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

**Nada se ejecutó todavía.** La memoria **no se mueve** en esta fase: el límite de la base binaria se mide y se propone.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **No cumple** |
| **CA cumplidos** | 1 de 2. Los dos transversales, en «Sí» |
| **CA en "No"** | El **CA-01**, en la mitad de las señales. Y no por lo que el plan suponía —«la base es binaria y su cambio no se puede leer»—: `memoria/senales.db` está en `.gitignore` y **no tiene ningún historial**, cero commits |
| **Defectos abiertos aceptados** | 2 — `D-01` las 237 señales sin historial, con las tres salidas propuestas y ninguna decidida; `D-02` el plan declaró cobertura completa sin contar los transversales |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) de esta fase |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | **Hecha** | CP-001. El historial de un recuerdo se lee línea por línea con `git log -p` |
| T-02 | **Hecha** | CP-002. Medido: **cero commits** de `memoria/senales.db`, porque está en `.gitignore` |
| T-03 | **Hecha** | Las tres salidas escritas —exportar a texto, declarar el límite, versionar el `.db`— **y ninguna decidida** |
| T-04 | **Hecha** | CP-003. Clase `IndiceDeLosRecuerdos`: 18 de 18 en los dos sentidos |
| T-05 | **Hecha** | CP-004. Un solo archivo abierto para ubicar cada uno de los cuatro temas |
| T-06 | **Hecha** | Corrida completa (260 pruebas, verde con 2 fallos esperados), resultado escrito y trazabilidad cerrada |

**Hechas:** 6 de 6. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| El límite de la base binaria se **mide y se propone**: cambiar dónde vive la memoria es una decisión de fondo, y decidir por cuenta propia dónde vive lo aprendido es peor que el límite | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| El índice se prueba en los dos sentidos: una línea sin archivo es un índice que miente, y ya pasó con otros índices del repositorio | §2.6 del plan |
| La forma de los recuerdos no se unifica con la de las señales: son dos cosas distintas, y unirlas es lo que [HU-005](../../HU-005-separar-aprendizaje-de-preferencia/HU-005-separar-aprendizaje-de-preferencia.md) dice que no se debe hacer | §2.6 del plan |
| El índice se **usa**, no solo se cuenta: uno completo pero inútil cumple el conteo y no el criterio | CP-004 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **La decisión que esta fase deja sobre la mesa, y que le falta al CA-01:** qué hacer con las 237 señales sin historial. **A** exportarlas a texto junto a la base · **B** declarar el límite en la HU · **C** versionar el `.db` tal cual. Lo que cuesta cada una está en [§2 del resultado](resultado_pruebas.md#detalle-de-cp-002--qué-se-puede-leer-del-historial-de-la-base-de-señales). **Es del usuario**, y el plan pedía proponerlas sin decidirlas (riesgo `R-02`).
- **El riesgo `R-01` no se materializó:** el índice está completo. 18 archivos, 18 líneas, sin sobrantes ni faltantes.
- **El módulo de la memoria no tiene especificación aparte.** Es uno de los casos que [EP-001 · HU-010](../../../EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) viene a resolver.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 9 esperando la autorización del commit, que es la puerta normal.
