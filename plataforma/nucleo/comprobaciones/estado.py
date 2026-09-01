# -*- coding: utf-8 -*-
"""El estado de una funcionalidad, fijado por la prueba corrida.

**Hoy el estado lo pone quien escribe.** El inventario tiene 35 funcionalidades
y todas dicen «Sin verificar», no porque estén mal sino porque nada convierte
una prueba corrida en un estado escrito. Y una vez que alguien empiece a
escribirlo a mano, va a decir lo que esa persona cree, no lo que pasó.

**De dónde sale el estado.** De la cadena que ya existe escrita:

    inventario -> especificacion del modulo (§13) -> fase -> veredicto

La especificación de cada módulo tiene una tabla que dice, por funcionalidad,
qué fase la construye. La fase dice en su estado si cumple. Nada de eso hay que
inventarlo: hay que seguirlo.

**Sin prueba es «sin verificar», y no se puede cerrar.** No es lo mismo que «no
cumple»: una es que se comprobó y salió mal, la otra es que nadie comprobó. Es
la misma distinción que el veredicto de un proyecto hace entre no cumplir y no
poderse comprobar, y por el mismo motivo: confundirlas hace que nadie mire.
"""
import io
import os
import re

VERIFICADO = "verificado"
NO_CUMPLE = "no cumple"
SIN_VERIFICAR = "sin verificar"

# La fila de trazabilidad de una especificación de módulo: la funcionalidad, su
# requisito, la historia y la fase que la construye. Las columnas de la derecha
# varían entre módulos, así que se toma la fila entera y se busca la fase dentro.
_FILA = re.compile(u"(?m)^\\|\\s*(F-\\d+)\\s*\\|\\s*RF-\\d+\\s*\\|(.*)$")

# El nombre de una fase, donde aparezca: `A-EP-015-HU-001-lo-que-sea`.
_FASE = re.compile(u"([A-Z]-EP-\\d+-HU-\\d+-[a-z0-9-]+)")

# Lo que el estado de una fase declara como veredicto. **Hay dos formas, y las
# dos valen.** Las fases de la versión 1 lo escriben como «Veredicto de las
# pruebas»; las de ahora, en una tabla con «Concepto». El molde cambió, y una
# fase cerrada no se reescribe: se lee como está.
_CONCEPTO = re.compile(
    u"(?m)^\\|\\s*\\*\\*(?:Concepto|Veredicto de las pruebas)\\*\\*\\s*\\|"
    u"\\s*\\**([^|*.]+)")

# Cada funcionalidad del inventario, por su ficha.
_DEL_INVENTARIO = re.compile(u"(?m)^\\|\\s*\\*\\*Identificador\\*\\*\\s*\\|\\s*`(F-\\d+)`")


def _leer(ruta):
    try:
        with io.open(ruta, encoding="utf-8", errors="replace") as archivo:
            return archivo.read()
    except OSError:
        return ""


def funcionalidades_del_inventario(raiz):
    """Todas las que el inventario declara, en orden."""
    texto = _leer(os.path.join(raiz, "cvds", "analisis-requisitos",
                               "inventario-funcionalidades.md"))
    vistas, orden = set(), []
    for una in _DEL_INVENTARIO.findall(texto):
        if una not in vistas:
            vistas.add(una)
            orden.append(una)
    return orden


def _fases_declaradas(raiz):
    """`{funcionalidad: [fases]}`, según las especificaciones de los módulos."""
    carpeta = os.path.join(raiz, "documentacion")
    declaradas = {}
    if not os.path.isdir(carpeta):
        return declaradas
    for modulo in sorted(os.listdir(carpeta)):
        spec = os.path.join(carpeta, modulo, "spec.md")
        if not os.path.isfile(spec):
            continue
        for funcionalidad, resto in _FILA.findall(_leer(spec)):
            declaradas.setdefault(funcionalidad, [])
            for fase in _FASE.findall(resto):
                if fase not in declaradas[funcionalidad]:
                    declaradas[funcionalidad].append(fase)
    return declaradas


def _veredicto_de(raiz, fase):
    """Lo que esa fase declara, o `""` si no se encuentra o no lo dice."""
    epicas = os.path.join(raiz, "documentacion", "epicas")
    for base, carpetas, _ in os.walk(epicas):
        if os.path.basename(base) != fase:
            continue
        concepto = _CONCEPTO.search(_leer(os.path.join(base, "estado-fase.md")))
        return concepto.group(1).strip().lower() if concepto else ""
    return ""


def estado_de_todas(raiz):
    """El estado de cada funcionalidad, con de dónde sale.

    Devuelve una lista de diccionarios con `funcionalidad`, `estado`, `fases` y
    `porque`. **El estado no se lee de ninguna parte: se deriva.**
    """
    declaradas = _fases_declaradas(raiz)
    salida = []
    for funcionalidad in funcionalidades_del_inventario(raiz):
        fases = declaradas.get(funcionalidad, [])
        if not fases:
            salida.append({
                "funcionalidad": funcionalidad, "estado": SIN_VERIFICAR,
                "fases": [], "porque": "ninguna fase la construye todavía"})
            continue

        veredictos = [(fase, _veredicto_de(raiz, fase)) for fase in fases]
        sin_veredicto = [f for f, v in veredictos if not v]
        no_cumplen = [f for f, v in veredictos if v.startswith("no cumple")]

        if no_cumplen:
            estado, porque = NO_CUMPLE, "la fase %s no cumple" % no_cumplen[0]
        elif sin_veredicto:
            estado = SIN_VERIFICAR
            porque = "la fase %s no declara veredicto" % sin_veredicto[0]
        else:
            estado, porque = VERIFICADO, "%d fase(s) con veredicto" % len(fases)
        salida.append({"funcionalidad": funcionalidad, "estado": estado,
                       "fases": fases, "porque": porque})
    return salida


def se_puede_cerrar(uno):
    """Si esa funcionalidad se puede dar por terminada.

    **Sin prueba no se cierra.** Es el criterio que impide que el estado lo
    ponga quien escribe: lo pone la fase que corrió.
    """
    return uno["estado"] == VERIFICADO


def resumen(estados):
    """Cuántas hay de cada estado."""
    cuenta = {VERIFICADO: 0, NO_CUMPLE: 0, SIN_VERIFICAR: 0}
    for uno in estados:
        cuenta[uno["estado"]] = cuenta.get(uno["estado"], 0) + 1
    return cuenta
