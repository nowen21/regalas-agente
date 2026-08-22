# -*- coding: utf-8 -*-
"""El checkpoint de la fase se reclama solo — `EP-005 · HU-013`.

**Qué mira.** Cuando se escribe uno de los tres documentos que marcan una
puerta de la fase (`plan_trabajo.md`, `resultado_pruebas.md`,
`funcionalidad_implementada.md`), compara su fecha de escritura con la del
`estado-fase.md` de la misma fase. Si el checkpoint falta o es anterior, hay
algo que decir.

**Qué no hace.** No escribe ni lee el `estado-fase.md`: decir en qué estación
va la fase es criterio, y el criterio no lo tiene un programa. Tampoco juzga
si el estado escrito es cierto; eso lo compara `fases.py` con el veredicto.

**Por qué fechas y no contenido.** Dos fechas del sistema de archivos no
cuestan nada y no dependen de cómo esté redactado el checkpoint. Leerlo y
buscar la estación sería opinar sobre el texto.

**Por qué acá y no en el adaptador.** Reconocer la fase y comparar fechas es
agnóstico; **enterarse** de que se escribió un archivo es de la herramienta, y
eso vive en el enganche del adaptador (`adaptadores/claude-code/`).
"""
import os

import comun
import fases

# Los tres documentos cuya escritura es pasar una puerta (`02·F15`). El plan de
# pruebas y el README no marcan ninguna; escribirlos no dispara nada.
DOCUMENTOS_DE_PUERTA = ("plan_trabajo.md", "resultado_pruebas.md",
                        "funcionalidad_implementada.md")
CHECKPOINT = "estado-fase.md"


def fase_de(ruta):
    """La carpeta de la fase a la que pertenece `ruta`, o "" si no es de una.

    Una fase se reconoce por el nombre de su carpeta (`02·F12.6`), con la misma
    expresión que usa `fases.py`: dos copias del patrón se desincronizan.
    """
    carpeta = os.path.dirname(os.path.abspath(ruta))
    return carpeta if fases._FASE.match(os.path.basename(carpeta)) else ""


def rezago(ruta):
    """`(motivo, fase, documento)` si el checkpoint quedó atrás, o None.

    `motivo` es `"falta"` (no hay `estado-fase.md`) o `"atrasado"` (lo hay,
    pero se escribió antes que el documento). None cuando no hay nada que
    decir: el archivo no es de puerta, no está en una fase, o ya no existe.
    """
    nombre = os.path.basename(ruta)
    if nombre not in DOCUMENTOS_DE_PUERTA:
        return None
    fase = fase_de(ruta)
    if not fase or not os.path.isfile(ruta):
        return None
    checkpoint = os.path.join(fase, CHECKPOINT)
    if not os.path.isfile(checkpoint):
        return ("falta", fase, nombre)
    try:
        if os.stat(checkpoint).st_mtime < os.stat(ruta).st_mtime:
            return ("atrasado", fase, nombre)
    except OSError:
        return None                     # se borró entre mirar y medir: silencio
    return None


def como_texto(hallazgo, raiz=""):
    """El aviso, con la fase relativa al proyecto para que se sepa dónde."""
    motivo, fase, documento = hallazgo
    donde = fase
    if raiz:
        try:
            donde = os.path.relpath(fase, raiz)
        except ValueError:              # otra unidad en Windows
            pass
    donde = donde.replace("\\", "/")
    if motivo == "falta":
        return ("[LA FASE PASÓ UNA PUERTA SIN CHECKPOINT]\n"
                f"Se escribió `{documento}` en `{donde}` y la fase no tiene "
                f"`{CHECKPOINT}`. Escribirlo con la estación en que va "
                "(`plantillas/ciclo-vida-proyectos/10-estado-fase.md`): es lo que la próxima sesión lee "
                "para seguir sin releer la conversación.")
    return ("[EL CHECKPOINT DE LA FASE QUEDÓ ATRÁS]\n"
            f"Se escribió `{documento}` en `{donde}` y su `{CHECKPOINT}` es "
            "anterior. Ponerlo al día con la puerta que acaba de pasar.")


if __name__ == "__main__":
    comun.no_es_punto_de_entrada()
