# -*- coding: utf-8 -*-
"""Publicar una versión del cuerpo de reglas. **La puerta va antes.**

**Publicar es lo que vuelve real un cambio.** Antes de eso, una regla escrita no
rige en ninguna parte: los proyectos siguen con la versión que adoptaron. Y
después, lo publicado se lo lleva quien lo adopte, con lo bueno y con lo roto.

**Tres cosas se comprueban antes, y ninguna es opcional:**

- **Que ese número no exista ya.** Publicar dos veces el mismo hace que dos
  proyectos con la misma versión declarada tengan reglas distintas.
- **Que el registro diga qué cambió.** Sin eso, el que adopte no puede saber si
  le toca rehacer algo, y el aviso de desfase no tiene qué contar.
- **Que la puerta pase.** Es la de `F-022`, y ya existe: corre las
  comprobaciones y la suite del proyecto.

**Lo que la plataforma no escribe es la entrada del registro.** Es prosa: dice
qué pasó y por qué importa, y eso lo escribe una persona. Lo que sí hace es
negarse a publicar sin ella.
"""
import io
import os
import re

from django.conf import settings

from nucleo.comprobaciones import puerta
from . import desfase

# `## 37.2.0 — 2026-08-31`
_ENTRADA = re.compile(u"(?m)^##\\s+(\\d+\\.\\d+\\.\\d+)\\b")

# `**MAYOR** (…)`, en cualquier parte de la entrada.
_TIPO = re.compile(u"\\*\\*(MAYOR|MENOR|PARCHE)\\*\\*")


class NoSePuedePublicar(Exception):
    """Falta algo para publicar, y se dice qué."""


def _archivo(raiz, nombre):
    return os.path.join(raiz, nombre)


def _leer(ruta):
    try:
        with io.open(ruta, encoding="utf-8", newline="") as archivo:
            return archivo.read()
    except OSError:
        return ""


def entrada_del_registro(raiz, version):
    """El texto de la entrada de esa versión en el registro, o `""`.

    Devuelve desde su encabezado hasta el de la siguiente entrada.
    """
    texto = _leer(_archivo(raiz, "CHANGELOG.md"))
    encontradas = list(_ENTRADA.finditer(texto))
    for numero, encontrada in enumerate(encontradas):
        if encontrada.group(1) != version:
            continue
        hasta = (encontradas[numero + 1].start()
                 if numero + 1 < len(encontradas) else len(texto))
        return texto[encontrada.start():hasta].strip()
    return ""


def revisar(identificador_del_proyecto, raiz, version_nueva):
    """Qué falta para publicar esa versión. Devuelve qué se comprobó.

    **No publica nada.** Es la revisión, y se puede pedir todas las veces que
    haga falta antes de decidir.
    """
    problemas = []

    if not re.match(u"^\\d+\\.\\d+\\.\\d+$", version_nueva or ""):
        problemas.append("«%s» no tiene forma de versión." % version_nueva)
        return {"se_puede": False, "problemas": problemas, "entrada": "",
                "tipo": "", "puerta": None}

    if desfase.existe(version_nueva):
        problemas.append(
            "La versión %s ya está publicada. **Publicar dos veces el mismo "
            "número hace que dos proyectos que declaran esa versión tengan "
            "reglas distintas.**" % version_nueva)

    entrada = entrada_del_registro(raiz, version_nueva)
    tipo = ""
    if not entrada:
        problemas.append(
            "El registro de cambios no tiene entrada para %s. **Sin decir qué "
            "cambió no se publica:** quien adopte no podría saber si le toca "
            "rehacer algo." % version_nueva)
    else:
        encontrado = _TIPO.search(entrada)
        tipo = encontrado.group(1) if encontrado else ""
        if not tipo:
            problemas.append(
                "La entrada de %s no dice si es MAYOR, MENOR o PARCHE. Es lo "
                "que le dice al que adopta si le toca rehacer algo."
                % version_nueva)

    revision = puerta.revisar_antes_de_publicar(identificador_del_proyecto)
    if not revision.pasa:
        problemas.append(
            "La puerta no pasa: %s **Una versión que rompe algo que servía no "
            "se publica.**"
            % (revision.porque or "algo que estaba en verde dejó de estarlo."))

    return {"se_puede": not problemas, "problemas": problemas,
            "entrada": entrada, "tipo": tipo, "puerta": revision}


def publicar(identificador_del_proyecto, raiz, version_nueva):
    """Escribe la versión nueva, **solo si la revisión pasa**.

    Devuelve la revisión. Levanta `NoSePuedePublicar` con todo lo que falta,
    junto: decirlo de a uno obliga a intentar tres veces.
    """
    revision = revisar(identificador_del_proyecto, raiz, version_nueva)
    if not revision["se_puede"]:
        raise NoSePuedePublicar("\n".join(revision["problemas"]))

    ruta = _archivo(raiz, "VERSION")
    con_salto = _leer(ruta).endswith("\n")
    with io.open(ruta, "w", encoding="utf-8", newline="") as archivo:
        archivo.write(version_nueva + ("\n" if con_salto else ""))
    revision["publicada_en"] = ruta
    return revision
