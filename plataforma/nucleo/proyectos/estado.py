# -*- coding: utf-8 -*-
"""En qué va un proyecto, calculado desde lo que la plataforma tiene traído.

**No se lee la carpeta del proyecto.** `CA-01` dice «y no hace falta abrir su
carpeta para saberlo», y hay una razón práctica: un proyecto entregado,
archivado o movido de máquina tiene que seguir mostrando su estado. Lo prueba
`CP-009`, que borra la carpeta y comprueba que el estado sale idéntico.

**El estado no se guarda: se calcula al pedirlo.** Un estado guardado a mano
envejece y miente, y el modelo de datos lo dice así.

**Lo que no se puede leer se dice, no se supone.** Contando los 125 estados de
fase del repositorio real aparecieron **doce formas distintas** de escribir en
qué estación va una fase, y cinco que no se dejan leer. Suponer que están
cerradas, o dejarlas fuera de la cuenta, sería afirmar sobre lo que no se leyó
(`04·R4`). Se dicen, con su ruta, y el usuario decide.
"""
import io
import os
import re

from django.conf import settings

from nucleo.importacion import moldes
from nucleo.importacion.models import Traido

# `**Estación actual:** 9 · commit único` y sus once variantes. Se busca el
# número que abre la línea, porque es lo único que se escribe siempre igual.
_ESTACION = re.compile(r"\*\*Estación actual:\*\*\s*(?P<dice>[^\n]*)")
_NUMERO = re.compile(r"^\s*(\d+)")
# `cerrada`, con o sin adornos, es la otra forma que aparece de verdad.
_CERRADA = re.compile(r"(?i)\bcerrad[ao]\b")

# `Aprobado por Ing. …, el 2026-08-25` · `**Estado: APROBADO** (2026-08-24, …)`
_APROBACION = re.compile(r"(?i)aprobad[oa]\s+por|estado:\s*\**APROBADO")
_FECHA = re.compile(r"(\d{4}-\d{2}-\d{2})")

# La última estación del ciclo. Una fase que llegó ahí, o que dice «cerrada»,
# ya no está abierta.
ULTIMA_ESTACION = 9


class Estado(object):
    """Lo que se puede decir de un proyecto sin abrir su carpeta."""

    SIN_EMPEZAR = "sin empezar"
    EN_CURSO = "en curso"

    def __init__(self, proyecto):
        self.proyecto = proyecto
        self.etapas_con_documento = []
        self.etapas_sin_documento = []
        self.fases = 0
        self.fases_abiertas = 0
        self.fases_ilegibles = []      # rutas de las que no se dejaron leer
        self.aprobados = 0
        self.ultima_aprobacion = ""
        self.documentos = 0

    @property
    def resumen(self):
        return self.SIN_EMPEZAR if not self.documentos else self.EN_CURSO

    @property
    def esta_sin_empezar(self):
        return not self.documentos

    @property
    def que_haria_falta(self):
        """Qué le falta a un proyecto sin nada. `CA-02` pide decirlo.

        Una pantalla vacía se lee como un error de la plataforma, y no lo es.
        """
        if not self.esta_sin_empezar:
            return ""
        if not self.proyecto.ruta_viva:
            return ("Para empezar hay que corregir dónde vive su código: la "
                    "carpeta que tiene registrada ya no está.")
        return ("Para empezar, traer lo que este proyecto ya tenga escrito. Si "
                "todavía no tiene documentación, lo primero es la etapa de "
                "planificación.")


def de(proyecto):
    """Calcula el estado de un proyecto. Nunca lee su carpeta."""
    estado = Estado(proyecto)
    traidos = list(Traido.objects.filter(proyecto=proyecto.identificador))
    estado.documentos = len(traidos)

    con_etapa = set()
    for documento in traidos:
        if documento.tipo == "etapa del ciclo de vida":
            con_etapa.add(_etapa_de(documento.origen))
        elif documento.tipo == "estado de fase":
            estado.fases += 1
            abierta, se_pudo_leer = _esta_abierta(documento)
            if not se_pudo_leer:
                estado.fases_ilegibles.append(documento.origen)
            elif abierta:
                estado.fases_abiertas += 1
        if _esta_aprobado(documento):
            estado.aprobados += 1
            fecha = _fecha_de_aprobacion(documento)
            if fecha > estado.ultima_aprobacion:
                estado.ultima_aprobacion = fecha

    estado.etapas_con_documento = [e for e in moldes.ETAPAS if e in con_etapa]
    estado.etapas_sin_documento = [e for e in moldes.ETAPAS if e not in con_etapa]
    return estado


def _etapa_de(origen):
    partes = origen.split("/")
    return partes[-2] if len(partes) >= 2 else ""


def _texto(documento):
    """El texto del documento traído, o "" si no se puede leer."""
    completa = os.path.join(str(settings.CARPETA_DATOS),
                            documento.guardado_en.replace("/", os.sep))
    try:
        with io.open(completa, encoding="utf-8", errors="replace") as abierto:
            return abierto.read()
    except OSError:
        return ""


def _esta_abierta(documento):
    """Si la fase sigue abierta, y **si se pudo saber**.

    Devuelve `(abierta, se_pudo_leer)`. Cuando no se puede leer no se inventa
    una respuesta: quien llama lo cuenta aparte y el estado lo dice.
    """
    dice = _ESTACION.search(_texto(documento))
    if not dice:
        return False, False
    linea = dice.group("dice")
    if _CERRADA.search(linea):
        return False, True
    numero = _NUMERO.search(linea)
    if not numero:
        return False, False
    return int(numero.group(1)) < ULTIMA_ESTACION, True


def _esta_aprobado(documento):
    return bool(_APROBACION.search(_texto(documento)))


def _fecha_de_aprobacion(documento):
    texto = _texto(documento)
    marca = _APROBACION.search(texto)
    if not marca:
        return ""
    # La fecha que sigue a la marca de aprobación, no la primera del documento.
    fecha = _FECHA.search(texto[marca.start():marca.start() + 300])
    return fecha.group(1) if fecha else ""
