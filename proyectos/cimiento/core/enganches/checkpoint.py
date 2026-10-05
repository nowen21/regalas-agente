"""El checkpoint de la fase se reclama solo (`EP-005·HU-013`).

Cuando se escribe uno de los tres documentos que marcan una puerta de la fase
(`plan_trabajo.md`, `resultado_pruebas.md`, `funcionalidad_implementada.md`),
compara su fecha de escritura con la del `estado-fase.md` de la misma fase. Si
el checkpoint falta o es anterior, hay algo que decir.

**No escribe ni lee el `estado-fase.md`**: decir en qué estación va la fase es
criterio, y el criterio no lo tiene un programa. **Fechas y no contenido**: dos
fechas del sistema de archivos no cuestan nada y no dependen de cómo esté
redactado el checkpoint. Enterarse de que se escribió un archivo es de la
herramienta y vive en el adaptador.
"""
import os

from ..validadores.epicas import Epicas

# Los tres documentos cuya escritura es pasar una puerta (`02·F15`). El plan de
# pruebas y el README no marcan ninguna.
DOCUMENTOS_DE_PUERTA = ("plan_trabajo.md", "resultado_pruebas.md", "funcionalidad_implementada.md")
CHECKPOINT = "estado-fase.md"


class Checkpoint:
    """Todo es estático: mira fechas, no guarda estado."""

    @staticmethod
    def fase_de(ruta):
        """La carpeta de la fase a la que pertenece `ruta`, o `""`. Se reconoce
        por el nombre de su carpeta (`02·F12.6`), con `Epicas.fase`: dos copias
        del patrón se desincronizan."""
        carpeta = os.path.dirname(os.path.abspath(ruta))
        return carpeta if Epicas.fase(os.path.basename(carpeta)) else ""

    @classmethod
    def rezago(cls, ruta):
        """`(motivo, fase, documento)` si el checkpoint quedó atrás, o `None`.

        `motivo` es `"falta"` o `"atrasado"`. `None` cuando no hay nada que
        decir: el archivo no es de puerta, no está en una fase, o ya no existe.
        """
        nombre = os.path.basename(ruta)
        if nombre not in DOCUMENTOS_DE_PUERTA:
            return None
        fase = cls.fase_de(ruta)
        if not fase or not os.path.isfile(ruta):
            return None
        checkpoint = os.path.join(fase, CHECKPOINT)
        if not os.path.isfile(checkpoint):
            return ("falta", fase, nombre)
        try:
            if os.stat(checkpoint).st_mtime < os.stat(ruta).st_mtime:
                return ("atrasado", fase, nombre)
        except OSError:
            return None                     # se borró entre mirar y medir: silencio
        return None

    @staticmethod
    def como_texto(hallazgo, raiz=""):
        """El aviso, con la fase relativa al proyecto para que se sepa dónde."""
        motivo, fase, documento = hallazgo
        donde = fase
        if raiz:
            try:
                donde = os.path.relpath(fase, raiz)
            except ValueError:              # otra unidad en Windows
                pass
        donde = donde.replace("\\", "/")
        if motivo == "falta":
            return ("[LA FASE PASÓ UNA PUERTA SIN CHECKPOINT]\n"
                    f"Se escribió `{documento}` en `{donde}` y la fase no tiene "
                    f"`{CHECKPOINT}`. Escribirlo con la estación en que va "
                    "(`plantillas/ciclo-vida-proyectos/10-estado-fase.md`): es lo que la próxima sesión lee "
                    "para seguir sin releer la conversación.")
        return ("[EL CHECKPOINT DE LA FASE QUEDÓ ATRÁS]\n"
                f"Se escribió `{documento}` en `{donde}` y su `{CHECKPOINT}` es "
                "anterior. Ponerlo al día con la puerta que acaba de pasar.")
