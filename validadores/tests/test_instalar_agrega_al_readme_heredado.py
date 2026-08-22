# -*- coding: utf-8 -*-
"""`EP-007 · HU-005` · El README heredado gana lo que la plantilla sumó.

**El defecto, dicho por el pendiente 33:** *«el mecanismo replica y el texto que
lo explica no»*. El `CLAUDE.md` de cada proyecto sí recibía las secciones nuevas
del estándar; el `README.md` del histórico, no. Un proyecto instalado en julio
se quedaba con el texto de julio para siempre, y nadie se enteraba: el archivo
existe, se lee bien y dice cosas ciertas — solo que menos.

**Lo que estas pruebas protegen es el límite, no el agregado.** Agregar es fácil;
lo difícil es no pisar. `CP-02` es el caso que decide: lo que el proyecto
escribió tiene que seguir ahí, palabra por palabra, después de instalar.
"""
import contextlib
import io
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import instalar    # noqa: E402
import version     # noqa: E402
import versiones   # noqa: E402
from comun import RAIZ, leer   # noqa: E402


@contextlib.contextmanager
def _estandar_temporal():
    """Copia desechable del estándar: la plantilla se edita, y no la de verdad."""
    carpeta = tempfile.mkdtemp(prefix="cimiento-estandar-")
    shutil.copytree(os.path.join(RAIZ, "plantillas"),
                    os.path.join(carpeta, "plantillas"))
    shutil.copy2(os.path.join(RAIZ, "VERSION"),
                 os.path.join(carpeta, "VERSION"))
    guardado = (instalar.RAIZ, instalar.REGISTRO, instalar.PLANTILLA_HISTORICO,
                instalar.PLANTILLA_MEMORIA, version.RAIZ)
    instalar.RAIZ = carpeta
    instalar.REGISTRO = os.path.join(carpeta, "plantillas", "proyectos.md")
    instalar.PLANTILLA_HISTORICO = os.path.join(carpeta, "plantillas",
                                                "historico-chat.md")
    instalar.PLANTILLA_MEMORIA = os.path.join(carpeta, "plantillas",
                                              "memoria.md")
    version.RAIZ = carpeta
    try:
        yield carpeta
    finally:
        (instalar.RAIZ, instalar.REGISTRO, instalar.PLANTILLA_HISTORICO,
         instalar.PLANTILLA_MEMORIA, version.RAIZ) = guardado
        shutil.rmtree(carpeta, ignore_errors=True)


class ElReadmeHeredadoSeCompleta(unittest.TestCase):

    def setUp(self):
        self.temporal = tempfile.mkdtemp(prefix="cimiento-")
        self.proyecto = os.path.join(self.temporal, "proyecto de prueba")
        os.makedirs(self.proyecto)
        self.contexto = _estandar_temporal()
        self.estandar = self.contexto.__enter__()

    def tearDown(self):
        self.contexto.__exit__(None, None, None)
        shutil.rmtree(self.temporal, ignore_errors=True)

    @property
    def readme(self):
        return os.path.join(self.proyecto, "historico-chat", "README.md")

    def _instalar(self):
        return instalar.instalar_historico(self.proyecto, aplicar=True)

    def _plantilla_gana_seccion(self, titulo="## Lo que el estándar sumó"):
        ruta = instalar.PLANTILLA_HISTORICO
        with io.open(ruta, "a", encoding="utf-8", newline="\n") as f:
            f.write(u"\n\n%s\n\nEsto es nuevo y tiene que llegar.\n" % titulo)
        return titulo.lstrip("# ").strip()

    def test_cp01_la_seccion_nueva_llega_al_proyecto_ya_instalado(self):
        self._instalar()                       # el proyecto queda instalado
        titulo = self._plantilla_gana_seccion()
        pasos = self._instalar()               # y el estándar cambió
        self.assertTrue(any("lo que la plantilla sumó" in p for p in pasos),
                        "el instalador no reportó lo que agregó: %s" % pasos)
        self.assertIn(titulo, leer(self.readme))
        self.assertIn("Esto es nuevo y tiene que llegar", leer(self.readme))

    def test_cp02_lo_que_el_proyecto_escribio_sigue_ahi(self):
        """El caso que decide: aditivo significa que nada se pisa."""
        self._instalar()
        propio = u"\n\n## Cómo trabajamos acá\n\nEsto lo escribió el proyecto.\n"
        with io.open(self.readme, "a", encoding="utf-8", newline="\n") as f:
            f.write(propio)
        self._plantilla_gana_seccion()
        self._instalar()
        texto = leer(self.readme)
        self.assertIn("Cómo trabajamos acá", texto)
        self.assertIn("Esto lo escribió el proyecto.", texto)

    def test_cp03_sin_novedad_no_reescribe_nada(self):
        """Un instalador que reporta siempre se apaga: sin cambios, se calla."""
        self._instalar()
        antes = leer(self.readme)
        pasos = self._instalar()
        self.assertEqual([], [p for p in pasos if "lo que la plantilla sumó" in p])
        self.assertEqual(antes, leer(self.readme))

    def test_cp04_la_seccion_llega_con_su_texto_no_vacia(self):
        """Agregar el título solo obligaría a ir a copiar el contenido a mano."""
        self._instalar()
        self._plantilla_gana_seccion(u"## Con su cuerpo")
        self._instalar()
        texto = leer(self.readme)
        i = texto.find("## Con su cuerpo")
        self.assertGreater(len(texto[i:].strip().splitlines()), 1)

    def test_cp05_el_sello_queda_al_dia(self):
        """Si el texto se completó, el sello tiene que decir contra qué."""
        self._instalar()
        self._plantilla_gana_seccion()
        self._instalar()
        self.assertIn("<!-- huella:", leer(self.readme))

    def test_cp06_si_no_existe_se_crea_entero(self):
        pasos = self._instalar()
        self.assertTrue(any("crear historico-chat/README.md" in p for p in pasos))
        self.assertTrue(os.path.isfile(self.readme))


if __name__ == "__main__":
    unittest.main()
