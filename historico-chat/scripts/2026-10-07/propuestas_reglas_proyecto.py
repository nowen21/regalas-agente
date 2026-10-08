# -*- coding: utf-8 -*-
"""EP-027·HU-006, fase E · Arma los borradores de las cinco propuestas que dicen
dónde viven las reglas de un proyecto: en la tabla de Cimiento si el proyecto
está registrado, y en `.agente/reglas-proyecto.md` si no.

Lee cada documento de la base, cambia solo la línea que nombra el archivo y deja
el borrador en `propuestas/` de la fase. No propone nada: eso lo hace
`manage.py proponer`, y lo aprueba el usuario en la pantalla.

    .venv/Scripts/python.exe manage.py shell -c "exec(open('../../historico-chat/scripts/2026-10-07/propuestas_reglas_proyecto.py',encoding='utf-8').read())"
"""
import os

from core.estandar.models import Documento

FASE = ("../../documentacion/epicas/EP-027-las-reglas-del-estandar-viven-en-tablas-con-la-estructura-del-molde/"
        "HU-006-las-reglas-de-cada-proyecto-viven-en-la-misma-tabla/E-EP-027-HU-006-la-plantilla-y-el-paso/propuestas")

CAMBIOS = [
    ("base/02-flujo-de-trabajo/estructura-base.md", "estructura-base.txt",
     "reglas-proyecto.md            #   si aplica (DOC10)",
     "reglas-proyecto.md            #   si aplica y el proyecto no está en Cimiento (DOC10)"),
    ("base/20-meta-reglas/base.md", "meta-reglas-base.txt",
     "| `.agente/reglas-proyecto.md` del proyecto (capa 3) |",
     "| la tabla de reglas de Cimiento, marcada con su proyecto; si el proyecto no está registrado, "
     "`.agente/reglas-proyecto.md` (capa 3) |"),
    ("base/20-meta-reglas/desempate.md", "desempate.txt",
     "(`CLAUDE.md §5.1` o `.agente/reglas-proyecto.md`)",
     "(`CLAUDE.md §5.1`, o sus reglas propias: en Cimiento, o en `.agente/reglas-proyecto.md` si el proyecto "
     "no está registrado)"),
    ("base/20-meta-reglas/estructura-regla.md", "estructura-regla.txt",
     "en `.agente/reglas-proyecto.md`.",
     "en su casilla de la tabla de reglas de Cimiento, o en `.agente/reglas-proyecto.md` si el proyecto no está "
     "registrado."),
    ("base/glosario.md", "glosario.txt",
     "| Agente | `.agente/reglas-proyecto.md` |",
     "| Agente | La tabla de reglas de Cimiento, marcada con su proyecto; si no está registrado, "
     "`.agente/reglas-proyecto.md` |"),
]

os.makedirs(FASE, exist_ok=True)
for ruta, borrador, viejo, nuevo in CAMBIOS:
    texto = Documento.objects.get(ruta=ruta).contenido.replace("\r\n", "\n")
    veces = texto.count(viejo)
    if veces != 1:
        print("NO SE ARMÓ %s: el texto a cambiar aparece %d veces" % (ruta, veces))
        continue
    with open(os.path.join(FASE, borrador), "w", encoding="utf-8", newline="\n") as f:
        f.write(texto.replace(viejo, nuevo))
    print("borrador %s ← %s" % (borrador, ruta))
