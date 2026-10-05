# -*- coding: utf-8 -*-
"""`EP-025·HU-005` · El nivel de cada regla en un proyecto, leído de MariaDB.

**Sin Django.** El freno corre antes y después de cada acción del agente;
arrancar Django tarda 2,4 segundos (análisis 1 del pendiente 116). Se lee con
PyMySQL: una conexión y una consulta que trae todos los niveles del proyecto.

**La conexión es la de Cimiento**: el `.env` de `proyectos/cimiento/`, con lo
que venga del ambiente por encima, igual que en los ajustes de Django.

**Sin fila, la regla frena.** Un proyecto que no está registrado, o que está
inactivo, tiene todas sus reglas en «frena»: lo que pasaba antes.

**Sin base no hay niveles**, y entonces el freno no deja modificar nada
(análisis 1 del pendiente 119, acuerdo 15). `BaseSinRespuesta` trae el mensaje
que se le da al agente.
"""
import os

APAGADA_SIN_SERVIDOR = {2002, 2003, 2005, 2006, 2013}
SIN_PERMISO = 1045
SIN_BASE = 1049
SIN_TABLA = 1146

_CONSULTA = ("SELECT n.regla, n.nivel FROM niveles_nivelderegla n "
             "JOIN proyectos_proyecto p ON p.id = n.proyecto_id "
             "WHERE p.activo = 1 AND LOWER(p.ruta) = LOWER(%s)")


class BaseSinRespuesta(Exception):
    """No se pudo leer la base de Cimiento. El mensaje dice qué hacer."""


class NivelesDelProyecto:
    """Los niveles de las reglas del proyecto en `raiz`."""

    def __init__(self, raiz, estandar=None, ajustes=None):
        self.raiz = os.path.abspath(raiz)
        self.estandar = estandar
        self._ajustes = ajustes
        self._niveles = None

    def ajustes(self):
        if self._ajustes is None:
            # Aquí y no arriba: el estándar se busca solo si hace falta.
            from config.ambiente import leer
            from ..comun import Proyecto

            estandar = self.estandar or Proyecto.estandar()
            archivo = leer(os.path.join(estandar, "proyectos", "cimiento", ".env"))

            def valor(clave, defecto):
                return os.environ.get(clave) or archivo.get(clave) or defecto

            self._ajustes = {"NAME": valor("DB_NOMBRE", "cimiento"), "USER": valor("DB_USUARIO", "root"),
                             "PASSWORD": valor("DB_CLAVE", ""), "HOST": valor("DB_SERVIDOR", "127.0.0.1"),
                             "PORT": valor("DB_PUERTO", "3307")}
        return self._ajustes

    def explicar(self, error):
        a = self.ajustes()
        donde = f"{a['HOST']}:{a['PORT']}"
        codigo = error.args[0] if error.args and isinstance(error.args[0], int) else None
        if codigo in APAGADA_SIN_SERVIDOR:
            return f"MariaDB no responde en {donde}: hay que prenderla"
        if codigo == SIN_PERMISO:
            return f"MariaDB no dejó entrar a «{a['USER']}» en {donde}: revisar DB_USUARIO y DB_CLAVE en el .env de Cimiento"
        if codigo in (SIN_BASE, SIN_TABLA):
            return f"la base «{a['NAME']}» en {donde} no está preparada: correr python manage.py preparar_base en proyectos/cimiento/"
        return f"MariaDB respondió en {donde} con el error {codigo}"

    def consultar(self, consulta):
        """Las filas de `consulta`, con la ruta del proyecto como único parámetro."""
        try:
            import pymysql
        except ImportError:
            raise BaseSinRespuesta("falta PyMySQL en el Python que corre los enganches: "
                                   "correr la instalación del estándar") from None
        a = self.ajustes()
        try:
            conexion = pymysql.connect(host=a["HOST"], port=int(a["PORT"]), user=a["USER"],
                                       password=a["PASSWORD"], database=a["NAME"],
                                       charset="utf8mb4", connect_timeout=2)
            try:
                with conexion.cursor() as cursor:
                    cursor.execute(consulta, [self.raiz])
                    return cursor.fetchall()
            finally:
                conexion.close()
        except pymysql.MySQLError as error:
            raise BaseSinRespuesta(self.explicar(error)) from None

    def todos(self):
        """`{regla: nivel}` de las reglas cambiadas en el proyecto. Una sola consulta."""
        if self._niveles is None:
            self._niveles = dict(self.consultar(_CONSULTA))
        return self._niveles


_LIMITES = ("SELECT limite_enganche, limite_archivo FROM proyectos_proyecto "
            "WHERE activo = 1 AND LOWER(ruta) = LOWER(%s)")


class LimitesDelProyecto(NivelesDelProyecto):
    """`EP-025·HU-009` · Desde cuántos tokens se avisa un enganche o un archivo.

    Misma conexión que los niveles. Sin registro o sin base se usan los de por
    defecto: el aviso es informativo y no debe callarse.
    """

    def limites(self):
        """`(por enganche, por archivo)`."""
        from ..proyectos.limites import LIMITE_ARCHIVO, LIMITE_ENGANCHE

        try:
            filas = self.consultar(_LIMITES)
        except BaseSinRespuesta:
            filas = ()
        return tuple(filas[0]) if filas else (LIMITE_ENGANCHE, LIMITE_ARCHIVO)
