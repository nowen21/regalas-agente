# -*- coding: utf-8 -*-
"""`EP-023 · HU-001 · fase B` · La conversación pasa sola al análisis prendido.

**Qué resuelve.** Hasta la versión 40.0.0, lo que pasaba la conversación al
análisis era un guion de sesión que se prendía y se apagaba a mano en cada
análisis (H-2 del 2026-09-30). Acá vive el trabajo que no depende de la
herramienta; el enganche que lo llama está en `adaptadores/claude-code/`.

**Los tres controles** (análisis 2 del pendiente 103, conclusión 2):

- **Prender**, con «Analicemos: el pendiente N». «Analicemos» sin pendiente no
  prende nada: sigue siendo analizar en el chat.
- **Pausar**, con «Pare». Los turnos en pausa no entran; queda una línea que
  dice cuáles fueron (conclusión 4).
- **Apagar**, con «Apruebo el análisis». La herramienta pone la marca con la
  fecha y el turno, y borra el estado cuando la respuesta a ese turno ya entró.

**Un solo análisis abierto** (conclusión 6). Está abierto el que no tiene la
marca «Aprobado», y también el aprobado cuyo plan no se ha cumplido: alguna HU
de su columna «Pasó a» no está terminada (análisis 3, punto 4).

**Lo que no hace, y se declara.** No copia el hallazgo ni el pendiente en el
análisis nuevo: qué hallazgo lo origina lo sabe la conversación. No corrige las
palabras copiadas: la conversación no se edita (análisis 1, conclusión 21).
"""
import glob
import os
import re
import time
import unicodedata

import comun
from comun import leer

ESTADO = os.path.join("historico-chat", ".estado", "analisis-en-curso.txt")
PLANTILLA = os.path.join("plantillas", "analisis.md")
FIN = "> acá termina la conversación"
APORTA = "Lo que aporta al análisis principal"
LISTA = "## Lista de análisis"

_ANALISIS = re.compile(r"^analisis-(\d+)\.md$")
_APROBADO = re.compile(r"^> \*\*Aprobado\*\*", re.M)
_TURNO_APROBADO = re.compile(r"^> \*\*Aprobado\*\* .*?en el turno (\d+)", re.M)
_TURNO = re.compile(r"^### (\d+) · Usuario", re.M)
_PENDIENTE = re.compile(r"\bpendiente\s+(\d+)\b")
_HU = re.compile(r"\bHU[- ]0*(\d+)\b")
_EPICA = re.compile(r"\bEP-0*(\d+)\b")
_RESULTADO = re.compile(r"^\*\*Resultado:\*\* *(\S.*?)\s*$", re.M)
_SUMA = re.compile(r"^\*\*Lo que suma al análisis principal:\*\* *(\S.*?)\s*$", re.M)
_FILA = re.compile(r"^\| *\d+ *\|", re.M)

# Lo que no es del repositorio: local, generado o de terceros.
FUERA = {".git", ".venv", "venv", "__pycache__", "node_modules", "terceros"}


def _limpio(texto):
    """Minúsculas y sin tildes, que es como se comparan las palabras."""
    sin = unicodedata.normalize("NFD", texto or "")
    sin = "".join(c for c in sin if unicodedata.category(c) != "Mn")
    return sin.lower().strip()


def _escribir(ruta, texto):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(texto)


# ── El estado ────────────────────────────────────────────────────────────────

def leer_estado(raiz):
    """`{analisis, transcripcion, desde, pausa, pausas}` con rutas absolutas, o None."""
    ruta = os.path.join(raiz, ESTADO)
    if not os.path.isfile(ruta):
        return None
    datos = {}
    for linea in leer(ruta).splitlines():
        if "=" in linea:
            clave, valor = linea.split("=", 1)
            datos[clave.strip()] = valor.strip()
    if not {"analisis", "transcripcion", "desde"} <= datos.keys():
        return None
    pausas = []
    for tramo in filter(None, datos.get("pausas", "").split(",")):
        a, b = tramo.split("-")
        pausas.append((int(a), int(b)))
    return {
        "analisis": os.path.normpath(os.path.join(raiz, datos["analisis"])),
        "transcripcion": os.path.normpath(os.path.join(raiz, datos["transcripcion"])),
        "desde": int(datos["desde"]),
        "pausa": int(datos["pausa"]) if datos.get("pausa") else None,
        "pausas": pausas,
    }


def _guardar_estado(raiz, estado):
    lineas = [
        "analisis=" + os.path.relpath(estado["analisis"], raiz).replace(os.sep, "/"),
        "transcripcion=" + os.path.relpath(estado["transcripcion"], raiz).replace(os.sep, "/"),
        "desde=%d" % estado["desde"],
    ]
    if estado.get("pausa"):
        lineas.append("pausa=%d" % estado["pausa"])
    if estado.get("pausas"):
        lineas.append("pausas=" + ",".join("%d-%d" % p for p in estado["pausas"]))
    _escribir(os.path.join(raiz, ESTADO), "\n".join(lineas) + "\n")


def _borrar_estado(raiz):
    ruta = os.path.join(raiz, ESTADO)
    if os.path.isfile(ruta):
        os.remove(ruta)


def ultimo_turno(transcripcion):
    """El número del último turno del usuario en la transcripción, o 0."""
    numeros = [int(n) for n in _TURNO.findall(leer(transcripcion))] if transcripcion and os.path.isfile(transcripcion) else []
    return max(numeros) if numeros else 0


# ── Pendientes y análisis ────────────────────────────────────────────────────

def _carpetas_con_pendiente(raiz):
    for carpeta, subcarpetas, archivos in os.walk(raiz):
        subcarpetas[:] = [s for s in subcarpetas if s not in FUERA]
        if "pendiente.md" in archivos:
            yield carpeta


def carpeta_del_pendiente(raiz, numero):
    """La carpeta `N-<slug>/` que tiene el `pendiente.md` del pendiente N, o ""."""
    for carpeta in _carpetas_con_pendiente(raiz):
        if os.path.basename(carpeta).split("-", 1)[0] == str(numero):
            return carpeta
    return ""


def _analisis_de(carpeta):
    """Los `analisis-N.md` de la carpeta, ordenados por N."""
    salida = []
    for nombre in os.listdir(carpeta):
        m = _ANALISIS.match(nombre)
        if m:
            salida.append((int(m.group(1)), os.path.join(carpeta, nombre)))
    return [ruta for _, ruta in sorted(salida)]


def aprobado(ruta):
    return bool(_APROBADO.search(leer(ruta)))


def turno_aprobado(ruta):
    """El turno en que se aprobó el análisis, o `None`."""
    m = _TURNO_APROBADO.search(leer(ruta)) if os.path.isfile(ruta) else None
    return int(m.group(1)) if m else None


def _hu_terminada(raiz, epica, hu):
    patron = os.path.join(raiz, "documentacion", "epicas")
    if not os.path.isdir(patron):
        return False
    for e in os.listdir(patron):
        if not re.match(r"EP-0*%d-" % epica, e):
            continue
        for h in os.listdir(os.path.join(patron, e)):
            if re.match(r"HU-0*%d-" % hu, h):
                archivo = os.path.join(patron, e, h, h + ".md")
                if os.path.isfile(archivo):
                    return bool(re.search(r"^\| \*\*Estado\*\* \|\s*Terminada", leer(archivo), re.M))
    return False


def _plan_pendiente(raiz, ruta):
    """Las HU de la columna «Pasó a» del análisis que todavía no terminan."""
    texto = leer(ruta)
    if "## Lo que se tiene que hacer" not in texto:
        return []
    tabla = texto.split("## Lo que se tiene que hacer", 1)[1]
    faltan = []
    for linea in tabla.splitlines():
        if not linea.startswith("|"):
            continue
        celda = linea.rstrip("|").split("|")[-1]
        ep = _EPICA.search(celda)
        for hu in _HU.findall(celda):
            if ep and not _hu_terminada(raiz, int(ep.group(1)), int(hu)):
                faltan.append("EP-%03d HU-%03d" % (int(ep.group(1)), int(hu)))
    return sorted(set(faltan))


def abiertos(raiz):
    """`[(ruta del análisis, por qué sigue abierto)]` de todo el repositorio."""
    salida = []
    for carpeta in _carpetas_con_pendiente(raiz):
        rutas = _analisis_de(carpeta)
        if not rutas:
            continue
        ultimo = rutas[-1]
        if not aprobado(ultimo):
            salida.append((ultimo, "no está aprobado"))
            continue
        faltan = _plan_pendiente(raiz, ultimo)
        if faltan:
            salida.append((ultimo, "su plan no se ha cumplido: falta " + ", ".join(faltan)))
    return salida


def _nuevo_analisis(raiz, carpeta):
    """El análisis que se prende: el último si sigue sin aprobar, o el siguiente."""
    rutas = _analisis_de(carpeta)
    if rutas and not aprobado(rutas[-1]):
        return rutas[-1]
    numero = len(rutas) + 1
    ruta = os.path.join(carpeta, "analisis-%d.md" % numero)
    plantilla = os.path.join(comun.RAIZ, PLANTILLA)
    texto = leer(plantilla) if os.path.isfile(plantilla) else (
        "# Análisis «N»\n\n## Conversación\n\n> La escribe el enganche.\n\n" + FIN + "\n")
    _escribir(ruta, texto.replace("# Análisis «N»", "# Análisis %d" % numero, 1))
    return ruta


# ── Los tres controles ───────────────────────────────────────────────────────

def pendiente_pedido(mensaje):
    """El N de «Analicemos: el pendiente N», o None si el mensaje no lo pide."""
    limpio = _limpio(mensaje)
    if not limpio.startswith("analicemos"):
        return None
    primera = limpio.split("\n", 1)[0]
    m = _PENDIENTE.search(primera)
    return int(m.group(1)) if m else None


def prender(raiz, numero, transcripcion, turno):
    """Prende el análisis del pendiente. Devuelve `(prendido, mensaje)`."""
    carpeta = carpeta_del_pendiente(raiz, numero)
    if not carpeta:
        return False, "no hay una carpeta con el pendiente %d" % numero
    otros = [(r, m) for r, m in abiertos(raiz)
             if os.path.normpath(os.path.dirname(r)) != os.path.normpath(carpeta)]
    if otros:
        ruta, motivo = otros[0]
        return False, ("no se prende: el análisis %s sigue abierto (%s)"
                       % (os.path.relpath(ruta, raiz).replace(os.sep, "/"), motivo))
    estado = leer_estado(raiz)
    if estado and os.path.dirname(estado["analisis"]) == os.path.normpath(carpeta) and not aprobado(estado["analisis"]):
        if estado.get("pausa"):
            estado["pausas"].append((estado["pausa"], turno - 1))
            estado["pausa"] = None
            _guardar_estado(raiz, estado)
        return True, "sigue prendido"
    analisis = _nuevo_analisis(raiz, carpeta)
    _guardar_estado(raiz, {"analisis": analisis, "transcripcion": transcripcion,
                           "desde": turno, "pausa": None, "pausas": []})
    return True, "prendido desde el turno %d" % turno


def pausar(raiz, turno):
    estado = leer_estado(raiz)
    if not estado or estado.get("pausa"):
        return False
    estado["pausa"] = turno
    _guardar_estado(raiz, estado)
    return True


def seccion(texto, titulo):
    """El texto de la sección `## <titulo>` hasta la siguiente `## `."""
    m = re.search(r"^## %s.*$" % re.escape(titulo), texto, re.M)
    if not m:
        return ""
    fin = re.search(r"^## ", texto[m.end():], re.M)
    return texto[m.end():m.end() + fin.start()] if fin else texto[m.end():]


def aporte(texto):
    """`(resultado, lo que suma)` de «Lo que aporta al análisis principal», o `None`."""
    parte = seccion(texto, APORTA)
    resultado, suma = _RESULTADO.search(parte), _SUMA.search(parte)
    if not (resultado and suma):
        return None
    return resultado.group(1).strip(), suma.group(1).strip()


def faltantes(texto):
    """Lo que le falta a un análisis para poder aprobarse (análisis 9, CA-25 y CA-26)."""
    salida = []
    if not _FILA.search(seccion(texto, "Lo que se tiene que hacer")):
        salida.append("falta al menos una fila en «Lo que se tiene que hacer»")
    if aporte(texto) is None:
        salida.append("falta «%s», con el resultado y lo que suma" % APORTA)
    return salida


_HALLAZGO_TITULO = re.compile(r"^### (H-\d+)\b", re.M)
_DE_DONDE_SALE = re.compile(r"^\|[^|\n]*De dónde sale[^|\n]*\|(.*)\|\s*$", re.M)


def hallazgo_en_el_pendiente(ruta):
    """`EP-023 · HU-003 · CA-09` · El hallazgo del análisis tiene que estar en su pendiente.

    Cada análisis aprobado deja el pendiente en su versión siguiente, con su
    hallazgo en «De dónde sale» (análisis 11 del pendiente 103, acuerdo 5). El
    análisis 1 no se revisa: es el que origina el pendiente.
    """
    m = _ANALISIS.match(os.path.basename(ruta))
    if not m or int(m.group(1)) == 1:
        return []
    h = _HALLAZGO_TITULO.search(seccion(leer(ruta), "Hallazgo"))
    if not h:
        return ["falta el número del hallazgo (H-N) en el título de «Hallazgo»"]
    pendiente = os.path.join(os.path.dirname(ruta), "pendiente.md")
    fila = _DE_DONDE_SALE.search(leer(pendiente)) if os.path.isfile(pendiente) else None
    if not fila or not re.search(r"\b%s\b" % re.escape(h.group(1)), fila.group(1)):
        return ["falta el %s en «De dónde sale» del pendiente: pasarlo a su versión siguiente antes de aprobar"
                % h.group(1)]
    return []


def por_que_no_se_aprueba(raiz):
    """Lo que le falta al análisis prendido para aprobarse; vacío si nada.

    Además de `faltantes()`, corre la revisión de origen: el punto que no dice de
    dónde sale, o que cita algo que no existe, se corrige antes de aprobar
    (análisis 14 del pendiente 103, acuerdo 4).
    """
    estado = leer_estado(raiz)
    if not estado or not os.path.isfile(estado["analisis"]):
        return []
    import origen
    return (faltantes(leer(estado["analisis"])) + hallazgo_en_el_pendiente(estado["analisis"])
            + origen.revisar_uno(estado["analisis"]))


def version():
    """La versión del estándar que corre, la que queda en la marca de aprobado."""
    ruta = os.path.join(comun.RAIZ, "VERSION")
    return leer(ruta).strip() if os.path.isfile(ruta) else ""


def principal_de(raiz, ruta):
    """El análisis principal del alcance de `ruta`: el primero que aparece subiendo de carpeta.

    Un módulo con su propio `analisis/<nombre>-analisis-principal.md` lo usa; si no lo
    tiene, se llega al del proyecto (análisis 9, punto 5 de «Lo acordado»).
    """
    raiz = os.path.abspath(raiz)
    carpeta = os.path.dirname(os.path.abspath(ruta))
    while True:
        hallados = sorted(glob.glob(os.path.join(carpeta, "analisis", "*analisis-principal*.md")))
        if hallados:
            return hallados[0]
        if os.path.normcase(carpeta) == os.path.normcase(raiz) or os.path.dirname(carpeta) == carpeta:
            return None
        carpeta = os.path.dirname(carpeta)


def nombre_del_analisis(ruta):
    """El texto del enlace en la «Lista de análisis»."""
    m = _ANALISIS.match(os.path.basename(ruta))
    if m:
        p = re.match(r"^(\d+)-", os.path.basename(os.path.dirname(ruta)))
        return "Análisis %s del pendiente %s" % (m.group(1), p.group(1)) if p else "Análisis %s" % m.group(1)
    return leer(ruta).split("\n", 1)[0].lstrip("# ").strip()


def anotar_en_principal(raiz, ruta, fecha):
    """Pasa tal cual lo que suma el análisis al principal de su alcance (CA-24).

    Lo que suma va al final de la redacción y la fila al final de la «Lista de
    análisis». Devuelve la ruta del principal, o `None` si no hay dónde anotarlo.
    """
    datos = aporte(leer(ruta))
    principal = principal_de(raiz, ruta)
    if not datos or not principal:
        return None
    texto = leer(principal)
    i = texto.find(LISTA)
    if i < 0:
        return None
    resultado, suma = datos
    enlace = os.path.relpath(ruta, os.path.dirname(principal)).replace(os.sep, "/")
    fila = "| %s | %s | [%s](%s) |\n" % (fecha, resultado.rstrip("."), nombre_del_analisis(ruta), enlace)
    _escribir(principal, texto[:i].rstrip("\n") + " " + suma + "\n\n" + texto[i:].rstrip("\n") + "\n" + fila)
    return principal


def aprobar(raiz, turno, fecha):
    """Pone la marca «Aprobado» con la fecha, el turno y la versión, una sola vez.

    No la pone si `por_que_no_se_aprueba()` encuentra algo. Puesta la marca,
    pasa lo que el análisis suma al análisis principal.
    """
    estado = leer_estado(raiz)
    if not estado or not os.path.isfile(estado["analisis"]):
        return False
    texto = leer(estado["analisis"])
    if _APROBADO.search(texto) or por_que_no_se_aprueba(raiz):
        return False
    con = ", con la versión %s" % version() if version() else ""
    marca = ("> **Aprobado** por el usuario el %s, en el turno %d%s. Desde ese momento "
             "este análisis no se reescribe.\n" % (fecha, turno, con))
    primera, _, resto = texto.partition("\n")
    _escribir(estado["analisis"], primera + "\n\n" + marca + resto)
    anotar_en_principal(raiz, estado["analisis"], fecha)
    return True


# ── Pasar la conversación ────────────────────────────────────────────────────

def _bloques(texto):
    """`[(turno, bloque)]` de la transcripción, desde cada `### N · Usuario`."""
    marcas = list(_TURNO.finditer(texto))
    salida = []
    for i, m in enumerate(marcas):
        fin = marcas[i + 1].start() if i + 1 < len(marcas) else len(texto)
        salida.append((int(m.group(1)), texto[m.start():fin].rstrip() + "\n"))
    return salida


def _limpiar(bloque):
    # La transcripción separa el turno de su hora con raya larga; el análisis
    # sigue `00·ID8`, así que ahí va una coma (análisis 2, conclusión 5).
    bloque = re.sub(r"^(### \d+ · Usuario|\*\*Agente\*\*) — ", r"\1, ", bloque, flags=re.M)
    # Por lo mismo, los puntos suspensivos de un solo carácter pasan a tres
    # puntos: el commit los rechaza (análisis 14 del pendiente 103, acuerdo 6).
    bloque = bloque.replace("…", "...")
    # Las marcas que la herramienta le pone al mensaje no son palabras del
    # usuario (conclusión 10).
    bloque = re.sub(r"</?pasted_content[^>]*>", "", bloque)
    bloque = re.sub(r"<ide_(?:opened_file|selection)>.*?</ide_(?:opened_file|selection)>", "", bloque, flags=re.S)
    bloque = re.sub(r"^> *\n(?=> *\n)", "", bloque, flags=re.M)
    return bloque


def conversacion(estado, raiz):
    """El texto que va en la sección «Conversación», con las pausas marcadas."""
    texto = leer(estado["transcripcion"]) if os.path.isfile(estado["transcripcion"]) else ""
    tramos = list(estado.get("pausas") or [])
    if estado.get("pausa"):
        tramos.append((estado["pausa"], 10 ** 9))
    partes, anunciados = [], set()
    # Lo que llega después del turno que lo aprobó no entra (`13·DOC24`).
    tope = turno_aprobado(estado["analisis"])
    for turno, bloque in _bloques(texto):
        if turno < estado["desde"] or (tope is not None and turno > tope):
            continue
        tramo = next((t for t in tramos if t[0] <= turno <= t[1]), None)
        if tramo:
            if tramo not in anunciados:
                anunciados.add(tramo)
                if tramo[1] >= 10 ** 9:
                    partes.append("> En pausa desde el turno %d.\n" % tramo[0])
                elif tramo[0] == tramo[1]:
                    partes.append("> Turno %d en pausa.\n" % tramo[0])
                else:
                    partes.append("> Turnos %d a %d en pausa.\n" % tramo)
            continue
        partes.append(_limpiar(bloque))
    cuerpo = "\n".join(partes)
    carpeta = os.path.dirname(estado["analisis"])
    subir = "../" * len(os.path.relpath(carpeta, raiz).split(os.sep))

    def ajustar(m):
        ruta = m.group(1)
        if not os.path.exists(os.path.join(raiz, ruta.split("#")[0])) and \
                os.path.exists(os.path.join(carpeta, ruta.split("#")[0])):
            return m.group(0)
        return "](" + subir + ruta + ")"

    cuerpo = re.sub(r"\]\((?!https?:|#|\.\./)([^)]+)\)", ajustar, cuerpo)

    # Un enlace cuyo destino ya no existe (se movió después de la respuesta)
    # pasa como texto: lo dicho se conserva y el análisis no queda con un
    # enlace roto.
    def vigente(m):
        destino = m.group(2).split("#")[0]
        if re.match(r"https?:", destino) or os.path.exists(os.path.normpath(os.path.join(carpeta, destino))):
            return m.group(0)
        return "%s (`%s`, ya no está ahí)" % (m.group(1), destino.replace("../", "").lstrip("./"))

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", vigente, cuerpo)


def pasar(raiz):
    """Copia la conversación al análisis prendido; apaga si ya se aprobó."""
    estado = leer_estado(raiz)
    if not estado or not os.path.isfile(estado["analisis"]):
        return False
    texto = leer(estado["analisis"])
    if "## Conversación" not in texto or FIN not in texto:
        return False
    inicio = texto.index("## Conversación")
    nota = texto.find("\n> ", inicio)
    inicio = texto.index("\n\n", nota + 1) + 2 if nota != -1 else inicio + len("## Conversación\n\n")
    fin = texto.rindex(FIN)
    nuevo = texto[:inicio] + conversacion(estado, raiz) + "\n" + texto[fin:]
    if nuevo != texto:
        _escribir(estado["analisis"], nuevo)
    # Se apaga cuando la respuesta al turno que lo aprobó ya entró. Al cerrar
    # ese turno puede no estar todavía, porque el histórico la escribe en el
    # mismo evento; por eso también se apaga apenas llega el turno siguiente.
    tope = turno_aprobado(estado["analisis"])
    if tope is not None:
        transcripcion = leer(estado["transcripcion"]) if os.path.isfile(estado["transcripcion"]) else ""
        bloques = dict(_bloques(transcripcion))
        siguiente = any(n > tope for n in bloques)
        respondido = "\n**Agente**" in bloques.get(tope, "")
        if siguiente or respondido:
            _borrar_estado(raiz)
    return True


# ── El aviso ─────────────────────────────────────────────────────────────────

def aviso(raiz, nota=""):
    """La línea que el agente recibe en cada mensaje."""
    estado = leer_estado(raiz)
    if not estado:
        linea = "Ningún análisis está prendido: la conversación no entra a ninguno."
    else:
        rel = os.path.relpath(estado["analisis"], raiz).replace(os.sep, "/")
        if estado.get("pausa"):
            linea = "El análisis %s está en pausa desde el turno %d." % (rel, estado["pausa"])
        else:
            linea = "La conversación entra al análisis %s." % rel
    return "[ANÁLISIS EN CURSO] " + linea + (" " + nota[0].upper() + nota[1:] + "." if nota else "")


def esperar(transcripcion, segundos=5.0):
    """Espera a que el histórico anote el turno; los dos corren en el mismo evento."""
    if not transcripcion or not os.path.isfile(transcripcion):
        return
    antes = os.path.getmtime(transcripcion)
    limite = time.time() + segundos
    while time.time() < limite:
        time.sleep(0.25)
        if os.path.getmtime(transcripcion) != antes:
            time.sleep(0.5)
            return


if __name__ == "__main__":
    comun.no_es_punto_de_entrada(la_corre="adaptadores/claude-code/hook_analisis.py")
