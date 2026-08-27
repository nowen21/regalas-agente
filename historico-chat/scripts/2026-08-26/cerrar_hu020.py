# -*- coding: utf-8 -*-
"""Cierra la HU-020: estado de la fase, §8 y §1 de la historia."""
import io
import os

os.chdir(r"c:\Ing. Jose\ia\agente")
BASE = ("documentacion/epicas/EP-004-comprobacion-automatica/"
        "HU-020-el-inventario-heredado-tampoco-se-mantiene-a-mano/")
FASE = BASE + "A-EP-004-HU-020-lo-que-se-hereda-tampoco-se-cuenta-a-mano/"

CAMBIOS = [
 (FASE + "estado-fase.md",
  "**Estación actual:** 7, planificador de tareas. **Última puerta pasada:** 6.",
  "**Estación actual:** 12, commit. **Última puerta pasada:** 11."),
 (FASE + "estado-fase.md",
  "| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☐ |",
  "| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ |"),
 (FASE + "estado-fase.md",
  "| 8 | Implementador | implementado + pruebas verdes | ☐ |",
  "| 8 | Implementador | implementado + pruebas verdes | ☑ |"),
 (FASE + "estado-fase.md",
  "| 9 | Verificador | trazabilidad sin faltantes | ☐ |",
  "| 9 | Verificador | trazabilidad sin faltantes | ☑ |"),
 (FASE + "estado-fase.md",
  "| 10 | Crítico | sin hallazgos graves | ☐ |",
  "| 10 | Crítico | sin hallazgos graves | ☑ |"),
 (FASE + "estado-fase.md",
  "| 11 | Cierre documental + señales | docs y señales al día | ☐ |",
  "| 11 | Cierre documental + señales | docs y señales al día | ☑ |"),
 (FASE + "estado-fase.md",
  "| **Concepto** | Todavía no se ejecutó |",
  "| **Concepto** | **Cumple**, en el ciclo 2 |"),
 (FASE + "estado-fase.md",
  "| **CA cumplidos** | 0 de 4 |", "| **CA cumplidos** | 4 de 4 |"),
 (FASE + "estado-fase.md",
  '| **CA en "No"** | Ninguno todavía: no se ha corrido nada |',
  '| **CA en "No"** | Ninguno |'),
 (FASE + "estado-fase.md",
  "| **Defectos abiertos aceptados** | Ninguno |",
  "| **Defectos abiertos aceptados** | Ninguno de esta fase. `DEF-03` "
  "reportado y **no corregido**, por estar fuera de lo declarado |"),
 (FASE + "estado-fase.md",
  "| **Fuente** | El `resultado_pruebas.md` de esta fase, todavía sin llenar |",
  "| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) · 381 pruebas, OK |"),
 (FASE + "estado-fase.md",
  "| T-01 a T-16 | Pendiente | No empiezan hasta que los dos planes estén "
  "aprobados (`02·F4`) |",
  "| T-01 a T-16 | Hecha | Las dieciséis |"),
 (FASE + "estado-fase.md",
  "**Hechas:** 0 de 16. **Bloqueadas:** ninguna, y ninguna empezada.",
  "**Hechas:** 16 de 16. **Bloqueadas:** ninguna."),
 (FASE + "estado-fase.md",
  "| Que un estándar puede arreglar algo para sí mismo y no repartirlo, y que "
  "eso pesa más que en un proyecto porque lo que reparte se multiplica | Por "
  "registrar al cerrar la fase |",
  "| Que un estándar puede arreglar algo para sí mismo y no repartirlo, y que "
  "eso pesa más que en un proyecto porque lo que reparte se multiplica | "
  "`S-045` |"),
 (FASE + "estado-fase.md",
  "| Que la comprobación de la fase anterior nació atada a una ruta fija, y "
  "nadie lo declaró | Por registrar al cerrar la fase |",
  "| Que la comprobación de la fase anterior nació atada a una ruta fija, y "
  "nadie lo declaró | `S-045` |\n"
  "| Que el mismo defecto tiene dos formas: el valor puesto y el hueco por "
  "llenar, y una sola expresión no caza las dos | `S-046` |\n"
  "| Que «no dupliques lo derivable» no aplica a un hecho histórico: la "
  "versión al cerrar es una foto, no una cuenta | `S-047` |"),
 (FASE + "estado-fase.md",
  "- **Esperando la aprobación del usuario** sobre el "
  "[plan_trabajo.md](plan_trabajo.md) y el [plan_pruebas.md](plan_pruebas.md). "
  "Hasta que llegue, no se toca nada (`02·F4`).\n"
  "- **Ninguna duda técnica abierta.** La única que había —si un proyecto "
  "puede correr el comando— se resolvió corriéndolo antes de escribir el "
  "plan, y está en su §2.",
  "- **Esperando autorización para el commit.** Construida, probada y "
  "documentada.\n"
  "- **Una decisión para el usuario:** el cierre de la fase anterior dice «la "
  "versión que declara `VERSION`» en vez de su número, y al subir a `34.2.0` "
  "pasó a afirmar que cerró bajo una versión que no existía cuando cerró. Es "
  "una línea. **No se corrigió porque el plan no declara ese archivo** "
  "(`02·F8`). Está en el cierre §6 y en `S-047`."),
 (FASE + "estado-fase.md",
  "No está bloqueada. Está esperando aprobación, que es la estación 7 haciendo "
  "lo suyo.",
  "No se bloqueó en ningún momento."),

 # -- La historia --
 (BASE + "HU-020-el-inventario-heredado-tampoco-se-mantiene-a-mano.md",
  "| **Estado** | Escrita el 2026-08-26. Sin construir |",
  "| **Estado** | **Cumplida.** Los cuatro criterios y su transversal, "
  "verificados el 2026-08-26 |"),
 (BASE + "HU-020-el-inventario-heredado-tampoco-se-mantiene-a-mano.md",
  "| `A-EP-004-HU-020-lo-que-se-hereda-tampoco-se-cuenta-a-mano` | CA-01, "
  "CA-02, CA-03, CA-04 | (vacío) | por escribir | por escribir | por escribir "
  "| Sin empezar |",
  "| [`A-EP-004-HU-020-lo-que-se-hereda-tampoco-se-cuenta-a-mano`]"
  "(A-EP-004-HU-020-lo-que-se-hereda-tampoco-se-cuenta-a-mano/) | CA-01, "
  "CA-02, CA-03, CA-04 | (vacío) | [plan_trabajo]"
  "(A-EP-004-HU-020-lo-que-se-hereda-tampoco-se-cuenta-a-mano/plan_trabajo.md) "
  "| [plan_pruebas]"
  "(A-EP-004-HU-020-lo-que-se-hereda-tampoco-se-cuenta-a-mano/plan_pruebas.md) "
  "| [resultado]"
  "(A-EP-004-HU-020-lo-que-se-hereda-tampoco-se-cuenta-a-mano/resultado_pruebas.md) "
  "· cumple | Cerrada |"),
 (BASE + "HU-020-el-inventario-heredado-tampoco-se-mantiene-a-mano.md",
  "- [ ] Código implementado y en rama principal",
  "- [x] Código implementado y en rama principal"),
 (BASE + "HU-020-el-inventario-heredado-tampoco-se-mantiene-a-mano.md",
  "- [ ] Pruebas unitarias e integración pasando",
  "- [x] Pruebas unitarias e integración pasando — 381 de 381"),
 (BASE + "HU-020-el-inventario-heredado-tampoco-se-mantiene-a-mano.md",
  "- [ ] Todos los criterios de aceptación verificados",
  "- [x] Todos los criterios de aceptación verificados"),
 (BASE + "HU-020-el-inventario-heredado-tampoco-se-mantiene-a-mano.md",
  "- [ ] Requisitos no funcionales validados",
  "- [x] Requisitos no funcionales validados"),
 (BASE + "HU-020-el-inventario-heredado-tampoco-se-mantiene-a-mano.md",
  "- [ ] Documentación técnica y de usuario actualizada",
  "- [x] Documentación técnica y de usuario actualizada"),
 (BASE + "HU-020-el-inventario-heredado-tampoco-se-mantiene-a-mano.md",
  "| 2026-08-26 | Agente, con el usuario | Creación de la HU. Sale del "
  "hallazgo H-31, y de verificar que la comprobación de la HU-019 mira una "
  "ruta fija |",
  "| 2026-08-26 | Agente, con el usuario | Creación de la HU. Sale del "
  "hallazgo H-31, y de verificar que la comprobación de la HU-019 mira una "
  "ruta fija |\n| 2026-08-26 | Agente | Cerrada la fase `A`. Los cuatro "
  "criterios cumplidos; tres defectos encontrados, dos corregidos y uno "
  "reportado por estar fuera de lo declarado (`S-045`, `S-046`, `S-047`) |"),
]

for ruta, viejo, nuevo in CAMBIOS:
    t = io.open(ruta, encoding="utf-8").read()
    assert t.count(viejo) == 1, "no coincide en %s -> %s" % (ruta[-24:], viejo[:44])
    io.open(ruta, "w", encoding="utf-8", newline="\n").write(
        t.replace(viejo, nuevo, 1))

print("HU-020 cerrada: %d cambios" % len(CAMBIOS))
