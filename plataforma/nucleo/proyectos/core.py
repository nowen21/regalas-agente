# -*- coding: utf-8 -*-
"""Conectar un proyecto: guardar dónde vive su código, y nada más.

**Conectar no toca el proyecto.** Es una anotación de la plataforma, no una
intervención: no se escribe, no se mueve ni se crea nada dentro de su carpeta.
Es `RN-1` de la historia, y el caso `CP-009` lo comprueba comparando la carpeta
archivo por archivo.

**Qué se rechaza y qué solo se avisa**, que es la diferencia que más cuesta
mantener derecha:

| Situación | Qué pasa |
|---|---|
| La ruta no existe | Se rechaza, diciendo qué ruta se buscó |
| La ruta ya está registrada | Se rechaza, diciendo qué proyecto la tiene |
| Declara una versión de reglas que no existe | Se rechaza |
| **No declara ninguna versión** | **Se conecta**, con su aviso |
| No está bajo control de versiones | Se conecta, con su aviso |

Vacío y falso no son lo mismo: un número inventado apagaría el aviso de
desfase, y no declarar nada solo dice que ese proyecto todavía no adoptó el
estándar. Decidido con el usuario el 2026-08-25.
"""
import os
import re
import unicodedata

from django.utils import timezone

from nucleo.almacen import core as almacen
from nucleo.auditoria import core as auditoria
from nucleo.seguridad import reglas


class RutaQueNoExiste(Exception):
    """La ruta que se dio no existe en la máquina."""


class RutaYaRegistrada(Exception):
    """Otro proyecto ya apunta a esa carpeta."""


class VersionQueNoExiste(Exception):
    """El proyecto declara una versión de reglas que nunca se publicó."""


def identificador_de(nombre):
    """Un nombre de carpeta seguro, derivado del nombre del proyecto.

    **Se guarda, no se recalcula.** Si el usuario renombra el proyecto, la
    carpeta se queda donde está: es lo mismo que el histórico ya aprendió con
    sus archivos de sesión, donde el nombre cambia y la marca de adentro no.
    """
    plano = unicodedata.normalize("NFKD", nombre)
    plano = plano.encode("ascii", "ignore").decode("ascii").lower()
    plano = re.sub(r"[^a-z0-9]+", "-", plano).strip("-")
    return plano or "proyecto"


def ruta_normalizada(ruta):
    """La misma carpeta escrita de dos maneras es la misma carpeta."""
    return os.path.normcase(os.path.realpath(os.path.expanduser(str(ruta))))


def _ficha(identificador):
    """Dónde vive la ficha del proyecto, dentro de su propia carpeta.

    La ficha va **adentro** de la carpeta de documentación a propósito: así
    crear la ficha crea la carpeta, y la carpeta queda con algo dentro. Una
    carpeta vacía no entra al control de versiones, y el respaldo es el
    repositorio (`DA-01`).
    """
    return "proyectos/%s/proyecto.md" % identificador


def _texto_de_la_ficha(nombre, ruta, version, conectado):
    return (
        "# %s\n\n"
        "| Campo | Valor |\n"
        "|---|---|\n"
        "| Nombre | %s |\n"
        "| Ruta del código | %s |\n"
        "| Versión de reglas adoptada | %s |\n"
        "| Fecha de conexión | %s |\n\n"
        "La ruta viva y el estado no se guardan acá: se calculan al mirarlos.\n"
        % (nombre, nombre, ruta, version or "ninguna todavía", conectado))


def avisos_de(ruta, version_declarada):
    """Lo que hay que decirle al usuario, sin impedirle conectar."""
    dichos = []
    if not version_declarada:
        dichos.append(
            "Este proyecto todavía no declara qué versión del estándar sigue. "
            "Se conecta igual, y el aviso de desfase no va a servir hasta que "
            "la declare en su CLAUDE.md.")
    else:
        desfase = reglas.quedo_atras(version_declarada)
        if desfase:
            dichos.append("Quedó atrás: %s" % desfase)
    if not os.path.isdir(os.path.join(ruta, ".git")):
        dichos.append(
            "La carpeta de este proyecto no está bajo control de versiones: "
            "su código no tiene respaldo.")
    return dichos


def conectar(nombre, ruta, quien="el usuario", sesion=""):
    """Registra un proyecto. Devuelve el proyecto y la lista de avisos.

    Revienta antes de escribir nada si la ruta no existe, si ya está
    registrada, o si el proyecto declara una versión de reglas que no existe.
    """
    from .models import Proyecto

    pedida = str(ruta)
    if not os.path.isdir(pedida):
        raise RutaQueNoExiste(
            "No existe la carpeta «%s». Revise la ruta." % pedida)

    normal = ruta_normalizada(pedida)
    ya = Proyecto.objects.filter(ruta_normalizada=normal).first()
    if ya:
        raise RutaYaRegistrada(
            "Esa carpeta ya está registrada por el proyecto «%s»." % ya.nombre)

    version = reglas.declarada_por(pedida)
    if not reglas.existe(version):
        raise VersionQueNoExiste(
            "El proyecto declara la versión %s del estándar, y esa versión "
            "nunca se publicó." % version)

    identificador = _identificador_libre(nombre)
    conectado = timezone.localtime().date().isoformat()
    texto = _texto_de_la_ficha(nombre, pedida, version, conectado)

    auditoria.con_constancia(
        lambda comprobante: almacen.guardar(
            _ficha(identificador), texto, comprobante),
        que_se_hizo="conectar un proyecto",
        sobre_que=_ficha(identificador),
        quien=quien,
        que_cambio="quedó registrado, apuntando a %s" % pedida,
        proyecto=identificador,
        sesion=sesion)

    proyecto = _indexar(identificador, nombre, pedida, version, conectado)
    return proyecto, avisos_de(pedida, version)


def _identificador_libre(nombre):
    """El identificador del nombre, y si ya está tomado, con un número."""
    from .models import Proyecto
    base = identificador_de(nombre)
    candidato, cuantos = base, 1
    while Proyecto.objects.filter(identificador=candidato).exists():
        cuantos += 1
        candidato = "%s-%d" % (base, cuantos)
    return candidato


def _indexar(identificador, nombre, ruta, version, conectado):
    from .models import Proyecto
    proyecto, _ = Proyecto.objects.update_or_create(
        identificador=identificador,
        defaults={
            "nombre": nombre,
            "ruta_codigo": ruta,
            "ruta_normalizada": ruta_normalizada(ruta),
            "version_reglas": version,
            "conectado": conectado,
        })
    return proyecto


_CAMPO = re.compile(r"^\|\s*(?P<campo>[^|]+?)\s*\|\s*(?P<valor>.*?)\s*\|\s*$",
                    re.MULTILINE)


def reconstruir_indice():
    """Borra el índice de proyectos y lo rehace leyendo las fichas."""
    from .models import Proyecto
    Proyecto.objects.all().delete()
    carpeta = os.path.join(str(almacen.carpeta_datos()), "proyectos")
    cuantos = 0
    if not os.path.isdir(carpeta):
        return 0
    for identificador in sorted(os.listdir(carpeta)):
        texto = almacen.leer(_ficha(identificador))
        if not texto:
            continue
        campos = {m.group("campo"): m.group("valor")
                  for m in _CAMPO.finditer(texto)}
        version = campos.get("Versión de reglas adoptada", "")
        _indexar(identificador,
                 campos.get("Nombre", identificador),
                 campos.get("Ruta del código", ""),
                 "" if version == "ninguna todavía" else version,
                 campos.get("Fecha de conexión", ""))
        cuantos += 1
    return cuantos
