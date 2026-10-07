# Plan de Trabajo · Fase A-EP-026-HU-001-el-registro-de-cambios (módulo Historia de Cimiento)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-026-HU-001-el-registro-de-cambios` |
| **Épica** | `EP-026` |
| **HU** | [`HU-001`](../HU-001-todo-cambio-guardado-en-la-base-deja-quien-cuando-antes-despues-y-por-que.md), una sola (`F12.1`) |
| **Módulo** | Historia de Cimiento, `proyectos/cimiento/core/historia/` |
| **Especificación del módulo** | La HU-001 y la [épica EP-026](../../epica.md) |
| **Fecha apertura** | 2026-10-06 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 132](../../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md), el 2026-10-06, con la versión 56.0.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Fase nueva: el módulo no existe. Sale del análisis 1 del pendiente 132, acuerdos 1, 3, 19 y 21.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-001` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-001-todo-cambio-guardado-en-la-base-deja-quien-cuando-antes-despues-y-por-que.md#ca-01--un-cambio-en-cualquier-tabla-queda-en-la-historia) | ☐ |
| [CA-02](../HU-001-todo-cambio-guardado-en-la-base-deja-quien-cuando-antes-despues-y-por-que.md#ca-02--lo-que-escriben-los-enganches-también-queda) | ☐ |
| [CA-03](../HU-001-todo-cambio-guardado-en-la-base-deja-quien-cuando-antes-despues-y-por-que.md#ca-03--un-cambio-se-puede-deshacer) | ☐ |
| [CA-04](../HU-001-todo-cambio-guardado-en-la-base-deja-quien-cuando-antes-despues-y-por-que.md#ca-04--sin-claves-en-la-historia) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** un solo registro de cambios para toda tabla de Cimiento, con su pantalla y su botón para deshacer.

**Fuera de alcance:** la versión de cada cambio (HU-002).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

Hoy solo `niveles.CambioDeNivel` guarda historia. Lo que escribe sin Django es `core/enganches/estado_en_base.py` (el estado del análisis). El gasto (`core/consumo/`) se trae de Claude Code y no se edita. Cada pantalla nueva necesita su sección de ayuda (`core/ayuda/secciones.py`, prueba `test_ninguna_pantalla_queda_sin_seccion`).

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/historia/__init__.py` | Crear | Módulo | |
| `proyectos/cimiento/core/historia/apps.py` | Crear | Módulo | Conecta las señales |
| `proyectos/cimiento/core/historia/models.py` | Crear | Modelo | `Cambio` |
| `proyectos/cimiento/core/historia/registro.py` | Crear | Lógica | Quién y por qué, señales, deshacer |
| `proyectos/cimiento/core/historia/middleware.py` | Crear | Lógica | La cuenta de cada petición |
| `proyectos/cimiento/core/historia/views.py` | Crear | Vista | Lista y deshacer |
| `proyectos/cimiento/core/historia/urls.py` | Crear | Rutas | |
| `proyectos/cimiento/core/historia/migrations/__init__.py` | Crear | Migración | |
| `proyectos/cimiento/core/historia/migrations/0001_initial.py` | Crear | Migración | Aditiva |
| `proyectos/cimiento/core/historia/templates/historia/lista.html` | Crear | Plantilla | |
| `proyectos/cimiento/core/historia/tests.py` | Crear | Test | |
| `proyectos/cimiento/config/settings/base.py` | Modificar | Config | La app y el middleware |
| `proyectos/cimiento/config/urls.py` | Modificar | Rutas | |
| `proyectos/cimiento/templates/base.html` | Modificar | Plantilla | La entrada «Historia» del menú |
| `proyectos/cimiento/core/enganches/estado_en_base.py` | Modificar | Lógica | Escribe su cambio en la historia |
| `proyectos/cimiento/core/ayuda/secciones.py` | Modificar | Ayuda | La sección de la pantalla |
| `proyectos/cimiento/core/ayuda/templates/ayuda/secciones/historia.html` | Crear | Ayuda | |

### 2.2 Matriz de dependencias del refactor

No aplica: todo es aditivo.

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

| Ruta | Método | Quién |
|---|---|---|
| `/historia/` | GET | Toda cuenta que entró |
| `/historia/<id>/deshacer/` | POST | Grupo administrador |

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

Menú lateral → «Historia».

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno nuevo: usa los grupos administrador y consulta.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Señales de Django sobre todas las tablas, menos las de Django que no son datos y el gasto | Un registro escrito en cada vista | Una tabla nueva queda cubierta sin escribir nada | Propuesta del agente |
| Se guardan solo los campos que cambiaron, y no las fechas automáticas | La fila entera | La historia dice qué cambió sin ruido | Propuesta del agente |
| El gasto no entra | Registrar cada línea | Cada línea ya es su historia, con su fecha, y nunca se edita; duplicaría miles de filas al día | Propuesta del agente |
| `CambioDeNivel` se queda | Migrarlo | Lo usa la pantalla de historial de niveles; la historia nueva también registra los niveles | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

| Acción | Contraria |
|---|---|
| Registrar un cambio | Deshacerlo, que deja otro cambio |

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Modelo `Cambio`, señales y quién y por qué | Modelo | 2 h | — | EV-01 |
| T-02 | El estado del análisis escribe su cambio | Lógica | 0,5 h | T-01 | EV-01 |
| T-03 | Deshacer y pantalla «Historia» con su ayuda | Vista | 1,5 h | T-01 | EV-01 |
| T-04 | Tapado de claves y contraseña «cambiada» | Lógica | 0,5 h | T-01 | EV-01 |
| T-05 | Pruebas de `core.historia` y regresión | Test | 1 h | T-01 a T-04 | EV-01 |

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
| Ambiente | Cimiento en la máquina local, con la base de pruebas que crea Django |
| Usuarios de prueba | Una cuenta administradora y una de consulta, creadas en la prueba |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit y deshacer la migración `historia 0001` (`manage.py migrate historia zero`).

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Aditiva: una tabla nueva. Cimiento corre en una sola máquina; se aplica con `manage.py migrate`.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `00·N6`, `20·M10`, `20·M11`, `02·F30`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Otra sesión escribe en la misma carpeta y el freno se lo cobra a esta | Detiene órdenes de consola | Se anota y se sigue cuando el archivo ajeno no cambia durante la orden | Abierto |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno todavía.
