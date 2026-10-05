# -*- coding: utf-8 -*-
"""Compara los validadores viejos del cuerpo de reglas con sus clases nuevas
(sesión del 2026-10-04, análisis 1 del pendiente 116): metareglas, ejecutable,
vigencia, numeracion, cruces, relacionadas y mapa_tareas, sobre este
repositorio y los proyectos dados.

    python paridad_reglas.py [proyecto ...]

Cada hallazgo se compara como (ruta normalizada, línea, severidad, mensaje), y
se comparan también los valores que devuelven las funciones públicas. No
escribe nada: `mapa_tareas.escribir` lo cubren las pruebas, en carpetas temporales.
"""
import os
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "validadores"))
sys.path.insert(0, os.path.join(RAIZ, "proyectos", "cimiento"))

import comun as v_comun  # noqa: E402
import cruces as v_cruces  # noqa: E402
import ejecutable as v_ejecutable  # noqa: E402
import mapa_tareas as v_mapa  # noqa: E402
import metareglas as v_meta  # noqa: E402
import numeracion as v_numeracion  # noqa: E402
import relacionadas as v_relacionadas  # noqa: E402
import vigencia as v_vigencia  # noqa: E402
from core.comun import Proyecto  # noqa: E402
from core.herramientas.mapa_tareas import MapaDeTareas, MapaDeTareasAlDia  # noqa: E402
from core.validadores.cruces import CrucesEntreModulos  # noqa: E402
from core.validadores.ejecutable import QuienLaHaceCumplir  # noqa: E402
from core.validadores.metareglas import CatalogoDelProyecto, CuerpoDeReglas, Metareglas, Sello  # noqa: E402
from core.validadores.numeracion import Numeracion  # noqa: E402
from core.validadores.relacionadas import ReglasRelacionadas  # noqa: E402
from core.validadores.vigencia import Vigencia  # noqa: E402

PROYECTOS = ["C:/DesarrollosClaude/personales/shopnest-mesa",
             "c:/wamp64/www/proyectos/personales/agro-system"]


def ruta(r):
    return os.path.normcase(os.path.normpath(os.path.realpath(r)))


def clave(h, raiz):
    archivo = h.archivo if os.path.isabs(h.archivo) else os.path.join(raiz, h.archivo)
    return (ruta(archivo), h.linea, h.severidad, h.mensaje)


def comparar(nombre, viejos, nuevos, raiz):
    a = sorted(clave(h, raiz) for h in viejos)
    b = sorted(clave(h, raiz) for h in nuevos)
    print("%-34s %-8s viejo %5d · nuevo %5d" % (nombre, "IGUAL" if a == b else "DISTINTO", len(a), len(b)))
    if a != b:
        for x in sorted(set(a) - set(b))[:5]:
            print("   solo viejo:", x)
        for x in sorted(set(b) - set(a))[:5]:
            print("   solo nuevo:", x)
    return a == b


def igual(nombre, viejo, nuevo):
    print("%-34s %s" % (nombre, "IGUAL" if viejo == nuevo else "DISTINTO"))
    if viejo != nuevo:
        print("   viejo:", repr(viejo)[:300])
        print("   nuevo:", repr(nuevo)[:300])
    return viejo == nuevo


def foto(r):
    """Lo que se compara de una regla."""
    return (r.id, r.titulo, r.nivel, ruta(r.archivo), r.linea, r.encabezado, r.cuerpo, r.ejemplo,
            r.texto, r.capitulo, r.prefijo, r.derogada, r.blindada, r.largo())


def reglas_y_sellos(raiz):
    viejas, nuevas = v_meta.reglas(raiz), CuerpoDeReglas.leer(raiz)
    ok = igual("metareglas · reglas", [foto(r) for r in viejas], [foto(r) for r in nuevas])
    ok &= igual("metareglas · dependencias", [v_meta._dependencias(r) for r in viejas],
                [CuerpoDeReglas.dependencias(r) for r in nuevas])
    ok &= igual("metareglas · letras", v_meta._letras_registradas(raiz), CuerpoDeReglas.letras_registradas(raiz))
    ok &= igual("metareglas · clasificadas", v_meta._clasificadas(raiz), CuerpoDeReglas.clasificadas(raiz))
    ok &= igual("metareglas · es_el_estandar", v_meta.es_el_estandar(raiz), CuerpoDeReglas.es_el_estandar(raiz))
    sellos_v, sellos_n = [], []
    for v, n in zip(viejas, nuevas):
        sellos_v.append((v_meta._cambio_de_verdad(v), v_meta._tocado_el(v.archivo)))
        sellos_n.append((Sello.cambio_de_verdad(n), Sello.tocado_el(n.archivo)))
    ok &= igual("metareglas · cambio y fecha", sellos_v, sellos_n)
    return ok, viejas, nuevas


def en(raiz, estandar):
    print("\n## %s" % raiz)
    ok = comparar("metareglas", v_meta.validar(raiz), Metareglas(raiz).validar(), raiz)
    ok &= comparar("metareglas · catalogo", v_meta.validar_catalogo(raiz, RAIZ),
                   CatalogoDelProyecto(raiz).validar(), raiz)
    ok &= comparar("ejecutable", v_ejecutable.validar(raiz), QuienLaHaceCumplir(raiz).validar(), raiz)
    e = QuienLaHaceCumplir(raiz)
    ok &= igual("ejecutable · cuenta", v_ejecutable.cuenta(raiz), e.cuenta())
    ok &= igual("ejecutable · como_texto", v_ejecutable.como_texto(raiz), e.como_texto())
    ok &= igual("ejecutable · declaracion", [v_ejecutable.declaracion(r) for r in v_ejecutable._del_nucleo(raiz)],
                [e.declaracion(r) for r in e.del_nucleo()])
    ok &= comparar("vigencia", v_vigencia.validar(raiz), Vigencia(raiz).validar(), raiz)
    vg = Vigencia(raiz)
    ok &= igual("vigencia · listado", [(r.id, a, b, c) for r, a, b, c in v_vigencia.listado(raiz)],
                [(r.id, a, b, c) for r, a, b, c in vg.listado()])
    ok &= igual("vigencia · linea_resumen", v_vigencia.linea_resumen(raiz), vg.linea_resumen())
    ok &= comparar("numeracion", v_numeracion.validar(raiz), Numeracion(raiz).validar(), raiz)
    ok &= igual("numeracion · guardada", v_numeracion.guardada(raiz), Numeracion.guardada(raiz))
    ok &= comparar("cruces", v_cruces.validar(raiz), CrucesEntreModulos(raiz).validar(), raiz)
    ok &= comparar("tareas", v_mapa.validar(raiz), MapaDeTareasAlDia(raiz).validar(), raiz)
    m = MapaDeTareas(raiz)
    ok &= igual("tareas · tareas", v_mapa.tareas(raiz), m.tareas())
    ok &= igual("tareas · palabras_clave", v_mapa.palabras_clave(raiz), m.palabras_clave())
    ok &= igual("tareas · siempre", v_mapa.siempre(raiz), m.siempre())
    ok &= igual("tareas · acciones", v_mapa.acciones(raiz), m.acciones())
    ok &= igual("tareas · reglas_por_tarea", {t: [r.id for r in rs] for t, rs in v_mapa.reglas_por_tarea(raiz).items()},
                {t: [r.id for r in rs] for t, rs in m.reglas_por_tarea().items()})
    ok &= igual("tareas · sin_lista", [(r.id, t) for r, t in v_mapa.sin_lista(raiz)],
                [(r.id, t) for r, t in m.sin_lista()])
    ok &= igual("tareas · armar", v_mapa.armar(raiz), m.armar())
    ok &= igual("tareas · armar_por_tarea", v_mapa.armar_por_tarea(raiz), m.armar_por_tarea())
    ok &= igual("tareas · archivos_de", [[ruta(x) for x in v_mapa.archivos_de(t, raiz)] for t in m.tareas()],
                [[ruta(x) for x in m.archivos_de(t)] for t in m.tareas()])
    if estandar:
        o, viejas, nuevas = reglas_y_sellos(raiz)
        ok &= o
        ok &= igual("tareas · cuerpo", [v_mapa.cuerpo(r) for r in viejas], [MapaDeTareas.cuerpo(r) for r in nuevas])
        ok &= igual("tareas · declaradas", [v_mapa.declaradas(r) for r in viejas],
                    [MapaDeTareas.declaradas(r) for r in nuevas])
        ok &= relacionadas(raiz)
    return ok


def relacionadas(raiz):
    """Cada archivo de `base/`, `pendientes/`, `plantillas/` y `documentacion/epicas/`, más uno ajeno."""
    # El catálogo se lee una vez de cada lado: su paridad ya se comparó arriba,
    # y leerlo por archivo hacía tardar la corrida más de diez minutos.
    viejas, nuevas = v_meta.reglas(raiz), CuerpoDeReglas.leer(raiz)
    v_reglas, n_leer = v_meta.reglas, CuerpoDeReglas.__dict__["leer"]
    v_meta.reglas = lambda r=None: viejas
    CuerpoDeReglas.leer = classmethod(lambda cls, r=None, a=None: nuevas)
    try:
        return _relacionadas(raiz)
    finally:
        v_meta.reglas, CuerpoDeReglas.leer = v_reglas, n_leer


def _relacionadas(raiz):
    nuevo = ReglasRelacionadas(raiz)
    archivos = [os.path.join(raiz, "notas", "README.md")]
    for carpeta in ("base", "pendientes", "plantillas"):
        archivos += list(Proyecto(raiz).recorrer_md(carpeta))
    archivos += list(Proyecto(raiz).recorrer_md("documentacion/epicas"))[:40]
    distintos = 0
    for archivo in archivos:
        a = v_relacionadas.relacionadas(archivo, raiz)
        b = nuevo.de(archivo)
        if {k: v for k, v in a.items() if k != "indice"} != {k: v for k, v in b.items() if k != "indice"} \
                or sorted(a.get("indice", {})) != sorted(b.get("indice", {})) \
                or v_relacionadas.como_texto(a, raiz) != ReglasRelacionadas.como_texto(b):
            distintos += 1
            print("   distinto:", archivo)
    print("%-34s %s (%d archivos)" % ("relacionadas", "IGUAL" if not distintos else "DISTINTO en %d" % distintos,
                                      len(archivos)))
    return not distintos


def main():
    v_comun.preparar_salida()
    ok = en(RAIZ, True)
    for proyecto in sys.argv[1:] or PROYECTOS:
        if os.path.isdir(proyecto):
            ok &= en(proyecto, False)
    print("\nparidad completa" if ok else "\nHAY DIFERENCIAS")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
