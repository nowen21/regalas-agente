# -*- coding: utf-8 -*-
"""La base de Cimiento: dónde está, si responde y cómo se crea.

**Se conecta sin nombre de base** para poder crearla: con el nombre puesto,
MariaDB rechaza la conexión justo cuando la base es lo que falta.

**El error se traduce a qué hacer.** El que trae el controlador habla de
sockets y códigos; quien abre Cimiento necesita saber si tiene que prender
MariaDB, revisar el `.env` o crear la base.
"""
from django.conf import settings

# Los códigos de MariaDB que dicen que el servidor no está escuchando.
APAGADA = {2002, 2003, 2005, 2006, 2013}
SIN_PERMISO = 1045
SIN_BASE = 1049


class BaseInalcanzable(Exception):
    """MariaDB no se pudo usar. El mensaje ya dice qué hacer."""


class BaseDeDatos:
    """La conexión `default` de los ajustes, vista desde MariaDB."""

    def __init__(self, ajustes=None):
        self.ajustes = ajustes or settings.DATABASES["default"]

    @property
    def nombre(self):
        return self.ajustes["NAME"]

    @property
    def donde(self):
        return f"{self.ajustes['HOST']}:{self.ajustes['PORT']}"

    def explicar(self, error):
        """Lo que hay que hacer, según el código del error de MariaDB."""
        codigo = error.args[0] if error.args and isinstance(error.args[0], int) else None
        if codigo in APAGADA:
            return (f"MariaDB no responde en {self.donde}. Hay que prenderla "
                    f"y volver a intentar.")
        if codigo == SIN_PERMISO:
            return (f"MariaDB respondió en {self.donde} pero no dejó entrar a "
                    f"«{self.ajustes['USER']}». Revisar DB_USUARIO y DB_CLAVE en el .env.")
        if codigo == SIN_BASE:
            return (f"La base «{self.nombre}» no existe en {self.donde}. "
                    f"Crearla con: python manage.py preparar_base")
        return f"MariaDB respondió en {self.donde} con el error {codigo}."

    def _conectar(self):
        # Aquí y no arriba: quien solo lee el nombre o el servidor no necesita
        # el controlador instalado.
        import MySQLdb

        try:
            return MySQLdb.connect(
                host=self.ajustes["HOST"], port=int(self.ajustes["PORT"]),
                user=self.ajustes["USER"], passwd=self.ajustes["PASSWORD"],
                charset="utf8mb4", connect_timeout=3)
        except MySQLdb.OperationalError as error:
            raise BaseInalcanzable(self.explicar(error)) from None

    def crear_si_falta(self):
        """Crea la base si no está. Devuelve si la creó."""
        conexion = self._conectar()
        try:
            cursor = conexion.cursor()
            cursor.execute("SHOW DATABASES LIKE %s", [self.nombre])
            if cursor.fetchone():
                return False
            # El nombre no admite parámetro; viene de los ajustes, no del usuario.
            cursor.execute(f"CREATE DATABASE `{self.nombre}` "
                           f"CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            return True
        finally:
            conexion.close()

    def pasar_a_innodb(self):
        """Pasa a InnoDB las tablas que estén en otro motor. Devuelve cuáles.

        Las que se crearon con MyISAM (el motor por defecto del MariaDB de
        WAMP) no tienen transacciones: una escritura a medias queda a medias.
        """
        conexion = self._conectar()
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT TABLE_NAME FROM information_schema.TABLES "
                           "WHERE TABLE_SCHEMA = %s AND TABLE_TYPE = 'BASE TABLE' "
                           "AND ENGINE <> 'InnoDB'", [self.nombre])
            tablas = [fila[0] for fila in cursor.fetchall()]
            for tabla in tablas:
                cursor.execute(f"ALTER TABLE `{self.nombre}`.`{tabla}` ENGINE=InnoDB")
            return tablas
        finally:
            conexion.close()

    @staticmethod
    def version(conexion):
        """«11.4.9», sin lo que MariaDB le pega detrás."""
        with conexion.cursor() as cursor:
            cursor.execute("SELECT VERSION()")
            completa = cursor.fetchone()[0]
        return completa.split("-")[0]
