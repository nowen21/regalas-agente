"""Ningún archivo que el instalador copia conserva un hueco sin llenar.

Fase `A-EP-007-HU-001-rellenar-los-marcadores-al-copiar`, casos CP-001 a CP-004.

**Por qué la prueba corre la instalación entera y no función por función.**
El defecto que motivó esta fase no estaba en ninguna función suelta: cada una
hacía bien lo suyo. Estaba en que **una de las cuatro rellenaba los marcadores
y tres no**, así que la cita a una regla llegaba muerta al proyecto. Una prueba
por función no lo habría visto; correr la instalación y mirar lo que quedó
escrito, sí.

Se usa `unittest` de la biblioteca estándar y no una herramienta de afuera:
la épica pide que todo corra sin internet y sin instalar nada antes.

Cómo se corre:

    python -m unittest discover -s validadores/tests
"""

import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import instalar  # noqa: E402
from comun import leer  # noqa: E402

# Qué hueco se comprueba, y cuál no.
#
# Un `.md` copiado puede llegar con dos clases de hueco, y solo una es defecto:
#
#   - Los que **el instalador sabe llenar** — la ruta del estándar, el nombre
#     del proyecto, la fecha. Si sobreviven a la copia, el enlace llega muerto
#     al proyecto: ese es el defecto que arregla esta fase.
#   - Los que **el proyecto llena después** — a qué se dedica el negocio, quién
#     usa el sistema. Llegan vacíos a propósito: son las preguntas que el
#     instalador no puede responder, y borrarlas sería inventar la respuesta.
#
# Por eso no se busca la marca `«` a secas: se buscan los marcadores de
# `_rellenos()`, que es la lista de lo que el instalador se comprometió a
# llenar. Al salir de esa lista, la prueba cubre sola el marcador que se agregue
# mañana, sin tener que actualizarla.
def _marcadores_del_instalador(proyecto):
    return sorted(instalar._rellenos(proyecto))


def _md_instalados(raiz):
    """Los .md que quedaron dentro del proyecto de prueba."""
    salida = []
    for carpeta, subcarpetas, archivos in os.walk(raiz):
        subcarpetas[:] = [s for s in subcarpetas if s != ".git"]
        for nombre in sorted(archivos):
            if nombre.lower().endswith(".md"):
                salida.append(os.path.join(carpeta, nombre))
    return salida


def _sin_llenar(raiz):
    """[(archivo, línea, marcador)] por cada marcador que el instalador dejó."""
    marcadores = _marcadores_del_instalador(raiz)
    hallazgos = []
    for archivo in _md_instalados(raiz):
        for n, linea in enumerate(leer(archivo).splitlines(), 1):
            for marcador in marcadores:
                if marcador in linea:
                    hallazgos.append(
                        (os.path.relpath(archivo, raiz), n, marcador))
    return hallazgos


class InstalacionSinMarcadores(unittest.TestCase):
    """Los cuatro casos del `plan_pruebas` de la fase."""

    nombre_carpeta = "proyecto de prueba"

    def setUp(self):
        self.temporal = tempfile.mkdtemp(prefix="cimiento-")
        self.proyecto = os.path.join(self.temporal, self.nombre_carpeta)
        os.makedirs(self.proyecto)

        # El registro central de proyectos se apunta a una copia desechable.
        # Instalar anota el proyecto en `plantillas/proyectos.md`, y una prueba
        # que escriba ahí deja una fila muerta por corrida: la lista real
        # terminó con 99 carpetas temporales que ya no existen, y es la que
        # `instalar.py --todos` recorre (`08·T4`: no se prueba contra lo real).
        self.registro = os.path.join(self.temporal, "proyectos.md")
        shutil.copy2(instalar.REGISTRO, self.registro)
        self.registro_real = instalar.REGISTRO
        instalar.REGISTRO = self.registro

    def tearDown(self):
        instalar.REGISTRO = self.registro_real
        shutil.rmtree(self.temporal, ignore_errors=True)

    def _instalar(self):
        return instalar.instalar(self.nombre_carpeta, self.proyecto,
                                 aplicar=True)

    def test_cp_001_ninguna_copia_conserva_un_marcador(self):
        """CP-001 · lo que el instalador sabe llenar, llega lleno."""
        self._instalar()

        self.assertTrue(_md_instalados(self.proyecto),
                        "la instalación no escribió ningún .md")

        huecos = _sin_llenar(self.proyecto)
        self.assertEqual(
            huecos, [],
            "el instalador dejó marcadores suyos sin llenar:\n" + "\n".join(
                f"  {a}:{n} — {m}" for a, n, m in huecos))

    def test_cp_002_la_ruta_del_estandar_quedo_escrita(self):
        """CP-002 · el enlace apunta al estándar, no al marcador.

        La parte de hacer clic es verificación manual y va en el
        `resultado_pruebas`. Acá se comprueba lo que sí se puede leer: que la
        ruta escrita existe en disco.
        """
        self._instalar()

        stack = os.path.join(self.proyecto, ".agente", "stack-instalacion.md")
        self.assertTrue(os.path.isfile(stack), "no se copió el stack")

        texto = leer(stack)
        self.assertNotIn("«RUTA-ESTANDAR»", texto)
        self.assertIn(instalar.RAIZ.replace("\\", "/"), texto)

    def test_cp_003_reinstalar_no_cambia_lo_que_ya_estaba_bien(self):
        """CP-003 · la segunda corrida no cambia nada ni deja huecos."""
        self._instalar()
        antes = {a: leer(a) for a in _md_instalados(self.proyecto)}

        self._instalar()
        despues = {a: leer(a) for a in _md_instalados(self.proyecto)}

        self.assertEqual(sorted(antes), sorted(despues),
                         "la segunda corrida agregó o quitó archivos")
        distintos = [os.path.relpath(a, self.proyecto)
                     for a in antes if antes[a] != despues[a]]
        self.assertEqual(distintos, [],
                         f"la segunda corrida cambió: {distintos}")
        self.assertEqual(_sin_llenar(self.proyecto), [])


class InstalacionEnRutaConTildes(InstalacionSinMarcadores):
    """CP-004 · lo mismo, en una carpeta con espacios y tilde en el nombre.

    Importa porque el repositorio del estándar vive en una ruta así: si el
    relleno se rompiera con eso, se rompería en la máquina donde se desarrolla.
    """

    nombre_carpeta = "proyecto de prueba ñ"


if __name__ == "__main__":
    unittest.main()
