# Plan de Trabajo — Fase A-EP-005-HU-014-el-aviso-por-tramo (módulo Automatismos — enganches)

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden y sobre qué archivos, y cómo se comprueba cada criterio antes de darlo por cumplido. Se aprueba antes de tocar nada. El requisito vive en la HU; las pruebas, en el [plan_pruebas.md](plan_pruebas.md); lo que dieron, en el [resultado_pruebas.md](resultado_pruebas.md); lo que quedó, en el [funcionalidad_implementada.md](funcionalidad_implementada.md).

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-005-HU-014-el-aviso-por-tramo` |
| **Épica** | [EP-005 Automatismos que no dependen de la memoria](../../epica.md) |
| **HU** | [HU-014 El consumo de la sesión se ve mientras se puede actuar](../HU-014-el-consumo-se-ve-a-tiempo.md) — una sola ([`02·F12.1`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) |
| **Módulo** | Automatismos — enganches |
| **Especificación del módulo** | [documentacion/automatismos/spec.md](../../../../automatismos/spec.md) |
| **Fecha apertura** | 2026-08-20 |
| **Rama** | `main` — el repositorio del estándar trabaja sobre su rama principal, con el commit autorizado aparte |

**ORIGEN:** 🔀 **Híbrido.** Le da historia a lo que la 27.0.0 construyó sin cadena (el reporte al cierre, `CA-01`) y agrega el aviso por tramo durante la sesión (`CA-02`, `CA-03`). Sale del [pendientes/hecho/el-consumo-se-ve-a-tiempo.md](../../../../../pendientes/hecho/el-consumo-se-ve-a-tiempo.md).

**CA de la HU que cubre esta fase:**

| CA de HU-014 que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-014-el-consumo-se-ve-a-tiempo.md#ca-01--al-terminar-se-reporta-el-consumo-de-la-sesión) · al terminar se reporta el consumo | ☐ |
| [CA-02](../HU-014-el-consumo-se-ve-a-tiempo.md#ca-02--al-cruzar-un-tramo-se-avisa-una-vez) · al cruzar un tramo se avisa una vez | ☐ |
| [CA-03](../HU-014-el-consumo-se-ve-a-tiempo.md#ca-03--sin-transcripción-calla-y-nunca-detiene) · sin transcripción calla, y nunca detiene | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que el consumo de la sesión se avise **mientras la sesión sigue**, una vez por cada millón de fichas cruzado, sin estado compartido y sin cambiar el reporte de cierre que ya existe.

**Fuera de alcance:**

- Cortar la sesión por consumo: lo hace la herramienta.
- Convertir fichas a dinero.
- Cambiar el comando del enganche de cierre ya instalado en los proyectos: el modo de cierre sigue siendo el que corre sin argumentos.

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

Leído el 2026-08-20:

- [validadores/presupuesto.py](../../../../../validadores/presupuesto.py): `resumen(consumos)`, `excedido(totales, umbral)`, `como_texto(totales, umbral)`. Suma por turno; el total excluye la caché.
- [adaptadores/claude-code/hook_presupuesto.py](../../../../../adaptadores/claude-code/hook_presupuesto.py): `consumos_de_transcripcion(ruta)` lee las líneas JSON con `message.usage`; `main()` acepta `--raiz` y `--umbral`, lee `transcript_path` de la entrada y siempre devuelve 0. No tiene `--modo`.
- [validadores/instalar.py](../../../../../validadores/instalar.py) línea 251: la fila `("Stop", None, "hook_presupuesto.py", ...)` sin argumentos. Se deja igual y se agrega otra para `UserPromptSubmit` con `--modo aviso`.
- [validadores/pruebas.py](../../../../../validadores/pruebas.py) línea 3752: `TestPresupuesto`, tres casos que fijan la suma, el umbral y la lectura de la transcripción. Siguen valiendo.
- La medición de las ocho sesiones está en la HU §3: de 144 mil a 12,7 millones de fichas sin caché.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/presupuesto.py` | Modificar | `TRAMO = 1_000_000`, `tramo(total, umbral)`, `cruzo_tramo(consumos, umbral)`, `aviso_de_tramo(...)` |
| `adaptadores/claude-code/hook_presupuesto.py` | Modificar | `--modo cierre|aviso`, con `cierre` por defecto para no tocar lo instalado |
| `validadores/instalar.py` | Modificar | Una fila más: `UserPromptSubmit`, `--modo aviso` |
| `validadores/tests/test_el_consumo_se_ve_a_tiempo.py` | Nuevo | Los casos |
| `documentacion/automatismos/spec.md` | Modificar | §4.6 con las RN y §13 con la trazabilidad |
| `anatomia/mapa-del-sitio.md` | Modificar | La fila del enganche, con sus dos eventos |
| `CHANGELOG.md` · `VERSION` | Modificar | Dentro de la entrada 27.1.0 del día |
| `.claude/settings.json` de los 9 proyectos | Modificar | Lo escribe el instalador |

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
| Tramo por defecto de **1.000.000** | 200.000, que es el tope de `notas/estructura.md` §3.2; o 500.000 | Con 200 mil avisa en todas las sesiones, hasta en la de 144 mil; con un millón avisa de 0 a 12 veces según el tamaño real medido. Un aviso que sale siempre se deja de leer |
| El cruce se decide **sin estado**: total con el último turno contra total sin él | Una marca en un archivo, como el resumen | El enganche no tiene archivo propio del proyecto donde marcar, y crear uno para esto es más estado del que la información vale |
| `--modo cierre` por defecto | Cambiar el comando de `Stop` a `--modo cierre` | Cambiar el comando instalado vence el enganche en los 9 proyectos hasta reinstalar (la 26.0.1 ya pagó ese precio). Con el defecto, lo instalado sigue valiendo |
| Se cuenta entrada más salida, sin caché | Contar también la caché leída | La caché leída es lo barato; contarla infla el número y el tramo deja de significar gasto |

### 2.7 Dudas por resolver antes de codificar

Ninguna. Todo lo que el plan afirma se leyó en el código el 2026-08-20.

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — en la HU: [CA-01](../HU-014-el-consumo-se-ve-a-tiempo.md#ca-01--al-terminar-se-reporta-el-consumo-de-la-sesión)

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Caso que fija el reporte de cierre tal como está (texto y cifras) | Prueba | 0,25 h | — | EV-01 |

### CA-02 — en la HU: [CA-02](../HU-014-el-consumo-se-ve-a-tiempo.md#ca-02--al-cruzar-un-tramo-se-avisa-una-vez)

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-02 | `presupuesto.py`: `TRAMO`, `tramo()`, `cruzo_tramo()`, `aviso_de_tramo()` | Validador | 0,75 h | — | EV-01 |
| T-03 | `hook_presupuesto.py`: `--modo`, y en `aviso` imprimir solo si cruzó | Adaptador | 0,5 h | T-02 | EV-01 |
| T-04 | Fila `UserPromptSubmit` en `HOOKS_CLAUDE` | Instalador | 0,25 h | T-03 | EV-02 |

### CA-03 — en la HU: [CA-03](../HU-014-el-consumo-se-ve-a-tiempo.md#ca-03--sin-transcripción-calla-y-nunca-detiene)

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-05 | Los casos: cruce, mismo tramo, segundo tramo, umbral 0, sin ruta, ruta inexistente, línea ilegible | Prueba | 0,75 h | T-03 | EV-01 |

### RNF — requisitos no funcionales y cierre

| ID | Tarea | Categoría | Est. | Ev. |
|---|---|---|:--:|---|
| T-06 | Especificación §4.6 y §13, mapa del sitio | Documentación | 0,5 h | EV-03 |
| T-07 | Instalar en los 9 proyectos y verificar uno | Instalación | 0,25 h | EV-02 |

**Total estimado:** 3,25 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-02 → T-03 → T-05 → T-04 → T-07. **Paralelizable:** T-01 y T-06.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). Descubrir uno nuevo detiene la ejecución y amplía el plan con el OK del usuario.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| [CA-01](../HU-014-el-consumo-se-ve-a-tiempo.md#ca-01--al-terminar-se-reporta-el-consumo-de-la-sesión) | Caso automatizado sobre el modo de cierre | EV-01 | ☐ |
| [CA-02](../HU-014-el-consumo-se-ve-a-tiempo.md#ca-02--al-cruzar-un-tramo-se-avisa-una-vez) | Tres casos: cruce, mismo tramo, segundo tramo | EV-01 | ☐ |
| [CA-03](../HU-014-el-consumo-se-ve-a-tiempo.md#ca-03--sin-transcripción-calla-y-nunca-detiene) | Tres casos de entrada rota | EV-01 | ☐ |
| RNF-01 · silencio entre tramos | El caso del mismo tramo | EV-01 | ☐ |
| RNF-02 · no se nota | Tiempo del enganche sobre la transcripción real más grande (12,7 M) | EV-02 | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Suite | `validadores/tests/test_el_consumo_se_ve_a_tiempo.py` |
| EV-02 | Salida del instalador y medición de tiempo | `resultado_pruebas.md` §2 |
| EV-03 | Diff de los documentos | `funcionalidad_implementada.md` §3 |

## 6. Datos y ambiente de prueba

Transcripciones de mentira en archivos temporales, armadas con sumas conocidas (950.000 + 100.000, etcétera). Para el RNF-02 se lee la transcripción real más grande de esta máquina, solo lectura.

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Se revierte el commit. El modo de cierre no cambió, así que los proyectos siguen reportando igual; la fila nueva se quita al reinstalar.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12

Aditiva. Un proyecto al día sigue igual hasta reinstalar, y `checklist.py` se lo reclama. Entra en la **27.1.0 (MENOR)** del día.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md#t1--todo-cambio-con-lógica-lleva-prueba), [`08·T3`](../../../../../base/08-pruebas.md#t3--aisladas-deterministas-repetibles), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md), [`00·N2`](../../../../../base/00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada).
- Del repositorio: la frontera de `adaptadores/contrato.md`; la lección de la 26.0.1 sobre no vencer comandos instalados.

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que `UserPromptSubmit` no traiga `transcript_path` en alguna versión de la herramienta | El aviso calla | Es el mismo campo que usa `hook_historico.py --modo agente`; si falta, calla con código 0 y el reporte de cierre sigue | Abierto por diseño |
| B-02 | El tramo no le sirve a un proyecto chico | Nunca avisa | `--umbral` por proyecto en el comando instalado, sin tocar código | Abierto por diseño |

## 11. Definition of Done

- [ ] Los tres CA verificados con evidencia (§5)
- [ ] RNF-01 y RNF-02 validados
- [ ] `validadores/tests/` y `validadores/pruebas.py` en verde
- [ ] Trazabilidad en la especificación §13 sin faltantes
- [ ] Mapa del sitio al día
- [ ] Señales registradas
- [ ] Instalado en los 9 proyectos
- [ ] Listo para el commit único, que el usuario autoriza aparte

## 12. Seguimiento diario

N/A: el trabajo lo lleva una sola persona y el avance va en el `estado-fase.md` §1.2.

## 13. Cierre

**No se escribe acá.** Vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
