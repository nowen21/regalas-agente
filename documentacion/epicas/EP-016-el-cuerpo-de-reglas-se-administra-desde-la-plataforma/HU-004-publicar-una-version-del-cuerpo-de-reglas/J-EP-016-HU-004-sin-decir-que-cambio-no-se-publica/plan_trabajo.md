# Plan de Trabajo — Fase `J-EP-016-HU-004-sin-decir-que-cambio-no-se-publica` (módulo Reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación. El requisito vive en la HU; las pruebas, en el `plan_pruebas`; lo que quedó hecho, en el `funcionalidad_implementada.md`.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `J-EP-016-HU-004-sin-decir-que-cambio-no-se-publica` |
| **Épica** | [EP-016](../../epica.md) |
| **HU** | [HU-004 Publicar una versión del cuerpo de reglas](../HU-004-publicar-una-version-del-cuerpo-de-reglas.md): **una sola** (`F12.1`) |
| **Módulo** | Reglas |
| **Especificación del módulo** | [documentacion/reglas/spec.md](../../../../reglas/spec.md) |
| **Fecha apertura** | 2026-09-01 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN:**

- ✨ **Funcionalidad nueva:** `F-008`. **Es la que cerraba la vuelta de la columna**: esperaba a `F-022`, que ya está.

> **El usuario autorizó ejecutar sin aprobar paso por paso** el 2026-09-01.

**CA de la HU que cubre esta fase:** los tres, todos ☑.

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** que una versión se publique solo cuando esté dicho qué cambió y nada se haya roto.

**La puerta ya existe**, y esta fase la usa. Lo que agrega es lo que la puerta no mira: que el número esté libre y que el registro diga qué cambió.

**Fuera de alcance:** escribir la entrada del registro. Es prosa, y la escribe una persona.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo que ya existe y se reutiliza:**

| Pieza | Qué aporta |
|---|---|
| `comprobaciones/puerta.py` | La puerta de `F-022` |
| `reglas/desfase.py` | Si un número ya se publicó |

**Lo verificado el 2026-09-01:**

| Qué se comprobó | Resultado |
|---|---|
| Entradas del registro | **197** |
| El tipo va en la entrada como `MAYOR`, `MENOR` o `PARCHE` | Sí, **en cualquiera de los dos órdenes** |
| Dónde vive el número publicado | El archivo `VERSION` |

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/reglas/publicacion.py` | Nuevo | Servicio | La revisión y la publicación |
| `plataforma/nucleo/reglas/management/commands/publicar_version.py` | Nuevo | Orden | Pedirla |
| `plataforma/nucleo/reglas/tests_publicacion.py` | Nuevo | Prueba | Los tres CA |
| `documentacion/reglas/spec.md` | Modificar | Especificación | Su §13, para nombrar la fase |

**Ninguna entidad y ninguna migración.**

### 2.2 Matriz de dependencias del refactor

Ni la puerta ni el desfase se tocan: esta fase los usa.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **La plataforma no escribe la entrada del registro** | Generarla | Es prosa: dice qué pasó y por qué importa. Generada, diría lo mismo siempre |
| **Sin entrada no se publica** | Publicar y avisar | Quien adopte no podría saber si le toca rehacer algo |
| **Una entrada sin tipo tampoco pasa** | Suponer PARCHE | Suponer el tipo es decidir por el que adopta |
| **Lo que falta se dice todo junto** | De a uno | De a uno obliga a intentar tres veces |
| **La revisión se puede pedir sin publicar** | Solo publicar | Sirve para saber qué falta antes de decidir |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | Encontrar la entrada del registro de una versión | Servicio | 2 h | — | CA-02 | EV-01 |
| T-02 | Leer su tipo, en los dos órdenes | Servicio | 1 h | T-01 | CA-02 | EV-01 |
| T-03 | Comprobar que el número esté libre | Servicio | 1 h | — | CA-01 | EV-01 |
| T-04 | Pedir la puerta | Servicio | 1 h | — | CA-03 | EV-01 |
| T-05 | Juntar todo lo que falte | Servicio | 1 h | T-02, T-03, T-04 | Todos | EV-01 |
| T-06 | Escribir la versión, solo si no falta nada | Servicio | 1 h | T-05 | CA-01 | EV-01 |
| T-07 | La orden de consola | Orden | 1 h | T-06 | Todos | EV-02 |
| T-08 | Las pruebas de los tres CA | Test | 2 h | T-07 | Todos | EV-01 |

**Total estimado:** 10 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-05 → T-06 → T-07. T-03 y T-04 van en paralelo.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Con un registro de prueba y todo en verde | EV-01 | 2026-09-01 | ☑ |
| CA-02 | Con un número sin entrada, y con una entrada sin tipo | EV-01 | 2026-09-01 | ☑ |
| CA-03 | Con la puerta en rojo | EV-01 | 2026-09-01 | ☑ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas de la publicación | `plataforma/nucleo/reglas/tests_publicacion.py` |
| EV-02 | La orden, corrida sobre el registro real | `resultado_pruebas.md` §3 |

---

## 6. Datos y ambiente de prueba

Un registro de cambios de mentiras, con las dos formas de escribir una entrada y una sin tipo. **La puerta se simula**: correrla de verdad tarda dos minutos por prueba.

---

## 7. Reversión / rollback  ·  Q11

Publicar escribe un número en un archivo versionado. **Lo que no se deshace es lo que otro ya adoptó**, y por eso la puerta va antes.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Ninguna migración, ninguna dependencia nueva.

---

## 9. Reglas aplicadas  ·  Q13

- Base: [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md), que es la que manda acá.
- Producto: las `RN-1` a `RN-4` de la historia.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | **Publicar dos veces el mismo número** | **Alto: no se deshace** | Se comprueba contra el registro | Cerrado |
| B-02 | Publicar sin decir qué cambió | Alto | Sin entrada no se publica | Cerrado |
| B-03 | Que la puerta tarde tanto que se pruebe poco | Medio | En las pruebas se simula; en la orden se corre de verdad | Cerrado |

---

## 11. Definition of Done

- [x] Los tres CA verificados con evidencia
- [x] Comprobado que sin entrada no se publica
- [x] Comprobado que el archivo de versión no cambia si algo falta
- [x] Las dos baterías en verde
- [x] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
