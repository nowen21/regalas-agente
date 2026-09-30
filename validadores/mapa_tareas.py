# -*- coding: utf-8 -*-
"""`EP-005·HU-023` · Arma el mapa de qué reglas aplican a cada tarea.

**Por qué existe.** El usuario decidió que el agente no cargue todas las reglas
al arrancar, sino que antes de cada tarea lea las que le aplican. Los índices de
`base/` van por capítulo, y para encontrar una regla había que saber de antemano
dónde estaba. Este programa junta las reglas por tarea.

**Lo escribe un programa y no una persona.** Cada regla dice a qué tareas aplica
con su línea `**Aplica a:**`, y el mapa sale de leerlas. Un mapa escrito a mano
envejece: el del amarre dejó de listar `recuperar.py` el día que entró, y nadie
lo notó hasta que fallaron sus pruebas.

**Las tareas son una lista cerrada**, en `base/tareas.md`. Una tarea que la
regla nombra y la lista no trae no entra al mapa: la reporta `sin_lista()`.

**Y escribe, por tarea, las reglas completas** (fase `C`, RN-08). El agente las
lee antes de actuar con la herramienta de lectura, porque el texto de un
enganche se corta en 10.000 caracteres y las reglas de una tarea suman hasta
218.000. Viven en `base/reglas-por-tarea/`, y los recorridos de los
validadores saltan esa carpeta (`comun.EXCLUIDAS`): son copias, y los
contarían como reglas repetidas.
"""
import io
import os
import re

import citas
import comun
import metareglas
from comun import FALLA, Hallazgo, RAIZ, leer

TAREAS = "base/tareas.md"
MAPA = "base/mapa-de-tareas.md"
POR_TAREA = "base/reglas-por-tarea"

# Cuántos caracteres lleva cada archivo por tarea como máximo. El agente los lee
# con un comando, porque la herramienta de lectura no vuelve a mandar un archivo
# que no cambió, y la salida de un comando se corta pasados 30.000 caracteres;
# con este tamaño cada parte llega entera.
PARTE = 25000

# Una fila de la tabla de `base/tareas.md`: `| \`recibir-pedido\` | … |`.
_TAREA = re.compile(r"^\|\s*`([a-z][a-z-]*)`\s*\|")
_APLICA = re.compile(r"(?m)^\*\*Aplica a:\*\*\s*(.+?)\s*$")
# La marca del encabezado no es parte del nombre de la regla.
_MARCA = re.compile(r"\s*(`\[[^\]]+\]`|\*opt-in\*)\s*$")
# Un enlace de markdown: `[texto](destino)`.
_ENLACE = re.compile(r"(\[[^\]\n]*\]\()([^)\s]+)(\))")


def _filas(raiz=None):
    """`[(tarea, [celdas])]` de la tabla de `base/tareas.md`."""
    ruta = os.path.join(raiz or RAIZ, *TAREAS.split("/"))
    salida = []
    for linea in leer(ruta).splitlines():
        m = _TAREA.match(linea.strip())
        if m:
            celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
            # La tabla de tareas tiene cuatro columnas; la de las acciones, dos.
            if len(celdas) >= 4:
                salida.append((m.group(1), celdas))
    return salida


def tareas(raiz=None):
    """Los nombres de la lista cerrada, en el orden en que la lista los trae."""
    return [t for t, _ in _filas(raiz)]


def palabras_clave(raiz=None):
    """`{tarea: {palabras clave}}` de la tercera columna (`01·C28`).

    La tarea que dice `siempre` va con el conjunto vacío y figura en
    `siempre()`: no la pide ninguna palabra porque va en todo mensaje.
    """
    salida = {}
    for tarea, celdas in _filas(raiz):
        texto = celdas[2] if len(celdas) > 2 else ""
        salida[tarea] = {p.strip().lower() for p in texto.split(",")
                         if p.strip() and p.strip().lower() != "siempre"}
    return salida


def siempre(raiz=None):
    """Las tareas que van en todo mensaje: su tercera columna dice `siempre`."""
    return [t for t, celdas in _filas(raiz)
            if len(celdas) > 2 and celdas[2].strip().lower() == "siempre"]


def acciones(raiz=None):
    """`{tarea: [(clase, [valores])]}` de la cuarta columna.

    `escribe en base/ plantillas/` da `("escribe en", ["base/", "plantillas/"])`;
    `comando git` da `("comando", ["git"])`; `comando` solo, `("comando", [])`.
    """
    salida = {}
    for tarea, celdas in _filas(raiz):
        texto = celdas[3] if len(celdas) > 3 else ""
        specs = []
        for crudo in texto.split(";"):
            partes = crudo.strip().strip("`").split()
            if not partes:
                continue
            if partes[:2] == ["escribe", "en"]:
                specs.append(("escribe en", partes[2:]))
            elif partes[0] == "escribe":
                specs.append(("escribe", partes[1:]))
            else:
                specs.append((partes[0], partes[1:]))
        salida[tarea] = specs
    return salida


def reglas_por_tarea(raiz=None):
    """`{tarea: [regla]}` de las reglas vigentes, en el orden de `base/`."""
    raiz = raiz or RAIZ
    salida = {t: [] for t in tareas(raiz)}
    for regla in metareglas.reglas(raiz):
        if regla.derogada:
            continue
        for t in declaradas(regla):
            if t in salida:
                salida[t].append(regla)
    return salida


def declaradas(regla):
    """Las tareas que la regla nombra en su línea `**Aplica a:**`."""
    m = _APLICA.search(regla.texto)
    if not m:
        return []
    return [t.strip().strip("`") for t in m.group(1).split(",") if t.strip()]


def _enlace(regla, desde):
    """La ruta a la regla, relativa a `desde`, con su ancla."""
    ruta = os.path.relpath(regla.archivo, desde).replace(os.sep, "/")
    if regla.nivel == 1:
        return ruta                     # la regla ocupa su archivo entero
    return ruta + "#" + citas.ancla(f"{regla.id} · {regla.titulo}")


def _nombre(regla):
    """El título sin la marca y sin raya ni punto medio, que en una lista son prosa."""
    nombre = _MARCA.sub("", regla.titulo)
    nombre = re.sub(r"\s*[—·]\s*$", "", nombre)   # la que precedía a la marca
    return re.sub(r"\s+[—·]\s+", ", ", nombre)


def armar(raiz=None):
    """El texto del mapa: cada tarea de la lista con las reglas que la declaran."""
    raiz = raiz or RAIZ
    lista = tareas(raiz)
    por_tarea = reglas_por_tarea(raiz)
    desde = os.path.dirname(os.path.join(raiz, *MAPA.split("/")))
    partes = [
        "# Mapa de tareas",
        "",
        "Qué reglas se leen antes de cada tarea. Lo escribe "
        "`validadores/mapa_tareas.py` leyendo la línea `**Aplica a:**` de cada "
        "regla: no se edita a mano. Para cambiarlo se cambia la regla y se vuelve "
        "a correr el programa.",
        "",
        "Las tareas son las de [base/tareas.md](tareas.md). El texto completo de "
        "las reglas de cada una está en "
        "[base/reglas-por-tarea/](reglas-por-tarea/README.md).",
    ]
    for t in lista:
        partes += ["", f"## `{t}`", ""]
        if not por_tarea[t]:
            partes.append("Ninguna regla la declara todavía.")
            continue
        for regla in por_tarea[t]:
            # Sin `·` entre el identificador y el nombre: en una lista es prosa,
            # y ahí el punto medio es una marca de `00·ID8`.
            partes.append(f"- [`{regla.capitulo}·{regla.id}`]"
                          f"({_enlace(regla, desde)}): {_nombre(regla)}")
    return "\n".join(partes) + "\n"


# ── Las reglas completas de cada tarea ────────────────────────────────────

def _ejemplo(regla):
    """El bloque `INCORRECTO / CORRECTO` de la regla, o `""`."""
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


def cuerpo(regla):
    """Lo que se entrega de una regla: encabezado, cuerpo y ejemplo, sin el sello."""
    partes = [regla.encabezado.strip()]
    partes += [t for _, t in regla.cuerpo]
    ejemplo = _ejemplo(regla)
    if ejemplo:
        partes.append("```\n" + ejemplo + "\n```")
    return "\n".join(p for p in partes if p).strip()


def _reubicar(texto, origen, destino):
    """Los enlaces relativos de `texto`, que resolvían desde `origen`, vistos desde `destino`.

    La regla se copia a otra carpeta: sin esto, cada enlace de su cuerpo
    quedaría roto en la copia.
    """
    def cambio(m):
        blanco = m.group(2)
        if re.match(r"^[a-z]+:", blanco) or blanco.startswith("«"):
            return m.group(0)
        ruta, _, ancla = blanco.partition("#")
        if ruta:
            absoluta = os.path.normpath(os.path.join(os.path.dirname(origen), ruta))
        else:
            absoluta = origen               # ancla del mismo archivo
        nueva = os.path.relpath(absoluta, destino).replace(os.sep, "/")
        return m.group(1) + nueva + ("#" + ancla if ancla else "") + m.group(3)
    return _ENLACE.sub(cambio, texto)


def _pieza(regla, carpeta):
    """Una regla completa, lista para el archivo de su tarea."""
    texto = _reubicar(cuerpo(regla), regla.archivo, carpeta)
    donde = _enlace(regla, carpeta)
    lineas = texto.splitlines()
    # El encabezado de la regla pasa a nivel 2 en todos los archivos.
    lineas[0] = "## " + lineas[0].lstrip("#").strip()
    return "\n".join(lineas) + f"\n\nFuente: [{regla.capitulo}·{regla.id}]({donde})\n"


def nombres_de(tarea, cuantas):
    """Los nombres de los archivos de una tarea: `tarea.md`, o `tarea-1.md`, `tarea-2.md`…"""
    if cuantas <= 1:
        return [f"{tarea}.md"]
    return [f"{tarea}-{i}.md" for i in range(1, cuantas + 1)]


def armar_por_tarea(raiz=None):
    """`{nombre de archivo: texto}` de `reglas-por-tarea/`, índice incluido."""
    raiz = raiz or RAIZ
    carpeta = os.path.join(raiz, *POR_TAREA.split("/"))
    salida, filas = {}, []
    for tarea, reglas in reglas_por_tarea(raiz).items():
        piezas = [_pieza(r, carpeta) for r in reglas]
        grupos, actual, largo = [], [], 0
        for p in piezas:
            if actual and largo + len(p) > PARTE:
                grupos.append(actual)
                actual, largo = [], 0
            actual.append(p)
            largo += len(p) + 1
        if actual or not grupos:
            grupos.append(actual)
        nombres = nombres_de(tarea, len(grupos))
        for i, (nombre, grupo) in enumerate(zip(nombres, grupos), start=1):
            parte = f", parte {i} de {len(grupos)}" if len(grupos) > 1 else ""
            cabeza = [f"# Reglas de la tarea `{tarea}`{parte}", "",
                      "Lo escribe `validadores/mapa_tareas.py` desde las reglas de "
                      "`base/`: no se edita a mano. Son las reglas que "
                      "[base/mapa-de-tareas.md](../mapa-de-tareas.md) pone "
                      "bajo esta tarea, completas. Las que llevan *opt-in* rigen "
                      "solo si el proyecto encendió su capítulo en el punto 5.1 "
                      "de su `CLAUDE.md`.", ""]
            cuerpo_ = grupo or ["Ninguna regla la declara todavía.\n"]
            salida[nombre] = "\n".join(cabeza) + "\n" + "\n".join(cuerpo_)
        filas.append((tarea, len(reglas), nombres))
    indice = ["# Las reglas de cada tarea", "",
              "El agente lee el archivo de una tarea antes de hacerla, y lo lee "
              "con la herramienta de lectura: así le llega entero. Lo escribe "
              "`validadores/mapa_tareas.py`; no se edita a mano.", "",
              "| Tarea | Reglas | Archivos |", "|---|---:|---|"]
    for tarea, n, nombres in filas:
        indice.append(f"| `{tarea}` | {n} | "
                      + ", ".join(f"[{x}]({x})" for x in nombres) + " |")
    salida["README.md"] = "\n".join(indice) + "\n"
    return salida


def archivos_de(tarea, raiz=None):
    """Las rutas absolutas de los archivos de una tarea, como están escritos."""
    raiz = raiz or RAIZ
    carpeta = os.path.join(raiz, *POR_TAREA.split("/"))
    if os.path.isfile(os.path.join(carpeta, f"{tarea}.md")):
        return [os.path.join(carpeta, f"{tarea}.md")]
    salida, i = [], 1
    while os.path.isfile(os.path.join(carpeta, f"{tarea}-{i}.md")):
        salida.append(os.path.join(carpeta, f"{tarea}-{i}.md"))
        i += 1
    return salida


def sin_lista(raiz=None):
    """Las parejas (regla, tarea) donde la tarea no está en la lista cerrada."""
    raiz = raiz or RAIZ
    lista = set(tareas(raiz))
    return [(r, t) for r in metareglas.reglas(raiz) if not r.derogada
            for t in declaradas(r) if t not in lista]


def validar(raiz=None):
    """`CA-04` y `CA-10` · Lo que no cuadra entre las reglas, la lista y lo escrito.

    Las fallas que dejan al mapa o a los archivos por tarea mintiendo: una
    regla vigente que no dice a qué tareas aplica (el agente no la encuentra),
    una tarea que la lista no trae (la regla queda fuera sin que se note), y un
    mapa o un archivo por tarea distinto del que escribiría el programa hoy
    (alguien cambió una regla y no lo volvió a escribir).

    **Donde no hay lista, no hay nada que reportar.** Un proyecto no tiene reglas
    propias en `base/`, igual que no las tiene para `ejecutable`.
    """
    raiz = raiz or RAIZ
    if not os.path.isfile(os.path.join(raiz, *TAREAS.split("/"))):
        return []
    hallazgos = []
    for regla in metareglas.reglas(raiz):
        if regla.derogada or declaradas(regla):
            continue
        hallazgos.append(Hallazgo(
            FALLA, regla.archivo, regla.linea,
            f"`{regla.capitulo}·{regla.id}` no dice a qué tareas aplica: le falta "
            f"su línea **Aplica a:**, y el agente no la encuentra en el mapa"))
    for regla, t in sin_lista(raiz):
        hallazgos.append(Hallazgo(
            FALLA, regla.archivo, regla.linea,
            f"`{regla.capitulo}·{regla.id}` nombra la tarea `{t}`, que no está "
            f"en {TAREAS}"))
    ruta = os.path.join(raiz, *MAPA.split("/"))
    actual = leer(ruta) if os.path.isfile(ruta) else ""
    if actual.replace("\r\n", "\n") != armar(raiz):
        hallazgos.append(Hallazgo(
            FALLA, ruta, 0,
            "el mapa no coincide con lo que dicen las reglas: se cambió una "
            "línea **Aplica a:** y no se volvió a correr "
            "`python validadores/mapa_tareas.py`"))
    carpeta = os.path.join(raiz, *POR_TAREA.split("/"))
    esperados = armar_por_tarea(raiz)
    for nombre, texto in esperados.items():
        ruta = os.path.join(carpeta, nombre)
        actual = leer(ruta) if os.path.isfile(ruta) else None
        if actual is None or actual.replace("\r\n", "\n") != texto:
            hallazgos.append(Hallazgo(
                FALLA, ruta, 0,
                "las reglas de esta tarea no coinciden con las de `base/`: se "
                "cambió una regla y no se volvió a correr "
                "`python validadores/mapa_tareas.py`"))
    if os.path.isdir(carpeta):
        for nombre in sorted(os.listdir(carpeta)):
            if nombre.endswith(".md") and nombre not in esperados:
                hallazgos.append(Hallazgo(
                    FALLA, os.path.join(carpeta, nombre), 0,
                    "sobra: ninguna tarea lo produce hoy; correr "
                    "`python validadores/mapa_tareas.py`"))
    return hallazgos


def escribir(raiz=None):
    """Escribe el mapa y los archivos por tarea. Devuelve la ruta del mapa."""
    raiz = raiz or RAIZ
    ruta = os.path.join(raiz, *MAPA.split("/"))
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(armar(raiz))
    carpeta = os.path.join(raiz, *POR_TAREA.split("/"))
    os.makedirs(carpeta, exist_ok=True)
    esperados = armar_por_tarea(raiz)
    for nombre in os.listdir(carpeta):
        if nombre.endswith(".md") and nombre not in esperados:
            os.remove(os.path.join(carpeta, nombre))
    for nombre, texto in esperados.items():
        with io.open(os.path.join(carpeta, nombre), "w", encoding="utf-8",
                     newline="\n") as f:
            f.write(texto)
    return ruta


def main():
    comun.preparar_salida()
    ruta = escribir()
    for regla, t in sin_lista():
        print(f"[AVISO] {regla.capitulo}·{regla.id} nombra `{t}`, "
              f"que no está en {TAREAS}")
    print(f"Mapa escrito en {comun.relativo(ruta)}, y las reglas por tarea en {POR_TAREA}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
