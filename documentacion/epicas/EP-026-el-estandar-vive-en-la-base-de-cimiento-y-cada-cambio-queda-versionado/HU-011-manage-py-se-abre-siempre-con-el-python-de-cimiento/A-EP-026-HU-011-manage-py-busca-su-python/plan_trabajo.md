# Plan de Trabajo · Fase A-EP-026-HU-011-manage-py-busca-su-python (módulo arranque de Cimiento)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-026-HU-011-manage-py-busca-su-python` |
| **Épica** | `EP-026` |
| **HU** | [`HU-011`](../HU-011-manage-py-se-abre-siempre-con-el-python-de-cimiento.md), una sola (`F12.1`) |
| **Módulo** | Arranque de Cimiento, `proyectos/cimiento/manage.py` |
| **Especificación del módulo** | La HU-011 y la [épica EP-026](../../epica.md) |
| **Fecha apertura** | 2026-10-08 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 2 del pendiente 145](../../../../../historico-chat/resumenes/2026-10-08/pendientes/145-manage-py-usa-el-python-de-cimiento/analisis-2.md), el 2026-10-08, en el turno 37, con la versión 56.8.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Fase nueva. Sale del análisis 1 del pendiente 145, acuerdos 1 y 2, y del análisis 2, acuerdo 1, que nombra la HU.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-011` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-011-manage-py-se-abre-siempre-con-el-python-de-cimiento.md#ca-01--abierto-con-el-python-del-computador-la-consulta-responde) | ☑ |
| [CA-02](../HU-011-manage-py-se-abre-siempre-con-el-python-de-cimiento.md#ca-02--sin-venv-o-ya-abierto-con-él-no-se-vuelve-a-abrir) | ☑ |
| [CA-03](../HU-011-manage-py-se-abre-siempre-con-el-python-de-cimiento.md#ca-03--las-tildes-salen-bien) | ☑ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** `manage.py` funciona con cualquier Python que lo abra, porque se vuelve a abrir con el de Cimiento, y escribe las tildes bien.

**Fuera de alcance:** cambiar el texto del aviso de cada sesión.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`manage.py` carga el `.env` y pone el puerto; no revisa con qué Python lo abrieron. Con el Python del computador (3.11, sin `MySQLdb`), `ver_estandar` termina con `ModuleNotFoundError`; con `proyectos/cimiento/.venv/Scripts/python.exe` responde. `corredor.py` (`python_de_la_plataforma`) ya busca el Python de `.venv` en `Scripts/` y en `bin/`. Nada prueba hoy `manage.py`.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/manage.py` | Modificar | Arranque | Busca su Python, se vuelve a abrir con él y escribe en UTF-8 |
| `proyectos/cimiento/core/comun/tests_arranque.py` | Crear | Test | |

### 2.2 Matriz de dependencias del refactor

No aplica.

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

No aplica: es la consola.

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| `manage.py` se vuelve a abrir con el Python de `.venv` | Cambiar el texto del aviso | El aviso no es el único que llama a `manage.py` | Acuerdo 1 |
| La búsqueda va dentro de `manage.py`, sin importar `core` | Reusar `python_de_la_plataforma` | Importar `core` antes de saber qué Python corre puede fallar con el Python equivocado | Propuesta del agente |
| Se compara la ruta del Python que corre con la de `.venv` | Revisar si `MySQLdb` se importa | Comparar rutas no depende de qué tenga instalado cada Python | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

No aplica: no crea nada que haya que deshacer.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `manage.py` busca su Python y se vuelve a abrir con él | Arranque | 0,5 h | — | EV-01 |
| T-02 | `manage.py` escribe en UTF-8 | Arranque | 0,2 h | — | EV-01 |
| T-03 | Pruebas | Test | 0,5 h | T-01, T-02 | EV-01 |

**Total estimado:** 1,2 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Pruebas de Django y la consulta real | EV-01 | 2026-10-08 | ☑ |
| CA-02 | Pruebas de Django | EV-01 | 2026-10-08 | ☑ |
| CA-03 | Pruebas de Django y la consulta real | EV-01 | 2026-10-08 | ☑ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas y de la consulta | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django |
| Usuarios de prueba | Ninguno |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

No aplica: no cambia la base.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `08·T1`, `00·M13`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que `manage.py` se vuelva a abrir sin fin | La orden no termina | Solo se vuelve a abrir si el Python que corre no es el de `.venv` | Abierto |

## 11. Definition of Done

- [x] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [x] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno todavía.
