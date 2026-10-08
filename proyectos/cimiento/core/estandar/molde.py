# -*- coding: utf-8 -*-
"""`EP-027·HU-001` · El molde de la regla, leído y armado.

**Sin Django**: lo usan la base, para guardar cada regla en sus casillas, y
cualquier lector que necesite el texto. Dos operaciones, una contraria de la
otra:

- `leer(bloque)` parte el texto de una regla en las casillas del molde
  (`20·M5`, `base/20-meta-reglas/estructura-regla.md`);
- `armar(casillas)` vuelve a escribir el texto desde las casillas.

`armar(leer(x))` da el texto de `x` escrito con el orden del molde: lo único que
puede cambiar es el espacio entre las partes y, en las pocas reglas que lo traían
de otra forma, el orden de esas partes. Lo prueba `tests_molde_casillas.py`
contra todas las reglas del estándar.
"""
import re

# `EP-027·HU-006` · La regla de un proyecto puede ir en `###`, bajo un grupo `##`.
ENCABEZADO = re.compile(r"^(#{2,3}) ([A-Z]+\d+(?:\.\d+)?) · (.+?)\s*$")
_CERCA = re.compile(r"^\s*(```|~~~)")
_TITULO_CUALQUIERA = re.compile(r"^(#{1,6}) ")
_MARCA = re.compile(r"(\s*(?:·\s*)?`\[[^\]]*\]`|\s*—\s*\*opt-in\*)$")
_EXCEPCION = re.compile(r"^(\*\*Excepción|Excepción[:*\s—-])")
_CUMPLE = re.compile(r"^\*\*(Quién la hace cumplir|Nadie la hace cumplir):\*\*")
_APLICA = re.compile(r"^\*\*Aplica a:\*\*\s*(.*)$")
_AUTORIZA = re.compile(r"^\*\*Autoriza escribir:\*\*")
_SELLO = re.compile(r"^### Checklist")
_RAYA = re.compile(r"^---\s*$")
_PAR = re.compile(r"^\s*(INCORRECTO|CORRECTO)\s*:\s?(.*)$")
_DEPENDENCIA = re.compile(
    r"\b(extiende(?: a)?|depende de|deroga(?: a)?)\s+"
    r"((?:\[(?:[^\[\]]|\[[^\]]*\])*\]\([^)\s]+\)(?:\s*(?:,|y de|y|e|o)\s*)?)+)")
_ENLACE = re.compile(r"\[((?:[^\[\]]|\[[^\]]*\])*)\]\(([^)\s]+)\)")
_CODIGO_EN_ENLACE = re.compile(r"(?:(\d\d)·)?([A-Z]+\d+(?:\.\d+)?)")

BLINDADA, OPT_IN, DEROGADA, SIN_MARCA = "blindada", "opt-in", "derogada", ""
EXTIENDE, DEPENDE, DEROGA = "extiende", "depende de", "deroga"

# Las casillas de texto, en el orden en que el molde las escribe.
CASILLAS = ("exigencia", "excepcion", "ejemplo", "notas", "quien_cumple", "aplica_a", "autoriza_escribir")


def _sin_retorno(texto):
    return (texto or "").replace("\r\n", "\n")


def nivel_de(texto):
    """2 si alguna regla del texto va en `##`; si no, 3: así escriben los proyectos."""
    return 2 if re.search(r"(?m)^## [A-Z]+\d+(?:\.\d+)? · ", texto or "") else 3


def partir(texto, nivel=2):
    """`[(inicio, fin, código)]` de cada regla dentro del texto de un documento.
    La regla va de su encabezado `## X · …` (o `###`, con `nivel=3`) hasta el
    siguiente título de su nivel o de uno mayor, sin los renglones en blanco del
    final. Lo que está entre cercas de código no cuenta: ahí hay ejemplos, no reglas."""
    lineas = _sin_retorno(texto).split("\n")
    pos, desplazamiento = [], 0
    for linea in lineas:
        pos.append(desplazamiento)
        desplazamiento += len(linea) + 1
    inicios, titulos, dentro = [], [], False
    for i, linea in enumerate(lineas):
        if _CERCA.match(linea):
            dentro = not dentro
            continue
        titulo = _TITULO_CUALQUIERA.match(linea) if not dentro else None
        if titulo and len(titulo.group(1)) <= nivel:
            titulos.append(i)
            regla = ENCABEZADO.match(linea)
            if regla and len(regla.group(1)) == nivel:
                inicios.append(i)
    salida = []
    for i in inicios:
        fin = next((t for t in titulos if t > i), len(lineas))
        while fin > i + 1 and not lineas[fin - 1].strip():
            fin -= 1
        salida.append((pos[i], pos[fin - 1] + len(lineas[fin - 1]), ENCABEZADO.match(lineas[i]).group(2)))
    return salida


def _segmentos(lineas):
    """Los párrafos de la regla: renglones seguidos sin blanco en medio. Un bloque
    de código es un solo segmento aunque traiga renglones en blanco."""
    segmentos, actual, dentro = [], [], False
    for linea in lineas:
        if _CERCA.match(linea):
            if not dentro and actual:
                segmentos.append(actual)
                actual = []
            actual.append(linea)
            dentro = not dentro
            if not dentro:
                segmentos.append(actual)
                actual = []
        elif dentro:
            actual.append(linea)
        elif not linea.strip():
            if actual:
                segmentos.append(actual)
                actual = []
        else:
            actual.append(linea)
    if actual:
        segmentos.append(actual)
    return segmentos


def _partir_excepcion(segmento):
    """El cuerpo pegado a su excepción, sin renglón en blanco: dos segmentos."""
    for i, linea in enumerate(segmento[1:], start=1):
        if _EXCEPCION.match(linea) and not _CERCA.match(segmento[0]):
            return [segmento[:i], segmento[i:]]
    return [segmento]


def es_ejemplo(segmento):
    return bool(_CERCA.match(segmento[0])) and any(_PAR.match(l) for l in segmento[1:-1])


def marca_de(marca_texto):
    texto = (marca_texto or "").upper()
    if "DEROGADA" in texto:
        return DEROGADA
    if "BLINDADA" in texto:
        return BLINDADA
    if "OPT-IN" in texto:
        return OPT_IN
    return SIN_MARCA


def leer(bloque):
    """Las casillas de una regla, desde su texto."""
    lineas = _sin_retorno(bloque).strip("\n").split("\n")
    m = ENCABEZADO.match(lineas[0])
    if not m:
        raise ValueError("no es una regla: %r" % lineas[0][:60])
    codigo, resto = m.group(2), m.group(3)
    marca = _MARCA.search(resto)
    casillas = {c: [] for c in CASILLAS}
    cuerpo, sello, raya = lineas[1:], [], False
    for n, linea in enumerate(cuerpo):
        if _SELLO.match(linea):
            cuerpo, sello = cuerpo[:n], cuerpo[n:]
            break
    segmentos = []
    for s in _segmentos(cuerpo):
        segmentos.extend(_partir_excepcion(s))
    empezo = False
    for s in segmentos:
        primera = s[0]
        if len(s) == 1 and _RAYA.match(primera):
            raya = True
            continue
        if es_ejemplo(s) and not casillas["ejemplo"]:
            casillas["ejemplo"].append("\n".join(s[1:-1]))
        elif _EXCEPCION.match(primera) and not casillas["excepcion"]:
            casillas["excepcion"].append("\n".join(s))
        elif _CUMPLE.match(primera):
            casillas["quien_cumple"].append("\n".join(s))
        elif _APLICA.match(primera) and len(s) == 1:
            casillas["aplica_a"].append(_APLICA.match(primera).group(1).strip())
        elif _AUTORIZA.match(primera):
            casillas["autoriza_escribir"].append("\n".join(s))
        elif not empezo:
            casillas["exigencia"].append("\n".join(s))
            continue
        else:
            casillas["notas"].append("\n".join(s))
            continue
        empezo = True
    salida = {c: "\n\n".join(v) for c, v in casillas.items()}
    salida.update({
        "codigo": codigo,
        "titulo": (resto[:marca.start()] if marca else resto).strip(),
        "marca_texto": marca.group(1) if marca else "",
        "marca": marca_de(marca.group(1) if marca else ""),
        "raya": raya,
        "sello": "\n".join(sello).strip("\n"),
    })
    return salida


def armar(c, nivel=2):
    """El texto de una regla, desde sus casillas, en el orden del molde."""
    partes = ["%s %s · %s%s" % ("#" * nivel, c["codigo"], c["titulo"], c.get("marca_texto") or "")]
    for nombre in ("exigencia", "excepcion"):
        if c.get(nombre):
            partes.append(c[nombre])
    if c.get("ejemplo"):
        partes.append("```\n%s\n```" % c["ejemplo"])
    for nombre in ("notas", "quien_cumple"):
        if c.get(nombre):
            partes.append(c[nombre])
    if c.get("aplica_a"):
        partes.append("**Aplica a:** %s" % c["aplica_a"])
    if c.get("autoriza_escribir"):
        partes.append(c["autoriza_escribir"])
    if c.get("raya"):
        partes.append("---")
    if c.get("sello"):
        partes.append(c["sello"])
    return "\n\n".join(partes)


def normalizar(bloque):
    """El texto de una regla como lo escribe `armar`."""
    return armar(leer(bloque))


# --- Lo que sale de las casillas -----------------------------------------

def tareas(aplica_a):
    return [t.strip() for t in (aplica_a or "").split(",") if t.strip()]


def par_del_ejemplo(ejemplo):
    """`(incorrecto, correcto)` del ejemplo, sin las etiquetas."""
    partes, actual = {"INCORRECTO": [], "CORRECTO": []}, None
    for linea in (ejemplo or "").split("\n"):
        m = _PAR.match(linea)
        if m:
            actual = m.group(1)
            partes[actual].append(m.group(2))
        elif actual:
            partes[actual].append(linea.strip())
    return "\n".join(partes["INCORRECTO"]).strip(), "\n".join(partes["CORRECTO"]).strip()


def partes_de_la_excepcion(excepcion):
    """`(condición, límite, autoriza)`: lo que va antes de cada rótulo entre paréntesis (`20·M8`)."""
    texto = re.sub(r"^\*\*Excepción\*\*\s*[—:-]?\s*|^\*\*Excepción[^*]*\*\*\s*|^Excepción\s*[:—-]?\s*", "",
                   excepcion or "").strip()
    salida = []
    for rotulo in (r"condici[oó]n", r"l[ií]mite", r"autoriza\w*"):
        m = re.search(r"^(.*?)\s*\(%s\)\s*[;,.]?\s*(?:y\s+)?" % rotulo, texto, re.S)
        if m:
            salida.append(m.group(1).strip(" ;,"))
            texto = texto[m.end():]
        else:
            salida.append("")
    return tuple(salida)


def sello_de(sello):
    """`(resultado, versión, fecha, observación)` del sello del checklist (`20·M9`)."""
    if not sello:
        return "", "", "", ""
    primera = sello.split("\n", 1)[0].upper()
    resultado = "NO CUMPLE" if "NO CUMPLE" in primera else ("CUMPLE" if "CUMPLE" in primera else "")
    version = re.search(r"contra \*\*v?([\d.]+)\*\*", sello)
    fecha = re.search(r"el \*\*(\d{4}-\d{2}-\d{2})\*\*", sello)
    observacion = ""
    total = re.search(r"^\*\*\d+ filas:.*$", sello, re.M)
    if total:
        extra = re.sub(r"^\*\*\d+ filas:[^*]*\*\*\.?\s*", "", total.group(0)).strip()
        resto = re.sub(r"^> Vale mientras.*$", "", sello[total.end():], flags=re.M).strip()
        observacion = "\n\n".join(p for p in (extra, resto) if p)
    return resultado, version.group(1) if version else "", fecha.group(1) if fecha else "", observacion


def dependencias(*textos):
    """`[(tipo, capítulo o '', código)]` que la regla declara con `20·M7`."""
    salida = []
    for texto in textos:
        for m in _DEPENDENCIA.finditer(texto or ""):
            tipo = DEPENDE if m.group(1).startswith("depende") else (
                EXTIENDE if m.group(1).startswith("extiende") else DEROGA)
            for enlace in _ENLACE.finditer(m.group(2)):
                c = _CODIGO_EN_ENLACE.search(enlace.group(1).replace("`", ""))
                if c and (tipo, c.group(1) or "", c.group(2)) not in salida:
                    salida.append((tipo, c.group(1) or "", c.group(2)))
    return salida
