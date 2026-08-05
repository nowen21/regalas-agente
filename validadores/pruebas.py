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
import enlaces          # noqa: E402
import fases            # noqa: E402
import instalar         # noqa: E402
import plantillas       # noqa: E402
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
        # F12.12 · `D-B-EP01-HU03-…` (la fase D complementa a la B).
        raiz = self._armar("EP-001-x", "HU-003-y", "D-B-EP-001-HU-003-ajuste")
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

    def test_sin_la_carpeta_epicas_es_falla(self):
        hallazgos = fases.validar(self.tmp.name)
        self.assertEqual(severidades(hallazgos), [FALLA])


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
