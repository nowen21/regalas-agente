"""Los validadores de Cimiento: cada uno es una clase que hereda de `Validador`.

Importar un validador lo registra; `Validador.registrados()` los da todos.
"""
from .aislamiento import PruebasAisladas
from .base import Validador
from .calidad import FuncionesLargas
from .ci import IntegracionContinua
from .citas import CitasEnlazadas, EnlazadorDeCitas, IndiceDeReglas
from .codigo import ValidadorDeCodigo
from .commits import MensajeDeCommit
from .declaracion import DeclaracionDelProyecto
from .dependencias import LockfileVersionado
from .entidades import TablasDeDominio
from .enlaces import EnlacesRotos, FormatoDeEnlaces, IndicesDeCarpetas, ReparadorDeEnlaces
from .errores import CapturasYLogs
from .esquema import IntegridadDeEsquema
from .estacion import EstacionDelCommit
from .estructura import ConvencionDeNombres
from .fases import EstructuraDeFases
from .marcas import Marcas, MarcasDeGeneracion
from .migraciones import MigracionesReversibles
from .moldes import Moldes
from .plantillas import DocumentoContraPlantilla
from .rama import RamaDedicada
from .rendimiento import ConsultasCostosas
from .secretos import SecretosEnElCodigo
from .seguridad import InyeccionYSesion
from .trazabilidad import TrazabilidadDeFases
from .veredictos import Veredictos
from .versionado import ArchivosVersionados

# Los que se pasaron en la fila 21 del análisis. Las clases de apoyo de cada
# módulo (`Pendientes`, `CuerpoDeReglas`, `Traza`…) se importan de su módulo.
from .acciones import InventarioDeAcciones
from .amarre import MapaDelAmarre
from .brevedad import Brevedad
from .checklist import Checklist
from .cruces import CrucesEntreModulos
from .ejecutable import QuienLaHaceCumplir
from .expediente import Expediente
from .guardian_version import VersionDelCambio
from .herramientas import Auditoria, Linter, Suite
from .indices import IndicesPorAfinar
from .inmutable import HistoricoInmutable
from .metareglas import CatalogoDelProyecto, Metareglas
from .numeracion import Numeracion
from .parecidas import ReglasParecidas
from .pendientes import NumeracionDePendientes
from .reaperturas import Reaperturas
from .repetidas import FuncionesRepetidas
from .sesiones import SesionesMezcladas
from .sitio import MapaDelSitio
from .version import VersionDelEstandar
from .vigencia import Vigencia

__all__ = ["Validador", "ValidadorDeCodigo", "FuncionesLargas", "CapturasYLogs",
           "InyeccionYSesion", "ConsultasCostosas", "PruebasAisladas", "DeclaracionDelProyecto",
           "MigracionesReversibles", "IntegridadDeEsquema", "ConvencionDeNombres", "TablasDeDominio",
           "ArchivosVersionados", "LockfileVersionado", "IntegracionContinua", "RamaDedicada",
           "SecretosEnElCodigo", "MensajeDeCommit", "EnlacesRotos", "FormatoDeEnlaces",
           "IndicesDeCarpetas", "ReparadorDeEnlaces", "TrazabilidadDeFases", "DocumentoContraPlantilla",
           "CitasEnlazadas", "EnlazadorDeCitas", "IndiceDeReglas", "Marcas", "MarcasDeGeneracion",
           "EstructuraDeFases", "EstacionDelCommit", "Moldes", "Veredictos",
           "Auditoria", "Brevedad", "CatalogoDelProyecto", "Checklist", "CrucesEntreModulos", "Expediente", "HistoricoInmutable", "IndicesPorAfinar", "InventarioDeAcciones", "Linter", "MapaDelAmarre", "MapaDelSitio", "Metareglas", "Numeracion", "NumeracionDePendientes", "QuienLaHaceCumplir", "Reaperturas", "SesionesMezcladas", "Suite", "VersionDelCambio", "VersionDelEstandar", "Vigencia", "FuncionesRepetidas", "ReglasParecidas"]
