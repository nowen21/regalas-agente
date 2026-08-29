# -*- coding: utf-8 -*-
"""Los 67 archivos en UN proceso: cuantos fallan por rojo y cuantos por estorbarse.

Corridos uno por uno son 61 verdes y 6 rojos. La pregunta que decide como se
arregla: si se cargan todos juntos, ?siguen siendo 6? Si aparecen mas, es que se
pisan entre ellos ---cambian de carpeta, parchan modulos--- y entonces el
corredor tiene que darle a cada archivo su propio proceso, no juntarlos.

Se carga cada modulo por su ruta, sin `discover`, para no depender de que la
carpeta sea un paquete.
"""
import importlib.util
import io
import os
import sys
import unittest

RAIZ = r"c:\Ing. Jose\ia\agente"
CARPETA = os.path.join(RAIZ, "validadores", "tests")
sys.path.insert(0, os.path.join(RAIZ, "validadores"))
os.chdir(os.path.join(RAIZ, "validadores"))

suite = unittest.TestSuite()
cargador = unittest.TestLoader()
no_cargan = []
for nombre in sorted(n for n in os.listdir(CARPETA) if n.endswith(".py")):
    ruta = os.path.join(CARPETA, nombre)
    spec = importlib.util.spec_from_file_location("t_" + nombre[:-3], ruta)
    modulo = importlib.util.module_from_spec(spec)
    try:
        sys.modules[spec.name] = modulo
        spec.loader.exec_module(modulo)
    except Exception as e:                                  # noqa: BLE001
        no_cargan.append((nombre, repr(e)[:70]))
        continue
    suite.addTests(cargador.loadTestsFromModule(modulo))

# Sin `TextTestRunner`: al imprimir la lista de fallas revienta por
# codificacion en la consola de Windows, y se lleva la medicion (`S-060`).
r = unittest.TestResult()
_salida = sys.stdout
sys.stdout = io.open(os.devnull, "w", encoding="utf-8")
try:
    suite.run(r)
finally:
    sys.stdout.close()
    sys.stdout = _salida

print("Modulos que no cargan: %d" % len(no_cargan))
for n, e in no_cargan:
    print("   %-56s %s" % (n, e))
print("")
print("Pruebas: %d   fallas: %d   errores: %d" %
      (r.testsRun, len(r.failures), len(r.errors)))
print("")
print("Corridos uno por uno: 6 archivos en rojo. Los archivos que fallan aca:")
vistos = []
for caso, _ in list(r.failures) + list(r.errors):
    origen = getattr(caso, "__module__", "?")
    if origen not in vistos:
        vistos.append(origen)
for v in sorted(vistos):
    print("   %s" % v)
print("")
print("Si esta lista tiene mas de 6 nombres, se estorban entre ellos y cada")
print("archivo necesita su propio proceso.")
