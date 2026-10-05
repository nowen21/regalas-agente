"""El stack de instalación del agente: qué le falta a un proyecto.

Mientras falte un componente, la instalación está **incompleta** y el agente lo
dice: es la diferencia entre "el estándar está instalado" como promesa y como
hecho comprobable.

**La lista no vive aquí.** Vive en `plantillas/stack-instalacion.md` (id, qué es
y cómo se instala) y se lee de ahí; acá solo está, para cada `id`, la
comprobación que dice sí o no. Así no hay dos listas que terminen diciendo
cosas distintas.

Tres cosas se reportan por separado porque se arreglan distinto: falta un
componente (instalarlo), el stack cambió (reinstalar) y el estándar subió de
versión (decisión del usuario).

No devuelve hallazgos sino un `Punto` por componente, y por eso no es un
`Validador`: el subcomando `checklist` de `validar.py` imprime los puntos.
"""
import json
import os
import re
from datetime import datetime

from ..comun import FALLA, Proyecto
from ..enganches.recuerdos import CARPETA as CARPETA_RECUERDOS
from ..enganches.recuerdos import Recuerdos
from ..enganches.sesion import ArranqueDeSesion
from ..herramientas.instalar import CONFIG_AGENTE, HOOKS_CLAUDE, IGNORADOS, Instalador
from .version import VersionDelEstandar
from .versiones import POR_ID, DocumentosHeredados, RegistroDeVersiones, Sello

PLANTILLA = "plantillas/stack-instalacion.md"
COPIA = os.path.join(".agente", "stack-instalacion.md")
MARCA = os.path.join(".agente", "INSTALACION-INCOMPLETA.md")

# Fila de la tabla de componentes: | `id` | Componente | Cómo se instala |
_FILA = re.compile(r"^\|\s*`([a-z0-9-]+)`\s*\|([^|]+)\|([^|]+)\|")

# El sello lo define `versiones`, el dueño del tema: una sola forma de sellar
# para todos los documentos heredados (`M2`).
_STACK = POR_ID["stack-instalacion"]


def _leer(ruta):
    try:
        with open(ruta, encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError:
        with open(ruta, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


class Punto:
    """Un componente del stack y cómo quedó al comprobarlo."""

    def __init__(self, id, componente, arreglo, cumple, detalle=""):
        self.id = id
        self.componente = componente
        self.arreglo = arreglo
        self.cumple = cumple
        self.detalle = detalle

    def __str__(self):
        marca = "ok" if self.cumple else "FALTA"
        return f"[{marca}] {self.id} — {self.detalle or self.componente}"


class Checklist:
    """Comprueba el stack de instalación de un proyecto contra un estándar."""

    # `id` de la plantilla: método que lo comprueba.
    COMPROBACIONES = {
        "f13": "_f13",
        "claude-md": "_claude_md",
        "gitignore": "_gitignore",
        "agente-config": "_agente_config",
        "stack-instalacion": "_stack_instalacion",
        "documentacion": "_documentacion",
        "historico": "_historico",
        "recuerdos": "_recuerdos",
        "enganches-git": "_enganches_git",
        "enganches-claude": "_enganches_claude",
        "registro": "_registro",
        "version": "_version",
        "versiones": "_versiones",
        "cadena": "_cadena",
    }

    def __init__(self, proyecto, estandar=None):
        self.proyecto = os.path.abspath(proyecto)
        self.estandar = os.path.abspath(estandar or Proyecto.estandar())

    # ── la lista y su sello ──────────────────────────────────────────────

    @staticmethod
    def ruta_plantilla(estandar=None):
        return os.path.join(estandar or Proyecto.estandar(), *PLANTILLA.split("/"))

    @classmethod
    def componentes(cls, estandar=None):
        """La lista, leída de la plantilla: `[(id, componente, cómo se instala)]`."""
        archivo = cls.ruta_plantilla(estandar)
        if not os.path.isfile(archivo):
            return []
        salida = []
        for linea in _leer(archivo).splitlines():
            m = _FILA.match(linea.strip())
            if m:
                salida.append((m.group(1), m.group(2).strip(), m.group(3).strip()))
        return salida

    @staticmethod
    def huella(estandar=None):
        """Huella del stack central. Cambia cuando cambia la lista."""
        return Sello.huella_central(_STACK, estandar)

    @staticmethod
    def huella_instalada(proyecto):
        """La huella que quedó sellada en la copia del proyecto, o ""."""
        return Sello.huella_sellada(proyecto, _STACK)

    @classmethod
    def sello(cls, estandar=None):
        """La línea que se le agrega a la copia para poder comparar después."""
        return "\n" + Sello.texto(cls.huella(estandar), VersionDelEstandar.vigente(estandar)) + "\n"

    # ── las comprobaciones, una por `id` de la plantilla ─────────────────

    def _f13(self):
        return (Instalador.cumple_f13(self.proyecto),
                "falta la carpeta `proyectos/` — el proyecto no está instalado")

    def _claude_md(self):
        """Existe, está lleno **y** está sincronizado con la plantilla central.

        Lo tercero se escapaba: las secciones faltantes y la diferencia de fechas
        salen como AVISO (acá solo cuentan las FALLA), y un cambio *dentro* de
        una sección no lo veía nadie. El sello compara la huella de la plantilla
        contra la que este `CLAUDE.md` declara haber seguido.
        """
        arranque = ArranqueDeSesion(self.proyecto, estandar=self.estandar)
        fallas = [h for h in arranque.revisar_claude_md() if h.severidad == FALLA]
        if fallas:
            return False, fallas[0].mensaje
        est = DocumentosHeredados(self.proyecto, self.estandar).estado_de("claude-md")
        if est and not est.al_dia:
            return False, est.mensaje()
        return True, ""

    def _gitignore(self):
        archivo = os.path.join(self.proyecto, ".gitignore")
        if not os.path.isfile(archivo):
            return False, "no hay .gitignore"
        lineas = {l.strip() for l in _leer(archivo).splitlines()}
        faltan = [x for x in IGNORADOS if x not in lineas]
        return not faltan, f"al .gitignore le faltan: {', '.join(faltan)}"

    def _agente_config(self):
        carpeta = os.path.join(self.proyecto, ".agente")
        faltan = [n for n in CONFIG_AGENTE if not os.path.isfile(os.path.join(carpeta, n))]
        return not faltan, f"faltan en .agente/: {', '.join(faltan)}"

    def _stack_instalacion(self):
        instalada = self.huella_instalada(self.proyecto)
        if not instalada:
            return False, "el proyecto no tiene copia del stack de instalación"
        actual = self.huella(self.estandar)
        if instalada != actual:
            return False, ("el stack de instalación cambió en el estándar "
                           f"({instalada} → {actual}): hay componentes nuevos")
        return True, ""

    def _documentacion(self):
        return (os.path.isdir(os.path.join(self.proyecto, "documentacion")),
                "falta la carpeta `documentacion/`")

    def _historico(self):
        if not os.path.isfile(os.path.join(self.proyecto, "historico-chat", "README.md")):
            return False, "falta `historico-chat/` con su README"
        est = DocumentosHeredados(self.proyecto, self.estandar).estado_de("historico")
        if est and not est.al_dia:
            return False, est.mensaje()
        return True, ""

    def _recuerdos(self):
        """La memoria del agente: existe en el repositorio y **solo** ahí
        (`01·C19`). Tener la carpeta y dejar los recuerdos en el almacén de la
        herramienta es no tener memoria."""
        memoria = Recuerdos(self.proyecto)
        if not memoria.indice_presente():
            return False, f"falta `{CARPETA_RECUERDOS.replace(os.sep, '/')}/` con su índice"
        est = DocumentosHeredados(self.proyecto, self.estandar).estado_de("recuerdos")
        if est and not est.al_dia:
            return False, est.mensaje()
        return memoria.revisar()

    def _versiones(self):
        return RegistroDeVersiones(self.proyecto, self.estandar).revisar()

    def _enganches_git(self):
        if not Instalador.repositorios_git(self.proyecto):
            return True, ""             # sin repos no hay enganche que poner
        hallazgos = ArranqueDeSesion(self.proyecto, estandar=self.estandar).revisar_enganches(self.proyecto)
        return not hallazgos, (hallazgos[0].mensaje if hallazgos else "")

    def _enganches_claude(self):
        archivo = os.path.join(self.proyecto, ".claude", "settings.json")
        if not os.path.isfile(archivo):
            return False, "no hay .claude/settings.json"
        try:
            datos = json.loads(_leer(archivo))
        except (json.JSONDecodeError, ValueError):
            return False, ".claude/settings.json tiene JSON inválido"

        # Se compara normalizado (pendiente 72): en Windows `c:/x` y `C:/x` son la
        # misma ruta, y como texto la minúscula daba los enganches por faltantes.
        puestos = {(evento, os.path.normcase(h.get("command") or ""))
                   for evento, grupos in (datos.get("hooks") or {}).items()
                   for g in grupos for h in g.get("hooks", [])}

        faltan = []
        for evento, _, guion, mensaje, args in HOOKS_CLAUDE:
            esperado = Instalador.hook_claude(
                self.estandar.replace("\\", "/"), self.proyecto.replace("\\", "/"),
                guion, mensaje, args)["command"]
            if (evento, os.path.normcase(esperado)) not in puestos:
                faltan.append(f"{evento}/{guion}")
        return not faltan, f"enganches de Claude Code sin poner o vencidos: {', '.join(faltan)}"

    def _registro(self):
        esperado = os.path.normcase(self.proyecto)
        for _, ruta in Instalador(self.estandar).proyectos_registrados():
            if os.path.normcase(os.path.abspath(ruta)) == esperado:
                return True, ""
        return False, "el proyecto no está en plantillas/proyectos.md del estándar"

    def _version(self):
        """Que el proyecto **declare** qué versión sigue; el número no reprueba.

        Un PARCHE que no le pide nada lo dejaba en rojo, y el ruido enseña a
        ignorar la alerta. Lo que tiene que aplicar lo dicen los sellos; acá solo
        se exige la declaración, sin la cual no hay con qué sellar las fases.
        """
        claude = os.path.join(self.proyecto, "CLAUDE.md")
        if not os.path.isfile(claude):
            return False, "no se encontró CLAUDE.md; no se puede leer la versión adoptada"
        if not VersionDelEstandar.extraer_adoptada(_leer(claude)):
            return False, ("el proyecto no declara qué versión del estándar sigue "
                           "— fijarla en su CLAUDE.md")
        return True, ""

    def _cadena(self):
        """`02·F0`: el proyecto arrancó la cadena.

        **El único punto que el instalador no instala**: un proyecto puede tener
        todo puesto, código commiteado y `prompts/` sin un planteamiento. La
        épica se exige **solo si ya hay código**: pedírsela a un proyecto recién
        instalado es ruido.
        """
        prompts = os.path.join(self.proyecto, "prompts")
        hay_planteamiento = any(
            n.lower().endswith("planteamiento.md")
            for n in (os.listdir(prompts) if os.path.isdir(prompts) else []))
        if not hay_planteamiento:
            return (False, "no hay ningún planteamiento en `prompts/` — la cadena "
                           "de `02·F0` arranca ahí, y lo escribe el agente con lo "
                           "que el usuario quiere, no el instalador")

        codigo = os.path.join(self.proyecto, "proyectos")
        hay_codigo = bool(os.path.isdir(codigo) and os.listdir(codigo))
        epicas = os.path.join(self.proyecto, "documentacion", "epicas")
        hay_epica = any(
            os.path.isdir(os.path.join(epicas, n))
            for n in (os.listdir(epicas) if os.path.isdir(epicas) else []))
        if hay_codigo and not hay_epica:
            return (False, "hay código en `proyectos/` y ninguna épica en "
                           "`documentacion/epicas/` — se construyó saltando la "
                           "cadena (`02·F0`)")
        return True, ""

    # ── la revisión completa ─────────────────────────────────────────────

    def revisar(self):
        """Un `Punto` por componente, en el orden de la plantilla."""
        puntos = []
        for id, componente, arreglo in self.componentes(self.estandar):
            metodo = self.COMPROBACIONES.get(id)
            if metodo is None:
                # Un componente que no se sabe comprobar se dice: suele ser que
                # el estándar de esta máquina quedó viejo.
                puntos.append(Punto(id, componente, arreglo, False,
                                    f"el validador no sabe comprobar «{id}» "
                                    f"— actualizar el estándar"))
                continue
            try:
                cumple, detalle = getattr(self, metodo)()
            except Exception as e:      # noqa: BLE001 (un componente roto no tumba el resto)
                cumple, detalle = False, f"no se pudo comprobar: {e}"
            puntos.append(Punto(id, componente, arreglo, cumple, "" if cumple else detalle))
        return puntos

    @staticmethod
    def pendientes(puntos):
        return [p for p in puntos if not p.cumple]

    @classmethod
    def resumen(cls, proyecto, puntos):
        """Una línea para la pantalla del usuario."""
        nombre = os.path.basename(os.path.abspath(proyecto))
        faltan = cls.pendientes(puntos)
        if not puntos:
            return f"Instalación del agente · {nombre} · no se pudo leer el stack"
        if not faltan:
            return f"Instalación del agente completa · {nombre} · {len(puntos)} de {len(puntos)}"
        ids = ", ".join(p.id for p in faltan[:4])
        if len(faltan) > 4:
            ids += f" y {len(faltan) - 4} más"
        return (f"INSTALACIÓN INCOMPLETA · {nombre} · "
                f"{len(puntos) - len(faltan)} de {len(puntos)} · falta: {ids}")

    @classmethod
    def detalle(cls, puntos):
        """El desglose que lee el agente: qué falta y cómo se arregla."""
        lineas = []
        for p in cls.pendientes(puntos):
            lineas.append(f"- **{p.id}** — {p.detalle or p.componente}")
            lineas.append(f"  Se arregla así: {p.arreglo}")
        return "\n".join(lineas)

    def escribir_marca(self, puntos):
        """Escribe (o borra) `.agente/INSTALACION-INCOMPLETA.md`.

        La ausencia del archivo **es** la señal de instalación completa: una
        marca que hay que borrar a mano termina mintiendo. Devuelve la ruta
        escrita, o "" si no había nada que marcar.
        """
        archivo = os.path.join(self.proyecto, MARCA)
        faltan = self.pendientes(puntos)

        if not faltan:
            if os.path.isfile(archivo):
                os.remove(archivo)
            return ""

        cuerpo = (
            "# Instalación del agente incompleta\n\n"
            f"Comprobado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} · "
            f"faltan {len(faltan)} de {len(puntos)} componentes.\n\n"
            "Mientras exista este archivo, el agente **no está completo** y lo avisa "
            "en cada mensaje. Lo escribe y lo borra el enganche; no se edita a mano.\n\n"
            "## Qué falta\n\n"
            f"{self.detalle(puntos)}\n\n"
            "## Se resuelve con una línea\n\n"
            "```sh\n"
            f'python "{self.estandar.replace(os.sep, "/")}/validadores/instalar.py" '
            f'"{self.proyecto.replace(os.sep, "/")}" --aplicar\n'
            "```\n\n"
            "El instalador pone todo lo de la lista y comprueba el resultado. Si "
            "después de correrlo algo sigue apareciendo aquí, es porque exige una "
            "decisión del usuario: qué código va en `proyectos/`, o subir la "
            "versión adoptada del estándar.\n\n"
            "> La lista completa de componentes está en `.agente/stack-instalacion.md`.\n")

        os.makedirs(os.path.dirname(archivo), exist_ok=True)
        with open(archivo, "w", encoding="utf-8", newline="\n") as f:
            f.write(cuerpo)
        return archivo
