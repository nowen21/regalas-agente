# Plan de Pruebas — Fase `Y-EP-011-HU-003-la-linea-base-dice-que-es-reconstruida`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [HU-003](../HU-003-medir-el-tiempo-que-se-gasta-revisando.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que **el tiempo sale de lo ya escrito**, que **la línea base dice que es reconstruida**, y que **cuando no se puede comparar se dice**.

### 1.2 Alcance

**Entra:** los huecos, los descartes, la mediana por mes, la línea base y la negativa a comparar.

**No entra:** medir el tiempo del agente, y reconstruir la medición inicial de verdad.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las decisiones técnicas |
| [documentacion/medicion/spec.md](../../../../medicion/spec.md) | El módulo |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| El hueco | Entre la respuesta del agente y el mensaje siguiente |
| Los descartes | El larguísimo, el de un segundo y el que no tiene hora |
| La línea base | Que salga marcada |
| La comparación | Que se niegue cuando no hay con qué |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De cálculo** | Los huecos, con horas puestas a mano |
| **De mensaje** | Que la advertencia salga escrita en la comparación |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-002 | **Una línea base que se presente como un antes hace que la mejora parezca mayor de lo que es** |
| Alta | CP-003 | Un almuerzo contado como revisión sería el mejor dato del reporte |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/medicion/` entera, y las dos baterías completas.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- El histórico indexado.

### 4.2 Criterios de salida

- Todos los casos ejecutados.
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **la línea base sale sin decir que es reconstruida**.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01 | CP-002 | De mensaje |
| CA-02 | CP-001 | De cálculo |
| Transversal | CP-003 y CP-004 | De descarte y de negativa |

---

## 6. Casos de prueba

### CP-001 — Los huecos se miden solos

- El hueco es **entre la respuesta del agente y el mensaje siguiente del usuario**.
- Dos mensajes seguidos del agente no son una revisión.
- Un mensaje sin hora **se cuenta aparte y no se le inventa una**.
- Un «si» de dos segundos no es una revisión.

### CP-002 — La línea base dice que es reconstruida

**El caso que decide la fase.**

- La base es el mes más viejo con datos suficientes, **y viene marcada**.
- Un mes con muy pocas revisiones no sirve de base.
- La comparación **dice que esa base no es un antes de verdad**.

### CP-003 — Las horas no se inventan

- Un hueco de cuatro horas **se descarta, y se cuenta cuántos se descartaron**.
- Uno de una hora sí cuenta.

### CP-004 — Cuando no se puede comparar, se dice

- Con un solo mes **no se compara**, y se explica.
- Sin nada indexado se dice, y **no se devuelve cero**.
- Con dos meses se compara, y se dice hacia dónde.

**14 pruebas** cubren estos casos.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

Sesiones de mentiras con horas puestas a mano, y **la corrida contra el histórico real**: 67 sesiones y 3720 mensajes.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**El antes de verdad.** No existe y no se puede fabricar. Las pruebas comprueban que la línea base salga marcada como reconstruida; **ninguna puede comprobar que sea comparable con el proyecto antes de empezar**, porque de esa época no quedó nada medido.

---

## 8. Herramientas

El corredor de la plataforma. **Ninguna dependencia nueva.**

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | La línea base se presenta como un antes de verdad |
| **Alta** | Un hueco larguísimo se cuenta como revisión · se inventa una hora |
| **Media** | Con un solo mes se devuelve un número |

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
| Comparaciones sin la advertencia | **Cero** |
| Horas inventadas | **Cero** |
| Huecos mayores a dos horas contados como revisión | **Cero** |

### 12.2 Dónde se miden

En las pruebas, y escrito en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Dar por bueno un número sin mirar de qué sale | Se corrió contra el histórico real, y ahí se vio que cabe en un mes |

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
