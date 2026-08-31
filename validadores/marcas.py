# -*- coding: utf-8 -*-
"""`00·ID8` · Las marcas que delatan generación automática, contadas.

La regla manda escribir sin las marcas de
[`base/00-identidad-y-rol/marcadores-de-ia.md`](../base/00-identidad-y-rol/marcadores-de-ia.md).
El [pendiente 11](../pendientes/11-limpiar-marcadores-de-ia-del-texto-del-estandar.md)
pide **contar antes de tocar**: sin el recuento no se sabe si limpiar el
estándar son dos horas o dos días.

**Solo se cuenta lo mecánico.** El anexo tiene ocho secciones y la mayoría pide
criterio —si la raya larga aparece «muy seguido», si el paralelismo es
«perfecto», si el español «no es de acá»—. Un programa que opinara de eso
llenaría de ruido lo que hoy nadie mira. Acá van las marcas que se cuentan sin
equivocarse, y el anexo mismo dice cuáles son: *«las únicas que un script
cuenta sin equivocarse»*.

**Lo que no se mira:**

- **Dentro de un bloque cercado o de comillas invertidas.** Ahí las marcas son
  ejemplos de lo que no hay que hacer, no marcas.
- **El propio anexo y esta documentación.** Un catálogo de marcas está lleno de
  marcas por definición, y contarlas sería contar el catálogo.
- **`historico-chat/`**, que es transcripción literal de lo que se dijo: no se
  reescribe, así que contarlo con lo demás mezcla deuda con lo que no lo es.
  Se cuenta aparte, para saber cuánto hay.
"""
import argparse
import os
import re
import sys

import comun
from comun import (AVISO, Hallazgo, RAIZ, es_ruta_de_datos, leer,
                   lineas_utiles, recorrer_md, relativo, reportar,
                   preparar_salida, sin_codigo_en_linea)

# Los archivos que hablan **de** las marcas: contarlas ahí es contar el catálogo.
CATALOGO = (
    "base/00-identidad-y-rol/marcadores-de-ia.md",
    "base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md",
    "validadores/marcas.py",
)

HISTORICO = "historico-chat"

# ── Sección 3 del anexo · las invisibles ──────────────────────────────────
INVISIBLES = {
    " ": "espacio duro (U+00A0)",
    "​": "ancho cero (U+200B)",
    "﻿": "marca de orden de bytes (U+FEFF)",
    "­": "guion suave (U+00AD)",
    "…": "puntos suspensivos en un solo carácter (…)",
    "–": "semiraya (–) donde va un guion",
    " ": "espacio fino (U+2009)",
    " ": "espacio fino sin salto (U+202F)",
}

# `EP-004·HU-025` · Los caracteres de control, que tampoco se ven y rompen mas.
#
# **El caso que lo hizo falta.** Al ir a agregarle una fila a la tabla de fases
# de una historia, la fila que ya estaba **empezaba con un `U+0001`** en vez de
# con la barra de la tabla. Esa fila no se renderiza como fila: desaparece del
# cuadro y queda como un parrafo suelto debajo. Estaba en **26 archivos**.
#
# **Se barre el rango completo, no los que aparecieron.** Agregar de a uno
# deja el trabajo a medias por definicion: el proximo se cuela igual. Quedan
# fuera los tres que si significan algo en un texto: salto de linea, retorno y
# tabulador.
_CONTROL = tuple(chr(c) for c in list(range(0x00, 0x20)) + [0x7F]
                 if c not in (0x09, 0x0A, 0x0D))

for _c in _CONTROL:
    INVISIBLES[_c] = "caracter de control (U+%04X)" % ord(_c)

# ── Sección 2 del anexo · lo que se cuenta sin opinar ─────────────────────
# El punto medio que **no** forma parte de una cita `NN·ID` ni de un `A · B`
# de encabezado: los dos son notación definida del estándar.
_CITA = re.compile(r"\d{2}·[A-Z]")

# El separador de encabezado —`09 · Control de versiones`, `Fase A · lo que hace`—
# es la otra mitad de esa notación, y **hasta hoy el comentario la nombraba y la
# expresión no la implementaba**. Se exime solo en la línea de un encabezado: en
# prosa, un punto medio entre frases sigue siendo lo que el anexo llama adorno.
_ENCABEZADO = re.compile(r"^#{1,6} ")
_SEPARADOR = " · "

# `21 · Automatización de procesos` — **así se nombra un capítulo**, y no solo
# en su encabezado: aparece igual en la tabla de letras, en el índice y en
# cualquier cita. Eximirlo solo dentro de un `#` era la mitad de la decisión,
# y la otra mitad se descubrió cuando el trinquete rechazó una fila de tabla
# que decía exactamente lo mismo que un título ya eximido.
_CAPITULO = re.compile(r"(?<!\d)\d{1,2} · ")

_RAYA = "—"

# **La raya se cuenta como inciso, y un inciso es prosa.** El anexo lo dice en
# su propia fila: «la raya larga (`—`) **como inciso**». Tres formas del
# estandar no son incisos, y contarlas era el contador siendo mas ancho que la
# regla. Es el mismo hallazgo del 2026-08-18 con el punto medio de los
# encabezados: la decision ya estaba escrita y faltaba implementarla.
#
#   `# EP-000 — Titulo`      el titulo de un documento, y el nombre de una seccion
#   `**CAE-01** — enunciado`  un identificador con lo que enuncia
#   `| Fase 1 — MVP |`        una celda de tabla, que es un dato y no un parrafo
_ETIQUETA_Y_ENUNCIADO = re.compile(r"\s*(?:[-*+] )?(?:\w+\. )?(?:\[[ x]\] )?\*\*[^*]+\*\*\s+\u2014")
_FILA_DE_TABLA = re.compile(r"^\s*\|")

# **El rotulo de un campo del formulario no es una vineta de prosa.** El anexo
# marca «vinetas que abren **todas** con negrita y dos puntos», que es una
# uniformidad de la prosa. Un molde no tiene prosa ahi: tiene campos, y lo que
# sigue a los dos puntos es el espacio por llenar.
#
#   `- **Objetivo:** «que se logra»`   campo del formulario, con su hueco
#   `- **Objetivo:** se logra esto`   ya es prosa, y ahi si cuenta
#
#   `- **Slug:** `«x»``  el valor va en comillas invertidas, y para cuando esta
#                       linea llega aca ya se le quito el codigo: queda vacio
_CAMPO_POR_LLENAR = re.compile(r"^\s*[-*+]\s+\*\*[^*]+:\*\*\s*(?:`?\u00ab|$)")

# `- **Algo:** ...` — la viñeta que abre con negrita y dos puntos.
_VINETA_NEGRITA = re.compile(r"^\s*[-*+]\s+\*\*[^*]+:\*\*")

# `→` o `✓` abriendo una línea, usados como viñeta.
_FLECHA_VINETA = re.compile(r"^\s*[→✓]\s")

_SEMAFORO = re.compile(r"[\U0001F534\U0001F7E1\U0001F7E2]")

# `## Título:` — dos puntos al final del encabezado.
_ENCABEZADO_DOS_PUNTOS = re.compile(r"^#{1,6}\s+.*:\s*$")

_COMILLA_CURVA = re.compile(r"[“”]")


def _excluido(raiz, archivo):
    rel = os.path.relpath(archivo, raiz).replace("\\", "/")
    return rel in CATALOGO


def _es_historico(raiz, archivo):
    rel = os.path.relpath(archivo, raiz).replace("\\", "/")
    return rel.split("/")[0] == HISTORICO


# El marcador de relleno de las plantillas. **Es notación de la casa, no
# adorno**, igual que la cita `NN·ID`: `flujo.py`, `comun.py` y `andamio.py`
# reconocen por él una celda sin llenar. Contarlo sería contar la notación, y
# limpiarlo rompería tres validadores.
_MARCADOR = u"«…»"


def marcas_de_linea(linea):
    """Las marcas mecánicas de una línea ya limpia de código. `[(clave, qué)]`."""
    salida = []
    linea = linea.replace(_MARCADOR, "")
    for caracter, nombre in INVISIBLES.items():
        for _ in range(linea.count(caracter)):
            salida.append((caracter, nombre))

    # La raya **como inciso**, que es lo que dice el anexo. No lo son el título
    # de un documento ni el nombre de una sección, ni el identificador que
    # antecede a lo que enuncia, ni una celda de tabla, que es un dato suelto.
    rayas = linea.count(_RAYA)
    if _ENCABEZADO.match(linea) or _FILA_DE_TABLA.match(linea):
        rayas = 0
    elif _ETIQUETA_Y_ENUNCIADO.match(linea):
        rayas -= 1
    for _ in range(max(rayas, 0)):
        salida.append(("raya", "raya larga (—) como inciso"))

    # El punto medio **separando frases en prosa**, descontando la cita `NN·ID`
    # y —si es un encabezado— el separador del título. Una celda de tabla
    # tampoco es prosa: ahí separa dato de dato.
    puntos = (linea.count("·") - len(_CITA.findall(linea))
              - len(_CAPITULO.findall(linea)))
    if _ENCABEZADO.match(linea):
        puntos -= linea.count(_SEPARADOR) - len(_CAPITULO.findall(linea))
    if _FILA_DE_TABLA.match(linea):
        puntos = 0
    for _ in range(max(puntos, 0)):
        salida.append(("punto-medio", "punto medio (·) fuera de una cita `NN·ID`"))

    for _ in _COMILLA_CURVA.findall(linea):
        salida.append(("comilla", "comilla curva (“ ”)"))
    # La viñeta con negrita **cuando es prosa**. El rótulo de un campo cuyo
    # valor es el espacio por llenar no lo es: eso es un formulario.
    if _VINETA_NEGRITA.match(linea) and not _CAMPO_POR_LLENAR.match(linea):
        salida.append(("vineta", "viñeta que abre con negrita y dos puntos"))
    if _FLECHA_VINETA.match(linea):
        salida.append(("flecha", "flecha o visto usado como viñeta"))
    for _ in _SEMAFORO.findall(linea):
        salida.append(("semaforo", "semáforo (🔴 🟡 🟢) en un documento formal"))
    if _ENCABEZADO_DOS_PUNTOS.match(linea):
        salida.append(("encabezado", "encabezado que termina en dos puntos"))
    return salida


def contar(raiz=None, incluir_historico=False):
    """`{clave: cuántas}` y `{archivo: cuántas}` sobre el árbol.

    Es el paso 1 del pendiente 11 —*contar antes de tocar*— y por eso devuelve
    dos repartos: **por marca**, para saber qué pesa; y **por archivo**, para
    saber por dónde empezar.
    """
    raiz = raiz or RAIZ
    por_marca, por_archivo, nombres = {}, {}, {}

    for archivo in recorrer_md(raiz):
        if _excluido(raiz, archivo):
            continue
        if _es_historico(raiz, archivo) and not incluir_historico:
            continue
        cuantas = 0
        for _n, linea in lineas_utiles(leer(archivo)):
            for clave, nombre in marcas_de_linea(sin_codigo_en_linea(linea)):
                por_marca[clave] = por_marca.get(clave, 0) + 1
                nombres[clave] = nombre
                cuantas += 1
        if cuantas:
            por_archivo[relativo(archivo)] = cuantas
    return por_marca, por_archivo, nombres


HEREDADAS = ("base", "plantillas")

# Cuántos archivos miró la última corrida de `validar`. Lo lee
# `alcance()` para no inventarse el número.
MIRADOS = None

# `EP-004·HU-024` · La salida dice sobre qué corrió y qué no cuenta.
#
# **El caso que lo hizo falta.** El 2026-08-30 el agente corrió este comando
# sobre veinticinco documentos de `documentacion/`, obtuvo cero, y escribió en
# el cuerpo de un commit que estaban limpios. El enganche del commit encontró
# trece avisos en esos mismos archivos: el cero salía de **no mirar**.
#
# Un validador que no dice sobre qué corrió no entrega un veredicto: entrega
# un número que el lector completa con lo que quiere creer.
NO_SE_CUENTAN = ("el español de otra parte, la estructura demasiado pareja, el tono, y el contraste con lo escrito antes",)


def alcance(raiz=None, mirados=None):
    """Las dos frases que acompañan al resultado: qué se miró y qué no.

    Se arma con lo que la corrida **de verdad** recorrió, no con un texto
    escrito aparte: si el alcance cambia y nadie actualiza la frase, la frase
    miente, y este defecto nació justamente de creerle a un número.
    """
    carpetas = ", ".join("`%s/`" % c for c in HEREDADAS)
    if mirados == 0:
        primera = ("no se miró ningún archivo: en %s no hay ninguno que revisar"
                   % carpetas)
    else:
        cuantos = "" if mirados is None else " (%d archivos)" % mirados
        primera = "se recorrió %s%s, que es lo que viaja a los proyectos" % (
            carpetas, cuantos)
    return (primera,
            "no se cuenta lo que hay que leer para verlo: %s" % NO_SE_CUENTAN[0])


def validar(raiz=None):
    """Las marcas de lo que se hereda: `base/` y `plantillas/`.

    **Solo esas dos carpetas**, y es el paso 2 del pendiente: son lo que viaja
    a los proyectos. `notas/`, `analisis/` y el histórico son bitácora y pueden
    esperar — reportarlos hoy sepultaría lo que sí hay que arreglar.
    """
    raiz = raiz or RAIZ
    hallazgos = []
    global MIRADOS
    MIRADOS = 0
    for archivo in recorrer_md(raiz):
        if _excluido(raiz, archivo):
            continue
        rel = os.path.relpath(archivo, raiz).replace("\\", "/").split("/")[0]
        if rel not in HEREDADAS:
            continue
        MIRADOS += 1
        for n, linea in lineas_utiles(leer(archivo)):
            vistas = set()
            for clave, nombre in marcas_de_linea(sin_codigo_en_linea(linea)):
                if clave in vistas:
                    continue        # una vez por línea: el conteo va en `contar`
                vistas.add(clave)
                hallazgos.append(Hallazgo(
                    AVISO, archivo, n,
                    f"{nombre} — `00·ID8` pide entregar sin las marcas del anexo"))
    return hallazgos


# ── La limpieza · solo lo que se reemplaza sin criterio ───────────────────
#
# **Se limpia la mitad que no es prosa.** Un espacio duro, un ancho cero, una
# semiraya donde va un guion, unos puntos suspensivos en un carácter: cada uno
# tiene **un** reemplazo y no hay nada que decidir. Se arreglan sin leer.
#
# La raya larga, el punto medio en prosa y la viñeta con negrita **no están
# acá**, y es a propósito: quitarlas es reescribir la frase, y un programa que
# reescribe frases del estándar cambia lo que el estándar dice. Esas quedan
# para quien escriba, con el trinquete impidiendo que sumen más.
REEMPLAZOS = {
    "\u00a0": " ",       # espacio duro
    "\u2009": " ",       # espacio fino
    "\u202f": " ",       # espacio fino sin salto
    "\u200b": "",        # ancho cero
    "\ufeff": "",        # marca de orden de bytes
    "\u00ad": "",        # guion suave
    "\u2026": "...",     # puntos suspensivos en un carácter
    "\u2013": "-",       # semiraya donde va un guion
    "\u201c": '"',       # comilla curva de apertura
    "\u201d": '"',       # comilla curva de cierre
}

# Los de control se borran: no hay reemplazo que elegir, no significan nada
# dentro de un texto (`EP-004·HU-025`).
for _c in _CONTROL:
    REEMPLAZOS[_c] = ""


def limpiar_texto(texto):
    """El texto con los reemplazos hechos, **fuera de código**. `(nuevo, n)`.

    Dentro de un bloque cercado o de comillas invertidas la marca es el
    ejemplo de lo que no hay que hacer: cambiarla borraría el ejemplo.
    """
    salida, cambios, cercado = [], 0, False
    for linea in texto.split("\n"):
        if linea.lstrip().startswith("```") or linea.lstrip().startswith("~~~"):
            cercado = not cercado
            salida.append(linea)
            continue
        if cercado:
            salida.append(linea)
            continue
        trozos = linea.split("`")
        for i in range(0, len(trozos), 2):      # los pares están fuera del código
            if _MARCADOR in trozos[i]:
                continue                        # notación de la casa: no se toca
            for viejo, nuevo in REEMPLAZOS.items():
                if viejo in trozos[i]:
                    cambios += trozos[i].count(viejo)
                    trozos[i] = trozos[i].replace(viejo, nuevo)
        salida.append("`".join(trozos))
    return "\n".join(salida), cambios


def limpiar(raiz=None, carpetas=None, escribir=False):
    """Limpia lo mecánico de esas carpetas. `[(archivo, cuántas)]`.

    Sin `escribir` solo simula, como el resto de los reparadores de esta casa.
    """
    raiz = raiz or RAIZ
    carpetas = HEREDADO if carpetas is None else carpetas
    tocados = []
    for archivo in recorrer_md(raiz):
        if _excluido(raiz, archivo) or _es_historico(raiz, archivo):
            continue
        rel = os.path.relpath(archivo, raiz).replace("\\", "/")
        if carpetas and rel.split("/")[0] not in carpetas:
            continue
        nuevo, cambios = limpiar_texto(leer(archivo))
        if not cambios:
            continue
        tocados.append((relativo(archivo), cambios))
        if escribir:
            with open(archivo, "w", encoding="utf-8", newline="\n") as f:
                f.write(nuevo)
    return tocados


# ── El trinquete · qué se bloquea al guardar ──────────────────────────────
#
# **Bloquear todas las marcas apagaría el enganche el primer día.** Medido sobre
# los seis commits anteriores a escribir esto: 425 marcas de estilo agregadas y
# 23 invisibles. Un enganche que rechaza cada commit se desactiva en una tarde,
# y ese es el defecto más caro de este repositorio.
#
# Lo que sí se puede sostener es un **trinquete**: que la deuda no crezca.
#
# - **Las invisibles, en cualquier archivo.** Nunca se escriben a propósito:
#   nadie teclea un espacio duro ni un ancho cero. Se arreglan en segundos.
# - **Todas las marcas, en `base/` y `plantillas/`.** Es lo que se hereda, y es
#   donde `00·ID8` importa. De los ocho commits medidos, seis pasaban ya.
#
# Fuera de eso se cuenta y se dice, sin bloquear: el número delante en el
# momento de escribir enseña más que una limpieza de una sola vez.
HEREDADO = ("base", "plantillas")

# El bloque de checklist de una regla. Se reconoce igual que en `cargador.py`,
# que ya lo trata aparte — y por el mismo motivo: **no es texto de nadie**.
_SELLO = re.compile(r"(?ms)^(?:---\s*\n+)?### Checklist.*?(?=^## |\Z)")


def _sin_sellos(texto):
    """El texto sin los bloques de checklist."""
    return _SELLO.sub("", texto)



def _git(raiz, *args):
    import subprocess
    r = subprocess.run(("git", "-C", raiz) + args, capture_output=True,
                       text=True, encoding="utf-8", errors="replace", timeout=60)
    return r.stdout if r.returncode == 0 else None


def archivos_preparados(raiz):
    """Los `.md` que entran en el commit que se está por hacer."""
    salida = _git(raiz, "diff", "--cached", "--name-only", "--diff-filter=ACMR")
    if not salida:
        return []
    return [l.strip() for l in salida.splitlines()
            if l.strip().lower().endswith(".md")]


def _cuenta(texto):
    """`{clave: cuántas}` de un texto, saltando código, cercados y **sellos**.

    **El sello no es prosa**: es el registro de haberle aplicado el checklist
    a la regla, y su forma —`A · Dónde va`, `B · Cómo se identifica`— la fija
    [`checklist.md`](../base/20-meta-reglas/checklist.md), no quien escribe.
    Contarlo sería contar el molde, y ninguna limpieza podría arreglarlo sin
    romper el sello. `cargador.py` ya trata el sello aparte por lo mismo.
    """
    salida = {}
    for _n, linea in lineas_utiles(_sin_sellos(texto)):
        for clave, _nombre in marcas_de_linea(sin_codigo_en_linea(linea)):
            salida[clave] = salida.get(clave, 0) + 1
    return salida


def _origen_rename(raiz, rel):
    """La ruta que `rel` tenía en `HEAD`, si el commit lo renombra. `None` si no.

    Un `git mv` no agrega marcas: es el mismo contenido con otra ruta. Sin
    esto, el trinquete le pone línea base cero al nombre nuevo y cuenta como
    nuevas todas las marcas que el archivo ya traía de antes.
    """
    salida = _git(raiz, "diff", "--cached", "--name-status", "--find-renames")
    if not salida:
        return None
    for linea in salida.splitlines():
        partes = linea.split("\t")
        if len(partes) == 3 and partes[0].startswith("R") and partes[2] == rel:
            return partes[1]
    return None


def _crecimiento(raiz, rel):
    """Cuántas marcas de cada clase **suma** este archivo respecto de `HEAD`.

    Se compara el archivo entero contra su versión anterior, no el diff en
    crudo: así lo que está dentro de un bloque cercado sigue sin contarse, que
    es donde viven los ejemplos del anexo.
    """
    ahora = _git(raiz, "show", ":%s" % rel)
    if ahora is None:
        return {}
    antes = _git(raiz, "show", "HEAD:%s" % rel)
    if antes is None:
        origen = _origen_rename(raiz, rel)
        if origen:
            antes = _git(raiz, "show", "HEAD:%s" % origen)
    antes = antes or ""
    a, b = _cuenta(ahora), _cuenta(antes)
    return {k: a.get(k, 0) - b.get(k, 0)
            for k in set(a) | set(b) if a.get(k, 0) > b.get(k, 0)}


def validar_preparados(raiz=None):
    """El trinquete sobre lo que entra en el commit. `[Hallazgo]`."""
    raiz = raiz or RAIZ
    hallazgos = []
    for rel in archivos_preparados(raiz):
        if rel in CATALOGO or rel.split("/")[0] == HISTORICO:
            continue
        # `00-ID8` habla de lo que **el agente entrega**, y lo que la
        # plataforma trajo lo escribio otro proyecto. Ademas `_crecimiento`
        # llama a git una vez por archivo: sin este corte, guardar una traida
        # de mil documentos son mil llamadas para juzgar lo que no es nuestro.
        if es_ruta_de_datos(rel):
            continue
        crece = _crecimiento(raiz, rel)
        if not crece:
            continue
        ruta = os.path.join(raiz, *rel.split("/"))
        heredado = rel.split("/")[0] in HEREDADO
        for clave, cuantas in sorted(crece.items(), key=lambda x: -x[1]):
            invisible = clave in INVISIBLES
            if invisible:
                nombre = INVISIBLES[clave]
                razon = ("no se escribe a propósito y se quita en segundos")
            else:
                nombre = clave
                razon = ("esto se hereda: `base/` y `plantillas/` son lo que "
                         "viaja a los proyectos")
            if invisible or heredado:
                hallazgos.append(Hallazgo(
                    comun.FALLA, ruta, 0,
                    f"agrega {cuantas} · {nombre} — {razon} (`00·ID8`)"))
            else:
                hallazgos.append(Hallazgo(
                    AVISO, ruta, 0,
                    f"agrega {cuantas} · {nombre} — no bloquea acá, pero es "
                    f"deuda que alguien limpia después (`00·ID8`)"))
    return hallazgos


def main():
    preparar_salida()
    p = argparse.ArgumentParser(
        description="Cuenta las marcas mecánicas de `00·ID8`.")
    p.add_argument("--raiz", default=RAIZ)
    p.add_argument("--historico", action="store_true",
                   help="incluye `historico-chat/`, que no se reescribe")
    p.add_argument("--archivos", type=int, default=15,
                   help="cuántos archivos listar, de mayor a menor")
    a = p.parse_args()

    por_marca, por_archivo, nombres = contar(a.raiz, a.historico)
    total = sum(por_marca.values())
    print(f"== Marcas mecánicas de `00·ID8` ==\n")
    print(f"{total} en {len(por_archivo)} archivos\n")

    print("Por marca:")
    for clave, cuantas in sorted(por_marca.items(), key=lambda x: -x[1]):
        print(f"  {cuantas:>6}  {nombres[clave]}")

    print(f"\nPor archivo, los {a.archivos} primeros:")
    for archivo, cuantas in sorted(por_archivo.items(),
                                   key=lambda x: -x[1])[:a.archivos]:
        print(f"  {cuantas:>6}  {archivo}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
