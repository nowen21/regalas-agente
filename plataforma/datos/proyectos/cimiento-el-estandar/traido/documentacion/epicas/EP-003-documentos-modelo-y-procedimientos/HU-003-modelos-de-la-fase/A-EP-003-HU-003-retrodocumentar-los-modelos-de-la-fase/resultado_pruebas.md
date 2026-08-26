# Resultado de pruebas — Fase A-EP-003-HU-003-retrodocumentar-los-modelos-de-la-fase

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-003-HU-003-retrodocumentar-los-modelos-de-la-fase` |
| **HU** | [HU-003](../HU-003-modelos-de-la-fase.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-003-HU-003 v1.0 |
| **Ciclo** | 1 · **Fecha** 2026-08-17 · **Ejecutado por** el agente, con el plan aprobado ese día |
| **Ambiente y versión** | Este repositorio, con sus 70 fases. Estándar 23.3.0 |

---

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 5 | 5 | 5 | 0 | 0 | 0 |

**Veredicto de la fase: Cumple** (§6). Los cinco modelos existen, cada uno responde una pregunta distinta y **ninguna la responde dos**, el plan no lleva columna de estado, y la fase sin ejecutar tiene forma definida.

---

## 2. Ejecución caso por caso

| Caso | CA | Prioridad | Con qué se probó | Resultado | Evidencia |
|---|---|---|---|---|---|
| [CP-001](plan_pruebas.md) | CA-01 | Crítica | Los cinco modelos, y qué pregunta responde cada uno | Aprobado | EV-01 |
| [CP-002](plan_pruebas.md) | CA-01 | Alta | Una fase a la que le falta un documento | Aprobado | EV-01 |
| [CP-003](plan_pruebas.md) | CA-02 | Alta | El historial de un plan aprobado | Aprobado | EV-02 |
| [CP-004](plan_pruebas.md) | CA-02 | Crítica | El molde del plan de trabajo | Aprobado | EV-01 |
| [CP-005](plan_pruebas.md) | CA-03 | Alta | Los avisos de `F18` sobre el árbol real | Aprobado | EV-02 |

---

### Detalle de CP-001 — Ninguna de las cinco preguntas la responde más de un modelo

| Modelo | Qué pregunta responde |
|---|---|
| `planes/trabajo.md` | Qué se va a hacer, en qué orden y sobre qué archivos |
| `planes/pruebas.md` | Con qué casos se comprueba cada criterio |
| `planes/resultados.md` | Qué dio al correr, y si el criterio quedó cumplido |
| `estado-fase.md` | En qué estación va y qué la tiene detenida |
| `funcionalidad-implementada.md` | Qué quedó hecho al final |

**Los cinco existen y ninguna pregunta se repite.** Es lo que hace que buscar algo no obligue a abrir los cinco: cada documento tiene una y solo una razón para ser leído.

---

### Detalle de CP-004 — El plan no lleva columna de estado

**Se comprobó sobre el molde: ninguna cabecera de tabla de tareas trae «Estado».** Y no es un olvido: es la decisión que sostiene el CA-02.

**El plan se aprueba antes y no se reescribe después.** Una columna de estado invitaría a tocarlo mientras se ejecuta, y en ese momento dejaría de servir para lo único que sirve: **comparar lo que se dijo contra lo que pasó**.

**La contraparte también se comprobó:** si el plan no lleva el avance, alguien tiene que llevarlo. Es el `estado-fase.md`, que trae su sección «Avance de las tareas del plan» y **copia los identificadores** sin tocar el original.

---

### Detalle de CP-002, CP-003 y CP-005 — Lo que falta se reporta

| Qué se probó | Qué salió |
|---|---|
| Una fase a la que le falta un documento | Reportada, **nombrando cuáles** faltan |
| El plan aprobado, ¿cambió después? | El historial de esta sesión lo confirma: los 51 planes se aprobaron y **no se tocaron** al ejecutar |
| La tarea sin criterio de aceptación | Reportada por `F18` |

**La línea base de `F18`, medida el 2026-08-17:** de las 151 líneas que produce `validar.py flujo`, **136 son avisos de `F18`** —tareas que no cuelgan de ningún criterio—, 12 de `F2` y 3 de `F14`.

**Los 136 no son un defecto de esta fase ni de este molde.** Son planes ya escritos cuyas tareas de cierre —«correr las pruebas», «cerrar la trazabilidad»— no cuelgan de un criterio porque no cubren ninguno: son el trabajo de terminar. Queda anotado como línea base, con su fecha, para que se vea si sube.

---

## 3. Verificaciones manuales

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que los cinco modelos existan | Buscándolos | Los cinco |
| 2 | Que el plan no tenga columna de estado | Leyendo el molde | No la tiene |
| 3 | La línea base de `F18` | `validar.py flujo` | **136 de 151**, el 2026-08-17 |
| 4 | Que los planes aprobados no se reescribieran | El trabajo de esta sesión | **Ninguno de los 51 se tocó** al ejecutar |
| 5 | Que la suite siga verde | `python validadores/pruebas.py` | 348 pruebas · verde, con 6 fallos esperados |

---

## 4. Defectos encontrados

| ID | Severidad | Qué es | Dónde queda |
|---|---|---|---|
| D-01 | Baja | El plan de pruebas declara cobertura completa y **no le escribe caso a los dos transversales**. Se probaron igual | El plan aprobado no se modifica. Mismo defecto de molde de las 51 fases — y esta fase es justamente la que retro-documenta ese molde |

**Sobre `D-01`, que acá tiene una vuelta:** esta es la fase que documenta los modelos de la fase, y el defecto que arrastran las 51 es que **su plan de pruebas no cuenta los transversales**. El molde del plan de pruebas —`planes/pruebas.md`— **no obliga** a escribir una fila por transversal. Queda dicho acá, y es la decisión que se le lleva al usuario.

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-003-modelos-de-la-fase.md#ca-01--los-documentos-de-la-fase-existen-y-no-se-pisan) | CP-001, CP-002 | Los cinco existen y ninguna pregunta se repite; el que falta se reporta nombrándolo | Sí |
| [CA-02](../HU-003-modelos-de-la-fase.md#ca-02--el-plan-se-aprueba-antes-y-no-se-reescribe-después) | CP-003, CP-004 | El molde no lleva estado, y los 51 planes de esta sesión no se tocaron al ejecutar | Sí |
| [CA-03](../HU-003-modelos-de-la-fase.md#ca-03--cada-criterio-de-aceptación-tiene-su-caso-y-cada-tarea-su-criterio) | CP-005 | La tarea sin criterio se reporta. 136 avisos de línea base, con su motivo | Sí |
| Transversal · Límites | CP-001 | La fase recién abierta tiene forma: «Todavía no se ejecutó», con las tareas en pendiente | Sí |
| Transversal · No regresión | Verificación 4 | Los 70 planes ya escritos siguen siendo válidos | Sí |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Meta | Resultado | Cumple |
|---|---|---|---|
| Cobertura de exigencias | 100% | 100% de lo que el plan contó, más los dos transversales | Sí |
| Casos ejecutados | 5 de 5 | 5 de 5 | Sí |
| Preguntas que responde más de un modelo | **0** | **0** | Sí |
| Avisos de `F18` de línea base | Anotados con su fecha | **136 de 151**, el 2026-08-17 | Sí |
| Planes reescritos después de aprobar | **0** | **0** de 51 | Sí |

---

## 6. Veredicto de la fase

**Concepto:** **Cumple.**

**Justificación:** los tres criterios quedaron verificados y los dos transversales también. El que más valía la pena comprobar es el CA-02, y se comprobó con la evidencia más fuerte posible: **esta misma sesión ejecutó 51 planes aprobados y no reescribió ninguno**. La decisión que lo sostiene —que el plan no lleve columna de estado— está en el molde y ahora está escrita con su motivo.

**Qué falta para que cumpla:** nada. Queda sobre la mesa una decisión que sale de esta fase: si el molde del plan de pruebas debe **obligar** a una fila por criterio transversal, que es el defecto que arrastran las 51 fases.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Casos automatizados | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `ModelosDeLaFase`: 4 pruebas, en verde |
| EV-02 | Mediciones | §2 y §3: 136 avisos de `F18`, y 51 planes sin reescribir |
| EV-03 | Lo escrito | [`documentacion/documentos-modelo/spec.md`](../../../../documentos-modelo/spec.md) §4.2 |
| EV-04 | Corrida completa | `python validadores/pruebas.py` — 348 pruebas, verde, 6 fallos esperados |

---

## 8. Ciclos anteriores

Ninguno: es el primero.
