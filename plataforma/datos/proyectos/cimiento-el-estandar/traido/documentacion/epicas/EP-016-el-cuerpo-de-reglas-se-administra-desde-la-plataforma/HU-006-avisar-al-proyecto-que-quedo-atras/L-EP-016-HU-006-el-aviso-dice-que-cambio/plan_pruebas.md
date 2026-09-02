# Plan de Pruebas — Fase `L-EP-016-HU-006-el-aviso-dice-que-cambio`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [HU-006](../HU-006-avisar-al-proyecto-que-quedo-atras.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que el aviso **dice qué cambió**, que al día no molesta, y que **un número inventado no pasa por estar al día**.

### 1.2 Alcance

**Entra:** el arreglo del lector del registro, las tres respuestas del desfase, y cuáles obligan a migrar.

**No entra:** subir la versión de un proyecto.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las cinco decisiones técnicas, y la medición que las explica |
| [documentacion/reglas/spec.md](../../../../reglas/spec.md) | El módulo |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| El lector del registro | **Cuántas entradas reconoce**, antes y después |
| Las tres respuestas | Al día · quedó atrás · número inventado |
| El tramo | Que traiga las versiones que separan |
| Los que obligan a migrar | Que salgan primero |
| Lo vacío | Que no declarar nada se responda distinto |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De conteo** | El arreglo del lector se mide contando entradas |
| De partición | Las tres respuestas, cada una |
| **De que NO pase** | Que un número inventado pase por estar al día |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-005 | **A simple vista, un número inventado se parece a ir adelantado** |
| Crítica | CP-004 | Un aviso que no dice qué cambió se ignora, y llevaba 54 versiones así |
| Alta | El conteo del lector | Es lo que muestra que el arreglo sirvió |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/reglas/` entera, **y las dos baterías completas**, porque se tocó el estándar.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Medido cuántas entradas reconoce el lector hoy.

### 4.2 Criterios de salida

- Los casos ejecutados.
- **El conteo del lector, antes y después, escrito.**
- El cambio al estándar, versionado y registrado.
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **el arreglo deja de entender el orden viejo**. Serían 143 entradas invisibles a cambio de 54: peor que antes.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01: dice qué cambió | CP-004 | De partición |
| CA-02: al día no molesta | CP-004 | De partición |
| CA-03: un número inventado se dice | CP-005 | Que **no** pase |

---

## 6. Casos de prueba

### CP-004 — El desfase dice qué cambió

| Entrada | Se espera |
|---|---|
| La versión vigente | Al día, sin lista |
| Una versión anterior | El motivo **y** qué cambió |
| Un tramo con una MAYOR | **Sale cuál obliga a migrar** |

### CP-005 — Un número inventado no está al día

**El caso que decide la fase.**

- Una versión que no aparece en el registro: **se dice que ese número no existió nunca**, y no se concluye que va adelantado.
- **No declarar nada** se responde distinto: no es declarar algo falso.

### El conteo del lector

- Antes del arreglo: **143 de 197**, la más reciente reconocida la 34.2.0.
- Después: **más**, y la más reciente es la del día.
- **Y el orden viejo se sigue entendiendo**, que es lo que el criterio de suspensión protege.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

El registro real para el conteo, y un lector simulado para las tres respuestas: así no dependen de qué versión vaya el estándar hoy.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Un registro escrito de una tercera forma.** Se aceptan las dos que existen; una tercera habría que volver a medirla.

---

## 8. Herramientas

El corredor de la plataforma y el lector del estándar. **Ninguna dependencia nueva.**

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | Un número inventado pasa por estar al día · el arreglo pierde el orden viejo |
| **Alta** | El aviso no dice qué cambió · no se dice cuál obliga a migrar |
| **Media** | No declarar nada se responde igual que declarar algo falso |

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
| Entradas del registro que el lector reconoce | **El número, antes y después** |
| Números inventados que pasan por estar al día | **Cero** |
| Entradas del registro reescritas | **Cero** |

### 12.2 Dónde se miden

Sobre el registro real, y escrito en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Probar solo con el orden nuevo | Se cuenta sobre el registro entero, que tiene los dos |
| Que las pruebas dependan de la versión de hoy | El lector se simula para las tres respuestas |

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
