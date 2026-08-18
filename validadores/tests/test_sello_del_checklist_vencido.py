# -*- coding: utf-8 -*-
"""Pendiente 52 · Un sello de checklist vencido se reporta.

Cada bloque de checklist cierra con esta frase:

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este
> resultado queda **anulado** y se vuelve a aplicar el checklist.

**La frase lo dice y nada lo comprobaba.** Una regla podía editarse y seguir
mostrando un CUMPLE aplicado contra otro texto, otra versión y otro día. Es
peor que no tener sello: el que no lo tiene al menos no engaña.

Se implementó la **salida B** del pendiente —la fecha del sello contra la del
último cambio— y no la A —una huella del texto—. La A detecta el cambio
exacto, pero obliga a recalcular el sello de las ~70 reglas que hoy están
bien: mucho riesgo para hacer visible algo que la fecha ya hace visible.

Su precio está asumido y dicho en el código: un cambio de una coma también
vence el sello, y un cambio sin confirmar no se ve.
"""
import os
import subprocess
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import metareglas   # noqa: E402

RAIZ = os.path.dirname(VALIDADORES)

SELLO = """> Regla del capítulo [`02 · Flujo`](../base.md).

## ZZ1 · Una regla de mentira

Exige algo.

```
INCORRECTO: así no
CORRECTO:   así sí
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../checklist.md) contra **v1.0.0**, el **%s**.

> Vale mientras el texto de arriba no cambie.
"""


class Regla:
    """Lo mínimo que `_sello_vencido` necesita, sin arrastrar el catálogo."""

    def __init__(self, archivo, texto, id="ZZ1"):
        self.archivo, self.texto, self.id = archivo, texto, id
        self.linea, self.derogada = 3, False


class ElSelloCaducaConElTexto(unittest.TestCase):

    def _repo(self, fecha_sello, tocar_despues):
        """Un repositorio de verdad: la fecha sale del control de versiones."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        raiz = tmp.name

        def git(*args, fecha=None):
            entorno = dict(os.environ,
                           GIT_AUTHOR_NAME="p", GIT_AUTHOR_EMAIL="p@p",
                           GIT_COMMITTER_NAME="p", GIT_COMMITTER_EMAIL="p@p")
            if fecha:
                entorno["GIT_AUTHOR_DATE"] = fecha + "T10:00:00"
                entorno["GIT_COMMITTER_DATE"] = fecha + "T10:00:00"
            subprocess.run(["git"] + list(args), cwd=raiz, env=entorno,
                           capture_output=True, text=True, timeout=30)

        git("init", "-q")
        ruta = os.path.join(raiz, "regla.md")
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(SELLO % fecha_sello)
        git("add", "-A")
        git("commit", "-qm", "nace", fecha=fecha_sello)

        if tocar_despues:
            with open(ruta, "a", encoding="utf-8") as f:
                f.write("\nUna línea más.\n")
            git("add", "-A")
            git("commit", "-qm", "se edita", fecha=tocar_despues)

        with open(ruta, encoding="utf-8") as f:
            return Regla(ruta, f.read())

    def test_editada_despues_del_sello_se_reporta(self):
        """El caso del pendiente: el texto cambió y el sello sigue diciendo CUMPLE."""
        regla = self._repo("2026-01-01", tocar_despues="2026-02-02")
        hallazgos = metareglas._sello_vencido(regla)
        self.assertEqual(1, len(hallazgos))
        self.assertIn("2026-01-01", hallazgos[0].mensaje)
        self.assertIn("2026-02-02", hallazgos[0].mensaje)

    def test_es_aviso_y_no_falla(self):
        """37 fallas de golpe volverían la corrida inservible y se ignoraría.

        Que el sello caducó no es que la regla esté mal escrita: es que hay
        que volver a mirarla. Eso se avisa, no se bloquea.
        """
        regla = self._repo("2026-01-01", tocar_despues="2026-02-02")
        self.assertEqual("AVISO", regla and
                         metareglas._sello_vencido(regla)[0].severidad)

    def test_sin_tocar_despues_no_se_reporta(self):
        regla = self._repo("2026-01-01", tocar_despues=None)
        self.assertEqual([], metareglas._sello_vencido(regla))

    def test_el_mismo_dia_no_vence(self):
        """Sellar y editar el mismo día es lo normal al escribir una regla."""
        regla = self._repo("2026-01-01", tocar_despues="2026-01-01")
        self.assertEqual([], metareglas._sello_vencido(regla))

    def test_sin_fecha_en_el_sello_no_se_inventa_nada(self):
        regla = Regla("cualquiera.md",
                      "### Checklist · **CUMPLE**\n\nAplicado contra **v1.0.0**.\n")
        self.assertEqual([], metareglas._sello_vencido(regla))

    def test_fuera_del_control_de_versiones_no_se_reporta(self):
        """Un hallazgo sin dato enseña a ignorar todos los demás."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        ruta = os.path.join(tmp.name, "suelta.md")
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(SELLO % "2026-01-01")
        with open(ruta, encoding="utf-8") as f:
            self.assertEqual([], metareglas._sello_vencido(Regla(ruta, f.read())))

    def test_la_derogada_no_se_reporta(self):
        regla = self._repo("2026-01-01", tocar_despues="2026-02-02")
        regla.derogada = True
        self.assertEqual([], metareglas._sello_vencido(regla))

    def test_la_fecha_sale_del_control_de_versiones_y_no_del_disco(self):
        """La fecha del sistema de archivos cambia con un clone, un checkout
        o un antivirus. Compararla daría vencidos falsos en cada máquina."""
        regla = self._repo("2026-01-01", tocar_despues=None)
        os.utime(regla.archivo, None)          # como si algo lo tocara ahora
        self.assertEqual([], metareglas._sello_vencido(regla))


class SobreElRepositorioDeVerdad(unittest.TestCase):

    def test_la_medicion_se_puede_repetir(self):
        """El pendiente decía «el número no se sabe hoy, y esa es media gracia».

        No se fija cuántos son —bajará a medida que se re-apliquen—, sino que
        la cuenta **se pueda hacer**: eso es lo que no existía.
        """
        vencidos = [h for r in metareglas.reglas(RAIZ)
                    for h in metareglas._sello_vencido(r)]
        self.assertTrue(all("se aplicó el" in h.mensaje for h in vencidos))
        self.assertTrue(all(h.severidad == "AVISO" for h in vencidos))


if __name__ == "__main__":
    unittest.main()
