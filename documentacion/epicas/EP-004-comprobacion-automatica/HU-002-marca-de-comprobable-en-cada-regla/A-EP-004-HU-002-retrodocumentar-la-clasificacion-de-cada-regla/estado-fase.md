# Estado de fase — Fase A-EP-004-HU-002-retrodocumentar-la-clasificacion-de-cada-regla (módulo Comprobación automática)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-002-retrodocumentar-la-clasificacion-de-cada-regla` |
| **Módulo** | Comprobación automática — [`validadores/reglas-validables.md`](../../../../../validadores/reglas-validables.md) y la fila 18 del [checklist](../../../../../base/20-meta-reglas/checklist.md) |
| **Épica / HU / origen** | [EP-004](../../epica.md) · [HU-002](../HU-002-marca-de-comprobable-en-cada-regla.md) · retro-documentación, fila de HU-002 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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
| 7 | Pruebas | [`resultado_pruebas.md`](resultado_pruebas.md) con veredicto **No cumple** | ☑ |
| 8 | Cierre documental | [`funcionalidad_implementada.md`](funcionalidad_implementada.md), §8 de la HU y fila del inventario 48 | ☑ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** §2.7 no dejó dudas abiertas: todo lo que la fase afirma se verificó contra el repositorio.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **No cumple** |
| **CA cumplidos** | 1 de 3. Los dos transversales, en «Sí» |
| **CA en "No"** | El **CA-01**: cuatro reglas escritas en `base/` con `###` **no existen para el analizador**, así que su clasificación es una fila que nadie comprueba. Y el **CA-03**, como se preveía: avisa, no detiene, y no corre |
| **Defectos abiertos aceptados** | 3 — `D-01` el analizador solo reconoce `## `; `D-02` la clasificación no detiene y `metareglas.py` no tiene subcomando; `D-03` el plan declaró cobertura completa sin contar los transversales |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) de esta fase |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | **Hecha** | CP-001, en los dos sentidos. La vuelta destapó `D-01`: 9 entradas que el analizador no reconoce |
| T-02 | **Hecha** | CP-002. **Cero rangos**: el arreglo de `A-EP-001-HU-009` sigue puesto, y ahora tiene prueba |
| T-03 | **Hecha** | 24 subcomandos, 35 módulos, **10 que el registro no nombra** — y ninguno es hueco real |
| T-04 | **Hecha** | CP-003. Tres reglas validables llegan a su programa leyendo solo el registro |
| T-05 | **Hecha** | CP-004, con la regla de mentira escrita **en una copia**. Avisa, y no detiene |
| T-06 | **Hecha** | Escrita la constancia: ninguno de los 24 subcomandos llama a `metareglas.py` |
| T-07 | **Hecha** | Corrida completa (268 pruebas, verde con 4 fallos esperados), resultado escrito y trazabilidad cerrada |

**Hechas:** 7 de 7. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| La prueba se escribe en `pruebas.py` y no arreglando el programa que no corre: es otro archivo y otro problema, ya anotado en el [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md) | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Un rango escrito como «C1–C17» no clasifica diecisiete reglas. Ese error produjo un diagnóstico falso que costó una sesión, y por eso se escribe como prueba y no como confianza | §2.6 del plan y CP-002 del [`plan_pruebas.md`](plan_pruebas.md) |
| La columna del programa va en el registro y no en un documento nuevo: dos documentos sobre lo mismo se separan solos | §2.6 del plan |
| La tabla distingue «no la comprueba nadie porque es humana» de «debería y no está»: sin esa distinción, la clasificación correcta se lee como hueco | Riesgo `R-02` del plan |

---

## 3. Pendiente / preguntas abiertas

- **`D-01`, que la fase no preveía:** el analizador solo reconoce las reglas escritas con `## `, así que **las cuatro `CQ` del capítulo 16 nunca han pasado por ninguna de las 20 filas del checklist**. Pide la fase `B-EP-004-HU-002`.
- **El CA-03 no lo cierra esta fase**, como ya se sabía: depende de un programa sin punto de entrada (pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md)). Acá quedó la evidencia y la prueba en rojo esperado.
- **El riesgo `R-01` no se materializó:** cero reglas sin clasificar entre las que el analizador ve.
- **Si otra sesión está tocando `validadores/pruebas.py`** (riesgo `R-03`): se guarda solo lo propio.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 9 esperando la autorización del commit, que es la puerta normal.
