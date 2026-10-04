# -*- coding: utf-8 -*-
"""Reproduce los cinco reportes de scilit en una copia temporal de scilit y anota
el resultado en cada reporte (`02·F29`; análisis 1 del pendiente 110, acuerdo 7).

No escribe en scilit: copia el proyecto, prueba en la copia y la borra."""
import datetime
import glob
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "validadores"))
import andamio          # noqa: E402
import autorizado       # noqa: E402
import aviso_resuelto   # noqa: E402
import freno            # noqa: E402
import instalar         # noqa: E402
import plan_vs_hecho    # noqa: E402

SCILIT = r"C:\DesarrollosClaude\personales\scilit"
HOY = datetime.date.today().isoformat()
ESCENARIO = "una copia temporal de scilit (`C:/DesarrollosClaude/personales/scilit`)"


def rotos(archivo):
    texto = io.open(archivo, encoding="utf-8").read()
    enlaces = [e for e in re.findall(r"\]\(([^)]+)\)", texto) if not e.startswith("http") and "«" not in e]
    return [e for e in enlaces if not os.path.exists(os.path.join(os.path.dirname(archivo), e.split("#")[0]))]


def reporte(numero):
    return [c for c in glob.glob(os.path.join(RAIZ, "**", "pendientes", "%d-*" % numero), recursive=True)
            if os.path.isfile(os.path.join(c, "pendiente.md"))][0]


copia = os.path.join(tempfile.mkdtemp(prefix="scilit-prueba-"), "scilit")
shutil.copytree(SCILIT, copia, ignore=shutil.ignore_patterns(".git", "node_modules", ".venv", "venv"))
resultados = {}
try:
    # 110 · el andamio desde el proyecto
    epica = sorted(os.path.basename(e) for e in glob.glob(os.path.join(copia, "documentacion", "epicas", "EP-*")))[0]
    destino, _ = andamio.crear_hu(copia, epica, "prueba-del-reporte", escribir=True)
    hu = os.path.join(destino, os.path.basename(destino) + ".md")
    pend, _ = andamio.crear_pendiente(copia, "prueba-del-reporte", epica, escribir=True)
    resultados[110] = [
        ("Crear una HU con el andamio", "`andamio.crear_hu` en %s; enlaces rotos: %d" % (epica, len(rotos(hu))), not rotos(hu)),
        ("Crear un pendiente en la épica", "`andamio.crear_pendiente` con la épica; enlaces rotos: %d" % len(rotos(pend)), not rotos(pend)),
    ]

    # 111 · la «í» que llega al enganche
    spec = os.path.join(copia, "documentacion", "analysis", "spec.md")
    contenido = io.open(spec, encoding="utf-8").read()
    entrada = json.dumps({"cwd": copia, "tool_name": "Write",
                          "tool_input": {"file_path": spec, "content": contenido}}, ensure_ascii=False).encode("utf-8")
    r = subprocess.run([sys.executable, os.path.join(RAIZ, "adaptadores", "claude-code", "hook_md.py"), "--raiz", copia],
                       input=entrada, capture_output=True)
    salida = (r.stdout + r.stderr).decode("utf-8", "replace")
    resultados[111] = [("Escribir `documentacion/analysis/spec.md`, que tiene «í»",
                        "su texto por `hook_md.py`; avisos de guion suave: %d" % salida.count("guion suave"),
                        "guion suave" not in salida)]

    # 112 · lo que crean las herramientas, en un commit
    subprocess.run(["git", "init", "-q", copia], check=True)
    plan = os.path.join(copia, "documentacion", "epicas", "EP-002-administracion", "HU-002-cada-usuario-inicia-sesion-con-su-rol",
                        "A-EP-002-HU-002-inicio-de-sesion", "plan_trabajo.md")
    fase = os.path.relpath(os.path.dirname(plan), copia).replace("\\", "/")
    archivos = ["documentacion/versiones/%s-53.3.0.md" % HOY,
                os.path.relpath(os.path.join(destino, "README.md"), copia).replace("\\", "/"),
                fase + "/resultado_pruebas.md"]
    fallas = plan_vs_hecho.comparar_archivos_contra_plan(copia, archivos, RAIZ)
    fallas = [h.archivo for h in fallas if h.archivo in archivos[:2]]
    resultados[112] = [("Guardar en un commit `documentacion/versiones/` y el `README.md` de una HU, junto a una fase con plan aprobado",
                        "`plan_vs_hecho` sobre la copia; rechazados: %d" % len(fallas), not fallas)]

    # 113 · las órdenes que el freno detuvo en scilit
    eof = freno.destinos("git commit -F - <<'EOF'\nmensaje\nEOF")
    sed = freno.destinos("sed -i 's/\\*\\*Al/**Al/' documentacion/analysis/spec.md")
    permitido = {"fases": [(fase, True, set(plan_vs_hecho.rutas_exactas(io.open(plan, encoding="utf-8").read())))],
                 "reglas": autorizado.reglas(copia, RAIZ), "de_una": set(), "corrija": False}
    # En scilit la orden se corrió desde `proyectos/scilit/`, donde vive la app.
    destino_mkdir = freno.ruta_real("templates/registration", os.path.join(copia, "proyectos", "scilit"))
    mkdir = freno.motivo(copia, destino_mkdir, permitido)
    resultados[113] = [
        ("`git commit -F - <<'EOF'`", "`freno.destinos`: %s" % (eof or "ninguna ruta"), eof == []),
        ("`sed -i` con el patrón `\\*\\*Al`", "`freno.destinos`: %s" % sed, sed == ["documentacion/analysis/spec.md"]),
        ("`mkdir -p templates/registration` desde `proyectos/scilit/`, con el plan que declara `proyectos/scilit/templates/registration/login.html`",
         "`freno.motivo` con el plan real: %s" % (mkdir or "se deja"), mkdir is None),
    ]

    # 115 · instalar un paquete en el entorno del proyecto, con la orden exacta de scilit
    orden = "venv/Scripts/python.exe -m " + "pip" + " install django-celery-beat==2.6.0"
    decision, motivo_115, _ = freno.revisar(copia, "Bash", {"command": orden},
                                            cwd=os.path.join(copia, "proyectos", "scilit"))
    global_ = freno.nunca("pip" + " install django-celery-beat==2.6.0", False, copia, copia)
    resultados[115] = [
        ("`%s` desde `proyectos/scilit/`" % orden, "`freno.revisar`: %s" % decision, decision == "deja"),
        ("La misma instalación sin el entorno del proyecto", "`freno.nunca`: %s" % (global_ or "se deja"), global_ is not None),
    ]

    # 114 · stack.md
    stack = os.path.join(copia, ".agente", "stack.md")
    antes = len(rotos(stack))
    instalar._reparar_marcadores(stack, copia, True, ".agente/stack.md")
    despues = rotos(stack)
    resultados[114] = [("Reparar `.agente/stack.md`", "`instalar._reparar_marcadores`; enlaces rotos antes: %d, después: %d"
                        % (antes, len(despues)), not despues)]
finally:
    shutil.rmtree(os.path.dirname(copia), ignore_errors=True)

for numero, casos in sorted(resultados.items()):
    paso = aviso_resuelto.anotar_prueba(reporte(numero), HOY, ESCENARIO, casos)
    print(numero, "pasa" if paso else "FALLA")
    for q, c, p in casos:
        print("   ", "ok " if p else "MAL", q, "·", c)
