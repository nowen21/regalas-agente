# -*- coding: utf-8 -*-
"""Corre los diez enganches que pasaron a leer la entrada en UTF-8, con una
entrada con tildes, y dice si alguno se cae (análisis 1 del pendiente 110, fila 4)."""
import json
import os
import subprocess
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
ENGANCHES = ["hook_md", "hook_checkpoint", "hook_externo", "hook_presupuesto", "hook_redaccion",
             "hook_relacionadas", "hook_resumen", "hook_rutas", "hook_turno", "hook_veredicto"]
entrada = json.dumps({"cwd": RAIZ, "tool_name": "Read", "tool_input": {"file_path": "README.md"},
                      "prompt": "aquí"}, ensure_ascii=False).encode("utf-8")
for n in ENGANCHES:
    r = subprocess.run([sys.executable, os.path.join(RAIZ, "adaptadores", "claude-code", n + ".py"),
                        "--raiz", RAIZ], input=entrada, capture_output=True)
    print(n, r.returncode, "se cayó" if b"Traceback" in r.stderr else "bien")
