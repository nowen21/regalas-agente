# Funcionalidad implementada — Fase «B-EP-001-HU-009-el-sello-no-se-contradice»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito **qué quedó hecho**, para que quien llegue después no tenga que deducirlo del código ni del historial.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-001-HU-009-el-sello-no-se-contradice` |
| **Épica / HU** | [EP-001](../../epica.md) · [HU-009](../HU-009-reglas-sin-checklist-al-dia.md) |
| **Versión del estándar** | 23.7.1 → **23.7.2** (PARCHE) |
| **Fecha de cierre** | 2026-08-18 |

---

## 1. Qué quedó funcionando

**Ningún bloque de checklist de `base/` afirma ya dos cosas contrarias**, y tres comprobaciones lo mantienen así:

| Comprobación | Qué encuentra | Cuántos había |
|---|---|---:|
| El texto reprueba una fila que la tabla da por buena | La mitad razonada del sello y su resumen no coinciden | **5** |
| La línea de totales no cuadra con su tabla | El resumen dice una cuenta y la tabla tiene otra | **10** |
| Dos bloques de checklist apilados | Un sello viejo encima del nuevo | **1** |

**El defecto no era de juicio, era de transcripción.** En los cinco casos el texto evaluaba bien y la tabla quedó mal — en cuatro, **corriendo una casilla del bloque `C`**, que son siete seguidas sin encabezado por columna. Es exactamente lo que un programa hace sin fallar y una persona no.

**Y pesa porque la tabla es lo que se lee.** Nadie recorre veinte filas de prosa: se mira el renglón de emoticones y se sigue. Cuando las dos mitades se contradicen, gana la que se ve, que era la falsa.

### Lo que se supo al medir

- **En los tres sellos del capítulo `01` la fila que se perdió fue siempre la 5** — la que dice que la base no nombra tecnología. Escrita en el texto las tres veces, y las tres veces sin llegar a la tabla.
- **Nueve de los diez totales fallaban por el mismo lado:** una N/A de más y un ✅ de menos.
- **`M14` llevaba dos sellos superpuestos** desde el 2026-08-07, el de la `v2.1.0` encima del de la `v2.2.0`. Es la regla que dice que ninguna regla nace fuera del procedimiento.

---

## 2. Qué se tocó

| Archivo | Qué |
|---|---|
| [`validadores/metareglas.py`](../../../../../validadores/metareglas.py) | `_sello_se_contradice`, `_totales_del_sello`, `_un_solo_sello` |
| [`validadores/tests/test_el_sello_no_se_contradice.py`](../../../../../validadores/tests/test_el_sello_no_se_contradice.py) | 15 casos, uno por cada cosa que pasó de verdad |
| [`base/01-conducta.md`](../../../../../base/01-conducta.md) | Tablas de `C10`, `C15`, `C16`; totales de `C1`, `C15`, `C16`, `C17`, `C18` |
| [`base/03-datos.md`](../../../../../base/03-datos.md) | Tablas de `D1` y `D4`; totales de `D4` y `D5` |
| [`base/00-nucleo-blindado.md`](../../../../../base/00-nucleo-blindado.md) · [`08-pruebas.md`](../../../../../base/08-pruebas.md) | Totales de `N1` y `T1` |
| [`base/20-meta-reglas/reglas/M14-…md`](../../../../../base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md) | Fuera el sello apilado de la `v2.1.0` |
| [`pendientes/19-…`](../../../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md) | Lo que esta fase deja medido. **Sigue abierto** |
| `CHANGELOG.md` · `VERSION` | 23.7.2 |

**Ninguna regla cambió de texto, y se comprobó línea por línea sobre el `diff`.** Las 72 en NO CUMPLE siguen siendo 72. Esta fase corrige **sellos**, no normas — por eso es PARCHE.

---

## 3. Lo que no hace

- **No arregla ninguna regla.** `C10` sigue nombrando `SQLite`, `MariaDB`, `React` y `Django`. Lo que cambió es que ahora su tabla lo dice, y ese es el [19](../../../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).
- **No vuelve a juzgar ninguna fila.** Donde las dos mitades discrepaban mandó el texto, que es la que razona.
- **No compara un CUMPLE contra su prosa.** Un sello en CUMPLE suele contar qué reprobaba **antes** de corregirlo, y compararlo daría contradictorio justo lo contrario. Es el caso de `17·I6`, y fue el falso positivo de la primera corrida.
- **No exige que cada ❌ tenga su párrafo.** El texto agrupa, y pedirlo volvería esto ruido sobre sellos correctos — que es como se apaga una comprobación.

---

## 4. Por qué la comprobación se escribió antes de corregir

Corregir primero los cinco y escribirla después la habría estrenado sobre un cuerpo ya limpio: **cero hallazgos, y ninguna forma de saber si sirve.** Escribiéndola antes, los cinco los encontró ella — y el falso positivo también.

Es lo mismo que [`02·F2`](../../../../../base/02-flujo-de-trabajo/reglas/F2-sin-spec-acordada-no-hay-codigo.md) pide un nivel más arriba: primero se dice qué se exige, después se arregla.
