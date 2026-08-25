# -*- coding: utf-8 -*-
"""El registro de auditoría. **Primero la constancia, después el efecto.**

Cada vez que un componente cambia algo, entrega la acción acá. Se escribe la
constancia, y **solo si quedó escrita** se ejecuta el cambio. Al revés no
sirve: si algo falla en el medio, queda un cambio del que nadie sabe.

**Solo se agrega.** No hay función de editar ni de borrar, y eso es parte del
diseño y no un olvido (`DA-08`). Las que existen acá con esos nombres no
modifican nada: rechazan y **dejan constancia del intento**, que es lo que
pide `CA-02`.

**Ninguna clave entra.** Todo lo que se escribe pasa antes por el enmascarador
del estándar. Si ese enmascarador no está, no se escribe nada y la acción
tampoco se ejecuta: es mejor detenerse que registrar una clave en claro
(`00·N6`).

**Qué NO guarda este módulo:** la conversación de la sesión. Guarda **la
acción**, y el identificador de la sesión para poder ir a leer el porqué en lo
que esa sesión dejó escrito (`RN-4` de la especificación).
"""
import io
import os

from django.conf import settings
from django.utils import timezone

from nucleo.almacen import core as almacen
from nucleo.constancia import Constancia
from nucleo.seguridad import claves

# Las columnas del registro, en el orden en que se escriben. Los seis datos que
# pide `CA-01`, más la sesión que pide `CA-04`.
COLUMNAS = ["cuándo", "quién", "qué se hizo", "sobre qué", "qué cambió",
            "proyecto", "sesión"]

_CABECERA = ("| " + " | ".join(COLUMNAS) + " |\n"
             + "|" + "|".join(["---"] * len(COLUMNAS)) + "|\n")


class RegistroNoSePudoEscribir(Exception):
    """No se pudo dejar la constancia. La acción no se ejecuta."""


class LoRegistradoNoSeToca(Exception):
    """Se intentó editar o borrar un registro. Nunca se puede."""


def _archivo_del_mes(cuando):
    """Un archivo por mes. Suficiente para no tener uno gigante ni miles."""
    return "auditoria/%s.md" % cuando.strftime("%Y-%m")


def _limpiar(valor):
    """Tapa las claves y deja el valor apto para una celda de la tabla."""
    texto, _ = claves.tapar(str(valor or ""))
    return texto.replace("|", "/").replace("\n", " ").strip()


def registrar(que_se_hizo, sobre_que, quien, que_cambio="", proyecto="",
              sesion=""):
    """Deja la constancia de una acción. Devuelve el comprobante.

    Ese comprobante es lo que el almacén exige para escribir, y solo vale para
    `sobre_que`: es lo que impide que una constancia sirva para cambiar otra
    cosa.

    Revienta con `RegistroNoSePudoEscribir` si no se pudo escribir. Quien la
    llame **no debe atrapar esa falla para seguir igual**: ese es justo el caso
    que `CA-03` prohíbe.
    """
    cuando = timezone.localtime()
    fila = [cuando.isoformat(timespec="seconds"), quien, que_se_hizo,
            sobre_que, que_cambio, proyecto, sesion]
    try:
        linea = "| " + " | ".join(_limpiar(dato) for dato in fila) + " |\n"
        _agregar(_archivo_del_mes(cuando), linea)
    except RegistroNoSePudoEscribir:
        raise
    except Exception as falla:
        raise RegistroNoSePudoEscribir(
            "No se pudo dejar la constancia: %s" % falla)
    return Constancia(sobre_que,
                      dict(zip(COLUMNAS, [_limpiar(dato) for dato in fila])))


def con_constancia(accion, que_se_hizo, sobre_que, quien, que_cambio="",
                   proyecto="", sesion=""):
    """Escribe la constancia y **solo entonces** ejecuta la acción.

    Es la forma en que los demás componentes deben cambiar algo, y la única
    que no obliga a acordarse del orden. A `accion` se le entrega el
    comprobante, que es lo que el almacén va a pedir:

        con_constancia(lambda c: almacen.guardar("uno.md", "# Uno", c),
                       que_se_hizo="guardar un documento",
                       sobre_que="uno.md", quien="el agente")

    Devuelve lo que devuelva `accion`. Si la constancia no se puede escribir,
    `accion` no llega a ejecutarse.
    """
    comprobante = registrar(que_se_hizo, sobre_que, quien, que_cambio,
                            proyecto, sesion)
    return accion(comprobante)


def _agregar(nombre, linea):
    """Agrega una línea al final. Nunca reescribe lo que ya está."""
    destino = almacen._ruta_real(nombre)
    carpeta = os.path.dirname(destino)
    try:
        os.makedirs(carpeta, exist_ok=True)
        nuevo = not os.path.exists(destino)
        with io.open(destino, "a", encoding="utf-8", newline="\n") as archivo:
            if nuevo:
                archivo.write(_CABECERA)
            archivo.write(linea)
    except OSError as falla:
        raise RegistroNoSePudoEscribir(
            "No se pudo escribir en %s: %s" % (nombre, falla))
    _indexar(linea)


def editar(*_args, **_opciones):
    """No se puede, y el intento queda registrado (`CA-02`)."""
    _dejar_constancia_del_intento("editar")
    raise LoRegistradoNoSeToca("Lo registrado no se edita.")


def borrar(*_args, **_opciones):
    """No se puede, y el intento queda registrado (`CA-02`)."""
    _dejar_constancia_del_intento("borrar")
    raise LoRegistradoNoSeToca("Lo registrado no se borra.")


def _dejar_constancia_del_intento(que):
    """Registra el intento. Si tampoco se puede, se calla y deja pasar el rechazo.

    Acá sí se traga la falla, y es a propósito: lo que importa es que la
    edición **no ocurra**. Un registro que no se pudo escribir no debe
    convertir un rechazo correcto en otro error distinto.
    """
    try:
        registrar(que_se_hizo="intento de %s el registro" % que,
                  sobre_que="el registro de auditoría",
                  quien="desconocido",
                  que_cambio="nada: se rechazó")
    except Exception:
        pass


def _indexar(linea):
    from .models import Registro
    partes = [parte.strip() for parte in linea.strip().strip("|").split("|")]
    if len(partes) != len(COLUMNAS):
        return
    Registro.objects.crear_desde_texto(dict(zip(COLUMNAS, partes)))


def reconstruir_indice():
    """Borra el índice del registro y lo rehace leyendo el texto.

    Igual que en el almacén: el texto es la fuente. Devuelve cuántas filas
    entraron.
    """
    from .models import Registro
    Registro.objects.todos().delete()
    carpeta = os.path.join(str(settings.CARPETA_DATOS), "auditoria")
    cuantas = 0
    if not os.path.isdir(carpeta):
        return 0
    for nombre in sorted(os.listdir(carpeta)):
        with io.open(os.path.join(carpeta, nombre), encoding="utf-8") as archivo:
            for linea in archivo:
                if not linea.startswith("|") or "---" in linea:
                    continue
                if linea.strip().strip("|").split("|")[0].strip() == COLUMNAS[0]:
                    continue
                _indexar(linea)
                cuantas += 1
    return cuantas
