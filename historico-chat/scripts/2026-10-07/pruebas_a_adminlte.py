# -*- coding: utf-8 -*-
"""EP-028·HU-007 · Pone al día con AdminLTE las pruebas que buscaban rastros de Tabler,
y la tabla que arma presentar.py. Se corre desde proyectos/cimiento."""
CAMBIOS = {
    "core/inicio/tests_tablas.py": [('"libs/list.js/dist/list.min.js"', '"list.js"')],
    "core/estandar/tests_vista_estandar.py": [
        ("def test_ejemplo_en_tarjetas_tabla_de_tabler_y_sin_marcas", "def test_ejemplo_en_tarjetas_tabla_de_la_plantilla_y_sin_marcas"),
        ('self.assertIn("border-danger", pagina)', 'self.assertIn("card-danger", pagina)'),
        ('self.assertIn("border-success", pagina)', 'self.assertIn("card-success", pagina)'),
        ("'<table class=\"table table-vcenter card-table\">'", "'<table class=\"table align-middle mb-0\">'")],
    "core/estandar/presentar.py": [('<table class="table table-vcenter card-table">', '<table class="table align-middle mb-0">')],
    "core/inicio/tests.py": [
        ('ESTATICOS = ("css/tabler.min.css", "js/tabler.min.js", "htmx.min.js", "apexcharts.min.js")',
         'ESTATICOS = ("css/adminlte.min.css", "js/adminlte.min.js", "js/bootstrap.bundle.min.js", "bootstrap-icons.min.css",\n             "list.js", "htmx.min.js", "apexcharts.min.js")'),
        ('self.assertContains(respuesta, "navbar-vertical")', 'self.assertContains(respuesta, "app-sidebar")')],
    "core/inicio/tests_menu.py": [
        ("""'dropdown-item active" href="%s"'""", """'nav-link active" href="%s"'"""),
        ("""'ms-auto">3</span>'""", """'text-bg-danger me-3">3</span>'""")],
    "core/consumo/tests_tablero.py": [('"Gasto de tokens</span>"', '"Gasto de tokens</p>"')],
}
for ruta, pares in CAMBIOS.items():
    texto = open(ruta, encoding="utf-8").read()
    for viejo, nuevo in pares:
        print(ruta, texto.count(viejo))
        texto = texto.replace(viejo, nuevo)
    open(ruta, "w", encoding="utf-8").write(texto)
