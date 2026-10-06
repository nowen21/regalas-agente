# Plan de Trabajo · Fase `A-EP-025-HU-014-rutas-y-hook-md` (módulo `proyectos/cimiento/core/enganches/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-014-rutas-y-hook-md` |
| **Épica** | [EP-025](../../epica.md) |
| **HU** | [HU-014](../HU-014-los-avisos-muestran-las-rutas-como-lo-diga-la-configuracion.md), una sola (`F12.1`) |
| **Módulo** | `proyectos/cimiento/core/enganches/` |
| **Especificación del módulo** | Los CA de la [HU-014](../HU-014-los-avisos-muestran-las-rutas-como-lo-diga-la-configuracion.md) |
| **Fecha apertura** | 2026-10-05 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva y traslado a `core/`. Sale de los puntos 7 y 8 del [análisis 2 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md).

**Carencias que cierra** (`02·F14` Q3): las rutas salen como cada enganche quiere, y `hook_md.py` usa copias viejas.

**Aprobación** (`02·F4`): [análisis 2 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md), el 2026-10-05, con la versión 54.4.0

**Disparo** (`02·F15`, etapa 2): el usuario pidió «continúe» el 2026-10-05, después de aprobar el análisis.

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-014 | Estado |
|---|---|
| CA-01 · Las rutas según el ajuste | ☑ |
| CA-02 · `hook_md.py` en `core/` | ☑ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** `Proyecto.mostrar` según el ajuste, los enganches que muestran rutas usándolo, y `hook_md.py` en `core/`.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Rutas | Programa | Media |
| CA-02 | `hook_md.py` | Programa | Media |

**Fuera de alcance:** retirar los módulos viejos de `validadores/`, que usa `evals/correr.py`.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Verificado el 2026-10-05, sobre la versión 55.0.0:

- `Proyecto.mostrar` da la ruta relativa si queda adentro y completa si queda afuera. `Proyecto.relativa` decide si una ruta es del proyecto: lo usa el código para decidir, no para mostrar.
- Muestran rutas armadas con `os.path.relpath`: `hook_resumen.py` (dos mensajes), `hook_sesion.py` (`_relativo`) y `hook_veredicto.py`. En `hook_relacionadas.py` la ruta relativa es una clave, no se muestra.
- `hook_md.py` importa de `validadores/` `comun`, `enlaces`, `marcas` y `sesiones`. En `core/` están `Marcas.medir`, `EnlacesRotos`, `IndicesDeCarpetas`, `Sesiones.anotar`, `entrada_json`, `raiz_pedida` y `archivo_editado`.
- `ConfiguracionDelProyecto` aplica la base a cualquier carpeta, registrada o no.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/comun/proyecto.py` | Modificar | Programa | `mostrar` con el ajuste |
| `proyectos/cimiento/core/enganches/configuracion.py` | Modificar | Programa | Sin registro, fábrica |
| `proyectos/cimiento/core/enganches/md.py`, `proyectos/cimiento/core/enganches/tests_md.py` | Crear | Programa | La lógica de `hook_md.py` |
| `adaptadores/claude-code/hook_md.py`, `adaptadores/claude-code/hook_resumen.py`, `adaptadores/claude-code/hook_sesion.py`, `adaptadores/claude-code/hook_veredicto.py` | Modificar | Programa | Llaman a `core/` |
| `proyectos/cimiento/core/proyectos/tests_rutas.py` | Crear | Pruebas | Las rutas con el ajuste |
| `proyectos/cimiento/core/enganches/tests_limites.py` | Modificar | Pruebas | Declarado durante la fase: su simulación de la consulta pasa de dos resultados a tres |
| `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-014-los-avisos-muestran-las-rutas-como-lo-diga-la-configuracion/HU-014-los-avisos-muestran-las-rutas-como-lo-diga-la-configuracion.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | Modificar | Documentación | La fila de la fase y el estado |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| `Proyecto.mostrar` lee el ajuste | Validadores, herramientas y enganches | Sin registro sigue relativo; se corren `tests_freno` y las de herramientas |
| `ConfiguracionDelProyecto` sin registro da fábrica | Límites y rutas | Se corren `tests_configuracion` y `tests_limites` |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

«Rutas en los avisos», en «Configuración» y en cada proyecto (HU-013).

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| El ajuste se aplica en `Proyecto.mostrar` | En `Proyecto.relativa`, como dice el punto 7 | `relativa` decide si una ruta es del proyecto; cambiarla rompería esas decisiones. `mostrar` es la que nombra rutas en los avisos | Propuesta del agente |
| Sin registro, todo de fábrica | Aplicar la base a cualquier carpeta | La base es de los proyectos que Cimiento administra; así una prueba con carpetas temporales no cambia según la máquina | Propuesta del agente |
| El ajuste se lee una vez por proyecto y por proceso | Leerlo en cada ruta | Un aviso puede nombrar cientos | RNF-01 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  `02·F30`

No aplica: la fase no agrega acciones; cambia cómo se muestra lo que ya existe.

## 3. Desglose de tareas por criterio de aceptación

### CA-01 · Las rutas según el ajuste

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | `mostrar` con el ajuste; sin registro, fábrica | `proyectos/cimiento/core/comun/proyecto.py`, `proyectos/cimiento/core/enganches/configuracion.py` | CA-01 | Todo lo que muestra rutas | 1 h | Ninguna | CP-001 |
| T-02 | Los enganches que muestran rutas usan `mostrar` | `adaptadores/claude-code/hook_resumen.py`, `adaptadores/claude-code/hook_sesion.py`, `adaptadores/claude-code/hook_veredicto.py` | CA-01 | Enganches | 0,5 h | T-01 | CP-001 |

### CA-02 · `hook_md.py` en `core/`

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-03 | `core/enganches/md.py` con la lógica; el adaptador solo lee y llama | `proyectos/cimiento/core/enganches/md.py`, `adaptadores/claude-code/hook_md.py` | CA-02 | Enganche | 1 h | Ninguna | CP-002 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-04 | Pruebas y cierre con `cerrar_fase` | `proyectos/cimiento/core/proyectos/tests_rutas.py`, `proyectos/cimiento/core/enganches/tests_md.py`, la HU y la épica | CA-01, CA-02 | Documentación | 1 h | T-01 a T-03 | CP-001, CP-002 |

## 4. Secuencia de ejecución

T-01 a T-04.

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | Proyecto registrado con cada valor del ajuste, y uno sin registro | CP-001 |
| CA-02 | El enganche con una entrada de muestra | CP-002 |

## 6. Datos y ambiente de prueba

La base de pruebas de Django y carpetas temporales.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Nada que migrar.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`07·Q4`, `00·ID8`, `13·DOC14`, `02·F4`, `02·F5`, `02·F8`, `00·ID9`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Que las pruebas dependan de la máquina | Sin registro, fábrica |

## 11. Definition of Done

- [ ] CA-01 y CA-02 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Las pruebas de la fase sin fallas, y cero marcas nuevas.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Las 4 tareas quedaron hechas el 2026-10-05, con la versión 55.0.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** ninguno.
