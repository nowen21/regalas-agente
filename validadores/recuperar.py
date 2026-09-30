# -*- coding: utf-8 -*-
"""Qué reglas pide **esta** solicitud del usuario.

**El problema que cierra.** Al abrir la sesión no se cargan las reglas: la
herramienta acepta 10.000 caracteres por enganche y el cuerpo de reglas pesa
mucho más (`EP-005·HU-009·CA-04`). Si leerlas dependiera de que el agente se
acuerde, trabajaría sin la regla y nadie se enteraría.

**Lo que hace.** Lee el mensaje del usuario, reconoce qué tareas pide y le
entrega al agente las reglas que el mapa de tareas pone bajo ellas:

- las de las tareas que van en **todo** mensaje (`recibir-pedido` y
  `responder`), con su título y dónde viven;
- las de las tareas que **este** mensaje pide, con su texto completo mientras
  quepan en el presupuesto, y nombradas las que no quepan.

**Por qué por tareas y no por semejanza** (`EP-005·HU-023`, fase `B`). Hasta el
2026-09-28 elegía comparando palabras del mensaje con el título de cada regla,
más una lista de disparadores. Con los mensajes reales de esa sesión falló:
«suba a git» no trajo nada, porque solo comparaba palabras de cuatro letras o
más y no reconocía «suba» como «subir»; un pedido de redacción trajo una regla
de índices y ninguna de las de redacción, porque excluía los capítulos `00` y
`01` suponiendo que habían llegado al arrancar. Cada regla dice ahora a qué
tareas aplica, y las palabras que señalan cada tarea están escritas en
`base/tareas.md`: no hay nada que adivinar.

**La derogada nunca va.** Inyectar una regla que dejó de regir es peor que no
inyectar ninguna.
"""
import os
import re
import unicodedata

import comun
import mapa_tareas
import metareglas
from comun import RAIZ, leer

# Cuánto se permite inyectar por turno. Por encima de 10 KB, la herramienta
# guarda la salida del enganche en un archivo aparte y deja ver solo el
# comienzo, que es lo que le pasó al arranque. El enganche que llama a este
# recuperador le suma su recordatorio fijo y la medición de la respuesta
# anterior, así que se le dejan 1,5 KB: medido el 2026-09-28, esas dos partes
# juntas no pasan de 1 KB.
TOPE = 10 * 1024 - 1536

# Un identificador citado en el mensaje: `02·F24`, `F24`, `13·DOC22`. Se acepta
# solo si existe en el índice, que es lo que descarta un `B2C` o un `PPT`.
_CITA = re.compile(r"(?:(\d{2})·)?\b([A-Z]{1,4}\d+(?:\.\d+)?)\b")

# Los siete capítulos que son patrones opt-in: rigen solo si el proyecto los
# encendió en el punto 5.1 de su `CLAUDE.md`. Ofrecer una regla de un capítulo
# apagado es peor que no ofrecer ninguna: el agente aplica algo que en este
# proyecto no rige.
_OPT_IN = re.compile(r"Patr[oó]n opt-in\s*`?(\d{2})`?[^:]*:\**\s*(.+)")

# La marca del encabezado no hace falta en el bloque de todo mensaje.
_MARCA = re.compile(r"\s*(`\[[^\]]+\]`|\*opt-in\*)\s*$")


def opt_in_apagados(proyecto):
    """Los capítulos opt-in que este proyecto dejó en `no`.

    Se leen del `CLAUDE.md` del proyecto, que es donde el punto 5.1 los
    declara. Sin proyecto o sin archivo no se apaga nada: el recuperador
    prefiere ofrecer de más antes que callar una regla que sí rige.
    """
    if not proyecto:
        return frozenset()
    ruta = os.path.join(proyecto, "CLAUDE.md")
    if not os.path.isfile(ruta):
        return frozenset()
    try:
        texto = leer(ruta)
    except Exception:                     # noqa: BLE001 — nunca romper el turno
        return frozenset()
    apagados = set()
    for linea in texto.splitlines():
        m = _OPT_IN.search(linea)
        if not m:
            continue
        valor = _limpio(m.group(2)).strip(" *`.«»")
        if not valor.startswith("si"):
            apagados.add(m.group(1))
    return frozenset(apagados)


def _limpio(texto):
    """Minúsculas y sin tildes, que es como se comparan dos palabras acá."""
    sin = unicodedata.normalize("NFKD", texto or "")
    sin = "".join(c for c in sin if not unicodedata.combining(c))
    return sin.lower()


def _palabras(texto):
    """Todas las palabras, de cualquier largo: «git» cuenta igual que «commit»."""
    return set(re.findall(r"[a-z0-9]+", _limpio(texto)))


# Lo que el editor le agrega al mensaje sin que el usuario lo escriba: qué
# archivo tiene abierto y qué seleccionó. Visto en uso el 2026-09-28: «qué
# sigue?» traía reglas de documentos y de la cadena porque la ruta del archivo
# abierto decía `.md`, `HU` y `plan`.
_DEL_EDITOR = re.compile(r"<(ide_[a-z_]+|system-reminder)>.*?</\1>", re.S)


def _lo_que_escribio(mensaje):
    """El mensaje sin lo que agregó el editor."""
    return _DEL_EDITOR.sub(" ", mensaje or "")


def indice(raiz=None):
    """`{id: regla}` de todas las reglas de `base/`, como las lee `metareglas`."""
    return {r.id: r for r in metareglas.reglas(raiz or RAIZ)}


# Donde empieza una frase: el comienzo del mensaje, o después de un punto, un
# signo de cierre o un salto de línea.
_FRASE = re.compile(r"(?:^|[.!?\n])\s*[¿¡«\"'(]*\s*([a-z0-9]+)")


def palabras_de_inicio(mensaje):
    """La primera palabra de cada frase del mensaje, sin tildes y en minúscula."""
    return [m.group(1) for m in _FRASE.finditer(_limpio(mensaje))]


PALABRAS = "base/01-conducta/palabras-clave.md"

# Una fila de la lista cerrada: la palabra en negrita y, si trae, sus otras
# formas después de la coma («**Hágalo**, aplique»).
_FILA_PALABRA = re.compile(r"^\|\s*\*\*([^*]+)\*\*([^|]*)\|")


def palabras_de_la_lista(raiz=None):
    """`[palabra]` de `01·C28`, en el orden de la lista y como se escriben."""
    ruta = os.path.join(raiz or RAIZ, *PALABRAS.split("/"))
    try:
        texto = leer(ruta)
    except OSError:
        return []
    salida = []
    for linea in texto.splitlines():
        m = _FILA_PALABRA.match(linea.strip())
        if m:
            salida.append(m.group(1).strip())
            salida += [p.strip() for p in m.group(2).split(",") if p.strip()]
    return salida


def trae_palabra_clave(mensaje, raiz=None):
    """¿Alguna frase del mensaje abre con una palabra de `01·C28`?"""
    lista = {_limpio(p) for p in palabras_de_la_lista(raiz)}
    return bool(lista & set(palabras_de_inicio(_lo_que_escribio(mensaje))))


def aviso_sin_palabra(raiz=None):
    """`EP-005·HU-023` · Lo que recibe el agente cuando el mensaje no trae la palabra.

    El usuario lo pidió el 2026-09-29: sin la palabra, el agente no actúa,
    recuerda la lista y espera; con la palabra de la respuesta se eligen las
    reglas. No lee ni muestra nada más.
    """
    lista = ", ".join("«%s»" % p for p in palabras_de_la_lista(raiz))
    return ("[EL MENSAJE NO ABRE CON UNA PALABRA DE `01·C28`]\n"
            "No hacer nada: recordarle al usuario, en una línea, que falta la "
            "palabra que dice qué se espera, y esperar su respuesta. Las "
            "palabras son: " + lista + ".")


def tareas_del_mensaje(mensaje, raiz=None):
    """`{tarea: palabras clave que la piden}`, sin las que van siempre.

    `EP-005·HU-023·RN-07` · **Solo cuenta la palabra clave** de `01·C28`, y solo
    donde esa regla dice que va: abriendo el mensaje o una de sus frases. Las
    demás palabras no cuentan. Hasta la fase `C` contaba cualquier palabra, y
    «reglas» en una pregunta traía las reglas de cambiar el estándar.
    """
    dichas = set(palabras_de_inicio(_lo_que_escribio(mensaje)))
    salida = {}
    for tarea, suyas in mapa_tareas.palabras_clave(raiz or RAIZ).items():
        comunes = dichas & suyas
        if comunes:
            salida[tarea] = comunes
    return salida


def _ejemplo(regla):
    """El bloque `INCORRECTO / CORRECTO` de la regla, o `""`.

    `regla.ejemplo` es un booleano, no el texto: el texto hay que sacarlo del
    archivo, y vale la pena, porque el ejemplo evita interpretar mal el cuerpo.
    """
    dentro, bloque = False, []
    for linea in (regla.texto or "").splitlines():
        if linea.startswith("```"):
            if dentro:
                break
            dentro = True
            continue
        if dentro:
            bloque.append(linea)
    texto = "\n".join(bloque).strip()
    return texto if "INCORRECTO" in texto else ""


def _cuerpo(regla):
    """Lo que se inyecta de una regla: encabezado, cuerpo y ejemplo, sin el sello."""
    return mapa_tareas.cuerpo(regla)


def _citadas(mensaje, idx):
    """Los identificadores que el mensaje nombra, si de verdad existen."""
    encontrados = []
    for m in _CITA.finditer(mensaje or ""):
        id = m.group(2)
        if id in idx and id not in encontrados:
            encontrados.append(id)
    return encontrados


def _cadena(ids, idx):
    """Lo que las elegidas extienden, derogan o de lo que dependen."""
    salida = {}
    for id in ids:
        regla = idx.get(id)
        if not regla:
            continue
        for forma, otro in metareglas._dependencias(regla):
            if otro in idx and otro not in ids:
                salida.setdefault(otro, "%s `%s`" % (forma, id))
    return salida


def elegir(mensaje, raiz=None, tope=TOPE, proyecto=None):
    """`(elegidas, descartadas, siempre)` para este mensaje.

    - `elegidas`: `[(id, motivo)]` que entran con su texto completo, ya
      recortadas al presupuesto que deja el bloque de `siempre`.
    - `descartadas`: las de las tareas del mensaje que no cupieron. Van
      **nombradas**: un recuperador que no dice qué dejó afuera repite el
      defecto del arranque, que fallaba en silencio.
    - `siempre`: `[id]` de las reglas de las tareas que van en todo mensaje.
    """
    raiz = raiz or RAIZ
    mensaje = _lo_que_escribio(mensaje)
    idx = indice(raiz)
    por_tarea = mapa_tareas.reglas_por_tarea(raiz)
    apagados = opt_in_apagados(proyecto)

    def rige(id):
        return (id in idx and not idx[id].derogada
                and idx[id].capitulo not in apagados)

    fijas = []
    for tarea in mapa_tareas.siempre(raiz):
        for regla in por_tarea.get(tarea, []):
            if rige(regla.id) and regla.id not in fijas:
                fijas.append(regla.id)

    # **La cita explícita manda:** si el mensaje nombra la regla, el usuario la
    # está pidiendo, y llega aunque su capítulo opt-in esté apagado, con la
    # advertencia al lado.
    motivos = {}
    for id in _citadas(mensaje, idx):
        if idx[id].derogada:
            continue
        motivos[id] = "el mensaje la cita"
        if idx[id].capitulo in apagados:
            motivos[id] += " (capítulo opt-in, apagado en este proyecto)"
    del_mensaje = tareas_del_mensaje(mensaje, raiz)
    for tarea, comunes in del_mensaje.items():
        motivo = "tarea `%s`: palabra clave «%s»" % (tarea, "», «".join(sorted(comunes)))
        for regla in por_tarea.get(tarea, []):
            if rige(regla.id):
                motivos.setdefault(regla.id, motivo)
    for id, motivo in _cadena(list(motivos), idx).items():
        if rige(id):
            motivos.setdefault(id, motivo)

    # El orden, de lo que más pesa a lo que menos: lo citado, lo blindado, lo
    # que además rige todo mensaje, y después el orden de `base/`. Nada se
    # ordena por parecido de palabras: lo que no cabe está completo en el
    # archivo de su tarea.
    def orden(id):
        regla = idx[id]
        citada = motivos[id].startswith("el mensaje la cita")
        return (0 if citada else 1, 0 if regla.blindada else 1,
                0 if id in fijas else 1, regla.capitulo, regla.linea)

    # **Todo lo que se inyecta cuenta contra el tope**: el encabezado, las
    # completas, la lista de las que no cupieron y las de todo mensaje. Se mide
    # el texto que de verdad saldría, regla por regla.
    candidatas = sorted(motivos, key=orden)
    elegidas = []
    # La que rige todo mensaje y no cupo completa ya llega en su bloque: no se
    # repite entre las que no cupieron.
    def fuera(dentro):
        return [i for i in candidatas if i not in dentro and i not in fijas]

    for id in candidatas:
        prueba = elegidas + [(id, motivos[id])]
        resto = fuera({i for i, _ in prueba})
        if len(_armar(prueba, resto, fijas, idx, raiz,
                      list(del_mensaje)).encode("utf-8")) <= tope:
            elegidas = prueba
    return elegidas, fuera({i for i, _ in elegidas}), fijas


_ENCABEZADO = ("[REGLAS QUE PIDE ESTA SOLICITUD, RECUPERADAS Y OBLIGATORIAS]\n"
               "Rigen esta respuesta. Ante cualquier "
               "choque gana el núcleo, y el desempate es el de `20·M6`.\n")


def _pieza(regla, motivo):
    """Lo que ocupa una regla completa en el texto: su línea de motivo y su cuerpo.

    Se mide el texto exacto que se inyecta, no una estimación: con un motivo
    largo, calcularlo por encima dejaba el total unos bytes sobre el tope.
    """
    sello = " `[BLINDADA]`" if regla.blindada else ""
    return "<<< %s·%s%s  ·  %s >>>\n%s\n\n" % (regla.capitulo, regla.id, sello,
                                               motivo, _cuerpo(regla))


def _donde(regla, raiz):
    return os.path.relpath(regla.archivo, raiz).replace(os.sep, "/")


def _archivos(tareas, raiz):
    """Los archivos de reglas completas de esas tareas, relativos a `raiz`."""
    salida = []
    for t in tareas:
        for ruta in mapa_tareas.archivos_de(t, raiz):
            salida.append(os.path.relpath(ruta, raiz).replace(os.sep, "/"))
    return salida


def _bloque_descartadas(ids, idx, tareas=(), raiz=None):
    """Las que no cupieron, y el archivo donde están completas."""
    if not ids:
        return ""
    donde = ", ".join(_archivos(tareas, raiz or RAIZ)) or "base/reglas-por-tarea/"
    return ("[DE LAS TAREAS DE ESTE MENSAJE, NO CUPIERON: están completas en "
            + donde + "]\n  "
            + ", ".join("%s·%s" % (idx[i].capitulo, i) for i in ids) + "\n")


def _bloque_siempre(fijas, idx, raiz):
    """Las reglas de todo mensaje: identificador, título y dónde viven."""
    if not fijas:
        return ""
    # Sin la ruta de cada una: la dice el mapa, y así el bloque ocupa la mitad y
    # deja lugar para que entren completas las de la tarea del mensaje.
    donde = ", ".join(_archivos(mapa_tareas.siempre(raiz), raiz))
    lineas = ["[LAS QUE RIGEN TODO MENSAJE: completas en %s]" % donde]
    for id in fijas:
        regla = idx[id]
        lineas.append("  %s·%s · %s" % (regla.capitulo, id, _MARCA.sub("", regla.titulo)))
    return "\n".join(lineas)


def como_texto(mensaje, raiz=None, tope=TOPE, proyecto=None):
    """El bloque que se le inyecta al agente, o `""` si no hay reglas que dar.

    **Dice qué trae y por qué.** Un recuperador que entrega reglas sin decir
    cuáles eligió no se puede auditar.
    """
    raiz = raiz or RAIZ
    idx = indice(raiz)
    if not trae_palabra_clave(mensaje, raiz):
        # La regla que el mensaje cita llega igual: «00 id9» corrige la
        # respuesta anterior, y el agente necesita el texto de lo que se cita.
        piezas = [_pieza(idx[i], "el mensaje la cita")
                  for i in _citadas(_lo_que_escribio(mensaje), idx)
                  if not idx[i].derogada]
        return (aviso_sin_palabra(raiz) + "\n\n" + "".join(piezas)).strip()
    elegidas, descartadas, fijas = elegir(mensaje, raiz, tope, proyecto)
    if not elegidas and not fijas:
        return ""
    return _armar(elegidas, descartadas, fijas, idx, raiz,
                  list(tareas_del_mensaje(mensaje, raiz)))


def _armar(elegidas, descartadas, fijas, idx, raiz, tareas=()):
    """El texto tal como se inyecta. Lo usan `como_texto` y la medición."""
    lineas = [_ENCABEZADO]
    for id, motivo in elegidas:
        lineas.append(_pieza(idx[id], motivo).rstrip("\n") + "\n")
    if descartadas:
        lineas.append(_bloque_descartadas(descartadas, idx, tareas, raiz))
    # La que ya va completa no se repite en el bloque de todo mensaje.
    completas = {i for i, _ in elegidas}
    bloque = _bloque_siempre([i for i in fijas if i not in completas], idx, raiz)
    if bloque:
        lineas.append(bloque)
    return "\n".join(lineas).strip()


if __name__ == "__main__":
    comun.no_es_punto_de_entrada("recuperar")
