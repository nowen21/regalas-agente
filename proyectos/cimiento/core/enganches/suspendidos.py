# -*- coding: utf-8 -*-
"""`EP-025·HU-032`, fase B · Cada enganche sabe al arrancar si su momento está suspendido.

**El primero que llega les cuenta a los otros** (análisis 1 del pendiente 149,
acuerdo 3). Los 8 enganches de cada mensaje arrancan a la vez, así que «el
primero» es el que gana el turno: crear un archivo con `O_EXCL` lo gana uno solo.
Ese consulta la base y deja la lista; los demás esperan hasta 2 segundos y la
leen. La lista es de la sesión y vale hasta el mensaje siguiente; los eventos sin
mensaje propio (antes y después de cada herramienta, al terminar) usan la del
mensaje en curso. Sin lista a tiempo, o sin base, el enganche corre: nada
suspendido es lo de siempre.

**Sin Django**, como el freno: se lee con PyMySQL (`niveles.py`).

    salir_si_esta_suspendido(__file__)      # primera línea de `main()` de cada adaptador
"""
import hashlib
import io
import json
import os
import sys
import time

from ..comun.enganches import MOMENTOS

CARPETA = ".agente"
ESPERA = 2.0            # segundos que se espera la lista de quien ganó el turno
TURNO_VIEJO = 5.0       # un turno sin lista después de esto se da por caído
GUARDADAS = 24 * 3600   # las listas de sesiones viejas se borran pasado un día

_CONSULTA = ("SELECT s.nombre, UNIX_TIMESTAMP(s.vence), s.motivo FROM proyectos_suspension s "
             "JOIN proyectos_proyecto p ON p.id = s.proyecto_id "
             "WHERE p.activo = 1 AND LOWER(p.ruta) = LOWER(%s) AND s.tipo = 'enganche' "
             "AND s.levantada IS NULL AND s.vence > UTC_TIMESTAMP()")


def _resumen(texto):
    return hashlib.sha1(texto.encode("utf-8")).hexdigest()[:16]


def clave_del_mensaje(evento, datos):
    """La clave de la lista: el mensaje, o `None` si el evento usa la del mensaje en curso."""
    if evento == "UserPromptSubmit":
        return "mensaje:" + _resumen(datos.get("prompt") or "")
    if evento == "SessionStart":
        return "inicio"
    return None


def consultar_la_base(raiz):
    """`[(nombre, vence en segundos, motivo)]` de lo suspendido en el proyecto. Lanza si no hay base."""
    from .niveles import NivelesDelProyecto
    (filas,) = NivelesDelProyecto(raiz).consultar_juntas((_CONSULTA, None))
    return [(nombre, float(vence), motivo) for nombre, vence, motivo in filas]


class Suspendidos:
    """La lista de lo suspendido en `raiz` para una sesión. `consultar` y `ahora` se cambian en las pruebas."""

    def __init__(self, raiz, sesion, consultar=None, ahora=time.time):
        self.raiz, self.sesion, self.ahora = raiz, sesion or "sin-sesion", ahora
        self.consultar = consultar or (lambda: consultar_la_base(raiz))
        self.carpeta = os.path.join(raiz, CARPETA)
        self.archivo = os.path.join(self.carpeta, "suspendidos.%s.json" % _resumen(self.sesion))

    def _leer(self):
        try:
            with io.open(self.archivo, encoding="utf-8") as f:
                return json.load(f)
        except (OSError, ValueError):
            return None

    def _escribir(self, clave, lista):
        temporal = "%s.%d.tmp" % (self.archivo, os.getpid())
        with io.open(temporal, "w", encoding="utf-8") as f:
            json.dump({"clave": clave, "lista": lista}, f, ensure_ascii=False)
        os.replace(temporal, self.archivo)

    def _ganar_el_turno(self, clave):
        turno = os.path.join(self.carpeta, "suspendidos.%s.turno" % _resumen(self.sesion + clave))
        for _ in range(2):
            try:
                os.close(os.open(turno, os.O_CREAT | os.O_EXCL | os.O_WRONLY))
                return turno
            except FileExistsError:
                try:
                    if self.ahora() - os.path.getmtime(turno) <= TURNO_VIEJO:
                        return None
                    os.remove(turno)            # quien lo tenía se cayó: se vuelve a intentar
                except OSError:
                    return None
        return None

    def _limpiar_viejas(self):
        try:
            for nombre in os.listdir(self.carpeta):
                ruta = os.path.join(self.carpeta, nombre)
                if nombre.startswith("suspendidos.") and self.ahora() - os.path.getmtime(ruta) > GUARDADAS:
                    os.remove(ruta)
        except OSError:
            pass

    def lista(self, clave):
        """Lo suspendido, consultando la base solo si este enganche gana el turno del mensaje."""
        guardada = self._leer()
        if guardada and (clave is None or guardada.get("clave") == clave):
            return guardada.get("lista") or []
        clave = clave or "sin-mensaje"
        try:
            os.makedirs(self.carpeta, exist_ok=True)
        except OSError:
            return []
        turno = self._ganar_el_turno(clave)
        if turno:
            try:
                guardada = self._leer()     # quien ganó antes pudo terminar entre la lectura y el turno
                if guardada and guardada.get("clave") == clave:
                    return guardada.get("lista") or []
                try:
                    lista = self.consultar()
                except Exception:       # noqa: BLE001 · sin base, nada suspendido: lo de siempre
                    lista = []
                self._escribir(clave, lista)
                self._limpiar_viejas()
                return lista
            finally:
                try:
                    os.remove(turno)
                except OSError:
                    pass
        limite = time.monotonic() + ESPERA
        while time.monotonic() < limite:
            guardada = self._leer()
            if guardada and guardada.get("clave") == clave:
                return guardada.get("lista") or []
            time.sleep(0.05)
        return []

    def esta(self, nombre, clave):
        ahora = self.ahora()
        return any(n == nombre and vence > ahora for n, vence, _motivo in self.lista(clave))


def _raiz(argv, datos):
    if "--raiz" in argv:
        i = argv.index("--raiz")
        if i + 1 < len(argv):
            return os.path.abspath(argv[i + 1])
    return os.path.abspath(datos.get("cwd") or os.getcwd())


def salir_si_esta_suspendido(adaptador, argv=None, consultar=None):
    """Lee la entrada; si el momento de `adaptador` está suspendido, sale con 0. Si no, la devuelve intacta.

    Los dos del freno no salen acá: el freno suspendido sigue deteniendo lo que viole
    el núcleo, y eso lo decide `Freno.nivel_para` (acuerdo 2)."""
    argv = sys.argv[1:] if argv is None else argv
    try:
        crudo = sys.stdin.buffer.read()
    except (AttributeError, ValueError):
        crudo = (sys.stdin.read() or "").encode("utf-8", "replace")
    sys.stdin = io.TextIOWrapper(io.BytesIO(crudo), encoding="utf-8")
    try:
        datos = json.loads(crudo.decode("utf-8", "replace") or "{}")
        if not isinstance(datos, dict):
            return
        evento = datos.get("hook_event_name") or ""
        nombre = MOMENTOS.get((evento, os.path.basename(adaptador)))
        if not nombre or nombre == "freno":
            return
        suspendidos = Suspendidos(_raiz(argv, datos), datos.get("session_id"), consultar=consultar)
        suspendido = suspendidos.esta(nombre, clave_del_mensaje(evento, datos))
    except Exception:       # noqa: BLE001 · revisar no puede tumbar el enganche: corre como siempre
        return
    if suspendido:
        sys.exit(0)
