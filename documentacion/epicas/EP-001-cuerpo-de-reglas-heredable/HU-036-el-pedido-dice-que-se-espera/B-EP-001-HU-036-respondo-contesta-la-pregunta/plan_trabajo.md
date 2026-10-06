# Plan de Trabajo · Fase B-EP-001-HU-036-respondo-contesta-la-pregunta (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba acepta el alcance y el costo. El requisito vive en la HU, el detalle de las pruebas en el `plan_pruebas` de la misma fase, y lo que quedó hecho en el `funcionalidad_implementada.md` del cierre.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-001-HU-036-respondo-contesta-la-pregunta` |
| **Épica** | [EP-001 Cuerpo de reglas heredable](../../epica.md) |
| **HU** | [HU-036 El pedido dice qué se espera](../HU-036-el-pedido-dice-que-se-espera.md), una sola (`F12.1`) |
| **Módulo** | Cuerpo de reglas, capítulo `01 · Conducta del agente` |
| **Especificación del módulo** | La propia HU y el anexo [palabras-clave.md](../../../../../base/01-conducta/palabras-clave.md) |
| **Fecha apertura** | 2026-10-06 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [análisis 1 del pendiente 131](../../../../../historico-chat/resumenes/2026-10-06/pendientes/131-responder-una-pregunta-no-tiene-palabra-clave/analisis-1.md), el 2026-10-06, con la versión 55.6.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): amplía la [fase A](../A-EP-001-HU-036-la-palabra-clave-que-dice-que-hacer/README.md), que creó la lista de `01·C28`. Le suma la palabra para contestar una pregunta del agente, que la lista no tenía. Sale del [análisis 1 del pendiente 131](../../../../../historico-chat/resumenes/2026-10-06/pendientes/131-responder-una-pregunta-no-tiene-palabra-clave/analisis-1.md).

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-036` que cierra esta fase | Estado |
|---|---|
| [CA-02](../HU-036-el-pedido-dice-que-se-espera.md#ca-02--con-palabra-clave-se-hace-eso-y-solo-eso) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** ejecutar y verificar los CA de la sección 0 hasta dejarlos cumplidos, con su evidencia en la sección 5.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| [CA-02](../HU-036-el-pedido-dice-que-se-espera.md#ca-02--con-palabra-clave-se-hace-eso-y-solo-eso) | El usuario abre con «Respondo»: el enganche la reconoce, no manda el aviso de `01·C28` y no le asigna tarea propia | Funcional | Baja |

**Fuera de alcance:**

- Cambiar el código del enganche: lee la lista del anexo y la fila nueva basta (análisis 1, «Lo que aportó cada parte»).
- Sumar «Respondo» a `base/tareas.md`: no pide tarea propia (acuerdo 2).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`RecuperadorDeReglas.palabras_de_la_lista` y `palabra_clave`, en `proyectos/cimiento/core/herramientas/recuperar.py`, toman toda fila de tabla de `palabras-clave.md` con la palabra en negrita. La tabla «Estas mandan sobre el trabajo mismo» tiene hoy Apruebo, Continúe y Pare. «Respondo» no aparece en ningún otro archivo de `base/`.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `base/01-conducta/palabras-clave.md` | Modificar | Regla | Fila «Respondo» |
| `proyectos/cimiento/core/herramientas/tests_respondo.py` | Nuevo | Test | |
| `CHANGELOG.md`, `VERSION` | Modificar | Versión | MENOR, 56.1.0 |
| `documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-036-el-pedido-dice-que-se-espera/README.md` | Modificar | Documentación | Fila de la fase B |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

No aplica: no cambia contratos de código.

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

No aplica: la palabra se escribe en el chat.

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| «Respondo» va en la tabla de las que mandan sobre el trabajo | Una tabla aparte | Contesta lo que el trabajo en curso preguntó | Análisis 1, acuerdo 1 |
| No pide tarea propia | Darle una tarea en `base/tareas.md` | Las reglas de lo que se haga llegan con la acción | Análisis 1, acuerdo 2 |
| Fase nueva de EP-001·HU-036 | Una HU nueva | Es la HU que creó la lista | Análisis 1, acuerdo 3 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

No aplica: la fase no agrega acciones.

## 3. Desglose de tareas por criterio de aceptación

### [CA-02](../HU-036-el-pedido-dice-que-se-espera.md#ca-02--con-palabra-clave-se-hace-eso-y-solo-eso) · «Respondo» contesta la pregunta y nada más

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Sumar la fila «Respondo» a la tabla de las que mandan sobre el trabajo | Regla | 0,25 h | — | |
| T-02 | Escribir las pruebas del reconocimiento | Test | 0,5 h | T-01 | EV-01 |
| T-03 | CHANGELOG y versión 56.1.0 | Versión | 0,25 h | T-01 | |

**Total estimado:** 1 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02.
**Paralelizables:** T-03 con T-02.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| [CA-02](../HU-036-el-pedido-dice-que-se-espera.md#ca-02--con-palabra-clave-se-hace-eso-y-solo-eso) | Pruebas automáticas | EV-01 | | ☐ |

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

Revertir el commit de la fase.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Aditivo: los proyectos que heredan reciben la palabra al actualizar; no tienen que hacer nada (MENOR, `20·M10`).

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: `01·C28`, `00·N1`, `01·C24`, `20·M10`, [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md).

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | «Respondo» leído como permiso amplio | El agente hace más de lo preguntado | El alcance de la fila dice «nada más» | Cerrado |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] Pruebas de la fase en verde, solo las suites que la fase toca ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md))
- [ ] Trazabilidad de la especificación a la implementación sin faltantes ([`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))
- [ ] Documentación e índices actualizados (`13`)
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno.
