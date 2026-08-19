# -*- coding: utf-8 -*-
"""`EP-001 · HU-012` · El inventario de acciones no tiene huecos.

**Qué comprueba.** Que cada clase de acción del anexo traiga **su nivel y su
ejemplo**, que el nivel sea uno de los tres de la escala, y que ninguna de las
herramientas que el agente tiene se haya quedado sin clase.

**Qué no comprueba, y se declara.** Que la clasificación sea la **acertada**.
Que borrar un archivo no versionado merezca el nivel más alto y no el del medio
es un juicio, y se discute leyendo. Un programa que opinara de eso estaría
inventando criterio.

**Por qué importa que esté completa.** El anexo existe para que un plan aprobado
cubra lo reversible y **nunca** lo irreversible. Una clase sin nivel deja esa
distinción sin decidir justo donde hace falta.
"""
import os
import re

import comun
from comun import FALLA, Hallazgo, leer

ANEXO = os.path.join("base", "00-identidad-y-rol", "acciones-y-riesgo.md")

# La escala es **cerrada**: tres valores y ninguno más. Si fuera texto libre,
# cada clase se clasificaría con su propia palabra y no habría comparación
# posible — que es justo lo que el anexo viene a arreglar.
ESCALA = ("🟢", "🟡", "🔴")

# Las diez que la historia enumera en su `CA-01`. Se buscan por una palabra
# suya, no por la frase entera: el anexo las nombra con sus palabras y no con
# las de la historia, y exigir la frase literal sería comprobar la redacción.
HERRAMIENTAS = {
    "leer": ("Leer",),
    "escribir en el repositorio": ("Escribir un archivo del repositorio",),
    "borrar": ("Borrar algo versionado", "Borrar algo NO versionado"),
    "comando local": ("Correr un comando local",),
    "salir a la red": ("Correr algo que sale a la red",),
    "control de versiones": ("Guardar en el control de versiones",
                             "Publicar o reescribir la historia"),
    "datos": ("Tocar datos reales",),
    "fuera del repositorio": ("Tocar la máquina fuera del repositorio",),
    "histórico": ("Escribir en el histórico",),
    "memoria": ("Escribir en la memoria",),
}

_FILA = re.compile(r"(?m)^\|\s*\*\*(.+?)\*\*\s*\|(.*?)\|(.*?)\|(.*?)\|")


def _ruta(raiz):
    return os.path.join(raiz or comun.RAIZ, *ANEXO.split(os.sep))


def clases(raiz=None):
    """`[(clase, nivel, ejemplo)]` de la tabla del anexo."""
    archivo = _ruta(raiz)
    if not os.path.isfile(archivo):
        return []
    salida = []
    for m in _FILA.finditer(leer(archivo)):
        nombre = m.group(1).strip()
        nivel = m.group(3).strip()
        ejemplo = m.group(4).strip()
        # La cabecera de la tabla y la fila de la escala no son clases.
        if nombre.startswith("Nivel") or "Qué incluye" in m.group(2):
            continue
        salida.append((nombre, nivel, ejemplo))
    return salida


def validar(raiz=None):
    """Los tres huecos que dejan la tabla sin servir."""
    raiz = raiz or comun.RAIZ
    archivo = _ruta(raiz)
    if not os.path.isfile(archivo):
        return [Hallazgo(FALLA, archivo, 0,
                         "falta el anexo de acciones y riesgo — sin él, `00·N1` "
                         "trata igual la coma del README y el borrado de la base")]

    hallazgos = []
    filas = clases(raiz)

    for nombre, nivel, ejemplo in filas:
        puestos = [e for e in ESCALA if e in nivel]
        if not puestos:
            hallazgos.append(Hallazgo(
                FALLA, archivo, 0,
                f"«{nombre}» tiene el nivel «{nivel}», que no es de la escala — "
                f"la escala es cerrada, si no no se pueden comparar dos clases"))
        elif len(puestos) > 1:
            # **Una fila con dos niveles es dos clases sin partir.** Se coló una
            # al construir el anexo —«🔴 para push, 🟡 el resto»— y la primera
            # versión de esta comprobación la dio por buena: miraba si había
            # *algún* nivel de la escala, no si había **uno**.
            hallazgos.append(Hallazgo(
                FALLA, archivo, 0,
                f"«{nombre}» pone {len(puestos)} niveles en la misma fila — "
                f"son dos clases sin partir, y así no se puede decir qué exige"))
        if not ejemplo:
            hallazgos.append(Hallazgo(
                FALLA, archivo, 0,
                f"«{nombre}» tiene nivel y **no tiene ejemplo** — el nivel solo "
                f"se discute; el ejemplo es lo que lo hace entender"))

    # Ninguna herramienta sin clase. Es el `CA-01`, y sin este recuento el
    # anexo puede estar bien formado y no cubrir lo que hace falta.
    #
    # **Se busca en los nombres de las clases, no en el texto entero.** La
    # primera versión miraba todo el archivo, y una clase borrada de la tabla
    # seguía «encontrada» porque su nombre aparecía en otra sección — la de las
    # masivas la nombra de ejemplo. Lo cazó su propio caso de prueba.
    nombres = chr(10).join(n for n, _niv, _ej in filas)
    for herramienta, marcas in sorted(HERRAMIENTAS.items()):
        if not any(m in nombres for m in marcas):
            hallazgos.append(Hallazgo(
                FALLA, archivo, 0,
                f"«{herramienta}» no tiene clase en el anexo — el agente puede "
                f"hacerlo y nada dice qué cuesta deshacerlo"))

    return hallazgos


def linea_resumen(raiz=None):
    """Cuántas clases hay y cómo se reparten. Va aunque no haya hallazgos."""
    filas = clases(raiz)
    if not filas:
        return ""
    cuenta = {e: sum(1 for _n, niv, _ej in filas if e in niv) for e in ESCALA}
    return ("Clases de acción: %d · 🟢 %d se deshacen solas · 🟡 %d con trabajo "
            "· 🔴 %d no se deshacen"
            % (len(filas), cuenta["🟢"], cuenta["🟡"], cuenta["🔴"]))


if __name__ == "__main__":
    comun.no_es_punto_de_entrada("acciones")
