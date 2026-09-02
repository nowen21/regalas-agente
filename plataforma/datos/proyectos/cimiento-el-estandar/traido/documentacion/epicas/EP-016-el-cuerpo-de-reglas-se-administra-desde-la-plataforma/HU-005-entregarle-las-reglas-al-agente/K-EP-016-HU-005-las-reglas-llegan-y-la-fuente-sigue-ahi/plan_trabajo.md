# Plan de Trabajo — Fase `K-EP-016-HU-005-las-reglas-llegan-y-la-fuente-sigue-ahi` (módulo Reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación. El requisito vive en la HU; las pruebas, en el `plan_pruebas`; lo que quedó hecho, en el `funcionalidad_implementada.md`.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `K-EP-016-HU-005-las-reglas-llegan-y-la-fuente-sigue-ahi` |
| **Épica** | [EP-016](../../epica.md) |
| **HU** | [HU-005 Entregarle las reglas al agente](../HU-005-entregarle-las-reglas-al-agente.md): **una sola** (`F12.1`) |
| **Módulo** | Reglas |
| **Especificación del módulo** | [documentacion/reglas/spec.md](../../../../reglas/spec.md) |
| **Fecha apertura** | 2026-09-01 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN:**

- ✨ **Funcionalidad nueva:** `F-009`, entregarle las reglas al agente al abrir sesión.

> **El usuario autorizó ejecutar sin aprobar paso por paso** el 2026-09-01.

**CA de la HU que cubre esta fase:** los tres, todos ☑.

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** que las reglas vigentes de un proyecto se entreguen enteras, rápido, y que si esto falla **se diga dónde está la fuente**.

**Se entrega el texto, no un resumen.** Un resumen de una regla es otra regla, y la que el agente obedecería sería la del resumen.

**Fuera de alcance:** que el agente las obedezca. Eso lo cubre `F-020`, ya construido.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo medido el 2026-09-01 sobre este repositorio:**

| Qué se midió | Resultado |
|---|---|
| Reglas vigentes | **248** |
| Archivos del cuerpo de reglas | **124** |
| Caracteres en total | **679 511** |
| **Cuánto tarda entregarlo** | **0,17 s** |

El límite de la ficha son dos segundos, y sobra con un orden de magnitud.

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/reglas/entrega.py` | Nuevo | Servicio | Entregar y medir |
| `plataforma/nucleo/reglas/management/commands/entregar_reglas.py` | Nuevo | Orden | Pedirlo |
| `plataforma/nucleo/reglas/tests_entrega.py` | Nuevo | Prueba | Los tres CA de esta fase y los de la siguiente |
| `documentacion/reglas/spec.md` | Modificar | Especificación | Su §13, para nombrar la fase |

**Ninguna entidad y ninguna migración.**

### 2.2 Matriz de dependencias del refactor

Usa el lector de `F-006` y no lo modifica.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **Se entrega el texto** | Un resumen | Un resumen de una regla es otra regla |
| **La fuente se nombra siempre** | Solo cuando falla | Nombrarla siempre recuerda que esto no es un intermediario obligatorio |
| **Si no se puede, se dice por qué** | Devolver una lista vacía | Una lista vacía se leería como «este proyecto no tiene reglas» |
| **El tiempo se reporta** | Suponerlo | El límite de la ficha es un número, y se comprueba con otro número |
| **Los capítulos van en el orden de sus nombres** | Alfabético puro | Los archivos están numerados, y ese es el orden en que se leen |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | Recorrer los capítulos en su orden | Servicio | 1 h | — | CA-01 | EV-01 |
| T-02 | Leer su texto, con sus rutas relativas | Servicio | 1 h | T-01 | CA-01 | EV-01 |
| T-03 | Contar las vigentes | Servicio | 1 h | T-02 | CA-01 | EV-01 |
| T-04 | Medir cuánto tardó | Servicio | 1 h | T-02 | CA-02 | EV-01 |
| T-05 | Decir dónde está la fuente, pase lo que pase | Servicio | 1 h | T-02 | CA-03 | EV-01 |
| T-06 | La orden de consola | Orden | 1 h | T-05 | Todos | EV-02 |
| T-07 | Las pruebas de los tres CA | Test | 2 h | T-06 | Todos | EV-01 |
| T-08 | **Medirlo sobre este repositorio** | Medición | 1 h | T-06 | CA-02 | EV-02 |

**Total estimado:** 9 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-05 → T-06 → T-08.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Sobre este repositorio, mirando que salga el texto | EV-01, EV-02 | 2026-09-01 | ☑ |
| CA-02 | **Midiendo, no suponiendo** | EV-01, EV-02 | 2026-09-01 | ☑ |
| CA-03 | Con un proyecto sin cuerpo de reglas | EV-01 | 2026-09-01 | ☑ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas de la entrega | `plataforma/nucleo/reglas/tests_entrega.py` |
| EV-02 | La medición sobre este repositorio | `resultado_pruebas.md` §1 |

---

## 6. Datos y ambiente de prueba

Un cuerpo de reglas de mentiras, y este repositorio para la medición. Solo se lee.

---

## 7. Reversión / rollback  ·  Q11

Nada que revertir: no escribe.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Ninguna migración, ninguna dependencia nueva.

---

## 9. Reglas aplicadas  ·  Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F19`](../../../../../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md).
- Producto: las `RN-1` a `RN-4` de la historia.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que tarde tanto que estorbe al abrir | Medio | Se mide: **0,17 s** contra un límite de 2 | Cerrado |
| B-02 | **Que un fallo se lea como «no hay reglas»** | **Alto** | Se dice por qué, y dónde está la fuente | Cerrado |
| B-03 | Que se entregue un resumen | Alto | Se entrega el texto, y hay una prueba que lo comprueba | Cerrado |

---

## 11. Definition of Done

- [x] Los tres CA verificados con evidencia
- [x] Medido sobre este repositorio, con el tiempo escrito
- [x] Comprobado que un fallo dice dónde está la fuente
- [x] Las dos baterías en verde
- [x] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
