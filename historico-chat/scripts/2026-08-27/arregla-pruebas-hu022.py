# -*- coding: utf-8 -*-
"""Dos arreglos en las pruebas de la HU-022, encontrados al correrlas.

1. La prueba «no hay una lista de marcadores en el codigo» buscaba el texto en
   `fases.py`, y **fallo por un comentario que cita un marcador para
   explicarse**. Se cambia por una de comportamiento: sin ninguna plantilla no
   puede quedar nada con que comparar.

2. Ocho `io.open(...).read()` dejaban el archivo abierto y llenaban la corrida
   de ResourceWarning. Se cambian por un ayudante con `with`.
"""
import io

F = r"c:\Ing. Jose\ia\agente\validadores\pruebas.py"
t = io.open(F, encoding="utf-8").read()

viejo = '''    def test_no_hay_una_lista_de_marcadores_escrita_a_mano(self):
        """El defecto que se corrigi\u00f3 con el vocabulario de estados."""
        codigo = comun.leer(os.path.join(self.RAIZ, "validadores", "fases.py"))
        cuerpo = codigo.split("MOLDES_DEL_CICLO", 1)[1]
        self.assertNotIn("l\u00edneas en lenguaje claro", cuerpo,
                         "hay marcadores de plantilla copiados en el c\u00f3digo")'''

nuevo = '''    def test_sin_ninguna_plantilla_no_queda_ninguna_lista_de_reserva(self):
        """Que no haya marcadores copiados en el c\u00f3digo, comprobado corriendo.

        Buscar el texto en `fases.py` no sirve: los comentarios citan
        marcadores para explicarse, y una prueba as\u00ed se rompe al documentar
        —pas\u00f3 en la primera corrida—. **Se comprueba por comportamiento:**
        sin ninguna plantilla no puede quedar nada con qu\u00e9 comparar.
        """
        raiz, fase = self._proyecto({})
        moldes = os.path.join(raiz, *fases.MOLDES_DEL_CICLO.split("/"))
        for nombre in os.listdir(moldes):
            os.remove(os.path.join(moldes, nombre))
        self.assertEqual(fases.marcadores_de_los_moldes(raiz), {},
                         "quedaron marcadores que no salieron de una plantilla")
        self._escribir(os.path.join(fase, "plan_pruebas.md"),
                       "| Fase | \u00abA-EP01-HU03-Descripci\u00f3n\u00bb |\\n"
                       "| M\u00f3dulo | \u00abM\u00bb |\\n| Fecha | AAAA-MM-DD |\\n")
        self.assertEqual(fases.inventario(raiz), (1, 1, 0))
        self.assertEqual(fases.documentos_que_siguen_siendo_el_molde(raiz), [])'''

assert viejo in t
t = t.replace(viejo, nuevo, 1)

# Dos ayudantes que cierran lo que abren.
ancla = '''    def _proyecto(self, cuerpos, plantillas=None):'''
ayudantes = '''    def _texto(self, ruta):
        with io.open(ruta, encoding="utf-8") as f:
            return f.read()

    def _escribir(self, ruta, texto):
        with io.open(ruta, "w", encoding="utf-8", newline="\\n") as f:
            f.write(texto)

    def _molde(self, raiz, nombre):
        return self._texto(os.path.join(
            raiz, *fases.MOLDES_DEL_CICLO.split("/"), nombre))

''' + ancla
assert ancla in t
t = t.replace(ancla, ayudantes, 1)

# Los ocho `io.open(...).read()` de esta clase.
cambios = [
    ('''        molde = io.open(os.path.join(raiz, *fases.MOLDES_DEL_CICLO.split("/"),
                                     "08-plan-pruebas.md"),
                        encoding="utf-8").read()''',
     '''        molde = self._molde(raiz, "08-plan-pruebas.md")'''),
    ('''        molde = io.open(os.path.join(raiz, *fases.MOLDES_DEL_CICLO.split("/"),
                                     "10-estado-fase.md"),
                        encoding="utf-8").read()''',
     '''        molde = self._molde(raiz, "10-estado-fase.md")'''),
    ('''        antes = io.open(ruta, encoding="utf-8").read()
        fases.validar(raiz)
        self.assertEqual(io.open(ruta, encoding="utf-8").read(), antes)''',
     '''        antes = self._texto(ruta)
        fases.validar(raiz)
        self.assertEqual(self._texto(ruta), antes)'''),
]
for v, n in cambios:
    if v not in t:
        print("AVISO: no se encontro un bloque; revisar")
    t = t.replace(v, n)

io.open(F, "w", encoding="utf-8", newline="\n").write(t)
print("pruebas arregladas")
