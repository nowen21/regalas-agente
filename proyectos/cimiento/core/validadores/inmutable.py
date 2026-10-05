"""La transcripción del histórico **solo crece**: se agrega, no se reescribe.

Un registro de auditoría que se puede reescribir sin que nadie lo note no es un
registro de auditoría (`notas/estructura.md`, §8). La transcripción la escribe
el programa turno a turno; si su pasado cambió, alguien la editó a mano.

**Cómo se comprueba**: en cada transcripción con cambios sin confirmar, lo ya
confirmado tiene que ser el **prefijo** de lo actual. La renombrada por
`historico.py --renombrar` es un archivo nuevo para git, así que la vía
sancionada no da falsos positivos.

**Todo aviso**: puede haber una edición legítima (tapar una clave filtrada), y
la confirma una persona. Detecta, no impide.
"""
import os
import re

from ..comun import AVISO, Git, Hallazgo
from .base import Validador

CARPETA = "historico-chat"

# Una transcripción: `AAAA-MM-DD-<tema>.md`, en la raíz de la carpeta.
_TRANSCRIPCION = re.compile(r"^\d{4}-\d{2}-\d{2}.*\.md$")


class HistoricoInmutable(Validador):
    """Un aviso por transcripción cuyo pasado confirmado cambió."""

    nombre = "inmutable"
    regla = ""
    descripcion = "la transcripción del histórico solo crece: detecta, no impide"

    @staticmethod
    def solo_crecio(viejo, nuevo):
        """`True` si `nuevo` es `viejo` más lo agregado al final, o igual. Los
        finales de línea de Windows no cuentan: el control de versiones los cambia."""
        return nuevo.replace("\r\n", "\n").startswith(viejo.replace("\r\n", "\n"))

    def modificadas(self):
        """Las transcripciones ya confirmadas que tienen cambios sin confirmar."""
        salida = []
        for linea in Git(self.proyecto.raiz, espera=None).correr("status", "--porcelain", "--", CARPETA).splitlines():
            if len(linea) < 4 or "M" not in linea[:2]:
                continue
            rel = linea[3:].strip().strip('"')
            if os.path.dirname(rel).replace("\\", "/") == CARPETA and _TRANSCRIPCION.match(os.path.basename(rel)):
                salida.append(rel.replace("\\", "/"))
        return salida

    def validar(self):
        git = Git(self.proyecto.raiz, espera=None)
        hallazgos = []
        for rel in self.modificadas():
            confirmado = git.correr("show", "HEAD:%s" % rel)
            if not confirmado:
                continue
            ruta = os.path.join(self.proyecto.raiz, rel)
            if not self.solo_crecio(confirmado, self.archivos.leer(ruta)):
                hallazgos.append(Hallazgo(AVISO, ruta, 0, "la transcripción no solo creció: su contenido ya "
                                                          "confirmado cambió. El histórico se agrega, no se "
                                                          "reescribe — si la edición es legítima (tapar una clave "
                                                          "filtrada), que quede dicha en el mensaje del commit"))
        return hallazgos
