# Plan de Trabajo · Fase `B-EP-005-HU-023-todas-las-reglas-declaran-sus-tareas` (módulo Cuerpo de reglas y validadores)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba acepta el alcance y el costo. El requisito vive en la HU, el detalle de las pruebas en el `plan_pruebas` de la misma fase, y lo que quedó hecho en el `funcionalidad_implementada.md` del cierre.

**Versión 2, del 2026-09-28.** La versión 1 se aprobó y se empezó a construir. En la T-10 apareció que el recuperador de reglas por solicitud ya existía y fallaba (H-9 de la sesión), y el usuario eligió que esta fase lo haga trabajar con el mapa. Se agregan RN-06, CA-07 y las tareas T-13 a T-16; las T-01 a T-12 conservan su número.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-005-HU-023-todas-las-reglas-declaran-sus-tareas` |
| **Épica** | [EP-005](../../epica.md) |
| **HU** | [HU-023](../HU-023-cada-tarea-sabe-que-reglas-le-aplican.md), una sola (`F12.1`) |
| **Módulo** | Cuerpo de reglas, `validadores/` y el adaptador |
| **Especificación del módulo** | Las reglas de negocio RN-04 a RN-06 de la HU-023 |
| **Fecha apertura** | 2026-09-28 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- Híbrido. Retoma la [fase `A`](../A-EP-005-HU-023-la-lista-de-tareas-y-el-mapa/funcionalidad_implementada.md), que dejó la lista, la línea en el núcleo y el programa del mapa. Suma la corrección del validador del amarre (H-8) y hacer que el recuperador de reglas existente, `validadores/recuperar.py`, trabaje con el mapa (H-9).

**CA de la HU que cubre esta fase** (trazabilidad `13·DOC11`):

| CA de HU-023 que cierra esta fase | Estado |
|---|---|
| [CA-04](../HU-023-cada-tarea-sabe-que-reglas-le-aplican.md#ca-04--el-validador-detecta-lo-que-falta-o-no-cuadra) | ☐ |
| [CA-05](../HU-023-cada-tarea-sabe-que-reglas-le-aplican.md#ca-05--toda-regla-vigente-declara-sus-tareas) | ☐ |
| [CA-06](../HU-023-cada-tarea-sabe-que-reglas-le-aplican.md#ca-06--el-mapa-del-amarre-no-da-por-clasificado-lo-que-solo-se-nombra) | ☐ |
| [CA-07](../HU-023-cada-tarea-sabe-que-reglas-le-aplican.md#ca-07--el-recuperador-trae-las-reglas-de-la-tarea-que-pide-el-mensaje) | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que las 252 reglas vigentes declaren sus tareas, que un validador lo exija antes de publicar, que el validador del amarre no se deje engañar, y que con cada mensaje el agente reciba las reglas de las tareas que el mensaje pide. Al cerrar, HU-023 queda terminada sin nada abierto.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-04 | Regla sin tareas, tarea fuera de la lista o mapa viejo: el validador falla | Funcional, error | Media |
| CA-05 | Las 252 reglas vigentes declaran sus tareas | Funcional, camino feliz | Alta |
| CA-06 | El validador del amarre no se deja engañar por una mención | Funcional, error | Media |
| CA-07 | El mensaje trae las reglas de su tarea, y siempre las de pedido y respuesta | Funcional, camino feliz | Alta |
| RNF-01 | Versionado | No funcional | Baja |
| RNF-02 | Lo nuevo y lo cambiado tienen sus pruebas | No funcional | Baja |

**Fuera de alcance:**

- Cambiar qué exige cualquier regla.
- El recordatorio fijo de `hook_reglas.py` (`CADA_TURNO`) y la medición de la respuesta anterior: siguen como están.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medida el 2026-09-28, antes de escribir esta versión:

```
metareglas.py: 261 reglas, 252 vigentes y 9 derogadas; con línea Aplica a: 10
validar.py tareas: existe (T-01 a T-03 hechas)
validar.py amarre: 2 fallas (hook_reglas.py y recuperar.py sin clasificar)
recuperar.py, con tres mensajes de la sesión:
  «suba a git»                         -> ninguna regla
  «cree el pendiente del H2»           -> F23, F0
  «aplique las reglas de la caja ...»  -> DOC17
.claude/settings.json del estándar: sin hook_reglas.py
VERSION: 39.2.0
```

Por qué falla el recuperador hoy:

- Compara solo palabras de cuatro letras o más, así que «git» no cuenta; y no reconoce otras formas del verbo («suba» no es «subir»).
- No recupera los capítulos `00` y `01` (`SIEMPRE`, línea 116), porque supone que llegaron enteros al arrancar. Hoy llegan cortados.
- Elige por semejanza de palabras con el título de la regla, y eso trae reglas que no vienen al caso.

`hook_reglas.py` llama a `recuperar.como_texto()` con el mensaje; basta cambiar el recuperador. `instalar.py` ya conecta el enganche en los proyectos (línea 284).

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/mapa_tareas.py` | Modificar | Validador | La función que reporta lo que no cuadra, y la que devuelve las reglas de cada tarea y las palabras de cada una |
| `validadores/validar.py` | Modificar | Validador | El subcomando `tareas` |
| `validadores/instalar.py` y `.githooks/pre-push` | Modificar | Validador | `tareas` entre lo que detiene la publicación |
| `validadores/amarre.py` | Modificar | Validador | Clasificado es solo una fila de tabla o una línea de nombres |
| `validadores/recuperar.py` | Modificar | Validador | Elige por las tareas del mensaje, con el mapa; sin excluir `00` y `01`; sin semejanza de títulos |
| `validadores/pruebas.py` | Modificar | Pruebas | Los casos del recuperador, con los mensajes de la sesión |
| `validadores/tests/test_cada_tarea_sabe_que_reglas_le_aplican.py` y `validadores/tests/test_el_mapa_del_amarre_no_envejece.py` | Modificar | Pruebas | Los casos del validador y de la corrección del amarre |
| `base/tareas.md` | Modificar | Estándar | Una columna con las palabras del pedido que señalan cada tarea |
| Los archivos de `base/` con reglas vigentes | Modificar | Estándar | La línea `**Aplica a:**` en las 242 que faltan |
| `base/mapa-de-tareas.md` | Modificar | Estándar | Lo vuelve a escribir el programa |
| `anatomia/que-esta-amarrado-a-la-herramienta.md` | Modificar | Documentación | `hook_reglas.py` y `recuperar.py` clasificados, con el recuento |
| `.claude/settings.json` | Modificar | Adaptador | `hook_reglas.py` en `UserPromptSubmit`, como lo pone `instalar.py` en los proyectos |
| `historico-chat/scripts/2026-09-28/` | Nuevo | Apoyo | El guion que pone las líneas desde la tabla de clasificación, con su `README.md` |
| `CHANGELOG.md` y `VERSION` | Modificar | Estándar | `39.3.0`, MENOR |
| Los documentos de esta fase, HU-023, el pendiente 100 y el resumen de la sesión | Modificar | Documentación | Cierre |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Archivo a refactorizar | Cambio de contrato | Archivos que dependen (rompen) | Dónde rompe |
|---|---|---|---|
| `validadores/amarre.py` | `validar()` deja de aceptar menciones sueltas | `validar.py amarre` y sus pruebas | Los dos programas sin clasificar se clasifican en la fase |
| `validadores/instalar.py` | El enganche `pre-push` suma `tareas` | Los proyectos, al reinstalar | Donde no hay reglas en `base/`, no reporta nada |
| `validadores/recuperar.py` | `elegir()` y `como_texto()` eligen por tareas; se quitan la semejanza y los disparadores | `hook_reglas.py` y los casos de `pruebas.py` | `hook_reglas.py` usa solo `como_texto()`, que conserva su firma. Los casos que esperaban la semejanza se reescriben |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica: la fase no crea ningún servicio.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica: no hay pantalla. Las reglas le llegan al agente en cada mensaje, por el enganche.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El recuperador elige por tareas y usa el mapa | Mantener la semejanza de palabras | La semejanza trajo `DOC17` para un pedido de redacción; las tareas dicen qué reglas aplican sin adivinar |
| Las palabras que señalan cada tarea van en `base/tareas.md`, con sus formas escritas («subir», «suba», «súbalo») | Comparar raíces de palabras | Una lista escrita se lee y se corrige; una raíz automática se equivoca sin que se vea por qué |
| `recibir-pedido` y `responder` van en todo mensaje | Que un saludo no traiga nada, como pedía el recuperador | Esas reglas rigen todo mensaje, «hola» incluido. El caso de prueba que esperaba cero reglas ante un saludo cambia |
| Sin excluir `00` ni `01` | Mantener `SIEMPRE` | La exclusión suponía que llegaban al arrancar, y no llegan |
| El validador detiene el `pre-push` | Que solo avise | Si solo avisa, una regla nueva sin tareas entra y el mapa envejece |
| Las líneas se ponen con un guion desde una tabla que llena el agente leyendo cada regla | 242 ediciones a mano | La decisión es del agente, regla por regla; el guion solo la escribe y queda en `historico-chat/scripts/` |
| Clasificado en el amarre es fila de tabla o línea de nombres | Solo fila de tabla | El mapa ya usa las dos formas |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

## 3. Desglose de tareas por criterio de aceptación

### CA-04 · El validador detecta lo que falta o no cuadra

> Agrupa las tareas que escriben el validador y lo dejan corriendo solo antes de publicar.

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | La función que reporta lo que no cuadra, en `mapa_tareas.py` | Validador | 1 h | — | CP-001 |
| T-02 | El subcomando `tareas` en `validar.py` | Validador | 0,3 h | T-01 | CP-001 |
| T-03 | `tareas` en el `pre-push` de `instalar.py` y en `.githooks/pre-push` | Validador | 0,5 h | T-02 | CP-001 |
| T-04 | Las pruebas del validador | Pruebas | 0,7 h | T-01 | CP-001 |

### CA-05 · Toda regla vigente declara sus tareas

> Agrupa las tareas que anotan las 242 reglas que faltan.

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-05 | Leer cada regla vigente sin línea y decidir sus tareas, capítulo por capítulo, en una tabla | Estándar | 4 h | — | CP-002 |
| T-06 | Poner las 242 líneas con el guion, desde esa tabla | Estándar | 0,5 h | T-05 | CP-002 |
| T-07 | Volver a escribir el mapa y correr el validador | Estándar | 0,2 h | T-01, T-06 | CP-002 |

### CA-06 · El mapa del amarre no da por clasificado lo que solo se nombra

> Agrupa las tareas que corrigen el validador del amarre y completan su mapa.

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-08 | `amarre.py`: clasificado es solo una fila de tabla o una línea de nombres | Validador | 0,7 h | — | CP-003 |
| T-09 | Sus pruebas: la mención en una frase no clasifica; la fila y la lista sí | Pruebas | 0,5 h | T-08 | CP-003 |
| T-10 | Clasificar `hook_reglas.py` y `recuperar.py` en el mapa del amarre, con el recuento | Documentación | 0,3 h | T-08 | CP-003 |

### CA-07 · El recuperador trae las reglas de la tarea que pide el mensaje

> Agrupa las tareas que hacen trabajar al recuperador con el mapa y lo conectan en el estándar.

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-13 | Agregar a `base/tareas.md` la columna con las palabras del pedido que señalan cada tarea, y que `mapa_tareas.py` la lea | Estándar | 0,7 h | — | CP-005 |
| T-14 | Cambiar `recuperar.py`: reconoce las tareas del mensaje, suma siempre `recibir-pedido` y `responder`, trae las reglas del mapa y las que el mensaje cita, sin excluir `00` y `01` y sin semejanza de títulos | Validador | 2 h | T-07, T-13 | CP-005 |
| T-15 | Reescribir los casos del recuperador en `pruebas.py` con los mensajes de la sesión | Pruebas | 1 h | T-14 | CP-005 |
| T-16 | Conectar `hook_reglas.py` en `.claude/settings.json` del estándar | Adaptador | 0,2 h | T-14 | CP-005 |

### RNF · Requisitos no funcionales

> Agrupa las tareas que dejan el cambio registrado y la HU cerrada.

| ID | Tarea | Categoría | Est. | Ev. |
|---|---|---|:--:|---|
| T-11 | Registrar el cambio en `CHANGELOG.md` y subir `VERSION` a `39.3.0` | Trazabilidad | 0,2 h | CP-004 |
| T-12 | Cerrar HU-023, el pendiente 100 y los hallazgos H-7, H-8 y H-9 | Trazabilidad | 0,2 h | — |

**Total estimado:** 13 h. Hechas antes de esta versión: T-01 a T-04 y T-08.

## 4. Secuencia de ejecución

**Ruta crítica:** T-05, T-06, T-07, T-14, T-15, T-16, T-11, T-12.
**Paralelizables:** T-09, T-10 y T-13 no esperan la clasificación.

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-04 | Pruebas del validador y `validar.py tareas` | CP-001 | | ☐ |
| CA-05 | `validar.py tareas` con 0 reglas sin tareas, y el mapa con 252 | CP-002 | | ☐ |
| CA-06 | Pruebas del amarre y `validar.py amarre` con 0 fallas | CP-003 | | ☐ |
| CA-07 | Los mensajes de la sesión contra el recuperador, y el enganche conectado | CP-005 | | ☐ |
| RNF | `CHANGELOG.md`, `VERSION` y las pruebas | CP-004 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| CP-001 a CP-005 | Resultado de cada caso | [resultado_pruebas.md](resultado_pruebas.md) |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | El propio repositorio, y carpetas temporales de las pruebas para los casos que rompen algo a propósito |
| Usuarios de prueba | No aplica: no hay usuarios |
| Datos precargados | Los mensajes reales de la sesión del 2026-09-28 |

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit de la fase. Si ya se reinstaló el enganche en un proyecto, se vuelve a correr el instalador con la versión anterior.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Un proyecto no tiene que tocar ningún archivo: el recuperador le llega con el estándar, y al reinstalar su `pre-push` suma `tareas`, que no reporta nada donde no hay reglas en `base/`. Por eso es MENOR.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

- Base: `20·M5` (la línea queda fuera del cuerpo), `20·M10` (versionar), `02·F4` (el plan que cambia se vuelve a aprobar), `02·F8` (solo los archivos declarados), `02·F23`, `01·C23` (buscar antes de crear), `01·C29` (el guion queda en el repositorio), `00·ID8`, `00·ID9`, `00·ID11` e `00·ID12` en todo lo que se escribe.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que una regla quede con tareas equivocadas | El agente recibe una regla que no aplica, o no recibe la que sí | El validador comprueba la lista, no el acierto. Se le muestra al usuario un resumen por tarea antes de cerrar | Abierto |
| B-02 | Que agregar `tareas` al `pre-push` rompa las pruebas del instalador | Fallan pruebas que comparan el enganche | Se corren en la fase y se ajustan las que comparan el texto | Abierto |
| B-03 | Que `recibir-pedido` y `responder` traigan tantas reglas que pasen el tope de 10 KB por mensaje | Parte de las reglas va a «no cupo» | Se mide en la T-15. Lo que no cabe sale nombrado, con la orden de leerlo, como ya hace el recuperador | Abierto |
| B-04 | Que una palabra del pedido active una tarea que no es | Llegan reglas de más | Las palabras son una lista escrita; se prueban con los mensajes de la sesión | Abierto |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] RNF-01 y RNF-02 validados
- [ ] `tareas`, `amarre`, `metareglas`, `estandar` y las pruebas tocadas sin fallas
- [ ] HU-023, el pendiente 100, H-7, H-8 y H-9 cerrados
- [ ] Commit autorizado por el usuario

## 13. Cierre

El cierre va en [funcionalidad_implementada.md](funcionalidad_implementada.md).
