#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enganche `UserPromptSubmit`: recuerda en cada turno las reglas de cada turno.

    python hook_reglas.py --raiz "C:/ruta/del/proyecto"

**Por qué existe.** `hook_sesion.py` carga las reglas una vez, al abrir, y esa
apuesta pierde de dos maneras distintas. Las dos se midieron el 2026-09-15 en
`master-ciberseguridad`:

  - **El paquete puede no entrar.** Pesaba 82,4 KB (62,3 de reglas, 15,6 del
    índice, 3,8 de memoria, 0,7 del histórico) y la herramienta corta la salida
    de un enganche cerca de los 80: la guardó en un archivo y le dejó al agente
    2 KB de vista previa. El banner, mientras tanto, decía «Estándar cargado».
    **El fallo se vio como éxito**, que es lo peor que puede pasarle a un aviso.
  - **Lo que entra se resume primero.** Lo dice `cargador.py` en su propia
    documentación: llenar la ventana adelanta el resumen automático del
    contexto, y lo primero que se resume es justo lo que se inyectó al arrancar.

Así que el volcado grande de una sola vez no alcanza, y este enganche pone lo
que falta: **un recordatorio corto en cada turno**, por el canal que sí llega y
que no se resume.

**Y devuelve la medición.** `hook_redaccion.py` ya cuenta las marcas de lo que
el agente acaba de escribir, pero corre en `Stop` e imprime donde nadie lo ve:
ni el usuario ni el modelo. Acá esa misma cuenta se vuelve a sacar sobre la
respuesta anterior y entra al turno siguiente, que es donde todavía sirve para
corregir. Mide la misma función (`redaccion.linea_de_cierre`), así que las dos
dicen siempre lo mismo.

**No duplica el texto de las reglas.** Del archivo de cada una se saca su
encabezado, y nada más. Si el estándar reescribe una regla, el recordatorio
cambia solo; si la renombra, también. Un resumen escrito a mano acá se
convertiría en una segunda versión de la norma, y la que manda es la del
capítulo (`20·M2`).

**Y recupera las reglas que pide el mensaje.** Del `02` en adelante las reglas
llegan al arranque solo como índice, con la orden de leer el archivo antes de
tocar el tema. Esa orden depende de que el agente se acuerde, y cuando no se
acuerda trabaja sin la regla. `recuperar.py` lee el mensaje y trae el texto
completo de las que ese mensaje pide, con su presupuesto y diciendo por qué
entró cada una.

**El recordatorio va al agente, no a la pantalla.** Es contexto, no alerta: por
eso sale por `additionalContext` en todos los turnos sin cansar a nadie. Por
`systemMessage` sale **solo** la medición, y solo cuando hay algo que decir —
que es la regla de oro de los avisos de esta casa.

Sale siempre con código 0: recordar una regla no puede costarle el turno a
nadie.
"""
import json
import os
import sys

# **Vive en el adaptador, no en `validadores/`.** Por eso tiene que decir
# dónde están los módulos que usa: el trabajo es agnóstico y sigue allá;
# acá sólo está lo que habla con esta herramienta.
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "validadores"))

import historico                                    # noqa: E402
import recuperar                                    # noqa: E402
import redaccion                                    # noqa: E402
from comun import RAIZ, leer, preparar_salida       # noqa: E402

# Las reglas que gobiernan **todos** los turnos, sin importar el tema. No es
# una selección de gusto: son las que hablan de cómo queda escrito cualquier
# mensaje, así que ninguna sesión las puede tener por ajenas.
#
# Cada una se nombra por su archivo y su encabezado. El texto sale de allá.
CADA_TURNO = (
    ("01·C5",  "base/01-conducta.md", "## C5 "),
    ("00·ID8", "base/00-identidad-y-rol/reglas/"
               "ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md",
     "## ID8 "),
    ("00·ID9", "base/00-identidad-y-rol/reglas/"
               "ID9-di-lo-mismo-en-menos-palabras.md", "## ID9 "),
    ("00·ID10", "base/00-identidad-y-rol/reglas/"
                "ID10-escribe-en-el-idioma-del-proyecto-en-tercera-persona-"
                "y-en-infinitivo.md", "## ID10 "),
)

# La lista cerrada que exige `ID8`. Se nombra aparte porque es un anexo y no una
# regla: el recordatorio dice dónde está, y el agente la lee cuando va a
# entregar algo escrito.
ANEXO_ID8 = "base/00-identidad-y-rol/marcadores-de-ia.md"


def opcion(argv, nombre, por_defecto=""):
    if nombre in argv:
        i = argv.index(nombre)
        if i + 1 < len(argv):
            return argv[i + 1]
    return por_defecto


def _entrada():
    """Lo que la herramienta manda por la entrada estándar, o `{}`."""
    try:
        crudo = sys.stdin.buffer.read()
    except (AttributeError, ValueError):
        crudo = (sys.stdin.read() or "").encode("utf-8", "replace")
    try:
        return json.loads(crudo.decode("utf-8", "replace"))
    except (json.JSONDecodeError, ValueError):
        return {}


def _encabezado(estandar, relativo, ancla):
    """La línea de encabezado de una regla, tal como la escribió el estándar.

    Se saca del archivo y no de una copia escrita acá para que no envejezca
    (`20·M2`: el dueño del texto es el capítulo). Si el archivo no está o
    cambió de forma, devuelve `""` y el recordatorio sigue con las demás: un
    recordatorio incompleto sirve más que ninguno.
    """
    ruta = os.path.join(estandar, relativo.replace("/", os.sep))
    if not os.path.isfile(ruta):
        return ""
    try:
        texto = leer(ruta)
    except Exception:                     # noqa: BLE001 — nunca romper el turno
        return ""
    for linea in texto.splitlines():
        if linea.startswith(ancla):
            # Se quita el `## ` del molde y el sello de derogación si lo trae.
            return linea[3:].split("  ·  ")[0].strip()
    return ""


def recordatorio(estandar):
    """El texto corto que entra en cada turno. `""` si no se pudo armar nada."""
    lineas = []
    for cita, relativo, ancla in CADA_TURNO:
        titulo = _encabezado(estandar, relativo, ancla)
        if titulo:
            lineas.append(f"  `{cita}` · {titulo}")
    if not lineas:
        return ""
    return (
        "[LAS REGLAS DE CADA TURNO — RIGEN ESTA RESPUESTA]\n"
        "Se recuerdan acá porque el volcado del arranque puede no haber "
        "entrado, y porque lo que entró es lo primero que el contexto resume.\n"
        + "\n".join(lineas) + "\n"
        f"La lista cerrada que exige `00·ID8`, incluido el español colombiano "
        f"de su sección 5, está en `{ANEXO_ID8}`: se relee **antes** de "
        f"entregar cualquier texto, no después."
    )


def medicion(raiz, entrada):
    """Cómo quedó escrita la respuesta anterior, o `""` si no hay nada que decir.

    Es la misma cuenta de `hook_redaccion.py`, que corre al cerrar el turno y
    la imprime donde nadie la lee. Acá llega **al turno siguiente**, que es
    cuando todavía se puede corregir.
    """
    ruta = entrada.get("transcript_path") or ""
    if not ruta or not os.path.isfile(ruta):
        return ""
    try:
        texto, _marca = historico.ultima_respuesta(ruta)
        if not texto:
            return ""
        return redaccion.linea_de_cierre(texto)
    except Exception:                     # noqa: BLE001 — medir no cuesta el turno
        return ""


def reglas_del_mensaje(entrada):
    """Las reglas que pide este mensaje, o `""`.

    Nunca cuesta el turno: si el recuperador falla, el turno sigue con el
    recordatorio fijo, que es lo que no puede faltar.
    """
    try:
        return recuperar.como_texto(entrada.get("prompt", ""), RAIZ)
    except Exception:                     # noqa: BLE001
        return ""


def main():
    preparar_salida()
    entrada = _entrada()
    raiz = opcion(sys.argv[1:], "--raiz") or entrada.get("cwd") or os.getcwd()
    raiz = os.path.abspath(raiz)

    partes = []
    aviso = recordatorio(RAIZ)
    if aviso:
        partes.append(aviso)

    pedidas = reglas_del_mensaje(entrada)
    if pedidas:
        partes.append(pedidas)

    cuenta = medicion(raiz, entrada)
    if cuenta:
        partes.append(
            f"[LA RESPUESTA ANTERIOR, MEDIDA]\n{cuenta}\n"
            "Corregir eso en esta respuesta, y no volver a entregarlo así.")

    if not partes:
        return 0

    salida = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": "\n\n".join(partes),
        },
    }

    # Por la pantalla del usuario sale **solo** la medición, y solo cuando hay
    # algo que decir. El recordatorio es contexto del agente: como banner en
    # cada turno, se dejaría de leer a los dos días y se llevaría puesto el
    # aviso que sí importaba.
    if cuenta:
        salida["systemMessage"] = cuenta

    print(json.dumps(salida, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
