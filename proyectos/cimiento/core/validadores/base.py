"""La clase de la que heredan todos los validadores.

**Comprobar, no arreglar.** La norma vive en los `.md` del estándar; un
validador solo verifica lo que se puede verificar sin criterio, y devuelve
hallazgos. No escribe nada.
"""
from ..comun import Archivos, Proyecto


class Validador:
    """Lo común a todo validador. Cada subclase declara su `nombre` y su `regla`,
    y escribe `validar()`.

    **Se registra solo al heredar.** Una lista aparte de validadores sería una
    segunda verdad que se separa de las clases; acá la lista son las clases.
    """

    nombre = ""         # cómo se pide: `calidad`, `enlaces`…
    regla = ""          # la regla que comprueba: `07·Q3`
    descripcion = ""    # una línea, para la ayuda

    _registro = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls.nombre:
            if cls.nombre in Validador._registro:
                raise ValueError("dos validadores con el nombre %r" % cls.nombre)
            Validador._registro[cls.nombre] = cls

    def __init__(self, proyecto, archivos=None):
        self.proyecto = proyecto if isinstance(proyecto, Proyecto) else Proyecto(proyecto)
        self.archivos = archivos or Archivos()

    def validar(self):
        """`[Hallazgo]` de este proyecto. Cada validador escribe el suyo."""
        raise NotImplementedError("%s no escribió validar()" % type(self).__name__)

    @classmethod
    def registrados(cls):
        """`{nombre: clase}` de todos los validadores importados."""
        return dict(cls._registro)
