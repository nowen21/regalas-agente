# Plan de Pruebas — Fase `F-EP-015-HU-003-la-puerta-corre-lo-que-ya-funcionaba`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [HU-003](../HU-003-no-publicar-lo-que-rompe-lo-anterior.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que **una versión que rompió algo no se publica**, que lo que obliga a rehacer se declara, y que un «no se pudo revisar» tampoco pasa.

### 1.2 Alcance

**Entra:** juntar el veredicto de las comprobaciones, el resultado de la suite y el estado de las funcionalidades, y decidir.

**No entra:** publicar.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las seis decisiones técnicas |
| [documentacion/comprobaciones/spec.md](../../../../comprobaciones/spec.md) | El módulo |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| Las comprobaciones en rojo | Que detengan |
| Las pruebas en rojo | Que detengan |
| «No cumple» | Que detenga y se nombre |
| «Sin verificar» | Que se declare y **no** detenga |
| El «no se pudo» | Que **no** pase |
| El tiempo | Que se reporte |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De que NO pase** | Es casi toda la fase: lo que no debe publicarse |
| De partición | Cada combinación de verde y rojo |
| **Sobre lo real** | Este repositorio, que está en verde y **tiene que pasar** |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-001 | **Es el criterio que decide.** Publicar no se deshace del lado de quien recibe |
| Crítica | CP-004 | Un «no se pudo» tratado como «pasó» es publicar a ciegas |
| Alta | CP-002 | Lo que obliga a rehacer |
| Alta | CP-003 | **Un rojo falso enseña a ignorar la puerta** |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/comprobaciones/` entera, y las dos baterías completas.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- `F-020` y `F-021` cerradas.

### 4.2 Criterios de salida

- Los cinco casos ejecutados.
- **La puerta corrida sobre este repositorio, con el tiempo escrito.**
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **la puerta da un rojo con todo en verde**. Un rojo falso es peor que no tener puerta: enseña a ignorarla, y el día que el rojo sea de verdad nadie lo va a mirar.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01 — lo que rompió no se publica | CP-001 | Que **no** pase |
| CA-02 — lo que obliga a rehacer se declara | CP-002 | De partición |
| CA-03 — lo que no rompió pasa, sin trabajo manual | CP-003 | De sistema |
| CA-04 — sin revisar no se publica | CP-004 | Que **no** pase |
| Transversal — cero comprobaciones | CP-005 | De partición |

---

## 6. Casos de prueba

### CP-001 — Una versión que rompió algo no se publica

**El caso que decide la fase.**

| Entrada | Se espera |
|---|---|
| Comprobaciones en rojo, pruebas en verde | No pasa |
| Comprobaciones en verde, pruebas en rojo | No pasa |
| Las dos en verde | Pasa |

### CP-002 — Lo que obliga a rehacer se declara

- Una funcionalidad en «no cumple»: **detiene y se nombra**.
- Funcionalidades sin verificar: **se declaran y no detienen**. Que no tengan prueba no quiere decir que esta versión las rompió.

### CP-003 — Lo que no rompió nada pasa, sin trabajo manual

- **Sobre este repositorio, que está en verde:** la puerta pasa.
- Una sola orden corre todo.
- **El tiempo se reporta**, sea el que sea.

### CP-004 — Sin revisar no se publica

| Entrada | Se espera |
|---|---|
| Un proyecto que no existe | No pasa, y lo dice |
| Sin veredicto | No pasa |
| Las baterías no corrieron | No pasa |

**Un «no se pudo» tratado como «pasó» es publicar a ciegas.**

### CP-005 — Cero comprobaciones tampoco pasa

- Viene del veredicto: cero no es verde, y la puerta lo hereda.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

Veredictos armados a mano para la partición, y este repositorio para la corrida entera.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Un proyecto realmente roto.** Los rojos se prueban armando el veredicto, no rompiendo el repositorio: romperlo a propósito para probar la puerta es el tipo de prueba que se olvida deshacer.

---

## 8. Herramientas

El corredor de la plataforma y el punto de entrada del estándar. **Ninguna dependencia nueva.**

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | Un «no se pudo» pasa · algo roto pasa |
| **Alta** | **Un rojo falso** · lo que obliga a rehacer no se nombra |
| **Media** | El tiempo no se reporta |

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
| Rojos falsos | **Cero** |
| «No se pudo» que pasan | **Cero** |
| Cuánto tarda la puerta | **El número escrito** |

### 12.2 Dónde se miden

Sobre este repositorio, y escrito en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Romper el repositorio para probar el rojo | No se rompe: el rojo se arma en el veredicto |
| Dar por buena la puerta sin correrla entera | Se corre entera sobre este repositorio |

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
