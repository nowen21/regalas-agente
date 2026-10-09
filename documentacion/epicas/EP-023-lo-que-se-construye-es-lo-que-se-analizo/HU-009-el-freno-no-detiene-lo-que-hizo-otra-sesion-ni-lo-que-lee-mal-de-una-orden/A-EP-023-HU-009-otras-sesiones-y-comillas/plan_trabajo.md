# Plan de Trabajo · Fase A-EP-023-HU-009-otras-sesiones-y-comillas (módulo freno)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-023-HU-009-otras-sesiones-y-comillas` |
| **Épica** | `EP-023` |
| **HU** | [`HU-009`](../HU-009-el-freno-no-detiene-lo-que-hizo-otra-sesion-ni-lo-que-lee-mal-de-una-orden.md), una sola (`F12.1`) |
| **Módulo** | Freno: `proyectos/cimiento/core/enganches/freno.py` y `adaptadores/claude-code/hook_despues.py` |
| **Especificación del módulo** | La HU-009 y la [épica EP-023](../../epica.md) |
| **Fecha apertura** | 2026-10-09 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 4 del pendiente 133](../../../../../historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-4.md), el 2026-10-09, en el turno 61, con la versión 59.3.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): retoma `A-EP-023-HU-007`, que puso el freno antes y después de cada orden, y le corrige dos casos que detenían trabajo permitido (análisis 4 del pendiente 133, acuerdos 1 y 2).

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-009` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-009-el-freno-no-detiene-lo-que-hizo-otra-sesion-ni-lo-que-lee-mal-de-una-orden.md#ca-01--lo-que-hizo-otra-sesión-no-detiene-a-esta) | ☐ |
| [CA-02](../HU-009-el-freno-no-detiene-lo-que-hizo-otra-sesion-ni-lo-que-lee-mal-de-una-orden.md#ca-02--la-orden-se-parte-solo-fuera-de-las-comillas) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** el freno no cuenta como de esta sesión un archivo que otra sesión activa nombra en lo que hizo, y parte las órdenes solo por los separadores que están fuera de comillas.

**Fuera de alcance:** resolver variables de la consola.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`Freno.fuera_del_plan` (`core/enganches/freno.py`) compara la foto de antes con `Freno.cambiados` y cuenta todo lo nuevo. `Freno.partes` corta la orden con una expresión que no mira las comillas. `hook_despues.py` recibe de Claude Code la entrada con `transcript_path`, la transcripción de la propia sesión; las de las otras sesiones del proyecto están en la misma carpeta, con extensión `.jsonl`.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/enganches/freno.py` | Modificar | Lógica | `partes` respeta las comillas; `fuera_del_plan` descarta lo que nombra otra sesión |
| `adaptadores/claude-code/hook_despues.py` | Modificar | Enganche | Le pasa al freno la transcripción de la sesión |
| `proyectos/cimiento/core/enganches/tests_freno_otras_sesiones.py` | Crear | Test | |

### 2.2 Matriz de dependencias del refactor

`Freno.partes` la usan `destinos` y las pruebas de `tests_freno.py`; se corren todas.

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

No aplica.

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Se busca la ruta del archivo en el final de las transcripciones de las otras sesiones escritas en los últimos 10 minutos | Leer el registro de cada turno | El registro se escribe al terminar el turno de la otra sesión, cuando ya es tarde | Propuesta del agente |
| Se leen los últimos 2 MB de cada transcripción | Leerlas enteras | Pueden pesar decenas de megas y el freno corre en cada orden | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

No aplica: no crea nada que haya que deshacer.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Descartar lo que nombra otra sesión | Lógica | 0,5 h | — | EV-01 |
| T-02 | Partir respetando las comillas | Lógica | 0,3 h | — | EV-01 |
| T-03 | Pruebas | Test | 0,5 h | T-01, T-02 | EV-01 |

**Total estimado:** 1,3 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Pruebas de Django | EV-01 | | ☐ |
| CA-02 | Pruebas de Django | EV-01 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | Carpetas temporales con transcripciones de prueba |
| Usuarios de prueba | Ninguno |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

No aplica.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `08·T1`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Otra sesión nombró el archivo sin escribirlo | Ese cambio no se detiene | El plazo de 10 minutos lo limita | Abierto |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno todavía.
