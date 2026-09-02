# Resultado de Pruebas — Fase `H-EP-016-HU-002-derogar-marca-y-no-borra`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó, con qué resultado y si cada criterio quedó cumplido**. Los casos están en el [plan_pruebas.md](plan_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `H-EP-016-HU-002-derogar-marca-y-no-borra` |
| **HU** | [HU-002 Escribir, corregir y derogar una regla](../HU-002-escribir-corregir-y-derogar-una-regla.md) |
| **Fecha de ejecución** | 2026-09-01 |
| **Ejecutó** | El agente, sobre un cuerpo de prueba y sobre el cuerpo real |
| **Ciclo** | 1 |

---

## 1. Resumen de la ejecución

| | Cuántos |
|---|---|
| Casos del plan | 3 |
| Ejecutados | 3 |
| Pasaron | 3 |
| Fallaron | 0 |
| Pruebas automáticas nuevas | **14** |

**Las reglas parecidas, contra las 248 vigentes de este repositorio:**

| Título con el que se preguntó | Qué encontró |
|---|---|
| «Las reglas no se borran: se derogan» | **`M11`**, que es exactamente esa regla |
| «Marca los espacios por llenar de un documento» | **`DOC19`**, con «espacios», «llenar» y «marca» en común |
| «Cocina una arepa de choclo» | Nada |

| | Cuánto |
|---|---|
| Reglas vigentes contra las que compara | **248** |
| Líneas perdidas al derogar | **0** |
| Reglas blindadas derogadas | **0** |
| Reglas reales tocadas al probar | **0** |
| Dependencias nuevas | **0** |

---

## 2. Ejecución caso por caso

### CP-005 — Se escribe una regla nueva

Queda guardada con el identificador que le tocaba, y el archivo trae el encabezado, el cuerpo y el ejemplo INCORRECTO/CORRECTO. **Nace con sus huecos puestos**, así que se ve que está incompleta. El nombre del archivo sale del título, sin tildes.

**Resultado: pasa.**

### CP-006 — Derogar no borra

**El caso que decide la fase.**

| Entrada | Salió |
|---|---|
| Una regla vigente | Marcada, **y su texto original entero** |
| La misma, después | Ya no está entre las vigentes |
| Su identificador | **Sigue ocupado** |
| Una que no existe | Se dice |
| Una ya derogada | Se dice |
| Una blindada | Se dice, y no se toca |

**Resultado: pasa.**

### CP-007 — Las reglas que hablan de lo mismo

Sobre las 248 vigentes, con el título de una regla que ya existe, **encuentra esa misma regla**. Con un título sin nada que ver, no devuelve nada. **No mira las derogadas:** una derogada ya no rige, no puede contradecir a nadie.

Y el aviso dice lo que esto no puede decir **encuentre o no encuentre**.

**Resultado: pasa.**

---

## 3. La prueba que valió más que las otras

Se le preguntó por un título casi idéntico al de una regla real:

```
Identificador que le tocaría: DOC24

Estas 1 hablan de lo mismo. Míralas antes de guardar: esto no dice si se
contradicen, solo que se parecen.
  DOC19    Marca con «…» los espacios por llenar de un documento modelo
           en común: documento, espacios, llenar, marca
```

**Habría evitado escribir una regla duplicada.** Es exactamente el caso que la ficha de `F-005` describe: *«escribir la regla es lo fácil; lo que cuesta es que no repita ni contradiga a otra»*.

**Y el aviso hace la mitad del trabajo.** Dice *«no dice si se contradicen»* cada vez, incluso cuando no encuentra nada. Sin esa frase, la funcionalidad sería peor que no existir: **quien confía en un detector deja de mirar**, y las contradicciones que se le escapen pasarían sin que nadie las revise.

---

## 4. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| Qué se miró | Resultado |
|---|---|
| El archivo de una regla derogada en la prueba | Marcado arriba, texto entero debajo |
| El cuerpo de reglas real | **Ninguna regla tocada** |
| El aviso sin resultados | También dice que no detecta contradicciones |

---

## 5. Veredicto por criterio de aceptación

| CA | Evidencia | Veredicto |
|---|---|---|
| CA-01 | CP-005 | **Cumple** |
| CA-02 | CP-006 | **Cumple** |
| CA-03 | CP-007, §3 | **Cumple** |

## 5.1 Lo que el plan exigía

| Lo que el plan pedía | Qué pasó |
|---|---|
| El molde canónico, con sus huecos | Hecho |
| Derogar marca y conserva | Hecho: **cero líneas perdidas** |
| Una blindada no se deroga | Hecho |
| Las parecidas, sobre el cuerpo real | Hecho, y encontró el duplicado |
| El aviso dice lo que no puede decir | Hecho, encuentre o no |
| Sin dependencias nuevas | **Cero** |

---

## 6. Veredicto de la fase

**Concepto: Cumple.**

Una regla se escribe y se deroga desde la plataforma. **Derogar marca y conserva**, y el identificador queda ocupado para siempre. Antes de escribir se ven las que hablan de lo mismo, y sobre el cuerpo real esa lista encontró el duplicado que habría pasado.

**Lo que más cuidado costó no fue el código, sino la frase.** El aviso tiene que decir, cada vez, que esto no detecta contradicciones. Sin ella la funcionalidad sería peor que no existir.

**Y lo que esta fase no puede decir:** si la regla escrita es buena. El criterio es de una persona, y la ficha ya lo advertía.

---

## 7. Evidencias

| ID | Qué es | Dónde |
|---|---|---|
| EV-01 | Las 14 pruebas de escribir y derogar | `plataforma/nucleo/reglas/tests_redaccion.py` |
| EV-02 | Las parecidas sobre el cuerpo real | §1 y §3 |

**Las dos baterías:** 733 pruebas del estándar y 382 de la plataforma, **cero rojas**.

---

## 8. Ciclos anteriores

No hay: es el primer ciclo de la fase.
