"""Busca en las plantillas de Cimiento las claves de ayuda que se usan, para comprobar que todas tienen texto."""
import re
from pathlib import Path

from django.conf import settings

_CAMPO = re.compile(r"""\{%\s*(?:ayuda_campo|campo_con_ayuda\s+\S+)\s+["']([^"']+)["']""")
_PANTALLA = re.compile(r"""\{%\s*ayuda_pantalla\s+["']([^"']+)["']""")


def _plantillas():
    raiz = Path(settings.RAIZ)          # Cimiento llama así a su carpeta, no `BASE_DIR`
    yield from (raiz / "templates").rglob("*.html")
    yield from (raiz / "core").glob("*/templates/**/*.html")


def usadas():
    """`(claves de campo, claves de pantalla)` que aparecen en las plantillas."""
    campos, pantallas = set(), set()
    for ruta in _plantillas():
        texto = ruta.read_text(encoding="utf-8")
        campos.update(_CAMPO.findall(texto))
        pantallas.update(_PANTALLA.findall(texto))
    return campos, pantallas
