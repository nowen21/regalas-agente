# -*- coding: utf-8 -*-
"""`EP-027·HU-004` · El estándar se lee como página.

Del texto de cada documento sale lo que la pantalla muestra: su título, su
capítulo, sus relaciones y su HTML. El paso a HTML es código propio, sin la
librería `markdown` (análisis 1 del pendiente 136, acuerdo 3). El texto se
escapa primero y solo después se le ponen las etiquetas: nada del documento
entra como HTML (RNF-02).
"""
import posixpath
import re
from collections import OrderedDict

from django.urls import reverse
from django.utils.html import escape

from core.comun import Markdown

_ENCABEZADO = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
_CERCA = re.compile(r"^\s*(```|~~~)")
_RAYA = re.compile(r"^\s*([-*_])(\s*\1){2,}\s*$")
_SEPARADOR = re.compile(r"^\s*\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)*\|?\s*$")
_ITEM = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")
_REGLA = re.compile(r"^([A-Z]+\d+(?:\.\d+)?)\s*·\s*(.+)$")
_MARCA = re.compile(r"\s*·?\s*`\[([^\]]*)\]`")
_CAPITULO = re.compile(r"^base/(\d\d-[^/]+?)(?:\.md)?(?:/|$)")
_ENLACE = re.compile(r"\[((?:[^\[\]]|\[[^\]]*\])*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
_CODIGO = re.compile(r"(`+)(.+?)\1")
_NEGRITA = re.compile(r"\*\*(.+?)\*\*")
_CURSIVA = re.compile(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])")
_DEPENDENCIA = re.compile(
    r"\b(extiende(?: a)?|depende de|deroga(?: a)?)\s+"
    r"((?:\[(?:[^\[\]]|\[[^\]]*\])*\]\([^)\s]+\)(?:\s*(?:,|y|e|o)\s*)?)+)")
_EXTERNO = re.compile(r"^(https?:|mailto:)")
_ESTADOS = {"CUMPLE": "success", "NO CUMPLE": "danger", "DEROGADA": "secondary", "PENDIENTE": "warning"}
GENERAL, TAREAS = "general", "tareas"


def _sin_marcas(texto):
    """El texto sin comillas invertidas ni asteriscos: así se lee un título."""
    return re.sub(r"\*\*|`", "", texto).strip()


def leer_titulo(texto):
    """`(título, marca)` del primer encabezado. La marca es lo que va entre
    ``[ ]`` después del título: `CAPA 2`, `DEROGADA en 4.0.0 → ver 13·DOC1`."""
    for _, linea in Markdown.lineas_utiles(texto):
        m = _ENCABEZADO.match(linea)
        if m:
            marcas = _MARCA.findall(m.group(2))
            return _sin_marcas(_MARCA.sub("", m.group(2))), " ".join(marcas)
    return "", ""


def ancla(texto):
    """El ancla que pone GitHub a un encabezado: así la escriben los enlaces del estándar."""
    texto = _sin_marcas(re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", texto)).lower()
    return re.sub(r"[^\w\- ]", "", texto).replace(" ", "-")


def capitulo_de(ruta):
    m = _CAPITULO.match(ruta)
    if m:
        return m.group(1)
    return TAREAS if ruta.startswith("base/reglas-por-tarea/") else GENERAL


def es_cabeza(ruta):
    """El documento que abre un capítulo: `base/NN-x.md` o `base/NN-x/base.md`."""
    return bool(re.match(r"^base/\d\d-[^/]+\.md$|^base/\d\d-[^/]+/base\.md$", ruta))


def es_regla(ruta):
    return "/reglas/" in ruta


def _orden_natural(codigo):
    return [int(p) if p.isdigit() else p for p in re.split(r"(\d+)", codigo or "")]


class Ficha:
    """Lo que la pantalla sabe de un documento sin mostrar su ruta."""

    def __init__(self, documento):
        self.pk = documento.pk
        self.ruta = documento.ruta
        self.contenido = documento.contenido
        titulo, marca = leer_titulo(documento.contenido)
        if not titulo:
            titulo = posixpath.basename(documento.ruta)[:-3].replace("-", " ").capitalize()
        m = _REGLA.match(titulo)
        self.codigo, self.nombre = (m.group(1), m.group(2)) if m else ("", titulo)
        self.titulo = titulo
        self.derogada = "DEROGADA" in marca.upper()
        self.capitulo = capitulo_de(documento.ruta)

    @property
    def url(self):
        return reverse("estandar:documento", args=[self.pk])

    def secciones(self):
        """Las reglas que un capítulo de un solo archivo lleva como secciones `## C1 · …`."""
        salida = []
        for _, linea in Markdown.lineas_utiles(self.contenido):
            m = _ENCABEZADO.match(linea)
            if m and len(m.group(1)) == 2:
                regla = _REGLA.match(_sin_marcas(_MARCA.sub("", m.group(2))))
                if regla:
                    salida.append({"pk": self.pk, "codigo": regla.group(1), "nombre": regla.group(2),
                                   "url": "%s#%s" % (self.url, ancla(m.group(2))),
                                   "derogada": "DEROGADA" in m.group(2).upper()})
        return salida


class Estandar:
    """Todos los documentos a la vez: los enlaces, los capítulos y las relaciones
    se resuelven contra lo que hay en la base, no contra los archivos."""

    def __init__(self, documentos):
        self.fichas = [Ficha(d) for d in documentos]
        self.por_ruta = {f.ruta: f for f in self.fichas}
        self.por_pk = {f.pk: f for f in self.fichas}

    def destino(self, enlace, desde):
        """`(ficha, ancla)` al que lleva un enlace escrito en `desde`, o None si no está en la base."""
        camino, _, marca = enlace.partition("#")
        if not camino:
            ficha = self.por_ruta.get(desde)
        else:
            ficha = self.por_ruta.get(posixpath.normpath(posixpath.join(posixpath.dirname(desde), camino)))
        return (ficha, marca) if ficha else None

    def url(self, enlace, desde):
        if _EXTERNO.match(enlace):
            return enlace
        llega = self.destino(enlace, desde)
        if not llega:
            return None
        return llega[0].url + ("#" + llega[1] if llega[1] else "")

    def nombre_de(self, ficha, marca):
        """Código y nombre de la regla a la que apunta un enlace."""
        if marca:
            for s in ficha.secciones():
                if s["url"].endswith("#" + marca):
                    return s["codigo"], s["nombre"]
        return ficha.codigo, ficha.nombre

    # --- Capítulos ---------------------------------------------------------

    def capitulos(self):
        """Los capítulos en orden, cada uno con su nombre y sus renglones:
        el capítulo, sus reglas en orden y sus anexos."""
        grupos = OrderedDict()
        for f in sorted(self.fichas, key=lambda f: (f.capitulo == TAREAS, f.capitulo == GENERAL, f.capitulo)):
            grupos.setdefault(f.capitulo, {"clave": f.capitulo, "nombre": "", "cabeza": [], "reglas": [], "anexos": []})
            grupo = grupos[f.capitulo]
            if es_cabeza(f.ruta):
                grupo["nombre"] = f.titulo
                grupo["cabeza"].append({"pk": f.pk, "nombre": "El capítulo completo", "url": f.url})
                grupo["reglas"].extend(f.secciones())
            elif es_regla(f.ruta):
                grupo["reglas"].append({"pk": f.pk, "codigo": f.codigo, "nombre": f.nombre, "url": f.url, "derogada": f.derogada})
            else:
                grupo["anexos"].append({"pk": f.pk, "nombre": f.titulo, "url": f.url})
        for g in grupos.values():
            g["reglas"].sort(key=lambda r: _orden_natural(r["codigo"]))
            g["anexos"].sort(key=lambda a: a["nombre"])
            g["nombre"] = g["nombre"] or {GENERAL: "Documentos generales", TAREAS: "Reglas de cada tarea"}.get(
                g["clave"], g["clave"].replace("-", " ").capitalize())
            g["renglones"] = g["cabeza"] + g["reglas"] + g["anexos"]
        return list(grupos.values())

    def capitulo_de(self, ficha):
        """Nombre y enlace del capítulo de un documento, para las migas."""
        for f in self.fichas:
            if f.capitulo == ficha.capitulo and es_cabeza(f.ruta):
                return {"nombre": f.titulo, "url": f.url, "es_el_mismo": f.pk == ficha.pk}
        return None

    # --- Relaciones --------------------------------------------------------

    def _renglon(self, ficha, marca):
        codigo, nombre = self.nombre_de(ficha, marca)
        return {"codigo": codigo, "nombre": nombre, "url": ficha.url + ("#" + marca if marca else "")}

    def relaciones(self, ficha):
        """Las dependencias de `20·M7`, las reglas que nombra el texto y los
        documentos que la nombran, cada cosa por separado (acuerdo 3)."""
        texto = "\n".join(Markdown.sin_codigo_en_linea(l) for _, l in Markdown.lineas_utiles(ficha.contenido))
        dependencias, vistos = [], set()
        for m in _DEPENDENCIA.finditer(texto):
            tipo = m.group(1).split()[0].capitalize().replace("Depende", "Depende de")
            for enlace in _ENLACE.finditer(m.group(2)):
                llega = self.destino(enlace.group(2), ficha.ruta)
                if llega and llega[0].pk != ficha.pk and (llega[0].pk, llega[1]) not in vistos:
                    vistos.add((llega[0].pk, llega[1]))
                    dependencias.append(dict(self._renglon(*llega), tipo=tipo))
        nombra = []
        for _, _, destino in Markdown.enlaces(ficha.contenido):
            llega = self.destino(destino, ficha.ruta)
            if llega and llega[0].pk != ficha.pk and (llega[0].pk, llega[1]) not in vistos:
                vistos.add((llega[0].pk, llega[1]))
                nombra.append(self._renglon(*llega))
        la_nombran = []
        for otra in self.fichas:
            if otra.pk == ficha.pk:
                continue
            if any((self.destino(d, otra.ruta) or (None,))[0] is ficha for _, _, d in Markdown.enlaces(otra.contenido)):
                la_nombran.append({"codigo": otra.codigo, "nombre": otra.nombre, "url": otra.url})
        la_nombran.sort(key=lambda r: (not r["codigo"], _orden_natural(r["codigo"]), r["nombre"]))
        return {"dependencias": dependencias, "nombra": nombra, "la_nombran": la_nombran}

    # --- El texto como página ---------------------------------------------

    def html(self, ficha):
        return Pagina(self, ficha.ruta).armar(ficha.contenido, saltar_titulo=True)


class Pagina:
    """Pasa el texto de un documento a HTML con los componentes de Tabler."""

    def __init__(self, estandar, ruta):
        self.estandar = estandar
        self.ruta = ruta
        self.usados = {}

    def _id(self, texto):
        """El ancla del encabezado; la que se repite lleva -1, -2…, como en GitHub."""
        base = ancla(texto)
        veces = self.usados.get(base, 0)
        self.usados[base] = veces + 1
        return base if not veces else "%s-%d" % (base, veces)

    # --- Lo que va dentro de una línea ------------------------------------

    def linea(self, texto):
        guardado = []

        def guardar(html):
            guardado.append(html)
            return "\x00%d\x00" % (len(guardado) - 1)

        texto = _CODIGO.sub(lambda m: guardar("<code>%s</code>" % escape(m.group(2).strip())), texto)
        texto = _ENLACE.sub(lambda m: guardar(self._enlace(m.group(1), m.group(2), guardado)), texto)
        texto = self._formato(escape(texto))
        while "\x00" in texto:
            texto = re.sub(r"\x00(\d+)\x00", lambda m: guardado[int(m.group(1))], texto)
        return texto

    @staticmethod
    def _formato(texto):
        texto = _NEGRITA.sub(r"<strong>\1</strong>", texto)
        texto = re.sub(r"&lt;br\s*/?&gt;", "<br>", texto)
        return _CURSIVA.sub(r"<em>\1</em>", texto)

    def _enlace(self, rotulo, destino, guardado):
        rotulo = self._formato(escape(rotulo))
        rotulo = re.sub(r"\x00(\d+)\x00", lambda m: guardado[int(m.group(1))], rotulo)
        url = self.estandar.url(destino, self.ruta)
        if url is None:
            return '<span class="text-secondary">%s</span>' % rotulo
        if _EXTERNO.match(url):
            return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (escape(url), rotulo)
        return '<a href="%s">%s</a>' % (escape(url), rotulo)

    # --- Los bloques -------------------------------------------------------

    def armar(self, texto, saltar_titulo=False):
        lineas = texto.replace("\r\n", "\n").split("\n")
        salida, parrafo, i = [], [], 0

        def cerrar_parrafo():
            if parrafo:
                junto = " ".join(l.strip() for l in parrafo)
                aplica = re.match(r"^\*\*Aplica a:\*\*\s*(.+)$", junto)
                if aplica:
                    salida.append(self.aplica_a(aplica.group(1)))
                else:
                    salida.append("<p>%s</p>" % self.linea(junto))
                parrafo.clear()

        while i < len(lineas):
            linea = lineas[i]
            if not linea.strip():
                cerrar_parrafo()
                i += 1
            elif _CERCA.match(linea):
                cerrar_parrafo()
                fin = i + 1
                while fin < len(lineas) and not _CERCA.match(lineas[fin]):
                    fin += 1
                salida.append(self.bloque_de_codigo(lineas[i + 1:fin]))
                i = fin + 1
            elif _ENCABEZADO.match(linea):
                cerrar_parrafo()
                m = _ENCABEZADO.match(linea)
                if saltar_titulo:
                    saltar_titulo = False
                    salida.append('<span id="%s"></span>' % self._id(m.group(2)))
                elif _sin_marcas(m.group(2)).startswith("Checklist"):
                    fin = i + 1
                    while fin < len(lineas) and not (
                            _ENCABEZADO.match(lineas[fin]) and len(_ENCABEZADO.match(lineas[fin]).group(1)) <= 2):
                        fin += 1
                    while fin > i + 1 and (not lineas[fin - 1].strip() or _RAYA.match(lineas[fin - 1])):
                        fin -= 1
                    salida.append(self.sello(m.group(2), lineas[i + 1:fin]))
                    i = fin
                    continue
                else:
                    salida.append(self.encabezado(len(m.group(1)), m.group(2)))
                i += 1
            elif _RAYA.match(linea):
                cerrar_parrafo()
                siguiente = next((l for l in lineas[i + 1:] if l.strip()), "")
                if not _ENCABEZADO.match(siguiente):
                    salida.append('<hr class="my-4">')
                i += 1
            elif linea.lstrip().startswith("|") and i + 1 < len(lineas) and _SEPARADOR.match(lineas[i + 1]):
                cerrar_parrafo()
                fin = i + 2
                while fin < len(lineas) and lineas[fin].lstrip().startswith("|"):
                    fin += 1
                salida.append(self.tabla(lineas[i], lineas[i + 2:fin]))
                i = fin
            elif linea.lstrip().startswith(">"):
                cerrar_parrafo()
                fin = i
                while fin < len(lineas) and lineas[fin].lstrip().startswith(">"):
                    fin += 1
                adentro = [re.sub(r"^\s*>\s?", "", l) for l in lineas[i:fin]]
                salida.append('<div class="alert alert-info">%s</div>' % self.armar("\n".join(adentro)))
                i = fin
            elif _ITEM.match(linea):
                cerrar_parrafo()
                fin = i + 1
                while fin < len(lineas) and lineas[fin].strip() and (
                        _ITEM.match(lineas[fin]) or lineas[fin].startswith((" ", "\t"))):
                    fin += 1
                salida.append(self.lista(lineas[i:fin]))
                i = fin
            else:
                parrafo.append(linea)
                i += 1
        cerrar_parrafo()
        return "\n".join(salida)

    @staticmethod
    def aplica_a(tareas):
        """La línea «Aplica a» de `20·M5`: las tareas como insignias."""
        insignias = "".join('<span class="badge bg-info-subtle text-info-emphasis">%s</span>' % escape(t.strip())
                            for t in tareas.split(",") if t.strip())
        return ('<div class="d-flex flex-wrap align-items-center gap-1 my-3">'
                '<span class="text-secondary me-1">Aplica a</span>%s</div>' % insignias)

    def sello(self, titulo, lineas):
        """El sello del checklist (`20·M9`) en una tarjeta que se abre al pulsarla:
        dice si la regla cumple sin tapar lo que exige."""
        estado = "NO CUMPLE" if "NO CUMPLE" in titulo.upper() else ("CUMPLE" if "CUMPLE" in titulo.upper() else "")
        ancla_ = self._id(titulo)
        id_ = "sello-%s" % ancla_
        insignia = ('<span class="badge bg-%s-subtle text-%s-emphasis ms-2">%s</span>' % (_ESTADOS[estado], _ESTADOS[estado], estado.capitalize())
                    if estado else "")
        return ('<div class="card my-3" id="%s"><div class="card-header">'
                '<a class="card-title text-reset d-flex align-items-center w-100" data-bs-toggle="collapse" '
                'href="#%s-cuerpo" role="button" aria-expanded="false" aria-controls="%s-cuerpo">'
                'Sello del checklist%s<span class="ms-auto text-secondary small">Ver el detalle</span></a></div>'
                '<div class="collapse" id="%s-cuerpo"><div class="card-body">%s</div></div></div>'
                % (ancla_, id_, id_, insignia, id_, self.armar("\n".join(lineas))))

    def encabezado(self, nivel, texto):
        id_ = self._id(texto)
        marcas = _MARCA.findall(texto)
        limpio = _MARCA.sub("", texto)
        insignias = "".join(' <span class="badge bg-secondary-subtle text-secondary-emphasis ms-1">%s</span>' % escape(m) for m in marcas)
        regla = _REGLA.match(_sin_marcas(limpio)) if nivel == 2 else None
        etiqueta = "h%d" % min(nivel + 1, 6)
        if regla:
            return ('<%s id="%s" class="mt-5 mb-3 pt-3 border-top"><span class="badge bg-primary-subtle text-primary-emphasis me-2">%s</span>%s%s</%s>'
                    % (etiqueta, id_, escape(regla.group(1)), self.linea(regla.group(2)), insignias, etiqueta))
        return '<%s id="%s" class="mt-4 mb-2">%s%s</%s>' % (etiqueta, id_, self.linea(limpio), insignias, etiqueta)

    def bloque_de_codigo(self, lineas):
        """El ejemplo INCORRECTO / CORRECTO de `20·M5` va en dos tarjetas; lo demás, como código."""
        partes, actual = [], None
        for l in lineas:
            m = re.match(r"^\s*(INCORRECTO|CORRECTO)\s*:?\s?(.*)$", l)
            if m:
                actual = [m.group(1), [m.group(2)]]
                partes.append(actual)
            elif actual:
                actual[1].append(l)
            else:
                break
        else:
            if partes:
                return self.ejemplo(partes)
        return '<pre class="p-3 bg-body-tertiary border rounded"><code>%s</code></pre>' % escape("\n".join(lineas))

    @staticmethod
    def ejemplo(partes):
        tarjetas = []
        for tipo, texto in partes:
            bien = tipo == "CORRECTO"
            color, rotulo, signo = ("success", "Correcto", "✓") if bien else ("danger", "Incorrecto", "✗")
            cuerpo = escape("\n".join(l.strip() for l in texto).strip())
            tarjetas.append(
                '<div class="col-md-6"><div class="card card-outline card-%s h-100">'
                '<div class="card-body"><div class="text-%s fw-bold mb-1"><span aria-hidden="true">%s</span> %s</div>'
                '<div class="ejemplo-texto">%s</div></div></div></div>' % (color, color, signo, rotulo, cuerpo))
        return '<div class="row g-2 my-3">%s</div>' % "".join(tarjetas)

    @staticmethod
    def celdas(linea):
        """Parte un renglón de tabla por sus `|`, sin partir dentro de comillas invertidas."""
        linea = linea.strip()
        linea = linea[1:] if linea.startswith("|") else linea
        linea = linea[:-1] if linea.endswith("|") and not linea.endswith("\\|") else linea
        celdas, actual, en_codigo, i = [], "", False, 0
        while i < len(linea):
            c = linea[i]
            if c == "\\" and i + 1 < len(linea) and linea[i + 1] == "|":
                actual += "|"
                i += 2
                continue
            if c == "`":
                en_codigo = not en_codigo
            if c == "|" and not en_codigo:
                celdas.append(actual.strip())
                actual = ""
            else:
                actual += c
            i += 1
        celdas.append(actual.strip())
        return celdas

    def celda(self, texto):
        estado = _ESTADOS.get(_sin_marcas(texto).upper())
        if estado:
            return '<span class="badge bg-%s-subtle text-%s-emphasis">%s</span>' % (estado, estado, escape(_sin_marcas(texto)))
        return self.linea(texto)

    def tabla(self, cabecera, filas):
        titulos = "".join("<th>%s</th>" % self.linea(c) for c in self.celdas(cabecera))
        cuerpo = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % self.celda(c) for c in self.celdas(f)) for f in filas)
        return ('<div class="card my-3"><div class="table-responsive"><table class="table align-middle mb-0">'
                '<thead><tr>%s</tr></thead><tbody>%s</tbody></table></div></div>' % (titulos, cuerpo))

    def lista(self, lineas):
        """Listas con viñeta o con número, anidadas por la sangría."""
        items = []  # (sangría, ordenada, texto)
        for l in lineas:
            m = _ITEM.match(l)
            if m:
                items.append([len(m.group(1).expandtabs(4)), m.group(2)[0].isdigit(), m.group(3)])
            elif items:
                items[-1][2] += " " + l.strip()
        return self._lista(items, 0)[0]

    def _lista(self, items, i):
        sangria, ordenada = items[i][0], items[i][1]
        partes = []
        while i < len(items) and items[i][0] >= sangria:
            if items[i][0] > sangria:
                interna, i = self._lista(items, i)
                partes[-1] = partes[-1][:-5] + interna + "</li>"
                continue
            texto = items[i][2]
            casilla = re.match(r"^\[([ xX])\]\s+(.*)$", texto)
            if casilla:
                texto = ("☑ " if casilla.group(1).strip() else "☐ ") + casilla.group(2)
            partes.append("<li>%s</li>" % self.linea(texto))
            i += 1
        etiqueta = "ol" if ordenada else "ul"
        return "<%s>%s</%s>" % (etiqueta, "".join(partes), etiqueta), i


# --- EP-027·HU-005 · Nombres legibles -----------------------------------------

def _con_espacios(nombre):
    nombre = re.sub(r"\.md$", "", nombre or "")
    nombre = re.sub(r"[-_]+", " ", nombre).strip()
    return nombre[:1].upper() + nombre[1:]


def recuerdo_legible(nombre, texto):
    """`(nombre, descripción)` de un recuerdo: el título de su texto o, si no
    tiene, su nombre con espacios; la descripción, la de su bloque de arriba."""
    texto = (texto or "").replace("\r\n", "\n")
    arriba, cuerpo = {}, texto
    if texto.startswith("---\n"):
        fin = texto.find("\n---", 4)
        if fin > 0:
            for linea in texto[4:fin].split("\n"):
                clave, _, valor = linea.partition(":")
                arriba[clave.strip()] = valor.strip()
            cuerpo = texto[fin + 4:]
    titulo = leer_titulo(cuerpo)[0]
    return titulo or _con_espacios(arriba.get("name") or nombre), arriba.get("description", "")


def titulo_de_texto(texto, ruta):
    """El título de un documento desde su texto, o su nombre de archivo con espacios."""
    return leer_titulo(texto or "")[0] or _con_espacios(posixpath.basename(ruta or ""))
