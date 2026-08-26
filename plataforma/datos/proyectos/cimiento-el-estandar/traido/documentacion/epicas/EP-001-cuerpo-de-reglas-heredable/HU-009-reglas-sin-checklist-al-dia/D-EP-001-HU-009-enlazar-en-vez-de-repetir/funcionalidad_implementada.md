# Funcionalidad implementada — Fase «D-EP-001-HU-009-enlazar-en-vez-de-repetir»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito **qué quedó hecho**, para que quien llegue después no tenga que deducirlo del código ni del historial.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `D-EP-001-HU-009-enlazar-en-vez-de-repetir` |
| **Épica / HU** | [EP-001](../../epica.md) · [HU-009](../HU-009-reglas-sin-checklist-al-dia.md) |
| **Versión del estándar** | 23.7.3 → **23.7.4** (PARCHE) |
| **Fecha de cierre** | 2026-08-18 |

---

## 1. Qué quedó funcionando

**Dos reglas que enlazaban a su vecina *y además* la copiaban se quedaron solo con lo suyo**, y pasaron de NO CUMPLE a CUMPLE.

| Regla | Se fue | Quedó |
|---|---|---|
| [`07·Q7`](../../../../../base/07-calidad-de-codigo.md#q7--deja-el-código-mejor-pero-en-tu-alcance) | el criterio de alcance, que es [`01·C3`](../../../../../base/01-conducta.md#c3--quédate-en-tu-tarea) | `C3` como **motivo enlazado**, y decirlo para su tarea |
| [`12·PR4`](../../../../../base/12-privacidad-datos.md#pr4--no-los-expongas-en-logs-errores-ni-mensajes) | lo de logs, que es [`05·E5`](../../../../../base/05-errores-y-logging.md#e5--nunca-registres-secretos-ni-datos-sensibles) | pantallas, reportes y mensajes a terceros |

**Ninguna exigencia desapareció del cuerpo:** lo que se fue de cada regla sigue rigiendo por la vecina que ya lo decía. El conteo de reglas en NO CUMPLE bajó **exactamente dos** — 72 a 70 —, que es la red contra el cambio no declarado.

---

## 2. Por qué el defecto duraba: se leía como diligencia

**Las dos enlazaban a la vecina.** El enlace estaba puesto, visible y correcto — y aun así reprobaban, porque **la fila 11 no pide enlazar: pide enlazar *en vez de* copiar**. Un enlace delante de un texto repetido se lee como cuidado, no como duplicación.

Sobrevivieron a varias lecturas porque **cumplían la mitad que se ve.**

---

## 3. El modelo estaba en el propio cuerpo

[`14·EST3`](../../../../../base/14-estructura-codigo.md#est3--respeta-el-legacy--la-convención-es-para-lo-nuevo) toma de `01·C3` **el mismo criterio de alcance** que `Q7`, y estaba en CUMPLE. La diferencia era la forma: `EST3` nombra a `C3` entre paréntesis como el **motivo** y todo lo demás es suyo; `Q7` reformulaba el criterio entero antes de enlazarlo.

**La respuesta a cómo se escribe esta regla ya estaba escrita, en otra regla del mismo cuerpo.** El análisis del 2026-08-07 las había nombrado juntas; lo que faltaba era usar una de molde para la otra.

---

## 4. Tres capas del mismo criterio, y solo una aportaba

`00·N6` (blindada) → `05·E5` → `12·PR4`, cada una reformulando a la anterior. Al separarlas, **la única parte que no dice ninguna otra regla es la mitad de pantallas y reportes de `PR4`**: `E5` habla de logs.

Es lo que la salvó de derogarse, y es la clase de cosa que solo aparece leyendo las tres seguidas.

**Y su ejemplo se quedaba ilustrando lo que la regla dejó de decir** — era de logs. Un ejemplo así es peor que ninguno, porque manda a buscar la exigencia donde ya no está. Se cambió con ella.

---

## 5. Qué se tocó

| Archivo | Qué |
|---|---|
| [`base/07-calidad-de-codigo.md`](../../../../../base/07-calidad-de-codigo.md) | Cuerpo y sello de `Q7` — 211 a 191 caracteres |
| [`base/12-privacidad-datos.md`](../../../../../base/12-privacidad-datos.md) | Cuerpo, ejemplo y sello de `PR4` — 242 a 220, y `depende de 05·E5` declarado |
| [`pendientes/19-…`](../../../../../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md) | Lo que esta fase cierra. **Sigue abierto** |
| `CHANGELOG.md` · `VERSION` | 23.7.4 |

**En `PR4` lo que importa no es que acorte** —22 caracteres— **sino que lo que queda es suyo**.

---

## 6. Lo que no hace

**La categoría queda a medias, y está dicho.** Siguen repitiendo al vecino `12·PR3` —que no exige nada propio y hay que decidir si se queda con algo o se deroga—, `01·C16` —cuyo arreglo pasa por normalizar el bloque `Encadenamiento` en cuatro reglas a la vez— y `04·S7`, cuyos dos sellos prescriben **derogarla**.

**Las tres tienen algo en común: no son un cambio de redacción.** Dos piden una decisión sobre si una regla deja de existir, y derogar obliga a adoptarlo ([`02·F22`](../../../../../base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md)) en todos los proyectos.
