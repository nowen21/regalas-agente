# -*- coding: utf-8 -*-
"""`EP-023 · HU-002 · CA-04` · Los acuerdos de los que sale lo que se trabaja.

**Qué resuelve.** Al escribir un plan, el agente leía el texto del criterio y no
seguía su «Sale de» hasta los acuerdos del análisis; preguntaba lo que ya estaba
decidido, y lo que leía se perdía cuando la conversación se resumía (H-13 del
2026-10-01). Este programa recorre esa cadena y arma el texto que un enganche le
entrega al agente con cada mensaje, como las reglas (análisis 10 del pendiente
103, acuerdos 3 y 4).

**Llegan en dos momentos.**
- Mientras una fase está en curso: los acuerdos que citan los CA de esa fase. Los
  CA salen de la tabla de su plan; si el plan todavía no los nombra, son todos
  los de su HU.
- Mientras hay un análisis prendido: los acuerdos de los análisis aprobados del
  mismo pendiente.

**La fase en curso** va desde que se crea su carpeta hasta que su estado tiene
el commit anotado. La fase cuyo plan no trae la aprobación con versión y ya tiene
`funcionalidad_implementada.md` cerró antes de que existiera esa anotación, y se
da por cerrada. La usa también el freno de la HU-007.

**El tope.** La herramienta acepta un máximo por enganche. Los acuerdos que
caben llegan completos; los demás, nombrados con su tema y su número, para
leerlos en su análisis.
"""
import os
import re

import analisis_en_curso as curso
import comun
import origen
import plan_vs_hecho
from comun import leer

CARPETA = os.path.join("documentacion", "epicas")
TOPE = 10 * 1024 - 1536

_FASE = re.compile(r"^[A-Z]{1,3}(?:-[A-Z]{1,3})?-EP-\d+-HU-\d+-")
_COMMIT = re.compile(r"^\|\s*12\s*\|[^\n]*(?:✅|`[0-9a-f]{7,40}`)", re.M)
_CA_DEL_PLAN = re.compile(r"^\|\s*(CA-\d+)\s*·", re.M)
_ANALISIS = re.compile(r"^analisis-(\d+)\.md$")
_PENDIENTE = re.compile(r"^(\d+)-")

ENCABEZADO = ("[LOS ACUERDOS DE LO QUE SE TRABAJA]\n"
              "Lo que el usuario ya decidió en los análisis. No se vuelve a preguntar, "
              "y lo que el plan decida fuera de esto va marcado como propuesta del agente.")


def _subcarpetas(ruta):
    if not os.path.isdir(ruta):
        return []
    return sorted(n for n in os.listdir(ruta) if os.path.isdir(os.path.join(ruta, n)))


def _leer(ruta):
    try:
        return leer(ruta)
    except OSError:
        return ""


def en_curso(ruta_fase):
    """¿La fase está en curso? Desde que se crea su carpeta hasta que se anota su commit."""
    if _COMMIT.search(_leer(os.path.join(ruta_fase, "estado-fase.md"))):
        return False
    aprobacion = plan_vs_hecho.aprobacion(_leer(os.path.join(ruta_fase, "plan_trabajo.md")))
    vieja = not (aprobacion and aprobacion[2])
    if vieja and os.path.isfile(os.path.join(ruta_fase, "funcionalidad_implementada.md")):
        return False            # cerró antes de que existiera la anotación del commit
    return True


def fases_en_curso(proyecto):
    """Las carpetas de las fases en curso del proyecto."""
    raiz = os.path.join(proyecto, CARPETA)
    salida = []
    for epica in _subcarpetas(raiz):
        for hu in _subcarpetas(os.path.join(raiz, epica)):
            if not hu.startswith("HU-"):
                continue
            for fase in _subcarpetas(os.path.join(raiz, epica, hu)):
                ruta = os.path.join(raiz, epica, hu, fase)
                if _FASE.match(fase) and en_curso(ruta):
                    salida.append(ruta)
    return salida


def _clave(ruta_analisis, numero):
    pendiente = _PENDIENTE.match(os.path.basename(os.path.dirname(ruta_analisis)))
    n = _ANALISIS.match(os.path.basename(ruta_analisis)).group(1)
    del_pendiente = " del pendiente %s" % pendiente.group(1) if pendiente else ""
    return "Análisis %s%s, acuerdo %d" % (n, del_pendiente, numero)


def _analisis_de_la_epica(ruta_epica):
    """`{número: ruta}` de los análisis de los pendientes de la épica."""
    salida = {}
    for actual, carpetas, archivos in os.walk(ruta_epica):
        carpetas.sort()
        for nombre in sorted(archivos):
            m = _ANALISIS.match(nombre)
            if m:
                salida.setdefault(int(m.group(1)), os.path.join(actual, nombre))
    return salida


def de_la_fase(ruta_fase):
    """`[(clave, acuerdo)]` de los CA que cubre la fase, siguiendo su «Sale de»."""
    ruta_hu = os.path.dirname(ruta_fase)
    hu = _leer(os.path.join(ruta_hu, os.path.basename(ruta_hu) + ".md"))
    pedidos = set(_CA_DEL_PLAN.findall(_leer(os.path.join(ruta_fase, "plan_trabajo.md"))))
    analisis = _analisis_de_la_epica(os.path.dirname(ruta_hu))
    leidos, salida, vistos = {}, [], set()
    partes = origen._CRITERIO.split(hu)
    for i in range(1, len(partes), 2):
        ca, cuerpo = partes[i], partes[i + 1]
        if pedidos and ca not in pedidos:
            continue
        sale = origen._SALE_DE.search(cuerpo)
        for numero, puntos in origen._CITA.findall(sale.group(1) if sale else ""):
            ruta = analisis.get(int(numero))
            if not ruta:
                continue
            datos = leidos.setdefault(ruta, origen.leer_analisis(ruta))
            for p in (int(x) for x in re.findall(r"\d+", puntos)):
                celdas = datos["hacer"].get(p) or []
                citados = re.findall(r"\d+", celdas[1]) if len(celdas) > 1 else []
                for c in (int(x) for x in citados):
                    clave = _clave(ruta, c)
                    if c in datos["acordado"] and clave not in vistos:
                        vistos.add(clave)
                        salida.append((clave, datos["acordado"][c]))
    return salida


def del_analisis_prendido(proyecto):
    """`[(clave, acuerdo)]` de los análisis aprobados del pendiente del análisis prendido."""
    estado = curso.leer_estado(proyecto)
    if not estado:
        return []
    carpeta = os.path.dirname(estado["analisis"])
    numeros = sorted(int(m.group(1)) for m in map(_ANALISIS.match, os.listdir(carpeta)) if m)
    salida = []
    for n in numeros:
        ruta = os.path.join(carpeta, "analisis-%d.md" % n)
        if os.path.normcase(ruta) == os.path.normcase(estado["analisis"]) or not curso.aprobado(ruta):
            continue
        for numero, acuerdo in sorted(origen.leer_analisis(ruta)["acordado"].items()):
            salida.append((_clave(ruta, numero), acuerdo))
    return salida


def tema(acuerdo):
    """Lo que va antes de los dos puntos del acuerdo: su tema."""
    return acuerdo.split(":", 1)[0].strip() if ":" in acuerdo else acuerdo[:60].strip()


def texto(proyecto, tope=TOPE):
    """El bloque para el agente, o "" si no hay nada en curso."""
    grupos = []
    for fase in fases_en_curso(proyecto):
        acuerdos = de_la_fase(fase)
        if acuerdos:
            grupos.append(("La fase en curso `%s`:" % os.path.basename(fase), acuerdos))
    prendido = del_analisis_prendido(proyecto)
    if prendido:
        grupos.append(("El análisis prendido, de los análisis aprobados de su pendiente:", prendido))
    if not grupos:
        return ""

    partes, usado, nombrados, vistos = [ENCABEZADO], len(ENCABEZADO), [], set()
    reserva = tope // 5
    for titulo, acuerdos in grupos:
        partes.append("\n" + titulo)
        usado += len(titulo) + 1
        for clave, acuerdo in acuerdos:
            if clave in vistos:
                continue
            vistos.add(clave)
            linea = "- %s. %s" % (clave, acuerdo)
            if usado + len(linea) + 1 <= tope - reserva:
                partes.append(linea)
                usado += len(linea) + 1
            else:
                nombrados.append("%s: %s" % (clave, tema(acuerdo)))
    if nombrados:
        cola = "\n[NO CUPIERON: se leen completos en su análisis]"
        usado += len(cola)
        partes.append(cola)
        for i, nombre in enumerate(nombrados):
            if usado + len(nombre) + 3 > tope:
                partes.append("  y %d más." % (len(nombrados) - i))
                break
            partes.append("  " + nombre)
            usado += len(nombre) + 3
    return "\n".join(partes)


if __name__ == "__main__":
    comun.no_es_punto_de_entrada(la_corre="adaptadores/claude-code/hook_acuerdos.py")
