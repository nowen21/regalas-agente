# -*- coding: utf-8 -*-
"""`EP-004 · HU-013` · Lo hecho contra el plan aprobado.

**Qué compara.** Un plan de trabajo declara en su §2.1 qué archivos va a tocar,
y [`02·F8`](../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)
exige que se toquen **esos**. Un plan de pruebas declara sus casos y la fase sus
criterios, y cada criterio tiene que tener quien lo compruebe. Las dos cosas se
comprobaban leyendo, o sea casi nunca.

**Contra qué se comparan los archivos tocados: contra el commit del que salió la
fase.** Es la decisión 22 del [pendiente 59](../pendientes/59-las-42-dudas-que-detienen-26-fases.md).
La rama arrastra trabajo ajeno y lo sin guardar cambia mientras se mira; el
commit de origen es el único punto fijo.

**Avisa, nunca detiene.** Un archivo de más puede ser un descubrimiento legítimo
que se reportó y se aprobó, y eso no se ve desde el disco. Lo que el programa
puede decir es **que la lista no cuadra**; si cuadra o no la explicación, lo lee
una persona.

**Lo que no compara, y se declara:** si los pasos que el resultado dice haber
ejecutado son los que el plan de pruebas escribió. Eso exige leer los dos textos
y entender si dicen lo mismo con otras palabras; queda como criterio humano
(decisión 10 del pendiente 59), y así está registrado en `reglas-validables.md`.
"""
import os
import re
import subprocess

import autorizado
import comun
from comun import AVISO, FALLA, Hallazgo, relativo

# La tabla de archivos del plan: su §2.1. Se buscan rutas entre comillas
# invertidas, que es como el molde las escribe.
_SECCION_ARCHIVOS = re.compile(
    r"(?ms)^###\s*2\.1[^\n]*\n(.*?)(?=^###\s|\Z)")
_RUTA = re.compile(r"`([\w][\w./\\-]*\.[\w]{1,5}|[\w][\w./\\-]*/)`")

# Los casos del plan de pruebas y los criterios que la fase declara cubrir.
_CASO = re.compile(r"(?m)^###?\s*(CP-\d+)")
_CRITERIO_EN_PLAN = re.compile(r"\b(CA-\d+)\b")

# Lo que nunca cuenta como «archivo tocado de más»: los documentos de la propia
# fase. Escribir el resultado de las pruebas **es** ejecutar la fase, y pedir
# que el plan se declare a sí mismo sería ruido en todas las fases.
DE_LA_FASE = ("plan_trabajo.md", "plan_pruebas.md", "resultado_pruebas.md",
              "estado-fase.md", "funcionalidad_implementada.md", "README.md")


def _git(repo, *args):
    try:
        r = subprocess.run(["git", "-C", repo] + list(args), capture_output=True,
                           text=True, encoding="utf-8", errors="replace", timeout=60)
    except (OSError, subprocess.SubprocessError):
        return ""
    return r.stdout if r.returncode == 0 else ""


def declarados(plan_texto):
    """Las rutas que el plan declara en su §2.1, sin repetir."""
    m = _SECCION_ARCHIVOS.search(plan_texto)
    if not m:
        return []
    vistas, salida = set(), []
    for ruta in _RUTA.findall(m.group(1)):
        limpia = ruta.replace("\\", "/").lstrip("./")
        if limpia and limpia not in vistas:
            vistas.add(limpia)
            salida.append(limpia)
    return salida


def tocados(repo, desde):
    """Los archivos que cambiaron desde ese commit hasta lo que hay hoy."""
    salida = _git(repo, "diff", "--name-only", desde)
    return sorted(set(l.strip().replace("\\", "/")
                      for l in salida.splitlines() if l.strip()))


def _cuadra(tocado, declarados_):
    """¿Ese archivo tocado está declarado, aunque sea por su carpeta?"""
    for d in declarados_:
        if tocado == d or (d.endswith("/") and tocado.startswith(d)):
            return True
        # El plan suele nombrar la carpeta o el archivo sin su ruta completa.
        if tocado.endswith("/" + d) or d.endswith("/" + tocado):
            return True
    return False


def comparar_archivos(carpeta_fase, repo=None, desde=None):
    """`CA-01` · el archivo tocado que el plan no declara."""
    repo = repo or comun.RAIZ
    plan = os.path.join(carpeta_fase, "plan_trabajo.md")
    if not os.path.isfile(plan):
        return [Hallazgo(AVISO, carpeta_fase, 0,
                         "no tiene `plan_trabajo.md`: no hay contra qué comparar")]
    dec = declarados(comun.leer(plan))
    if not dec:
        return [Hallazgo(AVISO, plan, 0,
                         "su §2.1 no declara ningún archivo, o no está escrita "
                         "como el molde: no hay contra qué comparar (02·F8)")]
    if not desde:
        return [Hallazgo(AVISO, plan, 0,
                         "no se dijo desde qué commit comparar — se compara "
                         "contra el commit del que salió la fase (02·F8)")]

    hallazgos = []
    for archivo in tocados(repo, desde):
        if os.path.basename(archivo) in DE_LA_FASE:
            continue
        if not _cuadra(archivo, dec):
            hallazgos.append(Hallazgo(
                AVISO, archivo, 0,
                "lo tocó la fase `%s` y su plan no lo declara — o el plan se "
                "amplió sin escribirlo, o se editó de más (02·F8)"
                % os.path.basename(carpeta_fase.rstrip("/\\"))))
    return hallazgos


def comparar_casos(carpeta_fase):
    """`CA-02` · el criterio sin caso, y el caso sin criterio."""
    plan = os.path.join(carpeta_fase, "plan_trabajo.md")
    pruebas = os.path.join(carpeta_fase, "plan_pruebas.md")
    if not (os.path.isfile(plan) and os.path.isfile(pruebas)):
        return []

    texto_plan, texto_pruebas = comun.leer(plan), comun.leer(pruebas)
    criterios = set(_CRITERIO_EN_PLAN.findall(texto_plan))
    cubiertos = set(_CRITERIO_EN_PLAN.findall(texto_pruebas))
    casos = set(_CASO.findall(texto_pruebas))

    hallazgos = []
    for ca in sorted(criterios - cubiertos):
        hallazgos.append(Hallazgo(
            AVISO, pruebas, 0,
            f"el plan declara cubrir `{ca}` y el plan de pruebas no lo nombra: "
            f"ningún caso lo comprueba (13·DOC11)"))
    if criterios and not casos:
        hallazgos.append(Hallazgo(
            AVISO, pruebas, 0,
            "no tiene ningún caso `CP-NNN`, y el plan declara criterios que "
            "alguien tiene que comprobar"))
    return hallazgos


# `EP-023·HU-007` · Desde esta versión el plan dice quién lo aprobó y con qué
# versión, su §2.1 trae solo rutas exactas y el commit se compara con ella. Los
# planes aprobados antes no se revisan: se escribieron con otro molde.
DESDE = (48, 0, 0)
_APROBACION = re.compile(r"^\|?\s*\*\*Aprobación\*\*[^:|\n]*[:|]\s*(.*)$", re.M)
_VERSION = re.compile(r"con la versión\s*\**v?(\d+)\.(\d+)\.(\d+)")
_FECHA = re.compile(r",?\s*el\s+(\d{4}-\d{2}-\d{2})\b")
_SOLO_RUTAS = re.compile(r"`[^`*\s]*[^`*\s/]`(?:\s*,\s*`[^`*\s]*[^`*\s/]`)*")


def aprobacion(plan_texto):
    """`(quién, fecha, versión)` de la línea de aprobación del plan; lo que no
    diga va en `None`. Sin línea, `None`."""
    m = _APROBACION.search(plan_texto)
    if not m:
        return None
    texto = m.group(1).strip().rstrip("|").strip()
    v = _VERSION.search(texto)
    f = _FECHA.search(texto)
    quien = texto[:f.start()].strip(" ,") if f else ""
    return (quien if quien and "«" not in quien else None,
            f.group(1) if f else None,
            tuple(int(x) for x in v.groups()) if v else None)


def aprobado_desde(plan_texto, desde=DESDE):
    """¿El plan se aprobó con esa versión del estándar o una posterior?"""
    a = aprobacion(plan_texto)
    return bool(a and a[2] and a[2] >= desde)


def filas_de_archivos(plan_texto):
    """`[(línea, primera celda)]` de la tabla de la §2.1."""
    m = _SECCION_ARCHIVOS.search(plan_texto)
    if not m:
        return []
    antes = plan_texto[:m.start(1)].count("\n")
    for _, filas in comun.tablas(m.group(1)):
        return [(antes + n, celdas[0]) for n, celdas in filas if celdas]
    return []


def rutas_exactas(plan_texto):
    """Las rutas que declara la §2.1, tal cual están escritas."""
    return [r for _, celda in filas_de_archivos(plan_texto)
            for r in re.findall(r"`([^`]+)`", celda)]


def revisar_aprobado(plan_texto):
    """`CA-01` · `[(línea, motivo)]` del plan aprobado desde `DESDE`: la
    aprobación sin quién o sin fecha, y la fila que no es solo rutas exactas."""
    a = aprobacion(plan_texto)
    if not (a and a[2] and a[2] >= DESDE):
        return []
    salida = []
    if not a[0] or not a[1]:
        salida.append((0, "la aprobación no dice quién la dio o cuándo: se escribe "
                          "«quién, el AAAA-MM-DD, con la versión X.Y.Z» (02·F4)"))
    for n, celda in filas_de_archivos(plan_texto):
        if not _SOLO_RUTAS.fullmatch(celda.strip()):
            salida.append((n, "la fila «%s» de la §2.1 no es solo rutas exactas entre "
                              "comillas invertidas: sin comodines, carpetas ni "
                              "descripciones (02·F8)" % celda.strip()))
    return salida


def preparados(repo):
    """Lo que entra en el próximo commit."""
    salida = _git(repo, "diff", "--cached", "--name-only")
    return sorted(set(l.strip().replace("\\", "/")
                      for l in salida.splitlines() if l.strip()))


def comparar_preparados(proyecto, estandar=None):
    """`CA-03` · El archivo del commit que el plan no declara y ninguna regla
    autoriza. Solo cuando el commit toca una fase cuyo plan se aprobó desde
    `DESDE`: sin ese plan no hay contra qué comparar."""
    proyecto = os.path.abspath(proyecto)
    archivos = preparados(proyecto)
    fases = []
    for carpeta in fases_de(proyecto):
        rel = os.path.relpath(carpeta, proyecto).replace("\\", "/") + "/"
        if not any(a.startswith(rel) for a in archivos):
            continue
        texto = comun.leer(os.path.join(carpeta, "plan_trabajo.md"))
        if aprobado_desde(texto):
            fases.append((rel, set(rutas_exactas(texto))))
    if not fases:
        return []

    autorizadas = autorizado.reglas(proyecto, estandar)
    # Lo que el análisis prendido manda hacer de una: la misma lista que usa el
    # freno (análisis 14 del pendiente 103, acuerdo 5).
    import freno
    de_una = freno._de_una(proyecto)
    nombres = ", ".join("`%s`" % os.path.basename(rel.rstrip("/")) for rel, _ in fases)
    hallazgos = []
    for archivo in archivos:
        if any(archivo.startswith(rel) or archivo in dec for rel, dec in fases):
            continue                # un documento de la fase, o declarado
        if archivo in de_una or autorizado.quien_autoriza(archivo, autorizadas):
            continue
        hallazgos.append(Hallazgo(
            FALLA, archivo, 0,
            "entra en el commit y ni el plan de %s lo declara ni una regla "
            "autoriza escribirlo (02·F8)" % nombres))
    return hallazgos


def fases_de(proyecto):
    """Las carpetas de fase del proyecto: las que tienen su plan de trabajo."""
    raiz = os.path.join(os.path.abspath(proyecto), "documentacion", "epicas")
    salida = []
    for actual, _, archivos in os.walk(raiz):
        if "plan_trabajo.md" in archivos:
            salida.append(actual)
    return sorted(salida)


def validar(proyecto, fase=None, desde=None):
    """Sobre una fase, o sobre todas si no se nombra ninguna."""
    proyecto = os.path.abspath(proyecto)
    carpetas = [os.path.abspath(fase)] if fase else fases_de(proyecto)
    hallazgos = []
    for carpeta in carpetas:
        if desde or fase:
            hallazgos += comparar_archivos(carpeta, proyecto, desde)
        hallazgos += comparar_casos(carpeta)
    return hallazgos


def linea_resumen(proyecto):
    return "Fases con plan: %d" % len(fases_de(proyecto))


if __name__ == "__main__":
    comun.no_es_punto_de_entrada("plan")
