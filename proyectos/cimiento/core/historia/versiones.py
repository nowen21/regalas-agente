# -*- coding: utf-8 -*-
"""`EP-026·HU-002` · Qué versión sube cada cambio, y con qué número.

**El ámbito sale de la tabla** (análisis 1 del pendiente 132, acuerdos 12 y 14):
lo que es de un proyecto sube la versión de ese proyecto; lo común a todos, la
del estándar. Las tablas que no están en `VERSIONADAS` tienen historia pero no
versión: no son configuración (`20·M10`).

**El tipo sale de dos preguntas** (acuerdo 7): ¿un proyecto que hoy cumple deja
de cumplir? MAYOR; ¿se agrega algo que nadie está obligado a usar? MENOR; si no,
PARCHE. Sin respuesta, PARCHE: un programa no responde preguntas.

**Una versión por envío y por ámbito**: lo que se guarda junto sube junto.
"""
import os

from .models import ESTANDAR, MAYOR, MENOR, PARCHE, PROYECTO, Version

# tabla → de dónde sale el proyecto: el nombre del campo, "pk" si la fila es el
# proyecto, o None si es del estándar.
VERSIONADAS = {
    "proyectos.proyecto": "pk",
    "proyectos.ajustedelproyecto": "proyecto_id",
    "proyectos.suspension": "proyecto_id",
    "niveles.nivelderegla": "proyecto_id",
    "proyectos.ajustebase": None,
    # `EP-026·HU-003` · La memoria es de cada proyecto, aunque viva en la app del estándar.
    "estandar.recuerdo": "proyecto_id",
}
# Las tablas del estándar (`EP-026·HU-003`) suben la del estándar.
APPS_DEL_ESTANDAR = {"estandar"}

INICIAL_PROYECTO = (1, 0, 0)
SI = "si"


def tipo_de(obliga, agrega):
    """El tipo que dan las dos preguntas, respondidas con "si" o "no"."""
    if obliga == SI:
        return MAYOR
    if agrega == SI:
        return MENOR
    return PARCHE


# `EP-026·HU-005` · Una propuesta tiene historia, pero no cambia nada hasta aprobarse.
SIN_VERSION = {"estandar.propuesta",
               # `EP-026·HU-008` · El reporte no sube versión: la sube la corrección.
               "estandar.reporte"}


def ambito_de(tabla, fila, datos):
    """`(ámbito, id del proyecto)`, o `None` si la tabla no lleva versión."""
    if tabla in SIN_VERSION:
        return None
    if tabla not in VERSIONADAS:
        return (ESTANDAR, None) if tabla.split(".")[0] in APPS_DEL_ESTANDAR else None
    campo = VERSIONADAS[tabla]
    if campo is None:
        return ESTANDAR, None
    if campo == "pk":
        return PROYECTO, int(fila)
    proyecto = (datos or {}).get(campo)
    return (PROYECTO, int(proyecto)) if proyecto else None


def _del_archivo():
    """La versión del archivo `VERSION` del estándar, de donde arranca la del estándar."""
    from core.comun import Proyecto

    raiz = Proyecto.estandar()
    try:
        with open(os.path.join(raiz, "VERSION"), encoding="utf-8") as f:
            return tuple(int(x) for x in f.read().strip().split("."))
    except (OSError, ValueError, TypeError):
        return (0, 0, 0)


def ultima(ambito, proyecto_id=None):
    """`(mayor, menor, parche)` de la última versión del ámbito."""
    filtro = Version.objects.filter(ambito=ambito, proyecto_id=proyecto_id).order_by("-id").first()
    if filtro:
        return filtro.mayor, filtro.menor, filtro.parche
    return _del_archivo() if ambito == ESTANDAR else INICIAL_PROYECTO


def siguiente(numero, tipo):
    mayor, menor, parche = numero
    if tipo == MAYOR:
        return mayor + 1, 0, 0
    if tipo == MENOR:
        return mayor, menor + 1, 0
    return mayor, menor, parche + 1


def nueva(ambito, proyecto_id, tipo, resumen, cuenta, quien):
    mayor, menor, parche = siguiente(ultima(ambito, proyecto_id), tipo)
    return Version.objects.create(ambito=ambito, proyecto_id=proyecto_id, mayor=mayor, menor=menor,
                                  parche=parche, tipo=tipo, resumen=resumen, cuenta=cuenta, quien=quien)


def de_partida(numero, resumen, quien):
    """`EP-026·HU-003` · La primera versión del estándar en la base, con el número
    que traía el archivo `VERSION`: importar no cambia lo que se exige."""
    mayor, menor, parche = numero
    return Version.objects.create(ambito=ESTANDAR, proyecto_id=None, mayor=mayor, menor=menor, parche=parche,
                                  tipo=PARCHE, resumen=resumen, quien=quien)


def del_archivo():
    return _del_archivo()


def actual(ambito, proyecto_id=None):
    """El número vigente del ámbito, como texto."""
    return "%d.%d.%d" % ultima(ambito, proyecto_id)
