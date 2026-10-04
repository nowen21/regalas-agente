"""Los validadores como clases: la base y los que revisan el código.

Las pruebas de cada validador son las que tenía en `validadores/pruebas.py`,
pasadas a su clase: lo que se comprobaba se sigue comprobando.
"""
import os
import subprocess
import tempfile
import unittest

from core.validadores import (CapturasYLogs, ConsultasCostosas, FuncionesLargas,
                              InyeccionYSesion, PruebasAisladas, Validador)
from core.validadores.codigo import Bloques


class LaBaseRegistraYExige(unittest.TestCase):

    def test_el_validador_queda_registrado_por_su_nombre(self):
        self.assertIs(Validador.registrados()["calidad"], FuncionesLargas)

    def test_dos_con_el_mismo_nombre_no_se_admiten(self):
        with self.assertRaises(ValueError):
            type("Otro", (Validador,), {"nombre": "calidad"})

    def test_el_que_no_escribe_validar_lo_dice(self):
        Incompleto = type("Incompleto", (Validador,), {})
        with self.assertRaises(NotImplementedError):
            Incompleto(".").validar()


class FuncionesLargasAvisa(unittest.TestCase):

    def setUp(self):
        self.validador = FuncionesLargas(".")
        self.tope = FuncionesLargas.tope

    def test_funcion_larga_de_php_avisa(self):
        cuerpo = "\n".join("    $x = %d;" % i for i in range(self.tope + 5))
        self.assertEqual(len(self.validador.revisar_texto("function grande() {\n" + cuerpo + "\n}")), 1)

    def test_funcion_corta_no_avisa(self):
        self.assertEqual(self.validador.revisar_texto("function chica() {\n  return 1;\n}"), [])

    def test_def_de_python_largo_avisa_y_cita_su_regla(self):
        cuerpo = "\n".join("    x = %d" % i for i in range(self.tope + 5))
        hallazgos = self.validador.revisar_texto("def grande():\n" + cuerpo)
        self.assertEqual([h.regla for h in hallazgos], ["07·Q3"])

    def test_recorre_solo_el_codigo_versionado(self):
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run(["git", "init", "-q", tmp], check=True)
            largo = "def grande():\n" + "\n".join("    x = %d" % i for i in range(self.tope + 5))
            for nombre in ("versionado.py", "suelto.py"):
                with open(os.path.join(tmp, nombre), "w") as f:
                    f.write(largo)
            subprocess.run(["git", "-C", tmp, "add", "versionado.py"], check=True)
            self.assertEqual([h.archivo for h in FuncionesLargas(tmp).validar()], ["versionado.py"])


class LosBloquesSeEncuentranIgual(unittest.TestCase):

    def test_llaves_anidadas(self):
        texto = "f() { a { b } c }"
        self.assertEqual(Bloques.llaves(texto, texto.index("{")), "{ a { b } c }")

    def test_sin_llaves_tras_la_condicion_no_hay_bloque(self):
        self.assertIsNone(Bloques.llaves_tras_condicion("while (x) y();", 6))

    def test_la_sangria_corta_donde_vuelve_el_margen(self):
        lineas = ["for x in y:", "    a", "", "    b", "c"]
        self.assertEqual(Bloques.sangria(lineas, 1, 0), ["    a", "", "    b"])


class CapturasYLogsAvisa(unittest.TestCase):
    """`05·E1` y `05·E5`."""

    def n(self, texto):
        return len(CapturasYLogs(".").revisar_texto(texto))

    def test_capturas_vacias_en_varios_lenguajes(self):
        for texto in ("try { x(); } catch (e) {}", "catch (Exception $e) {\n\n}",
                      "try { a() } catch {  }", "try:\n    x()\nexcept ValueError:\n    pass"):
            self.assertEqual(self.n(texto), 1, texto)

    def test_capturas_con_manejo_no_avisan(self):
        self.assertEqual(self.n("catch (e) { log(e); }"), 0)
        self.assertEqual(self.n("except ValueError:\n    log(e)\n    raise"), 0)

    def test_secretos_en_los_logs(self):
        self.assertEqual(self.n('Log::info("Login", ["email" => $email, "password" => $pass]);'), 1)
        self.assertEqual(self.n("console.log('auth', token)"), 1)
        self.assertEqual(self.n('Log::info("Login ok", ["user_id" => $id]);'), 0)


class ConsultasCostosasAvisa(unittest.TestCase):
    """`06·R1` y `06·R2`."""

    def mensajes(self, texto):
        return [h.mensaje for h in ConsultasCostosas(".").revisar_texto(texto)]

    def test_select_estrella(self):
        self.assertEqual(len(self.mensajes('q = "SELECT * FROM t"')), 1)
        self.assertEqual(len(self.mensajes("select * from t")), 1)
        self.assertEqual(self.mensajes("SELECT id, nombre FROM t"), [])

    def test_consulta_en_bucle(self):
        n1 = lambda t: sum("N+1" in m for m in self.mensajes(t))
        self.assertEqual(n1("foreach ($ids as $id) {\n  $c = Cliente::find($id);\n}"), 1)
        self.assertEqual(n1("for id in ids:\n    c = Cliente.objects.get(pk=id)\n    print(c)"), 1)
        self.assertEqual(n1("foreach ($items as $i) {\n  $total += $i->precio;\n}"), 0)


class InyeccionYSesionAvisa(unittest.TestCase):
    """`04·S3` y `04·S5`."""

    def mensajes(self, texto):
        return [h.mensaje for h in InyeccionYSesion(".").revisar_texto(texto)]

    def test_s3(self):
        self.assertTrue(any("SQL" in m for m in self.mensajes('$q = "SELECT * FROM users WHERE id = " . $id;')))
        self.assertFalse(any("SQL" in m for m in self.mensajes('DB::select("SELECT * FROM users WHERE id = ?", [$id]);')))
        self.assertTrue(any("shell" in m for m in self.mensajes('exec("convert " . $archivo . " out.png");')))
        self.assertTrue(any("masiva" in m for m in self.mensajes("protected $guarded = [];")))
        self.assertTrue(any("payload" in m for m in self.mensajes("User::create($request->all());")))

    def test_s5(self):
        self.assertTrue(any("S5" in m for m in self.mensajes("'http_only' => false,")))
        self.assertFalse(any("S5" in m for m in self.mensajes("'secure' => true,")))


class PruebasAisladasAvisa(unittest.TestCase):
    """`08·T3` y `08·T4`."""

    def test_la_base_de_las_pruebas(self):
        base = PruebasAisladas.motivo_de_la_base
        self.assertIsNone(base('<env name="DB_DATABASE" value=":memory:"/>'))
        self.assertIsNone(base('<env name="DB_DATABASE" value="agro_testing"/>'))
        self.assertIsNotNone(base('<env name="DB_DATABASE" value="agro_produccion"/>'))
        self.assertIsNotNone(base("<phpunit></phpunit>", hay_env_testing=False))
        self.assertIsNone(base("<phpunit></phpunit>", hay_env_testing=True))

    def test_el_orden(self):
        self.assertIsNone(PruebasAisladas.motivo_del_orden('<phpunit executionOrder="random">'))
        self.assertIsNotNone(PruebasAisladas.motivo_del_orden("<phpunit>"))

    def test_el_azar_solo_se_busca_en_las_pruebas(self):
        validador = PruebasAisladas(".")
        self.assertEqual(len(PruebasAisladas.fuentes_de_azar("$x = mt_rand(1, 9);")), 1)
        self.assertEqual(PruebasAisladas.fuentes_de_azar("$x = 5;"), [])
        self.assertTrue(validador.aplica_a("tests/Unit/PagoTest.php"))
        self.assertFalse(validador.aplica_a("app/Pago.php"))


if __name__ == "__main__":
    unittest.main()
