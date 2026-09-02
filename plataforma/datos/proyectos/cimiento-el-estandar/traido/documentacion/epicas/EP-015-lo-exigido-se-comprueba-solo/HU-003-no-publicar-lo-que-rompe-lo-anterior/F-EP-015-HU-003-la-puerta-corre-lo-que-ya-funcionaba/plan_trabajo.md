# Plan de Trabajo — Fase `F-EP-015-HU-003-la-puerta-corre-lo-que-ya-funcionaba` (módulo Comprobaciones)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación. El requisito vive en la HU; las pruebas, en el `plan_pruebas`; lo que quedó hecho, en el `funcionalidad_implementada.md`.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `F-EP-015-HU-003-la-puerta-corre-lo-que-ya-funcionaba` |
| **Épica** | [EP-015](../../epica.md) |
| **HU** | [HU-003 No publicar lo que rompe lo anterior](../HU-003-no-publicar-lo-que-rompe-lo-anterior.md) — **una sola** (`F12.1`) |
| **Módulo** | Comprobaciones |
| **Especificación del módulo** | [documentacion/comprobaciones/spec.md](../../../../comprobaciones/spec.md) |
| **Fecha apertura** | 2026-09-01 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN:**

- ✨ **Funcionalidad nueva:** `F-022`. **Cierra la vuelta de la columna**: `F-008`, publicar una versión, esperaba esta puerta.

> **El usuario autorizó ejecutar sin aprobar paso por paso** el 2026-09-01.

**CA de la HU que cubre esta fase:** los cuatro, todos ☑.

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** que antes de publicar se vuelva a correr todo lo que ya funcionaba, y que una versión que rompió algo no salga.

**Publicar es la única acción de la plataforma que no se puede deshacer del lado de quien recibe.** Retirar una versión rota no le devuelve a nadie el día que perdió.

**Qué es «lo que ya funcionaba»:** las comprobaciones del estándar y la suite del proyecto, enteras. No una lista escrita a mano de lo que alguien se acuerda.

**Fuera de alcance:** publicar. Esta fase es la puerta, no el acto.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo que ya existe y se junta:**

| Pieza | Qué aporta |
|---|---|
| `comprobaciones/core.py` | El veredicto de las comprobaciones |
| `comprobaciones/estado.py` | Qué funcionalidades quedaron en «no cumple» |
| `validadores/validar.py suite` | La suite del proyecto |

**Lo verificado el 2026-09-01:**

| Qué se comprobó | Resultado |
|---|---|
| Cuánto tardan las comprobaciones | ~117 s |
| Subcomando que corre la suite de un proyecto | `suite --raiz` |
| **Subcomando que NO acepta `--raiz`** | `internas`, que corre las del estándar donde vive |

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/comprobaciones/puerta.py` | Nuevo | Servicio | La puerta |
| `plataforma/nucleo/comprobaciones/management/commands/puerta_de_publicacion.py` | Nuevo | Orden | Pedirla |
| `plataforma/nucleo/comprobaciones/tests_puerta.py` | Nuevo | Prueba | Los cuatro CA |
| `documentacion/comprobaciones/spec.md` | Modificar | Especificación | Su §13, para nombrar la fase |

**Ninguna entidad y ninguna migración.**

### 2.2 Matriz de dependencias del refactor

Ni `core.py` ni `estado.py` se tocan: la puerta los usa.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **«Lo que ya funcionaba» es todo, no una lista** | Una lista de lo que hay que revisar | Una lista escrita a mano se queda corta justo en lo que nadie se acordó |
| **Un «no se pudo» no pasa** | Tratarlo como que pasó | Es la forma más silenciosa de publicar a ciegas |
| **Lo sin verificar se declara y no detiene** | Detener también con eso | Que algo no tenga prueba no quiere decir que esta versión lo rompió. Detener con eso vuelve la puerta inútil |
| **Lo que está en «no cumple» detiene** | Solo declararlo | Publicar sabiendo qué queda mal es una decisión; hacerlo sin la puerta es un accidente |
| **Una sola orden** | Varios pasos | Si pasar la puerta cuesta trabajo manual, se va a saltar |
| **Se corre la suite del proyecto**, no la del estándar | Correr `internas` | `internas` corre las pruebas del estándar donde el estándar vive, y no acepta que se le apunte a otro proyecto |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | Juntar el veredicto y el estado en una puerta | Servicio | 2 h | — | CA-01, CA-02 | EV-01 |
| T-02 | Correr la suite del proyecto | Servicio | 1 h | T-01 | CA-01 | EV-01 |
| T-03 | Que un «no se pudo» no pase | Servicio | 1 h | T-02 | CA-04 | EV-01 |
| T-04 | La orden de consola, con el tiempo | Orden | 1 h | T-03 | CA-03 | EV-02 |
| T-05 | Las pruebas de los cuatro CA | Test | 2 h | T-04 | Todos | EV-01 |
| T-06 | **Correr la puerta sobre este repositorio** | Medición | 1 h | T-04 | CA-03 | EV-02 |

**Total estimado:** 8 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-04 → T-06.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Con cada rojo por separado | EV-01 | 2026-09-01 | ☑ |
| CA-02 | Con una funcionalidad en «no cumple» | EV-01 | 2026-09-01 | ☑ |
| CA-03 | Sobre este repositorio, con el tiempo | EV-02 | 2026-09-01 | ☑ |
| CA-04 | Con un proyecto que no existe, y con las baterías sin correr | EV-01, EV-02 | 2026-09-01 | ☑ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas de la puerta | `plataforma/nucleo/comprobaciones/tests_puerta.py` |
| EV-02 | La puerta sobre este repositorio | `resultado_pruebas.md` §1 |

---

## 6. Datos y ambiente de prueba

Veredictos armados a mano para los casos de partición, y este repositorio para la corrida entera. Solo se lee.

---

## 7. Reversión / rollback  ·  Q11

Nada que revertir: no escribe.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Ninguna migración, ninguna dependencia nueva.

---

## 9. Reglas aplicadas  ·  Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F19`](../../../../../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md), [`09`](../../../../../base/09-git.md) por la puerta de publicación.
- Producto: las `RN-1` a `RN-5` de la historia.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | **Que dé un rojo falso** | **Alto — enseña a ignorar la puerta** | Se corre sobre este repositorio, que está en verde, y tiene que pasar | Abierto hasta T-06 |
| B-02 | Que un «no se pudo» pase | Alto | La puerta no pasa sin veredicto ni sin baterías corridas | Cerrado por diseño |
| B-03 | Que tarde tanto que se salte | Medio | El tiempo queda escrito | Abierto hasta T-06 |

---

## 11. Definition of Done

- [x] Los cuatro CA verificados con evidencia
- [x] La puerta corrida sobre este repositorio, **con el tiempo medido**
- [x] Comprobado que un «no se pudo» no pasa
- [x] Las dos baterías en verde
- [x] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
