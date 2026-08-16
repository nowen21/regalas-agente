# Pendiente · Falta la regla que obliga a reportar lo que es del estándar

**Estado:** abierto · anotado 2026-08-16.

| | |
|---|---|
| **Proyecto de origen** | **`shopnest-mesa`** · `C:/DesarrollosClaude/personales/shopnest-mesa` |
| **Su pendiente de seguimiento** | `pendientes/04-falta-la-regla-de-reporte-al-cimiento.md` — queda **abierto allá** hasta que este se corrija |
| **A quién avisar al cerrar** | a **todos los proyectos instalados**, no solo al de origen: la regla los rige a todos. La lista está en [`plantillas/proyectos.md`](../plantillas/proyectos.md) |

## El problema

El estándar dice qué no se toca, pero no dice **qué hacer con lo que no se toca**.

Un proyecto que encuentra un defecto del estándar hoy tiene tres caminos y ninguno escrito: arreglarlo por su cuenta —y pisar a los demás proyectos—, anotarlo solo en su repositorio —donde el estándar nunca lo va a ver— o no hacer nada. Los tres pasaron ya en `shopnest-mesa` el mismo día:

- El 2026-08-15 se parchearon los enlaces en las copias locales y se dejó anotado *«su pendiente va en el repositorio del estándar y ese no es este»*. El estándar no se enteró de nada durante un día.
- El 2026-08-16 el agente creó el pendiente allá y **cerró el del proyecto**, dándolo por traspasado. El seguimiento se perdió en el mismo acto de traspasarlo.

Nada de eso incumplió ninguna regla, porque la regla no existe.

## Qué falta

Una regla que fije el procedimiento. El usuario lo dictó completo el 2026-08-16, y es esto:

1. **No modificar el estándar.** El defecto se deja intacto para que lo corrija quien lo escribe.
2. **Crear un pendiente en `pendientes/` del estándar**, describiendo qué se encontró y qué debe corregirse.
3. **Nombrar explícitamente el proyecto de origen** en ese pendiente. Es obligatorio: sin eso no hay trazabilidad entre el estándar, la corrección y el proyecto afectado.
4. **Crear también un pendiente en el proyecto**, diciendo que hay una corrección pendiente en el estándar.
5. **El proyecto sigue trabajando solo lo suyo.** Lo que sea del estándar se reporta y no se toca.
6. **El estándar avisa al proyecto** cuando la corrección esté hecha.
7. **El pendiente del proyecto queda abierto** hasta confirmar la corrección. Es el seguimiento; no se cierra antes.

> En el proyecto se modifica únicamente lo que corresponde al proyecto. Lo que corresponde al estándar no se modifica: se reporta como pendiente en el estándar y también se registra como pendiente en el proyecto afectado. El estándar es responsable de corregir y de informar al proyecto cuando esté solucionado.

## Qué hay que construir

**1 · La regla.** Va en `base/`, y el capítulo lo decide el estándar. Dos candidatos: `01-conducta` —es una conducta del agente ante un defecto ajeno— o `02-flujo-de-trabajo` —es un paso del flujo—. Se cruza con `02·F20` (parar y proponer), que hoy choca con corregir el defecto que uno mismo detecta: eso está anotado en el [pendiente 33 · punto 8](33-defectos-que-destaparon-los-resumenes-viejos.md) y esta regla es la que lo resuelve.

**2 · Las dos plantillas del pendiente**, para que los dos lados salgan iguales siempre:
- La del estándar: cabecera con **proyecto de origen**, pendiente de seguimiento y a quién avisar al cerrar.
- La del proyecto: cabecera con **dónde está el defecto**, qué se reportó allá, qué se espera y cuándo cierra.

Los pendientes [34](hecho/enlaces-de-las-plantillas-al-estandar.md) y [35](35-renombrar-una-sesion-deja-roto-el-enlace-de-su-resumen.md) ya están escritos con esa forma; sirven de molde.

**3 · El aviso de vuelta (paso 6).** Es la mitad que nadie tiene hoy. El estándar sabe qué proyectos lo usan —[`plantillas/proyectos.md`](../plantillas/proyectos.md)— y sabe dónde está cada uno, así que puede escribir el aviso en el proyecto al cerrar el pendiente. Sin esto, el paso 7 deja pendientes abiertos para siempre y la regla se vuelve papel.

**4 · La comprobación.** Un pendiente del estándar sin proyecto de origen, o un pendiente de proyecto sin su par acá, es un fallo de trazabilidad y se puede detectar. Encaja con lo que ya hace `validadores/cruces.py`.

## Cómo se sabe que cerró

La regla está escrita en `base/` con su checklist, las dos plantillas existen, un pendiente reportado desde un proyecto se puede cerrar y el aviso llega solo al proyecto de origen.
