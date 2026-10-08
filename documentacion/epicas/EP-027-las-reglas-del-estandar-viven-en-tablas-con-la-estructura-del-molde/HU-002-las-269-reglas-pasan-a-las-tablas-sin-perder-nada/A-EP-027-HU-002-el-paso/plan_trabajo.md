# Plan de Trabajo · Fase A-EP-027-HU-002-el-paso (módulo Estándar en la base)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-027-HU-002-el-paso` |
| **Épica** | `EP-027` |
| **HU** | [`HU-002`](../HU-002-las-269-reglas-pasan-a-las-tablas-sin-perder-nada.md), una sola (`F12.1`) |
| **Módulo** | Estándar en la base: `core/estandar/` |
| **Especificación del módulo** | La HU-002 |
| **Fecha apertura** | 2026-10-07 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 136](../../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md), el 2026-10-07, con la versión 57.3.0; el usuario pidió terminar la épica («continúe termine todo», 2026-10-07) |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): `A-EP-027-HU-001-las-casillas`, que dejó las tablas vacías. Sale del acuerdo 1 del análisis 1 del pendiente 136.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-002` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-002-las-269-reglas-pasan-a-las-tablas-sin-perder-nada.md#ca-01--todas-las-reglas-quedan-en-las-tablas) | ☐ |
| [CA-02](../HU-002-las-269-reglas-pasan-a-las-tablas-sin-perder-nada.md#ca-02--nada-se-pierde) | ☐ |
| [CA-03](../HU-002-las-269-reglas-pasan-a-las-tablas-sin-perder-nada.md#ca-03--pasar-dos-veces-no-duplica) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** pasar todas las reglas de la base a sus tablas, mover las notas con fecha del sello a la historia y armar el texto de cada documento desde las tablas.

**Fuera de alcance:** que los cambios siguientes pasen por las tablas (HU-003); las reglas de cada proyecto (HU-006).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`molde.py` (HU-001) lee y arma cada regla. Las 156 notas con fecha están todas en el sello, que el agente no recibe (`MapaDeTareas.cuerpo` corta antes del sello). `validadores/reglas-validables.md` tiene tres secciones: «Ya son validadores» (tabla con la regla y su validador), «Validables, faltan» (tablas cuya primera columna es la regla) y «No validables» (listas por capítulo). La historia registra sola cada fila que se guarda en la app `estandar` (`core/historia/registro.py`), y `quien_y_por_que` agrupa todo en una versión.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/estandar/reglas.py` | Crear | Lógica | Pasar un documento a las tablas, leer «validable», mover las notas y armar el texto |
| `proyectos/cimiento/core/estandar/management/commands/pasar_reglas.py` | Crear | Comando | Pasa todo el estándar en una versión |
| `proyectos/cimiento/core/estandar/tests_pasar_reglas.py` | Crear | Test | |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| El texto de los documentos (sin las notas del sello) | Los enganches, el freno, `ver_estandar` | `core.estandar`, `core.enganches` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

Ninguna.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

Ninguno: `manage.py pasar_reglas`. Las notas se ven en «Historia».

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| La nota con fecha es un cambio de la historia de su regla, con su fecha y su texto como motivo | Una tabla aparte de notas | La historia ya es donde se cuenta cuándo y por qué cambió algo | Acuerdo 1 |
| Solo salen del sello los párrafos que abren con negrita y una fecha | Buscar fechas en todo el texto | El cuerpo también cita fechas, y eso sí es la regla | RN-06 |
| «Validable» se lee con prioridad: primero «Ya son validadores», después «Validables, faltan», después «No validables» | Tomar la primera mención | El registro nombra reglas de otra lista en su prosa («F8 salió de esta lista») | RN-05 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

| Acción | Contraria |
|---|---|
| `pasar_reglas` | «Deshacer» en la historia devuelve el texto de cada documento; las filas se quitan con `migrate estandar 0004` |

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `reglas.py` y el comando | Lógica | 2 h | Ninguna | EV-01 |
| T-02 | Pruebas | Test | 1 h | T-01 | EV-01 |
| T-03 | Pasar la base viva y comprobar | Datos | 0,5 h | T-02 | EV-02 |

**Total estimado:** 3,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Prueba de Django | EV-01 | | ☐ |
| CA-02 | Prueba de Django | EV-01 | | ☐ |
| CA-03 | Prueba de Django | EV-01 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |
| EV-02 | Salida de `pasar_reglas` en la base viva | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django, con el estándar importado de `base/`; después, la base viva |
| Usuarios de prueba | Ninguno |
| Datos precargados | El estándar |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

«Deshacer» la versión en la historia devuelve el texto de los documentos; `migrate estandar 0004` quita las tablas.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

La base viva es la de producción: se hace la copia del día antes de pasar (`00·N7`), y el paso es una sola transacción.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `00·N7`, `20·M7`, `20·M9`, `20·M10`, `20·M11`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Ninguno | | | |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno todavía.
