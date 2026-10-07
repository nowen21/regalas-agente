# -*- coding: utf-8 -*-
"""`EP-026·HU-010` · La copia diaria de la base de Cimiento.

**Dónde** (análisis 1 del pendiente 132, acuerdos 23 y 24): en `cimiento-copias`,
la carpeta hermana de la del estándar. Es la única ruta fuera del proyecto donde
esto escribe, y no se puede cambiar: así quedó autorizada.

**Cuántas** (acuerdo 25): las últimas 7. La última ya trae toda la historia; las
anteriores sirven si la base se daña sin que nadie lo note.

**Sin Django y sin `mysqldump`**: la escribe Python con PyMySQL, con la misma
conexión de los enganches, para que el inicio de sesión la pueda lanzar sin
saber dónde está instalado MariaDB.

**Sin claves** (`00·N6`): las sesiones del navegador van sin filas, porque su
llave deja entrar sin contraseña. El gasto ya entra tapado a la base.

**Comprimida con gzip**: sin comprimir pesa unos 440 MB por el gasto de tokens,
y siete copias pasarían de 3 GB.

**Una sentencia por línea**: el `CREATE TABLE` se pone en una sola línea y los
valores salen escapados por PyMySQL, que convierte los saltos de línea en `\\n`.
Por eso restaurar es leer línea por línea.
"""
import datetime
import gzip
import json
import os
import re
import subprocess
import sys

CARPETA = "cimiento-copias"
PREFIJO = "cimiento-"
GUARDAR = 7
SIN_FILAS = {"django_session"}
ESTADO = "estado.json"
POR_LOTE = 200
EXTENSION = ".sql.gz"
_NOMBRE = re.compile(r"^cimiento-(\d{4}-\d{2}-\d{2})\.sql\.gz$")


def carpeta(estandar=None):
    """`<padre del estándar>/cimiento-copias`."""
    from core.comun import Proyecto

    raiz = os.path.abspath(estandar or Proyecto.estandar())
    return os.path.join(os.path.dirname(raiz), CARPETA)


def _conectar(ajustes, base=None):
    import pymysql

    return pymysql.connect(host=ajustes["HOST"], port=int(ajustes["PORT"]), user=ajustes["USER"],
                           password=ajustes["PASSWORD"], database=base if base is not None else ajustes["NAME"],
                           charset="utf8mb4", connect_timeout=5)


def _ajustes(estandar=None):
    from core.enganches.niveles import NivelesDelProyecto

    return NivelesDelProyecto(estandar or ".", estandar=estandar).ajustes()


def copiar(destino, ajustes=None, hoy=None, estandar=None):
    """Escribe `cimiento-<hoy>.sql.gz` en `destino` y deja las últimas 7. Devuelve la ruta."""
    ajustes = ajustes or _ajustes(estandar)
    hoy = hoy or datetime.date.today()
    os.makedirs(destino, exist_ok=True)
    ruta = os.path.join(destino, "%s%s%s" % (PREFIJO, hoy.isoformat(), EXTENSION))
    temporal = ruta + ".parcial"
    conexion = _conectar(ajustes)
    try:
        with conexion.cursor() as cursor, gzip.open(temporal, "wt", encoding="utf-8", newline="\n") as f:
            f.write("-- Copia de la base «%s» del %s (EP-026·HU-010)\n" % (ajustes["NAME"], hoy.isoformat()))
            f.write("SET FOREIGN_KEY_CHECKS=0;\n")
            cursor.execute("SHOW FULL TABLES WHERE Table_type = 'BASE TABLE'")
            for (tabla, _tipo) in cursor.fetchall():
                cursor.execute("SHOW CREATE TABLE `%s`" % tabla)
                crear = " ".join(cursor.fetchone()[1].split())
                f.write("DROP TABLE IF EXISTS `%s`;\n%s;\n" % (tabla, crear))
                if tabla in SIN_FILAS:
                    continue
                cursor.execute("SELECT * FROM `%s`" % tabla)
                lote = []
                for fila in cursor.fetchall():
                    lote.append("(" + ", ".join(conexion.escape(v) for v in fila) + ")")
                    if len(lote) == POR_LOTE:
                        f.write("INSERT INTO `%s` VALUES %s;\n" % (tabla, ", ".join(lote)))
                        lote = []
                if lote:
                    f.write("INSERT INTO `%s` VALUES %s;\n" % (tabla, ", ".join(lote)))
            f.write("SET FOREIGN_KEY_CHECKS=1;\n")
    finally:
        conexion.close()
    os.replace(temporal, ruta)
    podar(destino)
    return ruta


def copias(destino):
    """Las copias de `destino`, de la más nueva a la más vieja."""
    if not os.path.isdir(destino):
        return []
    return sorted((n for n in os.listdir(destino) if _NOMBRE.match(n)), reverse=True)


_SIN_COMPRIMIR = re.compile(r"^cimiento-\d{4}-\d{2}-\d{2}\.sql$")


def podar(destino, guardar=GUARDAR):
    """Quita las copias que sobran después de las `guardar` más nuevas, y las
    que quedaron sin comprimir de la primera versión de esta copia."""
    for nombre in copias(destino)[guardar:]:
        os.remove(os.path.join(destino, nombre))
    for nombre in os.listdir(destino):
        if _SIN_COMPRIMIR.match(nombre):
            os.remove(os.path.join(destino, nombre))


def hay_de_hoy(destino, hoy=None):
    hoy = hoy or datetime.date.today()
    return "%s%s%s" % (PREFIJO, hoy.isoformat(), EXTENSION) in copias(destino)


def probar(ruta, ajustes=None, estandar=None):
    """Carga la copia en una base aparte, cuenta sus tablas y la borra. Devuelve
    `{tabla: filas}`. La base real no se toca."""
    ajustes = ajustes or _ajustes(estandar)
    aparte = "%s_prueba_copia" % ajustes["NAME"]
    conexion = _conectar(ajustes, base="")
    try:
        with conexion.cursor() as cursor:
            cursor.execute("DROP DATABASE IF EXISTS `%s`" % aparte)
            cursor.execute("CREATE DATABASE `%s` CHARACTER SET utf8mb4" % aparte)
            cursor.execute("USE `%s`" % aparte)
            with gzip.open(ruta, "rt", encoding="utf-8") as f:
                for linea in f:
                    linea = linea.rstrip("\n")
                    if linea and not linea.startswith("--"):
                        cursor.execute(linea)
            conexion.commit()
            cursor.execute("SHOW TABLES")
            tablas = [t for (t,) in cursor.fetchall()]
            cuenta = {}
            for tabla in tablas:
                cursor.execute("SELECT COUNT(*) FROM `%s`" % tabla)
                cuenta[tabla] = cursor.fetchone()[0]
            cursor.execute("DROP DATABASE `%s`" % aparte)
        return cuenta
    finally:
        conexion.close()


# ── la copia del día, desde el inicio de sesión ───────────────────────────

def guardar_estado(destino, dato):
    os.makedirs(destino, exist_ok=True)
    with open(os.path.join(destino, ESTADO), "w", encoding="utf-8") as f:
        json.dump(dato, f, ensure_ascii=False)


def estado(destino):
    try:
        with open(os.path.join(destino, ESTADO), encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def del_dia(estandar=None):
    """Hace la copia de hoy si falta, y anota cómo le fue. La corre el proceso en segundo plano."""
    destino = carpeta(estandar)
    if hay_de_hoy(destino):
        return None
    try:
        ruta = copiar(destino, estandar=estandar)
    except Exception as error:  # noqa: BLE001 — se anota y el inicio de sesión lo avisa
        guardar_estado(destino, {"fecha": datetime.date.today().isoformat(), "bien": False, "error": str(error)})
        return None
    guardar_estado(destino, {"fecha": datetime.date.today().isoformat(), "bien": True,
                             "archivo": os.path.basename(ruta)})
    return ruta


def lanzar_si_falta(estandar):
    """Lanza la copia de hoy en segundo plano si falta, y devuelve el aviso de la
    última copia si falló. Nunca detiene el inicio de sesión."""
    destino = carpeta(estandar)
    aviso = ""
    ultimo = estado(destino)
    if ultimo and not ultimo.get("bien"):
        aviso = "La copia de la base del %s falló: %s" % (ultimo.get("fecha"), ultimo.get("error"))
    if hay_de_hoy(destino):
        return aviso
    cimiento = os.path.join(os.path.abspath(estandar), "proyectos", "cimiento")
    orden = [sys.executable, "-c",
             "import sys; sys.path.insert(0, %r); from core.historia.copia import del_dia; del_dia(%r)"
             % (cimiento, os.path.abspath(estandar))]
    banderas = 0
    if os.name == "nt":
        banderas = subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP
    try:
        subprocess.Popen(orden, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                         creationflags=banderas, close_fds=True)
    except OSError as error:
        aviso = "No se pudo lanzar la copia de la base: %s" % error
    return aviso
