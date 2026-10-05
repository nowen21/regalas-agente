# -*- coding: utf-8 -*-
"""`EP-025·HU-007` · Lo que gastó una llamada, leído del envío de telemetría.

Claude Code manda sus eventos con OpenTelemetry, en `POST /v1/logs`, como JSON
(OTLP/HTTP). Cada evento es un registro con atributos; el nombre va en
`event.name`. Los nombres de los atributos son los de la documentación de
Claude Code, verificados el 2026-10-05, y viven solo acá.

**Devuelve las mismas clases que el lector del `.jsonl`**, para que el
guardado sea uno solo. No usa Django.

**No se guarda texto**: de los parámetros de una herramienta solo sale la ruta
del archivo leído.
"""
import json
from datetime import datetime, timezone

from .lector import ArchivoLeido, Herramienta, Llamada

LLAMADA = "claude_code.api_request"
HERRAMIENTA = "claude_code.tool_result"
LECTURA = "Read"


def _valor(valor):
    """El valor de un atributo OTLP: `{"stringValue": "x"}`, `{"intValue": "3"}`…"""
    if not isinstance(valor, dict):
        return None
    for clave in ("stringValue", "intValue", "doubleValue", "boolValue"):
        if clave in valor:
            return valor[clave]
    return None


def _entero(texto):
    try:
        return int(float(texto))
    except (TypeError, ValueError):
        return 0


def _fecha(atributos, registro):
    texto = atributos.get("event.timestamp")
    if texto:
        try:
            return datetime.fromisoformat(str(texto).replace("Z", "+00:00"))
        except ValueError:
            pass
    nanos = _entero(registro.get("timeUnixNano") or registro.get("observedTimeUnixNano"))
    return datetime.fromtimestamp(nanos / 1e9, tz=timezone.utc) if nanos else None


def _ruta_leida(parametros):
    """`file_path` de los parámetros de `Read`, que llegan como texto JSON."""
    if isinstance(parametros, str):
        try:
            parametros = json.loads(parametros)
        except ValueError:
            return ""
    return str((parametros or {}).get("file_path") or "") if isinstance(parametros, dict) else ""


class EnvioInvalido(ValueError):
    """El cuerpo no es un envío OTLP JSON."""


class EventosDeTelemetria:
    """Las llamadas y los archivos leídos de un envío OTLP JSON."""

    def __init__(self, cuerpo):
        try:
            self.envio = json.loads(cuerpo)
        except (TypeError, ValueError) as error:
            raise EnvioInvalido(str(error))
        if not isinstance(self.envio, dict):
            raise EnvioInvalido("el envío no es un objeto")

    def registros(self):
        """`(atributos, registro)` de cada evento, con los del recurso debajo."""
        for recurso in self.envio.get("resourceLogs") or []:
            comunes = {a.get("key"): _valor(a.get("value"))
                       for a in (recurso.get("resource") or {}).get("attributes") or []}
            for alcance in recurso.get("scopeLogs") or []:
                for registro in alcance.get("logRecords") or []:
                    atributos = dict(comunes)
                    atributos.update({a.get("key"): _valor(a.get("value")) for a in registro.get("attributes") or []})
                    yield atributos, registro

    def leer(self):
        """`(llamadas, archivos)`. Lo que no se entiende se salta."""
        llamadas, archivos, self._herramientas = [], [], []
        for atributos, registro in self.registros():
            evento, sesion = atributos.get("event.name"), atributos.get("session.id")
            if not sesion:
                continue
            if evento == LLAMADA and atributos.get("request_id"):
                llamadas.append(Llamada(
                    sesion=sesion, mensaje=atributos["request_id"], fecha=_fecha(atributos, registro),
                    modelo=atributos.get("model") or "", entrada=_entero(atributos.get("input_tokens")),
                    cache_creada=_entero(atributos.get("cache_creation_tokens")),
                    cache_leida=_entero(atributos.get("cache_read_tokens")),
                    salida=_entero(atributos.get("output_tokens")), solicitud=atributos["request_id"],
                    pedido=atributos.get("prompt.id") or ""))
            elif evento == HERRAMIENTA and atributos.get("tool_use_id"):
                fecha, tamano = _fecha(atributos, registro), _entero(atributos.get("tool_result_size_bytes"))
                # `EP-025·HU-010` · Toda herramienta, con el tamaño de su resultado.
                self._herramientas.append(Herramienta(
                    sesion=sesion, identificador=atributos["tool_use_id"], fecha=fecha,
                    nombre=atributos.get("tool_name") or "", caracteres=tamano))
                if atributos.get("tool_name") == LECTURA:
                    archivos.append(ArchivoLeido(
                        sesion=sesion, identificador=atributos["tool_use_id"], fecha=fecha,
                        ruta=_ruta_leida(atributos.get("tool_parameters")), caracteres=tamano))
        return llamadas, archivos

    def herramientas(self):
        """Las herramientas del envío, después de `leer`."""
        return getattr(self, "_herramientas", [])
