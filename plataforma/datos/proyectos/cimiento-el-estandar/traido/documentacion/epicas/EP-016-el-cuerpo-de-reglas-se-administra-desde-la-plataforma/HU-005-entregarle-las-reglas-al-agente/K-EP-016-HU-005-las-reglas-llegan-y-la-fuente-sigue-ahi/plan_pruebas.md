# Plan de Pruebas — Fase `K-EP-016-HU-005-las-reglas-llegan-y-la-fuente-sigue-ahi`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [HU-005](../HU-005-entregarle-las-reglas-al-agente.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que las reglas se entregan **enteras y rápido**, y que si esto falla **se dice dónde está la fuente**.

### 1.2 Alcance

**Entra:** recorrer los capítulos, leer su texto, contar las vigentes, medir el tiempo y nombrar la fuente.

**No entra:** que el agente las obedezca.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las cinco decisiones técnicas |
| [documentacion/reglas/spec.md](../../../../reglas/spec.md) | El módulo |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| Los capítulos | Que salgan con su texto y su ruta relativa |
| El texto | **Que sea el texto, no un resumen** |
| La cuenta | Cuántas vigentes y bajo qué versión |
| El tiempo | Que se reporte, **y que esté por debajo de dos segundos** |
| La fuente | Que se nombre **siempre** |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De contenido** | Que llegue el texto y no un resumen |
| **De rendimiento** | El `CA-2` es un número, y se comprueba con otro número |
| **De que NO pase** | Que un fallo devuelva una lista vacía |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-003 | **Una lista vacía se leería como «no hay reglas»** |
| Alta | CP-001 | Si llega un resumen, el agente obedece el resumen |
| Alta | CP-002 | Si estorba al abrir, se apaga |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/reglas/` entera, y las dos baterías completas.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- `F-006` cerrada, con el lector del cuerpo de reglas.

### 4.2 Criterios de salida

- Los tres casos ejecutados.
- **El tiempo medido sobre este repositorio, escrito.**
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **un fallo devuelve una lista vacía sin decir nada**. Ahí un proyecto con reglas parecería no tenerlas, y el agente trabajaría sin ninguna.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01: llegan las reglas | CP-001 | De contenido |
| CA-02: menos de dos segundos | CP-002 | De rendimiento |
| CA-03: si no se puede, la fuente sigue ahí | CP-003 | Que **no** pase |

---

## 6. Casos de prueba

### CP-001 — Se entregan las reglas

- Salen los capítulos con su texto.
- **Se entrega el texto, no un resumen:** una frase de una regla real aparece tal cual.
- Se dice cuántas rigen y bajo qué versión.
- Las rutas salen relativas al proyecto.

### CP-002 — Entregarlas es rápido

- El tiempo se reporta.
- **Está por debajo de dos segundos**, que es lo que la ficha pide.

### CP-003 — Si no se puede, la fuente sigue ahí

**El caso que decide la fase.**

| Entrada | Se espera |
|---|---|
| Un proyecto sin cuerpo de reglas | Se dice por qué |
| El mismo | **Se dice dónde está la fuente** |
| Un proyecto que sí se pudo | La fuente **también** se nombra |

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

Un cuerpo de reglas de mentiras en una carpeta temporal, y este repositorio para la medición.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Un cuerpo de reglas mucho más grande.** Se mide con 248 vigentes y 679 511 caracteres; un proyecto con diez veces eso tendría que volver a medirse.

---

## 8. Herramientas

El corredor de la plataforma y la librería estándar. **Ninguna dependencia nueva.**

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | Un fallo devuelve una lista vacía |
| **Alta** | Se entrega un resumen · tarda más de dos segundos |
| **Media** | Las rutas salen absolutas |

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
| Cuánto tarda entregar | **El número escrito**, por debajo de dos segundos |
| Caracteres entregados | El número escrito |
| Fallos que devuelven vacío | **Cero** |

### 12.2 Dónde se miden

Sobre este repositorio, y escrito en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Medir con un cuerpo de reglas de tres archivos | Se mide con el real: 124 archivos |
| Dar por bueno el límite sin medirlo | Hay una prueba que compara contra los dos segundos |

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
