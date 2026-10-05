"""Qué versión del estándar usa un proyecto, y desde cuándo.

Nada de lo que un proyecto hereda del estándar puede quedarse viejo. Tres
piezas resuelven eso, y cada una hace **una** cosa:

  1. **El sello** (`Sello`). Cada documento que el proyecto copió del estándar
     lleva al final la huella de la plantilla de la que salió. Comparar esa
     huella con la actual delata cualquier cambio sin depender de la fecha del
     archivo, que un `clone` reinicia.
  2. **La comprobación** (`DocumentosHeredados`). El componente cuya huella no
     coincide reprueba: estar viejo es instalación incompleta, no un aviso.
  3. **El registro** (`RegistroDeVersiones`). Cada actualización deja un `.md`
     en `documentacion/versiones/` con desde cuándo el proyecto usa esa versión
     y qué cambió de huella.

**No hay archivo de estado.** El estado se lee de los sellos y la historia de
los registros: dos sitios que declaren lo mismo terminan diciendo cosas
distintas.

El sello de un documento **no** es su huella: es la de la plantilla contra la
que se sincronizó. El `CLAUDE.md` lo llena cada proyecto, así que su contenido
siempre difiere del original, y aun así hay que poder decir si quedó viejo.
"""
import hashlib
import os
import re
from datetime import datetime

from ..comun import Proyecto

# Va en `documentacion/` y no en `.agente/`: `.agente/` se ignora en git, y
# saber con qué versión de las reglas se cerró cada fase es conocimiento del
# proyecto, no ajuste de una máquina.
CARPETA = os.path.join("documentacion", "versiones")

# El sello, tal como quedó escrito desde la primera versión. No cambia de forma:
# cambiarla dejaría "desactualizado" a todo proyecto instalado por un detalle de
# sintaxis. La versión es opcional al leer, aunque al escribir siempre va.
_SELLO = re.compile(
    r"^<!--\s*huella:\s*([0-9a-f]+)\s*(?:·\s*estandar\s*(\S+?)\s*)?-->\s*$",
    re.MULTILINE)

# Nombre de un registro: 2026-08-07-1.4.0.md, con sufijo si hay dos el mismo día.
_REGISTRO = re.compile(r"^(\d{4}-\d{2}-\d{2})-(.+?)(?:-(\d+))?\.md$")

AL_DIA = "al-dia"
VIEJO = "viejo"
SIN_SELLO = "sin-sello"
FALTA = "falta"


def _leer(ruta):
    try:
        with open(ruta, encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError:
        with open(ruta, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def _estandar(estandar=None):
    return estandar or Proyecto.estandar()


class Componente:
    """Un documento que el proyecto hereda del estándar y que puede quedar viejo.

    `plantilla` es la fuente en el estándar; `destino`, dónde vive la copia.
    `se_pisa` distingue la copia literal, que el instalador reescribe, de la que
    llena el proyecto, donde solo se refresca el sello.
    """

    def __init__(self, id, descripcion, plantilla, destino, se_pisa):
        self.id = id
        self.descripcion = descripcion
        self.plantilla = plantilla
        self.destino = destino
        self.se_pisa = se_pisa

    def ruta_plantilla(self, estandar=None):
        return os.path.join(_estandar(estandar), *self.plantilla.split("/"))

    def ruta_destino(self, proyecto):
        return os.path.join(proyecto, *self.destino.split("/"))


COMPONENTES = [
    Componente(
        "claude-md",
        "El `CLAUDE.md` del proyecto, sincronizado con la plantilla central",
        "plantillas/CLAUDE.md.plantilla", "CLAUDE.md", se_pisa=False),
    Componente(
        "stack-instalacion",
        "La lista de lo que el proyecto debe tener",
        "plantillas/stack-instalacion.md", ".agente/stack-instalacion.md",
        se_pisa=True),
    Componente(
        "historico",
        "El `README.md` de `historico-chat/`",
        "plantillas/historico-chat.md", "historico-chat/README.md",
        se_pisa=False),
    Componente(
        "recuerdos",
        "El índice de `historico-chat/memory/`, la memoria del agente",
        "plantillas/memoria.md", "historico-chat/memory/memory.md",
        se_pisa=False),
]

POR_ID = {c.id: c for c in COMPONENTES}


class Sello:
    """La marca `<!-- huella: … · estandar X.Y.Z -->` de un documento heredado."""

    @staticmethod
    def huella_texto(texto):
        """La huella de un contenido. Corta a propósito: se lee a simple vista."""
        return hashlib.sha256(texto.encode("utf-8")).hexdigest()[:12]

    @classmethod
    def huella_central(cls, componente, estandar=None):
        """Huella de la plantilla en el estándar, o "" si la plantilla no está."""
        archivo = componente.ruta_plantilla(estandar)
        if not os.path.isfile(archivo):
            return ""
        return cls.huella_texto(_leer(archivo))

    @staticmethod
    def leer(archivo):
        """El sello de un archivo: (huella, versión del estándar). ("", "") si no hay."""
        if not os.path.isfile(archivo):
            return "", ""
        m = None
        for m in _SELLO.finditer(_leer(archivo)):
            pass                        # el último sello es el vigente
        return (m.group(1), m.group(2) or "") if m else ("", "")

    @classmethod
    def huella_sellada(cls, proyecto, componente):
        return cls.leer(componente.ruta_destino(proyecto))[0]

    @staticmethod
    def texto(huella, version_estandar):
        return f"<!-- huella: {huella} · estandar {version_estandar or '?'} -->"

    @staticmethod
    def quitar(texto):
        """`texto` sin su sello, para poder agregarle contenido al final.

        El sello va último: si se le anexa una sección después, la marca queda
        en medio. Se quita, se escribe, y `poner` lo vuelve a dejar al final.
        """
        return _SELLO.sub("", texto).rstrip("\n") + "\n"

    @classmethod
    def poner(cls, texto, huella, version_estandar):
        """`texto` con su sello al día: reemplazado en su sitio o agregado al final.
        Nunca quedan dos: con dos sellos no se sabe cuál declara."""
        nuevo = cls.texto(huella, version_estandar)
        if _SELLO.search(texto):
            return _SELLO.sub(lambda _: nuevo, texto)
        if texto and not texto.endswith("\n"):
            texto += "\n"
        return f"{texto}\n{nuevo}\n"


class Estado:
    """Cómo quedó un componente al compararlo con el estándar."""

    def __init__(self, componente, situacion, sellada, actual):
        self.componente = componente
        self.situacion = situacion
        self.sellada = sellada
        self.actual = actual

    @property
    def id(self):
        return self.componente.id

    @property
    def al_dia(self):
        return self.situacion == AL_DIA

    def mensaje(self):
        if self.situacion == FALTA:
            return f"falta `{self.componente.destino}`"
        if self.situacion == SIN_SELLO:
            return (f"`{self.componente.destino}` no declara contra qué versión "
                    f"se sincronizó — reinstalar para sellarlo")
        if self.situacion == VIEJO:
            return (f"`{self.componente.destino}` quedó viejo: la plantilla "
                    f"cambió en el estándar ({self.sellada} → {self.actual})")
        return ""


class DocumentosHeredados:
    """Lo que un proyecto heredó del estándar, comparado contra sus plantillas."""

    def __init__(self, proyecto, estandar=None):
        self.proyecto = os.path.abspath(proyecto)
        self.estandar = estandar

    def estado(self):
        """Un `Estado` por componente heredado, en el orden de `COMPONENTES`."""
        salida = []
        for c in COMPONENTES:
            actual = Sello.huella_central(c, self.estandar)
            destino = c.ruta_destino(self.proyecto)
            if not os.path.isfile(destino):
                salida.append(Estado(c, FALTA, "", actual))
                continue
            sellada = Sello.huella_sellada(self.proyecto, c)
            if not sellada:
                salida.append(Estado(c, SIN_SELLO, "", actual))
            elif sellada != actual:
                salida.append(Estado(c, VIEJO, sellada, actual))
            else:
                salida.append(Estado(c, AL_DIA, sellada, actual))
        return salida

    def viejos(self):
        """Los componentes que no están al día. Vacío = nada viejo."""
        return [e for e in self.estado() if not e.al_dia]

    def estado_de(self, id):
        """El estado de un solo componente, por su `id`."""
        return next((e for e in self.estado() if e.id == id), None)


_CABECERA_INDICE = """# Versiones del estándar en este proyecto

Un archivo por actualización. Cada uno dice **desde cuándo** este proyecto usa
esa versión del estándar, qué componentes se actualizaron y qué cambió.

Los escribe `validadores/instalar.py`; no se editan a mano. Sirven para saber con
qué reglas se trabajó en cada momento: un cambio de norma no reabre lo que ya se
cerró bajo la anterior, y para saber bajo cuál cerró hay que poder mirarlo.

**Se versiona.** Va en `documentacion/` y no en `.agente/` justamente por eso:
`.agente/` está en el `.gitignore` y se queda en una sola máquina.

| Fecha | Versión | Registro |
|---|---|---|
"""


class RegistroDeVersiones:
    """La carpeta `documentacion/versiones/` de un proyecto: un archivo por
    actualización, más su índice."""

    def __init__(self, proyecto, estandar=None):
        self.proyecto = os.path.abspath(proyecto)
        self.estandar = estandar

    @property
    def carpeta(self):
        return os.path.join(self.proyecto, *CARPETA.split(os.sep))

    @staticmethod
    def orden_de_version(v):
        """La versión como números, para poder compararla.

        **Comparar el texto pone la `23.10.0` antes que la `23.5.0`.** Lo que no
        es número queda como texto al final, sin reventar.
        """
        partes = []
        for trozo in str(v).split("."):
            partes.append((0, int(trozo), "") if trozo.isdigit() else (1, 0, trozo))
        return partes

    def registros(self):
        """`[(nombre_archivo, fecha, version)]`, del más viejo al más nuevo.

        El orden sale de la fecha, después de la **versión** y por último del
        sufijo. Sin la versión en el criterio, dos registros del mismo día
        empataban y el desempate alfabético ponía la `23.10.0` antes que la
        `23.5.0`: el instalador escribía un registro vacío por corrida.
        """
        if not os.path.isdir(self.carpeta):
            return []
        salida = []
        for nombre in os.listdir(self.carpeta):
            m = _REGISTRO.match(nombre)
            if m:
                salida.append((nombre, m.group(1), m.group(2), int(m.group(3) or 1)))
        salida.sort(key=lambda r: (r[1], self.orden_de_version(r[2]), r[3]))
        return [(n, f, v) for n, f, v, _ in salida]

    def version_registrada(self):
        """La versión del último registro, o "" si el proyecto no tiene ninguno."""
        hechos = self.registros()
        return hechos[-1][2] if hechos else ""

    def version_sellada(self):
        """La versión que declaran los sellos ya puestos, o ""."""
        for c in COMPONENTES:
            _, ver = Sello.leer(c.ruta_destino(self.proyecto))
            if ver and ver != "?":
                return ver
        return ""

    @staticmethod
    def _nombre_libre(carpeta, fecha, version):
        base = f"{fecha}-{version}"
        if not os.path.exists(os.path.join(carpeta, f"{base}.md")):
            return f"{base}.md"
        n = 2
        while os.path.exists(os.path.join(carpeta, f"{base}-{n}.md")):
            n += 1
        return f"{base}-{n}.md"

    def nombre_previsto(self, version_nueva):
        """El nombre que va a tener el próximo registro, sin escribir nada.

        Lo usa la simulación del instalador: anunciar la actualización sin decir
        en qué archivo dejaba fuera justo el documento que deja constancia
        (`EP-007·HU-002`).
        """
        fecha = datetime.now().strftime("%Y-%m-%d")
        return self._nombre_libre(self.carpeta, fecha, version_nueva)

    def escribir_indice(self):
        """Reescribe el `README.md` de la carpeta con la lista de registros."""
        filas = "".join(f"| {fecha} | `{version}` | [{nombre}]({nombre}) |\n"
                        for nombre, fecha, version in self.registros())
        archivo = os.path.join(self.carpeta, "README.md")
        with open(archivo, "w", encoding="utf-8", newline="\n") as f:
            f.write(_CABECERA_INDICE + (filas or "| — | — | (todavía ninguno) |\n"))
        return archivo

    def registrar(self, version_nueva, antes, despues, pasos, pendientes=(), anterior=None):
        """Escribe el registro de una actualización y devuelve su ruta.

        `antes` y `despues` son `{id: huella}`; solo se listan los componentes
        cuya huella cambió. `anterior` se recibe y no se calcula: para cuando
        esto corre, los sellos ya dicen la versión nueva, y una instalación desde
        cero declararía venir de la misma que acaba de instalar.
        """
        os.makedirs(self.carpeta, exist_ok=True)

        ahora = datetime.now()
        fecha = ahora.strftime("%Y-%m-%d")
        momento = ahora.strftime("%Y-%m-%d %H:%M:%S")
        if anterior is None:
            anterior = self.version_registrada()

        cambiados = [(id, antes.get(id, ""), despues.get(id, ""))
                     for id in despues if antes.get(id, "") != despues.get(id, "")]

        lineas = [
            f"# Actualización a {version_nueva} — {fecha}",
            "",
            f"Desde **{momento}** este proyecto usa la versión **{version_nueva}** "
            f"del estándar.",
            "",
            "| | |",
            "|---|---|",
            f"| Versión anterior | {anterior or '(primera instalación)'} |",
            f"| Versión instalada | **{version_nueva}** |",
            f"| Fecha y hora | {momento} |",
            f"| Estándar | `{_estandar(self.estandar).replace(os.sep, '/')}` |",
            "",
            "## Componentes actualizados",
            "",
        ]

        if cambiados:
            lineas += ["| Componente | Qué es | Huella antes | Huella después |",
                       "|---|---|---|---|"]
            for id, viejo, nuevo in cambiados:
                que = POR_ID[id].descripcion if id in POR_ID else id
                lineas.append(f"| `{id}` | {que} | `{viejo or '—'}` | `{nuevo or '—'}` |")
        else:
            lineas.append("Ninguno cambió de huella: solo se refrescó la instalación.")

        lineas += ["", "## Qué se aplicó", ""]
        lineas += [f"- {p}" for p in pasos] or ["- (nada: ya estaba todo al día)"]

        archivo = os.path.join(self.carpeta, self._nombre_libre(self.carpeta, fecha, version_nueva))
        cierre = ["", "---", "",
                  "> Lo escribió `validadores/instalar.py`. No se edita a mano.", ""]

        def escribir(cuerpo):
            with open(archivo, "w", encoding="utf-8", newline="\n") as f:
                f.write("\n".join(cuerpo))

        # Lo pendiente se calcula **después** de que el archivo exista: antes, el
        # registro recién nacido se listaba a sí mismo como faltante. Por eso se
        # escribe dos veces y `pendientes` acepta una función.
        escribir(lineas + cierre)
        self.escribir_indice()

        faltan = pendientes() if callable(pendientes) else pendientes
        if faltan:
            lineas += ["", "## Qué quedó pendiente", "",
                       "Esto no lo aplica el instalador — es decisión del usuario:", ""]
            lineas += [f"- {p}" for p in faltan]
            escribir(lineas + cierre)

        return archivo

    def revisar(self):
        """¿La carpeta refleja lo que hoy está instalado? `(cumple, detalle)`,
        con la forma que espera el checklist."""
        if not os.path.isdir(self.carpeta):
            return False, f"falta `{CARPETA.replace(os.sep, '/')}/` con el registro de versiones"

        ultima = self.version_registrada()
        if not ultima:
            return False, "la carpeta de versiones está vacía: ninguna actualización quedó registrada"

        sellada = self.version_sellada()
        if sellada and sellada != ultima:
            return False, (f"lo instalado dice `{sellada}` y el último registro dice "
                           f"`{ultima}`: falta registrar la actualización")
        return True, ""
