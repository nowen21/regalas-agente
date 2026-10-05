# Plan de Trabajo · Fase `A-EP-025-HU-006-lectura-de-los-jsonl` (módulo `proyectos/cimiento/core/consumo/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-006-lectura-de-los-jsonl` |
| **Épica** | [EP-025](../../epica.md) |
| **HU** | [HU-006](../HU-006-el-gasto-de-cada-llamada-queda-guardado.md), una sola (`F12.1`) |
| **Módulo** | `proyectos/cimiento/core/consumo/`, `adaptadores/claude-code/hook_presupuesto.py`, `proyectos/cimiento/core/herramientas/` |
| **Especificación del módulo** | Los CA de la [HU-006](../HU-006-el-gasto-de-cada-llamada-queda-guardado.md) |
| **Fecha apertura** | 2026-10-05 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva. Sale de los puntos 5 y 6 del [análisis 1 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md) (acuerdos 7, 8 y 9).

**Carencias que cierra** (`02·F14` Q3): el gasto de tokens no se guarda, no se separa por proyecto, enganche ni archivo, y se pierde a los 30 días.

**Aprobación** (`02·F4`): [análisis 1 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md), el 2026-10-04, con la versión 54.2.0

**Disparo** (`02·F15`, etapa 2): el usuario aprobó el análisis el 2026-10-04 y pidió seguir con «Continúe con el pendiente 119».

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-006 | Estado |
|---|---|
| CA-01 · Las llamadas de un proyecto quedan guardadas | ☐ |
| CA-02 · Leer otra vez no duplica | ☐ |
| CA-03 · Una línea rota no tumba la lectura | ☐ |
| CA-04 · La suma es la de siempre y la lectura queda programada | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** guardar en la base de Cimiento cada llamada, cada enganche y cada archivo leído de los `.jsonl` de Claude Code, desde donde quedó la lectura anterior.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Lectura y guardado | Programa | Alta |
| CA-02 | Sin duplicar | Programa | Media |
| CA-03 | Líneas rotas | Programa | Baja |
| CA-04 | Suma y programación | Programa | Media |

**Fuera de alcance:** agentes auxiliares y demás niveles (HU-010); telemetría (HU-007).

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-10-05, sobre la versión 54.2.0:

- `~/.claude/projects/` tiene 385 MB en 58 `.jsonl`; 32 en la primera altura y el resto en `«sesión»/subagents/`.
- En el `.jsonl`: las llamadas son líneas `assistant` con `message.id`, `message.model` y `message.usage` (`input_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens`, `output_tokens`); una llamada ocupa varias líneas con el mismo `id` y el mismo `usage` (sesión `c3d82767`: 619 líneas, 208 llamadas).
- Los enganches son líneas `attachment` de tipo `hook_additional_context` (lo que llega al modelo, sin nombre del enganche), `hook_success` (con `command`, que es el mensaje de estado del enganche, y `stdout`) y `hook_blocking_error` (con `blockingError`); comparten `toolUseID` y `hookName`.
- Un archivo leído es un `tool_use` de `Read` (con `input.file_path`) y su `tool_result` en una línea `user`, unidos por el `id`.
- `hook_presupuesto.py` suma por línea y cuenta cada llamada unas tres veces. `presupuesto.py` (`Presupuesto.resumen`, `como_texto`) suma lo que se le dé.
- `core/proyectos/claude.py` (HU-003) da la carpeta de Claude Code de cada proyecto.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/consumo/__init__.py`, `proyectos/cimiento/core/consumo/apps.py`, `proyectos/cimiento/core/consumo/lector.py`, `proyectos/cimiento/core/consumo/models.py`, `proyectos/cimiento/core/consumo/guardar.py`, `proyectos/cimiento/core/consumo/tests.py` | Crear | Programa | El módulo de consumo |
| `proyectos/cimiento/core/consumo/migrations/__init__.py`, `proyectos/cimiento/core/consumo/migrations/0001_initial.py` | Crear | Datos | Llamadas, enganches, archivos leídos y avance |
| `proyectos/cimiento/core/consumo/management/__init__.py`, `proyectos/cimiento/core/consumo/management/commands/__init__.py`, `proyectos/cimiento/core/consumo/management/commands/leer_consumo.py` | Crear | Programa | La orden de lectura |
| `proyectos/cimiento/config/settings/base.py` | Modificar | Configuración | La aplicación |
| `adaptadores/claude-code/hook_presupuesto.py` | Modificar | Enganche | Usa el lector: una llamada cuenta una vez |
| `proyectos/cimiento/core/herramientas/instalar.py`, `proyectos/cimiento/core/herramientas/tests_instalacion.py`, `validadores/instalar.py` | Modificar | Programa | Programar la lectura una vez al día |
| `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-006-el-gasto-de-cada-llamada-queda-guardado/HU-006-el-gasto-de-cada-llamada-queda-guardado.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | Modificar | Documentación | La fila de la fase y el estado |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| `consumos_de_transcripcion()` de `hook_presupuesto.py` cuenta llamadas, no líneas | El propio enganche (aviso por tramo, `EP-005·HU-014`) | El total baja a lo real; el tramo se cruza cuando de verdad se gastó |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica: la pantalla es la HU-008.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Una llamada se identifica por `message.id` y vale su última línea | Contar cada línea | Una llamada ocupa varias líneas | Medición del 2026-10-05 |
| Enganche: cuenta lo que llega al modelo (`hook_additional_context`, `hook_blocking_error`); el nombre sale del `command` del `hook_success` hermano | Contar también el `stdout` | El `stdout` repite el mismo texto dentro de su JSON | Medición del 2026-10-05 |
| Tokens estimados de enganches y archivos: caracteres entre 3,5, en una sola constante | Contar con un tokenizador | Claude Code no da esos tokens y el tokenizador no es público; queda marcado como estimación | Propuesta del agente |
| El avance se guarda por archivo en bytes; la última línea sin salto no se cuenta como leída | Releer todo | Claude Code puede estar escribiendo esa línea | Acuerdo 9 |
| No se guarda texto: solo tamaños, nombres y rutas | Guardar los mensajes | Privacidad (capítulo `12`) y tamaño | Acuerdo 8 |
| Programar con `schtasks` en Windows; en otro sistema se dice cómo hacerlo | Un proceso que quede corriendo | La instalación no deja procesos vivos (`04·S10`) | Punto 6 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| Gasto de tokens | Solo en los `.jsonl`, 30 días | En la base de Cimiento, por proyecto, sesión, enganche y archivo | Acuerdos 7 y 8 |
| Suma de la sesión | Por línea, tres veces de más | Por llamada | `07·Q4` |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-01 · Las llamadas de un proyecto quedan guardadas

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | `LectorDeClaudeCode`: de un `.jsonl` desde un byte, saca llamadas, enganches y archivos leídos, sin Django | `proyectos/cimiento/core/consumo/lector.py` | CA-01 | HU-007 a HU-010 | 2 h | Ninguna | CP-001 |
| T-02 | Modelos `Llamada`, `GastoDeEnganche`, `GastoDeArchivo` y `AvanceDeLectura`, y su migración | `proyectos/cimiento/core/consumo/__init__.py`, `proyectos/cimiento/core/consumo/apps.py`, `proyectos/cimiento/core/consumo/models.py`, `proyectos/cimiento/core/consumo/migrations/__init__.py`, `proyectos/cimiento/core/consumo/migrations/0001_initial.py`, `proyectos/cimiento/config/settings/base.py` | CA-01 | La base | 1 h | Ninguna | CP-001 |
| T-03 | `GuardadoDeConsumo` y la orden `leer_consumo` | `proyectos/cimiento/core/consumo/guardar.py`, `proyectos/cimiento/core/consumo/management/__init__.py`, `proyectos/cimiento/core/consumo/management/commands/__init__.py`, `proyectos/cimiento/core/consumo/management/commands/leer_consumo.py` | CA-01, CA-02 | Cimiento | 2 h | T-01, T-02 | CP-001, CP-002 |

### CA-02 · Leer otra vez no duplica

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-04 | Únicos por sesión y mensaje o identificador; avance por archivo; un archivo sin cambios no se abre | `proyectos/cimiento/core/consumo/models.py`, `proyectos/cimiento/core/consumo/guardar.py` | CA-02 | La base | 1 h | T-03 | CP-002 |

### CA-03 · Una línea rota no tumba la lectura

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-05 | Línea ilegible se salta; la última sin salto queda para la próxima | `proyectos/cimiento/core/consumo/lector.py` | CA-03 | La lectura | 0,5 h | T-01 | CP-003 |

### CA-04 · La suma es la de siempre y la lectura queda programada

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-06 | `hook_presupuesto.py` saca los consumos del lector | `adaptadores/claude-code/hook_presupuesto.py` | CA-04 | El aviso por tramo | 0,5 h | T-01 | CP-004 |
| T-07 | `Instalador.programar_lectura(aplicar)` | `proyectos/cimiento/core/herramientas/instalar.py`, `validadores/instalar.py` | CA-04 | La instalación del estándar | 1 h | T-03 | CP-004 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-08 | Pruebas; fila de la fase en la HU y estado en la épica | `proyectos/cimiento/core/consumo/tests.py`, `proyectos/cimiento/core/herramientas/tests_instalacion.py`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-006-el-gasto-de-cada-llamada-queda-guardado/HU-006-el-gasto-de-cada-llamada-queda-guardado.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | CA-01 a CA-04 | Documentación | 1,5 h | T-01 a T-07 | CP-001 a CP-004 |

## 4. Secuencia de ejecución

T-01 y T-02; T-05, T-03, T-04, T-06, T-07 y al final T-08, con las pruebas de la fase (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | Un `.jsonl` de muestra con llamadas, enganches y un archivo leído; la orden sobre la carpeta de muestra; la orden real | CP-001 |
| CA-02 | Leer dos veces, y otra vez con líneas nuevas | CP-002 |
| CA-03 | Línea ilegible y línea final sin salto | CP-003 |
| CA-04 | La suma de la sesión con una llamada partida; el paso de programar | CP-004 |

## 6. Datos y ambiente de prueba

`.jsonl` de muestra armados en las pruebas, en carpetas temporales; la base de pruebas en MariaDB.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase y `manage.py migrate consumo zero`; la tarea programada se borra con `schtasks /Delete /TN "Cimiento leer consumo" /F`.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Aditiva: tablas nuevas. El aviso por tramo cambia: cuenta lo real, así que sale menos.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`03·D6`, `07·Q4`, `04·S10`, `12`, `02·F4`, `02·F5`, `02·F8`, `00·ID8`, `00·ID9`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Claude Code cambie el formato | El lector va aparte; lo que no entiende se salta |
| La estimación por caracteres se aleje | Una sola constante, marcada como estimación |

## 11. Definition of Done

- [ ] CA-01 a CA-04 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Las pruebas de la fase sin fallas, y cero marcas nuevas.

## 12. Seguimiento diario

N/A.

## 13. Cierre

«Se llena al cerrar la fase.»
