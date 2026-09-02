# Plan de Pruebas — Fase `J-EP-016-HU-004-sin-decir-que-cambio-no-se-publica`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [HU-004](../HU-004-publicar-una-version-del-cuerpo-de-reglas.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que **sin decir qué cambió no se publica**, que un número no se publica dos veces, y que con la puerta en rojo tampoco.

### 1.2 Alcance

**Entra:** encontrar la entrada del registro, leer su tipo, comprobar el número, pedir la puerta y escribir la versión.

**No entra:** escribir la entrada del registro.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las cinco decisiones técnicas |
| [documentacion/reglas/spec.md](../../../../reglas/spec.md) | El módulo |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| La entrada del registro | Que se encuentre y **que se recorte hasta la siguiente** |
| Su tipo | **En los dos órdenes** en que se ha escrito |
| El número | Que uno ya publicado se rechace |
| La puerta | Que un rojo detenga |
| El archivo de versión | **Que no cambie si algo falta** |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De que NO pase** | Es casi toda la fase: lo que no debe publicarse |
| De partición | Con entrada, sin entrada, con entrada sin tipo |
| De contenido | Que la entrada se recorte donde debe |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-002 | **Sin decir qué cambió, quien adopte no sabe si le toca rehacer algo** |
| Crítica | CP-001 | Dos proyectos con la misma versión y reglas distintas no se deshace |
| Alta | CP-003 | Una versión rota se la lleva quien la adopte |
| Alta | CP-004 | Que el archivo no cambie si algo falta |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/reglas/` entera, y las dos baterías completas.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- `F-022` cerrada, con la puerta.
- Verificado que el tipo se escribe en dos órdenes.

### 4.2 Criterios de salida

- Los cuatro casos ejecutados.
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **se publica algo sin entrada en el registro**. Publicar sin decir qué cambió deja al que adopta sin forma de saber si le toca rehacer algo.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01: un número no se publica dos veces | CP-001 | Que **no** pase |
| CA-02: sin decir qué cambió no se publica | CP-002 | Que **no** pase |
| CA-03: lo que rompe algo no se publica | CP-003 | Que **no** pase |
| CA-01: publicar escribe la versión | CP-004 | De sistema |

---

## 6. Casos de prueba

### CP-001 — No se publica dos veces el mismo número

- Una versión ya publicada se rechaza, y se dice por qué.
- Una que no existe pasa esa comprobación.

### CP-002 — Sin decir qué cambió no se publica

**El caso que decide la fase.**

| Entrada | Se espera |
|---|---|
| Sin entrada en el registro | Se rechaza |
| Con entrada, tipo delante | Se lee el tipo |
| Con entrada, **título delante** | Se lee el tipo igual |
| Con entrada sin tipo | Se rechaza |
| La entrada de una versión | **Recortada hasta la siguiente**, sin arrastrar la de al lado |

### CP-003 — Lo que rompe algo no se publica

- Con la puerta en rojo: se rechaza.
- Con todo en verde: se puede.

### CP-004 — Publicar escribe la versión

- Con todo en verde: el archivo queda con el número nuevo.
- Si falta algo: **el archivo no cambia**, y lo que falta sale **todo junto**.
- Un número sin forma de versión se rechaza.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

Un registro de cambios de mentiras, con las dos formas de escribir una entrada y una sin tipo. **La puerta se simula**: correrla de verdad tarda dos minutos por prueba.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**La puerta corriendo de verdad.** Se prueba que su respuesta se respete; que la puerta acierte lo probó su propia fase.

---

## 8. Herramientas

El corredor de la plataforma y la librería estándar. **Ninguna dependencia nueva.**

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | Se publica sin entrada · se publica dos veces el mismo número |
| **Alta** | El archivo cambia aunque falte algo · el tipo no se lee en un orden |
| **Media** | Lo que falta sale de a uno |

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
| Publicaciones sin entrada en el registro | **Cero** |
| Números publicados dos veces | **Cero** |
| Veces que el archivo cambia faltando algo | **Cero** |

### 12.2 Dónde se miden

En las pruebas, y escrito en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Probar el tipo en un solo orden | Se prueban los dos |
| Publicar de verdad al probar | Se usa un registro y un archivo de versión de mentiras |

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
