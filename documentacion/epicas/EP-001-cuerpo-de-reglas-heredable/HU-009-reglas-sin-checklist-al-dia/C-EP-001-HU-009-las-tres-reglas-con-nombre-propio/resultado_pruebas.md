# Resultado de Pruebas — Fase C-EP-001-HU-009: las tres reglas con nombre propio

| Campo | Valor |
|---|---|
| **Plan de pruebas** | [PP-C-EP-001-HU-009](plan_pruebas.md) v1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-18 |

---

## 1. Casos ejecutados

| Caso | Veredicto | Qué dio |
|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--los-nombres-que-ya-estaban-en-la-lista) | ✅ **Pasa** | Los cinco |
| [CP-002](plan_pruebas.md#cp-002--node-no-estaba-en-la-lista) | ✅ **Pasa** | Ahora se reporta |
| [CP-003](plan_pruebas.md#cp-003--softdeletes-tampoco-estaba) | ✅ **Pasa** | Ahora se reporta |
| [CP-004](plan_pruebas.md#cp-004--los-nombres-del-oficio-no-se-reportan) | ✅ **Pasa** | Los tres callan |
| [CP-005](plan_pruebas.md#cp-005--las-palabras-de-esta-casa-no-se-reportan) | ✅ **Pasa** | Silencio |
| [CP-006](plan_pruebas.md#cp-006--no-se-reporta-una-palabra-dentro-de-otra) | ✅ **Pasa** | «reaccionar» y «nodo» limpios |
| [CP-007](plan_pruebas.md#cp-007--en-base-solo-queda-el-declarado) | ✅ **Pasa** | Exactamente `{S11}` |
| [CP-008](plan_pruebas.md#cp-008--ninguna-de-las-cuatro-cambia-de-norma) | ✅ **Pasa** | 72 y 72 |
| [CP-009](plan_pruebas.md#cp-009--nada-de-lo-que-ya-estaba-deja-de-pasar) | ✅ **Pasa** | Ver §2 |

**9 de 9 ejecutados. 9 pasan.** 7 casos automatizados en [validadores/tests/test_la_base_no_nombra_stack.py](../../../../../validadores/tests/test_la_base_no_nombra_stack.py).

---

## 2. CP-009 · No regresión

| Qué se corrió | Resultado |
|---|---|
| `validadores/tests/` | **145 · OK** — eran 138 |
| `validadores/pruebas.py` | **357 · OK** (5 fallos esperados, los de siempre) |
| `validar.py estandar` | **Sin incumplimientos** |
| `validar.py metareglas` | 72 fallas · 120 avisos — **un solo hallazgo de fila 5**, el declarado |
| Reglas en NO CUMPLE, antes y después | **72 y 72** |

---

## 3. Qué se quitó y qué se conserva

| Regla | Decía | Dice |
|---|---|---|
| `01·C10` | «tests con SQLite in-memory · nunca MariaDB» | «las pruebas corren contra una base en memoria, nunca contra el motor de producción» |
| `01·C10` | «el rol id=2 es X en este ERP» | «el identificador 2 es el rol que aprueba» |
| `01·C10` | «¿tendría sentido en un proyecto React + Django de otra empresa?» | «¿tendría sentido en otra empresa, con otro lenguaje y otro negocio?» |
| `01·C15` | «el módulo Aportes» | «el módulo de referencia» |
| `01·C16` | las órdenes de lectura y edición del agente | el paso, no la orden |
| `01·C16` | dos órdenes del control de versiones | «pregúntale al control de versiones si…» |
| `04·S10` | «todos los `node`», «todos los `php`» | «todos los procesos de tal intérprete» |

**Se conservan tres a propósito:** `killall`, `pkill` y `taskkill` en `04·S10`. No son producto ni framework — son cómo se llama la misma acción en cada sistema, y quitarlos deja la regla sin decir qué prohíbe. **Tienen su caso** ([CP-004](plan_pruebas.md#cp-004--los-nombres-del-oficio-no-se-reportan)) para que la próxima pasada no los borre creyendo que mejora.

---

## 4. Lo que se supo ejecutando

### `C10` no pasaba la pregunta que ella misma manda hacerse

Es la regla que enseña a decidir si algo es transversal o local, y **su criterio para decidirlo nombraba dos frameworks**: *«¿esta regla tendría sentido en un proyecto React + Django de otra empresa?»*. La pregunta que le pedía al agente hacerse era la que no pasaba.

### `S10` no estaba en la lista de tres, y por qué se le pasó

El pendiente 19 hablaba de **tres** reglas con nombre propio. La cuarta la encontró el programa, no una lectura — y el motivo está escrito en el sello viejo de `S10`: **sí había argumentado la fila 5**, para defender `killall`, `pkill` y `taskkill`, y **al hacerlo la dio por revisada**. Los dos intérpretes estaban tres líneas más arriba.

> **Un argumento sobre una fila no es una revisión de la fila.** Quien lee el sello ve que alguien la miró; no ve qué parte miró. Es el mismo mecanismo que la fase `B` encontró en las tablas, un nivel más adentro.

### El detector callaba la mitad

`04·S10` decía `node` y `php`, y **solo se reportaba `php`**: `node` no estaba en la lista. Por eso el sello pudo dar la fila por buena sin contradecir al programa — los dos miraban distinto y ninguno veía el conjunto.

### Escribir en concepto cuesta caracteres

`C10` pasó de 1724 a **1780**. Es el precio de que la base sirva a cualquier proyecto, y se paga: la fila 10 ya reprobaba y sigue reprobando. Lo contrario —dejar el nombre porque acorta— es el motivo por el que el ejemplo de `03·D8` sobrevivió cuatro meses.

---

## 5. Lo que queda abierto  ·  [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)

- **`04·S11` sigue nombrando `SoftDeletes`**, y es a propósito: su sello decidió que reescribirlo en concepto es parte de partir la regla. Lo nuevo es que ahora **el programa lo dice también**, en vez de callar.
- **Las tres del capítulo `01` siguen en NO CUMPLE** por las otras filas: `C10` tiene tres exigencias, `C15` y `C16` usan el bloque `Encadenamiento` fuera de las tres formas de `M7`, y `C16` duplica a `C2` por escrito.
- **Los nombres que ni el sello ni el programa conocen todavía.** La lista del detector se estrecha cada vez que aparece uno, y hoy no hay forma de saber cuántos faltan.

---

## 6. Veredicto

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | el `CA-01` en la fila 5, y el transversal de no regresión |
| **CA en «No»** | ninguno |
| **Defectos abiertos aceptados** | dos: `S11` declarado, y las otras filas de las tres del `01` |
| **Ciclos** | 1 |
