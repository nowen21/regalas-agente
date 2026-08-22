# Plan de Trabajo — Fase B-EP-001-HU-009-el-sello-no-se-contradice (módulo Cuerpo de reglas)

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden y sobre qué archivos. El requisito vive en [HU-009](../HU-009-reglas-sin-checklist-al-dia.md); las pruebas, en el [plan_pruebas.md](plan_pruebas.md).

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-001-HU-009-el-sello-no-se-contradice` |
| **Épica** | [EP-001 Cuerpo de reglas heredable](../../epica.md) |
| **HU** | [HU-009 Poner al día las reglas que no pasan su propio checklist](../HU-009-reglas-sin-checklist-al-dia.md) — una sola ([`02·F12.1`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) |
| **Módulo** | Cuerpo de reglas — los bloques de checklist de `base/` |
| **Fecha apertura** | 2026-08-18 |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 🐛 **Defecto.** Es la fase `B` porque la [`A`](../A-EP-001-HU-009-clasificar-las-que-faltan/) ya cerró con el `CA-02`.

**De dónde sale:** aplicarle el checklist a los veinte capítulos, trabajo del [pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md](../../../../../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md). Al ir a arreglar las reglas que reprueban se encontró que **algunos sellos no dicen lo que su propia tabla dice**.

**CA que cubre:** el `CA-01` en su parte comprobable —que el resultado escrito de cada regla sea verificable— y el transversal de **no regresión**: *«una regla que ya traía su checklist no lo pierde ni cambia de resultado sin motivo escrito»*.

---

## 1. Objetivo y alcance

**Objetivo:** que ningún bloque de checklist de `base/` afirme dos cosas contrarias, y que no pueda volver a pasar sin que un programa lo diga.

**El defecto no es de juicio, es de transcripción.** En los cinco casos el texto razona bien y la tabla quedó mal — en cuatro, corriendo una casilla del bloque `C`. Nadie se equivocó al evaluar la regla: se equivocaron al pasarlo a la tabla, que es justo lo que un programa hace sin fallar.

**Y pesa porque la tabla es lo que se lee.** Nadie recorre veinte filas de prosa: se mira el renglón de emoticones y se sigue. Cuando las dos mitades del sello se contradicen, gana la falsa.

**Fuera de alcance:**

- **Arreglar las reglas que reprueban.** Esta fase corrige el **sello**, no la regla. Que `C10` nombre `SQLite` sigue estando mal después de esta fase; lo que cambia es que ahora su tabla lo dice.
- **Volver a juzgar ninguna fila.** Donde la tabla y el texto discrepan, manda el texto: es la mitad razonada.
- **El resto del 19.** Las 72 reglas en NO CUMPLE siguen igual.

---

## 2. Análisis previo — línea base verificada

**Medido el 2026-08-18, sobre las 200 reglas del cuerpo:**

| Qué | Cuántas |
|---|---|
| Sellos cuyo texto reprueba una fila que su tabla da por buena | **5** |
| Sellos cuya línea de totales no coincide con su tabla | **10** |
| Reglas con dos bloques de checklist apilados | **1** (`M14`) |

### 2.1 Los cinco que se contradicen

| Regla | Qué decía el texto | Qué decía la tabla |
|---|---|---|
| [`01·C10`](../../../../../base/01-conducta.md#c10--cada-mensaje-del-usuario-se-evalúa-como-posible-mejora-del-setup) | filas 5, 9 y 10 | 8 y 9 |
| [`01·C15`](../../../../../base/01-conducta.md#c15--al-replicar-un-patrón-replicar-la-paridad-completa) | filas 5, 10 y 14 | 10 y 14 |
| [`01·C16`](../../../../../base/01-conducta.md#c16--re-lee-justo-antes-de-editar--nunca-sobre-contexto-viejo) | filas 5, 10, 11 y 14 | 10, 11 y 14 |
| [`03·D1`](../../../../../base/03-datos.md#d1--normaliza-audita-e-indexa) | filas 9, 10 y 11 | 8, 9 y 10 |
| [`03·D4`](../../../../../base/03-datos.md#d4--valores-configurables-van-a-catálogo--cero-hardcode) | filas 9, 10 y 16 | 8, 9 y 16 |

**Cuatro de los cinco son el mismo error: una casilla corrida** en el bloque `C`, que va de la fila 7 a la 13. Es un bloque de siete casillas sin encabezado por columna, y contar de memoria hasta la séptima falla.

**Y en los tres del capítulo `01`, lo que se perdió fue siempre la fila 5** — la que dice que la base no nombra tecnología. Se escribió en el texto y no llegó a la tabla, tres veces.

### 2.2 Archivos que se crean o modifican

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/metareglas.py` | Modificar | Las tres comprobaciones |
| `validadores/tests/test_el_sello_no_se_contradice.py` | Nuevo | Los casos |
| `base/01-conducta.md` | Modificar | Las tablas de `C10`, `C15`, `C16`; los totales de `C1`, `C15`, `C16`, `C17`, `C18` |
| `base/03-datos.md` | Modificar | Las tablas de `D1` y `D4`; los totales de `D4` y `D5` |
| `base/00-nucleo-blindado.md` | Modificar | El total de `N1` |
| `base/08-pruebas.md` | Modificar | El total de `T1` |
| `base/20-meta-reglas/reglas/M14-…md` | Modificar | Quitar el sello apilado de la `v2.1.0` |
| `pendientes/19-…md` | Modificar | Lo que esta fase deja medido |
| `CHANGELOG.md` · `VERSION` | Modificar | **PARCHE** |

**Ninguna regla cambia de texto.** Solo cambian sellos: lo que se corrige es la descripción del veredicto, no la norma. Por eso es PARCHE y no MENOR.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **Manda el texto, no la tabla** | Manda la tabla | El texto es la mitad razonada: dice *por qué* falla cada fila. La tabla es su resumen, y un resumen mal copiado se corrige contra el original |
| Se reporta **una sola dirección** | Exigir que cada ❌ tenga su párrafo | El texto agrupa —«son tres reglas en una»— y no tiene por qué desglosar. Exigirlo volvería la comprobación ruido sobre sellos correctos |
| Un sello en **CUMPLE** no se compara contra su prosa | Compararlo igual | Un CUMPLE suele contar **qué reprobaba antes de corregirlo**. Compararlo daría contradictorio justo lo contrario. Es el caso de [`17·I6`](../../../../../base/17-interfaz.md#i6--funciona-en-los-tamaños-de-pantalla-que-el-proyecto-soporta), y salió como falso positivo en la primera corrida |
| Un CUMPLE **sí** se comprueba contra su tabla | Dejarlo pasar | Un sello que dice CUMPLE con un ❌ en la tabla es la misma contradicción por el otro lado, y esa sí es incondicional |
| Los totales se cuentan de la tabla | Contarlos de la prosa | La tabla es lo que alguien puede verificar casilla por casilla |
| Una tabla que no suma 20 **se dice**, no se corrige | Corregir el total igual | Corregir un total contra una tabla incompleta manda a arreglar lo que no es |

### 2.7 Dudas por resolver antes de escribir

**Ninguna.** Las dos que aparecieron —quién manda entre tabla y texto, y qué hacer con los CUMPLE que narran lo corregido— se resolvieron con el propio cuerpo de reglas delante y quedaron en §2.6.

---

## 3. Desglose de tareas

| ID | Tarea | Est. |
|---|---|:--:|
| T-01 | Medir cuántos sellos se contradicen, y de qué forma | 0,5 h |
| T-02 | La comprobación de tabla contra texto | 1 h |
| T-03 | La comprobación de la línea de totales | 0,5 h |
| T-04 | La de los sellos apilados | 0,25 h |
| T-05 | Corregir los cinco que se contradicen | 0,5 h |
| T-06 | Recalcular los diez totales | 0,5 h |
| T-07 | Los casos de prueba | 1 h |
| T-08 | Versionar y anotar lo medido en el 19 | 0,5 h |

**Total estimado:** 4,75 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-05 → T-07.

**T-02 va antes que T-05**, y no al revés. Corregir primero los cinco y escribir después la comprobación deja sin comprobar que la comprobación sirve: se estrenaría sobre un cuerpo ya limpio, sin un solo caso que encontrar. Escribiéndola antes, **los cinco los encontró ella**.

> Solo se tocan los archivos declarados en §2.2 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación

| CA | Método | Estado |
|---|---|---|
| CA-01 · el resultado escrito es verificable | `validar.py metareglas` sin hallazgos de esta familia | ☑ |
| Transversal · no regresión | Ninguna regla cambia de texto; las dos suites | ☑ |
| El caso de `I6` no se reporta | Caso dedicado | ☑ |

---

## 6. Datos y ambiente de prueba

Sellos de mentira armados en el propio caso, más **una prueba contra `base/` de verdad** que exige cero. Es la que se cae cuando alguien vuelva a escribir un sello a mano — que es exactamente cuando hace falta que se caiga.

---

## 7. Reversión / rollback

Se revierte volviendo el commit atrás. No hay dato ni estado externo.

---

## 8. Producción y migración incremental

**Aditiva.** Un proyecto que herede el estándar no tiene que hacer nada: las comprobaciones corren sobre `base/`, que es de acá.

---

## 9. Reglas del estándar aplicadas

[`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md), [`20·M14`](../../../../../base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Acción | Estado |
|---|---|---|---|
| B-01 | Falsos positivos sobre los sellos en CUMPLE que narran lo corregido | Salió en la primera corrida, con `I6`. Los CUMPLE no se comparan contra su prosa, y hay caso | **Cerrado** |
| B-02 | Que corregir la tabla cambie el veredicto de una regla | No pasa: los cinco ya decían NO CUMPLE, y lo siguen diciendo. Lo que cambia es **cuántas** filas fallan | **Cerrado** |
| B-03 | Que la comprobación pida desglosar en prosa cada ❌ de la tabla | Se reporta una sola dirección, con caso que lo fija | **Cerrado** |
| B-04 | Que el sello quede bien y la regla siga mal | **Es así a propósito, y hay que decirlo:** esta fase no arregla ninguna regla. Las 72 en NO CUMPLE siguen ahí | Abierto — es el 19 |

---

## 11. Definition of Done

- [x] Las tres comprobaciones, con sus casos
- [x] Los cinco sellos que se contradecían, corregidos
- [x] Los diez totales recalculados desde su tabla
- [x] El sello apilado de `M14`, quitado
- [x] `validar.py metareglas` sin hallazgos de esta familia
- [x] Versionada
- [ ] Aceptada por el usuario

---

## 13. Cierre

**No se escribe acá.** Vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
