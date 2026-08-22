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

import comun
from comun import AVISO, Hallazgo, relativo

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
