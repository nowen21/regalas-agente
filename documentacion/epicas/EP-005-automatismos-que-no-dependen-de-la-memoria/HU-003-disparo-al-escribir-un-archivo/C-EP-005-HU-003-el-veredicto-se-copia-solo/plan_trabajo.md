# Plan de Trabajo — Fase C-EP-005-HU-003-el-veredicto-se-copia-solo (módulo Automatismos — enganches)

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden y sobre qué archivos, y cómo se comprueba cada criterio antes de darlo por cumplido. Se aprueba antes de tocar nada. El requisito vive en la HU; las pruebas, en el [plan_pruebas.md](plan_pruebas.md); lo que dieron, en el [resultado_pruebas.md](resultado_pruebas.md); lo que quedó, en el [funcionalidad_implementada.md](funcionalidad_implementada.md).

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `C-EP-005-HU-003-el-veredicto-se-copia-solo` |
| **Épica** | [EP-005 Automatismos que no dependen de la memoria](../../epica.md) |
| **HU** | [HU-003 Disparar las comprobaciones al escribir un archivo](../HU-003-disparo-al-escribir-un-archivo.md) — una sola ([`02·F12.1`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) |
| **Módulo** | Automatismos — enganches |
| **Especificación del módulo** | [documentacion/automatismos/spec.md](../../../../automatismos/spec.md) |
| **Fecha apertura** | 2026-08-20 |
| **Rama** | `main` — el repositorio del estándar trabaja sobre su rama principal, con el commit autorizado aparte |

**ORIGEN:** ✨ **Funcionalidad nueva.** Sale del [pendientes/hecho/el-veredicto-se-copia-solo.md](../../../../../pendientes/hecho/el-veredicto-se-copia-solo.md): el veredicto del resultado se copia a mano en cuatro sitios y el programa que ya lo lee (`fases.py`) solo comprueba después que no se contradigan.

**CA de la HU que cubre esta fase:**

| CA de HU-003 que cierra esta fase | Estado |
|---|---|
| [CA-04](../HU-003-disparo-al-escribir-un-archivo.md#ca-04--lo-que-se-deriva-del-veredicto-lo-copia-el-programa) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que al escribir el `resultado_pruebas.md` de una fase un programa lea su §6 y deje el mismo veredicto en la fila del §8 de la historia y en los README de la fase y de la historia; y que `cerrar.py`, que ya arrastra las citas, deje además la fila del backlog en la forma «hecho». El `estado-fase.md` no: es el checkpoint y lo escribe el agente.

**Fuera de alcance:**

- Decidir o interpretar el veredicto: se copia lo que el §6 dice, con las mismas expresiones que `fases.py` ya usa para leerlo.
- El `estado-fase.md`: criterio del agente (HU-013).
- El estado de la historia («Hecha») en su §1: depende de todas sus fases, y eso es leer más de lo que esta fase sabe; queda para después.

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

Leído el 2026-08-20:

- [validadores/fases.py](../../../../../validadores/fases.py) líneas 46-52: `_CONCEPTO_FILA`, `_CONTEO`, y `_concepto(texto)` que devuelve `cumple` / `no cumple` / `""`. Se reutilizan.
- El §8 de las historias tiene dos formas: tres columnas (`Fase | Qué CA cubre | Estado`) y seis (`… | Plan de trabajo | Plan de pruebas | Resultado | Estado`). En las dos, la primera celda enlaza la carpeta de la fase y la última es el estado.
- Los README de fase escritos hoy llevan una línea `**Estado:** …`; los README de HU, una fila por fase con el estado en la última celda.
- [validadores/cerrar.py](../../../../../validadores/cerrar.py): `cerrar()` mueve y reescribe citas; no toca la forma de la fila del índice. Hoy la fila quedó con `| 64 | **P2** | [título](hecho/…)` y se reescribió a mano a `| ~~64~~ | — | **hecho** → …`.
- [adaptadores/claude-code/hook_checkpoint.py](../../../../../adaptadores/claude-code/hook_checkpoint.py): el patrón de un enganche `PostToolUse` que lee la ruta escrita; se copia la forma.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/veredicto.py` | Nuevo | `leer(resultado)` → (concepto, x, y) · `propagar(resultado, fecha)` → qué archivos tocó |
| `adaptadores/claude-code/hook_veredicto.py` | Nuevo | `PostToolUse` sobre `Write|Edit`: si el archivo es un `resultado_pruebas.md` de una fase con veredicto, propaga e imprime qué tocó |
| `validadores/cerrar.py` | Modificar | `_fila_hecha()`: la fila del índice en forma «hecho» |
| `validadores/instalar.py` | Modificar | Una fila más en `HOOKS_CLAUDE` |
| `validadores/tests/test_el_veredicto_se_copia_solo.py` | Nuevo | Los casos |
| `documentacion/automatismos/spec.md` | Modificar | §4.7 y §13 |
| `anatomia/mapa-del-sitio.md` · `anatomia/que-esta-amarrado-a-la-herramienta.md` | Modificar | Dos piezas más |
| `CHANGELOG.md` · `VERSION` | Modificar | 27.2.0 |
| `.claude/settings.json` de los 9 proyectos | Modificar | Lo escribe el instalador |

### 2.2 Matriz de dependencias del refactor

No aplica porque no cambia el contrato de ningún código existente: lo que ya llamaba a estos programas sigue llamándolos igual.

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

No aplica porque no hay servicio: son programas de línea de comandos que corren en la máquina de quien trabaja.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

No aplica porque no hay interfaz: el resultado se ve como texto en la consola o en la sesión.

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Propagar solo cuando el §6 tiene concepto `cumple` o `no cumple` | Propagar también «todavía no se ejecutó» | Un resultado a medio escribir no es un veredicto; copiarlo pondría «no ejecutado» en la historia cada vez que se guarda el borrador |
| Reutilizar `fases._concepto` y `_CONTEO` | Otra lectura del §6 | Dos lecturas del mismo texto se desincronizan, y `fases.py` es la que decide la puerta |
| La fila «hecho» la escribe `cerrar.py`, no un enganche | Otro enganche sobre `pendientes/README.md` | Cerrar ya es un comando que se pide; el enganche sería un segundo programa para el mismo acto |
| El `estado-fase.md` no se toca | Copiar ahí también | Es el checkpoint y es criterio (HU-013) |

### 2.7 Dudas por resolver antes de codificar

Ninguna. Todo lo que el plan afirma se leyó en el código el 2026-08-20.

## 3. Desglose de tareas por criterio de aceptación

### CA-04 — en la HU: [CA-04](../HU-003-disparo-al-escribir-un-archivo.md#ca-04--lo-que-se-deriva-del-veredicto-lo-copia-el-programa)

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `veredicto.py`: leer el §6, ubicar la historia y los README, reescribir la última celda y la línea de estado | Validador | 1,5 h | — | EV-01 |
| T-02 | `hook_veredicto.py` y su fila en `HOOKS_CLAUDE` | Adaptador | 0,5 h | T-01 | EV-01 |
| T-03 | `cerrar.py`: la fila del índice en forma «hecho» | Validador | 0,5 h | — | EV-01 |
| T-04 | Los casos: tres columnas y seis; cumple y no cumple; sin veredicto calla; el checkpoint intacto; la fila «hecho» | Prueba | 1 h | T-02, T-03 | EV-01 |
| T-05 | Especificación §4.7 y §13, mapas, instalar en los 9 proyectos | Documentación e instalación | 0,5 h | T-02 | EV-02 |

**Total estimado:** 4 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-04 → T-05. **Paralelizable:** T-03.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). Descubrir uno nuevo detiene la ejecución y amplía el plan con el OK del usuario.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| [CA-04](../HU-003-disparo-al-escribir-un-archivo.md#ca-04--lo-que-se-deriva-del-veredicto-lo-copia-el-programa) | Casos sobre una historia de prueba con sus dos formas de §8, y un cierre de pendiente sobre una copia del índice | EV-01 | ☐ |
| Instalado | Salida del instalador y un `settings.json` leído | EV-02 | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Suite | `validadores/tests/test_el_veredicto_se_copia_solo.py` |
| EV-02 | Salida del instalador | `resultado_pruebas.md` §3 |

## 6. Datos y ambiente de prueba

Historias y fases de mentira en carpetas temporales; una copia temporal de `pendientes/README.md` para el cierre.

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Se revierte el commit y se vuelve a correr el instalador, que quita la fila.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12

Aditiva. Los proyectos reciben el enganche al reinstalar, y `checklist.py` se lo reclama. Entra en la **27.2.0 (MENOR)**.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md#t1--todo-cambio-con-lógica-lleva-prueba), [`08·T3`](../../../../../base/08-pruebas.md#t3--aisladas-deterministas-repetibles), [`13·DOC14`](../../../../../base/13-documentacion/reglas/DOC14-enlaza-cada-md-con-ruta-legible-y-destino-relativo.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md), [`00·N2`](../../../../../base/00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada); la frontera de `adaptadores/contrato.md`.

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Una historia con el §8 en una tercera forma | No encuentra la fila | Si no la encuentra, imprime que no la encontró y no toca nada; con caso | Abierto por diseño |
| B-02 | Que el agente escriba el resultado en varias pasadas y el veredicto se propague a medias | La historia dice «Cumple» antes de tiempo | Solo se propaga con concepto escrito, que es lo último que se escribe | Abierto por diseño |

## 11. Definition of Done

- [ ] CA-04 verificado con evidencia
- [ ] `validadores/tests/` y `validadores/pruebas.py` en verde
- [ ] Especificación, mapas al día; instalado en los 9 proyectos
- [ ] Señal registrada
- [ ] Listo para el commit único del día, que el usuario autoriza aparte

## 12. Seguimiento diario

N/A: el trabajo lo lleva una sola persona y el avance va en el `estado-fase.md` §1.2.

## 13. Cierre

**No se escribe acá.** Vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
