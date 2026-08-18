# Estado de fase — Fase A-EP-007-HU-004-retrodocumentar-la-puesta-de-los-automatismos (módulo Instalación)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-007-HU-004-retrodocumentar-la-puesta-de-los-automatismos` |
| **Módulo** | Instalación — [`validadores/instalar.py`](../../../../../validadores/instalar.py) y los seis enganches |
| **Épica / HU / origen** | [EP-007](../../epica.md) · [HU-004](../HU-004-generar-los-automatismos.md) · retro-documentación, fila de HU-004 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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

**Nada se ejecutó todavía.** Ningún enganche real se rompe para probar: el fallo se simula.

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
| T-01 | **Hecha** | Caso de los seis enganches registrados — CP-001 |
| T-02 | **Hecha** | Caso de que cada uno se dispara en su momento — CP-002 |
| T-03 | **Hecha** | Prueba del enganche que falla — CP-003 |
| T-04 | **Hecha** | Tabla de los seis, con su momento y su fallo — CP-004 |
| T-05 | **Hecha** | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 5 de 5. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| El fallo se **simula**: romper un enganche real del repositorio afecta a todas las sesiones abiertas | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| La tabla de los seis se levanta **del instalador**, no de la documentación: lo que corre es lo que él registra, y la documentación puede estar vieja | §2.6 del plan y riesgo `R-03` |
| El CA-02 se prueba con un fallo de verdad, no con un aviso: un aviso que no traba no prueba que un fallo tampoco trabe | §2.6 del plan |
| Se prueba la función de cada enganche, separada del disparo: abrir sesiones reales para probar ensuciaría el histórico | Riesgo `R-02` del plan |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del plan.** Es lo único que falta para arrancar: §2.7 no dejó dudas.
- **Si un enganche sí detiene el trabajo al fallar** (riesgo `R-01`): se para y se reporta de inmediato. La herramienta quedaría trabada para todos.
- **El módulo de instalación no tiene especificación aparte**; los enganches sí la tienen, en [`documentacion/automatismos/spec.md`](../../../../automatismos/spec.md). Lo que esta HU cubre es **ponerlos**.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 9 esperando la autorización del commit, que es la puerta normal.
