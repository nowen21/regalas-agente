#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Las citas entre reglas se enlazan, no solo se nombran.

Una regla que cita a otra por su ID (`09·G2`, `M5`) obliga a quien lee a salir a
buscarla: abrir el capítulo, encontrar el encabezado. Con 285 citas repartidas en
47 archivos, eso es fricción suficiente para que nadie compruebe nada — y una
cita que nadie sigue es una dependencia que nadie verifica.

Este módulo hace tres cosas:

  1. **Indexa** dónde vive cada regla, leyendo `base/`. La verdad es el archivo,
     no una tabla escrita a mano que envejece.
  2. **Enlaza** las citas sueltas, convirtiéndolas en enlaces al sitio exacto.
  3. **Valida** que ninguna cita quede suelta y que ningún enlace apunte al vacío.

Lo que **no** se toca: el contenido de los bloques cercados. Ahí las citas son
ejemplos —muestran cómo se escribe una regla, no citan a nadie— y enlazarlas
convertiría el molde en algo que no se puede copiar.
"""
import os
import re

from comun import AVISO, FALLA, Hallazgo, RAIZ, leer, recorrer_md, relativo

BASE = "base"

# El encabezado de una regla: `## <PREFIJO><n>[.<m>] · <título>`, con lo que
# venga después (marcas como [BLINDADA]). También se acepta `#`: una regla que
# creció hasta ocupar su propia carpeta abre con H1, y sigue siendo una regla.
# El H1 de un capítulo no encaja: lleva número, no ID (`# 20 · Meta-reglas`).
_REGLA = re.compile(r"^(#{1,2})\s+([A-Z]{1,4}\d+(?:\.\d+)?)\s*·\s*(.+?)\s*$")
_REGLA_M = re.compile(_REGLA.pattern, re.MULTILINE)

# Una sub-regla enumerada en negrita, con título o sin él:
#   `**F12.1** — …`   ·   `**F12.13 · Materialización física**`
_SUBREGLA = re.compile(r"\*\*([A-Z]{1,4}\d+\.\d+)(?:\s*·[^*]*)?\*\*")

_ID = r"[A-Z]{1,4}\d+(?:\.\d+)?"

# Tres formas de citar conviven en `base/`, y `M4` solo admite la primera
# (`NN·ID`). Se reconocen las tres para poder enlazarlas **y** normalizarlas:
#
#   `04·S4`        la canónica
#   `00` · N3      el capítulo entre comillas y el ID fuera, con espacios
#   `00`·N3        igual, sin espacios
#
# El `(?<!\[)` descarta lo que ya es enlace: `[`09·G6`](…)`.
_CITA_PARTIDA = re.compile(rf"(?<!\[)`(\d{{2}})`\s*·\s*({_ID})")
_CITA = re.compile(rf"(?<!\[)`(?:(\d{{2}})·)?({_ID})`")

# La dependencia escrita sin comillas dentro del paréntesis, como pide `M7`:
# «(extiende 09·G6)».
_DEPENDENCIA = re.compile(
    rf"\((extiende|depende de|deroga)\s+(?:(\d{{2}})·)?({_ID})\)")

# Una cita que ya es enlace, para poder comprobar a dónde apunta.
_CITA_ENLAZADA = re.compile(
    r"\[`(?:(\d{2})·)?([A-Z]{1,4}\d+(?:\.\d+)?)`\]\(([^)]+)\)")

_CERCA = re.compile(r"^\s*(```|~~~)")


def ancla(titulo_completo):
    """El ancla que GitHub genera para un encabezado.

    Minúsculas, se quitan los signos y **cada** espacio pasa a un guion. Lo de
    "cada" no es un detalle: el `·` que separa ID y título va entre espacios, así
    que al quitarlo quedan dos seguidos y el ancla real lleva `--`. Colapsarlos
    produciría un enlace que no lleva a ninguna parte.
    """
    t = titulo_completo.strip().lower()
    t = re.sub(r"[^\w\s-]", "", t, flags=re.UNICODE)
    return re.sub(r"\s", "-", t).strip("-")


def indice(raiz=None):
    """{ID: (ruta absoluta, ancla)} de todas las reglas de `base/`.

    Una regla que vive en su propio archivo no lleva ancla: el enlace al archivo
    ya es el enlace a la regla.
    """
    raiz = raiz or RAIZ
    base = os.path.join(raiz, BASE)
    salida = {}
    for archivo in recorrer_md(base):
        texto = leer(archivo)
        dentro = False
        for linea in texto.splitlines():
            if _CERCA.match(linea):
                dentro = not dentro
                continue
            if dentro:
                continue
            m = _REGLA.match(linea)
            if not m:
                continue
            nivel, id, titulo = m.group(1), m.group(2), m.group(3)
            # Una regla por archivo: el enlace al archivo ya es el enlace a la
            # regla, y un ancla de más se rompería al renombrar el título. Pasa
            # de dos formas: el H1 del archivo, o un único `##` en un archivo
            # que se llama como la regla.
            sola = (nivel == "#"
                    or (len(_REGLA_M.findall(texto)) == 1
                        and os.path.basename(archivo).startswith(id + "-")))
            salida[id] = (archivo, "" if sola else ancla(f"{id} · {titulo}"))

        # Sub-reglas declaradas en negrita dentro del archivo de su madre
        # (`**F12.1** — …`), que es como `F12` enumera las suyas. No tienen
        # encabezado propio, así que el enlace es al archivo: llevar al lector
        # a la regla madre es mucho mejor que no llevarlo a ninguna parte.
        for m in _SUBREGLA.finditer(texto):
            sub = m.group(1)
            madre = sub.split(".")[0]
            if madre in salida and salida[madre][0] == archivo:
                salida.setdefault(sub, (archivo, ""))
    return salida


def destino(origen, id, idx):
    """El enlace relativo desde `origen` hasta la regla `id`, o "" si no existe."""
    if id not in idx:
        return ""
    archivo, anc = idx[id]
    rel = os.path.relpath(archivo, os.path.dirname(origen)).replace("\\", "/")
    return f"{rel}#{anc}" if anc else rel


def enlazar(texto, origen, idx):
    """Convierte las citas de `texto` en enlaces, ya normalizadas a `NN·ID`.

    Devuelve (texto, cuántas). Los bloques cercados no se tocan: ahí las citas
    son ejemplos del molde, no citas a nadie.
    """
    cambios = [0]
    salida = []
    dentro = False

    def enlace(capitulo, id, literal):
        """El enlace, o el texto original si la regla no existe."""
        ruta = destino(origen, id, idx)
        # Sin destino no se inventa un enlace: la cita queda como estaba y el
        # validador la reporta. Un enlace roto es peor que ninguno.
        if not ruta or idx[id][0] == origen:
            return literal
        cambios[0] += 1
        return f"[`{f'{capitulo}·{id}' if capitulo else id}`]({ruta})"

    for linea in texto.splitlines(keepends=True):
        if _CERCA.match(linea):
            dentro = not dentro
            salida.append(linea)
            continue
        if dentro or linea.lstrip().startswith("#"):
            salida.append(linea)
            continue

        # El orden importa: la partida primero, porque su `NN` entre comillas
        # también encajaría a medias en las otras.
        linea = _CITA_PARTIDA.sub(
            lambda m: enlace(m.group(1), m.group(2), m.group(0)), linea)
        linea = _DEPENDENCIA.sub(
            lambda m: (f"({m.group(1)} "
                       f"{enlace(m.group(2), m.group(3), m.group(3))})"), linea)
        linea = _CITA.sub(
            lambda m: enlace(m.group(1), m.group(2), m.group(0)), linea)
        salida.append(linea)

    return "".join(salida), cambios[0]


def reparar(texto, origen, idx):
    """Reapunta las citas ya enlazadas que quedaron mirando a otro sitio.

    Un archivo que se mueve —un capítulo que pasa a carpeta, una regla que se
    separa— deja atrás todos los enlaces que lo citaban. Sin esto, la exigencia
    de enlazar duraría hasta la primera reorganización.
    """
    cambios = [0]
    salida = []
    dentro = False

    def reemplazo(m):
        capitulo, id, ruta = m.group(1), m.group(2), m.group(3)
        esperado = destino(origen, id, idx)
        if not esperado or ruta == esperado:
            return m.group(0)
        cambios[0] += 1
        return f"[`{f'{capitulo}·{id}' if capitulo else id}`]({esperado})"

    for linea in texto.splitlines(keepends=True):
        if _CERCA.match(linea):
            dentro = not dentro
            salida.append(linea)
            continue
        salida.append(linea if dentro else _CITA_ENLAZADA.sub(reemplazo, linea))

    return "".join(salida), cambios[0]


def validar(raiz=None):
    """Citas sueltas y enlaces que no llevan a ninguna regla."""
    raiz = raiz or RAIZ
    idx = indice(raiz)
    hallazgos = []

    for archivo in recorrer_md(os.path.join(raiz, BASE)):
        dentro = False
        for n, linea in enumerate(leer(archivo).splitlines(), start=1):
            if _CERCA.match(linea):
                dentro = not dentro
                continue
            if dentro or linea.lstrip().startswith("#"):
                continue

            for m in _CITA_ENLAZADA.finditer(linea):
                id, ruta = m.group(2), m.group(3)
                if id not in idx:
                    hallazgos.append(Hallazgo(
                        FALLA, archivo, n,
                        f"la cita `{id}` enlaza a una regla que no existe"))
                    continue
                esperado = destino(archivo, id, idx)
                if ruta.split("#")[0] != esperado.split("#")[0]:
                    hallazgos.append(Hallazgo(
                        AVISO, archivo, n,
                        f"la cita `{id}` apunta a «{ruta}» y la regla está en "
                        f"«{esperado}»"))

            for m in _CITA.finditer(linea):
                id = m.group(2)
                if id not in idx:
                    continue          # no es una cita: es texto que se le parece
                if idx[id][0] == archivo:
                    continue          # se cita a sí misma o a una vecina del archivo
                hallazgos.append(Hallazgo(
                    AVISO, archivo, n,
                    f"la cita `{id}` no lleva enlace — quien lea tiene que ir "
                    f"a buscarla"))

    return hallazgos


def aplicar(raiz=None, escribir=False):
    """Enlaza las citas sueltas y repara las que apuntan a otro sitio.

    Devuelve [(archivo, enlazadas, reparadas)].
    """
    raiz = raiz or RAIZ
    idx = indice(raiz)
    tocados = []
    for archivo in recorrer_md(os.path.join(raiz, BASE)):
        texto = leer(archivo)
        nuevo, n = enlazar(texto, archivo, idx)
        nuevo, r = reparar(nuevo, archivo, idx)
        if n or r:
            tocados.append((archivo, n, r))
            if escribir:
                with open(archivo, "w", encoding="utf-8", newline="\n") as f:
                    f.write(nuevo)
    return tocados


if __name__ == "__main__":
    import sys
    from comun import preparar_salida

    preparar_salida()
    escribir = "--aplicar" in sys.argv
    idx = indice()
    print(f"{len(idx)} reglas indexadas en base/\n")
    tocados = aplicar(escribir=escribir)
    for archivo, n, r in tocados:
        detalle = " · ".join(x for x in
                             (f"{n} enlazadas" if n else "",
                              f"{r} reparadas" if r else "") if x)
        print(f"  {detalle:<28} {relativo(archivo)}")
    enlazadas = sum(n for _, n, _ in tocados)
    reparadas = sum(r for _, _, r in tocados)
    print(f"\n{enlazadas} enlazadas · {reparadas} reparadas · "
          f"{len(tocados)} archivos"
          f"{' — ESCRITAS' if escribir else ' (simulado; agrega --aplicar)'}")
