# -*- coding: utf-8 -*-
"""Compara los validadores viejos de documentos con sus clases nuevas
(sesión del 2026-10-04, análisis 1 del pendiente 116, fila 19): trazabilidad,
plantilla, citas y marcas, sobre este repositorio y los proyectos dados.

    python paridad_documentos.py [proyecto ...]

Cada hallazgo se compara como (ruta normalizada, línea, severidad, mensaje).
"""
import os
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "validadores"))
sys.path.insert(0, os.path.join(RAIZ, "proyectos", "cimiento"))

import citas as v_citas  # noqa: E402
import marcas as v_marcas  # noqa: E402
import plantillas as v_plantillas  # noqa: E402
import trazabilidad as v_trazabilidad  # noqa: E402
from core.comun import Proyecto  # noqa: E402
from core.validadores import (CitasEnlazadas, DocumentoContraPlantilla, EnlazadorDeCitas,  # noqa: E402
                              Marcas, MarcasDeGeneracion, TrazabilidadDeFases)
from core.validadores.citas import IndiceDeReglas  # noqa: E402


def clave(h, raiz):
    ruta = h.archivo if os.path.isabs(h.archivo) else os.path.join(raiz, h.archivo)
    return (os.path.normcase(os.path.normpath(ruta)), h.linea, h.severidad, h.mensaje)


def comparar(nombre, viejos, nuevos, raiz):
    a = sorted(clave(h, raiz) for h in viejos)
    b = sorted(clave(h, raiz) for h in nuevos)
    estado = "IGUAL" if a == b else "DISTINTO"
    print("%-26s %-8s viejo %5d · nuevo %5d" % (nombre, estado, len(a), len(b)))
    if a != b:
        for x in sorted(set(a) - set(b))[:5]:
            print("   solo viejo:", x)
        for x in sorted(set(b) - set(a))[:5]:
            print("   solo nuevo:", x)
    return a == b


def en_el_estandar():
    ok = comparar("citas", v_citas.validar(RAIZ), CitasEnlazadas(RAIZ).validar(), RAIZ)
    viejo_idx = v_citas.indice(RAIZ)
    nuevo = EnlazadorDeCitas(RAIZ)
    ok &= viejo_idx == nuevo.indice.reglas
    print("%-26s %s" % ("citas · índice", "IGUAL" if viejo_idx == nuevo.indice.reglas else "DISTINTO"))
    distintos = 0
    for archivo in Proyecto(RAIZ).recorrer_md("base"):
        texto = open(archivo, encoding="utf-8").read()
        if (v_citas.enlazar(texto, archivo, viejo_idx) != nuevo.enlazar(texto, archivo)
                or v_citas.reparar(texto, archivo, viejo_idx) != nuevo.reparar(texto, archivo)):
            distintos += 1
    print("%-26s %s" % ("citas · enlazar/reparar", "IGUAL" if not distintos else "DISTINTO en %d" % distintos))

    m = MarcasDeGeneracion(RAIZ)
    ok &= comparar("marcas · heredadas", v_marcas.validar(RAIZ), m.validar(), RAIZ)
    print("%-26s %s" % ("marcas · alcance", "IGUAL" if v_marcas.alcance(RAIZ, v_marcas.MIRADOS) == m.alcance()
                        else "DISTINTO"))
    for historico in (False, True):
        igual = v_marcas.contar(RAIZ, historico) == m.contar(historico)
        print("%-26s %s" % ("marcas · contar %s" % historico, "IGUAL" if igual else "DISTINTO"))
        ok &= igual
    igual = v_marcas.limpiar(RAIZ) == m.limpiar()
    print("%-26s %s" % ("marcas · limpiar", "IGUAL" if igual else "DISTINTO"))
    distintos = 0
    for archivo in Proyecto(RAIZ).recorrer_md():
        texto = open(archivo, encoding="utf-8", errors="replace").read()
        if (v_marcas.medir_texto(texto) != Marcas.medir(texto)
                or v_marcas.limpiar_texto(texto) != Marcas.limpiar(texto)):
            distintos += 1
    print("%-26s %s" % ("marcas · medir/limpiar", "IGUAL" if not distintos else "DISTINTO en %d" % distintos))
    ok &= comparar("marcas · preparados", v_marcas.validar_preparados(RAIZ),
                   MarcasDeGeneracion(RAIZ, solo_preparados=True).validar(), RAIZ)
    return ok and not distintos


def en_un_proyecto(raiz):
    print("== %s" % raiz)
    ok = True
    if os.path.isdir(os.path.join(raiz, "documentacion", "epicas")):
        ok &= comparar("trazabilidad", v_trazabilidad.validar(raiz), TrazabilidadDeFases(raiz).validar(), raiz)
    viejos, nuevos, sin_molde = [], [], 0
    for archivo in Proyecto(raiz).recorrer_md():
        texto = open(archivo, encoding="utf-8", errors="replace").read()
        molde_viejo = v_plantillas.deducir_plantilla(archivo, texto)
        if molde_viejo != DocumentoContraPlantilla.deducir(archivo, texto):
            print("   molde distinto:", archivo)
            ok = False
        if not molde_viejo or not os.path.isfile(molde_viejo):
            sin_molde += 1
            continue
        viejos += v_plantillas.validar(archivo, molde_viejo)
        nuevos += DocumentoContraPlantilla(raiz, archivo, molde_viejo).validar()
    ok &= comparar("plantilla", viejos, nuevos, raiz)
    return ok


if __name__ == "__main__":
    todo_bien = en_el_estandar()
    for proyecto in [RAIZ] + sys.argv[1:]:
        todo_bien &= en_un_proyecto(os.path.abspath(proyecto))
    print("\nPARIDAD COMPLETA" if todo_bien else "\nHAY DIFERENCIAS")
