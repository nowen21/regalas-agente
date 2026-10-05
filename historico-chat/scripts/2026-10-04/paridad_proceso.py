# -*- coding: utf-8 -*-
"""Compara los módulos viejos del grupo «proceso» (`pendientes`, `acciones`,
`amarre`, `brevedad`, `redaccion`, `expediente`, `reaperturas`, `sesiones`,
`sitio`, `inmutable`, `indices`, `conteo`) con sus clases nuevas (sesión del
2026-10-04, análisis 1 del pendiente 116), sobre este repositorio y los
proyectos dados. Solo lee: nada de lo que escribe a disco se llama acá.

    python paridad_proceso.py [proyecto ...]
"""
import os
import sys
import time

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "validadores"))
sys.path.insert(0, os.path.join(RAIZ, "proyectos", "cimiento"))

import acciones as v_acciones  # noqa: E402
import amarre as v_amarre  # noqa: E402
import brevedad as v_brevedad  # noqa: E402
import comun as v_comun  # noqa: E402
import conteo as v_conteo  # noqa: E402
import enlaces as v_enlaces  # noqa: E402
import expediente as v_expediente  # noqa: E402
import indices as v_indices  # noqa: E402
import inmutable as v_inmutable  # noqa: E402
import pendientes as v_pendientes  # noqa: E402
import reaperturas as v_reaperturas  # noqa: E402
import redaccion as v_redaccion  # noqa: E402
import sesiones as v_sesiones  # noqa: E402
import sitio as v_sitio  # noqa: E402
from core.comun import FALLA, Hallazgo  # noqa: E402
from core.validadores.acciones import InventarioDeAcciones  # noqa: E402
from core.validadores.amarre import MapaDelAmarre  # noqa: E402
from core.validadores.brevedad import Brevedad, Respuestas  # noqa: E402
from core.validadores.conteo import ConteoPorRegla  # noqa: E402
from core.validadores.expediente import Expediente  # noqa: E402
from core.validadores.indices import CompletadorDeIndices, IndicesPorAfinar  # noqa: E402
from core.validadores.inmutable import HistoricoInmutable  # noqa: E402
from core.validadores.pendientes import NumeracionDePendientes, Pendientes  # noqa: E402
from core.validadores.reaperturas import Reaperturas  # noqa: E402
from core.validadores.redaccion import Redaccion  # noqa: E402
from core.validadores.sesiones import Sesiones, SesionesMezcladas  # noqa: E402
from core.validadores.sitio import MapaDelSitio  # noqa: E402


def ruta(r, raiz):
    r = r if os.path.isabs(r) else os.path.join(raiz, r)
    return os.path.normcase(os.path.realpath(r))


def clave(h, raiz):
    return (ruta(h.archivo, raiz), h.linea, h.severidad, h.mensaje)


def rutas(lista, raiz):
    return [ruta(r, raiz) for r in lista]


def igual(nombre, a, b):
    print("%-34s %s" % (nombre, "IGUAL" if a == b else "DISTINTO"))
    if a != b:
        print("   viejo:", str(a)[:400])
        print("   nuevo:", str(b)[:400])
    return a == b


def hallazgos(nombre, viejos, nuevos, raiz):
    a = sorted(clave(h, raiz) for h in viejos)
    b = sorted(clave(h, raiz) for h in nuevos)
    ok = igual("%s (%d)" % (nombre, len(a)), a, b)
    if not ok:
        for x in sorted(set(a) - set(b))[:5]:
            print("   solo viejo:", x)
        for x in sorted(set(b) - set(a))[:5]:
            print("   solo nuevo:", x)
    return ok


def de_pendientes(raiz):
    p = Pendientes(raiz)
    ok = hallazgos("pendientes.validar", v_pendientes.validar(raiz), NumeracionDePendientes(raiz).validar(), raiz)
    ok &= igual("pendientes.numerados", v_pendientes.numerados(raiz), p.numerados())
    ok &= igual("pendientes.numeros_del_indice", v_pendientes.numeros_del_indice(raiz), p.numeros_del_indice())
    ok &= igual("pendientes.tomados", v_pendientes.tomados(raiz), p.tomados())
    ok &= igual("pendientes.sin_numero", v_pendientes.sin_numero(raiz), p.sin_numero())
    ok &= igual("pendientes.linea_proximo", v_pendientes.linea_proximo(raiz), p.linea_proximo())
    ok &= igual("pendientes.sin_proyecto_de_origen", v_pendientes.sin_proyecto_de_origen(raiz),
                p.sin_proyecto_de_origen())
    ok &= hallazgos("pendientes.cerrado_declara_su_fase", v_pendientes.cerrado_declara_su_fase(raiz),
                    p.cerrado_declara_su_fase(), raiz)
    ok &= hallazgos("pendientes.forma_nueva", v_pendientes.forma_nueva(raiz), p.forma_nueva(), raiz)
    carpetas = v_pendientes.carpetas(raiz)
    ok &= igual("pendientes.carpetas (%d)" % len(carpetas), rutas(carpetas, raiz), rutas(p.carpetas(), raiz))
    ok &= igual("pendientes.numeros_nuevos", {n: rutas(c, raiz) for n, c in v_pendientes.numeros_nuevos(raiz).items()},
                {n: rutas(c, raiz) for n, c in p.numeros_nuevos().items()})
    distintos = []
    for c in carpetas:
        if (v_pendientes.estado(c, raiz) != p.estado(c)
                or bool(v_pendientes.padre(c)) != bool(p.padre(c))
                or (v_pendientes.padre(c) and ruta(v_pendientes.padre(c), raiz) != ruta(p.padre(c), raiz))
                or v_pendientes.resuelto_en(c) != p.resuelto_en(c)
                or v_pendientes.analisis_de(c) != p.analisis_de(c)):
            distintos.append(c)
    ok &= igual("pendientes.estado/padre/resuelto", distintos, [])
    ok &= igual("pendientes.indice", v_pendientes.indice(raiz), p.indice())
    return ok


def de_mapas(raiz):
    a, m, s = InventarioDeAcciones(raiz), MapaDelAmarre(raiz), MapaDelSitio(raiz)
    ok = hallazgos("acciones.validar", v_acciones.validar(raiz), a.validar(), raiz)
    ok &= igual("acciones.clases", v_acciones.clases(raiz), a.clases())
    ok &= igual("acciones.linea_resumen", v_acciones.linea_resumen(raiz), a.linea_resumen())
    ok &= hallazgos("amarre.validar", v_amarre.validar(raiz), m.validar(), raiz)
    ok &= igual("amarre.piezas", v_amarre.piezas(raiz), m.piezas())
    ok &= igual("amarre.linea_resumen", v_amarre.linea_resumen(raiz), m.linea_resumen())
    ok &= hallazgos("sitio.validar", v_sitio.validar(raiz), s.validar(), raiz)
    ok &= igual("sitio.carpetas", v_sitio.carpetas(raiz), s.carpetas())
    ok &= igual("sitio.linea_resumen", v_sitio.linea_resumen(raiz), s.linea_resumen())
    return ok


def de_brevedad(raiz):
    b = Brevedad(raiz)
    ok = hallazgos("brevedad.validar", v_brevedad.validar(raiz), b.validar(), raiz)
    ok &= igual("brevedad.transcripciones", rutas(v_brevedad.transcripciones(raiz), raiz),
                rutas(b.transcripciones(), raiz))
    ok &= igual("brevedad.como_texto", v_brevedad.como_texto(raiz), b.como_texto())
    distintos, textos = [], []
    for t in b.transcripciones():
        if v_brevedad.resumen(t) != Respuestas.resumen(t) or v_brevedad.respuestas(t) != Respuestas.de(t):
            distintos.append(t)
        textos.append(v_comun.leer(t))
    ok &= igual("brevedad.resumen (%d)" % len(textos), distintos, [])
    # La redacción, sobre cada transcripción y cada documento de `base/`.
    base = os.path.join(raiz, "base")
    if os.path.isdir(base):
        textos += [v_comun.leer(r) for r in v_comun.recorrer_md(base)]
    distintos = [i for i, t in enumerate(textos)
                 if (v_redaccion.tratos(t), v_redaccion.medir(t), v_redaccion.linea_de_cierre(t, 900))
                 != (Redaccion.tratos(t), Redaccion.medir(t), Redaccion.linea_de_cierre(t, 900))]
    ok &= igual("redaccion (%d textos)" % len(textos), distintos, [])
    return ok


def de_expediente(raiz):
    lv, hv = v_expediente.reporte(raiz)
    ln, hn = Expediente(raiz).reporte()
    ok = igual("expediente.reporte (lineas)", lv, ln)
    return ok & hallazgos("expediente.reporte (hallazgos)", hv, hn, raiz)


def de_git(raiz):
    r = Reaperturas(raiz)
    viejas = v_reaperturas.reaperturas(raiz)
    nuevas = r.reaperturas()
    ok = igual("reaperturas.reaperturas (%d)" % len(viejas), [(ruta(p, raiz), v) for p, v in viejas],
               [(ruta(p, raiz), v) for p, v in nuevas])
    # Recorrer la historia de cada fase tarda minutos en este repositorio: ya
    # comparada, la lista se reusa para comparar lo que se arma con ella.
    original = v_reaperturas.reaperturas
    r.reaperturas = lambda: nuevas
    v_reaperturas.reaperturas = lambda _raiz=None: viejas
    try:
        ok &= hallazgos("reaperturas.validar", v_reaperturas.validar(raiz), r.validar(), raiz)
        ok &= igual("reaperturas.linea_resumen", v_reaperturas.linea_resumen(raiz), r.linea_resumen())
    finally:
        v_reaperturas.reaperturas = original
    ahora = time.time()
    s, sm = Sesiones(raiz), SesionesMezcladas(raiz, ahora=ahora)
    ok &= igual("sesiones.registros", v_sesiones.registros(raiz, ahora), s.registros(ahora))
    ok &= igual("sesiones.preparados", v_sesiones.preparados(raiz), sm.preparados())
    ok &= hallazgos("sesiones.validar_preparados", v_sesiones.validar_preparados(raiz, ahora), sm.validar(), raiz)
    ok &= igual("sesiones.cambios_del_turno", sorted(v_sesiones.cambios_del_turno(raiz, ahora - 86400)),
                sorted(s.cambios_del_turno(ahora - 86400)))
    ok &= igual("sesiones.estado_de_git", v_sesiones._estado_de_git(raiz), s.estado_de_git())
    i = HistoricoInmutable(raiz)
    ok &= igual("inmutable.modificadas", v_inmutable.modificadas(raiz), i.modificadas())
    ok &= hallazgos("inmutable.validar", v_inmutable.validar(raiz), i.validar(), raiz)
    casos = [("a\nb\n", "a\nb\nc\n"), ("a\nb\n", "a\nX\n"), ("a\nb\n", "a\r\nb\r\nc\r\n"), ("", "")]
    ok &= igual("inmutable.solo_crecio", [v_inmutable.solo_crecio(*c) for c in casos],
                [HistoricoInmutable.solo_crecio(*c) for c in casos])
    return ok


def de_indices_y_conteo(raiz):
    c = CompletadorDeIndices(raiz)
    ok = hallazgos("indices.validar", v_indices.validar(raiz), IndicesPorAfinar(raiz).validar(), raiz)
    ok &= igual("indices.completar (simulado)", [(ruta(i, raiz), n) for i, n in v_indices.completar(raiz)],
                [(ruta(i, raiz), n) for i, n in c.completar()])
    for rel in v_enlaces.CON_INDICE:
        carpeta = os.path.join(raiz, rel)
        ok &= igual("indices.faltantes %s" % rel, v_indices.faltantes(carpeta), c.faltantes(carpeta))
        if os.path.isdir(carpeta):
            md = [os.path.join(carpeta, n) for n in sorted(os.listdir(carpeta)) if n.endswith(".md")]
            ok &= igual("indices.titulo_de %s (%d)" % (rel, len(md)), [v_indices.titulo_de(m) for m in md],
                        [c.titulo_de(m) for m in md])
    k = ConteoPorRegla(raiz)
    ok &= igual("conteo.version", v_conteo.version_del(raiz), k.version())
    ok &= igual("conteo.corridas", v_conteo.corridas(raiz), k.corridas())
    ok &= igual("conteo.comparar", v_conteo.comparar(raiz), k.comparar())
    muestra = v_pendientes.validar(raiz) + v_sitio.validar(raiz) + v_acciones.validar(raiz)
    nueva = [Hallazgo(h.severidad, h.archivo, h.linea, h.mensaje) for h in muestra]
    muestra += [v_comun.Hallazgo(FALLA, "x", 0, "de `%02d·M%d`" % (n % 7, n)) for n in range(14)]
    nueva += [Hallazgo(FALLA, "x", 0, "de `%02d·M%d`" % (n % 7, n)) for n in range(14)]
    ok &= igual("conteo.lineas_del_conteo", v_conteo.lineas_del_conteo(muestra, raiz), k.lineas(nueva))
    return ok


def en_un_proyecto(raiz):
    print("== %s" % raiz)
    ok = True
    for parte in (de_pendientes, de_mapas, de_brevedad, de_expediente, de_git, de_indices_y_conteo):
        ok &= parte(raiz)
    return ok


PROYECTOS = ["C:/DesarrollosClaude/personales/shopnest-mesa", "c:/wamp64/www/proyectos/personales/agro-system"]

if __name__ == "__main__":
    todo_bien = True
    for proyecto in [RAIZ] + (sys.argv[1:] or PROYECTOS):
        todo_bien &= en_un_proyecto(os.path.abspath(proyecto))
    print("\nPARIDAD COMPLETA" if todo_bien else "\nHAY DIFERENCIAS")
