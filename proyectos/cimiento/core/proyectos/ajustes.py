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

# `EP-029·HU-001` · Qué tan estricta es la revisión de pruebas de un proyecto.
# Se guarda con las palabras que ve el usuario (acuerdo 8 del análisis 1 del
# pendiente 141): el formulario las muestra tal cual.
SOLO_AVISAR, NO_DEJAR_GUARDAR, NADA = "solo avisar", "no dejar guardar", "nada"
DIAS_DE_REVISION = 7

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
    "revision_pruebas": Ajuste(
        "Revisión de pruebas: qué tan estricto ser", (SOLO_AVISAR, NO_DEJAR_GUARDAR, NADA), SOLO_AVISAR,
        "Qué hace Cimiento cuando toca revisar qué partes del programa no tienen pruebas."),
    "dias_revision": Ajuste(
        "Revisión de pruebas: cada cuántos días", int, DIAS_DE_REVISION,
        "Cuántos días pueden pasar entre una revisión de pruebas y la siguiente."),
}

# `EP-026·HU-009` · Los capítulos opt-in se prenden por proyecto, como un ajuste
# más (análisis 1 del pendiente 132, acuerdo 10). De fábrica, apagados: un patrón
# opt-in se enciende cuando el proyecto lo necesita, no antes. El 17 ya no es
# opt-in: rige para todo proyecto con pantallas (`EP-028·HU-001`).
SI, NO = "sí", "no"
CAPITULOS_OPT_IN = {
    "15": "registros inmutables", "16": "cumplimiento normativo",
    "18": "despliegue e infraestructura", "19": "observabilidad y operación",
    "21": "automatización de procesos", "22": "sistemas que aprenden de datos"}


def clave_opt_in(capitulo):
    return "opt_in_%s" % capitulo


for _capitulo, _tema in CAPITULOS_OPT_IN.items():
    AJUSTES[clave_opt_in(_capitulo)] = Ajuste(
        "Patrón opt-in %s (%s)" % (_capitulo, _tema), (SI, NO), NO,
        "Si las reglas del capítulo %s rigen en el proyecto." % _capitulo)

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
