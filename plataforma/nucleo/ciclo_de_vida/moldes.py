# -*- coding: utf-8 -*-
"""Qué molde le toca a cada tipo de documento del ciclo.

**La tabla se declara; no se deduce del nombre.** Se intentó deducirla y falla
en cinco de los diecinueve tipos: tres moldes viven fuera de
`plantillas/ciclo-vida-proyectos/` y dos tipos no tienen molde escrito.

**Reconocer el tipo no es trabajo de este módulo.** Lo hace Importación, que ya
sabe distinguir por nombre, por forma y por ubicación. Acá solo se dice, dado un
tipo, cuál es su molde.

**Un tipo sin molde no es lo mismo que un tipo desconocido**, y confundirlos
esconde el que sí se puede arreglar. Por eso son dos respuestas distintas.
"""
import io
import os
import re

# El tipo, tal como lo devuelve Importación, y su molde dentro de `plantillas/`.
POR_TIPO = {
    "épica": "ciclo-vida-proyectos/03-epica.md",
    "historia de usuario": "ciclo-vida-proyectos/04-HU.md",
    "especificación de módulo": "ciclo-vida-proyectos/06-especificacion-modulo.md",
    "plan de trabajo": "ciclo-vida-proyectos/07-plan-trabajo.md",
    "plan de pruebas": "ciclo-vida-proyectos/08-plan-pruebas.md",
    "resultado de pruebas": "ciclo-vida-proyectos/09-resultado-pruebas.md",
    "estado de fase": "ciclo-vida-proyectos/10-estado-fase.md",
    "funcionalidad implementada":
        "ciclo-vida-proyectos/11-funcionalidad-implementada.md",
    "inventario de funcionalidades":
        "ciclo-vida-proyectos/02-inventario-funcionalidades.md",
    "estudio de factibilidad": "ciclo-vida-proyectos/12-estudio-factibilidad.md",
    "acta de constitución":
        "ciclo-vida-proyectos/13-acta-de-constitucion-y-plan-de-proyecto.md",
    "modelo de datos": "ciclo-vida-proyectos/14-modelo-de-datos.md",
    "diseño de interfaz": "ciclo-vida-proyectos/15-diseno-de-interfaz.md",
    "contrato de la interfaz": "ciclo-vida-proyectos/16-documentacion-de-api.md",
    # Los tres que viven fuera de la carpeta del ciclo. Son la razón de que esta
    # tabla se escriba a mano en vez de armarse con el número del tipo.
    "señales": "senales.md",
    "decisiones de arquitectura": "cvds/diseno/decisiones-de-arquitectura.md",
}

# Los que Importación reconoce y **no tienen molde**, con el porqué. Se dicen:
# callarlos haría creer que el documento no se reconoció.
SIN_MOLDE = {
    "índice": ("es el README de una carpeta cualquiera; describe lo que hay "
               "dentro, no sigue un molde"),
    "registro de versión": ("la adopción de una versión se anota, y nunca se "
                            "escribió su molde"),
}

# El documento de una etapa es el `README.md` de su carpeta, y su molde vive en
# `plantillas/cvds/<etapa>/README.md`. Cuál etapa depende de dónde está el
# archivo, no de su nombre.
ETAPA = re.compile(r"(?:^|/)cvds/([a-z-]+)/README\.md$")

TIPO_DE_ETAPA = "etapa del ciclo de vida"


def molde_de(tipo, relativa=""):
    """La ruta del molde dentro de `plantillas/`, o `""` si no tiene.

    `relativa` es la ruta del documento dentro de su proyecto. Hace falta para
    una sola cosa: la etapa del ciclo, cuyo molde depende de cuál etapa es.
    """
    if tipo == TIPO_DE_ETAPA:
        encontrada = ETAPA.search((relativa or "").replace("\\", "/"))
        if not encontrada:
            return ""
        return "cvds/%s/README.md" % encontrada.group(1)
    return POR_TIPO.get(tipo, "")


def por_que_no_tiene_molde(tipo):
    """Por qué un tipo reconocido no tiene molde, o `""` si sí tiene."""
    return SIN_MOLDE.get(tipo, "")


def texto_del_molde(carpeta_plantillas, tipo, relativa=""):
    """El texto del molde, o `""` si no hay molde o no se puede leer.

    **Se lee cuando se pide, no se copia.** Un molde copiado dentro del módulo
    envejece en cuanto el estándar cambie el original, y entonces los huecos que
    se busquen serían los de anteayer.
    """
    ruta = molde_de(tipo, relativa)
    if not ruta:
        return ""
    completa = os.path.join(str(carpeta_plantillas), *ruta.split("/"))
    try:
        with io.open(completa, encoding="utf-8", errors="replace") as abierto:
            return abierto.read()
    except OSError:
        return ""
