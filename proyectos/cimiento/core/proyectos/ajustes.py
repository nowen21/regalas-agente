# -*- coding: utf-8 -*-
"""`EP-025·HU-013` · Los ajustes de Cimiento, y cuál vale en un proyecto.

**Tres capas** (análisis 3 del pendiente 119, acuerdo 5): el valor de fábrica,
que está acá; el de la base de Cimiento, común a todos los proyectos; y el del
proyecto, que manda solo para él. Arriba de las tres, la suspensión temporal de
una regla o del freno, con motivo y vencimiento.

**Sin Django**: lo usan también los enganches, que leen la base con PyMySQL.

**Lo que nunca se suspende**: el núcleo (`00·N1` a `00·N8`), porque es lo que
protege los datos y las claves (`00·N6`), y el histórico, que además tapa las
claves antes de guardar la conversación.
"""
from collections import namedtuple

from ..comun.enganches import NO_SE_SUSPENDEN
from .limites import LIMITE_ARCHIVO, LIMITE_ENGANCHE

Ajuste = namedtuple("Ajuste", "titulo opciones fabrica ayuda")

RELATIVAS, COMPLETAS = "relativas", "completas"

AJUSTES = {
    "rutas_en_avisos": Ajuste(
        "Rutas en los avisos", (RELATIVAS, COMPLETAS), RELATIVAS,
        "Relativas al proyecto (base/02-…) o completas (C:/…)."),
    "limite_enganche": Ajuste(
        "Límite por enganche", int, LIMITE_ENGANCHE,
        "Tokens que puede agregar un enganche antes de avisar."),
    "limite_archivo": Ajuste(
        "Límite por archivo", int, LIMITE_ARCHIVO,
        "Tokens que puede ocupar un archivo leído antes de avisar."),
}

# Lo que se suspende como «el freno»: los dos enganches que detienen acciones.
FRENO = "freno"
ENGANCHES_DEL_FRENO = ("hook_antes.py", "hook_despues.py")
REGLA, ENGANCHE = "regla", "enganche"
TIPOS = [(REGLA, "Una regla"), (ENGANCHE, "El freno entero")]
DIAS_MAXIMOS = 30


def es_del_nucleo(id_completo):
    capitulo, _, regla = (id_completo or "").partition("·")
    return capitulo == "00" and regla.startswith("N")


def se_puede_suspender(tipo, nombre):
    """¿Se ofrece y se acepta suspender esto? El núcleo y el histórico, nunca."""
    if tipo == REGLA:
        return bool(nombre) and not es_del_nucleo(nombre)
    if tipo == ENGANCHE:
        return nombre == FRENO and not set(ENGANCHES_DEL_FRENO) & set(NO_SE_SUSPENDEN)
    return False


def limpio(clave, valor):
    """El valor como se guarda (texto), o `ValueError` si no es válido. Vacío es "" (usar la capa de abajo)."""
    ajuste = AJUSTES[clave]
    texto = ("" if valor is None else str(valor)).strip()
    if not texto:
        return ""
    if ajuste.opciones is int:
        try:
            numero = int(texto)
        except ValueError:
            raise ValueError("«%s» pide un número entero" % ajuste.titulo) from None
        if numero < 1:
            raise ValueError("«%s» va desde 1" % ajuste.titulo)
        return str(numero)
    if texto not in ajuste.opciones:
        raise ValueError("«%s» va con una de estas: %s" % (ajuste.titulo, ", ".join(ajuste.opciones)))
    return texto


def como_valor(clave, texto):
    """El texto guardado, con su tipo."""
    return int(texto) if AJUSTES[clave].opciones is int else texto


def efectivos(base=None, del_proyecto=None):
    """`{clave: (valor, capa)}`: el del proyecto, si no el de la base, si no el de fábrica."""
    base, del_proyecto = base or {}, del_proyecto or {}
    salida = {}
    for clave, ajuste in AJUSTES.items():
        for capa, valores in (("proyecto", del_proyecto), ("base", base)):
            try:
                texto = limpio(clave, valores.get(clave))
            except ValueError:
                texto = ""              # un valor roto en la base no tumba a nadie: cuenta la capa de abajo
            if texto:
                salida[clave] = (como_valor(clave, texto), capa)
                break
        else:
            salida[clave] = (ajuste.fabrica, "fábrica")
    return salida
