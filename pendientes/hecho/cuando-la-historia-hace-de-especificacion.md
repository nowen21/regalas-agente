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

**Se eligió el camino 2**, y la diferencia con el 1 no es de forma:

> **Una excepción dice cuándo la regla no rige. Lo que se escribió dice dónde vive lo que la regla exige.**

[`02·F2`](../../base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md) sigue exigiendo especificación acordada **en todos los casos**. Lo que agrega es de qué está hecha cuando el entregable no es código:

> *Si el entregable no es código, la especificación es la historia con sus criterios de aceptación.*

**Y pesa que `F2` ya tenía una excepción.** Abrirle la segunda a una regla que ya trae una es la puerta que después nadie cierra — [`08·T1`](../../base/08-pruebas.md#t1--todo-cambio-con-lógica-lleva-prueba) es el ejemplo vivo: su excepción deja al agente autorizándose a sí mismo a no probar.

**Lo que ordena:** las dos fases que se habían abierto declarando que no tienen especificación aparte dejan de ser un incumplimiento silencioso.

Fase: [`A-EP-001-HU-010`](../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/A-EP-001-HU-010-cuando-la-historia-hace-de-especificacion).
