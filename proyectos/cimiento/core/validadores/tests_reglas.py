"""Los validadores del cuerpo de reglas, como clases: meta-reglas, quién hace
cumplir el núcleo, vigencia, numeración, cruces, reglas relacionadas y el mapa
de tareas.

Son las pruebas que tenían en `validadores/pruebas.py` y en
`validadores/tests/` (`test_cada_tarea_sabe_que_reglas_le_aplican`,
`test_el_identificador_no_se_repite`, `test_el_largo_se_mide_por_lo_que_se_lee`,
`test_el_sello_no_se_contradice`, `test_la_base_no_nombra_stack`,
`test_la_entrada_del_registro_se_entiende`,
`test_la_regla_del_nucleo_dice_quien_la_hace_cumplir`,
`test_la_regla_que_nadie_vuelve_a_mirar`, `test_llegan_las_reglas_relacionadas`,
`test_metareglas_no_afirma_sobre_un_proyecto`, `test_sello_del_checklist_vencido`
y `test_una_sola_numeracion`), pasadas a su clase. Se quedaron afuera las que
miran otra pieza: el enganche de relacionadas, `instalar.py` y `validar.py`.
"""
import io
import os
import re
import subprocess
import tempfile
import unittest
from unittest import mock

from core.comun import AVISO, FALLA, Archivos, Proyecto
from core.herramientas.mapa_tareas import MapaDeTareas, MapaDeTareasAlDia
from core.validadores import ejecutable as modulo_ejecutable
from core.validadores import numeracion as modulo_numeracion
from core.validadores.citas import IndiceDeReglas
from core.validadores.cruces import CrucesEntreModulos
from core.validadores.ejecutable import MOTIVO_MINIMO, QuienLaHaceCumplir
from core.validadores.metareglas import (LIMITE_CUERPO, CatalogoDelProyecto, CuerpoDeReglas, Metareglas, Regla,
                                         Sello)
from core.validadores.numeracion import Numeracion
from core.validadores.relacionadas import ReglasRelacionadas
from core.validadores.vigencia import Vigencia

RAIZ = Proyecto.estandar()


def escribir(raiz, relativa, texto):
    ruta = os.path.join(raiz, *relativa.split("/"))
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)
    return ruta


class Carpeta(unittest.TestCase):

    def carpeta(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        return tmp.name


# ── El mapa de tareas ─────────────────────────────────────────────────────

LISTA = """# Las tareas del agente

| Tarea | Cuándo aplica | Palabras clave que la piden | Acciones que la señalan |
|---|---|---|---|
| `cambiar-codigo` | Se cambia código | | `escribe otro` |
| `escribir-documento` | Se escribe un documento | escriba | `escribe .md` |
| `tocar-git` | Se hace commit | suba | `comando git` |
"""

CUERPO = "Nombra cada cosa por lo que hace, no por cómo se construyó."


def capitulo(aplica):
    """Un capítulo con una sola regla; `aplica` es su línea, o None."""
    partes = ["# 07 · Calidad", "", "## Q1 · Nombra bien las cosas", "",
              CUERPO, "", "```", "INCORRECTO: x", "CORRECTO:   y", "```", ""]
    if aplica is not None:
        partes += ["**Aplica a:** " + aplica, ""]
    partes += ["---", ""]
    return "\n".join(partes)


class RepoDeTareas(Carpeta):

    def repo(self, aplica):
        raiz = self.carpeta()
        escribir(raiz, "base/tareas.md", LISTA)
        escribir(raiz, "base/07-calidad.md", capitulo(aplica))
        return raiz

    def regla(self, raiz):
        return [r for r in CuerpoDeReglas.leer(raiz) if r.id == "Q1"][0]

    def al_dia(self, aplica):
        raiz = self.repo(aplica)
        MapaDeTareas(raiz).escribir()
        return raiz


class LaLineaAplicaANoCambiaLaRegla(RepoDeTareas):
    """`EP-005·HU-023·CA-02`."""

    def test_no_cuenta_para_el_largo(self):
        sin = self.regla(self.repo(None)).largo()
        con = self.regla(self.repo("cambiar-codigo, tocar-git")).largo()
        self.assertEqual(sin, con)
        self.assertEqual(len(CUERPO), con)

    def test_no_vence_el_sello(self):
        self.assertEqual(Sello.sin_declaracion(capitulo(None)),
                         Sello.sin_declaracion(capitulo("cambiar-codigo")))


class ElMapaSaleDeLasReglas(RepoDeTareas):
    """`EP-005·HU-023·CA-03`."""

    def bloque(self, mapa, tarea):
        return [b for b in mapa.split("## `") if b.startswith(tarea)][0]

    def test_una_regla_con_dos_tareas_sale_en_las_dos(self):
        mapa = MapaDeTareas(self.repo("cambiar-codigo, escribir-documento")).armar()
        self.assertIn("07·Q1", self.bloque(mapa, "cambiar-codigo"))
        self.assertIn("07·Q1", self.bloque(mapa, "escribir-documento"))

    def test_cambiar_la_tarea_mueve_la_regla(self):
        raiz = self.repo("cambiar-codigo")
        antes = MapaDeTareas(raiz).armar()
        escribir(raiz, "base/07-calidad.md", capitulo("tocar-git"))
        despues = MapaDeTareas(raiz).armar()
        self.assertNotEqual(antes, despues)
        self.assertIn("07·Q1", self.bloque(despues, "tocar-git"))
        self.assertNotIn("07·Q1", self.bloque(despues, "cambiar-codigo"))

    def test_la_tarea_sin_reglas_lo_dice(self):
        mapa = MapaDeTareas(self.repo("cambiar-codigo")).armar()
        self.assertIn("Ninguna regla la declara todavía", self.bloque(mapa, "tocar-git"))

    def test_el_enlace_lleva_a_la_regla(self):
        mapa = MapaDeTareas(self.repo("cambiar-codigo")).armar()
        self.assertIn("(07-calidad.md#%s)" % IndiceDeReglas.ancla("Q1 · Nombra bien las cosas"), mapa)

    def test_la_tarea_fuera_de_la_lista_no_entra_y_se_reporta(self):
        mapa = MapaDeTareas(self.repo("cambiar-codigo, bailar"))
        self.assertNotIn("bailar", mapa.armar())
        self.assertEqual([("Q1", "bailar")], [(r.id, t) for r, t in mapa.sin_lista()])

    def test_escribir_deja_el_mapa_en_base(self):
        raiz = self.repo("cambiar-codigo")
        mapa = MapaDeTareas(raiz)
        ruta = mapa.escribir()
        self.assertEqual(os.path.join(Proyecto(raiz).raiz, "base", "mapa-de-tareas.md"), ruta)
        with io.open(ruta, encoding="utf-8") as f:
            self.assertEqual(mapa.armar(), f.read())

    def test_las_columnas_de_palabras_y_acciones(self):
        mapa = MapaDeTareas(self.repo("cambiar-codigo"))
        self.assertEqual({"escriba"}, mapa.palabras_clave()["escribir-documento"])
        self.assertEqual([("comando", ["git"])], mapa.acciones()["tocar-git"])
        self.assertEqual([("escribe", ["otro"])], mapa.acciones()["cambiar-codigo"])


class ElMapaAlDia(RepoDeTareas):
    """`EP-005·HU-023·CA-04` y `CA-10`."""

    def test_con_todo_al_dia_pasa(self):
        self.assertEqual([], MapaDeTareasAlDia(self.al_dia("cambiar-codigo")).validar())

    def test_la_regla_sin_tareas_falla(self):
        h = MapaDeTareasAlDia(self.al_dia(None)).validar()
        self.assertEqual(1, len(h))
        self.assertIn("07·Q1", h[0].mensaje)
        self.assertIn("Aplica a", h[0].mensaje)

    def test_la_tarea_fuera_de_la_lista_falla(self):
        h = MapaDeTareasAlDia(self.al_dia("bailar")).validar()
        self.assertEqual(1, len(h))
        self.assertIn("`bailar`", h[0].mensaje)

    def test_el_mapa_viejo_falla(self):
        raiz = self.al_dia("cambiar-codigo")
        escribir(raiz, "base/07-calidad.md", capitulo("tocar-git"))
        h = MapaDeTareasAlDia(raiz).validar()
        self.assertTrue(any("el mapa no coincide" in x.mensaje for x in h))
        viejos = {os.path.basename(x.archivo) for x in h if "reglas de esta tarea no coinciden" in x.mensaje}
        self.assertIn("cambiar-codigo.md", viejos)
        self.assertIn("tocar-git.md", viejos)

    def test_el_archivo_que_sobra_falla(self):
        raiz = self.al_dia("cambiar-codigo")
        escribir(raiz, "base/reglas-por-tarea/bailar.md", "# Bailar\n")
        h = MapaDeTareasAlDia(raiz).validar()
        self.assertEqual(1, len(h))
        self.assertIn("sobra", h[0].mensaje)

    def test_escribir_borra_el_que_sobra(self):
        raiz = self.al_dia("cambiar-codigo")
        sobra = escribir(raiz, "base/reglas-por-tarea/bailar.md", "# Bailar\n")
        MapaDeTareas(raiz).escribir()
        self.assertFalse(os.path.exists(sobra))

    def test_la_regla_completa_llega_al_archivo_de_su_tarea(self):
        raiz = self.al_dia("cambiar-codigo")
        archivos = MapaDeTareas(raiz).archivos_de("cambiar-codigo")
        self.assertEqual(["cambiar-codigo.md"], [os.path.basename(a) for a in archivos])
        with io.open(archivos[0], encoding="utf-8") as f:
            texto = f.read()
        self.assertIn("## Q1 · Nombra bien las cosas", texto)
        self.assertIn(CUERPO, texto)
        self.assertIn("INCORRECTO: x", texto)

    def test_la_regla_derogada_no_se_reporta(self):
        raiz = self.repo(None)
        escribir(raiz, "base/07-calidad.md", capitulo(None).replace(
            "## Q1 · Nombra bien las cosas", "## Q1 · Nombra bien las cosas `[DEROGADA en 1.0.0 → ver Q2]`"))
        MapaDeTareas(raiz).escribir()
        self.assertEqual([], MapaDeTareasAlDia(raiz).validar())

    def test_sin_lista_de_tareas_no_reporta_nada(self):
        self.assertEqual([], MapaDeTareasAlDia(self.carpeta()).validar())

    def test_las_blindadas_de_datos_llegan_a_su_tarea(self):
        """El archivo de la tarea de datos trae completas las tres blindadas
        que gobiernan borrar sobre datos reales (de `pruebas.py`)."""
        archivos = Archivos()
        texto = "".join(archivos.leer(r) for r in MapaDeTareas(RAIZ).archivos_de("tocar-datos"))
        for id_ in ("N4", "N5", "N7"):
            self.assertIn("## " + id_ + " ·", texto, "faltó %s en la tarea de datos" % id_)


# ── Meta-reglas: lo que se lee de `base/` ─────────────────────────────────

class ElIdentificadorNoSeRepite(Carpeta):
    """`EP-004·HU-011·CP-002`. Las derogadas cuentan igual (`20·M11`)."""

    def repetidos(self, raiz):
        return Metareglas.identificador_repetido(CuerpoDeReglas.leer(raiz))

    def test_dos_reglas_con_el_mismo_identificador_se_reportan(self):
        raiz = self.carpeta()
        escribir(raiz, "base/09-git.md", "# 09 · Git  ·  `[CAPA 2]`\n\n## G1 · Uno\n\ntexto\n\n## G1 · Dos\n\ntexto\n")
        h = self.repetidos(raiz)
        self.assertEqual(2, len(h), "se reporta en las dos, no solo en la segunda")
        self.assertEqual(FALLA, h[0].severidad)
        self.assertIn("`G1`", h[0].mensaje)

    def test_el_hallazgo_nombra_las_dos_en_conflicto(self):
        raiz = self.carpeta()
        escribir(raiz, "base/09-git.md", "# 09 · Git\n\n## G1 · Uno\n\ntexto\n")
        escribir(raiz, "base/03-datos.md", "# 03 · Datos\n\n## G1 · Otra\n\ntexto\n")
        h = self.repetidos(raiz)
        self.assertTrue(h)
        self.assertIn("09-git.md", h[0].mensaje)
        self.assertIn("03-datos.md", h[0].mensaje)

    def test_un_cuerpo_sin_repetidos_no_dice_nada(self):
        raiz = self.carpeta()
        escribir(raiz, "base/09-git.md", "# 09 · Git\n\n## G1 · Uno\n\ntexto\n\n## G2 · Dos\n\ntexto\n")
        self.assertEqual([], self.repetidos(raiz))

    def test_la_derogada_sigue_ocupando_su_identificador(self):
        raiz = self.carpeta()
        escribir(raiz, "base/09-git.md", "# 09 · Git\n\n## G1 · Vieja  ·  `[DEROGADA en 3.0.0 → ver G2]`\n\n"
                                         "texto\n\n## G1 · Nueva\n\ntexto\n")
        self.assertTrue(self.repetidos(raiz))

    def test_el_cuerpo_real_del_estandar_no_tiene_ninguno(self):
        self.assertEqual([], self.repetidos(RAIZ))


class Cuerpo:
    """Lo mínimo que `Regla.largo()` necesita."""

    def __init__(self, *lineas):
        self.cuerpo = list(enumerate(lineas, start=1))

    largo = Regla.largo


class ElLargoSeMidePorLoQueSeLee(unittest.TestCase):
    """Fila 10: el destino de un enlace no se cuenta (`20·M15` contra `20·M5`)."""

    def test_el_enlace_cuenta_por_su_texto(self):
        con = "Ver la regla [`04·S4`](../04-seguridad.md#s4--gestión-de-secretos) y seguirla."
        self.assertEqual(len("Ver la regla `04·S4` y seguirla."), Cuerpo(con).largo())

    def test_el_texto_sin_enlaces_no_cambia(self):
        texto = "Una regla corta y sin citas."
        self.assertEqual(len(texto), Cuerpo(texto).largo())

    def test_varios_enlaces_en_la_misma_linea(self):
        corto = Cuerpo("Ver [a](x.md) y [b](y.md).").largo()
        largo = Cuerpo("Ver [a](un/destino/mucho/mas/largo.md) y [b](otro/todavia/peor.md).").largo()
        self.assertEqual(corto, largo)
        self.assertEqual(len("Ver a y b."), corto)

    def test_la_regla_que_de_verdad_no_cabe_sigue_sin_caber(self):
        self.assertGreater(Cuerpo("x" * 400).largo(), LIMITE_CUERPO)

    def test_ninguna_regla_del_estandar_se_pasa_solo_por_el_marcado(self):
        culpables = [r for r in CuerpoDeReglas.leer(RAIZ)
                     if sum(len(t) for _, t in r.cuerpo) > LIMITE_CUERPO >= r.largo()]
        self.assertTrue(culpables, "la corrección no rescató ninguna regla")
        for r in culpables:
            self.assertFalse([h for h in Metareglas.fila7_10_12_13_formato(r) if "fila 10" in h.mensaje])


class ReglaMinima:
    """Lo mínimo que las comprobaciones de una regla suelta necesitan."""

    def __init__(self, texto="", id="ZZ1", cuerpo=(), archivo="base/x.md", linea=3):
        self.texto, self.id, self.archivo, self.linea = texto, id, archivo, linea
        self.cuerpo = [(1, l) for l in cuerpo]
        self.derogada = False


class LaBaseNoNombraStack(unittest.TestCase):
    """Fila 5 · `20·M3`: lo que se reporta y lo que se queda a propósito."""

    def nombres(self, texto):
        return [h.mensaje for h in Metareglas.fila5_tecnologia(ReglaMinima(cuerpo=[texto]))]

    def test_los_que_ya_estaban(self):
        for palabra in ("Django", "SQLite", "MariaDB", "React", "php"):
            with self.subTest(palabra=palabra):
                self.assertEqual(1, len(self.nombres("corre sobre %s" % palabra)))

    def test_node_y_softdeletes(self):
        self.assertEqual(1, len(self.nombres('"todos los `node`"')))
        self.assertEqual(1, len(self.nombres("`destroy()`, `SoftDeletes`, archivar")))

    def test_los_nombres_del_oficio_no_se_reportan(self):
        for palabra in ("killall", "pkill -f", "taskkill /IM"):
            with self.subTest(palabra=palabra):
                self.assertEqual([], self.nombres("Prohibido: `%s`" % palabra))

    def test_las_palabras_del_dominio_del_estandar_no_se_reportan(self):
        self.assertEqual([], self.nombres("La fase declara su historia, y la migración documenta por qué"))

    def test_no_se_reporta_una_palabra_dentro_de_otra(self):
        self.assertEqual([], self.nombres("el usuario puede reaccionar al aviso"))
        self.assertEqual([], self.nombres("el nodo del árbol"))

    def test_el_cuerpo_de_reglas_no_nombra_stack(self):
        self.assertEqual(set(), {r.id for r in CuerpoDeReglas.leer(RAIZ) if Metareglas.fila5_tecnologia(r)})


# ── El sello de cada regla ────────────────────────────────────────────────

TABLA = """| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | %s |
| B · Cómo se identifica | 5–6 | %s |
| C · Cómo está escrita | 7–13 | %s |
| D · Cómo se relaciona | 14–17 | %s |
| E · Fuera de su texto | 18–20 | %s |
"""
OK, NO, NA = "✅", "❌", "N/A"


def tabla(a=None, b=None, c=None, d=None, e=None):
    return TABLA % (" ".join(a or [OK] * 4), " ".join(b or [OK] * 2), " ".join(c or [OK] * 7),
                    " ".join(d or [NA, NA, NA, OK]), " ".join(e or [OK] * 3))


def sello(veredicto="NO CUMPLE", cuerpo=None, totales=None, prosa="", **bloques):
    return "\n".join(["### Checklist  ·  **%s**" % veredicto, "",
                      "Aplicado el checklist contra **v1.0.0**, el **2026-01-01**.", "",
                      cuerpo if cuerpo is not None else tabla(**bloques), totales or "", prosa])


class ElSelloNoSeContradice(unittest.TestCase):
    """Pendiente 19 · La tabla es la que se lee."""

    def test_el_texto_reprueba_una_fila_que_la_tabla_da_por_buena(self):
        h = Sello.se_contradice(ReglaMinima(sello(prosa="**Fila 5 · nombra un módulo de un proyecto real**.")))
        self.assertEqual(1, len(h))
        self.assertIn("fila 5", h[0].mensaje)

    def test_varias_filas_se_nombran_en_plural(self):
        h = Sello.se_contradice(ReglaMinima(sello(prosa="**Fila 5 · tecnología.**\n\n**Fila 10 · no cabe.**")))
        self.assertIn("las filas 5 y 10", h[0].mensaje)

    def test_el_texto_agrupado_tambien_cuenta(self):
        r = ReglaMinima(sello(prosa="**Filas 8, 9 y 10 ·** son tres reglas en una."))
        self.assertEqual(1, len(Sello.se_contradice(r)))

    def test_la_tabla_puede_marcar_mas_de_lo_que_el_texto_desglosa(self):
        r = ReglaMinima(sello(c=[OK, NO, NO, NO, OK, OK, OK], prosa="Son tres reglas en una y no cabe."))
        self.assertEqual([], Sello.se_contradice(r))

    def test_cuando_coinciden_no_se_reporta(self):
        r = ReglaMinima(sello(b=[NO, OK], prosa="**Fila 5 · nombra tecnología.**"))
        self.assertEqual([], Sello.se_contradice(r))

    def test_un_cumple_que_cuenta_lo_que_corrigio_no_se_reporta(self):
        r = ReglaMinima(sello(veredicto="CUMPLE", prosa="**Fila 8 · el título manda.** Se corrigió."))
        self.assertEqual([], Sello.se_contradice(r))

    def test_un_cumple_con_una_cruz_en_la_tabla_si_se_reporta(self):
        h = Sello.se_contradice(ReglaMinima(sello(veredicto="CUMPLE", c=[OK, NO, OK, OK, OK, OK, OK])))
        self.assertEqual(1, len(h))
        self.assertIn("CUMPLE", h[0].mensaje)

    def test_sin_bloque_de_checklist_no_hay_nada_que_comparar(self):
        self.assertEqual([], Sello.se_contradice(ReglaMinima("## ZZ1 · Algo\n\nExige algo.\n")))

    def test_los_totales_que_no_coinciden_se_reportan(self):
        r = ReglaMinima(sello(totales="**20 filas: 14 ✅ · 3 ❌ · 3 N/A.**",
                              c=[OK, OK, NO, NO, NO, OK, OK], d=[NA, NA, OK, OK]))
        h = Sello.totales(r)
        self.assertEqual(1, len(h))
        self.assertIn("14 ✅", h[0].mensaje)

    def test_los_totales_correctos_no_se_reportan(self):
        r = ReglaMinima(sello(totales="**20 filas: 14 ✅ · 3 ❌ · 3 N/A.**",
                              c=[OK, OK, NO, NO, NO, OK, OK], d=[NA, NA, NA, OK]))
        self.assertEqual([], Sello.totales(r))

    def test_una_tabla_que_no_suma_veinte_se_dice_asi(self):
        r = ReglaMinima(sello(totales="**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**", cuerpo="| A · Dónde va | 1–4 | ✅ ✅ |\n"))
        h = Sello.totales(r)
        self.assertEqual(1, len(h))
        self.assertIn("20 filas", h[0].mensaje)

    def test_sin_linea_de_totales_no_se_reporta(self):
        self.assertEqual([], Sello.totales(ReglaMinima(sello())))

    def test_dos_bloques_apilados_se_reportan(self):
        h = Sello.uno_solo(ReglaMinima(sello(veredicto="CUMPLE") + "\n---\n" + sello(veredicto="CUMPLE")))
        self.assertEqual(1, len(h))
        self.assertIn("2 bloques", h[0].mensaje)

    def test_uno_solo_no_se_reporta(self):
        self.assertEqual([], Sello.uno_solo(ReglaMinima(sello())))

    def test_ningun_sello_del_estandar_se_contradice(self):
        malos = []
        for r in CuerpoDeReglas.leer(RAIZ):
            malos += Sello.se_contradice(r) + Sello.totales(r) + Sello.uno_solo(r)
        self.assertEqual([], [h.mensaje for h in malos])


class LaMarcaBlindadaEsDelNucleo(Carpeta):
    """`20·M1` · Una regla no se declara intocable viviendo fuera del núcleo."""

    def blindadas(self, archivo, encabezado, cuerpo="Una exigencia corta."):
        raiz = self.carpeta()
        escribir(raiz, "base/" + archivo, "# Capítulo\n\n## %s\n\n%s\n\n```\nINCORRECTO: no\nCORRECTO:   sí\n```\n"
                 % (encabezado, cuerpo))
        return Metareglas.blindada_solo_en_el_nucleo(CuerpoDeReglas.leer(raiz))

    def test_en_el_nucleo_no_se_reporta(self):
        self.assertEqual([], self.blindadas("00-nucleo-blindado.md", "N9 · Algo `[BLINDADA]`"))

    def test_fuera_del_nucleo_es_falla_y_nombra_la_regla(self):
        h = self.blindadas("07-calidad-de-codigo.md", "Q9 · Algo `[BLINDADA]`")
        self.assertEqual(1, len(h))
        self.assertIn("Q9", h[0].mensaje)

    def test_una_regla_sin_la_marca_no_se_reporta(self):
        self.assertEqual([], self.blindadas("07-calidad-de-codigo.md", "Q9 · Algo corriente"))

    def test_la_palabra_en_la_prosa_no_cuenta(self):
        self.assertEqual([], self.blindadas("07-calidad-de-codigo.md", "Q9 · Algo corriente",
                                            "Esto no puede tocar una regla `[BLINDADA]` del núcleo."))


REGLA_SELLADA = """> Regla del capítulo [`02 · Flujo`](../base.md).

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


class ElSelloVencido(Carpeta):
    """Pendiente 52 · El sello vence si la regla cambió después de sellarse.

    **Corregida respecto de la vieja.** Allá la regla de mentira llevaba en
    `texto` el archivo entero con su encabezado, y la edición iba después del
    sello; la comparación contra lo guardado se hacía en el repositorio del
    estándar, no en el de la prueba, así que siempre daba «cambió» y la prueba
    pasaba sin comparar nada. Acá `texto` es lo que deja el lector (sin
    encabezado), la edición del cuerpo queda sin guardar (contra `HEAD` es lo
    único que se ve), y se prueba también que tocar solo el sello o la
    tipografía no lo vence.
    """

    def _git(self, raiz, *args, fecha=None):
        entorno = dict(os.environ, GIT_AUTHOR_NAME="p", GIT_AUTHOR_EMAIL="p@p",
                       GIT_COMMITTER_NAME="p", GIT_COMMITTER_EMAIL="p@p")
        if fecha:
            entorno["GIT_AUTHOR_DATE"] = entorno["GIT_COMMITTER_DATE"] = fecha + "T10:00:00"
        subprocess.run(["git"] + list(args), cwd=raiz, env=entorno, capture_output=True, text=True, timeout=30)

    def _cambiar(self, ruta, cambio):
        with io.open(ruta, encoding="utf-8") as f:
            texto = f.read()
        escribir(os.path.dirname(ruta), os.path.basename(ruta), texto.replace(*cambio))

    def _repo(self, fecha_sello, tocar_despues=None, sin_guardar=("Exige algo.", "Exige algo distinto.")):
        """El archivo se guarda el día del sello; `tocar_despues` guarda otro
        cambio fuera del cuerpo ese día, y `sin_guardar` cambia el texto sin
        guardarlo. **Lo que se compara es contra `HEAD`**: una edición ya
        guardada no vence el sello (límite del diseño, igual que en el viejo)."""
        raiz = self.carpeta()
        self._git(raiz, "init", "-q")
        ruta = escribir(raiz, "regla.md", REGLA_SELLADA % fecha_sello)
        self._git(raiz, "add", "-A")
        self._git(raiz, "commit", "-qm", "nace", fecha=fecha_sello)
        if tocar_despues:
            self._cambiar(ruta, ("> Vale mientras", "> Sigue valiendo mientras"))
            self._git(raiz, "add", "-A")
            self._git(raiz, "commit", "-qm", "se edita", fecha=tocar_despues)
        if sin_guardar:
            self._cambiar(ruta, sin_guardar)
        with io.open(ruta, encoding="utf-8") as f:
            texto = f.read()
        return ReglaMinima(texto.split("## ZZ1 · Una regla de mentira\n", 1)[1], archivo=ruta)

    def test_editada_despues_del_sello_se_reporta(self):
        h = Sello.vencido(self._repo("2026-01-01", tocar_despues="2026-02-02"))
        self.assertEqual(1, len(h))
        self.assertIn("2026-01-01", h[0].mensaje)
        self.assertIn("2026-02-02", h[0].mensaje)
        self.assertEqual(AVISO, h[0].severidad)

    def test_tocar_solo_el_sello_no_lo_vence(self):
        regla = self._repo("2026-01-01", tocar_despues="2026-02-02", sin_guardar=None)
        self.assertFalse(Sello.cambio_de_verdad(regla))
        self.assertEqual([], Sello.vencido(regla))

    def test_la_tipografia_no_vence_el_sello(self):
        """Un espacio de ancho cero agregado al cuerpo se limpia antes de comparar."""
        regla = self._repo("2026-01-01", tocar_despues="2026-02-02",
                           sin_guardar=("Exige algo.", "Exige​ algo."))
        self.assertFalse(Sello.cambio_de_verdad(regla))
        self.assertEqual([], Sello.vencido(regla))

    def test_sin_tocar_despues_no_se_reporta(self):
        self.assertEqual([], Sello.vencido(self._repo("2026-01-01")))

    def test_el_mismo_dia_no_vence(self):
        self.assertEqual([], Sello.vencido(self._repo("2026-01-01", tocar_despues="2026-01-01")))

    def test_sin_fecha_en_el_sello_no_se_inventa_nada(self):
        r = ReglaMinima("### Checklist · **CUMPLE**\n\nAplicado contra **v1.0.0**.\n", archivo="cualquiera.md")
        self.assertEqual([], Sello.vencido(r))

    def test_fuera_del_control_de_versiones_no_se_reporta(self):
        ruta = escribir(self.carpeta(), "suelta.md", REGLA_SELLADA % "2026-01-01")
        self.assertEqual([], Sello.vencido(ReglaMinima(REGLA_SELLADA % "2026-01-01", archivo=ruta)))

    def test_la_derogada_no_se_reporta(self):
        regla = self._repo("2026-01-01", tocar_despues="2026-02-02")
        regla.derogada = True
        self.assertEqual([], Sello.vencido(regla))

    def test_la_fecha_sale_del_control_de_versiones_y_no_del_disco(self):
        regla = self._repo("2026-01-01")
        os.utime(regla.archivo, None)
        self.assertEqual([], Sello.vencido(regla))

    def test_sobre_el_estandar_la_medicion_se_puede_repetir(self):
        vencidos = [h for r in CuerpoDeReglas.leer(RAIZ) for h in Sello.vencido(r)]
        self.assertTrue(all("se aplicó el" in h.mensaje and h.severidad == AVISO for h in vencidos))

    def test_sobre_el_estandar_no_queda_ninguno_vencido(self):
        self.assertEqual([], [h.mensaje[:60] for h in Metareglas(RAIZ).validar() if "se aplicó el" in h.mensaje])

    def test_la_regla_sin_cambios_no_vence(self):
        d2 = [x for x in CuerpoDeReglas.leer(RAIZ) if x.id == "D2"][0]
        self.assertFalse(Sello.cambio_de_verdad(d2))
        self.assertFalse(d2.texto.lstrip().startswith("## "), "el texto no trae el encabezado")


# ── Meta-reglas: el validador entero y el registro ────────────────────────

class ApuntarLasMetareglasAUnProyecto(Carpeta):
    """`81` · Sobre un proyecto no se inventan incumplimientos."""

    def setUp(self):
        self.proyecto = self.carpeta()
        escribir(self.proyecto, "CLAUDE.md", "# Un proyecto cualquiera\n")
        os.makedirs(os.path.join(self.proyecto, ".agente"))

    def test_un_solo_aviso_que_dice_que_hacer(self):
        h = Metareglas(self.proyecto).validar()
        self.assertEqual(1, len(h))
        self.assertEqual(AVISO, h[0].severidad)
        self.assertIn("--catalogo", h[0].mensaje)

    def test_el_estandar_se_reconoce_por_lo_que_solo_el_tiene(self):
        self.assertTrue(CuerpoDeReglas.es_el_estandar(RAIZ))
        self.assertFalse(CuerpoDeReglas.es_el_estandar(self.proyecto))
        os.makedirs(os.path.join(self.proyecto, "base"))
        self.assertFalse(CuerpoDeReglas.es_el_estandar(self.proyecto), "con base/ pero sin VERSION")

    def test_sobre_el_estandar_sigue_comprobando_de_verdad(self):
        self.assertFalse(any("--catalogo" in h.mensaje for h in Metareglas(RAIZ).validar()))

    def test_sin_los_archivos_la_fila_19_no_dice_nada(self):
        self.assertEqual([], Metareglas.fila19_version(self.carpeta()))

    def test_con_los_archivos_la_fila_19_trae_el_dato(self):
        raiz = self.carpeta()
        escribir(raiz, "VERSION", "9.9.9\n")
        escribir(raiz, "CHANGELOG.md", "# Cambios\n\n## 1.0.0 — 2026-01-01\n\nAlgo.\n")
        h = Metareglas.fila19_version(raiz)
        self.assertEqual(1, len(h))
        self.assertIn("9.9.9", h[0].mensaje)


class LaEntradaDelRegistroSeEntiende(Carpeta):
    """`20·M17` · El primer párrafo de la entrada vigente abre en llano."""

    def hallazgos(self, version, entrada, anteriores=""):
        raiz = self.carpeta()
        escribir(raiz, "VERSION", version + "\n")
        escribir(raiz, "CHANGELOG.md", "# Cambios del estándar\n\n## %s — 2026-08-18\n\n%s\n\n%s"
                 % (version, entrada, anteriores))
        return Metareglas.entrada_llana(raiz), raiz

    def test_abrir_con_un_identificador_de_regla(self):
        h, _ = self.hallazgos("1.0.0", "**MENOR** — la fila 12 de `20·M5` pide ejemplo.")
        self.assertEqual(1, len(h))
        self.assertIn("identificador de regla", h[0].mensaje)

    def test_abrir_con_una_ruta_de_archivo(self):
        h, _ = self.hallazgos("1.0.0", "**MENOR** — columna nueva en "
                                       "`plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md`.")
        self.assertEqual(1, len(h))
        self.assertIn("ruta de archivo", h[0].mensaje)

    def test_abrir_con_las_palabras_de_la_casa(self):
        h, _ = self.hallazgos("1.0.0", "**MENOR** — el checklist de la fase pasa a exigirlo.")
        self.assertEqual(1, len(h))
        self.assertIn("palabras de la casa", h[0].mensaje)

    def test_el_mensaje_junta_los_motivos(self):
        h, _ = self.hallazgos("1.0.0", "**MENOR** — `20·M5` y `plantillas/x.md`.")
        self.assertIn(" y ", h[0].mensaje)

    def test_la_entrada_llana_pasa(self):
        h, _ = self.hallazgos("1.0.0", "**MENOR** — al anotar que una prueba pasó ahora hay que decir con qué "
                                       "se probó.\n\nAntes se anotaba solo «aprobado», y así nadie podía repetirla.")
        self.assertEqual([], h)

    def test_el_detalle_debajo_no_cuenta(self):
        h, _ = self.hallazgos("1.0.0", "**MENOR** — al anotar que una prueba pasó hay que decir con qué se "
                                       "probó.\n\nAntes se anotaba solo «aprobado».\n\n**El detalle.** Lo pide "
                                       "`20·M5`, en `plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md`.")
        self.assertEqual([], h)

    def test_la_fecha_no_cuenta_como_parrafo(self):
        h, _ = self.hallazgos("1.0.0", "2026-08-18\n\n**MENOR** — `20·M5` lo pide.")
        self.assertEqual(1, len(h))

    def test_las_entradas_viejas_no_se_reportan(self):
        h, _ = self.hallazgos("1.0.0", "**MENOR** — al anotar que una prueba pasó hay que decir con qué se probó.",
                              anteriores="## 0.9.0 — 2026-08-01\n\n**MENOR** — `20·M5` en `base/x.md`.\n")
        self.assertEqual([], h)

    def test_sin_entrada_para_la_version_no_dice_nada(self):
        _, raiz = self.hallazgos("1.0.0", "llano y claro")
        escribir(raiz, "VERSION", "2.0.0\n")
        self.assertEqual([], Metareglas.entrada_llana(raiz))

    def test_la_entrada_vigente_del_estandar_abre_en_llano(self):
        self.assertEqual([], [x.mensaje for x in Metareglas.entrada_llana(RAIZ)])


class ClasificacionDeCadaRegla(Carpeta):
    """`EP-004·HU-002` · Toda regla dice si es comprobable (de `pruebas.py`)."""

    def test_ninguna_regla_de_base_se_queda_sin_clasificar(self):
        sin = [h.mensaje for h in Metareglas(RAIZ).validar() if "no aparece en" in h.mensaje]
        self.assertEqual([], sin)

    def test_el_registro_no_nombra_reglas_que_no_existan(self):
        archivos = Archivos()
        base = "\n".join(archivos.leer(os.path.join(c, n)) for c, _, ns in os.walk(os.path.join(RAIZ, "base"))
                         for n in ns if n.endswith(".md"))
        inventadas = [i for i in sorted(CuerpoDeReglas.clasificadas(RAIZ))
                      if not re.search(r"\b" + re.escape(i) + r"\b", base)]
        self.assertEqual([], inventadas)

    def test_el_analizador_ve_las_reglas_escritas_con_tres_almohadillas(self):
        vistas = {r.id for r in CuerpoDeReglas.leer(RAIZ)}
        for id_ in ("CQ1", "CQ2", "CQ3", "CQ4"):
            self.assertIn(id_, vistas)

    def test_el_registro_no_clasifica_por_rangos(self):
        clasificadas = CuerpoDeReglas.clasificadas(RAIZ)
        self.assertIn("C1", clasificadas)
        self.assertIn("C17", clasificadas)
        self.assertNotIn("C1–C17", clasificadas)
        self.assertNotIn("C1-C17", clasificadas)

    def test_la_derogada_no_se_exige_ni_se_reclama(self):
        derogadas = [r for r in CuerpoDeReglas.leer(RAIZ) if r.derogada]
        self.assertTrue(derogadas)
        clasificadas = CuerpoDeReglas.clasificadas(RAIZ)
        sin_clasificar = [r for r in derogadas if r.id not in clasificadas]
        self.assertTrue(sin_clasificar, "todas las derogadas están clasificadas")
        for r in sin_clasificar:
            self.assertEqual([], Metareglas.fila18_clasificada(r, clasificadas))
        reclamadas = [h.mensaje for h in Metareglas(RAIZ).validar() if "no aparece en" in h.mensaje]
        for r in derogadas:
            self.assertFalse(any(r.id in m for m in reclamadas))

    def test_ningun_identificador_derogado_vuelve_como_vigente(self):
        reglas = CuerpoDeReglas.leer(RAIZ)
        derogadas = {r.id for r in reglas if r.derogada}
        self.assertEqual(set(), derogadas & {r.id for r in reglas if not r.derogada})

    def test_a_la_derogada_no_se_le_reclama_nada(self):
        derogadas = {r.id for r in CuerpoDeReglas.leer(RAIZ) if r.derogada}
        reclamadas = [h.mensaje for h in Metareglas(RAIZ).validar()
                      if any(re.search(r"`%s`" % re.escape(d), h.mensaje) for d in derogadas)]
        self.assertEqual([], reclamadas)

    def test_una_regla_nueva_sin_clasificar_se_reporta(self):
        raiz = self.carpeta()
        escribir(raiz, "VERSION", "0.0.0\n")
        escribir(raiz, "base/99-inventado.md", "# Capítulo inventado\n\n## ZZ1 · Una regla que nadie clasificó\n\n"
                                               "Texto de la regla.\n\n```\nINCORRECTO: a\nCORRECTO: b\n```\n")
        escribir(raiz, "validadores/reglas-validables.md", "# Qué reglas del estándar son validables\n\n(ninguna)\n")
        h = [x for x in Metareglas(raiz).validar() if "ZZ1" in x.mensaje and "no aparece en" in x.mensaje]
        self.assertEqual(1, len(h))
        self.assertEqual(FALLA, h[0].severidad)


class ElAjusteDelProyectoNoAflojaElNucleo(Carpeta):
    """`EP-001·HU-006·CA-03` · Aflojar una blindada se reprueba; endurecerla pasa."""

    def proyecto(self, cuerpo):
        raiz = self.carpeta()
        escribir(raiz, ".agente/reglas-proyecto.md", cuerpo)
        return raiz

    def test_la_regla_que_afloja_una_blindada_se_reprueba(self):
        raiz = self.proyecto("# Reglas propias\n\n## P1 · El agente puede commitear sin pedir permiso\n\n"
                             "- **Respaldo:** afloja `N2`, que exige pedido explícito.\n")
        h = [x for x in CatalogoDelProyecto(raiz).validar() if "N2" in x.mensaje and "BLINDADA" in x.mensaje]
        self.assertEqual(1, len(h))

    def test_la_regla_que_endurece_una_blindada_pasa(self):
        raiz = self.proyecto("# Reglas propias\n\n## P1 · Toda migración se revisa en pareja antes de correr\n\n"
                             "- **Respaldo:** concreta `N4`, que exige autorización para lo destructivo sobre "
                             "datos reales.\n")
        self.assertEqual([], CatalogoDelProyecto(raiz).validar())

    def test_sin_respaldo_y_sin_catalogo(self):
        raiz = self.proyecto("# Reglas propias\n\n## P1 · Algo\n\nSin respaldo.\n")
        self.assertIn("Respaldo", CatalogoDelProyecto(raiz).validar()[0].mensaje)
        self.assertIn("no tiene", CatalogoDelProyecto(self.carpeta()).validar()[0].mensaje)


# ── Quién hace cumplir el núcleo ──────────────────────────────────────────

CHECKLIST = """
---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../20-meta-reglas/checklist.md) contra
**v1.0.0**, el **2026-01-02**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
"""


def regla_del_nucleo(id_, declaracion=""):
    return ("> Regla del capítulo `00 · Prueba`.\n\n## %s · Título de prueba\n\n"
            "El cuerpo pide una sola cosa, en presente.\n\n"
            "```\nINCORRECTO: hacerlo mal\nCORRECTO:   hacerlo bien\n```\n\n%s%s"
            % (id_, declaracion + "\n\n" if declaracion else "", CHECKLIST))


class QuienHaceCumplirElNucleo(Carpeta):
    """`EP-005·HU-012`."""

    MOTIVO = ("**Nadie la hace cumplir:** ningún programa ve si el usuario aprobó, porque la aprobación "
              "ocurre en el chat.")
    PIEZA = "**Quién la hace cumplir:** `validadores/marcas.py`, que la cuenta sobre lo que se entrega."

    def hallazgos(self, *reglas):
        raiz = self.carpeta()
        escribir(raiz, "validadores/marcas.py", "# una pieza que existe de verdad\n")
        for id_, declaracion in reglas:
            escribir(raiz, "base/00-prueba/%s-de-prueba.md" % id_, regla_del_nucleo(id_, declaracion))
        return QuienLaHaceCumplir(raiz).validar()

    def test_la_regla_sin_declaracion_se_reporta_como_falla_y_dice_donde(self):
        h = self.hallazgos(("N1", ""))
        self.assertEqual(1, len(h))
        self.assertEqual(FALLA, h[0].severidad)
        self.assertIn("`N1`", h[0].mensaje)
        self.assertIn("Quién la hace cumplir", h[0].mensaje)
        self.assertIn("antes del checklist", h[0].mensaje)

    def test_la_que_declara_su_pieza_no_se_reporta(self):
        self.assertEqual([], self.hallazgos(("N1", self.PIEZA)))

    def test_solo_se_reporta_la_que_falta(self):
        h = self.hallazgos(("N1", self.PIEZA), ("N2", ""))
        self.assertEqual(1, len(h))
        self.assertIn("`N2`", h[0].mensaje)

    def test_la_derogada_queda_fuera(self):
        raiz = self.carpeta()
        escribir(raiz, "base/00-prueba/N3-de-prueba.md",
                 "## N3 · Título de prueba `[DEROGADA en 2.0.0 → ver N4]`\n\nEl cuerpo que ya no manda.\n" + CHECKLIST)
        self.assertEqual([], QuienLaHaceCumplir(raiz).validar())

    def test_nadie_con_motivo_no_se_reporta(self):
        self.assertEqual([], self.hallazgos(("N1", self.MOTIVO)))

    def test_nadie_sin_motivo_se_reporta(self):
        h = self.hallazgos(("N1", "**Nadie la hace cumplir:** no."))
        self.assertEqual(1, len(h))
        self.assertIn("no dice por qué", h[0].mensaje)

    def test_una_casilla_marcada_no_es_una_decision(self):
        corto = "**Nadie la hace cumplir:** es criterio."
        self.assertLess(len(corto.split("**")[-1].strip()), MOTIVO_MINIMO)
        self.assertEqual(1, len(self.hallazgos(("N1", corto))))

    def test_la_pieza_inventada_se_reporta_por_su_nombre(self):
        h = self.hallazgos(("N1", "**Quién la hace cumplir:** `validadores/inventado.py`."))
        self.assertEqual(1, len(h))
        self.assertIn("`validadores/inventado.py`", h[0].mensaje)

    def test_decir_que_alguien_la_hace_cumplir_sin_nombrarlo_se_reporta(self):
        h = self.hallazgos(("N1", "**Quién la hace cumplir:** un enganche del estándar."))
        self.assertIn("no nombra la pieza", h[0].mensaje)

    def test_dos_piezas_declaradas_se_revisan_las_dos(self):
        h = self.hallazgos(("N1", "**Quién la hace cumplir:** `validadores/marcas.py` y "
                                  "`validadores/inventado.py`."))
        self.assertEqual(1, len(h))
        self.assertIn("inventado.py", h[0].mensaje)

    def test_no_es_punto_de_entrada(self):
        """Lo corre `validar.py ejecutable`: el módulo no tiene `main`."""
        self.assertFalse(hasattr(modulo_ejecutable, "main"))


class ElNucleoDeVerdad(unittest.TestCase):
    """`CA-04` y la no regresión, sobre el estándar publicado."""

    def test_ninguna_regla_del_nucleo_queda_sin_declarar(self):
        self.assertEqual([], QuienLaHaceCumplir(RAIZ).validar())

    def test_las_del_nucleo_estan_contadas(self):
        c = QuienLaHaceCumplir(RAIZ).cuenta()
        self.assertEqual(c["reglas"], c["con_pieza"] + c["sin_nadie"])

    def test_id9_e_id10_declaran_su_pieza(self):
        e = QuienLaHaceCumplir(RAIZ)
        nucleo = {r.id: r for r in e.del_nucleo()}
        for id_, pieza in (("ID9", "brevedad.py"), ("ID10", "redaccion.py")):
            clase, texto = e.declaracion(nucleo[id_])
            self.assertEqual("quien", clase)
            self.assertIn(pieza, texto)

    def test_dos_corridas_dan_lo_mismo(self):
        self.assertEqual([h.mensaje for h in QuienLaHaceCumplir(RAIZ).validar()],
                         [h.mensaje for h in QuienLaHaceCumplir(RAIZ).validar()])

    def test_la_linea_de_cierre_dice_las_dos_cifras_y_su_limite(self):
        texto = QuienLaHaceCumplir(RAIZ).como_texto()
        self.assertIn("con pieza que las ejecuta", texto)
        self.assertIn("sin quien las ejecute", texto)
        self.assertIn("lo lee una persona", texto)


# ── Vigencia ──────────────────────────────────────────────────────────────

SELLO_FECHADO = "Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v24.0.0**, el **2026-08-11**."


class LaVigenciaSeMide(unittest.TestCase):
    """Pendiente 14 · `EP-001·HU-007·CA-04`."""

    def test_el_sello_no_cuenta_como_revision_de_fondo(self):
        r = ReglaMinima(SELLO_FECHADO)
        self.assertEqual("2026-08-11", Vigencia.fecha_del_sello(r))
        self.assertEqual("", Vigencia.revisada(r))

    def test_la_linea_de_revision_si_cuenta(self):
        self.assertEqual("2026-08-19", Vigencia.revisada(
            ReglaMinima(SELLO_FECHADO + "\n> Revisada contra la realidad el 2026-08-19.")))

    def test_una_regla_sin_nada_no_revienta(self):
        self.assertEqual(("", ""), (Vigencia.revisada(ReglaMinima("")), Vigencia.fecha_del_sello(ReglaMinima(""))))

    def test_nunca_detiene_y_avisa_una_sola_vez(self):
        h = Vigencia(RAIZ).validar()
        self.assertLessEqual(len(h), 1)
        self.assertFalse([x for x in h if x.severidad == FALLA])

    def test_calla_cuando_todas_estan_revisadas(self):
        datos = [(ReglaMinima(""), "2026-08-19", "2026-08-11", 0)]
        with mock.patch.object(Vigencia, "listado", lambda self: datos):
            self.assertEqual([], Vigencia(RAIZ).validar())

    def test_la_que_nunca_se_reviso_encabeza_y_manda_el_sello_mas_viejo(self):
        datos = Vigencia(RAIZ).listado()
        self.assertTrue(datos)
        sin = [d for d in datos if not d[1]]
        if sin:
            self.assertEqual("", datos[0][1])
        self.assertEqual(sorted(d[2] for d in sin), [d[2] for d in sin])


# ── Numeración ────────────────────────────────────────────────────────────

CABEZA = "# Cambios del estándar\n\n"


def entrada(v, extra="", fecha="2026-08-18"):
    return "## %s — %s%s\n\nUna cosa cambió, y por esto.\n\n" % (v, fecha, extra)


class UnaSolaNumeracion(Carpeta):
    """`20·M18` · `EP-002·HU-006`."""

    def repo(self, version, registro, guardar=None):
        raiz = self.carpeta()
        if guardar is not None:
            for orden in (["init", "-q"], ["config", "user.email", "p@p"], ["config", "user.name", "p"]):
                subprocess.run(["git", "-C", raiz] + orden, capture_output=True)
            escribir(raiz, "VERSION", guardar + "\n")
            escribir(raiz, "CHANGELOG.md", registro)
            subprocess.run(["git", "-C", raiz, "add", "-A"], capture_output=True)
            subprocess.run(["git", "-C", raiz, "commit", "-qm", "x"], capture_output=True)
        escribir(raiz, "VERSION", version + "\n")
        escribir(raiz, "CHANGELOG.md", registro)
        return Numeracion(raiz).validar()

    def fallas(self, hs):
        return [h for h in hs if h.severidad == FALLA]

    def avisos(self, hs):
        return [h for h in hs if h.severidad == AVISO]

    def test_por_debajo_de_lo_guardado_es_falla_con_los_dos_numeros(self):
        m = self.fallas(self.repo("9.2.0", CABEZA + entrada("9.2.0"), guardar="10.0.0"))[0].mensaje
        self.assertIn("9.2.0", m)
        self.assertIn("10.0.0", m)

    def test_igual_o_por_encima_de_lo_guardado_no_es_falla(self):
        self.assertEqual([], self.fallas(self.repo("9.2.0", CABEZA + entrada("9.2.0"), guardar="9.2.0")))
        self.assertEqual([], self.fallas(self.repo("10.0.0", CABEZA + entrada("10.0.0"), guardar="9.2.0")))

    def test_sin_repositorio_no_dice_nada_de_esto(self):
        self.assertEqual([], self.fallas(self.repo("9.2.0", CABEZA + entrada("9.2.0"))))

    def test_la_guardada_sale_de_head(self):
        raiz = self.carpeta()
        self.assertIsNone(Numeracion.guardada(raiz))

    def test_version_sin_entrada_es_falla(self):
        self.assertTrue(self.fallas(self.repo("10.0.0", CABEZA + entrada("9.2.0"))))

    def test_con_su_entrada_calla_aunque_el_titulo_traiga_mas(self):
        self.assertEqual([], self.fallas(self.repo("10.0.0", CABEZA + entrada("10.0.0"))))
        self.assertEqual([], self.fallas(self.repo("10.0.0", CABEZA + entrada("10.0.0", "  ·  algo"))))

    def test_numero_repetido_es_falla_y_dice_cuantas(self):
        self.assertTrue(self.fallas(self.repo("15.4.0", CABEZA + entrada("15.4.0", fecha="2026-08-15")
                                              + entrada("15.4.0", fecha="2026-08-14"))))
        m = self.fallas(self.repo("15.4.0", CABEZA + entrada("15.4.0") * 3))[0].mensaje
        self.assertIn("3 entradas", m)

    def test_reconocido_en_el_registro_baja_a_aviso_y_sigue_a_la_vista(self):
        hs = self.repo("15.4.0", CABEZA + entrada("15.4.0", "  ·  ⚠ **número repetido**")
                       + entrada("15.4.0", fecha="2026-08-14"))
        self.assertEqual([], self.fallas(hs))
        self.assertIn("15.4.0", self.avisos(hs)[0].mensaje)

    def test_sin_repetidos_calla(self):
        self.assertEqual([], self.fallas(self.repo("15.5.0", CABEZA + entrada("15.5.0") + entrada("15.4.0"))))

    def test_el_hueco_avisa_y_los_consecutivos_no(self):
        hs = self.repo("1.0.3", CABEZA + entrada("1.0.3") + entrada("1.0.0"))
        self.assertEqual([], self.fallas(hs))
        self.assertTrue(self.avisos(hs))
        self.assertEqual([], self.repo("1.0.1", CABEZA + entrada("1.0.1") + entrada("1.0.0")))

    def test_version_con_forma_rara_es_falla_y_no_revienta(self):
        self.assertEqual(1, len(self.fallas(self.repo("v10", CABEZA + entrada("10.0.0")))))

    def test_sin_los_archivos_no_dice_nada(self):
        self.assertEqual([], Numeracion(self.carpeta()).validar())

    def test_registro_vacio_no_revienta(self):
        self.assertTrue(self.fallas(self.repo("1.0.0", CABEZA)))

    def test_no_es_punto_de_entrada(self):
        self.assertFalse(hasattr(modulo_numeracion, "main"))


# ── Cruces entre módulos ──────────────────────────────────────────────────

DOMINIO = """# Dominio

| Módulo | Carpeta | Especificación |
|---|---|---|
| pagos | app/pagos | doc/pagos.md |
| pedidos | app/pedidos | doc/pedidos.md |
"""
CONSUME = "# Pedidos\n\n| Módulo | Qué consume | Por qué |\n|---|---|---|\n| pagos | cobrar | cerrar |\n"
HISTORIAL = "# Pagos\n\n| Fecha | Módulo que consume | Qué |\n|---|---|---|\n| 2026-01-01 | pedidos | cobrar |\n"
SIN_HISTORIAL = "# Pagos\n\nNada.\n"


class LosCrucesSeRegistranEnLosDos(Carpeta):
    """`13·DOC7`. No tenían pruebas propias: solo la de su subcomando."""

    def hallazgos(self, pagos, pedidos=CONSUME, dominio=DOMINIO):
        raiz = self.carpeta()
        escribir(raiz, ".agente/dominio.md", dominio)
        escribir(raiz, "doc/pagos.md", pagos)
        escribir(raiz, "doc/pedidos.md", pedidos)
        return CrucesEntreModulos(raiz).validar()

    def test_los_dos_lados_no_dicen_nada(self):
        self.assertEqual([], self.hallazgos(HISTORIAL))

    def test_el_consumido_que_no_lo_registra_se_avisa(self):
        h = self.hallazgos(SIN_HISTORIAL)
        self.assertEqual(1, len(h))
        self.assertEqual(AVISO, h[0].severidad)
        self.assertTrue(h[0].archivo.replace("\\", "/").endswith("doc/pagos.md"))
        self.assertIn("`pedidos`", h[0].mensaje)

    def test_el_historial_sin_consumo_declarado_se_avisa(self):
        h = self.hallazgos(HISTORIAL, pedidos="# Pedidos\n\nNada.\n")
        self.assertEqual(1, len(h))
        self.assertIn("no declara qué consume", h[0].mensaje)

    def test_sin_modulos_declarados_se_dice(self):
        h = self.hallazgos(HISTORIAL, dominio="# Dominio\n")
        self.assertIn("no declara sus módulos", h[0].mensaje)

    def test_ninguno_es_una_fila_vacia(self):
        self.assertEqual([], CrucesEntreModulos.modulos("ninguno"))
        self.assertEqual(["a", "b"], CrucesEntreModulos.modulos("`A`, b"))


# ── Las reglas relacionadas ───────────────────────────────────────────────

class LleganLasReglasRelacionadas(unittest.TestCase):
    """`EP-005·HU-010`. Las del enganche se quedan con el enganche."""

    F2 = os.path.join(RAIZ, "base", "02-flujo-de-trabajo", "reglas", "F2-sin-especificacion-acordada-no-hay-codigo.md")

    def setUp(self):
        self.consulta = ReglasRelacionadas(RAIZ)

    def citan(self, rel):
        return [q for lista in rel["citan"].values() for q in lista]

    def test_encuentra_la_regla_con_la_que_se_choco_y_cruza_capitulos(self):
        citan = self.citan(self.consulta.de(self.F2))
        for id_ in ("F0", "ID3", "DOC3"):
            self.assertIn(id_, citan)

    def test_el_capitulo_duenio_sale_de_la_carpeta(self):
        casos = {os.path.join(RAIZ, "base", "01-conducta.md"): "20",
                 os.path.join(RAIZ, "pendientes", "x.md"): "02",
                 os.path.join(RAIZ, "plantillas", "x.md"): "13"}
        for ruta, capitulo in casos.items():
            with self.subTest(ruta=os.path.basename(ruta)):
                self.assertEqual(capitulo, ReglasRelacionadas.capitulo_de(ruta, RAIZ))

    def test_un_archivo_fuera_del_estandar_no_lo_gobierna_ninguno(self):
        """Corregido respecto del viejo: en otra unidad, `relpath` reventaba."""
        self.assertIsNone(ReglasRelacionadas.capitulo_de(os.path.join(tempfile.gettempdir(), "x.md"), RAIZ))

    def test_lo_que_no_gobierna_ningun_capitulo_devuelve_vacio(self):
        self.assertEqual({}, self.consulta.de(os.path.join(RAIZ, "notas", "README.md")))

    def test_el_aviso_nombra_la_fila_17_y_abre_con_las_que_dependen(self):
        texto = ReglasRelacionadas.como_texto(self.consulta.de(self.F2))
        self.assertIn("fila 17", texto)
        self.assertIn("dependen de lo que está tocando", texto)

    def test_un_archivo_sin_reglas_dentro_no_dice_nada(self):
        self.assertEqual("", ReglasRelacionadas.como_texto(self.consulta.de(os.path.join(RAIZ, "base", "README.md"))))

    def test_una_relacion_no_declarada_no_aparece(self):
        m17 = os.path.join(RAIZ, "base", "20-meta-reglas", "reglas",
                           "M17-la-entrada-del-registro-abre-en-castellano-llano.md")
        self.assertNotIn("ID7", self.consulta.de(m17)["citadas"])


if __name__ == "__main__":
    unittest.main()
