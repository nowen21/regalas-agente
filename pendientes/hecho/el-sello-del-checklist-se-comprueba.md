# Pendiente · El sello del checklist caduca con el texto y nada lo comprueba

**Estado:** **cerrado** el 2026-08-18. Anotado el 2026-08-16.

| | |
|---|---|
| **Historia de usuario** | [EP-001 · HU-009 — Poner al día las reglas que no pasan su propio checklist](../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/HU-009-reglas-sin-checklist-al-dia.md) — el sello vencido es la otra cara del 19: aquel cuenta las que no lo tienen, este las que lo tienen viejo |
| **De dónde sale** | El **punto 7** del [33](lo-que-quedo-abierto-en-las-sesiones-viejas.md), promovido a pendiente propio el 2026-08-16 |
| **Historia que lo recibiría** | [EP-001 · HU-009](../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/HU-009-reglas-sin-checklist-al-dia.md), o una nueva de EP-004 si se construye el programa |
| **Se cruza con** | El [19](ninguna-regla-reprueba-su-propio-checklist.md), que cuenta las reglas sin checklist; este cuenta las que lo tienen **vencido** |

## El problema

Cada bloque de checklist cierra con esta frase:

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

**La frase lo dice y nada lo comprueba.** Una regla puede editarse y seguir mostrando un CUMPLE que se aplicó contra otro texto, otra versión y otro día. Quien la lee ve un sello y confía.

## El caso concreto

Al reescribir [`02·F13`](../../base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md) el **2026-08-08**, su bloque de checklist quedó anulado y se dejó anotado «a re-aplicar en el próximo repaso». **No se hizo**, y hoy la regla figura en el capítulo `02` con el resultado *pendiente*.

Ocho días después nadie lo había vuelto a mirar. No es descuido de una persona: es que **nada lo recuerda**.

→ Sale de [la instalación se hace sola · H-3](../../historico-chat/resumenes/2026-08-08/la-instalacion-se-hace-sola.md).

## Por qué es `P1`

Un sello vencido **afirma algo que no es cierto**: dice que esa regla, tal como está escrita hoy, pasó las veinte filas. Es exactamente lo que la prioridad `P1` define — un documento del estándar diciendo algo falso — y además es peor que no tener sello, porque el que no lo tiene al menos no engaña.

## Las dos salidas

| Salida | Qué cuesta | Qué deja |
|---|---|---|
| **A · Huella del texto dentro del sello.** El bloque guarda una marca corta calculada del texto de la regla; el validador la recalcula y avisa si no coincide | **Cara.** Cambia el molde del sello y hay que recalcular la marca de las ~60 reglas que ya lo tienen. Es MAYOR | Detección exacta: cualquier cambio del texto vence el sello |
| **B · La fecha del sello contra la fecha del archivo.** El sello ya dice contra qué versión y **en qué fecha** se aplicó; si el archivo se modificó después, el sello está vencido | **Barata.** No cambia ningún molde ni ningún sello existente | Detección aproximada: un cambio de una coma también vence el sello, y un cambio sin commit no se ve |

**Recomendada la B para empezar**, y no por ahorrar: la A obliga a tocar sesenta reglas que hoy están bien, y eso es mucho riesgo para un problema que la B ya hace visible. Si la B produce demasiado ruido, la A queda como el paso siguiente con datos en la mano.

## Qué falta

1. **Decidir entre A y B.**
2. Construir la comprobación en `metareglas.py`, que ya es el dueño de este tema.
3. **Re-aplicar el checklist de `F13`**, que es el caso que lo destapó y sigue pendiente.
4. Correr la comprobación sobre `base/` y ver cuántos sellos más están vencidos. **El número no se sabe hoy**, y esa es media gracia del pendiente.

## El límite

La comprobación dice que el sello **caducó**, no que la regla esté mal escrita. Volver a aplicarle las veinte filas es trabajo con criterio, y es el mismo de las 121 reglas sin bloque del [19](ninguna-regla-reprueba-su-propio-checklist.md): conviene hacerlo por capítulo.

## Cómo se sabrá que cerró

Se edita el texto de una regla que tenga su sello en CUMPLE, se corre la comprobación y el sello sale reportado como vencido. Y `F13` tiene su checklist aplicado otra vez.

---

# Cómo cerró — 2026-08-18

**Los cuatro puntos.**

## 1 · Se eligió la B

La fecha del sello contra la del último cambio, como recomendaba el propio pendiente. La A —una huella del texto— detecta el cambio exacto, pero obliga a recalcular el sello de **73 reglas que hoy están bien**: mucho riesgo para hacer visible algo que la fecha ya hace visible. Si esto produce demasiado ruido, la A queda como el paso siguiente, ya con datos en la mano.

Su precio está asumido y escrito en el código: un cambio de una coma también vence el sello, y un cambio sin confirmar no se ve.

**La fecha sale del control de versiones, no del disco.** La del sistema de archivos cambia con un `clone`, con un `checkout` y hasta con un antivirus: compararla daría vencidos falsos en cada máquina nueva. Y sin dato **no se inventa un vencimiento** — un hallazgo falso acá enseña a ignorar todos los demás.

## 2 · La comprobación está en `metareglas.py`

`_sello_vencido()`, en el programa que ya era dueño del tema, y sale como **AVISO**. Que un sello caducó no es que la regla esté mal escrita: es que hay que volver a mirarla. Treinta y seis fallas de golpe volverían la corrida inservible, y una corrida inservible se deja de correr.

**Una corrida que estorba tampoco se corre.** La primera versión preguntaba al control de versiones una vez por regla —doscientas invocaciones— y la corrida pasó de segundos a minutos. Se hace en **una sola pasada**: 2,6 segundos.

## 3 · `F13` tiene su checklist aplicado

Y el resultado es **NO CUMPLE**, por una sola fila: la **10**, el cuerpo de 1 a 4 líneas. Mide **631 caracteres** y el molde da 320.

Las otras diecinueve pasan —16 ✅ y 3 N/A—. La fila que reprueba dice qué hacer cuando no cabe: o son dos reglas, o se está contando el porqué y ese va a `notas/`. Acá es lo segundo.

**Recortarla es un cambio de regla y no se hizo acá**: va al [19](ninguna-regla-reprueba-su-propio-checklist.md), que es el que trabaja por capítulo las reglas que no pasan su checklist. El bloque deja escrito **qué** falla, para que quien lo tome no vuelva a medirlo.

**Estaba peor de lo que se creía.** `F13` decía «pendiente de aplicar», y esa forma no la reconocía el validador: figuraba como *«no trae su bloque de checklist»*, un aviso, cuando en realidad era una regla publicada sin sello válido. Ahora dice NO CUMPLE y sale como falla — que es la verdad.

De paso: [validadores/reglas-validables.md](../../validadores/reglas-validables.md) registraba `F13` con el **título viejo**, de cuando detenía el arranque. Corregido.

## 4 · El número que nadie sabía

**36 sellos vencidos**, de 73 reglas selladas. Casi la mitad.

| | |
|---|---|
| Reglas con sello y fecha | 73 |
| **Con el sello vencido** | **36** |
| Publicadas en NO CUMPLE | 8 — eran 7, y `F13` es el octavo por decir la verdad |

Ese conteo es lo que el pendiente decía que «no se sabe hoy, y esa es media gracia». Ahora se puede repetir con una línea: `python validadores/validar.py metareglas`.

## Cómo quedó comprobado

[validadores/tests/test_sello_del_checklist_vencido.py](../../validadores/tests/test_sello_del_checklist_vencido.py), 9 casos, sobre repositorios de verdad con fechas de confirmación puestas a mano. Entre ellos los tres que evitan el ruido: sellar y editar el mismo día no vence, un sello sin fecha no se inventa nada, y un archivo fuera del control de versiones no se reporta. Y uno que fija el criterio: **tocar el archivo en el disco no vence el sello**.

## El límite sigue en pie

La comprobación dice que el sello **caducó**, no que la regla esté mal escrita. Volver a aplicarle las veinte filas a las 36 es trabajo con criterio, y es el mismo del [19](ninguna-regla-reprueba-su-propio-checklist.md): conviene hacerlo por capítulo.
