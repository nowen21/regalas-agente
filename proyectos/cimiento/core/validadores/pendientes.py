"""La numeración y la forma de los pendientes (`EP-004·HU-018`, `EP-023·HU-003`).

Un pendiente se numera por el orden en que conviene ejecutarlo, y su número
**no se reutiliza nunca**: los huecos son historia y los pendientes se citan
entre sí por número. Abrir uno con un número ya tomado rompe esas citas sin que
nadie se entere, porque los dos archivos existen y ninguno se pisa.

Dos formas conviven. La anterior, `pendientes/NN-slug.md` con `hecho/` para los
cerrados; y la nueva, una carpeta `NNN-slug/` con su `pendiente.md` y sus
análisis dentro de la carpeta `pendientes/` de lo que lo origina (una épica, una
HU o el resumen del día). El estado de la nueva no lo escribe nadie: se calcula.

`Pendientes` sabe leer las dos formas; `NumeracionDePendientes` es el validador.
"""
import os
import re

from ..comun import AVISO, FALLA, Hallazgo, Proyecto
from ..comun.archivos import Archivos
from .base import Validador

CARPETA = "pendientes"
CERRADOS = "hecho"
INDICE = "README.md"

# `07-x.md` es el 7: los ceros a la izquierda no cambian el número, y tenerlos
# como dos distintos dejaría pasar justo el choque que esto busca.
_NUMERADO = re.compile(r"^(\d+)-(.+)\.md$")

# Una fase se nombra `X-EP-NNN-HU-NNN-...` (`02·F12`, punto 6).
_NOMBRE_FASE = re.compile(r"\b([A-Z]-EP-\d{3}-HU-\d{3}-[\w\-]+)")

# `EP-004·HU-016` · Desde cuándo se exige que el cerrado nombre su fase. Lo
# cerrado antes no se reabre, igual que `20·M10` hace con cualquier norma nueva.
CORTE = "2026-08-16"

# Lo que se cierra **sin construir nada**: una decisión, una medición que dio en
# cero, un duplicado. No tuvo fase, y exigirle una obligaría a inventarla.
_SIN_FASE = re.compile(
    r"(?i)cerrad[oa] por decisión|no hubo (?:que )?constru|"
    r"sin fase porque|no fue desarrollo|se cerró sin construir")

# `02·F24` · El pendiente que nace de un proyecto lo nombra. Se busca la fila de
# la ficha y no el texto suelto: un pendiente puede nombrar tres proyectos en su
# prosa y no venir de ninguno.
_DE_UN_PROYECTO = re.compile(r"(?im)^\|\s*\*\*Proyecto de origen\*\*\s*\|(.*?)\|\s*$")

# Donde puede vivir una carpeta `pendientes/` de la forma nueva.
DONDE = (("documentacion", "epicas"), ("historico-chat", "resumenes"))
INDICE_NUEVO = os.path.join("documentacion", "pendientes.md")

_CARPETA_PENDIENTE = re.compile(r"^(\d+)-[^.]+$")
_ANALISIS = re.compile(r"^analisis-(\d+)\.md$")
_APROBADO = re.compile(r"^> \*\*Aprobado\*\*", re.M)
COMPROBADO = re.compile(r"^\*\*Comprobado:\*\*\s*\d{4}-\d{2}-\d{2}\s*$", re.M)
_DE_DONDE = re.compile(r"^\|\s*\*\*De dónde sale\*\*\s*\|(.+?)\|\s*$", re.M)
_ENLACE = re.compile(r"\]\(([^)#\s]+)")
# «HU-001» o «HU 1»: el análisis 1 del pendiente 103 escribe la segunda.
_HU_EN_TEXTO = re.compile(r"EP-0*(\d+)\D{1,40}?HU[- ]0*(\d+)")
_FILA = re.compile(r"^\| *\d+ *\|(.*)\|\s*$", re.M)
_PARTES = (("De dónde sale", re.compile(r"^\|\s*\*\*De dónde sale\*\*\s*\|", re.M)),
           ("El problema", re.compile(r"^## El problema\s*$", re.M)),
           ("Por qué importa", re.compile(r"^## Por qué importa\s*$", re.M)))
_SE_RESUELVE = re.compile(r"^Se resuelve en el \[[^\]]*\]\(([^)#\s]+)\)", re.M)


def _destino(enlace, desde):
    """La ruta a la que lleva un enlace relativo escrito en `desde`."""
    return os.path.normpath(os.path.join(os.path.dirname(desde), enlace.replace("/", os.sep)))


def _desde_el_estandar(ruta):
    """Cómo se nombra una ruta en un mensaje: desde la carpeta del estándar si
    queda adentro, completa si no."""
    estandar = Proyecto.estandar()
    return Proyecto(estandar).mostrar(ruta) if estandar else os.path.abspath(ruta).replace("\\", "/")


def _archivos_de(carpeta):
    """Los `.md` de la carpeta, sin su índice."""
    if not os.path.isdir(carpeta):
        return []
    return sorted(n for n in os.listdir(carpeta)
                  if n.endswith(".md") and n != INDICE and os.path.isfile(os.path.join(carpeta, n)))


class Pendientes:
    """Los pendientes de un proyecto, en sus dos formas. Solo lee."""

    def __init__(self, proyecto, archivos=None):
        self.proyecto = proyecto if isinstance(proyecto, Proyecto) else Proyecto(proyecto)
        self.archivos = archivos or Archivos()

    def _leer(self, ruta):
        return self.archivos.leer(ruta)

    @property
    def carpeta(self):
        return os.path.join(self.proyecto.raiz, CARPETA)

    # -- la forma anterior -------------------------------------------------

    def numerados(self):
        """`{numero: [nombres]}` de los archivos numerados de `pendientes/` y `hecho/`."""
        encontrados = {}
        for carpeta in (self.carpeta, os.path.join(self.carpeta, CERRADOS)):
            for nombre in _archivos_de(carpeta):
                m = _NUMERADO.match(nombre)
                if m:
                    encontrados.setdefault(int(m.group(1)), []).append(nombre)
        return encontrados

    def numeros_del_indice(self):
        """Los números que el índice registra, **incluidos los cerrados**.

        Al cerrarse, el archivo pasa a `hecho/` y pierde el número; lo que lo
        conserva es la fila tachada del índice, `~~02~~`.
        """
        indice = self._leer(os.path.join(self.carpeta, INDICE))
        return {int(n) for n in re.findall(r"^\|\s*~*(\d+)~*\s*\|", indice, re.M)}

    def tomados(self):
        """Todos los números que **no se pueden reutilizar**."""
        return set(self.numerados()) | self.numeros_del_indice() | set(self.numeros_nuevos())

    def sin_numero(self):
        """Los `.md` de `pendientes/` que no empiezan por un número."""
        return [n for n in _archivos_de(self.carpeta) if not _NUMERADO.match(n)]

    def proximo_libre(self):
        """El siguiente al mayor, no el primer hueco: entregar un hueco haría que
        «el 02» apuntara a dos cosas distintas según cuándo se leyera."""
        ocupados = self.tomados()
        return max(ocupados) + 1 if ocupados else 1

    def linea_proximo(self):
        """La línea que dice el próximo número libre (`CA-01`)."""
        ocupados = self.tomados()
        abiertos = len(self.numerados())
        return ("Pendientes: %d con archivo · %d números tomados · el próximo libre es el %02d (HU-018)"
                % (abiertos, len(ocupados), self.proximo_libre()))

    def sin_proyecto_de_origen(self):
        """`[(nombre, motivo)]` de los que dicen venir de un proyecto sin decir de cuál."""
        salida = []
        for nombre in _archivos_de(self.carpeta):
            m = _DE_UN_PROYECTO.search(self._leer(os.path.join(self.carpeta, nombre)))
            if not m:
                continue                    # no declara origen: no es de esta regla
            valor = m.group(1).strip().strip("*` ")
            if not valor or ("«" in valor and "»" in valor):
                salida.append((nombre, "la casilla está vacía"))
        return salida

    @staticmethod
    def fecha_de_cierre(texto):
        """La fecha que el propio pendiente declara al cerrarse, o `""`."""
        m = re.search(r"(?i)\*\*hecho\*\*[^\n]*?(\d{4}-\d{2}-\d{2})", texto)
        if m:
            return m.group(1)
        m = re.search(r"(?i)cerrad[oa][^\n]*?(\d{4}-\d{2}-\d{2})", texto)
        return m.group(1) if m else ""

    def _existe_la_fase(self, nombre):
        for _actual, carpetas, _ in os.walk(os.path.join(self.proyecto.raiz, "documentacion", "epicas")):
            if nombre in carpetas:
                return True
        return False

    def cerrado_declara_su_fase(self):
        """`EP-004·HU-016` · Un pendiente cerrado dice en qué fase se hizo.

        **Aviso, no falla**: que falte la fila corta la trazabilidad, no rompe
        nada. **Sin fecha declarada se deja pasar**: los viejos no la declaran,
        y exigirles la fase sería aplicar hacia atrás una norma nueva.
        """
        carpeta = os.path.join(self.carpeta, "hecho")
        if not os.path.isdir(carpeta):
            return []
        hallazgos = []
        for nombre in sorted(os.listdir(carpeta)):
            if not nombre.lower().endswith(".md") or nombre.upper() == "README.MD":
                continue
            ruta = os.path.join(carpeta, nombre)
            texto = self._leer(ruta)
            fecha = self.fecha_de_cierre(texto)
            if not fecha or fecha < CORTE or _SIN_FASE.search(texto):
                continue
            fases = _NOMBRE_FASE.findall(texto)
            if not fases:
                hallazgos.append(Hallazgo(AVISO, ruta, 0, "no dice en qué fase se hizo — un pendiente cerrado "
                                                          "sin su fase corta la trazabilidad hacia abajo "
                                                          "(EP-004·HU-016)"))
                continue
            hallazgos += [Hallazgo(AVISO, ruta, 0, "nombra la fase `%s`, que no existe en `documentacion/epicas/` "
                                                   "— o se renombró, o nunca estuvo" % fase)
                          for fase in sorted(set(fases)) if not self._existe_la_fase(fase)]
        return hallazgos

    # -- la forma nueva ----------------------------------------------------

    def carpetas(self):
        """Las carpetas de pendiente de la forma nueva: `[ruta absoluta]`."""
        salida = []
        for partes in DONDE:
            for actual, subcarpetas, archivos in os.walk(os.path.join(self.proyecto.raiz, *partes)):
                subcarpetas[:] = [s for s in subcarpetas if not s.startswith(".")]
                if "pendiente.md" in archivos and _CARPETA_PENDIENTE.match(os.path.basename(actual)):
                    salida.append(actual)
        return sorted(salida)

    def numeros_nuevos(self):
        """`{numero: [carpetas]}` de los pendientes de la forma nueva."""
        salida = {}
        for carpeta in self.carpetas():
            salida.setdefault(int(_CARPETA_PENDIENTE.match(os.path.basename(carpeta)).group(1)), []).append(carpeta)
        return salida

    def forma_nueva(self):
        """`CA-03` · El pendiente trae sus tres partes y vive en una carpeta `pendientes/`."""
        hallazgos = []
        for carpeta in self.carpetas():
            ruta = os.path.join(carpeta, "pendiente.md")
            texto = self._leer(ruta)
            faltan = [nombre for nombre, patron in _PARTES if not patron.search(texto)]
            if faltan:
                hallazgos.append(Hallazgo(FALLA, ruta, 0, "le falta " + ", ".join("«%s»" % f for f in faltan)
                                          + " — un pendiente trae de dónde sale, el problema y por qué "
                                            "importa (EP-023·HU-003)"))
            if os.path.basename(os.path.dirname(carpeta)) != CARPETA:
                hallazgos.append(Hallazgo(AVISO, carpeta, 0, "no está dentro de una carpeta `pendientes/` de lo "
                                                             "que lo origina (EP-023·HU-003)"))
        return hallazgos

    def padre(self, carpeta):
        """El pendiente que enlaza su «De dónde sale», si es otro pendiente: su carpeta, o `""`."""
        ruta = os.path.join(carpeta, "pendiente.md")
        m = _DE_DONDE.search(self._leer(ruta))
        if not m:
            return ""
        estandar = Proyecto.estandar()
        estandar = os.path.normcase(os.path.abspath(estandar)) + os.sep if estandar else None
        en_el_estandar = bool(estandar) and os.path.normcase(os.path.abspath(carpeta)).startswith(estandar)
        for enlace in _ENLACE.findall(m.group(1)):
            destino = _destino(enlace, ruta)
            if os.path.basename(destino) == "pendiente.md":
                destino = os.path.dirname(destino)
            # El pendiente que un proyecto reporta al estándar enlaza su
            # seguimiento en el proyecto: ese seguimiento no es su padre
            # (análisis 1 del pendiente 110, acuerdo 5).
            if en_el_estandar and not os.path.normcase(os.path.abspath(destino)).startswith(estandar):
                continue
            if os.path.isfile(os.path.join(destino, "pendiente.md")) and \
                    os.path.normcase(destino) != os.path.normcase(carpeta):
                return destino
        return ""

    def resuelto_en(self, carpeta):
        """La carpeta del pendiente en cuyo análisis se resuelve este, o `""`: el
        que otro reúne toma su estado (análisis 1 del pendiente 110, acuerdo 4)."""
        ruta = os.path.join(carpeta, "pendiente.md")
        m = _SE_RESUELVE.search(self._leer(ruta))
        if not m:
            return ""
        destino = _destino(m.group(1), ruta)
        destino = os.path.dirname(destino) if destino.endswith(".md") else destino
        return destino if os.path.isfile(os.path.join(destino, "pendiente.md")) else ""

    @staticmethod
    def analisis_de(carpeta):
        """Los `analisis-N.md` de la carpeta, en orden."""
        nombres = [n for n in os.listdir(carpeta) if _ANALISIS.match(n)] if os.path.isdir(carpeta) else []
        return [os.path.join(carpeta, n) for n in sorted(nombres, key=lambda n: int(_ANALISIS.match(n).group(1)))]

    def _hu_terminada(self, ruta):
        return bool(re.search(r"^\|\s*\*\*Estado\*\*\s*\|\s*Terminada", self._leer(ruta), re.M))

    def _hu_por_numero(self, epica, hu):
        base = os.path.join(self.proyecto.raiz, "documentacion", "epicas")
        if not os.path.isdir(base):
            return ""
        for e in os.listdir(base):
            if re.match(r"EP-0*%d-" % epica, e):
                for h in os.listdir(os.path.join(base, e)):
                    if re.match(r"HU-0*%d-" % hu, h):
                        ruta = os.path.join(base, e, h, h + ".md")
                        if os.path.isfile(ruta):
                            return ruta
        return ""

    def _epica_terminada(self, analisis):
        """Si la épica que contiene la carpeta del pendiente está terminada."""
        carpeta = os.path.dirname(os.path.abspath(analisis))
        while carpeta and os.path.dirname(carpeta) != carpeta:
            if re.match(r"EP-\d+", os.path.basename(carpeta)):
                return self._hu_terminada(os.path.join(carpeta, "epica.md"))
            carpeta = os.path.dirname(carpeta)
        return False

    def _fila_cumplida(self, celda, analisis):
        """Si el trabajo de una fila de «Lo que se tiene que hacer» ya está hecho."""
        if re.search(r"(?i)este análisis", celda):
            return True
        hus = [_destino(e, analisis) for e in _ENLACE.findall(celda)]
        hus = [h for h in hus if re.match(r"HU-\d+", os.path.basename(h)) and h.endswith(".md")]
        if not hus:
            hus = [r for r in (self._hu_por_numero(int(e), int(h)) for e, h in _HU_EN_TEXTO.findall(celda)) if r]
        if not hus:
            # La fila que no nombra una HU es trabajo de la épica: se cumple
            # cuando la épica donde vive el pendiente terminó.
            return self._epica_terminada(analisis)
        return all(self._hu_terminada(h) for h in hus)

    def estado(self, carpeta, _vistos=None):
        """`CA-04` · «abierto» o «cerrado», calculado: nadie lo escribe.

        Cerrado cuando tiene un análisis aprobado y cada fila de su «Lo que se
        tiene que hacer» está cumplida. El de seguimiento cierra cuando su padre
        cerró y su `aviso-resuelto.md` dice «Comprobado» con fecha.
        """
        vistos = _vistos or set()
        clave = os.path.normcase(os.path.abspath(carpeta))
        if clave in vistos:
            return "abierto"
        vistos.add(clave)
        reunido = self.resuelto_en(carpeta)
        if reunido:
            return self.estado(reunido, vistos)
        arriba = self.padre(carpeta)
        if arriba:
            if self.estado(arriba, vistos) != "cerrado":
                return "abierto"
            return "cerrado" if COMPROBADO.search(self._leer(os.path.join(carpeta, "aviso-resuelto.md"))) else "abierto"
        aprobados = [a for a in self.analisis_de(carpeta) if _APROBADO.search(self._leer(a))]
        if not aprobados:
            return "abierto"
        for analisis in aprobados:
            texto = self._leer(analisis)
            m = re.search(r"^## Lo que se tiene que hacer.*$", texto, re.M)
            if not m:
                continue
            fin = re.search(r"^## ", texto[m.end():], re.M)
            seccion = texto[m.end():m.end() + fin.start()] if fin else texto[m.end():]
            for resto in _FILA.findall(seccion):
                if not self._fila_cumplida(resto.split("|")[-1], analisis):
                    return "abierto"
        return "cerrado"

    # -- el índice ---------------------------------------------------------

    def _titulo(self, ruta):
        primera = self._leer(ruta).split("\n", 1)[0]
        return re.sub(r"^#\s*(Pendiente\s*[:·]\s*)?", "", primera).strip()

    def indice(self):
        """`CA-08` · El índice de todos los pendientes, armado por el programa."""
        raiz = self.proyecto.raiz
        destino = os.path.dirname(os.path.join(raiz, INDICE_NUEVO))
        filas = []
        for carpeta in self.carpetas():
            numero = int(_CARPETA_PENDIENTE.match(os.path.basename(carpeta)).group(1))
            ruta = os.path.join(carpeta, "pendiente.md")
            enlace = os.path.relpath(ruta, destino).replace(os.sep, "/")
            donde = os.path.relpath(carpeta, raiz).replace(os.sep, "/")
            filas.append((numero, "[%s](%s)" % (self._titulo(ruta), enlace), "`%s`" % donde, self.estado(carpeta)))
        nuevos = set(self.numeros_nuevos())
        for numero, nombres in self.numerados().items():
            if numero in nuevos:
                continue                    # pasó a la forma nueva: cuenta allá
            for nombre in nombres:
                sub = "" if os.path.isfile(os.path.join(self.carpeta, nombre)) else CERRADOS + "/"
                ruta = os.path.join(self.carpeta, sub + nombre)
                cerrado = sub or re.search(r"(?i)\*\*Estado:\*\*\s*\**hecho", self._leer(ruta))
                enlace = os.path.relpath(ruta, destino).replace(os.sep, "/")
                filas.append((numero, "[%s](%s)" % (self._titulo(ruta), enlace),
                              "`%s/%s`, forma anterior" % (CARPETA, sub), "cerrado" if cerrado else "abierto"))
        # Los cerrados de la forma anterior que perdieron su número al moverse
        # a `hecho/` entran igual, porque el índice es de todos.
        sin_numero_cerrados = []
        for nombre in _archivos_de(os.path.join(self.carpeta, CERRADOS)):
            if not _NUMERADO.match(nombre):
                ruta = os.path.join(self.carpeta, CERRADOS, nombre)
                enlace = os.path.relpath(ruta, destino).replace(os.sep, "/")
                sin_numero_cerrados.append("| — | [%s](%s) | `%s/%s/`, forma anterior | cerrado |"
                                           % (self._titulo(ruta), enlace, CARPETA, CERRADOS))
        lineas = ["# Pendientes", "",
                  "> Lo arma `python validadores/validar.py pendientes --indice`; no se edita a mano. "
                  "El estado se calcula: un pendiente cierra cuando se cumple el plan que salió de él. "
                  "Los de la forma anterior dicen el estado que tenían escrito; los cerrados que perdieron "
                  "su número al pasar a `pendientes/hecho/` van al final, sin número.", "",
                  "| # | Pendiente | Dónde vive | Estado |", "|---|---|---|---|"]
        lineas += ["| %d | %s | %s | %s |" % f for f in sorted(filas)]
        lineas += sorted(sin_numero_cerrados)
        return "\n".join(lineas) + "\n"

    def escribir_indice(self):
        """Escribe el índice en `documentacion/pendientes.md` y devuelve su ruta."""
        ruta = os.path.join(self.proyecto.raiz, INDICE_NUEVO)
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        texto = self.indice()
        with open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)
        return ruta


class NumeracionDePendientes(Validador):
    """Ningún número repetido, la carpeta y su índice de acuerdo, el origen
    nombrado y el cerrado con su fase."""

    nombre = "pendientes"
    regla = "02·F24"
    descripcion = "numeración de los pendientes y cruce con su índice"

    def __init__(self, proyecto, archivos=None):
        super().__init__(proyecto, archivos)
        self.pendientes = Pendientes(self.proyecto, self.archivos)

    def validar(self):
        p = self.pendientes
        # `EP-023·HU-003` · `pendientes/` es historia: el proyecto nuevo no la tiene.
        hallazgos = p.forma_nueva()
        hallazgos += self._repetidos()
        if not os.path.isdir(p.carpeta):
            return hallazgos
        # Un nombre que no se puede interpretar se reporta y no detiene.
        hallazgos += [Hallazgo(AVISO, os.path.join(p.carpeta, nombre), 0,
                               "no empieza por un número, así que no entra en la numeración (HU-018)")
                      for nombre in p.sin_numero()]
        hallazgos += self._contra_el_indice()
        hallazgos += [Hallazgo(FALLA, os.path.join(p.carpeta, nombre), 0,
                               "declara «Proyecto de origen» y %s — sin el nombre nadie sabe a quién avisarle "
                               "al cerrar, y ese proyecto se queda esperando para siempre (02·F24)" % motivo)
                      for nombre, motivo in p.sin_proyecto_de_origen()]
        # La historia a la que baja el abierto ya no se escribe en el
        # pendiente: la decide su análisis (`EP-023·HU-003`).
        return hallazgos + p.cerrado_declara_su_fase()

    def _repetidos(self):
        """`CA-02` · El número repetido, en las dos formas. El que pasó a la forma
        nueva deja su archivo viejo con el mismo número y nombre: es el mismo."""
        todos = self.pendientes.numerados()
        for numero, rutas in self.pendientes.numeros_nuevos().items():
            for ruta in rutas:
                if os.path.basename(ruta) + ".md" in todos.get(numero, []):
                    continue
                todos.setdefault(numero, []).append(_desde_el_estandar(ruta))
        return [Hallazgo(FALLA, self.pendientes.carpeta, 0,
                         "el número %d está tomado por %d pendientes: " % (numero, len(nombres))
                         + ", ".join("`%s`" % n for n in nombres) + " — un número no se reutiliza (HU-018)")
                for numero, nombres in sorted(todos.items()) if len(nombres) > 1]

    def _contra_el_indice(self):
        """`CA-03` · La carpeta y el índice, en los dos sentidos."""
        carpeta = self.pendientes.carpeta
        indice = self.archivos.leer(os.path.join(carpeta, INDICE))
        if not indice:
            return []
        propios = {e for e in re.findall(r"\]\(([^)]+\.md)\)", indice) if "/" not in e and e != INDICE}
        hallazgos = [Hallazgo(AVISO, os.path.join(carpeta, nombre), 0,
                              "no aparece en `%s/%s` (HU-018)" % (CARPETA, INDICE))
                     for nombre in _archivos_de(carpeta) if nombre not in propios]
        return hallazgos + [Hallazgo(AVISO, os.path.join(carpeta, INDICE), 0,
                                     "el índice enlaza `%s`, que no está en la carpeta (HU-018)" % nombre)
                            for nombre in sorted(propios - set(_archivos_de(carpeta)))]
