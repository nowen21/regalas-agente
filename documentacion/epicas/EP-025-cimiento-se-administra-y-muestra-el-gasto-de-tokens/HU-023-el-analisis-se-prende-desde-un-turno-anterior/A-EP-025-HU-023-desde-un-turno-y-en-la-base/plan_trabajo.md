# Plan de Trabajo · Fase `A-EP-025-HU-023-desde-un-turno-y-en-la-base` (módulo `proyectos/cimiento/core/enganches/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-023-desde-un-turno-y-en-la-base` |
| **Épica** | [EP-025](../../epica.md) |
| **HU** | [HU-023](../HU-023-el-analisis-se-prende-desde-un-turno-anterior.md), una sola (`F12.1`) |
| **Módulo** | `proyectos/cimiento/core/enganches/` |
| **Especificación del módulo** | Los CA de la [HU-023](../HU-023-el-analisis-se-prende-desde-un-turno-anterior.md) |
| **Fecha apertura** | 2026-10-05 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva. Sale del punto 10 del [análisis 3 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md).

**Carencias que cierra** (`02·F14` Q3): el análisis prende solo desde el turno actual, y su estado es un archivo que hubo que editar a mano.

**Aprobación** (`02·F4`): [análisis 3 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md), el 2026-10-05, con la versión 54.3.0

**Disparo** (`02·F15`, etapa 2): el usuario pidió «continúe» el 2026-10-05, después de aprobar el análisis.

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-023 | Estado |
|---|---|
| CA-01 · Prender desde un turno anterior | ☑ |
| CA-02 · El estado vive en la base | ☑ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** «desde el turno T» al prender, y el estado del análisis prendido en la base de Cimiento.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Desde un turno | Programa | Baja |
| CA-02 | En la base | Programa | Alta |

**Fuera de alcance:** que el freno lea el estado de su sesión (HU-024).

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Verificado el 2026-10-05, sobre la versión 55.0.0:

- `AnalisisEnCurso` guarda el estado en `historico-chat/.estado/analisis-en-curso/«sesión».txt`, o en el archivo único `analisis-en-curso.txt` si es de esa sesión o no se dice la sesión. Lo usan `hook_analisis.py`, `hook_historico.py`, `Freno`, `Acuerdos` y el validador del análisis.
- `prender(numero, transcripcion, turno)` guarda `desde=turno`; `hook_analisis.py` lo llama con el turno actual.
- El freno lee sin sesión, así que ve el archivo único (H-8 del resumen del 2026-10-04, sesión 3).
- `NivelesDelProyecto` (`core/enganches/niveles.py`) lee la base con PyMySQL, sin Django, con la conexión del `.env` de Cimiento.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/enganches/analisis_en_curso.py` | Modificar | Programa | «desde» y el estado en la base |
| `proyectos/cimiento/core/enganches/estado_en_base.py` | Crear | Programa | La lectura y escritura con PyMySQL |
| `proyectos/cimiento/core/proyectos/models.py`, `proyectos/cimiento/core/proyectos/migrations/0003_analisisprendido.py` | Modificar, crear | Datos | El modelo `AnalisisPrendido` |
| `adaptadores/claude-code/hook_analisis.py` | Modificar | Programa | Le pasa a `prender` el turno pedido |
| `proyectos/cimiento/core/enganches/tests_analisis_desde.py`, `proyectos/cimiento/core/proyectos/tests_analisis_prendido.py` | Crear | Pruebas | |
| `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-023-el-analisis-se-prende-desde-un-turno-anterior/HU-023-el-analisis-se-prende-desde-un-turno-anterior.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | Modificar | Documentación | La fila de la fase y el estado |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| `leer_estado`, `guardar_estado`, `borrar_estado` y `estados` leen la base si el proyecto está registrado | Los enganches, el freno, los acuerdos y el validador | Sin registro siguen con archivos; se corren `tests_analisis_en_curso` y `tests_freno` |
| `prender` recibe `desde` | `hook_analisis.py` | Sin `desde`, igual que antes |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

El mensaje «Analicemos: el pendiente N desde el turno T».

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Solo un proyecto registrado y con base usa la tabla; si no, el archivo | Siempre la base | El histórico no se puede caer, y las pruebas con carpetas temporales no deben escribir en la base real | Propuesta del agente |
| Sin sesión, se lee la fila más reciente del proyecto | No leer nada | Es lo que hacía el archivo único; el freno lee así hasta la HU-024 | Propuesta del agente |
| El modelo va en `core.proyectos` | Una aplicación nueva | Es estado de un proyecto | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  `02·F30`

| Acción nueva | Su contraria | Prueba |
|---|---|---|
| Prender desde un turno | Pausar y apagar, que ya existen; volver a prender desde otro turno lo corre | CP-001 |
| Pasar el estado del archivo a la base | Sin base o sin registro, el estado vuelve a escribirse en archivo | CP-002 |

## 3. Desglose de tareas por criterio de aceptación

### CA-01 · Prender desde un turno anterior

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | `turno_pedido(mensaje)` y `prender(..., desde)`; el enganche lo pasa | `proyectos/cimiento/core/enganches/analisis_en_curso.py`, `adaptadores/claude-code/hook_analisis.py` | CA-01 | Enganches | 1 h | Ninguna | CP-001 |

### CA-02 · El estado vive en la base

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-02 | El modelo `AnalisisPrendido` y su migración | `proyectos/cimiento/core/proyectos/models.py`, `proyectos/cimiento/core/proyectos/migrations/0003_analisisprendido.py` | CA-02 | Base | 0,5 h | Ninguna | CP-002 |
| T-03 | `EstadoEnBase`: leer, guardar, borrar y listar, y pasar a la base lo que quedó en archivo | `proyectos/cimiento/core/enganches/estado_en_base.py` | CA-02 | Enganches | 1,5 h | T-02 | CP-002 |
| T-04 | `AnalisisEnCurso` usa la base si el proyecto está registrado | `proyectos/cimiento/core/enganches/analisis_en_curso.py` | CA-02 | Enganches | 1 h | T-03 | CP-002 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-05 | Pruebas, migración en la base real y cierre con `cerrar_fase` | `proyectos/cimiento/core/enganches/tests_analisis_desde.py`, `proyectos/cimiento/core/proyectos/tests_analisis_prendido.py`, la HU y la épica | CA-01, CA-02 | Documentación | 1 h | T-01 a T-04 | CP-001, CP-002 |

## 4. Secuencia de ejecución

T-01 a T-05.

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | Prender desde un turno en una carpeta temporal | CP-001 |
| CA-02 | Proyecto registrado en la base de pruebas | CP-002 |

## 6. Datos y ambiente de prueba

Carpetas temporales; la base de pruebas de Django en MariaDB.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit; la migración `0003` se deshace con `migrate proyectos 0002`. Los estados que estén en la base se pierden al deshacerla: se apaga el análisis antes.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

`preparar_base` aplica la `0003`. Los estados en archivo pasan solos a la base al leerse.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`02·F30`, `03·D2`, `02·F4`, `02·F5`, `02·F8`, `00·ID8`, `00·ID9`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| El histórico se cae sin base | Sin base, archivo |
| Las pruebas escriben en la base real | Solo un proyecto registrado usa la base |

## 11. Definition of Done

- [ ] CA-01 y CA-02 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Las pruebas de la fase sin fallas, y cero marcas nuevas.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Las 5 tareas quedaron hechas el 2026-10-05, con la versión 55.0.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** ninguno.
