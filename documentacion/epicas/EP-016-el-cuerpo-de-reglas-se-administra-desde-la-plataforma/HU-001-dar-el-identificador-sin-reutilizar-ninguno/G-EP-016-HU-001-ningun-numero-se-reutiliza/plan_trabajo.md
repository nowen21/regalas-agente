# Plan de Trabajo — Fase `G-EP-016-HU-001-ningun-numero-se-reutiliza` (módulo Reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación. El requisito vive en la HU; las pruebas, en el `plan_pruebas`; lo que quedó hecho, en el `funcionalidad_implementada.md`.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `G-EP-016-HU-001-ningun-numero-se-reutiliza` |
| **Épica** | [EP-016](../../epica.md) |
| **HU** | [HU-001 Dar el identificador sin reutilizar ninguno](../HU-001-dar-el-identificador-sin-reutilizar-ninguno.md) — **una sola** (`F12.1`) |
| **Módulo** | Reglas |
| **Especificación del módulo** | [documentacion/reglas/spec.md](../../../../reglas/spec.md) |
| **Fecha apertura** | 2026-09-01 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN:**

- ✨ **Funcionalidad nueva:** `F-006`, la primera de Reglas y la que las demás necesitan.

> **El usuario autorizó ejecutar sin aprobar paso por paso** el 2026-09-01.

**CA de la HU que cubre esta fase:** los tres, todos ☑.

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** que cada regla nueva reciba un identificador que nadie tuvo antes, contando también las derogadas.

**Es lo primero de la épica porque es lo único irreversible.** Reutilizar un número hace que toda cita escrita antes apunte a otra cosa, y no se ve leyendo.

**Fuera de alcance:** escribir la regla, que es la fase siguiente.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo medido el 2026-09-01 sobre este repositorio:**

| Qué se midió | Resultado |
|---|---|
| Reglas en total | **257** |
| Vigentes | 248 |
| Derogadas | **9** |
| Capítulos con prefijo propio | 24 |
| Huecos de numeración | **Ninguno** en los capítulos revisados |

**El estándar ya sabe leer sus reglas:** las parte, les saca el identificador y distingue la derogada de la vigente. Se usa por un puente.

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/reglas/catalogo.py` | Nuevo | Servicio | El puente hacia el lector del estándar |
| `plataforma/nucleo/reglas/numeracion.py` | Nuevo | Servicio | El siguiente libre, y la comprobación |
| `plataforma/nucleo/reglas/apps.py` | Nuevo | Config | |
| `plataforma/nucleo/reglas/management/commands/reglas.py` | Nuevo | Orden | El catálogo y el siguiente |
| `plataforma/nucleo/reglas/tests.py` | Nuevo | Prueba | Los tres CA |
| `plataforma/config/settings/base.py` | Modificar | Config | `nucleo.reglas` en la lista |
| `documentacion/reglas/spec.md` | Nuevo | Especificación | Módulo nuevo |

**Ninguna entidad y ninguna migración:** el cuerpo de reglas **es** el conjunto de archivos.

### 2.2 Matriz de dependencias del refactor

No aplica: todo es nuevo, y el lector del estándar no se toca.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **El lector de reglas se usa por un puente** | Escribir uno propio | Dos lectores se separan, y el día que el formato cambie uno va a leer mal sin avisar |
| **El siguiente es el que sigue al mayor** | El primer hueco libre | Rellenar huecos es la única forma de reutilizar un número sin darse cuenta |
| **Las derogadas cuentan** | Contar solo las vigentes | Su identificador sigue citado en documentos de hace años |
| **Sin lector se revienta** | Devolver una lista vacía | Una lista vacía se lee como «no hay reglas», y ahí el siguiente sería el uno |
| **Los huecos se pueden mirar, no usar** | No mostrarlos | Sirven para revisar el cuerpo; lo que se ve ahí es lo que nunca se va a entregar |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | El puente hacia el lector del estándar | Servicio | 1 h | — | — | EV-01 |
| T-02 | Los identificadores usados, con las derogadas | Servicio | 1 h | T-01 | CA-02 | EV-01 |
| T-03 | El siguiente libre | Servicio | 1 h | T-02 | CA-01 | EV-01 |
| T-04 | La comprobación de antes de guardar | Servicio | 1 h | T-02 | CA-03 | EV-01 |
| T-05 | Los huecos, para mirar | Servicio | 1 h | T-02 | CA-02 | EV-01 |
| T-06 | La orden de consola | Orden | 1 h | T-03 | Todos | EV-02 |
| T-07 | Las pruebas de los tres CA | Test | 2 h | T-06 | Todos | EV-01 |
| T-08 | **Correrlo sobre este repositorio** | Medición | 1 h | T-06 | CA-01 | EV-02 |

**Total estimado:** 9 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-06 → T-08.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Sobre este repositorio, capítulo por capítulo | EV-01, EV-02 | 2026-09-01 | ☑ |
| CA-02 | Con un capítulo con derogadas y huecos | EV-01 | 2026-09-01 | ☑ |
| CA-03 | Con un identificador vigente y con uno derogado | EV-01 | 2026-09-01 | ☑ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas del módulo | `plataforma/nucleo/reglas/tests.py` |
| EV-02 | La corrida sobre este repositorio | `resultado_pruebas.md` §1 |

---

## 6. Datos y ambiente de prueba

Un cuerpo de reglas de mentiras, con una vigente y una derogada, y este repositorio para la medición. Solo se lee.

---

## 7. Reversión / rollback  ·  Q11

Nada que revertir: no escribe.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Ninguna migración, ninguna dependencia nueva.

---

## 9. Reglas aplicadas  ·  Q13

- Base: [`20·M11`](../../../../../base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md), que es la que manda acá. Y [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F19`](../../../../../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md).
- Producto: las `RN-1` a `RN-4` de la historia.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | **Que se rellene un hueco creyendo que está libre** | **Alto — no se deshace** | El siguiente es el que sigue al mayor | Cerrado por diseño |
| B-02 | Que el lector no esté y se devuelva vacío | Alto | Se revienta en vez de callar | Cerrado |
| B-03 | Que un identificador con punto consuma un número | Medio | `F12.1` cuenta como 12: es parte de otra regla | Cerrado |

---

## 11. Definition of Done

- [x] Los tres CA verificados con evidencia
- [x] Corrido sobre este repositorio, capítulo por capítulo
- [x] Las dos baterías en verde
- [x] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
