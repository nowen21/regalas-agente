# -*- coding: utf-8 -*-
"""Fase A de la HU-003, T-01: las tres plantillas del pendiente quedan con «De dónde sale», «El problema»
y «Por qué importa» (análisis 1, conclusiones 15 y 36). Se conserva la caja de reglas de redacción."""
import os
import re

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))


def reglas(texto):
    """La caja de reglas de redacción con la que abre la plantilla, tal como está."""
    m = re.search(r"^> Todo documento creado con esta plantilla.*?\n\n", texto, re.M | re.S)
    return m.group(0)


CUERPO = {
    "pendiente.md": (
        "# Pendiente: «qué falta, en una línea»\n\n",
        "> Modelo del pendiente. Vive en su propia carpeta, con este archivo como `pendiente.md` y sus análisis al lado, "
        "dentro de la carpeta `pendientes/` de lo que lo origina: una épica, una HU, o el resumen del día mientras su "
        "análisis no decide a dónde va. Lo levanta el andamio (`python validadores/andamio.py pendiente <slug>`). "
        "Qué historia dispara, cómo se construye y cuándo cierra no se escriben acá: los decide su análisis, y el estado "
        "lo calcula el programa siguiendo los enlaces. Al llenarlo se reemplazan los `«…»` y se borran las notas.\n\n",
        "| | |\n|---|---|\n"
        "| **De dónde sale** | «el hallazgo que lo destapó, con su enlace» |\n\n"
        "## El problema\n\n«Qué se encontró, con el detalle que necesita quien no vio el caso. Con rutas y líneas, verificadas.»\n\n"
        "## Por qué importa\n\n«Qué se rompe o qué se pierde si se deja como está.»\n"),
    "pendiente-de-seguimiento.md": (
        "# Pendiente: esperando una corrección del estándar, «qué»\n\n",
        "> Modelo del pendiente que queda en el proyecto cuando lo que hay que corregir es del estándar (`02·F24`). "
        "Su «De dónde sale» enlaza el pendiente que se abrió en el estándar: ese es su padre, y este cierra cuando cierra "
        "el plan de aquel, sin que nadie lo escriba acá. Su gemelo es [plantillas/pendiente-reportado.md](pendiente-reportado.md). "
        "Al llenarlo se reemplazan los `«…»` y se borran las notas.\n\n",
        "| | |\n|---|---|\n"
        "| **De dónde sale** | «el pendiente que se abrió en el estándar, con su enlace» |\n\n"
        "## El problema\n\n«El defecto visto desde este proyecto: qué se intentó, qué salió mal y qué se hace mientras tanto.»\n\n"
        "## Por qué importa\n\n«Qué se rompe o qué se pierde mientras el estándar no lo corrija.»\n"),
    "pendiente-reportado.md": (
        "# Pendiente: «qué se encontró, en una línea»\n\n",
        "> Modelo del pendiente que un proyecto le reporta al estándar (`02·F24`). Se crea **en el estándar**, y su "
        "«De dónde sale» enlaza el hallazgo del proyecto que lo destapó: ese enlace ya dice de qué proyecto viene. "
        "Su gemelo, el que queda en el proyecto, es [plantillas/pendiente-de-seguimiento.md](pendiente-de-seguimiento.md), "
        "y los dos se escriben en la misma sesión. Al llenarlo se reemplazan los `«…»` y se borran las notas.\n\n",
        "| | |\n|---|---|\n"
        "| **De dónde sale** | «el hallazgo del proyecto que lo destapó, con su enlace» |\n\n"
        "## El problema\n\n«Qué se encontró, con el detalle que necesita quien va a corregirlo y no vio el caso, y cómo se reproduce.»\n\n"
        "## Por qué importa\n\n«Qué se rompe o qué se pierde mientras siga abierto.»\n"),
}


def main():
    for nombre, (titulo, nota, cuerpo) in CUERPO.items():
        ruta = os.path.join(RAIZ, "plantillas", nombre)
        with open(ruta, encoding="utf-8") as f:
            caja = reglas(f.read())
        with open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(titulo + caja + nota + cuerpo)


if __name__ == "__main__":
    main()
