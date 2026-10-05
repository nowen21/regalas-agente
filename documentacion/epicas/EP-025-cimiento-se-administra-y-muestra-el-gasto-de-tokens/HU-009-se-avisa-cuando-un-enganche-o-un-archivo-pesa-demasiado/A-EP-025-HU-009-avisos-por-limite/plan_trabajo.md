# Plan de Trabajo · Fase `A-EP-025-HU-009-avisos-por-limite` (módulo `proyectos/cimiento/core/enganches/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-009-avisos-por-limite` |
| **Épica** | [EP-025](../../epica.md) |
| **HU** | [HU-009](../HU-009-se-avisa-cuando-un-enganche-o-un-archivo-pesa-demasiado.md), una sola (`F12.1`) |
| **Módulo** | `proyectos/cimiento/core/enganches/`, `proyectos/cimiento/core/consumo/lector.py`, `proyectos/cimiento/core/proyectos/`, `adaptadores/claude-code/hook_presupuesto.py` |
| **Especificación del módulo** | Los CA de la [HU-009](../HU-009-se-avisa-cuando-un-enganche-o-un-archivo-pesa-demasiado.md) |
| **Fecha apertura** | 2026-10-05 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva. Sale del punto 9 del [análisis 1 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md) (acuerdo 10).

**Carencias que cierra** (`02·F14` Q3): un enganche o un archivo que pesa demasiado solo se ve si alguien mira el tablero.

**Aprobación** (`02·F4`): [análisis 1 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md), el 2026-10-04, con la versión 54.2.0

**Disparo** (`02·F15`, etapa 2): el usuario pidió «continúe» el 2026-10-05.

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-009 | Estado |
|---|---|
| CA-01 · Lo que pasa el límite se avisa con el mensaje siguiente | ☐ |
| CA-02 · Cada exceso se avisa una vez | ☐ |
| CA-03 · Los límites son los del proyecto | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** con cada mensaje, avisarle al agente qué enganche o qué archivo del turno anterior pasó el límite de su proyecto.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Aviso | Programa | Media |
| CA-02 | Una vez | Programa | Media |
| CA-03 | Límites del proyecto | Programa | Baja |

**Fuera de alcance:** marcar excesos en el tablero; detener la acción.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Verificado el 2026-10-05, sobre la versión 54.2.0:

- `hook_presupuesto.py --modo aviso` corre en `UserPromptSubmit` de este proyecto y avisa el tramo comparando el total con y sin el último turno, sin estado. Recibe `transcript_path` por la entrada estándar.
- En el `.jsonl` de la sesión `c3d82767`, un mensaje del usuario es una línea `user` con un bloque `text`; la de `tool_result` no lo es, y la del resumen de compactación trae `isCompactSummary`. Lo que agregan los enganches de ese mensaje viene después de su línea.
- `LectorDeClaudeCode` no separa turnos: devuelve todo lo leído.
- `NivelesDelProyecto` (`core/enganches/niveles.py`) lee MariaDB con PyMySQL y el `.env` de Cimiento, sin Django.
- `LIMITE_ENGANCHE` y `LIMITE_ARCHIVO` viven en `core/proyectos/models.py`, que importa Django.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/proyectos/limites.py`, `proyectos/cimiento/core/enganches/tests_limites.py` | Crear | Programa | Los límites por defecto sin Django, y las pruebas |
| `proyectos/cimiento/core/proyectos/models.py` | Modificar | Programa | Toma los límites de `limites.py` |
| `proyectos/cimiento/core/consumo/lector.py` | Modificar | Programa | `turno_anterior` |
| `proyectos/cimiento/core/enganches/niveles.py` | Modificar | Programa | `LimitesDelProyecto` |
| `proyectos/cimiento/core/enganches/presupuesto.py` | Modificar | Programa | Lo que pasó el límite y su aviso |
| `adaptadores/claude-code/hook_presupuesto.py` | Modificar | Enganche | El aviso en el modo `aviso` |
| `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-009-se-avisa-cuando-un-enganche-o-un-archivo-pesa-demasiado/HU-009-se-avisa-cuando-un-enganche-o-un-archivo-pesa-demasiado.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | Modificar | Documentación | La fila de la fase y el estado |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| `leer()` del lector pasa a leer una lista de líneas | `guardar.py`, `hook_presupuesto.py` | La firma de `leer()` no cambia; se corren las pruebas de la HU-006 |
| Los límites por defecto salen de `limites.py` | El modelo y su migración `0001` | Mismo valor: la migración no cambia |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica: el aviso le llega al agente.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| El turno anterior va del penúltimo mensaje del usuario al último; si el último aún no está escrito, va hasta el final | Guardar qué se avisó | Sin estado, como el tramo: cada turno se mide una vez | RN-03 |
| El mensaje que se está mandando es el último si después de él no hay respuesta del agente | Comparar su texto con el `prompt` del enganche | Claude Code le suma al texto el contexto del editor, y la línea puede no estar escrita todavía | Propuesta del agente |
| Un mismo enganche que pasa varias veces en el turno sale una vez, con su mayor estimación y cuántas veces | Una línea por vez | El aviso tiene que ser corto | `00·ID9` |
| Sin base o sin registro, los límites por defecto | Callar | El aviso es informativo | RN-05 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| Aviso con cada mensaje | Solo el tramo de consumo | También lo que pasó su límite | Acuerdo 10 |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-01 · Lo que pasa el límite se avisa con el mensaje siguiente

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | `LectorDeClaudeCode.turno_anterior()`: la lectura del turno que terminó | `proyectos/cimiento/core/consumo/lector.py` | CA-01, CA-02 | El aviso | 1 h | Ninguna | CP-001, CP-002 |
| T-02 | `Presupuesto.pasados_del_limite` y `aviso_de_limites` | `proyectos/cimiento/core/enganches/presupuesto.py` | CA-01 | El aviso | 0,5 h | Ninguna | CP-001 |
| T-03 | El modo `aviso` de `hook_presupuesto.py` suma el aviso de límites | `adaptadores/claude-code/hook_presupuesto.py` | CA-01 | Cada mensaje | 0,5 h | T-01, T-02, T-04 | CP-001 |

### CA-03 · Los límites son los del proyecto

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-04 | Los límites por defecto en `limites.py`; `LimitesDelProyecto` los lee de MariaDB | `proyectos/cimiento/core/proyectos/limites.py`, `proyectos/cimiento/core/proyectos/models.py`, `proyectos/cimiento/core/enganches/niveles.py` | CA-03 | El aviso | 0,5 h | Ninguna | CP-003 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-05 | Pruebas; fila de la fase en la HU y estado en la épica | `proyectos/cimiento/core/enganches/tests_limites.py`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-009-se-avisa-cuando-un-enganche-o-un-archivo-pesa-demasiado/HU-009-se-avisa-cuando-un-enganche-o-un-archivo-pesa-demasiado.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | CA-01 a CA-03 | Documentación | 1 h | T-01 a T-04 | CP-001 a CP-003 |

## 4. Secuencia de ejecución

T-04, T-01 y T-02; T-03 y al final T-05, con las pruebas de la fase (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | Una transcripción de muestra con un enganche y un archivo grandes y uno chico | CP-001 |
| CA-02 | Dos turnos: el primero con exceso, el segundo sin | CP-002 |
| CA-03 | Límites propios, sin registro y sin base; un límite bajo en el registro real | CP-003 |

## 6. Datos y ambiente de prueba

Transcripciones de muestra armadas en las pruebas; los límites con una lectura falsa; la base local para el paso manual.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Aditiva: un aviso más en el mismo enganche.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`05`, `07·Q4`, `00·ID9`, `02·F4`, `02·F5`, `02·F8`, `00·ID8`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Claude Code cambie el orden de las líneas | La separación vive en el lector, con su prueba |

## 11. Definition of Done

- [ ] CA-01 a CA-03 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Las pruebas de la fase sin fallas, y cero marcas nuevas.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Las 5 tareas quedaron hechas el 2026-10-05, con la versión 54.2.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** D-01, corregido dentro de `lector.py`, que el plan declara.
