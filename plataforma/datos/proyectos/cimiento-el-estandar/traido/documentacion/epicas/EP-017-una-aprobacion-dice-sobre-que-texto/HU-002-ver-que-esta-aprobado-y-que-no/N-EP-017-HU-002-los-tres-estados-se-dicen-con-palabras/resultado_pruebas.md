# Resultado de Pruebas — Fase `N-EP-017-HU-002-los-tres-estados-se-dicen-con-palabras`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó, con qué resultado y si cada criterio quedó cumplido**. Los casos están en el [plan_pruebas.md](plan_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `N-EP-017-HU-002-los-tres-estados-se-dicen-con-palabras` |
| **HU** | [HU-002 Ver qué está aprobado y qué no](../HU-002-ver-que-esta-aprobado-y-que-no.md) |
| **Fecha de ejecución** | 2026-09-01 |
| **Ejecutó** | El agente |
| **Ciclo** | 1 |

---

## 1. Resumen de la ejecución

| | Cuántos |
|---|---|
| Casos del plan | 1, con cuatro comprobaciones |
| Ejecutados | 1 |
| Pasaron | 1 |
| Fallaron | 0 |
| Pruebas automáticas nuevas | **4** |

| | Cuánto |
|---|---|
| Estados posibles | **3** |
| Estados con su frase | **3 de 3** |
| Documentos sin aprobación que salen vacíos | **0** |
| Dependencias nuevas | **0** |

---

## 2. Ejecución caso por caso

### CP-005 — Los tres estados se dicen con palabras

| Entrada | Salió |
|---|---|
| Un documento sin aprobación | Sale, y dice que nadie lo ha aprobado todavía |
| Los tres estados | Cada uno con su frase |
| La frase de caducada | Dice que el documento cambió después de aprobarse |
| Varios documentos a la vez | Todos salen, cada uno con el suyo |

**Resultado: pasa.**

---

## 3. Por qué son tres estados y no dos

**Confundirlos pierde exactamente la información que hace falta.**

| Estado | Qué dice | Qué hacer |
|---|---|---|
| **Aprobado** | Hubo un juicio, y sigue valiendo | Nada |
| **Caducada** | **Hubo un juicio, y algo lo invalidó** | Mirar qué cambió |
| **Sin aprobación** | **Nunca hubo juicio** | Aprobarlo, o no |

Una plataforma con dos estados obligaría a meter «caducada» en alguno de los otros dos, y las dos opciones mienten: en «aprobado» diría que algo cubre un texto que ya no es ese; en «sin aprobación», borraría que alguien lo revisó.

**Y ninguno de los tres es «rechazado».** La plataforma no rechaza nada: registra lo que pasó.

---

## 4. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| Qué se miró | Resultado |
|---|---|
| Las tres frases | Las tres existen, y la de caducada dice por qué |
| La lista de varios documentos | Cada uno con su estado, ninguno vacío |

---

## 5. Veredicto por criterio de aceptación

| CA | Evidencia | Veredicto |
|---|---|---|
| CA-01 | CP-005 | **Cumple** |
| CA-02 | CP-005 | **Cumple** |
| CA-03 | CP-005 | **Cumple** |

## 5.1 Lo que el plan exigía

| Lo que el plan pedía | Qué pasó |
|---|---|
| Tres estados, no dos | Hecho |
| Cada uno con su frase | **3 de 3** |
| Lo sin aprobación aparece | Hecho |
| Sin dependencias nuevas | **Cero** |

---

## 6. Veredicto de la fase

**Concepto: Cumple.**

De cada documento se sabe si está aprobado, si su aprobación caducó o si nadie lo ha mirado, **y se dice con palabras**. Quien no distingue colores lo sabe igual.

**Lo que esta fase cuida:** que «caducada» no se confunda con «sin aprobación». Son dos cosas distintas y llevan a decisiones distintas.

**Y lo que no puede decir:** si las frases se entienden. Que existan se prueba; que sirvan lo dice quien las lea.

---

## 7. Evidencias

| ID | Qué es | Dónde |
|---|---|---|
| EV-01 | Las 4 pruebas de los estados | `plataforma/nucleo/aprobaciones/tests.py` |
| EV-02 | La orden de consola | §2 |

**Las dos baterías:** 733 pruebas del estándar y 473 de la plataforma, **cero rojas**.

---

## 8. Ciclos anteriores

No hay: es el primer ciclo de la fase.
