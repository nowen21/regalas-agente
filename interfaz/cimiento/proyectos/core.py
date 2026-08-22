# -*- coding: utf-8 -*-
"""Importar, exportar y medir: lo que el registro hace con el mundo de afuera.

- **Importar**: lee `plantillas/proyectos.md` (donde el instalador sigue
  anotando) y sube al registro lo que falte, sin pisar lo editado acá.
- **Exportar**: regenera ese mismo archivo desde el registro, porque el
  instalador y los avisos de cierre lo leen. El archivo deja de escribirse a
  mano: es una salida.
- **Medir**: corre los lectores del estándar (`expediente`, y los conteos de la
  cadena) sobre la carpeta real del proyecto.
"""
import io
import os
import re
import sys

from .models import Proyecto

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
REGISTRO_MD = os.path.join(RAIZ, "plantillas", "proyectos.md")
VALIDADORES = os.path.join(RAIZ, "validadores")

CABECERA = """# Proyectos que usan el agente  ·  `«LOCAL · NO versionar»`

> Registro central de los proyectos configurados con este estándar **en esta máquina**. NO se versiona (data local, como la memoria `.db`). **Este archivo se genera desde el registro de la interfaz** (`interfaz/proyectos/`): se edita allá, no acá. El instalador anota acá los proyectos nuevos y la interfaz los importa.

| Proyecto | Ruta | Scope de memoria | Stack |
|---|---|---|---|
"""

_FILA = re.compile(r"^\|\s*(?P<nombre>[^|]+?)\s*\|\s*`?(?P<ruta>[^|`]+?)`?\s*\|"
                   r"\s*`?(?P<scope>[^|`]*?)`?\s*\|\s*(?P<stack>[^|]*?)\s*\|\s*$")


def importar():
    """Sube al registro las filas del .md que no estén. Devuelve cuántas."""
    if not os.path.isfile(REGISTRO_MD):
        return 0
    nuevas = 0
    for linea in io.open(REGISTRO_MD, encoding="utf-8"):
        m = _FILA.match(linea.strip())
        if not m or m.group("nombre") in ("Proyecto", "---"):
            continue
        if set(m.group("nombre")) <= {"-"}:
            continue
        datos = {k: m.group(k).strip() for k in ("nombre", "ruta", "scope", "stack")}
        if not datos["ruta"] or datos["nombre"] == "Proyecto":
            continue
        _, creado = Proyecto.objects.get_or_create(
            nombre=datos["nombre"],
            defaults={"ruta": datos["ruta"], "scope": datos["scope"],
                      "stack": datos["stack"] or "por detectar"})
        nuevas += 1 if creado else 0
    return nuevas


class RegistroVacio(RuntimeError):
    """El registro devolvió cero activos y el .md tenía filas: no se sobrescribe."""


def _filas_en_md():
    if not os.path.isfile(REGISTRO_MD):
        return 0
    return sum(1 for l in io.open(REGISTRO_MD, encoding="utf-8")
               if _FILA.match(l.strip()) and not l.startswith("| Proyecto |"))


def exportar():
    """Regenera `plantillas/proyectos.md` desde el registro (solo activos).

    **Nunca escribe cero filas encima de un archivo que tenía filas.** Pasó
    (pendiente 76): las pruebas de las vistas exportaban su base de pruebas,
    vacía, sobre el registro real, y el checklist de los proyectos reprobaba
    «registro» en cada mensaje. Un registro vacío de verdad se exporta solo si
    el archivo ya estaba vacío; si no, se lanza `RegistroVacio` y el archivo
    queda como estaba.
    """
    filas = []
    for p in Proyecto.objects.filter(activo=True):
        filas.append(f"| {p.nombre} | `{p.ruta}` | `{p.scope}` | {p.stack} |")
    if not filas and _filas_en_md() > 0:
        raise RegistroVacio(
            "el registro no tiene proyectos activos pero plantillas/proyectos.md "
            "tiene filas: no se sobrescribe (¿base equivocada o vacía?)")
    texto = CABECERA + "\n".join(filas) + ("\n" if filas else "")
    io.open(REGISTRO_MD, "w", encoding="utf-8", newline="").write(texto)
    return len(filas)


def registrar(nombre, ruta, scope="", stack="por detectar"):
    """Alta o actualización de ruta desde afuera (el instalador). Exporta."""
    proyecto, creado = Proyecto.objects.get_or_create(
        nombre=nombre, defaults={"ruta": ruta, "scope": scope, "stack": stack})
    if not creado and proyecto.ruta != ruta:
        proyecto.ruta = ruta
        proyecto.save()
    exportar()
    return creado


def medir(proyecto):
    """`(existe_ruta, lineas_md)`: el expediente del proyecto, para renderizar."""
    if VALIDADORES not in sys.path:
        sys.path.insert(0, VALIDADORES)
    import expediente
    if not os.path.isdir(proyecto.ruta):
        return False, [f"La ruta `{proyecto.ruta}` no existe en esta máquina."]
    lineas, _hallazgos = expediente.reporte(proyecto.ruta)
    return True, lineas
