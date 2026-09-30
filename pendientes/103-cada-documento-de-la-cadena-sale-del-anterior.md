# Pendiente · Cada documento de la cadena sale del anterior

**Estado:** abierto. Espera la aprobación del usuario.

| | |
|---|---|
| **Historia de usuario** | Por asignar: nace al aprobarse este pendiente |
| **De dónde sale** | [H-13 de la sesión del 2026-09-28](../historico-chat/resumenes/2026-09-28/sesion.md), sobre por qué el agente olvida las reglas |
| **Proyecto de origen** | El estándar mismo |

## El problema

Entre el pendiente y la historia de usuario no hay un documento que fije el alcance exacto, y nada obliga a que cada documento de la cadena salga del anterior. El alcance queda abierto y el agente agrega lo que no se pidió: con el pedido «crear la clase `Matematica`», le suma métodos. En la fase `C` de HU-023 el plan y el código terminaron diciendo cosas distintas.

## Por qué importa

Cada eslabón puede traer asuntos que el anterior no nombró, y el plan termina con trabajo que nadie aprobó. El freno del [pendiente 105](105-nada-se-ejecuta-fuera-del-plan-aprobado.md) sirve solo si el plan es fiel a lo pedido.

## Qué falta

Lo definió el usuario el 2026-09-29:

1. **La cadena** es hallazgo, pendiente, `analisis.md`, historia de usuario y plan de trabajo. El análisis es el eslabón nuevo, entre el pendiente y la historia, y fija el alcance con dos listas: lo que se hace y lo que no se hace.
2. **Cada documento amplía el anterior en profundidad, nunca en alcance.** Detalla lo mismo y no trae asuntos nuevos; si hace falta algo nuevo, se vuelve al documento anterior y el usuario lo aprueba ahí.
3. **Cada documento depende del anterior:** nace de él con su enlace, no avanza sin él aprobado y se revisa si él cambia.
4. **Cada punto cita de qué punto del documento anterior sale.** Un validador sigue la cadena desde el plan hasta el hallazgo; lo que no tiene origen se detiene.

Faltan dos decisiones del usuario:

- si el análisis también prohíbe lo que «el oficio da por sentado» ([`01·C14`](../base/01-conducta.md#c14--lo-que-el-oficio-ya-da-por-sentado-se-aplica-sin-ofrecerlo-como-opción)), que choca con [`02·F19`](../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md);
- si va como regla nueva en `02` o dentro de [`02·F0`](../base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md).

## El límite

- No cambia los documentos ya cerrados.
- La plantilla del plan de trabajo es del [pendiente 104](104-la-plantilla-del-plan-se-puede-comprobar.md).

## Cómo se sabrá que cerró

- Existe la plantilla de `analisis.md` con sus dos listas.
- La regla está escrita, con su checklist en CUMPLE.
- Un validador rechaza un plan con una tarea que no cita un criterio, una historia con un criterio que no cita el análisis, y un análisis con un punto que no cita el pendiente.
