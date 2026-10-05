"""Lo que comparten los comandos de consola: la salida en UTF-8, la entrada JSON
de los enganches y el reporte de hallazgos.

Estaba en `validadores/comun.py` junto con todo lo demás; acá queda aparte
porque solo lo usa quien habla con una persona o con una herramienta, nunca
una comprobación.
"""
import json
import os
import sys

from .hallazgos import AVISO, FALLA
from .proyecto import Proyecto


def preparar_salida():
    """La consola de Windows no siempre es UTF-8: que un acento no rompa todo."""
    for flujo in (sys.stdout, sys.stderr):
        try:
            flujo.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass


def entrada_json():
    """El JSON que la herramienta manda por la entrada estándar, leído en UTF-8.

    `json.load(sys.stdin)` decodifica con la codificación de la consola, que en
    Windows no es UTF-8: la «í» llegaba partida (pendiente 111)."""
    try:
        crudo = sys.stdin.buffer.read()
    except AttributeError:
        crudo = (sys.stdin.read() or "").encode("utf-8", "replace")
    return json.loads(crudo.decode("utf-8", "replace") or "{}")


def raiz_pedida(argv, defecto):
    """La carpeta del proyecto: la de `--raiz X`, o `defecto`. Estaba copiada en
    once enganches, cada uno con su propio valor por defecto, que es lo único que
    cambiaba (análisis 1 del pendiente 116, fila 4)."""
    if "--raiz" in argv:
        i = argv.index("--raiz")
        if i + 1 < len(argv):
            return os.path.abspath(argv[i + 1])
    return os.path.abspath(defecto)


def archivo_editado(datos):
    """La ruta que la herramienta escribió: primero la de la entrada y después la
    de la respuesta, con las dos formas de nombrarla que usa."""
    entrada = (datos or {}).get("tool_input") or {}
    respuesta = (datos or {}).get("tool_response") or {}
    return (entrada.get("file_path") or entrada.get("filePath")
            or respuesta.get("filePath") or respuesta.get("file_path") or "")


def conteo_por_regla(hallazgos):
    """`{regla: cuántos}`. Lo que no nombra regla va aparte, bajo `"(sin regla)"`:
    repartirlo falsearía el número con que se decide qué regla cambiar."""
    cuenta = {}
    for h in hallazgos:
        clave = h.regla or "(sin regla)"
        cuenta[clave] = cuenta.get(clave, 0) + 1
    return cuenta


class Reporte:
    """Imprime hallazgos y guarda los de toda la corrida, para contarlos por regla
    al final (`EP-004·HU-009`)."""

    def __init__(self, raiz=None):
        self.proyecto = Proyecto(raiz or Proyecto.estandar() or os.getcwd())
        self.corrida = []

    def donde(self, hallazgo):
        ruta = self.proyecto.mostrar(hallazgo.archivo)
        return "%s:%s" % (ruta, hallazgo.linea) if hallazgo.linea else ruta

    def linea(self, hallazgo):
        return "[%s] %s — %s" % (hallazgo.severidad, self.donde(hallazgo), hallazgo.mensaje)

    def reportar(self, hallazgos, titulo=None, archivos=None):
        """Imprime y devuelve el código de salida: 1 si hay FALLA.

        Agrega lo que no se pudo leer (`EP-004·HU-003`): callarlo haría creer
        que se miró todo."""
        hallazgos = list(hallazgos)
        if archivos is not None:
            hallazgos += [h for h in archivos.ilegibles() if h not in hallazgos]
        self.corrida.extend(hallazgos)
        fallas = [h for h in hallazgos if h.severidad == FALLA]
        avisos = [h for h in hallazgos if h.severidad == AVISO]
        if titulo:
            print("== %s ==" % titulo)
        for h in fallas + avisos:
            print(self.linea(h))
        if not hallazgos:
            print("OK: sin incumplimientos.")
            return 0
        print("\n%d falla(s), %d aviso(s)." % (len(fallas), len(avisos)))
        return 1 if fallas else 0
