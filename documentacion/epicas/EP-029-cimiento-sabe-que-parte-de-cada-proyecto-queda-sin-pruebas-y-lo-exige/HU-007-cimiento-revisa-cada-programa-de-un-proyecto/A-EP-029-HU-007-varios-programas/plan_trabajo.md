# Plan de Trabajo · Fase A-EP-029-HU-007-varios-programas (módulo Pruebas de Cimiento)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-029-HU-007-varios-programas` |
| **Épica** | `EP-029` |
| **HU** | [`HU-007`](../HU-007-cimiento-revisa-cada-programa-de-un-proyecto.md), una sola (`F12.1`) |
| **Módulo** | Pruebas de Cimiento: `core/pruebas/` |
| **Especificación del módulo** | La HU-007 |
| **Fecha apertura** | 2026-10-08 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 4 del pendiente 141](../../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-4.md), el 2026-10-08, con la versión 59.0.0 |
| **Rama** | `main` |

**ORIGEN:** análisis 4 del pendiente 141, punto 3. Modifica las fases de las HU-002, HU-003 y HU-005, que suponían un programa por proyecto.

| CA de `HU-007` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-007-cimiento-revisa-cada-programa-de-un-proyecto.md#ca-01--cimiento-encuentra-todos-los-programas) | ☑ |
| [CA-02](../HU-007-cimiento-revisa-cada-programa-de-un-proyecto.md#ca-02--cada-programa-se-revisa-y-se-guarda-aparte) | ☑ |
| [CA-03](../HU-007-cimiento-revisa-cada-programa-de-un-proyecto.md#ca-03--la-fila-muestra-el-de-menos-pruebas-y-el-detalle-cada-uno) | ☑ |

## 1. Objetivo y alcance

**Objetivo:** que Cimiento revise cada programa de un proyecto y lo muestre.

**Fuera de alcance:** cambiar las herramientas de cada lenguaje.

## 2. Análisis previo, línea base verificada

`reconocer` (`core/pruebas/lenguaje.py`) devuelve un solo programa; `Revisor.revisar`, `ParteQueRevisa.poner` y `quitar` lo usan. En RNI hay `proyectos/rni-front` (Angular) y `proyectos/rni-back` (Python). Lo que pide el cambio (R-19): el campo `programa` de `Revision` genera una sola migración, `pruebas/0004_revision_programa.py`; ninguna pantalla nueva, ninguna carpeta que se borre.

### 2.1 Archivos que se crean o modifican

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/pruebas/models.py` | Modificar | Modelo | `programa`, las últimas revisiones y la de menos pruebas |
| `proyectos/cimiento/core/pruebas/migrations/0004_revision_programa.py` | Crear | Migración | El campo nuevo |
| `proyectos/cimiento/core/pruebas/lenguaje.py` | Modificar | Dominio | `reconocer_todos` |
| `proyectos/cimiento/core/pruebas/revisar.py` | Modificar | Dominio | Una revisión por programa |
| `proyectos/cimiento/core/pruebas/parte.py` | Modificar | Dominio | Pone y quita la herramienta en cada programa |
| `proyectos/cimiento/core/pruebas/views.py` | Modificar | Vista | La fila con el de menos pruebas; el detalle con todos |
| `proyectos/cimiento/core/pruebas/templates/pruebas/detalle.html` | Modificar | Plantilla | Un bloque por programa |
| `proyectos/cimiento/core/pruebas/tests_varios_programas.py` | Crear | Test | |

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Un programa dentro de otro Django, Laravel o Angular no cuenta aparte | Contar toda carpeta con señal | Un `requirements.txt` suelto dentro de Django no es otro programa | Propuesta del agente |
| Las revisiones de una misma vez comparten la fecha | Un grupo aparte | Sin tabla nueva; «las últimas» son las de la fecha más reciente | Propuesta del agente |

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

No hay acciones nuevas: «Borrar» sigue quitando cada revisión.

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `reconocer_todos` | Dominio | 1 h | Ninguna | EV-01 |
| T-02 | El modelo, la revisión por programa y la parte | Dominio | 2 h | T-01 | EV-01 |
| T-03 | La fila y el detalle | Vista | 1 h | T-02 | EV-01 |
| T-04 | Pruebas y regresión | Test | 1 h | T-01 a T-03 | EV-01 |

## 5. Verificación de criterios de aceptación

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Prueba de Django | EV-01 | 2026-10-08 | ☑ |
| CA-02 | Prueba de Django, con la herramienta simulada | EV-01 | 2026-10-08 | ☑ |
| CA-03 | Prueba de Django | EV-01 | 2026-10-08 | ☑ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 7. Reversión / rollback

Revertir el commit y `manage.py migrate pruebas 0003`.

## 8. Producción y migración incremental

Aditiva: un campo que queda vacío en las revisiones de antes.

## 9. Reglas del estándar y del proyecto aplicadas

- Base: `02·F8`, `02·F30`, `08·T3`, `00·ID7`.

## 11. Definition of Done

- [x] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [x] Pruebas en verde
- [ ] Rama lista para el commit único de la fase

## 13. Cierre

**Hallazgos al ejecutar:** H-9 del 2026-10-07: `models.py` se cambió antes de escribir este plan; el plan lo declara.
