"""Cierra un pendiente: lo mueve a `pendientes/hecho/` y arrastra sus citas.

**El problema que resuelve.** El backlog se cita a sí mismo todo el tiempo, y
también lo citan las fases, los resúmenes y el índice. Mover un archivo a
`hecho/` dejaba apuntando al vacío a todos ellos: 12 enlaces rotos al cerrar el
35 (2026-08-16) y 54 al cerrar el 53 (2026-08-17), repartidos en doce fases.

**Cómo lo resuelve.** No busca texto: resuelve cada enlace contra el disco y
compara rutas absolutas. Un enlace apunta al pendiente que se mueve o no apunta,
y eso no depende de cuántos `../` lleve delante. Después reescribe el destino
recalculando la ruta relativa desde el archivo que lo cita.

**Simula por omisión.** Sin `--aplicar` dice qué haría y no toca nada: mover
archivos y reescribir enlaces en decenas de documentos no debe pasar por
escribir mal un comando.

    python cerrar.py 53 --como ningun-validador-termina-en-silencio --fecha 2026-08-17
    python cerrar.py 53 --como ningun-validador-termina-en-silencio --fecha 2026-08-17 --aplicar

**Su contraria** (`02·F30`) lo devuelve de `hecho/`, con sus citas y su fila:

    python cerrar.py reabrir 53 --motivo "volvió a fallar" --fecha 2026-10-05 --aplicar
"""
import argparse
import os
import re
import shutil
import sys
from urllib.parse import unquote

if __name__ == "__main__" and not __package__:
    # Corrido por su ruta: se arma el paquete para que las importaciones
    # relativas encuentren a `core`.
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    __package__ = "core.herramientas"

from ..comun import Archivos, Markdown, Proyecto  # noqa: E402
from ..comun.consola import preparar_salida  # noqa: E402
from ..comun.proyecto import EXCLUIDAS  # noqa: E402
from ..validadores.enlaces import ReparadorDeEnlaces  # noqa: E402

PENDIENTES = "pendientes"
HECHO = "hecho"
CARPETA_AVISOS = "pendientes"

# La fila del índice, antes y después de cerrar (`EP-005 · HU-003`, fase C).
# `mover()` ya deja el enlace apuntando a `hecho/`; lo que quedaba a mano era
# la forma: el número tachado, la prioridad vacía y la marca de hecho.
_FILA_ABIERTA = re.compile(
    r"(?m)^\|\s*(?P<num>\d+)\s*\|\s*(?P<p>[^|]*)\|\s*\[(?P<titulo>[^\]]+)\]\((?P<destino>hecho/[^)]+)\)\s*\|(?P<resto>.*)$")

# La fila ya hecha, para reabrirla (`EP-025·HU-022`): el destino puede ser
# `hecho/x.md` o, después de mover, la ruta nueva.
_FILA_HECHA = re.compile(
    r"(?m)^\|\s*~~(?P<num>\d+)~~\s*\|\s*(?P<p>[^|]*)\|\s*\*\*hecho\*\*\s*→\s*"
    r"\[(?P<titulo>[^\]]+)\]\((?P<destino>[^)]+)\)\s*\|(?P<resto>.*)$")
_ESTADO_HECHO = re.compile(r"(?i)(\*\*Estado:\*\*\s*)\**hecho\**")

_ORIGEN = re.compile(r"(?im)^\|\s*\*\*Proyecto de origen\*\*\s*\|(.*?)\|\s*$")
_A_QUIEN = re.compile(r"(?im)^\|\s*\*\*A qui[eé]n avisar al cerrar\*\*\s*\|(.*?)\|\s*$")
_TODOS = re.compile(r"(?i)todos")

_PLANTILLA_AVISO = """# Aviso · El estándar corrigió lo que este proyecto reportó

**Recibido el {fecha}.** Lo escribió `validadores/cerrar.py` al cerrar el pendiente del estándar. No se edita a mano.

| | |
|---|---|
| **Qué se corrigió** | {titulo} |
| **Dónde quedó** | `{destino}` del estándar |
| **Versión que lo trae** | {version} |

## Qué hacer con esto

1. **Comprobarlo acá.** El pendiente de seguimiento de este proyecto dice con qué se verifica. Cerrar sin comprobar es dar por buena una promesa.
2. **Correr el instalador**, si la corrección viene en piezas que este proyecto hereda.
3. **Cerrar el pendiente de seguimiento** — y solo entonces.

> `02·F24`: el pendiente del proyecto queda abierto hasta que llega este aviso **y se comprueba**.
"""


def _mostrar(ruta):
    return Proyecto(Proyecto.estandar()).mostrar(ruta)


def _escribir(ruta, texto):
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


class CerradorDePendientes:
    """Mueve un pendiente a `hecho/` sin romper lo que lo cita ni lo que él cita."""

    def __init__(self, raiz, archivos=None):
        self.raiz = os.path.abspath(raiz)
        self.archivos = archivos or Archivos()

    def _leer(self, ruta):
        return self.archivos.leer(ruta)

    def archivo_del_pendiente(self, numero):
        """El `.md` cuyo nombre empieza por ese número. Uno solo, o se avisa."""
        carpeta = os.path.join(self.raiz, PENDIENTES)
        prefijo = "%02d-" % int(numero)
        candidatos = [n for n in sorted(os.listdir(carpeta))
                      if n.startswith(prefijo) and n.lower().endswith(".md")]
        if not candidatos:
            sys.exit(f"no hay ningún pendiente {prefijo}* en {_mostrar(carpeta)}")
        if len(candidatos) > 1:
            sys.exit(f"hay {len(candidatos)} archivos con el número {numero}: " + ", ".join(candidatos))
        return os.path.join(carpeta, candidatos[0])

    # ── los enlaces ───────────────────────────────────────────────────────

    @staticmethod
    def resuelve_a(archivo, destino):
        """La ruta absoluta a la que apunta un enlace, o None si no es de disco.

        El `unquote` no es un detalle: un enlace a un archivo con espacios se
        escribe con `%20`, y sin decodificarlo la comparación falla siempre (punto
        1 del pendiente 33).
        """
        if destino.startswith(("http://", "https://", "mailto:", "#", "//")):
            return None
        ruta = unquote(destino.split("#", 1)[0])
        if not ruta:
            return None
        return os.path.normpath(os.path.join(os.path.dirname(archivo), ruta))

    def md_del_repositorio(self):
        proyecto = Proyecto(self.raiz)
        for carpeta, subcarpetas, archivos in os.walk(self.raiz):
            subcarpetas[:] = [s for s in subcarpetas if s not in EXCLUIDAS]
            if proyecto.es_excluida(os.path.relpath(carpeta, self.raiz).replace(os.sep, "/")):
                subcarpetas[:] = []
                continue
            for nombre in sorted(archivos):
                if nombre.lower().endswith(".md"):
                    yield os.path.join(carpeta, nombre)

    def citas_a(self, objetivo):
        """Todo enlace del repositorio que apunta a `objetivo`: `[(archivo, línea, destino escrito)]`."""
        objetivo = os.path.normpath(objetivo)
        encontrados = []
        for archivo in self.md_del_repositorio():
            for n, _texto, destino in Markdown.enlaces(self._leer(archivo)):
                if self.resuelve_a(archivo, destino) == objetivo:
                    encontrados.append((archivo, n, destino))
        return encontrados

    @staticmethod
    def nuevo_destino(desde, nuevo_absoluto, destino_viejo):
        """La ruta relativa al archivo movido, conservando el ancla si la había.

        **El espacio vuelve codificado** (pendiente 71): un espacio termina el
        destino en Markdown y el enlace dejaba de ser enlace. Se codifica solo el
        espacio, no los acentos, que el resto del repositorio escribe literales.
        """
        rel = os.path.relpath(nuevo_absoluto, os.path.dirname(desde)).replace("\\", "/")
        rel = rel.replace(" ", "%20")
        ancla = destino_viejo.split("#", 1)
        return rel + ("#" + ancla[1] if len(ancla) > 1 else "")

    @classmethod
    def reescribir_salientes(cls, texto, origen, destino):
        """Recalcula los enlaces **de dentro** del archivo que se mueve.

        Bajarlo un nivel deja cortos todos sus `../`: el 53 llegó a `hecho/` con
        ocho enlaces rotos hacia afuera. No solo hay que arrastrar a **quien cita**
        al archivo, sino lo que **el archivo cita**.
        """
        if os.path.normpath(os.path.dirname(origen)) == os.path.normpath(os.path.dirname(destino)):
            return texto, 0
        cambios = 0
        for _n, _t, d in Markdown.enlaces(texto):
            absoluto = cls.resuelve_a(origen, d)
            if absoluto is None or not os.path.exists(absoluto):
                continue                      # externo, ancla, o ya roto de antes
            nuevo = cls.nuevo_destino(destino, absoluto, d)
            if nuevo == d:
                continue
            cuenta = texto.count("](" + d + ")")
            if cuenta:
                texto = texto.replace("](" + d + ")", "](" + nuevo + ")")
                cambios += cuenta
        return texto, cambios

    # ── cerrar y mover ────────────────────────────────────────────────────

    def cerrar(self, numero, como, escribir=False):
        """Mueve el pendiente a `hecho/<como>.md`, reescribe lo que lo citaba y deja
        su fila del índice en la forma de hecho."""
        origen = self.archivo_del_pendiente(numero)
        nombre = como if como.lower().endswith(".md") else como + ".md"
        resultado = self.mover(origen, os.path.join(self.raiz, PENDIENTES, HECHO, nombre), escribir)
        self.fila_hecha(numero, nombre, escribir)
        return resultado

    def fila_hecha(self, numero, nombre_en_hecho, escribir):
        """`| 64 | **P2** | [t](hecho/x.md) | …` pasa a `| ~~64~~ | — | **hecho** → [t](hecho/x.md) | …`."""
        indice = os.path.join(self.raiz, PENDIENTES, "README.md")
        if not os.path.isfile(indice):
            return False
        texto = self._leer(indice)
        for m in _FILA_ABIERTA.finditer(texto):
            if int(m.group("num")) != int(numero) or not m.group("destino").endswith(nombre_en_hecho):
                continue
            nueva = "| ~~%s~~ | — | **hecho** → [%s](%s) |%s" % (
                m.group("num"), m.group("titulo"), m.group("destino"), m.group("resto"))
            if escribir:
                _escribir(indice, texto[:m.start()] + nueva + texto[m.end():])
            return True
        return False

    # ── la contraria: reabrir (`EP-025·HU-022`) ──────────────────────────

    def indice(self):
        return os.path.join(self.raiz, PENDIENTES, "README.md")

    def fila_cerrada(self, numero):
        """La fila hecha de ese número en el índice, o None."""
        if not os.path.isfile(self.indice()):
            return None
        for m in _FILA_HECHA.finditer(self._leer(self.indice())):
            if int(m.group("num")) == int(numero):
                return m
        return None

    def reabrir(self, numero, motivo, fecha, escribir=False):
        """Devuelve el pendiente de `hecho/` a `pendientes/`, con sus enlaces y su fila.

        Es la contraria de `cerrar` (`02·F30`). El nombre original no quedó
        guardado al cerrar, así que vuelve como `«número»-«nombre en hecho».md`.
        El aviso de vuelta que se mandó al cerrar no se deshace: ya pudo leerse.
        Devuelve `(origen, destino, [(archivo, cuántos enlaces)])`.
        """
        if not (motivo or "").strip():
            sys.exit("reabrir pide el motivo")
        fila = self.fila_cerrada(numero)
        if not fila:
            sys.exit(f"el pendiente {numero} no aparece cerrado en {_mostrar(self.indice())}")
        origen = self.resuelve_a(self.indice(), fila.group("destino"))
        if not origen or not os.path.isfile(origen):
            sys.exit(f"la fila del {numero} apunta a {fila.group('destino')}, que no existe")
        destino = os.path.join(self.raiz, PENDIENTES, "%02d-%s" % (int(numero), os.path.basename(origen)))
        resultado = self.mover(origen, destino, escribir)
        if escribir:
            self.fila_reabierta(numero)
            texto = _ESTADO_HECHO.sub(r"\g<1>reabierto", self._leer(destino))
            titulo, _, resto = texto.partition("\n")
            marca = "> **Reabierto** el %s: %s." % (fecha, motivo.strip().rstrip("."))
            _escribir(destino, titulo + "\n\n" + marca + "\n" + resto)
        return resultado

    def fila_reabierta(self, numero):
        """`| ~~64~~ | — | **hecho** → [t](64-x.md) | …` vuelve a `| 64 | — | [t](64-x.md) | …`."""
        m = self.fila_cerrada(numero)
        if not m:
            return False
        texto = self._leer(self.indice())
        nueva = "| %s | %s | [%s](%s) |%s" % (m.group("num"), m.group("p").strip() or "—", m.group("titulo"),
                                              m.group("destino"), m.group("resto"))
        _escribir(self.indice(), texto[:m.start()] + nueva + texto[m.end():])
        return True

    def mover(self, origen, destino, escribir=False):
        """Mueve un `.md` y arrastra todo lo que lo citaba, en los dos sentidos.

        Devuelve `(origen, destino, [(archivo, cuántos enlaces)])`. Sirve para
        cualquier documento, no solo para un pendiente.
        """
        if os.path.exists(destino):
            sys.exit(f"ya existe {_mostrar(destino)} — elegí otro nombre")
        # Se agrupa por archivo para reescribir cada uno una sola vez.
        por_archivo = {}
        for archivo, _n, viejo in self.citas_a(origen):
            por_archivo.setdefault(archivo, []).append(viejo)
        # El que se mueve entra siempre: sus enlaces de salida hay que recalcularlos igual.
        por_archivo.setdefault(origen, [])
        reparador = ReparadorDeEnlaces(self.raiz, self.archivos)
        tocados, texto_movido = [], None
        for archivo, viejos in sorted(por_archivo.items()):
            texto = self._leer(archivo)
            # El propio archivo que se mueve cambia de sitio: sus enlaces se
            # recalculan desde el destino, no desde donde estaba.
            base = destino if archivo == origen else archivo
            cambios = 0
            for viejo in sorted(set(viejos), key=len, reverse=True):
                nuevo = self.nuevo_destino(base, destino, viejo)
                if nuevo == viejo:
                    continue
                cuenta = texto.count("](" + viejo + ")")
                if cuenta:
                    texto = texto.replace("](" + viejo + ")", "](" + nuevo + ")")
                    cambios += cuenta
            if archivo == origen:
                texto, salientes = self.reescribir_salientes(texto, origen, destino)
                cambios += salientes
                texto_movido = texto
            # `DOC14` pide que el texto del enlace diga dónde vive el destino: al
            # cambiar el destino, el texto que lo nombraba queda mintiendo.
            if cambios:
                texto, arreglados = reparador.reparar_texto(texto, archivo)
                cambios += arreglados
                if archivo == origen:
                    texto_movido = texto
            if cambios:
                tocados.append((archivo, cambios))
                if escribir and archivo != origen:
                    _escribir(archivo, texto)
        if escribir:
            os.makedirs(os.path.dirname(destino), exist_ok=True)
            shutil.move(origen, destino)
            if texto_movido is not None:
                _escribir(destino, texto_movido)
        return origen, destino, tocados

    # ── el aviso de vuelta ────────────────────────────────────────────────

    @staticmethod
    def misma_carpeta(a, b):
        """Si dos rutas son la misma. En Windows la caja de las letras no cuenta."""
        return os.path.normcase(os.path.abspath(a)) == os.path.normcase(os.path.abspath(b))

    @staticmethod
    def celda(patron, texto):
        m = patron.search(texto)
        return m.group(1).strip().strip("*` ") if m else ""

    @classmethod
    def destinatarios(cls, texto, proyectos):
        """A qué proyectos les toca el aviso, leído de la ficha del pendiente.

        `proyectos` es `[(nombre, ruta)]`, lo que devuelve el registro. Se compara
        por nombre sin distinguir mayúsculas: la ficha la escribe una persona y el
        registro un programa.
        """
        a_quien = cls.celda(_A_QUIEN, texto)
        origen = cls.celda(_ORIGEN, texto)
        if a_quien and _TODOS.search(a_quien):
            return list(proyectos)
        buscado = (origen or a_quien).lower()
        if not buscado:
            return []
        return [(n, r) for n, r in proyectos if n.lower() in buscado or buscado in n.lower()]

    def avisar(self, texto, destino, version, proyectos, fecha, escribir=False):
        """Escribe el aviso en cada proyecto al que le toca. Devuelve `(escritos, sin_entregar)`.

        **Es la mitad que nadie tenía**: sin esto el paso 7 de `02·F24` deja
        pendientes abiertos para siempre, porque nadie vuelve a mirar el
        repositorio ajeno. Solo escribe un archivo de pendiente: **nunca toca
        código del proyecto**.
        """
        titulo = ""
        for linea in texto.splitlines():
            if linea.startswith("# "):
                titulo = linea[2:].strip()
                break
        escritos, sin_entregar = [], []
        for nombre, ruta in self.destinatarios(texto, proyectos):
            # `normcase` y no `abspath` a secas: el registro escribe `c:\` y el
            # comando `C:\`, y sin esto el estándar se manda un aviso a sí mismo.
            if self.misma_carpeta(ruta, self.raiz):
                continue
            if not os.path.isdir(ruta):
                sin_entregar.append((nombre, "la carpeta del proyecto no existe"))
                continue
            carpeta = os.path.join(ruta, CARPETA_AVISOS)
            if not os.path.isdir(carpeta):
                # `61` · **No se le inventa la carpeta**, pero tampoco se calla: un
                # aviso que no llega y no se dice es el defecto de `02·F24`.
                sin_entregar.append((nombre, "no tiene `%s/` — la crea el instalador "
                                             "al ponerse al día" % CARPETA_AVISOS))
                continue
            archivo = os.path.join(carpeta, "aviso-%s-%s" % (fecha, os.path.basename(destino)))
            if os.path.exists(archivo):
                continue                    # idempotente: cerrar dos veces no duplica
            if escribir:
                try:
                    _escribir(archivo, _PLANTILLA_AVISO.format(
                        fecha=fecha, titulo=titulo or "(sin título)", destino=_mostrar(destino), version=version))
                except OSError as e:
                    sin_entregar.append((nombre, "no se pudo escribir: %s" % e.strerror))
                    continue
            escritos.append((nombre, archivo))
        return escritos, sin_entregar

    def version(self):
        """Qué versión trae la corrección. Sin `VERSION` se dice, no se inventa."""
        archivo = os.path.join(self.raiz, "VERSION")
        if not os.path.isfile(archivo):
            return "(sin VERSION)"
        return self._leer(archivo).strip() or "(sin VERSION)"

    @staticmethod
    def proyectos():
        """El registro de proyectos. Si no se puede leer, no se avisa a nadie. Se
        importa acá adentro: el instalador es pesado y lo demás no lo necesita."""
        try:
            from .instalar import Instalador
            return Instalador().proyectos_registrados()
        except Exception:                   # noqa: BLE001: sin registro, nadie recibe
            return []


def reabrir(argv):
    """`cerrar.py reabrir «número» --motivo «…» --fecha «…» [--aplicar]` (`EP-025·HU-022`)."""
    p = argparse.ArgumentParser(description="Reabre un pendiente cerrado: lo devuelve de hecho/ con sus citas.")
    p.add_argument("modo")
    p.add_argument("numero", help="el número del pendiente, p. ej. 53")
    p.add_argument("--motivo", required=True, help="por qué se reabre")
    p.add_argument("--fecha", required=True, help="la fecha de hoy (AAAA-MM-DD)")
    p.add_argument("--raiz", default=Proyecto.estandar())
    p.add_argument("--aplicar", action="store_true", help="escribe de verdad; sin esto solo simula")
    a = p.parse_args(argv)
    origen, destino, tocados = CerradorDePendientes(a.raiz).reabrir(a.numero, a.motivo, a.fecha, a.aplicar)
    print(f"{_mostrar(origen)}\n  -> {_mostrar(destino)}\n")
    for archivo, cuenta in tocados:
        print(f"  {cuenta:>3} enlace(s)  {_mostrar(archivo)}")
    print(f"\nLa fila del índice vuelve a abierta{'' if a.aplicar else ' (simulado; agrega --aplicar)'}.")
    print("El aviso de vuelta que se mandó al cerrar, si lo hubo, no se deshace: ya pudo leerse.")
    return 0


def main(argv=None):
    preparar_salida()
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] == "reabrir":
        return reabrir(argv)
    p = argparse.ArgumentParser(description="Cierra un pendiente moviéndolo a hecho/ sin romper sus citas.")
    p.add_argument("numero", help="el número del pendiente, p. ej. 53")
    p.add_argument("--como", required=True, help="nombre del archivo en hecho/, sin la extensión")
    p.add_argument("--raiz", default=Proyecto.estandar())
    p.add_argument("--aplicar", action="store_true", help="escribe de verdad; sin esto solo simula")
    p.add_argument("--fecha", required=True, help="la fecha de hoy (AAAA-MM-DD), para el aviso de vuelta")
    a = p.parse_args(argv)

    cerrador = CerradorDePendientes(a.raiz)
    texto_original = cerrador._leer(cerrador.archivo_del_pendiente(a.numero))
    origen, destino, tocados = cerrador.cerrar(a.numero, a.como, a.aplicar)

    print(f"{_mostrar(origen)}\n  -> {_mostrar(destino)}\n")
    total = sum(c for _, c in tocados)
    for archivo, cuenta in tocados:
        print(f"  {cuenta:>3} enlace(s)  {_mostrar(archivo)}")
    print(f"\n{total} enlace(s) en {len(tocados)} archivo(s)"
          f"{' — ESCRITO' if a.aplicar else ' (simulado; agrega --aplicar)'}")
    # El aviso de vuelta va acá y no en un comando aparte: **es parte de cerrar**
    # (`02·F24`). Separarlo abre la puerta a cerrar sin avisar.
    avisados, sin_entregar = cerrador.avisar(texto_original, destino, cerrador.version(),
                                             cerrador.proyectos(), a.fecha, a.aplicar)
    print()
    if not avisados and not sin_entregar:
        print("Sin aviso de vuelta: el pendiente no declara proyecto de origen, o a ninguno le toca hoy.")
    for nombre, archivo in avisados:
        print(f"  aviso -> {nombre}: {archivo}{'' if a.aplicar else '  (simulado)'}")
    # `61` · Lo que **no** se pudo entregar se dice: un `continue` mudo era el
    # mismo defecto que `02·F24` vino a cerrar, un nivel más abajo.
    if sin_entregar:
        print()
        print(f"  El aviso NO llegó a {len(sin_entregar)} proyecto(s):")
        for nombre, motivo in sin_entregar:
            print(f"    · {nombre} — {motivo}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
