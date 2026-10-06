# -*- coding: utf-8 -*-
"""`EP-025·HU-006` · Pone en la base lo que el lector sacó de un `.jsonl`.

**Sin duplicar.** Una llamada es única por sesión y mensaje: si vuelve, se
actualiza con su última línea. Enganches y archivos leídos son únicos por
sesión e identificador. Leer dos veces lo mismo deja la base igual.

**Un archivo sin cambios no se abre.** El avance guarda el tamaño y la fecha de
modificación; si siguen iguales, no hay nada nuevo. Si el archivo se achicó,
Claude Code lo reescribió: se lee desde el comienzo.

**Todo o nada por archivo**: lo guardado y el avance van en una transacción.

**Cada línea queda en la base, sin claves** (`EP-025·HU-025`): Claude Code
borra los `.jsonl` a los 30 días, así que el texto se trae en la misma
transacción que los conteos (análisis 1 del pendiente 124, acuerdo 5). Los
conteos salen de la línea original; la base guarda la tapada.

**La solicitud une la misma llamada** (`EP-025·HU-007`): la telemetría la
traía antes, con la solicitud como mensaje, y el `.jsonl` le pone su
`message.id`. La telemetría salió con la HU-012; lo que guardó se queda.
"""
import glob
import hashlib
import json
import os
from functools import lru_cache

from django.db import transaction

from core.enganches.enmascarar import Enmascarador
from core.proyectos.claude import proyectos_de_claude
from core.proyectos.models import Proyecto

from .lector import LectorDeClaudeCode
from .models import (AvanceDeLectura, EjecucionDeEnganche, GastoDeArchivo, GastoDeEnganche, GastoDeHerramienta,
                     LineaDeSesion, Llamada, Pedido)
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
        cuenta = {"llamadas": 0, "enganches": 0, "archivos": 0, "herramientas": 0, "lineas": 0, "leidos": 0}
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
            nuevo["lineas"] = self.guardar_lineas(ruta, lectura.crudas)
            avance.posicion, avance.tamano, avance.modificado = lectura.hasta, estado.st_size, estado.st_mtime
            avance.pedido = lectura.ultimo_pedido[:64]
            avance.save()
        return nuevo

    def nombre_de(self, ruta):
        """La ruta del `.jsonl` relativa a la carpeta de proyectos de Claude Code, con `/`."""
        try:
            return os.path.relpath(os.path.abspath(ruta), os.path.abspath(self.base)).replace(os.sep, "/")[:400]
        except ValueError:                  # otra unidad
            return os.path.basename(ruta)

    def guardar_lineas(self, ruta, crudas):
        """`EP-025·HU-025` · Cada línea con sus claves tapadas (`00·N6`). Cuántas nuevas.

        Única por archivo y huella: leerla otra vez no la duplica, y si Claude Code
        reescribe el archivo, la línea distinta en la misma posición también entra.
        """
        archivo = self.nombre_de(ruta)
        filas, vistas = [], set()
        for posicion, texto in crudas:
            huella = hashlib.sha1(texto.encode("utf-8")).hexdigest()
            if huella in vistas:
                continue
            vistas.add(huella)
            tapado, tapadas = Enmascarador.enmascarar(texto)
            filas.append(LineaDeSesion(proyecto=self.proyecto, archivo=archivo, huella=huella,
                                       posicion=posicion, texto=tapado, tapadas=tapadas))
        if not filas:
            return 0
        ya = set(LineaDeSesion.objects.filter(archivo=archivo, huella__in=[f.huella for f in filas])
                 .values_list("huella", flat=True))
        nuevas = [f for f in filas if f.huella not in ya]
        LineaDeSesion.objects.bulk_create(nuevas, batch_size=500)
        return len(nuevas)

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
                      "caracteres": h.caracteres, "orden": h.orden[:120]})[1] for h in lectura.herramientas)
        # `EP-025·HU-015` · Cada corrida de un enganche, le entregue o no algo al modelo.
        for e in lectura.ejecuciones:
            EjecucionDeEnganche.objects.get_or_create(
                sesion=e.sesion, identificador=e.identificador,
                defaults={"proyecto": self.proyecto, "fecha": e.fecha, "nombre": e.nombre[:200],
                          "evento": e.evento[:50]})
        enganches = sum(GastoDeEnganche.objects.get_or_create(
            sesion=e.sesion, identificador=e.identificador,
            defaults={"proyecto": self.proyecto, "fecha": e.fecha, "nombre": e.nombre[:200],
                      "evento": e.evento[:50], "caracteres": e.caracteres})[1] for e in lectura.enganches)
        # Si la telemetría lo trajo antes (hasta la HU-012), venía en bytes: el `.jsonl` lo deja en caracteres.
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
    """Guarda una llamada. `True` si es nueva. Si la telemetría ya la había guardado, la completa.
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
