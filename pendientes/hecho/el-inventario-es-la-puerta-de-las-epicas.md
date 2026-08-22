# Pendiente · La propuesta no exige el inventario de funcionalidades que da el punto de partida a las épicas

**Estado:** abierto · anotado 2026-08-21.

| | |
|---|---|
| **Historia de usuario** | [EP-003 — Documentos modelo y procedimientos](../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/epica.md) — es la épica dueña de los moldes; la HU exacta la decide cimiento (puede pedir molde nuevo y regla de flujo) |
| **Proyecto de origen** | **shopnest-mesa** · `C:/DesarrollosClaude/personales/shopnest-mesa` |
| **Su pendiente de seguimiento** | `pendientes/42-esperando-el-inventario-como-puerta-de-las-epicas.md` — queda **abierto allá** hasta que este se corrija |
| **A quién avisar al cerrar** | a **todos los instalados**: es método del flujo, no un caso de un proyecto — la lista está en [../plantillas/proyectos.md](../../plantillas/proyectos.md) |

## El problema

El flujo baja planteamiento → requisitos → épicas sin exigir, en ninguna estación, un **inventario de funcionalidades completo y aprobado por el usuario**. El §6 del molde de planteamiento lista requerimientos, pero nada obliga a que esa lista sea *el* inventario acordado ni a que las épicas se deriven de él y no de lo que el agente entendió.

La consecuencia se vio en `shopnest-mesa`: el agente escribió el planteamiento **asumiendo el alcance** — lo centró en el taller de la universidad — y de ahí derivaron tres épicas y 21 HU. El 2026-08-21 el usuario corrigió: *«eso lo asumió usted y de una hizo el planteamiento de esa manera; lo ideal es que me hubiera preguntado (...) no es para cerrarnos a eso sino para proyectarnos a cosas grandes. Lo ideal sería primero hacer un inventario de lo que se quiere (...) la propuesta debe venir acompañada del inventario que debe tener de manera clara todas las funcionalidades de lo que se va a desarrollar, porque eso es lo que da el punto de partida a las [épicas]»*. Y pidió, explícito, que cimiento lo sepa.

## Cómo se reproduce

`shopnest-mesa`, 2026-08-15 a 2026-08-21. El planteamiento se escribió el primer día centrado en el taller; el alcance real del usuario (ITIL 4 completo, el taller como punto de partida) solo salió a la luz seis días y tres épicas después, cuando una pregunta suya lo destapó. Ninguna regla del flujo lo habría preguntado antes.

## Por qué importa

No bloquea nada, y por eso es traicionero: el trabajo avanza en verde sobre un alcance que nadie confirmó. El costo se paga tarde y grande — épicas y HU escritas sobre el alcance asumido, y la corrección llega cuando ya hay 21 HU y código encima. Es la clase de error que una pregunta en la estación correcta evita entera.

## Qué falta

Tres piezas, y la tercera es de conducta:

1. **Un molde nuevo**, `plantillas/inventario-funcionalidades.md`: la lista completa de funcionalidades de lo que se va a desarrollar, con estado por ítem (existe / parcial / por construir / por confirmar) y las preguntas abiertas marcadas. Acompaña a la propuesta. Y con un rasgo que el usuario agregó después (2026-08-21): *«ese inventario es lo que se convierte en la documentación final del producto, manuales y todo eso»* — el molde debe nacer pensado para madurar hasta manual, no para botarse al derivar las épicas.
2. **Una regla del capítulo `02`** que lo exija **aprobado por el usuario antes de derivar épicas** — como `F2` exige la especificación antes del código: el inventario es el punto de partida de las épicas, y una épica que no baje de un ítem del inventario no arranca.
3. **La conducta**: el alcance que el usuario no ha dicho **se pregunta, no se asume** — evaluar si `01·C21` ya lo cubre o necesita la extensión explícita («ante alcance no declarado, la pregunta va antes del planteamiento»).

## El límite

No pide reabrir los planteamientos ya escritos de los proyectos instalados: el molde y la regla rigen hacia adelante. `shopnest-mesa` ya escribió el suyo por su cuenta (`propuesta-desarrollo/inventario-funcionalidades.md`) y puede servir de caso semilla del molde.

## Cómo se sabrá que cerró

El molde existe en `plantillas/`, una regla del `02` exige el inventario aprobado antes de derivar épicas, y el aviso llega a `shopnest-mesa` — donde se comprueba contra el inventario ya escrito: si el molde pide algo que el de acá no tiene, se completa acá; si el de acá tiene algo que el molde no pide, se reporta.
