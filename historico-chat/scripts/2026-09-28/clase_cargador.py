class RepartoDeLasReglas(unittest.TestCase):
    """Qué le dice el arranque al agente sobre las reglas.

    Hasta la 39.3.1 el arranque mandaba `00` y `01` enteros, y no cabían en el
    canal de la herramienta: 10.000 caracteres por enganche. Desde la 39.4.0
    las reglas llegan con cada mensaje y el arranque solo dice cómo
    (`EP-005 · HU-009 · CA-04`).
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

    def test_dice_como_llegan_las_reglas(self):
        raiz = self._base("00-nucleo.md", "05-tema/base.md")
        texto = cargador.contexto(raiz)
        self.assertIn("LLEGAN CON CADA MENSAJE", texto)
        self.assertIn("base/mapa-de-tareas.md", texto)
        self.assertIn("`01·C28`", texto)

    def test_no_manda_el_texto_de_ninguna_regla(self):
        raiz = self._base("00-nucleo.md", "01-conducta.md", "05-tema/base.md")
        texto = cargador.contexto(raiz)
        for nombre in ("00-nucleo.md", "01-conducta.md", "05-tema/base.md"):
            self.assertNotIn(f"Cuerpo de {nombre}", texto, nombre)

    def test_sin_carpeta_base_no_entrega_nada(self):
        raiz = tempfile.mkdtemp()
        self.assertEqual(cargador.contexto(raiz), "")
        self.assertEqual(os.listdir(raiz), [])

    def test_con_base_vacia_no_entrega_nada(self):
        raiz = tempfile.mkdtemp()
        os.makedirs(os.path.join(raiz, "base"))
        self.assertEqual(cargador.contexto(raiz), "")

    def test_sin_pasar_el_gate_entrega_solo_esa_regla(self):
        raiz = self._base("00-nucleo.md", cargador.GATE)
        texto = cargador.contexto(raiz, gate_ok=False)
        self.assertIn("ARRANQUE DETENIDO", texto)
        self.assertIn(f"Cuerpo de {cargador.GATE}", texto)
        self.assertNotIn("LLEGAN CON CADA MENSAJE", texto)

    def test_lo_de_este_repositorio_es_corto(self):
        """Deja espacio en el canal para la memoria y el histórico."""
        texto = cargador.contexto(comun.RAIZ)
        if not texto:
            self.skipTest("sin base/ en la raíz de la corrida")
        self.assertLess(len(texto), 1000)
        for ruta in ("base/mapa-de-tareas.md",
                     "base/01-conducta/palabras-clave.md",
                     "base/00-nucleo-blindado.md"):
            self.assertTrue(os.path.isfile(os.path.join(comun.RAIZ, ruta)), ruta)


