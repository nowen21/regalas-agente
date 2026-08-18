# Estado de fase — Fase A-EP-001-HU-006-retrodocumentar-la-capa-del-proyecto (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-001-HU-006-retrodocumentar-la-capa-del-proyecto` |
| **Módulo** | Cuerpo de reglas — la capa propia del proyecto ([`plantillas/reglas-proyecto.md`](../../../../../plantillas/reglas-proyecto.md)) |
| **Épica / HU / origen** | [EP-001](../../epica.md) · [HU-006](../HU-006-capa-propia-del-proyecto.md) · retro-documentación, fila de HU-006 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** 6 — ejecución continua, **detenida**. **Última puerta pasada:** 5, el plan aprobado por el usuario el 2026-08-17 («autorizados los planes de trabajo»).

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 orden de bajar a fase las HU del inventario 48 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 presentado el 2026-08-17 | ☑ |
| 5 | Aprobación del plan detallado | 👤 «autorizados los planes de trabajo», 2026-08-17 | ☑ |
| 6 | Ejecución continua | 8 tareas · **detenida por las 2 dudas de §2.7** | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** La fase trabaja sobre una **copia** del proyecto elegido: en la carpeta viva de un proyecto ajeno no se escribe ([`00·N4`](../../../../../base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)).

> **El plan quedó aprobado el 2026-08-17** y la fase **no arrancó**: las 2 dudas de §2.7 del plan sigue sin resolver, y solo la puede resolver el usuario. Lo que falta ya no es la aprobación — es la respuesta.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 3 |
| **CA en "No"** | Ninguno todavía: no se ha corrido nada |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Bloqueada | Elegir el proyecto y listar sus ajustes propios. Es la duda 1, que bloquea los tres CA |
| T-02 | Bloqueada | Caso del ajuste que gana a la convención general — CP-001 |
| T-03 | Bloqueada | Caso de la regla propia sin respaldo — CP-002 |
| T-04 | Pendiente | Constancia de que la comprobación automática no corre, y sumarla al pendiente 53 |
| T-05 | Bloqueada | Caso del ajuste contra una `[BLINDADA]` — CP-003. Depende también de la duda 2 |
| T-06 | Bloqueada | El mismo ajuste sobre una convención de capa 2 — CP-004 |
| T-07 | Bloqueada | Corridas de `validar.py plantilla` y `version` sobre la copia — CP-005 |
| T-08 | Pendiente | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 0 de 8. **Bloqueadas:** T-01, T-02, T-03, T-05, T-06 y T-07 — todas por la duda 1.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Se prueba sobre un proyecto ya instalado, no sobre uno armado: un proyecto de prueba trae ajustes inventados para que la prueba pase | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| El CA-03 necesita su par: el mismo ajuste contra el núcleo y contra una convención de capa 2. Con uno solo no se distingue "no manda nunca" de "no manda sobre el núcleo" | §3.3 y CP-004 del [`plan_pruebas.md`](plan_pruebas.md) |
| El CA-02 se cierra por lectura y se dice que fue por lectura: [`validadores/metareglas.py`](../../../../../validadores/metareglas.py) no tiene punto de entrada | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) y pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md) |

---

## 3. Pendiente / preguntas abiertas

- **Duda 1 de §2.7:** sobre qué proyecto instalado se hacen las pruebas. Bloquea los tres CA.
- **Duda 2 de §2.7:** si el ajuste que contradice el núcleo se escribe en el proyecto de prueba o basta simularlo en una copia. Bloquea el CA-03.
- **La aprobación del plan.** Sin ella no arranca la ejecución.
- **Si el proyecto elegido tiene reglas propias sin respaldo** (riesgo `R-01`): se anotan y se reportan a su dueño. Limpiar trabajo ajeno no es de esta fase.

---

## 4. Si se bloqueó

- **Estación:** 6 — ejecución continua, detenida. **Motivo:** el plan **está aprobado** desde el 2026-08-17, y sin el proyecto de la duda 1 no arranca ninguno de los tres CA. **Qué falta para desbloquear:** que el usuario apruebe el plan, elija el proyecto y decida la forma del caso del CA-03.
