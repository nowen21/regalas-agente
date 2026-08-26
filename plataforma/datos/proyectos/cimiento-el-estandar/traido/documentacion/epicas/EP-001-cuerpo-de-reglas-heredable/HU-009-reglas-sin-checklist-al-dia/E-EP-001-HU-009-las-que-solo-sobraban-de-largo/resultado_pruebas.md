# Resultado de Pruebas — Fase E-EP-001-HU-009: las que solo sobraban de largo

| Campo | Valor |
|---|---|
| **Plan de pruebas** | [PP-E-EP-001-HU-009](plan_pruebas.md) v1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-18 |

---

## 1. Casos ejecutados

| Caso | Veredicto | Qué dio |
|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--las-diez-caben-medidas-no-estimadas) | ✅ **Pasa** | Las diez ≤ 320, medidas |
| [CP-002](plan_pruebas.md#cp-002--las-diez-pasan-a-cumple) | ✅ **Pasa** | Ninguna en NO CUMPLE |
| [CP-003](plan_pruebas.md#cp-003--cada-exigencia-del-texto-viejo-sigue-en-el-nuevo) | ✅ **Pasa** | Ver §3 |
| [CP-004](plan_pruebas.md#cp-004--las-excepciones-no-se-tocaron) | ✅ **Pasa** | `G9` conserva condición y límite |
| [CP-005](plan_pruebas.md#cp-005--cada-sello-dice-qué-se-fue) | ✅ **Pasa** | Los diez dicen de cuánto a cuánto y qué salió |
| [CP-006](plan_pruebas.md#cp-006--el-conteo-baja-exactamente-diez) | ✅ **Pasa** | **70 → 60** |
| [CP-007](plan_pruebas.md#cp-007--nada-de-lo-que-ya-estaba-deja-de-pasar) | ✅ **Pasa** | Ver §2 |

**7 de 7 ejecutados. 7 pasan.**

---

## 2. CP-007 · No regresión

| Qué se corrió | Resultado |
|---|---|
| `validadores/tests/` | **154 · OK** |
| `validadores/pruebas.py` | **357 · OK** (5 fallos esperados, los de siempre) |
| `validar.py estandar` | **Sin incumplimientos** |
| Reglas en NO CUMPLE | **70 → 60** |

---

## 3. Lo que se fue de cada una

| Regla | Antes | Después | Qué salió |
|---|---:|---:|---|
| `01·C11` | 461 | **278** | El porqué: que sobre-verificar rompe el flujo y trata al usuario como si mintiera |
| `01·C12` | 462 | **269** | Los tres ejemplos de adjetivo, que ya están en el bloque INCORRECTO/CORRECTO |
| `01·C13` | 802 | **306** | El porqué del formulario cerrado y el detalle del formato de la pregunta |
| `01·C19` | 533 | **317** | El porqué: que lo no versionado no se revisa, no viaja y se pierde al clonar |
| `03·D3` | 378 | **306** | Nada: se apretó la redacción de los tres puntos |
| `04·S1` | 437 | **311** | Los paréntesis que enumeraban dónde comprobar y qué cuenta como registro propio |
| `04·S2` | 349 | **295** | La enumeración de qué es «dato de afuera» y los nombres de los ataques |
| `09·G7` | 421 | **270** | Los nombres de las órdenes del control de versiones |
| `09·G9` | 552 | **319** | Redacción, y una cita que no aportaba exigencia |
| `17·I1` | 395 | **293** | La explicación de cuándo ocurre cada estado |

**Ninguna exigencia se fue con el texto**, y se comprobó punto por punto: los tres de `D3`, los tres de `S1`, los cuatro de `S2`, los tres estados de `I1`, los tres criterios de `C13`.

**Y ninguna excepción se tocó.** La de `G9` conserva su condición y su límite; la de `C11` —verificar ante duda real— quedó entera.

---

## 4. Lo que se supo ejecutando

### La medición es el trabajo, no el trámite

**La primera reescritura dejó cinco de las diez todavía pasadas**, y `G9` necesitó **tres pasadas** para caber. Escribir corto no sale a la primera.

Es la razón de que el plan pusiera la medición en la ruta crítica: un sello firmado sobre un largo estimado hereda el error de quien estimó, **y ya había pasado en esta misma historia** — cinco sellos citaron números que nadie remidió después de corregir cómo se mide.

### Lo que sobra casi siempre es el porqué, y la regla ya lo decía

En ocho de las diez, lo que se fue era **razonamiento**: por qué sobre-verificar molesta, por qué el formulario cerrado empobrece la respuesta, por qué lo que no se versiona se pierde. [`20·M5`](../../../../../base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md) lo dice en la propia fila 10 — *si no cabe, o son dos reglas o se está contando el porqué, que va a `notas/`* — y el diagnóstico acertó ocho de diez veces.

**Las otras dos eran ejemplos dentro del cuerpo**, y su sitio ya existía: el bloque INCORRECTO/CORRECTO, **que no cuenta para la fila 10**. `C12` tenía tres ejemplos de adjetivo en el cuerpo teniendo su bloque debajo.

### El bloque de ejemplo es espacio gratis, y nadie lo estaba usando

La fila 10 mide **solo el cuerpo**. Un ejemplo largo no cuesta nada y una enumeración en el cuerpo cuesta todo — y aun así las reglas largas del cuerpo tenían ejemplos cortos. **La forma de acortar sin perder nada estaba disponible desde el principio.**

### Diez de las quince, y el corte importa

De las quince que reprueban solo la fila 10, **cinco no son de redacción**: `03·D8`, `04·S9` y `04·S10` tienen dentro un **procedimiento** —el caso de anexo—, `05·E4` ya tiene decidido que su escala se va a un anexo, y `02·F13` se reescribió hace días.

**`04·S9` tiene además un motivo propio:** es **el único modelo de excepción completa del cuerpo** —condición, límite y autorizador—, y acortarla de paso entre otras nueve es la forma de perderlo.

---

## 5. Lo que queda abierto  ·  [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)

**El porqué que se sacó no se escribió en `notas/`.** `M5` dice que ahí va, y esta fase lo quitó del cuerpo sin ponerlo en ningún lado. **No se perdió** —está en el historial y en los sellos, que dicen qué salió de cada una— pero tampoco está donde debería.

Son diez notas cortas, y es trabajo de una sesión. Queda anotado en el [19](../../../../../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md).

---

## 6. Veredicto

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | el `CA-01` en la fila 10, para las diez de redacción |
| **CA en «No»** | ninguno |
| **Defectos abiertos aceptados** | dos: las cinco de anexo, y las notas del porqué sin escribir |
| **Ciclos** | 1 |
