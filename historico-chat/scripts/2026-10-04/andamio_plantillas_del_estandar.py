# -*- coding: utf-8 -*-
"""El andamio toma las plantillas del estándar y arma sus enlaces hacia el
estándar, desde cualquier proyecto (análisis 1 del pendiente 110, acuerdo 2)."""
import io
import os

P = os.path.join(os.path.dirname(__file__), "..", "..", "..", "validadores", "andamio.py")
t = io.open(P, encoding="utf-8").read()

inicio = t.index("def _reenlazar(texto, origen_plantilla, destino, raiz):")
fin = t.index("def _escribir(ruta, texto, escribir):")
nuevo = '''def _hacia(base, destino):
    """El enlace de `destino` a `base`: relativo, o absoluto si están en otra unidad."""
    try:
        return os.path.relpath(base, destino).replace("\\\\", "/")
    except ValueError:
        return os.path.abspath(base).replace("\\\\", "/")


def _reenlazar(texto, origen_plantilla, destino):
    """Traslada a la carpeta de destino los enlaces que la plantilla hace a la raíz.

    Las plantillas son del estándar, y sus enlaces a la raíz apuntan al estándar
    (`base/`, `plantillas/`). Desde un proyecto se arman hacia Cimiento, no hacia
    el proyecto, donde no existen (análisis 1 del pendiente 110, acuerdo 2).
    Solo se traslada el prefijo que **llega exactamente a la raíz** —un `../`
    que se queda en `plantillas/` apunta a otra cosa y no se toca—, y el
    marcador de la ruta del estándar.
    """
    hacia_estandar = _hacia(comun.RAIZ, destino)
    desde_plantilla = os.path.relpath(
        comun.RAIZ, os.path.dirname(os.path.abspath(origen_plantilla))).replace("\\\\", "/")
    patron = re.compile(r"\\]\\(" + re.escape(desde_plantilla) + r"/(?!\\.\\.)")
    texto = patron.sub("](" + hacia_estandar + "/", texto)
    return texto.replace(MARCADOR_RAIZ, hacia_estandar)


'''
t = t[:inicio] + nuevo + t[fin:]

cambios = [
    ("        origen = os.path.join(raiz, plantilla)\n",
     "        origen = os.path.join(comun.RAIZ, plantilla)      # las plantillas son del estándar\n"),
    ("        texto = _reenlazar(texto, origen, destino, raiz)\n",
     "        texto = _reenlazar(texto, origen, destino)\n"),
    ("    origen = os.path.join(raiz, PLANTILLA_HU)\n",
     "    origen = os.path.join(comun.RAIZ, PLANTILLA_HU)      # las plantillas son del estándar\n"),
    ("    texto = _reenlazar(leer(origen), origen, destino, raiz)\n",
     "    texto = _reenlazar(leer(origen), origen, destino)\n"),
    ("    origen = os.path.join(raiz, PLANTILLA_PENDIENTE)\n",
     "    origen = os.path.join(comun.RAIZ, PLANTILLA_PENDIENTE)      # las plantillas son del estándar\n"),
    ("    texto = _reenlazar(leer(origen), origen, carpeta, raiz)\n",
     "    texto = _reenlazar(leer(origen), origen, carpeta)\n"),
    ('''    if con_historia:
        epica, hu = (hu_ref.replace("\\\\", "/").split("/") + [""])[:2]
        dueno = os.path.join(raiz, CARPETA, epica, hu)
        if not os.path.isfile(os.path.join(dueno, hu + ".md")):
            raise ValueError("no existe la historia: %s" % hu_ref)
''',
     '''    if con_historia:
        epica, hu = (hu_ref.replace("\\\\", "/").strip("/").split("/") + [""])[:2]
        if hu:
            dueno = os.path.join(raiz, CARPETA, epica, hu)
            if not os.path.isfile(os.path.join(dueno, hu + ".md")):
                raise ValueError("no existe la historia: %s" % hu_ref)
        else:
            # El pendiente de una épica entera vive en su carpeta `pendientes/`
            # (análisis 1 del pendiente 110, acuerdo 2).
            dueno = os.path.join(raiz, CARPETA, epica)
            if not os.path.isfile(os.path.join(dueno, "epica.md")):
                raise ValueError("no existe la épica: %s" % hu_ref)
'''),
]
for viejo, nuevo_txt in cambios:
    assert t.count(viejo) == 1, viejo[:60]
    t = t.replace(viejo, nuevo_txt)
io.open(P, "w", encoding="utf-8", newline="\n").write(t)
print("listo")
