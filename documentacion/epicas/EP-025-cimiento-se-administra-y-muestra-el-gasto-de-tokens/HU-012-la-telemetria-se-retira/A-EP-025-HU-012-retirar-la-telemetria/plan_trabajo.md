# Plan de Trabajo · Fase `A-EP-025-HU-012-retirar-la-telemetria` (módulo `proyectos/cimiento/core/consumo/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-012-retirar-la-telemetria` |
| **Épica** | [EP-025](../../epica.md) |
| **HU** | [HU-012](../HU-012-la-telemetria-se-retira.md), una sola (`F12.1`) |
| **Módulo** | `proyectos/cimiento/core/consumo/` |
| **Especificación del módulo** | Los CA de la [HU-012](../HU-012-la-telemetria-se-retira.md) |
| **Fecha apertura** | 2026-10-05 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): retiro de una funcionalidad. Sale del punto 4 del [análisis 2 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md).

**Carencias que cierra** (`02·F14` Q3): el gasto llega por dos caminos, y uno no aporta.

**Aprobación** (`02·F4`): [análisis 2 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md), el 2026-10-05, con la versión 54.4.0

**Disparo** (`02·F15`, etapa 2): el usuario pidió «continúe» el 2026-10-05, después de aprobar el análisis.

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-012 | Estado |
|---|---|
| CA-01 · No queda la telemetría en Cimiento | ☑ |
| CA-02 · La instalación la quita y no la vuelve a poner | ☑ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** quitar la telemetría de Cimiento y de la instalación.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Cimiento | Programa | Baja |
| CA-02 | Instalación | Programa | Baja |

**Fuera de alcance:** el campo `solicitud` de las llamadas.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Verificado el 2026-10-05, sobre la versión 55.0.0:

- La telemetría vive en `core/consumo/telemetria.py` (lector), `GuardadoDeTelemetria` en `guardar.py`, `RecibirEventos` en `views.py`, la ruta `v1/logs` en `urls.py`, y sus pruebas en `tests_telemetria.py` y en una prueba de `tests_segunda_tanda.py`.
- `Instalador.activar_telemetria` pone seis variables en `~/.claude/settings.json`, con los valores de `Instalador.telemetria()`; `Desinstalador.quitar_telemetria` ya las quita con el mismo criterio. Sus pruebas: `ActivarLaTelemetria` en `tests_instalacion.py`.
- `guardar_llamada` une por `solicitud` lo que llegaba por los dos caminos; el `.jsonl` también trae `requestId`, así que el campo se sigue llenando.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/consumo/telemetria.py`, `proyectos/cimiento/core/consumo/tests_telemetria.py` | Borrar | Programa | |
| `proyectos/cimiento/core/consumo/views.py`, `proyectos/cimiento/core/consumo/urls.py`, `proyectos/cimiento/core/consumo/guardar.py`, `proyectos/cimiento/core/consumo/lector.py`, `proyectos/cimiento/core/consumo/tests_segunda_tanda.py` | Modificar | Programa | Sin la ruta, la vista, el guardado ni su prueba |
| `proyectos/cimiento/core/consumo/tests_vigilante.py` | Modificar | Pruebas | La prueba de que la ruta ya no existe |
| `proyectos/cimiento/core/herramientas/instalar.py`, `proyectos/cimiento/core/herramientas/desinstalar.py`, `proyectos/cimiento/core/herramientas/tests_instalacion.py` | Modificar | Programa | `retirar_telemetria` en vez de `activar_telemetria` |
| `CHANGELOG.md` | Modificar | Registro | Lo de las HU-011 y HU-012 en la 55.0.0, que no se ha publicado |
| `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-007-el-gasto-llega-a-cimiento-en-vivo/HU-007-el-gasto-llega-a-cimiento-en-vivo.md` | Modificar | Documentación | Su bitácora dice que se retiró |
| `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-012-la-telemetria-se-retira/HU-012-la-telemetria-se-retira.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | Modificar | Documentación | La fila de la fase y el estado |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| Sale `GuardadoDeTelemetria` | `views.py`, `tests_segunda_tanda.py` | Salen con él |
| `activar_telemetria` pasa a `retirar_telemetria` | `Instalador.instalar`, `Desinstalador.quitar_telemetria` | El desinstalador la llama |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

Sale `POST /v1/logs`.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

Ninguno.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Lo guardado por la telemetría se queda | Borrarlo | Es gasto real | Propuesta del agente |
| Se queda `solicitud` | Una migración que lo quite | El `.jsonl` lo llena; quitarlo no aporta | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  `02·F30`

| Acción nueva | Su contraria | Prueba |
|---|---|---|
| Retirar las seis variables | No tiene: la telemetría se retira por acuerdo (análisis 2, acuerdo 2), que es lo que aprueba quedar sin contraria | CP-002 |

## 3. Desglose de tareas por criterio de aceptación

### CA-01 · No queda la telemetría en Cimiento

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | Borrar el lector y su prueba; sacar la ruta, la vista, el guardado y su prueba | `proyectos/cimiento/core/consumo/` | CA-01 | Cimiento | 0,5 h | Ninguna | CP-001 |

### CA-02 · La instalación la quita y no la vuelve a poner

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-02 | `retirar_telemetria`; el desinstalador la usa | `proyectos/cimiento/core/herramientas/instalar.py`, `proyectos/cimiento/core/herramientas/desinstalar.py` | CA-02 | Instalación | 0,5 h | Ninguna | CP-002 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-03 | Pruebas, retirar en esta máquina, registro de cambios, nota en la HU-007 y cierre con `cerrar_fase` | `proyectos/cimiento/core/herramientas/tests_instalacion.py`, `proyectos/cimiento/core/consumo/tests_vigilante.py`, `CHANGELOG.md`, la HU-007, la HU y la épica | CA-01, CA-02 | Documentación | 0,5 h | T-01, T-02 | CP-001, CP-002 |

## 4. Secuencia de ejecución

T-01 a T-03.

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | `/v1/logs` no existe; las pruebas de consumo | CP-001 |
| CA-02 | Una configuración temporal con las seis y otras | CP-002 |

## 6. Datos y ambiente de prueba

La base de pruebas y archivos temporales.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

La instalación del estándar quita las variables donde quedaron.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`02·F30`, `02·F4`, `02·F5`, `02·F8`, `00·ID8`, `00·ID9`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Quitar una variable del usuario | Solo la que tiene el valor exacto |

## 11. Definition of Done

- [ ] CA-01 y CA-02 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Las pruebas de la fase sin fallas, y cero marcas nuevas.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Las 3 tareas quedaron hechas el 2026-10-05, con la versión 55.0.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** ninguno.
