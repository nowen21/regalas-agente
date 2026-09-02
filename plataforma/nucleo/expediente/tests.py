# -*- coding: utf-8 -*-
"""Los casos del plan de pruebas de la fase `A-EP-012-HU-001`.

**Dos de los cinco criterios son de lo que NO debe pasar:** que la memoria entre
al expediente, y que armar toque un documento. Una comprobación que solo mira el
camino feliz aprueba cualquier cosa.

**Y el que más protege es el `CA-02`:** lo que falta se nombra. Un expediente que
no dice qué le falta se entrega incompleto sin que nadie lo note, que es
exactamente lo que hoy pasa armándolo a mano.
"""
import io
import os
import shutil
import tempfile

from django.test import TestCase, override_settings

from nucleo.importacion.models import Traido
from . import core, orden


class Base(TestCase):

    def setUp(self):
        self.datos = tempfile.mkdtemp(prefix="prueba-expediente-")
        self.contexto = override_settings(CARPETA_DATOS=self.datos)
        self.contexto.enable()

    def tearDown(self):
        self.contexto.disable()
        shutil.rmtree(self.datos, ignore_errors=True)

    def traer(self, origen, tipo, texto="# Un documento\n"):
        """Un documento traído, con su copia en datos."""
        guardado = "proyectos/de-prueba/traido/" + origen
        completa = os.path.join(self.datos, guardado.replace("/", os.sep))
        os.makedirs(os.path.dirname(completa), exist_ok=True)
        with io.open(completa, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)
        return Traido.objects.create(proyecto="de-prueba", origen=origen,
                                     tipo=tipo, guardado_en=guardado)

    def fase(self, nombre, tipos=None, base="documentacion/epicas/EP-001-x/HU-001-y"):
        """Una fase con los tipos que se le pidan; sin pedir, con los cinco."""
        archivos = {
            "plan de trabajo": "plan_trabajo.md",
            "plan de pruebas": "plan_pruebas.md",
            "resultado de pruebas": "resultado_pruebas.md",
            "estado de fase": "estado-fase.md",
            "funcionalidad implementada": "funcionalidad_implementada.md",
        }
        for tipo in (tipos if tipos is not None else orden.DE_UNA_FASE):
            self.traer("%s/%s/%s" % (base, nombre, archivos[tipo]), tipo)


class ElOrdenEsElDelCiclo(Base):
    """`CA-01` — agrupado por etapa, y en el orden en que el ciclo las produce."""

    def test_los_grupos_salen_en_el_orden_del_ciclo(self):
        self.traer("cvds/diseno/modelo-de-datos.md", "modelo de datos")
        self.traer("documentacion/epicas/EP-001-x/epica.md", "épica")
        self.traer("cvds/planificacion/README.md", "etapa del ciclo de vida")

        grupos = [g["grupo"] for g in core.armar("de-prueba")["grupos"]]
        self.assertEqual(["Planificación", "Diseño", "Épicas"], grupos)

    def test_los_cinco_de_una_fase_van_en_su_orden(self):
        self.fase("A-EP-001-HU-001-una")
        fases = [g for g in core.armar("de-prueba")["grupos"]
                 if g["grupo"] == "Fases"][0]
        self.assertEqual(list(orden.DE_UNA_FASE),
                         [d.tipo for d in fases["documentos"]])

    def test_un_proyecto_sin_documentos_no_devuelve_un_expediente_vacio(self):
        """Devuelve las listas en cero, y quien llama distingue eso de un error."""
        expediente = core.armar("no-existe")
        self.assertEqual([], expediente["grupos"])
        self.assertEqual([], expediente["falta"])


class LoQueFaltaSeNombra(Base):
    """`CA-02` — se lista con su nombre, y no se inventa."""

    def test_el_documento_que_falta_se_nombra(self):
        self.fase("A-EP-001-HU-001-una",
                  tipos=[t for t in orden.DE_UNA_FASE if t != "estado de fase"])
        falta = core.armar("de-prueba")["falta"]
        self.assertEqual(1, len(falta))
        self.assertEqual("estado de fase", falta[0]["que"])
        self.assertEqual("A-EP-001-HU-001-una", falta[0]["donde"])

    def test_lo_que_falta_no_aparece_en_el_expediente(self):
        """**No se inventa.** El documento ausente no entra vacío."""
        self.fase("A-EP-001-HU-001-una",
                  tipos=[t for t in orden.DE_UNA_FASE if t != "estado de fase"])
        expediente = core.armar("de-prueba")
        tipos = [d.tipo for g in expediente["grupos"] for d in g["documentos"]]
        self.assertNotIn("estado de fase", tipos)
        self.assertEqual(4, core.cuantos_documentos(expediente))

    def test_una_fase_completa_no_reporta_faltantes(self):
        self.fase("A-EP-001-HU-001-una")
        self.assertEqual([], core.armar("de-prueba")["falta"])


class LoIncompletoSeMarca(Base):
    """`CA-03` — los huecos sin llenar se cuentan antes de entregar."""

    def test_un_documento_con_huecos_se_marca(self):
        self.traer("documentacion/epicas/EP-001-x/epica.md", "épica",
                   u"# Épica\n\n| Campo | «…» |\n| Otro | «…» |\n")
        incompletos = core.armar("de-prueba")["incompletos"]
        self.assertEqual(1, len(incompletos))
        self.assertEqual(2, incompletos[0]["huecos"])

    def test_un_documento_lleno_no_se_marca(self):
        self.traer("documentacion/epicas/EP-001-x/epica.md", "épica",
                   u"# Épica\n\nTodo dicho.\n")
        self.assertEqual([], core.armar("de-prueba")["incompletos"])

    def test_una_cita_no_es_un_hueco(self):
        """**En esta casa se cita con esas comillas todo el tiempo.** Contarlas
        daría por incompleto cualquier documento bien escrito: se midió, y de
        559 documentos «a medio llenar» quedaron 31."""
        self.assertEqual(0, core.huecos_de(u"el usuario dijo «no hacer»"))
        self.assertEqual(1, core.huecos_de(u"| Campo | «…» |"))

    def test_salen_de_mas_huecos_a_menos(self):
        self.traer("a/epica.md", "épica", u"«…»\n")
        self.traer("b/epica.md", "épica", u"«…» «…» «…»\n")
        incompletos = core.armar("de-prueba")["incompletos"]
        self.assertEqual([3, 1], [d["huecos"] for d in incompletos])


class LaMemoriaNoEntra(Base):
    """`CA-04` — el caso de «que NO pase» de esta historia."""

    def test_las_senales_no_entran(self):
        self.traer("documentacion/senales.md", "señales")
        self.traer("documentacion/epicas/EP-001-x/epica.md", "épica")
        expediente = core.armar("de-prueba")
        tipos = [d.tipo for g in expediente["grupos"] for d in g["documentos"]]
        self.assertEqual(["épica"], tipos)

    def test_el_indice_de_una_carpeta_tampoco(self):
        """No es un documento del ciclo: el expediente arma su propia tabla."""
        self.traer("documentacion/README.md", "índice")
        self.assertEqual([], core.armar("de-prueba")["grupos"])

    def test_lo_excluido_no_se_reporta_como_que_no_encaja(self):
        """**Se excluye a propósito, no por no reconocerlo.** Meterlo en la
        lista de lo que no encaja lo haría ver como un defecto."""
        self.traer("documentacion/senales.md", "señales")
        self.assertEqual([], core.armar("de-prueba")["sin_encajar"])


class LoQueNoEncajaSeListaAparte(Base):
    """Acomodarlo al grupo más parecido convierte un dato en una suposición."""

    def test_lo_que_importacion_no_reconocio_se_dice(self):
        self.traer("algo/raro.md", "")
        expediente = core.armar("de-prueba")
        self.assertEqual(1, len(expediente["sin_encajar"]))
        self.assertEqual("", expediente["sin_encajar"][0]["tipo"])

    def test_un_tipo_conocido_sin_grupo_se_dice(self):
        self.traer("algo/otro.md", "un tipo que nadie ordenó")
        expediente = core.armar("de-prueba")
        self.assertEqual(1, len(expediente["sin_encajar"]))
        self.assertEqual([], expediente["grupos"])


class ElAlcanceSeRecortaDiciendolo(Base):
    """`CA-05` — recortar en silencio es lo mismo que perder."""

    def setUp(self):
        super(ElAlcanceSeRecortaDiciendolo, self).setUp()
        self.fase("A-EP-001-HU-001-una")
        self.fase("B-EP-001-HU-001-dos")

    def test_completo_trae_las_dos_fases(self):
        self.assertEqual(10, core.cuantos_documentos(core.armar("de-prueba")))

    def test_acotado_trae_solo_hasta_ahi(self):
        expediente = core.armar("de-prueba", hasta="A-EP-001-HU-001-una")
        self.assertEqual(5, core.cuantos_documentos(expediente))

    def test_lo_que_queda_fuera_se_dice(self):
        expediente = core.armar("de-prueba", hasta="A-EP-001-HU-001-una")
        self.assertEqual(5, len(expediente["fuera_del_alcance"]))
        self.assertEqual({"B-EP-001-HU-001-dos"},
                         {d["fase"] for d in expediente["fuera_del_alcance"]})

    def test_lo_acotado_no_reporta_faltantes_de_lo_que_dejo_fuera(self):
        """Si los reportara, un alcance acotado diría que al proyecto le falta
        justo lo que se pidió no mirar."""
        self.assertEqual([], core.armar(
            "de-prueba", hasta="A-EP-001-HU-001-una")["falta"])


class ArmarNoTocaNada(Base):
    """El transversal: armar el expediente no modifica ningún documento."""

    def retrato(self):
        salida = {}
        for base, _dirs, nombres in os.walk(self.datos):
            for nombre in nombres:
                completa = os.path.join(base, nombre)
                with io.open(completa, encoding="utf-8") as f:
                    salida[os.path.relpath(completa, self.datos)] = f.read()
        return salida

    def test_ningun_documento_cambia(self):
        self.fase("A-EP-001-HU-001-una")
        antes = self.retrato()
        core.armar("de-prueba")
        self.assertEqual(antes, self.retrato())


class CP009LosHuecosLosCuentaCicloDeVida(TestCase):
    """Lo que salió al preguntarle al expediente qué le faltaba al proyecto.

    **Contaba `texto.count("«…»")` a secas**, y reportaba 70 huecos en 38
    documentos que Ciclo de vida daba por completos. Los 68 de más eran citas de
    la marca dentro de un bloque de código, o marcas del propio molde.

    Dos módulos contando lo mismo con reglas distintas es tener dos verdades.
    """

    def test_la_marca_dentro_de_un_bloque_de_codigo_no_es_un_hueco(self):
        texto = (u"# Un documento\n\nSe escribe la marca así:\n\n"
                 u"```\n«…»\n```\n")
        self.assertEqual(0, core.huecos_de(texto, "historia de usuario",
                                           "documentacion/x.md"))

    def test_la_marca_en_codigo_de_una_linea_tampoco(self):
        texto = u"# Un documento\n\nLa marca es `«…»` y se reemplaza.\n"
        self.assertEqual(0, core.huecos_de(texto, "historia de usuario",
                                           "documentacion/x.md"))

    def test_una_marca_de_verdad_si_se_cuenta(self):
        texto = u"# Un documento\n\n| Responsable | «…» |\n"
        self.assertEqual(1, core.huecos_de(texto, "historia de usuario",
                                           "documentacion/x.md"))

    def test_un_texto_vacio_no_revienta(self):
        self.assertEqual(0, core.huecos_de(""))
        self.assertEqual(0, core.huecos_de(None))
