# Pendiente · La norma de redacción del estándar vive dentro de dos plantillas, no en `base/`

**Estado:** **hecho** el 2026-08-30, en la misma sesión que lo anotó.

| | |
|---|---|
| **Historia de usuario** | [EP-001 · HU-037](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-037-la-norma-de-redaccion-del-agente/HU-037-la-norma-de-redaccion-del-agente.md), aprobada el 2026-08-30 |
| **De dónde sale** | El hallazgo `H-2` de la sesión [2026-08-28 · plantilla-manual-instalacion](../historico-chat/resumenes/2026-08-28/plantilla-manual-instalacion.md) |
| **Proyecto de origen** | El estándar mismo |

## El problema

El usuario pidió que un documento se redactara en español colombiano, en tercera persona y en infinitivo. **No hubo regla de `base/` que citar.**

Esa exigencia solo está escrita en el cuerpo de dos plantillas, como su regla 11: [`plantillas/manual-usuario.md`](../plantillas/manual-usuario.md) y [`plantillas/manual-instalacion.md`](../plantillas/manual-instalacion.md). Dice, palabra por palabra:

> **Acciones en infinitivo, explicaciones en tercera persona.** Nada de «usted», «tú» ni imperativos. [...] El impersonal con «se» no sirve para las acciones.

Es una norma de cómo escribe el agente, y está guardada como si fuera un detalle de esos dos documentos.

**El estándar ya sabe que le falta.** El anexo [`marcadores-de-ia.md`](../base/00-identidad-y-rol/marcadores-de-ia.md) lo dice en su cierre, en «Lo que este anexo no cubre»:

> La **norma del español**: ortografía, gramática, sintaxis y variedad del país. [...] Exigir norma correcta y variedad colombiana necesita su propia regla, y todavía no existe.

## Por qué importa

[`00·ID8`](../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) rige todo documento que el agente entrega, pero solo cubre las marcas de generación automática: quita adorno. **Cómo se redacta queda a criterio de cada documento**, y un documento que no sea manual de usuario ni manual de instalación no tiene de dónde heredar la norma.

El costo se paga cada vez: la convención se aplica copiándola a mano de una plantilla, y lo que se copia a mano se copia distinto.

## Qué falta

Una regla de `base/`, por el procedimiento del [capítulo 20](../base/20-meta-reglas/base.md), que fije tres cosas separadas:

1. **La variedad del idioma**, que sale del proyecto y no se fija en «colombiano» a la fuerza: `01·C8` ya dice que se habla el idioma del proyecto, y esta la concreta.
2. **La persona**: tercera, con sujeto, para lo que se explica.
3. **La forma verbal**: infinitivo para lo que el lector hace, y el impersonal con «se» descartado para las acciones.

**La decisión que hay que tomar antes de escribirla:** si rige para **todo** documento que el agente entrega, o solo para los que lee alguien que no es del oficio. Un mensaje de commit y una regla del estándar no se escriben en infinitivo, así que el alcance no es obvio y no lo decide quien la redacta.

Al cerrarla, las dos plantillas dejan de llevar la regla en el cuerpo y la citan.

## El límite

Esto **no** es ortografía ni gramática. El anexo nombra las dos como pendientes suyas, y son otra regla: una cosa es cómo se conjuga y otra si el texto está bien escrito.

Tampoco cubre el registro del texto que ve el usuario final de un producto, que ya gobierna `17·I4`.

## Cómo se sabrá que cerró

Que exista la regla en `base/` con su identificador, que las dos plantillas la citen en vez de repetirla, y que `python validadores/validar.py metareglas` siga en verde con la regla nueva clasificada en [`validadores/reglas-validables.md`](../validadores/reglas-validables.md).
