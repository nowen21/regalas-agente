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

from django.db.models import Avg, Count, F, Max, Min, Sum
from django.utils import timezone

from core.proyectos import ajustes
from core.proyectos.models import AjusteBase

from .lector import estimar_tokens
from .models import EjecucionDeEnganche, GastoDeArchivo, GastoDeEnganche, GastoDeHerramienta, Llamada, Pedido

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
        self.ahora = ahora

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
            "sin_tokens": self.sin_tokens(), "candidatos": self.candidatos(),
            "graficas": {
                "proyectos": {"nombres": [p["proyecto__nombre"] for p in proyectos],
                              "totales": [p["total"] or 0 for p in proyectos]},
                "dias": {"fechas": [dia.strftime("%d/%m") for dia, _ in dias],
                         "totales": [total for _, total in dias]},
            },
        }

    # ── `EP-025·HU-015` · Lo que corre sin tokens, y lo que conviene automatizar ──

    REPETIDO = 3            # veces desde las que un archivo o un comando es candidato
    EN_CADA_MENSAJE = 0.8   # parte de los mensajes del período en que un enganche agrega contexto

    def sin_tokens(self):
        """Cada enganche con cuántas veces corrió y cuántos tokens agregó: también el que no agrega."""
        agregados = {fila["nombre"]: estimar_tokens(fila["c"] or 0) for fila in
                     self._filtrar(GastoDeEnganche).values("nombre").annotate(c=Sum("caracteres"))}
        filas = self._filtrar(EjecucionDeEnganche).values("nombre").annotate(veces=Count("id")).order_by("-veces")
        return [{"nombre": f["nombre"] or "(sin nombre)", "veces": f["veces"], "tokens": agregados.get(f["nombre"], 0)}
                for f in filas[:CUANTOS * 2]]

    def candidatos(self):
        """Lo que se repite, con los tokens que se ahorrarían si un programa lo hiciera."""
        def repetidos(modelo, campo, consulta=None):
            filas = (consulta if consulta is not None else self._filtrar(modelo)).values(campo)
            return filas.annotate(veces=Count("id"), c=Sum("caracteres")).filter(veces__gte=self.REPETIDO)

        def todas_menos_una(fila):
            return estimar_tokens(fila["c"] or 0) * (fila["veces"] - 1) // fila["veces"]

        # `EP-025·HU-026` · `gasto`: lo que cuesta hoy; `ahorro`, lo que dejaría de costar.
        salida = [{"tipo": "Archivo leído", "nombre": fila["ruta"], "veces": fila["veces"],
                   "gasto": estimar_tokens(fila["c"] or 0), "ahorro": todas_menos_una(fila)}
                  for fila in repetidos(GastoDeArchivo, "ruta")]
        mensajes = self._filtrar(Pedido).count()
        if mensajes:
            enganches = self._filtrar(GastoDeEnganche).filter(evento="UserPromptSubmit").values("nombre")
            for fila in enganches.annotate(veces=Count("id"), c=Sum("caracteres")):
                if fila["veces"] >= self.EN_CADA_MENSAJE * mensajes:
                    salida.append({"tipo": "Enganche en cada mensaje", "nombre": fila["nombre"],
                                   "veces": fila["veces"], "gasto": estimar_tokens(fila["c"] or 0),
                                   "ahorro": estimar_tokens(fila["c"] or 0)})
        comandos = self._filtrar(GastoDeHerramienta).exclude(orden="")
        salida += [{"tipo": "Comando repetido", "nombre": fila["orden"], "veces": fila["veces"],
                    "gasto": estimar_tokens(fila["c"] or 0), "ahorro": todas_menos_una(fila)}
                   for fila in repetidos(GastoDeHerramienta, "orden", comandos)]
        return sorted(salida, key=lambda f: -f["ahorro"])[:CUANTOS * 2]

    # ── `EP-025·HU-026` · La franja y las cinco pestañas ──────────────────

    AGRUPAR = OrderedDict([
        ("proyecto", ("Proyecto", "proyecto__nombre", {}, "(sin proyecto)")),
        ("palabra", ("Palabra clave", "pedido__palabra", {"pedido__isnull": False}, "(sin palabra clave)")),
        ("trabajo", ("Trabajo", "pedido__trabajo", {"pedido__isnull": False}, "(sin trabajo)")),
        ("modelo", ("Modelo", "modelo", {}, "(sin modelo)")),
        ("agente", ("Agente auxiliar", "agente", {"auxiliar": True}, "auxiliar")),
    ])

    def anterior(self):
        """El gasto del tramo anterior, cortado a la misma hora (análisis 1 del pendiente 124, acuerdo 2)."""
        consulta = Llamada.objects.filter(fecha__gte=self.desde - timedelta(days=self.dias),
                                          fecha__lt=self.ahora - timedelta(days=self.dias))
        if self.proyecto:
            consulta = consulta.filter(proyecto=self.proyecto)
        return consulta.aggregate(n=Sum(_TOTAL))["n"] or 0

    def franja(self):
        """Lo que va siempre arriba: total, variación, llamadas, % de caché releída y contexto máximo."""
        totales = self.totales()
        anterior = self.anterior()
        total = totales["total"]
        return {
            "total": total, "anterior": anterior, "llamadas": totales["llamadas"],
            "variacion": round((total - anterior) * 100 / anterior) if anterior else None,
            "cache_pct": round(totales["cache"] * 100 / total) if total else 0,
            "maximo": self.llamadas().aggregate(
                m=Max(F("entrada") + F("cache_creada") + F("cache_leida")))["m"] or 0,
        }

    def por_dia_por_tipo(self):
        """`{"fechas", "entrada", "creada", "leida", "salida"}`, un día por posición."""
        dias = OrderedDict(((self.desde + timedelta(days=n)).date(), [0, 0, 0, 0]) for n in range(self.dias))
        for fecha, entrada, creada, leida, salida in self.llamadas().values_list(
                "fecha", "entrada", "cache_creada", "cache_leida", "salida").iterator():
            dia = timezone.localtime(fecha).date()
            if dia in dias:
                for i, valor in enumerate((entrada, creada, leida, salida)):
                    dias[dia][i] += valor
        series = list(zip(*dias.values()))
        return {"fechas": [d.strftime("%d/%m") for d in dias], "entrada": list(series[0]),
                "creada": list(series[1]), "leida": list(series[2]), "salida": list(series[3])}

    def agrupar(self, por="proyecto", cuantos=CUANTOS):
        """`(por, filas)`: el gasto agrupado, con su porcentaje del total. Un `por` que no existe es «proyecto»."""
        por = por if por in self.AGRUPAR else "proyecto"
        _, campo, filtro, vacio = self.AGRUPAR[por]
        filas = list(_sumas(self.llamadas().filter(**filtro).values(campo)).order_by("-total")[:cuantos])
        total = self.totales()["total"] or 1
        return por, [dict(f, nombre=f[campo] or vacio, pct=round((f["total"] or 0) * 100 / total)) for f in filas]

    def limites(self):
        """`(por enganche, por archivo)`: los del proyecto filtrado, o los comunes de Cimiento."""
        if self.proyecto:
            return int(self.proyecto.ajuste("limite_enganche")), int(self.proyecto.ajuste("limite_archivo"))
        efectivos = ajustes.efectivos(dict(AjusteBase.objects.values_list("clave", "valor")))
        return int(efectivos["limite_enganche"][0]), int(efectivos["limite_archivo"][0])

    def _por_vez(self, modelo, campo):
        filas = self._filtrar(modelo).values(campo).annotate(
            veces=Count("id"), c=Sum("caracteres"), prom=Avg("caracteres"), mayor=Max("caracteres")
        ).order_by("-c")[:CUANTOS]
        return [{"nombre": f[campo] or "(sin nombre)", "veces": f["veces"], "tokens": estimar_tokens(f["c"] or 0),
                 "promedio": estimar_tokens(int(f["prom"] or 0)), "maximo": estimar_tokens(f["mayor"] or 0)}
                for f in filas]

    def contexto_por_vez(self):
        """Enganches y archivos con su promedio y su máximo por vez, junto al límite; no se marca nada
        (análisis 1 del pendiente 124, acuerdo 3)."""
        limite_enganche, limite_archivo = self.limites()
        return {"resumen": self.contexto(), "enganches": self._por_vez(GastoDeEnganche, "nombre"),
                "archivos": self._por_vez(GastoDeArchivo, "ruta"), "herramientas": self.por_herramienta(),
                "limite_enganche": limite_enganche, "limite_archivo": limite_archivo}

    def ahorro(self):
        """Lo que no gasta, lo que gasta y lo que gasta y se puede automatizar."""
        corridas = self.sin_tokens()
        candidatos = self.candidatos()
        return {"no_gasta": [f for f in corridas if not f["tokens"]], "gasta": [f for f in corridas if f["tokens"]],
                "candidatos": candidatos, "ahorro_total": sum(f["ahorro"] for f in candidatos)}

    PESTANAS = ("resumen", "donde", "contexto", "ahorro", "actividad")

    def pestana(self, nombre, agrupar_por="proyecto"):
        """Lo que necesita cada pestaña, y solo eso (RNF-01). Un nombre que no existe da `KeyError`."""
        if nombre == "resumen":
            ahorro = self.ahorro()
            por, filas = self.agrupar("palabra" if self.proyecto else "proyecto", cuantos=5)
            # `datos_graficas` va a `json_script`: lo dibuja ApexCharts.
            return {"datos_graficas": {"dias": self.por_dia_por_tipo(), "tipos": self.por_tipo_de_token()},
                    "candidatos": ahorro["candidatos"][:5], "ahorro_total": ahorro["ahorro_total"],
                    "agrupado_por": self.AGRUPAR[por][0], "donde": filas}
        if nombre == "donde":
            por, filas = self.agrupar(agrupar_por)
            return {"por": por, "opciones": [(k, v[0]) for k, v in self.AGRUPAR.items()], "filas": filas}
        if nombre == "contexto":
            return self.contexto_por_vez()
        if nombre == "ahorro":
            return self.ahorro()
        if nombre == "actividad":
            return {"sesiones": self.por_sesion(), "mensajes": self.ultimos_mensajes()}
        raise KeyError(nombre)
