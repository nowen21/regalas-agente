# Plan de Pruebas — Fase `H-EP-016-HU-002-derogar-marca-y-no-borra`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [HU-002](../HU-002-escribir-corregir-y-derogar-una-regla.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que una regla se escribe con su molde, que **derogar no borra**, y que antes de guardar se ven las que hablan de lo mismo **con lo que eso no puede decir**.

### 1.2 Alcance

**Entra:** el molde, escribir, derogar, y las reglas parecidas.

**No entra:** el checklist y su sello.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las seis decisiones técnicas |
| [documentacion/reglas/spec.md](../../../../reglas/spec.md) | La §5.2: qué hace y qué no hace la lista de parecidas |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| El molde | Que traiga el encabezado, el cuerpo y el ejemplo |
| Los huecos | Que la regla nazca incompleta **y se le note** |
| El nombre del archivo | Que salga del título, sin tildes |
| Derogar | **Que marque y conserve** |
| Lo que no se deroga | Una que no existe, una ya derogada, una blindada |
| Las parecidas | Que encuentren, que no inventen, y **que no miren las derogadas** |
| El aviso | Que diga lo que esto no puede decir, **encuentre o no** |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De que NO pase** | Borrar al derogar, y derogar una blindada |
| De partición | Las tres razones por las que no se deroga |
| De contenido | Que el archivo escrito traiga lo que el formato exige |
| **Sobre lo real** | Las parecidas, contra las 248 vigentes |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-006 | **Derogar no borra.** Lo que se borra no se puede volver a leer |
| Alta | CP-007 | Si nadie ve las parecidas, se repite una regla que ya existía |
| Alta | CP-005 | Que la regla quede con su molde |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/reglas/` entera, y las dos baterías completas.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- La fase anterior cerrada, con la numeración.
- El formato canónico y la marca de derogación, verificados sobre reglas reales.

### 4.2 Criterios de salida

- Los tres casos ejecutados.
- **Las parecidas corridas sobre el cuerpo real**, con lo que encuentre escrito.
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **derogar pierde una línea del texto original**. Es la parte que no se deshace: lo que se borró ya no se puede volver a leer para entender por qué existía.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01: la regla queda con su identificador | CP-005 | De contenido |
| CA-02: derogar marca y conserva | CP-006 | Que **no** pase |
| CA-03: se muestran las que hablan de lo mismo | CP-007 | De sistema |

---

## 6. Casos de prueba

### CP-005 — Se escribe una regla nueva

- Queda guardada con el identificador que le tocaba.
- El archivo trae el encabezado, el cuerpo y el ejemplo INCORRECTO/CORRECTO.
- **Nace con sus huecos puestos.**
- El nombre del archivo sale del título, sin tildes.

### CP-006 — Derogar no borra

**El caso que decide la fase.**

| Entrada | Se espera |
|---|---|
| Una regla vigente | Marcada, **y su texto original entero** |
| La misma, después | Ya no está entre las vigentes |
| Su identificador | **Sigue ocupado** |
| Una que no existe | Se dice |
| Una ya derogada | Se dice |
| Una blindada | Se dice, y no se toca |

### CP-007 — Las reglas que hablan de lo mismo

- Con el título de una regla vigente: la encuentra.
- Con un título sin nada que ver: no devuelve nada.
- **No mira las derogadas:** una derogada ya no rige, no puede contradecir a nadie.
- **El aviso dice lo que esto no puede decir, encuentre o no encuentre.**

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

Un cuerpo de reglas de mentiras para escribir y derogar. **El cuerpo real solo se mira**, nunca se escribe.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Si la regla escrita es buena.** Eso no lo puede decir ningún programa: el criterio es de una persona, y la ficha lo dice.

**Y si dos reglas se contradicen.** Se comprueba que se muestren las que se parecen; que se contradigan depende de lo que significan.

---

## 8. Herramientas

El corredor de la plataforma y la librería estándar. **Ninguna dependencia nueva.**

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | Derogar pierde texto · se deroga una blindada |
| **Alta** | La regla nace sin sus huecos · el aviso no dice lo que no puede decir |
| **Media** | Las parecidas se llenan de coincidencias sin sentido |

### 9.2 Flujo · 9.3 Contenido mínimo · 9.4 Registro

En el `resultado_pruebas.md` de esta fase.

---

## 10. Cronograma

Una jornada, la del 2026-09-01.

---

## 11. Roles y responsabilidades

Una sola persona cumple los roles. Quien aprueba es el usuario.

---

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Objetivo |
|---|---|
| Líneas perdidas al derogar | **Cero** |
| Blindadas derogadas | **Cero** |
| Reglas parecidas encontradas sobre un título real | **El número escrito** |

### 12.2 Dónde se miden

Sobre el cuerpo de reglas real, y escrito en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Escribir o derogar sobre el cuerpo real al probar | Las pruebas usan un cuerpo de mentiras; el real solo se lee |
| Dar por buenas las parecidas con un ejemplo inventado | Se corren contra las 248 vigentes, con el título de una que ya existe |

---

## 14. Control de versiones

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-09-01 | Ing. José Dúmar Jiménez Ruíz | Creación del plan de pruebas de la fase |

---

## 15. Aprobación

| Rol | Nombre | Aprobación |
|---|---|---|
| Usuario | Ing. José Dúmar Jiménez Ruíz | ☑ Autorizada la épica entera el 2026-09-01 |
