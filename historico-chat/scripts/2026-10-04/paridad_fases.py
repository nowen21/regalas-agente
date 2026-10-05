# -*- coding: utf-8 -*-
"""Compara `validadores/fases.py` y `estacion_commit.py` con sus clases nuevas
(sesión del 2026-10-04, análisis 1 del pendiente 116, fila 20), sobre este
repositorio y los proyectos dados.

    python paridad_fases.py [proyecto ...]
"""
import os
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "validadores"))
sys.path.insert(0, os.path.join(RAIZ, "proyectos", "cimiento"))

import estacion_commit as v_estacion  # noqa: E402
import fases as v_fases  # noqa: E402
from core.validadores import EstacionDelCommit, EstructuraDeFases, Veredictos  # noqa: E402
from core.validadores.epicas import Epicas  # noqa: E402


def clave(h, raiz):
    ruta = h.archivo if os.path.isabs(h.archivo) else os.path.join(raiz, h.archivo)
    return (os.path.normcase(os.path.normpath(ruta)), h.linea, h.severidad, h.mensaje)


def igual(nombre, a, b):
    print("%-30s %s" % (nombre, "IGUAL" if a == b else "DISTINTO"))
    if a != b:
        print("   viejo:", str(a)[:300])
        print("   nuevo:", str(b)[:300])
    return a == b


def en_un_proyecto(raiz):
    print("== %s" % raiz)
    nuevo = EstructuraDeFases(raiz)
    viejos = sorted(clave(h, raiz) for h in v_fases.validar(raiz))
    nuevos = sorted(clave(h, raiz) for h in nuevo.validar())
    ok = igual("validar (%d)" % len(viejos), viejos, nuevos)
    if not ok:
        for x in sorted(set(viejos) - set(nuevos))[:5]:
            print("   solo viejo:", x)
        for x in sorted(set(nuevos) - set(viejos))[:5]:
            print("   solo nuevo:", x)
    ok &= igual("inventario", v_fases.inventario(raiz), nuevo.inventario())
    ok &= igual("por_veredicto", v_fases.por_veredicto(raiz), nuevo.por_veredicto())
    ok &= igual("linea_inventario", v_fases.linea_inventario(raiz), nuevo.linea_inventario())
    distintos = []
    for epica in nuevo.arbol.epicas():
        for hu in nuevo.arbol.historias(epica):
            for fase in nuevo.arbol.fases(hu):
                if v_fases.veredicto_de(fase.ruta) != Veredictos.de_la_fase(fase.ruta):
                    distintos.append(fase.ruta)
                estado = os.path.join(fase.ruta, "estado-fase.md")
                texto = open(estado, encoding="utf-8", errors="replace").read() if os.path.isfile(estado) else ""
                if (v_estacion.marcar(texto, "abc1234") != EstacionDelCommit.marcar(texto, "abc1234")
                        or v_estacion.cierre_escrito(raiz, fase.documento("funcionalidad_implementada.md"))
                        != EstacionDelCommit.cierre_escrito(raiz, fase.documento("funcionalidad_implementada.md"))):
                    distintos.append(estado)
                rel = os.path.relpath(estado, raiz).replace("\\", "/")
                if v_estacion.fase_de(rel) != EstacionDelCommit.fase_de(rel):
                    distintos.append(rel)
    ok &= igual("veredicto, estación (%d)" % len(distintos), distintos, [])
    return ok


if __name__ == "__main__":
    todo_bien = True
    for proyecto in [RAIZ] + sys.argv[1:]:
        todo_bien &= en_un_proyecto(os.path.abspath(proyecto))
    print("\nPARIDAD COMPLETA" if todo_bien else "\nHAY DIFERENCIAS")
