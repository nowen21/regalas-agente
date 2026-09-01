# Plan de Pruebas — Fase `I-EP-016-HU-003-un-sello-no-sobrevive-a-un-cambio`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [HU-003](../HU-003-aplicar-el-checklist-y-guardar-su-sello.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que el checklist se lee del estándar, que el sello queda con su versión y su fecha, y que **la comparación por fechas no se presenta como veredicto**.

### 1.2 Alcance

**Entra:** leer las filas, leer el sello, la comparación por fechas, el veredicto del estándar y el molde.

**No entra:** responder las filas.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las cinco decisiones técnicas |
| [documentacion/reglas/spec.md](../../../../reglas/spec.md) | El módulo |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| Las filas | Que se lean, con su respaldo y su criterio |
| La cabecera de la tabla | Que **no** cuente como fila |
| El sello | Contra qué versión y cuándo |
| La comparación por fechas | Que exista **con su nombre** |
| El molde | Veredicto, cuentas, motivos y aviso de caducidad |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De nombre** | Que la función que compara fechas no se llame como un veredicto |
| De contenido | Que el molde traiga lo que el formato exige |
| **Sobre lo real** | Los sellos de las 248 reglas vigentes |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-003 | **185 avisos falsos** si las fechas fueran el veredicto |
| Alta | CP-004 | Un sello mal armado da confianza sin respaldo |
| Media | CP-001, CP-002 | Leer las filas y el sello |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/reglas/` entera, y las dos baterías completas.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- La `HU-002` cerrada.
- Medido el checklist: 20 filas.

### 4.2 Criterios de salida

- Los cuatro casos ejecutados.
- **Los sellos del cuerpo real, medidos**, con la diferencia entre las dos formas de medirlos escrita.
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **la comparación por fechas se presenta como el veredicto**. Ese aviso saldría en 185 de 248 reglas, y un aviso así enseña a ignorarlo.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| Transversal: se leen las filas | CP-001 | De sistema |
| CA-02: el sello se lee | CP-002 | De contenido |
| CA-02: las fechas no son el veredicto | CP-003 | **De nombre** |
| CA-01 y CA-03: el molde | CP-004 | De contenido |

---

## 6. Casos de prueba

### CP-001 — Se leen las filas del checklist

- Se leen con su número, su respaldo y su criterio.
- **La cabecera de la tabla no es una fila.**
- Sin checklist se dice, en vez de armar un sello contra nada.

### CP-002 — Se lee el sello de una regla

- Con sello: se dice contra qué versión y en qué fecha.
- Sin sello: se dice, y no hay versión ni fecha.

### CP-003 — Las fechas no son el veredicto

**El caso que decide la fase.**

| Entrada | Se espera |
|---|---|
| Sellada antes de tocar el archivo | No lo parece |
| Tocada después de sellar | **Lo parece**, y nada más |
| Sin sello | Lo parece siempre |
| Sin fecha de cambio | Lo parece: no se puede afirmar |

**Y una prueba de nombre:** que exista `veredicto_del_estandar` y **que no exista** una función que se llame como si las fechas decidieran.

### CP-004 — El molde del sello

- Todo en sí: **CUMPLE**, con la cuenta.
- Con un no: **NO CUMPLE**.
- Una fila que no aplica: su motivo queda escrito.
- Sin motivo: queda **un hueco marcado**, que se ve.
- Siempre trae su aviso de caducidad.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

Un checklist y reglas de mentiras en carpetas temporales. El cuerpo real **solo se mide**.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Si las respuestas del checklist son correctas.** Buena parte de las filas pide criterio, y eso lo responde una persona.

---

## 8. Herramientas

El corredor de la plataforma y la librería estándar. **Ninguna dependencia nueva.**

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | Las fechas se presentan como veredicto |
| **Alta** | Una fila que no aplica queda sin motivo · el molde no trae el aviso de caducidad |
| **Media** | La cabecera se cuenta como fila |

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
| Reglas con sello vencido según el estándar | **El número escrito** |
| Reglas que lo parecerían por fechas | **El número escrito**, para verlos al lado |
| Reglas reales tocadas | **Cero** |

### 12.2 Dónde se miden

Sobre el cuerpo real, y escrito en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Probar solo con la forma barata de medir | Se corre también la del estándar, y se ponen los dos números al lado |
| Escribir un sello en una regla real al probar | Las pruebas arman el bloque y no lo guardan |

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
