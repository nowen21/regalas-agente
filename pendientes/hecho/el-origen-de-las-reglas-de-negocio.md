# Pendiente · Las reglas de negocio del propio estándar no dicen de dónde bajan

**Estado:** cerrado 2026-08-18. Anotado el 2026-08-16.

> **Las 57 ya dicen de qué historia bajan** —eran 31 al anotarlo— y el validador da cero. Fase [`B-EP-003-HU-004`](../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-004-modelo-de-la-especificacion/B-EP-003-HU-004-el-origen-de-las-57-reglas).
>
> **El origen no hubo que inventarlo:** cada `### 4.N` ya declaraba su fase. Faltaba bajarlo de la sección a la regla.
>
> **Ninguna se borró, y esa era la tercera salida.** El usuario decidió el 2026-08-18 **no borrar ninguna**. Con eso el pendiente cierra entero.

| | |
|---|---|
| **Historia de usuario** | [EP-003 · HU-004 — Modelo de la especificación](../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-004-modelo-de-la-especificacion/HU-004-modelo-de-la-especificacion.md) — las 31 reglas sin origen están en las dos especificaciones de esta casa |
| **Nace de cerrar** | el [43](el-origen-de-la-regla-de-negocio.md) (v22.0.0 y v22.1.0). Es lo que su validador destapó, no su reapertura |
| **Proyecto de origen** | El estándar mismo |

## El problema

La v22.0.0 empezó a exigir que toda regla de negocio diga de dónde baja, y la v22.1.0 escribió el programa que lo comprueba. Al correrlo por primera vez sobre esta casa:

| Especificación | Reglas sin origen |
|---|---:|
| `documentacion/automatismos/spec.md` | 16 |
| `documentacion/documentos-modelo/spec.md` | 15 |
| **Total** | **31** |

**El estándar no cumple la regla que acaba de escribir.** Es el mismo tipo de hueco que el [pendiente 11](limpiar-marcadores-de-ia-del-texto-del-estandar.md) —una norma nueva y el texto viejo diciendo lo contrario— y el [19](ninguna-regla-reprueba-su-propio-checklist.md).

## Qué falta

**No es trabajo mecánico**, y por eso no se hizo al cerrar el 43: hay que decidir, regla por regla, de dónde baja. Tres salidas por cada una:

1. **Baja de algo que existe** — se le escribe el identificador y listo.
2. **No baja de nada pero debería existir** — se sube a la historia que corresponda y baja desde allá, que es lo que la regla nueva manda.
3. **No baja de nada y no hace falta** — se borra. Que esté escrita no la vuelve necesaria.

La tercera es la incómoda, y es la razón de ser de todo esto: alguna de esas 31 seguramente no la pidió nadie.

## Conviene hacerlo por archivo

Son dos especificaciones y se pueden cerrar por separado. Cada una es una fase de la historia de su módulo, no una fase de EP-003 ni de EP-004: lo que cambia es el documento de un módulo, no el molde ni el validador.

## El límite

**El estándar no reabre lo cerrado.** Estas 31 quedaron escritas bajo una versión que no pedía la procedencia, así que no son un incumplimiento retroactivo: son deuda visible. Lo que no se puede es dejarlas ahí y seguir exigiéndoles la regla a los proyectos herederos.

## Cómo se sabrá que cerró

`validar.py plantilla` sobre las dos especificaciones no reporta ninguna regla sin origen, y de cada una que se haya borrado quedó escrito por qué.


---

# Cómo cerró — 2026-08-18

**Las 57 dicen de qué historia bajan** —eran 31 al anotarlo— y el validador da cero. Fase [`B-EP-003-HU-004`](../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-004-modelo-de-la-especificacion/B-EP-003-HU-004-el-origen-de-las-57-reglas/README.md).

**La tercera salida no se usó: el usuario decidió no borrar ninguna.**

El motivo es el que el propio pendiente ya anotaba, y sigue valiendo al revés: **que una regla tenga procedencia no la vuelve necesaria, pero borrar una vigente quita algo del estándar.** Ninguna de las 57 estorba, ninguna contradice a otra, y la que sobre se verá cuando choque con algo — no antes.

**El origen no hubo que inventarlo:** cada `### 4.N` ya declaraba su fase. Faltaba bajarlo de la sección a la regla.

## Cómo quedó comprobado

`validar.py plantilla` sobre las dos especificaciones no reporta ninguna regla sin origen. Y no hay ninguna borrada de la que haya que explicar por qué, porque no se borró ninguna.
