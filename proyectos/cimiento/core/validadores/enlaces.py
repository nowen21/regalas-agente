"""Coherencia de los documentos: enlaces rotos, el texto de cada enlace (`13·DOC14`)
e índices de carpeta al día.

`Enlaces` reúne lo que deciden los cuatro de este módulo: qué enlace se puede
comprobar, cuál se salta y qué texto le corresponde. **El que reporta y el que
arregla miran igual a propósito**: si se separan, el arreglo deja hallazgos
vivos o toca lo que nadie reportó.
"""
import os
import re
from urllib.parse import unquote

from ..comun import AVISO, FALLA, Archivos, Hallazgo, Markdown, Proyecto
from .base import Validador

HISTORICO = "historico-chat"
# Carpetas cuyo README.md lista todos sus `.md`. El histórico entra aunque nadie
# lo escriba a mano: una sesión que no está en el índice no la encuentra la siguiente.
CON_INDICE = ["pendientes", "notas", HISTORICO]
RESUMENES = HISTORICO + "/resumenes"
PROMPTS = "prompts"
EXTERNOS = ("http://", "https://", "mailto:", "ftp://", "//")

# Las plantillas citan las reglas con este marcador delante, porque se copian
# dentro de un proyecto y allá `../base/` no es el estándar. Sin llenar, se
# resuelve contra la carpeta del estándar, no contra la que se valida.
MARCADOR_RAIZ = "«RUTA-ESTANDAR»"

_ANALISIS = re.compile(r"^analisis-\d+\.md$")
_SECCION = re.compile(r"^##\s+(.*?)\s*$")
_CON_ESPACIO = re.compile(r"\]\(([^)\n<]*?\s[^)\n]*?)\)")


class Enlaces:
    """Las decisiones sobre enlaces que comparten el validador y el reparador."""

    def __init__(self, proyecto):
        self.proyecto = proyecto

    @staticmethod
    def es_interno(destino):
        return not (destino.startswith(EXTERNOS) or destino.startswith("#"))

    @staticmethod
    def comprobable(texto, destino):
        """¿Se puede comprobar contra el disco? No los ejemplos con `<…>`, ni lo que
        apunta a código de un proyecto: solo `.md` y carpetas."""
        if "<" in texto or ">" in texto or "<" in destino or ">" in destino:
            return False
        ruta = destino.split("#", 1)[0]
        return ruta.lower().endswith(".md") or ruta.endswith("/")

    @staticmethod
    def es_transcripcion(archivo):
        """¿Es una sesión de `historico-chat/` y no su índice? Se copia literal del
        chat, con enlaces que se rompen por definición; reescribirlos la haría
        dejar de ser prueba de lo que se dijo."""
        return (os.path.basename(os.path.dirname(archivo)) == HISTORICO
                and os.path.basename(archivo).lower() != "readme.md")

    def es_del_usuario(self, archivo):
        """¿Está en `prompts/`? Son palabras del usuario: reescribir un enlace ahí es editarle la frase."""
        return os.path.relpath(archivo, self.proyecto.raiz).replace("\\", "/").split("/")[0] == PROMPTS

    @staticmethod
    def lineas_de_conversacion(archivo, texto):
        """Los renglones de la «Conversación» de un `analisis-N.md`: es copia literal
        del chat, y corregirle un enlace es cambiar lo que se dijo."""
        if not _ANALISIS.match(os.path.basename(archivo)):
            return set()
        salida, dentro = set(), False
        for n, linea in enumerate(texto.splitlines(), 1):
            m = _SECCION.match(linea)
            if m:
                dentro = m.group(1).lower() == "conversación"
            elif dentro:
                salida.add(n)
        return salida

    @staticmethod
    def es_vecino(destino):
        """¿Apunta a un archivo de la misma carpeta? `DOC14` pide la ruta desde la
        raíz «para saber dónde vive sin abrirlo», y para el vecino eso ya se sabe."""
        ruta = destino.split("#", 1)[0]
        return bool(ruta) and "/" not in ruta and not ruta.startswith(".")

    @staticmethod
    def destinos_con_espacio(texto):
        """`[(línea, destino)]` de destinos con un espacio literal: el espacio corta
        el enlace y lo vuelve invisible para todos. Lo que va entre `<…>` sí lo admite."""
        salida, en_cerca = [], False
        for n, linea in enumerate(texto.splitlines(), 1):
            if linea.lstrip().startswith(("```", "~~~")):
                en_cerca = not en_cerca
                continue
            if not en_cerca:
                salida += [(n, m.group(1)) for m in _CON_ESPACIO.finditer(Markdown.sin_codigo_en_linea(linea))
                           if not m.group(1).startswith(("http://", "https://", "mailto:", "«"))]
        return salida

    def destino_en_disco(self, archivo, destino):
        """La ruta en disco a la que lleva un destino; `%20` se decodifica."""
        ruta = unquote(destino.split("#", 1)[0])
        if not ruta:
            return None
        if ruta.startswith(MARCADOR_RAIZ):
            return os.path.normpath(os.path.join(Proyecto.estandar() or self.proyecto.raiz,
                                                 ruta[len(MARCADOR_RAIZ):].lstrip("/")))
        return os.path.normpath(os.path.join(os.path.dirname(archivo), ruta))

    def texto_esperado(self, archivo, texto, destino):
        """El texto que `DOC14` pide para el enlace, o `None` si no aplica o ya está
        bien: el externo, el de texto descriptivo (`[la guía]`) y el que ya dice la ruta."""
        if not self.es_interno(destino) or not self.comprobable(texto, destino):
            return None
        limpio = texto.strip().strip("`").strip()
        if "/" not in limpio and not limpio.lower().endswith(".md"):
            return None
        objetivo = os.path.normpath(os.path.join(os.path.dirname(archivo), destino.split("#", 1)[0]))
        esperado = os.path.relpath(objetivo, self.proyecto.raiz).replace("\\", "/")
        if limpio.lstrip("./").rstrip("/") == esperado.rstrip("/"):
            return None
        if not limpio.endswith("/"):
            return esperado
        # El texto nombra una carpeta. Si el destino es un archivo de ella (su
        # README), el texto sigue nombrando la carpeta: pegarle el archivo
        # dejaba `[base/x/README.md/](x/README.md)` (sesión del 2026-10-04).
        if not destino.split("#", 1)[0].endswith("/"):
            esperado = os.path.dirname(esperado)
            if limpio.lstrip("./").rstrip("/") == esperado:
                return None
        return esperado.rstrip("/") + "/"


class EnlacesRotos(Validador):
    """Todo enlace comprobable de un `.md` lleva a algo que existe."""

    nombre = "enlaces"
    regla = "13·DOC14"
    descripcion = "enlaces rotos en los documentos"

    def validar(self):
        e = Enlaces(self.proyecto)
        hallazgos = []
        for archivo in self.proyecto.recorrer_md():
            if e.es_transcripcion(archivo):
                continue
            texto = self.archivos.leer(archivo)
            hallazgos += [Hallazgo(AVISO, archivo, n, "el destino lleva un espacio sin codificar y deja de "
                                                       "ser enlace: %s (escribirlo con %%20)" % destino)
                          for n, destino in e.destinos_con_espacio(texto)]
            for n, etiqueta, destino in Markdown.enlaces(texto):
                if e.es_interno(destino) and e.comprobable(etiqueta, destino):
                    objetivo = e.destino_en_disco(archivo, destino)
                    if objetivo and not os.path.exists(objetivo):
                        hallazgos.append(Hallazgo(FALLA, archivo, n, "enlace roto: %s" % destino))
        return hallazgos


class FormatoDeEnlaces(Validador):
    """`13·DOC14`: el enlace cuyo texto tiene forma de ruta dice la ruta desde la raíz."""

    nombre = "formato-enlaces"
    regla = "13·DOC14"
    descripcion = "el texto del enlace dice dónde vive el archivo"

    def validar(self):
        e = Enlaces(self.proyecto)
        hallazgos = []
        for archivo in self.proyecto.recorrer_md():
            if e.es_transcripcion(archivo):
                continue
            contenido = self.archivos.leer(archivo)
            conversacion = e.lineas_de_conversacion(archivo, contenido)
            for n, texto, destino in Markdown.enlaces(contenido):
                esperado = None if n in conversacion else e.texto_esperado(archivo, texto, destino)
                if esperado is not None:
                    hallazgos.append(Hallazgo(AVISO, archivo, n, "el texto del enlace dice «%s» y el destino es "
                                                                 "«%s» — DOC14 pide la ruta desde la raíz"
                                              % (texto.strip().strip("`").strip(), esperado)))
        return hallazgos


class IndicesDeCarpetas(Validador):
    """Cada `.md` de una carpeta con índice está en su README, y cada día de
    resúmenes está en el índice de días; y al revés."""

    nombre = "indices"
    regla = "13·DOC17"
    descripcion = "los índices de carpeta están al día"

    def __init__(self, proyecto, archivos=None, carpetas=None):
        super().__init__(proyecto, archivos)
        self.carpetas = carpetas or CON_INDICE

    def validar(self):
        return self.archivos_de_carpetas() + self.dias_de_resumenes()

    def archivos_de_carpetas(self):
        hallazgos = []
        for nombre in self.carpetas:
            carpeta = os.path.join(self.proyecto.raiz, nombre)
            indice = os.path.join(carpeta, "README.md")
            if not os.path.isfile(indice):
                continue
            enlazados = {os.path.normpath(os.path.join(carpeta, d.split("#", 1)[0]))
                         for _, _, d in Markdown.enlaces(self.archivos.leer(indice)) if Enlaces.es_interno(d)}
            for archivo in sorted(os.listdir(carpeta)):
                ruta = os.path.normpath(os.path.join(carpeta, archivo))
                if archivo.lower().endswith(".md") and archivo != "README.md" and ruta not in enlazados:
                    hallazgos.append(Hallazgo(FALLA, indice, 0, "el índice no menciona %s" % self.proyecto.mostrar(ruta)))
            hallazgos += [Hallazgo(AVISO, indice, 0, "el índice menciona %s, que ya no existe" % self.proyecto.mostrar(ruta))
                          for ruta in sorted(enlazados)
                          if os.path.dirname(ruta) == os.path.normpath(carpeta) and not os.path.exists(ruta)]
        return hallazgos

    def dias_de_resumenes(self):
        """Cada carpeta de día está en el índice de días: si no, sus resúmenes
        existen y nadie los va a abrir."""
        carpeta = self.proyecto.ruta(RESUMENES)
        indice = os.path.join(carpeta, "README.md")
        if not os.path.isfile(indice):
            return []
        texto = self.archivos.leer(indice)
        dias = sorted(d for d in os.listdir(carpeta) if os.path.isdir(os.path.join(carpeta, d)))
        hallazgos = [Hallazgo(FALLA, indice, 0, "el índice de días no menciona %s/ — sus resúmenes existen "
                                                "y nadie los va a encontrar" % dia)
                     for dia in dias if "(%s/)" % dia not in texto]
        for _, _, destino in Markdown.enlaces(texto):
            d = destino.rstrip("/")
            if "/" not in d and d[:4].isdigit() and d not in dias:
                hallazgos.append(Hallazgo(AVISO, indice, 0, "el índice de días menciona %s/, que ya no existe" % d))
        return hallazgos


class ReparadorDeEnlaces:
    """Reescribe el **texto** de los enlaces para que diga la ruta desde la raíz.

    El destino no se toca nunca: ya funciona, y tocarlo es la única forma de
    romper un enlace que hoy anda. El vecino de la misma carpeta se deja fuera
    por defecto, y también las transcripciones y `prompts/`.
    """

    def __init__(self, proyecto, archivos=None):
        self.proyecto = proyecto if isinstance(proyecto, Proyecto) else Proyecto(proyecto)
        self.enlaces = Enlaces(self.proyecto)
        self.archivos = archivos or Archivos()

    def reparar_texto(self, contenido, archivo, incluir_vecinos=False):
        """`(texto nuevo, cuántos)` sobre un texto en memoria. Lo usa quien mueve un
        archivo, para no dejar atrás el texto que lo nombraba donde vivía antes."""
        e = self.enlaces
        if e.es_transcripcion(archivo) or e.es_del_usuario(archivo):
            return contenido, 0
        conversacion = e.lineas_de_conversacion(archivo, contenido)
        cambios = [(n, "[%s](%s)" % (texto, destino), "[%s](%s)" % (esperado, destino))
                   for n, texto, destino in Markdown.enlaces(contenido)
                   if n not in conversacion and (incluir_vecinos or not e.es_vecino(destino))
                   for esperado in [e.texto_esperado(archivo, texto, destino)] if esperado is not None]
        # Por renglón: reemplazar en todo el texto tocaba también las copias que no se debían tocar.
        lineas = contenido.splitlines(keepends=True)
        for n, viejo, nuevo in cambios:
            lineas[n - 1] = lineas[n - 1].replace(viejo, nuevo)
        return "".join(lineas), len(cambios)

    def reparar(self, escribir=False, incluir_vecinos=False):
        """`[(archivo, cuántos)]` en todo el proyecto. Sin `escribir`, solo simula."""
        tocados = []
        for archivo in self.proyecto.recorrer_md():
            original = self.archivos.leer(archivo)
            nuevo, cuantos = self.reparar_texto(original, archivo, incluir_vecinos)
            if cuantos:
                if escribir:
                    with open(archivo, "w", encoding="utf-8", newline="\n") as f:
                        f.write(nuevo)
                tocados.append((archivo, cuantos))
        return tocados
