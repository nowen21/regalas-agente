"""Lo que un validador encuentra: un incumplimiento o un aviso, anclado a archivo y línea."""
import re

FALLA = "FALLA"     # incumplimiento claro: rompe la corrida
AVISO = "AVISO"     # algo que una persona debe mirar: no rompe nada

# La regla sale del mensaje, que ya la cita: «(07·Q3)», «Q3», «02·F24».
_REGLA_EN_MENSAJE = re.compile(r"\b(?:(\d{2})·)?([A-Z]{1,4}\d+(?:\.\d+)?)\b")


class Hallazgo:
    """Un incumplimiento o aviso. `linea` 0 es el archivo completo."""

    def __init__(self, severidad, archivo, linea, mensaje, regla=None):
        self.severidad = severidad
        self.archivo = archivo
        self.linea = linea
        self.mensaje = mensaje
        self._regla = regla

    @property
    def regla(self):
        """`«NN·XN»` si se puede saber, o `""`. Nunca inventa.

        La declarada manda; si no hay, la primera cita con capítulo del mensaje
        gana sobre la suelta, porque el capítulo hace único al identificador.
        """
        if self._regla:
            return self._regla
        con_capitulo, suelta = "", ""
        for capitulo, id_ in _REGLA_EN_MENSAJE.findall(self.mensaje or ""):
            if capitulo and not con_capitulo:
                con_capitulo = "%s·%s" % (capitulo, id_)
            elif not suelta:
                suelta = id_
        return con_capitulo or suelta

    def __eq__(self, otro):
        return isinstance(otro, Hallazgo) and (
            self.severidad, self.archivo, self.linea, self.mensaje) == (
            otro.severidad, otro.archivo, otro.linea, otro.mensaje)

    def __repr__(self):
        return "Hallazgo(%r, %r, %r, %r)" % (self.severidad, self.archivo, self.linea, self.mensaje)

    def __str__(self):
        donde = "%s:%s" % (self.archivo, self.linea) if self.linea else self.archivo
        return "[%s] %s — %s" % (self.severidad, donde, self.mensaje)
