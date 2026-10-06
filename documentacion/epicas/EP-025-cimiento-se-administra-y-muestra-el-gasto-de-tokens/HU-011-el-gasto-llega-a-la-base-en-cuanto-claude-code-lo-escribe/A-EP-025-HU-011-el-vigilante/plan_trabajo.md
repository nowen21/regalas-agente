# Plan de Trabajo · Fase `A-EP-025-HU-011-el-vigilante` (módulo `proyectos/cimiento/core/consumo/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-011-el-vigilante` |
| **Épica** | [EP-025](../../epica.md) |
| **HU** | [HU-011](../HU-011-el-gasto-llega-a-la-base-en-cuanto-claude-code-lo-escribe.md), una sola (`F12.1`) |
| **Módulo** | `proyectos/cimiento/core/consumo/` |
| **Especificación del módulo** | Los CA de la [HU-011](../HU-011-el-gasto-llega-a-la-base-en-cuanto-claude-code-lo-escribe.md) |
| **Fecha apertura** | 2026-10-05 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva. Sale de los puntos 2, 3 y 15 del [análisis 2 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md).

**Carencias que cierra** (`02·F14` Q3): el `.jsonl` se lee al abrir el tablero y una vez al día; lo vivo depende de la telemetría.

**Aprobación** (`02·F4`): [análisis 2 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md), el 2026-10-05, con la versión 54.4.0

**Disparo** (`02·F15`, etapa 2): el usuario pidió «continúe» el 2026-10-05, después de aprobar el análisis.

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-011 | Estado |
|---|---|
| CA-01 · Lo nuevo se guarda cuando cambia el archivo | ☑ |
| CA-02 · Se arranca, se detiene y se instala | ☑ |
| CA-03 · El tablero solo consulta la base | ☑ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** `manage.py vigilar_consumo`, su arranque al iniciar sesión, y el tablero que solo consulta la base.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Guardar al cambiar | Programa | Media |
| CA-02 | Arrancar, detener, instalar | Programa | Media |
| CA-03 | Tablero | Programa | Baja |

**Fuera de alcance:** retirar la telemetría (HU-012).

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Verificado el 2026-10-05, sobre la versión 55.0.0:

- `GuardadoDeConsumo(proyecto).leer_archivo(ruta)` lee lo nuevo de un `.jsonl` desde su avance y lo guarda sin duplicar; `leer_lo_nuevo()` lo hace con todos los proyectos activos.
- `Tablero.get` llama a `leer_lo_nuevo()` antes de mostrar.
- `Instalador.programar_lectura` crea la tarea diaria «Cimiento leer consumo» con `schtasks`; `Desinstalador.quitar_lectura` la quita.
- `watchdog` 6.0.0 no tenía dependencias y no estaba en el ambiente; se instaló el 2026-10-05.
- `proyectos/*/.agente/` es local: lo ignora el `.gitignore`.
- El plan de la HU-006 dice en §2.6 que `04·S10` es «la instalación no deja procesos vivos».

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/consumo/vigilante.py`, `proyectos/cimiento/core/consumo/management/commands/vigilar_consumo.py` | Crear | Programa | El vigilante y su orden |
| `proyectos/cimiento/core/consumo/tests_vigilante.py` | Crear | Pruebas | |
| `proyectos/cimiento/core/consumo/views.py`, `proyectos/cimiento/core/consumo/tests_tablero.py` | Modificar | Programa | El tablero sin lectura; su prueba de leer al abrir pasa a probar que no lee |
| `proyectos/cimiento/core/consumo/management/commands/leer_consumo.py` | Modificar | Programa | Su texto ya no dice que lo corre el tablero |
| `proyectos/cimiento/core/herramientas/instalar.py`, `proyectos/cimiento/core/herramientas/desinstalar.py`, `proyectos/cimiento/core/herramientas/tests_desinstalar.py`, `proyectos/cimiento/core/herramientas/tests_instalacion.py` | Modificar | Programa | Arranque al iniciar sesión, y su contraria; las pruebas de la tarea diaria pasan a ser las del vigilante |
| `proyectos/cimiento/requirements/base.txt`, `proyectos/cimiento/requirements/lock.txt` | Modificar | Dependencias | `watchdog` |
| `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-006-el-gasto-de-cada-llamada-queda-guardado/A-EP-025-HU-006-lectura-de-los-jsonl/plan_trabajo.md` | Modificar | Documentación | La cita de `04·S10` |
| `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-011-el-gasto-llega-a-la-base-en-cuanto-claude-code-lo-escribe/HU-011-el-gasto-llega-a-la-base-en-cuanto-claude-code-lo-escribe.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | Modificar | Documentación | La fila de la fase y el estado |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| `programar_lectura` pasa a `programar_vigilante` | `Instalador.instalar` | Se corren `tests_instalacion` |
| `Tablero.get` ya no lee | El tablero | Se corren las pruebas del tablero |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No cambian.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

`python manage.py vigilar_consumo` y `python manage.py vigilar_consumo --parar`; arranca solo al iniciar sesión.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Arranca desde la carpeta de inicio de Windows, con `pythonw` | Una tarea `schtasks /SC ONLOGON` | Crear esa tarea pide permisos de administrador; la carpeta de inicio es del usuario | Propuesta del agente |
| Los cambios se juntan y se guardan cada 2 segundos | Guardar en cada aviso | Claude Code escribe varias líneas seguidas: se lee una vez | Propuesta del agente (RNF-01) |
| El número de proceso va en `proyectos/cimiento/.agente/vigilar-consumo.pid` | Otra carpeta | `.agente/` ya es local e ignorado | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  `02·F30`

| Acción nueva | Su contraria | Prueba |
|---|---|---|
| Arrancar el vigilante | `vigilar_consumo --parar` | CP-002 |
| Ponerlo a arrancar al iniciar sesión | La desinstalación lo quita | CP-002 |

## 3. Desglose de tareas por criterio de aceptación

### CA-01 · Lo nuevo se guarda cuando cambia el archivo

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | `VigilanteDeConsumo`: proyectos por carpeta, cambios juntados, guardar con `leer_archivo` | `proyectos/cimiento/core/consumo/vigilante.py` | CA-01 | Nuevo | 1,5 h | Ninguna | CP-001 |

### CA-02 · Se arranca, se detiene y se instala

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-02 | La orden, con el número de proceso y `--parar` | `proyectos/cimiento/core/consumo/management/commands/vigilar_consumo.py` | CA-02 | Nuevo | 1 h | T-01 | CP-002 |
| T-03 | La instalación lo arranca al iniciar sesión y quita la tarea diaria; la desinstalación lo detiene y lo quita | `proyectos/cimiento/core/herramientas/instalar.py`, `proyectos/cimiento/core/herramientas/desinstalar.py`, `proyectos/cimiento/core/herramientas/tests_desinstalar.py` | CA-02 | Instalación | 1 h | T-02 | CP-002 |
| T-04 | `watchdog` en los requisitos | `proyectos/cimiento/requirements/base.txt`, `proyectos/cimiento/requirements/lock.txt` | CA-02 | Dependencias | 0,2 h | Ninguna | CP-002 |

### CA-03 · El tablero solo consulta la base

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-05 | Quitar la lectura del tablero; corregir los textos y la cita del plan de la HU-006 | `proyectos/cimiento/core/consumo/views.py`, `proyectos/cimiento/core/consumo/management/commands/leer_consumo.py`, el plan de la HU-006 | CA-03 | Tablero | 0,3 h | Ninguna | CP-003 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-06 | Pruebas, prueba en vivo y cierre con `cerrar_fase` | `proyectos/cimiento/core/consumo/tests_vigilante.py`, la HU y la épica | CA-01 a CA-03 | Documentación | 1 h | T-01 a T-05 | CP-001 a CP-003 |

## 4. Secuencia de ejecución

T-04, T-01 a T-03, T-05, T-06.

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | Un `.jsonl` que cambia en una carpeta temporal | CP-001 |
| CA-02 | Número de proceso, `--parar`, instalar y desinstalar | CP-002 |
| CA-03 | El tablero no llama al lector | CP-003 |

## 6. Datos y ambiente de prueba

Carpetas temporales con `.jsonl` de muestra; la base de pruebas de Django.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit; `vigilar_consumo --parar` y quitar el archivo de la carpeta de inicio con la desinstalación.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

`pip install -r requirements/lock.txt` en el ambiente de Cimiento, y correr la instalación del estándar.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`02·F30`, `03·D6`, `04·S10`, `10·DEP2`, `02·F4`, `02·F5`, `02·F8`, `00·ID8`, `00·ID9`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Dos vigilantes a la vez | Al arrancar, si el número guardado es de un proceso vivo, no arranca otro |

## 11. Definition of Done

- [ ] CA-01 a CA-03 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Las pruebas de la fase sin fallas, y cero marcas nuevas.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Las 6 tareas quedaron hechas el 2026-10-05, con la versión 55.0.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** ninguno.
