"""El veredicto de una fase se copia solo a donde el estándar manda repetirlo
(`EP-005·HU-003`, fase C).

Lee el §6 del `resultado_pruebas.md` de una fase, con las mismas expresiones
con que se lee para pasar la puerta (`Veredictos`), y deja el mismo veredicto
en los tres sitios donde se repetía a mano: la fila de la fase en el §8 de su
historia, el `README.md` de la fase y el de la historia.

**No decide ni interpreta**: copia lo que el §6 dice. No toca el
`estado-fase.md`, que lo escribe el agente (`HU-013`). Y con un resultado a
medio escribir, sin concepto, no hace nada: un borrador no es un veredicto.
"""
import os
import re

from ..comun import Archivos
from ..validadores.epicas import Epicas
from ..validadores.veredictos import Veredictos

RESULTADO = "resultado_pruebas.md"
_ESTADO_README = re.compile(r"(?m)^\*\*Estado:\*\*.*$")


class CopiaDelVeredicto:
    """Todo es estático: lee un resultado y reescribe celdas."""

    RESULTADO = RESULTADO

    @staticmethod
    def leer_veredicto(resultado):
        """`(concepto, (cumplidos, total) | None)`; concepto es `cumple`, `no cumple` o `""`."""
        texto = Archivos().leer(resultado)
        return Veredictos.concepto(texto), Veredictos.conteo(texto)

    @staticmethod
    def texto_del_estado(concepto, conteo, fecha):
        """Lo que se escribe en la celda de estado."""
        etiqueta = "Cumple" if concepto == "cumple" else "No cumple"
        cabeza = ("Cerrada el %s" if concepto == "cumple" else "Ejecutada el %s") % fecha
        cola = (", %s de %s CA" % conteo) if conteo else ""
        return "%s: %s%s" % (cabeza, etiqueta, cola)

    @staticmethod
    def _fila_de_la_fase(texto, nombre_fase):
        """La fila de tabla cuya primera celda enlaza la carpeta de la fase, o `None`."""
        patron = re.compile(r"(?m)^\|\s*\[[^\]]*\]\(" + re.escape(nombre_fase)
                            + r"/?(?:README\.md)?\)\s*\|.*$")
        return patron.search(texto)

    @staticmethod
    def _con_ultima_celda(fila, nueva):
        celdas = fila.strip().strip("|").split("|")
        celdas[-1] = " " + nueva + " "
        return "|" + "|".join(celdas) + "|"

    @staticmethod
    def _guardar(ruta, texto, escribir):
        if not escribir:
            return
        with open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)

    @classmethod
    def propagar(cls, resultado, fecha, escribir=True):
        """Copia el veredicto a los tres sitios. `(tocados, avisos)`: las rutas
        reescritas, y lo que no se pudo hacer y por qué, para que el enganche
        lo diga en vez de callar."""
        resultado = os.path.abspath(resultado)
        fase = os.path.dirname(resultado)
        nombre = os.path.basename(fase)
        if os.path.basename(resultado) != RESULTADO or not Epicas.fase(nombre):
            return [], []
        if not os.path.isfile(resultado):
            return [], []
        concepto, conteo = cls.leer_veredicto(resultado)
        if concepto not in ("cumple", "no cumple"):
            return [], []                   # un borrador no es un veredicto
        estado = cls.texto_del_estado(concepto, conteo, fecha)
        tocados, avisos = [], []
        leer = Archivos().leer

        carpeta_hu = os.path.dirname(fase)
        hus = [n for n in os.listdir(carpeta_hu) if n.startswith("HU-") and n.lower().endswith(".md")]
        if hus:
            hu_md = os.path.join(carpeta_hu, hus[0])
            texto = leer(hu_md)
            m = cls._fila_de_la_fase(texto, nombre)
            if m:
                nueva = cls._con_ultima_celda(m.group(0), estado)
                if nueva != m.group(0):
                    cls._guardar(hu_md, texto[:m.start()] + nueva + texto[m.end():], escribir)
                    tocados.append(hu_md)
            else:
                avisos.append("la historia %s no tiene fila para la fase %s en su §8" % (hus[0], nombre))
        else:
            avisos.append("no hay documento de historia junto a la fase %s" % nombre)

        readme_fase = os.path.join(fase, "README.md")
        if os.path.isfile(readme_fase):
            texto = leer(readme_fase)
            linea = "**Estado:** %s. Falta el commit, que el usuario autoriza aparte." % estado
            if _ESTADO_README.search(texto):
                nuevo = _ESTADO_README.sub(lambda _: linea, texto, count=1)
            else:
                nuevo = texto.rstrip("\n") + "\n\n" + linea + "\n"
            if nuevo != texto:
                cls._guardar(readme_fase, nuevo, escribir)
                tocados.append(readme_fase)

        readme_hu = os.path.join(carpeta_hu, "README.md")
        if os.path.isfile(readme_hu):
            texto = leer(readme_hu)
            m = cls._fila_de_la_fase(texto, nombre)
            if m:
                celdas = m.group(0).strip().strip("|").split("|")
                vieja = celdas[-1].strip()
                prefijo = vieja.split(". ", 1)[0] + ". " if ". " in vieja else ""
                nueva = cls._con_ultima_celda(m.group(0), prefijo + estado)
                if nueva != m.group(0):
                    cls._guardar(readme_hu, texto[:m.start()] + nueva + texto[m.end():], escribir)
                    tocados.append(readme_hu)
        return tocados, avisos
