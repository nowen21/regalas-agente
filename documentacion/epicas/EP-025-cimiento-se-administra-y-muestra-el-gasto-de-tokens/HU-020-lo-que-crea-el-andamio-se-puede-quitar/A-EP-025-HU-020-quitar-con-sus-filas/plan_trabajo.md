# Plan de Trabajo · Fase `A-EP-025-HU-020-quitar-con-sus-filas` (módulo `proyectos/cimiento/core/herramientas/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-020-quitar-con-sus-filas` |
| **Épica** | [EP-025](../../epica.md) |
| **HU** | [HU-020](../HU-020-lo-que-crea-el-andamio-se-puede-quitar.md), una sola (`F12.1`) |
| **Módulo** | `proyectos/cimiento/core/herramientas/` |
| **Especificación del módulo** | Los CA de la [HU-020](../HU-020-lo-que-crea-el-andamio-se-puede-quitar.md) |
| **Fecha apertura** | 2026-10-05 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva. Sale del punto 5 del [análisis 3 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md) (acuerdos 1 y 4).

**Carencias que cierra** (`02·F14` Q3): lo que crea el andamio no se puede quitar.

**Aprobación** (`02·F4`): [análisis 3 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md), el 2026-10-05, con la versión 54.3.0

**Disparo** (`02·F15`, etapa 2): el usuario pidió «continúe» el 2026-10-05, después de aprobar el análisis.

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-020 | Estado |
|---|---|
| CA-01 · Lo que sigue siendo plantilla se borra con sus filas | ☐ |
| CA-02 · Lo que tiene trabajo se archiva | ☐ |
| CA-03 · Lo que no se puede quitar se dice | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** `andamio quitar «carpeta»` deshace lo que el andamio creó: borra si sigue siendo plantilla y archiva si tiene trabajo.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Borrar plantilla | Programa | Media |
| CA-02 | Archivar | Programa | Media |
| CA-03 | Rechazos y simulación | Programa | Baja |

**Fuera de alcance:** quitar desde la interfaz.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Verificado el 2026-10-05, sobre la versión 54.3.0:

- `Andamio.crear_hu` escribe la HU y su README, y agrega una fila en `epica.md` (después de `## 9.`) y otra en el `README.md` de la épica si existe. `crear` escribe los cinco documentos de la fase; `crear_pendiente`, el `pendiente.md`. Los textos salen de las plantillas del estándar con `reenlazar` y sustituciones.
- `siguiente_hu` cuenta las carpetas `HU-NNN-` de la épica; `siguiente_consecutivo`, las fases de la HU.
- `validadores/andamio.py` llama a `main` de `core/herramientas/andamio.py`.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/herramientas/andamio.py`, `proyectos/cimiento/core/herramientas/tests_andamio.py` | Modificar | Programa | `quitar` y sus pruebas |
| `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-020-lo-que-crea-el-andamio-se-puede-quitar/HU-020-lo-que-crea-el-andamio-se-puede-quitar.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | Modificar | Documentación | La fila de la fase y el estado |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| Los textos de la HU, la fase y el pendiente se arman en funciones aparte | `crear_hu`, `crear`, `crear_pendiente` | Escriben lo mismo que antes; se corren sus pruebas |
| `siguiente_hu` cuenta también lo archivado | `crear_hu` | Un número archivado no se reusa |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

`python validadores/andamio.py quitar «carpeta» [--aplicar]`.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| «Sigue siendo plantilla» es: idéntico, archivo por archivo, a lo que el andamio crearía hoy, y sin archivos de más | Buscar marcadores «…» | Un marcador queda aunque se haya escrito mucho alrededor | Propuesta del agente |
| Archivar es mover a `_archivo/` de la misma carpeta padre | Una carpeta global | Queda junto a sus hermanas y la fila solo cambia la ruta | Propuesta del agente |
| Una HU con fases no se quita | Quitarla con todo | Se perdería el rastro de las fases | RN-05 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| Andamio | Crea | Crea y quita | Acuerdo 2 del análisis 3 |

## 3. Desglose de tareas por criterio de aceptación

### CA-01 · Lo que sigue siendo plantilla se borra con sus filas

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | Sacar a funciones los textos que el andamio crea para una HU, una fase y un pendiente | `proyectos/cimiento/core/herramientas/andamio.py` | CA-01 | El andamio | 1 h | Ninguna | CP-001 |
| T-02 | `Andamio.quitar(carpeta, escribir)`: reconoce si es HU, fase o pendiente, compara, borra la carpeta y las filas | `proyectos/cimiento/core/herramientas/andamio.py` | CA-01 | El andamio | 1,5 h | T-01 | CP-001 |

### CA-02 · Lo que tiene trabajo se archiva

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-03 | Archivar en `_archivo/`, la fila apuntando ahí con «(archivada)»; `siguiente_hu` cuenta lo archivado | `proyectos/cimiento/core/herramientas/andamio.py` | CA-02 | El andamio | 1 h | T-02 | CP-002 |

### CA-03 · Lo que no se puede quitar se dice

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-04 | Rechazar una HU con fases o una carpeta que no es del andamio; simular sin `--aplicar`; el modo `quitar` en `main` | `proyectos/cimiento/core/herramientas/andamio.py` | CA-03 | El andamio | 0,5 h | T-02 | CP-003 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-05 | Pruebas; fila de la fase en la HU y estado en la épica | `proyectos/cimiento/core/herramientas/tests_andamio.py`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-020-lo-que-crea-el-andamio-se-puede-quitar/HU-020-lo-que-crea-el-andamio-se-puede-quitar.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | CA-01 a CA-03 | Documentación | 1 h | T-01 a T-04 | CP-001 a CP-003 |

## 4. Secuencia de ejecución

T-01, T-02, T-03, T-04 y al final T-05, con las pruebas de la fase (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | Crear y quitar una HU, una fase y un pendiente en una carpeta temporal | CP-001 |
| CA-02 | Cambiar una HU y quitarla | CP-002 |
| CA-03 | HU con fases, carpeta ajena y simulación | CP-003 |

## 6. Datos y ambiente de prueba

Carpetas temporales con una épica de muestra; las plantillas del estándar.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Aditiva: un modo nuevo del andamio.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`02·F4`, `02·F5`, `02·F8`, `00·ID8`, `00·ID9`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Borrar algo con trabajo | Solo se borra lo idéntico; lo demás se archiva |

## 11. Definition of Done

- [ ] CA-01 a CA-03 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Las pruebas de la fase sin fallas, y cero marcas nuevas.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Las 5 tareas quedaron hechas el 2026-10-05, con la versión 54.4.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** ninguno.
