#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Suite de los validadores. Solo biblioteca estándar.

    python validadores/pruebas.py

Cubre las reglas y, sobre todo, los **falsos positivos** que se detectaron al
probar contra el repositorio real: son los que hacen que nadie confíe en un
validador y termine ignorándolo.
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import commits          # noqa: E402
import dependencias     # noqa: E402
import enlaces          # noqa: E402
import fases            # noqa: E402
import instalar         # noqa: E402
import aislamiento      # noqa: E402
import calidad          # noqa: E402
import checklist        # noqa: E402
import ci               # noqa: E402
import citas            # noqa: E402
import errores          # noqa: E402
import esquema          # noqa: E402
import flujo            # noqa: E402
import herramientas     # noqa: E402
import historico        # noqa: E402
import migraciones      # noqa: E402
import plantillas       # noqa: E402
import rama             # noqa: E402
import recuerdos        # noqa: E402
import rendimiento      # noqa: E402
import resumen          # noqa: E402
import secretos         # noqa: E402
import seguridad        # noqa: E402
import trazabilidad     # noqa: E402
import version          # noqa: E402
import versionado       # noqa: E402
import versiones        # noqa: E402
import comun            # noqa: E402
from comun import AVISO, FALLA, lineas_utiles, marcadores  # noqa: E402


def _claude_md_completo(proyecto="demo"):
    """La plantilla central ya rellenada, como la deja el instalador."""
    plantilla = versiones.POR_ID["claude-md"].ruta_plantilla()
    return instalar._rellenar(comun.leer(plantilla),
                              instalar._rellenos(proyecto))


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

    def test_e5_log_con_password_avisa(self):
        self.assertEqual(self._n('Log::info("Login", ["email" => $email, "password" => $pass]);'), 1)

    def test_e5_console_log_con_token_avisa(self):
        self.assertEqual(self._n("console.log('auth', token)"), 1)

    def test_e5_log_sin_secreto_no_avisa(self):
        self.assertEqual(self._n('Log::info("Login ok", ["user_id" => $id]);'), 0)


class Rendimiento(unittest.TestCase):
    """`06·R2` — `SELECT *`. Núcleo puro."""

    def test_select_estrella_avisa(self):
        self.assertEqual(len(rendimiento.revisar_texto('q = "SELECT * FROM t"')), 1)

    def test_select_estrella_minuscula(self):
        self.assertEqual(len(rendimiento.revisar_texto("select * from t")), 1)

    def test_select_con_columnas_no_avisa(self):
        self.assertEqual(len(rendimiento.revisar_texto("SELECT id, nombre FROM t")), 0)

    def _n1(self, texto):
        return sum(1 for h in rendimiento.revisar_texto(texto) if "N+1" in h.mensaje)

    def test_r1_consulta_en_foreach_avisa(self):
        php = "foreach ($ids as $id) {\n  $c = Cliente::find($id);\n}"
        self.assertEqual(self._n1(php), 1)

    def test_r1_consulta_en_for_python_avisa(self):
        py = "for id in ids:\n    c = Cliente.objects.get(pk=id)\n    print(c)"
        self.assertEqual(self._n1(py), 1)

    def test_r1_bucle_sin_consulta_no_avisa(self):
        php = "foreach ($items as $i) {\n  $total += $i->precio;\n}"
        self.assertEqual(self._n1(php), 0)


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

    def _motivos(self, ruta, texto):
        return [mot for _, mot in esquema.revisar_esquema(ruta, texto)]

    def test_d3_columna_nueva_sin_default_en_alter_avisa(self):
        php = "Schema::table('users', function (Blueprint $table) {\n  $table->string('nit');\n});"
        self.assertTrue(any("D3" in m for m in self._motivos("m.php", php)))

    def test_d3_columna_con_default_o_nullable_no_avisa(self):
        php = "Schema::table('users', function ($t) {\n  $t->string('nit')->default('');\n});"
        self.assertFalse(any("D3" in m for m in self._motivos("m.php", php)))

    def test_d3_no_aplica_al_crear_tabla(self):
        # En una tabla nueva NOT NULL está bien: no hay filas que romper.
        php = "Schema::create('t', function ($t) {\n  $t->string('nit');\n});"
        self.assertFalse(any("D3" in m for m in self._motivos("m.php", php)))

    def test_d3_sql_add_not_null_sin_default_avisa(self):
        sql = "ALTER TABLE users ADD COLUMN nit VARCHAR(20) NOT NULL;"
        self.assertTrue(any("D3" in m for m in self._motivos("m.sql", sql)))

    def test_est2_identificador_muy_largo_avisa(self):
        largo = "x" + "a" * 70
        php = f"$table->boolean('{largo}');"
        self.assertTrue(any("EST2" in m for m in self._motivos("m.php", php)))


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


class Version(unittest.TestCase):
    """`pendiente 04` — desfase de versión. Núcleo puro."""

    def test_extrae_la_version_adoptada(self):
        txt = "- **Versión del estándar adoptada:** `1.2.0` · sellada `2026-08-06`"
        self.assertEqual(version.extraer_adoptada(txt), "1.2.0")

    def test_placeholder_sin_llenar_no_matchea(self):
        self.assertIsNone(version.extraer_adoptada("adoptada: `«X.Y.Z»`"))

    def test_al_dia_no_avisa(self):
        self.assertIsNone(version.comparar("1.0.0", "1.0.0"))
        self.assertIsNone(version.comparar("1.1.0", "1.0.0"))     # adelante: tampoco

    def test_por_detras_avisa(self):
        m = version.comparar("1.0.0", "1.2.0")
        self.assertIsNotNone(m)
        self.assertIn("1.2.0", m)

    def test_sin_declarar_avisa(self):
        self.assertIsNotNone(version.comparar(None, "1.0.0"))

    def test_estandar_sin_version_no_opina(self):
        self.assertIsNone(version.comparar(None, None))


class CI(unittest.TestCase):
    """`09·G6` — pipeline de CI. Núcleo puro."""

    def test_sin_ci_avisa(self):
        self.assertEqual(len(ci.revisar_ci([])), 1)

    def test_ci_con_pruebas_y_linter_no_avisa(self):
        yml = "jobs:\n  test:\n    run: phpunit\n  lint:\n    run: pint --test"
        self.assertEqual(ci.revisar_ci([yml]), [])

    def test_ci_sin_linter_avisa(self):
        self.assertTrue(any("linter" in m for m in ci.revisar_ci(["run: phpunit"])))

    def test_detecta_los_archivos_de_ci(self):
        for ruta in (".github/workflows/ci.yml", ".gitlab-ci.yml", "Jenkinsfile"):
            self.assertRegex(ruta, ci._CI)


class Seguridad_S5(unittest.TestCase):
    """`04·S5` — flags de cookie de sesión (en seguridad.py)."""

    def test_http_only_false_avisa(self):
        self.assertTrue(any("S5" in h.mensaje
                            for h in seguridad.revisar_texto("'http_only' => false,")))

    def test_secure_true_no_avisa(self):
        self.assertFalse(any("S5" in h.mensaje
                             for h in seguridad.revisar_texto("'secure' => true,")))


class Flujo(unittest.TestCase):
    """`02·F14`/`F17` — el plan de trabajo. Núcleo puro."""

    def _plan_completo(self):
        return "\n".join(f"## {n}. Sección" for n in range(0, 14))

    def test_plan_completo_no_reporta(self):
        faltan, inc = flujo.revisar_plan(self._plan_completo())
        self.assertEqual(faltan, [])
        self.assertEqual(inc, [])

    def test_secciones_faltantes_se_listan(self):
        texto = "## 0. Id\n## 1. Alcance\n## 13. Cierre"
        faltan, _ = flujo.revisar_plan(texto)
        self.assertIn(5, faltan)
        self.assertNotIn(0, faltan)
        self.assertNotIn(13, faltan)

    def test_marca_de_incertidumbre_se_reporta(self):
        texto = self._plan_completo() + "\n- ruta: app/Foo.php (o similar)"
        _, inc = flujo.revisar_plan(texto)
        self.assertEqual(len(inc), 1)

    def test_tbd_se_reporta(self):
        _, inc = flujo.revisar_plan("## 0.\ntabla: TBD")
        self.assertTrue(any("TBD" in frag for _, frag in inc))


class FlujoF0(unittest.TestCase):
    """`02·F0` — padres de cada fase. Contra un árbol temporal."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def _fase(self, con_doc_hu, con_doc_epica):
        base = os.path.join(self.tmp.name, "documentacion", "epicas",
                            "EP-001-x", "HU-001-y", "A-EP-001-HU-001-z")
        os.makedirs(base)
        hu = os.path.join(self.tmp.name, "documentacion", "epicas", "EP-001-x", "HU-001-y")
        ep = os.path.join(self.tmp.name, "documentacion", "epicas", "EP-001-x")
        if con_doc_hu:
            open(os.path.join(hu, "HU-001-y.md"), "w").close()
        if con_doc_epica:
            open(os.path.join(ep, "epica.md"), "w").close()
        return self.tmp.name

    def test_padres_presentes_no_reportan_f0(self):
        raiz = self._fase(True, True)
        self.assertFalse(any("F0" in h.mensaje for h in flujo.validar(raiz)))

    def test_hu_sin_documento_reporta_f0(self):
        raiz = self._fase(False, True)
        self.assertTrue(any("F0" in h.mensaje and "HU" in h.mensaje
                            for h in flujo.validar(raiz)))

    def test_epica_sin_documento_reporta_f0_una_vez(self):
        raiz = self._fase(True, False)
        n = sum(1 for h in flujo.validar(raiz) if "F0" in h.mensaje and "épica" in h.mensaje)
        self.assertEqual(n, 1)


class Plantillas_docs(unittest.TestCase):
    """El mapeo cubre los documentos del proyecto por su nombre real."""

    def test_deduce_docs_del_proyecto(self):
        for base, esperado in (("plan_trabajo", "planes/trabajo.md"),
                               ("funcionalidad_implementada", "funcionalidad-implementada.md"),
                               ("reglas-proyecto", "reglas-proyecto.md")):
            ruta = plantillas.deducir_plantilla(f"documentacion/x/{base}.md", "")
            self.assertIsNotNone(ruta, base)
            self.assertTrue(ruta.replace("\\", "/").endswith(esperado), base)


class Seguridad(unittest.TestCase):
    """`04·S3` — concatenación e inyección. Núcleo puro."""

    def _msgs(self, texto):
        return [h.mensaje for h in seguridad.revisar_texto(texto)]

    def test_sql_concatenado_avisa(self):
        php = '$q = "SELECT * FROM users WHERE id = " . $id;'
        self.assertTrue(any("SQL" in m for m in self._msgs(php)))

    def test_consulta_parametrizada_no_avisa(self):
        php = 'DB::select("SELECT * FROM users WHERE id = ?", [$id]);'
        self.assertFalse(any("SQL" in m for m in self._msgs(php)))

    def test_shell_con_concatenacion_avisa(self):
        php = 'exec("convert " . $archivo . " out.png");'
        self.assertTrue(any("shell" in m.lower() for m in self._msgs(php)))

    def test_guarded_vacio_avisa(self):
        self.assertTrue(any("masiva" in m for m in self._msgs("protected $guarded = [];")))

    def test_all_al_modelo_avisa(self):
        self.assertTrue(any("payload" in m for m in self._msgs("User::create($request->all());")))


class Calidad(unittest.TestCase):
    """`07·Q3` — funciones largas. Núcleo puro."""

    def test_funcion_larga_avisa(self):
        cuerpo = "\n".join(f"    $x = {i};" for i in range(calidad.TOPE + 5))
        php = "function grande() {\n" + cuerpo + "\n}"
        self.assertEqual(len(calidad.revisar_texto(php)), 1)

    def test_funcion_corta_no_avisa(self):
        php = "function chica() {\n  return 1;\n}"
        self.assertEqual(calidad.revisar_texto(php), [])

    def test_def_python_largo_avisa(self):
        cuerpo = "\n".join(f"    x = {i}" for i in range(calidad.TOPE + 5))
        py = "def grande():\n" + cuerpo
        self.assertEqual(len(calidad.revisar_texto(py)), 1)


class Aislamiento(unittest.TestCase):
    """`08·T4` — pruebas contra BD efímera. Núcleo puro."""

    def test_memoria_no_avisa(self):
        xml = '<env name="DB_CONNECTION" value="sqlite"/><env name="DB_DATABASE" value=":memory:"/>'
        self.assertIsNone(aislamiento.revisar_phpunit(xml))

    def test_bd_de_test_no_avisa(self):
        xml = '<env name="DB_DATABASE" value="agro_testing"/>'
        self.assertIsNone(aislamiento.revisar_phpunit(xml))

    def test_bd_real_avisa(self):
        xml = '<env name="DB_DATABASE" value="agro_produccion"/>'
        self.assertIsNotNone(aislamiento.revisar_phpunit(xml))

    def test_orden_aleatorio_no_avisa(self):
        self.assertIsNone(aislamiento.revisar_orden('<phpunit executionOrder="random">'))

    def test_sin_orden_aleatorio_avisa(self):
        self.assertIsNotNone(aislamiento.revisar_orden("<phpunit>"))

    def test_fuente_flaky_en_prueba_se_reporta(self):
        self.assertEqual(len(aislamiento.revisar_test("$x = mt_rand(1, 9);")), 1)

    def test_prueba_determinista_no_se_reporta(self):
        self.assertEqual(aislamiento.revisar_test("$x = 5;"), [])

    def test_sin_config_ni_env_testing_avisa(self):
        self.assertIsNotNone(aislamiento.revisar_phpunit("<phpunit></phpunit>", hay_env_testing=False))

    def test_sin_config_pero_con_env_testing_no_avisa(self):
        self.assertIsNone(aislamiento.revisar_phpunit("<phpunit></phpunit>", hay_env_testing=True))


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

    def test_el_historico_se_instala_en_dos_eventos(self):
        # El mismo guion cumple dos papeles; si se instalara uno solo, la
        # transcripción quedaría a medias (sin usuario, o sin agente).
        eventos = {e: args for e, _, g, _, args in instalar.HOOKS_CLAUDE
                   if g == "hook_historico.py"}
        self.assertEqual(eventos, {"UserPromptSubmit": "--modo usuario",
                                   "Stop": "--modo agente"})

    def test_los_argumentos_van_antes_de_la_raiz(self):
        cmd = instalar._hook_claude("/estandar", "/proy", "hook_historico.py",
                                    "…", "--modo agente")["command"]
        self.assertIn('hook_historico.py" --modo agente --raiz "/proy"', cmd)

    def test_crea_la_carpeta_del_historico_y_no_la_pisa(self):
        raiz = self._espacio()
        self.assertEqual(instalar.instalar_historico(raiz, aplicar=True),
                         ["crear historico-chat/README.md",
                          "crear historico-chat/resumenes/README.md"])
        indice = os.path.join(raiz, "historico-chat", "README.md")
        self.assertTrue(os.path.isfile(indice))
        # La carpeta de resúmenes va en la misma instalación: sin ella el
        # enganche del resumen queda mudo en el proyecto.
        self.assertTrue(os.path.isfile(
            os.path.join(raiz, "historico-chat", "resumenes", "README.md")))

        # Se crea ya sellado: quedar viejo tiene que poder detectarse después.
        comp = versiones.POR_ID["historico"]
        self.assertEqual(versiones.huella_sellada(raiz, comp),
                         versiones.huella_central(comp))

        with open(indice, "a", encoding="utf-8") as f:
            f.write("\n- línea del proyecto\n")
        self.assertEqual(instalar.instalar_historico(raiz, aplicar=True),
                         ["historico-chat/README.md ya estaba sellado al día"])
        with open(indice, encoding="utf-8") as f:
            self.assertIn("línea del proyecto", f.read())

    def test_al_readme_del_historico_solo_se_le_refresca_el_sello(self):
        # El contenido es del proyecto y no se pisa; lo único que el estándar
        # escribe ahí es contra qué plantilla se sincronizó.
        raiz = self._espacio()
        instalar.instalar_historico(raiz, aplicar=True)
        indice = os.path.join(raiz, "historico-chat", "README.md")

        with open(indice, "w", encoding="utf-8") as f:
            f.write("# El mío, reescrito entero\n")
        pasos = instalar.instalar_historico(raiz, aplicar=True)
        self.assertTrue(any("sellar" in p for p in pasos), pasos)

        with open(indice, encoding="utf-8") as f:
            texto = f.read()
        self.assertIn("El mío, reescrito entero", texto)
        self.assertIn("<!-- huella:", texto)

    def test_sella_el_claude_md_sin_tocarle_el_contenido(self):
        raiz = self._espacio()
        local = os.path.join(raiz, "CLAUDE.md")
        # Con todas las secciones de la plantilla, para que no haya nada que
        # agregar: lo único que debe pasar es que se selle.
        with open(local, "w", encoding="utf-8") as f:
            f.write(_claude_md_completo() + "\nlo mío\n")

        instalar.instalar_claude_md(raiz, aplicar=True)
        with open(local, encoding="utf-8") as f:
            texto = f.read()
        self.assertIn("lo mío", texto)
        self.assertEqual(
            versiones.huella_sellada(raiz, versiones.POR_ID["claude-md"]),
            versiones.huella_central(versiones.POR_ID["claude-md"]))

        # Segunda corrida: idempotente, no reescribe ni duplica el sello.
        self.assertEqual(instalar.instalar_claude_md(raiz, aplicar=True),
                         ["CLAUDE.md ya estaba sellado al día"])
        # Solo los sellos de verdad: la plantilla menciona uno de ejemplo
        # dentro de una frase, y ese no es un sello.
        with open(local, encoding="utf-8") as f:
            sellos = [l for l in f.read().splitlines()
                      if l.startswith("<!-- huella:")]
        self.assertEqual(len(sellos), 1, sellos)

    def test_sin_claude_md_se_genera_lleno_desde_la_plantilla(self):
        """Antes había que copiarlo y llenarlo a mano; ahora lo pone el instalador.

        Que no queden marcadores es lo que se comprueba: un `CLAUDE.md` con
        huecos reprueba el checklist, así que generarlo a medias sería mover el
        trabajo manual de sitio, no quitarlo.
        """
        raiz = self._espacio()
        pasos = instalar.instalar_claude_md(raiz, aplicar=True)
        self.assertIn("crear CLAUDE.md", pasos[0])

        with open(os.path.join(raiz, "CLAUDE.md"), encoding="utf-8") as f:
            texto = f.read()
        self.assertIsNone(instalar._MARCADOR.search(texto), texto[:400])
        self.assertIn(version.version_estandar(), texto)
        self.assertIn(comun.RAIZ.replace("\\", "/"), texto)

    def test_al_claude_md_solo_se_le_agrega_lo_que_la_plantilla_sumo(self):
        """`01·C18` es aditiva: no se pisa, no se reordena, no se borra."""
        raiz = self._espacio()
        local = os.path.join(raiz, "CLAUDE.md")
        completo = _claude_md_completo()
        recortado = completo.split("## 4. Precedencia")[0]
        with open(local, "w", encoding="utf-8") as f:
            f.write(recortado + "\n## Sección propia\n\nmía y de nadie más\n")

        pasos = instalar.instalar_claude_md(raiz, aplicar=True)
        self.assertTrue(any("lo que la plantilla sumó" in p for p in pasos), pasos)

        with open(local, encoding="utf-8") as f:
            texto = f.read()
        self.assertIn("mía y de nadie más", texto)
        self.assertIn("## 4. Precedencia", texto)
        self.assertEqual(texto.count("## 1. Ubicación del estándar"), 1)

    def test_la_estructura_base_se_crea_sola_y_no_toca_lo_que_hay(self):
        """`02·F13`: la carpeta la crea el instalador, el contenido es del usuario."""
        raiz = self._espacio()
        ajeno = os.path.join(raiz, "proyectos", "app")
        os.makedirs(ajeno)

        instalar.instalar_estructura(raiz, aplicar=True)
        for carpeta in instalar.CARPETAS_BASE:
            self.assertTrue(os.path.isdir(os.path.join(raiz, carpeta)), carpeta)
        self.assertTrue(os.path.isdir(ajeno), "se tocó el código del usuario")

        self.assertEqual(instalar.instalar_estructura(raiz, aplicar=True),
                         ["la estructura base ya estaba"])

    def test_el_gitignore_solo_se_le_agrega_lo_que_falta(self):
        raiz = self._espacio()
        archivo = os.path.join(raiz, ".gitignore")
        with open(archivo, "w", encoding="utf-8") as f:
            f.write("# lo mío\nnode_modules/\nCLAUDE.md\n")

        instalar.instalar_gitignore(raiz, aplicar=True)
        with open(archivo, encoding="utf-8") as f:
            lineas = f.read().splitlines()
        self.assertIn("node_modules/", lineas)
        self.assertEqual(lineas.count("CLAUDE.md"), 1, "se duplicó una línea")
        self.assertIn(".agente/", lineas)

        self.assertEqual(instalar.instalar_gitignore(raiz, aplicar=True),
                         ["el .gitignore ya ignoraba la configuración local"])

    def test_los_cuatro_archivos_de_agente_se_ponen_y_no_se_pisan(self):
        raiz = self._espacio()
        instalar.instalar_agente_config(raiz, aplicar=True)
        stack = os.path.join(raiz, ".agente", "stack.md")
        for nombre in instalar.CONFIG_AGENTE:
            self.assertTrue(os.path.isfile(os.path.join(raiz, ".agente", nombre)))

        with open(stack, "w", encoding="utf-8") as f:
            f.write("# lo que declaró el proyecto\n")
        self.assertEqual(instalar.instalar_agente_config(raiz, aplicar=True),
                         ["los 4 archivos de .agente/ ya estaban"])
        with open(stack, encoding="utf-8") as f:
            self.assertIn("lo que declaró el proyecto", f.read())

    def test_el_propio_estandar_no_se_trata_como_un_proyecto(self):
        """Es donde viven las reglas: no tiene `proyectos/` ni ignora su CLAUDE.md."""
        self.assertTrue(instalar.es_el_estandar(comun.RAIZ))
        self.assertFalse(instalar.es_el_estandar(self._espacio()))


class Historico(unittest.TestCase):
    """El enganche que escribe la transcripción de la sesión."""

    def _carpeta(self, contenido=None):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        os.makedirs(os.path.join(tmp.name, "historico-chat"))
        if contenido is not None:
            ruta = os.path.join(tmp.name, "historico-chat", "2026-01-01-x.md")
            with open(ruta, "w", encoding="utf-8", newline="\n") as f:
                f.write(contenido)
        return tmp.name

    def _leer(self, ruta):
        with open(ruta, encoding="utf-8") as f:
            return f.read()

    def test_el_primer_mensaje_crea_el_archivo(self):
        raiz = self._carpeta()
        ruta = historico.anotar_usuario(raiz, "s1", "hola")
        self.assertTrue(ruta, "un saludo también abre el histórico")
        texto = self._leer(ruta)
        self.assertIn("<!-- sesion: s1 -->", texto)
        self.assertIn("### 1 · Usuario — ", texto)
        self.assertIn("> hola", texto)

    def test_sin_carpeta_no_inventa_nada(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.assertEqual(historico.anotar_usuario(tmp.name, "s1", "hola"), "")

    def test_sigue_la_numeracion_y_respeta_abierto(self):
        raiz = self._carpeta("<!-- sesion: s2 -->\n\n# t\n\n## Conversación\n\n"
                             "### 7 · Usuario — 2026-01-01 00:00:00\n> vieja\n\n"
                             "## Abierto\n- nada.\n")
        ruta = historico.anotar_usuario(raiz, "s2", "nueva")
        texto = self._leer(ruta)
        self.assertIn("### 8 · Usuario — ", texto)
        self.assertLess(texto.index("### 8"), texto.index("## Abierto"),
                        "el mensaje nuevo quedó por debajo de `## Abierto`")

    def test_no_duplica_la_respuesta_si_el_enganche_repite(self):
        raiz = self._carpeta("<!-- sesion: s3 -->\n\n# t\n\n## Conversación\n")
        transcripcion = os.path.join(raiz, "t.jsonl")
        with open(transcripcion, "w", encoding="utf-8") as f:
            f.write(json.dumps({"type": "user",
                                "message": {"content": "pregunta"}}) + "\n")
            f.write(json.dumps({"type": "assistant", "uuid": "u1",
                                "message": {"content": [
                                    {"type": "text", "text": "respuesta"}]}}))

        self.assertTrue(historico.anotar_agente(raiz, "s3", transcripcion))
        self.assertEqual(historico.anotar_agente(raiz, "s3", transcripcion), "")

    def test_la_sesion_queda_en_el_indice_aunque_el_readme_llegue_despues(self):
        # La línea del índice es lo único por lo que la próxima sesión
        # encuentra a esta: si al crear el archivo no había README, la sesión
        # quedaba invisible para siempre.
        raiz = self._carpeta()
        carpeta = os.path.join(raiz, "historico-chat")
        ruta = historico.anotar_usuario(raiz, "s4", "primero")

        with open(os.path.join(carpeta, "README.md"), "w",
                  encoding="utf-8") as f:
            f.write("# Histórico\n\n## Índice\n\n")

        historico.anotar_usuario(raiz, "s4", "segundo")
        indice = self._leer(os.path.join(carpeta, "README.md"))
        self.assertIn(f"({os.path.basename(ruta)})", indice)
        self.assertEqual(indice.count(os.path.basename(ruta)), 2,
                         "la línea se duplicó: el índice no es idempotente")

    def test_el_indice_alimenta_el_arranque_de_la_proxima_sesion(self):
        raiz = self._carpeta()
        with open(os.path.join(raiz, "historico-chat", "README.md"), "w",
                  encoding="utf-8") as f:
            f.write("# Histórico\n\n## Índice\n\n"
                    "- [2026-01-01-x.md](2026-01-01-x.md) — de qué se trató.\n"
                    "- [README.md](README.md) — no es una sesión.\n")

        self.assertEqual(historico.sesiones(raiz),
                         [("2026-01-01-x.md", "de qué se trató.")])
        texto = historico.contexto(raiz)
        self.assertIn("historico-chat/2026-01-01-x.md — de qué se trató.", texto)
        self.assertNotIn("README.md", texto)

    def test_sin_sesiones_no_se_inyecta_nada(self):
        self.assertEqual(historico.contexto(self._carpeta()), "")

    def test_se_recortan_las_sesiones_viejas_y_se_dice(self):
        raiz = self._carpeta()
        filas = "".join(f"- [s{n}.md](s{n}.md) — tema {n}.\n" for n in range(10))
        with open(os.path.join(raiz, "historico-chat", "README.md"), "w",
                  encoding="utf-8") as f:
            f.write(f"# Histórico\n\n## Índice\n\n{filas}")

        texto = historico.contexto(raiz, limite=3)
        self.assertIn("últimas 3 de 10", texto)
        self.assertIn("s9.md", texto)
        self.assertNotIn("s6.md", texto, "se listó una fuera del recorte")

    def test_junta_el_texto_partido_por_herramientas_y_descarta_lo_ajeno(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        ruta = os.path.join(tmp.name, "t.jsonl")
        filas = [
            {"type": "user", "message": {"content": "pregunta real"}},
            {"type": "assistant", "uuid": "a1", "message": {"content": [
                {"type": "thinking", "thinking": "razonamiento"},
                {"type": "text", "text": "Primero."},
                {"type": "tool_use", "name": "Bash"}]}},
            {"type": "user", "message": {"content": [
                {"type": "tool_result", "content": "salida cruda"}]}},
            {"type": "assistant", "uuid": "a2", "message": {"content": [
                {"type": "text", "text": "Después."}]}},
            {"type": "assistant", "uuid": "a3", "isSidechain": True,
             "message": {"content": [{"type": "text", "text": "subagente"}]}},
        ]
        with open(ruta, "w", encoding="utf-8") as f:
            f.write("\n".join(json.dumps(x) for x in filas))

        texto, marca = historico.ultima_respuesta(ruta)
        self.assertEqual(texto, "Primero.\n\nDespués.")
        self.assertEqual(marca, "a2")


class Recuerdos(unittest.TestCase):
    """La memoria del agente: en el repositorio, y solo ahí (`01·C19`)."""

    def _monta(self, locales=None, repo=None):
        """Un proyecto temporal con su carpeta local y su carpeta del repo."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        proyecto = os.path.join(tmp.name, "proyecto")
        casa = os.path.join(tmp.name, "casa")

        for carpeta, archivos in ((recuerdos.carpeta_local(proyecto, casa),
                                   locales or {}),
                                  (recuerdos.carpeta_repo(proyecto),
                                   repo or {})):
            if archivos:
                os.makedirs(carpeta, exist_ok=True)
            for nombre, texto in archivos.items():
                with open(os.path.join(carpeta, nombre), "w",
                          encoding="utf-8") as f:
                    f.write(texto)
        return proyecto, casa

    def _leer(self, *partes):
        with open(os.path.join(*partes), encoding="utf-8") as f:
            return f.read()

    def test_la_carpeta_local_es_la_que_usa_la_herramienta(self):
        proyecto, casa = self._monta()
        local = recuerdos.carpeta_local(os.path.join(proyecto, "Ing. Jose"),
                                        casa)
        self.assertTrue(local.startswith(
            os.path.join(casa, ".claude", "projects")))
        self.assertEqual(os.path.basename(local), "memory")
        # El punto y el espacio son dos caracteres: dan dos guiones, no uno.
        self.assertTrue(os.path.basename(os.path.dirname(local))
                        .endswith("Ing--Jose"))

    def test_mueve_el_recuerdo_al_repositorio(self):
        proyecto, casa = self._monta({"lo-mio.md": "el recuerdo"})
        self.assertEqual(recuerdos.migrar(proyecto, True, casa),
                         [("lo-mio.md", "lo-mio.md")])
        self.assertEqual(recuerdos.sueltos(proyecto, casa), [])
        self.assertEqual(
            self._leer(recuerdos.carpeta_repo(proyecto), "lo-mio.md"),
            "el recuerdo")

    def test_simular_no_toca_nada(self):
        proyecto, casa = self._monta({"lo-mio.md": "el recuerdo"})
        self.assertTrue(recuerdos.migrar(proyecto, False, casa))
        self.assertTrue(recuerdos.sueltos(proyecto, casa),
                        "sin --aplicar no se mueve nada")

    def test_el_duplicado_identico_tampoco_se_borra(self):
        # Antes se borraba el del almacén "porque no se pierde nada". Con el
        # almacén enlazado al repositorio, ese razonamiento destruyó memoria
        # real: los dos eran el mismo archivo. Aquí no se borra nunca.
        proyecto, casa = self._monta({"x.md": "igual"}, {"x.md": "igual"})
        self.assertEqual(recuerdos.migrar(proyecto, True, casa),
                         [("x.md", "x-local.md")])
        repo = recuerdos.carpeta_repo(proyecto)
        self.assertEqual(self._leer(repo, "x.md"), "igual")
        self.assertEqual(self._leer(repo, "x-local.md"), "igual")

    def test_el_almacen_enlazado_a_la_carpeta_del_repo_ya_cumple(self):
        # Caso real: la carpeta de la herramienta es un junction a
        # `historico-chat/memory/`. Origen y destino son el MISMO archivo —
        # moverlo o compararlo consigo mismo es la forma de perderlo.
        proyecto, casa = self._monta(repo={"x.md": "el recuerdo",
                                           "memory.md": "# Índice"})
        original = recuerdos.carpeta_local
        recuerdos.carpeta_local = lambda p, c=None: recuerdos.carpeta_repo(p)
        self.addCleanup(setattr, recuerdos, "carpeta_local", original)

        self.assertTrue(recuerdos.enlazada(proyecto))
        self.assertEqual(recuerdos.sueltos(proyecto), [])
        self.assertEqual(recuerdos.migrar(proyecto, True), [])
        self.assertEqual(recuerdos.revisar(proyecto), (True, ""))

        repo = recuerdos.carpeta_repo(proyecto)
        self.assertEqual(sorted(os.listdir(repo)), ["memory.md", "x.md"],
                         "el enlace se llevó la memoria por delante")

        # Y el instalador tampoco toca la carpeta.
        self.assertEqual(instalar.instalar_recuerdos(proyecto, aplicar=True),
                         ["memoria enlazada a `historico-chat/memory/`: "
                          "ya cumple, no se toca"])
        self.assertEqual(self._leer(repo, "memory.md"), "# Índice")

    def test_el_indice_de_la_herramienta_cuenta_como_indice(self):
        # En Windows `MEMORY.md` y `memory.md` son el mismo archivo: preguntar
        # por el nombre exacto haría que el instalador lo diera por ausente y
        # lo escribiera encima.
        proyecto, _ = self._monta(repo={"MEMORY.md": "el índice del proyecto"})
        self.assertTrue(recuerdos.indice_presente(proyecto))
        instalar.instalar_recuerdos(proyecto, aplicar=True)
        # Se le agrega el sello —eso sí lo escribe el estándar—, pero el
        # contenido del proyecto queda intacto: no se escribió uno nuevo encima.
        self.assertIn("el índice del proyecto",
                      self._leer(recuerdos.carpeta_repo(proyecto), "MEMORY.md"))

    def test_un_nombre_ocupado_no_se_pisa(self):
        # Lo local puede ser otra versión: decidir cuál manda es del usuario.
        proyecto, casa = self._monta({"x.md": "la local"}, {"x.md": "la del repo"})
        self.assertEqual(recuerdos.migrar(proyecto, True, casa),
                         [("x.md", "x-local.md")])
        repo = recuerdos.carpeta_repo(proyecto)
        self.assertEqual(self._leer(repo, "x.md"), "la del repo")
        self.assertEqual(self._leer(repo, "x-local.md"), "la local")

    def test_el_indice_no_se_pierde_por_las_mayusculas(self):
        # Regresión: en Windows `MEMORY.md` y `memory.md` son el MISMO archivo.
        # Moviendo uno sobre otro se borraba el índice del proyecto en silencio.
        proyecto, casa = self._monta({"MEMORY.md": "el índice de la herramienta"},
                                     {"memory.md": "el índice del proyecto"})
        movidos = recuerdos.migrar(proyecto, True, casa)
        self.assertEqual(movidos, [("MEMORY.md", "MEMORY-local.md")])
        self.assertEqual(self._leer(recuerdos.carpeta_repo(proyecto),
                                    "memory.md"), "el índice del proyecto")

    def test_reprueba_mientras_quede_algo_en_la_carpeta_local(self):
        proyecto, casa = self._monta({"x.md": "lo mío"})
        cumple, detalle = recuerdos.revisar(proyecto, casa)
        self.assertFalse(cumple)
        self.assertIn("x.md", detalle)

        recuerdos.migrar(proyecto, True, casa)
        self.assertEqual(recuerdos.revisar(proyecto, casa), (True, ""))

    def test_la_memoria_se_inyecta_al_arrancar(self):
        # La herramienta solo carga sola lo que guarda ella, y ahí ya no hay
        # nada: sin esto, la memoria del repositorio no la vería nadie.
        proyecto, _ = self._monta(repo={"memory.md": "# Índice\n\n| a | b |\n"})
        texto = recuerdos.contexto(proyecto)
        self.assertIn("MEMORIA DEL AGENTE", texto)
        self.assertIn("| a | b |", texto)

    def test_sin_indice_no_se_inyecta_nada(self):
        proyecto, _ = self._monta()
        self.assertEqual(recuerdos.contexto(proyecto), "")

    def test_el_instalador_crea_el_indice_sellado_y_no_lo_pisa(self):
        proyecto, _ = self._monta()
        os.makedirs(proyecto, exist_ok=True)
        pasos = instalar.instalar_recuerdos(proyecto, aplicar=True)
        self.assertIn("crear historico-chat/memory/memory.md", pasos)

        comp = versiones.POR_ID["recuerdos"]
        self.assertEqual(versiones.huella_sellada(proyecto, comp),
                         versiones.huella_central(comp))

        indice = recuerdos.ruta_indice(proyecto)
        with open(indice, "a", encoding="utf-8") as f:
            f.write("\n| lo mío | una línea del proyecto |\n")
        self.assertEqual(instalar.instalar_recuerdos(proyecto, aplicar=True),
                         ["historico-chat/memory/memory.md ya estaba sellado "
                          "al día"])
        self.assertIn("una línea del proyecto", self._leer(indice))


class Checklist(unittest.TestCase):
    """El stack de instalación: qué le falta a un proyecto."""

    def test_la_lista_y_las_comprobaciones_no_se_separan(self):
        # La lista vive en la plantilla y las comprobaciones en el código: si
        # se desincronizan, el checklist mentiría por omisión.
        ids = {i for i, _, _ in checklist.componentes()}
        self.assertTrue(ids, "no se leyó plantillas/stack-instalacion.md")
        self.assertEqual(ids, set(checklist.COMPROBACIONES),
                         "la plantilla y COMPROBACIONES no listan lo mismo")

    def test_cada_componente_dice_como_se_instala(self):
        for id, componente, arreglo in checklist.componentes():
            self.assertTrue(componente.strip(), f"{id} sin descripción")
            self.assertTrue(arreglo.strip(), f"{id} no dice cómo se instala")

    def _proyecto(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        return tmp.name

    def test_un_proyecto_vacio_no_pasa_nada(self):
        puntos = checklist.revisar(self._proyecto())
        self.assertEqual(len(puntos), len(checklist.COMPROBACIONES))
        self.assertTrue(checklist.pendientes(puntos))
        self.assertIn("INSTALACIÓN INCOMPLETA",
                      checklist.resumen("x", puntos))

    def test_la_marca_se_escribe_y_se_borra_sola(self):
        raiz = self._proyecto()
        puntos = checklist.revisar(raiz)
        archivo = checklist.escribir_marca(raiz, puntos)
        self.assertTrue(os.path.isfile(archivo))

        # Al quedar todo cumplido, la ausencia del archivo es la señal.
        for p in puntos:
            p.cumple = True
        self.assertEqual(checklist.escribir_marca(raiz, puntos), "")
        self.assertFalse(os.path.isfile(archivo))

    def test_detecta_que_el_stack_central_cambio(self):
        raiz = self._proyecto()
        copia = os.path.join(raiz, ".agente", "stack-instalacion.md")
        os.makedirs(os.path.dirname(copia))
        with open(copia, "w", encoding="utf-8") as f:
            f.write("lo que sea\n<!-- huella: 000000000000 -->\n")

        self.assertEqual(checklist.huella_instalada(raiz), "000000000000")
        cumple, detalle = checklist._stack_instalacion(raiz, instalar.RAIZ)
        self.assertFalse(cumple)
        self.assertIn("cambió en el estándar", detalle)

    def test_un_componente_que_el_validador_no_conoce_se_dice(self):
        # Estándar viejo contra una plantilla nueva: callar sería peor.
        original = checklist.componentes
        checklist.componentes = lambda estandar=None: [
            ("inventado", "Algo nuevo", "correr el instalador")]
        self.addCleanup(setattr, checklist, "componentes", original)

        punto = checklist.revisar(self._proyecto())[0]
        self.assertFalse(punto.cumple)
        self.assertIn("no sabe comprobar", punto.detalle)


class Citas(unittest.TestCase):
    """Una regla que se cita se enlaza: quien lee no sale a buscarla."""

    def test_el_ancla_pone_un_guion_por_espacio(self):
        # El `·` va entre espacios: al quitarlo quedan dos, y el ancla real de
        # GitHub lleva `--`. Colapsarlos daría un enlace que no lleva a nada.
        self.assertEqual(citas.ancla("N3 · No romper cosas"),
                         "n3--no-romper-cosas")

    def test_el_ancla_conserva_las_tildes_y_quita_los_signos(self):
        self.assertEqual(citas.ancla("G2 · Mensajes: qué y por qué"),
                         "g2--mensajes-qué-y-por-qué")

    def test_una_regla_en_su_propio_archivo_no_lleva_ancla(self):
        idx = citas.indice()
        self.assertIn("M5", idx)
        self.assertEqual(idx["M5"][1], "",
                         "el enlace al archivo ya es el enlace a la regla")

    def test_una_regla_dentro_de_un_capitulo_si_lleva_ancla(self):
        idx = citas.indice()
        self.assertTrue(idx["G2"][1].startswith("g2--"))

    def test_las_tres_formas_de_citar_quedan_normalizadas(self):
        idx = citas.indice()
        origen = os.path.join(instalar.RAIZ, "base", "09-git.md")
        for entrada in ("`00·N3`", "`00` · N3", "`00`·N3"):
            salida, n = citas.enlazar(f"texto {entrada} más texto", origen, idx)
            self.assertEqual(n, 1, entrada)
            self.assertIn("[`00·N3`](00-nucleo-blindado.md#n3--", salida, entrada)

    def test_la_dependencia_entre_parentesis_tambien_se_enlaza(self):
        idx = citas.indice()
        origen = os.path.join(instalar.RAIZ, "base", "09-git.md")
        salida, n = citas.enlazar("(extiende 00·N3)", origen, idx)
        self.assertEqual(n, 1)
        self.assertTrue(salida.startswith("(extiende [`00·N3`]("), salida)

    def test_lo_cercado_no_se_toca(self):
        # Ahí las citas son el molde que alguien va a copiar, no citas a nadie.
        idx = citas.indice()
        origen = os.path.join(instalar.RAIZ, "base", "09-git.md")
        texto = "```\nver `00·N3`\n```\n"
        salida, n = citas.enlazar(texto, origen, idx)
        self.assertEqual((salida, n), (texto, 0))

    def test_un_id_que_no_existe_no_se_enlaza(self):
        # Un enlace roto es peor que ninguno: el validador lo reporta y ya.
        idx = citas.indice()
        origen = os.path.join(instalar.RAIZ, "base", "09-git.md")
        salida, n = citas.enlazar("ver `ZZ99`", origen, idx)
        self.assertEqual((salida, n), ("ver `ZZ99`", 0))

    def test_una_regla_no_se_enlaza_a_si_misma(self):
        idx = citas.indice()
        origen = idx["G2"][0]
        _, n = citas.enlazar("como dice `G2`", origen, idx)
        self.assertEqual(n, 0)

    def test_no_queda_ninguna_cita_suelta_en_base(self):
        # Es la regla que el usuario pidió: toda cita lleva su enlace.
        self.assertEqual(citas.validar(), [])

    def test_enlazar_dos_veces_no_cambia_nada(self):
        idx = citas.indice()
        origen = os.path.join(instalar.RAIZ, "base", "09-git.md")
        una, _ = citas.enlazar("ver `00·N3`", origen, idx)
        dos, n = citas.enlazar(una, origen, idx)
        self.assertEqual((dos, n), (una, 0))


class Versiones(unittest.TestCase):
    """Nada heredado del estándar puede quedar viejo."""

    def _proyecto(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        return tmp.name

    def _estandar(self, **plantillas):
        """Un estándar de mentira con las plantillas que se le pasen."""
        raiz = self._proyecto()
        os.makedirs(os.path.join(raiz, "plantillas"))
        for nombre, texto in plantillas.items():
            with open(os.path.join(raiz, "plantillas", nombre), "w",
                      encoding="utf-8") as f:
                f.write(texto)
        return raiz

    # ── El sello ──────────────────────────────────────────────────────────

    def test_el_sello_se_reemplaza_en_su_sitio_y_nunca_se_duplica(self):
        texto = versiones.poner_sello("hola\n", "aaa111", "1.0.0")
        self.assertIn("<!-- huella: aaa111 · estandar 1.0.0 -->", texto)

        de_nuevo = versiones.poner_sello(texto, "bbb222", "2.0.0")
        self.assertEqual(de_nuevo.count("<!-- huella:"), 1,
                         "quedaron dos sellos: no se sabría cuál rige")
        self.assertIn("bbb222", de_nuevo)
        self.assertNotIn("aaa111", de_nuevo)
        self.assertIn("hola", de_nuevo, "el sello se comió el contenido")

    def test_el_sello_se_lee_de_vuelta(self):
        archivo = os.path.join(self._proyecto(), "x.md")
        with open(archivo, "w", encoding="utf-8") as f:
            f.write(versiones.poner_sello("contenido\n", "abc123", "1.2.3"))
        self.assertEqual(versiones.leer_sello(archivo), ("abc123", "1.2.3"))

    def test_sin_sello_no_se_inventa_uno(self):
        archivo = os.path.join(self._proyecto(), "x.md")
        with open(archivo, "w", encoding="utf-8") as f:
            f.write("sin sello\n")
        self.assertEqual(versiones.leer_sello(archivo), ("", ""))

    # ── Detectar que algo quedó viejo ─────────────────────────────────────

    def test_un_cambio_dentro_de_una_seccion_existente_se_detecta(self):
        # Es el caso que se escapaba: comparar títulos no lo ve, y la fecha del
        # archivo miente en cuanto alguien edita el CLAUDE.md por otra razón.
        estandar = self._estandar(**{
            "CLAUDE.md.plantilla": "# C\n\n## 6. Instalación\n\n- paso uno\n"})
        proyecto = self._proyecto()
        comp = versiones.POR_ID["claude-md"]

        local = os.path.join(proyecto, "CLAUDE.md")
        with open(local, "w", encoding="utf-8") as f:
            f.write(versiones.poner_sello(
                "# C del proyecto\n\n## 6. Instalación\n\n- paso uno\n",
                versiones.huella_central(comp, estandar), "1.0.0"))
        self.assertTrue(versiones.estado_de(proyecto, "claude-md", estandar).al_dia)

        # La plantilla gana un paso DENTRO de la sección que ya existía.
        with open(os.path.join(estandar, "plantillas", "CLAUDE.md.plantilla"),
                  "w", encoding="utf-8") as f:
            f.write("# C\n\n## 6. Instalación\n\n- paso uno\n- paso dos\n")

        est = versiones.estado_de(proyecto, "claude-md", estandar)
        self.assertFalse(est.al_dia)
        self.assertEqual(est.situacion, versiones.VIEJO)
        self.assertIn("quedó viejo", est.mensaje())

    def test_un_documento_heredado_sin_sello_no_pasa_por_al_dia(self):
        estandar = self._estandar(**{"CLAUDE.md.plantilla": "# C\n"})
        proyecto = self._proyecto()
        with open(os.path.join(proyecto, "CLAUDE.md"), "w",
                  encoding="utf-8") as f:
            f.write("# el mío, sin sello\n")

        est = versiones.estado_de(proyecto, "claude-md", estandar)
        self.assertEqual(est.situacion, versiones.SIN_SELLO)
        self.assertIn("no declara", est.mensaje())

    def test_el_checklist_reprueba_un_claude_md_viejo(self):
        # Antes esto era un AVISO y el componente pasaba igual: un proyecto con
        # el CLAUDE.md viejo figuraba como instalación completa.
        proyecto = self._proyecto()
        with open(os.path.join(proyecto, "CLAUDE.md"), "w",
                  encoding="utf-8") as f:
            f.write(versiones.poner_sello("# mío\n", "000000000000", "0.0.1"))

        cumple, detalle = checklist._claude_md(proyecto, instalar.RAIZ)
        self.assertFalse(cumple)
        self.assertIn("viejo", detalle)

    # ── El registro ───────────────────────────────────────────────────────

    def test_registrar_deja_el_archivo_con_lo_que_cambio(self):
        proyecto = self._proyecto()
        archivo = versiones.registrar(
            proyecto, "1.5.0",
            antes={"claude-md": "aaa"}, despues={"claude-md": "bbb"},
            pasos=["sellar CLAUDE.md"], pendientes=["**f13** — falta proyectos/"])

        with open(archivo, encoding="utf-8") as f:
            texto = f.read()
        self.assertIn("1.5.0", texto)
        self.assertIn("claude-md", texto)
        self.assertIn("aaa", texto)
        self.assertIn("bbb", texto)
        self.assertIn("sellar CLAUDE.md", texto)
        self.assertIn("pendiente", texto.lower())
        self.assertIn("1.5.0", os.path.basename(archivo))

    def test_solo_se_listan_los_componentes_que_cambiaron(self):
        proyecto = self._proyecto()
        archivo = versiones.registrar(
            proyecto, "1.5.0",
            antes={"claude-md": "aaa", "historico": "zzz"},
            despues={"claude-md": "bbb", "historico": "zzz"},
            pasos=[])
        with open(archivo, encoding="utf-8") as f:
            texto = f.read()
        tabla = texto.split("## Componentes actualizados")[1].split("##")[0]
        self.assertIn("claude-md", tabla)
        self.assertNotIn("historico", tabla,
                         "se listó un componente que no cambió")

    def test_una_instalacion_desde_cero_no_declara_venir_de_si_misma(self):
        # Para cuando se registra, los sellos YA dicen la versión nueva. Si la
        # versión anterior se preguntara aquí, un proyecto virgen diría venir
        # de la misma que acaba de instalar.
        proyecto = self._proyecto()
        os.makedirs(os.path.join(proyecto, ".agente"))
        with open(os.path.join(proyecto, ".agente", "stack-instalacion.md"),
                  "w", encoding="utf-8") as f:
            f.write(versiones.poner_sello("copia\n", "abc123", "1.4.0"))

        archivo = versiones.registrar(proyecto, "1.4.0", {}, {"x": "a"}, [],
                                      anterior="")
        with open(archivo, encoding="utf-8") as f:
            self.assertIn("(primera instalación)", f.read())

    def test_una_actualizacion_declara_de_donde_viene(self):
        proyecto = self._proyecto()
        archivo = versiones.registrar(proyecto, "1.5.0", {}, {"x": "b"}, [],
                                      anterior="1.4.0")
        with open(archivo, encoding="utf-8") as f:
            texto = f.read()
        self.assertIn("| Versión anterior | 1.4.0 |", texto)

    def test_dos_registros_el_mismo_dia_no_se_pisan(self):
        proyecto = self._proyecto()
        uno = versiones.registrar(proyecto, "1.5.0", {}, {"x": "a"}, [])
        dos = versiones.registrar(proyecto, "1.5.0", {}, {"x": "b"}, [])
        self.assertNotEqual(uno, dos)
        self.assertTrue(os.path.isfile(uno))
        self.assertTrue(os.path.isfile(dos))

    def test_el_indice_lista_los_registros(self):
        proyecto = self._proyecto()
        versiones.registrar(proyecto, "1.5.0", {}, {"x": "a"}, [])
        indice = os.path.join(versiones.carpeta_registros(proyecto), "README.md")
        with open(indice, encoding="utf-8") as f:
            self.assertIn("1.5.0", f.read())

    def _con_claude(self, adoptada):
        proyecto = self._proyecto()
        with open(os.path.join(proyecto, "CLAUDE.md"), "w",
                  encoding="utf-8") as f:
            f.write(f"# C\n\n- Versión del estándar adoptada: {adoptada}\n")
        return proyecto

    def test_una_version_vieja_del_estandar_ya_no_reprueba_por_si_sola(self):
        # Al proyecto le importa lo que tiene que APLICAR, no el número. Antes
        # un PARCHE que no le pedía nada lo dejaba en rojo, y el ruido enseña a
        # ignorar la alerta.
        cumple, _ = checklist._version(self._con_claude("0.0.1"), instalar.RAIZ)
        self.assertTrue(cumple)

    def test_no_declarar_la_version_si_reprueba(self):
        # Sin versión declarada no hay con qué sellar una fase cerrada.
        cumple, detalle = checklist._version(self._con_claude("«X.Y.Z»"),
                                             instalar.RAIZ)
        self.assertFalse(cumple)
        self.assertIn("no declara", detalle)

    def test_el_registro_no_vive_en_una_carpeta_ignorada(self):
        # `.agente/` va en el .gitignore: ahí el historial se quedaría en una
        # sola máquina. Saber bajo qué versión cerró cada fase tiene que poder
        # mirarse desde cualquier copia del repositorio.
        partes = versiones.CARPETA.replace("\\", "/").split("/")
        self.assertNotIn(".agente", partes)
        self.assertEqual(partes[0], "documentacion")

    def test_sin_carpeta_de_versiones_el_componente_reprueba(self):
        cumple, detalle = versiones.revisar_registro(self._proyecto())
        self.assertFalse(cumple)
        self.assertIn("versiones", detalle)

    def test_instalado_una_version_y_registrado_otra_reprueba(self):
        proyecto = self._proyecto()
        versiones.registrar(proyecto, "1.0.0", {}, {"x": "a"}, [])
        os.makedirs(os.path.join(proyecto, ".agente"), exist_ok=True)
        with open(os.path.join(proyecto, ".agente", "stack-instalacion.md"),
                  "w", encoding="utf-8") as f:
            f.write(versiones.poner_sello("copia\n", "abc123", "2.0.0"))

        cumple, detalle = versiones.revisar_registro(proyecto)
        self.assertFalse(cumple)
        self.assertIn("falta registrar", detalle)

    def test_la_lista_de_componentes_heredados_no_se_desincroniza(self):
        # Cada componente heredado tiene que existir de verdad en el estándar,
        # o el sello compararía contra la nada y todo pasaría por "al día".
        for c in versiones.COMPONENTES:
            self.assertTrue(os.path.isfile(c.ruta_plantilla()),
                            f"{c.id}: no existe {c.plantilla}")
            self.assertTrue(versiones.huella_central(c), f"{c.id}: huella vacía")


class EnlacesDelHistorico(unittest.TestCase):

    def test_no_comprueba_los_enlaces_de_una_transcripcion(self):
        # La transcripción copia el chat literal, y ahí los enlaces se escriben
        # relativos a la raíz del proyecto: dentro de la carpeta se romperían.
        self.assertTrue(enlaces._es_transcripcion(
            os.path.join("x", "historico-chat", "2026-01-01-t.md")))

    def test_el_indice_del_historico_si_se_comprueba(self):
        self.assertFalse(enlaces._es_transcripcion(
            os.path.join("x", "historico-chat", "README.md")))



class ResumenDeLaSesion(unittest.TestCase):
    """El enganche que sostiene el resumen: crea, avisa y muestra lo abierto."""

    def _proyecto(self):
        raiz = tempfile.mkdtemp()
        os.makedirs(os.path.join(raiz, "historico-chat", "resumenes", "2026-08-14"))
        os.makedirs(os.path.join(raiz, "plantillas"))
        with open(os.path.join(raiz, "plantillas", "sesion.md"), "w",
                  encoding="utf-8") as f:
            f.write("# Modelo\n\n## Hallazgos de esta sesión\n\n"
                    "### H-1 · «título»\n- **Estado:** «resuelto acá / abierto»\n")
        return raiz

    def _resumen(self, raiz, nombre, cuerpo):
        ruta = os.path.join(raiz, "historico-chat", "resumenes", "2026-08-14", nombre)
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(cuerpo)
        return ruta

    # CP-001 · el archivo nace al abrir la sesión
    def test_crea_el_archivo_con_el_modelo_y_sin_hallazgos(self):
        raiz = self._proyecto()
        ruta = resumen.crear(raiz, "2026-08-14-maracuya.md", raiz)
        self.assertTrue(os.path.isfile(ruta))
        self.assertEqual(resumen.hallazgos(ruta), [])

    def test_no_pisa_el_resumen_que_ya_existe(self):
        raiz = self._proyecto()
        ruta = self._resumen(raiz, "maracuya.md",
                             "### H-1 · algo\n- **Estado:** abierto\n")
        resumen.crear(raiz, "2026-08-14-maracuya.md", raiz)
        with open(ruta, encoding="utf-8") as f:
            self.assertIn("H-1 · algo", f.read())

    # CP-002 · dos sesiones el mismo día no se pisan
    def test_dos_sesiones_del_mismo_dia_son_dos_archivos(self):
        raiz = self._proyecto()
        a = resumen.crear(raiz, "2026-08-14-maracuya.md", raiz)
        b = resumen.crear(raiz, "2026-08-14-pepito.md", raiz)
        self.assertNotEqual(a, b)
        self.assertTrue(os.path.isfile(a) and os.path.isfile(b))

    # CP-003 · el renombrado mueve los dos archivos
    def test_renombrar_mueve_tambien_el_resumen(self):
        raiz = self._proyecto()
        carpeta = os.path.join(raiz, "historico-chat")
        ruta = os.path.join(carpeta, "2026-08-14-sesion.md")
        with open(ruta, "w", encoding="utf-8") as f:
            f.write("<!-- sesion: x -->\n\n# 2026-08-14 — Sesión\n")
        self._resumen(raiz, "sesion.md", "# lo que quedó\n")
        historico.renombrar(ruta, "maracuya", "prueba")
        dia = os.path.join(carpeta, "resumenes", "2026-08-14")
        self.assertTrue(os.path.isfile(os.path.join(dia, "maracuya.md")))
        self.assertFalse(os.path.isfile(os.path.join(dia, "sesion.md")))

    def test_renombrar_sin_resumen_no_falla(self):
        raiz = self._proyecto()
        carpeta = os.path.join(raiz, "historico-chat")
        ruta = os.path.join(carpeta, "2026-08-14-sesion.md")
        with open(ruta, "w", encoding="utf-8") as f:
            f.write("<!-- sesion: x -->\n\n# 2026-08-14 — Sesión\n")
        historico.renombrar(ruta, "pepito", "prueba")
        self.assertTrue(os.path.isfile(os.path.join(carpeta, "2026-08-14-pepito.md")))

    # CP-004 y CP-005 · qué falta, y cuándo se calla
    def test_avisa_que_no_hay_ningun_hallazgo(self):
        raiz = self._proyecto()
        ruta = self._resumen(raiz, "maracuya.md", "# lo que quedó\n")
        self.assertEqual(resumen.falta(ruta), ["vacio"])

    def test_avisa_que_falta_decir_si_se_puede_cerrar(self):
        raiz = self._proyecto()
        ruta = self._resumen(raiz, "maracuya.md",
                             "### H-1 · algo\n- **Estado:** abierto\n\n"
                             "## ¿Se puede cerrar la sesión?\n\n| x | ☐ |\n")
        self.assertEqual(resumen.falta(ruta), ["cierre"])

    def test_calla_cuando_no_falta_nada(self):
        raiz = self._proyecto()
        ruta = self._resumen(raiz, "maracuya.md",
                             "### H-1 · algo\n- **Estado:** resuelto acá\n\n"
                             "## ¿Se puede cerrar la sesión?\n\n| x | ☑ |\n")
        self.assertEqual(resumen.falta(ruta), [])

    # CP-007 · el aviso no se repite
    def test_el_aviso_no_se_repite(self):
        raiz = self._proyecto()
        ruta = self._resumen(raiz, "maracuya.md", "# lo que quedó\n")
        self.assertEqual(resumen.falta(ruta), ["vacio"])
        resumen.marcar_avisado(ruta, "vacio")
        self.assertEqual(resumen.falta(ruta), [])

    def test_la_marca_del_aviso_vive_en_el_propio_resumen(self):
        raiz = self._proyecto()
        ruta = self._resumen(raiz, "maracuya.md", "# lo que quedó\n")
        resumen.marcar_avisado(ruta, "vacio")
        with open(ruta, encoding="utf-8") as f:
            self.assertIn(resumen.MARCA_VACIO, f.read())

    # CP-006 · se muestra lo abierto del propósito, y nada de otros temas
    def test_muestra_el_hallazgo_del_proposito_si_sigue_abierto(self):
        raiz = self._proyecto()
        self._resumen(raiz, "maracuya.md",
                      "### H-4 · el hueco\n- **Estado:** abierto\n"
                      "- **Con qué se retoma:** la pregunta viva\n")
        ruta = self._resumen(raiz, "pepito.md",
                             "**Viene de:** 2026-08-14 · maracuya · H-4\n")
        p = resumen.proposito(raiz, ruta)
        self.assertIsNotNone(p)
        self.assertEqual(p[1], "H-4")
        self.assertEqual(p[3], "la pregunta viva")

    def test_no_muestra_lo_abierto_de_otro_tema(self):
        raiz = self._proyecto()
        self._resumen(raiz, "otro-tema.md",
                      "### H-9 · nada que ver\n- **Estado:** abierto\n")
        self._resumen(raiz, "maracuya.md",
                      "### H-4 · el hueco\n- **Estado:** resuelto acá\n")
        ruta = self._resumen(raiz, "pepito.md",
                             "**Viene de:** 2026-08-14 · maracuya · H-4\n")
        self.assertIsNone(resumen.proposito(raiz, ruta))

    def test_sin_proposito_declarado_no_muestra_nada(self):
        raiz = self._proyecto()
        ruta = self._resumen(raiz, "pepito.md",
                             "**Viene de:** «AAAA-MM-DD · tema · H-N»\n")
        self.assertIsNone(resumen.proposito(raiz, ruta))

    # CP-009 · no se mete donde no lo llaman
    def test_un_proyecto_sin_carpeta_de_resumenes_no_se_ve_afectado(self):
        raiz = tempfile.mkdtemp()
        self.assertEqual(resumen.crear(raiz, "2026-08-14-maracuya.md", raiz), "")


class EngancheDelResumenPorElCaminoReal(unittest.TestCase):
    """Los mismos criterios, disparados como los dispara Claude Code.

    La clase de arriba prueba las piezas: llama a `resumen.crear()` con la
    transcripción ya en la mano. Eso dejó pasar el defecto que esta clase
    reproduce: al abrir la sesión esa transcripción **no existe**, así que el
    archivo nunca nacía. Acá no se arma ninguna precondición a mano — el
    proyecto lo instala el instalador y la transcripción la escribe su enganche.
    """

    VALIDADORES = os.path.dirname(os.path.abspath(__file__))

    def _hay_git(self):
        try:
            subprocess.run(["git", "--version"], capture_output=True, timeout=10)
            return True
        except (OSError, subprocess.SubprocessError):
            return False

    def _proyecto_instalado(self):
        """Una carpeta temporal pasada por el instalador de verdad.

        El instalador anota el proyecto en `plantillas/proyectos.md` del
        estándar; eso es su conducta normal, no un efecto de la prueba, así que
        se deja correr y se devuelve el archivo como estaba.
        """
        if not self._hay_git():
            self.skipTest("sin git")
        raiz = tempfile.mkdtemp()
        subprocess.run(["git", "init"], cwd=raiz, capture_output=True, timeout=30)

        registro = instalar.REGISTRO
        antes = comun.leer(registro) if os.path.isfile(registro) else None
        if antes is not None:
            self.addCleanup(self._restaurar, registro, antes)

        salida = subprocess.run(
            [sys.executable, os.path.join(self.VALIDADORES, "instalar.py"),
             raiz, "--aplicar"], capture_output=True, text=True, timeout=180)
        self.assertEqual(salida.returncode, 0, salida.stdout + salida.stderr)
        return raiz

    def _restaurar(self, ruta, texto):
        with open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)

    def _correr(self, guion, modo, raiz, sesion, prompt="hola"):
        """Corre el enganche como orden del sistema, con el JSON que recibe."""
        entrada = json.dumps({"session_id": sesion, "cwd": raiz,
                              "prompt": prompt, "transcript_path": ""})
        return subprocess.run(
            [sys.executable, os.path.join(self.VALIDADORES, guion),
             "--modo", modo, "--raiz", raiz],
            input=entrada, capture_output=True, text=True, timeout=60)

    def _transcripcion(self, raiz, sesion):
        carpeta = os.path.join(raiz, "historico-chat")
        for nombre in sorted(os.listdir(carpeta)):
            if not nombre.endswith(".md") or nombre == "README.md":
                continue
            if f"<!-- sesion: {sesion} -->" in comun.leer(os.path.join(carpeta, nombre)):
                return nombre
        return ""

    def _abrir_sesion(self, raiz, sesion, prompt="hola"):
        """Los tres enganches del arranque, en el orden en que ocurren."""
        self._correr("hook_resumen.py", "inicio", raiz, sesion)
        self._correr("hook_historico.py", "usuario", raiz, sesion, prompt)
        self._correr("hook_resumen.py", "aviso", raiz, sesion, prompt)
        transcripcion = self._transcripcion(raiz, sesion)
        return os.path.join(raiz, "historico-chat", "resumenes",
                            transcripcion[:10], transcripcion[11:])

    # CP-002 · el instalador deja el proyecto listo
    def test_el_instalador_deja_la_carpeta_de_resumenes(self):
        raiz = self._proyecto_instalado()
        self.assertTrue(os.path.isfile(
            os.path.join(raiz, "historico-chat", "resumenes", "README.md")))

    # CP-001 · el archivo aparece en una sesión nueva sin que nadie lo pida
    def test_el_resumen_aparece_solo_en_una_sesion_nueva(self):
        raiz = self._proyecto_instalado()
        ruta = self._abrir_sesion(raiz, "s1")
        self.assertTrue(os.path.isfile(ruta), "el resumen no nació")
        self.assertEqual(resumen.hallazgos(ruta), [])
        self.assertIn("¿Se puede cerrar la sesión?", comun.leer(ruta))

    def test_al_abrir_todavia_no_hay_transcripcion_y_no_falla(self):
        raiz = self._proyecto_instalado()
        salida = self._correr("hook_resumen.py", "inicio", raiz, "s1")
        self.assertEqual(salida.returncode, 0)
        self.assertEqual(salida.stdout.strip(), "")

    def test_el_indice_del_dia_queda_con_su_linea(self):
        raiz = self._proyecto_instalado()
        ruta = self._abrir_sesion(raiz, "s1")
        indice = os.path.join(os.path.dirname(ruta), "README.md")
        self.assertIn(os.path.basename(ruta), comun.leer(indice))

    # CP-003 · dos sesiones el mismo día no se pisan
    def test_dos_sesiones_el_mismo_dia_dan_dos_archivos(self):
        raiz = self._proyecto_instalado()
        a = self._abrir_sesion(raiz, "s1")
        b = self._abrir_sesion(raiz, "s2", "otra cosa")
        self.assertNotEqual(a, b)
        self.assertTrue(os.path.isfile(a) and os.path.isfile(b))

    # CP-004 · el encabezado no enlaza a nada que no exista
    def test_el_encabezado_no_enlaza_fuera_del_proyecto(self):
        raiz = self._proyecto_instalado()
        ruta = self._abrir_sesion(raiz, "s1")
        texto = comun.leer(ruta)
        self.assertNotIn("plantillas/sesion.md", texto)
        for destino in ("../../" + os.path.basename(self._transcripcion(raiz, "s1")),
                        "../../README.md"):
            self.assertTrue(
                os.path.isfile(os.path.join(os.path.dirname(ruta), destino)),
                f"enlace roto: {destino}")

    # CP-005 · avisa qué falta cuando la sesión produjo algo
    def test_avisa_que_el_resumen_sigue_vacio(self):
        raiz = self._proyecto_instalado()
        self._abrir_sesion(raiz, "s1")
        with open(os.path.join(raiz, "algo.txt"), "w", encoding="utf-8") as f:
            f.write("cambio\n")
        subprocess.run(["git", "add", "algo.txt"], cwd=raiz,
                       capture_output=True, timeout=30)
        salida = self._correr("hook_resumen.py", "aviso", raiz, "s1", "seguimos")
        self.assertIn("SIGUE VAC", salida.stdout.upper())

    # CP-006 · del propósito se muestra lo abierto, y nada de otros temas
    def test_muestra_lo_abierto_del_proposito_y_nada_mas(self):
        raiz = self._proyecto_instalado()
        ruta = self._abrir_sesion(raiz, "s1")
        dia = os.path.dirname(ruta)
        with open(os.path.join(dia, "maracuya.md"), "w", encoding="utf-8") as f:
            f.write("### H-4 · el hueco\n- **Estado:** abierto\n"
                    "- **Con qué se retoma:** la pregunta viva\n")
        with open(os.path.join(dia, "pepito.md"), "w", encoding="utf-8") as f:
            f.write("### H-9 · nada que ver\n- **Estado:** abierto\n")
        texto = comun.leer(ruta).replace(
            "**Viene de:** «...»",
            f"**Viene de:** {os.path.basename(dia)} · maracuya · H-4")
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(texto)

        salida = self._correr("hook_resumen.py", "inicio", raiz, "s1")
        self.assertIn("H-4", salida.stdout)
        self.assertIn("la pregunta viva", salida.stdout)
        self.assertNotIn("H-9", salida.stdout)

    # CP-007 · correr el enganche dos veces no pisa ni duplica
    def test_correr_los_dos_modos_no_pisa_lo_escrito(self):
        raiz = self._proyecto_instalado()
        ruta = self._abrir_sesion(raiz, "s1")
        with open(ruta, "a", encoding="utf-8") as f:
            f.write("\n### H-1 · algo escrito a mano\n- **Estado:** abierto\n")
        self._correr("hook_resumen.py", "inicio", raiz, "s1")
        self._correr("hook_resumen.py", "aviso", raiz, "s1", "otra vez")
        self.assertIn("algo escrito a mano", comun.leer(ruta))
        indice = comun.leer(os.path.join(os.path.dirname(ruta), "README.md"))
        self.assertEqual(indice.count(f"({os.path.basename(ruta)})"), 1)

    # CP-008 · un proyecto sin instalar no se ve afectado
    def test_un_proyecto_sin_instalar_no_se_ve_afectado(self):
        raiz = tempfile.mkdtemp()
        for modo in ("inicio", "aviso"):
            salida = self._correr("hook_resumen.py", modo, raiz, "s1")
            self.assertEqual(salida.returncode, 0)
            self.assertEqual(salida.stdout.strip(), "")
        self.assertEqual(os.listdir(raiz), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
