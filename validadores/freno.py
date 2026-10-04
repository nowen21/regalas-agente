# -*- coding: utf-8 -*-
"""`EP-023 · HU-007 · CA-02` · El freno: nada se escribe fuera del plan aprobado ni de lo autorizado.

**Qué decide.** Antes de cada acción, si se deja: lo que el plan de la fase en
curso declara, lo que una regla autoriza (`autorizado.py`) y lo que el análisis
prendido manda hacer «de una y sin fase» pasan; lo demás se detiene (análisis 1
del pendiente 103, acuerdo 46; análisis 10, acuerdo 6).

- Con la fase en curso y su plan sin aprobar: solo los documentos de la fase.
- Con el plan aprobado: también las rutas exactas de su tabla 2.1.
- Sin fase en curso: solo lo autorizado.

**Por su efecto, no por la herramienta** (análisis 8, acuerdos 1 y 3). La
herramienta de escritura dice su archivo; de una orden de consola se sacan sus
destinos (redirecciones, órdenes que crean, copian, mueven o borran, y las de
git que descartan cambios), y la ruta se resuelve antes de comparar: `..`, `~`,
variables y enlaces. Hay acciones que nunca se dejan: el segundo plano, instalar
paquetes, la configuración global y el proceso que queda corriendo. Lo que se
publica fuera del proyecto se pregunta cada vez.

**Después de actuar** se compara lo que cambió en git con una foto tomada justo
antes de la orden: así se ve lo que un programa escribió por dentro, aunque solo
dentro del proyecto.

**Al detener, anota el hallazgo** en el resumen de la sesión (acuerdos 18 y 44
del análisis 1): la ejecución se detiene y vuelve al análisis.
"""
import datetime
import json
import os
import re
import shlex
import subprocess

import acuerdos
import analisis_en_curso as curso
import autorizado
import comun
import origen
import plan_vs_hecho
import resumen

ESCRITURA = ("Write", "Edit", "MultiEdit", "NotebookEdit")
CONSOLA = ("Bash", "PowerShell")
_PUBLICA = re.compile(
    r"^(?:Artifact|mcp__.+__(?:create|update|delete|batch|send|post|publish|upload|write|edit|comment)\w*)$",
    re.I)
FOTO = os.path.join(".git", "cimiento-freno.json")
_NULOS = {"/dev/null", "nul", "$null", "&1", "&2"}

# Lo que nunca se deja: escribe fuera del proyecto o actúa sin que nadie mire.
_NUNCA = [
    (re.compile(r"(?:^|[;|&]\s*)nohup\b|(?<![&|])&\s*$|\bStart-Process\b|\bschtasks\b|\bcrontab\b", re.I),
     "deja un proceso corriendo después del turno (04·S10)"),
    (re.compile(r"\b(?:pip3?|python\s+-m\s+pip)\s+install\b|\bnpm\s+(?:install|i)\s+(?:-g|--global)\b|"
                r"\b(?:apt|apt-get|brew|choco|winget|gem)\s+install\b", re.I),
     "instala paquetes fuera del proyecto (04·S9)"),
    (re.compile(r"\bgit\s+config\s+--(?:global|system)\b|\bsetx\b|SetEnvironmentVariable|\breg\s+add\b", re.I),
     "cambia la configuración de la máquina (04·S9)"),
    (re.compile(r"\bgit\s+(?:clean\b|reset\s+--hard\b|checkout\s+\.(?:\s|$)|restore\s+\.(?:\s|$))", re.I),
     "descarta cambios de todo el proyecto (02·F8)"),
]

# `>=` compara, no redirige (análisis 15 del pendiente 103, acuerdo 1).
_REDIRECCION = re.compile(r"(?<![<>&\d=])(?:\d?>>?|&>>?)(?!=)\s*(\"[^\"]+\"|'[^']+'|[^\s;|&<>]+)")
_ENTRE_COMILLAS = re.compile(r"\"[^\"]*\"|'[^']*'")
_PS_RUTA = re.compile(r"-(?:FilePath|Path|LiteralPath|Destination)\s+(\"[^\"]+\"|'[^']+'|[^\s;|]+)", re.I)
_PS_ESCRIBE = re.compile(r"\b(?:Out-File|Set-Content|Add-Content|New-Item|Remove-Item|Copy-Item|Move-Item|Rename-Item)\b", re.I)


# ── la ruta ──────────────────────────────────────────────────────────────────

def ruta_real(ruta, cwd):
    """La ruta absoluta y resuelta: variables, `~`, `..` y enlaces."""
    ruta = os.path.expanduser(os.path.expandvars(ruta.strip().strip("\"'")))
    if not os.path.isabs(ruta):
        ruta = os.path.join(cwd, ruta)
    return os.path.realpath(ruta)


def relativa(proyecto, ruta_abs):
    """La ruta dentro del proyecto, con `/`, o `None` si queda afuera."""
    raiz = os.path.normcase(os.path.realpath(proyecto)).rstrip(os.sep)
    destino = os.path.normcase(ruta_abs)
    if destino != raiz and not destino.startswith(raiz + os.sep):
        return None
    return os.path.relpath(ruta_abs, os.path.realpath(proyecto)).replace("\\", "/")


# ── lo que se permite ────────────────────────────────────────────────────────

def _de_una(proyecto):
    """Las rutas exactas que el análisis prendido manda hacer «de una y sin fase»."""
    estado = curso.leer_estado(proyecto)
    if not estado or not os.path.isfile(estado["analisis"]):
        return set()
    return rutas_de_una(estado["analisis"])


def rutas_de_una(analisis):
    """Las rutas exactas que un análisis manda hacer «de una y sin fase»."""
    rutas = set()
    for celdas in origen.leer_analisis(analisis)["hacer"].values():
        if len(celdas) > 2 and re.search(r"(?i)de una", celdas[2]):
            # Los análisis nombran las rutas en «Pasó a»; también se leen en la
            # primera columna (análisis 14 del pendiente 103, acuerdo 2).
            texto = celdas[0] + " " + celdas[2]
            rutas |= {r.strip().lstrip("./") for r in re.findall(r"`([^`]+)`", texto) if "/" in r or "." in r}
    return rutas


def permitido(proyecto):
    """Lo que se deja escribir hoy en el proyecto."""
    fases = []
    for ruta in acuerdos.fases_en_curso(proyecto):
        texto = comun.leer(os.path.join(ruta, "plan_trabajo.md")) if os.path.isfile(
            os.path.join(ruta, "plan_trabajo.md")) else ""
        aprobado = plan_vs_hecho.aprobado_desde(texto)
        fases.append((relativa(proyecto, os.path.realpath(ruta)), aprobado,
                      set(plan_vs_hecho.rutas_exactas(texto)) if aprobado else set()))
    return {"fases": fases, "reglas": autorizado.reglas(proyecto), "de_una": _de_una(proyecto),
            "corrija": curso.corrija_activo(proyecto)}


# Lo que «Corrija» deja corregir sin análisis: las herramientas del proceso
# (análisis 16 del pendiente 103, acuerdo 2).
HERRAMIENTAS = ("validadores/", "adaptadores/")


def motivo(proyecto, ruta_abs, lo_permitido):
    """`None` si se deja escribir esa ruta; si no, por qué no."""
    rel = relativa(proyecto, ruta_abs)
    if rel is None:
        return "queda fuera del proyecto (04·S9)"
    if rel == ".git" or rel.startswith(".git/"):
        return None             # lo de git lo escribe git
    if autorizado.quien_autoriza(rel, lo_permitido["reglas"]) or rel in lo_permitido["de_una"]:
        return None
    if lo_permitido.get("corrija") and rel.startswith(HERRAMIENTAS):
        return None
    for carpeta, aprobado, declarados in lo_permitido["fases"]:
        if rel.startswith(carpeta + "/") or (aprobado and rel in declarados):
            return None
    if not lo_permitido["fases"]:
        return "no hay una fase en curso y ninguna regla autoriza escribirlo (02·F8)"
    return "el plan de la fase en curso no lo declara, o no está aprobado, y ninguna regla lo autoriza (02·F8)"


# ── la acción ────────────────────────────────────────────────────────────────

def publica(herramienta):
    return bool(_PUBLICA.match(herramienta or ""))


def nunca(orden, en_segundo_plano=False):
    """Por qué esa orden no se deja nunca, o `None`."""
    if en_segundo_plano:
        return "corre en segundo plano y deja su salida fuera del proyecto (04·S9)"
    for patron, porque in _NUNCA:
        if patron.search(orden or ""):
            return porque
    return None


def _partes(orden):
    return [p.strip() for p in re.split(r"&&|\|\||;|\n|(?<!\|)\|(?!\|)", orden) if p.strip()]


def _palabras(parte):
    try:
        return shlex.split(parte, posix=True)
    except ValueError:
        return parte.split()


def _archivos_de_sed(palabras):
    """Los archivos de un `sed -i`: lo que va tras `-e` o `-f` es la orden, no un
    archivo, y sin ellos la primera palabra suelta es la orden (análisis 14 del
    pendiente 103, acuerdo 10)."""
    sueltas, con_orden, i = [], False, 0
    while i < len(palabras):
        p = palabras[i]
        if p in ("-e", "-f", "--expression", "--file"):
            con_orden, i = True, i + 2
            continue
        if p.startswith(("--expression=", "--file=")):
            con_orden = True
        elif not p.startswith("-"):
            sueltas.append(p)
        i += 1
    return sueltas if con_orden else sueltas[1:]


_HEREDOC = re.compile(r"<<-?\s*(['\"]?)(\w+)\1[^\n]*\n.*?^\s*\2\s*$", re.S | re.M)


def _sin_heredoc(orden):
    """La orden sin el texto de sus heredocs: es lo que recibe el programa, no la
    consola (análisis 16 del pendiente 103, acuerdo 2). Se conserva la línea que
    abre el heredoc, que es donde va la redirección real."""
    return _HEREDOC.sub(lambda m: m.group(0).split("\n", 1)[0], orden or "")


def destinos(orden):
    """Las rutas que una orden de consola escribe o borra, tal como están escritas."""
    orden = _sin_heredoc(orden)
    # Un `>` dentro de comillas es texto, no una redirección (análisis 13 del
    # pendiente 103, acuerdo 7): se borra antes de buscarlas.
    sin_texto = _ENTRE_COMILLAS.sub(lambda m: m.group(0).replace(">", " "), orden or "")
    salida = [m.strip("\"'") for m in _REDIRECCION.findall(sin_texto)]
    for parte in _partes(orden or ""):
        palabras = [p for p in _palabras(parte) if not re.match(r"^\w+=", p)]
        while palabras and palabras[0] in ("sudo", "command", "exec"):
            palabras = palabras[1:]
        if not palabras:
            continue
        cmd, args = palabras[0].lower(), [a for a in palabras[1:] if not a.startswith("-")]
        args = [a for a in args if not re.match(r"^\d?>>?|^&>", a)]
        if cmd in ("rm", "rmdir", "touch", "mkdir", "truncate", "unlink"):
            salida += args
        elif cmd in ("cp", "install", "ln") and args:
            salida.append(args[-1])
        elif cmd == "mv" and args:
            salida += args
        elif cmd == "tee":
            salida += args
        elif cmd == "sed" and any(p.startswith("-i") for p in palabras[1:]):
            salida += _archivos_de_sed(palabras[1:])
        elif cmd in ("curl", "wget"):
            for i, p in enumerate(palabras):
                if p in ("-o", "-O", "--output") and i + 1 < len(palabras):
                    salida.append(palabras[i + 1])
        elif cmd == "git" and len(palabras) > 1 and palabras[1] in ("checkout", "restore", "rm", "mv"):
            if "--" in palabras:
                salida += palabras[palabras.index("--") + 1:]
            elif palabras[1] in ("restore", "rm", "mv"):
                salida += args[1:]
        elif _PS_ESCRIBE.search(parte):
            salida += [m.strip("\"'") for m in _PS_RUTA.findall(parte)]
    return [s for s in salida if s and s.lower() not in _NULOS]


def revisar(proyecto, herramienta, entrada, cwd=None):
    """`(decisión, motivo, ruta)`: «deja», «detiene» o «pregunta»."""
    entrada = entrada or {}
    cwd = cwd or proyecto
    if publica(herramienta):
        return ("pregunta", "publica fuera del proyecto, y eso no se deshace (00·N1)", "")
    if herramienta in ESCRITURA:
        ruta = entrada.get("file_path") or entrada.get("notebook_path") or ""
        if not ruta:
            return ("deja", "", "")
        ruta_abs = ruta_real(ruta, cwd)
        porque = motivo(proyecto, ruta_abs, permitido(proyecto))
        return ("detiene", porque, relativa(proyecto, ruta_abs) or ruta) if porque else ("deja", "", "")
    if herramienta in CONSOLA:
        orden = entrada.get("command") or ""
        porque = nunca(orden, bool(entrada.get("run_in_background")))
        if porque:
            return ("detiene", porque, "")
        lo_permitido = None
        for ruta in destinos(orden):
            lo_permitido = lo_permitido or permitido(proyecto)
            ruta_abs = ruta_real(ruta, cwd)
            porque = motivo(proyecto, ruta_abs, lo_permitido)
            if porque:
                return ("detiene", porque, relativa(proyecto, ruta_abs) or ruta)
    return ("deja", "", "")


# ── después de actuar ────────────────────────────────────────────────────────

def _cambiados(proyecto):
    """`{ruta: firma}` de lo que git ve cambiado o nuevo."""
    try:
        r = subprocess.run(["git", "-C", proyecto, "status", "--porcelain", "-uall", "-z"],
                           capture_output=True, timeout=30)
    except (OSError, subprocess.SubprocessError):
        return {}
    salida = {}
    for item in r.stdout.decode("utf-8", "replace").split("\0"):
        if len(item) < 4:
            continue
        ruta = item[3:].replace("\\", "/")
        completa = os.path.join(proyecto, *ruta.split("/"))
        try:
            st = os.stat(completa)
            salida[ruta] = "%d:%d" % (st.st_mtime_ns, st.st_size)
        except OSError:
            salida[ruta] = "borrado"
    return salida


def tomar_foto(proyecto):
    """Guarda en `.git/` lo que estaba cambiado justo antes de la orden."""
    ruta = os.path.join(proyecto, FOTO)
    if not os.path.isdir(os.path.dirname(ruta)):
        return
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(_cambiados(proyecto), f)


def despues(proyecto):
    """`[(ruta, motivo)]` de lo que cambió desde la foto y no se permite."""
    ruta = os.path.join(proyecto, FOTO)
    try:
        with open(ruta, encoding="utf-8") as f:
            antes = json.load(f)
    except (OSError, ValueError):
        return []
    ahora = _cambiados(proyecto)
    lo_permitido = permitido(proyecto)
    salida = []
    for rel, firma in sorted(ahora.items()):
        if antes.get(rel) == firma:
            continue
        porque = motivo(proyecto, os.path.realpath(os.path.join(proyecto, *rel.split("/"))), lo_permitido)
        if porque:
            salida.append((rel, porque))
    return salida


# ── el hallazgo ──────────────────────────────────────────────────────────────

_CIERRE = "\n---\n\n## ¿Se puede cerrar la sesión?"
_H = re.compile(r"^### H-(\d+)\b", re.M)


def transcripcion_de(proyecto, sesion):
    """La transcripción que lleva la marca de esa sesión, o ""."""
    carpeta = os.path.join(proyecto, resumen.CARPETA)
    marca = "<!-- sesion: %s -->" % sesion
    if not sesion or not os.path.isdir(carpeta):
        return ""
    for nombre in sorted(os.listdir(carpeta)):
        ruta = os.path.join(carpeta, nombre)
        if nombre.endswith(".md") and os.path.isfile(ruta) and marca in comun.leer(ruta):
            return ruta
    return ""


def analisis_prendido(proyecto):
    """`True` si hay un análisis que recibe la conversación y no se ha aprobado."""
    estado = curso.leer_estado(proyecto)
    return bool(estado and os.path.isfile(estado["analisis"]) and not curso.aprobado(estado["analisis"]))


def anotar_hallazgo(proyecto, sesion, accion, ruta, porque, ahora=None):
    """Suma el hallazgo al resumen de la sesión. Devuelve la ruta del resumen, o "".

    Con un análisis prendido no anota: lo que aparece se reporta en la
    conversación y se resuelve en ese análisis (análisis 13 del pendiente 103,
    acuerdo 6).
    """
    if analisis_prendido(proyecto):
        return ""
    transcripcion = transcripcion_de(proyecto, sesion)
    destino = resumen.ruta_de(proyecto, transcripcion) if transcripcion else ""
    if not destino or not os.path.isfile(destino):
        return ""
    texto = comun.leer(destino)
    sujeto = "`%s`" % ruta if ruta else "una orden"
    if ruta and ("El freno detuvo" in texto and sujeto in texto):
        return destino          # ya está anotado
    ahora = ahora or datetime.datetime.now()
    numero = max([int(n) for n in _H.findall(texto)] or [0]) + 1
    bloque = ("\n\n### H-%d · El freno detuvo %s fuera del plan\n\n| Campo | Valor |\n|---|---|\n"
              "| Qué pasó | El %s, el freno detuvo %s sobre %s: %s. |\n"
              "| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: "
              "la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |\n"
              "| Pendiente | Por crear: lo decide el análisis siguiente del pendiente de la fase |\n"
              % (numero, accion, ahora.strftime("%Y-%m-%d %H:%M"), accion, sujeto, porque))
    i = texto.find(_CIERRE)
    texto = texto.rstrip("\n") + bloque if i < 0 else texto[:i].rstrip("\n") + bloque + texto[i:]
    with open(destino, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)
    return destino


def aviso(porque, ruta, anotado, prendido=False):
    """El texto que recibe el agente cuando el freno detiene."""
    donde = " (`%s`)" % ruta if ruta else ""
    if prendido:
        cierre = ("Hay un análisis prendido: reportarlo en la conversación y resolverlo ahí; "
                  "no va al resumen (análisis 13 del pendiente 103, acuerdo 6).")
    else:
        cierre = "Quedó anotado en el resumen de la sesión." if anotado else "Anotarlo en el resumen de la sesión."
    return ("[EL FRENO DETUVO ESTA ACCIÓN%s]\n%s.\n"
            "Es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, "
            "acuerdos 18 y 44). %s"
            % (donde, porque[0].upper() + porque[1:], cierre))


if __name__ == "__main__":
    comun.no_es_punto_de_entrada(la_corre="adaptadores/claude-code/hook_antes.py y hook_despues.py")
