# -*- coding: utf-8 -*-
"""Los casos del plan de pruebas de `EP-022` — `F-036` y `F-037`.

**El caso que decide es el CP-001:** que ninguna pantalla responda sin haber
entrado. Se prueba **recorriendo todas las rutas registradas**, no una lista
escrita a mano: una lista a mano se queda corta el día que alguien agregue una
pantalla, y ese es justo el día en que hay que enterarse.

**Y el que más protege es el CP-004:** que el agente no pueda aprobar. Un agente
que aprueba lo que él mismo construyó vuelve la aprobación un trámite.
"""
import io
import os
import shutil
import tempfile

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import get_resolver

from nucleo.acceso import core, grupos, para_probar
from nucleo.acceso.middleware import ABIERTAS, sin_entrar
from nucleo.aprobaciones import core as aprobaciones
from nucleo.proyectos.models import Proyecto


def rutas_registradas():
    """Todas las direcciones de la plataforma, con un valor de ejemplo.

    Se sacan del propio enrutador. **No se escriben a mano**: una lista a mano
    envejece en silencio.
    """
    salida = []
    for patron in get_resolver().url_patterns:
        cruda = str(patron.pattern)
        if "<" in cruda:
            # Se rellenan los huecos con algo que exista, para no confundir un
            # 404 con un «no ha entrado».
            cruda = cruda.replace("<str:identificador>", "de-prueba")
            cruda = cruda.replace("<str:que>", "desconectar")
            cruda = cruda.replace("<str:cuando>", "2026-09-02-000000")
        salida.append("/" + cruda)
    return salida


class Base(TestCase):

    def setUp(self):
        self.cliente = Client()
        self.raiz = tempfile.mkdtemp(prefix="prueba-acceso-")
        Proyecto.objects.create(
            identificador="de-prueba", nombre="De prueba",
            ruta_codigo=self.raiz, ruta_normalizada=self.raiz.lower(),
            conectado="conectado")

    def tearDown(self):
        shutil.rmtree(self.raiz, ignore_errors=True)


class CP001SinEntrarNoSeVeNada(Base):
    """`CA-01` de `F-036`. **El caso que decide.**"""

    def test_ninguna_ruta_responde_sin_haber_entrado(self):
        abiertas = 0
        for ruta in rutas_registradas():
            respuesta = self.cliente.get(ruta)
            if sin_entrar(ruta):
                abiertas += 1
                self.assertNotEqual(302, respuesta.status_code, ruta)
                continue
            self.assertEqual(
                302, respuesta.status_code,
                "%s respondió sin haber entrado" % ruta)
            self.assertIn("/entrar/", respuesta["Location"], ruta)
        # Lo que está abierto es corto y se cuenta: si crece, esto lo dice.
        self.assertEqual(len(ABIERTAS), abiertas)

    def test_solo_entrar_y_salir_estan_abiertas(self):
        self.assertEqual(("/entrar/", "/salir/"), ABIERTAS)

    def test_los_estaticos_si_responden_porque_son_de_esa_pantalla(self):
        self.assertTrue(sin_entrar("/static/adminlte/adminlte.min.css"))

    def test_una_ruta_nueva_nace_protegida(self):
        """La razón de que esto sea middleware y no un decorador por vista."""
        self.assertFalse(sin_entrar("/una-pantalla-que-alguien-agregue/"))

    def test_habiendo_entrado_si_responden(self):
        para_probar.como_usuario(self.cliente)
        for ruta in ("/", "/tablero/", "/proyecto/de-prueba/"):
            self.assertEqual(200, self.cliente.get(ruta).status_code, ruta)


class CP002EntrarYSalir(Base):
    """`CA-02` y `CA-03` de `F-036`."""

    def cuenta(self):
        return para_probar._cuenta("quien-manda", grupos.USUARIO)

    def test_entrar_lleva_a_donde_se_iba(self):
        self.cuenta()
        respuesta = self.cliente.get("/tablero/")
        self.assertIn("next=/tablero/", respuesta["Location"])

        entrada = self.cliente.post(
            "/entrar/", {"username": "quien-manda",
                         "password": para_probar.CLAVE, "next": "/tablero/"})
        self.assertEqual("/tablero/", entrada["Location"])

    def test_la_contrasena_correcta_abre_la_sesion(self):
        self.cuenta()
        self.cliente.post("/entrar/", {"username": "quien-manda",
                                       "password": para_probar.CLAVE})
        self.assertEqual(200, self.cliente.get("/").status_code)

    def test_un_intento_fallido_no_dice_cual_dato_estuvo_mal(self):
        self.cuenta()
        for datos in ({"username": "quien-manda", "password": "no-es"},
                      {"username": "no-existe", "password": para_probar.CLAVE}):
            cuerpo = self.cliente.post("/entrar/", datos).content.decode("utf-8")
            self.assertIn("La cuenta o la contraseña no son correctas", cuerpo)
            self.assertNotIn("no existe", cuerpo.replace(
                "no se dice cuál", "").replace("confirmaría qué cuentas", ""))

    def test_la_contrasena_no_aparece_en_la_respuesta(self):
        self.cuenta()
        cuerpo = self.cliente.post(
            "/entrar/", {"username": "quien-manda",
                         "password": para_probar.CLAVE}).content.decode("utf-8")
        self.assertNotIn(para_probar.CLAVE, cuerpo)

    def test_la_contrasena_no_se_guarda_en_claro(self):
        cuenta = self.cuenta()
        self.assertNotIn(para_probar.CLAVE, cuenta.password)
        self.assertTrue(cuenta.check_password(para_probar.CLAVE))

    def test_salir_cierra_la_sesion(self):
        para_probar.como_usuario(self.cliente)
        self.cliente.post("/salir/")
        self.assertEqual(302, self.cliente.get("/tablero/").status_code)


class CP003LosDosGruposYSusPermisos(Base):
    """`CA-04` de `F-037`."""

    def test_son_dos_grupos_y_no_cuatro(self):
        puestos = grupos.poner_al_dia()
        self.assertEqual({grupos.USUARIO, grupos.AGENTE}, set(puestos))

    def test_el_usuario_puede_todo(self):
        quien = para_probar._cuenta("manda", grupos.USUARIO)
        for clave, _n, _p in grupos.SOLO_DEL_USUARIO:
            self.assertTrue(core.puede(quien, clave), clave)

    def test_el_agente_no_puede_las_cuatro(self):
        quien = para_probar._cuenta("agente", grupos.AGENTE)
        for clave, _n, _p in grupos.SOLO_DEL_USUARIO:
            self.assertFalse(core.puede(quien, clave), clave)

    def test_el_agente_si_puede_escribir_documentos(self):
        quien = para_probar._cuenta("agente", grupos.AGENTE)
        for clave, _n in grupos.DE_LOS_DOS:
            self.assertTrue(core.puede(quien, clave), clave)

    def test_poner_al_dia_se_puede_correr_muchas_veces(self):
        grupos.poner_al_dia()
        grupos.poner_al_dia()
        quien = para_probar._cuenta("manda", grupos.USUARIO)
        self.assertTrue(core.puede(quien, "aprobar_documento"))


class CP004ElAgenteNoAprueba(Base):
    """**El caso que más protege.** `CA-05` y `CA-06`."""

    def documento(self):
        ruta = os.path.join(self.raiz, "uno.md")
        with io.open(ruta, "w", encoding="utf-8", newline="") as abierto:
            abierto.write(u"# Uno\n")
        return "uno.md"

    def test_el_agente_no_puede_aprobar_y_se_dice_por_que(self):
        para_probar._cuenta("el-agente", grupos.AGENTE)
        with self.assertRaises(core.NoPuede) as fallo:
            aprobaciones.aprobar("de-prueba", self.documento(), "el-agente")
        dicho = str(fallo.exception)
        self.assertIn("aprobar_documento", dicho)
        self.assertIn("vuelve la aprobación un trámite", dicho)
        self.assertIn(grupos.USUARIO, dicho)

    def test_el_usuario_si_puede(self):
        para_probar._cuenta("manda", grupos.USUARIO)
        aprobada = aprobaciones.aprobar("de-prueba", self.documento(), "manda")
        self.assertEqual("manda", aprobada.quien)

    def test_una_cuenta_que_no_existe_se_rechaza(self):
        grupos.poner_al_dia()
        with self.assertRaises(core.NoPuede) as fallo:
            aprobaciones.aprobar("de-prueba", self.documento(), "nadie")
        self.assertIn("no hay ninguna cuenta", str(fallo.exception))
        self.assertIn("sin probarlo", str(fallo.exception))

    def test_no_queda_ninguna_aprobacion_de_las_rechazadas(self):
        from nucleo.aprobaciones.models import Aprobacion
        para_probar._cuenta("el-agente", grupos.AGENTE)
        documento = self.documento()
        for quien in ("el-agente", "nadie"):
            try:
                aprobaciones.aprobar("de-prueba", documento, quien)
            except core.NoPuede:
                pass
        self.assertEqual(0, Aprobacion.objects.count())

    def test_el_superusuario_puede_aunque_no_este_en_ningun_grupo(self):
        Cuenta = get_user_model()
        grupos.poner_al_dia()
        Cuenta.objects.create_superuser(username="raiz", password="x" * 12)
        aprobada = aprobaciones.aprobar("de-prueba", self.documento(), "raiz")
        self.assertEqual("raiz", aprobada.quien)
