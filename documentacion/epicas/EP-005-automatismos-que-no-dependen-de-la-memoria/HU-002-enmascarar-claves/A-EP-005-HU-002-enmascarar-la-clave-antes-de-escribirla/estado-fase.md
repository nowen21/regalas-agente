# Estado de fase — Fase A-EP-005-HU-002-enmascarar-la-clave-antes-de-escribirla (módulo Automatismos)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-005-HU-002-enmascarar-la-clave-antes-de-escribirla` |
| **Módulo** | Automatismos — [`hook_historico.py`](../../../../../validadores/hook_historico.py) y el reconocimiento de [`secretos.py`](../../../../../validadores/secretos.py) |
| **Épica / HU / origen** | [EP-005](../../epica.md) · [HU-002](../HU-002-enmascarar-claves.md) · ✨ funcionalidad nueva. Fila de HU-002 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** 8 — cierre documental. **Última puerta pasada:** 7, veredicto **Cumple**.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 orden de bajar a fase las HU del inventario 48 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 presentado el 2026-08-17 | ☑ |
| 5 | Aprobación del plan detallado | 👤 «autorizados los planes de trabajo», 2026-08-17 | ☑ |
| 6 | Ejecución continua | 6 tareas | ☑ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☑ Cumple, ciclo 1 |
| 8 | Cierre documental | trazabilidad sin faltantes | ☑ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |



---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 2 de 2 |
| **CA en «No»** | Ninguno |
| **Defectos abiertos aceptados** | dos: las transcripciones viejas sin revisar, y lo que se escribe fuera del histórico |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §6 |

---

> **Puesto al día el 2026-08-22.** Este documento decía que no se había ejecutado ninguna tarea, y la fase estaba **hecha y probada**: su [resultado_pruebas](resultado_pruebas.md) trae el veredicto y su [funcionalidad_implementada](funcionalidad_implementada.md) el cierre. Lo que faltaba era este archivo, que es justo el que una sesión nueva lee para saber por dónde va. Sale del [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md).

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | Escribir el enmascarado reusando lo que `secretos.py` reconoce |
| T-02 | Hecha | Que el enganche lo llame antes de escribir |
| T-03 | Hecha | Caso de la clave que no queda en claro — CP-001 |
| T-04 | Hecha | La marca que dice qué se tapó. Duda 1 |
| T-05 | Hecha | Caso del mensaje legible — CP-002. Depende de T-04 |
| T-06 | Hecha | Caso del ejemplo que no se tapa — CP-003 |
| T-07 | Hecha | Correr, escribir el incremento de la especificación y cerrar la trazabilidad |

**Hechas:** 7 de 7. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| El enmascarado reusa el reconocimiento de `secretos.py`: dos reconocedores distintos taparían y detectarían cosas distintas, y el peor caso es que uno tape y el otro no | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Si el enmascarado se cae, la transcripción **se escribe igual**: perder el rastro de la sesión por un fallo del enmascarado es cambiar un riesgo por otro peor | §2.6 del plan y CP-004 del [`plan_pruebas.md`](plan_pruebas.md) |
| La marca dice que hubo una clave, no cuál: sin marca no se entiende el mensaje, y con la clave el enmascarado no sirvió de nada | §2.6 del plan |
| Las transcripciones viejas **no se reescriben**. Si hay una clave vieja, es un incidente y lo decide el usuario | §2.6 del plan y capítulo de registros inmutables |

---

## 3. Pendiente / preguntas abiertas

- **Duda 1 de §2.7:** con qué marca se tapa, para que se vea que hubo algo y no se confunda con texto del usuario. Bloquea T-04 y T-05.
- **Duda 2 de §2.7:** qué se hace si aparece una clave en una transcripción vieja. **No bloquea esta fase**: define qué hacer si el hallazgo aparece.
- **La aprobación del plan.** Se toca el enganche que corre en cada mensaje.
- **Esta fase completa el CA-02 de [EP-001 · HU-003](../../../EP-001-cuerpo-de-reglas-heredable/HU-003-nucleo-que-no-se-sobrescribe/HU-003-nucleo-que-no-se-sobrescribe.md)**, que quedó cumplido a medias porque el enmascarado no existía.
- **Si aparece una clave real en una transcripción vieja** (riesgo `R-03`): se para, se reporta y no se reescribe nada por cuenta propia.

---

## 4. Si se bloqueó

- **Estación:** 6 — ejecución continua, detenida. **Motivo:** el plan **está aprobado** desde el 2026-08-17, y la duda 1 bloquea la marca y su caso. **Qué falta para desbloquear:** que el usuario apruebe el plan y elija la marca. El enmascarado y los otros dos casos pueden arrancar apenas se apruebe.

---

## Lo que la desbloqueó

**Las dudas de la §2.7 quedaron decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md). La decisión está escrita en el propio plan, con su motivo.

**La fase no arrancó todavía:** decidir no es ejecutar.

---

## Lo que quedó, en una línea

**Una clave pegada en el chat ya no llega a la transcripción.** Se tapa **antes** de escribir, porque una vez en el archivo la transcripción se versiona y de ahí no se borra.

La mitad del trabajo fue **no tapar de más**: el molde y la línea que lee del entorno se quedan como están.
