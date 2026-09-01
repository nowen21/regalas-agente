# -*- coding: utf-8 -*-
"""Convierte el texto de un documento al marcado del entregable.

**Con la librería estándar y nada más**, que es lo que el usuario decidió el
2026-08-31: el entregable es lo único que sale de la plataforma hacia un
tercero, y `CA-03` exige que dos corridas den el mismo archivo. Con una
biblioteca de por medio, una actualización cambia lo que el cliente ve sin que
nadie lo pida.

**Qué convierte, y por qué solo eso.** Lo que los documentos de este ciclo usan
de verdad: encabezados, tablas, listas, negrita, código, enlaces, citas y
bloques cercados. Convertir un lenguaje entero sería construir lo que ya existe;
convertir lo que se usa es lo que hace falta y se puede comprobar.

**Lo difícil son las listas dentro de una celda de tabla** (`CA-02` de la
historia), y por eso están escritas primero: en este repositorio casi toda tabla
las tiene, y es donde estos convertidores dejan la marca del texto a la vista.

**Lo que no se reconoce se deja como texto**, escapado. Nunca se inventa una
etiqueta: un convertidor que adivina produce un documento que se ve bien y dice
otra cosa.
"""
import re

# El orden importa: lo más específico primero, o la negrita se come al código.
_CODIGO = re.compile(r"`([^`]+)`")
_ENLACE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
_NEGRITA = re.compile(r"\*\*([^*]+)\*\*")
_CURSIVA = re.compile(r"(?<![\*\w])\*([^*]+)\*(?!\*)")

_ENCABEZADO = re.compile(r"^(#{1,6})\s+(.*)$")
_VINETA = re.compile(r"^(\s*)[-*+]\s+(.*)$")
_NUMERADA = re.compile(r"^(\s*)\d+\.\s+(.*)$")
_CITA = re.compile(r"^>\s?(.*)$")
_CERCA = re.compile(r"^\s*```")
_SEPARADOR = re.compile(r"^\s*-{3,}\s*$")
_FILA = re.compile(r"^\s*\|(.+)\|\s*$")
_SEPARADOR_DE_TABLA = re.compile(r"^\s*\|[\s:|-]+\|\s*$")

# Dentro de una celda, la lista viene con este separador porque una celda no
# tiene renglones. Es la forma en que este repositorio las escribe.
_EN_CELDA = re.compile(r"\s*·\s+")


def escapar(texto):
    """El texto sin significado de marcado. Va primero, siempre."""
    return (texto.replace("&", "&amp;").replace("<", "&lt;")
                 .replace(">", "&gt;"))


# Con esto se aparta lo que va en código mientras se convierte el resto. Es un
# carácter de control: no aparece en un documento escrito por una persona.
_APARTE = chr(0)


def en_linea(texto):
    """Lo que va dentro de una línea: código, enlaces, negrita, cursiva.

    **Lo que va en código se aparta primero y no se vuelve a tocar.** Sin eso,
    `**esto no es negrita**` salía en negrita: el código es justamente lo que
    se escribe para mostrar el marcado sin que actúe.
    """
    salida = escapar(texto)

    apartados = []

    def guardar(m):
        apartados.append(m.group(1))
        return _APARTE + str(len(apartados) - 1) + _APARTE

    salida = _CODIGO.sub(guardar, salida)
    salida = _ENLACE.sub(
        lambda m: '<a href="%s">%s</a>' % (m.group(2), m.group(1)), salida)
    salida = _NEGRITA.sub(lambda m: "<strong>%s</strong>" % m.group(1), salida)
    salida = _CURSIVA.sub(lambda m: "<em>%s</em>" % m.group(1), salida)

    for i, adentro in enumerate(apartados):
        salida = salida.replace(_APARTE + str(i) + _APARTE,
                                "<code>%s</code>" % adentro)
    return salida


def celda(texto):
    """El contenido de una celda. **Si trae una lista, sale como lista.**

    Es el `CA-02`, y es lo que decide esta pieza. En este repositorio las
    tablas llevan listas adentro por todas partes, escritas con un separador
    porque una celda no tiene renglones. Dejarlas como texto corrido pondría a
    la vista la marca del origen, que es lo que el criterio prohíbe.
    """
    partes = [p for p in _EN_CELDA.split(texto.strip()) if p.strip()]
    if len(partes) < 2 or not _se_puede_partir(partes):
        return en_linea(texto.strip())
    return "<ul>%s</ul>" % "".join("<li>%s</li>" % en_linea(p) for p in partes)


def _se_puede_partir(partes):
    """Si al partir no se rompió una negrita ni un trozo de código.

    **El separador también aparece dentro de lo resaltado.** «1 · Ver lo que
    hay», escrito entero en negrita, se partía en dos y las marcas quedaban a la
    vista: se midió sobre el entregable de este repositorio y eran 174.
    """
    for parte in partes:
        if parte.count("**") % 2 or parte.count("`") % 2:
            return False
    return True


def _filas_de(linea):
    """Las celdas de una fila, sin las barras de los extremos."""
    return [c for c in _FILA.match(linea).group(1).split("|")]


def a_marcado(texto):
    """El documento convertido. Devuelve el cuerpo, sin envoltura."""
    salida = []
    lineas = (texto or "").split("\n")
    i = 0
    while i < len(lineas):
        linea = lineas[i]

        if _CERCA.match(linea):
            i, bloque = _bloque_cercado(lineas, i)
            salida.append(bloque)
            continue

        if _FILA.match(linea):
            i, tabla = _tabla(lineas, i)
            salida.append(tabla)
            continue

        if _VINETA.match(linea) or _NUMERADA.match(linea):
            i, lista = _lista(lineas, i)
            salida.append(lista)
            continue

        m = _ENCABEZADO.match(linea)
        if m:
            nivel = len(m.group(1))
            salida.append("<h%d>%s</h%d>" % (nivel, en_linea(m.group(2)), nivel))
            i += 1
            continue

        if _CITA.match(linea):
            i, cita = _cita(lineas, i)
            salida.append(cita)
            continue

        if _SEPARADOR.match(linea):
            salida.append("<hr/>")
            i += 1
            continue

        if linea.strip():
            i, parrafo = _parrafo(lineas, i)
            salida.append(parrafo)
            continue

        i += 1

    return "\n".join(salida)


def _bloque_cercado(lineas, i):
    """Lo que va entre cercas queda tal cual: es código, no prosa."""
    adentro = []
    i += 1
    while i < len(lineas) and not _CERCA.match(lineas[i]):
        adentro.append(escapar(lineas[i]))
        i += 1
    return i + 1, "<pre><code>%s</code></pre>" % "\n".join(adentro)


def _tabla(lineas, i):
    filas = []
    while i < len(lineas) and _FILA.match(lineas[i]):
        if not _SEPARADOR_DE_TABLA.match(lineas[i]):
            filas.append(_filas_de(lineas[i]))
        i += 1
    if not filas:
        return i, ""
    cabeza = "".join("<th>%s</th>" % celda(c) for c in filas[0])
    cuerpo = "".join(
        "<tr>%s</tr>" % "".join("<td>%s</td>" % celda(c) for c in fila)
        for fila in filas[1:])
    return i, "<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>" % (
        cabeza, cuerpo)


def _lista(lineas, i):
    numerada = bool(_NUMERADA.match(lineas[i]))
    puntos = []
    while i < len(lineas):
        m = _NUMERADA.match(lineas[i]) if numerada else _VINETA.match(lineas[i])
        if not m:
            break
        puntos.append("<li>%s</li>" % en_linea(m.group(2)))
        i += 1
    etiqueta = "ol" if numerada else "ul"
    return i, "<%s>%s</%s>" % (etiqueta, "".join(puntos), etiqueta)


def _cita(lineas, i):
    """Lo citado se convierte **por dentro**, no se pega como texto.

    Una cita de este repositorio puede traer una tabla, una lista o un bloque
    de código adentro. Pegarla como prosa dejaba las barras de la tabla a la
    vista: se midió sobre el entregable real y eran 31.
    """
    adentro = []
    while i < len(lineas) and _CITA.match(lineas[i]):
        adentro.append(_CITA.match(lineas[i]).group(1))
        i += 1
    salto = chr(10)
    return i, "<blockquote>%s</blockquote>" % a_marcado(salto.join(adentro))


def _parrafo(lineas, i):
    adentro = []
    while (i < len(lineas) and lineas[i].strip()
           and not _ENCABEZADO.match(lineas[i])
           and not _FILA.match(lineas[i])
           and not _VINETA.match(lineas[i])
           and not _NUMERADA.match(lineas[i])
           and not _CITA.match(lineas[i])
           and not _CERCA.match(lineas[i])
           and not _SEPARADOR.match(lineas[i])):
        adentro.append(en_linea(lineas[i].strip()))
        i += 1
    return i, "<p>%s</p>" % " ".join(adentro)
