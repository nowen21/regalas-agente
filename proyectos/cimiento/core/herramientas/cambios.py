"""Separa lo que cambió cada sesión, para que el commit lleve solo lo de una (`EP-025·HU-016`).

El control del commit (`SesionesMezcladas`) ya sabe qué archivo tocó cada
sesión, pero solo avisa. Separar se hacía con un guion escrito para la ocasión
(análisis 2 del pendiente 119, acuerdo 6). Esto lo hace con el mismo registro de
`historico-chat/.tocado/`.

**Lo que tocaron dos sesiones no se prepara**: se nombra, y decide quien hace el
commit. **Toda acción trae su contraria** (análisis 3, acuerdo 2): `soltar` saca
del área de preparación lo que `preparar` puso.
"""
import subprocess
from collections import Counter

from ..comun import Proyecto
from ..validadores.sesiones import Sesiones


class CambiosPorSesion:
    """Cruza el registro de sesiones con `git status`. Sin `escribir`, simula."""

    def __init__(self, raiz, ahora=None):
        self.proyecto = Proyecto(raiz)
        self.sesiones = Sesiones(self.proyecto)
        self.ahora = ahora

    def _git(self, *argumentos):
        return subprocess.run(["git", "-c", "core.quotepath=false"] + list(argumentos), cwd=self.proyecto.raiz,
                              capture_output=True, text=True, encoding="utf-8", errors="replace")

    def cambiados(self):
        """Lo que git ve cambiado, archivo por archivo (también dentro de carpetas nuevas)."""
        proceso = self._git("status", "--porcelain", "-uall")
        if proceso.returncode != 0:
            raise ValueError("acá no hay un repositorio git: %s" % self.proyecto.raiz)
        salida = set()
        for linea in proceso.stdout.splitlines():
            ruta = linea[3:].strip().strip('"')
            salida.add(ruta.split(" -> ")[-1])
        return salida

    def preparados(self):
        return {l.strip() for l in self._git("diff", "--cached", "--name-only").stdout.splitlines() if l.strip()}

    def repartir(self):
        """`({sesión: [archivos solo de ella]}, [compartidos], [sin sesión])`."""
        cambiados = self.cambiados()
        por_sesion = {s: cambiados & archivos for s, archivos in self.sesiones.registros(self.ahora).items()}
        cuantas = Counter(a for archivos in por_sesion.values() for a in archivos)
        compartidos = {a for a, n in cuantas.items() if n > 1}
        propios = {s: sorted(archivos - compartidos) for s, archivos in por_sesion.items() if archivos - compartidos}
        return propios, sorted(compartidos), sorted(cambiados - set(cuantas))

    def sesion(self, prefijo):
        """La sesión viva cuyo identificador empieza por `prefijo`."""
        vivas = [s for s in self.sesiones.registros(self.ahora) if s.startswith(prefijo)]
        if len(vivas) != 1:
            raise ValueError("«%s» %s" % (prefijo, "no es una sesión viva" if not vivas
                                          else "nombra a %d sesiones; escribe más letras" % len(vivas)))
        return vivas[0]

    def preparar(self, prefijo, escribir=False):
        """Prepara para el commit lo que solo tocó esa sesión. `(sesión, [archivos], [compartidos])`."""
        sesion = self.sesion(prefijo)
        propios, compartidos, _sin = self.repartir()
        archivos = propios.get(sesion, [])
        if escribir and archivos:
            proceso = self._git("add", "-A", "--", *archivos)
            if proceso.returncode != 0:
                raise ValueError("git no preparó los archivos: %s" % proceso.stderr.strip())
        return sesion, archivos, compartidos

    def soltar(self, prefijo, escribir=False):
        """La contraria: saca del área de preparación lo de esa sesión. `(sesión, [archivos])`."""
        sesion = self.sesion(prefijo)
        propios, _compartidos, _sin = self.repartir()
        archivos = sorted(self.preparados() & set(propios.get(sesion, [])))
        if escribir and archivos:
            proceso = self._git("restore", "--staged", "--", *archivos)
            if proceso.returncode != 0:
                raise ValueError("git no soltó los archivos: %s" % proceso.stderr.strip())
        return sesion, archivos
