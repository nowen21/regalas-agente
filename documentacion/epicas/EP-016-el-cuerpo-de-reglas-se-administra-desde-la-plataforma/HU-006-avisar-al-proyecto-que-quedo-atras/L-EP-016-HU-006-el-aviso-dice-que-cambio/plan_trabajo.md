# Plan de Trabajo — Fase `L-EP-016-HU-006-el-aviso-dice-que-cambio` (módulo Reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación. El requisito vive en la HU; las pruebas, en el `plan_pruebas`; lo que quedó hecho, en el `funcionalidad_implementada.md`.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `L-EP-016-HU-006-el-aviso-dice-que-cambio` |
| **Épica** | [EP-016](../../epica.md) |
| **HU** | [HU-006 Avisar al proyecto que quedó atrás](../HU-006-avisar-al-proyecto-que-quedo-atras.md): **una sola** (`F12.1`) |
| **Módulo** | Reglas |
| **Especificación del módulo** | [documentacion/reglas/spec.md](../../../../reglas/spec.md) |
| **Fecha apertura** | 2026-09-01 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN:**

- 🩹 **Agujero abierto:** `F-010` estaba construida a medias y sin declarar. El aviso de desfase existía, y **la parte que sirve para decidir no salía**.

> **El usuario autorizó ejecutar sin aprobar paso por paso** el 2026-09-01.

**CA de la HU que cubre esta fase:** los tres, todos ☑.

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** que el aviso de desfase diga **qué cambió**, y que un número inventado se diga como lo que es.

**Decir «estás atrasado» no ayuda a decidir.** Lo que decide es si alguna versión obliga a migrar, cuántas van, y de qué se trataban.

**Fuera de alcance:** subir la versión de un proyecto. Es decisión del usuario.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo medido el 2026-09-01, y es lo que explica la fase:**

| Qué se midió | Resultado |
|---|---|
| Entradas del registro de cambios | **197** |
| **Cuántas reconocía el lector del estándar** | **143** |
| **La más reciente que entendía** | **34.2.0** |
| Versiones publicadas desde entonces | 54, todas invisibles |

**Una convención cambió y el lector se quedó atrás.** El registro se escribía con el tipo delante; cuando `M17` pidió que la entrada abriera contando qué pasó, el orden se invirtió y el lector solo entendía el viejo.

**Consecuencia:** un proyecto en la 35 preguntando qué cambió recibía **nada**, sin que nadie dijera por qué.

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/version.py` | Modificar | Estándar | El lector acepta los dos órdenes |
| `VERSION` · `CHANGELOG.md` | Modificar | Estándar | **`20·M10`**: el cambio se versiona y se registra |
| `plataforma/nucleo/reglas/desfase.py` | Nuevo | Servicio | Las tres respuestas, con qué cambió |
| `plataforma/nucleo/reglas/management/commands/desfase.py` | Nuevo | Orden | Pedirlo |
| `plataforma/nucleo/reglas/tests_entrega.py` | Modificar | Prueba | Los casos del desfase |
| `documentacion/reglas/spec.md` | Modificar | Especificación | Su §13, para nombrar la fase |

### 2.2 Matriz de dependencias del refactor

`validadores/version.py` lo usan el propio estándar y el puente de la plataforma. **Su corrección se comprueba con las dos baterías completas.**

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **El lector acepta los dos órdenes** | Reescribir 54 entradas del registro | Reescribir el registro para que un programa lo entienda es al revés |
| **La corrección se versiona como PARCHE** | No versionarla | `20·M10`: todo cambio se versiona y se registra. No cambia qué se exige: arregla un aviso que salía vacío |
| **Tres respuestas, no dos** | Al día / atrasado | Un número inventado no cabe en ninguna de las dos, y a simple vista se parece a ir adelantado |
| **Lo primero es si alguna obliga a migrar** | Solo el número de versiones | Es lo único del aviso que cambia qué hacer |
| **No declarar nada no es declarar algo falso** | Tratarlos igual | Son problemas distintos y se arreglan distinto |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | **Medir cuántas entradas reconoce el lector** | Medición | 1 h | — | CA-01 | EV-02 |
| T-02 | Que acepte los dos órdenes | Estándar | 2 h | T-01 | CA-01 | EV-02 |
| T-03 | Versionar y registrar la corrección | Estándar | 1 h | T-02 | — | EV-02 |
| T-04 | Comprobar que la versión declarada existió | Servicio | 1 h | — | CA-03 | EV-01 |
| T-05 | Traer las versiones del tramo | Servicio | 1 h | T-02 | CA-01 | EV-01 |
| T-06 | Decir cuáles obligan a migrar | Servicio | 1 h | T-05 | CA-01 | EV-01 |
| T-07 | La orden de consola | Orden | 1 h | T-06 | Todos | EV-02 |
| T-08 | Las pruebas de los tres CA | Test | 2 h | T-07 | Todos | EV-01 |

**Total estimado:** 10 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-05 → T-06 → T-07. La medición va primero: sin ella el arreglo no se ve.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Sobre el registro real, con una versión vieja | EV-01, EV-02 | 2026-09-01 | ☑ |
| CA-02 | Con la versión vigente | EV-01 | 2026-09-01 | ☑ |
| CA-03 | Con un número mayor que el real | EV-01, EV-02 | 2026-09-01 | ☑ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas del desfase | `plataforma/nucleo/reglas/tests_entrega.py` |
| EV-02 | La medición sobre el registro real | `resultado_pruebas.md` §1 |

---

## 6. Datos y ambiente de prueba

El registro real para medir, y un lector simulado para las pruebas: así se comprueban las tres respuestas sin depender de qué versión vaya el estándar hoy.

---

## 7. Reversión / rollback  ·  Q11

El cambio al lector está versionado y registrado. **Si resultara equivocado, se ve enseguida:** las dos baterías lo recorren.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro para la plataforma**, y un **PARCHE** para el estándar. Ninguna migración, ninguna dependencia nueva.

---

## 9. Reglas aplicadas  ·  Q13

- Base: [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md), que obliga a versionar el arreglo del lector.
- Producto: las `RN-1` a `RN-4` de la historia.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | **Que el lector deje de entender el orden viejo al arreglarlo** | **Alto** | Se aceptan los dos, y se mide cuántas entradas reconoce antes y después | Cerrado |
| B-02 | Que un número inventado apague el aviso | Alto | Se comprueba contra el registro | Cerrado |
| B-03 | Que tocar el estándar rompa algo | Alto | Las dos baterías completas | Cerrado |

---

## 11. Definition of Done

- [x] Los tres CA verificados con evidencia
- [x] Medido cuántas entradas reconoce el lector, antes y después
- [x] El cambio al estándar, versionado y registrado
- [x] Las dos baterías en verde
- [x] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
