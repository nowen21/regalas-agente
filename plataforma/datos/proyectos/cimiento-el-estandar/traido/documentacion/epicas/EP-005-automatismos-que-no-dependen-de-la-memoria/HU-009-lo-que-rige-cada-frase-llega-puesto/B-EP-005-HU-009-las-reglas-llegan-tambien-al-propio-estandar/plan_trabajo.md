# Plan de Trabajo — Fase B-EP-005-HU-009-las-reglas-llegan-tambien-al-propio-estandar (módulo Automatismos — enganches)

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden y sobre qué archivos, y cómo se comprueba cada criterio antes de darlo por cumplido. Se aprueba antes de tocar nada. El requisito vive en la HU; las pruebas, en el [plan_pruebas.md](plan_pruebas.md); lo que dieron, en el [resultado_pruebas.md](resultado_pruebas.md); lo que quedó, en el [funcionalidad_implementada.md](funcionalidad_implementada.md).

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-005-HU-009-las-reglas-llegan-tambien-al-propio-estandar` |
| **Épica** | [EP-005 Automatismos que no dependen de la memoria](../../epica.md) |
| **HU** | [HU-009 Lo que gobierna cada frase llega puesto al abrir la sesión](../HU-009-lo-que-rige-cada-frase-llega-puesto.md) — una sola ([`02·F12.1`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) |
| **Módulo** | Automatismos — enganches |
| **Especificación del módulo** | [documentacion/automatismos/spec.md](../../../../automatismos/spec.md) |
| **Fecha apertura** | 2026-08-20 |
| **Rama** | `main` — el repositorio del estándar trabaja sobre su rama principal, con el commit autorizado aparte |

**ORIGEN:** 🐛 **Defecto** del `CA-01`, que la fase [A](../A-EP-005-HU-009-retrodocumentar-el-reparto-de-las-reglas/) dio por cumplido midiendo solo proyectos herederos. En la carpeta del propio estándar las reglas no llegan, desde la primera versión del enganche. Sale del [pendientes/hecho/las-reglas-llegan-tambien-al-propio-estandar.md](../../../../../pendientes/hecho/las-reglas-llegan-tambien-al-propio-estandar.md).

**CA de la HU que cubre esta fase:**

| CA de HU-009 que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#ca-01--los-capítulos-que-rigen-cada-frase-llegan-con-su-texto) · los capítulos que rigen cada frase llegan con su texto, **también en la carpeta del estándar** | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que al abrir una sesión en la carpeta del estándar el enganche entregue las reglas de `base/` completas, como se las entrega a cualquier proyecto, sin dejar de entregar la memoria y el histórico, y sin correr la revisión de instalación que ahí no tiene qué revisar.

**Fuera de alcance:**

- Cambiar lo que reciben los proyectos herederos: ya lo reciben bien.
- Cambiar el reparto (qué capítulos van completos y cuáles en índice): es la `RN-01` a `RN-03` de la HU y no se toca.
- Hacer que la pantalla muestre que las reglas llegaron: las reglas van por el canal que no se dibuja, a propósito (son decenas de KB).

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

Leído el 2026-08-20:

- [adaptadores/claude-code/hook_sesion.py](../../../../../adaptadores/claude-code/hook_sesion.py) líneas 68-78: `main()` calcula `del_proyecto` y, si la carpeta es `RAIZ`, responde solo con eso y sale. `cargador.contexto()` se llama después, en la rama de los proyectos, con `instalar.cumple_f13(proyecto)`.
- [validadores/instalar.py](../../../../../validadores/instalar.py) línea 175: `cumple_f13()` mira si existe `proyectos/`; línea 185: `es_el_estandar()` ya sabe que la carpeta del estándar no es un proyecto y no la tiene.
- [validadores/cargador.py](../../../../../validadores/cargador.py) línea 128: `contexto(estandar, gate_ok=True)`; con `gate_ok=False` entrega solo la regla `F13`.
- Comprobado corriendo el enganche a mano: para `RAIZ` devuelve 13 KB con memoria e histórico y sin el bloque `[REGLAS BASE DEL ESTÁNDAR]`. Las 30 aperturas de sesión que la herramienta conserva de este repositorio (16 al 20 de agosto) tampoco lo traen.
- [evals/correr.py](../../../../../evals/correr.py): los tipos de caso son `commit`, `codigo-errores`, `codigo-secretos` y `transcripcion`. No hay uno que mire el arranque.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `adaptadores/claude-code/hook_sesion.py` | Modificar | En la rama del estándar, entregar `cargador.contexto(RAIZ, True)` junto con memoria e histórico; el docstring deja de decir que ahí no se cargan reglas |
| `validadores/tests/test_las_reglas_llegan_al_propio_estandar.py` | Nuevo | Los casos |
| `evals/correr.py` · `evals/casos.jsonl` | Modificar | Tipo `arranque`: el enganche de apertura sobre la carpeta del estándar trae el bloque de reglas |
| `documentacion/automatismos/spec.md` | Modificar | §4.1: una RN nueva, y §13 |
| `CHANGELOG.md` · `VERSION` | Modificar | Dentro de la entrada 27.1.0 del día |

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
| Para el estándar, `gate_ok=True` | Crear `proyectos/` en el repositorio del estándar para que el gate pase | El estándar no es un proyecto: es donde viven las reglas. `instalar.es_el_estandar()` ya lo dice; una carpeta vacía para engañar al gate sería mentirle al propio `F13` |
| Seguir sin correr `sesion.revisar()` en el estándar | Revisarlo como a un proyecto | No tiene `CLAUDE.md` instalado ni `.agente/`: la revisión reportaría faltantes que no son faltantes |
| Un caso en `evals/` además de la prueba | Solo la prueba unitaria | El banco existe para afirmar lo que el estándar promete; que las reglas lleguen es la primera promesa, y quince días sin nadie que la midiera lo demuestran |

### 2.7 Dudas por resolver antes de codificar

Ninguna. Todo lo que el plan afirma se leyó en el código el 2026-08-20.

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — en la HU: [CA-01](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#ca-01--los-capítulos-que-rigen-cada-frase-llegan-con-su-texto)

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `hook_sesion.py`: en la rama del estándar, sumar las reglas al contexto | Adaptador | 0,5 h | — | EV-01 |
| T-02 | Casos: el estándar trae el bloque y el núcleo; un heredero sigue igual; el JSON de salida es válido | Prueba | 0,75 h | T-01 | EV-01 |
| T-03 | Tipo `arranque` en `evals/correr.py` y su caso en `casos.jsonl` | Evals | 0,5 h | T-01 | EV-02 |

### RNF — cierre

| ID | Tarea | Categoría | Est. | Ev. |
|---|---|---|:--:|---|
| T-04 | Especificación §4.1 y §13 | Documentación | 0,25 h | EV-03 |
| T-05 | Abrir una sesión nueva en este repositorio y comprobar que el bloque llega | Verificación manual | 0,1 h | EV-04 |

**Total estimado:** 2,1 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-05. **Paralelizable:** T-03 y T-04 con T-02.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). Descubrir uno nuevo detiene la ejecución y amplía el plan con el OK del usuario.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| [CA-01](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#ca-01--los-capítulos-que-rigen-cada-frase-llegan-con-su-texto) en el estándar | Caso automatizado + caso de evals + apertura real | EV-01, EV-02, EV-04 | ☐ |
| Los herederos no cambian | Caso automatizado sobre un proyecto temporal | EV-01 | ☐ |
| RNF-03 de la HU · el arranque no se vuelve lento | Medir el tiempo del enganche antes y después sobre `RAIZ` | EV-01 | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Suite | `validadores/tests/test_las_reglas_llegan_al_propio_estandar.py` |
| EV-02 | Banco de evals | `python evals/correr.py` |
| EV-03 | Diff de la especificación | `funcionalidad_implementada.md` §3 |
| EV-04 | La apertura de la siguiente sesión, leída del archivo que la herramienta conserva | `resultado_pruebas.md` §2 |

## 6. Datos y ambiente de prueba

El propio repositorio para el caso del estándar (solo lectura), y un proyecto temporal con `proyectos/` para el caso del heredero.

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Se revierte el commit: el enganche vuelve a entregar memoria e histórico sin reglas, que es el estado de hoy.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12

No aplica a los proyectos: el cambio corre solo cuando la carpeta es la del estándar. Entra en la **27.1.0 (MENOR)** del día porque va en el mismo movimiento; por sí sola sería PARCHE.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md#t1--todo-cambio-con-lógica-lleva-prueba), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md), [`00·N2`](../../../../../base/00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada); y el §0 del `CLAUDE.md` de este repositorio, que es lo que esta fase hace cumplir.

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que cargar 73 KB más al abrir el estándar adelante la compactación | Se pierde lo inyectado al arrancar | Es lo que ya reciben los herederos desde la 5.0.0, con el reparto medido en la fase A; no se carga más que eso | Abierto por diseño |

## 11. Definition of Done

- [ ] El CA-01 verificado en la carpeta del estándar, con evidencia (§5)
- [ ] Los herederos sin cambio, con caso
- [ ] `validadores/tests/`, `validadores/pruebas.py` y `evals/correr.py` en verde
- [ ] Trazabilidad en la especificación §13 sin faltantes
- [ ] Señales registradas
- [ ] Listo para el commit único, que el usuario autoriza aparte

## 12. Seguimiento diario

N/A: el trabajo lo lleva una sola persona y el avance va en el `estado-fase.md` §1.2.

## 13. Cierre

**No se escribe acá.** Vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
