# Plan de Trabajo · Fase C-EP-001-HU-036-liste-y-ok-entran-a-la-lista (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba acepta el alcance y el costo. El requisito vive en la HU, el detalle de las pruebas en el `plan_pruebas` de la misma fase, y lo que quedó hecho en el `funcionalidad_implementada.md` del cierre.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-001-HU-036-liste-y-ok-entran-a-la-lista` |
| **Épica** | [EP-001 Cuerpo de reglas heredable](../../epica.md) |
| **HU** | [HU-036 El pedido dice qué se espera](../HU-036-el-pedido-dice-que-se-espera.md), una sola (`F12.1`) |
| **Módulo** | Cuerpo de reglas, capítulo `01 · Conducta del agente` |
| **Especificación del módulo** | La propia HU y el anexo [palabras-clave.md](../../../../../base/01-conducta/palabras-clave.md) |
| **Fecha apertura** | 2026-10-06 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | El usuario, el 2026-10-06, con la versión 56.2.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): amplía la [fase A](../A-EP-001-HU-036-la-palabra-clave-que-dice-que-hacer/README.md), que creó la lista de `01·C28`, y sigue a la [fase B](../B-EP-001-HU-036-respondo-contesta-la-pregunta/plan_trabajo.md), que le sumó «Respondo». Le suma dos palabras más y saca una fila que nunca funcionó.
- **La fase se abre con el cambio ya hecho y subido.** El usuario editó el anexo durante la sesión del 2026-08-31 y pidió versionarlo; el commit `634b28a` quedó en `origin/main` antes de que esta fase existiera. El 2026-10-06 decidió que el cambio sí lleva su cadena, así que esta fase **retro-documenta** lo hecho y agrega las pruebas que faltaron. Queda dicho acá para que nadie lea el orden al revés.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-036` que cierra esta fase | Estado |
|---|---|
| [CA-02](../HU-036-el-pedido-dice-que-se-espera.md#ca-02--con-palabra-clave-se-hace-eso-y-solo-eso) | ☐ |
| [CA-03](../HU-036-el-pedido-dice-que-se-espera.md#ca-03--la-palabra-que-no-esta-en-la-lista-se-trata-como-ausente) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** dejar comprobado por programa que `Liste` y `OK` se reconocen, que `OK` no autoriza ninguna acción, y que la forma que salió del anexo ya no figura como palabra.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| [CA-02](../HU-036-el-pedido-dice-que-se-espera.md#ca-02--con-palabra-clave-se-hace-eso-y-solo-eso) | El usuario abre con «Liste» o con «OK»: el enganche las reconoce y no manda el aviso de `01·C28` | Funcional | Baja |
| [CA-03](../HU-036-el-pedido-dice-que-se-espera.md#ca-03--la-palabra-que-no-esta-en-la-lista-se-trata-como-ausente) | «¿La pregunta que se haga?» ya no está en la lista, y una pregunta entre signos se trata como mensaje sin palabra | Funcional | Baja |

**Fuera de alcance:**

- **Que la pregunta escrita entre `¿` y `?` cuente como «Pregunta».** Se estudió en la sesión del 2026-08-31 y el usuario lo descartó. Pide tocar `_FRASE` y los tres métodos que la usan en `recuperar.py`, y no entra acá.
- Cambiar el código del enganche: lee la lista del anexo, y las filas nuevas bastan, igual que en la fase B.
- Sumar `Liste` u `OK` a `base/tareas.md`: ninguna de las dos pide tarea propia.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`RecuperadorDeReglas.palabras_de_la_lista` y `palabra_clave`, en `proyectos/cimiento/core/herramientas/recuperar.py`, toman toda fila de tabla de `palabras-clave.md` con la palabra en negrita, y `palabras_de_inicio` baja el mensaje a minúsculas sin tildes. La tabla «Ninguna de estas toca nada» tiene hoy diez filas, con `Liste` y `OK` al final.

**La fila que salió.** El anexo traía una fila cuya palabra era «¿La pregunta que se haga?». `_FILA_PALABRA` la leía como una palabra literal de veinticuatro caracteres, así que no coincidía con ningún mensaje y aparecía igual en el aviso que lista las palabras válidas. Verificado leyendo el aviso real que el enganche mandó el 2026-10-06.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `base/01-conducta/palabras-clave.md` | Modificar | Regla | Hecho en `634b28a`: filas `Liste` y `OK`, y sale la fila de la pregunta entre signos |
| `base/01-conducta.md` | Modificar | Regla | Hecho en `634b28a`: el sello de `C28` deja de contar las palabras |
| `CHANGELOG.md`, `VERSION` | Modificar | Versión | Hecho en `634b28a`: MENOR, 56.2.0 |
| `proyectos/cimiento/core/herramientas/tests_liste_y_ok.py` | Nuevo | Test | Falta: lo escribe esta fase |
| `documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-036-el-pedido-dice-que-se-espera/README.md` | Modificar | Documentación | Fila de la fase C |
| `documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-036-el-pedido-dice-que-se-espera/HU-036-el-pedido-dice-que-se-espera.md` | Modificar | Documentación | Fila en «Fases que la implementan» y línea de bitácora |

### 2.2 Matriz de dependencias del refactor

No aplica: no cambia contratos de código.

### 2.3 Rutas / endpoints y control de acceso

No aplica.

### 2.4 Punto de entrada en la UI

No aplica: las palabras se escriben en el chat.

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| `Liste` y `OK` van en la tabla de las que no tocan nada | Una tabla aparte para el acuse de recibo | Ninguna de las dos cambia el proyecto, que es lo que agrupa esa tabla | Edición del usuario, 2026-10-06 |
| `OK` no autoriza ninguna acción | Que valga como «Continúe» | Acusar recibo no es pedir que se siga; si valiera, el agente seguiría sin que nadie lo pidiera | Sesión del 2026-08-31 |
| La fila de la pregunta entre signos sale en vez de arreglarse | Dejarla y enseñarle la forma al programa | La forma entre signos se descartó; una fila que no coincide con nada ensucia el aviso | Sesión del 2026-08-31 |
| El sello de `C28` deja de decir cuántas palabras hay | Actualizar el número cada vez | El número se desactualiza con cada palabra nueva, y ya había quedado viejo dos veces | Sesión del 2026-08-31 |
| Fase nueva de EP-001·HU-036 | Una HU nueva, o ninguna fase | Es la HU dueña de la lista, y la fase B ya sentó el precedente | Decisión del usuario, 2026-10-06 |

### 2.7 Dudas por resolver antes de codificar

**Una, y es de redacción.** La celda de `OK` dice «Se entiende la explicación», que describe al usuario y no lo que queda autorizado. Las otras nueve de esa tabla dicen un verbo. Se propone «nada, es acuse de recibo», y se decide al aprobar este plan.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

No aplica: la fase no agrega acciones.

## 3. Desglose de tareas por criterio de aceptación

### [CA-02](../HU-036-el-pedido-dice-que-se-espera.md#ca-02--con-palabra-clave-se-hace-eso-y-solo-eso) · `Liste` y `OK` se reconocen, y `OK` no autoriza nada

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Escribir las pruebas del reconocimiento de las dos palabras | Test | 0,5 h | — | EV-01 |
| T-02 | Dejar la celda de `OK` diciendo qué autoriza, si el plan lo aprueba | Regla | 0,25 h | — | |

### [CA-03](../HU-036-el-pedido-dice-que-se-espera.md#ca-03--la-palabra-que-no-esta-en-la-lista-se-trata-como-ausente) · La forma que salió se trata como ausente

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-03 | Probar que la forma de la pregunta entre signos no está en la lista y que un mensaje así no trae palabra | Test | 0,25 h | T-01 | EV-01 |

### RNF · Requisitos no funcionales

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-04 | Índices de la HU al día: su README y la tabla de fases | Documentación | 0,25 h | — | |

**Total estimado:** 1,25 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-03.
**Paralelizables:** T-02 y T-04 con T-03.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| [CA-02](../HU-036-el-pedido-dice-que-se-espera.md#ca-02--con-palabra-clave-se-hace-eso-y-solo-eso) | Pruebas automáticas | EV-01 | | ☐ |
| [CA-03](../HU-036-el-pedido-dice-que-se-espera.md#ca-03--la-palabra-que-no-esta-en-la-lista-se-trata-como-ausente) | Pruebas automáticas | EV-01 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Reporte de pruebas | `resultado_pruebas.md` |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | Local, `.venv` de Cimiento |
| Usuarios de prueba | Ninguno |
| Datos precargados | El anexo real `base/01-conducta/palabras-clave.md` |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit `634b28a` y publicar una versión de corrección. Nada de lo que toca la fase borra información.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Aditivo: los proyectos que heredan reciben las dos palabras al actualizar, y no tienen que hacer nada (MENOR, `20·M10`). La fila que salió no obliga a nada, porque nunca funcionó: ningún mensaje la pudo haber usado.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: `01·C28`, `00·N1`, `01·C24`, `20·M10`, `20·M17`, [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F25`](../../../../../base/02-flujo-de-trabajo/reglas/F25-autorizar-el-arranque-no-aprueba-el-plan.md).

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | `OK` leído como permiso para seguir | El agente continúa sin que nadie lo pida | La celda dice que no autoriza acción; T-02 la deja explícita | Abierto |
| B-02 | La fase documenta algo ya subido | El orden de la cadena se lee al revés | Declarado en el ORIGEN, con el número del commit | Cerrado |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] Pruebas de la fase en verde, solo las suites que la fase toca ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md))
- [ ] Trazabilidad de la especificación a la implementación sin faltantes ([`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))
- [ ] Documentación e índices actualizados (`13`)
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** sin ejecutar todavía.
