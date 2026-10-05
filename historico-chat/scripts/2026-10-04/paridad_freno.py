# -*- coding: utf-8 -*-
"""Compara los módulos viejos del grupo «freno» (`freno`, `plan_vs_hecho`,
`acuerdos`, `autorizado`, `origen`, `analisis_en_curso`, `resumen`,
`aviso_resuelto`, `analisis`, `flujo`, `recuperar`, `andamio` y `cerrar`) con sus
clases nuevas (sesión del 2026-10-04, análisis 1 del pendiente 116), sobre este
repositorio y los proyectos dados. En los proyectos reales solo lee: lo que
escribe a disco se compara en copias dentro de carpetas temporales.

    python paridad_freno.py [--partes freno,curso,...] [proyecto ...]
"""
import datetime
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "validadores"))
sys.path.insert(0, os.path.join(RAIZ, "proyectos", "cimiento"))

import acuerdos as v_acuerdos  # noqa: E402
import analisis as v_analisis  # noqa: E402
import analisis_en_curso as v_curso  # noqa: E402
import andamio as v_andamio  # noqa: E402
import autorizado as v_autorizado  # noqa: E402
import aviso_resuelto as v_aviso  # noqa: E402
import cerrar as v_cerrar  # noqa: E402
import flujo as v_flujo  # noqa: E402
import freno as v_freno  # noqa: E402
import origen as v_origen  # noqa: E402
import pendientes as v_pendientes  # noqa: E402
import plan_vs_hecho as v_plan  # noqa: E402
import recuperar as v_recuperar  # noqa: E402
import resumen as v_resumen  # noqa: E402
from core.enganches.acuerdos import Acuerdos  # noqa: E402
from core.enganches.analisis_en_curso import AnalisisEnCurso  # noqa: E402
from core.enganches.autorizado import Autorizaciones  # noqa: E402
from core.enganches.aviso_resuelto import AvisoResuelto  # noqa: E402
from core.enganches.freno import Freno  # noqa: E402
from core.enganches.origen import LectorDeAnalisis, OrigenDeCadaPunto  # noqa: E402
from core.enganches.plan_vs_hecho import PlanContraLoHecho, PlanDeTrabajo  # noqa: E402
from core.enganches.resumen import Resumen  # noqa: E402
from core.herramientas.andamio import Andamio  # noqa: E402
from core.herramientas.cerrar import CerradorDePendientes  # noqa: E402
from core.herramientas.recuperar import RecuperadorDeReglas  # noqa: E402
from core.validadores.analisis import AnalisisAprobados  # noqa: E402
from core.validadores.flujo import PlanDeLaFase  # noqa: E402

PROYECTOS = ["C:/DesarrollosClaude/personales/shopnest-mesa", "c:/wamp64/www/proyectos/personales/agro-system"]
ANALISIS_EN_CURSO = ("historico-chat/resumenes/2026-10-04/pendientes/"
                     "116-el-codigo-de-cimiento-se-repite-en-vez-de-reusarse/analisis-1.md")


# ── comparar ──────────────────────────────────────────────────────────────

def ruta(r, raiz):
    r = r if os.path.isabs(r) else os.path.join(raiz, r)
    return os.path.normcase(os.path.realpath(r))


def clave(h, raiz):
    return (ruta(h.archivo, raiz), h.linea, h.severidad, h.mensaje)


def n(obj):
    """El objeto con cada ruta absoluta escrita igual, venga de `abspath` o de `realpath`."""
    if isinstance(obj, str):
        return os.path.normcase(os.path.realpath(obj)) if len(obj) > 3 and os.path.isabs(obj) else obj
    if isinstance(obj, dict):
        return {n(k): n(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return type(obj)(n(x) for x in obj)
    if isinstance(obj, (set, frozenset)):
        return {n(x) for x in obj}
    return obj


def igual(nombre, a, b):
    a, b = n(a), n(b)
    print("%-44s %s" % (nombre, "IGUAL" if a == b else "DISTINTO"))
    if a != b:
        print("   viejo:", str(a)[:600])
        print("   nuevo:", str(b)[:600])
    return a == b


def hallazgos(nombre, viejos, nuevos, raiz):
    a = sorted(clave(h, raiz) for h in viejos)
    b = sorted(clave(h, raiz) for h in nuevos)
    ok = a == b
    print("%-44s %s" % ("%s (%d)" % (nombre, len(a)), "IGUAL" if ok else "DISTINTO"))
    if not ok:
        for x in sorted(set(a) - set(b))[:5]:
            print("   solo viejo:", x)
        for x in sorted(set(b) - set(a))[:5]:
            print("   solo nuevo:", x)
    return ok


def arbol(carpeta):
    """`{ruta relativa: texto}` de todo lo que hay en la carpeta, sin `.git/`: sus
    objetos llevan la hora del commit y nunca coinciden entre dos copias."""
    salida = {}
    for actual, carpetas, archivos in os.walk(carpeta):
        carpetas[:] = [c for c in carpetas if c != ".git"]
        for nombre in archivos:
            r = os.path.join(actual, nombre)
            with open(r, "rb") as f:
                salida[os.path.relpath(r, carpeta).replace("\\", "/")] = f.read()
    return salida


def escribir(ruta_, texto):
    os.makedirs(os.path.dirname(ruta_), exist_ok=True)
    with io.open(ruta_, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def leer(ruta_):
    with io.open(ruta_, encoding="utf-8") as f:
        return f.read()


def git(repo, *args):
    subprocess.run(["git", "-C", repo, *args], capture_output=True, check=True)


def solo_md(origen, destino):
    """Copia los `.md` (y `VERSION`) de un proyecto, sin lo que no se recorre."""
    def ignorar(carpeta, nombres):
        fuera = {".git", "__pycache__", ".venv", "venv", "node_modules", "vendor", "proyectos"}
        return [x for x in nombres if x in fuera or (os.path.isfile(os.path.join(carpeta, x))
                                                     and not x.endswith(".md") and x != "VERSION")]
    shutil.copytree(origen, destino, ignore=ignorar)


# ── los validadores ───────────────────────────────────────────────────────

def de_validadores(raiz):
    ok = hallazgos("origen.validar", v_origen.validar(raiz), OrigenDeCadaPunto(raiz).validar(), raiz)
    ok &= igual("origen.revisar", sorted(v_origen.revisar(raiz)), sorted(OrigenDeCadaPunto(raiz).revisar()))
    a = AnalisisAprobados(raiz)
    ok &= hallazgos("analisis.validar", v_analisis.validar(raiz), a.validar(), raiz)
    ok &= igual("analisis.revisar", v_analisis.revisar(raiz), a.revisar())
    ok &= igual("analisis.recomendaciones", v_analisis.recomendaciones(raiz), a.recomendaciones())
    ok &= igual("analisis.copias", v_analisis.copias(raiz), a.copias())
    ok &= igual("analisis.fuera_de_la_lista", v_analisis.fuera_de_la_lista(raiz), a.fuera_de_la_lista())
    ok &= igual("analisis.de_forma_anterior", v_analisis.de_forma_anterior(raiz), a.de_forma_anterior())
    ok &= hallazgos("flujo.validar", v_flujo.validar(raiz), PlanDeLaFase(raiz).validar(), raiz)
    p = PlanContraLoHecho(raiz)
    ok &= hallazgos("plan.validar", v_plan.validar(raiz), p.validar(), raiz)
    ok &= hallazgos("plan.comparar_preparados", v_plan.comparar_preparados(raiz), p.comparar_preparados(), raiz)
    for rango in ("HEAD~1..HEAD", "HEAD~5..HEAD"):
        ok &= hallazgos("plan.comparar_rango %s" % rango, v_plan.comparar_rango(raiz, rango),
                        p.comparar_rango(rango), raiz)
    ok &= igual("plan.linea_resumen", v_plan.linea_resumen(raiz), p.linea_resumen())
    fases = v_plan.fases_de(raiz)
    ok &= igual("plan.fases_de (%d)" % len(fases), fases, p.fases_de())
    distintos = []
    for fase in fases:
        texto = leer(os.path.join(fase, "plan_trabajo.md"))
        if (v_plan.declarados(texto), v_plan.aprobacion(texto), v_plan.rutas_exactas(texto),
                v_plan.revisar_aprobado(texto), v_plan.aprobado_desde(texto)) != (
                PlanDeTrabajo.declarados(texto), PlanDeTrabajo.aprobacion(texto), PlanDeTrabajo.rutas_exactas(texto),
                PlanDeTrabajo.revisar_aprobado(texto), PlanDeTrabajo.aprobado_desde(texto)):
            distintos.append(fase)
        f = PlanContraLoHecho(raiz, fase=fase, desde="HEAD~3")
        pares = [(v_plan.comparar_casos(fase), f.comparar_casos(fase)),
                 (v_plan.pruebas_sin_declarar(fase, raiz), f.pruebas_sin_declarar(fase))]
        # `git diff` contra un commit tarda un segundo por fase: se compara en las últimas.
        if fase in fases[-6:]:
            pares.append((v_plan.comparar_archivos(fase, raiz, "HEAD~3"), f.comparar_archivos(fase, raiz, "HEAD~3")))
        for viejo, nuevo in pares:
            if sorted(clave(h, raiz) for h in viejo) != sorted(clave(h, raiz) for h in nuevo):
                distintos.append(fase)
    ok &= igual("plan por fase (%d)" % len(fases), distintos, [])
    if fases:
        ok &= hallazgos("plan.validar con fase y desde", v_plan.validar(raiz, fases[-1], "HEAD~2"),
                        PlanContraLoHecho(raiz, fase=fases[-1], desde="HEAD~2").validar(), raiz)
    return ok


# ── autorizado, acuerdos y el análisis en curso ───────────────────────────

RUTAS = ["historico-chat/resumenes/2026-10-04/tema.md", "historico-chat/2026-10-04-x.md", "src/a.py",
         "documentacion/versiones/2026-10-04-53.0.0.md", "documentacion/epicas/EP-001-x/HU-001-y/README.md",
         "validadores/freno.py", ".gitignore", "notas/x.md", "pendientes/README.md", "base/00-nucleo-blindado.md",
         "historico-chat/scripts/2026-10-04/x.py", "prompts/x.md", "./historico-chat/x.md", "memoria/x.db"]


def de_autorizado_y_acuerdos(raiz):
    viejas, nuevas = v_autorizado.reglas(raiz), Autorizaciones().reglas(raiz)
    ok = igual("autorizado.reglas (%d)" % len(viejas), viejas, nuevas)
    ok &= igual("autorizado.del_proyecto", v_autorizado.del_proyecto(raiz), Autorizaciones().del_proyecto(raiz))
    ok &= igual("autorizado.quien_autoriza", [v_autorizado.quien_autoriza(r, viejas) for r in RUTAS],
                [Autorizaciones.quien_autoriza(r, nuevas) for r in RUTAS])
    a = Acuerdos(raiz)
    fases = v_acuerdos.fases_en_curso(raiz)
    ok &= igual("acuerdos.fases_en_curso (%d)" % len(fases), fases, a.fases_en_curso())
    ok &= igual("acuerdos.de_la_fase", [v_acuerdos.de_la_fase(f) for f in fases], [a.de_la_fase(f) for f in fases])
    ok &= igual("acuerdos.del_analisis_prendido", v_acuerdos.del_analisis_prendido(raiz), a.del_analisis_prendido())
    for tope in (v_acuerdos.TOPE, 1200):
        ok &= igual("acuerdos.texto %d" % tope, v_acuerdos.texto(raiz, tope), a.texto(tope))
    todas = sorted(set(os.path.join(c, f) for c, _, fs in os.walk(os.path.join(raiz, "documentacion", "epicas"))
                       for f in fs) if os.path.isdir(os.path.join(raiz, "documentacion", "epicas")) else [])
    fases_todas = sorted({os.path.dirname(f) for f in todas if os.path.basename(f) == "plan_trabajo.md"})
    ok &= igual("acuerdos.en_curso (%d)" % len(fases_todas), [v_acuerdos.en_curso(f) for f in fases_todas],
                [a.en_curso(f) for f in fases_todas])
    return ok


def de_curso(raiz):
    c = AnalisisEnCurso(raiz)
    ok = igual("curso.leer_estado", v_curso.leer_estado(raiz), c.leer_estado())
    ok &= igual("curso.corrija_activo", v_curso.corrija_activo(raiz), c.corrija_activo())
    ok &= igual("curso.abiertos", v_curso.abiertos(raiz), c.abiertos())
    ok &= igual("curso.aviso", [v_curso.aviso(raiz), v_curso.aviso(raiz, "una nota")],
                [c.aviso(), c.aviso("una nota")])
    ok &= igual("curso.por_que_no_se_aprueba", v_curso.por_que_no_se_aprueba(raiz), c.por_que_no_se_aprueba())
    ok &= igual("curso.carpeta_del_pendiente", [v_curso.carpeta_del_pendiente(raiz, k) for k in (5, 103, 110, 116, 999)],
                [c.carpeta_del_pendiente(k) for k in (5, 103, 110, 116, 999)])
    estado = v_curso.leer_estado(raiz)
    if estado:
        ok &= igual("curso.conversacion", v_curso.conversacion(estado, raiz), c.conversacion(c.leer_estado()))
        ok &= igual("curso.ultimo_turno", v_curso.ultimo_turno(estado["transcripcion"]),
                    AnalisisEnCurso.ultimo_turno(estado["transcripcion"]))
    todos = v_analisis.analisis(raiz)
    distintos = []
    for r in todos:
        texto = v_curso.leer(r)
        viejo = (v_curso.faltantes(texto), v_curso.aporte(texto), v_curso.aprobado(r), v_curso.turno_aprobado(r),
                 v_curso.hallazgo_en_el_pendiente(r), v_curso._plan_pendiente(raiz, r),
                 v_curso.nombre_del_analisis(r), n(v_curso.principal_de(raiz, r)), v_origen.revisar_uno(r),
                 v_origen.leer_analisis(r), sorted(v_freno.rutas_de_una(r)))
        nuevo = (AnalisisEnCurso.faltantes(texto), AnalisisEnCurso.aporte(texto), AnalisisEnCurso.aprobado(r),
                 AnalisisEnCurso.turno_aprobado(r), AnalisisEnCurso.hallazgo_en_el_pendiente(r), c.plan_pendiente(r),
                 AnalisisEnCurso.nombre_del_analisis(r), n(c.principal_de(r)), OrigenDeCadaPunto.revisar_uno(r),
                 LectorDeAnalisis.leer(r), sorted(Freno.rutas_de_una(r)))
        if viejo != nuevo:
            distintos.append(r)
    ok &= igual("curso y origen por análisis (%d)" % len(todos), distintos, [])
    mensajes = ["Analicemos: el pendiente 7", "analicemos: El Pendiente 116\nmás", "Analicemos por qué falla",
                "Pregunta: el pendiente 3", "ANALICEMOS el pendiente 12 y el 13", ""]
    ok &= igual("curso.pendiente_pedido", [v_curso.pendiente_pedido(m) for m in mensajes],
                [AnalisisEnCurso.pendiente_pedido(m) for m in mensajes])
    celdas = ["EP-023, HU-007; EP-004, HU-012", "HU-1 sin épica EP-9 HU 2", "[HU-001](x.md) EP-002 HU-003"]
    ok &= igual("curso.hu_con_su_epica", [v_curso._hu_con_su_epica(x) for x in celdas],
                [AnalisisEnCurso.hu_con_su_epica(x) for x in celdas])
    return ok


# ── resumen y aviso de vuelta ─────────────────────────────────────────────

def de_resumen_y_aviso(raiz):
    carpeta = os.path.join(raiz, "historico-chat", "resumenes")
    resumenes = sorted(os.path.join(c, f) for c, _, fs in os.walk(carpeta) for f in fs
                       if f.endswith(".md") and f != "README.md") if os.path.isdir(carpeta) else []
    distintos = []
    for r in resumenes:
        viejo = (v_resumen.hallazgos(r), v_resumen.falta(r), v_resumen.hallazgos_fuera_del_molde(r),
                 v_resumen.sin_resolver(r), v_resumen.viene_de(r), n(v_resumen.proposito(raiz, r)))
        nuevo = (Resumen.hallazgos(r), Resumen.falta(r), Resumen.hallazgos_fuera_del_molde(r),
                 Resumen.sin_resolver(r), Resumen.viene_de(r), n(Resumen.proposito(raiz, r)))
        if viejo != nuevo:
            distintos.append((r, viejo, nuevo))
        else:
            for h, _t, _e in viejo[0]:
                if v_resumen._retoma(r, h) != Resumen.retoma(r, h):
                    distintos.append((r, h))
    ok = igual("resumen por archivo (%d)" % len(resumenes), distintos[:2], [])
    historico = os.path.join(raiz, "historico-chat")
    trans = sorted(f for f in os.listdir(historico) if f.endswith(".md")) if os.path.isdir(historico) else []
    ok &= igual("resumen.ruta_de (%d)" % len(trans), [v_resumen.ruta_de(raiz, t) for t in trans],
                [Resumen.ruta_de(raiz, t) for t in trans])
    v = AvisoResuelto(raiz)
    ok &= igual("aviso_resuelto.avisar (simulado)", v_aviso.avisar(raiz, "2026-10-04", "9.9.9", escribir=False),
                v.avisar("2026-10-04", "9.9.9", escribir=False))
    carpetas = v_pendientes.carpetas(raiz)
    ok &= igual("aviso_resuelto por pendiente (%d)" % len(carpetas),
                [(v_aviso.reportado(c, raiz), v_aviso.seguimiento_de(c), v_aviso.comprobado(c),
                  v_aviso.prueba_paso(c)) for c in carpetas],
                [(v.reportado(c), v.seguimiento_de(c), AvisoResuelto.comprobado(c),
                  AvisoResuelto.prueba_paso(c)) for c in carpetas])
    return ok


# ── el freno ──────────────────────────────────────────────────────────────

ORDENES = [
    "echo hola > notas.txt", "rm src/b.py", "cp src/a.py src/b.py", "python -m unittest", "pip install requests",
    "git config --global user.name x", "python servidor.py &", "git status", "python -m unittest 2>&1 | tail -3",
    "echo x > src/a.py", 'grep -n "> acá termina" analisis.md', "grep -n '> acá termina' analisis.md",
    'Select-String -Pattern "^## |^> acá" -Path a.md', 'grep "x" a.md > notas.txt', 'echo "a > b" > "otra nota.txt"',
    "sed -i -e 's/x/y/' -e 's/actual:/z/' a.md", "sed -i --expression='s/x/y/' a.md b.md", "sed -i 's/x/y/' a.md",
    "sed -n '1,5p' a.md", "python - <<'EOF'\nif a > b: print(1)\nx >> y\nEOF", "cat > nota.txt <<EOF\nhola > mundo\nEOF",
    "python - <<EOF\nif n >= 11: pass\nEOF", "awk '$1 => 2' a.txt", "echo x >> notas.txt",
    "x=$(python a.py 2>&1 >/dev/null)", "venv/Scripts/python.exe -m pip install paquete==1.0",
    ".venv/bin/pip install paquete", "python - <<'EOF'\nprint('pip install x')\nEOF",
    "C:/Python311/python.exe -m pip install paquete", "venv/Scripts/pip install a && npm install -g b",
    "git add -A", "git commit -m 'x; y'", 'git -C "C:/a b" commit -F m.txt',
    "cd /c/repo && git add . && git commit -m x && git push", "git commit -F - <<'EOF'\nmensaje; con punto y coma\nEOF",
    "git add -A && rm -rf x", "git checkout -- a.py", "python guion.py", "", "git rm x", "git mv a.py b.py",
    "git restore b.py", "git clean -fd", "git reset --hard", "git checkout .", "mkdir -p nueva/carpeta",
    "touch historico-chat/resumenes/2026-10-04/x.md", "mv a.md b.md", "tee salida.log < x", "curl -o baja.zip http://x",
    "wget -O baja.zip http://x", "ln -s a b", "install a.py /usr/bin/a", "Remove-Item -Path 'x.txt'",
    "Out-File -FilePath C:/Windows/x.txt", "Set-Content -Path validadores/x.py -Value 1", "nohup python x.py",
    "Start-Process notepad", "schtasks /create", "setx X 1", "reg add HKCU\\x", "npm install -g x", "apt-get install x",
    "echo x > /c/Windows/x.txt", "echo x > ~/x.txt", "echo x > $HOME/x.txt", "echo x > ../fuera.txt",
    "echo x > src/../../fuera.txt", "echo x > .gitignore", "echo x > ./validadores/comun.py",
    "echo x > " + ANALISIS_EN_CURSO, "echo x > documentacion/versiones/2026-10-04-x.md",
    "sudo rm x", "command touch y", "exec rm z", "A=1 rm w", "rm -rf /", "echo x 2> errores.log",
    "echo x &> todo.log", "echo x > nul", "echo x > $null", "echo x 2>&1",
    "cd proyectos/cimiento && python manage.py test core.enganches.tests_freno",
    "python \"C:/Ing. Jose/ia/agente/historico-chat/scripts/2026-10-04/paridad_freno.py\" > salida.txt",
]


def escrituras(raiz):
    """Rutas de escritura variadas: dentro y fuera del plan de cada fase en curso."""
    salida = list(RUTAS) + ["../fuera.txt", "src/../../fuera.txt", ".git/config", "/c/Windows/x", "~/x.txt",
                            "$HOME/x.txt", ANALISIS_EN_CURSO, "proyectos/cimiento/core/enganches/freno.py",
                            os.path.join(tempfile.gettempdir(), "guion.py"), raiz + "-otro/a.py", raiz, "."]
    for fase in v_acuerdos.fases_en_curso(raiz):
        rel = os.path.relpath(fase, raiz).replace("\\", "/")
        salida += [rel + "/plan_pruebas.md", rel + "/x/y.md", rel]
        texto = v_comun_leer(os.path.join(fase, "plan_trabajo.md"))
        exactas = v_plan.rutas_exactas(texto)
        salida += exactas[:6] + [os.path.dirname(r) for r in exactas[:4] if "/" in r]
    estado = v_curso.leer_estado(raiz)
    if estado and os.path.isfile(estado["analisis"]):
        salida += sorted(v_freno.rutas_de_una(estado["analisis"]))[:12]
    return salida


def v_comun_leer(r):
    return leer(r) if os.path.isfile(r) else ""


def de_freno(raiz):
    f = Freno(raiz)
    ok = igual("freno.permitido", v_freno.permitido(raiz), f.permitido())
    ok &= igual("freno.de_una", v_freno._de_una(raiz), f.de_una())
    ok &= igual("freno.analisis_prendido", v_freno.analisis_prendido(raiz), f.analisis_prendido())
    ok &= igual("freno.cambiados", v_freno._cambiados(raiz), f.cambiados())
    rutas = escrituras(raiz)
    viejas, nuevas = [], []
    for cwd in (raiz, os.path.join(raiz, "proyectos", "cimiento")):
        for r in rutas:
            for herramienta, campo in ((("Write", "file_path"),) if cwd == raiz else (("NotebookEdit", "notebook_path"),)):
                viejas.append(v_freno.revisar(raiz, herramienta, {campo: r}, cwd))
                nuevas.append(f.revisar(herramienta, {campo: r}, cwd))
    ok &= igual("freno.revisar escrituras (%d)" % len(viejas), viejas, nuevas)
    viejas, nuevas = [], []
    for cwd in (raiz, os.path.join(raiz, "proyectos", "app")):
        for orden in ORDENES:
            for fondo in (False, True):
                entrada = {"command": orden, "run_in_background": fondo}
                for herramienta in ("Bash", "PowerShell"):
                    viejas.append(v_freno.revisar(raiz, herramienta, entrada, cwd))
                    nuevas.append(f.revisar(herramienta, entrada, cwd))
    ok &= igual("freno.revisar órdenes (%d)" % len(viejas), viejas, nuevas)
    otras = [("mcp__docs__update", {}), ("Artifact", {}), ("Read", {}), ("mcp__x__query", {}),
             ("mcp__drive__upload_file", {}), ("Write", {}), ("Write", None), ("Bash", {})]
    ok &= igual("freno.revisar otras", [v_freno.revisar(raiz, h, e) for h, e in otras],
                [f.revisar(h, e) for h, e in otras])
    ok &= igual("freno.destinos", [v_freno.destinos(o) for o in ORDENES], [Freno.destinos(o) for o in ORDENES])
    ok &= igual("freno.nunca", [v_freno.nunca(o, False, raiz, raiz) for o in ORDENES],
                [f.nunca(o, False, raiz) for o in ORDENES])
    ok &= igual("freno.solo_registra", [v_freno.solo_registra(o) for o in ORDENES],
                [Freno.solo_registra(o) for o in ORDENES])
    for orden in ("git status", "python x.py"):
        ok &= igual("freno.despues «%s»" % orden, v_freno.despues(raiz, orden), f.despues(orden))
    ok &= igual("freno.transcripcion_de", [v_freno.transcripcion_de(raiz, s) for s in ("", "no-existe")],
                [f.transcripcion_de(s) for s in ("", "no-existe")])
    avisos = [("no está en el plan (02·F8)", "src/b.py", True, False), ("queda fuera", "", False, True),
              ("algo", "x", False, False)]
    ok &= igual("freno.aviso", [v_freno.aviso(*a) for a in avisos], [Freno.aviso(*a) for a in avisos])
    return ok


# ── las reglas que pide el mensaje ────────────────────────────────────────

MENSAJES = ["hola", "ya detecta el nuevo cambio?", "suba a git", "Suba el commit", "Suba el commit. Verifique las pruebas",
            "Escriba el readme con la caja de reglas de redacción", "Registre el pendiente del H2", "qué dice 02·F24?",
            "qué dice 21·AU6?", "Escriba el documento", "pero por qué no funciona", "Hágalo", "Listo. Continúe con eso",
            "<ide_opened_file>The user opened c:\\x\\HU-023\\plan_trabajo.md</ide_opened_file>qué sigue?",
            "00 id9", "Apruebo los dos planes. Hágalo", "dijo que suba todo", "Corrija el freno",
            "Pregunta: qué es 13·DOC22 y F8?", "Analicemos: el pendiente 116"]


def de_recuperar():
    r = RecuperadorDeReglas(RAIZ)
    ok = igual("recuperar.palabras_de_la_lista", v_recuperar.palabras_de_la_lista(RAIZ), r.palabras_de_la_lista())
    ok &= igual("recuperar.indice", sorted(v_recuperar.indice(RAIZ)), sorted(r.indice()))
    ok &= igual("recuperar.trae_palabra_clave", [v_recuperar.trae_palabra_clave(m, RAIZ) for m in MENSAJES],
                [r.trae_palabra_clave(m) for m in MENSAJES])
    ok &= igual("recuperar.tareas_del_mensaje", [v_recuperar.tareas_del_mensaje(m, RAIZ) for m in MENSAJES],
                [r.tareas_del_mensaje(m) for m in MENSAJES])
    for proyecto in [None, RAIZ] + PROYECTOS:
        ok &= igual("recuperar.opt_in_apagados %s" % (proyecto and os.path.basename(proyecto)),
                    v_recuperar.opt_in_apagados(proyecto), RecuperadorDeReglas.opt_in_apagados(proyecto))
        for tope in (v_recuperar.TOPE, 6000):
            ok &= igual("recuperar.como_texto %s %d" % (proyecto and os.path.basename(proyecto), tope),
                        [v_recuperar.como_texto(m, RAIZ, tope, proyecto) for m in MENSAJES],
                        [r.como_texto(m, tope, proyecto) for m in MENSAJES])
            ok &= igual("recuperar.elegir %s %d" % (proyecto and os.path.basename(proyecto), tope),
                        [v_recuperar.elegir(m, RAIZ, tope, proyecto) for m in MENSAJES],
                        [r.elegir(m, tope, proyecto) for m in MENSAJES])
    return ok


# ── lo que escribe, en copias ─────────────────────────────────────────────

def en_dos_copias(nombre, armar, viejo, nuevo):
    """Arma dos carpetas iguales, corre el viejo en una y el nuevo en la otra, y
    compara lo que devolvieron y lo que quedó escrito."""
    with tempfile.TemporaryDirectory() as tmp:
        a, b = os.path.join(tmp, "viejo"), os.path.join(tmp, "nuevo")
        armar(a)
        armar(b)
        try:
            ra = viejo(a)
        except (SystemExit, ValueError) as e:
            ra = ("error", type(e).__name__, str(e).replace(a, "<raiz>"))
        try:
            rb = nuevo(b)
        except (SystemExit, ValueError) as e:
            rb = ("error", type(e).__name__, str(e).replace(b, "<raiz>"))
        ra = n(ra)
        rb = n(rb)
        ra = _relativo(ra, n(a))
        rb = _relativo(rb, n(b))
        ok = igual(nombre + " (devuelve)", ra, rb)
        ta, tb = arbol(a), arbol(b)
        ok &= igual(nombre + " (escribe, %d archivos)" % len(ta), sorted(ta), sorted(tb))
        distintos = [k for k in ta if k in tb and ta[k] != tb[k].replace(b.encode(), a.encode())]
        ok &= igual(nombre + " (contenidos)", distintos, [])
        for k in distintos[:2]:
            print("   ", k, "\n   viejo:", ta[k][:300], "\n   nuevo:", tb[k][:300])
        return ok


def _relativo(obj, base):
    if isinstance(obj, str):
        return obj.replace(base, "<raiz>").replace(base.replace("\\", "/"), "<raiz>")
    if isinstance(obj, (list, tuple)):
        return type(obj)(_relativo(x, base) for x in obj)
    if isinstance(obj, dict):
        return {k: _relativo(v, base) for k, v in obj.items()}
    return obj


def de_escrituras_en_proyecto(raiz):
    ok = True
    # cerrar: el primer pendiente numerado de la forma anterior.
    carpeta = os.path.join(raiz, "pendientes")
    numerados = sorted(x for x in os.listdir(carpeta) if re.match(r"^\d+-.+\.md$", x)) if os.path.isdir(carpeta) else []
    for nombre in numerados[:1]:
        numero = nombre.split("-", 1)[0]
        ok &= en_dos_copias("cerrar %s" % nombre, lambda d: solo_md(raiz, d),
                            lambda d: v_cerrar.cerrar(d, numero, "cerrado-en-la-prueba", escribir=True),
                            lambda d: CerradorDePendientes(d).cerrar(numero, "cerrado-en-la-prueba", escribir=True))
        ok &= en_dos_copias("cerrar %s simulado" % nombre, lambda d: solo_md(raiz, d),
                            lambda d: v_cerrar.cerrar(d, numero, "cerrado-en-la-prueba", escribir=False),
                            lambda d: CerradorDePendientes(d).cerrar(numero, "cerrado-en-la-prueba", escribir=False))
    # andamio: una historia, una fase y dos pendientes en la primera épica con documento.
    epicas = os.path.join(raiz, "documentacion", "epicas")
    con_doc = [e for e in sorted(os.listdir(epicas)) if os.path.isfile(os.path.join(epicas, e, "epica.md"))] \
        if os.path.isdir(epicas) else []
    for epica in con_doc[:2]:
        hus = [h for h in sorted(os.listdir(os.path.join(epicas, epica))) if h.startswith("HU-")
               and os.path.isfile(os.path.join(epicas, epica, h, h + ".md"))]

        def armar(d, epica=epica):
            shutil.copytree(os.path.join(epicas, epica), os.path.join(d, "documentacion", "epicas", epica))

        ok &= en_dos_copias("andamio.crear_hu %s" % epica, armar,
                            lambda d: v_andamio.crear_hu(d, epica, "prueba-de-paridad", escribir=True),
                            lambda d: Andamio(d).crear_hu(epica, "prueba-de-paridad", escribir=True))
        ok &= en_dos_copias("andamio.crear_pendiente %s" % epica, armar,
                            lambda d: v_andamio.crear_pendiente(d, "algo-de-paridad", epica, escribir=True),
                            lambda d: Andamio(d).crear_pendiente("algo-de-paridad", epica, escribir=True))
        hoy = datetime.date(2026, 10, 4)
        ok &= en_dos_copias("andamio.crear_pendiente sin dueño %s" % epica, armar,
                            lambda d: v_andamio.crear_pendiente(d, "suelto", "", escribir=True, hoy=hoy),
                            lambda d: Andamio(d).crear_pendiente("suelto", "", escribir=True, hoy=hoy))
        if hus:
            hu = hus[0]
            ok &= en_dos_copias("andamio.crear %s/%s" % (epica, hu), armar,
                                lambda d: v_andamio.crear(d, epica, hu, "fase-de-paridad", escribir=True),
                                lambda d: Andamio(d).crear(epica, hu, "fase-de-paridad", escribir=True))
            ok &= en_dos_copias("andamio.crear_pendiente %s/%s" % (epica, hu), armar,
                                lambda d: v_andamio.crear_pendiente(d, "de-la-hu", epica + "/" + hu, escribir=True),
                                lambda d: Andamio(d).crear_pendiente("de-la-hu", epica + "/" + hu, escribir=True))
            ok &= en_dos_copias("andamio.crear_pendiente HU que no existe", armar,
                                lambda d: v_andamio.crear_pendiente(d, "x", epica + "/HU-999-no", escribir=True),
                                lambda d: Andamio(d).crear_pendiente("x", epica + "/HU-999-no", escribir=True))
    # resumen: marcar lo que le falta a cada resumen real, en una copia.
    dia = os.path.join(raiz, "historico-chat", "resumenes")
    if os.path.isdir(dia):
        def armar_resumenes(d):
            shutil.copytree(dia, os.path.join(d, "historico-chat", "resumenes"))

        def marcar(d, modulo):
            salida = []
            for c, _, fs in sorted(os.walk(os.path.join(d, "historico-chat", "resumenes"))):
                for f in sorted(fs):
                    r = os.path.join(c, f)
                    if f.endswith(".md") and f != "README.md":
                        for k in modulo.falta(r):
                            modulo.marcar_avisado(r, k)
                            salida.append((os.path.relpath(r, d), k))
            return salida

        ok &= en_dos_copias("resumen.marcar_avisado", armar_resumenes,
                            lambda d: marcar(d, v_resumen), lambda d: marcar(d, Resumen))
        transcripcion = "2026-10-04-sesion-de-paridad.md"
        ok &= en_dos_copias("resumen.crear", armar_resumenes,
                            lambda d: v_resumen.crear(d, transcripcion, RAIZ),
                            lambda d: Resumen.crear(d, transcripcion, RAIZ))
    return ok


# ── escenarios armados a mano, para lo que solo pasa escribiendo ──────────

APROBADO = "> **Aprobado** por el usuario el 2026-10-03, en el turno 2.\n\n"
FASE = "documentacion/epicas/EP-009-algo/HU-001-una-cosa/B-EP-009-HU-001-la-fase"
PENDIENTE = "documentacion/epicas/EP-009-algo/pendientes/110-algo"


def turno(k, usuario, agente="Respuesta."):
    return ("### %d · Usuario — 2026-10-02 10:0%d:00\n> %s\n\n**Agente** — 2026-10-02 10:0%d:30\n\n%s\n\n"
            % (k, k % 10, usuario, k % 10, agente))


def armar_curso(d):
    escribir(os.path.join(d, "historico-chat", "2026-10-02-sesion.md"), "# Sesión\n\n")
    escribir(os.path.join(d, "documentacion", "7-algo-que-falla", "pendiente.md"),
             "# Pendiente: algo que falla\n\n| | |\n|---|---|\n| **De dónde sale** | H-1 |\n")
    escribir(os.path.join(d, "analisis", "proyecto-analisis-principal.md"),
             "# Análisis principal\n\n## Qué es\n\nCimiento es algo.\n\n"
             "## Lista de análisis\n\n| Fecha | Resultado | Análisis |\n|---|---|---|\n")


def guion_del_curso(d, viejo):
    """Prender, pausar, volver, llenar, aprobar y apagar, con el viejo o el nuevo."""
    trans = os.path.join(d, "historico-chat", "2026-10-02-sesion.md")
    c = None if viejo else AnalisisEnCurso(d)
    llamar = (lambda nombre, *a: getattr(v_curso, nombre)(d, *a)) if viejo else \
        (lambda nombre, *a: getattr(c, nombre)(*a))
    salida = []

    def agregar(texto):
        with io.open(trans, "a", encoding="utf-8") as f:
            f.write(texto)

    agregar(turno(1, "hola") + turno(2, "Analicemos: el pendiente 7"))
    salida.append(llamar("prender", 7, trans, 2))
    salida.append(llamar("prender", 99, trans, 2))
    agregar(turno(3, "tres", "Quedó en [el archivo](otro/movido.md) y [la base](base/x.md).")
            + turno(4, "Pare") + turno(5, "otra cosa"))
    salida.append(llamar("pausar", 4))
    salida.append(llamar("pausar", 5))
    agregar(turno(6, "Analicemos: el pendiente 7"))
    salida.append(llamar("prender", 7, trans, 6))
    salida.append(llamar("pasar"))
    salida.append(llamar("aviso", "una nota"))
    salida.append(llamar("por_que_no_se_aprueba"))
    a1 = os.path.join(d, "documentacion", "7-algo-que-falla", "analisis-1.md")
    texto = leer(a1).replace("1. «tema»: «lo que se decidió» (turno «N»).", "1. Algo: se hace (turno 6).")
    texto = re.sub(r"^\| 1 \| Pasar el pendiente.*\n", "", texto, flags=re.M).replace("| «número» |", "| 1 |")
    escribir(a1, texto)
    agregar("### 7 · Usuario — 2026-10-02 10:07:00\n> Apruebo el análisis\n\n")
    salida.append(llamar("por_que_no_se_aprueba"))
    salida.append(llamar("aprobar", 7, "2026-10-02"))
    salida.append(llamar("pasar"))
    agregar("**Agente** — 2026-10-02 10:07:30\n\nAprobado.\n\n")
    salida.append(llamar("pasar"))
    salida.append(llamar("leer_estado"))
    llamar("marcar_corrija", 8)
    salida.append(llamar("corrija_activo"))
    llamar("borrar_corrija")
    salida.append(llamar("abiertos"))
    return salida


def armar_freno(d):
    os.makedirs(d)
    git(d, "init", "-q")
    git(d, "config", "user.email", "prueba@ejemplo.invalid")
    git(d, "config", "user.name", "Prueba")
    escribir(os.path.join(d, *FASE.split("/"), "plan_trabajo.md"),
             "# Plan\n\n**Aprobación** (`02·F4`): Ana Pérez, el 2026-10-03, con la versión 51.0.0.\n\n"
             "### 2.1 Archivos que se crean o modifican\n\n| Archivo | Tipo | Capa | Nota |\n|---|---|---|---|\n"
             "| `src/a.py` | Modificar | Programa | |\n| `plataforma/b.py` | Nuevo | Programa | |\n\n### 2.2 Otra\n")
    escribir(os.path.join(d, "plataforma", "a.py"), "x = 1\n" * 20)
    escribir(os.path.join(d, "historico-chat", "2026-10-03-tema.md"), "# Sesión\n\n<!-- sesion: abc -->\n")
    escribir(os.path.join(d, "historico-chat", "resumenes", "2026-10-03", "tema.md"),
             "# Resumen\n\n## Hallazgos\n\n### H-3 · otro\n\n---\n\n## ¿Se puede cerrar la sesión?\n\nNo.\n")
    git(d, "add", "-A")
    git(d, "commit", "-q", "-m", "inicio")


def guion_del_freno(d, viejo):
    salida = []
    if viejo:
        llamar = lambda nombre, *a: getattr(v_freno, nombre)(d, *a)  # noqa: E731
        cambiados = lambda: v_freno._cambiados(d)  # noqa: E731
    else:
        f = Freno(d)
        llamar = lambda nombre, *a: getattr(f, nombre)(*a)  # noqa: E731
        cambiados = f.cambiados
    escribir(os.path.join(d, "viejo.txt"), "x\n")
    llamar("tomar_foto")
    os.makedirs(os.path.join(d, "nueva"))
    os.replace(os.path.join(d, "plataforma", "a.py"), os.path.join(d, "nueva", "a.py"))
    git(d, "add", "-A")
    escribir(os.path.join(d, "src", "a.py"), "y\n")
    escribir(os.path.join(d, "src", "b.py"), "z\n")
    salida.append(sorted(cambiados()))
    for orden in ("python x.py", "git add -A", "git commit -m 'a; b'", ""):
        salida.append(llamar("despues", orden))
    ahora = datetime.datetime(2026, 10, 4, 9, 30)
    for _ in range(2):
        salida.append(llamar("anotar_hallazgo", "abc", "una escritura", "src/b.py", "no está en el plan", ahora))
    salida.append(llamar("anotar_hallazgo", "abc", "una orden de consola", "", "deja un proceso", ahora))
    salida.append(llamar("anotar_hallazgo", "otra", "una escritura", "src/c.py", "no está", ahora))
    escribir(os.path.join(d, *PENDIENTE.split("/"), "analisis-2.md"),
             "# Análisis 2\n\n## Lo que se tiene que hacer\n\n| # | Qué | Sale de | Pasó a |\n|---|---|---|---|\n"
             "| 1 | Corregir `src/c.py` | 1 | Este análisis, de una y sin fase: `.gitignore`, `./x/y.md` |\n\n## Otra\n")
    escribir(os.path.join(d, "historico-chat", ".estado", "analisis-en-curso.txt"),
             "analisis=%s/analisis-2.md\ntranscripcion=historico-chat/x.md\ndesde=1\n" % PENDIENTE)
    salida.append(llamar("anotar_hallazgo", "abc", "una escritura", "src/d.py", "no está", ahora))
    for r in ("src/c.py", ".gitignore", "x/y.md", "src/d.py", "src", "plataforma", "validadores/freno.py"):
        salida.append(llamar("revisar", "Write", {"file_path": os.path.join(d, r)}))
    salida.append(llamar("analisis_prendido"))
    return salida


def armar_aviso(d):
    epica = "documentacion/epicas/EP-009-algo"
    hu = epica + "/HU-001-una-cosa"
    reportado = epica + "/pendientes/110-algo-falla"
    resumen = "historico-chat/resumenes/2026-10-02"
    seguimiento = resumen + "/pendientes/5-espera"
    pendiente = ("# Pendiente: algo falla\n\n| | |\n|---|---|\n| **De dónde sale** | {origen} |\n\n"
                 "## El problema\n\nAlgo.\n\n## Por qué importa\n\nAlgo.\n")
    est, pro = os.path.join(d, "estandar"), os.path.join(d, "proyecto")
    escribir(os.path.join(est, *hu.split("/"), "HU-001-una-cosa.md"),
             "# HU-001\n\n| Campo | Valor |\n|---|---|\n| **Estado** | Terminada |\n")
    escribir(os.path.join(est, *reportado.split("/"), "pendiente.md"),
             pendiente.format(origen="[H-1 del proyecto](../../../../../../proyecto/%s/sesion.md)" % resumen))
    escribir(os.path.join(est, *reportado.split("/"), "analisis-1.md"),
             "# Análisis 1\n\n" + APROBADO + "## Lo que se tiene que hacer\n\n"
             "| # | Qué | Sale de | Pasó a |\n|---|---|---|---|\n"
             "| 1 | Hacer algo | 1 | [HU-001](../../HU-001-una-cosa/HU-001-una-cosa.md) |\n")
    escribir(os.path.join(pro, *resumen.split("/"), "sesion.md"),
             "# Sesión\n\n### H-1 · Algo del estándar falla\n\n| Campo | Valor |\n|---|---|\n"
             "| Qué pasó | Algo. |\n| Pendiente | [5](pendientes/5-espera/pendiente.md) |\n")
    escribir(os.path.join(pro, *seguimiento.split("/"), "pendiente.md"),
             pendiente.format(origen="[110](../../../../../../estandar/%s/pendiente.md)" % reportado))


def guion_del_aviso(d, viejo):
    est = os.path.join(d, "estandar")
    carpeta = os.path.join(est, "documentacion", "epicas", "EP-009-algo", "pendientes", "110-algo-falla")
    salida = []
    if viejo:
        salida.append(v_aviso.avisar(est, "2026-10-04", "53.0.0"))
        salida.append(v_aviso.anotar_prueba(carpeta, "2026-10-04", "una copia", [("el caso", "reproducirlo", True)]))
        salida.append(v_aviso.avisar(est, "2026-10-04", "53.0.0"))
        salida.append(v_aviso.avisar(est, "2026-10-04", "53.0.0"))
    else:
        a = AvisoResuelto(est)
        salida.append(a.avisar("2026-10-04", "53.0.0"))
        salida.append(AvisoResuelto.anotar_prueba(carpeta, "2026-10-04", "una copia", [("el caso", "reproducirlo", True)]))
        salida.append(a.avisar("2026-10-04", "53.0.0"))
        salida.append(a.avisar("2026-10-04", "53.0.0"))
    return salida


def armar_cierre_con_aviso(d):
    for i in (1, 2, 3):
        os.makedirs(os.path.join(d, "proy%d" % i, "pendientes" if i != 3 else "otra"))


def guion_del_cierre_con_aviso(d, viejo):
    ficha = ("# Pendiente · Algo que se rompió\n\n| | |\n|---|---|\n| **Proyecto de origen** | **Proyecto 2** · `x` |\n"
             "| **A quién avisar al cerrar** | %s |\n")
    proyectos = [("Proyecto %d" % i, os.path.join(d, "proy%d" % i)) for i in (1, 2, 3)] + [("Fantasma", "/no/existe")]
    salida = []
    for a_quien in ("al de origen", "a **todos** los proyectos", "a todos"):
        for escribir_ in (False, True):
            if viejo:
                salida.append(v_cerrar.avisar(os.path.join(d, "proy1"), ficha % a_quien, "/raiz/pendientes/hecho/algo.md",
                                              "9.9.9", proyectos, "2026-01-02", escribir_))
            else:
                salida.append(CerradorDePendientes(os.path.join(d, "proy1")).avisar(
                    ficha % a_quien, "/raiz/pendientes/hecho/algo.md", "9.9.9", proyectos, "2026-01-02", escribir_))
    return salida


def armar_resumen(d):
    os.makedirs(os.path.join(d, "historico-chat", "resumenes"))
    escribir(os.path.join(d, "historico-chat", "resumenes", "README.md"),
             "# Resúmenes\n\n## Días\n\n- [2026-01-01/](2026-01-01/) — algo.\n")


def guion_del_resumen(d, viejo):
    m = v_resumen if viejo else Resumen
    salida = [m.crear(d, "2026-03-04-un-tema.md", RAIZ), m.crear(d, "2026-03-04-un-tema.md", RAIZ),
              m.crear(d, "2026-03-04-otro.md", RAIZ), m.crear(d, "sin-fecha.md", RAIZ),
              m.crear(d, "2026-03-05-x.md", d)]
    (v_resumen._indexar_dias if viejo else Resumen.indexar_dias)(d, "2026-03-09")
    return salida


def de_escenarios():
    ok = en_dos_copias("curso (prender, pausar, aprobar)", armar_curso,
                       lambda d: guion_del_curso(d, True), lambda d: guion_del_curso(d, False))
    ok &= en_dos_copias("freno (foto, después, hallazgo)", armar_freno,
                        lambda d: guion_del_freno(d, True), lambda d: guion_del_freno(d, False))
    ok &= en_dos_copias("aviso_resuelto (escribe)", armar_aviso,
                        lambda d: guion_del_aviso(d, True), lambda d: guion_del_aviso(d, False))
    ok &= en_dos_copias("cerrar.avisar", armar_cierre_con_aviso,
                        lambda d: guion_del_cierre_con_aviso(d, True), lambda d: guion_del_cierre_con_aviso(d, False))
    ok &= en_dos_copias("resumen.crear e índices", armar_resumen,
                        lambda d: guion_del_resumen(d, True), lambda d: guion_del_resumen(d, False))
    return ok


PARTES = {"validadores": de_validadores, "autorizado": de_autorizado_y_acuerdos, "curso": de_curso,
          "resumen": de_resumen_y_aviso, "freno": de_freno, "escrituras": de_escrituras_en_proyecto}


def en_un_proyecto(raiz, partes):
    print("== %s" % raiz)
    ok = True
    for nombre in partes:
        if nombre in PARTES:
            ok &= PARTES[nombre](raiz)
    return ok


if __name__ == "__main__":
    # `--partes freno,curso` corre solo esas; sin ella, todas. Todas juntas tardan
    # más de diez minutos, y la consola del agente corta a los diez.
    argumentos = sys.argv[1:]
    partes = list(PARTES) + ["recuperar", "escenarios"]
    if "--partes" in argumentos:
        i = argumentos.index("--partes")
        partes = argumentos[i + 1].split(",")
        argumentos = argumentos[:i] + argumentos[i + 2:]
    todo_bien = True
    if any(p in PARTES for p in partes):
        for proyecto in [RAIZ] + (argumentos or PROYECTOS):
            todo_bien &= en_un_proyecto(os.path.abspath(proyecto), partes)
    if "recuperar" in partes:
        print("== recuperar")
        todo_bien &= de_recuperar()
    if "escenarios" in partes:
        print("== escenarios")
        todo_bien &= de_escenarios()
    print("\nPARIDAD COMPLETA" if todo_bien else "\nHAY DIFERENCIAS")
