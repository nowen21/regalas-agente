# Plan de Trabajo · Fase `C-EP-005-HU-009-el-arranque-cabe-en-el-canal` (módulo Adaptador y validadores)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba acepta el alcance y el costo. El requisito vive en la HU, el detalle de las pruebas en el `plan_pruebas` de la misma fase, y lo que quedó hecho en el `funcionalidad_implementada.md` del cierre.

**Versión 2, del 2026-09-28.** La versión 1 se aprobó y se construyó: T-01 a T-07 hechas, sin commit. Al construirla aparecieron textos que siguen describiendo el arranque viejo, y el usuario decidió que la HU no deje nada pendiente. Se agregan las tareas T-09 a T-15; las T-01 a T-08 conservan su número.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-005-HU-009-el-arranque-cabe-en-el-canal` |
| **Épica** | [EP-005](../../epica.md) |
| **HU** | [HU-009](../HU-009-lo-que-rige-cada-frase-llega-puesto.md), una sola (`F12.1`) |
| **Módulo** | El enganche de arranque, `validadores/` y los `CLAUDE.md` |
| **Especificación del módulo** | La regla de negocio RN-06 de la HU-009 |
| **Fecha apertura** | 2026-09-28 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- Corrige lo que dejaron las fases [`A`](../A-EP-005-HU-009-retrodocumentar-el-reparto-de-las-reglas/) y [`B`](../B-EP-005-HU-009-las-reglas-llegan-tambien-al-propio-estandar/): el arranque manda las reglas de `00` y `01` enteras, y eso no cabe en el canal. Sale del [pendiente 101](../../../../../pendientes/101-el-arranque-deja-de-mandar-las-reglas.md) y del H-1 de la sesión del 2026-09-28.

**CA de la HU que cubre esta fase** (trazabilidad `13·DOC11`):

| CA de HU-009 que cierra esta fase | Estado |
|---|---|
| [CA-04](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#ca-04--lo-que-entrega-el-arranque-cabe-entero-y-dice-cómo-llegan-las-reglas), que reemplaza al CA-01 | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que todo lo que entrega el arranque quepa en 10.000 caracteres y llegue entero al agente, en el estándar y en los proyectos. El arranque deja de mandar las reglas, que ya llegan con cada mensaje, y dice cómo llegan. Al cerrar, HU-009 y el pendiente 101 quedan terminados sin nada abierto.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-04 | Lo que entrega el arranque cabe en 10.000 caracteres y dice cómo llegan las reglas | Funcional, camino feliz | Media |
| RNF-01 | El arranque no se vuelve lento | No funcional | Baja |
| RNF-02 | Lo que no cupo se dice | No funcional | Baja |

**Fuera de alcance:**

- Cómo el recuperador elige las reglas de cada mensaje, y el recordatorio fijo de `hook_reglas.py`.
- Los otros enganches de arranque (`hook_recuerdos.py`, `hook_resumen.py`): medidos el 2026-09-28, no entregan nada al agente.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-09-28, antes de escribir este plan:

```
hook_sesion.py --raiz <estándar>        -> 85.787 caracteres (87.528 bytes)
  memoria (recuerdos.contexto)          ->  7.959 caracteres
  histórico (historico.contexto)        ->  5.073 caracteres
  gate F13, cuando no pasa (cargador)   ->  4.370 caracteres
TOPE_DEL_CANAL en hook_sesion.py        -> 72 * 1024 bytes
VERSION                                 -> 39.3.1
```

- El tope real es de 10.000 caracteres por enganche. Lo que pasa de ahí la herramienta lo guarda en un archivo fuera del repositorio y le deja al agente un avance de 2.000 (documentación de Claude Code, `hooks.md`, sección «JSON output»).
- Sin las reglas, memoria e histórico suman 13.032 caracteres: también pasan el tope. Hay que recortarlos.
- `cargador.paquete()` solo lo llama `hook_sesion.py`. Arma las reglas cuando el gate `02·F13` pasa, y solo el gate cuando no.
- Esperan las reglas al arrancar: `validadores/tests/test_las_reglas_llegan_al_propio_estandar.py`, los casos de `cargador` en `validadores/pruebas.py` y el caso `arranque-reglas-en-el-estandar` de `evals/casos.jsonl`.
- `CLAUDE.md` §0 y el paso 2 de `plantillas/CLAUDE.md.plantilla` piden cargar todos los archivos de `base/` al arrancar.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `adaptadores/claude-code/hook_sesion.py` | Modificar | Adaptador | `TOPE_DEL_CANAL` pasa a 10.000 caracteres; arma el texto por partes y recorta hasta caber |
| `validadores/cargador.py` | Modificar | Validador | Con el gate que pasa, devuelve la instrucción corta en vez de las reglas; con el gate que no pasa, el gate como hasta hoy |
| `validadores/recuerdos.py` y `validadores/historico.py` | Modificar | Validador | Aceptan un tope en caracteres: recortan por líneas y dicen dónde está el resto |
| `CLAUDE.md` y `plantillas/CLAUDE.md.plantilla` | Modificar | Estándar | Dicen cómo llegan las reglas, en vez de pedir cargarlas todas |
| `validadores/docs/cargador.md` y `validadores/docs/hook_sesion.md` | Modificar | Documentación | El ejemplo de salida y el tope |
| `validadores/tests/test_las_reglas_llegan_al_propio_estandar.py` | Modificar | Pruebas | Espera la instrucción y el tope, no las reglas |
| `validadores/pruebas.py` | Modificar | Pruebas | Los casos de `cargador` y el del tope del canal |
| `evals/casos.jsonl` | Modificar | Pruebas | El caso de arranque busca la instrucción |
| `CHANGELOG.md` y `VERSION` | Modificar | Estándar | `39.4.0`, MENOR |
| `adaptadores/claude-code/hook_reglas.py` y `validadores/recuperar.py` | Modificar | Adaptador y validador | Los avisos de cada mensaje dicen que las reglas llegan con el arranque |
| `evals/correr.py` | Modificar | Pruebas | El comentario del caso de arranque |
| `anatomia/mapa-del-sitio.md` y `base/glosario.md` | Modificar | Documentación y estándar | Describen `hook_sesion.py` y `cargador.py` como los que cargan las reglas |
| `cvds/despliegue/README.md` | Modificar | Documentación | Dice que las reglas se cargan solas al abrir |
| `notas/compactacion-mata-decisiones.md` | Modificar | Documentación | Da por resuelto que el arranque vuelva a entregar lo suyo tras resumir la conversación; antes llegaba cortado |
| `HU-009-lo-que-rige-cada-frase-llega-puesto.md` | Modificar | Documentación | RN-01 a RN-03 y CA-01 anotados como reemplazados; las seis marcas de redacción que ya tenía |
| Los documentos de esta fase, HU-009, el pendiente 101 y el resumen de la sesión | Modificar | Documentación | Cierre |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Archivo a refactorizar | Cambio de contrato | Archivos que dependen (rompen) | Dónde rompe |
|---|---|---|---|
| `validadores/cargador.py` | `paquete()` deja de devolver el texto de las reglas | `hook_sesion.py` y los casos de `pruebas.py` | Los casos que buscan `## N1` o `CARGADAS, OBLIGATORIAS` se reescriben en la fase |
| `validadores/recuerdos.py`, `validadores/historico.py` | `contexto()` suma un tope opcional | `hook_sesion.py` | Sin tope se comportan igual que hoy |
| `plantillas/CLAUDE.md.plantilla` | Cambia el paso 2 del arranque | Los `CLAUDE.md` de los proyectos | Los reescribe el instalador al reinstalar |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica: la fase no crea ningún servicio.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica: lo que cambia llega al agente al abrir la sesión.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El tope se mide en caracteres, 10.000 | Seguir en bytes | La herramienta cuenta caracteres; en bytes, una tilde vale dos y el tope quedaría mal |
| Se arma por prioridad: revisión o gate, instrucción de las reglas, memoria, histórico. Lo que no cabe se recorta desde el final | Recortar todo parejo | El gate detiene el trabajo y la memoria trae las preferencias del usuario; el histórico se puede abrir desde su índice |
| Se recorta por líneas enteras, y el bloque dice en qué archivo está el resto | Cortar a mitad de línea | Una línea cortada no dice nada; con la ruta, el agente abre lo que falta dentro del repositorio (`01·C29`) |
| La instrucción nombra `base/mapa-de-tareas.md`, `00-nucleo-blindado.md` como primero en prioridad y `01·C28` | Mandar el núcleo entero | El núcleo ya llega con cada mensaje por el recuperador cuando aplica; entero no cabe |
| Se conserva `cargador.py` para la instrucción y el gate | Pasar todo a `hook_sesion.py` | El gate ya vive ahí y tiene sus pruebas; el adaptador sigue delgado |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

## 3. Desglose de tareas por criterio de aceptación

### CA-04 · Lo que entrega el arranque cabe entero, y dice cómo llegan las reglas

> Agrupa las tareas que cambian lo que manda el arranque y los documentos que lo describen.

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `cargador.paquete()`: con el gate que pasa, la instrucción corta en vez de las reglas | Validador | 0,7 h | — | CP-001 |
| T-02 | `recuerdos.contexto()` e `historico.contexto()` con tope en caracteres, recorte por líneas y la ruta del resto | Validador | 0,7 h | — | CP-002 |
| T-03 | `hook_sesion.py`: `TOPE_DEL_CANAL` en 10.000 caracteres, el comentario con la fuente, y el armado por prioridad | Adaptador | 1 h | T-01, T-02 | CP-001, CP-002 |
| T-04 | `CLAUDE.md` §0 y el paso 2 de la plantilla dicen cómo llegan las reglas | Estándar | 0,3 h | — | CP-003 |
| T-05 | `validadores/docs/cargador.md` y `hook_sesion.md` al día | Documentación | 0,3 h | T-03 | CP-003 |
| T-06 | Reescribir las pruebas que esperaban las reglas al arrancar, y sumar la que falla por encima del tope, en el estándar y en un proyecto de prueba | Pruebas | 1 h | T-03 | CP-001, CP-002 |

### CA-04 · Ningún texto describe el arranque viejo

> Agrupa las tareas que salieron al construir la versión 1. La fase cierra con cero textos vigentes que digan que las reglas se cargan al abrir. Las fases ya cerradas y el histórico no se tocan: quedan sellados con su versión.

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-09 | Cambiar el aviso de `hook_reglas.py` («el volcado del arranque puede no haber entrado») y el de `recuperar.py` («igual que las del arranque»), con sus pruebas si las comparan | Adaptador y validador | 0,5 h | — | CP-005 |
| T-10 | Corregir el comentario de `evals/correr.py` | Pruebas | 0,1 h | — | CP-005 |
| T-11 | Corregir `anatomia/mapa-del-sitio.md` (líneas 160 y 278) y `base/glosario.md` (fila «Cargador») | Documentación | 0,3 h | — | CP-005 |
| T-12 | Corregir la fila 5 de `cvds/despliegue/README.md` | Documentación | 0,1 h | — | CP-005 |
| T-13 | Corregir el punto 7 de `notas/compactacion-mata-decisiones.md` con lo que hace el arranque ahora | Documentación | 0,2 h | — | CP-005 |
| T-14 | En HU-009, anotar RN-01 a RN-03 y CA-01 como reemplazados, y quitar las seis marcas de redacción | Documentación | 0,3 h | — | CP-005 |
| T-15 | Repetir la búsqueda en todo el repositorio y sumar el `glosario` a la entrada `39.4.0` | Trazabilidad | 0,2 h | T-09 a T-14 | CP-005 |

### RNF · Requisitos no funcionales

> Agrupa las tareas que dejan el cambio registrado y la HU cerrada.

| ID | Tarea | Categoría | Est. | Ev. |
|---|---|---|:--:|---|
| T-07 | Registrar el cambio en `CHANGELOG.md` y subir `VERSION` a `39.4.0` | Trazabilidad | 0,2 h | CP-004 |
| T-08 | Cerrar HU-009, el pendiente 101 y el H-1 de la sesión | Trazabilidad | 0,2 h | — |

**Total estimado:** 6,1 h. Hechas en la versión 1: T-01 a T-07.

## 4. Secuencia de ejecución

**Ruta crítica:** T-09 a T-14, T-15, T-08.
**Paralelizables:** T-09 a T-14 no dependen entre sí.

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-04 | Correr el enganche en el estándar y en un proyecto de prueba, contar caracteres y leer lo entregado; buscar textos viejos en todo el repositorio | CP-001 a CP-003, CP-005 | | ☐ |
| RNF | Tiempo del arranque, aviso de lo recortado, `CHANGELOG.md` y `VERSION` | CP-002, CP-004 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| CP-001 a CP-005 | Resultado de cada caso | [resultado_pruebas.md](resultado_pruebas.md) |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | El propio repositorio, y carpetas temporales para el proyecto de prueba y el gate |
| Usuarios de prueba | No aplica: no hay usuarios |
| Datos precargados | La memoria y el histórico reales del estándar, y una memoria de prueba más larga que el tope |

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit de la fase. En un proyecto ya reinstalado, se vuelve a correr el instalador con la versión anterior.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Un proyecto no tiene que hacer nada: el enganche le llega con el estándar y el instalador le reescribe el `CLAUDE.md` al reinstalar. Por eso es MENOR.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

- Base: `01·C29` (nada queda fuera del repositorio), `20·M10` (versionar), `02·F5` (solo las pruebas que la fase toca), `02·F8` (solo los archivos declarados), `02·F23`, `01·C23` (buscar antes de crear), `00·ID8`, `00·ID9`, `00·ID11` e `00·ID12` en todo lo que se escribe.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que la memoria crezca y deje sin espacio al histórico | El histórico llega solo con la ruta de su índice | Es lo que se busca: queda dicho y el índice está en el repositorio | Abierto |
| B-02 | Que la herramienta cambie su tope | El arranque vuelve a llegar cortado | El número queda en una sola constante, con la fuente citada | Abierto |

## 11. Definition of Done

- [ ] CA-04 verificado con evidencia en la sección 5
- [ ] RNF-01 y RNF-02 validados
- [ ] Las pruebas tocadas y `validar.py estandar` sin fallas
- [ ] Ningún texto vigente describe el arranque viejo
- [ ] HU-009, el pendiente 101 y el H-1 cerrados
- [ ] Commit autorizado por el usuario

## 13. Cierre

El cierre va en [funcionalidad_implementada.md](funcionalidad_implementada.md).
