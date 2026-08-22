# -*- coding: utf-8 -*-
"""`80` · Un commit que mezcla el trabajo de dos sesiones avisa.

**El caso que lo hizo falta.** El 2026-08-22 dos sesiones trabajaron a la vez
sobre este repositorio. Una hizo `git add` de todo el árbol y commiteó: se llevó
un validador a medio corregir, con el criterio que reprobaba documentos que
estaban bien, y estuvo ocho minutos publicado.

**No se comprueba de quién es el commit.** `git` no sabe qué sesión lo lanza, y
no hace falta: si lo que entra lo tocaron dos sesiones distintas, alguien está
publicando trabajo ajeno. Un commit legítimo sale de una sola conversación.

**La mitad de estas pruebas son de lo que NO tiene que avisar**, que es la que
falta siempre acá. Un aviso que salta en cada commit se apaga en una tarde.
"""
import io
import os
import shutil
import sys
import tempfile
import time
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import sesiones                    # noqa: E402
from comun import AVISO            # noqa: E402


class DosSesionesNoSePisan(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.tmp, "historico-chat"))
        self.entrando = []
        self._real = sesiones.preparados
        sesiones.preparados = lambda raiz=None: list(self.entrando)

    def tearDown(self):
        sesiones.preparados = self._real
        shutil.rmtree(self.tmp, ignore_errors=True)

    def toca(self, sesion, *relativos):
        for rel in relativos:
            ruta = os.path.join(self.tmp, *rel.split("/"))
            carpeta = os.path.dirname(ruta)
            if carpeta and not os.path.isdir(carpeta):
                os.makedirs(carpeta)
            with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
                f.write(u"x\n")
            sesiones.anotar(self.tmp, sesion, ruta)

    # ── lo que sí tiene que avisar ───────────────────────────────────────

    def test_el_commit_que_mezcla_dos_sesiones_avisa(self):
        self.toca("aaa111", "validadores/plantillas.py")
        self.toca("bbb222", "CHANGELOG.md")
        self.entrando = ["validadores/plantillas.py", "CHANGELOG.md"]

        h = sesiones.validar_preparados(self.tmp)
        self.assertEqual(1, len(h), "mezclar dos sesiones tiene que avisar")
        self.assertEqual(AVISO, h[0].severidad,
                         "avisa y no detiene: retomar lo ajeno a veces es lo correcto")
        self.assertIn(u"2 sesiones", h[0].mensaje)

    def test_el_aviso_nombra_algun_archivo_para_saber_por_donde_empezar(self):
        self.toca("aaa111", "mio.md")
        self.toca("bbb222", "ajeno.py")
        self.entrando = ["mio.md", "ajeno.py"]

        h = sesiones.validar_preparados(self.tmp)
        self.assertIn(u"ajeno.py", h[0].mensaje,
                      "sin un archivo concreto, el aviso no dice qué sacar")

    # ── lo que NO tiene que avisar ───────────────────────────────────────

    def test_una_sola_sesion_no_avisa(self):
        self.toca("aaa111", "uno.md", "dos.md")
        self.entrando = ["uno.md", "dos.md"]
        self.assertEqual([], sesiones.validar_preparados(self.tmp))

    def test_un_commit_vacio_no_avisa(self):
        self.toca("aaa111", "uno.md")
        self.toca("bbb222", "dos.md")
        self.entrando = []
        self.assertEqual([], sesiones.validar_preparados(self.tmp),
                         "sin nada preparado no hay nada que mezclar")

    def test_lo_que_toco_otra_sesion_pero_no_entra_al_commit_no_avisa(self):
        self.toca("aaa111", "mio.md")
        self.toca("bbb222", "ajeno.py")
        self.entrando = ["mio.md"]
        self.assertEqual([], sesiones.validar_preparados(self.tmp),
                         "lo que no entra al commit no lo publica nadie")

    def test_una_sesion_vieja_ya_no_cuenta(self):
        """Doce horas sin escribir y la sesión ya no está viva.

        Sin esto, el registro de la semana pasada haría saltar el aviso en cada
        commit, y un aviso que salta siempre se apaga.
        """
        self.toca("vieja1", "ajeno.py")
        ruta = os.path.join(self.tmp, sesiones.CARPETA, "vieja1.txt")
        viejo = time.time() - sesiones.VIGENCIA - 60
        os.utime(ruta, (viejo, viejo))

        self.toca("aaa111", "mio.md")
        self.entrando = ["mio.md", "ajeno.py"]
        self.assertEqual([], sesiones.validar_preparados(self.tmp))

    def test_el_mismo_archivo_tocado_por_las_dos_no_alcanza_para_callar(self):
        """Que las dos hayan tocado el índice no vuelve suyo lo demás."""
        self.toca("aaa111", "indice.md", "mio.md")
        self.toca("bbb222", "indice.md", "ajeno.py")
        self.entrando = ["indice.md", "mio.md", "ajeno.py"]
        self.assertEqual(1, len(sesiones.validar_preparados(self.tmp)))

    # ── el registro ──────────────────────────────────────────────────────

    def test_no_se_anota_lo_que_es_de_otro_proyecto(self):
        otro = tempfile.mkdtemp()
        try:
            ajeno = os.path.join(otro, "cosa.md")
            with io.open(ajeno, "w", encoding="utf-8") as f:
                f.write(u"x\n")
            sesiones.anotar(self.tmp, "aaa111", ajeno)
            self.assertEqual({}, sesiones.registros(self.tmp))
        finally:
            shutil.rmtree(otro, ignore_errors=True)

    def test_sin_identificador_de_sesion_no_se_anota_nada(self):
        self.toca("", "uno.md")
        self.assertEqual({}, sesiones.registros(self.tmp),
                         "una herramienta que no dé el identificador no debe romper nada")

    def test_el_mismo_archivo_dos_veces_se_anota_una(self):
        self.toca("aaa111", "uno.md")
        self.toca("aaa111", "uno.md")
        self.assertEqual({"aaa111": {"uno.md"}}, sesiones.registros(self.tmp))


if __name__ == "__main__":
    unittest.main()
