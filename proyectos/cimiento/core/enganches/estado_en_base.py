# -*- coding: utf-8 -*-
"""`EP-025·HU-023` · El estado del análisis prendido, en la base de Cimiento.

**Sin Django**, como los niveles: lo leen los enganches en cada mensaje y el
freno en cada acción. Usa la conexión de `NivelesDelProyecto`.

**Solo un proyecto registrado y activo** tiene fila: el que no lo está sigue con
su archivo, y lo decide `AnalisisEnCurso`. Así una carpeta temporal de una
prueba nunca escribe en la base real.
"""
import json

from .niveles import BaseSinRespuesta, NivelesDelProyecto

_PROYECTO = "SELECT id FROM proyectos_proyecto WHERE activo = 1 AND LOWER(ruta) = LOWER(%s)"
_COLUMNAS = "sesion, analisis, desde, pausa, pausas"
_TABLA = "proyectos_analisisprendido"


class EstadoEnBase(NivelesDelProyecto):
    """Las filas de `proyectos_analisisprendido` de un proyecto, una por sesión."""

    def __init__(self, raiz, estandar=None, ajustes=None):
        super().__init__(raiz, estandar, ajustes)
        self._id = None

    def ejecutar(self, consulta, parametros, escribir=False):
        """Las filas de `consulta`. Con `escribir`, confirma el cambio."""
        try:
            import pymysql
        except ImportError:
            raise BaseSinRespuesta("falta PyMySQL en el Python que corre los enganches") from None
        a = self.ajustes()
        try:
            conexion = pymysql.connect(host=a["HOST"], port=int(a["PORT"]), user=a["USER"],
                                       password=a["PASSWORD"], database=a["NAME"],
                                       charset="utf8mb4", connect_timeout=2)
            try:
                with conexion.cursor() as cursor:
                    cursor.execute(consulta, parametros)
                    filas = cursor.fetchall()
                if escribir:
                    conexion.commit()
                return filas
            finally:
                conexion.close()
        except pymysql.MySQLError as error:
            raise BaseSinRespuesta(self.explicar(error)) from None

    def proyecto_id(self):
        """El id del proyecto registrado y activo en `raiz`, o None."""
        if self._id is None:
            filas = self.ejecutar(_PROYECTO, [self.raiz])
            self._id = filas[0][0] if filas else 0
        return self._id or None

    @staticmethod
    def _dato(fila):
        sesion, analisis, desde, pausa, pausas = fila
        return {"sesion": sesion, "analisis": analisis, "desde": int(desde),
                "pausa": int(pausa) if pausa else None, "pausas": pausas or ""}

    def leer(self, sesion):
        filas = self.ejecutar("SELECT %s FROM %s WHERE proyecto_id = %%s AND sesion = %%s" % (_COLUMNAS, _TABLA),
                              [self.proyecto_id(), sesion])
        return self._dato(filas[0]) if filas else None

    def mas_reciente(self):
        """La fila que se cambió último: lo que leía el archivo único sin sesión."""
        filas = self.ejecutar("SELECT %s FROM %s WHERE proyecto_id = %%s ORDER BY actualizado DESC, id DESC LIMIT 1"
                              % (_COLUMNAS, _TABLA), [self.proyecto_id()])
        return self._dato(filas[0]) if filas else None

    def filas(self):
        filas = self.ejecutar("SELECT %s FROM %s WHERE proyecto_id = %%s ORDER BY sesion" % (_COLUMNAS, _TABLA),
                              [self.proyecto_id()])
        return [self._dato(f) for f in filas]

    # ── `EP-026·HU-001` · lo que se escribe acá también queda en la historia ──

    def _fila(self, sesion):
        filas = self.ejecutar("SELECT id, analisis, desde, pausa, pausas FROM %s WHERE proyecto_id = %%s AND sesion = %%s"
                              % _TABLA, [self.proyecto_id(), sesion])
        if not filas:
            return None, None
        id_, analisis, desde, pausa, pausas = filas[0]
        return id_, {"sesion": sesion, "analisis": analisis, "desde": int(desde),
                     "pausa": int(pausa) if pausa is not None else None, "pausas": pausas or ""}

    def _anotar(self, fila, accion, antes, despues):
        """Escribe el cambio en `historia_cambio`, a nombre del agente. Sin la tabla
        (Cimiento sin migrar) no se anota: el estado del análisis no se puede caer."""
        if accion == "cambiar":
            cambiados = sorted(k for k in despues if despues[k] != antes.get(k))
            if not cambiados:
                return
            antes = {k: antes.get(k) for k in cambiados}
            despues = {k: despues[k] for k in cambiados}
        try:
            self.ejecutar(
                "INSERT INTO historia_cambio (fecha, quien, tabla, fila, accion, antes, despues, motivo) "
                "VALUES (UTC_TIMESTAMP(6), 'agente', 'proyectos.analisisprendido', %s, %s, %s, %s, '')",
                [str(fila), accion, json.dumps(antes) if antes is not None else None,
                 json.dumps(despues) if despues is not None else None], escribir=True)
        except BaseSinRespuesta:
            pass

    def guardar(self, dato):
        """Escribe la fila de `dato["sesion"]`: la crea o la cambia, y anota el cambio."""
        _, antes = self._fila(dato["sesion"])
        self._escribir(dato)
        id_, despues = self._fila(dato["sesion"])
        if id_ is not None:
            self._anotar(id_, "cambiar" if antes else "crear", antes, despues)

    def _escribir(self, dato):
        self.ejecutar(
            "INSERT INTO %s (proyecto_id, sesion, analisis, desde, pausa, pausas, actualizado) "
            "VALUES (%%s, %%s, %%s, %%s, %%s, %%s, UTC_TIMESTAMP(6)) ON DUPLICATE KEY UPDATE "
            "analisis = VALUES(analisis), desde = VALUES(desde), pausa = VALUES(pausa), "
            "pausas = VALUES(pausas), actualizado = VALUES(actualizado)" % _TABLA,
            [self.proyecto_id(), dato["sesion"], dato["analisis"], dato["desde"], dato.get("pausa"),
             dato.get("pausas") or ""], escribir=True)

    def borrar(self, sesion):
        id_, antes = self._fila(sesion)
        self.ejecutar("DELETE FROM %s WHERE proyecto_id = %%s AND sesion = %%s" % _TABLA,
                      [self.proyecto_id(), sesion], escribir=True)
        if id_ is not None:
            self._anotar(id_, "borrar", antes, None)
