# -*- coding: utf-8 -*-
"""El conteo por regla al terminar la corrida completa (EP-004 · HU-009)."""
import io, os
os.chdir(r"c:\Ing. Jose\ia\agente")

# 1 · El módulo que guarda y compara.
io.open("validadores/conteo.py", "w", encoding="utf-8", newline="\n").write('''# -*- coding: utf-8 -*-
"""`EP-004 · HU-009` · Por cuál regla se incumple más.

**Para qué.** Una regla que produce cien hallazgos por semana no es un equipo
descuidado: casi siempre es una regla mal escrita, o una que hace falta
automatizar. Sin el número, esa conversación es opinión contra opinión.

**Qué se guarda, y qué no.** Solo el identificador de la regla y **cuántas
veces**. Nunca el texto del hallazgo ni la línea del archivo: en un mensaje de
incumplimiento viaja el contenido revisado, y ahí puede ir una clave o un dato
personal ([`00·N6`](../base/00-nucleo-blindado.md), [`12·PR4`](../base/12-privacidad-datos.md)).
El registro es un recuento, no una copia de lo revisado.

**Dónde vive.** En `metricas/`, **fuera del control de versiones**: es
generado, y [`09·G3`](../base/09-git.md) deja fuera lo generado. El precedente
es `plantillas/proyectos.md`, que se exporta y no se versiona.

**Una línea por corrida**, con su fecha, su versión y su recuento. Así dos
corridas se comparan sin guardar nada más.
"""
import io
import json
import os

import comun

REGISTRO = os.path.join("metricas", "conteo-por-regla.jsonl")


def _ruta(raiz=None):
    return os.path.join(os.path.abspath(raiz or comun.RAIZ), *REGISTRO.split(os.sep))


def version_del(raiz=None):
    """La versión del estándar en el momento de la corrida, o "" si no hay."""
    ruta = os.path.join(os.path.abspath(raiz or comun.RAIZ), "VERSION")
    if not os.path.isfile(ruta):
        return ""
    return (comun.leer(ruta).strip().splitlines() or [""])[0].strip()


def anotar(hallazgos, raiz=None, cuando="", version=""):
    """Agrega la línea de esta corrida y devuelve lo que anotó.

    `cuando` y `version` se reciben en vez de mirarse acá: quien corre sabe qué
    hora es y contra qué versión midió, y una función que lee el reloj no se
    puede probar dos veces con el mismo resultado.
    """
    fila = {
        "cuando": cuando,
        "version": version or version_del(raiz),
        "conteo": comun.conteo_por_regla(hallazgos),
        "total": len(list(hallazgos)),
    }
    ruta = _ruta(raiz)
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with io.open(ruta, "a", encoding="utf-8", newline="\\n") as f:
        f.write(json.dumps(fila, ensure_ascii=False, sort_keys=True) + "\\n")
    return fila


def corridas(raiz=None):
    """Lo anotado, de la más vieja a la más nueva. Una línea rota se salta."""
    ruta = _ruta(raiz)
    if not os.path.isfile(ruta):
        return []
    salida = []
    for linea in comun.leer(ruta).splitlines():
        linea = linea.strip()
        if not linea:
            continue
        try:
            salida.append(json.loads(linea))
        except ValueError:
            continue          # una línea rota no se lleva el registro entero
    return salida


def comparar(raiz=None):
    """Qué cambió entre las dos últimas corridas: `[(regla, antes, ahora)]`."""
    hechas = corridas(raiz)
    if len(hechas) < 2:
        return []
    antes, ahora = hechas[-2]["conteo"], hechas[-1]["conteo"]
    reglas = sorted(set(antes) | set(ahora))
    return [(r, antes.get(r, 0), ahora.get(r, 0)) for r in reglas
            if antes.get(r, 0) != ahora.get(r, 0)]


def lineas_del_conteo(hallazgos, raiz=None):
    """Lo que se imprime al terminar la corrida: el conteo y qué cambió."""
    cuenta = comun.conteo_por_regla(hallazgos)
    if not cuenta:
        return ["Ningún hallazgo que contar."]
    orden = sorted(cuenta.items(), key=lambda kv: (-kv[1], kv[0]))
    salida = ["Hallazgos por regla (%d en total):" % sum(cuenta.values())]
    for regla, cuantos in orden[:10]:
        salida.append("  %-12s %d" % (regla, cuantos))
    if len(orden) > 10:
        salida.append("  (y %d regla(s) más con menos hallazgos)" % (len(orden) - 10))
    cambios = comparar(raiz)
    if cambios:
        salida.append("Cambió desde la corrida anterior:")
        for regla, antes, ahora in cambios[:10]:
            flecha = "baja" if ahora < antes else "sube"
            salida.append("  %-12s %d → %d  (%s)" % (regla, antes, ahora, flecha))
    return salida


if __name__ == "__main__":
    comun.no_es_punto_de_entrada("todo")
''')

# 2 · Engancharlo en la corrida completa.
p = "validadores/validar.py"
s = io.open(p, encoding="utf-8").read()
s = s.replace("import comun", "import comun\nimport conteo", 1) if "import conteo" not in s else s
a = '''    print("== Corrida completa · %s ==" % relativo(os.path.abspath(a.raiz)))'''
assert a in s
nuevo = '''    print("== Corrida completa · %s ==" % relativo(os.path.abspath(a.raiz)))'''
s = s.replace(a, nuevo, 1)

b = '''    if not con_falla:
        print("Sin fallas. Los avisos de cada comprobación salen arriba.")
    return 1 if peor else 0'''
c = '''    if not con_falla:
        print("Sin fallas. Los avisos de cada comprobación salen arriba.")

    # `EP-004·HU-009` · El conteo por regla, que es lo que dice **qué regla
    # cambiar**. Se anota una línea por corrida, fuera del control de
    # versiones, con el identificador y el número: nunca el texto del hallazgo.
    if getattr(a, "conteo", True):
        todos = []
        for nombre, _, _ in resumen:
            todos += _hallazgos_de.get(nombre, [])
        if todos:
            conteo.anotar(todos, a.raiz, cuando=ahora, version=conteo.version_del(a.raiz))
            print()
            for linea in conteo.lineas_del_conteo(todos, a.raiz):
                print(linea)
    return 1 if peor else 0'''
assert b in s
s = s.replace(b, c, 1)
io.open(p, "w", encoding="utf-8", newline="").write(s)
print("escrito (falta recoger los hallazgos)")
