# Plan de Trabajo · Fase B-EP-001-HU-041-los-totales-del-sello-se-leen (módulo Capítulos 01 y 20)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, sobre qué archivos y cómo se comprueba. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-001-HU-041-los-totales-del-sello-se-leen` |
| **Épica** | `EP-001` |
| **HU** | [`HU-041`](../HU-041-las-reglas-reconocen-la-base-de-cimiento-como-fuente-del-estandar.md), una sola (`F12.1`) |
| **Módulo** | Capítulos `01 · Conducta de la IA` y `20 · Meta-reglas` |
| **Especificación del módulo** | [base/01-conducta.md](../../../../../base/01-conducta.md) y [base/20-meta-reglas/base.md](../../../../../base/20-meta-reglas/base.md) |
| **Fecha apertura** | 2026-10-06 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 132](../../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md), el 2026-10-06, con la versión 56.0.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): `A-EP-001-HU-041-las-reglas-nombran-la-base`. Esa fase escribió los totales del sello de `M10` y `C19` con comas; el validador solo lee el formato del checklist y, con comas, se salta la comparación con la tabla. Es un defecto de la fase A, dentro del alcance aprobado.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-041` que cierra esta fase | Estado |
|---|---|
| [CA-03](../HU-041-las-reglas-reconocen-la-base-de-cimiento-como-fuente-del-estandar.md#ca-03--las-reglas-pasan-sus-comprobaciones) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que los totales del sello de `M10` y `C19` vuelvan al formato del checklist, para que el validador los compare con la tabla.

**Fuera de alcance:** lo que exigen las reglas, que no cambia.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`_TOTALES_DEL_SELLO`, en `proyectos/cimiento/core/validadores/metareglas.py`, busca el formato del checklist; sin coincidencia, `totales` no devuelve nada.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md` | Modificar | Regla | Línea de totales del sello |
| `base/01-conducta.md` | Modificar | Regla | Línea de totales del sello de `C19` |

### 2.2 Matriz de dependencias del refactor

No aplica.

### 2.3 Rutas / endpoints y control de acceso

No aplica.

### 2.4 Punto de entrada en la UI

No aplica.

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Se vuelve al formato del checklist aunque el aviso de redacción marque el punto medio | Dejar las comas | El formato lo fija `base/20-meta-reglas/checklist.md` §3 y lo lee el validador | Propuesta del agente |
| Sin versión nueva | PARCHE | El sello no es el texto de la regla; lo que se exige no cambia | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva

No aplica.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Volver al formato del checklist en `M10` y `C19` | Regla | 0,1 h | — | EV-01 |
| T-02 | Correr `validar.py metareglas` | Test | 0,1 h | T-01 | EV-01 |

**Total estimado:** 0,2 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-03 | Validador de meta-reglas | EV-01 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida del validador | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

El repositorio del estándar, en la máquina local.

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit de la fase.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12

No aplica: no cambia lo que se exige.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `20·M5`.

## 10. Riesgos y bloqueos

Ninguno.

## 11. Definition of Done

- [ ] CA-03 verificado
- [ ] Validador en verde

## 13. Cierre

**Hallazgos al ejecutar:** ninguno todavía.
