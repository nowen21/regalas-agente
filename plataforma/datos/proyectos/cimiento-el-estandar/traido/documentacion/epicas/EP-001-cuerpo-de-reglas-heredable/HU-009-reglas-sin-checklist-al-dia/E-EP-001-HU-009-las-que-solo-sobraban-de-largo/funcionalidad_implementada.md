# Funcionalidad implementada — Fase «E-EP-001-HU-009-las-que-solo-sobraban-de-largo»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito **qué quedó hecho**, para que quien llegue después no tenga que deducirlo del código ni del historial.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `E-EP-001-HU-009-las-que-solo-sobraban-de-largo` |
| **Épica / HU** | [EP-001](../../epica.md) · [HU-009](../HU-009-reglas-sin-checklist-al-dia.md) |
| **Versión del estándar** | 23.7.4 → **23.7.5** (PARCHE) |
| **Fecha de cierre** | 2026-08-18 |

---

## 1. Qué quedó funcionando

**Diez reglas cuyo único defecto era el largo pasan a CUMPLE, sin que cambie una sola exigencia.** Las reglas en NO CUMPLE bajan de **70 a 60**.

| Regla | Antes | Después |
|---|---:|---:|
| `01·C13` | 802 | **306** |
| `09·G9` | 552 | **319** |
| `01·C19` | 533 | **317** |
| `01·C12` | 462 | **269** |
| `01·C11` | 461 | **278** |
| `04·S1` | 437 | **311** |
| `09·G7` | 421 | **270** |
| `17·I1` | 395 | **293** |
| `03·D3` | 378 | **306** |
| `04·S2` | 349 | **295** |

**El corte es lo que hizo la fase posible.** De las 70 que reprueban, quince fallan **solo** la fila 10, y diez de esas son puro exceso de explicación: no hay que partirlas, ni derogarlas, ni decidir nada. **Es el único trabajo grande del pendiente 19 que no depende de una decisión del usuario.**

---

## 2. Lo que sobra casi siempre es el porqué, y la regla ya lo decía

En **ocho de las diez** lo que se fue era razonamiento: por qué sobre-verificar molesta, por qué el formulario cerrado empobrece la respuesta, por qué lo que no se versiona se pierde. [`20·M5`](../../../../../base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md) lo dice en la propia fila 10 —*si no cabe, o son dos reglas o se está contando el porqué, que va a `notas/`*— y **el diagnóstico acertó ocho de diez veces**.

**Las otras dos eran ejemplos metidos en el cuerpo**, y su sitio ya existía: el bloque INCORRECTO/CORRECTO, **que no cuenta para la fila 10**. `01·C12` llevaba tres ejemplos de adjetivo en el cuerpo teniendo su bloque justo debajo.

### El bloque de ejemplo era espacio gratis y nadie lo usaba

La fila 10 mide **solo el cuerpo**. Un ejemplo largo no cuesta nada; una enumeración en el cuerpo cuesta todo. Y aun así las reglas más largas tenían ejemplos cortos: **la forma de acortar sin perder nada estaba disponible desde el principio.**

---

## 3. La medición es el trabajo, no el trámite

**La primera reescritura dejó cinco de las diez todavía pasadas**, y `09·G9` necesitó **tres pasadas**. Escribir corto no sale a la primera.

Por eso la medición fue paso de la ruta crítica y no un control final: **un sello firmado sobre un largo estimado hereda el error de quien estimó**, y ya había pasado en esta misma historia — cinco sellos citaron números que nadie remidió después de corregir cómo se mide.

---

## 4. Qué se tocó

| Archivo | Qué |
|---|---|
| [`base/01-conducta.md`](../../../../../base/01-conducta.md) | `C11`, `C12`, `C13`, `C19` |
| [`base/03-datos.md`](../../../../../base/03-datos.md) | `D3` |
| [`base/04-seguridad.md`](../../../../../base/04-seguridad.md) | `S1`, `S2` |
| [`base/09-git.md`](../../../../../base/09-git.md) | `G7`, `G9` |
| [`base/17-interfaz.md`](../../../../../base/17-interfaz.md) | `I1` |
| [`pendientes/19-…`](../../../../../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md) | Lo que esta fase cierra. **Sigue abierto** |
| `CHANGELOG.md` · `VERSION` | 23.7.5 |

**Ninguna exigencia se fue con el texto**, y se comprobó punto por punto: los tres de `D3`, los tres de `S1`, los cuatro de `S2`, los tres estados de `I1`, los tres criterios de `C13`.

**Ninguna excepción se tocó.** Es lo único de una regla que no se puede resumir sin cambiar qué permite: la de `G9` conserva condición y límite, y la de `C11` quedó entera.

**Cada sello dice de cuánto a cuánto y qué texto salió** — quien lea dentro de un año necesita saber si lo que falta se perdió o se movió.

---

## 5. Lo que no hace

**Cinco de las quince no se tocaron, y por motivos distintos:**

| Regla | Por qué |
|---|---|
| `03·D8` · `04·S9` · `04·S10` | Lo que sobra es **un procedimiento**, no una explicación: el caso de anexo |
| `05·E4` | Su sello ya decidió que la escala de cuatro niveles se va a un anexo |
| `02·F13` | Se reescribió hace días |

**Y `04·S9` tiene un motivo propio:** es **el único modelo de excepción completa del cuerpo** —condición, límite y autorizador—, y acortarla de paso, entre otras nueve, es la forma de perderlo.

**El porqué que se sacó no se escribió en `notas/`.** No se perdió —está en los sellos, que dicen qué salió de cada regla— pero tampoco está donde `M5` manda. Son diez notas cortas, y quedan anotadas en el 19.
