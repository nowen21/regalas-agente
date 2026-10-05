"""`09·G2` y `09·G8` · El mensaje de un commit.

  G2 · primera línea breve, con contenido; si hay cuerpo, va después de una
       línea en blanco.
  G8 · el mensaje no lleva firma de herramienta (`Co-Authored-By`, «generado con»).

Solo se comprueba lo que está escrito en `base/09-git.md`. Que el cuerpo arranque
con la idea del usuario (G8) no se puede medir y queda a criterio de quien escribe.
"""
import re

from ..comun import AVISO, FALLA, Git, Hallazgo
from .base import Validador

LARGO_MAXIMO = 72

# Mensajes que no dicen nada: el ejemplo INCORRECTO de G2.
VACIOS = {"cambios", "cambio", "fix", "wip", "update", "actualizacion", "actualización", "varios",
          "arreglo", "arreglos", "ajustes", "ajuste", "commit", "misc", "temp", "prueba", "test"}

# `[ \t]*` y no `\s*`: `\s` se come el salto de línea y ancla el hallazgo una línea antes.
PROHIBIDOS = [
    (re.compile(r"^[ \t]*Co-Authored-By:", re.IGNORECASE | re.MULTILINE), "Co-Authored-By"),
    (re.compile(r"Generated with \[?Claude Code", re.IGNORECASE), "firma de herramienta"),
]


class MensajeDeCommit(Validador):
    """Revisa un mensaje de commit: el dado, o el de una revisión del repositorio."""

    nombre = "commits"
    regla = "09·G2, 09·G8"
    descripcion = "el mensaje de un commit"

    def __init__(self, proyecto, archivos=None, mensaje=None, origen="(mensaje)", revision="HEAD"):
        super().__init__(proyecto, archivos)
        self.mensaje = mensaje
        self.origen = origen
        self.revision = revision

    def validar(self):
        if self.mensaje is None:
            return self.revisar(Git(self.proyecto.raiz).mensaje(self.revision), "commit %s" % self.revision)
        return self.revisar(self.mensaje, self.origen)

    @staticmethod
    def revisar(mensaje, origen="(mensaje)"):
        """El núcleo puro."""
        lineas = [l for l in mensaje.splitlines() if not l.startswith("#")]   # lo que git descarta
        while lineas and not lineas[-1].strip():
            lineas.pop()
        if not lineas or not lineas[0].strip():
            return [Hallazgo(FALLA, origen, 1, "el mensaje está vacío")]
        asunto = lineas[0].rstrip()
        hallazgos = []
        if asunto.strip().lower().rstrip(".") in VACIOS:
            hallazgos.append(Hallazgo(FALLA, origen, 1, "asunto sin contenido: «%s» — G2 pide qué y por qué" % asunto))
        if asunto.endswith("."):
            hallazgos.append(Hallazgo(AVISO, origen, 1, "el asunto no lleva punto final"))
        if len(asunto) > LARGO_MAXIMO:
            hallazgos.append(Hallazgo(AVISO, origen, 1, "asunto de %d caracteres; G2 lo pide breve (referencia: %d)"
                                      % (len(asunto), LARGO_MAXIMO)))
        if len(lineas) > 1 and lineas[1].strip():
            hallazgos.append(Hallazgo(FALLA, origen, 2, "falta la línea en blanco entre el asunto y el cuerpo"))
        for patron, nombre in PROHIBIDOS:
            m = patron.search(mensaje)
            if m:
                hallazgos.append(Hallazgo(FALLA, origen, mensaje[:m.start()].count("\n") + 1,
                                          "el mensaje incluye %s — G8 no firma con la herramienta" % nombre))
        return hallazgos
