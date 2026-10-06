"""Retira archivos que ya no hacen falta, sin dejar enlaces rotos.

**Si algo se elimina, ningún enlace lo sigue nombrando** (análisis 1 del
pendiente 116, acuerdo 15). Pero el documento que lo enlazaba es historia: lo que
dijo se queda como lo dijo. Por eso el enlace se convierte en texto simple
(`[la ficha](docs/x.md)` queda `la ficha`) y el archivo se borra en el mismo
cambio. No se enlaza la versión vieja: lo que ya no está no hace falta.

No toca lo que el revisor de enlaces tampoco corrige: las transcripciones, las
palabras del usuario en `prompts/` y la conversación copiada en un análisis.

Se pide a mano y simula si no se le dice `--aplicar`:

    python validadores/retirar.py documentacion/vieja.md
    python validadores/retirar.py validadores/docs/*.md --aplicar
"""
import argparse
import os
import re
import sys

if __name__ == "__main__" and not __package__:
    # Corrido por su ruta: se arma el paquete para que las importaciones
    # relativas encuentren a `core`.
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    __package__ = "core.herramientas"

from ..comun import Archivos, Proyecto
from ..comun.consola import preparar_salida
from ..validadores.enlaces import Enlaces

_ENLACE = re.compile(r"\[([^\]\n]*)\]\(([^)\s]+)\)")
_CODIGO = re.compile(r"(`+)(?:(?!\1).)*?\1")


class Retiro:
    """Los enlaces que apuntan a lo que se retira, y su conversión a texto."""

    def __init__(self, proyecto, archivos=None):
        self.proyecto = proyecto if isinstance(proyecto, Proyecto) else Proyecto(proyecto)
        self.archivos = archivos or Archivos()
        self.enlaces = Enlaces(self.proyecto)

    @staticmethod
    def _normal(ruta):
        return os.path.normcase(os.path.normpath(os.path.abspath(ruta)))

    def apunta_a(self, archivo, destino, retiradas):
        """Si el destino lleva a una de las rutas retiradas."""
        if not self.enlaces.es_interno(destino):
            return False
        en_disco = self.enlaces.destino_en_disco(archivo, destino)
        return bool(en_disco) and self._normal(en_disco) in retiradas

    def convertir(self, archivo, texto, retiradas):
        """`(texto nuevo, cuántos enlaces pasaron a texto)`. Lo que va en un bloque
        de código o entre comillas invertidas no es enlace y no se toca."""
        protegidas = self.enlaces.lineas_de_conversacion(archivo, texto)
        salida, cambios, en_cerca = [], 0, False
        for n, linea in enumerate(texto.split("\n"), 1):
            if linea.lstrip().startswith(("```", "~~~")):
                en_cerca = not en_cerca
            if en_cerca or n in protegidas:
                salida.append(linea)
                continue
            codigos = [(m.start(), m.end()) for m in _CODIGO.finditer(linea)]

            def cambiar(m):
                nonlocal cambios
                if any(a <= m.start() < b for a, b in codigos) or not self.apunta_a(archivo, m.group(2), retiradas):
                    return m.group(0)
                cambios += 1
                return m.group(1)

            salida.append(_ENLACE.sub(cambiar, linea))
        return "\n".join(salida), cambios

    def documentos(self):
        """Los `.md` donde se buscan enlaces: todos, menos los que no se corrigen."""
        for archivo in self.proyecto.recorrer_md():
            if not (self.enlaces.es_transcripcion(archivo) or self.enlaces.es_del_usuario(archivo)):
                yield archivo

    def retirar(self, rutas, aplicar=False):
        """`(cambios, faltan)`: `[(documento, cuántos)]` y las rutas pedidas que
        no existen. Con `aplicar`, escribe los documentos y borra los archivos."""
        faltan = [r for r in rutas if not os.path.isfile(r)]
        retiradas = {self._normal(r) for r in rutas if os.path.isfile(r)}
        cambios = []
        for archivo in self.documentos():
            if self._normal(archivo) in retiradas:
                continue
            nuevo, cuantos = self.convertir(archivo, self.archivos.leer(archivo), retiradas)
            if cuantos:
                cambios.append((archivo, cuantos))
                if aplicar:
                    with open(archivo, "w", encoding="utf-8", newline="\n") as f:
                        f.write(nuevo)
        if aplicar:
            for ruta in rutas:
                if os.path.isfile(ruta):
                    os.remove(ruta)
        return cambios, faltan


def main(argv=None):
    preparar_salida()
    p = argparse.ArgumentParser(description="Retira archivos y deja en texto simple los enlaces que los nombraban.")
    p.add_argument("rutas", nargs="+", help="archivos que se retiran")
    p.add_argument("--raiz", default=None, help="carpeta del proyecto; sin esto, el estándar")
    p.add_argument("--aplicar", action="store_true", help="escribe y borra; sin esto solo muestra lo que haría")
    a = p.parse_args(argv)
    proyecto = Proyecto(os.path.abspath(a.raiz) if a.raiz else Proyecto.estandar())
    cambios, faltan = Retiro(proyecto).retirar([os.path.abspath(r) for r in a.rutas], aplicar=a.aplicar)
    for ruta in faltan:
        print("no existe: %s" % proyecto.mostrar(ruta))
    for archivo, cuantos in cambios:
        print("%s: %d enlace(s) a texto" % (proyecto.mostrar(archivo), cuantos))
    print("\n%s %d archivo(s); %d enlace(s) pasan a texto en %d documento(s)%s." % (
        "Retirados" if a.aplicar else "Se retirarían", len(a.rutas) - len(faltan),
        sum(c for _, c in cambios), len(cambios), "" if a.aplicar else " (simulación: falta --aplicar)"))
    return 1 if faltan else 0


if __name__ == "__main__":
    sys.exit(main())
