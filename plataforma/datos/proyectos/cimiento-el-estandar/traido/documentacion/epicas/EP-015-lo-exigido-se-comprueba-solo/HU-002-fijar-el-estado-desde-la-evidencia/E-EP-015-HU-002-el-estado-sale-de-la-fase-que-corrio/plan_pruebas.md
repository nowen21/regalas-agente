# Plan de Pruebas — Fase `E-EP-015-HU-002-el-estado-sale-de-la-fase-que-corrio`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [HU-002](../HU-002-fijar-el-estado-desde-la-evidencia.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que el estado de una funcionalidad **se deriva de la fase que corrió**, que sin prueba queda sin verificar y no se cierra, y que las dos formas de escribir un veredicto se leen las dos.

### 1.2 Alcance

**Entra:** leer el inventario, seguir la trazabilidad, leer el veredicto y derivar el estado.

**No entra:** escribir el estado en el inventario, ni impedir publicar.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las cinco decisiones técnicas |
| [documentacion/comprobaciones/spec.md](../../../../comprobaciones/spec.md) | El módulo |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| El inventario | Que se lean sus funcionalidades |
| La trazabilidad | Que se siga hasta la fase |
| El veredicto | **Sus dos formas** |
| El estado | Verificado, no cumple, sin verificar |
| El cierre | Que lo sin verificar no se cierre |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De partición** | Los tres estados, y qué los produce |
| **De que NO pase** | Que algo sin prueba se pueda cerrar |
| De compatibilidad | La forma vieja de escribir el veredicto |
| **Sobre lo real** | Las 35 funcionalidades de este repositorio |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-002 | **Es lo que impide que el estado lo ponga quien escribe** |
| Crítica | CP-004 | Sin leer la forma vieja, siete funcionalidades cerradas salían sin verificar |
| Alta | CP-001, CP-003 | Los otros dos estados |
| Media | CP-005 | La cuenta sobre lo real |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/comprobaciones/` entera, y las dos baterías completas.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- `F-020` cerrada, con el módulo abierto.
- Medido cuántas funcionalidades tienen fila de trazabilidad.

### 4.2 Criterios de salida

- Los cinco casos ejecutados.
- **La cuenta de este repositorio escrita**, sea la que sea.
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **algo sin prueba sale verificado**. Ahí el estado volvería a ser una opinión, que es justo lo que esta fase viene a quitar.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01 — con prueba, verificado | CP-001 | De sistema |
| CA-02 — sin prueba, sin verificar y sin cerrar | CP-002 | Que **no** pase |
| CA-03 — con prueba fallida, no cumple | CP-003 | De partición |
| CA-04 — las dos formas de veredicto | CP-004 | De compatibilidad |
| Transversal — la cuenta real | CP-005 | De conteo |

---

## 6. Casos de prueba

### CP-001 — Con prueba y evidencia queda verificado

- Una fase que declara «Cumple» deja la funcionalidad verificada, y se puede cerrar.
- **El estado dice de qué fase sale.** Un estado sin origen es una opinión.

### CP-002 — Sin prueba queda sin verificar, y no se cierra

**El caso que decide la fase.**

| Entrada | Se espera |
|---|---|
| Ninguna fase la construye | Sin verificar, y no se cierra |
| Fase declarada que no existe | Sin verificar |
| Fase que existe y no declara veredicto | Sin verificar |

### CP-003 — Con prueba fallida queda «no cumple»

- Sale «no cumple», **con el nombre de la fase**, y no se cierra.
- «No cumple» y «sin verificar» son valores distintos.

### CP-004 — Las dos formas de veredicto se leen las dos

- La forma de la versión 1 se entiende igual que la de ahora.
- **Una fase cerrada no se reescribe para que un programa la entienda.**

### CP-005 — La cuenta sobre este repositorio

- Se cuentan las 35 funcionalidades y se reparten en los tres estados.
- El número queda escrito, sea el que sea.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

Carpetas temporales con inventario, especificación y fases de mentiras, y este repositorio para la cuenta.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Si el veredicto de una fase era correcto.** Acá se lee lo que la fase declaró; que lo declarado fuera cierto lo respondió esa fase en su día.

---

## 8. Herramientas

El corredor de la plataforma y la librería estándar. **Ninguna dependencia nueva.**

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | Algo sin prueba sale verificado |
| **Alta** | Una forma de veredicto no se lee · el estado no dice de dónde sale |
| **Media** | La cuenta no cuadra |

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
| Funcionalidades verificadas | **El número escrito** |
| Funcionalidades construidas que salen sin verificar | **Cero** |
| Documentos modificados al derivar | **Cero** |

### 12.2 Dónde se miden

Sobre este repositorio, y escrito en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Probar solo con la forma nueva de veredicto | Se prueba también la de la versión 1 |
| Dar por buena la cuenta sin cruzarla | Se compara contra qué versiones están construidas |

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
