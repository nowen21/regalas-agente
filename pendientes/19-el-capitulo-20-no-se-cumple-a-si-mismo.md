# Pendiente · El capítulo de meta-reglas no se cumple a sí mismo

**Estado:** abierto, con una de sus tres deudas cerrada · anotado 2026-08-14 · nace del hallazgo H-6 de [2026-08-14](../historico-chat/resumenes/2026-08-14/hu-de-la-comprobacion-automatica.md).

| | |
|---|---|
| **Historia de usuario** | [EP-001 · HU-009 — Poner al día las reglas que no pasan su propio checklist](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/HU-009-reglas-sin-checklist-al-dia.md) — es exactamente lo que esa historia pide, ya medido |

## El problema

El validador de meta-reglas midió por primera vez el propio cuerpo de reglas. De **188 reglas**:

| Qué | Cuántas |
|---|---|
| Sin bloque de checklist | 129 |
| Publicadas con el checklist en "no cumple" | 7 |
| Sin clasificar en `reglas-validables.md` | 33 |

Las siete en "no cumple" son `F4`, `F5`, `F12`, `M2`, `M4`, `M7` y `M8`. `M14` dice que sin CUMPLE una regla no se publica, y están publicadas.

Las 33 sin clasificar incluyen los capítulos `18` y `19` completos, que ese archivo no menciona.

## Qué falta

**1. Decidir qué se hace con las siete.** Tres caminos: corregirlas, derogarlas, o aceptar que el checklist no aplica hacia atrás y dejarlo escrito.

**2. Clasificar las 33.** ✅ **Hecho el 2026-08-16** (v23.1.1), en la fase [`A-EP-001-HU-009`](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/A-EP-001-HU-009-clasificar-las-que-faltan/). Bajaron a cero.

**Y cambió el diagnóstico:** quince de las 33 **ya estaban clasificadas**. El registro decía `C1–C17`, un rango, y el programa busca cada identificador literal. Las que faltaban de verdad eran 18 — los capítulos `18` y `19` completos, más `G9`, `M15`, `F4` y `F12`.

**3. Las 121 sin bloque** (eran 129 cuando se anotó). Aplicarles el checklist es trabajo largo y con criterio. Conviene por capítulo, no de a una.

## El límite

El validador dice cuáles faltan, no si la regla está bien escrita. Eso lo decide quien la lee.

## La medición vuelve a ser posible — 2026-08-17

Este pendiente citaba una medición hecha con `metareglas.py` el 2026-08-14, y desde entonces **no se podía repetir**: el programa no tenía subcomando en `validar.py`. Al cerrar el [53](hecho/ningun-validador-termina-en-silencio.md) lo ganó.

```
$ python validadores/validar.py metareglas
7 falla(s), 229 aviso(s).
```

**Ese es el tamaño real de este pendiente, medido hoy y repetible.**

Y llegó con un defecto que hay que resolver acá, el `D-02`: **una regla nueva sin clasificar sale como `AVISO`, y un aviso no detiene la publicación**. El `CA-03` de esa historia pide que la detenga. La prueba que lo denunciaba estaba marcada como fallo esperado por dos motivos —el subcomando y el aviso—; el subcomando se arregló, así que ahora **pasa con la mitad hecha**. Se le escribió encima qué no comprueba, para que nadie la lea como que el `CA-03` está cubierto.

## Lo que le agrega el cierre del 52 — 2026-08-18

**Una cuarta deuda, medida hoy: 36 sellos vencidos de 73.** Un sello vencido dice que la regla, tal como está escrita hoy, pasó las veinte filas — y no es cierto. Es peor que no tener sello. Se cuentan con `validar.py metareglas`.

**Y una regla más en NO CUMPLE: `F13`, ahora son ocho.** No es que haya empeorado: decía «pendiente de aplicar», una forma que el validador no reconocía, así que figuraba como «no trae su bloque» —un aviso— cuando era una regla publicada sin sello válido. Se le aplicó el checklist y reprueba por **una sola fila, la 10**: el cuerpo mide 631 caracteres y el molde da 320. Su bloque deja escrito qué falla, para no volver a medirlo.

**Recortar `F13` es trabajo de este pendiente**, no del 52: es un cambio de regla y va con el repaso del capítulo `02`.

## Los dos primeros capítulos con su checklist aplicado — 2026-08-18

El punto 3 pedía hacerlo **por capítulo, no de a una**. Van dos, empezando por los más chicos.

| Capítulo | Reglas | CUMPLE | NO CUMPLE |
|---|---|---|---|
| `14` Estructura del código | 3 | `EST1`, `EST3` | `EST2` |
| `15` Registros inmutables | 5 | `IM1`, `IM4`, `IM5` | `IM2`, `IM3` |
| `11` Configuración y entornos | 4 | `CFG1`, `CFG2`, `CFG4` | `CFG3` |

**Se arreglaron dos en la misma pasada, porque eran redacción y no norma:**

- `EST3` reprobaba la fila 10 por **tres caracteres**. Se recortó el porqué.
- `IM2` reprobaba la fila 8 con el título «Estados y campos de anulación», que nombra un tema sin decir ninguna norma. Pasa a *Guarda los tres estados y la trazabilidad de quien anula*.
- `CFG4` reprobaba la fila 12 por no tener ejemplo, y el análisis del 2026-08-07 decía por qué hacía falta: *«la bandera eterna es error frecuente»*. Una regla que nombra un error frecuente no entra en la excepción de «evidente». Se le agregó el ejemplo de verdad.

**Las tres que quedan en NO CUMPLE necesitan partirse o mudar su procedimiento, y eso ya no es redacción:**

| Regla | Qué falla | Qué hay que hacer |
|---|---|---|
| `14·EST2` | Filas 8, 9 y 10 | **Son tres reglas en una**: una convención por tipo, nombres con significado por contexto, y los límites de longitud del motor. Dos IDs nuevos |
| `15·IM2` | Fila 9 | **Son dos**: los tres estados, y los campos de la anulación. Se pueden cumplir por separado |
| `15·IM3` | Fila 10 | **Un procedimiento de cuatro pasos no cabe en el molde de una regla.** El caso que la fila prevé: la regla se queda con la exigencia y el procedimiento se va a un anexo al lado |
| `11·CFG3` | Filas 9 y 12 | **Son tres**: que los entornos se parezcan, que lo que las pruebas no reproducen se cubra con verificación manual documentada, y que los cambios de producción se documenten en vez de aplicarse de memoria |

### Lo que se supo aplicando el checklist

**Hay un análisis del 2026-08-07 que ya había medido esto**, en [analisis/base-2026-08-07-cumplimiento-meta-reglas.md](../analisis/base-2026-08-07-cumplimiento-meta-reglas.md), regla por regla y con recomendación. Al sellar `IM2` se razonó sin mirarlo y casi queda en CUMPLE una regla que ese análisis ya había reprobado — por el mismo motivo, la fila 9.

**Antes de aplicarle el checklist a un capítulo, hay que leer ese análisis.** Aplicarlo sin mirarlo es rehacer el juicio con menos datos.

### La fila 10 estaba midiendo mal, y castigaba a las reglas que citan bien

`M5` da cuatro líneas —320 caracteres— y [`20·M15`](../base/20-meta-reglas/reglas/M15-toda-cita-a-otra-regla-lleva-su-enlace.md) exige que **toda** cita lleve su enlace. El conteo cobraba el marcado completo, así que cada enlace costaba unos cincuenta caracteres que nadie lee.

**Dos reglas del estándar tirando en direcciones contrarias, y perdía la que se cumplía.**

Medido antes de corregirlo: de las **108** reglas que se pasaban del límite, **27 se pasaban solo por eso**. `ID3` contaba 561 y son 265; `CFG1` contaba 359 y son 234.

Desde el 2026-08-18 se mide el cuerpo **leído**: `[texto](destino)` cuenta como `texto`. Las que se pasan bajan de 108 a **78**, y ninguna de las 30 rescatadas se tocó — no hacía falta.

**No relaja la fila.** La regla que de verdad no cabe sigue sin caber, y hay una prueba que lo fija.

**Esto cambia el trabajo que queda:** treinta reglas que parecían necesitar reescritura no la necesitan. Conviene volver a mirar cualquier lista de «reglas largas» hecha antes de esta fecha, incluido el análisis del 2026-08-07.

### Cómo va la cuenta

| | Al anotarse | Antes de hoy | Hoy |
|---|---|---|---|
| Sin bloque de checklist | 129 | 121 | **108** |
| Publicadas en NO CUMPLE | 7 | 7 | **12** |
| Que se pasan del molde (fila 10) | — | 108 | **78** |

Trece reglas ganaron su sello hoy: las tres del `14`, las cinco del `15`, las cuatro del `11` y `F13`. Cinco de esas trece dicen NO CUMPLE.

**Las publicadas en NO CUMPLE suben, y es lo esperado.** No es que hayan empeorado: es que antes no tenían bloque y ahora dicen la verdad. El número que baja —las que no tienen sello— es el que mide el avance.
