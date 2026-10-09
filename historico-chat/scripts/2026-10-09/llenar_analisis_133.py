# -*- coding: utf-8 -*-
"""Llena las secciones que faltan del análisis 1 del pendiente 133, con lo acordado en la sesión 2 del 2026-10-09."""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
P = os.path.join(RAIZ, "historico-chat", "resumenes", "2026-10-05", "pendientes",
                 "133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje", "analisis-1.md")
R = "../../../../../"
EP = R + "documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/"

t = io.open(P, encoding="utf-8").read()


def entre(desde, hasta, cuerpo):
    global t
    i = t.index(desde)
    j = t.index(hasta, i + len(desde))
    t = t[:i] + cuerpo.rstrip() + "\n\n" + t[j:]


def cambiar(viejo, nuevo):
    global t
    assert viejo in t, viejo[:60]
    t = t.replace(viejo, nuevo)


entre("### Cimiento: las reglas que aplican y las que chocan", "### El proyecto", f"""### Cimiento: las reglas que aplican y las que chocan

Aplican `02·F0` (el cambio recorre la cadena), `08·T1` (cada cambio lleva su prueba), `00·N10` (la regla escrita manda: por eso el núcleo llega completo) y `01·C28` (la palabra clave dice qué autoriza el mensaje; la acción dice qué reglas rigen). Cambia lo que dice [base/tareas.md]({R}base/tareas.md) sobre cuándo llegan las reglas, y con eso `20·M10` pide versión. No choca ninguna.""")

entre("### Lo aprendido: señales, lecciones y análisis anteriores", "### El entorno", f"""### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| [HU-023 de EP-005: cada tarea sabe qué reglas le aplican]({EP}HU-023-cada-tarea-sabe-que-reglas-le-aplican/HU-023-cada-tarea-sabe-que-reglas-le-aplican.md) | Construyó el mapa de tareas y la elección por palabra clave. Dejó escrita la elección por acción, pero no la conectó a ningún enganche. Los acuerdos 1 y 3 la terminan |
| [Análisis 2 del pendiente 119: cuántos tokens se gastan, dónde y en vivo]({R}historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md) | Anticipó que el recordatorio de cada mensaje convenía pasarlo a un programa. Lo recoge el acuerdo 2 |
| Decisión del usuario del 2026-08-31, en la [HU-012 de EP-005: hacer cumplir lo que solo se recuerda]({EP}HU-012-hacer-cumplir-lo-que-solo-se-recuerda/HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md), RN-05 | Medir la redacción sin detener. El acuerdo 8 la confirma |""")

cambiar("""| Proyectos que heredan | «tipo de versión según `20·M10`, y si aplica `02·F22`» |
| Normas y leyes | «cuáles aplican, o "ninguna"» |""", """| Proyectos que heredan | MENOR (`20·M10`): cambia qué enganches se instalan y cuándo llegan las reglas, pero no les pide hacer nada a mano; llega con `instalar.py` |
| Normas y leyes | Ninguna |""")

i = t.index("| Caso | Dónde se presenta")
j = t.index("\n---", i)
t = t[:i] + """| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Un mensaje que solo pregunta | Toda sesión | Llegan reglas de trabajo que no aplican | Acuerdo 1: solo `responder` |
| Una acción que pide dos tareas, como `git commit` (`correr-comando` y `tocar-git`) | Toda sesión | La misma regla llega dos veces | Acuerdo 1: cada regla una vez por sesión |
| Cambiar código, datos, el estándar o ir afuera | Tareas sin palabra clave | Sus reglas no llegan nunca, como hoy | Acuerdo 1 |
| Escribir una prueba | Cualquier proyecto | Llegan 80 KB de reglas de código | Acuerdo 3 |
| La conversación se resume | Sesiones largas | Se pierden las reglas ya entregadas | Acuerdo 5 |
| Un subagente actúa | Claude Code con subagentes | El subagente actúa sin reglas | Acuerdo 1: `PreToolUse` también corre para los subagentes y trae `agent_id`; la cuenta se lleva por agente |
| Otro proyecto que hereda | Todos los de la base | Sigue con la carga vieja | `instalar.py` deja los enganches nuevos |
| Otra herramienta distinta de Claude Code | Proyectos con otra herramienta | No tiene `PreToolUse` | No hace falta cubrirlo hoy: Claude Code es la única herramienta instalada |
""" + t[j:]

entre("## Propuesta final", "## Lecciones aprendidas", f"""## Propuesta final: hallazgo y pendiente V2, épica y HU

### Hallazgo V2. Las reglas llegan repetidas en cada mensaje y no llegan cuando se actúa

| Campo | Valor |
|---|---|
| Qué pasó | Con cada mensaje llegan las mismas listas de reglas, y seis de ellas dos veces. Antes de cada acción no llega ninguna: `base/tareas.md` lo describe, pero ningún enganche lo hace. Por eso `cambiar-codigo`, `tocar-datos`, `ir-afuera` y `cambiar-estandar`, que no tienen palabra clave, no entregan sus reglas en ningún momento |
| Por qué importa | Se gastan tokens en cada mensaje de todos los proyectos, y aun así el agente cambia código y el estándar sin sus reglas |

### Pendiente V2. Las reglas llegan cuando se actúa, una sola vez, y nada se repite

| Campo | Valor |
|---|---|
| De dónde sale | El hallazgo V2: las reglas llegan repetidas en cada mensaje y no llegan cuando se actúa |
| El problema | Las reglas se eligen solo por la palabra clave del mensaje. Lo que de verdad dice qué reglas rigen es la acción, y antes de ella no llega nada |
| Por qué importa | El agente trabaja sin las reglas de lo que está haciendo, y cada mensaje paga reglas que no usa |

### Épica y HU que salen del análisis

Se suman a la [EP-005: automatismos que no dependen de que alguien se acuerde]({EP}epica.md), porque ahí está la HU-023, que eligió las reglas por tarea.

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | HU-025 | Las reglas de cada tarea llegan antes de la acción, una sola vez, y nada se repite | Antes de la acción no llega ninguna regla, y con cada mensaje llegan repetidas | Ninguna | Es la que arregla el problema grave, y la que más ahorra | 2 y 3 |
| 2 | HU-026 | Las reglas de cambiar código llegan partidas según lo que se toca | Con la HU-025, la primera vez que se toca código llegan 80 KB | HU-025 | Sin la HU-025 nadie entrega esas reglas | 4 |
| 3 | HU-027 | El núcleo llega completo, y lo entregado vuelve después de un resumen | Al resumir la conversación se pierde lo entregado, y el núcleo no llega completo | HU-025 | Necesita la cuenta de lo entregado que lleva la HU-025 | 5 |""")

cambiar("""| 1 | «lección» | Funcionó / Falló | «S-NNN» | «complementa R-n» / «nueva R-n» / «no aplica» |""",
        """| 1 | Antes de proponer un pendiente nuevo, buscar si ya hay uno abierto del mismo tema: este tema iba a abrir el 151 y ya existía el 133 | Falló | Se escribe al aprobar | Complementa R-2 |
| 2 | Explicar con un ejemplo de la misma sesión: la propuesta de no frenar la respuesta se entendió al mostrar el aviso real de los 2.697 caracteres | Funcionó | Se escribe al aprobar | Complementa R-10 |""")

cambiar("""| 1 | Pasar el pendiente a su versión siguiente | `13·DOC26` | Este análisis, de una y sin fase: `«ruta del pendiente.md»`, hecho el «fecha» |
| 2 | «qué hay que hacer» | «número» | «épica y HU, con su título y su enlace» |""",
        """| 1 | Pasar el pendiente a su versión siguiente | `13·DOC26` | Este análisis, de una y sin fase: `historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/pendiente.md` |
| 2 | Antes de cada acción, `hook_antes.py` reconoce la tarea con las acciones de `base/tareas.md` y entrega por `additionalContext` las reglas que todavía no se le dieron en la sesión a ese agente o subagente; con cada mensaje llegan solo las de `responder`, y las de `recibir-pedido` cuando la palabra autoriza cambiar algo | 1 | EP-005·HU-025 |
| 3 | Sale el bloque «LAS REGLAS DE CADA TURNO»; las listas de reglas se mandan solo cuando cambia la tarea; el aviso de las señales llega una vez, al abrir la sesión | 2, 6 | EP-005·HU-025 |
| 4 | `cambiar-codigo` se parte en pruebas, código y configuración, según la ruta y el tipo del archivo que se escribe | 3, 6 | EP-005·HU-026 |
| 5 | El núcleo llega completo al abrir la sesión; después de un resumen (`SessionStart` con origen `compact`) llegan otra vez el núcleo, `responder` y las reglas ya entregadas | 4, 5, 6 | EP-005·HU-027 |""")

cambiar("""**Resultado:** «ratifica, aclara, amplía, modifica la idea o cambia lo que se construye».

**Lo que suma al análisis principal:** «la frase que se agrega a la redacción del principal, escrita para leerse dentro de ella»""",
        """**Resultado:** cambia lo que se construye.

**Lo que suma al análisis principal:** Las reglas le llegan al agente en el momento en que va a actuar, según lo que va a hacer y una sola vez por sesión; con cada mensaje solo llegan las de responder, el núcleo llega completo y lo entregado vuelve después de cada resumen de la conversación.""")

io.open(P, "w", encoding="utf-8", newline="\n").write(t)
print("ok")
