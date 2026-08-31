# -*- coding: utf-8 -*-
"""Qué le tocó repetir al usuario. **Muestra el patrón; no decide la regla.**

Una corrección que se repite no es un descuido de quien corrige: es una regla
que falta. Hoy ese patrón se pierde en archivos que nadie vuelve a abrir, y esto
lo saca a la luz — ordenado, con cuántas veces y en qué sesiones.

**Qué cuenta como corrección** (`RN-6` de la especificación, decidido con el
usuario el 2026-08-31): **todo mensaje del usuario, menos una lista cerrada de
confirmaciones**. Ningún programa lee intención; lo que sí puede es no contar
«si», «hágale» ni «siga», que son la mitad de lo que se escribe y no corrigen
nada. La lista está abajo, es corta, y se lee.

**Cómo se agrupa lo mismo dicho distinto** (`RN-2`). Dos correcciones cuentan
como una cuando **comparten una frase** de dos palabras con contenido. Es lo que
hace que estas tres salgan como una sola:

    «adapte la plantilla al español colombiano»
    «recuerde el español colombiano»
    «pero español colombiano cómo sería»

**Se agrupa por la frase, no en cadena.** Si A se pareciera a B y B a C, juntar
las tres terminaría metiendo en un mismo montón cosas que no tienen nada que
ver: basta una cadena larga para que el reporte diga que todo es lo mismo. Acá
cada frase repetida es una fila, y un mensaje puede aparecer en dos filas si
repitió dos cosas — que es lo que de verdad pasó.

**No sale a la red y no instala nada** (`RNF-03`): cuenta palabras.
"""
import re
import unicodedata

from .models import Mensaje

# **La lista cerrada, y se lee.** Son las respuestas con las que se acepta o se
# manda seguir: no corrigen nada, y sin sacarlas encabezarían el reporte.
CONFIRMACIONES = (
    "si", "sí", "no", "ok", "okay", "dale", "listo", "bueno", "dele",
    "hagale", "hágale", "hagalo", "hágalo", "haga", "siga", "sigue",
    "continua", "continúa", "adelante", "correcto", "exacto", "perfecto",
    "gracias", "vale", "aprobado", "apruebo", "de una", "hazlo", "gg",
)

# Palabras que aparecen en todo y no dicen de qué se trata. Sin esta lista, la
# frase más repetida del reporte sería «de la».
PALABRAS_VACIAS = (
    "a", "al", "algo", "ahi", "ahora", "aqui", "asi", "como", "con", "cual",
    "cuando", "de", "del", "desde", "donde", "e", "el", "ella", "ello", "en",
    "esa", "ese", "eso", "esta", "este", "esto", "hay", "la", "las", "le",
    "les", "lo", "los", "mas", "me", "mi", "muy", "ni", "nos", "o", "otra",
    "otro", "para", "pero", "por", "porque", "que", "se", "sea", "ser", "si",
    "sin", "sobre", "su", "sus", "tambien", "tan", "te", "todo", "toda",
    "todos", "todas", "un", "una", "uno", "unos", "unas", "y", "ya",
)

# Un mensaje muy corto que no es confirmación tampoco dice nada que se pueda
# agrupar. El umbral no sale de una teoría: sale de que por debajo de eso no
# caben dos palabras con contenido, que es lo que la agrupación necesita.
LARGO_MINIMO = 12

# Cuántas veces hay que haber repetido algo para que sea «repetido». Dos.
VECES_MINIMAS = 2

# **Una frase hecha con las palabras de todos los días no señala nada.** El
# primer reporte lo encabezaban «debe quedar», «debe tener» y «debe estar»: no
# son correcciones, es la forma en que el usuario redacta cualquier exigencia.
# Una palabra que aparece en más de esta parte de las sesiones es vocabulario
# de la casa, no tema.
#
# **Se calcula, no se escribe.** Una lista a mano acierta en las palabras que
# uno se imagina y envejece con el proyecto; esta sale de lo que hay (`S-091`).
PARTE_QUE_ES_VOCABULARIO = 0.25

# **Con pocas sesiones no hay vocabulario de la casa que calcular.** Sobre tres
# conversaciones, cualquier palabra dicha dos veces pasa el umbral y el filtro
# se lleva todo. Por debajo de esto no se filtra, y se dice acá en vez de
# dejar un reporte vacío que se lee como «no hubo nada».
SESIONES_PARA_CALCULAR_VOCABULARIO = 8

# En cuántas sesiones distintas tiene que aparecer para contar como patrón.
# Repetir algo tres veces el mismo día es insistir; repetirlo en tres días
# distintos es una regla que falta.
SESIONES_MINIMAS = 2

_NO_LETRA = re.compile(r"[^\w\s]", re.UNICODE)
_ESPACIOS = re.compile(r"\s+")

# **Lo que la herramienta le pega al mensaje no es lo que la persona escribió.**
# El editor agrega qué archivo está abierto y qué líneas hay seleccionadas, y el
# estándar agrega sus recordatorios. Sin sacarlo, el reporte lo encabezaban
# frases como «this may» y «current task», repetidas 139 veces: se midió el
# 2026-08-31 antes de sacarlo, y por eso queda escrito.
_ETIQUETAS = (
    "ide_selection", "ide_opened_file", "ide_diagnostics", "system-reminder",
    "command-name", "command-message", "command-args", "local-command-stdout",
    "local-command-stderr", "task-notification",
)

_DE_LA_MAQUINA = re.compile(
    "(?is)" + "|".join(
        "<%s>.*?</%s>" % (e, e) for e in _ETIQUETAS)
    + "|<[^>]{1,60}/>")


def _sin_tildes(texto):
    return "".join(c for c in unicodedata.normalize("NFD", texto)
                   if unicodedata.category(c) != "Mn")


# **Una ruta de archivo no es una frase.** Al pegar `c:\Ing. Jose\ia\agente` en
# un mensaje, el nombre de la carpeta se cuenta como si el usuario lo hubiera
# dicho: «ing jose» encabezaba el reporte con doce sesiones. Es el mismo caso que
# lo que pega el editor — está en el mensaje y no es lo que se dijo.
_RUTA = re.compile(r"\S*[/\\]\S*")


def sin_lo_de_la_maquina(texto):
    """El mensaje sin lo que la herramienta le pegó. Lo que quedó lo escribió una persona."""
    return _RUTA.sub(" ", _DE_LA_MAQUINA.sub(" ", texto or ""))


def normalizar(texto):
    """El texto comparable: sin lo de la máquina, sin tildes, sin signos, en minúsculas."""
    limpio = _sin_tildes(sin_lo_de_la_maquina(texto).lower())
    return _ESPACIOS.sub(" ", _NO_LETRA.sub(" ", limpio)).strip()


def es_correccion(texto):
    """Si ese mensaje del usuario cuenta como corrección (`RN-6`)."""
    normal = normalizar(texto)
    if not normal or normal in CONFIRMACIONES:
        return False
    if len(normal) < LARGO_MINIMO:
        # Lo corto que no está en la lista tampoco alcanza para agrupar. Se
        # deja fuera **y se dice acá**, para que nadie lo lea como un olvido.
        return False
    return True


def frases_de(texto):
    """Las parejas de palabras con contenido, en orden. Sin repetir."""
    palabras = [p for p in normalizar(texto).split(" ")
                if p and p not in PALABRAS_VACIAS and len(p) > 2]
    salida = []
    for i in range(len(palabras) - 1):
        frase = "%s %s" % (palabras[i], palabras[i + 1])
        if frase not in salida:
            salida.append(frase)
    return salida


def vocabulario_de_la_casa(mensajes):
    """Las palabras que aparecen en tantas sesiones que ya no dicen de qué se trata.

    **Se calculan sobre lo que hay, no se escriben a mano.** Una lista escrita
    acierta en las palabras que uno se imagina —«debe», «archivo»— y envejece
    con el proyecto: el día que el trabajo cambie de tema, la lista vieja deja
    pasar el vocabulario nuevo y sigue tapando el viejo.
    """
    sesiones = set()
    donde = {}
    for mensaje in mensajes:
        if not es_correccion(mensaje.texto):
            continue
        sesiones.add(mensaje.sesion.archivo)
        for palabra in set(normalizar(mensaje.texto).split(" ")):
            if palabra and palabra not in PALABRAS_VACIAS and len(palabra) > 2:
                donde.setdefault(palabra, set()).add(mensaje.sesion.archivo)
    if len(sesiones) < SESIONES_PARA_CALCULAR_VOCABULARIO:
        return set()
    tope = len(sesiones) * PARTE_QUE_ES_VOCABULARIO
    return {p for p, s in donde.items() if len(s) > tope}


def correcciones(desde=None, hasta=None, proyecto=None,
                 veces_minimas=VECES_MINIMAS,
                 sesiones_minimas=SESIONES_MINIMAS, limite=20):
    """Lo repetido, de lo más repetido a lo menos.

    Devuelve `[{"frase","veces","sesiones"}]`. Lista vacía cuando no hubo nada
    repetido, que **no es lo mismo** que no haber mirado: quien llama lo
    distingue con `cuantas_correcciones`.
    """
    mensajes = Mensaje.objects.filter(quien="usuario").select_related("sesion")
    if proyecto is not None:
        mensajes = mensajes.filter(sesion__proyecto=proyecto)
    if desde:
        mensajes = mensajes.filter(sesion__fecha__gte=desde)
    if hasta:
        mensajes = mensajes.filter(sesion__fecha__lte=hasta)

    de_la_casa = vocabulario_de_la_casa(list(mensajes))

    montones = {}
    for mensaje in mensajes.iterator():
        if not es_correccion(mensaje.texto):
            continue
        for frase in frases_de(mensaje.texto):
            # **Lo hecho con el vocabulario de todos los días no señala nada.**
            # «debe quedar» encabezaba el reporte con 22 repeticiones, y no es
            # una corrección: es la forma de redactar cualquier exigencia.
            if any(p in de_la_casa for p in frase.split(" ")):
                continue
            monton = montones.setdefault(frase, {"veces": 0, "sesiones": []})
            monton["veces"] += 1
            if mensaje.sesion.archivo not in monton["sesiones"]:
                monton["sesiones"].append(mensaje.sesion.archivo)

    repetidas = [{"frase": f, "veces": d["veces"], "sesiones": d["sesiones"]}
                 for f, d in montones.items()
                 if d["veces"] >= veces_minimas
                 and len(d["sesiones"]) >= sesiones_minimas]
    # **Primero lo que aparece en más días distintos.** Repetir algo tres veces
    # el mismo día es insistir en una conversación; repetirlo en tres días es
    # una regla que falta. Entre iguales, por la frase: dos corridas sobre los
    # mismos datos tienen que dar la misma lista.
    repetidas.sort(key=lambda r: (-len(r["sesiones"]), -r["veces"], r["frase"]))
    return repetidas[:limite]


def cuantas_correcciones(desde=None, hasta=None, proyecto=None):
    """Cuántos mensajes del período cuentan como corrección.

    Separa **«no hubo nada repetido»** de **«no había nada que mirar»**. Las dos
    devuelven una lista vacía y no significan lo mismo.
    """
    mensajes = Mensaje.objects.filter(quien="usuario")
    if proyecto is not None:
        mensajes = mensajes.filter(sesion__proyecto=proyecto)
    if desde:
        mensajes = mensajes.filter(sesion__fecha__gte=desde)
    if hasta:
        mensajes = mensajes.filter(sesion__fecha__lte=hasta)
    return sum(1 for m in mensajes.iterator() if es_correccion(m.texto))
