# Estado de fase — Fase B-EP-004-HU-002-el-analizador-ve-todas-las-reglas (módulo Comprobación automática)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `B-EP-004-HU-002-el-analizador-ve-todas-las-reglas` |
| **Módulo** | Comprobación automática — [`validadores/metareglas.py`](../../../../../validadores/metareglas.py) |
| **Épica / HU / origen** | [EP-004](../../epica.md) · [HU-002](../HU-002-marca-de-comprobable-en-cada-regla.md) · **defecto** de la fase [`A`](../A-EP-004-HU-002-retrodocumentar-la-clasificacion-de-cada-regla/resultado_pruebas.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** 4 — pausa y presentación. **Última puerta pasada:** 3, con el plan de trabajo y el plan de pruebas escritos.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 🐞 el veredicto «No cumple» de la fase A | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 pendiente: falta presentarlo | ☐ |
| 5 | Aprobación del plan detallado | 👤 pendiente | ☐ |
| 6 | Ejecución continua | 10 tareas, ninguna empezada | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** **Cierra además el punto 2 del [pendiente 53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md)**, y **sube MAYOR**: la regla sin clasificar pasa a detener.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 2. El CA-02 ya estaba en «Sí» tras la fase A y hay que mantenerlo |
| **CA en "No"** | El **CA-01** y el **CA-03** vienen en «No» desde la fase A, y son lo que esta viene a cerrar |
| **Defectos abiertos aceptados** | Ninguno propio. Hereda los dos de la fase A, que son su motivo |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Pendiente | Reconocer las reglas escritas con `###` |
| T-02 | Pendiente | Reconocer las sub-reglas escritas como viñeta |
| T-03 | Pendiente | Destapar la prueba del analizador |
| T-04 | Pendiente | **Listar** las que aparezcan sin clasificar, sin clasificarlas |
| T-05 | Pendiente | Su subcomando en `validar.py` |
| T-06 | Pendiente | La fila 18 pasa de aviso a **falla** |
| T-07 | Pendiente | Destapar la prueba de la puerta |
| T-08 | Pendiente | Caso: las derogadas siguen sin que se les reclame nada — CP-005 |
| T-09 | Pendiente | Escribir qué cuenta como regla para el analizador |
| T-10 | Pendiente | Cerrar el punto 2 del pendiente 53, correr y cerrar la trazabilidad |

**Hechas:** 0 de 10. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| **El programa se adapta a lo escrito, no al revés.** Reescribir el capítulo 16 para acomodar al analizador invertiría quién manda — y el día que alguien vuelva a usar `###`, el defecto vuelve | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| Lo que aparezca sin clasificar **se lista y no se clasifica acá**: decidir si una regla es validable no es trabajo de una fase que arregla un analizador | §2.6 del plan y CP-004 paso 4 |
| El conteo se comprueba **contra el árbol**, no contra un número escrito en la prueba: un número solo dice que no cambió | CP-001 paso 1 |
| **El riesgo real son las cinco `F4.x` derogadas**, que estaban invisibles y ahora entran. Si la fila que las salta no las reconoce, aparecen cinco falsos incumplimientos el mismo día en que la falla empieza a detener | CP-005 y riesgo `R-02` |
| Que aparezcan muchos hallazgos nuevos del checklist **es lo que se busca**, no un problema: llevan versiones sin comprobarse | Riesgo `R-01` |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del plan.** Es lo único que falta para arrancar: §2.7 no dejó dudas.
- **Qué hacer con lo que aparezca sin clasificar** (T-04): se lista en esta fase y se decide después. Clasificarlas es de [`EP-001 · HU-009`](../../../EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/HU-009-reglas-sin-checklist-al-dia.md).
- **Sube MAYOR**, así que hay que avisar a los proyectos que heredan: los suyos empiezan a reprobar si escriben reglas propias sin clasificar.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 4 esperando la aprobación del plan, que es la puerta normal, no un bloqueo.
