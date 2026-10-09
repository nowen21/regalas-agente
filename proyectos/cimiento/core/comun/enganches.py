"""El catálogo de los enganches que instala Cimiento, en un solo lugar.

Vivía en `herramientas/instalar.py`, y `validadores/checklist.py` y
`enganches/sesion.py` lo importaban de ahí: los tres se necesitaban entre sí y
la carga solo cerraba en un orden (análisis 1 del pendiente 116, fila 23). Acá
no depende de nadie.

Es la lista de lo que **existe**. Qué tiene prendido cada proyecto lo decide su
configuración en la pantalla «Proyectos» (acuerdo 12 del mismo análisis); lo que
este catálogo marca es lo que ningún proyecto puede suspender.
"""

# Los enganches de git, por su nombre. Sus plantillas viven con el instalador,
# que es quien las escribe.
ENGANCHES_GIT = ("commit-msg", "pre-commit", "pre-push", "post-commit")

# Enganches de Claude Code: (evento, matcher, guion, mensaje, argumentos).
# `matcher` en None = el evento no filtra por herramienta (SessionStart).
# `argumentos` deja que un mismo guion sirva a dos eventos con papeles distintos,
# como el histórico: uno anota al usuario y el otro al agente.
HOOKS_CLAUDE = [
    ("PostToolUse", "Write|Edit", "hook_md.py",
     "Revisando los enlaces del proyecto...", ""),
    ("SessionStart", None, "hook_sesion.py",
     "Revisando el estándar...", ""),
    ("UserPromptSubmit", None, "hook_historico.py",
     "Anotando en el histórico...", "--modo usuario"),
    ("Stop", None, "hook_historico.py",
     "Anotando en el histórico...", "--modo agente"),
    # `EP-023 · HU-001 · fase B`: la conversación pasa sola al análisis
    # prendido. Al cerrar el turno no hay enganche propio: la respuesta la pasa
    # `hook_historico.py` apenas la escribe, porque dos enganches del mismo
    # evento corren a la vez y el del análisis copiaba antes de que la
    # respuesta existiera (H-9 de la sesión del 2026-10-01).
    ("UserPromptSubmit", None, "hook_analisis.py",
     "Revisando el análisis en curso...", "--modo mensaje"),
    ("UserPromptSubmit", None, "hook_checklist.py",
     "Revisando la instalación del agente...", ""),
    # Al abrir la sesión no se cargan las reglas: la herramienta acepta 10.000
    # caracteres por enganche (`EP-005 · HU-009 · CA-04`). Este enganche
    # entrega con cada mensaje las reglas de las tareas que pide
    # (`recuperar.py`), recuerda las de cada turno, y devuelve al turno
    # siguiente la cuenta que `hook_redaccion.py` imprime donde nadie la ve.
    ("UserPromptSubmit", None, "hook_reglas.py",
     "Recordando las reglas de cada turno...", ""),
    # `EP-023 · HU-002 · CA-04`: los acuerdos de la fase en curso y del
    # análisis prendido llegan con cada mensaje, en un enganche propio porque
    # el tope es por enganche y el de las reglas va casi lleno.
    ("UserPromptSubmit", None, "hook_acuerdos.py",
     "Trayendo los acuerdos de lo que se trabaja...", ""),
    ("SessionStart", None, "hook_recuerdos.py",
     "Recogiendo la memoria del agente...", ""),
    ("PostToolUse", "Write|Edit", "hook_recuerdos.py",
     "Recogiendo la memoria del agente...", ""),
    ("SessionStart", None, "hook_resumen.py",
     "Preparando el resumen de la sesión...", "--modo inicio"),
    ("UserPromptSubmit", None, "hook_resumen.py",
     "Revisando el resumen de la sesión...", "--modo aviso"),
    ("UserPromptSubmit", None, "hook_senales.py",
     "Revisando las señales del proyecto...", ""),
    ("PostToolUse", "Write|Edit", "hook_relacionadas.py",
     "Buscando las reglas relacionadas...", ""),
    # `EP-005 · HU-020`: al terminar el turno, el registro anota lo que
    # cambió, mire quien lo mire, para que la comprobación de sesiones no tenga
    # el hueco por el que entraban líneas ajenas.
    ("Stop", None, "hook_turno.py",
     "Anotando lo que tocó este turno...", ""),
    # `EP-005·HU-012`: al cerrar el turno, se mide como quedo escrito lo que
    # el agente acaba de decir. Tres reglas del nucleo hablan de eso y ninguna
    # tenia quien la hiciera cumplir. Mide y no detiene: cuando esto corre, el
    # texto ya salio, asi que lo unico que se puede hacer es dejarlo a la vista.
    ("Stop", None, "hook_redaccion.py",
     "Midiendo como quedo escrito el turno...", ""),
    ("Stop", None, "hook_presupuesto.py",
     "Sumando el consumo de la sesión...", ""),
    ("UserPromptSubmit", None, "hook_presupuesto.py",
     "Midiendo el consumo de la sesión...", "--modo aviso"),
    ("PostToolUse", "Write|Edit", "hook_checkpoint.py",
     "Revisando el checkpoint de la fase...", ""),
    ("PostToolUse", "Write|Edit", "hook_veredicto.py",
     "Copiando el veredicto de la fase...", ""),
    # `EP-005 · HU-018`: avisa si el archivo cayó fuera del proyecto. La regla
    # ya existía (`04·S9`) y se incumplió cuatro días seguidos, porque la
    # herramienta ofrece una carpeta temporal y la nombra como el sitio
    # recomendado: el camino cómodo apunta al lado contrario.
    ("PostToolUse", "Write|Edit", "hook_rutas.py",
     "Mirando dónde quedó lo que se escribió...", ""),
    # El portero (`EP-005 · HU-015`): lo que llega de afuera llega marcado.
    # El filtro es regex; el programa vuelve a decidir por si deja pasar de más.
    ("PostToolUse", "WebFetch|WebSearch|Read|mcp__.*", "hook_externo.py",
     "Marcando lo que llegó de afuera...", ""),
    # `EP-005 · HU-023 · RN-10`: ninguna escritura sale del proyecto. Obligar a
    # leer las reglas antes de actuar se quitó el 2026-09-29: llenaba la
    # conversación de lecturas y no hacía cumplir nada.
    # `EP-023 · HU-007 · CA-02`: el freno corre antes de toda acción, sin filtro
    # de herramienta, y después de cada orden de consola compara lo que cambió.
    ("PreToolUse", None, "hook_antes.py",
     "Revisando la acción contra el plan y lo autorizado...", "--modo accion"),
    ("PostToolUse", "Bash|PowerShell", "hook_despues.py",
     "Comparando lo que cambió con el plan...", ""),
]

# Pendiente 143, fase A · Lo que corre al cerrar el turno y nadie espera: se
# instala con `async`, y la respuesta deja de esperar cerca de 6 s. Su salida se
# descarta, y ninguno la necesita: lo que el turno siguiente lee queda en
# archivos, y la medición de la redacción la repite `hook_reglas.py`.
EN_SEGUNDO_PLANO = frozenset({
    ("Stop", "hook_historico.py"), ("Stop", "hook_turno.py"),
    ("Stop", "hook_redaccion.py"), ("Stop", "hook_presupuesto.py")})

# Lo que ningún ajuste del proyecto suspende (acuerdo 12): el histórico de la
# conversación, que además tapa las claves antes de guardarla (`00·N6`).
NO_SE_SUSPENDEN = ("hook_historico.py",)

# Los 4 archivos de configuración del proyecto. Los pone el instalador y el
# checklist revisa que estén; los dos los leen de acá (`20·M2`).
CONFIG_AGENTE = ["stack.md", "dominio.md", "mapeo-nombres.md",
                 "marco-normativo.md"]

# Lo que no es del repositorio: configuración local y el estado de trabajo que
# escriben los enganches. El instalador la pone y el checklist la revisa.
IGNORADOS = ["CLAUDE.md", ".agente/", "historico-chat/.tocado/"]
