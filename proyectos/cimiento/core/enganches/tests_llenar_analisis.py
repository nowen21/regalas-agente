"""`EP-025·HU-033` · Cimiento llena los análisis sin guiones sueltos.

Plan de pruebas: `PP-EP025-HU033-A`. Un proyecto temporal con un pendiente, el
resumen donde nació su hallazgo y la plantilla real del estándar.
"""
import io
import os
import shutil
import tempfile
import unittest

from django.core.management import call_command
from django.core.management.base import CommandError

from ..comun import Proyecto
from .analisis_en_curso import AnalisisEnCurso
from .llenar_analisis import llenar_encabezado

RESUMEN = """# Resumen

## Hallazgos de esta sesión

### H-1 · El primer problema

| Campo | Valor |
|---|---|
| Qué pasó | Algo se repetía |

### H-2 · Otro problema

| Campo | Valor |
|---|---|
| Qué pasó | Otra cosa |

---
"""

PENDIENTE = """# Pendiente: el primer problema

| | |
|---|---|
| **De dónde sale** | [H-1 · El primer problema](../../sesion.md), en el resumen del día |

## El problema

Algo se repetía.
"""


def escribir(ruta, texto):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def leer(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return f.read()


class ConUnPendiente(unittest.TestCase):
    def setUp(self):
        self.raiz = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.raiz, True)
        dia = os.path.join(self.raiz, "historico-chat", "resumenes", "2026-01-01")
        escribir(os.path.join(dia, "sesion.md"), RESUMEN)
        self.carpeta = os.path.join(dia, "pendientes", "5-el-primer-problema")
        escribir(os.path.join(self.carpeta, "pendiente.md"), PENDIENTE)
        self.plantilla = leer(os.path.join(Proyecto.estandar(), "plantillas", "analisis.md"))


class CP001ElPrimerAnalisisQuedaConSuEncabezado(ConUnPendiente):
    def test_rutas_pendiente_y_hallazgo(self):
        ruta = AnalisisEnCurso(self.raiz, base=False).nuevo_analisis(self.carpeta)
        texto = leer(ruta)
        for marca in ("«RUTA-ESTANDAR»", "«copia del pendiente»", "«copia del hallazgo»", "analisis-«N+1»"):
            self.assertNotIn(marca, texto)
        self.assertIn("Algo se repetía.", texto)
        self.assertIn("### H-1 · El primer problema", texto)
        self.assertNotIn("H-2", texto)
        self.assertIn("`analisis-2.md`", texto)


class CP002ElSegundoDejaElHallazgoAlAgente(ConUnPendiente):
    def test_el_segundo_analisis(self):
        texto = llenar_encabezado(self.plantilla, self.carpeta, 2, Proyecto.estandar())
        self.assertIn("Algo se repetía.", texto)
        self.assertIn("«copia del hallazgo»", texto)
        self.assertNotIn("«RUTA-ESTANDAR»", texto)

    def test_sin_hallazgo_enlazado_se_crea_igual(self):
        escribir(os.path.join(self.carpeta, "pendiente.md"), PENDIENTE.replace("[H-1 · El primer problema](../../sesion.md)", "una conversación"))
        texto = llenar_encabezado(self.plantilla, self.carpeta, 1, Proyecto.estandar())
        self.assertIn("«copia del hallazgo»", texto)
        self.assertIn("una conversación", texto)


class CP003ElComandoGuardaUnaSeccion(ConUnPendiente):
    def test_reemplaza_solo_esa_seccion(self):
        ruta = AnalisisEnCurso(self.raiz, base=False).nuevo_analisis(self.carpeta)
        antes = leer(ruta)
        cuerpo = os.path.join(self.raiz, "texto.md")
        escribir(cuerpo, "1. Se decidió algo (turno 3).\n\nSiguen abiertas: ninguna.\n")
        call_command("analisis", "seccion", ruta, "Lo acordado", archivo=cuerpo, stdout=io.StringIO())
        despues = leer(ruta)
        acordado = despues[despues.index("## Lo acordado"):despues.index("## Lo que aportó cada parte")]
        self.assertIn("## Lo acordado\n\n1. Se decidió algo (turno 3).", acordado)
        self.assertNotIn("«tema»", acordado)
        corte = despues.index("## Lo que aportó cada parte")
        self.assertEqual(antes[antes.index("## Lo que aportó cada parte"):], despues[corte:])
        self.assertEqual(antes[:antes.index("## Lo acordado")], despues[:despues.index("## Lo acordado")])


class CP004UnaSeccionQueNoExiste(ConUnPendiente):
    def test_falla_y_dice_cuales_hay(self):
        ruta = AnalisisEnCurso(self.raiz, base=False).nuevo_analisis(self.carpeta)
        antes = leer(ruta)
        cuerpo = os.path.join(self.raiz, "texto.md")
        escribir(cuerpo, "algo\n")
        with self.assertRaises(CommandError) as error:
            call_command("analisis", "seccion", ruta, "No existe", archivo=cuerpo, stdout=io.StringIO())
        self.assertIn("Lo acordado", str(error.exception))
        self.assertEqual(antes, leer(ruta))
