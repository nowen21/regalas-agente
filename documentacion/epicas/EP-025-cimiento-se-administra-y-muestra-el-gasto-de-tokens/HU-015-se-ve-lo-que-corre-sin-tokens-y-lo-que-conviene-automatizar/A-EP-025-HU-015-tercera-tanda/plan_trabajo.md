# Plan de Trabajo · Fase `A-EP-025-HU-015-tercera-tanda` (módulo `proyectos/cimiento/core/consumo/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-015-tercera-tanda` |
| **Épica** | [EP-025](../../epica.md) |
| **HU** | [HU-015](../HU-015-se-ve-lo-que-corre-sin-tokens-y-lo-que-conviene-automatizar.md), una sola (`F12.1`) |
| **Módulo** | `proyectos/cimiento/core/consumo/` |
| **Especificación del módulo** | Los CA de la [HU-015](../HU-015-se-ve-lo-que-corre-sin-tokens-y-lo-que-conviene-automatizar.md) |
| **Fecha apertura** | 2026-10-05 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva. Sale de los puntos 9 y 10 del [análisis 2 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md).

**Carencias que cierra** (`02·F14` Q3): no se ve lo que corre sin tokens ni lo que se repite.

**Aprobación** (`02·F4`): [análisis 2 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md), el 2026-10-05, con la versión 54.4.0

**Disparo** (`02·F15`, etapa 2): el usuario pidió «continúe» el 2026-10-05, después de aprobar el análisis.

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-015 | Estado |
|---|---|
| CA-01 · Lo que corre sin tokens | ☑ |
| CA-02 · Candidatos a automatizar | ☑ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** guardar cada ejecución de un enganche y la orden de cada comando, y las dos secciones nuevas de «Gasto».

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Sin tokens | Programa | Media |
| CA-02 | Candidatos | Programa | Media |

**Fuera de alcance:** los pedidos que siguen los mismos pasos (RN-05).

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Verificado el 2026-10-05, sobre la versión 55.0.0:

- `LectorDeClaudeCode.leer_lineas` arma `enganches` solo con lo que llega al modelo: `hook_additional_context`, `hook_blocking_error` y el texto plano de `UserPromptSubmit` y `SessionStart`. Cada corrida deja un `hook_success` con su `command`.
- `GastoDeEnganche` es único por sesión e identificador; sumarle las corridas sin texto contaría dos veces las que entregan JSON.
- `Herramienta` guarda el nombre y el tamaño del resultado; el comando de `Bash` no se guarda.
- `GastoDelPeriodo.todo()` arma lo que muestra «Gasto»; `_datos.html` lo pinta.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/consumo/lector.py`, `proyectos/cimiento/core/consumo/guardar.py` | Modificar | Programa | Ejecuciones y órdenes |
| `proyectos/cimiento/core/consumo/models.py`, `proyectos/cimiento/core/consumo/migrations/0004_tercera_tanda.py` | Modificar, crear | Datos | `EjecucionDeEnganche` y `orden` |
| `proyectos/cimiento/core/consumo/tablero.py`, `proyectos/cimiento/core/consumo/templates/consumo/_datos.html` | Modificar | Pantallas | Las dos secciones |
| `proyectos/cimiento/core/consumo/tests_tercera_tanda.py` | Crear | Pruebas | |
| `proyectos/cimiento/core/consumo/vigilante.py`, `proyectos/cimiento/core/consumo/tests_vigilante.py` | Modificar | Programa | Declarado durante la fase: al aplicar la `0004`, el vigilante que corría con el código viejo falló al guardar y se cayó; un error en un archivo ya no lo tumba |
| `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-015-se-ve-lo-que-corre-sin-tokens-y-lo-que-conviene-automatizar/HU-015-se-ve-lo-que-corre-sin-tokens-y-lo-que-conviene-automatizar.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | Modificar | Documentación | La fila de la fase y el estado |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| El lector suma `ejecuciones`, y `Herramienta` su `orden` | El guardado, el aviso por límite | Se corren todas las pruebas de `core.consumo` |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No cambian.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

«Gasto», dos secciones nuevas.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Las corridas van en una tabla propia | Sumarlas a `GastoDeEnganche` con cero | Las que entregan JSON se contarían dos veces | Propuesta del agente |
| La orden es el programa y la primera palabra que no es opción ni ruta larga; con `-m`, el módulo | Guardar el comando | Privacidad; alcanza para ver qué se repite | Punto 10 |
| «En casi cada mensaje» es en el 80 % de los mensajes del período o más | Exigir el 100 % | Un mensaje sin el enganche no lo hace menos repetido | Propuesta del agente |
| Lo que se ahorraría: un archivo o un comando, todas sus veces menos una; un enganche de cada mensaje, todo lo que agregó | Otra cuenta | Es lo que no se gastaría si un programa lo hiciera | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  `02·F30`

No aplica: la fase no agrega acciones; guarda y muestra.

## 3. Desglose de tareas por criterio de aceptación

### CA-01 · Lo que corre sin tokens

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | Ejecuciones en el lector, el modelo, la migración y el guardado | `proyectos/cimiento/core/consumo/lector.py`, `proyectos/cimiento/core/consumo/models.py`, `proyectos/cimiento/core/consumo/migrations/0004_tercera_tanda.py`, `proyectos/cimiento/core/consumo/guardar.py` | CA-01 | Consumo | 1,5 h | Ninguna | CP-001 |
| T-02 | La sección «Lo que corre sin tokens» | `proyectos/cimiento/core/consumo/tablero.py`, `proyectos/cimiento/core/consumo/templates/consumo/_datos.html` | CA-01 | Tablero | 1 h | T-01 | CP-001 |

### CA-02 · Candidatos a automatizar

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-03 | La orden de cada comando | `proyectos/cimiento/core/consumo/lector.py`, `proyectos/cimiento/core/consumo/guardar.py` | CA-02 | Consumo | 0,5 h | T-01 | CP-002 |
| T-04 | La sección «Candidatos a automatizar» | `proyectos/cimiento/core/consumo/tablero.py`, `proyectos/cimiento/core/consumo/templates/consumo/_datos.html` | CA-02 | Tablero | 1 h | T-03 | CP-002 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-05 | Pruebas, migración real y cierre con `cerrar_fase` | `proyectos/cimiento/core/consumo/tests_tercera_tanda.py`, la HU y la épica | CA-01, CA-02 | Documentación | 1 h | T-01 a T-04 | CP-001, CP-002 |

## 4. Secuencia de ejecución

T-01 a T-05.

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | Un `.jsonl` de muestra con un enganche con texto y otro sin | CP-001 |
| CA-02 | Lecturas, enganches y comandos repetidos | CP-002 |

## 6. Datos y ambiente de prueba

`.jsonl` armados en la prueba y la base de pruebas.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit y `migrate consumo 0003`.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

`preparar_base` aplica la `0004`; lo ya guardado no tiene ejecuciones ni órdenes: entran desde que el vigilante lea lo nuevo.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`12`, `03·D6`, `02·F4`, `02·F5`, `02·F8`, `00·ID8`, `00·ID9`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Que se guarde un comando entero | Solo programa y orden, con su prueba |

## 11. Definition of Done

- [ ] CA-01 y CA-02 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Las pruebas de la fase sin fallas, y cero marcas nuevas.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Las 5 tareas quedaron hechas el 2026-10-05, con la versión 55.0.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** ninguno.
