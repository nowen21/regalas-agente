# Estado de fase — Fase A-EP-003-HU-005-retrodocumentar-los-modelos-de-la-capa-3 (módulo Documentos modelo)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-003-HU-005-retrodocumentar-los-modelos-de-la-capa-3` |
| **Módulo** | Documentos modelo — [`stack.md`](../../../../../plantillas/stack.md), [`dominio.md`](../../../../../plantillas/dominio.md), [`mapeo-nombres.md`](../../../../../plantillas/mapeo-nombres.md) y [`declaracion.py`](../../../../../validadores/declaracion.py) |
| **Épica / HU / origen** | [EP-003](../../epica.md) · [HU-005](../HU-005-modelos-de-la-capa-de-proyecto.md) · retro-documentación, fila de HU-005 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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
| **Defectos abiertos aceptados** | 1 — `D-01`, que el plan declaró cobertura completa sin contar los transversales |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) de esta fase |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | **Hecha** | Incremento en la especificación: qué dato es de cuál modelo. Va con lo que salga de T-02 |
| T-02 | **Hecha** | Caso del dato con un solo dueño — CP-001 |
| T-03 | **Hecha** | Prueba de la declaración mal escrita — CP-002 |
| T-04 | **Hecha** | Prueba del silencio sin declaración de stack — CP-003 |
| T-05 | **Hecha** | Caso del dominio declarado a medias — CP-004 |
| T-06 | **Hecha** | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 6 de 6. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| El solape se mide por dato, no por sección: lo que no puede repetirse es el dato del que hay una sola verdad | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Las declaraciones se rompen en carpeta temporal: romper a propósito la capa 3 de un proyecto vivo es tocar trabajo ajeno | §2.6 del plan |
| Probar un silencio exige comprobar que el revisor **corrió** y calló, no que no corrió. Sin eso, un programa roto pasa el caso | Riesgo `R-02` y CP-003 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del plan.** Es lo único que falta para arrancar.
- **Si aparece un dato con dos dueños** entre los tres modelos (riesgo `R-01`): se anota y se propone. Cambiar un modelo sube versión ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).
- **Si otra sesión está tocando la especificación del módulo** (riesgo `R-03`): se relee justo antes de escribir.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 9 esperando la autorización del commit, que es la puerta normal.
