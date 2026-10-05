"""`EP-023 · HU-007 · CA-02` · El freno: nada se escribe fuera del plan aprobado ni de lo autorizado.

**Qué decide.** Antes de cada acción, si se deja: lo que el plan de la fase en
curso declara, lo que una regla autoriza (`autorizado`) y lo que el análisis
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
paquetes fuera del proyecto, la configuración global y el proceso que queda
corriendo. Lo que se publica fuera del proyecto se pregunta cada vez.

**Después de actuar** se compara lo que cambió en git con una foto tomada justo
antes de la orden: así se ve lo que un programa escribió por dentro, aunque solo
dentro del proyecto.

**Al detener, anota el hallazgo** en el resumen de la sesión (acuerdos 18 y 44
del análisis 1): la ejecución se detiene y vuelve al análisis.

**Cada regla tiene su nivel en el proyecto** (`EP-025·HU-005`). Cuando el freno
detiene por una regla, mira su nivel en la base de Cimiento: «frena» detiene,
«avisa» deja hacer y avisa, «apagada» deja hacer. El núcleo siempre frena. La
regla sale del motivo, que siempre la nombra entre paréntesis. Sin base no se
sabe ningún nivel, y entonces no se deja modificar nada; leer sigue pasando
(análisis 1 del pendiente 119, acuerdos 13 y 15).
"""
import datetime
import json
import os
import re
import shlex

from ..comun import Archivos, Git, Proyecto
from ..niveles.catalogo import es_del_nucleo
from .acuerdos import Acuerdos
from .analisis_en_curso import AnalisisEnCurso
from .autorizado import Autorizaciones
from .niveles import BaseSinRespuesta, NivelesDelProyecto
from .origen import LectorDeAnalisis
from .plan_vs_hecho import PlanDeTrabajo
from .resumen import CARPETA as HISTORICO
from .resumen import Resumen

FRENA, AVISA, APAGADA = "frena", "avisa", "apagada"
_REGLA_DEL_MOTIVO = re.compile(r"\((\d{2}·[A-Z]{1,4}\d+(?:\.\d+)?)\)")
SIN_BASE = ("%s. Sin la base no se sabe el nivel de cada regla, y no se deja modificar nada; "
            "leer sigue permitido (análisis 1 del pendiente 119, acuerdo 15)")

ESCRITURA = ("Write", "Edit", "MultiEdit", "NotebookEdit")
CONSOLA = ("Bash", "PowerShell")
_PUBLICA = re.compile(
    r"^(?:Artifact|mcp__.+__(?:create|update|delete|batch|send|post|publish|upload|write|edit|comment)\w*)$",
    re.I)
FOTO = os.path.join(".git", "cimiento-freno.json")
_NULOS = {"/dev/null", "nul", "$null", "&1", "&2"}

# Lo que «Corrija» deja corregir sin análisis: las herramientas del proceso
# (análisis 16 del pendiente 103, acuerdo 2). Desde que pasaron a clases, también
# viven en `proyectos/cimiento/core/` (sesión del 2026-10-04, «Corrija»).
HERRAMIENTAS = ("validadores/", "adaptadores/", "proyectos/cimiento/core/")

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
_INSTALA = re.compile(r"(?:\bpip3?(?:\.exe)?|-m\s+pip)\s+install\b", re.I)
_OTROS_INSTALADORES = re.compile(r"\b(?:npm|apt|apt-get|brew|choco|winget|gem)\b", re.I)
_HEREDOC = re.compile(r"<<-?\s*(['\"]?)(\w+)\1[^\n]*\n.*?^\s*\2\s*$", re.S | re.M)

# Las órdenes de git que solo registran lo que ya cambió. No escriben contenido:
# lo que entra al commit lo revisa el `pre-commit` (`validar.py plan`). Revisarlas
# acá frenaba todo commit con archivos nuevos (sesión del 2026-10-04).
_SOLO_REGISTRA = re.compile(r"^\s*git(\s+-C\s+(\"[^\"]*\"|'[^']*'|\S+))?\s+(add|commit|push|status|log|diff|show)\b")

_CIERRE = "\n---\n\n## ¿Se puede cerrar la sesión?"
_H = re.compile(r"^### H-(\d+)\b", re.M)


class Freno:
    """Decide sobre cada acción del agente en un proyecto."""

    def __init__(self, proyecto, archivos=None, niveles=None):
        self.proyecto = proyecto if isinstance(proyecto, Proyecto) else Proyecto(proyecto)
        self.archivos = archivos or Archivos()
        self.niveles = niveles or NivelesDelProyecto(self.proyecto.raiz)

    @property
    def raiz(self):
        return self.proyecto.raiz

    # ── lo que se permite ─────────────────────────────────────────────────

    @staticmethod
    def rutas_de_una(analisis, archivos=None):
        """Las rutas exactas que un análisis manda hacer «de una y sin fase»."""
        rutas = set()
        for celdas in LectorDeAnalisis.leer(analisis, archivos)["hacer"].values():
            if len(celdas) > 2 and re.search(r"(?i)de una", celdas[2]):
                # Los análisis nombran las rutas en «Pasó a»; también se leen en la
                # primera columna (análisis 14 del pendiente 103, acuerdo 2).
                texto = celdas[0] + " " + celdas[2]
                # Solo se quita un `./` del comienzo: `lstrip("./")` borraba también
                # el punto de `.gitignore` (sesión del 2026-10-04).
                rutas |= {re.sub(r"^(\./)+", "", r.strip()) for r in re.findall(r"`([^`]+)`", texto)
                          if "/" in r or "." in r}
        return rutas

    def de_una(self):
        """Las rutas exactas que el análisis prendido manda hacer «de una y sin fase»."""
        estado = AnalisisEnCurso(self.raiz).leer_estado()
        if not estado or not os.path.isfile(estado["analisis"]):
            return set()
        return self.rutas_de_una(estado["analisis"], self.archivos)

    def permitido(self):
        """Lo que se deja escribir hoy en el proyecto."""
        fases = []
        for ruta in Acuerdos(self.proyecto, self.archivos).fases_en_curso():
            plan = os.path.join(ruta, "plan_trabajo.md")
            texto = self.archivos.leer(plan) if os.path.isfile(plan) else ""
            aprobado = PlanDeTrabajo.aprobado(plan, texto)
            fases.append((self.proyecto.relativa(os.path.realpath(ruta)), aprobado,
                          set(PlanDeTrabajo.rutas_exactas(texto)) if aprobado else set()))
        return {"fases": fases, "reglas": Autorizaciones(self.archivos).reglas(self.raiz),
                "de_una": self.de_una(), "corrija": AnalisisEnCurso(self.raiz).corrija_activo()}

    def motivo(self, ruta_abs, lo_permitido):
        """`None` si se deja escribir esa ruta; si no, por qué no."""
        rel = self.proyecto.relativa(ruta_abs)
        if rel is None:
            return "queda fuera del proyecto (04·S9)"
        if rel == ".git" or rel.startswith(".git/"):
            return None             # lo de git lo escribe git
        if Autorizaciones.quien_autoriza(rel, lo_permitido["reglas"]) or rel in lo_permitido["de_una"]:
            return None
        if lo_permitido.get("corrija") and rel.startswith(HERRAMIENTAS):
            return None
        for carpeta, aprobado, declarados in lo_permitido["fases"]:
            if rel.startswith(carpeta + "/") or (aprobado and rel in declarados):
                return None
            # La carpeta de un archivo declarado: crearla es parte de crearlo
            # (análisis 1 del pendiente 110, acuerdo 2).
            if aprobado and any(d.startswith(rel.rstrip("/") + "/") for d in declarados):
                return None
        if not lo_permitido["fases"]:
            return "no hay una fase en curso y ninguna regla autoriza escribirlo (02·F8)"
        return "el plan de la fase en curso no lo declara, o no está aprobado, y ninguna regla lo autoriza (02·F8)"

    # ── la acción ─────────────────────────────────────────────────────────

    @staticmethod
    def publica(herramienta):
        return bool(_PUBLICA.match(herramienta or ""))

    def instala_en_el_proyecto(self, orden, cwd):
        """Si cada instalación de paquetes de la orden corre con el intérprete o el
        instalador de un entorno que está dentro del proyecto (`venv/`, `.venv/`):
        instala ahí, no fuera (pendiente 115; análisis 1 del pendiente 110, acuerdo 8)."""
        if _OTROS_INSTALADORES.search(orden or ""):
            return False
        hay = False
        for parte in self.partes(orden or ""):
            if not _INSTALA.search(parte):
                continue
            hay = True
            palabras = self.palabras(parte)
            if not palabras:
                return False
            programa = Proyecto.ruta_real(palabras[0], cwd or self.raiz)
            if not self.proyecto.contiene(programa):
                return False
            if not set(programa.replace("\\", "/").lower().split("/")) & {"venv", ".venv", "env", ".env"}:
                return False
        return hay

    def nunca(self, orden, en_segundo_plano=False, cwd=None):
        """Por qué esa orden no se deja nunca, o `None`."""
        if en_segundo_plano:
            return "corre en segundo plano y deja su salida fuera del proyecto (04·S9)"
        # El texto de un heredoc es lo que recibe el programa, no una orden de la
        # consola (análisis 1 del pendiente 110, acuerdo 8).
        orden = self.sin_heredoc(orden)
        for patron, porque in _NUNCA:
            if patron.search(orden or ""):
                if porque.startswith("instala paquetes") and self.instala_en_el_proyecto(orden, cwd):
                    continue
                return porque
        return None

    @staticmethod
    def partes(orden):
        return [p.strip() for p in re.split(r"&&|\|\||;|\n|(?<!\|)\|(?!\|)", orden) if p.strip()]

    @staticmethod
    def palabras(parte):
        try:
            return shlex.split(parte, posix=True)
        except ValueError:
            return parte.split()

    @staticmethod
    def archivos_de_sed(palabras):
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

    @staticmethod
    def sin_heredoc(orden):
        """La orden sin el texto de sus heredocs: es lo que recibe el programa, no la
        consola (análisis 16 del pendiente 103, acuerdo 2). Se conserva la línea que
        abre el heredoc, que es donde va la redirección real."""
        return _HEREDOC.sub(lambda m: m.group(0).split("\n", 1)[0], orden or "")

    @classmethod
    def destinos(cls, orden):
        """Las rutas que una orden de consola escribe o borra, tal como están escritas."""
        orden = cls.sin_heredoc(orden)
        # Un `>` dentro de comillas es texto, no una redirección (análisis 13 del
        # pendiente 103, acuerdo 7): se borra antes de buscarlas.
        sin_texto = _ENTRE_COMILLAS.sub(lambda m: m.group(0).replace(">", " "), orden or "")
        salida = [m.strip("\"'") for m in _REDIRECCION.findall(sin_texto)]
        for parte in cls.partes(orden or ""):
            palabras = [p for p in cls.palabras(parte) if not re.match(r"^\w+=", p)]
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
                salida += cls.archivos_de_sed(palabras[1:])
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
        # Dentro de `$( … )` el destino queda pegado al paréntesis que cierra:
        # `/dev/null)` sigue siendo el dispositivo nulo (análisis 1 del pendiente 110).
        salida = [s.rstrip(")") if s.rstrip(")").lower() in _NULOS else s for s in salida]
        return [s for s in salida if s and s.lower() not in _NULOS]

    # ── el nivel de la regla ──────────────────────────────────────────────

    @staticmethod
    def regla_de(porque):
        """La regla que nombra el motivo (`02·F8`), o `None`."""
        encontradas = _REGLA_DEL_MOTIVO.findall(porque or "")
        return encontradas[-1] if encontradas else None

    @staticmethod
    def nivel_para(regla, niveles):
        if not regla or es_del_nucleo(regla):
            return FRENA
        return niveles.get(regla, FRENA)

    def modifica(self, herramienta, entrada, cwd=None):
        """¿La acción escribe? La herramienta de escritura siempre; la consola, si
        tiene destinos o es de las que nunca se dejan."""
        if herramienta in ESCRITURA:
            return bool(entrada.get("file_path") or entrada.get("notebook_path"))
        if herramienta in CONSOLA:
            orden = entrada.get("command") or ""
            return bool(self.nunca(orden, bool(entrada.get("run_in_background")), cwd) or self.destinos(orden))
        return False

    def con_nivel(self, decision, modifica):
        """Aplica el nivel de la regla a la decisión. Sin base, lo que modifica
        se detiene con `sin_base`; lo que solo lee pasa."""
        accion, porque, ruta = decision
        if accion == "pregunta" or (accion == "deja" and not modifica):
            return decision
        try:
            niveles = self.niveles.todos()
        except BaseSinRespuesta as error:
            if not modifica:
                return decision
            motivo = str(error)
            return ("sin_base", SIN_BASE % (motivo[:1].upper() + motivo[1:]), ruta)
        if accion == "deja":
            return decision
        nivel = self.nivel_para(self.regla_de(porque), niveles)
        if nivel == AVISA:
            return ("avisa", porque, ruta)
        if nivel == APAGADA:
            return ("deja", "", "")
        return decision

    def revisar(self, herramienta, entrada, cwd=None):
        """`(decisión, motivo, ruta)`: «deja», «detiene», «avisa», «pregunta» o
        «sin_base»."""
        entrada = entrada or {}
        decision = self.decidir(herramienta, entrada, cwd)
        return self.con_nivel(decision, self.modifica(herramienta, entrada, cwd or self.raiz))

    def decidir(self, herramienta, entrada, cwd=None):
        """La decisión con lo que está en el código, sin mirar niveles."""
        entrada = entrada or {}
        cwd = cwd or self.raiz
        if self.publica(herramienta):
            return ("pregunta", "publica fuera del proyecto, y eso no se deshace (00·N1)", "")
        if herramienta in ESCRITURA:
            ruta = entrada.get("file_path") or entrada.get("notebook_path") or ""
            if not ruta:
                return ("deja", "", "")
            ruta_abs = Proyecto.ruta_real(ruta, cwd)
            porque = self.motivo(ruta_abs, self.permitido())
            return ("detiene", porque, self.proyecto.relativa(ruta_abs) or ruta) if porque else ("deja", "", "")
        if herramienta in CONSOLA:
            orden = entrada.get("command") or ""
            porque = self.nunca(orden, bool(entrada.get("run_in_background")), cwd)
            if porque:
                return ("detiene", porque, "")
            lo_permitido = None
            for ruta in self.destinos(orden):
                lo_permitido = lo_permitido or self.permitido()
                ruta_abs = Proyecto.ruta_real(ruta, cwd)
                porque = self.motivo(ruta_abs, lo_permitido)
                if porque:
                    return ("detiene", porque, self.proyecto.relativa(ruta_abs) or ruta)
        return ("deja", "", "")

    # ── después de actuar ─────────────────────────────────────────────────

    def cambiados(self):
        """`{ruta: firma}` de lo que git ve cambiado o nuevo."""
        salida = {}
        items = iter(Git(self.raiz, espera=30).correr("status", "--porcelain", "-uall", "-z").split("\0"))
        for item in items:
            if len(item) < 4:
                continue
            # Un renombrado o una copia (`R`, `C`) trae la ruta vieja en el campo
            # siguiente. Leída como un archivo más, le cortaba tres letras y salía
            # «taforma/…» como escrito fuera del plan (sesión del 2026-10-04).
            if item[0] in "RC":
                next(items, None)
            ruta = item[3:].replace("\\", "/")
            try:
                st = os.stat(self.proyecto.ruta(ruta))
                salida[ruta] = "%d:%d" % (st.st_mtime_ns, st.st_size)
            except OSError:
                salida[ruta] = "borrado"
        return salida

    def tomar_foto(self):
        """Guarda en `.git/` lo que estaba cambiado justo antes de la orden."""
        ruta = os.path.join(self.raiz, FOTO)
        if not os.path.isdir(os.path.dirname(ruta)):
            return
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(self.cambiados(), f)

    @classmethod
    def solo_registra(cls, orden):
        """¿Cada parte de la orden es un `git` que solo registra o consulta? Lo que
        va entre comillas es texto (el mensaje del commit): un `;` adentro no parte
        la orden."""
        sin_comillas = re.sub(r"'[^']*'|\"[^\"]*\"", "''", cls.sin_heredoc(orden))
        partes = [p for p in cls.partes(sin_comillas) if not re.match(r"^\s*cd\s", p)]
        return bool(partes) and all(_SOLO_REGISTRA.match(p) for p in partes)

    def despues(self, orden=""):
        """`[(ruta, motivo)]` de lo que cambió desde la foto, no se permite y frena."""
        return self.despues_por_nivel(orden)[0]

    def despues_por_nivel(self, orden=""):
        """`(frenan, avisan)`, cada una `[(ruta, motivo)]`, con el nivel de su
        regla aplicado. Sin base, lo que cambió no se puede juzgar: va un solo
        aviso de base apagada en `frenan`, con la ruta vacía."""
        fuera = self.fuera_del_plan(orden)
        if not fuera:
            return [], []
        try:
            niveles = self.niveles.todos()
        except BaseSinRespuesta as error:
            motivo = str(error)
            return [("", SIN_BASE % (motivo[:1].upper() + motivo[1:]))], []
        frenan, avisan = [], []
        for rel, porque in fuera:
            nivel = self.nivel_para(self.regla_de(porque), niveles)
            if nivel == AVISA:
                avisan.append((rel, porque))
            elif nivel != APAGADA:
                frenan.append((rel, porque))
        return frenan, avisan

    def fuera_del_plan(self, orden=""):
        """`[(ruta, motivo)]` de lo que cambió desde la foto y no se permite, sin niveles."""
        if self.solo_registra(orden):
            return []
        try:
            with open(os.path.join(self.raiz, FOTO), encoding="utf-8") as f:
                antes = json.load(f)
        except (OSError, ValueError):
            return []
        ahora = self.cambiados()
        lo_permitido = self.permitido()
        salida = []
        for rel, firma in sorted(ahora.items()):
            if antes.get(rel) == firma:
                continue
            porque = self.motivo(os.path.realpath(self.proyecto.ruta(rel)), lo_permitido)
            if porque:
                salida.append((rel, porque))
        return salida

    # ── el hallazgo ───────────────────────────────────────────────────────

    def transcripcion_de(self, sesion):
        """La transcripción que lleva la marca de esa sesión, o ""."""
        carpeta = os.path.join(self.raiz, HISTORICO)
        marca = "<!-- sesion: %s -->" % sesion
        if not sesion or not os.path.isdir(carpeta):
            return ""
        for nombre in sorted(os.listdir(carpeta)):
            ruta = os.path.join(carpeta, nombre)
            if nombre.endswith(".md") and os.path.isfile(ruta) and marca in self.archivos.leer(ruta):
                return ruta
        return ""

    def analisis_prendido(self):
        """`True` si hay un análisis que recibe la conversación y no se ha aprobado."""
        estado = AnalisisEnCurso(self.raiz).leer_estado()
        return bool(estado and os.path.isfile(estado["analisis"]) and not AnalisisEnCurso.aprobado(estado["analisis"]))

    def anotar_hallazgo(self, sesion, accion, ruta, porque, ahora=None):
        """Suma el hallazgo al resumen de la sesión. Devuelve la ruta del resumen, o "".

        Con un análisis prendido no anota: lo que aparece se reporta en la
        conversación y se resuelve en ese análisis (análisis 13 del pendiente 103,
        acuerdo 6).
        """
        if self.analisis_prendido():
            return ""
        transcripcion = self.transcripcion_de(sesion)
        destino = Resumen.ruta_de(self.raiz, transcripcion) if transcripcion else ""
        if not destino or not os.path.isfile(destino):
            return ""
        texto = self.archivos.leer(destino)
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

    @staticmethod
    def aviso_de_nivel(porque, ruta):
        """El texto que recibe el agente cuando la regla está en «avisa»: pasó, y se avisa."""
        donde = " (`%s`)" % ruta if ruta else ""
        return ("[EL FRENO AVISA%s]\n%s.\nLa regla está en «avisa» en este proyecto: la acción pasó. "
                "Su nivel se cambia en Cimiento, en las reglas del proyecto." % (donde, porque[0].upper() + porque[1:]))

    @staticmethod
    def aviso_sin_base(porque):
        """El texto que recibe el agente cuando no hay base: no es un hallazgo."""
        return "[EL FRENO NO TIENE BASE DE DATOS]\n%s." % porque

    @staticmethod
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
