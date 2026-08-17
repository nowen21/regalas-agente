# Pendiente · El sello del checklist caduca con el texto y nada lo comprueba

**Estado:** abierto · anotado 2026-08-16.

| | |
|---|---|
| **De dónde sale** | El **punto 7** del [33](33-defectos-que-destaparon-los-resumenes-viejos.md), promovido a pendiente propio el 2026-08-16 |
| **Historia que lo recibiría** | [EP-001 · HU-009](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/HU-009-reglas-sin-checklist-al-dia.md), o una nueva de EP-004 si se construye el programa |
| **Se cruza con** | El [19](19-el-capitulo-20-no-se-cumple-a-si-mismo.md), que cuenta las reglas sin checklist; este cuenta las que lo tienen **vencido** |

## El problema

Cada bloque de checklist cierra con esta frase:

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

**La frase lo dice y nada lo comprueba.** Una regla puede editarse y seguir mostrando un CUMPLE que se aplicó contra otro texto, otra versión y otro día. Quien la lee ve un sello y confía.

## El caso concreto

Al reescribir [`02·F13`](../base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md) el **2026-08-08**, su bloque de checklist quedó anulado y se dejó anotado «a re-aplicar en el próximo repaso». **No se hizo**, y hoy la regla figura en el capítulo `02` con el resultado *pendiente*.

Ocho días después nadie lo había vuelto a mirar. No es descuido de una persona: es que **nada lo recuerda**.

→ Sale de [la instalación se hace sola · H-3](../historico-chat/resumenes/2026-08-08/la-instalacion-se-hace-sola.md).

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

La comprobación dice que el sello **caducó**, no que la regla esté mal escrita. Volver a aplicarle las veinte filas es trabajo con criterio, y es el mismo de las 121 reglas sin bloque del [19](19-el-capitulo-20-no-se-cumple-a-si-mismo.md): conviene hacerlo por capítulo.

## Cómo se sabrá que cerró

Se edita el texto de una regla que tenga su sello en CUMPLE, se corre la comprobación y el sello sale reportado como vencido. Y `F13` tiene su checklist aplicado otra vez.
