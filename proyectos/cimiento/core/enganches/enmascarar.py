"""`EP-005·HU-002` · Tapa la clave antes de que se escriba en el histórico.

**El daño era real y estaba medido.** Una clave pegada en el chat quedaba
escrita en claro en la transcripción, y la transcripción se versiona: de ahí no
se borra, queda en el historial para siempre.

**Se reconoce con lo que `secretos` ya sabe**, y no con una lista nueva: las
ocho formas de secreto de proveedor y el molde de la variable con pinta de
clave. Duplicarlas acá dejaría dos listas que se separan.

**La marca es `«enmascarado»`**, la misma que el estándar usa para el espacio
por llenar: se ve que hubo algo, y se distingue del texto del mensaje.

**Lo que no se tapa, y es la mitad del trabajo:** el molde (`tu-clave`,
`changeme`, `<...>`), porque taparlo vuelve ilegible un ejemplo; y la línea que
lee del entorno, que es justo la forma correcta.
"""
import re

from ..validadores.secretos import _ENTORNO, ASIGNA, SEGUROS, SecretosEnElCodigo

MARCA = "«enmascarado»"

# **La misma clave, tecleada por una persona.** `ASIGNA` se escribió para buscar
# secretos en código fuente, donde el valor va entre comillas; en un chat nadie
# las escribe, y `API_KEY=secreto` pasaba en claro (pendiente 84). Acá el valor
# va sin comillas, sin espacios y de seis o más, el mismo mínimo del otro. Se
# suman `token`, `clave` y `contraseña`, que son las que se dicen hablando.
_CLAVE = (r"pass(?:word|wd)?|secret|api[_-]?key|apikey|access[_-]?key|"
          r"client[_-]?secret|auth[_-]?token|private[_-]?key|token|clave|"
          r"contraseña")
_ASIGNA_SIN_COMILLAS = re.compile(
    r"(?i)\b(?P<clave>" + _CLAVE + r")\b\s*[:=]>?\s*"
    r"(?P<valor>[^\s'" + chr(34) + r"`,;)]{6,})")


class Enmascarador:
    """Todo es estático: recibe texto y devuelve texto, no guarda estado."""

    MARCA = MARCA

    @staticmethod
    def _parece_clave_tecleada(valor):
        """Un valor sin comillas puede ser una clave o código pegado en el chat
        (`clave = h.regla`). **Un secreto casi siempre trae un número, y si no
        lo trae es largo**: medido sobre este repositorio, con esto desaparece
        el único falso positivo que quedaba."""
        v = valor.strip()
        return any(c.isdigit() for c in v) or len(v) >= 12

    @staticmethod
    def _tapar_asignacion(m):
        if not SecretosEnElCodigo._parece_secreto(m.group("valor")):
            return m.group(0)               # es un molde: taparlo empeora el texto
        return m.group(0).replace(m.group("valor"), MARCA, 1)

    @classmethod
    def enmascarar(cls, texto):
        """`(texto con las claves tapadas, cuántas)`.

        No toca nada más: ni el orden, ni los saltos de línea, ni el resto del
        mensaje. Un enmascarado que reescribe de más deja de ser fiable como
        transcripción, que es lo único que ese archivo tiene que ser.
        """
        if not texto:
            return texto, 0

        cuantas = [0]

        def uno(_m):
            cuantas[0] += 1
            return MARCA

        def asigna(m):
            nueva = cls._tapar_asignacion(m)
            if nueva != m.group(0):
                cuantas[0] += 1
            return nueva

        def asigna_sin_comillas(m):
            if not cls._parece_clave_tecleada(m.group("valor")):
                return m.group(0)
            return asigna(m)

        salida = []
        for linea in texto.splitlines(keepends=True):
            # 1 · Las formas que delatan un secreto de un proveedor concreto.
            for patron, _motivo in SEGUROS:
                linea = patron.sub(uno, linea)
            # 2 · La variable con pinta de clave asignada a un texto fijo, salvo
            #     que lea del entorno: ahí no hay secreto que tapar.
            if not _ENTORNO.search(linea):
                linea = ASIGNA.sub(asigna, linea)
                # 3 · La misma clave sin comillas. Va después a propósito: si
                #     la de comillas ya la tapó, aquí no queda nada.
                linea = _ASIGNA_SIN_COMILLAS.sub(asigna_sin_comillas, linea)
            salida.append(linea)
        return "".join(salida), cuantas[0]

    @classmethod
    def hay_clave(cls, texto):
        """Si el texto trae algo que se taparía. Para avisar sin reescribir."""
        return cls.enmascarar(texto)[1] > 0
