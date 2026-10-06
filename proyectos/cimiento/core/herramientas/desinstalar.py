"""`EP-025·HU-021` · Quita el estándar de un proyecto: la contraria de `instalar.py`.

**Toda acción trae su contraria** (`02·F30`). La instalación pone enganches,
copias, la integración continua de Cimiento, carpetas y el registro; esto los
quita. **Lo propio del proyecto se queda**: `CLAUDE.md` y los cuatro archivos de
`.agente/` los llena el proyecto, y `historico-chat/`, la memoria y
`documentacion/versiones/` son su historia. Las líneas del `.gitignore` también
se quedan: sin ellas, `CLAUDE.md` y `.agente/` aparecerían para versionar.

**Solo se quita lo que se reconoce como de la instalación**: el enganche de git
con la marca del instalador, la entrada de Claude Code que llama al adaptador, la
integración continua con su aviso. Lo ajeno se queda.

Sin `aplicar`, dice qué quitaría y no toca nada.

    python validadores/instalar.py «ruta» --desinstalar [--aplicar]
"""
import json
import os
import re
import shutil
import subprocess

from ..comun.enganches import HOOKS_CLAUDE
from .instalar import (_CI_AVISO, _FILA, ADAPTADOR, CARPETAS_BASE, CI_GITHUB, CI_GITLAB, HOOKS, MARCA,
                       Instalador, _leer, _mandar_git)

_AVISO_CI = _CI_AVISO.splitlines()[0]


def _escribir(ruta, texto):
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


class Desinstalador:
    """Deshace en un proyecto lo que puso `Instalador`."""

    def __init__(self, instalador=None):
        self.instalador = instalador or Instalador()

    # ── los enganches ────────────────────────────────────────────────────

    @staticmethod
    def quitar_git(repo, aplicar):
        """Los enganches con la marca del instalador, y `core.hooksPath` si ya no queda nada."""
        pasos = []
        carpeta = os.path.join(repo, ".githooks")
        propios = [n for n, _p, _d in HOOKS
                   if os.path.isfile(os.path.join(carpeta, n)) and MARCA in _leer(os.path.join(carpeta, n))]
        for nombre in propios:
            pasos.append(f"quitar .githooks/{nombre}")
            if aplicar:
                os.remove(os.path.join(carpeta, nombre))
        ajenos = [n for n in (os.listdir(carpeta) if os.path.isdir(carpeta) else []) if n not in propios]
        if aplicar and os.path.isdir(carpeta) and not ajenos:
            os.rmdir(carpeta)
        if _mandar_git(repo, "config", "--get", "core.hooksPath").stdout.strip() == ".githooks":
            if ajenos:
                pasos.append("core.hooksPath se queda: .githooks/ tiene enganches que no son de Cimiento")
            else:
                pasos.append("git config --unset core.hooksPath")
                if aplicar:
                    _mandar_git(repo, "config", "--unset", "core.hooksPath")
        return pasos

    @staticmethod
    def quitar_claude(ruta, aplicar):
        """Las entradas de `.claude/settings.json` que llaman al adaptador; las demás se quedan."""
        archivo = os.path.join(ruta, ".claude", "settings.json")
        if not os.path.isfile(archivo):
            return []
        try:
            datos = json.loads(_leer(archivo) or "{}")
        except ValueError:
            return ["OMITIDO: .claude/settings.json tiene JSON inválido — no se toca"]
        guiones = {g for _e, _m, g, _msg, _a in HOOKS_CLAUDE}

        def propio(enganche):
            orden = (enganche.get("command") or "").replace("\\", "/")
            return ADAPTADOR in orden and any(g in orden for g in guiones)

        quitados = 0
        enganches = datos.get("hooks") or {}
        for evento in list(enganches):
            for grupo in enganches[evento]:
                antes = len(grupo.get("hooks", []))
                grupo["hooks"] = [h for h in grupo.get("hooks", []) if not propio(h)]
                quitados += antes - len(grupo["hooks"])
            enganches[evento] = [g for g in enganches[evento] if g.get("hooks")]
            if not enganches[evento]:
                del enganches[evento]
        if not quitados:
            return []
        if "hooks" in datos and not datos["hooks"]:
            del datos["hooks"]
        if aplicar:
            if datos:
                _escribir(archivo, json.dumps(datos, indent=2, ensure_ascii=False) + "\n")
            else:
                os.remove(archivo)
                if not os.listdir(os.path.dirname(archivo)):
                    os.rmdir(os.path.dirname(archivo))
        return [f"quitar {quitados} enganche(s) de Claude Code de .claude/settings.json"]

    # ── lo que se copió ──────────────────────────────────────────────────

    @staticmethod
    def quitar_copias(ruta, aplicar):
        """La copia del stack y la plantilla sellada del `CLAUDE.md`: no las llena nadie."""
        pasos = []
        stack = os.path.join(ruta, ".agente", "stack-instalacion.md")
        if os.path.isfile(stack):
            pasos.append("quitar .agente/stack-instalacion.md")
            if aplicar:
                os.remove(stack)
        selladas = os.path.dirname(Instalador.copia_sellada(ruta))
        if os.path.isdir(selladas):
            pasos.append("quitar .agente/plantillas-selladas/")
            if aplicar:
                shutil.rmtree(selladas)
        return pasos

    @staticmethod
    def quitar_ci(ruta, aplicar):
        """La integración continua de Cimiento, reconocida por su aviso."""
        pasos = []
        for rel in (CI_GITHUB, CI_GITLAB):
            archivo = os.path.join(ruta, *rel.split("/"))
            if os.path.isfile(archivo) and _AVISO_CI in _leer(archivo):
                pasos.append(f"quitar {rel}")
                if aplicar:
                    os.remove(archivo)
        gitlab = os.path.join(ruta, ".gitlab-ci.yml")
        if os.path.isfile(gitlab) and CI_GITLAB in _leer(gitlab):
            texto = _leer(gitlab)
            nuevo = texto.replace(f"\n\ninclude:\n  - local: {CI_GITLAB}\n", "\n")
            if nuevo == texto:
                nuevo = re.sub(r"(?m)^\s*- local: %s\s*\n" % re.escape(CI_GITLAB), "", texto)
            pasos.append(f"sacar {CI_GITLAB} de .gitlab-ci.yml")
            if aplicar:
                _escribir(gitlab, nuevo)
        return pasos

    @staticmethod
    def quitar_estructura(ruta, aplicar):
        """Las carpetas base que la instalación creó y siguen vacías."""
        pasos = []
        for nombre in CARPETAS_BASE:
            carpeta = os.path.join(ruta, nombre)
            if os.path.isdir(carpeta) and not os.listdir(carpeta):
                pasos.append(f"quitar {nombre}/, que está vacía")
                if aplicar:
                    os.rmdir(carpeta)
        return pasos

    # ── el registro ──────────────────────────────────────────────────────

    def quitar_registro(self, ruta, aplicar):
        """Saca el proyecto de `plantillas/proyectos.md` y lo da de baja en Cimiento."""
        registro = self.instalador.registro
        if not os.path.isfile(registro):
            return []
        esperado = os.path.normcase(os.path.abspath(ruta))

        def es_suya(linea):
            m = _FILA.match(linea.strip())
            celda = m.group(2).strip() if m else ""
            if not celda.startswith("`"):
                return False            # el encabezado, los guiones o una fila sin ruta
            return os.path.normcase(os.path.abspath(celda.strip("`").strip())) == esperado

        lineas = _leer(registro).split("\n")
        nuevas = [l for l in lineas if not es_suya(l)]
        if nuevas == lineas:
            return []
        if not aplicar:
            return ["sacar el proyecto de plantillas/proyectos.md y darlo de baja en Cimiento"]
        _escribir(registro, "\n".join(nuevas))
        if self.dar_de_baja(ruta):
            return ["sacar el proyecto de plantillas/proyectos.md y darlo de baja en Cimiento"]
        return ["sacar el proyecto de plantillas/proyectos.md"]

    def dar_de_baja(self, ruta):
        """`manage.py registrar --baja`, solo contra el registro real, como el alta."""
        if not self.instalador._registro_real():
            return False
        cimiento = os.path.join(self.instalador.estandar, "proyectos", "cimiento")
        manage = os.path.join(cimiento, "manage.py")
        python = Instalador.python_de_cimiento(cimiento)
        if not (os.path.isfile(manage) and python):
            return False
        r = subprocess.run([python, manage, "registrar", "--ruta", os.path.abspath(ruta), "--baja"],
                           capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
        return r.returncode == 0

    # ── lo del propio estándar ───────────────────────────────────────────

    def quitar_vigilante(self, aplicar, ejecutar=subprocess.run, inicio=None):
        """`EP-025·HU-011` · El arranque del vigilante al iniciar sesión, y el vigilante que corre."""
        pasos = []
        archivo = os.path.join(inicio or Instalador.carpeta_de_inicio(), Instalador.VIGILANTE + ".cmd")
        if os.path.isfile(archivo):
            pasos.append("quitar el arranque del vigilante del consumo al iniciar sesión")
            if aplicar:
                os.remove(archivo)
        cimiento = os.path.join(self.instalador.estandar, "proyectos", "cimiento")
        python = Instalador.python_de_cimiento(cimiento)
        if python and os.path.isfile(os.path.join(cimiento, "manage.py")):
            if not aplicar:
                return pasos + ["detener el vigilante del consumo si está corriendo"]
            r = ejecutar([python, os.path.join(cimiento, "manage.py"), "vigilar_consumo", "--parar"],
                         capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
            if r.returncode == 0 and "detenido" in (r.stdout or ""):
                pasos.append("detener el vigilante del consumo")
        return pasos

    def quitar_lectura(self, aplicar, ejecutar=subprocess.run, sistema=os.name):
        """La tarea programada de la lectura del consumo, de antes del vigilante."""
        tarea = Instalador.TAREA_DE_CONSUMO
        if sistema != "nt":
            return ["OMITIDO: si se programó con cron, quitar a mano la línea de leer_consumo"]

        def correr(argumentos):
            return ejecutar(argumentos, capture_output=True, text=True, encoding="utf-8",
                            errors="replace", timeout=60)

        if correr(["schtasks", "/Query", "/TN", tarea]).returncode != 0:
            return []
        if not aplicar:
            return [f"quitar la tarea programada «{tarea}»"]
        r = correr(["schtasks", "/Delete", "/TN", tarea, "/F"])
        if r.returncode == 0:
            return [f"quitar la tarea programada «{tarea}»"]
        lineas = (r.stderr or r.stdout or "").strip().splitlines()
        return ["OMITIDO: no se pudo quitar la tarea programada: " + (lineas[-1] if lineas else "schtasks falló")]

    def quitar_telemetria(self, aplicar, configuracion=None):
        """Las variables de la telemetría, si quedaron: lo mismo que hace la instalación desde la HU-012."""
        return self.instalador.retirar_telemetria(aplicar, configuracion)

    # ── todo junto ───────────────────────────────────────────────────────

    def desinstalar(self, ruta, aplicar):
        """Lo que quita, en orden. Lo propio del proyecto no se toca."""
        ruta = os.path.abspath(ruta)
        if not os.path.isdir(ruta):
            return ["BLOQUEADO: la carpeta no existe — revisá la ruta"]
        pasos = []
        for repo in Instalador.repositorios_git(ruta):
            pasos += self.quitar_git(repo, aplicar)
        pasos += self.quitar_claude(ruta, aplicar)
        if self.instalador.es_el_estandar(ruta):
            pasos += self.quitar_vigilante(aplicar) + self.quitar_lectura(aplicar) + self.quitar_telemetria(aplicar)
        else:
            pasos += (self.quitar_copias(ruta, aplicar) + self.quitar_ci(ruta, aplicar)
                      + self.quitar_registro(ruta, aplicar) + self.quitar_estructura(ruta, aplicar))
        return pasos or ["no había nada de la instalación que quitar"]
