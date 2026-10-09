"""`EP-029·HU-008` · Daña el código a propósito y dice qué daños no detectan las pruebas.

Una prueba que no falla cuando el código está roto no prueba nada (`08·T8`). Para
saberlo se daña el código a propósito, se corren las pruebas y se mira si alguna
falla. Antes se escribía un guion para cada vez: hubo 19, y cada uno copiaba en
su encabezado las lecciones de los anteriores (análisis 1 del pendiente 148).
Aquí quedan resueltas de una vez:

- Se devuelve cada archivo **desde su copia**, nunca desde git: el código puede
  no estar guardado.
- Se devuelve en `finally`: si algo se cae con el daño puesto, el archivo vuelve.
- Se lee el **código de salida** de la orden, no su texto: leer «OK» falló dos
  veces (`S-060`, `S-068`).
- Lo que el daño escribió fuera del archivo se borra: se compara qué archivos hay
  antes y después de cada daño.
- Se termina corriendo las pruebas sin daños, y cada archivo se compara con su
  copia.

No depende del lenguaje: cambia texto en un archivo y corre la orden que se le da.
"""
import hashlib
import json
import os
import shutil
import signal
import subprocess
import tempfile

DETECTADO = "detectado"
SE_COLGO = "detectado (se pasó del tiempo)"
NO_DETECTADO = "no detectado"
NO_SE_APLICO = "no se aplicó"

# Carpetas que no son del código y que cuesta recorrer.
NO_SE_MIRAN = {".git", ".venv", "venv", "node_modules"}


class NoSeDana(Exception):
    """Lo que impide empezar, o lo que quedó mal al terminar."""


class Dano:
    def __init__(self, nombre, archivo, antes, despues):
        self.nombre, self.archivo, self.antes, self.despues = nombre, archivo, antes, despues


def leer_danos(ruta):
    """La lista de daños: un JSON con objetos `nombre`, `archivo`, `antes` y `despues`."""
    try:
        with open(ruta, encoding="utf-8") as f:
            datos = json.load(f)
    except (OSError, ValueError) as e:
        raise NoSeDana("no se pudo leer la lista de daños «%s»: %s" % (ruta, e))
    if not isinstance(datos, list) or not datos:
        raise NoSeDana("la lista de daños tiene que ser una lista con al menos un daño")
    danos = []
    for n, d in enumerate(datos, 1):
        faltan = [c for c in ("nombre", "archivo", "antes", "despues") if not isinstance(d, dict) or c not in d]
        if faltan:
            raise NoSeDana("al daño %d le falta: %s" % (n, ", ".join(faltan)))
        danos.append(Dano(str(d["nombre"]), str(d["archivo"]), str(d["antes"]), str(d["despues"])))
    return danos


def correr_orden(orden, carpeta, tiempo):
    """`(pasaron, se_colgo)`. Si se pasa del tiempo, mata la orden con todo lo que abrió."""
    nuevo_grupo = {"creationflags": subprocess.CREATE_NEW_PROCESS_GROUP} if os.name == "nt" \
        else {"start_new_session": True}
    proceso = subprocess.Popen(orden, shell=True, cwd=carpeta, stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL, **nuevo_grupo)
    try:
        return proceso.wait(timeout=tiempo) == 0, False
    except subprocess.TimeoutExpired:
        if os.name == "nt":
            subprocess.run(["taskkill", "/F", "/T", "/PID", str(proceso.pid)],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            os.killpg(proceso.pid, signal.SIGKILL)
        proceso.wait()
        return False, True


def _huella(ruta):
    with open(ruta, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


class Danar:
    """Corre una lista de daños sobre la carpeta `raiz`. `correr` se cambia en las pruebas."""

    def __init__(self, raiz, pruebas, tiempo=600, correr=correr_orden):
        self.raiz, self.pruebas, self.tiempo, self.correr_orden = os.path.abspath(raiz), pruebas, tiempo, correr
        self.borrados = []

    def _correr(self):
        return self.correr_orden(self.pruebas, self.raiz, self.tiempo)

    def _foto(self):
        """Las rutas, relativas a la raíz, de todo lo que hay: carpetas y archivos."""
        hay = set()
        for carpeta, subcarpetas, archivos in os.walk(self.raiz):
            subcarpetas[:] = [s for s in subcarpetas if s not in NO_SE_MIRAN]
            for nombre in subcarpetas + archivos:
                hay.add(os.path.relpath(os.path.join(carpeta, nombre), self.raiz))
        return hay

    def _limpiar(self, antes):
        """Borra lo que apareció desde la foto `antes`: primero archivos, después carpetas vacías."""
        nuevos = sorted(self._foto() - antes, key=len, reverse=True)
        for relativa in nuevos:
            ruta = os.path.join(self.raiz, relativa)
            if os.path.isfile(ruta) or os.path.islink(ruta):
                os.remove(ruta)
                self.borrados.append(relativa)
        for relativa in nuevos:
            ruta = os.path.join(self.raiz, relativa)
            if os.path.isdir(ruta) and not os.listdir(ruta):
                os.rmdir(ruta)
                self.borrados.append(relativa)

    @staticmethod
    def _cambiar(contenido, dano):
        """El contenido dañado, o `None` si el texto original no aparece exactamente una vez."""
        antes, despues = dano.antes.encode("utf-8"), dano.despues.encode("utf-8")
        if contenido.count(antes) != 1 and b"\r\n" in contenido:
            antes, despues = antes.replace(b"\n", b"\r\n"), despues.replace(b"\n", b"\r\n")
        if not antes or contenido.count(antes) != 1:
            return None
        return contenido.replace(antes, despues, 1)

    def correr(self, danos):
        """`[(daño, resultado)]`. Lanza `NoSeDana` si no puede empezar o si algo quedó distinto."""
        pasaron, _ = self._correr()
        if not pasaron:
            raise NoSeDana("las pruebas no pasan sin daños: primero hay que arreglarlas")
        foto = self._foto()
        copias = tempfile.mkdtemp(prefix="danar_a_proposito_")
        originales = {}                     # ruta absoluta → (copia, huella)
        resultados = []
        try:
            for n, dano in enumerate(danos, 1):
                ruta = os.path.join(self.raiz, dano.archivo)
                if not os.path.isfile(ruta):
                    resultados.append((dano, NO_SE_APLICO + ": el archivo no existe"))
                    continue
                with open(ruta, "rb") as f:
                    contenido = f.read()
                danado = self._cambiar(contenido, dano)
                if danado is None:
                    resultados.append((dano, NO_SE_APLICO + ": el texto original no aparece exactamente una vez"))
                    continue
                if ruta not in originales:
                    copia = os.path.join(copias, "%d_%s" % (n, os.path.basename(ruta)))
                    shutil.copy2(ruta, copia)
                    originales[ruta] = (copia, _huella(ruta))
                try:
                    with open(ruta, "wb") as f:
                        f.write(danado)
                    # Python (y otros) reusan lo compilado si el archivo tiene el mismo tamaño y la misma
                    # hora: cambiar «+» por «-» en el mismo segundo correría el código sin daño. Cada daño
                    # le pone al archivo una hora distinta; al devolverlo, `copy2` le pone la original.
                    hora = os.stat(originales[ruta][0]).st_mtime + 2 * n
                    os.utime(ruta, (hora, hora))
                    pasaron, se_colgo = self._correr()
                finally:
                    shutil.copy2(originales[ruta][0], ruta)
                    self._limpiar(foto)
                resultados.append((dano, SE_COLGO if se_colgo else (NO_DETECTADO if pasaron else DETECTADO)))
        finally:
            for ruta, (copia, _huella_original) in originales.items():
                shutil.copy2(copia, ruta)
        distintos = [os.path.relpath(r, self.raiz) for r, (_c, h) in originales.items() if _huella(r) != h]
        if distintos:
            raise NoSeDana("quedaron distintos de su copia: %s; las copias están en %s" % (", ".join(distintos), copias))
        shutil.rmtree(copias, ignore_errors=True)
        pasaron, _ = self._correr()
        if not pasaron:
            raise NoSeDana("las pruebas sin daños ya no pasan al terminar")
        return resultados
