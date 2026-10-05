"""Los validadores del repositorio y de git, como clases.

Son las pruebas que tenían en `validadores/pruebas.py`, pasadas a su clase. Las
claves de ejemplo se arman al correr (prefijo + cuerpo): el literal entero nunca
queda en el archivo, porque GitHub lo tomaría por real y bloquearía el envío.
"""
import os
import tempfile
import unittest

from core.comun import AVISO, FALLA
from core.validadores import (ArchivosVersionados, IntegracionContinua, LockfileVersionado,
                              MensajeDeCommit, RamaDedicada, SecretosEnElCodigo)
from core.validadores.ci import ARCHIVO_DE_CI


def severidades(hallazgos):
    return [h.severidad for h in hallazgos]


class MensajeDeCommitRevisa(unittest.TestCase):
    """`09·G2` y `09·G8`."""

    revisar = staticmethod(MensajeDeCommit.revisar)

    def test_el_ejemplo_correcto_de_g2_pasa(self):
        self.assertEqual(self.revisar("Corrige el saldo cuando hay documentos anulados\n\n"
                                      "Se sumaban al total; ahora se excluyen en la consulta.\n"), [])

    def test_vacio_y_sin_contenido_fallan(self):
        self.assertEqual(severidades(self.revisar("\n\n")), [FALLA])
        for vacio in ("wip", "fix", "cambios", "WIP", "Fix."):
            self.assertIn(FALLA, severidades(self.revisar(vacio)), vacio)

    def test_falta_la_linea_en_blanco(self):
        hallazgos = self.revisar("Corrige el saldo con documentos anulados\nSe sumaban al total.\n")
        self.assertEqual((severidades(hallazgos), hallazgos[0].linea), ([FALLA], 2))

    def test_asunto_largo_solo_avisa(self):
        self.assertEqual(severidades(self.revisar("C" * 100)), [AVISO])

    def test_la_firma_de_la_herramienta_se_ancla_en_su_linea(self):
        hallazgos = self.revisar("Corrige el saldo con documentos anulados\n\nSe sumaban al total.\n\n"
                                 "Co-Authored-By: Alguien <a@b.c>\n")
        self.assertEqual((severidades(hallazgos), hallazgos[0].linea), ([FALLA], 5))

    def test_las_lineas_que_git_descarta_no_cuentan(self):
        self.assertEqual(self.revisar("Corrige el saldo con documentos anulados\n\nSe sumaban al total.\n"
                                      "# Please enter the commit message...\n"), [])


class ArchivosVersionadosClasifica(unittest.TestCase):
    """`09·G3`."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def clasificar(self, archivo, contenido=None):
        if contenido is not None:
            destino = os.path.join(self.tmp.name, archivo)
            os.makedirs(os.path.dirname(destino), exist_ok=True)
            with open(destino, "w", encoding="utf-8") as f:
                f.write(contenido)
        return ArchivosVersionados.clasificar(self.tmp.name, archivo)

    def test_secretos_y_dependencias_son_falla(self):
        for archivo in (".env", ".env.produccion", "node_modules/x/index.js", "vendor/autoload.php",
                        "certs/servidor.pem", ".ssh/id_rsa", ".npmrc"):
            self.assertEqual(self.clasificar(archivo)[0], FALLA, archivo)

    def test_la_plantilla_de_ejemplo_si_se_versiona(self):
        for archivo in (".env.example", ".env.sample", "config.dist"):
            self.assertIsNone(self.clasificar(archivo), archivo)

    def test_la_libreria_copiada_a_proposito_no_se_marca(self):
        self.assertIsNone(self.clasificar("public/vendor/reveal/dist/theme/moon.css"))
        self.assertIsNone(self.clasificar("interfaz/visor/static/vendor/bootstrap.min.js"))

    def test_el_sql_se_decide_por_su_contenido(self):
        self.assertIsNone(self.clasificar("memoria/esquema.sql", "CREATE TABLE senales (id TEXT);"))
        volcado = "\n".join("INSERT INTO usuarios VALUES (%d, 'x');" % n for n in range(20))
        self.assertEqual(self.clasificar("documentacion/produccion.sql", volcado)[0], AVISO)

    def test_la_config_del_editor_solo_avisa(self):
        self.assertEqual(self.clasificar(".vscode/tasks.json")[0], AVISO)


class SecretosEnElCodigoBusca(unittest.TestCase):
    """`04·S4` y `00·N6`."""

    def severidad(self, linea):
        hallazgos = SecretosEnElCodigo.revisar_texto(linea)
        return hallazgos[0].severidad if hallazgos else None

    def test_las_formas_de_proveedor_son_falla(self):
        self.assertEqual(self.severidad('$key = "%s";' % ("AKIA" + "IOSFODNN7EXAMPLE")), FALLA)
        self.assertEqual(self.severidad("-----BEGIN RSA PRIVATE KEY-----"), FALLA)
        for prefijo, cuerpo in (("sk_live_", "abcdef0123456789ABCD"), ("xoxb-", "1234567890-abcdefghijklmno"),
                                ("ghp_", "0123456789abcdefghijklmnopqrstuvwxyz")):
            self.assertEqual(self.severidad('x = "%s%s"' % (prefijo, cuerpo)), FALLA, prefijo)

    def test_un_texto_fijo_avisa_y_el_entorno_o_el_molde_no(self):
        self.assertEqual(self.severidad("password = 'S3cretoReal!'"), AVISO)
        for linea in ("$key = env('API_KEY');", "password = os.environ['DB_PASS']",
                      "secret = process.env.CLIENT_SECRET", "token = config('services.slack.token')",
                      "password = 'changeme'", "api_key = 'your-api-key'", "secret = '<tu-secreto>'",
                      "password = 'xxxxxxxx'"):
            self.assertIsNone(self.severidad(linea), linea)

    def test_una_linea_un_hallazgo(self):
        self.assertEqual(len(SecretosEnElCodigo.revisar_texto('key = "' + "AKIA" + 'IOSFODNN7EXAMPLE"')), 1)


class LockfileVersionadoRevisa(unittest.TestCase):
    """`10·DEP2`."""

    revisar = staticmethod(LockfileVersionado.revisar)

    def test_lockfile_en_su_carpeta(self):
        self.assertEqual(self.revisar(["composer.json", "composer.lock"]), [])
        self.assertEqual(self.revisar(["package.json", "yarn.lock"]), [])
        self.assertEqual(severidades(self.revisar(["composer.json", "app/Http/Kernel.php"])), [AVISO])
        self.assertEqual(len(self.revisar(["front/package.json", "package-lock.json"])), 1)

    def test_el_manifiesto_de_una_dependencia_instalada_no_cuenta(self):
        self.assertEqual(self.revisar(["vendor/laravel/framework/composer.json"]), [])


class RamaDedicadaEvalua(unittest.TestCase):
    """`09·G4`."""

    evaluar = staticmethod(RamaDedicada.evaluar)

    def test_lo_que_se_senala(self):
        self.assertEqual(self.evaluar("HU-003-login", "main", 0), [])
        self.assertEqual(severidades(self.evaluar("main", "main", 0)), [AVISO])
        self.assertEqual(len(self.evaluar("master", "master", 0)), 1)
        self.assertEqual(self.evaluar("feature-x", "master", 0), [])
        self.assertIn("4 commit", self.evaluar("feature-x", "main", 4)[0].mensaje)
        self.assertEqual(severidades(self.evaluar("HEAD", "main", 0)), [AVISO])
        self.assertEqual(self.evaluar("cualquiera", None, 0), [])


class IntegracionContinuaRevisa(unittest.TestCase):
    """`09·G6`."""

    def test_lo_que_falta(self):
        self.assertEqual(len(IntegracionContinua.motivos([])), 1)
        self.assertEqual(IntegracionContinua.motivos(["jobs:\n  test:\n    run: phpunit\n  lint:\n    run: pint --test"]), [])
        self.assertTrue(any("linter" in m for m in IntegracionContinua.motivos(["run: phpunit"])))

    def test_reconoce_los_archivos_de_ci(self):
        for ruta in (".github/workflows/ci.yml", ".gitlab-ci.yml", "Jenkinsfile"):
            self.assertRegex(ruta, ARCHIVO_DE_CI)


if __name__ == "__main__":
    unittest.main()
