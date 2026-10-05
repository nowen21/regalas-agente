"""`EP-004·HU-022` · Un documento que sigue siendo el molde no cuenta escrito.

El andamio crea los cinco documentos de una fase en cuanto la abre, así que
existir no dice que estén escritos. Lo usaban `fases.py` (para el inventario) y
`estacion_commit.py` (para no marcar una fase recién abierta), cada uno
importando las funciones sueltas del otro.

**Se compara contra la plantilla, no contra un umbral de marcadores.** Este
repositorio usa comillas angulares en prosa todo el tiempo —`«Cumple»`—, así que
contando, un documento largo y bien escrito parecía molde. El corte en tres lo
dio el reparto: sobre 664 documentos, ninguno tenía entre 3 y 15.
"""
import os
import re

MOLDES_DEL_CICLO = "plantillas/ciclo-vida-proyectos"

DE_QUE_MOLDE = {
    "plan_trabajo.md": "07-plan-trabajo.md",
    "plan_pruebas.md": "08-plan-pruebas.md",
    "resultado_pruebas.md": "09-resultado-pruebas.md",
    "estado-fase.md": "10-estado-fase.md",
    "funcionalidad_implementada.md": "11-funcionalidad-implementada.md",
}

MINIMO = 3

_MARCADOR = re.compile("«[^»\n]{0,120}»|AAAA-MM-DD")


def _leer(ruta):
    try:
        with open(ruta, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


class Moldes:
    """Los marcadores de cada plantilla del ciclo, leídos una vez.

    **Se leen del repositorio, no de una lista en el código**: si una plantilla
    cambia sus marcadores, la comparación se ajusta sola. Una plantilla que no
    está no aporta nada y su documento deja de comprobarse (`04·R4`).
    """

    def __init__(self, raiz):
        carpeta = os.path.join(os.path.abspath(raiz), *MOLDES_DEL_CICLO.split("/"))
        self.de_cada_uno = {}
        for documento, molde in DE_QUE_MOLDE.items():
            suyos = self.marcadores(_leer(os.path.join(carpeta, molde)))
            if suyos:
                self.de_cada_uno[documento] = suyos

    def __bool__(self):
        return bool(self.de_cada_uno)

    @staticmethod
    def marcadores(texto):
        return set(m.strip() for m in _MARCADOR.findall(texto))

    def sigue_siendo_el_molde(self, ruta_documento, documento=None):
        """Los marcadores del molde que el documento conserva, si son bastantes,
        o `None` si está escrito. Cuenta cuántos son **del molde**, no cuántos tiene."""
        propios = self.de_cada_uno.get(documento or os.path.basename(ruta_documento))
        if not propios:
            return None
        quedan = self.marcadores(_leer(ruta_documento)) & propios
        return quedan if len(quedan) >= MINIMO else None

    def sin_llenar(self, ruta_fase):
        """`[(documento, marcadores que quedaron)]` de una fase."""
        encontrados = []
        for documento in sorted(self.de_cada_uno):
            ruta = os.path.join(ruta_fase, documento)
            if os.path.isfile(ruta):
                quedan = self.sigue_siendo_el_molde(ruta, documento)
                if quedan:
                    encontrados.append((documento, quedan))
        return encontrados
