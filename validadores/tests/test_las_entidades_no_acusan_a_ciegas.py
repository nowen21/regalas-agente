# -*- coding: utf-8 -*-
"""`01` · Lo que no se puede leer no se acusa treinta y una veces.

**Medido contra un proyecto real el 2026-08-18**, que es lo que el pendiente 01
siempre pidió y nunca se había hecho. `validar.py entidades` devolvió **31
avisos diciendo que ninguna migración creaba las tablas declaradas** — y las
migraciones estaban ahí, creándolas. Este validador solo sabe leer `.php` y
`.sql`, y las de ese proyecto son de otro formato.

**Un validador que reporta de más se termina apagando**, y apagado figura como
cubierto. Vale más decir «no sé leer esto» una vez que acusar treinta y una.

**Y no se arregla aprendiendo ese formato**: sería atar la base a una tecnología,
que es lo que `20·M3` prohíbe. Se arregla **sabiendo lo que no se sabe**.
"""
import io
import os
import subprocess
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import entidades      # noqa: E402
from comun import FALLA      # noqa: E402

DOMINIO = """# Dominio

## Entidades

| Entidad | Tabla | Clave natural | Inmutable |
|---|---|---|---|
| Factura | facturas | numero | sí |
| Cliente | clientes | documento | no |
"""


def proyecto(migracion, contenido=u"-- nada\n"):
    """Un proyecto de mentira con su declaración y una migración."""
    tmp = tempfile.TemporaryDirectory()
    r = tmp.name
    subprocess.run(["git", "init", "-q", r], capture_output=True)
    os.makedirs(os.path.join(r, ".agente"))
    with io.open(os.path.join(r, ".agente", "dominio.md"), "w", encoding="utf-8") as f:
        f.write(DOMINIO)
    destino = os.path.join(r, *migracion.split("/"))
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with io.open(destino, "w", encoding="utf-8") as f:
        f.write(contenido)
    subprocess.run(["git", "-C", r, "add", "-A"], capture_output=True)
    return tmp


class LoQueNoSePuedeLeerSeDiceUnaVez(unittest.TestCase):

    def test_con_migraciones_ilegibles_sale_un_solo_aviso(self):
        """**El caso medido:** dos entidades declaradas, y un aviso — no dos."""
        tmp = proyecto("database/migrations/0001_initial.py", u"# migración\n")
        self.addCleanup(tmp.cleanup)
        hallazgos = entidades.validar(tmp.name)
        self.assertEqual(1, len(hallazgos))
        self.assertIn("no se pueden mirar", hallazgos[0].mensaje)

    def test_no_dice_que_las_tablas_falten(self):
        """**Es la mitad que importa.** Decir «faltan» es acusar; decir «no las
        veo» es informar, y lo segundo es lo cierto."""
        tmp = proyecto("database/migrations/0001_initial.py", u"# migración\n")
        self.addCleanup(tmp.cleanup)
        mensajes = " ".join(h.mensaje for h in entidades.validar(tmp.name))
        self.assertNotIn("ninguna migración la crea", mensajes)
        self.assertIn("No es que falten", mensajes)

    def test_nunca_es_una_falla(self):
        tmp = proyecto("database/migrations/0001_initial.py", u"# migración\n")
        self.addCleanup(tmp.cleanup)
        self.assertEqual([], [h for h in entidades.validar(tmp.name)
                              if h.severidad == FALLA])


class ConMigracionesLegiblesSigueAcusando(unittest.TestCase):
    """**El arreglo no puede apagar el validador.** Si las migraciones se
    pueden leer y la tabla no está, eso sí es un hallazgo."""

    def test_la_tabla_que_de_verdad_falta_se_reporta(self):
        tmp = proyecto("database/migrations/0001_crear.sql",
                       u"CREATE TABLE clientes (id INT, documento VARCHAR(20));\n")
        self.addCleanup(tmp.cleanup)
        mensajes = " ".join(h.mensaje for h in entidades.validar(tmp.name))
        self.assertIn("facturas", mensajes)
        self.assertNotIn("no se pueden mirar", mensajes)

    def test_sin_ninguna_migracion_tampoco_se_calla(self):
        """Sin migraciones de ningún tipo no hay excusa: las tablas no están."""
        tmp = proyecto("README.md", u"# proyecto\n")
        self.addCleanup(tmp.cleanup)
        mensajes = " ".join(h.mensaje for h in entidades.validar(tmp.name))
        self.assertIn("ninguna migración la crea", mensajes)


class ElPermisoDeAnularSeEncuentraCuandoEsta(unittest.TestCase):
    """`EP-004·HU-010` · El patrón del permiso reemplaza su marcador.

    **El caso.** El patrón se declara como `anular_<recurso>` y la
    comprobación arma su expresión reemplazando el marcador **sobre el
    texto ya escapado**. Hasta Python 3.6 `re.escape` escapaba todo lo que
    no fuera alfanumérico, así que `<recurso>` salía como `\<recurso\>` y
    el reemplazo encajaba. Desde 3.7 solo escapa lo que significa algo en
    una expresión, y los ángulos no.

    **El reemplazo dejó de ocurrir en silencio.** La expresión quedaba
    literal, no encontraba ningún permiso, y toda entidad inmutable de todo
    proyecto recibía el reclamo de `15·IM5`. Un reclamo que sale siempre es
    el que se aprende a ignorar.
    """

    def test_el_permiso_escrito_en_el_codigo_se_encuentra(self):
        tmp = proyecto("src/ventas/permisos.py",
                       u'PERMISOS = ["anular_factura"]\n')
        with tmp:
            import declaracion
            d = declaracion.leer_declaracion(tmp.name)
            hallados = entidades.recursos_con_permiso(
                tmp.name, "anular_<recurso>", d)
        self.assertIn("factura", hallados,
                      "el marcador no se reemplazó: la expresión quedó literal")

    def test_el_patron_sin_marcador_no_busca_nada(self):
        """La contraprueba. Un patrón sin `<recurso>` no puede decir de qué
        entidad es el permiso, así que devuelve vacío en vez de adivinar."""
        tmp = proyecto("src/ventas/permisos.py",
                       u'PERMISOS = ["anular_factura"]\n')
        with tmp:
            import declaracion
            d = declaracion.leer_declaracion(tmp.name)
            hallados = entidades.recursos_con_permiso(
                tmp.name, "anular_factura", d)
        self.assertEqual(set(), hallados)


if __name__ == "__main__":
    unittest.main(verbosity=2)
