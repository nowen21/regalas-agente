# -*- coding: utf-8 -*-
"""Pendiente 36 · Al cerrar, el estándar le avisa al proyecto que lo reportó.

`02·F24` fija siete pasos, y **el sexto no lo hacía nadie**: avisarle al
proyecto cuando la corrección está. Sin ese aviso, el séptimo —el pendiente del
proyecto queda abierto hasta confirmar— **deja pendientes abiertos para
siempre**, porque nadie vuelve a mirar el repositorio ajeno.

Se sabe que pasa porque ya pasó: tres cierres anteriores quedaron con el aviso
sin mandar.

Lo que estas pruebas fijan es lo que impide que el aviso haga daño: escribe
**un archivo de pendiente y nada más**, nunca toca código, no duplica si se
cierra dos veces, y no inventa una carpeta en un proyecto que no lleva backlog.
"""
import io
import os
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import cerrar   # noqa: E402

FICHA = """# Pendiente · Algo que se rompió

| | |
|---|---|
| **Proyecto de origen** | **%s** · `%s` |
| **A quién avisar al cerrar** | %s |

## El problema

Algo.
"""


class ElAvisoLlegaAQuienLoReporto(unittest.TestCase):

    def _proyectos(self, cuantos=3, con_backlog=True):
        """Proyectos de mentira, como los devuelve `proyectos_registrados()`."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        salida = []
        for i in range(1, cuantos + 1):
            ruta = os.path.join(tmp.name, "proy%d" % i)
            os.makedirs(ruta)
            if con_backlog:
                os.makedirs(os.path.join(ruta, "pendientes"))
            salida.append(("Proyecto %d" % i, ruta))
        return salida

    def _avisar(self, texto, proyectos, escribir=True):
        return cerrar.avisar("/raiz", texto, "/raiz/pendientes/hecho/algo.md",
                             "9.9.9", proyectos, "2026-01-02", escribir)

    def test_llega_al_de_origen_y_a_nadie_mas(self):
        proyectos = self._proyectos()
        texto = FICHA % ("Proyecto 2", proyectos[1][1], "al de origen")
        escritos = self._avisar(texto, proyectos)
        self.assertEqual(1, len(escritos))
        self.assertEqual("Proyecto 2", escritos[0][0])
        self.assertTrue(os.path.isfile(escritos[0][1]))
        # Los otros dos siguen sin nada.
        for nombre, ruta in (proyectos[0], proyectos[2]):
            self.assertEqual([], os.listdir(os.path.join(ruta, "pendientes")),
                             f"{nombre} recibió un aviso que no era suyo")

    def test_si_dice_todos_llega_a_todos(self):
        """`RN-06`: si el arreglo rige para todos, el aviso va a todos."""
        proyectos = self._proyectos()
        texto = FICHA % ("Proyecto 2", proyectos[1][1],
                         "a **todos** los proyectos instalados")
        self.assertEqual(3, len(self._avisar(texto, proyectos)))

    def test_no_duplica_si_se_cierra_dos_veces(self):
        proyectos = self._proyectos()
        texto = FICHA % ("Proyecto 1", proyectos[0][1], "al de origen")
        self._avisar(texto, proyectos)
        self.assertEqual([], self._avisar(texto, proyectos),
                         "el segundo cierre escribió otro aviso")
        self.assertEqual(1, len(os.listdir(
            os.path.join(proyectos[0][1], "pendientes"))))

    def test_el_aviso_dice_qué_versión_lo_trae(self):
        proyectos = self._proyectos()
        texto = FICHA % ("Proyecto 1", proyectos[0][1], "al de origen")
        _n, archivo = self._avisar(texto, proyectos)[0]
        with io.open(archivo, encoding="utf-8") as f:
            contenido = f.read()
        self.assertIn("9.9.9", contenido)
        self.assertIn("Algo que se rompió", contenido)
        self.assertIn("comprob", contenido.lower(),
                      "no dice que hay que comprobarlo antes de cerrar")

    def test_no_escribe_nada_fuera_de_la_carpeta_de_pendientes(self):
        """Escribe un pendiente. **Nunca toca código del proyecto.**"""
        proyectos = self._proyectos()
        texto = FICHA % ("Proyecto 1", proyectos[0][1], "al de origen")
        ruta = proyectos[0][1]
        antes = set(os.listdir(ruta))
        self._avisar(texto, proyectos)
        self.assertEqual(antes, set(os.listdir(ruta)),
                         "creó algo fuera de `pendientes/`")

    def test_el_proyecto_sin_backlog_no_recibe_nada(self):
        """No se le inventa una carpeta a un proyecto que no la lleva."""
        proyectos = self._proyectos(con_backlog=False)
        texto = FICHA % ("Proyecto 1", proyectos[0][1], "al de origen")
        self.assertEqual([], self._avisar(texto, proyectos))

    def test_sin_proyecto_de_origen_no_avisa_a_nadie(self):
        proyectos = self._proyectos()
        self.assertEqual([], self._avisar("# Pendiente\n\nSin ficha.\n", proyectos))

    def test_simular_no_escribe(self):
        proyectos = self._proyectos()
        texto = FICHA % ("Proyecto 1", proyectos[0][1], "al de origen")
        escritos = self._avisar(texto, proyectos, escribir=False)
        self.assertEqual(1, len(escritos), "no dijo a quién avisaría")
        self.assertEqual([], os.listdir(
            os.path.join(proyectos[0][1], "pendientes")),
            "escribió sin --aplicar")


class ElProyectoDeOrigenSeComprueba(unittest.TestCase):
    """`02·F24` · sin el nombre, el aviso no tiene a dónde ir."""

    def _backlog(self, ficha):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        carpeta = os.path.join(tmp.name, "pendientes")
        os.makedirs(carpeta)
        with io.open(os.path.join(carpeta, "07-algo.md"), "w",
                     encoding="utf-8") as f:
            f.write(ficha)
        return tmp.name

    def test_la_casilla_vacia_se_reporta(self):
        import pendientes
        raiz = self._backlog("# Algo\n\n| | |\n|---|---|\n"
                             "| **Proyecto de origen** |  |\n")
        self.assertEqual(1, len(pendientes.sin_proyecto_de_origen(raiz)))

    def test_el_marcador_sin_llenar_se_reporta(self):
        import pendientes
        raiz = self._backlog("# Algo\n\n| | |\n|---|---|\n"
                             "| **Proyecto de origen** | «Nombre» · `«ruta»` |\n")
        self.assertEqual(1, len(pendientes.sin_proyecto_de_origen(raiz)))

    def test_el_nombre_puesto_no_se_reporta(self):
        import pendientes
        raiz = self._backlog("# Algo\n\n| | |\n|---|---|\n"
                             "| **Proyecto de origen** | **shopnest-mesa** |\n")
        self.assertEqual([], pendientes.sin_proyecto_de_origen(raiz))

    def test_el_que_no_declara_origen_no_se_reporta(self):
        """La mayoría del backlog nace acá y no viene de ningún proyecto."""
        import pendientes
        raiz = self._backlog("# Algo\n\nSin ficha de origen.\n")
        self.assertEqual([], pendientes.sin_proyecto_de_origen(raiz))


if __name__ == "__main__":
    unittest.main()
