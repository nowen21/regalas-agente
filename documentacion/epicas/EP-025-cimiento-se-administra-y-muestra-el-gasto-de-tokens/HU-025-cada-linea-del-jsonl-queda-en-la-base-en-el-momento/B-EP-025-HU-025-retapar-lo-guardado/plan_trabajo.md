# Plan de Trabajo · Fase B-EP-025-HU-025-retapar-lo-guardado (módulo Cimiento, consumo)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba acepta el alcance y el costo. El requisito vive en la HU, el detalle de las pruebas en el `plan_pruebas` de la misma fase, y lo que quedó hecho en el `funcionalidad_implementada.md` del cierre.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-025-HU-025-retapar-lo-guardado` |
| **Épica** | `EP-025` |
| **HU** | [`HU-025`](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md), una sola (`F12.1`) |
| **Módulo** | Cimiento, `core/consumo/` |
| **Especificación del módulo** | [HU-025](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md) |
| **Fecha apertura** | 2026-10-06 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 129](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-002-enmascarar-claves/pendientes/129-el-enmascarador-no-reconoce-las-claves-de-anthropic/analisis-1.md), el 2026-10-06, con la versión 55.2.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): `A-EP-025-HU-025-lineas-a-la-base-sin-relojes`, que guarda las líneas tapadas con el tapado del momento. Suma volver a taparlas cuando el tapado aprende algo. Sale del análisis 1 del pendiente 129, acuerdo 2.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-025` que cierra esta fase | Estado |
|---|---|
| [CA-05](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md#ca-05--lo-guardado-se-vuelve-a-tapar) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** `manage.py retapar_lineas` pasa el tapado de hoy por todas las líneas guardadas y deja tapada cada clave que reconozca; se corre una vez.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-05 | Lo guardado se vuelve a tapar | Funcional | Baja |

**Fuera de alcance:** cambiar lo que el tapado reconoce, que es la fase C de EP-005·HU-002.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`LineaDeSesion` guarda el texto tapado y cuántas claves tapó (`tapadas`). Medido el 2026-10-06: 102 478 líneas; 3 con `sk-ant-` en claro y 4 con `ANTHROPIC_API_KEY=`, todas la clave falsa de una prueba.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/consumo/management/commands/retapar_lineas.py` | Nuevo | Comando | |
| `proyectos/cimiento/core/consumo/tests_retapar.py` | Nuevo | Test | |
| `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento/HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md` | Modificar | Doc | CA-05 y la fila de la fase |

### 2.2 a 2.5

No aplica: sin contratos que cambien, sin rutas, sin pantalla, sin permisos.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Se recorre la base por tandas (`iterator`) y se guarda solo la línea que cambió | Cargar todo en memoria | Son más de cien mil líneas | Propuesta del agente |
| La huella no cambia | Recalcularla sobre el texto tapado | La huella identifica la línea original; si cambiara, la próxima lectura la volvería a guardar | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

| Acción nueva | Su contraria | Prueba |
|---|---|---|
| `retapar_lineas` | No tiene vuelta, a propósito: destapar una clave es lo que `00·N6` prohíbe | CP-002 muestra que correrla otra vez no cambia nada |

## 3. Desglose de tareas por criterio de aceptación

### [CA-05](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md#ca-05--lo-guardado-se-vuelve-a-tapar)

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `retapar_lineas` | Comando | 0,5 h | — | EV-01 |
| T-02 | `tests_retapar.py` | Test | 0,5 h | T-01 | EV-01 |
| T-03 | Correrla sobre la base real | Sistema | 0,2 h | T-02 | EV-02 |

**Total estimado:** 1,2 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-05 | Pruebas y corrida real | EV-01, EV-02 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de `tests_retapar` | `resultado_pruebas.md` |
| EV-02 | Salida de `retapar_lineas` y conteo posterior | `resultado_pruebas.md` |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | `manage.py test` local y la base `cimiento` local |
| Datos | Líneas armadas en la prueba, con la clave armada al correr |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit quita la orden. Lo tapado se queda tapado, a propósito.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Correr `manage.py retapar_lineas` una vez después de actualizar.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`00·N6`](../../../../../base/00-nucleo-blindado.md#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada), [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md).

## 10. Riesgos y bloqueos

Ninguno.

## 11. Definition of Done

- [ ] CA-05 verificado con evidencia
- [ ] Pruebas en verde

## 13. Cierre

Las 3 tareas quedaron hechas el 2026-10-06, con la versión 55.3.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** ninguno.
