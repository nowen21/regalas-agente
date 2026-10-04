"""Los validadores de Cimiento: cada uno es una clase que hereda de `Validador`.

Importar un validador lo registra; `Validador.registrados()` los da todos.
"""
from .aislamiento import PruebasAisladas
from .base import Validador
from .calidad import FuncionesLargas
from .codigo import ValidadorDeCodigo
from .errores import CapturasYLogs
from .rendimiento import ConsultasCostosas
from .seguridad import InyeccionYSesion

__all__ = ["Validador", "ValidadorDeCodigo", "FuncionesLargas", "CapturasYLogs",
           "InyeccionYSesion", "ConsultasCostosas", "PruebasAisladas"]
