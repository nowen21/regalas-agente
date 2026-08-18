# Resultado de Pruebas — Fase B-EP-001-HU-009: el sello no se contradice

| Campo | Valor |
|---|---|
| **Plan de pruebas** | [PP-B-EP-001-HU-009](plan_pruebas.md) v1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-18 |

---

## 1. Casos ejecutados

| Caso | Veredicto | Qué dio |
|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--el-texto-reprueba-una-fila-que-la-tabla-da-por-buena) | ✅ **Pasa** | Los dos pasos |
| [CP-002](plan_pruebas.md#cp-002--varias-filas-se-nombran-en-plural) | ✅ **Pasa** | «las filas 5 y 10» |
| [CP-003](plan_pruebas.md#cp-003--el-texto-agrupado-también-cuenta) | ✅ **Pasa** | `**Filas 8, 9 y 10**` se lee entero |
| [CP-004](plan_pruebas.md#cp-004--la-tabla-puede-marcar-más-de-lo-que-el-texto-desglosa) | ✅ **Pasa** | Silencio |
| [CP-005](plan_pruebas.md#cp-005--un-cumple-que-cuenta-lo-que-corrigió-no-se-reporta) | ✅ **Pasa** | Silencio — ver §3 |
| [CP-006](plan_pruebas.md#cp-006--un-cumple-con-una-cruz-en-la-tabla-sí-se-reporta) | ✅ **Pasa** | Reporta y dice CUMPLE |
| [CP-007](plan_pruebas.md#cp-007--los-totales-cuadran-con-su-tabla) | ✅ **Pasa** | Los dos pasos |
| [CP-008](plan_pruebas.md#cp-008--una-tabla-que-no-suma-veinte-se-dice-así) | ✅ **Pasa** | Dice que no suma 20, no que el total esté mal |
| [CP-009](plan_pruebas.md#cp-009--dos-bloques-apilados-se-reportan) | ✅ **Pasa** | «2 bloques» |
| [CP-010](plan_pruebas.md#cp-010--ningún-sello-del-estándar-se-contradice) | ✅ **Pasa** | Cero sobre las 200 reglas |
| [CP-011](plan_pruebas.md#cp-011--nada-de-lo-que-ya-estaba-deja-de-pasar) | ✅ **Pasa** | Ver §2 |

**11 de 11 ejecutados. 11 pasan.** 15 casos automatizados en [validadores/tests/test_el_sello_no_se_contradice.py](../../../../../validadores/tests/test_el_sello_no_se_contradice.py).

---

## 2. CP-011 · No regresión

| Qué se corrió | Resultado |
|---|---|
| `validadores/tests/` | **138 · OK** — eran 123 |
| `validadores/pruebas.py` | **357 · OK** (5 fallos esperados, los de siempre) |
| `validar.py estandar` | **Sin incumplimientos** |
| `validar.py metareglas` | 72 fallas · 123 avisos — **las mismas de antes**, ninguna de esta familia |
| Reglas en NO CUMPLE, antes y después | **72 y 72** |

**El paso 4 es el que fija el alcance, y salió igual.** Si el conteo hubiera bajado, esta fase habría cambiado una norma sin decirlo. Se comprobó además línea por línea sobre el `diff` de `base/`: **todo lo que cambió está dentro de un bloque de checklist.** Ninguna regla cambia de texto.

---

## 3. Lo que encontró la comprobación al estrenarse

**Se escribió antes de corregir nada, y por eso hay algo que contar.** Corregir primero los cinco y escribir la comprobación después la habría estrenado sobre un cuerpo ya limpio, sin un solo caso que encontrar — y sin saber si sirve.

### Los cinco que se contradicen

| Regla | El texto reprobaba | La tabla marcaba |
|---|---|---|
| `01·C10` | 5, 9, 10 | 8, 9 |
| `01·C15` | 5, 10, 14 | 10, 14 |
| `01·C16` | 5, 10, 11, 14 | 10, 11, 14 |
| `03·D1` | 9, 10, 11 | 8, 9, 10 |
| `03·D4` | 9, 10, 16 | 8, 9, 16 |

**Cuatro de cinco son el mismo error: una casilla corrida en el bloque `C`**, que va de la fila 7 a la 13. Siete casillas seguidas sin encabezado por columna, y contar de memoria hasta la séptima falla. No es un juicio equivocado — es una transcripción.

**Y en los tres del capítulo `01` la fila que se perdió fue siempre la 5**, la que dice que la base no nombra tecnología. Escrita en el texto las tres veces, y las tres veces sin llegar a la tabla.

### Los diez totales, y el patrón

Nueve de los diez fallaban **por el mismo lado: una N/A de más y un ✅ de menos.** `N1`, `C1`, `C15`, `C16`, `C17`, `C18`, `D4`, `D5`, `T1`. El décimo era `M14`, y era otra cosa (abajo).

En `C18` la diferencia era del otro tipo: el resumen decía 1 ❌ y la tabla marcaba 2. Se leyó el sello entero y **la tabla tenía razón** — el texto justifica las dos, solo que a la segunda no le escribió «Fila 14» delante.

### `M14` llevaba dos sellos apilados

El de la `v2.1.0` **encima** del de la `v2.2.0`, los dos del 2026-08-07. Quien leyera de arriba abajo se quedaba con el viejo, que además tenía la cuenta mal. Un sello se **reemplaza**, no se apila.

Es la regla que dice *«ninguna regla nace fuera del procedimiento»**, y llevaba once días con dos veredictos superpuestos.

---

## 4. El falso positivo que hubo que resolver

La primera corrida reportó **seis**, no cinco. El sexto era [`17·I6`](../../../../../base/17-interfaz.md#i6--funciona-en-los-tamaños-de-pantalla-que-el-proyecto-soporta), y **estaba bien**: su sello dice CUMPLE y cuenta que las filas 8 y 12 *reprobaban y se corrigieron*. La comparación leía esas filas como veredicto cuando eran historia.

**Un CUMPLE no se compara contra su prosa.** Lo que sí se le comprueba es que su tabla no traiga ni un ❌, que es contradicción incondicional. Los dos casos están en [CP-005](plan_pruebas.md#cp-005--un-cumple-que-cuenta-lo-que-corrigió-no-se-reporta) y [CP-006](plan_pruebas.md#cp-006--un-cumple-con-una-cruz-en-la-tabla-sí-se-reporta).

**Vale la pena decirlo porque es el modo de morir de estas comprobaciones:** una que reporta de más se apaga a la semana, y apagada no encuentra nada.

---

## 5. Lo que queda abierto  ·  [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)

**El sello queda bien y la regla sigue mal, y es a propósito.** `C10` sigue nombrando `SQLite`, `MariaDB`, `React` y `Django`; lo que cambió es que ahora su tabla lo dice. Las 72 reglas en NO CUMPLE siguen siendo 72.

Eso es el [19](../../../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md), y esta fase lo deja **medible**: antes, cinco de esas 72 tenían mal escrito cuántas filas les fallan.

---

## 6. Veredicto

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | el `CA-01` en su parte comprobable, y el transversal de no regresión |
| **CA en «No»** | ninguno |
| **Defectos abiertos aceptados** | uno: las 72 reglas que reprueban, fuera del alcance declarado en el plan §1 |
| **Ciclos** | 1 |
