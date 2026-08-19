# -*- coding: utf-8 -*-
"""`EP-001 · HU-012` · El inventario de acciones del agente y su riesgo.

**El defecto que corrige.** `00·N1` pide aprobación para **todo** cambio de
estado, así que corregir una coma en un README y borrar un archivo que no está
en el control de versiones piden lo mismo.

**Y un control parejo no protege más: protege menos.** Cuando la misma exigencia
cubre lo trivial y lo grave, se aprueba **en bloque** — y entonces también quedó
aprobado lo grave.

**Lo que NO se comprueba, y está declarado.** Que la clasificación sea la
acertada. Que borrar un archivo no versionado merezca el nivel más alto y no el
del medio es un juicio, y se discute leyendo.
"""
import io
import os
import subprocess
import sys
import tempfile
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import acciones    # noqa: E402
from comun import FALLA, RAIZ      # noqa: E402

ANEXO = os.path.join(RAIZ, *acciones.ANEXO.split(os.sep))


def copia(cambio=None):
    """El anexo real en una carpeta temporal, opcionalmente estropeado."""
    tmp = tempfile.TemporaryDirectory()
    carpeta = os.path.join(tmp.name, "base", "00-identidad-y-rol")
    os.makedirs(carpeta)
    with io.open(ANEXO, encoding="utf-8") as f:
        texto = f.read()
    if cambio:
        texto = cambio(texto)
    with io.open(os.path.join(carpeta, "acciones-y-riesgo.md"),
                 "w", encoding="utf-8") as f:
        f.write(texto)
    return tmp


class CA01LaListaCubreTodo(unittest.TestCase):

    def test_ninguna_herramienta_queda_sin_clase(self):
        """`CP-001` — las diez de la historia, huérfanas: cero."""
        self.assertEqual([], acciones.validar(RAIZ))

    def test_si_falta_una_clase_se_reporta(self):
        """`CP-002` · **es el que hace útil al anterior.** Sin él, «cero
        huérfanas» podría significar que el programa no busca nada."""
        tmp = copia(lambda t: t.replace("**Tocar datos reales**", "**Otra cosa**"))
        self.addCleanup(tmp.cleanup)
        hallazgos = acciones.validar(tmp.name)
        self.assertTrue(hallazgos)
        self.assertIn("datos", hallazgos[0].mensaje)

    def test_las_doce_clases_se_leen(self):
        self.assertEqual(12, len(acciones.clases(RAIZ)))


class CA02CadaClaseConSuNivelYSuEjemplo(unittest.TestCase):

    def test_ninguna_fila_sin_ejemplo(self):
        """`CP-003` — el nivel solo se discute; el ejemplo lo hace entender."""
        for nombre, _nivel, ejemplo in acciones.clases(RAIZ):
            self.assertTrue(ejemplo, nombre)

    def test_todos_los_niveles_son_de_la_escala(self):
        for nombre, nivel, _e in acciones.clases(RAIZ):
            self.assertTrue(any(x in nivel for x in acciones.ESCALA), nombre)

    def test_un_nivel_inventado_se_reporta(self):
        """`CP-004` — la escala es cerrada, no texto libre."""
        tmp = copia(lambda t: t.replace(
            "| Abrir cualquier archivo del repositorio o del que el usuario nombró | 🟢 |",
            "| Abrir cualquier archivo del repositorio o del que el usuario nombró | medio |"))
        self.addCleanup(tmp.cleanup)
        self.assertTrue([h for h in acciones.validar(tmp.name)
                         if "no es de la escala" in h.mensaje])

    def test_dos_niveles_en_la_misma_fila_se_reportan(self):
        """**Se coló uno al construir el anexo** —«🔴 para `push`, 🟡 el resto»—
        y la primera versión de esta comprobación lo dio por bueno: miraba si
        había *algún* nivel, no si había **uno**. Una fila con dos niveles son
        dos clases sin partir."""
        tmp = copia(lambda t: t.replace(
            "| Abrir cualquier archivo del repositorio o del que el usuario nombró | 🟢 |",
            "| Abrir cualquier archivo del repositorio o del que el usuario nombró | 🟢 o 🔴 |"))
        self.addCleanup(tmp.cleanup)
        self.assertTrue([h for h in acciones.validar(tmp.name)
                         if "niveles en la misma fila" in h.mensaje])

    def test_una_fila_sin_ejemplo_se_reporta(self):
        """`CP-005`."""
        tmp = copia(lambda t: t.replace(
            "| 🟢 | Nada: no cambia estado | — |", "| 🟢 |  | — |"))
        self.addCleanup(tmp.cleanup)
        self.assertTrue([h for h in acciones.validar(tmp.name)
                         if "no tiene ejemplo" in h.mensaje])


class CA03DosRiesgosDistintosNoPidenLoMismo(unittest.TestCase):
    """`CP-006` · **Si esto sale igual, la fase falló aunque todo lo demás
    pase.** Sin diferencia de exigencia el inventario es decoración."""

    def _escala(self):
        with io.open(ANEXO, encoding="utf-8") as f:
            texto = f.read()
        filas = {}
        for linea in texto.split("\n"):
            for marca in acciones.ESCALA:
                if linea.startswith("| " + marca) and "|" in linea:
                    filas[marca] = linea.split("|")[-2].strip()
        return filas

    def test_los_tres_niveles_declaran_que_exigen(self):
        self.assertEqual(3, len(self._escala()))

    def test_el_mas_bajo_y_el_mas_alto_no_exigen_lo_mismo(self):
        e = self._escala()
        self.assertNotEqual(e["🟢"], e["🔴"])

    def test_el_medio_tampoco_es_igual_al_alto(self):
        """La distinción que de verdad importa: un plan aprobado cubre 🟡 y
        **nunca** 🔴."""
        e = self._escala()
        self.assertNotEqual(e["🟡"], e["🔴"])

    def test_el_nivel_alto_pide_aprobacion_de_esa_accion(self):
        self.assertIn("acción concreta", self._escala()["🔴"])


class CA04LoQueNoEstaEnLaLista(unittest.TestCase):
    """`CP-007` — las tres cosas, no una."""

    def _texto(self):
        with io.open(ANEXO, encoding="utf-8") as f:
            return f.read()

    def test_dice_que_se_trata_como_lo_peor(self):
        self.assertIn("Se le aplica la exigencia del nivel más alto", self._texto())

    def test_dice_que_hay_que_decirlo(self):
        self.assertIn("Se dice que no está clasificada", self._texto())

    def test_dice_que_hay_que_anotarla(self):
        self.assertIn("Se anota para clasificarla", self._texto())


class Limites(unittest.TestCase):
    """`CP-008` · la que cae en dos clases, y `CP-009` · no regresión."""

    def _texto(self):
        with io.open(ANEXO, encoding="utf-8") as f:
            return f.read()

    def test_la_que_cae_en_dos_clases_tiene_comportamiento_definido(self):
        self.assertIn("Manda la más alta", self._texto())

    def test_en_masa_no_es_una_clase_sino_un_modificador(self):
        """**Salió de construirlo:** estaba en la tabla con el nivel «el de su
        clase, subido un nivel», que no es un nivel. Lo cazó el validador."""
        self.assertIn("no es una clase: es un modificador", self._texto())
        self.assertNotIn("| **Operar en masa** |", self._texto())

    def _reglas_del_nucleo(self, texto):
        """**El cuerpo de `N1` a `N6`, sin sus bloques de checklist.**

        La primera versión comparaba desde `## N1` hasta el final, y eso
        arrastraba la prosa de los sellos — que cita otras reglas y cambia cuando
        una de ellas se deroga. **Falló con la derogación de `04·S7`**, que no
        tocó ninguna exigencia del núcleo: solo movió un ancla dentro de la
        explicación de un sello.

        Lo que el criterio protege es *«`N1` a `N6` siguen vigentes tal como
        están»* — **sus exigencias**, no el archivo. Un sello es el registro de
        haberlas revisado, no lo que exigen.
        """
        import re
        cuerpos = []
        for bloque in re.split(r"(?m)^## (?=N\d)", texto)[1:]:
            cuerpos.append(bloque.split("### Checklist")[0].strip())
        return cuerpos

    def test_el_nucleo_no_cambio(self):
        """`CP-009` · **la lista organiza, no reemplaza.**

        **Este caso cazó un cambio real al construir la fase**, y valió: se le
        había puesto al núcleo el enlace al anexo, y el archivo cambió.

        Se compara **el texto de las seis reglas**, no el archivo entero, porque
        eso es lo que el criterio protege — *«`N1` a `N6` siguen vigentes tal
        como están»*. Una nota que dice «este anexo organiza y no cambia nada»,
        puesta encima de `N1`, no altera su vigencia. **Lo que no se puede es
        tocar una línea de las seis**, y eso es lo que se comprueba.
        """
        r = subprocess.run(
            ["git", "-C", RAIZ, "show", "HEAD:base/00-nucleo-blindado.md"],
            capture_output=True, text=True, encoding="utf-8", errors="replace")
        if r.returncode:
            self.skipTest("sin control de versiones no hay con qué comparar")
        with io.open(os.path.join(RAIZ, "base", "00-nucleo-blindado.md"),
                     encoding="utf-8") as f:
            ahora = f.read()
        self.assertEqual(self._reglas_del_nucleo(r.stdout),
                         self._reglas_del_nucleo(ahora),
                         "esta fase no puede cambiar el texto de N1 a N6")

    def test_las_seis_reglas_del_nucleo_siguen(self):
        with io.open(os.path.join(RAIZ, "base", "00-nucleo-blindado.md"),
                     encoding="utf-8") as f:
            nucleo = f.read()
        for n in ("## N1", "## N2", "## N3", "## N4", "## N5", "## N6"):
            self.assertIn(n, nucleo)


class Bordes(unittest.TestCase):

    def test_sin_anexo_se_reporta_y_no_revienta(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        hallazgos = acciones.validar(tmp.name)
        self.assertEqual(1, len(hallazgos))
        self.assertEqual(FALLA, hallazgos[0].severidad)

    def test_sin_anexo_no_hay_linea_de_resumen(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.assertEqual("", acciones.linea_resumen(tmp.name))

    def test_el_resumen_cuenta_los_tres_niveles(self):
        linea = acciones.linea_resumen(RAIZ)
        for marca in acciones.ESCALA:
            self.assertIn(marca, linea)

    def test_no_es_punto_de_entrada(self):
        with io.open(os.path.join(VALIDADORES, "acciones.py"),
                     encoding="utf-8") as f:
            self.assertIn("no_es_punto_de_entrada", f.read())


if __name__ == "__main__":
    unittest.main(verbosity=2)
