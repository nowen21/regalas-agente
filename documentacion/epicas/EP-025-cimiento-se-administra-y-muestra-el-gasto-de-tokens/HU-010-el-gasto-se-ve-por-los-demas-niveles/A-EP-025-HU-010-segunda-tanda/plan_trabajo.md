# Plan de Trabajo · Fase `A-EP-025-HU-010-segunda-tanda` (módulo `proyectos/cimiento/core/consumo/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-010-segunda-tanda` |
| **Épica** | [EP-025](../../epica.md) |
| **HU** | [HU-010](../HU-010-el-gasto-se-ve-por-los-demas-niveles.md), una sola (`F12.1`) |
| **Módulo** | `proyectos/cimiento/core/consumo/`, `proyectos/cimiento/core/herramientas/recuperar.py` |
| **Especificación del módulo** | Los CA de la [HU-010](../HU-010-el-gasto-se-ve-por-los-demas-niveles.md) |
| **Fecha apertura** | 2026-10-05 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva. Sale del punto 10 del [análisis 1 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md) (acuerdo 7).

**Carencias que cierra** (`02·F14` Q3): no se sabe cuánto cuesta cada clase de pedido, cada herramienta, cada agente auxiliar ni cada trabajo.

**Aprobación** (`02·F4`): [análisis 1 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md), el 2026-10-04, con la versión 54.2.0

**Disparo** (`02·F15`, etapa 2): el usuario pidió «continúe» el 2026-10-05.

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-010 | Estado |
|---|---|
| CA-01 · El gasto queda por mensaje, palabra clave y trabajo | ☐ |
| CA-02 · El gasto queda por herramienta y por agente auxiliar | ☐ |
| CA-03 · El tablero muestra los siete niveles | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** guardar y mostrar la segunda tanda de niveles del acuerdo 7.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Mensajes y trabajo | Programa | Alta |
| CA-02 | Herramientas y auxiliares | Programa | Media |
| CA-03 | Tablero | Programa | Media |

**Fuera de alcance:** el mensaje de un agente auxiliar; la palabra clave de lo que solo llegó por telemetría.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Verificado el 2026-10-05, sobre la versión 54.2.0:

- En la sesión `c3d82767`: las 1108 líneas `assistant` no traen `promptId`; las 612 `user` sí. Herramientas usadas: Bash 295, Write 127, Edit 127, Read 49 y otras.
- Hay 5 sesiones con `subagents/`; cada agente deja `agent-«id».jsonl` con `isSidechain` y `agentId`, y `agent-«id».meta.json` con `agentType` y `description`.
- `RecuperadorDeReglas` (`core/herramientas/recuperar.py`) lee la lista de `01·C28` y quita lo que agrega el editor; dice si un mensaje trae palabra, no cuál.
- `GuardadoDeConsumo.archivos()` lee solo la primera altura de la carpeta.
- `AvanceDeLectura` guarda dónde quedó cada archivo; una lectura puede empezar a mitad de un turno.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/consumo/trabajo.py`, `proyectos/cimiento/core/consumo/tests_segunda_tanda.py` | Crear | Programa | El trabajo de un turno y las pruebas |
| `proyectos/cimiento/core/consumo/migrations/0003_segunda_tanda.py` | Crear | Datos | Mensajes, herramientas, mensaje y agente de cada llamada |
| `proyectos/cimiento/core/consumo/lector.py`, `proyectos/cimiento/core/consumo/models.py`, `proyectos/cimiento/core/consumo/guardar.py`, `proyectos/cimiento/core/consumo/telemetria.py`, `proyectos/cimiento/core/consumo/views.py`, `proyectos/cimiento/core/consumo/tablero.py` | Modificar | Programa | Leer, guardar y sumar los niveles nuevos |
| `proyectos/cimiento/core/consumo/templates/consumo/_datos.html` | Modificar | Pantalla | Las secciones nuevas |
| `proyectos/cimiento/core/herramientas/recuperar.py` | Modificar | Programa | `palabra_clave(mensaje)` |
| `proyectos/cimiento/core/consumo/tests.py` | Modificar | Programa | La prueba de la HU-006 que dejaba fuera a los auxiliares pasa a exigirlos |
| `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-010-el-gasto-se-ve-por-los-demas-niveles/HU-010-el-gasto-se-ve-por-los-demas-niveles.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | Modificar | Documentación | La fila de la fase y el estado |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| La `Lectura` suma mensajes y herramientas | `guardar.py`, `hook_presupuesto.py` | Campos con valor por defecto; se corren las pruebas de las HU-006, 007 y 009 |
| `archivos()` suma los de `subagents/` | `leer_consumo`, el tablero | Se corren las pruebas de la HU-006 |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

Las de la HU-008, sin cambios.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

Las secciones nuevas en «Gasto».

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| El mensaje se identifica por su `promptId` | El `uuid` de la línea | Es el que repiten las líneas del turno y el `prompt.id` de la telemetría | Línea base |
| El avance de lectura guarda el último mensaje, para unir las llamadas de un turno leído en dos veces | Releer desde el mensaje | Leer desde un byte es lo que hace barata la lectura | HU-006 |
| El trabajo sale de las rutas tocadas en el turno; gana la que más veces aparece | El aviso de acuerdos | Ese aviso nombra fases de otras sesiones | Línea base |
| La palabra clave la reconoce `RecuperadorDeReglas`, con la misma lista y la misma limpieza | Otra lista | `07·Q4` | Línea base |
| Lo que llena el contexto: suma estimada de enganches, archivos leídos y otras herramientas, frente al contexto máximo de una llamada | Repartir cada llamada | El `.jsonl` no dice qué parte del contexto ocupa cada pieza | RN-06 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| Niveles del gasto | Proyecto, sesión, enganche, archivo y día | También mensaje, palabra, trabajo, herramienta, agente, modelo, tipo de token y contexto | Acuerdo 7 |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-01 · El gasto queda por mensaje, palabra clave y trabajo

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | El lector arma los mensajes (con su texto solo en memoria y las rutas tocadas) y une cada llamada a su mensaje | `proyectos/cimiento/core/consumo/lector.py` | CA-01 | El guardado | 1,5 h | Ninguna | CP-001 |
| T-02 | `trabajo_de(rutas)` y `RecuperadorDeReglas.palabra_clave(mensaje)` | `proyectos/cimiento/core/consumo/trabajo.py`, `proyectos/cimiento/core/herramientas/recuperar.py` | CA-01 | El guardado | 1 h | Ninguna | CP-001 |
| T-03 | Modelos `Pedido` y `GastoDeHerramienta`, `Llamada.pedido`, `Llamada.agente`, `AvanceDeLectura.pedido`; migración; guardado | `proyectos/cimiento/core/consumo/models.py`, `proyectos/cimiento/core/consumo/migrations/0003_segunda_tanda.py`, `proyectos/cimiento/core/consumo/guardar.py` | CA-01, CA-02 | La base | 2 h | T-01, T-02 | CP-001, CP-002 |

### CA-02 · El gasto queda por herramienta y por agente auxiliar

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-04 | El lector ve cada herramienta; el guardado lee `subagents/` con su meta; la telemetría guarda cada herramienta y el mensaje de la llamada | `proyectos/cimiento/core/consumo/lector.py`, `proyectos/cimiento/core/consumo/guardar.py`, `proyectos/cimiento/core/consumo/telemetria.py` | CA-02 | La base | 1,5 h | T-03 | CP-002 |

### CA-03 · El tablero muestra los siete niveles

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-05 | Las sumas nuevas y sus secciones | `proyectos/cimiento/core/consumo/tablero.py`, `proyectos/cimiento/core/consumo/templates/consumo/_datos.html` | CA-03 | El tablero | 2 h | T-03, T-04 | CP-003 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-06 | Pruebas; volver a leer los `.jsonl`; fila de la fase en la HU y estado en la épica | `proyectos/cimiento/core/consumo/tests_segunda_tanda.py`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-010-el-gasto-se-ve-por-los-demas-niveles/HU-010-el-gasto-se-ve-por-los-demas-niveles.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | CA-01 a CA-03 | Documentación | 1 h | T-01 a T-05 | CP-001 a CP-003 |

## 4. Secuencia de ejecución

T-01 y T-02; T-03, T-04, T-05 y al final T-06, con las pruebas de la fase (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | Un `.jsonl` con dos mensajes y un turno leído en dos veces | CP-001 |
| CA-02 | Herramientas, un auxiliar con su meta y un envío de telemetría | CP-002 |
| CA-03 | El tablero con la muestra y con el gasto real | CP-003 |

## 6. Datos y ambiente de prueba

`.jsonl` de muestra en carpetas temporales; la base de pruebas en MariaDB; la base local para el paso manual.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase y `manage.py migrate consumo 0002`.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Aditiva: tablas nuevas y campos que aceptan vacío. Para llenar lo ya guardado se vuelve a leer: se borra el avance de lectura y lo que sale de los `.jsonl`, que siguen en disco.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`03·D6`, `07·Q4`, `12`, `02·F4`, `02·F5`, `02·F8`, `00·ID8`, `00·ID9`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Un turno sin rutas de una fase queda sin trabajo | Se muestra «sin trabajo» |

## 11. Definition of Done

- [ ] CA-01 a CA-03 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Las pruebas de la fase sin fallas, y cero marcas nuevas.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Las 6 tareas quedaron hechas el 2026-10-05, con la versión 54.2.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** ninguno.
