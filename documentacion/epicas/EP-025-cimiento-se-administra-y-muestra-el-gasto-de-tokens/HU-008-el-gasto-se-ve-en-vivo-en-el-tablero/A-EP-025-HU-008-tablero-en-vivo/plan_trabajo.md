# Plan de Trabajo · Fase `A-EP-025-HU-008-tablero-en-vivo` (módulo `proyectos/cimiento/core/consumo/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-008-tablero-en-vivo` |
| **Épica** | [EP-025](../../epica.md) |
| **HU** | [HU-008](../HU-008-el-gasto-se-ve-en-vivo-en-el-tablero.md), una sola (`F12.1`) |
| **Módulo** | `proyectos/cimiento/core/consumo/` |
| **Especificación del módulo** | Los CA de la [HU-008](../HU-008-el-gasto-se-ve-en-vivo-en-el-tablero.md) |
| **Fecha apertura** | 2026-10-05 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva. Sale del punto 8 del [análisis 1 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md) (acuerdos 2, 5, 7, 9 y 14).

**Carencias que cierra** (`02·F14` Q3): el gasto está en la base y nadie lo ve.

**Aprobación** (`02·F4`): [análisis 1 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md), el 2026-10-04, con la versión 54.2.0

**Disparo** (`02·F15`, etapa 2): el usuario pidió «continúe» el 2026-10-05.

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-008 | Estado |
|---|---|
| CA-01 · El tablero muestra el gasto de todos los proyectos | ☐ |
| CA-02 · Se filtra por proyecto y por período | ☐ |
| CA-03 · Se actualiza solo | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** una pantalla «Gasto» con los totales y la primera tanda de niveles de todos los proyectos, que se actualiza sola.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Tablero | Programa | Media |
| CA-02 | Filtros | Programa | Baja |
| CA-03 | En vivo | Programa | Media |

**Fuera de alcance:** avisos por límite (HU-009); segunda tanda (HU-010).

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Verificado el 2026-10-05, sobre la versión 54.2.0:

- La base real tiene el gasto de 12 proyectos: unas 13 000 llamadas, 3800 enganches y 650 archivos leídos.
- `Llamada.total` suma los cuatro tipos; `GastoDeEnganche` y `GastoDeArchivo` tienen `tokens_estimados`.
- `USE_TZ = True` con `America/Bogota`: agrupar por día en la base pide las tablas de zonas horarias de MariaDB, que WAMP no trae. Se agrupa en Python.
- `templates/base.html` carga Tabler, htmx y ApexCharts con `defer`; el menú tiene «Inicio» y «Proyectos».
- `miles()` vive en la orden `leer_consumo`.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/consumo/tablero.py`, `proyectos/cimiento/core/consumo/formato.py`, `proyectos/cimiento/core/consumo/tests_tablero.py` | Crear | Programa | Las sumas, el formato de los números y sus pruebas |
| `proyectos/cimiento/core/consumo/templatetags/__init__.py`, `proyectos/cimiento/core/consumo/templatetags/gasto.py` | Crear | Pantalla | El filtro de miles |
| `proyectos/cimiento/core/consumo/templates/consumo/tablero.html`, `proyectos/cimiento/core/consumo/templates/consumo/_datos.html` | Crear | Pantalla | La página y la parte que se recarga |
| `proyectos/cimiento/core/consumo/views.py`, `proyectos/cimiento/core/consumo/urls.py`, `proyectos/cimiento/core/consumo/guardar.py`, `proyectos/cimiento/core/consumo/management/commands/leer_consumo.py` | Modificar | Programa | Las vistas, la lectura al abrir y `miles` en un solo lugar |
| `proyectos/cimiento/templates/base.html` | Modificar | Pantalla | «Gasto» en el menú |
| `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-008-el-gasto-se-ve-en-vivo-en-el-tablero/HU-008-el-gasto-se-ve-en-vivo-en-el-tablero.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | Modificar | Documentación | La fila de la fase y el estado |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| `miles()` pasa a `formato.py` | `leer_consumo` | La orden lo importa de ahí |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

| Ruta | Vista | Acceso |
|---|---|---|
| `/gasto/` | `Tablero` | Con cuenta, los dos grupos |
| `/gasto/datos/` | `DatosDelTablero` | Con cuenta, los dos grupos |

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

«Gasto» en el menú lateral.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Las sumas las hace la base, con `Sum` y `Count`; la entrada cuenta la caché creada, como `presupuesto.py` | Pasar cada fila por `Presupuesto.resumen` | 13 000 filas cada 10 segundos; la definición es la misma | RNF-01 |
| El gasto por día se agrupa en Python, con la hora de Colombia | `TruncDate` en la base | Pide tablas de zonas horarias que WAMP no trae | Línea base |
| htmx pide `/gasto/datos/` cada 10 segundos y reemplaza la parte de los números; las gráficas se redibujan con los datos que trae esa parte | Recargar la página | Así no se relee el `.jsonl` cada vez | Acuerdo 9 |
| La lectura de los `.jsonl` corre solo al abrir la página entera | Leer en cada recarga | Leer es lo lento; lo vivo llega por telemetría | Acuerdo 9 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| Gasto de tokens | Solo en la base | En el tablero, en vivo | Punto 8 |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-01 · El tablero muestra el gasto de todos los proyectos

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | `GastoDelPeriodo`: totales, por proyecto, por día, por sesión, por enganche y por archivo | `proyectos/cimiento/core/consumo/tablero.py` | CA-01 | HU-009, HU-010 | 1,5 h | Ninguna | CP-001 |
| T-02 | `miles` en `formato.py` y como filtro de plantilla | `proyectos/cimiento/core/consumo/formato.py`, `proyectos/cimiento/core/consumo/templatetags/__init__.py`, `proyectos/cimiento/core/consumo/templatetags/gasto.py`, `proyectos/cimiento/core/consumo/management/commands/leer_consumo.py` | CA-01 | La orden | 0,5 h | Ninguna | CP-001 |
| T-03 | `Tablero` y sus plantillas, con las gráficas; «Gasto» en el menú | `proyectos/cimiento/core/consumo/views.py`, `proyectos/cimiento/core/consumo/urls.py`, `proyectos/cimiento/core/consumo/templates/consumo/tablero.html`, `proyectos/cimiento/core/consumo/templates/consumo/_datos.html`, `proyectos/cimiento/templates/base.html` | CA-01 | Cimiento | 2 h | T-01, T-02 | CP-001 |

### CA-02 · Se filtra por proyecto y por período

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-04 | Filtros `proyecto` y `dias` (1, 7 o 30); lo que no vale se ignora | `proyectos/cimiento/core/consumo/views.py`, `proyectos/cimiento/core/consumo/tablero.py` | CA-02 | El tablero | 0,5 h | T-03 | CP-002 |

### CA-03 · Se actualiza solo

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-05 | `DatosDelTablero` y el `hx-trigger="every 10s"`; la página entera lee los `.jsonl` con `leer_lo_nuevo` | `proyectos/cimiento/core/consumo/views.py`, `proyectos/cimiento/core/consumo/guardar.py`, `proyectos/cimiento/core/consumo/templates/consumo/tablero.html` | CA-03 | El tablero | 1 h | T-03 | CP-003 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-06 | Pruebas; fila de la fase en la HU y estado en la épica | `proyectos/cimiento/core/consumo/tests_tablero.py`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-008-el-gasto-se-ve-en-vivo-en-el-tablero/HU-008-el-gasto-se-ve-en-vivo-en-el-tablero.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | CA-01 a CA-03 | Documentación | 1 h | T-01 a T-05 | CP-001 a CP-003 |

## 4. Secuencia de ejecución

T-01 y T-02; T-03, T-04, T-05 y al final T-06, con las pruebas de la fase (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | Datos de muestra de dos proyectos; la página con el gasto real | CP-001 |
| CA-02 | Filtro por proyecto, por período y con valores que no existen | CP-002 |
| CA-03 | La parte que se recarga trae lo nuevo; abrir la página lee el `.jsonl` | CP-003 |

## 6. Datos y ambiente de prueba

Llamadas, enganches y archivos creados en la base de pruebas; un `.jsonl` de muestra en una carpeta temporal.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase. No hay migración.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Aditiva: pantallas nuevas.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`04`, `06`, `07·Q4`, `00·ID12` (miles con punto), `02·F4`, `02·F5`, `02·F8`, `00·ID8`, `00·ID9`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| La primera lectura al abrir tarde | Solo lee los archivos que cambiaron |

## 11. Definition of Done

- [ ] CA-01 a CA-03 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Las pruebas de la fase sin fallas, y cero marcas nuevas.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Las 6 tareas quedaron hechas el 2026-10-05, con la versión 54.2.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** ninguno.
