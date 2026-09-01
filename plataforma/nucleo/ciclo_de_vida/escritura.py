# -*- coding: utf-8 -*-
"""Escribir en el lugar de un hueco, **sin tocar nada más del documento**.

Es lo que decide si la funcionalidad sirve. Un guardado que reformatea obliga a
revisar el archivo entero cada vez, y entonces conviene más abrir el editor.

**Tres cuidados, y ninguno es opcional:**

- **Los finales de línea se conservan tal como están.** Se lee y se escribe sin
  que Python los traduzca. Traducirlos cambiaría cada renglón del archivo, que
  es exactamente lo que el criterio prohíbe, y no se vería mirando el texto.
- **El archivo nunca queda a medias.** Se escribe completo al lado y se pone en
  su sitio de un golpe: o está el de antes o está el de después.
- **No se escribe a ciegas en una posición.** Se comprueba que la línea siga
  diciendo lo mismo. Si el documento se movió, ahí ya vive otra cosa.
"""
import hashlib
import io
import os


class SeMovio(Exception):
    """El documento cambió, y donde iba el hueco ya hay otra cosa."""


class CambioAjeno(Exception):
    """Alguien más escribió en el archivo desde que se leyó."""


def huella(texto):
    """La huella del contenido, para saber si alguien más lo tocó."""
    return hashlib.sha256((texto or "").encode("utf-8")).hexdigest()


def leer_tal_cual(ruta):
    """El texto del archivo **sin traducir los finales de línea**.

    Con la lectura normal, un archivo con finales de Windows llega con finales
    de Unix, y al guardarlo cambiarían **todos** los renglones. El criterio que
    esta pieza tiene que cumplir es que no cambie nada fuera del hueco.
    """
    with io.open(ruta, encoding="utf-8", newline="") as archivo:
        return archivo.read()


def reemplazar(texto, hueco, con):
    """El texto con ese hueco reemplazado, y nada más cambiado.

    `hueco` es uno de los que devuelve `huecos.encontrar`: trae la línea, la
    columna, la marca y el contexto. Los cuatro se comprueban antes de escribir.
    """
    if not con:
        raise ValueError(
            "Llenar con nada dejaría el documento peor: la marca desaparece y "
            "ya no se ve que falta.")

    lineas = texto.split("\n")
    numero = hueco["linea"]
    if numero < 1 or numero > len(lineas):
        raise SeMovio("El documento ya no tiene la línea %d." % numero)

    linea = lineas[numero - 1]
    desde = hueco["columna"] - 1
    marca = hueco["marca"]

    if linea[desde:desde + len(marca)] != marca:
        raise SeMovio(
            "En la línea %d, columna %d ya no está «%s». El documento se movió."
            % (numero, hueco["columna"], marca))
    if linea.strip() != hueco["contexto"]:
        raise SeMovio(
            "La línea %d ya no dice lo mismo que cuando se leyó. Escribir ahí "
            "sería escribir sobre lo que no era." % numero)

    lineas[numero - 1] = linea[:desde] + con + linea[desde + len(marca):]
    return "\n".join(lineas)


def guardar_de_un_golpe(ruta, texto):
    """Escribe el texto sin dejar el archivo a medias si algo se interrumpe.

    Se escribe completo en un archivo al lado, en la misma carpeta —tiene que
    ser el mismo disco para que ponerlo en su sitio sea un solo paso—, y
    después se pone en el lugar del original.
    """
    carpeta = os.path.dirname(ruta) or "."
    al_lado = os.path.join(carpeta, "." + os.path.basename(ruta) + ".escribiendo")
    with io.open(al_lado, "w", encoding="utf-8", newline="") as archivo:
        archivo.write(texto)
    os.replace(al_lado, ruta)


def llenar_el_hueco(ruta, hueco, con, huella_de_cuando_se_leyo=""):
    """Lee, comprueba, reemplaza y guarda. Devuelve la huella de lo escrito.

    Si `huella_de_cuando_se_leyo` viene y no coincide, **no se escribe**: entre
    la lectura y ahora alguien más cambió el archivo, y pisarlo perdería su
    trabajo. Adivinar cuál de los dos cambios vale no es del programa.
    """
    antes = leer_tal_cual(ruta)
    if huella_de_cuando_se_leyo and huella(antes) != huella_de_cuando_se_leyo:
        raise CambioAjeno(
            "El archivo cambió desde que se leyó. No se escribió nada: revise "
            "qué cambió y vuelva a pedir qué le falta.")
    despues = reemplazar(antes, hueco, con)
    guardar_de_un_golpe(ruta, despues)
    return huella(despues)
