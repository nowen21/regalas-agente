# -*- coding: utf-8 -*-
"""`EP-027·HU-002` · Pruebas de la fase A: las reglas pasan a las tablas sin perder nada (CP-001 a CP-003)."""
from collections import Counter

from django.test import SimpleTestCase, TestCase

from core.comun import Proyecto as Carpeta
from core.historia.models import Cambio
from core.historia.registro import quien_y_por_que

from . import molde
from .importar import importar
from .models import FALTA_EL_PROGRAMA, NO_VALIDABLE, VALIDABLE, Dependencia, Documento, Regla, ReglaTarea
from .reglas import QUIEN_NOTA, pasar_todo, validables


def _pasar():
    with quien_y_por_que(quien="prueba", motivo="prueba"):
        return pasar_todo(Carpeta.estandar())


def _renglones(texto):
    return Counter(l for l in texto.replace("\r\n", "\n").split("\n") if l.strip() and l.strip() != "---")


class ConElEstandarPasado(TestCase):

    @classmethod
    def setUpTestData(cls):
        importar(Carpeta.estandar())
        cls.antes = {d.ruta: d.contenido for d in Documento.objects.all()}
        cls.bloques = sum(len(molde.partir(t)) for r, t in cls.antes.items()
                          if r.startswith("base/") and not r.startswith("base/reglas-por-tarea/"))
        cls.total, cls.cambiados = _pasar()

    def regla(self, codigo):
        return Regla.objects.get(codigo=codigo, proyecto__isnull=True)


class TodasQuedanEnLasTablas(ConElEstandarPasado):
    """CP-001."""

    def test_una_fila_por_regla_con_capitulo_tareas_y_ejemplo(self):
        self.assertEqual(self.bloques, self.total)
        self.assertEqual(self.bloques, Regla.objects.count())
        f1 = self.regla("F1")
        self.assertEqual("02 · Flujo de trabajo", f1.capitulo.nombre)
        self.assertEqual("F", f1.capitulo.prefijo)
        self.assertEqual(["trabajar-cadena", "recibir-pedido"], [a.tarea.nombre for a in f1.aplica.all()])
        self.assertIn("la diseño desde cero", f1.ejemplo_incorrecto)
        self.assertEqual("CUMPLE", f1.sello_resultado)

    def test_las_dependencias_unidas_a_su_destino(self):
        f0 = self.regla("F0")
        dependencias = {(d.tipo, d.codigo): d.destino for d in f0.dependencias.all()}
        self.assertEqual({("depende de", "F2"), ("depende de", "DOC15"), ("depende de", "DOC16")}, set(dependencias))
        self.assertEqual(self.regla("F2"), dependencias[("depende de", "F2")])

    def test_validable_del_registro(self):
        g2 = self.regla("G2")
        self.assertEqual((VALIDABLE, "commits.py"), (g2.validable, g2.validador))
        self.assertEqual(FALTA_EL_PROGRAMA, self.regla("F2").validable)
        self.assertEqual(NO_VALIDABLE, self.regla("C1").validable)


class NadaSePierde(ConElEstandarPasado):
    """CP-002."""

    def test_el_texto_es_el_de_antes_sin_las_notas_del_sello(self):
        notas = Counter()
        for cambio in Cambio.objects.filter(tabla="estandar.regla", quien=QUIEN_NOTA):
            notas.update(_renglones(cambio.motivo))
        sobra, falta = Counter(), Counter()
        for documento in Documento.objects.filter(ruta__startswith="base/").exclude(
                ruta__startswith="base/reglas-por-tarea/"):
            antes, despues = _renglones(self.antes[documento.ruta]), _renglones(documento.contenido)
            sobra.update(despues - antes)
            falta.update(antes - despues)
        self.assertEqual(Counter(), sobra)
        self.assertEqual(notas, falta)

    def test_la_nota_queda_en_la_historia_de_su_regla_con_su_fecha(self):
        c1 = self.regla("C1")
        self.assertNotIn("Corregida el 2026-08-22", c1.sello)
        nota = Cambio.objects.get(tabla="estandar.regla", fila=str(c1.pk), quien=QUIEN_NOTA,
                                  motivo__startswith="**Corregida el 2026-08-22")
        self.assertEqual("2026-08-22", nota.fecha.date().isoformat())


class PasarDosVecesNoDuplica(ConElEstandarPasado):
    """CP-003."""

    def test_las_mismas_filas_y_notas(self):
        cuentas = lambda: (Regla.objects.count(), ReglaTarea.objects.count(), Dependencia.objects.count(),
                           Cambio.objects.filter(quien=QUIEN_NOTA).count())
        antes = cuentas()
        total, cambiados = _pasar()
        self.assertEqual(antes, cuentas())
        self.assertEqual([], cambiados)


class ElRegistroDeValidables(SimpleTestCase):

    def test_la_lista_de_arriba_manda(self):
        texto = ("## ✅ Ya son validadores (HECHAS)\n\n| Regla | Validador | Comprueba |\n|---|---|---|\n"
                 "| `G2` · `04·S4` | `commits.py` | algo |\n\n## 🟡 Validables, faltan (PENDIENTE)\n\n"
                 "| Regla | Qué |\n|---|---|\n| `F2` | algo |\n\n## 🔴 No validables\n\n"
                 "- **`01`:** `C1`, `C2`. `G2` salió de esta lista.\n")
        salida = validables(texto)
        self.assertEqual((VALIDABLE, "commits.py"), salida["G2"])
        self.assertEqual((VALIDABLE, "commits.py"), salida["S4"])
        self.assertEqual(FALTA_EL_PROGRAMA, salida["F2"][0])
        self.assertEqual(NO_VALIDABLE, salida["C1"][0])
