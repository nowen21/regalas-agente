# Estado de fase — Fase A-EP-004-HU-017-la-corrida-cuenta-las-hu-sin-fase (módulo Comprobación automática)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-017-la-corrida-cuenta-las-hu-sin-fase` |
| **Módulo** | Comprobación automática — [`validadores/fases.py`](../../../../../validadores/fases.py) |
| **Épica / HU / origen** | [EP-004](../../epica.md) · [HU-017](../HU-017-inventario-de-hu-sin-fase.md) · ✨ funcionalidad nueva, nacida del hallazgo H-1 del [inventario de HU](../../../../../historico-chat/resumenes/2026-08-16/las-hu-sin-su-fase.md). Fila de HU-017 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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

**Nada se ejecutó todavía.** §2.7 no dejó dudas abiertas: el criterio de «completa» lo fija el tablero, y los bordes están verificados en el árbol.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 4 de 4, y los dos transversales |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | 1 — `D-01`, que el plan declaró cobertura completa sin contar los transversales |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) de esta fase |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | **Hecha** | La línea con total, completas e incompletas |
| T-02 | **Hecha** | Caso del árbol de dos HU — CP-001 |
| T-03 | **Hecha** | Prueba de que el total es el número de carpetas — CP-002 |
| T-04 | **Hecha** | Que la HU con varias fases cuente completa solo si todas lo están |
| T-05 | **Hecha** | Caso de la HU con dos fases — CP-003 |
| T-06 | **Hecha** | Los dos bordes: épica sin HU y carpeta HU sin archivo |
| T-07 | **Hecha** | Caso de los bordes — CP-004 |
| T-08 | **Hecha** | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 8 de 8. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| La cuenta va en el programa que ya recorre el árbol: recorrerlo dos veces da dos verdades el día que uno de los dos se quede viejo | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| «Completa» es la HU cuyas fases tienen sus cinco documentos, que es el criterio del tablero. Cambiarlo haría que los dos números no se puedan comparar, y compararlos es para lo que sirven | §2.6 del plan |
| La cuenta se **reporta**, no se escribe en el tablero: un programa que edita el backlog pisa lo que otra sesión esté escribiendo | §2.6 del plan |
| Contar informa y no falla: un total alto que dejara el proyecto en rojo haría que el conteo se saque | Riesgo `R-02` y CP-005 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del plan.** Es lo único que falta para arrancar.
- **La cuenta del programa y la del tablero pueden no coincidir** (riesgo `R-01`): manda la corrida, y el resultado anota cuál era la diferencia el día que se midió.
- **Esta HU cuenta, no llena** (riesgo `R-03`): el pendiente [48](../../../../../pendientes/48-inventario-hu.md) sigue llenándose a mano.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 9 esperando la autorización del commit, que es la puerta normal.
