# -*- coding: utf-8 -*-
"""Lo que se salió de lo acordado — `F-029`.

**Demasiados avisos se vuelven ruido, y el ruido se ignora completo.** Está
escrito en la ficha de `F-029` y no lo arregla el código: lo arregla no inventar
avisos. Por eso son **tres clases** y no quince, y por eso cada una tiene que
poder decir qué la disparó y dónde mirar. Un aviso que no puede decirlo no se
emite.

**«Vencida» hubo que definirla, porque el estándar nunca le puso fecha a una
deuda.** Acá quiere decir *sin moverse hace más de tantos días*, que es lo único
que el texto sabe: la última vez que alguien tocó el `estado-fase.md`. No es lo
mismo que un vencimiento acordado, y por eso se dice en el aviso.

**Un aviso atendido no vuelve porque su causa desapareció.** Para el que se
quiere callar sin arreglarlo hay un archivo en el proyecto —`.agente/avisos-
atendidos.md`—, con qué se calló y por qué. Callar en la base, sin dejar rastro
en el repositorio, sería el aviso que nadie sabe que existió.
"""
import io
import os
import re

from nucleo.ciclo_de_vida import estaciones

CARPETA = ".agente"
ATENDIDOS = "avisos-atendidos.md"

# Cuántos días sin moverse antes de considerarla vencida. Se puede cambiar al
# pedirla: **el número correcto depende del proyecto y no lo sabe la plataforma.**
DIAS = 30

# De más grave a menos. El orden importa: lo primero que se lee es lo que se
# atiende, y lo que queda abajo se ignora.
DETENIDA = "fase detenida"
SIN_FASE = "historia sin fase"
SIN_VERIFICAR = "terminado sin comprobar"

GRAVEDAD = {DETENIDA: 0, SIN_FASE: 1, SIN_VERIFICAR: 2}

# Cuántos se muestran. Un tope callado se lee como «eso es todo lo que hay»
# (`S-113`), así que cuando recorta, lo dice.
TOPE = 50

_HU = re.compile(r"^HU-\d{3}-")
_FILA_ATENDIDO = re.compile(
    r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*$", re.M)
# `| F-019 | Consultar lo registrado | ... | Definida | Sin verificar |`
_DEL_INVENTARIO = re.compile(
    r"^\|\s*(F-\d{3})\s*\|\s*([^|]+?)\s*\|(?:[^|]*\|){3}\s*([^|]+?)\s*\|"
    r"\s*([^|]+?)\s*\|\s*$", re.M)


def _leer(ruta):
    try:
        with io.open(ruta, encoding="utf-8", errors="replace") as abierto:
            return abierto.read()
    except OSError:
        return ""


def atendidos(raiz):
    """Lo que este proyecto decidió callar, con el porqué. `{}` si nada."""
    texto = _leer(os.path.join(str(raiz), CARPETA, ATENDIDOS))
    callados = {}
    for que, cuando, por_que in _FILA_ATENDIDO.findall(texto):
        if que.lower() in ("qué", "que", "aviso"):
            continue
        callados[que.strip("` ")] = {"cuando": cuando, "por_que": por_que}
    return callados


def _aviso(clase, sobre_que, que_lo_disparo, donde_mirar):
    return {"clase": clase, "sobre_que": sobre_que,
            "que_lo_disparo": que_lo_disparo, "donde_mirar": donde_mirar,
            "gravedad": GRAVEDAD[clase]}


def fases_detenidas(raiz, hoy, dias=DIAS):
    """Fases sin cerrar que llevan más de `dias` sin que nadie las toque."""
    salida = []
    for fase in estaciones.de_un_proyecto(str(raiz)):
        if fase["actual"] == estaciones.TERMINADA:
            continue
        quieta = estaciones.detenida_desde(fase, hoy)
        if quieta < 0:
            # **No dice desde cuándo, así que no se sabe.** No se cuenta como
            # vencida ni como al día: se calla, y el módulo Ciclo de vida ya
            # dice cuántas están así.
            continue
        if quieta <= dias:
            continue
        salida.append(_aviso(
            DETENIDA, fase["fase"],
            "lleva %d día(s) sin tocarse, y está en la estación %d · %s"
            % (quieta, fase["actual"], fase["nombre"]),
            os.path.relpath(fase["ruta"], str(raiz))))
    return salida


def historias_sin_fase(raiz):
    """Historias de usuario que no tienen ninguna fase abierta."""
    epicas = os.path.join(str(raiz), "documentacion", "epicas")
    salida = []
    if not os.path.isdir(epicas):
        return salida
    for carpeta_epica in sorted(os.listdir(epicas)):
        dentro = os.path.join(epicas, carpeta_epica)
        if not os.path.isdir(dentro):
            continue
        for carpeta_hu in sorted(os.listdir(dentro)):
            if not _HU.match(carpeta_hu):
                continue
            de_la_hu = os.path.join(dentro, carpeta_hu)
            if not os.path.isdir(de_la_hu):
                continue
            tiene = any(
                os.path.isdir(os.path.join(de_la_hu, uno))
                and os.path.exists(os.path.join(de_la_hu, uno,
                                                "estado-fase.md"))
                for uno in os.listdir(de_la_hu))
            if not tiene:
                salida.append(_aviso(
                    SIN_FASE, carpeta_hu,
                    "está escrita y no tiene ninguna fase que la construya",
                    os.path.join("documentacion", "epicas", carpeta_epica,
                                 carpeta_hu)))
    return salida


def terminado_sin_comprobar(raiz):
    """Funcionalidades construidas que siguen sin verificarse."""
    ruta = os.path.join(str(raiz), "cvds", "analisis-requisitos",
                        "inventario-funcionalidades.md")
    texto = _leer(ruta)
    salida = []
    for identificador, nombre, estado, verificado in _DEL_INVENTARIO.findall(
            texto):
        if estado.strip().lower() != "construida":
            continue
        if verificado.strip().lower() != "sin verificar":
            continue
        salida.append(_aviso(
            SIN_VERIFICAR, identificador,
            "«%s» está construida y sigue sin verificar" % nombre.strip(),
            os.path.join("cvds", "analisis-requisitos",
                         "inventario-funcionalidades.md")))
    return salida


def de_un_proyecto(raiz, hoy, dias=DIAS, tope=TOPE):
    """Todos los avisos, de lo que más duele a lo que menos.

    Devuelve `{"avisos", "cuantos", "callados", "se_recorto", "por_clase"}`.
    """
    todos = (fases_detenidas(raiz, hoy, dias)
             + historias_sin_fase(raiz)
             + terminado_sin_comprobar(raiz))
    callados = atendidos(raiz)
    vivos = [uno for uno in todos if uno["sobre_que"] not in callados]
    vivos.sort(key=lambda uno: (uno["gravedad"], uno["sobre_que"]))

    por_clase = {}
    for uno in vivos:
        por_clase[uno["clase"]] = por_clase.get(uno["clase"], 0) + 1

    return {
        "avisos": vivos[:tope],
        "cuantos": len(vivos),
        "callados": len(todos) - len(vivos),
        "se_recorto": len(vivos) > tope,
        "por_clase": por_clase,
    }


def dicho(salida):
    """La frase de arriba. Un cero se dice; no se deja en blanco."""
    if not salida["cuantos"]:
        frase = "Nada se salió de lo acordado."
        if salida["callados"]:
            frase += (" (Y %d aviso(s) están callados a propósito, en %s.)"
                      % (salida["callados"],
                         os.path.join(CARPETA, ATENDIDOS)))
        return frase
    frase = "%d aviso(s): %s." % (
        salida["cuantos"],
        " · ".join("%d %s" % (cuantos, clase)
                   for clase, cuantos in sorted(salida["por_clase"].items())))
    if salida["callados"]:
        frase += " Y %d callado(s) a propósito." % salida["callados"]
    if salida["se_recorto"]:
        frase += (" Se muestran los primeros %d: **hay más**." % TOPE)
    return frase


def linea(aviso):
    """Un aviso, con lo que lo disparó y dónde mirar. Las dos cosas, siempre."""
    return "%s · %s — %s → %s" % (
        aviso["clase"], aviso["sobre_que"], aviso["que_lo_disparo"],
        aviso["donde_mirar"])
