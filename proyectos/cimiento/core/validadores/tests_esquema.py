"""Los validadores de migraciones y esquema, como clases.

Las pruebas de esquema, migraciones y entidades son las que tenían en
`validadores/pruebas.py` y `validadores/tests/`, pasadas a su clase. Las de
estructura y declaración son nuevas: antes no tenían.
"""
import io
import os
import subprocess
import tempfile
import unittest

from core.comun import FALLA, Archivos, Proyecto
from core.validadores import (ConvencionDeNombres, DeclaracionDelProyecto, IntegridadDeEsquema,
                              MigracionesReversibles, TablasDeDominio)
from core.validadores.declaracion import Declaracion
from core.validadores.migraciones import RecorridoDeMigraciones

DOMINIO = """## Entidades
| Entidad | Tabla | Clave natural | Inmutable |
|---|---|---|---|
| Factura | facturas | numero | sí |
| Cliente | clientes | documento | no |

## Módulos
| Módulo | Carpeta | Especificación |
|---|---|---|
| Ventas | app/Modules/Ventas | docs/ventas.md |
| Compras | | |
"""

MAPEO = """| Clave | Valor |
|---|---|
| `modulos.ruta` | `app/Modules/<modulo>` |
| `tablas.caso` | `snake_case` |
| `clases.caso` | `PascalCase` |
| `fk.sufijo` | `_id` |
| `inmutables.permiso` | `anular_<recurso>` |
| `legacy.ignorar` | `legacy/` |
| `columnas.caso` | `libre` |
"""


class ProyectoDePrueba:
    """Un repositorio git de mentira con los archivos dados, todos versionados."""

    def __init__(self, archivos):
        self.tmp = tempfile.TemporaryDirectory()
        self.raiz = self.tmp.name
        subprocess.run(["git", "init", "-q", self.raiz], check=True, capture_output=True)
        for relativa, texto in archivos.items():
            ruta = os.path.join(self.raiz, *relativa.split("/"))
            os.makedirs(os.path.dirname(ruta), exist_ok=True)
            with io.open(ruta, "w", encoding="utf-8") as f:
                f.write(texto)
        subprocess.run(["git", "-C", self.raiz, "add", "-A"], check=True, capture_output=True)

    def __enter__(self):
        return self.raiz

    def __exit__(self, *_):
        self.tmp.cleanup()


class IntegridadDeEsquemaAvisa(unittest.TestCase):
    """`03·D1`, `03·D3` y `14·EST2`."""

    def motivos(self, ruta, texto):
        return [m for _, m in IntegridadDeEsquema.revisar(ruta, texto)]

    def test_d1_claves_foraneas(self):
        self.assertEqual(len(self.motivos("m.php", "$table->foreignId('user_id')->constrained();")), 1)
        self.assertEqual(self.motivos("m.php", "$table->foreign('user_id')->references('id')->on('u')->onDelete('cascade');"), [])
        self.assertEqual(self.motivos("m.php", "$table->foreignId('user_id')->constrained()->cascadeOnDelete();"), [])
        self.assertEqual(len(self.motivos("m.sql", "FOREIGN KEY (user_id) REFERENCES users(id)")), 1)
        self.assertEqual(self.motivos("m.sql", "FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE"), [])

    def test_una_sentencia_un_hallazgo(self):
        self.assertEqual(len(self.motivos("m.php", "$table->foreignId('u')->constrained('users');")), 1)

    def test_d3_solo_en_un_alter(self):
        d3 = lambda ruta, texto: any("D3" in m for m in self.motivos(ruta, texto))
        self.assertTrue(d3("m.php", "Schema::table('users', function (Blueprint $table) {\n  $table->string('nit');\n});"))
        self.assertFalse(d3("m.php", "Schema::table('users', function ($t) {\n  $t->string('nit')->default('');\n});"))
        self.assertFalse(d3("m.php", "Schema::create('t', function ($t) {\n  $t->string('nit');\n});"))
        self.assertTrue(d3("m.sql", "ALTER TABLE users ADD COLUMN nit VARCHAR(20) NOT NULL;"))

    def test_est2_identificador_muy_largo(self):
        largo = "x" + "a" * 70
        self.assertTrue(any("EST2" in m for m in self.motivos("m.php", "$table->boolean('%s');" % largo)))


class MigracionesReversiblesAvisa(unittest.TestCase):
    """`03·D2`."""

    def test_cada_convencion(self):
        motivo = MigracionesReversibles.motivo
        self.assertIsNotNone(motivo("database/migrations/2024_x.php", "class X extends Migration {\n  public function up() {}\n}"))
        self.assertIsNone(motivo("database/migrations/2024_x.php", "public function up() {}\n  public function down() {}"))
        self.assertIsNotNone(motivo("alembic/versions/ab12.py", "revision = 'ab12'\ndef upgrade():\n    pass"))
        self.assertIsNotNone(motivo("app/migrations/0002_x.py", "from django.db import migrations\n"
                                    "operations = [migrations.RunPython(poblar)]"))
        self.assertIsNone(motivo("app/migrations/0003_x.py", "from django.db import migrations, models\n"
                                 "operations = [migrations.AddField('t', 'c', models.IntegerField())]"))
        self.assertIsNone(motivo("db/migrate/2024_x.rb", "class X < ActiveRecord::Migration[7.0]\n  def change\n  end\nend"))
        self.assertIsNotNone(motivo("migrations/2024_x.js", "exports.up = (knex) => knex.schema.createTable('t')"))

    def test_los_pares_sql(self):
        motivo = MigracionesReversibles.motivo
        self.assertIsNotNone(motivo("migrations/001_init.up.sql", "CREATE TABLE t;", {"001_init.up.sql"}))
        self.assertIsNone(motivo("migrations/001_init.up.sql", "CREATE TABLE t;", {"001_init.up.sql", "001_init.down.sql"}))

    def test_las_candidatas_sin_suponer_el_marco(self):
        es = RecorridoDeMigraciones.es_candidata
        for ruta in ("database/migrations/x.php", "app/migrations/0001.py", "db/migrate/x.rb", "m/001.up.sql"):
            self.assertTrue(es(ruta), ruta)
        for ruta in ("vendor/pkg/migrations/x.php", "app/Models/User.php"):
            self.assertFalse(es(ruta), ruta)


class LaDeclaracionSeLeeYSeDice(unittest.TestCase):

    def test_se_lee_lo_declarado_y_libre_no_cuenta(self):
        with ProyectoDePrueba({".agente/dominio.md": DOMINIO, ".agente/mapeo-nombres.md": MAPEO}) as raiz:
            d = Declaracion.leer(Proyecto(raiz), Archivos())
        self.assertEqual(d.convencion("tablas.caso"), "snake_case")
        self.assertEqual(d.convencion("columnas.caso"), "")
        self.assertEqual([e.nombre for e in d.inmutables()], ["Factura"])
        self.assertEqual([m.nombre for m in d.modulos], ["Ventas", "Compras"])
        self.assertTrue(d.ignorado("legacy/viejo.php"))

    def test_lo_que_falta_se_avisa_sin_fallar(self):
        with ProyectoDePrueba({"README.md": "# x\n"}) as raiz:
            hallazgos = DeclaracionDelProyecto(raiz).validar()
        self.assertTrue(any("no existe `.agente/dominio.md`" in h.mensaje for h in hallazgos))
        self.assertEqual([h for h in hallazgos if h.severidad == FALLA], [])


class ConvencionDeNombresAvisa(unittest.TestCase):
    """`14·EST1` y `14·EST2`."""

    def test_modulos_y_nombres_contra_lo_declarado(self):
        archivos = {
            ".agente/dominio.md": DOMINIO, ".agente/mapeo-nombres.md": MAPEO,
            "app/Modules/Ventas/Factura.php": "<?php\nclass factura_mala {}\nclass Factura {}\n",
            "app/Modules/Inventario/x.php": "<?php\n",
            "legacy/viejo.php": "<?php\nclass otro_malo {}\n",
            "database/migrations/2024_t.php": "<?php\nSchema::create('MalaTabla', function ($t) {\n"
                                              "  $t->foreignId('cliente');\n});\n",
        }
        with ProyectoDePrueba(archivos) as raiz:
            mensajes = " | ".join(h.mensaje for h in ConvencionDeNombres(raiz).validar())
        self.assertIn("`Compras` está declarado pero no tiene código", mensajes)
        self.assertIn("app/Modules/Inventario", mensajes)
        self.assertIn("la clase `factura_mala` no sigue `PascalCase`", mensajes)
        self.assertNotIn("otro_malo", mensajes)                     # legacy no se mira
        self.assertIn("la tabla `MalaTabla` no sigue `snake_case`", mensajes)
        self.assertIn("`MalaTabla.cliente` no termina en `_id`", mensajes)

    def test_sin_declaracion_lo_dice_una_vez(self):
        with ProyectoDePrueba({"README.md": "# x\n"}) as raiz:
            hallazgos = ConvencionDeNombres(raiz).validar()
        self.assertEqual(len(hallazgos), 1)

    def test_un_caso_que_no_se_conoce_no_acusa(self):
        self.assertTrue(ConvencionDeNombres.cumple_caso("lo_que_sea", "Inventado"))


class TablasDeDominioAvisa(unittest.TestCase):
    """`03·D1`, `15·IM2` y `15·IM5`; incluye el caso de las migraciones ilegibles (2026-08-18)."""

    def proyecto(self, migracion, contenido="-- nada\n", extra=None):
        archivos = {".agente/dominio.md": DOMINIO, migracion: contenido}
        archivos.update(extra or {})
        return ProyectoDePrueba(archivos)

    def test_con_migraciones_ilegibles_sale_un_solo_aviso_que_no_acusa(self):
        with self.proyecto("database/migrations/0001_initial.py", "# migración\n") as raiz:
            hallazgos = TablasDeDominio(raiz).validar()
        self.assertEqual(len(hallazgos), 1)
        self.assertIn("No es que falten", hallazgos[0].mensaje)
        self.assertNotIn("ninguna migración la crea", hallazgos[0].mensaje)

    def test_con_migraciones_legibles_la_tabla_que_falta_se_reporta(self):
        with self.proyecto("database/migrations/0001_crear.sql",
                           "CREATE TABLE clientes (id INT, documento VARCHAR(20));\n") as raiz:
            mensajes = " ".join(h.mensaje for h in TablasDeDominio(raiz).validar())
        self.assertIn("facturas", mensajes)
        self.assertNotIn("no se pueden mirar", mensajes)

    def test_sin_ninguna_migracion_tampoco_se_calla(self):
        with self.proyecto("README.md", "# proyecto\n") as raiz:
            mensajes = " ".join(h.mensaje for h in TablasDeDominio(raiz).validar())
        self.assertIn("ninguna migración la crea", mensajes)

    def test_el_permiso_de_anular_se_encuentra_cuando_esta(self):
        with self.proyecto("src/ventas/permisos.py", 'PERMISOS = ["anular_factura"]\n') as raiz:
            validador = TablasDeDominio(raiz)
            d = Declaracion.leer(validador.proyecto, validador.archivos)
            self.assertIn("factura", validador.recursos_con_permiso("anular_<recurso>", d))
            self.assertEqual(set(), validador.recursos_con_permiso("anular_factura", d))


if __name__ == "__main__":
    unittest.main()
