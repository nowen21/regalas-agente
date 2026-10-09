# -*- coding: utf-8 -*-
"""`EP-029·HU-003` · Si la revisión de pruebas de un proyecto falta o está vencida.

**Sin Django** (análisis 1 del pendiente 141, acuerdos 7 y 11): lo llaman el
arranque de cada sesión y el `pre-commit`, que no pueden esperar a que Django
arranque. Lee la base con la misma conexión de los enganches, en una sola vez.

**Sin base o sin registro, se calla**: el proyecto que Cimiento no administra no
tiene nada que cumplir, y un aviso no puede tumbar el arranque ni el commit.

**Qué tan estricto ser** lo dice el ajuste `revision_pruebas` (`EP-029·HU-001`):
«nada» calla, «solo avisar» avisa, «no dejar guardar» además detiene el commit.
"""
from datetime import datetime, timezone

from ..enganches.configuracion import ConfiguracionDelProyecto
from ..enganches.niveles import BaseSinRespuesta
from ..proyectos import ajustes as catalogo

_PARTE = ("SELECT e.tiene_parte FROM pruebas_pruebasdelproyecto e "
          "JOIN proyectos_proyecto p ON p.id = e.proyecto_id "
          "WHERE p.activo = 1 AND LOWER(p.ruta) = LOWER(%s)")
_ULTIMA = ("SELECT MAX(r.fecha) FROM pruebas_revision r "
           "JOIN proyectos_proyecto p ON p.id = r.proyecto_id "
           "WHERE p.activo = 1 AND LOWER(p.ruta) = LOWER(%s)")

SIN_PARTE = ("Este proyecto todavía no puede revisar qué partes del programa no tienen pruebas. "
             "Para arreglarlo, hay que volver a instalar Cimiento en él.")
NUNCA = ("Las pruebas de este proyecto nunca se han revisado. "
         "Toca hacerlo con el botón «Revisar», en «Revisión de pruebas» de Cimiento.")
VENCIDA = ("La última revisión de pruebas fue hace %d días, y toca cada %d. "
           "Toca hacer otra con el botón «Revisar», en «Revisión de pruebas» de Cimiento.")
DETIENE = " Mientras tanto, este proyecto no deja guardar los cambios."


class RevisionDelProyecto(ConfiguracionDelProyecto):
    """Lo que falta de la revisión de pruebas del proyecto en `raiz`."""

    def avisos(self, ahora=None):
        """`(textos, detiene)`: qué decir y si el commit se detiene."""
        estricto = self.valor("revision_pruebas")
        if not self.registrado or estricto == catalogo.NADA:
            return [], False
        try:
            parte, ultima = self.consultar_juntas((_PARTE, None), (_ULTIMA, None))
        except BaseSinRespuesta:
            return [], False
        textos = []
        if not (parte and parte[0][0]):
            textos.append(SIN_PARTE)
        fecha = ultima[0][0] if ultima else None
        dias = self.valor("dias_revision")
        if fecha is None:
            textos.append(NUNCA)
        else:
            # Django guarda en UTC (`USE_TZ`) y PyMySQL la devuelve sin zona.
            pasaron = ((ahora or datetime.now(timezone.utc).replace(tzinfo=None)) - fecha).days
            if pasaron > dias:
                textos.append(VENCIDA % (pasaron, dias))
        detiene = bool(textos) and estricto == catalogo.NO_DEJAR_GUARDAR
        if detiene:
            textos = [t + DETIENE for t in textos]
        return textos, detiene
