# Pendiente · `F2` no dice cuándo no aplica

**Estado:** **cerrado** el 2026-08-18, con la v23.10.0. Abierto · anotado 2026-08-14 · nace del hallazgo H-7 de [2026-08-14](../../historico-chat/resumenes/2026-08-14/hu-de-la-comprobacion-automatica.md).

| | |
|---|---|
| **Historia de usuario** | [EP-001 · HU-010 — Cuándo no aplica la exigencia de especificación](../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) — es la historia escrita para este pendiente; su fase A ya está abierta |

## El problema

[`02·F2`](../../base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md) exige una especificación acordada antes de tocar código. Está escrita dando por hecho que lo que se construye es el código de un módulo.

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

---

# Cómo cerró — 2026-08-18

**No hizo falta escribir nada: ya estaba escrito.**

[`02·F19`](../../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md) lo dice desde la v3.1.0:

> **La redacción del CA es la especificación funcional**

Osea que el estándar ya decía que los criterios de aceptación de la historia **son** la especificación. El pendiente preguntaba algo contestado en su propio capítulo, dos reglas más abajo.

## Cómo se descubrió, que es lo que vale

**Primero se hizo mal.** Se le agregó a `02·F2` una frase que decía lo mismo con otras palabras, y **chocaba con [`02·F0`](../../base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md)**: la cadena prohíbe que un eslabón *«se salte, **se fusione** ni se omita»*, y esa frase fusionaba la historia con la especificación.

**Lo vio el usuario preguntando**, no el agente comprobando. La fila 2 del checklist —[`20·M12`](../../base/20-meta-reglas/reglas/M12-antes-de-crear-una-regla-buscar-la-duplicacion-es-el-defecto-mas-caro.md), *«se leyó entero el capítulo dueño»*— se selló en verde sin leerlo. Al leerlo apareció `F19` en la misma pasada.

**El texto de `F2` se devolvió a como estaba**, con su sello original.

## Lo que dejó

Dos cosas que valen más que el pendiente:

1. **La fase [`A-EP-005-HU-010`](../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-010-la-regla-llega-al-escribir-el-archivo/A-EP-005-HU-010-el-capitulo-llega-al-escribir-el-archivo/)**, que hace que al tocar una regla lleguen las que se relacionan con ella. Hoy, al tocar `F2`, `F0` sale tercera en la lista.
2. **Que las dos fases que se abrieron sin especificación aparte no estaban incumpliendo nada.** `F19` ya las cubría, y nadie lo había mirado.
