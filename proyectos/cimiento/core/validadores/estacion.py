"""`EP-005·HU-019` · La estación 12 del ciclo, «commit», en el `estado-fase.md`.

El commit ocurre después de que el agente termina de escribir, así que nadie
vuelve a marcar la casilla. Esto la marca con el hash, después del commit: el
archivo queda modificado y sin guardar, porque reescribir el commit cambia el
hash y hacer otro commit solo cruza `00·N1`.

**No corrige, no mueve, no borra.** Escribe una casilla vacía y nada más. Y la
lee `fases`, para contar cuáles quedaron sin marcar.
"""
import io
import os
import re

from ..comun import Proyecto
from .epicas import Epicas
from .moldes import Moldes

# La fila 12 de la tabla de estaciones del molde `10`. Se exige la tabla: no se
# inventa una fila donde no hay ninguna.
_FILA_12 = re.compile(r"^(\|\s*12\s*\|[^|\n]*\|[^|\n]*\|)(\s*)([^|\n]*?)(\s*\|)\s*$", re.M)
# Ya marcada: trae un ✅ o algo con forma de hash.
_YA_MARCADA = re.compile(r"✅|`[0-9a-f]{7,40}`")


class EstacionDelCommit:

    @staticmethod
    def tiene_fila(texto):
        return bool(_FILA_12.search(texto or ""))

    @staticmethod
    def ya_marcada(texto):
        """**No se pisa**: el hash dice qué commit cerró la fase, y reescribirlo
        con el último la haría apuntar a la corrección de una coma."""
        dice = _FILA_12.search(texto or "")
        return bool(dice and _YA_MARCADA.search(dice.group(3)))

    @classmethod
    def marcar(cls, texto, hash_corto):
        """El texto con la casilla marcada, o `None` si no hay que tocarlo: sin
        cambio, quien llama no puede reescribir el archivo sin querer."""
        if not texto or not hash_corto or not cls.tiene_fila(texto) or cls.ya_marcada(texto):
            return None
        nuevo = _FILA_12.sub(lambda m: "%s ✅ `%s` |" % (m.group(1), hash_corto), texto, count=1)
        return nuevo if nuevo != texto else None

    @staticmethod
    def fase_de(ruta_relativa):
        """La carpeta de la fase a la que pertenece un archivo, o `""`. Se reconoce
        por la forma del nombre, así sirve en cualquier proyecto."""
        partes = ruta_relativa.replace("\\", "/").split("/")
        for i, tramo in enumerate(partes):
            if Epicas.fase(tramo):
                return "/".join(partes[:i + 1])
        return ""

    @classmethod
    def fases_que_toca(cls, archivos):
        vistas = []
        for archivo in archivos:
            carpeta = cls.fase_de(archivo)
            if carpeta and carpeta not in vistas:
                vistas.append(carpeta)
        return vistas

    @staticmethod
    def cierre_escrito(raiz, ruta_cierre):
        """`EP-005·HU-022` · El cierre ya no es el molde. Sin molde contra qué
        comparar no se afirma (`04·R4`), y se deja marcar."""
        moldes = Moldes(raiz) or Moldes(Proyecto.estandar() or raiz)
        if "funcionalidad_implementada.md" not in moldes.de_cada_uno:
            return True
        return moldes.sigue_siendo_el_molde(ruta_cierre) is None

    @classmethod
    def marcar_las_fases(cls, raiz, archivos, hash_corto, cerrada_en_git):
        """Escribe el hash en las fases que el commit cierra; devuelve las tocadas.
        Una fase cuyo cierre no está en git no se marca: diría que se commiteó algo
        que no se commiteó."""
        tocadas = []
        for carpeta in cls.fases_que_toca(archivos):
            ruta = os.path.join(raiz, *carpeta.split("/"))
            estado = os.path.join(ruta, "estado-fase.md")
            cierre = os.path.join(ruta, "funcionalidad_implementada.md")
            if not os.path.isfile(estado) or not cerrada_en_git(cierre) or not cls.cierre_escrito(raiz, cierre):
                continue
            try:
                with io.open(estado, encoding="utf-8", errors="replace") as f:
                    nuevo = cls.marcar(f.read(), hash_corto)
                if nuevo is None:
                    continue
                with io.open(estado, "w", encoding="utf-8", newline="\n") as f:
                    f.write(nuevo)
            except OSError:
                continue                    # no se detiene nada por no poder escribir
            tocadas.append(carpeta)
        return tocadas
