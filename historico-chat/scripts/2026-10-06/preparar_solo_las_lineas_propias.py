"""Prepara para el commit solo algunas líneas nuevas de un archivo que otras sesiones también cambiaron.

Uso: python preparar_solo_las_lineas_propias.py <archivo> <texto que identifica la línea> [...]

Toma el archivo como está en el último commit, le suma solo las líneas de la copia
de trabajo que contienen alguno de los textos dados (en el mismo puesto, después de
la línea que las antecede) y deja ese contenido en el área de preparación. La copia
de trabajo no se toca: las líneas de las otras sesiones siguen ahí, sin preparar.
"""
import subprocess
import sys

archivo, marcas = sys.argv[1], sys.argv[2:]
base = subprocess.run(["git", "show", "HEAD:" + archivo], capture_output=True, check=True).stdout.decode("utf-8").splitlines()
with open(archivo, encoding="utf-8") as f:
    trabajo = f.read().splitlines()

resultado = list(base)
for i, linea in enumerate(trabajo):
    if any(m in linea for m in marcas) and linea not in resultado:
        anterior = trabajo[i - 1] if i else None
        puesto = resultado.index(anterior) + 1 if anterior in resultado else len(resultado)
        resultado.insert(puesto, linea)
        print("preparada:", linea[:100])

contenido = ("\n".join(resultado) + "\n").encode("utf-8")
blob = subprocess.run(["git", "hash-object", "-w", "--stdin"], input=contenido, capture_output=True, check=True).stdout.decode().strip()
subprocess.run(["git", "update-index", "--cacheinfo", "100644,%s,%s" % (blob, archivo)], check=True)
