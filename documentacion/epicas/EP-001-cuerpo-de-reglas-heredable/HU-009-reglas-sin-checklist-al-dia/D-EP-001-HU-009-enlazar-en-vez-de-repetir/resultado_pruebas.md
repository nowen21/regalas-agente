# Resultado de Pruebas — Fase D-EP-001-HU-009: enlazar en vez de repetir

| Campo | Valor |
|---|---|
| **Plan de pruebas** | [PP-D-EP-001-HU-009](plan_pruebas.md) v1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-18 |

---

## 1. Casos ejecutados

| Caso | Veredicto | Qué dio |
|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--q7-se-queda-con-lo-suyo) | ✅ **Pasa** | `Q7` en CUMPLE, con la forma de `EST3` |
| [CP-002](plan_pruebas.md#cp-002--pr4-se-queda-con-lo-suyo) | ✅ **Pasa** | `PR4` en CUMPLE; `E5` no dice nada de pantallas |
| [CP-003](plan_pruebas.md#cp-003--pr4-declara-su-dependencia) | ✅ **Pasa** | `depende de 05·E5`, sin ciclo |
| [CP-004](plan_pruebas.md#cp-004--el-ejemplo-de-pr4-corresponde-a-lo-que-dice-hoy) | ✅ **Pasa** | El ejemplo es de pantalla |
| [CP-005](plan_pruebas.md#cp-005--lo-que-se-quitó-sigue-rigiendo) | ✅ **Pasa** | Cada frase eliminada está en su dueña |
| [CP-006](plan_pruebas.md#cp-006--el-conteo-baja-exactamente-dos) | ✅ **Pasa** | **72 → 70** |
| [CP-007](plan_pruebas.md#cp-007--nada-de-lo-que-ya-estaba-deja-de-pasar) | ✅ **Pasa** | Ver §2 |

**7 de 7 ejecutados. 7 pasan.**

---

## 2. CP-007 · No regresión

| Qué se corrió | Resultado |
|---|---|
| `validadores/tests/` | **154 · OK** |
| `validadores/pruebas.py` | **357 · OK** (5 fallos esperados, los de siempre) |
| `validar.py estandar` | **Sin incumplimientos** |
| Reglas en NO CUMPLE | **72 → 70** |

---

## 3. Qué se quitó y qué quedó

| Regla | Se fue | Quedó | Largo |
|---|---|---|---|
| `07·Q7` | *«refactorizar de más o mejorar de paso fuera de la tarea, no»* — es `01·C3` | el criterio de alcance como **motivo enlazado**, y decirlo para su tarea | 211 → **191** |
| `12·PR4` | *«logs y errores sin datos personales… usa identificadores, no el dato en claro»* — es `05·E5` | pantallas, reportes y mensajes a terceros | 242 → **220** |

**En `PR4` lo que importa no es que acorte** —22 caracteres— **sino que lo que queda es suyo.** Antes la mitad de la regla regía por `E5` y esta la repetía; hoy la enlaza y aporta lo que ninguna otra dice.

---

## 4. Lo que se supo ejecutando

### El defecto se leía como diligencia

**Las dos enlazaban a la vecina.** El enlace estaba puesto, visible, correcto — y aun así reprobaban, porque la fila 11 no pide enlazar: pide enlazar **en vez de** copiar. Un enlace delante de un texto repetido se lee como cuidado, no como duplicación.

Es por eso que las dos sobrevivieron a varias lecturas: **cumplían la mitad que se ve.**

### El modelo estaba en el propio cuerpo, y nadie los había leído juntos

[`14·EST3`](../../../../../base/14-estructura-codigo.md#est3--respeta-el-legacy--la-convención-es-para-lo-nuevo) toma de `01·C3` **el mismo criterio de alcance** que `Q7`, y estaba en CUMPLE. La diferencia era la forma: `EST3` nombra a `C3` entre paréntesis como el **motivo** y todo lo demás es suyo; `Q7` reformulaba el criterio entero antes de enlazarlo.

**La respuesta a cómo se escribe esta regla ya estaba escrita, en otra regla del mismo cuerpo.** El análisis del 2026-08-07 las había nombrado juntas; lo que faltaba era usar una como molde de la otra.

### Tres capas del mismo criterio, y solo una aporta

`00·N6` (blindada) → `05·E5` → `12·PR4`, cada una reformulando a la anterior. Al separarlas, **la única parte que no dice ninguna otra regla es la mitad de pantallas y reportes de `PR4`** — `E5` habla de logs.

Es lo que la salvó de derogarse, y es la clase de cosa que solo aparece leyendo las tres seguidas.

### El ejemplo se quedaba ilustrando lo que la regla dejó de decir

El de `PR4` era de logs. Al irse esa mitad, el ejemplo apuntaba a una exigencia que ya no estaba ahí — **peor que no tener ninguno**, porque manda a buscar donde no es. Se cambió con la regla: el reporte que enseña el teléfono del denunciante a cualquiera «porque ya está en la base».

---

## 5. Lo que queda abierto  ·  [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)

**La categoría queda a medias, y se dice en vez de taparse.** Siguen repitiendo al vecino:

| Regla | Por qué no se tocó |
|---|---|
| `12·PR3` | **No exige nada propio**: sus cuatro frases remiten al `04`. La salida es quedarse con lo que `04` no dice **o derogarla**, y eso lo decide el usuario |
| `01·C16` | Repite a `01·C2` y lo admite por escrito, pero su arreglo pasa por normalizar el bloque `Encadenamiento` en **cuatro reglas a la vez** |
| `04·S7` | Sus dos sellos —el suyo y el de `10·DEP3`— prescriben **derogarla**. Una derogación obliga a adoptarla ([`02·F22`](../../../../../base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md)) y eso es del usuario |

---

## 6. Veredicto

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | el `CA-01` en la fila 11, para las dos que no piden decisión |
| **CA en «No»** | ninguno |
| **Defectos abiertos aceptados** | tres: `PR3`, `C16` y `S7`, cada uno con su motivo |
| **Ciclos** | 1 |
