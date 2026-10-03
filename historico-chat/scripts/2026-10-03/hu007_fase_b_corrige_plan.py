# -*- coding: utf-8 -*-
"""Corrige el guion de los planes de la fase B de la HU-007 con el acuerdo 46 del análisis 1:
las reglas que mandan escribir la HU, la épica y el pendiente suman su línea «Autoriza escribir»,
y lo que un análisis aprobado manda hacer «de una y sin fase» no se frena."""
import io
import os

RUTA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hu007_fase_b_planes.py")
NL = "\\n"   # el salto de línea escrito dentro de las cadenas del guion

CAMBIOS = [
    ("| `validadores/instalar.py` | Modificar | Instalador | El enganche de antes sobre toda acción y el de después sobre la consola |\n",
     "| `validadores/instalar.py` | Modificar | Instalador | El enganche de antes sobre toda acción y el de después sobre la consola |\n"
     "| `base/13-documentacion/reglas/DOC15-crea-la-historia-de-usuario-desde-la-plantilla-central.md`, "
     "`base/13-documentacion/reglas/DOC16-crea-la-epica-desde-la-plantilla-central.md`, "
     "`base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md` | Modificar | Regla | Su línea «Autoriza escribir» y su sello |\n"
     "| `plantillas/analisis.md` | Modificar | Plantilla | La fila que se hace «de una y sin fase» nombra sus rutas exactas |\n"),
    ("ni `02·F23` traen la línea «Autoriza escribir».\n",
     "ni `02·F23` traen la línea «Autoriza escribir».\n"
     "- Los análisis 9 y 10 mandaron corregir cosas «de una y sin fase»; sus filas de «Lo que se tiene que hacer» no nombran las rutas que tocan.\n"),
    ("| No frena lo que una regla autoriza, leído por `autorizado.py` | Una lista aparte | Cada entrada cita la regla que la autoriza | Análisis 1, acuerdo 46 |\n",
     "| No frena lo que una regla autoriza, leído por `autorizado.py` | Una lista aparte | Cada entrada cita la regla que la autoriza | Análisis 1, acuerdo 46 |\n"
     "| `13·DOC15`, `13·DOC16` y `02·F23`, que mandan escribir la HU, la épica y el pendiente, suman su línea «Autoriza escribir» | Frenarlos hasta que haya una fase | Lo que una regla manda hacer no se frena, y su entrada se agrega en el mismo cambio | Análisis 1, acuerdo 46 |\n"
     "| Lo que un análisis aprobado manda hacer «de una y sin fase» no se frena: mientras ese análisis está prendido, el freno deja pasar las rutas exactas que nombra su fila, y la plantilla del análisis pide nombrarlas | Exigir una fase para todo | El usuario ya lo autorizó en el análisis; falta que un programa lo pueda leer | Propuesta del agente |\n"),
    ("1. **Lo que un análisis manda corregir «de una y sin fase».** Sin fase en curso, el acuerdo 6 del análisis 10 deja escribir solo lo que una regla autoriza. Los análisis 9 y 10 mandaron corregir cosas de una, sin fase, y esas correcciones tocaron código. Con el freno quedarían detenidas.\n"
     "2. **Las HU, las épicas y los pendientes.** Se escriben fuera de una fase y ninguna regla autoriza escribirlos. Con el freno quedarían detenidos.\n",
     "Ninguna. Las dos que había las resuelve el acuerdo 46 del análisis 1: el freno solo detiene lo que no está autorizado en ninguna parte.\n"),
    ("| T-03 | `hook_antes.py` corre",
     "| T-03 | Sumar la línea «Autoriza escribir» a `13·DOC15` (las HU), `13·DOC16` (las épicas) y `02·F23` (los pendientes), con sus sellos contra 51.0.0, y regenerar el mapa de tareas | Las tres reglas de la tabla 2.1 | CA-02 | Todo proyecto que adopte la versión | 0,5 h | Ninguna | CP-001 |\n"
     "| T-04 | La plantilla del análisis pide que la fila «de una y sin fase» nombre sus rutas exactas; `freno.py` las deja pasar mientras ese análisis está prendido | `plantillas/analisis.md`, `validadores/freno.py` | CA-02 | Los análisis nuevos | 1 h | T-01 | CP-001 |\n"
     "| T-05 | `hook_antes.py` corre"),
    ("| T-04 | `hook_despues.py`:", "| T-06 | `hook_despues.py`:"),
    ("| CA-02 | Toda orden de consola | 1 h | T-03 | CP-004 |", "| CA-02 | Toda orden de consola | 1 h | T-05 | CP-004 |"),
    ("| T-05 | El instalador pone", "| T-07 | El instalador pone"),
    ("| CA-02 | Todo proyecto, al reinstalar | 0,3 h | T-04 | CP-001 |", "| CA-02 | Todo proyecto, al reinstalar | 0,3 h | T-06 | CP-001 |"),
    ("| T-06 | Escribir los casos", "| T-08 | Escribir los casos"),
    ("| CA-02 | Todo proyecto adopta la versión | 1 h | T-01 a T-05 | CP-001 a CP-006 |", "| CA-02 | Todo proyecto adopta la versión | 1 h | T-01 a T-07 | CP-001 a CP-006 |"),
    ("T-01 y T-02; después T-03, T-04 y T-05; al final T-06,", "T-01 a T-04; después T-05, T-06 y T-07; al final T-08,"),
    ('      ("Escribir fuera del proyecto, también con `..` o `~`", "Se detiene"),',
     '      ("Sin fase en curso, escribir una HU", "Pasa: la autoriza `13·DOC15`"),\n'
     '      ("Con un análisis prendido cuya fila «de una y sin fase» nombra un archivo, escribirlo", "Pasa"),\n'
     '      ("Escribir fuera del proyecto, también con `..` o `~`", "Se detiene"),'),
    ('"☐ Escritos; esperan la aprobación y dos dudas"', '"☐ Escritos; esperan la aprobación"'),
    ('"**Hechas:** 0 de 6. **Bloqueadas:**', '"**Hechas:** 0 de 8. **Bloqueadas:**'),
    ("- Las dos dudas de la sección 2.7 del plan." + NL, ""),
    ('    escribir("plan_trabajo.md", PLAN.format(f=FASE, hu=HU_DOC, p=P103, hurel=HU_REL))\n'
     '    plan_pruebas()\n    estado()\n    fila_en_la_hu()',
     '    import sys\n'
     '    escribir("plan_trabajo.md", PLAN.format(f=FASE, hu=HU_DOC, p=P103, hurel=HU_REL))\n'
     '    plan_pruebas()\n    estado()\n'
     '    if "--sin-fila" not in sys.argv:\n        fila_en_la_hu()'),
]


def main():
    t = io.open(RUTA, encoding="utf-8").read()
    for a, b in CAMBIOS:
        assert t.count(a) == 1, a[:80]
        t = t.replace(a, b)
    io.open(RUTA, "w", encoding="utf-8", newline="\n").write(t)


if __name__ == "__main__":
    main()
