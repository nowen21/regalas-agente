"""`13·DOC7` · El cruce entre dos módulos se registra en los dos.

Cuando la especificación de un módulo declara que consume otro, el consumido lo
anota en su historial cruzado: **los dos lados o ninguno**. Si solo se escribe en
uno, el consumido cambia sin enterarse de quién dependía de él.

Se comprueba el registro, no la narrativa: que a cada declaración de un lado le
corresponda la del otro. Si el cruce está bien contado lo lee una persona.

Los módulos salen de la tabla de `.agente/dominio.md`, donde el proyecto declara
dónde vive la especificación de cada uno. Todo es **AVISO**: una especificación
puede estar a medio escribir, y una fase en curso es exactamente eso.
"""
from ..comun import AVISO, Hallazgo, Markdown
from .base import Validador
from .declaracion import DOMINIO, Declaracion

# La fila que dice «acá no hay nada», que no es lo mismo que una tabla vacía.
_NINGUNO = ("ninguno", "ninguna", "no aplica", "n/a")


class CrucesEntreModulos(Validador):
    """Cada consumo declarado en un lado está registrado en el otro."""

    nombre = "cruces"
    regla = "13·DOC7"
    descripcion = "el cruce entre dos módulos se registra en los dos"

    @staticmethod
    def modulos(celda):
        """Los módulos nombrados en una celda, en minúsculas y sin adornos."""
        valor = Markdown.valor_limpio(celda)
        if not valor or valor.lower() in _NINGUNO:
            return []
        return [p.strip().strip("`").lower() for p in valor.split(",") if p.strip()]

    @classmethod
    def consume(cls, texto):
        """Los módulos que esta especificación declara consumir."""
        salida = []
        for _, fila in Markdown.filas_de(texto, "módulo", "qué consume", "por qué"):
            salida += cls.modulos(fila["módulo"])
        return salida

    @classmethod
    def historial(cls, texto):
        """Los módulos que esta especificación registra como consumidores suyos."""
        salida = []
        for _, fila in Markdown.filas_de(texto, "fecha", "módulo que consume"):
            salida += cls.modulos(fila["módulo que consume"])
        return salida

    def validar(self):
        d = Declaracion.leer(self.proyecto, self.archivos)
        if not d.modulos:
            return [Hallazgo(AVISO, self.proyecto.ruta(DOMINIO), 0,
                             "el proyecto no declara sus módulos en `%s`: no hay especificaciones "
                             "que cruzar (DOC7)" % DOMINIO)]

        # `{nombre: (módulo, ruta de la especificación, texto)}`. La ruta va
        # absoluta: relativa, quien reporta la resolvía contra otra carpeta.
        especificaciones = {}
        for modulo in d.modulos:
            if not modulo.especificacion:
                continue
            ruta = self.proyecto.ruta(modulo.especificacion)
            texto = self.archivos.leer(ruta)
            if texto:
                especificaciones[modulo.nombre.lower()] = (modulo, ruta, texto)

        hallazgos = []
        for nombre, (modulo, ruta, texto) in sorted(especificaciones.items()):
            for otro in self.consume(texto):
                if otro not in especificaciones:
                    hallazgos.append(Hallazgo(AVISO, ruta, 0,
                                              "declara que consume `%s`, que no es un módulo declarado "
                                              "del proyecto (DOC7)" % otro))
                elif nombre not in self.historial(especificaciones[otro][2]):
                    hallazgos.append(Hallazgo(AVISO, especificaciones[otro][1], 0,
                                              "`%s` declara que lo consume y su historial cruzado no lo "
                                              "registra — DOC7 pide los dos lados" % modulo.nombre))
            for otro in self.historial(texto):
                if otro in especificaciones and nombre not in self.consume(especificaciones[otro][2]):
                    hallazgos.append(Hallazgo(AVISO, especificaciones[otro][1], 0,
                                              "`%s` lo registra como consumidor y esta especificación no "
                                              "declara qué consume de él — DOC7 pide los dos lados"
                                              % modulo.nombre))
        return hallazgos
