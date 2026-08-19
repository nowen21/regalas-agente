# -*- coding: utf-8 -*-
"""`EP-005 · HU-010` · Al escribir, llegan las reglas relacionadas.

**El defecto que esto cierra pasó el día que se construyó.** Se escribió una
frase en `02·F2` que chocaba con `02·F0` — la regla que `F2` cita en su propio
texto. El checklist tiene una fila para eso, la 17, y se selló en verde sin
mirar.

**El `CA-01` decía otra cosa hasta hoy:** *«llega completo el capítulo»*. Se
cambió, y el motivo importa — el capítulo `02` pesa 98 KB, y mandarlo entero
obliga a encontrar la relación uno mismo, que es exactamente lo que falla.
**Y solo trae a los vecinos del mismo capítulo**, cuando las relaciones cruzan
capítulos.

**Lo que la consulta no puede hacer:** encontrar una relación que nadie
declaró. `20·M7` y `20·M15` dejan de ser trámite por eso.
"""
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

# Los enganches viven en el adaptador desde el 2026-08-19, no en
# `validadores/`: `validadores/` es lo que sirve con cualquier agente.
ADAPTADOR = os.path.join(os.path.dirname(VALIDADORES),
                         "adaptadores", "claude-code")
sys.path.insert(0, ADAPTADOR)


import relacionadas   # noqa: E402

RAIZ = os.path.dirname(VALIDADORES)
F2 = os.path.join(RAIZ, "base", "02-flujo-de-trabajo", "reglas",
                  "F2-sin-especificacion-acordada-no-hay-codigo.md")


class LaConsulta(unittest.TestCase):

    def test_encuentra_la_regla_con_la_que_se_chocó(self):
        """`02·F0` tiene que salir al tocar `02·F2`. Es el caso que da origen
        a todo: la relación estaba escrita y nadie la miró."""
        rel = relacionadas.relacionadas(F2, RAIZ)
        citan = [q for lista in rel["citan"].values() for q in lista]
        self.assertIn("F0", citan)

    def test_cruza_capítulos(self):
        """Es la ventaja sobre mandar el capítulo entero: `00·ID3` y `13·DOC3`
        dependen de `02·F2` y viven en otros capítulos."""
        rel = relacionadas.relacionadas(F2, RAIZ)
        citan = [q for lista in rel["citan"].values() for q in lista]
        self.assertIn("ID3", citan)
        self.assertIn("DOC3", citan)

    def test_el_capítulo_dueño_sale_de_la_carpeta(self):
        """Duda 41: por carpeta y no por tipo de documento. El tipo hay que
        adivinarlo; la carpeta se lee de la ruta."""
        casos = {
            os.path.join(RAIZ, "base", "01-conducta.md"): "20",
            os.path.join(RAIZ, "pendientes", "x.md"): "02",
            os.path.join(RAIZ, "plantillas", "x.md"): "13",
        }
        for ruta, capitulo in casos.items():
            with self.subTest(ruta=os.path.basename(ruta)):
                self.assertEqual(capitulo, relacionadas._capitulo_de(ruta, RAIZ))

    def test_lo_que_no_gobierna_ningún_capítulo_devuelve_vacío(self):
        self.assertEqual({}, relacionadas.relacionadas(
            os.path.join(RAIZ, "notas", "README.md"), RAIZ))

    def test_el_aviso_nombra_la_fila_17(self):
        """Quien lo recibe tiene que saber para qué le llega."""
        texto = relacionadas.como_texto(relacionadas.relacionadas(F2, RAIZ), RAIZ)
        self.assertIn("fila 17", texto)

    def test_las_que_dependen_van_primero(self):
        """Cambiar una regla rompe a quien dependía de ella, y ese es el lado
        que no se mira. Lo que ella cita al menos está delante mientras se
        escribe."""
        texto = relacionadas.como_texto(relacionadas.relacionadas(F2, RAIZ), RAIZ)
        self.assertLess(texto.index("dependen de lo que está tocando"),
                        len(texto))

    def test_un_archivo_sin_reglas_dentro_no_dice_nada(self):
        """`base/README.md` lo gobierna el `20`, pero no vive ninguna regla ahí."""
        texto = relacionadas.como_texto(
            relacionadas.relacionadas(os.path.join(RAIZ, "base", "README.md"), RAIZ), RAIZ)
        self.assertEqual("", texto)


class ElEnganche(unittest.TestCase):

    def correr(self, sesion, ruta):
        datos = json.dumps({"session_id": sesion, "tool_input": {"file_path": ruta}})
        r = subprocess.run(
            [sys.executable, os.path.join(ADAPTADOR, "hook_relacionadas.py"),
             "--raiz", RAIZ],
            input=datos, capture_output=True, text=True,
            encoding="utf-8", errors="replace", timeout=120)
        return r

    def sesion(self):
        """Una sesión que nadie usó antes, para no chocar con la marca."""
        return "prueba-" + os.urandom(6).hex()

    def test_ca01_llega_al_escribir(self):
        r = self.correr(self.sesion(), F2)
        self.assertIn("SE RELACIONA", r.stdout)
        self.assertEqual(0, r.returncode)

    def test_ca02_no_se_repite_en_la_misma_sesión(self):
        s = self.sesion()
        self.assertIn("SE RELACIONA", self.correr(s, F2).stdout)
        self.assertEqual("", self.correr(s, F2).stdout.strip())

    def test_ca02_otra_sesión_sí_lo_recibe(self):
        """La marca es de la sesión, no del archivo: quien abre una sesión
        nueva no heredó lo que se avisó en otra."""
        self.correr(self.sesion(), F2)
        self.assertIn("SE RELACIONA", self.correr(self.sesion(), F2).stdout)

    def test_ca03_lo_que_no_le_toca_no_dispara_nada(self):
        r = self.correr(self.sesion(), os.path.join(RAIZ, "notas", "README.md"))
        self.assertEqual("", r.stdout.strip())
        self.assertEqual(0, r.returncode)

    def test_nunca_detiene(self):
        """Es información para decidir, no una comprobación. Lo que se
        comprueba tiene su validador y ese sí corta."""
        for ruta in (F2, os.path.join(RAIZ, "notas", "README.md"), "no-existe.md"):
            with self.subTest(ruta=os.path.basename(ruta)):
                self.assertEqual(0, self.correr(self.sesion(), ruta).returncode)

    def test_sin_json_no_hace_nada(self):
        r = subprocess.run(
            [sys.executable, os.path.join(ADAPTADOR, "hook_relacionadas.py"),
             "--raiz", RAIZ],
            input="no es json", capture_output=True, text=True,
            encoding="utf-8", errors="replace", timeout=60)
        self.assertEqual(0, r.returncode)


class ElLimiteDeclarado(unittest.TestCase):
    """Lo que la consulta **no** puede encontrar, escrito para que se vea."""

    def test_una_relación_no_declarada_no_aparece(self):
        """`20·M17` se relaciona con `00·ID7` —las dos hablan de escribir para
        que se entienda— y **no sale**, porque esa relación solo se argumentó
        en el sello y nunca se declaró en el cuerpo.

        **No es un defecto del programa: es el precio de que las relaciones se
        escriban a mano.** Por eso `20·M7` y `20·M15` dejan de ser trámite.
        """
        m17 = os.path.join(RAIZ, "base", "20-meta-reglas", "reglas",
                           "M17-la-entrada-del-registro-abre-en-castellano-llano.md")
        rel = relacionadas.relacionadas(m17, RAIZ)
        self.assertNotIn("ID7", rel["citadas"])


if __name__ == "__main__":
    unittest.main()
