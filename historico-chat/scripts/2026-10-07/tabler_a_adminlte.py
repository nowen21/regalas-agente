# -*- coding: utf-8 -*-
"""EP-028·HU-007 · Cambia las clases propias de Tabler por las de Bootstrap 5 y
AdminLTE 4 en las plantillas y en el código que arma HTML de Cimiento.

Solo toca clases dentro de `class="..."` (y en `presentar.py`, también dentro de
las cadenas que arman ese atributo). La estructura de las páginas (`base.html`,
la de entrada y la de Cimiento apagado) se rehace a mano: no la cambia este guion.

    python historico-chat/scripts/2026-10-07/tabler_a_adminlte.py            # ensayo: dice qué cambiaría
    python historico-chat/scripts/2026-10-07/tabler_a_adminlte.py --aplicar  # lo escribe
"""
import glob
import os
import re
import sys

RAIZ = os.path.join(os.path.dirname(__file__), "..", "..", "..", "proyectos", "cimiento")

# Una clase de Tabler → sus clases de Bootstrap/AdminLTE ("" la quita).
CLASES = {
    "table-vcenter": "align-middle",
    "card-table": "mb-0",
    "form-hint": "form-text",
    "btn-list": "d-flex flex-wrap gap-2",
    "badge-sm": "",
    "card-sm": "",
    "card-md": "",
    "row-cards": "g-3",
    "subheader": "text-uppercase small fw-semibold text-secondary",
    "empty": "text-center py-5",
    "empty-title": "fs-5 fw-semibold mb-1",
    "empty-subtitle": "text-secondary mb-0",
    "empty-action": "mt-3",
    "alert-title": "alert-heading",
    "text-red-fg": "",
    "bg-red": "text-bg-danger",
    "bg-blue-lt": "bg-primary-subtle text-primary-emphasis",
    "bg-azure-lt": "bg-info-subtle text-info-emphasis",
    "bg-purple-lt": "bg-info-subtle text-info-emphasis",
    "bg-green-lt": "bg-success-subtle text-success-emphasis",
    "bg-red-lt": "bg-danger-subtle text-danger-emphasis",
    "bg-yellow-lt": "bg-warning-subtle text-warning-emphasis",
    "bg-secondary-lt": "bg-secondary-subtle text-secondary-emphasis",
}
_ATRIBUTO = re.compile(r'class="([^"]*)"')


def cambiar_clases(valor):
    partes = re.split(r"(\{[%{].*?[%}]\}|\s+)", valor)
    salida = []
    for p in partes:
        if p in CLASES:
            if CLASES[p]:
                salida.append(CLASES[p])
        else:
            salida.append(p)
    return re.sub(r"\s{2,}", " ", "".join(salida)).strip()


def cambiar(texto):
    return _ATRIBUTO.sub(lambda m: 'class="%s"' % cambiar_clases(m.group(1)), texto)


def archivos():
    patrones = ["templates/**/*.html", "core/**/templates/**/*.html"]
    for patron in patrones:
        yield from glob.glob(os.path.join(RAIZ, patron), recursive=True)


def main(aplicar):
    for ruta in sorted(archivos()):
        texto = open(ruta, encoding="utf-8").read()
        nuevo = cambiar(texto)
        if nuevo != texto:
            print(("cambia " if aplicar else "cambiaría ") + os.path.relpath(ruta, RAIZ).replace("\\", "/"))
            if aplicar:
                with open(ruta, "w", encoding="utf-8", newline="") as f:
                    f.write(nuevo)


if __name__ == "__main__":
    main("--aplicar" in sys.argv)
