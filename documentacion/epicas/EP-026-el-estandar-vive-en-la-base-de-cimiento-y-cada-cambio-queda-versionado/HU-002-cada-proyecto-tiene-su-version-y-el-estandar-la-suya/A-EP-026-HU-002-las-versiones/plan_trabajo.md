# Plan de Trabajo · Fase A-EP-026-HU-002-las-versiones (módulo Historia de Cimiento)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-026-HU-002-las-versiones` |
| **Épica** | `EP-026` |
| **HU** | [`HU-002`](../HU-002-cada-proyecto-tiene-su-version-y-el-estandar-la-suya.md), una sola (`F12.1`) |
| **Módulo** | Historia de Cimiento, `proyectos/cimiento/core/historia/` |
| **Especificación del módulo** | La HU-002 y la [épica EP-026](../../epica.md) |
| **Fecha apertura** | 2026-10-06 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 132](../../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md), el 2026-10-06, con la versión 56.0.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): `A-EP-026-HU-001-el-registro-de-cambios`, que creó la historia. Sale del análisis 1 del pendiente 132, acuerdos 1, 7, 12, 13 y 14.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-002` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-002-cada-proyecto-tiene-su-version-y-el-estandar-la-suya.md#ca-01--un-cambio-de-un-proyecto-sube-su-versión-no-la-del-estándar) | ☐ |
| [CA-02](../HU-002-cada-proyecto-tiene-su-version-y-el-estandar-la-suya.md#ca-02--las-dos-preguntas-fijan-el-tipo) | ☐ |
| [CA-03](../HU-002-cada-proyecto-tiene-su-version-y-el-estandar-la-suya.md#ca-03--un-ajuste-común-sube-la-versión-del-estándar) | ☐ |
| [CA-04](../HU-002-cada-proyecto-tiene-su-version-y-el-estandar-la-suya.md#ca-04--las-versiones-se-ven) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que todo cambio de configuración suba la versión de su proyecto o la del estándar, con el tipo que dan las dos preguntas.

**Fuera de alcance:** las tablas del estándar (HU-003) y los reportes (HU-008).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

La historia (`core/historia/registro.py`, función `anotar`) escribe cada cambio. Los formularios que guardan configuración son `niveles/reglas.html`, `proyectos/configuracion.html`, `proyectos/formulario.html` y `proyectos/suspensiones.html`. La versión del estándar está en el archivo `VERSION`.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/historia/models.py` | Modificar | Modelo | `Version` y `Cambio.version` |
| `proyectos/cimiento/core/historia/versiones.py` | Crear | Lógica | Ámbito, tipo y número |
| `proyectos/cimiento/core/historia/registro.py` | Modificar | Lógica | El cambio apunta a su versión |
| `proyectos/cimiento/core/historia/middleware.py` | Modificar | Lógica | Lee las dos preguntas del envío |
| `proyectos/cimiento/core/historia/views.py` | Modificar | Vista | Pantalla «Versiones» |
| `proyectos/cimiento/core/historia/urls.py` | Modificar | Rutas | |
| `proyectos/cimiento/core/historia/migrations/0002_version.py` | Crear | Migración | Aditiva |
| `proyectos/cimiento/core/historia/templates/historia/versiones.html` | Crear | Plantilla | |
| `proyectos/cimiento/core/historia/templates/historia/lista.html` | Modificar | Plantilla | Enlace a versiones y columna |
| `proyectos/cimiento/core/historia/templates/historia/_tipo_de_version.html` | Crear | Plantilla | Las dos preguntas y el motivo |
| `proyectos/cimiento/core/historia/tests_versiones.py` | Crear | Test | |
| `proyectos/cimiento/core/niveles/templates/niveles/reglas.html` | Modificar | Plantilla | Incluye las preguntas |
| `proyectos/cimiento/core/proyectos/templates/proyectos/configuracion.html` | Modificar | Plantilla | Incluye las preguntas |
| `proyectos/cimiento/core/proyectos/templates/proyectos/formulario.html` | Modificar | Plantilla | Incluye las preguntas |
| `proyectos/cimiento/core/proyectos/templates/proyectos/suspensiones.html` | Modificar | Plantilla | Incluye las preguntas |
| `proyectos/cimiento/core/ayuda/secciones.py` | Modificar | Ayuda | La pantalla de versiones |
| `proyectos/cimiento/core/ayuda/templates/ayuda/secciones/historia.html` | Modificar | Ayuda | Versiones y las dos preguntas |

### 2.2 Matriz de dependencias del refactor

No aplica: todo es aditivo.

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

| Ruta | Método | Quién |
|---|---|---|
| `/historia/versiones/` | GET | Toda cuenta que entró |

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

«Historia» → «Versiones»; las preguntas, al pie de cada formulario que guarda configuración.

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| El middleware lee las dos preguntas del envío y la versión se crea al anotar el primer cambio | Escribir la versión en cada vista | Una pantalla nueva solo incluye el pedazo de plantilla | Propuesta del agente |
| Sin preguntas respondidas, PARCHE | Rechazar el cambio | Un programa no responde preguntas; las propuestas del agente llegan con la HU-005 | Propuesta del agente |
| Cuentas y estado del análisis sin versión | Versionarlo todo | `20·M10` versiona el estándar y la configuración de cada proyecto | `20·M10` |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

| Acción | Contraria |
|---|---|
| Subir una versión | Deshacer su cambio, que sube otra versión |

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Modelo `Version`, ámbito y número | Modelo | 1,5 h | — | EV-01 |
| T-02 | El cambio apunta a su versión, una por envío | Lógica | 1 h | T-01 | EV-01 |
| T-03 | Las dos preguntas en los formularios | Plantilla | 1 h | T-02 | EV-01 |
| T-04 | Pantalla «Versiones» y ayuda | Vista | 1 h | T-01 | EV-01 |
| T-05 | Pruebas y regresión | Test | 1 h | T-01 a T-04 | EV-01 |

**Total estimado:** 5,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03, T-04, T-05

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Pruebas de Django | EV-01 | | ☐ |
| CA-02 | Pruebas de Django | EV-01 | | ☐ |
| CA-03 | Pruebas de Django | EV-01 | | ☐ |
| CA-04 | Pruebas de Django | EV-01 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | Cimiento en la máquina local, con la base de pruebas de Django |
| Usuarios de prueba | Una cuenta administradora, creada en la prueba |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit y `manage.py migrate historia 0001`.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Aditiva: una tabla y una columna que admite vacío.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `20·M10`, `02·F30`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Otra sesión escribe en la misma carpeta y el freno se lo cobra a esta | Detiene órdenes de consola | Se anota y se sigue | Abierto |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno todavía.
