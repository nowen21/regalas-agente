# -*- coding: utf-8 -*-
"""Pendiente 19 · `20·M3` — la base no nombra tecnología ni nombre propio.

Un proyecto que hereda el estándar lee reglas escritas para el stack de otro.
No rompe nada: se lee, se entiende a medias y se aplica peor.

**Lo que estas pruebas fijan no es que el detector encuentre, sino qué se
decidió que sí y qué no.** Tres nombres se quedan a propósito —`killall`,
`pkill`, `taskkill`— porque no son producto sino cómo se llama la misma acción
en cada sistema, y quitarlos dejaría la regla sin decir qué prohíbe. Sin un
caso que lo escriba, la próxima pasada los borra creyendo que mejora.

El detector se amplió con lo que se le escapó de verdad: `node` no estaba en
la lista, y `SoftDeletes` tampoco.
"""
import os
import sys
import unittest

VALIDADORES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, VALIDADORES)

import metareglas   # noqa: E402


class Regla:
    """Lo mínimo que `_fila5_tecnologia` necesita."""

    def __init__(self, cuerpo, id="ZZ1"):
        self.cuerpo = [(1, l) for l in cuerpo]
        self.id, self.archivo, self.linea = id, "base/x.md", 1


def nombres(texto):
    return [h.mensaje for h in metareglas._fila5_tecnologia(Regla([texto]))]


class LoQueSeNombraSeReporta(unittest.TestCase):

    def test_los_que_ya_estaban(self):
        for palabra in ("Django", "SQLite", "MariaDB", "React", "php"):
            with self.subTest(palabra=palabra):
                self.assertEqual(1, len(nombres(u"corre sobre %s" % palabra)),
                                 palabra)

    def test_node_no_estaba_en_la_lista(self):
        """`04·S10` decía «todos los `node`» y «todos los `php`».

        **Solo se reportaba el segundo.** El sello de esa regla había
        argumentado la fila 5 —para defender `killall`, `pkill` y `taskkill`—
        y al hacerlo la dio por revisada; los dos intérpretes estaban tres
        líneas más arriba.
        """
        self.assertEqual(1, len(nombres(u'"todos los `node`"')))

    def test_softdeletes_tampoco(self):
        """`04·S11` lo nombra, y su sello ya lo tenía anotado como pendiente.

        Ahora el programa dice lo mismo que el sello, en vez de callar.
        """
        self.assertEqual(1, len(nombres(u"`destroy()`, `SoftDeletes`, archivar")))


class LoQueSeQuedaAProposito(unittest.TestCase):
    """Las decisiones que hay que poder releer, no volver a tomar."""

    def test_los_nombres_del_oficio_no_se_reportan(self):
        """`killall`, `pkill` y `taskkill` no son producto ni framework: son
        cómo se llama la misma acción en cada sistema. `04·S10` los conserva."""
        for palabra in ("killall", "pkill -f", "taskkill /IM"):
            with self.subTest(palabra=palabra):
                self.assertEqual([], nombres(u"Prohibido: `%s`" % palabra))

    def test_las_palabras_del_dominio_del_estandar_no_se_reportan(self):
        """Fase, historia, épica, catálogo, migración: son el vocabulario de
        esta casa, no de un stack."""
        self.assertEqual([], nombres(
            u"La fase declara su historia, y la migración documenta por qué"))

    def test_no_se_reporta_una_palabra_dentro_de_otra(self):
        """`java` dentro de `javascript` ya está resuelto por los bordes, y
        conviene que haya caso: sin ellos, «reaccionar» reportaría `react`."""
        self.assertEqual([], nombres(u"el usuario puede reaccionar al aviso"))
        self.assertEqual([], nombres(u"el nodo del árbol"))


class ElCuerpoDeReglasNoNombraStack(unittest.TestCase):
    """Sobre `base/` de verdad. **Exige cero, desde el 2026-08-18.**

    **Durante once días permitió uno**, `04·S11`, que nombraba `SoftDeletes` y
    `destroy()`. Su sello decidió no corregirlo, y tenía razón: ahí **el nombre
    del método era el argumento** —suena a borrar y escribe—, así que quitarlo
    habría dejado la regla sin su punto. Reescribirlo en concepto solo se podía
    hacer **al partirla**, y eso pasó: la mitad que nombraba el framework es
    ahora `04·S12`, escrita como «el método que suena a borrar y en realidad
    marca un campo».

    **La deuda declarada se pagó, así que la lista vuelve a cero.** Dejarla en
    `{"S11"}` sería seguir permitiendo un hueco que ya no existe — y un permiso
    que sobrevive a su motivo es como una lista negra se vuelve decorativa.
    """

    PERMITIDOS = set()

    def test_solo_queda_el_que_esta_declarado(self):
        con_nombre = set()
        for r in metareglas.reglas():
            if metareglas._fila5_tecnologia(r):
                con_nombre.add(r.id)
        self.assertEqual(self.PERMITIDOS, con_nombre)


if __name__ == "__main__":
    unittest.main()
