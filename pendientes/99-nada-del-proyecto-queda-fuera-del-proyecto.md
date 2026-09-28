# Pendiente · Nada del agente ni del proyecto queda fuera de ellos

**Estado:** **hecho** el 2026-09-28, en la misma sesión que lo anotó. Lo construyó la fase `B` de HU-011 en EP-001: la regla [`01·C29`](../base/01-conducta.md#c29--guarda-dentro-del-repositorio-todo-lo-del-agente-y-del-proyecto), versión 39.1.0.

| | |
|---|---|
| **Historia de usuario** | [EP-001 · HU-011](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-011-buscar-antes-de-preguntar/HU-011-buscar-antes-de-preguntar.md), CA-04, fase `B`. Esa y no una nueva porque es la historia dueña del capítulo 01, donde va la regla |
| **De dónde sale** | [H-2 de la sesión del 2026-09-28](../historico-chat/resumenes/2026-09-28/sesion.md), sobre por qué el agente olvida las reglas |
| **Proyecto de origen** | El estándar mismo |

## El problema

Lo que pertenece al agente o al proyecto puede terminar guardado por la herramienta fuera del repositorio, y ninguna regla lo impide.

Pasó el 2026-09-28: el arranque de la sesión le entregó al agente 79,7 KB de reglas. Claude Code los guardó en su propio almacén, `~/.claude/projects/<proyecto>/<id-de-sesión>/tool-results/`, y al agente le mostró solo los primeros 2 KB. Las reglas del proyecto quedaron en un archivo que nadie versiona ni revisa, y el agente trabajó sin ellas.

Las dos reglas que tocan el tema cubren solo una parte:

- [`01·C19`](../base/01-conducta.md#c19--escribe-la-memoria-del-agente-dentro-del-repositorio-del-proyecto) pide que la memoria del agente viva en el repositorio. Cubre la memoria y nada más.
- [`04·S9`](../base/04-seguridad.md#s9--no-toques-rutas-del-sistema-fuera-del-proyecto--solo-autorizadas-exactas) pide que el agente escriba solo dentro del proyecto. Cubre lo que escribe el agente, no lo que guarda la herramienta por su cuenta. Además dice «Leer fuera sí», y eso deja abierto que el agente dependa de contenido del proyecto guardado afuera.

El usuario lo pidió así: *«nada debe quedar por fuera del agente o del proyecto. Si se necesita alguna información, debe existir un enlace que lleve al lugar donde está el contenido. Lo que pertenece al agente o al proyecto debe permanecer dentro del agente o del proyecto, no en Claude. Eso debe aplicar para todo»*. Hoy vive solo como recuerdo, [nada del agente ni del proyecto queda por fuera de ellos](../historico-chat/memory/nada-del-proyecto-queda-en-la-herramienta.md).

## Por qué importa

Lo que queda en el almacén de la herramienta no se versiona, no se revisa y no viaja a otra máquina. Si el agente depende de eso, trabaja con algo que nadie ve. En el caso del 2026-09-28, el agente trabajó sin las reglas que el estándar da por cargadas.

## Qué falta

Una regla en `base/` que diga: todo lo que pertenece al agente o al proyecto vive en el repositorio, y a su contenido se llega por un enlace. Si la herramienta guarda algo del proyecto afuera, eso se corrige en su origen, no se lee de allá.

Hay dos salidas:

- **Una regla nueva que cubra lo que hoy cubren `C19` y `S9` por partes**, y que las dos la extiendan. Queda una sola regla para el principio, y las otras dos dicen lo suyo.
- **Ampliar `S9`** para que cubra también lo que guarda la herramienta. Es más corto, pero `S9` es de seguridad y habla de rutas del sistema; el principio es más amplio que eso.

Conviene la regla nueva: el principio vale para todo, y meterlo en una regla de rutas lo esconde.

El recuerdo se queda, con el registro de que el usuario lo pidió y cuándo, como dice [memory.md](../historico-chat/memory/memory.md) para la preferencia que sube a regla.

## El límite

No cubre qué le entrega el arranque de la sesión al agente ni cómo cabe en el contexto: eso es de H-1. Tampoco construye el programa que avise cuando algo del proyecto quede afuera.

## Cómo se sabrá que cerró

- La regla existe en `base/`, con su identificador, su ejemplo INCORRECTO y CORRECTO, y su checklist aplicado.
- `C19` la extiende en vez de repetirla, y la regla nueva enlaza `S9`. `S9` no se cambia desde aquí: su capítulo tiene su propia historia dueña, HU-017.
- `python validadores/validar.py estandar` y `python validadores/validar.py metareglas` terminan sin fallas.
