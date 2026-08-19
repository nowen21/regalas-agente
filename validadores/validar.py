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

import acciones         # noqa: E402
import aislamiento      # noqa: E402
import amarre           # noqa: E402
import brevedad         # noqa: E402
import calidad          # noqa: E402
import checklist        # noqa: E402
import citas            # noqa: E402
import versiones        # noqa: E402
import ci               # noqa: E402
import commits          # noqa: E402
import cruces           # noqa: E402
import dependencias     # noqa: E402
import enlaces          # noqa: E402
import entidades        # noqa: E402
import errores          # noqa: E402
import esquema          # noqa: E402
import estructura       # noqa: E402
import fases            # noqa: E402
import pendientes       # noqa: E402
import flujo            # noqa: E402
import herramientas     # noqa: E402
import indices          # noqa: E402
import instalar         # noqa: E402
import marcas           # noqa: E402
import metareglas       # noqa: E402
import migraciones      # noqa: E402
import numeracion       # noqa: E402
import plantillas       # noqa: E402
import rama             # noqa: E402
import reaperturas      # noqa: E402
import rendimiento      # noqa: E402
import secretos         # noqa: E402
import seguridad        # noqa: E402
import trazabilidad     # noqa: E402
import version          # noqa: E402
import versionado       # noqa: E402
from comun import RAIZ, leer, preparar_salida, relativo, reportar  # noqa: E402


def raiz_del_proyecto():
    """Dónde está parado quien corre el comando, no dónde vive el estándar.

    `61` · **`RAIZ` es la carpeta del propio estándar**, y usarla por defecto en
    los subcomandos que revisan *un proyecto* hacía que revisaran el estándar
    creyendo que revisaban el proyecto. Lo reportó `rni-dp`: `validar.py
    secretos` le devolvió **10 fallas y 8 avisos** sobre archivos de
    `validadores/`, una carpeta que ese proyecto no tiene — eran las claves
    falsas que el propio detector usa para comprobar que detecta.

    **Lo grave no es el ruido: es que la comprobación decía que sí había
    corrido.** Un validador de secretos que siempre falla deja de servir para
    ver lo nuevo, y lo nuevo aquí son credenciales.

    Los subcomandos que revisan **el estándar** siguen apuntando a `RAIZ`: ahí
    sí es lo correcto.
    """
    return os.getcwd()


def cmd_estandar(a):
    hallazgos = (enlaces.validar_enlaces(a.raiz)
                 + enlaces.validar_indices(a.raiz)
                 + enlaces.validar_dias_con_resumen(a.raiz)
                 + citas.validar(a.raiz))
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
    codigo = reportar(fases.validar(raiz), f"Épica → HU → Fase · {relativo(raiz)}")
    # HU-017 · el inventario va al final, después de los hallazgos: es el
    # resumen de cuánto falta, no un incumplimiento más. Va aunque no haya
    # ninguno, que es cuando más se quiere leer.
    linea = fases.linea_inventario(raiz)
    if linea:
        print(linea)
    return codigo


def cmd_pendientes(a):
    raiz = os.path.abspath(a.raiz)
    codigo = reportar(pendientes.validar(raiz),
                      f"Numeración de pendientes · {relativo(raiz)}")
    # HU-018 · el próximo número libre va siempre, haya hallazgos o no: es la
    # pregunta que se hace quien va a abrir un pendiente, no un incumplimiento.
    linea = pendientes.linea_proximo(raiz)
    if linea:
        print(linea)
    return codigo


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

    # `22` · Y la numeración en sí: que no se haya quedado atrás de lo guardado,
    # que tenga su entrada y que no repita un número. Va acá y no aparte porque
    # es la misma pregunta —¿este cambio está versionado?— vista por el número.
    hallazgos += numeracion.validar(raiz)

    alcance = "lo que entra en el commit" if a.preparados else "todo el repositorio"
    return reportar(hallazgos, f"Qué está versionado ({alcance}) · {relativo(raiz)}")


def cmd_metareglas(a):
    """`53` · El único programa que comprueba once de las veinte filas del
    checklist del estándar no tenía por dónde correrse. Entre ellas la 5, que
    `M3` necesita, y la 15, que impide que una regla normal mande sobre una
    `[BLINDADA]`."""
    raiz = os.path.abspath(a.raiz)
    hallazgos = metareglas.validar(raiz)
    if a.catalogo:
        hallazgos += metareglas.validar_catalogo(a.catalogo, raiz)
    return reportar(hallazgos, f"El estándar contra sus meta-reglas · {relativo(raiz)}")


def cmd_acciones(a):
    """`13` · El inventario de lo que el agente puede hacer, y qué cuesta deshacerlo."""
    raiz = os.path.abspath(a.raiz)
    codigo = reportar(acciones.validar(raiz),
                      f"Acciones del agente y su riesgo · {relativo(raiz)}")
    linea = acciones.linea_resumen(raiz)
    if linea:
        print(linea)
    return codigo


def cmd_amarre(a):
    """`15` · Qué se queda y qué hay que rehacer si mañana el agente es otro."""
    raiz = os.path.abspath(a.raiz)
    codigo = reportar(amarre.validar(raiz),
                      f"El mapa del amarre a la herramienta · {relativo(raiz)}")
    linea = amarre.linea_resumen(raiz)
    if linea:
        print(linea)
    return codigo


def cmd_brevedad(a):
    """`58` · Cuánto ocupa lo que el agente contesta. **Mide, no detiene.**

    `ID9` no se puede comprobar con un programa —decidir qué palabra sobra
    exige entender qué cambia la decisión del que lee— y esto no lo intenta.
    Cuenta lo que sí se cuenta, para que «me parece que contesta largo» deje de
    ser una impresión.
    """
    raiz = os.path.abspath(a.raiz)
    codigo = reportar(brevedad.validar(raiz),
                      f"Brevedad de las respuestas · {relativo(raiz)}")
    linea = brevedad.como_texto(raiz)
    if linea:
        print(linea)
    return codigo


def cmd_indices(a):
    """`09·14` · Escribe la línea del índice que falta, en vez de solo reportarla.

    **Sin `--aplicar` solo dice qué escribiría.** Es el mismo trato que el resto
    de los reparadores: ver antes de tocar.
    """
    raiz = os.path.abspath(a.raiz)
    tocados = indices.completar(raiz, escribir=a.aplicar)
    if not tocados:
        print(f"== Índices · {relativo(raiz)} ==")
        print("OK: ningún índice tiene líneas que agregar.")
    else:
        marca = "escrito" if a.aplicar else "simulado; agrega --aplicar"
        print(f"== Índices · {relativo(raiz)} ==")
        for archivo, cuantas in tocados:
            print(f"  {relativo(archivo)}: {cuantas} línea(s) ({marca})")
    return reportar(indices.validar(raiz), None)


def cmd_reaperturas(a):
    """`09·10` · Qué fases se reabrieron. **Mide retrabajo, no culpa.**"""
    raiz = os.path.abspath(a.raiz)
    codigo = reportar(reaperturas.validar(raiz),
                      f"Fases reabiertas · {relativo(raiz)}")
    linea = reaperturas.linea_resumen(raiz)
    if linea:
        print(linea)
    return codigo


def cmd_marcas(a):
    """`11` · Las marcas de `00·ID8` en lo que se hereda.

    Solo `base/` y `plantillas/`: es lo que viaja a los proyectos. El recuento
    completo del árbol lo da `python validadores/marcas.py`.
    """
    raiz = os.path.abspath(a.raiz)
    return reportar(marcas.validar(raiz),
                    f"Marcas de generación automática · {relativo(raiz)}")


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


def cmd_estructura(a):
    """`01` · Dónde vive el código y cómo se llama — `14·EST1` y `14·EST2`.

    **Contra la convención que el proyecto declara**, no contra una inventada:
    lo que no está declarado no se comprueba, y se dice cuál se saltó.
    """
    raiz = os.path.abspath(a.raiz)
    return reportar(estructura.validar(raiz),
                    f"Ubicación y nombres del código · {relativo(raiz)}")


def cmd_entidades(a):
    """`01` · Lo que se le exige a una tabla de dominio — `03·D1`, `15·IM2`, `15·IM5`."""
    raiz = os.path.abspath(a.raiz)
    return reportar(entidades.validar(raiz),
                    f"Tablas de dominio y entidades inmutables · {relativo(raiz)}")


def cmd_cruces(a):
    """`01` · El cruce entre dos módulos se registra en los dos — `13·DOC7`."""
    raiz = os.path.abspath(a.raiz)
    return reportar(cruces.validar(raiz),
                    f"Cruces entre módulos · {relativo(raiz)}")


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

    # El desfase de número se informa, no reprueba: lo que el proyecto tiene
    # que aplicar ya lo dicen los componentes de arriba.
    for h in version.validar(raiz):
        print(f"\nAl margen: {h.mensaje}")
    return 1 if faltan else 0


def cmd_versiones(a):
    raiz = os.path.abspath(a.raiz)
    print(f"== Documentos heredados del estándar · {relativo(raiz)} ==")
    for e in versiones.estado(raiz):
        marca = "ok" if e.al_dia else "VIEJO"
        print(f"  [{marca}] {e.id} — {e.mensaje() or e.componente.destino}")

    ultima = versiones.version_registrada(raiz)
    print(f"\nÚltima actualización registrada: {ultima or '(ninguna)'}")
    for nombre, fecha, ver in versiones.registros(raiz)[-5:]:
        print(f"  {fecha}  {ver:<10} {nombre}")

    atrasados = versiones.viejos(raiz)
    cumple, detalle = versiones.revisar_registro(raiz)
    if not cumple:
        print(f"\n{detalle}")
    if atrasados:
        print("\nSe pone al día con:")
        print(f'  python "{RAIZ.replace(os.sep, "/")}/validadores/instalar.py" '
              f'"{raiz.replace(os.sep, "/")}" --aplicar')
    return 1 if (atrasados or not cumple) else 0


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
    fs.add_argument("--raiz", default=None, help="carpeta del proyecto (por defecto, donde estás parado)")
    fs.set_defaults(func=cmd_fases)

    pd = sub.add_parser("pendientes",
                        help="numeración de `pendientes/` y cruce con su índice · HU-018")
    pd.add_argument("--raiz", default=None, help="carpeta del proyecto (por defecto, donde estás parado)")
    pd.set_defaults(func=cmd_pendientes)

    tz = sub.add_parser("trazabilidad",
                        help="enlace épica↔HU, ORIGEN y tabla de cierre · F4/DOC")
    tz.add_argument("--raiz", default=None, help="carpeta del proyecto (por defecto, donde estás parado)")
    tz.set_defaults(func=cmd_trazabilidad)

    v = sub.add_parser("versionado",
                       help="secretos y artefactos versionados · 09-git.md · G3")
    v.add_argument("--raiz", default=None, help="carpeta del proyecto (por defecto, donde estás parado)")
    v.add_argument("--preparados", action="store_true",
                   help="solo lo que entra en el commit actual (para el enganche)")
    v.set_defaults(func=cmd_versionado)

    mr = sub.add_parser("metareglas",
                        help="el cuerpo de reglas contra el checklist del capítulo 20")
    mr.add_argument("--raiz", default=RAIZ, help="carpeta del estándar")
    mr.add_argument("--catalogo",
                    help="carpeta de un proyecto, para comprobar además su catálogo · M16")
    mr.set_defaults(func=cmd_metareglas)

    re_ = sub.add_parser("reaperturas",
                         help="qué fases volvieron atrás desde su cierre · retrabajo")
    re_.add_argument("--raiz", default=RAIZ, help="carpeta del estándar")
    re_.set_defaults(func=cmd_reaperturas)

    ix = sub.add_parser("indices",
                        help="escribe la línea del índice que falta · 13·DOC13")
    ix.add_argument("--raiz", default=RAIZ, help="carpeta del estándar")
    ix.add_argument("--aplicar", action="store_true",
                    help="escribe de verdad; sin esto solo simula")
    ix.set_defaults(func=cmd_indices)

    ma = sub.add_parser("marcas",
                        help="marcas de generación automática en lo que se hereda · 00·ID8")
    ma.add_argument("--raiz", default=RAIZ, help="carpeta del estándar")
    ma.set_defaults(func=cmd_marcas)

    ac = sub.add_parser("acciones",
                        help="el inventario de acciones del agente y su riesgo · 00·N1")
    ac.add_argument("--raiz", default=RAIZ, help="carpeta del estándar")
    ac.set_defaults(func=cmd_acciones)

    am = sub.add_parser("amarre",
                        help="qué piezas están atadas a la herramienta · el mapa no envejece")
    am.add_argument("--raiz", default=RAIZ, help="carpeta del estándar")
    am.set_defaults(func=cmd_amarre)

    br = sub.add_parser("brevedad",
                        help="cuánto ocupa lo que el agente contesta · 00·ID9 · mide, no detiene")
    br.add_argument("--raiz", default=RAIZ, help="carpeta del estándar")
    br.set_defaults(func=cmd_brevedad)

    es = sub.add_parser("estructura",
                        help="dónde vive el código y cómo se llama · 14·EST1 · 14·EST2")
    es.add_argument("--raiz", default=None,
                    help="carpeta del proyecto (por defecto, donde estás parado)")
    es.set_defaults(func=cmd_estructura)

    en = sub.add_parser("entidades",
                        help="tablas de dominio y entidades inmutables · 03·D1 · 15·IM2 · 15·IM5")
    en.add_argument("--raiz", default=None,
                    help="carpeta del proyecto (por defecto, donde estás parado)")
    en.set_defaults(func=cmd_entidades)

    cr = sub.add_parser("cruces",
                        help="el cruce entre dos módulos se registra en los dos · 13·DOC7")
    cr.add_argument("--raiz", default=None,
                    help="carpeta del proyecto (por defecto, donde estás parado)")
    cr.set_defaults(func=cmd_cruces)

    se = sub.add_parser("secretos",
                        help="secretos incrustados en el código · 04·S4")
    se.add_argument("--raiz", default=None, help="carpeta del proyecto (por defecto, donde estás parado)")
    se.set_defaults(func=cmd_secretos)

    dp = sub.add_parser("dependencias",
                        help="lockfile presente y versionado · 10·DEP2")
    dp.add_argument("--raiz", default=None, help="carpeta del proyecto (por defecto, donde estás parado)")
    dp.set_defaults(func=cmd_dependencias)

    rm = sub.add_parser("rama",
                        help="trabajo en rama dedicada y al día · 09·G4")
    rm.add_argument("--raiz", default=None, help="carpeta del proyecto (por defecto, donde estás parado)")
    rm.set_defaults(func=cmd_rama)

    mg = sub.add_parser("migraciones",
                        help="cada migración declara su reversión · 03·D2")
    mg.add_argument("--raiz", default=None, help="carpeta del proyecto (por defecto, donde estás parado)")
    mg.set_defaults(func=cmd_migraciones)

    er = sub.add_parser("errores", help="capturas de error vacías · 05·E1")
    er.add_argument("--raiz", default=None, help="carpeta del proyecto (por defecto, donde estás parado)")
    er.set_defaults(func=cmd_errores)

    rd = sub.add_parser("rendimiento", help="`SELECT *` y cargas sin límite · 06·R2")
    rd.add_argument("--raiz", default=None, help="carpeta del proyecto (por defecto, donde estás parado)")
    rd.set_defaults(func=cmd_rendimiento)

    es = sub.add_parser("esquema", help="FK con política de borrado · 03·D1")
    es.add_argument("--raiz", default=None, help="carpeta del proyecto (por defecto, donde estás parado)")
    es.set_defaults(func=cmd_esquema)

    fl = sub.add_parser("flujo",
                        help="el plan de trabajo: 13 preguntas e incertidumbre · 02·F14/F17")
    fl.add_argument("--raiz", default=None, help="carpeta del proyecto (por defecto, donde estás parado)")
    fl.set_defaults(func=cmd_flujo)

    sg = sub.add_parser("seguridad",
                        help="concatenación SQL/shell y asignación masiva · 04·S3")
    sg.add_argument("--raiz", default=None, help="carpeta del proyecto (por defecto, donde estás parado)")
    sg.set_defaults(func=cmd_seguridad)

    cl = sub.add_parser("calidad", help="funciones demasiado largas · 07·Q3")
    cl.add_argument("--raiz", default=None, help="carpeta del proyecto (por defecto, donde estás parado)")
    cl.set_defaults(func=cmd_calidad)

    ci_ = sub.add_parser("ci", help="pipeline de CI con pruebas y linter · 09·G6")
    ci_.add_argument("--raiz", default=None, help="carpeta del proyecto (por defecto, donde estás parado)")
    ci_.set_defaults(func=cmd_ci)

    ai = sub.add_parser("aislamiento",
                        help="pruebas contra BD efímera, no real · 08·T4")
    ai.add_argument("--raiz", default=None, help="carpeta del proyecto (por defecto, donde estás parado)")
    ai.set_defaults(func=cmd_aislamiento)

    ln = sub.add_parser("linter",
                        help="corre el linter/formateador del stack · 07·Q6")
    ln.add_argument("--raiz", default=None, help="carpeta del proyecto (por defecto, donde estás parado)")
    ln.set_defaults(func=cmd_linter)

    su = sub.add_parser("suite",
                        help="corre la suite de pruebas del stack · 08·T5")
    su.add_argument("--raiz", default=None, help="carpeta del proyecto (por defecto, donde estás parado)")
    su.set_defaults(func=cmd_suite)

    au = sub.add_parser("audit",
                        help="audit de vulnerabilidades del stack · 10·DEP3")
    au.add_argument("--raiz", default=None, help="carpeta del proyecto (por defecto, donde estás parado)")
    au.set_defaults(func=cmd_auditoria)

    vr = sub.add_parser("version",
                        help="desfase de versión del estándar vs la que declara el proyecto")
    vr.add_argument("--raiz", default=None, help="carpeta del proyecto (por defecto, donde estás parado)")
    vr.set_defaults(func=cmd_version)

    ck = sub.add_parser("checklist",
                        help="stack de instalación del agente: qué le falta al proyecto")
    ck.add_argument("--raiz", default=None, help="carpeta del proyecto (por defecto, donde estás parado)")
    ck.set_defaults(func=cmd_checklist)

    vs = sub.add_parser("versiones",
                        help="documentos heredados del estándar: cuáles quedaron viejos")
    vs.add_argument("--raiz", default=None, help="carpeta del proyecto (por defecto, donde estás parado)")
    vs.set_defaults(func=cmd_versiones)

    c = sub.add_parser("commit", help="mensaje de commit contra 09-git.md · G2")
    c.add_argument("--archivo", help="archivo con el mensaje (p. ej. COMMIT_EDITMSG)")
    c.add_argument("--revision", default="HEAD", help="commit ya hecho (por defecto HEAD)")
    c.set_defaults(func=cmd_commit)

    a = p.parse_args()
    # `61` · El que revisa **un proyecto** arranca donde está parado el usuario.
    # Antes caía en la carpeta del estándar y revisaba el estándar creyendo que
    # revisaba el proyecto — silencioso, y el resultado decía que sí había corrido.
    if getattr(a, "raiz", "") is None:
        a.raiz = raiz_del_proyecto()
    sys.exit(a.func(a))


if __name__ == "__main__":
    main()
