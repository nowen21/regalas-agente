# Plan de Trabajo — Fase A-EP-001-HU-011-la-regla-de-buscar-antes-de-preguntar (módulo Cuerpo de reglas)

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en [HU-011](../HU-011-buscar-antes-de-preguntar.md); las pruebas, en el [plan_pruebas.md](plan_pruebas.md); lo que dieron, en el [resultado_pruebas.md](resultado_pruebas.md); lo que quedó, en el [funcionalidad_implementada.md](funcionalidad_implementada.md).

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-001-HU-011-la-regla-de-buscar-antes-de-preguntar` |
| **Épica** | [EP-001 Cuerpo de reglas heredable](../../epica.md) |
| **HU** | [HU-011 Buscar en el repositorio antes de preguntar](../HU-011-buscar-antes-de-preguntar.md) — una sola (`F12.1`) |
| **Módulo** | Cuerpo de reglas — capítulo `01 · Conducta de la IA` |
| **Especificación del módulo** | La propia HU. El entregable es una regla: sus criterios de aceptación y el [checklist del estándar](../../../../../base/20-meta-reglas/checklist.md) son la especificación |
| **Fecha apertura** | 2026-08-18 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): ✨ **Funcionalidad nueva.** No hay fase previa en esta HU. La historia nació el 2026-08-17 al enrutar el backlog, con el texto que el propio pendiente traía redactado.

**De dónde sale:** el [pendientes/hecho/buscar-en-el-repositorio-antes-de-preguntar.md](../../../../../pendientes/hecho/buscar-en-el-repositorio-antes-de-preguntar.md), del hallazgo H-1 del 2026-08-14.

**CA de la HU que cubre esta fase**

| CA | Qué exige | Estado al abrir |
|---|---|---|
| [CA-01](../HU-011-buscar-antes-de-preguntar.md) | Lo que ya está escrito no se pregunta | **No existía la regla** |
| [CA-02](../HU-011-buscar-antes-de-preguntar.md) | Lo que no está escrito sí se pregunta, diciendo dónde se buscó | — |
| [CA-03](../HU-011-buscar-antes-de-preguntar.md) | Lo escrito que contradice el pedido se muestra | — |

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que el agente no le devuelva al usuario el trabajo de leer lo que él mismo dejó escrito.

**El caso que la originó.** El 2026-08-14 el agente preguntó en qué orden trabajar dos historias y ofreció tres opciones. La respuesta estaba en la §9 de una de ellas, que declaraba la dependencia con impacto alto. **La pregunta tenía premisa falsa:** cualquiera de las tres respuestas habría contradicho algo ya decidido.

**Fuera de alcance:**

- **Reducir las preguntas.** Preguntar lo que de verdad no está decidido es lo que evita adivinar, y la regla no lo toca. Cambia **cuáles**, no cuántas.
- **La comprobación automática.** Que el agente haya buscado no lo puede ver ningún programa. Queda declarado en `reglas-validables.md` y la mitad comprobable —que la respuesta traiga su cita— se escribe aparte.
- **Qué manda cuando el brief y el histórico se contradicen.** Es un hueco propio, anotado en el punto 8 del [pendientes/hecho/lo-que-quedo-abierto-en-las-sesiones-viejas.md](../../../../../pendientes/hecho/lo-que-quedo-abierto-en-las-sesiones-viejas.md).

---

## 2. Análisis previo — línea base verificada  ·  `F17`

**Medido el 2026-08-18 contra el repositorio:**

| Qué | Cuánto |
|---|---|
| Reglas del capítulo `01` | 22, la última `C22` |
| Próximo identificador libre | **`C23`** |
| Reglas del cuerpo con su bloque de checklist | 200 de 200 |

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `base/01-conducta.md` | Modificar | La regla `C23` con su bloque de checklist |
| `validadores/reglas-validables.md` | Modificar | `C23` clasificada, con el motivo de por qué es validable a medias |
| `CHANGELOG.md` · `VERSION` | Modificar | Entrada **MENOR**: regla nueva, aditiva |

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **Extiende `01·C7`** | No declarar dependencia | `C7` manda preguntar ante dos lecturas y **da por hecho que el dato no está**. Esta agrega el paso previo, así que la extiende — no la repite |
| El orden va **en el cuerpo**, nombrado | Dejarlo al criterio de cada sesión | Sin orden fijo, cada sesión busca en un sitio distinto y la regla no se puede cumplir igual dos veces |
| El **porqué** del orden va a la HU | Dejarlo en la regla | No cabía: el cuerpo medía 368 caracteres para un molde de 320. Es lo que la fila 10 manda hacer con el razonamiento |
| Validable **a medias**, y declarado | Declararla no validable | Que se haya buscado no se ve; que la respuesta traiga su cita, sí. Decir «no validable» cerraría la puerta a la mitad que sí se puede |

### 2.7 Dudas por resolver antes de escribir

**Ninguna abierta.** La única que la HU dejaba —el orden de búsqueda— se resolvió con lo que el propio repositorio ya declara: **la historia y su §9 · la épica · el resumen de sesión · el histórico · la memoria**. De lo más específico a lo más general, parando en cuanto se encuentra. No es una preferencia: es dónde el estándar manda escribir cada cosa.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Comprobar el próximo identificador libre del capítulo | Cuerpo de reglas | 0,25 h | — | EV-01 |
| T-02 | Escribir `C23` con el molde de `M5` | Cuerpo de reglas | 0,75 h | T-01 | EV-02 |
| T-03 | Aplicarle el checklist de las veinte filas | Cuerpo de reglas | 0,75 h | T-02 | EV-02 |
| T-04 | Recortar el cuerpo hasta que quepa | Cuerpo de reglas | 0,25 h | T-03 | EV-03 |
| T-05 | Clasificarla en `reglas-validables.md` | Documentación | 0,25 h | T-02 | EV-04 |
| T-06 | Comprobar que ninguna corrida se rompió | Test | 0,25 h | T-04 | EV-05 |
| T-07 | Entrada en `CHANGELOG.md` y subir `VERSION` | Versionado | 0,25 h | T-06 | — |

**Total estimado:** 2,75 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-04 → T-06 → T-07.

**T-03 va antes que T-04 y no al revés.** Aplicar el checklist es lo que destapó que no cabía; recortar primero habría sido recortar a ojo.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| CA-01, CA-02, CA-03 | La regla los cubre en su cuerpo; se comprueban leyéndola contra cada uno | EV-02 | ☑ |
| `M14` · nace con su checklist | El bloque, aplicado y con resultado | EV-02 | ☑ |
| `M5` · cabe en el molde | Medida con `validar.py metareglas` | EV-03 | ☑ |
| `M9` · declarada validable o no | Registrada con su motivo | EV-04 | ☑ |
| No regresión | Las dos suites y las corridas de siempre | EV-05 | ☑ |

---

## 6. Datos y ambiente de prueba

No aplica: el entregable es texto. Se comprueba con los programas del propio repositorio.

---

## 7. Reversión / rollback

Se revierte volviendo el commit atrás. La regla es aditiva: ningún proyecto al día tiene que hacer nada para seguir cumpliendo.

---

## 8. Producción y migración incremental

**Es aditiva y no obliga a migrar.** Un proyecto que herede la versión nueva recibe una exigencia más sobre cómo se le pregunta, y nada de lo que ya hacía deja de valer.

---

## 9. Reglas del estándar aplicadas

[`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), [`20·M4`](../../../../../base/20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md), [`20·M5`](../../../../../base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md), [`20·M7`](../../../../../base/20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md), [`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md), [`20·M14`](../../../../../base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que la regla se lea como «no preguntes» y el agente empiece a adivinar | Alto | El fuera de alcance está en la HU y en el bloque de checklist, fila 16 | **Cerrado** |
| B-02 | Que el orden se vuelva ritual y se busque en los cinco sitios siempre | Medio | El orden para en cuanto se encuentra, y va de lo más específico a lo más general | **Cerrado** |
| B-03 | Que nadie la haga cumplir, como pasó con `ID9` | Alto | Queda declarada validable a medias; la mitad comprobable espera su fase | Abierto |

---

## 11. Definition of Done

- [x] `C23` escrita con el molde de `M5`
- [x] Su bloque de checklist aplicado, con resultado **CUMPLE**
- [x] Cabe: 271 de 320
- [x] Clasificada en `reglas-validables.md` con su motivo
- [x] Las dos suites en verde y `validar.py estandar` sin incumplimientos
- [x] Versionada
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md) de esta fase.
