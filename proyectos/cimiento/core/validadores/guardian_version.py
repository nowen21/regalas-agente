"""`EP-005 · HU-005` · Un cambio de reglas no se guarda sin su versión.

Si lo que se va a guardar toca `base/` o `plantillas/` (lo que viaja a los
proyectos que heredan), en el mismo commit van su subida de `VERSION` y su
entrada en `CHANGELOG.md`. Es `20·M10` dicho por un programa.

**Detiene y no avisa** (decisión 9 del pendiente 59): que falte la versión se
comprueba mirando qué archivos entran al commit, sin criterio de por medio; un
aviso que nada respalda se ignora.

**No mira** si la entrada dice la verdad ni si el tipo de versión es el
correcto: eso es leer y juzgar. Y un cambio en `documentacion/`, `pendientes/` o
`validadores/` no exige nada: no cambia lo que se le exige a un proyecto.
"""
from ..comun import FALLA, Git, Hallazgo
from .base import Validador

# Lo que viaja a los proyectos que heredan. Si cambia, cambió la norma.
HEREDABLE = ("base/", "plantillas/")

# Lo que tiene que acompañarlo, en el mismo commit.
ACOMPANA = ("VERSION", "CHANGELOG.md")

_QUE_FALTA = {"VERSION": "subir `VERSION`",
              "CHANGELOG.md": "escribir su entrada en `CHANGELOG.md`"}


class VersionDelCambio(Validador):
    """Lo que entra en el commit: si toca la norma, trae su versión y su entrada.

    En `validar.py` corre dentro de `versionado --preparados`; `versionado` ya
    es el nombre de `ArchivosVersionados`, así que este se registra con el del
    módulo.
    """

    nombre = "guardian_version"
    regla = "20·M10"
    descripcion = "un cambio de la norma sin su versión ni su entrada"

    def __init__(self, proyecto, archivos=None, ruta_mostrada=None, preparados=None):
        super().__init__(proyecto, archivos)
        # El repositorio se nombra como llegó, igual que antes de pasarlo a clase.
        self.origen = ruta_mostrada or (proyecto if isinstance(proyecto, str) else self.proyecto.raiz)
        self.preparados = preparados

    def _congelada(self):
        """`EP-026·HU-006` · ¿El estándar de este repositorio está congelado?"""
        from ..estandar import congelado

        return congelado.congelada(self.proyecto.raiz)

    def _con_el_estandar_congelado(self, preparados):
        """`EP-026·HU-006` · `base/`, `VERSION` y `CHANGELOG.md` no entran; `plantillas/`
        entra si el estándar tiene una versión en la base después del último commit."""
        from ..enganches.niveles import BaseSinRespuesta
        from ..estandar import congelado

        salida = []
        quietos = sorted(a for a in preparados if congelado.quieto(a))
        if quietos:
            salida.append(Hallazgo(FALLA, self.origen, 0, "este commit trae `%s`, y %s" % (quietos[0],
                                                                                         congelado.MOTIVO)))
        plantillas = sorted(a for a in preparados if a.startswith("plantillas/"))
        if plantillas:
            ultimo = Git(self.proyecto.raiz).correr("log", "-1", "--format=%ct").strip()
            try:
                fecha = congelado.ultima_version_del_estandar(self.proyecto.raiz)
            except BaseSinRespuesta as error:
                fecha, ultimo = None, ultimo or "0"
                salida.append(Hallazgo(FALLA, self.origen, 0, "sin base no se sabe la versión del estándar: %s"
                                       % error))
                return salida
            if fecha is None or (ultimo and fecha.timestamp() <= int(ultimo)):
                salida.append(Hallazgo(
                    FALLA, self.origen, 0,
                    "este commit cambia `%s` y el estándar no tiene una versión nueva en la base: registrarla "
                    "con `manage.py registrar_version` (20·M10)" % plantillas[0]))
        return salida

    @staticmethod
    def _normalizar(rutas):
        return {r.replace("\\", "/") for r in rutas}

    @classmethod
    def reglas_tocadas(cls, preparados):
        """Los archivos heredables que entran en este commit."""
        return sorted(a for a in cls._normalizar(preparados) if a.startswith(HEREDABLE))

    def validar(self):
        """Vacío si el commit no toca la norma, o si la trae completa."""
        preparados = self.preparados
        if preparados is None:
            preparados = Git(self.proyecto.raiz).preparados()
        preparados = self._normalizar(preparados)

        congelada = self._congelada()
        if congelada:
            return self._con_el_estandar_congelado(preparados)
        tocadas = self.reglas_tocadas(preparados)
        if not tocadas:
            return []
        faltan = [a for a in ACOMPANA if a not in preparados]
        if not faltan:
            return []

        resto = (" y %d archivo(s) más de la norma" % (len(tocadas) - 1)
                 if len(tocadas) > 1 else "")
        que_falta = " y ".join(_QUE_FALTA[a] for a in faltan)
        return [Hallazgo(
            FALLA, self.origen, 0,
            "este commit cambia `%s`%s y no trae %s — lo que viaja a los "
            "proyectos se versiona y se registra (20·M10)" % (tocadas[0], resto, que_falta))]
