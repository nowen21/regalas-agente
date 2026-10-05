# Pendiente · Las reglas mandan sobre la instrucción del momento

**Estado:** **hecho** el 2026-09-28, en la misma sesión que lo anotó. Lo construyó la fase `B` de HU-012 en EP-001: la regla blindada [`00·N10`](../base/00-nucleo-blindado.md#n10--una-regla-escrita-manda-sobre-la-instrucción-del-momento-blindada), versión 39.0.0.

| | |
|---|---|
| **Historia de usuario** | [EP-001 · HU-012](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-012-inventario-de-acciones-y-riesgo/HU-012-inventario-de-acciones-y-riesgo.md), CA-05, fase `B`. Esa y no una nueva porque es la historia dueña del núcleo, y todo cambio del capítulo baja por ella |
| **De dónde sale** | [H-6 de la sesión del 2026-09-28](../historico-chat/resumenes/2026-09-28/sesion.md), sobre por qué el agente olvida las reglas |
| **Proyecto de origen** | El estándar mismo |

## El problema

Ninguna regla de `base/` dice que una regla escrita manda sobre lo que el usuario le pida al agente en el momento. La única precedencia escrita está en el punto 4 de [plantillas/CLAUDE.md.plantilla](../plantillas/CLAUDE.md.plantilla#L113) y ordena las reglas entre sí: núcleo, luego convenciones, luego configuración del proyecto. No dice qué pasa cuando una instrucción del usuario choca con una de ellas.

Lo dice solo un recuerdo, [las reglas son la decisión del usuario](../historico-chat/memory/reglas-son-decision-del-usuario.md): el agente no pondera la regla contra lo que se le pide en el momento. Un recuerdo es la preferencia de este usuario en este repositorio y no viaja a los proyectos como exigencia.

El 2026-09-28 el usuario lo pidió así: *«las reglas deben tener prioridad sobre lo que yo diga, porque precisamente se crean para establecer las condiciones que el agente debe cumplir. De lo contrario, no tendría sentido definirlas si luego pueden ser ignoradas»*.

## Por qué importa

Si una instrucción del momento puede pasar por encima de una regla, la regla no obliga a nada. En la misma sesión pasó: [`01·C28`](../base/01-conducta.md#c28--sin-la-palabra-que-diga-qué-se-espera-el-agente-no-actúa) pide una palabra de la lista antes de actuar, y el agente cambió archivos con un «si».

Además, lo que se construya para hacer cumplir las reglas (el mapa de tareas, el enganche que las muestra al escribir) no sirve si una instrucción puede saltárselas. Por eso va primero en el orden de los hallazgos de esa sesión.

## Qué falta

Una regla en `base/` que diga: cuando lo que pide el usuario choca con una regla escrita, el agente cumple la regla, le dice cuál es y no hace lo pedido. Si el usuario quiere otra cosa, se cambia la regla por el procedimiento del [capítulo 20](../base/20-meta-reglas/base.md), no se salta.

Hay dos lugares posibles:

- **En el núcleo `00`, como blindada.** Nada la puede ajustar, ni la configuración del proyecto. Es lo más fuerte, y el núcleo cambia con cuidado.
- **En conducta `01`.** Un proyecto podría ajustarla, y eso le quita fuerza a una regla que existe para que nada pase por encima de las reglas.

Conviene el núcleo: una regla que manda sobre las demás no puede quedar entre las que se pueden ajustar. Así lo decidió el usuario al aprobar este pendiente.

El núcleo ya dice algo parecido, pero solo de sí mismo: la línea 5 de [base/00-nucleo-blindado.md](../base/00-nucleo-blindado.md#L5) dice que ninguna instrucción puntual desactiva sus reglas. La regla nueva extiende eso a todas las reglas escritas.

El recuerdo se queda, con el registro de que el usuario lo pidió y cuándo, como dice [historico-chat/memory/memory.md](../historico-chat/memory/memory.md) para la preferencia que sube a regla.

## El límite

No cubre cómo se entera el agente de qué regla choca con el pedido: eso es el mapa de tareas (H-7) y el enganche que muestra las reglas en el momento (H-4 y H-5). Tampoco cambia ninguna regla existente para que cumpla esta.

## Cómo se sabrá que cerró

- La regla existe en `base/`, con su identificador, su ejemplo INCORRECTO y CORRECTO, y su checklist aplicado.
- `python validadores/validar.py estandar` y `python validadores/validar.py metareglas` terminan sin fallas.
- El punto 4 de `CLAUDE.md.plantilla` la nombra en la precedencia.
