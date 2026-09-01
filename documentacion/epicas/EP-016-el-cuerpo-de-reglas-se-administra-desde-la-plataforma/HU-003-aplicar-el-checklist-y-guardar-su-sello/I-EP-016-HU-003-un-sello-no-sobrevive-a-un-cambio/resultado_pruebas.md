# Resultado de Pruebas — Fase `I-EP-016-HU-003-un-sello-no-sobrevive-a-un-cambio`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó, con qué resultado y si cada criterio quedó cumplido**. Los casos están en el [plan_pruebas.md](plan_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `I-EP-016-HU-003-un-sello-no-sobrevive-a-un-cambio` |
| **HU** | [HU-003 Aplicar el checklist y guardar su sello](../HU-003-aplicar-el-checklist-y-guardar-su-sello.md) |
| **Fecha de ejecución** | 2026-09-01 |
| **Ejecutó** | El agente, sobre un cuerpo de prueba y sobre el cuerpo real |
| **Ciclo** | 1 |

---

## 1. Resumen de la ejecución

| | Cuántos |
|---|---|
| Casos del plan | 4 |
| Ejecutados | 4 |
| Pasaron | 4 |
| Fallaron | 0 |
| Pruebas automáticas nuevas | **16** |

**Los sellos del cuerpo real, medidos de las dos formas:**

| Cómo se mide | Reglas con el sello anulado |
|---|---|
| **Lo que dice el estándar** | **Ninguna** |
| Comparando solo fechas | **185 de 248** |

| | Cuánto |
|---|---|
| Filas del checklist | **20** |
| Reglas vigentes con sello escrito | **248 de 248** |
| Reglas reales tocadas | **0** |
| Dependencias nuevas | **0** |

---

## 2. Ejecución caso por caso

### CP-001 — Se leen las filas del checklist

Las 20 filas se leen con su número, su respaldo y su criterio. **La cabecera de la tabla no cuenta como fila.** Sin checklist se dice, en vez de armar un sello contra nada.

**Resultado: pasa.**

### CP-002 — Se lee el sello de una regla

Con sello se dice contra qué versión y en qué fecha; sin sello se dice, y no hay ni versión ni fecha.

**Resultado: pasa.**

### CP-003 — Las fechas no son el veredicto

**El caso que decide la fase.**

| Entrada | Salió |
|---|---|
| Sellada antes de tocar el archivo | No lo parece |
| Tocada después de sellar | Lo parece, y nada más |
| Sin sello | Lo parece siempre |
| Sin fecha de cambio | Lo parece: no se puede afirmar |

**Y la prueba de nombre:** existe `veredicto_del_estandar`, y **no existe** ninguna función que se llame como si las fechas decidieran.

**Resultado: pasa.**

### CP-004 — El molde del sello

Todo en sí da **CUMPLE** con su cuenta; un no da **NO CUMPLE**; una fila que no aplica lleva su motivo, y sin motivo queda **un hueco marcado**. Siempre trae su aviso de caducidad.

**Resultado: pasa.**

---

## 3. Los 185 avisos falsos que casi salen

**La medición del plan salvó la fase.**

Comparando la fecha del sello con la del último cambio del archivo, **185 de las 248 reglas vigentes salían con el sello anulado**. El estándar dice que **ninguna** lo está, y tiene razón: compara el **cuerpo** de la regla contra el guardado y **descuenta los cambios de tipografía**.

Y es una diferencia con historia: limpiar unas semirayas en setenta y cuatro reglas habría vencido sus sellos de golpe, y entonces nadie limpia nunca.

**Qué se hizo con eso:**

| Antes | Después |
|---|---|
| Una función llamada `esta_vencido` | Se llama `parece_vencido`, y su nombre dice que no decide |
| Una comparación propia | Se le pregunta al estándar, que ya sabe hacerla bien |

**Es la tercera vez en el día que aparece el mismo riesgo:** un aviso falso enseña a ignorar el aviso. Esta vez se vio antes de que saliera.

---

## 4. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| Qué se miró | Resultado |
|---|---|
| `M11`, sellada el 2026-08-07 y tocada el 2026-08-19 | La orden dice que **parece** anulado, y que decide el estándar |
| Lo que dice el estándar de los sellos | Ninguno vencido |
| El cuerpo de reglas real | **Ninguna regla tocada** |

---

## 5. Veredicto por criterio de aceptación

| CA | Evidencia | Veredicto |
|---|---|---|
| CA-01 | CP-004 | **Cumple** |
| CA-02 | CP-003, §3 | **Cumple** |
| CA-03 | CP-004 | **Cumple** |

## 5.1 Lo que el plan exigía

| Lo que el plan pedía | Qué pasó |
|---|---|
| Las filas leídas del estándar | Hecho: 20 |
| La comparación por fechas con su nombre | Hecha, **y con una prueba de nombre** |
| El veredicto se le pregunta al estándar | Hecho |
| Los sellos del cuerpo real, medidos | Hechos: **0 contra 185** |
| Sin dependencias nuevas | **Cero** |

---

## 6. Veredicto de la fase

**Concepto: Cumple.**

El checklist se trae del estándar, el sello queda con su versión y su fecha, y una fila que no aplica lleva su motivo. Y sobre todo: **la comparación barata se llama como lo que es**, y el veredicto se le pregunta a quien sabe darlo.

**Lo que esta fase evitó:** 185 avisos falsos en 248 reglas. Un aviso así no molesta: enseña a ignorar el aviso, y el día que uno sea de verdad nadie lo mira.

**Y lo que esta fase no puede decir:** si las respuestas del checklist son correctas. Buena parte de las filas pide criterio.

---

## 7. Evidencias

| ID | Qué es | Dónde |
|---|---|---|
| EV-01 | Las 16 pruebas del sello | `plataforma/nucleo/reglas/tests_sello.py` |
| EV-02 | La medición sobre el cuerpo real | §1 y §3 |

**Las dos baterías:** 733 pruebas del estándar y 426 de la plataforma, **cero rojas**.

---

## 8. Ciclos anteriores

No hay: es el primer ciclo de la fase.
