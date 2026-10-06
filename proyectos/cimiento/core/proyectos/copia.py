# -*- coding: utf-8 -*-
"""`EP-025·HU-013` · La copia de la configuración en la carpeta del proyecto.

Lo que se maneja desde la interfaz vive en la base; lo que un proyecto necesita
como archivo es una copia que Cimiento genera, nunca la fuente (análisis 3 del
pendiente 119, acuerdo 3). Se escribe cada vez que cambia algo que la afecta,
en `.agente/configuracion.md`, que es local: el instalador lo deja ignorado.
"""
import os

from django.utils import timezone

from . import ajustes as catalogo

ARCHIVO = os.path.join(".agente", "configuracion.md")


def texto_de(proyecto, ahora=None):
    ahora = timezone.localtime(ahora or timezone.now())
    filas = ["| %s | %s | %s |" % (catalogo.AJUSTES[clave].titulo, valor, capa)
             for clave, (valor, capa) in proyecto.ajustes().items()]
    suspensiones = ["| %s | %s | %s |" % ("El freno entero" if s.tipo == catalogo.ENGANCHE else s.nombre,
                                         s.motivo.replace("|", "/"), timezone.localtime(s.vence).strftime("%Y-%m-%d %H:%M"))
                    for s in proyecto.suspensiones_vigentes()]
    return "\n".join([
        "# Configuración de «%s»" % proyecto.nombre, "",
        "> La genera Cimiento desde su base cada vez que cambia (`EP-025·HU-013`). No se edita: "
        "lo que haya que cambiar se cambia en Cimiento, en «Configuración» o en «Proyectos».", "",
        "Generada el %s." % ahora.strftime("%Y-%m-%d a las %H:%M"), "",
        "## Ajustes", "",
        "| Ajuste | Vale | De dónde sale |", "|---|---|---|", *filas, "",
        "## Suspensiones vigentes", "",
        *(["| Qué | Motivo | Vence |", "|---|---|---|", *suspensiones] if suspensiones else ["Ninguna."]),
        ""])


def escribir(proyecto):
    """Escribe la copia del proyecto. Devuelve la ruta, o None si su carpeta no está en esta máquina."""
    if not proyecto.ruta or not os.path.isdir(proyecto.ruta):
        return None
    ruta = os.path.join(proyecto.ruta, ARCHIVO)
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto_de(proyecto))
    return ruta


def escribir_todas():
    """Cuando cambia la base, cambia la copia de todos los proyectos activos."""
    from .models import Proyecto
    return [r for r in (escribir(p) for p in Proyecto.objects.filter(activo=True)) if r]
