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

# `55` · Una celda bajo una de estas columnas **muestra** un identificador; no
# cita ninguna regla. Exigirle el enlace obliga a redactar torcido para callar
# al validador, que es la salida mala que el pendiente 55 describe.
#
# El caso que lo destapó: `estructura-regla.md` explica la anatomía de un
# identificador, y su columna «Lo que sale mal» dice «ponerle `G9` a una regla
# del capítulo de pruebas». Ahí `G9` es el token equivocado del ejemplo, no la
# regla `G9` de git — que existe, aunque el pendiente afirmara lo contrario.
COLUMNAS_DE_EJEMPLO = {
    "lo que sale mal", "así se ve", "asi se ve", "ejemplo", "ejemplos",
    "incorrecto", "correcto", "mal", "bien", "qué es de verdad",
}


def _celdas_de(linea):
    return [c.strip() for c in linea.strip().strip("|").split("|")]


def _es_muestra(linea, columna_de, id):
    """¿El identificador cae en una celda de columna de ejemplos?"""
    if not columna_de or not linea.strip().startswith("|"):
        return False
    for i, celda in enumerate(_celdas_de(linea)):
        if id in celda and i < len(columna_de):
            return columna_de[i] in COLUMNAS_DE_EJEMPLO
    return False


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
    estado = {"encabezados": [], "linea": "", "previo": ""}

    def enlace(capitulo, id, literal, antes=""):
        """El enlace, o el texto original si la regla no existe."""
        ruta = destino(origen, id, idx)
        # Sin destino no se inventa un enlace: la cita queda como estaba y el
        # validador la reporta. Un enlace roto es peor que ninguno.
        if not ruta or idx[id][0] == origen:
            return literal
        # `55` · El reparador obedece las mismas exclusiones que el validador.
        # Si no, escribe en `base/` justo lo que el validador ya aceptó que no
        # era una cita — y eso es peor que reportar de más.
        if _es_muestra(estado["linea"], estado["encabezados"], id):
            return literal
        # Ya enlazada antes: en una línea anterior, o **en esta misma antes de
        # esta mención** —incluidos los enlaces que ya venían escritos, que
        # `_CITA` no ve porque los descarta—. `antes` es el tramo de línea que
        # queda a la izquierda.
        previo = estado["previo"] + antes
        if f"[`{id}`](" in previo or f"·{id}`](" in previo:
            return literal
        cambios[0] += 1
        return f"[`{f'{capitulo}·{id}' if capitulo else id}`]({ruta})"

    for linea in texto.splitlines(keepends=True):
        anterior = estado["previo"]
        estado["previo"] = anterior + linea
        estado["linea"] = linea
        if _CERCA.match(linea):
            dentro = not dentro
            salida.append(linea)
            continue
        if dentro or linea.lstrip().startswith("#"):
            salida.append(linea)
            continue

        if re.fullmatch(r"\|[-:|\s]+\|", linea.strip()):
            previas = anterior.splitlines()
            estado["encabezados"] = ([c.lower() for c in _celdas_de(previas[-1])]
                                     if previas else [])
        elif not linea.strip().startswith("|"):
            estado["encabezados"] = []
        estado["previo"] = anterior      # lo previo no incluye esta línea

        # El orden importa: la partida primero, porque su `NN` entre comillas
        # también encajaría a medias en las otras.
        linea = _CITA_PARTIDA.sub(
            lambda m: enlace(m.group(1), m.group(2), m.group(0),
                             m.string[:m.start()]), linea)
        linea = _DEPENDENCIA.sub(
            lambda m: (f"({m.group(1)} "
                       f"{enlace(m.group(2), m.group(3), m.group(3), m.string[:m.start()])})"),
            linea)
        linea = _CITA.sub(
            lambda m: enlace(m.group(1), m.group(2), m.group(0),
                             m.string[:m.start()]), linea)
        salida.append(linea)
        estado["previo"] = anterior + linea

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
        # `55` · El ancla suelta a una regla de este mismo archivo es correcta
        # —`[`G1`](#g1--…)`— y reescribirla a la ruta completa la empeora.
        if not ruta.split("#")[0] and idx[id][0] == origen:
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
        encabezados = []          # las columnas de la tabla que se está leyendo
        # Lo ya leído del archivo, para saber si una cita se enlazó antes.
        # `55` · Exigir el enlace en la segunda mención del mismo documento es
        # ruido: quien lee ya lo tiene tres líneas más arriba.
        texto_previo = ""
        for n, linea in enumerate(leer(archivo).splitlines(), start=1):
            anterior, texto_previo = texto_previo, texto_previo + linea + "\n"
            if _CERCA.match(linea):
                dentro = not dentro
                continue
            if dentro or linea.lstrip().startswith("#"):
                continue
            texto_previo_sin_esta = anterior

            # El encabezado de la tabla en curso: la fila anterior al renglón
            # de guiones. Se olvida al salir de la tabla.
            if re.fullmatch(r"\|[-:|\s]+\|", linea.strip()):
                encabezados = [c.lower() for c in _celdas_de(anterior.splitlines()[-1])]                     if anterior.strip() else []
            elif not linea.strip().startswith("|"):
                encabezados = []

            for m in _CITA_ENLAZADA.finditer(linea):
                id, ruta = m.group(2), m.group(3)
                if id not in idx:
                    hallazgos.append(Hallazgo(
                        FALLA, archivo, n,
                        f"la cita `{id}` enlaza a una regla que no existe"))
                    continue
                esperado = destino(archivo, id, idx)
                # `55` · El ancla suelta vale cuando la regla vive en este
                # mismo archivo: `[`G1`](#g1--…)` es la forma correcta de
                # citar a una vecina, y compararla contra la ruta completa la
                # daba por mal apuntada.
                if not ruta.split("#")[0] and idx[id][0] == archivo:
                    continue
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
                # `55` · Ya se enlazó antes: en una línea anterior, o en
                # esta misma antes de esta mención. Lo segundo se descubrió el
                # 2026-08-18, sellando `07·Q4`: dos menciones en el mismo
                # párrafo y en el mismo renglón, la primera con su enlace.
                antes = texto_previo_sin_esta + linea[:m.start()]
                if f"[`{id}`](" in antes or f"·{id}`](" in antes:
                    continue
                if _es_muestra(linea, encabezados, id):
                    continue          # `55` · es una muestra, no una cita
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
