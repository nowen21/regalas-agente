# -*- coding: utf-8 -*-
"""Qué reglas pide **esta** solicitud del usuario.

**El problema que cierra.** Al abrir la sesión, las reglas llegan cortadas: la
herramienta guarda aparte todo lo que pase de su tope y deja ver solo el
comienzo. Leer el resto depende de que el agente se acuerde, y cuando no se
acuerda trabaja sin la regla y nadie se entera.

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


def tareas_del_mensaje(mensaje, raiz=None):
    """`{tarea: palabras del mensaje que la señalan}`, sin las que van siempre."""
    dichas = _palabras(mensaje)
    salida = {}
    for tarea, suyas in mapa_tareas.palabras(raiz or RAIZ).items():
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
    partes = [regla.encabezado.strip()]
    partes += [t for _, t in regla.cuerpo]
    ejemplo = _ejemplo(regla)
    if ejemplo:
        partes.append("```\n" + ejemplo + "\n```")
    return "\n".join(p for p in partes if p).strip()


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


# Palabras que en este repositorio están en todas partes y no distinguen una
# regla de otra. **Solo pesan fuera del orden**, no de reconocer la tarea: «cree
# una regla» sí es cambiar el estándar, pero «reglas» en el título no dice cuál
# regla viene al caso. Lo aprendió el recuperador anterior el 2026-09-16, y se
# volvió a ver el 2026-09-28: «aplique las reglas de redacción» ponía delante
# `M7` y `M11` por decir «reglas», y dejaba afuera `ID8`.
_GENERICAS = frozenset("""
regla reglas estandar archivo archivos proyecto proyectos cambio cambios cambiar
cambie nuevo nueva nuevos nuevas cosa cosas parte partes caso casos tema temas
trabajo trabajar tarea tareas agente herramienta aplique aplicar hacer haga
""".split())


def _con_contenido(palabras):
    """Sin las palabras cortas («el», «del») ni las que están en todas partes."""
    return {p for p in palabras if len(p) >= 4 and p not in _GENERICAS}


def _afinidad(regla, dichas):
    """Cuántas palabras con contenido del mensaje están en el título de la regla.

    **No elige: ordena.** Dentro de una tarea con muchas reglas, las que
    comparten palabras con el pedido van primero, para que sean las que entren
    completas si el presupuesto no alcanza para todas.
    """
    return len(_con_contenido(dichas) & _palabras(regla.titulo))


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
    dichas = _palabras(mensaje)

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
    for tarea, comunes in tareas_del_mensaje(mensaje, raiz).items():
        motivo = "tarea `%s`: el mensaje dice «%s»" % (tarea, "», «".join(sorted(comunes)))
        for regla in por_tarea.get(tarea, []):
            if rige(regla.id):
                motivos.setdefault(regla.id, motivo)
    for id, motivo in _cadena(list(motivos), idx).items():
        if rige(id):
            motivos.setdefault(id, motivo)

    # El orden, de lo que más pesa a lo que menos: lo citado; lo blindado; y
    # después un puntaje: dos puntos por cada palabra del pedido en el título,
    # y uno si la regla además rige todo mensaje (en un pedido de redacción,
    # las reglas de cómo se escribe). A igual puntaje, el orden de `base/`.
    def orden(id):
        regla = idx[id]
        citada = motivos[id].startswith("el mensaje la cita")
        puntaje = 2 * _afinidad(regla, dichas) + (1 if id in fijas else 0)
        return (0 if citada else 1, 0 if regla.blindada else 1, -puntaje,
                regla.capitulo, regla.linea)

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
        if len(_armar(prueba, resto, fijas, idx, raiz).encode("utf-8")) <= tope:
            elegidas = prueba
    return elegidas, fuera({i for i, _ in elegidas}), fijas


_ENCABEZADO = ("[REGLAS QUE PIDE ESTA SOLICITUD, RECUPERADAS Y OBLIGATORIAS]\n"
               "Rigen esta respuesta igual que las del arranque. Ante cualquier "
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


def _bloque_descartadas(ids, idx):
    """Las que no cupieron, en una línea: dónde vive cada una lo dice el mapa."""
    if not ids:
        return ""
    return ("[DE LAS TAREAS DE ESTE MENSAJE, NO CUPIERON: leerlas antes de "
            "tocar su tema; dónde vive cada una lo dice base/mapa-de-tareas.md]\n  "
            + ", ".join("%s·%s" % (idx[i].capitulo, i) for i in ids) + "\n")


def _bloque_siempre(fijas, idx, raiz):
    """Las reglas de todo mensaje: identificador, título y dónde viven."""
    if not fijas:
        return ""
    # Sin la ruta de cada una: la dice el mapa, y así el bloque ocupa la mitad y
    # deja lugar para que entren completas las de la tarea del mensaje.
    lineas = ["[LAS QUE RIGEN TODO MENSAJE: se leen antes de responder; dónde "
              "vive cada una lo dice base/mapa-de-tareas.md]"]
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
    elegidas, descartadas, fijas = elegir(mensaje, raiz, tope, proyecto)
    if not elegidas and not fijas:
        return ""
    return _armar(elegidas, descartadas, fijas, idx, raiz)


def _armar(elegidas, descartadas, fijas, idx, raiz):
    """El texto tal como se inyecta. Lo usan `como_texto` y la medición."""
    lineas = [_ENCABEZADO]
    for id, motivo in elegidas:
        lineas.append(_pieza(idx[id], motivo).rstrip("\n") + "\n")
    if descartadas:
        lineas.append(_bloque_descartadas(descartadas, idx))
    # La que ya va completa no se repite en el bloque de todo mensaje.
    completas = {i for i, _ in elegidas}
    bloque = _bloque_siempre([i for i in fijas if i not in completas], idx, raiz)
    if bloque:
        lineas.append(bloque)
    return "\n".join(lineas).strip()


if __name__ == "__main__":
    comun.no_es_punto_de_entrada("recuperar")
