# Funcionalidad implementada — Fase A-EP-006-HU-002-retrodocumentar-el-guardado-en-el-repositorio (módulo Memoria)

> **Veredicto de la fase: [No cumple](resultado_pruebas.md#6-veredicto-de-la-fase).** Los 18 recuerdos viven en el repositorio con su historial legible y su índice cuadrado en los dos sentidos. Las **237 señales, no**: `memoria/senales.db` está excluida del control de versiones. La salida está propuesta y **sin decidir**, que es lo que el plan pedía.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-002-retrodocumentar-el-guardado-en-el-repositorio` |
| **Módulo** | Memoria — [`historico-chat/memory/`](../../../../../historico-chat/memory/memory.md) y [`memoria/senales.db`](../../../../../memoria/esquema.sql) |
| **Especificación del módulo** | No la hay aparte: la especificación son los CA de [HU-002](../HU-002-guardar-en-el-repositorio.md) y [`01·C19`](../../../../../base/01-conducta.md#c19--escribe-la-memoria-del-agente-dentro-del-repositorio-del-proyecto) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / exigencias cubiertas** | HU-002: [CA-01](../HU-002-guardar-en-el-repositorio.md#ca-01--lo-guardado-vive-en-el-repositorio-y-se-ve-en-el-historial), [CA-02](../HU-002-guardar-en-el-repositorio.md#ca-02--hay-un-índice-que-dice-de-qué-trata-cada-cosa) y sus dos transversales |
| **Fecha de cierre** | 2026-08-17 |
| **Commit** | Pendiente de autorización del usuario |

---

## 1. Qué se implementó — resumen

**Nada de programa: la fase escribió la prueba del índice y midió lo que el CA-01 daba por hecho.** Los recuerdos en el repositorio y su índice están en producción desde `01·C19`. Lo que no existía era una prueba que comprobara el cuadre **en los dos sentidos**, ni nadie había mirado si la otra mitad de la memoria —las señales— cumple el mismo criterio.

No lo cumple, y no por descuido.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| Los recuerdos viven en el repositorio, como texto | datos | [`historico-chat/memory/`](../../../../../historico-chat/memory/memory.md) — 18 archivos | ✅ Ya existía | CP-001 |
| Su historial dice qué cambió, línea por línea | herramienta | `git log -p`, sin nada extra | ✅ Ya existía | CP-001 |
| **Las señales viven en el repositorio** | datos | `memoria/senales.db` está en `.gitignore` | ❌ **No se cumple** | CP-002 |
| Hay un índice que dice de qué trata cada uno | datos | `historico-chat/memory/memory.md` | ✅ Ya existía | CP-003, CP-004 |
| El cuadre del índice, en los dos sentidos | pruebas | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `IndiceDeLosRecuerdos` | ✅ Escrito acá | 5 pruebas en verde |
| Que ningún recuerdo lleve claves | pruebas | La misma clase, con el detector de `04·S4` | ✅ Escrito acá | 0 hallazgos |

### 2.2 Criterios de aceptación

| CA | Cómo quedó cubierto | Estado |
|---|---|---|
| CA-01 | Los 18 recuerdos sí; las 237 señales no tienen historial | ❌ |
| CA-02 | 18 de 18 en los dos sentidos; por el índice se llega abriendo un archivo | ✅ |
| Transversal · Privacidad | 0 hallazgos del detector de secretos sobre los recuerdos | ✅ |
| Transversal · Límites | Un índice vacío es válido: probado | ✅ |

---

## 3. Lo que la fase midió

| Medición, 2026-08-17 | Valor |
|---|---|
| Recuerdos en el repositorio | **18** |
| Recuerdos sin línea en el índice | **0** |
| Líneas del índice sin archivo | **0** |
| Archivos que hubo que abrir para ubicar un tema | **1** |
| Señales guardadas | **237** |
| Commits en el historial de `memoria/senales.db` | **0** |
| Hallazgos de secretos en los recuerdos | **0** |

**La fila de los cero commits es el hallazgo.** No es que el historial de un binario se lea mal: es que **no hay historial**. `.gitignore` línea 10 excluye la base, con su motivo escrito — *«la base es del usuario, no del estándar»*—, que es una decisión razonable para un proyecto cualquiera y deja a este repositorio con 237 señales que solo existen en una máquina.

---

## 4. La salida, propuesta y sin decidir

La tarea `T-03` del plan pedía exactamente esto: proponer, no decidir. Las tres salidas, con lo que cuesta cada una, están en [§2 del resultado](resultado_pruebas.md#detalle-de-cp-002--qué-se-puede-leer-del-historial-de-la-base-de-señales):

| Salida | En una línea |
|---|---|
| **A** · exportar las señales a texto junto a la base | Devuelve el historial y la copia; hay que mantener el export |
| **B** · declarar el límite en la HU | Cuesta cero; las señales siguen sin historial ni copia |
| **C** · versionar el `.db` tal cual | Historial ilegible, y en otro proyecto mete datos del usuario al repositorio |

**Ninguna se ejecutó.** Cero señales exportadas o movidas en esta fase, que era la meta del plan.

---

## 5. Decisiones y señales

| Decisión | Dónde quedó |
|---|---|
| El cuadre del índice se comprueba **en los dos sentidos**: con uno solo pasa la mitad de los errores | Clase `IndiceDeLosRecuerdos` y CP-003 del [resultado](resultado_pruebas.md) |
| La privacidad se comprueba con el **detector de secretos**, no a ojo: a ojo, un recuerdo nuevo con una clave pasaría el día que nadie mire | La misma clase |
| El índice **vacío es válido**: un proyecto sin recuerdos todavía no está en falta | La misma clase |
| El límite de las señales se escribe **con lo medido** —cero commits— y no con lo supuesto —«el historial de un binario no se lee» | CP-002 del resultado |

---

## 6. Lo que no entró, y dónde sigue

| Qué | Dónde |
|---|---|
| Elegir entre A, B y C para el historial de las señales | **Decisión del usuario.** Sin fase hasta que se elija |
| Qué se guarda, con qué tipo y alcance | [HU-001](../../HU-001-que-se-guarda-tipos-y-alcances/HU-001-que-se-guarda-tipos-y-alcances.md) |
| Sacar del almacén local lo que deba vivir en el repositorio | [HU-006](../../HU-006-sacar-del-almacen-local/HU-006-sacar-del-almacen-local.md) |

**La advertencia que deja esta fase:** la memoria tiene dos mitades y solo una está en el repositorio. La que se escribe a mano —18 recuerdos— tiene historial, revisión y copia. La que se acumula sola —237 señales— no tiene ninguna de las tres, y es la más grande.
