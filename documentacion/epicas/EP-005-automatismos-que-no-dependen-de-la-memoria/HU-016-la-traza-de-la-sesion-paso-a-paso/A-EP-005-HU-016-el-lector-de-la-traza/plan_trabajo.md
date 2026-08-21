# Plan de Trabajo — Fase A-EP-005-HU-016-el-lector-de-la-traza (módulo Automatismos — lectores de la sesión)

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden y sobre qué archivos, y cómo se comprueba cada criterio antes de darlo por cumplido. Se aprueba antes de tocar nada. El requisito vive en la HU; las pruebas, en el [plan_pruebas.md](plan_pruebas.md); lo que dieron, en el [resultado_pruebas.md](resultado_pruebas.md); lo que quedó, en el [funcionalidad_implementada.md](funcionalidad_implementada.md).

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-005-HU-016-el-lector-de-la-traza` |
| **Épica** | [EP-005 Automatismos que no dependen de la memoria](../../epica.md) |
| **HU** | [HU-016 La traza de la sesión, paso a paso](../HU-016-la-traza-de-la-sesion-paso-a-paso.md) — una sola ([`02·F12.1`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) |
| **Módulo** | Automatismos — lectores de la sesión |
| **Especificación del módulo** | [documentacion/automatismos/spec.md](../../../../automatismos/spec.md) |
| **Fecha apertura** | 2026-08-20 |
| **Rama** | `main` — el repositorio del estándar trabaja sobre su rama principal, con el commit autorizado aparte |

**ORIGEN:** ✨ **Funcionalidad nueva.** Sale del [pendientes/hecho/la-sesion-tiene-su-traza.md](../../../../../pendientes/hecho/la-sesion-tiene-su-traza.md): la transcripción interna registra cada paso y nadie lo lee.

**CA de la HU que cubre esta fase:**

| CA de HU-016 que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-016-la-traza-de-la-sesion-paso-a-paso.md#ca-01--la-línea-de-tiempo-de-una-sesión) · la línea de tiempo | ☐ |
| [CA-02](../HU-016-la-traza-de-la-sesion-paso-a-paso.md#ca-02--el-cierre-dice-los-totales) · el cierre | ☐ |
| [CA-03](../HU-016-la-traza-de-la-sesion-paso-a-paso.md#ca-03--con---escribir-queda-junto-al-histórico-indexada) · `--escribir` junto al histórico | ☐ |
| [CA-04](../HU-016-la-traza-de-la-sesion-paso-a-paso.md#ca-04--lo-raro-no-revienta) · lo raro no revienta | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** un lector, `validadores/traza.py`, expuesto como `validar.py traza`, que de una transcripción saque la línea de tiempo de los pasos (hora, herramienta, entrada recortada, duración, estado) y su cierre, y que con `--escribir` la deje en `historico-chat/trazas/` con el nombre del histórico de esa sesión. Sin enganches ni cambios en los proyectos.

**Fuera de alcance:**

- Escribirla sola al cerrar: sería un enganche, otra historia.
- Tapar claves dentro de la entrada recortada.
- Trazar lo que la herramienta no registra.

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

Leído el 2026-08-20:

- Una transcripción real de este repositorio (1 MB, 112 líneas del agente): los bloques `tool_use` van en `message.content` de las líneas `type: assistant` con `timestamp` ISO 8601; los `tool_result` en las líneas `type: user`, con `tool_use_id` e `is_error`. Hay líneas de otros tipos (`attachment`, `system`, `queue-operation`) que se ignoran.
- [adaptadores/claude-code/hook_presupuesto.py](../../../../../adaptadores/claude-code/hook_presupuesto.py) `consumos_de_transcripcion`: cómo se lee línea a línea saltando lo ilegible. Se sigue el mismo patrón, pero en `validadores/` (RN-07), como [validadores/brevedad.py](../../../../../validadores/brevedad.py), que ya lee transcripciones allí.
- [validadores/historico.py](../../../../../validadores/historico.py) línea 179 `_archivo`: encuentra el histórico de una sesión por la marca `<!-- sesion: id -->`; línea 217 `_indexar`: agrega la línea al README si no está. Se reutilizan las dos ideas; `_archivo` es privada y se le da un nombre público.
- [validadores/validar.py](../../../../../validadores/validar.py): registro de subcomandos por `import` y `add_parser`; `comun.no_es_punto_de_entrada()` en el módulo.
- [validadores/amarre.py](../../../../../validadores/amarre.py): reporta un programa de `validadores/` que nombre la herramienta. `traza.py` no la nombra.
- [anatomia/mapa-del-sitio.md](../../../../../anatomia/mapa-del-sitio.md) línea 142: filas de `validadores/`.
- [documentacion/automatismos/spec.md](../../../../automatismos/spec.md): §4.7 última sección de reglas; §13 trazabilidad.
- [historico-chat/README.md](../../../../../historico-chat/README.md): explica qué hay en la carpeta; le falta decir qué es `trazas/`.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/traza.py` | Nuevo | `pasos(ruta)`, `cierre(pasos)`, `como_texto(pasos, cierre)`, `escribir(raiz, sesion, texto)`, `registrar(sub)` |
| `validadores/validar.py` | Modificar | `import traza` y el subcomando `traza <transcripción> [--escribir] [--raiz]` |
| `validadores/historico.py` | Modificar | `archivo_de_sesion(raiz, sesion)` público sobre `_archivo(..., crear=False)`; una línea |
| `validadores/tests/test_la_sesion_tiene_traza.py` | Nuevo | Los casos |
| `historico-chat/README.md` | Modificar | Un párrafo: qué es `trazas/` y cómo se produce |
| `anatomia/mapa-del-sitio.md` | Modificar | La fila de `traza.py` |
| `documentacion/automatismos/spec.md` | Modificar | §4.9 con las RN y §13 |
| `CHANGELOG.md` · `VERSION` | Modificar | La misma entrada 28.0.0 de la fase del portero |

### 2.2 Matriz de dependencias del refactor

| Archivo a refactorizar | Cambio de contrato | Archivos que dependen (rompen) | Dónde rompe |
|---|---|---|---|
| `validadores/historico.py` | Se **agrega** `archivo_de_sesion`; `_archivo` no cambia | Ninguno | — |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

No aplica porque no hay servicio: es un programa de línea de comandos.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

No aplica porque no hay interfaz: la traza se imprime o se escribe en `historico-chat/trazas/`.

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **Lector a demanda**, no enganche | Escribirla en el evento de cierre, como el consumo | Cero cambios en nueve proyectos; la traza se necesita cuando algo salió mal, no en cada respuesta. Si después conviene, es un enganche de una línea sobre este lector |
| **No copiar resultados** | Incluir un extracto del resultado por paso | Ahí viajan claves y datos personales; la entrada recortada y el estado alcanzan para reconstruir qué pasó |
| Guardar con el **nombre del histórico** | Nombrar por id de sesión | El id no dice nada; el nombre del histórico ya lleva fecha y tema, y los dos archivos quedan emparejados a la vista |
| Emparejar por `tool_use_id` | Por orden de aparición | Las respuestas pueden llegar en otro orden cuando hay llamadas en paralelo |
| En `validadores/`, sin nombrar la herramienta | En el adaptador | Lee un formato de transcripción, no habla con la herramienta; `brevedad` sentó el precedente y `amarre` lo vigila |

### 2.7 Dudas por resolver antes de codificar

Ninguna. Todo lo que el plan afirma se leyó en el código o en una transcripción real el 2026-08-20.

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — en la HU: [CA-01](../HU-016-la-traza-de-la-sesion-paso-a-paso.md#ca-01--la-línea-de-tiempo-de-una-sesión)

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `traza.py`: `pasos(ruta)` empareja, recorta la entrada, calcula duración y estado | Validador | 1 h | — | EV-01 |
| T-02 | `como_texto`: las filas | Validador | 0,5 h | T-01 | EV-01 |

### CA-02 — en la HU: [CA-02](../HU-016-la-traza-de-la-sesion-paso-a-paso.md#ca-02--el-cierre-dice-los-totales)

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-03 | `cierre(pasos)` y su texto | Validador | 0,5 h | T-01 | EV-01 |

### CA-03 — en la HU: [CA-03](../HU-016-la-traza-de-la-sesion-paso-a-paso.md#ca-03--con---escribir-queda-junto-al-histórico-indexada)

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-04 | `historico.archivo_de_sesion`; `traza.escribir` con el índice de `trazas/`; subcomando en `validar.py` | Validador | 0,75 h | T-02, T-03 | EV-01 |

### CA-04 — en la HU: [CA-04](../HU-016-la-traza-de-la-sesion-paso-a-paso.md#ca-04--lo-raro-no-revienta)

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-05 | Los casos: tres pasos con error, cierre, escribir e indexar una vez, sin histórico, ilegible, sin respuesta, vacío, inexistente, privacidad, 1 MB | Prueba | 1 h | T-04 | EV-01 |

### RNF — requisitos no funcionales y cierre

| ID | Tarea | Categoría | Est. | Ev. |
|---|---|---|:--:|---|
| T-06 | Especificación §4.9 y §13, mapa del sitio, README del histórico | Documentación | 0,5 h | EV-03 |
| T-07 | Trazar una sesión real de este repositorio y dejarla en `historico-chat/trazas/` | Verificación | 0,25 h | EV-02 |

**Total estimado:** 4,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-04 → T-05 → T-07. **Paralelizable:** T-06 con T-05.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). Descubrir uno nuevo detiene la ejecución y amplía el plan con el OK del usuario.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| [CA-01](../HU-016-la-traza-de-la-sesion-paso-a-paso.md#ca-01--la-línea-de-tiempo-de-una-sesión) | Caso con tres pasos y un error | EV-01 | ☐ |
| [CA-02](../HU-016-la-traza-de-la-sesion-paso-a-paso.md#ca-02--el-cierre-dice-los-totales) | Caso que lee los totales | EV-01 | ☐ |
| [CA-03](../HU-016-la-traza-de-la-sesion-paso-a-paso.md#ca-03--con---escribir-queda-junto-al-histórico-indexada) | Tres casos: escribe, no duplica, sin histórico | EV-01 | ☐ |
| [CA-04](../HU-016-la-traza-de-la-sesion-paso-a-paso.md#ca-04--lo-raro-no-revienta) | Cuatro casos raros | EV-01 | ☐ |
| RNF-01 · 1 MB en menos de 2 s | Caso medido sobre una transcripción real | EV-02 | ☐ |
| RNF-02 · privacidad | Caso que busca el contenido del resultado en la salida | EV-01 | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Suite | `validadores/tests/test_la_sesion_tiene_traza.py` |
| EV-02 | Salida del lector sobre una sesión real | `resultado_pruebas.md` §2 y `historico-chat/trazas/` |
| EV-03 | Diff de los documentos | `funcionalidad_implementada.md` §3 |

## 6. Datos y ambiente de prueba

Transcripciones sintéticas escritas por la prueba en carpetas temporales, con marcas de tiempo fijas ([`08·T3`](../../../../../base/08-pruebas.md#t3--aisladas-deterministas-repetibles)). La sesión real de T-07 es la de este repositorio, cuyo contenido ya está en el histórico.

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Se revierte el commit. No toca proyectos ni deja nada instalado.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12

Aditiva: un subcomando nuevo. Por sí sola sería MENOR; va en la entrada **28.0.0** junto con el portero.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`00·N6`](../../../../../base/00-nucleo-blindado.md#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada) (por eso no se copian resultados), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md#t1--todo-cambio-con-lógica-lleva-prueba), [`08·T3`](../../../../../base/08-pruebas.md#t3--aisladas-deterministas-repetibles), `13·DOC14` (el índice de `trazas/` escribe el texto del enlace con la ruta desde la raíz), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md), [`00·N2`](../../../../../base/00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada).
- Del repositorio: la frontera de `adaptadores/contrato.md`.

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que la transcripción real tenga bloques en un formato que la sintética no reproduce | Una fila menos | T-07 traza una sesión real y se compara el número de pasos con un conteo directo | Abierto |

## 11. Definition of Done

- [ ] Los cuatro CA verificados con evidencia (§5)
- [ ] RNF-01 y RNF-02 validados
- [ ] `validadores/tests/` y `validadores/pruebas.py` en verde; `validar.py amarre` sin falla nueva
- [ ] Especificación §13, mapa del sitio y README del histórico al día
- [ ] Señales registradas
- [ ] Una sesión real trazada en `historico-chat/trazas/`
- [ ] Listo para el commit único, que el usuario autoriza aparte

## 12. Seguimiento diario

N/A: el trabajo lo lleva una sola persona y el avance va en el `estado-fase.md` §1.2.

## 13. Cierre

**No se escribe acá.** Vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
