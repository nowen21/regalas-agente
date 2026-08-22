# Estado de fase — Fase A-EP-001-HU-010-cuando-la-historia-hace-de-especificacion (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-001-HU-010-cuando-la-historia-hace-de-especificacion` |
| **Módulo** | Cuerpo de reglas — [`02·F2`](../../../../../base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md) |
| **Épica / HU / origen** | [EP-001](../../epica.md) · [HU-010](../HU-010-cuando-no-aplica-la-especificacion.md) · ✨ funcionalidad nueva, bajada del pendiente [20](../../../../../pendientes/hecho/cuando-la-historia-hace-de-especificacion.md) por [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md). Fila de HU-010 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
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
| 6 | Ejecución continua | la frase nueva en `F2` y su checklist | ☑ |
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
| **CA cumplidos** | 0 de 2 |
| **CA en "No"** | Ninguno todavía: no se ha corrido nada |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

> **Puesto al día el 2026-08-22.** Este documento decía que no se había ejecutado ninguna tarea, y la fase estaba **hecha y probada**: su [resultado_pruebas](resultado_pruebas.md) trae el veredicto y su [funcionalidad_implementada](funcionalidad_implementada.md) el cierre. Lo que faltaba era este archivo, que es justo el que una sesión nueva lee para saber por dónde va. Sale del [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md).

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | Escribir en `F2` lo que decida la duda 1. Las tres dudas la bloquean |
| T-02 | Hecha | Rehacer el bloque de checklist de `F2`: cambiar el texto anula el sello anterior |
| T-03 | Hecha | Criterio de la fase mezclada — CP-002 |
| T-04 | Hecha | Caso del lector ajeno — CP-001 |
| T-05 | Hecha | Levantar la tabla de fases. **Es medición y no depende de ninguna duda** |
| T-06 | Hecha | Caso de `validar.py flujo` — CP-004 |
| T-07 | Hecha | Corregir la cuenta del pendiente 20 y cerrarlo si la regla lo resuelve |
| T-08 | Hecha | Corregir el CA-02 de la HU, que dice dos fases cuando son más |
| T-09 | Hecha | Caso de no regresión sobre código de módulo — CP-005 |
| T-10 | Hecha | Versionar, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 10 de 10. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| El pendiente 20 hablaba de dos fases; contadas el 2026-08-17 son muchas más. Un pendiente con la cuenta vieja hace decidir sobre un dato falso, así que se corrige y no se borra | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Lo que se decida vale **hacia adelante**: ninguna fase cerrada se reabre, porque eso desordena la trazabilidad de lo ya sellado | RN-05 de la HU y §2.6 del plan |
| Una regla que hay que explicar para que se entienda no resolvió el problema: el CA-01 se prueba con alguien que no estuvo en la decisión | §3.3 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **Duda 1 de §2.7:** cuál de los dos caminos del pendiente 20 — escribirle a `F2` la excepción con sus tres partes, o aceptar en la regla que la historia hace de especificación cuando el entregable no es código.
- **Duda 2 de §2.7:** si el caso cubre solo el estándar o cualquier proyecto cuyo entregable no sea código.
- **Duda 3 de §2.7:** si `flujo.py` tiene que distinguir las dos formas de llenar la casilla o le basta con que el archivo exista. Si la respuesta obliga a tocar `flujo.py`, **el plan se amplía antes de editarlo**.
- **La aprobación del plan.** Sin ella no se toca `base/`.

---

## 4. Si se bloqueó

- **Estación:** 4 — pausa y presentación. **Motivo:** las tres dudas de §2.7 bloquean toda la construcción; solo la medición de T-05 puede avanzar. **Qué falta para desbloquear:** que el usuario apruebe el plan y elija el camino de la duda 1, del que dependen las otras dos.

---

## Lo que la desbloqueó

**Las dudas de la §2.7 quedaron decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md). La decisión está escrita en el propio plan, con su motivo.

**La fase no arrancó todavía:** decidir no es ejecutar.
