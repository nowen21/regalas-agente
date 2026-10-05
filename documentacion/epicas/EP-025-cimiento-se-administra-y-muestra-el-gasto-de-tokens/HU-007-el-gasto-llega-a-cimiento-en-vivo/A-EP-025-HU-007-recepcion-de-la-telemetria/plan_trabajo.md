# Plan de Trabajo · Fase `A-EP-025-HU-007-recepcion-de-la-telemetria` (módulo `proyectos/cimiento/core/consumo/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-007-recepcion-de-la-telemetria` |
| **Épica** | [EP-025](../../epica.md) |
| **HU** | [HU-007](../HU-007-el-gasto-llega-a-cimiento-en-vivo.md), una sola (`F12.1`) |
| **Módulo** | `proyectos/cimiento/core/consumo/`, `proyectos/cimiento/core/herramientas/` |
| **Especificación del módulo** | Los CA de la [HU-007](../HU-007-el-gasto-llega-a-cimiento-en-vivo.md) |
| **Fecha apertura** | 2026-10-05 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva. Sale del punto 7 del [análisis 1 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md) (acuerdo 9).

**Carencias que cierra** (`02·F14` Q3): el gasto llega a Cimiento solo con la lectura diaria de los `.jsonl`.

**Aprobación** (`02·F4`): [análisis 1 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md), el 2026-10-04, con la versión 54.2.0

**Disparo** (`02·F15`, etapa 2): el usuario pidió «continúe» el 2026-10-05, después de cerrar las HU-003, 004 y 006.

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-007 | Estado |
|---|---|
| CA-01 · Una llamada llega y queda guardada | ☐ |
| CA-02 · Lo que no vale no se guarda | ☐ |
| CA-03 · La misma llamada por los dos caminos cuenta una vez | ☐ |
| CA-04 · La instalación activa la telemetría | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** recibir en Cimiento los eventos de telemetría de Claude Code y guardarlos en las tablas de la HU-006, sin duplicar lo que trae el `.jsonl`.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Recepción y guardado | Programa | Media |
| CA-02 | Envíos rechazados | Programa | Baja |
| CA-03 | Los dos caminos | Programa | Media |
| CA-04 | Activar en la instalación | Programa | Baja |

**Fuera de alcance:** el tablero (HU-008); las métricas de OpenTelemetry; prender Cimiento al encender la máquina.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Verificado el 2026-10-05, sobre la versión 54.2.0:

- La documentación de Claude Code (`monitoring-usage`): con `OTEL_LOGS_EXPORTER=otlp` y `OTEL_EXPORTER_OTLP_PROTOCOL=http/json`, los eventos llegan en `POST «dirección»/v1/logs` (o a `OTEL_EXPORTER_OTLP_LOGS_ENDPOINT`), cada 5 segundos. El nombre va en el atributo `event.name` (`claude_code.api_request`, `claude_code.tool_result`). `api_request` trae `session.id`, `request_id`, `model`, `input_tokens`, `output_tokens`, `cache_read_tokens`, `cache_creation_tokens` y `event.timestamp`. `tool_result` trae `tool_name`, `tool_use_id`, `tool_result_size_bytes` y, con `OTEL_LOG_TOOL_DETAILS=1`, `tool_parameters`.
- `CLAUDE_CODE_ENABLE_TELEMETRY` y las variables del exportador se ignoran en la configuración de un repositorio; valen en `~/.claude/settings.json`, que hoy no tiene bloque `env`.
- En el `.jsonl` de la sesión `c3d82767`: 816 líneas `assistant`, 286 mensajes, cada `message.id` con un solo `requestId`.
- `Llamada` es única por sesión y mensaje (HU-006). `GastoDeArchivo` usa el `tool_use_id` como identificador: es el mismo de `tool_result`.
- `manage.py` levanta `runserver` en el `PUERTO` del `.env` (8015 en esta máquina); `config/ambiente.py` lo lee sin tocar el ambiente (`leer`).
- `LoginRequiredMiddleware` pide cuenta en toda ruta; Django 5.2 tiene `login_not_required`.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/consumo/telemetria.py`, `proyectos/cimiento/core/consumo/views.py`, `proyectos/cimiento/core/consumo/urls.py`, `proyectos/cimiento/core/consumo/tests_telemetria.py` | Crear | Programa | Leer el envío, la ruta y sus pruebas |
| `proyectos/cimiento/core/consumo/migrations/0002_llamada_solicitud.py` | Crear | Datos | La solicitud de cada llamada |
| `proyectos/cimiento/core/consumo/models.py`, `proyectos/cimiento/core/consumo/lector.py`, `proyectos/cimiento/core/consumo/guardar.py` | Modificar | Programa | La solicitud, y guardar sin duplicar por los dos caminos |
| `proyectos/cimiento/config/urls.py` | Modificar | Configuración | La ruta `/v1/logs` |
| `proyectos/cimiento/core/herramientas/instalar.py`, `proyectos/cimiento/core/herramientas/tests_instalacion.py`, `validadores/instalar.py` | Modificar | Programa | Activar la telemetría |
| `proyectos/cimiento/README.md` | Modificar | Documentación | Cimiento prendido recibe el gasto en vivo |
| `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-007-el-gasto-llega-a-cimiento-en-vivo/HU-007-el-gasto-llega-a-cimiento-en-vivo.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | Modificar | Documentación | La fila de la fase y el estado |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| `Llamada` del lector suma `solicitud` | `guardar.py`, `hook_presupuesto.py` (solo `como_consumo`) | Campo con valor por defecto: `hook_presupuesto.py` no cambia |
| El guardado del `.jsonl` busca primero por solicitud | `leer_consumo` | Las pruebas de la HU-006 se vuelven a correr |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

| Ruta | Vista | Acceso |
|---|---|---|
| `POST /v1/logs` | `RecibirEventos` | Sin cuenta, solo desde la misma máquina (`127.0.0.1` o `::1`); sin CSRF, porque no la llama un navegador |

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| La llamada que llega por telemetría se guarda con `mensaje` igual al `request_id`; cuando el `.jsonl` la encuentra por `solicitud`, le pone el `message.id` | Esperar al `.jsonl` | Así se ve en vivo y no se duplica | Acuerdo 9, `03·D6` |
| El proyecto sale de la sesión, buscando `«sesión».jsonl` en la carpeta de Claude Code de cada proyecto activo | Mandar la carpeta con `OTEL_RESOURCE_ATTRIBUTES` | Esa variable es de toda la máquina y no sabe en qué carpeta se abrió cada sesión | Propuesta del agente |
| El archivo leído por telemetría se mide en bytes (`tool_result_size_bytes`); la lectura del `.jsonl` lo corrige a caracteres | Dejar los bytes | La HU-006 mide en caracteres | Propuesta del agente |
| La instalación agrega en `env` solo las claves que falten; nunca pisa una que el usuario ya tenga | Escribir todas | La configuración es del usuario | RN-05 |
| `OTEL_METRICS_EXPORTER=none` | Recibir también métricas | Repiten lo de los eventos y Cimiento no tiene ruta para ellas | Propuesta del agente |
| Responder `{}` con 200 aunque se descarte un evento sin proyecto | Responder error | Un error haría que Claude Code reintente lo que nunca va a entrar | OTLP/HTTP |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| Gasto en la base de Cimiento | Una vez al día | A los 5 segundos, con Cimiento prendido | Acuerdo 9 |
| `~/.claude/settings.json` | Sin `env` | Con las variables de la telemetría | Punto 7 |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-01 · Una llamada llega y queda guardada

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | `EventosDeTelemetria`: de un envío OTLP JSON saca llamadas y archivos leídos, con las clases del lector, sin Django | `proyectos/cimiento/core/consumo/telemetria.py`, `proyectos/cimiento/core/consumo/lector.py` | CA-01 | HU-008 | 1,5 h | Ninguna | CP-001 |
| T-02 | `solicitud` en `Llamada` y su migración; el lector del `.jsonl` la saca de `requestId` | `proyectos/cimiento/core/consumo/models.py`, `proyectos/cimiento/core/consumo/lector.py`, `proyectos/cimiento/core/consumo/migrations/0002_llamada_solicitud.py` | CA-01, CA-03 | La base | 0,5 h | Ninguna | CP-001 |
| T-03 | `RecibirEventos` en `/v1/logs` y `GuardadoDeTelemetria` | `proyectos/cimiento/core/consumo/views.py`, `proyectos/cimiento/core/consumo/urls.py`, `proyectos/cimiento/core/consumo/guardar.py`, `proyectos/cimiento/config/urls.py` | CA-01 | Cimiento | 1,5 h | T-01, T-02 | CP-001 |

### CA-02 · Lo que no vale no se guarda

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-04 | 403 desde otra máquina, 400 con JSON roto; sesión sin proyecto se descarta | `proyectos/cimiento/core/consumo/views.py`, `proyectos/cimiento/core/consumo/guardar.py` | CA-02 | La ruta | 0,5 h | T-03 | CP-002 |

### CA-03 · La misma llamada por los dos caminos cuenta una vez

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-05 | Los dos guardados buscan primero por sesión y solicitud | `proyectos/cimiento/core/consumo/guardar.py` | CA-03 | La base | 1 h | T-03 | CP-003 |

### CA-04 · La instalación activa la telemetría

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-06 | `Instalador.activar_telemetria(aplicar, configuracion)`; la instalación del propio estándar lo llama | `proyectos/cimiento/core/herramientas/instalar.py`, `validadores/instalar.py` | CA-04 | `~/.claude/settings.json` | 1 h | Ninguna | CP-004 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-07 | Pruebas; README; fila de la fase en la HU y estado en la épica | `proyectos/cimiento/core/consumo/tests_telemetria.py`, `proyectos/cimiento/core/herramientas/tests_instalacion.py`, `proyectos/cimiento/README.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-007-el-gasto-llega-a-cimiento-en-vivo/HU-007-el-gasto-llega-a-cimiento-en-vivo.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | CA-01 a CA-04 | Documentación | 1 h | T-01 a T-06 | CP-001 a CP-004 |

## 4. Secuencia de ejecución

T-01 y T-02; T-03, T-04, T-05; T-06 y al final T-07, con las pruebas de la fase (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | Un envío de muestra con una llamada y un `Read`, por la ruta | CP-001 |
| CA-02 | Otra máquina, JSON roto, sesión sin proyecto | CP-002 |
| CA-03 | Telemetría y después `.jsonl`; `.jsonl` y después telemetría; el mismo envío dos veces | CP-003 |
| CA-04 | Configuración sin `env`, con claves propias, y en simulación | CP-004 |

## 6. Datos y ambiente de prueba

Envíos OTLP JSON armados en las pruebas con los nombres de la documentación; `.jsonl` de muestra en carpetas temporales; la base de pruebas en MariaDB.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase y `manage.py migrate consumo 0001`; quitar del `env` de `~/.claude/settings.json` las claves `CLAUDE_CODE_ENABLE_TELEMETRY` y `OTEL_*`.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Aditiva: un campo nuevo que acepta vacío. Las llamadas ya guardadas lo llenan en la siguiente lectura de su `.jsonl` solo si el archivo cambia; no hace falta, porque la telemetría solo trae llamadas nuevas.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`03·D6`, `04`, `12`, `00·N6` (la telemetría no lleva claves), `02·F4`, `02·F5`, `02·F8`, `00·ID8`, `00·ID9`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Claude Code cambie los nombres de los atributos | Los nombres viven en `telemetria.py`; lo que no entiende se salta |
| Cimiento apagado | El `.jsonl` recupera lo perdido |

## 11. Definition of Done

- [ ] CA-01 a CA-04 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Las pruebas de la fase sin fallas, y cero marcas nuevas.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Las 7 tareas quedaron hechas el 2026-10-05, con la versión 54.2.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** ninguno.
