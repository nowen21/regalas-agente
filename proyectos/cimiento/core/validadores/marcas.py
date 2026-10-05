"""`00·ID8` · Las marcas que delatan generación automática, contadas.

La regla manda escribir sin las marcas de
`base/00-identidad-y-rol/marcadores-de-ia.md`. **Solo se cuenta lo mecánico**:
lo que el anexo llama «las únicas que un script cuenta sin equivocarse». La
mayoría de sus secciones piden criterio, y un programa que opinara de eso
llenaría de ruido lo que hoy nadie mira.

No se mira lo de adentro de un bloque cercado o de comillas invertidas (ahí las
marcas son ejemplos), el propio catálogo (está lleno de marcas por definición)
ni `historico-chat/`, que es transcripción literal y se cuenta aparte.

Tres piezas: `Marcas` mide un texto y limpia lo que tiene un solo reemplazo;
`MarcasDeGeneracion` es el validador, sobre lo heredado o sobre lo que entra en
el commit (el trinquete); `contar` da el recuento de todo el árbol.
"""
import re

from ..comun import AVISO, FALLA, Git, Hallazgo, Markdown
from ..comun.proyecto import EXCLUIDAS
from .base import Validador

# Los archivos que hablan **de** las marcas: contarlas ahí es contar el catálogo.
CATALOGO = (
    "base/00-identidad-y-rol/marcadores-de-ia.md",
    "base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md",
    "validadores/marcas.py",
)
HISTORICO = "historico-chat"
# Lo que viaja a los proyectos: ahí `00·ID8` importa y ahí bloquea el trinquete.
HEREDADAS = ("base", "plantillas")

# Sección 3 del anexo · las invisibles. El orden es el de los hallazgos de una línea.
INVISIBLES = {
    " ": "espacio duro (U+00A0)",
    "​": "ancho cero (U+200B)",
    "﻿": "marca de orden de bytes (U+FEFF)",
    "­": "guion suave (U+00AD)",
    "…": "puntos suspensivos en un solo carácter (…)",
    "–": "semiraya (–) donde va un guion",
    " ": "espacio fino (U+2009)",
    " ": "espacio fino sin salto (U+202F)",
}
# `EP-004·HU-025` · Los caracteres de control, que tampoco se ven: una fila de
# tabla que empezaba con `U+0001` desaparecía del cuadro. Se barre el rango
# completo menos salto de línea, retorno y tabulador.
_CONTROL = tuple(chr(c) for c in list(range(0x00, 0x20)) + [0x7F] if c not in (0x09, 0x0A, 0x0D))
for _c in _CONTROL:
    INVISIBLES[_c] = "caracter de control (U+%04X)" % ord(_c)

# Lo que se reemplaza sin criterio: cada uno tiene **un** reemplazo. La raya, el
# punto medio y la viñeta con negrita no están: quitarlas es reescribir la frase.
REEMPLAZOS = {
    " ": " ", " ": " ", " ": " ",
    "​": "", "﻿": "", "­": "",
    "…": "...", "–": "-",
    "“": '"', "”": '"',
}
for _c in _CONTROL:
    REEMPLAZOS[_c] = ""

# Qué se escribe en lugar de cada marca, con las palabras del anexo.
EN_SU_LUGAR = {
    "raya": "coma, dos puntos o paréntesis",
    "punto-medio": "punto, coma o la palabra que une las frases",
    "comilla": "comillas rectas, o las angulares « »",
    "vineta": "texto normal, o una tabla si son campos; negrita solo donde resalta algo",
    "flecha": "guion de lista, o la palabra que dice la relación",
    "semaforo": "la palabra: cumple, en riesgo o no cumple",
    "encabezado": "el mismo encabezado sin los dos puntos",
}

# Lo que no se cuenta, y se dice: un cero sin alcance se lee como «limpio» (`EP-004·HU-024`).
NO_SE_CUENTAN = "el español de otra parte, la estructura demasiado pareja, el tono, y el contraste con lo escrito antes"

# Sección 2 del anexo · lo que se cuenta sin opinar.
_CITA = re.compile(r"\d{2}·[A-Z]")                  # `NN·ID`: notación de la casa
_ENCABEZADO = re.compile(r"^#{1,6} ")
_SEPARADOR = " · "                                   # `09 · Control de versiones`
_CAPITULO = re.compile(r"(?<!\d)\d{1,2} · ")         # así se nombra un capítulo, en todas partes
_RAYA = "—"
# La raya cuenta como inciso, y no lo son el identificador con lo que enuncia
# (`**CAE-01** — …`) ni la celda de tabla.
_ETIQUETA_Y_ENUNCIADO = re.compile(r"\s*(?:[-*+] )?(?:\w+\. )?(?:\[[ x]\] )?\*\*[^*]+\*\*\s+—")
_FILA_DE_TABLA = re.compile(r"^\s*\|")
# El rótulo de un campo por llenar no es una viñeta de prosa: `- **Objetivo:** «…»`.
_CAMPO_POR_LLENAR = re.compile(r"^\s*[-*+]\s+\*\*[^*]+:\*\*\s*(?:`?«|$)")
_VINETA_NEGRITA = re.compile(r"^\s*[-*+]\s+\*\*[^*]+:\*\*")
_FLECHA_VINETA = re.compile(r"^\s*[→✓]\s")
_SEMAFORO = re.compile(r"[\U0001F534\U0001F7E1\U0001F7E2]")
_ENCABEZADO_DOS_PUNTOS = re.compile(r"^#{1,6}\s+.*:\s*$")
_COMILLA_CURVA = re.compile(r"[“”]")
# El relleno de las plantillas es notación de la casa: tres validadores lo reconocen.
_MARCADOR = "«…»"
# El bloque de checklist de una regla: su forma la fija `checklist.md`, no quien escribe.
_SELLO = re.compile(r"(?ms)^(?:---\s*\n+)?### Checklist.*?(?=^## |\Z)")


class Marcas:
    """Medir y limpiar un texto. No sabe de archivos ni de proyectos."""

    @staticmethod
    def de_linea(linea):
        """`[(clave, qué)]` de una línea ya limpia de código."""
        salida = []
        linea = linea.replace(_MARCADOR, "")
        for caracter, nombre in INVISIBLES.items():
            salida += [(caracter, nombre)] * linea.count(caracter)

        rayas = linea.count(_RAYA)
        if _ENCABEZADO.match(linea) or _FILA_DE_TABLA.match(linea):
            rayas = 0
        elif _ETIQUETA_Y_ENUNCIADO.match(linea):
            rayas -= 1
        salida += [("raya", "raya larga (—) como inciso")] * max(rayas, 0)

        capitulos = len(_CAPITULO.findall(linea))
        puntos = linea.count("·") - len(_CITA.findall(linea)) - capitulos
        if _ENCABEZADO.match(linea):
            puntos -= linea.count(_SEPARADOR) - capitulos
        if _FILA_DE_TABLA.match(linea):
            puntos = 0
        salida += [("punto-medio", "punto medio (·) fuera de una cita `NN·ID`")] * max(puntos, 0)

        salida += [("comilla", "comilla curva (“ ”)")] * len(_COMILLA_CURVA.findall(linea))
        if _VINETA_NEGRITA.match(linea) and not _CAMPO_POR_LLENAR.match(linea):
            salida.append(("vineta", "viñeta que abre con negrita y dos puntos"))
        if _FLECHA_VINETA.match(linea):
            salida.append(("flecha", "flecha o visto usado como viñeta"))
        salida += [("semaforo", "semáforo (🔴 🟡 🟢) en un documento formal")] * len(_SEMAFORO.findall(linea))
        if _ENCABEZADO_DOS_PUNTOS.match(linea):
            salida.append(("encabezado", "encabezado que termina en dos puntos"))
        return salida

    @classmethod
    def de_texto(cls, texto):
        """`[(línea, clave, qué)]` saltando bloques cercados y comillas invertidas."""
        return [(n, clave, nombre) for n, linea in Markdown.lineas_utiles(texto)
                for clave, nombre in cls.de_linea(Markdown.sin_codigo_en_linea(linea))]

    @staticmethod
    def sin_sellos(texto):
        return _SELLO.sub("", texto)

    @classmethod
    def medir(cls, texto):
        """`[(línea, clave, qué es, qué va en su lugar)]` de un texto suelto.

        `EP-004·HU-012·CA-05` · Es lo que mide el enganche de escritura sobre lo
        que el agente **acaba de escribir**, no sobre el archivo entero.
        """
        salida = []
        for n, clave, nombre in cls.de_texto(cls.sin_sellos(texto)):
            if clave in REEMPLAZOS:
                nuevo = REEMPLAZOS[clave]
                lugar = "un espacio normal" if nuevo == " " else "quitarlo" if not nuevo else "«%s»" % nuevo
            else:
                lugar = EN_SU_LUGAR.get(clave, "lo que dice el anexo de marcas")
            salida.append((n, clave, nombre, lugar))
        return salida

    @classmethod
    def cuenta(cls, texto):
        """`{clave: cuántas}`, sin código ni sellos."""
        salida = {}
        for _, clave, _ in cls.de_texto(cls.sin_sellos(texto)):
            salida[clave] = salida.get(clave, 0) + 1
        return salida

    @staticmethod
    def limpiar(texto):
        """`(nuevo, cuántos)` con los reemplazos hechos **fuera de código**:
        adentro, la marca es el ejemplo de lo que no hay que hacer."""
        salida, cambios, cercado = [], 0, False
        for linea in texto.split("\n"):
            if linea.lstrip().startswith(("```", "~~~")):
                cercado = not cercado
            if cercado or linea.lstrip().startswith(("```", "~~~")):
                salida.append(linea)
                continue
            trozos = linea.split("`")
            for i in range(0, len(trozos), 2):      # los pares quedan fuera del código
                if _MARCADOR in trozos[i]:
                    continue
                for viejo, nuevo in REEMPLAZOS.items():
                    if viejo in trozos[i]:
                        cambios += trozos[i].count(viejo)
                        trozos[i] = trozos[i].replace(viejo, nuevo)
            salida.append("`".join(trozos))
        return "\n".join(salida), cambios


class MarcasDeGeneracion(Validador):
    """Las marcas de lo que se hereda, o el trinquete sobre lo que entra en el commit.

    **El trinquete no bloquea todo**: medido sobre seis commits, eran 425 marcas
    de estilo agregadas, y un enganche que rechaza cada commit se desactiva en
    una tarde. Bloquea las invisibles en cualquier archivo y todas las marcas en
    `base/` y `plantillas/`; lo demás se avisa.
    """

    nombre = "marcas"
    regla = "00·ID8"
    descripcion = "marcas de generación automática en lo que se hereda"

    def __init__(self, proyecto, archivos=None, solo_preparados=False):
        super().__init__(proyecto, archivos)
        self.solo_preparados = solo_preparados
        self.mirados = None

    def _relativa(self, archivo):
        return self.proyecto.relativa(archivo) or ""

    def _fuera_de_cuenta(self, relativa):
        return relativa in CATALOGO

    def validar(self):
        return self._preparados() if self.solo_preparados else self._heredadas()

    def _heredadas(self):
        """Una por clase y por línea: el recuento va en `contar`."""
        hallazgos, self.mirados = [], 0
        for archivo in self.proyecto.recorrer_md():
            rel = self._relativa(archivo)
            if self._fuera_de_cuenta(rel) or rel.split("/")[0] not in HEREDADAS:
                continue
            self.mirados += 1
            vistas = set()
            for n, clave, nombre in Marcas.de_texto(self.archivos.leer(archivo)):
                if (n, clave) not in vistas:
                    vistas.add((n, clave))
                    hallazgos.append(Hallazgo(AVISO, archivo, n, "%s — `00·ID8` pide entregar sin las "
                                                                 "marcas del anexo" % nombre))
        return hallazgos

    def alcance(self):
        """Las dos frases que acompañan al resultado: qué se miró y qué no.
        Salen de lo que la corrida recorrió de verdad."""
        carpetas = ", ".join("`%s/`" % c for c in HEREDADAS)
        if self.mirados == 0:
            primera = "no se miró ningún archivo: en %s no hay ninguno que revisar" % carpetas
        else:
            cuantos = "" if self.mirados is None else " (%d archivos)" % self.mirados
            primera = "se recorrió %s%s, que es lo que viaja a los proyectos" % (carpetas, cuantos)
        return primera, "no se cuenta lo que hay que leer para verlo: %s" % NO_SE_CUENTAN

    def _preparados(self):
        git = Git(self.proyecto.raiz)
        hallazgos = []
        for rel in git.preparados():
            if not rel.lower().endswith(".md") or self._fuera_de_cuenta(rel) or rel.split("/")[0] == HISTORICO:
                continue
            # Las copias que escribe un programa (`reglas-por-tarea/`) ya se
            # midieron en su archivo, y lo traído de otro proyecto no lo escribió el agente.
            if any(p in EXCLUIDAS for p in rel.split("/")[:-1]) or self.proyecto.es_excluida(rel):
                continue
            hallazgos += self._crecimiento_como_hallazgos(git, rel)
        return hallazgos

    def _crecimiento_como_hallazgos(self, git, rel):
        ruta = self.proyecto.ruta(rel)
        heredado = rel.split("/")[0] in HEREDADAS
        salida = []
        for clave, cuantas in sorted(self.crecimiento(git, rel).items(), key=lambda x: -x[1]):
            if clave in INVISIBLES:
                salida.append(Hallazgo(FALLA, ruta, 0, "agrega %d · %s — no se escribe a propósito y se "
                                                       "quita en segundos (`00·ID8`)" % (cuantas, INVISIBLES[clave])))
            elif heredado:
                salida.append(Hallazgo(FALLA, ruta, 0, "agrega %d · %s — esto se hereda: `base/` y "
                                                       "`plantillas/` son lo que viaja a los proyectos "
                                                       "(`00·ID8`)" % (cuantas, clave)))
            else:
                salida.append(Hallazgo(AVISO, ruta, 0, "agrega %d · %s — no bloquea acá, pero es deuda "
                                                       "que alguien limpia después (`00·ID8`)" % (cuantas, clave)))
        return salida

    @staticmethod
    def crecimiento(git, rel):
        """`{clave: cuántas suma}` del archivo preparado respecto de `HEAD`.

        Se compara el archivo entero y no el diff, para seguir saltando los
        bloques cercados. Un `git mv` no agrega marcas: si el archivo no estaba
        en `HEAD`, se compara con su nombre anterior.
        """
        ahora = git.correr("show", ":%s" % rel)
        if not ahora:
            return {}
        antes = git.correr("show", "HEAD:%s" % rel)
        if not antes:
            for linea in git.lineas("diff", "--cached", "--name-status", "--find-renames"):
                partes = linea.split("\t")
                if len(partes) == 3 and partes[0].startswith("R") and partes[2] == rel:
                    antes = git.correr("show", "HEAD:%s" % partes[1])
                    break
        a, b = Marcas.cuenta(ahora), Marcas.cuenta(antes)
        return {k: a.get(k, 0) - b.get(k, 0) for k in set(a) | set(b) if a.get(k, 0) > b.get(k, 0)}

    def contar(self, incluir_historico=False):
        """`({clave: cuántas}, {archivo: cuántas}, {clave: nombre})` de todo el
        árbol: por marca, para saber qué pesa; por archivo, para saber por dónde empezar."""
        por_marca, por_archivo, nombres = {}, {}, {}
        for archivo in self.proyecto.recorrer_md():
            rel = self._relativa(archivo)
            if self._fuera_de_cuenta(rel) or (rel.split("/")[0] == HISTORICO and not incluir_historico):
                continue
            marcas = Marcas.de_texto(self.archivos.leer(archivo))
            for _, clave, nombre in marcas:
                por_marca[clave] = por_marca.get(clave, 0) + 1
                nombres[clave] = nombre
            if marcas:
                por_archivo[rel] = len(marcas)
        return por_marca, por_archivo, nombres

    def limpiar(self, carpetas=HEREDADAS, escribir=False):
        """`[(archivo, cuántos)]` de lo mecánico limpiado. Sin `escribir` solo simula."""
        tocados = []
        for archivo in self.proyecto.recorrer_md():
            rel = self._relativa(archivo)
            if self._fuera_de_cuenta(rel) or rel.split("/")[0] == HISTORICO:
                continue
            if carpetas and rel.split("/")[0] not in carpetas:
                continue
            nuevo, cambios = Marcas.limpiar(self.archivos.leer(archivo))
            if cambios:
                tocados.append((rel, cambios))
                if escribir:
                    with open(archivo, "w", encoding="utf-8", newline="\n") as f:
                        f.write(nuevo)
        return tocados
