# Plan de Trabajo — Fase `I-EP-016-HU-003-un-sello-no-sobrevive-a-un-cambio` (módulo Reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación. El requisito vive en la HU; las pruebas, en el `plan_pruebas`; lo que quedó hecho, en el `funcionalidad_implementada.md`.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `I-EP-016-HU-003-un-sello-no-sobrevive-a-un-cambio` |
| **Épica** | [EP-016](../../epica.md) |
| **HU** | [HU-003 Aplicar el checklist y guardar su sello](../HU-003-aplicar-el-checklist-y-guardar-su-sello.md): **una sola** (`F12.1`) |
| **Módulo** | Reglas |
| **Especificación del módulo** | [documentacion/reglas/spec.md](../../../../reglas/spec.md) |
| **Fecha apertura** | 2026-09-01 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN:**

- ✨ **Funcionalidad nueva:** `F-007`, la lista de comprobación de una regla.

> **El usuario autorizó ejecutar sin aprobar paso por paso** el 2026-09-01.

**CA de la HU que cubre esta fase:** los tres, todos ☑.

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** traer las veinte filas del checklist, guardar lo que se responda, y **no dejar que el resultado sobreviva a un cambio del texto**.

**Lo que de verdad protege es la caducidad.** Un sello pegado a una regla que después se editó dice que algo se comprobó, y lo que se comprobó era otro texto: da confianza sin respaldo.

**Fuera de alcance:** responder las filas. El criterio es de una persona, y la ficha lo dice.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo medido el 2026-09-01:**

| Qué se midió | Resultado |
|---|---|
| Filas del checklist | **20** |
| Reglas vigentes con sello escrito | **248 de 248** |
| Reglas que el estándar considera con el sello vencido | **Ninguna** |
| **Reglas que lo parecerían comparando solo fechas** | **185** |

**Ese último número decidió el diseño.** El estándar compara el **cuerpo** de la regla contra el guardado y descuenta los cambios de tipografía; comparar fechas da 185 falsos.

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/reglas/sello.py` | Nuevo | Servicio | Las filas, el sello y su molde |
| `plataforma/nucleo/reglas/management/commands/sello_de_regla.py` | Nuevo | Orden | Pedirlo |
| `plataforma/nucleo/reglas/tests_sello.py` | Nuevo | Prueba | Los tres CA |
| `documentacion/reglas/spec.md` | Modificar | Especificación | Su §13, para nombrar la fase |

**Ninguna entidad y ninguna migración.**

### 2.2 Matriz de dependencias del refactor

No aplica: todo es nuevo.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **La comparación por fechas se llama `parece_vencido`** | Llamarla `esta_vencido` | Medida así, 185 de 248 reglas salían anuladas y el estándar dice que ninguna lo está |
| **El veredicto se le pregunta al estándar** | Reimplementar la comparación | Dos versiones de la misma pregunta se separan, y la vieja avisa de más |
| **Una fila que no aplica lleva su motivo** | Solo marcarla | Sin motivo no se distingue de una que se saltó |
| **Sin motivo queda un hueco marcado** | Dejarlo vacío | Un hueco se ve; un vacío no |
| **El checklist se lee, no se copia** | Copiar las filas | Copiadas, envejecen en cuanto el estándar las cambie |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | Leer las filas del checklist | Servicio | 1 h | — | CA-01 | EV-01 |
| T-02 | Leer el sello de una regla | Servicio | 1 h | — | CA-02 | EV-01 |
| T-03 | La comparación por fechas, **con su nombre** | Servicio | 1 h | T-02 | CA-02 | EV-01 |
| T-04 | Preguntarle al estándar el veredicto | Servicio | 1 h | T-03 | CA-02 | EV-01 |
| T-05 | El molde del sello, con los motivos | Servicio | 2 h | T-01 | CA-01, CA-03 | EV-01 |
| T-06 | La orden de consola | Orden | 1 h | T-04 | Todos | EV-02 |
| T-07 | Las pruebas de los tres CA | Test | 2 h | T-06 | Todos | EV-01 |
| T-08 | **Medir los sellos del cuerpo real** | Medición | 1 h | T-06 | CA-02 | EV-02 |

**Total estimado:** 10 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-05 → T-06 → T-08. T-02 a T-04 van en paralelo.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Armando el sello con respuestas de prueba | EV-01 | 2026-09-01 | ☑ |
| CA-02 | Con `M11`, sellada el 2026-08-07 y tocada el 2026-08-19 | EV-01, EV-02 | 2026-09-01 | ☑ |
| CA-03 | Armando el sello con y sin motivo | EV-01 | 2026-09-01 | ☑ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas del sello | `plataforma/nucleo/reglas/tests_sello.py` |
| EV-02 | La medición sobre el cuerpo real | `resultado_pruebas.md` §3 |

---

## 6. Datos y ambiente de prueba

Un checklist de mentiras y reglas de mentiras, y el cuerpo real solo para medir. **Ninguna regla real se toca.**

---

## 7. Reversión / rollback  ·  Q11

Nada que revertir: esta fase no escribe en ninguna regla. Arma el bloque del sello y lo devuelve.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Ninguna migración, ninguna dependencia nueva.

---

## 9. Reglas aplicadas  ·  Q13

- Base: [`20·M14`](../../../../../base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md), que es la que manda acá.
- Producto: las `RN-1` a `RN-5` de la historia.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | **Que la comparación por fechas se tome por veredicto** | **Alto: 185 avisos falsos** | Se llama `parece_vencido`, y hay una prueba que comprueba que no exista `esta_vencido` | Cerrado |
| B-02 | Que alguien crea que la plataforma responde las filas | Medio | La orden lo dice al final | Cerrado |
| B-03 | Que la cabecera de la tabla se cuente como fila | Bajo | Se descarta por su texto | Cerrado |

---

## 11. Definition of Done

- [x] Los tres CA verificados con evidencia
- [x] Medidos los sellos del cuerpo real
- [x] Las dos baterías en verde
- [x] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
