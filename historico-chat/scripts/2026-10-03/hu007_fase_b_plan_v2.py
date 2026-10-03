# -*- coding: utf-8 -*-
"""Análisis 11 aprobado: el H-14 apunta a su análisis, y el plan de la fase B de la HU-007 pasa a su
versión 2 con `autorizado.py` y su prueba (acuerdo 1). La ejecución sigue desde la T-04."""
import glob
import io
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
D = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "HU-007-*", "B-EP-023-*"))[0]
RESUMEN = os.path.join(RAIZ, "historico-chat", "resumenes", "2026-10-01", "sesion.md")
A11 = "documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-11.md"


def cambiar(ruta, pares):
    t = io.open(ruta, encoding="utf-8").read()
    for a, b in pares:
        assert t.count(a) == 1, (ruta, a[:70])
        t = t.replace(a, b)
    io.open(ruta, "w", encoding="utf-8", newline="\n").write(t)


def main():
    t = io.open(RESUMEN, encoding="utf-8").read()
    i = t.index("### H-14 ·")
    j = t.index("\n---", i)
    bloque = t[i:j]
    a = "pendiente.md), en su análisis siguiente |"
    assert bloque.count(a) == 1
    bloque = bloque.replace(a, "pendiente.md), en su [análisis 11](../../../%s), aprobado el 2026-10-03; lo resuelve la fase `B` de la HU-007 |" % A11)
    io.open(RESUMEN, "w", encoding="utf-8", newline="\n").write(t[:i] + bloque + t[j:])

    cambiar(os.path.join(D, "plan_trabajo.md"), [
        ("y del punto 3 del [análisis 10](../../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-10.md) (acuerdo 6).",
         "y del punto 3 del [análisis 10](../../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-10.md) (acuerdo 6). "
         "**Versión 2**, del [análisis 11](../../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-11.md) (puntos 1 a 3): "
         "suma `autorizado.py` y su prueba, por el hallazgo H-14."),
        ("**Aprobación** (`02·F4`): Ing. José Dúmar Jiménez Ruíz, el 2026-10-03, con la versión 50.0.0.",
         "**Aprobación** (`02·F4`): Ing. José Dúmar Jiménez Ruíz, el 2026-10-03, con la versión 50.0.0. "
         "La versión 2 la aprobó con el análisis 11, que fija lo que cambia (acuerdo 1)."),
        ("| `plantillas/analisis.md` | Modificar | Plantilla | La fila que se hace «de una y sin fase» nombra sus rutas exactas |\n",
         "| `plantillas/analisis.md` | Modificar | Plantilla | La fila que se hace «de una y sin fase» nombra sus rutas exactas |\n"
         "| `validadores/autorizado.py` | Modificar | Programa | Solo la regla vigente autoriza: la derogada y la *opt-in* apagada no (versión 2) |\n"
         "| `validadores/tests/test_nada_fuera_del_plan.py` | Modificar | Pruebas | Lo autorizado se prueba con reglas de ejemplo, sin nombres ni cantidad fijos (versión 2) |\n"),
        ("| No frena lo que una regla autoriza, leído por `autorizado.py` | Una lista aparte | Cada entrada cita la regla que la autoriza | Análisis 1, acuerdo 46 |\n",
         "| No frena lo que una regla autoriza, leído por `autorizado.py` | Una lista aparte | Cada entrada cita la regla que la autoriza | Análisis 1, acuerdo 46 |\n"
         "| Solo la regla vigente autoriza: la que lleva `[DEROGADA…]` en su título y la *opt-in* de un capítulo apagado no | Leer todas las líneas | Una regla que sale deja de autorizar sin tocar el programa | Análisis 11, acuerdos 2 y 3 |\n"
         "| La prueba de lo autorizado usa reglas de ejemplo, sin nombres ni cantidad fijos | Una lista fija de reglas | Si entra o sale una regla, nada se rompe | Análisis 11, acuerdo 4 |\n"),
        ("### Cierre\n",
         "### Versión 2 · El H-14\n\n"
         "| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |\n"
         "|---|---|---|---|---|:--:|---|---|\n"
         "| T-09 | `autorizado.py` lee el estado de cada regla en ella misma y solo usa la vigente | `validadores/autorizado.py` | CA-02 | Lo usan el `pre-commit` y el freno | 0,5 h | T-03 | CP-001 |\n"
         "| T-10 | La prueba de lo autorizado comprueba con reglas de ejemplo que la vigente autoriza y la derogada o apagada no | `validadores/tests/test_nada_fuera_del_plan.py` | CA-02 | Ninguno | 0,5 h | T-09 | CP-001 |\n\n"
         "### Cierre\n"),
        ("T-01 a T-04; después T-05, T-06 y T-07; al final T-08,",
         "T-01 a T-03, T-09 y T-10, y T-04; después T-05, T-06 y T-07; al final T-08,"),
    ])
    cambiar(os.path.join(D, "estado-fase.md"), [
        ("- Detenida por el hallazgo H-14 (hallazgo al ejecutar): la T-03 hace fallar una prueba de la fase `A` que el plan no declara. Vuelve al análisis siguiente del pendiente 103.\n",
         "Ninguna. El hallazgo H-14 lo resolvió el análisis 11: el plan pasó a su versión 2 y la ejecución sigue.\n"),
        ("**Hechas:** 3 de 8 (T-01 a T-03).", "**Hechas:** 3 de 10 (T-01 a T-03)."),
    ])


if __name__ == "__main__":
    main()
