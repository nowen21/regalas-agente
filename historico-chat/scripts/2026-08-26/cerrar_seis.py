# -*- coding: utf-8 -*-
"""Marca la estación y el estado de las seis fases que se cerraron.

**No se inventa nada.** La estación pasa de 11 a cerrada porque el documento
de cierre ya existe; el estado de la historia pasa a `Terminada` porque su
única fase está cerrada y su resultado dice Cumple.
"""
import io
import os
import re

os.chdir(r"c:\Ing. Jose\ia\agente")

SEIS = [
 ("EP-001-cuerpo-de-reglas-heredable/HU-004-conducta-de-la-ia",
  "A-EP-001-HU-004-retrodocumentar-la-conducta-de-la-ia"),
 ("EP-002-versionado-y-adopcion/HU-002-registro-de-cambios",
  "A-EP-002-HU-002-retrodocumentar-el-registro-de-cambios"),
 ("EP-003-documentos-modelo-y-procedimientos/HU-007-procedimiento-que-dirige",
  "A-EP-003-HU-007-retrodocumentar-el-procedimiento-que-dirige"),
 ("EP-003-documentos-modelo-y-procedimientos/HU-008-puntos-de-aprobacion",
  "A-EP-003-HU-008-retrodocumentar-los-puntos-de-aprobacion"),
 ("EP-004-comprobacion-automatica/HU-001-criterio-de-lo-comprobable",
  "A-EP-004-HU-001-retrodocumentar-el-criterio-de-lo-comprobable"),
 ("EP-005-automatismos-que-no-dependen-de-la-memoria/HU-006-bateria-antes-de-publicar",
  "A-EP-005-HU-006-la-bateria-antes-de-publicar"),
]

EST = re.compile(r"\*\*Estación actual:\*\*[^\n]*")
ESTADO_HU = re.compile(r"^(\|\s*\*\*Estado\*\*\s*\|\s*)([^|]+?)(\s*\|)", re.M)

NOTA = ("\n\n> **La fase se cerró el 2026-08-26.** Estaba ejecutada desde el "
        "2026-08-22 con sus criterios en verde, y lo que faltaba era el "
        "documento de cierre. Las dos fechas se dejan escritas porque son "
        "distintas: no se verificó hoy lo que se verificó entonces.")

tocados = 0
for carpeta_hu, fase in SEIS:
    base = os.path.join("documentacion", "epicas", *carpeta_hu.split("/"))

    # 1. La estación de la fase.
    ruta = os.path.join(base, fase, "estado-fase.md")
    t = io.open(ruta, encoding="utf-8").read()
    m = EST.search(t)
    assert m, "sin línea de estación: %s" % fase
    t = t[:m.start()] + ("**Estación actual:** cerrada. **Última puerta "
                         "pasada:** 11, el cierre documental." + NOTA) + t[m.end():]
    io.open(ruta, "w", encoding="utf-8", newline="\n").write(t)

    # 2. El estado de la historia.
    nombre_hu = os.path.basename(carpeta_hu)
    ruta_hu = os.path.join(base, "%s.md" % nombre_hu)
    t = io.open(ruta_hu, encoding="utf-8").read()
    m = ESTADO_HU.search(t)
    assert m, "sin campo Estado: %s" % nombre_hu
    antes = m.group(2).strip()
    if not antes.startswith("Terminada"):
        t = t[:m.start()] + m.group(1) + "Terminada" + m.group(3) + t[m.end():]
        io.open(ruta_hu, "w", encoding="utf-8", newline="\n").write(t)
    print("   %-56s %s -> Terminada" % (nombre_hu[:56], antes[:22]))
    tocados += 1

print()
print("Fases cerradas y marcadas: %d" % tocados)
