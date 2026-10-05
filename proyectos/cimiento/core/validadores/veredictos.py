"""Leer el veredicto de una fase: «Cumple» o «No cumple», y cuántos criterios.

Lo usaban `fases.py`, `veredicto.py` (que lo copia a los tres sitios donde se
dice) y el inventario, cada uno metiendo la mano en las expresiones privadas del
otro. Acá están una vez.
"""
import os
import re

# `EP-004·HU-021` · Las formas en que el repositorio escribe el veredicto del
# resultado, contadas una por una: `**Concepto:** …`, la fila `| **Concepto** |`
# y `**Concepto: Cumple.**`, con los dos puntos dentro de la negrita.
_VEREDICTO = re.compile(
    r"\*\*Concepto:?\*\*:?\s*\|?\s*\**(No cumple|Cumple)"
    r"|\|\s*\*\*(?:Concepto|Veredicto)\*\*\s*\|\s*\**(No cumple|Cumple)"
    r"|\*\*Concepto:\s*(No cumple|Cumple)",
    re.IGNORECASE)
# La palabra sola bajo el encabezado. **Se exige el título exacto**: en un
# resultado «Cumple» aparece en cada fila de criterio, y buscarla suelta tomaría
# el primer criterio por el veredicto de la fase, que miente hacia lo optimista.
_BAJO_TITULO = re.compile(r"^##\s+\d+\.?\s*Veredicto de la fase[^\n]*\n+\**(No cumple|Cumple)",
                          re.MULTILINE | re.IGNORECASE)
_TITULO_SOLO = re.compile(r"^##\s+\d+\.?\s*Veredicto\s*$\n+\**(No cumple|Cumple)", re.MULTILINE | re.IGNORECASE)
_CONCEPTO_TITULO = re.compile(r"^##\s+\d+\.?\s*Concepto[^\n]*\n+\**(No cumple|Cumple)",
                              re.MULTILINE | re.IGNORECASE)

# El concepto que declaran el resultado y el estado, para compararlos (`HU-014`).
_CONCEPTO_FILA = re.compile(r"^\|\s*\*\*Concepto\*\*\s*\|([^|]+)\|", re.M)
_CONCEPTO_SUELTO = re.compile(r"\*\*Concepto:\s*([^*.]+)", re.M)
# `CA cumplidos` en las fases nuevas, `Criterios cumplidos` en las viejas.
_CONTEO = re.compile(r"\*\*(?:CA|Criterios)\s+cumplidos\*\*\s*\|\s*\**(\d+)\**\s+de\s+\**(\d+)", re.I)
# El §5 del resultado: la tabla de veredicto por exigencia.
_SECCION_5 = re.compile(r"^##\s+5\.[^\n]*\n(.*?)(?=^##\s)", re.M | re.S)
# `EP-004·HU-023` · Un rojo se cierra declarándolo, no deduciéndolo del orden.
_REEMPLAZA = re.compile(r"\|\s*\*\*Reemplaza el veredicto de\*\*\s*\|\s*([^|\n]*?)\s*\|", re.IGNORECASE)

RESULTADO = "resultado_pruebas.md"
ESTADO = "estado-fase.md"
CIERRE = "funcionalidad_implementada.md"


def _leer(ruta):
    try:
        with open(ruta, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


class Veredictos:
    """Todo es estático: lee documentos, no guarda estado."""

    @staticmethod
    def de_la_fase(ruta_fase):
        """`"Cumple"`, `"No cumple"` o `None` si el resultado no lo deja leer.
        Se mira con qué palabra empieza: «Cumple, con los tres criterios» es un cumple."""
        texto = _leer(os.path.join(ruta_fase, RESULTADO))
        if not texto:
            return None
        dice = (_VEREDICTO.search(texto) or _BAJO_TITULO.search(texto)
                or _TITULO_SOLO.search(texto) or _CONCEPTO_TITULO.search(texto))
        if not dice:
            return None
        return next(g for g in dice.groups() if g).strip().capitalize()

    @staticmethod
    def concepto(texto):
        """`"cumple"`, `"no cumple"` o `""`. La salvedad del lado no es otro veredicto."""
        m = _CONCEPTO_FILA.search(texto) or _CONCEPTO_SUELTO.search(texto)
        if not m:
            return ""
        crudo = m.group(1).strip().lower().replace("*", "")
        return "no cumple" if crudo.startswith("no cumple") else ("cumple" if crudo.startswith("cumple") else "")

    @staticmethod
    def conteo(texto):
        """`(cumplidos, total)` de los criterios, o `None` si el documento no lo dice."""
        m = _CONTEO.search(texto)
        return (m.group(1), m.group(2)) if m else None

    @staticmethod
    def exigencias_en_no(texto):
        """Las filas del §5 del resultado cuya última columna es «No»."""
        seccion = _SECCION_5.search(texto)
        if not seccion:
            return []
        salida = []
        for fila in seccion.group(1).splitlines():
            celdas = [c.strip() for c in fila.strip().strip("|").split("|")]
            if len(celdas) >= 3 and celdas[-1].replace("*", "").lower() == "no":
                nombre = celdas[0].replace("*", "").strip()
                if nombre and not nombre.startswith("-"):
                    salida.append(nombre)
        return salida

    @staticmethod
    def declara_reemplazar(ruta_fase):
        """El nombre de la fase que el cierre declara dejar atrás, o `""`."""
        dice = _REEMPLAZA.search(_leer(os.path.join(ruta_fase, CIERRE)))
        return dice.group(1).strip().strip("`*").strip() if dice else ""

    @classmethod
    def reemplazados(cls, ruta_hu, fases):
        """Las fases de la historia cuyo veredicto sale de la cuenta.

        Tres condiciones: quien declara **cumple** (un rojo no cierra otro rojo),
        la nombrada es **de esta historia** y **no es ella misma**. El documento
        reemplazado no se toca (`20·M11`): el rastro del rojo es información.
        """
        dejados = set()
        for nombre in fases:
            nombrada = cls.declara_reemplazar(os.path.join(ruta_hu, nombre))
            if (nombrada and nombrada != nombre and nombrada in fases
                    and cls.de_la_fase(os.path.join(ruta_hu, nombre)) == "Cumple"):
                dejados.add(nombrada)
        return dejados
