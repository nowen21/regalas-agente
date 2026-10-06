# Plan de Trabajo · Fase `A-EP-025-HU-017-guiones-repetidos` (módulo `proyectos/cimiento/core/enganches/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-017-guiones-repetidos` |
| **Épica** | [EP-025](../../epica.md) |
| **HU** | [HU-017](../HU-017-el-freno-no-deja-escribir-un-guion-para-lo-que-cimiento-ya-hace.md), una sola (`F12.1`) |
| **Módulo** | `proyectos/cimiento/core/enganches/` |
| **Especificación del módulo** | Los CA de la [HU-017](../HU-017-el-freno-no-deja-escribir-un-guion-para-lo-que-cimiento-ya-hace.md) |
| **Fecha apertura** | 2026-10-05 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva. Sale del punto 13 del [análisis 2 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md).

**Carencias que cierra** (`02·F14` Q3): nada impide escribir otro guion para lo que ya se repite.

**Aprobación** (`02·F4`): [análisis 2 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md), el 2026-10-05, con la versión 54.4.0

**Disparo** (`02·F15`, etapa 2): el usuario pidió «continúe» el 2026-10-05, después de aprobar el análisis.

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-017 | Estado |
|---|---|
| CA-01 · Lo que Cimiento ya hace se detiene | ☑ |
| CA-02 · Lo parecido se avisa | ☑ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** el freno detiene el guion de lo que Cimiento ya hace y avisa el que se parece a uno anterior.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Detener | Programa | Media |
| CA-02 | Avisar | Programa | Media |

**Fuera de alcance:** los guiones creados por la consola.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Verificado el 2026-10-05, sobre la versión 55.0.0:

- Escribir en `historico-chat/scripts/` lo autoriza una regla (`Autorizaciones`); `Freno.decidir` devuelve «deja» y no mira el texto.
- `Freno.revisar` aplica el nivel de la regla del motivo; una decisión «avisa» llega al agente como aviso y la acción sigue.
- En `historico-chat/scripts/2026-10-05/` están `cerrar_hu_006.py` a `cerrar_hu_010.py`, que escriben `estado-fase.md`, `resultado_pruebas.md` y `funcionalidad_implementada.md`, y `clasificar_cambios_de_la_sesion.py`, que lee `historico-chat/.tocado`.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/enganches/guiones.py`, `proyectos/cimiento/core/enganches/tests_guiones.py` | Crear | Programa | El catálogo y la comparación |
| `proyectos/cimiento/core/enganches/freno.py` | Modificar | Programa | Los aplica al escribir un guion |
| `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-017-el-freno-no-deja-escribir-un-guion-para-lo-que-cimiento-ya-hace/HU-017-el-freno-no-deja-escribir-un-guion-para-lo-que-cimiento-ya-hace.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | Modificar | Documentación | La fila de la fase y el estado |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| `Freno.decidir` mira el texto de un guion | El freno antes de cada escritura | Se corre `tests_freno` |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

El aviso del freno.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Lo que Cimiento hace se reconoce por señales del texto: los archivos y carpetas que solo toca esa tarea | Por el nombre del guion | El nombre lo elige el agente; lo que escribe el guion dice qué hace | Propuesta del agente |
| Parecido es el mismo nombre sin sus números, o el 70 % del texto igual | Comparar solo el texto | Los cinco de cierre se llamaban igual salvo el número | Propuesta del agente |
| Lo parecido avisa y no detiene | Detenerlo | El acuerdo dice que avisa; puede ser una tarea nueva que se parece | Acuerdo 6 |
| El motivo cita `04·S18` | Otra regla | Es la regla que manda los guiones a esa carpeta; su nivel por proyecto se aplica igual | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  `02·F30`

No aplica: la fase no agrega acciones; el freno decide sobre lo que ya existe.

## 3. Desglose de tareas por criterio de aceptación

### CA-01 · Lo que Cimiento ya hace se detiene

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | El catálogo de lo que Cimiento hace, con su orden y sus señales | `proyectos/cimiento/core/enganches/guiones.py` | CA-01 | Freno | 1 h | Ninguna | CP-001 |
| T-02 | El freno lo aplica al escribir un `.py` en `historico-chat/scripts/` | `proyectos/cimiento/core/enganches/freno.py` | CA-01 | Freno | 0,5 h | T-01 | CP-001 |

### CA-02 · Lo parecido se avisa

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-03 | La comparación con los guiones anteriores; el freno avisa | `proyectos/cimiento/core/enganches/guiones.py`, `proyectos/cimiento/core/enganches/freno.py` | CA-02 | Freno | 1 h | T-02 | CP-002 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-04 | Pruebas y cierre con `cerrar_fase` | `proyectos/cimiento/core/enganches/tests_guiones.py`, la HU y la épica | CA-01, CA-02 | Documentación | 0,5 h | T-01 a T-03 | CP-001, CP-002 |

## 4. Secuencia de ejecución

T-01 a T-04.

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | Guiones de muestra con las señales de cada tarea | CP-001 |
| CA-02 | Un guion anterior y uno nuevo parecido | CP-002 |

## 6. Datos y ambiente de prueba

Carpetas temporales con guiones de muestra.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Nada que migrar.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`04·S18`, `07·Q4`, `02·F4`, `02·F5`, `02·F8`, `00·ID8`, `00·ID9`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Detener un guion legítimo | Señales específicas; lo parecido solo avisa; la regla se puede suspender en Cimiento |

## 11. Definition of Done

- [ ] CA-01 y CA-02 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Las pruebas de la fase sin fallas, y cero marcas nuevas.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Las 4 tareas quedaron hechas el 2026-10-05, con la versión 55.0.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** ninguno.
