"""Puente a la ruta nueva — el enganche vive en `adaptadores/claude-code/`.

La v26.0.0 movió los enganches de la herramienta a `adaptadores/claude-code/`
sin dejar nada acá, y toda instalación que todavía llamaba esta ruta fallaba
con código 2 — que para la herramienta significa **bloquear el mensaje del
usuario**. Este puente reenvía la llamada tal cual (argumentos, entrada y
código de salida) para que ninguna instalación rezagada se bloquee. El
instalador reescribe la ruta al volver a correr; entonces este archivo deja
de usarse, pero se queda: es lo que evita el bloqueo la próxima vez.
"""
import os
import subprocess
import sys

_NUEVO = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), os.pardir,
    "adaptadores", "claude-code", os.path.basename(__file__)))

raise SystemExit(subprocess.call([sys.executable, _NUEVO] + sys.argv[1:]))
