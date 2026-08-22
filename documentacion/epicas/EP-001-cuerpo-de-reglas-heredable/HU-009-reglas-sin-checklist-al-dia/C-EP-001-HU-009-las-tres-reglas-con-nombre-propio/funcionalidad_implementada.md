# Funcionalidad implementada — Fase «C-EP-001-HU-009-las-tres-reglas-con-nombre-propio»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito **qué quedó hecho**, para que quien llegue después no tenga que deducirlo del código ni del historial.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `C-EP-001-HU-009-las-tres-reglas-con-nombre-propio` |
| **Épica / HU** | [EP-001](../../epica.md) · [HU-009](../HU-009-reglas-sin-checklist-al-dia.md) |
| **Versión del estándar** | 23.7.2 → **23.7.3** (PARCHE) |
| **Fecha de cierre** | 2026-08-18 |

---

## 1. Qué quedó funcionando

**Ninguna regla de `base/` nombra ya un lenguaje, un framework, un motor, una herramienta del agente ni un módulo de un proyecto real** — salvo una, declarada, con su motivo escrito.

**Eran tres según el pendiente 19. Eran cuatro.**

| Regla | Qué nombraba |
|---|---|
| [`01·C10`](../../../../../base/01-conducta.md#c10--cada-mensaje-del-usuario-se-evalúa-como-posible-mejora-del-setup) | `SQLite`, `MariaDB`, `React`, `Django` y «este ERP» |
| [`01·C15`](../../../../../base/01-conducta.md#c15--al-replicar-un-patrón-replicar-la-paridad-completa) | «el módulo Aportes», de un proyecto real |
| [`01·C16`](../../../../../base/01-conducta.md#c16--re-lee-justo-antes-de-editar--nunca-sobre-contexto-viejo) | Las órdenes de lectura y edición del agente, y dos del control de versiones |
| [`04·S10`](../../../../../base/04-seguridad.md#s10--no-mates-procesos-globales--solo-pid-exacto-y-estrictamente-necesario) | `node` y `php` — **la cuarta, que ninguna lista tenía** |

**Por qué esto y no el capítulo más grande:** es el defecto que **daña a quien hereda**, no a quien escribe. Un proyecto que instalaba el estándar leía reglas redactadas para el stack de otro — no rompe nada, se lee, se entiende a medias y se aplica peor.

### Lo que se supo

- **`C10` no pasaba la pregunta que ella misma manda hacerse.** Es la regla que enseña a decidir si algo es transversal o local, y su criterio decía *«¿tendría sentido en un proyecto React + Django de otra empresa?»*.
- **`S10` se le pasó a la revisión por haber sido revisada.** Su sello **sí argumentó la fila 5** —para defender `killall`, `pkill` y `taskkill`— y al hacerlo la dio por buena; los dos intérpretes estaban tres líneas más arriba. **Un argumento sobre una fila no es una revisión de la fila.**
- **El detector callaba la mitad:** `node` no estaba en su lista, así que de los dos nombres de `S10` solo reportaba `php`. El sello y el programa miraban distinto y ninguno veía el conjunto.
- **Escribir en concepto cuesta.** `C10` pasó de 1724 a 1780 caracteres. Es el precio, y es por lo que el ejemplo con nombre propio de `03·D8` sobrevivió cuatro meses: se lee más fácil y convence más.

---

## 2. Qué se tocó

| Archivo | Qué |
|---|---|
| [`base/01-conducta.md`](../../../../../base/01-conducta.md) | Cuerpo y sello de `C10`, `C15`, `C16` |
| [`base/04-seguridad.md`](../../../../../base/04-seguridad.md) | Cuerpo y sello de `S10` |
| [`validadores/metareglas.py`](../../../../../validadores/metareglas.py) | `node`, `deno`, `bun`, `dotnet` y `softdeletes` al detector de la fila 5 |
| [`validadores/tests/test_la_base_no_nombra_stack.py`](../../../../../validadores/tests/test_la_base_no_nombra_stack.py) | 7 casos |
| [`pendientes/19-…`](../../../../../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md) | Lo que esta fase cierra. **Sigue abierto** |
| `CHANGELOG.md` · `VERSION` | 23.7.3 |

**Ninguna de las cuatro cambia lo que exige**, y el conteo de reglas en NO CUMPLE no se movió: **72 antes y 72 después**. Por eso es PARCHE.

---

## 3. Lo que se conserva a propósito

**`killall`, `pkill` y `taskkill` se quedan en `04·S10`.** No son producto ni framework: son cómo se llama la misma acción en cada sistema, y quitarlos deja la regla sin decir qué prohíbe. Ya estaba razonado el 2026-08-07 y sigue valiendo.

**Tienen su caso de prueba**, y ese caso es el que más pesa de los nueve: sin él, la próxima pasada los borra creyendo que mejora. Un criterio que solo vive en un sello se pierde; uno que vive en una prueba se defiende solo.

**`04·S11` sigue nombrando `SoftDeletes`**, también a propósito: su sello decidió que ahí el nombre del método **es el argumento** —suena a borrar y escribe—, así que reescribirlo es parte de partir la regla. Lo que cambió es que ahora **el programa lo dice**, en vez de callar. La prueba contra `base/` no exige cero: exige exactamente esa lista.

---

## 4. Lo que no hace

- **No arregla ninguna otra fila.** Las tres del `01` siguen en NO CUMPLE: `C10` tiene tres exigencias, `C15` y `C16` usan `Encadenamiento` fuera de las tres formas de `M7`, y `C16` duplica a `C2` por escrito.
- **No garantiza que no queden nombres.** La lista del detector se estrecha cada vez que aparece uno; hoy no hay forma de saber cuántos faltan. Lo que sí cambió: los que se conocen ya no dependen de que alguien los note leyendo.
