# Resultado de Pruebas — Fase `G-EP-016-HU-001-ningun-numero-se-reutiliza`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó, con qué resultado y si cada criterio quedó cumplido**. Los casos están en el [plan_pruebas.md](plan_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `G-EP-016-HU-001-ningun-numero-se-reutiliza` |
| **HU** | [HU-001 Dar el identificador sin reutilizar ninguno](../HU-001-dar-el-identificador-sin-reutilizar-ninguno.md) |
| **Fecha de ejecución** | 2026-09-01 |
| **Ejecutó** | El agente, sobre este repositorio |
| **Ciclo** | 1 |

---

## 1. Resumen de la ejecución

| | Cuántos |
|---|---|
| Casos del plan | 4 |
| Ejecutados | 4 |
| Pasaron | 4 |
| Fallaron | 0 |
| Pruebas automáticas nuevas | **15** |

**El cuerpo de reglas de este repositorio, leído desde la plataforma:**

| | Cuánto |
|---|---|
| Reglas en total | **257** |
| Vigentes | 248 |
| Derogadas | **9** |
| Blindadas | 9 |
| Capítulos con prefijo propio | **24** |
| Huecos de numeración | **Ninguno** |
| Identificadores entregados que ya existieran | **0** |

**El siguiente identificador de cada capítulo revisado:**

```
ID   siguiente: ID11    huecos: []
F    siguiente: F27     huecos: []
DOC  siguiente: DOC24   huecos: []
M    siguiente: M21     huecos: []
N    siguiente: N10     huecos: []
```

**Y la comprobación que decide:** `ID2` está derogada, y aparece como **usado**. Su número no se entrega.

---

## 2. Ejecución caso por caso

### CP-001 — Se lee el cuerpo de reglas

Se leen las vigentes y las derogadas. La derogada **no está entre las vigentes** y **sí entre todas**: su identificador sigue ocupado, y por eso tiene que salir.

**Sin el lector del estándar se revienta**, en vez de devolver una lista vacía. Una lista vacía se leería como «no hay reglas», y ahí el siguiente identificador sería el uno: el peor error posible en esta fase.

**Resultado: pasa.**

### CP-002 — El siguiente identificador

| Entrada | Salió |
|---|---|
| Un capítulo con reglas hasta la N | La N más uno |
| Un capítulo sin reglas | El uno |
| Los usados con una derogada | La derogada adentro |

**Resultado: pasa.**

### CP-003 — No se guarda con un identificador usado

Uno vigente se rechaza; uno derogado se rechaza; uno libre pasa. **La comprobación va antes de guardar**: después ya habría dos reglas con el mismo número, y la que se lea primero gana.

**Resultado: pasa.**

### CP-004 — El de una derogada no se reasigna

**El caso que decide la fase.**

Con un capítulo que tiene `M1`, `M2` derogada y `M5`, el siguiente es **`M6`**, y los huecos `[3, 4]` se pueden mirar **pero no se entregan**.

**Resultado: pasa.**

---

## 3. Lo que la medición mostró del cuerpo de reglas

Correrlo sobre este repositorio dejó dos datos que no se sabían:

| Dato | Cuánto |
|---|---|
| Capítulos con prefijo propio | **24**, más de los que se hubieran contado a ojo |
| **Huecos de numeración** | **Ninguno** en los capítulos revisados |

Que no haya huecos quiere decir que en tres años nadie se saltó un número ni reutilizó uno. **Es la disciplina que esta fase viene a sostener cuando deje de hacerse a mano.**

---

## 4. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| Qué se miró | Resultado |
|---|---|
| `ID2`, que está derogada | Sale como usado |
| Los cinco capítulos revisados | Ningún siguiente pisa un identificador existente |
| Que leer no modifique nada | Nada cambió |

---

## 5. Veredicto por criterio de aceptación

| CA | Evidencia | Veredicto |
|---|---|---|
| CA-01 | CP-002, §1 | **Cumple** |
| CA-02 | CP-004, §1 | **Cumple** |
| CA-03 | CP-003 | **Cumple** |

## 5.1 Lo que el plan exigía

| Lo que el plan pedía | Qué pasó |
|---|---|
| El siguiente es el que sigue al mayor | Hecho |
| Las derogadas cuentan | Hecho, y comprobado con `ID2` |
| Sin lector se revienta | Hecho |
| Corrido sobre este repositorio | **257 reglas, 24 capítulos, cero huecos** |
| Sin dependencias nuevas | **Cero** |

---

## 6. Veredicto de la fase

**Concepto: Cumple.**

Cada regla nueva recibe un identificador que nadie tuvo antes, contando también las derogadas. Lo único irreversible de esta épica queda impedido por construcción.

**Lo que la medición dejó:** el cuerpo tiene 257 reglas en 24 capítulos y **ningún hueco de numeración**. Lo que se hacía a mano se hacía bien; ahora hay quien lo sostenga.

**Y lo que esta fase no puede decir:** si el formato de una regla cambia. Eso lo sabe el lector del estándar, con sus propias pruebas.

---

## 7. Evidencias

| ID | Qué es | Dónde |
|---|---|---|
| EV-01 | Las 15 pruebas del módulo | `plataforma/nucleo/reglas/tests.py` |
| EV-02 | La corrida sobre este repositorio | §1 y §3 |

**Las dos baterías:** 733 pruebas del estándar y 382 de la plataforma, **cero rojas**.

---

## 8. Ciclos anteriores

No hay: es el primer ciclo de la fase.
