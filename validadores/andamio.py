# -*- coding: utf-8 -*-
"""`09·12` · Crea el esqueleto de una fase, de una historia o de un pendiente.

**Hoy esto se hace a mano y es donde se cometen los errores** que `fases.py` y
`trazabilidad.py` detectan después: el consecutivo repetido, el nombre que no
sigue el molde, el enlace que falta en uno de los dos lados. La estructura se
corrige en vez de nacer bien.

**Genera el esqueleto y nada de contenido**, que es la advertencia que trae el
propio pendiente y la más importante de todas:

> *Un generador que además rellena texto produce documentos que pasan el
> validador sin decir nada, que es la peor combinación posible.*

Por eso los marcadores `«…»` de las plantillas **se dejan intactos**: lo único
que se sustituye es lo estructural —identificadores, rutas, enlaces—, que es
justamente lo que un programa puede saber y una persona escribe mal.

**El consecutivo se calcula leyendo lo que hay**, no se pide: es lo mismo que
`fases.py` ya sabe hacer para comprobarlo, usado al revés.

**Tres alturas de la cadena, un solo programa** (`EP-007 · HU-003`, fase B):
la fase, que es la de siempre; la historia, con su fila en la épica y en el
README de la épica; y el pendiente, con su fila en el índice del backlog y su
historia en el mapa. Lo mecánico de la cadena lo hace esto; el contenido sigue
siendo de quien escribe.

**Los enlaces se trasladan al copiar** (`EP-004 · HU-005`, fase C): una
plantilla enlaza la raíz del repositorio desde su propia carpeta, y la fase
vive cinco niveles más abajo. Copiarla tal cual dejaba un enlace roto en cada
fase que se levantaba.

**Se corre solo, no por `validar.py`**, y la separación es la de siempre en esta
casa: `validar.py` es la puerta de lo que **comprueba**; esto **escribe**, como
`cerrar.py` o `historico.py`.

    python validadores/andamio.py EP-001-… HU-003-… descripcion-de-la-fase
    python validadores/andamio.py hu EP-001-… descripcion-de-la-historia
    python validadores/andamio.py pendiente descripcion --hu EP-001-…/HU-003-…
"""
import os
import re

import comun
import pendientes as _pendientes
from comun import leer

CARPETA = os.path.join("documentacion", "epicas")
PENDIENTES = "pendientes"

# Los cinco documentos de una fase (`02·F12.13`) y la plantilla de cada uno.
DOCUMENTOS = [
    ("plan_trabajo.md", os.path.join("plantillas", "planes", "trabajo.md")),
    ("plan_pruebas.md", os.path.join("plantillas", "planes", "pruebas.md")),
    ("resultado_pruebas.md", os.path.join("plantillas", "planes", "resultados.md")),
    ("estado-fase.md", os.path.join("plantillas", "estado-fase.md")),
    ("funcionalidad_implementada.md",
     os.path.join("plantillas", "funcionalidad-implementada.md")),
]
PLANTILLA_HU = os.path.join("plantillas", "HU.md")
PLANTILLA_PENDIENTE = os.path.join("plantillas", "pendiente.md")

_CONSECUTIVO = re.compile(r"^([A-Z]{1,3})(?:-[A-Z]{1,3})?-EP-")
_HU = re.compile(r"^HU-(\d+)-")
_TITULO = re.compile(r"(?m)^#\s+(.+?)\s*$")
MARCADOR_RAIZ = "«RUTA-ESTANDAR»"


def _letras(n):
    """`1 → A`, `26 → Z`, `27 → AA`. El consecutivo de `02·F12.5`."""
    salida = ""
    while n > 0:
        n, resto = divmod(n - 1, 26)
        salida = chr(ord("A") + resto) + salida
    return salida


def siguiente_consecutivo(carpeta_hu):
    """La letra que le toca a la próxima fase de esa HU.

    **Se lee lo que hay en vez de contar cuántas hay**: si existen `A` y `C`
    porque la `B` se renombró, contar daría `C` y pisaría una fase viva.
    """
    usadas = set()
    if os.path.isdir(carpeta_hu):
        for nombre in os.listdir(carpeta_hu):
            m = _CONSECUTIVO.match(nombre)
            if m and os.path.isdir(os.path.join(carpeta_hu, nombre)):
                usadas.add(m.group(1))
    n = 1
    while _letras(n) in usadas:
        n += 1
    return _letras(n)


def siguiente_hu(carpeta_epica):
    """`HU-004` si existen la 1 y la 3: el siguiente al mayor, leído del disco.

    **El siguiente al mayor, no el primer hueco**, como los pendientes: una
    historia se cita por número desde fases, pendientes y commits, y un hueco
    puede ser una historia que se movió. Las fases sí toman el primer hueco,
    porque su letra solo vive dentro de su historia.
    """
    usadas = set()
    if os.path.isdir(carpeta_epica):
        for nombre in os.listdir(carpeta_epica):
            m = _HU.match(nombre)
            if m and os.path.isdir(os.path.join(carpeta_epica, nombre)):
                usadas.add(int(m.group(1)))
    return "HU-%03d" % (max(usadas) + 1 if usadas else 1)


def _sustituciones(consecutivo, epica, hu, descripcion, nombre_fase):
    """Solo lo **estructural**. Los `«…»` de contenido no se tocan."""
    return {
        "«CONSECUTIVO»": consecutivo,
        "«EPICA»": epica,
        "«HU»": hu,
        "«FASE»": nombre_fase,
        "«DESCRIPCION-FASE»": descripcion,
    }


def _reenlazar(texto, origen_plantilla, destino, raiz):
    """Traslada a la carpeta de destino los enlaces que la plantilla hace a la raíz.

    Una plantilla en `plantillas/planes/` llega a la raíz con `../../`; la
    fase, cinco niveles abajo, necesita `../../../../../`. Solo se traslada el
    prefijo que **llega exactamente a la raíz** —un `../` que se queda en
    `plantillas/` apunta a otra cosa y no se toca—, y el marcador de la ruta
    del estándar, que el instalador rellena en los proyectos y acá no rellenaba
    nadie.
    """
    hacia_raiz = os.path.relpath(raiz, destino).replace("\\", "/")
    desde_plantilla = os.path.relpath(
        raiz, os.path.dirname(os.path.abspath(origen_plantilla))).replace("\\", "/")
    patron = re.compile(r"\]\(" + re.escape(desde_plantilla) + r"/(?!\.\.)")
    texto = patron.sub("](" + hacia_raiz + "/", texto)
    return texto.replace(MARCADOR_RAIZ, hacia_raiz)


def _escribir(ruta, texto, escribir):
    if not escribir:
        return
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def _agregar_fila(ruta, fila, despues_de, escribir):
    """Agrega `fila` al final de la primera tabla que sigue al encabezado `despues_de`.

    Si `despues_de` es None, al final de la última tabla del archivo. El
    número de columnas lo decide la cabecera real de esa tabla, no la
    plantilla: EP-005 tiene cuatro y la plantilla de épica trae seis.
    """
    texto = leer(ruta)
    inicio = 0
    if despues_de:
        m = re.search(r"(?m)^" + re.escape(despues_de) + r".*$", texto)
        if not m:
            raise ValueError("no está «%s» en %s" % (despues_de, comun.relativo(ruta)))
        inicio = m.end()
    tabla = re.compile(r"(?m)^\|.*\n(?:\|.*\n?)*")
    bloques = list(tabla.finditer(texto, inicio))
    if not bloques:
        raise ValueError("no hay tabla después de «%s» en %s"
                         % (despues_de, comun.relativo(ruta)))
    bloque = bloques[0] if despues_de else bloques[-1]
    cabecera = bloque.group(0).splitlines()[0]
    columnas = cabecera.count("|") - 1
    celdas = [c.strip() for c in fila.strip().strip("|").split("|")]
    while len(celdas) < columnas:
        celdas.append("«…»")
    fila_lista = "| " + " | ".join(celdas[:columnas]) + " |"
    cuerpo = bloque.group(0).rstrip("\n")
    nuevo = texto[:bloque.start()] + cuerpo + "\n" + fila_lista + "\n" + texto[bloque.end():]
    _escribir(ruta, nuevo, escribir)
    return fila_lista


def crear(raiz, epica, hu, descripcion, escribir=False):
    """Crea la fase y devuelve `(ruta, [archivos])`. Sin `escribir`, simula.

    `epica` y `hu` van como los nombres de sus carpetas — `EP-001-…`, `HU-003-…`.
    """
    raiz = os.path.abspath(raiz)
    carpeta_hu = os.path.join(raiz, CARPETA, epica, hu)
    if not os.path.isdir(carpeta_hu):
        raise ValueError("no existe la HU: %s" % os.path.join(CARPETA, epica, hu))

    num_ep = re.match(r"^EP-(\d+)", epica)
    num_hu = re.match(r"^HU-(\d+)", hu)
    if not num_ep or not num_hu:
        raise ValueError("la épica o la HU no siguen el molde de `02·F12`")

    consecutivo = siguiente_consecutivo(carpeta_hu)
    nombre = "%s-EP-%s-HU-%s-%s" % (consecutivo, num_ep.group(1),
                                    num_hu.group(1), descripcion)
    destino = os.path.join(carpeta_hu, nombre)

    subs = _sustituciones(consecutivo, epica, hu, descripcion, nombre)
    escritos = []
    for archivo, plantilla in DOCUMENTOS:
        origen = os.path.join(raiz, plantilla)
        if not os.path.isfile(origen):
            continue
        texto = leer(origen)
        for viejo, nuevo in subs.items():
            texto = texto.replace(viejo, nuevo)
        texto = _reenlazar(texto, origen, destino, raiz)
        escritos.append(archivo)
        _escribir(os.path.join(destino, archivo), texto, escribir)
    return destino, escritos


def _titulo_de(ruta):
    m = _TITULO.search(leer(ruta))
    return m.group(1) if m else os.path.basename(ruta)


def crear_hu(raiz, epica, descripcion, escribir=False):
    """Crea la historia con su README y sus dos filas en la épica.

    Devuelve `(ruta de la carpeta, [archivos escritos o tocados])`.
    """
    raiz = os.path.abspath(raiz)
    carpeta_epica = os.path.join(raiz, CARPETA, epica)
    epica_md = os.path.join(carpeta_epica, "epica.md")
    if not os.path.isfile(epica_md):
        raise ValueError("no existe la épica: %s" % os.path.join(CARPETA, epica))
    origen = os.path.join(raiz, PLANTILLA_HU)
    if not os.path.isfile(origen):
        raise ValueError("falta la plantilla %s" % PLANTILLA_HU)

    hu_id = siguiente_hu(carpeta_epica)
    nombre = "%s-%s" % (hu_id, descripcion)
    destino = os.path.join(carpeta_epica, nombre)
    titulo_epica = _titulo_de(epica_md)

    # Primero se trasladan los enlaces de la plantilla y después se ponen los
    # propios: al revés, el `../epica.md` recién puesto se trasladaría también.
    texto = _reenlazar(leer(origen), origen, destino, raiz)
    texto = texto.replace("HU-000", hu_id)
    texto = texto.replace("«Épica padre»", "[%s](../epica.md)" % titulo_epica)
    tocados = []
    _escribir(os.path.join(destino, nombre + ".md"), texto, escribir)
    tocados.append(os.path.join(destino, nombre + ".md"))

    readme = ("# %s\n\nContenido inmediato de esta carpeta.\n\n"
              "| Qué | De qué se trata |\n|---|---|\n"
              "| [%s.md](%s.md) | La historia de usuario: «…» |\n" % (nombre, nombre, nombre))
    _escribir(os.path.join(destino, "README.md"), readme, escribir)
    tocados.append(os.path.join(destino, "README.md"))

    _agregar_fila(epica_md, "| [%s](%s/%s.md) | «Título» | «Prioridad» | «Estimación» |"
                  % (hu_id, nombre, nombre), "## 9.", escribir)
    tocados.append(epica_md)

    readme_epica = os.path.join(carpeta_epica, "README.md")
    if os.path.isfile(readme_epica):
        _agregar_fila(readme_epica, "| [%s/%s/%s/](%s/) | Historia de usuario: «…» |"
                      % (CARPETA.replace(os.sep, "/"), epica, nombre, nombre), None, escribir)
        tocados.append(readme_epica)
    return destino, tocados


SECCION_SIN_AGRUPAR = "### Sin agrupar todavía"
MAPA = "## Ningún pendiente vive suelto"


def crear_pendiente(raiz, descripcion, hu_ref, escribir=False):
    """Crea el pendiente desde su molde, con su fila en el backlog y su historia en el mapa.

    `hu_ref` es `EP-00N-…/HU-00N-…`. Devuelve `(ruta, [archivos tocados])`.
    """
    raiz = os.path.abspath(raiz)
    epica, hu = (hu_ref.replace("\\", "/").split("/") + [""])[:2]
    carpeta_hu = os.path.join(raiz, CARPETA, epica, hu)
    hu_md = os.path.join(carpeta_hu, hu + ".md")
    if not os.path.isfile(hu_md):
        raise ValueError("no existe la historia: %s" % hu_ref)
    origen = os.path.join(raiz, PLANTILLA_PENDIENTE)
    if not os.path.isfile(origen):
        raise ValueError("falta la plantilla %s" % PLANTILLA_PENDIENTE)

    numero = _pendientes.proximo_libre(raiz)
    nombre = "%02d-%s.md" % (numero, descripcion)
    destino = os.path.join(raiz, PENDIENTES, nombre)
    ep_id = re.match(r"^EP-\d+", epica).group(0)
    hu_id = re.match(r"^HU-\d+", hu).group(0)
    titulo_hu = _titulo_de(hu_md)
    enlace_hu = "[%s · %s — %s](../%s/%s/%s/%s.md)" % (
        ep_id, hu_id, titulo_hu.split("—", 1)[-1].strip(),
        CARPETA.replace(os.sep, "/"), epica, hu, hu)

    texto = _reenlazar(leer(origen), origen, os.path.dirname(destino), raiz)
    texto = texto.replace("«HISTORIA»", enlace_hu)
    _escribir(destino, texto, escribir)
    tocados = [destino]

    indice = os.path.join(raiz, PENDIENTES, "README.md")
    if os.path.isfile(indice):
        tocados.append(indice)
        if escribir:                    # en simulación solo se dice qué se tocaría
            texto_i = leer(indice)
            if SECCION_SIN_AGRUPAR not in texto_i:
                seccion = ("%s\n\nLos que el andamio dejó acá y nadie movió todavía a su "
                           "sección. Moverlos es criterio.\n\n"
                           "| # | P | Pendiente | Qué resuelve |\n|---|---|---|---|\n\n"
                           % SECCION_SIN_AGRUPAR)
                if "---\n\n" + MAPA in texto_i:
                    texto_i = texto_i.replace("---\n\n" + MAPA, seccion + "---\n\n" + MAPA, 1)
                elif MAPA in texto_i:
                    texto_i = texto_i.replace(MAPA, seccion + MAPA, 1)
                else:
                    texto_i = texto_i.rstrip("\n") + "\n\n" + seccion
                _escribir(indice, texto_i, True)
            _agregar_fila(indice, "| %d | «P?» | [«qué falta, en una línea»](%s) | «qué resuelve» |"
                          % (numero, nombre), SECCION_SIN_AGRUPAR, True)
            _mapa(indice, ep_id, hu_id, titulo_hu, epica, hu, numero, True)
    return destino, tocados


def _mapa(indice, ep_id, hu_id, titulo_hu, epica, hu, numero, escribir):
    """La historia del pendiente queda en el mapa: se suma el número o nace la fila."""
    texto = leer(indice)
    if MAPA not in texto:
        return
    patron = re.compile(r"(?m)^\| \[%s · %s\]\([^)]*\)[^|]*\|([^|]*)\|\s*$"
                        % (re.escape(ep_id), re.escape(hu_id)))
    m = patron.search(texto)
    if m:
        numeros = m.group(1).strip()
        nueva = m.group(0).replace("| %s |" % numeros, "| %s, %d |" % (numeros, numero)) \
            if numeros else m.group(0).replace("|  |", "| %d |" % numero)
        _escribir(indice, texto[:m.start()] + nueva + texto[m.end():], escribir)
        return
    fila = "| [%s · %s](../%s/%s/%s/%s.md) — %s | %d |" % (
        ep_id, hu_id, CARPETA.replace(os.sep, "/"), epica, hu, hu,
        titulo_hu.split("—", 1)[-1].strip(), numero)
    _agregar_fila(indice, fila, MAPA, escribir)


def main():
    """`09·12` · el andamio se pide, no se ejecuta solo."""
    import argparse
    import sys
    comun.preparar_salida()             # imprime «·» y «…»: sin esto, mojibake
    modo = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] in ("hu", "pendiente") else "fase"
    p = argparse.ArgumentParser(
        description="Crea el esqueleto de una fase, una historia o un pendiente. "
                    "No escribe contenido: los marcadores «…» quedan para llenarse.")
    if modo == "hu":
        p.add_argument("modo")
        p.add_argument("epica", help="carpeta de la épica, p. ej. EP-001-cuerpo-de-reglas")
        p.add_argument("descripcion", help="qué pide la historia, en minúsculas con guiones")
    elif modo == "pendiente":
        p.add_argument("modo")
        p.add_argument("descripcion", help="qué falta, en minúsculas con guiones")
        p.add_argument("--hu", required=True, help="EP-001-…/HU-003-…: la historia que lo recibe")
    else:
        p.add_argument("epica", help="carpeta de la épica, p. ej. EP-001-cuerpo-de-reglas")
        p.add_argument("hu", help="carpeta de la HU, p. ej. HU-003-nucleo")
        p.add_argument("descripcion", help="qué hace la fase, en minúsculas con guiones")
    p.add_argument("--raiz", default=comun.RAIZ)
    p.add_argument("--aplicar", action="store_true",
                   help="escribe de verdad; sin esto solo dice qué crearía")
    a = p.parse_args()

    if modo == "hu":
        destino, tocados = crear_hu(a.raiz, a.epica, a.descripcion, a.aplicar)
    elif modo == "pendiente":
        destino, tocados = crear_pendiente(a.raiz, a.descripcion, a.hu, a.aplicar)
    else:
        destino, tocados = crear(a.raiz, a.epica, a.hu, a.descripcion, a.aplicar)
    marca = "creada" if a.aplicar else "simulado; agrega --aplicar"
    print("%s  (%s)" % (comun.relativo(destino), marca))
    for e in tocados:
        print("  · %s" % (e if modo == "fase" else comun.relativo(e)))
    print("\nLos marcadores «…» quedan sin llenar a propósito: el andamio no "
          "escribe contenido.")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
