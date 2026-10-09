# Plan de Trabajo · Fase B-EP-025-HU-028-ningun-mensaje-sin-trabajo (módulo El gasto)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-025-HU-028-ningun-mensaje-sin-trabajo` |
| **Épica** | `EP-025` |
| **HU** | [`HU-028`](../HU-028-el-trabajo-de-cada-mensaje-sale-de-lo-que-esta-abierto.md), una sola (`F12.1`) |
| **Módulo** | El gasto: `core/consumo/` |
| **Especificación del módulo** | Los CA de la HU-028 |
| **Fecha apertura** | 2026-10-08 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | El usuario, con la orden de erradicar «(sin trabajo)», el 2026-10-08, con la versión 58.0.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): `A-EP-025-HU-028-el-trabajo-abierto`, que dejó el 30 % de los mensajes sin trabajo.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-028` que cierra esta fase | Estado |
|---|---|
| [CA-05](../HU-028-el-trabajo-de-cada-mensaje-sale-de-lo-que-esta-abierto.md#ca-05--ningún-mensaje-queda-sin-trabajo) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** saber qué deja a cada mensaje sin trabajo y corregirlo en la causa, hasta que ningún mensaje quede «(sin trabajo)».

**Fuera de alcance:** cambiar las fuentes de la fase A.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

Medido el 2026-10-08 en la base real: 591 mensajes de 7 días sin trabajo, en 17 conversaciones (382 de este repo, 167 de scilit, 32 de master-ciberseguridad, 10 de LocalHub). 8 de esas conversaciones no tienen ningún mensaje con trabajo (167 mensajes); 6 no tienen sus líneas en la base. El detalle de las causas lo da el guion de diagnóstico.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-028-el-trabajo-de-cada-mensaje-sale-de-lo-que-esta-abierto/HU-028-el-trabajo-de-cada-mensaje-sale-de-lo-que-esta-abierto.md` | Modificar | Documento | CA-05 y la fase B |
| `proyectos/cimiento/core/consumo/trabajo.py` | Modificar | Lógica | |
| `proyectos/cimiento/core/consumo/lector.py` | Modificar | Lógica | |
| `proyectos/cimiento/core/consumo/guardar.py` | Modificar | Lógica | |
| `proyectos/cimiento/core/consumo/models.py` | Modificar | Modelo | Si hace falta un dato nuevo del mensaje |
| `proyectos/cimiento/core/consumo/migrations/0007_trabajo_de_la_conversacion.py` | Crear | Migración | Si hace falta |
| `proyectos/cimiento/core/consumo/management/commands/recalcular_trabajo.py` | Modificar | Orden | |
| `proyectos/cimiento/core/consumo/tablero.py` | Modificar | Lógica | |
| `proyectos/cimiento/core/consumo/templates/consumo/_actividad.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/consumo/templates/consumo/_donde.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/ayuda/textos.py` | Modificar | Lógica | El «?» de «Trabajo» |
| `proyectos/cimiento/core/consumo/tests_trabajo_abierto.py` | Modificar | Test | |
| `proyectos/cimiento/core/consumo/tests_segunda_tanda.py` | Modificar | Test | Esperaba «(sin trabajo)» |
| `historico-chat/scripts/2026-10-08/diagnostico_sin_trabajo.py` | Crear | Guion de apoyo | Clasifica por causa los mensajes sin trabajo |
| `historico-chat/scripts/2026-10-08/salida_diagnostico_sin_trabajo.txt` | Crear | Evidencia | Antes y después |
| `historico-chat/scripts/2026-10-08/README.md` | Modificar | Índice | |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| `lector.py`, `guardar.py`, `trabajo.py` | El vigilante y `leer_consumo` | `core.consumo` |
| `textos.py` | La ayuda | `core.ayuda` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

Ninguna nueva.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

Gasto de tokens → «Dónde se gasta» → Trabajo, y «Actividad».

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

Se escriben al terminar el diagnóstico (T-01).

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

`recalcular_trabajo` se puede volver a correr.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Diagnóstico: cada mensaje sin trabajo con su causa | Guion | 0,5 h | Ninguna | EV-02 |
| T-02 | Corregir cada causa | Lógica | 1 h | T-01 | EV-01 |
| T-03 | Recalcular la base real y medir | Orden | 0,25 h | T-02 | EV-02 |
| T-04 | Pruebas, pantalla y ayuda | Test | 0,5 h | T-02 | EV-01 |

**Total estimado:** 2,25 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03, T-04.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-05 | Prueba de Django y la base real | EV-01, EV-02 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |
| EV-02 | Diagnóstico antes y después | `historico-chat/scripts/2026-10-08/salida_diagnostico_sin_trabajo.txt` |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django; la base real para medir |
| Usuarios de prueba | Ninguno |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit y volver a correr `recalcular_trabajo`.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Aditiva. Después de desplegar, `manage.py recalcular_trabajo` una vez.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `02·F10`, `04·S18`, `00·N6`.

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
