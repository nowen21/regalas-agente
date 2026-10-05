"""`EP-023 · HU-003 · CA-11` · El proyecto se entera cuando su pendiente se resuelve.

**Qué resuelve.** Un proyecto que encuentra un defecto del estándar lo reporta
con un pendiente allá y deja otro de seguimiento acá (`02·F24`). Con la forma
vieja, el aviso de vuelta lo escribía `cerrar` al mover el pendiente a
`pendientes/hecho/`; la forma nueva no mueve nada, y el aviso no llegaba a nadie.

**Cómo lo resuelve** (análisis 13 del pendiente 103, acuerdos 3 y 4). Para cada
pendiente reportado que quedó cerrado sigue los enlaces hasta el seguimiento del
proyecto: el pendiente del estándar enlaza el hallazgo del proyecto, y ese
hallazgo enlaza su pendiente. Ahí deja `aviso-resuelto.md`, una sola vez, con
«Comprobado» lleno: Cimiento ya probó la corrección en el proyecto (análisis 1
del pendiente 110, acuerdo 7).

**Lo que no hace, y se declara.** No toca el código ni el pendiente del
proyecto: solo escribe el aviso. Si un enlace falta o lleva a otra parte, no
escribe y dice cuál.
"""
import os
import re

from ..comun import Archivos
from ..validadores.pendientes import COMPROBADO, Pendientes

AVISO = "aviso-resuelto.md"

_DE_DONDE = re.compile(r"^\|\s*\*\*De dónde sale\*\*\s*\|(.+?)\|\s*$", re.M)
_ENLACE_H = re.compile(r"\[[^\]]*?(H-\d+)[^\]]*\]\(([^)#\s]+)")
_FILA_PENDIENTE = re.compile(r"^\|\s*Pendiente\s*\|(.*)\|\s*$", re.M)
_ENLACE = re.compile(r"\]\(([^)#\s]+)")

PLANTILLA = """# Aviso: el estándar resolvió el pendiente que este proyecto reportó

Lo escribió `validadores/aviso_resuelto.py` el {fecha}. No se edita.

| | |
|---|---|
| **Pendiente del estándar** | `{pendiente}` |
| **Versión que trae la corrección** | {version} |

## Cómo lo comprobó Cimiento

Cimiento reprodujo el caso en una copia de este proyecto, en el escenario donde se presentó, y comprobó que la corrección funciona antes de avisar (`02·F29`).

{prueba}

## Qué hacer con esto

Actualizar el estándar en este proyecto y seguir con el trabajo. El pendiente de seguimiento de esta carpeta queda cerrado.

**Comprobado:** {fecha}
"""

# `02·F29` · Lo que Cimiento comprobó en el proyecto que reportó, antes de avisar.
PRUEBA = "prueba-en-el-proyecto.md"
_RESULTADO = re.compile(r"^\*\*Resultado:\*\*\s*(pasa|falla)\s*$", re.M)


def _leer(ruta):
    return Archivos().leer(ruta)


def _destino(enlace, desde):
    return os.path.normpath(os.path.join(os.path.dirname(desde), enlace.replace("/", os.sep)))


class AvisoResuelto:
    """El aviso de vuelta del estándar a los proyectos que reportaron."""

    def __init__(self, estandar):
        self.estandar = os.path.abspath(estandar)

    # ── la prueba en el proyecto ──────────────────────────────────────────

    @staticmethod
    def anotar_prueba(carpeta, fecha, escenario, casos):
        """Escribe `prueba-en-el-proyecto.md` en la carpeta del reporte.

        `casos`: `[(qué se probó, cómo, pasó)]`. Pasa solo si pasan todos."""
        paso = bool(casos) and all(c[2] for c in casos)
        filas = "\n".join("| %s | %s | %s |" % (q, c, "Pasa" if p else "Falla") for q, c, p in casos)
        texto = ("# Prueba en el proyecto que reportó\n\n"
                 "Hecha por Cimiento el %s, en %s (`02·F29`).\n\n"
                 "| Qué se probó | Cómo | Resultado |\n|---|---|---|\n%s\n\n"
                 "**Resultado:** %s\n" % (fecha, escenario, filas, "pasa" if paso else "falla"))
        with open(os.path.join(carpeta, PRUEBA), "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)
        return paso

    @staticmethod
    def prueba_paso(carpeta):
        """Si Cimiento ya comprobó la corrección en el proyecto y pasó."""
        m = _RESULTADO.search(_leer(os.path.join(carpeta, PRUEBA)))
        return bool(m) and m.group(1) == "pasa"

    @staticmethod
    def tabla_de_la_prueba(carpeta):
        m = re.search(r"(?ms)^\| Qué se probó.*?(?=^\*\*Resultado)", _leer(os.path.join(carpeta, PRUEBA)))
        return m.group(0).strip() if m else ""

    # ── el seguimiento del proyecto ───────────────────────────────────────

    @staticmethod
    def bloque_del_hallazgo(texto, h):
        """El texto del hallazgo `### H-N` hasta el siguiente encabezado o raya."""
        m = re.search(r"^### %s\b.*$" % re.escape(h), texto, re.M)
        if not m:
            return ""
        fin = re.search(r"^(#{2,3} |---\s*$)", texto[m.end():], re.M)
        return texto[m.end():m.end() + fin.start()] if fin else texto[m.end():]

    def _fuera_del_estandar(self, ruta):
        return not os.path.normcase(ruta).startswith(os.path.normcase(self.estandar) + os.sep)

    def seguimiento_directo(self, ruta, fila):
        """La carpeta del seguimiento que el reporte enlaza directo, fuera del
        estándar, o "" (análisis 1 del pendiente 110, acuerdo 5)."""
        for enlace in _ENLACE.findall(fila):
            destino = _destino(enlace, ruta)
            if os.path.basename(destino) == "pendiente.md":
                destino = os.path.dirname(destino)
            if not self._fuera_del_estandar(destino):
                continue
            if os.path.isfile(os.path.join(destino, "pendiente.md")):
                return destino
        return ""

    def seguimiento_de(self, carpeta):
        """`(carpeta del seguimiento, "")` o `("", por qué no se encontró)`.

        Primero por el enlace directo que trae el reporte; si no lo trae, siguiendo
        el hallazgo del proyecto hasta su pendiente (análisis 1 del pendiente 110,
        acuerdo 5)."""
        ruta = os.path.join(carpeta, "pendiente.md")
        fila = _DE_DONDE.search(_leer(ruta)) if os.path.isfile(ruta) else None
        if not fila:
            return "", "el pendiente no tiene «De dónde sale»"
        directo = self.seguimiento_directo(ruta, fila.group(1))
        if directo:
            return directo, ""
        for h, enlace in _ENLACE_H.findall(fila.group(1)):
            resumen = _destino(enlace, ruta)
            if not os.path.isfile(resumen):
                return "", "el hallazgo %s apunta a %s, que no existe" % (h, enlace)
            fila_p = _FILA_PENDIENTE.search(self.bloque_del_hallazgo(_leer(resumen), h))
            if not fila_p:
                return "", "el hallazgo %s no enlaza su pendiente" % h
            for e in _ENLACE.findall(fila_p.group(1)):
                destino = _destino(e, resumen)
                if os.path.basename(destino) == "pendiente.md":
                    destino = os.path.dirname(destino)
                if os.path.isfile(os.path.join(destino, "pendiente.md")):
                    return destino, ""
            return "", "el pendiente que enlaza el hallazgo %s no existe" % h
        return "", "«De dónde sale» no enlaza un hallazgo"

    def reportado(self, carpeta):
        """`True` si el pendiente enlaza un hallazgo que está fuera del estándar, o
        enlaza directo su seguimiento en el proyecto (análisis 1 del pendiente 110, acuerdo 5)."""
        ruta = os.path.join(carpeta, "pendiente.md")
        fila = _DE_DONDE.search(_leer(ruta)) if os.path.isfile(ruta) else None
        celda = fila.group(1) if fila else ""
        for _, enlace in _ENLACE_H.findall(celda):
            if self._fuera_del_estandar(_destino(enlace, ruta)):
                return True
        for enlace in _ENLACE.findall(celda):
            destino = _destino(enlace, ruta)
            if destino.endswith("pendiente.md") and self._fuera_del_estandar(destino):
                return True
        return False

    @staticmethod
    def comprobado(carpeta):
        """`True` si el aviso de la carpeta del seguimiento ya tiene fecha de comprobado."""
        ruta = os.path.join(carpeta, AVISO)
        return os.path.isfile(ruta) and bool(COMPROBADO.search(_leer(ruta)))

    # ── avisar ────────────────────────────────────────────────────────────

    def avisar(self, fecha, version, escribir=True):
        """`(escritos, sin_entregar)`: rutas de los avisos, y `(pendiente, por qué)` de los que no llegaron."""
        pendientes = Pendientes(self.estandar)
        escritos, sin_entregar = [], []
        for carpeta in pendientes.carpetas():
            if not self.reportado(carpeta) or pendientes.estado(carpeta) != "cerrado":
                continue
            if not self.prueba_paso(carpeta):
                sin_entregar.append((carpeta, "Cimiento todavía no comprobó la corrección en el proyecto "
                                              "(falta %s con resultado «pasa»)" % PRUEBA))
                continue
            destino, porque = self.seguimiento_de(carpeta)
            if not destino:
                sin_entregar.append((carpeta, porque))
                continue
            aviso = os.path.join(destino, AVISO)
            if os.path.exists(aviso):
                continue                    # una sola vez
            if escribir:
                with open(aviso, "w", encoding="utf-8", newline="\n") as f:
                    f.write(PLANTILLA.format(fecha=fecha, version=version, prueba=self.tabla_de_la_prueba(carpeta),
                                             pendiente=os.path.relpath(carpeta, self.estandar).replace(os.sep, "/")))
            escritos.append(aviso)
        return escritos, sin_entregar
