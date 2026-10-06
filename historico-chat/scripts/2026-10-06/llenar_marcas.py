# -*- coding: utf-8 -*-
"""Llena, en orden, las marcas «…» que deja la primera pasada de `manage.py cerrar_fase`.

    python llenar_marcas.py «archivo.md» «valores.txt»

`valores.txt` trae un valor por línea, en el orden en que aparecen las marcas.
Cada línea reemplaza la primera marca que quede. Si sobran o faltan valores, no
escribe nada y dice cuántos esperaba.
"""
import sys

MARCA = "«…»"
VERDICTO = "«se llena al cerrar»"


def main(archivo, valores):
    with open(archivo, encoding="utf-8") as f:
        texto = f.read()
    with open(valores, encoding="utf-8") as f:
        lineas = [l.rstrip("\n") for l in f if l.strip()]
    marcas = texto.count(MARCA) + texto.count(VERDICTO)
    if marcas != len(lineas):
        print("no se escribe: hay %d marcas y %d valores" % (marcas, len(lineas)))
        return 1
    for valor in lineas:
        i, j = texto.find(MARCA), texto.find(VERDICTO)
        if j >= 0 and (i < 0 or j < i):
            texto = texto[:j] + valor + texto[j + len(VERDICTO):]
        else:
            texto = texto[:i] + valor + texto[i + len(MARCA):]
    with open(archivo, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)
    print("llenas %d marcas en %s" % (len(lineas), archivo))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
