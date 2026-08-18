# Pendiente · Falta la regla que obliga a reportar lo que es del estándar

**Estado:** **cerrado** el 2026-08-18. Anotado el 2026-08-16.

| | |
|---|---|
| **Historia de usuario** | [EP-007 · HU-008 — El proyecto reporta lo que es del estándar](../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-008-el-proyecto-reporta-al-estandar/HU-008-el-proyecto-reporta-al-estandar.md) — el canal del proyecto hacia el estándar es de instalación y actualización, que es esa épica |
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

Los pendientes [34](hecho/enlaces-de-las-plantillas-al-estandar.md) y [35](hecho/renombrar-deja-el-resumen-coherente.md) ya están escritos con esa forma; sirven de molde.

**3 · El aviso de vuelta (paso 6).** Es la mitad que nadie tiene hoy. El estándar sabe qué proyectos lo usan —[`plantillas/proyectos.md`](../plantillas/proyectos.md)— y sabe dónde está cada uno, así que puede escribir el aviso en el proyecto al cerrar el pendiente. Sin esto, el paso 7 deja pendientes abiertos para siempre y la regla se vuelve papel.

**4 · La comprobación.** Un pendiente del estándar sin proyecto de origen, o un pendiente de proyecto sin su par acá, es un fallo de trazabilidad y se puede detectar. Encaja con lo que ya hace `validadores/cruces.py`.

## Cómo se sabe que cerró

La regla está escrita en `base/` con su checklist, las dos plantillas existen, un pendiente reportado desde un proyecto se puede cerrar y el aviso llega solo al proyecto de origen.

---

# Cómo cerró — 2026-08-18

Fase: [`A-EP-007-HU-008`](../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-008-el-proyecto-reporta-al-estandar/A-EP-007-HU-008-la-regla-y-el-aviso-de-vuelta/), veredicto **Cumple**.

## Lo que faltaba de verdad era el paso 6

Los siete pasos los dictó el usuario y los cinco primeros se venían haciendo por criterio de cada sesión. **El aviso de vuelta no lo hacía nadie**, y sin él el paso 7 —el pendiente del proyecto queda abierto hasta confirmar— deja pendientes abiertos para siempre: nadie vuelve a mirar el repositorio ajeno.

## Las cuatro piezas

**1 · La regla.** [`02·F24`](../base/02-flujo-de-trabajo/reglas/F24-el-defecto-del-estandar-se-reporta-no-se-corrige.md), con su checklist en CUMPLE. **Va al capítulo `02` y no a la épica de instalación:** lo que gobierna es un paso del flujo —qué hace el agente cuando lo que hay que arreglar no es suyo—; la instalación es por dónde viaja el aviso, no de qué trata la regla.

**Y resuelve el choque con `02·F20`** que estaba anotado en el punto 8 del [33](33-defectos-que-destaparon-los-resumenes-viejos.md): `F20` manda parar y proponer, y no decía qué hacer cuando lo descubierto es del estándar. Ahora `F20` para y `F24` dice a dónde va.

**2 · Las dos plantillas.** [pendiente-reportado](../plantillas/pendiente-reportado.md) y [pendiente-de-seguimiento](../plantillas/pendiente-de-seguimiento.md), **cada una nombrando a la otra** — porque uno sin el otro es exactamente la mitad que falló los dos días de agosto que originaron esto.

**3 · El aviso de vuelta.** `cerrar.py` lo escribe en cada proyecto al que le toca. **Un archivo de pendiente y nada más: nunca toca código**, y hay una prueba que compara la raíz del proyecto antes y después. Idempotente.

**4 · La comprobación.** `validar.py pendientes` reporta el pendiente que dice venir de un proyecto sin nombrarlo. **Los 34 del backlog pasan sin tocar ninguno**, que es la señal de que la regla describe lo que ya se hacía bien en vez de inventar una exigencia.

## Lo que este pendiente decía, comprobado

Decía: *«sin el aviso, cada reporte deja un pendiente abierto para siempre en el proyecto»*. **Tres cierres lo demuestran** y quedaron anotados: dos los espera `shopnest-mesa` y uno `dp`, y ninguno lo sabe.

**No se mandan hacia atrás.** Inventar hoy un aviso sobre una corrección de hace dos días es escribir una fecha falsa.

## Lo que queda abierto

**Que el proyecto compruebe el aviso no lo hace nadie.** El aviso llega solo; abrirlo, verificar y cerrar el pendiente de seguimiento sigue dependiendo de que alguien lo lea — y ningún programa de acá puede verlo, porque ese pendiente vive en otro repositorio.

**Y falta avisarles.** La propia regla manda avisarle a **todos los proyectos instalados** al cerrar esto, no solo a `shopnest-mesa`: la regla los rige a todos.
