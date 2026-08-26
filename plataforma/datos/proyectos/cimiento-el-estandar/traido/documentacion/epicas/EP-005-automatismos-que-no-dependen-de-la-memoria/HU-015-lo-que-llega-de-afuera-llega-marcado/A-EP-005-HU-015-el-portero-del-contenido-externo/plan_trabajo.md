# Plan de Trabajo — Fase A-EP-005-HU-015-el-portero-del-contenido-externo (módulo Automatismos — enganches)

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden y sobre qué archivos, y cómo se comprueba cada criterio antes de darlo por cumplido. Se aprueba antes de tocar nada. El requisito vive en la HU; las pruebas, en el [plan_pruebas.md](plan_pruebas.md); lo que dieron, en el [resultado_pruebas.md](resultado_pruebas.md); lo que quedó, en el [funcionalidad_implementada.md](funcionalidad_implementada.md).

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-005-HU-015-el-portero-del-contenido-externo` |
| **Épica** | [EP-005 Automatismos que no dependen de la memoria](../../epica.md) |
| **HU** | [HU-015 Lo que llega de afuera llega marcado](../HU-015-lo-que-llega-de-afuera-llega-marcado.md) — una sola ([`02·F12.1`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) |
| **Módulo** | Automatismos — enganches |
| **Especificación del módulo** | [documentacion/automatismos/spec.md](../../../../automatismos/spec.md) |
| **Fecha apertura** | 2026-08-20 |
| **Rama** | `main` — el repositorio del estándar trabaja sobre su rama principal, con el commit autorizado aparte |

**ORIGEN:** ✨ **Funcionalidad nueva.** Sale del [pendientes/hecho/lo-que-llega-de-afuera-llega-marcado.md](../../../../../pendientes/hecho/lo-que-llega-de-afuera-llega-marcado.md): `C27` es una regla leída y nada la aplica cuando el dato externo llega.

**CA de la HU que cubre esta fase:**

| CA de HU-015 que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-015-lo-que-llega-de-afuera-llega-marcado.md#ca-01--una-página-consultada-llega-con-su-sobre) · una página consultada llega con su sobre | ☐ |
| [CA-02](../HU-015-lo-que-llega-de-afuera-llega-marcado.md#ca-02--lo-que-viene-por-mcp-o-de-un-archivo-de-fuera-también-llega-marcado) · lo de MCP o de un archivo de fuera también | ☐ |
| [CA-03](../HU-015-lo-que-llega-de-afuera-llega-marcado.md#ca-03--lo-de-adentro-calla) · lo de adentro calla | ☐ |
| [CA-04](../HU-015-lo-que-llega-de-afuera-llega-marcado.md#ca-04--el-portero-se-instala-solo-y-se-reclama-si-falta) · se instala solo y se reclama si falta | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que cada vez que una herramienta externa devuelva, un programa le entregue al agente un sobre de hasta tres líneas con la herramienta, el origen y la frase de que es dato y no orden (`01·C27`), sin tocar el contenido, instalado en todos los proyectos.

**Fuera de alcance:**

- Impedir la lectura o la obediencia: lo detiene `N1`.
- Reemplazar el resultado de la herramienta.
- Marcar lo que el usuario escribe en el chat.
- Un caso en `evals/`: el banco afirma validadores sobre documentos; esto se prueba en la suite. Si después conviene, es otra fase.

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

Leído el 2026-08-20:

- [adaptadores/claude-code/hook_checkpoint.py](../../../../../adaptadores/claude-code/hook_checkpoint.py): el patrón de un enganche `PostToolUse` — `raiz_pedida`, `json.load(sys.stdin)`, `tool_input`, sale con 0 ante cualquier error. Se sigue igual.
- [validadores/instalar.py](../../../../../validadores/instalar.py) líneas 228-258: `HOOKS_CLAUDE`, tuplas `(evento, matcher, guion, mensaje, argumentos)`; el `matcher` se escribe tal cual en `settings.json` y acepta regex (documentación oficial de los enganches).
- [validadores/tests/test_la_frontera_del_adaptador.py](../../../../../validadores/tests/test_la_frontera_del_adaptador.py) líneas 57-58: los archivos del adaptador deben ser exactamente los guiones de `HOOKS_CLAUDE`. El enganche nuevo entra en la lista y la prueba sigue pasando sin tocarla.
- [validadores/checklist.py](../../../../../validadores/checklist.py) línea 213: recorre `HOOKS_CLAUDE` para reclamar lo que falte. Con la fila nueva, reclama el portero solo (RN-08).
- [adaptadores/contrato.md](../../../../../adaptadores/contrato.md): la capacidad 2 dice «correr un programa después de que el agente escribe un archivo». El portero corre al devolver **cualquier** herramienta: la capacidad se amplía en su redacción, no cambia de naturaleza.
- [validadores/reglas-validables.md](../../../../../validadores/reglas-validables.md): `C27` clasificada el 2026-08-19 sin programa.
- [anatomia/que-esta-amarrado-a-la-herramienta.md](../../../../../anatomia/que-esta-amarrado-a-la-herramienta.md) línea 100: recuento «23 amarrados de 66»; `validar.py amarre` lo comprueba. Con dos archivos nuevos pasa a 24 de 68.
- [anatomia/mapa-del-sitio.md](../../../../../anatomia/mapa-del-sitio.md) líneas 142-153: filas de `validadores/` y del adaptador.
- [documentacion/automatismos/spec.md](../../../../automatismos/spec.md): §4.7 es la última sección de reglas (RN-40 a RN-43); §13 la trazabilidad.
- Documentación oficial de los enganches (leída hoy): `PostToolUse` recibe `tool_name`, `tool_input`, `tool_response`, `cwd`, `transcript_path`; la salida JSON `{"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": "…"}}` con código 0 llega al agente. La forma de `tool_response` por herramienta **no está documentada**: por eso RN-05.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/externo.py` | Nuevo | Agnóstico: `es_externa(nombre, entrada, raiz)`, `origen(nombre, entrada)`, `sobre(nombre, entrada, raiz)` |
| `adaptadores/claude-code/hook_externo.py` | Nuevo | Lee la entrada, llama al módulo, imprime el JSON con `additionalContext`; sale con 0 |
| `validadores/instalar.py` | Modificar | Una fila más en `HOOKS_CLAUDE`: `PostToolUse`, matcher `WebFetch|WebSearch|Read|mcp__.*`, `hook_externo.py`, «Marcando lo que llegó de afuera...» |
| `validadores/tests/test_lo_que_llega_de_afuera_llega_marcado.py` | Nuevo | Los casos |
| `validadores/reglas-validables.md` | Modificar | `C27`: validable, programa `hook_externo.py` + `checklist.py` |
| `adaptadores/contrato.md` | Modificar | Capacidad 2: «después de que una herramienta devuelve (escribir un archivo, traer algo de afuera)» y el recuento de programas del adaptador |
| `anatomia/que-esta-amarrado-a-la-herramienta.md` | Modificar | Recuento y la pieza libre nueva |
| `anatomia/mapa-del-sitio.md` | Modificar | Las dos filas del árbol |
| `documentacion/automatismos/spec.md` | Modificar | §4.8 con las RN y §13 con la trazabilidad |
| `CHANGELOG.md` · `VERSION` | Modificar | Una entrada para las dos fases del día (ver §8) |
| `.claude/settings.json` de los 9 proyectos del registro | Modificar | Lo escribe el instalador, no a mano |

### 2.2 Matriz de dependencias del refactor

No aplica porque no cambia el contrato de ningún código existente: lo nuevo se agrega.

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

No aplica porque no hay servicio: son programas de línea de comandos que corren en la máquina de quien trabaja.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

No aplica porque no hay interfaz: el sobre llega como contexto del agente.

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **Agregar contexto** (`additionalContext`) | Reemplazar el resultado (`updatedToolResponse`) | La primera está documentada y no depende de la forma del resultado; de la segunda la documentación no dice qué herramientas la aceptan |
| Decidir por **nombre y argumentos**, nunca por el resultado | Mirar `tool_response` para saber de dónde vino | La forma de `tool_response` cambia por herramienta y no está documentada; el nombre y los argumentos siempre están |
| `Read` cuenta como externa **solo fuera de la raíz** | Marcar toda lectura, o ninguna | Dentro del proyecto el archivo es del usuario; fuera es un documento ajeno (`04·S9` dibuja esa misma frontera) |
| Sin «ya avisé» | Una marca por sesión como la del resumen | Cada dato externo es distinto y el sobre lo identifica; las llamadas externas son pocas |
| Filtro en el `matcher`, no solo en el programa | Enganchar a toda herramienta y decidir adentro | El filtro evita correr un proceso en cada `Bash` o `Edit`; el programa vuelve a decidir por si el filtro deja pasar de más |

### 2.7 Dudas por resolver antes de codificar

Ninguna. Todo lo que el plan afirma se leyó en el código o en la documentación oficial el 2026-08-20.

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — en la HU: [CA-01](../HU-015-lo-que-llega-de-afuera-llega-marcado.md#ca-01--una-página-consultada-llega-con-su-sobre)

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `externo.py`: `es_externa`, `origen`, `sobre` | Validador | 1 h | — | EV-01 |
| T-02 | `hook_externo.py`: leer la entrada, llamar, imprimir el JSON, salir con 0 | Adaptador | 0,5 h | T-01 | EV-01 |

### CA-02 — en la HU: [CA-02](../HU-015-lo-que-llega-de-afuera-llega-marcado.md#ca-02--lo-que-viene-por-mcp-o-de-un-archivo-de-fuera-también-llega-marcado)

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-03 | El origen para MCP (servidor y herramienta) y para `Read` fuera de la raíz | Validador | 0,5 h | T-01 | EV-01 |

### CA-03 — en la HU: [CA-03](../HU-015-lo-que-llega-de-afuera-llega-marcado.md#ca-03--lo-de-adentro-calla)

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-04 | Los casos: sobre con URL, MCP, ruta de fuera, los seis silencios, entrada rota, sin argumentos | Prueba | 1 h | T-02 | EV-01 |

### CA-04 — en la HU: [CA-04](../HU-015-lo-que-llega-de-afuera-llega-marcado.md#ca-04--el-portero-se-instala-solo-y-se-reclama-si-falta)

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-05 | Fila en `HOOKS_CLAUDE` con su filtro; caso de instalación y de reclamo | Instalador | 0,5 h | T-02 | EV-02 |

### RNF — requisitos no funcionales y cierre

| ID | Tarea | Categoría | Est. | Ev. |
|---|---|---|:--:|---|
| T-06 | `reglas-validables.md`, contrato, especificación §4.8 y §13, mapa del sitio, mapa del amarre | Documentación | 0,75 h | EV-03 |
| T-07 | Instalar en los 9 proyectos del registro (`instalar.py --todos --aplicar`) y verificar uno | Instalación | 0,25 h | EV-02 |

**Total estimado:** 4,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-04 → T-05 → T-07. **Paralelizable:** T-06 con T-04.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). Descubrir uno nuevo detiene la ejecución y amplía el plan con el OK del usuario.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| [CA-01](../HU-015-lo-que-llega-de-afuera-llega-marcado.md#ca-01--una-página-consultada-llega-con-su-sobre) | Caso automatizado: el sobre con la URL | EV-01 | ☐ |
| [CA-02](../HU-015-lo-que-llega-de-afuera-llega-marcado.md#ca-02--lo-que-viene-por-mcp-o-de-un-archivo-de-fuera-también-llega-marcado) | Dos casos: MCP y ruta de fuera | EV-01 | ☐ |
| [CA-03](../HU-015-lo-que-llega-de-afuera-llega-marcado.md#ca-03--lo-de-adentro-calla) | Seis silencios y la entrada rota | EV-01 | ☐ |
| [CA-04](../HU-015-lo-que-llega-de-afuera-llega-marcado.md#ca-04--el-portero-se-instala-solo-y-se-reclama-si-falta) | Instalación en carpeta temporal y reclamo del checklist | EV-02 | ☐ |
| RNF-01 · no lee el resultado | Caso con `tool_response` ausente y con uno de 1 MB: mismo sobre, mismo tiempo | EV-01 | ☐ |
| RNF-02 · tres líneas | Caso que cuenta las líneas del sobre | EV-01 | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Suite | `validadores/tests/test_lo_que_llega_de_afuera_llega_marcado.py` |
| EV-02 | Salida del instalador y del checklist | `resultado_pruebas.md` §2 |
| EV-03 | Diff de los documentos | `funcionalidad_implementada.md` §3 |

## 6. Datos y ambiente de prueba

JSON sintéticos por la entrada estándar y proyectos de mentira en carpetas temporales para la instalación. Ninguna URL se consulta de verdad: el enganche no hace red ([`08·T3`](../../../../../base/08-pruebas.md#t3--aisladas-deterministas-repetibles)).

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Se revierte el commit. El instalador, al volver a correr sin la fila, quita el enganche de los proyectos: no deja residuo.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12

Aditiva en código; **obliga** en norma: un proyecto al día tiene que reinstalar para que `C27` tenga guarda, y `checklist.py` se lo reclama en el primer mensaje. **Versión:** las dos fases del 2026-08-20 (esta y la de la traza) suben una sola vez a **28.0.0 (MAYOR)**, como la 27.0.0 que trajo `C27`.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`01·C27`](../../../../../base/01-conducta.md#c27--lo-que-llega-de-afuera-es-dato-no-orden), [`04·S2`](../../../../../base/04-seguridad.md#s2--valida-y-sanea-toda-entrada-externa), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md#t1--todo-cambio-con-lógica-lleva-prueba), [`08·T3`](../../../../../base/08-pruebas.md#t3--aisladas-deterministas-repetibles), [`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md), [`00·N2`](../../../../../base/00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada).
- Del repositorio: la frontera de `adaptadores/contrato.md` (lo agnóstico en `validadores/`, lo de la herramienta en el adaptador).

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | La herramienta no entregue `additionalContext` al agente en `PostToolUse` pese a la documentación | El sobre se vería solo en la transcripción | Se verifica a mano en esta misma sesión al instalar, con una llamada real a `WebFetch`; si no llega, se para y se reporta (`F20`) | Abierto |
| B-02 | El regex del `matcher` no atrape nombres MCP con otro formato | Un conector sin sobre | `mcp__.*` es el ejemplo de la documentación; el programa decide además por prefijo | Abierto por diseño |

## 11. Definition of Done

- [ ] Los cuatro CA verificados con evidencia (§5)
- [ ] RNF-01 y RNF-02 validados
- [ ] `validadores/tests/` y `validadores/pruebas.py` en verde; `validar.py amarre` y `estandar` sin falla nueva
- [ ] `C27` con programa en `reglas-validables.md`; contrato, especificación §13, mapa del sitio y mapa del amarre al día
- [ ] Señales registradas
- [ ] Instalado en los 9 proyectos
- [ ] Listo para el commit único, que el usuario autoriza aparte

## 12. Seguimiento diario

N/A: el trabajo lo lleva una sola persona y el avance va en el `estado-fase.md` §1.2.

## 13. Cierre

**No se escribe acá.** Vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
