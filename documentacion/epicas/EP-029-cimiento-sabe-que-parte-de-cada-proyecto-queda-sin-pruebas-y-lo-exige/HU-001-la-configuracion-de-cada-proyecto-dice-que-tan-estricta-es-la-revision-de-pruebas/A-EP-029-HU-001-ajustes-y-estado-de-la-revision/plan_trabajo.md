# Plan de Trabajo · Fase A-EP-029-HU-001-ajustes-y-estado-de-la-revision (módulo Pruebas de Cimiento)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-029-HU-001-ajustes-y-estado-de-la-revision` |
| **Épica** | `EP-029` |
| **HU** | [`HU-001`](../HU-001-la-configuracion-de-cada-proyecto-dice-que-tan-estricta-es-la-revision-de-pruebas.md), una sola (`F12.1`) |
| **Módulo** | Pruebas de Cimiento: la app nueva `core/pruebas/`, y los ajustes de `core/proyectos/` con su ayuda |
| **Especificación del módulo** | La HU-001: sus CA y sus reglas de negocio |
| **Fecha apertura** | 2026-10-08 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 141](../../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-1.md), el 2026-10-08, con la versión 56.8.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Nueva funcionalidad: sale del análisis 1 del pendiente 141, puntos 2, 3 y 11.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-001` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-001-la-configuracion-de-cada-proyecto-dice-que-tan-estricta-es-la-revision-de-pruebas.md#ca-01--los-dos-ajustes-existen-en-las-tres-capas) | ☑ |
| [CA-02](../HU-001-la-configuracion-de-cada-proyecto-dice-que-tan-estricta-es-la-revision-de-pruebas.md#ca-02--los-dos-ajustes-salen-en-la-página-del-proyecto-con-su-ayuda) | ☑ |
| [CA-03](../HU-001-la-configuracion-de-cada-proyecto-dice-que-tan-estricta-es-la-revision-de-pruebas.md#ca-03--la-base-guarda-el-estado-de-la-revisión-de-cada-proyecto) | ☑ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que cada proyecto tenga en su configuración qué tan estricta es la revisión de pruebas y cada cuántos días toca, y que la base guarde el estado de cada revisión.

**Fuera de alcance:** correr la revisión (HU-002) y avisar (HU-003).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

Los ajustes viven en el catálogo `AJUSTES` de `core/proyectos/ajustes.py`, con sus tres capas en `efectivos()`. `ProyectoForm` y `ConfiguracionForm` (`core/proyectos/forms.py`) arman un campo por cada clave del catálogo, sin tocar sus plantillas. La ayuda de cada ajuste es la clave `configuracion.<clave>` de `core/ayuda/textos.py`, y `core/ayuda/tests.py` exige que toda clave del catálogo tenga texto. La historia de la base (`core/historia/registro.py`) cubre sola toda tabla nueva por las señales de Django. No existe ninguna app de pruebas.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/proyectos/ajustes.py` | Modificar | Dominio | Los dos ajustes |
| `proyectos/cimiento/core/ayuda/textos.py` | Modificar | Ayuda | El texto del «?» de cada ajuste |
| `proyectos/cimiento/config/settings/base.py` | Modificar | Configuración | La app nueva en `INSTALLED_APPS` |
| `proyectos/cimiento/core/pruebas/__init__.py` | Crear | App | |
| `proyectos/cimiento/core/pruebas/apps.py` | Crear | App | |
| `proyectos/cimiento/core/pruebas/models.py` | Crear | Modelo | El estado de cada proyecto y sus revisiones |
| `proyectos/cimiento/core/pruebas/migrations/__init__.py` | Crear | Migración | |
| `proyectos/cimiento/core/pruebas/migrations/0001_inicial.py` | Crear | Migración | Tablas nuevas |
| `proyectos/cimiento/core/pruebas/tests.py` | Crear | Test | |
| `proyectos/cimiento/core/proyectos/migrations/0007_ajustes_de_revision.py` | Crear | Migración | Las opciones nuevas de la clave de los ajustes; la agregó el análisis 2 del pendiente 141, acuerdo 1, verificada con `makemigrations --dry-run` |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| El catálogo `AJUSTES` gana dos claves | Los formularios, la configuración que leen los enganches, la copia local y la ayuda | `core.pruebas`, `core.proyectos`, `core.ayuda`, `core.enganches` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

Ninguna nueva.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

«Proyectos» → «Editar», y «Configuración».

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Los dos ajustes van en el catálogo que ya existe | Campos nuevos en `Proyecto` | Así heredan las tres capas, el formulario y la ayuda | Acuerdo 9, `17·I5` |
| Las opciones se guardan con las palabras que ve el usuario: «solo avisar», «no dejar guardar», «nada» | Códigos internos | El formulario muestra la opción tal cual y nadie tiene que traducirla | Acuerdo 8 |
| Una app nueva, `core/pruebas/` | Meter las tablas en `core/proyectos/` | La revisión crece en las HU-002, 003 y 005; separada no mezcla módulos (`02·F11`) | `02·F11` (propuesta del agente) |
| Las revisiones quedan en la historia de la base | Sacarlas como el gasto | Tocar `core/historia/` sería otro módulo; una fila por revisión no pesa | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

Poner un valor en un ajuste tiene su contraria: dejarlo vacío, que vuelve a la capa de abajo. Las revisiones se borran con su proyecto.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Los dos ajustes en el catálogo | Dominio | 0,5 h | Ninguna | EV-01 |
| T-02 | La ayuda de los dos ajustes | Ayuda | 0,5 h | T-01 | EV-01 |
| T-03 | La app `core/pruebas/` con sus modelos y su migración | Modelo | 1 h | Ninguna | EV-01 |
| T-04 | Pruebas | Test | 1 h | T-01 a T-03 | EV-01 |

**Total estimado:** 3 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03, T-04.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Prueba de Django | EV-01 | 2026-10-08 | ☑ |
| CA-02 | Prueba de Django | EV-01 | 2026-10-08 | ☑ |
| CA-03 | Prueba de Django | EV-01 | 2026-10-08 | ☑ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django |
| Usuarios de prueba | Uno, creado por la prueba |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit y deshacer la migración con `manage.py migrate pruebas zero`.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Aditiva: tablas nuevas y dos claves de ajuste que, sin fila, valen lo de fábrica.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `02·F11`, `02·F30`, `08·T6`, `00·ID7`, `20·M3`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Ninguno | | | |

## 11. Definition of Done

- [x] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [x] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** H-2 de la sesión del 2026-10-07: falta declarar `core/proyectos/migrations/0007_…py`, la migración que piden las dos claves nuevas de ajustes. El análisis 2 del pendiente 141 la agregó a la §2.1 y la fase siguió desde T-03.
