# Resultado de Pruebas — Fase B-EP-001-HU-007-primero-que-el-proceso-sirva   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-001-HU-007-primero-que-el-proceso-sirva` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-17 |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente |
| **CA que cubre** | CA-05 de HU-007 |

---

## 1. Lo que se comprobó

La regla existe y tiene su identificador: [`20·M19`](../../../../../base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md).

> Antes de construir el programa que comprueba una regla, se deja escrito si hoy se cumple a mano, cuántas veces se incumplió y por qué, y cuántas falsas alarmas daría.

**Y esta jornada la puso a prueba tres veces, sin proponérselo. Las tres veces habría ahorrado trabajo.**

### Caso 1 · La comprobación del encuadre, primer criterio

Se escribió un programa que exigía que el encuadre de un planteamiento citara una regla. Se corrió sobre 651 documentos y **reprobó uno que estaba bien**: `planteamiento.md` deletrea la cadena en palabras en vez de citar identificadores.

`M19` pide contar las falsas alarmas **antes** de construir. Aquí se contaron después, y hubo que rehacer el criterio.

### Caso 2 · La misma comprobación, defecto del bloque

La primera versión tomaba la tabla de ficha como texto fijo, y **reprobaba 110 planes de pruebas**. Misma lección: la cuenta de falsas alarmas llegó después de escribir.

### Caso 3 · La resolución del nombre del planteamiento

Un arreglo que aceptaba cualquier sufijo **resolvía mal 29 documentos**, tomando cada resultado de pruebas por un plan de pruebas. Este sí se midió antes de dejarlo, y por eso no llegó a quedarse.

**El tercero es el que muestra que la regla sirve:** la única de las tres que no costó rehacer trabajo es la que se midió antes.

---

## 2. Lo que la regla exige, contra lo que pasó

| Lo que `M19` pide antes de construir | Caso 1 | Caso 2 | Caso 3 |
|---|---|---|---|
| ¿Se cumple hoy a mano? | no se preguntó | no se preguntó | sí |
| ¿Cuántas veces se incumplió y por qué? | no se contó | no se contó | sí |
| ¿Cuántas falsas alarmas daría? | **se supo después: 1** | **se supo después: 110** | **antes: 29** |
| ¿Hubo que rehacer? | sí | sí | **no** |

---

## 3. Defectos encontrados

| ID | Severidad | Qué pasó | Estado |
|---|---|---|---|
| D-01 | Media | `M19` existe y **nada la hace cumplir**. Se incumplió dos veces en un solo día, en el mismo repositorio que la escribió, sin que nada avisara | **Abierto** |
| D-02 | Baja | La regla pide un dato —cuántas falsas alarmas daría— que solo se puede saber corriendo el programa que todavía no existe. En la práctica se cumple corriendo un borrador contra el repositorio antes de dejarlo, y eso no está dicho en ninguna parte | **Abierto** |

---

## 4. Veredicto por criterio de aceptación

| CA | Cómo se comprobó | Concepto |
|---|---|---|
| CA-05, no se automatiza hasta saber que sirve | La regla existe, y tres casos reales del mismo día: los dos que la incumplieron costaron rehacer, el que la cumplió no | Cumple |

---

## 5. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** el criterio quedó probado contra casos reales y no contra un ejemplo escrito para la ocasión, que es lo que el plan pedía. Y quedó probado en las dos direcciones: qué pasa cuando se sigue y qué pasa cuando no.

**Lo que la fase deja dicho** es el D-02, que es la parte incómoda: `M19` pide un número que solo se obtiene corriendo un borrador contra el repositorio. Eso es lo que hay que escribir en alguna parte, porque es lo que de verdad hace que la regla se pueda cumplir.

---

## 6. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | La regla | [`20·M19`](../../../../../base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md) |
| EV-02 | Los tres casos | Fases `B-EP-004-HU-004` y `C-EP-003-HU-002` del 2026-08-22, con sus defectos D-01 y D-02 |
| EV-03 | El costo de no cumplirla | Dos criterios rehechos y una corrección adicional, en una sola jornada |

---

## 7. Ciclos anteriores

Ninguno.
