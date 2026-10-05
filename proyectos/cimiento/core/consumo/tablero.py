# -*- coding: utf-8 -*-
"""`EP-025·HU-008` · Las sumas del tablero: el gasto de un período, por nivel.

**Suma la base, no Python.** Son miles de llamadas y el tablero se recarga
cada 10 segundos. La definición es la de `presupuesto.py`: la entrada cuenta
la caché creada.

**El día se arma en Python**, con la hora de Colombia: agruparlo en MariaDB
pide sus tablas de zonas horarias, que WAMP no trae.

**Enganches y archivos son estimación**: se guardan en caracteres
(`lector.CARACTERES_POR_TOKEN`).
"""
from collections import OrderedDict
from datetime import timedelta

from django.db.models import Count, F, Max, Min, Sum
from django.utils import timezone

from .lector import estimar_tokens
from .models import GastoDeArchivo, GastoDeEnganche, GastoDeHerramienta, Llamada, Pedido

PERIODOS = OrderedDict([(1, "Hoy"), (7, "7 días"), (30, "30 días")])
PERIODO_POR_DEFECTO = 7
CUANTOS = 10

_ENTRADA = F("entrada") + F("cache_creada")
_TOTAL = F("entrada") + F("cache_creada") + F("cache_leida") + F("salida")


def _sumas(consulta):
    return consulta.annotate(
        llamadas=Count("id"), entrada_total=Sum(_ENTRADA), salida_total=Sum("salida"),
        cache_total=Sum("cache_leida"), total=Sum(_TOTAL))


class GastoDelPeriodo:
    """El gasto desde el comienzo del período, de todos los proyectos o de uno."""

    def __init__(self, dias=PERIODO_POR_DEFECTO, proyecto=None, ahora=None):
        self.dias = dias if dias in PERIODOS else PERIODO_POR_DEFECTO
        self.proyecto = proyecto
        ahora = timezone.localtime(ahora or timezone.now())
        hoy = ahora.replace(hour=0, minute=0, second=0, microsecond=0)
        self.desde = hoy - timedelta(days=self.dias - 1)

    def _filtrar(self, modelo):
        consulta = modelo.objects.filter(fecha__gte=self.desde)
        return consulta.filter(proyecto=self.proyecto) if self.proyecto else consulta

    def llamadas(self):
        return self._filtrar(Llamada)

    def totales(self):
        # Los nombres no pueden ser los de los campos: Django los confunde.
        datos = self.llamadas().aggregate(
            n_llamadas=Count("id"), n_entrada=Sum(_ENTRADA), n_salida=Sum("salida"),
            n_cache=Sum("cache_leida"), n_total=Sum(_TOTAL))
        return {clave.removeprefix("n_"): valor or 0 for clave, valor in datos.items()}

    def por_proyecto(self):
        return list(_sumas(self.llamadas().values("proyecto__id", "proyecto__nombre")).order_by("-total"))

    def por_dia(self):
        """`[(fecha, total)]`, un día por fila, también los que no tuvieron gasto."""
        dias = OrderedDict(((self.desde + timedelta(days=n)).date(), 0) for n in range(self.dias))
        for fecha, entrada, creada, leida, salida in self.llamadas().values_list(
                "fecha", "entrada", "cache_creada", "cache_leida", "salida").iterator():
            dia = timezone.localtime(fecha).date()
            if dia in dias:
                dias[dia] += entrada + creada + leida + salida
        return list(dias.items())

    def por_sesion(self):
        consulta = self.llamadas().values("sesion", "proyecto__nombre")
        return list(_sumas(consulta).annotate(inicio=Min("fecha"), fin=Max("fecha")).order_by("-fin")[:CUANTOS])

    def _estimados(self, modelo, campo):
        filas = self._filtrar(modelo).values(campo).annotate(
            veces=Count("id"), caracteres=Sum("caracteres")).order_by("-caracteres")[:CUANTOS]
        return [{"nombre": fila[campo] or "(sin nombre)", "veces": fila["veces"],
                 "tokens": estimar_tokens(fila["caracteres"] or 0)} for fila in filas]

    def por_enganche(self):
        return self._estimados(GastoDeEnganche, "nombre")

    def por_archivo(self):
        return self._estimados(GastoDeArchivo, "ruta")

    # ── `EP-025·HU-010` · La segunda tanda ─────────────────────────────────

    def _por(self, campo, vacio, consulta=None):
        """Llamadas agrupadas por `campo`, con `vacio` donde no hay valor."""
        filas = _sumas((consulta if consulta is not None else self.llamadas()).values(campo)).order_by("-total")
        return [dict(fila, nombre=fila[campo] or vacio) for fila in filas[:CUANTOS]]

    def por_palabra(self):
        return self._por("pedido__palabra", "(sin palabra clave)",
                         self.llamadas().filter(pedido__isnull=False))

    def por_trabajo(self):
        return self._por("pedido__trabajo", "(sin trabajo)", self.llamadas().filter(pedido__isnull=False))

    def por_agente(self):
        return self._por("agente", "auxiliar", self.llamadas().filter(auxiliar=True))

    def por_modelo(self):
        return self._por("modelo", "(sin modelo)")

    def por_tipo_de_token(self):
        datos = self.llamadas().aggregate(n_entrada=Sum("entrada"), n_creada=Sum("cache_creada"),
                                          n_leida=Sum("cache_leida"), n_salida=Sum("salida"))
        nombres = {"n_entrada": "Entrada nueva", "n_creada": "Escrita en caché", "n_leida": "Releída de caché",
                   "n_salida": "Salida"}
        return [{"nombre": nombres[clave], "total": valor or 0} for clave, valor in datos.items()]

    def por_herramienta(self):
        return self._estimados(GastoDeHerramienta, "nombre")

    def contexto(self):
        """Lo que entró al contexto por enganches, archivos y otras herramientas (estimado),
        y el contexto más grande que alcanzó una llamada (contado)."""
        def estimado(consulta):
            return estimar_tokens(consulta.aggregate(c=Sum("caracteres"))["c"] or 0)

        return {
            "enganches": estimado(self._filtrar(GastoDeEnganche)),
            "archivos": estimado(self._filtrar(GastoDeArchivo)),
            "otras": estimado(self._filtrar(GastoDeHerramienta).exclude(nombre="Read")),
            "maximo": self.llamadas().aggregate(m=Max(F("entrada") + F("cache_creada") + F("cache_leida")))["m"] or 0,
        }

    def ultimos_mensajes(self):
        consulta = Pedido.objects.filter(fecha__gte=self.desde)
        if self.proyecto:
            consulta = consulta.filter(proyecto=self.proyecto)
        return list(consulta.annotate(n_llamadas=Count("llamadas"), total=Sum(
            F("llamadas__entrada") + F("llamadas__cache_creada") + F("llamadas__cache_leida")
            + F("llamadas__salida"))).values("fecha", "palabra", "trabajo", "proyecto__nombre", "n_llamadas", "total")
            .order_by("-fecha")[:CUANTOS])

    def todo(self):
        """Lo que muestra el tablero, sumado una vez. `graficas` va a `json_script`."""
        proyectos, dias = self.por_proyecto(), self.por_dia()
        return {
            "totales": self.totales(), "proyectos": proyectos, "sesiones": self.por_sesion(),
            "enganches": self.por_enganche(), "archivos": self.por_archivo(),
            "niveles": [("Por palabra clave", self.por_palabra()), ("Por trabajo", self.por_trabajo()),
                        ("Por modelo", self.por_modelo()), ("Por agente auxiliar", self.por_agente())],
            "tipos": self.por_tipo_de_token(), "herramientas": self.por_herramienta(),
            "contexto": self.contexto(), "mensajes": self.ultimos_mensajes(),
            "graficas": {
                "proyectos": {"nombres": [p["proyecto__nombre"] for p in proyectos],
                              "totales": [p["total"] or 0 for p in proyectos]},
                "dias": {"fechas": [dia.strftime("%d/%m") for dia, _ in dias],
                         "totales": [total for _, total in dias]},
            },
        }
