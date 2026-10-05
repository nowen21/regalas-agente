# -*- coding: utf-8 -*-
"""Compara el grupo «instalación» de `validadores/` (`instalar.py`, `checklist.py`,
`version.py`, `versiones.py`, `guardian_version.py`, `herramientas.py`,
`recuerdos.py` y `sesion.py`) con sus clases nuevas (sesión del 2026-10-04,
análisis 1 del pendiente 116), sobre este repositorio y los proyectos dados.

El instalador se compara **solo simulando** (sin `--aplicar`): nunca se escribe
en un proyecto real. Las herramientas del ecosistema no se corren (van a la red
y tocan bases de datos): se compara qué encuentran y qué orden elegirían.

    python paridad_instalacion.py [proyecto ...]
"""
import contextlib
import io
import os
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "validadores"))
sys.path.insert(0, os.path.join(RAIZ, "proyectos", "cimiento"))

import checklist as v_checklist  # noqa: E402
import guardian_version as v_guardian  # noqa: E402
import herramientas as v_herramientas  # noqa: E402
import instalar as v_instalar  # noqa: E402
import recuerdos as v_recuerdos  # noqa: E402
import sesion as v_sesion  # noqa: E402
import version as v_version  # noqa: E402
import versiones as v_versiones  # noqa: E402
from core.enganches.recuerdos import Recuerdos  # noqa: E402
from core.enganches.sesion import ArranqueDeSesion  # noqa: E402
from core.herramientas import instalar as n_instalar  # noqa: E402
from core.herramientas.instalar import Instalador, Plantillas  # noqa: E402
from core.validadores.checklist import Checklist  # noqa: E402
from core.validadores.guardian_version import VersionDelCambio  # noqa: E402
from core.validadores.herramientas import Auditoria, Linter, Suite  # noqa: E402
from core.validadores.version import VersionDelEstandar  # noqa: E402
from core.validadores.versiones import DocumentosHeredados, RegistroDeVersiones, Sello  # noqa: E402

PROYECTOS = [
    "C:/DesarrollosClaude/personales/shopnest-mesa",
    "c:/wamp64/www/proyectos/personales/agro-system",
    "C:/DesarrollosClaude/dp/proyectos/rni-back",
]


def clave(h, raiz):
    ruta = h.archivo if os.path.isabs(h.archivo) else os.path.join(raiz, h.archivo)
    return (os.path.normcase(os.path.normpath(ruta)), h.linea, h.severidad, h.mensaje)


def claves(hallazgos, raiz):
    return sorted(clave(h, raiz) for h in hallazgos)


def igual(nombre, a, b):
    print("%-44s %s" % (nombre, "IGUAL" if a == b else "DISTINTO"))
    if a != b:
        print("   viejo:", str(a)[:600])
        print("   nuevo:", str(b)[:600])
    return a == b


def salida_de(funcion, *args):
    """Lo que la función imprime, con la ruta del estándar igual en los dos."""
    texto = io.StringIO()
    with contextlib.redirect_stdout(texto):
        devuelto = funcion(*args)
    return devuelto, texto.getvalue()


def puntos(lista):
    return [(p.id, p.componente, p.arreglo, p.cumple, p.detalle, str(p)) for p in lista]


def estados(lista):
    return [(e.id, e.situacion, e.sellada, e.actual, e.al_dia, e.mensaje()) for e in lista]


def textos_generados():
    """Las plantillas que escribe el instalador, comparadas como texto."""
    print("== textos generados")
    ok = True
    estandar = RAIZ.replace("\\", "/")
    for (nv, pv, dv), (nn, pn, dn) in zip(v_instalar.HOOKS, n_instalar.HOOKS):
        a = pv.format(marca=v_instalar.MARCA, estandar=estandar, nombre=nv, descripcion=dv)
        b = pn.format(marca=n_instalar.MARCA, estandar=estandar, nombre=nn, descripcion=dn)
        ok &= igual("enganche de git %s" % nv, (nv, a), (nn, b))
    ok &= igual("cuántos enganches de git", len(v_instalar.HOOKS), len(n_instalar.HOOKS))
    ok &= igual("HOOKS_CLAUDE", v_instalar.HOOKS_CLAUDE, n_instalar.HOOKS_CLAUDE)
    ok &= igual("comandos de la herramienta",
                [v_instalar._hook_claude(estandar, "C:/p", g, m, a) for _e, _m, g, m, a in v_instalar.HOOKS_CLAUDE],
                [Instalador.hook_claude(estandar, "C:/p", g, m, a) for _e, _m, g, m, a in n_instalar.HOOKS_CLAUDE])
    for nombre in ("MARCA", "ADAPTADOR", "TEXTO_RESUMENES", "PLANTILLA_CI_GITHUB", "PLANTILLA_CI_GITLAB",
                   "CI_GITHUB", "CI_GITLAB", "_CI_DESDE", "_CI_OTROS", "CARPETAS_BASE", "CONFIG_AGENTE",
                   "IGNORADOS", "SECCIONES_DEL_PROYECTO"):
        ok &= igual(nombre, getattr(v_instalar, nombre), getattr(n_instalar, nombre))
    ok &= igual("enganches_enchufados", v_instalar.enganches_enchufados(), Instalador.enganches_enchufados())
    ok &= igual("proyectos_registrados", v_instalar.proyectos_registrados(), Instalador().proyectos_registrados())
    for texto in ("Proyecto de grado", "agro-system", "Ñandú ñoño", "", "  "):
        ok &= igual("slug %r" % texto, v_instalar._slug(texto), Plantillas.slug(texto))
    return ok


def guardian():
    print("== guardian_version")
    casos = [[], ["base/09-git.md"], ["base/09-git.md", "VERSION", "CHANGELOG.md"],
             ["base/09-git.md", "VERSION"], ["base/09-git.md", "CHANGELOG.md"],
             ["validadores/x.py", "documentacion/a.md"],
             ["base/09-git.md", "base/03-datos.md", "plantillas\\ADR.md"]]
    ok = True
    for caso in casos:
        a = [(h.severidad, h.archivo, h.linea, h.mensaje) for h in v_guardian.validar(".", preparados=caso)]
        b = [(h.severidad, h.archivo, h.linea, h.mensaje) for h in VersionDelCambio(".", preparados=caso).validar()]
        ok &= igual("guardian %s" % caso, a, b)
    a = claves(v_guardian.validar(RAIZ, "./"), RAIZ)
    b = claves(VersionDelCambio(RAIZ, ruta_mostrada="./").validar(), RAIZ)
    ok &= igual("guardian sobre lo preparado hoy", a, b)
    return ok


def herramientas(raiz):
    """Qué manifiestos se encuentran y qué orden se elegiría, sin correrla."""
    ok = True
    for repo in v_instalar.repositorios_git(raiz):
        viejos = v_herramientas.proyectos(repo)
        ok &= igual("herramientas: manifiestos (%d)" % len(viejos), viejos, Linter.proyectos(repo))
        for carpeta, stack in viejos:
            for viejo, clase in ((v_herramientas._cmd_linter, Linter), (v_herramientas._cmd_suite, Suite),
                                 (v_herramientas._cmd_audit, Auditoria)):
                ok &= igual("  %s %s" % (clase.nombre, os.path.basename(carpeta)),
                            viejo(carpeta, stack), clase(raiz).comando(carpeta, stack))
    return ok


def en_un_proyecto(raiz):
    print("\n== %s" % raiz)
    ok = True
    estandar = RAIZ

    # version y versiones
    nueva = VersionDelEstandar(raiz)
    ok &= igual("version.validar", claves(v_version.validar(raiz), raiz), claves(nueva.validar(), raiz))
    ok &= igual("version.validar_fase", claves(v_version.validar_fase(raiz), raiz), claves(nueva.validar_fase(), raiz))
    ok &= igual("version.ultima_adopcion", v_version.ultima_adopcion(raiz), VersionDelEstandar.ultima_adopcion(raiz))
    claude = os.path.join(raiz, "CLAUDE.md")
    adoptada = v_version.extraer_adoptada(open(claude, encoding="utf-8").read()) if os.path.isfile(claude) else None
    vigente = v_version.version_estandar()
    ok &= igual("version.tramo", v_version.tramo(adoptada or "1.0.0", vigente),
                nueva.tramo(adoptada or "1.0.0", vigente))
    ok &= igual("version.resumen_del_tramo", v_version._resumen_del_tramo(v_version.tramo(adoptada or "1.0.0", vigente)),
                VersionDelEstandar.resumen_del_tramo(nueva.tramo(adoptada or "1.0.0", vigente)))
    ok &= igual("versiones.estado", estados(v_versiones.estado(raiz)), estados(DocumentosHeredados(raiz).estado()))
    registro = RegistroDeVersiones(raiz)
    ok &= igual("versiones.registros", v_versiones.registros(raiz), registro.registros())
    ok &= igual("versiones.version_registrada", v_versiones.version_registrada(raiz), registro.version_registrada())
    ok &= igual("versiones.version_sellada", v_versiones.version_sellada(raiz), registro.version_sellada())
    ok &= igual("versiones.revisar_registro", v_versiones.revisar_registro(raiz), registro.revisar())
    ok &= igual("versiones.nombre_previsto", v_versiones.nombre_previsto(raiz, vigente), registro.nombre_previsto(vigente))

    # checklist
    nuevo = Checklist(raiz)
    viejos = v_checklist.revisar(raiz)
    nuevos = nuevo.revisar()
    ok &= igual("checklist.revisar (%d)" % len(viejos), puntos(viejos), puntos(nuevos))
    ok &= igual("checklist.resumen", v_checklist.resumen(raiz, viejos), Checklist.resumen(raiz, nuevos))
    ok &= igual("checklist.detalle", v_checklist.detalle(viejos), Checklist.detalle(nuevos))
    ok &= igual("checklist.huella_instalada", v_checklist.huella_instalada(raiz), Checklist.huella_instalada(raiz))

    # sesion
    arranque = ArranqueDeSesion(raiz, estandar=estandar)
    viejos = v_sesion.revisar(raiz, estandar)
    nuevos = arranque.revisar()
    ok &= igual("sesion.revisar (%d)" % len(viejos), claves(viejos, raiz), claves(nuevos, raiz))
    ok &= igual("sesion.resumen", v_sesion.resumen(raiz, viejos), ArranqueDeSesion.resumen(raiz, nuevos))
    if os.path.isdir(os.path.join(raiz, "proyectos")) or v_instalar.cumple_f13(raiz):
        ok &= igual("sesion.revisar_claude_md", claves(v_sesion.revisar_claude_md(raiz, estandar), raiz),
                    claves(arranque.revisar_claude_md(), raiz))
    ok &= igual("sesion.revisar_enganches", claves(v_sesion.revisar_enganches(raiz, estandar), raiz),
                claves(arranque.revisar_enganches(), raiz))

    # recuerdos
    memoria = Recuerdos(raiz)
    for nombre, viejo, nuevo_ in (
            ("carpeta_local", v_recuerdos.carpeta_local(raiz), memoria.carpeta_local()),
            ("indice_presente", v_recuerdos.indice_presente(raiz), memoria.indice_presente()),
            ("enlazada", v_recuerdos.enlazada(raiz), memoria.enlazada()),
            ("sueltos", v_recuerdos.sueltos(raiz), memoria.sueltos()),
            ("revisar", v_recuerdos.revisar(raiz), memoria.revisar()),
            ("contexto", v_recuerdos.contexto(raiz), memoria.contexto()),
            ("contexto con tope", v_recuerdos.contexto(raiz, tope=3000), memoria.contexto(tope=3000)),
            ("pasos de migrar (simulado)", v_recuerdos.pasos(v_recuerdos.migrar(raiz, aplicar=False)),
             Recuerdos.pasos(memoria.migrar(aplicar=False)))):
        ok &= igual("recuerdos.%s" % nombre, viejo, nuevo_)

    # herramientas
    ok &= herramientas(raiz)

    # instalador: piezas que no escriben
    instalador = Instalador()
    ok &= igual("instalar.rellenos", v_instalar._rellenos(raiz), instalador.rellenos(raiz))
    plantilla = os.path.join(estandar, "plantillas", "CLAUDE.md.plantilla")
    texto = open(plantilla, encoding="utf-8").read()
    ok &= igual("instalar.rellenar (CLAUDE.md)", v_instalar._rellenar(texto, v_instalar._rellenos(raiz), raiz),
                instalador.rellenar(texto, instalador.rellenos(raiz), raiz))
    if os.path.isfile(claude):
        local = open(claude, encoding="utf-8").read()
        copia = v_instalar.copia_sellada(raiz)
        base = open(copia, encoding="utf-8").read() if os.path.isfile(copia) else ""
        limpio = v_versiones.quitar_sello(v_instalar._rellenar(texto, v_instalar._rellenos(raiz)))
        ok &= igual("instalar.completar_secciones", v_instalar._completar_secciones(local, limpio),
                    Plantillas.completar_secciones(local, limpio))
        ok &= igual("instalar.sincronizar_secciones", v_instalar._sincronizar_secciones(local, limpio, base),
                    Plantillas.sincronizar_secciones(local, limpio, base))
        ok &= igual("versiones.quitar y poner sello", v_versiones.poner_sello(v_versiones.quitar_sello(local), "abc", "1.0.0"),
                    Sello.poner(Sello.quitar(local), "abc", "1.0.0"))
    ok &= igual("instalar.huellas", v_instalar._huellas(raiz), instalador.huellas(raiz))
    ok &= igual("instalar.huellas_previstas", v_instalar._huellas_previstas(raiz), instalador.huellas_previstas(raiz))
    ok &= igual("instalar.version_anterior", v_instalar._version_anterior(raiz), instalador.version_anterior(raiz))
    ok &= igual("instalar.pendientes", v_instalar._pendientes(raiz), instalador.pendientes(raiz))
    ok &= igual("instalar.repositorios_git", v_instalar.repositorios_git(raiz), Instalador.repositorios_git(raiz))
    ok &= igual("instalar.es_el_estandar", v_instalar.es_el_estandar(raiz), instalador.es_el_estandar(raiz))

    # instalador: la simulación completa, lo que imprime y lo que devuelve
    nombre = os.path.basename(raiz.rstrip("/\\"))
    ok &= igual("instalar (simulado)", salida_de(v_instalar.instalar, nombre, raiz, False),
                salida_de(instalador.instalar, nombre, raiz, False))
    return ok


def main_sin_ruta():
    print("\n== main sin argumentos (la lista del registro)")
    guardado = sys.argv
    sys.argv = ["instalar.py"]
    try:
        viejo = salida_de(v_instalar.main)
    finally:
        sys.argv = guardado
    return igual("main()", viejo, salida_de(n_instalar.main, []))


if __name__ == "__main__":
    todo_bien = textos_generados() & guardian() & main_sin_ruta()
    for proyecto in [RAIZ] + (sys.argv[1:] or PROYECTOS):
        todo_bien &= en_un_proyecto(proyecto)
    print("\nPARIDAD COMPLETA" if todo_bien else "\nHAY DIFERENCIAS")
