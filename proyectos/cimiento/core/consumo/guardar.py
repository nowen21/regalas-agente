# -*- coding: utf-8 -*-
"""`EP-025·HU-006` · Pone en la base lo que el lector sacó de un `.jsonl`.

**Sin duplicar.** Una llamada es única por sesión y mensaje: si vuelve, se
actualiza con su última línea. Enganches y archivos leídos son únicos por
sesión e identificador. Leer dos veces lo mismo deja la base igual.

**Un archivo sin cambios no se abre.** El avance guarda el tamaño y la fecha de
modificación; si siguen iguales, no hay nada nuevo. Si el archivo se achicó,
Claude Code lo reescribió: se lee desde el comienzo.

**Todo o nada por archivo**: lo guardado y el avance van en una transacción.

**La misma llamada por dos caminos** (`EP-025·HU-007`): la telemetría la trae
antes, con la solicitud como mensaje. Cuando el `.jsonl` la encuentra por la
solicitud, le pone su `message.id`; si llega primero el `.jsonl`, la
telemetría la reconoce y no la repite.
"""
import glob
import json
import os
import re
from functools import lru_cache

from django.db import IntegrityError, transaction

from core.proyectos.claude import proyectos_de_claude
from core.proyectos.models import Proyecto

from .lector import LectorDeClaudeCode
from .models import (AvanceDeLectura, GastoDeArchivo, GastoDeEnganche, GastoDeHerramienta, Llamada,
                     Pedido)
from .trabajo import trabajo_de


@lru_cache(maxsize=1)
def _recuperador():
    # Aquí y no arriba: el recuperador arma el mapa de tareas, y solo hace falta al guardar.
    from core.herramientas.recuperar import RecuperadorDeReglas
    return RecuperadorDeReglas()


def palabra_clave(texto):
    """La palabra de `01·C28` con que abre el mensaje (`EP-025·HU-010`), o ""."""
    try:
        return _recuperador().palabra_clave(texto)[:40]
    except Exception:  # noqa: BLE001  Sin la lista, el mensaje queda sin palabra; no se pierde el gasto.
        return ""


class GuardadoDeConsumo:
    """Lee y guarda los `.jsonl` de un proyecto."""

    def __init__(self, proyecto, base=None):
        self.proyecto = proyecto
        self.base = base or proyectos_de_claude()

    def carpeta(self):
        return os.path.join(self.base, self.proyecto.carpeta_claude)

    def archivos(self):
        """Los `.jsonl` de las sesiones y los de sus agentes auxiliares (`EP-025·HU-010`)."""
        return sorted(glob.glob(os.path.join(self.carpeta(), "*.jsonl"))
                      + glob.glob(os.path.join(self.carpeta(), "*", "subagents", "agent-*.jsonl")))

    @staticmethod
    def agente_de(ruta):
        """El `agentType` del `.meta.json` de un agente auxiliar, o ""."""
        if os.path.basename(os.path.dirname(ruta)) != "subagents":
            return ""
        try:
            with open(ruta[:-len(".jsonl")] + ".meta.json", encoding="utf-8") as meta:
                return str(json.load(meta).get("agentType") or "auxiliar")[:100]
        except (OSError, ValueError, AttributeError):
            return "auxiliar"

    def leer_todo(self):
        """`{"llamadas", "enganches", "archivos", "leidos"}`: lo nuevo que quedó guardado."""
        cuenta = {"llamadas": 0, "enganches": 0, "archivos": 0, "herramientas": 0, "leidos": 0}
        for ruta in self.archivos():
            nuevo = self.leer_archivo(ruta)
            if nuevo is None:
                continue
            cuenta["leidos"] += 1
            for clave, valor in nuevo.items():
                cuenta[clave] += valor
        return cuenta

    def leer_archivo(self, ruta):
        """Lo nuevo de un archivo, o `None` si no cambió desde la última vez."""
        try:
            estado = os.stat(ruta)
        except OSError:
            return None
        avance, _ = AvanceDeLectura.objects.get_or_create(archivo=os.path.abspath(ruta))
        if avance.tamano == estado.st_size and avance.modificado == estado.st_mtime and avance.posicion:
            return None
        desde = avance.posicion if estado.st_size >= avance.posicion else 0
        lectura = LectorDeClaudeCode(ruta, desde).leer(avance.pedido if desde else "")
        with transaction.atomic():
            nuevo = self.guardar(lectura, self.agente_de(ruta))
            avance.posicion, avance.tamano, avance.modificado = lectura.hasta, estado.st_size, estado.st_mtime
            avance.pedido = lectura.ultimo_pedido[:64]
            avance.save()
        return nuevo

    def guardar_pedidos(self, lectura):
        """`{identificador: Pedido}` de los mensajes de la lectura y de los que siguen de antes."""
        pedidos = {}
        for p in lectura.pedidos:
            pedidos[p.identificador], _ = Pedido.objects.get_or_create(
                sesion=p.sesion, identificador=p.identificador[:64],
                defaults={"proyecto": self.proyecto, "fecha": p.fecha, "palabra": palabra_clave(p.texto)})
        faltan = {ll.pedido for ll in lectura.llamadas if ll.pedido} | set(lectura.rutas)
        for pedido in Pedido.objects.filter(proyecto=self.proyecto, identificador__in=faltan - set(pedidos)):
            pedidos[pedido.identificador] = pedido
        for identificador, rutas in lectura.rutas.items():
            pedido = pedidos.get(identificador)
            trabajo = trabajo_de(rutas)[:200]
            if pedido and trabajo and not pedido.trabajo:
                pedido.trabajo = trabajo
                pedido.save(update_fields=["trabajo"])
        return pedidos

    def guardar(self, lectura, agente=""):
        pedidos = self.guardar_pedidos(lectura)
        nuevas = sum(guardar_llamada(self.proyecto, llamada, {"pedido": pedidos.get(llamada.pedido),
                                                              "agente": agente})
                     for llamada in lectura.llamadas)
        herramientas = sum(GastoDeHerramienta.objects.update_or_create(
            sesion=h.sesion, identificador=h.identificador,
            defaults={"proyecto": self.proyecto, "fecha": h.fecha, "nombre": h.nombre[:100],
                      "caracteres": h.caracteres})[1] for h in lectura.herramientas)
        enganches = sum(GastoDeEnganche.objects.get_or_create(
            sesion=e.sesion, identificador=e.identificador,
            defaults={"proyecto": self.proyecto, "fecha": e.fecha, "nombre": e.nombre[:200],
                      "evento": e.evento[:50], "caracteres": e.caracteres})[1] for e in lectura.enganches)
        # Si la telemetría lo trajo antes, venía en bytes: el `.jsonl` lo deja en caracteres.
        archivos = sum(GastoDeArchivo.objects.update_or_create(
            sesion=a.sesion, identificador=a.identificador,
            defaults={"proyecto": self.proyecto, "fecha": a.fecha, "ruta": a.ruta[:500],
                      "caracteres": a.caracteres})[1] for a in lectura.archivos)
        return {"llamadas": nuevas, "enganches": enganches, "archivos": archivos, "herramientas": herramientas}


def leer_lo_nuevo(base=None):
    """Lee lo nuevo de los `.jsonl` de todos los proyectos activos (`EP-025·HU-008`).

    La corre el tablero al abrirse: lo que llegó con Cimiento apagado entra
    antes de mostrar nada. Solo abre los archivos que cambiaron.
    """
    for proyecto in Proyecto.objects.filter(activo=True):
        GuardadoDeConsumo(proyecto, base).leer_todo()


_DATOS = ("fecha", "modelo", "entrada", "cache_creada", "cache_leida", "salida", "auxiliar")


def guardar_llamada(proyecto, llamada, extra=None):
    """Guarda una llamada de cualquiera de los dos caminos. `True` si es nueva.
    `extra`: su mensaje y su agente (`EP-025·HU-010`); un mensaje vacío no pisa el que tenga."""
    datos = {campo: getattr(llamada, campo) for campo in _DATOS}
    datos.update({clave: valor for clave, valor in (extra or {}).items() if valor or clave == "agente"})
    del_jsonl = llamada.mensaje != llamada.solicitud
    if llamada.solicitud:
        existente = Llamada.objects.filter(sesion=llamada.sesion, solicitud=llamada.solicitud).first()
        if existente:
            if del_jsonl:
                Llamada.objects.filter(pk=existente.pk).update(mensaje=llamada.mensaje, proyecto=proyecto, **datos)
            return False
    if not del_jsonl and Llamada.objects.filter(sesion=llamada.sesion, mensaje=llamada.mensaje).exists():
        return False
    _, creada = Llamada.objects.update_or_create(
        sesion=llamada.sesion, mensaje=llamada.mensaje,
        defaults={"proyecto": proyecto, "solicitud": llamada.solicitud or None, **datos})
    return creada


class GuardadoDeTelemetria:
    """`EP-025·HU-007` · Guarda lo que llegó por telemetría, en las tablas de la HU-006.

    El evento no dice el proyecto: sale de la sesión, buscando su `.jsonl` en
    la carpeta de Claude Code de cada proyecto activo. Un evento de una sesión
    sin proyecto se descarta; si después se registra el proyecto, la lectura
    del `.jsonl` lo trae.
    """

    _SESION = re.compile(r"^[A-Za-z0-9-]{1,64}$")

    def __init__(self, base=None):
        self.base = base or proyectos_de_claude()
        self._proyectos = {}

    def proyecto_de(self, sesion):
        if sesion not in self._proyectos:
            self._proyectos[sesion] = None
            if self._SESION.match(sesion or ""):
                self._proyectos[sesion] = next(
                    (p for p in Proyecto.objects.filter(activo=True)
                     if os.path.isfile(os.path.join(self.base, p.carpeta_claude, sesion + ".jsonl"))), None)
        return self._proyectos[sesion]

    def guardar(self, llamadas, archivos, herramientas=()):
        """`{"llamadas", "archivos", "herramientas", "descartados"}`: lo nuevo que quedó guardado."""
        cuenta = {"llamadas": 0, "archivos": 0, "herramientas": 0, "descartados": 0}
        for llamada in llamadas:
            proyecto = self.proyecto_de(llamada.sesion)
            if proyecto is None:
                cuenta["descartados"] += 1
                continue
            # El mensaje solo se une si ya lo trajo el `.jsonl`: la telemetría no trae su texto.
            pedido = Pedido.objects.filter(sesion=llamada.sesion, identificador=llamada.pedido).first() \
                if llamada.pedido else None
            try:
                with transaction.atomic():
                    cuenta["llamadas"] += guardar_llamada(proyecto, llamada, {"pedido": pedido})
            except IntegrityError:
                pass  # La guardó al mismo tiempo la lectura del `.jsonl`.
        for herramienta in herramientas:
            proyecto = self.proyecto_de(herramienta.sesion)
            if proyecto is None:
                cuenta["descartados"] += 1
                continue
            cuenta["herramientas"] += GastoDeHerramienta.objects.get_or_create(
                sesion=herramienta.sesion, identificador=herramienta.identificador,
                defaults={"proyecto": proyecto, "fecha": herramienta.fecha, "nombre": herramienta.nombre[:100],
                          "caracteres": herramienta.caracteres})[1]
        for archivo in archivos:
            proyecto = self.proyecto_de(archivo.sesion)
            if proyecto is None:
                cuenta["descartados"] += 1
                continue
            cuenta["archivos"] += GastoDeArchivo.objects.get_or_create(
                sesion=archivo.sesion, identificador=archivo.identificador,
                defaults={"proyecto": proyecto, "fecha": archivo.fecha, "ruta": archivo.ruta[:500],
                          "caracteres": archivo.caracteres})[1]
        return cuenta
