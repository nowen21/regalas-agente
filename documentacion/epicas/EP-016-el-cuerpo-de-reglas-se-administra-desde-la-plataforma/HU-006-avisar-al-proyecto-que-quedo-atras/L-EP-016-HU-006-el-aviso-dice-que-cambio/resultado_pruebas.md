# Resultado de Pruebas — Fase `L-EP-016-HU-006-el-aviso-dice-que-cambio`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó, con qué resultado y si cada criterio quedó cumplido**. Los casos están en el [plan_pruebas.md](plan_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `L-EP-016-HU-006-el-aviso-dice-que-cambio` |
| **HU** | [HU-006 Avisar al proyecto que quedó atrás](../HU-006-avisar-al-proyecto-que-quedo-atras.md) |
| **Fecha de ejecución** | 2026-09-01 |
| **Ejecutó** | El agente, sobre el registro real de este repositorio |
| **Ciclo** | 1 |

---

## 1. Resumen de la ejecución

| | Cuántos |
|---|---|
| Casos del plan | 3 |
| Ejecutados | 3 |
| Pasaron | 3 |
| Fallaron | 0 |
| Pruebas automáticas nuevas | **5** |

**El lector del registro, antes y después:**

| | Antes | Después |
|---|---|---|
| Entradas que reconoce | **143 de 197** | **162 de 197** |
| La más reciente que entiende | **34.2.0** | **la del día** |
| Entradas del registro reescritas | — | **0** |

**El aviso, sobre un proyecto en la 35.0.0:**

```
el proyecto declara v35.0.0, el estándar va en v37.2.1: subir es decisión
del usuario; las fases cerradas quedan selladas. Qué cambió: **2 obligan a
migrar** (v37.0.0, v36.0.0), van 18. Lo último: ...
```

Antes de esta fase, todo lo que venía después de los dos puntos **salía vacío**.

---

## 2. Ejecución caso por caso

### CP-004 — El desfase dice qué cambió

| Entrada | Salió |
|---|---|
| La versión vigente | Al día, sin lista |
| Una versión anterior | El motivo **y** qué cambió |
| Un tramo con una MAYOR | Sale cuál obliga a migrar |

**Lo primero que se dice es cuáles obligan a migrar**, porque es lo único del aviso que cambia qué hacer.

**Resultado: pasa.**

### CP-005 — Un número inventado no está al día

**El caso que decide la fase.**

Una versión que no aparece en el registro se responde diciendo que **ese número no existió nunca**, y no se concluye que va adelantado. **No declarar nada** se responde distinto: no es declarar algo falso.

**Resultado: pasa.**

### El conteo del lector

De **143 a 162** entradas reconocidas, y la más reciente pasó de la 34.2.0 a la del día. **El orden viejo se sigue entendiendo**, que era el criterio de suspensión de esta fase.

**Resultado: pasa.**

---

## 3. El aviso que llevaba 54 versiones saliendo vacío

**Es el hallazgo de la fase, y explica por qué `F-010` parecía construida y no lo estaba.**

El aviso de desfase existía y se daba al conectar un proyecto. Lo que no salía era la parte que sirve para decidir: **qué cambió**. Y no salía porque el lector del registro no entendía las entradas nuevas.

**Qué pasó, en una línea:** el registro se escribía con el tipo delante; cuando `M17` pidió que la entrada abriera contando qué pasó, el orden se invirtió, y el lector solo entendía el viejo.

**Es la tercera vez en el día que aparece el mismo patrón:** una convención cambió y el lector se quedó atrás. Las otras dos fueron el veredicto de una fase y la marca de un espacio por llenar.

**Y la respuesta fue la misma las tres veces:** el que se adapta es el que lee. **No se reescribió ninguna entrada del registro.**

El arreglo se versionó como **PARCHE 37.2.1**, porque `20·M10` lo exige y porque no cambia qué se le pide a nadie: arregla un aviso que salía vacío.

---

## 4. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| Qué se miró | Resultado |
|---|---|
| El registro real, con sus 197 entradas | Ninguna reescrita |
| El aviso sobre una versión vieja | Trae el resumen y los que obligan a migrar |
| Las dos baterías después de tocar el estándar | 733 y 426, en verde |

---

## 5. Veredicto por criterio de aceptación

| CA | Evidencia | Veredicto |
|---|---|---|
| CA-01 | CP-004, §1 | **Cumple** |
| CA-02 | CP-004 | **Cumple** |
| CA-03 | CP-005 | **Cumple** |

## 5.1 Lo que el plan exigía

| Lo que el plan pedía | Qué pasó |
|---|---|
| Medir cuántas entradas reconoce el lector | Hecho: **143 antes, 162 después** |
| Que acepte los dos órdenes | Hecho, y el viejo se sigue entendiendo |
| Versionar y registrar la corrección | Hecho: **PARCHE 37.2.1** |
| Un número inventado se dice | Hecho |
| Sin dependencias nuevas | **Cero** |

---

## 6. Veredicto de la fase

**Concepto: Cumple.**

El aviso de desfase dice qué cambió, cuáles obligan a migrar y cuántas van. Y las tres respuestas al día, quedó atrás, y ese número no existió se dan distinto, porque son cosas distintas.

**Lo que esta fase destapó:** un aviso que llevaba **54 versiones saliendo vacío**, y nadie lo había notado porque salir vacío se ve igual que no tener nada que decir.

**Y lo que confirma:** el que se adapta es el que lee. Ninguna de las 197 entradas del registro se reescribió.

---

## 7. Evidencias

| ID | Qué es | Dónde |
|---|---|---|
| EV-01 | Las 5 pruebas del desfase | `plataforma/nucleo/reglas/tests_entrega.py` |
| EV-02 | El conteo sobre el registro real | §1 y §3 |

**Las dos baterías:** 733 pruebas del estándar y 426 de la plataforma, **cero rojas**.

---

## 8. Ciclos anteriores

No hay: es el primer ciclo de la fase.
