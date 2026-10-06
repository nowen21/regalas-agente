"""`09·12` · Crea el esqueleto de una fase, de una historia o de un pendiente.

**A mano es donde se cometen los errores** que `fases` y `trazabilidad` detectan
después: el consecutivo repetido, el nombre que no sigue el molde, el enlace que
falta en uno de los dos lados. La estructura se corrige en vez de nacer bien.

**Genera el esqueleto y nada de contenido**, que es la advertencia más
importante del propio pendiente: *un generador que además rellena texto produce
documentos que pasan el validador sin decir nada, que es la peor combinación
posible.* Por eso los marcadores `«…»` de las plantillas **se dejan intactos**:
solo se sustituye lo estructural (identificadores, rutas, enlaces), que es lo
que un programa puede saber y una persona escribe mal.

**El consecutivo se calcula leyendo lo que hay**, no se pide. **Tres alturas de
la cadena, un solo programa** (`EP-007 · HU-003`, fase B): la fase; la historia,
con su fila en la épica y en el README de la épica; y el pendiente. **Los enlaces
se trasladan al copiar** (`EP-004 · HU-005`, fase C): la plantilla enlaza la raíz
desde su propia carpeta, y la fase vive cinco niveles más abajo.

**Se corre solo, no por `validar.py`**: `validar.py` comprueba, esto escribe.

    python andamio.py EP-001-… HU-003-… descripcion-de-la-fase
    python andamio.py hu EP-001-… descripcion-de-la-historia
    python andamio.py pendiente descripcion [--hu EP-001-…/HU-003-…]
    python andamio.py quitar carpeta        (la contraria: `EP-025·HU-020`)
"""
import argparse
import datetime
import os
import re
import shutil
import sys

if __name__ == "__main__" and not __package__:
    # Corrido por su ruta: se arma el paquete para que las importaciones
    # relativas encuentren a `core`.
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    __package__ = "core.herramientas"

from ..comun import Archivos, Proyecto  # noqa: E402
from ..comun.consola import preparar_salida  # noqa: E402
from ..validadores.pendientes import Pendientes  # noqa: E402

CARPETA = os.path.join("documentacion", "epicas")
PENDIENTES = "pendientes"

# Los cinco documentos de una fase (`02·F12.13`) y la plantilla de cada uno.
DOCUMENTOS = [
    ("plan_trabajo.md", os.path.join("plantillas", "ciclo-vida-proyectos", "07-plan-trabajo.md")),
    ("plan_pruebas.md", os.path.join("plantillas", "ciclo-vida-proyectos", "08-plan-pruebas.md")),
    ("resultado_pruebas.md", os.path.join("plantillas", "ciclo-vida-proyectos", "09-resultado-pruebas.md")),
    ("estado-fase.md", os.path.join("plantillas", "ciclo-vida-proyectos", "10-estado-fase.md")),
    ("funcionalidad_implementada.md",
     os.path.join("plantillas", "ciclo-vida-proyectos", "11-funcionalidad-implementada.md")),
]
PLANTILLA_HU = os.path.join("plantillas", "ciclo-vida-proyectos", "04-HU.md")
PLANTILLA_PENDIENTE = os.path.join("plantillas", "pendiente.md")
# Donde queda lo que se quita cuando ya tenía trabajo (`EP-025·HU-020`).
ARCHIVO = "_archivo"

_CONSECUTIVO = re.compile(r"^([A-Z]{1,3})(?:-[A-Z]{1,3})?-EP-")
_HU = re.compile(r"^HU-(\d+)-")
_TITULO = re.compile(r"(?m)^#\s+(.+?)\s*$")
MARCADOR_RAIZ = "«RUTA-ESTANDAR»"


def _mostrar(ruta):
    return Proyecto(Proyecto.estandar()).mostrar(ruta)


class Andamio:
    """Levanta la estructura de la cadena en un proyecto. Sin `escribir`, simula."""

    def __init__(self, raiz, archivos=None):
        self.raiz = os.path.abspath(raiz)
        self.archivos = archivos or Archivos()

    def _leer(self, ruta):
        return self.archivos.leer(ruta)

    # ── los números ───────────────────────────────────────────────────────

    @staticmethod
    def letras(n):
        """`1` es `A`, `26` es `Z`, `27` es `AA`: el consecutivo de `02·F12.5`."""
        salida = ""
        while n > 0:
            n, resto = divmod(n - 1, 26)
            salida = chr(ord("A") + resto) + salida
        return salida

    @classmethod
    def siguiente_consecutivo(cls, carpeta_hu):
        """La letra que le toca a la próxima fase de esa HU.

        **Se lee lo que hay en vez de contar cuántas hay**: si existen `A` y `C`
        porque la `B` se renombró, contar daría `C` y pisaría una fase viva.
        """
        usadas = set()
        if os.path.isdir(carpeta_hu):
            for nombre in os.listdir(carpeta_hu):
                m = _CONSECUTIVO.match(nombre)
                if m and os.path.isdir(os.path.join(carpeta_hu, nombre)):
                    usadas.add(m.group(1))
        n = 1
        while cls.letras(n) in usadas:
            n += 1
        return cls.letras(n)

    @staticmethod
    def siguiente_hu(carpeta_epica):
        """`HU-004` si existen la 1 y la 3: el siguiente al mayor, leído del disco.

        **El siguiente al mayor, no el primer hueco**, como los pendientes: una
        historia se cita por número desde fases, pendientes y commits, y un hueco
        puede ser una historia que se movió. Las fases sí toman el primer hueco,
        porque su letra solo vive dentro de su historia.
        """
        usadas = set()
        # Lo archivado sigue citado por su número: no se reusa (`EP-025·HU-020`).
        for carpeta in (carpeta_epica, os.path.join(carpeta_epica, ARCHIVO)):
            if os.path.isdir(carpeta):
                for nombre in os.listdir(carpeta):
                    m = _HU.match(nombre)
                    if m and os.path.isdir(os.path.join(carpeta, nombre)):
                        usadas.add(int(m.group(1)))
        return "HU-%03d" % (max(usadas) + 1 if usadas else 1)

    # ── el texto ──────────────────────────────────────────────────────────

    @staticmethod
    def sustituciones(consecutivo, epica, hu, descripcion, nombre_fase):
        """Solo lo **estructural**. Los `«…»` de contenido no se tocan."""
        return {"«CONSECUTIVO»": consecutivo, "«EPICA»": epica, "«HU»": hu,
                "«FASE»": nombre_fase, "«DESCRIPCION-FASE»": descripcion}

    @staticmethod
    def hacia(base, destino):
        """El enlace de `destino` a `base`: relativo, o absoluto si están en otra unidad."""
        try:
            return os.path.relpath(base, destino).replace("\\", "/")
        except ValueError:
            return os.path.abspath(base).replace("\\", "/")

    @classmethod
    def reenlazar(cls, texto, origen_plantilla, destino):
        """Traslada a la carpeta de destino los enlaces que la plantilla hace a la raíz.

        Las plantillas son del estándar, y sus enlaces a la raíz apuntan al estándar:
        desde un proyecto se arman hacia Cimiento, no hacia el proyecto, donde no
        existen (análisis 1 del pendiente 110, acuerdo 2). Solo se traslada el
        prefijo que **llega exactamente a la raíz**, y el marcador de su ruta.
        """
        estandar = Proyecto.estandar()
        hacia_estandar = cls.hacia(estandar, destino)
        desde_plantilla = os.path.relpath(
            estandar, os.path.dirname(os.path.abspath(origen_plantilla))).replace("\\", "/")
        patron = re.compile(r"\]\(" + re.escape(desde_plantilla) + r"/(?!\.\.)")
        texto = patron.sub("](" + hacia_estandar + "/", texto)
        return texto.replace(MARCADOR_RAIZ, hacia_estandar)

    @staticmethod
    def _escribir(ruta, texto, escribir):
        if not escribir:
            return
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)

    def agregar_fila(self, ruta, fila, despues_de, escribir):
        """Agrega `fila` al final de la primera tabla que sigue al encabezado `despues_de`.

        Si `despues_de` es None, al final de la última tabla del archivo. El número
        de columnas lo decide la cabecera real de esa tabla, no la plantilla.
        """
        texto = self._leer(ruta)
        inicio = 0
        if despues_de:
            m = re.search(r"(?m)^" + re.escape(despues_de) + r".*$", texto)
            if not m:
                raise ValueError("no está «%s» en %s" % (despues_de, _mostrar(ruta)))
            inicio = m.end()
        tabla = re.compile(r"(?m)^\|.*\n(?:\|.*\n?)*")
        bloques = list(tabla.finditer(texto, inicio))
        if not bloques and not despues_de and re.search(r"(?m)^- \[", texto):
            # Un índice escrito como lista, no como tabla: la fila entra con la
            # misma forma (análisis 1 del pendiente 110, acuerdo 2).
            celdas = [c.strip() for c in fila.strip().strip("|").split("|")]
            item = "- " + " — ".join(celdas)
            self._escribir(ruta, texto.rstrip("\n") + "\n" + item + "\n", escribir)
            return item
        if not bloques:
            raise ValueError("no hay tabla después de «%s» en %s" % (despues_de, _mostrar(ruta)))
        bloque = bloques[0] if despues_de else bloques[-1]
        columnas = bloque.group(0).splitlines()[0].count("|") - 1
        celdas = [c.strip() for c in fila.strip().strip("|").split("|")]
        while len(celdas) < columnas:
            celdas.append("«…»")
        fila_lista = "| " + " | ".join(celdas[:columnas]) + " |"
        nuevo = texto[:bloque.start()] + bloque.group(0).rstrip("\n") + "\n" + fila_lista + "\n" + texto[bloque.end():]
        self._escribir(ruta, nuevo, escribir)
        return fila_lista

    def titulo_de(self, ruta):
        m = _TITULO.search(self._leer(ruta))
        return m.group(1) if m else os.path.basename(ruta)

    # ── las tres alturas ──────────────────────────────────────────────────

    def crear(self, epica, hu, descripcion, escribir=False):
        """Crea la fase y devuelve `(ruta, [archivos])`. `epica` y `hu` van como los
        nombres de sus carpetas: `EP-001-…`, `HU-003-…`."""
        carpeta_hu = os.path.join(self.raiz, CARPETA, epica, hu)
        if not os.path.isdir(carpeta_hu):
            raise ValueError("no existe la HU: %s" % os.path.join(CARPETA, epica, hu))
        num_ep = re.match(r"^EP-(\d+)", epica)
        num_hu = re.match(r"^HU-(\d+)", hu)
        if not num_ep or not num_hu:
            raise ValueError("la épica o la HU no siguen el molde de `02·F12`")
        consecutivo = self.siguiente_consecutivo(carpeta_hu)
        nombre = "%s-EP-%s-HU-%s-%s" % (consecutivo, num_ep.group(1), num_hu.group(1), descripcion)
        destino = os.path.join(carpeta_hu, nombre)
        escritos = []
        for archivo, texto in self.textos_de_fase(epica, hu, consecutivo, descripcion, destino).items():
            escritos.append(archivo)
            self._escribir(os.path.join(destino, archivo), texto, escribir)
        return destino, escritos

    def textos_de_fase(self, epica, hu, consecutivo, descripcion, destino):
        """`{archivo: texto}` de los documentos que el andamio pone en una fase."""
        subs = self.sustituciones(consecutivo, epica, hu, descripcion, os.path.basename(destino))
        textos = {}
        for archivo, plantilla in DOCUMENTOS:
            origen = os.path.join(Proyecto.estandar(), plantilla)      # las plantillas son del estándar
            if not os.path.isfile(origen):
                continue
            texto = self._leer(origen)
            for viejo, nuevo in subs.items():
                texto = texto.replace(viejo, nuevo)
            textos[archivo] = self.reenlazar(texto, origen, destino)
        return textos

    @staticmethod
    def hu_pedida(carpeta_epica, numero):
        """`HU-016` si no existe ya una historia con ese número.

        Análisis 3 del pendiente 119, acuerdo 4: el análisis que aprueba las
        historias les da su número, y el andamio tiene que poder respetarlo. Sin
        esto nació una HU-011 que el análisis llamaba HU-016, y no había cómo
        quitarla.
        """
        hu_id = "HU-%03d" % int(numero)
        if any(os.path.isdir(c) and any(n.startswith(hu_id + "-") for n in os.listdir(c))
               for c in (carpeta_epica, os.path.join(carpeta_epica, ARCHIVO))):
            raise ValueError("ya existe la %s en %s" % (hu_id, os.path.basename(carpeta_epica)))
        return hu_id

    def crear_hu(self, epica, descripcion, escribir=False, numero=None):
        """Crea la historia con su README y sus dos filas en la épica. Devuelve
        `(ruta de la carpeta, [archivos escritos o tocados])`. Con `numero`, la
        historia toma ese número; sin él, el siguiente al mayor."""
        carpeta_epica = os.path.join(self.raiz, CARPETA, epica)
        epica_md = os.path.join(carpeta_epica, "epica.md")
        if not os.path.isfile(epica_md):
            raise ValueError("no existe la épica: %s" % os.path.join(CARPETA, epica))
        origen = os.path.join(Proyecto.estandar(), PLANTILLA_HU)      # las plantillas son del estándar
        if not os.path.isfile(origen):
            raise ValueError("falta la plantilla %s" % PLANTILLA_HU)
        hu_id = self.hu_pedida(carpeta_epica, numero) if numero else self.siguiente_hu(carpeta_epica)
        nombre = "%s-%s" % (hu_id, descripcion)
        destino = os.path.join(carpeta_epica, nombre)
        tocados = []
        for archivo, texto in self.textos_de_hu(epica_md, destino).items():
            self._escribir(os.path.join(destino, archivo), texto, escribir)
            tocados.append(os.path.join(destino, archivo))
        self.agregar_fila(epica_md, "| [%s](%s/%s.md) | «Título» | «Prioridad» | «Estimación» |"
                          % (hu_id, nombre, nombre), "## 9.", escribir)
        tocados.append(epica_md)
        readme_epica = os.path.join(carpeta_epica, "README.md")
        if os.path.isfile(readme_epica):
            self.agregar_fila(readme_epica, "| [%s/%s/%s/](%s/) | Historia de usuario: «…» |"
                              % (CARPETA.replace(os.sep, "/"), epica, nombre, nombre), None, escribir)
            tocados.append(readme_epica)
        return destino, tocados

    def textos_de_hu(self, epica_md, destino):
        """`{archivo: texto}` de lo que el andamio pone en la carpeta de una HU."""
        nombre = os.path.basename(destino)
        hu_id = "HU-" + _HU.match(nombre).group(1)
        origen = os.path.join(Proyecto.estandar(), PLANTILLA_HU)
        # Primero se trasladan los enlaces de la plantilla y después se ponen los
        # propios: al revés, el `../epica.md` recién puesto se trasladaría también.
        texto = self.reenlazar(self._leer(origen), origen, destino)
        texto = texto.replace("HU-000", hu_id)
        texto = texto.replace("«Épica padre»", "[%s](../epica.md)" % self.titulo_de(epica_md))
        readme = ("# %s\n\nContenido inmediato de esta carpeta.\n\n"
                  "| Qué | De qué se trata |\n|---|---|\n"
                  "| [%s.md](%s.md) | La historia de usuario: «…» |\n" % (nombre, nombre, nombre))
        return {nombre + ".md": texto, "README.md": readme}

    def texto_de_pendiente(self, carpeta):
        origen = os.path.join(Proyecto.estandar(), PLANTILLA_PENDIENTE)
        return self.reenlazar(self._leer(origen), origen, carpeta)

    def crear_pendiente(self, descripcion, hu_ref="", escribir=False, hoy=None):
        """Crea el pendiente en la forma nueva: una carpeta con su `pendiente.md`.

        `EP-023·HU-003` · Vive en la carpeta `pendientes/` de su dueño: la HU o la
        épica de `hu_ref`, o, sin ella, el resumen del día, hasta que su análisis
        decida a dónde va (análisis 1 del pendiente 103, conclusión 11). **Un
        `hu_ref` que no existe sigue siendo un error**: confundirlo con «sin dueño»
        dejaría el pendiente en el lugar equivocado por un error de tipeo.
        Devuelve `(ruta del pendiente.md, [archivos tocados])`.
        """
        if (hu_ref or "").strip():
            epica, hu = (hu_ref.replace("\\", "/").strip("/").split("/") + [""])[:2]
            if hu:
                dueno = os.path.join(self.raiz, CARPETA, epica, hu)
                if not os.path.isfile(os.path.join(dueno, hu + ".md")):
                    raise ValueError("no existe la historia: %s" % hu_ref)
            else:
                # El pendiente de una épica entera vive en su carpeta `pendientes/`
                # (análisis 1 del pendiente 110, acuerdo 2).
                dueno = os.path.join(self.raiz, CARPETA, epica)
                if not os.path.isfile(os.path.join(dueno, "epica.md")):
                    raise ValueError("no existe la épica: %s" % hu_ref)
        else:
            dia = (hoy or datetime.date.today()).isoformat()
            dueno = os.path.join(self.raiz, "historico-chat", "resumenes", dia)
        origen = os.path.join(Proyecto.estandar(), PLANTILLA_PENDIENTE)      # las plantillas son del estándar
        if not os.path.isfile(origen):
            raise ValueError("falta la plantilla %s" % PLANTILLA_PENDIENTE)
        numero = Pendientes(self.raiz, self.archivos).proximo_libre()
        carpeta = os.path.join(dueno, PENDIENTES, "%03d-%s" % (numero, descripcion))
        destino = os.path.join(carpeta, "pendiente.md")
        self._escribir(destino, self.texto_de_pendiente(carpeta), escribir)
        return destino, [destino]

    # ── la contraria: quitar (`EP-025·HU-020`) ────────────────────────────

    def _que_es(self, carpeta):
        """`("hu" | "fase" | "pendiente", padre)`, o error si no lo creó el andamio."""
        nombre, padre = os.path.basename(carpeta), os.path.dirname(carpeta)
        if os.path.basename(padre) == PENDIENTES and os.path.isfile(os.path.join(carpeta, "pendiente.md")):
            return "pendiente", padre
        if _CONSECUTIVO.match(nombre) and _HU.match(os.path.basename(padre)):
            return "fase", padre
        if _HU.match(nombre) and os.path.isfile(os.path.join(padre, "epica.md")):
            return "hu", padre
        raise ValueError("no es una HU, una fase ni un pendiente del andamio: %s" % _mostrar(carpeta))

    def _esperado(self, tipo, carpeta, padre):
        """Lo que el andamio crearía hoy en `carpeta`, archivo por archivo."""
        if tipo == "pendiente":
            return {"pendiente.md": self.texto_de_pendiente(carpeta)}
        if tipo == "hu":
            return self.textos_de_hu(os.path.join(padre, "epica.md"), carpeta)
        m = re.match(r"^([A-Z]{1,3})-EP-\d+-HU-\d+-(.+)$", os.path.basename(carpeta))
        if not m:
            return {}
        epica = os.path.basename(os.path.dirname(padre))
        return self.textos_de_fase(epica, os.path.basename(padre), m.group(1), m.group(2), carpeta)

    def es_plantilla(self, tipo, carpeta, padre):
        """¿Lo que hay es idéntico a lo que el andamio crearía, y nada más?

        Se compara el texto entero y no los marcadores `«…»`: un marcador queda
        aunque se haya escrito mucho alrededor.
        """
        esperado = self._esperado(tipo, carpeta, padre)
        if not esperado or sorted(os.listdir(carpeta)) != sorted(esperado):
            return False
        return all(self._leer(os.path.join(carpeta, a)) == t for a, t in esperado.items())

    @staticmethod
    def _bajar_un_nivel(texto):
        """Los enlaces que suben (`../`) suben uno más: la carpeta quedó dentro de `_archivo/`."""
        return re.sub(r"\]\(\.\./", "](../../", texto)

    def quitar(self, carpeta, escribir=False):
        """Deshace lo que el andamio creó en `carpeta`. Devuelve `(qué hizo, [archivos tocados])`.

        Lo que creó junto se quita junto (análisis 3 del pendiente 119, acuerdo 4).
        Si sigue siendo la plantilla, se borra con sus filas. Si tiene trabajo, se
        archiva en `_archivo/` de su misma carpeta padre y la fila apunta ahí con
        «(archivada)»: nada se pierde y el número no se reusa. Una HU con fases
        no se quita: primero se quitan sus fases.
        """
        carpeta = os.path.abspath(carpeta)
        if not os.path.isdir(carpeta):
            raise ValueError("no existe: %s" % _mostrar(carpeta))
        tipo, padre = self._que_es(carpeta)
        nombre = os.path.basename(carpeta)
        if tipo == "hu" and any(_CONSECUTIVO.match(n) for n in os.listdir(carpeta)):
            raise ValueError("la %s tiene fases: primero se quitan sus fases" % nombre)
        plantilla = self.es_plantilla(tipo, carpeta, padre)
        archivada = os.path.join(padre, ARCHIVO, nombre)
        if not plantilla and os.path.exists(archivada):
            raise ValueError("ya hay una archivada con ese nombre: %s" % _mostrar(archivada))
        tocados = [carpeta]
        if tipo == "hu":
            filas = [(os.path.join(padre, "epica.md"), "](%s/%s.md)" % (nombre, nombre)),
                     (os.path.join(padre, "README.md"), "](%s/)" % nombre)]
            for archivo, marca in filas:
                if not os.path.isfile(archivo):
                    continue
                lineas = self._leer(archivo).split("\n")
                if plantilla:
                    nuevas = [l for l in lineas if marca not in l]
                else:
                    nueva_marca = "](%s/%s (archivada)" % (ARCHIVO, marca[2:])
                    nuevas = [l.replace(marca, nueva_marca, 1) for l in lineas]
                if nuevas != lineas:
                    tocados.append(archivo)
                    self._escribir(archivo, "\n".join(nuevas), escribir)
        if escribir:
            if plantilla:
                shutil.rmtree(carpeta)
            else:
                os.makedirs(os.path.dirname(archivada), exist_ok=True)
                shutil.move(carpeta, archivada)
                for raiz, _, archivos in os.walk(archivada):
                    for a in archivos:
                        if a.endswith(".md"):
                            ruta = os.path.join(raiz, a)
                            self._escribir(ruta, self._bajar_un_nivel(self._leer(ruta)), True)
        accion = "borrada: era la plantilla" if plantilla else "archivada en %s" % _mostrar(archivada)
        return "%s %s" % (tipo, accion), tocados


def main(argv=None):
    """`09·12` · el andamio se pide, no se ejecuta solo."""
    preparar_salida()                   # imprime «·» y «…»: sin esto, mojibake
    argv = list(sys.argv[1:] if argv is None else argv)
    modo = argv[0] if argv and argv[0] in ("hu", "pendiente", "quitar") else "fase"
    p = argparse.ArgumentParser(
        description="Crea el esqueleto de una fase, una historia o un pendiente. "
                    "No escribe contenido: los marcadores «…» quedan para llenarse.")
    if modo == "hu":
        p.add_argument("modo")
        p.add_argument("epica", help="carpeta de la épica, p. ej. EP-001-cuerpo-de-reglas")
        p.add_argument("descripcion", help="qué pide la historia, en minúsculas con guiones")
        p.add_argument("--numero", type=int, default=None,
                       help="el número que le dio el análisis; sin él, el siguiente al mayor")
    elif modo == "quitar":
        p.add_argument("modo")
        p.add_argument("carpeta", help="la carpeta de la HU, la fase o el pendiente que creó el andamio")
    elif modo == "pendiente":
        p.add_argument("modo")
        p.add_argument("descripcion", help="qué falta, en minúsculas con guiones")
        p.add_argument("--hu", default="",
                       help="EP-001-…/HU-003-…: la historia dueña del pendiente. Sin ella, "
                            "nace en el resumen del día (EP-023·HU-003)")
    else:
        p.add_argument("epica", help="carpeta de la épica, p. ej. EP-001-cuerpo-de-reglas")
        p.add_argument("hu", help="carpeta de la HU, p. ej. HU-003-nucleo")
        p.add_argument("descripcion", help="qué hace la fase, en minúsculas con guiones")
    p.add_argument("--raiz", default=Proyecto.estandar())
    p.add_argument("--aplicar", action="store_true", help="escribe de verdad; sin esto solo dice qué crearía")
    a = p.parse_args(argv)

    andamio = Andamio(a.raiz)
    if modo == "quitar":
        try:
            accion, tocados = andamio.quitar(os.path.join(a.raiz, a.carpeta), a.aplicar)
        except ValueError as e:
            print("No se quita: %s" % e)
            return 1
        print("%s  (%s)" % (accion, "hecho" if a.aplicar else "simulado; agrega --aplicar"))
        for e in tocados:
            print("  · %s" % _mostrar(e))
        return 0
    if modo == "hu":
        destino, tocados = andamio.crear_hu(a.epica, a.descripcion, a.aplicar, a.numero)
    elif modo == "pendiente":
        destino, tocados = andamio.crear_pendiente(a.descripcion, a.hu, a.aplicar)
    else:
        destino, tocados = andamio.crear(a.epica, a.hu, a.descripcion, a.aplicar)
    marca = "creada" if a.aplicar else "simulado; agrega --aplicar"
    print("%s  (%s)" % (_mostrar(destino), marca))
    for e in tocados:
        print("  · %s" % (e if modo == "fase" else _mostrar(e)))
    print("\nLos marcadores «…» quedan sin llenar a propósito: el andamio no escribe contenido.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
