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

**Lo suspendido queda «apagada» mientras dure** (`EP-025·HU-013`): la regla
suspendida con su ID, y el freno entero con `*`. El núcleo sigue en «frena»: lo
decide `Freno.nivel_para`.
"""
import os

APAGADA_SIN_SERVIDOR = {2002, 2003, 2005, 2006, 2013}
SIN_PERMISO = 1045
SIN_BASE = 1049
SIN_TABLA = 1146

_CONSULTA = ("SELECT n.regla, n.nivel FROM niveles_nivelderegla n "
             "JOIN proyectos_proyecto p ON p.id = n.proyecto_id "
             "WHERE p.activo = 1 AND LOWER(p.ruta) = LOWER(%s)")

# `EP-025·HU-013` · Las suspensiones vigentes, en la misma lectura que los niveles.
_SUSPENDIDAS = ("SELECT s.tipo, s.nombre FROM proyectos_suspension s "
                "JOIN proyectos_proyecto p ON p.id = s.proyecto_id "
                "WHERE p.activo = 1 AND LOWER(p.ruta) = LOWER(%s) "
                "AND s.levantada IS NULL AND s.vence > UTC_TIMESTAMP()")
TODAS = "*"


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

    def consultar(self, consulta, parametros=None):
        """Las filas de `consulta`. Sin `parametros`, la ruta del proyecto es el único."""
        return self.consultar_juntas((consulta, parametros))[0]

    def consultar_juntas(self, *consultas):
        """Las filas de cada `(consulta, parámetros)`, en una sola conexión."""
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
                salida = []
                with conexion.cursor() as cursor:
                    for consulta, parametros in consultas:
                        cursor.execute(consulta, [self.raiz] if parametros is None else parametros)
                        salida.append(cursor.fetchall())
                return salida
            finally:
                conexion.close()
        except pymysql.MySQLError as error:
            raise BaseSinRespuesta(self.explicar(error)) from None

    def todos(self):
        """`{regla: nivel}` de las reglas cambiadas en el proyecto, con lo suspendido en «apagada»."""
        if self._niveles is None:
            filas, suspendidas = self.consultar_juntas((_CONSULTA, None), (_SUSPENDIDAS, None))
            niveles = dict(filas)
            for tipo, nombre in suspendidas:
                # `EP-025·HU-032` · Desde que se suspende cualquier momento, solo «freno» apaga el freno entero.
                if tipo == "enganche" and nombre != "freno":
                    continue
                niveles[TODAS if tipo == "enganche" else nombre] = "apagada"
            self._niveles = niveles
        return self._niveles


class LimitesDelProyecto(NivelesDelProyecto):
    """`EP-025·HU-009` · Desde cuántos tokens se avisa un enganche o un archivo.

    Desde la `EP-025·HU-013` son ajustes: el del proyecto, si no el de la base
    de Cimiento, si no el de fábrica. Sin registro o sin base, el de fábrica: el
    aviso es informativo y no debe callarse.
    """

    def limites(self):
        """`(por enganche, por archivo)`."""
        from .configuracion import ConfiguracionDelProyecto
        configuracion = ConfiguracionDelProyecto(self.raiz, self.estandar, self._ajustes)
        return configuracion.valor("limite_enganche"), configuracion.valor("limite_archivo")
