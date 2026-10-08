# -*- coding: utf-8 -*-
"""`EP-027·HU-006` · Pruebas de la fase B: las reglas del proyecto en la tabla (CP-001 a CP-003)."""
import io
import os
import tempfile

from django.contrib.auth.models import Group, User
from django.core.management import call_command
from django.test import TestCase

from core.cuentas.permisos import ADMINISTRADOR, CONSULTA
from core.historia.models import PROYECTO, Cambio, Version
from core.proyectos.models import Proyecto

from .models import Regla
from .reglas import ARCHIVO_DEL_PROYECTO

CON_GRUPOS = """# Reglas propias del proyecto  ·  `[CAPA 3]`

## Precedencia (dónde mandan estas reglas)

Texto de la plantilla.

## 1. Comportamiento obligatorio del agente

### P1 · Todo monto se guarda en centavos

Un monto viaja como entero de centavos (concreta `03·D1`).

```
INCORRECTO: guardar 12.5
CORRECTO:   guardar 1250
```

## 2. Base de datos

### P2 · Cada tabla lleva su dueño

La tabla dice a qué finca pertenece.

**Autoriza escribir:** `documentacion/fincas/**`
"""

EN_DOS = """# Reglas propias del proyecto — RNI

## RP1 · Commits sin atribución de IA

El commit no nombra a la IA.
"""


class ConUnProyecto(TestCase):

    def setUp(self):
        self.carpeta = tempfile.TemporaryDirectory()
        self.addCleanup(self.carpeta.cleanup)
        self.proyecto = Proyecto.objects.create(nombre="Finca", ruta=os.path.abspath(self.carpeta.name))
        self.escribir(CON_GRUPOS)

    def escribir(self, texto):
        archivo = os.path.join(self.carpeta.name, *ARCHIVO_DEL_PROYECTO.split("/"))
        os.makedirs(os.path.dirname(archivo), exist_ok=True)
        with open(archivo, "w", encoding="utf-8") as f:
            f.write(texto)
        return archivo

    def pasar(self, *extra):
        salida = io.StringIO()
        call_command("pasar_reglas_proyecto", "--proyecto", self.carpeta.name, *extra, stdout=salida)
        return salida.getvalue()

    def reglas(self):
        return list(Regla.objects.filter(proyecto=self.proyecto, apartada=False).order_by("orden"))


class PasanALaTabla(ConUnProyecto):
    """CP-001."""

    def test_con_su_proyecto_su_grupo_y_su_version(self):
        antes = Version.objects.filter(ambito=PROYECTO, proyecto=self.proyecto).count()
        self.pasar()
        p1, p2 = self.reglas()
        self.assertEqual(("P1", "Todo monto se guarda en centavos", "1. Comportamiento obligatorio del agente"),
                         (p1.codigo, p1.titulo, p1.grupo))
        self.assertEqual("guardar 12.5", p1.ejemplo_incorrecto)
        self.assertEqual("2. Base de datos", p2.grupo)
        self.assertIn("documentacion/fincas/**", p2.autoriza_escribir)
        self.assertEqual(antes + 1, Version.objects.filter(ambito=PROYECTO, proyecto=self.proyecto).count())

    def test_en_dos_almohadillas_tambien(self):
        self.escribir(EN_DOS)
        self.pasar()
        self.assertEqual(["RP1"], [r.codigo for r in self.reglas()])

    def test_pasar_dos_veces_no_duplica(self):
        self.pasar()
        self.pasar()
        self.assertEqual(2, Regla.objects.filter(proyecto=self.proyecto).count())


class ElArchivoQuedaEnLaHistoria(ConUnProyecto):
    """CP-002."""

    def test_se_guarda_entero_y_se_borra(self):
        archivo = os.path.join(self.carpeta.name, *ARCHIVO_DEL_PROYECTO.split("/"))
        self.pasar("--borrar")
        self.assertFalse(os.path.exists(archivo))
        cambio = Cambio.objects.filter(tabla="proyectos.proyecto", fila=str(self.proyecto.pk)).latest("id")
        self.assertEqual(CON_GRUPOS, cambio.antes[ARCHIVO_DEL_PROYECTO])


class SeVenYSeCambian(ConUnProyecto):
    """CP-003."""

    def setUp(self):
        super().setUp()
        self.pasar()
        self.admin = User.objects.create_user("admin", password="una-clave-larga-1")
        self.admin.groups.add(Group.objects.get_or_create(name=ADMINISTRADOR)[0])
        self.mira = User.objects.create_user("mira", password="una-clave-larga-1")
        self.mira.groups.add(Group.objects.get_or_create(name=CONSULTA)[0])
        self.url = "/estandar/proyecto/%d/reglas/" % self.proyecto.pk

    def test_la_pantalla(self):
        self.client.force_login(self.admin)
        html = self.client.get(self.url).content.decode()
        for texto in ("Todo monto se guarda en centavos", "1. Comportamiento obligatorio del agente", ">P2<"):
            self.assertIn(texto, html)
        self.assertIn("Reglas de cada proyecto", self.client.get("/estandar/").content.decode())

    def test_ver_regla(self):
        indice, una = io.StringIO(), io.StringIO()
        call_command("ver_regla", "--proyecto", self.carpeta.name, stdout=indice)
        call_command("ver_regla", "P1", "--proyecto", self.carpeta.name, stdout=una)
        self.assertIn("P1 · Todo monto se guarda en centavos", indice.getvalue())
        self.assertIn("P2 · Cada tabla lleva su dueño", indice.getvalue())
        self.assertTrue(una.getvalue().startswith("## P1 · Todo monto se guarda en centavos"))
        self.assertIn("INCORRECTO: guardar 12.5", una.getvalue())

    def test_cambiar_desde_la_pantalla(self):
        self.client.force_login(self.admin)
        texto = self.client.get(self.url).context["texto"]
        texto = texto.replace("Un monto viaja como entero de centavos", "Un monto viaja en centavos")
        texto = texto[:texto.index("## 2. Base de datos")]
        datos = {"contenido": texto, "version_obliga": "no", "version_agrega": "no", "version_motivo": "prueba"}
        self.client.post(self.url, datos)
        p1 = Regla.objects.get(proyecto=self.proyecto, codigo="P1")
        self.assertIn("Un monto viaja en centavos", p1.exigencia)
        self.assertTrue(Regla.objects.get(proyecto=self.proyecto, codigo="P2").apartada)

    def test_la_consulta_no_cambia(self):
        self.client.force_login(self.mira)
        respuesta = self.client.post(self.url, {"contenido": "# nada\n"})
        self.assertEqual(403, respuesta.status_code)
        self.assertEqual(2, len(self.reglas()))


class UnCodigoRepetidoNoPasa(ConUnProyecto):
    """CP-001: lo que no pasa se dice, y nada se pierde."""

    def test_no_pasa_ni_se_borra(self):
        archivo = self.escribir(CON_GRUPOS.replace("### P2 ·", "### P1 ·"))
        errores = io.StringIO()
        call_command("pasar_reglas_proyecto", "--proyecto", self.carpeta.name, "--borrar",
                     stdout=io.StringIO(), stderr=errores)
        self.assertIn("P1", errores.getvalue())
        self.assertTrue(os.path.exists(archivo))
        self.assertFalse(Regla.objects.filter(proyecto=self.proyecto).exists())
