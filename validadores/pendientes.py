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
    return set(numerados(proyecto)) | numeros_del_indice(proyecto) | set(numeros_nuevos(proyecto))


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

    # `EP-023·HU-003` · Desde la 45.0.0 `pendientes/` es historia: el proyecto
    # nuevo no la tiene, y eso no es una falla.
    hallazgos += forma_nueva(proyecto)

    # CA-02 · el número repetido, en las dos formas. El pendiente que pasó a
    # la forma nueva deja su archivo viejo como historia, con el mismo número
    # y el mismo nombre: es el mismo pendiente, no un choque.
    todos = numerados(proyecto)
    for numero, rutas in numeros_nuevos(proyecto).items():
        for ruta in rutas:
            viejos = todos.get(numero, [])
            if os.path.basename(ruta) + ".md" in viejos:
                continue
            todos.setdefault(numero, []).append(comun.relativo(ruta))
    for numero, nombres in sorted(todos.items()):
        if len(nombres) > 1:
            hallazgos.append(Hallazgo(
                FALLA, f"{CARPETA}/", 0,
                f"el número {numero} está tomado por {len(nombres)} pendientes: "
                + ", ".join(f"`{n}`" for n in nombres)
                + " — un número no se reutiliza (HU-018)"))

    if not os.path.isdir(raiz):
        return hallazgos

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

    # `EP-004·HU-016` · El cerrado dice en qué fase se hizo. La historia a la
    # que baja el abierto ya no se escribe en el pendiente: la decide su
    # análisis (`EP-023·HU-003`, análisis 1 del pendiente 103, conclusión 15).
    hallazgos += cerrado_declara_su_fase(proyecto)

    return hallazgos


# ── `EP-023·HU-003` · La forma nueva ─────────────────────────────────────────
#
# Cada pendiente es una carpeta `NNN-<slug>/` con su `pendiente.md` y sus
# análisis, dentro de una carpeta `pendientes/` de lo que lo origina: una épica,
# una HU o el resumen del día mientras no tiene dueño (análisis 8 del pendiente
# 103, punto 15 de «Lo acordado»). Solo tiene «De dónde sale», «El problema» y
# «Por qué importa»; su estado lo calcula `estado()` siguiendo los enlaces.

# Donde puede vivir una carpeta `pendientes/`.
DONDE = (("documentacion", "epicas"), ("historico-chat", "resumenes"))
INDICE_NUEVO = os.path.join("documentacion", "pendientes.md")

_CARPETA_PENDIENTE = re.compile(r"^(\d+)-[^.]+$")
_ANALISIS = re.compile(r"^analisis-(\d+)\.md$")
_APROBADO = re.compile(r"^> \*\*Aprobado\*\*", re.M)
_COMPROBADO = re.compile(r"^\*\*Comprobado:\*\*\s*\d{4}-\d{2}-\d{2}\s*$", re.M)
_DE_DONDE = re.compile(r"^\|\s*\*\*De dónde sale\*\*\s*\|(.+?)\|\s*$", re.M)
_ENLACE = re.compile(r"\]\(([^)#\s]+)")
# «HU-001» o «HU 1»: el análisis 1 del pendiente 103 escribe la segunda (análisis 15, acuerdo 1).
_HU_EN_TEXTO = re.compile(r"EP-0*(\d+)\D{1,40}?HU[- ]0*(\d+)")
_FILA = re.compile(r"^\| *\d+ *\|(.*)\|\s*$", re.M)
_PARTES = (("De dónde sale", re.compile(r"^\|\s*\*\*De dónde sale\*\*\s*\|", re.M)),
           ("El problema", re.compile(r"^## El problema\s*$", re.M)),
           ("Por qué importa", re.compile(r"^## Por qué importa\s*$", re.M)))


def carpetas(proyecto):
    """Las carpetas de pendiente de la forma nueva: `[ruta absoluta]`."""
    proyecto = os.path.abspath(proyecto)
    salida = []
    for partes in DONDE:
        base = os.path.join(proyecto, *partes)
        for actual, subcarpetas, archivos in os.walk(base):
            subcarpetas[:] = [s for s in subcarpetas if not s.startswith(".")]
            if "pendiente.md" in archivos and _CARPETA_PENDIENTE.match(os.path.basename(actual)):
                salida.append(actual)
    return sorted(salida)


def numeros_nuevos(proyecto):
    """`{numero: [carpetas]}` de los pendientes de la forma nueva."""
    salida = {}
    for carpeta in carpetas(proyecto):
        numero = int(_CARPETA_PENDIENTE.match(os.path.basename(carpeta)).group(1))
        salida.setdefault(numero, []).append(carpeta)
    return salida


def forma_nueva(proyecto):
    """`CA-03` · el pendiente de la forma nueva trae sus tres partes, y vive en `pendientes/`."""
    hallazgos = []
    for carpeta in carpetas(proyecto):
        ruta = os.path.join(carpeta, "pendiente.md")
        texto = _leer(ruta)
        faltan = [nombre for nombre, patron in _PARTES if not patron.search(texto)]
        if faltan:
            hallazgos.append(Hallazgo(
                FALLA, ruta, 0,
                "le falta " + ", ".join(f"«{f}»" for f in faltan)
                + " — un pendiente trae de dónde sale, el problema y por qué importa (EP-023·HU-003)"))
        if os.path.basename(os.path.dirname(carpeta)) != CARPETA:
            hallazgos.append(Hallazgo(
                AVISO, carpeta, 0,
                "no está dentro de una carpeta `pendientes/` de lo que lo origina (EP-023·HU-003)"))
    return hallazgos


def _destino(enlace, desde):
    """La ruta a la que lleva un enlace relativo escrito en `desde`."""
    return os.path.normpath(os.path.join(os.path.dirname(desde), enlace.replace("/", os.sep)))


def padre(carpeta):
    """El pendiente que enlaza su «De dónde sale», si es otro pendiente: su carpeta, o ""."""
    ruta = os.path.join(carpeta, "pendiente.md")
    m = _DE_DONDE.search(_leer(ruta))
    if not m:
        return ""
    for enlace in _ENLACE.findall(m.group(1)):
        destino = _destino(enlace, ruta)
        if os.path.basename(destino) == "pendiente.md":
            destino = os.path.dirname(destino)
        if os.path.isfile(os.path.join(destino, "pendiente.md")) and \
                os.path.normcase(destino) != os.path.normcase(carpeta):
            return destino
    return ""


def analisis_de(carpeta):
    """Los `analisis-N.md` de la carpeta, en orden."""
    nombres = [n for n in os.listdir(carpeta) if _ANALISIS.match(n)] if os.path.isdir(carpeta) else []
    return [os.path.join(carpeta, n) for n in sorted(nombres, key=lambda n: int(_ANALISIS.match(n).group(1)))]


def _hu_terminada(ruta):
    return bool(re.search(r"^\|\s*\*\*Estado\*\*\s*\|\s*Terminada", _leer(ruta), re.M))


def _hu_por_numero(proyecto, epica, hu):
    base = os.path.join(proyecto, "documentacion", "epicas")
    if not os.path.isdir(base):
        return ""
    for e in os.listdir(base):
        if re.match(r"EP-0*%d-" % epica, e):
            for h in os.listdir(os.path.join(base, e)):
                if re.match(r"HU-0*%d-" % hu, h):
                    ruta = os.path.join(base, e, h, h + ".md")
                    if os.path.isfile(ruta):
                        return ruta
    return ""


def _fila_cumplida(celda, analisis, proyecto):
    """Si el trabajo de una fila de «Lo que se tiene que hacer» ya está hecho."""
    if re.search(r"(?i)este análisis", celda):
        return True
    hus = [_destino(e, analisis) for e in _ENLACE.findall(celda)]
    hus = [h for h in hus if re.match(r"HU-\d+", os.path.basename(h)) and h.endswith(".md")]
    if not hus:
        hus = [r for r in (_hu_por_numero(proyecto, int(e), int(h)) for e, h in _HU_EN_TEXTO.findall(celda)) if r]
    if not hus:
        # La fila que no nombra una HU es trabajo de la épica: queda cumplida
        # cuando la épica donde vive el pendiente terminó (análisis 15, acuerdo 1).
        return _epica_terminada(analisis)
    return all(_hu_terminada(h) for h in hus)


def _epica_terminada(analisis):
    """Si la épica que contiene la carpeta del pendiente está terminada."""
    carpeta = os.path.dirname(os.path.abspath(analisis))
    while carpeta and os.path.dirname(carpeta) != carpeta:
        if re.match(r"EP-\d+", os.path.basename(carpeta)):
            return _hu_terminada(os.path.join(carpeta, "epica.md"))
        carpeta = os.path.dirname(carpeta)
    return False


def estado(carpeta, proyecto=None, _vistos=None):
    """`CA-04` · «abierto» o «cerrado», calculado: nadie lo escribe.

    Cerrado cuando tiene al menos un análisis aprobado y cada fila de su «Lo que
    se tiene que hacer» está cumplida: dice «Este análisis», o toda HU que nombra
    está terminada. El pendiente de seguimiento cierra cuando su padre cerró y
    su `aviso-resuelto.md` dice «Comprobado» con fecha (análisis 1 del
    pendiente 103, conclusiones 16 y 36; análisis 13, acuerdo 4).
    """
    proyecto = os.path.abspath(proyecto or comun.RAIZ)
    vistos = _vistos or set()
    clave = os.path.normcase(os.path.abspath(carpeta))
    if clave in vistos:
        return "abierto"
    vistos.add(clave)
    arriba = padre(carpeta)
    if arriba:
        if estado(arriba, proyecto, vistos) != "cerrado":
            return "abierto"
        aviso = _leer(os.path.join(carpeta, "aviso-resuelto.md"))
        return "cerrado" if _COMPROBADO.search(aviso) else "abierto"
    aprobados = [a for a in analisis_de(carpeta) if _APROBADO.search(_leer(a))]
    if not aprobados:
        return "abierto"
    for analisis in aprobados:
        texto = _leer(analisis)
        m = re.search(r"^## Lo que se tiene que hacer.*$", texto, re.M)
        if not m:
            continue
        fin = re.search(r"^## ", texto[m.end():], re.M)
        seccion = texto[m.end():m.end() + fin.start()] if fin else texto[m.end():]
        for resto in _FILA.findall(seccion):
            celda = resto.split("|")[-1]
            if not _fila_cumplida(celda, analisis, proyecto):
                return "abierto"
    return "cerrado"


def _titulo(ruta):
    primera = _leer(ruta).split("\n", 1)[0]
    return re.sub(r"^#\s*(Pendiente\s*[:·]\s*)?", "", primera).strip()


def indice(proyecto=None):
    """`CA-08` · El índice de todos los pendientes, armado por el programa."""
    proyecto = os.path.abspath(proyecto or comun.RAIZ)
    destino = os.path.dirname(os.path.join(proyecto, INDICE_NUEVO))
    filas = []
    for carpeta in carpetas(proyecto):
        numero = int(_CARPETA_PENDIENTE.match(os.path.basename(carpeta)).group(1))
        ruta = os.path.join(carpeta, "pendiente.md")
        enlace = os.path.relpath(ruta, destino).replace(os.sep, "/")
        donde = os.path.relpath(carpeta, proyecto).replace(os.sep, "/")
        filas.append((numero, f"[{_titulo(ruta)}]({enlace})", f"`{donde}`", estado(carpeta, proyecto)))
    viejos = os.path.join(proyecto, CARPETA)
    nuevos = set(numeros_nuevos(proyecto))
    for numero, nombres in numerados(proyecto).items():
        if numero in nuevos:
            continue                    # pasó a la forma nueva: cuenta allá
        for nombre in nombres:
            sub = "" if os.path.isfile(os.path.join(viejos, nombre)) else CERRADOS + "/"
            ruta = os.path.join(viejos, sub + nombre)
            texto = _leer(ruta)
            cerrado = sub or re.search(r"(?i)\*\*Estado:\*\*\s*\**hecho", texto)
            enlace = os.path.relpath(ruta, destino).replace(os.sep, "/")
            filas.append((numero, f"[{_titulo(ruta)}]({enlace})", f"`{CARPETA}/{sub}`, forma anterior",
                          "cerrado" if cerrado else "abierto"))
    # Los cerrados de la forma anterior que perdieron su número al moverse a
    # `hecho/`: entran igual, porque el índice es de todos.
    sin_numero_cerrados = []
    for nombre in _archivos(os.path.join(viejos, CERRADOS)):
        if not _NUMERADO.match(nombre):
            ruta = os.path.join(viejos, CERRADOS, nombre)
            enlace = os.path.relpath(ruta, destino).replace(os.sep, "/")
            sin_numero_cerrados.append(f"| — | [{_titulo(ruta)}]({enlace}) | `{CARPETA}/{CERRADOS}/`, forma anterior | cerrado |")
    lineas = ["# Pendientes", "",
              "> Lo arma `python validadores/validar.py pendientes --indice`; no se edita a mano. "
              "El estado se calcula: un pendiente cierra cuando se cumple el plan que salió de él. "
              "Los de la forma anterior dicen el estado que tenían escrito; los cerrados que perdieron "
              "su número al pasar a `pendientes/hecho/` van al final, sin número.", "",
              "| # | Pendiente | Dónde vive | Estado |", "|---|---|---|---|"]
    lineas += ["| %d | %s | %s | %s |" % f for f in sorted(filas)]
    lineas += sorted(sin_numero_cerrados)
    return "\n".join(lineas) + "\n"


def escribir_indice(proyecto=None):
    """Escribe el índice en `documentacion/pendientes.md` y devuelve su ruta."""
    proyecto = os.path.abspath(proyecto or comun.RAIZ)
    ruta = os.path.join(proyecto, INDICE_NUEVO)
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(indice(proyecto))
    return ruta


def linea_proximo(proyecto):
    """La línea que dice el próximo número libre — CA-01."""
    ocupados = tomados(proyecto)
    abiertos = len(numerados(proyecto))
    return (f"Pendientes: {abiertos} con archivo · {len(ocupados)} números "
            f"tomados · el próximo libre es el {proximo_libre(proyecto):02d} (HU-018)")


if __name__ == "__main__":
    # `53` · Un modulo que se ejecuta solo y no imprime nada dice, con su
    # silencio, lo mismo que diria si hubiera comprobado y estuviera todo bien.
    comun.no_es_punto_de_entrada("pendientes")
