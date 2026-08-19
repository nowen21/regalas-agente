#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Coherencia interna del estándar: enlaces rotos e índices desactualizados.

Este validador corre sobre ESTE repositorio (el estándar), no sobre un proyecto
que lo use. Es el único que puede correr sin nada más.
"""
import os
from urllib.parse import unquote

import comun
from comun import (AVISO, FALLA, Hallazgo, RAIZ, enlaces, leer, recorrer_md,
                   relativo)

# Carpeta de transcripciones: se escribe sola y copia el diálogo literal.
HISTORICO = "historico-chat"

# Carpetas cuyo README.md debe listar todos sus .md.
#
# El histórico entra aquí aunque nadie lo escriba a mano: una sesión que no está
# en el índice es una sesión que la siguiente no va a encontrar — y el índice es
# lo único que se le carga al agente al arrancar. La línea la pone el enganche
# al crear el archivo; esto detecta la que se perdió o quedó vieja tras un
# renombre.
CON_INDICE = ["pendientes", "notas", HISTORICO]

# Los resúmenes se indexan en dos niveles: cada día lista sus sesiones, y el
# índice de arriba lista los días. `validar_indices` solo mira archivos, así
# que el de los días —que lista **carpetas**— necesita su propia comprobación.
RESUMENES = HISTORICO + "/resumenes"

EXTERNOS = ("http://", "https://", "mailto:", "ftp://", "//")

# Las plantillas citan las reglas con este marcador delante, y no con `../base/`.
# Tienen que hacerlo: la plantilla se copia dentro de un proyecto, y allá
# `../base/` es la carpeta que está encima del proyecto — nunca el estándar.
# `instalar.py` lo reemplaza por la ruta real al instalar.
MARCADOR_RAIZ = "«RUTA-ESTANDAR»"

# Y cuando todavía está sin llenar, se resuelve contra la carpeta donde vive el
# estándar — que es la de este archivo —, **no** contra la que se está
# validando. No es lo mismo: los enganches corren este programa desde el
# estándar y le pasan el proyecto como `--raiz`, así que dentro de un proyecto
# la raíz validada no es el estándar y el marcador apuntaría a
# `<proyecto>/base/…`, una carpeta que nunca existe. Corriendo sobre el propio
# estándar las dos coinciden y el resultado es el mismo; la diferencia aparece
# justo donde importa.
ESTANDAR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _es_interno(destino):
    return not (destino.startswith(EXTERNOS) or destino.startswith("#"))


def _comprobable(texto, destino):
    """¿Este enlace se puede comprobar contra el disco?

    Se descartan dos cosas, y por razones distintas:

    - Los que llevan `<...>` en el texto o el destino: son ejemplos de formato
      dentro de la documentación (`[<ruta legible>](<path-relativo>.md)`),
      no enlaces a nada.
    - Los que no apuntan a un `.md` ni a una carpeta: apuntan a código de un
      proyecto (`app/PagoService.php`), que por diseño no vive en este
      repositorio. Comprobarlos sería exigir que el estándar contenga los
      proyectos que lo usan.
    """
    if "<" in texto or ">" in texto or "<" in destino or ">" in destino:
        return False
    ruta = destino.split("#", 1)[0]
    return ruta.lower().endswith(".md") or ruta.endswith("/")


def _es_transcripcion(archivo):
    """¿Es una sesión de `historico-chat/`, y no su índice?

    Esos archivos los escribe el enganche del histórico copiando el diálogo
    **literal**, y en el chat los enlaces se escriben relativos a la raíz del
    proyecto (`validadores/README.md`), no a la carpeta donde termina la copia.
    Se rompen por definición.

    La alternativa sería reescribirlos al copiar, y eso ya no sería literal: el
    histórico dejaría de ser prueba de lo que se dijo. Se prefiere no comprobar.
    El `README.md` de la carpeta sí se comprueba — ese lo escribe una persona.
    """
    return (os.path.basename(os.path.dirname(archivo)) == HISTORICO
            and os.path.basename(archivo).lower() != "readme.md")


def validar_enlaces(raiz=None):
    """Todo enlace comprobable de un .md apunta a algo que existe."""
    raiz = raiz or RAIZ
    hallazgos = []

    for archivo in recorrer_md(raiz):
        if _es_transcripcion(archivo):
            continue
        carpeta = os.path.dirname(archivo)
        for n, texto, destino in enlaces(leer(archivo)):
            if not _es_interno(destino) or not _comprobable(texto, destino):
                continue
            # El ancla (#seccion) no se comprueba, solo el archivo.
            #
            # `33 · 1` · El `unquote` no es cosmético: un enlace a un archivo
            # cuyo nombre lleva espacios se escribe con `%20`, y sin
            # decodificarlo se busca en disco un archivo que nadie llamó así.
            # Se reportaba roto con el archivo delante.
            ruta = unquote(destino.split("#", 1)[0])
            if not ruta:
                continue
            if ruta.startswith(MARCADOR_RAIZ):
                base = ESTANDAR
                ruta = ruta[len(MARCADOR_RAIZ):].lstrip("/")
            else:
                base = carpeta
            objetivo = os.path.normpath(os.path.join(base, ruta))
            if not os.path.exists(objetivo):
                hallazgos.append(Hallazgo(
                    FALLA, archivo, n, f"enlace roto: {destino}"))

    return hallazgos


def _ruta_desde_raiz(raiz, archivo, destino):
    """La ruta del destino contada desde la raíz, que es lo que `DOC14` pide
    como texto del enlace."""
    objetivo = os.path.normpath(
        os.path.join(os.path.dirname(archivo), destino.split("#", 1)[0]))
    return os.path.relpath(objetivo, raiz).replace("\\", "/")


def validar_formato(raiz=None):
    """`13·DOC14`: el texto del enlace es la ruta completa desde la raíz.

    Solo se mira el enlace cuyo texto **ya tiene forma de ruta** — lleva `/` o
    termina en `.md`. Ese es el caso que la regla resuelve: el que dice dónde
    vive algo, pero lo dice mal. El enlace de texto descriptivo (`[la guía]`) no
    se toca: la propia regla lo permite cuando quien lee ya sabe dónde vive, y
    marcarlo llenaría de ruido todo documento del proyecto.
    """
    raiz = raiz or RAIZ
    hallazgos = []

    for archivo in recorrer_md(raiz):
        if _es_transcripcion(archivo):
            continue
        for n, texto, destino in enlaces(leer(archivo)):
            # El mismo criterio que `reparar_formato`, y a propósito: si el
            # que reporta y el que arregla miran distinto, el arreglo deja
            # hallazgos vivos o toca lo que nadie reportó.
            esperado = _texto_esperado(raiz, archivo, texto, destino)
            if esperado is None:
                continue
            hallazgos.append(Hallazgo(
                AVISO, archivo, n,
                f"el texto del enlace dice «{texto.strip().strip('`').strip()}» "
                f"y el destino es «{esperado}» — DOC14 pide la ruta desde la raíz"))
    return hallazgos


PROMPTS = "prompts"


def _es_del_usuario(raiz, archivo):
    """Lo que está en `prompts/` son palabras del usuario, copiadas como las dijo.

    Reescribirle un enlace ahí es editarle la frase. Se deja como está, y se
    dice: es una exclusión declarada, no un archivo que se olvidó.

    Se cuenta contra la raíz **que se recibe**, no contra la del repositorio:
    si no, sobre un árbol de prueba la exclusión no reconoce nada y se acaba
    escribiendo justo donde no se debe.
    """
    rel = os.path.relpath(archivo, raiz).replace("\\", "/")
    return rel.split("/")[0] == PROMPTS


def _texto_esperado(raiz, archivo, texto, destino):
    """El texto que `DOC14` pide para ese enlace, o `None` si ya está bien.

    Devuelve `None` en los tres casos que la regla **no** cubre: el enlace
    externo, el de texto descriptivo —`[la guía]`, que la propia regla
    permite— y el que ya dice la ruta desde la raíz.
    """
    if not _es_interno(destino) or not _comprobable(texto, destino):
        return None
    limpio = texto.strip().strip("`").strip()
    if "/" not in limpio and not limpio.lower().endswith(".md"):
        return None                     # texto descriptivo: no se toca
    esperado = _ruta_desde_raiz(raiz, archivo, destino)
    if limpio.lstrip("./").rstrip("/") == esperado.rstrip("/"):
        return None
    if limpio.endswith("/"):
        esperado = esperado.rstrip("/") + "/"
    return esperado


def _es_vecino(destino):
    """Si el enlace apunta a un archivo de la **misma carpeta**.

    `DOC14` pide la ruta desde la raíz *«para saber dónde vive sin abrirlo»*.
    Para el vecino ese propósito ya está cumplido —quien lee está parado ahí—
    y exigirla igual produce un texto de unos 130 caracteres para nombrar el
    archivo de al lado.

    **La regla no distingue el caso**, y decidir si lo distingue es del
    usuario. Mientras tanto se reparan los otros, que son los que la regla
    resuelve de verdad.
    """
    ruta = destino.split("#", 1)[0]
    return bool(ruta) and "/" not in ruta and not ruta.startswith(".")


def reparar_texto(contenido, archivo, raiz=None, incluir_vecinos=False):
    """El arreglo de `DOC14` sobre **un texto en memoria**. `(texto, cuántos)`.

    Existe porque quien **mueve** un archivo cambia el destino de cada enlace
    que lo citaba, y el texto que lo nombraba queda diciendo dónde vivía antes.
    `cerrar.py` la llama en el mismo paso, para no dejar atrás lo que acaba de
    desordenar: sin esto el desajuste aparecía dos cierres después, en la suite,
    lejos de lo que lo causó.

    **Respeta las mismas exclusiones** que `reparar_formato` —transcripción del
    chat, palabras del usuario, vecino de la misma carpeta— porque son la misma
    decisión y separarlas es como se desincronizan.
    """
    raiz = raiz or RAIZ
    if _es_transcripcion(archivo) or _es_del_usuario(raiz, archivo):
        return contenido, 0

    cambios = []
    for _n, texto, destino in enlaces(contenido):
        if not incluir_vecinos and _es_vecino(destino):
            continue
        esperado = _texto_esperado(raiz, archivo, texto, destino)
        if esperado is not None:
            cambios.append((f"[{texto}]({destino})", f"[{esperado}]({destino})"))

    for viejo, nuevo in cambios:
        contenido = contenido.replace(viejo, nuevo)
    return contenido, len(cambios)


def reparar_formato(raiz=None, escribir=False, incluir_vecinos=False):
    """Reescribe el **texto** de los enlaces para que diga la ruta desde la raíz.

    `13·DOC14` pide dos partes: el texto dice dónde vive el archivo y el
    destino lleva a él. El destino **no se toca** — ya funciona, y tocarlo es
    la única forma de romper un enlace que hoy anda.

    **Lo mecánico es el arreglo, no la decisión.** El validador ya calcula,
    enlace por enlace, qué texto corresponde; lo que faltaba era escribirlo.
    Hacerlo a mano sobre mil enlaces es como se cometen los errores que este
    arreglo viene a quitar.

    **El vecino de la misma carpeta se deja fuera por defecto** — ver
    `_es_vecino`. Son 747 de los 1031, y son justo los que la regla no
    resuelve: exigirles la ruta desde la raíz da un texto de 130 caracteres
    para nombrar el archivo de al lado.

    Devuelve `[(archivo, cuántos)]`, y sin `escribir` solo simula.
    """
    raiz = raiz or RAIZ
    tocados = []

    for archivo in recorrer_md(raiz):
        if _es_transcripcion(archivo) or _es_del_usuario(raiz, archivo):
            continue                    # literales del chat · palabras del usuario
        original = leer(archivo)
        cambios = []
        for n, texto, destino in enlaces(original):
            if not incluir_vecinos and _es_vecino(destino):
                continue
            esperado = _texto_esperado(raiz, archivo, texto, destino)
            if esperado is None:
                continue
            cambios.append((f"[{texto}]({destino})", f"[{esperado}]({destino})"))
        if not cambios:
            continue
        texto_nuevo = original
        for viejo, nuevo in cambios:
            texto_nuevo = texto_nuevo.replace(viejo, nuevo)
        if escribir:
            with open(archivo, "w", encoding="utf-8", newline="\n") as f:
                f.write(texto_nuevo)
        tocados.append((archivo, len(cambios)))
    return tocados


def validar_dias_con_resumen(raiz=None):
    """`32` · Cada carpeta de día aparece en el índice de días, y al revés.

    El enganche crea la carpeta del día y el resumen dentro. Si además no
    escribe la línea, el resumen existe y nadie lo va a abrir — que es
    exactamente el defecto que el resumen existe para arreglar. Pasó con el
    2026-08-15, que tuvo dos resúmenes sin una sola mención.

    Se comprueba en los dos sentidos, como el índice de archivos: la carpeta
    que no está nombrada, y el día nombrado cuya carpeta ya no existe.
    """
    raiz = raiz or RAIZ
    carpeta = os.path.join(raiz, *RESUMENES.split("/"))
    indice = os.path.join(carpeta, "README.md")
    if not os.path.isfile(indice):
        return []

    texto = leer(indice)
    hallazgos = []
    dias = sorted(d for d in os.listdir(carpeta)
                  if os.path.isdir(os.path.join(carpeta, d)))

    for dia in dias:
        if f"({dia}/)" not in texto:
            hallazgos.append(Hallazgo(
                FALLA, indice, 0,
                f"el índice de días no menciona {dia}/ — sus resúmenes existen "
                f"y nadie los va a encontrar"))

    for _n, _t, destino in enlaces(texto):
        d = destino.rstrip("/")
        if "/" in d or not d[:4].isdigit():
            continue
        if d not in dias:
            hallazgos.append(Hallazgo(
                AVISO, indice, 0,
                f"el índice de días menciona {d}/, que ya no existe"))

    return hallazgos


def validar_indices(raiz=None, carpetas=None):
    """Cada .md de una carpeta con índice está enlazado desde su README."""
    raiz = raiz or RAIZ
    hallazgos = []

    for nombre in (carpetas or CON_INDICE):
        carpeta = os.path.join(raiz, nombre)
        indice = os.path.join(carpeta, "README.md")
        if not os.path.isfile(indice):
            continue

        texto = leer(indice)
        enlazados = {
            os.path.normpath(os.path.join(carpeta, d.split("#", 1)[0]))
            for _, _, d in enlaces(texto) if _es_interno(d)
        }

        for archivo in sorted(os.listdir(carpeta)):
            if not archivo.lower().endswith(".md") or archivo == "README.md":
                continue
            ruta = os.path.normpath(os.path.join(carpeta, archivo))
            if ruta not in enlazados:
                hallazgos.append(Hallazgo(
                    FALLA, indice, 0,
                    f"el índice no menciona {relativo(ruta)}"))

        # Y al revés: el índice no apunta a archivos que ya no existen.
        # (los enlaces rotos ya los detecta validar_enlaces; aquí solo se
        #  avisa de huérfanos dentro de la propia carpeta)
        for ruta in sorted(enlazados):
            if (os.path.dirname(ruta) == os.path.normpath(carpeta)
                    and not os.path.exists(ruta)):
                hallazgos.append(Hallazgo(
                    AVISO, indice, 0,
                    f"el índice menciona {relativo(ruta)}, que ya no existe"))

    return hallazgos


if __name__ == "__main__":
    # `53` · Un modulo que se ejecuta solo y no imprime nada dice, con su
    # silencio, lo mismo que diria si hubiera comprobado y estuviera todo bien.
    comun.no_es_punto_de_entrada("estandar")
