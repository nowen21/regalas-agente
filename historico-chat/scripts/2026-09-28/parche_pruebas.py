import io

p = r"C:\Ing. Jose\ia\agente\validadores\pruebas.py"
crudo = io.open(p, encoding="utf-8", newline="").read()
crlf = "\r\n" in crudo
s = crudo.replace("\r\n", "\n")

a = s.index("class LasReglasQuePideLaSolicitud(unittest.TestCase):")
b = s.index("\nclass ", a + 10)
clase = s[a:b]


def c(viejo, nuevo, todas=False):
    global clase
    assert viejo in clase, viejo[:70]
    clase = clase.replace(viejo, nuevo) if todas else clase.replace(viejo, nuevo, 1)


c('''    tareas: cada regla dice a qué tareas aplica, y las palabras que señalan cada
    tarea están en `base/tareas.md`.''',
  '''    tareas: cada regla dice a qué tareas aplica. Desde la fase `C`
    (`RN-07`), las tareas del mensaje salen solo de la palabra clave de
    `01·C28`: nada se elige adivinando por las demás palabras.''')

c('"haga commit y suba"', '"Suba el commit"', todas=True)
c('"aplique las reglas de la caja de reglas de redacción al readme"',
  '"Escriba el readme con la caja de reglas de redacción"', todas=True)
c('"cree el pendiente del H2"', '"Registre el pendiente del H2"', todas=True)
c('"cambie el código del validador y corra las pruebas"',
  '"Verifique las pruebas del validador"')
c('''            "borre los registros de producción y corra las pruebas",''',
  '''            "Suba el commit. Verifique las pruebas",''', todas=True)
c('''                        "borre los registros de producción",''',
  '''                        "Suba el commit. Verifique las pruebas",''')

c('''    def test_borrar_en_produccion_trae_las_tres_que_lo_gobiernan(self):
        ids = [i for i, _ in recuperar.elegir(
            "borre los registros de producción", comun.RAIZ)[0]]
        for id in ("N4", "N5", "N7"):
            self.assertIn(id, ids, f"faltó {id} en un pedido destructivo")''',
  '''    def test_borrar_en_produccion_trae_las_tres_que_lo_gobiernan(self):
        """Desde la fase `C` la tarea de datos no sale de las palabras del
        mensaje sino de la acción: el comando que toca la base. Su archivo de
        reglas trae completas las tres blindadas que la gobiernan."""
        import leidas
        tareas = leidas.tareas_de_la_accion(
            "Bash", {"command": 'mysql -e "DELETE FROM registros"'}, comun.RAIZ)
        self.assertIn("tocar-datos", tareas)
        texto = "".join(comun.leer(r) for r in leidas.archivos(["tocar-datos"]))
        for id in ("N4", "N5", "N7"):
            self.assertIn("## " + id + " ·", texto, f"faltó {id} en la tarea de datos")''')

c('''        proyecto = self._con_opt_in(apagados=("21",))
        ids = [i for i, _ in recuperar.elegir("prueba", comun.RAIZ,
                                              proyecto=proyecto)[0]]
        self.assertNotIn("AU6", ids)
        self.assertIn("T1", ids, "se llevó también las que sí rigen")''',
  '''        proyecto = self._con_opt_in(apagados=("21",))
        idx = recuperar.indice(comun.RAIZ)
        elegidas, descartadas, siempre = recuperar.elegir(
            "Escriba el documento", comun.RAIZ, proyecto=proyecto)
        todas = [i for i, _ in elegidas] + descartadas
        self.assertFalse([i for i in todas if idx[i].capitulo == "21"])
        self.assertIn("ID8", todas + siempre, "se llevó también las que sí rigen")''')

c('''        idx = recuperar.indice(comun.RAIZ)
        ids = [i for i, _ in recuperar.elegir("prueba", comun.RAIZ,
                                              proyecto=proyecto)[0]]
        self.assertTrue(any(idx[i].capitulo == "21" for i in ids),
                        "apagó un capítulo que el proyecto encendió")''',
  '''        idx = recuperar.indice(comun.RAIZ)
        elegidas, descartadas, _s = recuperar.elegir(
            "Escriba el documento", comun.RAIZ, proyecto=proyecto)
        todas = [i for i, _ in elegidas] + descartadas
        self.assertTrue(any(idx[i].capitulo == "21" for i in todas),
                        "apagó un capítulo que el proyecto encendió")''')

c('''        self.assertIn("F23", [i for i, _ in elegidas])''',
  '''        self.assertIn("F23", [i for i, _ in elegidas] + _d)''')

clase += '''
    # `EP-005·HU-023·CA-08` · Nada se elige adivinando.
    def test_solo_la_palabra_clave_elige_la_tarea(self):
        """Mensajes reales del 2026-09-28 que trajeron reglas de más."""
        for mensaje in ("es sencillo debe entender las reglas no lo que le parezca",
                        "como así que entendió que yo quería cambiar el estándar?",
                        "termine la fase D"):
            self.assertEqual({}, recuperar.tareas_del_mensaje(mensaje, comun.RAIZ),
                             f"«{mensaje}» eligió una tarea sin palabra clave")
        self.assertEqual({"tocar-git"}, set(recuperar.tareas_del_mensaje("Suba", comun.RAIZ)))
        self.assertEqual({"escribir-documento"},
                         set(recuperar.tareas_del_mensaje("Escriba el plan del estándar", comun.RAIZ)))
        self.assertEqual({"trabajar-cadena"},
                         set(recuperar.tareas_del_mensaje("Apruebo los dos planes. Hágalo", comun.RAIZ)))

    def test_la_palabra_clave_cuenta_solo_al_abrir_una_frase(self):
        """«que suba todo» no es un pedido de subir: `01·C28` dice que la
        palabra abre el pedido."""
        self.assertEqual({}, recuperar.tareas_del_mensaje("dijo que suba todo", comun.RAIZ))
        self.assertIn("tocar-git",
                      recuperar.tareas_del_mensaje("Listo. Suba todo", comun.RAIZ))

    def test_lo_que_no_cupo_dice_en_que_archivo_esta_completo(self):
        texto = recuperar.como_texto("Suba el commit. Verifique las pruebas",
                                     comun.RAIZ, tope=6000)
        self.assertIn("reglas-por-tarea/correr-comando.md", texto)
'''

s = s[:a] + clase + s[b:]
if crlf:
    s = s.replace("\n", "\r\n")
io.open(p, "w", encoding="utf-8", newline="").write(s)
print("ok")
