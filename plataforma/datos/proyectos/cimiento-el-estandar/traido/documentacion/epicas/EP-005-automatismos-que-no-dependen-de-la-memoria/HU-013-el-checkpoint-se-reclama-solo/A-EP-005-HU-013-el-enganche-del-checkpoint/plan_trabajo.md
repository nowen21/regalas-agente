# Plan de Trabajo — Fase A-EP-005-HU-013-el-enganche-del-checkpoint (módulo Automatismos — enganches)

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden y sobre qué archivos, y cómo se comprueba cada criterio antes de darlo por cumplido. Se aprueba antes de tocar nada. El requisito vive en la HU; las pruebas, en el [plan_pruebas.md](plan_pruebas.md); lo que dieron, en el [resultado_pruebas.md](resultado_pruebas.md); lo que quedó, en el [funcionalidad_implementada.md](funcionalidad_implementada.md).

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-005-HU-013-el-enganche-del-checkpoint` |
| **Épica** | [EP-005 Automatismos que no dependen de la memoria](../../epica.md) |
| **HU** | [HU-013 El checkpoint de la fase se reclama solo](../HU-013-el-checkpoint-se-reclama-solo.md) — una sola ([`02·F12.1`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) |
| **Módulo** | Automatismos — enganches |
| **Especificación del módulo** | [documentacion/automatismos/spec.md](../../../../automatismos/spec.md) |
| **Fecha apertura** | 2026-08-20 |
| **Rama** | `main` — el repositorio del estándar trabaja sobre su rama principal, con el commit autorizado aparte |

**ORIGEN:** ✨ **Funcionalidad nueva.** Sale del [pendientes/hecho/el-checkpoint-se-reclama-solo.md](../../../../../pendientes/hecho/el-checkpoint-se-reclama-solo.md): el checkpoint de la fase lo escribe el agente cuando se acuerda, y nada lo reclama cuando una puerta pasa sin él.

**CA de la HU que cubre esta fase:**

| CA de HU-013 que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-013-el-checkpoint-se-reclama-solo.md#ca-01--una-puerta-pasa-sin-checkpoint-y-se-avisa) · una puerta pasa sin checkpoint y se avisa | ☐ |
| [CA-02](../HU-013-el-checkpoint-se-reclama-solo.md#ca-02--el-checkpoint-existe-pero-quedó-atrás) · el checkpoint existe pero quedó atrás | ☐ |
| [CA-03](../HU-013-el-checkpoint-se-reclama-solo.md#ca-03--lo-que-no-es-puerta-calla-y-el-enganche-no-toca-el-checkpoint) · lo que no es puerta calla | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que al escribir un documento que marca una puerta de una fase (`plan_trabajo.md`, `resultado_pruebas.md`, `funcionalidad_implementada.md`) un programa avise si el `estado-fase.md` de esa fase falta o quedó atrás, nombrando la fase y el documento. El programa no escribe el checkpoint.

**Fuera de alcance:**

- Escribir o corregir el `estado-fase.md`: es criterio.
- Juzgar si el estado escrito es cierto: lo hace `validar.py fases` comparando veredictos.
- Avisar por `plan_pruebas.md` o `README.md`: no marcan puerta.

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

Leído el 2026-08-20:

- [validadores/fases.py](../../../../../validadores/fases.py) línea 38: `_FASE`, la expresión que reconoce el nombre de una carpeta de fase (`02·F12.6`). Se reutiliza; no se copia.
- [adaptadores/claude-code/hook_md.py](../../../../../adaptadores/claude-code/hook_md.py): cómo un enganche `PostToolUse` lee la ruta escrita de la entrada estándar (`tool_input.file_path`, y de respaldo `tool_response.filePath`). Se sigue el mismo patrón.
- [validadores/instalar.py](../../../../../validadores/instalar.py) línea 228: `HOOKS_CLAUDE`, la lista que el instalador enchufa en cada proyecto; [validadores/checklist.py](../../../../../validadores/checklist.py) línea 213 la recorre para reclamar lo que falte.
- [validadores/tests/test_la_frontera_del_adaptador.py](../../../../../validadores/tests/test_la_frontera_del_adaptador.py): afirma que en el adaptador hay **8** enganches. Hoy hay 9 (`hook_presupuesto.py` entró en la 27.0.0 sin tocarlo), y esta fase agrega el décimo: la prueba se corrige para contar lo que hay, no un número fijo.
- [anatomia/que-esta-amarrado-a-la-herramienta.md](../../../../../anatomia/que-esta-amarrado-a-la-herramienta.md): el recuento «21 amarrados de 62» lo comprueba `validar.py amarre`; con dos archivos nuevos pasa a 22 de 64 y la pieza libre nueva se nombra por su nombre.
- [documentacion/automatismos/spec.md](../../../../automatismos/spec.md): §4 lleva las reglas de negocio por automatismo y §13 la trazabilidad.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/checkpoint.py` | Nuevo | Agnóstico: reconoce la fase, compara fechas, arma el texto |
| `adaptadores/claude-code/hook_checkpoint.py` | Nuevo | Lee la ruta escrita y llama al módulo; sale con 0 |
| `validadores/instalar.py` | Modificar | Una fila más en `HOOKS_CLAUDE` (`PostToolUse`, `Write|Edit`) |
| `validadores/tests/test_el_checkpoint_se_reclama_solo.py` | Nuevo | Los casos |
| `validadores/tests/test_la_frontera_del_adaptador.py` | Modificar | Cuenta los enganches contra la lista del instalador, no contra el 8 |
| `anatomia/que-esta-amarrado-a-la-herramienta.md` | Modificar | Recuento y la pieza libre nueva |
| `anatomia/mapa-del-sitio.md` | Modificar | Las dos filas del árbol |
| `documentacion/automatismos/spec.md` | Modificar | §4.5 con las RN y §13 con la trazabilidad |
| `CHANGELOG.md` · `VERSION` | Modificar | Una entrada MENOR para las tres fases de hoy (ver §8) |
| `.claude/settings.json` de los 9 proyectos del registro | Modificar | Lo escribe el instalador, no a mano |

### 2.2 Matriz de dependencias del refactor

No aplica porque no cambia el contrato de ningún código existente: lo nuevo se agrega y lo que ya llamaba a estos módulos sigue llamándolos igual.

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

No aplica porque no hay servicio: son programas de línea de comandos que corren en la máquina de quien trabaja.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

No aplica porque no hay interfaz: el resultado se ve como texto en la sesión.

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Comparar **fechas de escritura**, no contenido | Leer el `estado-fase.md` y buscar la estación | Dos fechas del sistema de archivos no cuestan nada; leer y juzgar el contenido es criterio y es lo que la HU saca de alcance |
| Solo tres documentos disparan | Cualquier escritura dentro de la fase | Escribir el plan de pruebas o el README no pasa ninguna puerta; avisar ahí es ruido, y el ruido se deja de leer |
| El aviso se repite mientras el checkpoint siga atrás | Una marca «ya avisé», como hace el resumen | Acá no hay dónde dejar la marca sin escribir en un archivo del agente, y escribir el checkpoint es justo lo que el enganche no hace. Dispara pocas veces por fase |
| Reutilizar `fases._FASE` | Otra expresión igual en el módulo nuevo | Dos copias del mismo patrón se desincronizan |

### 2.7 Dudas por resolver antes de codificar

Ninguna. Todo lo que el plan afirma se leyó en el código el 2026-08-20.

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — en la HU: [CA-01](../HU-013-el-checkpoint-se-reclama-solo.md#ca-01--una-puerta-pasa-sin-checkpoint-y-se-avisa)

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `checkpoint.py`: `fase_de(ruta)`, `rezago(ruta)`, `como_texto(...)` | Validador | 1 h | — | EV-01 |
| T-02 | `hook_checkpoint.py`: leer la entrada, llamar, imprimir, salir con 0 | Adaptador | 0,5 h | T-01 | EV-01 |

### CA-02 — en la HU: [CA-02](../HU-013-el-checkpoint-se-reclama-solo.md#ca-02--el-checkpoint-existe-pero-quedó-atrás)

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-03 | Fila en `HOOKS_CLAUDE` y corrección de la prueba de la frontera | Instalador | 0,5 h | T-02 | EV-02 |

### CA-03 — en la HU: [CA-03](../HU-013-el-checkpoint-se-reclama-solo.md#ca-03--lo-que-no-es-puerta-calla-y-el-enganche-no-toca-el-checkpoint)

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-04 | Los casos: falta, atrasado, al día, los cuatro silencios, huella intacta, entrada rota | Prueba | 1 h | T-02 | EV-01 |

### RNF — requisitos no funcionales y cierre

| ID | Tarea | Categoría | Est. | Ev. |
|---|---|---|:--:|---|
| T-05 | Especificación §4.5 y §13, mapa del sitio, mapa del amarre | Documentación | 0,5 h | EV-03 |
| T-06 | Instalar en los 9 proyectos del registro (`instalar.py --todos --aplicar`) y verificar uno | Instalación | 0,25 h | EV-02 |

**Total estimado:** 3,75 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-04 → T-03 → T-06. **Paralelizable:** T-05 con T-04.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). Descubrir uno nuevo detiene la ejecución y amplía el plan con el OK del usuario.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| [CA-01](../HU-013-el-checkpoint-se-reclama-solo.md#ca-01--una-puerta-pasa-sin-checkpoint-y-se-avisa) | Caso automatizado | EV-01 | ☐ |
| [CA-02](../HU-013-el-checkpoint-se-reclama-solo.md#ca-02--el-checkpoint-existe-pero-quedó-atrás) | Dos casos: atrasado y al día | EV-01 | ☐ |
| [CA-03](../HU-013-el-checkpoint-se-reclama-solo.md#ca-03--lo-que-no-es-puerta-calla-y-el-enganche-no-toca-el-checkpoint) | Cuatro silencios y la huella | EV-01 | ☐ |
| RNF-01 · no lee el contenido | Revisión del código: solo `os.stat` | EV-01 | ☐ |
| RNF-02 · el aviso dice qué y dónde | Caso que busca la ruta relativa en el texto | EV-01 | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Suite | `validadores/tests/test_el_checkpoint_se_reclama_solo.py` |
| EV-02 | Salida del instalador | `resultado_pruebas.md` §2 |
| EV-03 | Diff de los documentos | `funcionalidad_implementada.md` §3 |

## 6. Datos y ambiente de prueba

Fases de mentira en carpetas temporales, con nombres que siguen `02·F12.6`. Nada toca `documentacion/epicas/` real. Las fechas se fuerzan con `os.utime` para que el caso no dependa del reloj ([`08·T3`](../../../../../base/08-pruebas.md#t3--aisladas-deterministas-repetibles)).

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Se revierte el commit. El instalador, al volver a correr sin la fila, quita el enganche de los proyectos: no deja residuo.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12

Aditiva. Un proyecto al día no hace nada hasta que corre el instalador; `checklist.py` se lo reclama en el primer mensaje. **Versión:** las tres fases del 2026-08-20 suben una sola vez a **27.1.0 (MENOR)**: enganches nuevos que no obligan a nada, con aviso automático de reinstalación.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md#t1--todo-cambio-con-lógica-lleva-prueba), [`08·T3`](../../../../../base/08-pruebas.md#t3--aisladas-deterministas-repetibles), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md), [`00·N2`](../../../../../base/00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada).
- Del repositorio: la frontera de `adaptadores/contrato.md` (lo agnóstico en `validadores/`, lo de la herramienta en el adaptador).

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Dos escrituras en el mismo segundo den la misma fecha | El aviso no sale una vez | En la prueba se fuerzan fechas distintas; en uso real median minutos | Abierto por diseño |
| B-02 | La prueba de la frontera cuenta 8 y ya hay 9 | La suite estaba en rojo antes de esta fase | T-03 la hace contar contra la lista del instalador | Abierto |

## 11. Definition of Done

- [ ] Los tres CA verificados con evidencia (§5)
- [ ] RNF-01 y RNF-02 validados
- [ ] `validadores/tests/` y `validadores/pruebas.py` en verde
- [ ] Trazabilidad en la especificación §13 sin faltantes
- [ ] Mapa del sitio y mapa del amarre al día
- [ ] Señales registradas
- [ ] Instalado en los 9 proyectos
- [ ] Listo para el commit único, que el usuario autoriza aparte

## 12. Seguimiento diario

N/A: el trabajo lo lleva una sola persona y el avance va en el `estado-fase.md` §1.2.

## 13. Cierre

**No se escribe acá.** Vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
