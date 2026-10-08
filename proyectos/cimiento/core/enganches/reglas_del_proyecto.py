# -*- coding: utf-8 -*-
"""`EP-027·HU-006` · Las reglas propias de un proyecto, desde la base de Cimiento.

**Sin Django**, como la memoria: lo leen el arranque de la sesión y el freno, en
cada acción. Las reglas del proyecto viven en la tabla de reglas, marcadas con su
proyecto. Al abrir la sesión llega el índice; cada regla se lee entera con
`manage.py ver_regla`. Las de AgroSystem ocupan más de 100.000 caracteres y el
arranque tiene 10.000: por eso llega el índice, como llega el de la memoria.

Un proyecto sin reglas en la tabla, o sin base, devuelve nada: sigue con su
archivo `.agente/reglas-proyecto.md`, como antes.
"""
import os

from .niveles import BaseSinRespuesta, NivelesDelProyecto

_DEL_PROYECTO = ("FROM estandar_regla r JOIN proyectos_proyecto p ON p.id = r.proyecto_id "
                 "WHERE p.activo = 1 AND LOWER(p.ruta) = LOWER(%s) AND r.apartada = 0")
_INDICE = "SELECT r.codigo, r.titulo, r.grupo " + _DEL_PROYECTO + " ORDER BY r.orden, r.id"
_AUTORIZAN = ("SELECT r.codigo, r.autoriza_escribir " + _DEL_PROYECTO +
              " AND r.autoriza_escribir <> '' ORDER BY r.orden, r.id")


class ReglasDelProyecto:
    """Las reglas propias de `proyecto` que viven en la base. Todo es de lectura."""

    def __init__(self, proyecto, ajustes=None):
        self.proyecto = os.path.abspath(proyecto)
        self.ajustes = ajustes

    def _consultar(self, consulta):
        try:
            return NivelesDelProyecto(self.proyecto, ajustes=self.ajustes).consultar(consulta, [self.proyecto])
        except BaseSinRespuesta:
            return None

    def indice(self):
        """`[(código, título, grupo)]`, o `None` si no hay base."""
        filas = self._consultar(_INDICE)
        return None if filas is None else [tuple(f) for f in filas]

    def autorizan(self):
        """`[(código, texto de su línea «Autoriza escribir»)]`, o `None` si el proyecto
        no tiene reglas en la base. Una sola conexión para saberlo y para leerlas."""
        try:
            indice, autorizan = NivelesDelProyecto(self.proyecto, ajustes=self.ajustes).consultar_juntas(
                (_INDICE, [self.proyecto]), (_AUTORIZAN, [self.proyecto]))
        except BaseSinRespuesta:
            return None
        return [tuple(f) for f in autorizan] if indice else None

    def orden(self):
        from ..comun import Proyecto

        manage = os.path.join(Proyecto.estandar() or "", "proyectos", "cimiento", "manage.py").replace(os.sep, "/")
        return 'python "%s" ver_regla --proyecto "%s"' % (manage, self.proyecto.replace(os.sep, "/"))

    def contexto(self, tope=None):
        """El índice para el arranque, o `""` si el proyecto no tiene reglas en la base.
        Con `tope`, en caracteres, cabe siempre: van las filas que quepan."""
        indice = self.indice()
        if not indice:
            return ""
        orden = self.orden()
        cabeza = ("[REGLAS PROPIAS DEL PROYECTO — ÍNDICE, OBLIGATORIAS]\n"
                  "Solo valen en este proyecto y rigen junto al estándar. Viven en la base de "
                  "Cimiento. Antes de una tarea que toque una de ellas, leerla entera con "
                  f"`{orden} <código>`; todas juntas, con `{orden} --todas`. El índice dice de "
                  "qué trata cada una, no qué exige.\n\n")
        filas = ["  %s · %s%s" % (codigo, titulo, " (%s)" % grupo if grupo else "") for codigo, titulo, grupo in indice]
        entero = cabeza + "\n".join(filas)
        if tope is None or len(entero) <= tope:
            return entero
        for cuantas in range(len(filas) - 1, -1, -1):
            pie = f"Se listan {cuantas} de {len(filas)}; el resto, con el comando de arriba.\n\n"
            salida = cabeza + pie + "\n".join(filas[:cuantas])
            if len(salida) <= tope:
                return salida
        return ""
