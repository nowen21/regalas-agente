# Plan de Trabajo · Fase `A-EP-016-HU-005-la-promesa-dice-cuando-llegan-las-reglas` (módulo Reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba acepta el alcance y el costo. El requisito vive en la HU, el detalle de las pruebas en el `plan_pruebas` de la misma fase, y lo que quedó hecho en el `funcionalidad_implementada.md` del cierre.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-016-HU-005-la-promesa-dice-cuando-llegan-las-reglas` |
| **Épica** | [EP-016](../../epica.md) |
| **HU** | [HU-005](../HU-005-entregarle-las-reglas-al-agente.md), una sola (`F12.1`) |
| **Módulo** | Reglas |
| **Especificación del módulo** | La funcionalidad `F-009` del [inventario](../../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Fecha apertura** | 2026-09-28 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- Sale de la fase [`C` de EP-005 HU-009](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-009-lo-que-rige-cada-frase-llega-puesto/C-EP-005-HU-009-el-arranque-cabe-en-el-canal/plan_trabajo.md). Desde la versión 39.4.0 las reglas ya no se cargan al abrir la sesión, porque no caben en el canal de la herramienta: 10.000 caracteres por enganche. Llegan con cada mensaje las que aplican a lo que se pide. La plataforma sigue prometiendo que llegan «al abrir, sin pedirlas». El usuario decidió corregir esa promesa, en una fase propia de la plataforma (`02·F11`).

**CA de la HU que cubre esta fase** (trazabilidad `13·DOC11`):

| CA de HU-005 que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-005-entregarle-las-reglas-al-agente.md#ca-01--cuando-se-piden-salen-las-reglas-con-su-texto), que cambia de título | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que ningún documento de la plataforma prometa que las reglas llegan al abrir la sesión. Deben decir lo que pasa: con cada mensaje llegan las reglas de la tarea, y enteras cuando se piden.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | La promesa dice cuándo llegan las reglas | Documental | Baja |

**Fuera de alcance:**

- El código de `plataforma/nucleo/reglas/entrega.py`: entrega las reglas cuando se le piden, y eso no cambia.
- `prompts/`: guarda las palabras del usuario tal como las dijo.
- Las fases cerradas, que quedan fijas con su versión.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-09-28:

- `F-009` se llama «Entregarle las reglas al agente al abrir sesión», y su `CA-1` dice «al abrir, el agente tiene las reglas sin pedirlas».
- Lo construido en la fase `K` es `entregar`: devuelve las 248 reglas enteras, unos 680.000 caracteres, cuando se le pide. No está conectado al arranque, y no cabría: el tope es de 10.000.
- El título del CA-01 de HU-005 dice «Al abrir», y su escenario dice «Cuando se piden sus reglas». Se probó el escenario.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `documentacion/epicas/EP-016-…/HU-005-…/HU-005-entregarle-las-reglas-al-agente.md` | Modificar | Documentación | Narrativa, contexto y título del CA-01; estado de la historia y bitácora |
| `documentacion/epicas/EP-016-…/epica.md` | Modificar | Documentación | Líneas 54, 71 y 107 |
| `cvds/analisis-requisitos/README.md` | Modificar | Documentación | `RF-09` |
| `cvds/analisis-requisitos/inventario-funcionalidades.md` | Modificar | Documentación | `F-009`: la fila del resumen y su ficha |
| `cvds/pruebas/README.md` | Modificar | Documentación | La fila de la prueba de integración |
| `cvds/planificacion/README.md` | Modificar | Documentación | El riesgo 1 y la dependencia de la herramienta |
| `cvds/diseno/decisiones-de-arquitectura.md` | Modificar | Documentación | Cuándo se revisaría la decisión |
| Los documentos de esta fase | Crear | Documentación | Cierre |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

No aplica: no cambia ningún programa.

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| `F-009` pasa a llamarse «Entregarle al agente las reglas que rigen en el proyecto» | Dejar «al abrir sesión» | Al abrir no caben; con cada mensaje llegan las de la tarea (EP-005 HU-023) y enteras cuando se piden (`entregar`) |
| El CA-01 de HU-005 pasa a llamarse «Cuando se piden, salen las reglas con su texto» | Reescribir su escenario | El escenario ya dice «cuando se piden», y es lo que se probó; solo el título prometía otra cosa |
| No se crea regla nueva ni se toca el código | Conectar `entregar` al arranque | No cabe en el canal |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

## 3. Desglose de tareas por criterio de aceptación

### CA-01 · La promesa dice cuándo llegan las reglas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | HU-005: narrativa, contexto que explique por qué no al abrir, título del CA-01, estado y bitácora | Documentación | 0,3 h | — | CP-001 |
| T-02 | `epica.md` de EP-016: las tres líneas | Documentación | 0,1 h | — | CP-001 |
| T-03 | `RF-09` y `F-009`, en el análisis y el inventario | Documentación | 0,3 h | — | CP-001 |
| T-04 | Pruebas, planificación y decisiones de arquitectura en `cvds/` | Documentación | 0,2 h | — | CP-001 |
| T-05 | Buscar «al abrir» junto a «reglas» en la plataforma y en `cvds/`, y cerrar la fase | Trazabilidad | 0,2 h | T-01 a T-04 | CP-001 |

**Total estimado:** 1,1 h.

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 a T-04 en cualquier orden, y T-05 al final.

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Búsqueda en los documentos y `validar.py estandar` | CP-001 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| CP-001 | Resultado del caso | [resultado_pruebas.md](resultado_pruebas.md) |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | El propio repositorio |
| Usuarios de prueba | No aplica |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit de la fase.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

No cambia nada en producción: son documentos de la plataforma. No toca `base/` ni `plantillas/`, así que no sube la versión del estándar.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

- Base: `02·F11` (una fase por módulo), `02·F8` (solo los archivos declarados), `02·F23`, `00·ID8`, `00·ID9`, `00·ID11` e `00·ID12` en todo lo que se escribe.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que otro documento de la plataforma repita la promesa con otras palabras | Queda una promesa falsa | La T-05 busca por las dos palabras juntas, no por una frase exacta | Abierto |

## 11. Definition of Done

- [ ] CA-01 verificado con evidencia en la sección 5
- [ ] `validar.py estandar` sin fallas
- [ ] Ningún documento vigente de la plataforma promete las reglas al abrir
- [ ] Commit autorizado por el usuario

## 13. Cierre

El cierre va en [funcionalidad_implementada.md](funcionalidad_implementada.md).
