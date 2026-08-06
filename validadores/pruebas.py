#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Suite de los validadores. Solo biblioteca estándar.

    python validadores/pruebas.py

Cubre las reglas y, sobre todo, los **falsos positivos** que se detectaron al
probar contra el repositorio real: son los que hacen que nadie confíe en un
validador y termine ignorándolo.
"""
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import commits          # noqa: E402
import dependencias     # noqa: E402
import enlaces          # noqa: E402
import fases            # noqa: E402
import instalar         # noqa: E402
import errores          # noqa: E402
import esquema          # noqa: E402
import herramientas     # noqa: E402
import migraciones      # noqa: E402
import plantillas       # noqa: E402
import rama             # noqa: E402
import rendimiento      # noqa: E402
import secretos         # noqa: E402
import trazabilidad     # noqa: E402
import versionado       # noqa: E402
from comun import AVISO, FALLA, lineas_utiles, marcadores  # noqa: E402


def severidades(hallazgos):
    return [h.severidad for h in hallazgos]


def mensajes(hallazgos):
    return " | ".join(h.mensaje for h in hallazgos)


class Comun(unittest.TestCase):

    def test_no_mira_dentro_de_bloques_de_codigo(self):
        # Regresión: sin esto, los ejemplos de la documentación se trataban
        # como contenido real.
        texto = "## Real\n\n```\n## Falso\n[marcador]\n```\n\n## Otro real\n"
        self.assertEqual([l for _, l in lineas_utiles(texto)],
                         ["## Real", "", "", "## Otro real"])

    def test_marcador_ignora_enlaces_y_casillas(self):
        texto = "- [ ] pendiente\n- [x] hecho\n[Ver](otro.md)\n[Módulo]\n"
        self.assertEqual([t for _, t in marcadores(texto)], ["[Módulo]"])


class Commits(unittest.TestCase):

    def test_ejemplo_correcto_de_g2_pasa(self):
        # El ejemplo CORRECTO textual de base/09-git.md · G2.
        mensaje = ("Corrige el saldo cuando hay documentos anulados\n\n"
                   "Se sumaban al total; ahora se excluyen en la consulta.\n")
        self.assertEqual(commits.validar(mensaje), [])

    def test_mensaje_vacio(self):
        self.assertEqual(severidades(commits.validar("\n\n")), [FALLA])

    def test_asunto_sin_contenido(self):
        for vacio in ("wip", "fix", "cambios", "WIP", "Fix."):
            with self.subTest(vacio=vacio):
                self.assertIn(FALLA, severidades(commits.validar(vacio)))

    def test_falta_linea_en_blanco_antes_del_cuerpo(self):
        mensaje = "Corrige el saldo con documentos anulados\nSe sumaban al total.\n"
        hallazgos = commits.validar(mensaje)
        self.assertEqual(severidades(hallazgos), [FALLA])
        self.assertEqual(hallazgos[0].linea, 2)

    def test_asunto_largo_avisa_pero_no_falla(self):
        mensaje = "C" * 100
        self.assertEqual(severidades(commits.validar(mensaje)), [AVISO])

    def test_co_authored_by_se_ancla_en_su_linea(self):
        # Regresión: el patrón usaba \s*, que se comía el salto anterior y
        # anclaba el hallazgo una línea antes.
        mensaje = ("Corrige el saldo con documentos anulados\n\n"
                   "Se sumaban al total.\n\n"
                   "Co-Authored-By: Alguien <a@b.c>\n")
        hallazgos = commits.validar(mensaje)
        self.assertEqual(severidades(hallazgos), [FALLA])
        self.assertEqual(hallazgos[0].linea, 5)

    def test_ignora_las_lineas_que_git_descarta(self):
        mensaje = ("Corrige el saldo con documentos anulados\n\n"
                   "Se sumaban al total.\n"
                   "# Please enter the commit message...\n")
        self.assertEqual(commits.validar(mensaje), [])


class Enlaces(unittest.TestCase):

    def test_descarta_ejemplos_de_formato(self):
        # Regresión: `[<ruta legible>](<path-relativo>.md)` no es un enlace.
        self.assertFalse(enlaces._comprobable("<ruta legible>", "otro.md"))
        self.assertFalse(enlaces._comprobable("texto", "<path-relativo>.md"))

    def test_descarta_rutas_a_codigo_de_proyecto(self):
        # Regresión: `app/PagoService.php` vive en un proyecto, no aquí.
        self.assertFalse(enlaces._comprobable("PagoService", "app/PagoService.php"))
        self.assertFalse(enlaces._comprobable("x", "../../../ruta/relativa"))

    def test_comprueba_md_y_carpetas(self):
        self.assertTrue(enlaces._comprobable("Ver", "../base/09-git.md"))
        self.assertTrue(enlaces._comprobable("Ver", "otro.md#seccion"))
        self.assertTrue(enlaces._comprobable("Ver", "interfaz/"))

    def test_el_estandar_no_tiene_enlaces_rotos(self):
        rotos = enlaces.validar_enlaces()
        self.assertEqual(rotos, [], mensajes(rotos))

    def test_los_indices_estan_al_dia(self):
        desfase = enlaces.validar_indices()
        self.assertEqual(desfase, [], mensajes(desfase))


class Plantillas(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def _escribir(self, nombre, contenido):
        ruta = os.path.join(self.tmp.name, nombre)
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(contenido)
        return ruta

    def test_marcador_sin_llenar_es_falla(self):
        pl = self._escribir("pl.md", "# T\n\n## 1. Datos\n\n| Módulo | [Módulo] |\n")
        doc = self._escribir("doc.md", "# T\n\n## 1. Datos\n\n| Módulo | [Módulo] |\n")
        hallazgos = plantillas.validar(doc, pl)
        self.assertEqual(severidades(hallazgos), [FALLA])

    def test_etiqueta_conservada_en_linea_llena_no_se_reporta(self):
        # Regresión con un caso real de LocalHub: la plantilla trae
        # `- [ ] [Backend] …` y el documento escribe la tarea conservando la
        # etiqueta. La línea está llena; `[Backend]` no es un hueco.
        pl = self._escribir("pl.md", "# T\n\n## 7. Tareas\n\n- [ ] [Backend] …\n")
        doc = self._escribir(
            "doc.md",
            "# T\n\n## 7. Tareas\n\n- [ ] **T1** · [Backend] Interpretar Markdown.\n")
        self.assertEqual(plantillas.validar(doc, pl), [])

    def test_corchete_propio_del_documento_no_se_reporta(self):
        # Un documento puede usar corchetes legítimamente; solo cuenta lo que
        # viene textual de la plantilla.
        pl = self._escribir("pl.md", "# T\n\n## 1. Datos\n\n[Módulo]\n")
        doc = self._escribir("doc.md", "# T\n\n## 1. Datos\n\nVentas [POS] activo\n")
        self.assertEqual(plantillas.validar(doc, pl), [])

    def test_seccion_ausente_es_aviso_no_falla(self):
        # Las plantillas dicen "elimine las secciones que no apliquen".
        pl = self._escribir("pl.md", "# T\n\n## 1. Datos\n\n## 2. Riesgos\n")
        doc = self._escribir("doc.md", "# T\n\n## 1. Datos\n")
        hallazgos = plantillas.validar(doc, pl)
        self.assertEqual(severidades(hallazgos), [AVISO])
        self.assertIn("2. Riesgos", hallazgos[0].mensaje)

    def test_encabezado_de_ejemplo_no_cuenta_como_ausente(self):
        # Regresión: `### CA-01 — [Nombre del escenario]` cambia de nombre en
        # cada documento; compararlo por título daba un aviso falso.
        pl = self._escribir("pl.md", "# T\n\n### CA-01 — [Nombre del escenario]\n")
        doc = self._escribir("doc.md", "# T\n\n### CA-01 — Alta con datos mínimos\n")
        self.assertEqual(plantillas.validar(doc, pl), [])

    def test_deduce_la_plantilla_por_el_id(self):
        doc = self._escribir("cualquiera.md", "# HU-014 — Registrar cliente\n")
        ruta = plantillas.deducir_plantilla(doc, "# HU-014 — Registrar cliente\n")
        self.assertTrue(ruta.endswith(os.path.join("plantillas", "HU.md")))

    def test_sin_id_reconocible_no_adivina(self):
        doc = self._escribir("cualquiera.md", "# Documento suelto\n")
        self.assertIsNone(plantillas.deducir_plantilla(doc, "# Documento suelto\n"))


class Fases(unittest.TestCase):
    """`02·F12` — jerarquía y nomenclatura Épica → HU → Fase."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def _armar(self, epica, hu=None, fase=None, con_documentos=True):
        raiz = os.path.join(self.tmp.name, "documentacion", "epicas", epica)
        os.makedirs(raiz, exist_ok=True)
        open(os.path.join(raiz, "epica.md"), "w").close()
        if hu:
            ruta_hu = os.path.join(raiz, hu)
            os.makedirs(ruta_hu, exist_ok=True)
            open(os.path.join(ruta_hu, f"{hu}.md"), "w").close()
            if fase:
                ruta_fase = os.path.join(ruta_hu, fase)
                os.makedirs(ruta_fase, exist_ok=True)
                if con_documentos:
                    for d in fases.DOCUMENTOS:
                        open(os.path.join(ruta_fase, d), "w").close()
        return self.tmp.name

    def test_estructura_conforme_no_reporta_nada(self):
        raiz = self._armar("EP-002-aportes", "HU-013-socios",
                           "A-EP-002-HU-013-validacion")
        self.assertEqual(fases.validar(raiz), [])

    def test_el_ancho_de_los_numeros_no_importa(self):
        # Regresión: F12.13 escribe `EP01-«slug»` y los proyectos usan
        # `EP-002-«slug»`. Exigir la forma literal del ejemplo marcaría
        # proyectos enteros por una diferencia que la regla no declara.
        raiz = self._armar("EP-2-aportes", "HU-13-socios", "A-EP-002-HU-013-x")
        self.assertEqual(fases.validar(raiz), [])

    def test_fase_que_complementa_es_valida(self):
        # F12.12 · `C-B-EP01-HU03-…` (la fase C complementa a la B), en una
        # secuencia A, B, C sin huecos (F12.5).
        raiz = self._armar("EP-001-x", "HU-003-y", "A-EP-001-HU-003-uno")
        hu = os.path.join(raiz, "documentacion", "epicas", "EP-001-x", "HU-003-y")
        for nombre in ("B-EP-001-HU-003-dos", "C-B-EP-001-HU-003-ajuste"):
            ruta = os.path.join(hu, nombre)
            os.makedirs(ruta)
            for d in fases.DOCUMENTOS:
                open(os.path.join(ruta, d), "w").close()
        self.assertEqual(fases.validar(raiz), [])

    def test_nombre_de_fase_fuera_de_f12_6(self):
        raiz = self._armar("EP-000-login", "HU-01-tipos", "fase-gz-tipo-usuario")
        hallazgos = fases.validar(raiz)
        self.assertEqual(severidades(hallazgos), [FALLA])
        self.assertIn("F12.6", mensajes(hallazgos))

    def test_fase_guardada_bajo_la_hu_equivocada(self):
        # F12.3 · una fase no se comparte entre HU.
        raiz = self._armar("EP-001-x", "HU-005-y", "A-EP-001-HU-009-z")
        hallazgos = fases.validar(raiz)
        self.assertEqual(severidades(hallazgos), [FALLA])
        self.assertIn("F12.3", mensajes(hallazgos))

    def test_consecutivo_repetido_en_la_misma_hu(self):
        raiz = self._armar("EP-001-x", "HU-003-y", "A-EP-001-HU-003-primera")
        gemela = os.path.join(raiz, "documentacion", "epicas", "EP-001-x",
                              "HU-003-y", "A-EP-001-HU-003-segunda")
        os.makedirs(gemela)
        for d in fases.DOCUMENTOS:
            open(os.path.join(gemela, d), "w").close()
        hallazgos = fases.validar(raiz)
        self.assertIn(FALLA, severidades(hallazgos))
        self.assertIn("F12.7", mensajes(hallazgos))

    def test_dentro_de_una_epica_solo_van_hu(self):
        raiz = self._armar("EP-001-x")
        os.makedirs(os.path.join(raiz, "documentacion", "epicas",
                                 "EP-001-x", "notas-sueltas"))
        hallazgos = fases.validar(raiz)
        self.assertEqual(severidades(hallazgos), [FALLA])
        self.assertIn("F12.11", mensajes(hallazgos))

    def test_hu_sin_fases_solo_avisa(self):
        # F12.2 pide al menos una, pero una HU recién abierta no incumple.
        raiz = self._armar("EP-001-x", "HU-003-y")
        self.assertEqual(severidades(fases.validar(raiz)), [AVISO])

    def test_consecutivo_contiguo_no_reporta(self):
        # F12.5 · A, B sin huecos.
        raiz = self._armar("EP-001-x", "HU-003-y", "A-EP-001-HU-003-uno")
        b = os.path.join(raiz, "documentacion", "epicas", "EP-001-x",
                         "HU-003-y", "B-EP-001-HU-003-dos")
        os.makedirs(b)
        for d in fases.DOCUMENTOS:
            open(os.path.join(b, d), "w").close()
        self.assertEqual(fases.validar(raiz), [])

    def test_consecutivo_con_hueco_avisa(self):
        # F12.5 · A y C sin B → hueco.
        raiz = self._armar("EP-001-x", "HU-003-y", "A-EP-001-HU-003-uno")
        c = os.path.join(raiz, "documentacion", "epicas", "EP-001-x",
                         "HU-003-y", "C-EP-001-HU-003-tres")
        os.makedirs(c)
        for d in fases.DOCUMENTOS:
            open(os.path.join(c, d), "w").close()
        hallazgos = fases.validar(raiz)
        self.assertIn(AVISO, severidades(hallazgos))
        self.assertIn("F12.5", mensajes(hallazgos))

    def test_sin_la_carpeta_epicas_es_falla(self):
        hallazgos = fases.validar(self.tmp.name)
        self.assertEqual(severidades(hallazgos), [FALLA])


class Trazabilidad(unittest.TestCase):
    """`02·F4` y `13·DOC` — enlace bidireccional, ORIGEN, tabla de cierre."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def _armar(self, doc_epica, doc_hu, plan="", cierre=""):
        base = os.path.join(self.tmp.name, "documentacion", "epicas",
                            "EP-002-aportes")
        hu = os.path.join(base, "HU-013-socios")
        fase = os.path.join(hu, "A-EP-002-HU-013-alta")
        os.makedirs(fase, exist_ok=True)
        self._escribir(os.path.join(base, "epica.md"), doc_epica)
        self._escribir(os.path.join(hu, "HU-013-socios.md"), doc_hu)
        self._escribir(os.path.join(fase, "plan_trabajo.md"), plan)
        self._escribir(os.path.join(fase, "funcionalidad_implementada.md"), cierre)
        return self.tmp.name

    @staticmethod
    def _escribir(ruta, texto):
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(texto)

    def test_todo_conforme_no_reporta(self):
        raiz = self._armar(
            doc_epica="Épica EP-002. HUs: HU-013, HU-014.",
            doc_hu="HU de la épica EP-002.",
            plan="## 0. Identificación\nORIGEN: funcionalidad nueva.",
            cierre="| Ítem | Estado |\n|---|---|\n| x | ✅ |")
        self.assertEqual(trazabilidad.validar(raiz), [])

    def test_hu_no_declara_su_epica(self):
        raiz = self._armar("HUs: HU-013.", "Socios, sin decir de qué épica.")
        self.assertIn("DOC16", mensajes(trazabilidad.validar(raiz)))

    def test_epica_no_lista_la_hu(self):
        raiz = self._armar("Épica EP-002, sin listar sus HU.", "De la épica EP-002.")
        msgs = mensajes(trazabilidad.validar(raiz))
        self.assertIn("no lista la HU-13", msgs)

    def test_plan_sin_origen_avisa(self):
        raiz = self._armar("HU-013", "EP-002", plan="## Plan sin campo de origen.")
        self.assertIn("ORIGEN", mensajes(trazabilidad.validar(raiz)))

    def test_cierre_con_pendiente_avisa(self):
        raiz = self._armar("HU-013", "EP-002",
                           cierre="| Ítem | Estado |\n|---|---|\n| y | ❌ |")
        self.assertIn("❌", mensajes(trazabilidad.validar(raiz)))

    def test_sin_carpeta_epicas_es_falla(self):
        self.assertEqual(severidades(trazabilidad.validar(self.tmp.name)), [FALLA])


class Versionado(unittest.TestCase):
    """`09-git.md` · G3 — qué está versionado que no debería."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def _clasificar(self, archivo, contenido=None):
        if contenido is not None:
            destino = os.path.join(self.tmp.name, archivo)
            os.makedirs(os.path.dirname(destino), exist_ok=True)
            with open(destino, "w", encoding="utf-8") as f:
                f.write(contenido)
        return versionado.clasificar(self.tmp.name, archivo)

    def test_secretos_y_dependencias_son_falla(self):
        for archivo in (".env", ".env.produccion", "node_modules/x/index.js",
                        "vendor/autoload.php", "certs/servidor.pem",
                        ".ssh/id_rsa", ".npmrc"):
            with self.subTest(archivo=archivo):
                veredicto = self._clasificar(archivo)
                self.assertIsNotNone(veredicto, f"{archivo} debió marcarse")
                self.assertEqual(veredicto[0], FALLA)

    def test_la_plantilla_de_ejemplo_si_se_versiona(self):
        # G3 pide versionar el molde sin valores.
        for archivo in (".env.example", ".env.sample", "config.dist"):
            with self.subTest(archivo=archivo):
                self.assertIsNone(self._clasificar(archivo))

    def test_libreria_copiada_a_proposito_no_se_marca(self):
        # Regresión: `vendor/` en la raíz son dependencias de Composer, pero
        # `public/vendor/…` es una librería vendorizada para andar sin internet.
        # Su `dist/` interno se marcaba como artefacto de compilación.
        self.assertIsNone(
            self._clasificar("public/vendor/reveal/dist/theme/moon.css"))
        self.assertIsNone(
            self._clasificar("interfaz/visor/static/vendor/bootstrap.min.js"))

    def test_sql_de_estructura_no_se_marca(self):
        # Regresión: marcar todo `.sql` señalaba esquemas y documentación.
        esquema = "CREATE TABLE senales (id TEXT);\nCREATE INDEX i ON senales(id);"
        self.assertIsNone(self._clasificar("memoria/esquema.sql", esquema))

    def test_sql_con_datos_reales_avisa(self):
        volcado = "\n".join(f"INSERT INTO usuarios VALUES ({n}, 'x');"
                            for n in range(20))
        veredicto = self._clasificar("documentacion/produccion.sql", volcado)
        self.assertIsNotNone(veredicto)
        self.assertEqual(veredicto[0], AVISO)

    def test_config_del_editor_solo_avisa(self):
        # Puede ser deliberado (compartir tareas del equipo): se señala, no bloquea.
        veredicto = self._clasificar(".vscode/tasks.json")
        self.assertEqual(veredicto[0], AVISO)


class Secretos(unittest.TestCase):
    """`04·S4` / `00·N6` — secretos incrustados en el código."""

    def _sev(self, linea):
        h = secretos.revisar_texto(linea)
        return h[0].severidad if h else None

    def test_clave_aws_es_falla(self):
        # Los tokens de estos tests se arman en runtime (prefijo + cuerpo): el
        # literal completo nunca queda en el archivo. Si no, el escaneo de
        # secretos de la plataforma lo toma por real y bloquea el push — que es,
        # justamente, lo que secretos.py hace y este test comprueba.
        aws = "AKIA" + "IOSFODNN7EXAMPLE"
        self.assertEqual(self._sev(f'$key = "{aws}";'), FALLA)

    def test_bloque_de_clave_privada_es_falla(self):
        self.assertEqual(
            self._sev("-----BEGIN RSA PRIVATE KEY-----"), FALLA)

    def test_tokens_de_proveedor_son_falla(self):
        for prefijo, cuerpo in (("sk_live_", "abcdef0123456789ABCD"),
                                ("xoxb-", "1234567890-abcdefghijklmno"),
                                ("ghp_", "0123456789abcdefghijklmnopqrstuvwxyz")):
            with self.subTest(prefijo=prefijo):
                self.assertEqual(self._sev(f'x = "{prefijo}{cuerpo}"'), FALLA)

    def test_password_a_texto_fijo_avisa(self):
        self.assertEqual(self._sev("password = 'S3cretoReal!'"), AVISO)

    def test_leer_del_entorno_no_se_marca(self):
        # Lo correcto: el valor sale de la configuración, no del código.
        for linea in ("$key = env('API_KEY');",
                      "password = os.environ['DB_PASS']",
                      "secret = process.env.CLIENT_SECRET",
                      "token = config('services.slack.token')"):
            with self.subTest(linea=linea):
                self.assertIsNone(self._sev(linea))

    def test_placeholder_no_se_marca(self):
        # Un molde evidente no es un secreto.
        for linea in ("password = 'changeme'",
                      "api_key = 'your-api-key'",
                      "secret = '<tu-secreto>'",
                      "password = 'xxxxxxxx'"):
            with self.subTest(linea=linea):
                self.assertIsNone(self._sev(linea))

    def test_una_linea_un_hallazgo(self):
        # Regresión: no reportar el mismo renglón por dos motivos.
        h = secretos.revisar_texto('key = "' + "AKIA" + 'IOSFODNN7EXAMPLE"')
        self.assertEqual(len(h), 1)


class Dependencias(unittest.TestCase):
    """`10·DEP2` — lockfile presente y versionado."""

    def test_manifiesto_con_lockfile_no_reporta(self):
        self.assertEqual(
            dependencias.revisar(["composer.json", "composer.lock"]), [])

    def test_manifiesto_sin_lockfile_avisa(self):
        h = dependencias.revisar(["composer.json", "app/Http/Kernel.php"])
        self.assertEqual(len(h), 1)
        self.assertEqual(h[0].severidad, AVISO)

    def test_cualquiera_de_los_lockfiles_aceptados_sirve(self):
        # npm/Node admite varios; basta uno.
        self.assertEqual(
            dependencias.revisar(["package.json", "yarn.lock"]), [])

    def test_el_lockfile_debe_estar_en_la_misma_carpeta(self):
        # Un lock en otra carpeta no cubre este manifiesto.
        h = dependencias.revisar(["front/package.json", "package-lock.json"])
        self.assertEqual(len(h), 1)

    def test_manifiesto_de_dependencia_instalada_se_ignora(self):
        # `vendor/.../composer.json` es de un paquete, no la raíz del proyecto.
        self.assertEqual(
            dependencias.revisar(["vendor/laravel/framework/composer.json"]), [])


class Errores(unittest.TestCase):
    """`05·E1` — capturas de error vacías, multi-lenguaje. Núcleo puro."""

    def _n(self, texto):
        return len(errores.revisar_texto(texto))

    def test_catch_con_llaves_vacio_avisa(self):
        self.assertEqual(self._n("try { x(); } catch (e) {}"), 1)

    def test_catch_vacio_en_varias_lineas(self):
        self.assertEqual(self._n("catch (Exception $e) {\n\n}"), 1)

    def test_catch_js_sin_parentesis(self):
        self.assertEqual(self._n("try { a() } catch {  }"), 1)

    def test_except_pass_python(self):
        self.assertEqual(self._n("try:\n    x()\nexcept ValueError:\n    pass"), 1)

    def test_catch_con_manejo_no_avisa(self):
        self.assertEqual(self._n("catch (e) { log(e); }"), 0)

    def test_except_con_manejo_no_avisa(self):
        self.assertEqual(self._n("except ValueError:\n    log(e)\n    raise"), 0)


class Rendimiento(unittest.TestCase):
    """`06·R2` — `SELECT *`. Núcleo puro."""

    def test_select_estrella_avisa(self):
        self.assertEqual(len(rendimiento.revisar_texto('q = "SELECT * FROM t"')), 1)

    def test_select_estrella_minuscula(self):
        self.assertEqual(len(rendimiento.revisar_texto("select * from t")), 1)

    def test_select_con_columnas_no_avisa(self):
        self.assertEqual(len(rendimiento.revisar_texto("SELECT id, nombre FROM t")), 0)


class Esquema(unittest.TestCase):
    """`03·D1` — FK con política de borrado, multi-stack. Núcleo puro."""

    def test_laravel_fk_sin_politica_avisa(self):
        php = "$table->foreignId('user_id')->constrained();"
        self.assertEqual(len(esquema.revisar_esquema("m.php", php)), 1)

    def test_laravel_fk_con_ondelete_no_avisa(self):
        php = "$table->foreign('user_id')->references('id')->on('u')->onDelete('cascade');"
        self.assertEqual(esquema.revisar_esquema("m.php", php), [])

    def test_laravel_cascade_on_delete_helper_no_avisa(self):
        php = "$table->foreignId('user_id')->constrained()->cascadeOnDelete();"
        self.assertEqual(esquema.revisar_esquema("m.php", php), [])

    def test_sql_references_sin_on_delete_avisa(self):
        sql = "FOREIGN KEY (user_id) REFERENCES users(id)"
        self.assertEqual(len(esquema.revisar_esquema("m.sql", sql)), 1)

    def test_sql_references_con_on_delete_no_avisa(self):
        sql = "FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE"
        self.assertEqual(esquema.revisar_esquema("m.sql", sql), [])

    def test_una_sentencia_un_hallazgo(self):
        # `foreignId` + `constrained` en la misma línea = un solo aviso.
        php = "$table->foreignId('u')->constrained('users');"
        self.assertEqual(len(esquema.revisar_esquema("m.php", php)), 1)


class Migraciones(unittest.TestCase):
    """`03·D2` — reversibilidad, multi-stack por detección. Núcleo puro."""

    def _m(self, ruta, texto, hermanos=()):
        return migraciones.revisar_migracion(ruta, texto, hermanos)

    def test_laravel_up_sin_down_avisa(self):
        php = "class X extends Migration {\n  public function up() {}\n}"
        self.assertIsNotNone(self._m("database/migrations/2024_x.php", php))

    def test_laravel_up_y_down_ok(self):
        php = "public function up() {}\n  public function down() {}"
        self.assertIsNone(self._m("database/migrations/2024_x.php", php))

    def test_alembic_sin_downgrade_avisa(self):
        py = "revision = 'ab12'\ndef upgrade():\n    pass"
        self.assertIsNotNone(self._m("alembic/versions/ab12.py", py))

    def test_django_runpython_sin_reverse_avisa(self):
        py = ("from django.db import migrations\n"
              "class Migration(migrations.Migration):\n"
              "    operations = [migrations.RunPython(poblar)]")
        self.assertIsNotNone(self._m("app/migrations/0002_x.py", py))

    def test_django_schema_op_es_reversible(self):
        # AddField y demás se revierten solas: no se aviso.
        py = ("from django.db import migrations, models\n"
              "class Migration(migrations.Migration):\n"
              "    operations = [migrations.AddField('t', 'c', models.IntegerField())]")
        self.assertIsNone(self._m("app/migrations/0003_x.py", py))

    def test_rails_change_es_reversible(self):
        rb = "class X < ActiveRecord::Migration[7.0]\n  def change\n  end\nend"
        self.assertIsNone(self._m("db/migrate/2024_x.rb", rb))

    def test_node_up_sin_down_avisa(self):
        js = "exports.up = (knex) => knex.schema.createTable('t')"
        self.assertIsNotNone(self._m("migrations/2024_x.js", js))

    def test_par_sql_sin_reversion_avisa(self):
        self.assertIsNotNone(
            self._m("migrations/001_init.up.sql", "CREATE TABLE t;", {"001_init.up.sql"}))

    def test_par_sql_con_reversion_ok(self):
        hermanos = {"001_init.up.sql", "001_init.down.sql"}
        self.assertIsNone(
            self._m("migrations/001_init.up.sql", "CREATE TABLE t;", hermanos))

    def test_detecta_las_candidatas_sin_asumir_stack(self):
        self.assertTrue(migraciones.es_candidata("database/migrations/x.php"))
        self.assertTrue(migraciones.es_candidata("app/migrations/0001.py"))
        self.assertTrue(migraciones.es_candidata("db/migrate/x.rb"))
        self.assertTrue(migraciones.es_candidata("m/001.up.sql"))
        self.assertFalse(migraciones.es_candidata("vendor/pkg/migrations/x.php"))
        self.assertFalse(migraciones.es_candidata("app/Models/User.php"))


class Rama(unittest.TestCase):
    """`09·G4` — rama dedicada y al día. Núcleo puro, sin git."""

    def test_rama_dedicada_al_dia_no_reporta(self):
        self.assertEqual(rama.evaluar("HU-003-login", "main", 0), [])

    def test_trabajar_en_la_principal_avisa(self):
        h = rama.evaluar("main", "main", 0)
        self.assertEqual(len(h), 1)
        self.assertEqual(h[0].severidad, AVISO)

    def test_no_asume_el_nombre_de_la_principal(self):
        # `master`, `trunk`… valen igual: lo que importa es que actual == principal.
        self.assertEqual(len(rama.evaluar("master", "master", 0)), 1)
        self.assertEqual(rama.evaluar("feature-x", "master", 0), [])

    def test_rama_atrasada_avisa(self):
        h = rama.evaluar("feature-x", "main", 4)
        self.assertEqual(len(h), 1)
        self.assertIn("4 commit", h[0].mensaje)

    def test_head_desprendido_avisa(self):
        h = rama.evaluar("HEAD", "main", 0)
        self.assertEqual(len(h), 1)
        self.assertEqual(h[0].severidad, AVISO)

    def test_sin_principal_detectable_no_opina(self):
        self.assertEqual(rama.evaluar("cualquiera", None, 0), [])


class Herramientas(unittest.TestCase):
    """Q6/T5/DEP3 — corren la herramienta del stack. Se prueba la detección
    (lo puro); la ejecución depende del toolchain y se verifica a mano."""

    def test_detecta_el_ecosistema_por_manifiesto(self):
        self.assertEqual(herramientas.stack_de_manifiesto("composer.json"), "php")
        self.assertEqual(herramientas.stack_de_manifiesto("package.json"), "node")
        self.assertEqual(herramientas.stack_de_manifiesto("pyproject.toml"), "python")
        self.assertEqual(herramientas.stack_de_manifiesto("Gemfile"), "ruby")
        self.assertIsNone(herramientas.stack_de_manifiesto("README.md"))

    def test_ignora_manifiestos_de_dependencias_instaladas(self):
        self.assertTrue(herramientas._es_instalado("vendor/x/composer.json"))
        self.assertTrue(herramientas._es_instalado("node_modules/y/package.json"))
        self.assertFalse(herramientas._es_instalado("proyectos/app/composer.json"))


class Instalador(unittest.TestCase):

    def test_lee_el_registro_de_proyectos(self):
        proyectos = instalar.proyectos_registrados()
        self.assertTrue(proyectos, "no se leyó plantillas/proyectos.md")
        # El encabezado y la línea de guiones no son proyectos.
        nombres = [n for n, _ in proyectos]
        self.assertNotIn("Proyecto", nombres)
        for _, ruta in proyectos:
            self.assertNotIn("`", ruta)

    def _espacio(self, *repos):
        """Crea un espacio de trabajo temporal con los repos indicados."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        for repo in repos:
            os.makedirs(os.path.join(tmp.name, repo, ".git"))
        return tmp.name

    def test_el_gate_f13_exige_la_carpeta_proyectos(self):
        conforme = self._espacio("proyectos/rni-back")
        self.assertTrue(instalar.cumple_f13(conforme))

        # Caso LocalHub: el código cuelga de la raíz, sin `proyectos/`.
        suelto = self._espacio()
        os.makedirs(os.path.join(suelto, "localhub"))
        self.assertFalse(instalar.cumple_f13(suelto))

    def test_encuentra_los_repos_dentro_de_proyectos(self):
        # Caso RNI: la raíz no está versionada; el código son DOS repos
        # independientes dentro de `proyectos/` (02·F13).
        raiz = self._espacio("proyectos/rni-back", "proyectos/rni-front")
        hallados = [os.path.relpath(r, raiz).replace("\\", "/")
                    for r in instalar.repositorios_git(raiz)]
        self.assertEqual(hallados, ["proyectos/rni-back", "proyectos/rni-front"])

    def test_un_solo_repo_en_la_raiz(self):
        # Caso AgroSystem: todo el espacio es un único repositorio.
        raiz = self._espacio(".")
        self.assertEqual(instalar.repositorios_git(raiz), [raiz])

    def test_sin_repos_no_devuelve_nada(self):
        # Caso LocalHub: no está bajo git.
        raiz = self._espacio()
        os.makedirs(os.path.join(raiz, "documentacion"))
        self.assertEqual(instalar.repositorios_git(raiz), [])

    def _grupo(self, comandos):
        return {"matcher": "Write|Edit",
                "hooks": [{"type": "command", "command": c} for c in comandos]}

    def test_reemplaza_un_enganche_propio_en_vez_de_duplicarlo(self):
        # Regresión: al cambiar el comando, la versión anterior quedaba
        # corriendo en paralelo con la nueva.
        datos = {"hooks": {"PostToolUse": [
            self._grupo(["prettier --write x",
                         'python "/viejo/validadores/hook_md.py"'])]}}
        grupo = datos["hooks"]["PostToolUse"][0]
        propios = [i for i, h in enumerate(grupo["hooks"])
                   if "hook_md.py" in h["command"]]
        self.assertEqual(propios, [1], "no reconoció el enganche propio")
        self.assertEqual(len(grupo["hooks"]) - len(propios), 1,
                         "no debe tocar los hooks ajenos")


if __name__ == "__main__":
    unittest.main(verbosity=2)
