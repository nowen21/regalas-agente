# Pendiente · `F2` no dice cuándo no aplica

**Estado:** abierto · anotado 2026-08-14 · nace del hallazgo H-7 de [2026-08-14](../historico-chat/resumenes/2026-08-14/hu-de-la-comprobacion-automatica.md).

## El problema

[`02·F2`](../base/02-flujo-de-trabajo/reglas/F2-sin-spec-acordada-no-hay-codigo.md) exige una especificación acordada antes de tocar código. Está escrita dando por hecho que lo que se construye es el código de un módulo.

Dos fases seguidas de este repositorio se abrieron declarando que no tienen especificación aparte:

- `A-EP-001-HU-001-molde-de-regla`, porque su entregable es texto normativo.
- `A-EP-004-HU-010-declaracion-y-comprobacion`, porque son programas cortos cuya especificación son los criterios de aceptación de su historia.

En los dos casos, una especificación aparte diría lo mismo que la historia de usuario.

## Qué falta

Decidir entre dos caminos, y escribirlo:

**1. Escribirle la excepción a `F2`**, con sus tres partes: cuándo aplica, hasta dónde llega y quién la autoriza.

**2. Aceptar que la historia de usuario hace de especificación** cuando el módulo es el propio estándar, y decirlo en la regla.

Cualquiera de los dos pasa por el procedimiento del capítulo `20`, con checklist y versión.

## Por qué importa

Una regla que se incumple dos veces seguidas con buenos motivos se vuelve costumbre incumplirla. Y la próxima vez nadie va a saber si el caso era legítimo o si se saltó el paso.
