# -*- coding: utf-8 -*-
"""`EP-005 · HU-005` · Un cambio de reglas no se guarda sin su versión.

**Qué exige.** Si lo que se va a guardar toca `base/` o `plantillas/` —lo que
viaja a los proyectos que heredan—, en el mismo commit tienen que ir su subida
de `VERSION` y su entrada en `CHANGELOG.md`. Es [`20·M10`](../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)
dicho por un programa.

**Por qué detiene y no avisa.** Es la decisión 9 del [pendiente 59](../pendientes/59-las-42-dudas-que-detienen-26-fases.md),
y la evidencia estaba medida: *«un aviso que nada respalda se ignora»*. Que
falte la versión se comprueba **mirando qué archivos entran al commit**, sin
criterio de por medio; lo que se comprueba sin criterio, detiene.

**Qué no mira, y se declara.** Si la entrada del registro **dice la verdad**, ni
si el tipo de versión (mayor, menor o parche) es el correcto: eso es leer y
juzgar. Acá se comprueba que estén, que es lo que un programa sabe.

**Y no aplica a lo que no viaja.** Un cambio en `documentacion/`, `pendientes/`
o `validadores/` no exige nada: cambiar un validador no cambia lo que se le
exige a un proyecto.
"""
import os

import comun
import versionado
from comun import FALLA, Hallazgo

# Lo que viaja a los proyectos que heredan. Si cambia, cambió la norma.
HEREDABLE = ("base/", "plantillas/")

# Lo que tiene que acompañarlo, en el mismo commit.
ACOMPANA = ("VERSION", "CHANGELOG.md")


def _normalizar(rutas):
    return {r.replace("\\", "/") for r in rutas}


def reglas_tocadas(preparados):
    """Los archivos heredables que entran en este commit."""
    return sorted(a for a in _normalizar(preparados)
                  if a.startswith(HEREDABLE))


def validar(repo, ruta_mostrada=None, preparados=None):
    """`[Hallazgo]`. Vacío si el commit no toca la norma, o si la trae completa."""
    origen = ruta_mostrada or repo
    if preparados is None:
        preparados = versionado.archivos_preparados(repo)
    preparados = _normalizar(preparados)

    tocadas = reglas_tocadas(preparados)
    if not tocadas:
        return []                      # no toca la norma: nada que exigir

    faltan = [a for a in ACOMPANA if a not in preparados]
    if not faltan:
        return []

    ejemplo = tocadas[0]
    resto = (" y %d archivo(s) más de la norma" % (len(tocadas) - 1)
             if len(tocadas) > 1 else "")
    que_falta = " y ".join(
        {"VERSION": "subir `VERSION`",
         "CHANGELOG.md": "escribir su entrada en `CHANGELOG.md`"}[a]
        for a in faltan)
    return [Hallazgo(
        FALLA, origen, 0,
        "este commit cambia `%s`%s y no trae %s — lo que viaja a los "
        "proyectos se versiona y se registra (20·M10)" % (ejemplo, resto, que_falta))]


if __name__ == "__main__":
    comun.no_es_punto_de_entrada("versionado")
