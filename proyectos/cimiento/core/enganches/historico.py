"""Escribe la transcripción de la sesión en `historico-chat/`.

Esto no comprueba nada: **escribe**. Es la excepción al principio de que los
validadores solo verifican, y por un motivo concreto: la regla dice que toda
sesión queda registrada, y mientras eso dependa de que el agente se acuerde,
no se cumple siempre. Aquí lo hace el programa.

Dos entradas, una por cada momento del diálogo:

  - `anotar_usuario`: la llama el enganche `UserPromptSubmit`, con el mensaje
    tal como lo envió el usuario.
  - `anotar_agente`: la llama el enganche `Stop`, leyendo del transcript de
    Claude Code el texto que el agente acaba de responder.

La hora sale del reloj de la máquina en el instante en que ocurre cada cosa,
que es justo lo que un agente no puede garantizar de memoria.

A qué archivo va cada sesión lo dice la marca `<!-- sesion: <id> -->` de su
primera línea, no el nombre: así el archivo se puede renombrar (para ponerle el
tema real) sin que la sesión pierda el hilo. El archivo nace
`AAAA-MM-DD-sesion.md`; cuando ya hubo una respuesta, `aviso_de_nombre` le
recuerda al agente que le ponga tema, y `renombrar` mueve el archivo y corrige
la línea del índice, que es lo único por lo que la próxima sesión encuentra a
esta.
"""
import json
import os
import re
import sys
import unicodedata
from datetime import datetime

if __name__ == "__main__" and not __package__:
    # Corrido por su ruta, como lo pide `aviso_de_nombre`: se arma el paquete
    # para que las importaciones relativas encuentren a `core`.
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    __package__ = "core.enganches"

from ..comun.consola import preparar_salida  # noqa: E402
from .enmascarar import Enmascarador  # noqa: E402

CARPETA = "historico-chat"
INDICE = "README.md"

# Cuántas sesiones se listan al arrancar. Las viejas siguen en el índice del
# README; lo que se recorta es el bloque que se le inyecta al agente.
LIMITE = 40

# Dónde vive el resumen de una sesión, relativo a la carpeta del histórico, y
# cómo se sube desde él (`resumenes/AAAA-MM-DD/tema.md`) hasta la transcripción.
RESUMENES = "resumenes"
HACIA_HISTORICO = "../../"

# Queda en el archivo cuando ya se pidió el nombre, para no pedirlo otra vez.
MARCA_NOMBRE = "<!-- nombre: preguntado -->"

_NUMERO = re.compile(r"^### (\d+) · ", re.MULTILINE)

# `EP-005·HU-024` · Lo que Claude Code mete por `UserPromptSubmit` sin que lo haya
# escrito el usuario: el fin de algo que corría en segundo plano y el informe de
# un agente auxiliar (análisis 1 del pendiente 124, acuerdo 8). Una sola lista: si
# Claude Code cambia las marcas, se ajustan aquí y el enganche de reglas las toma.
AVISOS_INTERNOS = ("<task-notification>", "<agent-message")


def es_aviso_interno(mensaje):
    """¿El mensaje es un aviso interno de Claude Code y no algo que escribió el usuario?"""
    return (mensaje or "").lstrip().startswith(AVISOS_INTERNOS)

# Una línea del índice, con su resumen de sesión al final si ya lo tiene:
# `- [nombre.md](nombre.md) — de qué se trató. · [resumenes/AAAA-MM-DD/tema.md](…)`
_LINEA = re.compile(
    r"^- \[[^\]]*\]\(([^)#\s]+\.md)\)\s*(?:—\s*(.*?))?"
    r"\s*(?:·\s*\[[^\]]*\]\([^)]+\))?\s*$")

# `EP-011·HU-001` · Dónde empieza cada turno. Quien escribe el formato es quien
# sabe leerlo: copiar estas expresiones en otro lado dejaría dos verdades que
# se separan el día que una marca cambie.
_TURNO = re.compile(
    r"(?m)^(?:### \d+ · (Usuario) — (.+?)\s*$|\*\*(Agente)\*\* — (.+?)\s*$)")

# El comentario que el enganche deja para no repetir el turno del agente.
_SELLO_AGENTE = re.compile(r"(?m)^<!-- agente: [^>]*-->\s*$")

# La fecha con la que empieza el nombre del archivo de una sesión.
_FECHA = re.compile(r"^(\d{4}-\d{2}-\d{2})")

# El nombre que pone el enganche mientras no se sabe el tema: `2026-08-09-sesion.md`.
_GENERICO = re.compile(r"^\d{4}-\d{2}-\d{2}-sesion(?:-\d+)?\.md$", re.IGNORECASE)


def _leer(ruta):
    try:
        with open(ruta, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def _agregar(ruta, texto):
    with open(ruta, "a", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def _sobrescribir(ruta, texto):
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def _ahora():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def _fecha_de(nombre):
    """La fecha del nombre del archivo (`AAAA-MM-DD-tema.md`), o la de hoy."""
    m = _FECHA.match(nombre)
    return m.group(1) if m else datetime.now().strftime("%Y-%m-%d")


class Transcript:
    """Lo que dejó el agente en el transcript de la herramienta (líneas JSON)."""

    @classmethod
    def ultima_respuesta(cls, transcript):
        """`(texto que el agente respondió en el último turno, su identificador)`.

        Se recorre de atrás hacia adelante juntando los bloques de texto del
        agente hasta topar con un mensaje **real** del usuario: los resultados
        de herramientas también viajan como mensajes de usuario, y cortar ahí
        dejaría solo el último párrafo de una respuesta larga. No se guarda el
        razonamiento ni la salida de herramientas: el histórico es la
        conversación, no la máquina por dentro.
        """
        if not transcript or not os.path.isfile(transcript):
            return "", ""

        entradas = []
        with open(transcript, encoding="utf-8", errors="replace") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                try:
                    entradas.append(json.loads(linea))
                except (json.JSONDecodeError, ValueError):
                    continue

        partes, marca = [], ""
        for dato in reversed(entradas):
            if dato.get("isSidechain"):
                continue                    # los subagentes no son el diálogo
            if cls._es_usuario(dato):
                break
            if dato.get("type") != "assistant":
                continue
            textos = [b.get("text", "") for b in cls._bloques(dato)
                      if b.get("type") == "text" and b.get("text", "").strip()]
            if not textos:
                continue
            if not marca:
                marca = dato.get("uuid") or ""
            partes.insert(0, "\n\n".join(t.strip() for t in textos))

        return "\n\n".join(partes), marca

    @staticmethod
    def _es_usuario(dato):
        """Un mensaje escrito por la persona, no un resultado de herramienta."""
        if dato.get("type") != "user":
            return False
        contenido = (dato.get("message") or {}).get("content")
        if isinstance(contenido, str):
            return True
        if isinstance(contenido, list):
            return any(b.get("type") != "tool_result" for b in contenido if isinstance(b, dict))
        return False

    @staticmethod
    def _bloques(dato):
        contenido = (dato.get("message") or {}).get("content")
        if isinstance(contenido, list):
            return [b for b in contenido if isinstance(b, dict)]
        return []


class Historico:
    """La carpeta `historico-chat/` de un proyecto.

    La raíz se guarda tal como llega, sin resolverla: las rutas que se
    devuelven son las mismas que armaba el módulo de funciones, y los
    enganches las comparan y las muestran así.
    """

    def __init__(self, raiz):
        self.raiz = raiz

    @property
    def carpeta(self):
        return os.path.join(self.raiz, CARPETA)

    # ── Leer ──────────────────────────────────────────────────────────────

    @staticmethod
    def turnos(texto):
        """`[(quién, cuándo, lo dicho)]` de una transcripción, en orden.

        `quién` es `"usuario"` o `"agente"`; `cuándo`, la hora que el enganche
        anotó. **Lo que no encaja no se inventa:** un archivo sin ninguna marca
        devuelve una lista vacía, que es un dato y no un error.
        """
        salida = []
        marcas = list(_TURNO.finditer(texto or ""))
        for i, m in enumerate(marcas):
            fin = marcas[i + 1].start() if i + 1 < len(marcas) else len(texto)
            cuerpo = texto[m.end():fin]
            if m.group(1):
                quien, cuando = "usuario", m.group(2)
                # El mensaje del usuario se escribe citado, con `> ` delante.
                dicho = "\n".join(l[1:].lstrip() if l.startswith(">") else l
                                  for l in cuerpo.strip().split("\n"))
            else:
                quien, cuando = "agente", m.group(4)
                dicho = _SELLO_AGENTE.sub("", cuerpo).strip()
            salida.append((quien, (cuando or "").strip(), dicho.strip()))
        return salida

    def archivo(self, sesion, crear=False):
        """La ruta del archivo de esta sesión; lo crea si hace falta y se permite.

        Si el proyecto no tiene carpeta `historico-chat/`, no se inventa: ese
        proyecto no lleva histórico y el enganche no tiene nada que hacer.
        """
        carpeta = self.carpeta
        if not os.path.isdir(carpeta):
            return ""
        marca = f"<!-- sesion: {sesion} -->"
        for nombre in sorted(os.listdir(carpeta)):
            if not nombre.lower().endswith(".md") or nombre == INDICE:
                continue
            ruta = os.path.join(carpeta, nombre)
            if marca in _leer(ruta):
                return ruta
        return self._crear(carpeta, sesion) if crear and sesion else ""

    def archivo_de_sesion(self, sesion):
        """La ruta del histórico que lleva la marca de esa sesión, sin crear
        nada, o `""`. La traza la usa para nombrarse igual que el histórico."""
        return self.archivo(sesion, crear=False)

    def sesiones(self):
        """`[(archivo, de qué se trató)]`, en orden. Se leen del índice y no de
        la carpeta: el índice dice **de qué trató** cada una, y un listado de
        nombres no serviría para decidir cuál abrir."""
        salida = []
        for linea in _leer(os.path.join(self.carpeta, INDICE)).splitlines():
            m = _LINEA.match(linea.strip())
            if m and m.group(1).lower() != INDICE.lower():
                salida.append((m.group(1), (m.group(2) or "").strip()))
        return salida

    def contexto(self, limite=LIMITE, tope=None):
        """El índice de sesiones que se le inyecta al agente al abrir.

        Va el índice, **no** las transcripciones: son la conversación entera y
        llenarían la ventana. Con `tope`, en caracteres, se listan menos
        sesiones hasta caber: el arranque tiene 10.000 para todo
        (`EP-005·HU-009·CA-04`), y la cabeza ya dice dónde está el resto.
        """
        hechas = self.sesiones()
        if not hechas:
            return ""

        if tope is not None:
            for cuantas in range(min(limite, len(hechas)), 0, -1):
                texto = self.contexto(cuantas)
                if len(texto) <= tope:
                    return texto
            return ""

        recorte = hechas[-limite:]
        cabeza = [
            "[HISTÓRICO DE SESIONES — NO ESTÁ CARGADO, SOLO EL ÍNDICE]",
            "Cada sesión con este proyecto quedó transcrita literal. Antes de "
            "retomar un tema, leer con Read la sesión que lo trató: ahí está qué se "
            "decidió y por qué. No suponer qué dice una sesión por su título.",
        ]
        if len(hechas) > len(recorte):
            cabeza.append(f"Se listan las últimas {len(recorte)} de {len(hechas)}; "
                          f"el resto, en {CARPETA}/{INDICE}.")
        cuerpo = [f"  {CARPETA}/{archivo}" + (f" — {tema}" if tema else "")
                  for archivo, tema in recorte]
        return "\n".join(cabeza + [""] + cuerpo)

    # ── Escribir la conversación ─────────────────────────────────────────

    def anotar_usuario(self, sesion, mensaje):
        """Agrega el mensaje del usuario. La ruta escrita, o `""` si no aplica."""
        if not (mensaje or "").strip():
            return ""
        ruta = self.archivo(sesion, crear=True)
        if not ruta:
            return ""

        numero = self._siguiente_numero(_leer(ruta))
        # `EP-005·HU-002`: la clave se tapa **antes** de escribirse. Una vez en
        # el archivo ya no se borra: la transcripción se versiona.
        mensaje, _tapadas = Enmascarador.enmascarar(mensaje)
        cita = "\n".join(f"> {l}" if l.strip() else ">" for l in mensaje.rstrip().splitlines())
        # `EP-005·HU-024` · El aviso interno lleva su remitente: no lo escribió el usuario.
        quien = "Aviso del sistema" if es_aviso_interno(mensaje) else "Usuario"
        self._anotar(ruta, f"\n### {numero} · {quien} — {_ahora()}\n{cita}\n")

        # En cada mensaje, no solo al crear el archivo: si al crearlo no había
        # README, la sesión quedaría invisible. Es idempotente.
        nombre = os.path.basename(ruta)
        self._indexar(os.path.dirname(ruta), nombre, _fecha_de(nombre))
        return ruta

    def anotar_agente(self, sesion, transcript):
        """Agrega la respuesta del agente leída del transcript. Ruta escrita, o `""`."""
        respuesta, marca = Transcript.ultima_respuesta(transcript)
        if not respuesta:
            return ""
        ruta = self.archivo(sesion, crear=False)
        if not ruta:
            return ""                       # sin mensaje previo no hay dónde escribir
        if marca and f"<!-- agente: {marca} -->" in _leer(ruta):
            return ""                       # ya estaba: el enganche puede repetirse
        sello = f"\n<!-- agente: {marca} -->" if marca else ""
        respuesta, _tapadas = Enmascarador.enmascarar(respuesta)
        self._anotar(ruta, f"\n**Agente** — {_ahora()}{sello}\n\n{respuesta}\n")
        return ruta

    @staticmethod
    def _siguiente_numero(texto):
        numeros = [int(n) for n in _NUMERO.findall(texto)]
        return max(numeros) + 1 if numeros else 1

    @staticmethod
    def _anotar(ruta, bloque):
        """Mete el bloque al final de la conversación, no al final del archivo:
        la plantilla cierra con `## Abierto`, y pegar al final dejaría los
        mensajes nuevos por debajo de esa sección."""
        texto = _leer(ruta)
        corte = texto.find("\n## Abierto")
        if corte < 0:
            _agregar(ruta, bloque)
            return
        _sobrescribir(ruta, f"{texto[:corte].rstrip()}\n{bloque.rstrip()}\n\n{texto[corte:].lstrip()}")

    @classmethod
    def _crear(cls, carpeta, sesion):
        fecha = datetime.now().strftime("%Y-%m-%d")
        previas = [n for n in os.listdir(carpeta) if n.startswith(f"{fecha}-") and n.lower().endswith(".md")]
        sufijo = "" if not previas else f"-{len(previas) + 1}"
        nombre = f"{fecha}-sesion{sufijo}.md"
        ruta = os.path.join(carpeta, nombre)
        _sobrescribir(ruta, f"<!-- sesion: {sesion} -->\n\n# {fecha} — Sesión\n\n## Conversación\n")
        cls._indexar(carpeta, nombre, fecha)
        return ruta

    @staticmethod
    def _indexar(carpeta, nombre, fecha):
        """Agrega la línea al índice del README. Si no hay índice, no pasa nada."""
        ruta = os.path.join(carpeta, INDICE)
        if not os.path.isfile(ruta):
            return
        texto = _leer(ruta)
        if f"({nombre})" in texto:
            return
        linea = f"- [{nombre}]({nombre}) — sesión del {fecha}.\n"
        _agregar(ruta, linea if texto.endswith("\n") else f"\n{linea}")

    # ── Ponerle el tema al nombre ─────────────────────────────────────────

    @classmethod
    def aviso_de_nombre(cls, ruta):
        """Lo que hay que recordarle al agente para que nombre la sesión, o `""`.

        Se pide **una sola vez** y no en el primer mensaje: al abrir el chat
        nadie sabe todavía de qué va a tratar. Se pide cuando ya hubo una
        respuesta y queda la marca en el archivo para no volver a pedirlo. No
        renombra nada: el nombre lo aprueba el usuario.
        """
        if not ruta:
            return ""
        nombre = os.path.basename(ruta)
        if not _GENERICO.match(nombre):
            return ""                       # ya tiene tema
        texto = _leer(ruta)
        if MARCA_NOMBRE in texto or "\n**Agente**" not in texto:
            return ""                       # ya se pidió, o todavía no hay tema

        cls._marcar(ruta)
        orden = os.path.abspath(__file__).replace(os.sep, "/")
        return "\n".join([
            "[HISTÓRICO — ESTA SESIÓN TODAVÍA NO TIENE NOMBRE]",
            f"Se está guardando en `{CARPETA}/{nombre}`, que no dice de qué trata. "
            "Ese nombre y su línea en el índice son lo único que la próxima sesión "
            "va a ver de esta.",
            "Antes de seguir, proponer en una línea el nombre y el resumen — por "
            "ejemplo: «esta sesión la guardo como "
            f"{_fecha_de(nombre)}-<tema>.md — <de qué se trató>, ¿va?».",
            "Si el usuario aprueba, correr esto, que renombra el archivo y corrige "
            "la línea del índice (las dos cosas, o el índice apunta a un archivo "
            "que ya no está):",
            f'    python "{orden}" --renombrar "{os.path.abspath(ruta).replace(os.sep, "/")}" '
            '--tema "<tema-en-guiones>" --resumen "<de qué se trató>"',
            "Y pedirle que pegue esta línea, que le pone el mismo nombre a la "
            "sesión de Claude Code —lo que se ve en la pestaña, en la barra del "
            "prompt y en `/resume`—. Es un comando del usuario: el agente no puede "
            "escribirlo por él.",
            "    /rename <tema-en-guiones>",
            "Si no quiere ponerle nombre, se deja como está. Esto se pide una sola "
            "vez en la sesión.",
        ])

    @staticmethod
    def _marcar(ruta):
        """Deja `MARCA_NOMBRE` bajo la marca de sesión, en la cabecera del archivo."""
        lineas = _leer(ruta).split("\n")
        lineas.insert(1 if lineas and lineas[0].startswith("<!-- sesion:") else 0, MARCA_NOMBRE)
        _sobrescribir(ruta, "\n".join(lineas))

    @classmethod
    def renombrar(cls, archivo, tema, resumen=""):
        """Le pone el tema al nombre del archivo y corrige el índice. Ruta nueva.

        Las dos cosas van juntas: renombrar sin tocar el índice deja una línea
        apuntando a un archivo que ya no existe. La fecha sale del nombre viejo,
        no del reloj: una sesión que se nombra al otro día sigue siendo la del
        día que ocurrió.
        """
        archivo = os.path.abspath(archivo)
        if not os.path.isfile(archivo):
            raise FileNotFoundError(f"no existe el archivo de sesión: {archivo}")
        if not cls._slug(tema):
            raise ValueError("el tema queda vacío al pasarlo a nombre de archivo")

        carpeta = os.path.dirname(archivo)
        viejo = os.path.basename(archivo)
        nuevo = cls._libre(carpeta, f"{_fecha_de(viejo)}-{cls._slug(tema)}.md", viejo)

        cls._titular(archivo, _fecha_de(viejo), tema)
        cls._mover_resumen(carpeta, viejo, nuevo)
        if nuevo != viejo:
            os.rename(archivo, os.path.join(carpeta, nuevo))
        cls._reindexar(carpeta, viejo, nuevo, resumen)
        return os.path.join(carpeta, nuevo)

    @classmethod
    def _mover_resumen(cls, carpeta, viejo, nuevo):
        """Le pone el nombre nuevo al resumen de esa sesión, si ya existe.

        Va **antes** de mover la transcripción y de tocar el índice: si algo
        falla, lo que queda mal es el resumen, que se puede volver a mover, y
        no el índice. El resumen se llama igual que la transcripción sin la
        fecha, así que los dos nombres se mueven juntos.
        """
        fecha = _fecha_de(viejo)
        dia = os.path.join(carpeta, RESUMENES, fecha)
        origen = os.path.join(dia, os.path.basename(viejo)[len(fecha) + 1:])
        destino = os.path.join(dia, os.path.basename(nuevo)[len(fecha) + 1:])
        if origen == destino or not os.path.isfile(origen) or os.path.exists(destino):
            return
        try:
            os.rename(origen, destino)
        except OSError:
            return                          # no poder moverlo no detiene el renombrado
        cls._reindexar_dia(dia, os.path.basename(origen), os.path.basename(destino))
        cls._reenlazar(destino, carpeta, os.path.basename(viejo), os.path.basename(nuevo))

    @staticmethod
    def _reenlazar(resumen, carpeta, viejo, nuevo):
        """Deja con el nombre nuevo el enlace que el resumen le hace a su sesión.

        Se cambian **las dos partes**, el texto y el destino, porque `13·DOC14`
        pide que el texto diga dónde vive el archivo. Se reemplaza el par
        exacto, no toda aparición del nombre viejo: un resumen puede nombrar
        otras sesiones, y a esas no hay que tocarles nada.
        """
        texto = _leer(resumen)
        if not texto:
            return
        hist = os.path.basename(carpeta.rstrip(os.sep + "/"))
        nuevo_texto = texto.replace(f"[{hist}/{viejo}]({HACIA_HISTORICO}{viejo})",
                                    f"[{hist}/{nuevo}]({HACIA_HISTORICO}{nuevo})")
        # Y el que lleve otro texto, que igual apunta a la misma sesión.
        nuevo_texto = nuevo_texto.replace(f"]({HACIA_HISTORICO}{viejo})", f"]({HACIA_HISTORICO}{nuevo})")
        if nuevo_texto == texto:
            return
        try:
            _sobrescribir(resumen, nuevo_texto)
        except OSError:
            return                          # tampoco esto detiene el renombrado

    @staticmethod
    def _reindexar_dia(dia, viejo, nuevo):
        """Deja la línea del índice del día apuntando al nombre nuevo."""
        ruta = os.path.join(dia, INDICE)
        if not os.path.isfile(ruta):
            return
        texto = _leer(ruta)
        if f"({viejo})" not in texto:
            return
        _sobrescribir(ruta, texto.replace(f"[{viejo}]({viejo})", f"[{nuevo}]({nuevo})"))

    @classmethod
    def _titular(cls, ruta, fecha, tema):
        """Cambia el título `# AAAA-MM-DD — Sesión` por el tema real."""
        texto = _leer(ruta)
        nuevo = re.sub(rf"^# {re.escape(fecha)} — .*$", f"# {fecha} — {cls._legible(tema)}",
                       texto, count=1, flags=re.MULTILINE)
        if nuevo != texto:
            _sobrescribir(ruta, nuevo)

    @classmethod
    def _reindexar(cls, carpeta, viejo, nuevo, resumen):
        """Deja la línea del índice apuntando al nombre nuevo, con el resumen."""
        ruta = os.path.join(carpeta, INDICE)
        if not os.path.isfile(ruta):
            return
        resumen = (resumen or "").strip() or f"sesión del {_fecha_de(nuevo)}"
        if not resumen.endswith((".", "!", "?")):
            resumen += "."
        linea = f"- [{nuevo}]({nuevo}) — {resumen}{cls._enlace_al_resumen(carpeta, nuevo)}"

        salida, puesta = [], False
        for cruda in _leer(ruta).splitlines():
            m = _LINEA.match(cruda.strip())
            if m and m.group(1) == viejo:
                salida.append(linea)
                puesta = True
            else:
                salida.append(cruda)
        texto = "\n".join(salida).rstrip("\n") + "\n"
        if not puesta:
            texto += f"{linea}\n"           # no estaba indexada: se agrega ahora
        _sobrescribir(ruta, texto)

    @staticmethod
    def _enlace_al_resumen(carpeta, nombre):
        """` · [ruta](ruta)` al resumen de esa sesión, o `""` si todavía no existe.

        El resumen vive en `resumenes/AAAA-MM-DD/<tema>.md`. Si el archivo no
        está, no se inventa el enlace: uno roto en el índice es peor que no
        tenerlo. El texto dice dónde vive desde la raíz (`13·DOC14`); el
        destino, el camino desde el índice (pendiente 68).
        """
        fecha = _fecha_de(nombre)
        tema = os.path.basename(nombre)[len(fecha) + 1:]
        if not tema:
            return ""
        rel = f"{RESUMENES}/{fecha}/{tema}"
        if not os.path.isfile(os.path.join(carpeta, RESUMENES, fecha, tema)):
            return ""
        return f" · [{CARPETA}/{rel}]({rel})"

    @staticmethod
    def _libre(carpeta, nombre, actual):
        """`nombre`, o con sufijo `-2`, `-3` si ese ya está ocupado por otro."""
        if nombre == actual or not os.path.exists(os.path.join(carpeta, nombre)):
            return nombre
        raiz, ext = os.path.splitext(nombre)
        n = 2
        while os.path.exists(os.path.join(carpeta, f"{raiz}-{n}{ext}")):
            n += 1
        return f"{raiz}-{n}{ext}"

    @staticmethod
    def _slug(tema):
        """El tema como parte de un nombre de archivo: minúsculas y guiones.

        Se quitan las tildes y la eñe pasa a `n`: el nombre viaja en enlaces,
        rutas y URLs. El texto con tildes se conserva en el título y el índice.
        """
        plano = unicodedata.normalize("NFKD", str(tema or ""))
        plano = "".join(c for c in plano if not unicodedata.combining(c))
        return re.sub(r"-{2,}", "-", re.sub(r"[^a-z0-9]+", "-", plano.lower())).strip("-")

    @staticmethod
    def _legible(tema):
        """El tema para el título: guiones a espacios y la primera en mayúscula."""
        texto = str(tema or "").replace("-", " ").replace("_", " ").strip()
        return texto[:1].upper() + texto[1:] if texto else "Sesión"


def main(argv=None):
    """`--renombrar <archivo> --tema <tema> [--resumen <texto>]`.

    Es lo que corre el agente cuando el usuario aprueba el nombre. Va por
    comando y no a mano para que el archivo y el índice cambien juntos.
    """
    import argparse

    preparar_salida()
    p = argparse.ArgumentParser(description="Le pone el tema al nombre de una sesión del histórico.")
    p.add_argument("--renombrar", metavar="ARCHIVO", required=True,
                   help="el archivo de la sesión, tal como está hoy")
    p.add_argument("--tema", required=True, help="de qué trató, en pocas palabras")
    p.add_argument("--resumen", default="", help="la línea del índice; si falta, queda la fecha")
    a = p.parse_args(argv)

    try:
        ruta = Historico.renombrar(a.renombrar, a.tema, a.resumen)
    except (OSError, ValueError) as e:
        print(f"No se pudo renombrar: {e}", file=sys.stderr)
        return 1
    print(f"Sesión guardada como {os.path.basename(ruta)}; índice al día.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
