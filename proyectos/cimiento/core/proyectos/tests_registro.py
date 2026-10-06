# -*- coding: utf-8 -*-
"""Los proyectos que existen entran al registro, y el instalador registra.

Ciclo 2 de la fase de la HU-003 (D-01): la base vieja se reinició y los
proyectos se traen de `plantillas/proyectos.md`.
"""
import io
import os
import shutil
import tempfile
from unittest import mock

from django.core.management import call_command
from django.test import TestCase

from core.proyectos import registro
from core.proyectos.models import Proyecto


class ConCarpetas(TestCase):
    def setUp(self):
        # Fuera de la carpeta temporal del sistema: allá el registro no trae nada.
        self.raiz = tempfile.mkdtemp(dir=os.path.dirname(os.path.abspath(__file__)))
        self.addCleanup(shutil.rmtree, self.raiz, True)
        self.uno = os.path.join(self.raiz, "uno")
        self.dos = os.path.join(self.raiz, "dos")
        os.makedirs(self.uno)
        os.makedirs(self.dos)

    def md(self, filas):
        ruta = os.path.join(self.raiz, "proyectos.md")
        texto = "# Proyectos\n\n| Proyecto | Ruta | Scope de memoria | Stack |\n|---|---|---|---|\n"
        texto += "".join(f"| {n} | `{r}` | `proyecto:x` | por detectar |\n" for n, r in filas)
        io.open(ruta, "w", encoding="utf-8").write(texto)
        return ruta


class LosProyectosQueExistenEntran(ConCarpetas):
    def test_trae_las_filas_cuya_carpeta_existe(self):
        md = self.md([("Uno · módulo", self.uno), ("Dos", self.dos),
                      ("Fantasma", os.path.join(self.raiz, "no-existe"))])
        self.assertEqual(registro.traer_de_proyectos_md(Proyecto, md), ["Uno · módulo", "Dos"])
        uno = Proyecto.objects.get(nombre="Uno · módulo")
        self.assertEqual(uno.ruta, self.uno)
        self.assertTrue(uno.carpeta_claude)
        self.assertEqual(uno.ajuste("limite_enganche"), 2000)

    def test_repetir_no_duplica_ni_pisa(self):
        md = self.md([("Uno", self.uno)])
        registro.traer_de_proyectos_md(Proyecto, md)
        Proyecto.objects.filter(nombre="Uno").update(nombre="Uno editado")
        self.assertEqual(registro.traer_de_proyectos_md(Proyecto, self.md([("Uno", self.uno.upper())])), [])
        self.assertEqual(Proyecto.objects.get().nombre, "Uno editado")

    def test_la_carpeta_temporal_no_entra(self):
        temporal = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, temporal, True)
        self.assertEqual(registro.traer_de_proyectos_md(Proyecto, self.md([("Prueba", temporal)])), [])

    def test_sin_archivo_no_trae_nada(self):
        self.assertEqual(registro.traer_de_proyectos_md(Proyecto, os.path.join(self.raiz, "no.md")), [])

    def test_la_base_de_pruebas_arranca_vacia(self):
        self.assertFalse(Proyecto.objects.exists())

    def test_la_lista_es_la_del_estandar(self):
        estandar = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))))))
        self.assertEqual(registro.proyectos_md(), os.path.join(estandar, "plantillas", "proyectos.md"))


class ElInstaladorRegistra(ConCarpetas):
    def registrar(self, nombre, ruta):
        salida = io.StringIO()
        call_command("registrar", "--nombre", nombre, "--ruta", ruta, "--scope", "proyecto:x", stdout=salida)
        return salida.getvalue().strip()

    def test_registra_y_repetir_no_cambia(self):
        self.assertEqual(self.registrar("uno", self.uno), "registrado")
        self.assertEqual(self.registrar("otro nombre", self.uno.upper()), "ya estaba registrado")
        self.assertEqual(Proyecto.objects.get().nombre, "uno")

    def test_el_nombre_ocupado_lleva_numero(self):
        self.registrar("app", self.uno)
        self.registrar("app", self.dos)
        self.assertEqual(Proyecto.objects.get(ruta=self.dos).nombre, "app (2)")


class ElInstaladorLlamaACimiento(ConCarpetas):
    def test_llama_la_orden_de_cimiento_y_no_la_de_interfaz(self):
        import core.validadores  # noqa: F401  (antes del instalador: el ciclo del pendiente 121)
        from core.herramientas.instalar import Instalador

        instalador = Instalador.__new__(Instalador)
        instalador.estandar = self.raiz
        instalador.registro = os.path.join(self.raiz, "plantillas", "proyectos.md")
        cimiento = os.path.join(self.raiz, "proyectos", "cimiento")
        os.makedirs(os.path.join(cimiento, ".venv", "Scripts"))
        python = os.path.join(cimiento, ".venv", "Scripts", "python.exe")
        io.open(python, "w").close()
        io.open(os.path.join(cimiento, "manage.py"), "w").close()
        with mock.patch.object(Instalador, "_registro_real", return_value=True), \
                mock.patch("core.herramientas.instalar.subprocess.run") as correr:
            correr.return_value.returncode = 0
            self.assertTrue(instalador.registrar_en_cimiento("uno", self.uno, "proyecto:uno"))
        orden = correr.call_args[0][0]
        self.assertEqual(orden[:3], [python, os.path.join(cimiento, "manage.py"), "registrar"])
