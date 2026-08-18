# -*- coding: utf-8 -*-
"""Pendiente 54 · Cerrar un pendiente no rompe los enlaces que lo citaban.

El backlog se cita a sí mismo todo el tiempo, y también lo citan las fases, los
resúmenes y el índice. Mover un archivo a `hecho/` dejaba apuntando al vacío a
todos ellos, y se corregían a mano — justo cuando uno está terminando algo, que
es cuando menos ganas hay de mirarlo.

Se midió dos veces y empeoraba:

| Cuándo | Qué se cerró | Enlaces rotos |
|---|---|---|
| 2026-08-16 | el pendiente 35 | 12 |
| 2026-08-17 | el pendiente 53 | **58**, en 39 archivos |

`cerrar.py` no busca texto: resuelve cada enlace contra el disco y compara
rutas absolutas, así que da igual cuántos `../` lleve delante o desde qué
carpeta se escribió. Estas pruebas fijan las dos direcciones —lo que cita al
archivo y lo que el archivo cita— y las tres trampas que costaron una corrida
cada una.
"""
import os
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import cerrar     # noqa: E402
import enlaces    # noqa: E402


class CerrarArrastraLasCitas(unittest.TestCase):

    def _repo(self, archivos):
        """Un repositorio de mentira: {ruta relativa: contenido}."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        raiz = tmp.name
        for rel, texto in archivos.items():
            ruta = os.path.join(raiz, rel.replace("/", os.sep))
            os.makedirs(os.path.dirname(ruta), exist_ok=True)
            with open(ruta, "w", encoding="utf-8") as f:
                f.write(texto)
        return raiz

    def _leer(self, raiz, rel):
        with open(os.path.join(raiz, rel.replace("/", os.sep)),
                  encoding="utf-8") as f:
            return f.read()

    # -- lo que cita al pendiente ------------------------------------------

    def test_la_cita_desde_lejos_se_reapunta(self):
        """El caso real: una fase enterrada cinco carpetas abajo."""
        raiz = self._repo({
            "pendientes/07-algo.md": "# Algo\n",
            "documentacion/epicas/EP-1/HU-1/A-1/plan.md":
                "Ver [el 07](../../../../../pendientes/07-algo.md).\n",
        })
        cerrar.cerrar(raiz, "07", "algo-resuelto", escribir=True)
        texto = self._leer(raiz, "documentacion/epicas/EP-1/HU-1/A-1/plan.md")
        self.assertIn("../../../../../pendientes/hecho/algo-resuelto.md", texto)
        self.assertEqual([], enlaces.validar_enlaces(raiz))

    def test_la_cita_desde_la_misma_carpeta_tambien(self):
        """El índice del backlog cita sin `../`, y también hay que arreglarlo."""
        raiz = self._repo({
            "pendientes/07-algo.md": "# Algo\n",
            "pendientes/README.md": "- [07](07-algo.md)\n",
        })
        cerrar.cerrar(raiz, "07", "algo-resuelto", escribir=True)
        self.assertIn("hecho/algo-resuelto.md",
                      self._leer(raiz, "pendientes/README.md"))

    def test_el_ancla_se_conserva(self):
        raiz = self._repo({
            "pendientes/07-algo.md": "# Algo\n\n## El problema\n",
            "notas/n.md": "Ver [el 07](../pendientes/07-algo.md#el-problema).\n",
        })
        cerrar.cerrar(raiz, "07", "algo-resuelto", escribir=True)
        self.assertIn("algo-resuelto.md#el-problema",
                      self._leer(raiz, "notas/n.md"))

    def test_el_enlace_con_espacios_tambien_se_arrastra(self):
        """Un `%20` sin decodificar no coincide, y ese enlace se quedaría roto
        en silencio. Es el punto 1 del pendiente 33, por el otro lado."""
        raiz = self._repo({
            "pendientes/07-un algo.md": "# Algo\n",
            "notas/n.md": "Ver [el 07](../pendientes/07-un%20algo.md).\n",
        })
        cerrar.cerrar(raiz, "07", "algo-resuelto", escribir=True)
        self.assertIn("hecho/algo-resuelto.md", self._leer(raiz, "notas/n.md"))

    # -- lo que el pendiente cita ------------------------------------------

    def test_lo_que_el_archivo_citaba_se_recalcula(self):
        """La trampa que costó la primera corrida.

        Mover el archivo lo baja un nivel, así que **sus** `../` quedan cortos:
        `../base/x.md` pasaría a apuntar a `pendientes/base/x.md`, que no
        existe. El 53 llegó a `hecho/` con ocho rotos hacia afuera.
        """
        raiz = self._repo({
            "base/x.md": "# X\n",
            "pendientes/07-algo.md": "Ver [x](../base/x.md).\n",
        })
        cerrar.cerrar(raiz, "07", "algo-resuelto", escribir=True)
        texto = self._leer(raiz, "pendientes/hecho/algo-resuelto.md")
        self.assertIn("../../base/x.md", texto)
        self.assertEqual([], enlaces.validar_enlaces(raiz))

    def test_el_archivo_que_se_cita_a_si_mismo_no_se_enreda(self):
        raiz = self._repo({
            "pendientes/07-algo.md": "Yo soy [el 07](07-algo.md).\n",
        })
        cerrar.cerrar(raiz, "07", "algo-resuelto", escribir=True)
        self.assertIn("(algo-resuelto.md)",
                      self._leer(raiz, "pendientes/hecho/algo-resuelto.md"))

    # -- lo que no se toca --------------------------------------------------

    def test_no_toca_lo_externo_ni_los_anclajes_sueltos(self):
        raiz = self._repo({
            "pendientes/07-algo.md": "# Algo\n",
            "notas/n.md": ("[fuera](https://ejemplo.org/07-algo.md) y "
                           "[acá](#07-algo).\n"),
        })
        cerrar.cerrar(raiz, "07", "algo-resuelto", escribir=True)
        texto = self._leer(raiz, "notas/n.md")
        self.assertIn("https://ejemplo.org/07-algo.md", texto)
        self.assertIn("(#07-algo)", texto)

    def test_no_confunde_a_otro_pendiente_con_numero_parecido(self):
        raiz = self._repo({
            "pendientes/07-algo.md": "# Algo\n",
            "pendientes/70-otro.md": "# Otro\n",
            "notas/n.md": "[70](../pendientes/70-otro.md)\n",
        })
        cerrar.cerrar(raiz, "07", "algo-resuelto", escribir=True)
        self.assertIn("../pendientes/70-otro.md", self._leer(raiz, "notas/n.md"))

    # -- las salvaguardas ---------------------------------------------------

    def test_simular_no_escribe_nada(self):
        raiz = self._repo({
            "pendientes/07-algo.md": "# Algo\n",
            "notas/n.md": "[07](../pendientes/07-algo.md)\n",
        })
        _o, _d, tocados = cerrar.cerrar(raiz, "07", "algo-resuelto",
                                        escribir=False)
        self.assertTrue(tocados, "no dijo qué haría")
        self.assertTrue(os.path.isfile(
            os.path.join(raiz, "pendientes", "07-algo.md")),
            "movió el archivo sin --aplicar")
        self.assertIn("07-algo.md", self._leer(raiz, "notas/n.md"))

    def test_no_pisa_un_nombre_que_ya_existe(self):
        raiz = self._repo({
            "pendientes/07-algo.md": "# Algo\n",
            "pendientes/hecho/algo-resuelto.md": "# Ya estaba\n",
        })
        with self.assertRaises(SystemExit):
            cerrar.cerrar(raiz, "07", "algo-resuelto", escribir=True)
        self.assertIn("Ya estaba",
                      self._leer(raiz, "pendientes/hecho/algo-resuelto.md"))

    def test_avisa_si_el_numero_no_existe(self):
        raiz = self._repo({"pendientes/07-algo.md": "# Algo\n"})
        with self.assertRaises(SystemExit):
            cerrar.cerrar(raiz, "99", "lo-que-sea", escribir=True)

    def test_avisa_si_el_numero_esta_repetido(self):
        """Elegir uno en silencio movería el que no era."""
        raiz = self._repo({"pendientes/07-uno.md": "# Uno\n",
                           "pendientes/07-otro.md": "# Otro\n"})
        with self.assertRaises(SystemExit):
            cerrar.cerrar(raiz, "07", "lo-que-sea", escribir=True)


if __name__ == "__main__":
    unittest.main()
