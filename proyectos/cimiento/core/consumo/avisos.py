# -*- coding: utf-8 -*-
"""`EP-025·HU-027` · La pantalla «Gasto» se entera en el momento de lo que guarda el vigilante.

**Sin relojes** (análisis 1 del pendiente 124, acuerdos 4 y 7). El vigilante,
que es otro proceso, le avisa a Cimiento con un `POST` local en cuanto guarda
algo nuevo. Cimiento guarda el aviso en memoria y despierta a cada pantalla que
escucha por SSE; la pantalla vuelve a pedir lo que se ve, que sale de la base.
Nadie pregunta cada cierto tiempo: el que espera, duerme hasta que lo despiertan.

**Con Cimiento apagado el aviso se pierde sin daño**: al abrir la pantalla todo
se lee de la base. El tope de 2 segundos del `POST` es para que un Cimiento
colgado no detenga al vigilante; no es un intervalo.
"""
import os
import threading
import urllib.request

ESPERA_MAXIMA_DEL_AVISO = 2


class Avisos:
    """El número de avisos que llevan llegados, y quién espera el siguiente."""

    _condicion = threading.Condition()
    _numero = 0

    @classmethod
    def numero(cls):
        with cls._condicion:
            return cls._numero

    @classmethod
    def avisar(cls):
        """Hay datos nuevos: despierta a todos los que esperan."""
        with cls._condicion:
            cls._numero += 1
            cls._condicion.notify_all()
            return cls._numero

    @classmethod
    def esperar(cls, visto):
        """Duerme hasta que haya un aviso después de `visto`, y devuelve el número nuevo."""
        with cls._condicion:
            cls._condicion.wait_for(lambda: cls._numero != visto)
            return cls._numero


def eventos():
    """El flujo SSE de una pantalla abierta: un evento `gasto` por cada aviso."""
    visto = Avisos.numero()
    yield ": escuchando\n\n"
    while True:
        visto = Avisos.esperar(visto)
        yield "event: gasto\ndata: %d\n\n" % visto


def direccion_del_aviso():
    """`http://127.0.0.1:«PUERTO»/gasto/aviso/`, con el puerto del `.env` de Cimiento."""
    from config.ambiente import leer
    cimiento = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    puerto = os.environ.get("PUERTO") or leer(os.path.join(cimiento, ".env")).get("PUERTO") or "8000"
    return "http://127.0.0.1:%s/gasto/aviso/" % puerto


def avisar_a_cimiento(direccion=None):
    """Lo llama el vigilante después de guardar. `True` si Cimiento recibió el aviso."""
    try:
        peticion = urllib.request.Request(direccion or direccion_del_aviso(), data=b"", method="POST")
        with urllib.request.urlopen(peticion, timeout=ESPERA_MAXIMA_DEL_AVISO) as respuesta:
            return respuesta.status == 204
    except (OSError, ValueError):
        return False
