#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Utilidades compartidas por los validadores del estándar.

Principio: los validadores COMPRUEBAN, no arreglan. La norma vive en los `.md`;
aquí solo se verifica lo que se puede verificar sin criterio.

Dos severidades:
  FALLA — incumplimiento claro. Rompe la ejecución (código de salida 1).
  AVISO — algo que un humano debe mirar. No rompe nada.
"""
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FALLA = "FALLA"
AVISO = "AVISO"

# Carpetas que nunca se recorren.
EXCLUIDAS = {".git", "__pycache__", ".venv", "venv", "node_modules", "vendor"}

# Un marcador de plantilla: [texto] que NO es un enlace markdown ](...)
# ni una casilla de verificación - [ ] / - [x].
_MARCADOR = re.compile(r"\[([^\[\]\n]+)\](?!\()")
_ENCABEZADO = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
_CERCA = re.compile(r"^\s*(```|~~~)")
_ENLACE = re.compile(r"\[([^\]\n]*)\]\(([^)\s]+)")

# Un tramo `entre comillas invertidas`, con una o varias comillas de apertura,
# como en markdown. Lo de adentro es una muestra, no contenido del documento.
_CODIGO_EN_LINEA = re.compile(r"(`+)(?:(?!\1).)*?\1")


# `EP-004·HU-009` · La regla a la que pertenece un hallazgo.
#
# **Sale del mensaje, no de una lista.** Los 24 validadores ya citan su regla al
# explicar el incumplimiento —«(20·M5 · fila 10)», «S4/N6», «02·F24»—, así que
# agruparlos no exige tocarlos uno por uno: exige leer lo que ya escriben. Una
# lista aparte de qué validador comprueba qué regla sería una segunda verdad,
# y el día que difieran nadie sabría cuál manda.
_REGLA_EN_MENSAJE = re.compile(r"\b(?:(\d{2})·)?([A-Z]{1,4}\d+(?:\.\d+)?)\b")


class Hallazgo:
    """Un incumplimiento o aviso, anclado a archivo y línea."""

    def __init__(self, severidad, archivo, linea, mensaje, regla=None):
        self.severidad = severidad
        self.archivo = archivo
        self.linea = linea          # 0 = el archivo completo, sin línea concreta
        self.mensaje = mensaje
        self._regla = regla

    @property
    def regla(self):
        """`«NN·XN»` si se puede saber, o `""`. Nunca inventa.

        Si quien creó el hallazgo la declaró, esa manda. Si no, se busca en el
        mensaje: la primera cita con capítulo (`20·M5`) gana sobre la suelta
        (`M5`), porque el capítulo hace único al identificador.
        """
        if self._regla:
            return self._regla
        con_capitulo, suelta = "", ""
        for capitulo, id_ in _REGLA_EN_MENSAJE.findall(self.mensaje or ""):
            if capitulo and not con_capitulo:
                con_capitulo = f"{capitulo}·{id_}"
            elif not suelta:
                suelta = id_
        return con_capitulo or suelta

    def __str__(self):
        rel = relativo(self.archivo)
        donde = f"{rel}:{self.linea}" if self.linea else rel
        return f"[{self.severidad}] {donde} — {self.mensaje}"


def conteo_por_regla(hallazgos):
    """`{regla: cuántos}`, para saber por cuál se incumple más.

    **Lo que no se sabe se dice, no se reparte.** Los hallazgos cuyo mensaje no
    nombra ninguna regla se cuentan aparte, bajo `"(sin regla)"`: sumarlos a
    cualquier otra falsearía el número que se usa para decidir qué regla
    cambiar, y ese número es todo el punto de contarlos.
    """
    cuenta = {}
    for h in hallazgos:
        clave = h.regla or "(sin regla)"
        cuenta[clave] = cuenta.get(clave, 0) + 1
    return cuenta


def preparar_salida():
    """La consola de Windows no siempre es UTF-8; evita que un acento rompa todo."""
    for flujo in (sys.stdout, sys.stderr):
        try:
            flujo.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass


def relativo(ruta):
    """Ruta relativa al repositorio; absoluta si el archivo vive fuera de él."""
    try:
        rel = os.path.relpath(ruta, RAIZ).replace("\\", "/")
    except ValueError:      # otra unidad en Windows
        return ruta.replace("\\", "/")
    if rel.startswith(".."):
        return os.path.abspath(ruta).replace("\\", "/")
    return rel


# `EP-004·HU-003` · Los archivos que no se pudieron leer bien en esta corrida.
#
# **Por qué un registro y no una excepción.** Hasta el 2026-08-22 `leer` abría
# sin red: un `.md` mal codificado tumbaba la corrida entera con un volcado de
# Python, y se llevaba por delante **todos los hallazgos ya encontrados**. Y la
# salida contraria —leer reemplazando lo que no entiende y callar— es peor:
# convierte un archivo roto en uno que parece sano.
#
# Así que se hacen las dos cosas: la corrida **sigue**, y el archivo queda
# anotado acá para que el que reporta lo diga con su ruta.
ILEGIBLES = {}


def leer(ruta):
    """El texto del archivo. Nunca revienta: lo que falla queda anotado.

    - **No está o no se puede abrir** → devuelve `""` y lo anota.
    - **No es UTF-8** → devuelve lo que se pudo leer, con los caracteres malos
      reemplazados, y lo anota. Devolver vacío escondería el resto del archivo,
      que sí sirve.
    - **Se lee bien** → devuelve el texto, y si estaba anotado de antes se
      borra la anotación: el archivo se arregló.

    Quién lo cuenta: `ilegibles()`, que es lo que `validar.py` reporta.
    """
    try:
        with open(ruta, encoding="utf-8") as f:
            texto = f.read()
    except UnicodeDecodeError as e:
        ILEGIBLES[os.path.abspath(ruta)] = (
            "no es UTF-8 (byte %s en la posición %d) — se leyó reemplazando lo "
            "que no se entiende, así que lo que se diga de este archivo puede "
            "estar incompleto" % (
                getattr(e, "object", b"")[getattr(e, "start", 0):
                                          getattr(e, "start", 0) + 1] or b"?",
                getattr(e, "start", 0)))
        with open(ruta, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError as e:
        ILEGIBLES[os.path.abspath(ruta)] = "no se pudo abrir: %s" % (
            getattr(e, "strerror", None) or e)
        return ""
    ILEGIBLES.pop(os.path.abspath(ruta), None)
    return texto


def ilegibles():
    """`[Hallazgo]` por cada archivo que esta corrida no pudo leer bien.

    **Aviso, no falla.** Un archivo ilegible no dice que el proyecto incumpla
    nada: dice que de ese archivo no se puede opinar. Detener la corrida por él
    es justamente lo que esta función vino a evitar.
    """
    return [Hallazgo(AVISO, ruta, 0, motivo)
            for ruta, motivo in sorted(ILEGIBLES.items())]


def lineas_utiles(texto):
    """Devuelve (numero_de_linea, contenido) saltando los bloques de código.

    Sin esto, un ejemplo dentro de ``` se trataría como encabezado o marcador.
    """
    dentro = False
    for n, linea in enumerate(texto.splitlines(), start=1):
        if _CERCA.match(linea):
            dentro = not dentro
            continue
        if not dentro:
            yield n, linea


def encabezados(texto, desde_nivel=2):
    """Encabezados del documento, del nivel indicado hacia abajo.

    Se ignora el H1 a propósito: en un documento real lleva el ID y el título
    concretos, así que nunca coincide con el de la plantilla.
    """
    salida = []
    for n, linea in lineas_utiles(texto):
        m = _ENCABEZADO.match(linea)
        if m and len(m.group(1)) >= desde_nivel:
            salida.append((n, m.group(2).strip()))
    return salida


def marcadores(texto):
    """Marcadores [así] sin llenar. Excluye enlaces y casillas de verificación."""
    salida = []
    for n, linea in lineas_utiles(texto):
        for m in _MARCADOR.finditer(linea):
            contenido = m.group(1).strip()
            if contenido and contenido not in ("x", "X"):
                salida.append((n, m.group(0)))
    return salida


def sin_codigo_en_linea(linea):
    """La línea con los tramos `entre comillas invertidas` en blanco.

    `55` · Un plan de pruebas escribió, entre comillas, el texto que el caso
    tenía que encontrar: `` `[historico-chat/…](../../…)` ``. Eso no es un
    enlace, es una muestra — y el validador lo reportó roto dos veces. Las dos
    salidas eran malas: redactar torcido para callarlo, o aprender a ignorarlo.

    Se reemplaza por espacios en vez de borrarse, para no correr las columnas:
    el número de línea y la posición siguen valiendo.
    """
    return _CODIGO_EN_LINEA.sub(lambda m: " " * len(m.group(0)), linea)


def enlaces(texto):
    """Enlaces markdown del documento: (numero_de_linea, texto, destino).

    No mira dentro de los bloques cercados (`lineas_utiles`) ni de las comillas
    invertidas: ahí lo que hay son ejemplos de cómo se escribe un enlace, no
    enlaces a ninguna parte.
    """
    salida = []
    for n, linea in lineas_utiles(texto):
        for m in _ENLACE.finditer(sin_codigo_en_linea(linea)):
            salida.append((n, m.group(1), m.group(2)))
    return salida


def _celdas(linea):
    """Las celdas de una fila markdown, sin los bordes ni los espacios."""
    return [c.strip() for c in linea.strip().strip("|").split("|")]


def _es_separador(celdas):
    return bool(celdas) and all(re.fullmatch(r":?-{2,}:?", c) for c in celdas)


def tablas(texto):
    """Las tablas markdown del documento.

    Devuelve `[(encabezados, filas)]`, donde `filas` es `[(numero_de_linea,
    celdas)]`. Se salta los bloques de código, así que una tabla de ejemplo
    dentro de ``` no cuenta como tabla del documento.

    Una tabla es un bloque de renglones que empiezan por `|` cuya segunda línea
    es la de guiones. Sin esa línea, markdown no la dibuja como tabla y aquí
    tampoco cuenta.
    """
    salida = []
    bloque = []

    def cerrar():
        if len(bloque) >= 2 and _es_separador(_celdas(bloque[1][1])):
            encabezados = _celdas(bloque[0][1])
            filas = [(n, _celdas(l)) for n, l in bloque[2:]]
            salida.append((encabezados, filas))
        bloque.clear()

    for n, linea in lineas_utiles(texto):
        if linea.strip().startswith("|"):
            bloque.append((n, linea))
        else:
            cerrar()
    cerrar()
    return salida


def filas_de(texto, *columnas):
    """Las filas de la primera tabla que tenga todas esas columnas.

    Devuelve `[(numero_de_linea, {columna: valor})]`. Busca por nombre de
    columna y no por posición: así una tabla que gane una columna al final no
    rompe a quien la lee.
    """
    objetivo = [c.lower() for c in columnas]
    for encabezados, filas in tablas(texto):
        bajos = [e.lower() for e in encabezados]
        if not all(c in bajos for c in objetivo):
            continue
        salida = []
        for n, celdas in filas:
            fila = {e: (celdas[i] if i < len(celdas) else "")
                    for i, e in enumerate(bajos)}
            salida.append((n, fila))
        return salida
    return []


def valor_limpio(celda):
    """El contenido de una celda, sin comillas invertidas ni marcador de plantilla.

    Una celda que sigue trayendo el `«…»` de la plantilla es una celda **sin
    llenar**: vale lo mismo que vacía, y devolver el marcador haría que el
    validador comparara contra un texto que nadie escribió.
    """
    v = celda.strip().strip("`").strip()
    if not v or v in ("—", "-", "–") or ("«" in v and "»" in v):
        return ""
    return v


def recorrer_md(raiz):
    """Todos los .md bajo `raiz`, saltando las carpetas excluidas."""
    for carpeta, subcarpetas, archivos in os.walk(raiz):
        subcarpetas[:] = [s for s in subcarpetas if s not in EXCLUIDAS]
        for nombre in sorted(archivos):
            if nombre.lower().endswith(".md"):
                yield os.path.join(carpeta, nombre)


# `EP-004·HU-009` · Todo lo reportado en esta corrida, para poder contarlo por
# regla al terminar. Se acumula acá y no en cada validador porque **todos pasan
# por `reportar`**: pedirle a los veinticuatro que además devuelvan sus
# hallazgos sería tocar veinticuatro archivos para saber algo que ya pasa por
# un solo punto.
CORRIDA = []


def reportar(hallazgos, titulo=None):
    """Imprime los hallazgos y devuelve el código de salida (1 si hay FALLA).

    **Agrega lo que la corrida no pudo leer** (`EP-004·HU-003`). Un archivo
    ilegible ya no tumba nada, pero callarlo sería peor que reventar: quien
    lee el reporte creería que se miró todo. Se dice, y como aviso.
    """
    hallazgos = list(hallazgos) + [h for h in ilegibles()
                                   if h not in hallazgos]
    CORRIDA.extend(hallazgos)
    fallas = [h for h in hallazgos if h.severidad == FALLA]
    avisos = [h for h in hallazgos if h.severidad == AVISO]

    if titulo:
        print(f"== {titulo} ==")

    for h in fallas:
        print(str(h))
    for h in avisos:
        print(str(h))

    if not hallazgos:
        print("OK: sin incumplimientos.")
        return 0

    print(f"\n{len(fallas)} falla(s), {len(avisos)} aviso(s).")
    return 1 if fallas else 0


def no_es_punto_de_entrada(subcomando=None):
    """Muere diciendo por dónde se corre. Nunca devuelve.

    Un módulo de comprobación **importado** por `validar.py` no hace nada al
    ejecutarse solo: cae hasta el final del archivo y sale con código 0. Y un
    código 0 sin salida se lee igual que «no encontré nada» — que es la peor
    mentira que puede decir un validador, porque afirma sin haber mirado.

    Ya costó una métrica falsa: la fase `B-EP-005-HU-008` escribió «cero
    enlaces rotos» el 2026-08-16 porque corrió `enlaces.py` a mano y no
    imprimió nada. El entrypoint real reportaba veinte.

    Sale con código 2 —ni 0 ni 1— para que un guion que lo llame por error
    pueda distinguir «no comprobé nada» de «comprobé y hay fallas».
    """
    modulo = os.path.basename(sys.argv[0]) or "este módulo"
    linea = (f"python validadores/validar.py {subcomando}" if subcomando
             else "python validadores/validar.py --help")
    preparar_salida()
    print(f"{modulo} no se corre solo: es una pieza de `validar.py`, "
          f"y correrlo así **no comprueba nada**.", file=sys.stderr)
    print(f"\nSe corre con:\n  {linea}", file=sys.stderr)
    sys.exit(2)
