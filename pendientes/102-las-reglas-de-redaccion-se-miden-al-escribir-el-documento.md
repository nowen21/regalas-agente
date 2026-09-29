# Pendiente · Las reglas de redacción se miden al escribir el documento

**Estado:** **hecho** el 2026-09-28, en la misma sesión que lo anotó. Lo construyó la fase `D` de HU-012 de EP-004 (39.5.0): el enganche de escritura mide lo recién escrito y el molde del resumen lleva sus campos en tabla.

| | |
|---|---|
| **Historia de usuario** | [EP-004 · HU-012](../documentacion/epicas/EP-004-comprobacion-automatica/HU-012-marcas-de-generacion-automatica/HU-012-marcas-de-generacion-automatica.md), CA-05 y CA-06, fase `D`. Es la historia que cuenta las marcas |
| **De dónde sale** | [H-4 de la sesión del 2026-09-28](../historico-chat/resumenes/2026-09-28/sesion.md), sobre por qué el agente olvida las reglas |
| **Proyecto de origen** | El estándar mismo |

## El problema

Cuando el agente escribe o edita un documento, nada mide ese texto contra las reglas de redacción (`00·ID8`, `00·ID9`, `00·ID11`, `00·ID12`). Revisado el 2026-09-28:

- Los enganches que corren al escribir un archivo (`PostToolUse` sobre `Write|Edit`, en `validadores/instalar.py`) revisan enlaces, recuerdos, reglas relacionadas, rutas y veredictos. Ninguno cuenta las marcas.
- El `pre-commit` (`.githooks/pre-commit`) sí las cuenta, pero solo al guardar y solo como aviso: «no bloquea acá, pero es deuda que alguien limpia después».
- La respuesta del chat sí se mide y la medición vuelve en el mensaje siguiente (`hook_reglas.py`, «LA RESPUESTA ANTERIOR, MEDIDA»). Los documentos no tienen nada igual.

Además, la plantilla [plantillas/sesion.md](../plantillas/sesion.md) produce marcas por sí sola: cada campo lleno queda como viñeta que abre con negrita y dos puntos (`- **Qué pasó:** …`), que es una de las marcas de `00·ID8`.

Medido en H-4: el resumen de esta sesión tenía 39 líneas con marcas; `historico-chat/resumenes/` suma 5550 marcas en 68 de 90 archivos, y `historico-chat/memory/`, 112 en 25 de 26. Parte de las de los resúmenes son campos de formulario llenos.

## Por qué importa

El agente recibe las reglas de redacción cuando el mensaje pide escribir, y aun así entrega documentos con marcas, porque nadie se las muestra en el momento. El aviso llega al commit, cuando el documento ya se entregó y el usuario ya lo leyó. El usuario lo pidió así: *«todo debe saber en tiempo real que se deben aplicar esas reglas»*.

## Qué falta

1. **Medir al escribir.** Un enganche sobre `Write|Edit` que cuente las marcas de lo que se acaba de escribir en un `.md` y se las devuelva al agente en ese mismo turno, con la línea y la marca, para que corrija antes de entregar.
2. **Decidir el formato de campos de `sesion.md`.** Hay dos salidas:
   - cambiar el molde para que los campos no produzcan la marca, lo que toca la plantilla y los resúmenes nuevos;
   - declarar el campo de formulario como formato permitido en el anexo de marcas, lo que cambia qué exige `00·ID8`.
   El usuario eligió la primera el 2026-09-28: los campos van en tabla.

## El límite

- No corrige los documentos ya escritos ni las transcripciones, que son literales.
- No cambia cómo se mide la respuesta del chat, que ya funciona.
- Quitar de las plantillas la caja de reglas copiada es de H-3, no de este pendiente.

## Cómo se sabrá que cerró

- Escribir un `.md` de prueba con una raya larga y una viñeta con negrita devuelve, en ese mismo turno, las dos marcas con su línea.
- Llenar un campo de un resumen nuevo con el molde de `sesion.md` no produce marca, o el anexo lo declara permitido, según lo que decida el usuario.
- `python validadores/validar.py estandar` termina sin incumplimientos.
