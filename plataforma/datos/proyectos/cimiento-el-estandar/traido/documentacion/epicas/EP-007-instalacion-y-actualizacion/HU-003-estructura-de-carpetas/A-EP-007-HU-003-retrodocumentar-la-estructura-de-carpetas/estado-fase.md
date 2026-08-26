# Estado de fase — Fase A-EP-007-HU-003-retrodocumentar-la-estructura-de-carpetas (módulo Instalación)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-007-HU-003-retrodocumentar-la-estructura-de-carpetas` |
| **Módulo** | Instalación — [`instalar.py`](../../../../../validadores/instalar.py), [`estructura.py`](../../../../../validadores/estructura.py) y [`estructura-base.md`](../../../../../base/02-flujo-de-trabajo/estructura-base.md) |
| **Épica / HU / origen** | [EP-007](../../epica.md) · [HU-003](../HU-003-estructura-de-carpetas.md) · retro-documentación, fila de HU-003 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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

**Nada se ejecutó todavía.** Todas las corridas van sobre carpetas temporales: ningún proyecto vivo se instala ni se actualiza.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 2 de 2, y los dos transversales |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | 1 — `D-01`, que el plan declaró cobertura completa sin contar los transversales |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) de esta fase |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | **Hecha** | Caso de la instalación en carpeta vacía — CP-001 |
| T-02 | **Hecha** | Prueba de que no se pisa contenido — CP-002 |
| T-03 | **Hecha** | Caso de instalar dos veces — CP-003 |
| T-04 | **Hecha** | Caso de la carpeta quitada — CP-004 |
| T-05 | **Hecha** | Anotar cómo se lee la revisión en esta casa — CP-005 |
| T-06 | **Hecha** | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 6 de 6. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| La prueba de que no pisa usa archivos **con contenido**: pisar es perder contenido, y una carpeta que sigue ahí con un archivo vacío se ve igual de bien | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Instalar dos veces es un caso propio: es la forma en que esto se rompe de verdad, porque **la segunda corrida es la que borra** | §2.6 del plan |
| El resultado de la revisión sobre esta casa se explica en el `resultado_pruebas`: quien lo lea tiene que entender por qué reprueba acá sin reconstruirlo | §2.6 del plan y riesgo `R-03` |
| Si el CA-02 falla, la fase **se detiene y se reporta**: un instalador que borra trabajo es un defecto grave, y corregirlo es una fase con su propio plan | Riesgo `R-01` del plan |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del plan.** Es lo único que falta para arrancar: §2.7 no dejó dudas.
- **El módulo de instalación no tiene especificación aparte.** Se declara como deuda en las fases hermanas de esta épica.
- **La revisión reprueba en esta casa con razón**: falta el planteamiento del propio estándar (pendiente [56](../../../../../pendientes/hecho/el-estandar-tiene-su-planteamiento.md)). No se arregla acá; se explica.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 9 esperando la autorización del commit, que es la puerta normal.
