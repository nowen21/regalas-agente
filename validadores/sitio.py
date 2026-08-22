# -*- coding: utf-8 -*-
"""`EP-005 · HU-011` · El mapa del sitio no envejece en silencio.

**Qué contesta el mapa.** Dónde vive cada cosa del repositorio y para qué sirve:
es la puerta de entrada de quien abre esto por primera vez y no sabe por dónde
empezar ([`anatomia/mapa-del-sitio.md`](../anatomia/mapa-del-sitio.md)).

**Por qué hace falta comprobarlo.** El mapa se escribe a mano, y un mapa escrito
a mano envejece **en silencio**: una carpeta nueva no aparece ahí hasta que
alguien se acuerde, y quien lo lea creerá que no existe. Le pasó ya: `anatomia/`
estuvo fuera de la tabla del `CLAUDE.md` hasta el 2026-08-18.

**Se mira por los dos lados**, igual que en [`amarre.py`](amarre.py):

1. La carpeta que **existe y el mapa no nombra**.
2. La carpeta que **el mapa nombra y ya no existe** — arreglar solo el primero
   deja la mitad del problema, y esta mitad es la que promete algo que no está.

**Lo que no comprueba, y se declara.** Si la descripción es la **acertada**, ni
si la carpeta está en la zona correcta: eso es un juicio y se lee. Acá se
comprueba que **esté nombrada**, que es lo único que un programa puede saber.

**Nunca detiene por lo que no es suyo.** Las carpetas de trabajo local (`.git`,
`.venv`, `__pycache__`, `terceros/`) no son del mapa: no viajan, no se versionan
y nombrarlas sería ruido.
"""
import os
import re

import comun
from comun import AVISO, FALLA, Hallazgo, leer

MAPA = os.path.join("anatomia", "mapa-del-sitio.md")

# Lo que no es del mapa: generado, local o de terceros. Se nombra una por una y
# no por patrón amplio, para que una carpeta nueva de verdad no se cuele por el
# hueco de una regla demasiado ancha.
FUERA = {
    ".git", ".venv", "venv", "__pycache__", ".pytest_cache", ".idea", ".vscode",
    "node_modules", "terceros", ".mypy_cache", ".ruff_cache", "dist", "build",
}


def carpetas(raiz=None):
    """Las carpetas de primer nivel que el mapa debería nombrar."""
    raiz = raiz or comun.RAIZ
    salida = []
    for nombre in sorted(os.listdir(raiz)):
        if nombre in FUERA or nombre.startswith("."):
            continue
        if os.path.isdir(os.path.join(raiz, nombre)):
            salida.append(nombre)
    return salida


def _mapa(raiz):
    archivo = os.path.join(raiz or comun.RAIZ, *MAPA.split(os.sep))
    return archivo, (leer(archivo) if os.path.isfile(archivo) else "")


def validar(raiz=None):
    """Las dos formas de envejecer de un mapa escrito a mano."""
    raiz = raiz or comun.RAIZ
    archivo, texto = _mapa(raiz)
    if not texto:
        return [Hallazgo(FALLA, archivo, 0,
                         "falta el mapa del sitio, que es por donde entra "
                         "quien abre el repositorio y no sabe dónde está nada")]

    hallazgos = []
    existentes = carpetas(raiz)

    # 1 · La carpeta que existe y el mapa no nombra.
    for nombre in existentes:
        if not re.search(r"(?<![\w/-])%s/" % re.escape(nombre), texto):
            hallazgos.append(Hallazgo(
                FALLA, archivo, 0,
                f"`{nombre}/` no está en el mapa — quien lo lea va a creer "
                f"que esa carpeta no existe"))

    # 2 · La carpeta que el mapa nombra y ya no existe.
    for citada in sorted(set(re.findall(r"`([a-z0-9][\w.-]*)/`", texto))):
        if citada not in existentes and citada not in FUERA:
            hallazgos.append(Hallazgo(
                AVISO, archivo, 0,
                f"el mapa nombra `{citada}/`, que ya no existe — se movió o se "
                f"borró, y el mapa manda a alguien a un sitio vacío"))

    return hallazgos


def linea_resumen(raiz=None):
    """El recuento, para poder mirarlo sin abrir el mapa."""
    raiz = raiz or comun.RAIZ
    _, texto = _mapa(raiz)
    if not texto:
        return ""
    existentes = carpetas(raiz)
    nombradas = sum(
        1 for n in existentes
        if re.search(r"(?<![\w/-])%s/" % re.escape(n), texto))
    return ("Carpetas de primer nivel: %d · nombradas en el mapa: %d · "
            "sin nombrar: %d" % (len(existentes), nombradas,
                                 len(existentes) - nombradas))


if __name__ == "__main__":
    comun.no_es_punto_de_entrada("sitio")
