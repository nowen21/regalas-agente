# Estado de fase — Fase A-EP-001-HU-008-retrodocumentar-la-derogacion (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-001-HU-008-retrodocumentar-la-derogacion` |
| **Módulo** | Cuerpo de reglas — la derogación ([`20·M11`](../../../../../base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md)) y [`validadores/version.py`](../../../../../validadores/version.py) |
| **Épica / HU / origen** | [EP-001](../../epica.md) · [HU-008](../HU-008-derogacion-sin-borrar.md) · retro-documentación, fila de HU-008 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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
| 6 | Ejecución continua | 8 tareas, las 8 hechas | ☑ |
| 7 | Pruebas | [`resultado_pruebas.md`](resultado_pruebas.md) con veredicto **Cumple** | ☑ |
| 8 | Cierre documental | [`funcionalidad_implementada.md`](funcionalidad_implementada.md), §8 de la HU y fila del inventario 48 | ☑ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** Esta fase es de las pocas de la épica **sin dudas abiertas**: arranca en cuanto se apruebe el plan.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 3 de 3, y los dos transversales |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | 2 — `D-01`, que la vigilancia vive en `metareglas.py`, sin punto de entrada (pendiente 53); `D-02`, que el plan declaró cobertura completa sin contar los transversales |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) de esta fase |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | **Hecha** | Prueba de que cada derogación conserva archivo y cuerpo — CP-001 |
| T-02 | **Hecha** | Caso de la marca completa — CP-002 |
| T-03 | **Hecha** | Prueba de que ningún identificador derogado vuelve — CP-003 |
| T-04 | **Hecha** | Caso del consecutivo que no reutiliza — CP-004 |
| T-05 | **Hecha** | Caso de la derogada que no cuenta como incumplimiento — CP-005 |
| T-06 | **Hecha** | Constancia de qué mitad la comprueba un programa que corre |
| T-07 | **Hecha** | Corrida completa con su número — CP-006 |
| T-08 | **Hecha** | Escribir el resultado y cerrar la trazabilidad |

**Hechas:** 8 de 8. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| La lista de derogaciones se lee del cuerpo, no se escribe a mano dentro de la prueba: una lista escrita envejece con la primera derogación nueva y la prueba pasa a mentir | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Código que no se puede correr no comprueba nada. El CA-03 dice por qué camino se comprueba cada mitad, en vez de darse por cumplido porque el código lo contempla | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| El número de pruebas se anota **antes** de tocar la suite: sin línea base no se distingue lo propio de lo heredado cuando aparece rojo | §3.3 del [`plan_pruebas.md`](plan_pruebas.md) y riesgo `R-01` |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del plan.** Es lo único que falta para arrancar: §2.7 no dejó ninguna duda abierta.
- **[`validadores/metareglas.py`](../../../../../validadores/metareglas.py) no se puede correr** (pendiente [53](../../../../../pendientes/53-enlaces-py-no-tiene-punto-de-entrada.md)): la mitad del CA-03 que vive ahí queda sin comprobación automática, y el resultado tiene que decirlo.
- **Si otra sesión está tocando `validadores/pruebas.py`** (riesgo `R-03`): se guarda solo lo propio.
- **Si aparece una regla que debería estar derogada y no lo está** (riesgo `R-04`): se propone. Derogar lo decide el usuario.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 9 esperando la autorización del commit, que es la puerta normal.
