# -*- coding: utf-8 -*-
"""Qué rige en cada proyecto — `F-004`.

**Lo obligatorio no se puede apagar.** Es la única exigencia dura de esta
funcionalidad, y la razón de que exista: sin ella, «configurable» quiere decir
«el estándar rige cuando conviene», que es no tener estándar.

**Qué es opcional lo dice el estándar, no la plataforma.** Una regla es opt-in
cuando ella lo dice (`*opt-in*`) o cuando lo dice la cabecera de su capítulo
(`[CAPA 2 · opt-in]`), y entonces rige a todas las del capítulo. Guardar acá una
lista propia de cuáles son opcionales sería una segunda verdad que envejece.

**La configuración vive en el proyecto, no en la base.** Un archivo de texto en
`.agente/configuracion.md`, que viaja con el repositorio y se lee en el commit.
Guardarla en la base de la plataforma dejaría a un proyecto clonado sin ella.

**Cada opción es una forma más de que dos proyectos no se parezcan.** Está
escrito en la ficha de `F-004` y no se resuelve con código: por eso lo que se
enciende y se apaga queda escrito, con fecha y con quién.
"""
import io
import os
import re

from nucleo.auditoria.core import con_constancia

CARPETA = ".agente"
ARCHIVO = "configuracion.md"

# `*opt-in*` marcado en la línea de la propia regla.
_OPT_IN = re.compile(r"\*opt-in\*")
# `[CAPA 2 · opt-in]` en la cabecera: rige a todas las reglas del capítulo.
_CAPITULO_OPT_IN = re.compile(r"·\s*opt-in\s*\]")
# `## DOC5 · Registra... — *opt-in*` — la regla en su propio archivo. **La marca
# tiene que estar en su línea**, no en cualquier parte del archivo: un archivo de
# capítulo nombra varias reglas, y una sola de ellas puede ser la opcional.
# Buscarla en todo el texto marcaba 52 reglas como opcionales, y entre ellas
# `02·F0`, que es la cadena entera del flujo de trabajo.
_ID_DE_REGLA = re.compile(r"^##\s+([A-Z]+\d+(?:\.\d+)?)\s*·([^\n]*)", re.M)
# `| [`DOC5`](reglas/...) | *opt-in* · ...` — la fila del índice del capítulo.
_FILA_DE_INDICE = re.compile(
    r"^\|\s*\[`([A-Z]+\d+(?:\.\d+)?)`\][^|]*\|([^|]*)\|", re.M)

ENCENDIDA = "encendida"
APAGADA = "apagada"
OBLIGATORIA = "obligatoria"


class NoSePuedeApagar(Exception):
    """Se intentó apagar una regla que no es opcional."""


def _leer(ruta):
    try:
        with io.open(ruta, encoding="utf-8", errors="replace") as abierto:
            return abierto.read()
    except OSError:
        return ""


def opcionales(raiz_del_estandar):
    """Los identificadores de las reglas que un proyecto puede apagar.

    Se recorre `base/` y se juntan las dos formas en que el estándar marca lo
    opcional. **Una regla que no aparezca acá es obligatoria**, y esa es la
    respuesta segura: ante la duda, no se puede apagar.
    """
    base = os.path.join(str(raiz_del_estandar), "base")
    sueltas = set()
    for carpeta, _dirs, archivos in os.walk(base):
        for nombre in archivos:
            if not nombre.endswith(".md"):
                continue
            texto = _leer(os.path.join(carpeta, nombre))
            if not texto:
                continue
            cabecera = texto.split("\n\n", 1)[0]
            capitulo_entero = bool(_CAPITULO_OPT_IN.search(cabecera))
            for identificador, titulo in _ID_DE_REGLA.findall(texto):
                if capitulo_entero or _OPT_IN.search(titulo):
                    sueltas.add(identificador)
            for identificador, resto in _FILA_DE_INDICE.findall(texto):
                if capitulo_entero or _OPT_IN.search(resto):
                    sueltas.add(identificador)
    return sueltas


def _ruta(raiz_del_proyecto):
    return os.path.join(str(raiz_del_proyecto), CARPETA, ARCHIVO)


def _molde(proyecto):
    return (u"# Qué rige en %s\n"
            u"\n"
            u"Lo escrito acá lo lee el agente al abrir sesión. **Solo se pueden "
            u"apagar las reglas que el estándar marca `*opt-in*`**; las demás "
            u"rigen siempre y no aparecen en esta lista.\n"
            u"\n"
            u"| Regla | Estado | Desde | Quién |\n"
            u"|---|---|---|---|\n" % proyecto)


_FILA = re.compile(
    r"^\|\s*`?([A-Z]+\d+(?:\.\d+)?)`?\s*\|\s*(encendida|apagada)\s*\|"
    r"\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*$", re.M | re.I)


def de_un_proyecto(raiz_del_proyecto):
    """Lo que ese proyecto tiene configurado. `{}` si no configuró nada.

    **Un proyecto sin archivo no es un proyecto sin reglas**: es uno donde rige
    todo lo obligatorio y ninguna opcional, que es el arranque de fábrica.
    """
    texto = _leer(_ruta(raiz_del_proyecto))
    puesto = {}
    for identificador, estado, desde, quien in _FILA.findall(texto):
        puesto[identificador] = {"estado": estado.lower(), "desde": desde,
                                 "quien": quien}
    return puesto


def rige(raiz_del_proyecto, identificador, raiz_del_estandar):
    """¿Esa regla rige en ese proyecto? Devuelve `(sí_o_no, por_qué)`."""
    if identificador not in opcionales(raiz_del_estandar):
        return True, "es obligatoria: no se puede apagar"
    puesto = de_un_proyecto(raiz_del_proyecto).get(identificador)
    if not puesto:
        return False, ("es opcional y este proyecto no la encendió: de fábrica, "
                       "lo opcional viene apagado")
    if puesto["estado"] == ENCENDIDA:
        return True, "encendida el %s por %s" % (puesto["desde"], puesto["quien"])
    return False, "apagada el %s por %s" % (puesto["desde"], puesto["quien"])


def poner(raiz_del_proyecto, identificador, estado, raiz_del_estandar,
          cuando, quien="el usuario", proyecto="", sesion=""):
    """Enciende o apaga una regla opcional en un proyecto. Devuelve la fila.

    Apagar una obligatoria **no se hace y se dice por qué**: es la exigencia de
    la funcionalidad, no un detalle de la implementación.
    """
    if estado not in (ENCENDIDA, APAGADA):
        raise NoSePuedeApagar(
            "el estado es «%s» o «%s», y llegó %r" % (ENCENDIDA, APAGADA, estado))
    if identificador not in opcionales(raiz_del_estandar):
        raise NoSePuedeApagar(
            "%s no es opcional: el estándar solo deja apagar las que marca "
            "`*opt-in*`. Apagar una obligatoria volvería el estándar una "
            "sugerencia" % identificador)

    ruta = _ruta(raiz_del_proyecto)

    def escribir(_comprobante):
        texto = _leer(ruta) or _molde(proyecto or os.path.basename(
            str(raiz_del_proyecto)))
        fila = u"| `%s` | %s | %s | %s |\n" % (identificador, estado, cuando,
                                               quien)
        # Se reemplaza la fila anterior si la había; **nunca se borra la
        # historia del archivo**, porque el control de versiones la guarda.
        anterior = re.compile(
            u"^\\|\\s*`?%s`?\\s*\\|[^\n]*\n" % re.escape(identificador), re.M)
        texto = anterior.sub(u"", texto)
        if not texto.endswith(u"\n"):
            texto += u"\n"
        texto += fila
        carpeta = os.path.dirname(ruta)
        if not os.path.isdir(carpeta):
            os.makedirs(carpeta)
        with io.open(ruta, "w", encoding="utf-8", newline="") as abierto:
            abierto.write(texto)
        return {"regla": identificador, "estado": estado, "desde": cuando,
                "quien": quien, "ruta": ruta}

    return con_constancia(
        escribir,
        que_se_hizo="poner una regla opcional en %s" % estado,
        sobre_que=identificador, quien=quien, proyecto=proyecto, sesion=sesion,
        que_cambio="en %s" % os.path.join(CARPETA, ARCHIVO))


def para_el_agente(raiz_del_proyecto, raiz_del_estandar):
    """Lo que se le entrega al agente al abrir: qué rige y qué no, de ESTE.

    **De este proyecto y de ninguno más.** Se arma leyendo su propio archivo; no
    hay estado compartido entre proyectos que pueda filtrarse de uno a otro.
    """
    todas_las_opcionales = opcionales(raiz_del_estandar)
    puesto = de_un_proyecto(raiz_del_proyecto)
    encendidas = sorted(uno for uno in todas_las_opcionales
                        if puesto.get(uno, {}).get("estado") == ENCENDIDA)
    apagadas = sorted(todas_las_opcionales - set(encendidas))
    return {
        "encendidas": encendidas,
        "apagadas": apagadas,
        "cuantas_opcionales": len(todas_las_opcionales),
        "configuro": bool(puesto),
    }


def dicho(entregado):
    """La frase para la consola."""
    if not entregado["configuro"]:
        return ("Este proyecto no configuró nada: rige todo lo obligatorio y "
                "ninguna de las %d opcionales." % entregado["cuantas_opcionales"])
    return "De %d reglas opcionales, este proyecto encendió %d." % (
        entregado["cuantas_opcionales"], len(entregado["encendidas"]))
