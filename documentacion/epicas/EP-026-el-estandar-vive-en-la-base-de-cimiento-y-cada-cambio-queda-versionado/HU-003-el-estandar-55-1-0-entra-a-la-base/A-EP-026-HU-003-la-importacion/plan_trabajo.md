# Plan de Trabajo · Fase A-EP-026-HU-003-la-importacion (módulo Estándar en la base)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-026-HU-003-la-importacion` |
| **Épica** | `EP-026` |
| **HU** | [`HU-003`](../HU-003-el-estandar-55-1-0-entra-a-la-base.md), una sola (`F12.1`) |
| **Módulo** | Estándar en la base, `proyectos/cimiento/core/estandar/` |
| **Especificación del módulo** | La HU-003 y la [épica EP-026](../../epica.md) |
| **Fecha apertura** | 2026-10-06 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 132](../../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md), el 2026-10-06, con la versión 56.0.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Fase nueva. Sale del análisis 1 del pendiente 132, acuerdos 2, 5, 6, 10 y 17.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-003` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-003-el-estandar-55-1-0-entra-a-la-base.md#ca-01--todo-base-entra-a-la-base) | ☐ |
| [CA-02](../HU-003-el-estandar-55-1-0-entra-a-la-base.md#ca-02--la-memoria-de-cada-proyecto-entra-a-la-base) | ☐ |
| [CA-03](../HU-003-el-estandar-55-1-0-entra-a-la-base.md#ca-03--la-importación-es-la-versión-de-partida-y-no-se-repite) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que `base/` y la memoria de cada proyecto queden en la base de Cimiento, con la versión del estándar como punto de partida.

**Fuera de alcance:** leer desde la base (HU-004) y editar desde la pantalla (HU-005).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`base/` tiene 152 documentos `.md` y nada más, 1,4 MB. Los lectores del estándar (`CuerpoDeReglas.leer`, `MapaDeTareas`, `recuperar.py`) leen con `Archivos.leer` y recorren con `Proyecto.recorrer_md`: guardar cada documento con su ruta deja que la HU-004 los sirva desde la base sin reescribirlos. La memoria vive en `historico-chat/memory/` de cada proyecto; hay 12 proyectos registrados. `VERSION` dice 56.1.0.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/estandar/__init__.py` | Crear | Módulo | |
| `proyectos/cimiento/core/estandar/apps.py` | Crear | Módulo | |
| `proyectos/cimiento/core/estandar/models.py` | Crear | Modelo | `Documento`, `Recuerdo` |
| `proyectos/cimiento/core/estandar/importar.py` | Crear | Lógica | |
| `proyectos/cimiento/core/estandar/migrations/__init__.py` | Crear | Migración | |
| `proyectos/cimiento/core/estandar/migrations/0001_initial.py` | Crear | Migración | Aditiva |
| `proyectos/cimiento/core/estandar/management/__init__.py` | Crear | Orden | |
| `proyectos/cimiento/core/estandar/management/commands/__init__.py` | Crear | Orden | |
| `proyectos/cimiento/core/estandar/management/commands/importar_estandar.py` | Crear | Orden | |
| `proyectos/cimiento/core/estandar/tests.py` | Crear | Test | |
| `proyectos/cimiento/core/historia/registro.py` | Modificar | Lógica | `en_version`: los cambios van a una versión dada |
| `proyectos/cimiento/core/historia/versiones.py` | Modificar | Lógica | La versión de partida del estándar |
| `proyectos/cimiento/config/settings/base.py` | Modificar | Config | La app |

### 2.2 Matriz de dependencias del refactor

No aplica.

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

No aplica: `manage.py importar_estandar`, una vez.

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Cada documento entra entero, con su ruta | Partir cada regla en columnas | Una sola fuente: las reglas, el mapa y las palabras se siguen leyendo con los lectores de hoy; partirlas dejaría dos copias que se separan | Propuesta del agente |
| La memoria es un `Recuerdo` por proyecto | Un documento más del estándar | La memoria es de cada proyecto, no del estándar (`01·C19`) | Acuerdo 17 |
| La versión de partida es la del archivo `VERSION` y lleva todos los documentos | Subir una versión por documento | Importar no cambia lo que se exige | Acuerdo 6 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

| Acción | Contraria |
|---|---|
| Importar el estándar | `manage.py migrate estandar zero` quita las tablas; los archivos de `base/` siguen intactos |

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Modelos `Documento` y `Recuerdo` | Modelo | 0,5 h | — | EV-01 |
| T-02 | Importar `base/` y la memoria, con la versión de partida | Lógica | 1,5 h | T-01 | EV-01 |
| T-03 | Pruebas | Test | 1 h | T-02 | EV-01 |
| T-04 | Importar en la base real | Datos | 0,2 h | T-03 | EV-02 |

**Total estimado:** 3,2 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03, T-04

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Pruebas de Django | EV-01 | | ☐ |
| CA-02 | Pruebas de Django | EV-01 | | ☐ |
| CA-03 | Pruebas de Django e importación real | EV-01, EV-02 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |
| EV-02 | Salida de la importación real | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django; el estándar real como origen |
| Usuarios de prueba | Ninguno |
| Datos precargados | Un proyecto con una carpeta temporal de recuerdos |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit y `manage.py migrate estandar zero`. Hay copia diaria de la base (HU-010).

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Aditiva: dos tablas nuevas y su carga. Nadie las lee hasta la HU-004.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `20·M10`, `01·C19`, `01·C29`, `00·N7`.

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
