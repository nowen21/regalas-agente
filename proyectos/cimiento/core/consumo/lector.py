# -*- coding: utf-8 -*-
"""`EP-025·HU-006` · Lo que gastó una sesión de Claude Code, leído de su `.jsonl`.

**Leer va aparte de guardar.** Esto solo entiende el formato de Claude Code y
devuelve llamadas, enganches y archivos leídos; `guardar.py` los pone en la
base. Otra herramienta de IA agrega su propio lector. No usa Django: lo usa
también `hook_presupuesto.py`.

**Una llamada ocupa varias líneas**, todas con el mismo `message.id` y el mismo
`usage`. Se cuenta una vez, con su última línea (sesión `c3d82767`, medida el
2026-10-05: 619 líneas, 208 llamadas).

**Los enganches y los archivos no traen tokens.** Claude Code solo cuenta
tokens por llamada. Lo que agrega un enganche y lo que ocupa un archivo leído
se miden en caracteres y se estiman en tokens con `CARACTERES_POR_TOKEN`: es
una estimación, y así se muestra.

**Desde un byte.** La lectura empieza donde quedó la anterior. La última línea
sin salto puede estar a medio escribir: no se cuenta como leída.

**No se guarda texto**: solo tamaños, nombres y rutas.
"""
import json
import re
from dataclasses import dataclass, field
from datetime import datetime

# Estimación: el español con Markdown da entre 3 y 4 caracteres por token.
CARACTERES_POR_TOKEN = 3.5

_LLEGA_AL_MODELO = ("hook_additional_context", "hook_blocking_error")
# En estos dos momentos, lo que un enganche escribe como texto plano también
# llega al modelo; en los demás (`Stop`, `PostToolUse`) solo queda anotado.
_TEXTO_PLANO_LLEGA = ("UserPromptSubmit", "SessionStart")
_TITULO = re.compile(r"^\[([^\]\n]{3,120})\]")


def estimar_tokens(caracteres):
    return round(caracteres / CARACTERES_POR_TOKEN)


def _fecha(texto):
    try:
        return datetime.fromisoformat((texto or "").replace("Z", "+00:00"))
    except ValueError:
        return None


@dataclass
class Llamada:
    sesion: str
    mensaje: str
    fecha: datetime
    modelo: str
    entrada: int
    cache_creada: int
    cache_leida: int
    salida: int
    auxiliar: bool = False
    # `requestId` del `.jsonl`: une la llamada con lo que guardó la telemetría hasta la HU-012.
    solicitud: str = ""
    # `EP-025·HU-010` · El `promptId` del mensaje del usuario que la originó.
    pedido: str = ""

    def como_consumo(self):
        """El consumo como lo suma `presupuesto.py`: la caché creada cuenta como entrada."""
        return {"entrada": self.entrada + self.cache_creada, "salida": self.salida, "cache": self.cache_leida}


@dataclass
class Enganche:
    sesion: str
    identificador: str
    fecha: datetime
    nombre: str
    evento: str
    caracteres: int


@dataclass
class ArchivoLeido:
    sesion: str
    identificador: str
    fecha: datetime
    ruta: str
    caracteres: int


@dataclass
class Herramienta:
    """`EP-025·HU-010` · Un uso de una herramienta y el tamaño de su resultado."""
    sesion: str
    identificador: str
    fecha: datetime
    nombre: str
    caracteres: int
    # `EP-025·HU-015` · De un comando, solo el programa y su orden: nunca el comando.
    orden: str = ""


@dataclass
class Ejecucion:
    """`EP-025·HU-015` · Una corrida de un enganche, le entregue o no algo al modelo."""
    sesion: str
    identificador: str
    fecha: datetime
    nombre: str
    evento: str


@dataclass
class Pedido:
    """`EP-025·HU-010` · Un mensaje del usuario. Su `texto` solo vive en memoria:
    de ahí sale la palabra clave, y no se guarda."""
    sesion: str
    identificador: str
    fecha: datetime
    texto: str = ""


@dataclass
class Lectura:
    llamadas: list = field(default_factory=list)
    enganches: list = field(default_factory=list)
    archivos: list = field(default_factory=list)
    herramientas: list = field(default_factory=list)
    pedidos: list = field(default_factory=list)
    ejecuciones: list = field(default_factory=list)
    # `{pedido: [ruta]}` de lo que leyó o escribió cada turno, también del que
    # empezó en una lectura anterior. De ahí sale el trabajo; no se guarda.
    rutas: dict = field(default_factory=dict)
    ultimo_pedido: str = ""
    hasta: int = 0
    # `EP-025·HU-025` · `[(posición, texto)]` de las líneas leídas, sin tocar.
    crudas: list = field(default_factory=list)


def _texto(valor):
    if isinstance(valor, str):
        return valor
    if isinstance(valor, list):
        return "\n".join(_texto(v.get("text", "") if isinstance(v, dict) else v) for v in valor)
    if isinstance(valor, dict):
        return _texto(valor.get("text") or valor.get("blockingError") or valor.get("content") or "")
    return ""


def _titulo(texto):
    """`[LAS REGLAS DE CADA TURNO]` al comienzo del texto: así se presentan los enganches."""
    encontrado = _TITULO.match((texto or "").lstrip())
    return encontrado.group(1).strip() if encontrado else ""


_PROGRAMA = re.compile(r"^(?:.*[\/])?([\w.+-]+?)(?:\.exe)?$", re.I)
_CONSOLA = ("Bash", "PowerShell")
_ORDEN = re.compile(r"^[\w.-]{1,40}(?:/[\w.-]{1,40})?$")


def orden_de(comando):
    """`EP-025·HU-015` · El programa y su orden: `git status`, `python manage.py`,
    `python -m unittest`. Nunca el comando completo (`12`).

    Se salta lo que va antes de la primera parte que hace algo (`cd`, variables)
    y las rutas largas: una ruta con carpetas no es una orden.
    """
    for parte in re.split(r"&&|\|\||;|\n|\|", comando or ""):
        palabras = parte.strip().split()
        while palabras and re.match(r"^\w+=", palabras[0]):
            palabras = palabras[1:]
        if not palabras or palabras[0] in ("cd", "export", "set"):
            continue
        programa = _PROGRAMA.match(palabras[0].strip("\"'"))
        nombre = (programa.group(1) if programa else palabras[0]).lower()
        if nombre.startswith("python"):
            nombre = "python"
        resto = palabras[1:]
        if resto[:1] == ["-m"] and len(resto) > 1:
            return "%s -m %s" % (nombre, resto[1].strip("\"'"))[:120]
        siguiente = next((p for p in resto if not p.startswith("-")), "")
        if siguiente[:1] in ("\"", "'"):
            siguiente = ""          # entre comillas es texto, no una orden
        # Una palabra, o un archivo con a lo sumo una carpeta: lo demás puede
        # ser texto o datos, y no se guarda.
        if _ORDEN.match(siguiente):
            return ("%s %s" % (nombre, siguiente.rsplit("/", 1)[-1]))[:120]
        return nombre[:120]
    return ""


def _contexto_del_stdout(stdout):
    """El `additionalContext` que trae el JSON de un enganche, o ""."""
    try:
        datos = json.loads(stdout or "")
    except (json.JSONDecodeError, ValueError, TypeError):
        return ""
    return _texto(((datos or {}).get("hookSpecificOutput") or {}).get("additionalContext") or "") \
        if isinstance(datos, dict) else ""


class LectorDeClaudeCode:
    """Un `.jsonl` de una sesión de Claude Code, desde el byte `desde`."""

    def __init__(self, ruta, desde=0):
        self.ruta = ruta
        self.desde = desde
        # `EP-025·HU-025` · `[(posición en bytes, texto)]` de cada línea completa,
        # tal como está en el archivo: es lo que se guarda en la base.
        self.crudas = []

    def lineas(self):
        """`(lineas_completas, hasta)`: la última sin salto queda fuera."""
        try:
            with open(self.ruta, "rb") as archivo:
                archivo.seek(self.desde)
                crudo = archivo.read()
        except OSError:
            return [], self.desde
        corte = crudo.rfind(b"\n")
        if corte < 0:
            return [], self.desde
        completas = crudo[:corte + 1]
        self.crudas, posicion = [], self.desde
        for linea in completas.split(b"\n")[:-1]:
            texto = linea.rstrip(b"\r").decode("utf-8", "replace")
            if texto.strip():
                self.crudas.append((posicion, texto))
            posicion += len(linea) + 1
        return completas.decode("utf-8", "replace").splitlines(), self.desde + len(completas)

    def leer(self, pedido=""):
        """Lo nuevo desde `desde`. `pedido`: el mensaje en curso donde quedó la
        lectura anterior, para unirle las llamadas que faltan de su turno."""
        lineas, hasta = self.lineas()
        lectura = self.leer_lineas(lineas, pedido)
        lectura.hasta = hasta
        lectura.crudas = self.crudas
        return lectura

    @staticmethod
    def es_pedido(dato):
        """¿La línea es un mensaje del usuario? No lo son el resultado de una
        herramienta ni el resumen que deja la compactación."""
        if dato.get("type") != "user" or dato.get("isMeta") or dato.get("isCompactSummary") \
                or dato.get("isSidechain"):
            return False
        contenido = (dato.get("message") or {}).get("content")
        if isinstance(contenido, str):
            return True
        return isinstance(contenido, list) and any(
            isinstance(b, dict) and b.get("type") == "text" for b in contenido) and not any(
            isinstance(b, dict) and b.get("type") == "tool_result" for b in contenido)

    def turno_anterior(self):
        """`EP-025·HU-009` · Lo que gastó el turno que acaba de terminar.

        Va del penúltimo mensaje del usuario al último. Si después del último no
        hay respuesta del agente, ese es el que se está mandando y el turno
        terminado es el de antes; si la hay, el último todavía no está escrito
        y el turno va de él al final.
        """
        lineas, _ = self.lineas()
        pedidos, ultima_respuesta = [], -1
        for numero, linea in enumerate(lineas):
            try:
                dato = json.loads(linea)
            except (json.JSONDecodeError, ValueError):
                continue
            if not isinstance(dato, dict):
                continue
            if self.es_pedido(dato):
                pedidos.append(numero)
            elif dato.get("type") == "assistant":
                ultima_respuesta = numero
        fin = len(lineas)
        if pedidos and ultima_respuesta < pedidos[-1]:
            fin = pedidos.pop()
        if not pedidos:
            return Lectura()
        return self.leer_lineas(lineas[pedidos[-1]:fin])

    def leer_lineas(self, lineas, pedido=""):
        lectura = Lectura(ultimo_pedido=pedido)
        llamadas, lecturas_pedidas, usos, exitos = {}, {}, {}, {}
        contextos = []
        for linea in lineas:
            try:
                dato = json.loads(linea)
            except (json.JSONDecodeError, ValueError):
                continue
            if not isinstance(dato, dict):
                continue
            tipo, sesion, fecha = dato.get("type"), dato.get("sessionId") or "", _fecha(dato.get("timestamp"))
            if self.es_pedido(dato):
                identificador = dato.get("promptId") or dato.get("uuid") or ""
                lectura.pedidos.append(Pedido(sesion=sesion, identificador=identificador, fecha=fecha,
                                              texto=_texto((dato.get("message") or {}).get("content"))))
                lectura.ultimo_pedido = identificador
            elif tipo == "assistant":
                self._llamada(dato, sesion, fecha, llamadas, lecturas_pedidas, usos, lectura)
            elif tipo == "user":
                self._resultado(dato, sesion, fecha, lecturas_pedidas, lectura.archivos, usos, lectura.herramientas)
            elif tipo == "attachment":
                adjunto = dato.get("attachment") or {}
                if adjunto.get("type") in ("hook_success", "hook_blocking_error"):
                    # `EP-025·HU-015` · Cada corrida, entregue o no algo al modelo.
                    bloqueo = adjunto.get("blockingError")
                    nombre = adjunto.get("command") or (bloqueo.get("command") if isinstance(bloqueo, dict) else "")
                    lectura.ejecuciones.append(Ejecucion(
                        sesion=sesion, identificador=dato.get("uuid") or "", fecha=fecha,
                        nombre=(nombre or adjunto.get("hookName") or "")[:200], evento=adjunto.get("hookEvent") or ""))
                if adjunto.get("type") == "hook_success":
                    clave = (adjunto.get("toolUseID"), adjunto.get("hookName"))
                    exitos.setdefault(clave, []).append(adjunto)
                    if self._texto_plano_al_modelo(adjunto):
                        contextos.append((dato, sesion, fecha, adjunto))
                elif adjunto.get("type") in _LLEGA_AL_MODELO:
                    contextos.append((dato, sesion, fecha, adjunto))
        lectura.llamadas = list(llamadas.values())
        lectura.enganches = [self._enganche(d, s, f, a, exitos) for d, s, f, a in contextos]
        return lectura

    @staticmethod
    def _llamada(dato, sesion, fecha, llamadas, lecturas_pedidas, usos, lectura):
        mensaje = dato.get("message") or {}
        for bloque in mensaje.get("content") or []:
            if not (isinstance(bloque, dict) and bloque.get("type") == "tool_use"):
                continue
            entrada = bloque.get("input") if isinstance(bloque.get("input"), dict) else {}
            ruta = entrada.get("file_path") or entrada.get("notebook_path") or ""
            nombre = bloque.get("name") or ""
            usos[bloque.get("id")] = (nombre, orden_de(entrada.get("command")) if nombre in _CONSOLA else "")
            if ruta and lectura.ultimo_pedido and not dato.get("isSidechain"):
                lectura.rutas.setdefault(lectura.ultimo_pedido, []).append(ruta)
            if bloque.get("name") == "Read":
                lecturas_pedidas[bloque.get("id")] = ruta
        uso = mensaje.get("usage")
        if not isinstance(uso, dict) or not mensaje.get("id"):
            return
        llamadas[mensaje["id"]] = Llamada(
            sesion=sesion, mensaje=mensaje["id"], fecha=fecha, modelo=mensaje.get("model") or "",
            entrada=uso.get("input_tokens") or 0, cache_creada=uso.get("cache_creation_input_tokens") or 0,
            cache_leida=uso.get("cache_read_input_tokens") or 0, salida=uso.get("output_tokens") or 0,
            auxiliar=bool(dato.get("isSidechain")), solicitud=dato.get("requestId") or "",
            pedido="" if dato.get("isSidechain") else lectura.ultimo_pedido)

    @staticmethod
    def _resultado(dato, sesion, fecha, lecturas_pedidas, archivos, usos, herramientas):
        contenido = (dato.get("message") or {}).get("content")
        if not isinstance(contenido, list):
            return
        for bloque in contenido:
            if not (isinstance(bloque, dict) and bloque.get("type") == "tool_result"):
                continue
            identificador = bloque.get("tool_use_id")
            caracteres = len(_texto(bloque.get("content")))
            if identificador in usos:
                nombre, orden = usos.pop(identificador)
                herramientas.append(Herramienta(sesion=sesion, identificador=identificador, fecha=fecha,
                                                nombre=nombre, caracteres=caracteres, orden=orden))
            if identificador in lecturas_pedidas:
                archivos.append(ArchivoLeido(sesion=sesion, identificador=identificador, fecha=fecha,
                                             ruta=lecturas_pedidas.pop(identificador), caracteres=caracteres))

    @staticmethod
    def _texto_plano_al_modelo(adjunto):
        """¿Es un `hook_success` cuyo texto plano llega al modelo? Si es JSON, lo
        que llega viene aparte, en su `hook_additional_context`."""
        salida = (adjunto.get("stdout") or "").strip()
        if adjunto.get("hookEvent") not in _TEXTO_PLANO_LLEGA or not salida:
            return False
        try:
            json.loads(salida)
        except (json.JSONDecodeError, ValueError):
            return True
        return False

    @staticmethod
    def _enganche(dato, sesion, fecha, adjunto, exitos):
        if adjunto.get("type") == "hook_success":
            return Enganche(sesion=sesion, identificador=dato.get("uuid") or "", fecha=fecha,
                            nombre=adjunto.get("command") or adjunto.get("hookName") or "",
                            evento=adjunto.get("hookEvent") or "", caracteres=len(adjunto.get("stdout") or ""))
        texto = _texto(adjunto.get("content") if adjunto.get("type") == "hook_additional_context"
                       else adjunto.get("blockingError"))
        nombre = ""
        bloqueo = adjunto.get("blockingError")
        if isinstance(bloqueo, dict):
            nombre = bloqueo.get("command") or ""
        # El nombre está en el `hook_success` hermano cuyo JSON trae el mismo texto.
        for exito in exitos.get((adjunto.get("toolUseID"), adjunto.get("hookName")), []):
            if not nombre and texto and _contexto_del_stdout(exito.get("stdout")) == texto:
                nombre = exito.get("command") or ""
        return Enganche(sesion=sesion, identificador=dato.get("uuid") or "", fecha=fecha,
                        nombre=nombre or _titulo(texto) or adjunto.get("hookName") or "",
                        evento=adjunto.get("hookEvent") or "",
                        caracteres=len(texto))
