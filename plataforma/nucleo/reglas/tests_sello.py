# -*- coding: utf-8 -*-
"""Los casos del plan de pruebas de la fase `I-EP-016-HU-003`.

**El caso que decide es el CP-003:** que la comparación por fechas **no** sea el
veredicto. Midiéndolo así, 185 de las 248 reglas vigentes salían con el sello
anulado, y el estándar dice que ninguna lo está. Un aviso falso de esa magnitud
enseña a ignorarlo.
"""
import io
import os
import shutil
import tempfile

from django.test import TestCase

from . import sello

CHECKLIST = u"""# 20 · Checklist de la regla

| # | Qué comprueba | Respaldo | Criterio |
|---|---|---|---|
| 1 | Es regla del estándar | `M13` | su destino es `base/` |
| 2 | No existe ya | `M12` | se buscó por concepto |
| 3 | La capa es la correcta | `M1` | capa 1 solo si es innegociable |
"""

CON_SELLO = u"""## M1 · Una regla

Su cuerpo.

---

### Checklist  ·  **CUMPLE**

Aplicado el checklist contra **v2.2.0**, el **2026-08-07**.

> Vale mientras el texto de arriba no cambie.
"""

SIN_SELLO = u"""## M2 · Otra regla

Su cuerpo, y nada más.
"""


class Base(TestCase):

    def setUp(self):
        self.raiz = tempfile.mkdtemp(prefix="prueba-sello-")
        ruta = os.path.join(self.raiz, "base", "20-meta-reglas")
        os.makedirs(ruta, exist_ok=True)
        with io.open(os.path.join(ruta, "checklist.md"), "w",
                     encoding="utf-8", newline="\n") as archivo:
            archivo.write(CHECKLIST)

    def tearDown(self):
        shutil.rmtree(self.raiz, ignore_errors=True)


class CP001SeLeenLasFilas(Base):

    def test_se_leen_las_filas_del_checklist(self):
        filas = sello.filas(self.raiz)
        self.assertEqual(len(filas), 3)
        self.assertEqual(filas[0]["numero"], 1)

    def test_cada_fila_trae_su_respaldo_y_su_criterio(self):
        una = sello.filas(self.raiz)[0]
        self.assertIn("M13", una["respaldo"])
        self.assertIn("base/", una["criterio"])

    def test_la_cabecera_de_la_tabla_no_es_una_fila(self):
        numeros = [una["numero"] for una in sello.filas(self.raiz)]
        self.assertEqual(numeros, [1, 2, 3])

    def test_sin_checklist_lo_dice(self):
        shutil.rmtree(os.path.join(self.raiz, "base"), ignore_errors=True)
        with self.assertRaises(sello.NoHayChecklist):
            sello.filas(self.raiz)


class CP002SeLeeElSello(TestCase):

    def test_una_regla_con_sello_lo_dice(self):
        self.assertTrue(sello.tiene_sello(CON_SELLO))

    def test_una_sin_sello_tambien(self):
        self.assertFalse(sello.tiene_sello(SIN_SELLO))

    def test_se_lee_contra_que_version_y_cuando(self):
        self.assertEqual(sello.contra_que(CON_SELLO), ("2.2.0", "2026-08-07"))

    def test_sin_sello_no_hay_version_ni_fecha(self):
        self.assertEqual(sello.contra_que(SIN_SELLO), ("", ""))


class CP003LasFechasNoSonElVeredicto(TestCase):
    """**El caso que decide.** 185 falsos positivos midiendo por fechas."""

    def test_una_regla_tocada_despues_parece_vencida(self):
        self.assertTrue(sello.parece_vencido(CON_SELLO, "2026-08-19"))

    def test_una_no_tocada_no_lo_parece(self):
        self.assertFalse(sello.parece_vencido(CON_SELLO, "2026-08-07"))

    def test_sin_sello_siempre_parece_vencida(self):
        self.assertTrue(sello.parece_vencido(SIN_SELLO, "2026-08-07"))

    def test_sin_fecha_de_cambio_tampoco_se_puede_afirmar(self):
        self.assertTrue(sello.parece_vencido(CON_SELLO, ""))

    def test_el_nombre_dice_que_no_es_el_veredicto(self):
        """Quien lo pregunte de verdad usa el del estándar."""
        self.assertTrue(hasattr(sello, "veredicto_del_estandar"))
        self.assertFalse(hasattr(sello, "esta_vencido"))


class CP004ElMoldeDelSello(TestCase):

    def test_con_todo_en_si_el_veredicto_es_cumple(self):
        texto = sello.molde_del_sello("37.2.0", "2026-09-01",
                                      {1: "si", 2: "si", 3: "si"})
        self.assertIn(u"**CUMPLE**", texto)
        self.assertIn(u"3 ✅", texto)

    def test_con_un_no_el_veredicto_es_no_cumple(self):
        texto = sello.molde_del_sello("37.2.0", "2026-09-01",
                                      {1: "si", 2: "no"})
        self.assertIn(u"**NO CUMPLE**", texto)

    def test_una_fila_que_no_aplica_lleva_su_motivo(self):
        """Sin motivo no se distingue de una que se saltó."""
        texto = sello.molde_del_sello(
            "37.2.0", "2026-09-01", {1: "si", 2: ("n/a", "no declara dependencia")})
        self.assertIn(u"N/A", texto)
        self.assertIn(u"no declara dependencia", texto)

    def test_una_que_no_aplica_sin_motivo_queda_marcada_como_hueco(self):
        texto = sello.molde_del_sello("37.2.0", "2026-09-01", {1: "n/a"})
        self.assertIn(u"«…»", texto)

    def test_el_sello_trae_su_aviso_de_caducidad(self):
        texto = sello.molde_del_sello("37.2.0", "2026-09-01", {1: "si"})
        self.assertIn(u"queda **anulado**", texto)
