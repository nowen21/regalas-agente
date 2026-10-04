"""`06·R1` y `06·R2` · Una consulta por lista, y solo las columnas que se usan.

R2: nada de `SELECT *`. R1: no ejecutar una consulta por cada elemento (N+1).
Lo comprobable es el caso explícito: una consulta que ejecuta **dentro de un
bucle**. El acceso a una relación diferida dentro del bucle no se ve sin correr
el código, y queda para el ojo humano.

Todo es aviso: puede ser una consulta armada por partes; lo confirma una persona.
"""
import re

from ..comun import AVISO, Hallazgo
from .codigo import Bloques, RecorridoDeCodigo, ValidadorDeCodigo

_SELECT_ESTRELLA = re.compile(r"(?i)\bSELECT\s+\*")
_BUCLE_LLAVES = re.compile(r"\b(foreach|for|while)\b\s*\(")
_BUCLE_PYTHON = re.compile(r"^(\s*)(for|while)\b.*:\s*(#.*)?$")

# Una consulta que ejecuta contra la base (no solo la arma).
_CONSULTA = re.compile(
    r"->\s*(get|first|firstOrFail|find|findOrFail|value|pluck|count|exists|sum|avg|max|min|paginate)\s*\(|"
    r"::\s*(find|findOrFail|first|firstWhere|count)\s*\(|"
    r"\bDB::\s*(select|table|statement|insert|update|delete|scalar)\b|"
    r"\.objects\.\s*(get|filter|all|first|count|exists)\b|"
    r"\.(query|execute|fetchall|fetchone)\s*\(")

_N_MAS_UNO = "consulta dentro de un bucle — R1: posible N+1 (usar eager loading)"


class ConsultasCostosas(ValidadorDeCodigo):
    """Avisa de `SELECT *` y de las consultas dentro de un bucle."""

    nombre = "rendimiento"
    regla = "06·R1, 06·R2"
    descripcion = "SELECT * y consultas en bucle"

    def revisar_texto(self, texto, donde=""):
        hallazgos = [Hallazgo(AVISO, donde, RecorridoDeCodigo.linea_de(texto, m.start()),
                              "`SELECT *` — R2 pide traer solo las columnas necesarias")
                     for m in _SELECT_ESTRELLA.finditer(texto)]
        for m in _BUCLE_LLAVES.finditer(texto):
            cuerpo = Bloques.llaves_tras_condicion(texto, m.end() - 1)
            if cuerpo and _CONSULTA.search(cuerpo):
                hallazgos.append(Hallazgo(AVISO, donde, RecorridoDeCodigo.linea_de(texto, m.start()), _N_MAS_UNO))
        lineas = texto.splitlines()
        for i, linea in enumerate(lineas):
            m = _BUCLE_PYTHON.match(linea)
            if m and _CONSULTA.search("\n".join(Bloques.sangria(lineas, i + 1, len(m.group(1))))):
                hallazgos.append(Hallazgo(AVISO, donde, i + 1, _N_MAS_UNO))
        return hallazgos
