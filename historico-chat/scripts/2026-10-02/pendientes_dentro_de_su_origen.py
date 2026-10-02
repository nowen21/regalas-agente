# -*- coding: utf-8 -*-
"""Turnos 173 a 177: el pendiente 108 pasa a la carpeta `pendientes/` de la HU-036,
con solo sus tres campos, y el análisis 8 suma la conclusión y el punto para la HU-003."""
import os
import shutil

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
HU36 = os.path.join(RAIZ, "documentacion", "epicas", "EP-001-cuerpo-de-reglas-heredable",
                    "HU-036-el-pedido-dice-que-se-espera")
NOMBRE = "108-la-respuesta-corta-a-una-pregunta-cuenta-como-respuesta"
VIEJA = os.path.join(HU36, NOMBRE)
NUEVA = os.path.join(HU36, "pendientes", NOMBRE)
RESUMEN = os.path.join(RAIZ, "historico-chat", "resumenes", "2026-10-01", "sesion.md")
ANALISIS = os.path.join(RAIZ, "documentacion", "epicas", "EP-023-lo-que-se-construye-es-lo-que-se-analizo",
                        "103-cada-documento-de-la-cadena-sale-del-anterior", "analisis-8.md")
H3 = ("../HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde/"
      "HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde.md")

PENDIENTE = """# Pendiente: la respuesta corta a una pregunta del agente cuenta como respuesta

| | |
|---|---|
| **De dónde sale** | [H-10 de la sesión del 2026-10-01](../../../../../../historico-chat/resumenes/2026-10-01/sesion.md) |

## El problema

`01·C28` detiene todo mensaje que no abre con una de sus palabras, aunque responda una pregunta del agente. El 2026-10-02 se detuvieron «sí» y «A», dados después de una pregunta, y «00 id9», que pide aplicar esa regla a la última respuesta. Cada uno hubo que repetirlo con su palabra.

## Por qué importa

Cuesta turnos y corta la conversación justo cuando el usuario decide, que es lo que más importa que quede.
"""


def escribir(ruta, texto):
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def leer(ruta):
    with open(ruta, encoding="utf-8") as f:
        return f.read()


def main():
    os.makedirs(os.path.dirname(NUEVA), exist_ok=True)
    shutil.move(VIEJA, NUEVA)
    escribir(os.path.join(NUEVA, "pendiente.md"), PENDIENTE)

    r = leer(RESUMEN)
    viejo = "HU-036-el-pedido-dice-que-se-espera/" + NOMBRE + "/pendiente.md"
    assert r.count(viejo) == 1
    escribir(RESUMEN, r.replace(viejo, "HU-036-el-pedido-dice-que-se-espera/pendientes/" + NOMBRE + "/pendiente.md"))

    a = leer(ANALISIS)
    a = a.replace("\nSiguen abiertas: ninguna.",
                  "| 15 | Dónde vive el pendiente | Dentro de lo que lo origina va una carpeta `pendientes/`, y dentro de ella cada pendiente en su carpeta, con `pendiente.md` y sus análisis. La numeración sigue siendo una sola en todo el proyecto. Un programa arma el índice de todos, con su número, dónde viven y si su plan cerró. El validador de fases acepta `pendientes/` dentro de una épica, de una HU o de un resumen del día. Cuando el análisis decide a dónde va un pendiente que esperaba en el resumen del día, la carpeta se mueve y sus enlaces se actualizan. Si ya se sabe a quién pertenece, nace allá: el 108 va en `pendientes/` de la HU-036. Precisa la conclusión 11 del análisis 1 | Turnos 173 a 177 |\n"
                  "\nSiguen abiertas: ninguna.", 1)
    fila = [l for l in a.split("\n") if l.startswith("| 9 | Subir la corrección del H-9")][0]
    a = a.replace(fila, fila + "\n| 10 | Sumar a la HU-003 la carpeta `pendientes/` dentro de lo que origina cada pendiente, con la numeración única, el índice que se arma solo, el validador de fases y el traslado de los pendientes de `pendientes/` y del 103 | 15 | EP-023, [HU-003](" + H3 + ") |", 1)
    escribir(ANALISIS, a)


if __name__ == "__main__":
    main()
