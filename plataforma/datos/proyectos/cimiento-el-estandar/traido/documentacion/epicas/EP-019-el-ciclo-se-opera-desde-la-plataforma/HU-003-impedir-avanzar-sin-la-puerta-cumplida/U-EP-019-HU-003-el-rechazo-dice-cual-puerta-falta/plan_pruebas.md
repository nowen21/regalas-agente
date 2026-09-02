# Plan de Pruebas — Fase `U-EP-019-HU-003-el-rechazo-dice-cual-puerta-falta`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [HU-003](../HU-003-impedir-avanzar-sin-la-puerta-cumplida.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que **sin la puerta cumplida no se pasa**, y que **el rechazo dice cuál falta**.

### 1.2 Alcance

**Entra:** las tres puertas comprobables y el motivo de cada veredicto.

**No entra:** las otras diez estaciones, e impedirlo de verdad.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las decisiones técnicas |
| [documentacion/ciclo-de-vida/spec.md](../../../../ciclo-de-vida/spec.md) | El módulo |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| La puerta de ejecución | Con la 7 cumplida y sin cumplir |
| La puerta de cierre | Con los tres veredictos |
| El motivo | Que nombre la puerta, en el sí y en el no |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De que NO pase** | Que se cierre una fase sin veredicto |
| **De mensaje** | El motivo nombra la puerta, no solo dice que falta |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-006 | **Cerrar sin veredicto deja escrito que algo funciona sin que conste que se probó** |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/ciclo_de_vida/` entera, y las dos baterías completas.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- La fase `T` cerrada.

### 4.2 Criterios de salida

- Todos los casos ejecutados.
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **una fase pasa una puerta que no cumple**.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01, CA-02 y CA-03 | CP-006 | Que **no** pase, y de mensaje |

---

## 6. Casos de prueba

### CP-006 — La puerta dice cuál falta

**El caso entero de la fase.**

| Entrada | Se espera |
|---|---|
| La estación 7 sin cumplir, y se pide pasar a la 8 | **No pasa**, y el motivo nombra la 7 |
| La 7 cumplida | Pasa, y el motivo dice cuál se cumplió |
| Sin veredicto, y se pide cerrar | **No cierra** |
| Veredicto «No cumple» | **Tampoco cierra**, y se dice qué dice hoy |
| Veredicto «Cumple» | Cierra |
| Una estación sin puerta comprobable | Pasa, **diciendo que no opina** |
| Las tres de un golpe | Salen las tres, todas con motivo |

**7 pruebas** cubren estos casos.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

Tablas de estaciones de mentiras, de trece y de menos, con las dos marcas. Y **la corrida contra las 209 fases reales del repositorio**, que es de solo lectura.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Alguien que se salte la puerta a propósito.** El archivo se puede escribir a mano, y esto no lo impide. Lo que se logra es que saltarla sea **un acto deliberado en vez de un olvido**, y esa es la promesa entera.

---

## 8. Herramientas

El corredor de la plataforma. **Ninguna dependencia nueva.**

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | Una fase cierra sin veredicto |
| **Alta** | El rechazo no nombra la puerta |
| **Media** | Un sí sin motivo |

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
| Fases que pasan una puerta sin cumplirla | **Cero** |
| Veredictos sin motivo | **Cero** |

### 12.2 Dónde se miden

En las pruebas, y escrito en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Probar solo el rechazo | También se prueba el sí, y que traiga motivo |

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
