# Plan de Pruebas — Fase `X-EP-020-HU-002-sin-datos-no-es-cero`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [HU-002](../HU-002-reportar-como-va-cada-proyecto.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que **el reporte usa la misma medida y dice cuál es**, y que **un proyecto sin datos aparece así**.

### 1.2 Alcance

**Entra:** el avance, la deuda, la vencida, las quietas y la definición de cada columna.

**No entra:** ordenar por bueno o malo, y la pantalla.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las decisiones técnicas |
| [documentacion/avisos/spec.md](../../../../avisos/spec.md) | El módulo |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| El avance | Con fases y sin ninguna |
| La deuda | Separada de la vencida |
| La definición | Que salga impresa con la tabla |
| El orden | Que los sin datos vayan al final |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De distinción** | «Sin datos» y «cero» nunca se escriben igual |
| **De contenido** | La definición sale con la tabla, no aparte |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-005 | **Cero por cien dice «va mal» cuando lo que pasa es que no se sabe** |
| Alta | CP-004 | Una comparación sin su definición engaña |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/avisos/` entera, y las dos baterías completas.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- La fase `W` cerrada.

### 4.2 Criterios de salida

- Todos los casos ejecutados.
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **un proyecto sin datos aparece con un número**.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01 | CP-004 | De contenido |
| CA-02 | CP-004 | De separación |
| CA-03 | CP-005 | De distinción |

---

## 6. Casos de prueba

### CP-004 — El reporte dice qué mide

- El avance es fases cerradas sobre el total, para todos igual.
- **La definición de cada columna sale impresa con la tabla**, incluida la advertencia de que el estándar nunca le puso fecha a una deuda.
- La deuda y la vencida salen separadas.

### CP-005 — Sin datos no es cero

**El caso que decide la fase.**

- Un proyecto sin ninguna fase **no dice cero por cien**: dice «sin datos».
- El reporte lo nombra aparte, con la frase «no es cero».
- **Los sin datos van al final**, no primeros.
- Sin ningún proyecto conectado, se dice; no se deja la tabla en blanco.

**7 pruebas** cubren estos casos.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

Carpetas temporales con fases, historias e inventarios de mentiras. Y **la corrida contra este repositorio**, que es de solo lectura.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Dos proyectos de verdad, de tamaños distintos.** Hoy hay uno solo conectado; la comparación se probó con proyectos de mentiras. Que la misma medida sea justa entre un proyecto de 209 fases y uno de tres **no lo dice ninguna prueba**: lo dice quien los compara, y para eso está la definición impresa.

---

## 8. Herramientas

El corredor de la plataforma. **Ninguna dependencia nueva.**

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | Un proyecto sin datos aparece con un número |
| **Alta** | La tabla sale sin su definición |
| **Media** | La deuda y la vencida se confunden |

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
| Proyectos sin datos que salen con un número | **Cero** |
| Columnas sin definición al lado | **Cero** |

### 12.2 Dónde se miden

En las pruebas, y escrito en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Probar solo con proyectos que tienen datos | El caso que decide es justamente el que no los tiene |

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
