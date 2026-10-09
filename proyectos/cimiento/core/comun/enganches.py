"""El catálogo de los enganches que instala Cimiento, en un solo lugar.

Vivía en `herramientas/instalar.py`, y `validadores/checklist.py` y
`enganches/sesion.py` lo importaban de ahí: los tres se necesitaban entre sí y
la carga solo cerraba en un orden (análisis 1 del pendiente 116, fila 23). Acá
no depende de nadie.

Es la lista de lo que **existe**. Qué tiene prendido cada proyecto lo decide su
configuración en la pantalla «Proyectos» (acuerdo 12 del mismo análisis). Desde la
`EP-025·HU-032`, cada momento y cada revisión de git tiene acá su nombre para
suspenderlo; lo que no conviene suspender lleva su motivo en `NO_CONVIENE`.
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

# `EP-025·HU-032` · El nombre fijo de cada momento, para suspenderlo desde Cimiento
# (análisis 1 del pendiente 149, acuerdo 1). Se suspende el momento, no el guion:
# cuatro guiones corren en dos momentos. El nombre sale de `(evento, guion)`, que
# Claude Code le dice a cada enganche, y no de un campo más en `HOOKS_CLAUDE`, que
# el instalador, el desinstalador y el checklist desarman en cinco.
FRENO = "freno"
MOMENTOS = {
    ("PostToolUse", "hook_md.py"): "enlaces-al-escribir",
    ("SessionStart", "hook_sesion.py"): "estandar-al-abrir",
    ("UserPromptSubmit", "hook_historico.py"): "historico-del-usuario",
    ("Stop", "hook_historico.py"): "historico-del-agente",
    ("UserPromptSubmit", "hook_analisis.py"): "analisis-en-curso",
    ("UserPromptSubmit", "hook_checklist.py"): "instalacion",
    ("UserPromptSubmit", "hook_reglas.py"): "reglas-de-cada-turno",
    ("UserPromptSubmit", "hook_acuerdos.py"): "acuerdos",
    ("SessionStart", "hook_recuerdos.py"): "memoria-al-abrir",
    ("PostToolUse", "hook_recuerdos.py"): "memoria-al-escribir",
    ("SessionStart", "hook_resumen.py"): "resumen-al-abrir",
    ("UserPromptSubmit", "hook_resumen.py"): "resumen-en-cada-mensaje",
    ("UserPromptSubmit", "hook_senales.py"): "senales",
    ("PostToolUse", "hook_relacionadas.py"): "reglas-relacionadas",
    ("Stop", "hook_turno.py"): "registro-del-turno",
    ("Stop", "hook_redaccion.py"): "redaccion",
    ("Stop", "hook_presupuesto.py"): "consumo-al-terminar",
    ("UserPromptSubmit", "hook_presupuesto.py"): "consumo-en-cada-mensaje",
    ("PostToolUse", "hook_checkpoint.py"): "checkpoint",
    ("PostToolUse", "hook_veredicto.py"): "veredicto",
    ("PostToolUse", "hook_rutas.py"): "rutas",
    ("PostToolUse", "hook_externo.py"): "lo-que-llega-de-afuera",
    # Los dos del freno se suspenden juntos, como hasta ahora; el núcleo lo sigue frenando.
    ("PreToolUse", "hook_antes.py"): FRENO,
    ("PostToolUse", "hook_despues.py"): FRENO,
}

# Las revisiones de git, por la orden de `validar.py` que las corre (acuerdo 4):
# «versionado» se suspende igual en `pre-commit` que en `pre-push`.
REVISIONES_GIT = {
    "commit": ("git-mensaje", "Revisa el mensaje del commit"),
    "versionado": ("git-versionado", "Que no entren secretos ni artefactos"),
    "marcas": ("git-marcas", "Que no suban las marcas de redacción"),
    "plan": ("git-plan", "Lo que entra contra el plan aprobado"),
    "sesiones": ("git-sesiones", "Que el commit no se lleve el trabajo de otra sesión"),
    "pruebas": ("git-pruebas", "La revisión de pruebas al día"),
    "estandar": ("git-enlaces", "Enlaces rotos e índices, antes de publicar"),
    "ejecutable": ("git-ejecutable", "Quién hace cumplir cada regla del núcleo, antes de publicar"),
    "tareas": ("git-tareas", "A qué tareas aplica cada regla, antes de publicar"),
    "metareglas": ("git-metareglas", "Las reglas contra su molde, antes de publicar"),
    "internas": ("git-pruebas-del-estandar", "Si hay commits que las pruebas del estándar no vieron"),
    "estacion": ("git-estacion", "Anota el commit en el estado de la fase"),
}

# Lo que no conviene suspender, y por qué (acuerdo 2): se puede, pero la pantalla lo advierte.
NO_CONVIENE = {
    "historico-del-usuario": "Deja de guardar lo que escribe el usuario: la sesión se pierde al borrar el chat.",
    "historico-del-agente": "Deja de guardar lo que responde el agente: la sesión se pierde al borrar el chat.",
    "reglas-de-cada-turno": "Las reglas no se cargan al abrir: sin él, el agente trabaja sin ellas.",
    "registro-del-turno": "Sin él, un commit puede llevarse el trabajo de otra sesión sin aviso.",
    "lo-que-llega-de-afuera": "Lo que llega de una página o un archivo deja de marcarse como dato, no orden.",
    FRENO: "Deja pasar lo que el plan no declara. El núcleo se sigue frenando.",
    "git-versionado": "Pueden entrar al repositorio claves o archivos que no van.",
}


def suspendibles():
    """`[(nombre, qué hace, por qué no conviene o "")]`: los momentos y después las revisiones de git."""
    que_hace = {}
    for evento, _filtro, guion, mensaje, _argumentos in HOOKS_CLAUDE:
        nombre = MOMENTOS[(evento, guion)]
        que_hace.setdefault(nombre, "Revisando la acción contra el plan, antes y después" if nombre == FRENO
                            else mensaje.rstrip("."))
    que_hace.update((nombre, texto) for nombre, texto in REVISIONES_GIT.values())
    return [(nombre, texto, NO_CONVIENE.get(nombre, "")) for nombre, texto in que_hace.items()]


# Pendiente 143, fase A · Lo que corre al cerrar el turno y nadie espera: se
# instala con `async`, y la respuesta deja de esperar cerca de 6 s. Su salida se
# descarta, y ninguno la necesita: lo que el turno siguiente lee queda en
# archivos, y la medición de la redacción la repite `hook_reglas.py`.
EN_SEGUNDO_PLANO = frozenset({
    ("Stop", "hook_historico.py"), ("Stop", "hook_turno.py"),
    ("Stop", "hook_redaccion.py"), ("Stop", "hook_presupuesto.py")})

# Los 4 archivos de configuración del proyecto. Los pone el instalador y el
# checklist revisa que estén; los dos los leen de acá (`20·M2`).
CONFIG_AGENTE = ["stack.md", "dominio.md", "mapeo-nombres.md",
                 "marco-normativo.md"]

# Lo que no es del repositorio: configuración local y el estado de trabajo que
# escriben los enganches. El instalador la pone y el checklist la revisa.
IGNORADOS = ["CLAUDE.md", ".agente/", "historico-chat/.tocado/"]
