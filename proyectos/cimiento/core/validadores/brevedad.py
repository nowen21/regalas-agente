"""`00·ID9` · Cuánto ocupa lo que el agente contesta. **Mide, no detiene.**

`ID9` no se puede comprobar con un programa: contar renglones es fácil, decidir
cuál sobra exige entender qué cambia la decisión del que lee. Esto cuenta lo
fácil y no opina de lo otro. Sirve igual porque «me parece que contesta largo»
no se puede revisar, y «la mediana subió de 900 a 2 400 caracteres» sí
(pendiente 58).

No rebota la respuesta: al terminar el turno el texto ya salió, y rebotarlo le
costaría al usuario leer la versión larga y después la corta.
"""
import os
import re

from ..comun import AVISO, Hallazgo
from ..comun.archivos import Archivos
from .base import Validador

# La transcripción la escribe `hook_historico.py`. Cada respuesta abre con esta
# marca y termina donde empieza el siguiente turno.
_AGENTE = re.compile(r"(?m)^\*\*Agente\*\*\s+—\s+([0-9:\- ]+)$")
_TURNO = re.compile(r"(?m)^(?:### \d+ · Usuario|\*\*Agente\*\*) ")
_HTML = re.compile(r"<!--.*?-->", re.S)
_TRANSCRIPCION = re.compile(r"^\d{4}-\d{2}-\d{2}.*\.md$")

# Cuatro líneas de molde son 320 caracteres (`20·M5`); una respuesta no es una
# regla, así que el umbral es seis veces eso. Sale de que las respuestas que el
# usuario paró con «no entiendo» pasaban de ahí, y las que aceptó, no.
HOLGADO = 320 * 6


class Respuestas:
    """Las respuestas del agente en una transcripción. Lo usa también el
    enganche que mide cada turno."""

    @staticmethod
    def de(archivo, archivos=None):
        """`[(fecha, cuántos caracteres)]` de cada respuesta del agente.

        Se mide el texto **como se lee**, sin los comentarios de máquina. Tablas
        y código cuentan a propósito: ocupan pantalla igual.
        """
        texto = (archivos or Archivos()).leer(archivo)
        salida = []
        for m in _AGENTE.finditer(texto):
            siguiente = _TURNO.search(texto, m.end())
            cuerpo = _HTML.sub("", texto[m.end():siguiente.start() if siguiente else len(texto)]).strip()
            if cuerpo:
                salida.append((m.group(1).strip(), len(cuerpo)))
        return salida

    @staticmethod
    def mediana(numeros):
        if not numeros:
            return 0
        orden = sorted(numeros)
        medio = len(orden) // 2
        return orden[medio] if len(orden) % 2 else (orden[medio - 1] + orden[medio]) // 2

    @classmethod
    def resumen(cls, archivo, archivos=None):
        """`{"cuantas","mediana","maxima","total"}` de una transcripción."""
        largos = [n for _f, n in cls.de(archivo, archivos)]
        return {"cuantas": len(largos), "mediana": cls.mediana(largos),
                "maxima": max(largos) if largos else 0, "total": sum(largos)}


class Brevedad(Validador):
    """Un aviso por sesión cuya **mediana** pasa el umbral. Nunca una falla.

    Se mira la mediana y no el máximo: una respuesta larga suele estar
    justificada; lo que señala un problema es que la mitad lo sean.
    """

    nombre = "brevedad"
    regla = "00·ID9"
    descripcion = "cuánto ocupa lo que el agente contesta: mide, no detiene"

    def transcripciones(self):
        """Los archivos de sesión, del más viejo al más nuevo."""
        carpeta = os.path.join(self.proyecto.raiz, "historico-chat")
        if not os.path.isdir(carpeta):
            return []
        return [os.path.join(carpeta, n) for n in sorted(os.listdir(carpeta)) if _TRANSCRIPCION.match(n)]

    def validar(self):
        hallazgos = []
        for archivo in self.transcripciones():
            r = Respuestas.resumen(archivo, self.archivos)
            if r["cuantas"] >= 5 and r["mediana"] > HOLGADO:
                hallazgos.append(Hallazgo(AVISO, archivo, 0, "la mitad de las %d respuestas pasa de %d caracteres "
                                                             "(holgado: %d) — `00·ID9`. No es un incumplimiento: "
                                                             "es un número para mirar al cerrar"
                                          % (r["cuantas"], r["mediana"], HOLGADO)))
        return hallazgos

    def como_texto(self):
        """La serie, para leerla al cerrar la sesión."""
        lineas = []
        for archivo in self.transcripciones():
            r = Respuestas.resumen(archivo, self.archivos)
            if r["cuantas"]:
                nombre = os.path.basename(archivo)[:-3]
                lineas.append("  %-46s %3d resp · mediana %5d · máxima %6d"
                              % (nombre[:46], r["cuantas"], r["mediana"], r["maxima"]))
        if not lineas:
            return ""
        return "Cuánto ocupa lo que el agente contesta (`00·ID9` · mide, no detiene)\n" + "\n".join(lineas)
