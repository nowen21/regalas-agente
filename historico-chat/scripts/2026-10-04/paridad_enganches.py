# -*- coding: utf-8 -*-
"""Compara los enganches de `adaptadores/claude-code/` como estaban en HEAD
(importando de `validadores/`) con los de la copia de trabajo (importando de
`proyectos/cimiento/core/`), sesión del 2026-10-04, pendiente 116.

    python paridad_enganches.py [--solo hook_turno,hook_rutas] [--heredero RUTA]

Nada corre contra un proyecto real. Dentro de una carpeta temporal se arman:

  - `est`: una copia del estándar (sus documentos, `validadores/` como está en
    disco y `proyectos/cimiento/core/`), con su propio repositorio de git. El
    enganche se copia en `est/adaptadores/claude-code/`, así que para él esa
    copia **es** el estándar: no lee ni escribe el repositorio real.
  - `her`: una copia de un proyecto heredero (por defecto agro-system), sin su
    `.git` ni su `proyectos/`, también con repositorio propio.
  - `vacio`: una carpeta vacía.
  - `casa` y `temporal`: la carpeta personal y la temporal que ve el enganche.

Cada caso corre dos veces sobre el mismo punto de partida: con el enganche
viejo (`git show HEAD:...`) y con el nuevo. Se comparan el código de salida, la
salida estándar, la de errores y todo lo que quedó escrito (en el proyecto, en
`.git/cimiento-freno.json`, en la casa y en la temporal). Las horas se
normalizan, y en `hook_historico` también la ruta del guion que renombra la
sesión: el viejo nombra `validadores/historico.py` y el nuevo
`proyectos/cimiento/core/enganches/historico.py`, que es donde vive ahora.
"""
import argparse
import difflib
import io
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import time

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
ENGANCHES = os.path.join(RAIZ, "adaptadores", "claude-code")
HEREDERO = "c:/wamp64/www/proyectos/personales/agro-system"

# Lo que no se copia del estándar: pesado y ajeno a los enganches.
FUERA_DEL_ESTANDAR = {".git", "interfaz", "cvds", "proyectos", "Manual-Estandar-Agente.docx", "evals"}
FUERA_DEL_HEREDERO = {".git", "proyectos"}
IGNORAR = shutil.ignore_patterns("__pycache__", "*.pyc")

FECHA_GIT = "2026-10-04T12:00:00"
_HORA = re.compile(r"\b\d{1,2}:\d{2}(?::\d{2}(?:\.\d+)?)?\b")
_FIRMA = re.compile(r'"(\d+):(\d+)"')
SESION_EST = "efe758cc-0e19-465b-8e26-55cd2bee7ad7"


# ── las copias ────────────────────────────────────────────────────────────

def _quitar_solo_lectura(funcion, ruta, _info):
    os.chmod(ruta, stat.S_IWRITE)
    funcion(ruta)


def borrar(ruta):
    if os.path.isdir(ruta):
        shutil.rmtree(ruta, onerror=_quitar_solo_lectura)


def git(carpeta, *args, entrada=None):
    env = dict(os.environ, GIT_AUTHOR_DATE=FECHA_GIT, GIT_COMMITTER_DATE=FECHA_GIT,
               GIT_AUTHOR_NAME="paridad", GIT_AUTHOR_EMAIL="paridad@local",
               GIT_COMMITTER_NAME="paridad", GIT_COMMITTER_EMAIL="paridad@local")
    r = subprocess.run(["git", "-c", "core.autocrlf=false", "-c", "core.safecrlf=false", "-c", "core.longpaths=true"] + list(args),
                       cwd=carpeta, env=env, capture_output=True, input=entrada)
    if r.returncode != 0:
        raise RuntimeError("git %s: %s" % (" ".join(args), r.stderr.decode("utf-8", "replace")))
    return r.stdout.decode("utf-8", "replace")


def copiar_arriba(origen, destino, fuera):
    os.makedirs(destino, exist_ok=True)
    for nombre in os.listdir(origen):
        if nombre in fuera:
            continue
        de, a = os.path.join(origen, nombre), os.path.join(destino, nombre)
        if os.path.isdir(de):
            shutil.copytree(de, a, ignore=IGNORAR)
        else:
            shutil.copy2(de, a)


def iniciar_repo(carpeta):
    git(carpeta, "init", "-q")
    git(carpeta, "add", "-A", "-f")
    git(carpeta, "commit", "-q", "--no-verify", "-m", "base de la paridad")
    return git(carpeta, "rev-parse", "HEAD").strip()


def armar_estandar(destino):
    copiar_arriba(RAIZ, destino, FUERA_DEL_ESTANDAR)
    shutil.copytree(os.path.join(RAIZ, "proyectos", "cimiento", "core"),
                    os.path.join(destino, "proyectos", "cimiento", "core"), ignore=IGNORAR)
    # La transcripción que usan los casos, copiada para leerla sin tocar la real.
    return iniciar_repo(destino)


def armar_heredero(origen, destino):
    copiar_arriba(origen, destino, FUERA_DEL_HEREDERO)
    os.makedirs(os.path.join(destino, "proyectos"), exist_ok=True)
    with io.open(os.path.join(destino, "proyectos", "LEEME.txt"), "w", encoding="utf-8") as f:
        f.write("carpeta de la paridad\n")
    return iniciar_repo(destino)


class Mundo:
    """Las carpetas de una corrida y cómo volverlas al punto de partida."""

    def __init__(self, tmp, heredero):
        self.tmp = tmp
        self.est = os.path.join(tmp, "est")
        self.her = os.path.join(tmp, "her")
        self.vacio = os.path.join(tmp, "vacio")
        self.casa = os.path.join(tmp, "casa")
        self.temporal = os.path.join(tmp, "temporal")
        self.otro = os.path.join(tmp, "otro")
        self.datos = os.path.join(tmp, "datos")
        print("Armando la copia del estándar...")
        self.base = {"est": armar_estandar(self.est)}
        if os.path.isdir(heredero):
            print("Armando la copia del heredero...")
            self.base["her"] = armar_heredero(heredero, self.her)
        os.makedirs(self.datos)
        self.transcript = self._transcript()
        self.transcript_real = self._transcript_real()

    def raiz(self, cual):
        return {"est": self.est, "her": self.her, "vacio": self.vacio}[cual]

    def reiniciar(self):
        for cual, base in self.base.items():
            carpeta = self.raiz(cual)
            git(carpeta, "reset", "-q", "--hard", base)
            git(carpeta, "clean", "-q", "-fdx")
            foto = os.path.join(carpeta, ".git", "cimiento-freno.json")
            if os.path.exists(foto):
                os.remove(foto)
        for carpeta in (self.vacio, self.casa, self.temporal, self.otro):
            borrar(carpeta)
            os.makedirs(carpeta)

    def _transcript(self):
        """Una transcripción de Claude Code hecha a mano: dos turnos con uso de fichas
        y una respuesta con marcas que la medición tiene que ver."""
        lineas = [
            {"type": "user", "message": {"role": "user", "content": "hola, ¿qué falta?"}},
            {"type": "assistant", "message": {"role": "assistant", "content": [{"type": "text", "text": "Falta poco."}],
                                              "usage": {"input_tokens": 600000, "output_tokens": 300,
                                                        "cache_creation_input_tokens": 1000,
                                                        "cache_read_input_tokens": 50}}},
            {"type": "user", "message": {"role": "user", "content": "¿y ahora?"}},
            {"type": "assistant", "message": {"role": "assistant", "content": [{"type": "text", "text": (
                "Usted tiene razón — en resumen, es importante destacar que esto funciona. "
                "Le comento que **sin duda** quedó listo. 🚀\n\n" + "Una línea más de relleno. " * 200)}],
                "usage": {"input_tokens": 500000, "output_tokens": 900, "cache_read_input_tokens": 70}}},
            "esto no es json",
        ]
        ruta = os.path.join(self.datos, "transcript.jsonl")
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            for l in lineas:
                f.write((l if isinstance(l, str) else json.dumps(l, ensure_ascii=False)) + "\n")
        return ruta

    def _transcript_real(self):
        carpeta = os.path.join(os.path.expanduser("~"), ".claude", "projects", "c--Ing--Jose-ia-agente")
        nombre = "f6dbc715-b0ac-488e-9a51-c495f3004132.jsonl"
        if not os.path.isfile(os.path.join(carpeta, nombre)):
            return self.transcript
        shutil.copy2(os.path.join(carpeta, nombre), os.path.join(self.datos, nombre))
        return os.path.join(self.datos, nombre)


# ── lo que queda escrito ──────────────────────────────────────────────────

def normalizar(texto, hook):
    texto = _HORA.sub("<hora>", texto)
    if hook == "hook_historico.py":
        for guion in ("validadores/historico.py", "proyectos/cimiento/core/enganches/historico.py"):
            texto = re.sub(r"[^\"`\s]*" + re.escape(guion), "<orden>", texto)
    return texto


def leer(ruta):
    with io.open(ruta, encoding="utf-8", errors="replace", newline="") as f:
        return f.read()


def foto_de_git(carpeta):
    """`{ruta: texto}` de lo que git ve distinto del punto de partida."""
    salida = {}
    crudo = git(carpeta, "status", "--porcelain=v1", "-z", "-uall", "--ignored")
    items = iter(crudo.split("\0"))
    for item in items:
        if len(item) < 4:
            continue
        if item[0] in "RC":
            next(items, None)
        rel = item[3:]
        if "__pycache__" in rel or re.match(r"adaptadores/claude-code/hook_\w+\.py$", rel):
            continue
        ruta = os.path.join(carpeta, *rel.split("/"))
        salida[rel] = leer(ruta) if os.path.isfile(ruta) else "<no está: %s>" % item[:2]
    foto = os.path.join(carpeta, ".git", "cimiento-freno.json")
    if os.path.isfile(foto):
        # La firma lleva la fecha en nanosegundos: cambia de una corrida a la otra.
        salida[".git/cimiento-freno.json"] = _FIRMA.sub(r'"<fecha>:\2"', leer(foto))
    return salida


def foto_de_carpeta(carpeta):
    salida = {}
    for actual, subs, archivos in os.walk(carpeta):
        subs[:] = [s for s in subs if s != "__pycache__"]
        for nombre in archivos:
            ruta = os.path.join(actual, nombre)
            salida[os.path.relpath(ruta, carpeta).replace("\\", "/")] = leer(ruta)
    return salida


def foto(mundo):
    salida = {}
    for cual in mundo.base:
        salida.update({"%s/%s" % (cual, k): v for k, v in foto_de_git(mundo.raiz(cual)).items()})
    for nombre in ("vacio", "casa", "temporal", "otro"):
        salida.update({"%s/%s" % (nombre, k): v for k, v in foto_de_carpeta(getattr(mundo, nombre)).items()})
    return salida


# ── correr un enganche ────────────────────────────────────────────────────

def version_vieja(hook):
    return subprocess.run(["git", "show", "HEAD:adaptadores/claude-code/" + hook], cwd=RAIZ,
                          capture_output=True, check=True).stdout


def version_nueva(hook):
    with open(os.path.join(ENGANCHES, hook), "rb") as f:
        return f.read()


def correr(mundo, hook, contenido, caso):
    mundo.reiniciar()
    if caso.get("preparar"):
        caso["preparar"](mundo)
    destino = os.path.join(mundo.est, "adaptadores", "claude-code", hook)
    with open(destino, "wb") as f:
        f.write(contenido)
    # Que git no vea el enganche recién copiado como un cambio: si no, el viejo
    # (distinto del que quedó en la base) aparecería entre lo cambiado.
    git(mundo.est, "update-index", "--assume-unchanged", "adaptadores/claude-code/" + hook)
    env ={k: v for k, v in os.environ.items() if k not in ("CIMIENTO", "CLAUDE_SESSION_ID", "PYTHONPATH")}
    env.update({"USERPROFILE": mundo.casa, "HOME": mundo.casa, "TEMP": mundo.temporal, "TMP": mundo.temporal,
                "TMPDIR": mundo.temporal,
                "PYTHONDONTWRITEBYTECODE": "1", "GIT_CEILING_DIRECTORIES": mundo.tmp})
    env.update(caso.get("env", {}))
    entrada = caso.get("entrada", {})
    if callable(entrada):
        entrada = entrada(mundo)
    crudo = entrada if isinstance(entrada, bytes) else json.dumps(entrada, ensure_ascii=False).encode("utf-8")
    args = caso["args"](mundo) if callable(caso["args"]) else caso["args"]
    cwd = caso["cwd"](mundo) if callable(caso.get("cwd")) else mundo.est
    inicio = time.time()
    r = subprocess.run([sys.executable, destino] + args, input=crudo, cwd=cwd, env=env,
                       capture_output=True, timeout=300)
    return {"codigo": r.returncode,
            "salida": normalizar(r.stdout.decode("utf-8", "replace"), hook),
            "errores": normalizar(r.stderr.decode("utf-8", "replace"), hook),
            "escrito": {k: normalizar(v, hook) for k, v in foto(mundo).items()},
            "segundos": time.time() - inicio}


def _diff(a, b):
    """Las líneas que cambian, con el signo de cada lado (- viejo, + nuevo)."""
    lineas = difflib.unified_diff(str(a).splitlines(), str(b).splitlines(), "viejo", "nuevo", n=1, lineterm="")
    return "\n      ".join(l[:300] for l in list(lineas)[:40])


def comparar(viejo, nuevo):
    diferencias = []
    for campo in ("codigo", "salida", "errores"):
        if viejo[campo] != nuevo[campo]:
            diferencias.append("%s:\n      %s" % (campo, _diff(viejo[campo], nuevo[campo])))
    a, b = viejo["escrito"], nuevo["escrito"]
    for k in sorted(set(a) | set(b)):
        if a.get(k) != b.get(k):
            diferencias.append("escrito %s:\n      %s" % (k, _diff(a.get(k, "<no está>"), b.get(k, "<no está>"))))
    return diferencias


# ── los casos ─────────────────────────────────────────────────────────────

def escribir(ruta, texto, modo="w"):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with io.open(ruta, modo, encoding="utf-8", newline="\n") as f:
        f.write(texto)


def con_raiz(cual, *resto):
    return lambda m: ["--raiz", m.raiz(cual)] + list(resto)


def sesion_de(carpeta):
    """La marca de sesión de la última transcripción de `carpeta`, o ""."""
    historico = os.path.join(carpeta, "historico-chat")
    if not os.path.isdir(historico):
        return ""
    for nombre in sorted(os.listdir(historico), reverse=True):
        if nombre.endswith(".md") and nombre != "README.md":
            m = re.search(r"<!-- sesion: (.+?) -->", leer(os.path.join(historico, nombre)))
            if m:
                return m.group(1)
    return ""


def archivos_de_epicas(raiz, nombre, cuantos):
    """`cuantos` archivos llamados `nombre` en las épicas, repartidos de punta a punta."""
    salida = []
    for carpeta, _s, archivos in os.walk(os.path.join(raiz, "documentacion", "epicas")):
        if nombre in archivos:
            salida.append(os.path.join(carpeta, nombre))
    salida.sort()
    paso = max(1, len(salida) // cuantos)
    return salida[::paso][:cuantos] + salida[-1:]


ANALISIS_103 = ("documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/pendientes/"
                "103-cada-documento-de-la-cadena-sale-del-anterior/analisis-16.md")


def prender_analisis(cual="est", analisis=ANALISIS_103, transcripcion="historico-chat/2026-10-04-sesion.md"):
    """Deja prendido un análisis: el freno, los acuerdos y el análisis en curso lo leen."""
    def preparar(m):
        escribir(os.path.join(m.raiz(cual), "historico-chat", ".estado", "analisis-en-curso.txt"),
                 "analisis=%s\ntranscripcion=%s\ndesde=1\n" % (analisis, transcripcion))
    return preparar


def editado(ruta_de, **mas):
    def entrada(m):
        datos = {"session_id": "s-paridad", "tool_name": "Edit", "tool_input": {"file_path": ruta_de(m)}}
        datos["tool_input"].update(mas)
        return datos
    return entrada


def casos_simples(m):
    """Los casos de cada enganche. `m` es el mundo ya armado (para elegir archivos)."""
    sesion_her = sesion_de(m.her) if "her" in m.base else ""
    resultados = archivos_de_epicas(m.est, "resultado_pruebas.md", 10)
    estados = (archivos_de_epicas(m.est, "estado-fase.md", 2) + archivos_de_epicas(m.est, "plan_trabajo.md", 4)
               + archivos_de_epicas(m.est, "funcionalidad_implementada.md", 4))
    planes = archivos_de_epicas(m.est, "plan_trabajo.md", 2)
    hay_her = "her" in m.base
    raices = ["est", "her"] if hay_her else ["est"]
    C = {}

    # hook_turno
    def tocar_y_atrasar(m):
        registro = os.path.join(m.est, "historico-chat", ".tocado", "s1.txt")
        escribir(registro, "README.md\n")
        viejo = time.time() - 3600
        os.utime(registro, (viejo, viejo))
        escribir(os.path.join(m.est, "base", "nuevo.md"), "# nuevo\n")
        escribir(os.path.join(m.est, "README.md"), "\nlinea\n", "a")
        os.remove(os.path.join(m.est, "VERSION"))
    C["hook_turno.py"] = [
        {"nombre": "primera vuelta", "args": con_raiz("est"), "entrada": {"session_id": "s1"}},
        {"nombre": "con cambios", "args": con_raiz("est"), "entrada": {"session_id": "s1"},
         "preparar": tocar_y_atrasar},
        {"nombre": "sin --raiz, con cwd", "args": [], "entrada": lambda m: {"session_id": "s1", "cwd": m.est},
         "preparar": tocar_y_atrasar},
        {"nombre": "sin sesión", "args": con_raiz("est"), "entrada": {"cwd": "x"}},
        {"nombre": "JSON roto", "args": con_raiz("est"), "entrada": b"{no"},
        {"nombre": "lista", "args": con_raiz("est"), "entrada": [1]},
        {"nombre": "carpeta que no está", "args": lambda m: ["--raiz", os.path.join(m.tmp, "no-esta")],
         "entrada": {"session_id": "s1"}},
        {"nombre": "vacío sin git", "args": con_raiz("vacio"), "entrada": {"session_id": "s1"}},
    ]

    # hook_veredicto
    C["hook_veredicto.py"] = [
        {"nombre": "resultado %d" % i, "args": con_raiz("est"),
         "entrada": (lambda r: lambda m: {"tool_input": {"file_path": r}})(r)} for i, r in enumerate(resultados)
    ] + [
        {"nombre": "copia a tres sitios", "args": con_raiz("est"),
         "entrada": lambda m: {"tool_input": {"file_path": os.path.join(m.est, *(
             "documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/"
             "A-EP-001-HU-009-clasificar-las-que-faltan/resultado_pruebas.md").split("/"))}}},
        {"nombre": "por la respuesta", "args": con_raiz("est"),
         "entrada": (lambda r: lambda m: {"tool_response": {"filePath": r}})(resultados[0])},
        {"nombre": "resultado que no está", "args": con_raiz("est"),
         "entrada": lambda m: {"tool_input": {"file_path": os.path.join(m.est, "x", "resultado_pruebas.md")}}},
        {"nombre": "otro archivo", "args": con_raiz("est"),
         "entrada": lambda m: {"tool_input": {"file_path": os.path.join(m.est, "README.md")}}},
        {"nombre": "sin --raiz", "args": [], "entrada": (lambda r: lambda m: {"tool_input": {"file_path": r}})(resultados[0])},
        {"nombre": "JSON roto", "args": con_raiz("est"), "entrada": b"["},
    ]

    # hook_rutas
    def rutas_caso(nombre, ruta, args=None):
        return {"nombre": nombre, "args": args or con_raiz("est"),
                "entrada": lambda m: {"tool_input": {"file_path": ruta(m)}}}
    C["hook_rutas.py"] = [
        rutas_caso("adentro", lambda m: os.path.join(m.est, "base", "x.md")),
        rutas_caso("afuera", lambda m: os.path.join(m.otro, "x.py")),
        rutas_caso("vecino con prefijo", lambda m: m.est + "-viejo/x.py"),
        rutas_caso("relativa", lambda m: "README.md"),
        rutas_caso("vacía", lambda m: ""),
        rutas_caso("consola de git", lambda m: "/c/Users/x.py"),
        rutas_caso("con barras", lambda m: m.est.replace("\\", "/") + "/a/b.py"),
        rutas_caso("sin --raiz", lambda m: os.path.join(m.otro, "x.py"), args=[]),
        {"nombre": "por la respuesta", "args": con_raiz("est"),
         "entrada": lambda m: {"tool_response": {"file_path": os.path.join(m.otro, "y.md")}}},
        {"nombre": "JSON roto", "args": con_raiz("est"), "entrada": b"x"},
        {"nombre": "no es objeto", "args": con_raiz("est"), "entrada": "texto"},
    ]

    # hook_acuerdos
    C["hook_acuerdos.py"] = [
        {"nombre": "--raiz %s" % r, "args": con_raiz(r), "entrada": {"prompt": "hola"}} for r in raices
    ] + [
        {"nombre": "cwd", "args": [], "entrada": lambda m: {"cwd": m.est}},
        {"nombre": "análisis prendido", "args": con_raiz("est"), "entrada": {}, "preparar": prender_analisis()},
        {"nombre": "análisis prendido, tope chico", "args": con_raiz("est"), "entrada": {},
         "preparar": prender_analisis(analisis=ANALISIS_103.replace("16", "3"))},
        {"nombre": "vacío", "args": con_raiz("vacio"), "entrada": {}},
        {"nombre": "JSON roto", "args": con_raiz("est"), "entrada": b"{"},
    ]

    # hook_checkpoint
    C["hook_checkpoint.py"] = [
        {"nombre": "fase %d" % i, "args": con_raiz("est"),
         "entrada": (lambda r: lambda m: {"tool_input": {"file_path": r}})(r)} for i, r in enumerate(estados)
    ] + [
        {"nombre": "plan inventado", "args": con_raiz("est"), "entrada": lambda m: {"tool_input": {
            "file_path": os.path.join(m.est, "documentacion", "epicas", "X-EP-1-HU-1-x", "plan_trabajo.md")}}},
        {"nombre": "fuera de épicas", "args": con_raiz("est"),
         "entrada": lambda m: {"tool_input": {"file_path": os.path.join(m.est, "README.md")}}},
        {"nombre": "sin ruta", "args": con_raiz("est"), "entrada": {"tool_input": {}}},
        {"nombre": "sin --raiz", "args": [], "entrada": (lambda r: lambda m: {"tool_input": {"file_path": r}})(estados[0])},
    ] + [
        {"nombre": "plan más nuevo que el checkpoint %d" % i, "args": con_raiz("est"),
         "preparar": (lambda r: lambda m: os.utime(r, (time.time() + 100, time.time() + 100)))(r),
         "entrada": (lambda r: lambda m: {"tool_input": {"file_path": r}})(r)} for i, r in enumerate(planes)
    ] + [
        {"nombre": "fase sin checkpoint %d" % i, "args": con_raiz("est"),
         "preparar": (lambda r: lambda m: os.remove(os.path.join(os.path.dirname(r), "estado-fase.md")))(r),
         "entrada": (lambda r: lambda m: {"tool_input": {"file_path": r}})(r)} for i, r in enumerate(planes)
    ] + [
        {"nombre": "JSON roto", "args": con_raiz("est"), "entrada": b"{"},
    ]

    # hook_externo
    def externo(nombre, entrada_herramienta, args=None):
        return {"nombre": nombre, "args": args or con_raiz("est"),
                "entrada": lambda m: {"tool_name": nombre.split(" ")[0], "tool_input": entrada_herramienta(m)}}
    C["hook_externo.py"] = [
        externo("WebFetch", lambda m: {"url": "https://ejemplo.org"}),
        externo("WebSearch", lambda m: {"query": "q"}),
        externo("mcp__gmail__leer", lambda m: {"id": 1}),
        externo("Read adentro", lambda m: {"file_path": os.path.join(m.est, "README.md")}),
        externo("Read afuera", lambda m: {"file_path": os.path.join(m.otro, "x.txt")}),
        externo("Read sin ruta", lambda m: {}),
        externo("Bash", lambda m: {"command": "curl x"}),
        {"nombre": "cwd", "args": [], "entrada": lambda m: {"tool_name": "Read", "cwd": m.est,
                                                            "tool_input": {"file_path": os.path.join(m.otro, "x")}}},
        {"nombre": "JSON roto", "args": con_raiz("est"), "entrada": b"{"},
    ]

    # hook_presupuesto
    def presupuesto(nombre, args, transcript):
        return {"nombre": nombre, "args": args,
                "entrada": lambda m: {"transcript_path": transcript(m)}}
    C["hook_presupuesto.py"] = [
        presupuesto("cierre", ["--raiz", "."], lambda m: m.transcript),
        presupuesto("cierre con umbral", ["--umbral", "1000"], lambda m: m.transcript),
        presupuesto("aviso", ["--modo", "aviso"], lambda m: m.transcript),
        presupuesto("aviso tramo chico", ["--modo", "aviso", "--umbral", "100000"], lambda m: m.transcript),
        presupuesto("aviso apagado", ["--modo", "aviso", "--umbral", "0"], lambda m: m.transcript),
        presupuesto("transcripción real", [], lambda m: m.transcript_real),
        presupuesto("aviso real", ["--modo", "aviso", "--umbral", "500000"], lambda m: m.transcript_real),
        presupuesto("sin transcripción", [], lambda m: ""),
        presupuesto("transcripción que no está", [], lambda m: os.path.join(m.otro, "no.jsonl")),
        {"nombre": "modo inválido", "args": ["--modo", "otro"], "entrada": {}},
        {"nombre": "JSON roto", "args": [], "entrada": b"{"},
    ]

    # hook_senales
    def senales_heredero(m):
        escribir(os.path.join(m.her, "documentacion", "senales.md"), "# Señales\n\nalgo\n")

    def senales_ya(m):
        escribir(os.path.join(m.est, "documentacion", "senales.md"), "# Señales\n\n<!-- avisado: s9 -->\n")
    C["hook_senales.py"] = [
        {"nombre": "est sin sesión", "args": con_raiz("est"), "preparar": senales_ya},
        {"nombre": "est con sesión", "args": con_raiz("est"), "env": {"CLAUDE_SESSION_ID": "s1"}, "preparar": senales_ya},
        {"nombre": "est ya avisado", "args": con_raiz("est"), "env": {"CLAUDE_SESSION_ID": "s9"}, "preparar": senales_ya},
        {"nombre": "est tal cual", "args": [], "env": {"CLAUDE_SESSION_ID": "s1"}},
        {"nombre": "vacío", "args": con_raiz("vacio"), "env": {"CLAUDE_SESSION_ID": "s1"}},
    ] + ([{"nombre": "heredero", "args": con_raiz("her"), "env": {"CLAUDE_SESSION_ID": "s1"},
           "preparar": senales_heredero}] if hay_her else [])

    # hook_recuerdos
    def memoria_local(cual, nombres):
        def preparar(m):
            slug = re.sub(r"[^A-Za-z0-9]", "-", os.path.abspath(m.raiz(cual)))
            for n in nombres:
                escribir(os.path.join(m.casa, ".claude", "projects", slug, "memory", n), "recuerdo %s\n" % n)
        return preparar
    C["hook_recuerdos.py"] = [
        {"nombre": "nada que mover", "args": con_raiz("est"), "entrada": {}},
        {"nombre": "dos recuerdos", "args": con_raiz("est"), "entrada": {"hook_event_name": "PostToolUse"},
         "preparar": memoria_local("est", ["feedback_uno.md", "MEMORY.md"])},
        {"nombre": "sin evento, por cwd", "args": [], "entrada": lambda m: {"cwd": m.est},
         "preparar": memoria_local("est", ["otro.md"])},
        {"nombre": "vacío", "args": con_raiz("vacio"), "entrada": {}, "preparar": memoria_local("vacio", ["a.md"])},
        {"nombre": "JSON roto", "args": con_raiz("est"), "entrada": b"{", "preparar": memoria_local("est", ["b.md"])},
    ]

    # hook_relacionadas
    def ya_avisado(m):
        import hashlib
        raiz = os.path.abspath(m.est)
        huella = hashlib.sha1(raiz.encode("utf-8")).hexdigest()[:12]
        rel = os.path.relpath(os.path.join(raiz, "base", "01-conducta.md"), raiz)
        escribir(os.path.join(m.temporal, "agente-avisado-relacionadas-%s.txt" % huella), "s-paridad\t%s\n" % rel)
    C["hook_relacionadas.py"] = [
        {"nombre": "regla del núcleo", "args": con_raiz("est"),
         "entrada": editado(lambda m: os.path.join(m.est, "base", "01-conducta.md"))},
        {"nombre": "ya avisado", "args": con_raiz("est"), "preparar": ya_avisado,
         "entrada": editado(lambda m: os.path.join(m.est, "base", "01-conducta.md"))},
        {"nombre": "plantilla", "args": con_raiz("est"),
         "entrada": editado(lambda m: os.path.join(m.est, "plantillas", "sesion.md"))},
        {"nombre": "no es md", "args": con_raiz("est"),
         "entrada": editado(lambda m: os.path.join(m.est, "validadores", "comun.py"))},
        {"nombre": "afuera", "args": con_raiz("est"),
         "entrada": editado(lambda m: os.path.join(m.otro, "x.md"))},
        {"nombre": "sin --raiz", "args": [],
         "entrada": editado(lambda m: os.path.join(m.est, "base", "02-flujo-de-trabajo.md"))},
        {"nombre": "JSON roto", "args": con_raiz("est"), "entrada": b"{"},
    ] + ([{"nombre": "heredero", "args": con_raiz("her"),
           "entrada": editado(lambda m: os.path.join(m.her, "CLAUDE.md"))}] if hay_her else [])

    # hook_redaccion
    C["hook_redaccion.py"] = [
        {"nombre": "respuesta con marcas", "args": con_raiz("est"),
         "entrada": lambda m: {"transcript_path": m.transcript, "session_id": SESION_EST}},
        {"nombre": "sesión sin histórico", "args": con_raiz("est"),
         "entrada": lambda m: {"transcript_path": m.transcript, "session_id": "nada"}},
        {"nombre": "transcripción real", "args": con_raiz("est"),
         "entrada": lambda m: {"transcript_path": m.transcript_real, "session_id": SESION_EST}},
        {"nombre": "sin transcripción", "args": con_raiz("est"), "entrada": {}},
        {"nombre": "sin --raiz", "args": [], "entrada": lambda m: {"transcript_path": m.transcript}},
        {"nombre": "JSON roto", "args": con_raiz("est"), "entrada": b"{"},
    ] + ([{"nombre": "heredero", "args": con_raiz("her"),
           "entrada": lambda m: {"transcript_path": m.transcript, "session_id": sesion_her}}] if hay_her else [])

    # hook_reglas
    mensajes = ["hola", "Corrija el enlace roto", "Analicemos el pendiente 116", "Hágalo con 02·F4 y C21",
                "Revise base/01-conducta.md", "Escriba la regla y redacte el plan", "Suba los cambios",
                "Pare", "Apruebo el análisis"]
    C["hook_reglas.py"] = [
        {"nombre": "«%s» %s" % (t, r), "args": con_raiz(r),
         "entrada": (lambda t: lambda m: {"prompt": t, "transcript_path": m.transcript})(t)}
        for t in mensajes for r in raices
    ] + [
        {"nombre": "sin medición", "args": con_raiz("est"), "entrada": {"prompt": "hola"}},
        {"nombre": "cwd", "args": [], "entrada": lambda m: {"prompt": "x", "cwd": m.est}},
        {"nombre": "JSON roto", "args": con_raiz("est"), "entrada": b"{"},
    ]

    # hook_checklist
    C["hook_checklist.py"] = [
        {"nombre": "el estándar", "args": con_raiz("est"), "entrada": {}},
        {"nombre": "vacío", "args": con_raiz("vacio"), "entrada": {}},
        {"nombre": "cwd vacío", "args": [], "entrada": lambda m: {"cwd": m.vacio}},
        {"nombre": "JSON roto", "args": con_raiz("vacio"), "entrada": b"{"},
    ] + ([{"nombre": "heredero", "args": con_raiz("her"), "entrada": {}}] if hay_her else [])

    # hook_estacion
    fila_12 = re.compile(r"^(\|\s*12\s*\|[^|\n]*\|[^|\n]*\|)[^|\n]*\|\s*$", re.M)

    def commit_en_fase(cual):
        """Un commit que toca una fase cerrada con la casilla 12 vacía: el enganche la marca."""
        def preparar(m):
            raiz = m.raiz(cual)
            for estado in archivos_de_epicas(raiz, "estado-fase.md", 400):
                texto = leer(estado)
                cierre = os.path.join(os.path.dirname(estado), "funcionalidad_implementada.md")
                if fila_12.search(texto) and os.path.isfile(cierre):
                    escribir(estado, fila_12.sub(lambda f: f.group(1) + " ☐ |", texto, count=1))
                    break
            escribir(os.path.join(raiz, "README.md"), "\nlínea\n", "a")
            git(raiz, "add", "-A")
            git(raiz, "commit", "-q", "--no-verify", "-m", "commit de la paridad")
        return preparar
    C["hook_estacion.py"] = [
        {"nombre": "commit en el estándar", "args": con_raiz("est"), "preparar": commit_en_fase("est")},
        {"nombre": "sin commit nuevo", "args": con_raiz("est")},
        {"nombre": "vacío sin git", "args": con_raiz("vacio")},
    ] + ([{"nombre": "commit en el heredero", "args": con_raiz("her"), "preparar": commit_en_fase("her")}]
         if hay_her else [])

    # hook_md
    marcas = "Usted — en resumen, es importante destacar esto. 🚀\n" * 3
    C["hook_md.py"] = [
        {"nombre": "md con marcas", "args": con_raiz("est"),
         "entrada": editado(lambda m: os.path.join(m.est, "notas", "x.md"), new_string=marcas)},
        {"nombre": "md con enlace roto", "args": con_raiz("est"),
         "preparar": lambda m: escribir(os.path.join(m.est, "notas", "roto.md"), "[a](no-existe.md)\n"),
         "entrada": editado(lambda m: os.path.join(m.est, "notas", "roto.md"), content="[a](no-existe.md)\n")},
        {"nombre": "pendiente fuera del índice", "args": con_raiz("est"),
         "preparar": lambda m: escribir(os.path.join(m.est, "pendientes", "999-sin-indice.md"), "# x\n"),
         "entrada": editado(lambda m: os.path.join(m.est, "pendientes", "999-sin-indice.md"), content="# x\n")},
        {"nombre": "heredero, pendiente fuera del índice", "args": con_raiz("her"),
         "preparar": lambda m: (escribir(os.path.join(m.her, "pendientes", "999-sin-indice.md"), "# x\n"),
                                escribir(os.path.join(m.her, "pendientes", "README.md"), "# Pendientes\n")),
         "entrada": editado(lambda m: os.path.join(m.her, "pendientes", "999-sin-indice.md"), content="# x\n")},
        {"nombre": "py", "args": con_raiz("est"),
         "entrada": editado(lambda m: os.path.join(m.est, "validadores", "comun.py"))},
        {"nombre": "afuera", "args": con_raiz("est"), "entrada": editado(lambda m: os.path.join(m.otro, "x.md"))},
        {"nombre": "multiedit", "args": [], "entrada": editado(lambda m: os.path.join(m.est, "base", "x.md"),
                                                               edits=[{"new_string": "— a"}, {"new_string": "b"}])},
        {"nombre": "JSON roto", "args": con_raiz("est"), "entrada": b"{"},
    ] + ([{"nombre": "heredero", "args": con_raiz("her"),
           "entrada": editado(lambda m: os.path.join(m.her, "CLAUDE.md"), new_string=marcas)}] if hay_her else [])

    # hook_analisis
    def analisis(texto, cual="est", sesion=SESION_EST, args=None):
        return {"nombre": "«%s» %s" % (texto, cual), "args": args or con_raiz(cual, "--modo", "mensaje"),
                "entrada": {"prompt": texto, "session_id": sesion}}
    C["hook_analisis.py"] = [
        analisis("hola"), analisis("Corrija el enlace"), analisis("pare"), analisis("Apruebo el análisis"),
        analisis("sigamos con el pendiente 116"), analisis("sigamos con el pendiente 999"),
        analisis("hola", sesion="no-hay"),
        {"nombre": "cierre", "args": con_raiz("est", "--modo", "cierre"), "entrada": {}},
        {"nombre": "JSON roto", "args": con_raiz("est"), "entrada": b"{"},
    ] + ([analisis("hola", "her", sesion_her), analisis("pare", "her", sesion_her)] if hay_her else [])

    # hook_resumen
    def sesion_nueva(cual):
        def preparar(m):
            escribir(os.path.join(m.raiz(cual), "historico-chat", "2026-10-04-sesion.md"),
                     "<!-- sesion: s-nueva -->\n# Sesión\n\n### 1 · Usuario · <hora>\n\nhola\n")
        return preparar

    def produjo(m):
        sesion_nueva("est")(m)
        escribir(os.path.join(m.est, "base", "algo.md"), "x\n")
    C["hook_resumen.py"] = [
        {"nombre": "inicio %s" % s, "args": con_raiz("est", "--modo", "inicio"), "entrada": {"session_id": s},
         "preparar": sesion_nueva("est")} for s in (SESION_EST, "s-nueva", "no-hay")
    ] + [
        {"nombre": "aviso %s" % s, "args": con_raiz("est", "--modo", "aviso"), "entrada": {"session_id": s},
         "preparar": produjo} for s in (SESION_EST, "s-nueva", "no-hay")
    ] + [
        {"nombre": "sin modo", "args": con_raiz("est"), "entrada": {}},
        {"nombre": "cwd", "args": ["--modo", "aviso"], "entrada": lambda m: {"cwd": m.est, "session_id": SESION_EST}},
        {"nombre": "JSON roto", "args": con_raiz("est", "--modo", "aviso"), "entrada": b"{"},
    ] + ([{"nombre": "heredero %s" % modo, "args": con_raiz("her", "--modo", modo), "entrada": {"session_id": s},
           "preparar": sesion_nueva("her")} for modo in ("inicio", "aviso") for s in (sesion_her, "s-nueva")]
         if hay_her else [])

    # hook_sesion
    C["hook_sesion.py"] = [
        {"nombre": "el estándar", "args": con_raiz("est"), "entrada": {}},
        {"nombre": "vacío", "args": con_raiz("vacio"), "entrada": {}},
        {"nombre": "sin --raiz (cwd del proceso)", "args": [], "entrada": {}},
    ] + ([{"nombre": "heredero", "args": con_raiz("her"), "entrada": {}}] if hay_her else [])

    # hook_historico
    def generico(m):
        escribir(os.path.join(m.est, "historico-chat", "2026-10-04-sesion.md"),
                 "<!-- sesion: s-gen -->\n# Sesión\n\n### 1 · Usuario · 10:00:00\n\nhola\n\n**Agente**\n\nlisto\n")
    C["hook_historico.py"] = [
        {"nombre": "usuario nuevo", "args": con_raiz("est", "--modo", "usuario"),
         "entrada": {"session_id": "s-nueva", "prompt": "hola con API_KEY=supersecreto123456"}},
        {"nombre": "usuario existente", "args": con_raiz("est", "--modo", "usuario"),
         "entrada": {"session_id": SESION_EST, "prompt": "seguimos"}},
        {"nombre": "usuario vacío", "args": con_raiz("est", "--modo", "usuario"),
         "entrada": {"session_id": "s-nueva", "prompt": "   "}},
        {"nombre": "pide el nombre", "args": con_raiz("est", "--modo", "usuario"), "preparar": generico,
         "entrada": {"session_id": "s-gen", "prompt": "y ahora"}},
        {"nombre": "agente", "args": con_raiz("est", "--modo", "agente"),
         "entrada": lambda m: {"session_id": SESION_EST, "transcript_path": m.transcript}},
        {"nombre": "agente sin archivo", "args": con_raiz("est", "--modo", "agente"),
         "entrada": lambda m: {"session_id": "no-hay", "transcript_path": m.transcript}},
        {"nombre": "sin modo, por cwd", "args": [], "entrada": lambda m: {"cwd": m.est, "session_id": "s-x",
                                                                         "prompt": "hola"}},
        {"nombre": "vacío", "args": con_raiz("vacio"), "entrada": {"session_id": "s", "prompt": "hola"}},
        {"nombre": "JSON roto", "args": con_raiz("est"), "entrada": b"{"},
    ] + ([{"nombre": "heredero %s" % modo, "args": con_raiz("her", "--modo", modo),
           "entrada": (lambda modo: lambda m: {"session_id": sesion_her, "prompt": "hola",
                                               "transcript_path": m.transcript})(modo)}
          for modo in ("usuario", "agente")] if hay_her else [])

    # hook_antes
    def antes(nombre, herramienta, entrada_herramienta, cual="est", sesion=SESION_EST, preparar=None):
        return {"nombre": nombre, "args": con_raiz(cual, "--modo", "accion"), "preparar": preparar,
                "entrada": lambda m: {"session_id": sesion, "tool_name": herramienta,
                                      "tool_input": entrada_herramienta(m), "cwd": m.raiz(cual)}}

    def resumen_de_her(m):
        """Que la sesión del heredero tenga resumen, para que el freno anote ahí."""
        if not sesion_her:
            return
        carpeta = os.path.join(m.her, "historico-chat")
        for nombre in sorted(os.listdir(carpeta)):
            ruta = os.path.join(carpeta, nombre)
            if nombre.endswith(".md") and "<!-- sesion: %s -->" % sesion_her in leer(ruta):
                escribir(os.path.join(carpeta, "resumenes", nombre[:10], nombre[11:]),
                         "# Resumen\n\n### H-1 · algo\n\n---\n\n## ¿Se puede cerrar la sesión?\n\n| a |\n")
    C["hook_antes.py"] = [
        antes("Write en base", "Write", lambda m: {"file_path": os.path.join(m.est, "base", "x.md"), "content": "x"}),
        antes("Write en el análisis", "Write", lambda m: {"file_path": os.path.join(
            m.est, "historico-chat", "resumenes", "2026-10-04", "x.md")}),
        antes("Write afuera", "Write", lambda m: {"file_path": os.path.join(m.otro, "x.py")}),
        antes("Edit relativo", "Edit", lambda m: {"file_path": "pendientes/x.md"}),
        antes("Write sin ruta", "Write", lambda m: {}),
        antes("Bash redirige", "Bash", lambda m: {"command": "echo hola > base/y.md"}),
        antes("Bash afuera", "Bash", lambda m: {"command": "echo hola > %s/z.txt" % m.otro.replace("\\", "/")}),
        antes("Bash git status", "Bash", lambda m: {"command": "git status"}),
        antes("Bash pip", "Bash", lambda m: {"command": "pip install requests"}),
        antes("Bash segundo plano", "Bash", lambda m: {"command": "python x.py", "run_in_background": True}),
        antes("PowerShell", "PowerShell", lambda m: {"command": "Set-Content -Path base/q.md -Value x"}),
        antes("Read", "Read", lambda m: {"file_path": os.path.join(m.est, "README.md")}),
        antes("publica", "mcp__gmail__send", lambda m: {"to": "x"}),
        {"nombre": "sin modo", "args": con_raiz("est"), "entrada": {"tool_name": "Write"}},
        {"nombre": "JSON roto", "args": con_raiz("est", "--modo", "accion"), "entrada": b"{"},
        {"nombre": "cwd del proceso", "args": ["--modo", "accion"],
         "entrada": lambda m: {"tool_name": "Write", "tool_input": {"file_path": os.path.join(m.est, "base", "x.md")}}},
    ] + ([
        antes("heredero Write", "Write", lambda m: {"file_path": os.path.join(m.her, "app", "x.py")}, "her",
              sesion_her, resumen_de_her),
        antes("heredero Bash", "Bash", lambda m: {"command": "echo x > app/y.py"}, "her", sesion_her, resumen_de_her),
        antes("heredero Bash foto", "Bash", lambda m: {"command": "ls"}, "her", sesion_her,
              lambda m: escribir(os.path.join(m.her, "app", "suelto.py"), "x\n")),
    ] if hay_her else [])

    # hook_despues
    def foto_vacia_y_cambios(cual):
        def preparar(m):
            raiz = m.raiz(cual)
            escribir(os.path.join(raiz, ".git", "cimiento-freno.json"), "{}")
            escribir(os.path.join(raiz, "base", "cambio.md"), "x\n")
            escribir(os.path.join(raiz, "README.md"), "\notra\n", "a")
            escribir(os.path.join(raiz, "historico-chat", "resumenes", "2026-10-04", "nota.md"), "x\n")
            if cual == "her":
                resumen_de_her(m)
        return preparar

    def despues(nombre, herramienta, orden, cual="est", sesion=SESION_EST, preparar=True):
        return {"nombre": nombre, "args": con_raiz(cual), "preparar": foto_vacia_y_cambios(cual) if preparar else None,
                "entrada": {"session_id": sesion, "tool_name": herramienta, "tool_input": {"command": orden}}}
    C["hook_despues.py"] = [
        despues("Bash", "Bash", "python x.py"),
        despues("PowerShell", "PowerShell", "python x.py"),
        despues("solo registra", "Bash", "git add -A && git commit -m 'x; y'"),
        despues("sin foto", "Bash", "python x.py", preparar=False),
        despues("Read", "Read", ""),
        {"nombre": "JSON roto", "args": con_raiz("est"), "entrada": b"{"},
        {"nombre": "cwd del proceso", "args": [], "preparar": foto_vacia_y_cambios("est"),
         "entrada": {"tool_name": "Bash", "tool_input": {"command": "x"}}},
    ] + ([despues("heredero", "Bash", "python x.py", "her", sesion_her)] if hay_her else [])

    return C


# Del de menos riesgo al de más: el orden en que se cambian.
ORDEN = ["hook_turno.py", "hook_veredicto.py", "hook_rutas.py", "hook_acuerdos.py", "hook_checkpoint.py",
         "hook_externo.py", "hook_presupuesto.py", "hook_senales.py", "hook_recuerdos.py",
         "hook_relacionadas.py", "hook_redaccion.py", "hook_checklist.py", "hook_estacion.py", "hook_md.py",
         "hook_analisis.py", "hook_resumen.py", "hook_reglas.py", "hook_sesion.py",
         "hook_antes.py", "hook_despues.py", "hook_historico.py"]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--solo", default="", help="enganches separados por coma (con o sin .py)")
    p.add_argument("--heredero", default=HEREDERO)
    a = p.parse_args()
    pedidos = [h if h.endswith(".py") else h + ".py" for h in a.solo.split(",") if h]
    todo_bien = True
    with tempfile.TemporaryDirectory(prefix="pe-") as tmp:
        try:
            mundo = Mundo(tmp, a.heredero)
            casos = casos_simples(mundo)
            for hook in ORDEN:
                if pedidos and hook not in pedidos:
                    continue
                viejo_txt, nuevo_txt = version_vieja(hook), version_nueva(hook)
                iguales = 0
                for caso in casos[hook]:
                    viejo = correr(mundo, hook, viejo_txt, caso)
                    nuevo = correr(mundo, hook, nuevo_txt, caso)
                    diferencias = comparar(viejo, nuevo)
                    if diferencias:
                        todo_bien = False
                        print("  DISTINTO %s · %s" % (hook, caso["nombre"]))
                        for d in diferencias:
                            print("    " + d)
                    else:
                        iguales += 1
                        print("  igual    %s · %s (%.1f s / %.1f s, código %s, %d car. de salida, %d de errores, "
                              "%d escrito(s))" % (hook, caso["nombre"], viejo["segundos"], nuevo["segundos"],
                                                  viejo["codigo"], len(viejo["salida"]), len(viejo["errores"]),
                                                  len(viejo["escrito"])))
                print("%-24s %d/%d casos iguales%s" % (hook, iguales, len(casos[hook]),
                                                       "" if viejo_txt != nuevo_txt else " (sin cambiar todavía)"))
        finally:
            os.chdir(RAIZ)
            try:
                borrar(tmp)
            except OSError:
                pass
    print("\nPARIDAD COMPLETA" if todo_bien else "\nHAY DIFERENCIAS")
    return 0 if todo_bien else 1


if __name__ == "__main__":
    sys.exit(main())
