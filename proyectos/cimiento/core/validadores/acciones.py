"""`00·N1` · `EP-001·HU-012` · El inventario de acciones del agente no tiene huecos.

Cada clase de acción del anexo trae **su nivel y su ejemplo**, el nivel es uno
de los tres de la escala, y ninguna herramienta del agente se queda sin clase.

**Qué no se comprueba, y se declara**: que la clasificación sea la acertada.
Eso es un juicio y se discute leyendo; un programa que opinara estaría
inventando criterio.

El anexo existe para que un plan aprobado cubra lo reversible y **nunca** lo
irreversible: una clase sin nivel deja esa distinción sin decidir justo donde
hace falta.
"""
import os
import re

from ..comun import FALLA, Hallazgo
from .base import Validador

ANEXO = os.path.join("base", "00-identidad-y-rol", "acciones-y-riesgo.md")

# La escala es **cerrada**: con texto libre cada clase usaría su propia palabra
# y no habría comparación posible.
ESCALA = ("🟢", "🟡", "🔴")

# Las diez herramientas del `CA-01`. Se buscan por una palabra suya y no por la
# frase entera: exigir la frase literal sería comprobar la redacción.
HERRAMIENTAS = {
    "leer": ("Leer",),
    "escribir en el repositorio": ("Escribir un archivo del repositorio",),
    "borrar": ("Borrar algo versionado", "Borrar algo NO versionado"),
    "comando local": ("Correr un comando local",),
    "salir a la red": ("Correr algo que sale a la red",),
    "control de versiones": ("Guardar en el control de versiones",
                             "Publicar o reescribir la historia"),
    "datos": ("Tocar datos reales",),
    "fuera del repositorio": ("Tocar la máquina fuera del repositorio",),
    "histórico": ("Escribir en el histórico",),
    "memoria": ("Escribir en la memoria",),
}

_FILA = re.compile(r"(?m)^\|\s*\*\*(.+?)\*\*\s*\|(.*?)\|(.*?)\|(.*?)\|")


class InventarioDeAcciones(Validador):
    """Los tres huecos que dejan la tabla del anexo sin servir."""

    nombre = "acciones"
    regla = "00·N1"
    descripcion = "el inventario de acciones del agente y su riesgo"

    @property
    def anexo(self):
        return os.path.join(self.proyecto.raiz, *ANEXO.split(os.sep))

    def clases(self):
        """`[(clase, nivel, ejemplo)]` de la tabla del anexo."""
        if not os.path.isfile(self.anexo):
            return []
        salida = []
        for m in _FILA.finditer(self.archivos.leer(self.anexo)):
            # La cabecera de la tabla y la fila de la escala no son clases.
            if m.group(1).strip().startswith("Nivel") or "Qué incluye" in m.group(2):
                continue
            salida.append((m.group(1).strip(), m.group(3).strip(), m.group(4).strip()))
        return salida

    def validar(self):
        archivo = self.anexo
        if not os.path.isfile(archivo):
            return [Hallazgo(FALLA, archivo, 0, "falta el anexo de acciones y riesgo — sin él, `00·N1` "
                                                "trata igual la coma del README y el borrado de la base")]
        hallazgos = []
        filas = self.clases()
        for nombre, nivel, ejemplo in filas:
            puestos = [e for e in ESCALA if e in nivel]
            if not puestos:
                hallazgos.append(Hallazgo(FALLA, archivo, 0, "«%s» tiene el nivel «%s», que no es de la escala — "
                                                             "la escala es cerrada, si no no se pueden comparar "
                                                             "dos clases" % (nombre, nivel)))
            elif len(puestos) > 1:
                # Una fila con dos niveles es dos clases sin partir: mirar si hay
                # *algún* nivel y no si hay **uno** dejó pasar una al construir el anexo.
                hallazgos.append(Hallazgo(FALLA, archivo, 0, "«%s» pone %d niveles en la misma fila — son dos "
                                                             "clases sin partir, y así no se puede decir qué "
                                                             "exige" % (nombre, len(puestos))))
            if not ejemplo:
                hallazgos.append(Hallazgo(FALLA, archivo, 0, "«%s» tiene nivel y **no tiene ejemplo** — el nivel "
                                                             "solo se discute; el ejemplo es lo que lo hace "
                                                             "entender" % nombre))
        # Se busca en los nombres de las clases y no en el texto entero: una
        # clase borrada de la tabla seguía «encontrada» porque otra sección la
        # nombraba de ejemplo.
        nombres = "\n".join(n for n, _niv, _ej in filas)
        hallazgos += [Hallazgo(FALLA, archivo, 0, "«%s» no tiene clase en el anexo — el agente puede hacerlo y "
                                                  "nada dice qué cuesta deshacerlo" % herramienta)
                      for herramienta, marcas in sorted(HERRAMIENTAS.items())
                      if not any(m in nombres for m in marcas)]
        return hallazgos

    def linea_resumen(self):
        """Cuántas clases hay y cómo se reparten. Va aunque no haya hallazgos."""
        filas = self.clases()
        if not filas:
            return ""
        cuenta = {e: sum(1 for _n, niv, _ej in filas if e in niv) for e in ESCALA}
        return ("Clases de acción: %d · 🟢 %d se deshacen solas · 🟡 %d con trabajo · 🔴 %d no se deshacen"
                % (len(filas), cuenta["🟢"], cuenta["🟡"], cuenta["🔴"]))
