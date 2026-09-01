# Resultado de Pruebas — Fase `K-EP-016-HU-005-las-reglas-llegan-y-la-fuente-sigue-ahi`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó, con qué resultado y si cada criterio quedó cumplido**. Los casos están en el [plan_pruebas.md](plan_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `K-EP-016-HU-005-las-reglas-llegan-y-la-fuente-sigue-ahi` |
| **HU** | [HU-005 Entregarle las reglas al agente](../HU-005-entregarle-las-reglas-al-agente.md) |
| **Fecha de ejecución** | 2026-09-01 |
| **Ejecutó** | El agente, sobre este repositorio |
| **Ciclo** | 1 |

---

## 1. Resumen de la ejecución

| | Cuántos |
|---|---|
| Casos del plan | 3 |
| Ejecutados | 3 |
| Pasaron | 3 |
| Fallaron | 0 |
| Pruebas automáticas nuevas | **9** |

**La entrega sobre este repositorio:**

```
Reglas vigentes: 248, en 124 capítulo(s), bajo la versión 37.2.1.
Entregadas en 0.17 s.
Caracteres: 679511
```

| | Cuánto |
|---|---|
| Reglas vigentes | **248** |
| Archivos entregados | **124** |
| Caracteres | **679 511** |
| **Cuánto tardó** | **0,17 s** |
| **El límite de la ficha** | 2 s |
| Fallos que devolvieron vacío | **0** |
| Dependencias nuevas | **0** |

---

## 2. Ejecución caso por caso

### CP-001 — Se entregan las reglas

Salen los 124 capítulos con su texto y su ruta relativa, y se dice cuántas rigen y bajo qué versión.

**Se entrega el texto, no un resumen:** hay una prueba que busca una frase de una regla real en lo entregado y la encuentra. Un resumen de una regla es otra regla, y la que el agente obedecería sería la del resumen.

**Resultado: pasa.**

### CP-002 — Entregarlas es rápido

**0,17 segundos** contra un límite de dos. Sobra un orden de magnitud, y el número queda escrito para el día que el cuerpo de reglas crezca.

**Resultado: pasa.**

### CP-003 — Si no se puede, la fuente sigue ahí

**El caso que decide la fase.**

| Entrada | Salió |
|---|---|
| Un proyecto sin cuerpo de reglas | Se dice por qué |
| El mismo | **Se dice dónde está la fuente** |
| Un proyecto que sí se pudo | La fuente también se nombra |

**Devolver una lista vacía se leería como «este proyecto no tiene reglas»**, y el agente trabajaría sin ninguna sin que nadie lo notara.

**Resultado: pasa.**

---

## 3. Por qué la fuente se nombra también cuando todo sale bien

Podría parecer ruido. No lo es: **es lo que recuerda que esta pieza no es un intermediario obligatorio.**

El cuerpo de reglas son archivos en el proyecto. Quien no pueda usar la plataforma los abre y trabaja igual. Nombrar la fuente siempre mantiene eso a la vista, en vez de dejar que la plataforma se vuelva, de a poco, la única forma de llegar a las reglas.

---

## 4. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| Qué se miró | Resultado |
|---|---|
| Lo entregado sobre este repositorio | 124 archivos, con su texto entero |
| El tiempo | 0,17 s, medido, no supuesto |
| Que leer no modificara nada | Nada cambió |

---

## 5. Veredicto por criterio de aceptación

| CA | Evidencia | Veredicto |
|---|---|---|
| CA-01 | CP-001, §1 | **Cumple** |
| CA-02 | CP-002, §1 | **Cumple** |
| CA-03 | CP-003 | **Cumple** |

## 5.1 Lo que el plan exigía

| Lo que el plan pedía | Qué pasó |
|---|---|
| Se entrega el texto | Hecho, con una prueba que lo comprueba |
| El tiempo medido | **0,17 s** contra un límite de 2 |
| La fuente se nombra siempre | Hecho |
| Sin dependencias nuevas | **Cero** |

---

## 6. Veredicto de la fase

**Concepto: Cumple.**

Las reglas vigentes de un proyecto se entregan enteras en 0,17 segundos, con su cuenta y su versión. Y si algo falla, se dice por qué y dónde está la fuente.

**Lo que esta fase cuida sin que se note:** que la plataforma no se vuelva la única forma de llegar a las reglas. Por eso la fuente se nombra también cuando todo sale bien.

**Y lo que no se puede decir todavía:** cómo se comporta con un cuerpo de reglas diez veces más grande. Se midió con 248 vigentes y 679 511 caracteres.

---

## 7. Evidencias

| ID | Qué es | Dónde |
|---|---|---|
| EV-01 | Las 9 pruebas de la entrega | `plataforma/nucleo/reglas/tests_entrega.py` |
| EV-02 | La medición sobre este repositorio | §1 |

**Las dos baterías:** 733 pruebas del estándar y 426 de la plataforma, **cero rojas**.

---

## 8. Ciclos anteriores

No hay: es el primer ciclo de la fase.
