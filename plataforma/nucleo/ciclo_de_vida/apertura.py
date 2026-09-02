# -*- coding: utf-8 -*-
"""Abrir una unidad de trabajo con sus documentos ya formados — `F-011`.

**El nombre no se escribe a mano: sale del identificador.** Una fase se llama
`<LETRA>-<EPICA>-<HU>-<de-qué-trata>`, y las tres primeras partes las pone la
plataforma. Escribirlas a mano es de donde salen las fases que no se sabe a qué
historia pertenecen.

**Una fase sin historia no se abre.** No es una comodidad: `02·F0` pide que cada
eslabón cuelgue del anterior, y una fase suelta es trabajo que nadie pidió.

**Nada se pisa.** Si la carpeta ya existe, se dice y no se toca. Abrir dos veces
la misma fase sobre una que ya tiene trabajo escrito sería el único daño
irreparable de este módulo.
"""
import io
import os
import re
import unicodedata

from nucleo.auditoria.core import con_constancia
from nucleo.ciclo_de_vida import core, moldes


class NoSePuedeAbrir(Exception):
    """Falta la historia, falta el título, o la carpeta ya existe."""


# Los cinco documentos de una fase, con el tipo cuyo molde les toca.
LOS_CINCO = (
    ("plan_trabajo.md", "plan de trabajo"),
    ("plan_pruebas.md", "plan de pruebas"),
    ("resultado_pruebas.md", "resultado de pruebas"),
    ("funcionalidad_implementada.md", "funcionalidad implementada"),
    ("estado-fase.md", "estado de fase"),
)

_LETRA = re.compile(r"^[A-Z]$")
_EPICA = re.compile(r"^EP-\d{3}$")
_HISTORIA = re.compile(r"^HU-\d{3}$")


def en_minusculas_con_guiones(titulo):
    """El título, como se escribe dentro de un nombre de carpeta.

    Se quitan las tildes y la eñe pasa a `n`: es lo que hacen los nombres que ya
    están en el repositorio, y un nombre de carpeta con tilde se rompe distinto
    en cada sistema.
    """
    sin_tildes = "".join(
        letra for letra in unicodedata.normalize("NFD", titulo)
        if unicodedata.category(letra) != "Mn")
    limpio = re.sub(r"[^a-zA-Z0-9]+", "-", sin_tildes).strip("-").lower()
    return limpio


def nombre_de_fase(letra, epica, historia, titulo):
    """`D-EP-009-HU-001-la-constancia-va-antes-que-el-efecto`, armado.

    **Es la única forma de nombrar una fase.** Se expone aparte para poder
    comprobarla sin tocar el disco.
    """
    if not _LETRA.match(letra or ""):
        raise NoSePuedeAbrir(
            "la letra de la fase es una sola mayúscula, y llegó %r" % (letra,))
    if not _EPICA.match(epica or ""):
        raise NoSePuedeAbrir("la épica se escribe `EP-000`, y llegó %r" % (epica,))
    if not _HISTORIA.match(historia or ""):
        raise NoSePuedeAbrir(
            "la historia se escribe `HU-000`, y llegó %r" % (historia,))
    de_que_trata = en_minusculas_con_guiones(titulo)
    if not de_que_trata:
        raise NoSePuedeAbrir(
            "la fase necesita un título: el nombre dice de qué trata, no solo "
            "a qué historia pertenece")
    return "%s-%s-%s-%s" % (letra, epica, historia, de_que_trata)


def _raiz_del_proyecto(proyecto):
    from nucleo.proyectos.models import Proyecto
    try:
        return Proyecto.objects.get(identificador=proyecto).ruta_codigo
    except Proyecto.DoesNotExist:
        return ""


def _carpeta_de_la_historia(raiz, epica, historia):
    """La carpeta de esa historia dentro del proyecto, o `""` si no está.

    Se busca por el prefijo del identificador, no por el nombre completo: el
    título de la historia va pegado al identificador y **no se puede adivinar**.
    """
    epicas = os.path.join(raiz, "documentacion", "epicas")
    if not os.path.isdir(epicas):
        return ""
    for carpeta_epica in sorted(os.listdir(epicas)):
        if not carpeta_epica.startswith(epica + "-"):
            continue
        dentro = os.path.join(epicas, carpeta_epica)
        if not os.path.isdir(dentro):
            continue
        for carpeta_hu in sorted(os.listdir(dentro)):
            if carpeta_hu.startswith(historia + "-") and os.path.isdir(
                    os.path.join(dentro, carpeta_hu)):
                return os.path.join(dentro, carpeta_hu)
    return ""


def donde_iria(proyecto, letra, epica, historia, titulo):
    """Dónde quedaría la fase, sin crear nada. Devuelve `(carpeta, nombre)`."""
    nombre = nombre_de_fase(letra, epica, historia, titulo)
    raiz = _raiz_del_proyecto(proyecto)
    if not raiz:
        raise NoSePuedeAbrir(
            "el proyecto %r no está conectado: no se sabe dónde escribir"
            % (proyecto,))
    de_la_historia = _carpeta_de_la_historia(raiz, epica, historia)
    if not de_la_historia:
        raise NoSePuedeAbrir(
            "no existe la historia %s dentro de %s: una fase sin historia no "
            "se abre, porque sería trabajo que nadie pidió" % (historia, epica))
    return os.path.join(de_la_historia, nombre), nombre


def _texto_inicial(tipo, nombre, epica, historia):
    """El molde, encabezado con a qué fase pertenece.

    El molde se lee del estándar **en el momento**, no se copia: uno copiado
    envejece en cuanto el estándar cambie el original.
    """
    cuerpo = moldes.texto_del_molde(core._carpeta_de_plantillas(), tipo)
    encabezado = (
        "<!-- Fase `%s` · %s · %s — abierta desde la plataforma.\n"
        "     El molde se copió del estándar al abrir; lo que diga acá manda "
        "sobre lo que\n     el molde traía de ejemplo. -->\n\n"
        % (nombre, epica, historia))
    if not cuerpo:
        return encabezado + (
            "# %s\n\n**Sin molde en el estándar.** Se abre vacío a propósito: "
            "inventarle uno acá sería un molde que nadie mantiene.\n" % tipo)
    return encabezado + cuerpo


def abrir_fase(proyecto, letra, epica, historia, titulo, quien="el usuario",
               sesion=""):
    """Crea la carpeta de la fase con sus cinco documentos. No pisa nada.

    Devuelve `{"nombre", "carpeta", "documentos"}`.
    """
    carpeta, nombre = donde_iria(proyecto, letra, epica, historia, titulo)
    if os.path.isdir(carpeta):
        raise NoSePuedeAbrir(
            "la fase %s ya existe; no se toca, porque puede tener trabajo "
            "escrito" % nombre)

    def escribir(_comprobante):
        os.makedirs(carpeta)
        escritos = []
        for archivo, tipo in LOS_CINCO:
            destino = os.path.join(carpeta, archivo)
            with io.open(destino, "w", encoding="utf-8", newline="") as abierto:
                abierto.write(_texto_inicial(tipo, nombre, epica, historia))
            escritos.append(archivo)
        return {"nombre": nombre, "carpeta": carpeta, "documentos": escritos}

    return con_constancia(
        escribir,
        que_se_hizo="abrir una fase con sus cinco documentos",
        sobre_que=nombre, quien=quien, proyecto=proyecto, sesion=sesion,
        que_cambio="cinco documentos nuevos, con el molde del estándar")


def dicho(abierta):
    """La frase para la consola."""
    return "Abierta la fase %s con sus %d documentos, en %s" % (
        abierta["nombre"], len(abierta["documentos"]), abierta["carpeta"])
