# Plan de Pruebas — Fase `G-EP-016-HU-001-ningun-numero-se-reutiliza`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [HU-001](../HU-001-dar-el-identificador-sin-reutilizar-ninguno.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que **ningún identificador se reutiliza**, ni el de una regla derogada, y que se rechaza guardar con uno ya usado.

### 1.2 Alcance

**Entra:** leer el cuerpo de reglas, los identificadores usados, el siguiente libre y la comprobación previa.

**No entra:** escribir la regla.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las cinco decisiones técnicas |
| [documentacion/reglas/spec.md](../../../../reglas/spec.md) | La §5.1: por qué el siguiente es el que sigue al mayor |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| El puente | Que lea, y que reviente si no está el lector |
| Las vigentes y las derogadas | Que se distingan, **y que las dos cuenten para el número** |
| El siguiente libre | Con reglas, sin ninguna, y con huecos |
| La comprobación previa | Con uno vigente, con uno derogado y con uno libre |
| Los huecos | Que se vean, y que no se entreguen |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De que NO pase** | Reutilizar un identificador es lo único que esta fase no puede permitir |
| De partición | Vigente, derogada, inexistente |
| **Sobre lo real** | Los 24 capítulos de este repositorio |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-004 | **Es el criterio que decide.** Una cita vieja apuntaría a otra cosa |
| Crítica | CP-003 | Guardar con uno usado deja dos reglas con el mismo número |
| Alta | CP-002 | El siguiente libre |
| Media | CP-001 | Leer el cuerpo |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/reglas/` entera, y las dos baterías completas.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- La especificación del módulo, con su §5.1.
- Medido el cuerpo de reglas de este repositorio.

### 4.2 Criterios de salida

- Los cuatro casos ejecutados.
- **El siguiente identificador de cada capítulo, comprobado sobre este repositorio.**
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **se entrega un identificador que ya existe**. No hay arreglo posterior: las citas que se escriban con él ya apuntarían mal.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| Transversal: se lee el cuerpo | CP-001 | De sistema |
| CA-01: el siguiente libre | CP-002 | De partición |
| CA-03: no se guarda con uno usado | CP-003 | Que **no** pase |
| CA-02: el de una derogada no se reasigna | CP-004 | Que **no** pase |

---

## 6. Casos de prueba

### CP-001 — Se lee el cuerpo de reglas

- Se leen las vigentes y las derogadas.
- La derogada **no está entre las vigentes** y **sí entre todas**: su identificador sigue ocupado.
- **Sin el lector del estándar se revienta**, en vez de devolver una lista vacía.

### CP-002 — El siguiente identificador

| Entrada | Se espera |
|---|---|
| Un capítulo con reglas hasta la N | La N más uno |
| Un capítulo sin reglas | El uno |
| Los usados de un capítulo con una derogada | La derogada adentro |

### CP-003 — No se guarda con un identificador usado

- Uno vigente: se rechaza.
- Uno derogado: se rechaza.
- Uno libre: pasa.

### CP-004 — El de una derogada no se reasigna

**El caso que decide la fase.**

- El identificador de una derogada sigue usado.
- No se puede volver a pedir.
- **Con huecos por debajo del mayor, el siguiente sigue siendo el que sigue al mayor**, y los huecos se pueden mirar aparte.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

Un cuerpo de reglas de mentiras en una carpeta temporal, con una vigente y una derogada, y este repositorio para la medición.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Si el formato de una regla cambia.** Eso lo sabe el lector del estándar, con sus propias pruebas. Acá se prueba que la plataforma lo use y cuente bien lo que responde.

---

## 8. Herramientas

El corredor de la plataforma y el lector del estándar. **Ninguna dependencia nueva.**

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | Se entrega un identificador ya usado · se rellena un hueco |
| **Alta** | Una derogada no cuenta para el número · sin lector se devuelve vacío |
| **Media** | Los huecos no se ven |

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
| Identificadores entregados que ya existían | **Cero** |
| Huecos rellenados | **Cero** |
| Capítulos con su siguiente comprobado | Todos los que se revisen |

### 12.2 Dónde se miden

Sobre este repositorio, y escrito en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Probar solo con un capítulo sin derogadas | El cuerpo de mentiras trae una derogada desde el principio |
| Dar por bueno el siguiente sin cruzarlo | Se compara contra los usados de verdad |

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
