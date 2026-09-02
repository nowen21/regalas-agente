# -*- coding: utf-8 -*-
"""El `.env` de la máquina, y el puerto que sale de él.

**El archivo existía y nadie lo leía.** `.env.example` decía «copiar a `.env` y
llenar», y los ajustes lo buscaban en el ambiente del proceso, que es otra cosa.
Quien lo copiara y lo llenara no cambiaba nada, y no había cómo notarlo.

**El caso que decide es el CP-002:** que el ambiente gane sobre el archivo. Si
ganara el archivo, poner una variable para una corrida no serviría, y entender
por qué cuesta media hora.
"""
import io
import os
import shutil
import tempfile

from django.test import TestCase

from config import ambiente
import manage


class Base(TestCase):

    def setUp(self):
        self.carpeta = tempfile.mkdtemp(prefix="prueba-ambiente-")
        self.antes = dict(os.environ)

    def tearDown(self):
        shutil.rmtree(self.carpeta, ignore_errors=True)
        os.environ.clear()
        os.environ.update(self.antes)

    def archivo(self, texto):
        ruta = os.path.join(self.carpeta, ".env")
        with io.open(ruta, "w", encoding="utf-8", newline="") as abierto:
            abierto.write(texto)
        return ruta


class CP001ElArchivoSeLee(Base):

    def test_lo_declarado_queda_en_el_ambiente(self):
        os.environ.pop("PUERTO", None)
        puestas = ambiente.cargar(self.archivo(u"PUERTO=8015\n"))
        self.assertEqual({"PUERTO": "8015"}, puestas)
        self.assertEqual("8015", os.environ["PUERTO"])

    def test_los_comentarios_y_las_lineas_vacias_no_cuentan(self):
        os.environ.pop("UNA", None)
        puestas = ambiente.cargar(self.archivo(
            u"# un comentario\n\n   \nUNA=dos\n"))
        self.assertEqual({"UNA": "dos"}, puestas)

    def test_una_clave_sin_valor_no_se_pone(self):
        os.environ.pop("VACIA", None)
        self.assertEqual({}, ambiente.cargar(self.archivo(u"VACIA=\n")))
        self.assertNotIn("VACIA", os.environ)

    def test_las_comillas_se_quitan(self):
        os.environ.pop("CON", None)
        ambiente.cargar(self.archivo(u'CON="entre comillas"\n'))
        self.assertEqual("entre comillas", os.environ["CON"])

    def test_un_valor_con_signo_igual_no_se_parte_dos_veces(self):
        os.environ.pop("CLAVE", None)
        ambiente.cargar(self.archivo(u"CLAVE=a=b=c\n"))
        self.assertEqual("a=b=c", os.environ["CLAVE"])

    def test_sin_archivo_no_pasa_nada_y_no_revienta(self):
        self.assertEqual({}, ambiente.cargar(
            os.path.join(self.carpeta, "no-existe")))


class CP002ElAmbienteGanaSobreElArchivo(Base):
    """**El caso que decide.** Pisar una variable para una corrida tiene que servir."""

    def test_lo_que_ya_esta_en_el_ambiente_no_se_pisa(self):
        os.environ["PUERTO"] = "9999"
        puestas = ambiente.cargar(self.archivo(u"PUERTO=8015\n"))
        self.assertEqual({}, puestas)
        self.assertEqual("9999", os.environ["PUERTO"])


class CP003ElPuertoSaleDelArchivo(Base):
    """Lo que salió al levantarla: tres servidores viejos en el mismo puerto."""

    def test_runserver_sin_puerto_usa_el_declarado(self):
        os.environ["PUERTO"] = "8015"
        self.assertEqual(["manage.py", "runserver", "8015"],
                         manage.con_el_puerto(["manage.py", "runserver"]))

    def test_runserver_con_puerto_no_se_le_discute(self):
        os.environ["PUERTO"] = "8015"
        self.assertEqual(["manage.py", "runserver", "9000"],
                         manage.con_el_puerto(["manage.py", "runserver", "9000"]))

    def test_las_banderas_no_cuentan_como_puerto(self):
        os.environ["PUERTO"] = "8015"
        self.assertEqual(["manage.py", "runserver", "8015", "--noreload"],
                         manage.con_el_puerto(
                             ["manage.py", "runserver", "--noreload"]))

    def test_sin_puerto_declarado_queda_el_de_fabrica(self):
        os.environ.pop("PUERTO", None)
        self.assertEqual(manage.PUERTO_DE_FABRICA, manage.puerto_declarado())

    def test_ninguna_otra_orden_se_toca(self):
        os.environ["PUERTO"] = "8015"
        for orden in (["manage.py", "test"], ["manage.py", "migrate"],
                      ["manage.py"]):
            self.assertEqual(orden, manage.con_el_puerto(orden))
