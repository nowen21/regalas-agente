# -*- coding: utf-8 -*-
"""Pendiente 55 y punto 1 del 33 · Lo que se muestra no es lo que se cita.

Un validador que reporta de más enseña a ignorarlo, y eso se contagia a lo que
sí es cierto. El pendiente 55 lo dice con las dos únicas salidas que dejaba:
**redactar torcido** para que el validador calle —lo que se hizo una vez— o
**aprender a ignorar** sus hallazgos.

Los cinco falsos positivos que había en `base/` se arreglaron sin tocar una
línea de `base/`, y cada uno por un motivo distinto. Esta prueba fija los cinco
motivos, y de paso el del reparador: **si el validador no lo reporta, el
reparador no lo escribe**. Eso era lo peor de todo — `citas.py --aplicar`
habría metido en `base/` los cuatro ejemplos enlazados como si fueran citas.
"""
import os
import sys
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import citas      # noqa: E402
import comun      # noqa: E402
import enlaces    # noqa: E402

RAIZ = os.path.dirname(VALIDADORES)


class LoQueSeMuestraNoSeCita(unittest.TestCase):
    """Los cinco casos reales de `base/`, cada uno por su motivo."""

    def setUp(self):
        self.hallazgos = citas.validar(RAIZ)
        self.mensajes = [str(h) for h in self.hallazgos]

    def _no_reportado(self, id, archivo):
        malos = [m for m in self.mensajes if f"`{id}`" in m and archivo in m]
        self.assertEqual([], malos, f"`{id}` en {archivo} se sigue reportando")

    def test_el_ejemplo_en_columna_de_ejemplos_no_se_cita(self):
        """`G9` vive en la columna «Lo que sale mal» de la anatomía del
        identificador. Ahí es el token equivocado del ejemplo, no la regla."""
        self._no_reportado("G9", "estructura-regla.md")

    def test_el_identificador_nombrado_en_el_glosario_no_se_cita(self):
        """«el código corto de una regla, como `C20` o `F12`»."""
        self._no_reportado("C20", "glosario.md")
        self._no_reportado("F12", "glosario.md")

    def test_la_segunda_mencion_del_mismo_archivo_no_pide_enlace(self):
        """La primera mención de `ID7` en `ID9` **sí** lleva su enlace. Pedirlo
        otra vez tres líneas más abajo es ruido, y el ruido se ignora."""
        self._no_reportado("ID7", "ID9-")

    def test_el_ancla_del_mismo_archivo_es_correcta(self):
        """`[`G1`](#g1--…)` dentro de `09-git.md` es la forma correcta de citar
        a una vecina. Compararla contra la ruta completa la daba por rota."""
        self._no_reportado("G1", "09-git.md")

    def test_g9_existe_aunque_el_pendiente_dijera_lo_contrario(self):
        """El pendiente 55 afirmaba que `G9` no existe. Sí existe.

        Sigue siendo falso positivo, pero por ser un ejemplo — no por apuntar a
        nada. La diferencia importa: si el motivo hubiera sido el que el
        pendiente daba, el arreglo habría sido otro y no habría funcionado.
        """
        self.assertIn("G9", citas.indice(RAIZ))

    def test_base_queda_sin_un_solo_hallazgo(self):
        self.assertEqual([], self.mensajes)


class ElReparadorObedeceAlValidador(unittest.TestCase):
    """Lo que el validador acepta, el reparador no lo toca.

    Es la mitad que el pendiente 55 no había visto. Aquel decía que el
    validador **reporta** de más; medido el 2026-08-17, `citas.py --aplicar`
    **escribiría** ese error en `base/`: cuatro ejemplos enlazados y un ancla
    correcta reescrita. En una sola corrida y sin que nadie revisara las cinco.
    """

    def test_no_propone_ni_un_cambio_sobre_base(self):
        tocados = citas.aplicar(RAIZ, escribir=False)
        detalle = ", ".join(f"{comun.relativo(a)} ({n}+{r})"
                            for a, n, r in tocados)
        self.assertEqual([], tocados,
                         "el reparador quiere escribir en base/: " + detalle)


class EnlaceDentroDeComillas(unittest.TestCase):
    """Un enlace de ejemplo entre comillas invertidas no es un enlace.

    El caso literal del pendiente: un plan de pruebas escribió, entre comillas,
    el texto que la prueba tenía que encontrar. Se reportó roto dos veces.
    """

    def test_el_enlace_de_muestra_no_se_reporta(self):
        linea = ("| 1 | Comprobar el estado inicial | Dice "
                 "`[historico-chat/2026-01-02-sesion.md](../../2026-01-02-sesion.md)` |")
        self.assertEqual([], comun.enlaces(linea))

    def test_el_enlace_de_verdad_en_la_misma_linea_si_se_ve(self):
        """No vale callar de más: fuera de las comillas se sigue leyendo."""
        linea = "Ver [base/09-git.md](../base/09-git.md) y no `[x](y.md)`."
        destinos = [d for _n, _t, d in comun.enlaces(linea)]
        self.assertEqual(["../base/09-git.md"], destinos)

    def test_las_comillas_no_corren_las_columnas(self):
        """El tramo se reemplaza por espacios, no se borra: la posición de lo
        que viene después no se mueve."""
        linea = "`[a](b.md)` y [real](c.md)"
        limpia = comun.sin_codigo_en_linea(linea)
        self.assertEqual(len(linea), len(limpia))


class EnlaceConEspacios(unittest.TestCase):
    """Punto 1 del pendiente 33 · el `%20` se decodifica antes de buscar."""

    def _carpeta(self):
        import tempfile
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        return tmp.name

    def test_el_archivo_con_espacios_no_se_da_por_roto(self):
        raiz = self._carpeta()
        con_espacios = os.path.join(raiz, "un archivo con espacios.md")
        with open(con_espacios, "w", encoding="utf-8") as f:
            f.write("# destino\n")
        with open(os.path.join(raiz, "origen.md"), "w", encoding="utf-8") as f:
            f.write("Ver [un archivo con espacios.md](un%20archivo%20con%20espacios.md).\n")

        rotos = enlaces.validar_enlaces(raiz)
        self.assertEqual([], [str(h) for h in rotos])

    def test_el_que_de_verdad_no_existe_se_sigue_reportando(self):
        """El arreglo no puede volverse una excusa para callar."""
        raiz = self._carpeta()
        with open(os.path.join(raiz, "origen.md"), "w", encoding="utf-8") as f:
            f.write("Ver [no esta.md](no%20esta.md).\n")

        rotos = enlaces.validar_enlaces(raiz)
        self.assertEqual(1, len(rotos), "dejó de reportar lo que sí está roto")


if __name__ == "__main__":
    unittest.main()
