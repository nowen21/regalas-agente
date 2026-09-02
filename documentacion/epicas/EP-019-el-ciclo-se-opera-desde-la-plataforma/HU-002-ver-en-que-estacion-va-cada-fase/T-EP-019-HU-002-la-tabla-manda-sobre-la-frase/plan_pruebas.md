# Plan de Pruebas — Fase `T-EP-019-HU-002-la-tabla-manda-sobre-la-frase`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [HU-002](../HU-002-ver-en-que-estacion-va-cada-fase.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que **la estación de una fase sale de su tabla**, que se dice qué puerta falta, y que una fase detenida dice desde cuándo.

### 1.2 Alcance

**Entra:** leer la tabla, las dos marcas, «sin marcar», el modelo de la tabla y los días quieta.

**No entra:** marcar las estaciones, y reescribir las fases viejas.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las decisiones técnicas |
| [documentacion/ciclo-de-vida/spec.md](../../../../ciclo-de-vida/spec.md) | El módulo |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| La tabla | De trece estaciones, de once, y con las dos marcas |
| La frase | Cuando coincide con la tabla y cuando no |
| La casilla con prosa | Que no se cuente como pendiente |
| La fecha | Cuando está y cuando no |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **Contra datos reales** | Las 209 fases del repositorio, que es donde aparecieron las tres sorpresas |
| **De distinción** | Tres respuestas —cumplida, pendiente, sin marcar— y no dos |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-007 | **Es el que descubrió que el lector suponía un solo modelo** |
| Alta | CP-004 | Si la frase manda sobre la tabla, el estado vuelve a depender de la memoria |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/ciclo_de_vida/` entera, y las dos baterías completas.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Las fases del repositorio, legibles.

### 4.2 Criterios de salida

- Todos los casos ejecutados.
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **alguna fase del repositorio se modifica** durante la lectura. Esta fase es de solo lectura.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01 | CP-004 | De lectura |
| CA-02 y CA-03 | CP-005 | De mensaje |
| Transversal | CP-007 | Contra datos reales |

---

## 6. Casos de prueba

### CP-004 — La tabla manda sobre la frase

- La estación actual es la primera que no está cumplida.
- Si la frase dice otra cosa, **manda la tabla y se dice**.
- Una fase con todo marcado está terminada, y la estación `N/A` no la detiene.

### CP-005 — Se ve qué falta y desde cuándo

- Sale el **nombre** de la puerta, no solo el número.
- Una fase detenida dice cuántos días lleva.
- **La que no dice desde cuándo se distingue de la de cero días.**
- Se leen todas las fases del proyecto, y la menos avanzada sale primero.

### CP-007 — Lo que salió al correrlo contra las 209 fases

**Los tres casos que decidieron el diseño, y ninguno se pensó antes.**

- **La marca vieja también cuenta:** 76 fases cierran con `✅`.
- **Una estación con prosa no es una estación pendiente.**
- **Una tabla de otro modelo no se compara con la frase:** 107 de 209 no son de trece estaciones.

**11 pruebas** cubren estos casos.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

Tablas de estaciones de mentiras, de trece y de menos, con las dos marcas. Y **la corrida contra las 209 fases reales del repositorio**, que es de solo lectura.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Las 33 fases que siguen en desacuerdo.** Después de las tres correcciones quedan 33 cuya frase y cuya tabla no coinciden de verdad. **Son reales**, y esta fase no las arregla: arreglarlas es reescribir fases cerradas, y eso no se hace.

---

## 8. Herramientas

El corredor de la plataforma. **Ninguna dependencia nueva.**

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | Se acusa en falso a una fase · se reescribe una fase cerrada |
| **Alta** | Una fase terminada aparece sin cerrar |
| **Media** | No se distingue «no se marcó» de «pendiente» |

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
| Fases acusadas en falso | **Cero** |
| Fases cerradas reescritas | **Cero** |
| Fases terminadas contadas como abiertas | **Cero** |

### 12.2 Dónde se miden

En las pruebas, y escrito en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Probar solo con tablas escritas hoy | Se corre contra las 209 reales, que traen tres modelos distintos |
| Dar por bueno el número sin mirar la lista | Se leyó la salida fase por fase |

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
