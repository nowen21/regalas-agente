# Resultado de Pruebas — Fase `E-EP-015-HU-002-el-estado-sale-de-la-fase-que-corrio`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó, con qué resultado y si cada criterio quedó cumplido**. Los casos están en el [plan_pruebas.md](plan_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `E-EP-015-HU-002-el-estado-sale-de-la-fase-que-corrio` |
| **HU** | [HU-002 Fijar el estado desde la evidencia](../HU-002-fijar-el-estado-desde-la-evidencia.md) |
| **Fecha de ejecución** | 2026-09-01 |
| **Ejecutó** | El agente, sobre este repositorio |
| **Ciclo** | 1 |

---

## 1. Resumen de la ejecución

| | Cuántos |
|---|---|
| Casos del plan | 5 |
| Ejecutados | 5 |
| Pasaron | 5 |
| Fallaron | 0 |
| Pruebas automáticas nuevas | **11** |

**Las 35 funcionalidades de este repositorio, con su estado derivado:**

| Estado | Cuántas |
|---|---|
| **Verificadas** | **14** |
| No cumplen | 0 |
| Sin verificar | 21 |

**Las 14 verificadas son exactamente las construidas:** siete de la versión 1, cinco de la versión 2 y dos de la versión 3. Ni una más ni una menos.

| Antes de esta fase | Después |
|---|---|
| 35 dicen «Sin verificar», escrito a mano | 14 verificadas, derivadas de la fase que corrió |

---

## 2. Ejecución caso por caso

### CP-001 — Con prueba y evidencia queda verificado

Una fase que declara «Cumple» deja la funcionalidad verificada y cerrable, y **el estado dice de qué fase sale**.

**Resultado: pasa.**

### CP-002 — Sin prueba queda sin verificar, y no se cierra

**El caso que decide la fase.**

| Entrada | Salió |
|---|---|
| Ninguna fase la construye | Sin verificar, no se cierra |
| Fase declarada que no existe | Sin verificar |
| Fase que existe y no declara veredicto | Sin verificar |

**Resultado: pasa.**

### CP-003 — Con prueba fallida queda «no cumple»

Sale «no cumple», con el nombre de la fase, y no se cierra. Es un valor distinto de «sin verificar».

**Resultado: pasa.**

### CP-004 — Las dos formas de veredicto se leen las dos

**Este caso nació de un defecto encontrado construyendo.**

La primera versión leía solo la forma de ahora, y **siete funcionalidades cerradas y en verde salían «sin verificar»**: las de la versión 1, cuyas fases escriben el veredicto de otra manera. Ahora se leen las dos.

**Resultado: pasa.**

### CP-005 — La cuenta sobre este repositorio

35 funcionalidades, 14 verificadas, 21 sin verificar, ninguna en «no cumple».

**Resultado: pasa.**

---

## 3. Los dos defectos que aparecieron construyendo

Los dos venían de lo mismo: **la convención cambió con el tiempo, y lo escrito antes sigue escrito como antes.**

### D-01 — Siete filas nombraban la fase por su letra sola

Las especificaciones de la versión 1 dicen `| F-002 | RF-02 | C |`. Una letra sola no se puede seguir: **cada épica tiene su «A»**. Se completaron las siete con el nombre entero, y el cambio quedó registrado en la §15 de cada especificación, que existe para eso.

### D-02 — El veredicto se escribía de otra manera

Las fases de la versión 1 lo escriben como «Veredicto de las pruebas»; las de ahora, en una tabla con «Concepto». Con solo la forma nueva, **siete funcionalidades cerradas salían sin verificar**.

**No se reescribió ninguna fase cerrada.** Una fase dice lo que era cierto el día que cerró; el que se adapta es el que lee.

---

## 4. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| Qué se miró | Resultado |
|---|---|
| Las 14 verificadas | Son exactamente las construidas |
| Las 21 sin verificar | Ninguna está construida |
| Que derivar no modifique nada | Ningún documento cambió |

---

## 5. Veredicto por criterio de aceptación

| CA | Evidencia | Veredicto |
|---|---|---|
| CA-01 | CP-001, §1 | **Cumple** |
| CA-02 | CP-002 | **Cumple** |
| CA-03 | CP-003 | **Cumple** |
| CA-04 | CP-004, §3 | **Cumple** |

## 5.1 Lo que el plan exigía

| Lo que el plan pedía | Qué pasó |
|---|---|
| El estado derivado, no escrito | Hecho |
| Las dos formas de veredicto | Hecho, y era un defecto real |
| Las siete filas completadas | Hechas, con su registro en la §15 |
| La cuenta escrita | **14 de 35** |
| Sin dependencias nuevas | **Cero** |

---

## 6. Veredicto de la fase

**Concepto: Cumple.**

El estado de una funcionalidad ya sale de la fase que la construyó. Antes las 35 decían lo mismo porque nadie lo había comprobado; ahora **14 dicen que están verificadas porque una fase lo declaró**, y las otras 21 dicen que nadie las comprobó, que es distinto de decir que están mal.

**Lo que la fase encontró:** dos defectos de la misma clase, los dos por la convención que cambió con el tiempo. Ninguna fase cerrada se reescribió: el que se adapta es el que lee.

**Y lo que esta fase no puede decir:** si el veredicto de una fase era correcto. Eso lo respondió esa fase en su día.

---

## 7. Evidencias

| ID | Qué es | Dónde |
|---|---|---|
| EV-01 | Las 11 pruebas del estado | `plataforma/nucleo/comprobaciones/tests_estado.py` |
| EV-02 | La cuenta sobre este repositorio | §1 |

**Las dos baterías:** 733 pruebas del estándar y 353 de la plataforma, **cero rojas**.

---

## 8. Ciclos anteriores

No hay: es el primer ciclo de la fase.
