#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cierra un pendiente: lo mueve a `pendientes/hecho/` y arrastra sus citas.

**El problema que resuelve.** El backlog se cita a sí mismo todo el tiempo, y
también lo citan las fases, los resúmenes y el índice. Mover un archivo a
`hecho/` deja apuntando al vacío a todos ellos, y hasta hoy se corregían a mano.

Se midió dos veces y empeora:

| Cuándo | Qué se cerró | Enlaces rotos |
|---|---|---|
| 2026-08-16 | el pendiente 35 | 12 |
| 2026-08-17 | el pendiente 53 | **54** |

Los 54 estaban repartidos en doce fases de cuatro épicas, dos resúmenes de
sesión, el índice del backlog y el propio documento de cierre que se acababa de
escribir. Corregir eso a mano, justo cuando uno está terminando algo, es la
clase de trabajo que se hace mal.

**Cómo lo resuelve.** No busca texto: resuelve cada enlace contra el disco y
compara rutas absolutas. Un enlace apunta al pendiente que se mueve o no
apunta, y eso no depende de cuántos `../` lleve delante ni de desde qué carpeta
se escribió. Después reescribe el destino recalculando la ruta relativa desde
el archivo que lo cita.

**Simula por omisión.** Sin `--aplicar` dice qué haría y no toca nada, igual
que `citas.py`. Mover archivos y reescribir enlaces en decenas de documentos no
es algo que deba pasar por escribir mal un comando.

Uso:
  python validadores/cerrar.py 53 --como ningun-validador-termina-en-silencio
  python validadores/cerrar.py 53 --como ningun-validador-termina-en-silencio --aplicar
"""
import argparse
import os
import shutil
import sys
from urllib.parse import unquote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from comun import (EXCLUIDAS, RAIZ, enlaces, leer, preparar_salida,  # noqa: E402
                   relativo)

PENDIENTES = "pendientes"
HECHO = "hecho"


def archivo_del_pendiente(raiz, numero):
    """El `.md` cuyo nombre empieza por ese número. Uno solo, o se avisa."""
    carpeta = os.path.join(raiz, PENDIENTES)
    prefijo = "%02d-" % int(numero)
    candidatos = [n for n in sorted(os.listdir(carpeta))
                  if n.startswith(prefijo) and n.lower().endswith(".md")]
    if not candidatos:
        sys.exit(f"no hay ningún pendiente {prefijo}* en {relativo(carpeta)}")
    if len(candidatos) > 1:
        sys.exit(f"hay {len(candidatos)} archivos con el número {numero}: "
                 + ", ".join(candidatos))
    return os.path.join(carpeta, candidatos[0])


def _resuelve_a(archivo, destino):
    """La ruta absoluta a la que apunta un enlace, o None si no es de disco.

    El `unquote` no es un detalle: un enlace a un archivo con espacios se
    escribe con `%20`, y sin decodificarlo la comparación falla siempre. Es el
    punto 1 del pendiente 33, que acá haría que un enlace no se arrastrara.
    """
    if destino.startswith(("http://", "https://", "mailto:", "#", "//")):
        return None
    ruta = unquote(destino.split("#", 1)[0])
    if not ruta:
        return None
    return os.path.normpath(os.path.join(os.path.dirname(archivo), ruta))


def _md_del_repositorio(raiz):
    for carpeta, subcarpetas, archivos in os.walk(raiz):
        subcarpetas[:] = [s for s in subcarpetas if s not in EXCLUIDAS]
        for nombre in sorted(archivos):
            if nombre.lower().endswith(".md"):
                yield os.path.join(carpeta, nombre)


def citas_a(raiz, objetivo):
    """Todo enlace del repositorio que apunta a `objetivo`.

    Devuelve `[(archivo, linea, destino_escrito)]`.
    """
    objetivo = os.path.normpath(objetivo)
    encontrados = []
    for archivo in _md_del_repositorio(raiz):
        for n, _texto, destino in enlaces(leer(archivo)):
            if _resuelve_a(archivo, destino) == objetivo:
                encontrados.append((archivo, n, destino))
    return encontrados


def _nuevo_destino(desde, nuevo_absoluto, destino_viejo):
    """La ruta relativa al archivo movido, conservando el ancla si la había."""
    rel = os.path.relpath(nuevo_absoluto,
                          os.path.dirname(desde)).replace("\\", "/")
    ancla = destino_viejo.split("#", 1)
    return rel + ("#" + ancla[1] if len(ancla) > 1 else "")


def reescribir_salientes(texto, origen, destino):
    """Recalcula los enlaces **de dentro** del archivo que se mueve.

    Mover un pendiente a `hecho/` lo baja un nivel, así que todos sus `../`
    quedan cortos: `../base/…` pasa a apuntar a `pendientes/base/…`, que no
    existe. Se descubrió cerrando el 53 — el archivo llegó a su sitio con
    ocho enlaces rotos hacia afuera.

    Es el mismo defecto que esta herramienta arregla, visto del otro lado: no
    solo hay que arrastrar a **quien cita** al archivo, sino lo que **el
    archivo cita**.
    """
    viejo_dir = os.path.dirname(origen)
    nuevo_dir = os.path.dirname(destino)
    if os.path.normpath(viejo_dir) == os.path.normpath(nuevo_dir):
        return texto, 0

    cambios = 0
    for _n, _t, d in enlaces(texto):
        absoluto = _resuelve_a(origen, d)
        if absoluto is None or not os.path.exists(absoluto):
            continue                      # externo, ancla, o ya roto de antes
        nuevo = _nuevo_destino(destino, absoluto, d)
        if nuevo == d:
            continue
        cuenta = texto.count("](" + d + ")")
        if cuenta:
            texto = texto.replace("](" + d + ")", "](" + nuevo + ")")
            cambios += cuenta
    return texto, cambios


def cerrar(raiz, numero, como, escribir=False):
    """Mueve el pendiente a `hecho/<como>.md` y reescribe lo que lo citaba.

    Devuelve `(origen, destino, [(archivo, cuántos enlaces)])`.
    """
    origen = archivo_del_pendiente(raiz, numero)
    nombre = como if como.lower().endswith(".md") else como + ".md"
    destino = os.path.join(raiz, PENDIENTES, HECHO, nombre)

    if os.path.exists(destino):
        sys.exit(f"ya existe {relativo(destino)} — elegí otro nombre")

    pendientes_de_arreglar = citas_a(raiz, origen)

    # Se agrupa por archivo para reescribir cada uno una sola vez.
    por_archivo = {}
    for archivo, _n, viejo in pendientes_de_arreglar:
        por_archivo.setdefault(archivo, []).append(viejo)

    # El que se mueve entra siempre, aunque no se cite a sí mismo: sus
    # enlaces de salida hay que recalcularlos igual.
    por_archivo.setdefault(origen, [])

    tocados = []
    texto_movido = None
    for archivo, viejos in sorted(por_archivo.items()):
        texto = leer(archivo)
        # El propio archivo que se mueve cambia de sitio: sus enlaces se
        # recalculan desde el destino, no desde donde estaba.
        base = destino if archivo == origen else archivo
        cambios = 0
        for viejo in sorted(set(viejos), key=len, reverse=True):
            nuevo = _nuevo_destino(base, destino, viejo)
            if nuevo == viejo:
                continue
            cuenta = texto.count("](" + viejo + ")")
            if cuenta:
                texto = texto.replace("](" + viejo + ")", "](" + nuevo + ")")
                cambios += cuenta

        if archivo == origen:
            texto, salientes = reescribir_salientes(texto, origen, destino)
            cambios += salientes
            texto_movido = texto

        if cambios:
            tocados.append((archivo, cambios))
            if escribir and archivo != origen:
                with open(archivo, "w", encoding="utf-8", newline="\n") as f:
                    f.write(texto)

    if escribir:
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        shutil.move(origen, destino)
        if texto_movido is not None:
            with open(destino, "w", encoding="utf-8", newline="\n") as f:
                f.write(texto_movido)

    return origen, destino, tocados


def main():
    preparar_salida()
    p = argparse.ArgumentParser(
        description="Cierra un pendiente moviéndolo a hecho/ sin romper sus citas.")
    p.add_argument("numero", help="el número del pendiente, p. ej. 53")
    p.add_argument("--como", required=True,
                   help="nombre del archivo en hecho/, sin la extensión")
    p.add_argument("--raiz", default=RAIZ)
    p.add_argument("--aplicar", action="store_true",
                   help="escribe de verdad; sin esto solo simula")
    a = p.parse_args()

    raiz = os.path.abspath(a.raiz)
    origen, destino, tocados = cerrar(raiz, a.numero, a.como, a.aplicar)

    print(f"{relativo(origen)}\n  -> {relativo(destino)}\n")
    total = sum(c for _, c in tocados)
    for archivo, cuenta in tocados:
        print(f"  {cuenta:>3} enlace(s)  {relativo(archivo)}")
    print(f"\n{total} enlace(s) en {len(tocados)} archivo(s)"
          f"{' — ESCRITO' if a.aplicar else ' (simulado; agrega --aplicar)'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
