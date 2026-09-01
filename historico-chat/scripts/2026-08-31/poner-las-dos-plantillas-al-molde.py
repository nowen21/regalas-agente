# -*- coding: utf-8 -*-
"""Deja las dos plantillas nuevas cumpliendo lo que el estandar ya exige.

Tres arreglos, todos declarados con el usuario el 2026-08-31:

1. **Los huecos se marcan como los marca la casa** (`13-DOC19`). El documento de
   arquitectura traia 218 huecos escritos `<ASI>`, y el manual de usuario
   tambien usa esa forma. Publicar asi significa que cada proyecto que copie el
   modelo marque sus huecos con una notacion que su propio validador le va a
   reportar.

2. **Los dos citan `00-ID10`** en vez de callar la norma de redaccion o
   repetirla. Repetirla es lo que hizo que naciera la regla: una norma escrita
   dentro de un documento modelo solo la hereda quien llene ese modelo
   (`S-090`).

3. **El manual de usuario recupera su bloque de reglas**, que se perdio al
   reemplazarlo entero. Recuperarlo no es copiarlo: es citar la regla.

**No se toca el contenido de las plantillas.** Lo que cambia es como se marcan
los huecos y una linea de cita en cada una.
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

ARQUITECTURA = os.path.join(RAIZ, "plantillas", "documento-arquitectura.md")
USUARIO = os.path.join(RAIZ, "plantillas", "manual-usuario.md")

# `<LO_QUE_SEA>` pasa a «LO_QUE_SEA». Se pide mayuscula o guion bajo para no
# tocar lo que sea sintaxis de otra cosa: una etiqueta de marcado, una
# comparacion, una flecha.
_HUECO = re.compile(r"<([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑ0-9_ ]*)>")

CITA = (u"> **Cómo se escribe lo que se llena.** En la variedad del idioma que usa "
        u"el proyecto, en tercera persona para lo que se explica y en infinitivo "
        u"para lo que el lector hace — la regla es "
        u"[`00·ID10`](../base/00-identidad-y-rol/reglas/"
        u"ID10-escribe-en-el-idioma-del-proyecto-en-tercera-persona-y-en-infinitivo.md), "
        u"y se cita en vez de repetirla: lo que se copia a mano se copia distinto "
        u"(`S-090`). Los espacios por llenar van marcados `«…»`, que es la marca "
        u"de todos los modelos "
        u"([`13·DOC19`](../base/13-documentacion/reglas/"
        u"DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md)).")


def marcar_los_huecos(texto):
    """Los huecos con la marca de la casa. Devuelve el texto y cuantos cambio."""
    cuantos = len(_HUECO.findall(texto))
    return _HUECO.sub(lambda m: u"«%s»" % m.group(1), texto), cuantos


def poner_la_cita(texto):
    """La cita, despues del titulo. Si ya esta, no se repite."""
    if u"00·ID10" in texto:
        return texto, False
    lineas = texto.split("\n")
    for i, linea in enumerate(lineas):
        if linea.startswith("# "):
            lineas[i + 1:i + 1] = ["", CITA]
            return "\n".join(lineas), True
    return texto, False


def main():
    for ruta in (ARQUITECTURA, USUARIO):
        if not os.path.isfile(ruta):
            print("no esta:", ruta)
            continue
        texto = io.open(ruta, encoding="utf-8").read()
        texto, cuantos = marcar_los_huecos(texto)
        texto, citada = poner_la_cita(texto)
        io.open(ruta, "w", encoding="utf-8", newline="\n").write(texto)
        print("%-28s %3d hueco(s) remarcado(s) · cita %s"
              % (os.path.basename(ruta), cuantos,
                 "puesta" if citada else "ya estaba"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
