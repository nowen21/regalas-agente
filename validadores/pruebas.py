#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Suite de los validadores. Solo biblioteca estándar.

    python validadores/pruebas.py

Cubre las reglas y, sobre todo, los **falsos positivos** que se detectaron al
probar contra el repositorio real: son los que hacen que nadie confíe en un
validador y termine ignorándolo.
"""
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import cargador         # noqa: E402
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
import estacion_commit  # noqa: E402
import flujo            # noqa: E402
import herramientas     # noqa: E402
import historico        # noqa: E402
import metareglas       # noqa: E402
import pendientes       # noqa: E402
import migraciones      # noqa: E402
import plantillas       # noqa: E402
import rama             # noqa: E402
import recuerdos        # noqa: E402
import rendimiento      # noqa: E402
import rutas_fuera      # noqa: E402
import resumen          # noqa: E402
import secretos         # noqa: E402
import sesiones         # noqa: E402
import corredor        # noqa: E402
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
        self.assertTrue(ruta.endswith(os.path.join("plantillas", "ciclo-vida-proyectos", "04-HU.md")))

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
        for base, esperado in (("plan_trabajo", "ciclo-vida-proyectos/07-plan-trabajo.md"),
                               ("funcionalidad_implementada", "ciclo-vida-proyectos/11-funcionalidad-implementada.md"),
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
        """Es la regla que el usuario pidió: toda cita lleva su enlace.

        **Pasa desde el 2026-08-17**, al cerrarse el pendiente 55. Estuvo
        marcada como fallo esperado porque las cinco que reportaba eran falsos
        positivos, y `base/` estaba bien escrito: torcer el texto para callar
        al validador era la salida mala que ese pendiente describe.

        Las cinco se resolvieron sin tocar una línea de `base/`, y cada una por
        un motivo distinto:

        - `C20` y `F12` en el glosario, y `G9` en `estructura-regla.md`: caen
          en columnas de ejemplo —«Lo que sale mal»—, así que muestran un
          identificador en vez de citarlo.
        - `ID7` en `ID9`: es la segunda mención del mismo archivo, y la
          primera sí lleva su enlace.
        - `G1` en `09-git.md`: es un ancla del mismo archivo, que es la forma
          correcta de citar a una vecina.

        Y un dato que el pendiente daba mal: **`G9` sí existe** — es *La
        historia de usuario es la unidad del commit*, en `09-git.md`. Seguía
        siendo falso positivo, pero por ser ejemplo y no por no existir."""
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


class RepartoDeLasReglas(unittest.TestCase):
    """Qué llega puesto al abrir la sesión y qué llega como índice.

    El reparto existía desde la 5.0.0 y nadie lo probaba: una línea cambiada
    dejaba al agente sin identidad y nada avisaba. Estas pruebas son esa red.
    Se comprueba **el reparto**, no el texto de una regla concreta, para que
    renombrar una regla no las rompa.
    """

    def _base(self, *nombres):
        """Un cuerpo de reglas de prueba, con un archivo por nombre pedido."""
        raiz = tempfile.mkdtemp()
        base = os.path.join(raiz, "base")
        for nombre in nombres:
            ruta = os.path.join(base, nombre)
            os.makedirs(os.path.dirname(ruta), exist_ok=True)
            with open(ruta, "w", encoding="utf-8") as f:
                f.write(f"# Título de {nombre}\n\nCuerpo de {nombre}.\n")
        return raiz

    # CP-001 · los capítulos que rigen cada frase llegan con su texto
    def test_los_capitulos_00_y_01_llegan_completos(self):
        raiz = self._base("00-nucleo.md", "00-identidad/base.md",
                          "01-conducta.md", "05-tema/base.md")
        texto = cargador.contexto(raiz)
        for nombre in ("00-nucleo.md", "00-identidad/base.md", "01-conducta.md"):
            self.assertIn(f"Cuerpo de {nombre}", texto, nombre)

    def test_el_resto_llega_solo_como_indice(self):
        raiz = self._base("00-nucleo.md", "05-tema/base.md")
        texto = cargador.contexto(raiz)
        self.assertNotIn("Cuerpo de 05-tema/base.md", texto)
        self.assertIn("base/05-tema/base.md", texto)
        self.assertIn("Título de 05-tema/base.md", texto)

    def test_un_capitulo_nuevo_del_prefijo_entra_solo(self):
        # El reparto mira el prefijo de la ruta, así que un `01-` nuevo no
        # obliga a tocar el programa (RN-14).
        raiz = self._base("00-nucleo.md", "01-conducta.md", "01-otro-nuevo.md")
        self.assertIn("Cuerpo de 01-otro-nuevo.md", cargador.contexto(raiz))

    def test_el_capitulo_en_carpeta_no_cae_al_indice(self):
        # Se decide por el primer tramo de la ruta y no por el nombre del
        # archivo: si no, `00-identidad/base.md` caería al índice (RN-12).
        raiz = self._base("00-identidad/base.md")
        self.assertIn("Cuerpo de 00-identidad/base.md", cargador.contexto(raiz))

    # CP-002 · el contexto dice qué llegó puesto y qué hay que abrir
    def test_dice_que_lo_cargado_es_obligatorio(self):
        raiz = self._base("00-nucleo.md", "05-tema/base.md")
        self.assertIn("CARGADAS, OBLIGATORIAS", cargador.contexto(raiz))

    def test_dice_que_el_indice_hay_que_abrirlo(self):
        raiz = self._base("00-nucleo.md", "05-tema/base.md")
        texto = cargador.contexto(raiz)
        self.assertIn("NO ESTÁN CARGADAS, SOLO EL ÍNDICE", texto)
        self.assertIn("leer el archivo completo", texto)

    # CP-003 · sin cuerpo de reglas no entrega nada
    def test_sin_carpeta_base_no_entrega_nada(self):
        raiz = tempfile.mkdtemp()
        self.assertEqual(cargador.contexto(raiz), "")
        self.assertEqual(os.listdir(raiz), [])

    def test_con_base_vacia_no_entrega_nada(self):
        raiz = tempfile.mkdtemp()
        os.makedirs(os.path.join(raiz, "base"))
        self.assertEqual(cargador.contexto(raiz), "")

    # CP-005 · con el gate sin pasar entrega solo esa regla
    def test_sin_pasar_el_gate_entrega_solo_esa_regla(self):
        raiz = self._base("00-nucleo.md", cargador.GATE)
        texto = cargador.contexto(raiz, gate_ok=False)
        self.assertIn("ARRANQUE DETENIDO", texto)
        self.assertIn(f"Cuerpo de {cargador.GATE}", texto)
        self.assertNotIn("Cuerpo de 00-nucleo.md", texto)

    # CP-004 · lo que cuesta el arranque, medido contra el repositorio real
    def test_lo_que_se_inyecta_de_este_repositorio_se_puede_medir(self):
        texto = cargador.contexto(comun.RAIZ if hasattr(comun, "RAIZ") else ".")
        if not texto:
            self.skipTest("sin base/ en la raíz de la corrida")
        kb = len(texto.encode("utf-8")) / 1024
        self.assertGreater(kb, 1)
        self.assertLess(kb, 90, "el arranque creció más de lo medido en la fase")

    # CP-005 · el sello no viaja al arranque
    def test_el_arranque_no_lleva_los_bloques_de_checklist(self):
        """**El sello no le sirve al agente para obedecer.**

        Es el registro de que alguien revisó la regla contra el molde, y le
        sirve a quien mantiene el estándar. Medido el 2026-08-19: de los
        **122,6 KB** que se inyectaban, **70 eran sellos** — el 57 %.

        **Lo destapó esta prueba, no la lectura.** El techo saltó al partir las
        reglas del núcleo, y en vez de subirlo se miró qué había adentro.
        """
        texto = cargador.contexto(comun.RAIZ)
        if not texto:
            self.skipTest("sin base/ en la raíz de la corrida")
        self.assertNotIn("### Checklist", texto)

    def test_pero_las_reglas_llegan_enteras(self):
        """**Quitar el sello no puede quitar la regla.** Sin este caso, un
        recorte de más pasaría por ahorro."""
        texto = cargador.contexto(comun.RAIZ)
        if not texto:
            self.skipTest("sin base/ en la raíz de la corrida")
        for marca in ("## N1", "## N9", "INCORRECTO:", "CORRECTO:"):
            self.assertIn(marca, texto)


class EngancheDelResumenPorElCaminoReal(unittest.TestCase):
    """Los mismos criterios, disparados como los dispara Claude Code.

    La clase de arriba prueba las piezas: llama a `resumen.crear()` con la
    transcripción ya en la mano. Eso dejó pasar el defecto que esta clase
    reproduce: al abrir la sesión esa transcripción **no existe**, así que el
    archivo nunca nacía. Acá no se arma ninguna precondición a mano — el
    proyecto lo instala el instalador y la transcripción la escribe su enganche.
    """

    VALIDADORES = os.path.dirname(os.path.abspath(__file__))
    # Los enganches se mudaron al adaptador el 2026-08-19: `validadores/`
    # es lo que sirve con cualquier agente, y esto existe porque **esta**
    # herramienta lo llama.
    ADAPTADOR = os.path.join(os.path.dirname(VALIDADORES),
                             "adaptadores", "claude-code")

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
             raiz, "--aplicar"], capture_output=True, text=True, encoding="utf-8", timeout=180)
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
            [sys.executable, os.path.join(self.ADAPTADOR, guion),
             "--modo", modo, "--raiz", raiz],
            input=entrada, capture_output=True, text=True, encoding="utf-8", timeout=60)

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


class DerogacionSinBorrar(unittest.TestCase):
    """Derogar sin borrar ni renumerar — EP-001 · HU-008.

    Las especificaciones, los commits y las fases cerradas citan las reglas por
    identificador. Borrar una regla derogada rompe esas citas sin dejar rastro,
    y reutilizar su identificador es peor: la cita sigue resolviendo, y a otra
    cosa.
    """

    RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def _texto_de_base(self):
        partes = []
        for carpeta, _, archivos in os.walk(os.path.join(self.RAIZ, "base")):
            for n in archivos:
                if n.endswith(".md"):
                    partes.append(comun.leer(os.path.join(carpeta, n)))
        return "\n".join(partes)

    # -- CA-01 · la derogada sigue siendo legible -------------------------
    def test_cada_derogacion_conserva_su_cuerpo(self):
        derogadas = version.derogaciones()
        self.assertTrue(derogadas, "no hay derogaciones que comprobar")
        base = self._texto_de_base()
        for _, identificador, _ in derogadas:
            self.assertIn(identificador, base,
                          f"`{identificador}` está derogada y su texto desapareció")

    def test_la_marca_dice_desde_cuando_y_por_cual(self):
        """CA-01: la marca trae la versión y el reemplazo, y el reemplazo
        **existe**. Una derogación que apunta a una regla inventada manda a
        buscar lo que no está."""
        base = self._texto_de_base()
        for desde, identificador, reemplazo in version.derogaciones():
            self.assertRegex(desde, r"^\d+\.\d+\.\d+$",
                             f"`{identificador}` no dice desde qué versión")
            self.assertTrue(reemplazo, f"`{identificador}` no dice por cuál")
            # El reemplazo puede ser uno o varios: «F16 y F17», «13·DOC1».
            import re as _re
            for nombre in _re.findall(r"[A-Z]{1,4}\d+(?:\.\d+)?", reemplazo):
                self.assertIn(nombre, base,
                              f"`{identificador}` remite a `{nombre}`, que no existe")

    # -- CA-02 · el identificador liberado no se reutiliza ----------------
    def test_ningun_identificador_derogado_vuelve_como_regla_vigente(self):
        vigentes = {r.id for r in metareglas.reglas(self.RAIZ) if not r.derogada}
        for _, identificador, _ in version.derogaciones():
            self.assertNotIn(
                identificador, vigentes,
                f"`{identificador}` está derogada y además vigente: la cita "
                f"resolvería a otra cosa")

    # -- CA-03 · la derogada no cuenta como incumplimiento ----------------
    def test_la_derogada_no_entra_en_la_cuenta_de_incumplimientos(self):
        derogadas = {i for _, i, _ in version.derogaciones()}
        reclamadas = [h.mensaje for h in metareglas.validar(self.RAIZ)
                      if any(d in h.mensaje for d in derogadas)]
        self.assertEqual(reclamadas, [],
                         "se le reclama algo a una regla derogada")

    # -- transversal de límites --------------------------------------------
    def test_limites_toda_derogacion_de_hoy_tiene_reemplazo(self):
        """El transversal pide que esté definido qué pasa cuando **no** hay
        reemplazo. Hoy las ocho lo tienen; se deja escrito que ese caso no ha
        ocurrido nunca, en vez de dar por buena una regla que nadie probó."""
        sin_reemplazo = [i for _, i, r in version.derogaciones() if not r]
        self.assertEqual(sin_reemplazo, [])


class NumeroDeVersion(unittest.TestCase):
    """El número de versión y qué significa cada parte — EP-002 · HU-001."""

    RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def _versiones_del_registro(self):
        import re as _re
        texto = comun.leer(os.path.join(self.RAIZ, "CHANGELOG.md"))
        return [tuple(int(p) for p in v.split("."))
                for v in _re.findall(r"^## (\d+\.\d+\.\d+)", texto, _re.M)]

    def test_el_numero_tiene_tres_partes_y_sale_de_version(self):
        crudo = comun.leer(os.path.join(self.RAIZ, "VERSION")).strip()
        self.assertRegex(crudo, r"^\d+\.\d+\.\d+$")
        self.assertEqual(version.version_estandar(), crudo)

    def test_la_version_del_archivo_es_la_ultima_del_registro(self):
        """CP-002: ningún otro número manda. El del archivo y el de la primera
        entrada del registro son el mismo, o hay dos verdades."""
        crudo = comun.leer(os.path.join(self.RAIZ, "VERSION")).strip()
        self.assertEqual(self._versiones_del_registro()[0],
                         tuple(int(p) for p in crudo.split(".")))

    @unittest.expectedFailure
    def test_las_tres_partes_avanzan_sin_saltos_ni_reinicios(self):
        """CP-005 y el transversal de no regresión: entre dos entradas
        consecutivas, o sube la mayor y las otras van a cero, o sube la menor
        y el parche va a cero, o sube el parche. Nunca baja el número.

        **Falla hoy** (defecto `D-01` de la fase): **`15.4.0` aparece dos veces
        en el registro**, con fechas distintas —2026-08-14 y 2026-08-15—. Dos
        cambios distintos comparten número, así que un proyecto que declare
        «adopté la 15.4.0» no puede saber cuál de los dos tiene."""
        versiones = list(reversed(self._versiones_del_registro()))
        for antes, ahora in zip(versiones, versiones[1:]):
            self.assertGreater(ahora, antes,
                               f"la versión bajó: {antes} → {ahora}")
            ma, me, pa = antes
            Ma, Me, Pa = ahora
            if Ma != ma:
                self.assertEqual((Ma, Me, Pa), (ma + 1, 0, 0),
                                 f"salto de MAYOR mal formado: {antes} → {ahora}")
            elif Me != me:
                self.assertEqual((Me, Pa), (me + 1, 0),
                                 f"salto de MENOR mal formado: {antes} → {ahora}")
            else:
                self.assertEqual(Pa, pa + 1,
                                 f"salto de PARCHE mal formado: {antes} → {ahora}")

    def test_toda_entrada_del_registro_declara_su_tipo(self):
        """CA-02 y CA-03: cada entrada dice si es MAYOR, MENOR o PARCHE. Sin
        eso, el número sube y nadie sabe qué significó."""
        import re as _re
        texto = comun.leer(os.path.join(self.RAIZ, "CHANGELOG.md"))
        bloques = _re.split(r"^## (\d+\.\d+\.\d+)", texto, flags=_re.M)[1:]
        pares = list(zip(bloques[::2], bloques[1::2]))
        self.assertTrue(pares)
        # La primera versión no declara tipo, y está bien: no hay nada
        # anterior contra lo que compararla. El marcador va en negrita, con o
        # sin punto dentro: `**MENOR**` y `**MENOR.**` cuentan igual.
        sin_tipo = [v for v, cuerpo in pares[:-1]
                    if not _re.search(r"\*\*(MAYOR|MENOR|PARCHE)\.?\*\*", cuerpo)]
        self.assertEqual(sin_tipo, [], f"entradas sin tipo declarado: {sin_tipo}")


class TranscripcionDeLaSesion(unittest.TestCase):
    """La sesión se escribe sola, con la hora del reloj — EP-005 · HU-001."""

    RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def test_la_hora_viene_del_reloj_y_no_del_texto_del_mensaje(self):
        """CA-02. Se manda un mensaje que **contiene** una hora falsa y se
        comprueba que la anotada no es esa: si el programa copiara lo que dice
        el texto, bastaría con escribir «10:00» para falsear el histórico."""
        import datetime
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        os.makedirs(os.path.join(tmp.name, "historico-chat"))
        historico.anotar_usuario(tmp.name, "s1", "eran las 03:33 de la madrugada")
        archivos = [n for n in os.listdir(os.path.join(tmp.name, "historico-chat"))
                    if n.endswith(".md")]
        self.assertTrue(archivos, "no nació el archivo de la sesión")
        texto = comun.leer(os.path.join(tmp.name, "historico-chat", archivos[0]))
        self.assertIn("03:33", texto, "no se guardó el mensaje")
        hoy = datetime.date.today().isoformat()
        self.assertIn(hoy, texto, "la fecha no es la del reloj")

    def test_limites_un_proyecto_sin_carpeta_de_sesiones_no_se_ve_afectado(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        historico.anotar_usuario(tmp.name, "s1", "hola")
        self.assertEqual(os.listdir(tmp.name), [],
                         "escribió en un proyecto que no tiene la carpeta")

    def test_privacidad_lo_enmascarado_no_queda_en_claro(self):
        """**El transversal que no se puede comprobar todavía**: la HU pide que
        lo enmascarado no quede en claro, y **nada enmascara**. Se deja escrito
        que el texto se guarda tal cual, que es la verdad de hoy."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        os.makedirs(os.path.join(tmp.name, "historico-chat"))
        historico.anotar_usuario(tmp.name, "s1", "mi clave es " + "abc" + "123def")
        archivos = [n for n in os.listdir(os.path.join(tmp.name, "historico-chat"))
                    if n.endswith(".md")]
        texto = comun.leer(os.path.join(tmp.name, "historico-chat", archivos[0]))
        self.assertIn("abc123def", texto,
                      "algo cambió: si ya se enmascara, esta prueba hay que reescribirla")


class DisparoAlEscribirUnArchivo(unittest.TestCase):
    """El disparo al escribir — EP-005 · HU-003."""

    VALIDADORES = os.path.dirname(os.path.abspath(__file__))
    # Los enganches se mudaron al adaptador el 2026-08-19: `validadores/`
    # es lo que sirve con cualquier agente, y esto existe porque **esta**
    # herramienta lo llama.
    ADAPTADOR = os.path.join(os.path.dirname(VALIDADORES),
                             "adaptadores", "claude-code")

    def _correr(self, raiz, archivo):
        entrada = json.dumps({"cwd": raiz, "tool_input": {"file_path": archivo}})
        return subprocess.run(
            [sys.executable, os.path.join(self.ADAPTADOR, "hook_md.py"),
             "--raiz", raiz],
            input=entrada, capture_output=True, text=True, encoding="utf-8", timeout=60)

    def test_lo_que_no_le_toca_se_ignora_en_silencio(self):
        """CA-02: con un archivo que no es `.md`, el enganche **corre igual** y
        no dice nada. Que calle no puede confundirse con que no se ejecutó."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        codigo = os.path.join(tmp.name, "programa.py")
        with open(codigo, "w", encoding="utf-8") as f:
            f.write("x = 1\n")
        salida = self._correr(tmp.name, codigo)
        self.assertEqual(salida.returncode, 0)
        self.assertEqual(salida.stdout.strip(), "")

    def test_el_documento_con_enlace_roto_produce_el_aviso_en_el_momento(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        doc = os.path.join(tmp.name, "documento.md")
        with open(doc, "w", encoding="utf-8") as f:
            f.write("# Título\n\nVer [lo que no está](no-existe-en-ningun-lado.md).\n")
        salida = self._correr(tmp.name, doc)
        self.assertIn("no-existe-en-ningun-lado.md", salida.stdout + salida.stderr)

    def test_errores_si_la_comprobacion_no_puede_correr_el_trabajo_continua(self):
        """Transversal de errores: con un archivo que ya no está cuando el
        enganche llega —se borró entre la escritura y el disparo—, no revienta."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        salida = self._correr(tmp.name, os.path.join(tmp.name, "fantasma.md"))
        self.assertIn(salida.returncode, (0, 2),
                      f"el enganche murió con código {salida.returncode}")

    def test_rendimiento_el_disparo_no_se_nota(self):
        """Transversal de rendimiento. Se mide, no se supone."""
        import time
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        doc = os.path.join(tmp.name, "documento.md")
        with open(doc, "w", encoding="utf-8") as f:
            f.write("# Título\n\nTexto normal, sin enlaces.\n")
        inicio = time.perf_counter()
        self._correr(tmp.name, doc)
        tardo = time.perf_counter() - inicio
        self.assertLess(tardo, 5.0, f"el disparo tardó {tardo:.2f} s")


class ModelosDelEncargo(unittest.TestCase):
    """Los tres modelos del encargo se encadenan — EP-003 · HU-002."""

    RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def test_toda_hu_nombra_su_epica_y_toda_epica_lista_sus_hu(self):
        """CA-01, sobre el árbol real: el encadenamiento se comprueba en los
        dos sentidos, que es lo que hace `trazabilidad.py` con `DOC16`."""
        sueltos = [h for h in trazabilidad.validar(self.RAIZ)
                   if "épica" in h.mensaje.lower() and h.severidad == comun.FALLA]
        self.assertEqual([h.mensaje for h in sueltos], [])

    def test_los_tres_modelos_del_encargo_existen(self):
        for modelo in ("ciclo-vida-proyectos/01-planteamiento.md", "ciclo-vida-proyectos/03-epica.md", "ciclo-vida-proyectos/04-HU.md"):
            self.assertTrue(
                os.path.isfile(os.path.join(self.RAIZ, "plantillas", modelo)),
                f"falta el modelo `{modelo}`")

    def test_el_modelo_de_hu_pide_como_validar_cada_criterio(self):
        """CA-02: un criterio sin «cómo validarlo» no se puede comprobar, y la
        HU entera se vuelve opinión."""
        molde = comun.leer(os.path.join(self.RAIZ, "plantillas", "ciclo-vida-proyectos/04-HU.md"))
        self.assertIn("Cómo validarlo", molde)
        self.assertIn("Aprobado cuando", molde)

    def test_limites_la_epica_sin_hu_y_la_hu_sin_fases_tienen_forma(self):
        molde_epica = comun.leer(os.path.join(self.RAIZ, "plantillas", "ciclo-vida-proyectos/03-epica.md"))
        molde_hu = comun.leer(os.path.join(self.RAIZ, "plantillas", "ciclo-vida-proyectos/04-HU.md"))
        self.assertIn("Historias de usuario", molde_epica)
        self.assertIn("Fases que la implementan", molde_hu)


class ModelosDeLaFase(unittest.TestCase):
    """Los cinco modelos de la fase — EP-003 · HU-003."""

    RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CINCO = {
        "ciclo-vida-proyectos/07-plan-trabajo.md": "qué se va a hacer",
        "ciclo-vida-proyectos/08-plan-pruebas.md": "con qué casos se comprueba",
        "ciclo-vida-proyectos/09-resultado-pruebas.md": "qué dio al correr",
        "ciclo-vida-proyectos/10-estado-fase.md": "en qué estación va",
        "ciclo-vida-proyectos/11-funcionalidad-implementada.md": "qué quedó hecho",
    }

    def test_los_cinco_modelos_de_la_fase_existen(self):
        for modelo in self.CINCO:
            self.assertTrue(
                os.path.isfile(os.path.join(self.RAIZ, "plantillas", *modelo.split("/"))),
                f"falta el modelo `{modelo}`")

    def test_el_plan_no_lleva_columna_de_estado(self):
        """CP-004: el plan se aprueba antes y **no se reescribe después**. Una
        columna de estado invitaría a tocarlo mientras se ejecuta, y entonces
        dejaría de servir para comparar lo dicho contra lo hecho."""
        molde = comun.leer(os.path.join(self.RAIZ, "plantillas", "planes", "trabajo.md"))
        cabeceras = [l for l in molde.splitlines()
                     if l.startswith("|") and "Tarea" in l]
        for c in cabeceras:
            self.assertNotIn("Estado", c,
                             f"el molde del plan trae columna de estado: {c}")

    def test_el_avance_de_las_tareas_vive_en_el_estado_de_fase(self):
        """La contraparte: si el plan no lleva estado, alguien tiene que
        llevarlo. Es el `estado-fase`, y por eso copia los identificadores."""
        molde = comun.leer(os.path.join(self.RAIZ, "plantillas", "ciclo-vida-proyectos/10-estado-fase.md"))
        self.assertIn("Avance de las tareas", molde)

    def test_limites_la_fase_recien_abierta_tiene_forma_en_el_resultado(self):
        molde = comun.leer(os.path.join(self.RAIZ, "plantillas", "ciclo-vida-proyectos/10-estado-fase.md"))
        self.assertIn("Todavía no se ejecutó", molde,
                      "el molde no dice cómo se ve una fase sin ejecutar")


class ModelosDeLaCapaDeProyecto(unittest.TestCase):
    """Los modelos de la capa 3 — EP-003 · HU-005."""

    RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    TRES = ("stack.md", "dominio.md", "mapeo-nombres.md")

    def test_los_tres_modelos_de_la_capa_de_proyecto_existen(self):
        for modelo in self.TRES:
            self.assertTrue(
                os.path.isfile(os.path.join(self.RAIZ, "plantillas", modelo)),
                f"falta el modelo `{modelo}`")

    def test_privacidad_ningun_modelo_pide_credenciales(self):
        """Transversal de privacidad: un modelo que pidiera una clave la
        convertiría en un archivo versionado en cada proyecto que lo llene."""
        prohibidas = ("contraseña", "password", "api key", "api_key", "token de",
                      "clave de acceso", "credencial")
        for modelo in self.TRES:
            texto = comun.leer(os.path.join(self.RAIZ, "plantillas", modelo)).lower()
            for palabra in prohibidas:
                self.assertNotIn(
                    palabra + ":", texto,
                    f"`{modelo}` pide `{palabra}` como dato por llenar")

    def test_limites_el_proyecto_recien_instalado_tiene_los_tres_vacios(self):
        """Con los tres documentos recién copiados y sin llenar, el marcador
        `«…»` sigue puesto: eso es lo que `13·DOC20` usa para saber que el
        documento no está terminado."""
        for modelo in self.TRES:
            texto = comun.leer(os.path.join(self.RAIZ, "plantillas", modelo))
            self.assertIn("«", texto,
                          f"`{modelo}` no marca sus espacios por llenar")


class _ProyectoDePrueba(unittest.TestCase):
    """Base de las clases de EP-007: un proyecto temporal con git."""

    VALIDADORES = os.path.dirname(os.path.abspath(__file__))
    # Los enganches se mudaron al adaptador el 2026-08-19: `validadores/`
    # es lo que sirve con cualquier agente, y esto existe porque **esta**
    # herramienta lo llama.
    ADAPTADOR = os.path.join(os.path.dirname(VALIDADORES),
                             "adaptadores", "claude-code")

    def _proyecto(self, nombre="proyecto"):
        if not shutil.which("git"):
            self.skipTest("sin git")
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        raiz = os.path.join(tmp.name, nombre)
        os.makedirs(raiz)
        subprocess.run(["git", "init"], cwd=raiz, capture_output=True, timeout=30)
        # El instalador anota el proyecto en el registro del estándar: es su
        # conducta normal, así que se deja y se devuelve el archivo como estaba.
        registro = instalar.REGISTRO
        antes = comun.leer(registro) if os.path.isfile(registro) else None
        if antes is not None:
            self.addCleanup(lambda: open(registro, "w", encoding="utf-8").write(antes))
        return raiz

    def _instalar(self, raiz, aplicar):
        orden = [sys.executable, os.path.join(self.VALIDADORES, "instalar.py"), raiz]
        if aplicar:
            orden.append("--aplicar")
        return subprocess.run(orden, capture_output=True, text=True, encoding="utf-8", timeout=180)

    def _archivos(self, raiz):
        encontrados = {}
        for carpeta, dirs, archivos in os.walk(raiz):
            dirs[:] = [d for d in dirs if d != ".git"]
            for a in archivos:
                completa = os.path.join(carpeta, a)
                encontrados[os.path.relpath(completa, raiz)] = comun.leer(completa)
        return encontrados


class RutasLargas(_ProyectoDePrueba):
    """El instalador deja puesto `core.longpaths` — EP-007 · HU-009.

    En Windows, guardar una ruta de más de 260 caracteres falla con «Filename
    too long». Le pasó a este repositorio y detuvo un commit dos veces.

    **Ninguna prueba fabrica rutas largas, y es a propósito.** Que el ajuste
    sirva ya está comprobado en la realidad: es lo que dejó pasar el commit de
    1005 archivos con 59 rutas sobre el tope. Fabricar el caso extremo probaría
    a git, no al instalador.
    """

    def _ajuste(self, raiz):
        return subprocess.run(
            ["git", "config", "--get", "core.longpaths"], cwd=raiz,
            capture_output=True, text=True, timeout=30).stdout.strip()

    def _global(self):
        return subprocess.run(
            ["git", "config", "--global", "--get", "core.longpaths"],
            capture_output=True, text=True, timeout=30).stdout.strip()

    # -- CA-01 · instalar deja el ajuste puesto ---------------------------
    def test_instalar_deja_core_longpaths_en_true(self):
        raiz = self._proyecto()
        self.assertEqual(self._ajuste(raiz), "",
                         "el repositorio de prueba ya venía con el ajuste")

        salida = self._instalar(raiz, aplicar=True)
        self.assertEqual(salida.returncode, 0, salida.stderr)

        self.assertEqual(self._ajuste(raiz), "true")
        self.assertIn("core.longpaths", salida.stdout,
                      "el instalador no dice que lo puso")

    def test_correrlo_dos_veces_no_repite_el_trabajo(self):
        raiz = self._proyecto()
        self._instalar(raiz, aplicar=True)
        salida = self._instalar(raiz, aplicar=True)
        self.assertIn("ya estaba puesto", salida.stdout)
        self.assertEqual(self._ajuste(raiz), "true")

    # -- CA-02 · un «false» puesto a propósito no se pisa -----------------
    def test_un_false_puesto_a_mano_no_se_pisa(self):
        """Pisar una decisión ajena sin decirlo es peor que no hacer nada."""
        raiz = self._proyecto()
        subprocess.run(["git", "config", "core.longpaths", "false"], cwd=raiz,
                       capture_output=True, timeout=30)

        salida = self._instalar(raiz, aplicar=True)
        self.assertEqual(salida.returncode, 0, salida.stderr)

        self.assertEqual(self._ajuste(raiz), "false",
                         "el instalador pisó un «false» puesto a propósito")
        self.assertIn("OMITIDO", salida.stdout,
                      "lo dejó como estaba, pero no lo dijo")

    # -- CA-01 · el modo que muestra no escribe ---------------------------
    def test_el_modo_que_muestra_no_pone_el_ajuste(self):
        """`HU-002` ya prometió que mostrar no toca nada. Esto no la rompe."""
        raiz = self._proyecto()
        salida = self._instalar(raiz, aplicar=False)
        self.assertIn("core.longpaths", salida.stdout,
                      "no dice que lo pondría")
        self.assertEqual(self._ajuste(raiz), "",
                         "el modo que muestra escribió el ajuste")

    # -- `RNF-01` · nada fuera del repositorio ----------------------------
    def test_no_se_toca_la_configuracion_global_de_la_maquina(self):
        """El único caso que puede ver esto.

        Un `git config --global` escrito por error le cambiaría la máquina a
        quien corra la suite, y eso no sale en ninguna otra prueba.
        """
        antes = self._global()
        raiz = self._proyecto()
        self._instalar(raiz, aplicar=False)
        self.assertEqual(self._global(), antes,
                         "el modo que muestra tocó la configuración global")
        self._instalar(raiz, aplicar=True)
        self.assertEqual(self._global(), antes,
                         "el instalador tocó la configuración global")

        # **Comparar el global antes y después no basta, y lo destapó un
        # sabotaje.** Si otra prueba ya lo dejó puesto, antes y después son
        # iguales y esto pasa aunque el instalador escriba globalmente. Se
        # pregunta por el valor **local**: si el instalador hubiera escrito
        # afuera, acá no habría nada y `--get` a secas heredaría el de la
        # máquina. Esto no depende del orden en que corran las pruebas.
        local = subprocess.run(
            ["git", "config", "--local", "--get", "core.longpaths"], cwd=raiz,
            capture_output=True, text=True, timeout=30).stdout.strip()
        self.assertEqual(local, "true",
                         "el ajuste no quedó en el repositorio: el instalador "
                         "lo escribió fuera")

    # -- CA-03 · quien clone y no instale sabe qué hacer ------------------
    def test_esta_escrito_que_hacer_al_ver_el_error(self):
        raiz_estandar = os.path.dirname(self.VALIDADORES)
        texto = comun.leer(os.path.join(raiz_estandar, "cvds", "despliegue",
                                        "README.md"))
        self.assertIn("Filename too long", texto,
                      "no está escrito qué hacer al ver el error")
        self.assertIn("core.longpaths", texto,
                      "no dice el comando que lo resuelve")
        self.assertIn("--global", texto,
                      "no dice el comando que alcanza a los clones futuros")
        self.assertIn("no viaja al clonar", texto,
                      "no dice por qué el instalador no pudo hacerlo por uno")


class MostrarAntesDeHacer(_ProyectoDePrueba):
    """El modo que muestra no toca nada — EP-007 · HU-002."""

    def test_el_modo_que_muestra_no_escribe_ni_un_archivo(self):
        raiz = self._proyecto()
        antes = self._archivos(raiz)
        salida = self._instalar(raiz, aplicar=False)
        self.assertEqual(salida.returncode, 0, salida.stderr)
        self.assertEqual(self._archivos(raiz), antes,
                         "el modo simulación escribió algo")
        self.assertIn("SIMULACIÓN", salida.stdout)

    @unittest.expectedFailure
    def test_lo_que_muestra_es_lo_que_hace(self):
        """CA-02: cada archivo que la simulación anuncia aparece de verdad al
        aplicar, y no aparece ninguno que no hubiera anunciado.

        **Falla hoy** (defecto `D-01` de la fase): la simulación dice
        «versiones: ni las plantillas ni la versión cambiaron, no hay
        actualización que registrar» y al aplicar **sí** aparece
        `documentacion/versiones/<fecha>-<version>.md`. La causa es que en
        simulación no se ha copiado nada todavía, así que la comparación de
        huellas no ve cambios; al aplicar, los archivos ya están y el registro
        se escribe. Lo que muestra no es lo que hace, justo en el archivo que
        deja constancia de qué se instaló."""
        import re
        raiz = self._proyecto()
        simulado = self._instalar(raiz, aplicar=False).stdout
        antes = set(self._archivos(raiz))
        self._instalar(raiz, aplicar=True)
        nuevos = set(self._archivos(raiz)) - antes
        self.assertTrue(nuevos, "aplicar no creó nada")
        for archivo in nuevos:
            hoja = os.path.basename(archivo)
            self.assertIn(hoja, simulado,
                          f"apareció `{archivo}` y la simulación no lo anunció")

    def test_limites_un_proyecto_al_dia_muestra_una_lista_vacia_y_lo_dice(self):
        raiz = self._proyecto()
        self._instalar(raiz, aplicar=True)
        segunda = self._instalar(raiz, aplicar=False).stdout
        self.assertNotIn("(simulado) crear", segunda,
                         "un proyecto al día sigue anunciando trabajo")
        self.assertIn("SIMULACIÓN", segunda)

    def test_claridad_cada_linea_dice_el_verbo_y_el_archivo(self):
        """Transversal de claridad: la lista se entiende sin conocer el
        instalador por dentro. Cada línea empieza por qué se va a hacer."""
        raiz = self._proyecto()
        lineas = [l.strip() for l in self._instalar(raiz, aplicar=False).stdout.splitlines()
                  if "(simulado)" in l]
        self.assertTrue(lineas)
        # Cada línea tiene que decir **qué se va a hacer** en palabras, no
        # solo nombrar un archivo. Se acepta la orden literal de una
        # herramienta —`git config …`— porque nombra lo que ejecuta; lo que no
        # se acepta es una línea que solo diga una ruta.
        for l in lineas:
            resto = l.split("(simulado)", 1)[1].strip()
            self.assertTrue(resto, f"línea vacía: {l}")
            primera = resto.split()[0].rstrip(":")
            self.assertGreaterEqual(
                len(resto.split()), 2,
                f"la línea no dice qué se hace, solo nombra algo: {l}")
            self.assertFalse(primera.startswith((".", "/", "\\")),
                             f"la línea empieza por una ruta, no por la acción: {l}")


class EstructuraDeCarpetas(_ProyectoDePrueba):
    """Las carpetas quedan creadas y lo que existía no se toca — EP-007 · HU-003."""

    def test_instalar_dos_veces_deja_el_mismo_resultado(self):
        raiz = self._proyecto()
        self._instalar(raiz, aplicar=True)
        primera = self._archivos(raiz)
        self._instalar(raiz, aplicar=True)
        segunda = self._archivos(raiz)
        self.assertEqual(set(primera), set(segunda), "la segunda pasada creó o borró")
        distintos = [a for a in primera if primera[a] != segunda[a]]
        # El registro de versión lleva la fecha; el resto no puede cambiar.
        self.assertEqual([a for a in distintos if "versiones" not in a], [])

    def test_compatibilidad_ruta_con_espacios_y_tildes(self):
        raiz = self._proyecto("proyecto de prueba con tildes áéíóú")
        salida = self._instalar(raiz, aplicar=True)
        self.assertEqual(salida.returncode, 0, salida.stderr)
        self.assertTrue(os.path.isfile(os.path.join(raiz, "CLAUDE.md")),
                        "no instaló en una ruta con espacios y tildes")

    def test_limites_el_proyecto_completo_no_cambia_en_nada(self):
        raiz = self._proyecto()
        self._instalar(raiz, aplicar=True)
        antes = self._archivos(raiz)
        salida = self._instalar(raiz, aplicar=False)
        self.assertEqual(self._archivos(raiz), antes)
        self.assertNotIn("(simulado) crear", salida.stdout)


class GenerarLosAutomatismos(_ProyectoDePrueba):
    """Los automatismos quedan puestos — EP-007 · HU-004."""

    def _ajustes(self, raiz):
        with open(os.path.join(raiz, ".claude", "settings.json"),
                  encoding="utf-8") as f:
            return json.load(f)

    def test_los_enganches_quedan_registrados_con_su_momento(self):
        raiz = self._proyecto()
        self._instalar(raiz, aplicar=True)
        ganchos = self._ajustes(raiz).get("hooks", {})
        self.assertTrue(ganchos, "no quedó ningún enganche registrado")
        puestos = json.dumps(ganchos)
        for guion in ("hook_sesion.py", "hook_historico.py", "hook_recuerdos.py",
                      "hook_md.py", "hook_checklist.py", "hook_resumen.py"):
            self.assertIn(guion, puestos, f"falta `{guion}`")

    def test_no_se_duplican_al_instalar_dos_veces(self):
        raiz = self._proyecto()
        self._instalar(raiz, aplicar=True)
        una = json.dumps(self._ajustes(raiz).get("hooks", {}))
        self._instalar(raiz, aplicar=True)
        dos = json.dumps(self._ajustes(raiz).get("hooks", {}))
        self.assertEqual(una, dos, "los enganches se duplicaron")

    def test_un_enganche_que_se_cae_no_detiene_el_trabajo(self):
        """CA-01: todos los enganches terminan en 0 aunque su proyecto no
        tenga nada instalado. Si uno reventara, la sesión se caería con él."""
        vacio = tempfile.mkdtemp()
        self.addCleanup(lambda: shutil.rmtree(vacio, ignore_errors=True))
        entrada = json.dumps({"session_id": "s1", "cwd": vacio,
                              "prompt": "hola", "transcript_path": ""})
        for guion, args in (("hook_sesion.py", []),
                            ("hook_historico.py", ["--modo", "prompt"]),
                            ("hook_recuerdos.py", []),
                            ("hook_resumen.py", ["--modo", "inicio"])):
            salida = subprocess.run(
                [sys.executable, os.path.join(self.ADAPTADOR, guion),
                 *args, "--raiz", vacio],
                input=entrada, capture_output=True, text=True, encoding="utf-8", timeout=60)
            self.assertEqual(salida.returncode, 0,
                             f"`{guion}` terminó en {salida.returncode}: {salida.stderr[:200]}")

    def test_compatibilidad_la_ruta_generada_soporta_espacios(self):
        raiz = self._proyecto("carpeta con espacios")
        self._instalar(raiz, aplicar=True)
        puestos = json.dumps(self._ajustes(raiz).get("hooks", {}))
        self.assertIn("hook_sesion.py", puestos)


class ElGuionSeQuedaEnElRepositorio(unittest.TestCase):
    """Avisar al escribir fuera del proyecto — EP-005 · HU-018.

    **La regla ya existía y se incumplió cuatro días seguidos.** `04·S9` dice
    que el agente escribe solo dentro del proyecto; el usuario lo precisó el
    2026-08-22 y se dejó de cumplir el 24: 38 guiones en la carpeta temporal
    del sistema (`S-057`).

    **Lo que se vigila no es que avise: es que NO avise de más.** El agente
    escribe decenas de archivos del proyecto por sesión, y un solo falso
    positivo por sesión convierte esto en ruido — que se apaga, y con él lo que
    sí avisaba.
    """

    RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ADAPTADOR = os.path.join(RAIZ, "adaptadores", "claude-code")

    def _casa(self, nombre="agente"):
        """Un proyecto de verdad en disco: resolver una ruta que no existe
        no comprueba lo mismo."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        casa = os.path.join(tmp.name, nombre)
        os.makedirs(os.path.join(casa, "validadores"))
        os.makedirs(os.path.join(casa, "historico-chat", "scripts"))
        return tmp.name, casa

    # -- CA-01 · escribir fuera avisa, y dice dónde iba --------------------
    def test_escribir_fuera_avisa(self):
        padre, casa = self._casa()
        texto = rutas_fuera.aviso(os.path.join(padre, "suelto.py"), casa)
        self.assertTrue(texto, "no avisó de un archivo fuera del proyecto")

    def test_el_aviso_nombra_la_ruta_y_el_destino(self):
        padre, casa = self._casa()
        fuera = os.path.join(padre, "suelto.py")
        texto = rutas_fuera.aviso(fuera, casa)
        self.assertIn("suelto.py", texto, "el aviso no dice qué archivo")
        self.assertIn(rutas_fuera.DESTINO, texto,
                      "el aviso no dice dónde debía ir")

    # -- CA-02 · y NO avisa al escribir dentro ----------------------------
    #
    # **Es el caso crítico.** Un enganche que habla en cada escritura se apaga
    # el mismo día, y entonces no queda nada.

    def test_no_avisa_por_las_rutas_del_proyecto(self):
        _, casa = self._casa()
        dentro = [
            os.path.join(casa, "validadores", "x.py"),
            os.path.join(casa, "historico-chat", "scripts", "y.py"),
            os.path.join(casa, "README.md"),
            casa,
        ]
        for ruta in dentro:
            self.assertEqual(rutas_fuera.aviso(ruta, casa), "",
                             "avisó por una ruta del proyecto: %s" % ruta)

    def test_no_avisa_por_una_ruta_relativa_dentro_del_proyecto(self):
        """**Lo pidió un sabotaje que pasó en verde**, y el plan ya lo exigía.

        `normpath` colapsa un `..` sin tocar el disco, así que los casos con
        `..` pasan igual aunque la ruta no se resuelva. **La relativa es la
        única que distingue resolver de no resolver**: sin `abspath` no tiene
        con qué compararse contra el proyecto.
        """
        _, casa = self._casa()
        antes = os.getcwd()
        os.chdir(casa)
        self.addCleanup(os.chdir, antes)
        for ruta in ("README.md", os.path.join("validadores", "x.py"), "."):
            self.assertEqual(rutas_fuera.aviso(ruta, casa), "",
                             "avisó por una ruta relativa del proyecto: %s" % ruta)

    def test_no_avisa_por_una_ruta_que_sale_y_vuelve_a_entrar(self):
        _, casa = self._casa()
        vuelve = os.path.join(casa, "validadores", "..", "README.md")
        self.assertEqual(rutas_fuera.aviso(vuelve, casa), "")

    def test_no_avisa_por_los_dos_separadores(self):
        _, casa = self._casa()
        for ruta in (casa + "/validadores/x.py", casa + "\\validadores\\x.py"):
            self.assertEqual(rutas_fuera.aviso(ruta, casa), "", ruta)

    # -- CA-03 · el borde que un `startswith` no ve -----------------------
    def test_la_carpeta_hermana_con_el_mismo_prefijo_si_avisa(self):
        """`…/agente` es prefijo de `…/agente-viejo`.

        Comparando cadenas, la hermana pasa por dentro — y el aviso calla
        justo donde debía hablar.
        """
        padre, casa = self._casa("agente")
        hermana = os.path.join(padre, "agente-viejo", "x.py")
        self.assertTrue(rutas_fuera.aviso(hermana, casa),
                        "una carpeta hermana pasó por dentro del proyecto")

    def test_una_ruta_que_empieza_dentro_y_termina_fuera_avisa(self):
        padre, casa = self._casa()
        sale = os.path.join(casa, "validadores", "..", "..", "afuera.py")
        self.assertTrue(rutas_fuera.aviso(sale, casa))

    # -- CA-05 · ninguna entrada mala detiene el trabajo ------------------
    def test_no_revienta_con_entradas_malas(self):
        _, casa = self._casa()
        for ruta in ("", None, "   "):
            self.assertEqual(rutas_fuera.aviso(ruta, casa), "", repr(ruta))
        self.assertEqual(rutas_fuera.aviso("x.py", ""), "")

    def test_si_la_ruta_no_se_deja_resolver_se_calla(self):
        """**Lo pidió un sabotaje que pasó en verde.**

        Ante la duda no se acusa (`04·R4`): sin poder resolver la ruta no hay
        con qué afirmar que esté fuera, y un aviso falso apaga el enganche
        entero.

        **Se fuerza el fallo a propósito.** El primer intento usó una ruta con
        un byte nulo creyendo que reventaría, y **no revienta**: se resuelve
        contra el directorio actual como cualquier otra. Una prueba que no
        toca la rama que dice probar es peor que no tenerla.
        """
        _, casa = self._casa()
        original = os.path.realpath

        def revienta(_ruta):
            raise OSError("de mentira, para tocar la rama")

        os.path.realpath = revienta
        self.addCleanup(setattr, os.path, "realpath", original)
        self.assertEqual(rutas_fuera.aviso(os.path.join(casa, "..", "x.py"), casa), "",
                         "acusó por una ruta que no pudo resolver")

    def test_el_enganche_calla_y_sale_bien_con_entrada_rota(self):
        for entrada in ("", "no soy json", "[]", '{"tool_input":{}}'):
            salida = subprocess.run(
                [sys.executable, os.path.join(self.ADAPTADOR, "hook_rutas.py"),
                 "--raiz", self.RAIZ],
                input=entrada, capture_output=True, text=True,
                encoding="utf-8", timeout=60)
            self.assertEqual(salida.returncode, 0,
                             "el enganche murió con %r" % entrada)
            self.assertEqual(salida.stdout.strip(), "",
                             "el enganche habló con %r" % entrada)

    # -- CA-01 · conexión: el enganche corre de verdad --------------------
    def test_el_enganche_avisa_por_una_ruta_de_afuera(self):
        entrada = json.dumps({"tool_input": {
            "file_path": os.path.join(tempfile.gettempdir(), "suelto.py")}})
        salida = subprocess.run(
            [sys.executable, os.path.join(self.ADAPTADOR, "hook_rutas.py"),
             "--raiz", self.RAIZ],
            input=entrada, capture_output=True, text=True,
            encoding="utf-8", timeout=60)
        self.assertEqual(salida.returncode, 0)
        self.assertIn("fuera del proyecto", salida.stdout)

    def test_el_enganche_calla_por_una_ruta_del_proyecto(self):
        entrada = json.dumps({"tool_input": {
            "file_path": os.path.join(self.RAIZ, "validadores", "comun.py")}})
        salida = subprocess.run(
            [sys.executable, os.path.join(self.ADAPTADOR, "hook_rutas.py"),
             "--raiz", self.RAIZ],
            input=entrada, capture_output=True, text=True,
            encoding="utf-8", timeout=60)
        self.assertEqual(salida.stdout.strip(), "",
                         "avisó por un archivo del propio repositorio")

    def test_el_enganche_esta_registrado_en_el_instalador(self):
        """**Construido y no colgado no sirve de nada.**

        Es el defecto de `EP-002·HU-004`: el aviso de desfase estaba escrito,
        probado y en verde, y el arranque no lo llamaba.
        """
        guiones = [h[2] for h in instalar.HOOKS_CLAUDE]
        self.assertIn("hook_rutas.py", guiones,
                      "el enganche existe pero nadie lo cuelga")

    # -- CA-04 · la regla dice dónde van los guiones ----------------------
    def test_la_regla_esta_en_base_y_nombra_la_carpeta(self):
        texto = comun.leer(os.path.join(self.RAIZ, "base", "04-seguridad.md"))
        self.assertIn("historico-chat/scripts/", texto,
                      "`base/` no dice dónde van los guiones de apoyo")

    def test_la_regla_declara_su_dependencia_con_s9(self):
        """`M7` y `M12`: se declara de qué cuelga, y no se repite."""
        texto = comun.leer(os.path.join(self.RAIZ, "base", "04-seguridad.md"))
        bloque = texto.split("## S18")[-1].split("\n## ")[0]
        self.assertIn("S9", bloque,
                      "la regla nueva no declara su dependencia con `04·S9`")


class NoPisarLoEscrito(_ProyectoDePrueba):
    """Lo que la persona llenó no se pierde — EP-007 · HU-005."""

    def test_el_archivo_modificado_a_mano_conserva_su_contenido(self):
        raiz = self._proyecto()
        self._instalar(raiz, aplicar=True)
        propio = os.path.join(raiz, ".agente", "stack.md")
        with open(propio, "a", encoding="utf-8") as f:
            f.write("\n## Lo que escribió la persona\n\nEsto no se puede perder.\n")
        self._instalar(raiz, aplicar=True)
        self.assertIn("Esto no se puede perder", comun.leer(propio))

    def test_el_claude_md_con_texto_propio_sobrevive(self):
        raiz = self._proyecto()
        self._instalar(raiz, aplicar=True)
        claude = os.path.join(raiz, "CLAUDE.md")
        with open(claude, "a", encoding="utf-8") as f:
            f.write("\n## Regla propia del proyecto\n\nNo tocar los viernes.\n")
        self._instalar(raiz, aplicar=True)
        self.assertIn("No tocar los viernes", comun.leer(claude))

    def test_los_dos_enganches_de_git_si_se_reemplazan(self):
        """Comportamiento definido, la mitad del transversal de límites: de los
        15 archivos que deja la instalación, **13 conservan** lo que la persona
        les escriba y **2 no** — los guiones de `.githooks/`, que son programa
        generado y no documento por llenar."""
        raiz = self._proyecto()
        self._instalar(raiz, aplicar=True)
        gancho = os.path.join(raiz, ".githooks", "commit-msg")
        with open(gancho, "a", encoding="utf-8") as f:
            f.write("\n# lo escribió la persona\n")
        self._instalar(raiz, aplicar=True)
        self.assertNotIn("lo escribió la persona", comun.leer(gancho))

    def test_limites_pisar_un_archivo_modificado_se_avisa(self):
        """La otra mitad del transversal: «tiene comportamiento definido **y se
        avisa**».

        Se avisa: con el archivo intacto el plan dice «commit-msg ya estaba al
        día»; con el archivo modificado dice «escribir .githooks/commit-msg».
        Quien lea el plan ve que ese archivo va a cambiar.

        Lo que el aviso **no** distingue es escribirlo por primera vez de
        pisar lo que alguien escribió: la palabra es la misma. Queda anotado
        como observación en el resultado de la fase, no como incumplimiento —
        el criterio pide avisar, y avisa."""
        raiz = self._proyecto()
        self._instalar(raiz, aplicar=True)
        limpio = self._instalar(raiz, aplicar=False).stdout
        gancho = os.path.join(raiz, ".githooks", "commit-msg")
        with open(gancho, "a", encoding="utf-8") as f:
            f.write("\n# lo escribió la persona\n")
        modificado = self._instalar(raiz, aplicar=False).stdout
        self.assertNotEqual(
            limpio, modificado,
            "el plan dice lo mismo con el archivo intacto que modificado")

    def test_el_registro_de_version_dice_que_se_actualizo(self):
        raiz = self._proyecto()
        self._instalar(raiz, aplicar=True)
        carpeta = os.path.join(raiz, "documentacion", "versiones")
        registros = [n for n in os.listdir(carpeta) if n != "README.md"]
        self.assertTrue(registros, "no quedó registro de versión")
        texto = comun.leer(os.path.join(carpeta, registros[0]))
        self.assertIn(comun.leer(os.path.join(
            os.path.dirname(self.VALIDADORES), "VERSION")).strip(), texto)


class NumeracionDePendientes(unittest.TestCase):
    """El número de pendiente ya tomado — EP-004 · HU-018.

    Lo que esto evita es concreto: los pendientes se citan entre sí por número
    —«hermano del 33», «el punto 2 del 53»—, así que dar un número ya usado
    rompe esas citas **sin que nadie se entere**, porque los dos archivos
    existen y ninguno pisa al otro.
    """

    RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def _carpeta(self, abiertos=(), cerrados=(), indice=None):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        raiz = os.path.join(tmp.name, "pendientes")
        os.makedirs(os.path.join(raiz, "hecho"), exist_ok=True)
        for nombre in abiertos:
            with open(os.path.join(raiz, nombre), "w", encoding="utf-8") as f:
                f.write("# pendiente de mentira\n")
        for nombre in cerrados:
            with open(os.path.join(raiz, "hecho", nombre), "w", encoding="utf-8") as f:
                f.write("# cerrado de mentira\n")
        if indice is not None:
            with open(os.path.join(raiz, "README.md"), "w", encoding="utf-8") as f:
                f.write(indice)
        return tmp.name

    # -- CA-01 · cuál es el próximo número libre --------------------------
    def test_dice_cual_es_el_proximo_numero_libre(self):
        raiz = self._carpeta(abiertos=("01-uno.md", "02-dos.md", "03-tres.md"))
        self.assertEqual(pendientes.proximo_libre(raiz), 4)
        self.assertIn("el próximo libre es el 04", pendientes.linea_proximo(raiz))

    def test_el_hueco_no_se_reutiliza(self):
        """El índice dice que «el número no se reutiliza ni se renumeran los
        demás: los huecos son historia». Entregar un hueco haría que «el 02»
        apuntara a dos cosas distintas según cuándo se leyera."""
        raiz = self._carpeta(abiertos=("01-uno.md", "05-cinco.md"))
        self.assertEqual(pendientes.proximo_libre(raiz), 6)

    def test_el_numero_de_un_cerrado_sigue_tomado_aunque_pierda_el_nombre(self):
        """**El caso que destapó el defecto de fondo.** Al cerrar un pendiente
        su archivo se mueve a `hecho/` y **pierde el número**: `02-vigencia…md`
        pasa a `vigencia-y-poda-de-memoria.md`. Mirando solo la carpeta, el 02
        parece libre. Lo que conserva la numeración es la fila tachada del
        índice, `~~02~~`, y por eso hay que leerlo."""
        indice = ("# Pendientes\n\n"
                  "| # | P | Pendiente |\n|---|---|---|\n"
                  "| 01 | P1 | [uno](01-uno.md) |\n"
                  "| ~~02~~ | — | **hecho** → [dos](hecho/sin-numero.md) |\n")
        raiz = self._carpeta(abiertos=("01-uno.md",),
                             cerrados=("sin-numero.md",), indice=indice)
        self.assertIn(2, pendientes.tomados(raiz),
                      "el número de un cerrado se dio por libre")
        self.assertEqual(pendientes.proximo_libre(raiz), 3)

    def test_la_linea_sale_en_la_corrida_de_verdad(self):
        salida = subprocess.run(
            [sys.executable, os.path.join(self.RAIZ, "validadores", "validar.py"),
             "pendientes"], capture_output=True, text=True, encoding="utf-8", timeout=120, cwd=self.RAIZ)
        self.assertIn("el próximo libre es el", salida.stdout)
        self.assertEqual(salida.returncode, 0)

    def _de_numeracion(self, raiz):
        """Las fallas **de numeración**, que es lo que esta clase mide.

        Desde el 2026-08-22 `pendientes.validar` también comprueba que un
        pendiente abierto nombre su historia (`EP-004·HU-016`), y los árboles de
        mentira de estas pruebas no la traen. Filtrar por asunto es lo correcto:
        contar todo lo que reporta el módulo haría que cada comprobación nueva
        rompiera pruebas que no hablan de ella.
        """
        return [h for h in pendientes.validar(raiz)
                if h.severidad == comun.FALLA and "número" in h.mensaje]

    # -- CA-02 · el número repetido ---------------------------------------
    def test_avisa_del_numero_repetido(self):
        raiz = self._carpeta(abiertos=("07-uno.md", "07-otro.md"))
        fallas = self._de_numeracion(raiz)
        self.assertEqual(len(fallas), 1)
        self.assertIn("07-uno.md", fallas[0].mensaje)
        self.assertIn("07-otro.md", fallas[0].mensaje)

    def test_el_repetido_entre_abierto_y_cerrado_tambien_se_ve(self):
        raiz = self._carpeta(abiertos=("07-uno.md",), cerrados=("07-otro.md",))
        self.assertEqual(len(self._de_numeracion(raiz)), 1)

    def test_los_ceros_a_la_izquierda_no_hacen_dos_numeros(self):
        """Transversal de límites: `07` y `7` son el mismo número. Tratarlos
        como distintos dejaría pasar justo el choque que esto busca."""
        raiz = self._carpeta(abiertos=("07-uno.md", "7-otro.md"))
        self.assertEqual(len(self._de_numeracion(raiz)), 1,
                         "`07` y `7` no se vieron como el mismo")

    # -- CA-03 · la carpeta contra el índice, en los dos sentidos ---------
    def test_el_pendiente_sin_linea_en_el_indice_se_avisa(self):
        indice = "# Pendientes\n\n| # | Pendiente |\n|---|---|\n| 01 | [uno](01-uno.md) |\n"
        raiz = self._carpeta(abiertos=("01-uno.md", "02-dos.md"), indice=indice)
        avisos = [h for h in pendientes.validar(raiz)
                  if "02-dos.md" in h.archivo
                  and "Historia de usuario" not in h.mensaje]
        self.assertEqual(len(avisos), 1)

    def test_la_linea_del_indice_sin_archivo_se_avisa(self):
        indice = ("# Pendientes\n\n| # | Pendiente |\n|---|---|\n"
                  "| 01 | [uno](01-uno.md) |\n| 02 | [dos](02-dos.md) |\n")
        raiz = self._carpeta(abiertos=("01-uno.md",), indice=indice)
        avisos = [h for h in pendientes.validar(raiz)
                  if "02-dos.md" in h.mensaje and "no está en la carpeta" in h.mensaje]
        self.assertEqual(len(avisos), 1)

    def test_este_repositorio_no_tiene_numeros_repetidos(self):
        self.assertEqual([h.mensaje for h in self._de_numeracion(self.RAIZ)], [])

    # -- transversales de límites y errores -------------------------------
    def test_limites_la_carpeta_vacia_no_revienta(self):
        raiz = self._carpeta()
        self.assertEqual(pendientes.numerados(raiz), {})
        self.assertEqual(pendientes.proximo_libre(raiz), 1)
        self.assertEqual([h for h in pendientes.validar(raiz)
                          if h.severidad == comun.FALLA], [])

    def test_limites_sin_la_carpeta_es_falla(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        hallazgos = pendientes.validar(tmp.name)
        self.assertTrue(any(h.severidad == comun.FALLA for h in hallazgos))

    def test_errores_el_archivo_sin_numero_se_reporta_y_no_detiene(self):
        """El nombre que no se puede interpretar sale como **aviso**: un
        archivo suelto no puede invalidar la comprobación de los otros."""
        raiz = self._carpeta(abiertos=("01-uno.md", "notas-sueltas.md"))
        hallazgos = pendientes.validar(raiz)
        avisos = [h for h in hallazgos if "no empieza por un número" in h.mensaje]
        self.assertEqual(len(avisos), 1)
        # Las fallas que sí puede haber son de otra comprobación: los
        # pendientes de mentira de estas pruebas no traen su historia.
        self.assertEqual([h for h in hallazgos
                          if h.severidad == comun.FALLA
                          and "Historia de usuario" not in h.mensaje], [])
        self.assertEqual(pendientes.proximo_libre(raiz), 2)   # sigue contando

    # -- transversal de no regresión --------------------------------------
    def test_no_regresion_estandar_sigue_dando_lo_mismo(self):
        salida = subprocess.run(
            [sys.executable, os.path.join(self.RAIZ, "validadores", "validar.py"),
             "estandar"], capture_output=True, text=True, encoding="utf-8", timeout=180, cwd=self.RAIZ)
        self.assertEqual(salida.returncode, 0)


class InventarioDeHU(unittest.TestCase):
    """La corrida cuenta las HU sin fase — EP-004 · HU-017.

    Lo que se vigila es que el número **salga del árbol**, no de una tabla que
    alguien mantiene a mano: una cuenta manual se desactualiza en la primera
    fase que cierre, y el inventario del pendiente 48 existe justamente porque
    eso ya pasó.
    """

    RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CINCO = ["plan_trabajo.md", "plan_pruebas.md", "resultado_pruebas.md",
             "funcionalidad_implementada.md", "estado-fase.md"]

    def _arbol(self, estructura):
        """`{'EP-001-e/HU-001-h': {'A-EP-001-HU-001-f': [documentos]}}`."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        for ruta_hu, fases_ in estructura.items():
            completa_hu = os.path.join(tmp.name, "documentacion", "epicas", ruta_hu)
            os.makedirs(completa_hu, exist_ok=True)
            for nombre_fase, documentos in fases_.items():
                completa = os.path.join(completa_hu, nombre_fase)
                os.makedirs(completa, exist_ok=True)
                for doc in documentos:
                    with open(os.path.join(completa, doc), "w", encoding="utf-8") as f:
                        f.write("# de mentira\n")
        return tmp.name

    # -- CA-01 · la corrida dice el total, las completas y las incompletas -
    def test_con_dos_hu_una_completa_y_otra_no_la_linea_dice_2_1_y_1(self):
        raiz = self._arbol({
            "EP-001-e/HU-001-completa": {"A-EP-001-HU-001-f": self.CINCO},
            "EP-001-e/HU-002-incompleta": {"A-EP-001-HU-002-f": ["plan_trabajo.md"]},
        })
        self.assertEqual(fases.inventario(raiz), (2, 1, 1))
        linea = fases.linea_inventario(raiz)
        self.assertIn("2 en total", linea)
        # **Las palabras cambiaron en la 35.2.0, la conducta no.** La línea
        # decía «1 completas · 1 incompletas»; ahora dice «terminadas» y «sin
        # terminar», porque «completas» se leía como «cumplen» y eran cosas
        # distintas (`EP-004·HU-021`). Lo que esta prueba vigila —que la línea
        # reporte las dos cuentas— sigue igual; lo que se ajustó es el texto
        # contra el que compara.
        self.assertIn("1 terminadas", linea)
        self.assertIn("1 sin terminar", linea)

    def test_la_linea_sale_en_la_corrida_de_verdad(self):
        salida = subprocess.run(
            [sys.executable, os.path.join(self.RAIZ, "validadores", "validar.py"),
             "fases"], capture_output=True, text=True, encoding="utf-8", timeout=180, cwd=self.RAIZ)
        self.assertIn("HU:", salida.stdout)
        self.assertIn("en total", salida.stdout)

    # -- CA-02 · el total coincide con las carpetas que hay ---------------
    def test_el_total_es_el_numero_de_carpetas_hu_del_arbol(self):
        raiz = os.path.join(self.RAIZ, "documentacion", "epicas")
        a_mano = 0
        for epica in sorted(os.listdir(raiz)):
            ruta = os.path.join(raiz, epica)
            if not os.path.isdir(ruta) or not epica.startswith("EP-"):
                continue
            a_mano += len([h for h in os.listdir(ruta)
                           if h.startswith("HU-")
                           and os.path.isdir(os.path.join(ruta, h))])
        self.assertEqual(fases.inventario(self.RAIZ)[0], a_mano)

    # -- CA-03 · con dos fases, completa solo si las dos lo están ---------
    def test_la_hu_con_dos_fases_solo_cuenta_completa_si_las_dos_lo_estan(self):
        con_las_dos = self._arbol({"EP-001-e/HU-001-h": {
            "A-EP-001-HU-001-una": self.CINCO,
            "B-EP-001-HU-001-otra": self.CINCO}})
        self.assertEqual(fases.inventario(con_las_dos), (1, 1, 0))

        una_a_medias = self._arbol({"EP-001-e/HU-001-h": {
            "A-EP-001-HU-001-una": self.CINCO,
            "B-EP-001-HU-001-otra": self.CINCO[:-1]}})
        self.assertEqual(fases.inventario(una_a_medias), (1, 0, 1),
                         "una HU con una fase a medias contó como completa")

    def test_la_hu_sin_ninguna_fase_no_cuenta_completa(self):
        raiz = self._arbol({"EP-001-e/HU-001-h": {}})
        self.assertEqual(fases.inventario(raiz), (1, 0, 1))

    # -- CA-04 y transversal de límites · los tres bordes -----------------
    def test_limites_la_epica_sin_hu_no_rompe_la_cuenta(self):
        raiz = self._arbol({"EP-002-con-hu/HU-001-h": {
            "A-EP-002-HU-001-f": self.CINCO}})
        os.makedirs(os.path.join(raiz, "documentacion", "epicas", "EP-001-sin-hu"))
        self.assertEqual(fases.inventario(raiz), (1, 1, 0))

    def test_limites_la_carpeta_hu_sin_su_archivo_cuenta_incompleta(self):
        """Existe como trabajo aunque le falte el documento. No contarla la
        volvería invisible, que es lo contrario de lo que el inventario hace."""
        raiz = self._arbol({"EP-001-e/HU-001-sin-su-md": {}})
        self.assertEqual(fases.inventario(raiz), (1, 0, 1))

    def test_limites_el_arbol_vacio_no_revienta_y_no_imprime_linea(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.assertEqual(fases.inventario(tmp.name), (0, 0, 0))
        self.assertEqual(fases.linea_inventario(tmp.name), "",
                         "sin árbol no debería imprimirse ninguna línea")

    def test_lo_que_no_es_epica_ni_hu_no_se_cuenta(self):
        raiz = self._arbol({"EP-001-e/HU-001-h": {"A-EP-001-HU-001-f": self.CINCO}})
        os.makedirs(os.path.join(raiz, "documentacion", "epicas", "notas"))
        os.makedirs(os.path.join(raiz, "documentacion", "epicas",
                                 "EP-001-e", "borradores"))
        self.assertEqual(fases.inventario(raiz), (1, 1, 0))

    # -- transversal de no regresión --------------------------------------
    def test_no_regresion_los_avisos_de_antes_siguen_saliendo_uno_por_uno(self):
        """Contar no puede cambiar lo que se reporta: `validar()` y el
        inventario son dos caminos separados sobre el mismo árbol."""
        raiz = self._arbol({
            "EP-001-e/HU-001-h": {"A-EP-001-HU-001-f": ["plan_trabajo.md"]}})
        faltan = [h for h in fases.validar(raiz) if "faltan documentos" in h.mensaje]
        self.assertEqual(len(faltan), 1)
        self.assertEqual(fases.inventario(raiz), (1, 0, 1))

    # -- `EP-004·HU-019` · el inventario no guarda la cuenta ---------------
    #
    # **Acá vivía la prueba que comparaba los dos números**: el del árbol
    # contra el escrito a mano en el pendiente. Se quitó porque ya no hay dos
    # que comparar — y mientras existió pasó lo que estaba puesta a cazar: las
    # copias se separaron tres veces, y la última llevaba 34 de retraso.
    # Detectarlo no alcanzaba; la salida fue que no hubiera segunda copia.
    #
    # Lo que se comprueba ahora es que no vuelva.

    def _pendiente_de_mentira(self, texto):
        """Un árbol con su pendiente del inventario. Devuelve `(raíz, ruta)`.

        En carpeta temporal: **el pendiente real no se edita para probar**
        (`08·T4`).
        """
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        os.makedirs(os.path.join(tmp.name, "pendientes"))
        ruta = os.path.join(tmp.name, "pendientes", "48-inventario-hu.md")
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)
        return tmp.name, ruta

    # -- CA-02 · reponer un número a mano se reporta ----------------------
    def test_un_total_escrito_a_mano_en_el_inventario_se_avisa(self):
        raiz, _ = self._pendiente_de_mentira(
            "# Inventario\n\n| **Total de HU** | 99 |\n")
        avisos = fases.cuenta_escrita_a_mano(raiz)
        self.assertEqual(len(avisos), 1, "la cuenta a mano no se avisó")
        self.assertIn("Total de HU", avisos[0].mensaje)
        self.assertIn("validar.py fases", avisos[0].mensaje,
                      "el aviso no dice de dónde sale la cuenta de verdad")

    def test_los_tres_campos_de_la_cuenta_se_avisan(self):
        raiz, _ = self._pendiente_de_mentira(
            "# Inventario\n\n| **Total de HU** | 99 |\n"
            "| **Completas** | 50 |\n| **Incompletas** | 49 |\n")
        self.assertEqual(len(fases.cuenta_escrita_a_mano(raiz)), 3)

    def test_sin_la_cuenta_escrita_no_se_avisa_nada(self):
        raiz, _ = self._pendiente_de_mentira(
            "# Inventario\n\nLa cuenta la da `validar.py fases`.\n")
        self.assertEqual(fases.cuenta_escrita_a_mano(raiz), [])

    # -- CA-02 · borde: la narrativa trae cifras que no son la cuenta -----
    def test_las_cifras_de_la_narrativa_no_disparan_el_aviso(self):
        """Un aviso que marca cualquier número se aprende a ignorar."""
        raiz, _ = self._pendiente_de_mentira(
            "# Inventario\n\n> **68 a 74 total.** Seis historias nuevas al "
            "enrutar el backlog: 6 que ya existían.\n")
        self.assertEqual(fases.cuenta_escrita_a_mano(raiz), [])

    # -- `RN-04` · el programa reporta y NO corrige -----------------------
    def test_avisar_de_la_cuenta_no_toca_el_archivo(self):
        """Se compara en **bytes**, no como texto.

        Comparar como texto dejaría pasar un cambio de fin de línea, que es
        justo el defecto que se coló en la fase E de la plataforma.
        """
        raiz, ruta = self._pendiente_de_mentira(
            "# Inventario\n\n| **Total de HU** | 99 |\n")
        with io.open(ruta, "rb") as f:
            antes = f.read()
        cuantos_antes = len(os.listdir(os.path.dirname(ruta)))

        self.assertTrue(fases.cuenta_escrita_a_mano(raiz),
                        "no reportó nada, así que no probaría que no corrige")

        with io.open(ruta, "rb") as f:
            self.assertEqual(f.read(), antes,
                             "el programa corrigió el archivo (`EP-004 §10.2`)")
        self.assertEqual(len(os.listdir(os.path.dirname(ruta))), cuantos_antes,
                         "el programa creó un archivo")

    # -- `RNF-02` · la comprobación sale por la corrida de siempre --------
    def test_el_aviso_sale_en_la_corrida_de_fases(self):
        """Que la comprobación exista no sirve si nadie la llama.

        **Lo destapó un sabotaje**: descolgar `cuenta_escrita_a_mano` de
        `validar` dejaba las otras seis pruebas en verde, porque todas la
        llamaban directo. Una comprobación que no sale por el comando que la
        gente corre es una comprobación que no existe.
        """
        raiz, _ = self._pendiente_de_mentira(
            "# Inventario\n\n| **Total de HU** | 99 |\n")
        os.makedirs(os.path.join(raiz, "documentacion", "epicas"))
        mensajes = [h.mensaje for h in fases.validar(raiz)]
        self.assertTrue(any("Total de HU" in m for m in mensajes),
                        "el aviso no sale por `validar`, que es lo que corre "
                        "`validar.py fases`")

    # -- `EP-004·HU-020` · el inventario se vigila donde el proyecto lo tenga
    #
    # La versión anterior miraba `pendientes/48-inventario-hu.md` escrito fijo,
    # así que vigilaba el estándar y nada más: en un proyecto el inventario
    # vive en `documentacion/`, y ahí no veía nada.

    def _proyecto_con_inventario(self, carpeta, nombre, texto):
        """Un proyecto con su inventario en la carpeta que se le diga."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        os.makedirs(os.path.join(tmp.name, "documentacion", "epicas"))
        destino = os.path.join(tmp.name, carpeta)
        if not os.path.isdir(destino):
            os.makedirs(destino)
        ruta = os.path.join(destino, nombre)
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)
        return tmp.name, ruta

    CON_CUENTA = "# Inventario\n\n| **Total de HU** | 99 |\n"

    def test_el_inventario_en_documentacion_tambien_se_vigila(self):
        raiz, _ = self._proyecto_con_inventario(
            "documentacion", "inventario-hu.md", self.CON_CUENTA)
        avisos = fases.cuenta_escrita_a_mano(raiz)
        self.assertEqual(len(avisos), 1,
                         "un proyecto que guarda su inventario en "
                         "`documentacion/` no se estaba vigilando")

    def test_el_aviso_nombra_la_ruta_real_y_no_una_fija(self):
        raiz, _ = self._proyecto_con_inventario(
            "documentacion", "cuanto-falta.md", self.CON_CUENTA)
        donde = fases.cuenta_escrita_a_mano(raiz)[0].archivo
        self.assertEqual(donde, "documentacion/cuanto-falta.md",
                         "el aviso no nombra el archivo que encontró")

    def test_el_nombre_del_archivo_no_decide_nada(self):
        """La plantilla no fija el nombre: lo elige cada proyecto.

        Lo constante es la forma del defecto, no cómo se llame el archivo.
        """
        raiz, _ = self._proyecto_con_inventario(
            "pendientes", "tablero.md", self.CON_CUENTA)
        self.assertEqual(len(fases.cuenta_escrita_a_mano(raiz)), 1)

    # -- `RNF-01` · la búsqueda tiene el alcance que se declaró -----------
    def test_fuera_de_las_carpetas_declaradas_no_se_busca(self):
        """Corta en los dos sentidos.

        Si el alcance se ampliara sin querer, esta prueba lo dice. Y si algún
        día hay que ampliarlo a propósito, **hay que cambiar esta prueba**, que
        es lo que obliga a decidirlo en vez de que ocurra solo.
        """
        raiz, _ = self._proyecto_con_inventario(
            "notas", "inventario-hu.md", self.CON_CUENTA)
        self.assertEqual(fases.cuenta_escrita_a_mano(raiz), [],
                         "se buscó fuera de las carpetas declaradas")

    def test_no_se_busca_dentro_de_las_subcarpetas(self):
        raiz, _ = self._proyecto_con_inventario(
            os.path.join("documentacion", "epicas"), "inventario-hu.md",
            self.CON_CUENTA)
        self.assertEqual(fases.cuenta_escrita_a_mano(raiz), [],
                         "se recorrió el árbol en vez del primer nivel")

    # -- CA-01 · el pendiente real ya no guarda la cuenta -----------------
    def test_el_inventario_de_este_repositorio_no_guarda_la_cuenta(self):
        self.assertEqual(fases.cuenta_escrita_a_mano(self.RAIZ), [],
                         "el inventario volvió a guardar la cuenta a mano")

    def test_el_inventario_de_este_repositorio_nombra_el_comando(self):
        texto = comun.leer(os.path.join(self.RAIZ, "pendientes",
                                        "48-inventario-hu.md"))
        self.assertIn("validar.py fases", texto,
                      "el inventario no dice con qué comando se saca la cuenta")

    # -- CA-01 · la plantilla tampoco pide mantener una cuenta ------------
    #
    # `cuenta_escrita_a_mano` mira `pendientes/` y `documentacion/`, y la
    # plantilla vive en `plantillas/`: nada la vigilaba. Y es la que se copia,
    # así que un defecto ahí se multiplica por cada proyecto que la use.

    def _plantilla_del_inventario(self):
        return comun.leer(os.path.join(self.RAIZ, "plantillas",
                                       "inventario-hu.md"))

    def test_la_plantilla_no_trae_campos_de_cuenta(self):
        """El defecto tiene **dos formas**, y una sola expresión no caza las dos.

        `fases.CUENTA_A_MANO` exige un número, porque en un inventario de
        verdad el defecto es un número escrito. En una **plantilla** el mismo
        defecto viene como `«N»`, el hueco por llenar — y con esa expresión
        pasaba desapercibido. Lo destapó un sabotaje que devolvía
        `| **Total de HU** | «N» |` a la plantilla y dejaba la suite en verde.

        Acá se busca el **rótulo como campo**, valga lo que valga: pedirle a
        alguien que llene ese hueco ya es el defecto.
        """
        rotulos = re.findall(
            r"^\|\s*\*\*(Total de HU|Completas|Incompletas)\*\*\s*\|",
            self._plantilla_del_inventario(), re.MULTILINE)
        self.assertEqual(rotulos, [],
                         "la plantilla volvió a pedir una cuenta a mano")

    def test_la_plantilla_no_trae_la_tabla_de_una_fila_por_historia(self):
        self.assertNotIn("| Épica | HU | Fase |",
                         self._plantilla_del_inventario(),
                         "la plantilla volvió a traer la tabla que se desfasa")

    def test_la_plantilla_nombra_el_comando_y_lo_entrecomilla(self):
        """Las comillas no son estilo: la ruta al estándar puede tener
        espacios —la del propio estándar los tiene— y sin ellas la terminal
        parte la orden por la mitad."""
        texto = self._plantilla_del_inventario()
        self.assertIn("validar.py", texto,
                      "la plantilla no dice con qué comando se saca la cuenta")
        self.assertIn('"«RUTA-ESTANDAR»/validadores/validar.py"', texto,
                      "el comando de la plantilla no está entrecomillado")


class LaCuentaMiraElVeredicto(unittest.TestCase):
    """Terminada no es lo mismo que cumplida — EP-004 · HU-021.

    Hasta la 35.1.0 el conteo miraba que los documentos estuvieran. Eso dice si
    el trabajo se **terminó**, no si **cumplió**: diecinueve fases cerradas con
    «No cumple» contaban entre las completas.

    **El caso que más importa es el de la tercera cuenta.** Repartir entre
    «cumple» y «no cumple» lo que no se deja leer haría que el número mintiera
    de una forma nueva, que es justo lo que esto viene a terminar.
    """

    RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CINCO = ["plan_trabajo.md", "plan_pruebas.md", "resultado_pruebas.md",
             "estado-fase.md", "funcionalidad_implementada.md"]

    def _arbol(self, fases_y_veredictos, hu="HU-001-una"):
        """`{"A-EP-001-HU-001-x": "Cumple" | "No cumple" | None}`.

        `None` deja el resultado sin veredicto legible.
        """
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        base = os.path.join(tmp.name, "documentacion", "epicas", "EP-001-e", hu)
        for nombre, veredicto in fases_y_veredictos.items():
            carpeta = os.path.join(base, nombre)
            os.makedirs(carpeta)
            for doc in self.CINCO:
                cuerpo = "# de mentira\n"
                if doc == "resultado_pruebas.md" and veredicto:
                    cuerpo += "\n**Concepto:** %s.\n" % veredicto
                with io.open(os.path.join(carpeta, doc), "w",
                             encoding="utf-8", newline="\n") as f:
                    f.write(cuerpo)
        return tmp.name

    # -- CA-02 · basta una fase que no cumpla -----------------------------
    def test_una_historia_cuyas_fases_cumplen_cuenta_cumplida(self):
        raiz = self._arbol({"A-EP-001-HU-001-x": "Cumple",
                            "B-EP-001-HU-001-y": "Cumple"})
        self.assertEqual(fases.por_veredicto(raiz), (1, 0, 0))

    def test_basta_una_fase_que_no_cumpla(self):
        """Cerrar la primera fase no cierra la historia."""
        raiz = self._arbol({"A-EP-001-HU-001-x": "Cumple",
                            "B-EP-001-HU-001-y": "No cumple"})
        self.assertEqual(fases.por_veredicto(raiz), (0, 1, 0))

    def test_todas_sin_cumplir_tambien_es_una_sola(self):
        raiz = self._arbol({"A-EP-001-HU-001-x": "No cumple",
                            "B-EP-001-HU-001-y": "No cumple"})
        self.assertEqual(fases.por_veredicto(raiz), (0, 1, 0))

    # -- CA-03 · lo ilegible se cuenta aparte -----------------------------
    def test_sin_veredicto_no_se_reparte_entre_las_otras_dos(self):
        raiz = self._arbol({"A-EP-001-HU-001-x": None})
        cumplen, no_cumplen, sin_veredicto = fases.por_veredicto(raiz)
        self.assertEqual(sin_veredicto, 1)
        self.assertEqual(cumplen, 0, "se repartió entre las que cumplen")
        self.assertEqual(no_cumplen, 0, "se repartió entre las que no cumplen")

    def test_una_fase_ilegible_arrastra_a_la_historia_entera(self):
        """Si no se puede leer una, no se puede afirmar de la historia."""
        raiz = self._arbol({"A-EP-001-HU-001-x": "Cumple",
                            "B-EP-001-HU-001-y": None})
        self.assertEqual(fases.por_veredicto(raiz), (0, 0, 1))

    # -- Transversal · límites --------------------------------------------
    def test_limites_una_historia_a_medias_no_entra_en_ninguna_cuenta(self):
        """No tiene veredicto que dar: contarla la mezclaría con las que sí."""
        raiz = self._arbol({"A-EP-001-HU-001-x": "Cumple"})
        falta = os.path.join(raiz, "documentacion", "epicas", "EP-001-e",
                             "HU-001-una", "A-EP-001-HU-001-x",
                             "funcionalidad_implementada.md")
        os.remove(falta)
        self.assertEqual(fases.por_veredicto(raiz), (0, 0, 0))

    def test_limites_el_veredicto_con_texto_detras_se_lee(self):
        raiz = self._arbol({"A-EP-001-HU-001-x": "Cumple, en el ciclo 2"})
        self.assertEqual(fases.por_veredicto(raiz), (1, 0, 0))

    def test_limites_la_caja_no_importa_para_el_veredicto(self):
        """A diferencia del estado, acá la caja no cambia el sentido."""
        raiz = self._arbol({"A-EP-001-HU-001-x": "no cumple"})
        self.assertEqual(fases.por_veredicto(raiz), (0, 1, 0))

    def test_limites_arbol_vacio_devuelve_ceros(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.assertEqual(fases.por_veredicto(tmp.name), (0, 0, 0))

    # -- CA-01 · la línea dice las tres, y cuadran ------------------------
    def test_la_linea_dice_las_tres_cuentas(self):
        raiz = self._arbol({"A-EP-001-HU-001-x": "No cumple"})
        linea = fases.linea_inventario(raiz)
        for palabra in ("cumplen", "no cumplen", "no dicen si cumplen",
                        "sin terminar", "terminadas"):
            self.assertIn(palabra, linea,
                          "la línea no dice «%s»" % palabra)

    def test_las_tres_cuentas_suman_las_terminadas(self):
        """Sobre el árbol real, que es el único con variedad de verdad."""
        _total, completas, _inc = fases.inventario(self.RAIZ)
        cumplen, no_cumplen, sin_veredicto = fases.por_veredicto(self.RAIZ)
        self.assertEqual(cumplen + no_cumplen + sin_veredicto, completas,
                         "las tres cuentas no suman las terminadas: alguna "
                         "historia se contó dos veces o ninguna")

    # -- CA-03 (fase B) · las tres formas del veredicto -------------------
    #
    # El veredicto está escrito de tres maneras, contadas una por una sobre las
    # 129 fases. La tercera —la palabra sola bajo el encabezado— no se leía, y
    # siete historias se contaban entre las que «no dicen si cumplen» **cuando
    # sí lo dicen**.

    def _resultado(self, cuerpo):
        """Un árbol con una fase cuyo `resultado_pruebas.md` dice `cuerpo`."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        carpeta = os.path.join(tmp.name, "documentacion", "epicas", "EP-001-e",
                               "HU-001-una", "A-EP-001-HU-001-x")
        os.makedirs(carpeta)
        for doc in self.CINCO:
            texto = cuerpo if doc == "resultado_pruebas.md" else "# x\n"
            with io.open(os.path.join(carpeta, doc), "w", encoding="utf-8",
                         newline="\n") as f:
                f.write(texto)
        return carpeta

    def test_forma_1_concepto_con_dos_puntos(self):
        c = self._resultado("## 5. Veredicto de la fase\n\n**Concepto:** Cumple.\n")
        self.assertEqual(fases.veredicto_de(c), "Cumple")

    def test_forma_2_tabla_con_concepto(self):
        c = self._resultado("## 5. Veredicto de la fase\n\n| Campo | Valor |\n"
                            "|---|---|\n| **Concepto** | **No cumple** |\n")
        self.assertEqual(fases.veredicto_de(c), "No cumple")

    def test_forma_3_la_palabra_sola_bajo_el_encabezado(self):
        """La que faltaba. Siete fases del repositorio la usan."""
        c = self._resultado("## 5. Veredicto de la fase\n\n"
                            "**Cumple.** Los tres criterios quedaron "
                            "comprobados.\n")
        self.assertEqual(fases.veredicto_de(c), "Cumple")

    def test_forma_3_tambien_para_no_cumple(self):
        c = self._resultado("## 6. Veredicto de la fase\n\n"
                            "**No cumple.** Falta el `CA-02`.\n")
        self.assertEqual(fases.veredicto_de(c), "No cumple")

    # -- CA-03 (fase B) · y no se lee de más ------------------------------
    #
    # **Es el caso crítico.** En un resultado la palabra «Cumple» aparece en
    # cada fila de criterio. Un lector que la buscara suelta tomaría el primer
    # criterio por el veredicto de la fase, y daría por cumplida una que no lo
    # está — que miente en la dirección peor.

    def test_no_lee_los_criterios_cuando_no_hay_encabezado_de_veredicto(self):
        c = self._resultado("## 3. Veredicto por criterio\n\n| CA | Concepto |\n"
                            "|---|---|\n| CA-01 | Cumple |\n"
                            "| CA-02 | Cumple |\n")
        self.assertIsNone(fases.veredicto_de(c),
                          "leyó una fila de criterio como el veredicto")

    def test_no_lee_un_encabezado_sin_nada_debajo(self):
        c = self._resultado("## 5. Veredicto de la fase\n\n"
                            "Pendiente de escribir.\n")
        self.assertIsNone(fases.veredicto_de(c))

    def test_no_lee_la_palabra_suelta_en_prosa(self):
        c = self._resultado("# Resultado\n\nLa fase cumple con lo que el plan "
                            "pedía, y se cumple el plazo.\n")
        self.assertIsNone(fases.veredicto_de(c))

    def test_no_revienta_con_el_resultado_vacio(self):
        c = self._resultado("")
        self.assertIsNone(fases.veredicto_de(c))

    # -- CA-03 (fase C) · el mismo encabezado, sin «de la fase» -----------
    #
    # La fase B dijo «tres formas y 39 fases sin encabezado». Al **enumerar**
    # los encabezados de los 130 resultados —en vez de contar los que ya se
    # reconocían— salió que sin encabezado hay **2**, y que un título más es el
    # veredicto de la fase: `## N. Veredicto`, en quince de ellas.
    #
    # **El título tiene que ser exacto.** Setenta encabezados empiezan por
    # «Veredicto» y son la tabla criterio por criterio. Aceptarlos devolvería
    # el primer criterio como veredicto de la fase — la mentira optimista.

    def test_titulo_veredicto_a_secas(self):
        """El que faltaba. Quince fases del repositorio lo usan."""
        c = self._resultado("## 5. Veredicto\n\n**Cumple.** Once casos de "
                            "once.\n")
        self.assertEqual(fases.veredicto_de(c), "Cumple")

    def test_titulo_veredicto_a_secas_tambien_para_no_cumple(self):
        c = self._resultado("## 6. Veredicto\n\n**No cumple.** El `CA-03` "
                            "sigue en rojo.\n")
        self.assertEqual(fases.veredicto_de(c), "No cumple")

    def test_el_numero_del_encabezado_no_importa(self):
        for cabeza in ("## 2. Veredicto", "## 11. Veredicto", "## 5 Veredicto"):
            c = self._resultado("%s\n\n**Cumple.**\n" % cabeza)
            self.assertEqual(fases.veredicto_de(c), "Cumple", cabeza)

    def test_no_lee_veredicto_por_criterio_de_aceptacion(self):
        """**El caso crítico de esta fase.** Cuarenta fases lo escriben así.

        Se le pone delante justo la tabla que lo tentaría: la primera fila dice
        `Cumple`. Tomarla sería dar por cumplida la fase leyendo un criterio.
        """
        c = self._resultado("## 4. Veredicto por criterio de aceptación\n\n"
                            "| CA | Concepto |\n|---|---|\n"
                            "| CA-01 | Cumple |\n| CA-02 | No cumple |\n")
        self.assertIsNone(fases.veredicto_de(c),
                          "tomó un criterio por el veredicto de la fase")

    def test_no_lee_veredicto_por_criterio_y_requisito_no_funcional(self):
        c = self._resultado("## 4. Veredicto por criterio de aceptación y "
                            "requisito no funcional\n\n**Cumple.**\n")
        self.assertIsNone(fases.veredicto_de(c))

    def test_no_lee_veredicto_final(self):
        """Sus cuatro casos no van seguidos de la palabra: no se agrega."""
        c = self._resultado("## 6. Veredicto final\n\n**Cumple.**\n")
        self.assertIsNone(fases.veredicto_de(c))

    def test_no_lee_los_otros_dos_titulos_parecidos(self):
        for titulo in ("Veredicto por exigencia",
                       "Veredicto por criterio de la historia"):
            c = self._resultado("## 3. %s\n\n**Cumple.**\n" % titulo)
            self.assertIsNone(fases.veredicto_de(c), titulo)

    def test_el_titulo_solo_tampoco_lee_un_encabezado_vacio(self):
        c = self._resultado("## 5. Veredicto\n\nSe escribe al cerrar.\n")
        self.assertIsNone(fases.veredicto_de(c))

    def test_la_palabra_tiene_que_ir_pegada_al_encabezado(self):
        """**Lo pidió un sabotaje que pasó en verde.**

        Aflojar el patrón para que la palabra pueda estar en cualquier parte
        después del encabezado no rompía ninguna prueba: las que había ponían
        `Cumple` justo debajo, o no lo ponían en ninguna parte. **Faltaba el
        caso de en medio**, que es el que ocurre de verdad — un encabezado de
        veredicto seguido de prosa, y la palabra más abajo dentro de una tabla
        de criterios.
        """
        c = self._resultado("## 5. Veredicto\n\nEl detalle va en la tabla.\n\n"
                            "| CA | Concepto |\n|---|---|\n| CA-01 | Cumple |\n")
        self.assertIsNone(fases.veredicto_de(c),
                          "se saltó la prosa y leyó una fila de criterio")

    # -- CA-04 · los moldes usan un solo vocabulario ----------------------
    #
    # **Lo pidió un sabotaje.** Devolver al molde del cierre su tercer valor
    # dejaba las doce pruebas en verde: el criterio solo tenía comprobación a
    # mano, y un molde sin guardia vuelve a lo de antes en la primera edición.
    # Es el mismo hueco que la `HU-020` encontró con la plantilla del
    # inventario.

    def _molde(self, nombre):
        return comun.leer(os.path.join(self.RAIZ, "plantillas",
                                       "ciclo-vida-proyectos",
                                       "%s.md" % nombre))

    def test_el_molde_del_cierre_no_ofrece_un_tercer_valor(self):
        texto = self._molde("11-funcionalidad-implementada")
        campo = [l for l in texto.split("\n")
                 if l.startswith("| **Veredicto**")]
        self.assertEqual(len(campo), 1,
                         "el molde del cierre no tiene su campo de veredicto")
        self.assertIn("No cumple", campo[0],
                      "el molde no puede declarar «No cumple»")
        self.assertNotIn("con observaciones", campo[0],
                         "el molde volvió a ofrecer un tercer valor")

    def test_ningun_molde_prohibe_cerrar_con_un_criterio_en_rojo(self):
        """La regla decía lo contrario de lo que se hace, y se hace bien."""
        for nombre in ("07-plan-trabajo", "09-resultado-pruebas",
                       "11-funcionalidad-implementada"):
            self.assertNotIn("no cierra con", self._molde(nombre),
                             "%s volvió a prohibir cerrar con un rojo" % nombre)

    # -- Transversal · no regresión ---------------------------------------
    def test_no_regresion_inventario_sigue_devolviendo_tres_valores(self):
        """Diez pruebas dependen de su firma. La cuenta nueva va aparte."""
        self.assertEqual(len(fases.inventario(self.RAIZ)), 3)

    def test_la_cuenta_nueva_no_cambia_el_total_ni_las_sin_terminar(self):
        raiz = self._arbol({"A-EP-001-HU-001-x": "No cumple"})
        self.assertEqual(fases.inventario(raiz), (1, 1, 0),
                         "la cuenta nueva movió lo que no debía")


class LasPruebasQueExistenSeCorren(unittest.TestCase):
    """`EP-005·HU-021` · 650 pruebas escritas que ningún comando ejecutaba.

    **El caso que lo hizo falta:** una prueba escrita para cazar exactamente el
    defecto que tuvimos seis días en rojo **nunca se corrió**, porque la orden
    documentada se caía antes de correr nada (`S-075`).

    **Lo que más se vigila es que cero pruebas NO pase por verde.** Ese es el
    defecto original, y un corredor que lo repita no arregla nada: lo disfraza.
    """

    RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    UNA_QUE_PASA = ("import unittest\n"
                    "class C(unittest.TestCase):\n"
                    "    def test_a(self): self.assertTrue(True)\n"
                    "    def test_b(self): self.assertTrue(True)\n")
    UNA_QUE_FALLA = ("import unittest\n"
                     "class D(unittest.TestCase):\n"
                     "    def test_c(self): self.assertEqual(1, 2)\n")

    def _proyecto(self, con=()):
        """Un proyecto de mentira con su `validadores/tests/`."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        carpeta = os.path.join(tmp.name, "validadores", "tests")
        os.makedirs(carpeta)
        for nombre, cuerpo in con:
            with io.open(os.path.join(carpeta, nombre), "w",
                         encoding="utf-8", newline="\n") as f:
                f.write(cuerpo)
        return tmp.name

    # -- CA-02 · cero pruebas es rojo -------------------------------------
    #
    # **Es el crítico.** Es el defecto original, y reconstruirlo sería cambiar
    # una orden que no corría nada por otra que tampoco.

    def test_la_carpeta_vacia_es_roja(self):
        raiz = self._proyecto()
        fallas = [h for h in corredor.validar(raiz) if h.severidad == FALLA]
        self.assertTrue(fallas, "una carpeta vacía pasó por verde")
        self.assertIn("0 pruebas", fallas[0].mensaje)

    def test_la_carpeta_que_no_existe_es_roja(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        fallas = [h for h in corredor.validar(tmp.name)
                  if h.severidad == FALLA]
        self.assertTrue(fallas, "sin carpeta, dijo que estaba bien")
        self.assertIn("no existe", fallas[0].mensaje)

    def test_archivos_sin_ninguna_prueba_dentro_es_rojo(self):
        raiz = self._proyecto([("test_vacio.py", "x = 1\n")])
        fallas = [h for h in corredor.validar(raiz) if h.severidad == FALLA]
        self.assertTrue(fallas, "un archivo sin pruebas pasó por verde")

    def test_unittest_discover_solo_daria_cero_y_por_eso_hace_falta(self):
        """No prueba el corredor: **prueba que el corredor hace falta**.

        `discover` sobre una carpeta vacía termina en 0. Si algún día dejara de
        hacerlo, esta prueba avisa de que la justificación cambió.
        """
        raiz = self._proyecto()
        with io.open(os.path.join(raiz, "validadores", "tests", "__init__.py"),
                     "w", encoding="utf-8") as f:
            f.write("")
        salida = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", "tests"],
            cwd=os.path.join(raiz, "validadores"), capture_output=True,
            text=True, encoding="utf-8", errors="replace", timeout=120)
        self.assertEqual(salida.returncode, 0,
                         "`discover` ya no da 0 con cero pruebas — la razón "
                         "por la que existe el corredor cambió")

    # -- CA-01 · corre y cuenta -------------------------------------------
    def test_corre_y_dice_cuantas(self):
        raiz = self._proyecto([("test_uno.py", self.UNA_QUE_PASA)])
        hallazgos = corredor.validar(raiz)
        self.assertEqual([], [h for h in hallazgos if h.severidad == FALLA])
        avisos = [h for h in hallazgos if h.severidad == AVISO]
        self.assertTrue(any("2 prueba(s)" in h.mensaje for h in avisos),
                        "no dijo cuántas corrió: %s"
                        % [h.mensaje for h in avisos])

    def test_una_falla_nombra_su_archivo_y_su_caso(self):
        raiz = self._proyecto([("test_uno.py", self.UNA_QUE_PASA),
                               ("test_dos.py", self.UNA_QUE_FALLA)])
        fallas = [h for h in corredor.validar(raiz) if h.severidad == FALLA]
        self.assertEqual(1, len(fallas))
        self.assertIn("test_dos.py", fallas[0].archivo)
        self.assertIn("test_c", fallas[0].mensaje)

    def test_un_archivo_que_no_carga_se_reporta_y_no_tumba_el_resto(self):
        """`EP-004·HU-003`: un archivo roto no se lleva lo que ya se sabía."""
        raiz = self._proyecto([("test_uno.py", self.UNA_QUE_PASA),
                               ("test_roto.py", "import no_existe_este_modulo\n")])
        hallazgos = corredor.validar(raiz)
        fallas = [h for h in hallazgos if h.severidad == FALLA]
        self.assertTrue(any("no se pudo cargar" in h.mensaje for h in fallas))
        self.assertTrue(
            any("2 prueba(s)" in h.mensaje for h in hallazgos),
            "el archivo roto se llevó el conteo del que sí cargó")

    # -- CA-03 · subconjunto ----------------------------------------------
    def test_se_puede_pedir_un_solo_archivo(self):
        raiz = self._proyecto([("test_uno.py", self.UNA_QUE_PASA),
                               ("test_dos.py", self.UNA_QUE_FALLA)])
        hallazgos = corredor.validar(raiz, solo=["test_uno"])
        self.assertEqual([], [h for h in hallazgos if h.severidad == FALLA],
                         "corrió el que no se le pidió")
        self.assertTrue(any("2 prueba(s) en 1 archivo(s)" in h.mensaje
                            for h in hallazgos))

    def test_un_nombre_que_no_existe_es_rojo_no_una_corrida_vacia(self):
        """Pedir mal y recibir verde es el defecto original por la puerta de al lado."""
        raiz = self._proyecto([("test_uno.py", self.UNA_QUE_PASA)])
        fallas = [h for h in corredor.validar(raiz, solo=["test_no_esta"])
                  if h.severidad == FALLA]
        self.assertTrue(any("no está en la carpeta" in h.mensaje
                            for h in fallas),
                        "un nombre mal escrito no se reportó")

    # -- CA-04 · el reclamo, y que esté colgado ---------------------------
    def test_sin_sello_reclama(self):
        raiz = self._proyecto([("test_uno.py", self.UNA_QUE_PASA)])
        avisos = corredor.reclamo(raiz)
        self.assertTrue(avisos, "no reclamó sin haber corrido nunca")
        self.assertIn("nunca corrieron", avisos[0].mensaje)

    def test_la_corrida_entera_y_limpia_deja_el_sello(self):
        raiz = self._proyecto([("test_uno.py", self.UNA_QUE_PASA)])
        corredor.validar(raiz)
        self.assertTrue(os.path.isfile(os.path.join(raiz, corredor.SELLO)),
                        "una corrida limpia no dejó constancia")

    def test_una_corrida_con_fallas_no_sella(self):
        raiz = self._proyecto([("test_dos.py", self.UNA_QUE_FALLA)])
        corredor.validar(raiz)
        self.assertFalse(os.path.isfile(os.path.join(raiz, corredor.SELLO)),
                         "selló una corrida que falló")

    def test_un_subconjunto_no_sella(self):
        """Sellar un subconjunto diría «esto se comprobó» sobre lo que no se miró."""
        raiz = self._proyecto([("test_uno.py", self.UNA_QUE_PASA),
                               ("test_tres.py", self.UNA_QUE_PASA)])
        corredor.validar(raiz, solo=["test_uno"])
        self.assertFalse(os.path.isfile(os.path.join(raiz, corredor.SELLO)),
                         "un subconjunto en verde selló la carpeta entera")

    def test_el_reclamo_calla_cuando_el_sello_es_posterior_al_commit(self):
        if not shutil.which("git"):
            self.skipTest("sin git")
        raiz = self._proyecto([("test_uno.py", self.UNA_QUE_PASA)])
        for orden in (["init", "-q"], ["config", "user.name", "p"],
                      ["config", "user.email", "p@l"],
                      ["add", "-A"], ["commit", "-qm", "base"]):
            subprocess.run(["git"] + orden, cwd=raiz, capture_output=True)
        corredor.sellar(raiz)
        self.assertEqual([], corredor.reclamo(raiz),
                         "reclamó con el sello más nuevo que el último commit")

    def test_el_reclamo_no_revienta_sin_repositorio(self):
        raiz = self._proyecto([("test_uno.py", self.UNA_QUE_PASA)])
        corredor.sellar(raiz)
        self.assertEqual([], corredor.reclamo(raiz),
                         "afirmó sobre una carpeta que no es repositorio")

    def test_el_reclamo_esta_colgado_del_pre_push(self):
        """Es la lección de `EP-002·HU-004`: construido, y nadie lo llamaba."""
        self.assertIn("internas --reclamo", instalar.PLANTILLA_PRE_PUSH,
                      "el reclamo existe pero el enganche no lo llama")

    def test_el_pre_push_no_corre_las_pruebas(self):
        """9,6 minutos por push se apagan en una tarde. **Reclama, no corre.**"""
        sin_reclamo = instalar.PLANTILLA_PRE_PUSH.replace(
            "internas --reclamo", "")
        self.assertNotIn("validar.py internas", sin_reclamo,
                         "el enganche corre las 650: eso es un peaje, no un control")

    # -- Conexión y no regresión -------------------------------------------
    def test_el_subcomando_existe_en_validar(self):
        salida = subprocess.run(
            [sys.executable, os.path.join(self.RAIZ, "validadores", "validar.py"),
             "internas", "--reclamo"],
            capture_output=True, text=True, encoding="utf-8",
            errors="replace", timeout=120)
        self.assertIn(salida.returncode, (0, 1))
        self.assertIn("pruebas del estándar", salida.stdout.lower())

    def test_la_carpeta_de_verdad_es_un_paquete(self):
        """Sin esto, la orden documentada se cae antes de correr nada."""
        self.assertTrue(
            os.path.isfile(os.path.join(self.RAIZ, "validadores", "tests",
                                        "__init__.py")),
            "falta el `__init__.py`: `unittest discover` no puede cargarla")

    def test_la_corrida_de_todos_no_arrastra_las_650(self):
        """`02·F5`: juntarlas daría 13 minutos en cada corrida de rutina.

        No se mira si `pruebas.py` nombra al corredor —esta misma clase lo
        nombra— sino si `internas` está declarado **fuera** de la corrida
        completa, que es lo único que impide que se arrastre.
        """
        import validar
        self.assertIn("internas", validar.FUERA_DE_LA_CORRIDA,
                      "`validar.py todo` arrastraría las 650: son 10 minutos "
                      "en cada corrida de rutina")
        self.assertIn("tarda", validar.FUERA_DE_LA_CORRIDA["internas"],
                      "queda fuera sin decir por qué")


class ElTurnoAnotaLoQueCambio(unittest.TestCase):
    """El registro deja de depender de la herramienta — EP-005 · HU-020.

    **El caso que lo hizo falta:** un commit se llevó 712 líneas ajenas y la
    comprobación de sesiones dijo OK, porque a esos archivos no los había
    registrado ninguna (`S-071`).

    **Lo que más se vigila es que NO reclame de más.** Sin eso, la primera
    sesión del día se atribuye todo lo que esté sucio, y la comprobación pasa
    de callar siempre a hablar siempre — el mismo defecto por el otro extremo.
    """

    RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def _repo(self):
        """Un repositorio de git de verdad: sin él, `git status` no dice nada."""
        if not shutil.which("git"):
            self.skipTest("sin git")
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        raiz = tmp.name
        for orden in (["init", "-q"],
                      ["config", "user.name", "prueba"],
                      ["config", "user.email", "prueba@local"]):
            subprocess.run(["git"] + orden, cwd=raiz, capture_output=True)
        return raiz

    def _escribir(self, raiz, rel, texto, cuando=None):
        ruta = os.path.join(raiz, *rel.split("/"))
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)
        if cuando is not None:
            os.utime(ruta, (cuando, cuando))
        return ruta

    def _registro(self, raiz, sesion):
        ruta = os.path.join(raiz, "historico-chat", ".tocado", sesion + ".txt")
        return sesiones.leer_sesion(ruta)

    # -- CA-01 · lo escrito con un guion queda registrado ------------------
    def test_lo_escrito_sin_las_herramientas_queda_anotado(self):
        raiz = self._repo()
        sesiones.anotar_el_turno(raiz, "s1")          # arranca el reloj
        antes = os.path.getmtime(os.path.join(
            raiz, "historico-chat", ".tocado", "s1.txt"))
        self._escribir(raiz, "del-guion.md", "x\n", cuando=antes + 10)
        sesiones.anotar_el_turno(raiz, "s1")
        self.assertIn("del-guion.md", self._registro(raiz, "s1"),
                      "no anotó lo que escribió un guion")

    def test_un_archivo_nuevo_sin_seguimiento_tambien_se_anota(self):
        """Los dos moldes que causaron el daño eran archivos nuevos."""
        raiz = self._repo()
        sesiones.anotar_el_turno(raiz, "s1")
        reloj = os.path.join(raiz, "historico-chat", ".tocado", "s1.txt")
        self._escribir(raiz, "nuevo.md", "x\n",
                       cuando=os.path.getmtime(reloj) + 10)
        sesiones.anotar_el_turno(raiz, "s1")
        self.assertIn("nuevo.md", self._registro(raiz, "s1"))

    # -- CA-02 · y NO se reclama lo de antes -------------------------------
    #
    # **Es el crítico.** Reclamar lo viejo cambia un silencio inútil por un
    # ruido inútil, y el ruido apaga también lo que servía.

    def test_no_reclama_un_archivo_de_antes_del_turno(self):
        raiz = self._repo()
        sesiones.anotar_el_turno(raiz, "s1")
        reloj = os.path.join(raiz, "historico-chat", ".tocado", "s1.txt")
        self._escribir(raiz, "viejo.md", "x\n",
                       cuando=os.path.getmtime(reloj) - 3600)
        sesiones.anotar_el_turno(raiz, "s1")
        self.assertNotIn("viejo.md", self._registro(raiz, "s1"),
                         "reclamó un archivo modificado antes del turno")

    def test_la_primera_vuelta_no_reclama_el_arbol_entero(self):
        """El caso que se cuela: sin fecha anterior, todo parece del turno."""
        raiz = self._repo()
        for i in range(5):
            self._escribir(raiz, "sucio-%d.md" % i, "x\n")
        anotados = sesiones.anotar_el_turno(raiz, "s1")
        self.assertEqual(anotados, [],
                         "la primera vuelta se llevó el árbol: %s" % anotados)
        self.assertEqual(self._registro(raiz, "s1"), set())

    def test_la_primera_vuelta_deja_el_reloj_puesto(self):
        raiz = self._repo()
        sesiones.anotar_el_turno(raiz, "s1")
        self.assertTrue(os.path.isfile(os.path.join(
            raiz, "historico-chat", ".tocado", "s1.txt")),
            "sin reloj, la vuelta siguiente tampoco anota nada")

    def test_solo_entra_lo_modificado_despues_del_reloj(self):
        raiz = self._repo()
        sesiones.anotar_el_turno(raiz, "s1")
        reloj = os.path.getmtime(os.path.join(
            raiz, "historico-chat", ".tocado", "s1.txt"))
        self._escribir(raiz, "antes.md", "x\n", cuando=reloj - 60)
        self._escribir(raiz, "despues.md", "x\n", cuando=reloj + 60)
        sesiones.anotar_el_turno(raiz, "s1")
        registro = self._registro(raiz, "s1")
        self.assertIn("despues.md", registro)
        self.assertNotIn("antes.md", registro)

    def test_un_borrado_se_anota_aunque_no_tenga_fecha(self):
        """No tiene fecha de modificación: si se filtrara por fecha, se perdería."""
        raiz = self._repo()
        self._escribir(raiz, "condenado.md", "x\n")
        subprocess.run(["git", "add", "-A"], cwd=raiz, capture_output=True)
        subprocess.run(["git", "commit", "-qm", "base"], cwd=raiz,
                       capture_output=True)
        sesiones.anotar_el_turno(raiz, "s1")
        os.remove(os.path.join(raiz, "condenado.md"))
        sesiones.anotar_el_turno(raiz, "s1")
        self.assertIn("condenado.md", self._registro(raiz, "s1"),
                      "el borrado se perdió: dos sesiones que borran lo mismo "
                      "es justo lo que hay que ver")

    # -- CA-03 · dos sesiones producen colisión ----------------------------
    def test_dos_sesiones_con_el_mismo_archivo_avisan(self):
        raiz = self._repo()
        self._escribir(raiz, "compartido.md", "x\n")
        for sesion in ("s1", "s2"):
            sesiones.anotar(raiz, sesion,
                            os.path.join(raiz, "compartido.md"))
        subprocess.run(["git", "add", "compartido.md"], cwd=raiz,
                       capture_output=True)
        hallazgos = sesiones.validar_preparados(raiz)
        self.assertEqual(len(hallazgos), 1, "no vio la colisión")
        self.assertIn("2 sesiones", hallazgos[0].mensaje)

    def test_el_caso_real_una_sesion_escribe_y_otra_commitea(self):
        """Reproduce el daño: una escribe dos archivos, otra los commitea."""
        raiz = self._repo()
        for nombre in ("manual-a.md", "manual-b.md"):
            self._escribir(raiz, nombre, "x\n")
        sesiones.anotar_el_turno(raiz, "otra")
        reloj = os.path.getmtime(os.path.join(
            raiz, "historico-chat", ".tocado", "otra.txt"))
        for nombre in ("manual-a.md", "manual-b.md"):
            self._escribir(raiz, nombre, "cambiado\n", cuando=reloj + 10)
        sesiones.anotar_el_turno(raiz, "otra")          # la otra los anota
        sesiones.anotar_el_turno(raiz, "mia")           # arranca su reloj
        mio = os.path.getmtime(os.path.join(
            raiz, "historico-chat", ".tocado", "mia.txt"))
        self._escribir(raiz, "manual-a.md", "y otra vez\n", cuando=mio + 10)
        sesiones.anotar_el_turno(raiz, "mia")           # y esta también
        subprocess.run(["git", "add", "-A"], cwd=raiz, capture_output=True)
        hallazgos = sesiones.validar_preparados(raiz)
        self.assertEqual(len(hallazgos), 1,
                         "el caso que causó el daño sigue sin verse")

    # -- CA-04 · no se duplica lo que ya estaba ----------------------------
    def test_no_duplica_lo_que_la_herramienta_ya_anoto(self):
        raiz = self._repo()
        sesiones.anotar_el_turno(raiz, "s1")
        reloj = os.path.join(raiz, "historico-chat", ".tocado", "s1.txt")
        ruta = self._escribir(raiz, "doble.md", "x\n",
                              cuando=os.path.getmtime(reloj) + 10)
        sesiones.anotar(raiz, "s1", ruta)               # como la herramienta
        sesiones.anotar_el_turno(raiz, "s1")            # y como el turno
        with io.open(reloj, encoding="utf-8") as f:
            crudo = f.read().split()
        self.assertEqual(crudo.count("doble.md"), 1,
                         "el archivo quedó dos veces en el registro")

    # -- CA-05 · un fallo no rompe el turno --------------------------------
    def test_sin_git_no_revienta_y_no_anota(self):
        """Caso real: una máquina sin git instalado."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.assertEqual(sesiones.cambios_del_turno(tmp.name, 0), [],
                         "afirmó sobre una carpeta que no es un repositorio")

    def test_sin_sesion_no_hace_nada(self):
        raiz = self._repo()
        self.assertEqual(sesiones.anotar_el_turno(raiz, ""), [])
        self.assertFalse(os.path.isdir(
            os.path.join(raiz, "historico-chat", ".tocado")))

    def test_el_enganche_calla_y_sale_bien_con_entrada_rota(self):
        adaptador = os.path.join(os.path.dirname(self.RAIZ), "agente",
                                 "adaptadores", "claude-code")
        guion = os.path.join(adaptador, "hook_turno.py")
        if not os.path.isfile(guion):
            guion = os.path.join(self.RAIZ, "adaptadores", "claude-code",
                                 "hook_turno.py")
        ausente = os.path.join(tempfile.gettempdir(), "cimiento-no-existe")
        shutil.rmtree(ausente, ignore_errors=True)      # que la falta sea de esta vuelta
        for entrada in ("", "no soy json", "[]",
                        json.dumps({"cwd": ausente, "session_id": "s"})):
            salida = subprocess.run(
                [sys.executable, guion], input=entrada, capture_output=True,
                text=True, encoding="utf-8", errors="replace", timeout=60)
            self.assertEqual(salida.returncode, 0,
                             "el enganche murió con %r" % entrada)
            self.assertEqual(salida.stdout.strip(), "",
                             "el enganche habló con %r" % entrada)
        self.assertFalse(os.path.exists(ausente),
                         "el enganche escribió fuera de todo proyecto")

    # -- Conexión y no regresión -------------------------------------------
    def test_el_enganche_esta_registrado_en_el_instalador(self):
        guiones = [h[2] for h in instalar.HOOKS_CLAUDE]
        self.assertIn("hook_turno.py", guiones,
                      "el enganche existe pero nadie lo cuelga")

    def test_validar_preparados_no_cambio_de_firma(self):
        """No se toca la comprobación: se le arregla el registro."""
        self.assertEqual(sesiones.validar_preparados(self._repo()), [])


class ElHashDelCommitSeAnotaSolo(_ProyectoDePrueba):
    """La estación del commit se marca sola — EP-005 · HU-019.

    **Se prueba con repositorios de git de verdad.** Un enganche de git no se
    puede comprobar sin commits reales: probar la función suelta dejaría fuera
    justo lo que falla — que esté colgado, y que un fallo suyo no rompa nada.

    **Lo que más se vigila es que NO escriba.** De los 140 `estado-fase.md` del
    árbol, **106 no tienen la fila** donde marcar (`S-066`): un programa que les
    invente estructura haría más daño que el problema que corrige.
    """

    TABLA = ("# Estado de fase\n\n"
             "| # | Estación | Puerta | Estado |\n|---|---|---|---|\n"
             "| 11 | Cierre | docs al día | OK |\n"
             "| 12 | Commit | autorizado |  |\n"
             "| 13 | Publicación | autorizado |  |\n")
    SIN_FILA = "# Estado de fase\n\nEsta fase no tiene tabla de estaciones.\n"

    # -- La lógica, sin git -----------------------------------------------
    def test_marca_una_fila_vacia(self):
        nuevo = estacion_commit.marcar(self.TABLA, "abc1234")
        self.assertIsNotNone(nuevo)
        self.assertIn("abc1234", nuevo)

    def test_no_inventa_una_fila_donde_no_hay_tabla(self):
        """**El caso crítico.** Son 106 de 140 documentos del árbol."""
        self.assertIsNone(estacion_commit.marcar(self.SIN_FILA, "abc1234"),
                          "inventó estructura en un documento sin tabla")

    def test_no_pisa_un_hash_ya_puesto(self):
        marcada = estacion_commit.marcar(self.TABLA, "primero")
        self.assertIsNone(estacion_commit.marcar(marcada, "segundo"),
                          "pisó el hash que decía qué commit cerró la fase")

    def test_devuelve_nada_cuando_no_hay_que_tocar(self):
        """`None` y no el mismo texto: sin cambio no puede haber escritura."""
        for texto, h in ((self.SIN_FILA, "abc"), (self.TABLA, ""), ("", "abc")):
            self.assertIsNone(estacion_commit.marcar(texto, h))

    def test_solo_cambia_la_fila_doce(self):
        nuevo = estacion_commit.marcar(self.TABLA, "abc1234")
        viejas = [l for l in self.TABLA.splitlines() if not l.startswith("| 12 ")]
        nuevas = [l for l in nuevo.splitlines() if not l.startswith("| 12 ")]
        self.assertEqual(viejas, nuevas, "cambió algo fuera de la fila 12")

    def test_reconoce_la_fase_por_su_forma(self):
        """Por su forma y no por una lista: sirve en cualquier proyecto."""
        self.assertEqual(
            estacion_commit.fase_de(
                "documentacion/epicas/EP-001-e/HU-001-u/A-EP-001-HU-001-x/x.md"),
            "documentacion/epicas/EP-001-e/HU-001-u/A-EP-001-HU-001-x")
        self.assertEqual(estacion_commit.fase_de("validadores/fases.py"), "")

    # -- Con git de verdad -------------------------------------------------
    def _repo_con_enganche(self):
        """Un repositorio de git real, con el enganche colgado."""
        if not shutil.which("git"):
            self.skipTest("sin git")
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        raiz = tmp.name
        for orden in (["init", "-q"],
                      ["config", "user.name", "prueba"],
                      ["config", "user.email", "prueba@local"],
                      ["config", "core.hooksPath", ".githooks"]):
            subprocess.run(["git"] + orden, cwd=raiz, capture_output=True)
        ganchos = os.path.join(raiz, ".githooks")
        os.makedirs(ganchos)
        guion = os.path.join(self.VALIDADORES, "hook_estacion.py")
        archivo = os.path.join(ganchos, "post-commit")
        with io.open(archivo, "w", encoding="utf-8", newline="\n") as f:
            f.write('#!/bin/sh\npython "%s" --raiz "$(pwd)" || true\nexit 0\n'
                    % guion.replace("\\", "/"))
        os.chmod(archivo, 0o755)
        return raiz

    def _fase(self, raiz, nombre, estado, con_cierre=True):
        carpeta = os.path.join(raiz, "documentacion", "epicas", "EP-001-e",
                               "HU-001-una", nombre)
        os.makedirs(carpeta, exist_ok=True)
        with io.open(os.path.join(carpeta, "estado-fase.md"), "w",
                     encoding="utf-8", newline="\n") as f:
            f.write(estado)
        if con_cierre:
            with io.open(os.path.join(carpeta, "funcionalidad_implementada.md"),
                         "w", encoding="utf-8", newline="\n") as f:
                f.write("# cierre escrito\n")
        return carpeta

    def _commit(self, raiz, mensaje):
        subprocess.run(["git", "add", "-A"], cwd=raiz, capture_output=True)
        r = subprocess.run(["git", "commit", "-m", mensaje], cwd=raiz,
                           capture_output=True, text=True, encoding="utf-8",
                           errors="replace")
        h = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=raiz,
                           capture_output=True, text=True, encoding="utf-8",
                           errors="replace").stdout.strip()
        return r, h

    def _texto(self, carpeta):
        with io.open(os.path.join(carpeta, "estado-fase.md"),
                     encoding="utf-8") as f:
            return f.read()

    def test_al_commitear_el_hash_queda_escrito(self):
        raiz = self._repo_con_enganche()
        carpeta = self._fase(raiz, "A-EP-001-HU-001-con-fila", self.TABLA)
        r, h = self._commit(raiz, "primero")
        self.assertEqual(r.returncode, 0)
        self.assertIn(h, self._texto(carpeta),
                      "el enganche no escribió el hash al commitear")

    def test_al_commitear_no_se_toca_la_fase_sin_fila(self):
        raiz = self._repo_con_enganche()
        carpeta = self._fase(raiz, "B-EP-001-HU-001-sin-fila", self.SIN_FILA)
        self._commit(raiz, "primero")
        self.assertEqual(self._texto(carpeta), self.SIN_FILA,
                         "tocó un documento sin la fila de la estación 12")

    def test_al_commitear_no_se_pisa_el_hash_anterior(self):
        raiz = self._repo_con_enganche()
        carpeta = self._fase(raiz, "A-EP-001-HU-001-con-fila", self.TABLA)
        _, primero = self._commit(raiz, "primero")
        _, segundo = self._commit(raiz, "segundo")
        texto = self._texto(carpeta)
        self.assertIn(primero, texto)
        self.assertNotIn(segundo, texto, "el segundo commit pisó al primero")

    def test_una_fase_sin_cierre_escrito_no_se_marca(self):
        """Marcarla diría que se commiteó algo que no se commiteó."""
        raiz = self._repo_con_enganche()
        carpeta = self._fase(raiz, "A-EP-001-HU-001-sin-cierre", self.TABLA,
                             con_cierre=False)
        _, h = self._commit(raiz, "primero")
        self.assertNotIn(h, self._texto(carpeta))

    def test_un_enganche_roto_no_rompe_el_commit(self):
        """**De no destruir.** Un commit perdido no se recupera con un aviso."""
        raiz = self._repo_con_enganche()
        self._fase(raiz, "A-EP-001-HU-001-con-fila", self.TABLA)
        gancho = os.path.join(raiz, ".githooks", "post-commit")
        with io.open(gancho, "w", encoding="utf-8", newline="\n") as f:
            f.write('#!/bin/sh\npython "no-existe.py" || true\nexit 0\n')
        os.chmod(gancho, 0o755)
        r, _ = self._commit(raiz, "con el enganche roto")
        self.assertEqual(r.returncode, 0, "el enganche roto tumbó el commit")
        log = subprocess.run(["git", "log", "--oneline"], cwd=raiz,
                             capture_output=True, text=True, encoding="utf-8",
                             errors="replace").stdout
        self.assertIn("con el enganche roto", log, "el commit se perdió")

    def test_el_enganche_no_revienta_si_no_hay_git(self):
        """**Lo pidió un sabotaje que pasó en verde**, y es un caso real.

        La prueba anterior rompía el *guion de shell* que llama al enganche, no
        el enganche: su red de seguridad nunca se tocaba. Acá se corre
        `hook_estacion.py` **sin `git` en el camino**, que es lo que pasa en una
        máquina que no lo tiene instalado: sin la red, revienta con traza y
        código 1 justo después de un commit correcto.
        """
        guion = os.path.join(self.VALIDADORES, "hook_estacion.py")
        entorno = {"SYSTEMROOT": os.environ.get("SYSTEMROOT", ""),
                   "PATH": "", "PATHEXT": os.environ.get("PATHEXT", "")}
        salida = subprocess.run(
            [sys.executable, guion, "--raiz", os.path.dirname(self.VALIDADORES)],
            capture_output=True, text=True, encoding="utf-8",
            errors="replace", env=entorno, timeout=60)
        self.assertEqual(salida.returncode, 0,
                         "el enganche murió sin git: %s" % salida.stderr[:200])
        self.assertEqual(salida.stderr.strip(), "",
                         "el enganche alarmó después de un commit correcto")

    # -- El conteo, con sus tres grupos ------------------------------------
    def test_el_conteo_separa_los_tres_grupos(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        raiz = tmp.name
        self._fase(raiz, "A-EP-001-HU-001-solo-marca", self.TABLA)
        self._fase(raiz, "B-EP-001-HU-001-sin-cierre", self.TABLA,
                   con_cierre=False)
        self._fase(raiz, "C-EP-001-HU-001-sin-fila", self.SIN_FILA)
        mensajes = [h.mensaje for h in
                    fases.estacion_del_commit_sin_marcar(raiz)]
        self.assertEqual(len(mensajes), 3, "no salieron los tres grupos")
        self.assertTrue(any("es la marca, no el trabajo" in m for m in mensajes))
        self.assertTrue(any("esto sí es trabajo" in m for m in mensajes))
        self.assertTrue(any("sin la fila" in m for m in mensajes))

    def test_el_conteo_dice_cuales_y_no_solo_cuantas(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self._fase(tmp.name, "A-EP-001-HU-001-solo-marca", self.TABLA)
        mensajes = [h.mensaje for h in
                    fases.estacion_del_commit_sin_marcar(tmp.name)]
        self.assertTrue(
            any("A-EP-001-HU-001-solo-marca" in m for m in mensajes),
            "el conteo dice cuántas pero no cuáles")

    def test_el_conteo_llega_por_validar(self):
        raiz = os.path.dirname(self.VALIDADORES)
        mensajes = [h.mensaje for h in fases.validar(raiz)]
        self.assertTrue(any("estación 12" in m for m in mensajes),
                        "el conteo no llega por `validar`")

    def test_el_enganche_esta_registrado_en_el_instalador(self):
        """Construido y no colgado no sirve de nada — `EP-002·HU-004`."""
        nombres = [h[0] for h in instalar.HOOKS]
        self.assertIn("post-commit", nombres,
                      "el enganche existe pero el instalador no lo escribe")


class UnRojoSeCierraDeclarandolo(unittest.TestCase):
    """Un veredicto en rojo se puede cerrar — EP-004 · HU-023.

    **Comprobado haciéndolo:** dos fases verificaron criterios en rojo,
    midieron que hoy se cumplen y cerraron con «Cumple», **y el número no se
    movió**. Un rojo entraba en la cuenta y no salía nunca (`S-065`).

    **Lo que se vigila no es que cierre: es que NO cierre solo.** De las 16
    historias con un rojo, ocho tienen fase posterior y **solo dos volvieron a
    verificar**. Deducir el reemplazo del orden daría por cumplidas las otras
    seis — la mentira optimista que esta cuenta vino a impedir.
    """

    RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CINCO = ["plan_trabajo.md", "plan_pruebas.md", "resultado_pruebas.md",
             "estado-fase.md", "funcionalidad_implementada.md"]

    def _arbol(self, fases_y_datos, hu="HU-001-una"):
        """`{"A-EP-001-HU-001-x": ("Cumple", "nombre que reemplaza o None")}`."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        base = os.path.join(tmp.name, "documentacion", "epicas", "EP-001-e", hu)
        for nombre, (veredicto, reemplaza) in fases_y_datos.items():
            carpeta = os.path.join(base, nombre)
            os.makedirs(carpeta)
            for doc in self.CINCO:
                cuerpo = "# de mentira\n"
                if doc == "resultado_pruebas.md" and veredicto:
                    cuerpo += "\n**Concepto:** %s.\n" % veredicto
                if doc == "funcionalidad_implementada.md" and reemplaza is not None:
                    cuerpo += ("\n| **Reemplaza el veredicto de** | `%s` |\n"
                               % reemplaza)
                with io.open(os.path.join(carpeta, doc), "w",
                             encoding="utf-8", newline="\n") as f:
                    f.write(cuerpo)
        return tmp.name

    # -- CA-01 · declarar cierra el rojo ----------------------------------
    def test_sin_el_campo_el_rojo_sigue_contando(self):
        raiz = self._arbol({"A-EP-001-HU-001-x": ("No cumple", None),
                            "B-EP-001-HU-001-y": ("Cumple", None)})
        self.assertEqual(fases.por_veredicto(raiz), (0, 1, 0))

    def test_con_el_campo_el_rojo_se_cierra(self):
        raiz = self._arbol({"A-EP-001-HU-001-x": ("No cumple", None),
                            "B-EP-001-HU-001-y": ("Cumple", "A-EP-001-HU-001-x")})
        self.assertEqual(fases.por_veredicto(raiz), (1, 0, 0),
                         "declarar el reemplazo no cerró el rojo")

    def test_quitar_el_campo_lo_devuelve_a_rojo(self):
        """Que el cambio lo produzca el campo, y no otra cosa que se movió."""
        raiz = self._arbol({"A-EP-001-HU-001-x": ("No cumple", None),
                            "B-EP-001-HU-001-y": ("Cumple", "A-EP-001-HU-001-x")})
        self.assertEqual(fases.por_veredicto(raiz)[0], 1)
        cierre = os.path.join(raiz, "documentacion", "epicas", "EP-001-e",
                              "HU-001-una", "B-EP-001-HU-001-y",
                              "funcionalidad_implementada.md")
        with io.open(cierre, "w", encoding="utf-8", newline="\n") as f:
            f.write("# de mentira\n")
        self.assertEqual(fases.por_veredicto(raiz), (0, 1, 0))

    # -- CA-02 · un rojo no cierra otro rojo ------------------------------
    #
    # **Estas tres se comprueban sobre el CONJUNTO de reemplazos, no sobre la
    # cuenta.** Ahí es donde actúan las guardias: quitar cualquiera de las tres
    # deja la cuenta igual en estos árboles —el rojo de quien declara ya la
    # ensucia— y una prueba que mirara la cuenta **no podría fallar**. Lo
    # destaparon tres sabotajes que pasaron en verde.

    def _fases_de(self, raiz, hu="HU-001-una"):
        base = os.path.join(raiz, "documentacion", "epicas", "EP-001-e", hu)
        return base, sorted(fases._subcarpetas(base))

    def test_una_fase_en_rojo_no_entra_al_conjunto_de_reemplazos(self):
        raiz = self._arbol({"A-EP-001-HU-001-x": ("No cumple", None),
                            "B-EP-001-HU-001-y": ("No cumple", "A-EP-001-HU-001-x")})
        base, fs = self._fases_de(raiz)
        self.assertEqual(fases.veredictos_reemplazados(base, fs), set(),
                         "un rojo cerró otro rojo")
        self.assertEqual(fases.por_veredicto(raiz), (0, 1, 0))

    def test_una_fase_sin_veredicto_no_entra_al_conjunto(self):
        raiz = self._arbol({"A-EP-001-HU-001-x": ("No cumple", None),
                            "B-EP-001-HU-001-y": (None, "A-EP-001-HU-001-x")})
        base, fs = self._fases_de(raiz)
        self.assertEqual(fases.veredictos_reemplazados(base, fs), set())
        self.assertEqual(fases.por_veredicto(raiz), (0, 0, 1))

    def test_el_rojo_que_declara_tambien_se_avisa(self):
        raiz = self._arbol({"A-EP-001-HU-001-x": ("No cumple", None),
                            "B-EP-001-HU-001-y": ("No cumple", "A-EP-001-HU-001-x")})
        avisos = fases.reemplazos_que_no_resuelven(raiz)
        self.assertEqual(len(avisos), 1)
        self.assertIn("un rojo no cierra", avisos[0].mensaje)

    # -- CA-03 · no se deduce del orden -----------------------------------
    #
    # **Es el caso que decide si esta fase sirve.** Medido: de las ocho
    # historias con fase posterior, seis no resolvieron el rojo.

    def test_tres_fases_sin_el_campo_siguen_sin_cumplir(self):
        raiz = self._arbol({"A-EP-001-HU-001-x": ("No cumple", None),
                            "B-EP-001-HU-001-y": ("Cumple", None),
                            "C-EP-001-HU-001-z": ("Cumple", None)})
        self.assertEqual(fases.por_veredicto(raiz), (0, 1, 0),
                         "el reemplazo se dedujo del orden de las fases")

    def test_en_el_arbol_real_solo_cierra_lo_declarado(self):
        """Contra el repositorio: ninguna historia se cierra sin declararlo.

        Se cuentan las historias con un rojo cuya última fase **no** declara
        nada, y se comprueba que siguen entre las que no cumplen.
        """
        raiz = os.path.join(self.RAIZ, "documentacion", "epicas")
        if not os.path.isdir(raiz):
            self.skipTest("sin árbol real")
        de_cada_uno = fases.marcadores_de_los_moldes(self.RAIZ)
        sin_declarar = 0
        for ep in fases._subcarpetas(raiz):
            if not fases._EPICA.match(ep):
                continue
            for hu in fases._subcarpetas(os.path.join(raiz, ep)):
                if not fases._HU.match(hu):
                    continue
                rhu = os.path.join(raiz, ep, hu)
                fs = [n for n in fases._subcarpetas(rhu) if fases._FASE.match(n)]
                if not fases._historia_terminada(rhu, de_cada_uno):
                    continue
                rojas = [f for f in fs
                         if fases.veredicto_de(os.path.join(rhu, f)) == "No cumple"]
                if rojas and not fases.veredictos_reemplazados(rhu, fs):
                    sin_declarar += 1
        _, no_cumplen, _ = fases.por_veredicto(self.RAIZ)
        self.assertEqual(sin_declarar, no_cumplen,
                         "hay historias con un rojo que salieron de la cuenta "
                         "sin declarar el reemplazo")

    # -- CA-04 · un nombre que no resuelve avisa y no reemplaza -----------
    def test_una_fase_que_cumple_no_se_cierra_a_si_misma(self):
        """**En verde**, que es donde la guardia actúa.

        Con la fase en rojo, la condición de que quien declara cumpla ya la
        bloquea, y la prueba pasaba sin tocar esta guardia.
        """
        raiz = self._arbol({"A-EP-001-HU-001-x": ("Cumple",
                                                  "A-EP-001-HU-001-x")})
        base, fs = self._fases_de(raiz)
        self.assertEqual(fases.veredictos_reemplazados(base, fs), set(),
                         "una fase se cerró a sí misma")

    def test_la_fase_que_se_nombra_a_si_misma_se_avisa(self):
        raiz = self._arbol({"A-EP-001-HU-001-x": ("Cumple",
                                                  "A-EP-001-HU-001-x")})
        avisos = fases.reemplazos_que_no_resuelven(raiz)
        self.assertEqual(len(avisos), 1)
        self.assertIn("se nombra a sí misma", avisos[0].mensaje)

    def test_nombrar_una_fase_de_otra_historia_no_entra_al_conjunto(self):
        raiz = self._arbol({"A-EP-001-HU-001-x": ("No cumple", None),
                            "B-EP-001-HU-001-y": ("Cumple", "A-EP-009-HU-009-ajena")})
        base, fs = self._fases_de(raiz)
        self.assertEqual(fases.veredictos_reemplazados(base, fs), set(),
                         "se aceptó el nombre de una fase de otra historia")
        self.assertEqual(fases.por_veredicto(raiz), (0, 1, 0))

    def test_nombrar_una_fase_que_no_existe_no_reemplaza(self):
        raiz = self._arbol({"A-EP-001-HU-001-x": ("No cumple", None),
                            "B-EP-001-HU-001-y": ("Cumple", "Z-EP-001-HU-001-nada")})
        base, fs = self._fases_de(raiz)
        self.assertEqual(fases.veredictos_reemplazados(base, fs), set())
        self.assertEqual(fases.por_veredicto(raiz), (0, 1, 0))

    def test_el_campo_vacio_no_reemplaza_ni_revienta(self):
        raiz = self._arbol({"A-EP-001-HU-001-x": ("No cumple", None),
                            "B-EP-001-HU-001-y": ("Cumple", "")})
        self.assertEqual(fases.por_veredicto(raiz), (0, 1, 0))

    def test_el_aviso_dice_el_nombre_escrito_y_el_motivo(self):
        raiz = self._arbol({"A-EP-001-HU-001-x": ("No cumple", None),
                            "B-EP-001-HU-001-y": ("Cumple", "Z-EP-001-HU-001-nada")})
        avisos = fases.reemplazos_que_no_resuelven(raiz)
        self.assertEqual(len(avisos), 1)
        self.assertIn("Z-EP-001-HU-001-nada", avisos[0].mensaje,
                      "el aviso no dice qué nombre se escribió")
        self.assertIn("no está en esta historia", avisos[0].mensaje)

    def test_el_aviso_llega_por_validar_no_solo_por_la_funcion(self):
        raiz = self._arbol({"A-EP-001-HU-001-x": ("No cumple", None),
                            "B-EP-001-HU-001-y": ("Cumple", "Z-EP-001-HU-001-nada")})
        mensajes = [h.mensaje for h in fases.validar(raiz)]
        self.assertTrue(any("declara reemplazar" in m for m in mensajes),
                        "el aviso no llega por `validar`")

    # -- CA-05 · el veredicto reemplazado no se borra ---------------------
    def test_el_veredicto_reemplazado_sigue_diciendo_lo_que_decia(self):
        """La cuenta lo ignora; el dato no desaparece."""
        raiz = self._arbol({"A-EP-001-HU-001-x": ("No cumple", None),
                            "B-EP-001-HU-001-y": ("Cumple", "A-EP-001-HU-001-x")})
        vieja = os.path.join(raiz, "documentacion", "epicas", "EP-001-e",
                             "HU-001-una", "A-EP-001-HU-001-x")
        antes = comun.leer(os.path.join(vieja, "resultado_pruebas.md"))
        fases.validar(raiz)
        self.assertEqual(comun.leer(os.path.join(vieja, "resultado_pruebas.md")),
                         antes)
        self.assertEqual(fases.veredicto_de(vieja), "No cumple",
                         "el veredicto reemplazado dejó de leerse")

    # -- Transversal · no regresión ---------------------------------------
    def test_por_veredicto_sigue_devolviendo_tres_valores(self):
        self.assertEqual(len(fases.por_veredicto(self.RAIZ)), 3)

    def test_el_molde_del_cierre_trae_el_campo_como_opcional(self):
        texto = comun.leer(os.path.join(
            self.RAIZ, "plantillas", "ciclo-vida-proyectos",
            "11-funcionalidad-implementada.md"))
        campo = [l for l in texto.split("\n")
                 if l.startswith("| **Reemplaza el veredicto de**")]
        self.assertEqual(len(campo), 1, "el molde no trae el campo")
        self.assertIn("Opcional", campo[0],
                      "el campo no se declara opcional, y obligaría a 130 fases")


class ElMoldeSinLlenarNoCuenta(unittest.TestCase):
    """Un documento que sigue siendo su plantilla — EP-004 · HU-022.

    El andamio crea los cinco documentos vacíos al abrir una fase, así que
    hasta la 35.2.0 **una fase recién abierta ya contaba como terminada**.
    Cobró cuatro veces el 2026-08-27, dos de ellas moviendo una medición en
    curso.

    **Lo que se vigila no es que señale el molde: es que NO señale la prosa.**
    Una primera medida contó los marcadores con un umbral y marcó tres
    documentos escritos, cerrados y publicados el mismo día — este repositorio
    usa comillas angulares en su prosa todo el tiempo (`S-059`).
    """

    RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CINCO = ["plan_trabajo.md", "plan_pruebas.md", "resultado_pruebas.md",
             "estado-fase.md", "funcionalidad_implementada.md"]

    def _texto(self, ruta):
        with io.open(ruta, encoding="utf-8") as f:
            return f.read()

    def _escribir(self, ruta, texto):
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)

    def _molde(self, raiz, nombre):
        return self._texto(os.path.join(
            raiz, *fases.MOLDES_DEL_CICLO.split("/"), nombre))

    def _proyecto(self, cuerpos, plantillas=None):
        """Un árbol con una fase, y **sus propias plantillas**.

        Llevar plantillas propias es lo que permite probar `CA-04` sin tocar
        las de verdad.
        """
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)

        moldes = os.path.join(tmp.name, *fases.MOLDES_DEL_CICLO.split("/"))
        os.makedirs(moldes)
        if plantillas is None:
            plantillas = {d: "# molde\n\n| Campo | Valor |\n|---|---|\n"
                             "| Fase | «A-EP01-HU03-Descripción» |\n"
                             "| Módulo | «M» |\n| Fecha | AAAA-MM-DD |\n"
                          for d in self.CINCO}
        for documento, texto in plantillas.items():
            with io.open(os.path.join(moldes, fases.DE_QUE_MOLDE[documento]),
                         "w", encoding="utf-8", newline="\n") as f:
                f.write(texto)

        fase = os.path.join(tmp.name, "documentacion", "epicas", "EP-001-e",
                            "HU-001-una", "A-EP-001-HU-001-x")
        os.makedirs(fase)
        for documento in self.CINCO:
            with io.open(os.path.join(fase, documento), "w",
                         encoding="utf-8", newline="\n") as f:
                f.write(cuerpos.get(documento, "# escrito\n\nProsa real.\n"))
        return tmp.name, fase

    # -- CA-01 · la fase con un documento sin llenar no cuenta terminada ---
    def test_con_los_cinco_escritos_cuenta_terminada(self):
        raiz, _ = self._proyecto({})
        self.assertEqual(fases.inventario(raiz), (1, 1, 0))

    def test_un_documento_que_es_el_molde_la_saca_de_terminadas(self):
        raiz, fase = self._proyecto({})
        molde = self._molde(raiz, "08-plan-pruebas.md")
        with io.open(os.path.join(fase, "plan_pruebas.md"), "w",
                     encoding="utf-8", newline="\n") as f:
            f.write(molde)
        self.assertEqual(fases.inventario(raiz), (1, 0, 1),
                         "un molde sin llenar siguió contando como escrito")

    def test_volver_a_escribirlo_la_devuelve_a_terminadas(self):
        raiz, fase = self._proyecto({})
        ruta = os.path.join(fase, "plan_pruebas.md")
        molde = self._molde(raiz, "08-plan-pruebas.md")
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(molde)
        self.assertEqual(fases.inventario(raiz)[1], 0)
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write("# escrito de verdad\n")
        self.assertEqual(fases.inventario(raiz)[1], 1)

    def test_la_historia_sin_terminar_sale_del_reparto_de_veredictos(self):
        """`por_veredicto` solo mira las terminadas: si deja de estarlo, sale.

        Lo contrario la dejaría en «no dice si cumple», que es afirmar sobre
        una historia que ni siquiera está terminada.
        """
        raiz, fase = self._proyecto(
            {"resultado_pruebas.md": "## 5. Veredicto\n\n**Cumple.**\n"})
        self.assertEqual(fases.por_veredicto(raiz), (1, 0, 0))
        molde = self._molde(raiz, "10-estado-fase.md")
        with io.open(os.path.join(fase, "estado-fase.md"), "w",
                     encoding="utf-8", newline="\n") as f:
            f.write(molde)
        self.assertEqual(fases.por_veredicto(raiz), (0, 0, 0),
                         "una historia sin terminar entró al reparto")

    # -- CA-02 · y NO se señala un documento escrito -----------------------
    #
    # **Es el caso crítico.** La medida anterior —contar marcadores con un
    # umbral— señaló tres documentos escritos el mismo día en que se
    # escribieron, porque esta casa usa comillas angulares en su prosa.

    def _marcadores_del_molde_de(self, documento):
        return fases.marcadores_de_los_moldes(self.RAIZ)[documento]

    def test_no_señala_la_prosa_con_muchas_comillas(self):
        cuerpo = ("# resultado\n\nSe decidió entre «Cumple» y «No cumple», "
                  "y el «Veredicto por criterio de aceptación» quedó aparte. "
                  "Las palabras «terminada», «cumplida», «propuesta», "
                  "«aprobada», «lista», «en curso», «en prueba», «bloqueada» "
                  "y «cancelada» son el vocabulario.\n")
        raiz, _ = self._proyecto({"resultado_pruebas.md": cuerpo})
        self.assertEqual(fases.inventario(raiz), (1, 1, 0),
                         "señaló prosa por tener comillas angulares")

    def test_no_señala_los_documentos_reales_que_la_medida_vieja_marco(self):
        """Los tres de `C-EP-004-HU-021`, escritos y publicados el mismo día."""
        fase = os.path.join(
            self.RAIZ, "documentacion", "epicas", "EP-004-comprobacion-automatica",
            "HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido",
            "C-EP-004-HU-021-cualquier-encabezado-de-veredicto-se-lee")
        if not os.path.isdir(fase):
            self.skipTest("la fase C de la HU-021 no está en este árbol")
        de_cada_uno = fases.marcadores_de_los_moldes(self.RAIZ)
        self.assertEqual(fases.moldes_sin_llenar(fase, de_cada_uno), [],
                         "señaló documentos escritos de la fase C")

    def test_señala_un_documento_que_es_la_plantilla_real(self):
        """La plantilla de verdad, copiada tal cual, tiene que señalarse.

        **Antes esta prueba apuntaba a un `plan_pruebas.md` real** que seguía
        siendo el molde. Se escribió el 2026-08-27 —que era el objetivo— y la
        prueba se cayó sola. **Una prueba que se rompe cuando el repositorio
        mejora está atada al síntoma, no a la regla**: ahora copia la plantilla
        a un árbol de mentira, que es lo que no cambia.
        """
        raiz, fase = self._proyecto({})
        molde = os.path.join(self.RAIZ, "plantillas", "ciclo-vida-proyectos",
                             "08-plan-pruebas.md")
        if not os.path.isfile(molde):
            self.skipTest("no está la plantilla en este árbol")
        with io.open(molde, encoding="utf-8") as f:
            texto = f.read()
        self._escribir(os.path.join(fase, "plan_pruebas.md"), texto)
        de_cada_uno = fases.marcadores_de_los_moldes(self.RAIZ)
        señalados = dict(fases.moldes_sin_llenar(fase, de_cada_uno))
        self.assertIn("plan_pruebas.md", señalados,
                      "no reconoció la plantilla real copiada tal cual")

    def test_dos_marcadores_del_molde_no_alcanzan(self):
        """El corte es tres, y el reparto real no tiene nada entre 3 y 15."""
        raiz, fase = self._proyecto({})
        propios = sorted(fases.marcadores_de_los_moldes(raiz)["plan_trabajo.md"])
        with io.open(os.path.join(fase, "plan_trabajo.md"), "w",
                     encoding="utf-8", newline="\n") as f:
            f.write("# escrito\n\n%s y %s.\n" % (propios[0], propios[1]))
        self.assertEqual(fases.inventario(raiz), (1, 1, 0))

    # -- CA-03 · el aviso dice cuáles -------------------------------------
    def test_el_aviso_nombra_el_documento_y_un_marcador(self):
        raiz, fase = self._proyecto({})
        molde = self._molde(raiz, "08-plan-pruebas.md")
        with io.open(os.path.join(fase, "plan_pruebas.md"), "w",
                     encoding="utf-8", newline="\n") as f:
            f.write(molde)
        avisos = fases.documentos_que_siguen_siendo_el_molde(raiz)
        self.assertEqual(len(avisos), 1)
        self.assertIn("plan_pruebas.md", avisos[0].archivo)
        # **Lo pidió un sabotaje que pasó en verde.** La comprobación de
        # antes era `assertIn("«", mensaje + "«")`, que es cierta siempre:
        # se compara contra un texto al que se le acaba de pegar lo buscado.
        # Se exige un marcador **de los que el documento conserva de verdad**.
        propios = fases.marcadores_de_los_moldes(raiz)["plan_pruebas.md"]
        self.assertTrue(
            any(m in avisos[0].mensaje for m in propios),
            "el aviso dice cuántos pero no cuál: %s" % avisos[0].mensaje)

    def test_el_aviso_llega_por_validar_no_solo_por_la_funcion(self):
        """Una comprobación bien escrita y desconectada deja todo en verde."""
        raiz, fase = self._proyecto({})
        molde = self._molde(raiz, "08-plan-pruebas.md")
        with io.open(os.path.join(fase, "plan_pruebas.md"), "w",
                     encoding="utf-8", newline="\n") as f:
            f.write(molde)
        mensajes = [h.mensaje for h in fases.validar(raiz)]
        self.assertTrue(any("sigue siendo la plantilla" in m for m in mensajes),
                        "el aviso no llega por `validar`")

    # -- CA-04 · las plantillas se leen del repositorio --------------------
    def test_un_marcador_nuevo_en_la_plantilla_se_reconoce_solo(self):
        raiz, fase = self._proyecto({})
        molde = os.path.join(raiz, *fases.MOLDES_DEL_CICLO.split("/"),
                             "07-plan-trabajo.md")
        with io.open(molde, "a", encoding="utf-8", newline="\n") as f:
            f.write("\n«un marcador que nadie había visto»\n"
                    "«ni este tampoco»\n«ni este otro»\n")
        with io.open(os.path.join(fase, "plan_trabajo.md"), "w",
                     encoding="utf-8", newline="\n") as f:
            f.write("«un marcador que nadie había visto»\n"
                    "«ni este tampoco»\n«ni este otro»\n")
        self.assertEqual(fases.inventario(raiz), (1, 0, 1),
                         "no leyó los marcadores nuevos de la plantilla")

    def test_sin_plantilla_no_se_afirma_nada_de_ese_documento(self):
        """`04·R4`: sin con qué comparar, no se afirma. Y no revienta."""
        raiz, fase = self._proyecto({})
        os.remove(os.path.join(raiz, *fases.MOLDES_DEL_CICLO.split("/"),
                               "08-plan-pruebas.md"))
        with io.open(os.path.join(fase, "plan_pruebas.md"), "w",
                     encoding="utf-8", newline="\n") as f:
            f.write("| Fase | «A-EP01-HU03-Descripción» |\n| Módulo | «M» |\n"
                    "| Fecha | AAAA-MM-DD |\n")
        self.assertEqual(fases.inventario(raiz), (1, 1, 0))

    def test_sin_ninguna_plantilla_no_queda_ninguna_lista_de_reserva(self):
        """Que no haya marcadores copiados en el código, comprobado corriendo.

        Buscar el texto en `fases.py` no sirve: los comentarios citan
        marcadores para explicarse, y una prueba así se rompe al documentar
        —pasó en la primera corrida—. **Se comprueba por comportamiento:**
        sin ninguna plantilla no puede quedar nada con qué comparar.
        """
        raiz, fase = self._proyecto({})
        moldes = os.path.join(raiz, *fases.MOLDES_DEL_CICLO.split("/"))
        for nombre in os.listdir(moldes):
            os.remove(os.path.join(moldes, nombre))
        self.assertEqual(fases.marcadores_de_los_moldes(raiz), {},
                         "quedaron marcadores que no salieron de una plantilla")
        self._escribir(os.path.join(fase, "plan_pruebas.md"),
                       "| Fase | «A-EP01-HU03-Descripción» |\n"
                       "| Módulo | «M» |\n| Fecha | AAAA-MM-DD |\n")
        self.assertEqual(fases.inventario(raiz), (1, 1, 0))
        self.assertEqual(fases.documentos_que_siguen_siendo_el_molde(raiz), [])

    # -- CA-05 · avisa y no corrige ---------------------------------------
    def test_la_comprobacion_no_escribe_en_el_documento(self):
        raiz, fase = self._proyecto({})
        ruta = os.path.join(fase, "plan_pruebas.md")
        molde = self._molde(raiz, "08-plan-pruebas.md")
        with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(molde)
        antes = self._texto(ruta)
        fases.validar(raiz)
        self.assertEqual(self._texto(ruta), antes)

    # -- Transversal · no regresión ---------------------------------------
    def test_inventario_sigue_devolviendo_tres_valores(self):
        self.assertEqual(len(fases.inventario(self.RAIZ)), 3)

    def test_un_documento_que_falta_sigue_contando_como_falta(self):
        """Lo de antes no se reemplaza: se le suma."""
        raiz, fase = self._proyecto({})
        os.remove(os.path.join(fase, "plan_pruebas.md"))
        self.assertEqual(fases.inventario(raiz), (1, 0, 1))


class VocabularioDeEstados(unittest.TestCase):
    """El estado se escribe con una palabra del glosario — EP-003 · HU-012.

    Lo que se vigila no es que la comprobación funcione: es **de dónde saca el
    vocabulario**. Hasta la 34.2.0 cada molde traía su propia lista, y así se
    llegó a cuatro listas, tres palabras para «terminado», y 111 de 115
    historias fuera del vocabulario de su propio molde. Una lista escrita en el
    código sería la quinta.
    """

    RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def _arbol(self, estado, nombre="HU-001-una"):
        """Un proyecto con una historia que declara `estado`.

        Si `estado` es `None`, la historia no trae el campo.
        """
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        carpeta = os.path.join(tmp.name, "documentacion", "epicas",
                               "EP-001-e", nombre)
        os.makedirs(carpeta)
        fila = "" if estado is None else "| **Estado** | %s |\n" % estado
        with io.open(os.path.join(carpeta, "%s.md" % nombre), "w",
                     encoding="utf-8", newline="\n") as f:
            f.write("# %s\n\n| Campo | Valor |\n|---|---|\n%s" % (nombre, fila))
        return tmp.name

    def _avisos(self, estado, **kw):
        return [h.mensaje for h in
                fases.estado_fuera_del_vocabulario(self._arbol(estado, **kw))]

    # -- CA-01 · el vocabulario sale del glosario -------------------------
    def test_el_vocabulario_lo_da_el_glosario_y_no_el_codigo(self):
        vocab = fases.vocabulario_de_estados()
        self.assertIn("Historia de usuario", vocab)
        self.assertIn("Épica", vocab)
        self.assertIn("Tarea", vocab)

    def test_terminada_es_la_misma_palabra_en_los_tres_conjuntos(self):
        """El corazón de la historia: mismo concepto, misma palabra."""
        vocab = fases.vocabulario_de_estados()
        for quien in ("Épica", "Historia de usuario", "Tarea"):
            self.assertIn("Terminada", vocab[quien],
                          "«%s» no usa la misma palabra que las otras" % quien)

    def test_cambiar_el_glosario_cambia_que_acepta(self):
        """Si el vocabulario viviera en el código, esto pasaría igual.

        Es la prueba que impide que vuelvan las dos copias, que es el problema
        entero de esta fase.
        """
        raiz = self._arbol("Terminada")
        self.assertEqual(fases.estado_fuera_del_vocabulario(raiz), [])

        with io.open(fases.GLOSARIO, "rb") as f:
            copia = f.read()

        def restaurar():
            with io.open(fases.GLOSARIO, "wb") as g:
                g.write(copia)

        self.addCleanup(restaurar)
        texto = copia.decode("utf-8").replace(
            "| **Historia de usuario** | Pendiente · Lista · En curso · "
            "En prueba · Terminada |",
            "| **Historia de usuario** | Pendiente · En curso |", 1)
        with io.open(fases.GLOSARIO, "w", encoding="utf-8",
                     newline="\n") as f:
            f.write(texto)

        self.assertTrue(fases.estado_fuera_del_vocabulario(raiz),
                        "quitar «Terminada» del glosario no cambió qué acepta: "
                        "el vocabulario está escrito en el código")

    # -- CA-03 · el estado inventado se avisa -----------------------------
    def test_un_estado_del_vocabulario_no_se_avisa(self):
        self.assertEqual(self._avisos("Pendiente"), [])

    def test_un_estado_inventado_se_avisa_y_dice_cuales_valen(self):
        avisos = self._avisos("Casi lista")
        self.assertEqual(len(avisos), 1)
        self.assertIn("Casi lista", avisos[0])
        self.assertIn("Terminada", avisos[0],
                      "el aviso no dice cuáles valen")

    def test_una_palabra_de_otro_conjunto_tampoco_vale(self):
        """`Cancelada` existe, pero es de una épica, no de una historia."""
        avisos = self._avisos("Cancelada")
        self.assertEqual(len(avisos), 1)

    # -- Transversal de límites -------------------------------------------
    def test_limites_el_estado_con_texto_detras_es_valido(self):
        """El detalle que sigue es lo que hace útil el campo."""
        self.assertEqual(self._avisos("Terminada el 2026-08-14"), [])
        self.assertEqual(
            self._avisos("Terminada — los tres criterios verificados"), [])

    def test_limites_la_negrita_se_tolera(self):
        self.assertEqual(self._avisos("**Terminada**"), [])

    def test_limites_la_caja_si_cuenta(self):
        """Aceptar `terminada` abriría la puerta a que vuelvan las variantes."""
        self.assertEqual(len(self._avisos("terminada")), 1)

    def test_limites_sin_campo_de_estado_no_lo_reporta_esta_comprobacion(self):
        """**El plan pedía reportarlo, y al construirlo se vio que no.**

        Reportarlo dejaba en rojo siete pruebas de estructura cuyos árboles de
        mentira no traen el campo porque no están probando eso; en un proyecto
        haría lo mismo con cualquier historia mínima. Acá se comprueba **el
        vocabulario**. Que el documento traiga sus campos es otra cosa, y va
        aparte — queda anotado en el cierre de la fase.
        """
        self.assertEqual(self._avisos(None), [])

    def test_limites_el_campo_vacio_no_se_confunde_con_el_que_falta(self):
        avisos = self._avisos("")
        self.assertEqual(len(avisos), 1)
        self.assertIn("vacío", avisos[0])

    # -- `RN-06` · reporta y NO corrige -----------------------------------
    def test_avisar_no_toca_el_archivo(self):
        """Se compara en **bytes**, no como texto."""
        raiz = self._arbol("Casi lista")
        ruta = os.path.join(raiz, "documentacion", "epicas", "EP-001-e",
                            "HU-001-una", "HU-001-una.md")
        with io.open(ruta, "rb") as f:
            antes = f.read()

        self.assertTrue(fases.estado_fuera_del_vocabulario(raiz),
                        "no reportó nada, así que no probaría que no corrige")

        with io.open(ruta, "rb") as f:
            self.assertEqual(f.read(), antes,
                             "el programa corrigió el archivo (`EP-004 §10.2`)")

    # -- `RNF` · sale por el punto de entrada de verdad --------------------
    def test_el_aviso_sale_en_la_corrida_de_fases(self):
        """Una comprobación que nadie llama es una comprobación que no existe.

        Lo enseñó un sabotaje en la fase anterior (`S-043`): descolgarla de
        `validar` dejaba todas sus otras pruebas en verde.
        """
        raiz = self._arbol("Casi lista")
        mensajes = [h.mensaje for h in fases.validar(raiz)]
        self.assertTrue(any("Casi lista" in m for m in mensajes),
                        "el aviso no sale por `validar`")

    # -- CA-02 · el árbol real, ya normalizado -----------------------------
    def test_las_historias_de_este_repositorio_usan_el_vocabulario(self):
        self.assertEqual(fases.estado_fuera_del_vocabulario(self.RAIZ), [],
                         "alguna historia volvió a salirse del vocabulario")

    def test_ningun_molde_lista_los_estados_por_su_cuenta(self):
        """CA-01: un solo sitio define, los moldes citan."""
        viejos = ["Backlog / Ready", "En curso / Completada",
                  "En curso / Hecha / Bloqueada"]
        for nombre in ("01-planteamiento", "03-epica", "04-HU",
                       "10-estado-fase"):
            texto = comun.leer(os.path.join(
                self.RAIZ, "plantillas", "ciclo-vida-proyectos",
                "%s.md" % nombre))
            for viejo in viejos:
                self.assertNotIn(viejo, texto,
                                 "%s volvió a listar los estados" % nombre)


class ClavesYDatosSensibles(unittest.TestCase):
    """Claves en el código y archivos que no se guardan — EP-004 · HU-007.

    Lo que la clase `Secretos` ya probaba es que se detecte. Lo que faltaba es
    lo de alrededor: que el hallazgo **no reproduzca el secreto**, y que un
    archivo binario, uno enorme y uno ilegible no rompan la corrida.

    Ningún secreto de esta clase se escribe entero como literal: se arma en
    tiempo de ejecución, porque el escaneo de GitHub bloquea el envío si ve uno
    con forma real, aunque sea de mentira.
    """

    def _clave_aws(self):
        return "AKIA" + "IOSFODNN7" + "EXAMPLE1"

    # -- transversal de privacidad · el hallazgo no reproduce el secreto ---
    def test_privacidad_el_hallazgo_no_reproduce_la_clave_encontrada(self):
        clave = self._clave_aws()
        hallazgos = secretos.revisar_texto(f"clave = '{clave}'\n", "x.py")
        self.assertTrue(hallazgos, "no detectó la clave")
        for h in hallazgos:
            self.assertNotIn(clave, h.mensaje,
                             "el hallazgo reproduce el secreto que encontró")

    def test_privacidad_el_aviso_nombra_la_clave_pero_no_su_valor(self):
        valor = "sup3rs3cr3to-de-verdad"
        hallazgos = secretos.revisar_texto(f'password = "{valor}"\n', "x.py")
        self.assertTrue(hallazgos)
        self.assertIn("password", hallazgos[0].mensaje)
        self.assertNotIn(valor, hallazgos[0].mensaje)

    # -- CA-01 · la clave se reporta con archivo y línea -------------------
    def test_la_clave_se_reporta_con_su_archivo_y_su_linea(self):
        texto = "linea uno\nlinea dos\nclave = '" + self._clave_aws() + "'\n"
        hallazgos = secretos.revisar_texto(texto, "config/ajustes.py")
        self.assertEqual(len(hallazgos), 1)
        self.assertEqual(hallazgos[0].archivo, "config/ajustes.py")
        self.assertEqual(hallazgos[0].linea, 3)
        self.assertEqual(hallazgos[0].severidad, comun.FALLA)

    # -- CA-03 · el ejemplo no se confunde con una clave ------------------
    def test_los_moldes_no_se_reportan(self):
        for valor in ("changeme", "your-api-key", "tu_clave_aqui", "<TU_CLAVE>",
                      "placeholder", "xxxxxxxx", "ejemplo-de-token"):
            self.assertEqual(
                secretos.revisar_texto(f'api_key = "{valor}"\n', "x.py"), [],
                f"`{valor}` se reportó como secreto y es un molde")

    def test_leer_del_entorno_no_se_reporta(self):
        for linea in ('api_key = os.environ["API_KEY"]',
                      'secret = process.env.SECRET',
                      'password = config("DB_PASS")'):
            self.assertEqual(secretos.revisar_texto(linea + "\n", "x.py"), [],
                             f"se reportó una línea que lee del entorno: {linea}")

    # -- transversal de límites · binario, enorme y sin permisos ----------
    def test_limites_binario_enorme_e_ilegible_no_rompen_la_corrida(self):
        """Los tres bordes del transversal, sobre el camino real de
        `secretos.validar`, que es el que abre archivos."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        if not shutil.which("git"):
            self.skipTest("sin git")
        subprocess.run(["git", "init"], cwd=tmp.name, capture_output=True, timeout=30)

        with open(os.path.join(tmp.name, "binario.py"), "wb") as f:
            f.write(b"\x00\x01\xff\xfe" * 100 + b"\nclave = 'x'\n")
        with open(os.path.join(tmp.name, "enorme.py"), "w", encoding="utf-8") as f:
            f.write("# relleno\n" * 200_000)          # ~2 MB, más del tope de 1 MB
        with open(os.path.join(tmp.name, "normal.py"), "w", encoding="utf-8") as f:
            f.write("clave = '" + self._clave_aws() + "'\n")
        subprocess.run(["git", "add", "-A"], cwd=tmp.name, capture_output=True, timeout=30)

        hallazgos = secretos.validar(tmp.name)          # no revienta
        self.assertTrue(any("normal.py" in h.archivo for h in hallazgos),
                        "el archivo normal dejó de revisarse por culpa de los bordes")

    def test_limites_el_texto_vacio_no_produce_nada(self):
        self.assertEqual(secretos.revisar_texto("", "x.py"), [])
        self.assertEqual(secretos.revisar_texto("\n\n\n", "x.py"), [])

    # -- CA-02 · el archivo que no debe guardarse se reporta --------------
    def test_el_env_versionado_se_reporta(self):
        if not shutil.which("git"):
            self.skipTest("sin git")
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        subprocess.run(["git", "init"], cwd=tmp.name, capture_output=True, timeout=30)
        with open(os.path.join(tmp.name, ".env"), "w", encoding="utf-8") as f:
            f.write("DB_PASS=algo\n")
        subprocess.run(["git", "add", "-f", ".env"], cwd=tmp.name,
                       capture_output=True, timeout=30)
        hallazgos = versionado.validar(tmp.name)
        self.assertTrue(any(".env" in h.mensaje or ".env" in h.archivo
                            for h in hallazgos),
                        "un `.env` versionado no se reportó")


class EstructuraYNomenclatura(unittest.TestCase):
    """Lo que `fases.py` comprueba de `F12` — EP-004 · HU-006.

    Los tres criterios de la HU ya tenían casos sueltos en la clase `Fases`;
    lo que faltaba era el del CA-03 —que la fase incompleta **diga cuáles**
    documentos le faltan— y los dos bordes del transversal de límites.
    """

    def _arbol(self, fases_con_documentos):
        """Un árbol `documentacion/epicas/` de mentira.

        `fases_con_documentos` es `{ruta_de_fase: [documentos]}`.
        """
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        for ruta, documentos in fases_con_documentos.items():
            completa = os.path.join(tmp.name, "documentacion", "epicas", ruta)
            os.makedirs(completa, exist_ok=True)
            for doc in documentos:
                with open(os.path.join(completa, doc), "w", encoding="utf-8") as f:
                    f.write("# de mentira\n")
        return tmp.name

    # -- CA-03 · la fase incompleta dice qué le falta ---------------------
    def test_la_fase_con_solo_su_plan_dice_cuales_cuatro_le_faltan(self):
        raiz = self._arbol({
            "EP-001-epica/HU-001-hu/A-EP-001-HU-001-fase": ["plan_trabajo.md"],
        })
        faltan = [h for h in fases.validar(raiz) if "faltan documentos" in h.mensaje]
        self.assertEqual(len(faltan), 1, "no se reportó la fase incompleta")
        mensaje = faltan[0].mensaje
        for doc in ("plan_pruebas.md", "resultado_pruebas.md",
                    "estado-fase.md", "funcionalidad_implementada.md"):
            self.assertIn(doc, mensaje, f"el hallazgo no nombra `{doc}`")
        self.assertNotIn("plan_trabajo.md", mensaje,
                         "nombra como faltante uno que sí está")

    def test_la_fase_completa_no_se_reporta(self):
        raiz = self._arbol({
            "EP-001-epica/HU-001-hu/A-EP-001-HU-001-fase": [
                "plan_trabajo.md", "plan_pruebas.md", "resultado_pruebas.md",
                "estado-fase.md", "funcionalidad_implementada.md"],
        })
        faltan = [h for h in fases.validar(raiz) if "faltan documentos" in h.mensaje]
        self.assertEqual(faltan, [], "se reportó una fase que está completa")

    # -- transversal de límites · los tres bordes -------------------------
    def test_limites_epica_sin_hu_hu_sin_fases_y_carpeta_vacia(self):
        raiz = self._arbol({})
        os.makedirs(os.path.join(raiz, "documentacion", "epicas",
                                 "EP-001-epica-sin-hu"), exist_ok=True)
        os.makedirs(os.path.join(raiz, "documentacion", "epicas",
                                 "EP-002-epica/HU-001-hu-sin-fases"), exist_ok=True)
        hallazgos = fases.validar(raiz)
        # Ninguno de los tres bordes puede reventar la corrida ni dar falla.
        self.assertEqual([h for h in hallazgos if h.severidad == comun.FALLA], [],
                         "un borde vacío produjo una falla")
        self.assertTrue(any("HU-001-hu-sin-fases" in h.archivo or
                            "HU-001-hu-sin-fases" in h.mensaje for h in hallazgos),
                        "la HU sin fases no se avisó")

    def test_limites_el_arbol_vacio_es_falla_y_no_una_excepcion(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        hallazgos = fases.validar(tmp.name)
        self.assertTrue(any(h.severidad == comun.FALLA for h in hallazgos),
                        "un árbol sin `documentacion/epicas/` debería ser falla")

    # -- transversal de no regresión --------------------------------------
    def test_no_regresion_lo_ya_cerrado_sigue_pasando(self):
        """Las fases ya cerradas de este repositorio no pueden empezar a
        reportarse por haber sumado comprobaciones."""
        raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        cerradas = ("A-EP-003-HU-001-marca-de-espacio-por-llenar",
                    "A-EP-007-HU-001-rellenar-los-marcadores-al-copiar",
                    "A-EP-004-HU-014-comparar-los-dos-veredictos")
        malas = [h for h in fases.validar(raiz)
                 if any(c in h.archivo for c in cerradas)]
        self.assertEqual([h.mensaje for h in malas], [])


class FormatoDelHallazgo(unittest.TestCase):
    """Qué trae un hallazgo y qué hace cada severidad — EP-004 · HU-003.

    Lo que se vigila es que el hallazgo **alcance para arreglar sin abrir el
    programa que lo reportó**: archivo, línea cuando la hay, y la regla que se
    incumplió. Y que la severidad signifique algo: el aviso no detiene, la
    falla sí.
    """

    RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def _corrida_real(self):
        hallazgos = []
        for modulo in (flujo, fases, trazabilidad):
            hallazgos += modulo.validar(self.RAIZ)
        return hallazgos

    # -- CA-01 · el hallazgo alcanza para arreglar -------------------------
    def test_todo_hallazgo_dice_en_que_archivo(self):
        sin = [h for h in self._corrida_real() if not h.archivo]
        self.assertEqual(sin, [], f"{len(sin)} hallazgos sin archivo")

    def test_todo_hallazgo_nombra_la_regla_que_se_incumple(self):
        """Sin la regla, el hallazgo dice qué está mal y no **por qué**, y hay
        que abrir el programa para saber qué se exigía."""
        import re
        # La regla va entre paréntesis, sola —`(F18)`— o seguida de dos puntos
        # y su porqué —`(F2: sin especificación acordada no hay código)`—, y a
        # veces con varias —`(F4/F14)`—. Las tres formas cuentan.
        patron = re.compile(r"\([A-Z]{1,4}\d+(\.\d+)?([/·][A-Z]{1,4}\d+)*[):]|\bHU-\d+\b")
        sin = [h for h in self._corrida_real() if not patron.search(h.mensaje)]
        self.assertEqual([h.mensaje for h in sin], [],
                         "hay hallazgos que no dicen qué regla se incumple")

    def test_el_hallazgo_de_archivo_entero_no_inventa_una_linea(self):
        """Transversal de límites: un hallazgo sobre el archivo completo —«al
        plan le faltan secciones»— **no tiene** línea concreta, y la forma
        definida es dejarla en cero, no apuntar a la línea 1, que mandaría a
        mirar donde no está el problema."""
        sin_linea = [h for h in self._corrida_real() if not h.linea]
        self.assertTrue(sin_linea, "no hay ningún hallazgo de archivo entero que probar")
        for h in sin_linea:
            self.assertEqual(h.linea, 0)
            self.assertTrue(h.archivo)

    # -- CA-02 y CA-03 · qué hace cada severidad --------------------------
    def test_solo_avisos_termina_en_cero(self):
        codigo = comun.reportar([comun.Hallazgo(comun.AVISO, "a.md", 3, "algo (X1)"),
                                 comun.Hallazgo(comun.AVISO, "b.md", 0, "otra (X2)")],
                                titulo=None)
        self.assertEqual(codigo, 0)

    def test_una_falla_termina_en_uno(self):
        codigo = comun.reportar([comun.Hallazgo(comun.AVISO, "a.md", 3, "algo (X1)"),
                                 comun.Hallazgo(comun.FALLA, "b.md", 7, "grave (X2)")],
                                titulo=None)
        self.assertEqual(codigo, 1)

    def test_sin_hallazgos_termina_en_cero(self):
        self.assertEqual(comun.reportar([], titulo=None), 0)

    def test_errores_el_archivo_que_no_se_puede_leer_no_vuelca_la_excepcion(self):
        """Transversal de errores de la HU: «el archivo que no se puede leer
        produce un mensaje entendible, no un volcado técnico».

        **Arreglado el 2026-08-22** en la fase `B-EP-004-HU-003`. Antes
        `comun.leer` abría sin red, así que un `.md` que no fuera UTF-8
        **tumbaba la corrida entera** con un `UnicodeDecodeError` y se llevaba
        por delante todos los hallazgos ya encontrados. Ahora se lee lo que se
        pueda, el archivo queda anotado y `reportar` lo dice como aviso: la
        corrida sigue, y nadie cree que se miró lo que no se pudo mirar."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        raro = os.path.join(tmp.name, "raro.md")
        with open(raro, "wb") as f:
            f.write(b"# T\xed\xf3tulo mal codificado\n\ntexto\n")
        comun.leer(raro)                 # no revienta

        # Y lo que importa: queda **dicho**. Leer reemplazando y callar
        # convertiría un archivo roto en uno que parece sano.
        avisos = [h for h in comun.ilegibles() if raro in h.archivo]
        self.assertTrue(avisos, "el archivo ilegible no quedó anotado")
        self.assertEqual(comun.AVISO, avisos[0].severidad,
                         "un archivo ilegible no puede detener la corrida")
        self.assertIn("UTF-8", avisos[0].mensaje)

    def test_errores_la_corrida_sigue_y_reporta_lo_demas(self):
        """El caso que decide: un archivo roto no se lleva los hallazgos ya
        encontrados. Antes del arreglo, la corrida terminaba sin una sola línea
        de salida útil."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        with open(os.path.join(tmp.name, "roto.md"), "wb") as f:
            f.write(b"# T\xed\xf3tulo mal codificado\n")
        bueno = os.path.join(tmp.name, "bueno.md")
        with open(bueno, "w", encoding="utf-8") as f:
            f.write("# Bueno\n\n[enlace roto](no-existe.md)\n")

        comun.ILEGIBLES.clear()
        for nombre in sorted(os.listdir(tmp.name)):
            comun.leer(os.path.join(tmp.name, nombre))

        anotados = comun.ilegibles()
        self.assertEqual(1, len(anotados), "se anotó lo que sí se pudo leer")
        self.assertIn("roto.md", anotados[0].archivo)
        comun.ILEGIBLES.clear()

    def test_la_corrida_completa_respeta_los_dos_codigos(self):
        """Por el camino real, no llamando a `reportar`: se corre `validar.py`
        como orden del sistema."""
        def correr(sub):
            return subprocess.run(
                [sys.executable, os.path.join(self.RAIZ, "validadores", "validar.py"), sub],
                capture_output=True, text=True, encoding="utf-8", timeout=180, cwd=self.RAIZ).returncode
        self.assertEqual(correr("flujo"), 0, "una corrida de solo avisos no dio 0")
        self.assertEqual(correr("estandar"), 0, "`estandar` está en rojo por otra causa")


class ClasificacionDeCadaRegla(unittest.TestCase):
    """Toda regla dice si es comprobable — EP-004 · HU-002.

    El registro es [`validadores/reglas-validables.md`](../validadores/reglas-validables.md).
    Se comprueba **en los dos sentidos**: que ninguna regla se quede sin
    clasificar, y que el registro no nombre reglas que no existan. Hoy el
    programa solo mira el primer sentido.
    """

    RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def _base(self):
        textos = []
        for carpeta, _, archivos in os.walk(os.path.join(self.RAIZ, "base")):
            for n in archivos:
                if n.endswith(".md"):
                    textos.append(comun.leer(os.path.join(carpeta, n)))
        return "\n".join(textos)

    # -- CA-01, ida: ninguna regla sin clasificar -------------------------
    def test_ninguna_regla_de_base_se_queda_sin_clasificar(self):
        sin = [h for h in metareglas.validar(self.RAIZ)
               if "no aparece en" in h.mensaje]
        self.assertEqual(sin, [], f"reglas sin clasificar: {[h.mensaje for h in sin]}")

    # -- CA-01, vuelta: el registro no inventa reglas ---------------------
    def test_el_registro_no_nombra_reglas_que_no_existan(self):
        """La vuelta que el programa **no** comprueba. Se hace acá contra el
        texto de `base/`, no contra lo que el analizador reconoce: si no,
        cualquier regla que el analizador no vea saldría como inventada."""
        import re
        base = self._base()
        inventadas = [rid for rid in sorted(metareglas._clasificadas(self.RAIZ))
                      if not re.search(r"\b" + re.escape(rid) + r"\b", base)]
        self.assertEqual(inventadas, [], f"el registro nombra lo que no existe: {inventadas}")

    @unittest.expectedFailure
    def test_el_analizador_ve_todas_las_reglas_escritas_en_base(self):
        """**Falla hoy** (defecto `D-01` de la fase): `metareglas.reglas()`
        solo reconoce las reglas escritas como `## `. Las cuatro del capítulo
        16 están escritas como `### CQ1 · …`, así que el analizador **no las
        ve** — y ninguna de las 20 filas del checklist se les aplica nunca.

        No es que estén mal clasificadas: es que no existen para el programa.
        Sale en verde por el mismo motivo por el que pasaría un validador que
        no valida nada."""
        vistas = {r.id for r in metareglas.reglas(self.RAIZ)}
        for rid in ("CQ1", "CQ2", "CQ3", "CQ4"):
            self.assertIn(rid, vistas, f"el analizador no ve `{rid}`")

    # -- CA-01: el registro no se lee por rangos --------------------------
    def test_el_registro_no_clasifica_por_rangos(self):
        """Un rango como «C1–C17» no puede valer por diecisiete reglas: nadie
        sabría cuál de las diecisiete falta. Ya pasó, y se arregló en
        `A-EP-001-HU-009`."""
        clasificadas = metareglas._clasificadas(self.RAIZ)
        self.assertIn("C1", clasificadas)
        self.assertIn("C17", clasificadas)
        self.assertNotIn("C1–C17", clasificadas)
        self.assertNotIn("C1-C17", clasificadas)

    # -- CA-02: la regla comprobada dice quién la comprueba ---------------
    def test_por_el_registro_se_llega_al_programa_que_comprueba(self):
        registro = comun.leer(os.path.join(self.RAIZ, "validadores",
                                           "reglas-validables.md"))
        for regla, programa in (("04·S4", "secretos.py"),
                                ("10·DEP2", "dependencias.py"),
                                ("09·G4", "rama.py")):
            fila = [l for l in registro.splitlines()
                    if l.startswith("|") and regla in l]
            self.assertTrue(fila, f"`{regla}` no tiene fila en el registro")
            self.assertIn(programa, fila[0],
                          f"la fila de `{regla}` no nombra su programa")
            self.assertTrue(os.path.isfile(
                os.path.join(self.RAIZ, "validadores", programa)),
                f"`{programa}` no existe")

    # -- transversales de la HU, que el plan de pruebas no cubrió ---------
    def test_limites_la_regla_derogada_se_conserva_marcada_y_no_se_exige(self):
        """Transversal de límites: una regla derogada **no desaparece** del
        registro ni se le exige clasificación nueva. Las cuatro `F4.x` están
        derogadas, siguen en `base/` con su marca, y el validador no las
        reclama."""
        derogadas = [r for r in metareglas.reglas(self.RAIZ) if r.derogada]
        self.assertTrue(derogadas, "no hay ninguna regla derogada que probar")
        reclamadas = {h.mensaje for h in metareglas.validar(self.RAIZ)
                      if "no aparece en" in h.mensaje}
        for r in derogadas:
            self.assertFalse(any(r.id in m for m in reclamadas),
                             f"se le exige clasificación a `{r.id}`, que está derogada")

    # -- CA-03: una regla nueva sin clasificar se avisa -------------------
    def test_una_regla_nueva_sin_clasificar_se_avisa(self):
        """En copia, no sobre `base/`: escribir una regla de mentira en el
        cuerpo real dejaría el repositorio con una regla que nadie aprobó."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        base = os.path.join(tmp.name, "base")
        os.makedirs(os.path.join(base, "20-meta-reglas"))
        # `base/` y `VERSION` son lo que `es_el_estandar` mira para no juzgar
        # con meta-reglas una carpeta que no es el estándar (pendiente 81). El
        # árbol de mentira tiene que parecerse en eso, o el validador se niega
        # a mirarlo y la prueba comprueba el rechazo en vez de la regla.
        with open(os.path.join(tmp.name, "VERSION"), "w", encoding="utf-8") as f:
            f.write("0.0.0" + chr(10))
        with open(os.path.join(base, "99-inventado.md"), "w", encoding="utf-8") as f:
            f.write("# Capítulo inventado\n\n## ZZ1 · Una regla que nadie clasificó\n\n"
                    "Texto de la regla.\n\n```\nINCORRECTO: a\nCORRECTO: b\n```\n")
        os.makedirs(os.path.join(tmp.name, "validadores"))
        with open(os.path.join(tmp.name, "validadores", "reglas-validables.md"),
                  "w", encoding="utf-8") as f:
            f.write("# Qué reglas del estándar son validables\n\n(ninguna)\n")
        avisos = [h for h in metareglas.validar(tmp.name)
                  if "ZZ1" in h.mensaje and "no aparece en" in h.mensaje]
        self.assertEqual(len(avisos), 1, "la regla sin clasificar no se avisó")

    def test_la_regla_sin_clasificar_detiene_la_publicacion(self):
        """CA-03 pide que una regla nueva **no se publique** sin clasificar.

        **Pasa desde el 2026-08-17**, al cerrarse el punto 2 del pendiente 53:
        `metareglas.py` ya tiene su subcomando y en una corrida normal se
        ejecuta. Antes estaba marcada como fallo esperado.

        **Ojo con lo que esta prueba NO comprueba.** La otra mitad del defecto
        `D-02` sigue abierta: lo que sale es un **AVISO**, y un aviso no detiene
        nada. Que el programa se pueda correr no es que la regla sin clasificar
        detenga la publicación — solo que ahora hay quien la mire. Lo que falta
        vive en el pendiente [19].
        """
        import re
        entradas = re.findall(r'sub\.add_parser\("([a-z]+)"',
                              comun.leer(os.path.join(self.RAIZ, "validadores",
                                                      "validar.py")))
        self.assertIn("metareglas", entradas,
                      "`metareglas.py` no se puede correr desde `validar.py`")


class TodoEnganchePreparaSuSalida(unittest.TestCase):
    """Ningún enganche escribe en la página de códigos de la consola.

    Es el pendiente [45] otra vez, en otro archivo: allá `instalar()` se moría
    al imprimir una flecha porque solo `main()` preparaba la consola; acá
    `hook_resumen.py` era el único de los seis que no llamaba a
    `preparar_salida()`, y su texto —lleno de acentos y comillas angulares—
    salía en cp1252. Con la salida en una tubería ni siquiera se podía
    decodificar. Se arregló el 2026-08-17; esta prueba es para que la lista no
    vuelva a quedar coja cuando nazca el séptimo.
    """

    VALIDADORES = os.path.dirname(os.path.abspath(__file__))
    # Los enganches se mudaron al adaptador el 2026-08-19: `validadores/`
    # es lo que sirve con cualquier agente, y esto existe porque **esta**
    # herramienta lo llama.
    ADAPTADOR = os.path.join(os.path.dirname(VALIDADORES),
                             "adaptadores", "claude-code")

    def test_los_seis_enganches_llaman_a_preparar_salida(self):
        enganches = sorted(f for f in os.listdir(self.ADAPTADOR)
                           if f.startswith("hook_") and f.endswith(".py"))
        self.assertGreaterEqual(len(enganches), 6, "faltan enganches por revisar")
        sin_preparar = [f for f in enganches
                        if "preparar_salida()" not in
                        comun.leer(os.path.join(self.ADAPTADOR, f))]
        self.assertEqual(sin_preparar, [],
                         f"enganches que no preparan su salida: {sin_preparar}")


class IndiceDeLosRecuerdos(unittest.TestCase):
    """El índice dice de qué trata cada recuerdo — EP-006 · HU-002 · CA-02.

    Se comprueba **en los dos sentidos**. Con uno solo, la mitad de los errores
    pasa: si solo se mira que cada archivo tenga su línea, una línea que apunta
    a un archivo borrado sobrevive; si solo se mira al revés, un recuerdo nuevo
    sin indexar tampoco se ve.
    """

    CARPETA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                           "historico-chat", "memory")

    def _archivos(self, carpeta):
        return {f for f in os.listdir(carpeta)
                if f.endswith(".md") and f != "memory.md"}

    def _enlazados(self, carpeta):
        import re
        idx = comun.leer(os.path.join(carpeta, "memory.md"))
        return {e for e in re.findall(r"\]\(([^)]+\.md)\)", idx)
                if "/" not in e and e != "memory.md"}

    def test_todo_recuerdo_de_esta_casa_tiene_su_linea_en_el_indice(self):
        faltan = self._archivos(self.CARPETA) - self._enlazados(self.CARPETA)
        self.assertEqual(faltan, set(), f"sin línea en el índice: {sorted(faltan)}")

    def test_toda_linea_del_indice_de_esta_casa_tiene_su_archivo(self):
        sobran = self._enlazados(self.CARPETA) - self._archivos(self.CARPETA)
        self.assertEqual(sobran, set(), f"línea sin archivo: {sorted(sobran)}")

    def test_privacidad_ningun_recuerdo_lleva_claves_ni_datos_personales(self):
        """Transversal de privacidad de la HU. Se corre el mismo detector que
        vigila el código (`04·S4`), no una revisión a ojo: a ojo, un recuerdo
        nuevo con una clave pegada pasaría el día que nadie mire."""
        hallazgos = [h for h in secretos.validar(instalar.RAIZ)
                     if os.path.join("historico-chat", "memory") in h.archivo]
        self.assertEqual(hallazgos, [], f"secretos en los recuerdos: {hallazgos}")

    def test_el_indice_vacio_es_valido(self):
        """Transversal de límites: un proyecto sin nada guardado tiene un
        índice válido, vacío. No es un error que no haya recuerdos todavía."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        os.makedirs(tmp.name, exist_ok=True)
        with open(os.path.join(tmp.name, "memory.md"), "w", encoding="utf-8") as f:
            f.write("# Memoria del agente\n\n## Índice\n\n(todavía no hay ninguno)\n")
        self.assertEqual(self._archivos(tmp.name), set())
        self.assertEqual(self._enlazados(tmp.name), set())

    def test_por_el_indice_se_llega_al_recuerdo_sin_abrir_los_otros(self):
        """CA-02: cada línea dice **de qué trata**, no solo cómo se llama. Se
        comprueba que ninguna línea del índice sea solo el enlace: si el texto
        de la fila no agrega nada, hay que abrir los 18 para encontrar uno."""
        import re
        idx = comun.leer(os.path.join(self.CARPETA, "memory.md"))
        filas = [l for l in idx.splitlines()
                 if l.startswith("|") and re.search(r"\]\([^/)]+\.md\)", l)]
        self.assertGreaterEqual(len(filas), 1, "el índice no tiene filas de recuerdo")
        for fila in filas:
            celdas = [c.strip() for c in fila.strip().strip("|").split("|")]
            descripcion = celdas[-1]
            self.assertNotEqual(descripcion, "", f"fila sin descripción: {fila}")
            self.assertGreater(len(descripcion), 20,
                               f"la descripción no dice de qué trata: {fila}")


class ElRecuerdoTraeSusTresPartes(unittest.TestCase):
    """Qué se pide, por qué y cómo se aplica — EP-006 · HU-005 · CA-02.

    El **por qué** es el que se pierde primero y el que más cuesta reponer: sin
    él, un recuerdo se lee como un capricho y la siguiente sesión lo discute
    otra vez. El **cómo se aplica** es lo que lo vuelve accionable.
    """

    CARPETA = IndiceDeLosRecuerdos.CARPETA

    def _partes(self, texto):
        return ("**Por qué" in texto, "Cómo se aplica" in texto)

    def test_todo_recuerdo_de_esta_casa_dice_por_que_y_como_se_aplica(self):
        sin_partes = []
        for f in sorted(os.listdir(self.CARPETA)):
            if not f.endswith(".md") or f == "memory.md":
                continue
            porque, como = self._partes(comun.leer(os.path.join(self.CARPETA, f)))
            if not (porque and como):
                sin_partes.append((f, porque, como))
        self.assertEqual(sin_partes, [], f"recuerdos incompletos: {sin_partes}")

    def test_un_recuerdo_sin_el_porque_se_detecta(self):
        """El caso negativo. Sin él, la prueba de arriba pasaría también con
        un comprobador que no comprueba nada."""
        porque, como = self._partes("# Algo\n\nSe hace así.\n\n**Cómo se aplica:** así.\n")
        self.assertFalse(porque)
        self.assertTrue(como)


class ElAlmacenLocalQuedaVacio(unittest.TestCase):
    """El almacén de la herramienta queda vacío — EP-006 · HU-006.

    Lo que se vigila no es que el recuerdo llegue al repositorio, sino que **no
    quede una segunda copia** donde nadie la revisa: dos versiones del mismo
    recuerdo terminan diciendo cosas distintas, y manda la que no se ve.
    """

    CASA_REAL = os.path.expanduser("~")

    def _monta(self, locales=None, repo=None):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        proyecto = os.path.join(tmp.name, "proyecto")
        casa = os.path.join(tmp.name, "casa")
        for carpeta, archivos in ((recuerdos.carpeta_local(proyecto, casa), locales or {}),
                                  (recuerdos.carpeta_repo(proyecto), repo or {})):
            if archivos:
                os.makedirs(carpeta, exist_ok=True)
                for nombre, texto in archivos.items():
                    with open(os.path.join(carpeta, nombre), "w", encoding="utf-8") as f:
                        f.write(texto)
        return proyecto, casa

    def test_despues_de_recoger_el_almacen_local_no_tiene_archivos(self):
        proyecto, casa = self._monta(locales={"algo.md": "# Algo\n"})
        recuerdos.migrar(proyecto, aplicar=True, casa=casa)
        local = recuerdos.carpeta_local(proyecto, casa)
        self.assertEqual([f for f in os.listdir(local) if f.endswith(".md")], [])

    def test_no_queda_un_puntero_en_lugar_del_texto(self):
        """CA-02: puesto a mano un archivo que solo dice dónde quedó el
        recuerdo, el recogido **también** lo saca. Un puntero es una segunda
        copia que envejece igual que el texto."""
        puntero = "# Ver el repositorio\n\nEste recuerdo vive en `historico-chat/memory/algo.md`.\n"
        proyecto, casa = self._monta(locales={"puntero.md": puntero})
        recuerdos.migrar(proyecto, aplicar=True, casa=casa)
        local = recuerdos.carpeta_local(proyecto, casa)
        quedan = [f for f in os.listdir(local) if f.endswith(".md")]
        self.assertEqual(quedan, [], f"quedó un puntero en el almacén local: {quedan}")

    def test_con_el_almacen_ya_vacio_no_falla_ni_hace_nada(self):
        proyecto, casa = self._monta(repo={"algo.md": "# Algo\n"})
        movidos = recuerdos.migrar(proyecto, aplicar=True, casa=casa)
        self.assertEqual(movidos, [])

    @unittest.expectedFailure
    def test_no_se_lleva_lo_que_no_es_recuerdo(self):
        """CP-001, paso 5: en el almacén local puede haber archivos de la
        herramienta que no son recuerdos. Llevárselos al repositorio sería
        peor que dejarlos.

        **Falla hoy, y el programa no está claramente equivocado.** `sueltos()`
        devuelve *todo* archivo del almacén, no solo los `.md`, así que un
        `config.json` termina en `historico-chat/memory/`. Pero dejarlo sería
        incumplir [`01·C19`], que exige el almacén **vacío** — y entonces
        `revisar()` reprobaría para siempre por un archivo que no es un
        recuerdo.

        Las dos salidas son malas y elegir entre ellas no es del que ejecuta:
        o el recogido distingue qué es recuerdo y `C19` acepta que quede lo que
        no lo es, o se acepta que se lleve todo. Queda como fallo esperado y
        como pregunta al usuario, no como parche."""
        proyecto, casa = self._monta(locales={"algo.md": "# Algo\n",
                                              "config.json": "{}\n"})
        recuerdos.migrar(proyecto, aplicar=True, casa=casa)
        local = recuerdos.carpeta_local(proyecto, casa)
        self.assertIn("config.json", os.listdir(local))
        self.assertNotIn("config.json", os.listdir(recuerdos.carpeta_repo(proyecto)))

    def test_no_quedan_dos_versiones_del_mismo_recuerdo(self):
        """CP-002, paso 5: lo que este vaciado evita no es perder el recuerdo,
        sino tener dos copias donde manda la que nadie revisa."""
        proyecto, casa = self._monta(locales={"algo.md": "# Algo local\n"})
        recuerdos.migrar(proyecto, aplicar=True, casa=casa)
        local = recuerdos.carpeta_local(proyecto, casa)
        repo = recuerdos.carpeta_repo(proyecto)
        en_local = [f for f in os.listdir(local) if f.endswith(".md")]
        en_repo = [f for f in os.listdir(repo) if f.endswith(".md")]
        self.assertEqual(en_local, [])
        self.assertEqual(len(en_repo), 1)

    def test_el_almacen_de_esta_maquina_esta_vacio(self):
        """El estado real, no el simulado. Es el caso que el plan pedía dejar
        escrito: qué había de verdad en el almacén de esta máquina."""
        raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        local = recuerdos.carpeta_local(raiz, self.CASA_REAL)
        quedan = ([f for f in os.listdir(local) if f.endswith(".md")]
                  if os.path.isdir(local) else [])
        self.assertEqual(quedan, [], f"el almacén local de esta máquina tiene: {quedan}")


class TestPresupuesto(unittest.TestCase):
    """El consumo de la sesión: sumar y avisar, sin detener nada."""

    def test_suma_y_total(self):
        import presupuesto
        r = presupuesto.resumen([
            {"entrada": 100, "salida": 20, "cache": 5},
            {"entrada": 50, "salida": 30},                 # sin cache: cuenta 0
        ])
        self.assertEqual(r["turnos"], 2)
        self.assertEqual(r["entrada"], 150)
        self.assertEqual(r["salida"], 50)
        self.assertEqual(r["cache"], 5)
        self.assertEqual(r["total"], 200)                  # la caché no suma al total

    def test_umbral(self):
        import presupuesto
        r = presupuesto.resumen([{"entrada": 900, "salida": 200}])
        self.assertTrue(presupuesto.excedido(r, 1000))
        self.assertFalse(presupuesto.excedido(r, 2000))
        self.assertFalse(presupuesto.excedido(r, 0))       # sin umbral no avisa
        self.assertIn("AVISO", presupuesto.como_texto(r, 1000))
        self.assertNotIn("AVISO", presupuesto.como_texto(r))

    def test_el_adaptador_lee_la_transcripcion_de_la_herramienta(self):
        """La línea ilegible se salta; la del usuario (sin consumo) no cuenta."""
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(
            os.path.abspath(__file__))), "adaptadores", "claude-code"))
        import hook_presupuesto
        with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False,
                                         encoding="utf-8") as f:
            f.write(json.dumps({"type": "user", "message": {"role": "user"}}) + "\n")
            f.write("esto no es JSON\n")
            f.write(json.dumps({"message": {"usage": {
                "input_tokens": 10, "cache_creation_input_tokens": 5,
                "cache_read_input_tokens": 100, "output_tokens": 7}}}) + "\n")
            ruta = f.name
        try:
            consumos = hook_presupuesto.consumos_de_transcripcion(ruta)
        finally:
            os.unlink(ruta)
        self.assertEqual(consumos, [{"entrada": 15, "salida": 7, "cache": 100}])


class TestInmutable(unittest.TestCase):
    """El histórico solo crece: se agrega, no se reescribe."""

    def test_agregar_al_final_es_crecer(self):
        import inmutable
        self.assertTrue(inmutable.solo_crecio("a\nb\n", "a\nb\nc\n"))
        self.assertTrue(inmutable.solo_crecio("a\nb\n", "a\nb\n"))

    def test_editar_el_pasado_no_es_crecer(self):
        import inmutable
        self.assertFalse(inmutable.solo_crecio("a\nb\n", "a\nX\nc\n"))

    def test_los_finales_de_linea_de_windows_no_confunden(self):
        """`git show` entrega LF y el disco puede tener CRLF: no es una edición."""
        import inmutable
        self.assertTrue(inmutable.solo_crecio("a\nb\n", "a\r\nb\r\nc\r\n"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
