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

# Una fila de la tabla de `base/tareas.md`: `| \`recibir-pedido\` | … |`.
_TAREA = re.compile(r"^\|\s*`([a-z][a-z-]*)`\s*\|")
_APLICA = re.compile(r"(?m)^\*\*Aplica a:\*\*\s*(.+?)\s*$")
# La marca del encabezado no es parte del nombre de la regla.
_MARCA = re.compile(r"\s*(`\[[^\]]+\]`|\*opt-in\*)\s*$")


def tareas(raiz=None):
    """Los nombres de la lista cerrada, en el orden en que la lista los trae."""
    ruta = os.path.join(raiz or RAIZ, *TAREAS.split("/"))
    nombres = []
    for linea in leer(ruta).splitlines():
        m = _TAREA.match(linea.strip())
        if m:
            nombres.append(m.group(1))
    return nombres


def palabras(raiz=None):
    """`{tarea: {palabras}}` de la tercera columna de la lista.

    La tarea que dice `siempre` va con el conjunto vacío y figura en
    `siempre()`: no la señala ninguna palabra porque va en todo mensaje.
    """
    ruta = os.path.join(raiz or RAIZ, *TAREAS.split("/"))
    salida = {}
    for linea in leer(ruta).splitlines():
        m = _TAREA.match(linea.strip())
        if not m:
            continue
        celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
        texto = celdas[2] if len(celdas) > 2 else ""
        salida[m.group(1)] = {p.strip().lower() for p in texto.split(",")
                              if p.strip() and p.strip().lower() != "siempre"}
    return salida


def siempre(raiz=None):
    """Las tareas que van en todo mensaje: su columna de palabras dice `siempre`."""
    ruta = os.path.join(raiz or RAIZ, *TAREAS.split("/"))
    salida = []
    for linea in leer(ruta).splitlines():
        m = _TAREA.match(linea.strip())
        if m and linea.strip().rstrip("|").strip().endswith("siempre"):
            salida.append(m.group(1))
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
    """La ruta a la regla, relativa a la carpeta del mapa, con su ancla."""
    ruta = os.path.relpath(regla.archivo, desde).replace(os.sep, "/")
    if regla.nivel == 1:
        return ruta                     # la regla ocupa su archivo entero
    return ruta + "#" + citas.ancla(f"{regla.id} · {regla.titulo}")


def armar(raiz=None):
    """El texto del mapa: cada tarea de la lista con las reglas que la declaran."""
    raiz = raiz or RAIZ
    lista = tareas(raiz)
    por_tarea = {t: [] for t in lista}
    for regla in metareglas.reglas(raiz):
        if regla.derogada:
            continue
        for t in declaradas(regla):
            if t in por_tarea:
                por_tarea[t].append(regla)
    desde = os.path.dirname(os.path.join(raiz, *MAPA.split("/")))
    partes = [
        "# Mapa de tareas",
        "",
        "Qué reglas se leen antes de cada tarea. Lo escribe "
        "`validadores/mapa_tareas.py` leyendo la línea `**Aplica a:**` de cada "
        "regla: no se edita a mano. Para cambiarlo se cambia la regla y se vuelve "
        "a correr el programa.",
        "",
        "Las tareas son las de [base/tareas.md](tareas.md).",
    ]
    for t in lista:
        partes += ["", f"## `{t}`", ""]
        if not por_tarea[t]:
            partes.append("Ninguna regla la declara todavía.")
            continue
        for regla in por_tarea[t]:
            # En el encabezado de la regla, la raya larga y el punto medio son
            # notación permitida; en una lista son prosa y marca de `00·ID8`.
            # El mapa los escribe con coma, y la regla no cambia.
            nombre = _MARCA.sub("", regla.titulo)
            nombre = re.sub(r"\s*[—·]\s*$", "", nombre)   # la que precedía a la marca
            nombre = re.sub(r"\s+[—·]\s+", ", ", nombre)
            # Sin `·` entre el identificador y el nombre: en una lista es prosa,
            # y ahí el punto medio es una marca de `00·ID8`.
            partes.append(f"- [`{regla.capitulo}·{regla.id}`]"
                          f"({_enlace(regla, desde)}): {nombre}")
    return "\n".join(partes) + "\n"


def sin_lista(raiz=None):
    """Las parejas (regla, tarea) donde la tarea no está en la lista cerrada."""
    raiz = raiz or RAIZ
    lista = set(tareas(raiz))
    return [(r, t) for r in metareglas.reglas(raiz) if not r.derogada
            for t in declaradas(r) if t not in lista]


def validar(raiz=None):
    """`CA-04` · Lo que no cuadra entre las reglas, la lista y el mapa.

    Tres fallas, las tres que dejan al mapa mintiendo: una regla vigente que no
    dice a qué tareas aplica (el agente no la encuentra), una tarea que la lista
    no trae (la regla queda fuera del mapa sin que se note) y un mapa distinto
    del que armaría el programa hoy (alguien cambió una regla y no lo volvió a
    escribir).

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
    return hallazgos


def escribir(raiz=None):
    """Escribe el mapa y devuelve su ruta."""
    raiz = raiz or RAIZ
    ruta = os.path.join(raiz, *MAPA.split("/"))
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(armar(raiz))
    return ruta


def main():
    comun.preparar_salida()
    ruta = escribir()
    for regla, t in sin_lista():
        print(f"[AVISO] {regla.capitulo}·{regla.id} nombra `{t}`, "
              f"que no está en {TAREAS}")
    print(f"Mapa escrito en {comun.relativo(ruta)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
