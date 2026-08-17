"""Un proyecto que ya estaba instalado queda al día corriendo el instalador.

Fase `A-EP-007-HU-006-poner-al-dia-lo-ya-instalado`, casos CP-001 a CP-005. El
CP-006 es verificación manual sobre el proyecto de origen y va en el
`resultado_pruebas`.

**Por qué todos los casos instalan dos veces.** El defecto que motivó esta fase
no aparece al instalar: aparece al **volver** a instalar sobre algo que ya
estaba. Una prueba que solo instale en carpeta vacía pasa en verde con el código
roto — que es exactamente lo que pasó en la 21.1.0.

**Por qué se arma un estándar de mentira.** Dos casos necesitan que el estándar
cambie: uno le edita una plantilla y otro le sube el `VERSION`. Eso no se hace
sobre el estándar de verdad ([`00·N4`](../../base/00-nucleo-blindado.md)), así
que se copia lo que el instalador lee —`plantillas/` y `VERSION`— a una carpeta
temporal y se apunta ahí. De paso, el registro central de proyectos que el
instalador escribe cae en la copia y no en el real.

Cómo se corre:

    python -m unittest discover -s validadores/tests
"""

import contextlib
import io
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import checklist  # noqa: E402
import instalar  # noqa: E402
import version  # noqa: E402
import versiones  # noqa: E402
from comun import RAIZ, leer  # noqa: E402

MARCADOR = "«RUTA-ESTANDAR»"


def _escribir(archivo, texto):
    with open(archivo, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


@contextlib.contextmanager
def _estandar_temporal():
    """Una copia desechable del estándar, con `instalar` apuntando ahí.

    Se copia solo lo que el instalador lee de su propia carpeta. Los enganches
    que escribe citan rutas de esta copia y no se ejecutan en la prueba, así que
    no hace falta traerse `validadores/` ni `base/`.
    """
    carpeta = tempfile.mkdtemp(prefix="cimiento-estandar-")
    shutil.copytree(os.path.join(RAIZ, "plantillas"),
                    os.path.join(carpeta, "plantillas"))
    shutil.copy2(os.path.join(RAIZ, "VERSION"),
                 os.path.join(carpeta, "VERSION"))

    guardado = (instalar.RAIZ, instalar.REGISTRO, instalar.PLANTILLA_HISTORICO,
                instalar.PLANTILLA_MEMORIA, version.RAIZ)
    instalar.RAIZ = carpeta
    instalar.REGISTRO = os.path.join(carpeta, "plantillas", "proyectos.md")
    instalar.PLANTILLA_HISTORICO = os.path.join(carpeta, "plantillas",
                                                "historico-chat.md")
    instalar.PLANTILLA_MEMORIA = os.path.join(carpeta, "plantillas",
                                              "memoria.md")
    version.RAIZ = carpeta
    try:
        yield carpeta
    finally:
        (instalar.RAIZ, instalar.REGISTRO, instalar.PLANTILLA_HISTORICO,
         instalar.PLANTILLA_MEMORIA, version.RAIZ) = guardado
        shutil.rmtree(carpeta, ignore_errors=True)


class ReparaLoYaInstalado(unittest.TestCase):
    """Los cinco casos automatizados del `plan_pruebas` de la fase."""

    def setUp(self):
        self.temporal = tempfile.mkdtemp(prefix="cimiento-")
        self.proyecto = os.path.join(self.temporal, "proyecto de prueba")
        os.makedirs(self.proyecto)
        self.contexto = _estandar_temporal()
        self.estandar = self.contexto.__enter__()

    def tearDown(self):
        self.contexto.__exit__(None, None, None)
        shutil.rmtree(self.temporal, ignore_errors=True)

    def _instalar(self):
        return instalar.instalar("proyecto de prueba", self.proyecto,
                                 aplicar=True)

    def _en_proyecto(self, *partes):
        return os.path.join(self.proyecto, *partes)

    def _agente_config(self):
        return [self._en_proyecto(".agente", n) for n in instalar.CONFIG_AGENTE]

    def _config_con_ruta(self):
        """El archivo de `.agente/` que sí cita al estándar.

        Se busca en vez de nombrarlo: cuál de los cuatro trae la ruta depende de
        las plantillas, y clavar un nombre haría que la prueba dejara de probar
        el día que ese archivo cambie.
        """
        ruta = self.estandar.replace("\\", "/")
        for archivo in self._agente_config():
            if ruta in leer(archivo):
                return archivo
        self.fail("ningún archivo de .agente/ quedó citando al estándar")

    # ── CP-001 ───────────────────────────────────────────────────────────

    def test_cp_001_una_copia_con_el_marcador_crudo_queda_limpia(self):
        """CP-001 · el defecto que reportó `shopnest-mesa`.

        Se ensucia el archivo **sin tocar su sello**: así queda igual que allá,
        al día contra la plantilla y mal escrito a la vez. Antes de esta fase el
        instalador decía "ya estaba al día" y no lo abría.
        """
        self._instalar()

        sucios = [self._en_proyecto(".agente", "stack-instalacion.md"),
                  self._config_con_ruta()]
        for archivo in sucios:
            _escribir(archivo, leer(archivo).replace(
                self.estandar.replace("\\", "/"), MARCADOR))
            self.assertIn(MARCADOR, leer(archivo),
                          f"el caso no logró ensuciar {archivo}")

        self._instalar()

        for archivo in sucios:
            texto = leer(archivo)
            nombre = os.path.relpath(archivo, self.proyecto)
            self.assertNotIn(MARCADOR, texto,
                             f"{nombre} conserva el marcador crudo")
            self.assertIn(self.estandar.replace("\\", "/"), texto,
                          f"{nombre} no quedó con la ruta del estándar")

    # ── CP-002 ───────────────────────────────────────────────────────────

    def test_cp_002_la_plantilla_que_cambio_baja_al_proyecto(self):
        """CP-002 · el camino que ya funcionaba sigue funcionando.

        El envoltorio de reparación se agrega en la rama de "ya estaba al día".
        Este caso comprueba que la otra rama, la de la huella distinta, no se
        rompió.
        """
        self._instalar()

        plantilla = os.path.join(self.estandar, "plantillas",
                                 "stack-instalacion.md")
        _escribir(plantilla, leer(plantilla) + "\nLínea nueva de la prueba.\n")

        self._instalar()

        texto = leer(self._en_proyecto(".agente", "stack-instalacion.md"))
        self.assertIn("Línea nueva de la prueba.", texto,
                      "la plantilla cambió y el proyecto no la recibió")
        self.assertNotIn(MARCADOR, texto, "lo que bajó llegó sin rellenar")

    # ── CP-003 ───────────────────────────────────────────────────────────

    def test_cp_003_el_hueco_que_llena_el_proyecto_sobrevive(self):
        """CP-003 · reparar no borra lo que el estándar no sabe reponer.

        Los 4 archivos de `.agente/` llegan con huecos **a propósito**: son las
        preguntas que solo el proyecto puede responder. Es la lección del
        `DEF-01` de la fase anterior, y el riesgo `B-01` de esta.
        """
        self._instalar()

        antes = {a: leer(a) for a in self._agente_config()}
        huecos_antes = {a: leer(a).count("«") for a in self._agente_config()}
        self.assertGreater(sum(huecos_antes.values()), 0,
                           "el caso no prueba nada: no quedó ningún hueco")

        self._instalar()

        for archivo in self._agente_config():
            nombre = os.path.relpath(archivo, self.proyecto)
            self.assertEqual(leer(archivo).count("«"), huecos_antes[archivo],
                             f"reparar cambió los huecos de {nombre}")
            self.assertEqual(leer(archivo), antes[archivo],
                             f"reparar reescribió {nombre}")

    # ── CP-004 ───────────────────────────────────────────────────────────

    def test_cp_004_sube_la_version_y_queda_el_registro(self):
        """CP-004 · el defecto del pendiente 44.

        El veredicto del paso 6 no lo da el instalador, que es quien escribe:
        lo da `checklist`, que es el programa que reprobaba.
        """
        self._instalar()
        primeros = versiones.registros(self.proyecto)
        self.assertTrue(primeros, "la primera instalación no dejó registro")

        _escribir(os.path.join(self.estandar, "VERSION"), "99.0.0\n")
        self.assertEqual(version.version_estandar(), "99.0.0")

        self._instalar()

        despues = versiones.registros(self.proyecto)
        self.assertEqual(len(despues), len(primeros) + 1,
                         "subió la versión y no se escribió el registro")
        self.assertEqual(despues[-1][2], "99.0.0")

        texto = leer(os.path.join(versiones.carpeta_registros(self.proyecto),
                                  despues[-1][0]))
        self.assertIn("99.0.0", texto)
        self.assertIn("Ninguno cambió de huella", texto,
                      "el registro no dice que fue solo subida de versión")

        cumple, detalle = versiones.revisar_registro(self.proyecto,
                                                     self.estandar)
        self.assertTrue(cumple, f"el checklist sigue reprobando: {detalle}")

        faltan = checklist.pendientes(
            checklist.revisar(self.proyecto, self.estandar))
        self.assertEqual([p.id for p in faltan], [],
                         "el proyecto no llegó a la instalación completa")

    def test_cp_004_el_propio_estandar_no_se_escribe_registros(self):
        """CP-004 · paso 7, el riesgo `B-03`.

        El estándar no hereda de sí mismo: lleva su `CHANGELOG` y su `versiones`
        ni siquiera se revisa.
        """
        pasos = instalar.registrar_version(self.estandar, {}, [], aplicar=True,
                                           anterior="1.0.0")

        self.assertEqual(pasos, [])
        self.assertFalse(
            os.path.isdir(versiones.carpeta_registros(self.estandar)),
            "se le escribió un registro a la carpeta del propio estándar")

    # ── CP-005 ───────────────────────────────────────────────────────────

    def test_cp_005_reinstalar_sin_novedad_no_agrega_registro(self):
        """CP-005 · el límite de la decisión del 44.

        Lo pide el paso 3 del CA-02 de la HU: sin cambios no se agrega una
        entrada vacía. Lo que cambió es qué cuenta como cambio.
        """
        self._instalar()
        antes = len(versiones.registros(self.proyecto))

        self._instalar()

        self.assertEqual(len(versiones.registros(self.proyecto)), antes,
                         "reinstalar sin novedad agregó un registro")


class PreparaSuPropiaSalida(unittest.TestCase):
    """Fase `B-EP-007-HU-001-prepara-su-propia-salida`, caso CP-001.

    Vive en este archivo y no en uno aparte porque necesita exactamente el
    mismo montaje: un proyecto temporal y una copia desechable del estándar.
    """

    def setUp(self):
        self.temporal = tempfile.mkdtemp(prefix="cimiento-")
        self.proyecto = os.path.join(self.temporal, "proyecto de prueba")
        os.makedirs(self.proyecto)
        self.contexto = _estandar_temporal()
        self.estandar = self.contexto.__enter__()

    def tearDown(self):
        self.contexto.__exit__(None, None, None)
        shutil.rmtree(self.temporal, ignore_errors=True)

    @staticmethod
    def _consola_pobre():
        """Una salida que escribe en `cp1252` y no perdona lo que no cabe.

        Es la consola con la que arranca Windows. `errors="strict"` es lo que
        la hace reventar en vez de dibujar un signo de pregunta, que es el
        comportamiento que se quiere reproducir.
        """
        return io.TextIOWrapper(io.BytesIO(), encoding="cp1252", errors="strict")

    def test_cp_001_instalar_no_revienta_con_una_consola_pobre(self):
        """CP-001 · el instalador prepara su propia salida.

        Antes dependía de que lo hiciera `main()`, así que llamarlo como
        biblioteca lo mataba al imprimir el primer `→`.

        **La corrida que importa es la segunda.** Instalar en carpeta vacía
        nunca imprime una flecha: esa sale al refrescar un sello que ya
        existía. Por eso primero se instala, se sube la versión del estándar
        para que los sellos queden viejos, y recién ahí se corre con la consola
        pobre. Diseñado al revés, el caso pasa en verde con el defecto puesto —
        y así pasó la primera vez.
        """
        # La consola armada de verdad no admite la flecha. Sin comprobarlo, el
        # caso pasaría siempre y no probaría nada.
        with self.assertRaises(UnicodeEncodeError):
            self._consola_pobre().write("→")

        instalar.instalar("proyecto de prueba", self.proyecto, aplicar=True)
        _escribir(os.path.join(self.estandar, "VERSION"), "99.0.0\n")

        original = sys.stdout
        sys.stdout = self._consola_pobre()
        try:
            instalar.instalar("proyecto de prueba", self.proyecto, aplicar=True)
            sys.stdout.flush()
            escrito = sys.stdout.buffer.getvalue().decode("utf-8", "replace")
        finally:
            sys.stdout = original

        self.assertIn("→", escrito,
                      "el caso no reproduce el defecto: no se imprimió ninguna "
                      "flecha, así que la consola pobre nunca se puso a prueba")


if __name__ == "__main__":
    unittest.main()
