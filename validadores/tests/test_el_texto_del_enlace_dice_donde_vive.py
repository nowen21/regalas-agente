# -*- coding: utf-8 -*-
"""Pendiente 18 · `13·DOC14` — el texto del enlace dice dónde vive el archivo.

La regla pide dos partes: como **texto**, la ruta desde la raíz —para saber
dónde vive sin abrirlo—; como **destino**, la ruta relativa. El estándar la
incumplía en **1031 enlaces** de 347 archivos: casi todos dicen el nombre del
archivo y no dónde está.

**El destino no se toca nunca.** Ya funciona, y tocarlo es la única forma de
romper un enlace que hoy anda. Lo que se reescribe es el texto.

Dos exclusiones **declaradas**, no olvidadas:

- Las transcripciones de `historico-chat/`, que se copian literales del chat.
- `prompts/`, que son palabras del usuario: reescribirle un enlace ahí es
  editarle la frase.

Y una que la propia regla permite: el enlace de **texto descriptivo**
—`[la guía]`— se queda como está.
"""
import io
import os
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import comun      # noqa: E402
import enlaces    # noqa: E402


class Repo(unittest.TestCase):
    """Un repositorio de mentira con los archivos que haga falta."""

    def repo(self, archivos):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        for rel, contenido in archivos.items():
            ruta = os.path.join(tmp.name, *rel.split("/"))
            carpeta = os.path.dirname(ruta)
            if carpeta and not os.path.isdir(carpeta):
                os.makedirs(carpeta)
            with io.open(ruta, "w", encoding="utf-8") as f:
                f.write(contenido)
        return tmp.name

    def leer(self, raiz, rel):
        with io.open(os.path.join(raiz, *rel.split("/")), encoding="utf-8") as f:
            return f.read()


class ElTextoPasaADecirLaRuta(Repo):

    def test_el_que_sube_carpetas(self):
        raiz = self.repo({
            "base/x.md": u"# X\n",
            "doc/a/b.md": u"Ver [x.md](../../base/x.md).\n",
        })
        enlaces.reparar_formato(raiz, escribir=True)
        self.assertIn(u"[base/x.md](../../base/x.md)",
                      self.leer(raiz, "doc/a/b.md"))

    def test_el_destino_no_se_toca(self):
        """Es lo único que puede romper un enlace que hoy funciona."""
        raiz = self.repo({
            "base/x.md": u"# X\n",
            "doc/a/b.md": u"Ver [x.md](../../base/x.md).\n",
        })
        enlaces.reparar_formato(raiz, escribir=True)
        self.assertIn(u"](../../base/x.md)", self.leer(raiz, "doc/a/b.md"))

    def test_el_texto_entre_comillas_invertidas_no_se_ve__limite_conocido(self):
        """**Punto ciego declarado:** ``[`x.md`](destino)`` no se toca.

        `comun.enlaces()` borra los trozos entre comillas invertidas antes de
        buscar enlaces —para no leer los ejemplos de cómo se escribe uno— y con
        eso el texto se queda vacío: deja de parecer una ruta, y ni el que
        reporta ni el que arregla lo ven.

        **No es un defecto de esta fase**, y quitarlo cambiaría cómo se leen
        los enlaces en todo el repositorio. Queda escrito acá para que se vea,
        en vez de descubrirlo dentro de un año preguntándose por qué el número
        no llegaba a cero.
        """
        raiz = self.repo({
            "base/x.md": u"# X\n",
            "doc/b.md": u"Ver [`x.md`](../base/x.md).\n",
        })
        self.assertEqual([], enlaces.reparar_formato(raiz, escribir=True))
        self.assertIn(u"[`x.md`](../base/x.md)", self.leer(raiz, "doc/b.md"))

    def test_la_carpeta_conserva_su_barra(self):
        raiz = self.repo({
            "doc/area/README.md": u"# A\n",
            "doc/b.md": u"Ver [area/](area/).\n",
        })
        enlaces.reparar_formato(raiz, escribir=True)
        self.assertIn(u"[doc/area/](area/)", self.leer(raiz, "doc/b.md"))


class LoQueNoSeToca(Repo):
    """Las exclusiones, cada una con su motivo escrito."""

    def test_el_texto_descriptivo_se_queda(self):
        """La propia regla lo permite cuando quien lee ya sabe dónde vive."""
        raiz = self.repo({
            "base/x.md": u"# X\n",
            "doc/b.md": u"Ver [la guía](../base/x.md).\n",
        })
        self.assertEqual([], enlaces.reparar_formato(raiz, escribir=True))
        self.assertIn(u"[la guía](../base/x.md)", self.leer(raiz, "doc/b.md"))

    def test_las_palabras_del_usuario_se_quedan(self):
        """`prompts/` es lo que el usuario dijo. Reescribirlo es editarle la frase."""
        raiz = self.repo({
            "base/x.md": u"# X\n",
            "prompts/p.md": u"Ver [x.md](../base/x.md).\n",
        })
        self.assertEqual([], enlaces.reparar_formato(raiz, escribir=True))
        self.assertIn(u"[x.md](../base/x.md)", self.leer(raiz, "prompts/p.md"))

    def test_el_que_ya_esta_bien_no_se_reescribe(self):
        raiz = self.repo({
            "base/x.md": u"# X\n",
            "doc/b.md": u"Ver [base/x.md](../base/x.md).\n",
        })
        self.assertEqual([], enlaces.reparar_formato(raiz))

    def test_el_enlace_externo_no_se_toca(self):
        raiz = self.repo({"doc/b.md": u"Ver [algo.md](https://ejemplo/algo.md).\n"})
        self.assertEqual([], enlaces.reparar_formato(raiz))

    def test_simular_no_escribe(self):
        raiz = self.repo({
            "base/x.md": u"# X\n",
            "doc/b.md": u"Ver [x.md](../base/x.md).\n",
        })
        self.assertEqual(1, len(enlaces.reparar_formato(raiz)))
        self.assertIn(u"[x.md](../base/x.md)", self.leer(raiz, "doc/b.md"))


class ElQueReportaYElQueArreglaMiranIgual(Repo):
    """Si se separan, el arreglo deja hallazgos vivos o toca lo que nadie pidió."""

    ARCHIVOS = {
        "base/x.md": u"# X\n",
        "doc/a/b.md": u"[x.md](../../base/x.md) y [la guía](../../base/x.md)\n",
        "doc/a/c.md": u"[base/x.md](../../base/x.md)\n",
        "prompts/p.md": u"[x.md](../base/x.md)\n",
    }

    def test_lo_que_se_repara_es_lo_que_se_reporta(self):
        raiz = self.repo(self.ARCHIVOS)
        antes = len([h for h in enlaces.validar_formato(raiz)
                     if "prompts" not in comun.relativo(h.archivo)])
        reparados = sum(n for _, n in enlaces.reparar_formato(raiz, escribir=True))
        self.assertEqual(antes, reparados)

    def test_despues_de_reparar_no_queda_nada_que_reportar(self):
        raiz = self.repo(self.ARCHIVOS)
        enlaces.reparar_formato(raiz, escribir=True)
        quedan = [comun.relativo(h.archivo) for h in enlaces.validar_formato(raiz)
                  if "prompts" not in comun.relativo(h.archivo)]
        self.assertEqual([], quedan)


class ElVecinoDeLaMismaCarpetaSeDejaAparte(Repo):
    """`DOC14` no distingue el caso, y aplicarla al vecino la vuelve ilegible.

    La regla pide la ruta desde la raíz *«para saber dónde vive sin abrirlo»*.
    Para el archivo de al lado ese propósito ya está cumplido — quien lee está
    parado ahí— y exigirla igual da un texto de unos 130 caracteres para
    nombrar al vecino.

    **Son 747 de los 1031 del estándar.** Se probó aplicarlo y el resultado
    fue una tabla donde cada celda ocupaba cinco líneas para decir
    `plan_trabajo.md`. Se revirtió: **si distinguir el caso es cambiar la
    regla, y eso lo decide el usuario.**
    """

    ARCHIVOS = {
        "doc/a/plan.md": u"# Plan\n",
        "base/x.md": u"# X\n",
        "doc/a/README.md": u"[plan.md](plan.md) y [x.md](../../base/x.md)\n",
    }

    def test_por_defecto_el_vecino_no_se_toca(self):
        raiz = self.repo(self.ARCHIVOS)
        enlaces.reparar_formato(raiz, escribir=True)
        leido = self.leer(raiz, "doc/a/README.md")
        self.assertIn(u"[plan.md](plan.md)", leido)
        self.assertIn(u"[base/x.md](../../base/x.md)", leido)

    def test_pidiéndolo_expresamente_sí_se_toca(self):
        """La puerta queda abierta para el día que se decida."""
        raiz = self.repo(self.ARCHIVOS)
        enlaces.reparar_formato(raiz, escribir=True, incluir_vecinos=True)
        self.assertIn(u"[doc/a/plan.md](plan.md)",
                      self.leer(raiz, "doc/a/README.md"))


class ElEstandarNoTieneEnlacesEntreCarpetasMalEscritos(unittest.TestCase):
    """Sobre el repositorio de verdad. Se cae con el primero que se escriba mal.

    **No se exige cero:** lo que queda son los vecinos de la misma carpeta,
    que esperan la decisión sobre `DOC14`. Lo que sí tiene que estar en cero es
    el enlace **entre carpetas**, que es el que la regla resuelve de verdad.
    """

    def test_cero_entre_carpetas_fuera_de_prompts(self):
        quedan = sum(n for _, n in enlaces.reparar_formato())
        self.assertEqual(0, quedan)


if __name__ == "__main__":
    unittest.main()
