# -*- coding: utf-8 -*-
"""Los espacios por llenar de un documento, y cuál de ellos es cierto.

**Solo una clase de marca es un hueco seguro:** `«…»`, la convención que fija
`13·DOC19`. Las otras se parecen y no lo son, y por eso se separan.

**Por qué el hueco con nombre no cuenta.** En un documento ya escrito, `«ROL»`
no se distingue de una cita: acá se cita con esas mismas comillas todo el
tiempo. Se midió el 2026-09-01 sobre las 130 historias de usuario reales del
repositorio:

- 341 marcas `«...»` en total.
- 75 de ellas también están en el molde de la historia.
- **Ninguna** sigue en la línea del molde: son el autor usando el vocabulario
  del molde como etiqueta, y no huecos sin llenar.

Contarlas daría por incompleto un documento bien escrito, que es el mismo error
que una vez dio 559 documentos incompletos donde había 31.

**Se listan igual, aparte.** Cuando la plataforma cree documentos desde el molde
—`F-011`, de la versión 5— el documento **será** el molde, y entonces cada hueco
con nombre sí es cierto. Dejarlos listados evita rehacer esta pieza.

**Y una tercera clase que no se le pregunta a nadie:** `«RUTA-ESTANDAR»`, que la
reemplaza la instalación. Sin apartarla, un molde le pide al usuario 134 cosas
que él no responde. Se cuenta aparte, porque borrarla en silencio es perder en
silencio con otro nombre.
"""
import re

# La marca de la casa, y la única cierta.
MARCA_CIERTA = u"«…»"

# La que llena la instalación, no el usuario.
MARCA_DE_INSTALACION = u"«RUTA-ESTANDAR»"

CIERTO = "cierto"
POSIBLE = "posible"
INSTALACION = "instalación"

# Cualquier marca entre comillas angulares, sin pasar de renglón. El límite de
# largo evita que dos comillas lejanas de un párrafo se tomen por una marca.
_MARCA = re.compile(u"«[^»\n]{0,120}»")

# El principio o el final de un bloque cercado. Lo que va adentro es un ejemplo,
# y una marca ahí se escribe **para que se vea**, no para llenarla.
_CERCA = re.compile(r"^\s*(```|~~~)")


def _lineas_en_codigo(texto):
    """Los números de línea que caen dentro de un bloque cercado."""
    dentro = False
    adentro = set()
    for numero, linea in enumerate((texto or "").split("\n"), 1):
        if _CERCA.match(linea):
            dentro = not dentro
            adentro.add(numero)
            continue
        if dentro:
            adentro.add(numero)
    return adentro


def marcas_del_molde(texto_del_molde):
    """Las marcas con nombre que trae un molde, para reconocer las posibles."""
    return set(_MARCA.findall(texto_del_molde or ""))


def encontrar(texto, del_molde=()):
    """Los huecos de un texto, cada uno con su clase y su ubicación.

    Devuelve una lista de diccionarios con `clase`, `linea`, `columna`, `marca`
    y `contexto`. **La ubicación lleva el contexto y no solo la posición**:
    quien vaya a escribir ahí necesita comprobar que el documento no se movió, y
    un número de línea solo no lo dice.
    """
    del_molde = set(del_molde or ())
    en_codigo = _lineas_en_codigo(texto)
    hallados = []
    for numero, linea in enumerate((texto or "").split("\n"), 1):
        if numero in en_codigo:
            continue
        for encontrada in _MARCA.finditer(linea):
            marca = encontrada.group(0)
            if marca == MARCA_DE_INSTALACION:
                clase = INSTALACION
            elif marca == MARCA_CIERTA:
                clase = CIERTO
            elif marca in del_molde:
                clase = POSIBLE
            else:
                # Una cita del autor. Ni se cuenta ni se lista: no es un hueco.
                continue
            hallados.append({
                "clase": clase,
                "linea": numero,
                "columna": encontrada.start() + 1,
                "marca": marca,
                "contexto": linea.strip(),
            })
    return hallados


def por_clase(hallados, clase):
    """Los de una clase, en el orden en que aparecen."""
    return [uno for uno in hallados if uno["clase"] == clase]
