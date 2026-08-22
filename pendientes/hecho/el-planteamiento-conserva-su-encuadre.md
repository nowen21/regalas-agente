# Pendiente · Un planteamiento llenado puede pisar su encuadre y nadie lo nota

**Estado:** cerrado el 2026-08-22, en la fase [`B-EP-004-HU-004`](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-004-forma-de-los-documentos/B-EP-004-HU-004-el-encuadre-de-la-plantilla-sobrevive-al-llenado/funcionalidad_implementada.md) (v31.12.0) · anotado ese mismo día.

| | |
|---|---|
| **Historia de usuario** | [EP-004 · HU-004 — Forma de los documentos](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-004-forma-de-los-documentos/HU-004-forma-de-los-documentos.md). Va ahí y no en EP-003 porque lo que falta es el programa que comprueba, no el molde: el molde lo arregla la [fase C de HU-002](../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-002-modelos-del-encargo/C-EP-003-HU-002-el-planteamiento-se-reconstruye-igual/plan_trabajo.md) |
| **De dónde sale** | Hallazgo H-2 del resumen [2026-08-22 · sesión 2](../../historico-chat/resumenes/2026-08-22/sesion-2.md) |
| **Proyecto de origen** | El estándar mismo |

## El problema

El molde [`plantillas/ciclo-vida-proyectos/01-planteamiento.md`](../../plantillas/ciclo-vida-proyectos/01-planteamiento.md) trae un recuadro de instrucciones que manda borrarse al llenar, y debajo un renglón de encuadre que queda fuera de ese recuadro. Ese renglón es lo que le dice al agente que el documento es insumo y no orden, y que no hay código hasta que el plan esté aprobado.

Nada impide reemplazarlo. Ya pasó: [`prompts/cimiento-planteamiento.md`](../../prompts/cimiento-planteamiento.md) se escribió con una nota de procedencia en ese lugar, con fecha, fuentes y el número del pendiente que cerraba, y el encuadre desapareció. Estuvo así hasta que el usuario preguntó qué aportaba ese párrafo.

Ningún validador lo mira. `validar.py` comprueba enlaces, citas, fases, trazabilidad, versionado, marcas y expediente, y ninguno de esos abre un `*-planteamiento.md` para ver si conserva su encuadre.

## Por qué importa

No bloquea nada hoy, y ese es el problema: falla en silencio. Un planteamiento sin encuadre llega igual al agente, se lee igual, y lo único que cambia es que se le quitó el freno que impide leerlo como orden de entregar código. El daño aparece después, cuando alguien escribe código sin plan aprobado y nadie sabe por qué.

Y viaja. El molde se copia a cada proyecto que instala el estándar, así que el hueco es el mismo en todos.

## Qué falta

Un validador que abra los `*-planteamiento.md` del proyecto y compruebe que el encuadre está, con su texto.

Dos salidas:

1. **Comparar contra el texto del molde.** Barato de escribir. Se rompe cada vez que el molde cambia una coma, y entonces reprueba lo que está bien, que es justo el caso borde que el planteamiento de Cimiento nombra en §8.
2. **Comprobar que estén las dos frases que importan**, la que dice que el documento es insumo y la que dice que no hay código sin plan aprobado, sin exigir literalidad. Más trabajo, sobrevive a la redacción.

Conviene la segunda. El costo de la primera se paga entero la primera vez que alguien corrige el molde.

## El límite

No cubre el resto de los moldes del ciclo. Si el problema resulta general, sale de acá como otro pendiente.

No cubre que el encuadre sea el correcto: solo que esté. Que diga lo que debe decir lo fija la [fase C de HU-002](../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-002-modelos-del-encargo/C-EP-003-HU-002-el-planteamiento-se-reconstruye-igual/plan_trabajo.md), y este pendiente se construye después de ella.

## Cómo se sabrá que cerró

Se toma un `*-planteamiento.md` llenado, se le borra el renglón del encuadre, se corre el validador y reprueba nombrando el archivo. Se repone el renglón y aprueba.

---

## Cómo se cerró — 2026-08-22

**Se tomó la segunda salida**, la de comprobar sin exigir literalidad, y por el motivo que este pendiente ya preveía: comparar contra el texto del molde reprueba lo que está bien la primera vez que alguien corrige una coma.

**Pero el criterio que se propuso acá no sirvió, y se supo midiendo.** La idea era pedir que el encuadre citara alguna regla. Reprobó [`planteamiento.md`](../../planteamiento.md), que dice exactamente lo que debe decir pero deletrea la cadena en palabras. Se probó entonces el solapamiento de vocabulario con el molde: 31%, 17% y 11% en los tres casos reales, o sea que no separa nada. El criterio que quedó es otro: **falla si el texto fijo trae una fecha que la plantilla no tiene ahí**, porque una fecha en ese lugar es procedencia, y la procedencia va en la identificación. Cero falsos positivos en 651 documentos.

**Y encontró algo antes de estrenarse:** el molde manda nombrar el archivo `prompts/<slug>-planteamiento.md` y el validador solo reconocía el nombre pelado, así que la comprobación no alcanzaba a ninguno de los documentos que el molde produce. Corregido en la [fase C de EP-003 · HU-002](../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-002-modelos-del-encargo/C-EP-003-HU-002-el-planteamiento-se-reconstruye-igual/funcionalidad_implementada.md).

**Lo que quedó abierto:** cinco planes de pruebas del repositorio perdieron su línea fija. Es el primer hallazgo del validador, no un defecto suyo.
