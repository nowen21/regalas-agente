# -*- coding: utf-8 -*-
"""Las comprobaciones de las fases D de EP-005-HU-001 y EP-003-HU-002.

**Se corre, no se cita.** Las dos fases vuelven a medir en vez de apoyarse en
lo que midio la fase A: una fase que hereda la medicion de otra hereda tambien
su error, y el punto de estas dos es no heredarlo.
"""
import io
import os
import re
import subprocess
import sys

RAIZ = r"c:\Ing. Jose\ia\agente"
sys.path.insert(0, os.path.join(RAIZ, "validadores"))
import enmascarar                                        # noqa: E402
import trazabilidad                                      # noqa: E402

print("=" * 70)
print("FASE D de EP-005-HU-001 - la privacidad")
print("=" * 70)

print("\nCP-001 - enmascara:")
for entrada in ("API_KEY=supersecreto123456",
                "password: MiClave123456",
                "la contrasena: Patito2026"):
    salida, cuantas = enmascarar.enmascarar(entrada)
    print("   %-34s -> %s" % (entrada, salida))

print("\nCP-002 - NO enmascara de mas (el critico):")
for entrada in ("la clave del asunto es que el proceso sirva",
                "clave = h.regla or algo",
                "token: xyz",
                "API_KEY=os.environ['X']",
                "password: changeme"):
    salida, cuantas = enmascarar.enmascarar(entrada)
    igual = "INTACTO" if salida == entrada else "!! TAPADO DE MAS"
    print("   %-44s -> %s" % (entrada, igual))

print("\nCP-003 - esta conectado a quien escribe:")
hist = io.open(os.path.join(RAIZ, "validadores", "historico.py"),
               encoding="utf-8").read()
gancho = io.open(os.path.join(RAIZ, "adaptadores", "claude-code",
                              "hook_historico.py"), encoding="utf-8").read()
print("   hook_historico.py llama a historico.anotar_usuario:",
      "anotar_usuario" in gancho)
print("   hook_historico.py llama a historico.anotar_agente: ",
      "anotar_agente" in gancho)
print("   historico.py llama al enmascarado, veces:          ",
      hist.count("enmascarar.enmascarar("))
print("   ...y las dos rutas lo hacen ANTES de escribir:")
for nombre in ("anotar_usuario", "anotar_agente"):
    i = hist.index("def %s" % nombre)
    cuerpo = hist[i:i + 2500]
    orden_mask = cuerpo.find("enmascarar.enmascarar(")
    orden_escr = min([x for x in (cuerpo.find("io.open"), cuerpo.find("_escribir"),
                                  cuerpo.find("open(")) if x > 0] or [10 ** 6])
    print("      %-16s enmascara en %5d, escribe en %5d -> %s"
          % (nombre, orden_mask, orden_escr,
             "ANTES" if 0 <= orden_mask < orden_escr else "REVISAR"))

print()
print("=" * 70)
print("FASE D de EP-003-HU-002 - los tres modelos y la cadena")
print("=" * 70)

MOLDES = os.path.join(RAIZ, "plantillas", "ciclo-vida-proyectos")
print("\nCP-001 - los tres modelos existen:")
for nombre, cual in (("01-planteamiento.md", "la necesidad"),
                     ("03-epica.md", "la epica"),
                     ("04-HU.md", "la historia")):
    hay = os.path.isfile(os.path.join(MOLDES, nombre))
    print("   %-24s (%s): %s" % (nombre, cual, "esta" if hay else "!! FALTA"))

hu = io.open(os.path.join(MOLDES, "04-HU.md"), encoding="utf-8").read()
ep = io.open(os.path.join(MOLDES, "03-epica.md"), encoding="utf-8").read()
print("   el molde de la historia nombra su epica:", "pica" in hu[:4000])
print("   el molde de la epica lista sus historias:",
      bool(re.search(r"HU.*\|.*T[ií]tulo|Historias de usuario", ep)))

print("\nCP-002 - la cadena, corrida sobre el arbol real (no citada):")
hallazgos = trazabilidad.validar(RAIZ)
rotos = [h for h in hallazgos if "DOC16" in h.mensaje or "bidirec" in h.mensaje]
epicas = len([d for d in os.listdir(os.path.join(RAIZ, "documentacion", "epicas"))
              if d.startswith("EP-")])
historias = 0
base = os.path.join(RAIZ, "documentacion", "epicas")
for e in os.listdir(base):
    if not e.startswith("EP-"):
        continue
    historias += len([d for d in os.listdir(os.path.join(base, e))
                      if d.startswith("HU-") and
                      os.path.isdir(os.path.join(base, e, d))])
print("   medido sobre %d epicas y %d historias" % (epicas, historias))
print("   fallas de enlace bidireccional: %d" % len(rotos))
for h in rotos[:5]:
    print("      %s" % h.mensaje[:110])

print("\nCP-003 - el hueco que la fase A senalo:")
plant = os.path.join(RAIZ, "prompts", "cimiento-planteamiento.md")
hay = os.path.isfile(plant)
print("   el planteamiento de esta casa existe:", hay)
if hay:
    texto = io.open(plant, encoding="utf-8").read()
    marcadores = len(re.findall("«[^»\n]{0,120}»|AAAA-MM-DD", texto))
    print("   lineas: %d, marcadores del molde sin llenar: %d"
          % (len(texto.splitlines()), marcadores))
cerrado = os.path.isfile(os.path.join(RAIZ, "pendientes", "hecho",
                                      "el-estandar-tiene-su-planteamiento.md"))
print("   el pendiente 56 que cito la fase A esta en hecho/:", cerrado)
