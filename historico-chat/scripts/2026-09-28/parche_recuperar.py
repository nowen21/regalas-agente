import io

p = r"C:\Ing. Jose\ia\agente\validadores\recuperar.py"
crudo = io.open(p, encoding="utf-8", newline="").read()
crlf = "\r\n" in crudo
s = crudo.replace("\r\n", "\n")


def c(viejo, nuevo):
    global s
    assert viejo in s, viejo[:70]
    s = s.replace(viejo, nuevo, 1)


c('''def tareas_del_mensaje(mensaje, raiz=None):
    """`{tarea: palabras del mensaje que la señalan}`, sin las que van siempre."""
    dichas = _palabras(mensaje)
    salida = {}
    for tarea, suyas in mapa_tareas.palabras(raiz or RAIZ).items():
        comunes = dichas & suyas
        if comunes:
            salida[tarea] = comunes
    return salida''',
'''# Donde empieza una frase: el comienzo del mensaje, o después de un punto, un
# signo de cierre o un salto de línea.
_FRASE = re.compile(r"(?:^|[.!?\\n])\\s*[¿¡«\\"'(]*\\s*([a-z0-9]+)")


def palabras_de_inicio(mensaje):
    """La primera palabra de cada frase del mensaje, sin tildes y en minúscula."""
    return [m.group(1) for m in _FRASE.finditer(_limpio(mensaje))]


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
    return salida''')

c('''# Palabras que en este repositorio están en todas partes y no distinguen una
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


''', '')

c('''    apagados = opt_in_apagados(proyecto)
    dichas = _palabras(mensaje)
''', '''    apagados = opt_in_apagados(proyecto)
''')

c('''    for tarea, comunes in tareas_del_mensaje(mensaje, raiz).items():
        motivo = "tarea `%s`: el mensaje dice «%s»" % (tarea, "», «".join(sorted(comunes)))''',
'''    for tarea, comunes in tareas_del_mensaje(mensaje, raiz).items():
        motivo = "tarea `%s`: palabra clave «%s»" % (tarea, "», «".join(sorted(comunes)))''')

c('''    # El orden, de lo que más pesa a lo que menos: lo citado; lo blindado; y
    # después un puntaje: dos puntos por cada palabra del pedido en el título,
    # y uno si la regla además rige todo mensaje (en un pedido de redacción,
    # las reglas de cómo se escribe). A igual puntaje, el orden de `base/`.
    def orden(id):
        regla = idx[id]
        citada = motivos[id].startswith("el mensaje la cita")
        puntaje = 2 * _afinidad(regla, dichas) + (1 if id in fijas else 0)
        return (0 if citada else 1, 0 if regla.blindada else 1, -puntaje,
                regla.capitulo, regla.linea)''',
'''    # El orden, de lo que más pesa a lo que menos: lo citado, lo blindado, lo
    # que además rige todo mensaje, y después el orden de `base/`. Nada se
    # ordena por parecido de palabras: lo que no cabe está completo en el
    # archivo de su tarea.
    def orden(id):
        regla = idx[id]
        citada = motivos[id].startswith("el mensaje la cita")
        return (0 if citada else 1, 0 if regla.blindada else 1,
                0 if id in fijas else 1, regla.capitulo, regla.linea)''')

c('''def _bloque_descartadas(ids, idx):
    """Las que no cupieron, en una línea: dónde vive cada una lo dice el mapa."""
    if not ids:
        return ""
    return ("[DE LAS TAREAS DE ESTE MENSAJE, NO CUPIERON: leerlas antes de "
            "tocar su tema; dónde vive cada una lo dice base/mapa-de-tareas.md]\\n  "
            + ", ".join("%s·%s" % (idx[i].capitulo, i) for i in ids) + "\\n")''',
'''def _archivos(tareas, raiz):
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
    donde = ", ".join(_archivos(tareas, raiz or RAIZ)) or "reglas-por-tarea/"
    return ("[DE LAS TAREAS DE ESTE MENSAJE, NO CUPIERON: están completas en "
            + donde + "; leerlas con Read antes de actuar]\\n  "
            + ", ".join("%s·%s" % (idx[i].capitulo, i) for i in ids) + "\\n")''')

c('''    lineas = ["[LAS QUE RIGEN TODO MENSAJE: se leen antes de responder; dónde "
              "vive cada una lo dice base/mapa-de-tareas.md]"]''',
'''    donde = ", ".join(_archivos(mapa_tareas.siempre(raiz), raiz))
    lineas = ["[LAS QUE RIGEN TODO MENSAJE: completas en %s; leerlas con Read "
              "antes de la primera respuesta]" % donde]''')

c('''    elegidas, descartadas, fijas = elegir(mensaje, raiz, tope, proyecto)
    if not elegidas and not fijas:
        return ""
    return _armar(elegidas, descartadas, fijas, idx, raiz)''',
'''    elegidas, descartadas, fijas = elegir(mensaje, raiz, tope, proyecto)
    if not elegidas and not fijas:
        return ""
    return _armar(elegidas, descartadas, fijas, idx, raiz,
                  list(tareas_del_mensaje(mensaje, raiz)))''')

c('''def _armar(elegidas, descartadas, fijas, idx, raiz):
    """El texto tal como se inyecta. Lo usan `como_texto` y la medición."""
    lineas = [_ENCABEZADO]
    for id, motivo in elegidas:
        lineas.append(_pieza(idx[id], motivo).rstrip("\\n") + "\\n")
    if descartadas:
        lineas.append(_bloque_descartadas(descartadas, idx))''',
'''def _armar(elegidas, descartadas, fijas, idx, raiz, tareas=()):
    """El texto tal como se inyecta. Lo usan `como_texto` y la medición."""
    lineas = [_ENCABEZADO]
    for id, motivo in elegidas:
        lineas.append(_pieza(idx[id], motivo).rstrip("\\n") + "\\n")
    if descartadas:
        lineas.append(_bloque_descartadas(descartadas, idx, tareas, raiz))''')

c('''def _cuerpo(regla):
    """Lo que se inyecta de una regla: encabezado, cuerpo y ejemplo, sin el sello."""
    partes = [regla.encabezado.strip()]
    partes += [t for _, t in regla.cuerpo]
    ejemplo = _ejemplo(regla)
    if ejemplo:
        partes.append("```\\n" + ejemplo + "\\n```")
    return "\\n".join(p for p in partes if p).strip()''',
'''def _cuerpo(regla):
    """Lo que se inyecta de una regla: encabezado, cuerpo y ejemplo, sin el sello."""
    return mapa_tareas.cuerpo(regla)''')

if crlf:
    s = s.replace("\n", "\r\n")
io.open(p, "w", encoding="utf-8", newline="").write(s)
print("ok")
