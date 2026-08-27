# -*- coding: utf-8 -*-
"""Cierra la HU-012: estado de la fase, §8 y §1 de la historia."""
import io
import os

os.chdir(r"c:\Ing. Jose\ia\agente")
BASE = ("documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/"
        "HU-012-una-sola-palabra-para-cada-estado/")
FASE = BASE + "A-EP-003-HU-012-una-sola-palabra-por-estado/"
HU = BASE + "HU-012-una-sola-palabra-para-cada-estado.md"

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
  "| **Fuente** | El `resultado_pruebas.md` de esta fase, todavía sin llenar |",
  "| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) · 396 pruebas, OK |"),
 (FASE + "estado-fase.md",
  "| T-01 a T-14 | Pendiente | No empiezan hasta que los dos planes estén "
  "aprobados (`02·F4`) |",
  "| T-01 a T-14 | Terminada | Las catorce |"),
 (FASE + "estado-fase.md",
  "**Hechas:** 0 de 14. **Bloqueadas:** ninguna, y ninguna empezada.",
  "**Hechas:** 14 de 14. **Bloqueadas:** ninguna."),
 (FASE + "estado-fase.md",
  "| Que el desorden no era descuido: los moldes del propio estándar enseñaban "
  "tres palabras para lo mismo | Por registrar al cerrar la fase |",
  "| Que el desorden no era descuido: los moldes del propio estándar enseñaban "
  "tres palabras para lo mismo | `S-049` |"),
 (FASE + "estado-fase.md",
  "| Que el estado de una épica estaba definido dos veces con listas que no "
  "coincidían | Por registrar al cerrar la fase |",
  "| Que el estado de una épica estaba definido dos veces con listas que no "
  "coincidían | `S-049` |"),
 (FASE + "estado-fase.md",
  "| Que un vocabulario sin sitio único no se puede comprobar, y por eso nada "
  "cazó el error de `S-048` | Por registrar al cerrar la fase |",
  "| Que un vocabulario sin sitio único no se puede comprobar, y por eso nada "
  "cazó el error de `S-048` | `S-049` |\n"
  "| Que una comprobación que reporta fuera de su tema apaga las demás | "
  "`S-050` |"),
 (FASE + "estado-fase.md",
  "- **Esperando la aprobación del usuario** sobre el "
  "[plan_trabajo.md](plan_trabajo.md) y el [plan_pruebas.md](plan_pruebas.md). "
  "Hasta que llegue, no se toca nada (`02·F4`).\n"
  "- **Una duda técnica, y se resuelve leyendo:** qué significa `Aprobada` en "
  "las dos historias que lo usan. Está en el plan §2.7 y la cierra `T-04`.\n"
  "- **Una decisión que el usuario ya conoce y quedó fuera de alcance:** el "
  "vocabulario está en inglés —`Backlog`, `Ready`, `Done`— y eso choca con "
  "`01·C8`. Se dejó aparte a propósito: hoy el problema es que sean tres "
  "palabras, no en qué idioma.",
  "- **Esperando autorización para el commit.** Construida, probada y "
  "documentada.\n"
  "- **El vocabulario acabó traducido**, y no quedó aparte como se había "
  "pensado: el plan lo forzaba. Escribir `Backlog` en el glosario —que es el "
  "documento que lleva la lista de lo que se queda en otro idioma **y por "
  "qué**— habría sido incumplir donde más se nota.\n"
  "- **Dos cosas quedan sin dueño, y están en el cierre §6:** que nadie "
  "reporte un campo `Estado` faltante, y que solo se comprueben las historias "
  "— épicas y planes tienen vocabulario pero no guardia."),
 (FASE + "estado-fase.md",
  "No está bloqueada. Está esperando aprobación, que es la estación 7 haciendo "
  "lo suyo.",
  "No se bloqueó en ningún momento."),

 # -- La historia --
 (HU, "| **Estado** | Backlog |", "| **Estado** | Terminada |"),
 (HU,
  "| `A-EP-003-HU-012-una-sola-palabra-por-estado` | CA-01, CA-02, CA-03, "
  "CA-04 | (vacío) | por escribir | por escribir | por escribir | Sin empezar |",
  "| [`A-EP-003-HU-012-una-sola-palabra-por-estado`]"
  "(A-EP-003-HU-012-una-sola-palabra-por-estado/) | CA-01, CA-02, CA-03, "
  "CA-04 | (vacío) | [plan_trabajo]"
  "(A-EP-003-HU-012-una-sola-palabra-por-estado/plan_trabajo.md) | "
  "[plan_pruebas](A-EP-003-HU-012-una-sola-palabra-por-estado/plan_pruebas.md) "
  "| [resultado]"
  "(A-EP-003-HU-012-una-sola-palabra-por-estado/resultado_pruebas.md) · cumple "
  "| Terminada |"),
 (HU, "- [ ] Código implementado y en rama principal",
  "- [x] Código implementado y en rama principal"),
 (HU, "- [ ] Pruebas unitarias e integración pasando",
  "- [x] Pruebas unitarias e integración pasando — 396 de 396"),
 (HU, "- [ ] Todos los criterios de aceptación verificados",
  "- [x] Todos los criterios de aceptación verificados"),
 (HU, "- [ ] Requisitos no funcionales validados",
  "- [x] Requisitos no funcionales validados"),
 (HU, "- [ ] Documentación técnica y de usuario actualizada",
  "- [x] Documentación técnica y de usuario actualizada"),
 (HU,
  "| 2026-08-26 | Agente, con el usuario | Creación de la HU. Sale de medir "
  "por qué se pudo afirmar cuatro veces que una historia cerrada estaba "
  "abierta (`S-048`) |",
  "| 2026-08-26 | Agente, con el usuario | Creación de la HU. Sale de medir "
  "por qué se pudo afirmar cuatro veces que una historia cerrada estaba "
  "abierta (`S-048`) |\n"
  "| 2026-08-26 | Agente y usuario | El alcance creció: se decidió **traducir** "
  "el vocabulario, y pasó de 51 documentos a 111 |\n"
  "| 2026-08-26 | Agente | Cerrada la fase `A`. Los cuatro criterios "
  "cumplidos; tres defectos, los tres corregidos (`S-049`, `S-050`) |"),
]

for ruta, viejo, nuevo in CAMBIOS:
    t = io.open(ruta, encoding="utf-8").read()
    assert t.count(viejo) == 1, "no coincide en %s -> %s" % (ruta[-22:], viejo[:44])
    io.open(ruta, "w", encoding="utf-8", newline="\n").write(
        t.replace(viejo, nuevo, 1))

print("HU-012 cerrada: %d cambios" % len(CAMBIOS))
