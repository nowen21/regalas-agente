# Plan de Trabajo · Fase `A-EP-025-HU-021-desinstalar` (módulo `proyectos/cimiento/core/herramientas/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-021-desinstalar` |
| **Épica** | [EP-025](../../epica.md) |
| **HU** | [HU-021](../HU-021-el-estandar-se-puede-desinstalar-de-un-proyecto.md), una sola (`F12.1`) |
| **Módulo** | `proyectos/cimiento/core/herramientas/` |
| **Especificación del módulo** | Los CA de la [HU-021](../HU-021-el-estandar-se-puede-desinstalar-de-un-proyecto.md) |
| **Fecha apertura** | 2026-10-05 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva. Sale del punto 6 del [análisis 3 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md).

**Carencias que cierra** (`02·F14` Q3): la instalación no se deshace.

**Aprobación** (`02·F4`): [análisis 3 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md), el 2026-10-05, con la versión 54.3.0

**Disparo** (`02·F15`, etapa 2): el usuario pidió «continúe» el 2026-10-05, después de aprobar el análisis.

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-021 | Estado |
|---|---|
| CA-01 · Quitar lo que puso la instalación | ☑ |
| CA-02 · Lo propio se queda | ☑ |
| CA-03 · Simular y repetir | ☑ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** `instalar.py «ruta» --desinstalar`, la contraria de la instalación.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Quitar | Programa | Alta |
| CA-02 | Lo propio se queda | Programa | Media |
| CA-03 | Simular y repetir | Programa | Baja |

**Fuera de alcance:** la interfaz.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Verificado el 2026-10-05, sobre la versión 55.0.0:

- `Instalador.instalar` pone: `.githooks/` con la marca `MARCA` y `core.hooksPath`; `core.longpaths`; las entradas de `HOOKS_CLAUDE` en `.claude/settings.json`, que llaman a `adaptadores/claude-code/`; `historico-chat/` y la memoria; y, en un proyecto, `proyectos/`, `documentacion/` y `prompts/`, las líneas de `IGNORADOS` en el `.gitignore`, `.agente/stack-instalacion.md`, los cuatro archivos de `.agente/`, `CLAUDE.md` con su copia en `.agente/plantillas-selladas/`, la fila de `plantillas/proyectos.md` con el alta en Cimiento, y la integración continua (`.github/workflows/cimiento.yml`, `.cimiento-ci.yml`). En el propio estándar, además, la tarea `Cimiento leer consumo` y la telemetría en `~/.claude/settings.json`.
- `CLAUDE.md` y `.agente/` son locales y los llena el proyecto: están en `IGNORADOS`.
- `instalar.py` ya pasa de 1.390 líneas.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/herramientas/desinstalar.py`, `proyectos/cimiento/core/herramientas/tests_desinstalar.py` | Crear | Programa | El desinstalador y sus pruebas |
| `proyectos/cimiento/core/herramientas/instalar.py` | Modificar | Programa | `--desinstalar` en la orden |
| `proyectos/cimiento/core/proyectos/registro.py`, `proyectos/cimiento/core/proyectos/management/commands/registrar.py` | Modificar | Programa | `--baja` |
| `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-021-el-estandar-se-puede-desinstalar-de-un-proyecto/HU-021-el-estandar-se-puede-desinstalar-de-un-proyecto.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | Modificar | Documentación | La fila de la fase y el estado |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| `main` de `instalar.py` suma `--desinstalar` | `validadores/instalar.py` | Sin la opción, igual; se corren `tests_instalacion` |
| `manage.py registrar` suma `--baja` | El instalador | Sin la opción, igual |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

`python validadores/instalar.py «ruta» --desinstalar [--aplicar]`.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| El desinstalador va en su propio archivo | Sumarlo a `instalar.py` | Ese archivo ya es grande; usa sus constantes | Propuesta del agente |
| Se quedan `CLAUDE.md`, `.agente/` y las líneas del `.gitignore` | Borrarlos | Los llena el proyecto; y sin las líneas del `.gitignore`, `CLAUDE.md` y `.agente/` aparecerían para versionar | Propuesta del agente (RN-05) |
| Se queda `core.longpaths` | Quitarlo | No se sabe si lo puso alguien más, y no estorba | Propuesta del agente |
| El proyecto se desactiva en Cimiento, no se borra | Borrarlo | El modelo dice que su gasto es historia | Modelo `Proyecto` |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  `02·F30`

| Acción nueva | Su contraria | Prueba |
|---|---|---|
| Desinstalar | Instalar, que ya existe | CP-001 instala, desinstala y compara los enganches |
| `registrar --baja` | `registrar`, que lo vuelve a activar | CP-001 |

## 3. Desglose de tareas por criterio de aceptación

### CA-01 · Quitar lo que puso la instalación

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | Quitar los enganches de git y de Claude Code, las copias, la integración continua y las carpetas vacías | `proyectos/cimiento/core/herramientas/desinstalar.py` | CA-01 | Nuevo | 2 h | Ninguna | CP-001 |
| T-02 | Sacar del registro y dar de baja en Cimiento; `registrar` vuelve a activar | `proyectos/cimiento/core/herramientas/desinstalar.py`, `proyectos/cimiento/core/proyectos/registro.py`, `proyectos/cimiento/core/proyectos/management/commands/registrar.py` | CA-01 | Registro | 1 h | T-01 | CP-001 |
| T-03 | En el estándar: la tarea programada y la telemetría | `proyectos/cimiento/core/herramientas/desinstalar.py` | CA-01 | Estándar | 0,5 h | T-01 | CP-001 |

### CA-02 · Lo propio se queda

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-04 | Lo propio no se toca | `proyectos/cimiento/core/herramientas/desinstalar.py` | CA-02 | Nuevo | 0,5 h | T-01 | CP-002 |

### CA-03 · Simular y repetir

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-05 | Simulación y `--desinstalar` en la orden | `proyectos/cimiento/core/herramientas/instalar.py` | CA-03 | Orden | 0,5 h | T-01 | CP-003 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-06 | Pruebas y cierre con `cerrar_fase` | `proyectos/cimiento/core/herramientas/tests_desinstalar.py`, la HU y la épica | CA-01 a CA-03 | Documentación | 1 h | T-01 a T-05 | CP-001 a CP-003 |

## 4. Secuencia de ejecución

T-01 a T-06.

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | Instalar en un repositorio temporal, desinstalar y comparar | CP-001 |
| CA-02 | Lo propio, igual antes y después | CP-002 |
| CA-03 | Simular y repetir | CP-003 |

## 6. Datos y ambiente de prueba

Un repositorio git temporal y un registro de proyectos temporal.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase. Lo desinstalado se vuelve a poner con `instalar.py «ruta» --aplicar`.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Aditiva: una opción nueva.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`02·F30`, `04·S9`, `02·F4`, `02·F5`, `02·F8`, `00·ID8`, `00·ID9`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Borrar algo del proyecto | Solo lo marcado o lo que llama al adaptador |

## 11. Definition of Done

- [ ] CA-01 a CA-03 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Las pruebas de la fase sin fallas, y cero marcas nuevas.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Las 6 tareas quedaron hechas el 2026-10-05, con la versión 55.0.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** ninguno.
