# -*- coding: utf-8 -*-
"""EP-028·HU-007 · Arma el borrador de la propuesta que dice, en la guía de diseño de
pantallas, que la plantilla de Cimiento es AdminLTE 4. No propone: eso lo hace
`manage.py proponer`, y lo aprueba el usuario en la pantalla.

    .venv/Scripts/python.exe manage.py shell -c "exec(open('../../historico-chat/scripts/2026-10-07/propuesta_guia_adminlte.py',encoding='utf-8').read())"
"""
import os

from core.estandar.models import Documento

BORRADOR = ("../../documentacion/epicas/EP-028-las-pantallas-orientan-al-usuario-sin-que-conozca-como-esta-armado-el-sistema/"
            "HU-007-cimiento-usa-adminlte-4/A-EP-028-HU-007-adminlte/propuestas/guia-de-pantallas.txt")
CAMBIOS = [
    ("y después **cómo se hace con Tabler**, que es la plantilla de Cimiento y el ejemplo de referencia. Un proyecto "
     "con otra plantilla (por ejemplo AdminLTE) busca en la suya el recurso que hace lo mismo.",
     "y después **cómo se hace con Tabler**, que es el ejemplo de referencia. Un proyecto con otra plantilla busca en "
     "la suya el recurso que hace lo mismo: Cimiento usa AdminLTE 4, sobre Bootstrap 5."),
    ("**Cómo con Tabler.** En Cimiento: Tabler 1.6.1, con List.js, Tom Select, Litepicker, Driver.js, Dropzone y "
     "ApexCharts instalados; la ayuda vive en `core/ayuda/`.",
     "**En Cimiento.** AdminLTE 4.10.0, sobre Bootstrap 5.3.8, con Bootstrap Icons, List.js, htmx y ApexCharts "
     "instalados; lo poco que la plantilla no trae vive en `static/cimiento.css`, y la ayuda, en `core/ayuda/`."),
]

texto = Documento.objects.get(ruta="base/17-guia-de-pantallas.md").contenido.replace("\r\n", "\n")
for viejo, nuevo in CAMBIOS:
    print("encontrado %d vez" % texto.count(viejo))
    texto = texto.replace(viejo, nuevo)
os.makedirs(os.path.dirname(BORRADOR), exist_ok=True)
with open(BORRADOR, "w", encoding="utf-8", newline="\n") as f:
    f.write(texto)
print("borrador escrito")
