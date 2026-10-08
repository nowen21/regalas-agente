# Plan de Trabajo · Fase C-EP-027-HU-006-el-agente-las-recibe (módulo Enganches)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-027-HU-006-el-agente-las-recibe` |
| **Épica** | `EP-027` |
| **HU** | [`HU-006`](../HU-006-las-reglas-de-cada-proyecto-viven-en-la-misma-tabla.md), una sola (`F12.1`) |
| **Módulo** | Enganches: `core/enganches/` y su adaptador de arranque (`adaptadores/claude-code/hook_sesion.py`) |
| **Especificación del módulo** | La HU-006, RN-06 y RN-07 |
| **Fecha apertura** | 2026-10-07 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 136](../../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md) y el usuario, que aprobó el alcance de la HU-006, el 2026-10-07, con la versión 57.4.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): la que hizo el índice de la memoria desde la base (EP-026·HU-005) y la que hizo lo que autorizan las reglas (análisis 1 del pendiente 103). Depende de `B-EP-027-HU-006-reglas-en-la-tabla`.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-006` que cierra esta fase | Estado |
|---|---|
| [CA-03](../HU-006-las-reglas-de-cada-proyecto-viven-en-la-misma-tabla.md#ca-03--el-agente-del-proyecto-las-recibe-de-la-base) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que al abrir la sesión de un proyecto registrado llegue el índice de sus reglas, con el comando para leer cada una, y que el freno deje escribir lo que esas reglas autorizan, leído de la tabla.

**Fuera de alcance:** el catálogo (fase D), la plantilla y el paso de los proyectos (fase E).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`hook_sesion._del_proyecto` arma la memoria y el índice del histórico dentro del tope de 10.000 caracteres. `Recuerdos.desde_la_base` consulta la base sin Django con `NivelesDelProyecto(...).consultar`, buscando el proyecto por su ruta. `Autorizaciones.del_proyecto` lee `.agente/reglas-proyecto.md` y reconoce solo códigos `P<n>`: las reglas `RP<n>` de RNI quedan sin nombre.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/enganches/reglas_del_proyecto.py` | Crear | Lógica | El índice y lo que autorizan, desde la base, sin Django |
| `proyectos/cimiento/core/enganches/autorizado.py` | Modificar | Lógica | `del_proyecto` lee la tabla si el proyecto tiene reglas en ella |
| `adaptadores/claude-code/hook_sesion.py` | Modificar | Enganche | El índice de las reglas del proyecto entra al arranque |
| `proyectos/cimiento/core/enganches/tests_reglas_del_proyecto.py` | Crear | Test | |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| `Autorizaciones.del_proyecto` | El freno, el pre-commit | `core.enganches` |
| El arranque | Toda sesión de un proyecto | `core.enganches` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

Ninguna.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

Ninguno: el arranque de la sesión.

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Llega el índice, y cada regla se lee con `ver_regla` | Inyectar todas las reglas | Las de AgroSystem ocupan 105.000 caracteres y el arranque tiene 10.000; es como llega la memoria | RN-06 |
| Si el proyecto no tiene reglas en la tabla, el freno sigue con el archivo | Dejar de leer el archivo | El proyecto no registrado, o el que aún no pasó, sigue funcionando | RN-08 |
| Una sola consulta por arranque | Una por regla | RNF-01 | RNF-01 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

No hay acciones nuevas: solo lectura.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `reglas_del_proyecto.py` y el arranque | Lógica | 1 h | Ninguna | EV-01 |
| T-02 | `del_proyecto` desde la tabla | Lógica | 0,5 h | T-01 | EV-01 |
| T-03 | Pruebas y regresión de `core.enganches` | Test | 1 h | T-02 | EV-01 |

**Total estimado:** 2,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-03 | Prueba de Django | EV-01 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django y una carpeta temporal de proyecto |
| Usuarios de prueba | Ninguno |
| Datos precargados | Un proyecto con dos reglas en la tabla, una que autoriza escribir |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Sin migración. Hasta que un proyecto pase sus reglas, todo sigue leyendo su archivo.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F11`](../../../../../base/02-flujo-de-trabajo/reglas/F11-una-fase-solo-modifica-codigo-de-su-propio-modulo.md), `01·C19`.

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
