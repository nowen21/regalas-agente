# -*- coding: utf-8 -*-
"""`EP-005·HU-023` · Cada tarea sabe qué reglas le aplican.

Se prueba sobre un repositorio de mentira en una carpeta temporal: los casos
cambian las tareas de una regla, y eso no se puede hacer sobre `base/`.

- CA-02: la línea `**Aplica a:**` no cuenta para el largo de la regla ni vence
  el sello de su checklist.
- CA-03: el mapa sale de las líneas, y cambia cuando cambian.
"""
import io
import os
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import citas         # noqa: E402
import mapa_tareas   # noqa: E402
import metareglas    # noqa: E402

LISTA = u"""# Las tareas del agente

| Tarea | Cuándo aplica | Palabras clave que la piden | Acciones que la señalan |
|---|---|---|---|
| `cambiar-codigo` | Se cambia código | | `escribe otro` |
| `escribir-documento` | Se escribe un documento | escriba | `escribe .md` |
| `tocar-git` | Se hace commit | suba | `comando git` |
"""

CUERPO = u"Nombra cada cosa por lo que hace, no por cómo se construyó."


def capitulo(aplica):
    """Un capítulo con una sola regla; `aplica` es su línea, o None."""
    partes = [u"# 07 · Calidad", u"", u"## Q1 · Nombra bien las cosas", u"",
              CUERPO, u"", u"```", u"INCORRECTO: x", u"CORRECTO:   y", u"```", u""]
    if aplica is not None:
        partes += [u"**Aplica a:** " + aplica, u""]
    partes += [u"---", u""]
    return u"\n".join(partes)


class Repo(unittest.TestCase):

    def repo(self, aplica):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        os.makedirs(os.path.join(tmp.name, "base"))
        self.escribir(tmp.name, "base/tareas.md", LISTA)
        self.escribir(tmp.name, "base/07-calidad.md", capitulo(aplica))
        return tmp.name

    def escribir(self, raiz, ruta, texto):
        with io.open(os.path.join(raiz, *ruta.split("/")), "w",
                     encoding="utf-8", newline="\n") as f:
            f.write(texto)

    def regla(self, raiz):
        return [r for r in metareglas.reglas(raiz) if r.id == "Q1"][0]


class LaLineaNoCambiaLaRegla(Repo):
    """CA-02."""

    def test_no_cuenta_para_el_largo(self):
        sin = self.regla(self.repo(None)).largo()
        con = self.regla(self.repo(u"cambiar-codigo, tocar-git")).largo()
        self.assertEqual(sin, con)
        self.assertEqual(len(CUERPO), con)

    def test_no_vence_el_sello(self):
        """El sello compara el texto sin las líneas que no son la regla."""
        sin = metareglas._sin_declaracion(capitulo(None))
        con = metareglas._sin_declaracion(capitulo(u"cambiar-codigo"))
        self.assertEqual(sin, con)


class ElMapaSaleDeLasReglas(Repo):
    """CA-03."""

    def test_una_regla_con_dos_tareas_sale_en_las_dos(self):
        mapa = mapa_tareas.armar(self.repo(u"cambiar-codigo, escribir-documento"))
        bloques = mapa.split(u"## `")
        codigo = [b for b in bloques if b.startswith(u"cambiar-codigo")][0]
        documento = [b for b in bloques if b.startswith(u"escribir-documento")][0]
        self.assertIn(u"07·Q1", codigo)
        self.assertIn(u"07·Q1", documento)

    def test_cambiar_la_tarea_mueve_la_regla(self):
        raiz = self.repo(u"cambiar-codigo")
        antes = mapa_tareas.armar(raiz)
        self.escribir(raiz, "base/07-calidad.md", capitulo(u"tocar-git"))
        despues = mapa_tareas.armar(raiz)
        self.assertNotEqual(antes, despues)
        git = [b for b in despues.split(u"## `") if b.startswith(u"tocar-git")][0]
        codigo = [b for b in despues.split(u"## `") if b.startswith(u"cambiar-codigo")][0]
        self.assertIn(u"07·Q1", git)
        self.assertNotIn(u"07·Q1", codigo)

    def test_la_tarea_sin_reglas_lo_dice(self):
        mapa = mapa_tareas.armar(self.repo(u"cambiar-codigo"))
        git = [b for b in mapa.split(u"## `") if b.startswith(u"tocar-git")][0]
        self.assertIn(u"Ninguna regla la declara todavía", git)

    def test_el_enlace_lleva_a_la_regla(self):
        mapa = mapa_tareas.armar(self.repo(u"cambiar-codigo"))
        ancla = citas.ancla(u"Q1 · Nombra bien las cosas")
        self.assertIn(u"(07-calidad.md#%s)" % ancla, mapa)

    def test_la_tarea_fuera_de_la_lista_no_entra_y_se_reporta(self):
        raiz = self.repo(u"cambiar-codigo, bailar")
        self.assertNotIn(u"bailar", mapa_tareas.armar(raiz))
        fuera = [(r.id, t) for r, t in mapa_tareas.sin_lista(raiz)]
        self.assertEqual([(u"Q1", u"bailar")], fuera)

    def test_escribir_deja_el_mapa_en_base(self):
        raiz = self.repo(u"cambiar-codigo")
        ruta = mapa_tareas.escribir(raiz)
        self.assertEqual(os.path.join(raiz, "base", "mapa-de-tareas.md"), ruta)
        with io.open(ruta, encoding="utf-8") as f:
            self.assertEqual(mapa_tareas.armar(raiz), f.read())


class ElValidadorDetectaLoQueNoCuadra(Repo):
    """CA-04."""

    def al_dia(self, aplica):
        raiz = self.repo(aplica)
        mapa_tareas.escribir(raiz)
        return raiz

    def test_con_todo_al_dia_pasa(self):
        self.assertEqual([], mapa_tareas.validar(self.al_dia(u"cambiar-codigo")))

    def test_la_regla_sin_tareas_falla(self):
        h = mapa_tareas.validar(self.al_dia(None))
        self.assertEqual(1, len(h))
        self.assertIn(u"07·Q1", h[0].mensaje)
        self.assertIn(u"Aplica a", h[0].mensaje)

    def test_la_tarea_fuera_de_la_lista_falla(self):
        h = mapa_tareas.validar(self.al_dia(u"bailar"))
        self.assertEqual(1, len(h))
        self.assertIn(u"`bailar`", h[0].mensaje)

    def test_el_mapa_viejo_falla(self):
        raiz = self.al_dia(u"cambiar-codigo")
        self.escribir(raiz, "base/07-calidad.md", capitulo(u"tocar-git"))
        h = mapa_tareas.validar(raiz)
        self.assertTrue(any(u"el mapa no coincide" in x.mensaje for x in h))
        # `CA-10` · Los archivos de reglas por tarea también quedaron viejos.
        viejos = {os.path.basename(x.archivo) for x in h
                  if u"reglas de esta tarea no coinciden" in x.mensaje}
        self.assertIn(u"cambiar-codigo.md", viejos)
        self.assertIn(u"tocar-git.md", viejos)

    def test_el_archivo_que_sobra_falla(self):
        """`CA-10` · Un archivo por tarea que ninguna tarea produce se reporta."""
        raiz = self.al_dia(u"cambiar-codigo")
        self.escribir(raiz, "base/reglas-por-tarea/bailar.md", u"# Bailar\n")
        h = mapa_tareas.validar(raiz)
        self.assertEqual(1, len(h))
        self.assertIn(u"sobra", h[0].mensaje)

    def test_la_regla_completa_llega_al_archivo_de_su_tarea(self):
        """`CA-10` · El archivo de la tarea trae la regla entera, con su ejemplo."""
        raiz = self.al_dia(u"cambiar-codigo")
        texto = io.open(os.path.join(raiz, "base", "reglas-por-tarea", "cambiar-codigo.md"),
                        encoding="utf-8").read()
        self.assertIn(u"## Q1 · Nombra bien las cosas", texto)
        self.assertIn(CUERPO, texto)
        self.assertIn(u"INCORRECTO: x", texto)

    def test_la_regla_derogada_no_se_reporta(self):
        raiz = self.repo(None)
        derogada = capitulo(None).replace(
            u"## Q1 · Nombra bien las cosas",
            u"## Q1 · Nombra bien las cosas `[DEROGADA en 1.0.0 → ver Q2]`")
        self.escribir(raiz, "base/07-calidad.md", derogada)
        mapa_tareas.escribir(raiz)
        self.assertEqual([], mapa_tareas.validar(raiz))

    def test_sin_lista_de_tareas_no_reporta_nada(self):
        """Un proyecto no tiene reglas propias en `base/`."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.assertEqual([], mapa_tareas.validar(tmp.name))

    def test_el_pre_push_lo_corre(self):
        import instalar
        self.assertIn(u"ejecutable tareas; do", instalar.PLANTILLA_PRE_PUSH)


if __name__ == "__main__":
    unittest.main()
