#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validadores del estándar — punto de entrada único.

Uso:
  python validadores/validar.py estandar
  python validadores/validar.py plantilla <documento.md> [--contra <plantilla.md>]
  python validadores/validar.py commit [--archivo <ruta> | --revision HEAD]

Código de salida: 0 si no hay FALLA, 1 si hay al menos una.
Los AVISO no rompen la ejecución: señalan lo que un humano debe mirar.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import aislamiento      # noqa: E402
import calidad          # noqa: E402
import checklist        # noqa: E402
import ci               # noqa: E402
import commits          # noqa: E402
import dependencias     # noqa: E402
import enlaces          # noqa: E402
import errores          # noqa: E402
import esquema          # noqa: E402
import fases            # noqa: E402
import flujo            # noqa: E402
import herramientas     # noqa: E402
import instalar         # noqa: E402
import migraciones      # noqa: E402
import plantillas       # noqa: E402
import rama             # noqa: E402
import rendimiento      # noqa: E402
import secretos         # noqa: E402
import seguridad        # noqa: E402
import trazabilidad     # noqa: E402
import version          # noqa: E402
import versionado       # noqa: E402
from comun import RAIZ, leer, preparar_salida, relativo, reportar  # noqa: E402


def cmd_estandar(a):
    hallazgos = enlaces.validar_enlaces(a.raiz) + enlaces.validar_indices(a.raiz)
    return reportar(hallazgos, "Coherencia del estándar")


def cmd_plantilla(a):
    if not os.path.isfile(a.documento):
        sys.exit(f"no existe el documento: {a.documento}")

    texto = leer(a.documento)
    ruta_plantilla = a.contra or plantillas.deducir_plantilla(a.documento, texto)

    if not ruta_plantilla:
        sys.exit(
            f"no se pudo deducir la plantilla de {relativo(a.documento)}.\n"
            f"Indícala con --contra plantillas/<archivo>.md")
    if not os.path.isfile(ruta_plantilla):
        sys.exit(f"no existe la plantilla: {ruta_plantilla}")

    hallazgos = plantillas.validar(a.documento, ruta_plantilla)
    return reportar(
        hallazgos,
        f"{relativo(a.documento)} contra {relativo(ruta_plantilla)}")


def cmd_fases(a):
    raiz = os.path.abspath(a.raiz)
    return reportar(fases.validar(raiz), f"Épica → HU → Fase · {relativo(raiz)}")


def cmd_trazabilidad(a):
    raiz = os.path.abspath(a.raiz)
    return reportar(trazabilidad.validar(raiz),
                    f"Trazabilidad épica↔HU · plan · cierre · {relativo(raiz)}")


def cmd_versionado(a):
    raiz = os.path.abspath(a.raiz)
    repos = instalar.repositorios_git(raiz)
    if not repos:
        sys.exit(f"no hay repositorios git en {relativo(raiz)}")

    hallazgos = []
    for repo in repos:
        etiqueta = os.path.relpath(repo, raiz).replace("\\", "/")
        hallazgos += versionado.validar(
            repo, repo if etiqueta == "." else f"{etiqueta}/",
            solo_preparados=a.preparados)

    alcance = "lo que entra en el commit" if a.preparados else "todo el repositorio"
    return reportar(hallazgos, f"Qué está versionado ({alcance}) · {relativo(raiz)}")


def cmd_secretos(a):
    raiz = os.path.abspath(a.raiz)
    return reportar(secretos.validar(raiz), f"Secretos en el código · {relativo(raiz)}")


def cmd_dependencias(a):
    raiz = os.path.abspath(a.raiz)
    return reportar(dependencias.validar(raiz),
                    f"Lockfile versionado · {relativo(raiz)}")


def cmd_rama(a):
    raiz = os.path.abspath(a.raiz)
    return reportar(rama.validar(raiz), f"Rama de trabajo · {relativo(raiz)}")


def cmd_migraciones(a):
    raiz = os.path.abspath(a.raiz)
    return reportar(migraciones.validar(raiz),
                    f"Migraciones reversibles · {relativo(raiz)}")


def cmd_errores(a):
    raiz = os.path.abspath(a.raiz)
    return reportar(errores.validar(raiz), f"Errores tragados · {relativo(raiz)}")


def cmd_rendimiento(a):
    raiz = os.path.abspath(a.raiz)
    return reportar(rendimiento.validar(raiz),
                    f"Cargas sin límite · {relativo(raiz)}")


def cmd_esquema(a):
    raiz = os.path.abspath(a.raiz)
    return reportar(esquema.validar(raiz), f"Integridad de esquema · {relativo(raiz)}")


def cmd_flujo(a):
    raiz = os.path.abspath(a.raiz)
    return reportar(flujo.validar(raiz), f"Plan de trabajo · {relativo(raiz)}")


def cmd_ci(a):
    raiz = os.path.abspath(a.raiz)
    return reportar(ci.validar(raiz), f"Integración continua · {relativo(raiz)}")


def cmd_seguridad(a):
    raiz = os.path.abspath(a.raiz)
    return reportar(seguridad.validar(raiz),
                    f"Concatenación e inyección · {relativo(raiz)}")


def cmd_calidad(a):
    raiz = os.path.abspath(a.raiz)
    return reportar(calidad.validar(raiz), f"Funciones largas · {relativo(raiz)}")


def cmd_aislamiento(a):
    raiz = os.path.abspath(a.raiz)
    return reportar(aislamiento.validar(raiz),
                    f"Pruebas aisladas · {relativo(raiz)}")


def cmd_linter(a):
    raiz = os.path.abspath(a.raiz)
    return reportar(herramientas.linter(raiz), f"Linter/formateador · {relativo(raiz)}")


def cmd_suite(a):
    raiz = os.path.abspath(a.raiz)
    return reportar(herramientas.suite(raiz), f"Suite de pruebas · {relativo(raiz)}")


def cmd_auditoria(a):
    raiz = os.path.abspath(a.raiz)
    return reportar(herramientas.auditoria(raiz),
                    f"Audit de vulnerabilidades · {relativo(raiz)}")


def cmd_version(a):
    raiz = os.path.abspath(a.raiz)
    return reportar(version.validar(raiz), f"Versión del estándar · {relativo(raiz)}")


def cmd_checklist(a):
    raiz = os.path.abspath(a.raiz)
    puntos = checklist.revisar(raiz)
    if not puntos:
        sys.exit("no se pudo leer plantillas/stack-instalacion.md")

    print(f"== Instalación del agente · {relativo(raiz)} ==")
    for p in puntos:
        print(f"  {p}")

    faltan = checklist.pendientes(puntos)
    print(f"\n{checklist.resumen(raiz, puntos)}")
    if faltan:
        print(f"\n{checklist.detalle(puntos)}")
    return 1 if faltan else 0


def cmd_commit(a):
    if a.archivo:
        mensaje, origen = leer(a.archivo), a.archivo
    else:
        mensaje, origen = commits.leer_de_git(a.revision), f"commit {a.revision}"
    return reportar(commits.validar(mensaje, origen), f"Mensaje de {origen}")


def main():
    preparar_salida()

    p = argparse.ArgumentParser(
        description="Comprueba lo que del estándar se puede comprobar sin criterio.")
    sub = p.add_subparsers(dest="comando", required=True)

    e = sub.add_parser("estandar", help="enlaces rotos e índices desactualizados")
    e.add_argument("--raiz", default=RAIZ)
    e.set_defaults(func=cmd_estandar)

    pl = sub.add_parser("plantilla", help="un documento contra su plantilla")
    pl.add_argument("documento")
    pl.add_argument("--contra", help="ruta de la plantilla (si no se deduce sola)")
    pl.set_defaults(func=cmd_plantilla)

    fs = sub.add_parser("fases",
                        help="jerarquía y nombres de épica/HU/fase · 02·F12")
    fs.add_argument("--raiz", default=RAIZ, help="carpeta del proyecto")
    fs.set_defaults(func=cmd_fases)

    tz = sub.add_parser("trazabilidad",
                        help="enlace épica↔HU, ORIGEN y tabla de cierre · F4/DOC")
    tz.add_argument("--raiz", default=RAIZ, help="carpeta del proyecto")
    tz.set_defaults(func=cmd_trazabilidad)

    v = sub.add_parser("versionado",
                       help="secretos y artefactos versionados · 09-git.md · G3")
    v.add_argument("--raiz", default=RAIZ, help="carpeta del proyecto")
    v.add_argument("--preparados", action="store_true",
                   help="solo lo que entra en el commit actual (para el enganche)")
    v.set_defaults(func=cmd_versionado)

    se = sub.add_parser("secretos",
                        help="secretos incrustados en el código · 04·S4")
    se.add_argument("--raiz", default=RAIZ, help="carpeta del proyecto")
    se.set_defaults(func=cmd_secretos)

    dp = sub.add_parser("dependencias",
                        help="lockfile presente y versionado · 10·DEP2")
    dp.add_argument("--raiz", default=RAIZ, help="carpeta del proyecto")
    dp.set_defaults(func=cmd_dependencias)

    rm = sub.add_parser("rama",
                        help="trabajo en rama dedicada y al día · 09·G4")
    rm.add_argument("--raiz", default=RAIZ, help="carpeta del proyecto")
    rm.set_defaults(func=cmd_rama)

    mg = sub.add_parser("migraciones",
                        help="cada migración declara su reversión · 03·D2")
    mg.add_argument("--raiz", default=RAIZ, help="carpeta del proyecto")
    mg.set_defaults(func=cmd_migraciones)

    er = sub.add_parser("errores", help="capturas de error vacías · 05·E1")
    er.add_argument("--raiz", default=RAIZ, help="carpeta del proyecto")
    er.set_defaults(func=cmd_errores)

    rd = sub.add_parser("rendimiento", help="`SELECT *` y cargas sin límite · 06·R2")
    rd.add_argument("--raiz", default=RAIZ, help="carpeta del proyecto")
    rd.set_defaults(func=cmd_rendimiento)

    es = sub.add_parser("esquema", help="FK con política de borrado · 03·D1")
    es.add_argument("--raiz", default=RAIZ, help="carpeta del proyecto")
    es.set_defaults(func=cmd_esquema)

    fl = sub.add_parser("flujo",
                        help="el plan de trabajo: 13 preguntas e incertidumbre · 02·F4.1/F4.3")
    fl.add_argument("--raiz", default=RAIZ, help="carpeta del proyecto")
    fl.set_defaults(func=cmd_flujo)

    sg = sub.add_parser("seguridad",
                        help="concatenación SQL/shell y asignación masiva · 04·S3")
    sg.add_argument("--raiz", default=RAIZ, help="carpeta del proyecto")
    sg.set_defaults(func=cmd_seguridad)

    cl = sub.add_parser("calidad", help="funciones demasiado largas · 07·Q3")
    cl.add_argument("--raiz", default=RAIZ, help="carpeta del proyecto")
    cl.set_defaults(func=cmd_calidad)

    ci_ = sub.add_parser("ci", help="pipeline de CI con pruebas y linter · 09·G6")
    ci_.add_argument("--raiz", default=RAIZ, help="carpeta del proyecto")
    ci_.set_defaults(func=cmd_ci)

    ai = sub.add_parser("aislamiento",
                        help="pruebas contra BD efímera, no real · 08·T4")
    ai.add_argument("--raiz", default=RAIZ, help="carpeta del proyecto")
    ai.set_defaults(func=cmd_aislamiento)

    ln = sub.add_parser("linter",
                        help="corre el linter/formateador del stack · 07·Q6")
    ln.add_argument("--raiz", default=RAIZ, help="carpeta del proyecto")
    ln.set_defaults(func=cmd_linter)

    su = sub.add_parser("suite",
                        help="corre la suite de pruebas del stack · 08·T5")
    su.add_argument("--raiz", default=RAIZ, help="carpeta del proyecto")
    su.set_defaults(func=cmd_suite)

    au = sub.add_parser("audit",
                        help="audit de vulnerabilidades del stack · 10·DEP3")
    au.add_argument("--raiz", default=RAIZ, help="carpeta del proyecto")
    au.set_defaults(func=cmd_auditoria)

    vr = sub.add_parser("version",
                        help="desfase de versión del estándar vs la que declara el proyecto")
    vr.add_argument("--raiz", default=RAIZ, help="carpeta del proyecto")
    vr.set_defaults(func=cmd_version)

    ck = sub.add_parser("checklist",
                        help="stack de instalación del agente: qué le falta al proyecto")
    ck.add_argument("--raiz", default=RAIZ, help="carpeta del proyecto")
    ck.set_defaults(func=cmd_checklist)

    c = sub.add_parser("commit", help="mensaje de commit contra 09-git.md · G2")
    c.add_argument("--archivo", help="archivo con el mensaje (p. ej. COMMIT_EDITMSG)")
    c.add_argument("--revision", default="HEAD", help="commit ya hecho (por defecto HEAD)")
    c.set_defaults(func=cmd_commit)

    a = p.parse_args()
    sys.exit(a.func(a))


if __name__ == "__main__":
    main()
