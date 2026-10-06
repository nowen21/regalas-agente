# Plan de Trabajo · Fase `A-EP-025-HU-022-reabrir-con-sus-enlaces` (módulo `proyectos/cimiento/core/herramientas/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-022-reabrir-con-sus-enlaces` |
| **Épica** | [EP-025](../../epica.md) |
| **HU** | [HU-022](../HU-022-un-pendiente-cerrado-se-puede-reabrir.md), una sola (`F12.1`) |
| **Módulo** | `proyectos/cimiento/core/herramientas/` |
| **Especificación del módulo** | Los CA de la [HU-022](../HU-022-un-pendiente-cerrado-se-puede-reabrir.md) |
| **Fecha apertura** | 2026-10-05 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva. Sale del punto 7 del [análisis 3 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md).

**Carencias que cierra** (`02·F14` Q3): un pendiente cerrado no se puede reabrir.

**Aprobación** (`02·F4`): [análisis 3 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md), el 2026-10-05, con la versión 54.3.0

**Disparo** (`02·F15`, etapa 2): el usuario pidió «continúe» el 2026-10-05, después de aprobar el análisis.

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-022 | Estado |
|---|---|
| CA-01 · Reabrir con sus enlaces y su fila | ☑ |
| CA-02 · Lo que no se puede reabrir se dice | ☑ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** `cerrar.py reabrir`, la contraria de `cerrar.py`.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Reabrir | Programa | Media |
| CA-02 | Rechazos y simulación | Programa | Baja |

**Fuera de alcance:** los pendientes de la forma nueva.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Verificado el 2026-10-05, sobre la versión 55.0.0:

- `CerradorDePendientes.cerrar` mueve con `mover`, que reescribe las citas al archivo y las del archivo, y después `fila_hecha` deja la fila como `| ~~NN~~ | — | **hecho** → [título](hecho/x.md) | …`.
- El nombre original del archivo se pierde al cerrar: la fila guarda solo el número y el nombre en `hecho/`.
- Las pruebas de `cerrar` viven en `core/enganches/tests_freno.py` (`CerrarArrastraLasCitas`).

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/herramientas/cerrar.py` | Modificar | Programa | `reabrir` y su modo |
| `proyectos/cimiento/core/herramientas/tests_reabrir.py` | Crear | Pruebas | |
| `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-022-un-pendiente-cerrado-se-puede-reabrir/HU-022-un-pendiente-cerrado-se-puede-reabrir.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | Modificar | Documentación | La fila de la fase y el estado |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| `main` de `cerrar.py` suma el modo `reabrir` | `validadores/cerrar.py` | Sin el modo, sigue igual; se corren sus pruebas |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

`python validadores/cerrar.py reabrir «número» --motivo «…» --fecha «AAAA-MM-DD» [--aplicar]`.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| El archivo vuelve como `«número»-«nombre en hecho».md` | Recuperar el nombre original | El original no queda guardado; el número es lo que lo identifica | Propuesta del agente |
| Las pruebas van en un archivo nuevo | Sumarlas a `tests_freno.py` | Ese archivo ya pasa de 2.900 líneas | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  `02·F30`

| Acción nueva | Su contraria | Prueba |
|---|---|---|
| `reabrir` | `cerrar`, que ya existe | CP-001 cierra, reabre y compara |

## 3. Desglose de tareas por criterio de aceptación

### CA-01 · Reabrir con sus enlaces y su fila

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | `reabrir`: busca la fila, mueve con `mover`, deja la fila abierta y la marca en el pendiente | `proyectos/cimiento/core/herramientas/cerrar.py` | CA-01 | Nuevo | 1 h | Ninguna | CP-001 |

### CA-02 · Lo que no se puede reabrir se dice

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-02 | Rechazos, simulación y el modo en `main` | `proyectos/cimiento/core/herramientas/cerrar.py` | CA-02 | Nuevo | 0,5 h | T-01 | CP-002 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-03 | Pruebas y cierre con `cerrar_fase` | `proyectos/cimiento/core/herramientas/tests_reabrir.py`, la HU y la épica | CA-01, CA-02 | Documentación | 0,5 h | T-01, T-02 | CP-001, CP-002 |

## 4. Secuencia de ejecución

T-01, T-02, T-03.

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | Cerrar y reabrir en una carpeta temporal | CP-001 |
| CA-02 | Número abierto, destino ocupado, simulación | CP-002 |

## 6. Datos y ambiente de prueba

Carpetas temporales con un `pendientes/` de muestra.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Aditiva: un modo nuevo.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`02·F30`, `02·F4`, `02·F5`, `02·F8`, `00·ID8`, `00·ID9`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Romper enlaces | El mismo `mover` de cerrar |

## 11. Definition of Done

- [ ] CA-01 y CA-02 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Las pruebas de la fase sin fallas, y cero marcas nuevas.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Las 3 tareas quedaron hechas el 2026-10-05, con la versión 55.0.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** ninguno.
