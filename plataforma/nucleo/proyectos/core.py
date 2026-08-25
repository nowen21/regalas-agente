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

**Desde la fase H, conectar tiene reversa.** Se puede desconectar, renombrar y
corregir la versión declarada, y **nada de eso borra ni mueve nada**:
desconectar deja la documentación donde está, y renombrar deja la carpeta donde
está. Un proyecto desconectado **libera su ruta**, y volver a conectar esa
carpeta lo **reactiva** en vez de crear uno nuevo: crear uno nuevo dejaría la
documentación del anterior sin dueño.

**Desde la fase C, la ruta que se pierde se avisa y se corrige.** El aviso dice
**qué ruta se buscó**, y corregirla comprueba lo mismo que al conectar. Perder
la ruta no pierde nada: la documentación vive en la plataforma, no allá.
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


class NombreVacio(Exception):
    """Se intentó dejar un proyecto sin nombre."""


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


def _texto_de_la_ficha(nombre, ruta, version, conectado, desconectado=""):
    """El texto de la ficha. Es la fuente; el índice se rehace desde acá.

    El campo de desconexión va en la ficha y no solo en el índice: si viviera
    solo en la base, rehacer el índice resucitaría al proyecto desconectado.
    """
    return (
        "# %s\n\n"
        "| Campo | Valor |\n"
        "|---|---|\n"
        "| Nombre | %s |\n"
        "| Ruta del código | %s |\n"
        "| Versión de reglas adoptada | %s |\n"
        "| Fecha de conexión | %s |\n"
        "| Fecha de desconexión | %s |\n\n"
        "La ruta viva y el estado no se guardan acá: se calculan al mirarlos.\n"
        % (nombre, nombre, ruta, version or "ninguna todavía", conectado,
           desconectado or "sigue conectado"))


def avisos_de(ruta, version_declarada):
    """Lo que hay que decirle al usuario, sin impedirle conectar."""
    dichos = []
    if not os.path.isdir(str(ruta)):
        # **El aviso nombra la ruta**, no solo dice que falló (`RN-2` de la
        # historia). Sin ella el usuario no puede ver si fue un renombre, un
        # movimiento, o un disco que no está montado.
        dichos.append(
            "La carpeta de su código ya no está donde estaba. Se buscó en "
            "«%s». Su documentación sigue guardada acá." % ruta)
        return dichos
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
    ya = Proyecto.objects.filter(ruta_normalizada=normal,
                                 desconectado="").first()
    if ya:
        raise RutaYaRegistrada(
            "Esa carpeta ya está registrada por el proyecto «%s»." % ya.nombre)

    # Un desconectado liberó su ruta, pero su documentación se quedó. Volver a
    # conectar esa carpeta lo **reactiva**: crear uno nuevo dejaría lo suyo sin
    # dueño. Decidido con el usuario el 2026-08-25.
    dormido = Proyecto.objects.filter(ruta_normalizada=normal).first()
    if dormido:
        return reconectar(dormido, quien=quien, sesion=sesion)

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


def desconectado_en(ruta):
    """El proyecto desconectado que tenía esa ruta, o None.

    Sirve para que la pantalla avise **antes de confirmar** que ahí hay una
    historia guardada: si el usuario quería empezar de cero con esa carpeta,
    reactivar le devolvería lo viejo sin haberlo pedido.
    """
    from .models import Proyecto
    if not os.path.isdir(str(ruta)):
        return None
    return Proyecto.objects.filter(
        ruta_normalizada=ruta_normalizada(ruta)).exclude(
            desconectado="").first()


def desconectar(proyecto, quien="el usuario", sesion=""):
    """Saca el proyecto de la lista. **No borra su documentación.**

    Escribe la fecha en su ficha, que es la fuente. Devuelve el proyecto.
    """
    cuando = timezone.localtime().date().isoformat()
    _reescribir_ficha(proyecto, desconectado=cuando,
                      que_se_hizo="desconectar un proyecto",
                      que_cambio="su documentación se queda en la plataforma",
                      quien=quien, sesion=sesion)
    return _indexar(proyecto.identificador, proyecto.nombre,
                    proyecto.ruta_codigo, proyecto.version_reglas,
                    proyecto.conectado, desconectado=cuando)


def reconectar(proyecto, quien="el usuario", sesion=""):
    """Vuelve a conectar un desconectado, con lo que tenía. Devuelve el par
    del `conectar` normal: el proyecto y sus avisos."""
    _reescribir_ficha(proyecto, desconectado="",
                      que_se_hizo="volver a conectar un proyecto",
                      que_cambio="vuelve con la documentación que ya tenía",
                      quien=quien, sesion=sesion)
    vuelto = _indexar(proyecto.identificador, proyecto.nombre,
                      proyecto.ruta_codigo, proyecto.version_reglas,
                      proyecto.conectado, desconectado="")
    return vuelto, avisos_de(vuelto.ruta_codigo, vuelto.version_reglas)


def renombrar(proyecto, nombre_nuevo, quien="el usuario", sesion=""):
    """Le cambia el nombre. **El identificador no cambia, así que su carpeta
    de documentación se queda donde está.**"""
    nombre_nuevo = (nombre_nuevo or "").strip()
    if not nombre_nuevo:
        raise NombreVacio("Un proyecto tiene que llamarse de alguna manera.")
    viejo = proyecto.nombre
    _reescribir_ficha(proyecto, nombre=nombre_nuevo,
                      que_se_hizo="renombrar un proyecto",
                      que_cambio="de «%s» a «%s»" % (viejo, nombre_nuevo),
                      quien=quien, sesion=sesion)
    return _indexar(proyecto.identificador, nombre_nuevo,
                    proyecto.ruta_codigo, proyecto.version_reglas,
                    proyecto.conectado, desconectado=proyecto.desconectado)


def corregir_ruta(proyecto, ruta_nueva, quien="el usuario", sesion=""):
    """Vuelve a apuntar el proyecto a otra carpeta. Devuelve el proyecto.

    **La ruta nueva se comprueba igual que al conectar**: que exista, y que no
    la tenga ya otro proyecto. Corregir no puede ser una puerta de atrás para
    lo que conectar rechaza.

    **Y se relee la versión de reglas de la carpeta nueva.** La carpeta cambió,
    así que lo que declara puede ser otra cosa; dejar la vieja sería afirmar
    sobre lo que no se leyó.
    """
    from .models import Proyecto

    pedida = str(ruta_nueva or "").strip()
    if not os.path.isdir(pedida):
        raise RutaQueNoExiste(
            "No existe la carpeta «%s». Se deja la ruta que tenía." % pedida)

    normal = ruta_normalizada(pedida)
    ya = Proyecto.objects.filter(ruta_normalizada=normal,
                                 desconectado="").exclude(pk=proyecto.pk).first()
    if ya:
        raise RutaYaRegistrada(
            "Esa carpeta ya está registrada por el proyecto «%s». Se deja la "
            "ruta que tenía." % ya.nombre)

    version = reglas.declarada_por(pedida)
    if not reglas.existe(version):
        raise VersionQueNoExiste(
            "La carpeta nueva declara la versión %s del estándar, y esa "
            "versión nunca se publicó. Se deja la ruta que tenía." % version)

    vieja = proyecto.ruta_codigo
    _reescribir_ficha(proyecto, ruta=pedida, version=version,
                      que_se_hizo="corregir la ruta de un proyecto",
                      que_cambio="de «%s» a «%s»" % (vieja, pedida),
                      quien=quien, sesion=sesion)
    return _indexar(proyecto.identificador, proyecto.nombre, pedida, version,
                    proyecto.conectado, desconectado=proyecto.desconectado)


def corregir_version(proyecto, quien="el usuario", sesion=""):
    """Vuelve a leer del proyecto qué versión declara, y la comprueba.

    No se pide escrita, por lo mismo que al conectar: teclearla es la forma de
    que quede un número que no existe.
    """
    if not os.path.isdir(proyecto.ruta_codigo):
        raise RutaQueNoExiste(
            "No existe la carpeta «%s», así que no hay de dónde leer la "
            "versión." % proyecto.ruta_codigo)

    version = reglas.declarada_por(proyecto.ruta_codigo)
    if not reglas.existe(version):
        raise VersionQueNoExiste(
            "El proyecto declara la versión %s del estándar, y esa versión "
            "nunca se publicó. Se deja la que tenía." % version)

    viejo = proyecto.version_reglas
    _reescribir_ficha(proyecto, version=version,
                      que_se_hizo="corregir la versión de reglas declarada",
                      que_cambio="de «%s» a «%s»" % (viejo or "ninguna",
                                                     version or "ninguna"),
                      quien=quien, sesion=sesion)
    return _indexar(proyecto.identificador, proyecto.nombre,
                    proyecto.ruta_codigo, version, proyecto.conectado,
                    desconectado=proyecto.desconectado)


def _reescribir_ficha(proyecto, que_se_hizo, que_cambio, quien, sesion,
                      nombre=None, version=None, desconectado=None, ruta=None):
    """Vuelve a escribir la ficha con el cambio, dejando la constancia antes.

    **Reescribe la ficha entera, nunca la carpeta.** Lo que hay dentro de la
    carpeta de documentación de ese proyecto no se toca.
    """
    texto = _texto_de_la_ficha(
        proyecto.nombre if nombre is None else nombre,
        proyecto.ruta_codigo if ruta is None else ruta,
        proyecto.version_reglas if version is None else version,
        proyecto.conectado,
        proyecto.desconectado if desconectado is None else desconectado)
    auditoria.con_constancia(
        lambda comprobante: almacen.guardar(
            _ficha(proyecto.identificador), texto, comprobante),
        que_se_hizo=que_se_hizo,
        sobre_que=_ficha(proyecto.identificador),
        quien=quien,
        que_cambio=que_cambio,
        proyecto=proyecto.identificador,
        sesion=sesion)


def _identificador_libre(nombre):
    """El identificador del nombre, y si ya está tomado, con un número."""
    from .models import Proyecto
    base = identificador_de(nombre)
    candidato, cuantos = base, 1
    while Proyecto.objects.filter(identificador=candidato).exists():
        cuantos += 1
        candidato = "%s-%d" % (base, cuantos)
    return candidato


def _indexar(identificador, nombre, ruta, version, conectado,
             desconectado=""):
    from .models import Proyecto
    proyecto, _ = Proyecto.objects.update_or_create(
        identificador=identificador,
        defaults={
            "nombre": nombre,
            "ruta_codigo": ruta,
            "ruta_normalizada": ruta_normalizada(ruta),
            "version_reglas": version,
            "conectado": conectado,
            "desconectado": desconectado,
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
        # Una ficha de antes de la fase H no trae este campo, y se lee como un
        # proyecto conectado. Por eso no hubo que migrar nada.
        fuera = campos.get("Fecha de desconexión", "")
        _indexar(identificador,
                 campos.get("Nombre", identificador),
                 campos.get("Ruta del código", ""),
                 "" if version == "ninguna todavía" else version,
                 campos.get("Fecha de conexión", ""),
                 desconectado="" if fuera == "sigue conectado" else fuera)
        cuantos += 1
    return cuantos
