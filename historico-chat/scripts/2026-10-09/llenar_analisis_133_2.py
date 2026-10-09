# -*- coding: utf-8 -*-
"""Escribe lo acordado y completa las secciones del análisis 2 del pendiente 133."""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
P = os.path.join(RAIZ, "historico-chat", "resumenes", "2026-10-05", "pendientes",
                 "133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje", "analisis-2.md")
R = "../../../../../"
EP = R + "documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/"
HU26 = EP + ("HU-026-las-reglas-de-cambiar-codigo-llegan-partidas-segun-lo-que-se-toca/"
             "HU-026-las-reglas-de-cambiar-codigo-llegan-partidas-segun-lo-que-se-toca.md")

t = io.open(P, encoding="utf-8").read()


def entre(desde, hasta, cuerpo):
    global t
    i = t.index(desde)
    j = t.index(hasta, i + len(desde))
    t = t[:i] + cuerpo.rstrip() + "\n\n" + t[j:]


def cambiar(viejo, nuevo):
    global t
    assert viejo in t, viejo[:60]
    t = t.replace(viejo, nuevo, 1)


cambiar("""1. «tema»: «lo que se decidió» (turno «N»).

Siguen abiertas: «pregunta sin decidir, o "ninguna"».""",
        """1. Las reglas de cambiar código se reparten por temas: cada capítulo del estándar es un tema, y el agente sabe que si está haciendo una cosa le aplican unas reglas y si está haciendo otra, otras. Cada tipo de archivo recibe solo los temas que toca, según una tabla en `base/tareas.md`; el archivo que no encaja en la tabla recibe todos los temas de código; las reglas generales llegan una vez a todo archivo de código. Reemplaza los tres grupos del acuerdo 3 del análisis 1 (turno 35).

Siguen abiertas: ninguna.""")

entre("### Cimiento: las reglas que aplican y las que chocan", "### El proyecto", """### Cimiento: las reglas que aplican y las que chocan

Aplican `02·F28` (el cambio baja en orden: la HU-026 pasa a su versión siguiente), `13·DOC26` (el pendiente pasa a su versión siguiente) y `20·M10` (cambia `base/tareas.md`). No choca ninguna.""")

entre("### El proyecto: lo que existe, lo que funciona y lo que falta", "### Lo aprendido", """### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| Las reglas de `cambiar-codigo` | 128 reglas, 67 KB, en 21 capítulos. Llegan en unas 10 entregas, todas, sin importar el archivo |
| La entrega por acción | `core/herramientas/entrega_de_reglas.py` (HU-025) elige la tarea con la columna de acciones de `base/tareas.md`; `escribe otro` no distingue tipos de archivo |
| La HU-026 | Dice tres tareas: pruebas, código y configuración. Sin empezar |""")

entre("### Lo aprendido: señales, lecciones y análisis anteriores", "### El entorno", """### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Análisis 1 de este pendiente, acuerdo 3 | Partir en tres grupos. El acuerdo 1 de este análisis lo afina: por temas |""")

cambiar("""| Proyectos que heredan | «tipo de versión según `20·M10`, y si aplica `02·F22`» |
| Normas y leyes | «cuáles aplican, o "ninguna"» |
| Herramientas | «qué condiciona lo que se va a construir» |""",
        """| Proyectos que heredan | MENOR (`20·M10`): no les pide hacer nada |
| Normas y leyes | Ninguna |
| Herramientas | El enganche de antes de la acción conoce la ruta del archivo que se escribe; con eso se elige el tema |""")

i = t.index("| Caso | Dónde se presenta")
j = t.index("\n---", i)
t = t[:i] + """| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Un archivo que no encaja en la tabla | Cualquier proyecto, cualquier lenguaje | Se queda sin sus reglas | Acuerdo 1: recibe todos los temas de código |
| Un archivo que toca varios temas | Una vista que valida y guarda | Le faltan reglas | Acuerdo 1: la tabla le da todos sus temas |
| Otros lenguajes y marcos | Proyectos que no son Django | La tabla no los reconoce | Acuerdo 1: sin patrón, todos los temas |
| Comandos de consola que escriben código | `sed`, `python -c` | No hay ruta clara | No cambia: la acción de consola sigue en `correr-comando` |
""" + t[j:]

entre("## Propuesta final", "## Lecciones aprendidas", f"""## Propuesta final: hallazgo y pendiente V3, épica y HU

### Hallazgo V2. Partir `cambiar-codigo` se hace por temas

| Campo | Valor |
|---|---|
| Qué pasó | El análisis 1 dijo partir `cambiar-codigo` en pruebas, código y configuración, sin decir cómo repartir sus 128 reglas. Se decidió repartirlas por temas: cada capítulo es un tema y cada tipo de archivo recibe los suyos |
| Por qué importa | Cada acción sobre código trae solo lo que le aplica, con una sola propuesta del estándar |

### Pendiente V3. Las reglas llegan cuando se actúa, una sola vez, y las de código por temas

| Campo | Valor |
|---|---|
| De dónde sale | El hallazgo V2 de H-1 del 2026-10-05 y el hallazgo V2 de H-6 del 2026-10-09: partir `cambiar-codigo` se hace por temas |
| El problema | Además de lo de la versión 2: las reglas de código llegan todas, sin importar qué archivo se escribe |
| Por qué importa | El agente recibe reglas que no aplican a lo que hace, y tarda unas 10 entregas en tener las que sí |

### Épica y HU que salen del análisis

Sigue en la [EP-005: automatismos que no dependen de que alguien se acuerde]({EP}epica.md). La [HU-026: las reglas de cambiar código llegan partidas según lo que se toca]({HU26}) pasa a su versión siguiente: por temas en vez de tres grupos.

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | HU-026 | Las reglas de cambiar código llegan partidas según lo que se toca | Las reglas de código llegan todas, sin importar el archivo | HU-025 | La HU-025 ya entrega por acción | 3 y 4 |""")

cambiar("""| 1 | «lección» | Funcionó / Falló | «S-NNN» | «complementa R-n» / «nueva R-n» / «no aplica» |""",
        """| 1 | Medir antes de proponer cómo partir: contar reglas y KB por capítulo mostró el tamaño real del problema | Funcionó | Se escribe al aprobar | Complementa R-2 |""")

cambiar("""| 1 | Pasar el pendiente a su versión siguiente | `13·DOC26` | Este análisis, de una y sin fase: `«ruta del pendiente.md»`, hecho el «fecha» |
| 2 | «qué hay que hacer» | «número» | «épica y HU, con su título y su enlace» |""",
        """| 1 | Pasar el pendiente a su versión siguiente | `13·DOC26` | Este análisis, de una y sin fase: `historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/pendiente.md` |
| 2 | Pasar la HU-026 a su versión siguiente: por temas | `02·F28` | Este análisis, de una y sin fase: `documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-026-las-reglas-de-cambiar-codigo-llegan-partidas-segun-lo-que-se-toca/HU-026-las-reglas-de-cambiar-codigo-llegan-partidas-segun-lo-que-se-toca.md` |
| 3 | `base/tareas.md` trae la tabla de temas: qué capítulos recibe cada tipo de archivo, y que sin patrón recibe todos los de código. Propuesta del agente para la tabla: pruebas (`tests*`, `test_*`, `*.spec.*`) → 08; datos (`models*`, `migrations/`, `*.sql`) → 03, 12, 15; servidor (`views*`, `forms*`, `urls*`, `api*`, `services*`) → 04, 05, 06; interfaz (`*.html`, `*.css`, `*.js`, `*.ts`, `templates/`, `static/`) → 17; configuración (`settings*`, `*.env*`, `*.yml`, `*.toml`, `Dockerfile`, `requirements*`, `package.json`) → 10, 11, 18, 19; procesos (`tasks*`, `jobs*`) → 21; todo código además 07, 14, 16 y las generales 00, 01, 02 | 1 | EP-005·HU-026 |
| 4 | `entrega_de_reglas.py` elige los temas por la ruta del archivo con esa tabla, y entrega solo las reglas de esos capítulos | 1 | EP-005·HU-026 |""")

cambiar("""**Resultado:** «ratifica, aclara, amplía, modifica la idea o cambia lo que se construye».

**Lo que suma al análisis principal:** «la frase que se agrega a la redacción del principal, escrita para leerse dentro de ella»""",
        """**Resultado:** modifica la idea.

**Lo que suma al análisis principal:** Las reglas de código llegan por temas: cada tipo de archivo recibe solo los capítulos que toca, y el que no encaja recibe todos.""")

io.open(P, "w", encoding="utf-8", newline="\n").write(t)
print("ok")
