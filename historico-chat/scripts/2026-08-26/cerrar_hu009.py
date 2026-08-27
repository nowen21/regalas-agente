# -*- coding: utf-8 -*-
"""Cierra la HU-009 y el hallazgo H-28 del resumen."""
import io
import os

os.chdir(r"c:\Ing. Jose\ia\agente")
BASE = ("documentacion/epicas/EP-007-instalacion-y-actualizacion/"
        "HU-009-las-rutas-largas-no-detienen-el-guardado/")
FASE = BASE + "A-EP-007-HU-009-el-instalador-deja-puestas-las-rutas-largas/"
HU = BASE + "HU-009-las-rutas-largas-no-detienen-el-guardado.md"

CAMBIOS = [
 (FASE + "estado-fase.md",
  "**Estación actual:** 7, planificador de tareas. **Última puerta pasada:** 6.",
  "**Estación actual:** 12, commit. **Última puerta pasada:** 11."),

 (HU, "| **Estado** | Pendiente |", "| **Estado** | Terminada |"),
 (HU,
  "| `A-EP-007-HU-009-el-instalador-deja-puestas-las-rutas-largas` | CA-01, "
  "CA-02, CA-03 | (vacío) | por escribir | por escribir | por escribir | "
  "Pendiente |",
  "| [`A-EP-007-HU-009-el-instalador-deja-puestas-las-rutas-largas`]"
  "(A-EP-007-HU-009-el-instalador-deja-puestas-las-rutas-largas/) | CA-01, "
  "CA-02, CA-03 | (vacío) | [plan_trabajo]"
  "(A-EP-007-HU-009-el-instalador-deja-puestas-las-rutas-largas/plan_trabajo.md) "
  "| [plan_pruebas]"
  "(A-EP-007-HU-009-el-instalador-deja-puestas-las-rutas-largas/plan_pruebas.md) "
  "| [resultado]"
  "(A-EP-007-HU-009-el-instalador-deja-puestas-las-rutas-largas/resultado_pruebas.md) "
  "· cumple | Terminada |"),
 (HU, "- [ ] Código implementado y en rama principal",
  "- [x] Código implementado y en rama principal"),
 (HU, "- [ ] Pruebas unitarias e integración pasando",
  "- [x] Pruebas unitarias e integración pasando — 402 de 402"),
 (HU, "- [ ] Todos los criterios de aceptación verificados",
  "- [x] Todos los criterios de aceptación verificados"),
 (HU, "- [ ] Requisitos no funcionales validados",
  "- [x] Requisitos no funcionales validados"),
 (HU, "- [ ] Documentación técnica y de usuario actualizada",
  "- [x] Documentación técnica y de usuario actualizada"),
 (HU,
  "| 2026-08-26 | Agente, con el usuario | Creación de la HU. Sale del "
  "hallazgo `H-28` y de la señal `S-042` |",
  "| 2026-08-26 | Agente, con el usuario | Creación de la HU. Sale del "
  "hallazgo `H-28` y de la señal `S-042` |\n"
  "| 2026-08-26 | Agente | Cerrada la fase `A`. Los tres criterios cumplidos; "
  "dos defectos, los dos en la forma de probar (`S-051`) |"),
]

for ruta, viejo, nuevo in CAMBIOS:
    t = io.open(ruta, encoding="utf-8").read()
    assert t.count(viejo) == 1, "no coincide en %s -> %s" % (ruta[-22:], viejo[:44])
    io.open(ruta, "w", encoding="utf-8", newline="\n").write(
        t.replace(viejo, nuevo, 1))

# -- H-28 del resumen: cierra --
ruta = "historico-chat/resumenes/2026-08-22/sesion-6.md"
t = io.open(ruta, encoding="utf-8").read()

H28 = [
 ("- **Qué lo soluciona:** `core.longpaths` en este repositorio, y con eso "
  "entró.",
  "- **Qué lo soluciona:** se resolvió acá, por la cadena: `EP-007` · `HU-009` "
  "· fase `A`. **El instalador lo deja puesto**, sin pisar un `false` que "
  "alguien haya decidido y sin tocar la configuración de la máquina."),
 ("- **Estado:** resuelto acá para esta máquina; abierto lo de quien clone.",
  "- **Estado:** resuelto acá lo que se puede resolver. **Lo de quien clone y "
  "no instale no tiene arreglo desde el repositorio**, y por eso quedó escrito "
  "qué hacer en el documento de despliegue."),
 ("- **Dispara:** por decidir con el usuario, y **con una opción menos de las "
  "que parecía**. Acortar el prefijo se midió y no alcanza: ahorra 15 "
  "caracteres y la ruta más larga quedaría en 292, todavía sobre 260. Quedan "
  "dos: que el instalador de la plataforma active `core.longpaths`, o acortar "
  "la convención de carpetas del estándar — que es mucho más grande y toca "
  "todo lo ya escrito.",
  "- **Dispara:** la [HU-009](../../../documentacion/epicas/"
  "EP-007-instalacion-y-actualizacion/"
  "HU-009-las-rutas-largas-no-detienen-el-guardado/"
  "HU-009-las-rutas-largas-no-detienen-el-guardado.md), construida y cerrada "
  "el 2026-08-26. **Acortar nombres se descartó midiendo**: la holgura del "
  "peor caso son 8 caracteres y anidar necesita 55; acortar la convención "
  "ahorra 14. Ninguna combinación crea los 55 que faltan."),
 ("- **Dónde queda:** la señal `S-042` y el cuerpo del commit que guardó lo "
  "traído.",
  "- **Dónde queda:** `_rutas_largas` en [validadores/instalar.py]"
  "(../../../validadores/instalar.py), la §3.1 del documento de "
  "[despliegue](../../../cvds/despliegue/README.md), y las señales `S-042` y "
  "`S-051`."),
 ("- **Cerrado en:** —\n- **Con qué se retoma:** decidir entre que el "
  "instalador active `core.longpaths` o acortar la convención de carpetas — "
  "sabiendo que lo segundo arregla también los 81 que ya están al borde sin "
  "que nadie los haya anidado.",
  "- **Cerrado en:** 2026-08-22 · sesion-6\n- **Con qué se retoma:** —"),
]
for viejo, nuevo in H28:
    assert t.count(viejo) == 1, "H-28: no coincide -> %s" % viejo[:46]
    t = t.replace(viejo, nuevo, 1)

viejo_cierre = ("**`H-34` también cerró, y cerró corrigiéndose**: la regla que "
                "decía faltar existía desde antes. Queda **uno** abierto y sin "
                "pendiente creado: `H-28`, el tope de ruta en Windows. Falta "
                "una decisión del usuario, que es la que dice qué pendiente "
                "escribir.")
nuevo_cierre = ("**`H-28` también cerró**, y con él **todos los hallazgos de "
                "la sesión**. El tope de ruta se resolvió por la cadena, "
                "después de medir que ningún cambio de nombres alcanzaba. "
                "**No queda ninguno abierto**, así que no falta ningún "
                "pendiente por escribir.")
assert t.count(viejo_cierre) == 1, "cierre no coincide"
t = t.replace(viejo_cierre, nuevo_cierre, 1)
t = t.replace("| Todo hallazgo abierto tiene su pendiente creado | ☐ · falta "
              "el de `H-28` |",
              "| Todo hallazgo abierto tiene su pendiente creado | ☑ · no "
              "queda ninguno abierto |", 1)

io.open(ruta, "w", encoding="utf-8", newline="\n").write(t)
print("HU-009 cerrada y H-28 también")
