"""Las citas entre reglas se enlazan, no solo se nombran (`20·M4`).

Una regla que cita a otra por su identificador (`09·G2`, `M5`) obliga a quien
lee a salir a buscarla. Acá hay tres piezas:

  `IndiceDeReglas`  dónde vive cada regla, leído de `base/`: la verdad es el
                    archivo, no una tabla escrita a mano que envejece.
  `CitasEnlazadas`  ninguna cita queda suelta y ningún enlace apunta al vacío.
  `EnlazadorDeCitas` enlaza las sueltas y reapunta las que quedaron mal.

Lo de adentro de un bloque cercado no se toca: ahí las citas son ejemplos del
molde, no citas a nadie.
"""
import os
import re

from ..comun import AVISO, FALLA, Hallazgo, Markdown
from .base import Validador

BASE = "base"

# `## <ID> · <título>`. También `#`: una regla que creció hasta ocupar su propia
# carpeta abre con H1. El H1 de un capítulo lleva número, no ID, y no encaja.
_REGLA = re.compile(r"^(#{1,2})\s+([A-Z]{1,4}\d+(?:\.\d+)?)\s*·\s*(.+?)\s*$")
_REGLA_M = re.compile(_REGLA.pattern, re.MULTILINE)
# Una sub-regla en negrita: `**F12.1** — …` o `**F12.13 · Materialización física**`.
_SUBREGLA = re.compile(r"\*\*([A-Z]{1,4}\d+\.\d+)(?:\s*·[^*]*)?\*\*")

_ID = r"[A-Z]{1,4}\d+(?:\.\d+)?"
# Tres formas de citar conviven, y `M4` solo admite la primera: `04·S4`,
# `00` · N3 y `00`·N3. `(?<!\[)` descarta lo que ya es enlace.
_CITA_PARTIDA = re.compile(r"(?<!\[)`(\d{2})`\s*·\s*(%s)" % _ID)
_CITA = re.compile(r"(?<!\[)`(?:(\d{2})·)?(%s)`" % _ID)
# La dependencia sin comillas dentro del paréntesis, como pide `M7`: «(extiende 09·G6)».
_DEPENDENCIA = re.compile(r"\((extiende|depende de|deroga)\s+(?:(\d{2})·)?(%s)\)" % _ID)
_CITA_ENLAZADA = re.compile(r"\[`(?:(\d{2})·)?([A-Z]{1,4}\d+(?:\.\d+)?)`\]\(([^)]+)\)")
_CERCA = re.compile(r"^\s*(```|~~~)")
_SEPARADOR_DE_TABLA = re.compile(r"\|[-:|\s]+\|")

# `55` · Una celda bajo estas columnas **muestra** un identificador; no cita
# ninguna regla. Exigirle el enlace obliga a redactar torcido.
COLUMNAS_DE_EJEMPLO = {
    "lo que sale mal", "así se ve", "asi se ve", "ejemplo", "ejemplos",
    "incorrecto", "correcto", "mal", "bien", "qué es de verdad",
}


def _celdas_de(linea):
    return [c.strip() for c in linea.strip().strip("|").split("|")]


def _es_muestra(linea, columnas, id_):
    """¿El identificador cae en una celda de una columna de ejemplos?"""
    if not columnas or not linea.strip().startswith("|"):
        return False
    for i, celda in enumerate(_celdas_de(linea)):
        if id_ in celda and i < len(columnas):
            return columnas[i] in COLUMNAS_DE_EJEMPLO
    return False


def _ya_enlazada(antes, id_):
    """`55` · Exigir el enlace en la segunda mención del mismo documento es
    ruido: quien lee ya lo tiene más arriba, o en este mismo renglón."""
    return "[`%s`](" % id_ in antes or "·%s`](" % id_ in antes


def _columnas_de_la_tabla(linea, anterior, columnas):
    """Las columnas de la tabla en curso: la fila anterior al renglón de guiones.
    Se olvidan al salir de la tabla."""
    if _SEPARADOR_DE_TABLA.fullmatch(linea.strip()):
        previas = anterior.splitlines()
        return [c.lower() for c in _celdas_de(previas[-1])] if anterior.strip() and previas else []
    if not linea.strip().startswith("|"):
        return []
    return columnas


class IndiceDeReglas:
    """`{ID: (ruta absoluta, ancla)}` de todas las reglas de `base/`."""

    def __init__(self, proyecto, archivos):
        self.proyecto = proyecto
        self.reglas = self._indexar(archivos)

    @staticmethod
    def ancla(titulo_completo):
        """El ancla que GitHub genera para un encabezado.

        **Cada** espacio pasa a un guion: el `·` entre ID y título va entre
        espacios, y al quitarlo quedan dos seguidos. Colapsarlos daría un enlace
        que no lleva a ninguna parte.
        """
        t = re.sub(r"[^\w\s-]", "", titulo_completo.strip().lower(), flags=re.UNICODE)
        return re.sub(r"\s", "-", t).strip("-")

    def _indexar(self, archivos):
        salida = {}
        for archivo in self.proyecto.recorrer_md(BASE):
            texto = archivos.leer(archivo)
            for _, linea in Markdown.lineas_utiles(texto):
                m = _REGLA.match(linea)
                if not m:
                    continue
                nivel, id_, titulo = m.groups()
                # Una regla por archivo: el enlace al archivo ya es el enlace a
                # la regla, y un ancla de más se rompería al renombrar el título.
                sola = nivel == "#" or (len(_REGLA_M.findall(texto)) == 1
                                        and os.path.basename(archivo).startswith(id_ + "-"))
                salida[id_] = (archivo, "" if sola else self.ancla("%s · %s" % (id_, titulo)))
            # Las sub-reglas en negrita no tienen encabezado: el enlace es al
            # archivo de su madre, que es mejor que no llevar a ninguna parte.
            for m in _SUBREGLA.finditer(texto):
                sub = m.group(1)
                madre = sub.split(".")[0]
                if madre in salida and salida[madre][0] == archivo:
                    salida.setdefault(sub, (archivo, ""))
        return salida

    def __contains__(self, id_):
        return id_ in self.reglas

    def __len__(self):
        return len(self.reglas)

    def archivo_de(self, id_):
        return self.reglas[id_][0]

    def destino(self, origen, id_):
        """El enlace relativo desde `origen` hasta la regla, o `""` si no existe."""
        if id_ not in self.reglas:
            return ""
        archivo, anc = self.reglas[id_]
        rel = os.path.relpath(archivo, os.path.dirname(origen)).replace("\\", "/")
        return "%s#%s" % (rel, anc) if anc else rel


class CitasEnlazadas(Validador):
    """Citas sueltas y enlaces que no llevan a ninguna regla, en `base/`."""

    nombre = "citas"
    regla = "20·M4"
    descripcion = "citas entre reglas sin enlace o mal apuntadas"

    def validar(self):
        idx = IndiceDeReglas(self.proyecto, self.archivos)
        hallazgos = []
        for archivo in self.proyecto.recorrer_md(BASE):
            hallazgos += self._revisar(archivo, idx)
        return hallazgos

    def _revisar(self, archivo, idx):
        hallazgos, dentro, columnas, previo = [], False, [], ""
        for n, linea in enumerate(self.archivos.leer(archivo).splitlines(), start=1):
            anterior, previo = previo, previo + linea + "\n"
            if _CERCA.match(linea):
                dentro = not dentro
                continue
            if dentro or linea.lstrip().startswith("#"):
                continue
            columnas = _columnas_de_la_tabla(linea, anterior, columnas)
            for m in _CITA_ENLAZADA.finditer(linea):
                hallazgos += self._enlace_mal_apuntado(archivo, n, m.group(2), m.group(3), idx)
            for m in _CITA.finditer(linea):
                id_ = m.group(2)
                if (id_ not in idx or idx.archivo_de(id_) == archivo
                        or _ya_enlazada(anterior + linea[:m.start()], id_) or _es_muestra(linea, columnas, id_)):
                    continue
                hallazgos.append(Hallazgo(AVISO, archivo, n, "la cita `%s` no lleva enlace — quien lea "
                                                             "tiene que ir a buscarla" % id_))
        return hallazgos

    @staticmethod
    def _enlace_mal_apuntado(archivo, n, id_, ruta, idx):
        if id_ not in idx:
            return [Hallazgo(FALLA, archivo, n, "la cita `%s` enlaza a una regla que no existe" % id_)]
        # `55` · El ancla suelta a una regla del mismo archivo es la forma correcta.
        if not ruta.split("#")[0] and idx.archivo_de(id_) == archivo:
            return []
        esperado = idx.destino(archivo, id_)
        if ruta.split("#")[0] != esperado.split("#")[0]:
            return [Hallazgo(AVISO, archivo, n, "la cita `%s` apunta a «%s» y la regla está en «%s»"
                             % (id_, ruta, esperado))]
        return []


class EnlazadorDeCitas:
    """Enlaza las citas sueltas y reapunta las mal apuntadas, con las mismas
    exclusiones que el validador: si no, escribe en `base/` lo que el validador
    ya aceptó que no era una cita."""

    def __init__(self, proyecto, archivos=None):
        self.validador = CitasEnlazadas(proyecto, archivos)
        self.proyecto = self.validador.proyecto
        self.archivos = self.validador.archivos
        self.indice = IndiceDeReglas(self.proyecto, self.archivos)

    def enlazar(self, texto, origen):
        """`(texto, cuántas)` con las citas convertidas en enlaces y normalizadas a `NN·ID`."""
        idx, cambios, salida = self.indice, [0], []
        dentro, columnas, previo = False, [], ""

        def enlace(capitulo, id_, literal, antes):
            ruta = idx.destino(origen, id_)
            # Sin destino no se inventa un enlace: un enlace roto es peor que ninguno.
            if (not ruta or idx.archivo_de(id_) == origen or _es_muestra(linea_actual[0], columnas, id_)
                    or _ya_enlazada(previo + antes, id_)):
                return literal
            cambios[0] += 1
            return "[`%s`](%s)" % ("%s·%s" % (capitulo, id_) if capitulo else id_, ruta)

        linea_actual = [""]
        for linea in texto.splitlines(keepends=True):
            linea_actual[0] = linea
            if _CERCA.match(linea):
                dentro = not dentro
            if _CERCA.match(linea) or dentro or linea.lstrip().startswith("#"):
                salida.append(linea)
                previo += linea
                continue
            columnas = _columnas_de_la_tabla(linea, previo, columnas)
            # La partida primero: su `NN` entre comillas encajaría a medias en las otras.
            linea = _CITA_PARTIDA.sub(lambda m: enlace(m.group(1), m.group(2), m.group(0), m.string[:m.start()]),
                                      linea)
            linea = _DEPENDENCIA.sub(lambda m: "(%s %s)" % (m.group(1), enlace(
                m.group(2), m.group(3), m.group(3), m.string[:m.start()])), linea)
            linea = _CITA.sub(lambda m: enlace(m.group(1), m.group(2), m.group(0), m.string[:m.start()]), linea)
            salida.append(linea)
            previo += linea
        return "".join(salida), cambios[0]

    def reparar(self, texto, origen):
        """`(texto, cuántas)` con las citas enlazadas reapuntadas a donde vive la regla:
        un archivo que se mueve deja atrás todos los enlaces que lo citaban."""
        idx, cambios, salida, dentro = self.indice, [0], [], False

        def reemplazo(m):
            capitulo, id_, ruta = m.groups()
            esperado = idx.destino(origen, id_)
            if not esperado or ruta == esperado or (not ruta.split("#")[0] and idx.archivo_de(id_) == origen):
                return m.group(0)
            cambios[0] += 1
            return "[`%s`](%s)" % ("%s·%s" % (capitulo, id_) if capitulo else id_, esperado)

        for linea in texto.splitlines(keepends=True):
            if _CERCA.match(linea):
                dentro = not dentro
                salida.append(linea)
                continue
            salida.append(linea if dentro else _CITA_ENLAZADA.sub(reemplazo, linea))
        return "".join(salida), cambios[0]

    def aplicar(self, escribir=False):
        """`[(archivo, enlazadas, reparadas)]`. Sin `escribir` solo simula."""
        tocados = []
        for archivo in self.proyecto.recorrer_md(BASE):
            nuevo, n = self.enlazar(self.archivos.leer(archivo), archivo)
            nuevo, r = self.reparar(nuevo, archivo)
            if n or r:
                tocados.append((archivo, n, r))
                if escribir:
                    with open(archivo, "w", encoding="utf-8", newline="\n") as f:
                        f.write(nuevo)
        return tocados
