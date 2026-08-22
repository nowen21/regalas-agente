#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La numeración de `pendientes/` — EP-004 · HU-018.

Un pendiente se numera por el orden en que conviene ejecutarlo, y su número
**no se reutiliza nunca**: los huecos son historia y los pendientes se citan
entre sí por número. Abrir uno con un número ya tomado rompe esas citas sin
que nadie se entere, porque los dos archivos existen y ninguno se pisa.

Esto comprueba tres cosas:

1. **Cuál es el próximo número libre**, para no tener que mirar la carpeta.
2. **Que ningún número esté repetido**, contando también los cerrados de
   `hecho/`: un número liberado por cerrarse sigue tomado.
3. **Que la carpeta y el índice digan lo mismo**, en los dos sentidos.

    python validadores/validar.py pendientes
"""
import os
import re

import comun
from comun import AVISO, FALLA, Hallazgo

CARPETA = "pendientes"
CERRADOS = "hecho"
INDICE = "README.md"

# `07-persona-no-admite-homonimos.md` → 7. Los ceros a la izquierda no cambian
# el número: `07` y `7` son el mismo, y tenerlos como dos distintos dejaría
# pasar justo el choque que esto busca.
_NUMERADO = re.compile(r"^(\d+)-(.+)\.md$")


def _leer(ruta):
    """El texto del archivo, o "" si no está o no se puede leer.

    **Desde el 2026-08-22 es `comun.leer`**, que es lo que esta función quería
    desde el principio: hasta entonces la lectura común reventaba con el
    archivo ausente o mal codificado, y esta comprobación tiene que poder
    correr sobre una carpeta de pendientes que todavía no tiene índice. Era el
    defecto `D-01` de la fase `A-EP-004-HU-003`, arreglado en su fase `B`.
    """
    return comun.leer(ruta)


# `EP-004·HU-016` · La ficha de cabecera de un pendiente, sus dos filas.
#
# **Por qué una fila y no una sección.** Una sección se olvida sin dejar rastro;
# una fila de la ficha se ve vacía. Es la decisión 27 del pendiente 59, tomada
# con el dato a la vista: solo **1 de 35** archivos de `hecho/` la llevaba.
_FILA_HISTORIA = re.compile(r"^\|\s*\*\*Historia de usuario\*\*\s*\|(.+?)\|\s*$", re.M)
_FILA_FASE = re.compile(r"^\|\s*\*\*Fase\*\*\s*\|(.+?)\|\s*$", re.M)

# Una fase se nombra `X-EP-NNN-HU-NNN-...` (`02·F12`, punto 6).
_NOMBRE_FASE = re.compile(r"\b([A-Z]-EP-\d{3}-HU-\d{3}-[\w\-]+)")

# `EP-004·HU-016` · **Desde cuándo se exige.** Es la decisión 26 del pendiente
# 59: desde el 2026-08-16, que es cuando nació la exigencia. Lo cerrado antes no
# se reabre, igual que `20·M10` hace con cualquier norma nueva.
CORTE = "2026-08-16"

# Lo que se cierra **sin construir nada**: una decisión, una medición que dio en
# cero, un duplicado. No tuvo fase porque no hubo desarrollo, y exigirle una
# obligaría a inventarla.
_SIN_FASE = re.compile(
    r"(?i)cerrad[oa] por decisión|no hubo (?:que )?constru|"
    r"sin fase porque|no fue desarrollo|se cerró sin construir")


def _fecha_de_cierre(texto):
    """La fecha que el propio pendiente declara al cerrarse, o "" si no dice."""
    m = re.search(r"(?i)\*\*hecho\*\*[^\n]*?(\d{4}-\d{2}-\d{2})", texto)
    if m:
        return m.group(1)
    m = re.search(r"(?i)cerrad[oa][^\n]*?(\d{4}-\d{2}-\d{2})", texto)
    return m.group(1) if m else ""


def cerrado_declara_su_fase(raiz):
    """`CA-01` · un pendiente cerrado dice en qué fase se hizo.

    **Aviso, no falla.** Que falte la fila no rompe nada hoy: dice que la
    trazabilidad hacia abajo se cortó. Detener la corrida por un pendiente
    viejo sería un obstáculo permanente, y eso se apaga.
    """
    carpeta = os.path.join(raiz, CARPETA, "hecho")
    if not os.path.isdir(carpeta):
        return []
    hallazgos = []
    for nombre in sorted(os.listdir(carpeta)):
        if not nombre.lower().endswith(".md") or nombre.upper() == "README.MD":
            continue
        ruta = os.path.join(carpeta, nombre)
        texto = _leer(ruta)
        fecha = _fecha_de_cierre(texto)
        # **Sin fecha declarada se deja pasar**, y es a propósito: la exigencia
        # nació el 2026-08-16 y lo cerrado antes no se reabre. Los pendientes
        # viejos no declaran fecha de cierre, así que exigirles la fase sería
        # aplicar hacia atrás una norma nueva — y treinta avisos que nunca se
        # van apagan la comprobación entera.
        if not fecha or fecha < CORTE:
            continue
        if _SIN_FASE.search(texto):
            continue                       # no hubo desarrollo: no hay fase
        fases = _NOMBRE_FASE.findall(texto)
        if not fases:
            hallazgos.append(Hallazgo(
                AVISO, ruta, 0,
                "no dice en qué fase se hizo — un pendiente cerrado sin su fase "
                "corta la trazabilidad hacia abajo (EP-004·HU-016)"))
            continue
        for fase in sorted(set(fases)):
            if not _existe_la_fase(raiz, fase):
                hallazgos.append(Hallazgo(
                    AVISO, ruta, 0,
                    f"nombra la fase `{fase}`, que no existe en "
                    f"`documentacion/epicas/` — o se renombró, o nunca estuvo"))
    return hallazgos


def _existe_la_fase(raiz, nombre):
    epicas = os.path.join(raiz, "documentacion", "epicas")
    for actual, carpetas, _ in os.walk(epicas):
        if nombre in carpetas:
            return True
    return False


def abierto_nombra_su_historia(raiz):
    """`CA-02` · un pendiente abierto dice a qué historia baja.

    **Falla, no aviso.** Un pendiente abierto sin historia no se puede
    ejecutar: `02·F23` manda bajarlo a fase de una historia, y sin ella nadie
    sabe de cuál. El enrutamiento del 2026-08-17 dejó las 33 con la suya, y
    esto es lo que impide que la 34 nazca sin ella.
    """
    carpeta = os.path.join(raiz, CARPETA)
    if not os.path.isdir(carpeta):
        return []
    hallazgos = []
    for nombre in sorted(os.listdir(carpeta)):
        if not re.match(r"^\d+-.+\.md$", nombre, re.I):
            continue
        ruta = os.path.join(carpeta, nombre)
        texto = _leer(ruta)
        m = _FILA_HISTORIA.search(texto)
        if not m:
            hallazgos.append(Hallazgo(
                FALLA, ruta, 0,
                "no trae la fila **Historia de usuario** en su ficha — sin ella "
                "nadie sabe a qué historia baja este pendiente (02·F23)"))
            continue
        dicho = m.group(1).strip()
        if not dicho or dicho in ("—", "-"):
            hallazgos.append(Hallazgo(
                FALLA, ruta, 0,
                "la fila **Historia de usuario** está vacía — o nombra la "
                "historia, o dice por qué todavía no tiene"))
    return hallazgos


def _archivos(carpeta):
    if not os.path.isdir(carpeta):
        return []
    return sorted(n for n in os.listdir(carpeta)
                  if n.endswith(".md") and n != INDICE
                  and os.path.isfile(os.path.join(carpeta, n)))


def numerados(proyecto):
    """`{numero: [nombres]}` de los archivos numerados de la carpeta."""
    raiz = os.path.join(os.path.abspath(proyecto), CARPETA)
    encontrados = {}
    for carpeta in (raiz, os.path.join(raiz, CERRADOS)):
        for nombre in _archivos(carpeta):
            m = _NUMERADO.match(nombre)
            if m:
                encontrados.setdefault(int(m.group(1)), []).append(nombre)
    return encontrados


def numeros_del_indice(proyecto):
    """Los números que el índice registra, **incluidos los cerrados**.

    Es la única memoria completa de la numeración. Al cerrar un pendiente su
    archivo se mueve a `hecho/` y **pierde el número** —`02-vigencia…md` pasa a
    `vigencia-y-poda-de-memoria.md`—, así que mirando solo la carpeta el 02
    parece libre. Lo que lo conserva es la fila tachada del índice: `~~02~~`.
    """
    indice = _leer(os.path.join(os.path.abspath(proyecto), CARPETA, INDICE))
    return {int(n) for n in re.findall(r"^\|\s*~*(\d+)~*\s*\|", indice, re.M)}


def tomados(proyecto):
    """Todos los números que **no se pueden reutilizar**: los de la carpeta y
    los que el índice recuerda de los ya cerrados."""
    return set(numerados(proyecto)) | numeros_del_indice(proyecto)


def sin_numero(proyecto):
    """Los `.md` de `pendientes/` que no empiezan por un número."""
    raiz = os.path.join(os.path.abspath(proyecto), CARPETA)
    return [n for n in _archivos(raiz) if not _NUMERADO.match(n)]


def proximo_libre(proyecto):
    """El siguiente número que se puede usar sin pisar a nadie.

    **El siguiente al mayor, no el primer hueco.** El índice dice que «el
    número no se reutiliza ni se renumeran los demás: los huecos son historia»,
    y los pendientes se citan entre sí por número. Entregar un hueco haría que
    «el 02» apuntara a dos cosas distintas según cuándo se leyera.
    """
    ocupados = tomados(proyecto)
    return max(ocupados) + 1 if ocupados else 1


# `02·F24` · El pendiente que nace de un proyecto lo nombra.
#
# Sin el nombre no hay trazabilidad entre el estándar, la corrección y el
# proyecto que la espera — y ese proyecto se queda con su pendiente abierto
# para siempre, porque nadie sabe a quién avisarle al cerrar.
#
# Se busca la fila de la ficha, no el texto suelto: un pendiente puede nombrar
# tres proyectos en su prosa y no venir de ninguno.
_DE_UN_PROYECTO = re.compile(
    r"(?im)^\|\s*\*\*Proyecto de origen\*\*\s*\|(.*?)\|\s*$")

# Lo que no es un nombre de proyecto, aunque llene la casilla.
_SIN_PROYECTO = re.compile(
    r"(?i)^\s*(el est[áa]ndar mismo|—|-|n/?a|ninguno|este repositorio)\s*$")


def sin_proyecto_de_origen(proyecto):
    """Los pendientes que dicen venir de un proyecto sin decir de cuál."""
    raiz = os.path.join(os.path.abspath(proyecto), CARPETA)
    salida = []
    for nombre in _archivos(raiz):
        texto = _leer(os.path.join(raiz, nombre))
        m = _DE_UN_PROYECTO.search(texto)
        if not m:
            continue                    # no declara origen: no es de esta regla
        valor = m.group(1).strip().strip("*` ")
        # Vacío o con el marcador de la plantilla sin llenar.
        if not valor or ("«" in valor and "»" in valor):
            salida.append((nombre, "la casilla está vacía"))
    return salida


def validar(proyecto):
    proyecto = os.path.abspath(proyecto)
    raiz = os.path.join(proyecto, CARPETA)
    hallazgos = []

    if not os.path.isdir(raiz):
        return [Hallazgo(FALLA, CARPETA, 0,
                         "no existe la carpeta de pendientes (HU-018)")]

    # CA-02 · el número repetido.
    for numero, nombres in sorted(numerados(proyecto).items()):
        if len(nombres) > 1:
            hallazgos.append(Hallazgo(
                FALLA, f"{CARPETA}/", 0,
                f"el número {numero} está tomado por {len(nombres)} pendientes: "
                + ", ".join(f"`{n}`" for n in nombres)
                + " — un número no se reutiliza (HU-018)"))

    # Transversal de errores · el nombre que no se puede interpretar se
    # reporta y **no detiene**: un archivo suelto no puede invalidar la
    # comprobación de los otros cuarenta.
    for nombre in sin_numero(proyecto):
        hallazgos.append(Hallazgo(
            AVISO, f"{CARPETA}/{nombre}", 0,
            "no empieza por un número, así que no entra en la numeración (HU-018)"))

    # CA-03 · la carpeta y el índice, en los dos sentidos.
    indice = _leer(os.path.join(raiz, INDICE))
    if indice:
        enlazados = set(re.findall(r"\]\(([^)]+\.md)\)", indice))
        propios = {e for e in enlazados if "/" not in e and e != INDICE}
        for nombre in _archivos(raiz):
            if nombre not in propios:
                hallazgos.append(Hallazgo(
                    AVISO, f"{CARPETA}/{nombre}", 0,
                    f"no aparece en `{CARPETA}/{INDICE}` (HU-018)"))
        for nombre in sorted(propios - set(_archivos(raiz))):
            hallazgos.append(Hallazgo(
                AVISO, f"{CARPETA}/{INDICE}", 0,
                f"el índice enlaza `{nombre}`, que no está en la carpeta (HU-018)"))

    # `02·F24` · el proyecto de origen se nombra o no se declara.
    for nombre, motivo in sin_proyecto_de_origen(proyecto):
        hallazgos.append(Hallazgo(
            FALLA, f"{CARPETA}/{nombre}", 0,
            f"declara «Proyecto de origen» y {motivo} — sin el nombre nadie "
            f"sabe a quién avisarle al cerrar, y ese proyecto se queda "
            f"esperando para siempre (02·F24)"))

    # `EP-004·HU-016` · Las dos direcciones de la trazabilidad de un pendiente:
    # hacia arriba (el abierto dice a qué historia baja) y hacia abajo (el
    # cerrado dice en qué fase se hizo).
    hallazgos += abierto_nombra_su_historia(proyecto)
    hallazgos += cerrado_declara_su_fase(proyecto)

    return hallazgos


def linea_proximo(proyecto):
    """La línea que dice el próximo número libre — CA-01."""
    if not os.path.isdir(os.path.join(os.path.abspath(proyecto), CARPETA)):
        return ""
    ocupados = tomados(proyecto)
    abiertos = len(numerados(proyecto))
    return (f"Pendientes: {abiertos} con archivo · {len(ocupados)} números "
            f"tomados · el próximo libre es el {proximo_libre(proyecto):02d} (HU-018)")


if __name__ == "__main__":
    # `53` · Un modulo que se ejecuta solo y no imprime nada dice, con su
    # silencio, lo mismo que diria si hubiera comprobado y estuviera todo bien.
    comun.no_es_punto_de_entrada("pendientes")
