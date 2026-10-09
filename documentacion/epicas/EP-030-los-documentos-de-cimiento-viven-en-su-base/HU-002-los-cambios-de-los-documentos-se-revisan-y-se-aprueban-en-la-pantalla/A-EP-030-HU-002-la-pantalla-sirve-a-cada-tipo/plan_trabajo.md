# Plan de Trabajo · Fase A-EP-030-HU-002-la-pantalla-sirve-a-cada-tipo (módulo Estándar de Cimiento)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-030-HU-002-la-pantalla-sirve-a-cada-tipo` |
| **Épica** | `EP-030` |
| **HU** | [`HU-002`](../HU-002-los-cambios-de-los-documentos-se-revisan-y-se-aprueban-en-la-pantalla.md), una sola (`F12.1`) |
| **Módulo** | Estándar de Cimiento, `proyectos/cimiento/core/estandar/` |
| **Especificación del módulo** | La HU-002 y la [épica EP-030](../../epica.md) |
| **Fecha apertura** | 2026-10-09 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 142](../../../../../historico-chat/resumenes/2026-10-08/pendientes/142-los-documentos-de-cimiento-viven-en-la-base/analisis-1.md), el 2026-10-08, en el turno 49, con la versión 56.8.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Fase nueva. Sale del análisis 1 del pendiente 142, acuerdo 5, punto 2 de «Lo que se tiene que hacer».

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-002` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-002-los-cambios-de-los-documentos-se-revisan-y-se-aprueban-en-la-pantalla.md#ca-01--la-pantalla-muestra-lo-que-cambió) | ☑ |
| [CA-02](../HU-002-los-cambios-de-los-documentos-se-revisan-y-se-aprueban-en-la-pantalla.md#ca-02--se-aprueba-con-un-botón) | ☑ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que la pantalla «Estándar → Propuestas» muestre el antes y el después y apruebe cualquier tipo de documento registrado en el camino único, sin código aparte por tipo.

**Fuera de alcance:** los tipos nuevos y sus tablas (HU-003 en adelante); el botón de git, que ya hizo la EP-026·HU-007.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

La pantalla ya existe (EP-026·HU-005 y EP-028·HU-004): lista las propuestas, muestra lo que cambia línea por línea con `que_cambia` y las aprueba o rechaza con un botón, guardando `resuelta_por` y `resuelta`. El botón de git es de la EP-026·HU-007, terminada. Lo que ata la pantalla a dos tipos son `cambios.aplicar` y `cambios.actual_de`, que preguntan `objeto == DOCUMENTO` a mano.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/estandar/documentos.py` | Modificar | Lógica | Cada tipo sabe dar su texto actual y aplicar una propuesta |
| `proyectos/cimiento/core/estandar/cambios.py` | Modificar | Lógica | `aplicar` y `actual_de` le preguntan al tipo |
| `proyectos/cimiento/core/estandar/tests_revision.py` | Crear | Test | |

### 2.2 Matriz de dependencias del refactor

| Lo que cambia | Quién lo usa |
|---|---|
| `cambios.aplicar`, `cambios.actual_de` | La pantalla de propuestas, `que_cambia`, las vistas de documento y recuerdo; la firma no cambia |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

Las de hoy: `estandar/propuestas/`, `…/aprobar/` y `…/rechazar/`, con el permiso que ya tienen.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

Cimiento → Estándar → Propuestas.

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Se reusa la pantalla de propuestas | Una pantalla nueva | Ya muestra el antes y el después y aprueba con un botón | Propuesta del agente |
| El tipo aplica su propia propuesta | Un `if` por tipo en `cambios.py` | Cada tipo nuevo se registra y la pantalla lo sirve sola | Acuerdo 2 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

No aplica: aprobar y rechazar ya existen.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Cada tipo da su texto actual y aplica la propuesta | Lógica | 0,5 h | — | EV-01 |
| T-02 | `aplicar` y `actual_de` le preguntan al tipo | Lógica | 0,5 h | T-01 | EV-01 |
| T-03 | Pruebas | Test | 1 h | T-01, T-02 | EV-01 |

**Total estimado:** 2 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Pruebas de Django | EV-01 | 2026-10-09 | ☑ |
| CA-02 | Pruebas de Django | EV-01 | 2026-10-09 | ☑ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django |
| Usuarios de prueba | Una cuenta administradora creada por la prueba |
| Datos precargados | Un documento del estándar, un proyecto y un recuerdo |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

No aplica: no cambia la base.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `08·T1`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | La base de prueba compartida falla si otra sesión corre pruebas a la vez | No se pueden verificar los CA | Se repite cuando la base está libre | Abierto |

## 11. Definition of Done

- [x] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [x] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno todavía.
